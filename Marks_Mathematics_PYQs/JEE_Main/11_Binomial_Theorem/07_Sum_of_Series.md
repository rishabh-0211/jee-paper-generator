# JEE Main Mathematics - Binomial Theorem

## Topic 7: Sum of Series

**Total Questions:** 53

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $26\left(\dfrac{2^3}{3}\binom{12}{2} + \dfrac{2^5}{5}\binom{12}{4} + \dfrac{2^7}{7}\binom{12}{6} + \ldots + \dfrac{2^{13}}{13}\binom{12}{12}\right) = 3^{13} - \alpha$, then $\alpha$ is equal to:

**Options:**

- **(A)** $45$
- **(B)** $48$
- **(C)** $51$
- **(D)** $54$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $51$**

**Detailed Solution:**

Let $S = \dfrac{2^3}{3} \ ^{12}C_{2} + \dfrac{2^5}{5} \ ^{12}C_{4} + \dfrac{2^7}{7} \ ^{12}C_{6} + \ldots + \dfrac{2^{13}}{13} \ ^{12}C_{12}$

Using the property $\dfrac{1}{r+1} \ ^{n}C_{r} = \dfrac{1}{n+1} \ ^{n+1}C_{r+1}$, we can rewrite the terms:

$S = \dfrac{2^3}{13} \ ^{13}C_{3} + \dfrac{2^5}{13} \ ^{13}C_{5} + \dfrac{2^7}{13} \ ^{13}C_{7} + \ldots + \dfrac{2^{13}}{13} \ ^{13}C_{13}$

$13S = 2^3 \ ^{13}C_{3} + 2^5 \ ^{13}C_{5} + 2^7 \ ^{13}C_{7} + \ldots + 2^{13} \ ^{13}C_{13}$

We know the binomial expansions:

$(1+x)^{13} = \ ^{13}C_{0} + \ ^{13}C_{1}x + \ ^{13}C_{2}x^2 + \ ^{13}C_{3}x^3 + \ldots + \ ^{13}C_{13}x^{13}$

$(1-x)^{13} = \ ^{13}C_{0} - \ ^{13}C_{1}x + \ ^{13}C_{2}x^2 - \ ^{13}C_{3}x^3 + \ldots - \ ^{13}C_{13}x^{13}$

Subtracting the second equation from the first gives:

$(1+x)^{13} - (1-x)^{13} = 2 \left( \ ^{13}C_{1}x + \ ^{13}C_{3}x^3 + \ ^{13}C_{5}x^5 + \ldots + \ ^{13}C_{13}x^{13} \right)$

Substituting $x = 2$:

$(1+2)^{13} - (1-2)^{13} = 2 \left( \ ^{13}C_{1}(2) + \ ^{13}C_{3}(2^3) + \ ^{13}C_{5}(2^5) + \ldots + \ ^{13}C_{13}(2^{13}) \right)$

$3^{13} - (-1)^{13} = 2 \left( 26 + 13S \right)$

$3^{13} + 1 = 52 + 26S$

$26S = 3^{13} + 1 - 52$

$26S = 3^{13} - 51$

Comparing this with the given expression $26S = 3^{13} - \alpha$, we get:

$\alpha = 51$

Answer: $51$

</details>

---

### Q2. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{S}=\frac{1}{25!}+\frac{1}{3!23!}+\frac{1}{5!21!}+\ldots$ up to 13 terms. If $13 \mathrm{~S}=\frac{2^{k}}{n!}, k \in \mathrm{~N}$, then $n+k$ is equal to

**Options:**

- **(A)** 50
- **(B)** 49
- **(C)** 52
- **(D)** 51

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 49**

**Detailed Solution:**

The general term is $\frac{1}{(2r-1)!(27-2r)!}$ for $r=1$ to $13$.
Multiply and divide by $26!$: $\frac{1}{(2r-1)!(27-2r)!} = \frac{1}{26!}\binom{26}{2r-1}$
$S = \frac{1}{26!}\sum_{r=1}^{13}\binom{26}{2r-1} = \frac{1}{26!}\left[\binom{26}{1}+\binom{26}{3}+\cdots+\binom{26}{25}\right]$
Sum of odd-indexed binomial coefficients: $\sum \binom{26}{\text{odd}} = 2^{25}$
$S = \frac{2^{25}}{26!}$
$13S = \frac{13 \cdot 2^{25}}{26!} = \frac{13 \cdot 2^{25}}{26 \cdot 25!} = \frac{2^{25}}{2 \cdot 25!} = \frac{2^{24}}{25!}$
So $k = 24,\; n = 25$, giving $n + k = 49$.

</details>

---

### Q3. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\frac{{ }^{100} \mathrm{C}_{50}}{51}+\frac{{ }^{100} \mathrm{C}_{51}}{52}+\ldots.+\frac{{ }^{100} \mathrm{C}_{100}}{101}$ is :

**Options:**

- **(A)** $\frac{2^{101}}{100}$
- **(B)** $\frac{2^{100}}{100}$
- **(C)** $\frac{2^{101}}{101}$
- **(D)** $\frac{2^{100}}{101}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2^{100}}{101}$**

**Detailed Solution:**

Using $\frac{\binom{n}{r}}{r+1} = \frac{1}{n+1}\binom{n+1}{r+1}$:
$\sum_{r=50}^{100}\frac{\binom{100}{r}}{r+1} = \frac{1}{101}\sum_{r=50}^{100}\binom{101}{r+1} = \frac{1}{101}\sum_{k=51}^{101}\binom{101}{k}$.
Since $101$ is odd, by symmetry $\sum_{k=51}^{101}\binom{101}{k} = \sum_{k=0}^{50}\binom{101}{k} = \frac{2^{101}}{2} = 2^{100}$.
Required value $= \frac{2^{100}}{101}$.

</details>

---

### Q4. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{C}_{\mathrm{r}}$ denote the coefficient of $x^{\mathrm{r}}$ in the binomial expansion of $(1+x)^{\mathrm{n}}, \mathrm{n} \in \mathrm{N}, 0 \leq \mathrm{r} \leq \mathrm{n}$. If $P_{n}=C_{0}-C_{1}+\frac{2^{2}}{3} C_{2}-\frac{2^{3}}{4} C_{3}+\ldots. .+\frac{(-2)^{n}}{n+1} C_{n}$, then the value of $\sum_{n=1}^{25} \frac{1}{P_{2 n}}$ equals.

**Options:**

- **(A)** 650
- **(B)** 675
- **(C)** 525
- **(D)** 580

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 675**

**Detailed Solution:**

Using the identity $\frac{1}{r+1}\binom{n}{r} = \frac{1}{n+1}\binom{n+1}{r+1}$,
we get $P_n = \sum_{r=0}^{n}\frac{(-2)^r}{r+1}C_r = \frac{1}{n+1}\sum_{s=1}^{n+1}(-2)^{s}\binom{n+1}{s}$.
Since $(1-2)^{n+1} = (-1)^{n+1} = \sum_{s=0}^{n+1}(-2)^s\binom{n+1}{s}$,
we have $\sum_{s=1}^{n+1}(-2)^s\binom{n+1}{s} = (-1)^{n+1} - 1$.
For even $n = 2k$: $P_{2k} = \frac{1 - (-1)}{2(2k+1)} = \frac{1}{2k+1}$.
Thus $\frac{1}{P_{2n}} = 2n+1$, and $\sum_{n=1}^{25}(2n+1) = 2 \cdot \frac{25 \cdot 26}{2} + 25 = 675$.

</details>

---

### Q5. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The coefficient of $x^{48}$ in $(1+x)+2(1+x)^{2}+3(1+x)^{3}+\ldots+100(1+x)^{100}$ is equal to

**Options:**

- **(A)** $100 \cdot{ }^{100} \mathrm{C}_{49}-{ }^{100} \mathrm{C}_{48}$
- **(B)** ${ }^{100} \mathrm{C}_{50}+{ }^{101} \mathrm{C}_{49}$
- **(C)** ${ }^{100 \cdot{ }^{101} \mathrm{C}_{49}-{ }^{101} \mathrm{C}_{50}}$
- **(D)** $100 \cdot{ }^{100} \mathrm{C}_{49}-{ }^{100} \mathrm{C}_{50}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) ${ }^{100 \cdot{ }^{101} \mathrm{C}_{49}-{ }^{101} \mathrm{C}_{50}}$**

**Detailed Solution:**

Let $1 + x = r$
$\therefore S = 1 \cdot r + 2 \cdot r^2 + 3 \cdot r^3 + \ldots + 100r^{100}$ ......(1) (AGP)
$rS = 1 \cdot r^2 + 2 \cdot r^3 + \ldots + 99r^{100} + 100r^{101}$ ......(2)
(1) $-$ (2) gives
$S = -\dfrac{(1+x)^{101}}{x^2} + \dfrac{1}{x^2} + \dfrac{100(1+x)^{101}}{x}$
$\therefore$ coefficient $x^{48}$ in S
$= -$ coefficient of $x^{48}$ in $\dfrac{(1+x)^{101}}{x^2} + 100 \cdot$ Coefficient of $x^{48}$ in $\dfrac{(1+x)^{101}}{x}$
$= 100 \cdot {}^{101}C_{49} - {}^{101}C_{50}$

</details>

---

### Q6. JEE Main 2025 (7 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

The sum of the series
$2 \times 1 \times{ }^{20} \mathrm{C}_4-3 \times 2 \times{ }^{20} \mathrm{C}_5+4 \times 3 \times{ }^{20} \mathrm{C}_6-5 \times 4$ $\times { }^{20} \mathrm{C}_7+\ldots+18 \times 17 \times{ }^{20} \mathrm{C}_{20}$, is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **34**

**Detailed Solution:**

$\begin{aligned}
& (1-\mathrm{x})^{20}={ }^{20} \mathrm{C}_0-{ }^{20} \mathrm{C}_1 \mathrm{x}+{ }^{20} \mathrm{C}_2 \mathrm{x}^2 \ldots . .+{ }^{20} \mathrm{C}_{20} \mathrm{x}^{20} \\
& \frac{(1-\mathrm{x})^{20}}{\mathrm{x}^2}=\frac{{ }^{20} \mathrm{C}_0}{\mathrm{x}^2}-\frac{{ }^{20} \mathrm{C}_1}{\mathrm{x}}+{ }^{20} \mathrm{C}_2-{ }^{20} \mathrm{C}_3 \mathrm{x}+{ }^{20} \mathrm{C}_4 \mathrm{x}^2 \ldots
\end{aligned}$

Diff twice and put $\mathrm{x}=1$
$\begin{aligned}
& =6-{ }^{20} \mathrm{C}_1(2)+\mathrm{A} \\
& \mathrm{~A}=40-6=34
\end{aligned}$

</details>

---

### Q7. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If \(1^2 \cdot\left({ }^{15} C_1\right)+2^2 \cdot\left({ }^{15} C_2\right)+3^2 \cdot\left({ }^{15} C_3\right)+\ldots\) \(+15^2 \cdot\left({ }^{15} C_{15}\right)=2^m \cdot 3^n \cdot 5^k\), where \(m, n, k \in \mathbf{N}\), then \(\mathrm{m}+\mathrm{n}+\mathrm{k}\) is equal to :

**Options:**

- **(A)** $19$
- **(B)** $21$
- **(C)** $18$
- **(D)** $20$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $19$**

**Detailed Solution:**

$\begin{aligned} & \sum_{\mathrm{r}=1}^{15} \mathrm{r}^2\left({ }^{15} \mathrm{C}_{\mathrm{r}}\right) \Rightarrow 15 \sum_{\mathrm{r}=1}^{15} \mathrm{r}^{14} \mathrm{C}_{\mathrm{r}-1} \\ & 15 \sum_{\mathrm{r}=1}^{15}(\mathrm{r}-1+1){ }^{14} \mathrm{C}_{\mathrm{r}-1} \\ & 15 \cdot 14 \sum_{\mathrm{r}=1}^{15}{ }^{13} \mathrm{C}_{\mathrm{r}-2}+15 \sum_{\mathrm{r}=1}^{15}{ }^{14} \mathrm{C}_{\mathrm{r}-1} \\ & 15 \cdot 14 \cdot 2^{13}+15 \cdot 2^{14} \\ & 3^1 \cdot 2^{13}(70+10) \\ & 3^1 \cdot 2^{13} \cdot 80 \\ & 3^1 \cdot 5^1 \cdot 2^{17} \\ & \mathrm{~m}=17 \mathrm{n}=1 \quad \mathrm{k}=1 \\ & \text { option }(1)\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sum_{\mathrm{r}=1}^9\left(\frac{\mathrm{r}+3}{2^{\mathrm{r}}}\right) .{ }^9 \mathrm{C}_{\mathrm{r}}=\alpha\left(\frac{3}{2}\right)^9-\beta, \quad \alpha, \beta \in \mathrm{N}, \quad$ then $(\alpha+\beta)^2$ is equal to

**Options:**

- **(A)** $27$
- **(B)** $9$
- **(C)** $81$
- **(D)** $18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $81$**

**Detailed Solution:**

$\sum_{\mathrm{r}=1}^9\left(\frac{\mathrm{r}+3}{2^{\mathrm{r}}}\right) \cdot{ }^9 \mathrm{C}_{\mathrm{r}}=\alpha\left(\frac{3}{2}\right)^9-\beta, \alpha, \beta \in \mathrm{N}$
Now,
$\begin{aligned}
& \sum_{\mathrm{r}=1}^9\left(\frac{\mathrm{r}+3}{2^{\mathrm{r}}}\right) \cdot{ }^9 \mathrm{C}_{\mathrm{r}}=\sum_{\mathrm{r}=1}^9\left(\frac{\mathrm{r}}{2^{\mathrm{r}}}\right) \cdot{ }^9 \mathrm{C}_{\mathrm{r}}+\sum_{\mathrm{r}=1}^9\left(\frac{3}{2^{\mathrm{r}}}\right) \cdot{ }^9 \mathrm{C}_{\mathrm{r}} \\
& =\sum_{\mathrm{r}=1}^9\left(\frac{9}{2^{\mathrm{r}}}\right) \cdot{ }^8 \mathrm{C}_{\mathrm{r}-1}+3 \sum_{\mathrm{r}=1}^9{ }^9 \mathrm{C}_{\mathrm{r}}\left(\frac{1}{2}\right)^{\mathrm{r}}\left[\mathrm{U} \sin \mathrm{~g} \frac{{ }^9 \mathrm{C}_{\mathrm{r}}}{{ }^8 \mathrm{C}_{\mathrm{r}-1}}=\frac{9}{\mathrm{r}}\right] \\
& =\frac{9}{2} \sum_{\mathrm{r}=1}^9{ }^8 \mathrm{C}_{\mathrm{r}-1}\left(\frac{1}{2}\right)^{\mathrm{r}-1}+3\left(\sum_{\mathrm{r}=0}^9\left({ }^9 \mathrm{C}_{\mathrm{r}}\left(\frac{1}{2}\right)^{\mathrm{r}}\right)-1\right) \\
& =\frac{9}{2}\left(1+\frac{1}{2}\right)^8+3\left(\left(1+\frac{1}{2}\right)^9-1\right)
\end{aligned}$
$=\frac{9}{2} \cdot\left(\frac{3}{2}\right)^8+3\left(\frac{3}{2}\right)^9-3=6 \cdot\left(\frac{3}{2}\right)^9-3$
Hence, $\alpha=6, \beta=3$
Thus $(\alpha+\beta)^2=81$

