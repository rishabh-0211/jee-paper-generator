# JEE Main Mathematics - Permutation Combination

## Topic 1: Factorial

**Total Questions:** 6

---

### Q1. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The largest $\mathrm{n} \in \mathbf{N}$, for which $7^{\mathrm{n}}$ divides 101!, is :

**Options:**

- **(A)** 16
- **(B)** 15
- **(C)** 18
- **(D)** 19

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 16**

**Detailed Solution:**

Exponent of 7 in $101!$ is:
$\left\lfloor \frac{101}{7} \right\rfloor + \left\lfloor \frac{101}{7^2} \right\rfloor + \left\lfloor \frac{101}{7^3}\right\rfloor + \ldots = 14 + 2 = 16$.

</details>

---

### Q2. JEE Main 2024 (09 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

The number of integers, between 100 and 1000 having the sum of their digits equals to 14 , is _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **70**

**Detailed Solution:**

$\mathrm{N}=\mathrm{ab} \mathrm{c}$ (i)
$\begin{aligned}
& \text { All distinct digits } \\
& \mathrm{a}+\mathrm{b}+\mathrm{c}=14 \\
& \mathrm{a} \geq 1 \\
& \mathrm{~b}, \mathrm{c} \in\{0 \text { to } 9\}
\end{aligned}$
$\begin{array}{lll} 
by hit \& trial : & 8 cases \\
(6,5,3) & (8,6,0) & (9,4,1) \\
(7,6,1) & (8,5,1) & (9,3,2) \\
(7,5,2) & (8,4,2) & \\
(7,4,3) & (9,5,0) &
\end{array}$
(ii) 2 same, 1 diff $\quad a=b$;c
$2 \mathrm{a}+\mathrm{c}=14$
by values :
$\begin{aligned}
& \left.\begin{array}{l}
(3,8) \\
(4,6) \\
(5,4) \\
(6,2) \\
(7,0)
\end{array}\right\} \frac{3 !}{2 !} \times 5-1 \\
& =14 \text { cases }
\end{aligned}$
(iii) all same :
$\begin{aligned}
& \begin{array}{l}
3 a=14 \\
a=\frac{14}{3} \times \text { rejected } \\
0 \text { cases }
\end{array}
\end{aligned}$
Hence, Total cases:
$\begin{aligned}
& 8 \times 3 !+2 \times(4)+14 \\
& =48+22 \\
& =70
\end{aligned}$

</details>

---

### Q3. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $0 \leq \mathrm{r} \leq \mathrm{n}$. If ${ }^{\mathrm{n}+1} \mathrm{C}_{\mathrm{r}+1}:{ }^n \mathrm{C}_{\mathrm{r}}:{ }^{\mathrm{n}-1} \mathrm{C}_{\mathrm{r}-1}=55: 35: 21$, then $2 \mathrm{n}+5 \mathrm{r}$ is equal to:

**Options:**

- **(A)** 50
- **(B)** 62
- **(C)** 55
- **(D)** 60

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 50**

**Detailed Solution:**

$\begin{aligned} & \frac{{ }^{n+1} C_r}{{ }^n C_r}=\frac{55}{35} \\ & \frac{(n+1) !}{(r+1) !(n-r)} ! \frac{r !(n-r) !}{n !}=\frac{11}{7} \\ & \frac{(n+1)}{r+1}=\frac{11}{7}\end{aligned}$
$\begin{aligned} & 7 \mathrm{n}=4+11 \mathrm{r} \\ & \frac{{ }^n C_r}{{ }^{n-1} C_{r-1}}=\frac{35}{21} \\ & \frac{n !}{r !(n-r) !}=\frac{(r-1) !(n-r) !}{(n-1) !}=\frac{5}{3} \\ & \frac{n}{r}=\frac{5}{3} \\ & 3 n=5 r \\ & \text { By solving } r=6 \quad n=10 \\ & 2 n+5 r=50\end{aligned}$

</details>

---

