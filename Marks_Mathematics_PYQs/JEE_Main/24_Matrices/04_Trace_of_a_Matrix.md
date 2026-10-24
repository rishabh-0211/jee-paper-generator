# JEE Main Mathematics - Matrices

## Topic 4: Trace of a Matrix

**Total Questions:** 6

---

### Q1. JEE Main 2024 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $A=\left[\begin{array}{cc}2 & -1 \\ 1 & 1\end{array}\right]$. If the sum of the diagonal elements of $A^{13}$ is $3^n$, then $n$ is equal to_________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

$A=\left[\begin{array}{cc}2 & -1 \\ 1 & 1\end{array}\right]$
$\begin{aligned} & A^2=\left[\begin{array}{cc}2 & -1 \\ 1 & 1\end{array}\right]\left[\begin{array}{cc}2 & -1 \\ 1 & 1\end{array}\right]=\left[\begin{array}{cc}3 & -3 \\ 3 & 0\end{array}\right] \\ & A^3=\left[\begin{array}{cc}3 & -3 \\ 3 & 0\end{array}\right]\left[\begin{array}{cc}2 & -1 \\ 1 & 1\end{array}\right]=\left[\begin{array}{cc}3 & -6 \\ 6 & -3\end{array}\right] \\ & A^4=\left[\begin{array}{cc}3 & -6 \\ 6 & -3\end{array}\right]\left[\begin{array}{cc}2 & -1 \\ 1 & 1\end{array}\right]=\left[\begin{array}{cc}0 & -9 \\ 9 & -9\end{array}\right] \\ & A^5=\left[\begin{array}{cc}0 & -9 \\ 9 & -9\end{array}\right]\left[\begin{array}{cc}2 & -1 \\ 1 & 1\end{array}\right]=\left[\begin{array}{cc}-9 & -9 \\ 9 & -18\end{array}\right] \\ & A^6=\left[\begin{array}{cc}-9 & -9 \\ 9 & -18\end{array}\right]\left[\begin{array}{cc}2 & -1 \\ 1 & 1\end{array}\right]=\left[\begin{array}{cc}-27 & 0 \\ 0 & -27\end{array}\right] \\ & A^7=\left[\begin{array}{cc}-27 & -0 \\ 0 & -27\end{array}\right]\left[\begin{array}{cc}-54 & 27 \\ -27 & -27\end{array}\right]=\left[\begin{array}{cc}3^6 \times 2 & -27^2 \\ 27^2 & 3^6\end{array}\right] \\ & 3^7=3^n \Rightarrow n=7\end{aligned}$

</details>

---

