# JEE Main Mathematics - Matrices

## Topic 1: Formation and Basic of Matrix

**Total Questions:** 25

---

### Q1. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $M$ be a $3 \times 3$ matrix such that $M \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$, $M \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix}$ and $M \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}$. If $M \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 7 \\ 11 \end{pmatrix}$, then $x + y + z$ equals :

**Options:**

- **(A)** $4$
- **(B)** $5$
- **(C)** $7$
- **(D)** $11$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $5$**

**Detailed Solution:**

Let $M$ be the matrix whose columns are the given vectors. We have:

$M = \begin{pmatrix} 1 & 0 & -1 \\ 2 & 1 & 1 \\ 3 & 2 & 1 \end{pmatrix}$

Given $M \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 7 \\ 11 \end{pmatrix}$, we can write this as a system of linear equations:

$x - z = 1$

$2x + y + z = 7$

$3x + 2y + z = 11$

Subtracting the second equation from the third equation gives:

$x + y = 4$

Adding the first equation and the second equation gives:

$3x + y = 8$

Subtracting the equation $x + y = 4$ from $3x + y = 8$ gives:

$2x = 4 \Rightarrow x = 2$

Substituting $x = 2$ into $x + y = 4$ gives:

$2 + y = 4 \Rightarrow y = 2$

Substituting $x = 2$ into $x - z = 1$ gives:

$2 - z = 1 \Rightarrow z = 1$

Therefore, $x + y + z = 2 + 2 + 1 = 5$.

Answer: $5$

</details>

---

### Q2. JEE Main 2025 (7 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of singular matrices of order 2 , whose elements are from the set $\{2,3,6,9\}$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

$\left|\begin{array}{ll}
\mathrm{a} & \mathrm{~d} \\
\mathrm{~b} & \mathrm{c}
\end{array}\right|=\mathrm{ad}-\mathrm{bc} \Rightarrow \mathrm{ad}=\mathrm{bc}$
Case-I Exactly 1 no. is used
$\Rightarrow \text { All singular }={ }^4 \mathrm{C}_1$
Case-II Exactly 2 no. is used
$\Rightarrow{ }^4 \mathrm{C}_2 \times 2 \times 2$
Case-III Exactly 3 no. is used
None will be singular
Case-IV Exactly 4 No. is used
ad=bc
$\begin{aligned} & \Rightarrow 2 \times 9=3 \times 6 \\ & \left|\begin{array}{ll}9 & - \\ - & 2\end{array}\right| \Rightarrow{ }^4 \mathrm{C}_1 \times 21\end{aligned}$
Total $=36$

</details>

---

### Q3. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha \beta \neq 0$ and $A=\left[\begin{array}{rrr}\beta & \alpha & 3 \\ \alpha & \alpha & \beta \\ -\beta & \alpha & 2 \alpha\end{array}\right]$. If $B=\left[\begin{array}{rrr}3 \alpha & -9 & 3 \alpha \\ -\alpha & 7 & -2 \alpha \\ -2 \alpha & 5 & -2 \beta\end{array}\right]$ is the matrix of cofactors of the elements of $A$, then $\operatorname{det}(A B)$ is equal to :

**Options:**

- **(A)** 64
- **(B)** 216
- **(C)** 343
- **(D)** 125

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 216**

**Detailed Solution:**

Equating co-factor fo $\mathrm{A}_{21}$
$\begin{aligned}
& \left(2 \alpha^2-3 \alpha\right)=\alpha \\
& \alpha=0,2 \text { (accept) }
\end{aligned}$
Now, $2 \alpha^2-\alpha \beta=3 \alpha$
$\begin{aligned}
& \alpha=2 \quad \beta=1 \\
& |\mathrm{AB}|=|\mathrm{A} \operatorname{cof}(\mathrm{A})|=|\mathrm{A}|^3 \\
& \mathrm{~A}=\left|\begin{array}{lll}
1 & 2 & 3 \\
2 & 2 & 1 \\
-1 & 2 & 4
\end{array}\right|=6-2(9)+3(6)=6
\end{aligned}$

</details>

---

### Q4. JEE Main 2024 (04 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $A$ be a $2 \times 2$ symmetric matrix such that $A\left[\begin{array}{l}1 \\ 1\end{array}\right]=\left[\begin{array}{l}3 \\ 7\end{array}\right]$ and the determinant of $A$ be 1 . If $A^{-1}=\alpha A+\beta I$, where $I$ is an identity matrix of order $2 \times 2$, then $\alpha+\beta$ equals _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$\begin{aligned} & \text { Let } A=\left[\begin{array}{ll}a & b \\ b & d\end{array}\right] \\ & {\left[\begin{array}{ll}a & b \\ b & d\end{array}\right]\left[\begin{array}{l}1 \\ 1\end{array}\right]=\left[\begin{array}{l}3 \\ 7\end{array}\right], a d-b^2=1} \\ & a+b=3, b+d=7,(3-b)(7-b)-b^2=1 \\ & 21-10 b=1 \rightarrow b=2, a=1, d=5 \\ & A=\left[\begin{array}{ll}1 & 2 \\ 2 & 5\end{array}\right], A^{-1}=\left[\begin{array}{cc}5 & -2 \\ -2 & 1\end{array}\right] \\ & A^{-1}=\alpha A+\beta I \\ & {\left[\begin{array}{cc}5 & -2 \\ -2 & 1\end{array}\right]=\left[\begin{array}{cc}\alpha+\beta & 2 \alpha \\ 2 \alpha & 5 \alpha+\beta\end{array}\right]} \\ & \alpha=-1, \beta=6 \rightarrow \alpha+\beta=5\end{aligned}$

