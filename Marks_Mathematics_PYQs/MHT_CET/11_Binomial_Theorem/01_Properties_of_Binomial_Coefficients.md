# MHT CET Mathematics - Binomial Theorem

## Topic 1: Properties of Binomial Coefficients

**Total Questions:** 6

---

### Q1. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If ${}^{n}C_4, {}^{n}C_5$ and ${}^{n}C_6$ are in arithmetic progression (A.P.), then the value of n is...

**Options:**

- **(A)** $5$ or $11$
- **(B)** $7$ or $14$
- **(C)** $8$ or $15$
- **(D)** $6$ or $13$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $7$ or $14$**

**Detailed Solution:**

Given that $^{n}C_4, ^{n}C_5, ^{n}C_6$ are in A.P.

$2 \times ^{n}C_5 = ^{n}C_4 + ^{n}C_6$

$2 \times \dfrac{n!}{5!(n-5)!} = \dfrac{n!}{4!(n-4)!} + \dfrac{n!}{6!(n-6)!}$

Multiplying the entire equation by $\dfrac{6!(n-4)!}{n!}$:

$2 \times 6 \times (n-4) = 6 \times 5 + (n-4)(n-5)$

$12n - 48 = 30 + n^2 - 9n + 20$

$n^2 - 21n + 98 = 0$

$(n-7)(n-14) = 0$

$n = 7$ or $n = 14$

Answer: $7$ or $14$

</details>

---

### Q2. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of ${ }^{47} C_4+\sum_{j=1}^5{ }^{(52-j)} C_3$ is

**Options:**

- **(A)** ${ }^{52} \mathrm{C}_4$
- **(B)** ${ }^{52} \mathrm{C}_2$
- **(C)** ${ }^{48} \mathrm{C}_4$
- **(D)** ${ }^{48} \mathrm{C}_2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) ${ }^{52} \mathrm{C}_4$**

**Detailed Solution:**

The given expression is $^{47}C_{4} + \sum_{j=1}^{5} {}^{52-j}C_{3}$.

Expanding the summation, we get:

$^{47}C_{4} + ^{51}C_{3} + ^{50}C_{3} + ^{49}C_{3} + ^{48}C_{3} + ^{47}C_{3}$

Rearranging the terms:

$(^{47}C_{4} + ^{47}C_{3}) + ^{48}C_{3} + ^{49}C_{3} + ^{50}C_{3} + ^{51}C_{3}$

Using the identity $^{n}C_{r} + ^{n}C_{r-1} = ^{n+1}C_{r}$:

$^{47}C_{4} + ^{47}C_{3} = ^{48}C_{4}$

Substituting this back:

$^{48}C_{4} + ^{48}C_{3} + ^{49}C_{3} + ^{50}C_{3} + ^{51}C_{3}$

Applying the identity repeatedly:

$^{48}C_{4} + ^{48}C_{3} = ^{49}C_{4}$

$^{49}C_{4} + ^{49}C_{3} = ^{50}C_{4}$

$^{50}C_{4} + ^{50}C_{3} = ^{51}C_{4}$

$^{51}C_{4} + ^{51}C_{3} = ^{52}C_{4}$

Answer: ${ }^{52} \mathrm{C}_4$

</details>

---

### Q3. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If ${ }^{15} \mathrm{C}_4+{ }^{15} \mathrm{C}_5+{ }^{16} \mathrm{C}_6+{ }^{17} \mathrm{C}_7+{ }^{18} \mathrm{C}_8={ }^{19} \mathrm{C}_{\mathrm{r}}$, then the value of r is equal to

**Options:**

- **(A)** 9 or 10
- **(B)** 7 or 12
- **(C)** 8 or 10
- **(D)** 8 or 11

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 8 or 11**

**Detailed Solution:**

Using the identity $^{n}C_{r} + ^{n}C_{r-1} = ^{n+1}C_{r}$, we can simplify the given expression step by step.

$^{15}C_{4} + ^{15}C_{5} = ^{16}C_{5}$

Substituting this into the given equation:

