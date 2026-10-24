# JEE Main Mathematics - Binomial Theorem

## Topic 2: Remainder and Divisibility Problems

**Total Questions:** 28

---

### Q1. JEE Main 2025 (8 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

The product of the last two digits of $(1919)^{1919}$ is
$\qquad$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **63**

**Detailed Solution:**

$\begin{aligned} & (1919)^{1919}=(1920-1)^{1919} \\ & ={ }^{1919} \mathrm{C}_0(1920)^{1919}-{ }^{1919} \mathrm{C}_1(1920)^{1918}+\ldots . \\ & +{ }^{1919} \mathrm{C}_{1918}(1920)^1-{ }^{1919} \mathrm{C}_{1919} \\ & =100 \lambda+1919 \times 1920-1 \\ & =100 \lambda+3684480-1 \\ & =100 \lambda+\ldots \ldots \ldots . .79 \text { (last two digit) } \\ & \Rightarrow \text { Number having last two digit } 79 \\ & \therefore \text { Product of last two digit } 63\end{aligned}$

</details>

---

### Q2. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The remainder when $\left((64)^{(64)}\right)^{(64)}$ is divided by 7 is equal to

**Options:**

- **(A)** 4
- **(B)** 1
- **(C)** 3
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

Let $\mathrm{N}=\left((64)^{64}\right)^{64}$
$\mathbf{N}=(64)^{64^2}$
$\mathbf{N}=(1+63)^{64^2}, \text { let } 64^2=\mathrm{n}$

Expanding by binomial
$\begin{aligned}
& \mathrm{N}=(1+63)^{\mathrm{n}}=1+{ }^{\mathrm{n}} \mathrm{C}_1 63+{ }^{\mathrm{n}} \mathrm{C}_2(63)^2+\ldots . \\
& =1+63 \lambda=1+7(9 \lambda)
\end{aligned}$

Remainder when divided by 7 is 1

</details>

---

### Q3. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The remainder, when $7^{103}$ is divided by 23 , is equal to :

**Options:**

- **(A)** 6
- **(B)** 17
- **(C)** 9
- **(D)** 14

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 14**

**Detailed Solution:**

$\begin{aligned}
& 7^{103}=7\left(7^{102}\right)=7(343)^{34}=7(345-2)^{34} \\
& 7^{103}=23 \mathrm{~K}_1+7.2^{34}
\end{aligned}$

Now $7.2^{34}=7.2^2 \cdot 2^{32}$
$\begin{aligned}
& =28 \cdot(256)^4 \\
& =28(253+3)^4 \\
& \therefore 28 \times 81 \Rightarrow(23+5)(69+12) \\
& 23 \mathrm{~K}_2+60 \\
& \therefore \text { Remainder }=14
\end{aligned}$

</details>

---

### Q4. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

The remainder when $428^{2024}$ is divided by 21 is__________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

$\begin{aligned}
& (428)^{2024}=(420+8)^{2024} \\
& =(21 \times 20+8)^{2024} \\
& =21 \mathrm{~m}+8^{2024}
\end{aligned}$
Now $8^{2024}=\left(8^2\right)^{1012}$
$\begin{aligned}
& =(64)^{1012} \\
& =(63+1)^{1012} \\
& =(21 \times 3+1)^{1012} \\
& =2 \ln +1
\end{aligned}$
$\Rightarrow$ Remainder is 1.

</details>

---

### Q5. JEE Main 2024 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

Remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>64</mn><msup><mn>32</mn><mn>32</mn></msup></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>64</mn><msup><mn>32</mn><mn>32</mn></msup></msup><mo>=</mo><msup><mfenced><mrow><mn>63</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mn>32</mn><mo>×</mo><mn>32</mn><mo>×</mo><mn>32</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>32</mn><mtext>times</mtext></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mn>64</mn><msup><mn>32</mn><mn>32</mn></msup></msup><mo>=</mo><msup><mfenced><mrow><mn>63</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mn>32</mn><mi>λ</mi></mrow></msup></math></p><p>Now we know that by binomial theorem,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>63</mn></mrow></mfenced><mrow><mn>32</mn><mi>λ</mi></mrow></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><msup><mrow></mrow><mrow><mn>32</mn><mi>λ</mi></mrow></msup></mmultiscripts><mo>·</mo><mn>1</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><msup><mrow></mrow><mrow><mn>32</mn><mi>λ</mi></mrow></msup></mmultiscripts><mo>·</mo><mn>1</mn><mo>·</mo><mn>63</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><msup><mrow></mrow><mrow><mn>32</mn><mi>λ</mi></mrow></msup></mmultiscripts><mo>·</mo><mn>1</mn><mo>·</mo><msup><mn>63</mn><mn>2</mn></msup><mo>+</mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>63</mn></mrow></mfenced><mrow><mn>32</mn><mi>λ</mi></mrow></msup><mo>=</mo><mn>1</mn><mo>+</mo><mn>9</mn><mi>α</mi></math></p><p>So, when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>64</mn><msup><mn>32</mn><mn>32</mn></msup></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> as remainder.</p>

</details>

---

### Q6. JEE Main 2023 (13 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