</details>

---

### Q5. JEE Main 2024 (04 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $A$ be a $3 \times 3$ matrix of non-negative real elements such that $A\left[\begin{array}{l}1 \\ 1 \\ 1\end{array}\right]=3\left[\begin{array}{l}1 \\ 1 \\ 1\end{array}\right]$. Then the maximum value of $\operatorname{det}(\mathrm{A})$ is ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **27**

**Detailed Solution:**

$\begin{aligned} \text { Let } A & =\left[\begin{array}{lll}a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3\end{array}\right] \\ A\left[\begin{array}{l}1 \\ 1 \\ 1\end{array}\right] & =3\left[\begin{array}{l}1 \\ 1 \\ 1\end{array}\right]\end{aligned}$
$\Rightarrow a_1+a_2+a_3=3$ ...(1)
$\Rightarrow b_1+b_2+b_3=3$ ...(2)
$\Rightarrow c_1+\mathrm{ca}_2+\mathrm{c}_3=3$ ...(3)
Now,
$\begin{aligned}
& |A|=\left(a_1 b_2 c_3+a_2 b_3 c_1+a_3 b_1 c_2\right) \\
& -\left(a_3 b_2 c_1+a_2 b_1 c_3+a_1 b_3 c_2\right)
\end{aligned}$
$\therefore$ From above in formation, clearly $|\mathrm{A}|_{\max }=27$, when $a_1=3, b_2=3, c_3=3$

</details>

---

### Q6. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The number of symmetric matrices of order 3, with all the entries from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>9</mn><mo>}</mo></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>6</mn><mn>10</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>6</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>9</mn><mn>10</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>9</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>6</mn></msup></math>**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mn>8</mn><mo>,</mo><mn>9</mn><mo>}</mo></math></p><p>We need to find the number of symmetric matrices.</p><p>We know that a matrix is symmetric if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mi>&#964;</mi></msup><mo>=</mo><mi>A</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>11</mn></msub></mtd><mtd><msub><mi>a</mi><mn>12</mn></msub></mtd><mtd><msub><mi>a</mi><mn>13</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>21</mn></msub></mtd><mtd><msub><mi>a</mi><mn>22</mn></msub></mtd><mtd><msub><mi>a</mi><mn>23</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>31</mn></msub></mtd><mtd><msub><mi>a</mi><mn>32</mn></msub></mtd><mtd><msub><mi>a</mi><mn>33</mn></msub></mtd></mtr></mtable></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>11</mn></msub><mo>,</mo><msub><mi>a</mi><mn>22</mn></msub><mo>,</mo><msub><mi>a</mi><mn>33</mn></msub></math> can have any digit from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>.</p><p>Number of ways this can be done is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><msup><mn>10</mn><mn>3</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>12</mn></msub><mo>=</mo><msub><mi>a</mi><mn>21</mn></msub></math>. So number of ways this can be done is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#215;</mo><mn>1</mn></math>.</p><p>Similarly <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>13</mn></msub><mo>=</mo><msub><mi>a</mi><mn>31</mn></msub></math>, So number of ways this can be done is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#215;</mo><mn>1</mn></math>.</p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>23</mn></msub><mo>=</mo><msub><mi>a</mi><mn>32</mn></msub></math>. So number of ways this can be done is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#215;</mo><mn>1</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Total symmetric matrix<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>10</mn><mn>3</mn></msup><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><msup><mn>10</mn><mn>6</mn></msup></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q7. JEE Main 2023 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="&#8970;" close="&#8971;"><msub><mi>a</mi><mrow><mover><mi>i</mi><mo>^</mo></mover><mover><mi>j</mi><mo>^</mo></mover></mrow></msub></mfenced><mo>&#183;</mo><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>&#8712;</mo><mi>Z</mi><mo>&#8745;</mo><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>&#8804;</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>&#8804;</mo><mn>2</mn></math>. The number of matrices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> such that the sum of all entries is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> prime number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>13</mn></mrow></mfenced></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **204**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>11</mn></msub></mtd><mtd><msub><mi>a</mi><mn>12</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>21</mn></msub></mtd><mtd><msub><mi>a</mi><mn>22</mn></msub></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>a</mi><mn>11</mn></msub><mo>,</mo><msub><mi>a</mi><mn>12</mn></msub><mo>,</mo><msub><mi>a</mi><mn>21</mn></msub><mo>,</mo><msub><mi>a</mi><mn>22</mn></msub><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>Now given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>11</mn></msub><mo>+</mo><msub><mi>a</mi><mn>12</mn></msub><mo>+</mo><msub><mi>a</mi><mn>23</mn></msub><mo>+</mo><msub><mi>a</mi><mn>22</mn></msub><mo>=</mo></math> prime number,</p><p>So sum can be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn></math></p><p>Now using multinomial theorem we get,</p><p>Sum will be sum of coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>,</mo><mo>&#160;</mo><msup><mi>x</mi><mn>5</mn></msup><mo>,</mo><mo>&#160;</mo><msup><mi>x</mi><mn>7</mn></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>11</mn></msup></math>in expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mn>0</mn></msup><mo>+</mo><msup><mi>x</mi><mn>1</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>5</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mn>4</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>5</mn></msup></mrow></mfenced><mn>4</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>4</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mmultiscripts><mi>C</mi><msub><mi>r</mi><mn>1</mn></msub><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><msup><mfenced><mrow><mo>-</mo><msup><mi>x</mi><mn>5</mn></msup></mrow></mfenced><msub><mi>r</mi><mn>1</mn></msub></msup></mrow></mfenced><mfenced><mrow><mmultiscripts><mi>C</mi><msub><mi>r</mi><mn>2</mn></msub><none></none><mprescripts></mprescripts><none></none><mrow><mn>4</mn><mo>+</mo><msub><mi>r</mi><mn>2</mn></msub><mo>-</mo><mn>1</mn></mrow></mmultiscripts><msup><mi>x</mi><msup><mi>r</mi><mn>2</mn></msup></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mn>1</mn></mrow><mrow><mn>3</mn><mo>+</mo><msub><mi>r</mi><mn>2</mn></msub></mrow><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><msub><mi>C</mi><mrow><mi>r</mi><mn>2</mn></mrow></msub><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><msub><mi>r</mi><mn>1</mn></msub></msup><msup><mfenced><mi>x</mi></mfenced><msup><mrow></mrow><mrow><mn>5</mn><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><msub><mi>r</mi><mn>2</mn></msub></mrow></msup></msup></math></p><p>Now taking, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn></math></p><p>when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn><mo>&#8658;</mo><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn></math></p><p>when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn><mo>&#8658;</mo><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math></p><p>when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>7</mn><mo>&#8658;</mo><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>7</mn></math></p><p>when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>11</mn><mo>&#8658;</mo><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>11</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>6</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn></math></p><p>So, sum of all coefficient <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>11</mn><none></none><mprescripts></mprescripts><none></none><mn>14</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mo>+</mo><mn>56</mn><mo>-</mo><mn>4</mn><mo>+</mo><mn>120</mn><mo>-</mo><mn>40</mn><mo>+</mo><mn>364</mn><mo>-</mo><mn>336</mn><mo>+</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>204</mn></math></p>

