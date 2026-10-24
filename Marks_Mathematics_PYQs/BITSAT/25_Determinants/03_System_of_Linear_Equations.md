# BITSAT Mathematics - Determinants

## Topic 3: System of Linear Equations

**Total Questions:** 10

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `1`

Suppose $p, q, r \neq 0$ and system of equation
$\begin{gathered}
(p+a) x+b y+c z=0 \\
a x+(q+b) y+c z=0
\end{gathered}$
$a x+b y+(r+c) z=0$, has a non-trivial solution, then the value of $\frac{a}{p}+\frac{b}{q}+\frac{c}{r}$ is

**Options:**

- **(A)** -1
- **(B)** 0
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -1**

**Detailed Solution:**

Let $|A|=\left|\begin{array}{ccc}p+a & b & c \\ a & q+b & c \\ a & b & r+c\end{array}\right|$
Also, given that equations has non trivial solution
$|A|=0$
$\begin{aligned}
& \Rightarrow \quad\left|\begin{array}{ccc}
p+a & b & c \\
a & q+b & c \\
a & b & r+c
\end{array}\right|=0 \\
& \Rightarrow(p+a)[(q+b)(r+c)-b c]-b[a(r+c)-c a] \\
& +c[a b-a(q+b)]=0 \\
& \Rightarrow \quad(p+a)[q r+q c+b r]-b[a r]+c[-a q]=0 \\
& \Rightarrow \quad p q r+p q c+p b r+a q r=0
\end{aligned}$
Dividing whole equation by $p q r$
$\begin{aligned}
\Rightarrow & \frac{p q r}{p q r}+\frac{p q c}{p q r}+\frac{p r b}{p q r}+\frac{q r a}{p q r} & =0 \\
\Rightarrow & 1+\frac{c}{r}+\frac{b}{q}+\frac{a}{p} & =0 \\
\Rightarrow & \frac{a}{p}+\frac{b}{q}+\frac{c}{r} & =-1
\end{aligned}$

</details>

---

### Q2. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

The equations $x-y+2 z=4$
$3 x+y+4 z=6$
$x+y+z=1$ have

**Options:**

- **(A)** unique solution
- **(B)** infinitely many solutions
- **(C)** no solution
- **(D)** two solutions

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) infinitely many solutions**

**Detailed Solution:**

Given equations, $x-y+2 z=4$
$3 x+y+4 z=6$
$x+y+z=1$
Let $\Delta=\left|\begin{array}{ccc}1 & -1 & 2 \\ 3 & 1 & 4 \\ 1 & 1 & 1\end{array}\right|$
$=1(1-4)+1(3-4)+2(3-1)$
$=-3-1+4=0$
and $\Delta_1=\left|\begin{array}{ccc}4 & -1 & 2 \\ 6 & 1 & 4 \\ 1 & 1 & 1\end{array}\right|$
$=4(1-4)+1(6-4)+2(6-1)$
$=-12+2+10=0$
Now, $\Delta=0$ and $\Delta_1=0$
$\therefore$ These equations have infinitely many solutions.

</details>

---

### Q3. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

If the system of linear equations $2 x+y-z=7$
$x-3 y+2 z=1 ; x+4 y+\delta z=k$
where $\delta, k \in R$ has infinitely many solutions, then $\delta+k$ is equal to:

**Options:**

- **(A)** $-3$
- **(B)** $3$
- **(C)** $6$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3$**

**Detailed Solution:**

For getting infinite solutions $\mathrm{D}=0, \mathrm{D}_1=$ $\mathrm{D}_2=\mathrm{D}=0$ then check all the three equations
Let $\Delta=\left|\begin{array}{ccc}2 & 1 & -1 \\ 1 & -3 & 2 \\ 1 & 4 & \delta\end{array}\right|=0 \quad \Rightarrow \delta=-3$
And $\Delta_1=\left|\begin{array}{ccc}7 & 1 & -1 \\ 1 & -3 & 2 \\ k & 4 & -3\end{array}\right|=0 \Rightarrow k=6$
$\Rightarrow \delta+k=3$

</details>

---

### Q4. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `2`

If $p \neq a, q \neq b, r \neq c$ and the system of equations
$\begin{aligned}
& p x+a y+a z=0 \\
& b x+q y+b z=0 \\
& c x+c y+r z=0
\end{aligned}$
has a non-trivial solution, then the value of 
$\frac{p}{p-a}+\frac{q}{q-b}+\frac{r}{r-c}$ is

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $\frac{1}{2}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

