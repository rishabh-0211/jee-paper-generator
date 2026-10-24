# JEE Main Mathematics - Sequences and Series

## Topic 1: Arithmetic Progression

**Total Questions:** 110

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha = 3+4+8+9+13+14+\ldots$ upto 40 terms. If $(\tan\beta)^{\frac{\alpha}{1020}}$ is a root of the equation $x^2+x-2=0$, $\beta \in \left(0, \dfrac{\pi}{2}\right)$, then $\sin^2\beta + 3\cos^2\beta$ is equal to:

**Options:**

- **(A)** $2$
- **(B)** $\dfrac{7}{4}$
- **(C)** $\dfrac{5}{2}$
- **(D)** $\dfrac{3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2$**

**Detailed Solution:**

The given series is $\alpha = 3+4+8+9+13+14+\ldots$ up to $40$ terms.

We can split the series into two arithmetic progressions, each containing $20$ terms:

$S_1 = 3 + 8 + 13 + \ldots$ up to $20$ terms

$S_2 = 4 + 9 + 14 + \ldots$ up to $20$ terms

Using the sum formula for an AP, $S_n = \dfrac{n}{2}[2a + (n-1)d]$:

$S_1 = \dfrac{20}{2}[2(3) + (20-1)5] = 10[6 + 95] = 1010$

$S_2 = \dfrac{20}{2}[2(4) + (20-1)5] = 10[8 + 95] = 1030$

Therefore, $\alpha = S_1 + S_2 = 1010 + 1030 = 2040$.

The exponent in the given expression is $\dfrac{\alpha}{1020} = \dfrac{2040}{1020} = 2$.

Thus, $(\tan\beta)^2 = \tan^2\beta$ is a root of the equation $x^2+x-2=0$.

Solving $x^2+x-2=0$ gives $(x+2)(x-1)=0 \Rightarrow x = -2$ or $x = 1$.

Since $\tan^2\beta \ge 0$, we must have $\tan^2\beta = 1$.

Given $\beta \in \left(0, \dfrac{\pi}{2}\right)$, $\tan\beta = 1 \Rightarrow \beta = \dfrac{\pi}{4}$.

We need to find the value of $\sin^2\beta + 3\cos^2\beta$.

Substituting $\beta = \dfrac{\pi}{4}$:

$\sin^2\left(\dfrac{\pi}{4}\right) + 3\cos^2\left(\dfrac{\pi}{4}\right) = \left(\dfrac{1}{\sqrt{2}}\right)^2 + 3\left(\dfrac{1}{\sqrt{2}}\right)^2 = \dfrac{1}{2} + \dfrac{3}{2} = 2$.

Answer: $2$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A_1, A_2, A_3, \ldots, A_{39}$ be $39$ arithmetic means between the numbers $59$ and $159$. Then the mean of $A_{25}, A_{28}, A_{31}$ and $A_{36}$ is equal to :

**Options:**

- **(A)** $129$
- **(B)** $136$
- **(C)** $131.50$
- **(D)** $134$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $134$**

**Detailed Solution:**

The sequence $59, A_1, A_2, \ldots, A_{39}, 159$ forms an arithmetic progression with $41$ terms.

The common difference $d$ is given by $d = \dfrac{159 - 59}{39 + 1} = \dfrac{100}{40} = 2.5$

The $k$-th arithmetic mean is $A_k = 59 + k \cdot d$

The required mean is $\dfrac{A_{25} + A_{28} + A_{31} + A_{36}}{4}$

$\dfrac{A_{25} + A_{28} + A_{31} + A_{36}}{4} = \dfrac{(59 + 25d) + (59 + 28d) + (59 + 31d) + (59 + 36d)}{4}$

$= \dfrac{4 \times 59 + 120d}{4} = 59 + 30d$

Substituting $d = 2.5$:

$= 59 + 30(2.5) = 59 + 75 = 134$

Answer: $134$

</details>

---

### Q3. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the sum of the first $n$ terms of an A.P. be $3n^2 + 5n$. Then the sum of squares of the first $10$ terms of the A.P. is:

**Options:**

- **(A)** $10220$
- **(B)** $12860$
- **(C)** $15220$
- **(D)** $19780$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $15220$**

**Detailed Solution:**

Given the sum of the first $n$ terms of the A.P. is $S_n = 3n^2 + 5n$.

The $n$-th term of the A.P. is given by:

$T_n = S_n - S_{n-1}$

$T_n = (3n^2 + 5n) - [3(n-1)^2 + 5(n-1)]$

$T_n = 3n^2 + 5n - [3(n^2 - 2n + 1) + 5n - 5]$

$T_n = 3n^2 + 5n - (3n^2 - 6n + 3 + 5n - 5)$

$T_n = 6n + 2$

We need to find the sum of the squares of the first $10$ terms:

$\sum_{n=1}^{10} T_n^2 = \sum_{n=1}^{10} (6n + 2)^2$

$\sum_{n=1}^{10} T_n^2 = \sum_{n=1}^{10} (36n^2 + 24n + 4)$

$\sum_{n=1}^{10} T_n^2 = 36 \sum_{n=1}^{10} n^2 + 24 \sum_{n=1}^{10} n + \sum_{n=1}^{10} 4$

Using the formulas for the sum of squares and sum of first $n$ natural numbers:

$\sum_{n=1}^{10} T_n^2 = 36 \left( \dfrac{10 \times 11 \times 21}{6} \right) + 24 \left( \dfrac{10 \times 11}{2} \right) + 4 \times 10$

$\sum_{n=1}^{10} T_n^2 = 36(385) + 24(55) + 40$

$\sum_{n=1}^{10} T_n^2 = 13860 + 1320 + 40 = 15220$

Answer: $15220$

</details>

---

### Q4. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The first term of an A.P. of $30$ non-negative terms is $\dfrac{10}{3}$. If the sum of this A.P. is the cube of its last term, then its common difference is:

**Options:**

- **(A)** $\dfrac{5}{87}$
- **(B)** $\dfrac{25}{83}$
- **(C)** $\dfrac{15}{29}$
- **(D)** $\dfrac{5}{29}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{5}{87}$**

**Detailed Solution:**

Given $a = \dfrac{10}{3}$ and $n = 30$.

Let the last term be $l$ and the common difference be $d$.

The sum of the A.P. is given by $S_{30} = \dfrac{30}{2}(a + l) = 15\left(\dfrac{10}{3} + l\right)$.

According to the given condition, $S_{30} = l^3$.

$15\left(\dfrac{10}{3} + l\right) = l^3$

$50 + 15l = l^3$

$l^3 - 15l - 50 = 0$

$(l - 5)(l^2 + 5l + 10) = 0$

Since $l^2 + 5l + 10 = 0$ has no real roots, we get $l = 5$.

The last term of the A.P. is $l = a + 29d$.

$\dfrac{10}{3} + 29d = 5$

$29d = 5 - \dfrac{10}{3} = \dfrac{5}{3}$

$d = \dfrac{5}{87}$

Answer: $\dfrac{5}{87}$

</details>

---

### Q5. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $a_1, a_2, a_3, \ldots$ be an A.P. and $g_1 = a_1, g_2, g_3, \ldots$ be an increasing G.P. If $a_1 = a_2 + g_2 = 1$ and $a_3 + g_3 = 4$, then $a_{10} + g_5$ is equal to:

**Options:**

- **(A)** $81$
- **(B)** $76$
- **(C)** $62$
- **(D)** $55$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $55$**

**Detailed Solution:**

Let the common difference of the A.P. be $d$ and the common ratio of the G.P. be $r$.

Given $a_1 = 1$ and $g_1 = a_1 = 1$.

From $a_2 + g_2 = 1$, we have:
$(a_1 + d) + g_1 r = 1$
$1 + d + r = 1 \Rightarrow d = -r$

From $a_3 + g_3 = 4$, we have:
$(a_1 + 2d) + g_1 r^2 = 4$
$1 + 2d + r^2 = 4$
$2d + r^2 = 3$

Substituting $d = -r$ into the equation:
$-2r + r^2 = 3$
$r^2 - 2r - 3 = 0$
$(r - 3)(r + 1) = 0$

Since the G.P. is increasing and $g_1 = 1$, the common ratio $r$ must be greater than $1$. Thus, $r = 3$.

Then, $d = -3$.

We need to find $a_{10} + g_5$:
$a_{10} = a_1 + 9d = 1 + 9(-3) = -26$
$g_5 = g_1 r^4 = 1(3)^4 = 81$

$a_{10} + g_5 = -26 + 81 = 55$

Answer: $55$

</details>

---

### Q6. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A$ be the set of first 101 terms of an A.P., whose first term is 1 and the common difference is 5 and let $B$ be the set of first 71 terms of an A.P., whose first term is 9 and the common difference is 7. Then the number of elements in $A \cap B$, which are divisible by 3, is :

**Options:**

- **(A)** $4$
- **(B)** $5$
- **(C)** $6$
- **(D)** $7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $5$**

**Detailed Solution:**

The set $A$ consists of the first 101 terms of an A.P. with first term $a_1 = 1$ and common difference $d_1 = 5$.

The terms of $A$ are $1, 6, 11, 16, \dots, 1 + (101-1) \times 5 = 501$.

The set $B$ consists of the first 71 terms of an A.P. with first term $b_1 = 9$ and common difference $d_2 = 7$.

The terms of $B$ are $9, 16, 23, 30, \dots, 9 + (71-1) \times 7 = 499$.

The first common term of $A$ and $B$ is $16$.

The common difference of the terms in $A \cap B$ is the least common multiple of $d_1$ and $d_2$, which is $\text{lcm}(5, 7) = 35$.

The general term of $A \cap B$ is given by $T_k = 16 + 35k$, where $k \ge 0$ is an integer.

Since the maximum possible value in $A \cap B$ cannot exceed the maximum value in $B$ (which is $499$), we have:

$16 + 35k \le 499$

$35k \le 483$

$k \le 13.8$

Thus, the possible values for $k$ are $0, 1, 2, \dots, 13$.

We require the terms in $A \cap B$ to be divisible by $3$. Therefore:

$16 + 35k \equiv 0 \pmod 3$

$1 + 2k \equiv 0 \pmod 3$

$2k \equiv 2 \pmod 3$

$k \equiv 1 \pmod 3$

The values of $k$ in the range $0 \le k \le 13$ that satisfy $k \equiv 1 \pmod 3$ are $1, 4, 7, 10, 13$.

There are exactly $5$ such values of $k$, which correspond to $5$ elements in $A \cap B$ that are divisible by $3$.

Answer: $5$

</details>

---

### Q7. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let the arithmetic mean of $\frac{1}{\mathrm{a}}$ and $\frac{1}{\mathrm{~b}}$ be $\frac{5}{16}, \mathrm{a}>2$. If $\alpha$ is such that $\mathrm{a}, 4, \alpha, \mathrm{~b}$ are in A.P., then the equation $\alpha x^{2}-a x+2(\alpha-2 b)=0$ has:

**Options:**

- **(A)** one root in $(0,2)$ and another in $(-4,-2)$
- **(B)** one root in (1,4) and another in (-2,0)
- **(C)** both roots in the interval $(-2,0)$
- **(D)** complex roots of magnitude less than 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) one root in (1,4) and another in (-2,0)**

**Detailed Solution:**

Given AM of $\frac{1}{a}$ and $\frac{1}{b}$ is $\frac{5}{16}$ with $a > 2$. Since $a, 4, \alpha, b$ are in AP:
$4 - a = \alpha - 4 = b - \alpha$
This gives $\alpha = 8 - a$ and $b = 12 - 2a$.
From AM condition: $\frac{\frac{1}{a} + \frac{1}{b}}{2} = \frac{5}{16}$ leads to $\frac{a+b}{ab} = \frac{5}{8}$
Substituting: $\frac{20-3a}{96-28a+2a^2} = \frac{5}{8}$
$160 - 24a = 480 - 140a + 10a^2$
$10a^2 - 116a + 320 = 0$ or $5a^2 - 58a + 160 = 0$
Using the quadratic formula gives $a = 4$ or $a = 8$.
For $a = 4$: $\alpha = 4, b = 4$.
The equation becomes $4x^2 - 4x - 8 = 0$ or $x^2 - x - 2 = 0$ with roots 2 and $-1$.
One root lies in $(1,4)$ and the other in $(-2,0)$.

</details>

---

### Q8. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The common difference of the A.P.: $a_{1}, a_{2}, \ldots, a_{\mathrm{m}}$ is 13 more than the common difference of the A.P.: $b_{1}, b_{2}, \ldots, b_{n}$. If $b_{31}=-277, b_{43}=-385$ and $a_{78}=327$, then $a_{1}$ is equal to

**Options:**

- **(A)** 16
- **(B)** 21
- **(C)** 19
- **(D)** 24

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 19**

**Detailed Solution:**

Let $d$ and $d'$ be the common differences of the two APs respectively.
Given: $d = d' + 13$. 
 From the second AP: $b_{43} - b_{31} = 12d'$, so $-385 - (-277) = 12d'$, giving $-108 = 12d'$ and $d' = -9$. 
 Therefore $d = -9 + 13 = 4$. 
 For the first AP: $a_{78} = a_1 + 77d$, so $327 = a_1 + 77(4) = a_1 + 308$. 
 Thus $a_1 = 19$

</details>

---

### Q9. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $a_{1}, a_{2}, a_{3}, a_{4}$ be an A.P. of four terms such that each term of the A.P. and its common difference $l$ are integers. If $a_{1}+a_{2}+a_{3}+a_{4}=48$ and $a_{1} a_{2} a_{3} a_{4}+l^{4}=361$, then the largest term of the A.P. is equal to

**Options:**

- **(A)** 23
- **(B)** 21
- **(C)** 27
- **(D)** 24

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 27**

**Detailed Solution:**

Let the four terms be $12 - 3k,\ 12 - k,\ 12 + k,\ 12 + 3k$ with common difference $l = 2k$.
Sum $= 48$ is satisfied. Product condition:
$(144 - 9k^2)(144 - k^2) + 16k^4 = 361$
$25k^4 - 1440k^2 + 20375 = 0$
Let $u = k^2$: $25u^2 - 1440u + 20375 = 0$
$u = \frac{1440 \pm \sqrt{2073600 - 2037500}}{50} = \frac{1440 \pm 190}{50}$
$u = 25$ (integer) or $u = 32.6$ (rejected).
$k = 5$, $l = 10$. Terms: $-3, 7, 17, 27$.
Largest term $= 27$.

</details>

---

### Q10. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider an A.P.: $a_{1}, a_{2}, \ldots, a_{\mathrm{n}} ; a_{1}>0$. If $a_{2}-a_{1}=\frac{-3}{4}, a_{\mathrm{n}}=\frac{1}{4} a_{1}$, and $\sum_{\mathrm{i}=1}^{\mathrm{n}} a_{\mathrm{i}}=\frac{525}{2}$, then $\sum_{\mathrm{i}=1}^{17} a_{\mathrm{i}}$ is equal to

**Options:**

- **(A)** 136
- **(B)** 476
- **(C)** 238
- **(D)** 952

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 238**

**Detailed Solution:**

Common difference $d = a_2 - a_1 = -3/4$.
$a_n = a_1 + (n-1)(-3/4) = a_1/4$ 
 $\Rightarrow$ $3a_1/4 = 3(n-1)/4$
$\Rightarrow a_1 = n-1$.
$S_n = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}\cdot\frac{5a_1}{4} = \frac{5na_1}{8} = \frac{525}{2}$
$na_1 = 420$.
Since $a_1 = n-1$: $n(n-1) = 420$
$\Rightarrow n = 21,\; a_1 = 20$.
$\sum_{i=1}^{17} a_i = \frac{17}{2}(2 \cdot 20 + 16 \cdot (-3/4))$ 
$= \frac{17}{2}(40 - 12) = 17 \times 14 = 238$

</details>

---

### Q11. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\sum_{k=1}^{n} a_{k}=\alpha n^{2}+\beta n$. If $a_{10}=59$ and $a_{6}=7 a_{1}$, then $\alpha+\beta$ is equal to

**Options:**

- **(A)** 3
- **(B)** 12
- **(C)** 7
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 5**

**Detailed Solution:**

$S_n = \alpha n^2 + \beta n \Rightarrow a_n = S_n - S_{n-1} = \alpha(2n-1) + \beta$ for $n \ge 1$.
$a_{10} = 19\alpha + \beta = 59$ ... (i)
$a_6 = 11\alpha + \beta$, $a_1 = \alpha + \beta$.
$a_6 = 7a_1 \Rightarrow 11\alpha + \beta = 7\alpha + 7\beta \Rightarrow 4\alpha = 6\beta \Rightarrow \alpha = \frac{3\beta}{2}$ ... (ii)
Substituting (ii) in (i): $19 \cdot \frac{3\beta}{2} + \beta = 59 \Rightarrow \frac{59\beta}{2} = 59 \Rightarrow \beta = 2$, $\alpha = 3$.
$\alpha + \beta = 5$.

</details>

---

### Q12. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the sum of the first four terms of an A.P. is 6 and the sum of its first six terms is 4, then the sum of its first twelve terms is

**Options:**

- **(A)** -22
- **(B)** -24
- **(C)** -20
- **(D)** -26

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -22**

**Detailed Solution:**

$S_4 = 6 \Rightarrow 2(2a+3d) = 6 \Rightarrow 2a+3d = 3$ ...(i)
$S_6 = 4 \Rightarrow 3(2a+5d) = 4 \Rightarrow 2a+5d = \frac{4}{3}$ ...(ii)
(ii) $-$ (i): $2d = \frac{4}{3} - 3 = -\frac{5}{3} \Rightarrow d = -\frac{5}{6}$.
From (i): $2a = 3 + \frac{5}{2} = \frac{11}{2}$.
$S_{12} = 6(2a + 11d) = 6\left(\frac{11}{2} - \frac{55}{6}\right) = 6 \times \frac{-22}{6} = -22$.

</details>

---

### Q13. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{a}_{\mathrm{n}}$ be the $\mathrm{n}^{\text {th }}$ term of an A. P.
If $S_n=a_1+a_2+a_3+\ldots+a_n=700, a_6=7$ and $S_7=7$, then $\mathrm{a}_{\mathrm{n}}$ is equal to :

**Options:**

- **(A)** 56
- **(B)** 65
- **(C)** 64
- **(D)** 70

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 64**

**Detailed Solution:**

$\mathrm{S}_{\mathrm{n}}=700=\frac{\mathrm{n}}{2}[2 \mathrm{a}+(\mathrm{n}-1) \mathrm{d}]$...(i)
$a_6=7 \Rightarrow a+5 d=7$...(ii)
$\mathrm{S}_7=7 \Rightarrow \frac{7}{2}(2 \mathrm{a}+6 \mathrm{~d})=7$
$a+3 d=1$...(iii)
Solve (ii) and (iii)
$\begin{aligned}
& \frac{\mathrm{n}}{2}(-16+3 n-3)=700 \Rightarrow 3 n^2-19 n-1400=0 \\
& (3 n+56)(\mathrm{n}-25)=0 \\
& \therefore \mathrm{a}_{25}=\mathrm{a}+24 \mathrm{~d}=-8+24 \times 3 \\
& =-8+72
\end{aligned}$
=64

</details>

---

### Q14. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider two sets $A$ and $B$, each containing three numbers in A.P. Let the sum and the product of the elements of A be 36 and p respectively and the sum and the product of the elements of B be 36 and q respectively. Let d and D be the common differences of AP's in A and B respectively such that $D=d+3, d \gt 0$. If $\frac{p+q}{p-q}=\frac{19}{5}$, then $p-q$ is equal to

**Options:**

- **(A)** $600$
- **(B)** $450$
- **(C)** $630$
- **(D)** $540$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $540$**

**Detailed Solution:**

$\begin{array}{lc}\text { Let } A(a-d, a, a+d) & B(b-D, b, b+D) \\ \quad a=12 & b=12 \\ p=12\left(144-d^2\right) & \\ q=12\left(144-D^2\right) & \\ \frac{p+q}{p-q}=\frac{19}{5} & \end{array}$
$\begin{aligned} & \frac{p}{q}=\frac{24}{14}=\frac{12}{7} \\ & \frac{144-d^2}{144-\left(d^2+6 d+9\right)}=\frac{12}{7} \\ & 1008-7 d^2=-12 d^2-72 d+1620 \\ & 5 d^2+72 d-612=0 \\ & d=6 \\ & D=9 \\ & p-q=12\left(D^2-d^3\right) \\ & =12(81-36) \\ & =12(45) \\ & =540 \\ & \text { option }(4)\end{aligned}$

</details>

---

### Q15. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\{1,6,11,16, \ldots\}$ and $B=\{9,16,23,30, \ldots\}$ be the sets consisting of the first 2025 terms of two arithmetic progressions. Then $n(A \cup B)$ is

**Options:**

- **(A)** 3814
- **(B)** 4027
- **(C)** 3761
- **(D)** 4003

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3761**

**Detailed Solution:**