</details>

---

### Q8. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of square matrices of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> with entries from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>}</mo></math>, such that the sum of all the elements in each row is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and the sum of all the elements in each column is also <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>225</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>125</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math>**

**Detailed Solution:**

<p>Given,</p><p>A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#215;</mo><mn>5</mn></math> matrix whose each entry is either <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>, is such that sum of entries of each column as well as each row is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>,</p><p>Taking a possible case we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now arranging the above case we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="}" open=""><mtable><mtr><mtd><mo>&#8594;</mo><mn>5</mn><mo>&#160;</mo><mtext>ways</mtext></mtd></mtr><mtr><mtd><mo>&#8594;</mo><mn>4</mn><mo>&#160;</mo><mtext>ways</mtext></mtd></mtr><mtr><mtd><mo>&#8594;</mo><mn>3</mn><mo>&#160;</mo><mtext>ways</mtext></mtd></mtr><mtr><mtd><mo>&#8594;</mo><mn>2</mn><mo>&#160;</mo><mtext>ways</mtext></mtd></mtr><mtr><mtd><mo>&#8594;</mo><mn>1</mn><mo>&#160;</mo><mtext>way</mtext></mtd></mtr></mtable></mfenced></math> because if we fix <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> at first row and first column then in second row first column <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> cannot come and vice-versa.</p><p>So total number of such matrices will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>=</mo><mn>120</mn></math></p>

</details>

---

### Q9. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following matrices can NOT be obtained from the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> by a single elementary row operation?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>7</mn></mtd></mtr></mtable></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable columnalign="right"><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>7</mn></mtd></mtr></mtable></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>(1) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>(2) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>&#8596;</mo><msub><mi>R</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math> </p><p>(3) Option is not possible</p><p>(4) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>+</mo><mn>2</mn><msub><mi>R</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math> </p></blockquote>

</details>

---

### Q10. JEE Main 2022 (29 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

The number of matrices of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math>, whose entries are either <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and the sum of all the entries is a prime number, is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **282**

**Detailed Solution:**