### Q2. JEE Main 2024 (27 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>×</mo><mn>2</mn></math> real matrix and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> be the identity matrix of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo></math> If the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi mathvariant="normal">A</mi><mo>-</mo><mi>xI</mi><mo>|</mo><mo>=</mo><mn>0</mn></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo></math> then the sum of the diagonal elements of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>2</mn></msup></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi mathvariant="normal">A</mi><mo>-</mo><mi>xI</mi><mo>|</mo><mo>=</mo><mn>0</mn></math> have roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>.</p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi mathvariant="normal">a</mi></mtd><mtd><mi mathvariant="normal">b</mi></mtd></mtr><mtr><mtd><mi mathvariant="normal">c</mi></mtd><mtd><mi mathvariant="normal">d</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">A</mi><mo>-</mo><mi>xI</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi mathvariant="normal">a</mi></mtd><mtd><mi mathvariant="normal">b</mi></mtd></mtr><mtr><mtd><mi mathvariant="normal">c</mi></mtd><mtd><mi mathvariant="normal">d</mi></mtd></mtr></mtable></mfenced><mo>-</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi mathvariant="normal">x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi mathvariant="normal">x</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">A</mi><mo>-</mo><mi>xI</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi mathvariant="normal">a</mi><mo>-</mo><mi mathvariant="normal">x</mi></mtd><mtd><mi mathvariant="normal">b</mi></mtd></mtr><mtr><mtd><mi mathvariant="normal">c</mi></mtd><mtd><mi mathvariant="normal">d</mi><mo>-</mo><mi mathvariant="normal">x</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><mi mathvariant="normal">A</mi><mo>-</mo><mi>xI</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mi mathvariant="normal">a</mi><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mfenced><mrow><mi mathvariant="normal">d</mi><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mo>-</mo><mi>bc</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><mi mathvariant="normal">A</mi><mo>-</mo><mi>xI</mi></mrow></mfenced><mo>=</mo><mi>ad</mi><mo>-</mo><mi>ax</mi><mo>-</mo><mi>dx</mi><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mi>bc</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><mi mathvariant="normal">A</mi><mo>-</mo><mi>xI</mi></mrow></mfenced><mo>=</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mi mathvariant="normal">a</mi><mo>+</mo><mi mathvariant="normal">d</mi></mrow></mfenced><mi mathvariant="normal">x</mi><mo>+</mo><mfenced><mrow><mi>ad</mi><mo>-</mo><mi>bc</mi></mrow></mfenced></math></p><p>Sum of roots, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">a</mi><mo>+</mo><mi mathvariant="normal">d</mi><mo>=</mo><mn>2</mn></math></p><p>Product of roots, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ad</mi><mo>-</mo><mi>bc</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>Now finding matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>2</mn></msup></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi mathvariant="normal">a</mi></mtd><mtd><mi mathvariant="normal">b</mi></mtd></mtr><mtr><mtd><mi mathvariant="normal">c</mi></mtd><mtd><mi mathvariant="normal">d</mi></mtd></mtr></mtable></mfenced><mo>×</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi mathvariant="normal">a</mi></mtd><mtd><mi mathvariant="normal">b</mi></mtd></mtr><mtr><mtd><mi mathvariant="normal">c</mi></mtd><mtd><mi mathvariant="normal">d</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>+</mo><mi>bc</mi></mtd><mtd><mi>ab</mi><mo>+</mo><mi>bd</mi></mtd></mtr><mtr><mtd><mi>ac</mi><mo>+</mo><mi>cd</mi></mtd><mtd><mi>bc</mi><mo>+</mo><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math></p><p>Sum of diagonal elements, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>=</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>+</mo><mi>bc</mi><mo>+</mo><mi>bc</mi><mo>+</mo><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">S</mi><mo>=</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>bc</mi><mo>+</mo><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">S</mi><mo>=</mo><mo>(</mo><mi mathvariant="normal">a</mi><mo>+</mo><mi mathvariant="normal">d</mi><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mrow><mi>ad</mi><mo>-</mo><mi>bc</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">S</mi><mo>=</mo><mo>(</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">S</mi><mo>=</mo><mn>4</mn><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">S</mi><mo>=</mo><mn>10</mn></math></p>

</details>

---

### Q3. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{A}$, other than $\mathrm{I}$ or $-\mathrm{I}$, be a $2 \times 2$ real matrix such that $\mathrm{A}^2=\mathrm{I}$, I being the unit matrix. Let $\operatorname{Tr}(\mathrm{A})$ be the sum of diagonal elements of A.
Statement-1: $\operatorname{Tr}(\mathrm{A})=0$
Statement-2: $\operatorname{det}(\mathrm{A})=-1$

**Options:**

- **(A)** Statement-1 is true; Statement- 2 is false.
- **(B)** Statement-1 is true; Statement-2 is true; Statement-2 is not a correct explanation for Statement-1.
- **(C)** Statement-1 is true; Statement-2 is true; Statement-2 is a correct explanation for Statement-1.
- **(D)** Statement-1 is false; Statement- 2 is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement-1 is true; Statement-2 is true; Statement-2 is not a correct explanation for Statement-1.**

**Detailed Solution:**

