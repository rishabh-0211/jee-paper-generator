# JEE Advanced Mathematics - Matrices

## Topic 7: Inverse of a Matrix

**Total Questions:** 6

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Which one of the following matrices can be obtained by performing elementary row transformations on the $3 \times 3$ identity matrix?

**Options:**

- **(A)** $\begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$
- **(B)** $\begin{bmatrix} 1 & 1 & 1 \\ 2 & 3 & 4 \\ 1 & 2 & 1 \end{bmatrix}$
- **(C)** $\begin{bmatrix} 1 & 1 & 1 \\ 2 & 3 & 4 \\ 2 & 5 & 8 \end{bmatrix}$
- **(D)** $\begin{bmatrix} 1 & 1 & 1 \\ -1 & 1 & 2 \\ 0 & 2 & 3 \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\begin{bmatrix} 1 & 1 & 1 \\ 2 & 3 & 4 \\ 1 & 2 & 1 \end{bmatrix}$**

**Detailed Solution:**

Any matrix obtained by performing elementary row transformations on the identity matrix is equivalent to the identity matrix, which means it must be non-singular (invertible). Therefore, its determinant must be non-zero.

Evaluating the determinant of the matrix in option (A):
$\begin{vmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{vmatrix} = 0$

Evaluating the determinant of the matrix in option (B):
$\begin{vmatrix} 1 & 1 & 1 \\ 2 & 3 & 4 \\ 1 & 2 & 1 \end{vmatrix} = 1(3 - 8) - 1(2 - 4) + 1(4 - 3) = -5 + 2 + 1 = -2 \neq 0$

Evaluating the determinant of the matrix in option (C):
$\begin{vmatrix} 1 & 1 & 1 \\ 2 & 3 & 4 \\ 2 & 5 & 8 \end{vmatrix} = 1(24 - 20) - 1(16 - 8) + 1(10 - 6) = 4 - 8 + 4 = 0$

Evaluating the determinant of the matrix in option (D):
$\begin{vmatrix} 1 & 1 & 1 \\ -1 & 1 & 2 \\ 0 & 2 & 3 \end{vmatrix} = 1(3 - 4) - 1(-3 - 0) + 1(-2 - 0) = -1 + 3 - 2 = 0$

Since only the matrix in option (B) has a non-zero determinant, it is the only one that can be obtained from the identity matrix by elementary row transformations.

Answer: $\begin{bmatrix} 1 & 1 & 1 \\ 2 & 3 & 4 \\ 1 & 2 & 1 \end{bmatrix}$

</details>

---

### Q2. JEE Advanced 2023 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfenced><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced><mo>,</mo><mo>&#160;</mo><mi>i</mi><mo>,</mo><mo>&#160;</mo><mi>j</mi><mo>&#8712;</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>}</mo></math>, be the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><mn>1</mn></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>j</mi><mo>+</mo><mn>1</mn></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>, otherwise <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><mn>0</mn></math>. Then which of the following statements is(are) true?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is invertible
- **(B)** There exists a nonzero column matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mfenced><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><mo>-</mo><msub><mi>a</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><mo>-</mo><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math>
- **(C)** The set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>X</mi><mo>&#8712;</mo><msup><mi mathvariant="normal">&#8477;</mi><mn>3</mn></msup><mo>:</mo><mi>M</mi><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>&#8800;</mo><mo>{</mo><mn>0</mn><mo>}</mo></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math>
- **(D)** The matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>M</mi><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>I</mi><mo>)</mo></math> is invertible, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> is the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> identity matrix

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) The set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>X</mi><mo>&#8712;</mo><msup><mi mathvariant="normal">&#8477;</mi><mn>3</mn></msup><mo>:</mo><mi>M</mi><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>&#8800;</mo><mo>{</mo><mn>0</mn><mo>}</mo></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfenced separators="|"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced><mo>,</mo><mo>&#160;</mo><mi>i</mi><mo>,</mo><mo>&#160;</mo><mi>j</mi><mo>&#8712;</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><mn>1</mn><mtext>&#160;if&#160;</mtext><mi>j</mi><mo>+</mo><mn>1</mn><mtext>&#160;is divisible by&#160;</mtext><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>otherwise&#160;</mtext><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>11</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>12</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>13</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>21</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>22</mn></msub><mo>=</mo><mn>0</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><msub><mi>a</mi><mn>33</mn></msub><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable columnalign="left left left" columnspacing="1em" rowspacing="4pt"><mtr><mtd><mn>1</mn><mo>&#8197;&#8197;&#8197;&#8197;</mo><mn>1</mn><mo>&#8197;&#8197;&#8197;&#8197;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>&#8197;&#8197;&#8197;&#8197;</mo><mn>0</mn><mo>&#8197;&#8197;&#8197;&#8197;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>&#8197;&#8197;&#8197;&#8197;</mo><mn>1</mn><mo>&#8197;&#8197;&#8197;&#8197;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>M</mi><mo>|</mo><mo>=</mo><mn>1</mn><mo>(</mo><mo>&#8722;</mo><mn>1</mn><mo>)</mo><mo>&#8722;</mo><mn>1</mn><mo>(</mo><mo>&#8722;</mo><mn>1</mn><mo>)</mo><mo>=</mo><mo>&#8722;</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is not invertible</p><p>Now solving option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><mo>-</mo><msub><mi>a</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><mo>-</mo><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><mo>-</mo><msub><mi>a</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><mo>-</mo><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math></p><p>Now on comparing we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mo>-</mo><msub><mi>a</mi><mn>2</mn></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><msub><mi>a</mi><mn>3</mn></msub></math></p><p>Now on solving we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math></p><p>So, there will be infinite possibility for <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>a</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> There exist a column matrix (infinite possibilities)</p><p>Now solving option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>C</mi></mfenced></math> we get,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd></mtr><mtr><mtd><mi>z</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mi>z</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Now on comparing we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>y</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></math></p><p>Yes it is possible</p><p>Now solving option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>D</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>M</mi><mo>&#8722;</mo><mn>2</mn><mi>I</mi><mo>|</mo><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable columnalign="center center center" columnspacing="1em" rowspacing="4pt"><mtr><mtd><mo>&#8722;</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>&#8722;</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>&#8722;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>M</mi><mo>&#8722;</mo><mn>2</mn><mi>I</mi><mo>|</mo><mo>=</mo><mo>&#8722;</mo><mn>1</mn><mfenced><mn>3</mn></mfenced><mo>&#8722;</mo><mn>1</mn><mfenced><mrow><mo>&#8722;</mo><mn>2</mn><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>&#8722;</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p>Hence, it is not invertible.</p>