<blockquote><p>Let the matrix be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>d</mi></mtd><mtd><mi>e</mi></mtd><mtd><mi>f</mi></mtd></mtr><mtr><mtd><mi>g</mi></mtd><mtd><mi>h</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced></math></p><p>Since the elements can be either of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mn>1</mn></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>e</mi><mo>+</mo><mi>f</mi><mo>+</mo><mi>g</mi><mo>+</mo><mi>h</mi><mo>+</mo><mi>i</mi><mo>=</mo><mn>2</mn><mo>/</mo><mn>3</mn><mo>/</mo><mn>5</mn><mo>/</mo><mn>7</mn></math></p><p>For sum as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, the number of cases will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mn>7</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>36</mn></math></p><p>For sum as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>, the number of cases will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>6</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>84</mn></math></p><p>For sum as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>, the number of cases will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>5</mn><mo>!</mo><mn>4</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>126</mn></math></p><p>For sum as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>, the number of cases will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mn>7</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>36</mn></math></p><p>Total required matrix will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>282</mn></math></p></blockquote>

</details>

---

### Q11. JEE Main 2022 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set containing all <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrices with entries from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>. The total number of matrices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8712;</mo><mi>S</mi></math> such that the sum of all the diagonal elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mi>T</mi></msup><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5376**

**Detailed Solution:**

<blockquote><p>Given that the sum of all the diagonal elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mi>T</mi></msup><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>, means sum of all diagonal elements is equal to sum of square each element of the matrix.</p><p>i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mi>T</mi></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math></p><p>Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mi>r</mi></msub><mfenced><mrow><mi>A</mi><mo>&#183;</mo><msup><mi>A</mi><mi>T</mi></msup></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mi>a</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>a</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>a</mi><mn>3</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>b</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>b</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>b</mi><mn>3</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>c</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>c</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>c</mi><mn>3</mn><mn>2</mn></msubsup></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>i</mi></msub><mo>,</mo><msub><mi>b</mi><mi>i</mi></msub><mo>,</mo><msub><mi>c</mi><mi>i</mi></msub><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></math></p><p>Now sum to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> exactly three of them should be zero and rest should be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>.</p><p>So, total number of possible matrices <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><mo>&#215;</mo><msup><mn>2</mn><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>7</mn></mrow><mn>6</mn></mfrac><mo>&#215;</mo><mn>64</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5376</mn></math></p></blockquote>

</details>

---

### Q12. JEE Main 2022 (26 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

The number of matrices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi mathvariant="normal">d</mi><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mn>10</mn></mrow></mfenced></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **50**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>A</mi><mo>&#183;</mo><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>c</mi></mtd><mtd><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>d</mi></mtd></mtr><mtr><mtd><mi>a</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>d</mi></mtd><mtd><mi>b</mi><mi>c</mi><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>On comparing both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>d</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>d</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mi>c</mi><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>4</mn></mfenced></math></p><p>Now equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>-</mo><mfenced><mn>4</mn></mfenced></math> gives</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>d</mi><mo>=</mo><mn>0</mn></math></p><p>Case-I</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>d</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Assuming case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>a</mi></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Now from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>12</mn></math> possibilities</p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>12</mn></math> possibilities</p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> is repeated</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>2</mn><mo>&#215;</mo><mn>12</mn><mo>=</mo><mn>24</mn></math></p><p>So, total case will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mo>-</mo><mn>1</mn></math> (repeated) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>23</mn></math> pairs.</p><p>case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>b</mi></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8658;</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#8594;</mo><mn>23</mn></math> pairs</p><p>case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>c</mi></mfenced><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#8658;</mo><mo>&#160;</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mn>2</mn></math> pairs</p><p>Case-II</p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>d</mi></math></p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8800;</mo><mn>0</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn><mo>=</mo><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mn>2</mn></math> pairs</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>  Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>23</mn><mo>+</mo><mn>23</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>50</mn></math> pairs.</p></blockquote>

</details>

---

### Q13. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The probability that a randomly chosen <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn></math> matrix with all the entries from the set of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> primes, is singular, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>133</mn><msup><mn>10</mn><mn>4</mn></msup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><msup><mn>10</mn><mn>3</mn></msup></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>18</mn><msup><mn>10</mn><mn>3</mn></msup></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>271</mn><msup><mn>10</mn><mn>4</mn></msup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><msup><mn>10</mn><mn>3</mn></msup></mfrac></math>**

**Detailed Solution:**

Let $\mathrm{A}=\left[\begin{array}{ll}\mathrm{a} & \mathrm{b} \\ \mathrm{c} & \mathrm{d}\end{array}\right]$ where $\mathrm{a}, \mathrm{b}, \mathrm{c}, \mathrm{d}$ are prime.
Total number of matrices A formed $=10^4$
Let $\mathrm{S}$ be a matrix from set of matrices $\mathrm{A}$ such that $\mathrm{S}$ is singular.
For singular matrix $|\mathrm{S}|=\mathrm{ad}-\mathrm{bc}=0 \Rightarrow \mathrm{ad}=\mathrm{bc}$
Number of singular matrices $=$ All entries are same $+$ only two prime number are used in matrix
then number of matrices with two prime numbers $=(10 \times 9) \times 2 !=180$
then number of matrices with one prime number $=10 \times 1=10$
So required probability $=\frac{10 \times 9 \times 2 !+10}{10^4}=\frac{19}{1000}=0.019$

