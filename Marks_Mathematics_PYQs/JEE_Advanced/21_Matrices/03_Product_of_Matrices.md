# JEE Advanced Mathematics - Matrices

## Topic 3: Product of Matrices

**Total Questions:** 13

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let $\mathbb{R}$ denote the set of all real numbers and let $i = \sqrt{-1}$. Consider the matrices
$S = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ and $T = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$.
Let $a, b, c, d$ be real numbers such that
$ST = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$.
Let
$H = \{x + iy : x, y \in \mathbb{R} \text{ and } y > 0\}$.
Then which of the following statements is (are) TRUE ?

**Options:**

- **(A)** $\dfrac{b + ia}{d + ic} = i$
- **(B)** If $\omega = \dfrac{-1 + i\sqrt{3}}{2}$, then $\dfrac{a\omega + b}{c\omega + d} = \omega$
- **(C)** If $m$ is an integer greater than $2$ such that $(ST)^2 = (ST)^m$, then $m$ is an integer multiple of $8$
- **(D)** If $z \in H$, then $\dfrac{az + b}{cz + d} \in H$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) If $z \in H$, then $\dfrac{az + b}{cz + d} \in H$**

**Detailed Solution:**

We are given the matrices $S = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ and $T = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$.

First, we compute the product $ST$:
$ST = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 \\ 1 & 1 \end{bmatrix}$

Comparing this with $ST = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, we get $a = 0$, $b = -1$, $c = 1$, and $d = 1$.

Evaluating Option (A):
$\dfrac{b + ia}{d + ic} = \dfrac{-1 + i(0)}{1 + i(1)} = \dfrac{-1}{1 + i} = \dfrac{-1(1 - i)}{(1 + i)(1 - i)} = \dfrac{-1 + i}{2}$
This is not equal to $i$, so statement (A) is FALSE.

Evaluating Option (B):
Given $\omega = \dfrac{-1 + i\sqrt{3}}{2}$, which is a complex cube root of unity, satisfying $\omega^2 + \omega + 1 = 0$ and $\omega^3 = 1$.
$\dfrac{a\omega + b}{c\omega + d} = \dfrac{0 \cdot \omega - 1}{1 \cdot \omega + 1} = \dfrac{-1}{\omega + 1}$
Since $\omega + 1 = -\omega^2$, we have:
$\dfrac{-1}{-\omega^2} = \dfrac{1}{\omega^2} = \dfrac{\omega^3}{\omega^2} = \omega$
Thus, statement (B) is TRUE.

Evaluating Option (C):
The characteristic equation of $ST$ is $\lambda^2 - \text{Tr}(ST)\lambda + \det(ST) = 0$, which gives $\lambda^2 - \lambda + 1 = 0$.
By the Cayley-Hamilton theorem, $(ST)^2 - ST + I = 0$.
Multiplying by $(ST + I)$, we get $(ST)^3 + I = 0 \Rightarrow (ST)^3 = -I$.
Squaring both sides gives $(ST)^6 = I$.
We are given $(ST)^2 = (ST)^m$, which implies $(ST)^{m-2} = I$.
This means $m - 2$ must be a multiple of $6$, so $m = 6k + 2$ for some integer $k$.
For $k = 1$, $m = 8$ (which is a multiple of $8$).
For $k = 2$, $m = 14$ (which is NOT a multiple of $8$).
Thus, statement (C) is FALSE.

Evaluating Option (D):
For $z \in H$, let $z = x + iy$ where $y > 0$.
$\dfrac{az + b}{cz + d} = \dfrac{-1}{z + 1} = \dfrac{-1}{(x + 1) + iy}$
Multiplying the numerator and denominator by the conjugate $(x + 1) - iy$:
$\dfrac{-1}{(x + 1) + iy} \times \dfrac{(x + 1) - iy}{(x + 1) - iy} = \dfrac{-(x + 1) + iy}{(x + 1)^2 + y^2}$
The imaginary part of this new complex number is $\dfrac{y}{(x + 1)^2 + y^2}$.
Since $y > 0$ and $(x + 1)^2 + y^2 > 0$, the imaginary part is strictly positive.
Therefore, $\dfrac{az + b}{cz + d} \in H$, making statement (D) TRUE.

Answer: If $\omega = \dfrac{-1 + i\sqrt{3}}{2}$, then $\dfrac{a\omega + b}{c\omega + d} = \omega$; If $z \in H$, then $\dfrac{az + b}{cz + d} \in H$

</details>

---

### Q2. JEE Advanced 2026 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

Consider the matrix

$M = \begin{bmatrix} 2 & -1 \\ 1 & 0 \end{bmatrix}$.

Let $p, q, r, s, a, b, c$ and $d$ be integers such that