$\begin{aligned} & A=\{1,6,11,16,21,26,31,36,41,46,51,56,61, \\ & 66,71,76,81,86,91, \ldots \ldots\} \\ & B=\{9,16,23,30,37,44,51,58,65,72,79,86, \\ & 93,100, \ldots \ldots\} \\ & A \cap B=\{16,51,86, \ldots \ldots\} \\ & \text { For set 'A' } \Rightarrow T_{2025}=1+(2025-1)(5)=10121 \\ & \text { For set ' } B^{\prime} \Rightarrow T_{2025}=9+(2025-1)(7)=14177 \\ & \text { So, for }(A \cap B) \Rightarrow T_n=16+(n-1)(35) \leq 10121 \\ & (n-1) \leq \frac{10121-16}{35}=288.71 \\ & n \leq 289.71 \Rightarrow n=289 \\ & \therefore n(A \cup B)=n(A)+n(B)-n(A \cap B) \\ & =2025+2025-289=3761\end{aligned}$

</details>

---

### Q16. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of terms of an A.P. is even; the sum of all the odd terms is 24 , the sum of all the even terms is 30 and the last term exceeds the first by $\frac{21}{2}$. Then the number of terms which are integers in the A.P. is :

**Options:**

- **(A)** $4$
- **(B)** $10$
- **(C)** $6$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4$**

**Detailed Solution:**

$\mathrm{a}_2+\mathrm{a}_4+\ldots+\mathrm{a}_{\mathrm{n}}=30$   ...(1)
$\mathrm{a}_1+\mathrm{a}_3+\ldots+\mathrm{a}_{\mathrm{n}-1}=24$   ...(2)
$(1)-(2)$
$\left(a_2-a_1\right)+\left(a_4-a_3\right) \ldots\left(a_n-a_{n-1}\right)=6$
$\begin{aligned} & \Rightarrow \frac{\mathrm{n}}{2} \mathrm{~d}=6 \Rightarrow \mathrm{nd}=12 \\ & \mathrm{a}_{\mathrm{n}}-\mathrm{a}_1=(\mathrm{n}-1) \mathrm{d}=\frac{21}{2} \\ & \Rightarrow \mathrm{nd}-\mathrm{d}=\frac{21}{2} \Rightarrow 12-\frac{21}{2}=\mathrm{d} \\ & \Rightarrow \mathrm{d}=\frac{3}{2}, \mathrm{n}=8\end{aligned}$
$\begin{aligned}
& \text { Sum of odd terms }=\frac{4}{2}[2 \mathrm{a}+(4-1) 3]=24 \\
& \Rightarrow \mathrm{a}=\frac{3}{2} \\
& \text { A.P. } \Rightarrow \frac{3}{2}, 3, \frac{9}{2}, 6, \frac{15}{2}, 9, \frac{21}{2}, 12
\end{aligned}$
no. of integer terms $=4$

</details>

---

### Q17. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $a_1, a_2, a_3 \ldots$ be in an A.P. such that $\sum_{\mathrm{k}=1}^{12} \mathrm{a}_{2 \mathrm{k}-1}=-\frac{72}{5} \mathrm{a}_1, \mathrm{a}_1 \neq 0$. If $\sum_{\mathrm{k}=1}^{\mathrm{n}} \mathrm{a}_{\mathrm{k}}=0$, then n is:

**Options:**

- **(A)** 11
- **(B)** 10
- **(C)** 18
- **(D)** 17

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 11**

**Detailed Solution:**

Let $a_1=a$, common difference $=d$
$a_1+a_3+a_5+\ldots \ldots+a_{23}=-\frac{72}{5} a$
$\frac{12}{2}[2 a+11 \times 2 d]=-\frac{72}{5} a$
$12 a+132 d=-\frac{72}{5} a$
$132 a+132 \times 5 d=0$
$\mathrm{a}=-5 \mathrm{~d}$
$\frac{\mathrm{n}}{2}(2 \mathrm{a}+(\mathrm{n}-1) \mathrm{d})=0 \Rightarrow-10 \mathrm{~d}+\mathrm{nd}-\mathrm{d}=0$
$\mathrm{n}=11$

</details>

---

### Q18. JEE Main 2025 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

Let $a_1, a_2, \ldots, a_{2024}$ be an Arithmetic Progression such that $a_1+\left(a_5+a_{10}+a_{15}+\ldots+a_{2020}\right)+a_{2024}=2233$. Then $a_1+a_2+a_3+\ldots+a_{2024}$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11132**

**Detailed Solution:**

As $a_1+a_5+a_{10}+\ldots+a_{2020}+a_{2024}=2233$  ...(1)
We know in arithmetic progression.
Sum of terms equidistant from ends is equal
$\therefore$ from (1)
$\underbrace{a_1+a_{2024}=a_5+a_{2020}=a_{10}+a_{2015}=\ldots}_{203 \text { pairs }}$
$\begin{aligned} & \Rightarrow \quad 203\left(a_1+a_{2024}\right)=2233 \\ & \Rightarrow \quad a_1+a_{2024}=11\end{aligned}$
Now $\begin{aligned} \sum_{i=1}^{2024} a_i & =S_{2024}=\frac{2024}{2}\left[a_1+a_{2024}\right] \\ & =1012(11) \\ & =11132\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider an A. P. of positive integers, whose sum of the first three terms is 54 and the sum of the first twenty terms lies between 1600 and 1800. Then its \(11^{\text {th }}\) term is :

**Options:**

- **(A)** 90
- **(B)** 84
- **(C)** 122
- **(D)** 108

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 90**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{S}_3=3 \mathrm{a}+3 \mathrm{~d}=54 \\
& \Rightarrow \mathrm{a}+\mathrm{d}=18 \\
& \mathrm{~S}_{20}=10(2 \mathrm{a}+19 \mathrm{~d}) \\
& \Rightarrow 10(36+17 \mathrm{~d}) \\
& \Rightarrow 1600 < 10(36+17 \mathrm{~d}) < 1800 \\
& \Rightarrow 160 < 36+17 \mathrm{~d} < 180 \\
& \Rightarrow 124 < 17 \mathrm{~d} < 144 \\
& \Rightarrow 7 \frac{5}{17} < \mathrm{d} < 8 \frac{8}{17}
\end{aligned}$

Common difference will be natural number
$\begin{aligned}
& \Rightarrow d=8 \Rightarrow a=10 \\
& \Rightarrow a_{11}=10+10 \times 8=90
\end{aligned}$

</details>

---

### Q20. JEE Main 2025 (28 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

The interior angles of a polygon with n sides, are in an A.P. with common difference $6^{\circ}$. If the largest interior angle of the polygon is $219^{\circ}$, then n is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

$\frac{n}{2}[2 a+(n-1) 6]=(n-2) 180^{\circ}$
and $a n+3 n^2-3 n=3 n(n-2) 180^{\circ}$...(i)
$\begin{aligned}
& \therefore \quad \text { Given } a+(n-1) 6^{\circ}=219^{\circ} \\
& \Rightarrow a=225^{\circ}-6 n^{\circ}
\end{aligned}$
Putting value of $a$ in (i)
$\begin{aligned}
& \text { We get }\left(225-6 n^2\right)+3 n^2-3 n=180 n-360^{\circ} \\
& \Rightarrow 2 n^2-42 n-360=0 \\
& \Rightarrow n^2-14 n-120=0 \\
& \Rightarrow(n-20)(n+6)=0 \\
& \Rightarrow n=20,-6 \text { (Rejected) } \\
& \therefore n=20
\end{aligned}$

</details>

---

### Q21. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{T}_{\mathrm{r}}$ be the $\mathrm{r}^{\text {th }}$ term of an A.P. If for some $\mathrm{m}, \mathrm{T}_{\mathrm{m}}=\frac{1}{25}, \mathrm{~T}_{25}=\frac{1}{20}$, and $20 \sum_{\mathrm{r}=1}^{25} \mathrm{~T}_{\mathrm{r}}=13$, then $5 \mathrm{~m} \sum_{\mathrm{r}=\mathrm{m}}^{2 \mathrm{~m}} \mathrm{~T}_{\mathrm{r}}$ is equal to

**Options:**

- **(A)** 98
- **(B)** 126
- **(C)** 142
- **(D)** 112

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 126**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{T}_{\mathrm{m}}=\frac{1}{25}, \mathrm{~T}_{25}=\frac{1}{20}, 20 \sum_{\mathrm{r}=1}^{25} \mathrm{~T}_{\mathrm{r}}=13 \\
& \mathrm{~T}_{\mathrm{m}}=\mathrm{a}+(\mathrm{m}-1) \mathrm{d}=\frac{1}{25} \ldots \ldots .(1) \\
& \mathrm{T}_{25}=\mathrm{a}+24 \mathrm{~d}=\frac{1}{20} \\
& 20 \cdot \frac{25}{2}\left[\mathrm{a}+\frac{1}{20}\right]=13 \Rightarrow \mathrm{a}=\frac{1}{500}
\end{aligned}$
also, $20 \mathrm{~S}_{25}=20 \cdot \frac{25}{2}[2 \mathrm{a}+24 \mathrm{~d}]=13 \Rightarrow \mathrm{~d}=\frac{1}{500}$
from (1) $\frac{1}{500}+\frac{\mathrm{m}-1}{500}=\frac{1}{25} \Rightarrow \mathrm{~m}=20$
Now,
$5 \mathrm{~m} \sum_{\mathrm{r}=\mathrm{m}}^{2 \mathrm{~m}} \mathrm{~T}_{\mathrm{r}}=100 \sum_{\mathrm{r}=20}^{40} \mathrm{~T}_{\mathrm{r}}=126$

</details>

---

### Q22. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\text { In an arithmetic progression, if } S_{40}=1030 \text { and } S_{12}=57 \text {, then } S_{30}-S_{10} \text { is equal to : }$

**Options:**

- **(A)** 525
- **(B)** 510
- **(C)** 515
- **(D)** 505

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 515**

**Detailed Solution:**

$\begin{aligned}
& S_{40}=1030 \Rightarrow \frac{40}{2}[2 a+39 d]=1030 \\
& \Rightarrow \quad 2 a+39 d=\frac{103}{2}....(1) \\
& \quad S_{12}=57 \Rightarrow \frac{12}{2}[2 a+11 d]=57 \\
& \Rightarrow \quad 2 a+11 d=\frac{57}{6}...(2)
\end{aligned}$
Equation (1) - equation (2)
$\begin{aligned}
& 28 d=\frac{103}{2}-\frac{57}{6} \\
& 28 d=\frac{309-57}{6}
\end{aligned}$
$d=\frac{3}{2}$
$\Rightarrow \quad a=-\frac{7}{2}$
$S_{30}-S_{10}=\frac{30}{2}[2 a+29 d]-\frac{10}{2}[2 a+9 d]$
$=15[2 a+29 d]-5[2 a+9 d]$
$=5[6 a+87 d-2 a-9 d]$
$=5[4 a+78 d]$
$=5[-14+117]$
$=515$

</details>

---

### Q23. JEE Main 2025 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of 3 -digit numbers, that are divisible by 2 and 3 , but not divisible by 4 and 9 , is______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **125**

**Detailed Solution:**

No, of 3 digits $=999-99=900$
No. of 3 digit numbers divisible by 2 & 3 i.e. by 6
$\frac{900}{6}=150$

No. of 3 digit numbers divisible by 4 & 9 i.e. by 36
$\frac{900}{36}=25$
$\therefore$ No of 3 digit numbers divisible by $2 ~\&~ 3$ but not by $4 ~\&~ 9$
$150-25=125$

</details>

---

### Q24. JEE Main 2025 (23 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

The roots of the quadratic equation $3 x^2-\mathrm{p} x+\mathrm{q}=0$ are $10^{\text {th }}$ and $11^{\text {th }}$ terms of an arithmetic progression with common difference $\frac{3}{2}$. If the sum of the first 11 terms of this arithmetic progression is 88 , then $q-2 p$ is equal to $\qquad$ -.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **474**

**Detailed Solution:**

$\begin{aligned}
& S_{11}=\frac{11}{2}(2 a+10 d)=88 \\
& a+5 d=8 \\
& a=8-5 \times \frac{3}{2}=\frac{1}{2}
\end{aligned}$

Roots are
$\begin{aligned}
& \mathrm{T}_{10}=\mathrm{a}+9 \mathrm{~d}=\frac{1}{2}+9 \times \frac{3}{2}=14 \\
& \mathrm{~T}_{11}=\mathrm{a}+10 \mathrm{~d}=\frac{1}{2}+10 \times \frac{3}{2}=\frac{31}{2} \\
& \frac{\mathrm{p}}{3}=\mathrm{T}_{10}+\mathrm{T}_{11}=14+\frac{31}{2}=\frac{59}{2} \\
& \mathrm{p}=\frac{177}{2} \\
& \frac{\mathrm{q}}{3}=\mathrm{T}_{10} \times \mathrm{T}_{11}=7 \times 31=217 \\
& \mathrm{q}=651 \\
& \mathrm{q}-2 \mathrm{p} \\
& =651-177 \\
& =474
\end{aligned}$

</details>

---

### Q25. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the first term of an A.P. is 3 and the sum of its first four terms is equal to one-fifth of the sum of the next four terms, then the sum of the first 20 terms is equal to

**Options:**

- **(A)** $-1080$
- **(B)** $-1020$
- **(C)** $-1200$
- **(D)** $-120$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-1080$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{a}=3 \\ & \mathrm{~S}_4=\frac{1}{5}\left(\mathrm{~S}_8-\mathrm{S}_4\right) \\ & \Rightarrow 5 \mathrm{~S}_4=\mathrm{S}_8-\mathrm{S}_4 \\ & \Rightarrow 6 \mathrm{~S}_4=\mathrm{S}_8 \\ & \Rightarrow 6 \cdot \frac{4}{2}[2 \times 3+(4-1) \times \mathrm{d}] \\ & =\frac{8}{2}[2 \times 3+(8-1) \mathrm{d}] \\ & \Rightarrow 12(6+3 \mathrm{~d})=4(6+7 \mathrm{~d}) \\ & \Rightarrow 18+9 \mathrm{~d}=6+7 \mathrm{~d} \\ & \Rightarrow \mathrm{~d}=-6 \\ & \mathrm{~S}_{20}=\frac{20}{2}[2 \times 3+(20-1)(-6)] \\ & =10[6-114] \\ & =-1080\end{aligned}$

</details>

---

### Q26. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Suppose that the number of terms in an A.P. is $2 k, k \in N$. If the sum of all odd terms of the A.P. is 40 , the sum of all even terms is 55 and the last term of the A.P. exceeds the first term by 27, then k is equal to :

**Options:**

- **(A)** 6
- **(B)** 5
- **(C)** 8
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5**

**Detailed Solution:**

Let the A.P. be
$\begin{aligned}
& a, a+2, a+2 d, \ldots, a+(2 k-1) d \\
& \text { Now, } a+a+2 d+a+4 d+\ldots+a+(2 k-2) d=40 \\
& k a+2 d+4 d+\ldots+(2 k-2) d=40 \\
& \Rightarrow k a+\frac{k-1}{2}[2 d+2 k d-2 d]=40
\end{aligned}$
$\Rightarrow k a+k(k-1) d=40$  ...(1)
And $a+d+a+3 d+\ldots+a+(2 k-1) d=55$
$\Rightarrow k a+\frac{k}{2}(d+2 k d-d)=55$
$\Rightarrow k a+k^2 d=55$   ....(2)
Also, $a+(2 k-1) d-a=27$
$\Rightarrow \quad(2 k-1) d=27 \Rightarrow d=\frac{27}{2 k-1}$   ...(3)
From equation (1) and (2)
$k^2 d-k d-k^2 d=-15$
$\Rightarrow \quad d=\frac{15}{k}$
From equation (3) and (4)
$\begin{aligned}
& \frac{27}{2 k-1}=\frac{15}{k} \\
& 27 k=30 k-15 \\
& \Rightarrow 3 k=15 \\
& \Rightarrow k=5
\end{aligned}$

</details>

---

### Q27. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the sum of the series $\frac{1}{1 \cdot(1+\mathrm{d})}+\frac{1}{(1+\mathrm{d})(1+2 \mathrm{~d})}+\ldots+\frac{1}{(1+9 \mathrm{~d})(1+10 \mathrm{~d})}$ is equal to 5 , then $50 \mathrm{~d}$ is equal to :

**Options:**

- **(A)** 10
- **(B)** 5
- **(C)** 15
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5**

**Detailed Solution:**

$\begin{aligned} & \frac{1}{1 \cdot(1+\mathrm{d})}+\frac{1}{(1+\mathrm{d})(1+2 \mathrm{~d})}+\ldots \ldots \ldots \ldots . . \\ & \frac{1}{(1+9 \mathrm{~d})(1+10 \mathrm{~d})}=5\end{aligned}$
$\begin{aligned} & \frac{1}{d}\left[\frac{(1+d)-1}{1 \cdot(1+d)}+\frac{(1+2 d)-(1-d)}{(1+d)(1+2 d)}\right]+\ldots \ldots \ldots \ldots . . . \\ & \frac{(1+10 d)-(1+9 d)}{(1+9 d)(1+10 d)}=5 \\ & \frac{1}{d}\left[\left(1-\frac{1}{1+d}\right)+\left(\frac{1}{1+d}-\frac{1}{1+2 d}\right)+\ldots \ldots \ldots \ldots . .\right. \\ & \left.\left(\frac{1}{1+9 d}-\frac{1}{1+10 d}\right)\right]=5 \\ & \frac{1}{d}\left[1-\frac{1}{(1+10 d)}\right]=5 \\ & \frac{10 d}{1+10 d}=5 d \\ & 50 d=5\end{aligned}$

</details>

---

### Q28. JEE Main 2024 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

An arithmetic progression is written in the following way
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bB7stDSups0-uIPe4AZasRrPBcAqCP8cz5i9_2KTLvs.original.fullsize.png">
The sum of all the terms of the $10^{\text {th }}$ row is_______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1505**

**Detailed Solution:**

$\begin{aligned} & 2,5,11,20, \ldots . . \\ & \text { General term }=\frac{3 n^2-3 n+4}{2} \\ & \begin{aligned} & \mathrm{T}_{10}=\frac{3(100)-3(10)+4}{2} \\ & \quad= 137 \\ & 10 \text { terms with c.d. }=3 \\ & \text { sum }=\frac{10}{2}(2(137)+9(3)) \\ &=1505\end{aligned}\end{aligned}$

</details>

---

### Q29. JEE Main 2024 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let the positive integers be written in the form :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/swzd3iPlVE6VC8HzgThfej6f0P9tj4skKl_HIny6prY.original.fullsize.png">
If the $k^{\text {th }}$ row contains exactly $k$ numbers for every natural number $k$, then the row in which the number 5310 will be, is _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **103**

**Detailed Solution:**

$\begin{aligned} & \mathrm{S}=1+2+4+7+\ldots \ldots+\mathrm{T}_{\mathrm{n}} \\ & \mathrm{S}=1+2+4+\ldots \ldots \\ & \mathrm{Tn}=1+1+2+3+\ldots \ldots+\left(\mathrm{T}_{\mathrm{n}}-\mathrm{T}_{\mathrm{n}-1}\right) \\ & \mathrm{T}_{\mathrm{n}}=1+\left(\frac{\mathrm{n}-1}{2}\right)[2+(\mathrm{n}-2) \times 1] \\ & \mathrm{T}_{\mathrm{n}}=1+1+\frac{\mathrm{n}(\mathrm{n}-1)}{2} \\ & \mathrm{n}=100 \quad \mathrm{~T}_{\mathrm{n}}=1+\frac{100 \times 99}{2}=4950+1 \\ & \mathrm{n}=101 \quad \mathrm{~T}_{\mathrm{n}}=1+\frac{101 \times 100}{2}=5050+1=5051 \\ & \mathrm{n}=102 \quad \mathrm{~T}_{\mathrm{n}}=1+\frac{102 \times 101}{2}=5151+1=5152 \\ & \mathrm{n}=103 \quad \mathrm{~T}_{\mathrm{n}}=1+\frac{103 \times 102}{2}=5254 \\ & \mathrm{n}=104 \quad \mathrm{~T}_{\mathrm{n}}=1+\frac{104 \times 103}{2}=5357\end{aligned}$

</details>

---

### Q30. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A software company sets up $m$ number of computer systems to finish an assignment in 17 days. If 4 computer systems crashed on the start of the second day, 4 more computer systems crashed on the start of the third day and so on, then it took 8 more days to finish the assignment. The value of $\mathrm{m}$ is equal to:

**Options:**

- **(A)** 150
- **(B)** 180
- **(C)** 160
- **(D)** 125

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 150**

**Detailed Solution:**

$\begin{aligned} & 17 \mathrm{~m}=\mathrm{m}+(\mathrm{m}-4)+(\mathrm{m}-4 \times 2) \ldots+\ldots(\mathrm{m}-4 \times 24) \\ & 17 \mathrm{~m}=25 \mathrm{~m}-4(1+2 \ldots 24) \\ & 8 \mathrm{~m}=\frac{4 \cdot 24 \cdot 25}{2}=150\end{aligned}$

</details>

---

### Q31. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\{n \in[100,700] \cap \mathbb{N}: n$ is neither a multiple of 3 nor a multiple of 4$\}$. Then the number of elements in $A$ is

**Options:**

- **(A)** 290
- **(B)** 280
- **(C)** 300
- **(D)** 310

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 300**

**Detailed Solution:**

$\begin{aligned} & \mathrm{n}(3) \Rightarrow \text { multiple of } 3 \\ & 102,105,108, \ldots . ., 699 \\ & \mathrm{~T}_{\mathrm{n}}=699=102+(\mathrm{n}-1)(3) \\ & \mathrm{n}=200 \\ & \mathrm{n}(3)=200 \\ & \because \mathrm{n}(4) \Rightarrow \text { multiple of } 4\end{aligned}$
$\begin{aligned} & 100,104,108, \ldots ., 700 \\ & T_n=700=100+(n-1)(4) \\ & n=151 \\ & n(4)=151 \\ & n(3 \cap 4) \Rightarrow \text { multiple of } 3 \& 4 \text { both } \\ & 108,120,132, \ldots ., 696 \\ & T_n=696=108+(n-1)(12) \\ & n=50 \\ & n(3 \cap 4)=50 \\ & n(3 \cup 4)=n(3)+n(4)-n(3 \cap 4) \\ & \quad=200+151-50 \\ & \quad=301 \\ & n(\overline{3 \cup 4})=\text { Total }-n(3 \cup 4)=\text { neither a multiple } \\ & \text { of } 3 \text { nor a multiple of } 4 \\ & =601-301=300\end{aligned}$

</details>

---

### Q32. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For $x \geqslant 0$, the least value of $\mathrm{K}$, for which $4^{1+x}+4^{1-x}, \frac{\mathrm{K}}{2}, 16^x+16^{-x}$ are three consecutive terms of an A.P., is equal to :

**Options:**

- **(A)** 8
- **(B)** 4
- **(C)** 10
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 10**

**Detailed Solution:**

\(\begin{gathered}\mathrm{k}=4\left(4^{\mathrm{x}}+\frac{1}{4^{\mathrm{x}}}\right)+\left(4^{2 \mathrm{x}}+\frac{1}{4^{2 \mathrm{x}}}\right) \\ \qquad \geq 2 \quad\qquad\qquad \geq 2\end{gathered}\)
$\mathrm{k} \geq 10$

</details>

---

### Q33. JEE Main 2024 (05 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $a_1, a_2, a_3, \ldots$ be in an arithmetic progression of positive terms.
Let $\mathrm{A}_{\mathrm{k}}=\mathrm{a}_1^2-\mathrm{a}_2^2+\mathrm{a}_3^2-\mathrm{a}_4^2+\ldots+\mathrm{a}_{2 \mathrm{k}-1}^2-\mathrm{a}_{2 \mathrm{k}}^2$.
If $\mathrm{A}_3=-153, \mathrm{~A}_5=-435$ and $\mathrm{a}_1^2+\mathrm{a}_2^2+\mathrm{a}_3^2=66$, then $\mathrm{a}_{17}-\mathrm{A}_7$ is equal to______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **910**

**Detailed Solution:**

$\begin{aligned} & \mathrm{d} \rightarrow \text { common diff. } \\ & \mathrm{A}_{\mathrm{k}}=-\mathrm{kd}[2 \mathrm{a}+(2 \mathrm{k}-1) \mathrm{d}] \\ & \mathrm{A}_3=-153 \\ & \Rightarrow 153=13 \mathrm{~d}[2 \mathrm{a}+5 \mathrm{~d}] \\ & 51=\mathrm{d}[2 \mathrm{a}+5 \mathrm{~d}]...(1) \\ & \mathrm{A}_5=-435 \\ & 435=5 \mathrm{~d}[2 \mathrm{a}+9 \mathrm{~d}] \\ & 87=\mathrm{d}[2 \mathrm{a}+9 \mathrm{~d}] \\ & (2)-(1) \\ & 36=4 \mathrm{~d}^2 \\ & \mathrm{~d}=3, \mathrm{a}=1 \\ & \mathrm{a}_{17}-\mathrm{A}_7=49-[-7.3[2+39]]=910\end{aligned}$

</details>

---

### Q34. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub></math> denote the sum of the first n terms of an arithmetic progression. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>10</mn></msub><mo>=</mo><mn>390</mn></math> and the ratio of the tenth and the fifth terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo> </mo><mo>:</mo><mo> </mo><mn>7</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>15</mn></msub><mo>−</mo><msub><mi>S</mi><mn>5</mn></msub></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>800</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>890</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>790</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>690</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>790</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>a</mi><mn>10</mn></msub><msub><mi>a</mi><mn>5</mn></msub></mfrac><mo>=</mo><mfrac><mn>15</mn><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mstyle displaystyle="true"><mi>a</mi><mo>+</mo><mn>9</mn><mi>d</mi></mstyle><mstyle displaystyle="true"><mi>a</mi><mo>+</mo><mn>4</mn><mi>d</mi></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>15</mn></mstyle><mstyle displaystyle="true"><mn>7</mn></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>7</mn><mi>a</mi><mo>+</mo><mn>63</mn><mi>d</mi><mo>=</mo><mn>15</mn><mi>a</mi><mo>+</mo><mn>60</mn><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mi>d</mi><mo>=</mo><mn>8</mn><mi>a</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>10</mn></msub><mo>=</mo><mn>390</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>10</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>9</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>390</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>24</mn><mi>a</mi><mo>=</mo><mn>78</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mn>15</mn></msub><mo>-</mo><msub><mi>S</mi><mn>5</mn></msub><mo>=</mo><mfrac><mn>15</mn><mn>2</mn></mfrac><mfenced><mrow><mn>6</mn><mo>+</mo><mn>14</mn><mo>×</mo><mn>8</mn></mrow></mfenced><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mfenced><mrow><mn>6</mn><mo>+</mo><mn>4</mn><mo>×</mo><mn>8</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mn>15</mn></msub><mo>-</mo><msub><mi>S</mi><mn>5</mn></msub><mo>=</mo><mfrac><mn>15</mn><mn>2</mn></mfrac><mo>×</mo><mn>118</mn><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>×</mo><mn>38</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mn>15</mn></msub><mo>-</mo><msub><mi>S</mi><mn>5</mn></msub><mo>=</mo><mn>885</mn><mo>-</mo><mn>95</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mn>15</mn></msub><mo>-</mo><msub><mi>S</mi><mn>5</mn></msub><mo>=</mo><mn>790</mn></math></p>

</details>

---

### Q35. JEE Main 2024 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo> </mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>,</mo><mo> </mo><mn>15</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>403</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mo> </mo><mn>5</mn><mo>,</mo><mo> </mo><mn>8</mn><mo>,</mo><mo> </mo><mn>11</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>404</mn></math> be two arithmetic progressions. Then the sum, of the common terms in them, is equal to_________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6699**

**Detailed Solution:**

<p>Given AP are: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo> </mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>,</mo><mo> </mo><mn>15</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>403</mn><mo> </mo><mtext>and</mtext><mo> </mo><mn>2</mn><mo>,</mo><mo> </mo><mn>5</mn><mo>,</mo><mo> </mo><mn>8</mn><mo>,</mo><mo> </mo><mn>11</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>404</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo> </mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn><mo>,</mo><mo> </mo><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn></math></p><p>So, for the common AP,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>11</mn><mo>,</mo><mo> </mo><mi>d</mi><mo>=</mo><mi>LCM</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>12</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mn>403</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>11</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>12</mn><mo>≤</mo><mn>403</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>1</mn><mo>+</mo><mn>12</mn><mi>n</mi><mo>≤</mo><mn>403</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>≤</mo><mfrac><mn>404</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>≤</mo><mn>33</mn><mo>.</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>=</mo><mn>33</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>33</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mo>×</mo><mn>11</mn><mo>+</mo><mn>32</mn><mo>×</mo><mn>12</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mn>6699</mn></math></p>

</details>

---

### Q36. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>a</mi></msub></math> denote the sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> terms an arithmetic progression. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>20</mn></msub><mo>=</mo><mn>790</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>10</mn></msub><mo>=</mo><mn>145</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>15</mn></msub><mo>-</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">S</mi><mn>5</mn></msub></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>395</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>390</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>405</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>410</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>395</mn></math>**

**Detailed Solution:**

<p>Given,</p><p>In an arithmetic progression sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>790</mn></math></p><p>So, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> be the first term and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> be common difference,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>20</mn></msub><mo>=</mo><mfrac><mn>20</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>19</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>790</mn><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And sum of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>145</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>10</mn></msub><mo>=</mo><mfrac><mn>10</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>9</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>145</mn><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>By solving equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mn>8</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mi>d</mi><mo>=</mo><mn>5</mn></math></p><p> Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>15</mn></msub><mo>-</mo><msub><mi>S</mi><mn>5</mn></msub><mo>=</mo><mfrac><mn>15</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mo>×</mo><mfenced><mrow><mo>-</mo><mn>8</mn></mrow></mfenced><mo>+</mo><mn>14</mn><mo>×</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mo>×</mo><mfenced><mrow><mo>-</mo><mn>8</mn></mrow></mfenced><mo>+</mo><mn>4</mn><mo>×</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mn>15</mn></msub><mo>-</mo><msub><mi>S</mi><mn>5</mn></msub><mo>=</mo><mn>405</mn><mo>-</mo><mn>10</mn><mo>=</mo><mn>395</mn></math> </p>

</details>

---

### Q37. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mi>a</mi><mo>,</mo><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi><mo>,</mo><msub><mi>log</mi><mi>e</mi></msub><mi>c</mi></math> are in an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mi>a</mi><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mi>b</mi><mo>,</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mi>b</mi><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn><mi>c</mi><mo>,</mo><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn><mi>c</mi><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mi>a</mi></math> are also in an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>:</mo><mi>b</mi><mo>:</mo><mi>c</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>:</mo><mo> </mo><mn>6</mn><mo>:</mo><mo> </mo><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>:</mo><mo> </mo><mn>4</mn><mo>:</mo><mo> </mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mo>:</mo><mo> </mo><mn>10</mn><mo>:</mo><mo> </mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>:</mo><mo> </mo><mn>3</mn><mo>:</mo><mo> </mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>:</mo><mo> </mo><mn>6</mn><mo>:</mo><mo> </mo><mn>4</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mi>a</mi><mo>,</mo><mo> </mo><mi>log</mi><mi>b</mi><mo>,</mo><mo> </mo><mi>log</mi><mi>c</mi></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>log</mi><mi>b</mi><mo>=</mo><mi>log</mi><mi>a</mi><mo>+</mo><mi>log</mi><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mi>a</mi><mi>c</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mi>a</mi><mo>-</mo><mi>log</mi><mn>2</mn><mi>b</mi><mo>,</mo><mo> </mo><mi>log</mi><mn>2</mn><mi>b</mi><mo>-</mo><mi>log</mi><mn>3</mn><mi>c</mi><mo>,</mo><mo> </mo><mi>log</mi><mn>3</mn><mi>c</mi><mo>-</mo><mi>log</mi><mi>a</mi></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>log</mi><mfrac><mrow><mn>2</mn><mi>b</mi></mrow><mrow><mn>3</mn><mi>c</mi></mrow></mfrac><mo>=</mo><mi>log</mi><mfrac><mi>a</mi><mrow><mn>2</mn><mi>b</mi></mrow></mfrac><mo>+</mo><mi>log</mi><mfrac><mrow><mn>3</mn><mi>c</mi></mrow><mi>a</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mfrac><mrow><mn>2</mn><mi>b</mi></mrow><mrow><mn>3</mn><mi>c</mi></mrow></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mi>a</mi><mrow><mn>2</mn><mi>b</mi></mrow></mfrac><mo>×</mo><mfrac><mrow><mn>3</mn><mi>c</mi></mrow><mi>a</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mfrac><mrow><mn>2</mn><mi>b</mi></mrow><mrow><mn>3</mn><mi>c</mi></mrow></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>3</mn><mi>c</mi></mrow><mrow><mn>2</mn><mi>b</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>b</mi><mo>=</mo><mn>3</mn><mi>c</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn><msup><mi>c</mi><mn>2</mn></msup><mo> </mo><mo>&amp;</mo><mo> </mo><mn>6</mn><mi>b</mi><mo>=</mo><mn>9</mn><mi>c</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now solving the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>a</mi><mi>c</mi><mo>=</mo><mn>9</mn><msup><mi>c</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi>a</mi><mo>=</mo><mn>9</mn><mi>c</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>Then from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mfenced><mn>3</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>a</mi><mo>=</mo><mn>6</mn><mi>b</mi><mo>=</mo><mn>9</mn><mi>c</mi><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mfrac><mi>k</mi><mn>4</mn></mfrac><mo>,</mo><mo> </mo><mi>b</mi><mo>=</mo><mfrac><mi>k</mi><mn>6</mn></mfrac><mo> </mo><mo>&amp;</mo><mo> </mo><mi>c</mi><mo>=</mo><mfrac><mi>k</mi><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>:</mo><mi>b</mi><mo>:</mo><mi>c</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>:</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>:</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>=</mo><mn>9</mn><mo>:</mo><mn>6</mn><mo>:</mo><mn>4</mn></math></p>

</details>

---

### Q38. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In an A.P., the sixth term <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>6</mn></msub><mo>=</mo><mn>2</mn></math>. If the <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><msub><mi mathvariant="normal">a</mi><mn>4</mn></msub><msub><mi mathvariant="normal">a</mi><mn>5</mn></msub></math> is the greatest, then the common difference of the A.P., is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>5</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>5</mn></mfrac></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>6</mn></msub><mo>=</mo><mn>2</mn></math>. Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><msub><mi mathvariant="normal">a</mi><mn>4</mn></msub><msub><mi mathvariant="normal">a</mi><mn>5</mn></msub></math> is greatest.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">a</mi><mo>+</mo><mn>5</mn><mi mathvariant="normal">d</mi><mo>=</mo><mn>2</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><msub><mi mathvariant="normal">a</mi><mn>4</mn></msub><msub><mi mathvariant="normal">a</mi><mn>5</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">a</mi><mo>(</mo><mi mathvariant="normal">a</mi><mo>+</mo><mn>3</mn><mi mathvariant="normal">d</mi><mo>)</mo><mo>(</mo><mi mathvariant="normal">a</mi><mo>+</mo><mn>4</mn><mi mathvariant="normal">d</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mo>(</mo><mn>2</mn><mo>-</mo><mn>5</mn><mi mathvariant="normal">d</mi><mo>)</mo><mo>(</mo><mn>2</mn><mo>-</mo><mn>2</mn><mi mathvariant="normal">d</mi><mo>)</mo><mo>(</mo><mn>2</mn><mo>-</mo><mi mathvariant="normal">d</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mfenced><mrow><mn>4</mn><mo>-</mo><mn>4</mn><mi mathvariant="normal">d</mi><mo>-</mo><mn>10</mn><mi mathvariant="normal">d</mi><mo>+</mo><mn>10</mn><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>-</mo><mi mathvariant="normal">d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mfenced><mrow><mn>4</mn><mo>-</mo><mn>14</mn><mi mathvariant="normal">d</mi><mo>+</mo><mn>10</mn><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>-</mo><mi mathvariant="normal">d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>8</mn><mo>-</mo><mn>4</mn><mi mathvariant="normal">d</mi><mo>-</mo><mn>28</mn><mi mathvariant="normal">d</mi><mo>+</mo><mn>14</mn><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup><mo>+</mo><mn>20</mn><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><msup><mi mathvariant="normal">d</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>8</mn><mo>-</mo><mn>32</mn><mi mathvariant="normal">d</mi><mo>+</mo><mn>34</mn><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><msup><mi mathvariant="normal">d</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">y</mi><mo>'</mo></msup><mo>=</mo><mo>-</mo><mn>32</mn><mo>+</mo><mn>68</mn><mi mathvariant="normal">d</mi><mo>-</mo><mn>30</mn><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">y</mi><mo>'</mo></msup><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mn>15</mn><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup><mo>-</mo><mn>34</mn><mi mathvariant="normal">d</mi><mo>+</mo><mn>16</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">y</mi><mo>'</mo></msup><mo>=</mo><mo>-</mo><mn>2</mn><mo>(</mo><mn>5</mn><mi mathvariant="normal">d</mi><mo>-</mo><mn>8</mn><mo>)</mo><mo>(</mo><mn>3</mn><mi mathvariant="normal">d</mi><mo>-</mo><mn>2</mn><mo>)</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/55534d98-30fa-4a4b-a436-b55039eb0a36.png" style="width: 300px; height: 72px;"/></p><p>So,  the function attains maxima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">d</mi><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac></math></p>

</details>

---

### Q39. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>20</mn><mtext>th </mtext></msup></math> term from the end of the progression <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>,</mo><mn>19</mn><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mn>18</mn><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>17</mn><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mo>…</mo><mo>,</mo><mo>-</mo><mn>129</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></math> is :-

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>118</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>110</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>115</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>100</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>115</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>P</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>,</mo><mn>19</mn><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mn>18</mn><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>17</mn><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>-</mo><mn>129</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></math>.</p><p>Common difference, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">d</mi><mn>1</mn></msub><mo>=</mo><mn>19</mn><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mn>20</mn><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p>Reversing the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>P</mi></math> such that first term becomes the last and last term becomes first.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>129</mn><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>19</mn><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mn>20</mn></math></p><p>This is also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>P</mi></math>.</p><p>First term, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">a</mi><mo>=</mo><mo>-</mo><mn>129</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></math> and common difference, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">d</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>a</mi><mn>20</mn></msub><mo>=</mo><mo>-</mo><mn>129</mn><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mo>(</mo><mn>20</mn><mo>-</mo><mn>1</mn><mo>)</mo><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>a</mi><mn>20</mn></msub><mo>=</mo><mfrac><mrow><mo>-</mo><mn>517</mn></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>57</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>a</mi><mn>20</mn></msub><mo>=</mo><mfrac><mrow><mo>-</mo><mn>460</mn></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>a</mi><mn>20</mn></msub><mo>=</mo><mo>-</mo><mn>115</mn></math></p>

</details>

---

### Q40. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of common terms in the progressions <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>14</mn><mo>,</mo><mn>19</mn><mo>,</mo><mo>…</mo><mo>…</mo></math>, up to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>25</mn><mtext>th </mtext></msup></math> term and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>12</mn></math>,.... up to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>37</mn><mtext>th </mtext></msup></math> term is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>14</mn><mo>,</mo><mn>19</mn><mo>,</mo><mo>…</mo></math>, up to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>25</mn><mtext>th </mtext></msup></math> term</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">T</mi><mn>25</mn></msub><mo>=</mo><mn>4</mn><mo>+</mo><mo>(</mo><mn>25</mn><mo>-</mo><mn>1</mn><mo>)</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">T</mi><mn>25</mn></msub><mo>=</mo><mn>4</mn><mo>+</mo><mn>120</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">T</mi><mn>25</mn></msub><mo>=</mo><mn>124</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>12</mn><mo>,</mo><mo>…</mo></math>, up to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>37</mn><mtext>th </mtext></msup></math> term</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">T</mi><mn>37</mn></msub><mo>=</mo><mn>3</mn><mo>+</mo><mo>(</mo><mn>37</mn><mo>-</mo><mn>1</mn><mo>)</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">T</mi><mn>37</mn></msub><mo>=</mo><mn>3</mn><mo>+</mo><mn>108</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">T</mi><mn>37</mn></msub><mo>=</mo><mn>111</mn></math></p><p>Common difference of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">I</mi><mtext>st </mtext></msup></math> series is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">d</mi><mn>1</mn></msub><mo>=</mo><mn>5</mn></math></p><p>Common difference of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>II</mi><mtext>nd </mtext></msup></math> series is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">d</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn></math></p><p>First common term <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn></math>, and their common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>15</mn><mo>(</mo><mi>LCM</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">d</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open=""><msub><mi mathvariant="normal">d</mi><mn>2</mn></msub></mfenced></math>.</p><p>So, the common terms are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>,</mo><mo> </mo><mn>24</mn><mo>,</mo><mo> </mo><mn>39</mn><mo>,</mo><mo> </mo><mn>54</mn><mo>,</mo><mo> </mo><mn>69</mn><mo>,</mo><mo> </mo><mn>84</mn><mo>,</mo><mo> </mo><mn>99</mn></math>.</p>

</details>

---

### Q41. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>s</mi><mn>1</mn></msub><mo>,</mo><msub><mi>s</mi><mn>2</mn></msub><mo>,</mo><msub><mi>s</mi><mn>3</mn></msub><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><msub><mi>s</mi><mn>10</mn></msub></math> respectively be the sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> terms of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>.</mo><mi>Ps</mi></math> whose first terms are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>10</mn></math> and the common differences are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>19</mn></math> respectively. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>s</mi><mi>i</mi></msub></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7220</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7360</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7260</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7380</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7260</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>First term of A.P are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>10</mn></math>, so general term of the first term will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></p><p>And common difference are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math>, so general term of common difference is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>i</mi><mo>-</mo><mn>1</mn></math></p><p>Now sum of the A.P  is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>i</mi></msub><mo>=</mo><mfrac><mn>12</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mo>&#215;</mo><mi>i</mi><mo>+</mo><mfenced><mrow><mn>12</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>i</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mi>i</mi></msub><mo>=</mo><mn>6</mn><mfenced close="]" open="["><mrow><mn>2</mn><mo>&#215;</mo><mi>i</mi><mo>+</mo><mn>11</mn><mfenced><mrow><mn>2</mn><mi>i</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mi>i</mi></msub><mo>=</mo><mn>144</mn><mi>i</mi><mo>-</mo><mn>66</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>S</mi><mi>i</mi></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mn>144</mn><mi>i</mi><mo>-</mo><mn>66</mn><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>S</mi><mi>i</mi></msub><mo>=</mo><mn>144</mn><mfenced><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>11</mn></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>66</mn><mo>&#215;</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>S</mi><mi>i</mi></msub><mo>=</mo><mn>792</mn><mfenced><mn>10</mn></mfenced><mo>-</mo><mn>66</mn><mo>&#215;</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>S</mi><mi>i</mi></msub><mo>=</mo><mn>7260</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q42. JEE Main 2023 (10 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

The sum of all those terms, of the arithmetic progression <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mn>13</mn><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><mn>373</mn></math>, which are not divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>, is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9525**

**Detailed Solution:**

<blockquote><p>Given sequence is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>13</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>373</mn></math>.</p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo mathvariant="italic">=</mo><mn>3</mn><mo mathvariant="italic">,</mo><mo mathvariant="italic">&#160;</mo><mi>d</mi><mo mathvariant="italic">=</mo><mn>5</mn><mo mathvariant="italic">&#160;</mo><mi>and</mi><mo mathvariant="italic">&#160;</mo><msub><mi>a</mi><mi>n</mi></msub><mo mathvariant="italic">=</mo><mn>373</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>373</mn><mo>=</mo><mn>3</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>75</mn></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced><mrow><mi>a</mi><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>75</mn></msub><mo>=</mo><mfrac><mn>75</mn><mn>2</mn></mfrac><mfenced><mrow><mn>3</mn><mo>+</mo><mn>373</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>75</mn></msub><mo>=</mo><mn>14100</mn></math></p><p>Now let us write the sequence of terms which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>.</p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>18</mn><mo>,</mo><mn>33</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>363</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>363</mn><mo>=</mo><mn>3</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>25</mn></math></p><p>Now let us find the sum of terms divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mrow><mi>d</mi><mi>i</mi><mi>v</mi><mo>&#160;</mo><mi>b</mi><mi>y</mi><mo>&#160;</mo><mn>3</mn></mrow></msub><mo>=</mo><mfrac><mn>25</mn><mn>2</mn></mfrac><mfenced><mrow><mn>3</mn><mo>+</mo><mn>363</mn></mrow></mfenced><mo>=</mo><mn>4575</mn></math></p><p>Required sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>Sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>75</mn></math> terms<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo></math>Sum of terms divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>14100</mn><mo>-</mo><mn>4575</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9525</mn></math>.</p><p>Therefore, the required sum is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9525</mn></math></p></blockquote>

</details>

---

### Q43. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><msub><mi>a</mi><mi>n</mi></msub></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi></math> positive consecutive terms of an arithmetic progression. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>&#62;</mo><mn>0</mn></math> is its common difference, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msqrt><mfrac><mi>d</mi><mi>n</mi></mfrac></msqrt><mfenced><mrow><mfrac><mn>1</mn><mrow><msqrt><msub><mi>a</mi><mn>1</mn></msub></msqrt><mo>+</mo><msqrt><msub><mi>a</mi><mn>2</mn></msub></msqrt></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><msqrt><msub><mi>a</mi><mn>2</mn></msub></msqrt><mo>+</mo><msqrt><msub><mi>a</mi><mn>3</mn></msub></msqrt></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mn>1</mn><mrow><msqrt><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></msqrt><mo>+</mo><msqrt><msub><mi>a</mi><mi>n</mi></msub></msqrt></mrow></mfrac></mrow></mfenced></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mi>d</mi></msqrt></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>d</mi></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><msub><mi>a</mi><mi>n</mi></msub></math> are terms of an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi></math>, </p><p>So common difference will be, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><msub><mi>a</mi><mn>2</mn></msub><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><msub><mi>a</mi><mn>3</mn></msub><mo>-</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>=</mo><msub><mi>a</mi><mi>n</mi></msub><mo>-</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></math></p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msqrt><mfrac><mi>d</mi><mi>n</mi></mfrac></msqrt><mfenced><mrow><mfrac><mn>1</mn><mrow><msqrt><msub><mi>a</mi><mn>1</mn></msub></msqrt><mo>+</mo><msqrt><msub><mi>a</mi><mn>2</mn></msub></msqrt></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><msqrt><msub><mi>a</mi><mn>2</mn></msub></msqrt><mo>+</mo><msqrt><msub><mi>a</mi><mn>3</mn></msub></msqrt></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mn>1</mn><mrow><msqrt><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></msqrt><mo>+</mo><msqrt><msub><mi>a</mi><mi>n</mi></msub></msqrt></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msqrt><mfrac><mi>d</mi><mi>n</mi></mfrac></msqrt><mfenced><mrow><mfrac><mrow><msqrt><msub><mi>a</mi><mn>2</mn></msub></msqrt><mo>-</mo><msqrt><msub><mi>a</mi><mn>1</mn></msub></msqrt></mrow><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub></mrow></mfrac><mo>+</mo><mfrac><mrow><msqrt><msub><mi>a</mi><mn>3</mn></msub></msqrt><mo>-</mo><msqrt><msub><mi>a</mi><mn>2</mn></msub></msqrt></mrow><mrow><msub><mi>a</mi><mn>3</mn></msub><mo>-</mo><msub><mi>a</mi><mn>2</mn></msub></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mrow><msqrt><msub><mi>a</mi><mi>n</mi></msub></msqrt><mo>-</mo><msqrt><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></msqrt></mrow><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>-</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msqrt><mfrac><mi>d</mi><mi>n</mi></mfrac></msqrt><mo>&#215;</mo><mfrac><mn>1</mn><mi>d</mi></mfrac><mfenced><mrow><msqrt><msub><mi>a</mi><mi>n</mi></msub></msqrt><mo>-</mo><msqrt><msub><mi>a</mi><mn>1</mn></msub></msqrt></mrow></mfenced></math></p><p>Now using the formula <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><msqrt><mi>d</mi></msqrt></mfrac><mfenced><mfrac><mrow><msqrt><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>d</mi></msqrt><mo>-</mo><msqrt><msub><mi>a</mi><mn>1</mn></msub></msqrt></mrow><msqrt><mi>n</mi></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><msqrt><mi>d</mi></msqrt></mfrac><mfenced><mfrac><mrow><msqrt><mi>n</mi></msqrt><mfenced><mrow><msqrt><mstyle displaystyle="true"><mfrac><msub><mi>a</mi><mn>1</mn></msub><mi>n</mi></mfrac></mstyle><mo>+</mo><mi>d</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mi>d</mi><mi>n</mi></mfrac></mstyle></msqrt><mo>-</mo><msqrt><mstyle displaystyle="true"><mfrac><msub><mi>a</mi><mn>1</mn></msub><mi>n</mi></mfrac></mstyle></msqrt></mrow></mfenced></mrow><msqrt><mi>n</mi></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><msqrt><mi>d</mi></msqrt></mfrac><mfenced><mfenced><mrow><msqrt><mn>0</mn><mo>+</mo><mi>d</mi><mo>-</mo><mn>0</mn></msqrt><mo>-</mo><msqrt><mn>0</mn></msqrt></mrow></mfenced></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><msqrt><mi>d</mi></msqrt></mfrac><mo>&#215;</mo><msqrt><mi>d</mi></msqrt><mo>=</mo><mn>1</mn></math></p></blockquote>

</details>

---

### Q44. JEE Main 2023 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>The sum of the common terms of the following three arithmetic progressions.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>,</mo><mn>15</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mn>399</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>11</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>359</mn></math>  and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>12</mn><mo>,</mo><mn>17</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mn>197</mn></math>, is equal to _____ .</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **321**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>:</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>11</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>359</mn></math></p><p>Common difference is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>:</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>,</mo><mn>15</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>399</mn></math></p><p>Common difference is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>3</mn></msub><mo>:</mo><mn>2</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>12</mn><mo>,</mo><mn>17</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>197</mn></math></p><p>Common difference is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>3</mn></msub><mo>=</mo><mn>5</mn></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LCM</mi></math> of common difference we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LCM</mi><mfenced><mrow><msub><mi>d</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>d</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>d</mi><mn>3</mn></msub></mrow></mfenced><mo>=</mo><mn>60</mn></math></p><p>So, common terms are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>47</mn><mo>,</mo><mn>107</mn><mo>,</mo><mn>167</mn></math>,</p><p>Hence, the sum will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>47</mn><mo>+</mo><mn>107</mn><mo>+</mo><mn>167</mn><mo>=</mo><mn>321</mn></math>.</p>

</details>

---

### Q45. JEE Main 2023 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>-digit numbers, that are divisible by either <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> but not divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **514**

**Detailed Solution:**

<p>We know that total number of three-digit number will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>900</mn></math>,</p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>A</mi></mfenced></math> be number of three-digit number which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, i.e,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>100</mn><mo>,</mo><mn>102</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>998</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mn>450</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>B</mi></mfenced></math> be number of three-digit number which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>, i.e, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>102</mn><mo>,</mo><mn>105</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>999</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mn>300</mn></math></p><p>Numbers divisible by both <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>102</mn><mo>,</mo><mn>108</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>996</mn></mrow></mfenced></math> i.e, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn></math></p><p>Numbers divisible by both <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>112</mn><mo>,</mo><mn>126</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>994</mn></mrow></mfenced></math> i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math> numbers.</p><p>Numbers divisible by both <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>105</mn><mo>,</mo><mn>126</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>987</mn></mrow></mfenced></math> i.e, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>43</mn></math> numbers.</p><p>Numbers divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>3</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>7</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>126</mn><mo>,</mo><mn>168</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>966</mn></mrow></mfenced></math> i.e, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math> numbers.</p><p>Required number</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>450</mn><mo>+</mo><mn>150</mn><mo>-</mo><mn>64</mn><mo>-</mo><mn>43</mn><mo>+</mo><mn>21</mn><mo>=</mo><mn>514</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>514</mn></math> three-digit number are there which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><mtext>but&#160;not&#160;divisible&#160;by</mtext><mo>&#160;</mo><mn>7</mn></math>.</p>

</details>

---

### Q46. JEE Main 2023 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>8</mn><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>.</mo><msub><mi>a</mi><mi>n</mi></msub></math> be an A.P. If the sum of its first four terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> and the sum of its last four terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>170</mn></math> , then the product of its middle two terms is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **754**

**Detailed Solution:**

<p>Let the common difference of an A.P. be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub><mo>=</mo><mn>50</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>a</mi><mo>+</mo><mn>6</mn><mi>d</mi><mo>=</mo><mn>50</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>32</mn><mo>+</mo><mn>6</mn><mi>d</mi><mo>=</mo><mn>50</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mn>3</mn></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></msub><mo>+</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msub><mo>+</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>170</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mn>4</mn><mi>n</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mo>&#183;</mo><mi>d</mi><mo>=</mo><mn>170</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>32</mn><mo>+</mo><mfenced><mrow><mn>4</mn><mi>n</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mo>&#183;</mo><mn>3</mn><mo>=</mo><mn>170</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>14</mn></math></p><p>So, middle terms are </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>7</mn></msub><mo>=</mo><mi>a</mi><mo>+</mo><mn>6</mn><mi>d</mi><mo>=</mo><mn>26</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>8</mn></msub><mo>=</mo><mi>a</mi><mo>+</mo><mn>7</mn><mi>d</mi><mo>=</mo><mn>29</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi mathvariant="normal">a</mi><mn>7</mn></msub><mo>&#183;</mo><msub><mi mathvariant="normal">a</mi><mn>8</mn></msub><mo>=</mo><mn>754</mn></math></p>

</details>

---

### Q47. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo></math>. be an A.P. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>7</mn></msub><mo>=</mo><mn>3</mn></math>, the product <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>4</mn></msub></mrow></mfenced></math> is minimum and the sum of its first <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> terms is zero then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>!</mo><mo>-</mo><mn>4</mn><msub><mi>a</mi><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></msub></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>381</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>33</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>**

**Detailed Solution:**

<p>We know the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term of an A.P. is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>7</mn></msub><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mn>6</mn><mi>d</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mn>3</mn><mo>-</mo><mn>6</mn><mi>d</mi></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>4</mn></msub><mo>=</mo><mi>a</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mn>3</mn><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>3</mn><mo>-</mo><mn>6</mn><mi>d</mi></mrow></mfenced><mfenced><mrow><mn>3</mn><mo>-</mo><mn>3</mn><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>18</mn><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><mn>27</mn><mi>d</mi><mo>+</mo><mn>9</mn></math></p><p>Given product <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>4</mn></msub></mrow></mfenced></math> is minimum then,</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>d</mi><mo>)</mo><mo>=</mo><mn>18</mn><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><mn>27</mn><mi>d</mi><mo>+</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>d</mi><mo>)</mo><mo>=</mo><mn>36</mn><mi>d</mi><mo>-</mo><mn>27</mn></math></p><p>Product to be minimum, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>d</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>36</mn><mi>d</mi><mo>-</mo><mn>27</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mfrac><mn>27</mn><mn>36</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mo>-</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>5</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>!</mo><mo>-</mo><mn>4</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>+</mo><mn>2</mn><mo>)</mo></mrow></msub><mo>=</mo><mn>5</mn><mo>!</mo><mo>-</mo><mn>4</mn><msub><mi>a</mi><mn>35</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>120</mn><mo>-</mo><mn>4</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mn>34</mn><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>120</mn><mo>-</mo><mn>4</mn><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mn>34</mn><mo>&#215;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>120</mn><mo>+</mo><mn>6</mn><mo>-</mo><mn>102</mn><mo>=</mo><mn>24</mn></math></p>

