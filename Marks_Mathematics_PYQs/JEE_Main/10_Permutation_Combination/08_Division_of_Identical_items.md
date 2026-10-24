# JEE Main Mathematics - Permutation Combination

## Topic 8: Division of Identical items

**Total Questions:** 18

---

### Q1. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\{(a,b,c): a,b,c \text{ are non-negative integers and } a+b+2c=22\}$. Then $n(A)$ is equal to:

**Options:**

- **(A)** $121$
- **(B)** $124$
- **(C)** $144$
- **(D)** $169$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $144$**

**Detailed Solution:**

The given equation is $a + b + 2c = 22$, where $a, b, c$ are non-negative integers.

This can be rewritten as $a + b = 22 - 2c$.

Since $a \ge 0$ and $b \ge 0$, we must have $22 - 2c \ge 0$, which gives $c \le 11$.

Since $c$ is a non-negative integer, the possible values for $c$ are $0, 1, 2, \dots, 11$.

For a fixed value of $c$, the number of non-negative integer solutions to the equation $a + b = 22 - 2c$ is given by $(22 - 2c) + 1 = 23 - 2c$.

The total number of solutions $n(A)$ is the sum of the number of solutions for each possible value of $c$:

$n(A) = \sum_{c=0}^{11} (23 - 2c)$

$n(A) = 23 + 21 + 19 + \dots + 1$

This is an arithmetic progression with $12$ terms, first term $1$, and last term $23$.

$n(A) = \dfrac{12}{2} (1 + 23) = 6 \times 24 = 144$

Answer: $144$

</details>

---

### Q2. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of ways, in which 16 oranges can be distributed to four children such that each child gets at least one orange, is

**Options:**

- **(A)** 455
- **(B)** 429
- **(C)** 403
- **(D)** 384

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 455**

**Detailed Solution:**

Distributing 16 identical oranges to 4 children with each getting at least 1.
Let $x_i \ge 1$ for $i = 1,2,3,4$ and $x_1+x_2+x_3+x_4 = 16$.
Substituting $y_i = x_i - 1 \ge 0$: $y_1+y_2+y_3+y_4 = 12$.
By stars and bars, number of ways $= \binom{12+3}{3} = \binom{15}{3} = \frac{15 \times 14 \times 13}{6} = 455$.

</details>

---

### Q3. JEE Main 2026 (21 January Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $\mathrm{S}=\{(\mathrm{m}, \mathrm{n}): \mathrm{m}, \mathrm{n} \in\{1,2,3, \ldots.., 50\}\}$. If the number of elements $(\mathrm{m}, \mathrm{n})$ in S such that $6^{\mathrm{m}}+9^{\mathrm{n}}$ is a multiple of 5 is $p$ and the number of elements ($m, n$) in $S$ such that $m+n$ is a square of a prime number is q, then $\mathrm{p}+\mathrm{q}$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1333**

**Detailed Solution:**

For $6^m + 9^n \equiv 0 \pmod{5}$:
$6 \equiv 1 \pmod{5}$ and $9 \equiv -1 \pmod{5}$
So $6^m + 9^n \equiv 1 + (-1)^n \pmod{5}$
This equals 0 only when n is odd.
Number of odd n in {1,...,50} = 25, and m can be any of 50 values.
$p = 50 \times 25 = 1250$
For $m + n$ = square of prime, possible values are 4, 9, 25, 49.
$m + n = 4$: 3 pairs
$m + n = 9$: 8 pairs
$m + n = 25$: 24 pairs
$m + n = 49$: 48 pairs
$q = 3 + 8 + 24 + 48 = 83$
$p + q = 1250 + 83 = 1333$

</details>

---

### Q4. JEE Main 2025 (7 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

For $\mathrm{n} \geq 2$, let $S_n$ denote the set of all subsets of $\{1,2 \ldots . . ., n\}$ with no two consecutive numbers. For example $\{1,3,5\} \in \mathrm{S}_6$, but $\{1,2,4\} \notin \mathrm{S}_6$. Then $n\left(\mathrm{~S}_5\right)$ is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **13**

**Detailed Solution:**

$\mathrm{A}=\{1,2,3,4,5 \ldots . . . \mathrm{n}\}$
No. of subsets having $r$ elements such that no two are consecutive is $={ }^{n-r+1} C_r$
for $\mathrm{n}=5$, no. of ways $={ }^{6 \cdot \mathrm{r}} \mathrm{C}_{\mathrm{r}}$
Subsets having no element $=1$
Subsets having exactly 1 element $={ }^5 \mathrm{C}_1=5$
Subsets having exactly 2 element $={ }^4 \mathrm{C}_2=6$
Subsets having exactly 3 element $={ }^3 \mathrm{C}_3=1$
$\Rightarrow 5+6+1+1=13$

