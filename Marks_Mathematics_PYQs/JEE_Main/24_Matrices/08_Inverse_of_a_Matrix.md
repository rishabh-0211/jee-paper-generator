# JEE Main Mathematics - Matrices

## Topic 8: Inverse of a Matrix

**Total Questions:** 26

---

### Q1. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $A=\begin{bmatrix} 1 & 2 & 7 \\ 4 & -2 & 8 \\ 3 & 8 & -7 \end{bmatrix}$ and $\det(A-\alpha I)=0$, where $\alpha$ is a real number. If the largest possible value of $\alpha$ is $p$, then the circle $(x-p)^2+(y-2p)^2=320$, intersects the co-ordinate axes at

**Options:**

- **(A)** $1$ point
- **(B)** $2$ points
- **(C)** $3$ points
- **(D)** $4$ points

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$ points**

**Detailed Solution:**

The characteristic equation is given by $\det(A-\alpha I) = 0$.

$\det \begin{bmatrix} 1-\alpha & 2 & 7 \\ 4 & -2-\alpha & 8 \\ 3 & 8 & -7-\alpha \end{bmatrix} = 0$

Expanding the determinant along the first row:

$(1-\alpha)[(-2-\alpha)(-7-\alpha) - 64] - 2[4(-7-\alpha) - 24] + 7[32 - 3(-2-\alpha)] = 0$

$(1-\alpha)(\alpha^2 + 9\alpha - 50) - 2(-4\alpha - 52) + 7(3\alpha + 38) = 0$

$-\alpha^3 - 8\alpha^2 + 59\alpha - 50 + 8\alpha + 104 + 21\alpha + 266 = 0$

$\alpha^3 + 8\alpha^2 - 88\alpha - 320 = 0$

By inspection, $\alpha = 8$ is a root since $8^3 + 8(8^2) - 88(8) - 320 = 512 + 512 - 704 - 320 = 0$.

Factoring out $(\alpha - 8)$, we get:

$(\alpha - 8)(\alpha^2 + 16\alpha + 40) = 0$

The roots are $\alpha = 8$ and $\alpha = \dfrac{-16 \pm \sqrt{256 - 160}}{2} = -8 \pm 2\sqrt{6}$.

The largest possible value of $\alpha$ is $p = 8$.

Substituting $p = 8$ into the given equation of the circle:

$(x-8)^2 + (y-16)^2 = 320$

To find the intersection points with the x-axis, substitute $y = 0$:

$(x-8)^2 + (-16)^2 = 320$

$(x-8)^2 + 256 = 320 \Rightarrow (x-8)^2 = 64 \Rightarrow x-8 = \pm 8$

$x = 0$ or $x = 16$

The circle intersects the x-axis at $(0, 0)$ and $(16, 0)$.

To find the intersection points with the y-axis, substitute $x = 0$:

$(-8)^2 + (y-16)^2 = 320$

$64 + (y-16)^2 = 320 \Rightarrow (y-16)^2 = 256 \Rightarrow y-16 = \pm 16$

$y = 0$ or $y = 32$

The circle intersects the y-axis at $(0, 0)$ and $(0, 32)$.

The distinct points of intersection with the coordinate axes are $(0, 0)$, $(16, 0)$, and $(0, 32)$.

Thus, the circle intersects the coordinate axes at exactly $3$ points.

Answer: $3$ points

</details>

---

### Q2. JEE Main 2026 (02 April Shift 2)

*Type:* `numerical` | *Level:* `2`

Consider the matrices $A = \begin{bmatrix} 2 & -2 \\ 4 & -2 \end{bmatrix}$ and $B = \begin{bmatrix} 3 & 9 \\ 1 & 3 \end{bmatrix}$. If matrices P and Q are such that $PA = B$ and $AQ = B$, then the absolute value of the sum of the diagonal elements of $2(P + Q)$ is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **34**

**Detailed Solution:**

Given $A = \begin{bmatrix} 2 & -2 \\ 4 & -2 \end{bmatrix}$, we find its determinant:

$|A| = (2)(-2) - (-2)(4) = 4$

Since $|A| \neq 0$, $A$ is invertible. The inverse of $A$ is:

$A^{-1} = \dfrac{1}{4} \begin{bmatrix} -2 & 2 \\ -4 & 2 \end{bmatrix} = \begin{bmatrix} -1/2 & 1/2 \\ -1 & 1/2 \end{bmatrix}$

We are given $PA = B \Rightarrow P = BA^{-1}$ and $AQ = B \Rightarrow Q = A^{-1}B$.

Using the cyclic property of trace $\text{Tr}(XY) = \text{Tr}(YX)$, we have:

$\text{Tr}(P) = \text{Tr}(BA^{-1}) = \text{Tr}(A^{-1}B) = \text{Tr}(Q)$

Let us calculate $\text{Tr}(P)$ by finding the diagonal elements of $P = BA^{-1}$:

$P = \begin{bmatrix} 3 & 9 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} -1/2 & 1/2 \\ -1 & 1/2 \end{bmatrix}$

The diagonal elements of $P$ are:

$P_{11} = 3\left(-\dfrac{1}{2}\right) + 9(-1) = -\dfrac{21}{2}$

$P_{22} = 1\left(\dfrac{1}{2}\right) + 3\left(\dfrac{1}{2}\right) = 2$

$\text{Tr}(P) = P_{11} + P_{22} = -\dfrac{21}{2} + 2 = -\dfrac{17}{2}$

Since $\text{Tr}(P) = \text{Tr}(Q) = -\dfrac{17}{2}$, the sum of the diagonal elements of $2(P + Q)$ is:

$\text{Tr}(2(P + Q)) = 2(\text{Tr}(P) + \text{Tr}(Q)) = 2\left(-\dfrac{17}{2} - \dfrac{17}{2}\right) = 2(-17) = -34$

The absolute value is $|-34| = 34$.

Answer: $34$

</details>

---

### Q3. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A = \begin{bmatrix} 1 & 2 \\ 1 & \alpha \end{bmatrix}$ and $B = \begin{bmatrix} 3 & 3 \\ \beta & 2 \end{bmatrix}$. If $A^2 - 4A + I = O$ and $B^2 - 5B - 6I = O$, then among the two statements :
(S1): $[(B-A)(B+A)]^T = \begin{bmatrix} 13 & 15 \\ 7 & 10 \end{bmatrix}$
and
(S2): $\det(\text{adj}(A+B)) = -5$,

**Options:**

- **(A)** only (S1) is correct
- **(B)** only (S2) is correct
- **(C)** both (S1) and (S2) are correct
- **(D)** both (S1) and (S2) are wrong

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) only (S2) is correct**

**Detailed Solution:**

For a $2 \times 2$ matrix $M$, the characteristic equation is given by $M^2 - \text{Tr}(M)M + \det(M)I = O$.

