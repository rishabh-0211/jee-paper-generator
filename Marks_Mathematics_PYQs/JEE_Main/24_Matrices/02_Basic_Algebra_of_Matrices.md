# JEE Main Mathematics - Matrices

## Topic 2: Basic Algebra of Matrices

**Total Questions:** 10

---

### Q1. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha$ be a solution of $x^2+x+1=0$, and for some $a$ and $b$ in
$\mathbb{R},\left[\begin{array}{lll}4 & \mathrm{a} & \mathrm{b}\end{array}\right]\left[\begin{array}{ccc}1 & 16 & 13 \\ -1 & -1 & 2 \\ -2 & -14 & -8\end{array}\right]=\left[\begin{array}{ccc}0 & 0 & 0\end{array}\right]$. If $\frac{4}{\alpha^4}$ $+\frac{\mathrm{m}}{\alpha^{\mathrm{a}}}+\frac{\mathrm{n}}{\alpha^{\mathrm{b}}}=3$, then $\mathrm{m}+\mathrm{n}$ is equal to

**Options:**

- **(A)** 3
- **(B)** 11
- **(C)** 7
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 11**

**Detailed Solution:**

$x^2+x+1=0$
$\alpha$ is root
$\begin{aligned}
& \therefore \alpha^2+\alpha+1=0 \\
& \Rightarrow \alpha=\omega \text { as } \omega^2 \text { [cube root of unity] }
\end{aligned}$
also
$\left.\begin{array}{l}
{\left[\begin{array}{ll}
4-a-2 b & 64-a-14 b
\end{array} 52+2 a-8 b\right.}
\end{array}\right]$
$\begin{aligned} & =\left[\begin{array}{ll}0 & 0&0\end{array}\right] \\ \therefore & a+2 b=4 \\ & a+14 b=64 \\ \Rightarrow & 12 b=60 \Rightarrow b=5 \\ \Rightarrow & a=-6 \\ \therefore & \frac{4}{\alpha^4}+\frac{m}{\alpha^{-6}}+\frac{n}{\alpha^5}=3 \\ \Rightarrow & \frac{4}{\omega}+\frac{m}{1}+\frac{n}{\omega^2}=3 \\ \Rightarrow & 4 \omega^2+m+n \omega=3\end{aligned}$
$\begin{aligned}
& \Rightarrow 4\left(-\frac{1}{2}-\frac{\sqrt{3}}{2} \mathrm{i}\right)+\mathrm{m}+\mathrm{n}\left(-\frac{1}{2}+\frac{\sqrt{3}}{2} \mathrm{i}\right)=3 \\
& \therefore-2+\mathrm{m}-\frac{\mathrm{n}}{2}=3....(1) \\
& \& \frac{-4 \sqrt{3}}{2}+\frac{\mathrm{n} \sqrt{3}}{2}=0 \\
& \therefore \mathrm{n}=4 \\
& \mathrm{~m}=7 \\
& \therefore \mathrm{~m}+\mathrm{n}=11
\end{aligned}$

</details>

---

### Q2. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\left[\begin{array}{cc}\alpha & -1 \\ 6 & \beta\end{array}\right], \alpha \gt 0$, such that $\operatorname{det}(A)=0$ and $\alpha+\beta=1$. If I denotes $2 \times 2$ identity matrix, then the matrix $(1+\mathrm{A})^8$ is:

**Options:**