The remainder, when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mn>103</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn><mo>,</mo></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<blockquote><p>Using the binomial expansion in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mn>103</mn></msup><mo>=</mo><msup><mfenced><msup><mn>7</mn><mn>2</mn></msup></mfenced><mn>51</mn></msup><mo>&#183;</mo><mn>7</mn><mo>=</mo><msup><mfenced><mrow><mn>51</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mn>51</mn></msup><mo>&#183;</mo><mn>7</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>51</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mn>51</mn></msup><mo>&#183;</mo><mn>7</mn><mo>=</mo><mn>7</mn><mo>&#183;</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><msup><mn>51</mn><mn>51</mn></msup><mo>&#183;</mo><msup><mn>2</mn><mn>0</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><msup><mn>51</mn><mn>50</mn></msup><mo>&#183;</mo><msup><mn>2</mn><mn>1</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>51</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts><msup><mn>2</mn><mn>51</mn></msup></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>51</mn></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>, so when above equation is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>&#183;</mo><mfenced><mrow><mo>-</mo><msup><mn>2</mn><mn>51</mn></msup></mrow></mfenced></math> as remainder,</p><p>Now again using binomial in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>&#183;</mo><mfenced><mrow><mo>-</mo><msup><mn>2</mn><mn>51</mn></msup></mrow></mfenced><mo>=</mo><mo>-</mo><mn>56</mn><msup><mfenced><msup><mn>2</mn><mn>4</mn></msup></mfenced><mn>12</mn></msup><mo>=</mo><mo>-</mo><mn>56</mn><msup><mfenced><mrow><mn>17</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>12</mn></msup></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>56</mn><msup><mfenced><mrow><mn>17</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>12</mn></msup><mo>=</mo><mo>-</mo><mn>56</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>12</mn></mmultiscripts><msup><mn>17</mn><mn>12</mn></msup><mo>&#183;</mo><msup><mn>1</mn><mn>0</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>12</mn></mmultiscripts><msup><mn>17</mn><mn>11</mn></msup><mo>&#183;</mo><msup><mn>1</mn><mn>1</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>12</mn><none></none><mprescripts></mprescripts><none></none><mn>12</mn></mmultiscripts><msup><mn>1</mn><mn>12</mn></msup></mrow></mfenced></math></p><p>Now dividing above equation by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>56</mn><mo>&#215;</mo><mn>1</mn></mrow></mfenced><mo>&#247;</mo><mn>17</mn><mo>=</mo><mo>-</mo><mn>5</mn></math>,</p><p>Now changing negative remainder to positive we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn><mo>+</mo><mn>17</mn><mo>=</mo><mn>12</mn></math>,</p><p>Hence, when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mn>103</mn></msup></math> divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math> gives <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> as remainder.</p></blockquote>

</details>

---

### Q7. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Fractional part of the number <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>4</mn><mn>2022</mn></msup><mn>15</mn></mfrac></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>15</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>15</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>14</mn><mn>15</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>15</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>15</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>4</mn><mn>2022</mn></msup><mn>15</mn></mfrac></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>x</mi></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mi>n</mi></msup><msup><mi>x</mi><mn>0</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>x</mi><mn>1</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mn>0</mn></msup><msup><mi>x</mi><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mn>4</mn><mn>2022</mn></msup><mn>15</mn></mfrac><mo>=</mo><mfrac><msup><mn>16</mn><mn>1011</mn></msup><mn>15</mn></mfrac><mo>=</mo><mfrac><msup><mfenced><mrow><mn>15</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>1011</mn></msup><mn>15</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mfenced><mn>15</mn></mfenced><mn>1011</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mfenced><mn>15</mn></mfenced><mn>1010</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>1011</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mfenced><mn>15</mn></mfenced><mn>0</mn></msup></mrow><mn>15</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mfenced><mn>15</mn></mfenced><mn>1011</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mfenced><mn>15</mn></mfenced><mn>1010</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>1010</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mfenced><mn>15</mn></mfenced><mn>1</mn></msup></mrow><mn>15</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>15</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Fractional part of<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>4</mn><mn>2022</mn></msup><mn>15</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>15</mn></mfrac></math></p><p>Hence this is the required option.</p></blockquote>

</details>

---

### Q8. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let the number <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>22</mn><msup><mo>)</mo><mrow><mn>2022</mn><mo>&#160;</mo></mrow></msup><mo>+</mo><mo>&#160;</mo><mo>(</mo><mn>2022</mn><msup><mo>)</mo><mn>22</mn></msup></math> leave the remainder <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#945;</mi></math> when divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#946;</mi></math> when divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msup><mi mathvariant="normal">&#945;</mi><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mi mathvariant="normal">&#946;</mi><mn>2</mn></msup><mo>&#160;</mo><mo>)</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> be the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>22</mn></mfenced><mn>2022</mn></msup><mo>+</mo><msup><mfenced><mn>2022</mn></mfenced><mn>22</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> be the remainder when the same is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mn>22</mn></mfenced><mn>2022</mn></msup><mo>+</mo><msup><mfenced><mn>2022</mn></mfenced><mn>22</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>21</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2022</mn></msup><mo>+</mo><msup><mfenced><mn>2022</mn></mfenced><mn>22</mn></msup></math>.</p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>2022</mn></mfenced><mn>22</mn></msup></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2022</mn></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>.</p><p>So on expanding <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>21</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2022</mn></msup></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>21</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2022</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>2022</mn></mmultiscripts><msup><mfenced><mn>21</mn></mfenced><mn>2022</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2022</mn></mmultiscripts><msup><mfenced><mn>21</mn></mfenced><mn>2021</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>2022</mn><none></none><mprescripts></mprescripts><none></none><mn>2022</mn></mmultiscripts><msup><mfenced><mn>1</mn></mfenced><mn>2022</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mn>3</mn><mn>2021</mn></msup><mo>&#215;</mo><msup><mn>7</mn><mn>2022</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2022</mn></mmultiscripts><mo>&#215;</mo><msup><mn>3</mn><mn>2020</mn></msup><mo>&#215;</mo><msup><mn>7</mn><mn>2021</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><msub><mi>k</mi><mn>1</mn></msub><mo>+</mo><mn>1</mn></math></p><p>In this case the remainder is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mn>22</mn></mfenced><mn>2022</mn></msup><mo>+</mo><msup><mfenced><mn>2022</mn></mfenced><mn>22</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>21</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2022</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2023</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>22</mn></msup></math></p><p>Take <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2023</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>22</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>2023</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>22</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts><msup><mfenced><mn>2023</mn></mfenced><mn>22</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts><msup><mfenced><mn>2023</mn></mfenced><mn>21</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>22</mn><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>22</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts><msup><mfenced><mn>7</mn></mfenced><mn>21</mn></msup><msup><mfenced><mn>289</mn></mfenced><mn>22</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts><msup><mfenced><mn>7</mn></mfenced><mn>20</mn></msup><msup><mfenced><mn>289</mn></mfenced><mn>21</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><msub><mi>k</mi><mn>2</mn></msub><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>21</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2022</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2023</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>22</mn></msup><mo>=</mo><mn>7</mn><msub><mi>k</mi><mn>1</mn></msub><mo>+</mo><mn>1</mn><mo>+</mo><mn>7</mn><msub><mi>k</mi><mn>2</mn></msub><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mi>&#956;</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn></math>.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>=</mo><mn>5</mn></math>.</p><p>Therefore, the required answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>.</p></blockquote>

