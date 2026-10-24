# MHT CET Mathematics - Determinants

## Topic 3: System of Linear Equations

**Total Questions:** 12

---

### Q1. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the planes $ax = y + z$, $by = z + x$, $cz = x + y$ pass through a common line, then the value of $(a + b + c - abc) = \cdots$

**Options:**

- **(A)** $-2$
- **(B)** $-1$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-2$**

**Detailed Solution:**

The given equations of the planes can be rewritten as:

$ax - y - z = 0$
$-x + by - z = 0$
$-x - y + cz = 0$

Since the planes pass through a common line, the system of homogeneous equations has infinitely many solutions. Thus, the determinant of the coefficient matrix must be zero.

$\Delta = \begin{vmatrix} a & -1 & -1 \\ -1 & b & -1 \\ -1 & -1 & c \end{vmatrix} = 0$

Expanding the determinant along the first row:

$a(bc - 1) - (-1)(-c - 1) + (-1)(1 + b) = 0$

$abc - a - c - 1 - 1 - b = 0$

$abc - a - b - c - 2 = 0$

$a + b + c - abc = -2$

Answer: $-2$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\begin{bmatrix} 1 & 1 & 1 \\ 2 & -1 & 7 \\ 3 & 1 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 1 \\ 7 \\ 2 \end{bmatrix}$ then $\begin{bmatrix} x \\ y \\ z \end{bmatrix} =$

**Options:**

- **(A)** $\begin{bmatrix} 0 \\ -1 \\ 0 \end{bmatrix}$
- **(B)** $\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$
- **(C)** $\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$
- **(D)** $\begin{bmatrix} 0 \\ 1 \\ 2 \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$**

**Detailed Solution:**

The given matrix equation can be written as $x C_1 + y C_2 + z C_3 = B$, where $C_1, C_2, C_3$ are the columns of the coefficient matrix and $B$ is the constant matrix.

Substituting the given matrices:

$x \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + y \begin{bmatrix} 1 \\ -1 \\ 1 \end{bmatrix} + z \begin{bmatrix} 1 \\ 7 \\ 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 7 \\ 2 \end{bmatrix}$

Notice that the constant matrix on the right side is identical to the third column of the coefficient matrix.

Comparing both sides, we get $x = 0$, $y = 0$, and $z = 1$.

Thus, $\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$.

Answer: $\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$

</details>

---

### Q3. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A^T = \begin{bmatrix} 1 & 1 & 2 \\ 1 & -1 & 1 \\ 1 & 2 & -1 \end{bmatrix}$, $B^T = \begin{bmatrix} 6 & 5 & 1 \end{bmatrix}$ and $X = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$. If $AX = B$, then the values of $x, y, z$ are..........

**Options:**

- **(A)** $x = 2, y = 1, z = 3$
- **(B)** $x = 3, y = 2, z = 1$
- **(C)** $x = 1, y = 2, z = 3$
- **(D)** $x = 2, y = 3, z = 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x = 1, y = 2, z = 3$**

**Detailed Solution:**

Given $A^T = \begin{bmatrix} 1 & 1 & 2 \\ 1 & -1 & 1 \\ 1 & 2 & -1 \end{bmatrix}$, we have $A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & -1 & 2 \\ 2 & 1 & -1 \end{bmatrix}$.

Given $B^T = \begin{bmatrix} 6 & 5 & 1 \end{bmatrix}$, we have $B = \begin{bmatrix} 6 \\ 5 \\ 1 \end{bmatrix}$.

The equation $AX = B$ can be written as:

$\begin{bmatrix} 1 & 1 & 1 \\ 1 & -1 & 2 \\ 2 & 1 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 6 \\ 5 \\ 1 \end{bmatrix}$

This gives the system of equations:

$x + y + z = 6$

$x - y + 2z = 5$

$2x + y - z = 1$

Adding the first two equations gives:

$2x + 3z = 11$

Adding the second and third equations gives:

$3x + z = 6 \Rightarrow z = 6 - 3x$

Substituting $z$ into $2x + 3z = 11$ gives:

$2x + 3(6 - 3x) = 11$

$2x + 18 - 9x = 11$

$-7x = -7 \Rightarrow x = 1$

Substituting $x = 1$ into $z = 6 - 3x$ gives:

$z = 6 - 3(1) = 3$

Substituting $x = 1$ and $z = 3$ into $x + y + z = 6$ gives:

$1 + y + 3 = 6 \Rightarrow y = 2$

Thus, $x = 1, y = 2, z = 3$.

Answer: $x = 1, y = 2, z = 3$

</details>

---