</details>

---

### Q14. JEE Main 2022 (27 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a matrix of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn></math>, whose entries are from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math>. If the sum of all the entries of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is a prime number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>,</mo><mn>2</mn><mo>&#60;</mo><mi>p</mi><mo>&#60;</mo><mn>8</mn></math>, then the number of such matrices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **180**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="&#8971;" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>=</mo><mi>p</mi><mo>,</mo><mi>p</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math></p><p>Case-i</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>=</mo><mn>3</mn></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>Entries will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>20</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Case-ii</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>=</mo><mn>5</mn></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math></p><p>Entries will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>56</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Case-iii</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>=</mo><mn>7</mn></math></p><p>Number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> total number of ways when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">a</mi><mo>,</mo><mi mathvariant="normal">b</mi><mo>,</mo><mi mathvariant="normal">c</mi><mo>,</mo><mi mathvariant="normal">d</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math>-total number of ways when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#8713;</mo><mfenced close="}" open="{"><mrow><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math></p><p>Number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mrow><mn>7</mn><mo>+</mo><mn>4</mn><mo>-</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mrow><mn>4</mn><mo>-</mo><mn>1</mn></mrow></msub><mo>-</mo><mfenced><mrow><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>-</mo><mn>16</mn><mo>=</mo><mn>104</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>3</mn></mfenced></math></p><p>Hence adding all equation so total number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>180</mn></math></p>

</details>

---

### Q15. JEE Main 2022 (25 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix having entries from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>. The number of all such matrices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> having sum of all the entries equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>, is _____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **414**

**Detailed Solution:**

<p>Given Matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mo>&#8722;</mo></mtd><mtd><mo>&#8722;</mo></mtd><mtd><mo>&#8722;</mo></mtd></mtr><mtr><mtd><mo>&#8722;</mo></mtd><mtd><mo>&#8722;</mo></mtd><mtd><mo>&#8722;</mo></mtd></mtr><mtr><mtd><mo>&#8722;</mo></mtd><mtd><mo>&#8722;</mo></mtd><mtd><mo>&#8722;</mo></mtd></mtr></mtable></mfenced></math></p><p>Here we can see we have to find nine elements whose sum is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></p><p><strong>Case 1</strong>: When five 1&#39;s are there &amp; four O&#39;s are there </p><p>Now by division &amp; distribution Method</p><p>We get <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>5</mn><mo>!</mo><mn>4</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>126</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><strong>Case 2: </strong>when six 1&#39;s are there &amp; one <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math> &amp; two O&#39;s are there.</p><p>Again by division &amp; distribution Method</p><p>we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>6</mn><mo>!</mo><mn>2</mn><mo>!</mo><mn>1</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>252</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p><strong>Case 3:</strong> When seven 1&#39;s are there are two <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math> are there,</p><p>By division &amp; distribution we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>7</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>36</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>iii</mi></mfenced></math></p><p>Now adding equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>+</mo><mfenced><mi>ii</mi></mfenced><mo>+</mo><mfenced><mi>iii</mi></mfenced></math></p><p>We get <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>126</mn><mo>+</mo><mn>252</mn><mo>+</mo><mn>36</mn><mo>=</mo><mn>414</mn></math></p><p>So total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>414</mn></math> ways will be there. </p>

</details>

---

### Q16. JEE Main 2021 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>:</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#8712;</mo><mfenced><mrow><mo>&#177;</mo><mn>3</mn><mo>,</mo><mo>&#177;</mo><mn>2</mn><mo>,</mo><mo>&#177;</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></mrow></mfenced></math>. Define <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>M</mi><mo>&#8594;</mo><mi>Z</mi><mo>,</mo></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mo>det</mo><mfenced><mi>A</mi></mfenced><mo>,</mo></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8712;</mo><mi>M</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi></math> is set of all integers. Then the number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8712;</mo><mi>M</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mn>15</mn></math> is equal to <u>                </u>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<p>.<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>15</mn></math></p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mo>&#177;</mo><mn>3</mn><mo>,</mo><mo>&#177;</mo><mn>2</mn><mo>,</mo><mo>&#177;</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>:</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>=</mo><mn>9</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>b</mi><mi>c</mi><mo>=</mo><mo>-</mo><mn>6</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi></math> possible pairs are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced><mo>.</mo></math> </p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mi>c</mi></math> possible pairs are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math> </p><p>So, total number of matrices in case <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>8</mn></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi><mo>:</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>b</mi><mi>c</mi><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p>Similarly, total number of matrices in case <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>8</mn></math></p><p>Hence, total number of matrices are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>.</p>

</details>

---

