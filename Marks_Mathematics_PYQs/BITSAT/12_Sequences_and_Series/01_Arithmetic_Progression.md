# BITSAT Mathematics - Sequences and Series

## Topic 1: Arithmetic Progression

**Total Questions:** 11

---

### Q1. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `1`

If $\alpha, \beta, \gamma \in[0, \pi]$ and if $\alpha, \beta, \gamma$ are in AP, then 
$\frac{\sin \alpha-\sin \gamma}{\cos \gamma-\cos \alpha}$ is equal to

**Options:**

- **(A)** $\sin \beta$
- **(B)** $\cos \beta$
- **(C)** $\cot \beta$
- **(D)** $2 \cos \beta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\cot \beta$**

**Detailed Solution:**

$\frac{\sin \alpha-\sin \gamma}{\cos \gamma-\cos \alpha}=\frac{2 \cos \frac{\alpha+\gamma}{2} \sin \frac{\alpha-\gamma}{2}}{2 \sin \frac{\alpha+\gamma}{2} \cdot \sin \frac{\alpha-\gamma}{2}}$
$=\cot \frac{\alpha+\gamma}{2}$
$\left[\begin{array}{l}\because \sin A-\sin B=2 \cos \left(\frac{A+B}{2}\right) \sin \left(\frac{A-B}{2}\right) \\ \text { and } \cos A-\cos B=2 \sin \left(\frac{A+B}{2}\right) \sin \left(\frac{B-A}{2}\right)\end{array}\right]$
But $\alpha, \beta, \gamma$ are in $AP$
$\Rightarrow \quad \frac{\alpha+\gamma}{2}=\beta$
So, required value is $\cot \beta$.

</details>

---

### Q2. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `1`

If the harmonic mean between $a$ and $b$ be $H$, then the value of $\frac{1}{\mathrm{H}-a}+\frac{1}{\mathrm{H}-b}$ is

**Options:**

- **(A)** $a+b$
- **(B)** $a b$
- **(C)** $\frac{1}{a}+\frac{1}{b}$
- **(D)** $\frac{1}{a}-\frac{1}{b}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{a}+\frac{1}{b}$**

**Detailed Solution:**

Putting $\mathrm{H}=\frac{2 a b}{a+b}$, we have

$\begin{array}{l}

\frac{1}{\mathrm{H}-a}+\frac{1}{\mathrm{H}-b} \\

=\frac{1}{\left(\frac{2 a b}{a+b}-a\right)}+\frac{1}{\left(\frac{2 a b}{a+b}-b\right)}=\frac{a+b}{a b-a^{2}}+\frac{a+b}{a b-b^{2}}

\end{array}$

$=\left(\frac{a+b}{b-a}\right)\left(\frac{1}{a}-\frac{1}{b}\right)=\left(\frac{a+b}{b-a}\right)\left(\frac{b-a}{a b}\right)=\frac{a+b}{a b}=\frac{1}{a}+\frac{1}{b}$

</details>

---

### Q3. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `2`

The sum of all odd numbers between 1 and 1000 which are divisible by 3 is

**Options:**

- **(A)** 83667
- **(B)** 90000
- **(C)** 83660
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 83667**

**Detailed Solution:**

Sum of odd numbers between 1 and 1000 , which is divisible by $3=3+9+15+21+27+\ldots+999=\mathrm{S}$ (let)

$\therefore$ Let $\mathrm{n}$ be the number of terms in series and $\mathrm{a}$ is first term.

$\therefore l=a+(n-1) d$,

where $l$ is last term and $d$ is is common difference.

$\begin{array}{l}

999=3+(n-1) \times 6 \\

n-1=\frac{999-3}{6}=\frac{996}{6} \\

\Rightarrow n-1=166 \\

\Rightarrow n=167 \\

\therefore \mathrm{S}=\frac{n}{2}[2 a+(n-1) d] \\

=\frac{167}{2}[2 \times 3+(167-1) \times 6] \\

=\frac{167}{2}[1002]=167 \times 501=83667

\end{array}$

</details>

---

### Q4. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `1`

If the sum of a certain number of terms of the A.P. $25,22,19, \ldots$ is 116 then the last term is

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** 4
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

$a=25, d=22-25=-3 \text {. }$

Let $n$ be the no. of terms

$\begin{array}{l}

\text { Sum }=116 ; \\

\text { Sum }=\frac{n}{2}[2 a+(n-1) d] \\

116=\frac{n}{2}[50+(n-1)(-3)] \\

\text { or } 232=n[50-3 n+3]=n[53-3 n]=-3 n^{2}+53 n \\

\Rightarrow 3 n^{2}-53+232=0 \\

\Rightarrow(n-8)(3 n-29)=0 \\

\Rightarrow n=8 \text { or } n=\frac{29}{3}, \\

n \neq \frac{29}{3} \\

\therefore n=8 \\

\therefore \text { Now, } \mathrm{T}_{8}=a+(8-1) d=25+7 \times(-3)=25-21=4 \\

