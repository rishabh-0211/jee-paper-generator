# BITSAT Mathematics - Limits

## Topic 1: Existance of Limit

**Total Questions:** 7

---

### Q1. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

If $f(x)=\left\{\begin{array}{l}x^2-1,0 < x < 2 \\ 2 x+3,2 \leq x < 3\end{array}\right.$, then the quadratic equation whose roots are $\lim _{x \rightarrow 2^{-}} f(x)$ and $\lim _{x \rightarrow 2^{+}} f(x)$ is

**Options:**

- **(A)** $x^2-6 x+9=0$
- **(B)** $x^2-7 x+8=0$
- **(C)** $x^2-14 x+49=0$
- **(D)** $x^2-10 x+21=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x^2-10 x+21=0$**

**Detailed Solution:**

Since, $f(x)= \begin{cases}x^2-1, & 0 < x < 2 \\ 2 x+3, & 2 \leq x < 3\end{cases}$
Now, $\lim _{x \rightarrow 2^{-}} f(x)=\lim _{x \rightarrow 2^{-}}\left(x^2-1\right)$
$\begin{aligned}
& =\lim _{h \rightarrow 0}\left[(2-h)^2-1\right]=\lim _{h \rightarrow 0}\left[4+h^2-4 h-1\right] \\
& =\lim _{h \rightarrow 0}\left[h^2-4 h+3\right]=0-0+3=3
\end{aligned}$
and $\lim _{x \rightarrow 2^{+}} f(x)=\lim _{x \rightarrow 2^{+}}(2 x+3)$
$=\lim _{h \rightarrow 0}[2(2+h)+3]=\lim _{h \rightarrow 0}[4+2 h+3]=7$
Hence the quadratic equation whose roots are 3 and 7 is given by $x^2-(3+7) x+(3+7)=0 \Rightarrow x^2$ $-10 x+21=0$

</details>

---

### Q2. BITSAT 2023 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \frac{|\sin x|}{x}$ is equal to

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** Does not exist
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Does not exist**

**Detailed Solution:**

Let $l=\lim _{x \rightarrow 0} \frac{[\sin x]}{x} ; \mathrm{RHL}=\lim _{x \rightarrow 0^{+}} \frac{\sin x}{x}=1$
$\mathrm{LHL}=\lim _{x \rightarrow 0^{-}}\left(\frac{-\sin x}{x}\right)=-\left(\lim _{x \rightarrow 0^{-}} \frac{\sin x}{x}\right)=-1$
$\left[|x|=\begin{array}{c}x \text { if } x \geq 0 \\ -x \text { if } x \leq 0\end{array}\right]$
As, LHL $\neq$ RHL Hence, limit $l$.does not exist.

</details>

---

### Q3. BITSAT 2018

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>, so that <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mfenced><mrow><msup><mi>e</mi><mrow><mi>a</mi><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mfenced><mrow><msup><mi>e</mi><mrow><mi>a</mi><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mi>a</mi><msup><mi>e</mi><mrow><mi>a</mi><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math> (using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math>&#39;Hospital rule to the left hand side)</p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mn>0</mn></math>, the denominator is zero and as the value of the limit is finite so, numerator must be zero for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mn>0</mn></math>.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>2</mn></math>.</p>

</details>

---

### Q4. BITSAT 2017

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mi>a</mi><mi>n</mi><mo>-</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>b</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is finite number, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><mo>an</mo><mo>(</mo><mn>1</mn><mo>+</mo><mi>n</mi><mo>)</mo><mo>-</mo><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mo>&#8734;</mo></math>,</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>1</mn><mo>&#8800;</mo><mn>0</mn></math> limit does not exist and if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><mi>a</mi><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>a</mi><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mi>b</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q5. BITSAT 2017

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>sin</mi><mfenced open="[" close="]"><mrow><mi>&#960;</mi><msqrt><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8734;</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** does not exist
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>sin</mi><mfenced close="}" open="{"><mrow><mi>n</mi><mi>&#960;</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>sin</mi><mfenced open="{" close="}"><mrow><mi>n</mi><mi>&#960;</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>8</mn><msup><mi>n</mi><mn>4</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>sin</mi><mfenced close="}" open="{"><mrow><mi>n</mi><mi>&#960;</mi><mo>+</mo><mfrac><mi>&#960;</mi><mrow><mn>2</mn><mi>n</mi></mrow></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mrow><mn>8</mn><msup><mi>n</mi><mn>3</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><mi>sin</mi><mi>&#960;</mi><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>8</mn><msup><mi>n</mi><mn>3</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q6. BITSAT 2010

*Type:* `singleCorrect` | *Level:* `1`

Find the equation of chord of the circle \(x^2+y^2=8 x\) bisected at the point \((4,3)\)

**Options:**

- **(A)** \(y=3\)
- **(B)** \(y=1\)
- **(C)** \(y=6\)
- **(D)** \(y=7\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) \(y=3\)**

**Detailed Solution:**

\(\begin{aligned}
& \mathrm{T}=\mathrm{S}_1 \Rightarrow \mathrm{x}(4)+\mathrm{y}(3)-4(\mathrm{x}+4)=16+9-32 \\
& \Rightarrow 3 \mathrm{y}-9=0 \Rightarrow \mathrm{y}=3
\end{aligned}\)

</details>

---

### Q7. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `3`

Two tangents \(P Q\) and \(P R\) drawn to the circle \(x^2+y^2-2 x-4 y-20=0\) from point \(P(16,7)\). Ifthe centre of the circle is \(C\) then the area of quadrilateral \(\mathrm{PQCR}\) is

**Options:**

- **(A)** 75 sq. unit
- **(B)** 73 sq. unit
- **(C)** 72 sq. unit
- **(D)** 74 sq. unit

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 75 sq. unit**

**Detailed Solution:**

Area \(\mathrm{PQCR}=2~ \triangle ~\mathrm{PQC}=2 \times \frac{1}{2} \mathrm{~L} \times r\)
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/2MlwpK4A6CfMHiqk-ouZZSz-r8ZeW9skHwUpBdQRtt0.original.fullsize.png">

where \(\mathrm{L}=\) length of tangent and \(r=\) radius of circle.
\(\mathrm{L}=\sqrt{\mathrm{S}_1}=15 \text { and } \mathrm{r}=\sqrt{1+4+20}=5\)
Hence the required area \(=75\) sq. units.

</details>

---