### Q17. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced></math> be a real matrix of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>,</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>i</mi><mn>1</mn></mrow></msub><mo>+</mo><msub><mi>a</mi><mrow><mi>i</mi><mn>2</mn></mrow></msub><mo>+</mo><msub><mi>a</mi><mrow><mi>i</mi><mn>3</mn></mrow></msub><mo>=</mo><mn>1</mn><mo>,</mo></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>&#160;</mo><mo>.</mo></math> Then, the sum of all the entries of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>11</mn></msub></mtd><mtd><msub><mi>a</mi><mn>12</mn></msub></mtd><mtd><msub><mi>a</mi><mn>13</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>21</mn></msub></mtd><mtd><msub><mi>a</mi><mn>22</mn></msub></mtd><mtd><msub><mi>a</mi><mn>23</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>31</mn></msub></mtd><mtd><msub><mi>a</mi><mn>32</mn></msub></mtd><mtd><msub><mi>a</mi><mn>33</mn></msub></mtd></mtr></mtable></mfenced></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Then, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>X</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>11</mn></msub></mtd><mtd><msub><mi>a</mi><mn>12</mn></msub></mtd><mtd><msub><mi>a</mi><mn>13</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>21</mn></msub></mtd><mtd><msub><mi>a</mi><mn>22</mn></msub></mtd><mtd><msub><mi>a</mi><mn>23</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>31</mn></msub></mtd><mtd><msub><mi>a</mi><mn>32</mn></msub></mtd><mtd><msub><mi>a</mi><mn>33</mn></msub></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>11</mn></msub><mo>+</mo><msub><mi>a</mi><mn>12</mn></msub><mo>+</mo><msub><mi>a</mi><mn>13</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>21</mn></msub><mo>+</mo><msub><mi>a</mi><mn>22</mn></msub><mo>+</mo><msub><mi>a</mi><mn>23</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>31</mn></msub><mo>+</mo><msub><mi>a</mi><mn>32</mn></msub><mo>+</mo><msub><mi>a</mi><mn>33</mn></msub></mtd></mtr></mtable></mfenced></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>i</mi><mn>1</mn></mrow></msub><mo>+</mo><msub><mi>a</mi><mrow><mi>i</mi><mn>2</mn></mrow></msub><mo>+</mo><msub><mi>a</mi><mrow><mi>i</mi><mn>3</mn></mrow></msub><mo>=</mo><mn>1</mn><mo>,</mo></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>11</mn></msub><mo>+</mo><msub><mi>a</mi><mn>12</mn></msub><mo>+</mo><msub><mi>a</mi><mn>13</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>21</mn></msub><mo>+</mo><msub><mi>a</mi><mn>22</mn></msub><mo>+</mo><msub><mi>a</mi><mn>23</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>31</mn></msub><mo>+</mo><msub><mi>a</mi><mn>32</mn></msub><mo>+</mo><msub><mi>a</mi><mn>33</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mi>X</mi><mo>=</mo><mi>X</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Pre multiply by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mi>X</mi><mo>=</mo><mi>A</mi><mi>X</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>,</mo></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mi>X</mi><mo>=</mo><mi>X</mi></math></p><p>Again, pre multiply by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mi>X</mi><mo>=</mo><mi>A</mi><mi>X</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced><mo>,</mo></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mi>X</mi><mo>=</mo><mi>X</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>x</mi><mn>1</mn></msub></mtd><mtd><msub><mi>x</mi><mn>2</mn></msub></mtd><mtd><msub><mi>x</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>y</mi><mn>1</mn></msub></mtd><mtd><msub><mi>y</mi><mn>2</mn></msub></mtd><mtd><msub><mi>y</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>z</mi><mn>1</mn></msub></mtd><mtd><msub><mi>z</mi><mn>2</mn></msub></mtd><mtd><msub><mi>z</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>2</mn></msub><mo>+</mo><msub><mi>y</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub><mo>+</mo><msub><mi>z</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>2</mn></msub><mo>+</mo><msub><mi>y</mi><mn>3</mn></msub><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub><mo>+</mo><msub><mi>z</mi><mn>3</mn></msub><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>2</mn></msub><mo>+</mo><msub><mi>y</mi><mn>3</mn></msub><mo>+</mo><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub><mo>+</mo><msub><mi>z</mi><mn>3</mn></msub><mo>=</mo><mn>3</mn><mo>.</mo></math></p><p>Thus, the sum of all the elements is<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>.</mo></math></p>

</details>

---

### Q18. JEE Main 2021 (16 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