- **(A)** $\left[\begin{array}{ll}4 & -1 \\ 6 & -1\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}257 & -64 \\ 514 & -127\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}1025 & -511 \\ 2024 & -1024\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}766 & -255 \\ 1530 & -509\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\begin{array}{cc}766 & -255 \\ 1530 & -509\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & |\mathrm{A}|=0 \\ & \alpha \beta+6=0 \\ & \alpha \beta=-6 \\ & \alpha+\beta=1 \\ & \Rightarrow \alpha=3, \beta=-2 \\ & \mathrm{~A}=\left[\begin{array}{ll}3 & -1 \\ 6 & -2\end{array}\right] \\ & \mathrm{A}^2=\left[\begin{array}{ll}3 & -1 \\ 6 & -2\end{array}\right]\left[\begin{array}{ll}3 & -1 \\ 6 & -2\end{array}\right]=\left[\begin{array}{ll}3 & -1 \\ 6 & -2\end{array}\right] \\ & \therefore \mathrm{A}^2=\mathrm{A} \\ & \mathrm{A}=\mathrm{A}^2=\mathrm{A}^3=\mathrm{A}^4=\mathrm{A}^5 \\ & (\mathrm{I}+\mathrm{A})^8 \\ & =\mathrm{I}+{ }^8 \mathrm{C}_1 \mathrm{~A}^7+{ }^8 \mathrm{C}_2 \mathrm{~A}^6+\ldots . .+{ }^8 \mathrm{C}_8 \mathrm{~A}^8 \\ & =\mathrm{I}+\mathrm{A}\left({ }^8 \mathrm{C}_1+{ }^8 \mathrm{C}_2+\ldots . .+{ }^8 \mathrm{C}_8\right) \\ & =\mathrm{I}+\mathrm{A}\left(2^8-1\right) \\ & =\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]+\left[\begin{array}{cc}765 & -255 \\ 1530 & -510\end{array}\right]\end{aligned}$
$=\left[\begin{array}{cc}766 & -255 \\ 1530 & -509\end{array}\right]$

</details>

---

### Q3. JEE Main 2025 (28 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let M denote the set of all real matrices of order $3 \times 3$ and let $\mathrm{S}=\{-3,-2,-1,1,2\}$. Let
$$
\begin{aligned}
& \mathrm{S}_1=\left\{\mathrm{A}=\left[a_{\mathrm{ij}}\right] \in \mathrm{M}: \mathrm{A}=\mathrm{A}^{\mathrm{T}} \text { and } a_{\mathrm{ij}} \in \mathrm{~S}, \forall \mathrm{i}, \mathrm{j}\right\}, \\
& \mathrm{S}_2=\left\{\mathrm{A}=\left[a_{\mathrm{ij}}\right] \in \mathrm{M}: \mathrm{A}=-\mathrm{A}^{\mathrm{T}} \text { and } a_{\mathrm{ij}} \in \mathrm{~S}, \forall \mathrm{i}, \mathrm{j}\right\}, \\
& \mathrm{S}_3=\left\{\mathrm{A}=\left[a_{\mathrm{ij}}\right] \in \mathrm{M}: a_{11}+a_{22}+a_{33}=0 \text { and } a_{\mathrm{ij}} \in \mathrm{~S}, \forall \mathrm{i}, \mathrm{j}\right\} .
\end{aligned}
$$
If $n\left(\mathrm{~S}_1 \cup_2 \mathrm{US}_3\right)=125 \alpha$, then $\alpha$ equals _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1613**

**Detailed Solution:**

$\left[\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right]$

No. of elements in $\mathrm{S}_1: \mathrm{A}=\mathrm{A}^{\mathrm{T}} \Rightarrow 5^3 \times 5^3$
No. of elements in $A=-A^T \Rightarrow 0$
since no. zero in 5
No. of elements in $\mathrm{S}_3 \Rightarrow$
$\left.\begin{array}{c}a_{11}+a_{22}+a_{33}=0 \Rightarrow(1,2,-3) \Rightarrow 31 \\ \text { or } \\ (1,1,-2) \Rightarrow 3 \\ \text { or } \\ (-1,-1,2) \Rightarrow 3\end{array}\right\} \Rightarrow 12 \times 5^6$

$\begin{aligned} & \mathrm{n}\left(\mathrm{S}_1 \cap \mathrm{~S}_3\right)=12 \times 5^3 \\ & \mathrm{n}\left(\mathrm{S}_1 \cup \mathrm{~S}_2 \cup \mathrm{~S}_3\right)=5^6(1+12)-12 \times 5^3 \\ & \quad \Rightarrow 5^3 \times\left[13 \times 5^3-12\right]=125 \alpha \\ & \quad \alpha=1613\end{aligned}$