</details>

---

### Q9. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>25</mn><mn>190</mn></msup><mo>-</mo><msup><mn>19</mn><mn>190</mn></msup><mo>-</mo><msup><mn>8</mn><mn>190</mn></msup><mo>+</mo><msup><mn>2</mn><mn>190</mn></msup></math> is divisible by

**Options:**

- **(A)** neither <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math> but not by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math> but not by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>
- **(D)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math> but not by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>25</mn><mn>190</mn></msup><mo>-</mo><msup><mn>19</mn><mn>190</mn></msup><mo>-</mo><msup><mn>8</mn><mn>190</mn></msup><mo>+</mo><msup><mn>2</mn><mn>190</mn></msup></math></p><p>Now  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mn>25</mn><mn>190</mn></msup><mo>-</mo><msup><mn>19</mn><mn>190</mn></msup></mrow></mfenced><mo>,</mo><mo>&#160;</mo><msup><mn>8</mn><mn>190</mn></msup><mo>,</mo><mo>&#160;</mo><msup><mn>2</mn><mn>190</mn></msup></math> are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>25</mn><mn>190</mn></msup></math> will give remainder as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>19</mn><mn>190</mn></msup></math> will give remainder as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> when divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, so combined <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>25</mn><mn>190</mn></msup><mo>-</mo><msup><mn>19</mn><mn>190</mn></msup></math> will give remainder <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> </p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mn>25</mn><mn>190</mn></msup><mo>-</mo><msup><mn>8</mn><mn>190</mn></msup></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mo>-</mo><msup><mn>19</mn><mn>190</mn></msup><mo>+</mo><msup><mn>2</mn><mn>190</mn></msup></mrow></mfenced></math> are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mi>n</mi></msup><mo>-</mo><msup><mi>b</mi><mi>n</mi></msup></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>b</mi></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is even, 
So given number is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math> as it is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>17</mn></math> both,</p><p>Now,<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>25</mn><mn>190</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>7</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mn>190</mn></msup></math>, dividing by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>7</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mn>190</mn></msup><mo>=</mo><msup><mn>4</mn><mn>190</mn></msup><mo>=</mo><msup><mn>16</mn><mn>95</mn></msup><mo>=</mo><msup><mn>2</mn><mn>95</mn></msup><mo>=</mo><mn>4</mn><mo>&#183;</mo><msup><mn>8</mn><mn>31</mn></msup></math></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#183;</mo><msup><mfenced><mrow><mn>7</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>31</mn></msup></math> divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> will give remainder as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#183;</mo><mn>1</mn><mo>=</mo><mn>4</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>19</mn><mn>190</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>7</mn><mo>&#215;</mo><mn>3</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mn>190</mn></msup></math>, when divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>7</mn><mo>&#215;</mo><mn>3</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mn>190</mn></msup><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mn>190</mn></msup><mo>=</mo><msup><mn>2</mn><mn>190</mn></msup><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mn>8</mn><mn>63</mn></msup><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mfenced><mrow><mn>7</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>63</mn></msup></math></p><p>So, when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><msup><mfenced><mrow><mn>7</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>63</mn></msup></math> divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> will give remainder as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p><p>Similarly <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>8</mn><mn>190</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>7</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>190</mn></msup></math> will give <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> remainder </p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>190</mn></msup><mo>=</mo><mn>2</mn><msup><mfenced><mrow><mn>7</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>63</mn></msup></math> will give <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> remainder,</p><p>So combining all we get,<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>25</mn><mn>190</mn></msup><mo>-</mo><msup><mn>19</mn><mn>190</mn></msup><mo>-</mo><msup><mn>8</mn><mn>190</mn></msup><mo>+</mo><msup><mn>2</mn><mn>190</mn></msup><mo>=</mo><mn>4</mn><mo>-</mo><mn>2</mn><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>5</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>Not divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>, so it will not be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math></p></blockquote>

</details>

---

### Q10. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Among the statements :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>S</mi><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><msup><mn>2023</mn><mn>2022</mn></msup><mo>-</mo><msup><mn>1999</mn><mn>2022</mn></msup></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>S</mi><mn>2</mn><mo>)</mo><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mn>13</mn><mo>(</mo><mn>13</mn><msup><mo>)</mo><mi>n</mi></msup><mo>-</mo><mn>11</mn><mi>n</mi><mo>-</mo><mn>13</mn></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>144</mn></math> for infinitely many <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math></p>

**Options:**

- **(A)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is correct
- **(B)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>S</mi><mn>1</mn><mo>)</mo></math> is correct
- **(C)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are correct
- **(D)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are incorrect

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>S</mi><mn>1</mn><mo>)</mo></math> is correct**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>S</mi><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mo>(</mo><mn>2023</mn><msup><mo>)</mo><mn>2022</mn></msup><mo>-</mo><mo>(</mo><mn>1999</mn><msup><mo>)</mo><mn>2022</mn></msup></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></p><p>Now we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>)</mo></math> divides <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mi>n</mi></msup><mo>-</mo><msup><mi>y</mi><mi>n</mi></msup></mrow></mfenced><mo>&#160;</mo><mo>&#8704;</mo><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2023</mn><mo>-</mo><mn>1999</mn></mrow></mfenced></math> divides <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2023</mn><msup><mo>)</mo><mn>2022</mn></msup><mo>-</mo><mo>(</mo><mn>1999</mn><msup><mo>)</mo><mn>2022</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>24</mn></math> divides <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2023</mn><msup><mo>)</mo><mn>2022</mn></msup><mo>-</mo><mo>(</mo><mn>1999</mn><msup><mo>)</mo><mn>2002</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>8</mn></math> will divide <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2023</mn><msup><mo>)</mo><mn>2022</mn></msup><mo>-</mo><mo>(</mo><mn>1999</mn><msup><mo>)</mo><mn>2002</mn></msup></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> divides <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> is correct</p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mn>13</mn><msup><mfenced><mn>13</mn></mfenced><mi>n</mi></msup><mo>-</mo><mn>11</mn><mi>n</mi><mo>-</mo><mn>13</mn></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>144</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math></p><p>So using binomial theorem in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>12</mn></mrow></mfenced><mi>n</mi></msup></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>12</mn></mrow></mfenced><mi>n</mi></msup><mo>-</mo><mn>11</mn><mi>n</mi><mo>-</mo><mn>13</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>13</mn><mfenced><mrow><msup><mrow></mrow><mi>n</mi></msup><msub><mi>C</mi><mn>0</mn></msub><msup><mo>+</mo><mi>n</mi></msup><msub><mi>C</mi><mn>1</mn></msub><mn>12</mn><msup><mo>+</mo><mi>n</mi></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mn>12</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mo>+</mo><mi>n</mi></msup><msub><mi>C</mi><mi>n</mi></msub><msup><mn>12</mn><mi>n</mi></msup></mrow></mfenced><mo>-</mo><mn>11</mn><mi>n</mi><mo>-</mo><mn>13</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>12</mn><mo>&#215;</mo><mn>13</mn><mi>n</mi><mo>-</mo><mn>11</mn><mi>n</mi><mo>+</mo><msup><mn>12</mn><mn>2</mn></msup><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>145</mn><mi>n</mi><mo>+</mo><mn>144</mn><mi>&#955;</mi></math> which is not divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>144</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is incorrect</p></blockquote>