The total number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> having enteries from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> such that the sum of all the diagonal entries of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>A</mi><mi>T</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>, is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **766**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>d</mi></mtd><mtd><mi>e</mi></mtd><mtd><mi>f</mi></mtd></mtr><mtr><mtd><mi>g</mi></mtd><mtd><mi>h</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><msup><mi>A</mi><mi>T</mi></msup><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>d</mi></mtd><mtd><mi>g</mi></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mi>e</mi></mtd><mtd><mi>h</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>f</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced></math></p><p>Diagonal elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>A</mi><mi>T</mi></msup><mo>&#160;</mo><mtext>is</mtext><mo>&#160;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>,</mo><msup><mrow><mo>&#160;</mo><mi>d</mi></mrow><mn>2</mn></msup><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><msup><mi>f</mi><mn>2</mn></msup><mo>,</mo><msup><mrow><mo>&#160;</mo><mi>g</mi></mrow><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>.</mo><mo>&#160;</mo></math></p><p>Sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><msup><mi>f</mi><mn>2</mn></msup><mo>+</mo><msup><mi>g</mi><mn>2</mn></msup><mo>+</mo><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>i</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>,</mo><mi>e</mi><mo>,</mo><mi>f</mi><mo>,</mo><mi>g</mi><mo>,</mo><mi>h</mi><mo>,</mo><mi>i</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td>Case</td>			<td>No. of Matrices</td>		</tr>		<tr>			<td>(1)</td>			<td>All &ndash; <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mo>'</mo></msup><mi mathvariant="normal">s</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>9</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>1</mn></math></td>		</tr>		<tr>			<td>(2)</td>			<td>One <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><msup><mn>3</mn><mo>'</mo></msup><mi mathvariant="normal">s</mi></math>, remaining-<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>0</mn><mo>'</mo></msup><mi mathvariant="normal">s</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>1</mn><mo>!</mo><mo>&#215;</mo><mn>8</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>9</mn></math></td>		</tr>		<tr>			<td>(3)</td>			<td>			<p>One-<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mo>'</mo></msup><mi mathvariant="normal">s</mi></math></p>			<p>Five-<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mo>'</mo></msup><mi mathvariant="normal">s</mi></math></p>			<p>Three-<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>0</mn><mo>'</mo></msup><mi mathvariant="normal">s</mi></math></p>			</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>1</mn><mo>!</mo><mo>&#215;</mo><mn>5</mn><mo>!</mo><mo>&#215;</mo><mn>3</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>8</mn><mo>&#215;</mo><mn>63</mn></math></td>		</tr>		<tr>			<td>(4)</td>			<td>Two -<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#39;</mo><mi mathvariant="normal">s</mi></math>
			One-<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mo>'</mo></msup><mi mathvariant="normal">s</mi></math>
			Six-<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#39;</mo><mi mathvariant="normal">s</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mo>&#215;</mo><mn>6</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>63</mn><mo>&#215;</mo><mn>4</mn></math></td>		</tr>	</tbody></table><p>Then, the total no. of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>8</mn><mo>&#215;</mo><mn>63</mn><mo>+</mo><mn>63</mn><mo>&#215;</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>766</mn></math></p>

</details>

---

### Q19. JEE Main 2021 (24 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> be any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix with entries from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>. The maximum number of such matrices, for which the sum of diagonal elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>M</mi><mi>T</mi></msup><mi>M</mi></math> is seven, is______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **540**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>d</mi></mtd><mtd><mi>e</mi></mtd><mtd><mi>f</mi></mtd></mtr><mtr><mtd><mi>g</mi></mtd><mtd><mi>h</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>d</mi></mtd><mtd><mi>g</mi></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mi>e</mi></mtd><mtd><mi>h</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>f</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><msup><mi>f</mi><mn>2</mn></msup><mo>+</mo><msup><mi>g</mi><mn>2</mn></msup><mo>+</mo><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>i</mi><mn>2</mn></msup><mo>=</mo><mn>7</mn></math></p><p>Case-I : Seven <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>&#39;</mo><mi>s</mi></mrow></mfenced></math> and two <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>&#39;</mo><mi>s</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><mo>=</mo><mn>36</mn></math></p><p>Case-II: One <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> and three <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>&#39;</mo><mi>s</mi></mrow></mfenced></math> and five <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>&#39;</mo><mi>s</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>5</mn><mo>!</mo><mn>3</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>504</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>540</mn></math></p>

</details>

---

### Q20. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn></math> real matrix with entries from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>&#8800;</mo><mn>0</mn></math>. Consider the following two statements;</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>P</mi></mfenced></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8800;</mo><msub><mi>l</mi><mn>2</mn></msub></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>Q</mi></mfenced></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mi>r</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mn>2</mn></math></p><p>Where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub></math> denotes <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn></math> identity matrix and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mi>r</mi><mfenced><mi>A</mi></mfenced></math> denotes the sum of the diagonal entries of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. Then</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>P</mi></mfenced></math> is false and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>Q</mi></mfenced></math> is true
- **(B)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>P</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>Q</mi></mfenced></math> are false
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>P</mi></mfenced></math> is true and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>Q</mi></mfenced></math> is false
- **(D)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>P</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>Q</mi></mfenced></math> are true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>P</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>Q</mi></mfenced></math> are true**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>&#160;&#160;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#8712;</mo><mo>{</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>a</mi><mi>d</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>0</mn></math>  or  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>P</mi></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8800;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>&#8800;</mo><mn>1</mn><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mo>|</mo><mi>A</mi><mo>|</mo><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>P</mi></mfenced></math> is true.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>Q</mi></mfenced></math> </p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>a</mi><mi>d</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mo>&#160;</mo><mo mathvariant="italic">tr</mo><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>Q</mi></mfenced></math> is true.</p>

</details>

---