</details>

---

### Q9. JEE Main 2025 (28 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

${ }^{\text { } }$ If $\alpha=1+\sum_{r=1}^6(-3)^{r-1} \quad{ }^{12} \mathrm{C}_{2 r-1}$, then the distance of the point $(12, \sqrt{3})$ from the line $\alpha x-\sqrt{3} y+1=0$ is _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$\begin{aligned} & \alpha=1+\sum_{\mathrm{r}=1}^6(-1)^{\mathrm{r}-1}{ }^{12} \mathrm{C}_{2 \mathrm{r}-1} 3^{\mathrm{r}-1} \\ & \alpha=1+\sum_{\mathrm{r}=1}^6{ }^{12} \mathrm{C}_{2 \mathrm{r}-1} \frac{(\sqrt{3} \mathrm{i})^{2 \mathrm{t}-1}}{\sqrt{3} \mathrm{i}} \quad \mathrm{i}=\text { iota, let } \sqrt{3} \mathrm{i}=\mathrm{x}\end{aligned}$
$\begin{aligned} \alpha & =1+\frac{1}{\sqrt{3} \mathrm{i}}\left({ }^{12} \mathrm{C}_1 \mathrm{x}+{ }^{12} \mathrm{C}_3 \mathrm{x}^3+\ldots .{ }^{12} \mathrm{C}_{11} \mathrm{x}^{11}\right) \\ & =1+\frac{1}{\sqrt{3} \mathrm{i}}\left(\frac{(1+\sqrt{3} \mathrm{i})^{12}-(1-\sqrt{3} \mathrm{i})^{12}}{2}\right)\end{aligned}$
$=1+\frac{1}{\sqrt{3} \mathrm{i}}\left(\frac{\left(-2 \mathrm{w}^2\right)^{12}-(2 \mathrm{w})^{12}}{2}\right)=1$
so distance of $(12, \sqrt{3})$ from $x-\sqrt{3} y+1=0$ is
$\frac{12-3+1}{2}=5$

</details>

---

### Q10. JEE Main 2025 (22 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

If $\sum_{r=1}^{30} \frac{r^2\left({ }^{30} C_r\right)^2}{{ }^{30} C_{r-1}}=\alpha \times 2^{29}$, then $\alpha$ is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **465**

**Detailed Solution:**

$\begin{aligned} & \sum_{\mathrm{r}=1}^{30} \frac{\mathrm{r}^2\left({ }^{30} \mathrm{C}_{\mathrm{r}}\right)^2}{{ }^{30} \mathrm{C}_{\mathrm{r}-1}} \\ & =\sum_{\mathrm{r}=1}^{30} \mathrm{r}^2\left(\frac{31-\mathrm{r}}{\mathrm{r}}\right) \cdot \frac{30!}{\mathrm{r}!(30-\mathrm{r})!} \\ & \left(\because \frac{{ }^{30} \mathrm{C}_{\mathrm{r}}}{{ }^{30} \mathrm{C}_{\mathrm{r}-1}}=\frac{30-\mathrm{r}+1}{\mathrm{r}}=\frac{31-\mathrm{r}}{\mathrm{r}}\right)\end{aligned}$


$\begin{aligned} & =\sum_{\mathrm{r}=1}^{30} \frac{(31-\mathrm{r}) 30!}{(\mathrm{r}-1)!(30-\mathrm{r})!} \\ & =30 \sum_{\mathrm{r}=1}^{30} \frac{(31-\mathrm{r}) 29!}{(\mathrm{r}-1)!(30-\mathrm{r})!} \\ & =30 \sum_{\mathrm{r}=1}^{30}(30-\mathrm{r}+1)^{29} \mathrm{C}_{30-\mathrm{r}} \\ & =30\left(\sum_{\mathrm{r}=1}^{30}(31-\mathrm{r})^{29} \mathrm{C}_{30-\mathrm{r}}+\sum_{\mathrm{r}=1}^{30}{ }^{29} \mathrm{C}_{30-\mathrm{r}}\right) \\ & =30\left(29 \times 2^{28}+2^{29}\right)=30(29+2) 2^{28} \\ & =15 \times 31 \times 2^{29} \\ & =465\left(2^{29}\right) \\ & \alpha=465\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (22 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

If $\sum_{r=0}^5 \frac{{ }^{11} C_{2r+1}}{2 r+2}=\frac{\mathrm{m}}{\mathrm{n}}, \operatorname{gcd}(\mathrm{m}, \mathrm{n})=1$, then $\mathrm{m}-\mathrm{n}$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2035**

**Detailed Solution:**

$\begin{aligned}
& (1+x)^{11}={ }^{11} C_0+{ }^{11} C_1 x+{ }^{11} C_2 x^2+\cdots+{ }^{11} C_{11} x^{11} \\
& \int_0^1(1+x)^{11} d x=\int_0^1\left({ }^{11} C_0+{ }^{11} C_1 x+{ }^{11} C_2 x^2+\cdots+{ }^{11} C_{11} x x^{11}\right) d x \\
& \left.\left.\frac{(1-x)^{12}}{12}\right|_0 ^1={ }^{11} C_{0 x}+\frac{{ }^{11} C_1 x^2}{2}+\frac{{ }^{11} C_2 x}{3}+\cdots+\frac{{ }^{11} C_{11} x^{12}}{12}\right]_0^1 \\
& \frac{2^{12}-1}{12}=C_0+\frac{C_1}{2}+\frac{C_2}{3}+\cdots+\frac{C_{11}}{12} \ldots(1)
\end{aligned}$
Now,
$\begin{aligned}
& \int_{-1}^0(1+x)^{11} d x=\int_{-1}^0\left({ }^{11} C_0+{ }^{11} C_1 x+{ }^{11} C_2 x^2+\cdots+{ }^{11} C_{11} x^{11}\right) d x \\
& \left.\left.\frac{(1+x)^{12}}{12}\right]_{-1}^0={ }^{11} C_0 x+\frac{{ }^{11} C_1 x^2}{2}+\frac{{ }^{11} C_2 x^3}{3}+\cdots+\frac{{ }^{11} C_{11} x^{12}}{12}\right]_{-1}^0
\end{aligned}$
$\frac{1}{12}=C_0-\frac{C_1}{2}+\frac{C_2}{3} \cdots$
$\begin{aligned}
& (1)-(2) \\
& =\frac{2^{12}-2}{12}=2\left[\frac{C_1}{2}+\frac{C_3}{4}+\cdots\right] \\
& \Rightarrow \sum_{r=0}^5 \frac{C_{2 r+1}}{2 r+2}=\frac{2^{11}-1}{12}=\frac{2047}{12}=\frac{m}{n} \\
& =2047-12=2035
\end{aligned}$

</details>

---

### Q12. JEE Main 2024 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $\alpha=\sum_{r=0}^n\left(4 r^2+2 r+1\right){ }^n C_r$ and $\beta=\left(\sum_{r=0}^n \frac{{ }^n C_r}{r+1}\right)+\frac{1}{n+1}$. If $140 < \frac{2 \alpha}{\beta} < 281$, then the value of $n$ is _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$\begin{aligned} & \alpha=\sum_{r=0}^n\left(4 r^2+2 r+1\right) \cdot{ }^n C_r \\ & \alpha=4 \sum_{r=0}^n r^2 \cdot \frac{n}{r} \cdot{ }^{n-1} C_{r-1}+2 \sum_{r=0}^n r \cdot \frac{n}{r} \cdot{ }^{n-1} C_{r-}+\sum_{r=0}^n{ }^n C_r \\ & +4 n \sum_{r=0}^n{ }^{n-1} C_{r-1}+2 n \sum_{r=0}^n{ }^{n-1} C_{r-1}+\sum_{r=0}^n{ }^n C_r \\ & \alpha=4 n(n-1) \cdot 2^{n-2}+4 n \cdot 2^{n-1}+2 n \cdot 2^{n-1}+2^n \\ & \alpha=2^{n-2}[4 n(n-1)+8 n+4 n+4] \\ & \alpha=2^{n-2}\left[4 n^2+8 n+4\right] \\ & \alpha=2 n(n+1)^2 \\ & \beta=\sum_{r=0}^n \frac{{ }^n C_r}{r+1}+\frac{1}{n+1} \\ & =\sum_{r=0}^n \frac{C^{n+1} C_{r+1}}{n+1}+\frac{1}{n+1} \\ & =\frac{1}{n+1}\left(1+{ }^{n+1} C_1+\ldots .+{ }^{n+1} C_{n+1}\right) \\ & =\frac{2^{n+1}}{n+1} \\ & \frac{2 \alpha}{\beta}=\frac{2^{n+1}(n+1)^2}{2^{n+1}} \cdot(n+1)=(n+1)^3 \\ & 140 < (n+1)^3 < 281 \\ & n=4 \Rightarrow(n+1)^3=125 \\ & n=5 \Rightarrow(n+1)^3=216 \\ & n=6 \Rightarrow(n+1)^3=343 \\ & \therefore n=5\end{aligned}$

</details>

---

### Q13. JEE Main 2024 (04 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $a=1+\frac{{ }^2 \mathrm{C}_2}{3 !}+\frac{{ }^3 \mathrm{C}_2}{4 !}+\frac{{ }^4 \mathrm{C}_2}{5 !}+\ldots$,
$\mathrm{b}=1+\frac{{ }^1 \mathrm{C}_0+{ }^1 \mathrm{C}_1}{1 !}+\frac{{ }^2 \mathrm{C}_0+{ }^2 \mathrm{C}_1+{ }^2 \mathrm{C}_2}{2 !}+\frac{{ }^3 \mathrm{C}_0+{ }^3 \mathrm{C}_1+{ }^3 \mathrm{C}_2+{ }^3 \mathrm{C}_3}{3 !}+\ldots$
Then $\frac{2 b}{a^2}$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{f}(\mathrm{x})=1+\frac{(1+\mathrm{x})}{1 !}+\frac{(1+\mathrm{x})^2}{2 !}+\frac{(1+\mathrm{x})^3}{3 !}+\ldots . . \\
& \frac{\mathrm{e}^{(1+\mathrm{x})}}{1+\mathrm{x}}=\frac{1}{1+\mathrm{x}}+1+\frac{(1+\mathrm{x})}{2 !}+\frac{(1+\mathrm{x})^2}{3 !}+\frac{(1+\mathrm{x})^2}{4 !} \\
& \text { coef } \mathrm{x}^2 \text { in RHS : } 1+\frac{{ }^2 \mathrm{C}_2}{3}+\frac{{ }^3 \mathrm{C}_2}{4}+\ldots=\mathrm{a}
\end{aligned}$
coeff. $x^2$ in L.H.S.
$e\left(1+x+\frac{x^2}{2 !}\right) \ldots\left(1-x+\frac{x^2}{2 !} \ldots \ldots\right)$
is $\mathrm{e}-\mathrm{e}+\frac{\mathrm{e}}{2 !}=\mathrm{a}$
$\begin{aligned}
& \mathrm{b}=1+\frac{2}{1 !}+\frac{2^2}{2 !}+\frac{2^3}{3 !}+\ldots \ldots=\mathrm{e}^2 \\
& \frac{2 \mathrm{~b}}{\mathrm{a}^2}=8
\end{aligned}$

</details>

---

### Q14. JEE Main 2024 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mn>2</mn></mfrac><mo>+</mo><mfrac><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mn>3</mn></mfrac><mo>+</mo><mo>…</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mn>10</mn></mfrac><mo>=</mo><mfrac><mi>n</mi><mi>m</mi></mfrac></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>gcd</mo><mo>(</mo><mi>n</mi><mo>,</mo><mi>m</mi><mo>)</mo><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>+</mo><mi>m</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2041**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mn>2</mn></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>3</mn></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>10</mn></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mi>m</mi></mstyle><mstyle displaystyle="true"><mi>n</mi></mstyle></mfrac></math></p><p>Now, we know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>11</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mi>x</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>11</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><msup><mi>x</mi><mn>11</mn></msup></math></p><p>Now integrating the above expression both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>11</mn></msup><mo>d</mo><mi>x</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mn>1</mn></msubsup><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mi>x</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>11</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><msup><mi>x</mi><mn>11</mn></msup><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msubsup><mfenced close="]" open="["><mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>12</mn></msup><mn>12</mn></mfrac></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mi>x</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>11</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mfrac><msup><mi>x</mi><mn>12</mn></msup><mn>12</mn></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><msup><mn>2</mn><mn>12</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>12</mn></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mn>2</mn></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>3</mn></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>10</mn></mstyle></mfrac><mo>+</mo><mfrac><mn>11</mn><mn>11</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math>​​​​​​</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><msup><mn>2</mn><mn>12</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>12</mn></mfrac><mo>-</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>12</mn></mfrac><mo>=</mo><mfrac><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mn>2</mn></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>3</mn></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>10</mn></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mn>2</mn></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>3</mn></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>10</mn></mstyle></mfrac><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mn>12</mn></msup><mo>-</mo><mn>2</mn><mo>-</mo><mn>24</mn></mrow><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mn>2</mn></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>3</mn></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>10</mn></mstyle></mfrac><mo>=</mo><mfrac><mrow><mn>4096</mn><mo>-</mo><mn>26</mn></mrow><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mn>2</mn></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>3</mn></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>10</mn></mstyle></mfrac><mo>=</mo><mfrac><mn>4070</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mn>2</mn></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>3</mn></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mstyle><mstyle displaystyle="true"><mn>10</mn></mstyle></mfrac><mo>=</mo><mfrac><mn>2035</mn><mn>6</mn></mfrac></math></p><p>Hence, on comparing we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>2041</mn></math></p>

</details>

---