\therefore \text { Last term }=4

\end{array}$

</details>

---

### Q5. BITSAT 2020

*Type:* `singleCorrect` | *Level:* `1`

A student read common difference of an A. P. as

-2 instead of 2 and got the sum of first 5 terms as -5 . Actual sum of first five terms is

**Options:**

- **(A)** 25
- **(B)** -25
- **(C)** -35
- **(D)** 35

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 35**

**Detailed Solution:**

$\frac{5}{2}\{2 \mathrm{a}+4(-2)\}=-5 \Rightarrow 2 \mathrm{a}=6$

$\therefore$ Actual sum $=\frac{5}{2}\{6+4(2)\}=35$

</details>

---

### Q6. BITSAT 2017

*Type:* `singleCorrect` | *Level:* `2`

The numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>,</mo><mn>14</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mn>4</mn><mo>-</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mrow></msup></math> form first three terms of an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math>, then its fifth term is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>25</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>53</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>53</mn></math>**

**Detailed Solution:**

<p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>,</mo><mn>14</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mn>4</mn><mo>-</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mrow></msup></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AP</mi></math>. Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>14</mn><mo>=</mo><msup><mn>3</mn><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mn>3</mn><mrow><mn>4</mn><mo>-</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>28</mn><mo>=</mo><mfrac><mi>a</mi><mn>3</mn></mfrac><mo>+</mo><mfrac><msup><mn>3</mn><mn>4</mn></msup><mi>a</mi></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><msup><mn>3</mn><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>84</mn><mi>a</mi><mo>+</mo><mn>243</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mn>81</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mn>81</mn><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mn>3</mn><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mrow></msup><mo>=</mo><msup><mn>3</mn><mn>4</mn></msup></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mrow></msup><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>=</mo><mn>1</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><mo>&#160;</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>&#8800;</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>=</mo><mn>30</mn><mo>&#176;</mo><mo>&#160;&#160;</mo><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><mo>&#160;</mo><mi>sin</mi><mn>30</mn><mo>&#176;</mo><mo>=</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></mfenced></math></p><p>Thus, the first three terms of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AP</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>14</mn><mo>,</mo><mn>27</mn></math>.</p><p>Hence, its fifth term <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>5</mn></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mfenced><mrow><mn>5</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>13</mn><mo>=</mo><mn>1</mn><mo>+</mo><mn>52</mn><mo>=</mo><mn>53</mn></math></p>

</details>

---

### Q7. BITSAT 2016

*Type:* `singleCorrect` | *Level:* `1`

If $\log$ a, $\log \mathrm{b}$, and $\log \mathrm{c}$ are in A.P. and also $\log$ a $-\log 2 b, \log 2 b-\log 3 c, \log 3 c-\log$ a are in A.P.,

then

**Options:**

- **(A)** $\mathrm{a}, \mathrm{b}, \mathrm{c},$ are in $\mathrm{H.P.}$
- **(B)** $a, 2 b, 3 c$ are in A.P.
- **(C)** $\mathrm{a}, \mathrm{b}, \mathrm{c}$ are the sides of a triangle
- **(D)** none of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{a}, \mathrm{b}, \mathrm{c}$ are the sides of a triangle**

**Detailed Solution:**

\(\log \mathrm{a}, \log \mathrm{b}, \log \mathrm{c}\) are in A.P.

\(\begin{aligned}

&\Rightarrow 2 \log \mathrm{b}=\log \mathrm{a}+\log \mathrm{c} \\

&\Rightarrow \log \mathrm{b}^{2}=\log (\mathrm{ac}) \\

&\Rightarrow \mathrm{b}^{2}=\mathrm{ac} \Rightarrow \mathrm{a}, \mathrm{b}, \mathrm{c} \text { are in G.P. } \\

&\log \mathrm{a}-\log 2 \mathrm{~b}, \log 2 \mathrm{~b}-\log 3 \mathrm{c}, \log 3 \mathrm{c}-\log \text { a are in A.P. }

\end{aligned}\)

\(\Rightarrow 2(\log 2 b-\log 3 c)=(\log a-\log 2 b)+(\log 3 c-\log a)\)

\(\Rightarrow 3 \log 2 \mathrm{~b}=3 \log 3 \mathrm{c} \Rightarrow 2 \mathrm{~b}=3 \mathrm{c}\)

Now, \(b^{2}=a c \Rightarrow b^{2}=a \cdot \frac{2 b}{3} \Rightarrow b=\frac{2 a}{3}, c=\frac{4 a}{9}\)

\(\begin{aligned}

&\text { i.e., } a=a, b=\frac{2 a}{3}, c=\frac{4 a}{9} \\

&\Rightarrow a: b: c=1: \frac{2}{3}: \frac{4}{9}=9: 6: 4

\end{aligned}\)

Since, sum of any two is greater than the \(3^{\mathrm{rd}}, \mathrm{a}, \mathrm{b}, \mathrm{c}\) form a triangle.