</details>

---

### Q5. JEE Main 2024 (05 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

The number of ways of getting a sum 16 on throwing a dice four times is______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **125**

**Detailed Solution:**

$\begin{aligned} & \left(x^1+x^2 \ldots+x^6\right)^4 \\ & x^4 \cdot\left(\frac{1-x^6}{1-x}\right)^4 \\ & x^4 \cdot\left(1-x^6\right)^4 \cdot(1-x)^{-4} \\ & x^4\left[1-4 x^6+6 x^{12} \ldots .\right]\left[(1-x)^{-4}\right] \\ & \left(x^4-4 x^{10}+6 x^{16} \ldots\right)(1-x)^{-4} \\ & \left(x^4-4 x^{10}+6 x^{16}\right)\left(1+{ }^{15} C_{12} x^{12}+{ }^9 C_6 x^6 \ldots .\right) \\ & \left({ }^{15} C_{12}-4 \cdot{ }^9 C_6+6\right) x^{16} \\ & \left({ }^{15} C_3-4 \cdot{ }^9 C_6+6\right) \\ & =35 \times 13-6 \times 8 \times 7+6 \\ & =455-336+6 \\ & =125\end{aligned}$

</details>

---

### Q6. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The number of ways in which <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math> identical apples can be distributed among three children such that each child gets at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> apples, is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>406</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>130</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>142</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>136</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>136</mn></math>**

**Detailed Solution:**

<p>Let us initially distribute <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> apples to each children.</p><p>So, the remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> apples are to be distributed such that each children can get any number of apples.</p><p>So, the required number of ways will be given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mmultiscripts></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>N</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>15</mn><mo>+</mo><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>N</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>17</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>N</mi><mo>=</mo><mfrac><mrow><mn>17</mn><mo>×</mo><mn>16</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>N</mi><mo>=</mo><mn>136</mn></math></p>

</details>

---

### Q7. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Number of ways of arranging <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> identical books into <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> identical shelves where any number of shelves may remain empty is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>**

**Detailed Solution:**

<p>We have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> identical shelves in which any number of shelves can be empty.</p><p>So, we will put <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>,</mo><mo> </mo><mn>1</mn><mo>,</mo><mo> </mo><mn>0</mn></math> shelves empty one by one.</p><p>Also, the non-empty shelves won't require internal arrangement as all the shelves are identical.  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> Shelf empty: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>8</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>→</mo><mn>1</mn></math> way</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> shelf empty: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open=""><mtable><mtr><mtd><mo>(</mo><mn>7</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>)</mo></mtd></mtr><mtr><mtd><mo>(</mo><mn>6</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>)</mo></mtd></mtr><mtr><mtd><mo>(</mo><mn>5</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>)</mo></mtd></mtr><mtr><mtd><mo>(</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>)</mo></mtd></mtr></mtable></mfenced><mo>→</mo><mn>4</mn></math> ways</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> shelf empty: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open=""><mtable columnalign="left"><mtr><mtd><mo>(</mo><mn>6</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo></mtd><mtd><mo>(</mo><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo>)</mo></mtd></mtr><mtr><mtd><mo>(</mo><mn>5</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo></mtd><mtd><mo>(</mo><mn>4</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo>)</mo></mtd></mtr><mtr><mtd><mo>(</mo><mn>4</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo></mtd><mtd></mtd></mtr></mtable></mfenced><mo>→</mo><mn>5</mn></math>ways</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> shelf empty: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open=""><mtable columnalign="left right"><mtr><mtd><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>2</mn><mo>)</mo></mtd><mtd><mo>(</mo><mn>5</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo></mtd></mtr><mtr><mtd><mo>(</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>)</mo></mtd><mtd></mtd></mtr><mtr><mtd><mo>(</mo><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo></mtd><mtd></mtd></mtr><mtr><mtd><mo>(</mo><mn>4</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo></mtd><mtd></mtd></mtr></mtable></mfenced><mo>→</mo><mn>5</mn></math> ways</p><p>Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>15</mn></math> ways</p>

</details>

---

### Q8. JEE Main 2023 (13 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>The number of seven digit positive integers formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> only and sum of the digits equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> is<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo>.</mo></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **413**