### Q4. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mfrac><mrow><mo>(</mo><mn>4</mn><mo>!</mo><mo>)</mo><mo>!</mo></mrow><mrow><mo>(</mo><mn>4</mn><mo>!</mo><msup><mo>)</mo><mrow><mn>3</mn><mo>!</mo></mrow></msup></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><mfrac><mrow><mo>(</mo><mn>5</mn><mo>!</mo><mo>)</mo><mo>!</mo></mrow><mrow><mo>(</mo><mn>5</mn><mo>!</mo><msup><mo>)</mo><mrow><mn>4</mn><mo>!</mo></mrow></msup></mrow></mfrac></math>. Then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>∈</mo><mi mathvariant="normal">N</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>∉</mo><mi mathvariant="normal">N</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>∉</mo><mi mathvariant="normal">N</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>∈</mo><mi mathvariant="normal">N</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>∈</mo><mi mathvariant="normal">N</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>∈</mo><mi mathvariant="normal">N</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>∉</mo><mi mathvariant="normal">N</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>∉</mo><mi mathvariant="normal">N</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>∈</mo><mi mathvariant="normal">N</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>∈</mo><mi mathvariant="normal">N</mi></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">α</mi><mo>=</mo><mfrac><mrow><mo>(</mo><mn>4</mn><mo>!</mo><mo>)</mo><mo>!</mo></mrow><mrow><mo>(</mo><mn>4</mn><mo>!</mo><msup><mo>)</mo><mrow><mn>3</mn><mo>!</mo></mrow></msup></mrow></mfrac><mo>,</mo><mo> </mo><mi mathvariant="normal">β</mi><mo>=</mo><mfrac><mrow><mo>(</mo><mn>5</mn><mo>!</mo><mo>)</mo><mo>!</mo></mrow><mrow><mo>(</mo><mn>5</mn><mo>!</mo><msup><mo>)</mo><mrow><mn>4</mn><mo>!</mo></mrow></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">α</mi><mo>=</mo><mfrac><mrow><mo>(</mo><mn>24</mn><mo>)</mo><mo>!</mo></mrow><mrow><mo>(</mo><mn>4</mn><mo>!</mo><msup><mo>)</mo><mn>6</mn></msup></mrow></mfrac><mo>,</mo><mo> </mo><mi mathvariant="normal">β</mi><mo>=</mo><mfrac><mrow><mo>(</mo><mn>120</mn><mo>)</mo><mo>!</mo></mrow><mrow><mo>(</mo><mn>5</mn><mo>!</mo><msup><mo>)</mo><mn>24</mn></msup></mrow></mfrac></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math> distinct objects are divided into <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> groups of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> objects in each group, then the number of ways of formation of group is<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>24</mn><mo>!</mo></mrow><mrow><mo>(</mo><mn>4</mn><mo>!</mo><msup><mo>)</mo><mn>6</mn></msup><mo>.</mo><mn>6</mn><mo>!</mo></mrow></mfrac><mo>∈</mo><mi mathvariant="normal">N</mi></math></p><p>Similarly, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math> distinct objects are divided into <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math> groups of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> objects in each group.</p><p>So, the number of ways of formation of groups</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>(</mo><mn>120</mn><mo>)</mo><mo>!</mo></mrow><mrow><mo>(</mo><mn>5</mn><mo>!</mo><msup><mo>)</mo><mn>24</mn></msup><mo>·</mo><mn>24</mn><mo>!</mo></mrow></mfrac><mo>∈</mo><mi mathvariant="normal">N</mi></math></p>

</details>

---

### Q5. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mrow></mrow><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup><msub><mi>C</mi><mn>6</mn></msub></mrow><mrow><msup><mrow></mrow><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><msub><mi>P</mi><mn>2</mn></msub></mrow></mfrac><mo>=</mo><mn>11</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> satisfies the equation:

**Options:**

- **(A)** <math><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>n</mi><mo>-</mo><mn>110</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>80</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>3</mn><mi>n</mi><mo>-</mo><mn>108</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>5</mn><mi>n</mi><mo>-</mo><mn>84</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>3</mn><mi>n</mi><mo>-</mo><mn>108</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<math><mfrac><mrow><msup><mrow></mrow><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>6</mn></mrow></msub></mrow><mrow><msup><mrow></mrow><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><msub><mrow><mi>P</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mn>11</mn></math>

<math><mo>&#8658;</mo></math> <math><mfrac><mrow><mfrac><mrow><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mi>n</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>6</mn><mi>&#160;</mi><mo>.</mo><mn>5</mn><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mn>4</mn><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mn>3</mn><mo>.</mo><mi>&#160;</mi><mn>2</mn><mo>.</mo><mi>&#160;</mi><mn>1</mn><mi>&#160;</mi></mrow></mfrac></mrow><mrow><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>11</mn></math>

<math><mo>&#8658;</mo></math> <math><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>11.10.9</mn><mo>.</mo><mn>8</mn></math>

<math><mo>&#8658;</mo></math> <math><mi>n</mi><mo>=</mo><mn>9</mn></math>

</details>

---

### Q6. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

If ${ }^n C_r$ denotes the number of combination of $n$ things taken $r$ at a time, then the expression ${ }^n C_{r+1}+{ }^n C_{r-1}+2 x^n C_r$ equals

**Options:**

- **(A)** ${ }^{n+1} C_{r+1}$
- **(B)** ${ }^{n+2} C_r$
- **(C)** ${ }^{n+2} C_{r+1}$
- **(D)** ${ }^{n+1} C_r$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) ${ }^{n+2} C_{r+1}$**

**Detailed Solution:**

After t; velocity $=\mathrm{f} \times \mathrm{t}$
$V_{B A}=\vec{f} t+(-\vec{u})=\sqrt{f^2 t^2+u^2-2 f u t \cos \alpha}$
For max. and min.
$\frac{\mathrm{d}}{\mathrm{dt}}\left(\mathrm{V}_{\mathrm{BA}}^2\right)=2 \mathrm{f}^2 \mathrm{t}-2 \mathrm{fu} \cos \alpha=0 \quad$ or $\quad \mathrm{t}=\frac{\mathrm{u} \cos \alpha}{\mathrm{f}}$
Therefore, total no. of values of $\mathrm{r}=33$.

</details>

---