For matrix $A = \begin{bmatrix} 1 & 2 \\ 1 & \alpha \end{bmatrix}$, we are given $A^2 - 4A + I = O$.
Comparing the trace, we get $\text{Tr}(A) = 1 + \alpha = 4 \implies \alpha = 3$.
Thus, $A = \begin{bmatrix} 1 & 2 \\ 1 & 3 \end{bmatrix}$.

For matrix $B = \begin{bmatrix} 3 & 3 \\ \beta & 2 \end{bmatrix}$, we are given $B^2 - 5B - 6I = O$.
Comparing the determinant, we get $\det(B) = 6 - 3\beta = -6 \implies 3\beta = 12 \implies \beta = 4$.
Thus, $B = \begin{bmatrix} 3 & 3 \\ 4 & 2 \end{bmatrix}$.

Evaluating Statement (S1):
$B - A = \begin{bmatrix} 3 & 3 \\ 4 & 2 \end{bmatrix} - \begin{bmatrix} 1 & 2 \\ 1 & 3 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 3 & -1 \end{bmatrix}$

$B + A = \begin{bmatrix} 3 & 3 \\ 4 & 2 \end{bmatrix} + \begin{bmatrix} 1 & 2 \\ 1 & 3 \end{bmatrix} = \begin{bmatrix} 4 & 5 \\ 5 & 5 \end{bmatrix}$

$(B-A)(B+A) = \begin{bmatrix} 2 & 1 \\ 3 & -1 \end{bmatrix} \begin{bmatrix} 4 & 5 \\ 5 & 5 \end{bmatrix} = \begin{bmatrix} 2(4)+1(5) & 2(5)+1(5) \\ 3(4)-1(5) & 3(5)-1(5) \end{bmatrix} = \begin{bmatrix} 13 & 15 \\ 7 & 10 \end{bmatrix}$

$[(B-A)(B+A)]^T = \begin{bmatrix} 13 & 15 \\ 7 & 10 \end{bmatrix}^T = \begin{bmatrix} 13 & 7 \\ 15 & 10 \end{bmatrix}$
Since $\begin{bmatrix} 13 & 7 \\ 15 & 10 \end{bmatrix} \neq \begin{bmatrix} 13 & 15 \\ 7 & 10 \end{bmatrix}$, Statement (S1) is incorrect.

Evaluating Statement (S2):
For any $2 \times 2$ matrix $M$, $\det(\text{adj}(M)) = \det(M)^{2-1} = \det(M)$.

$\det(\text{adj}(A+B)) = \det(A+B)$

$\det(A+B) = \det \begin{bmatrix} 4 & 5 \\ 5 & 5 \end{bmatrix} = 4(5) - 5(5) = 20 - 25 = -5$

Thus, $\det(\text{adj}(A+B)) = -5$. Statement (S2) is correct.

Therefore, only (S2) is correct.

Answer: only (S2) is correct

</details>

---

### Q4. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A, B$ and $C$ be three $2 \times 2$ matrices with real entries such that $B=(I+A)^{-1}$ and $\mathrm{A}+\mathrm{C}=\mathrm{I}$. If $\mathrm{BC}=\left[\begin{array}{cc}1 & -5 \\ -1 & 2\end{array}\right]$ and $\mathrm{CB}\left[\begin{array}{l}x_{1} \\ x_{2}\end{array}\right]=\left[\begin{array}{c}12 \\ -6\end{array}\right]$, then $x_{1}+x_{2}$ is

**Options:**

- **(A)** 2
- **(B)** -2
- **(C)** 0
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

From $B = (I + A)^{-1}$ we get $B(I + A) = I$, so $BA = I - B$.
From $A + C = I$: $C = I - A$. 
 Calculating $CB = C(I+A)^{-1} = (I-A)(I+A)^{-1}$.
Since $B(I+A) = I$, we have $(I+A) = B^{-1}$, so $C = (I-A)B^{-1}$.
Multiplying by $B$: $CB = (I-A)$. 
 However, using the given $BC = \begin{bmatrix} 1 & -5 \\ -1 & 2 \end{bmatrix}$ and $B(I+A) = I$ implies $B - BA = B - (I-B) = 2B - I = BC$, i.e. $BC = 2B - I$. 
 Therefore $B = \frac{1}{2}(BC + I) = \frac{1}{2}\begin{bmatrix} 2 & -5 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} 1 & -5/2 \\ -1/2 & 3/2 \end{bmatrix}$. 
 Also $CB = 2B - I = \begin{bmatrix} 1 & -5 \\ -1 & 2 \end{bmatrix}$. 
 From $CB\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 12 \\ -6 \end{bmatrix}$: $(CB)^{-1} = -\frac{1}{3}\begin{bmatrix} 2 & 5 \\ 1 & 1 \end{bmatrix}$. 
 So $\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = -\frac{1}{3}\begin{bmatrix} -6 \\ 6 \end{bmatrix} = \begin{bmatrix} 2 \\ -2 \end{bmatrix}$. 
 Therefore $x_1 + x_2 = 0$

</details>

---

### Q5. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 3 & 5\end{array}\right]$, then the determinant of the matrix $\left(\mathrm{A}^{2025}-3 \mathrm{~A}^{2024}+\mathrm{A}^{2023}\right)$ is

**Options:**

- **(A)** 12
- **(B)** 28
- **(C)** 24
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 16**

**Detailed Solution:**

$A = \begin{bmatrix} 2 & 3 \\ 3 & 5 \end{bmatrix} \Rightarrow A^2 = \begin{bmatrix} 13 & 21 \\ 21 & 34 \end{bmatrix}$
$|A^{2025} - 3A^{2024} + A^{2023}|$
$= \left| A^{2023} \left( A^2 - 3A + I \right) \right|$
$= |A|^{2023} |A^2 - 3A + I|$
$= 1 \cdot \begin{vmatrix} 8 & 12 \\ 12 & 20 \end{vmatrix} = 160 - 144 = 16$

</details>

---

### Q6. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}, \mathrm{B}$, and $\left(\operatorname{adj}\left(\mathrm{A}^{-1}\right)+\operatorname{adj}\left(\mathrm{B}^{-1}\right)\right)$ are non-singular matrices of same order, then the inverse of $\mathrm{A}\left(\operatorname{adj}\left(\mathrm{A}^{-1}\right)+\operatorname{adj}\left(\mathrm{B}^{-1}\right)\right)^{-1} \mathrm{~B}$, is equal to

**Options:**

- **(A)** $\mathrm{AB}^{-1}+\mathrm{A}^{-1} \mathrm{~B}$
- **(B)** $\operatorname{adj}\left(\mathrm{B}^{-1}\right)+\operatorname{adj}\left(\mathrm{A}^{-1}\right)$
- **(C)** $\frac{A B^{-1}}{|A|}+\frac{B A^{-1}}{|B|}$
- **(D)** $\frac{1}{|A B|}(\operatorname{adj}(B)+\operatorname{adj}(A))$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{|A B|}(\operatorname{adj}(B)+\operatorname{adj}(A))$**