### Q15. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> denotes the sum of all the coefficients in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>10</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>n</mi></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> denotes the sum of all the coefficients in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>n</mi></msup></math>, then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><msup><mi mathvariant="normal">B</mi><mn>3</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo> </mo><mi mathvariant="normal">A</mi><mo>=</mo><mi mathvariant="normal">B</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi><mo>=</mo><msup><mi mathvariant="normal">A</mi><mn>3</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mn>3</mn><mo> </mo><mi mathvariant="normal">B</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><msup><mi mathvariant="normal">B</mi><mn>3</mn></msup></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo></math>Sum of the coefficients in the expansion of</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>10</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mo>(</mo><mn>1</mn><mo>-</mo><mn>3</mn><mo>+</mo><mn>10</mn><msup><mo>)</mo><mi>n</mi></msup><mo>=</mo><mo>(</mo><mn>8</mn><msup><mo>)</mo><mi>n</mi></msup><mo>=</mo><mo>(</mo><mn>2</mn><msup><mo>)</mo><mrow><mn>3</mn><mi>n</mi></mrow></msup></math></p><p>(putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>)</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo></math>Sum of the coefficients in the expansion of</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mo>(</mo><mn>1</mn><mo>+</mo><mn>1</mn><msup><mo>)</mo><mi>n</mi></msup><mo>=</mo><msup><mn>2</mn><mi>n</mi></msup></math></p><p>Clearly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msup><mi mathvariant="normal">B</mi><mn>3</mn></msup></math>.</p>

</details>

---

### Q16. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum, of the coefficients of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> terms in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>100</mn></msup><mo>,</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mn>101</mn></msup><msub><mi>C</mi><mn>50</mn></msub></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mn>99</mn></msup><msub><mi>C</mi><mn>49</mn></msub></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>-</mo><mn>101</mn></msup><msub><mi>C</mi><mn>50</mn></msub></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>-</mo><mn>99</mn></msup><msub><mi>C</mi><mn>49</mn></msub></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>-</mo><mn>99</mn></msup><msub><mi>C</mi><mn>49</mn></msub></math>**

**Detailed Solution:**

<p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>100</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>&#183;</mo><mi>x</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>&#183;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>&#183;</mo><msup><mi>x</mi><mn>49</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>100</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>&#183;</mo><msup><mi>x</mi><mn>100</mn></msup></math></p><p>Now let, the sum of first fifty coefficients be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts></math></p><p>Let us substitute <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> in the expansion.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>100</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>&#183;</mo><mn>1</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>&#183;</mo><msup><mn>1</mn><mn>2</mn></msup><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>&#183;</mo><msup><mn>1</mn><mn>49</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>100</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>&#183;</mo><msup><mn>1</mn><mn>100</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>50</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>51</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>52</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>100</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts></math></p><p>There are total of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>101</mn></math> terms and the middle term is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>51</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>50</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts></math>.</p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>50</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>48</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>=</mo><mmultiscripts><mi>C</mi><mn>50</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>48</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>=</mo><mmultiscripts><mi>C</mi><mn>50</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mn>2</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfrac><mmultiscripts><mi>C</mi><mn>50</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mn>2</mn></mfrac><mo>=</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mo>=</mo><mo>-</mo><mfrac><mmultiscripts><mi>C</mi><mn>50</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mn>2</mn></mfrac></math></p><p>Therefore, the required answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mmultiscripts><mi>C</mi><mn>50</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>100</mn><mn>50</mn></mfrac><mmultiscripts><mi>C</mi><mn>49</mn><none/><mprescripts/><none/><mn>99</mn></mmultiscripts><mo>=</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>49</mn><none/><mprescripts/><none/><mn>99</mn></mmultiscripts></math>.</p>

</details>

---

### Q17. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><msup><mo>&#160;</mo><mi>n</mi></msup><msub><mi>C</mi><mi>n</mi></msub><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><msup><mo>&#160;</mo><mi>n</mi></msup><msub><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mo>&#160;</mo><mi>n</mi></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mo>+</mo><mi>n</mi></msup><msub><mi>C</mi><mn>0</mn></msub><mo>=</mo><mfrac><mn>1023</mn><mn>10</mn></mfrac></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><msup><mo>&#160;</mo><mi>n</mi></msup><msub><mi>C</mi><mi>n</mi></msub><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><msup><mo>&#160;</mo><mi>n</mi></msup><msub><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mo>&#160;</mo><mi>n</mi></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mo>+</mo><mi>n</mi></msup><msub><mi>C</mi><mn>0</mn></msub><mo>=</mo><mfrac><mn>1023</mn><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mi>n</mi></munderover><mfrac><mn>1</mn><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac><msup><mo>&#160;</mo><mi>n</mi></msup><msub><mi>C</mi><mi>r</mi></msub><mo>=</mo><mfrac><mn>1023</mn><mn>10</mn></mfrac><mo>&#160;</mo><mfenced><mrow><mo>&#8756;</mo><msup><mo>&#160;</mo><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac><msup><mo>&#160;</mo><mi>n</mi></msup><msub><mi>C</mi><mi>r</mi></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mi>n</mi></munderover><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><msup><mo>&#160;</mo><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mn>1023</mn><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mfenced close="]" open="["><mrow><msup><mrow></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mo>+</mo><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mn>2</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mo>+</mo><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow></mfenced><mo>=</mo><mfrac><mn>1023</mn><mn>10</mn></mfrac></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>=</mo><msup><mn>2</mn><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mn>2</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1023</mn><mn>10</mn></mfrac><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>9</mn></math></p><p>Hence this is the correct option.</p>

</details>

---

### Q18. JEE Main 2023 (11 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

The mean of the coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><msup><mi>x</mi><mn>7</mn></msup></math> in the binomial expression of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mn>9</mn></msup></math> is _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2736**

**Detailed Solution:**

<blockquote><p>We know that.</p><p>Binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>9</mn></msup></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>9</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mi>x</mi><mn>0</mn></msup><msup><mn>2</mn><mn>9</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mi>x</mi><mn>1</mn></msup><msup><mn>2</mn><mn>8</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mi>x</mi><mn>9</mn></msup><msup><mn>2</mn><mn>0</mn></msup></math></p><p>Now put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>9</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>9</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>8</mn></msup><mo>+</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>7</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>0</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mn>9</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>9</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>8</mn></msup><mo>+</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>7</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>0</mn></msup></math></p><p>So, sum of coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><msup><mi>x</mi><mn>3</mn></msup><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msup><mi>x</mi><mn>7</mn></msup></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>8</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>7</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>2</mn></msup><mo>=</mo><msup><mn>3</mn><mn>9</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>9</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>8</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>1</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>0</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>8</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>7</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>2</mn></msup><mo>=</mo><msup><mn>3</mn><mn>9</mn></msup><mo>-</mo><msup><mn>2</mn><mn>9</mn></msup><mo>-</mo><mn>18</mn><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>8</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>7</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>7</mn><none/><mprescripts/><none/><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>2</mn></msup><mo>=</mo><mn>19683</mn><mo>-</mo><mn>512</mn><mo>-</mo><mn>19</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>8</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>7</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mn>2</mn><mn>2</mn></msup><mo>=</mo><mn>19152</mn></math></p><p>Now mean is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19152</mn><mn>7</mn></mfrac><mo>=</mo><mn>2736</mn></math></p></blockquote>

</details>

---

### Q19. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>The value of</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>!</mo><mn>50</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>!</mo><mn>48</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>!</mo><mn>46</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><mrow><mn>49</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>51</mn><mo>!</mo><mn>1</mn><mo>!</mo></mrow></mfrac></math> is </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>2</mn><mn>50</mn></msup><mrow><mn>50</mn><mo>!</mo></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>2</mn><mn>50</mn></msup><mrow><mn>51</mn><mo>!</mo></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>2</mn><mn>51</mn></msup><mrow><mn>51</mn><mo>!</mo></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>2</mn><mn>51</mn></msup><mrow><mn>50</mn><mo>!</mo></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>2</mn><mn>50</mn></msup><mrow><mn>51</mn><mo>!</mo></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>!</mo><mo>&#183;</mo><mn>50</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>3</mn><mo>!</mo><mo>&#183;</mo><mn>48</mn><mo>!</mo></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>5</mn><mo>!</mo><mo>&#183;</mo><mn>46</mn><mo>!</mo></mstyle></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>51</mn><mo>!</mo><mo>&#183;</mo><mn>1</mn><mo>!</mo></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>51</mn><mo>!</mo></mrow></mfrac><mfenced close="]" open="["><mrow><mfrac><mrow><mn>51</mn><mo>!</mo></mrow><mrow><mn>1</mn><mo>!</mo><mo>&#183;</mo><mn>50</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>51</mn><mo>!</mo></mstyle><mstyle displaystyle="true"><mn>3</mn><mo>!</mo><mo>&#183;</mo><mn>48</mn><mo>!</mo></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>51</mn><mo>!</mo></mstyle><mstyle displaystyle="true"><mn>5</mn><mo>!</mo><mo>&#183;</mo><mn>46</mn><mo>!</mo></mstyle></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>51</mn><mo>!</mo></mstyle><mstyle displaystyle="true"><mn>51</mn><mo>!</mo><mo>&#183;</mo><mn>0</mn><mo>!</mo></mstyle></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>51</mn><mo>!</mo></mrow></mfrac><mfenced close="]" open="["><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>51</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><msup><mn>2</mn><mrow><mn>51</mn><mo>-</mo><mn>1</mn></mrow></msup><mrow><mn>51</mn><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><msup><mn>2</mn><mn>50</mn></msup><mrow><mn>51</mn><mo>!</mo></mrow></mfrac></math></p>

</details>

---

### Q20. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> be the sum of the coefficients of the odd powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>99</mn></msup></math>. Let a be the middle term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mn>200</mn></msup></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mmultiscripts><mi>C</mi><mn>99</mn><none/><mprescripts/><none/><mn>200</mn></mmultiscripts><mi>K</mi></mrow><mi>a</mi></mfrac><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mi>l</mi></msup><mi>m</mi></mrow><mi>n</mi></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> are odd numbers, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>l</mi><mo>,</mo><mi mathvariant="normal">n</mi></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>50</mn><mo>,</mo><mn>51</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>51</mn><mo>,</mo><mn>99</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>50</mn><mo>,</mo><mn>101</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>51</mn><mo>,</mo><mn>101</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>50</mn><mo>,</mo><mn>101</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>In the binomial expansion of
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>99</mn></msup></math>, the sum of odd coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><msub><mi>C</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msub><mi>C</mi><mn>99</mn></msub><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mn>99</mn></msup><mo>-</mo><mn>0</mn></mrow><mn>2</mn></mfrac><mo>=</mo><msup><mn>2</mn><mn>98</mn></msup></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo></math>Middle term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mn>200</mn></msup></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mfrac><mn>200</mn><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msub><mi>T</mi><mrow><mn>100</mn><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>100</mn><none></none><mprescripts></mprescripts><none></none><mn>200</mn></mmultiscripts><msup><mfenced><mn>2</mn></mfenced><mn>100</mn></msup><msup><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mn>100</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mn>100</mn><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>100</mn><none></none><mprescripts></mprescripts><none></none><mn>200</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mn>50</mn></msup></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mmultiscripts><mi>C</mi><mn>99</mn><none></none><mprescripts></mprescripts><none></none><mn>200</mn></mmultiscripts><mi>K</mi></mrow><mi>a</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>99</mn><none></none><mprescripts></mprescripts><none></none><mn>200</mn></mmultiscripts><mo>&#215;</mo><msup><mn>2</mn><mn>98</mn></msup></mrow><mrow><mmultiscripts><mi>C</mi><mn>100</mn><none></none><mprescripts></mprescripts><none></none><mn>200</mn></mmultiscripts><mo>&#215;</mo><msup><mn>2</mn><mn>50</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>100</mn><mn>101</mn></mfrac><mo>&#215;</mo><msup><mn>2</mn><mn>48</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>25</mn><mn>101</mn></mfrac><mo>&#215;</mo><msup><mn>2</mn><mn>50</mn></msup><mo>=</mo><mfenced><mfrac><mi>m</mi><mi>n</mi></mfrac></mfenced><msup><mn>2</mn><mi>l</mi></msup></math></p><p>On comparing, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>50</mn><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>=</mo><mn>25</mn><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>101</mn></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>l</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mn>50</mn><mo>,</mo><mn>101</mn></mrow></mfenced></math>. </p>

</details>

---

### Q21. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mn>6</mn></munderover><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mrow><mn>51</mn><mo>-</mo><mi>k</mi></mrow></mmultiscripts></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>51</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>45</mn></mmultiscripts></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>51</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>45</mn></mmultiscripts></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>52</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>45</mn></mmultiscripts></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>52</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>45</mn></mmultiscripts></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>52</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>45</mn></mmultiscripts></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>6</mn></munderover><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>51</mn><mo>-</mo><mi>k</mi></mrow></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>48</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>47</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>46</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>45</mn></mmultiscripts></math></p><p>Now we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math></p><p>Now using the above formula in given expression we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>6</mn></munderover><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>51</mn><mo>-</mo><mi>k</mi></mrow></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>48</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>47</mn></mmultiscripts><mo>+</mo><munder><munder><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>46</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>46</mn></mmultiscripts></mrow><mo>&#9183;</mo></munder><mrow></mrow></munder><mo>-</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>45</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>6</mn></munderover><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>51</mn><mo>-</mo><mi>k</mi></mrow></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>48</mn></mmultiscripts><mo>+</mo><munder><munder><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>47</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>47</mn></mmultiscripts></mrow><mo>&#9183;</mo></munder><mrow></mrow></munder><mo>-</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>45</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>6</mn></munderover><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>51</mn><mo>-</mo><mi>k</mi></mrow></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>48</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>48</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>45</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>6</mn></munderover><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>51</mn><mo>-</mo><mi>k</mi></mrow></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>45</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>6</mn></munderover><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>51</mn><mo>-</mo><mi>k</mi></mrow></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>45</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>6</mn></munderover><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>51</mn><mo>-</mo><mi>k</mi></mrow></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>45</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>6</mn></munderover><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>51</mn><mo>-</mo><mi>k</mi></mrow></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>52</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>45</mn></mmultiscripts></math>.</p>

</details>

---

### Q22. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>r</mi></msub></math> is the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup></math> in the Binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>10</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>r</mi><mn>3</mn></msup><msup><mfenced><mfrac><msub><mi>a</mi><mi>r</mi></msub><msub><mi>a</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub></mfrac></mfenced><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4895</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1210</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5445</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3025</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1210</mn></math>**

**Detailed Solution:**