</details>

---

### Q11. JEE Main 2023 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

The remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>19</mn><mn>200</mn></msup><mo>+</mo><msup><mn>23</mn><mn>200</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn></math>, is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **29**

**Detailed Solution:**

<p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>19</mn><mn>200</mn></msup><mo>+</mo><msup><mn>23</mn><mn>200</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>21</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mn>200</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>21</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mn>200</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="}" open="{"><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>200</mn></mmultiscripts><msup><mfenced><mn>21</mn></mfenced><mn>200</mn></msup><mo>&#215;</mo><msup><mn>2</mn><mn>0</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>200</mn></mmultiscripts><msup><mfenced><mn>21</mn></mfenced><mn>198</mn></msup><mo>&#215;</mo><msup><mn>2</mn><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>200</mn><none></none><mprescripts></mprescripts><none></none><mn>200</mn></mmultiscripts><msup><mfenced><mn>21</mn></mfenced><mn>0</mn></msup><mo>&#215;</mo><msup><mn>2</mn><mn>200</mn></msup></mrow></mfenced></math></p><p>Now we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>21</mn><mn>2</mn></msup><mo>=</mo><mn>441</mn></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn></math>,</p><p>So rest of the terms will be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn></math> </p><p>So lets consider for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced close="}" open="{"><mrow><mmultiscripts><mi>C</mi><mn>200</mn><none></none><mprescripts></mprescripts><none></none><mn>200</mn></mmultiscripts><msup><mfenced><mn>21</mn></mfenced><mn>0</mn></msup><mo>&#215;</mo><msup><mn>2</mn><mn>200</mn></msup></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mn>201</mn></msup></math></p><p>Now rewriting the term <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>201</mn></msup><mo>=</mo><msup><mfenced><msup><mn>2</mn><mn>3</mn></msup></mfenced><mn>67</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>7</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>67</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>7</mn></mrow></mfenced><mn>67</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>67</mn></mmultiscripts><mo>&#215;</mo><mn>1</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>67</mn></mmultiscripts><mn>7</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>67</mn></mmultiscripts><msup><mn>7</mn><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>67</mn><mo>&#215;</mo><mn>7</mn><mo>+</mo><mn>49</mn><mi>k</mi></math></p><p>Now when dividing <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>7</mn></mrow></mfenced><mn>67</mn></msup></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn></math> we consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>67</mn><mo>&#215;</mo><mn>7</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn><mi>k</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn></math></p><p>Now  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>67</mn><mo>&#215;</mo><mn>7</mn><mo>=</mo><mn>470</mn></math> which when divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn></math> leaves remainder as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>29</mn></math>.</p>

</details>

---

### Q12. JEE Main 2023 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

The remainder on dividing <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mn>99</mn></msup></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>Now to divide <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mn>99</mn></msup></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> we need to check the cyclicity of power of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> when divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>,</p><p>So remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>5</mn><mn>1</mn></msup><mn>11</mn></mfrac><mo>&#8594;</mo><mn>5</mn><mo>&#160;</mo><mtext>as&#160;remainder</mtext></math></p><p>Similarly,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>5</mn><mn>2</mn></msup><mn>11</mn></mfrac><mo>=</mo><mfrac><mn>25</mn><mn>11</mn></mfrac><mo>&#8594;</mo><mn>3</mn><mo>&#160;</mo><mtext>as&#160;remainder</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>5</mn><mn>3</mn></msup><mn>11</mn></mfrac><mo>=</mo><mfrac><mn>125</mn><mn>11</mn></mfrac><mo>&#8594;</mo><mn>4</mn><mo>&#160;</mo><mtext>as&#160;remainder</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>5</mn><mn>4</mn></msup><mn>11</mn></mfrac><mo>=</mo><mfrac><mn>625</mn><mn>11</mn></mfrac><mo>&#8594;</mo><mn>9</mn><mo>&#160;</mo><mtext>as&#160;remainder</mtext></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>5</mn><mn>5</mn></msup><mn>11</mn></mfrac><mo>=</mo><mfrac><mn>3125</mn><mn>11</mn></mfrac><mo>&#8594;</mo><mn>1</mn><mo>&#160;</mo><mtext>as&#160;remainder</mtext></math></p><p>So, rewriting the expression we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><msup><mn>5</mn><mn>5</mn></msup></mfenced><mn>19</mn></msup><mo>&#215;</mo><msup><mn>5</mn><mn>4</mn></msup></math></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mfenced><msup><mn>5</mn><mn>5</mn></msup></mfenced><mn>19</mn></msup><mo>&#215;</mo><msup><mn>5</mn><mn>4</mn></msup></mrow><mn>11</mn></mfrac><mo>&#8594;</mo><mn>1</mn><mo>&#215;</mo><mfrac><msup><mn>5</mn><mn>4</mn></msup><mn>11</mn></mfrac><mo>&#160;</mo></math></p><p>Now again simplifying we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>5</mn><mn>4</mn></msup><mn>11</mn></mfrac><mo>&#160;</mo><mo>&#8594;</mo><mn>9</mn><mo>&#160;</mo><mo>&#160;</mo><mtext>as&#160;remainder</mtext></math>.</p>