$M^{26} = \begin{bmatrix} p & q \\ r & s \end{bmatrix}$ and $\sum_{k=1}^{26} M^k = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$.

Then which of the following statements is (are) TRUE?

**Options:**

- **(A)** There exists a $2 \times 2$ invertible matrix $N$ with real entries such that $MN = N \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$
- **(B)** The value of $a$ is $378$
- **(C)** For any two given integers $m$ and $n$, there exist unique integers $x$ and $y$ such that $px + qy = m$ and $rx + sy = n$
- **(D)** For each positive real number $t$, the system of linear equations $(a + t)x + by = 1$ and $cx + (d + t)y = -1$ has a unique solution

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) For each positive real number $t$, the system of linear equations $(a + t)x + by = 1$ and $cx + (d + t)y = -1$ has a unique solution**

**Detailed Solution:**

The characteristic equation of $M$ is given by $\det(M - \lambda I) = 0$:
$\begin{vmatrix} 2 - \lambda & -1 \\ 1 & -\lambda \end{vmatrix} = \lambda^2 - 2\lambda + 1 = (\lambda - 1)^2 = 0$
The only eigenvalue is $\lambda = 1$ with algebraic multiplicity $2$.

For the eigenvector, $(M - I)X = 0 \Rightarrow \begin{bmatrix} 1 & -1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \Rightarrow x = y$.
Since there is only one linearly independent eigenvector, $M$ is not diagonalizable but can be reduced to its Jordan canonical form $J = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$.
Thus, there exists an invertible matrix $N$ such that $M = N J N^{-1} \Rightarrow MN = N \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$.
Statement (A) is TRUE.

We can write $M = I + A$, where $A = \begin{bmatrix} 1 & -1 \\ 1 & -1 \end{bmatrix}$.
Notice that $A^2 = \begin{bmatrix} 1 & -1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 1 & -1 \\ 1 & -1 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$.
Using the binomial theorem (since $I$ and $A$ commute), $M^k = (I + A)^k = I + kA = \begin{bmatrix} 1+k & -k \\ k & 1-k \end{bmatrix}$.

For $k=26$, $M^{26} = \begin{bmatrix} 27 & -26 \\ 26 & -25 \end{bmatrix} = \begin{bmatrix} p & q \\ r & s \end{bmatrix}$.
The determinant of $M^{26}$ is $ps - qr = 27(-25) - (-26)(26) = 1$.
Since $\det(M^{26}) = 1$, its inverse has integer entries. Thus, for any integers $m$ and $n$, the system $\begin{bmatrix} p & q \\ r & s \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} m \\ n \end{bmatrix}$ has a unique integer solution.
Statement (C) is TRUE.

Now, let's find $\sum_{k=1}^{26} M^k = \sum_{k=1}^{26} \begin{bmatrix} 1+k & -k \\ k & 1-k \end{bmatrix} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$.
$a = \sum_{k=1}^{26} (1+k) = 2 + 3 + \dots + 27 = \dfrac{26}{2}(2 + 27) = 13 \times 29 = 377$.
Statement (B) is FALSE.

We also have:
$b = \sum_{k=1}^{26} (-k) = -351$
$c = \sum_{k=1}^{26} k = 351$
$d = \sum_{k=1}^{26} (1-k) = 26 - 351 = -325$

For statement (D), the system of equations is $\begin{bmatrix} a+t & b \\ c & d+t \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$.
The determinant of the coefficient matrix is:
$\Delta = (a+t)(d+t) - bc = (377+t)(-325+t) - (-351)(351)$
$\Delta = t^2 + 52t - 122525 + 123201 = t^2 + 52t + 676 = (t+26)^2$
For any positive real number $t > 0$, $\Delta = (t+26)^2 > 0$, meaning the determinant is non-zero. Hence, the system has a unique solution.
Statement (D) is TRUE.

Answer: There exists a $2 \times 2$ invertible matrix $N$ with real entries such that $MN = N \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$; For any two given integers $m$ and $n$, there exist unique integers $x$ and $y$ such that $px + qy = m$ and $rx + sy = n$; For each positive real number $t$, the system of linear equations $(a + t)x + by = 1$ and $cx + (d + t)y = -1$ has a unique solution

</details>

---

### Q3. JEE Advanced 2025 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let $I=\left(\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right)$ and $P=\left(\begin{array}{ll}2 & 0 \\ 0 & 3\end{array}\right)$. Let $Q=\left(\begin{array}{ll}\mathrm{x} & \mathrm{y} \\ \mathrm{z} & 4\end{array}\right)$ for some non-zero real numbers $x, y$, and $z$, for which there is $2 \times 2$ matrix $R$ with all entries being non-zero real numbers, such that $Q R=R P$. Then which of the following statements is (are) TRUE?

**Options:**