</details>

---

### Q8. BITSAT 2016

*Type:* `singleCorrect` | *Level:* `2`

The fourth term of an A.P. is three times of the first term and the seventh term exceeds the twice of the third term by one, then the common difference of the progression is

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** $\frac{3}{2}$
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

Let the progression be $a$, $a+d$, a +2 d,

Then $x_{4}=3 x_{1} \Rightarrow a+3 d=3 a \Rightarrow 3 d=2 a \ldots$ (i)

Again $x_{7}=2 x_{3}+1$

$\Rightarrow a+6 d=2(a+2 d)+1 \Rightarrow 2 d=a+1 \quad \ldots$ (ii)

Solving (i) and (ii), we get $\mathrm{a}=3, \mathrm{~d}=2$

</details>

---

### Q9. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `2`

If $\frac{1}{\mathrm{a}}, \frac{1}{\mathrm{~b}}, \frac{1}{\mathrm{c}}$ are in A. P., then $\left(\frac{1}{\mathrm{a}}+\frac{1}{\mathrm{~b}}-\frac{1}{\mathrm{c}}\right) \left(\frac{1}{b}+\frac{1}{c}-\frac{1}{a}\right)$ is equal to

**Options:**

- **(A)** $\frac{4}{a c}-\frac{3}{b^{2}}$
- **(B)** $\frac{b^{2}-a c}{a^{2} b^{2} c^{2}}$
- **(C)** $\frac{4}{a c}-\frac{1}{b^{2}}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{4}{a c}-\frac{3}{b^{2}}$**

**Detailed Solution:**

$\frac{1}{\mathrm{a}}-\frac{1}{\mathrm{~b}}=\frac{1}{\mathrm{~b}}-\frac{1}{\mathrm{c}}$

$\therefore\left(\frac{1}{\mathrm{a}}+\frac{1}{\mathrm{~b}}-\frac{1}{\mathrm{c}}\right)\left(\frac{1}{\mathrm{~b}}+\frac{1}{\mathrm{c}}-\frac{1}{\mathrm{a}}\right)$

$=\left(\frac{2}{\mathrm{a}}-\frac{1}{\mathrm{~b}}\right)\left(\frac{2}{\mathrm{c}}-\frac{1}{\mathrm{~b}}\right)=\frac{4}{\mathrm{ac}}-\frac{1}{\mathrm{~b}}\left(\frac{2}{\mathrm{a}}+\frac{2}{\mathrm{c}}\right)+\frac{1}{\mathrm{~b}^{2}}$

$=\frac{4}{\mathrm{ac}}-\frac{2}{\mathrm{~b}}\left(\frac{2}{\mathrm{~b}}\right)+\frac{1}{\mathrm{~b}^{2}}=\frac{4}{\mathrm{ac}}-\frac{3}{\mathrm{~b}^{2}}$

</details>

---

### Q10. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `1`

Let $a_{1}, a_{2}, a_{3} \ldots \ldots \ldots \ldots .$ be terms on A.P. If
$\frac{a_{1}+a_{2}+\ldots \ldots \ldots a_{p}}{a_{1}+a_{2}+\ldots \ldots \ldots .+a_{q}}=\frac{p^{2}}{q^{2}}, p \neq q,$ then $\frac{a_{6}}{a_{21}}$
equals

**Options:**

- **(A)** $\frac{41}{11}$
- **(B)** $\frac{7}{2}$
- **(C)** $\frac{2}{7}$
- **(D)** $\frac{11}{41}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{11}{41}$**

**Detailed Solution:**

$\frac{\frac{p}{2}\left[2 a_{1}+(p-1) d\right]}{\frac{q}{2}\left[2 a_{1}+(q-1) d\right]}=\frac{p^{2}}{q^{2}}$
$\Rightarrow \frac{2 a_{1}+(p-1) d}{2 a_{1}+(q-1) d}=\frac{p}{q}$
$\frac{a_{1}+\left(\frac{p-1}{2}\right) d}{a_{1}+\left(\frac{q-1}{2}\right) d}=\frac{p}{q}$ For $\frac{a_{6}}{a_{21}}, \quad p=11, q=41$

</details>

---

### Q11. BITSAT 2011

*Type:* `singleCorrect` | *Level:* `2`

If the sum of the first \(2 n\) terms of \(2,5,8, \ldots \ldots\) is equal to the sum of the first \(n\) terms of 57,59 , \(61 \ldots \ldots\). , then \(\mathrm{n}\) is equal to

**Options:**

- **(A)** 10
- **(B)** 12
- **(C)** 11
- **(D)** 13

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 11**

**Detailed Solution:**

Given,
\(\frac{2 n}{2}\{2.2+(2 n-1) 3\}=\frac{n}{2}\{2.57+(n-1) 2\}\)
or \(2(6 n+1)=112+2 n\) or \(10 n=110, ~\therefore n=11\)

</details>

---