**Detailed Solution:**

<blockquote><p>The given numbers are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></math> and sum of digits should be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>.</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mo>&#160;</mo><menclose notation="bottom"><mn>4</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>3</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose></math> ,Here the sum of the digits is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>.</p><p>The number of ways arranging them is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>7</mn><mo>!</mo></mrow><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>42</mn></math>.</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mo>&#160;</mo><menclose notation="bottom"><mn>4</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose></math>.</p><p>The number of ways arranging them is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>7</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mn>4</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>105</mn></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>:</mo><mo>&#160;</mo><menclose notation="bottom"><mn>3</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose></math>.</p><p>The number of ways arranging them is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>7</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>3</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>140</mn></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>:</mo><mo>&#160;</mo><menclose notation="bottom"><mn>3</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>3</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose></math>.</p><p>The number of ways arranging them is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>7</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mn>4</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>105</mn></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>:</mo><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>1</mn></menclose></math></p><p>The number of ways arranging them is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>7</mn><mo>!</mo></mrow><mrow><mn>5</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>21</mn></math></p><p>The total number of ways are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>42</mn><mo>+</mo><mn>105</mn><mo>+</mo><mn>140</mn><mo>+</mo><mn>105</mn><mo>+</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>413</mn></math></p><p>Therefore, the required answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>413</mn></math>.</p></blockquote>

</details>

---

### Q9. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of triplets <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi></math> are distinct non negative integers satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>15</mn></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>136</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>114</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>92</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>114</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>15</mn></math></p><p>Now we know that,</p><p>Non-negative integral solution of equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mi>n</mi></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mmultiscripts></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>b</mi><mo>=</mo><mi>c</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mi>b</mi><mo>&#8800;</mo><mi>c</mi></math> are also possibilities</p><p>So by above formula we get,</p><p>Total number of non-negative solution will be,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mn>15</mn><mo>+</mo><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>17</mn></mmultiscripts></math></p><p>Now solving If any of these <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> are equal
So, the equation will become<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>15</mn></math></p><p>Now finding possible cases we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mi>y</mi><mo>=</mo><mn>0</mn></mtd><mtd><mi>x</mi><mo>=</mo><mn>15</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mi>y</mi><mo>=</mo><mn>1</mn></mtd><mtd><mi>x</mi><mo>=</mo><mn>13</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mi>y</mi><mo>=</mo><mn>2</mn></mtd><mtd><mi>x</mi><mo>=</mo><mn>11</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mi>y</mi><mo>=</mo><mn>3</mn></mtd><mtd><mi>x</mi><mo>=</mo><mn>9</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mi>y</mi><mo>=</mo><mn>4</mn></mtd><mtd><mi>x</mi><mo>=</mo><mn>7</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>5</mn><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mn>5</mn><mo>&#8594;</mo><mi>x</mi><mo>=</mo><mi>y</mi><mo>=</mo><mi>z</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>6</mn><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>7</mn><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>So, total possibilities where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>z</mi></math> are distinct will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>17</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mo>&#215;</mo><mn>8</mn><mo>+</mo><mn>2</mn></math></p><p>{Note adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> because the cases <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>=</mo><mi>z</mi></math> is subtracted three times}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>136</mn><mo>-</mo><mn>24</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>114</mn></math></p></blockquote>

</details>

---

### Q10. JEE Main 2023 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>The number of ways of giving <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> distinct oranges to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> children such that each child gets at least one orange is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **171**

**Detailed Solution:**

<blockquote><p>Given,</p><p>We have to distribute <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> identical oranges to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> children,</p><p>Let children <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> get <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>O</mi><mi>A</mi></msub></math> oranges, children <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> gets <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>O</mi><mi>B</mi></msub></math> oranges and children <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> gets <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>O</mi><mi>C</mi></msub></math> oranges,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>O</mi><mi>A</mi></msub><mo>+</mo><msub><mi>O</mi><mi>B</mi></msub><mo>+</mo><msub><mi>O</mi><mi>C</mi></msub><mo>=</mo><mn>20</mn></math></p><p>Now this can be distributed using the multinomial theorem,</p><p>So, Number of ways will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>20</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi mathvariant="normal">x</mi><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mi>x</mi><mn>18</mn></msup></mrow></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>20</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><msup><mi>x</mi><mn>17</mn></msup></mrow></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>17</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>18</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>17</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi><msup><mo>)</mo><mrow><mo>-</mo><mn>3</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>19</mn></mmultiscripts><mo>=</mo><mn>171</mn></math></p><p>As we know that expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi><msup><mo>)</mo><mrow><mo>-</mo><mn>3</mn></mrow></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mi>x</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>17</mn><none></none><mprescripts></mprescripts><none></none><mn>19</mn></mmultiscripts><msup><mi>x</mi><mn>17</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#8734;</mo></math></p><p>Note: This is bonus question as here <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> oranges are considered identical but in question it is considered distinct.</p></blockquote>