As the given system of equations has a non-trivial solution.
$\Delta=\left|\begin{array}{lll}p & a & a \\ b & q & b \\ c & c & r\end{array}\right|=0$
Applying $C_2 \rightarrow C_2-C_1$ and $C_3 \rightarrow C_3-C_1$
$\Delta=\left|\begin{array}{ccc}p & a-p & a-p \\ b & q-b & 0 \\ c & 0 & r-c\end{array}\right|=0$
Expanding along $C_3$, we get
$(a-p)\left|\begin{array}{cc}b & q-b \\ c & 0\end{array}\right|+(r-c)\left|\begin{array}{cc}p & a-p \\ b & q-b\end{array}\right|=0$
$\begin{aligned}
& \Rightarrow(a-p)(-c)(q-b)+(r-c) \\
& \{p(q-b)-b(a-p)\}=0 \\
& \Rightarrow \\
& (p-a)(q-b) c+p(r-c)(q-b)+b(r-c)(p-a)=0
\end{aligned}$
Dividing by $(p-a)(q-b)(r-c)$, we get
$\frac{c}{r-c}+\frac{p}{p-a}+\frac{b}{q-b}=0$
$\Rightarrow \frac{p}{p-a}+\frac{q}{q-b}+\frac{r}{r-c}=\frac{q-b}{q-b}+\frac{r-c}{r-c}=2$

</details>

---

### Q5. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `1`

Given $2 x-y+2 z=2, x-2 y+z=-4$, $x+y+\lambda z=4$, then the value of $\lambda$ such that the given system of equation has no solution is

**Options:**

- **(A)** $-3$
- **(B)** 1
- **(C)** 0
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

Since, the system has no solution.
$\left|\begin{array}{ccc}2 & -1 & 2 \\ 1 & -2 & -1 \\ 1 & 1 & \lambda\end{array}\right|=0$
$\Rightarrow 2(-2 \lambda+1)+1(\lambda+1)+2(3)=0$
$\Rightarrow \quad-4 \lambda+2+\lambda+1+6=0$
$\Rightarrow \quad 3 \lambda=9 \Rightarrow \lambda=3$

</details>

---

### Q6. BITSAT 2020

*Type:* `singleCorrect` | *Level:* `1`

Suppose $\mathrm{p}, \mathrm{q}, \mathrm{r} \neq 0$ and system of equation $(\mathrm{p}+\mathrm{a}) \mathrm{x}+\mathrm{by}+\mathrm{cz}=0$

$a x+(q+b) y+c z=0$

$a x+b y+(r+c) z=0$ has a non-trivial solution,

then value of $\frac{a}{p}+\frac{b}{q}+\frac{c}{r}$ is

**Options:**

- **(A)** -1
- **(B)** 0
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -1**

**Detailed Solution:**

Since the system is homogeneous and has a non-trivial solution

$0=\left|\begin{array}{ccc}p+a & b & c \\ a & q+b & c \\ a & b & r+c\end{array}\right|=\left|\begin{array}{ccc}p & -q & 0 \\ 0 & q & -r \\ a & b & r+c\end{array}\right|$

using $\mathrm{R}_{1} \rightarrow \mathrm{R}_{1}-\mathrm{R}_{2}$ and $\mathrm{R}_{2} \rightarrow \mathrm{R}_{2}-\mathrm{R}_{3}$

Expanding along $\mathrm{C}$, we get $\Rightarrow \mathrm{p}[\mathrm{q}(\mathrm{r}+\mathrm{c})+\mathrm{br}]+\mathrm{aqr}=0$

$\Rightarrow \mathrm{pqr}+\mathrm{pqc}+\mathrm{prb}+\mathrm{qra}=0$

$\Rightarrow \frac{a}{p}+\frac{b}{q}+\frac{c}{r}=-1$

</details>

---

### Q7. BITSAT 2019

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>&#8712;</mo><msup><mi>R</mi><mo>+</mo></msup></math> and the system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>-</mo><mi>a</mi><mo>)</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>+</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>b</mi><mo>)</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>c</mi><mo>)</mo><mi>z</mi><mo>=</mo><mn>0</mn></math> has infinitely many solutions, the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>b</mi></mrow></mfenced><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfenced><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p>has many solutions </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn><mo>-</mo><mi>a</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn><mo>-</mo><mi>b</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn><mo>-</mo><mi>c</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>a</mi><mi>b</mi><mo>+</mo><mi>a</mi><mi>c</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>=</mo><mi>a</mi><mi>b</mi><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfrac><mrow><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>a</mi><mi>c</mi></mrow><mn>3</mn></mfrac><mo>&#8805;</mo><msup><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mspace linebreak="newline"/><mo>&#8658;</mo><msup><mfenced><mrow><mi>a</mi><mi>b</mi><mi>c</mi></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>&#8805;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Minimum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mo>=</mo><msup><mfenced><mn>3</mn></mfenced><mn>3</mn></msup><mo>=</mo><mn>27</mn></math></p>

</details>

---

### Q8. BITSAT 2019

*Type:* `singleCorrect` | *Level:* `1`