</details>

---

### Q48. JEE Main 2023 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>-digit numbers that are less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2800</mn></math> and either divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> or by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> , is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **710**

**Detailed Solution:**

<p>Four-digit numbers that are less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2800</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1000</mn><mo>,</mo><mn>1001</mn><mo>,</mo><mn>1002</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>2800</mn></mrow></mfenced></math></p><p>Numbers divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1002</mn><mo>,</mo><mo>&#160;</mo><mn>1005</mn><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>2796</mn><mo>,</mo><mn>2799</mn></mrow></mfenced></math></p><p>Let total numbers be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1002</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mn>3</mn><mo>=</mo><mn>2799</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>600</mn></math></p><p>Numbers divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1001</mn><mo>,</mo><mo>&#160;</mo><mn>1012</mn><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><mn>2794</mn></mrow></mfenced></math></p><p>Let total numbers be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2794</mn><mo>=</mo><mn>1001</mn><mo>+</mo><mfenced><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mn>164</mn></math></p><p>Numbers divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math> are</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1023</mn><mo>,</mo><mn>1056</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>2772</mn></mrow></mfenced></math></p><p>Let total numbers be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2772</mn><mo>=</mo><mn>1023</mn><mo>+</mo><mfenced><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>33</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>54</mn></math></p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>-digit numbers that are less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2800</mn></math> and either divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> or by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> , is equal to<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>600</mn><mo>+</mo><mn>164</mn><mo>-</mo><mn>54</mn><mo>=</mo><mn>710</mn></math></p>