</details>

---

### Q3. JEE Advanced 2021 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

For any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>M</mi><mo>|</mo></math> denote the determinant of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> be the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> identity matrix. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math> be two <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrices such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>I</mi><mo>-</mo><mi>E</mi><mi>F</mi><mo>)</mo></math> is invertible. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mo>=</mo><mo>(</mo><mi>I</mi><mo>-</mo><mi>E</mi><mi>F</mi><msup><mo>)</mo><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, then which of the following statements is (are) TRUE ?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>F</mi><mi>E</mi><mo>|</mo><mo>=</mo><mo>|</mo><mi>I</mi><mo>-</mo><mi>F</mi><mi>E</mi><mo>|</mo><mo>|</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>|</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>I</mi><mo>-</mo><mi>F</mi><mi>E</mi><mo>)</mo><mo>(</mo><mi>I</mi><mo>+</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>)</mo><mo>=</mo><mi>I</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mi>F</mi><mi>G</mi><mo>=</mo><mi>G</mi><mi>E</mi><mi>F</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>I</mi><mo>-</mo><mi>F</mi><mi>E</mi><mo>)</mo><mo>(</mo><mi>I</mi><mo>-</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>)</mo><mo>=</mo><mi>I</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mi>F</mi><mi>G</mi><mo>=</mo><mi>G</mi><mi>E</mi><mi>F</mi></math>**

**Detailed Solution:**