### Q4. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\begin{bmatrix} 2 & 1 & -1 \\ -1 & 2 & 1 \\ 1 & -1 & 2 \end{bmatrix} \begin{bmatrix} a \\ b \\ c \end{bmatrix} = \begin{bmatrix} 4 \\ 0 \\ -2 \end{bmatrix}$ then the distance of point $P(a, b, c)$ from the plane $2x + y + 2z = 10$ is

**Options:**

- **(A)** $2$ units.
- **(B)** $3$ units.
- **(C)** $4$ units.
- **(D)** $5$ units.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3$ units.**

**Detailed Solution:**

The given matrix equation represents the following system of linear equations:

$2a + b - c = 4$

$-a + 2b + c = 0$

$a - b + 2c = -2$

Adding the first and second equations gives $a + 3b = 4$.

Adding the second and third equations gives $b + 3c = -2$.

Adding the first and third equations gives $3a + c = 2$.

Solving these equations, we get $a = 1$, $b = 1$, and $c = -1$.

The point $P(a, b, c)$ is $P(1, 1, -1)$.

The perpendicular distance of the point $P(1, 1, -1)$ from the plane $2x + y + 2z - 10 = 0$ is given by:

$d = \dfrac{|2(1) + 1(1) + 2(-1) - 10|}{\sqrt{2^2 + 1^2 + 2^2}}$

$d = \dfrac{|2 + 1 - 2 - 10|}{\sqrt{4 + 1 + 4}}$

$d = \dfrac{|-9|}{3} = 3$ units.

Answer: $3$ units.

</details>

---

### Q5. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\left[\begin{array}{lll}1 & 3 & 3 \\ 1 & 4 & 4 \\ 1 & 3 & 4\end{array}\right]\left[\begin{array}{l}x \\ y \\ z\end{array}\right]=\left[\begin{array}{l}12 \\ 15 \\ 13\end{array}\right]$, then the value of $x^2+y^2+z^2=$

**Options:**

- **(A)** $6$
- **(B)** $12$
- **(C)** $3$
- **(D)** $14$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $14$**

**Detailed Solution:**

The given matrix equation corresponds to the system of linear equations:

$x + 3y + 3z = 12$

$x + 4y + 4z = 15$

$x + 3y + 4z = 13$

Subtracting the first equation from the second equation:

$y + z = 3$

Subtracting the first equation from the third equation:

$z = 1$

Substituting $z = 1$ into $y + z = 3$:

$y + 1 = 3 \Rightarrow y = 2$

Substituting $y = 2$ and $z = 1$ into the first equation:

$x + 3(2) + 3(1) = 12 \Rightarrow x + 9 = 12 \Rightarrow x = 3$

The value of $x^2 + y^2 + z^2$ is:

$x^2 + y^2 + z^2 = 3^2 + 2^2 + 1^2 = 9 + 4 + 1 = 14$

Answer: $14$

</details>

---

### Q6. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & 1 & -3 \\ 1 & 1 & 1\end{array}\right]$ and $B=\left[\begin{array}{l}4 \\ 0 \\ 2\end{array}\right]$ such that $\mathrm{AX}=\mathrm{B}$, then $\mathrm{X}=$

**Options:**