</details>

---

### Q49. JEE Main 2023 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>a</mi><mi>n</mi></msub></math> be in A.P. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>5</mn></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mn>7</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>11</mn></msub><mo>=</mo><mn>18</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mfenced><mrow><mfrac><mn>1</mn><mrow><msqrt><msub><mi>a</mi><mn>10</mn></msub></msqrt><mo>+</mo><msqrt><msub><mi>a</mi><mn>11</mn></msub></msqrt></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><msqrt><msub><mi>a</mi><mn>11</mn></msub></msqrt><mo>+</mo><msqrt><msub><mi>a</mi><mn>12</mn></msub></msqrt></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mfrac><mn>1</mn><mrow><msqrt><msub><mi>a</mi><mn>17</mn></msub></msqrt><mo>+</mo><msqrt><msub><mi>a</mi><mn>18</mn></msub></msqrt></mrow></mfrac></mrow></mfenced></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>Let the common difference of an A.P. be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>a</mi><mn>7</mn></msub><mo>=</mo><msub><mi>a</mi><mn>5</mn></msub></math>   (given)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>6</mn><mi>d</mi></mrow></mfenced><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>4</mn><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>8</mn><mi>d</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>11</mn></msub><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>10</mn><mi>d</mi><mo>=</mo><mn>18</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mn>72</mn><mo>,</mo><mi>d</mi><mo>=</mo><mn>9</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>18</mn></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>17</mn><mi>d</mi><mo>=</mo><mo>-</mo><mn>72</mn><mo>+</mo><mn>153</mn><mo>=</mo><mn>81</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>10</mn></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>9</mn><mi>d</mi><mo>=</mo><mn>9</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mfenced><mrow><mfrac><mn>1</mn><mrow><msqrt><msub><mi>a</mi><mn>10</mn></msub></msqrt><mo>+</mo><msqrt><msub><mi>a</mi><mn>11</mn></msub></msqrt></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><msqrt><msub><mi>a</mi><mn>11</mn></msub></msqrt><mo>+</mo><msqrt><msub><mi>a</mi><mn>12</mn></msub></msqrt></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mfrac><mn>1</mn><mrow><msqrt><msub><mi>a</mi><mn>17</mn></msub></msqrt><mo>+</mo><msqrt><msub><mi>a</mi><mn>18</mn></msub></msqrt></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>12</mn><mfenced><mrow><mfrac><mrow><msqrt><msub><mi>a</mi><mn>11</mn></msub></msqrt><mo>-</mo><msqrt><msub><mi>a</mi><mn>10</mn></msub></msqrt></mrow><mrow><mo>&#160;</mo><mi>d</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><msqrt><msub><mi>a</mi><mn>12</mn></msub></msqrt><mo>-</mo><msqrt><msub><mi>a</mi><mn>11</mn></msub></msqrt></mrow><mrow><mo>&#160;</mo><mi>d</mi></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mfrac><mrow><msqrt><msub><mi>a</mi><mn>18</mn></msub></msqrt><mo>-</mo><msqrt><msub><mi>a</mi><mn>17</mn></msub></msqrt></mrow><mrow><mo>&#160;</mo><mi>d</mi></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>12</mn><mfenced><mfrac><mrow><msqrt><msub><mi>a</mi><mn>18</mn></msub></msqrt><mo>-</mo><msqrt><msub><mi>a</mi><mn>10</mn></msub></msqrt></mrow><mi>d</mi></mfrac></mfenced><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mrow><mn>12</mn><mfenced><mrow><mn>9</mn><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mn>9</mn></mfrac><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q50. JEE Main 2023 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>The <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>8</mn><mtext>th&#160;</mtext></msup></math> common term of the series
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>15</mn><mo>+</mo><mn>19</mn><mo>+</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>21</mn><mo>+</mo><mo>&#8230;</mo></math>. is</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **151**

**Detailed Solution:**

<p>Given,</p><p>Two A.P&#39;s  as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>,</mo><mn>15</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> </p><p>First term<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>a</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>3</mn></math></p><p>Common difference<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>d</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>4</mn></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>11</mn><mo>,</mo><mn>16</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo></math>,</p><p>First term<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>a</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>1</mn></math></p><p>Common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>d</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>5</mn></math></p><p>Now, common difference of the series of the common terms of the given A.P&#39;s is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mi>LCM</mi><mfenced><mrow><msub><mi>d</mi><mn>1</mn></msub><mo>,</mo><msub><mi>d</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mi>LCM</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>20</mn></math></p><p>Now, series of common term is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>,</mo><mn>31</mn><mo>,</mo><mn>51</mn><mo>,</mo><mn>71</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>8</mn><mi>th</mi></msup></math> common term appearing in the both the series is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>8</mn></msub><mo>=</mo><mn>11</mn><mo>+</mo><mfenced><mrow><mn>8</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>8</mn></msub><mo>=</mo><mn>11</mn><mo>+</mo><mn>7</mn><mo>&#215;</mo><mn>20</mn><mo>=</mo><mn>151</mn></math></p>

</details>

---

### Q51. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> digit numbers, that are divisible by either <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> but not divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math> , is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>472</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>432</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>507</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>432</mn></math>**

**Detailed Solution:**

<p>We know that,</p><p>Total number of three digit number will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>999</mn><mo>-</mo><mn>99</mn><mo>=</mo><mn>900</mn></math>,</p><p>Now,</p><p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo></math> digit number which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mfrac><mn>900</mn><mn>3</mn></mfrac></mfenced><mo>=</mo><mn>300</mn></math>,</p><p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo></math> digit number which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mfrac><mn>900</mn><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>225</mn></math>,</p><p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo></math> digit number which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>4</mn></math> both will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mfrac><mn>900</mn><mn>12</mn></mfrac></mfenced><mo>=</mo><mn>75</mn></math>,</p><p>So , number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo></math> digit number which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mn>4</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>300</mn><mo>+</mo><mn>225</mn><mo>-</mo><mn>75</mn><mo>=</mo><mn>450</mn></math>,</p><p>Now, number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo></math> digit number which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mfrac><mn>900</mn><mn>48</mn></mfrac></mfenced><mo>=</mo><mn>18</mn></math></p><p>So, number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo></math> digit number which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mn>4</mn><mo>&#160;</mo><mtext>but&#160;not</mtext><mo>&#160;</mo><mn>48</mn></math> will be </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>450</mn><mo>-</mo><mn>18</mn><mo>=</mo><mn>432</mn></math></p>

</details>

---

### Q52. JEE Main 2023 (25 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>,</mo><msub><mi>A</mi><mn>2</mn></msub><mo>,</mo><msub><mi>A</mi><mn>3</mn></msub></math> be the three A.P. with the same common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> and having their first terms as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>A</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>A</mi><mo>+</mo><mn>2</mn></math>, respectively. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></math> be the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mtext>th&#160;</mtext></msup><mo>,</mo><msup><mn>9</mn><mtext>th&#160;</mtext></msup><mo>,</mo><msup><mn>17</mn><mtext>th&#160;</mtext></msup></math> terms of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>A</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>A</mi><mn>3</mn></msub></math>, respectively such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mn>7</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>b</mi></mtd><mtd><mn>17</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mn>17</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mn>70</mn><mo>=</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>29</mn></math>, then the sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> terms of an AP whose first term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>-</mo><mi>a</mi><mo>-</mo><mi>b</mi></math> and common difference is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mn>12</mn></mfrac></math>, is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **495**

**Detailed Solution:**

<p>From the definition of A.P., we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>A</mi><mo>+</mo><mn>6</mn><mi>d</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mi>A</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>8</mn><mi>d</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mi>A</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>16</mn><mi>d</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>iii</mi></mfenced></math></p><p>Now, we are given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mn>7</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>b</mi></mtd><mtd><mn>17</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mn>17</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mn>70</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mi>A</mi><mo>+</mo><mn>6</mn><mi>d</mi></mtd><mtd><mn>7</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>A</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>16</mn><mi>d</mi></mtd><mtd><mn>17</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>A</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>16</mn><mi>d</mi></mtd><mtd><mn>17</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mn>70</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mi>A</mi><mo>+</mo><mn>6</mn><mi>d</mi></mtd><mtd><mn>7</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mo>+</mo><mn>4</mn><mi>d</mi></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>A</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mn>70</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mi>A</mi><mo>+</mo><mn>70</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mo>-</mo><mn>7</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>A</mi><mo>+</mo><mn>6</mn><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>29</mn><mo>=</mo><mo>-</mo><mn>7</mn><mo>+</mo><mn>6</mn><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>c</mi><mo>-</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>d</mi><mo>-</mo><mi>A</mi><mo>=</mo><mn>13</mn><mo>+</mo><mn>7</mn><mo>=</mo><mn>20</mn></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mn>12</mn></mfrac><mo>=</mo><mfrac><mn>6</mn><mn>12</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>20</mn></msub><mo>=</mo><mfrac><mn>20</mn><mn>2</mn></mfrac><mfenced><mrow><mn>40</mn><mo>+</mo><mn>19</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>99</mn><mo>=</mo><mn>495</mn></math></p>

</details>

---

### Q53. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For three positive integers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>,</mo><mi>q</mi><mo>,</mo><mi>r</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mi>p</mi><msup><mi>q</mi><mn>2</mn></msup></mrow></msup><mo>=</mo><msup><mi>y</mi><mrow><mi>q</mi><mi>r</mi></mrow></msup><mo>=</mo><msup><mi>z</mi><mrow><msup><mi>p</mi><mn>2</mn></msup><mi>r</mi></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mi>p</mi><mi>q</mi><mo>+</mo><mn>1</mn></math> such that  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><msub><mi>log</mi><mi>y</mi></msub><mi>x</mi><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><msub><mi>log</mi><mi>z</mi></msub><mi>y</mi><mo>,</mo><mo>&#160;</mo><mn>7</mn><msub><mi>log</mi><mi>x</mi></msub><mi>z</mi><mo>&#160;</mo><mo>&#160;</mo></math>are in  A.P. with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>. The <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>-</mo><mi>p</mi><mo>-</mo><mi>q</mi><mo>&#160;</mo></math>is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mi>p</mi><msup><mi>q</mi><mn>2</mn></msup></mrow></msup><mo>=</mo><msup><mi>y</mi><mrow><mi>q</mi><mi>r</mi></mrow></msup><mo>=</mo><msup><mi>z</mi><mrow><msup><mi>p</mi><mn>2</mn></msup><mi>r</mi></mrow></msup><mo>=</mo><mi>&#955;</mi></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><msup><mi>q</mi><mn>2</mn></msup><mo>=</mo><msub><mi>log</mi><mi>x</mi></msub><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mi>r</mi><mo>=</mo><msub><mi>log</mi><mi>y</mi></msub><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mn>2</mn></msup><mi>r</mi><mo>=</mo><msub><mi>log</mi><mi>z</mi></msub><mi>&#955;</mi></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>log</mi><mi>y</mi></msub><mi>&#955;</mi></mrow><mrow><msub><mi>log</mi><mi>x</mi></msub><mi>&#955;</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>q</mi><mi>r</mi></mrow><mrow><mi>p</mi><msup><mi>q</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mi>y</mi></msub><mi>x</mi><mo>=</mo><mfrac><mi>r</mi><mrow><mi>p</mi><mi>q</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Similarly,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>x</mi></msub><mi>z</mi><mo>=</mo><mfrac><mrow><mi>p</mi><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><msup><mi>p</mi><mn>2</mn></msup><mi>r</mi></mrow></mfrac><mo>=</mo><mfrac><msup><mi>q</mi><mn>2</mn></msup><mrow><mi>p</mi><mi>r</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>z</mi></msub><mi>y</mi><mo>=</mo><mfrac><mrow><msup><mi>p</mi><mn>2</mn></msup><mi>r</mi></mrow><mrow><mi>q</mi><mi>r</mi></mrow></mfrac><mo>=</mo><mfrac><msup><mi>p</mi><mn>2</mn></msup><mi>q</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><msub><mi>log</mi><mi>y</mi></msub><mi>x</mi><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><msub><mi>log</mi><mi>z</mi></msub><mi>y</mi><mo>,</mo><mo>&#160;</mo><mn>7</mn><msub><mi>log</mi><mi>x</mi></msub><mi>z</mi><mo>&#160;</mo><mo>&#160;</mo></math> are in A.P., hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mfrac><mrow><mn>3</mn><mi>r</mi></mrow><mrow><mi>p</mi><mi>q</mi></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><msup><mi>p</mi><mn>2</mn></msup></mrow><mi>q</mi></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mi>p</mi><mi>r</mi></mrow></mfrac></math> are in A.P. Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>r</mi></mrow><mrow><mi>p</mi><mi>q</mi></mrow></mfrac><mo>-</mo><mn>3</mn><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mfrac><mn>7</mn><mn>6</mn></mfrac><mi>p</mi><mi>q</mi></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mi>p</mi><mi>q</mi><mo>+</mo><mn>1</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mi>q</mi><mo>+</mo><mn>1</mn><mo>=</mo><mfrac><mn>7</mn><mn>6</mn></mfrac><mi>p</mi><mi>q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mi>q</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>7</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msup><mi>p</mi><mn>2</mn></msup></mrow><mi>q</mi></mfrac><mo>=</mo><mn>3</mn><mo>+</mo><mn>2</mn><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>3</mn><msup><mi>p</mi><mn>3</mn></msup></mrow><mrow><mi>p</mi><mi>q</mi></mrow></mfrac><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>p</mi><mn>3</mn></msup><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>q</mi><mo>=</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>-</mo><mi>p</mi><mo>-</mo><mi>q</mi><mo>=</mo><mn>7</mn><mo>-</mo><mn>2</mn><mo>-</mo><mn>3</mn><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q54. JEE Main 2022 (28 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>,</mo><mi>q</mi><mo>&#8712;</mo><mi>R</mi></math>, consider the real valued function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>p</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mi>q</mi><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>&#62;</mo><mn>0</mn></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>4</mn></msub></math> be in an arithmetic progression with mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> and positive common difference. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>f</mi><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced></mrow></mfenced><mo>=</mo><mn>500</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></math>, then the absolute difference between the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **50**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>p</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mi>q</mi><mo>=</mo><mn>0</mn></math></p><p>So, roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>+</mo><msqrt><mi>q</mi></msqrt><mo>,</mo><mi>p</mi><mo>-</mo><msqrt><mi>q</mi></msqrt></math></p><p>Now absolute difference between roots will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mi>q</mi></msqrt></math>.</p><p>Now given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><msub><mi>a</mi><mn>4</mn></msub></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi></math> and its mean is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><msub><mi>a</mi><mn>4</mn></msub></math>  be  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mi>p</mi><mo>-</mo><mn>3</mn><mi>d</mi><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mi>p</mi><mo>-</mo><mi>d</mi><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mi>p</mi><mo>+</mo><mi>d</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>a</mi><mn>4</mn></msub><mo>=</mo><mi>p</mi><mo>+</mo><mn>3</mn><mi>d</mi></math></p><p>Now given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced></mrow></mfenced><mo>=</mo><mn>500</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><msub><mi>a</mi><mn>4</mn></msub></mfenced></mrow></mfenced><mo>=</mo><mn>500</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><msup><mfenced><mrow><msub><mi>a</mi><mn>4</mn></msub><mo>-</mo><mi>p</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mi>q</mi></mrow></mfenced><mo>=</mo><mn>500</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msub><mi>a</mi><mn>4</mn></msub><mo>-</mo><mi>p</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mi>q</mi><mo>=</mo><mn>500</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><mi>q</mi><mo>=</mo><mn>500</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced></mrow></mfenced><mo>=</mo><mn>500</mn><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></math></p><p>We get <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><msub><mi>a</mi><mn>4</mn></msub></mfenced></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><msub><mi>a</mi><mn>3</mn></msub></mfenced></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msup><mfenced><mrow><msub><mi>a</mi><mn>4</mn></msub><mo>-</mo><mi>p</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><msup><mfenced><mrow><msub><mi>a</mi><mn>3</mn></msub><mo>-</mo><mi>p</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mi>q</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><mi>q</mi><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><mi>q</mi><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>q</mi><mo>=</mo><mn>10</mn><msup><mi>d</mi><mn>2</mn></msup><mo>&#8658;</mo><mi>q</mi><mo>=</mo><mn>5</mn><msup><mi>d</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mfrac><mi>q</mi><mn>5</mn></mfrac></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mfenced><mfrac><mi>q</mi><mn>5</mn></mfrac></mfenced><mo>-</mo><mi>q</mi><mo>=</mo><mn>500</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>4</mn><mi>q</mi></mrow><mn>5</mn></mfrac><mo>=</mo><mn>500</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>q</mi><mo>=</mo><mfrac><mrow><mn>500</mn><mo>&#215;</mo><mn>5</mn></mrow><mn>4</mn></mfrac></math></p><p>Now absolute difference is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mi>q</mi></msqrt><mo>=</mo><mn>2</mn><mo>&#215;</mo><msqrt><mfrac><mrow><mn>500</mn><mo>&#215;</mo><mn>5</mn></mrow><mn>4</mn></mfrac></msqrt><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>50</mn><mn>2</mn></mfrac><mo>=</mo><mn>50</mn></math></p></blockquote>

</details>

---

### Q55. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>a</mi><mi mathvariant="normal">n</mi></msub><mo>,</mo><mo>&#8230;</mo></math> be an arithmetic progression of natural numbers. If the ratio of the sum of the first five terms to the sum of first nine terms of the progression is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>:</mo><mn>17</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>110</mn><mo>&#60;</mo><msub><mi>a</mi><mn>15</mn></msub><mo>&#60;</mo><mn>120</mn></math>, then the sum of the first ten terms of the progression is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>290</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>380</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>460</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>510</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>380</mn></math>**

**Detailed Solution:**

<blockquote><p>Given the ratio of the sum of the first five terms to the sum of the first nine terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>:</mo><mn>17</mn></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>S</mi><mn>5</mn></msub><msub><mi>S</mi><mn>9</mn></msub></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>17</mn></mfrac><mo>&#8658;</mo><mfrac><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>4</mn><mi>d</mi></mrow></mfenced></mrow><mrow><mfrac><mn>9</mn><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>8</mn><mi>d</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>17</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>17</mn><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>4</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>9</mn><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>8</mn><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>34</mn><mi>a</mi><mo>+</mo><mn>68</mn><mi>d</mi><mo>=</mo><mn>18</mn><mi>a</mi><mo>+</mo><mn>72</mn><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mn>4</mn><mi>a</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>15</mn></msub><mo>=</mo><mi>a</mi><mo>+</mo><mn>14</mn><mi>d</mi><mo>=</mo><mn>57</mn><mi>a</mi></math></p><p>Also given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>110</mn><mo>&#60;</mo><msub><mi mathvariant="normal">a</mi><mn>15</mn></msub><mo>&#60;</mo><mn>120</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>110</mn><mo>&#60;</mo><mn>57</mn><mi mathvariant="normal">a</mi><mo>&#60;</mo><mn>120</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#8756;</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mn>8</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>10</mn></msub><mo>=</mo><mfrac><mn>10</mn><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>9</mn><mo>&#215;</mo><mn>8</mn></mrow></mfenced><mo>=</mo><mn>380</mn></math></p></blockquote>