</details>

---

### Q11. JEE Main 2023 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `1`

Number of integral solutions to the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>21</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>1</mn><mo>,</mo><mi>y</mi><mo>&#8805;</mo><mn>3</mn><mo>,</mo><mi>z</mi><mo>&#8805;</mo><mn>4</mn></math>, is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **105**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8805;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>&#8805;</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>-</mo><mn>3</mn><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>-</mo><mn>4</mn><mo>&#8805;</mo><mn>0</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>z</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>13</mn></math></p><p>So, number of non-negative integral solutions is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mrow><mn>13</mn><mo>+</mo><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><mo>=</mo><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>14</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>105</mn></math></p>

</details>

---

### Q12. JEE Main 2023 (25 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Suppose Anil&#39;s mother wants to give <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> whole fruits to Anil from a basket of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> red apples, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> white apples and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> oranges. If in the selected <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> fruits, at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> orange, at least one red apple and at least one white apple must be given, then the number of ways, Anil&#39;s mother can offer <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> fruits to Anil is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6860**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> Red apple<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>R</mi><mi>A</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> white apple<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>W</mi><mi>A</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> oranges <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">O</mi></mfenced></math></p><p>Now, for offering <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> fruits to be selected </p><p>Possible selections :- <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mi mathvariant="normal">O</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mi>R</mi><mi>A</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>WA</mi><mo>)</mo></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi mathvariant="normal">O</mi><mo>,</mo><mn>2</mn><mi>RA</mi><mo>,</mo><mn>1</mn><mi>WA</mi></mrow></mfenced></math>,  or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mi mathvariant="normal">O</mi><mo>,</mo><mn>1</mn><mi>RA</mi><mo>,</mo><mn>1</mn><mi>WA</mi></mrow></mfenced></math></p><p>Required number of ways</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1960</mn><mo>+</mo><mn>2940</mn><mo>+</mo><mn>1960</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6860</mn></math></p>

</details>

---

### Q13. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of ways to distribute <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math> identical candies among four children <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mo>,</mo><msub><mi>C</mi><mn>2</mn></msub><mo>,</mo><msub><mi>C</mi><mn>3</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>4</mn></msub></math> so that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub></math> receives atleast <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> and atmost <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> candies, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>3</mn></msub></math> receives atleast <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and atmost <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> candies, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>205</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>615</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>510</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>430</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>430</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><msub><mi>C</mi><mn>2</mn></msub><mo>+</mo><msub><mi>C</mi><mn>3</mn></msub><mo>+</mo><msub><mi>C</mi><mn>4</mn></msub><mo>=</mo><mn>30</mn></math></p><p>Now it has given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#8804;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>&#8804;</mo><mn>7</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>2</mn><mo>&#8804;</mo><msub><mi>C</mi><mn>3</mn></msub><mo>&#8804;</mo><mn>6</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>C</mi><mn>4</mn></msub></math> can take any value.</p><p>Finding coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>30</mn></msup></math> in</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>0</mn></msup><mo>+</mo><msup><mi>x</mi><mn>1</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mi>x</mi><mn>30</mn></msup></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mi>x</mi><mn>7</mn></msup></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>0</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mi>x</mi><mn>30</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>31</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mn>2</mn></msup><msup><mi>x</mi><mn>4</mn></msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>4</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><msup><mi>x</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>5</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced></math></p><p>{Ignoring higher power more than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mn>2</mn></msup><msup><mi>x</mi><mn>4</mn></msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>4</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><msup><mi>x</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>5</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>x</mi><mn>6</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>5</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>4</mn></mrow></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>x</mi><mn>6</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>5</mn></msup><mo>-</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>9</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>4</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>6</mn></msup><mo>-</mo><msup><mi>x</mi><mn>11</mn></msup><mo>-</mo><msup><mi>x</mi><mn>10</mn></msup><mo>+</mo><msup><mi>x</mi><mn>15</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>4</mn></mrow></msup></math></p><p>Required coefficient <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>24</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>4</mn><mo>+</mo><mn>24</mn><mo>-</mo><mn>1</mn></mrow></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>19</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>4</mn><mo>+</mo><mn>19</mn><mo>-</mo><mn>1</mn></mrow></mmultiscripts></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mo>&#160;</mo><mmultiscripts><mi>C</mi><mn>20</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>20</mn><mo>+</mo><mn>4</mn><mo>-</mo><mn>1</mn></mrow></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>15</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>15</mn><mo>+</mo><mn>4</mn><mo>-</mo><mn>1</mn></mrow></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>24</mn><none></none><mprescripts></mprescripts><none></none><mn>27</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>19</mn><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>20</mn><none></none><mprescripts></mprescripts><none></none><mn>23</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>15</mn><none></none><mprescripts></mprescripts><none></none><mn>18</mn></mmultiscripts></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>430</mn></math></p>