<p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>r</mi></msub></math> is the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup></math> in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>10</mn></msup></math>, therefore</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>r</mi></msub><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>a</mi><mi>r</mi></msub><msub><mi>a</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub></mfrac><mo>=</mo><mfrac><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>a</mi><mi>r</mi></msub><msub><mi>a</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub></mfrac><mo>=</mo><mfrac><mrow><mn>10</mn><mo>!</mo></mrow><mrow><mi>r</mi><mo>!</mo><mo>&#215;</mo><mfenced><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mfenced><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>&#215;</mo><mfenced><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></mfenced><mo>!</mo></mrow><mrow><mn>10</mn><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>a</mi><mi>r</mi></msub><msub><mi>a</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub></mfrac><mo>=</mo><mfrac><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow><mi>r</mi></mfrac></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>r</mi><mn>3</mn></msup><msup><mfenced><mfrac><msub><mi>a</mi><mi>r</mi></msub><msub><mi>a</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>r</mi><mn>3</mn></msup><msup><mfenced><mfrac><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow><mi>r</mi></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>r</mi><mn>3</mn></msup><msup><mfenced><mfrac><msub><mi>a</mi><mi>r</mi></msub><msub><mi>a</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>r</mi><msup><mfenced><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>r</mi><mn>3</mn></msup><msup><mfenced><mfrac><msub><mi>a</mi><mi>r</mi></msub><msub><mi>a</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>r</mi><mfenced><mrow><mn>121</mn><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mn>22</mn><mi>r</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>r</mi><mn>3</mn></msup><msup><mfenced><mfrac><msub><mi>a</mi><mi>r</mi></msub><msub><mi>a</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><mn>121</mn><mi>r</mi><mo>+</mo><msup><mi>r</mi><mn>3</mn></msup><mo>-</mo><mn>22</mn><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>r</mi><mn>3</mn></msup><msup><mfenced><mfrac><msub><mi>a</mi><mi>r</mi></msub><msub><mi>a</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>121</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>11</mn></mrow><mn>2</mn></mfrac><mo>+</mo><msup><mfenced><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>11</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mfrac><mrow><mn>22</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>11</mn><mo>&#215;</mo><mn>21</mn></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>r</mi><mn>3</mn></msup><msup><mfenced><mfrac><msub><mi>a</mi><mi>r</mi></msub><msub><mi>a</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>6655</mn><mo>+</mo><mn>3025</mn><mo>-</mo><mn>8470</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>r</mi><mn>3</mn></msup><msup><mfenced><mfrac><msub><mi>a</mi><mi>r</mi></msub><msub><mi>a</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>1210</mn></math></p>

</details>

---

### Q23. JEE Main 2023 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>2023</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><mo>=</mo><mn>2023</mn><mo>&#215;</mo><mi>&#945;</mi><mo>&#215;</mo><msup><mn>2</mn><mn>2022</mn></msup></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1012**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>2023</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><mo>=</mo><mn>2023</mn><mo>&#215;</mo><mi>&#945;</mi><mo>&#215;</mo><msup><mn>2</mn><mn>2022</mn></msup></math></p><p>Now taking L.H.S we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>2023</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>2023</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mfrac><mn>2023</mn><mi>r</mi></mfrac><mo>&#183;</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>2022</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>2023</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>2023</mn></munderover><mi>r</mi><mo>&#183;</mo><mn>2023</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>2022</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>2023</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><mo>=</mo><mn>2023</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>2023</mn></munderover><mfenced><mrow><mi>r</mi><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#183;</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>2022</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>2023</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><mo>=</mo><mn>2023</mn><mfenced close="]" open="["><mrow><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>2023</mn></munderover><mfenced><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#183;</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>2022</mn></mmultiscripts><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>2023</mn></munderover><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>2022</mn></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>2023</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><mo>=</mo><mn>2023</mn><mfenced close="]" open="["><mrow><mn>2022</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>2</mn></mrow><mn>2023</mn></munderover><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>2</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>2021</mn></mmultiscripts><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>2023</mn></munderover><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>2022</mn></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>2023</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><mo>=</mo><mn>2023</mn><mfenced close="]" open="["><mrow><mn>2022</mn><mo>&#215;</mo><msup><mn>2</mn><mn>2021</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2022</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>2023</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><mo>=</mo><mn>2023</mn><mo>&#215;</mo><msup><mn>2</mn><mn>2022</mn></msup><mfenced close="]" open="["><mrow><mn>1011</mn><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>2023</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><mo>=</mo><mn>2023</mn><mo>&#215;</mo><mn>1012</mn><mo>&#215;</mo><msup><mn>2</mn><mn>2022</mn></msup></math></p><p>Now on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>2023</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><mo>=</mo><mn>2023</mn><mo>&#215;</mo><mi>&#945;</mi><mo>&#215;</mo><msup><mn>2</mn><mn>2022</mn></msup></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1012</mn></math></p>

</details>

---

### Q24. JEE Main 2022 (28 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts></mrow></mfenced><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>50</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts></mrow></mfenced></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>n</mi></msup><mo>.</mo><mi>m</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is odd, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>+</mo><mi>m</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **99**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts></mrow></mfenced><mfenced><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>50</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts></mrow></mfenced></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>49</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts><mo>=</mo><msup><mn>2</mn><mn>49</mn></msup></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>50</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>=</mo><msup><mn>2</mn><mn>49</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>50</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mo>=</mo><msup><mn>2</mn><mn>49</mn></msup><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfenced><mrow><msup><mn>2</mn><mn>49</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mn>2</mn><mn>49</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>98</mn></msup></math></p><p>Now comparing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msup><mn>2</mn><mi>n</mi></msup><mi>m</mi></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>98</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>99</mn></math></p></blockquote>

</details>

---

### Q25. JEE Main 2022 (27 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

If the sum of the coefficients of all the positive powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mi>n</mi></msup><mo>+</mo><mfrac><mn>2</mn><msup><mi>x</mi><mn>5</mn></msup></mfrac></mrow></mfenced><mn>7</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>939</mn></math>, then the sum of all the possible integral values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **57**

**Detailed Solution:**

<p>Plotting the table for coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mi>n</mi></msup><mo>+</mo><mfrac><mn>2</mn><msup><mi>x</mi><mn>5</mn></msup></mfrac></mrow></mfenced><mn>7</mn></msup></math> and there cumulative sum :</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td>Coefficient</td>			<td>Commulative sum</td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mn>7</mn><mi>n</mi></mrow></msup><mo>&#8594;</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mn>6</mn><mi>n</mi><mo>-</mo><mn>5</mn></mrow></msup><mo>&#8594;</mo><mn>2</mn><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>14</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mn>5</mn><mi>n</mi><mo>-</mo><mn>10</mn></mrow></msup><mo>&#8594;</mo><msup><mn>2</mn><mn>2</mn></msup><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>14</mn><mo>+</mo><mn>84</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mn>4</mn><mi>n</mi><mo>-</mo><mn>15</mn></mrow></msup><mo>&#8594;</mo><msup><mn>2</mn><mn>3</mn></msup><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>14</mn><mo>+</mo><mn>84</mn><mo>+</mo><mn>280</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mn>3</mn><mi>n</mi><mo>-</mo><mn>20</mn></mrow></msup><mo>&#8594;</mo><msup><mn>2</mn><mn>4</mn></msup><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>84</mn><mo>+</mo><mn>280</mn><mo>+</mo><mn>560</mn><mo>=</mo><mn>939</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>25</mn></mrow></msup><mo>&#8594;</mo><msup><mn>2</mn><mn>5</mn></msup><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts></math></td>			<td> </td>		</tr>	</tbody></table><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>n</mi><mo>-</mo><mn>20</mn><mo>&#8805;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8745;</mo><mo>&#160;</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>25</mn><mo>&#60;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8745;</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>7</mn><mo>&#8804;</mo><mi mathvariant="normal">n</mi><mo>&#8804;</mo><mn>12</mn></math></p><p>Sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>10</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>12</mn><mo>=</mo><mn>57</mn></math></p>

</details>

---

### Q26. JEE Main 2022 (26 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>40</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>41</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>42</mn></mmultiscripts><mo>+</mo><mo>&#8943;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>20</mn><none/><mprescripts/><none/><mn>60</mn></mmultiscripts><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>20</mn><none/><mprescripts/><none/><mn>60</mn></mmultiscripts></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> are co-prime, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **102**

**Detailed Solution:**

<p>We know <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>40</mn></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>41</mn></mmultiscripts></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>41</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>41</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>42</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>20</mn><none></none><mprescripts></mprescripts><none></none><mn>60</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>42</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>42</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>43</mn></mmultiscripts><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>20</mn><none></none><mprescripts></mprescripts><none></none><mn>60</mn></mmultiscripts></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>43</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>43</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mmultiscripts><mi>C</mi><mn>20</mn><none></none><mprescripts></mprescripts><none></none><mn>60</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>19</mn><none></none><mprescripts></mprescripts><none></none><mn>60</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>20</mn><none></none><mprescripts></mprescripts><none></none><mn>60</mn></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>20</mn><none></none><mprescripts></mprescripts><none></none><mn>61</mn></mmultiscripts></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>20</mn><none/><mprescripts/><none/><mn>61</mn></mmultiscripts><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac><mmultiscripts><mi>C</mi><mn>20</mn><none/><mprescripts/><none/><mn>60</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>41</mn><none/><mprescripts/><none/><mn>61</mn></mmultiscripts><mo>=</mo><mfrac><mn>61</mn><mn>41</mn></mfrac><mmultiscripts><mi>C</mi><mn>40</mn><none/><mprescripts/><none/><mn>60</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>61</mn><mn>41</mn></mfrac><mmultiscripts><mi>C</mi><mn>20</mn><none/><mprescripts/><none/><mn>60</mn></mmultiscripts><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac><mmultiscripts><mi>C</mi><mn>20</mn><none/><mprescripts/><none/><mn>60</mn></mmultiscripts></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>61</mn><mn>41</mn></mfrac><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac><mo>&#160;</mo><mo>&#8658;</mo><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>102</mn></math></p>

</details>

---

### Q27. JEE Main 2022 (25 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

If the sum of the co-efficients of all the positive even powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>3</mn><mi>x</mi></mfrac></mrow></mfenced><mn>10</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mn>10</mn></msup><mo>-</mo><mi>&#946;</mi><mo>&#183;</mo><msup><mn>3</mn><mn>9</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **83**

**Detailed Solution:**

<p>Given,</p><p>Binomial expression <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>3</mn><mi>x</mi></mfrac></mrow></mfenced><mn>10</mn></msup></math>, so its <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mn>3</mn><mi>x</mi></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><msup><mn>2</mn><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mn>3</mn><mi>r</mi></msup><msup><mi>x</mi><mrow><mn>30</mn><mo>-</mo><mn>4</mn><mi>r</mi></mrow></msup></math></p><p>Now putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>7</mn></math> and adding all term we get </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>3</mn><mi>x</mi></mfrac></mrow></mfenced><mn>10</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mn>2</mn><mn>10</mn></msup><msup><mn>3</mn><mn>0</mn></msup><msup><mi>x</mi><mn>30</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mn>2</mn><mn>9</mn></msup><msup><mn>3</mn><mn>1</mn></msup><msup><mi>x</mi><mn>26</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>7</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mn>2</mn><mn>3</mn></msup><msup><mn>3</mn><mn>7</mn></msup><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>8</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mn>2</mn><mn>2</mn></msup><msup><mn>3</mn><mn>8</mn></msup><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>3</mn><mi>x</mi></mfrac></mrow></mfenced><mn>10</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>8</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mn>2</mn><mn>2</mn></msup><msup><mn>3</mn><mn>8</mn></msup><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mn>2</mn><mn>10</mn></msup><msup><mn>3</mn><mn>0</mn></msup><msup><mi>x</mi><mn>30</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mn>2</mn><mn>9</mn></msup><msup><mn>3</mn><mn>1</mn></msup><msup><mi>x</mi><mn>26</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>7</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mn>2</mn><mn>3</mn></msup><msup><mn>3</mn><mn>7</mn></msup><msup><mi>x</mi><mn>2</mn></msup></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mn>10</mn></msup><mo>-</mo><msup><mn>3</mn><mn>9</mn></msup><mfenced><mrow><mn>60</mn><mo>+</mo><mn>20</mn><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mn>2</mn><mn>10</mn></msup><msup><mn>3</mn><mn>0</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mn>2</mn><mn>9</mn></msup><msup><mn>3</mn><mn>1</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>7</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mn>2</mn><mn>3</mn></msup><msup><mn>3</mn><mn>7</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mn>10</mn></msup><mo>-</mo><msup><mn>3</mn><mn>9</mn></msup><mfenced><mn>83</mn></mfenced><mo>=</mo><mtext>sum&#160;of&#160;even&#160;coefficients</mtext></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>83</mn></math></p>

</details>

---