- **(A)** The determinant of $Q-2 I$ is zero
- **(B)** The determinant of $\mathrm{Q}-6 I$ is 12
- **(C)** The determinant of $Q-3 I$ is 15
- **(D)** $y z=2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) The determinant of $\mathrm{Q}-6 I$ is 12**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{QR}=\mathrm{RP} \\
& P=\left(\begin{array}{ll}
2 & 0 \\
0 & 3
\end{array}\right) \quad Q=\left(\begin{array}{ll}
x & y \\
z & 4
\end{array}\right) \\
& \left(\begin{array}{ll}
x & y \\
z & 4
\end{array}\right)\left(\begin{array}{ll}
r_1 & r_2 \\
r_3 & r_4
\end{array}\right)=\left(\begin{array}{ll}
r_1 & r_2 \\
r_3 & r_4
\end{array}\right)\left(\begin{array}{ll}
2 & 0 \\
0 & 3
\end{array}\right) \\
& \left.\begin{array}{l}
\mathrm{xr}_1+\mathrm{yr}_3=2 \mathrm{r}_1 \\
\mathrm{zr}_1+4 \mathrm{r}_3=2 \mathrm{r}_3
\end{array}\right\} \rightarrow \frac{\mathrm{x}-2}{-\mathrm{y}}=\frac{\mathrm{r}_3}{\mathrm{r}_1}=\frac{\mathrm{z}}{-2}
\end{aligned}$
\(2 x-4=y z\)
$\left.\begin{array}{l}\mathrm{xr}_2+\mathrm{yr}_4=3 \mathrm{r}_2 \\ \mathrm{zr}_2+4 \mathrm{r}_4=3 \mathrm{r}_4\end{array}\right\} \rightarrow \frac{\mathrm{x}-3}{-\mathrm{y}}=\frac{\mathrm{r}_4}{\mathrm{r}_2}=-\mathrm{z} \quad$ \(\mathrm{x}-3=\mathrm{yz}\)
$\Rightarrow 2 x-4=x-3$ \(\Rightarrow x=1 ~\&~ y z=-2\)
$\begin{aligned}
& \Rightarrow \mathrm{Q}-\lambda \mathrm{I}=\left(\begin{array}{cc}
\mathrm{x}-\lambda & \mathrm{y} \\
\mathrm{z} & 4-\lambda
\end{array}\right) \\
& |\mathrm{Q}-\lambda \mathrm{I}|=(\lambda-\mathrm{x})(\lambda-4)-\mathrm{yz} \\
& =\lambda^2-(\mathrm{x}+4) \lambda+4 \mathrm{x}-\mathrm{yz} \\
& |\mathrm{Q}-\lambda \mathrm{I}|=\lambda^2-5 \lambda+6
\end{aligned}$
Now verify the option

</details>

---

### Q4. JEE Advanced 2022 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfenced><mtable><mtr><mtd><mfrac><mn>5</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced></math>, then which of the following matrices is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>M</mi><mn>2022</mn></msup></math> ?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtable><mtr><mtd><mn>3034</mn></mtd><mtd><mn>3033</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3033</mn></mtd><mtd><mo>-</mo><mn>3032</mn></mtd></mtr></mtable></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtable columnalign="left"><mtr><mtd><mn>3034</mn></mtd><mtd><mo>-</mo><mn>3033</mn></mtd></mtr><mtr><mtd><mn>3033</mn></mtd><mtd><mo>-</mo><mn>3032</mn></mtd></mtr></mtable></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtable><mtr><mtd><mn>3033</mn></mtd><mtd><mn>3032</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3032</mn></mtd><mtd><mo>-</mo><mn>3031</mn></mtd></mtr></mtable></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtable><mtr><mtd><mn>3032</mn></mtd><mtd><mn>3031</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3031</mn></mtd><mtd><mo>-</mo><mn>3030</mn></mtd></mtr></mtable></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtable><mtr><mtd><mn>3034</mn></mtd><mtd><mn>3033</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3033</mn></mtd><mtd><mo>-</mo><mn>3032</mn></mtd></mtr></mtable></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfenced><mtable><mtr><mtd><mfrac><mn>5</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>M</mi><mn>2</mn></msup><mo>=</mo><mfenced><mtable><mtr><mtd><mfrac><mn>5</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced><mfenced><mtable><mtr><mtd><mfrac><mn>5</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>M</mi><mn>3</mn></msup><mo>=</mo><mfenced><mtable><mtr><mtd><mfrac><mn>5</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced><mfenced><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable><mtr><mtd><mfrac><mn>11</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>9</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>M</mi><mn>4</mn></msup><mo>=</mo><mfenced><mtable><mtr><mtd><mfrac><mn>11</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>9</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced><mfenced><mtable><mtr><mtd><mfrac><mn>11</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>9</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable><mtr><mtd><mn>7</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr></mtable></mfenced></math></p><p>and so on</p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>M</mi><mi>n</mi></msup><mo>=</mo><mfenced><mtable><mtr><mtd><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mtd><mtd><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>M</mi><mn>2022</mn></msup><mo>=</mo><mfenced><mtable><mtr><mtd><mfrac><mrow><mn>3</mn><mo>&#215;</mo><mn>2022</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mtd><mtd><mfrac><mrow><mn>3</mn><mo>&#215;</mo><mn>2022</mn></mrow><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mrow><mn>3</mn><mo>&#215;</mo><mn>2022</mn></mrow><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mrow><mn>3</mn><mo>&#215;</mo><mn>2022</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mtable><mtr><mtd><mn>3034</mn></mtd><mtd><mn>3033</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3033</mn></mtd><mtd><mo>-</mo><mn>3032</mn></mtd></mtr></mtable></mfenced></math></p></blockquote>