$^{16}C_{5} + ^{16}C_{6} + ^{17}C_{7} + ^{18}C_{8} = ^{19}C_{r}$

$^{17}C_{6} + ^{17}C_{7} + ^{18}C_{8} = ^{19}C_{r}$

$^{18}C_{7} + ^{18}C_{8} = ^{19}C_{r}$

$^{19}C_{8} = ^{19}C_{r}$

We know that if $^{n}C_{x} = ^{n}C_{y}$, then either $x = y$ or $x + y = n$.

Therefore, $r = 8$ or $r = 19 - 8 = 11$.

Answer: 8 or 11

</details>

---

### Q4. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\frac{{ }^{10} \mathrm{C}_{\mathrm{r}}}{{ }^{11} \mathrm{C}_{\mathrm{r}}}$, when both the numerator and denominator are at their greatest values, is

**Options:**

- **(A)** $\frac{6}{11}$
- **(B)** $\frac{1}{11}$
- **(C)** $\frac{4}{11}$
- **(D)** $\frac{3}{11}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{6}{11}$**

**Detailed Solution:**

Greatest value of ${ }^{-10} \mathrm{C}_{\mathrm{r}}$ is at $\mathrm{r}=5$ Greatest value of ${ }^{11} \mathrm{C}_{\mathrm{r}}$ is at $\mathrm{r}=5$
$\therefore \quad \frac{{ }^{10} \mathrm{C}_{\mathrm{r}}}{{ }^{11} \mathrm{C}_{\mathrm{r}}}=\frac{{ }^{10} \mathrm{C}_5}{{ }^{11} \mathrm{C}_5}=\frac{\frac{10 !}{5 ! 5 !}}{\frac{11 !}{5 ! 6 !}}=\frac{6}{11}$

</details>

---

### Q5. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The difference between the maximum values of ${ }^6 \mathrm{C}_{\mathrm{r}}$ and ${ }^n \mathrm{C}_{\mathrm{r}} 16$, then $\mathrm{n}=$

**Options:**

- **(A)** 3
- **(B)** 5
- **(C)** 2
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

The maximum value of ${ }^6 \mathrm{C}_{\mathrm{r}}$ occurs at $\mathrm{r}=\frac{6}{2}=3$
$$
\therefore{ }^6 \mathrm{C}_3=\frac{6 !}{3 ! 3 !}=\frac{6 \times 5 \times 4}{6}=20
$$
As per data given $\left|{ }^6 \mathrm{C}_3-{ }^{\mathrm{n}} \mathrm{C}_3\right|=16$
$$
\therefore{ }^{\mathrm{n}} \mathrm{C}_3=20+16 \text { or }{ }^{\mathrm{n}} \mathrm{C}_3=20-16
$$
If ${ }^n C_3=36 \Rightarrow \frac{n !}{(n-3) ! n !}=36 \Rightarrow n(n-1)(n-2)=216$ is not possible for
$$
\mathrm{n} \in \mathrm{N}
$$
$$
\begin{aligned}
& \text { If }{ }^{\mathrm{n}} \mathrm{C}_3=4 \Rightarrow \frac{\mathrm{n} !}{(\mathrm{n}-3) ! 3 !}=4 \Rightarrow \mathrm{n}(\mathrm{n}-1)(\mathrm{n}-2)=24 \\
& \Rightarrow \mathrm{n}=4
\end{aligned}
$$

</details>

---

### Q6. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The co-efficient of $x^{6}$ in the series of $e^{2 x}$ is

**Options:**

- **(A)** $\frac{2}{45}$
- **(B)** $\frac{7}{45}$
- **(C)** $\frac{4}{45}$
- **(D)** $\frac{1}{45}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4}{45}$**

**Detailed Solution:**

$e^{2 x}=1+2 x+\frac{(2 x)^{2}}{2 !}+\frac{(2 x)^{3}}{3 !}+\frac{(2 x)^{4}}{4 !}+\frac{(2 x)^{6}}{6 !}+$
$x^{6} \rightarrow$ coefficient $=\left(\frac{2^{6} \cdot x^{6}}{6 !}=\frac{4}{45}\right.$

</details>

---