</details>

---

### Q13. JEE Main 2023 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>50</mn><mtext>th&#160;</mtext></msup></math> root of a number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>50</mn><mtext>th&#160;</mtext></msup></math> root of another number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mo>&#160;</mo></math> . Then the remainder obtained on dividing <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">y</mi><mo>)</mo></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math> is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **23**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mfrac><mn>1</mn><mn>50</mn></mfrac></msup><mo>=</mo><mn>12</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msup><mn>12</mn><mn>50</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mfrac><mn>1</mn><mn>50</mn></mfrac></msup><mo>=</mo><mn>18</mn><mo>&#8658;</mo><mi>y</mi><mo>=</mo><msup><mn>18</mn><mn>50</mn></msup></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><msup><mn>12</mn><mn>50</mn></msup><mo>+</mo><msup><mn>18</mn><mn>50</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>25</mn></mfrac><mo>=</mo><mfrac><msup><mn>12</mn><mn>50</mn></msup><mn>25</mn></mfrac><mo>+</mo><mfrac><msup><mn>18</mn><mn>50</mn></msup><mn>25</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>25</mn></mfrac><mo>=</mo><mfrac><mrow><msup><mfenced><msup><mn>12</mn><mn>3</mn></msup></mfenced><mn>16</mn></msup><msup><mn>12</mn><mn>2</mn></msup></mrow><mn>25</mn></mfrac><mo>+</mo><mfrac><msup><mfenced><msup><mn>18</mn><mn>2</mn></msup></mfenced><mn>25</mn></msup><mn>25</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>25</mn></mfrac><mo>=</mo><mfrac><mrow><msup><mfenced><mn>1728</mn></mfenced><mn>16</mn></msup><msup><mn>12</mn><mn>2</mn></msup></mrow><mn>25</mn></mfrac><mo>+</mo><mfrac><msup><mfenced><mrow><mn>325</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>25</mn></msup><mn>25</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>25</mn></mfrac><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mn>1725</mn><mo>+</mo><mn>3</mn></mrow></mfenced><mn>16</mn></msup><msup><mn>12</mn><mn>2</mn></msup></mrow><mn>25</mn></mfrac><mo>+</mo><mfrac><msup><mfenced><mrow><mn>325</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>25</mn></msup><mn>25</mn></mfrac></math></p><p>So, remainder is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mn>3</mn><mn>16</mn></msup><msup><mn>12</mn><mn>2</mn></msup></mrow><mn>25</mn></mfrac><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mrow><msup><mfenced><msup><mn>3</mn><mn>3</mn></msup></mfenced><mn>5</mn></msup><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>144</mn></mrow><mn>25</mn></mfrac><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mn>25</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mn>5</mn></msup><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>144</mn></mrow><mn>25</mn></mfrac><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mn>25</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mn>5</mn></msup><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mfenced><mrow><mn>150</mn><mo>-</mo><mn>6</mn></mrow></mfenced></mrow><mn>25</mn></mfrac><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mn>5</mn></msup><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced></mrow><mn>25</mn></mfrac><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>25</mn><mo>+</mo><mn>7</mn></mrow></mfenced><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced></mrow><mn>25</mn></mfrac><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mn>21</mn></mfenced><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced></mrow><mn>25</mn></mfrac><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>25</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced></mrow><mn>25</mn></mfrac><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced></mrow><mn>25</mn></mfrac><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>24</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>23</mn></math></p><p>Hence, the remainder is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>23</mn></math></p>

</details>

---

### Q14. JEE Main 2023 (25 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

The remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>2023</mn></mfenced><mn>2023</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<p>To find the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2023</mn><mn>2023</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math> we will use binomial expansion,</p><p>Now rewriting above expression we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2023</mn><mn>2023</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>2030</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mn>2023</mn></msup></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>2030</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mn>2023</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><msup><mn>2030</mn><mn>2023</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2023</mn></mmultiscripts><msup><mfenced><mn>2030</mn></mfenced><mn>2022</mn></msup><mo>&#215;</mo><mn>7</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><msup><mn>7</mn><mn>2023</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>2030</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mn>2023</mn></msup><mo>=</mo><mn>35</mn><mi>k</mi><mo>-</mo><msup><mn>7</mn><mn>2023</mn></msup></math>; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8712;</mo><mi>Z</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>as</mi><mo>&#160;</mo><mn>2030</mn><mo>&#160;</mo><mi>is</mi><mo>&#160;</mo><mi>multiple</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;35</mo></mrow></mfenced></math></p><p>Now remainder will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mn>7</mn><mn>2023</mn></msup></math>. Rewriting <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mn>7</mn><mn>2023</mn></msup></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mn>7</mn><mn>2023</mn></msup><mo>=</mo><mo>-</mo><msup><mfenced><msup><mn>7</mn><mn>3</mn></msup></mfenced><mn>674</mn></msup><mo>&#215;</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msup><mfenced><msup><mn>7</mn><mn>3</mn></msup></mfenced><mn>674</mn></msup><mo>&#215;</mo><mn>7</mn><mo>=</mo><mo>-</mo><msup><mfenced><mn>343</mn></mfenced><mn>674</mn></msup><mo>&#215;</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msup><mfenced><mn>343</mn></mfenced><mn>674</mn></msup><mo>&#215;</mo><mn>7</mn><mo>=</mo><mo>-</mo><msup><mfenced><mrow><mn>350</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mn>674</mn></msup><mo>&#215;</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>35</mn><msub><mi>k</mi><mn>1</mn></msub><mo>+</mo><msup><mn>7</mn><mn>674</mn></msup></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>7</mn></mrow></mfenced></math></p><p>So, again using binomial we get remainder as <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn><mo>&#215;</mo><msup><mn>7</mn><mn>674</mn></msup></math></p><p>Again rewriting the expression as </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn><mo>&#215;</mo><msup><mn>7</mn><mn>674</mn></msup><mo>=</mo><mo>-</mo><msup><mn>7</mn><mn>675</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><msup><mn>7</mn><mn>675</mn></msup><mo>=</mo><mo>-</mo><msup><mfenced><msup><mn>7</mn><mn>3</mn></msup></mfenced><mn>225</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>350</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mn>75</mn></msup></math></p><p>Again using binomial we get remainder as </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>350</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mn>75</mn></msup><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>7</mn></mrow></mfenced><mn>75</mn></msup><mo>=</mo><mo>-</mo><msup><mfenced><mrow><mn>350</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mn>25</mn></msup></math></p><p>Again using binomial we get remainder as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mn>25</mn></msup></math>.</p><p>Now again rewriting <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><msup><mn>7</mn><mn>3</mn></msup></mfenced><mn>8</mn></msup><mo>&#215;</mo><mn>7</mn><mo>=</mo><msup><mfenced><mrow><mn>350</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mn>8</mn></msup><mo>&#215;</mo><mn>7</mn></math></p><p>Using binomial remainder will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mn>9</mn></msup></math> which can be written as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><msup><mn>7</mn><mn>3</mn></msup></mfenced><mn>3</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>350</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mn>3</mn></msup></math>,</p><p>Using binomial remainder will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mn>7</mn><mn>3</mn></msup></math> which can be written as <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>343</mn></math>, so remainder will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>350</mn><mo>-</mo><mn>343</mn><mo>=</mo><mn>7</mn></math>,</p><p>Hence, the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2023</mn><mn>2023</mn></msup></math> when divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>.</p>

