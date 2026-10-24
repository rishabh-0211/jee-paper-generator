# BITSAT Mathematics - Sequences and Series

## Topic 6: Summation of Series

**Total Questions:** 9

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `2`

If $\sum_{k=1}^n k(k+1)(k-1)=p n^4+q n^3+t n^2+s n$ where $p, q, t$ and $s$ are constants, then the value of $s$ is equal to

**Options:**

- **(A)** $-\frac{1}{4}$
- **(B)** $-\frac{1}{2}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{1}{2}$**

**Detailed Solution:**

$\begin{aligned}
\text { Let } S & =\sum_{k=1}^n k(k+1)(k-1) \\
& =\sum_{k=1}^n k^3-k
\end{aligned}$
We know that
$\sum_{r=1}^P r=\frac{P(P+1)}{2}$
and
$\sum_{r=1}^P r^3=\left[\frac{P(P+1)}{2}\right]^2$
$\begin{aligned}
S & =\left[\frac{n(n+1)}{2}\right]^2-\left[\frac{n(n+1)}{2}\right] \\
& =\frac{n(n+1)}{2}\left[\frac{n(n+1)}{2}-1\right] \\
& =\left(\frac{n^2+n}{2}\right)\left[\frac{n^2+n-2}{2}\right] \\
& =\frac{n^4}{4}+\frac{n^3}{2}-\frac{n^2}{4}-\frac{n}{2}...(i)
\end{aligned}$
Now, by comparing $p n^4+q n^3+t n^2+s n$ with Eq. (i),
$S=-\frac{1}{2}$

</details>

---

### Q2. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\tan ^{-1}\left[\frac{1}{1+1.2}\right]+\tan ^{-1}\left[\frac{1}{1+2.3}\right]+$ $\ldots+\tan ^{-1}\left[\frac{1}{1+n(n+1)}\right]=\tan ^{-1}[x]$, then $x$ is
equal to

**Options:**