### Q28. JEE Main 2022 (25 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mi>r</mi></msub></math> denote the binomial coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mi>r</mi></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>10</mn></msup></math>. If for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi mathvariant="bold-italic">R</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><mo>&#183;</mo><mn>2</mn><msub><mi>C</mi><mn>2</mn></msub><mo>+</mo><mn>5</mn><mo>&#183;</mo><mn>3</mn><msub><mi>C</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo></math> upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> terms <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>&#945;</mi><mo>&#215;</mo><msup><mn>2</mn><mn>11</mn></msup></mrow><mrow><msup><mn>2</mn><mi>&#946;</mi></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>0</mn></msub><mo>+</mo><mfrac><msub><mi>C</mi><mn>1</mn></msub><mn>2</mn></mfrac><mo>+</mo><mfrac><msub><mi>C</mi><mn>2</mn></msub><mn>3</mn></mfrac><mo>+</mo><mo>&#8230;</mo></math> upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> terms) then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **286**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>10</mn></msup><mo>=</mo><msub><mi>C</mi><mn>0</mn></msub><mo>+</mo><msub><mi>C</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><msub><mi>C</mi><mn>2</mn></msub><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>C</mi><mn>10</mn></msub><msup><mi>x</mi><mn>10</mn></msup></math></p><p>Differentiating, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>9</mn></msup><mo>=</mo><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>C</mi><mn>2</mn></msub><mi>x</mi><mo>+</mo><mn>3</mn><msub><mi>C</mi><mn>3</mn></msub><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>10</mn><msub><mi>C</mi><mn>10</mn></msub><msup><mi>x</mi><mn>9</mn></msup></math></p><p>Now replacing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>9</mn></msup><mo>=</mo><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>C</mi><mn>2</mn></msub><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msub><mi>C</mi><mn>3</mn></msub><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mn>10</mn><msub><mi>C</mi><mn>10</mn></msub><msup><mi>x</mi><mn>18</mn></msup></math></p><p>Multiplying by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> on both the sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#183;</mo><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>9</mn></msup><mo>=</mo><msub><mi>C</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><mn>2</mn><msub><mi>C</mi><mn>2</mn></msub><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><msub><mi>C</mi><mn>3</mn></msub><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>10</mn><msub><mi>C</mi><mn>10</mn></msub><msup><mi>x</mi><mn>19</mn></msup></math></p><p>Differentiating again, we get </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mfenced><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>9</mn></msup><mo>&#183;</mo><mn>1</mn><mo>+</mo><mn>9</mn><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>8</mn></msup><mn>2</mn><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>C</mi><mn>2</mn></msub><mo>&#183;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>&#183;</mo><mn>5</mn><mo>&#183;</mo><msub><mi>C</mi><mn>3</mn></msub><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>10</mn><mo>&#183;</mo><mn>19</mn><msub><mi>C</mi><mn>10</mn></msub><msup><mi>x</mi><mn>18</mn></msup></math></p><p>putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mfenced><mrow><msup><mn>2</mn><mn>9</mn></msup><mo>+</mo><mn>18</mn><mo>&#183;</mo><msup><mn>2</mn><mn>8</mn></msup></mrow></mfenced><mo>=</mo><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><mo>&#183;</mo><mn>2</mn><mo>&#183;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>+</mo><mn>5</mn><mo>&#183;</mo><mn>3</mn><mo>&#183;</mo><msub><mi>C</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mn>19</mn><mo>&#183;</mo><mn>10</mn><mo>&#183;</mo><msub><mi>C</mi><mn>10</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><mo>&#183;</mo><mn>2</mn><mo>&#183;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mn>19</mn><mo>&#183;</mo><mn>10</mn><mo>&#183;</mo><msub><mi>C</mi><mn>10</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mo>&#183;</mo><msup><mn>2</mn><mn>9</mn></msup><mo>&#183;</mo><mn>10</mn><mo>=</mo><mn>100</mn><mo>&#183;</mo><msup><mn>2</mn><mn>9</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>10</mn></msup><mo>=</mo><msub><mi>C</mi><mn>0</mn></msub><mo>+</mo><msub><mi>C</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><msub><mi>C</mi><mn>2</mn></msub><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>C</mi><mn>10</mn></msub><msup><mi>x</mi><mn>10</mn></msup></math></p><p>Integrating, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mfenced open="[" close="]"><mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>11</mn></msup><mn>11</mn></mfrac></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>=</mo><msubsup><mfenced open="[" close="]"><mrow><msub><mi>C</mi><mn>0</mn></msub><mi>x</mi><mo>+</mo><msub><mi>C</mi><mn>1</mn></msub><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><msub><mi>C</mi><mn>2</mn></msub><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mrow><msub><mi>C</mi><mn>10</mn></msub><msup><mi>x</mi><mn>11</mn></msup></mrow><mn>11</mn></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>0</mn></msub><mo>+</mo><mfrac><msub><mi>C</mi><mn>1</mn></msub><mn>2</mn></mfrac><mo>+</mo><mfrac><msub><mi>C</mi><mn>2</mn></msub><mn>3</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><msub><mi>C</mi><mn>9</mn></msub><mn>10</mn></mfrac><mo>+</mo><mfrac><msub><mi>C</mi><mn>10</mn></msub><mn>11</mn></mfrac><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mn>11</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>11</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>0</mn></msub><mo>+</mo><mfrac><msub><mi>C</mi><mn>1</mn></msub><mn>2</mn></mfrac><mo>+</mo><mfrac><msub><mi>C</mi><mn>2</mn></msub><mn>3</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><msub><mi>C</mi><mn>9</mn></msub><mn>10</mn></mfrac><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mn>11</mn></msup><mo>-</mo><mn>2</mn></mrow><mn>11</mn></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#183;</mo><msup><mn>2</mn><mn>9</mn></msup><mo>=</mo><mfrac><mrow><mi>&#945;</mi><mo>&#183;</mo><msup><mn>2</mn><mn>11</mn></msup></mrow><mrow><msup><mn>2</mn><mi>&#946;</mi></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mfenced><mfrac><mrow><msup><mn>2</mn><mn>11</mn></msup><mo>-</mo><mn>2</mn></mrow><mn>11</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>275</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>11</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>286</mn></math></p>

</details>

---

### Q29. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mi mathvariant="normal">r</mi><none></none><mprescripts></mprescripts><none></none><mn>20</mn></mmultiscripts></math> is the co-efficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mi mathvariant="normal">r</mi></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mn>20</mn></msup></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">r</mi><mo>=</mo><mn>0</mn></mrow><mn>20</mn></munderover><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup><mfenced><mmultiscripts><mi mathvariant="normal">C</mi><mi mathvariant="normal">r</mi><none/><mprescripts/><none/><mn>20</mn></mmultiscripts></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>420</mn><mo>&#215;</mo><msup><mn>2</mn><mn>18</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>380</mn><mo>&#215;</mo><msup><mn>2</mn><mn>18</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>380</mn><mo>&#215;</mo><mn>219</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>420</mn><mo>&#215;</mo><msup><mn>2</mn><mn>19</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>420</mn><mo>&#215;</mo><msup><mn>2</mn><mn>18</mn></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>20</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mfenced><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>20</mn></mmultiscripts></mfenced><mo>=</mo><mo>&#8721;</mo><mi>r</mi><mfenced><mrow><mi>r</mi><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>20</mn></mmultiscripts></mrow></mfenced><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mi>r</mi><mo>&#183;</mo><mn>20</mn><mo>.</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>19</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>20</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mo>(</mo><mi>r</mi><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn><mrow><mo>)</mo><msup><mo>&#183;</mo><mn>19</mn></msup></mrow><msub><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>20</mn><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mo>(</mo><mi>r</mi><mo>-</mo><mn>1</mn><mo>)</mo><msup><mo>&#183;</mo><mn>19</mn></msup><msub><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mn>19</mn></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>20</mn><mfenced><mrow><mn>19</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>2</mn></mrow><mn>20</mn></munderover><mmultiscripts><mi mathvariant="normal">C</mi><mrow><mi mathvariant="normal">r</mi><mo>-</mo><mn>2</mn></mrow><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mmultiscripts><mi mathvariant="normal">C</mi><mrow><mi mathvariant="normal">r</mi><mo>-</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mn>19</mn></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>380</mn><mo>)</mo><msup><mn>2</mn><mn>18</mn></msup><mo>+</mo><mn>20</mn><mo>&#183;</mo><msup><mn>2</mn><mn>19</mn></msup><mo>&#8658;</mo><msup><mn>2</mn><mn>20</mn></msup><mo>&#183;</mo><mo>(</mo><mn>95</mn><mo>+</mo><mn>10</mn><mo>)</mo><mo>=</mo><mo>(</mo><mn>105</mn><mo>)</mo><msup><mn>2</mn><mn>20</mn></msup><mo>=</mo><mn>420</mn><mo>&#215;</mo><msup><mn>2</mn><mn>18</mn></msup></math></p>

</details>

---

### Q30. JEE Main 2021 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi mathvariant="bold-italic">N</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denote the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>.</mo></math> If the sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math> terms of <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>,</mo><mn>3</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>,</mo><mn>5</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>,</mo><mn>7</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>,</mo><mo>&#8230;</mo></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>100</mn></msup><mo>&#183;</mo><mn>101</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced close="]" open="["><mfrac><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **98**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mn>3</mn><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mn>5</mn><mo>.</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>r</mi></msub><mo>=</mo><msup><mfenced><mrow><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><msub><mi>C</mi><mi>r</mi></msub></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mi>&#931;</mi><msub><mi>T</mi><mi>r</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mi>&#931;</mi><msup><mfenced><mrow><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><msub><mi>C</mi><mi>r</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#931;</mi><mn>2</mn><mi>r</mi><mfenced><mrow><msup><mrow/><mi>n</mi></msup><msub><mi>C</mi><mi>r</mi></msub></mrow></mfenced><mo>+</mo><mi>&#931;</mi><mfenced><mrow><msup><mrow/><mi>n</mi></msup><msub><mi>C</mi><mi>r</mi></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mn>2</mn><mfenced><mrow><mi>n</mi><mo>&#183;</mo><msup><mn>2</mn><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mo>+</mo><msup><mn>2</mn><mi>n</mi></msup><mo>=</mo><msup><mn>2</mn><mi>n</mi></msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mi>n</mi></msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mn>100</mn></msup><mo>.</mo><mn>101</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>100</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced close="]" open="["><mfrac><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mfrac><mn>99</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>98</mn><mo>.</mo></math></p>

</details>

---

### Q31. JEE Main 2021 (18 Mar Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math> denote the binomial coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mi>r</mi></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mi>n</mi></msup></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mn>10</mn></munderover><mfenced><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>k</mi></mrow></mfenced><mmultiscripts><mi>C</mi><mi>k</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mi>&#945;</mi><mo>.</mo><msup><mn>3</mn><mn>10</mn></msup><mo>+</mo><mi>&#946;</mi><mo>&#183;</mo><msup><mn>2</mn><mn>10</mn></msup><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>&#8712;</mo><mi>R</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to ___ .</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **19**

**Detailed Solution:**

<p>Instead of <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>k</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts></math> it must be <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>k</mi><none/><mprescripts/><none/><mn>10</mn></mmultiscripts></math> i.e.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mn>10</mn></munderover><mfenced><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>k</mi></mrow></mfenced><mmultiscripts><mi>C</mi><mi>k</mi><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><mo>=</mo><mi>&#945;</mi><mo>&#183;</mo><msup><mn>3</mn><mn>10</mn></msup><mo>+</mo><mi>&#946;</mi><mo>&#183;</mo><msup><mn>2</mn><mn>10</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mi>H</mi><mi>S</mi><mo>=</mo><mn>4</mn><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mn>10</mn></munderover><mmultiscripts><mi>C</mi><mi>k</mi><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><mo>+</mo><mn>3</mn><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mn>10</mn></munderover><mi>k</mi><mo>&#183;</mo><mfrac><mn>10</mn><mi>k</mi></mfrac><mo>&#183;</mo><mmultiscripts><mi>C</mi><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mn>9</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>.</mo><msup><mn>2</mn><mn>10</mn></msup><mo>+</mo><mn>3</mn><mo>.</mo><mn>10</mn><mo>.</mo><msup><mn>2</mn><mn>9</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>19</mn><mo>.</mo><msup><mn>2</mn><mn>10</mn></msup><mo>=</mo><mi>&#945;</mi><mo>.</mo><msup><mn>3</mn><mn>10</mn></msup><mo>+</mo><mi>&#946;</mi><mo>.</mo><msup><mn>2</mn><mn>10</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mn>19</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>19</mn></math></p>

</details>

---

### Q32. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>20</mn></msup><mo>=</mo><msub><mi>a</mi><mn>0</mn></msub><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mn>40</mn></msub><msup><mi>x</mi><mn>40</mn></msup><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><msub><mi>a</mi><mn>5</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mn>37</mn></msub></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>20</mn></msup><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>21</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>19</mn></msup><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>21</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>19</mn></msup><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>+</mo><mn>21</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>20</mn></msup><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>+</mo><mn>21</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>19</mn></msup><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>21</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>20</mn></msup><mo>=</mo><msub><mi>a</mi><mn>0</mn></msub><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mn>40</mn></msub><msup><mi>x</mi><mn>40</mn></msup></math> </p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>0</mn></msub><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mn>40</mn></msub><mo>=</mo><msup><mn>4</mn><mn>20</mn></msup></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>0</mn></msub><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mn>40</mn></msub><mo>=</mo><msup><mn>2</mn><mn>20</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mn>39</mn></msub><mo>=</mo><mfrac><mrow><msup><mn>4</mn><mn>20</mn></msup><mo>-</mo><msup><mn>2</mn><mn>20</mn></msup></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mn>37</mn></msub><mo>=</mo><msup><mn>2</mn><mn>39</mn></msup><mo>-</mo><msup><mn>2</mn><mn>19</mn></msup><mo>-</mo><msub><mi>a</mi><mn>39</mn></msub></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>39</mn></msub><mo>=</mo><mfrac><mrow><mn>20</mn><mo>!</mo><mo>(</mo><mn>2</mn><msup><mo>)</mo><mn>19</mn></msup><mo>&#215;</mo><mn>1</mn></mrow><mrow><mn>19</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>20</mn><mo>&#215;</mo><msup><mn>2</mn><mn>19</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mn>37</mn></msub><mo>=</mo><msup><mn>2</mn><mn>19</mn></msup><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>1</mn><mo>-</mo><mn>20</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>19</mn></msup><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>21</mn></mrow></mfenced></math></p>

</details>

---