</details>

---

### Q15. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mn>2022</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2022</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<blockquote><p>Using the binomial expansion in the given expression we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mn>2022</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2022</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>50</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>1011</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>10</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>1011</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mfenced><mn>50</mn></mfenced><mn>1011</mn></msup><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>0</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mfenced><mn>50</mn></mfenced><mn>1010</mn></msup><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>1</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>1011</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mfenced><mn>50</mn></mfenced><mn>0</mn></msup><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>1011</mn></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mfenced><mn>10</mn></mfenced><mn>1011</mn></msup><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>0</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mfenced><mn>10</mn></mfenced><mn>1010</mn></msup><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>1</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>1011</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mfenced><mn>10</mn></mfenced><mn>0</mn></msup><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>1011</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mi>k</mi><mo>-</mo><mn>2</mn></math></p><p>Using binomial expansion we get the remainder as <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>3</mn></math></p></blockquote>

</details>

---

### Q16. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>2021</mn></mfenced><mn>2022</mn></msup><mo>+</mo><msup><mfenced><mn>2022</mn></mfenced><mn>2021</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>We know <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2023</mn><mo>=</mo><mn>7</mn><mo>&#215;</mo><mn>289</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>2021</mn></mfenced><mn>2022</mn></msup><mo>+</mo><msup><mfenced><mn>2022</mn></mfenced><mn>2021</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>2023</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2022</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2023</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2021</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><msub><mi>m</mi><mn>1</mn></msub><mo>+</mo><msup><mn>2</mn><mn>2022</mn></msup><mo>+</mo><mn>7</mn><msub><mi>m</mi><mn>2</mn></msub><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2021</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mfenced><mrow><msub><mi>m</mi><mn>1</mn></msub><mo>+</mo><msub><mi>m</mi><mn>2</mn></msub></mrow></mfenced><mo>+</mo><msup><mn>8</mn><mn>674</mn></msup><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mfenced><mrow><msub><mi>m</mi><mn>1</mn></msub><mo>+</mo><msub><mi>m</mi><mn>2</mn></msub></mrow></mfenced><mo>+</mo><mo>(</mo><mn>7</mn><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>674</mn></msup><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mfenced><mrow><msub><mi>m</mi><mn>1</mn></msub><mo>+</mo><msub><mi>m</mi><mn>2</mn></msub></mrow></mfenced><mo>+</mo><mn>7</mn><msub><mi>m</mi><mn>3</mn></msub><mo>+</mo><mn>1</mn><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mfenced><mrow><msub><mi>m</mi><mn>1</mn></msub><mo>+</mo><msub><mi>m</mi><mn>2</mn></msub><mo>+</mo><msub><mi>m</mi><mn>3</mn></msub></mrow></mfenced></math></p><p>This is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p><p>Hence, remainder is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></p></blockquote>

</details>

---

### Q17. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>11</mn></mfenced><mn>1011</mn></msup><mo>+</mo><msup><mfenced><mn>1011</mn></mfenced><mn>11</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> is _____ .

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>11</mn><mn>1011</mn></msup><mo>=</mo><msup><mfenced><msup><mn>11</mn><mn>3</mn></msup></mfenced><mn>327</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>9</mn><mi>k</mi><mo>+</mo><mn>8</mn></mrow></mfenced><mn>327</mn></msup></math></p><p>when divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> is equivalent to the division of </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>8</mn><mn>327</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>9</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>327</mn></msup></math></p><p>i.e. remainder<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>1</mn><mo>+</mo><mn>9</mn><mo>=</mo><mn>8</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>1011</mn></mfenced><mn>11</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>9</mn><mi>m</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>11</mn></msup></math></p><p>when divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> is equivalent to the division of </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>11</mn></msup><mo>=</mo><msup><mfenced><mn>9</mn></mfenced><mn>5</mn></msup><mo>&#215;</mo><mn>3</mn></math></p><p>i.e. remainder<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mn>11</mn><mn>1011</mn></msup><mo>+</mo><msup><mn>1011</mn><mn>11</mn></msup></math> has same remainder as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>.</p>

</details>

---

### Q18. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>2021</mn></mfenced><mn>2023</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p>The remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2021</mn></math> divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>. Hence, the problem reduces to finding the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2023</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2022</mn></msup><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>2</mn><mn>2022</mn></msup></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#215;</mo><msup><mfenced><msup><mn>2</mn><mn>3</mn></msup></mfenced><mn>674</mn></msup></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#215;</mo><msup><mfenced><mn>8</mn></mfenced><mn>674</mn></msup></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#215;</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>7</mn></mrow></mfenced><mn>674</mn></msup></mrow><mn>7</mn></mfrac></math></p><p>Using binomial theorem, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#215;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mn>7</mn><mi>k</mi></mrow></mfenced></mrow><mn>7</mn></mfrac></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is an integer.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>14</mn><mi>k</mi></mrow><mn>7</mn></mfrac></math></p><p>Clearly, the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>14</mn><mi>k</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>5</mn><mo>+</mo><mn>5</mn></mrow><mn>7</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>7</mn></mfrac></math></p><p>Hence, the remainder is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>.</p>