- **(A)** $\frac{1}{n+1}$
- **(B)** $\frac{n}{n+1}$
- **(C)** $\frac{1}{n+2}$
- **(D)** $\frac{n}{n+2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{n}{n+2}$**

**Detailed Solution:**

$\begin{aligned} & \text { Given } \tan ^{-1}\left(\frac{1}{1+1.2}\right)+\tan ^{-1}\left(\frac{1}{1+2.3}\right)+\ldots \\ & +\tan ^{-1}\left(\frac{1}{1+n(n+1)}\right)=\tan ^{-1}(x)\end{aligned}$
$\begin{aligned} \Rightarrow \tan ^{-1}\left(\frac{2-1}{1+1.2}\right) & +\tan ^{-1}\left(\frac{3-2}{1+2.3}\right)+\ldots \\ & +\tan ^{-1}\left(\frac{n+1-n}{1+n(n+1)}\right)=\tan ^{-1}(x)\end{aligned}$
$\begin{aligned} & \Rightarrow \tan ^{-1}(2)-\tan ^{-1}(1)+\tan ^{-1}(3)-\tan ^{-1}(2)+\ldots \\ & +\tan ^{-1}(\mathrm{n}+1)-\tan ^{-1}(\mathrm{n})=\tan ^{-1}(x)\end{aligned}$
$\Rightarrow \tan ^{-1}(\mathrm{n}+1)-\tan ^{-1}(1)=\tan ^{-1}(x)$
$\left\{\because \tan ^{-1}(A)-\tan ^{-1}(B)=\tan ^{-1}\left(\frac{A-B}{1+A \cdot B}\right)\right\}$
$\Rightarrow \tan ^{-1}\left(\frac{n}{n+2}\right)=\tan ^{-1}(x) \Rightarrow x=\frac{n}{n+2}$

</details>

---

### Q3. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the infinite series
$1+\frac{5}{6}+\frac{12}{6^2}+\frac{22}{6^3}+\frac{35}{6^4}+\frac{51}{6^5}+\frac{70}{6^6}+\ldots .$. is equal
to:

**Options:**

- **(A)** $\frac{425}{216}$
- **(B)** $\frac{429}{216}$
- **(C)** $\frac{288}{125}$
- **(D)** $\frac{280}{125}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{288}{125}$**

**Detailed Solution:**

Let $S=1+\frac{5}{6}+\frac{12}{6^2}+\frac{22}{6^3}+\frac{35}{6^4}+\ldots$    .....(i)
$\frac{S}{6}=\frac{1}{6}+\frac{5}{6^2}+\frac{12}{6^3}+\frac{22}{6^4}+\ldots$  ....(ii)
On subtracting (i) from (ii)
$\frac{5}{6} S=1+\frac{4}{6}+\frac{7}{6^2}+\frac{10}{6^3}+\frac{13}{6^4}+\cdots$
$\frac{5}{36} S=\frac{1}{6}+\frac{4}{6^2}+\frac{7}{6^3}+\frac{10}{6^4}+\frac{13}{6^5}+\cdots$
on subtraction
$\frac{25}{36} S=1+\frac{3}{6}+\frac{3}{6^2}+\frac{3}{6^3}+\ldots=\frac{8}{5}$
$S=\frac{8}{5} \times \frac{36}{25}=\frac{288}{125}$

</details>

---

### Q4. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1} \frac{1}{x^2+x+1}+\tan ^{-1} \frac{1}{x^2+3 x+3}$
$+\tan ^{-1} \frac{1}{x^2+5 x+7}+\ldots$.to $n$ terms, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{1}{x^2+n^2}-\frac{1}{x^2+1}$
- **(B)** $\frac{1}{(x+n)^2+1}-\frac{1}{x^2+1}$
- **(C)** $\frac{1}{x^2+(n+1)^2}-\frac{1}{x^2+1}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{(x+n)^2+1}-\frac{1}{x^2+1}$**

**Detailed Solution:**

Given, $y=\tan ^{-1} \frac{1}{x^2+x+1}$
$+\tan ^{-1} \frac{1}{x^2+3 x+3}+\tan ^{-1} \frac{1}{x^2+5 x+7}+\cdots \cdot$
to $n$ terms
$=\tan ^{-1}\left\{\frac{1}{1+x(x+1)}\right\}+\tan ^{-1}\left\{\frac{1}{1+(x+1)(x+2)}\right\}$
$+\tan ^{-1}\left\{\frac{1}{1+(x+2)(x+3)}\right\}$
$+\ldots \ldots \ldots+\tan ^{-1}\left\{\frac{1}{1+(x+(n-1))(x+n)}\right\}$
$=\tan ^{-1}\left\{\frac{(x+1)-x}{1+(x+1) x}\right\}$
$+\tan ^{-1}\left\{\frac{(x+2)-(x+1)}{1+(x+2)(x+1)}\right\}$
$+\tan ^{-1}\left\{\frac{(x+3)-(x+2)}{1+(x+3)(x+2)}\right\}$
$+\ldots .+\tan ^{-1}\left(\frac{(x+n)-(x+n-1)}{1+(x+n)(x+n-1)}\right)$
$\therefore y=\left\{\tan ^{-1}(x+1)-\tan ^{-1}(x)\right\}$
$+\left\{\tan ^{-1}(x+2)-\tan ^{-1}(x+1)\right\}$
$+\left\{\tan ^{-1}(x+3)-\tan ^{-1}(x+2)\right\}$
$+\ldots \ldots . .+\left\{\tan ^{-1}(x+n)-\tan ^{-1}[x+(n-1)]\right\}$
So, $\quad y=\tan ^{-1}(x+n)-\tan ^{-1}(x)$
On differentiating both sides w.r.t. $x$, we get
$\frac{d y}{d x}=\frac{1}{1+(x+n)^2}-\frac{1}{1+x^2}$

</details>

---

### Q5. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

The sum to infinite term of the series $1+\frac{2}{3}+\frac{6}{3^2}+\frac{10}{3^3}+\frac{14}{3^4}+\cdots$ is

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 6
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

We have
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/v4Z1kTVNykWyCrgSFIT-Hx_GqWd1cn_W85BMAa4x06o.original.fullsize.png">

Multiplying both sides by $\frac{1}{3}$, we get<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/rGNr5MT4r0M2gB_qD0WW5Cd7tquZXrpCI5abkeFzpcU.original.fullsize.png">

Subtracting eqn. (ii) from eqn. (i), we get
$\begin{aligned} & \frac{2}{3} S=1+\frac{1}{3}+\frac{4}{3^2}+\frac{4}{3^3}+\frac{4}{3^4}+\ldots \ldots \ldots \infty \\ & \Rightarrow \frac{2}{3} S=\frac{4}{3}+\frac{4}{3^2}+\frac{4}{3^3}+\frac{4}{3^4}+\ldots \ldots \ldots \infty \\ & \Rightarrow \frac{2}{3} S=\frac{\frac{4}{3}}{1-\frac{1}{3}}=\frac{4}{3} \times \frac{3}{2} \Rightarrow S=3\end{aligned}$

</details>

---

### Q6. BITSAT 2020

*Type:* `singleCorrect` | *Level:* `2`

The sum of the infinite series $\frac{2^{2}}{2 !}+\frac{2^{4}}{4 !}+\frac{2^{6}}{6 !}+\ldots$

is equal to

**Options:**

- **(A)** $\frac{\mathrm{e}^{2}+1}{2 \mathrm{e}}$
- **(B)** $\frac{\mathrm{e}^{4}+1}{2 \mathrm{e}^{2}}$
- **(C)** $\frac{\left(\mathrm{e}^{2}-1\right)^{2}}{2 \mathrm{e}^{2}}$
- **(D)** $\frac{\left(\mathrm{e}^{2}+1\right)^{2}}{2 \mathrm{e}^{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\left(\mathrm{e}^{2}-1\right)^{2}}{2 \mathrm{e}^{2}}$**

**Detailed Solution:**

We know that

$\frac{e^{x}+e^{-x}}{2}=1+\frac{x^{2}}{2 !}+\frac{x^{4}}{4 !}+\frac{x^{6}}{6 !}+\ldots$

keeping $\mathrm{x}=2$, we get

Expression $=\frac{1}{2}\left[\frac{e^{2}+e^{-2}}{2}\right]-1=\frac{\left(e^{2}-1\right)^{2}}{2 e^{2}}$

</details>

---

### Q7. BITSAT 2018

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><mi>t</mi><mi>r</mi></msub><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow><mn>8</mn></mfrac><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mi>r</mi></msub></math> denotes the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term of a series, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mn>1</mn><msub><mi>t</mi><mi>r</mi></msub></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><mi>t</mi><mi>r</mi></msub><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow><mn>8</mn></mfrac><mo>=</mo><msub><mi>S</mi><mi>n</mi></msub></math> (say)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><msub><mi>t</mi><mi>r</mi></msub><mo>=</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mn>8</mn></mfrac><mo>=</mo><msub><mi>S</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mi>n</mi></msub><mo>=</mo><msub><mi>S</mi><mi>n</mi></msub><mo>-</mo><msub><mi>S</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mn>1</mn><msub><mi>t</mi><mi>r</mi></msub></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mn>2</mn><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfenced><mrow><mfrac><mn>1</mn><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfenced><mrow><mfrac><mn>1</mn><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mfrac><mn>1</mn><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced><mrow><mn>0</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q8. BITSAT 2016

*Type:* `singleCorrect` | *Level:* `3`

$\left(x+\frac{1}{x}\right)^{2}+\left(x^{2}+\frac{1}{x^{2}}\right)^{2}+$

$\left(x^{3}+\frac{1}{x^{3}}\right)^{2} \quad \ldots .$ upto $n$ terms is

**Options:**

- **(A)** $\frac{x^{2 n}-1}{x^{2}-1} \times \frac{x^{2 n+2}+1}{x^{2 n}}+2 n$
- **(B)** $\frac{x^{2 n}+1}{x^{2}+1} \times \frac{x^{2 n+2}-1}{x^{2 n}}-2 n$
- **(C)** $\frac{x^{2 n}-1}{x^{2}-1} \times \frac{x^{2 n}-1}{x^{2 n}}-2 n$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{x^{2 n}-1}{x^{2}-1} \times \frac{x^{2 n+2}+1}{x^{2 n}}+2 n$**

**Detailed Solution:**

The series is

$$

\begin{array}{l}

\left(x^{2}+x^{4}+x^{6}+\ldots\right)+\left(\frac{1}{x^{2}}+\frac{1}{x^{4}}+\frac{1}{x^{6}}+\ldots\right) \\

+(2+2+\ldots . .) \\

=\frac{x^{2}\left(x^{2 n}-1\right)}{x^{2}-1}+\frac{\frac{1}{x^{2}}\left(1-\frac{1}{x^{2 n}}\right)}{1-\frac{1}{x^{2}}}+2 n \\

=\frac{x^{2}\left(x^{2 n}-1\right)}{x^{2}-1}+\frac{x^{2 n}-1}{\left(x^{2}-1\right) x^{2 n}}+2 n \\

=\frac{x^{2 n}-1}{x^{2}-1} \times \frac{x^{2 n+2}+1}{x^{2 n}}+2 n

\end{array}

$$

</details>

---

### Q9. BITSAT 2013

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series $1+2.2+3.2^{2}+4.2^{3}+\ldots .+100.2^{99}$ is

**Options:**

- **(A)** $100 \cdot 2^{100}+1$
- **(B)** $99.2^{100}+1$
- **(C)** $99.2^{100}-1$
- **(D)** $100.2^{100}+1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $99.2^{100}+1$**

**Detailed Solution:**

Let $S=1+2.2+3.2^{2}+4.2^{2}+\ldots .+100.2^{99}$

It is an arithmetico - geometric series. On multiplying Eq.

(i) by 2 and then subtracting it from Eq. (i), we get

$S=1+2.2+3.2^{2}+4.2^{3}+\ldots+100.2^{99}$

$2 S=1.2+2.2^{2} \pm 3.2^{3}+\ldots+99.2^{99}+100.2^{100}$

$\begin{aligned}-S &=1+2+2^{2}+2^{3} \ldots+2^{99}-100.2^{100} \\ & \Rightarrow-S=\frac{1\left(2^{100}-1\right)}{2-1}-100.2^{100} \\ & \Rightarrow-S=2^{100}-1-100.2^{100} \\ & \Rightarrow-S=-1-99.2^{100} \\ & \Rightarrow S=99.2^{100}+1 \end{aligned}$

</details>

---