</details>

---

### Q4. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\left[\begin{array}{lll}2 & a & 0 \\ 1 & 3 & 1 \\ 0 & 5 & b\end{array}\right]$. If $A^3=4 A^2-A-21 I$, where $I$ is the identity matrix of order $3 \times 3$, then $2 a+3 b$ is equal to

**Options:**

- **(A)** -9
- **(B)** -13
- **(C)** -10
- **(D)** -12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -13**

**Detailed Solution:**

$\begin{aligned} & A^3-4 A^2+A+21 I=0 \\ & \operatorname{tr}(A)=4=5+6 \Rightarrow b=-1 \\ & |A|=-21 \\ & -16+a=-21 \Rightarrow a=-5 \\ & 2 a+3 b=-13\end{aligned}$

</details>

---

### Q5. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mn>2</mn><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>A</mi><mo>-</mo><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mi>r</mi><mfenced><mi>A</mi></mfenced></math> denotes the sum of all diagonal elements of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Tr</mo><mo>(</mo><mi>A</mi><mo>)</mo><mo>-</mo><mo>Tr</mo><mo>(</mo><mi>B</mi><mo>)</mo></math> has value equal to<gwmw style="display:none;"></gwmw>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mn>2</mn><mi>B</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mtable><mtr/><mtr/><mtr/></mtable><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>A</mi><mo>-</mo><mi>B</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mtable><mtr/><mtr/><mtr/></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>A</mi><mo>-</mo><mn>2</mn><mi>B</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>10</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>12</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>+</mo><mfenced><mn>2</mn></mfenced><mo>&#8658;</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>5</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>10</mn></mtd></mtr><mtr><mtd><mn>10</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>15</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>B</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>-</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">tr</mo><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>tr</mo><mo>(</mo><mi>B</mi><mo>)</mo><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>tr</mo><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>tr</mo><mo>(</mo><mi>B</mi><mo>)</mo><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>tr</mo><mo>(</mo><mi>A</mi><mo>)</mo><mo>-</mo><mo>tr</mo><mo>(</mo><mi>B</mi><mo>)</mo><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q6. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $p, q, r$ are 3 real numbers satisfying the matrix equation, $[p q r]\left[\begin{array}{lll}3 & 4 & 1 \\ 3 & 2 & 3 \\ 2 & 0 & 2\end{array}\right]=\left[\begin{array}{lll}3 & 0 & 1\end{array}\right]$ then $2 p+q-r$ equals :

**Options:**

- **(A)** $-3$
- **(B)** $-1$
- **(C)** 4
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-3$**

**Detailed Solution:**

Given
$$
\begin{aligned}
& {\left[\begin{array}{lll}
p & q & r
\end{array}\right]\left[\begin{array}{lll}
3 & 4 & 1 \\
3 & 2 & 3 \\
2 & 0 & 2
\end{array}\right]=\left[\begin{array}{lll}
3 & 0 & 1
\end{array}\right]} \\
& \Rightarrow\left[\begin{array}{lll}
3 p+3 q+2 r & 4 p+2 q & p+3 q+2 r
\end{array}\right]=\left[\begin{array}{lll}
3 & 0 & 1
\end{array}\right] \\
& \Rightarrow 3 p+3 q+2 r=3 \\
& 4 p+2 q=0 \Rightarrow q=-2 p \\
& p+3 q+2 r=1 \\
&
\end{aligned}
$$
$p=1, q=-2, r=3$
$\therefore 2 p+q-r=2(1)+(-2)-(3)=-3$.

</details>

---

### Q7. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}1 & 0 & 0 \\ 2 & 1 & 0 \\ -3 & 2 & 1\end{array}\right]$ and $B=\left[\begin{array}{ccc}1 & 0 & 0 \\ -2 & 1 & 0 \\ 7 & -2 & 1\end{array}\right]$ then $A B$ equals

**Options:**

- **(A)** $I$
- **(B)** $A$
- **(C)** $B$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $I$**

**Detailed Solution:**