</details>

---

### Q5. JEE Advanced 2022 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> be a real number. Consider the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced><mtable><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>7</mn></msup><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>A</mi><mn>6</mn></msup><mo>-</mo><mi>&#946;</mi><msup><mi>A</mi><mn>5</mn></msup></math> is a singular matrix, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#946;</mi></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced><mtable><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>det</mo><mfenced><mi>A</mi></mfenced><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>7</mn></msup><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>A</mi><mn>6</mn></msup><mo>-</mo><mi>&#946;</mi><msup><mi>A</mi><mn>5</mn></msup></math> to be singular</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>A</mi><mn>7</mn></msup><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>A</mi><mn>6</mn></msup><mo>-</mo><mi>&#946;</mi><msup><mi>A</mi><mn>5</mn></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><msup><mi>A</mi><mn>5</mn></msup></mfenced><mfenced close="|" open="|"><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mo>(</mo><mi>&#946;</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>A</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><msup><mi>A</mi><mn>5</mn></msup></mfenced><mfenced close="|" open="|"><mrow><mfenced><mrow><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mfenced><mrow><mi>A</mi><mo>-</mo><mi>&#946;</mi><mi>l</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced close="|" open="|"><msup><mi>A</mi><mn>5</mn></msup></mfenced><mfenced close="|" open="|"><mrow><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mfenced close="|" open="|"><mrow><mi>A</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>A</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>A</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mtable><mtr><mtd><mi>&#946;</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mtext>here&#160;</mtext><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>&#8800;</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced close="|" open="|"><mrow><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>A</mi><mo>-</mo><mi>&#946;</mi><mi>l</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn><mo>-</mo><mi>&#946;</mi></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn><mo>-</mo><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>-</mo><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>-</mo><mn>3</mn><mo>+</mo><mn>3</mn><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mn>9</mn><mi>&#946;</mi><mo>=</mo><mn>3</mn></math></p></blockquote>

</details>

---

### Q6. JEE Advanced 2017 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

The number of <math><mn>3</mn><mo>×</mo><mn>3</mn></math> matrices <math><mi>M</mi></math> with entries from <math><mo>{</mo><mn>0,1</mn><mo>,</mo><mn>2</mn><mo>}</mo></math>, such that the sum of the diagonal elements of <math><msup><mrow><mi>M</mi></mrow><mrow><mi>T</mi></mrow></msup><mi>M</mi></math> is <math><mn>5</mn></math>, are

**Options:**

- **(A)** <math><mn>198</mn></math>
- **(B)** <math><mn>126</mn></math>
- **(C)** <math><mn>135</mn></math>
- **(D)** <math><mn>162</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>198</mn></math>**

**Detailed Solution:**