</details>

---

### Q56. JEE Main 2022 (26 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Different A.P.&#39;s are constructed with the first term <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>, the last term <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>199</mn></math>, And integral common differences. The sum of the common differences of all such, A.P&#39;s having at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> terms and at most <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math> terms is.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **53**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mi>st</mi></msup></math> term of the A.P<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>100</mn><mo>=</mo><mi>a</mi></math></p><p>And the last term <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>199</mn><mo>=</mo><mi>L</mi></math></p><p>Let the three term be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>a</mi><mo>+</mo><mi>d</mi><mo>,</mo><mi>a</mi><mo>+</mo><mn>2</mn><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mi>L</mi><mo>=</mo><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mi>i</mi></msub><mo>=</mo><mfrac><mrow><mi>L</mi><mo>-</mo><mi>a</mi></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8594;</mo></math> number of terms</p><p>Now checking for what value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> we have integral common difference,</p><p>For, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>199</mn><mo>-</mo><mn>100</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>99</mn><mn>2</mn></mfrac><mo>&#8713;</mo><mi mathvariant="normal">I</mi></math></p><p>For, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>4</mn><mo>,</mo><msub><mrow><mo>&#160;</mo><mi>d</mi></mrow><mn>2</mn></msub><mo>=</mo><mfrac><mn>99</mn><mn>3</mn></mfrac><mo>=</mo><mn>33</mn><mo>&#8712;</mo><mi>I</mi></math></p><p>.</p><p>.</p><p>.</p><p>For, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>10</mn><mo>,</mo><msub><mrow><mo>&#160;</mo><mi>d</mi></mrow><mn>3</mn></msub><mo>=</mo><mfrac><mn>99</mn><mn>9</mn></mfrac><mo>=</mo><mn>11</mn><mo>&#8712;</mo><mi>I</mi></math></p><p>For, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>12</mn><mo>,</mo><msub><mrow><mo>&#160;</mo><mi>d</mi></mrow><mn>4</mn></msub><mo>=</mo><mfrac><mn>99</mn><mn>11</mn></mfrac><mo>=</mo><mn>9</mn><mo>&#8712;</mo><mi>I</mi></math></p><p>So, sum of all common difference that are integer will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8721;</mo><msub><mi>d</mi><mi>i</mi></msub><mo>=</mo><mn>33</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>9</mn><mo>=</mo><mn>53</mn></math></p></blockquote>

</details>

---

### Q57. JEE Main 2022 (26 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

The series of positive multiples of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> is divided into sets : <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mn>3</mn></mfenced><mo>,</mo><mfenced open="{" close="}"><mrow><mn>6</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>12</mn></mrow></mfenced><mo>,</mo><mfenced open="{" close="}"><mrow><mn>15</mn><mo>,</mo><mn>18</mn><mo>,</mo><mn>21</mn><mo>,</mo><mn>24</mn><mo>,</mo><mn>27</mn></mrow></mfenced><mo>,</mo><mo>&#8230;</mo></math> Then the sum of the elements in the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>11</mn><mrow><mi>th</mi><mo>&#160;</mo></mrow></msup></math> set is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6993**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mn>3</mn></mfenced><mo>,</mo><mfenced close="}" open="{"><mrow><mn>6</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>12</mn></mrow></mfenced><mo>,</mo><mfenced close="}" open="{"><mrow><mn>15</mn><mo>,</mo><mn>18</mn><mo>,</mo><mn>21</mn><mo>,</mo><mn>24</mn><mo>,</mo><mn>27</mn></mrow></mfenced><mo>,</mo><mo>&#8943;</mo></math></p><p>Now, the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>11</mn><mtext>th&#160;</mtext></msup></math> set will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mfenced><mn>10</mn></mfenced><mo>&#160;</mo><mn>2</mn><mo>=</mo><mn>21</mn></math> </p><p>The total number of elements up to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mtext>th</mtext></msup></math> set will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>19</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>10</mn><mn>2</mn></msup><mo>=</mo><mn>100</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>11</mn><mtext>th</mtext></msup></math> set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="}" open="{"><mrow><mn>3</mn><mo>&#183;</mo><mn>101</mn><mo>,</mo><mn>3</mn><mo>&#183;</mo><mn>102</mn><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>3</mn><mo>&#183;</mo><mn>121</mn></mrow></mfenced></math></p><p>Sum of these elements <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mfenced><mrow><mn>101</mn><mo>+</mo><mn>102</mn><mo>+</mo><mo>&#8943;</mo><mo>+</mo><mn>121</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>&#215;</mo><mfrac><mn>21</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfenced><mrow><mn>101</mn><mo>+</mo><mn>121</mn></mrow></mfenced><mo>=</mo><mn>6993</mn></math></p></blockquote>

</details>

---

### Q58. JEE Main 2022 (29 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mn>12</mn><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo></math> upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>78</mn></math> terms and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mn>13</mn><mo>,</mo><mo>&#160;</mo><mn>17</mn><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo></math> upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>59</mn></math> terms be two series. Then, the sum of the terms common to both the series is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2223**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn><mo>,</mo><mo>&#8943;</mo></math> upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>78</mn></math> terms</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>t</mi><mn>78</mn></msub><mo>=</mo><mn>3</mn><mo>+</mo><mn>77</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>234</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>13</mn><mo>,</mo><mo>&#8943;</mo></math> upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>59</mn></math> terms</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>t</mi><mn>59</mn></msub><mo>=</mo><mn>5</mn><mo>+</mo><mn>58</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>237</mn></math></p><p>Common difference of common terms <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>LCM</mi><mfenced close="}" open="{"><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>12</mn></math></p><p>First common term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> and last common term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>225</mn></math></p><p>So series will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>,</mo><mn>21</mn><mo>,</mo><mn>33</mn><mo>,</mo><mo>&#8943;</mo><mo>,</mo><mn>225</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>19</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mi>a</mi><mo>+</mo><mi>l</mi></mrow></mfenced><mo>=</mo><mfrac><mn>19</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>9</mn><mo>+</mo><mn>225</mn></mrow></mfenced><mo>=</mo><mn>2223</mn></math></p>

</details>

---

### Q59. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>&#8230;</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>,</mo><msub><mi>b</mi><mn>2</mn></msub><mo>,</mo><msub><mi>b</mi><mn>3</mn></msub><mo>&#8230;</mo><mo>.</mo></math> are A.P. and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><msub><mi>a</mi><mn>10</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><msub><mi>a</mi><mn>1</mn></msub><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>=</mo><msub><mi>a</mi><mn>10</mn></msub><msub><mi>b</mi><mn>10</mn></msub></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>4</mn></msub><msub><mi>b</mi><mn>4</mn></msub></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>28</mn><mn>27</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>28</mn><mn>24</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>23</mn><mn>26</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>22</mn><mn>23</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>28</mn><mn>27</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>b</mi><mn>1</mn></msub><mo>,</mo><msub><mi>b</mi><mn>2</mn></msub><mo>,</mo><msub><mi>b</mi><mn>3</mn></msub></math>.....are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi></math></p><p>Also given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>10</mn></msub><mo>=</mo><mn>3</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>=</mo><msub><mi>a</mi><mn>10</mn></msub><msub><mi>b</mi><mn>10</mn></msub></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>10</mn></msub><mo>=</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>10</mn></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Now using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term formula we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>10</mn></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>9</mn><msub><mi>d</mi><mi>a</mi></msub><mo>&#8658;</mo><mn>3</mn><mo>=</mo><mn>2</mn><mo>+</mo><mn>9</mn><msub><mi>d</mi><mi>a</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>d</mi><mi>a</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math></p><p>Using same formula we get,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>10</mn></msub><mo>=</mo><msub><mi>b</mi><mn>1</mn></msub><mo>+</mo><mn>9</mn><msub><mi>d</mi><mi>b</mi></msub></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>9</mn><msub><mi>d</mi><mi>b</mi></msub></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>d</mi><mi>b</mi></msub><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>54</mn></mfrac></math></p><p>Now calculating <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>4</mn></msub><msub><mi>b</mi><mn>4</mn></msub><mo>=</mo><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>d</mi><mi>a</mi></msub></mrow></mfenced><mfenced><mrow><msub><mi>b</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>d</mi><mi>b</mi></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mn>3</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></mrow></mfenced><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>3</mn><mo>&#215;</mo><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>54</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mfrac><mn>7</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>8</mn><mn>18</mn></mfrac><mo>=</mo><mfrac><mn>56</mn><mn>54</mn></mfrac><mo>=</mo><mfrac><mn>28</mn><mn>27</mn></mfrac></math></p>

</details>

---

### Q60. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mfenced open="{" close="}"><msub><mi>a</mi><mi>i</mi></msub></mfenced><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi mathvariant="normal">n</mi></msubsup></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is an even integer, is an arithmetic progression with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><mi>a</mi><mi>i</mi></msub><mo>=</mo><mn>192</mn><mo>,</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mfrac><mi>n</mi><mn>2</mn></mfrac></munderover><msub><mi>a</mi><mrow><mn>2</mn><mi>i</mi></mrow></msub><mo>=</mo><mn>120</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>96</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>96</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><mi>a</mi><mi>i</mi></msub><mo>=</mo><mn>192</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mo>&#160;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>192</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></mfenced><mo>=</mo><mn>192</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>384</mn><mi>n</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Also given <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mfrac><mi>n</mi><mn>2</mn></mfrac></munderover><msub><mi>a</mi><mrow><mn>2</mn><mi>i</mi></mrow></msub><mo>=</mo><mn>120</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><munder><munder><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub><mo>+</mo><msub><mi>a</mi><mn>6</mn></msub><mo>&#160;</mo><mo>&#8943;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>&#160;</mo></mrow><mo>&#9183;</mo></munder><mrow><mfrac><mi>n</mi><mn>2</mn></mfrac><mo>&#160;</mo><mi>terms</mi></mrow></munder><mo>=</mo><mn>120</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></mfenced><mo>=</mo><mn>120</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>480</mn><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>1</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>480</mn><mi>n</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>-</mo></math>equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>480</mn><mi>n</mi></mfrac><mo>-</mo><mfrac><mn>384</mn><mi>n</mi></mfrac><mo>=</mo><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>n</mi></mfrac><mfenced><mrow><mn>480</mn><mo>-</mo><mn>384</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>480</mn><mo>-</mo><mn>384</mn><mo>=</mo><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>96</mn></math></p>

</details>

---

### Q61. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo></math> be an A.P. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mn>10</mn></msub></mrow><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mi>p</mi></msub></mrow></mfrac><mo>=</mo><mfrac><mn>100</mn><msup><mi>p</mi><mn>2</mn></msup></mfrac><mo>,</mo><mo>&#160;</mo><mi>p</mi><mo>&#8800;</mo><mn>10</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>a</mi><mn>11</mn></msub><msub><mi>a</mi><mn>10</mn></msub></mfrac></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>21</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>100</mn><mn>121</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>21</mn><mn>19</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>121</mn><mn>100</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>21</mn><mn>19</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mn>10</mn></msub></mrow><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mi>p</mi></msub></mrow></mfrac><mo>=</mo><mfrac><msub><mi>S</mi><mn>10</mn></msub><msub><mi>S</mi><mi>p</mi></msub></mfrac><mo>=</mo><mfrac><mn>100</mn><msup><mi>p</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>10</mn><mn>2</mn></mfrac></mstyle><mfenced close="]" open="["><mrow><mn>2</mn><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>9</mn><mi>d</mi></mrow></mfenced></mrow><mrow><mstyle displaystyle="true"><mfrac><mi>p</mi><mn>2</mn></mfrac></mstyle><mfenced close="]" open="["><mrow><mn>2</mn><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mfenced><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>100</mn><msup><mi>p</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><mn>10</mn><mfenced close="]" open="["><mrow><mn>2</mn><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>9</mn><mi>d</mi></mrow></mfenced></mstyle><mstyle displaystyle="true"><mi>p</mi><mfenced close="]" open="["><mrow><mn>2</mn><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mfenced><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced></mstyle></mfrac><mo>=</mo><mfrac><mn>100</mn><msup><mi>p</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><mn>2</mn><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>9</mn><mi>d</mi></mstyle><mstyle displaystyle="true"><mn>2</mn><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mfenced><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mstyle></mfrac><mo>=</mo><mfrac><mn>10</mn><mi>p</mi></mfrac></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>p</mi><mi>a</mi><mo>+</mo><mn>9</mn><mi>p</mi><mi>d</mi><mo>=</mo><mn>20</mn><mi>a</mi><mo>+</mo><mn>10</mn><mi>p</mi><mi>d</mi><mo>-</mo><mn>10</mn><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>p</mi><mi>a</mi><mo>-</mo><mn>20</mn><mi>a</mi><mo>=</mo><mi>p</mi><mi>d</mi><mo>-</mo><mn>10</mn><mi>d</mi></math>        <math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mfenced><mrow><mi>p</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mo>=</mo><mi>d</mi><mfenced><mrow><mi>p</mi><mo>-</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>=</mo><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><mi>d</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>a</mi><mn>11</mn></msub><msub><mi>a</mi><mn>10</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mn>10</mn><mi>d</mi></mrow><mrow><mi>a</mi><mo>+</mo><mn>9</mn><mi>d</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>a</mi><mn>11</mn></msub><msub><mi>a</mi><mn>10</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mfenced><mrow><mstyle displaystyle="true"><mfrac><mi>a</mi><mi>d</mi></mfrac></mstyle><mo>+</mo><mn>10</mn></mrow></mfenced></mrow><mrow><mi>d</mi><mfenced><mrow><mstyle displaystyle="true"><mfrac><mi>a</mi><mi>d</mi></mfrac></mstyle><mo>+</mo><mn>9</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>a</mi><mn>11</mn></msub><msub><mi>a</mi><mn>10</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>10</mn></mrow><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>9</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>a</mi><mn>11</mn></msub><msub><mi>a</mi><mn>10</mn></msub></mfrac><mo>=</mo><mfrac><mn>21</mn><mn>19</mn></mfrac></math></p>

</details>

---

### Q62. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mfrac><mi>&#960;</mi><mn>9</mn></mfrac></mfenced><mo>,</mo><mi>x</mi><mo>,</mo><mi>tan</mi><mfenced><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></mfenced></math> are in arithmetic progression and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mfrac><mi>&#960;</mi><mn>9</mn></mfrac></mfenced><mo>,</mo><mi>y</mi><mo>,</mo><mi>tan</mi><mfenced><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></mfenced></math> are also in arithmetic progression, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>x</mi><mo mathvariant="italic">-</mo><mn>2</mn><mi>y</mi></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>tan</mi><mfrac><mi>&#960;</mi><mn>9</mn></mfrac><mo>+</mo><mi>tan</mi><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></mrow></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mo>=</mo><mi>tan</mi><mfrac><mi>&#960;</mi><mn>9</mn></mfrac><mo>+</mo><mi>tan</mi><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></math></p><p>so, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>tan</mi><mfrac><mi>&#960;</mi><mn>9</mn></mfrac><mo>+</mo><mi>tan</mi><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfenced><mrow><mi>tan</mi><mfrac><mi>&#960;</mi><mn>9</mn></mfrac><mo>+</mo><mi>tan</mi><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mfrac><mrow><mi>cot</mi><mfrac><mi>&#960;</mi><mn>9</mn></mfrac><mo>-</mo><mi>tan</mi><mfrac><mi>&#960;</mi><mn>9</mn></mfrac></mrow><mn>2</mn></mfrac><mo>-</mo><mi>tan</mi><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mfrac><mrow><msup><mi>cot</mi><mn>2</mn></msup><mfrac><mi>&#960;</mi><mn>9</mn></mfrac><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>c</mi><mi>o</mi><mi>t</mi><mfrac><mi>&#960;</mi><mn>9</mn></mfrac></mrow></mfrac><mo>-</mo><mi>tan</mi><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mi>cot</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>-</mo><mi>tan</mi><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><mi>tan</mi><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac><mo>=</mo><mi>c</mi><mi>o</mi><mi>t</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></mrow></mfenced><mo>=</mo><mi>cot</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></mfenced><mspace linebreak="newline"></mspace></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><mi>tan</mi><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac><mo>=</mo><mi>c</mi><mi>o</mi><mi>t</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></mrow></mfenced><mo>=</mo><mi>cot</mi><mfrac><mi>&#960;</mi><mn>9</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><mfrac><mrow><msup><mi>cot</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>c</mi><mi>o</mi><mi>t</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mi>c</mi><mi>o</mi><mi>t</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced></math></p>

</details>

---

### Q63. JEE Main 2021 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>3</mn></msub><mn>2</mn><mo>,</mo><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>5</mn></mrow></mfenced><mo>,</mo><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></mrow></mfenced></math> are in an arithmetic progression, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>3</mn></msub><mn>2</mn><mo>,</mo><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>5</mn></mrow></mfenced><mo>,</mo><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></mrow></mfenced></math> are in arithmetic progression, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mn>3</mn></msub><mn>2</mn><mo>+</mo><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mn>3</mn></msub><msup><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msub><mi>log</mi><mn>3</mn></msub><mn>2</mn><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>x</mi></msup><mo>=</mo><mi>t</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>3</mn></msub><msup><mfenced><mrow><mi>t</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msub><mi>log</mi><mn>3</mn></msub><mn>2</mn><mfenced><mrow><mi>t</mi><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>t</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>t</mi><mo>-</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>t</mi><mo>+</mo><mn>32</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>t</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>t</mi><mo>-</mo><mn>8</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mi>x</mi></msup><mo>=</mo><mn>4</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>x</mi></msup><mo>=</mo><mn>8</mn></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mn>2</mn><mo>,</mo></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><mn>4</mn><mo>-</mo><mn>5</mn></mrow></mfenced></math> does not exist. </p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q64. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub></math> be the sum of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> terms of an arithmetic progression. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mrow><mn>3</mn><mi>n</mi></mrow></msub><mo>=</mo><mn>3</mn><msub><mi>S</mi><mrow><mn>2</mn><mi>n</mi></mrow></msub></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>S</mi><mrow><mn>4</mn><mi>n</mi></mrow></msub><msub><mi>S</mi><mrow><mn>2</mn><mi>n</mi></mrow></msub></mfrac></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> be first term and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> be common difference of this A.P.</p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mrow><mn>3</mn><mi>n</mi></mrow></msub><mo>=</mo><mn>3</mn><msub><mi>S</mi><mrow><mn>2</mn><mi>n</mi></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mn>3</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mo>&#215;</mo><mfrac><mrow><mn>2</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mo>(</mo><mn>3</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>d</mi><mo>=</mo><mn>4</mn><mi>a</mi><mo>+</mo><mo>(</mo><mn>4</mn><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>d</mi><mo>=</mo><mn>0</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>S</mi><mrow><mn>4</mn><mi>n</mi></mrow></msub><msub><mi>S</mi><mrow><mn>2</mn><mi>n</mi></mrow></msub></mfrac><mo>=</mo><mfrac><mrow><mfrac><mrow><mn>4</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mn>4</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>2</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mfenced open="[" close="]"><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mo>+</mo><mn>3</mn><mi>n</mi><mi>d</mi></mrow></mfenced></mrow><mfenced open="[" close="]"><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mo>+</mo><mi>n</mi><mi>d</mi></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>6</mn><mi>n</mi><mi>d</mi></mrow><mrow><mi>n</mi><mi>d</mi></mrow></mfrac><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q65. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub></math> denote the sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>-terms of an arithmetic progression. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>10</mn></msub><mo>=</mo><mn>530</mn><mo>,</mo><msub><mrow><mo>&#160;</mo><mi>S</mi></mrow><mn>5</mn></msub><mo>=</mo><mn>140</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>20</mn></msub><mo>-</mo><msub><mi>S</mi><mn>6</mn></msub></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1862</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1842</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1852</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1872</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1862</mn></math>**

**Detailed Solution:**

<blockquote><p>We know that the sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> terms of an arithmetic progression with its first term as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced><mo>.</mo></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>10</mn></msub><mo>=</mo><mn>530</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>10</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>9</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>530</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>9</mn><mi>d</mi><mo>=</mo><mn>106</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>5</mn></msub><mo>=</mo><mn>140</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>4</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>140</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>4</mn><mi>d</mi><mo>=</mo><mn>56</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Subtracting the two equation, we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>d</mi><mo>=</mo><mn>50</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mn>10</mn></math></p><p>On putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> in the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>56</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>8</mn><mo>.</mo></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>20</mn></msub><mo>-</mo><msub><mi>S</mi><mn>6</mn></msub><mo>=</mo><mfrac><mn>20</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>19</mn><mi>d</mi></mrow></mfenced><mo>-</mo><mfrac><mn>6</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>5</mn><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>14</mn><mi>a</mi><mo>+</mo><mn>175</mn><mo>&#160;</mo><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mn>14</mn><mo>&#215;</mo><mn>8</mn><mo>)</mo><mo>+</mo><mo>(</mo><mn>175</mn><mo>&#215;</mo><mn>10</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1862</mn><mo>.</mo></math></p></blockquote>

</details>

---

### Q66. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If sum of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math> terms of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><msup><mn>9</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mn>9</mn><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mn>9</mn><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>504</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>243</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>81</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>81</mn></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><msub><mi>log</mi><msup><mn>9</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mn>9</mn><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mn>9</mn><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>log</mi><msup><mn>9</mn><mrow><mn>1</mn><mo>/</mo><mn>22</mn></mrow></msup></msub><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mn>2</mn><msub><mi>log</mi><mn>9</mn></msub><mi>x</mi><mo>+</mo><mn>3</mn><msub><mi>log</mi><mn>9</mn></msub><mi>x</mi><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mn>22</mn><msub><mi>log</mi><mn>9</mn></msub><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><msub><mi>log</mi><mn>9</mn></msub><mi>x</mi><mo>(</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>22</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><msub><mi>log</mi><mn>9</mn></msub><mi>x</mi><mfenced close="}" open="{"><mrow><mfrac><mn>21</mn><mn>2</mn></mfrac><mo>(</mo><mn>2</mn><mo>+</mo><mn>22</mn><mo>)</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mn>252</mn><msub><mi>log</mi><mn>9</mn></msub><mi>x</mi></math></p><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mn>504</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>252</mn><msub><mi>log</mi><mn>9</mn></msub><mi>x</mi><mo>=</mo><mn>504</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mn>9</mn></msub><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>81</mn></math></p>

</details>

---

### Q67. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> be the sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi></math> terms of an arithmetic progression. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> be the sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>n</mi></math> terms of the same arithmetic progression. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>S</mi><mn>2</mn></msub><mo>-</mo><msub><mi>S</mi><mn>1</mn></msub></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math>, then the sum of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>n</mi></math> terms of the arithmetic progression is equal to:<gwmw style="display:none;"></gwmw>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7000</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5000</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3000</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3000</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mrow><mn>2</mn><mi>n</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><msub><mi>S</mi><mrow><mn>4</mn><mi>n</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>4</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mn>4</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>2</mn></msub><mo>-</mo><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>4</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mo>[</mo><mn>2</mn><mi>a</mi><mo>+</mo><mo>(</mo><mn>4</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>d</mi><mo>]</mo><mo>-</mo><mfrac><mrow><mn>2</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mi>a</mi><mi>n</mi><mo>+</mo><mo>(</mo><mn>4</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mn>2</mn><mi>n</mi><mi>d</mi><mo>-</mo><mn>2</mn><mi>n</mi><mi>a</mi><mo>-</mo><mo>(</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>d</mi><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>n</mi><mi>a</mi><mo>+</mo><mi>n</mi><mi>d</mi><mo>[</mo><mn>8</mn><mi>n</mi><mo>-</mo><mn>2</mn><mo>-</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>]</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>n</mi><mi>a</mi><mo>+</mo><mi>n</mi><mi>d</mi><mo>[</mo><mn>6</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>]</mo><mo>=</mo><mn>1000</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mn>6</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mo>=</mo><mfrac><mn>1000</mn><mi>n</mi></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mrow><mn>6</mn><mi>n</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>6</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mn>6</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mi>n</mi><mo>&#183;</mo><mfrac><mn>1000</mn><mi>n</mi></mfrac><mo>=</mo><mn>3000</mn></math></p>

