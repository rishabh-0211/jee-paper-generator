# MHT CET Mathematics - Limits

## Topic 6: Miscellaneous

**Total Questions:** 5

---

### Q1. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{n \rightarrow \infty} \frac{1}{n^3+1}+\frac{4}{n^3+1}+\frac{9}{n^3+1}+\ldots \ldots \ldots \ldots+\frac{n^2}{n^3+1}=$

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{6}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{3}$**

**Detailed Solution:**

The given limit can be written as:

$\lim_{n \rightarrow \infty} \sum_{k=1}^{n} \dfrac{k^2}{n^3+1}$

Since the denominator is common, we can write it as:

$\lim_{n \rightarrow \infty} \dfrac{1}{n^3+1} \sum_{k=1}^{n} k^2$

Using the formula for the sum of squares of the first $n$ natural numbers, $\sum_{k=1}^{n} k^2 = \dfrac{n(n+1)(2n+1)}{6}$:

$\lim_{n \rightarrow \infty} \dfrac{n(n+1)(2n+1)}{6(n^3+1)}$

$\lim_{n \rightarrow \infty} \dfrac{2n^3 + 3n^2 + n}{6n^3 + 6}$

Dividing the numerator and denominator by $n^3$:

$\lim_{n \rightarrow \infty} \dfrac{2 + \dfrac{3}{n} + \dfrac{1}{n^2}}{6 + \dfrac{6}{n^3}}$

As $n \rightarrow \infty$, $\dfrac{1}{n} \rightarrow 0$. Thus, the limit evaluates to:

$\dfrac{2 + 0 + 0}{6 + 0} = \dfrac{2}{6} = \dfrac{1}{3}$

Answer: $\frac{1}{3}$

</details>

---

### Q2. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{n \rightarrow \infty}\left[\frac{1}{1-\mathrm{n}^4}+\frac{8}{1-\mathrm{n}^4}+\ldots \ldots \ldots \ldots . .+\frac{\mathrm{n}^3}{1-\mathrm{n}^4}\right]=$

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{1}{2}$
- **(C)** $-\frac{1}{2}$
- **(D)** $-\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{1}{4}$**

**Detailed Solution:**

The given limit can be written as:

$\lim_{n \rightarrow \infty} \left[ \dfrac{1^3 + 2^3 + \ldots + n^3}{1-n^4} \right]$

Using the formula for the sum of cubes of the first $n$ natural numbers, $\sum_{k=1}^n k^3 = \left( \dfrac{n(n+1)}{2} \right)^2$, we get:

$\lim_{n \rightarrow \infty} \dfrac{\left( \dfrac{n(n+1)}{2} \right)^2}{1-n^4}$

$\lim_{n \rightarrow \infty} \dfrac{n^2(n+1)^2}{4(1-n^4)}$

Dividing the numerator and the denominator by $n^4$:

$\lim_{n \rightarrow \infty} \dfrac{n^4 \left(1 + \dfrac{1}{n}\right)^2}{4n^4 \left(\dfrac{1}{n^4} - 1\right)}$

$\lim_{n \rightarrow \infty} \dfrac{\left(1 + \dfrac{1}{n}\right)^2}{4 \left(\dfrac{1}{n^4} - 1\right)}$

As $n \rightarrow \infty$, $\dfrac{1}{n} \rightarrow 0$ and $\dfrac{1}{n^4} \rightarrow 0$. Substituting these values:

$\dfrac{(1 + 0)^2}{4(0 - 1)} = -\dfrac{1}{4}$

Answer: $-\frac{1}{4}$

</details>

---

### Q3. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\mathrm{S}_1=\sum_{\mathrm{r}=1}^{\mathrm{n}} \mathrm{r}, \mathrm{S}_2=\sum_{\mathrm{r}=1}^{\mathrm{n}} \mathrm{r}^2$ and $\mathrm{S}_3=\sum_{\mathrm{r}=1}^{\mathrm{n}} \mathrm{r}^3$, then the value of $\lim _{n \rightarrow \infty} \dfrac{s_1\left(1+\dfrac{s_3}{4}\right)}{s_2^2}$ is

**Options:**

- **(A)** $\dfrac{9}{16}$
- **(B)** $\dfrac{9}{2}$
- **(C)** $\dfrac{9}{32}$
- **(D)** $\dfrac{9}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{9}{32}$**

**Detailed Solution:**

The sums of the first $n$ natural numbers, their squares, and their cubes are given by:

$S_1 = \sum_{r=1}^n r = \dfrac{n(n+1)}{2}$

$S_2 = \sum_{r=1}^n r^2 = \dfrac{n(n+1)(2n+1)}{6}$