**Detailed Solution:**

$\begin{aligned} & {\left[\mathrm{A}\left(\operatorname{adj}\left(\mathrm{A}^{-1}\right)+\operatorname{adj}\left(\mathrm{B}^{-1}\right)\right)^{-1} \cdot \mathrm{~B}\right]^{-1}} \\ & \Rightarrow \mathrm{~B}^{-1} \cdot\left(\operatorname{adj}\left(\mathrm{~A}^{-1}\right)+\operatorname{adj}\left(\mathrm{B}^{-1}\right)\right) \cdot \mathrm{A}^{-1} \\ & \Rightarrow \mathrm{~B}^{-1} \operatorname{adj}\left(\mathrm{~A}^{-1}\right) \mathrm{A}^{-1}+\mathrm{B}^{-1}\left(\operatorname{adj}\left(\mathrm{~B}^{-1}\right)\right) \cdot \mathrm{A}^{-1} \\ & \Rightarrow \mathrm{~B}^{-1}\left|\mathrm{~A}^{-1}\right| \mathrm{I}+\left|\mathrm{B}^{-1}\right| \mathrm{IA}^{-1} \\ & \Rightarrow \frac{\mathrm{~B}^{-1}}{|\mathrm{~A}|}+\frac{\mathrm{A}^{-1}}{|\mathrm{~B}|} \\ & \Rightarrow \frac{\operatorname{adjB}}{|\mathrm{B}||\mathrm{A}|}+\frac{\operatorname{adj}}{|\mathrm{A}||\mathrm{B}|} \\ & =\frac{1}{|\mathrm{~A}||\mathrm{B}|}(\operatorname{adjB}+\operatorname{adj} \mathrm{A})\end{aligned}$

</details>

---

### Q7. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $B=\left[\begin{array}{ll}1 & 3 \\ 1 & 5\end{array}\right]$ and $A$ be a $2 \times 2$ matrix such that $A B^{-1}=A^{-1}$. If $B C B^{-1}=A$ and $C^4+\alpha C^2+\beta I=O$, then $2 \beta-\alpha$ is equal to

**Options:**

- **(A)** 16
- **(B)** 2
- **(C)** 8
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 10**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{BCB}^{-1}=\mathrm{A} \\
& \Rightarrow\left(\mathrm{BCB}^{-1}\right)\left(\mathrm{BCB}^{-1}\right)=\mathrm{A} \cdot \mathrm{A} \\
& \Rightarrow \mathrm{BCI} \mathrm{CB}^{-1}=\mathrm{A}^2 \\
& \Rightarrow \mathrm{BC}^2 \mathrm{~B}^{-1}=\mathrm{A}^2 \\
& \Rightarrow \mathrm{B}^{-1}\left(\mathrm{BC}^2 \mathrm{~B}^{-1}\right) \mathrm{B}=\mathrm{B}^{-1} \text { (A.A)B }
\end{aligned}$
From equation (1)
$\begin{aligned}
& \mathrm{C}^2=\mathrm{A}^{-1} \cdot \mathrm{A} \cdot \mathrm{B} \\
& \mathrm{C}^2=\mathrm{B}
\end{aligned}$
$\begin{aligned}
& \text { Also } \mathrm{AB}^{-1}=\mathrm{A}^{-1} \\
& \Rightarrow \mathrm{AB}^{-1} \cdot \mathrm{A}=\mathrm{A}^{-1} \mathrm{~A}=\mathrm{I} \\
& \Rightarrow \mathrm{A}^{-1}\left(\mathrm{AB}^{-1} \mathrm{~A}\right)=\mathrm{A}^{-1} \mathrm{I} \\
& \mathrm{B}^{-1} \mathrm{~A}=\mathrm{A}^{-1}
\end{aligned}$
Now characteristics equation of $\mathrm{C}^2$ is
$\begin{aligned}
& \left|C_2-\lambda I\right|=0 \\
& |B-\lambda I|=0
\end{aligned}$
$\begin{aligned} & \Rightarrow\left|\begin{array}{cc}1-\lambda & 3 \\ 1 & 5-\lambda\end{array}\right|=0 \\ & \Rightarrow(1-\lambda)(5-1)-3=0 \Rightarrow\left(\lambda^2-6 \lambda+5\right)-3=0 \\ & \Rightarrow \lambda^2-6 \lambda+2=0 \\ & \Rightarrow \beta^2-6 \mathrm{~B}+2 \mathrm{I}=0 \\ & \Rightarrow \mathrm{C}^4-6 \mathrm{C}^2+2 \mathrm{I}=0 \\ & \alpha=-6 \\ & \beta=2 \\ & \therefore 2 \beta-\alpha=4+6=10\end{aligned}$

</details>

---

### Q8. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>11</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>7</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced></math>. The sum of the prime factors of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi mathvariant="normal">P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>AP</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">I</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>66</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>23</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><msup><mi mathvariant="normal">P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>AP</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">I</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><msup><mi mathvariant="normal">P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>AP</mi><mo>-</mo><mn>2</mn><msup><mi mathvariant="normal">P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi mathvariant="normal">P</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mfenced><mrow><msup><mi mathvariant="normal">P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi mathvariant="normal">I</mi></mrow></mfenced><mo>(</mo><mo> </mo><mi mathvariant="normal">A</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>)</mo><mi mathvariant="normal">P</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><msup><mi mathvariant="normal">P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi mathvariant="normal">I</mi></mrow></mfenced><mo>|</mo><mi mathvariant="normal">A</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>|</mo><mo>|</mo><mi mathvariant="normal">P</mi><mo>|</mo></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi mathvariant="normal">A</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mfenced close="|" open="|"><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mo>|</mo><mi mathvariant="normal">A</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">I</mi><mo>|</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>11</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>-</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>11</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>0</mn><mo>-</mo><mfenced><mrow><mn>0</mn><mo>-</mo><mn>33</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>18</mn><mo>-</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>69</mn></math></p><p>Now, prime factor of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>69</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>23</mn></math>.</p><p>So, sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>26</mn></math></p>

</details>

---

### Q9. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>. Given below are two statements :
Statement I:<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mo>-</mo><mi>x</mi><mo>)</mo></math> is the inverse of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>.
Statement II: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo> </mo><mi>f</mi><mo>(</mo><mi>y</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>)</mo></math>.
In the light of the above statements, choose the correct answer from the options given below

**Options:**

