# BITSAT Mathematics - Binomial Theorem

## Topic 1: Terms of Binomial Expansion

**Total Questions:** 18

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `3`

The coefficient of $x^n$ in the expansion of $\frac{e^{7 x}+e^x}{e^{3 x}}$ is

**Options:**

- **(A)** $\frac{4^{n-1}+(-2)^n}{n!}$
- **(B)** $\frac{4^{n-1}+2^n}{n!}$
- **(C)** $\frac{4^n+(-2)^n}{n!}$
- **(D)** $\frac{4^{n-1}+(-2)^{n-1}}{n!}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4^n+(-2)^n}{n!}$**

**Detailed Solution:**

Given, $\frac{e^{7 x}+e^x}{e^{3 x}} \Rightarrow e^{4 x}+e^{-2 x}$
Series of $e^a=1+\frac{a}{1!}+\frac{a^2}{2!}+\frac{a^3}{3!} \ldots$
$\begin{aligned}
\Rightarrow e^{4 x}+ & e^{-2 x}=\left(1+\frac{4 x}{1!}+\frac{(4 x)^2}{2!}+\frac{(4 x)^3}{3!}+\ldots\right) \\
& +\left(1+\frac{(-2 x)}{1!}+\frac{(-2 x)^2}{2!}+\ldots \ldots\right)
\end{aligned}$
Here, coefficient of
$\begin{aligned}
& x^2 \equiv \frac{4^2}{2!}+\frac{(-2)^2}{2!} \\
& x^3  \equiv \frac{4^3}{3!}+\frac{(-2)^3}{3!} \\
& \vdots \\
& x^n=\frac{4^n}{n!}+\frac{(-2)^n}{n!}
\end{aligned}$

</details>

---

### Q2. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `1`

The coefficient of $x^2$ term in the binomial expansion of $\left(\frac{1}{3} x^{\frac{1}{2}}+x^{\frac{-1}{4}}\right)^{10}$ is

**Options:**

- **(A)** $\frac{70}{243}$
- **(B)** $\frac{60}{423}$
- **(C)** $\frac{50}{13}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{70}{243}$**

**Detailed Solution:**

General term of given binomial expansion is
$\begin{aligned}
T_{r+1} & ={ }^{10} C_r\left(\frac{1}{3} x^{\frac{1}{2}}\right)^{10-r}\left(x^{-\frac{1}{4}}\right)^r \\
& ={ }^{10} C_r \times\left(\frac{1}{3}\right)^{10-r} x^{\frac{10-r}{2}-\frac{r}{4}}
\end{aligned}$
We have to find coefficient of $x^2$
$\begin{aligned}
\frac{10-r}{2}-\frac{r}{4} & =2 \Rightarrow r=4 \\
\Rightarrow \quad T_{4+1} & ={ }^{10} C_4\left(\frac{1}{3}\right)^6 x^2 \\
\therefore \text { Coefficient of } x^2 & ={ }^{10} C_4\left(\frac{1}{3}\right)^6 \\
& =\frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} \times \frac{1}{3^6}=\frac{70}{243}
\end{aligned}$

</details>

---

### Q3. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

The coefficient of the highest power of $x$ in the expansion of 
$\left(x+\sqrt{x^2-1}\right)^8+\left(x-\sqrt{x^2-1}\right)^8$

**Options:**

- **(A)** $64$
- **(B)** $128$
- **(C)** $256$
- **(D)** $512$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $256$**

**Detailed Solution:**

Since $\left(x+\sqrt{x^2-1}\right)^8+\left(x-\sqrt{x^2-1}\right)^8$
$\begin{array}{r}=2\left\{{ }^8 C_0 x^8+{ }^8 C_2 x^6\left(x^2-1\right)+{ }^8 C_4 x^4\left(x^2-1\right)^2\right. \\ \left.+{ }^8 C_6 x^2\left(x^2-1\right)^3+{ }^8 C_8 x^0\left(x^2-1\right)^4\right\}\end{array}$
So coefficient of highest power of $x$
$=2\left\{{ }^8 C_0+{ }^8 C_2+{ }^8 C_4+{ }^8 C_6+{ }^8 C_8\right\}$
$=(1+1)^8+(1-1)^8=2^8=256$

</details>

---

