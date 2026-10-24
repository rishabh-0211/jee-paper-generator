# JEE Advanced Mathematics - Matrices

## Topic 1: Formation and Basic of Matrix

**Total Questions:** 2

---

### Q1. JEE Advanced 2023 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mn>3</mn></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mn>2</mn></mtd><mtd><mi>d</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>:</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>0</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>,</mo><mn>13</mn><mo>,</mo><mn>17</mn><mo>,</mo><mn>19</mn></mrow></mfenced></mrow></mfenced></math>. Then the number of invertible matrices in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3780**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mn>3</mn></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mn>2</mn></mtd><mtd><mi>d</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>R</mi><mo>|</mo><mo>=</mo><mo>-</mo><mn>5</mn><mfenced close="|" open="|"><mtable columnalign="left center"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math></p><p>We know that, for invertible matrices <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>R</mi></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>R</mi><mo>|</mo></math> can be zero in following cases:</p><p>(i) Two of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></math> are zeroes which can be (<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>),(<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>),(<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>) or (<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mn>4</mn><mo>&#215;</mo><msup><mn>7</mn><mn>2</mn></msup><mtext>&#160;ways&#160;</mtext><mo>=</mo><mn>196</mn></math></p><p>(ii) Any three of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></math> are zeroes</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>&#215;</mo><mn>7</mn><mo>=</mo><mn>28</mn></math></p><p>(iii) All four of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></math> are zeroes</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mn>1</mn></math></p><p>(iv) All four of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></math> are non-zero but same number</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mn>7</mn></math></p><p>(v) When two are alike and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> other are alike (non-zero)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mn>7</mn><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>84</mn></math></p><p>Number of invertible matrices</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>8</mn><mn>4</mn></msup><mo>-</mo><mn>196</mn><mo>-</mo><mn>28</mn><mo>-</mo><mn>1</mn><mo>-</mo><mn>7</mn><mo>-</mo><mn>84</mn><mo>=</mo><mn>3780</mn></math></p></blockquote>

</details>

---

### Q2. JEE Advanced 2011 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\omega \neq 1$ be a cube root of unity and $S$ be the set of all non-singular matrices of the form $\left[\begin{array}{ccc}1 & a & b \\ \omega & 1 & c \\ \omega^2 & \omega & 1\end{array}\right]$, where each of $a, b$ and $c$ is either $\omega$ or $\omega^2$. Then, the number of distinct matrices in the set $S$ is

**Options:**

- **(A)** 2
- **(B)** 6
- **(C)** 4
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

$|A| \neq 0$, as non-singular.
$$
\begin{aligned}
& \therefore \quad\left|\begin{array}{ccc}
1 & a & b \\
\omega & 1 & c \\
\omega^2 & \omega & 1
\end{array}\right| \neq 0 \\
& \Rightarrow \quad 1(1-c \omega)-a\left(\omega-c \omega^2\right) \\
& +b\left(\omega^2-\omega^2\right) \neq 0 \\
& \Rightarrow \quad 1-c \omega-a \omega+a c \omega^2 \neq 0 \\
&
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow \quad(1-c \omega)(1-a \omega) \neq 0 \\
& \Rightarrow \quad a \neq \frac{1}{\omega}, c \neq \frac{1}{\omega} \Rightarrow a=\omega, c=\omega
\end{aligned}
$$
and $b \in\left\{\omega, \omega^2\right\} \Rightarrow 2$ solutions

</details>

---