<p>Let,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>d</mi></mtd><mtd><mi>e</mi></mtd><mtd><mi>f</mi></mtd></mtr><mtr><mtd><mi>g</mi></mtd><mtd><mi>h</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Sum of the diagonal elements, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Tr</mi><mo>(</mo><msup><mi>M</mi><mi>T</mi></msup><mtext>&#8203;</mtext><mtext>&#8201;</mtext><mi>M</mi><mo>)</mo><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><msup><mi>f</mi><mn>2</mn></msup><mo>+</mo><msup><mi>g</mi><mn>2</mn></msup><mo>+</mo><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><msup><mi>i</mi><mn>2</mn></msup><mo>=</mo><mn>5</mn><mo>,</mo></math> where entries are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Only two cases are possible.</p><p>(I) Five entries are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and other fourare <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></p><p><math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>9</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>&#215;</mo><mn>1</mn></math></p><p>(II) One entry is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, one entry is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and others are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>.</p><p><math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>9</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&#215;</mo><mn>2</mn></math></p><p>Total cases<math><mo>=</mo><mn>126</mn><mo>+</mo><mn>72</mn><mo>=</mo><mn>198</mn><mo>.</mo></math></p>

</details>

---

### Q7. JEE Advanced 2016 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>P</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>16</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> and <math><mi>I</mi></math> be the identity matrix of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>. If <math><mi>Q</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><msub><mrow><mi>q</mi></mrow><mrow><mi>i</mi><mi>j</mi></mrow></msub></mrow></mfenced></math> is a matrix such that <math><msup><mrow><mi>P</mi></mrow><mrow><mn>50</mn></mrow></msup><mo>-</mo><mi>Q</mi><mo>=</mo><mi>I</mi><mo>,</mo></math> then the value of <math><mfrac><mrow><msub><mrow><mi>q</mi></mrow><mrow><mn>31</mn></mrow></msub><mo>+</mo><msub><mrow><mi>q</mi></mrow><mrow><mn>32</mn></mrow></msub></mrow><mrow><msub><mrow><mi>q</mi></mrow><mrow><mn>21</mn></mrow></msub></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>103</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>201</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>205</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>103</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>16</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mi>&#160;</mi><mi>&#160;</mi><mspace linebreak="newline"/><mo>&#8658;</mo><msup><mi>P</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>8</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>16</mn><mo>+</mo><mn>32</mn></mtd><mtd><mn>8</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
So, <math><msup><mrow><mi>P</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>12</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>16</mn><mo>+</mo><mn>32</mn><mo>+</mo><mn>48</mn></mtd><mtd><mn>12</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
Using symmetry, we can write
<math><msup><mrow><mi>P</mi></mrow><mrow><mn>50</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>200</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mrow><mn>16.50.51</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mn>200</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
As, <math> <mrow> <msup> <mi>P</mi> <mrow> <mn>50</mn> </mrow> </msup> <mo>&#8722;</mo><mi>Q</mi><mo>=</mo><mi>I</mi><mo>&#8658;</mo><mi>Q</mi><mo>=</mo><msup> <mi>P</mi> <mrow> <mn>50</mn> </mrow> </msup> <mo>&#8722;</mo><mi>I</mi><mo>=</mo><mrow><mo>[</mo> <mrow> <mtable> <mtr> <mtd> <mn>0</mn> </mtd> <mtd> <mn>0</mn> </mtd> <mtd> <mn>0</mn> </mtd> </mtr> <mtr> <mtd> <mrow> <mn>200</mn> </mrow> </mtd> <mtd> <mn>0</mn> </mtd> <mtd> <mn>0</mn> </mtd> </mtr> <mtr> <mtd> <mrow> <mfrac> <mrow> <mn>16.50.51</mn> </mrow> <mn>2</mn> </mfrac> </mrow> </mtd> <mtd> <mrow> <mn>200</mn> </mrow> </mtd> <mtd> <mn>0</mn> </mtd> </mtr> </mtable> </mrow> <mo>]</mo></mrow><mtext>&#8201;</mtext><mo>,</mo></mrow></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>31</mn></msub><mo>=</mo><mfrac><mn>16.50.51</mn><mn>2</mn></mfrac><mo>,</mo></math>  <math><msub><mrow><mi>q</mi></mrow><mrow><mn>32</mn></mrow></msub><mo>=</mo><mn>200</mn></math> and <math><msub><mrow><mi>q</mi></mrow><mrow><mn>21</mn></mrow></msub><mo>=</mo><mn>200</mn></math>
<math><mo>&#8756;</mo></math> <math><mfrac><mrow><msub><mrow><mi>q</mi></mrow><mrow><mn>31</mn></mrow></msub><mo>+</mo><msub><mrow><mi>q</mi></mrow><mrow><mn>32</mn></mrow></msub></mrow><mrow><msub><mrow><mi>q</mi></mrow><mrow><mn>21</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>16.50.51</mn></mrow><mrow><mn>2.200</mn></mrow></mfrac><mo>+</mo><mn>1</mn><mo>=</mo><mn>102</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>103</mn></math>

</details>

---

### Q8. JEE Advanced 2016 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Let <math><mtext>z</mtext><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mtext>&#160;</mtext><msqrt><mn>3</mn></msqrt><mtext>i</mtext></mrow><mrow><mn>2</mn></mrow></mfrac></math> , where <math><mtext>i</mtext><mo>=</mo><mtext>&#160;</mtext><msqrt><mo>-</mo><mn>1</mn></msqrt></math> , and <math><mtext>r</mtext><mo>,</mo><mtext>&#160;</mtext><mtext>s</mtext><mo>&#8712;</mo><mfenced close="}" open="{" separators="|"><mrow><mn>1</mn><mo>,</mo><mtext>&#160;</mtext><mn>2</mn><mo>,</mo><mtext>&#160;</mtext><mn>3</mn></mrow></mfenced><mo>.</mo></math> Let <math><mtext>P</mtext><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>z</mn></mrow></mfenced></mrow><mrow><mtext>r</mtext></mrow></msup></mtd><mtd><msup><mrow><mtext>z</mtext></mrow><mrow><mn>2</mn><mtext>s</mtext></mrow></msup></mtd></mtr><mtr><mtd><msup><mrow><mtext>z</mtext></mrow><mrow><mn>2</mn><mtext>s</mtext></mrow></msup></mtd><mtd><msup><mrow><mtext>z</mtext></mrow><mrow><mtext>r</mtext></mrow></msup></mtd></mtr></mtable></mrow></mfenced></math> and <math><mtext>I</mtext></math> be the identity matrix of order 2. Then the total number of ordered pairs <math> <mrow> <mo stretchy="false">(</mo><mtext>r</mtext><mo>,</mo><mtext>s</mtext><mo stretchy="false">)</mo> </mrow> </math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mtext>P</mtext><mn>2</mn></msup><mo>=</mo><mo>-</mo><mtext>I</mtext></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<math><mtext>z</mtext><mo>=</mo><mtext>&#969;</mtext></math> (<math><mtext>&#969;</mtext></math> is complex cube root of unity)
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>P</mtext><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><msup><mfenced separators="|"><mrow><mo>-</mo><mtext>&#969;</mtext></mrow></mfenced><mtext>r</mtext></msup></mtd><mtd><msup><mtext>&#969;</mtext><mrow><mn>2</mn><mtext>s</mtext></mrow></msup></mtd></mtr><mtr><mtd><msup><mtext>&#969;</mtext><mrow><mn>2</mn><mtext>s</mtext></mrow></msup></mtd><mtd><msup><mtext>&#969;</mtext><mtext>r</mtext></msup></mtd></mtr></mtable></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mtext>P</mtext><mn>2</mn></msup><mo>=</mo><mo>-</mo><mtext>I</mtext></math>
<math><mo>&#8658;</mo><msup><mrow><mtext>P</mtext></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mtext>&#969;</mtext></mrow><mrow><mn>2</mn><mtext>r</mtext></mrow></msup><mo>+</mo><msup><mrow><mtext>&#969;</mtext></mrow><mrow><mn>4</mn><mtext>s</mtext></mrow></msup></mtd><mtd><msup><mrow><mtext>&#969;</mtext></mrow><mrow><mtext>r</mtext><mo>+</mo><mn>2</mn><mtext>s</mtext></mrow></msup><mfenced separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mtext>r</mtext></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mtd></mtr><mtr><mtd><msup><mrow><mtext>&#969;</mtext></mrow><mrow><mtext>r</mtext><mo>+</mo><mn>2</mn><mtext>s</mtext></mrow></msup><mfenced separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mtext>r</mtext></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mtd><mtd><msup><mrow><mtext>&#969;</mtext></mrow><mrow><mn>4</mn><mtext>s</mtext></mrow></msup><mo>+</mo><msup><mrow><mtext>&#969;</mtext></mrow><mrow><mn>2</mn><mtext>r</mtext></mrow></msup></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mtext>&#160;</mtext><mo>-</mo><mtext>I</mtext></math> <math><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtext> </mtext><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mtext> </mtext></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mtext>r</mtext></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>r</mi></math> is odd <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#160;</mtext><mtext>r</mtext><mo>=</mo><mn>1</mn><mo>,</mo><mtext>&#160;</mtext><mn>3</mn></math>
Also <math><msup><mrow><mtext>&#969;</mtext></mrow><mrow><mn>2</mn><mtext>r</mtext></mrow></msup><mo>+</mo><msup><mrow><mtext>&#969;</mtext></mrow><mrow><mn>4</mn><mtext>s</mtext></mrow></msup><mo>=</mo><mtext>&#160;</mtext><mo>-</mo><mn>1</mn></math>
<math><mo>&#8756;</mo></math> <math><mtext>r</mtext><mtext>&#160;</mtext><mo>&#8800;</mo><mn>3</mn></math>
By <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>r</mtext><mo>=</mo><mn>1</mn><mo>&#8658;</mo><msup><mtext>&#969;</mtext><mn>2</mn></msup><mo>+</mo><msup><mtext>&#969;</mtext><mrow><mn>4</mn><mtext>s</mtext></mrow></msup><mo>=</mo><mo>-</mo><mn>1</mn></math> <math><mtext> </mtext><mo>&#8658;</mo><msup><mrow><mtext>&#969;</mtext></mrow><mrow><mn>4</mn><mtext>s</mtext></mrow></msup><mo>=</mo><mtext>&#969;</mtext><mo>=</mo><msup><mrow><mtext>&#969;</mtext></mrow><mrow><mn>4</mn></mrow></msup><mtext> </mtext></math>
<math><mo>&#8658;</mo></math> <math><mtext>s</mtext><mo>=</mo><mn>1</mn></math>
<math><mfenced separators="|"><mrow><mtext>r</mtext><mo>,</mo><mtext>&#160;</mtext><mtext>s</mtext></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mtext>&#160;</mtext><mn>1</mn></mrow></mfenced></math>
Only 1 pair

</details>

---

### Q9. JEE Advanced 2011 (Paper 2)

*Type:* `numerical` | *Level:* `1`

$$
\text { Let } M \text { be a } 3 \times 3 \text { matrix satisfying }
$$

$$
M\left[\begin{array}{l}
0 \\
1 \\
0
\end{array}\right]=\left[\begin{array}{c}
-1 \\
2 \\
3
\end{array}\right], M\left[\begin{array}{c}
1 \\
-1 \\
0
\end{array}\right]=\left[\begin{array}{c}
1 \\
1 \\
-1
\end{array}\right] \text { and } M\left[\begin{array}{l}
1 \\
1 \\
1
\end{array}\right]=\left[\begin{array}{c}
0 \\
0 \\
12
\end{array}\right]
$$
Then, the sum of the diagonal entries of $M$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

Let $M=\left[\begin{array}{lll}a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3\end{array}\right]$
$\therefore M\left[\begin{array}{l}0 \\ 1 \\ 0\end{array}\right]=\left[\begin{array}{r}-1 \\ 2 \\ 3\end{array}\right], M\left[\begin{array}{r}1 \\ -1 \\ 0\end{array}\right]=\left[\begin{array}{r}1 \\ 1 \\ -1\end{array}\right]$,
$M\left[\begin{array}{l}1 \\ 1 \\ 1\end{array}\right]=\left[\begin{array}{r}0 \\ 0 \\ 12\end{array}\right]$,
$$
\begin{aligned}
\Rightarrow & {\left[\begin{array}{l}
a_2 \\
b_2 \\
c_2
\end{array}\right]=\left[\begin{array}{r}
-1 \\
2 \\
3
\end{array}\right],\left[\begin{array}{l}
a_1-a_2 \\
b_1-b_2 \\
c_1-c_2
\end{array}\right]=\left[\begin{array}{r}
1 \\
1 \\
-1
\end{array}\right], } \\
& {\left[\begin{array}{l}
a_1+a_2+a_3 \\
b_1+b_2+b_3 \\
c_1+c_2+c_3
\end{array}\right]=\left[\begin{array}{r}
0 \\
0 \\
12
\end{array}\right] } \\
\Rightarrow & a_2=-1, b_2=2, c_2=3, a_1-a_2=1, \\
\Rightarrow & b_1-b_2=1, c_1-c_2=-1 \\
\Rightarrow \quad & a_1+a_2+a_3=0, b_1+b_2+b_3=0, \\
\therefore & c_1+c_2+c_3=12 \\
\therefore & a_1=0, b_2=2 \text { and } c_3=7
\end{aligned}
$$
Hence, sum of diagonal elements
$$
=0+2+7=9
$$

</details>

---

### Q10. JEE Advanced 2011 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

<strong>Paragraph:</strong>
Let $a$, b and $c$ be three real numbers satisfying $\left[\begin{array}{lll}a & b & c\end{array}\right]\left[\begin{array}{lll}1 & 9 & 7 \\ 8 & 2 & 7 \\ 7 & 3 & 7\end{array}\right]=\left[\begin{array}{lll}0 & 0 & 0\end{array}\right]$<strong>Question:</strong>
Let $b=6$, with $a$ and $c$ satisfying Eq. (E). If $\alpha$ and $\beta$ are the roots of the quadratic equation $a x^2+b x+c=0$, then $\sum_{n=0}^{\infty}\left(\frac{1}{\alpha}+\frac{1}{\beta}\right)^n$ is

**Options:**

- **(A)** 6
- **(B)** 7
- **(C)** $\frac{6}{7}$
- **(D)** $\infty$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 7**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Given, }[a b c]_{1 \times 3}\left[\begin{array}{lll}
1 & 9 & 7 \\
8 & 2 & 7 \\
7 & 3 & 7
\end{array}\right]_{3 \times 3}=\left[\begin{array}{lll}
0 & 0 & 0
\end{array}\right] \\
& \Rightarrow \quad\left[\begin{array}{c}
a+8 b+7 c \\
9 a+2 b+3 c \\
7 a+7 b+7 c
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\
0
\end{array}\right] \\
& \Rightarrow \quad a+8 b+7 c=0 \\
& \Rightarrow 9 a+2 b+3 c=0 \\
& \Rightarrow \quad a+b+c=0 \\
&
\end{aligned}
$$
On multiplying Eq. (iii) by 2 , then subtract from Eq. (ii), we get
$$
7 a+c=0
$$
Again multiplying Eq. (iii) by 3 , then subtract from Eq. (ii), we get
$$
\begin{array}{ll} 
& 6 a-b=0 \\
\therefore \quad & b=6 a \text { and } c=-7 a
\end{array}
$$
If $b=6, a=1$ and $c=-7$
$$
\begin{array}{ll}
\therefore & a x^2+b x+c=0 \\
\Rightarrow & x^2+6 x-7=0 \\
\Rightarrow & (x+7)(x-1)=0 \\
\therefore & x=1,-7 \\
\Rightarrow & \quad \sum_{n=0}^{\infty}\left(\frac{1}{1}-\frac{1}{7}\right)^n \Rightarrow \sum_{n=0}^{\infty}\left(\frac{6}{7}\right)^n \\
\Rightarrow & 1+\frac{6}{7}+\left(\frac{6}{7}\right)^n+\ldots \infty \\
& =\frac{1}{1-\frac{6}{7}}=\frac{1}{1 / 7}=7
\end{array}
$$