### Q33. JEE Main 2021 (16 Mar Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> be a positive integer. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mi>n</mi></munderover><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>k</mi></msup><mo>&#215;</mo><mmultiscripts><mi>C</mi><mi>k</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mfenced close="]" open="["><mrow><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>k</mi></msup><mo>+</mo><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mi>k</mi></msup><mo>+</mo><msup><mfenced><mfrac><mn>7</mn><mn>8</mn></mfrac></mfenced><mi>k</mi></msup><mo>+</mo><msup><mfenced><mfrac><mn>15</mn><mn>16</mn></mfrac></mfenced><mi>k</mi></msup><mo>+</mo><msup><mfenced><mfrac><mn>31</mn><mn>32</mn></mfrac></mfenced><mi>k</mi></msup></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn><mi>A</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>30</mn></msup></mfrac><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to ______ .<gwmw style="display:none;"></gwmw>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mi>n</mi></munderover><mmultiscripts><mi>C</mi><mi>k</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mi>k</mi></msup><mo>+</mo><msup><mfenced><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac></mfenced><mi>k</mi></msup><mo>+</mo><msup><mfenced><mfrac><mrow><mo>-</mo><mn>7</mn></mrow><mn>8</mn></mfrac></mfenced><mi>k</mi></msup><mo>+</mo><msup><mfenced><mfrac><mrow><mo>-</mo><mn>15</mn></mrow><mn>16</mn></mfrac></mfenced><mi>k</mi></msup><mo>+</mo><msup><mfenced><mfrac><mrow><mo>-</mo><mn>31</mn></mrow><mn>32</mn></mfrac></mfenced><mi>k</mi></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mi>n</mi></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced><mi>n</mi></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>7</mn><mn>8</mn></mfrac></mrow></mfenced><mi>n</mi></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>15</mn><mn>16</mn></mfrac></mrow></mfenced><mi>n</mi></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>31</mn><mn>32</mn></mfrac></mrow></mfenced><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>4</mn><mi>n</mi></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>8</mn><mi>n</mi></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>16</mn><mi>n</mi></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>32</mn><mi>n</mi></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mfenced><mfrac><mn>1</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac></mfenced><mn>5</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac></mrow></mfrac></mfenced><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mrow><mn>5</mn><mi>n</mi></mrow></msup></mfrac></mrow></mfenced><mfenced><mrow><msup><mn>2</mn><mi>n</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mn>2</mn><mi>n</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>A</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mrow><mn>5</mn><mi>n</mi></mrow></msup></mfrac><mo>,</mo></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn><mi>A</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>30</mn></msup></mfrac></math></p><p>Clearly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>n</mi><mo>=</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q34. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denote greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. If for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>,</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mi>n</mi></msup><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>0</mn></mrow><mrow><mn>3</mn><mi>n</mi></mrow></munderover><msub><mi>a</mi><mi>j</mi></msub><msup><mi>x</mi><mi>j</mi></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>0</mn></mrow><mfenced open="[" close="]"><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><mn>2</mn></mfrac></mfenced></munderover><msub><mi>a</mi><mrow><mn>2</mn><mi>j</mi></mrow></msub><mo>+</mo><mn>4</mn><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>0</mn></mrow><mfenced open="[" close="]"><mfrac><mrow><mn>3</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced></munderover><msub><mi>a</mi><mrow><mn>2</mn><mi>j</mi><mo>+</mo><mn>1</mn></mrow></msub></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mi>n</mi></msup><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>0</mn></mrow><mrow><mn>3</mn><mi>n</mi></mrow></munderover><msub><mi>a</mi><mi>j</mi></msub><msup><mi>x</mi><mi>j</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mi>n</mi></msup><mo>=</mo><msub><mi>a</mi><mn>0</mn></msub><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><msup><mi>x</mi><mn>2</mn></msup><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mrow><mn>3</mn><mi>n</mi></mrow></msub><msup><mi>x</mi><mrow><mn>3</mn><mi>n</mi></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>0</mn></mrow><mfenced close="]" open="["><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><mn>2</mn></mfrac></mfenced></munderover><msub><mi>a</mi><mrow><mn>2</mn><mi>j</mi></mrow></msub><mo>=</mo><msub><mi>a</mi><mn>0</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub><mo>&#8230;</mo><mo>&#8230;</mo></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>0</mn></mrow><mfenced open="[" close="]"><mfrac><mrow><mn>3</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced></munderover><msub><mi>a</mi><mrow><mn>2</mn><mi>j</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><msub><mi>a</mi><mn>5</mn></msub><mo>&#8230;</mo><mo>&#8230;</mo></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, then we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>=</mo><msub><mi>a</mi><mn>0</mn></msub><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>a</mi><mrow><mn>3</mn><mi>n</mi></mrow></msub></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">A</mi><mo>)</mo></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, then we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>=</mo><msub><mi>a</mi><mn>0</mn></msub><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>-</mo><msub><mi>a</mi><mn>3</mn></msub><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mn>3</mn><mi>n</mi></mrow></msup><msub><mi>a</mi><mrow><mn>3</mn><mi>n</mi></mrow></msub></math>    <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">B</mi><mo>)</mo></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">A</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">B</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>0</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><msub><mi>a</mi><mn>5</mn></msub><mo>&#8230;</mo><mo>&#8230;</mo><mo>=</mo><mn>0</mn></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>0</mn></mrow><mfenced close="]" open="["><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><mn>2</mn></mfrac></mfenced></munderover><msub><mi>a</mi><mrow><mn>2</mn><mi>j</mi></mrow></msub><mo>+</mo><mn>4</mn><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>0</mn></mrow><mfenced close="]" open="["><mfrac><mrow><mn>3</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced></munderover><msub><mi>a</mi><mrow><mn>2</mn><mi>j</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q35. JEE Main 2021 (26 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>,</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>gcd</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mfenced><mtable><mtr><mtd><mn>30</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mn>29</mn><mfenced><mtable><mtr><mtd><mn>30</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>2</mn><mfenced><mtable><mtr><mtd><mn>30</mn></mtd></mtr><mtr><mtd><mn>28</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mn>1</mn><mfenced><mtable><mtr><mtd><mn>30</mn></mtd></mtr><mtr><mtd><mn>29</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>n</mi><mo>.</mo><msup><mn>2</mn><mi>m</mi></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>+</mo><mi>m</mi></math> is equal to _______. (Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtable columnalign="left"><mtr><mtd><mi>n</mi></mtd></mtr><mtr><mtd><mi>k</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mmultiscripts><mi>C</mi><mi>k</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math>)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **45**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mfenced><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts></mfenced><mo>+</mo><mn>29</mn><mfenced><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>2</mn><mfenced><mmultiscripts><mi>C</mi><mn>28</mn><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts></mfenced><mo>+</mo><mn>1</mn><mfenced><mmultiscripts><mi>C</mi><mn>29</mn><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts></mfenced></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>30</mn><mfenced><mmultiscripts><mi>C</mi><mn>30</mn><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts></mfenced><mo>+</mo><mn>29</mn><mfenced><mmultiscripts><mi>C</mi><mn>29</mn><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts></mfenced><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mn>2</mn><mfenced><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts></mfenced><mo>+</mo><mn>1</mn><mfenced><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>30</mn></munderover><mi>r</mi><mfenced><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>30</mn></munderover><mi>r</mi><mfenced><mfrac><mn>30</mn><mi>r</mi></mfrac></mfenced><mfenced><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>29</mn></mmultiscripts></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>30</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>30</mn></munderover><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>29</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>30</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>29</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>29</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>29</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>29</mn><none></none><mprescripts></mprescripts><none></none><mn>29</mn></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>30</mn><mfenced><msup><mn>2</mn><mn>29</mn></msup></mfenced><mo>=</mo><mn>15</mn><msup><mfenced><mn>2</mn></mfenced><mn>30</mn></msup><mo>=</mo><mi>n</mi><msup><mfenced><mn>2</mn></mfenced><mi>m</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>15</mn><mo>,</mo><mi>m</mi><mo>=</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>+</mo><mi>m</mi><mo>=</mo><mn>45</mn></math></p>

</details>

---

### Q36. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#10878;</mo><mn>2</mn></math> is a positive integer, then the sum of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>+</mo><mn>2</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>4</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mn>12</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>+</mo><mn>2</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>4</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>+</mo><mn>2</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>4</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts></mrow></mfenced></math></p><p>{use <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts></math>}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>+</mo><mn>2</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>4</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>4</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>+</mo><mn>2</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>+</mo><mn>2</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>+</mo><mn>2</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>n</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mo>&#183;</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mi>n</mi></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mo>.</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac></math></p>

</details>

---

### Q37. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><mo>+</mo><mn>2</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><mo>-</mo><mn>3</mn><msup><mo>&#183;</mo><mn>15</mn></msup><msub><mi>C</mi><mn>3</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mn>15</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>15</mn><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>14</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>14</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mn>14</mn></mmultiscripts><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>11</mn><none/><mprescripts/><none/><mn>14</mn></mmultiscripts></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>14</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>13</mn></msup><mo>-</mo><mn>13</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>16</mn></msup><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>13</mn></msup><mo>-</mo><mn>14</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>13</mn></msup><mo>-</mo><mn>14</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>+</mo><mn>2</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>-</mo><mn>3</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>-</mo><mn>15</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>15</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts></mrow></mfenced><mo>+</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>14</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>14</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>11</mn><none></none><mprescripts></mprescripts><none></none><mn>14</mn></mmultiscripts></mrow></mfenced></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup><mo>&#183;</mo><mi>r</mi><msup><mo>&#183;</mo><mn>15</mn></msup><msub><mi>C</mi><mi>r</mi></msub></mrow></mfenced><mo>+</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>14</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>14</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>11</mn><none/><mprescripts/><none/><mn>14</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>13</mn><none/><mprescripts/><none/><mn>14</mn></mmultiscripts></mrow></mfenced><mo>-</mo><mmultiscripts><mi>C</mi><mn>13</mn><none/><mprescripts/><none/><mn>14</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup><mo>&#183;</mo><mn>15</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mn>14</mn></mmultiscripts></mrow></mfenced><mo>+</mo><msup><mn>2</mn><mn>13</mn></msup><mo>-</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>15</mn><mfenced><mrow><mo>-</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>14</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>14</mn></mmultiscripts><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>14</mn><none></none><mprescripts></mprescripts><none></none><mn>14</mn></mmultiscripts></mrow></mfenced><mo>+</mo><msup><mn>2</mn><mn>13</mn></msup><mo>-</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>13</mn></msup><mo>-</mo><mn>14</mn></math></p>

</details>

---

### Q38. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>20</mn></munderover><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>50</mn><mo>-</mo><mi>r</mi></mrow></mmultiscripts></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>7</mn><none/><mprescripts/><none/><mn>50</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>7</mn><none/><mprescripts/><none/><mn>30</mn></mmultiscripts></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>6</mn><none/><mprescripts/><none/><mn>50</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>6</mn><none/><mprescripts/><none/><mn>30</mn></mmultiscripts></math> <math xmlns="http://www.w3.org/1998/Math/MathML"></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>7</mn><none/><mprescripts/><none/><mn>51</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>7</mn><none/><mprescripts/><none/><mn>30</mn></mmultiscripts></math> <math xmlns="http://www.w3.org/1998/Math/MathML"></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>20</mn></munderover><mmultiscripts><mi>C</mi><mn mathvariant="italic">6</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>50</mn><mo>-</mo><mi>r</mi></mrow></mmultiscripts><mo mathvariant="italic">=</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo mathvariant="italic">=</mo><mn mathvariant="italic">50</mn></msup><msub><mi>C</mi><mn mathvariant="italic">6</mn></msub><msup><mo>+</mo><mn mathvariant="italic">49</mn></msup><msub><mi>C</mi><mn mathvariant="italic">6</mn></msub><msup><mo>+</mo><mn mathvariant="italic">48</mn></msup><msub><mi>C</mi><mn mathvariant="italic">6</mn></msub><mo>+</mo><mo mathvariant="italic">.</mo><mo mathvariant="italic">..</mo><mo mathvariant="italic">.</mo><msup><mo>+</mo><mn mathvariant="italic">30</mn></msup><msub><mi>C</mi><mn mathvariant="italic">6</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mo>&#8722;</mo><mn>30</mn></msup><msub><mi mathvariant="normal">C</mi><mn>7</mn></msub><msup><mo>+</mo><mn>30</mn></msup><msub><mi mathvariant="normal">C</mi><mn>7</mn></msub><msup><mo>+</mo><mn>30</mn></msup><msub><mi mathvariant="normal">C</mi><mn>6</mn></msub><msup><mo>+</mo><mn>31</mn></msup><msub><mi mathvariant="normal">C</mi><mn>6</mn></msub><msup><mo>+</mo><mn>32</mn></msup><msub><mi mathvariant="normal">C</mi><mn>6</mn></msub><mo>+</mo><mo>.</mo><mo>...</mo><msup><mo>+</mo><mn>50</mn></msup><msub><mi mathvariant="normal">C</mi><mn>6</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">=</mo><msup><mo mathvariant="italic">&#8722;</mo><mn mathvariant="italic">30</mn></msup><msub><mi>C</mi><mn mathvariant="italic">7</mn></msub><msup><mo>+</mo><mn mathvariant="italic">31</mn></msup><msub><mi>C</mi><mn mathvariant="italic">7</mn></msub><msup><mo>+</mo><mn mathvariant="italic">31</mn></msup><msub><mi>C</mi><mn mathvariant="italic">6</mn></msub><msup><mo>+</mo><mn mathvariant="italic">32</mn></msup><msub><mi>C</mi><mn mathvariant="italic">6</mn></msub><mo>+</mo><mo mathvariant="italic">.</mo><mo mathvariant="italic">...</mo><msup><mo>+</mo><mn mathvariant="italic">50</mn></msup><msub><mi>C</mi><mn mathvariant="italic">6</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mo>&#8722;</mo><mn>30</mn></msup><msub><mi mathvariant="normal">C</mi><mn>7</mn></msub><msup><mo>+</mo><mn>32</mn></msup><msub><mi mathvariant="normal">C</mi><mn>7</mn></msub><msup><mo>+</mo><mn>32</mn></msup><msub><mi mathvariant="normal">C</mi><mn>6</mn></msub><mo>+</mo><mo>.</mo><mo>...</mo><msup><mo>+</mo><mn>50</mn></msup><msub><mi mathvariant="normal">C</mi><mn>6</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mo>&#8722;</mo><mn>30</mn></msup><msub><mi>C</mi><mn>7</mn></msub><msup><mo>+</mo><mn>51</mn></msup><msub><mi>C</mi><mn>7</mn></msub></math>.</p>

</details>

---

### Q39. JEE Main 2020 (09 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub><mo>&#8801;</mo><mmultiscripts><mrow><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub></mrow><mprescripts></mprescripts><mrow><mi></mi></mrow><mrow><mn>25</mn></mrow></mmultiscripts></math> and <math><msub><mrow><mi>C</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><mn>5</mn><mo>&#8729;</mo><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>9</mn><mo>&#8729;</mo><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfenced separators="|"><mrow><mn>101</mn></mrow></mfenced><mo>&#8729;</mo><msub><mrow><mi>C</mi></mrow><mrow><mn>25</mn></mrow></msub><mo>=</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>25</mn></mrow></msup><mo>&#8729;</mo><mi>k</mi><mo>,</mo></math> then <math><mi>k</mi></math> is equal to ____________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **51**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>25</mn></munderover><msup><mfenced separators="|"><mrow><mn>4</mn><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>25</mn></msup><msub><mi>C</mi><mi>r</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>25</mn></munderover><mi>r</mi><msup><mo>.</mo><mn>25</mn></msup><msub><mi>C</mi><mi>r</mi></msub><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>25</mn></munderover><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><mrow/><mn>25</mn></mmultiscripts></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>25</mn></munderover><mi>r</mi><mo>&#215;</mo><mfrac><mn>25</mn><mi>r</mi></mfrac><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none/><mprescripts/><mrow/><mn>24</mn></mmultiscripts><mo>+</mo><msup><mn>2</mn><mn>25</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>100</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>25</mn></munderover><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none/><mprescripts/><mrow/><mn>25</mn></mmultiscripts><mo>+</mo><msup><mn>2</mn><mn>25</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>100.2</mn><mn>24</mn></msup><mo>+</mo><msup><mn>2</mn><mn>25</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>25</mn></msup><mfenced separators="|"><mrow><mn>50</mn><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>51</mn><msup><mo>.2</mo><mn>25</mn></msup></math>
So, <math><mi>k</mi><mo>=</mo><mn>51</mn></math></p>

</details>

---

### Q40. JEE Main 2020 (07 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