- **(A)** Statement I is false but Statement II is true
- **(B)** Both Statement I and Statement II are false
- **(C)** Statement I is true but Statement II is false
- **(D)** Both Statement I and Statement II are true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Both Statement I and Statement II are true**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>×</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>×</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>×</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mi>f</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced></math></p><p>Hence statement-I is correct</p><p>Now, checking statement II</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>y</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mi>y</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>sin</mi><mi>y</mi></mtd><mtd><mi>cos</mi><mi>y</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>y</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mi>y</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>sin</mi><mi>y</mi></mtd><mtd><mi>cos</mi><mi>y</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>x</mi><mi>cos</mi><mi>y</mi><mo>-</mo><mi>sin</mi><mi>x</mi><mi>sin</mi><mi>y</mi></mtd><mtd><mo>-</mo><mi>cos</mi><mi>x</mi><mi>sin</mi><mi>y</mi><mo>-</mo><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>y</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>y</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mi>sin</mi><mi>y</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mi>x</mi><mi>sin</mi><mi>y</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mi>cos</mi><mi>y</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">y</mi><mo>)</mo></mtd><mtd><mo>-</mo><mi>sin</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">y</mi><mo>)</mo></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>sin</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">y</mi><mo>)</mo></mtd><mtd><mi>cos</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">y</mi><mo>)</mo></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>·</mo><mi>f</mi><mo>(</mo><mi>y</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>)</mo></math></p><p>Hence statement-II is also correct.</p>

</details>

---

### Q10. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mi>&#955;</mi></mtd><mtd><mn>10</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>&#945;</mi><mi>A</mi><mo>+</mo><mi>&#946;</mi><mi>I</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#955;</mi><mn>2</mn></msup></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mi>&#955;</mi></mtd><mtd><mn>10</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>&#945;</mi><mi>A</mi><mo>+</mo><mi>&#946;</mi><mi>I</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>,</p><p>Now solving by using characteristic equation, we get
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>A</mi><mo>-</mo><mi>k</mi><mo>|</mo><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn><mo>-</mo><mi>k</mi></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mi>&#955;</mi></mtd><mtd><mn>10</mn><mo>-</mo><mi>k</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>11</mn><mi>k</mi><mo>+</mo><mn>10</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mn>11</mn><mi>A</mi><mo>+</mo><mo>(</mo><mn>10</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi><mo>)</mo><mi>I</mi><mo>=</mo><mn>0</mn></math> {by putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mi>A</mi></math>}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mrow><mn>10</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi></mrow></mfrac><mo>(</mo><mo>-</mo><mi>A</mi><mo>+</mo><mn>11</mn><mi>I</mi><mo>)</mo></math></p><p>Now on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>&#945;</mi><mi>A</mi><mo>+</mo><mi>&#946;</mi><mi>I</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mn>10</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>11</mn><mrow><mn>10</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi></mrow></mfrac></math></p><p>And given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>11</mn></mrow><mn>5</mn></mfrac></math></p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>=</mo><mn>14</mn></math></p></blockquote>

</details>

---

### Q11. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>The set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>, for which the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><msup><mi mathvariant="normal">e</mi><mi>t</mi></msup></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced><mrow><mi>sin</mi><mi>t</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mi>t</mi></mrow></mfenced></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced><mrow><mo>-</mo><mn>2</mn><mi>sin</mi><mi>t</mi><mo>-</mo><mi>cos</mi><mi>t</mi></mrow></mfenced></mtd></mtr><mtr><mtd><msup><mi mathvariant="normal">e</mi><mi>t</mi></msup></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>t</mi><mo>+</mo><mi>cos</mi><mi>t</mi></mrow></mfenced></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced><mrow><mi>sin</mi><mi>t</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mi>t</mi></mrow></mfenced></mtd></mtr><mtr><mtd><msup><mi mathvariant="normal">e</mi><mi>t</mi></msup></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mi>cos</mi><mi>t</mi></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mi>sin</mi><mi>t</mi></mtd></mtr></mtable></mfenced></math> is invertible, is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced><mrow><mn>2</mn><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mi>k</mi><mo>&#8712;</mo><mi>&#8484;</mi></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>k</mi><mi>&#960;</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mi>k</mi><mo>&#8712;</mo><mi>&#8484;</mi></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>k</mi><mi>&#960;</mi><mo>,</mo><mi>k</mi><mo>&#8712;</mo><mi>&#8484;</mi></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8477;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8477;</mi></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><msup><mi mathvariant="normal">e</mi><mi>t</mi></msup></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced><mrow><mi>sin</mi><mi>t</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mi>t</mi></mrow></mfenced></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced><mrow><mo>-</mo><mn>2</mn><mi>sin</mi><mi>t</mi><mo>-</mo><mi>cos</mi><mi>t</mi></mrow></mfenced></mtd></mtr><mtr><mtd><msup><mi mathvariant="normal">e</mi><mi>t</mi></msup></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>t</mi><mo>+</mo><mi>cos</mi><mi>t</mi></mrow></mfenced></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced><mrow><mi>sin</mi><mi>t</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mi>t</mi></mrow></mfenced></mtd></mtr><mtr><mtd><msup><mi mathvariant="normal">e</mi><mi>t</mi></msup></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mi>cos</mi><mi>t</mi></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mi>sin</mi><mi>t</mi></mtd></mtr></mtable></mfenced></math></p><p>Given matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is invertible if</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mtable><mtr><mtd><msup><mi mathvariant="normal">e</mi><mi>t</mi></msup></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced><mrow><mi>sin</mi><mi>t</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mi>t</mi></mrow></mfenced></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced><mrow><mo>-</mo><mn>2</mn><mi>sin</mi><mi>t</mi><mo>-</mo><mi>cos</mi><mi>t</mi></mrow></mfenced></mtd></mtr><mtr><mtd><msup><mi mathvariant="normal">e</mi><mi>t</mi></msup></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>t</mi><mo>+</mo><mi>cos</mi><mi>t</mi></mrow></mfenced></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced><mrow><mi>sin</mi><mi>t</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mi>t</mi></mrow></mfenced></mtd></mtr><mtr><mtd><msup><mi mathvariant="normal">e</mi><mi>t</mi></msup></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mi>cos</mi><mi>t</mi></mtd><mtd><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mi>sin</mi><mi>t</mi></mtd></mtr></mtable></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>t</mi></msup><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>sin</mi><mi>t</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mi>t</mi></mtd><mtd><mo>-</mo><mn>2</mn><mi>sin</mi><mi>t</mi><mo>-</mo><mi>cos</mi><mi>t</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn><mi>sin</mi><mi>t</mi><mo>+</mo><mi>cos</mi><mi>t</mi></mtd><mtd><mi>sin</mi><mi>t</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mi>t</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>cos</mi><mi>t</mi></mtd><mtd><mi>sin</mi><mi>t</mi></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p>Applying <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">R</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi mathvariant="normal">R</mi><mn>1</mn></msub><mo>-</mo><msub><mi mathvariant="normal">R</mi><mn>2</mn></msub></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi mathvariant="normal">R</mi><mn>2</mn></msub><mo>-</mo><msub><mi mathvariant="normal">R</mi><mn>3</mn></msub></math>, ee get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced open="|" close="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mi>sin</mi><mi>t</mi><mo>-</mo><mn>3</mn><mi>cos</mi><mi>t</mi></mtd><mtd><mo>-</mo><mn>3</mn><mi>sin</mi><mi>t</mi><mo>+</mo><mi>cos</mi><mi>t</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn><mi>sin</mi><mi>t</mi></mtd><mtd><mo>-</mo><mn>2</mn><mi>cos</mi><mi>t</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>cos</mi><mi>t</mi></mtd><mtd><mi>sin</mi><mi>t</mi></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p>By expanding we have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mo>&#215;</mo><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>t</mi><mi>co</mi><mi>s</mi><mi>t</mi><mo>+</mo><mn>6</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>t</mi><mo>+</mo><mn>6</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi><mo>-</mo><mn>2</mn><mi>sin</mi><mi>t</mi><mi>cos</mi><mi>t</mi></mrow></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mo>&#215;</mo><mn>6</mn><mo>&#8800;</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8704;</mo><mi>t</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math></p>