### Q4. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x^{18}$ occurs in the rth term in the expansion of $\left(x^4+\frac{1}{x^3}\right)^{15}$, then what is the value of $r$ ?

**Options:**

- **(A)** 3
- **(B)** 5
- **(C)** 7
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7**

**Detailed Solution:**

In the expansion of $\left(x^4+\frac{1}{x^3}\right)^{15}$, let $T_r$ is the $r^{\text {th }}$ term
$\begin{aligned}
T_r & ={ }^{15} C_{r-1}\left(x^4\right)^{15-r+1}\left(\frac{1}{x^3}\right)^{r-1} \\
& ={ }^{15} C_{r-1} x^{64-4 r-3 r+3}=15_{C_{r-1}} x^{67-7 r}
\end{aligned}$
$\mathrm{x}^{18}$ occurs in this term
$\Rightarrow 18=67-7 r \Rightarrow 7 r=49 \Rightarrow r=7 .$

</details>

---

### Q5. BITSAT 2023 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

The middle term in the expansion of $\left(\frac{10}{x}+\frac{x}{10}\right)^{10}$ is

**Options:**

- **(A)** ${ }^{10} \mathrm{C}_5$
- **(B)** ${ }^{10} \mathrm{C}_6$
- **(C)** ${ }^{10} \mathrm{C}_5 \frac{1}{x^{10}}$
- **(D)** ${ }^{10} \mathrm{C}_5 \mathrm{x}^{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) ${ }^{10} \mathrm{C}_5$**

**Detailed Solution:**

General term $=T_{r+1}$
$={ }^{10} \mathrm{C}_r\left(\frac{10}{x}\right)^{10-r}\left(\frac{x}{10}\right)^r$
Here $n=10$, which is an even number.
Now, $\left[\frac{10}{2}+1\right]^{\text {th }}$ term i.e. $6^{\text {th }}$ term is the middle term.
Hence, middle term $=T_6$
$\mathrm{T}_{5+1}={ }^{10} \mathrm{C}_5\left(\frac{10}{x}\right)^{10-5}\left(\frac{x}{10}\right)^5$
$={ }^{10} \mathrm{C}_5\left(\frac{10}{x}\right)^5\left(\frac{x}{10}\right)^5={ }^{10} \mathrm{C}_5$.

</details>

---

### Q6. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `2`

If the sum of the coefficients in the expansion of $(x+y)^n$ is 1024 , then the value of the greatest coefficient in the expansion is

**Options:**

- **(A)** $356$
- **(B)** $252$
- **(C)** $210$
- **(D)** $120$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $252$**

**Detailed Solution:**

Given, sum of the coefficient $=1024$
$\begin{array}{ll}\text { i.e. } & 2^n=1024=2^{10} \\ \Rightarrow & n=10\end{array}$
Since, $n$ is even, so greatest coefficient
$={ }^n C_{n / 2}={ }^{10} C_5=252$

</details>

---

### Q7. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `3`

The number of terms in the expansion of $(1+5 \sqrt{2} x)^9+(1-5 \sqrt{2} x)^9$, is

**Options:**

- **(A)** 5
- **(B)** 7
- **(C)** 9
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 5**

**Detailed Solution:**

We have,
$(1+5 \sqrt{2} x)^9+(1-5 \sqrt{2} x)^9$
$=2\left\{{ }^2 C_0+{ }^9 C_2(5 \sqrt{2} x)^2+\ldots+{ }^9 C_8(5 \sqrt{2} x)^8\right\}$
Clearly, it has 5 terms.

</details>

---

### Q8. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `2`

Coefficient of $x^{13}$ in the expansion of $(1-x)^{5}\left(1+x+x^{2}+x^{3}\right)^{4}$ is

**Options:**

- **(A)** 4
- **(B)** 6
- **(C)** 32
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 4**

**Detailed Solution:**

Expression $=(1-x)^{5} \cdot(1+x)^{4}\left(1+x^{2}\right)^{4}$

$\begin{array}{l}

=(1-x)\left(1-x^{2}\right)^{4}\left(1+x^{2}\right)^{4} \\

=(1-x)\left(1-x^{4}\right)^{4}

\end{array}$

$\therefore$ Coefficient of $x^{13}=-{ }^{4} \mathrm{C}_{3}(-1)^{3}=4$

</details>

---

### Q9. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `1`