</details>

---

### Q68. JEE Main 2021 (17 Mar Shift 2)

*Type:* `numerical` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><msup><mn>4</mn><mi>x</mi></msup><mo>-</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><msup><mn>4</mn><mi>x</mi></msup><mo>+</mo><mfrac><mn>18</mn><mn>5</mn></mfrac></mrow></mfenced></math> are in arithmetic progression for a real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> then the value of the determinant <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></mtd><mtd><mi>x</mi><mo>-</mo><mn>1</mn></mtd><mtd><msup><mi>x</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math> is equal to:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>If three numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></math> are in arithmetic progression, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>b</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>c</mi><mo>.</mo></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><msup><mn>4</mn><mi>x</mi></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><msup><mn>4</mn><mi>x</mi></msup><mo>+</mo><mfrac><mn>18</mn><mn>5</mn></mfrac></mrow></mfenced></math> are in arithmetic progression, then we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><msup><mn>4</mn><mi>x</mi></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><msup><mn>4</mn><mi>x</mi></msup><mo>+</mo><mfrac><mn>18</mn><mn>5</mn></mfrac></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>10</mn></msub><msup><mi>m</mi><mi>n</mi></msup><mo>=</mo><mi>n</mi><msub><mi>log</mi><mn>10</mn></msub><mi>m</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>10</mn></msub><msup><mfenced><mrow><msup><mn>4</mn><mi>x</mi></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msub><mi>log</mi><mn>10</mn></msub><mfenced><mn>10</mn></mfenced><mo>+</mo><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><msup><mn>4</mn><mi>x</mi></msup><mo>+</mo><mfrac><mn>18</mn><mn>5</mn></mfrac></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>10</mn></msub><mfenced><mi>m</mi></mfenced><mo>+</mo><msub><mi>log</mi><mn>10</mn></msub><mfenced><mi>n</mi></mfenced><mo>=</mo><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><mi>m</mi><mi>n</mi></mrow></mfenced><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>10</mn></msub><msup><mfenced><mrow><msup><mn>4</mn><mi mathvariant="normal">x</mi></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><mn>10</mn><mfenced><mrow><msup><mn>4</mn><mi mathvariant="normal">x</mi></msup><mo>+</mo><mfrac><mn>18</mn><mn>5</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msup><mn>4</mn><mi mathvariant="normal">x</mi></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>10</mn><mfenced><mrow><msup><mn>4</mn><mi mathvariant="normal">x</mi></msup><mo>+</mo><mfrac><mn>18</mn><mn>5</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><msup><mn>4</mn><mi mathvariant="normal">x</mi></msup></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>-</mo><mn>4</mn><mo>&#183;</mo><msup><mn>4</mn><mi mathvariant="normal">x</mi></msup><mo>=</mo><mn>10</mn><mo>&#183;</mo><msup><mn>4</mn><mi mathvariant="normal">x</mi></msup><mo>+</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><msup><mn>4</mn><mi>x</mi></msup></mfenced><mn>2</mn></msup><mo>-</mo><mn>14</mn><mfenced><msup><mn>4</mn><mi>x</mi></msup></mfenced><mo>-</mo><mn>32</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mn>4</mn><mi>x</mi></msup><mo>-</mo><mn>16</mn></mrow></mfenced><mfenced><mrow><msup><mn>4</mn><mi mathvariant="normal">x</mi></msup><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>4</mn><mi mathvariant="normal">x</mi></msup><mo>=</mo><mn>16</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>4</mn><mi>x</mi></msup><mo>+</mo><mn>2</mn><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></mtd><mtd><mi>x</mi><mo>-</mo><mn>1</mn></mtd><mtd><msup><mi>x</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mfenced><mrow><mn>0</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>0</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mn>4</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>6</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>2</mn><mo>.</mo></math></p>

</details>

---

### Q69. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A man is walking on a straight line. The arithmetic mean of the reciprocals of the intercepts of this line on the coordinate axes is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>. Three stones <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> are placed at the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> respectively. Then which of these stones is<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>/</mo></math>are on the path of the man?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> only
- **(B)** All the three
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> only
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> only**

**Detailed Solution:**

Let the line be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><mi>c</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> - intercept : <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>c</mi><mi>m</mi></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> - intercept : <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">M</mi></math> of reciprocals of the intercepts :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mfrac><mi>m</mi><mi>c</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>c</mi></mfrac></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>m</mi></mrow></mfenced><mo>=</mo><mi>c</mi></math></p><p>line <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>:</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>m</mi></mrow></mfenced><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi>m</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> line always passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q70. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The common difference of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo><mo>&#160;</mo><msub><mi mathvariant="normal">b</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi mathvariant="normal">b</mi><mn>2</mn></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><msub><mi mathvariant="normal">b</mi><mi mathvariant="normal">m</mi></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> more than common difference of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo><mo>&#160;</mo><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></msub></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>40</mn></msub><mo>=</mo><mo>-</mo><mn>159</mn><mo>,</mo><mo>&#160;</mo><msub><mi mathvariant="normal">a</mi><mn>100</mn></msub><mo>=</mo><mo>-</mo><mn>399</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">b</mi><mn>100</mn></msub><mo>=</mo><msub><mi mathvariant="normal">a</mi><mn>70</mn></msub></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">b</mi><mn>1</mn></msub></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>81</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>127</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>81</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>127</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>81</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mn>1</mn><mo>,</mo></mrow></msub><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>d</mi><mrow><mn>1</mn><mo>,</mo></mrow></msub><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><mi>d</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math>first <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>40</mn></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>39</mn><mi>d</mi><mo>=</mo><mo>-</mo><mn>159</mn></math>.....................(1)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>100</mn></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>99</mn><mi>d</mi><mo>=</mo><mo>-</mo><mn>399</mn></math>....................(2)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mo>-</mo><mn>4</mn><mo>,</mo><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>now</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>100</mn></msub><mo>=</mo><msub><mi>a</mi><mn>70</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>b</mi><mn>1</mn></msub><mo>+</mo><mn>99</mn><mi>D</mi><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>69</mn><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>+</mo><mn>99</mn><mo>(</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>=</mo><mo>-</mo><mn>3</mn><mo>+</mo><mn>69</mn><mo>(</mo><mo>-</mo><mn>4</mn><mo>)</mo></math></p><p>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math>Accoding to question <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mi>d</mi><mo>+</mo><mn>2</mn></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mn>81</mn></math></p>

</details>

---

### Q71. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the sum of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> terms of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mfenced><msup><mn>7</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfenced></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><mfenced><msup><mn>7</mn><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mfenced></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><mfenced><msup><mn>7</mn><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfenced></msub><mi>x</mi><mo>+</mo><mo>&#8230;</mo></math>is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>460</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mrow><mn>46</mn><mo>/</mo><mn>21</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mn>2</mn></msup></math>**

**Detailed Solution:**

Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mfenced><msup><mn>7</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfenced></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><mfenced><msup><mn>7</mn><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mfenced></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><mfenced><msup><mn>7</mn><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfenced></msub><mi>x</mi><mo>+</mo><mo>&#8230;</mo><mn>20</mn></math> times <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>460</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mo>(</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>4</mn><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>21</mn><mo>)</mo><msub><mi>log</mi><mn>7</mn></msub><mi>x</mi><mo>=</mo><mn>460</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mn>20</mn><mn>2</mn></mfrac><mo>(</mo><mn>2</mn><mo>+</mo><mn>21</mn><mo>)</mo><msub><mi>log</mi><mn>7</mn></msub><mi>x</mi><mo>=</mo><mn>460</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msub><mi>log</mi><mn>7</mn></msub><mi>x</mi><mo>=</mo><mn>2</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mn>49</mn></math>

</details>

---

### Q72. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>,</mo><mn>14</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mn>4</mn><mo>-</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mrow></msup></math> are the first three terms of an A.P. for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> , then the sixth term of this A.P. is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>66</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>81</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>65</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>78</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>66</mn></math>**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></math> are in AP, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> is A.M of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>c</mi></math>. </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo><mi>b</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>28</mn><mo>=</mo><msup><mn>3</mn><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mn>3</mn><mrow><mn>4</mn><mo>-</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mrow></msup></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mrow></msup><mo>=</mo><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn><mo>=</mo><mfrac><mi>x</mi><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>81</mn><mi>x</mi></mfrac><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>84</mn><mi>x</mi><mo>+</mo><mn>243</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>81</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mn>3</mn><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mrow></msup><mo>=</mo><mn>3</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>&#8800;</mo><mn>2</mn></math></p><p>Terms are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>14</mn><mo>,</mo><mn>27</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo></math> then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>6</mn></msub><mo>=</mo><mn>1</mn><mo>+</mo><mn>5</mn><mo>(</mo><mn>13</mn><mo>)</mo><mo>=</mo><mn>66</mn></math></p><p> </p><p> </p>

</details>

---