</details>

---

### Q12. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mi>&#947;</mi><mi>A</mi><mo>+</mo><mn>18</mn><mi>I</mi><mo>=</mo><mi>O</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>det</mo><mfenced><mi>A</mi></mfenced></math> is equal to _______.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>18</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>50</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>&#8658;</mo><mi>det</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mn>4</mn><mi>&#946;</mi><mo>+</mo><mn>2</mn><mi>&#945;</mi></math></p><p>Characteristic equation of the matrix is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mn>4</mn><mo>-</mo><mi>&#955;</mi></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi><mo>-</mo><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>&#946;</mi><mo>+</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mi>&#955;</mi><mo>+</mo><mn>2</mn><mi>&#945;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mi>&#955;</mi><mo>+</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>4</mn><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p>Comparing with given equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mi>&#947;</mi><mi>A</mi><mo>+</mo><mn>18</mn><mi>I</mi><mo>=</mo><mn>0</mn></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>4</mn><mi>&#946;</mi><mo>=</mo><mn>18</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>det</mo><mfenced><mi>A</mi></mfenced><mo>=</mo><mn>4</mn><mi>&#946;</mi><mo>+</mo><mn>2</mn><mi>&#945;</mi><mo>=</mo><mn>18</mn></math></p></blockquote>

</details>

---

### Q13. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr></mtable></mfenced></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mi>&#946;</mi><mi>A</mi><mo>=</mo><mn>2</mn><mi>I</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>**

**Detailed Solution:**

<blockquote><p>We know that characteristic equation of matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is given by, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>A</mi><mo>-</mo><mi>&#955;</mi><mi>I</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn><mo>-</mo><mi>&#955;</mi></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>5</mn><mo>-</mo><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>&#955;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>A</mi><mo>=</mo><mi>I</mi></math></p><p>Multiplying by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>A</mi><mo>=</mo><mn>2</mn><mi>I</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mi>&#946;</mi><mi>A</mi><mo>=</mo><mn>2</mn><mi>I</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now on Comparing equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>10</mn></math></p></blockquote>

</details>

---

### Q14. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be two <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> real matrices such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>B</mi><mn>2</mn></msup></mrow></mfenced></math> is invertible matrix. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>5</mn></msup><mo>=</mo><msup><mi>B</mi><mn>5</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><msup><mrow><mo>&#160;</mo><mi>B</mi></mrow><mn>2</mn></msup><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi>B</mi></mrow><mn>3</mn></msup><mo>,</mo></math> then the value of the determinant of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mo>+</mo><msup><mi>B</mi><mn>3</mn></msup></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>B</mi><mn>2</mn></msup><mo>;</mo><mfenced close="|" open="|"><mi>C</mi></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>5</mn></msup><mo>=</mo><msup><mi>B</mi><mn>5</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><msup><mrow><mo>&#160;</mo><mi>B</mi></mrow><mn>2</mn></msup><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi>B</mi></mrow><mn>3</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Subtracting equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>5</mn></msup><mo>-</mo><msup><mi>A</mi><mn>3</mn></msup><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><msup><mi>B</mi><mn>5</mn></msup><mo>-</mo><msup><mi>A</mi><mn>2</mn></msup><msup><mi>B</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mfenced><mrow><msup><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>2</mn></msup><mo>-</mo><msup><mi>B</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><msup><mi>B</mi><mn>3</mn></msup><mfenced><mrow><msup><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>2</mn></msup><mo>-</mo><msup><mi>B</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mi>O</mi></math></p><p>Post multiplying inverse of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>B</mi><mn>2</mn></msup><mo>:</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mo>+</mo><msup><mi>B</mi><mn>3</mn></msup><mo>=</mo><mi>O</mi><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><msup><mi>A</mi><mn>3</mn></msup><mo>+</mo><msup><mi>B</mi><mn>3</mn></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q15. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>.</mo></math>  If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>&#945;</mi><mi>I</mi><mo>+</mo><mi>&#946;</mi><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mo>&#160;</mo><mi>I</mi></math> is a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn></math> identity matrix, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>&#8658;</mo><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mn>6</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mrow><mo>adj</mo><mi>A</mi></mrow><mfenced open="|" close="|"><mi>A</mi></mfenced></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced open="[" close="]"><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mfrac><mn>2</mn><mn>3</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>6</mn></mfrac></mtd><mtd><mfrac><mn>1</mn><mn>6</mn></mfrac></mtd></mtr></mtable></mfenced></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mfrac><mn>2</mn><mn>3</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>6</mn></mfrac></mtd><mtd><mfrac><mn>1</mn><mn>6</mn></mfrac></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mo>+</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>2</mn><mi>&#946;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>&#946;</mi></mtd><mtd><mn>4</mn><mi>&#946;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="" close="}"><mtable columnalign="left"><mtr><mtd><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mtd></mtr><mtr><mtd><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></mtd></mtr></mtable></mfenced><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>4</mn><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q16. JEE Main 2021 (16 Mar Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>30</mn></mtd><mtd><mn>20</mn></mtd><mtd><mn>56</mn></mtd></mtr><mtr><mtd><mn>90</mn></mtd><mtd><mn>140</mn></mtd><mtd><mn>112</mn></mtd></mtr><mtr><mtd><mn>120</mn></mtd><mtd><mn>60</mn></mtd><mtd><mn>14</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>7</mn></mtd><mtd><msup><mi>&#969;</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mi>&#969;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mi>&#969;</mi></mtd><mtd><mo>-</mo><mi>&#969;</mi><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>3</mn></msub></math> be the identity matrix of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>. If the determinant of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>A</mi><mi>P</mi><mo>-</mo><msub><mi>I</mi><mn>3</mn></msub></mrow></mfenced><mn>2</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><msup><mi>&#969;</mi><mn>2</mn></msup></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to _________.<gwmw style="display:none;"></gwmw>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><msup><mfenced><mrow><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>A</mi><mi>P</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>A</mi><mi>P</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>A</mi><mi>P</mi><mo>+</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>A</mi><mn>2</mn></msup><mi>P</mi><mo>-</mo><mn>2</mn><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>A</mi><mi>P</mi><mo>+</mo><mi>I</mi><mfenced><mrow><mo>&#8757;</mo><msup><mfenced><mrow><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>A</mi><mi>P</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfenced><mrow><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>A</mi><mi>P</mi></mrow></mfenced><mfenced><mrow><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>A</mi><mi>P</mi></mrow></mfenced></mrow></mfenced></math></p><p>Multiplying with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> on both sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mi>M</mi><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mi>P</mi><mo>-</mo><mn>2</mn><mi>A</mi><mi>P</mi><mo>+</mo><mi>P</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>A</mi><mo>.</mo><mi>I</mi><mo>+</mo><msup><mi>I</mi><mn>2</mn></msup></mrow></mfenced><mi>P</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>Det</mo><mfenced><mrow><mi>P</mi><mi>M</mi></mrow></mfenced><mo>=</mo><mo>Det</mo><mfenced><mrow><msup><mfenced><mrow><mi>A</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mn>2</mn></msup><mo>&#215;</mo><mi>P</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>Det</mo><mfenced><mrow><mi>P</mi><mi>M</mi></mrow></mfenced><mo>=</mo><mo>Det</mo><msup><mfenced><mrow><mi>A</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mn>2</mn></msup><mo>&#215;</mo><mo>Det</mo><mfenced><mi>P</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Det</mi><mo>&#160;</mo><mi>M</mi><mo>=</mo><msup><mfenced><mrow><mi>Det</mi><mfenced><mrow><mi>A</mi><mo>-</mo><mi>I</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>-</mo><mi>I</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>7</mn></mtd><mtd><msup><mi>w</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mi>w</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mi>w</mi></mtd><mtd><mo>-</mo><mi>w</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Det</mo><mfenced><mrow><mi>A</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><msup><mi>w</mi><mn>2</mn></msup><mo>+</mo><mi>w</mi><mo>+</mo><mi>w</mi></mrow></mfenced><mo>+</mo><mn>7</mn><mfenced><mrow><mo>-</mo><mi>w</mi></mrow></mfenced><mo>+</mo><msup><mi>w</mi><mn>3</mn></msup><mo>=</mo><mo>-</mo><mn>6</mn><mi>w</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Det</mo><msup><mfenced><mfenced><mrow><mi>A</mi><mo>-</mo><mi>I</mi></mrow></mfenced></mfenced><mn>2</mn></msup><mo>=</mo><mn>36</mn><msup><mi>w</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>36</mn></math></p>