If the sum of the coefficients of all even powers of <math><mi>x</mi></math> in the product <math><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn><mi>n</mi></mrow></msup></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn><mi>n</mi></mrow></msup></mrow></mfenced></math> is <math><mn>61</mn><mo>,</mo><mi></mi></math> then n is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>.</mo><mo>.</mo></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8230;</mo></mrow></mfenced><mo>=</mo><msub><mi>a</mi><mn>0</mn></msub><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><mo>&#215;</mo><msub><mi>a</mi><mn>2</mn></msub><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo></math>
Put <math><mi>x</mi><mo>=</mo><mn>1</mn></math>,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msub><mi>a</mi><mn>0</mn></msub><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><msub><mi>a</mi><mrow><mn>2</mn><mi>n</mi></mrow></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced separators="|"><mn>2</mn></mfenced></math>
Put <math><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mn>1</mn><mo>=</mo><msub><mi>a</mi><mn>0</mn></msub><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><msub><mi>a</mi><mrow><mn>2</mn><mi>n</mi></mrow></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced separators="|"><mn>2</mn></mfenced></math>
From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>+</mo><mfenced><mn>2</mn></mfenced></math>
<math><mn>4</mn><mi>n</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><msub><mrow><mi>a</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mo>&#8230;</mo></mrow></mfenced></math>
<math><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>61</mn></math>
<math><mo>&#8658;</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>61</mn><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>30</mn></math>

</details>

---