The coefficient of the term independent of $x$ in the expansion of $\left(\sqrt{\frac{x}{3}}+\frac{3}{2 x^{2}}\right)^{10}$ is

**Options:**

- **(A)** $\frac{5}{4}$
- **(B)** $\frac{7}{4}$
- **(C)** $\frac{9}{4}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{5}{4}$**

**Detailed Solution:**

The $(r+1)$ th term in the expansion of $\left(\sqrt{\frac{x}{3}}+\frac{3}{2 x^{2}}\right)^{10}$ is given by

$\begin{array}{l}

\mathrm{T}_{r+1}={ }^{10} \mathrm{C}_{r}\left(\sqrt{\frac{x}{3}}\right)^{10-r}\left(\frac{3}{2 x^{2}}\right)^{r} \\

={ }^{10} \mathrm{C}_{r} \frac{x^{5-\left(\frac{r}{2}\right)}}{3^{5-\left(\frac{r}{2}\right)}} \cdot \frac{3^{r}}{2^{r} x^{2 r}} \\

={ }^{10} \mathrm{C}_{r} \frac{3^{\left(\frac{3 r}{2}\right)-5}-5-\left(\frac{5 r}{2}\right)}{2^{r}} x

\end{array}$

$\mathrm{T}_{r+1}={ }^{10} \mathrm{C}_{r}\left(\sqrt{\frac{x}{3}}\right)^{10-r}\left(\frac{3}{2 x^{2}}\right)^{r}$ $={ }^{10} \mathrm{C}_{r} \frac{x^{5-\left(\frac{r}{2}\right)}}{3} \cdot \frac{3^{r}}{2^{r} x^{2 r}}$ $={ }^{10} \mathrm{C}_{r} \frac{3^{\left(\frac{3 r}{2}\right)-5}-\left(\frac{5}{2}\right)-\left(\frac{5 r}{2}\right)}{2^{r}} x$ For $\mathrm{T}_{r+1}$ to be independent of $x$, we must have $5-\left(\frac{5 r}{2}\right)=0$ or $r=2$.

Thus, the 3 rd term is independent of $x$ and is equal to ${ }^{10} \mathrm{C}_{2} \frac{3^{3-5}}{2^{2}}=\frac{10 \times 9}{2} \times \frac{3^{-2}}{4}=\frac{5}{4}$

</details>

---

### Q10. BITSAT 2019

*Type:* `singleCorrect` | *Level:* `2`

If the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>18</mn></msup></math> in powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> are both zero, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>16</mn><mo>,</mo><mfrac><mn>251</mn><mn>3</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>14</mn><mo>,</mo><mfrac><mn>251</mn><mn>3</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>14</mn><mo>,</mo><mfrac><mn>272</mn><mn>3</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>16</mn><mo>,</mo><mfrac><mn>272</mn><mn>3</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>16</mn><mo>,</mo><mfrac><mn>272</mn><mn>3</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>We have, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>18</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><mn>2</mn><mi>x</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mn>4</mn></msup><mo>&#8230;</mo></mrow></mfenced></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><msup><mfenced><mn>2</mn></mfenced><mn>3</mn></msup><mo>+</mo><mi>a</mi><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><msup><mfenced><mn>2</mn></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>18</mn></msup><msub><mi>C</mi><mn>1</mn></msub><mfenced><mn>2</mn></mfenced></math></p><p>and coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><msup><mfenced><mn>2</mn></mfenced><mn>4</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><msup><mfenced><mn>2</mn></mfenced><mn>3</mn></msup><mi>a</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><msup><mfenced><mn>2</mn></mfenced><mn>2</mn></msup><mi>b</mi></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup></math> are zero.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><msup><mfenced><mn>2</mn></mfenced><mn>3</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><msup><mfenced><mn>2</mn></mfenced><mn>2</mn></msup><mfenced><mi>a</mi></mfenced><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><mfenced><mn>2</mn></mfenced><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mrow><mn>4</mn><mo>&#215;</mo><mn>17</mn><mo>&#215;</mo><mn>16</mn></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>2</mn></mrow></mfrac><mo>-</mo><mn>17</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn></math>    <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn><mo>-</mo><mfrac><mn>32</mn><mn>3</mn></mfrac><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Solving Eqs. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>ii</mi><mo>)</mo></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>16</mn><mo>,</mo><mi>b</mi><mo>=</mo><mfrac><mn>272</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q11. BITSAT 2018