</details>

---

### Q17. JEE Main 2021 (25 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mi>tan</mi><mfenced><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mfenced></mtd></mtr><mtr><mtd><mi>tan</mi><mfenced><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mfenced></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><mi>A</mi></mrow></mfenced><msup><mfenced><mrow><msub><mi>I</mi><mn>2</mn></msub><mo>-</mo><mi>A</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mo>-</mo><mi>b</mi></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mi>a</mi></mtd></mtr></mtable></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **13**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>+</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>-</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#160;&#160;</mo><mfenced close="}" open="{"><mrow><mo>&#8756;</mo><mo>&#160;</mo><mo>|</mo><mi>I</mi><mo>-</mo><mi>A</mi><mo>|</mo><mo>=</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi><mo>/</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>I</mi><mo>-</mo><mi>A</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mrow><msup><mi>sec</mi><mn>2</mn></msup><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow></mfrac><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>I</mi><mo>+</mo><mi>A</mi></mrow></mfenced><msup><mfenced><mrow><mi>I</mi><mo>-</mo><mi>A</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mrow><msup><mi>sec</mi><mn>2</mn></msup><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow></mfrac><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd><mtd><mo>&#160;</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#160;&#160;</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd><mtd><mo>&#160;</mo><mo>&#160;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mrow><msup><mi>sec</mi><mn>2</mn></msup><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow></mfrac><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mn>2</mn><mo>&#160;</mo><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd><mtd><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow><mrow><msup><mi>sec</mi><mn>2</mn></msup><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#160;</mo><mi>tan</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow><mrow><msup><mi>sec</mi><mn>2</mn></msup><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>13</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>13</mn></math></p>

</details>

---

### Q18. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced separators="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfenced separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo></math> then <math><mn>10</mn><mtext>&#8201;</mtext><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, is equal to.

**Options:**

- **(A)** <math><mi>A</mi><mo>-</mo><mn>4</mn><mi>I</mi></math>
- **(B)** <math><mn>6</mn><mi>I</mi><mo>-</mo><mi>A</mi></math>
- **(C)** <math><mi>A</mi><mo>-</mo><mn>6</mn><mi>I</mi></math>
- **(D)** <math><mn>4</mn><mi>I</mi><mo>-</mo><mi>A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>A</mi><mo>-</mo><mn>6</mn><mi>I</mi></math>**

**Detailed Solution:**

<p>Characteristics equation of matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>-</mo><mi>x</mi><mi>I</mi><mo>=</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>-</mo><mi>x</mi><mfenced separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|" separators="|"><mrow><mtable><mtr><mtd><mn>2</mn><mo>-</mo><mi>x</mi></mtd></mtr><mtr><mtd><mn>9</mn></mtd></mtr></mtable><mtable><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>4</mn><mo>-</mo><mi>x</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>10</mn><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8756;</mo><mi mathvariant="normal"></mi><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>6</mn><mi>A</mi><mo>-</mo><mn>10</mn><mi>I</mi><mo>=</mo><mn>0</mn></math>
<math><mn>10</mn><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>A</mi><mo>-</mo><mn>6</mn><mi>I</mi></math>.</p>

</details>

---

### Q19. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>B</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd><mtd><mn>2</mn><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> is the inverse of a <math><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matix <math><mi>A</mi><mo>,</mo></math> then the sum of all values of <math><mi>&#945;</mi></math> for which  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>e</mi><mi>t</mi><mfenced separators="|"><mi>A</mi></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>,</mo></math> is:

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** <math><mn>0</mn></math>
- **(D)** <math><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>1</mn></math>**

**Detailed Solution:**

<p>Since, <math><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math>
Hence, <math><mfenced close="|" open="|" separators="|"><mrow><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mo>|</mo><mi>A</mi><mo>|</mo></mrow></mfrac><mo>=</mo><mo>-</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mi>B</mi></mfenced><mo>=</mo><mn>5</mn><mfenced separators="|"><mrow><mo>-</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi>&#945;</mi><mfenced separators="|"><mrow><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mi>&#945;</mi></math>
           <math><mo>=</mo><mn>2</mn><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>25</mn></math></p><p><math><mn>1</mn><mo>+</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>12</mn><mo>=</mo><mn>0</mn></math>
Sum <math><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q20. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#8230;</mo><mo>.</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>n</mi><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>78</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo></math> then the inverse of <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>n</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> is:

**Options:**