</details>

---

### Q14. JEE Main 2022 (27 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

The number of ways, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math> identical cubes, of which <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> are blue and rest are red, can be placed in a row so that between any two red cubes there should be at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> blue cubes, is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **56**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> blue &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> red spherical ball</p><p>Now according to question there should be minimum 2 blue ball in between any two red ball.</p><p>So assume <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>,</mo><mi>e</mi><mo>,</mo><mi>f</mi></math> are number of blue balls,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/31d6f758-d3c6-4489-b708-f0c9d81e48e1-d28.png" style="width: 311px; height: 40px;" /></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>e</mi><mo>+</mo><mi>f</mi><mo>=</mo><mn>11</mn><mo>&#160;</mo></math> ......(i)</p><p>Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>,</mo><mi>e</mi><mo>&#10878;</mo><mn>2</mn></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><msup><mi>b</mi><mo>&#39;</mo></msup><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><msup><mi>c</mi><mo>&#39;</mo></msup><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><msup><mi>d</mi><mo>&#39;</mo></msup><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><msup><mi>e</mi><mo>&#39;</mo></msup><mo>+</mo><mn>2</mn></math></p><p>So equation (i) becomes</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><msup><mi>b</mi><mo>&#39;</mo></msup><mo>+</mo><mn>2</mn><mo>+</mo><msup><mi>c</mi><mo>&#39;</mo></msup><mo>+</mo><mn>2</mn><mo>+</mo><msup><mi>d</mi><mo>&#39;</mo></msup><mo>+</mo><mn>2</mn><mo>+</mo><msup><mi>e</mi><mo>&#39;</mo></msup><mo>+</mo><mn>2</mn><mo>+</mo><mi>f</mi><mo>=</mo><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>a</mi><mo>+</mo><msup><mi>b</mi><mo>&#39;</mo></msup><mo>+</mo><msup><mi>c</mi><mo>&#39;</mo></msup><mo>+</mo><msup><mi>d</mi><mo>&#39;</mo></msup><mo>+</mo><msup><mi>e</mi><mo>&#39;</mo></msup><mo>+</mo><mi>f</mi><mo>=</mo><mn>3</mn></math></p><p>Now total ways will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mrow><mo>&#160;</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>-</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mrow><mn>6</mn><mo>-</mo><mn>1</mn></mrow></msub><msup><mo>=</mo><mn>8</mn></msup><msub><mi>C</mi><mn>5</mn></msub><msup><mo>=</mo><mn>8</mn></msup><msub><mi>C</mi><mn>3</mn></msub><mo>=</mo><mn>56</mn></math></p>

</details>

---

### Q15. JEE Main 2022 (25 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

The number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>-digit odd numbers, whose sum of digits is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>, is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **63**

**Detailed Solution:**