*Type:* `singleCorrect` | *Level:* `2`

The greatest term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mrow></mfenced><mn>20</mn></msup></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>26840</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>24840</mn><mn>9</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25840</mn><mn>9</mn></mfrac></math>
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25840</mn><mn>9</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mn>3</mn></msqrt><msup><mo>&#183;</mo><mn>20</mn></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mi>r</mi></msup></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>r</mi></msub><mo>=</mo><msqrt><mn>3</mn></msqrt><msup><mo>&#183;</mo><mn>20</mn></msup><msub><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub><msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><msub><mi>T</mi><mi>r</mi></msub></mfrac><mo>=</mo><mfrac><mrow><mn>20</mn><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mi>r</mi></mfrac><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>&#8805;</mo><msub><mi>T</mi><mi>r</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>20</mn><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn><mo>&#8805;</mo><msqrt><mn>3</mn></msqrt><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>&#8804;</mo><mfrac><mn>21</mn><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>21</mn><mrow><mn>2</mn><mo>.</mo><mn>73</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>&#8804;</mo><mn>7</mn><mo>.</mo><mn>692</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> The greatest term is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>8</mn></msub><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>7</mn><none/><mprescripts/><none/><mn>20</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mn>7</mn></msup><mo>=</mo><mfrac><mn>25840</mn><mn>9</mn></mfrac></math></p>

</details>

---

### Q12. BITSAT 2018

*Type:* `singleCorrect` | *Level:* `2`

The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mi>n</mi></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>n</mi></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mi>n</mi></msup></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>n</mi></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>n</mi></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mi>n</mi></msup><mo>=</mo><msup><mfenced close="]" open="["><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced></mrow></mfenced><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>n</mi></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mi>n</mi></msup><mo>=</mo><msup><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>n</mi></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mi>n</mi></msup><mo>=</mo><msup><mfenced close="]" open="["><mrow><mfenced><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>n</mi></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>n</mi></msup><mo>&#183;</mo><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>&#183;</mo><msup><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mn>1</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>&#183;</mo><mfrac><mn>1</mn><msup><mi>x</mi><mi>n</mi></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mi>n</mi></mrow></msup><mo>=</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q13. BITSAT 2017

*Type:* `singleCorrect` | *Level:* `2`

The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>5</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>21</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>22</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>30</mn></msup></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mn>51</mn></mmultiscripts></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mn>9</mn></mmultiscripts></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>6</mn><none/><mprescripts/><none/><mn>31</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>6</mn><none/><mprescripts/><none/><mn>21</mn></mmultiscripts></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mn>30</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mn>20</mn></mmultiscripts></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>6</mn><none/><mprescripts/><none/><mn>31</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>6</mn><none/><mprescripts/><none/><mn>21</mn></mmultiscripts></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>21</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>22</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>30</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>21</mn></msup><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>1</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>9</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>21</mn></msup><mfenced open="[" close="]"><mfrac><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mfenced open="[" close="]"><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>31</mn></msup><mo>-</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>21</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>5</mn></msup></math> in the given expression</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>5</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>x</mi></mfrac><mfenced open="[" close="]"><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>31</mn></msup><mo>-</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>21</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>6</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>31</mn></msup><mo>-</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>21</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>31</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>21</mn></mmultiscripts></math></p>

</details>

---

### Q14. BITSAT 2013

*Type:* `singleCorrect` | *Level:* `1`

The coefficient of the middle term in the expansion of $(2+3 \mathrm{x})^{4}$ is:

**Options:**

- **(A)** 6
- **(B)** $5 !$
- **(C)** $8 !$
- **(D)** 216

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 216**

**Detailed Solution:**

When exponent is $n$ then total number of terms are $\mathrm{n}+1 .$ So, total number of terms in $(2+3 x)^{4}=5$

Middle term is 3rd. $\Rightarrow \mathrm{T}_{3}={ }^{4} \mathrm{C}_{2}(2)^{2} \cdot(3 \mathrm{x})^{2}$

$$

=\frac{4 \times 3 \times 2 \times 1}{2 \times 1 \times 2} \times 4 \times 9 \mathrm{x}^{2}=216 \mathrm{x}^{2}