$\left[\begin{array}{ll}a & b \\ c & d\end{array}\right]\left[\begin{array}{ll}a & b \\ c & d\end{array}\right]=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$
$$
\begin{aligned}
& {\left[\begin{array}{ll}
a^2+b c & a b+b d \\
a c+c d & b c+d^2
\end{array}\right]=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]} \\
& b(a+d)=0, b=0 \text { or } a=-d \\
& c(a+d)=0, c=0 \text { or } a=-d \\
& a^2+b c=1, b c+d^2=1
\end{aligned}
$$
' $a$ ' and ' $d$ ' are diagonal elements $a+d=0$ statement- 1 is correct.
Now, $\operatorname{det}(A)=a d-b c$
Now, from (3) $a^2+b c=1$ and $d^2+b c=1$
So, $a^2-d^2=0$
Adding $a^2+d^2+2 b c=2$
$$
=(a+d)^2-2 a d+2 b c=2
$$
or $0-2(a d-b c)=2$
So, $a d-b c=1 \Rightarrow \operatorname{det}(A)=-1$
So, statement $-2$ is also true.
But statement $-2$ is not the correct explanation of statement-I

</details>

---

### Q4. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If $A^T$ denotes the transpose of the matrix $A=\left[\begin{array}{lll}0 & 0 & a \\ 0 & b & c \\ d & e & f\end{array}\right]$, where $a, b, c, d, e$ and $f$ are integers such that $a b d \neq 0$, then the number of such matrices for which $A^{-1}=A^T$ is

**Options:**

- **(A)** 2(3!)
- **(B)** $3(2 !)$
- **(C)** $2^3$
- **(D)** $3^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2^3$**

**Detailed Solution:**

$$
\begin{aligned} 
& \text { } A=\left[\begin{array}{lll}
0 & 0 & a \\
0 & b & c \\
d & e & f
\end{array}\right],|A|=-a b d \neq 0 \\
& c_{11}=+(b f-c e), c_{12}=-(-c \mathrm{~d})=c d, \\
& c_{21}=-(-c a)=a e, c_{22}=+(-a d)=-a d, \\
& c_{31}=+(-a b)=-a b, c_{32} \quad c_{23}=-(0)=0 \\
& \operatorname{Adj} A=\left[\begin{array}{ccc}
(b f-c e) & a e & -a b \\
c d & -a d & 0 \\
-b d & 0 & 0
\end{array}\right]
\end{aligned}
$$
$A^{-1}=\frac{1}{|A|}(\operatorname{adj} A)=\frac{1}{a b d}\left[\begin{array}{ccc}b f-c e & a e & -a b \\ c d & -a d & 0 \\ -b d & 0 & 0\end{array}\right]$

$$
\begin{aligned}
& A^T=\left[\begin{array}{lll}
0 & 0 & d \\
0 & b & e \\
a & c & f
\end{array}\right] \\
& \text { Now } A^{-1}=A^T \\
& \Rightarrow \frac{1}{-a b d}\left[\begin{array}{ccc}
b f-c e & a e & -a b \\
c d & -a d & 0 \\
-b d & 0 & 0
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{cccc}
b f-c e & a e & -a b \\
c d & -a d & 0 \\
-b d & 0 & 0
\end{array}\right] \\
& \therefore b f-c e=\left[\begin{array}{ccc}
0 & 0 & d \\
0 & b & e \\
a & c & f
\end{array}\right]
\end{aligned}
$$
$a b d^2=a b, a b^2 d=a d, a^2 b d=b d \quad$...(ii)
abde $=a b c d=a b d f=0$
From (ii),
$\left(a b d^2\right) \cdot\left(a b^2 d\right) \cdot\left(a^2 b d\right)=a b . a d . b d$
$\Rightarrow(a b d)^4-(a b d)^2=0$
$\Rightarrow(a b d)^2\left[(a b d)^2-1\right]=0$
$\because a b d \neq 0, \therefore a b d=\pm 1$
From (iii) and (iv),
$$
e=c=f=0
$$
From (i) and (v),
$$
b f=a e=c d=0
$$
From (iv), (v) and (vi), it is clear that $a, b$, $d$ can be any non-zero integer such that $a b d=\pm 1$
But it is only possible, if $a=b=d=\pm 1$ Hence, there are 2 choices for each $a, b$ and $d$. there fore, there are $2 \times 2 \times 2$ choices for $a, b$ and $d$. Hence number of required matrices $=2 \times 2 \times 2=(2)^3$