- **(A)** <math><mfenced open="[" close="]" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>–</mo><mn>12</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(B)** <math><mfenced open="[" close="]" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>12</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(C)** <math><mfenced open="[" close="]" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>13</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math><mfenced open="[" close="]" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>–</mo><mn>13</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced open="[" close="]" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>–</mo><mn>13</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>n</mi><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>78</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>And, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn><mo>+</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>n</mi><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>n</mi><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>n</mi><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>78</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Using the sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> natural numbers i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mo>=</mo><mn>78</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi><mo>-</mo><mn>156</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>13</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>12</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>13</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mo>-</mo><mn>12</mn></math> (reject as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is a natural number)
<math><mo>&#8756;</mo></math> We have to find inverse of <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>13</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math></p><p>Which can be find by using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow><mfenced close="|" open="|"><mi>A</mi></mfenced></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>13</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mn>0</mn><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>11</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>A</mi><mn>12</mn></msub><mo>=</mo><mo>-</mo><mn>13</mn><mo>,</mo><mo>&#160;</mo><msub><mi>A</mi><mn>21</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>A</mi><mn>22</mn></msub><mo>=</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>13</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>13</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>.</mo></math></p>

</details>

---

### Q21. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup></mtd><mtd><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>t</mi></mrow></msup><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">&#160;</mi><mi>t</mi></mtd><mtd><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>t</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#160;</mi></mrow></mrow><mi>t</mi></mtd></mtr><mtr><mtd><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup></mtd><mtd><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>t</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi></mrow></mrow><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>t</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi></mrow></mrow></mtd><mtd><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>t</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi></mrow></mrow><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>t</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi></mrow></mrow></mtd></mtr><mtr><mtd><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup></mtd><mtd><msup><mrow><mn>2</mn><mi>e</mi></mrow><mrow><mo>-</mo><mi>t</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi></mrow></mrow></mtd><mtd><mo>-</mo><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>t</mi></mrow></msup><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>t</mi></mrow></mrow></mtd></mtr></mtable></mrow></mfenced><mo>,</mo></math> then <math><mi>A</mi></math> is:

**Options:**

- **(A)** Invertible only if  <math><mi>t</mi><mo>=</mo><mi>π</mi></math>
- **(B)** Not invertible for any  <math><mi>t</mi><mo>∈</mo><mi>R</mi></math>
- **(C)** Invertible only if  <math><mi>t</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** Invertible for all  <math><mi>t</mi><mo>∈</mo><mi>R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Invertible for all  <math><mi>t</mi><mo>∈</mo><mi>R</mi></math>**

**Detailed Solution:**

Since given matrix <math><mi>A</mi></math> is invertible <math><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>&#8800;</mo><mn>0</mn></math>
 <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>cos</mi><mo>&#160;</mo><mi>t</mi></mtd><mtd><mi>sin</mi><mo>&#160;</mo><mi>t</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>cos</mi><mo>&#160;</mo><mi>t</mi><mo>-</mo><mi>sin</mi><mo>&#160;</mo><mi>t</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mo>&#160;</mo><mi>t</mi><mo>+</mo><mi>cos</mi><mo>&#160;</mo><mi>t</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>t</mi></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>cos</mi><mo>&#160;</mo><mi>t</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>-</mo><msub><mi>R</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>-</mo><msub><mi>R</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>cos</mi><mo>&#160;</mo><mi>t</mi></mtd><mtd><mi>sin</mi><mo>&#160;</mo><mi>t</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>cos</mi><mo>&#160;</mo><mi>t</mi><mo>-</mo><mi>sin</mi><mo>&#160;</mo><mi>t</mi></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>t</mi><mo>+</mo><mi>cos</mi><mo>&#160;</mo><mi>t</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>t</mi><mo>-</mo><mi>cos</mi><mo>&#160;</mo><mi>t</mi></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>cos</mi><mo>&#160;</mo><mi>t</mi><mo>-</mo><mi>sin</mi><mo>&#160;</mo><mi>t</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mfenced open="{" close="}"><mrow><msup><mfenced><mrow><mn>2</mn><mi>cos</mi><mi>t</mi><mo>+</mo><mi>sin</mi><mi>t</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>t</mi><mo>-</mo><mi>cos</mi><mi>t</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup></math></p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mi>A</mi></mfenced><mo>=</mo><mn>5</mn><mi>&#160;</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mo>&#8800;</mo><mn>0</mn><mi>&#160;</mi><mo>&#8704;</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">t</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math>

Hence, given matrix is always invertible.

</details>

---

### Q22. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#952;</mi></mtd><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi></mtd></mtr><mtr><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#952;</mi></mtd></mtr></mtable></mrow></mfenced></math> , then the matrix <math><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>50</mn></mrow></msup></math> when <math><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>12</mn></mrow></mfrac><mo>,</mo></math> is equal to:

**Options:**

- **(A)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr></mtable></mrow></mfenced></math>
- **(B)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr></mtable></mrow></mfenced></math>
- **(C)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr><mtr><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr><mtr><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr></mtable></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr></mtable></mrow></mfenced></math>**

**Detailed Solution:**

<math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mtd></mtr><mtr><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd></mtr></mtable></mrow></mfenced><mo>⇒</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mtd></mtr><mtr><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi><mo>=</mo><mn>1</mn></math> 

        And  <math><mi>a</mi><mi>d</mi><mi>j</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd></mtr></mtable></mrow></mfenced></math> 

         <math><mo>⇒</mo><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced></mrow></mfrac><mi>a</mi><mi>d</mi><mi>j</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd></mtr></mtable></mrow></mfenced></math> 

         <math><mo>⇒</mo><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>     

         <math><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd></mtr></mtable></mrow></mfenced><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd></mtr></mtable></mrow></mfenced></math> 

         <math><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi><mo>-</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></mtd><mtd><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi></mtd><mtd><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>θ</mi></mtd></mtr></mtable></mrow></mfenced></math> 

         <math><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>θ</mi></mtd><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>θ</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>θ</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>θ</mi></mtd></mtr></mtable></mrow></mfenced></math> 

        It is visible that

         <math><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>n</mi><mi>θ</mi></mtd><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>n</mi><mi>θ</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>n</mi><mi>θ</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>n</mi><mi>θ</mi></mtd></mtr></mtable></mrow></mfenced></math> 

         <math><mo>⇒</mo><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>50</mn></mrow></msup><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>50</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>50</mn><mi>θ</mi></mtd><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>50</mn><mi>θ</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>50</mn><mi>θ</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>50</mn><mi>θ</mi></mtd></mtr></mtable></mrow></mfenced></math> 

        Now at  <math><mi>θ</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>12</mn></mrow></mfrac><mo>,</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>50</mn><mi>θ</mi><mo>=</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mn>50</mn><mi>π</mi></mrow><mrow><mn>12</mn></mrow></mfrac><mo>=</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> 

         <math><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>50</mn><mi>θ</mi><mo>=</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfrac><mrow><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math> 

         <math><mo>⇒</mo><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>50</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr><mtr><mtd><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr></mtable></mrow></mfenced></math>