</details>

---

### Q11. JEE Advanced 2011 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

<strong>Paragraph:</strong>
Let $a$, b and $c$ be three real numbers satisfying $\left[\begin{array}{lll}a & b & c\end{array}\right]\left[\begin{array}{lll}1 & 9 & 7 \\ 8 & 2 & 7 \\ 7 & 3 & 7\end{array}\right]=\left[\begin{array}{lll}0 & 0 & 0\end{array}\right]$<strong>Question:</strong>
If the point $P(a, b, c)$, with reference to Eq. (E), lies on the plane $2 x+y+z=1$, then the value of $7 a+b+c$ is

**Options:**

- **(A)** 0
- **(B)** 12
- **(C)** 7
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 6**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Given, }[a b c]_{1 \times 3}\left[\begin{array}{lll}
1 & 9 & 7 \\
8 & 2 & 7 \\
7 & 3 & 7
\end{array}\right]_{3 \times 3}=\left[\begin{array}{lll}
0 & 0 & 0
\end{array}\right] \\
& \Rightarrow \quad\left[\begin{array}{c}
a+8 b+7 c \\
9 a+2 b+3 c \\
7 a+7 b+7 c
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\
0
\end{array}\right] \\
& \Rightarrow \quad a+8 b+7 c=0 \\
& \Rightarrow 9 a+2 b+3 c=0 \\
& \Rightarrow \quad a+b+c=0 \\
&
\end{aligned}
$$
On multiplying Eq. (iii) by 2 , then subtract from Eq. (ii), we get
$$
7 a+c=0
$$
Again multiplying Eq. (iii) by 3 , then subtract from Eq. (ii), we get
$$
\begin{array}{ll} 
& 6 a-b=0 \\
\therefore \quad & b=6 a \text { and } c=-7 a
\end{array}
$$
As $(a, b, c)$ lies on $2 x+y+z=1$
$$
\begin{array}{lc}
\Rightarrow & 2 a+b+c=1 \\
\Rightarrow & 2 a+6 a-7 a=1 \\
\Rightarrow & a=1, b=6 \text { and } c=-7 \\
\therefore & 7 a+b+c=7+6-7=6
\end{array}
$$

</details>

---

### Q12. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `1`

<strong>Paragraph:</strong>
Read the following passage and answer the questions.<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/88iLE50zA6etAHkOmNt74CAbkJliurfrRZp8CzupJk0.original.fullsize.png">
<strong>Question:</strong>
The value of $\left[\begin{array}{lll}3 & 2 & 0\end{array}\right]\left[\begin{array}{l}3 \\ 2 \\ 0\end{array}\right]$ is

**Options:**

- **(A)** $[5]$
- **(B)** $\left[\frac{5}{2}\right]$
- **(C)** [4]
- **(D)** $\left[\frac{3}{2}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $[5]$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ZQgvpskrRTIhBmqoFgX30lBrLbKluyTOLvJb7_-5kd4.original.fullsize.png">

</details>

---

### Q13. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Read the following passage and answer the questions.<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/88iLE50zA6etAHkOmNt74CAbkJliurfrRZp8CzupJk0.original.fullsize.png">
<strong>Question:</strong>
The value of $|U|$ is

**Options:**

- **(A)** 3
- **(B)** $-3$
- **(C)** $\frac{3}{2}$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/wgH9BbHmJlVwdCzbsjL7tQqY-vkRnukiLSB1oxMNbTc.original.fullsize.png">

</details>

---