### Q41. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mo>(</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>)</mo><mtext>&#8201;</mtext><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mo>(</mo><msup><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>)</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced separators="|"><mrow><msup><mrow><mn>20</mn></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mtext>&#8201;</mtext><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>20</mn></mrow></msub><mo>=</mo><mi>A</mi><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mi>&#946;</mi></mrow></msup></mrow></mfenced><mo>,</mo></math> then the ordered pair <math><mo>(</mo><mi>A</mi><mo>,</mo><mi>&#946;</mi><mo>)</mo></math> is equal to

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mn>380</mn><mo>,</mo><mi> </mi><mn>19</mn></mrow></mfenced></math>
- **(B)** <math><mo>(</mo><mn>420</mn><mo>,</mo><mi> </mi><mn>18</mn><mo>)</mo></math>
- **(C)** <math><mo>(</mo><mn>420</mn><mo>,</mo><mi> </mi><mn>19</mn><mo>)</mo></math>
- **(D)** <math><mo>(</mo><mn>380</mn><mo>,</mo><mi> </mi><mn>18</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mo>(</mo><mn>420</mn><mo>,</mo><mi> </mi><mn>18</mn><mo>)</mo></math>**

**Detailed Solution:**

<math><msup><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow><mrow><mi>n</mi></mrow></msup><mo>=</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>x</mi><mo>+</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>n</mi></mrow></msub><msup><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msup></math>
Diff. w. r. t. <math><mi>x</mi></math>
<math><mo>&#8658;</mo><mi>n</mi><msup><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mtext>&#8201;</mtext><mo>+</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>(</mo><mn>2</mn><mi>x</mi><mo>)</mo><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>n</mi></mrow></msub><mi>n</mi><msup><mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math>
Multiply by <math><mi>x</mi></math> both side
<math><mo>&#8658;</mo><mi>n</mi><mi>x</mi><msup><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>x</mi><mo>+</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>n</mi></mrow></msub><mfenced separators="|"><mrow><mi>n</mi><msup><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msup></mrow></mfenced></math>
Diff. w. r. t. <math><mi>x</mi></math>
<math><mo>&#8658;</mo><mi>n</mi><mo>[</mo><msup><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>x</mi><msup><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>]</mo><mtext>&#8201;</mtext><mo>=</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mtext>&#8201;</mtext><mo>+</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><msup><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msup><mi>X</mi><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>(</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>)</mo><msup><mrow><mi>x</mi></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math>
Put <math><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math><mi>n</mi><mo>=</mo><mn>20</mn></math>
<math><mo>&#8658;</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mtext>&#8201;</mtext><msup><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mtext>&#8201;&#8201;</mtext><msup><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mrow><mo>(</mo><mn>20</mn><mo>)</mo></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>20</mn></mrow></msub></math>
<math><mo>=</mo><mn>20</mn><mo>&#215;</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>18</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mo>+</mo><mn>19</mn></mrow></mfenced><mo>=</mo><mn>420</mn><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>18</mn></mrow></msup></mrow></mfenced><mo>=</mo><mi>A</mi><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mi>&#946;</mi></mrow></msup></mrow></mfenced></math>
Hence, <math><mfenced separators="|"><mrow><mi>A</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mo>(</mo><mn>420</mn><mo>,</mo><mi>&#160;</mi><mn>18</mn><mo>)</mo></math>

</details>

---

### Q42. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series <math><msup><mrow><mn>2</mn><mo>.</mo></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><msup><mrow><mn>5</mn><mo>.</mo></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msup><mrow><mn>8</mn><mo>.</mo></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msup><mrow><mn>11</mn><mo>.</mo></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mrow><mn>62</mn><mo>.</mo></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>20</mn></mrow></msub></math> is equal to

**Options:**

- **(A)** <math><msup><mrow><mn>2</mn></mrow><mrow><mn>26</mn></mrow></msup></math>
- **(B)** <math><msup><mrow><mn>2</mn></mrow><mrow><mn>25</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mn>2</mn></mrow><mrow><mn>24</mn></mrow></msup></math>
- **(D)** <math><msup><mrow><mn>2</mn></mrow><mrow><mn>23</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msup><mrow><mn>2</mn></mrow><mrow><mn>25</mn></mrow></msup></math>**

**Detailed Solution:**

<p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mi>&#160;</mi><mn>2</mn><msup><mo>.</mo><mn>20</mn></msup><msub><mi>C</mi><mn>0</mn></msub><mo>+</mo><mn>5</mn><msup><mo>.</mo><mn>20</mn></msup><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><mn>8</mn><msup><mo>.</mo><mn>20</mn></msup><msub><mi>C</mi><mn>3</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>62</mn><msup><mo>.</mo><mn>20</mn></msup><msub><mi>C</mi><mn>20</mn></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mn>62</mn><msup><mo>.</mo><mn>20</mn></msup><msub><mi>C</mi><mn>0</mn></msub><mo>+</mo><mn>59</mn><msup><mo>.</mo><mn>20</mn></msup><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><mn>56</mn><msup><mo>.</mo><mn>20</mn></msup><msub><mi>C</mi><mn>3</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>2</mn><msup><mo>.</mo><mn>20</mn></msup><msub><mi>C</mi><mn>20</mn></msub><mi mathvariant="normal">&#160;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math> (Writing in reverse order <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mi>n</mi></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mo>=</mo><mi>n</mi></msup><msub><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msub></math> )
Adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>
<math><mn>2</mn><mi>S</mi><mo>=</mo><mn>64</mn><msup><mrow><mo>(</mo></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mo>+</mo></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><msup><mrow><mo>+</mo></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mrow><mo>+</mo></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>20</mn></mrow></msub><mo>)</mo></math>
<math><mo>&#8658;</mo><mi mathvariant="normal">S</mi><mo>=</mo><msup><mrow><mn>32.2</mn></mrow><mrow><mn>20</mn></mrow></msup><mo>=</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>25</mn></mrow></msup></math></p>

</details>

---

### Q43. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced separators="|"><mfrac><mrow><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>i</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow><mrow><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mi>i</mi></msub><msup><mo>+</mo><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>i</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow></mfrac></mfenced></mrow><mn>3</mn></msup><mo>=</mo><mfrac><mi>k</mi><mn>21</mn></mfrac><mo>,</mo></math> then <math><mi>k</mi></math> equals

**Options:**

- **(A)** <math><mn>200</mn></math>
- **(B)** <math><mn>100</mn></math>
- **(C)** <math><mn>50</mn></math>
- **(D)** <math><mn>400</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>100</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></msubsup><msup><mfenced separators="|"><mfrac><mrow><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>i</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow><mrow><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mi>i</mi></msub><mo>+</mo><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>i</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow></mfrac></mfenced><mn>3</mn></msup><mo>=</mo><mfrac><mi>k</mi><mn>21</mn></mfrac></math>

We have <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>i</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow><mrow><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mi>i</mi></msub><mo>+</mo><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>i</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow></mfrac></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>i</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow><mrow><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mi>i</mi></msub><mo>+</mo><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>i</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>i</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow><mrow><msup><mi>&#160;</mi><mn>21</mn></msup><msub><mi>C</mi><mi>i</mi></msub></mrow></mfrac></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mfrac><mi>n</mi><mi>r</mi></mfrac><mo>&#215;</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mmultiscripts><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>&#160;</mi><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>i</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow><mrow><msup><mi>&#160;</mi><mn>21</mn></msup><msub><mi>C</mi><mi>i</mi></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow></mrow><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>i</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow><mrow><mstyle displaystyle="true"><mfrac><mn>21</mn><mi>i</mi></mfrac></mstyle><mo>&#215;</mo><mfenced><mrow><msup><mrow></mrow><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>i</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mi>i</mi><mn>21</mn></mfrac></math>

Hence, the given sum is 

<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></msubsup><mfrac><msup><mfenced separators="|"><mi>i</mi></mfenced><mn>3</mn></msup><msup><mfenced><mn>21</mn></mfenced><mn>3</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><msup><mfenced separators="|"><mn>21</mn></mfenced><mn>3</mn></msup></mfrac><mfenced separators="|"><mrow><msubsup><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></msubsup><msup><mi>i</mi><mn>3</mn></msup></mrow></mfenced></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mrow><mo>&#8721;</mo><msup><mi>r</mi><mn>3</mn></msup></mrow><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mo>=</mo><msup><mfenced><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mfenced><mn>21</mn></mfenced><mn>3</mn></msup></mfrac><msubsup><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></msubsup><msup><mi>i</mi><mn>3</mn></msup><mo>=</mo><mfrac><mn>1</mn><msup><mfenced separators="|"><mn>21</mn></mfenced><mn>3</mn></msup></mfrac><msup><mfenced separators="|"><mfrac><mrow><mn>20</mn><mo>&#183;</mo><mn>21</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>100</mn><mn>21</mn></mfrac></math>

Using the given sum, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>100</mn><mn>21</mn></mfrac><mo>=</mo><mfrac><mi>k</mi><mn>21</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>100</mn><mo>.</mo></math></p>

</details>

---

### Q44. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `3`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mrow/><mn>21</mn></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mo>-</mo><mn>10</mn></msup><msub><mi>C</mi><mn>1</mn></msub></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mrow/><mn>21</mn></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mo>-</mo><mn>10</mn></msup><msub><mi>C</mi><mn>2</mn></msub></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mrow/><mn>21</mn></msup><msub><mi>C</mi><mn>3</mn></msub><msup><mo>-</mo><mn>10</mn></msup><msub><mi>C</mi><mn>3</mn></msub></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mrow/><mn>21</mn></msup><msub><mi>C</mi><mn>4</mn></msub><msup><mo>-</mo><mn>10</mn></msup><msub><mi>C</mi><mn>4</mn></msub></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><msup><mrow/><mn>21</mn></msup><msub><mi>C</mi><mn>10</mn></msub><msup><mo>-</mo><mn>10</mn></msup><msub><mi>C</mi><mn>10</mn></msub></mrow></mfenced><mi>&#160;</mi></math>is

**Options:**

- **(A)** <math><msup><mrow><mn>2</mn></mrow><mrow><mn>21</mn></mrow></msup><mo>-</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>11</mn></mrow></msup></math>
- **(B)** <math><msup><mrow><mn>2</mn></mrow><mrow><mn>21</mn></mrow></msup><mo>-</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mn>2</mn></mrow><mrow><mn>20</mn></mrow></msup><mo>-</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>9</mn></mrow></msup></math>
- **(D)** <math><msup><mrow><mn>2</mn></mrow><mrow><mn>20</mn></mrow></msup><mo>-</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msup><mrow><mn>2</mn></mrow><mrow><mn>20</mn></mrow></msup><mo>-</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup></math>**

**Detailed Solution:**

<blockquote><p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mrow/><mn>21</mn></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mo>-</mo><mn>10</mn></msup><msub><mi>C</mi><mn>1</mn></msub></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mrow/><mn>21</mn></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mo>-</mo><mn>10</mn></msup><msub><mi>C</mi><mn>2</mn></msub></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mrow/><mn>21</mn></msup><msub><mi>C</mi><mn>3</mn></msub><msup><mo>-</mo><mn>10</mn></msup><msub><mi>C</mi><mn>3</mn></msub></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mrow/><mn>21</mn></msup><msub><mi>C</mi><mn>4</mn></msub><msup><mo>-</mo><mn>10</mn></msup><msub><mi>C</mi><mn>4</mn></msub></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><msup><mrow/><mn>21</mn></msup><msub><mi>C</mi><mn>10</mn></msub><msup><mo>-</mo><mn>10</mn></msup><msub><mi>C</mi><mn>10</mn></msub></mrow></mfenced><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msup><mrow/><mn>21</mn></msup><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><msup><mi>&#160;</mi><mn>21</mn></msup><msub><mi>C</mi><mn>2</mn></msub><mo>+</mo><msup><mi>&#160;</mi><mn>21</mn></msup><msub><mi>C</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>&#160;</mi><mn>21</mn></msup><msub><mi>C</mi><mn>10</mn></msub></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mrow/><mn>10</mn></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mo>+</mo><mn>10</mn></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mo>+</mo><mn>10</mn></msup><msub><mi>C</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><msup><mo>+</mo><mn>10</mn></msup><msub><mi>C</mi><mn>10</mn></msub></mrow></mfenced><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msup><mrow></mrow><mn>21</mn></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mo>+</mo><mn>21</mn></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mo>+</mo><mn>21</mn></msup><msub><mi>C</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><msup><mo>+</mo><mn>21</mn></msup><msub><mi>C</mi><mn>10</mn></msub><msup><mo>+</mo><mn>21</mn></msup><msub><mi>C</mi><mn>11</mn></msub><mo>+</mo><mo>&#8230;</mo><msup><mo>+</mo><mn>21</mn></msup><msub><mi>C</mi><mn>20</mn></msub></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msup><mn>2</mn><mn>21</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>1</mn><mo>-</mo><msup><mn>2</mn><mn>10</mn></msup><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><msup><mn>2</mn><mn>10</mn></msup></math>.</p></blockquote>

</details>

---

### Q45. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The sum <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced separators="|"><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mfenced separators="|"><mrow><mi>r</mi><mo>!</mo></mrow></mfenced></math>, is equal to:

**Options:**

- **(A)** <math><mn>11</mn><mi> </mi><mo>×</mo><mfenced separators="|"><mrow><mn>11</mn><mo>!</mo></mrow></mfenced></math>
- **(B)** <math><mn>10</mn><mi> </mi><mo>×</mo><mfenced separators="|"><mrow><mn>11</mn><mo>!</mo><mi> </mi></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mn>11</mn></mrow></mfenced><mo>!</mo></math>
- **(D)** <math><mn>101</mn><mi> </mi><mo>×</mo><mfenced separators="|"><mrow><mn>10</mn><mo>!</mo></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>10</mn><mi> </mi><mo>×</mo><mfenced separators="|"><mrow><mn>11</mn><mo>!</mo><mi> </mi></mrow></mfenced></math>**

**Detailed Solution:**

<math><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>10</mn></mrow></munderover><mrow><mfenced separators="|"><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mrow><mi>r</mi><mo>!</mo></math>
Let us express the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term, as a difference involving consecutive factorials, <math><msub><mrow><mi>T</mi></mrow><mrow><mi>r</mi></mrow></msub><mo>=</mo><mfenced separators="|"><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn><mo>+</mo><mi>r</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mi>&#160;</mi><mi>r</mi><mo>!</mo><mi>&#160;</mi><mo>=</mo><mfenced separators="|"><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>r</mi></mrow></mfenced><mi>&#160;</mi><mi>r</mi><mo>!</mo><mo>-</mo><mfenced separators="|"><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi><mo>!</mo></math>
Therefore,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mi>r</mi></msub><mo>=</mo><mi>r</mi><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>-</mo><mfenced separators="|"><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi><mo>!</mo><mi>&#160;</mi></math>
Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>10</mn><mo>&#160;</mo></math>and adding, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced open="{" close="}"><mrow><mi>r</mi><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>-</mo><mfenced separators="|"><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi><mo>!</mo></mrow></mfenced><mi>&#160;</mi><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>11</mn><mo>!</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced separators="|"><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mi>r</mi><mo>!</mo><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>11</mn><mo>!</mo></math>

</details>

---

### Q46. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>&#160;</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#8800;</mo><mo>-</mo><mn>1</mn><mo>,</mo></math> if <math><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2016</mn></mrow></msup><mo>+</mo><mi>x</mi><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2015</mn></mrow></msup><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2014</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2016</mn></mrow></msup><mo>=</mo><mi></mi><mrow> <mstyle displaystyle="true"> <munderover> <mo>&#8721;</mo> <mrow> <mi>i</mi><mo>=</mo><mn>0</mn> </mrow> <mrow> <mn>2016</mn> </mrow> </munderover> <mrow> <msub> <mi>a</mi> <mi>i</mi> </msub> <msub> <mi>x</mi> <mi>i</mi> </msub> </mrow> </mstyle> </mrow> </math>, then <math><msub><mrow><mi>a</mi></mrow><mrow><mn>17</mn></mrow></msub></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>2017</mn><mi></mi><mo>!</mo></mrow><mrow><mn>17</mn><mi></mi><mo>!</mo><mn>2000</mn><mi></mi><mo>!</mo></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>2016</mn><mo>!</mo></mrow><mrow><mn>17</mn><mo>!1</mo><mn>999</mn><mo>!</mo></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>2016</mn><mo>!</mo></mrow><mrow><mn>16</mn><mo>!</mo></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>2017</mn><mo>!</mo></mrow><mrow><mn>2000</mn><mo>!</mo></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>2017</mn><mi></mi><mo>!</mo></mrow><mrow><mn>17</mn><mi></mi><mo>!</mo><mn>2000</mn><mi></mi><mo>!</mo></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2016</mn></msup><mo>+</mo><mi>x</mi><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2015</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2014</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>x</mi><mn>2015</mn></msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>x</mi><mn>2016</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mfrac><mi>x</mi><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mi>&#160;</mi><mi>S</mi><mo>=</mo><mi>x</mi><mi>&#160;</mi><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2015</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2014</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>x</mi><mn>2016</mn></msup><mo>+</mo><mfrac><msup><mi>x</mi><mn>2017</mn></msup><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>-</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>S</mi><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2016</mn></msup><mo>-</mo><mfrac><msup><mi>x</mi><mn>2017</mn></msup><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></math>

<math><mo>&#8756;</mo></math> <math><mi>S</mi><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2017</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2017</mn></mrow></msup></math>

Coefficient <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>17</mn></msub><msup><mo>=</mo><mn>2017</mn></msup><msub><mi>C</mi><mn>17</mn></msub><mi>&#160;</mi><mo>=</mo><mfrac><mrow><mn>2017</mn><mo>!</mo></mrow><mrow><mn>17</mn><mo>!</mo><mn>2000</mn><mo>!</mo></mrow></mfrac></math></p>

</details>

---

### Q47. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `3`

If the number of terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>+</mo><mfrac><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>n</mi></msup><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math>, then the sum of the coefficients of all the terms in this expansion is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>243</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>729</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2187</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>729</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>+</mo><mfrac><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>n</mi></msup></math></p><p>We know, if having three variables then total number of terms would be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi mathvariant="normal">n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi mathvariant="normal">n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>=</mo><mn>28</mn></math>

<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mi mathvariant="normal">n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi mathvariant="normal">n</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">&#160;</mi></mrow></mfenced><mo>=</mo><mn>56</mn></math>

Which gives <math><mi mathvariant="normal">n</mi><mo>=</mo><mn>6</mn></math> , and sum of coefficients would be </p><p><math><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mo>+</mo><mn>4</mn></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></msup><mo>=</mo><msup><mrow><mn>3</mn></mrow><mrow><mn>6</mn></mrow></msup><mo>=</mo><mn>729</mn></math> .</p>

</details>

---

### Q48. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the rational terms in the binomial expansion of $\left(2^{\frac{1}{2}}+3^{\frac{1}{5}}\right)^{10}$ is :

**Options:**

- **(A)** 25
- **(B)** 32
- **(C)** 9
- **(D)** 41

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 41**

**Detailed Solution:**

$\left(2^{1 / 2}+3^{1 / 5}\right)^{10}={ }^{10} \mathrm{C}_0\left(2^{1 / 2}\right)^{10}$
$$
+{ }^{10} \mathrm{C}_1\left(2^{1 / 2}\right)^9\left(3^{1 / 5}\right)+\ldots \ldots+{ }^{10} \mathrm{C}_{10}\left(3^{1 / 5}\right)^{10}
$$
There are only two rational terms - first term
and last term.
Now sum of two rational terms
$$
=(2)^5+(3)^2=32+9=41
$$

</details>

---

### Q49. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{S}_1=\sum_{\mathrm{j}=1}^{10} \mathrm{j}(\mathrm{j}-1)^{10} \mathrm{C}_{\mathrm{j}}, \mathrm{S}_2=\sum_{\mathrm{j}=1}^{10} \mathrm{j}^{10} \mathrm{C}_{\mathrm{j}}$ and $\mathrm{S}_3=\sum_{\mathrm{j}=1}^{10} \mathrm{j}^2{ }^{10} \mathrm{C}_{\mathrm{j}}$.
Statement-1: $\mathrm{S}_3=55 \times 2^9$
Statement-2: $S_1=90 \times 2^8$ and $S_2=10 \times 2^8$.

**Options:**

- **(A)** Statement-1 is true, Statement-2 is true; Statement-2 is not the correct explanation for Statement-1
- **(B)** Statement-1 is true, Statement-2 is false
- **(C)** Statement-1 is false, Statement-2 is true
- **(D)** Statement-1 is true, Statement-2 is true; Statement-2 is the correct explanation for Statement-1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement-1 is true, Statement-2 is false**

**Detailed Solution:**

$S_1=\sum_{j=1}^{10} j(j-1) \frac{10 !}{j(j-1)(j-2) !(10-j) !}=90 \sum_{j=2}^{10} \frac{8 !}{(j-2) !(8-(j-2)) !}=90 \cdot 2^8$.
$S_2=\sum_{j=1}^{10} j \frac{10 !}{j(j-1) !(9-(j-1)) !}=10 \sum_{j=1}^{10} \frac{9 !}{(j-1) !(9-(j-1)) !}=10 \cdot 2^9$.
$S_3=\sum_{j=1}^{10}[j(j-1)+j] \frac{10 !}{j !(10-j) !}=\sum_{j=1}^{10} j(j-1)^{10} C_j=\sum_{j=1}^{10} j^{10} C_j=90 \cdot 2^8+10 \cdot 2^9$
$=90 \cdot 2^8+20 \cdot 2^8=110 \cdot 2^8=55 \cdot 2^9$.

</details>

---

### Q50. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `3`

Statement-1: $\sum_{r=0}^n(r+1)^n C_r=(n+2) 2^{n-1}$
Statement -2: $\quad \sum_{r=0}^n(r+1)^n C_r x^r=(1+x)^n+n x(1+x)^{n-1}$.

**Options:**

- **(A)** Statement $-1$ is false, Statement $-2$ is true
- **(B)** Statement $-1$ is true, Statement $-2$ is true, Statement $-2$ is a correct explanation for Statement $-1$
- **(C)** Statement $-1$ is true, Statement $-2$ is true; Statement $-2$ is not a correct explanation for Statement $-1$.
- **(D)** Statement $-1$ is true, Statement $-2$ is false.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement $-1$ is true, Statement $-2$ is true, Statement $-2$ is a correct explanation for Statement $-1$**

**Detailed Solution:**

$$
\begin{aligned}
& \sum_{r=0}^n(r+1){ }^n C_r=\sum_{r=0}^n r{ }^n C_r+{ }^n C_r \\
& =\sum_{r=0}^n r \frac{n}{r}{ }^{n-1} C_{r-1}+\sum_{r=0}^n{ }^n C_r=n 2^{n-1}+2^n \\
& =2^{n-1}(n+2)
\end{aligned}
$$
Statement $-1$ is true
$$
\begin{aligned}
& \sum(r+1)^n C_r x^r=\sum r{ }^n C_r x^r+\sum{ }^n C_r x^r \\
& =n \sum_{r=0}^n{ }^{n-1} C_{r-1} x^r+\sum_{r=0}^n{ }^n C_r x^r=n x(1+x)^{n-1}+(1+x)^n
\end{aligned}
$$
Substituting $x=1$
$$
\sum(r+1)^n C_r=n 2^{n-1}+2^n
$$
Hence Statement $-2$ is also true and is a correct explanation of Statement $-1$.

</details>

---

### Q51. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series
${ }^{20} \mathrm{C}_0-{ }^{20} \mathrm{C}_1+{ }^{20} \mathrm{C}_2-{ }^{20} \mathrm{C}_3+\ldots-\ldots+{ }^{20} \mathrm{C}_{10} \text { is }$

**Options:**

- **(A)** $-{ }^{20} \mathrm{C}_{10}$
- **(B)** $\frac{1}{2}{ }^{20} \mathrm{C}_{10}$
- **(C)** $0$
- **(D)** ${ }^{20} \mathrm{C}_{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2}{ }^{20} \mathrm{C}_{10}$**

**Detailed Solution:**

$(1+\mathrm{x})^{20}={ }^{20} \mathrm{C}_0+{ }^{20} \mathrm{C}_1 \mathrm{x}+\ldots+{ }^{20} \mathrm{C}_{10} \mathrm{x}{ }^{10}+\ldots+{ }^{20} \mathrm{C}_{20} \mathrm{x}^{20}$
put $\mathrm{x}=-1$,
$0={ }^{20} \mathrm{C}_0-{ }^{20} \mathrm{C}_1+\ldots-{ }^{20} \mathrm{C}_9+{ }^{20} \mathrm{C}_{10}-{ }^{20} \mathrm{C}_{11}+\ldots+{ }^{20} \mathrm{C}_{20}$
$0=2\left({ }^{20} \mathrm{C}_0-{ }^{20} \mathrm{C}_1+\ldots-{ }^{20} \mathrm{C}_9\right)+{ }^{20} \mathrm{C}_{10}$
$\Rightarrow{ }^{20} \mathrm{C}_0-{ }^{20} \mathrm{C}_1+\ldots+{ }^{20} \mathrm{C}_{10}=\frac{1}{2}{ }^{20} \mathrm{C}_{10}$.

</details>

---

### Q52. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `3`

The value of ${ }^{50} \mathrm{C}_4+\sum_{\mathrm{r}=1}^6{ }^{56-r} \mathrm{C}_3$ is

**Options:**

- **(A)** ${ }^{55} \mathrm{C}_4$
- **(B)** ${ }^{55} \mathrm{C}_3$
- **(C)** ${ }^{56} \mathrm{C}_3$
- **(D)** ${ }^{56} \mathrm{C}_4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) ${ }^{56} \mathrm{C}_4$**

**Detailed Solution:**

$$
\begin{aligned}
& { }^{50} \mathrm{C}_4+\sum_{\mathrm{r}=1}^6{ }^{56-r} \mathrm{C}_3 \\
& \Rightarrow{ }^{50} \mathrm{C}_4+\left[{ }^{55} \mathrm{C}_3+{ }^{54} \mathrm{C}_3+{ }^{53} \mathrm{C}_3+{ }^{52} \mathrm{C}_3+{ }^{51} \mathrm{C}_3+{ }^{50} \mathrm{C}_3\right] \\
& =\left({ }^{50} \mathrm{C}_4+{ }^{50} \mathrm{C}_3\right)+{ }^{51} \mathrm{C}_3+{ }^{52} \mathrm{C}_3+{ }^{53} \mathrm{C}_3+{ }^{54} \mathrm{C}_3+{ }^{55} \mathrm{C}_3 \\
& \Rightarrow\left({ }^{51} \mathrm{C}+{ }^{51} \mathrm{C}\right)+{ }^{52} \mathrm{C}_3+{ }^{53} \mathrm{C}_3+{ }^{54} \mathrm{C}_3+{ }^{55} \mathrm{C}_3 \\
& \Rightarrow{ }^{55} \mathrm{C}_4+{ }^{55} \mathrm{C}_3={ }^{56} \mathrm{C}_4 .
\end{aligned}
$$

</details>

---

### Q53. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `3`

If $S_n=\sum_{r=0}^n \frac{1}{{ }^n C_r}$ and $t_n=\sum_{r=0}^n \frac{r}{{ }^n C_r}$, then $\frac{t_n}{S_n}$ is equal to

**Options:**

- **(A)** $\frac{1}{2} \mathrm{n}$
- **(B)** $\frac{1}{2} n-1$
- **(C)** $n-1$
- **(D)** $\frac{2 n-1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2} \mathrm{n}$**

**Detailed Solution:**

$t=\sum_{r=0}^n \frac{r}{{ }^n C_r}=\sum_{r=0}^n \frac{n-r}{{ }^n C_{n-r}}=\sum_{r=0}^n \frac{n-r}{{ }^n C_r}\left(\because{ }^n C_r={ }^n C_{n-r}\right)$
$2 t_n=\sum_{r=0}^n \frac{r+n-r}{{ }^n C_r}=\sum_{r=0}^n \frac{n}{{ }^n C_r} \Rightarrow t_n=\frac{n}{2} \sum_{r=0}^n \frac{1}{{ }^n C_r}=\frac{n}{2} S_n \Rightarrow \frac{t_n}{S_n}=\frac{n}{2}$

</details>

---