<p>(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mo>=</mo><mo>(</mo><mi>I</mi><mo>-</mo><mi>E</mi><mi>F</mi><msup><mo>)</mo><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>=</mo><mi>F</mi><mo>(</mo><mi>I</mi><mo>-</mo><mi>E</mi><mi>F</mi><msup><mo>)</mo><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>E</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><msup><mi>E</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>I</mi><mo>-</mo><mi>E</mi><mi>F</mi><mo>)</mo><msup><mi>F</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>=</mo><msup><mfenced><mrow><msup><mi>E</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi>F</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mi>I</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>|</mo><mo>&#183;</mo><mfenced close="|" open="|"><mrow><msup><mi>E</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi>F</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mi>I</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>|</mo><mo>&#183;</mo><mfenced close="|" open="|"><mrow><msup><mi>E</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi>F</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mi>I</mi></mrow></mfenced><mo>|</mo><mi>F</mi><mi>E</mi><mo>|</mo><mo>=</mo><mo>|</mo><mi>F</mi><mi>E</mi><mo>|</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>|</mo><mo>|</mo><mi>I</mi><mo>-</mo><mi>F</mi><mi>E</mi><mo>|</mo><mo>=</mo><mo>|</mo><mi>F</mi><mi>E</mi><mo>|</mo></math></p><p>(B) &amp; (D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>I</mi><mo>-</mo><mi>F</mi><mi>E</mi><mo>)</mo><mo>&#183;</mo><mo>(</mo><mi>I</mi><mo>+</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>I</mi><mo>+</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>-</mo><mi>F</mi><mi>E</mi><mo>-</mo><mi>F</mi><mi>E</mi><mo>&#183;</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>I</mi><mo>+</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>-</mo><mi>F</mi><mi>E</mi><mo>-</mo><mi>F</mi><mo>(</mo><mi>G</mi><mo>-</mo><mi>I</mi><mo>)</mo><mi>E</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>I</mi><mo>+</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>-</mo><mi>F</mi><mi>E</mi><mo>-</mo><mi>F</mi><mi>G</mi><mi>E</mi><mo>+</mo><mi>F</mi><mi>E</mi><mo>=</mo><mi>I</mi></math></p><p>(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>I</mi><mo>-</mo><mi>E</mi><mi>F</mi><mo>)</mo><mi>G</mi><mo>=</mo><mi>I</mi><mo>=</mo><mi>G</mi><mo>(</mo><mi>I</mi><mo>-</mo><mi>E</mi><mi>F</mi><mi>G</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>G</mi><mo>-</mo><mi>E</mi><mi>F</mi><mi>G</mi><mo>=</mo><mi>I</mi><mo>=</mo><mi>G</mi><mo>-</mo><mi>G</mi><mi>E</mi><mi>F</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mi>F</mi><mi>G</mi><mo>=</mo><mi>G</mi><mi>E</mi><mi>F</mi></math></p>

</details>

---

### Q4. JEE Advanced 2019 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi mathvariant="normal">M</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mtd><mtd><mo>-</mo><mn>1</mn><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mtd></mtr><mtr><mtd><mn>1</mn><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mtd><mtd><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi mathvariant="normal">&#945;</mi><mi mathvariant="normal">I</mi><mo>+</mo><mi mathvariant="normal">&#946;</mi><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>,</mo></math> where <math><mi mathvariant="normal">&#945;</mi><mo>=</mo><mi mathvariant="normal">&#945;</mi><mfenced separators="|"><mrow><mi mathvariant="normal">&#952;</mi></mrow></mfenced></math> and <math><mi mathvariant="normal">&#946;</mi><mo>=</mo><mi mathvariant="normal">&#946;</mi><mfenced separators="|"><mrow><mi mathvariant="normal">&#952;</mi></mrow></mfenced></math> are real number, and <math><mi mathvariant="normal">I</mi></math> is the <math><mn>2</mn><mo>&#215;</mo><mn>2</mn></math> identity matrix. If <math><msup><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mi mathvariant="normal">*</mi></mrow></msup></math> is the minimum of the set { <math><mi mathvariant="normal">&#945;</mi><mfenced separators="|"><mrow><mi mathvariant="normal">&#952;</mi></mrow></mfenced><mo>:</mo><mi mathvariant="normal">&#952;</mi><mo>&#8712;</mo><mfenced open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi mathvariant="normal">&#160;</mi><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow></mfenced><mo>}</mo></math> and <math><msup><mrow><mi mathvariant="normal">&#946;</mi></mrow><mrow><mi mathvariant="normal">*</mi></mrow></msup></math> is the minimum of the set <math><mfenced close="}" open="{" separators="|"><mrow><mi mathvariant="normal">&#946;</mi><mfenced separators="|"><mrow><mi mathvariant="normal">&#952;</mi></mrow></mfenced><mo>:</mo><mi mathvariant="normal">&#952;</mi><mo>&#8712;</mo><mfenced open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi mathvariant="normal">&#160;</mi><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow></mfenced></mrow></mfenced><mo>,</mo></math> then the value of <math><msup><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mi mathvariant="normal">*</mi></mrow></msup><mo>+</mo><msup><mrow><mi mathvariant="normal">&#946;</mi></mrow><mrow><mi mathvariant="normal">*</mi></mrow></msup></math> is

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>37</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(B)** <math><mo>-</mo><mfrac><mrow><mn>31</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>29</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>17</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>-</mo><mfrac><mrow><mn>29</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>**