</details>

---

### Q23. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let A be a $3 \times 3$ matrix such that
$$
\mathrm{A}\left[\begin{array}{lll}
1 & 2 & 3 \\
0 & 2 & 3 \\
0 & 1 & 1
\end{array}\right]=\left[\begin{array}{lll}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{array}\right]
$$
Then $\mathrm{A}^{-1}$ is:

**Options:**

- **(A)** $\left[\begin{array}{lll}3 & 1 & 2 \\ 3 & 0 & 2 \\ 1 & 0 & 1\end{array}\right]$
- **(B)** $\left[\begin{array}{lll}3 & 2 & 1 \\ 3 & 2 & 0 \\ 1 & 1 & 0\end{array}\right]$
- **(C)** $\left[\begin{array}{lll}0 & 1 & 3 \\ 0 & 2 & 3 \\ 1 & 1 & 1\end{array}\right]$
- **(D)** $\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 2 & 3\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\begin{array}{lll}3 & 1 & 2 \\ 3 & 0 & 2 \\ 1 & 0 & 1\end{array}\right]$**

**Detailed Solution:**

$$
\text { Given } A\left[\begin{array}{lll}
1 & 2 & 3 \\
0 & 2 & 3 \\
0 & 1 & 1
\end{array}\right]=\left[\begin{array}{lll}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{array}\right]
$$

Applying $\mathrm{C}_1 \leftrightarrow \mathrm{C}_3$
$$
\mathrm{A}\left[\begin{array}{lll}
3 & 2 & 1 \\
3 & 2 & 0 \\
1 & 1 & 0
\end{array}\right]=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 0 & 1 \\
0 & 1 & 0
\end{array}\right]
$$
Again Applying $\mathrm{C}_2 \leftrightarrow \mathrm{C}_3$
$$
\text { A }\left[\begin{array}{lll}
3 & 1 & 2 \\
3 & 0 & 2 \\
1 & 0 & 1
\end{array}\right]=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]
$$
pre-multiplying both sides by $\mathrm{A}^{-1}$
$$
\begin{aligned}
&\mathrm{A}^{-1} \mathrm{~A}\left[\begin{array}{lll}
3 & 1 & 2 \\
3 & 0 & 2 \\
1 & 0 & 1
\end{array}\right]=\mathrm{A}^{-1}\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
&\mathrm{I}\left[\begin{array}{lll}
3 & 1 & 2 \\
3 & 0 & 2 \\
1 & 0 & 1
\end{array}\right]=\mathrm{A}^{-1} \mathrm{I}=\mathrm{A}^{-1} \\
&\left(\because \mathrm{A}^{-1} \mathrm{~A}=\mathrm{I} \text { and } \mathrm{I}=\text { Identity matrix }\right)
\end{aligned}
$$

$$
\text { Hence, } A^{-1}=\left[\begin{array}{lll}
3 & 1 & 2 \\
3 & 0 & 2 \\
1 & 0 & 1
\end{array}\right]
$$

</details>

---

### Q24. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Let $A$ and $B$ be real matrices of the form $\left[\begin{array}{ll}\alpha & 0 \\ 0 & \beta\end{array}\right]$ and $\left[\begin{array}{ll}0 & \gamma \\ \delta & 0\end{array}\right]$, respectively.
Statement 1: $A B-B A$ is always an invertible matrix.
Statement $2: A B-B A$ is never an identity matrix.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is false.
- **(B)** Statement 1 is false, Statement 2 is true.
- **(C)** Statement 1 is true, Statement 2 is true; Statement 2 is a correct explanation of Statement 1 .
- **(D)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation of Statement 1.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement 1 is true, Statement 2 is false.**

**Detailed Solution:**

Let $A$ and $B$ be real matrices such that $A=\left[\begin{array}{ll}\alpha & 0 \\ 0 & \beta\end{array}\right]$ and $B=\left[\begin{array}{ll}0 & \gamma \\ \delta & 0\end{array}\right]$ Now, $A B=\left[\begin{array}{cc}0 & \alpha \gamma \\ \beta \delta & 0\end{array}\right]$ and $B A=\left[\begin{array}{cc}0 & \gamma \beta \\ \delta \alpha & 0\end{array}\right]$ Statement-1:
$$
\begin{aligned}
& \left.A B-B A=\left[\begin{array}{cc}
0 & \gamma(\alpha-\beta \\
\delta(\beta-\alpha) & 0
\end{array}\right]\right) \\
& |A B-B A|=\left(\alpha-\beta^2\right\rangle \delta \neq 0
\end{aligned}
$$
$\therefore A B-B A$ is always an invertible matrix. Hence, statement $-1$ is true. But $A B-B A$ can be identity matrix if $\gamma=-\delta$ or $\delta=-\gamma$ So, statement $-2$ is false.

</details>

---

### Q25. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathbf{A}$ be a square matrix all of whose entries are integers. Then which one of the following is true?

**Options:**

- **(A)** If $\operatorname{det} A=\pm 1$, then $A^{-1}$ exists but all its entries are not necessarily integers
- **(B)** If $\operatorname{det} A \neq \pm 1$, then $A^{-1}$ exists and all its entries are non-integers
- **(C)** If $\operatorname{det} A=\pm 1$, then $A^{-1}$ exists and all its entries are integers
- **(D)** If $\operatorname{det} A=\pm 1$, then $A^{-1}$ need not exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) If $\operatorname{det} A=\pm 1$, then $A^{-1}$ exists and all its entries are integers**

**Detailed Solution:**

Each entry of $A$ is integer, so the cofactor of every entry is an integer and hence each entry in the adjoint of matrix $A$ is integer.
Now $\operatorname{det} A=\pm 1$ and $A^{-1}=\frac{1}{\operatorname{det}(A)}(\operatorname{adj} A)$
$\Rightarrow$ all entries in $\mathrm{A}^{-1}$ are integers.

</details>

---

### Q26. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\left(\begin{array}{ccc}1 & -1 & 1 \\ 2 & 1 & -3 \\ 1 & 1 & 1\end{array}\right)(10) B=\left(\begin{array}{ccc}4 & 2 & 2 \\ -5 & 0 & \alpha \\ 1 & -2 & 3\end{array}\right)$. If $B$

**Options:**

- **(A)** $-2$
- **(B)** 5
- **(C)** 2
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5**

**Detailed Solution:**

$A B=I \Rightarrow A(10 B)=10 \mathrm{I}$
$\Rightarrow\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & 1 & -3 \\ 1 & 1 & 1\end{array}\right]\left[\begin{array}{ccc}4 & 2 & 2 \\ -5 & 0 & \alpha \\ 1 & -2 & 3\end{array}\right]=\left[\begin{array}{ccc}10 & 0 & 5-\alpha \\ 0 & 10 & \alpha-5 \\ 0 & 0 & 5+\alpha\end{array}\right]=10\left[\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]$ if $\alpha=5$.

</details>

---