$$
\begin{aligned}
& A=\left[\begin{array}{ccc}
1 & 0 & 0 \\
2 & 1 & 0 \\
-3 & 2 & 1
\end{array}\right], B=\left[\begin{array}{ccc}
1 & 0 & 0 \\
-2 & 1 & 0 \\
7 & -2 & 1
\end{array}\right] \\
& A B=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]=I
\end{aligned}
$$

</details>

---

### Q8. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\left(\begin{array}{lll}1 & 0 & 0 \\ 2 & 1 & 0 \\ 3 & 2 & 1\end{array}\right)$. If $u_1$ and $u_2$ are column matrices such that $A u_1=\left(\begin{array}{l}1 \\ 0 \\ 0\end{array}\right)$ and $A u_2=\left(\begin{array}{l}0 \\ 1 \\ 0\end{array}\right)$, then $u_1+u_2$ is equal to

**Options:**

- **(A)** $\left(\begin{array}{c}-1 \\ 1 \\ 0\end{array}\right)$
- **(B)** $\left(\begin{array}{c}-1 \\ 1 \\ -1\end{array}\right)$
- **(C)** $\left(\begin{array}{c}-1 \\ -1 \\ 0\end{array}\right)$
- **(D)** $\left(\begin{array}{c}1 \\ -1 \\ -1\end{array}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\begin{array}{c}1 \\ -1 \\ -1\end{array}\right)$**

**Detailed Solution:**

$A=\left(\begin{array}{lll}1 & 0 & 0 \\ 2 & 1 & 0 \\ 3 & 2 & 1\end{array}\right)$
Let $u_1=\left[\begin{array}{l}a \\ b \\ c\end{array}\right] ; u_2=\left[\begin{array}{l}d \\ e \\ f\end{array}\right]$
$\mathrm{Au}_1=\left[\begin{array}{l}1 \\ 0 \\ 0\end{array}\right] \quad \Rightarrow u_1=\left[\begin{array}{c}1 \\ -2 \\ 1\end{array}\right]$
$\mathrm{Au}_2=\left[\begin{array}{l}0 \\ 1 \\ 0\end{array}\right] \quad \Rightarrow \mathrm{u}_2=\left[\begin{array}{c}0 \\ 1 \\ -2\end{array}\right] \quad \Rightarrow \mathrm{u}_1+\mathrm{u}_2=\left[\begin{array}{c}1 \\ -1 \\ -1\end{array}\right]$

</details>

---

### Q9. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\left(\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}\right)$ and $B=\left(\begin{array}{ll}a & 0 \\ 0 & b\end{array}\right), a, b \in N$. Then

**Options:**

- **(A)** there cannot exist any B such that AB = BA
- **(B)** there exist more than one but finite number of B’s such that AB = BA
- **(C)** there exists exactly one B such that AB = BA
- **(D)** there exist infinitely many B’s such that AB = BA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) there exist infinitely many B’s such that AB = BA**

**Detailed Solution:**

$A=\left[\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}\right] \quad B=\left[\begin{array}{ll}a & 0 \\ 0 & b\end{array}\right]$
$A B=\left[\begin{array}{ll}a & 2 b \\ 3 a & 4 b\end{array}\right]$
$B A=\left[\begin{array}{ll}a & 0 \\ 0 & b\end{array}\right]\left[\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}\right]=\left[\begin{array}{cc}a & 2 a \\ 3 b & 4 b\end{array}\right]$
$A B=B A$ only when $a=b$

</details>

---

### Q10. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

If $A^2-A+I=0$, then the inverse of $A$ is

**Options:**

- **(A)** $A+I$
- **(B)** $A$
- **(C)** $A-I$
- **(D)** $I-A$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $I-A$**

**Detailed Solution:**

Given $A^2-A+I=0$
$A^{-1} A^2-A^{-1} A+A^{-1}-I=A^{-1} \cdot 0$ (Multiplying $A^{-1}$ on both sides)
$\Rightarrow A-I+A^{-1}=0$ or $A^{-1}=I-A$

</details>

---