</details>

---

### Q19. JEE Main 2022 (25 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mo>&#183;</mo><msup><mn>3</mn><mn>10</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>9</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>&#183;</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mi>K</mi><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>10</mn></msup></mrow></mfrac></math>, then the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p>We know <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mi>n</mi></msup><mo>-</mo><msup><mi>y</mi><mi>n</mi></msup><mo>=</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mi>y</mi><mo>+</mo><mo>&#8943;</mo><mi>x</mi><msup><mi>y</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>+</mo><msup><mi>y</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mo>&#183;</mo><msup><mn>3</mn><mn>10</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>9</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8943;</mo><mo>&#183;</mo><mfrac><mn>1</mn><mrow><msup><mn>2</mn><mn>9</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>&#183;</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mn>9</mn></msup><mo>+</mo><msup><mn>2</mn><mn>8</mn></msup><mo>&#183;</mo><mn>3</mn><mo>+</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn><mo>&#183;</mo><msup><mn>3</mn><mn>8</mn></msup><mo>+</mo><msup><mn>3</mn><mn>9</mn></msup></mrow><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>16</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mn>3</mn><mn>10</mn></msup><mo>-</mo><msup><mn>2</mn><mn>10</mn></msup></mrow><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>10</mn></msup></mrow></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><msup><mn>3</mn><mn>10</mn></msup><mo>-</mo><msup><mn>2</mn><mn>10</mn></msup></math>
Since we need the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></p><p>so, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>10</mn></msup><mo>=</mo><mn>6</mn><msub><mi>q</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>10</mn></msup><mo>=</mo><mn>6</mn><msub><mi>q</mi><mn>2</mn></msub><mo>+</mo><mn>4</mn></math>
Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> will be of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>6</mn><msub><mi>q</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>6</mn><msub><mi>q</mi><mn>2</mn></msub><mo>+</mo><mn>4</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mfenced><mrow><msub><mi>q</mi><mn>1</mn></msub><mo>-</mo><msub><mi>q</mi><mn>2</mn></msub></mrow></mfenced><mo>-</mo><mn>1</mn></math>
Hence, when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>, we get the remainder as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q20. JEE Main 2022 (24 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

The remainder on dividing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mn>3</mn><mn>2021</mn></msup></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mo>&#8943;</mo><mo>&#183;</mo><msup><mn>3</mn><mn>2021</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mn>3</mn><mn>2022</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mn>3</mn><mn>2022</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p>Simplifying by using binomial expansion we get<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mfenced><msup><mn>3</mn><mn>2</mn></msup></mfenced><mn>1011</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mo>(</mo><mn>10</mn><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>1011</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mrow><msup><mrow></mrow><mn>1011</mn></msup><msub><mi>C</mi><mn>0</mn></msub><msup><mn>10</mn><mn>1011</mn></msup><msup><mo>-</mo><mn>1011</mn></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mn>10</mn><mn>1010</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>1010</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mn>10</mn><mn>1</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>1011</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><mo>&#215;</mo><mn>1</mn><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>100</mn><mi>q</mi><mo>+</mo><mn>1011</mn><mo>&#215;</mo><mn>10</mn><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mn>100</mn><mi>q</mi><mo>+</mo><mn>10110</mn><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>100</mn><mi>q</mi><mo>+</mo><mn>10108</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>50</mn><mi>q</mi><mo>+</mo><mn>5054</mn></math></p><p>Now dividing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mi>q</mi><mo>+</mo><mn>5054</mn></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math></p><p>We get <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> as remainder.</p><p>Hence option B is correct.</p>

</details>

---

### Q21. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>2022</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><msup><mn>3</mn><mn>2</mn></msup></mfenced><mn>1011</mn></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>10</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>1011</mn></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>10</mn></mrow></mfenced><mn>1011</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><msub><mmultiscripts><mi>C</mi><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><mn>1</mn></msub><mn>10</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>1011</mn></mmultiscripts><msup><mn>10</mn><mn>2</mn></msup><mo>&#8230;</mo></mrow></mfenced><mo>=</mo><mn>10</mn><mi>q</mi><mo>-</mo><mn>1</mn></math></p><p>So, here the remainder will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q22. JEE Main 2021 (27 Aug Shift 2)

*Type:* `numerical` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><msup><mn>7</mn><mn>22</mn></msup><mo>+</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mn>22</mn></msup><mo>-</mo><mn>44</mn></math> when divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math> leaves the remainder

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **15**

**Detailed Solution:**

<p>Given that: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><msup><mn>7</mn><mn>22</mn></msup><mo>+</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mn>22</mn></msup><mo>-</mo><mn>44</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>&#215;</mo><mo>(</mo><mn>6</mn><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>22</mn></msup><mo>+</mo><mn>2</mn><mo>&#215;</mo><mo>(</mo><mn>9</mn><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>22</mn></msup><mo>-</mo><mn>44</mn></math></p><p>As we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow><mi>n</mi></msup><mo>=</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>(</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mi>x</mi><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>)</mo><mo>=</mo><mn>1</mn><mo>+</mo><mi>k</mi><mi>x</mi><mo>&#160;</mo><mo>;</mo><mo>&#160;</mo><mi>k</mi><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>18</mn><mi>&#955;</mi><mo>+</mo><mn>3</mn><mo>+</mo><mn>18</mn><mi>&#956;</mi><mo>+</mo><mn>2</mn><mo>-</mo><mn>44</mn><mo>&#160;</mo><mo>&#160;</mo><mo>;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>,</mo><mi>&#956;</mi><mo>&#8712;</mo><mi mathvariant="normal">I</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>18</mn><mi>&#948;</mi><mo>-</mo><mn>39</mn><mo>&#160;</mo><mo>;</mo><mi>&#948;</mi><mo>&#8712;</mo><mi mathvariant="normal">I</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>18</mn><mi>&#946;</mi><mo>+</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>remainder <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>15</mn></math></p>

</details>

---

### Q23. JEE Main 2021 (17 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2021</mn><msup><mo>)</mo><mn>3762</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn><mo>,</mo></math> then the remainder is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2023</mn><mo>-</mo><mn>2</mn><msup><mo>)</mo><mn>3762</mn></msup><mo>=</mo><mn>2023</mn><msub><mi>k</mi><mn>1</mn></msub><mo>+</mo><msup><mn>2</mn><mn>3762</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>17</mn><msub><mi>k</mi><mn>2</mn></msub><mo>+</mo><msup><mn>2</mn><mn>3762</mn></msup></math> (as<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2023</mn><mo>=</mo><mn>17</mn><mo>&#215;</mo><mn>17</mn><mo>&#215;</mo><mn>9</mn></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>17</mn><msub><mi>k</mi><mn>2</mn></msub><mo>+</mo><mn>4</mn><mo>&#215;</mo><msup><mn>16</mn><mn>940</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>17</mn><msub><mi>k</mi><mn>2</mn></msub><mo>+</mo><mn>4</mn><mo>&#215;</mo><mo>(</mo><mn>17</mn><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>940</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>17</mn><msub><mi>k</mi><mn>2</mn></msub><mo>+</mo><mn>4</mn><mfenced><mrow><mn>17</mn><msub><mi>k</mi><mn>3</mn></msub><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>17</mn><mi>k</mi><mo>+</mo><mn>4</mn><mo>&#8658;</mo></math>remainder<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q24. JEE Main 2021 (25 Feb Shift 2)

*Type:* `numerical` | *Level:* `3`

If the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>, then the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2020</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2022</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> is ___ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn><mi>k</mi><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mfenced><mrow><mn>2020</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2022</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>2020</mn><mo>+</mo><mn>4</mn><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2022</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>4</mn><mfenced><mrow><mn>505</mn><mo>+</mo><mi>k</mi></mrow></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2022</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>4</mn><mi>&#955;</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2022</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>16</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>24</mn><mi>&#955;</mi><mo>+</mo><mn>9</mn></mrow></mfenced><mn>1011</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>8</mn><mfenced><mrow><mn>2</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mn>1011</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>8</mn><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>1011</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Remainder when divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>=</mo><mn>1</mn></math>.</p>

</details>

---

### Q25. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi mathvariant="normal">p</mi><mo>}</mo></math> denotes the fractional part of the number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">p</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mfrac><msup><mn>3</mn><mn>200</mn></msup><mn>8</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>8</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>**

**Detailed Solution:**

<p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>200</mn></msup><mo>=</mo><msup><mn>9</mn><mn>100</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>1</mn><mo>+</mo><mn>8</mn><msup><mo>)</mo><mn>100</mn></msup><mo>=</mo><mn>1</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><mn>8</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>100</mn></mmultiscripts><msup><mfenced><mn>8</mn></mfenced><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mn>8</mn><mn>100</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mn>200</mn></msup><mo>=</mo><mn>1</mn><mo>+</mo><mn>8</mn><mi>&#955;</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is some integer.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mn>3</mn><mn>200</mn></msup><mn>8</mn></mfrac><mo>=</mo><mi>&#955;</mi><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="}" open="{"><mfrac><msup><mn>3</mn><mn>200</mn></msup><mn>8</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p>