</details>

---

### Q5. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `2`

Let $A$ be a $2 \times 2$ matrix with non-zero entries and let $A^2=1$, where 1 is $2 \times 2$ identity matrix. Define $\operatorname{Tr}(\mathrm{A})=$ sum of diagonal elements of $A$ and $|A|=$ determinant of matrix $A$.
Statement-1: $\operatorname{Tr}(\mathrm{A})=0$
Statement-2: $|\mathrm{A}|=1$

**Options:**

- **(A)** Statement-1 is true, Statement-2 is true; Statement-2 is not the correct explanation for Statement-1
- **(B)** Statement-1 is true, Statement-2 is false
- **(C)** Statement-1 is false, Statement-2 is true
- **(D)** Statement-1 is true, Statement-2 is true; Statement-2 is the correct explanation for Statement-1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement-1 is true, Statement-2 is false**

**Detailed Solution:**

Let $A=\left(\begin{array}{ll}a & b \\ c & d\end{array}\right), a b c d \neq 0$
$$
\begin{aligned}
& A^2=\left(\begin{array}{ll}
a & b \\
c & d
\end{array}\right) \cdot\left(\begin{array}{ll}
a & b \\
c & d
\end{array}\right) \\
& \Rightarrow A^2=\left(\begin{array}{ll}
a^2+b c & a b+b d \\
a c+c d & b c+d^2
\end{array}\right) \\
& \Rightarrow a^2+b c=1, b c+d^2=1 \\
& a b+b d=a c+c d=0 \\
& c \neq 0 \text { and } b \neq 0 \\
& \text { Trace } A=a+d=0 \\
& |A|=a d-b c=-a^2-b c=-1 .
\end{aligned}
$$

</details>

---

### Q6. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{A}$ be a $2 \times 2$ matrix with real entries. Let I be the $2 \times 2$ identity matrix. Denote by $\operatorname{tr}(\mathrm{A})$, the sum of diagonal entries of $A$. Assume that $A^2=1$.
Statement -1: If $A \neq 1$ and $A \neq-1$, then $\operatorname{det} A=-1$.
Statement $-2$ : If $A \neq 1$ and $A \neq-1$, then $\operatorname{tr}(A) \neq 0$.

**Options:**

- **(A)** Statement $-1$ is false, Statement $-2$ is true
- **(B)** Statement $-1$ is true, Statement $-2$ is true, Statement $-2$ is a correct explanation for Statement $-1$
- **(C)** Statement $-1$ is true, Statement $-2$ is true; Statement $-2$ is not a correct explanation for Statement $-1$
- **(D)** Statement $-1$ is true, Statement $-2$ is false.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement $-1$ is true, Statement $-2$ is false.**

**Detailed Solution:**

Let $A=\left[\begin{array}{ll}a & b \\ c & d\end{array}\right]$ so that $A^2=\left[\begin{array}{ll}a^2+b c & a b+b d \\ a c+d c & b c+d^2\end{array}\right]=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$
$\Rightarrow a^2+b c=1=b c+d^2$ and $(a+d) c=0=(a+d) b$.
Since $A \neq I, A \neq 1, a=-d$ and hence $\operatorname{det} A=\left|\begin{array}{cc}\sqrt{1-b c} & b \\ c & -\sqrt{1-b c}\end{array}\right|=-1+b c-b c=-1$
Statement 1 is true.
But tr. $A=0$ and hence statement 2 is false.

</details>

---