- **(A)** $\left[\begin{array}{c}-1 \\ 2 \\ 1\end{array}\right]$
- **(B)** $\left[\begin{array}{c}2 \\ -1 \\ 1\end{array}\right]$
- **(C)** $\left[\begin{array}{c}-1 \\ 1 \\ 2\end{array}\right]$
- **(D)** $\left[\begin{array}{c}-2 \\ 1 \\ -1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[\begin{array}{c}2 \\ -1 \\ 1\end{array}\right]$**

**Detailed Solution:**

The given matrix equation $AX = B$ can be written as a system of linear equations:

$x - y + z = 4$

$2x + y - 3z = 0$

$x + y + z = 2$

Subtracting the third equation from the first equation gives:

$-2y = 2 \Rightarrow y = -1$

Substituting $y = -1$ into the first and second equations:

$x - (-1) + z = 4 \Rightarrow x + z = 3$

$2x + (-1) - 3z = 0 \Rightarrow 2x - 3z = 1$

Multiplying $x + z = 3$ by $3$ and adding to $2x - 3z = 1$ gives:

$3x + 3z + 2x - 3z = 9 + 1$

$5x = 10 \Rightarrow x = 2$

Substituting $x = 2$ into $x + z = 3$ gives:

$2 + z = 3 \Rightarrow z = 1$

Thus, $X = \begin{bmatrix} 2 \\ -1 \\ 1 \end{bmatrix}$.

Answer: $\left[\begin{array}{c}2 \\ -1 \\ 1\end{array}\right]$

</details>

---

### Q7. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $X=\left[\begin{array}{l}\mathrm{a} \\ \mathrm{b} \\ \mathrm{c}\end{array}\right], \mathrm{A}=\left[\begin{array}{ccc}1 & -1 & 2 \\ 2 & 0 & 1 \\ 3 & 2 & 1\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{l}3 \\ 1 \\ 4\end{array}\right]$.
If $A X=B$, then the value of $2 a-3 b+4 c$ will be

**Options:**

- **(A)** 0
- **(B)** -4
- **(C)** 6
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

Given the matrix equation $AX = B$, we can write the system of linear equations as:

$a - b + 2c = 3$  ... (1)

$2a + c = 1$  ... (2)

$3a + 2b + c = 4$  ... (3)

From equation (2), we get $c = 1 - 2a$.

Substituting $c = 1 - 2a$ into equation (1):

$a - b + 2(1 - 2a) = 3$

$a - b + 2 - 4a = 3$

$-3a - b = 1 \Rightarrow b = -3a - 1$

Substituting $b = -3a - 1$ and $c = 1 - 2a$ into equation (3):

$3a + 2(-3a - 1) + (1 - 2a) = 4$

$3a - 6a - 2 + 1 - 2a = 4$

$-5a - 1 = 4$

$-5a = 5 \Rightarrow a = -1$

Now, substituting $a = -1$ back to find $b$ and $c$:

$b = -3(-1) - 1 = 3 - 1 = 2$

$c = 1 - 2(-1) = 1 + 2 = 3$

We need to find the value of $2a - 3b + 4c$:

$2a - 3b + 4c = 2(-1) - 3(2) + 4(3)$

$= -2 - 6 + 12$

$= 4$

Answer: 4

</details>

---

### Q8. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The sum of three numbers is 6 . Thrice the third number when added to the first number given 7 . On adding three time first number to the sum of second and third number we get 12 . The product of these numbers is

**Options:**

- **(A)** $20$
- **(B)** $3$
- **(C)** $\frac{20}{3}$
- **(D)** $\frac{5}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{20}{3}$**

**Detailed Solution:**

Let the numbers be $x, y, z$
$$
\begin{aligned}
& x+y+z=6   ..(1)\\
& x+3 z==7 ..(2)\\
& 3 x+y+z=12..(3) \\
& \text { Eq. (3)-(1), gives } \\
& 2 x=6 \Rightarrow x=3
\end{aligned}
$$
$$
2 \mathrm{x}=6 \Rightarrow \mathrm{x}=3
$$
From eq. (2), we get
$$
3+3 z+7 \Rightarrow z=\frac{4}{3}
$$
From eq. (1), we get
$$
\begin{aligned}
& 3+y+\frac{4}{3}=6 \quad \Rightarrow \quad y=\frac{5}{3} \\
& \therefore x y z=(3)\left(\frac{5}{3}\right)\left(\frac{4}{3}\right)=\frac{20}{3}
\end{aligned}
$$

</details>

---

### Q9. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A X=B$, where $A=\left[\begin{array}{lll}1 & 3 & 3 \\ 1 & 4 & 4 \\ 1 & 3 & 4\end{array}\right], X=\left[\begin{array}{l}x \\ y \\ z\end{array}\right]$ and $B=\left[\begin{array}{l}12 \\ 15 \\ 13\end{array}\right]$, then $x^{2}+y^{2}+z^{2}=$

**Options:**

- **(A)** 14
- **(B)** 19
- **(C)** 21
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 14**

**Detailed Solution:**

(A)
Given $\mathrm{AX}=\mathrm{B}$
$\left[\begin{array}{lll}
1 & 3 & 3 \\
1 & 4 & 4 \\
1 & 3 & 4
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{c}
12 \\
15 \\
13
\end{array}\right]$
$\mathrm{R}_{2} \rightarrow \mathrm{R}_{2}-\mathrm{R}_{1}$ and $\mathrm{R}_{3} \rightarrow \mathrm{R}_{3}-\mathrm{R}_{1}$
$\left[\begin{array}{lll}1 & 3 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1\end{array}\right]\left[\begin{array}{l}x \\ y \\ z\end{array}\right]=\left[\begin{array}{l}12 \\ 3 \\ 1\end{array}\right] \Rightarrow\left[\begin{array}{l}x+3 y+3 z \\ y+z \\ z\end{array}\right]=\left[\begin{array}{l}12 \\ 3 \\ 1\end{array}\right]$
$\begin{aligned}
\therefore & x+3 y+3 z=12 \\
& y+z=3 \\
& z=1
\end{aligned}$
Thus $z=1, y=2, x=3$
$\therefore x^{2}+y^{2}+z^{2}=9+4+1=14$

</details>

---

### Q10. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{AX}=\mathrm{B}$, where $\mathrm{A}=\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & -1 & 0 \\ 3 & 3 & -4\end{array}\right], \mathrm{B}=\left[\begin{array}{l}1 \\ 1 \\ 2\end{array}\right]$ and $\mathrm{X}=\left[\begin{array}{l}x \\ y \\ z\end{array}\right]$, then $x+y+z=$

**Options:**

- **(A)** $2$
- **(B)** $3$
- **(C)** $6$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3$**

**Detailed Solution:**

Given $A=\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & -1 & 0 \\ 3 & 3 & -4\end{array}\right]$ and $B=\left[\begin{array}{l}1 \\ 1 \\ 2\end{array}\right], X=\left[\begin{array}{l}x \\ y \\ z\end{array}\right]$ and $A X=B$ $\therefore \mathrm{AA}^{-1} \mathrm{X}=\mathrm{A}^{-1} \mathrm{~B} \Rightarrow \mathrm{IX}=\mathrm{A}^{-1} \mathrm{~B} \Rightarrow \mathrm{X}=\mathrm{A}^{-1} \mathrm{~B}$
Now $|\mathrm{A}|=4+(-8)+9=5$
$$
\begin{aligned}
\therefore A^{-1} &=\left[\begin{array}{lll}
4 & -1 & 1 \\
8 & -7 & 2 \\
9 & -6 & 1
\end{array}\right] \times \frac{1}{5} \\
\therefore\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] &=\frac{1}{5}\left[\begin{array}{ccc}
4 & -1 & 1 \\
8 & -7 & 2 \\
9 & -6 & 1
\end{array}\right]\left[\begin{array}{l}
1 \\
1 \\
2
\end{array}\right] \\
&=\frac{1}{5}\left[\begin{array}{ll}
8-1+2 \\
8-7+4 \\
9-6+2
\end{array}\right]=\frac{1}{5}\left[\begin{array}{l}
5 \\
5 \\
5
\end{array}\right] \\
y &=\left[\begin{array}{l}
1 \\
1 \\
1
\end{array}\right]
\end{aligned}
$$
On comparing both side, we get
$$
x=y=z=1 \Rightarrow x+y+z=1+1+1=3
$$