**Detailed Solution:**

Method I
As given, <math><mi>M</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><mo>-</mo><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd></mtr><mtr><mtd><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi>&#945;</mi><mi>I</mi><mo>+</mo><mi>&#946;</mi><msup><mrow><mi>M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
<math><mi>a</mi><mi>d</mi><mi>j</mi><mtext>&#8201;</mtext><mfenced separators="|"><mrow><mi>M</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></mtd></mtr></mtable></mrow></mfenced></math>
<math><msup><mrow><mi>M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mo>|</mo><mi>M</mi><mo>|</mo></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></mtd></mtr></mtable></mrow></mfenced></math>
<math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><mo>-</mo><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd></mtr><mtr><mtd><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi>&#945;</mi><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>+</mo><mfrac><mrow><mi>&#946;</mi></mrow><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>M</mi></mrow></mfenced></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></mtd></mtr></mtable></mrow></mfenced></math>
Compare element <math><msub><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>12</mn></mrow></msub></math> in L.H.S. and R.H.S.
<math><mo>-</mo><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi><mo>=</mo><mn>0</mn><mo>+</mo><mfrac><mrow><mi>&#946;</mi></mrow><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>M</mi></mrow></mfenced></mrow></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mrow></mfenced></math>
<math><mi>&#946;</mi><mo>=</mo><mtext>&#8201;</mtext><mo>|</mo><mi>M</mi><mo>|</mo></math> ...(iii)
Compare element <math><msub><mrow><mi>a</mi></mrow><mrow><mn>11</mn></mrow></msub></math> in LHS. and R.H.S.
<math><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi><mo>=</mo><mi>&#945;</mi><mo>+</mo><mfrac><mrow><mi>&#946;</mi></mrow><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>M</mi></mrow></mfenced></mrow></mfrac><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></mrow></mfenced></math>
From equation (iii)
<math><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi><mo>=</mo><mi>&#945;</mi><mo>-</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></math>
<math><mi>&#945;</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></math> ...(iv)
Now from equation (iv)
<math><mi>&#945;</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></math>
<math><mi>&#945;</mi><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></math>
<math><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mn>2</mn><mi>&#952;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mn>0</mn><mo>&#8804;</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mn>2</mn><mi>&#952;</mi><mo>&#8804;</mo><mn>1</mn></math>
<math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#8804;</mo><mfrac><mrow><mo>-</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mn>2</mn><mi>&#952;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn></math>
<math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn><mo>-</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mn>2</mn><mi>&#952;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math>
<math><mi>&#945;</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math> , <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mi>&#945;</mi><mo>*</mo></math>
For <math><mi>&#946;</mi></math> , consider
<math><mfenced close="|" open="|" separators="|"><mrow><mi>M</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi><mo>+</mo><mn>2</mn></math>
<math><mfenced close="|" open="|" separators="|"><mrow><mi>M</mi></mrow></mfenced><mfenced close="}" open="{" separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></math>
<math><mfenced close="|" open="|" separators="|"><mrow><mi>M</mi></mrow></mfenced><mfenced close="}" open="{" separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mn>2</mn><mi>&#952;</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></math>
<math><mn>0</mn><mo>&#8804;</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mn>2</mn><mi>&#952;</mi><mo>&#8804;</mo><mn>1</mn></math>
Hence, <math><mfenced close="|" open="|" separators="|"><mrow><mi>M</mi></mrow></mfenced><mtext>&#8201;</mtext><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mo>,</mo><mfrac><mrow><mn>37</mn></mrow><mrow><mn>16</mn></mrow></mfrac></mrow></mfenced></math>
<math><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfenced close="|" open="|" separators="|"><mrow><mi>M</mi></mrow></mfenced></math>
<math><mi>&#946;</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>37</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#946;</mi><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></msub><mo>=</mo><mo>-</mo><mfrac><mn>37</mn><mn>16</mn></mfrac><mo>=</mo><mi>&#946;</mi><mo>*</mo></math>
<math><mi>&#945;</mi><mi>*</mi><mo>+</mo><mi>&#946;</mi><mi>*</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>37</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mn>29</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
Method II
<math><mi>M</mi><mo>=</mo><mi>&#945;</mi><mi>I</mi><mo>+</mo><mi>&#946;</mi><msup><mrow><mi>M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
Multiply with <math><mi>M</mi></math> both side
<math><msup><mrow><mi>M</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>&#945;</mi><mi>M</mi><mo>+</mo><mi>&#946;</mi><mi>I</mi></math>
<math><msup><mrow><mi>M</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>&#945;</mi><mi>M</mi><mo>-</mo><mi>B</mi><mi>I</mi><mo>=</mo><mn>0</mn></math> ...(i)
Equation (i) represents characteristic equation of matrix <math><mi>&#8216;</mi><mi>M</mi><mi>&#8217;</mi></math>
Hence, Trace <math><mo>(</mo><mi>M</mi><mo>)</mo><mo>=</mo><mi>&#945;</mi></math>
<math><mfenced close="|" open="|" separators="|"><mrow><mi>M</mi></mrow></mfenced><mtext>&#8201;</mtext><mo>=</mo><mo>-</mo><mi>&#946;</mi></math>
Sum of roots of characteristic equation <math><mo>=</mo></math> Trace of matrix
Product of roots of characteristic equation <math><mo>=</mo></math> determined of matrix
<math><mo>&#8756;</mo><mtext>&#8201;</mtext><mi>&#945;</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi></math>
<math><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi>&#952;</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math>
Now proceed as Method 1