$S_3 = \sum_{r=1}^n r^3 = \dfrac{n^2(n+1)^2}{4}$

Substitute these into the given limit expression:

$\lim_{n \rightarrow \infty} \dfrac{S_1\left(1+\dfrac{S_3}{4}\right)}{S_2^2} = \lim_{n \rightarrow \infty} \dfrac{\dfrac{n(n+1)}{2} \left(1 + \dfrac{n^2(n+1)^2}{16}\right)}{\left(\dfrac{n(n+1)(2n+1)}{6}\right)^2}$

Simplifying the expression:

$= \lim_{n \rightarrow \infty} \dfrac{18}{n(n+1)(2n+1)^2} \left(1 + \dfrac{n^2(n+1)^2}{16}\right)$

Separating into two limits:

$= \lim_{n \rightarrow \infty} \dfrac{18}{n(n+1)(2n+1)^2} + \lim_{n \rightarrow \infty} \dfrac{18 n^2(n+1)^2}{16 n(n+1)(2n+1)^2}$

The first term approaches $0$ as $n \rightarrow \infty$. For the second term, simplifying the fraction gives:

$= 0 + \lim_{n \rightarrow \infty} \dfrac{9 n(n+1)}{8 (2n+1)^2}$

Dividing the numerator and the denominator by $n^2$:

$= \lim_{n \rightarrow \infty} \dfrac{9 \left(1 + \dfrac{1}{n}\right)}{8 \left(2 + \dfrac{1}{n}\right)^2}$

As $n \rightarrow \infty$, $\dfrac{1}{n} \rightarrow 0$, yielding:

$= \dfrac{9(1)}{8(2)^2} = \dfrac{9}{32}$

Answer: $\dfrac{9}{32}$

</details>

---

### Q4. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $l=\lim _{x \rightarrow 0} \frac{x}{|x|+x^2}$, then the value of $l$ is

**Options:**

- **(A)** $1$
- **(B)** $-1$
- **(C)** $2$
- **(D)** non-existant

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) non-existant**

**Detailed Solution:**

Let $\mathrm{f}(x)=\frac{x}{|x|+x^2}$
$\begin{aligned}
& \lim _{x \rightarrow 0^{-}} \mathrm{f}(x)=\lim _{x \rightarrow 0} \frac{x}{-x+x^2}=\lim _{x \rightarrow 0} \frac{1}{-1+x}=-1 \\
& \lim _{x \rightarrow 0^{+}} \mathrm{f}(x)=\lim _{x \rightarrow 0} \frac{x}{x+x^2}=\lim _{x \rightarrow 0} \frac{1}{1+x}=1
\end{aligned}$
Here, $\lim _{x \rightarrow 0^{-}} \mathrm{f}(x) \neq \lim _{x \rightarrow 0^{+}} \mathrm{f}(x)$
$\therefore \quad$ Value of $l$ is non-existant

</details>

---

### Q5. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $a=\lim _{n \rightarrow \infty} \frac{1+2+3+\ldots+n}{n^2}$ and $b=\lim _{n \rightarrow \infty} \frac{1^2+2^2+3^2+\ldots+n^2}{n^3}$, then

**Options:**

- **(A)** $a=b$
- **(B)** $2 \mathrm{a}=3 \mathrm{~b}$
- **(C)** $a=2 b$
- **(D)** $3 \mathrm{a}=2 \mathrm{~b}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \mathrm{a}=3 \mathrm{~b}$**

**Detailed Solution:**

$$
\begin{aligned}
& a=\lim _{n \rightarrow \infty} \frac{1+2+3+\ldots+n}{n^2} \\
& =\lim _{n \rightarrow \infty} \frac{n(n+1)}{2(n)(n)}=\lim _{n \rightarrow \infty}\left(\frac{1}{2}\right)\left(\frac{n+1}{n}\right)=\frac{1}{2} \lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)=\frac{1}{2} \\
& b=\lim _{n \rightarrow \infty} \frac{1^2+2^2+3^2+\ldots .+n^2}{n^3} \\
& =\lim _{n \rightarrow \infty} \frac{n(n+1)(2 n+1)}{6 n^3}=\lim _{n \rightarrow \infty} \frac{2 n^2+3 n+1}{6 n^2} \\
& =\lim _{n \rightarrow \infty}\left(\frac{1}{6}\right)\left(2+\frac{3}{n}+\frac{1}{n^2}\right)=\frac{2}{6}=\frac{1}{3}
\end{aligned}
$$
Thus $\mathrm{a}=\frac{1}{2}$ and $\mathrm{b}=\frac{1}{3} \Rightarrow 2 \mathrm{a}=3 \mathrm{~b}$

</details>

---