If system of equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>a</mi><mo>,</mo><mi>x</mi><mo>+</mo><mi>b</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>c</mi><mi>z</mi><mo>=</mo><mi>c</mi></math> is inconsistent, then which of the following is correct?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mo>-</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>-</mo><mi>c</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mo>-</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>-</mo><mi>c</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mo>-</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>-</mo><mi>c</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mo>-</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>-</mo><mi>c</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>&#8800;</mo><mn>1</mn><mo>,</mo><mi>b</mi><mo>&#8800;</mo><mn>1</mn><mo>,</mo><mi>c</mi><mo>&#8800;</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mo>-</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>-</mo><mi>c</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>&#8800;</mo><mn>1</mn><mo>,</mo><mi>b</mi><mo>&#8800;</mo><mn>1</mn><mo>,</mo><mi>c</mi><mo>&#8800;</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>We have, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>a</mi></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>b</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>b</mi></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>ii</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>c</mi><mi>z</mi><mo>=</mo><mi>c</mi></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>iii</mi><mo>)</mo></math></p><p>are inconsistent. </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mo>&#8756;</mo></mtd><mtd><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>b</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mi>b</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>b</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>a</mi><mo>(</mo><mi>b</mi><mi>c</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>-</mo><mn>1</mn><mo>(</mo><mi>c</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>+</mo><mn>1</mn><mo>(</mo><mn>1</mn><mo>-</mo><mi>b</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mo>-</mo><mi>a</mi><mo>-</mo><mi>c</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>-</mo><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mo>-</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>-</mo><mi>c</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mi>b</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p>It is possible only when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8800;</mo><mn>1</mn><mo>,</mo><mi>b</mi><mo>&#8800;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>&#8800;</mo><mn>1</mn></math></p>

</details>

---

### Q9. BITSAT 2016

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha_{1}, \alpha_{2}$ and $\beta_{1}, \beta_{2}$ be the roots of $a x^{2}+b x+c$ $=0$ and $\mathrm{px}^{2}+\mathrm{qx}+\mathrm{r}=0$ respectively. If the system of equations $\alpha_{1} \mathrm{y}+\alpha_{2} \mathrm{z}=0$ and $\beta_{1} \mathrm{y}+\beta_{2} \mathrm{z}=0$ has a non-trivial solution, then

**Options:**

- **(A)** $\frac{b^{2}}{q^{2}}=\frac{a c}{p r}$
- **(B)** $\frac{\mathrm{c}^{2}}{\mathrm{r}^{2}}=\frac{\mathrm{ab}}{\mathrm{pq}}$
- **(C)** $\frac{a^{2}}{p^{2}}=\frac{b c}{q r}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{b^{2}}{q^{2}}=\frac{a c}{p r}$**

**Detailed Solution:**

Since $\alpha_{1}, \alpha_{2}$ and $\beta_{1}, \beta_{2}$ are the roots of ax $^{2}$ $+b x+c=0$ and $p x^{2}+q x+r=0$ respectively

therefore

$$

\alpha_{1}+\alpha_{2}=\frac{-b}{a}, \alpha_{1} \alpha_{2}=\frac{c}{a}

$$

and $\beta_{1}+\beta_{2}=\frac{-q}{p}, \beta_{1} \beta_{2}=\frac{r}{p}$

Since the given system of equation has a non-trivial solution

$$

\therefore\left|\begin{array}{ll}

\alpha_{1} & \alpha_{2} \\

\beta_{1} & \beta_{2}

\end{array}\right|=0 \text { i.e. } \alpha_{1} \beta_{2}-\alpha_{2} \beta_{1}=0

$$

or $\quad \frac{\alpha_{1}}{\beta_{1}}=\frac{\alpha_{2}}{\beta_{2}}=\frac{\alpha_{1}+\alpha_{2}}{\beta_{1}+\beta_{2}}=\sqrt{\frac{\alpha_{1} \alpha_{2}}{\beta_{1} \beta_{2}}}$

$\Rightarrow \frac{\mathrm{pb}}{\mathrm{qa}}=\sqrt{\frac{\mathrm{pc}}{\mathrm{ra}}} \Rightarrow \frac{\mathrm{b}^{2}}{\mathrm{q}^{2}}=\frac{\mathrm{ac}}{\mathrm{pr}}$

</details>

---

### Q10. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `1`

The equations $2 x+3 y+4=0 ; 3 x+4 y+6=0$ and $4 x+5 y+8=0$ are

**Options:**

- **(A)** consistent with unique solution
- **(B)** inconsistent
- **(C)** consistent with infinitely many solutions
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) consistent with unique solution**

**Detailed Solution:**

Consider first two equations:
$2 x+3 y=-4 \quad$ and $\quad 3 x+4 y=-6$
We have $\Delta=\left|\begin{array}{ll}2 & 3 \\ 3 & 4\end{array}\right|=-1 \neq 0$
$$
\Delta_{\mathrm{x}}=\left|\begin{array}{ll}
-4 & 3 \\
-6 & 4
\end{array}\right|=2 \quad \text { and } \quad \Delta_{\mathrm{y}}=\left|\begin{array}{cc}
2 & -4 \\
3 & -6
\end{array}\right|=0
$$
$\therefore x=-2$ and $y=0$
Now this solution satisfies the third, so the equations are consistent with unique solution.

</details>

---