</details>

---

### Q26. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the fractional part of the number <math><mfrac><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>403</mn></mrow></msup></mrow><mrow><mn>15</mn></mrow></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>k</mi><mn>15</mn></mfrac><mo>,</mo></math> then <math><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>
- **(C)** <math><mn>8</mn></math>
- **(D)** <math><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>8</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>403</mn></msup><mo>=</mo><msup><mn>2</mn><mn>3</mn></msup><mo>.</mo><msup><mfenced separators="|"><msup><mn>2</mn><mn>4</mn></msup></mfenced><mn>100</mn></msup><mi>&#160;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mo>.</mo><msup><mfenced separators="|"><mrow><mn>15</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>100</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mfenced open="[" close="]" separators="|"><mrow><msup><mrow/><mn>100</mn></msup><msub><mi>C</mi><mn>0</mn></msub><msup><mn>15</mn><mn>100</mn></msup><mo>+</mo><msup><mi>&#8201;</mi><mn>100</mn></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mn>15</mn><mn>99</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>&#8201;</mi><mn>100</mn></msup><msub><mi>C</mi><mn>99</mn></msub><mn>15</mn><mo>+</mo><msup><mi>&#8201;</mi><mn>100</mn></msup><msub><mi>C</mi><mn>100</mn></msub></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mo>.</mo><mfenced open="[" close="]" separators="|"><mrow><mn>15</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>
<math><mo>=</mo><mn>8.15</mn><mi>&#955;</mi><mo>+</mo><mn>8</mn></math>
<math><mo>&#8658;</mo><mfrac><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>403</mn></mrow></msup></mrow><mrow><mn>15</mn></mrow></mfrac><mo>=</mo><mn>8</mn><mi>&#955;</mi><mo>+</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>
Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>8</mn></math>

</details>

---

### Q27. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mn>27</mn></mfenced><mn>999</mn></msup></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>, then the remainder is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>27</mn><msup><mo>)</mo><mn>999</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mfenced separators="|"><mrow><mn>28</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>999</mn></msup><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>28</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>28</mn><mi>&#955;</mi><mo>-</mo><mn>7</mn><mo>+</mo><mn>7</mn><mo>-</mo><mn>1</mn></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>7</mn><mfenced separators="|"><mrow><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>6</mn></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Remainder<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q28. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `3`

The remainder left out when $8^{2 n}-(62)^{2 n+1}$ is divided by 9 is

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** 7
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

$$
\begin{aligned}
& 8^{2 n}-(62)^{2 n+1}=(1+63)^n-(63-1)^{2 n+1} \\
& =(1+63)^n+(1-63)^{2 n+1}=\left(1+{ }^n c_1 63+{ }^n c_2(63)^2+\ldots .+(63)^n\right)+\left(1-{ }^{(2 n+1)} c_1 63+{ }^{(2 n+1)} c_2(63)^2+\ldots .+(-1)(63)^{(2 n+1)}\right) \\
& =2+63\left({ }^n c_1+{ }^n c_2(63)+\ldots .+(63)^{n-1}-{ }^{(2 n+1)} c_1+{ }^{(2 n+1)} c_2(63)+\ldots .(63)^{(2 n)}\right)
\end{aligned}
$$
$\therefore$ Reminder is 2

</details>

---