### Q21. JEE Main 2020 (08 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

The number of all <math><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrices <math><mi>A</mi><mo>,</mo></math> with entries from the set <math><mfenced close="}" open="{" separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mi></mi><mn>0</mn><mo>,</mo><mi></mi><mn>1</mn></mrow></mfenced></math> such that the sum of the diagonal elements of <math><mi>A</mi><msup><mrow><mi>A</mi></mrow><mrow><mi>T</mi></mrow></msup></math> is <math><mn>3</mn><mo>,</mo></math> is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **672**

**Detailed Solution:**

Let, <math><mi>A</mi><mo>=</mo><msub><mrow><mfenced close="]" open="[" separators="|"><mrow><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi><mi>i</mi></mrow></msub></mrow></mfenced></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>3</mn></mrow></msub></math>
<math><mi>t</mi><mi>r</mi><mo>(</mo><mi>A</mi><msup><mrow><mi>A</mi></mrow><mrow><mi>T</mi></mrow></msup><mo>)</mo><mo>=</mo><mn>3</mn></math>
<math><msubsup><mrow><mi>a</mi></mrow><mrow><mn>11</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>a</mi></mrow><mrow><mn>12</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mi mathvariant="normal"></mi><mo>+</mo><msubsup><mrow><mi>a</mi></mrow><mrow><mn>13</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>a</mi></mrow><mrow><mn>21</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msubsup><mrow><mi>a</mi></mrow><mrow><mn>33</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mn>3</mn></math>
Possible cases
<math><mfenced close="}" open="" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn><mo>,</mo><mn>0,0</mn><mo>,</mo><mn>0,0</mn><mo>,</mo><mn>0,1</mn><mo>,</mo><mn>1,1</mn></mtd><mtd><mo>&#8594;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo><mn>0,0</mn><mo>,</mo><mn>0,0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mtd><mtd><mo>&#8594;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo><mn>0,0</mn><mo>,</mo><mn>0,0</mn><mo>,</mo><mn>0,1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mtd><mtd><mo>&#8594;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo><mn>0,0</mn><mo>,</mo><mn>0,0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mo>-</mo><mn>1,1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mtd><mtd><mo>&#8594;</mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><msup><mrow><mo>&#8201;</mo></mrow><mrow><mn>9</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>6</mn></mrow></msub><mo>&#215;</mo><mn>8</mn><mo>=</mo><mn>84</mn><mo>&#215;</mo><mn>8</mn><mo>=</mo><mn>672</mn></math>

</details>

---

### Q22. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A common tangent to the conics $x^2=6 y$ and $2 x^2-4 y^2=9$ is:

**Options:**

- **(A)** $x-y=\frac{3}{2}$
- **(B)** $x+y=1$
- **(C)** $x+y=\frac{9}{2}$
- **(D)** $x-y=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x-y=\frac{3}{2}$**

**Detailed Solution:**

$$
\begin{aligned}
&x^2-6 y \\
&2 x^2-4 y^2=9
\end{aligned}
$$
Consider the line,
$$
x-y=\frac{3}{2}
$$
On solving (i) and (iii), we get only
$$
x=3, y=\frac{3}{2}
$$
Hence $\left(3, \frac{3}{2}\right)$ is the point of contact of conic (i), and line (iii)
On solving (ii) and (iii), we get only $x=3$,
$$
y=\frac{3}{2}
$$
Hence $\left(3, \frac{3}{2}\right)$ is also the point of contact of conic (ii) and line (iii).
Hence line (iii) is the common tangent to both the given conics.

</details>

---

### Q23. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `2`

The number of $3 \times 3$ non-singular matrices, with four entries as 1 and all other entries as 0 , is

**Options:**

- **(A)** 5
- **(B)** 6
- **(C)** at least 7
- **(D)** less than 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) at least 7**

**Detailed Solution:**

First row with exactly one zero; total number of cases $=6$ 
First row 2 zeros we get more cases 
Total we get more than 7 .

</details>

---

### Q24. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

If $A$ and $B$ are square matrices of size $n \times n$ such that $A^2-B^2=(A-B)(A+B)$, then which of the following will be always true?

**Options:**

- **(A)** A = B
- **(B)** AB = BA
- **(C)** either of A or B is a zero matrix
- **(D)** either of A or B is an identity matrix

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) AB = BA**

**Detailed Solution:**

$A^2-B^2=(A-B)(A+B)$
$A^2-B^2=A^2+A B-B A-B^2$
$\Rightarrow A B=B A$

</details>

---

### Q25. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\left(\begin{array}{ccc}0 & 0 & -1 \\ 0 & -1 & 0 \\ -1 & 0 & 0\end{array}\right)$
The only correct statement about the matrix $A$ is

**Options:**

- **(A)** $A$ is a zero matrix
- **(B)** $A^2=I$
- **(C)** $\mathrm{A}^{-1}$ does not exist
- **(D)** $A=(-1) I$, where $I$ is a unit matrix

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $A^2=I$**

**Detailed Solution:**

$A . A=\left[\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]=I$

</details>

---