<p>Let the three-digit odd number be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mi>z</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>1</mn><mo>/</mo><mn>3</mn><mo>/</mo><mn>5</mn><mo>/</mo><mn>7</mn><mo>/</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>7</mn><mo>/</mo><mn>14</mn><mo>/</mo><mn>21</mn></math>  [for sum of digit to be multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>]</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>&#160;</mo><mo>=</mo><mn>6</mn><mo>/</mo><mn>4</mn><mo>/</mo><mn>2</mn><mo>/</mo><mn>13</mn><mo>/</mo><mn>11</mn><mo>/</mo><mn>9</mn><mo>/</mo><mn>7</mn><mo>/</mo><mn>5</mn><mo>/</mo><mn>20</mn><mo>/</mo><mn>18</mn><mo>/</mo><mn>16</mn><mo>/</mo><mn>14</mn><mo>/</mo><mn>12</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>6</mn><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Total possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Total possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Total possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>13</mn><mo>&#8658;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>9</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>Total possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>11</mn><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>9</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Total possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>9</mn><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>9</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Total possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>7</mn><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Total possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>5</mn><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Total possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>20</mn></math>  No possibilities</p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>18</mn><mo>&#8658;</mo><mfenced><mrow><mn>9</mn><mo>,</mo><mn>9</mn></mrow></mfenced></math></p><p>Total possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>16</mn><mo>&#8658;</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>9</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math></p><p>Total possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>14</mn><mo>&#8658;</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>9</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math></p><p>Total possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>12</mn><mo>&#8658;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>&#8230;</mo><mo>.</mo><mfenced><mrow><mn>9</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>Total possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn></math></p><p>Hence, the total number of three digit odd numbers whose sum of digit is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn></math></p>

</details>

---

### Q16. JEE Main 2022 (24 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

In an examination, there are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> multiple choice questions with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> choices, out of which exactly one is correct. There are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> marks for each correct answer, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math> marks for each wrong answer and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> mark if the question is not attempted. Then, the number of ways a student appearing in the examination gets <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> marks is _____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **40**

**Detailed Solution:**

<p>Let the marks obtained in each of the five MCQ be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>4</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>5</mn></msub></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><msub><mi>x</mi><mn>4</mn></msub><mo>+</mo><msub><mi>x</mi><mn>5</mn></msub><mo>=</mo><mn>5</mn></math></p><p>Only one possibility satisfies the above equation i.e.  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>2</mn></math></p><p>Hence, total number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>40</mn></math></p>

</details>

---

### Q17. JEE Main 2021 (25 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The total number of positive integral solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mi>z</mi><mo>=</mo><mn>24</mn></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>**

**Detailed Solution:**

<blockquote><p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mi>z</mi><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mi>z</mi><mo>=</mo><msup><mn>2</mn><mn>3</mn></msup><mo>&#215;</mo><msup><mn>3</mn><mn>1</mn></msup></math></p><p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msup><mn>2</mn><msub><mi>&#945;</mi><mn>1</mn></msub></msup><mo>&#215;</mo><msup><mn>3</mn><msub><mi>&#946;</mi><mn>1</mn></msub></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mn>2</mn><msub><mi>&#945;</mi><mn>2</mn></msub></msup><mo>&#215;</mo><msup><mn>3</mn><msub><mi>&#946;</mi><mn>2</mn></msub></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><msup><mn>2</mn><msub><mi>&#945;</mi><mn>3</mn></msub></msup><mo>&#215;</mo><msup><mn>3</mn><msub><mi>&#946;</mi><mn>2</mn></msub></msup></math></p><p>where,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#945;</mi><mn>2</mn></msub><mo>+</mo><msub><mi>&#945;</mi><mn>3</mn></msub><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#946;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#946;</mi><mn>2</mn></msub><mo>+</mo><msub><mi>&#946;</mi><mn>3</mn></msub><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Number of non-negative integral solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>=</mo><mn>10</mn></math> </p><p>Number of non-negative integral solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mo>=</mo><mn>3</mn></math></p><p>Total number of positive integral solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mi>z</mi></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mi>z</mi><mo>=</mo><mn>24</mn></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>30</mn></math></p></blockquote>

</details>

---

### Q18. JEE Main 2020 (03 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

The total number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo></math>digit numbers whose sum of digits is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>, is ..........

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **54**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mi>z</mi></math> be the three-digit number such that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>&#8805;</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi>t</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>1</mn><mo>&#8658;</mo><mi>t</mi><mo>+</mo><mn>1</mn><mo>&#8805;</mo><mn>1</mn><mo>&#8658;</mo><mi>t</mi><mo>&#8805;</mo><mn>0</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>10</mn><mo>&#8658;</mo><mi>t</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>10</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>9</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>t</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>&#8804;</mo><mn>9</mn></math></p><p>Thus, total number of non-negative integral solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mn>9</mn><mo>+</mo><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>=</mo><mfrac><mrow><mn>11</mn><mo>.</mo><mn>10</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>55</mn></math></p><p>But for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>10</mn></math>, so required number of integers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>55</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>54</mn></math>.</p>

</details>

---