$$

</details>

---

### Q15. BITSAT 2011

*Type:* `singleCorrect` | *Level:* `2`

In the binomial \(\left(2^{1 / 3}+3^{-1 / 3}\right)^{\mathrm{n}}\), if the ratio of the seventh term from the beginning of the expansion to the seventh term from its end is \(1 / 6\), then \(n\) equal to

**Options:**

- **(A)** 6
- **(B)** 9
- **(C)** 12
- **(D)** 15

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 9**

**Detailed Solution:**

\(\mathrm{T}_{\mathrm{r}+1}={ }^{\mathrm{n}} \mathrm{C}_{\mathrm{r}} a^{\mathrm{n}-\mathrm{r}} \cdot \mathrm{b}^{\mathrm{r}}\) where \(\mathrm{a}=2^{1 / 3}\) and \(\mathrm{b}=3^{-1 / 3}\)
\(\mathrm{T}_7\) from beginning \(={ }^n \mathrm{C}_6 a^{\mathrm{n}-6} \mathrm{~b}^6\) and \(\mathrm{T}_7\) from end \(={ }^{\mathrm{n}} \mathrm{C}_6 \quad \mathrm{~b}^{\mathrm{n}-6} \quad \mathrm{a}^6\)
\(\begin{aligned}
& \Rightarrow \frac{\mathrm{a}^{\mathrm{n}-12}}{\mathrm{~b}^{\mathrm{n}-12}}=\frac{1}{6} \Rightarrow 2^{\frac{\mathrm{n}-12}{3}} \cdot 3^{\frac{\mathrm{n}-12}{3}}=6^{-1} \\
& \Rightarrow \mathrm{n}-12=-3 \Rightarrow \mathrm{n}=9
\end{aligned}\)

</details>

---

### Q16. BITSAT 2011

*Type:* `singleCorrect` | *Level:* `2`

The term independent of \(x\) in the expansion of \(\left(9 \mathrm{x}-\frac{1}{3 \sqrt{\mathrm{x}}}\right)^{18}, \mathrm{x} > 0\), is a times the corresponding binomial coefficient. Then a is

**Options:**

- **(A)** 3
- **(B)** \(1 / 3\)
- **(C)** \(-1 / 3\)
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) None of these**

**Detailed Solution:**

\(\begin{aligned}
\mathrm{T}_{\mathrm{r}+1} & ={ }^{18} \mathrm{C}_{\mathrm{r}}(9 \mathrm{x})^{18-\mathrm{r}}\left(-\frac{1}{3 \sqrt{\mathrm{x}}}\right)^{\mathrm{r}} \\
& =(-\mathrm{r})^{\mathrm{r}}{ }^{18} \mathrm{C}_{\mathrm{r}} 9^{18-\frac{3 \mathrm{r}}{2}} \mathrm{x}^{18-\frac{3 \mathrm{r}}{2}}
\end{aligned}\)
is independent of \(\mathrm{x}\) provided \(\mathrm{r}=12\) and then \(\mathrm{a}=1\).

</details>

---

### Q17. BITSAT 2010

*Type:* `singleCorrect` | *Level:* `1`

With 17 consonants and 5 vowels the number of words of four letters that can be formed having two different vowels in the middle and one consonant, repeated or different at each end is

**Options:**

- **(A)** 5780
- **(B)** 2890
- **(C)** 5440
- **(D)** 2720

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 5780**

**Detailed Solution:**

The two letters, the first and the last of the four lettered word can be chosen in \((17)^2\) ways, as repetition is allowed for consonants. The two vowels in the middle are distinct so that the number of ways of filling up the two places is \({ }^5 \mathrm{P}_2=20\).
The no. of different words \(=(17)^2 \cdot 20=5780\).

</details>

---

### Q18. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `1`

The letters of the word TOUGH are written in all possible orders and these words are written out as in a dictionary, then the rank of the word TOUGH is

**Options:**

- **(A)** 120
- **(B)** 88
- **(C)** 89
- **(D)** 90

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 89**

**Detailed Solution:**

\(\begin{aligned}
& \text { Rank }=(4 ! \times 3)+(3 ! \times 2)+(2 ! \times 2)+1 \\
& =72+12+4+1=89
\end{aligned}\)

</details>

---