</details>

---

### Q11. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

The value of ${ }^{\prime} a$ for which the system of equations
$$
\begin{array}{r}
a^{3} x+(a+1)^{3} y+(a+2)^{3} z=0 \\
a x+(a+1) y+(a+2) z=0 \\
x+y+z=0
\end{array}
$$
has a non-zero solution is

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** $-1$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-1$**

**Detailed Solution:**

For non-zero solution,
$$
\left|\begin{array}{ccc}
a^{3} & (a+1)^{3} & (a+2)^{3} \\
a & (a+1) & (a+2) \\
1 & 1 & 1
\end{array}\right|=0
$$
$$
\left.\begin{array}{l}
\Rightarrow \quad-\left|\begin{array}{ccc}
1 & 1 & 1 \\
a & (a+1) & (a+2) \\
a^{3} & (a+1)^{3} & (a+2)^{3}
\end{array}\right|=0 \\
\Rightarrow & -(a-a-1)(a+1-a-2)(a+2-a) \\
& \quad \quad \times(a+a+1+a+2)=0 \\
\Rightarrow & -2(3 a+3)=0 \\
\Rightarrow & \quad a=-1 \\
& {\left[\begin{array}{ccc}
1 & 1 & 1 \\
x & y & z \\
x^{3} & y^{3} & z^{3}
\end{array} \mid=\right.} \\
(x-y)(y-z)(z-x)(x+y+z)
\end{array}\right]
$$

</details>

---

### Q12. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

For the equations
$$
x+2 y+3 z=1,2 x+y+3 z=2
$$
and $5 x+5 y+9 z=4$

**Options:**

- **(A)** there is only one solution
- **(B)** there exists infinitely many solution
- **(C)** there is no solution
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) there is only one solution**

**Detailed Solution:**

\Delta &=\left|\begin{array}{lll}
1 & 2 & 3 \\
2 & 1 & 3 \\
5 & 5 & 9
\end{array}\right| \\
&=1(9-15)-2(18-15)+3(10-5) \\
&=-6-6+15=3 \neq 0
\end{aligned}
$$
Hence, the system of equations has a unique solution.

</details>

---