</details>

---

### Q5. JEE Advanced 2014 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `1`

Let M be a <math><mn>2</mn><mi>&#160;</mi><mo>&#215;</mo><mn>2</mn></math> symmetric matrix with integer entries. Then M is invertible if

**Options:**

- **(A)** The first column of M is the transpose of the second row of M
- **(B)** The second row of M is the transpose of the first column of M
- **(C)** M is a diagonal matrix with non - zero entries in the main diagonal
- **(D)** The product of entries in the main diagonal of M is not the square of an integer

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The product of entries in the main diagonal of M is not the square of an integer**

**Detailed Solution:**

Let  <math><mi>M</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mrow></mfenced></math>   (where a, b, c  <math><mo>∈</mo><mi>I</mi></math> ) 
Then Det  <math><mi>M</mi><mo>=</mo><mi>a</mi><mi>b</mi><mo>-</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></math> 
If  <math><mi>a</mi><mo>=</mo><mi>b</mi><mo>=</mo><mi>c</mi><mo>,</mo><mi> </mi><mi>D</mi><mi>e</mi><mi>t</mi><mfenced separators="|"><mrow><mi>M</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> 
If  <math><mi>c</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>a</mi><mo>,</mo><mi> </mi><mi>b</mi><mi> </mi><mo>≠</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>D</mi><mi>e</mi><mi>t</mi><mi> </mi><mfenced separators="|"><mrow><mi>M</mi></mrow></mfenced><mo>≠</mo><mn>0</mn></math> 
If  <math><mi>a</mi><mi>b</mi><mi> </mi><mo>≠</mo><mi> </mi></math> square of integer,  <math><mi>D</mi><mi>e</mi><mi>t</mi><mi> </mi><mfenced separators="|"><mrow><mi>M</mi></mrow></mfenced><mo>≠</mo><mn>0</mn></math>

</details>

---

### Q6. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Read the following passage and answer the questions.<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/88iLE50zA6etAHkOmNt74CAbkJliurfrRZp8CzupJk0.original.fullsize.png">
<strong>Question:</strong>
The value of the elements of $U^{-1}$ is

**Options:**

- **(A)** $-1$
- **(B)** 0
- **(C)** 1
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-1$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/YBHdmRS2Jayt5PH1g06WziEPbMaRY-1B-tsUnQ-177g.original.fullsize.png">

</details>

---