### Q73. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mmultiscripts><mo>,</mo><mprescripts></mprescripts><mn>1</mn><none></none></mmultiscripts><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>a</mi><mi>n</mi></msub></math> be a given A.P. whose common difference is an integer and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>300</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>&#8804;</mo><mi>n</mi><mo>&#8804;</mo><mn>50</mn><mo>,</mo></math> then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi mathvariant="normal">S</mi><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></msub><mo>,</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></msub></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2490</mn><mo>,</mo><mn>249</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2480</mn><mo>,</mo><mn>249</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2480</mn><mo>,</mo><mn>248</mn><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2490</mn><mo>,</mo><mn>248</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2490</mn><mo>,</mo><mn>248</mn><mo>)</mo></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>300</mn><mo>=</mo><mn>1</mn><mo>+</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>d</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mfrac><mn>299</mn><mrow><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>13</mn><mo>&#215;</mo><mn>23</mn></mrow><mrow><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow></mfrac><mo>=</mo></math> integer
so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>-</mo><mn>1</mn><mo>=</mo><mo>&#177;</mo><mn>13</mn><mo>,</mo><mo>&#177;</mo><mn>23</mn><mo>,</mo><mo>&#177;</mo><mn>299</mn><mo>,</mo><mo>&#177;</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>n</mi><mo>=</mo><mn>14</mn><mo>,</mo><mo>-</mo><mn>12</mn><mo>,</mo><mn>24</mn><mo>,</mo><mo>-</mo><mn>22</mn><mo>,</mo><mn>300</mn><mo>,</mo><mo>-</mo><mn>298</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>0</mn></math>
But <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mo>[</mo><mn>15</mn><mo>,</mo><mo>&#160;</mo><mn>50</mn><mo>]</mo><mo>&#160;</mo><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>24</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mn>13</mn></math>
Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></msub><mo>=</mo><msub><mi>S</mi><mn>20</mn></msub><mo>=</mo><mfrac><mn>20</mn><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mn>2</mn><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mo>(</mo><mn>20</mn><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>13</mn><mo>)</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></msub><mo>=</mo><mn>2490</mn></math>
And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></msub><mo>=</mo><msub><mi>a</mi><mn>20</mn></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>19</mn><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>19</mn><mo>&#215;</mo><mn>13</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>248</mn></math></p>

</details>

---

### Q74. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the first term of an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo mathvariant="italic">.</mo><mi>P</mi><mo mathvariant="italic">.</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and the sum of its first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math> terms is equal to the sum of its next <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> terms, then the common difference of this <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math>is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>7</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>**

**Detailed Solution:**

<p>Sum of first<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math> terms=sum of next <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> terms</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>25</mn></msub><mo>=</mo><msub><mi>S</mi><mrow><mi>N</mi><mi>e</mi><mi>x</mi><mi>t</mi><mo>&#160;</mo><mn>15</mn></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>25</mn></msub><mo>+</mo><msub><mi>S</mi><mrow><mi>N</mi><mi>e</mi><mi>x</mi><mi>t</mi><mo>&#160;</mo><mn>15</mn></mrow></msub><mo>=</mo><msub><mi>S</mi><mn>40</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#215;</mo><msub><mi>S</mi><mn>25</mn></msub><mo>=</mo><msub><mi>S</mi><mn>40</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>25</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>24</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mfrac><mn>40</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>39</mn><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mfenced close="]" open="["><mrow><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>24</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>4</mn><mfenced close="]" open="["><mrow><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>39</mn><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>30</mn><mo>+</mo><mn>120</mn><mi>d</mi><mo>=</mo><mn>24</mn><mo>+</mo><mn>156</mn><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>36</mn><mi>d</mi><mo>=</mo><mn>6</mn><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p> </p><p> </p>

</details>

---

### Q75. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> terms of an A.P. ,<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>&#8230;</mo><mo>&#8230;</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>&#8800;</mo><mn>0</mn></mrow></mfenced></math> then the sum of the A.P <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><msub><mi>a</mi><mn>5</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><msub><mi>a</mi><mn>23</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><msub><mi>a</mi><mn>1</mn></msub></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>121</mn><mn>10</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>121</mn><mn>10</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>72</mn><mn>5</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>72</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>72</mn><mn>5</mn></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub></math> be the first term and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> be the common difference of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi mathvariant="normal">S</mi><mn>11</mn></msub><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mfrac><mn>11</mn><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>10</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><mo>+</mo><mn>5</mn><mi mathvariant="normal">d</mi><mo>=</mo><mn>0</mn></math></p><p> Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><msub><mi>a</mi><mn>5</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mn>23</mn></msub><mo>=</mo><mfrac><mn>12</mn><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mfenced><mrow><mn>12</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn><mi>d</mi></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>12</mn><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>11</mn><mi>d</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>12</mn><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>-</mo><mfrac><mrow><mn>11</mn><msub><mi>a</mi><mn>1</mn></msub></mrow><mn>5</mn></mfrac></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mrow><mn>72</mn><msub><mi>a</mi><mn>1</mn></msub></mrow><mn>5</mn></mfrac></math></p>

</details>

---

### Q76. JEE Main 2020 (09 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

The number of terms common to the two A.P.&rsquo;s <math><mn>3</mn><mo>,</mo><mi></mi><mn>7</mn><mo>,</mo><mi></mi><mn>11</mn><mo>,</mo><mi></mi><mo>&#8230;</mo><mo>,</mo><mi></mi><mn>407</mn></math> and <math><mn>2</mn><mo>,</mo><mi></mi><mn>9</mn><mo>,</mo><mi></mi><mn>16</mn><mo>,</mo><mi></mi><mo>&#8230;</mo><mo>,</mo><mi></mi><mn>709</mn></math> is ____________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<p>Common Difference of first series <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math></p><p>Common difference of second series <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn></math></p><p>First common term <math><mo>=</mo><mn>23</mn></math></p><p>Common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>L</mi><mo>.</mo><mi>C</mi><mo>.</mo><mi>M</mi><mfenced><mrow><mn>7</mn><mo>&#215;</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>28</mn></math></p><p>To find number of common terms we put</p><p>Last term <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mn>407</mn></math></p><p><math><mo>&#8658;</mo><mn>23</mn><mo>+</mo><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mn>28</mn><mi></mi><mo>&#8804;</mo><mn>407</mn></math></p><p><math><mo>&#8658;</mo><mi></mi><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mn>28</mn><mi></mi><mo>&#8804;</mo><mn>384</mn></math></p><p><math><mo>&#8658;</mo><mi>n</mi><mi></mi><mo>&#8804;</mo><mn>13.71</mn><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>&#8804;</mo><mn>14.71</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>14</mn></math></p>

</details>

---

### Q77. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the <math><msup><mrow><mn>10</mn></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math>, term of an A.P. is <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>20</mn></mrow></mfrac></math>, and its <math><msup><mrow><mn>20</mn></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math>, term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>10</mn></mfrac></math>, then the sum of its first <math><mn>200</mn></math>, terms is.

**Options:**

- **(A)** <math><mn>50</mn></math>
- **(B)** <math><mn>50</mn><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mn>100</mn></math>
- **(D)** <math><mn>100</mn><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>100</mn><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>d</mi></math> is the first term and common difference of arithmetic progression respectively, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>10</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>20</mn></mfrac><mo>=</mo><mi>a</mi><mo>+</mo><mn>9</mn><mi>d</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>20</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>=</mo><mi>a</mi><mo>+</mo><mn>19</mn><mi>d</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>After solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>, we get
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>200</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mfrac><mn>1</mn><mn>200</mn></mfrac></math></p><p>Now</p><p><math><msub><mrow><mi>S</mi></mrow><mrow><mn>200</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>200</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>200</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>199</mn></mrow><mrow><mn>200</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>201</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>100</mn><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>.</p>

</details>

---

### Q78. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be such that for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mfenced separators="|"><mrow><msup><mn>2</mn><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math> and <math><mfenced separators="|"><mrow><msup><mrow><mn>3</mn></mrow><mrow><mi>x</mi></mrow></msup><mo>+</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></math> are in A.P., then the minimum value of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><mn>0</mn></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>3</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced separators="|"><mfrac><mrow><msup><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>2</mn><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>3</mn><mi>x</mi></msup><mo>+</mo><msup><mn>3</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced separators="|"><mfrac><mrow><mn>2</mn><mfenced><mrow><msup><mn>3</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mn>3</mn><mi>x</mi></msup><mo>+</mo><msup><mn>3</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced separators="|"><mrow><mfenced><mrow><msup><mn>3</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfenced><mo>+</mo><mfenced><mfrac><mrow><msup><mn>3</mn><mi>x</mi></msup><mo>+</mo><msup><mn>3</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced></math></p><p>
Using <math><mi>A</mi><mi>M</mi><mo>&#8805;</mo><mi>G</mi><mi>M</mi></math>
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#8805;</mo><mn>3</mn></math></p>

</details>

---

### Q79. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Five numbers are in <math><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo><mo>,</mo><mi mathvariant="normal"></mi></math> whose sum is <math><mn>25</mn></math> and product is <math><mn>2520</mn><mo>.</mo></math> If one of these five numbers is <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi></mi></math> then the greatest number amongst them is

**Options:**

- **(A)** <math><mn>27</mn></math>
- **(B)** <math><mn>7</mn></math>
- **(C)** <math><mfrac><mrow><mn>21</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>16</mn></math>**

**Detailed Solution:**

Let term be <math><mi>a</mi><mo>-</mo><mn>2</mn><mi>d</mi><mo>,</mo><mi></mi><mi>a</mi><mo>-</mo><mi>d</mi><mo>,</mo><mi></mi><mi>a</mi><mo>,</mo><mi></mi><mi>a</mi><mo>+</mo><mi>d</mi><mo>,</mo><mi></mi><mi>a</mi><mo>+</mo><mn>2</mn><mi>d</mi></math>
Sum <math><mo>=</mo><mn>25</mn><mo>&#8658;</mo><mn>5</mn><mi>a</mi><mo>=</mo><mn>25</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>5</mn></math>
Product <math><mo>=</mo><mn>2520</mn></math>
<math><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mn>2</mn><mi>d</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mi>d</mi></mrow></mfenced><mn>5</mn><mfenced separators="|"><mrow><mn>5</mn><mo>+</mo><mi>d</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>5</mn><mo>+</mo><mn>2</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>2520</mn></math>
<math><mo>&#8658;</mo><mfenced separators="|"><mrow><mn>25</mn><mo>-</mo><mn>4</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mfenced separators="|"><mrow><mn>25</mn><mo>-</mo><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>=</mo><mn>504</mn></math>
<math><mo>&#8658;</mo><mn>625</mn><mo>-</mo><mn>100</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>25</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>=</mo><mn>504</mn></math>
<math><mo>&#8658;</mo><mn>4</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mn>125</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>625</mn><mo>-</mo><mn>504</mn><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mn>4</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mn>125</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>121</mn><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mn>4</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mn>121</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>121</mn><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mfenced separators="|"><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>4</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>121</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn><mo>,</mo><mi></mi><mi>d</mi><mo>=</mo><mo>&#8723;</mo><mfrac><mrow><mn>11</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mi>d</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn><mo>,</mo><mi></mi></math> does not give <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> as a term
<math><mo>&#8756;</mo><mi>d</mi><mo>=</mo><mfrac><mrow><mn>11</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mo>&#8756;</mo></math> Largest term <math><mo>=</mo><mn>5</mn><mo>+</mo><mn>2</mn><mi>d</mi><mo>=</mo><mn>5</mn><mo>+</mo><mn>11</mn><mo>=</mo><mn>16</mn></math>

</details>

---

### Q80. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> are in A.P. such that <math><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>7</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>16</mn></mrow></msub><mo>=</mo><mn>40</mn><mo>,</mo></math> then the sum of the first <math><mn>15</mn></math> terms of this A.P is:

**Options:**

- **(A)** <math><mn>280</mn></math>
- **(B)** <math><mn>120</mn></math>
- **(C)** <math><mn>150</mn></math>
- **(D)** <math><mn>200</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>200</mn></math>**

**Detailed Solution:**

Let the 1<sup>st</sup> terms of A.P. be <math><mi mathvariant="normal">&#39;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">&#39;</mi></math> and common difference <math><mi mathvariant="normal">&#39;</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">&#39;</mi></math> .
Given <math><mo>&#8201;</mo><msub><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>7</mn></mrow></msub><mo>+</mo><msub><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>16</mn></mrow></msub><mo>=</mo><mn>40</mn></math>
<math><mo>&#8658;</mo><mi mathvariant="normal">a</mi><mo>+</mo><mi mathvariant="normal">a</mi><mo>+</mo><mn>6</mn><mi mathvariant="normal">d</mi><mo>+</mo><mi mathvariant="normal">a</mi><mo>+</mo><mn>15</mn><mi mathvariant="normal">d</mi><mo>=</mo><mn>40</mn></math>
<math><mo>&#8658;</mo><mi mathvariant="normal">a</mi><mo>+</mo><mn>7</mn><mi mathvariant="normal">d</mi><mo>=</mo><mfrac><mrow><mn>40</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math> &hellip;.(1)
Sum of first <math><mn>15</mn></math> term
<math><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>15</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>[</mo><mn>2</mn><mi mathvariant="normal">a</mi><mo>+</mo><mn>14</mn><mi mathvariant="normal">d</mi><mo>]</mo></math>
<math><mo>=</mo><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mfrac><mrow><mn>40</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mn>200</mn></math>

</details>

---

### Q81. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><msub><mrow><mi>S</mi></mrow><mrow><mi>n</mi></mrow></msub></math> denote the sum of the first <math><mi>n</mi></math> terms of an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math>. If <math><msub><mrow><mi>S</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mn>16</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>6</mn></msub><mo>=</mo><mo>-</mo><mn>48</mn></math> , then <math><msub><mrow><mi>S</mi></mrow><mrow><mn>10</mn></mrow></msub></math> is equal to:

**Options:**

- **(A)** <math><mo>-</mo><mn>320</mn></math>
- **(B)** <math><mo>-</mo><mn>380</mn></math>
- **(C)** <math><mo>-</mo><mn>260</mn></math>
- **(D)** <math><mo>-</mo><mn>410</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>-</mo><mn>320</mn></math>**

**Detailed Solution:**

Let the first term of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> is <math><mi>&#8216;</mi><mi>a</mi><mi>&#8217;</mi></math> and the common difference is <math><mi>&#8216;</mi><mi>d</mi><mi>&#8217;</mi></math>.
<math><mo>&#8756;</mo><mtext>&#8201;</mtext><msub><mrow><mi>S</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced><mo>=</mo><mn>16</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>d</mi><mo>=</mo><mn>8</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math>
and <math><msub><mrow><mi>S</mi></mrow><mrow><mn>6</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced separators="|"><mrow><mn>6</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>48</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>5</mn><mi>d</mi><mo>=</mo><mo>-</mo><mn>16</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>
<math><mo>&#8756;</mo></math> From <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>i</mi><mo>)</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo></math>, <math><mi>a</mi><mo>=</mo><mn>22</mn></math> <math><mo>&#38;</mo></math> <math><mi>d</mi><mo>=</mo><mo>-</mo><mn>12</mn></math>
<math><mo>&#8756;</mo><mtext>&#8201;</mtext><msub><mrow><mi>S</mi></mrow><mrow><mn>10</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>10</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>(</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>9</mn><mi>d</mi><mo>)</mo><mo>=</mo><mn>5</mn><mfenced separators="|"><mrow><mn>2</mn><mo>&#215;</mo><mn>22</mn><mo>+</mo><mn>9</mn><mfenced separators="|"><mrow><mo>-</mo><mn>12</mn></mrow></mfenced></mrow></mfenced></math>
<math><mo>=</mo><mo>-</mo><mn>320</mn></math>

</details>

---

### Q82. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>3</mn></msub><mo>.</mo><mo>.</mo><mo>.</mo></math> be an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>6</mn></msub><mo>=</mo><mn>2</mn><mo>.</mo></math> Then, the common difference of this <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo><mo>,</mo></math> which maximise the product <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>&#183;</mo><msub><mi>a</mi><mn>4</mn></msub><mo>&#183;</mo><msub><mi>a</mi><mn>5</mn></msub><mo>,</mo></math>is :

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>6</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let, the first term of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> be <math><mi>a</mi></math> and common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>,</mo></math> then we know that the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math>term of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mo>.</mo></math></p><p>Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>6</mn></msub><mo>=</mo><mi>a</mi><mo>+</mo><mn>5</mn><mi>d</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mo>-</mo><mn>5</mn><mi>d</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>&#183;</mo><msub><mi>a</mi><mn>4</mn></msub><mo>&#183;</mo><msub><mi>a</mi><mn>5</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mo>=</mo><mi>a</mi><mo>&#183;</mo><mo>(</mo><mi>a</mi><mo>+</mo><mn>3</mn><mi>d</mi><mo>)</mo><mo>&#183;</mo><mo>(</mo><mi>a</mi><mo>+</mo><mn>4</mn><mi>d</mi><mo>)</mo></math></p><p>Put the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mo>=</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mn>5</mn><mi>d</mi></mrow></mfenced><mo>&#183;</mo><mo>(</mo><mn>2</mn><mo>-</mo><mn>5</mn><mi>d</mi><mo>+</mo><mn>3</mn><mi>d</mi><mo>)</mo><mo>&#183;</mo><mo>(</mo><mn>2</mn><mo>-</mo><mn>5</mn><mi>d</mi><mo>+</mo><mn>4</mn><mi>d</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mo>=</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mn>5</mn><mi>d</mi></mrow></mfenced><mo>&#183;</mo><mo>(</mo><mn>2</mn><mo>-</mo><mn>2</mn><mi>d</mi><mo>)</mo><mo>&#183;</mo><mo>(</mo><mn>2</mn><mo>-</mo><mi>d</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"/><math><mo>&#8658;</mo><mo>&#8710;</mo><mo>=</mo><mo>-</mo><mn>2</mn><mo>(</mo><mn>5</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>17</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>16</mn><mi>d</mi><mo>-</mo><mn>4</mn><mo>)</mo></math></p><p>For finding the maximum or minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mo>&#8710;</mo></mrow><mrow><mi>d</mi><mi>d</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn><mo>(</mo><mn>15</mn><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><mn>34</mn><mi>d</mi><mo>+</mo><mn>16</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mo>&#8710;</mo></mrow><mrow><mi>d</mi><mi>d</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn><mfenced separators="|"><mrow><mn>5</mn><mi>d</mi><mo>-</mo><mn>8</mn></mrow></mfenced><mo>(</mo><mn>3</mn><mi>d</mi><mo>-</mo><mn>2</mn><mo>)</mo></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mo>&#8710;</mo></mrow><mrow><mi>d</mi><mi>d</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mfenced separators="|"><mrow><mn>5</mn><mi>d</mi><mo>-</mo><mn>8</mn></mrow></mfenced><mo>(</mo><mn>3</mn><mi>d</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mo>&#8710;</mo></mrow><mrow><mi>d</mi><msup><mi>d</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn><mo>(</mo><mn>30</mn><mi>d</mi><mo>-</mo><mn>34</mn><mo>)</mo></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mo>&#8710;</mo></mrow><mrow><mi>d</mi><msup><mi>d</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mn>30</mn><mo>&#215;</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mo>-</mo><mn>34</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>28</mn><mo>&#60;</mo><mn>0</mn></math> and at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mo>&#8710;</mo></mrow><mrow><mi>d</mi><msup><mi>d</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mn>30</mn><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>-</mo><mn>34</mn></mrow></mfenced><mo>=</mo><mn>28</mn><mo>&#62;</mo><mn>0</mn></math></p><p>We know that if at any point the first derivative of a function is zero and the second derivative is negative, then it is the point of maxima of the function.</p><p>Hence, it is clear that <math><mo>&#8710;</mo></math> is maximum when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q83. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><msub><mi>a</mi><mi>n</mi></msub></math> are in <math><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mo>&#8201;</mo><msub><mi>a</mi><mn>4</mn></msub><mo>+</mo><msub><mi>a</mi><mn>7</mn></msub><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mn>16</mn></msub><mo>=</mo><mn>114</mn></math> , then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>6</mn></msub><mo>+</mo><msub><mi>a</mi><mn>11</mn></msub><mo>+</mo><msub><mi>a</mi><mn>16</mn></msub></math> is equal to :

**Options:**

- **(A)** <math><mn>64</mn></math>
- **(B)** <math><mn>98</mn></math>
- **(C)** <math><mn>38</mn></math>
- **(D)** <math><mn>76</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>76</mn></math>**

**Detailed Solution:**

<p><math><mo>&#8756;</mo></math> We know that sum of equidistant term from end &amp; beginning is same in any <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math><math><mo>&#8658;</mo><mi>&#160;</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>16</mn></mrow></msub><msub><mrow><mo>=</mo><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>15</mn></mrow></msub><mo>=</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>14</mn></mrow></msub><msub><mrow><mo>=</mo><mi>a</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>13</mn></mrow></msub><mo>=</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>12</mn></mrow></msub><mo>=</mo><mo>&#8230;</mo><mo>=</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>7</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>10</mn></mrow></msub></math></p><p><math><mo>&#8757;</mo><mi>&#160;</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>4</mn></mrow></msub><msub><mrow><mo>+</mo><mi>a</mi></mrow><mrow><mn>7</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>10</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>13</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>16</mn></mrow></msub><mo>=</mo><mn>114</mn></math></p><p><math><mo>&#8658;</mo><mn>3</mn><mfenced separators="|"><mrow><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>16</mn></mrow></msub></mrow></mfenced><mo>=</mo><mn>114</mn><mo>&#8658;</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>16</mn></mrow></msub><mo>=</mo><mn>38</mn></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>6</mn></msub><msub><mrow><mo>+</mo><mi>a</mi></mrow><mn>11</mn></msub><mo>+</mo><msub><mi>a</mi><mn>16</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>16</mn></msub></mrow></mfenced><mo>=</mo><mn>76</mn></math></p>

</details>

---

### Q84. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the sum and product of the first three terms in an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1155</mn></math>, respectively, then a value of its <math><msup><mrow><mn>11</mn></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> term is:

**Options:**

- **(A)** <math><mo>-</mo><mn>25</mn></math>
- **(B)** <math><mo>-</mo><mn>35</mn></math>
- **(C)** <math><mn>25</mn></math>
- **(D)** <math><mo>-</mo><mn>36</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>-</mo><mn>25</mn></math>**

**Detailed Solution:**

<p>Let, the first <math><mn>3</mn></math> terms of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> are <math><mi>a</mi><mo>-</mo><mi>d</mi><mo>,</mo><mi>&#160;</mi><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>a</mi><mo>+</mo><mi>d</mi></math></p><p><math><mo>&#8658;</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">m</mi><mo>=</mo><mn>3</mn><mi>a</mi><mo>=</mo><mn>33</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>11</mn></math></p><p>And product <math><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mi>d</mi></mrow></mfenced><mi>&#160;</mi><mi>a</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>=</mo><mn>1155</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>11</mn><mfenced><mrow><msup><mn>11</mn><mn>2</mn></msup><mo>-</mo><msup><mi>d</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>1155</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>121</mn><mo>-</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1155</mn><mn>11</mn></mfrac><mo>=</mo><mn>105</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mn>121</mn><mo>-</mo><mn>105</mn><mo>=</mo><mn>16</mn></math></p><p><math><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mo>&#177;</mo><mn>4</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>11</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mn>4</mn><mo>,</mo></math> the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>,</mo><mi>&#160;</mi><mn>11</mn><mo>,</mo><mi>&#160;</mi><mn>15</mn><mo>,</mo><mo>&#8230;</mo></math></p><p>The <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term of an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo><mo>,</mo></math> with first term <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mi>A</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>11</mn></msub><mo>=</mo><mn>7</mn><mo>+</mo><mn>10</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>47</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>11</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mo>-</mo><mn>4</mn><mo>,</mo></math> the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>,</mo><mi>&#160;</mi><mn>11</mn><mo>,</mo><mi>&#160;</mi><mn>7</mn><mo>,</mo><mo>&#8230;</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>11</mn></msub><mo>=</mo><mn>15</mn><mo>+</mo><mn>10</mn><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>25</mn><mo>.</mo></math></p>

</details>

---

### Q85. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the sum of the first <math><mi>n</mi></math> terms of a non-constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mi>n</mi></msub></math> be <math><mn>50</mn><mi>n</mi><mo>+</mo><mfrac><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>-</mo><mn>7</mn><mo>)</mo></mrow><mrow><mn>2</mn></mrow></mfrac><mi>A</mi><mo>,</mo></math> where <math><mi>A</mi></math> is a constant. If <math><mi>d</mi></math> is the common difference of this <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math>, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>d</mi><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>50</mn></msub></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mn>50</mn><mo>,</mo><mi> </mi><mn>50</mn><mo>+</mo><mn>46</mn><mi>A</mi></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mi>A</mi><mo>,</mo><mi> </mi><mn>50</mn><mo>+</mo><mn>45</mn><mi>A</mi></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>50,</mn><mo>&#160;</mo><mn>50</mn><mo>+</mo><mn>45</mn><mi>A</mi></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mi>A</mi><mo>,</mo><mi> </mi><mn>50</mn><mo>+</mo><mn>46</mn><mi>A</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced separators="|"><mrow><mi>A</mi><mo>,</mo><mi> </mi><mn>50</mn><mo>+</mo><mn>46</mn><mi>A</mi></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mn>50</mn><mi>n</mi><mo>+</mo><mfrac><mrow><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>7</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mi>A</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>50</mn><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>+</mo><mfrac><mrow><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mi>A</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced separators="|"><mn>2</mn></mfenced></math></p><p>Subtracting <math><mo>(</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>-</mo><msub><mi>S</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>50</mn><mi>n</mi><mo>-</mo><mn>50</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>7</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mi>A</mi><mo>-</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mi>n</mi></msub><mo>-</mo><msub><mi>S</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>50</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mi>A</mi><mn>2</mn></mfrac><mfenced><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mi>n</mi></msub><mo>-</mo><msub><mi>S</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>50</mn><mo>+</mo><mfrac><mi>A</mi><mn>2</mn></mfrac><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi>n</mi><mo>-</mo><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><mi>n</mi><mo>-</mo><mn>8</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><msub><mi>S</mi><mi>n</mi></msub><mo>-</mo><msub><mi>S</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>50</mn><mo>+</mo><mi>A</mi><mo>(</mo><mi>n</mi><mo>-</mo><mn>4</mn><mo>)</mo></math></p><p>Hence, <math><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>50</mn><mo>-</mo><mn>3</mn><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub><mo>=</mo><mn>50</mn><mo>-</mo><mn>2</mn><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><msub><mi>T</mi><mn>2</mn></msub><mo>-</mo><msub><mi>T</mi><mn>1</mn></msub><mo>=</mo><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>50</mn></msub><mo>=</mo><mn>50</mn><mo>+</mo><mn>46</mn><mi>A</mi><mo>.</mo></math></p>

</details>

---

### Q86. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all natural numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> such that <math><mn>100</mn><mo>&#60;</mo><mi>n</mi><mo>&#60;</mo><mn>200</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi><mo>.</mo><mi>C</mi><mo>.</mo><mi>F</mi><mo>.</mo></math> <math><mfenced separators="|"><mrow><mn>91</mn><mo>,</mo><mi>n</mi></mrow></mfenced><mo>&#62;</mo><mn>1</mn></math> is

**Options:**

- **(A)** <math><mn>3203</mn></math>
- **(B)** <math><mn>3221</mn></math>
- **(C)** <math><mn>3121</mn></math>
- **(D)** <math><mn>3303</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>3121</mn></math>**

**Detailed Solution:**

<p>Since,<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>H</mi><mo>.</mo><mi>C</mi><mo>.</mo><mi>F</mi><mo>.</mo></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>91</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi></mrow></mfenced><mo>&#62;</mo><mn>1</mn><mo>.</mo></math></p><p>Hence, <math><mi>n</mi></math> should be multiple of <math><mn>7</mn></math> or <math><mn>13</mn></math> or both.</p><p>Hence, when <math><mi>n</mi></math> is multiple of <math><mn>7</mn></math>,</p><p>Number of terms<math><mo>=</mo><mn>14</mn><mo>,</mo></math> <math><msub><mrow><mi>t</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>105</mn><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>196</mn></math></p><p><math><mo>&#8756;</mo><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>14</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>105</mn><mo>+</mo><mn>196</mn></mrow></mfenced><mo>=</mo><mn>7</mn><mo>&#215;</mo><mn>301</mn><mo>=</mo><mn>2107</mn></math></p><p>When <math><mi>n</mi></math> is multiple of <math><mn>13</mn></math>,</p><p>Number of terms <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><msub><mi>t</mi><mn>1</mn></msub><mo>=</mo><mn>104</mn><mo>,</mo><mi>&#160;</mi><mi>l</mi><mo>=</mo><mn>195</mn></math></p><p><math><mo>&#8756;</mo><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mn>299</mn><mo>=</mo><mn>1196</mn></math></p><p>When <math><mi>n</mi></math> is multiple of <math><mn>91</mn></math></p><p><math><mo>&#8756;</mo></math> Number of term <math><mo>=</mo><mn>1</mn><mi>&#160;</mi></math></p><p><math><msub><mrow><mi>S</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>182</mn></math></p><p><math><mo>&#8756;</mo></math> Required sum <math><mo>=</mo><mn>2107</mn><mo>+</mo><mn>1196</mn><mo>-</mo><mn>182</mn><mo>=</mo><mn>3121</mn></math></p>

</details>

---

### Q87. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>k</mi></msub><mo>=</mo><mfrac><mrow><mn>1</mn><mi>&#160;</mi><mo>+</mo><mi>&#160;</mi><mn>2</mn><mi>&#160;</mi><mo>+</mo><mi>&#160;</mi><mn>3</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>k</mi></mrow><mi>k</mi></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>S</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>S</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msubsup><mi>S</mi><mn>10</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mi>A</mi></math>, then <math><mi>A</mi></math> is equal to :

**Options:**

- **(A)** <math><mn>301</mn></math>
- **(B)** <math><mn>303</mn></math>
- **(C)** <math><mn>156</mn></math>
- **(D)** <math><mn>283</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>303</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>k</mi></msub><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>k</mi></mrow><mi>k</mi></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mi>k</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msubsup><mi>S</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>S</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msubsup><mi>S</mi><mn>10</mn><mn>2</mn></msubsup><mo>=</mo><msup><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced separators="|"><mfrac><mrow><mn>2</mn><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mfenced separators="|"><mfrac><mrow><mn>10</mn><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></math>  (using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced separators="|"><mfrac><mn>2</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced separators="|"><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mfenced separators="|"><mfrac><mn>11</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>2</mn></msup></mfrac><mfenced close="]" open="[" separators="|"><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mn>11</mn><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfenced><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mn>11</mn><mn>2</mn></msup></mrow></mfenced><mo>-</mo><msup><mn>1</mn><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>11</mn><mo>&#215;</mo><mn>12</mn><mo>&#215;</mo><mn>23</mn></mrow><mn>6</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced></math> (using the identity <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mrow><mo>&#8721;</mo><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>=</mo><mi>n</mi></mrow></munderover><mo>=</mo><mfrac><mrow><mfenced><mi>n</mi></mfenced><mstyle displaystyle="true"><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mstyle><mstyle displaystyle="true"><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mstyle></mrow><mn>6</mn></mfrac></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#215;</mo><mn>505</mn></math></p><p>Comparing with the given condition in question, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>12</mn></mfrac><mi>A</mi><mo>=</mo><mfrac><mn>505</mn><mn>4</mn></mfrac></math></p><p><math><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mrow><mn>505</mn><mo>&#215;</mo><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mn>303</mn></math>.</p>

</details>

---

### Q88. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If 19 th term of a non-zero A.P. is zero, then its (49th term):

(29th term) is:

**Options:**

- **(A)** 4: 1
- **(B)** 1: 3
- **(C)** 3: 1
- **(D)** 2: 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3: 1**

**Detailed Solution:**

Let first term and common difference of $A P$ be a and d respectively, then

$t_{n}=a+(n-1) d$

$\therefore \quad t_{19}=a+18 d=0$

$\therefore \quad a=-18 d$

$\therefore \quad \frac{t_{49}}{t_{29}}=\frac{a+48 d}{a+28 d}$

$=\frac{-18 d+48 d}{-18 d+28 d}=\frac{30 d}{10 d}=3$

$t_{49}: t_{29}=3: 1$

</details>

---

### Q89. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all two digit positive numbers which when divided by <math><mn>7</mn></math> yield <math><mn>2</mn></math> or <math><mn>5</mn></math> as remainder is

**Options:**

- **(A)** <math><mn>1356</mn></math>
- **(B)** <math><mn>1365</mn></math>
- **(C)** <math><mn>1256</mn></math>
- **(D)** <math><mn>1465</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>1356</mn></math>**

**Detailed Solution:**

<p>Two-digit numbers of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>,</mo><mi>&#160;</mi><mn>23</mn><mo>,</mo><mo>&#160;</mo><mn>30</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><mn>93</mn></math></p><p>These number are forming an arithmetic progression with first term <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>16</mn><mo>,</mo></math> common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mn>23</mn><mo>-</mo><mn>16</mn><mo>=</mo><mn>7</mn></math> and last term <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>93</mn></math></p><p>And, we know that the last term of an arithmetic progression is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>93</mn><mo>=</mo><mn>16</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>77</mn><mo>=</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>12</mn></math>

Two-digit numbers of the form <math><mn>7</mn><mi>&#955;</mi><mo>+</mo><mn>5</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>,</mo><mi>&#160;</mi><mn>19</mn><mo>,</mo><mo>&#160;</mo><mn>26</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><mn>96</mn></math></p><p>Again, using the last term of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo><mo>,</mo></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>96</mn><mo>=</mo><mn>12</mn><mo>+</mo><mfenced><mrow><msub><mi>n</mi><mn>1</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>84</mn><mo>=</mo><mfenced><mrow><msub><mi>n</mi><mn>1</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>13</mn></math></p><p>Now, the sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> terms of an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced><mrow><mi>a</mi><mo>+</mo><mi>l</mi></mrow></mfenced><mo>,</mo></math> we get the sum of all the above numbers as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>12</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><mn>16</mn><mo>+</mo><mn>93</mn></mrow></mfenced><mo>+</mo><mfrac><mn>13</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><mn>12</mn><mo>+</mo><mn>96</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>654</mn><mo>+</mo><mn>702</mn><mo>=</mo><mn>1356</mn><mo>.</mo></math></p>

</details>

---

### Q90. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><mo>&#8230;</mo><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>30</mn></mrow></msub></math> be an A.P., <math><mi>S</mi><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>30</mn></mrow></munderover><mrow><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub></mrow></mrow></math> and <math><mi>T</mi><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>15</mn></mrow></munderover><mrow><msub><mrow><mi>a</mi></mrow><mrow><mo>(</mo><mn>2</mn><mi>i</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow></msub><mo>.</mo></mrow></mrow></math> If <math><msub><mrow><mi>a</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>=</mo><mn>27</mn></math> and <math><mi>S</mi><mo>-</mo><mn>2</mn><mi>T</mi><mo>=</mo><mn>75</mn><mo>,</mo></math> then <math><msub><mrow><mi>a</mi></mrow><mrow><mn>10</mn></mrow></msub></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>47</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>42</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>57</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn></math>**

**Detailed Solution:**

Let common difference <math><mo>=</mo><mi>d</mi></math>

<math><mo>&#8756;</mo><mi>S</mi><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>30</mn></mrow></munderover><mrow><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub></mrow></mrow><mo>=</mo><mfrac><mrow><mn>30</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>2</mn><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>29</mn><mi>&#160;</mi><mi>d</mi></mrow></mfenced></math>

<math><mo>&#8756;</mo><mi>S</mi><mo>=</mo><mn>15</mn><mi>&#160;</mi><mfenced separators="|"><mrow><mn>2</mn><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>29</mn><mi>&#160;</mi><mi>d</mi></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mo>(</mo><mi>i</mi><mo>)</mo></math>

<math><mi>T</mi><mo>=</mo><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>2</mn><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>14</mn><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mn>2</mn><mi>d</mi></mrow></mfenced></math>

<math><mi>T</mi><mo>=</mo><mn>15</mn><mi>&#160;</mi><mfenced separators="|"><mrow><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>14</mn><mi>d</mi></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo></math>

<math><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>4</mn><mi>d</mi><mo>=</mo><mn>27</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mo>(</mo><mi>i</mi><mi>i</mi><mi>i</mi><mo>)</mo></math>

<math><mi>S</mi><mo>-</mo><mn>2</mn><mi>T</mi><mo>=</mo><mn>75</mn></math>

<math><mo>&#8658;</mo><mn>15</mn><mfenced separators="|"><mrow><mn>2</mn><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>29</mn><mi>&#160;</mi><mi>d</mi></mrow></mfenced><mo>-</mo><mn>30</mn><mi>&#160;</mi><mfenced separators="|"><mrow><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>14</mn><mi>d</mi><mi>&#160;</mi></mrow></mfenced><mo>=</mo><mn>75</mn></math>
<math><mo>&#8658;</mo><mn>15</mn><mi>&#160;</mi><mi>d</mi><mfenced separators="|"><mrow><mn>29</mn><mo>-</mo><mn>28</mn></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mn>75</mn></math>
<math><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mn>5</mn></math>
<math><mo>&#8756;</mo><mi>&#160;</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>i</mi><mi>i</mi><mi>i</mi><mo>)</mo></math> <math><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>7</mn></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>10</mn></mrow></msub><mo>=</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>9</mn><mi>d</mi><mo>=</mo><mn>7</mn><mo>+</mo><mn>45</mn><mo>=</mo><mn>52</mn></math>

</details>

---

### Q91. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mi>n</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msub><mi>h</mi><mn>1</mn></msub></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><msub><mi>h</mi><mn>2</mn></msub></mfrac><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><msub><mi>h</mi><mi>n</mi></msub></mfrac></math> are two A.P.s such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><msub><mi>h</mi><mn>2</mn></msub><mo>=</mo><mn>8</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>x</mi><mn>8</mn></msub><mo>=</mo><msub><mi>h</mi><mn>7</mn></msub><mo>=</mo><mn>20</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>5</mn></msub><mo>&#183;</mo><msub><mi>h</mi><mn>10</mn></msub></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3200</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1600</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2650</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2560</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2560</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub></math> be the common difference of the A.P. <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>8</mn></msub><mo>-</mo><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mn>5</mn><msub><mrow><mo>&#160;</mo><mi>d</mi></mrow><mn>1</mn></msub><mo>=</mo><mn>12</mn><mo>&#8658;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>5</mn></msub><mo>=</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><mn>2</mn><msub><mrow><mo>&#160;</mo><mi>d</mi></mrow><mn>1</mn></msub><mo>=</mo><mn>8</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>12</mn><mn>5</mn></mfrac><mo>=</mo><mn>12</mn><mo>.</mo><mn>8</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>2</mn></msub></math> be the common difference of the other sequence then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mrow><mo>&#160;</mo><mi>d</mi></mrow><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>20</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>40</mn></mfrac><mo>&#8658;</mo><msub><mi>d</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><msub><mrow><mo>&#160;</mo><mi>h</mi></mrow><mn>10</mn></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><msub><mrow><mo>&#160;</mo><mi>h</mi></mrow><mn>7</mn></msub></mfrac><mo>+</mo><mn>3</mn><msub><mrow><mo>&#160;</mo><mi>d</mi></mrow><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>200</mn></mfrac><mo>&#8658;</mo><msub><mi>h</mi><mn>10</mn></msub><mo>=</mo><mn>200</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>5</mn></msub><mo>&#183;</mo><msub><mi>h</mi><mn>10</mn></msub><mo>=</mo><mn>12</mn><mo>.</mo><mn>8</mn><mo>&#215;</mo><mn>200</mn><mo>=</mo><mn>2560</mn></math></p>

</details>

---

### Q92. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `1`

If $x_1, x_2, \ldots ., x_n$ and $\frac{1}{h_1}, \frac{1}{h^2}, \ldots . . \frac{1}{h_n}$ are two A.P's such that $x_3=h_2=8$ and $x_8=h_7=20$, then $x_5 . h_{10}$ equals.

**Options:**

- **(A)** 2560
- **(B)** 2650
- **(C)** 3200
- **(D)** 1600

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2560**

**Detailed Solution:**

Suppose $d_1$ is the common difference of the A.P.
$x_1, x_2, \ldots . x_n$ then
$$
\begin{aligned}
&\because x_8-x_3=5 d_1=12 \Rightarrow d_1=\frac{12}{5}=2.4 \\
&\Rightarrow x_5=x_3+2 d_1=8+2 \times \frac{12}{5}=12.8
\end{aligned}
$$
Suppose $d_2$ is the common difference of the
A.P $\frac{1}{h_1}, \frac{1}{h_2}, \ldots . \cdot \frac{1}{h_n}$ then
$$
\begin{aligned}
&5 d_2=\frac{1}{20}-\frac{1}{8}=\frac{-3}{40} \Rightarrow d_2=\frac{-3}{200} \\
&\because \frac{1}{h_{10}}=\frac{1}{h_7}+3 d_2=\frac{1}{200} \Rightarrow h_{10}=200 \\
&\Rightarrow x_5 . h_{10}=12.8 \times 200=2560
\end{aligned}
$$

</details>

---

### Q93. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mo>&#8230;</mo><msub><mrow><mi>a</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>,</mo><mo>&#8230;</mo></math> ,be in A.P. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><msub><mi>a</mi><mn>7</mn></msub><mo>+</mo><msub><mi>a</mi><mn>11</mn></msub><mo>+</mo><msub><mi>a</mi><mn>15</mn></msub><mo>=</mo><mn>72</mn></math>, then the sum of its first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math> terms is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>306</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>204</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>153</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>612</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>306</mn></math>**

**Detailed Solution:**

<math><msub><mrow><mi>a</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>7</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>11</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>15</mn></mrow></msub><mo>=</mo><mn>72</mn></math>

<math><mfenced separators="|"><mrow><msub><mrow><mi>a</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>15</mn></mrow></msub></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><msub><mrow><mi>a</mi></mrow><mrow><mn>7</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>11</mn></mrow></msub></mrow></mfenced><mo>=</mo><mn>72</mn></math>

<math><msub><mrow><mi>a</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>15</mn></mrow></msub><mo>=</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>7</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>11</mn></mrow></msub><mo>=</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>17</mn></mrow></msub></math>

<math><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>17</mn></mrow></msub><mo>=</mo><mn>36</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>17</mn></msub><mo>=</mo><mfrac><mn>17</mn><mn>2</mn></mfrac><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>17</mn></msub></mrow></mfenced><mo>=</mo><mn>17</mn><mo>&#215;</mo><mn>18</mn><mo>=</mo><mn>306</mn></math>

</details>

---

### Q94. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let the sum of the first three terms of an A.P. be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>39</mn></math> and the sum of its last four terms be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>178</mn></math>. If the first term of this A.P. is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>,</mo></math> then the median of the A.P. is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn><mo>.</mo><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>29</mn><mo>.</mo><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>29</mn><mo>.</mo><mn>5</mn></math>**

**Detailed Solution:**

Let the A.P. be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>+</mo><mi>d</mi><mo>,</mo><mi>a</mi><mo>+</mo><mn>2</mn><mi>d</mi><mo>&#8943;</mo><mo>&#8943;</mo><mo>,</mo><mi>l</mi><mo>-</mo><mn>3</mn><mi>d</mi><mo>,</mo><mi>&#160;</mi><mi>l</mi><mo>-</mo><mn>2</mn><mi>d</mi><mo>,</mo><mi>&#160;</mi><mi>l</mi><mo>-</mo><mi>d</mi><mo>,</mo><mi>l</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math>
Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is the first term and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is the last term,
Sum of <math><msup><mrow><mn>1</mn></mrow><mrow><mi>s</mi><mi>t</mi></mrow></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>terms is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>39</mn></math>.
<math><mn>30</mn><mo>+</mo><mn>3</mn><mi>d</mi><mo>=</mo><mn>39</mn></math> as <math><mi>a</mi><mo>=</mo><mn>10</mn></math> (Given)
<math><mi>d</mi><mo>=</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mn>3</mn></math>
Sum of last <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> terms is<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>178</mn></math>.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>l</mi><mo>-</mo><mn>6</mn><mi>d</mi><mo>=</mo><mn>178</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>49</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>13</mn><mo>,</mo><mo>&#160;</mo><mn>16</mn><mo>,</mo><mo>&#160;</mo><mn>19</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>46</mn><mo>,</mo><mo>&#160;</mo><mn>49</mn></math>
Let number of terms are, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math>term is<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mo>(</mo><mi>n</mi><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>49</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>14</mn></math>
So the median of the series would be mean of <math><msup><mrow><mn>7</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup><mi>&#160;</mi><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><msup><mrow><mn>8</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term
<math><mfrac><mrow><mn>10</mn><mo>+</mo><mn>6</mn><mo>&#8901;</mo><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced><mo>+</mo><mn>10</mn><mo>+</mo><mn>7</mn><mo>&#8901;</mo><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>59</mn><mn>2</mn></mfrac><mi>&#160;</mi><mo>=</mo><mn>29.5</mn></math>

<strong>Alternate way</strong>
The median would be mean of 10 and 49, That is 29.5.

</details>

---

### Q95. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The number of terms in an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> is even, the sum of the odd terms in it is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math> and that the even terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>.</mo></math> If the last term exceeds the first term by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo></math> then the number of terms in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<p>We know that the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term and sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>terms of an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> with first term <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> are respectively <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced><mo>.</mo></math></p><p>Let, the number of terms in the given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi></math> then there are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mi>n</mi></math> even terms and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> odd terms.</p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub><mo>=</mo><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mn>2</mn><mi>n</mi></mrow></msub><mo>=</mo><mi>a</mi><mo>+</mo><mo>(</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>d</mi></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mn>2</mn><mi>n</mi></mrow></msub><mo>-</mo><msub><mi>T</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>21</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mo>=</mo><mfrac><mn>21</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>n</mi><mi>d</mi><mo>-</mo><mi>d</mi><mo>=</mo><mfrac><mn>21</mn><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Also, the sum of odd terms i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn><mi>d</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>4</mn><mi>d</mi></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn><mi>d</mi><mo>=</mo><mfrac><mn>48</mn><mi>n</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>And, the sum of even terms i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>+</mo><mi>d</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>3</mn><mi>d</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>5</mn><mi>d</mi></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mi>d</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#8658;</mtext><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn><mi>d</mi><mo>+</mo><mn>2</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>30</mn></math></p><p>Put the value from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mn>48</mn><mi>n</mi></mfrac><mo>+</mo><mn>2</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>24</mn><mo>+</mo><mi>d</mi><mi>n</mi><mo>=30</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mi>d</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Put this value in the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo></math> to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>6</mn><mo>-</mo><mi>d</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mn>4</mn><mo>-</mo><mn>2</mn><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p>Now, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> in the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced><mo>,</mo></math> to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>&#215;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>n</mi><mo>=</mo><mn>8</mn></math></p><p>Thus, the number of terms in the given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo></math></p>

</details>

---

### Q96. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the first 20 terms common between the series $3+7+11+15+$ and $1+6+11+$ $16+\ldots .$. is

**Options:**

- **(A)** 4000
- **(B)** 4020
- **(C)** 4200
- **(D)** 4220

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 4020**

**Detailed Solution:**

Given $\mathrm{n}=20 ; \mathrm{S}_{20}=$ ?
Series (1) $\rightarrow 3,7, \underline{11}, 15,19,23,27, \underline{31}, 35$, $39,43,47$,
$\underline{51}, 55,59 \ldots$
Series (2) $\rightarrow 1,6, \underline{11}, 16,21,26, \underline{31}, 36,41$, $46, \underline{51}, 56$, $61,66,71$.
The common terms between both the series are $11,31,51,71 \ldots$
Above series forms an Arithmetic progression (A.P).
Therefore, first term (a) $=11$ and common difference $(\mathrm{d})=20$
Now, $\mathrm{S}_{\mathrm{n}}=\frac{n}{2}[2 a+(n-1) d]$
$$
\begin{aligned}
&\mathrm{S}_{20}=\frac{20}{2}[2 \times 11+(20-1) 20] \\
&\mathrm{S}_{20}=10[22+19 \times 20] \\
&\mathrm{S}_{20}=10 \times 402=4020 \\
&\therefore \mathrm{S}_{20}=4020
\end{aligned}
$$

</details>

---

### Q97. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Given an A.P. whose terms are all positive integers. The sum of its first nine terms is greater than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn></math> and less than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>220</mn><mo>.</mo></math>  If the second term in it is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>, then its <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>4</mn><mi>th</mi></msup></math> term is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>**

**Detailed Solution:**

<p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn><mo>&#60;</mo><msub><mi>S</mi><mn>9</mn></msub><mo>&#60;</mo><mn>220</mn></math></p><p>As we know sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> terms of A.P whose first term is  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;&#160;200&#60;</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>8</mn><mi>d</mi></mrow></mfenced><mo>&#60;</mo><mn>220</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><mfrac><mrow><mn>2</mn><mn>0</mn><mn>0</mn></mrow><mn>9</mn></mfrac><mo>&#60;</mo><mi>a</mi><mo>+</mo><mn>4</mn><mi>d</mi><mo>&#60;</mo><mfrac><mrow><mn>2</mn><mn>2</mn><mn>0</mn></mrow><mn>9</mn></mfrac></math></p><p>As we know <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term of A.P is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></math>

Also   <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub><mo>=</mo><mi>a</mi><mo>+</mo><mi>d</mi><mo>=</mo><mn>1</mn><mn>2</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><mn>4</mn><mi>d</mi><mo>=</mo><mn>48</mn><mo>-</mo><mn>4</mn><mi>a</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;&#160;&#160;</mo><mfrac><mrow><mn>2</mn><mn>0</mn><mn>0</mn></mrow><mn>9</mn></mfrac><mo>&#60;</mo><mi>a</mi><mo>+</mo><mn>48</mn><mo>-</mo><mn>4</mn><mi>a</mi><mo>&#60;</mo><mfrac><mrow><mn>2</mn><mn>2</mn><mn>0</mn></mrow><mn>9</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><mfrac><mrow><mn>2</mn><mn>0</mn><mn>0</mn></mrow><mn>9</mn></mfrac><mo>-</mo><mn>4</mn><mn>8</mn><mo>&#60;</mo><mo>-</mo><mn>3</mn><mi>a</mi><mo>&#60;</mo><mfrac><mrow><mn>2</mn><mn>2</mn><mn>0</mn></mrow><mn>9</mn></mfrac><mo>-</mo><mn>4</mn><mn>8</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mn>3</mn><mn>2</mn></mrow><mn>9</mn></mfrac><mo>&#60;</mo><mo>-</mo><mn>3</mn><mi>a</mi><mo>&#60;</mo><mo>-</mo><msub><mfrac><mrow><mn>2</mn><mn>1</mn><mn>2</mn></mrow><mn>9</mn></mfrac><msub><maction actiontype="argument"><mrow/></maction><mrow/></msub></msub></math>

OR   <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mn>1</mn><mn>2</mn></mrow><mrow><mn>2</mn><mn>7</mn></mrow></mfrac><mo>&#60;</mo><mi>a</mi><mo>&#60;</mo><mfrac><mrow><mn>2</mn><mn>3</mn><mn>2</mn></mrow><mrow><mn>2</mn><mn>7</mn></mrow></mfrac></math>

i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mfrac><mrow><mn>2</mn><mn>3</mn></mrow><mrow><mn>2</mn><mn>7</mn></mrow></mfrac><mo>&#60;</mo><mi>a</mi><mo>&#60;</mo><mn>8</mn><mfrac><mrow><mn>1</mn><mn>6</mn></mrow><mrow><mn>2</mn><mn>7</mn></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><mi>a</mi><mo>=</mo><mn>8</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><mi>d</mi><mo>=</mo><mn>4</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>4</mn></msub><mo>=</mo><mi>a</mi><mo>+</mo><mn>3</mn><mi>d</mi><mo>=</mo><mn>8</mn><mo>+</mo><mn>1</mn><mn>2</mn><mo>=</mo><mn>2</mn><mn>0</mn></math></p>

</details>

---

### Q98. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If $a_1, a_2, a_3, \ldots, a_n, \ldots$. are in A.P. such that $a_4-a_7$ $+a_{10}=m$, then the sum of first 13 terms of this A.P., is :

**Options:**

- **(A)** $10 \mathrm{~m}$
- **(B)** $12 \mathrm{~m}$
- **(C)** $13 \mathrm{~m}$
- **(D)** $15 \mathrm{~m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $13 \mathrm{~m}$**

**Detailed Solution:**

If $d$ be the common difference, then
$$
\begin{aligned}
m & =a_4-a_7+a_{10}=a_4-a_7+a_7+3 \mathrm{~d}=a_7 \\
\mathrm{~S}_{13} & =\frac{13}{2}\left[a_1+a_{13}\right]=\frac{13}{2}\left[a_1+a_7+6 d\right] \\
& =\frac{13}{2}\left[2 a_7\right]=13 a_7=13 \mathrm{~m}
\end{aligned}
$$

</details>

---

### Q99. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Given sum of the first $n$ terms of an A.P. is $2 n+$ $3 n^2$. Another A.P. is formed with the same first term and double of the common difference, the sum of $n$ terms of the new A.P. is :

**Options:**

- **(A)** $n+4 n^2$
- **(B)** $6 n^2-n$
- **(C)** $n^2+4 n$
- **(D)** $3 n+2 n^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6 n^2-n$**

**Detailed Solution:**

Given $\mathrm{S}_n=2 n+3 n^2$
Now, first term $=2+3=5$
second term $=2(2)+3(4)=16$
third term $=2(3)+3(9)=33$
Now, sum given in option (b) only has the same first term and difference between 2 nd and 1 st term is double also.

</details>

---

### Q100. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $a_1, a_2, a_3, \ldots$ be an A.P, such that $\frac{a_1+a_2+\ldots+a_p}{a_1+a_2+a_3+\ldots+a_q}=\frac{p^3}{q^3} ; p \neq q$. Then $\frac{a_6}{a_{21}}$ is equal to:

**Options:**

- **(A)** $\frac{41}{11}$
- **(B)** $\frac{31}{121}$
- **(C)** $\frac{11}{41}$
- **(D)** $\frac{121}{1861}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{31}{121}$**

**Detailed Solution:**

$\begin{aligned} & \frac{a_1+a_2+a_3+\ldots \ldots+a_p}{a_1+a_2+a_3+\ldots \ldots+a_q}=\frac{p^3}{q^3} \\ \Rightarrow & \frac{a_1+a_2}{a_1}=\frac{8}{1} \Rightarrow a_1+\left(a_1+d\right)=8 a_1 \\ \Rightarrow \quad & d=6 a_1 \\ & \text { Now } \frac{a_6}{a_{21}}=\frac{a_1+5 d}{a_1+20 d} \\ = & \frac{a_1+5 \times 6 a_1}{a_1+20 \times 6 a_1}=\frac{1+30}{1+120}=\frac{31}{121}\end{aligned}$

</details>

---

### Q101. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi></math> are positive numbers in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>z</mi></math> are also in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math>, then which of the following is correct.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>x</mi><mo>=</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>2</mn><mi>z</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>x</mi><mo>=</mo><mn>4</mn><mi>y</mi><mo>=</mo><mn>3</mn><mi>z</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>=</mo><mi>z</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>=</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>6</mn><mi>z</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>=</mo><mi>z</mi></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>,</mo><mo>&#160;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>z</mi></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>z</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>y</mi><mo>&#8722;</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>&#8722;</mo><mi>y</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>y</mi><mi>z</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math></p><p>i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>z</mi><mo>&#8658;</mo><mi>y</mi><mo>&#8722;</mo><mi>x</mi><mo>=</mo><mi>z</mi><mo>&#8722;</mo><mi>y</mi></math></p><p>Hence, from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>x</mi><mi>y</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi>y</mi><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mo>=</mo><mi>y</mi><mi>z</mi></math> either <math> <mrow> <mi>y</mi><mo>=</mo><mn>0</mn></mrow> </math> (rejected) or <math> <mrow> <mi>x</mi><mo>=</mo><mi>z</mi></mrow> </math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>y</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>z</mi></math>.</p>

</details>

---

### Q102. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `1`

If the A.M. between $p^{\text {th }}$ and $q^{\text {th }}$ terms of an A.P. is equal to the A.M. between $r^{\text {th }}$ and $s^{\text {th }}$ terms of the same A.P., then $p+q$ is equal to

**Options:**

- **(A)** $r+s-1$
- **(B)** $r+s-2$
- **(C)** $r+s+1$
- **(D)** $r+s$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $r+s$**

**Detailed Solution:**

Given: $\frac{a_p+a_q}{2}=\frac{a_r+a_s}{2}$
$$
\begin{aligned}
& \Rightarrow a+(p-1) d+a+(q-1) d \\
& \quad=a+(r-1) d+a+(s-1) d \\
& \Rightarrow 2 a+(p+q) d-2 d=2 a+(r+s) d-2 d \\
& \Rightarrow(p+q) d=(r+s) d \Rightarrow p+q=r+s .
\end{aligned}
$$

</details>

---

### Q103. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `1`

If $100$ times the $100^{\text {th }}$ term of an $AP$ with non zero common difference equals the $50$ times its $50^{\text {th }}$ term, then the $150^{\text {th }}$ term of this $A P$ is

**Options:**

- **(A)** $-150$
- **(B)** $150$ times its $50^{\text {th }}$ term
- **(C)** $150$
- **(D)** zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) zero**

**Detailed Solution:**

$100\left(T_{100}\right)=50\left(T_{50}\right) \quad \Rightarrow 2[a+99 d]=a+49 d \Rightarrow a+149 d=0 \quad \Rightarrow T_{150}=0$

</details>

---

### Q104. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `1`

A man saves Rs. 200 in each of the first three months of his service. In each of the subsequent months his saving increases by Rs. 40 more than the saving of immediately previous month. His total saving from the start of service will be Rs. 11040 after

**Options:**

- **(A)** 19 months
- **(B)** 20 months
- **(C)** 21 months
- **(D)** 18 months

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 21 months**

**Detailed Solution:**

$\begin{array}{ccccccc}1 & 2 & 3 & 4 & 5 & 6 & \ldots \ldots . \\ 200 & 200 & 200 & 240 & 280 & \ldots \ldots . & \ldots \ldots \ldots\end{array}$
Sum $=11040$
$120+80+160+40+200+240+\ldots=11040$
$\frac{n}{2}[2 a+(n-1) d]+80+40=11040$
$\frac{n}{2}[240+(n-1) 40]=10920$
$n[6+n-1]=546$
$n(n+5)=546$
$n=21$

</details>

---

### Q105. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `2`

A person is to count 4500 currency notes. Let $a_n$ denote the number of notes he counts in the $\mathrm{n}^{\text {th }}$ minute. If $\mathrm{a}_1=\mathrm{a}_2=\ldots \ldots=\mathrm{a}_{10}=150$ and $\mathrm{a}_{10}, \mathrm{a}_{11}, \ldots \ldots$ are in A.P. with common difference $-2$, then the time taken by him to count all notes is

**Options:**

- **(A)** 34 minutes
- **(B)** 125 minutes
- **(C)** 135 minutes
- **(D)** 24 minutes

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 34 minutes**

**Detailed Solution:**

Till $10^{\text {th }}$ minute number of counted notes $=1500$
$$
3000=\frac{n}{2}[2 \times 148+(n-1)(-2)]=n[148-n+1]
$$
$$
\begin{aligned}
& n^2-149 n+3000=0 \\
& n=125,24 \\
& n=125 \text { is not possible. }
\end{aligned}
$$
Total time $=24+10=34$ minutes.

</details>

---

### Q106. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

Let $a_1, a_2, a_3, \ldots$ be terms of an A.P. If $\frac{a_1+a_2+\cdots a_p}{a_1+a_2+\cdots+a_q}=\frac{p^2}{q^2}, p \neq q$, then $\frac{a_6}{a_{21}}$ equals

**Options:**

- **(A)** $\frac{41}{11}$
- **(B)** $\frac{7}{2}$
- **(C)** $\frac{2}{7}$
- **(D)** $\frac{11}{41}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{11}{41}$**

**Detailed Solution:**

$$
\begin{aligned}
& \frac{\frac{p}{2}\left[2 a_1+(p-1) d\right]}{\frac{q}{2}\left[2 a_1+(q-1) d\right]}=\frac{p^2}{q^2} \Rightarrow \frac{2 a_1+(p-1) d}{2 a_1+(q-1) d}=\frac{p}{q} \\
& \frac{a_1+\left(\frac{p-1}{2}\right) d}{a_1+\left(\frac{q-1}{2}\right) d}=\frac{p}{q}
\end{aligned}
$$
For $\frac{a_6}{a_{21}}, p=11, q=41 \rightarrow \frac{a_6}{a_{21}}=\frac{11}{41}$

</details>

---

### Q107. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

Let $T_r$ be the rth term of an A.P. whose first term is a and common difference is $d$. If for some positive integers $m, n, m \neq n, T_m=\frac{1}{n}$ and $T_n=\frac{1}{m}$, then $a-d$ equals

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $\frac{1}{\mathrm{mn}}$
- **(D)** $\frac{1}{m}+\frac{1}{n}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

$$
T_m=\frac{1}{n}=a+(m-1) d
$$
and $T_n=\frac{1}{m}=a+(n-1) d$
from (1) and (2) we get $a=\frac{1}{m n}, \quad d=\frac{1}{m n}$ Hence $\mathrm{a}-\mathrm{d}=0$

</details>

---

### Q108. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)$ be a polynomial function of second degree. If $f(1)=f(-1)$ and $a, b, c$ are in A.P, then $f^{\prime}(a), f^{\prime}(c)$ are in

**Options:**

- **(A)** Arithmetic-Geometric Progression
- **(B)** A.P.
- **(C)** G.P.
- **(D)** H.P.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) A.P.**

**Detailed Solution:**

$f(x)=a x^2+b x+c$
$f(1)=f(-1) \Rightarrow a+b+c=a-b+c$ or $b=0$
$\therefore f(x)=a x^2+c$ or $f^{\prime}(x)=2 a x$
Now $f^{\prime}(a) ; f^{\prime}(b) ;$ and $f^{\prime}(c)$ are $2 a(a) ; 2 a(b) ; 2 a(c)$. If $a, b, c$ are in A.P. then $f^{\prime}(a) ; f^{\prime}(b)$ and $f^{\prime}(c)$ are also in A.P.

</details>

---

### Q109. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

The sum of integers from 1 to 100 that are divisible by 2 or 5 is

**Options:**

- **(A)** 3000
- **(B)** 3050
- **(C)** 3600
- **(D)** 3250

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3050**

**Detailed Solution:**

Required sum $=(2+4+6+\ldots \ldots+100)+(5+10+15+\ldots \ldots+100)-(10+20+\ldots . .+100)$
$=2550+1050-530=3050$

</details>

---

### Q110. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

If $1, \log _9\left(3^{1-x}+2\right), \log _3\left(4.3^x-1\right)$ are in A.P. then $x$ equals

**Options:**

- **(A)** $\log _3 4$
- **(B)** 1 + $\log _3 4$
- **(C)** 1 - $\log _3 4$
- **(D)** $\log _4 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1 - $\log _3 4$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/UtPPNrf-ySVyySeVekP8Iwo86TYuwmF0CkTQ-oHHvyU.original.fullsize.png">

</details>

---

