# JEE Main Mathematics - Determinants

## Topic 4: System of Linear Equations

**Total Questions:** 137

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the system of linear equations:
$x+y+z=6$,
$x+2y+5z=10$,
$2x+3y+\lambda z=\mu$
has infinitely many solutions, then the value of $\lambda+\mu$ equals:

**Options:**

- **(A)** $12$
- **(B)** $16$
- **(C)** $22$
- **(D)** $28$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $22$**

**Detailed Solution:**

For the system of linear equations to have infinitely many solutions, the determinant of the coefficient matrix $\Delta$ must be zero, and $\Delta_x = \Delta_y = \Delta_z = 0$.

$\Delta = \begin{vmatrix} 1 & 1 & 1 \\ 1 & 2 & 5 \\ 2 & 3 & \lambda \end{vmatrix} = 0$

Expanding the determinant:

$1(2\lambda - 15) - 1(\lambda - 10) + 1(3 - 4) = 0$

$\lambda - 6 = 0 \Rightarrow \lambda = 6$

Now, setting $\Delta_z = 0$:

$\Delta_z = \begin{vmatrix} 1 & 1 & 6 \\ 1 & 2 & 10 \\ 2 & 3 & \mu \end{vmatrix} = 0$

Expanding the determinant:

$1(2\mu - 30) - 1(\mu - 20) + 6(3 - 4) = 0$

$\mu - 16 = 0 \Rightarrow \mu = 16$

Therefore, $\lambda + \mu = 6 + 16 = 22$.

Answer: $22$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The sum of all possible values of $\theta \in [0, 2\pi]$, for which the system of equations :
$x\cos 3\theta - 8y - 12z = 0$
$x\cos 2\theta + 3y + 3z = 0$
$x + y + 3z = 0$
has a non-trivial solution, is equal to :

**Options:**

- **(A)** $\pi$
- **(B)** $2\pi$
- **(C)** $3\pi$
- **(D)** $4\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4\pi$**

**Detailed Solution:**

For the given system of homogeneous linear equations to have a non-trivial solution, the determinant of the coefficient matrix must be zero.

$\begin{vmatrix} \cos 3\theta & -8 & -12 \\ \cos 2\theta & 3 & 3 \\ 1 & 1 & 3 \end{vmatrix} = 0$

Expanding the determinant along the first row:

$\cos 3\theta (9 - 3) - (-8)(3\cos 2\theta - 3) + (-12)(\cos 2\theta - 3) = 0$

$6\cos 3\theta + 24\cos 2\theta - 24 - 12\cos 2\theta + 36 = 0$

$6\cos 3\theta + 12\cos 2\theta + 12 = 0$

Dividing by $6$, we get:

$\cos 3\theta + 2\cos 2\theta + 2 = 0$

Using the multiple angle formulas $\cos 3\theta = 4\cos^3 \theta - 3\cos \theta$ and $\cos 2\theta = 2\cos^2 \theta - 1$, we substitute these into the equation:

$(4\cos^3 \theta - 3\cos \theta) + 2(2\cos^2 \theta - 1) + 2 = 0$

$4\cos^3 \theta + 4\cos^2 \theta - 3\cos \theta = 0$

$\cos \theta (4\cos^2 \theta + 4\cos \theta - 3) = 0$

$\cos \theta (2\cos \theta - 1)(2\cos \theta + 3) = 0$

This gives the possible values for $\cos \theta$:

$\cos \theta = 0 \implies \theta = \dfrac{\pi}{2}, \dfrac{3\pi}{2}$

$\cos \theta = \dfrac{1}{2} \implies \theta = \dfrac{\pi}{3}, \dfrac{5\pi}{3}$

$\cos \theta = -\dfrac{3}{2}$ (Not possible since $\cos \theta \in [-1, 1]$)

The possible values of $\theta \in [0, 2\pi]$ are $\dfrac{\pi}{2}, \dfrac{3\pi}{2}, \dfrac{\pi}{3}, \dfrac{5\pi}{3}$.

Sum of all possible values of $\theta$:

$\sum \theta = \left(\dfrac{\pi}{2} + \dfrac{3\pi}{2}\right) + \left(\dfrac{\pi}{3} + \dfrac{5\pi}{3}\right) = 2\pi + 2\pi = 4\pi$

Answer: $4\pi$

</details>

---

### Q3. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider the system of linear equations in $x, y, z$:
$x + 2y + tz = 0$,
$6x + y + 5tz = 0$,
$3x + t^2 y + f(t) z = 0$,
where $f: \mathbb{R} \rightarrow \mathbb{R}$ is a differentiable function. If this system has infinitely many solutions for all $t \in \mathbb{R}$, then $f$

**Options:**

- **(A)** is a constant function
- **(B)** is strictly increasing on $\mathbb{R}$
- **(C)** is strictly decreasing on $\mathbb{R}$
- **(D)** has two critical points

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) is strictly increasing on $\mathbb{R}$**

**Detailed Solution:**

For a homogeneous system of linear equations to have infinitely many solutions, the determinant of its coefficient matrix must be zero.

The coefficient matrix is:
$\Delta = \begin{vmatrix} 1 & 2 & t \\ 6 & 1 & 5t \\ 3 & t^2 & f(t) \end{vmatrix}$

Expanding the determinant along the first row, we get:
$\Delta = 1(1 \cdot f(t) - 5t \cdot t^2) - 2(6 \cdot f(t) - 3 \cdot 5t) + t(6 \cdot t^2 - 3 \cdot 1)$

$\Delta = f(t) - 5t^3 - 12f(t) + 30t + 6t^3 - 3t$

$\Delta = -11f(t) + t^3 + 27t$

Since the system has infinitely many solutions for all $t \in \mathbb{R}$, we must have $\Delta = 0$ for all $t \in \mathbb{R}$.

$-11f(t) + t^3 + 27t = 0$

$f(t) = \dfrac{t^3 + 27t}{11}$

To determine the nature of the function $f(t)$, we find its derivative with respect to $t$:

$f'(t) = \dfrac{3t^2 + 27}{11}$

Since $t^2 \ge 0$ for all $t \in \mathbb{R}$, we have $3t^2 + 27 \ge 27 > 0$.

Therefore, $f'(t) > 0$ for all $t \in \mathbb{R}$, which implies that $f(t)$ is a strictly increasing function on $\mathbb{R}$.

Answer: is strictly increasing on $\mathbb{R}$

</details>

---

### Q4. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the system of equations:
$x+y+z=5$
$x+2y+3z=9$
$x+3y+\lambda z=\mu$
has infinitely many solutions, then the value of $\lambda+\mu$ is:

**Options:**

- **(A)** $16$
- **(B)** $18$
- **(C)** $19$
- **(D)** $21$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $18$**

**Detailed Solution:**

For the system to have infinitely many solutions, $\Delta = 0$ and $\Delta_x = \Delta_y = \Delta_z = 0$.

$\Delta = \begin{vmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & 3 & \lambda \end{vmatrix} = 1(2\lambda - 9) - 1(\lambda - 3) + 1(3 - 2)$

$\Delta = 2\lambda - 9 - \lambda + 3 + 1 = \lambda - 5$

Setting $\Delta = 0$ gives $\lambda = 5$.

Now, calculating $\Delta_z$:

$\Delta_z = \begin{vmatrix} 1 & 1 & 5 \\ 1 & 2 & 9 \\ 1 & 3 & \mu \end{vmatrix} = 1(2\mu - 27) - 1(\mu - 9) + 5(3 - 2)$

$\Delta_z = 2\mu - 27 - \mu + 9 + 5 = \mu - 13$

Setting $\Delta_z = 0$ gives $\mu = 13$.

For $\lambda = 5$ and $\mu = 13$, we can verify that $\Delta_x = 0$ and $\Delta_y = 0$ as well.

Therefore, $\lambda + \mu = 5 + 13 = 18$.

Answer: $18$

</details>

---

### Q5. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the system of equations
$x + 5y + 6z = 4$,
$2x + 3y + 4z = 7$,
$x + 6y + az = b$
has infinitely many solutions, then the point $(a, b)$ lies on the line

**Options:**

- **(A)** $y - x = 3$
- **(B)** $x - y = 3$
- **(C)** $x + y = 11$
- **(D)** $x + y = 12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x - y = 3$**

**Detailed Solution:**

For the given system of equations to have infinitely many solutions, the determinant of the coefficient matrix must be zero, $\Delta = 0$.

$\Delta = \begin{vmatrix} 1 & 5 & 6 \\ 2 & 3 & 4 \\ 1 & 6 & a \end{vmatrix} = 0$

Expanding along the first row:

$1(3a - 24) - 5(2a - 4) + 6(12 - 3) = 0$

$3a - 24 - 10a + 20 + 54 = 0$

$-7a + 50 = 0 \Rightarrow a = \dfrac{50}{7}$

For infinitely many solutions, we must also have $\Delta_z = 0$.

$\Delta_z = \begin{vmatrix} 1 & 5 & 4 \\ 2 & 3 & 7 \\ 1 & 6 & b \end{vmatrix} = 0$

Expanding along the first row:

$1(3b - 42) - 5(2b - 7) + 4(12 - 3) = 0$

$3b - 42 - 10b + 35 + 36 = 0$

$-7b + 29 = 0 \Rightarrow b = \dfrac{29}{7}$

The point $(a, b)$ is $\left(\dfrac{50}{7}, \dfrac{29}{7}\right)$.

Checking the given options, we evaluate $a - b$:

$a - b = \dfrac{50}{7} - \dfrac{29}{7} = \dfrac{21}{7} = 3$

Therefore, the point $(a, b)$ lies on the line $x - y = 3$.

Answer: $x - y = 3$

</details>

---

### Q6. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha, \beta \in \mathbb{R}$ be such that the system of linear equations
$x + 2y + z = 5$
$2x + y + \alpha z = 5$
$8x + 4y + \beta z = 18$
has no solution. Then $\dfrac{\beta}{\alpha}$ is equal to :

**Options:**

- **(A)** $-4$
- **(B)** $4$
- **(C)** $8$
- **(D)** $-8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4$**

**Detailed Solution:**

The given system of linear equations is:
$x + 2y + z = 5$
$2x + y + \alpha z = 5$
$8x + 4y + \beta z = 18$

For the system to have no solution, the determinant of the coefficient matrix $D$ must be zero.

$D = \begin{vmatrix} 1 & 2 & 1 \\ 2 & 1 & \alpha \\ 8 & 4 & \beta \end{vmatrix} = 0$

Expanding along the first row:

$1(\beta - 4\alpha) - 2(2\beta - 8\alpha) + 1(8 - 8) = 0$

$\beta - 4\alpha - 4\beta + 16\alpha = 0$

$12\alpha - 3\beta = 0$

$\beta = 4\alpha$

To verify the no solution condition, substitute $\beta = 4\alpha$ into the third equation:

$8x + 4y + 4\alpha z = 18$

$4(2x + y + \alpha z) = 18$

$2x + y + \alpha z = \dfrac{9}{2}$

However, the second equation is $2x + y + \alpha z = 5$. This results in a contradiction since $\dfrac{9}{2} \neq 5$. Thus, the system has no solution when $\beta = 4\alpha$.

Therefore, $\dfrac{\beta}{\alpha} = 4$.

Answer: $4$

</details>

---

### Q7. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The system of linear equations 
 $x+y+z=6$ 
 $2 x+5 y+a z=36$ 
 $x+2 y+3 z=b$ 
 has

**Options:**

- **(A)** unique solution for $a=8$ and $b=16$
- **(B)** infinitely many solutions for $a=8$ and $b=16$
- **(C)** unique solution for $a=8$ and $b=14$
- **(D)** infinitely many solutions for $a=8$ and $b=14$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) infinitely many solutions for $a=8$ and $b=14$**

**Detailed Solution:**

Coefficient matrix determinant: $\Delta = 1(15-2a) - 1(6-a) + 1(4-5) = 8 - a$.
For $a = 8$, $\Delta = 0$, so unique solution is not possible.
With $a = 8$: $R_2 - 2R_1$ gives $3y + 6z = 24 \Rightarrow y + 2z = 8$.
$R_3 - R_1$ gives $y + 2z = b - 6$.
For consistency: $b - 6 = 8 \Rightarrow b = 14$.
When $a = 8, b = 14$: the system has infinitely many solutions.

</details>

---

### Q8. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let n be the number obtained on rolling a fair die. If the probability that the system 
 $x-\mathrm{n} y+z=6$ 
 $x+(\mathrm{n}-2) y+(\mathrm{n}+1) z=8$ 
 $(\mathrm{n}-1) y+z=1$ has a unique solution is $\frac{k}{6}$, 
 then the sum of $k$ and all possible values of $n$ is :

**Options:**

- **(A)** 20
- **(B)** 24
- **(C)** 21
- **(D)** 22

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 22**

**Detailed Solution:**

The coefficient matrix has determinant $\det(A) = -(n-1)(n-2)$.
The system has a unique solution when $\det(A) \neq 0$, which requires $n \neq 1$ and $n \neq 2$.
For a fair die, $n \in \{1,2,3,4,5,6\}$, so the unique solution occurs for $n \in \{3,4,5,6\}$.
The probability is $\frac{4}{6} = \frac{2}{3}$, giving $k = 4$.
The sum of $k$ and all possible values of $n$ where unique solution exists is $4 + (3+4+5+6) = 22$.

</details>

---

### Q9. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the system of equations 
 $3 x+y+4 z=3$ 
 $2 x+\alpha y-z=-3$ 
 $x+2 y+z=4$ 
 has no solution, then the value of $\alpha$ is equal to :

**Options:**

- **(A)** $19$
- **(B)** 4
- **(C)** 13
- **(D)** 23

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $19$**

**Detailed Solution:**

For no solution $\Delta = 0$
$\begin{vmatrix} 3 & 1 & 4 \\ 2 & \alpha & -1 \\ 1 & 2 & 1 \end{vmatrix} = 0$
$\Rightarrow 3(\alpha + 2) + 1(-1 - 2) + 4(4 - \alpha) = 0$
$\Rightarrow 19 - \alpha = 0 \Rightarrow \boxed{\alpha = 19}$
& for $\alpha = 19$
$\Delta_x = \begin{vmatrix} 3 & 1 & 4 \\ -3 & 19 & -1 \\ 4 & 2 & 1 \end{vmatrix} = 3(21) + 1(-1) + 4(-82)$
$\neq 0$
$\therefore$ no solution for $\alpha = 19$

</details>

---

### Q10. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the system of equations
$\begin{aligned}
& x+5 y-z=1 \\
& 4 x+3 y-3 z=7 \\
& 24 x+y+\lambda z=\mu
\end{aligned}$
$\lambda, \mu \in \mathrm{R}$, have infinitely many solutions. Then the number of the solutions of this system, If $x, y, z$ are integers and satisfy $7 \leq x+y+z \leq 77$, is

**Options:**

- **(A)** 3
- **(B)** 6
- **(C)** 5
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

For infinitely many solution
$\begin{aligned}
& \Delta=0 \\
& \left|\begin{array}{ccc}
1 & 5 & -1 \\
4 & 3 & -3 \\
24 & 1 & \lambda
\end{array}\right|=0 \\
& \Rightarrow 1(3 \lambda+3)-5(4 \lambda+72)-1(4-72)=0 \\
& \Rightarrow-17 \lambda+3-4 \times 72-4=0 \\
& \Rightarrow 17 \lambda=-289
\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7-c_hdCFQvu16JfOLyNS-8i1dWhF0E2oA9S0bgQBZIs.original.fullsize.png"/>
$\begin{aligned} & \Delta 1=0 \\ & \Rightarrow\left|\begin{array}{ccc}1 & 5 & -1 \\ 7 & 3 & -3 \\ \mu & 1 & -17\end{array}\right|=0 \\ & \Rightarrow 1(-51+3)-5(-119+3 \mu)-1(7-3 \mu)=0 \\ & \Rightarrow-48+595-15 \mu-7+3 \mu=0 \\ & \Rightarrow 12 \mu=540\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/mNf-6EoELq135XhILyjgdf08phxmjlyXuMxrneTFevo.original.fullsize.png"/>
$\begin{aligned} & x+5 y-z=1 \\ & 4 x+3 y-3 z=7 \\ & 24 x+y-17 z=45 \\ & \text { Let } z=1 \\ & x+5 y=1+\lambda] \times 4 \\ & 4 x+3 y=7+3 \lambda \\ & 4 x+20 y=4+4 \lambda \\ & \frac{-17 y=3-\lambda}{-17}\end{aligned}$
$\begin{aligned} & \begin{aligned} \mathrm{y} & =\frac{\lambda-3}{17}, \mathrm{x}=1+\lambda-\frac{5 \lambda-15}{17} \\ & =\frac{32-12 \lambda}{17} \\ 7 & \leq \frac{\lambda-3}{17}+\frac{32+12 \lambda}{17}+\lambda \leq 77 \\ 7 & \leq \frac{30 \lambda+29}{17} \leq 77 \\ 3 & \leq \lambda \leq 42 \\ \lambda & =3,20,37\end{aligned}\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the system of equations :
$\begin{aligned}
& 2 x+3 y+5 z=9 \\
& 7 x+3 y-2 z=8 \\
& 12 x+3 y-(4+\lambda) z=16-\mu
\end{aligned}$
have infinitely many solutions. Then the radius of the circle centred at $(\lambda, \mu)$ and touching the line $4 x=3 y$ is

**Options:**

- **(A)** $\frac{17}{5}$
- **(B)** $\frac{7}{5}$
- **(C)** 7
- **(D)** $\frac{21}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{7}{5}$**

**Detailed Solution:**

$\begin{aligned} & \left|\begin{array}{ccc}2 & 3 & 5 \\ 7 & 3 & -2 \\ 12 & 3 & -(\lambda+4)\end{array}\right|=0 \\ & \Rightarrow 12(-21)-3(-39)-(\lambda+4)(-15)=0 \\ & \Rightarrow-252+117+15(1+4)=0 \\ & \Rightarrow 15 \lambda+177-252=0 \\ & \Rightarrow 15 \lambda-75=0 \Rightarrow \lambda=5 \\ & \left|\begin{array}{ccc}9 & 3 & 5 \\ 8 & 3 & -2 \\ 16-\mu & 3 & -9\end{array}\right|=0 \Rightarrow\left|\begin{array}{ccc}1 & 0 & 7 \\ \mu-8 & 0 & 7 \\ 16-\mu & 3 & -9\end{array}\right|=0 \\ & \Rightarrow 7-7(\mu-8)=0 \Rightarrow 1-(\mu-8)=0 \Rightarrow \mu=9 \\ & \Rightarrow \text { centre of circle }(5,9) \\ & \text { radius }=\text { length of } \perp \text { from centre }(5, \quad 9)= \\ & \left|\frac{20-27}{5}\right|=\frac{7}{5}\end{aligned}$

</details>

---

### Q12. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the system of equation
$\begin{aligned}
& 2 x+\lambda y+3 z=5 \\
& 3 x+2 y-z=7 \\
& 4 x+5 y+\mu z=9
\end{aligned}$
has infinitely many solutions, then $\left(\lambda^2+\mu^2\right)$ is equal to :

**Options:**

- **(A)** $22$
- **(B)** $18$
- **(C)** $26$
- **(D)** $30$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $26$**

**Detailed Solution:**

$\Delta=0 \Rightarrow\left|\begin{array}{ccc}2 & \lambda & 3 \\ 3 & 2 & -1 \\ 4 & 5 & \mu\end{array}\right|=0$
$\Rightarrow 2(2 \mu+5)+\lambda(-4-3 \mu)+3(7)=0$
$\Rightarrow 4 \mu-3 \lambda \mu-4 \lambda+31=0$   ...(1)
$\begin{aligned}
& \Delta_3=0 \Rightarrow\left|\begin{array}{lll}
2 & \lambda & 5 \\
3 & 2 & 7 \\
4 & 5 & 9
\end{array}\right|=0 \\
& \Rightarrow 2(-17)+\lambda(1)+5(7)=0 \\
& \Rightarrow \lambda=-1
\end{aligned}$
from equation (1)
$4 \mu+3 \mu+4+31=0 \Rightarrow \mu=-5$
$\therefore \lambda^2+\mu^2=26$

</details>

---

### Q13. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the system of linear equations
$\begin{aligned} & 3 x+y+\beta z=3 \\ & 2 x+\alpha y-z=-3 \\ & x+2 y+z=4\end{aligned}$
has infinitely many solutions, then the value of $22 \beta-9 \alpha$ is :

**Options:**

- **(A)** 49
- **(B)** 31
- **(C)** 43
- **(D)** 37

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 31**

**Detailed Solution:**

$\Delta=\left|\begin{array}{ccc}3 & 1 & \beta \\ 2 & \alpha & -1 \\ 1 & 2 & 1\end{array}\right|=0$
$3 \alpha+4 \beta-\alpha \beta+3=0$
$\Delta_3=\left|\begin{array}{ccc}3 & 1 & 3 \\ 2 & \alpha & -3 \\ 1 & 2 & 4\end{array}\right|=0$
$9 \alpha+19=0$
$\alpha=\frac{-19}{9}, \beta=\frac{6}{11}$
$\Rightarrow 22 \beta-9 \alpha=31$

</details>

---

### Q14. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\alpha, \beta(\alpha \neq \beta)$ be the values of m , for which the equations $x+y+z=1 ; x+2 y+4 z=\mathrm{m}$ and $x+4 y+10 z=m^2$ have infinitely many solutions. Then the value of $\sum_{n=1}^{10}\left(n^\alpha+n^\beta\right)$ is equal to :

**Options:**

- **(A)** 3080
- **(B)** 560
- **(C)** 3410
- **(D)** 440

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 440**

**Detailed Solution:**

$\begin{aligned}
\Delta & =\left|\begin{array}{llc}
1 & 1 & 1 \\
1 & 2 & 4 \\
1 & 4 & 10
\end{array}\right|=1(20-16)-1(10-4)+1(4-2) \\
& =4-6+2=0
\end{aligned}$

For infinite solutions
$\begin{aligned}
& \Delta_x=\Delta_y=\Delta_z=0 \\
& m^2-3 x+2=0 \\
& m=1,2 \\
& \alpha=1, \beta=2 \\
& \therefore \sum_{n=1}^{10}\left(n^\alpha+n^\beta\right)=\sum_{n=1}^{10} n^1+\sum_{n=1}^{10} n^2 \\
&= \frac{10(11)}{2}+\frac{10(11)(21)}{6} \\
&= 55+385 \\
&= 440
\end{aligned}$

</details>

---

### Q15. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the system of equations
$\begin{aligned}
& x+2 y-3 z=2 \\
& 2 x+\lambda y+5 z=5 \\
& 14 x+3 y+\mu z=33
\end{aligned}$
has infinitely many solutions, then $\lambda+\mu$ is equal to :

**Options:**

- **(A)** 13
- **(B)** 10
- **(C)** 12
- **(D)** 11

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 12**

**Detailed Solution:**

$\begin{aligned}
& \Delta=\left|\begin{array}{ccc}
1 & 2 & -3 \\
2 & \lambda & 5 \\
14 & 3 & \mu
\end{array}\right|=0 \Rightarrow \lambda \mu+42 \lambda-4 \mu+107=0 \\
& \Delta_1=\left|\begin{array}{ccc}
2 & 2 & -3 \\
5 & \lambda & 5 \\
33 & 3 & \mu
\end{array}\right|=0 \Rightarrow 2 \lambda \mu+99 \lambda-10 \mu+255=0 \\
& \Delta_2=\left|\begin{array}{ccc}
1 & 2 & -3 \\
2 & 5 & 5 \\
14 & 33 & \mu
\end{array}\right|=0 \Rightarrow \mu=13
\end{aligned}$
Also, $\lambda=-1$
Hence, $\lambda+\mu=13-1=12$

</details>

---

### Q16. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the system of equations
$\begin{aligned}
& 2 x-y+z=4 \\
& 5 x+\lambda y+3 z=12 \\
& 100 x-47 y+\mu z=212
\end{aligned}$
has infinitely many solutions, then $\mu-2 \lambda$ is equal to

**Options:**

- **(A)** $57$
- **(B)** $59$
- **(C)** $55$
- **(D)** $56$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $57$**

**Detailed Solution:**

$\begin{aligned} & 2 x-y+z=4 \\ & 5 x+\lambda y+3 z=12 \\ & 100 x-47 y+\mu z=212 \\ & \Delta x=\Delta y=\Delta z=0 \\ & \Delta z=\left|\begin{array}{ccc}2 & -1 & 4 \\ 5 & \lambda & 12 \\ 100 & -47 & 212\end{array}\right|=0 \\ & \Rightarrow 2(212 \lambda+564)+1(1060-1200) \\ & \Rightarrow 424 \lambda+1128-140-940-400 \lambda=0 \\ & \Rightarrow \lambda=-2 \\ & \quad \Delta y=\left|\begin{array}{ccc}2 & -1 & 1 \\ 5 & -2 & 3 \\ 100 & -47 & \mu\end{array}\right|=0 \\ & \Rightarrow 2(-2 \mu+141)+1(5 \mu-300)+1(-235+200)=0 \\ & \Rightarrow \quad \mu=53 \\ & \mu-2 \lambda=53-2(-2)=57\end{aligned}$

</details>

---

### Q17. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The system of equations
$\begin{aligned}
& x+y+z=6 \\
& x+2 y+5 z=9, \\
& x+5 y+\lambda z=\mu,
\end{aligned}$
has no solution if

**Options:**

- **(A)** $\lambda=15, \mu \neq 17$
- **(B)** $\lambda \neq 17, \mu \neq 18$
- **(C)** $\lambda=17, \mu \neq 18$
- **(D)** $\lambda=17, \mu=18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\lambda=17, \mu \neq 18$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{D}=\left|\begin{array}{lll}1 & 1 & 1 \\ 1 & 2 & 5 \\ 1 & 5 & \lambda\end{array}\right|=0 \\ & \lambda=17 \\ & D_z=\left|\begin{array}{lll}1 & 1 & 6 \\ 1 & 2 & 9 \\ 1 & 5 & \mu\end{array}\right| \neq 0 \\ & \mu \neq 18\end{aligned}$

</details>

---

### Q18. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the system of equations
$\begin{aligned} & (\lambda-1) x+(\lambda-4) y+\lambda z=5 \\ & \lambda x+(\lambda-1) y+(\lambda-4) z=7 \\ & (\lambda+1) x+(\lambda+2) y-(\lambda+2) z=9\end{aligned}$
has infinitely many solutions, then $\lambda^2+\lambda$ is equal to

**Options:**

- **(A)** $6$
- **(B)** $10$
- **(C)** $20$
- **(D)** $12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $12$**

**Detailed Solution:**

$\begin{aligned}
& (\lambda-1) x+(\lambda-4) y+\lambda z=5 \\
& \lambda x+(\lambda-1) y+(\lambda-4) z=7 \\
& (\lambda+1) x+(\lambda+2) y-(\lambda+2) z=9
\end{aligned}$

For infinitely many solutions
$\begin{aligned}
& \mathrm{D}=\left|\begin{array}{ccc}
\lambda-1 & \lambda-4 & \lambda \\
\lambda & \lambda-1 & \lambda-4 \\
\lambda+1 & \lambda+2 & -(\lambda+2)
\end{array}\right|=0 \\
& (\lambda-3)(2 \lambda+1)=0 \\
& \mathrm{D}_{\mathrm{x}}=\left|\begin{array}{ccc}
5 & \lambda-4 & \lambda \\
7 & \lambda-1 & \lambda-4 \\
9 & \lambda+2 & -(\lambda+2)
\end{array}\right|=0 \\
& 2(3-\lambda)(23-2 \lambda)=0 \\
& \lambda=3 \\
& \therefore \lambda^2+\lambda=9+3=12
\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the system of linear equations :
$\begin{aligned}
& x+y+2 z=6 \\
& 2 x+3 y+\mathrm{a} z=\mathrm{a}+1 \\
& -x-3 y+\mathrm{b} z=2 \mathrm{~b}
\end{aligned}$
where $a, b \in \mathbf{R}$, has infinitely many solutions, then $7 a+3 b$ is equal to :

**Options:**

- **(A)** 16
- **(B)** 12
- **(C)** 22
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 16**

**Detailed Solution:**

The given equations are
$\begin{aligned}
& x+y+2 z=6 \\
& 2 x+3 y+a z=a+1 \\
& -x-3 y+b z=2 b, \text { where } a, b, \in \mathbf{R}
\end{aligned}$

For infinite many solutions:
$D=D_1=D_2=D_3=0$
$\begin{aligned}
& \therefore D=\left|\begin{array}{ccc}
1 & 1 & 2 \\
2 & 3 & a \\
-1 & -3 & b
\end{array}\right|=2 a+b-6 \\
& D_1=\left|\begin{array}{ccc}
6 & 1 & 2 \\
a+1 & 3 & a \\
2 b & -3 & b
\end{array}\right|=12 a+5 b+a b-6 \\
& D_2=\left|\begin{array}{ccc}
1 & 6 & 2 \\
2 & a+1 & a \\
-1 & 2 b & b
\end{array}\right|=-4 a-3 b-a b+2 \\
& \text { and } D_3=\left|\begin{array}{ccc}
1 & 1 & 6 \\
2 & 3 & a+1 \\
-1 & -3 & 2 b
\end{array}\right|=2 a+2 b-16
\end{aligned}$
from above relations
$\begin{aligned}
& a=-2, b=10 \\
& \therefore 7 a+3 b=16
\end{aligned}$

</details>

---

### Q20. JEE Main 2024 (09 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Consider the matrices : $A=\left[\begin{array}{ll}2 & -5 \\ 3 & m\end{array}\right], B=\left[\begin{array}{l}20 \\ m\end{array}\right]$ and $X=\left[\begin{array}{l}x \\ y\end{array}\right]$. Let the set of all $m$, for which the system of equations $A X=B$ has a negative solution (i.e., $x < 0$ and $y < 0$ ), be the interval $(a, b)$. Then $8 \int_a^b|A| d m$ is equal to_________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **450**

**Detailed Solution:**

$\begin{aligned} & A=\left(\begin{array}{cc}2 & -5 \\ 3 & m\end{array}\right), B=\left(\begin{array}{c}20 \\ m\end{array}\right) \\ & X=\left(\begin{array}{l}x \\ y\end{array}\right) \\ & 2 x-5 y=20 \ldots(1)\\ & 3 x+m y=m \ldots(2)\\ & \Rightarrow y=\frac{2 m-60}{2 m+15} \\ & y < 0 \Rightarrow m \in\left(\frac{-15}{2}, 30\right)\end{aligned}$
$\begin{aligned}
& \mathrm{x}=\frac{25 \mathrm{~m}}{2 \mathrm{~m}+15} \\
& \mathrm{x} < 0 \Rightarrow \mathrm{m} \in\left(\frac{-15}{2}, 0\right) \\
& \Rightarrow \mathrm{m} \in\left(\frac{-15}{2}, 0\right) \\
& |\mathrm{A}|=2 \mathrm{~m}+15
\end{aligned}$
Now,
$\begin{aligned}
& 8 \int_{\frac{-15}{2}}^0(2 \mathrm{~m}+15) \mathrm{dm}=8\left\{\mathrm{~m}^2+15 \mathrm{~m}\right\}_{\frac{-15}{2}}^0 \\
& \Rightarrow 8\left\{-\left(\frac{225}{4}-\frac{225}{2}\right)\right\} \\
& =8 \times \frac{225}{4}=450
\end{aligned}$

</details>

---

### Q21. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $\lambda, \mu \in \mathbf{R}$. If the system of equations
$\begin{aligned}
& 3 x+5 y+\lambda z=3 \\
& 7 x+11 y-9 z=2 \\
& 97 x+155 y-189 z=\mu
\end{aligned}$
has infinitely many solutions, then $\mu+2 \lambda$ is equal to :

**Options:**

- **(A)** 24
- **(B)** 25
- **(C)** 22
- **(D)** 27

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 25**

**Detailed Solution:**

$\begin{array}{l}
3 x+5 y+\lambda z=3 \\
7 x+11 y-9 z=2 \\
97 x+155 y-189 z=\mu \\
93 x+155 y+31 \lambda z=93 \\
97 x+155 y-189 z=\mu \\
-\quad+\quad+\quad- \\
\hline-4 x+(31 \lambda+189) z=93-\mu \\
1085 x+1705 y-1395 z=310 \\
1067 x+1705 y-2079 z=11 \mu \\
-\quad+\quad-\quad \\
\hline 18 x+684 z=310-11 \mu
\end{array}$
$\begin{aligned}
& -36 x+9(31 \lambda+189) z=9(93-\mu) \\
& 36 x+1368 z=2(310-11 \mu) \\
& (279 \lambda+3069) z=1457-31 \mu
\end{aligned}$
for infinite solutions -
$\begin{aligned}
& \lambda=\frac{-3069}{279}=\frac{-341}{31} \\
& \mu=\frac{1457}{31}
\end{aligned}$
$\mu+2 \lambda=\frac{1457-682}{31}=\frac{775}{31}=25$

</details>

---

### Q22. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the system of equations $x+4 y-z=\lambda, 7 x+9 y+\mu z=-3,5 x+y+2 z=-1$ has infinitely many solutions, then $(2 \mu+3 \lambda)$ is equal to :

**Options:**

- **(A)** 3
- **(B)** -3
- **(C)** -2
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -3**

**Detailed Solution:**

$\begin{aligned} & \Delta=\left|\begin{array}{ccc}1 & 4 & -1 \\ 7 & 9 & \mu \\ 5 & 1 & 2\end{array}\right|=0 \\ & \Rightarrow(18-\mu)-4(14-5 \mu)-(7-45)=0 \Rightarrow \mu=0 \\ & \Delta=\Delta_{\mathrm{x}}=\Delta_{\mathrm{y}}=\Delta_{\mathrm{z}}=0 \text { (For infinite solution) } \\ & \Delta_{\mathrm{x}}=\left|\begin{array}{ccc}\lambda & 4 & -1 \\ -3 & 9 & \mu \\ -1 & 1 & 2\end{array}\right|=0 \\ & \lambda(18-\mu)-4(-6+\mu)-1(-3+9)=0 \\ & 18 \lambda+24-6=0 \Rightarrow \lambda=-1\end{aligned}$

</details>

---

### Q23. JEE Main 2024 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

If the system of equations
$\begin{aligned}
& 2 x+7 y+\lambda z=3 \\
& 3 x+2 y+5 z=4 \\
& x+\mu y+32 z=-1
\end{aligned}$
has infinitely many solutions, then $(\lambda-\mu)$ is equal to________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **38**

**Detailed Solution:**

$\begin{aligned} & \mathrm{D}=\mathrm{D}_1=\mathrm{D}_2=\mathrm{D}_3=0 \\ & \mathrm{D}_3=\left|\begin{array}{ccc}2 & 7 & 3 \\ 3 & 2 & 4 \\ 1 & \mu & -1\end{array}\right|=0 \Rightarrow \mu=-39 \\ & \mathrm{D}=\left|\begin{array}{ccc}2 & 7 & \lambda \\ 3 & 2 & 5 \\ 1 & -39 & 32\end{array}\right|=0 \Rightarrow \lambda=-1 \\ & \lambda-\mu=38\end{aligned}$

</details>

---

### Q24. JEE Main 2024 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $\alpha \beta \gamma=45 ; \alpha, \beta, \gamma \in \mathbb{R}$. If $x(\alpha, 1,2)+y(1, \beta, 2)+z(2,3, \gamma)=(0,0,0)$ for some $x, y, z \in \mathbb{R}, x y z \neq 0$, then $6 \alpha+4 \beta+\gamma$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **55**

**Detailed Solution:**

$\begin{aligned} & \alpha \beta \gamma=45, \alpha \beta \gamma \in \mathrm{R} \\ & \mathrm{x}(\alpha, 1,2)+\mathrm{y}(1, \beta, 2)+\mathrm{z}(2,3, \gamma)=(0,0,0) \\ & \mathrm{x}, \mathrm{y}, \mathrm{z} \in \mathrm{R}, \mathrm{xyz} \neq 0 \\ & \alpha \mathrm{x}+\mathrm{y}+2 \mathrm{z}=0 \\ & \mathrm{x}+\beta \mathrm{y}+3 \mathrm{z}=0 \\ & 2 \mathrm{x}+2 \mathrm{y}+\gamma \mathrm{z}=0 \\ & \mathrm{xyz} \neq 0 \Rightarrow \text { non-trivial } \\ & \left|\begin{array}{lll}\alpha & 1 & 2 \\ 1 & \beta & 3 \\ 2 & 2 & \gamma\end{array}\right|=0\end{aligned}$
$\begin{aligned} & \Rightarrow \alpha(\beta \gamma-6)-1(\gamma-6)+2(2-2 \beta)=0 \\ & \Rightarrow \alpha \beta \gamma-6 \alpha-\gamma+6+4-4 \beta=0 \\ & \Rightarrow 6 \alpha+4 \beta+\gamma=55\end{aligned}$

</details>

---

### Q25. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The values of $m, n$, for which the system of equations
$\begin{aligned}
& x+y+z=4, \\
& 2 x+5 y+5 z=17, \\
& x+2 y+\mathrm{m} z=\mathrm{n}
\end{aligned}$
has infinitely many solutions, satisfy the equation:

**Options:**

- **(A)** $m^2+n^2-m n=39$
- **(B)** $m^2+n^2-m-n=46$
- **(C)** $m^2+n^2+m+n=64$
- **(D)** $m^2+n^2+m n=68$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $m^2+n^2-m n=39$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{D}=\left|\begin{array}{lll}1 & 1 & 1 \\ 2 & 5 & 5 \\ 1 & 2 & \mathrm{~m}\end{array}\right|=0 \Rightarrow \mathrm{m}=2 \\ & \mathrm{D}_3=\left|\begin{array}{ccc}1 & 1 & 4 \\ 2 & 5 & 17 \\ 1 & 2 & \mathrm{n}\end{array}\right|=0 \Rightarrow \mathrm{n}=7\end{aligned}$

</details>

---

### Q26. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the system of equations
$\begin{array}{r}
11 x+y+\lambda z=-5 \\
2 x+3 y+5 z=3 \\
8 x-19 y-39 z=\mu
\end{array}$
has infinitely many solutions, then $\lambda^4-\mu$ is equal to :

**Options:**

- **(A)** 51
- **(B)** 45
- **(C)** 47
- **(D)** 49

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 47**

**Detailed Solution:**

$\begin{aligned}
& 11 x+y+\lambda z=-5 \\
& 2 x+3 y+5 z=3 \\
& 8 x-19 y-39 z=\mu
\end{aligned}$
for infinite sol.
$\begin{aligned}
& \mathrm{D}=\left|\begin{array}{ccc}
11 & 1 & \lambda \\
2 & 3 & 5 \\
8 & -19 & -39
\end{array}\right|=0 \\
& \Rightarrow 11(-117+95)-1(-78-40)+\lambda(-38-24) \\
& \Rightarrow 11(-22)+118-\lambda(62)=0 \\
& \Rightarrow 62 \lambda=118-242 \\
& \Rightarrow \lambda=\frac{-124}{62}=-2
\end{aligned}$
$\begin{aligned} & \mathrm{D}_1=\left|\begin{array}{ccc}-5 & 1 & -2 \\ 3 & 3 & 5 \\ \mu & -19 & -39\end{array}\right|=0 \\ & \Rightarrow-5(-117+95)-1(-117-5 \mu)-2(-57-3 \mu)=0 \\ & \Rightarrow-5(-22)+117+5 \mu+114+6 \mu=0 \\ & \Rightarrow 11 \mu=-110-231=-341 \\ & \Rightarrow \mu=-31 \\ & \lambda^4-\mu=(-2)^4-(-31)=16+31=47\end{aligned}$

</details>

---

### Q27. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the system of equations
$\begin{aligned}
& x+(\sqrt{2} \sin \alpha) y+(\sqrt{2} \cos \alpha) z=0 \\
& x+(\cos \alpha) y+(\sin \alpha) z=0 \\
& x+(\sin \alpha) y-(\cos \alpha) z=0
\end{aligned}$
has a non-trivial solution, then $\alpha \in\left(0, \frac{\pi}{2}\right)$ is equal to :

**Options:**

- **(A)** $\frac{11 \pi}{24}$
- **(B)** $\frac{5 \pi}{24}$
- **(C)** $\frac{7 \pi}{24}$
- **(D)** $\frac{3 \pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5 \pi}{24}$**

**Detailed Solution:**

$\begin{aligned} & \left|\begin{array}{ccc}1 & \sqrt{2} \sin \alpha & \sqrt{2} \cos \alpha \\ 1 & \sin \alpha & -\cos \alpha \\ 1 & \cos \alpha & \sin \alpha\end{array}\right|=0 \\ & \Rightarrow 1-\sqrt{2} \sin \alpha(\sin \alpha+\cos \alpha)+\sqrt{2} \cos \alpha(\cos \alpha-\sin \alpha)=0 \\ & \Rightarrow 1+\sqrt{2} \cos 2 \alpha-\sqrt{2} \sin 2 \alpha=0 \\ & \cos 2 \alpha-\sin 2 \alpha=-\frac{1}{\sqrt{2}} \\ & \cos \left(2 \alpha+\frac{\pi}{4}\right)=-\frac{1}{2} \\ & 2 \alpha+\frac{\pi}{4}=2 \mathrm{n} \pi \pm \frac{2 \pi}{3} \\ & \alpha+\frac{\pi}{8}=\mathrm{n} \pi \pm \frac{\pi}{3} \\ & \mathrm{n}=0 \\ & \mathrm{x}=\frac{\pi}{3}-\frac{\pi}{8}=\frac{5 \pi}{24}\end{aligned}$

</details>

---

### Q28. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let the system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>5</mn><mo>,</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>9</mn><mo>,</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>λ</mi><mi>z</mi><mo>=</mo><mi>μ</mi></math> have infinite number of solutions. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>+</mo><mn>2</mn><mi>μ</mi></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>5</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>9</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>λ</mi><mi>z</mi><mo>=</mo><mi>μ</mi></math>.</p><p>For infinite solutions, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Δ</mi><mo>=</mo><msub><mi>Δ</mi><mn>1</mn></msub><mo>=</mo><msub><mi>Δ</mi><mn>2</mn></msub><mo>=</mo><msub><mi>Δ</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Δ</mi><mo>=</mo><mfenced close="|" open="|"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>λ</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mi>λ</mi><mo>-</mo><mn>3</mn><mo>-</mo><mn>4</mn><mi>λ</mi><mo>+</mo><mn>8</mn><mo>+</mo><mn>18</mn><mo>-</mo><mn>36</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mo>−</mo><mn>13</mn></math></p><p>Now, finding </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>Δ</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>5</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>μ</mi></mtd><mtd><mn>3</mn></mtd><mtd><mo>−</mo><mn>13</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>μ</mi><mo>=</mo><mn>15</mn></math></p><p>Now, finding</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>Δ</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>9</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mi>μ</mi></mtd><mtd><mi>λ</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>Δ</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>9</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>15</mn></mtd><mtd><mo>−</mo><mn>13</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>Δ</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math></p><p>And </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>Δ</mi><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>9</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>μ</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>Δ</mi><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>9</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>15</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>Δ</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>=</mo><mo>−</mo><mn>13</mn><mo>,</mo><mo> </mo><mi>μ</mi><mo>=</mo><mn>15</mn></math> system of equation has infinite solutions.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>+</mo><mn>2</mn><mi>μ</mi><mo>=</mo><mn>17</mn></math>.</p>

</details>

---

### Q29. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>If the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>−</mo><mi>z</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>α</mi><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mo>−</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>−</mo><mi>y</mi><mo>+</mo><mi>β</mi><mi>z</mi><mo>=</mo><mn>7</mn></math></p><p>has infinitely many solutions, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mi>α</mi><mi>β</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1110</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1120</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1210</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1220</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1120</mn></math>**

**Detailed Solution:**

<p>Given:</p><p>The system of equations,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>α</mi><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>β</mi><mi>z</mi><mo>=</mo><mn>7</mn></math> have many solutions,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>△</mo><mo>=</mo><msub><mo>△</mo><mn>1</mn></msub><mo>=</mo><msub><mo>△</mo><mn>2</mn></msub><mo>=</mo><msub><mo>△</mo><mn>3</mn></msub></math></p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>△</mo><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>7</mn></mtd><mtd><mi>β</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>4</mn><mi>β</mi><mo>-</mo><mn>21</mn></mrow></mfenced><mo>-</mo><mn>5</mn><mfenced><mrow><mi>β</mi><mo>-</mo><mn>9</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>7</mn><mo>+</mo><mn>12</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>13</mn><mi>β</mi><mo>=</mo><mo>-</mo><mn>16</mn></math></p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>△</mo><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>α</mi></mtd><mtd><mo>-</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>7</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>14</mn><mi>α</mi><mo>-</mo><mn>8</mn><mo>-</mo><mn>57</mn><mo>-</mo><mn>5</mn><mo>-</mo><mn>15</mn><mi>α</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mo>-</mo><mn>70</mn></math></p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mi>α</mi><mi>β</mi><mo>=</mo><mn>70</mn><mo>×</mo><mn>16</mn><mo>=</mo><mn>1120</mn></math></p>

</details>

---

### Q30. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let A be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>×</mo><mn>3</mn></math> real matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>2</mn><mfenced><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo> </mo><mi>A</mi><mfenced><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mo>−</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>4</mn><mfenced><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mo>−</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo> </mo><mi>A</mi><mfenced><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>2</mn><mfenced><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math>. Then, the system <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>A</mi><mo>−</mo><mn>3</mn><mi>I</mi></mrow></mfenced><mfenced><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd></mtr><mtr><mtd><mi>z</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math> has</p>

**Options:**

- **(A)** unique solution
- **(B)** exactly two solutions
- **(C)** no solution
- **(D)** infinitely many solutions

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) unique solution**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><msub><mi>x</mi><mn>1</mn></msub></mtd><mtd><msub><mi>y</mi><mn>1</mn></msub></mtd><mtd><msub><mi>z</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>x</mi><mn>2</mn></msub></mtd><mtd><msub><mi>y</mi><mn>2</mn></msub></mtd><mtd><msub><mi>z</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>x</mi><mn>3</mn></msub></mtd><mtd><msub><mi>y</mi><mn>3</mn></msub></mtd><mtd><msub><mi>z</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math></p><p>It is given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><msub><mi>z</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><msub><mi>z</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mo>−</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mo>−</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mo>−</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><mo>−</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><mo>−</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><msub><mi>z</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mo>-</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>−</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><mo>−</mo><mn>4</mn><mo>,</mo><mo> </mo><mo>−</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mo>−</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><msub><mi>z</mi><mn>3</mn></msub><mo>=</mo><mn>4</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><msub><mi>y</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>y</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>y</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><msub><mi>y</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo> </mo><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mo>−</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><mo>−</mo><mn>1</mn><mo>,</mo><mo> </mo><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><msub><mi>z</mi><mn>3</mn></msub><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>−</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>−</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>A</mi><mo>−</mo><mn>3</mn><mi>I</mi></mrow></mfenced><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd></mtr><mtr><mtd><mi>z</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mo>−</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>−</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>−</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>−</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd></mtr><mtr><mtd><mi>z</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mo>−</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mo>−</mo><mi>z</mi></mtd></mtr><mtr><mtd><mo>−</mo><mi>y</mi></mtd></mtr><mtr><mtd><mo>−</mo><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>z</mi><mo>=</mo><mo>−</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mo>−</mo><mn>2</mn><mo>,</mo><mo> </mo><mi>x</mi><mo>=</mo><mo>−</mo><mn>3</mn></math></p>

</details>

---

### Q31. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>If the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>α</mi><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>β</mi><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p>has infinitely many solutions, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>α</mi><mo>+</mo><mn>13</mn><mi>β</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>54</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>58</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>58</mn></math>**

**Detailed Solution:**

<p>Given:</p><p>The system of linear equations </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>4</mn></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>α</mi><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>5</mn></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>β</mi><mi>z</mi><mo>=</mo><mn>3</mn></math> has infinity many solutions,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>△</mo><mo>=</mo><msub><mo>△</mo><mn>1</mn></msub><mo>=</mo><msub><mo>△</mo><mn>2</mn></msub><mo>=</mo><msub><mo>△</mo><mn>3</mn></msub></math></p><p>Now, finding, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>△</mo><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>β</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>5</mn><mi>β</mi><mo>-</mo><mn>9</mn><mo>+</mo><mn>8</mn><mi>β</mi><mo>-</mo><mn>36</mn><mo>-</mo><mn>9</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>13</mn><mi>β</mi><mo>=</mo><mn>54</mn></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>△</mo><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>α</mi></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mi>α</mi><mo>+</mo><mn>5</mn><mo>+</mo><mn>12</mn><mo>-</mo><mn>30</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>12</mn><mi>α</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>15</mn><mi>α</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>12</mn><mi>α</mi><mo>=</mo><mn>4</mn></math></p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>α</mi><mo>+</mo><mn>13</mn><mi>β</mi><mo>=</mo><mn>4</mn><mo>+</mo><mn>54</mn><mo>=</mo><mn>58</mn></math></p>

</details>

---

### Q32. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider the system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>5</mn><mo>,</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><msup><mi>λ</mi><mn>2</mn></msup><mi>z</mi><mo>=</mo><mn>9</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>λ</mi><mi>z</mi><mo>=</mo><mi>μ</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>,</mo><mi>μ</mi><mo>∈</mo><mi>R</mi></math>. Then, which of the following statement is NOT correct ?

**Options:**

- **(A)** System has infinite number of solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi><mo>=</mo><mn>13</mn></math>
- **(B)** System is inconsistent if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi><mo>≠</mo><mn>13</mn></math>
- **(C)** System has unique solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>≠</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi><mo>≠</mo><mn>13</mn></math>
- **(D)** System is consistent if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>≠</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi><mo>=</mo><mn>13</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) System has unique solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>≠</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi><mo>≠</mo><mn>13</mn></math>**

**Detailed Solution:**

<blockquote><p>Given: </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><msup><mi>λ</mi><mn>2</mn></msup><mi>z</mi><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo> </mo><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>λ</mi><mi>z</mi><mo>=</mo><mi>μ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>△</mo><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><msup><mi>λ</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>λ</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>△</mo><mo>=</mo><mn>2</mn><mi>λ</mi><mo>-</mo><mn>3</mn><msup><mi>λ</mi><mn>2</mn></msup><mo>-</mo><mi>λ</mi><mo>+</mo><msup><mi>λ</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>△</mo><mo>=</mo><mo>-</mo><mn>2</mn><msup><mi>λ</mi><mn>2</mn></msup><mo>+</mo><mi>λ</mi><mo>+</mo><mn>1</mn></math></p><p>We know that for infinite solutions, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>△</mo><mo>=</mo><mn>0</mn><mo> </mo><mo>&amp;</mo><mo> </mo><msub><mo>△</mo><mn>1</mn></msub><mo>=</mo><msub><mo>△</mo><mn>2</mn></msub><mo>=</mo><msub><mo>△</mo><mn>3</mn></msub><mo>=</mo><mn>0</mn><mo> </mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>2</mn><msup><mi>λ</mi><mn>2</mn></msup><mo>+</mo><mi>λ</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msup><mi>λ</mi><mn>2</mn></msup><mo>-</mo><mi>λ</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>λ</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>λ</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>△</mo><mn>1</mn></msub></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Δ</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|" separators="|"><mtable columnalign="left"><mtr><mtd><mn>5</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>μ</mi></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">Δ</mi><mn>1</mn></msub><mo>=</mo><mi>μ</mi><mo>-</mo><mn>13</mn></math></p><p>And for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Δ</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|" separators="|"><mtable columnalign="left"><mtr><mtd><mn>5</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>2</mn></mtd><mtd><mfrac><mn>1</mn><mn>4</mn></mfrac></mtd></mtr><mtr><mtd><mi>μ</mi></mtd><mtd><mn>3</mn></mtd><mtd><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced close="|" open="|" separators="|"><mtable columnalign="left"><mtr><mtd><mn>5</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>μ</mi></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfrac><mn>7</mn><mn>4</mn></mfrac><mfenced><mrow><mn>13</mn><mo>-</mo><mi>μ</mi></mrow></mfenced></math></p><p>So, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>≠</mo><mn>1</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mi>μ</mi><mo>≠</mo><mn>13</mn></math> system has no solution,</p><p>Hence, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>C</mi></mfenced></math> is the correct answer.</p></blockquote>

</details>

---

### Q33. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider the system of linear equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>μ</mi><mo>,</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>λ</mi><mi>z</mi><mo>=</mo><mn>10</mn><mi>μ</mi><mo>,</mo><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>4</mn><msup><mi>λ</mi><mn>2</mn></msup><mi>z</mi><mo>=</mo><msup><mi>μ</mi><mn>2</mn></msup><mo>+</mo><mn>15</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>,</mo><mi>μ</mi><mo>∈</mo><mi mathvariant="normal">R</mi></math>. Which one of the following statements is NOT correct?

**Options:**

- **(A)** The system has unique solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>≠</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi><mo>≠</mo><mn>1</mn><mo>,</mo><mn>15</mn></math>
- **(B)** The system is inconsistent if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi><mo>≠</mo><mn>1</mn></math>
- **(C)** The system has infinite number of solutions if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi><mo>=</mo><mn>15</mn></math>
- **(D)** The system is consistent if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>≠</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) The system is inconsistent if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi><mo>≠</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Given: </p><p>System of linear equations,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>4</mn><mi>μ</mi><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>λ</mi><mi>z</mi><mo>=</mo><mn>10</mn><mi>μ</mi><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>4</mn><mi>λ</mi><mmultiscripts><mi>z</mi><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mo>=</mo><msup><mi>μ</mi><mn>2</mn></msup><mo>+</mo><mn>15</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Δ</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn><mi>λ</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>4</mn><msup><mi>λ</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Δ</mi><mo>=</mo><mfenced><mrow><mn>8</mn><msup><mi>λ</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>λ</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>4</mn><msup><mi>λ</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>λ</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Δ</mi><mo>=</mo><mpadded lspace="-1px"><mn>8</mn><msup><mi>λ</mi><mn>2</mn></msup></mpadded><mo>-</mo><mn>6</mn><mi>λ</mi><mo>-</mo><mn>4</mn><msup><mi>λ</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>λ</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Δ</mi><mo>=</mo><mpadded lspace="-1px"><mn>4</mn><msup><mi>λ</mi><mn>2</mn></msup></mpadded><mo>-</mo><mn>4</mn><mi>λ</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Δ</mi><mo>=</mo><mo>(</mo><mn>2</mn><mi>λ</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></math></p><p>For unique solution, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Δ</mi><mo>≠</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>λ</mi><mo>-</mo><mn>1</mn><mo>≠</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>≠</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Δ</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>λ</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>We know that, for infinite solutions, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Δ</mi><mi>x</mi></msub><mo>=</mo><msub><mi>Δ</mi><mi>y</mi></msub><mo>=</mo><msub><mi>Δ</mi><mi>z</mi></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>Δ</mi><mi>x</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>4</mn><mi>μ</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>10</mn><mi>μ</mi></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><msup><mi>μ</mi><mn>2</mn></msup><mo>+</mo><mn>15</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>Δ</mi><mi>x</mi></msub><mo>=</mo><mn>4</mn><mi>μ</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>10</mn><mi>μ</mi><mo>-</mo><msup><mi>μ</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>30</mn><mi>μ</mi><mo>-</mo><mn>2</mn><msup><mi>μ</mi><mn>2</mn></msup><mo>-</mo><mn>30</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>Δ</mi><mi>x</mi></msub><mo>=</mo><mo>-</mo><mn>4</mn><mi>μ</mi><mo>-</mo><mn>10</mn><mi>μ</mi><mo>+</mo><msup><mi>μ</mi><mn>2</mn></msup><mo>+</mo><mn>15</mn><mo>+</mo><mn>30</mn><mi>μ</mi><mo>-</mo><mn>2</mn><msup><mi>μ</mi><mn>2</mn></msup><mo>-</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>Δ</mi><mi>x</mi></msub><mo>=</mo><mo>-</mo><msup><mi>μ</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><mi>μ</mi><mo>-</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>(</mo><mi>μ</mi><mo>-</mo><mn>15</mn><mo>)</mo><mo>(</mo><mi>μ</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p>So, for infinite solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo> </mo><mi>μ</mi><mo>=</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>.</p>

</details>

---

### Q34. JEE Main 2024 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>Let for any three distinct consecutive terms <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo> </mo><mi>b</mi><mo>,</mo><mo> </mo><mi>c</mi></math> of an A.P, the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mi>y</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> be concurrent at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>(</mo><mi>α</mi><mo>,</mo><mi>β</mi><mo>)</mo></math> be a point such that the system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mi>α</mi><mi>z</mi><mo>=</mo><mi>β</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mo> </mo><mi>y</mi><mo>+</mo><mn>3</mn><mo> </mo><mi>z</mi><mo>=</mo><mn>4</mn></math>, has infinitely many solutions. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>P</mi><mi>Q</mi><msup><mo>)</mo><mn>2</mn></msup></math> is equal to _______.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **113**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>b</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>c</mi><mo>⇒</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>Now, on comparing above equation with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mi>y</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> we get,</p><p> The line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mi>y</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> passes through fixed point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi>P</mi><mo>=</mo><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo></math></p><p>Now, we know that for infinite solution,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd><mtd><mi>α</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>8</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>β</mi></mtd><mtd><mn>5</mn></mtd><mtd><mi>α</mi></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>⇒</mo><mi>β</mi><mo>=</mo><mn>6</mn></math></p><p>So, the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi></mrow></mfenced><mo>=</mo><mo>(</mo><mn>8</mn><mo>,</mo><mn>6</mn><mo>)</mo></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><msup><mi>Q</mi><mn>2</mn></msup><mo>=</mo><msup><mn>7</mn><mn>2</mn></msup><mo>+</mo><msup><mn>8</mn><mn>2</mn></msup><mo>=</mo><mn>49</mn><mo>+</mo><mn>64</mn><mo>=</mo><mn>113</mn></math></p>

</details>

---

### Q35. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8211;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>9</mn><mi>z</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>13</mn><mi>z</mi><mo>=</mo><mi>&#955;</mi></math></p><p>has a unique solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mi>&#947;</mi></math>. Then the distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi></mrow></mfenced></math> from the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>&#955;</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>System of linear equation,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8211;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>9</mn><mi>z</mi><mo>=</mo><mn>7</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8211;</mo><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>9</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8211;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>8</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>iii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8211;</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>13</mn><mi>z</mi><mo>=</mo><mi>&#955;</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>iv</mi></mfenced></math></p><p>Now solving, equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mi>iii</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>&#8211;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p>Now substituting in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>iv</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>=</mo><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>11</mn></math></p><p>Now finding the distance of Point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8211;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math> from the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>11</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mo>-</mo><mn>6</mn><mo>-</mo><mn>4</mn><mo>-</mo><mn>11</mn></mrow><msqrt><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mn>21</mn><mn>3</mn></mfrac><mo>=</mo><mn>7</mn></math></p></blockquote>

</details>

---

### Q36. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>If the system of equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>5</mn><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mi>&#956;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>7</mn></math>
has infinitely many solutions, then<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><msup><mo>)</mo><mn>2</mn></msup></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>904</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>916</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>912</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>920</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>916</mn></math>**

**Detailed Solution:**

<blockquote><p>Given system of equations.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>5</mn><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mi>&#956;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>7</mn></math></p><p>For infinite solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mn>0</mn><mo>=</mo><msub><mi>&#916;</mi><mn>1</mn></msub><mo>=</mo><msub><mi>&#916;</mi><mn>2</mn></msub><mo>=</mo><msub><mi>&#916;</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#916;</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>51</mn><mo>-</mo><mn>3</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#916;</mi><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>5</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#956;</mi></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>7</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>3</mn><mo>(</mo><mi>&#956;</mi><mo>+</mo><mn>13</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>13</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mn>17</mn><mo>+</mo><mn>13</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mn>17</mn><mo>-</mo><mn>13</mn><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>900</mn><mo>+</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>916</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q37. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>For the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>a</mi><mi>z</mi><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>8</mn></math></p><p>which of the following is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOT</mi></math> correct?</p>

**Options:**

- **(A)** <p>It has unique solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>b</mi><mo>=</mo><mn>6</mn></math></p>
- **(B)** <p>It has infinitely many solutions if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>6</mn></math></p>
- **(C)** <p>It has infinitely many solutions if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>8</mn></math></p>
- **(D)** <p>It has unique solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>b</mi><mo>=</mo><mn>8</mn></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <p>It has infinitely many solutions if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>6</mn></math></p>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>System of linear equations,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>a</mi><mi>z</mi><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>4</mn></math></p><p>Now finding,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>2</mn><mi>a</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#9651;</mo><mo>=</mo><mo>-</mo><mn>18</mn><mfenced><mrow><mi>a</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p>Hence, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mo>&#9651;</mo><mo>=</mo><mn>0</mn></math></p><p>Now finding,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#9651;</mo><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>b</mi></mtd><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>8</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mo>&#9651;</mo><mn>3</mn></msub><mo>=</mo><mn>9</mn><mfenced><mrow><mi>b</mi><mo>-</mo><mn>8</mn></mrow></mfenced></math></p><p>So, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><msub><mo>&#9651;</mo><mn>3</mn></msub><mo>=</mo><mn>0</mn></math></p><p>Now solving options we get,</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>8</mn></math> we&#39;ll have infinite solution</p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>8</mn><mo>,</mo><mi>b</mi><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mo>&#9651;</mo><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mo>&#9651;</mo><mn>3</mn></msub><mo>=</mo><mn>0</mn><mo>&#8658;</mo></math>unique solution</p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>b</mi><mo>=</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mo>&#9651;</mo><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mo>&#9651;</mo><mn>3</mn></msub><mo>&#8800;</mo><mn>0</mn><mo>&#8658;</mo></math> unique solution</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>b</mi><mo>=</mo><mn>6</mn></math> we&#39;ll have no solution</p></blockquote>

</details>

---

### Q38. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mi>x</mi><mo>+</mo><mn>11</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mn>13</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mi>&#946;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>175</mn><mi>x</mi><mo>+</mo><mn>194</mn><mi>y</mi><mo>+</mo><mn>57</mn><mi>z</mi><mo>=</mo><mn>361</mn></math>
has infinitely many solutions, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mn>2</mn></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p>Given,</p><p>System of linear equations,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mi>x</mi><mo>+</mo><mn>11</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mn>13</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mi>&#946;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>175</mn><mi>x</mi><mo>+</mo><mn>194</mn><mi>y</mi><mo>+</mo><mn>57</mn><mi>z</mi><mo>=</mo><mn>361</mn></math></p><p>Now we know that, for infinite solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>0</mn></math> we get,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>7</mn></mtd><mtd><mn>11</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>7</mn></mtd></mtr><mtr><mtd><mn>175</mn></mtd><mtd><mn>194</mn></mtd><mtd><mn>57</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now applying operation <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>-</mo><mn>25</mn><msub><mi>R</mi><mn>1</mn></msub></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>7</mn></mtd><mtd><mn>11</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>7</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>81</mn></mtd><mtd><mn>57</mn><mo>-</mo><mn>25</mn><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>81</mn><mo>(</mo><mn>49</mn><mo>-</mo><mn>5</mn><mi>&#945;</mi><mo>)</mo><mo>+</mo><mo>(</mo><mn>57</mn><mo>-</mo><mn>25</mn><mi>&#945;</mi><mo>)</mo><mo>(</mo><mo>-</mo><mn>27</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>270</mn><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>2430</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p>And now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>13</mn></mtd><mtd><mn>11</mn></mtd><mtd><mo>-</mo><mn>9</mn></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>4</mn></mtd><mtd><mn>7</mn></mtd></mtr><mtr><mtd><mn>361</mn></mtd><mtd><mn>194</mn></mtd><mtd><mn>57</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>13</mn><mfenced><mrow><mn>4</mn><mo>&#215;</mo><mn>57</mn><mo>-</mo><mn>7</mn><mo>&#215;</mo><mn>194</mn></mrow></mfenced><mo>-</mo><mi>&#946;</mi><mfenced><mrow><mn>11</mn><mo>&#215;</mo><mn>57</mn><mo>+</mo><mn>9</mn><mo>&#215;</mo><mn>194</mn></mrow></mfenced><mo>+</mo><mn>361</mn><mfenced><mrow><mn>11</mn><mo>&#215;</mo><mn>7</mn><mo>+</mo><mn>9</mn><mo>&#215;</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>13</mn><mfenced><mrow><mo>-</mo><mn>1130</mn></mrow></mfenced><mo>-</mo><mi>&#946;</mi><mfenced><mn>2373</mn></mfenced><mo>+</mo><mn>361</mn><mfenced><mn>113</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>13</mn><mfenced><mrow><mo>-</mo><mn>10</mn></mrow></mfenced><mo>-</mo><mi>&#946;</mi><mfenced><mn>21</mn></mfenced><mo>+</mo><mn>361</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>21</mn><mi>&#946;</mi><mo>=</mo><mn>231</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q39. JEE Main 2023 (10 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#955;</mi></math>, for which the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>&#955;</mi><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>4</mn><msup><mi>&#955;</mi><mn>2</mn></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>&#955;</mi><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>&#955;</mi><mi>z</mi><mo>=</mo><mi>&#955;</mi></math> has no solution. Then,<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><munder><mo>&#8721;</mo><mrow><mi>&#955;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mfenced open="|" close="|"><mi>&#955;</mi></mfenced></math> is equal to _______.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **24**

**Detailed Solution:**

<blockquote><p>Given,</p><p>System of equations,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>&#955;</mi><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>4</mn><msup><mi>&#955;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>&#955;</mi><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>&#955;</mi><mi>z</mi><mo>=</mo><mi>&#955;</mi></math></p><p>For no solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mo>=</mo><mn>0</mn></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>6</mn><mi>&#955;</mi></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>6</mn><mi>&#955;</mi></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><msup><mi>&#955;</mi><mn>3</mn></msup><mo>-</mo><mn>7</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></mrow></mfenced></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><munder><mo>&#8721;</mo><mrow><mi>&#955;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mfenced close="|" open="|"><mi>&#955;</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><munder><mo>&#8721;</mo><mrow><mi>&#955;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mo>=</mo><mn>12</mn><mo>&#215;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mn>24</mn></math></p></blockquote>

</details>

---

### Q40. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>For the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mi>&#946;</mi></math>,</p><p>which of the following is NOT correct?</p>

**Options:**

- **(A)** The system has infinitely many solutions for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>&#8211;</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>9</mn></math>
- **(B)** The system has infinitely many solutions for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>6</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>9</mn></math>
- **(C)** The system in inconsistent for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>&#8211;</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>8</mn></math>
- **(D)** The system has a unique solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8800;</mo><mo>&#8211;</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) The system has infinitely many solutions for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>6</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>9</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>For the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mi>&#946;</mi></math>,</p><p>Now finding,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>5</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>D</mi><mo>=</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mn>7</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>D</mi><mo>=</mo><mn>7</mn><mi>&#945;</mi><mo>+</mo><mn>35</mn></math></p><p>Now we know that, for unique solution<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#8800;</mo><mn>0</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>&#8800;</mo><mo>&#8211;</mo><mn>5</mn></math></p><p>So, in option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>&#8211;</mo><mn>6</mn></math> corresponds to infinitely many solution, which is completely wrong hence, this is answer.</p></blockquote>

</details>

---

### Q41. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mi>&#960;</mi><mo>,</mo><mi>&#960;</mi><mo>]</mo></math> for which the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><msqrt><mn>3</mn></msqrt><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>x</mi><mo>+</mo><mo>(</mo><mi>tan</mi><mi>&#952;</mi><mo>)</mo><mi>y</mi><mo>+</mo><msqrt><mn>7</mn></msqrt><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mo>(</mo><mi>tan</mi><mi>&#952;</mi><mo>)</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>
has non-trivial solution.Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>120</mn><mi>&#960;</mi></mfrac><munder><mo>&#8721;</mo><mrow><mn>0</mn><mo>&#8712;</mo><mi>S</mi></mrow></munder><mi>&#952;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mi>&#960;</mi><mo>,</mo><mi>&#960;</mi><mo>]</mo></math> for which the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><msqrt><mn>3</mn></msqrt><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>x</mi><mo>+</mo><mo>(</mo><mi>tan</mi><mi>&#952;</mi><mo>)</mo><mi>y</mi><mo>+</mo><msqrt><mn>7</mn></msqrt><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mo>(</mo><mi>tan</mi><mi>&#952;</mi><mo>)</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>
has non-trivial solution,</p><p>So, by condition of non-trivial solution we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><msqrt><mn>3</mn></msqrt></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>tan</mi><mi>&#952;</mi></mtd><mtd><msqrt><mn>7</mn></msqrt></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>tan</mi><mi>&#952;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><msqrt><mn>7</mn></msqrt></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mi>tan</mi><mi>&#952;</mi><mo>-</mo><msqrt><mn>7</mn></msqrt></mrow></mfenced><mo>+</mo><msqrt><mn>3</mn></msqrt><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mi>tan</mi><mi>&#952;</mi><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>tan</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>tan</mi><mi>&#952;</mi><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>,</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>120</mn><mi>&#960;</mi></mfrac><mo>&#8721;</mo><mi>&#952;</mi><mo>=</mo><mn>120</mn><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mn>20</mn></math></p></blockquote>

</details>

---

### Q42. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>For the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mi>&#946;</mi></math>, which one of the following is NOT true?</p>

**Options:**

- **(A)** System has no solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>24</mn></math>
- **(B)** System has a unique solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>14</mn></math>
- **(C)** System has infinitely many solutions for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>14</mn></math>
- **(D)** System has a unique solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>&#8800;</mo><mn>14</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) System has a unique solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>&#8800;</mo><mn>14</mn></math>**

**Detailed Solution:**

<blockquote><p>Given, the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mi>&#946;</mi></math></p><p>Now finding,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#9651;</mo><mo>=</mo><mn>1</mn><mfenced><mrow><mn>10</mn><mo>-</mo><mn>3</mn><mi>&#945;</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>5</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#9651;</mo><mo>=</mo><mn>6</mn><mo>-</mo><mn>2</mn><mi>&#945;</mi></math></p><p>Now for unique solution, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mo>&#8800;</mo><mn>0</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>&#8800;</mo><mn>3</mn></math></p><p>So, for unique solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>&#8800;</mo><mn>3</mn></math></p><p>But in option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>D</mi></mfenced></math>, system has unique solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn></math> which is completely wrong.</p></blockquote>

</details>

---

### Q43. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>If the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p>has infinitely many solutions, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>23</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>23</mn></math>**

**Detailed Solution:**

<blockquote><p>Given system of equations are</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mi>b</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>6</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>3</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>iii</mi></mfenced></math></p><p>It is given that the system of equations have infinite solutions.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mfenced><mrow><mn>15</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>6</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>a</mi><mfenced><mrow><mn>4</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>7</mn></math> </p><p>Also, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mo>&#8710;</mo><mn>1</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mi>b</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mfenced><mrow><mn>15</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>18</mn><mo>-</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mn>7</mn><mfenced><mrow><mn>12</mn><mo>-</mo><mn>15</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>a</mi><mo>=</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>3</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>14</mn><mo>+</mo><mn>9</mn><mo>=</mo><mn>23</mn></math></p><p>Hence, this is the correct option.</p></blockquote>

</details>

---

### Q44. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For the system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>a</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mi>&#946;</mi></math>, which one of the following statements is NOT correct?

**Options:**

- **(A)** It has infinitely many solutions if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>
- **(B)** It has no solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>1</mn></math>
- **(D)** It has infinitely many solutions if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) It has infinitely many solutions if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>For infinite solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><msub><mo>&#8710;</mo><mi>x</mi></msub><mo>=</mo><msub><mo>&#8710;</mo><mi>y</mi></msub><mo>=</mo><msub><mo>&#8710;</mo><mi>z</mi></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mi>&#945;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>1</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>1</mn></math>, then all planes are overlapping</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> option (d) is correct.</p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn></math> the system equations as,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p>Adding all three above equations we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> option (c) is correct.</p><p>Now, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn></math> then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mo>&#8710;</mo><mi>x</mi></msub><mo>&#8800;</mo><mn>0</mn></math>  (No solution)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> option (b) is correct.</p><p>Now, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>&#8800;</mo><mn>0</mn></math> (unique solution exists)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> option (a) is incorrect</p>

</details>

---

### Q45. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> denote the set of all real values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> such that the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>&#955;</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mn>1</mn></math>
is inconsistent, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>&#955;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mfenced><mrow><msup><mfenced open="|" close="|"><mi>&#955;</mi></mfenced><mn>2</mn></msup><mo>+</mo><mfenced open="|" close="|"><mi>&#955;</mi></mfenced></mrow></mfenced></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

<p>System of equations </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mspace linebreak="newline"></mspace><mi>x</mi><mo>+</mo><mi>&#955;</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mspace linebreak="newline"></mspace><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p>has no solution, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#955;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#955;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#955;</mi><mo>+</mo><mn>2</mn></mtd><mtd><mn>2</mn><mo>+</mo><mi>&#955;</mi></mtd><mtd><mn>2</mn><mo>+</mo><mi>&#955;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#955;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mi>&#955;</mi></mrow></mfenced><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#955;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mi>&#955;</mi></mrow></mfenced><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#955;</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>&#955;</mi><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mi>&#955;</mi></mrow></mfenced><msup><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>1</mn></math>, we get infinite solutions, since equation will be identical.</p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow></mrow><mrow></mrow></munderover><mfenced><mrow><msup><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mn>2</mn></msup><mo>+</mo><mfenced close="|" open="|"><mi>&#955;</mi></mfenced></mrow></mfenced><mo>=</mo><mn>4</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>6</mn></math> </p>

</details>

---

### Q46. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math> satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mi>&#947;</mi></mtd></mtr></mtable></mfenced><mfenced><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>10</mn></mtd><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mn>8</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>8</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable columnalign="left left left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math> lies on the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>5</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>&#945;</mi><mo>+</mo><mn>9</mn><mi>&#946;</mi><mo>+</mo><mn>7</mn><mi>&#947;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mi>&#947;</mi></mtd></mtr></mtable></mfenced><mfenced><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>10</mn></mtd><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mn>8</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>8</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable columnalign="left left left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mtable><mtr><mtd><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>9</mn><mi>&#946;</mi><mo>+</mo><mn>8</mn><mi>&#947;</mi></mtd><mtd><mn>10</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn><mi>&#946;</mi><mo>+</mo><mn>4</mn><mi>&#947;</mi></mtd><mtd><mn>8</mn><mi>&#945;</mi><mo>+</mo><mn>8</mn><mi>&#946;</mi><mo>+</mo><mn>8</mn><mi>&#947;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable columnalign="left left left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Now on comparing both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>8</mn><mi>&#947;</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn><mi>&#946;</mi><mo>+</mo><mn>4</mn><mi>&#947;</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>&#945;</mi><mo>+</mo><mn>8</mn><mi>&#946;</mi><mo>+</mo><mn>8</mn><mi>&#947;</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>3</mn></mfenced></math></p><p>Now from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> by cross multiplication we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>&#946;</mi><mn>6</mn></mfrac><mo>=</mo><mfrac><mi>&#947;</mi><mrow><mo>-</mo><mn>7</mn></mrow></mfrac><mo>=</mo><mi>k</mi><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mi>k</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>6</mn><mi>k</mi><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><mn>7</mn><mi>k</mi></math></p><p>Point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math> lie on the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>5</mn><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>4</mn><mi>&#946;</mi><mo>+</mo><mn>3</mn><mi>&#947;</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>k</mi><mo>+</mo><mn>24</mn><mi>k</mi><mo>-</mo><mn>21</mn><mi>k</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>&#945;</mi><mo>+</mo><mn>9</mn><mi>&#946;</mi><mo>+</mo><mn>7</mn><mi>&#947;</mi><mo>=</mo><mn>6</mn><mi>k</mi><mo>+</mo><mn>54</mn><mi>k</mi><mo>-</mo><mn>49</mn><mi>k</mi><mo>=</mo><mn>11</mn><mi>k</mi><mo>=</mo><mn>11</mn></math>.</p>

</details>

---

### Q47. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>For the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>+</mo><mi>&#946;</mi><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>14</mn></math>
which of the following is NOT true ?</p>

**Options:**

- **(A)** If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mi>&#946;</mi><mo>=</mo><mn>7</mn></math>, then the system has no solution
- **(B)** If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mi>&#946;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8800;</mo><mn>7</mn></math> then the system has a unique solution.
- **(C)** There is a unique point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>)</mo></math> on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>18</mn><mo>=</mo><mn>0</mn></math> for which the system has infinitely many solutions
- **(D)** For every point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>)</mo><mo>&#8800;</mo><mo>(</mo><mn>7</mn><mo>,</mo><mn>7</mn><mo>)</mo></math> on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">y</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>0</mn></math>, the system has infinitely many solutions.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) For every point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>)</mo><mo>&#8800;</mo><mo>(</mo><mn>7</mn><mo>,</mo><mn>7</mn><mo>)</mo></math> on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">y</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>0</mn></math>, the system has infinitely many solutions.**

**Detailed Solution:**

<p>Given system of linear equations:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>+</mo><mi>&#946;</mi><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>14</mn></math></p><p>On taking determinant, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mn>7</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mn>3</mn><mi>&#946;</mi><mo>-</mo><mn>14</mn><mo>)</mo><mo>-</mo><mo>(</mo><mn>3</mn><mi>&#945;</mi><mo>-</mo><mn>7</mn><mo>)</mo><mo>+</mo><mo>(</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>7</mn></math></p><p>Here, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mi>&#946;</mi><mo>=</mo><mn>7</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mn>0</mn></math> and the system has no solution. So, option A is correct.</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>&#8800;</mo><mn>7</mn></math> then the system has a unique solution. So, option B is correct.</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>)</mo><mo>&#8800;</mo><mo>(</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>)</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>&#8800;</mo><mn>0</mn></math>. So, system has not infinitely many solution. Therefore, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> is false.</p>

</details>

---

### Q48. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>, suppose the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>5</mn></math> 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mn>8</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mi>&#946;</mi></math></p><p>has infinitely many solutions. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are the roots of </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>16</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>18</mn><mi>x</mi><mo>+</mo><mn>56</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>18</mn><mi>x</mi><mo>+</mo><mn>56</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>14</mn><mi>x</mi><mo>+</mo><mn>24</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>18</mn><mi>x</mi><mo>+</mo><mn>56</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>, suppose the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>5</mn></math> 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mn>8</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mi>&#946;</mi></math></p><p>has infinitely many solutions,</p><p>So, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mo>+</mo><mi>&#945;</mi><mo>-</mo><mn>2</mn><mo>(</mo><mo>-</mo><mn>4</mn><mo>+</mo><mn>1</mn><mo>)</mo><mo>+</mo><mn>3</mn><mo>(</mo><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mo>+</mo><mi>&#945;</mi><mo>+</mo><mn>6</mn><mo>-</mo><mn>3</mn><mi>&#945;</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>4</mn></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#9651;</mo><mi>z</mi></msub><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mfenced><mrow><mo>-</mo><mn>18</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>&#946;</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>14</mn></math></p><p>Hence, quadratic equation having roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mo>&#38;</mo><mn>14</mn><mo>&#160;</mo></math> will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mn>4</mn><mo>+</mo><mn>14</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>14</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>18</mn><mi>x</mi><mo>+</mo><mn>56</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q49. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>k</mi><mi>z</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mi>k</mi></math></p><p>have infinitely many solutions. Then the system</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mi>x</mi><mo>+</mo><mfenced><mrow><mn>2</mn><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced close="|" open="|"><mrow><mi>k</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mi>y</mi><mo>=</mo><mn>10</mn></math> has :</p>

**Options:**

- **(A)** infinitely many solutions
- **(B)** unique solution satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>1</mn></math>
- **(C)** no solution
- **(D)** unique solution satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) unique solution satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>k</mi><mi>z</mi><mo>=</mo><mn>2</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mi>k</mi></math> have infinitely many solutions.</p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>k</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mfenced><mn>10</mn></mfenced><mo>-</mo><mn>1</mn><mfenced><mn>7</mn></mfenced><mo>+</mo><mi>k</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mo>-</mo><mn>7</mn><mo>-</mo><mi>k</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>-</mo><mi>k</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>3</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>3</mn></math>, the second system of equations is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>=</mo><mn>7</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mi>x</mi><mo>+</mo><mn>8</mn><mi>y</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Clearly, they have a unique solution</p><p>Subtracting <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q50. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Consider the following system of questions</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>&#945;</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mi>&#946;</mi></math></p><p>For some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. Then which of the following is NOT correct.</p>

**Options:**

- **(A)** It has no solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#8800;</mo><mn>2</mn></math>
- **(B)** It has no solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>
- **(C)** It has no solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn></math> and for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#8800;</mo><mn>2</mn></math>
- **(D)** It has a solution for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8800;</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) It has no solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>**

**Detailed Solution:**

<p>Given,</p><p>System of questions</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>&#945;</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mi>&#946;</mi></math></p><p>Now finding, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>&#945;</mi></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>(</mo><mn>6</mn><mo>-</mo><mi>&#945;</mi><mo>)</mo><mo>-</mo><mn>2</mn><mo>(</mo><mn>4</mn><mi>&#945;</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>+</mo><mn>1</mn><mo>(</mo><mn>2</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>(</mo><mi>&#945;</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>x</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>2</mn></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mo>(</mo><mn>3</mn><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi><mo>)</mo><mo>+</mo><mo>(</mo><mn>6</mn><mo>-</mo><mi>&#945;</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>y</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>(</mo><mi>&#946;</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>-</mo><mn>1</mn><mo>(</mo><mn>2</mn><mi>&#945;</mi><mi>&#946;</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>+</mo><mn>1</mn><mo>(</mo><mn>4</mn><mi>&#945;</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>(</mo><mn>2</mn><mo>-</mo><mi>&#946;</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>z</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>&#945;</mi></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> the system of equations will have infinite solutions,</p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn></math> the system has infinite solution,</p><p>And when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>&#8800;</mo><mn>2</mn></math> the system has no solution as <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>x</mi></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>D</mi><mi>y</mi></msub><mo>&#8800;</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#8800;</mo><mn>2</mn></math>,</p><p>Hence, only option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> is not correct</p>

</details>

---

### Q51. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> be respectively the sets of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mn>0</mn></mfenced></math> for which the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>a</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>a</mi><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mi>x</mi><mo>+</mo><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mi>y</mi><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>z</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mi>a</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>&#160;</mo><mi>x</mi><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>&#160;</mo><mi>y</mi><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p>has unique solution and infinitely many solutions. Then</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mfenced><msub><mi>S</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> is an infinite set
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> is an infinite set an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><msub><mi>S</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mi>&#981;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mi mathvariant="normal">&#8477;</mi><mo>-</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mi mathvariant="normal">&#8477;</mi><mo>-</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mi>&#981;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mi mathvariant="normal">&#8477;</mi><mo>-</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mi>&#981;</mi></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> be respectively the sets of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mn>0</mn></mfenced></math> for which the system of linear equations</p><p>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>a</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>a</mi><mi>z</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mi>x</mi><mo>+</mo><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mi>y</mi><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>z</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mi>a</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>&#160;</mo><mi>x</mi><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>&#160;</mo><mi>y</mi><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>Now from above equations finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mn>2</mn><mi>a</mi></mtd><mtd><mo>-</mo><mn>3</mn><mi>a</mi></mtd></mtr><mtr><mtd><mn>2</mn><mi>a</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn></mtd><mtd><mi>a</mi><mo>+</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn><mi>a</mi><mo>+</mo><mn>5</mn></mtd><mtd><mi>a</mi><mo>+</mo><mn>5</mn></mtd><mtd><mi>a</mi><mo>+</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>a</mi><mfenced><mrow><mn>15</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>31</mn><mi>a</mi><mo>+</mo><mn>36</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>0</mn></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>31</mn><mi>a</mi><mo>+</mo><mn>36</mn></math> cannot be zero as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>31</mn><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>15</mn><mo>&#215;</mo><mn>36</mn><mo>&#60;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>&#8800;</mo><mn>0</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mn>0</mn></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mn>0</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mi>&#981;</mi></math></p>

</details>

---

### Q52. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>If the system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>3</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mn>9</mn><mo>+</mo><mi>&#956;</mi></math> has infinitely many solutions, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#955;</mi><mo>,</mo><mi>&#956;</mi></mrow></mfenced></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>72</mn><mn>5</mn></mfrac><mo>,</mo><mfrac><mn>21</mn><mn>5</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>72</mn></mrow><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>21</mn></mrow><mn>5</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>72</mn><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>21</mn></mrow><mn>5</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>72</mn></mrow><mn>5</mn></mfrac><mo>,</mo><mfrac><mn>21</mn><mn>5</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>72</mn><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>21</mn></mrow><mn>5</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p>The system of equations </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mn>9</mn><mo>+</mo><mi>&#956;</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>Now using the operation, equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#215;</mo><mn>4</mn><mo>-</mo><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>y</mi><mo>+</mo><mn>16</mn><mi>z</mi><mo>=</mo><mn>8</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>Now using the operation, equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>&#215;</mo><mn>2</mn><mo>-</mo><mfenced><mn>3</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mo>+</mo><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>8</mn></mrow></mfenced><mi>z</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>-</mo><mi>&#956;</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>5</mn></mfenced></math></p><p>Now using the operation, equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced><mo>&#215;</mo><mn>2</mn><mo>-</mo><mfenced><mn>3</mn></mfenced><mo>&#215;</mo><mn>5</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>72</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi></mrow></mfenced><mi>z</mi><mo>=</mo><mn>21</mn><mo>+</mo><mn>5</mn><mi>&#956;</mi></math></p><p>Now given system of equation has infinitely many solutions, so making coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> to be zero and equating <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn><mo>+</mo><mn>5</mn><mi>&#956;</mi></math> with zero we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mn>72</mn><mn>5</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn><mo>+</mo><mn>5</mn><mi>&#956;</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>21</mn></mrow><mn>5</mn></mfrac></math></p><p>Hence, the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#955;</mi><mo>,</mo><mi>&#956;</mi></mrow></mfenced></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>72</mn><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>21</mn></mrow><mn>5</mn></mfrac></mrow></mfenced></math>.</p>

</details>

---

### Q53. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> denote the number that turns up when a fair die is rolled. If the probability that the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mspace linebreak="newline"/><mn>2</mn><mi>x</mi><mo>+</mo><mi>N</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>2</mn><mspace linebreak="newline"/><mn>3</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>N</mi><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p>has unique solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>k</mi><mn>6</mn></mfrac><mo>,</mo></math> then the sum of value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> and all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>**

**Detailed Solution:**

<p>Given equations are</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mspace linebreak="newline"/><mn>2</mn><mi>x</mi><mo>+</mo><mi>N</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>2</mn><mspace linebreak="newline"/><mn>3</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>N</mi><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>N</mi></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>N</mi></mtd></mtr></mtable></mfenced></math></p><p>Applying <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub><mo>&#8596;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>-</mo><msub><mi>C</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>3</mn></msub><mo>&#8596;</mo><msub><mi>C</mi><mn>3</mn></msub><mo>-</mo><msub><mi>C</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>N</mi><mo>-</mo><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>N</mi><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mo>=</mo><mfenced><mrow><mi>N</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>N</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p>For unique solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>&#8800;</mo><mn>0</mn></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>&#8800;</mo><mn>2</mn><mo>,</mo><mn>3</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math> and for unique solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> can take values <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi></math>(system has unique solution ) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>4</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mi>k</mi><mn>6</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>4</mn></math></p><p>Therefore, required sum is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>6</mn><mo>=</mo><mn>20</mn></math></p>

</details>

---

### Q54. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>If the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>14</mn></math></p><p>has infinitely many solutions, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>44</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>44</mn></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mi>&#946;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>14</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>For infinite solution </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>15</mn><mo>-</mo><mn>2</mn><mi>&#945;</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>6</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>4</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mo>-</mo><mi>&#945;</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>8</mn></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd><mtd><mi>&#946;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>14</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>70</mn><mo>-</mo><mn>2</mn><mi>&#946;</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>28</mn><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mn>6</mn><mfenced><mrow><mn>4</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>36</mn><mo>-</mo><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>44</mn></math></p></blockquote>

</details>

---

### Q55. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>If the system of linear equations.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>=</mo><mi>&#956;</mi></math></p><p>has infinitely many solutions, then the distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#955;</mi><mo>,</mo><mi>&#956;</mi><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math> from the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>5</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>26</mn><mn>9</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given the system of linear equations.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>=</mo><mi>&#956;</mi></math></p><p>has infinitely many solutions, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>8</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#955;</mi></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>4</mn></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#956;</mi></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mo>-</mo><mn>6</mn><mo>-</mo><mn>3</mn><mi>&#956;</mi><mo>=</mo><mn>0</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Hence the point will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Now distance of point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math> from plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>32</mn><mo>-</mo><mn>2</mn><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn></mrow><msqrt><msup><mn>8</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup></msqrt></mfrac></mfenced><mo>=</mo><mfenced close="|" open="|"><mfrac><mn>30</mn><mn>9</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>10</mn><mn>3</mn></mfrac></math></p></blockquote>

</details>

---

### Q56. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The number of real values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math>, such that the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mfenced><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mfenced close="|" open="|"><mi>&#955;</mi></mfenced></mrow></mfenced><mi>z</mi><mo>=</mo><mn>16</mn></math> has no solutions, is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>For the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mfenced><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mfenced close="|" open="|"><mi>&#955;</mi></mfenced></mrow></mfenced><mi>z</mi><mo>=</mo><mn>16</mn></math> to have no solutions, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo></math> should be equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>.</p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mfenced close="|" open="|"><mi>&#955;</mi></mfenced></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mn>3</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>5</mn><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mn>9</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mo>-</mo><mn>43</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><msup><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mn>2</mn></msup><mo>-</mo><mn>9</mn><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mo>-</mo><mn>43</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>&#955;</mi></mfenced></math> as for the above quadratic the value of determinant is greater than zero.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> satisfy the system of equations to obtain no solution.</p></blockquote>

</details>

---

### Q57. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>4</mn><mi>&#960;</mi></mrow></mfenced></math> for which the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mrow></mfenced><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>x</mi><mo>+</mo><mn>7</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>9</mn></math> has no solution is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<blockquote><p>The number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>4</mn><mi>&#960;</mi></mrow></mfenced></math> for which the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mrow></mfenced><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>x</mi><mo>+</mo><mn>7</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>9</mn></math> has no solution is :</p><p>We know that for the system of equation has no solution,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mtd><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>7</mn></mtd><mtd><mn>7</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>21</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi><mo>+</mo><mn>42</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>42</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mn>3</mn><mi>&#952;</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>-</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mi>sin</mi><mn>3</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>3</mn><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mn>4</mn><msup><mi>sin</mi><mn>3</mn></msup><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mfenced><mrow><mn>4</mn><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mn>3</mn><mo>+</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mn>3</mn><mo>+</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mi mathvariant="normal">&#960;</mi><mo>,</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mo>,</mo><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mn>3</mn><mo>+</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>&#177;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> (ignoring negative sign as it will not lie in range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#952;</mi></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>13</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>17</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced></math></p><p>So, total number of solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>4</mn><mi>&#960;</mi></mrow></mfenced></math></p></blockquote>

</details>

---

### Q58. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>7</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mi>&#948;</mi><mi>z</mi><mo>=</mo><mi>k</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#948;</mi><mo>,</mo><mi>k</mi><mo>&#8712;</mo><mi>R</mi></math>
has infinitely many solutions, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#948;</mi><mo>+</mo><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>For infinitely many solutions, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd><mtd><mi>&#948;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#948;</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>1</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable columnalign="center center right"><mtr><mtd><mn>7</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi>K</mi></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#948;</mi><mo>+</mo><mi>K</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q59. JEE Main 2022 (28 Jun Shift 2)

*Type:* `numerical` | *Level:* `1`

If the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>=</mo><mi>&#947;</mi><mo>+</mo><mn>5</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>=</mo><mi>&#946;</mi><mo>+</mo><mn>1</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi><mo>&#8712;</mo><mi mathvariant="bold">R</mi></math> has infinitely many solutions, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mn>9</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn><mi>&#946;</mi><mo>+</mo><mn>5</mn><mi>&#947;</mi></mrow></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **58**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>=</mo><mi>&#947;</mi><mo>+</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>=</mo><mi>&#946;</mi><mo>+</mo><mn>1</mn></math></p><p>Has infinite many solutions</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>&#946;</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>&#947;</mi><mo>+</mo><mn>5</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>10</mn></mrow><mn>3</mn></mfrac><mo>,</mo><mo>&#160;&#160;</mo><mn>5</mn><mi>&#947;</mi><mo>+</mo><mn>25</mn><mo>=</mo><mo>-</mo><mn>3</mn><mi>&#946;</mi><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>30</mn><mo>,</mo><mo>&#160;&#160;</mo><mn>3</mn><mi>&#946;</mi><mo>+</mo><mn>5</mn><mi>&#947;</mi><mo>=</mo><mo>-</mo><mn>28</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn><mi>&#946;</mi><mo>+</mo><mn>5</mn><mi>&#947;</mi><mo>=</mo><mo>-</mo><mn>58</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mn>9</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn><mi>&#946;</mi><mo>+</mo><mn>5</mn><mi>&#947;</mi></mrow></mfenced><mo>=</mo><mn>58</mn></math></p>

</details>

---

### Q60. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>If the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mi>z</mi><mo>=</mo><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>4</mn></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>,</p><p>has no solution, then</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>7</mn></math>**

**Detailed Solution:**

<p>If we have three equations in three variables, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><mi>z</mi><mo>=</mo><msub><mi>d</mi><mn>1</mn></msub><mspace linebreak="newline"></mspace><msub><mi>a</mi><mn>2</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mi>z</mi><mo>=</mo><msub><mi>d</mi><mn>2</mn></msub><mspace linebreak="newline"></mspace><msub><mi>a</mi><mn>3</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>3</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mi>z</mi><mo>=</mo><msub><mi>d</mi><mn>3</mn></msub><mspace linebreak="newline"></mspace></math></p><p>then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math>,<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>d</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>d</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>d</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math>,<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>d</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>d</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>d</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math>,<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>d</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>d</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>d</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math>.</p><p>If the set of equations do not have a solution then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mn>0</mn></math> and at least one among <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>1</mn></msub><mo>,</mo><msub><mo>&#8710;</mo><mn>2</mn></msub><mo>,</mo><msub><mo>&#8710;</mo><mn>3</mn></msub></math> is not equal to zero.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mfenced close="|" open="|"><mi>&#955;</mi></mfenced></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mo>=</mo><mn>7</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>&#177;</mo><mn>7</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Case 1: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>7</mn></math></p><p>The system of equations are </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>2</mn><mspace linebreak="newline"></mspace><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>4</mn><mspace linebreak="newline"></mspace><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>b</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>-</mo><mn>24</mn></mrow></mfenced></math></p><p>Comparing the coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>1</mn><mspace linebreak="newline"></mspace><mn>3</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>5</mn></math></p><p>For these values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>, coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> and the constant values are matching. So the set of equations will have infinitely many solutions.</p><p>Case 2: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>7</mn></math></p><p>The system of equations are </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>2</mn><mspace linebreak="newline"></mspace><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>4</mn><mspace linebreak="newline"></mspace><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mn>7</mn><mi>z</mi><mo>=</mo><mo>-</mo><mn>32</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>b</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mn>7</mn><mi>z</mi><mo>+</mo><mn>32</mn></mrow></mfenced></math></p><p>Comparing the coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>1</mn><mspace linebreak="newline"></mspace><mn>3</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>5</mn></math></p><p>For these values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>, coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> and the constant values are not matching. So the set of equations will have no solutions.</p>

</details>

---

### Q61. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>2</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mi>&#945;</mi><mo>,</mo><mo>-</mo><mi>&#945;</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mo>-</mo><mi>&#945;</mi></math> be inconsistent. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, the system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>2</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mi>&#945;</mi><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#945;</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mo>-</mo><mi>&#945;</mi></math> </p><p>Now for system to be inconsistent, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mtext>either&#160;of&#160;</mtext><mo>&#160;</mo><msub><mo>&#8710;</mo><mn>1</mn></msub><mo>,</mo><msub><mo>&#8710;</mo><mn>2</mn></msub><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><msub><mo>&#8710;</mo><mn>3</mn></msub><mo>&#160;</mo><mo>&#8800;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>6</mn><mo>+</mo><mi mathvariant="normal">y</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>&#945;</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>3</mn><mi>&#945;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>4</mn><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mo>+</mo><mn>2</mn><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></math></p><p>Now calculating, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>14</mn><mo>+</mo><mn>2</mn><mi>&#945;</mi></math></p><p>Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></math> so, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>1</mn></msub><mo>=</mo><mn>14</mn><mo>-</mo><mn>7</mn><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>1</mn></msub><mo>&#8800;</mo><mn>0</mn></math>, hence system is inconsistent at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>7</mn></mrow><mn>2</mn></mfrac></math></p>

</details>

---

### Q62. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>5</mn><mo>,</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>4</mn><mo>,</mo><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mi>&#946;</mi></math>. Has infinitely many solutions, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>We know that, for infinitely many solutions,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mn>0</mn><mo>=</mo><msub><mi>&#916;</mi><mi>x</mi></msub><mo>=</mo><msub><mi>&#916;</mi><mi>y</mi></msub><mo>=</mo><msub><mi>&#916;</mi><mi>z</mi></msub></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mfenced><mrow><mn>10</mn><mo>-</mo><mn>9</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>5</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>-</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn></math></p><p>Now checking for <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mi>x</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>5</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mfenced><mrow><mn>10</mn><mo>-</mo><mn>9</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>20</mn><mo>-</mo><mn>3</mn><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mn>12</mn><mo>-</mo><mn>2</mn><mi>&#946;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mo>-</mo><mn>20</mn><mo>+</mo><mn>3</mn><mi>&#946;</mi><mo>+</mo><mn>12</mn><mo>-</mo><mn>2</mn><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>3</mn><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>3</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p>

</details>

---

### Q63. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math>, for which the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>x</mi><mo>-</mo><mn>8</mn><mi>y</mi><mo>+</mo><mn>9</mn><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>
has no solution, is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given system of linear equations are
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>x</mi><mo>-</mo><mn>8</mn><mi>y</mi><mo>+</mo><mn>9</mn><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>For system to have no solution, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mo>-</mo><mn>8</mn></mtd><mtd><mn>9</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mfenced><mrow><mo>-</mo><mn>8</mn><mi>a</mi><mo>-</mo><mn>9</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>5</mn><mi>a</mi><mo>-</mo><mn>18</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mn>21</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>2</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mo>-</mo><mn>8</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>3</mn><mfenced><mn>5</mn></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>11</mn></mrow></mfenced><mo>+</mo><mi>b</mi><mfenced><mn>21</mn></mfenced><mo>=</mo><mn>21</mn><mi>b</mi><mo>-</mo><mn>7</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>2</mn></msub><mo>=</mo><mn>0</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> must be equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q64. JEE Main 2022 (25 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The system of equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>k</mi><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>14</mn><mi>z</mi><mo>=</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>15</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mi>k</mi><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>4</mn></math></p><p>Question: is consistent for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> in the set</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>11</mn><mo>,</mo><mn>13</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>13</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>11</mn><mo>,</mo><mn>11</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>11</mn><mo>,</mo><mn>11</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>For consistent solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mo>-</mo><mi>k</mi></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>14</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>15</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mi>k</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>-</mo><mi>k</mi><mfenced><mrow><mn>12</mn><mo>+</mo><mi>k</mi></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced><mrow><mo>-</mo><mn>45</mn><mo>-</mo><mn>4</mn><mi>k</mi></mrow></mfenced><mo>-</mo><mn>14</mn><mfenced><mrow><mo>-</mo><mn>15</mn><mo>+</mo><mn>16</mn></mrow></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>-</mo><mn>12</mn><mi>k</mi><mo>-</mo><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>135</mn><mo>+</mo><mn>12</mn><mi>k</mi><mo>-</mo><mn>14</mn><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>&#8800;</mo><mn>121</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>k</mi><mo>&#8800;</mo><mn>11</mn><mo>,</mo><mo>-</mo><mn>11</mn></math></p>

</details>

---

### Q65. JEE Main 2022 (25 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> real matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>;</mo><mi>A</mi><mfenced><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><msup><mfenced open="[" close="]"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi>x</mi><mn>3</mn></msub></mrow></mfenced><mi>T</mi></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> is an identity matrix of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>, then the system <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>A</mi><mo>-</mo><mn>2</mn><mi>I</mi></mrow></mfenced><mi>X</mi><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> has

**Options:**

- **(A)** no solution
- **(B)** infinitely many solutions
- **(C)** unique solution
- **(D)** exactly two solutions

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) infinitely many solutions**

**Detailed Solution:**

<p>Let the matrix be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msub><mi>c</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi>c</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi>c</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>c</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>c</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>c</mi><mn>3</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><msub><mi>b</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><msub><mi>b</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><msub><mi>b</mi><mn>3</mn></msub><mo>=</mo><mn>1</mn></math></p><p>So matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>-</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>A</mi><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>I</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>x</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>x</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>x</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;&#160;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>x</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>x</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>x</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>Solving the above system of equations we get infinite solutions.</p>

</details>

---

### Q66. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>1</mn></math>
have a unique solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi></msup><mo>,</mo><msup><mi>y</mi></msup><mo>,</mo><msup><mi>z</mi></msup></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><msup><mi>x</mi></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><msup><mi>y</mi></msup><mo>,</mo><mi>&#945;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi></msup><mo>,</mo><mo>-</mo><msup><mi>y</mi></msup></mrow></mfenced></math> are collinear points, then the sum of absolute values of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Given,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>1</mn></math>
Now finding,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left left right"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8800;</mo><mo>-</mo><mn>3</mn><mo>,</mo><mi>x</mi><mo>=</mo><mfrac><msub><mo>&#9651;</mo><mn>1</mn></msub><mo>&#9651;</mo></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><mi>y</mi><mo>=</mo><mfrac><msub><mo>&#9651;</mo><mn>2</mn></msub><mo>&#9651;</mo></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><mi>z</mi><mo>=</mo><mfrac><msub><mo>&#9651;</mo><mn>3</mn></msub><mo>&#9651;</mo></mfrac><mo>=</mo><mn>0</mn><mo>,</mo></math></p><p>Now points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mi>&#945;</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> are collinear</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mi>&#945;</mi><mo>-</mo><mn>1</mn><mo>-</mo><mi>&#945;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mn>1</mn></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q67. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The number of values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> for which the system of equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>&#945;</mi><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>&#945;</mi><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>4</mn></math></p><p>is inconsistent, is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given linear equations are </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>&#945;</mi><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>&#945;</mi><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>4</mn></math></p><p>For this system of linear equations to have inconsistent solution</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>2</mn><mi>&#945;</mi></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn><mi>&#945;</mi></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>10</mn><mo>-</mo><mn>9</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mn>5</mn><mo>-</mo><mn>12</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mo>-</mo><mn>3</mn><mo>-</mo><mn>8</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>17</mn><mo>-</mo><mn>11</mn><mo>&#8800;</mo><mn>0</mn></math></p><p>Hence, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn></math> the system of equation has inconsistent solution.</p>

</details>

---

### Q68. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Consider the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mi>a</mi><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mi>a</mi><mi>z</mi><mo>=</mo><mn>7</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> be the set of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>R</mi></math> for which the system is inconsistent and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> be the set of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>R</mi></math> for which the system has infinitely many solutions. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>1</mn></msub></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>2</mn></msub></mfenced></math> denote the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">S</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">S</mi><mn>2</mn></msub></math> respectively, then</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>For system to be inconsistent <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mi>a</mi></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi>a</mi><mo>+</mo><mn>12</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>x</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>a</mi></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>7</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>15</mn><mi>a</mi><mo>+</mo><mn>31</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">D</mi><mi>x</mi></msub><mo>&#8800;</mo><mn>0</mn><mtext>&#160;for&#160;</mtext><mi mathvariant="normal">a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mn>4</mn></math></p><p>Similarly we can show <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">D</mi><mi>y</mi></msub><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi mathvariant="normal">D</mi><mi>z</mi></msub><mo>&#8800;</mo><mn>0</mn><mtext>&#160;for&#160;</mtext><mi mathvariant="normal">a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mn>4</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>2</mn></math></p><p>Now for infinitely many solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo></math>also <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">D</mi><mi mathvariant="normal">x</mi></msub><mo>=</mo><msub><mi mathvariant="normal">D</mi><mi mathvariant="normal">y</mi></msub><mo>=</mo><msub><mi mathvariant="normal">D</mi><mi>z</mi></msub><mo>=</mo><mn>0</mn></math> which is not possible value of any real of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">a</mi></math>, since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>D</mi><mi>x</mi></msub><mo>=</mo><mn>0</mn></math> have different solutions for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>0</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi mathvariant="normal">n</mi><mfenced><msub><mi mathvariant="normal">S</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q69. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>2</mn><mi>&#960;</mi><mo>,</mo></math> then the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mfenced><mrow><mi>cos</mi><mi>&#947;</mi></mrow></mfenced><mi>y</mi><mo>+</mo><mfenced><mrow><mi>cos</mi><mi>&#946;</mi></mrow></mfenced><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>cos</mi><mi>&#947;</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mfenced><mrow><mi>cos</mi><mi>&#945;</mi></mrow></mfenced><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>cos</mi><mi>&#946;</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced><mrow><mi>cos</mi><mi>&#945;</mi></mrow></mfenced><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p>has :</p>

**Options:**

- **(A)** infinitely many solutions
- **(B)** a unique solution
- **(C)** no solution
- **(D)** exactly two solutions

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) infinitely many solutions**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>2</mn><mi>&#960;</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>cos</mi><mi>&#947;</mi></mtd><mtd><mi>cos</mi><mi>&#946;</mi></mtd></mtr><mtr><mtd><mi>cos</mi><mi>&#947;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>cos</mi><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>cos</mi><mi>&#946;</mi></mtd><mtd><mi>cos</mi><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>By expanding along the first column, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mn>1</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#945;</mi></mrow></mfenced><mo>-</mo><mi>cos</mi><mi>&#947;</mi><mfenced><mrow><mi>cos</mi><mi>&#947;</mi><mo>-</mo><mi>cos</mi><mi>&#945;</mi><mo>.</mo><mi>cos</mi><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mi>cos</mi><mi>&#946;</mi><mfenced><mrow><mi>cos</mi><mi>&#945;</mi><mo>.</mo><mi>cos</mi><mi>&#947;</mi><mo>-</mo><mi>cos</mi><mi>&#946;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#945;</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#947;</mi><mo>+</mo><mi>cos</mi><mi>&#947;</mi><mo>.</mo><mi>cos</mi><mi>&#945;</mi><mo>.</mo><mi>cos</mi><mi>&#946;</mi><mo>+</mo><mi>cos</mi><mi>&#946;</mi><mo>.</mo><mi>cos</mi><mi>&#945;</mi><mo>.</mo><mi>cos</mi><mi>&#947;</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#945;</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#946;</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#947;</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>&#945;</mi><mo>.</mo><mi>cos</mi><mi>&#946;</mi><mo>.</mo><mi>cos</mi><mi>&#947;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#945;</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#946;</mi><mo>-</mo><mi>cos</mi><mi>&#947;</mi><mo>(</mo><mi>cos</mi><mi>&#947;</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mi>&#945;</mi><mo>.</mo><mi>cos</mi><mi>&#946;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mi>cos</mi><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo><mo>.</mo><mi>cos</mi><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo><mo>-</mo><mi>cos</mi><mi>&#947;</mi><mfenced close="]" open="["><mrow><mi>cos</mi><mfenced close="}" open="{"><mrow><mn>2</mn><mi>&#960;</mi><mo>-</mo><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo></mrow></mfenced><mo>-</mo><mn>2</mn><mi>cos</mi><mi>&#945;</mi><mo>.</mo><mi>cos</mi><mi>&#946;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mi>cos</mi><mo>(</mo><mn>2</mn><mi>&#960;</mi><mo>-</mo><mi>&#947;</mi><mo>)</mo><mi>cos</mi><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo><mo>-</mo><mi>cos</mi><mi>&#947;</mi><mfenced close="]" open="["><mrow><mi>cos</mi><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo><mo>-</mo><mn>2</mn><mi>cos</mi><mi>&#945;</mi><mo>.</mo><mi>cos</mi><mi>&#946;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mi>cos</mi><mo>(</mo><mn>2</mn><mi>&#960;</mi><mo>-</mo><mi>&#947;</mi><mo>)</mo><mo>.</mo><mi>cos</mi><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo><mo>-</mo><mi>cos</mi><mi>&#947;</mi><mfenced close="]" open="["><mrow><mi>cos</mi><mi>&#945;</mi><mo>.</mo><mi>cos</mi><mi>&#946;</mi><mo>-</mo><mi>sin</mi><mi>&#945;</mi><mo>.</mo><mi>sin</mi><mi>&#946;</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mi>&#945;</mi><mo>.</mo><mi>cos</mi><mi>&#946;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mi>cos</mi><mi>&#947;</mi><mo>.</mo><mi>cos</mi><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo><mo>+</mo><mi>cos</mi><mi>&#947;</mi><mo>.</mo><mi>cos</mi><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mn>0</mn></math></p><p>Hence, the system of equations has infinitely many solutions.</p>

</details>

---

### Q70. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the following system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>5</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>3</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>a</mi><mo>&#160;</mo><mi>z</mi><mo>=</mo><mi>b</mi></math>
has no solution, then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mi>b</mi><mo>&#8800;</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8800;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mi>b</mi><mo>=</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8800;</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mi>b</mi><mo>=</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mi>b</mi><mo>&#8800;</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mi>b</mi><mo>&#8800;</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Given system of equations</p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>5</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>3</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>a</mi><mo>&#160;</mo><mi>z</mi><mo>=</mo><mi>b</mi></math>
has no solution, <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mi>a</mi><mo>-</mo><mn>2</mn><mo>-</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>5</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>5</mn><mfenced><mrow><mo>-</mo><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mfenced><mrow><mn>3</mn><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>&#160;</mo><mo>+</mo><mn>1</mn><mfenced><mrow><mn>3</mn><mo>+</mo><mi>b</mi></mrow></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>-</mo><mn>8</mn><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>b</mi></mtd><mtd><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mn>3</mn><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>&#160;</mo><mo>-</mo><mn>5</mn><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mi>b</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mi>b</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mn>1</mn><mo>&#160;</mo><mfenced><mrow><mi>b</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mn>5</mn><mfenced><mn>2</mn></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>7</mn><mo>-</mo><mn>3</mn><mi>b</mi></math></p><p>For the system to have no solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>D</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><msub><mi>D</mi><mn>3</mn></msub><mo>&#160;</mo><mo>&#8800;</mo><mo>&#160;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>a</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#160;</mo><mo>&#8800;</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></math>.</p>

</details>

---

### Q71. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>&#955;</mi><mo>]</mo></math> be the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math>. The set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> for which the system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>9</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mo>(</mo><mn>28</mn><mo>+</mo><mo>[</mo><mi>&#955;</mi><mo>]</mo><mo>)</mo><mi>z</mi><mo>=</mo><mo>[</mo><mi>&#955;</mi><mo>]</mo></math> has a solution is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>9</mn><mo>)</mo><mo>&#8746;</mo><mo>[</mo><mo>-</mo><mn>8</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>9</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mo>-</mo><mn>9</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>9</mn><mo>,</mo><mo>-</mo><mn>8</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>**

**Detailed Solution:**

<p>Given, the system of linear equations, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>3</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mo>(</mo><mn>28</mn><mo>+</mo><mo>[</mo><mi>&#955;</mi><mo>]</mo><mo>]</mo><mi>z</mi><mo>=</mo><mo>[</mo><mi>&#955;</mi><mo>]</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|" separators="|"><mtable columnalign="center center center" columnspacing="1em" rowspacing="4pt"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>28</mn><mo>+</mo><mo>[</mo><mi>&#955;</mi><mo>]</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mfenced open="{" close="}"><mrow><mn>56</mn><mo>+</mo><mn>2</mn><mfenced open="[" close="]"><mi>&#955;</mi></mfenced><mo>-</mo><mn>20</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced open="{" close="}"><mrow><mn>84</mn><mo>+</mo><mn>3</mn><mfenced open="[" close="]"><mi>&#955;</mi></mfenced><mo>-</mo><mn>45</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mn>12</mn><mo>-</mo><mn>18</mn></mrow></mfenced><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mo>&#8722;</mo><mo>(</mo><mo>[</mo><mi>&#955;</mi><mo>]</mo><mo>+</mo><mn>9</mn><mo>)</mo></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mo>-</mo><mfenced><mrow><mo>[</mo><mi>&#955;</mi><mo>]</mo><mo>+</mo><mn>9</mn></mrow></mfenced><mo>&#8800;</mo><mn>0</mn></math> then unique solution
If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mo>-</mo><mfenced><mrow><mo>[</mo><mi>&#955;</mi><mo>]</mo><mo>+</mo><mn>9</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math> infinite solutions</p><p>Hence,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi></math></p>

</details>

---

### Q72. JEE Main 2021 (27 Aug Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>If the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>&#946;</mi><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p>has infinitely many solutions, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced></math> is equal to __________.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>&#946;</mi><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>&#160;</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p>For Equation to have infinitely many solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>A</mi><mi>d</mi><mi>j</mi><mo>.</mo><mo>&#160;</mo><mi>A</mi></mrow></mfenced><mo>.</mo><mi>B</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>3</mn><mi>&#946;</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Now,</p><p>Minor of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>3</mn></mtd><mtd><mi>&#946;</mi><mo>+</mo><mn>3</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mi>&#946;</mi><mo>+</mo><mn>3</mn></mtd><mtd><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>3</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p>Cofactor of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mfenced><mrow><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>-</mo><mn>6</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>-</mo><mfenced><mrow><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p>Adjoint of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mfenced><mrow><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>-</mo><mfenced><mrow><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mo>.</mo><mo>&#160;</mo><mi>A</mi></mrow></mfenced><mo>.</mo><mi>B</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mfenced><mrow><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>-</mo><mfenced><mrow><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>6</mn><mi>&#946;</mi><mo>-</mo><mn>9</mn><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi><mo>-</mo><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>6</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3</mn><mi>&#946;</mi><mo>-</mo><mn>9</mn><mo>-</mo><mn>2</mn><mi>&#945;</mi><mi>&#946;</mi><mo>-</mo><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>18</mn><mo>-</mo><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>9</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>18</mn><mo>-</mo><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>Therefore,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mo>-</mo><mn>3</mn><mo>-</mo><mn>1</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mo>-</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mn>7</mn></math></p><p> </p>

</details>

---

### Q73. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Two fair dice are thrown. The numbers on them are taken as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#955;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#956;</mi><mo>,</mo></math> and a system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mi>&#956;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mn>1</mn></math>
is constructed. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is the probability that the system has a unique solution and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> is the probability that the system has no solution, then:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mn>5</mn><mn>36</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mn>1</mn><mn>36</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mn>1</mn><mn>36</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mn>5</mn><mn>36</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mn>5</mn><mn>36</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mi mathvariant="normal">&#955;</mi><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#916;</mi><mn>1</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#956;</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mi>&#955;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>10</mn><mi mathvariant="normal">&#955;</mi><mo>+</mo><mn>3</mn><mi mathvariant="normal">&#956;</mi><mo>-</mo><mi>&#955;&#956;</mi><mo>-</mo><mn>44</mn><mspace linebreak="newline"/></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#916;</mi><mn>2</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#956;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#955;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>5</mn><mi mathvariant="normal">&#955;</mi><mo>+</mo><mi mathvariant="normal">&#956;</mi><mo>-</mo><mi>&#955;&#956;</mi><mo>-</mo><mn>13</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#916;</mi><mn>3</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>&#956;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mi mathvariant="normal">&#956;</mi><mo>+</mo><mn>6</mn></math></p><p>For unique solution
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#955;</mi><mo>&#8800;</mo><mn>5</mn><mo>,</mo><mi mathvariant="normal">&#956;</mi><mo>&#8712;</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>&#215;</mo><mn>1</mn><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math>
For No Solution
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#955;</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">&#956;</mi><mo>&#8800;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>q</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>36</mn></mfrac></math></p>

</details>

---

### Q74. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>. If the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfenced><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><mi>y</mi><mo>+</mo><mn>4</mn><mi>sin</mi><mo>&#8289;</mo><mn>3</mn><mi>&#952;</mi><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfenced><mi>y</mi><mo>+</mo><mn>4</mn><mi>sin</mi><mo>&#8289;</mo><mn>3</mn><mi>&#952;</mi><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><mi>y</mi><mo>+</mo><mo>(</mo><mn>1</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mo>&#8289;</mo><mn>3</mn><mi>&#952;</mi><mo>)</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>
has a non-trivial solution, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>18</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>1</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">R</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi mathvariant="normal">R</mi><mn>3</mn></msub><mo>-</mo><msub><mi mathvariant="normal">R</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>+</mo><msub><mi>C</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>2</mn></mtd><mtd><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>2</mn></mtd><mtd><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mo>+</mo><msub><mi mathvariant="normal">C</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>2</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd><mtd><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>2</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd><mtd><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Expanding along <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mrow></mfenced><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mn>3</mn><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>18</mn></mfrac></math></p>

</details>

---

### Q75. JEE Main 2021 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

For real numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>,</mo></math> consider the following system of linear equations: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>&#946;</mi><mo>.</mo></math> If the system has infinite solutions, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Given system of linear equations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>&#946;</mi></math></p><p>Using Cramer Rule, we can say for infinite solutions</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><msub><mi>&#916;</mi><mn>1</mn></msub><mo>=</mo><msub><mi>&#916;</mi><mn>2</mn></msub><mo>=</mo><msub><mi>&#916;</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Apply <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>&#8596;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mfenced><mrow><mn>2</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>&#946;</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q76. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>, for which the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>6</mn><mi>z</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>9</mn><mi>z</mi><mo>=</mo><mi>b</mi></math></p><p>has no solution, are :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>b</mi><mo>&#8800;</mo><mn>13</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8800;</mo><mn>3</mn><mo>,</mo><mi>b</mi><mo>&#8800;</mo><mn>13</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8800;</mo><mn>3</mn><mo>,</mo><mi>b</mi><mo>=</mo><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>b</mi><mo>=</mo><mn>13</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>b</mi><mo>&#8800;</mo><mn>13</mn></math>**

**Detailed Solution:**

<p>The given equation is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>6</mn><mi>z</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>9</mn><mi>z</mi><mo>=</mo><mi>b</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>9</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mn>18</mn><mo>-</mo><mn>5</mn><mi>a</mi></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced><mrow><mn>9</mn><mo>-</mo><mn>3</mn><mi>a</mi></mrow></mfenced><mo>+</mo><mn>6</mn><mfenced><mrow><mn>5</mn><mo>-</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>36</mn><mo>-</mo><mn>10</mn><mi>a</mi><mo>-</mo><mn>27</mn><mo>+</mo><mn>9</mn><mi>a</mi><mo>+</mo><mn>30</mn><mo>-</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>-</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>z</mi></msub><mo>=</mo><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd><mtd><mo>&#160;</mo><mi>b</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>b</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced><mrow><mi>b</mi><mo>-</mo><mn>15</mn></mrow></mfenced><mo>+</mo><mn>8</mn><mfenced><mrow><mn>5</mn><mo>-</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mi>b</mi><mo>-</mo><mn>20</mn><mo>-</mo><mn>3</mn><mi>b</mi><mo>+</mo><mn>15</mn><mo>+</mo><mn>40</mn><mo>-</mo><mn>48</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>b</mi><mo>-</mo><mn>13</mn></math></p><p>The system of equation has no solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>D</mi><mi>z</mi></msub><mo>&#8800;</mo><mn>0</mn></math></p><p>So, If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#8800;</mo><mn>13</mn></math>, then the system of equation has no solution.</p>

</details>

---

### Q77. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi></math> such that the system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>26</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mi>&#956;</mi></math> has no solution, are:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>&#956;</mi><mo>=</mo><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>&#956;</mi><mo>&#8800;</mo><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8800;</mo><mn>2</mn><mo>,</mo><mi>&#956;</mi><mo>=</mo><mn>10</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#956;</mi><mo>&#8800;</mo><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#956;</mi><mo>&#8800;</mo><mn>10</mn></math>**

**Detailed Solution:**

<p>For the system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><mi>z</mi><mo>=</mo><msub><mi>d</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mi>z</mi><mo>=</mo><msub><mi>d</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>3</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mi>z</mi><mo>=</mo><msub><mi>d</mi><mn>3</mn></msub><mo>,</mo></math></p><p>We have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><msub><mi>D</mi><mi>x</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>d</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>d</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>d</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><msub><mi>D</mi><mi>y</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>d</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>d</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>d</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>z</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>d</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>d</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>d</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>.</mo></math></p><p>And, the system has no solution, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>0</mn></math> and atleast one of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>x</mi></msub><mo>,</mo><mo>&#160;</mo><msub><mi>D</mi><mi>y</mi></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>D</mi><mi>z</mi></msub></math> is non-zero.</p><p>Thus, for the given system of equations,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>26</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">y</mi><mo>+</mo><mi>&#955;</mi><mi mathvariant="normal">z</mi><mo>=</mo><mi>&#956;</mi></math></p><p>We have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mfenced><mrow><mn>5</mn><mi>&#955;</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mn>6</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>&#955;</mi><mo>-</mo><mn>10</mn><mo>-</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>5</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#955;</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn><mo>.</mo></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>z</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>26</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>&#956;</mi></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mfenced><mrow><mn>5</mn><mi>&#956;</mi><mo>-</mo><mn>52</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>3</mn><mi>&#956;</mi><mo>-</mo><mn>26</mn></mrow></mfenced><mo>+</mo><mn>6</mn><mfenced><mrow><mn>6</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>&#956;</mi><mo>-</mo><mn>52</mn><mo>-</mo><mn>3</mn><mi>&#956;</mi><mo>+</mo><mn>26</mn><mo>+</mo><mn>6</mn><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#956;</mi><mo>&#8800;</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mo>&#8800;</mo><mn>10</mn><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> For no solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>&#8800;</mo><mn>10</mn><mo>.</mo></math></p>

</details>

---

### Q78. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> for which the following system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>3</mn><mi>z</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mi>k</mi><mi>z</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>has infinitely many solutions, is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>3</mn><mi>z</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mi>k</mi><mi>z</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>For infinitely many solutions,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>5</mn></mtd><mtd><mo>&#160;</mo><mi>k</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>(</mo><mn>2</mn><mi>k</mi><mo>+</mo><mn>15</mn><mo>)</mo><mo>+</mo><mn>1</mn><mfenced><mrow><mi>k</mi><mo>+</mo><mn>18</mn></mrow></mfenced><mo>+</mo><mn>4</mn><mfenced><mrow><mn>5</mn><mo>-</mo><mn>12</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>(</mo><mn>2</mn><mi>k</mi><mo>+</mo><mn>15</mn><mo>)</mo><mo>+</mo><mi>k</mi><mo>+</mo><mn>18</mn><mo>-</mo><mn>28</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mi>k</mi><mo>+</mo><mn>35</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mo>-</mo><mn>5</mn></math></p>

</details>

---

### Q79. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mi>&#955;</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi><mo>&#8712;</mo><mi>R</mi></math>
has a non-trivial solution. Then which of the following is true?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi><mo>&#8712;</mo><mi>R</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi><mo>&#8712;</mo><mi>R</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi></math>**

**Detailed Solution:**

<p>For non-trivial solution</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mi>&#955;</mi></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#956;</mi></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>20</mn><mo>-</mo><mn>6</mn><mi>&#955;</mi><mo>+</mo><mi>&#955;</mi><mi>&#956;</mi><mo>+</mo><mn>8</mn><mo>+</mo><mn>2</mn><mi>&#956;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#956;</mi><mo>-</mo><mn>6</mn><mi>&#955;</mi><mo>+</mo><mi>&#955;</mi><mi>&#956;</mi><mo>=</mo><mn>12</mn></math></p><p>when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>12</mn><mo>-</mo><mn>6</mn><mi>&#955;</mi><mo>+</mo><mn>6</mn><mi>&#955;</mi><mo>=</mo><mn>12</mn></math></p><p>which is satisfied by all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mi>&#956;</mi><mo>=</mo><mn>24</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mi>&#956;</mi><mo>=</mo><mn>30</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>12</mn><mo>-</mo><mn>6</mn><mi>&#955;</mi><mo>-</mo><mn>6</mn><mi>&#955;</mi><mo>=</mo><mn>12</mn></math></p>

</details>

---

### Q80. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></math> be the real roots of the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>&#8712;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8800;</mo><mn>0</mn></math>). If the system of equations (in, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>,</mo><mi>v</mi><mo>,</mo><mi>w</mi></math>) given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>u</mi><mo>+</mo><mi>&#946;</mi><mi>v</mi><mo>+</mo><mi>&#947;</mi><mi>w</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mi>u</mi><mo>+</mo><mi>&#947;</mi><mi>v</mi><mo>+</mo><mi>&#945;</mi><mi>w</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mi>u</mi><mo>+</mo><mi>&#945;</mi><mi>v</mi><mo>+</mo><mi>&#946;</mi><mi>w</mi><mo>=</mo><mn>0</mn></math> has non-trivial solution, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>a</mi><mn>2</mn></msup><mi>b</mi></mfrac></math> is<gwmw style="display:none;"></gwmw>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>Equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> has roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi></math>. Therefore, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>+</mo><mi>&#946;</mi><mi>&#947;</mi><mo>+</mo><mi>&#947;</mi><mi>&#945;</mi><mo>=</mo><mi>b</mi></math></p><p>Since the given system of equations has non-trivial solutions,</p><p>we have </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mi>&#947;</mi></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd><mtd><mi>&#947;</mi></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>&#947;</mi></mtd><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#947;</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>&#945;</mi><mi>&#946;</mi><mi>&#947;</mi><mo>=</mo><mn>0</mn></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mo>&#160;</mo><mfenced close="]" open="["><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#947;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi><mo>-</mo><mi>&#946;</mi><mi>&#947;</mi><mo>-</mo><mi>&#947;</mi><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mo>&#160;</mo><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>3</mn><mfenced><mrow><mi>&#945;</mi><mi>&#946;</mi><mo>+</mo><mi>&#946;</mi><mi>&#947;</mi><mo>+</mo><mi>&#947;</mi><mi>&#945;</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>-</mo><mi>a</mi><mfenced close="]" open="["><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>b</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>/</mo><mi>b</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q81. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mi>k</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>k</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mi>k</mi><mo>=</mo><msup><mi>k</mi><mn>2</mn></msup></math> has no solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>k</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mi>k</mi><mo>=</mo><msup><mi>k</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>K</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>K</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>K</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mi>K</mi><mfenced><mrow><msup><mi>K</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mi>K</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>K</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>K</mi><mn>3</mn></msup><mo>-</mo><mi>K</mi><mo>-</mo><mi>K</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>-</mo><mi>K</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>K</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mo>&#160;</mo><mi>K</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mi>K</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mfenced><mrow><mo>&#160;</mo><mi>K</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><msub><mi>&#916;</mi><mn>1</mn></msub><mo>=</mo><msub><mi>&#916;</mi><mn>2</mn></msub><mo>=</mo><msub><mi>&#916;</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math></p><p>But for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo></math> at least one out of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>1</mn></msub><mo>,</mo><msub><mi>&#916;</mi><mn>2</mn></msub><mo>,</mo><msub><mi>&#916;</mi><mn>3</mn></msub></math> are not zero</p><p>Hence for no solution, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p>

</details>

---

### Q82. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Consider the following system of equations: </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>3</mn><mi>z</mi><mo>=</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>y</mi><mo>-</mo><mn>11</mn><mi>z</mi><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mi>c</mi></math></p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> are real constants. Then the system of equations :</p>

**Options:**

- **(A)** has a unique solution when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>a</mi><mo>=</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi></math>
- **(B)** has no solution for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>
- **(C)** has infinite number of solutions when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>a</mi><mo>=</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi></math>
- **(D)** has a unique solution for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) has infinite number of solutions when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>a</mi><mo>=</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>6</mn></mtd><mtd><mo>-</mo><mn>11</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>7</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mo>-</mo><mn>2</mn><mo>(</mo><mn>25</mn><mo>)</mo><mo>-</mo><mn>3</mn><mo>(</mo><mo>-</mo><mn>10</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mo>-</mo><mn>50</mn><mo>+</mo><mn>30</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mn>6</mn></mtd><mtd><mo>-</mo><mn>11</mn></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>7</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mi>a</mi><mo>-</mo><mn>2</mn><mo>(</mo><mn>7</mn><mi>b</mi><mo>+</mo><mn>11</mn><mi>c</mi><mo>)</mo><mo>-</mo><mn>3</mn><mo>(</mo><mo>-</mo><mn>2</mn><mi>b</mi><mo>-</mo><mn>6</mn><mi>c</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mi>a</mi><mo>-</mo><mn>14</mn><mi>b</mi><mo>-</mo><mn>22</mn><mi>c</mi><mo>+</mo><mn>6</mn><mi>b</mi><mo>+</mo><mn>18</mn><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mi>a</mi><mo>-</mo><mn>8</mn><mi>b</mi><mo>-</mo><mn>4</mn><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>(</mo><mn>5</mn><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mo>-</mo><mi>c</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>b</mi></mtd><mtd><mo>-</mo><mn>11</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd><mtd><mn>7</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mi>b</mi><mo>+</mo><mn>11</mn><mi>c</mi><mo>-</mo><mi>a</mi><mo>(</mo><mn>25</mn><mo>)</mo><mo>-</mo><mn>3</mn><mo>(</mo><mn>2</mn><mi>c</mi><mo>-</mo><mi>b</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mi>b</mi><mo>+</mo><mn>11</mn><mi>c</mi><mo>-</mo><mn>25</mn><mi>a</mi><mo>-</mo><mn>6</mn><mi>c</mi><mo>+</mo><mn>3</mn><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>25</mn><mi>a</mi><mo>+</mo><mn>10</mn><mi>b</mi><mo>+</mo><mn>5</mn><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>5</mn><mo>(</mo><mn>5</mn><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mo>-</mo><mi>c</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>6</mn></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mi>c</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>-</mo><mn>2</mn><mo>(</mo><mn>2</mn><mi>c</mi><mo>-</mo><mi>b</mi><mo>)</mo><mo>-</mo><mn>10</mn><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>10</mn><mi>a</mi><mo>+</mo><mn>4</mn><mi>b</mi><mo>+</mo><mn>2</mn><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><mo>(</mo><mn>5</mn><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mo>-</mo><mi>c</mi><mo>)</mo><mo>&#160;</mo></math></p><p>for infinite solution</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>a</mi><mo>=</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi></math></p>

</details>

---

### Q83. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The following system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>9</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>9</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>8</mn></math>

**Options:**

- **(A)** has infinitely many solutions
- **(B)** has a unique solution
- **(C)** has a solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math> satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#947;</mi><mn>3</mn></msup><mo>=</mo><mn>12</mn></math>
- **(D)** does not have any solution

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) has a unique solution**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>9</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>9</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>8</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>-</mo><mfenced><mn>2</mn></mfenced><mo>&#8658;</mo><mo>-</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced><mo>&#160;</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>8</mn><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mn>2</mn></math></p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>y</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> system has unique solution.</p>

</details>

---

### Q84. JEE Main 2021 (25 Feb Shift 1)

*Type:* `numerical` | *Level:* `1`

If the system of equations<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p>has infinitely many solutions, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to ______ .</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **21**

**Detailed Solution:**

If the system of equations<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mo>:</mo><mo>&#160;</mo><mi>k</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub><mo>:</mo><mo>&#160;</mo><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>3</mn></msub><mo>:</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>3</mn></math></p><p>Which are equivalent to equations of planes.</p><p>We observe <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mi>P</mi><mn>2</mn></msub><mo>-</mo><msub><mi>P</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><msub><mi>P</mi><mn>3</mn></msub></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>-</mo><mi>K</mi><mo>=</mo><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>K</mi><mo>=</mo><mn>21</mn></math></p>

</details>

---

### Q85. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> real matrices such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is a symmetric matrix and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is a skew-symmetric matrix. Then the system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi>B</mi><mn>2</mn></msup><mo>-</mo><msup><mi>B</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi>A</mi><mn>2</mn></msup></mrow></mfenced><mi>X</mi><mo>=</mo><mi>O</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> is a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>1</mn></math> column matrix of unknown variables and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> is a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>1</mn></math> null matrix, has

**Options:**

- **(A)** exactly two solutions
- **(B)** infinitely many solutions
- **(C)** a unique solution
- **(D)** no solution

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) infinitely many solutions**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mi>T</mi></msup><mo>=</mo><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mi>T</mi></msup><mo>=</mo><mo>-</mo><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><msup><mi>B</mi><mn>2</mn></msup><mo>-</mo><msup><mi>B</mi><mn>2</mn></msup><msup><mi>A</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>C</mi><mi>T</mi></msup><mo>=</mo><msup><mfenced><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi>B</mi><mn>2</mn></msup></mrow></mfenced><mi>T</mi></msup><mo>-</mo><msup><mfenced><mrow><msup><mi>B</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi>A</mi><mn>2</mn></msup></mrow></mfenced><mi>T</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><msup><mi>B</mi><mn>2</mn></msup></mfenced><mi>T</mi></msup><msup><mfenced><msup><mi>A</mi><mn>2</mn></msup></mfenced><mi>T</mi></msup><mo>-</mo><msup><mfenced><msup><mi>A</mi><mn>2</mn></msup></mfenced><mi>T</mi></msup><msup><mfenced><msup><mi>B</mi><mn>2</mn></msup></mfenced><mi>T</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>B</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><msup><mi>A</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi>B</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>C</mi><mi>T</mi></msup><mo>=</mo><mo>-</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is skew symmetric.</p><p>So det <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>C</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p>so system have infinite solutions.</p>

</details>

---

### Q86. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>For the system of linear equations:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>k</mi><mi>z</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>k</mi><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mi>k</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>Consider the following statements:
(A) The system has unique solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8800;</mo><mn>2</mn><mo>,</mo><mi>k</mi><mo>&#8800;</mo><mo>-</mo><mn>2</mn><mo>.</mo></math>
(B) The system has unique solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>.</mo></math>
(C) The system has unique solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>2</mn><mo>.</mo></math>
(D) The system has no-solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>2</mn><mo>.</mo></math>
(E) The system has infinite number of solutions if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8800;</mo><mo>-</mo><mn>2</mn><mo>.</mo></math> </p><p>Which of the following statements are correct?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>E</mi></mfenced></math> only
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>E</mi></mfenced></math> only
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>D</mi></mfenced></math> only
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>C</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>D</mi></mfenced></math> only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>D</mi></mfenced></math> only**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>k</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>k</mi></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>4</mn><mo>-</mo><msup><mi>k</mi><mn>2</mn></msup></math></p><p>so, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is correct and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>,</mo><mi>C</mi><mo>,</mo><mi>E</mi></math> are incorrect. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mo>&#177;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>48</mn><mo>&#8800;</mo><mn>0</mn></math></p><p>So, no solution if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mo>&#177;</mo><mn>2</mn></math></p>

</details>

---

### Q87. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The system of linear equations<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mi>k</mi><mi>z</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi>m</mi></math>
is inconsistent if :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>&#8800;</mo><mfrac><mstyle displaystyle="true"><mn>4</mn></mstyle><mstyle displaystyle="true"><mn>5</mn></mstyle></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>=</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8800;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>&#8712;</mo><mi>R</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8800;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>&#8800;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>&#8800;</mo><mfrac><mstyle displaystyle="true"><mn>4</mn></mstyle><mstyle displaystyle="true"><mn>5</mn></mstyle></mfrac></math>**

**Detailed Solution:**

<p>For inconsistent system of equation the conditions should be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mn>0</mn></math> and at least one of the <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mi>x</mi></msub><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><msub><mo>&#8710;</mo><mi>y</mi></msub><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><msub><mo>&#8710;</mo><mi>z</mi></msub></math> should not be equal to zero.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mi>k</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>24</mn><mo>+</mo><mn>2</mn><mfenced><mn>0</mn></mfenced><mo>-</mo><mi>k</mi><mfenced><mn>8</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>3</mn></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#916;</mi><mi>x</mi></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>10</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>5</mn><mo>&#160;</mo><mi>m</mi></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mo>&#8710;</mo><mi>x</mi></msub><mo>=</mo><mfenced open="[" close="]"><mrow><mn>10</mn><mfenced><mn>8</mn></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>10</mn><mo>&#160;</mo><mi>m</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced><mrow><mn>12</mn><mo>+</mo><mn>20</mn><mo>&#160;</mo><mi>m</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mo>&#8710;</mo><mi>x</mi></msub><mo>=</mo><mn>8</mn><mfenced><mrow><mn>4</mn><mo>-</mo><mn>5</mn><mi>m</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mi>x</mi></msub><mo>&#8800;</mo><mn>0</mn><mo>&#8658;</mo><mi>m</mi><mo>&#8800;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mi>y</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>10</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>6</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>5</mn><mo>&#160;</mo><mi>m</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mfenced><mrow><mo>-</mo><mn>6</mn><mo>+</mo><mn>10</mn><mo>&#160;</mo><mi>m</mi></mrow></mfenced><mo>+</mo><mn>10</mn><mfenced><mn>0</mn></mfenced><mo>-</mo><mn>3</mn><mfenced><mrow><mn>10</mn><mo>&#160;</mo><mi>m</mi><mo>-</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mi>z</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>10</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>5</mn><mi>m</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#916;</mi><mi>z</mi></msub><mo>=</mo><mn>3</mn><mfenced><mrow><mo>-</mo><mn>20</mn><mi>m</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>10</mn><mi>m</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mn>10</mn><mfenced><mrow><mn>4</mn><mo>+</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#916;</mi><mi>z</mi></msub><mo>=</mo><mo>-</mo><mn>60</mn><mi>m</mi><mo>-</mo><mn>36</mn><mo>+</mo><mn>20</mn><mi>m</mi><mo>-</mo><mn>12</mn><mo>+</mo><mn>80</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#916;</mi><mi>z</mi></msub><mo>=</mo><mo>-</mo><mn>40</mn><mi>m</mi><mo>+</mo><mn>32</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mo>&#8710;</mo><mi>z</mi></msub><mo>=</mo><mn>8</mn><mfenced><mrow><mn>4</mn><mo>-</mo><mn>5</mn><mi>m</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mi>z</mi></msub><mo>&#8800;</mo><mn>0</mn><mo>&#8658;</mo><mi>m</mi><mo>&#8800;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></math></p>

</details>

---

### Q88. JEE Main 2020 (06 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>The sum of distinct values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> for which the system of equations :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mi>x</mi><mo>+</mo><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>&#955;</mi><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">x</mi><mo>+</mo><mfenced><mrow><mn>4</mn><mi mathvariant="normal">&#955;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">y</mi><mo>+</mo><mfenced><mrow><mi mathvariant="normal">&#955;</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mfenced><mrow><mn>3</mn><mi mathvariant="normal">&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">y</mi><mo>+</mo><mn>3</mn><mo>&#160;</mo><mfenced><mrow><mi mathvariant="normal">&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">z</mi><mo>=</mo><mn>0</mn></math>,</p><p>Has non-zero solutions, is ....... .</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#955;</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>2</mn><mi>&#955;</mi></mtd></mtr><mtr><mtd><mi>&#955;</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn></mtd><mtd><mi>&#955;</mi><mo>+</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>3</mn><mo>(</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>)</mo></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>-</mo><msub><mi>R</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>-</mo><msub><mi>R</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#955;</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>2</mn><mi>&#955;</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>&#955;</mi><mo>-</mo><mn>3</mn></mtd><mtd><mo>-</mo><mi>&#955;</mi><mo>+</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn><mo>-</mo><mi>&#955;</mi></mtd><mtd><mn>0</mn></mtd><mtd><mi>&#955;</mi><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><msub><mi>C</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>2</mn><mi>&#955;</mi></mtd></mtr><mtr><mtd><mn>3</mn><mo>-</mo><mi>&#955;</mi></mtd><mtd><mi>&#955;</mi><mo>-</mo><mn>3</mn></mtd><mtd><mn>3</mn><mo>-</mo><mi>&#955;</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>&#955;</mi><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mfenced close="]" open="["><mrow><mn>6</mn><mi>&#955;</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></math></p><p>sum of values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q89. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi></math> for which the system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>2</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi>y</mi><mo>+</mo><mn>3</mn><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>5</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mi>&#956;</mi></math> has infinitely many solutions, are respectively

**Options:**

- **(A)** 6 and 8
- **(B)** 5 and 7
- **(C)** 5 and 8
- **(D)** 4 and 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5 and 8**

**Detailed Solution:**

<p>For infinite number of solutions, all determinants <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>,</mo><mo>&#160;</mo><msub><mi>D</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>D</mi><mn>2</mn></msub><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><msub><mi>D</mi><mn>3</mn></msub></math> must be zero and planes represented by these equations should not be parallel. So, we have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mi>&#956;</mi></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#956;</mi></mtd><mtd><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#956;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mn>8</mn></math></p><p> </p>

</details>

---

### Q90. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
has a non-zero solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>)</mo></math> for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">k</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>+</mo><mfenced><mfrac><mi mathvariant="normal">y</mi><mi mathvariant="normal">z</mi></mfrac></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>**

**Detailed Solution:**

<p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>0</mn><mo>&#8594;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><msup><mi>k</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>3</mn><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mo>&#160;</mo><mi>y</mi><mo>+</mo><mn>9</mn><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>3</mn><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo><mo>-</mo><mo>(</mo><mn>3</mn><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>y</mi><mi>z</mi></mfrac><mo>=</mo><mo>-</mo><mn>3</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>so</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mfenced><mfrac><mi>y</mi><mi>z</mi></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p> </p>

</details>

---

### Q91. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math>. The system of linear equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>4</mn><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mi>&#955;</mi><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>6</mn><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>10</mn><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mn>4</mn><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mn>3</mn></math>
is inconsistent for :

**Options:**

- **(A)** exactly one positive value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math>
- **(B)** exactly one negative value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math>
- **(C)** every value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math>
- **(D)** exactly two values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) exactly one negative value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math>**

**Detailed Solution:**

<p>Here, we will use Cramer&#39;s Rule according to which, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>0</mn></math> and, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>&#8800;</mo><mn>0</mn></math> if the system of linear equations is inconsistent. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#955;</mi></mtd><mtd><mo>-</mo><mn>10</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>24</mn><mo>+</mo><mn>10</mn></mrow></mfenced><mo>+</mo><mn>4</mn><mfenced><mrow><mn>4</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mo>-</mo><mn>10</mn><mo>+</mo><mn>6</mn><mi>&#955;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mn>3</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi>&#955;</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>10</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>1</mn><mfenced><mrow><mo>-</mo><mn>24</mn><mo>+</mo><mn>10</mn></mrow></mfenced><mo>+</mo><mn>4</mn><mfenced><mrow><mn>8</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mo>-</mo><mn>20</mn><mo>+</mo><mn>18</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mn>3</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;&#160;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>,</mo><msub><mi mathvariant="normal">D</mi><mn>1</mn></msub><mo>&#8800;</mo><mn>0</mn></math></p>

</details>

---

### Q92. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Suppose the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>3</mn></msub></math> are the solutions of the system of linear equations, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>x</mi><mo>=</mo><mi>b</mi></math> when the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> on the right side is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>,</mo><msub><mi>b</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>3</mn></msub></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>; <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mn>2</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mn>3</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math>, then the determinant of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><msub><mi>&#945;</mi><mn>1</mn></msub></mtd><mtd><msub><mi>&#945;</mi><mn>2</mn></msub></mtd><mtd><msub><mi>&#945;</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>&#946;</mi><mn>1</mn></msub></mtd><mtd><msub><mi>&#946;</mi><mn>2</mn></msub></mtd><mtd><msub><mi>&#946;</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>&#947;</mi><mn>1</mn></msub></mtd><mtd><msub><mi>&#947;</mi><mn>2</mn></msub></mtd><mtd><msub><mi>&#947;</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math>. Now satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>3</mn></msub></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>x</mi><mo>=</mo><mi>b</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><msub><mi>b</mi><mn>1</mn></msub><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>&#945;</mi><mn>1</mn></msub></mtd><mtd><msub><mi>&#945;</mi><mn>2</mn></msub></mtd><mtd><msub><mi>&#945;</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>&#946;</mi><mn>1</mn></msub></mtd><mtd><msub><mi>&#946;</mi><mn>2</mn></msub></mtd><mtd><msub><mi>&#946;</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>&#947;</mi><mn>1</mn></msub></mtd><mtd><msub><mi>&#947;</mi><mn>2</mn></msub></mtd><mtd><msub><mi>&#947;</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="" open="{"><mtable><mtr><mtd><msub><mi>&#945;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#945;</mi><mn>2</mn></msub><mo>+</mo><msub><mi>&#945;</mi><mn>3</mn></msub><mo>=</mo><mn>1</mn></mtd></mtr><mtr><mtd><msub><mi>&#946;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#946;</mi><mn>2</mn></msub><mo>+</mo><msub><mi>&#946;</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><msub><mi>&#947;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#947;</mi><mn>2</mn></msub><mo>+</mo><msub><mi>&#947;</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced><mo>&#8230;</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Now </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><msub><mi>b</mi><mn>2</mn></msub><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>&#945;</mi><mn>1</mn></msub></mtd><mtd><msub><mi>&#945;</mi><mn>2</mn></msub></mtd><mtd><msub><mi>&#945;</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>&#946;</mi><mn>1</mn></msub></mtd><mtd><msub><mi>&#946;</mi><mn>2</mn></msub></mtd><mtd><msub><mi>&#946;</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>&#947;</mi><mn>1</mn></msub></mtd><mtd><msub><mi>&#947;</mi><mn>2</mn></msub></mtd><mtd><msub><mi>&#947;</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>2</mn><msub><mi>&#945;</mi><mn>2</mn></msub><mo>+</mo><msub><mi>&#945;</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn><msub><mi>&#946;</mi><mn>2</mn></msub><mo>+</mo><msub><mi>&#946;</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn><msub><mi>&#947;</mi><mn>2</mn></msub><mo>+</mo><msub><mi>&#947;</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced><mo>&#8230;</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math></p><p>And satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>3</mn></msub></math> gives,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#946;</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#947;</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn></math></p><p>Now using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>&#946;</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>&#947;</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>&#946;</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>&#947;</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mn>1</mn></math>
Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>&#8658;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q93. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>If the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>2</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>4</mn><mo>&#160;</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>6</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mi>&#956;</mi></math></p><p>has infinitely many solutions, then :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>&#955;</mi><mo>+</mo><mn>2</mn><mi>&#956;</mi><mo>=</mo><mn>14</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>=</mo><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>-</mo><mn>2</mn><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>=</mo><mn>14</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>=</mo><mn>14</mn></math>**

**Detailed Solution:**

<p>For infinitely many solutions, all determinants should be zero.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi mathvariant="normal">&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi mathvariant="normal">&#955;</mi><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">D</mi><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi mathvariant="normal">&#956;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi mathvariant="normal">&#956;</mi><mo>=</mo><mn>5</mn></math></p><p>Now check each option </p>

</details>

---

### Q94. JEE Main 2020 (04 Sep Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>If the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>9</mn></math> 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>b</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>7</mn><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mn>24</mn><mo>,</mo></math> has infinitely many solutions, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>b</mi></math> is equal to ______</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>For infinitely many solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>1</mn><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mo>&#8722;</mo><mn>2</mn><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn><mtext>&#8201;&#160;&#160;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mn>1</mn><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mo>&#8722;</mo><mn>7</mn><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mn>1</mn><mfenced><mrow><mo>&#8722;</mo><mn>2</mn><mo>&#8722;</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>7</mn><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mi>a</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mo>&#8722;</mo><mn>5</mn><mo>&#8722;</mo><mn>35</mn><mo>+</mo><mn>5</mn><mi>a</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;</mtext><mi>a</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>9</mn><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mo>&#8722;</mo><mn>2</mn><mtext>&#8201;&#160;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mn>3</mn></mtd></mtr><mtr><mtd><mi>b</mi><mtext>&#8201;&#8201;&#8201;&#160;&#160;&#8201;&#8201;&#8201;&#8201;</mtext><mn>1</mn><mtext>&#8201;&#160;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mn>1</mn></mtd></mtr><mtr><mtd><mn>24</mn><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mo>&#8722;</mo><mn>7</mn><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>9</mn><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mo>&#8722;</mo><mn>2</mn><mtext>&#8201;&#160;&#160;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mn>3</mn></mtd></mtr><mtr><mtd><mi>b</mi><mtext>&#8201;&#160;&#160;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mn>1</mn><mtext>&#8201;&#8201;&#160;&#160;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mn>1</mn></mtd></mtr><mtr><mtd><mn>24</mn><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mo>&#8722;</mo><mn>7</mn><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#160;</mtext><mn>8</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mo>&#8722;</mo><mi>b</mi><mfenced><mrow><mo>&#8722;</mo><mn>16</mn><mo>+</mo><mn>21</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mn>72</mn><mo>&#8722;</mo><mn>72</mn></mrow></mfenced><mo>&#8722;</mo><mn>1</mn><mfenced><mrow><mo>&#8722;</mo><mn>63</mn><mo>+</mo><mn>48</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mo>&#8722;</mo><mn>5</mn><mi>b</mi><mo>+</mo><mn>15</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mi>b</mi><mo>=</mo><mn>3</mn></math></p><p>similarly <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>8</mn><mo>,</mo><mtext>&#8201;&#8201;</mtext><mi>b</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>    <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8722;</mo><mi>b</mi><mo>=</mo><mn>8</mn><mo>&#8722;</mo><mn>3</mn><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q95. JEE Main 2020 (03 Sep Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all integer solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi></mrow></mfenced></math> of the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>y</mi><mo>+</mo><mn>5</mn><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>4</mn><mo>&#160;</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>14</mn><mo>&#160;</mo><mi>y</mi><mo>+</mo><mn>9</mn><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p>such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>150</mn></math>. Then, the number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is equal to ..........</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>14</mn><mi>y</mi><mo>+</mo><mn>9</mn><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Applying <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo></math> equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>+</mo></math>equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>0</mn></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mi>y</mi></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>150</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>15</mn><mo>&#8804;</mo><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>150</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>&#8804;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>&#177;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>&#177;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mo>&#177;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mo>&#177;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn></math> solutions.</p>

</details>

---

### Q96. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi></math> for which the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>&#955;</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>4</mn></math></p><p>has no solution. Then the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></p>

**Options:**

- **(A)** Contains more than two elements
- **(B)** Is an empty set
- **(C)** Is a singleton
- **(D)** Contains exactly two elements

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Contains exactly two elements**

**Detailed Solution:**

<p> For no solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mn>0</mn></math> and at least one of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>1</mn></msub><mo>,</mo><msub><mi>&#916;</mi><mn>2</mn></msub><mo>,</mo><msub><mi>&#916;</mi><mn>3</mn></msub></math> is non-zero.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#955;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#916;</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mi>&#955;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>&#955;</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>&#955;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p> And for  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mo>&#8710;</mo><mn>1</mn></msub><mo>&#8800;</mo><mn>0</mn></math>
Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q97. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The following system of linear equations
<math><mn>7</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>6</mn><mi>z</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> has

**Options:**

- **(A)** infinitely many solutions, <math><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi></mi><mi>y</mi><mo>,</mo><mi></mi><mi>z</mi></mrow></mfenced></math> satisfying <math><mi>y</mi><mo>=</mo><mn>2</mn><mi>z</mi></math>
- **(B)** no solution
- **(C)** infinitely many solutions, <math><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi></mi><mi>y</mi><mo>,</mo><mi></mi><mi>z</mi></mrow></mfenced></math> satisfying <math><mi>x</mi><mo>=</mo><mn>2</mn><mi>z</mi></math>
- **(D)** only the trivial solution

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) infinitely many solutions, <math><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi></mi><mi>y</mi><mo>,</mo><mi></mi><mi>z</mi></mrow></mfenced></math> satisfying <math><mi>x</mi><mo>=</mo><mn>2</mn><mi>z</mi></math>**

**Detailed Solution:**

<p><math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>7</mn></mtd><mtd><mn>6</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>6</mn></mtd></mtr></mtable></mrow></mfenced></math></p><p><math><mo>=</mo><mn>7</mn><mfenced separators="|"><mrow><mo>-</mo><mn>20</mn></mrow></mfenced><mo>-</mo><mn>6</mn><mfenced separators="|"><mrow><mo>-</mo><mn>20</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced separators="|"><mrow><mo>-</mo><mn>10</mn></mrow></mfenced></math></p><p><math><mo>=</mo><mo>-</mo><mn>140</mn><mo>+</mo><mn>120</mn><mo>+</mo><mn>20</mn><mo>=</mo><mn>0</mn></math></p><p>So infinite non-trivial solution exist
Now equation <math><mo>(</mo><mn>1</mn><mo>)</mo><mi></mi><mo>+</mo><mi></mi><mn>3</mn></math> equation <math><mo>(</mo><mn>3</mn><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mi>x</mi><mo>-</mo><mn>20</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn><mi>z</mi></math></p>

</details>

---

### Q98. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If for some <math><mi>&#945;</mi></math> and <math><mi>&#946;</mi></math> in <math><mi>R</mi></math> , the intersection of the following three planes
<math><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>1</mn></math>
<math><mi>x</mi><mo>+</mo><mn>7</mn><mi>y</mi><mo>-</mo><mn>5</mn><mi>z</mi><mo>=</mo><mi>&#946;</mi></math>
<math><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mn>5</mn></math>
is a line in <math><msup><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msup></math> , then <math><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to:

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** <math><mn>10</mn></math>
- **(C)** <math><mn>2</mn></math>
- **(D)** <math><mo>-</mo><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>10</mn></math>**

**Detailed Solution:**

<math><mo>∆</mo><mo>=</mo><mn>0</mn><mi></mi><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>7</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd><mtd><mi>α</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><mfenced separators="|"><mrow><mn>7</mn><mi>α</mi><mo>+</mo><mn>25</mn></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mn>4</mn><mi>α</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mn>20</mn><mo>+</mo><mn>14</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><mn>3</mn><mi>α</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>0</mn><mi></mi><mo>&#8658;</mo><mi>α</mi><mo>=</mo><mo>-</mo><mn>3</mn></math>  
Also <math><msub><mrow><mi>D</mi></mrow><mrow><mi>z</mi></mrow></msub><mo>=</mo><mn>0</mn><mi></mi><mo>&#8658;</mo><mi></mi><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>7</mn></mtd><mtd><mi>β</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><mn>1</mn><mfenced separators="|"><mrow><mn>35</mn><mo>-</mo><mn>5</mn><mi>β</mi></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mn>15</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced separators="|"><mrow><mn>4</mn><mi>β</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><mi>β</mi><mo>=</mo><mn>13</mn></math>

</details>

---

### Q99. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The system of linear equations
<math><mi>&#955;</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>5</mn></math>
<math><mn>2</mn><mi>&#955;</mi><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>8</mn></math>
<math><mn>4</mn><mi>x</mi><mo>+</mo><mi>&#955;</mi><mi>y</mi><mo>+</mo><mn>6</mn><mi>z</mi><mo>=</mo><mn>10</mn></math> has

**Options:**

- **(A)** no solution when <math><mi>λ</mi><mo>=</mo><mn>8</mn></math>
- **(B)** a unique solution when <math><mi>λ</mi><mo>=</mo><mo>-</mo><mn>8</mn></math>
- **(C)** no solution when <math><mi>λ</mi><mo>=</mo><mn>2</mn></math>
- **(D)** infinitely many solutions when <math><mi>λ</mi><mo>=</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) no solution when <math><mi>λ</mi><mo>=</mo><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mi>&#955;</mi></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>&#955;</mi></mtd><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mi>&#955;</mi></mtd><mtd><mn>6</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>&#955;</mi><mfenced><mrow><mn>18</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mn>12</mn><mi>&#955;</mi><mo>-</mo><mn>20</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn></mrow></mfenced><mo>=</mo><mo>-</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>&#955;</mi><mo>+</mo><mn>16</mn><mo>=</mo><mfenced separators="|"><mrow><mi>&#955;</mi><mo>+</mo><mn>8</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mn>0</mn></math> for <math><mi>&#955;</mi><mo>=</mo><mn>2</mn></math>,
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mn>5</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>8</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>10</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>6</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>1</mn></msub><mo>=</mo><mn>5</mn><mfenced close="]" open="[" separators="|"><mrow><mn>18</mn><mo>-</mo><mn>10</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><mn>48</mn><mo>-</mo><mn>50</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><mn>16</mn><mo>-</mo><mn>30</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>1</mn></msub><mo>=</mo><mn>40</mn><mo>+</mo><mn>4</mn><mo>-</mo><mn>28</mn><mo>&#8800;</mo><mn>0</mn></math>
No solution for <math><mi>&#955;</mi><mo>=</mo><mn>2</mn></math>.</p>

</details>

---

### Q100. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For which of the following ordered pairs <math><mfenced separators="|"><mrow><mi>&#956;</mi><mo>,</mo><mi></mi><mi>&#948;</mi></mrow></mfenced><mo>,</mo></math> the system of linear equations
<math><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>1</mn></math>
<math><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mi>&#956;</mi></math>
<math><mn>4</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mi>&#948;</mi></math>
is inconsistent?

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mi></mi><mn>3</mn></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mi></mi><mn>6</mn></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mi></mi><mn>4</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mi></mi><mn>3</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced open="|" close="|" separators="|"><mrow><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable><mo>&#8201;</mo></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced separators="|"><mrow><msub><mi>R</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>-</mo><mn>2</mn><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>R</mi><mn>2</mn></msub></mrow></mfenced></math>
    <math><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable><mo>&#8201;</mo></mrow></mfenced><mo>=</mo><mn>0</mn></math>
Now, let <math><msub><mrow><mi>P</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#8801;</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>-</mo><mi>&#948;</mi><mo>=</mo><mn>0</mn><mo>.</mo></math> If the system has solutions it will have infinite solution, so,<math><msub><mrow><mi>P</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#8801;</mo><mi>&#945;</mi><msub><mrow><mi>P</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mi>&#946;</mi><msub><mrow><mi>P</mi></mrow><mrow><mn>2</mn></mrow></msub></math>
Hence, <math><mn>3</mn><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>4</mn></math> and <math><mn>4</mn><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#946;</mi><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>&#8201;</mo><mi>a</mi><mi>n</mi><mi>d</mi><mo>&#8201;</mo><mo>&#8201;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>
So, for infinite solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#956;</mi><mo>-</mo><mn>2</mn><mo>=</mo><mi>&#948;</mi></math></p><p>For system to be inconsistent,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8201;</mo><mn>2</mn><mi>&#956;</mi><mo>&#8800;</mo><mi>&#948;</mi><mo>+</mo><mn>2</mn></math>
So, checking option, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>)</mo></math> satisfies.</p>

</details>

---

### Q101. JEE Main 2020 (07 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

If the system of linear equations,
<math><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn></math>
<math><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>10</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mi>&#956;</mi></math>
has more than two solutions, then <math><mi>&#956;</mi><mo>-</mo><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup></math>, is equal to.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **13**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mi>&#956;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>3</mn></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>,
If <math><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>6</mn></math> and <math><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>10</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>2</mn></math>
If <math><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn></math> and <math><mi>x</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>10</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>4</mn></math></p><p>So, <math><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mi>&#956;</mi></math>, must pass through <math><mo>(</mo><mn>2,4</mn><mo>,</mo><mn>0</mn><mo>)</mo></math> and <math><mo>(</mo><mn>4,0</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>.</p><p><math><mn>6</mn><mo>+</mo><mn>8</mn><mo>=</mo><mi>&#956;</mi><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mn>14</mn></math>
And <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>+</mo><mn>2</mn><mi>&#955;</mi><mo>=</mo><mi>&#956;</mi><mo>&#160;</mo><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>1</mn></math></p><p>So, <math><mi>&#956;</mi><mo>-</mo><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>14</mn><mo>-</mo><mn>1</mn></math><math><mo>=</mo><mn>13</mn></math></p>

</details>

---

### Q102. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the system of linear equations
<math><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>a</mi><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>b</mi><mi>y</mi><mo>+</mo><mi>b</mi><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>c</mi><mi>y</mi><mo>+</mo><mi>c</mi><mi>z</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi></mi></math>
where <math><mi>a</mi><mo>,</mo><mi></mi><mi>b</mi><mo>,</mo><mi></mi><mi>c</mi><mo>&#8712;</mo><mi>R</mi></math> are non-zero and distinct; has a non-zero solution, then

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>a</mi></mrow></mfrac><mo>,</mo><mi></mi><mfrac><mrow><mn>1</mn></mrow><mrow><mi>b</mi></mrow></mfrac><mo>,</mo><mi></mi><mfrac><mrow><mn>1</mn></mrow><mrow><mi>c</mi></mrow></mfrac></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math>
- **(B)** <math><mi>a</mi><mo>,</mo><mi></mi><mi>b</mi><mo>,</mo><mi></mi><mi>c</mi></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mo>.</mo><mi>P</mi><mo>.</mo></math>
- **(C)** <math><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math><mi>a</mi><mo>,</mo><mi></mi><mi>b</mi><mo>,</mo><mi></mi><mi>c</mi></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>a</mi></mrow></mfrac><mo>,</mo><mi></mi><mfrac><mrow><mn>1</mn></mrow><mrow><mi>b</mi></mrow></mfrac><mo>,</mo><mi></mi><mfrac><mrow><mn>1</mn></mrow><mrow><mi>c</mi></mrow></mfrac></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math>**

**Detailed Solution:**

<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn><mi>a</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn><mi>b</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>4</mn><mi>c</mi></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn><mi>a</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn><mi>b</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>4</mn><mi>c</mi></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><mfenced separators="|"><mrow><mn>3</mn><mi>b</mi><mi>c</mi><mo>-</mo><mn>4</mn><mi>b</mi><mi>c</mi></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mn>2</mn><mi>a</mi><mi>c</mi><mo>-</mo><mn>4</mn><mi>a</mi><mi>c</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mi>a</mi><mi>b</mi><mo>-</mo><mn>3</mn><mi>a</mi><mi>b</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><mo>-</mo><mi>b</mi><mi>c</mi><mo>+</mo><mn>2</mn><mi>a</mi><mi>c</mi><mo>-</mo><mi>a</mi><mi>b</mi><mo>=</mo><mn>0</mn></math>
<math><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>2</mn><mi>a</mi><mi>c</mi></math>
<math><mi>a</mi><mo>,</mo><mi></mi><mi>b</mi><mo>,</mo><mi></mi><mi>c</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi><mo>.</mo><mi>P</mi><mo>.</mo></math>
<math><mo>&#8658;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>a</mi></mrow></mfrac><mo>,</mo><mi></mi><mfrac><mrow><mn>1</mn></mrow><mrow><mi>b</mi></mrow></mfrac><mo>,</mo><mi></mi><mfrac><mrow><mn>1</mn></mrow><mrow><mi>c</mi></mrow></mfrac></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math>

</details>

---

### Q103. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mo>[</mo><mi>x</mi><mo>]</mo></math> denotes the greatest integer <math><mo>&#8804;</mo><mi>x</mi><mo>,</mo></math> then the system of linear equations <math><mo>[</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>]</mo><mi>x</mi><mo>+</mo><mo>[</mo><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#952;</mi><mo>]</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>, <math><mo>[</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">t</mi><mi>&#952;</mi><mo>]</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>

**Options:**

- **(A)** has a unique solution if <math><mi>θ</mi><mo>∈</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>∪</mo><mfenced separators="|"><mrow><mi>π</mi><mo>,</mo><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></math>
- **(B)** have infinitely many solution if  <math><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mi>&#960;</mi><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></math>
- **(C)** has a unique if <math><mi>θ</mi><mo>∈</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math> and have infinitely many solutions if <math><mi>θ</mi><mo>∈</mo><mfenced separators="|"><mrow><mi>π</mi><mo>,</mo><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></math>
- **(D)** have infinitely many solutions if <math><mi>θ</mi><mo>∈</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math> and has a unique solution if <math><mi>θ</mi><mo>∈</mo><mfenced separators="|"><mrow><mi>π</mi><mo>,</mo><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) have infinitely many solutions if <math><mi>θ</mi><mo>∈</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math> and has a unique solution if <math><mi>θ</mi><mo>∈</mo><mfenced separators="|"><mrow><mi>π</mi><mo>,</mo><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><math><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></mrow></mfenced><mi>y</mi><mo>=</mo><mn>0</mn><mi>&#160;</mi></math> and <math><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></mrow></mfenced><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn><mi>&#160;</mi></math> for infinite many solution
<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></mrow></mfenced></mtd><mtd><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></mrow></mfenced></mtd></mtr><mtr><mtd><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi><mi>&#160;</mi></mrow></mrow></mrow></mfenced></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>
i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mi>&#160;</mi><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mrow><mi>c</mi><mi>o</mi><mi>t</mi><mi>&#952;</mi></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math>
when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>cos</mi><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> and  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cot</mi><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>,</mo><mi>&#160;</mi><mn>0</mn></mrow></mfenced><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mi>cot</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math>
When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mi>&#960;</mi><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mn>0</mn></mrow></mfenced><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>cos</mi><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mo>&#8658;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> and 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cot</mi><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><msqrt><mn>3</mn></msqrt><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mi>cot</mi><mi>&#952;</mi></mrow></mfenced><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mi>&#8734;</mi></mrow></mfenced></math>
When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>&#160;</mi></math> then the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> satisfied therefore infinitely many solution.
When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mi>&#960;</mi><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced><mi>&#160;</mi></math> then the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> not satisfied therefore unique solution.</p>

</details>

---

### Q104. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> be a real number for which the system of linear equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mi>&#955;</mi><mi>y</mi><mo>-</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mi>&#955;</mi><mo>-</mo><mn>2</mn></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>4</mn><mi>z</mi><mo>=</mo><mo>-</mo><mn>5</mn></math></p><p>has infinitely many solutions. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is a root of the quadratic equation:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mi>&#955;</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>The system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><mi>z</mi><mo>+</mo><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mi>z</mi><mo>+</mo><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>3</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mi>z</mi><mo>+</mo><msub><mi>d</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math> have a infinitely many solution, if</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><msub><mi>d</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>d</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>d</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>d</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>d</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>d</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>d</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>d</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>d</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>.</mo></math></p><p>Thus, for infinitely many solutions, we have <math><mi>D</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mi>&#955;</mi></mtd><mtd><mo>-</mo><mi>&#955;</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mfenced><mrow><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mo>-</mo><mn>16</mn><mo>+</mo><mn>3</mn><mi>&#955;</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mn>8</mn><mo>-</mo><mn>3</mn><mi>&#955;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>16</mn><mo>-</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>8</mn><mo>-</mo><mn>3</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>24</mn><mo>-</mo><mn>3</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>3</mn></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>3</mn></math> satisfies the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn><mo>.</mo></math></p>

</details>

---

### Q105. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>If the system of linear equations <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>5</mn></math>, <math><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>6</mn></math>,  <math><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mi>&#181;</mi><mo>,</mo><mi>&#160;</mi><mo>(</mo><mi>&#955;</mi><mo>,</mo><mi>&#160;</mi><mi>&#181;</mi><mi>&#160;</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>)</mo></math> , has infinitely many solutions, then the value of <math><mi>&#955;</mi><mo>+</mo><mi>&#181;</mi></math> is:</p>

**Options:**

- **(A)** <math><mn>7</mn></math>
- **(B)** <math><mn>10</mn></math>
- **(C)** <math><mn>12</mn></math>
- **(D)** <math><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>10</mn></math>**

**Detailed Solution:**

<math><mo>&#8710;</mo><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mi>&#955;</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math>
<math><msub><mrow><mo>&#8710;</mo></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi>&#956;</mi></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>4</mn><mfenced separators="|"><mrow><mi>&#955;</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math>
<math><msub><mrow><mo>&#8710;</mo></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#956;</mi></mtd><mtd><mi>&#955;</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>+</mo><mn>4</mn></math>
<math><msub><mrow><mo>&#8710;</mo></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#956;</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi>&#956;</mi><mo>-</mo><mn>7</mn></math>
For infinite many solution <math><mo>&#8710;</mo><mo>=</mo><msub><mrow><mo>&#8710;</mo></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><msub><mrow><mo>&#8710;</mo></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><msub><mrow><mo>&#8710;</mo></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><mi>&#956;</mi><mo>=</mo><mn>7</mn><mi>&#160;</mi></math> from <math><mi>&#160;</mi><mo>&#8710;</mo><mo>=</mo><mn>0</mn><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><msub><mrow><mo>&#8710;</mo></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mn>0</mn></math>
&amp; <math><mi>&#160;</mi><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mi>&#956;</mi><mo>=</mo><mn>7</mn><mi>&#160;</mi></math> Satisfies <math><msub><mrow><mo>&#8710;</mo></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>0</mn><mo>=</mo><msub><mrow><mo>&#8710;</mo></mrow><mrow><mn>1</mn></mrow></msub></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>=</mo><mn>10</mn></math>

</details>

---

### Q106. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the system of equations <math><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>,</mo><mtext>&#8201;</mtext><mi>x</mi><mo>+</mo><mi>k</mi><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn></math> and <math><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math> has a non-trivial solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi></mrow></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>+</mo><mfrac><mi>y</mi><mi>z</mi></mfrac><mo>+</mo><mfrac><mi>z</mi><mi>x</mi></mfrac><mo>+</mo><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mn>4</mn></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>The system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><mi>z</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mi>z</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>3</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mi>z</mi><mo>=</mo><mn>0</mn></math> has a non-trivial solution, if </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>.</mo></math></p><p>Hence, for the given lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mi>k</mi><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>k</mi></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mi>k</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>k</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>k</mi><mo>-</mo><mn>4</mn><mo>-</mo><mn>15</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>k</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></math></p><p>Thus, the lines are </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>-</mo><mfenced><mn>3</mn></mfenced><mo>&#8658;</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mo>=</mo><mi>z</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><mi>z</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>5</mn></mfenced></math></p><p>put <math><mi>z</mi></math> from eq <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math> into <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p><math><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>6</mn></mfenced></math></p><p>From eq <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>6</mn></mfenced></math></p><p><math><mfrac><mrow><mi>z</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>+</mo><mfrac><mi>y</mi><mi>z</mi></mfrac><mo>+</mo><mfrac><mi>z</mi><mi>x</mi></mfrac><mo>+</mo><mi>k</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mn>4</mn><mo>+</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q107. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the system of linear equations
<math><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>k</mi><mi>z</mi><mo>=</mo><mn>1</mn></math>
<math><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>2</mn></math>
<math><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mi>k</mi><mi>z</mi><mo>=</mo><mn>3</mn></math>
has a solution <math><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mi>z</mi></mrow></mfenced><mo>,</mo><mi>z</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo></math> then <math><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced></math> lies on the straight line whose equation is:

**Options:**

- **(A)** <math><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math><mn>3</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mn>3</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p><math><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>k</mi><mi>z</mi><mo>=</mo><mn>1</mn></math> .........(1)
<math><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>2</mn></math> .........(2)
<math><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mi>k</mi><mi>z</mi><mo>=</mo><mn>3</mn></math> ........(3)
 </p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mi>k</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mi>k</mi></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd></mtr><mtr><mtd><mi>z</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p>For infinite solution,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mi>k</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mi>k</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mo>-</mo><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>2</mn><mi>k</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mi>k</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Put this value in the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>2</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>Adding the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>4</mn></math></p><p>Hence, the equation of straight line is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q108. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The greatest value of <math><mi>c</mi><mo>&#8712;</mo><mi>R</mi></math> for which the system of linear equations <math><mi>x</mi><mo>-</mo><mi>c</mi><mi>y</mi><mo>-</mo><mi>c</mi><mi>z</mi><mo>=</mo><mn>0</mn></math>, <math><mi>c</mi><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>c</mi><mi>z</mi><mo>=</mo><mn>0</mn></math>, <math><mi>c</mi><mi>x</mi><mo>+</mo><mi>c</mi><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn></math> has a non-trivial solution, is

**Options:**

- **(A)** <math><mo>-</mo><mn>1</mn></math>
- **(B)** <math><mn>2</mn></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math><mo>&#8757;</mo></math> System of equation has non trivial solution. It is possible only when <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mn>0</mn></math>.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#8710;</mo><mi>&#160;</mi><mo>=</mo><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>c</mi></mtd><mtd><mo>-</mo><mi>c</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>c</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mn>1</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>+</mo><mi>c</mi><mfenced separators="|"><mrow><mo>-</mo><mi>c</mi><mo>-</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>-</mo><mi>c</mi><mfenced separators="|"><mrow><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><msup><mrow><mn>2</mn><mi>c</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>3</mn><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>&#160;</mi></math></p><p>Hence, the greatest value of <math><mi>c</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>.</p>

</details>

---

### Q109. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The set of all values of <math><mi>&#955;</mi></math> for which the system of linear equations
<math><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mi>&#955;</mi><mi>x</mi></math>
<math><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>&#955;</mi><mi>y</mi></math>
<math><mo>-</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mi>&#955;</mi><mi>z</mi></math>
has a non-trivial solution :

**Options:**

- **(A)** is an empty set
- **(B)** contains more than two elements
- **(C)** is a singleton
- **(D)** contains exactly two elements

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) is a singleton**

**Detailed Solution:**

<p>For non-trivial solution, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mn>0</mn></math>.</p><p><math><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn><mo>-</mo><mi>&#955;</mi></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn><mo>-</mo><mi>&#955;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mi>&#955;</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced separators="|"><mrow><mo>-</mo><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mi>&#160;</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><msup><mrow><mfenced separators="|"><mrow><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>1</mn></math></p><p>Singleton set</p>

</details>

---

### Q110. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An ordered pair <math><mfenced separators="|"><mrow><mi>&#945;</mi><mo>,</mo><mi>&#160;</mi><mi>&#946;</mi></mrow></mfenced></math> for which the system of linear equations
<math><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mi>&#946;</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>2</mn></math>
<math><mi>&#945;</mi><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>3</mn></math>
<math><mi>&#945;</mi><mi>x</mi><mo>+</mo><mi>&#946;</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>2</mn></math> has a unique solution, is :

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mi> </mi><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi> </mi><mn>4</mn></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mi> </mi><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi> </mi><mn>4</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>For unique solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p>Applying <math><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>&#8594;</mo><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mn>2</mn></mtd><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mn>2</mn></mtd><mtd><mn>1</mn><mo>+</mo><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mn>2</mn></mtd><mtd><mi>&#946;</mi></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn><mo>+</mo><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#946;</mi></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mn>2</mn><mo>&#8800;</mo><mn>0</mn></math></p><p>Clearly, point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn></mrow></mfenced></math> satisfying the given condition.</p>

</details>

---

### Q111. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the system of linear equations $2 x+2 y+3 z=a$

$3 x-y+5 z=b$

$x-3 y+2 z=c$

where, $a, b,$ care non-zero real numbers, has more than onc solution, then

**Options:**

- **(A)** $b-c+a=0$
- **(B)** $b-c-a=0$
- **(C)** $a+b+c=0$
- **(D)** $b+c-a=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $b-c-a=0$**

**Detailed Solution:**

$\because$ System of equations has more than one solution

$\therefore \Delta=\Delta_{1}=\Delta_{2}=\Delta_{3}=0$ for infinite solution

$\begin{aligned}

\Delta_{1} &=\left|\begin{array}{ccc}

a & 2 & 3 \\

b & -1 & 5 \\

c & -3 & 2

\end{array}\right|=a(13)+2(5 c-2 b)+3(-3 b+c) \\

&=13 a-13 b+13 c=0

\end{aligned}$

i.c, $a-b+c=0$

or $\quad b-c-a=0$

</details>

---

### Q112. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of values of <math><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#960;</mi></mrow></mfenced></math> for which the system of linear equations
<math><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math><mo>-</mo><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>3</mn><mi>&#952;</mi></mrow></mrow></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>&#952;</mi></mrow></mrow></mrow></mfenced><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
has a non-trivial solution, is:

**Options:**

- **(A)** Two
- **(B)** Three
- **(C)** Four
- **(D)** One

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Two**

**Detailed Solution:**

<p>For non-trivial solutions

<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>7</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>7</mn></mtd></mtr><mtr><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>3</mn><mi>&#952;</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>&#952;</mi></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mn>4</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>3</mn></mrow></msup><mi>&#952;</mi><mo>+</mo><mn>4</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi><mo>-</mo><mn>3</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn></math> or <math><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>

Since <math><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mtext>&#8201;</mtext><mi>&#960;</mi></mrow></mfenced></math>

<math><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math> and <math><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math> will satisfy the equation</p><p>because <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math> is not possible as range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#952;</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>

<math><mo>&#8658;</mo></math> Number of <math><mi>&#952;</mi></math> &#39; <math><mi>s</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q113. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the system of equations <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>5</mn><mo>,</mo></math> <math><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>9</mn><mo>,</mo></math> <math><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mi>&#946;</mi></math> has inifinitely many solutions, then <math><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi></math> equals

**Options:**

- **(A)** <math><mn>8</mn></math>
- **(B)** <math><mn>21</mn></math>
- **(C)** <math><mn>5</mn></math>
- **(D)** <math><mn>18</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>8</mn></math>**

**Detailed Solution:**

<p>The system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><mi>z</mi><mo>+</mo><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mi>z</mi><mo>+</mo><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>3</mn></msub><mi>y</mi><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mi>z</mi><mo>+</mo><msub><mi>d</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math> have infinitely many solutions, if</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>d</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>d</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>d</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>d</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>d</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>d</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>d</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>d</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>d</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>.</mo></math></p><p>Hence, for the system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>9</mn></math> and <math><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mi>&#946;</mi></math> have infinitely many solution, if</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>9</mn></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mi>&#945;</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>9</mn><mo>-</mo><mi>&#945;</mi><mo>+</mo><mn>3</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>5</mn><mo>.</mo></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>5</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>5</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mfenced><mrow><mn>10</mn><mo>-</mo><mn>9</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>45</mn><mo>-</mo><mn>3</mn><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>27</mn><mo>-</mo><mn>2</mn><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mo>-</mo><mn>45</mn><mo>+</mo><mn>3</mn><mi>&#946;</mi><mo>+</mo><mn>27</mn><mo>-</mo><mn>2</mn><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>13</mn><mo>.</mo></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi><mo>=</mo><mn>13</mn><mo>-</mo><mn>5</mn><mo>=</mo><mn>8</mn><mo>.</mo></math></p>

</details>

---

### Q114. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mi>g</mi></math>; <math><mn>3</mn><mi>y</mi><mo>-</mo><mn>5</mn><mi>z</mi><mo>=</mo><mi>h</mi></math>; <math><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>-</mo><mn>9</mn><mi>z</mi><mo>=</mo><mi>k</mi></math> is consistent, then:

**Options:**

- **(A)** <math><mi>g</mi><mo>+</mo><mi>h</mi><mo>+</mo><mn>2</mn><mi>k</mi><mo>=</mo><mn>0</mn></math>
- **(B)** <math><mi>g</mi><mo>+</mo><mn>2</mn><mi>h</mi><mo>+</mo><mi>k</mi><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mn>2</mn><mi>g</mi><mo>+</mo><mi>h</mi><mo>+</mo><mi>k</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math><mi>g</mi><mo>+</mo><mi>h</mi><mo>+</mo><mi>k</mi><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>2</mn><mi>g</mi><mo>+</mo><mi>h</mi><mo>+</mo><mi>k</mi><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<math><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mi>g</mi></math> ...(i)

<math><mn>3</mn><mi>y</mi><mo>-</mo><mn>5</mn><mi>z</mi><mo>=</mo><mi>h</mi></math> ...(ii)

<math><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>-</mo><mn>9</mn><mi>z</mi><mo>=</mo><mi>k</mi></math> ...(iii)

(i) + (ii), we get

<math><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mi>g</mi><mo>+</mo><mi>h</mi></math> ...(iv)

(ii) - (iii), we get

<math><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mi>h</mi><mo>-</mo><mi>k</mi></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mfrac><mrow><mi>h</mi><mo>-</mo><mi>k</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math> ...(v)

Since, coefficient of <math><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mi>z</mi></math> in (iv) and (v) are same. Hence, for system to be consistent

<math><mi>g</mi><mo>+</mo><mi>h</mi><mo>=</mo><mfrac><mrow><mi>h</mi><mo>-</mo><mi>k</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mn>2</mn><mi>g</mi><mo>+</mo><mn>2</mn><mi>h</mi><mo>=</mo><mi>h</mi><mo>-</mo><mi>k</mi></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mn>2</mn><mi>g</mi><mo>+</mo><mi>h</mi><mo>+</mo><mi>k</mi><mo>=</mo><mn>0</mn></math>

</details>

---

### Q115. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The system of linear equations
<math><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>2</mn></math>
<math><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>5</mn></math>
<math><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mfenced separators="|"><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>z</mi><mo>=</mo><mi>a</mi><mo>+</mo><mn>1</mn></math>

**Options:**

- **(A)** is inconsistent when  <math><mfenced close="|" open="|" separators="|"><mrow><mi>a</mi></mrow></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt></math>
- **(B)** has a unique solution for  <math><mfenced close="|" open="|" separators="|"><mrow><mi>a</mi></mrow></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt></math>
- **(C)** has infinitely many solutions for  <math><mi>a</mi><mo>=</mo><mn>4</mn></math>
- **(D)** is inconsistent when  <math><mi>a</mi><mo>=</mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) is inconsistent when  <math><mfenced close="|" open="|" separators="|"><mrow><mi>a</mi></mrow></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

Here,  <math><mi>D</mi><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> 

         <math><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn></math> 

        Hence at  <math><mo>|</mo><mi>a</mi><mo>|</mo><mo>=</mo><msqrt><mn>3</mn></msqrt></math> ,  <math><mi>D</mi><mo>=</mo><mn>0</mn></math> . So system don't have unique solution.

        At  <math><mi>a</mi><mo>=</mo><mn>4</mn></math> ,  <math><mi>D</mi><mo>≠</mo><mn>0</mn></math> , So, system has unique solution. Hence not inconsistent.

        At  <math><mo>|</mo><mi>a</mi><mo>|</mo><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>,</mo><mi>D</mi><mo>=</mo><mn>0</mn></math>  and  <math><msup><mrow><mn>2</mn></mrow><mrow><mi>n</mi><mi>d</mi></mrow></msup></math>  &  <math><msup><mrow><mn>3</mn></mrow><mrow><mi>r</mi><mi>d</mi></mrow></msup></math>  equation are parallel. Hence no solution are possible.

        Hence, system is inconsistent for  <math><mo>|</mo><mi>a</mi><mo>|</mo><mo>=</mo><msqrt><mn>3</mn></msqrt></math>

</details>

---

### Q116. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The number of values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> for which the system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mn>10</mn><mi>y</mi><mo>=</mo><mi>k</mi><mo>&#160;</mo><mo>&#38;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mi>y</mi><mo>=</mo><mi>k</mi><mo>-</mo><mn>1</mn></math> has no solution is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>For no solution</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow><mi>k</mi></mfrac><mo>=</mo><mfrac><mn>10</mn><mrow><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mi>k</mi><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>10</mn><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>k</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8800;</mo><mn>2</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>2</mn></math> both lines are identical.</p><p>So, only <math><mi>k</mi><mo>=</mo><mn>3</mn></math> is possible.</p><p>So the number of values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>.</p>

</details>

---

### Q117. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `2`

If the system of linear equations
$$
\begin{aligned}
&x+a y+z=3 \\
&x+2 y+2 z=6 \\
&x+5 y+3 z=b
\end{aligned}
$$
has no solution, then

**Options:**

- **(A)** $a=1, b \neq 9$
- **(B)** $a \neq-1, b=9$
- **(C)** $a=-1, b=9$
- **(D)** $a=-1, b \neq 9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a=-1, b \neq 9$**

**Detailed Solution:**

As the system of equations has no solution then $\Delta$ should be zero and at least one of $\Delta_1$, $\Delta_2$ and $\Delta_3$ should not be zero.
$$
\begin{aligned}
&\therefore \Delta=\left|\begin{array}{lll}
1 & a & 1 \\
1 & 2 & 2 \\
1 & 5 & 3
\end{array}\right|=0 \\
&\Rightarrow-a-1=0 \Rightarrow a=-1 \\
&\Delta_2=\left|\begin{array}{lll}
1 & 3 & 1 \\
1 & 6 & 2 \\
1 & b & 3
\end{array}\right| \neq 0 \\
&\Rightarrow b \neq 9
\end{aligned}
$$

</details>

---

### Q118. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all real values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> for which the system of linear equations
<math><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>2</mn></math>
<math><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>3</mn></math>
<math><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>k</mi><mi>z</mi><mo>=</mo><mn>4</mn></math>
has a unique solution. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>&#160;</mo></math>is :

**Options:**

- **(A)** equal to <math><mi>R</mi><mi> </mi><mo>–</mo><mo>{</mo><mn>0</mn><mo>}</mo></math>
- **(B)** an empty set
- **(C)** equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>
- **(D)** equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mn>0</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) equal to <math><mi>R</mi><mi> </mi><mo>–</mo><mo>{</mo><mn>0</mn><mo>}</mo></math>**

**Detailed Solution:**

<p>For unique solution, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>k</mi></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mfenced separators="|"><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced separators="|"><mrow><mn>2</mn><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mo>&#8658;</mo><mo>-</mo><mi>k</mi><mo>&#8800;</mo><mn>0</mn><mo>&#8658;</mo><mi>k</mi><mo>&#8800;</mo><mn>0</mn></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mn>0</mn></mfenced></math></p>

</details>

---

### Q119. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $S$ be the set of all real values of $k$ for which the system of linear equations
$$
\begin{aligned}
&x+y+z=2 \\
&2 x+y-z=3 \\
&3 x+2 y+k z=4
\end{aligned}
$$
has a unique solution. Then $S$ is

**Options:**

- **(A)** an empty set
- **(B)** equal to $\mathrm{R}-\{0\}$
- **(C)** equal to $\{0\}$
- **(D)** equal to $\mathrm{R}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) equal to $\mathrm{R}-\{0\}$**

**Detailed Solution:**

The system of linear equations is:
$$
\begin{aligned}
&x+y+z=2 \\
&2 x+y-z=3 \\
&3 x+2 y+k z=4
\end{aligned}
$$
As, system has unique solution.
$$
\begin{aligned}
&\text { So, }\left|\begin{array}{ccc}
1 & 1 & 1 \\
2 & 1 & -1 \\
3 & 2 & k
\end{array}\right| \neq 0 \\
&\Rightarrow k+2-(2 k+3)+1 \neq 0 \\
&\Rightarrow k \neq 0
\end{aligned}
$$
Hence, $k \in R-\{0\} \equiv S$

</details>

---

### Q120. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `1`

<p>If the system of linear equations</p><p><math><mi>x</mi><mo>+</mo><mi>k</mi><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math><mn>3</mn><mi>x</mi><mo>+</mo><mi>k</mi><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p>has a non-zero solution <math><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>,</mo><mi>&#160;</mi><mi>z</mi></mrow></mfenced><mo>,</mo></math> then <math><mfrac><mrow><mi>x</mi><mi>z</mi></mrow><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>
- **(B)** <math><mo>-</mo><mn>10</mn></math>
- **(C)** <math><mn>10</mn></math>
- **(D)** <math><mo>-</mo><mn>30</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>10</mn></math>**

**Detailed Solution:**

<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>k</mi></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mi>k</mi></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>8</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn><mi>k</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced separators="|"><mrow><mo>-</mo><mn>5</mn><mi>k</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>4</mn><mi>k</mi><mo>+</mo><mn>44</mn><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math><mi>k</mi><mo>=</mo><mn>11</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mn>11</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>11</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math>

On solving equations<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we get

<math><mn>2</mn><mi>x</mi><mo>-</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mi>z</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>

Put it in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math>, we get

<math><mn>2</mn><mi>z</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>y</mi></math>

<math><mo>&#8756;</mo><mfrac><mrow><mi>x</mi><mi>z</mi></mrow><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn><mi>y</mi></mrow></mfenced><mo>&#215;</mo><mfenced separators="|"><mrow><mo>-</mo><mn>5</mn><mi>y</mi></mrow></mfenced></mrow><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>10</mn></math>

</details>

---

### Q121. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>x</mi><mo>=</mo><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>=</mo><mi>b</mi><mo>,</mo><mi>&#160;</mi><mi>z</mi><mo>=</mo><mi>c</mi></math> is a solution of the system of linear equations
<math><mi>x</mi><mo>+</mo><mn>8</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math><mn>9</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>
Such that the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></math>  lies on the plane <math><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>6</mn></math> , then <math><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></math> equals:

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mo>-</mo><mn>1</mn></math>
- **(C)** <math><mn>1</mn></math>
- **(D)** <math><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mn>8</mn><mi>y</mi><mo>+</mo><mn>7</mn><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mtd></mtr><mtr><mtd><mn>9</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mtd></mtr></mtable></math>.....</p><p>Solve the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mi>y</mi><mo>+</mo><mn>6</mn><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p>Solve the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mi>x</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#955;</mi><mi>&#160;</mi><mo>&#38;</mo><mo>&#160;</mo><mfenced close="|" open="|" separators="|"><mrow><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>6</mn><mfenced separators="|"><mrow><mo>-</mo><mn>7</mn><mi>&#955;</mi></mrow></mfenced></mrow><mn>7</mn></mfrac></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>7</mn><mi>&#955;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>x</mi><mo>=</mo><mi>&#955;</mi></mtd><mtd><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>6</mn><mi>&#955;</mi></mtd><mtd><mo>&#38;</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>7</mn><mi>&#955;</mi></mtd></mtr></mtable></math>

  <math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mtable><mtr><mtd><mo>&#8658;</mo><mi>&#955;</mi><mo>+</mo><mn>12</mn><mi>&#955;</mi><mo>&#8722;</mo><mn>7</mn><mi>&#955;</mi><mo>=</mo><mn>6</mn></mtd></mtr><mtr><mtd><mo>&#8658;</mo><mn>6</mn><mi>&#955;</mi><mo>=</mo><mn>6</mn></mtd></mtr><mtr><mtd><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>1</mn></mtd></mtr></mtable><mtext>&#8201;</mtext><mo>|</mo></mrow><mtext>&#8201;</mtext><mtable><mtr><mtd><mo>&#8658;</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>6</mn><mi>&#955;</mi><mo>&#8722;</mo><mn>7</mn><mi>&#955;</mi></mtd></mtr><mtr><mtd><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>1</mn></mtd></mtr></mtable></math>

Hence, <math><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>b</mi><mo>=</mo><mn>6</mn><mo>,</mo><mi>&#160;</mi><mi>c</mi><mo>=</mo><mo>-</mo><mn>7</mn></math>

<math><mo>&#8756;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q122. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

<p>The number of real values of <math><mi>&#955;</mi></math> for which the system of linear equations, <math><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>-</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mn>0</mn></math>, <math><mn>4</mn><mi>x</mi><mo>+</mo><mi>&#955;</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn></math> and <math><mi>&#955;</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn></math>, has infinitely many solutions, is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>For Infinite many solution <math><mi mathvariant="normal">&#916;</mi><mo>=</mo><mn>0</mn></math>

i.e , <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mo>&#955;</mo></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>&#955;</mo></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>&#955;</mo></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mo>-</mo><mn>4</mn><mfenced><mrow><mn>8</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mo>-</mo><mi>&#955;</mi><mfenced><mrow><mn>8</mn><mo>-</mo><msup><mi>&#955;</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mo>&#955;</mo><mn>3</mn></msup><mo>+</mo><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>40</mn><mo>=</mo><mn>0&#160;</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>40</mn></math> is strictly increasing</p><p>i.e., equation has only one real root,

Also, <math><msub><mrow><mo>&#8710;</mo></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0</mn></math>, <math><msub><mrow><mo>&#8710;</mo></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math>, <math><msub><mrow><mo>&#8710;</mo></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>0</mn></math>

<math><mo>&#8756;</mo></math> Only one value of <math><mi>&#955;</mi></math> is possible</p>

</details>

---

### Q123. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is the set of distinct values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> for which the following system of linear equations

<math><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math>

<math><mi>x</mi><mo>+</mo><mi>a</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math>

<math><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>

has no solution, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>  is:

**Options:**

- **(A)** An empty set
- **(B)** An infinite set
- **(C)** A finite set containing two or more elements
- **(D)** A singleton

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) A singleton**

**Detailed Solution:**

<p>For no solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Expanding the determinant along the first row, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mo>-</mo><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>a</mi><mo>=</mo><mn>1</mn></math></p><p>For <math><mi>a</mi><mo>=</mo><mn>1</mn></math>, first two planes are coincident.</p><p>Now, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p>For no solution, these two planes are parallel.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>1</mn></math>.</p><p><math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>b</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&#160;&#8658;&#160;</mo></math>it is a singleton set</p>

</details>

---

### Q124. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `1`

The system of linear equations

<math><mi>x</mi><mo>+</mo><mi>&#955;</mi><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>

<math><mi>&#955;</mi><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>

<math><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mn>0</mn></math>

has a non -trivial solution for

**Options:**

- **(A)** Exactly two values of  <math><mi>λ</mi></math>
- **(B)** Exactly three values of  <math><mi>λ</mi></math>
- **(C)** Infinitely many values of  <math><mi>λ</mi></math>
- **(D)** Exactly one value of  <math><mi>λ</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Exactly three values of  <math><mi>λ</mi></math>**

**Detailed Solution:**

For non - trivial solution.

 <math><mi mathvariant="normal">Δ</mi><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>λ</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>λ</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>λ</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math> 

 <math><mn>1</mn><mfenced separators="|"><mrow><mi>λ</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>λ</mi><mfenced separators="|"><mrow><mo>-</mo><msup><mrow><mi>λ</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced separators="|"><mrow><mi>λ</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> 

 <math><mfenced separators="|"><mrow><mi>λ</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>λ</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>λ</mi></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>λ</mi></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mi>λ</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> 

 <math><mi>λ</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>λ</mi></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>λ</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mi> </mi></math> 

 <math><mi>λ</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>λ</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi>λ</mi><mo>=</mo><mi> </mi><mo>-</mo><mn>1</mn></math> 

Exactly there value of  <math><mi>λ</mi><mo>.</mo></math>

</details>

---

### Q125. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The set of all values of <math> <mrow> <mi>&#955;</mi> </mrow> </math> for which the system of linear equations:
<math> <mrow> <mn>2</mn> <msub> <mi>x</mi> <mn>1</mn> </msub> <mo>-</mo> <mn>2</mn> <msub> <mi>x</mi> <mn>2</mn> </msub> <mo>+</mo> <msub> <mi>x</mi> <mn>3</mn> </msub> <mo>=</mo> <mi>&#955;</mi> <msub> <mi>x</mi> <mn>1</mn> </msub> </mrow> </math>
<math> <mrow> <mn>2</mn> <msub> <mi>x</mi> <mn>1</mn> </msub> <mo>-</mo> <mn>3</mn> <msub> <mi>x</mi> <mn>2</mn> </msub> <mo>+</mo> <msub> <mrow> <mn>2</mn> <mi>x</mi> </mrow> <mn>3</mn> </msub> <mo>=</mo> <mi>&#955;</mi> <msub> <mi>x</mi> <mn>2</mn> </msub> </mrow> </math>
<math> <mrow> <mo>-</mo> <msub> <mi>x</mi> <mn>1</mn> </msub> <mo>+</mo> <msub> <mrow> <mn>2</mn> <mi>x</mi> </mrow> <mn>2</mn> </msub> <mo>=</mo> <mi>&#955;</mi> <msub> <mi>x</mi> <mn>3</mn> </msub> </mrow> </math>
has a non-trivial solution,

**Options:**

- **(A)** Contains more than two elements.
- **(B)** Is an empty set.
- **(C)** Is a singleton.
- **(D)** Contains two elements.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Contains two elements.**

**Detailed Solution:**

<math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>2</mn> <mo>-</mo> <mi>λ</mi> </mrow> </mfenced> <msub> <mi>x</mi> <mn>1</mn> </msub> <mo>-</mo> <mn>2</mn> <msub> <mi>x</mi> <mn>2</mn> </msub> <mo>+</mo> <msub> <mi>x</mi> <mn>3</mn> </msub> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <mn>2</mn> <msub> <mi>x</mi> <mn>1</mn> </msub> <mo>-</mo> <mfenced close=")" open="(" separators=","> <mrow> <mi>λ</mi> <mo>+</mo> <mn>3</mn> </mrow> </mfenced> <msub> <mi>x</mi> <mn>2</mn> </msub> <mo>+</mo> <mn>2</mn> <msub> <mi>x</mi> <mn>3</mn> </msub> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <mo>-</mo> <msub> <mi>x</mi> <mn>1</mn> </msub> <mo>+</mo> <mn>2</mn> <msub> <mi>x</mi> <mn>2</mn> </msub> <mo>-</mo> <mi>λ</mi> <msub> <mi>x</mi> <mn>3</mn> </msub> <mo>=</mo> <mn>0</mn> </mrow> </math>

The systems of linear equations will have a non-trivial solution

<math> <mrow> <mo>⇒    </mo> <mfenced close="|" open="|" separators=","> <mrow> <mtable> <mtr> <mtd> <mn>2</mn> <mo>-</mo> <mi>λ</mi> </mtd> <mtd> <mo>-</mo> <mn>2</mn> </mtd> <mtd> <mn>1</mn> </mtd> </mtr> <mtr> <mtd> <mn>2</mn> </mtd> <mtd> <mo>-</mo> <mi>λ</mi> <mo>-</mo> <mn>3</mn> </mtd> <mtd> <mn>2</mn> </mtd> </mtr> <mtr> <mtd> <mo>-</mo> <mn>1</mn> </mtd> <mtd> <mn>2</mn> </mtd> <mtd> <mo>-</mo> <mi>λ</mi> </mtd> </mtr> </mtable> </mrow> </mfenced> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <mo>⇒    </mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>2</mn> <mo>-</mo> <mi>λ</mi> </mrow> </mfenced> <mfenced close="]" open="[" separators=","> <mrow> <msup> <mi>λ</mi> <mn>2</mn> </msup> <mo>+</mo> <mn>3</mn> <mi>λ</mi> <mo>-</mo> <mn>4</mn> </mrow> </mfenced> <mo>+</mo> <mn>2</mn> <mfenced close="]" open="[" separators=","> <mrow> <mo>-</mo> <mn>2</mn> <mi>λ</mi> <mo>+</mo> <mn>2</mn> </mrow> </mfenced> <mo>+</mo> <mn>1</mn> <mfenced close="]" open="[" separators=","> <mrow> <mn>4</mn> <mo>-</mo> <mi>λ</mi> <mo>-</mo> <mn>3</mn> </mrow> </mfenced> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <mn>2</mn> <msup> <mi>λ</mi> <mn>2</mn> </msup> <mo>+</mo> <mn>6</mn> <mi>λ</mi> <mo>-</mo> <mn>8</mn> <mo>-</mo> <msup> <mi>λ</mi> <mn>3</mn> </msup> <mo>-</mo> <mn>3</mn> <msup> <mi>λ</mi> <mn>2</mn> </msup> <mo>+</mo> <mn>4</mn> <mi>λ</mi> <mo>-</mo> <mn>4</mn> <mi>λ</mi> <mo>+</mo> <mn>4</mn> <mo>+</mo> <mn>1</mn> <mo>-</mo> <mi>λ</mi> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <mo>-</mo> <msup> <mi>λ</mi> <mn>3</mn> </msup> <mo>-</mo> <msup> <mi>λ</mi> <mn>2</mn> </msup> <mo>+</mo> <mn>5</mn> <mi>λ</mi> <mo>-</mo> <mn>3</mn> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <msup> <mi>λ</mi> <mn>3</mn> </msup> <mo>+</mo> <msup> <mi>λ</mi> <mn>2</mn> </msup> <mo>-</mo> <mn>5</mn> <mi>λ</mi> <mo>+</mo> <mn>3</mn> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mi>λ</mi> <mo>-</mo> <mn>1</mn> </mrow> </mfenced> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mi>λ</mi> <mn>2</mn> </msup> <mo>+</mo> <mn>2</mn> <mi>λ</mi> <mo>-</mo> <mn>3</mn> </mrow> </mfenced> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mi>λ</mi> <mo>-</mo> <mn>1</mn> </mrow> </mfenced> <mfenced close=")" open="(" separators=","> <mrow> <mi>λ</mi> <mo>+</mo> <mn>3</mn> </mrow> </mfenced> <mfenced close=")" open="(" separators=","> <mrow> <mi>λ</mi> <mo>-</mo> <mn>1</mn> </mrow> </mfenced> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <mo>⇒   </mo> <mi>λ</mi> <mo>=</mo> <mn>-3</mn> <mo>,</mo>  <mn>1</mn> <mo>,</mo> <mn>1</mn> </mrow> </math>

</details>

---

### Q126. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></math>  are non - zero real numbers and if the system of equations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mo>=</mo><mi>y</mi><mo>+</mo><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>c</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>y</mi></math></p><p>has a non - trivial solution, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>a</mi></math>  equals :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi></math>**

**Detailed Solution:**

Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mo>=</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>y</mi><mo>=</mo><mi>z</mi><mo>+</mo><mi>x</mi><mo>&#8658;</mo><mo>-</mo><mi>x</mi><mo>+</mo><mfenced><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>c</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>z</mi><mo>=</mo><mi>y</mi><mo>+</mo><mi>x</mi><mo>=</mo><mo>-</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mfenced><mrow><mi>c</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>z</mi><mo>=</mo><mn>0</mn></math>

For a non-trivial solution

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>a</mi><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>b</mi><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>c</mi><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn><mo>-</mo><mi>a</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn><mo>-</mo><mi>b</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn><mo>-</mo><mi>c</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced open="[" close="]"><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced open="[" close="]"><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced open="[" close="]"><mrow><mn>1</mn><mo>-</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>b</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><mn>1</mn><mo>-</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>a</mi></mrow></mfenced><mo>-</mo><mi>a</mi><mi>b</mi><mi>c</mi><mo>-</mo><mn>1</mn><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>a</mi><mo>=</mo><mi>a</mi><mi>b</mi><mi>c</mi></math>

</details>

---

### Q127. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Statement-1: The system of linear equations
$$
\begin{aligned}
& x+(\sin \alpha) y+(\cos \alpha) z=0 \\
& x+(\cos \alpha) y+(\sin \alpha) z=0 \\
& x-(\sin \alpha) y-(\cos \alpha) z=0
\end{aligned}
$$
has a non-trivial solution for only one value of $\alpha$
lying in the interval $\left(0, \frac{\pi}{2}\right)$.
Statement-2: The equation in $\alpha$
$$
\left|\begin{array}{ccc}
\cos \alpha & \sin \alpha & \cos \alpha \\
\sin \alpha & \cos \alpha & \sin \alpha \\
\cos \alpha & -\sin \alpha & -\cos \alpha
\end{array}\right|=0
$$
has only one solution lying in the interval
$\left(0, \frac{\pi}{2}\right)$

**Options:**

- **(A)** Statement-1 is true, Statement-2 is true, Statement-2 is not correct explantion for Statement-1.
- **(B)** Statement-1 is true, Statement-2 is true, Statement-2 is a correct explantion for Statement-1.
- **(C)** Statement-1 is true, Statement- 2 is false.
- **(D)** Statememt-1 is false, Statement-2 is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement-1 is true, Statement- 2 is false.**

**Detailed Solution:**

$$
\begin{aligned}
& \Rightarrow \alpha=\frac{64 x}{3 \times 16 x}=\frac{4}{3} \\
& \Delta_1=\left|\begin{array}{ccc}
1 & \sin \alpha & \cos \alpha \\
1 & \cos \alpha & \sin \alpha \\
1 & -\sin \alpha & \cos \alpha
\end{array}\right| \\
& =\left|\begin{array}{ccc}
0 & \sin \alpha-\cos \alpha & \cos \alpha-\sin \alpha \\
0 & \cos \alpha+\sin \alpha & \sin \alpha-\cos \alpha \\
1 & -\sin \alpha & \cos \alpha
\end{array}\right| \\
& =(\sin \alpha-\cos \alpha)^2-\left(\cos ^2 \alpha-\sin ^2 \alpha\right) \\
& =\sin ^2 \alpha+\cos ^2 \alpha-2 \sin \alpha \cdot \cos \alpha-\cos ^2 \alpha \\
& =2 \sin ^2 \alpha-2 \sin \alpha \cdot \cos \alpha \\
& =2 \sin ^2 \alpha(\sin \alpha-\cos \alpha)
\end{aligned}
$$
Now, $\sin \alpha-\cos \alpha=0$ for only
$$
\begin{aligned}
\alpha & =\frac{\pi}{4} \text { in }\left(0, \frac{\pi}{2}\right) \\
\therefore \quad \Delta_1 & =2(\sin \alpha) \times 0=0,
\end{aligned}
$$
since value of $\sin \alpha$ is finite for $\alpha \in\left(0, \frac{\pi}{2}\right)$
Hence non-trivivial solution for only one value of $\alpha$ in $\left(0, \frac{\pi}{2}\right)$
$$
\begin{aligned}
& \left|\begin{array}{ccc}
\cos \alpha & \sin \alpha & \cos \alpha \\
\sin \alpha & \cos \alpha & \sin \alpha \\
\cos \alpha & -\sin \alpha & -\cos \alpha
\end{array}\right|=0 \\
& \Rightarrow\left|\begin{array}{ccc}
0 & \sin \alpha & \cos \alpha \\
0 & \cos \alpha & \sin \alpha \\
2 \cos \alpha & -\sin \alpha & -\cos \alpha
\end{array}\right|=0 \\
& \Rightarrow 2 \cos \alpha\left(\sin ^2 \alpha-\cos ^2 \alpha\right)=0 \\
& \therefore \cos \alpha=0 \text { or } \sin ^2 \alpha-\cos ^2 \alpha=0
\end{aligned}
$$
But $\cos \alpha=0$ not possible for any value of
$$
\begin{aligned}
& \alpha \in\left(0, \frac{\pi}{2}\right) \\
& \therefore \sin ^2 \alpha-\cos ^2 \alpha=0 \Rightarrow \sin \alpha=-\cos \alpha,
\end{aligned}
$$
which is also not possible for any value of
$$
\alpha \in\left(0, \frac{\pi}{2}\right)
$$
Hence, there is no solution.

</details>

---

### Q128. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If the system of linear equations :
$$
\begin{aligned}
& x_1+2 x_2+3 x_3=6 \\
& x_1+3 x_2+5 x_3=9 \\
& 2 x_1+5 x_2+a x_3=b
\end{aligned}
$$
is consistent and has infinite number of solutions, then :

**Options:**

- **(A)** $a=8, b$ can be any real number
- **(B)** $b=15, a$ can be any real number
- **(C)** $a \in R-\{8\}$ and $b \in R-\{15\}$
- **(D)** $a=8, b=15$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a=8, b=15$**

**Detailed Solution:**

Given system of equations can be written in matrix form as $\mathrm{AX}=\mathrm{B}$ where $\mathrm{A}=\left(\begin{array}{lll}1 & 2 & 3 \\ 1 & 3 & 5 \\ 2 & 5 & a\end{array}\right)$ and $\mathrm{B}=\left(\begin{array}{l}6 \\ 9 \\ b\end{array}\right)$
Since, system is consistent and has infinitely many solutions
$\therefore(\operatorname{adj} . \mathrm{A}) \mathrm{B}=0$

$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{ccc}
3 a-25 & 15-2 a & 1 \\
10-a & a-6 & -2 \\
-1 & -1 & 1
\end{array}\right)\left(\begin{array}{l}
6 \\
9 \\
b
\end{array}\right)=\left(\begin{array}{l}
0 \\
0 \\
0
\end{array}\right) \\
& \Rightarrow-6-9+b=0 \Rightarrow b=15 \\
& \text { and } 6(10-a)+9(a-6)-2(b)=0 \\
& \Rightarrow 60-6 a+9 a-54-30=0 \\
& \Rightarrow 3 a=24 \Rightarrow a=8
\end{aligned}
$$
Hence, $a=8, b=15$.

</details>

---

### Q129. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `1`

<p>The number of values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>, for which the system of equations :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mn>8</mn><mi>y</mi><mo>=</mo><mn>4</mn><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>x</mi><mo>+</mo><mfenced><mrow><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mi>y</mi><mo>=</mo><mn>3</mn><mi>k</mi><mo>-</mo><mn>1</mn></math></p>has no solution, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** Infinite
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mi>y</mi><mo>=</mo><msub><mi>c</mi><mn>1</mn></msub><mi>and</mi><mi>a</mi><mn>2</mn><mi>x</mi><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mi>y</mi><mo>=</mo><msub><mi>c</mi><mn>2</mn></msub></math> to have no solution,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><msub><mi>b</mi><mn>1</mn></msub><msub><mi>b</mi><mn>2</mn></msub></mfrac><mo>&#8800;</mo><mfrac><msub><mi>c</mi><mn>1</mn></msub><msub><mi>c</mi><mn>2</mn></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow><mi>k</mi></mfrac><mo>=</mo><mfrac><mn>8</mn><mrow><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8800;</mo><mfrac><mrow><mn>4</mn><mi>k</mi></mrow><mrow><mn>3</mn><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>8</mn><mi>k</mi><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>k</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>3</mn></math></p><p>but, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>1</mn><mo>,</mo><mfrac><mn>8</mn><mrow><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mi>k</mi></mrow><mrow><mn>3</mn><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>k</mi><mo>=</mo><mn>3</mn></math></p><p>Hence, only one value</p>

</details>

---

### Q130. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Statement 1: If the system of equations $x+k y+$ $3 z=0,3 x+k y-2 z=0,2 x+3 y-4 z=0$ has a nontrivial solution, then the value of $k$ is $\frac{31}{2}$.
Statement 2: A system of three homogeneous equations in three variables has a non trivial solution if the determinant of the coefficient matrix is zero.

**Options:**

- **(A)** Statement 1 is false, Statement 2 is true.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation for Statement 1.
- **(C)** Statement 1 is true, Statement 2 is true,, Statement 2 is not a correct explanation for Statement 1.
- **(D)** Statement 1 is true, Statement 2 is false.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement 1 is false, Statement 2 is true.**

**Detailed Solution:**

Given system of equations is
$$
\begin{aligned}
& x+k y+3 z=0 \\
& 3 x+k y-2 z=0 \\
& 2 x+3 y-4 z=0
\end{aligned}
$$
Since, system has non-trivial solution
$$
\begin{aligned}
& \therefore\left|\begin{array}{ccc}
1 & k & 3 \\
3 & k & -2 \\
2 & 3 & -4
\end{array}\right|=0 \\
\Rightarrow & 1(-4 k+6)-k(-12+4)+3(9-2 k)=0 \\
\Rightarrow & 4 k+33-6 k=0 \Rightarrow k=\frac{33}{2}
\end{aligned}
$$
Hence, statement - 1 is false.
Statement- 2 is the property.
It is a true statement.

</details>

---

### Q131. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If the system of equations
$$
\begin{aligned}
& x+y+z=6 \\
& x+2 y+3 z=10 \\
& x+2 y+\lambda z=0
\end{aligned}
$$
has a unique solution, then $\lambda$ is not equal to

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

Given system of equations is
$$
\begin{aligned}
& x+y+z=6 \\
& x+2 y+3 z=10 \\
& x+2 y+\lambda z=0
\end{aligned}
$$
It has unique solution.
$$
\begin{aligned}
& \therefore\left|\begin{array}{lll}
1 & 1 & 1 \\
1 & 2 & 3 \\
1 & 2 & \lambda
\end{array}\right| \neq 0 \\
& \Rightarrow \quad 1(2 \lambda-6)-1(\lambda-3)+1(2-2) \neq 0 \\
& \Rightarrow \quad 2 \lambda-6-\lambda+3 \neq 0 \Rightarrow \lambda-3 \neq 0 \Rightarrow \lambda \neq 3
\end{aligned}
$$

</details>

---

### Q132. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `2`

The number of values of $\mathrm{k}$ for which the linear equations $4 x+k y+2 z=0 ; k x+4 y+z=0 ; 2 x+2 y+z=0$ possess a non-zero solution is

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** zero
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

$\left|\begin{array}{lll}4 & k & 2 \\ k & 4 & 1 \\ 2 & 2 & 1\end{array}\right|=0 \Rightarrow k^2-6 k+8=0 \Rightarrow k=4,2$

</details>

---

### Q133. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `1`

Consider the system of linear equations:
$$
\begin{aligned}
& x_1+2 x_2+x_3=3 \\
& 2 x_1+3 x_2+x_3=3 \\
& 3 x_1+5 x_2+2 x_3=1
\end{aligned}
$$
The system has

**Options:**

- **(A)** exactly 3 solutions
- **(B)** a unique solution
- **(C)** no solution
- **(D)** infinite number of solutions

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) no solution**

**Detailed Solution:**

$$
\begin{aligned}
& D=\left|\begin{array}{lll}
1 & 2 & 1 \\
2 & 3 & 1 \\
3 & 5 & 2
\end{array}\right|=0 \\
& D_1=\left|\begin{array}{lll}
3 & 2 & 1 \\
3 & 3 & 1 \\
1 & 5 & 2
\end{array}\right| \neq 0
\end{aligned}
$$
$\Rightarrow$ Given system, does not have any solution.
$\Rightarrow$ No solution.

</details>

---

### Q134. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

Let $A$ and $B$ denote the statements
A: $\cos \alpha+\cos \beta+\cos \gamma=0$
B: $\sin \alpha+\sin \beta+\sin \gamma=0$
If $\cos (\beta-\gamma)+\cos (\gamma-\alpha)+\cos (\alpha-\beta)=-\frac{3}{2}$, then

**Options:**

- **(A)** $A$ is true and $B$ is false
- **(B)** $A$ is false and $B$ is true
- **(C)** both $A$ and $B$ are true
- **(D)** both $A$ and $B$ are false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) both $A$ and $B$ are true**

**Detailed Solution:**

$$
\begin{aligned}
& \cos (\beta-\gamma)+\cos (\gamma-\alpha)+\cos (\alpha-\beta)=-\frac{3}{2} \\
& \Rightarrow 2[\cos (\beta-\gamma)+\cos (\gamma-\alpha)+\cos (\alpha-\beta)]+3=0 \\
& \Rightarrow 2[\cos (\beta-\gamma)+\cos (\gamma-\alpha)+\cos (\alpha-\beta)]+\sin ^2 \alpha+\cos ^2 \alpha+\sin ^2 \beta+\cos ^2 \beta+\sin ^2 \gamma+\cos ^2 \gamma=0 \\
& \Rightarrow(\sin \alpha+\sin \beta+\sin \gamma)^2+(\cos \alpha+\cos \beta+\cos \gamma)^2=0
\end{aligned}
$$

</details>

---

### Q135. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `1`

Let $a, b, c$ be any real numbers. Suppose that there are real numbers $x, y, z$ not all zero such that $x=$ $c y+b z, y=a z+c x$ and $z=b x+a y$. Then $a^2+b^2+c^2+2 a b c$ is equal to

**Options:**

- **(A)** 2
- **(B)** $-1$
- **(C)** 0
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

The system of equations $x-c y-b z=0, c x-y+a z=0$ and $b x+a y-z=0$ have non-trivial solution if $\left|\begin{array}{ccc}1 & -c & -b \\ c & -1 & a \\ b & a & -1\end{array}\right|=0 \Rightarrow 1\left(1-a^2\right)+c(-c-a b)-b(c a+b)=0$ $\Rightarrow a^2+b^2+c^2+2 a b c=1$.

</details>

---

### Q136. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

The system of equations
$$
\begin{aligned}
& \alpha x+y+z=\alpha-1 \\
& x+\alpha y+z=\alpha-1 \\
& x+y+\alpha z=\alpha-1
\end{aligned}
$$
has no solution, if $\alpha$ is

**Options:**

- **(A)** $-2$
- **(B)** either $-2$ or 1
- **(C)** not -2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-2$**

**Detailed Solution:**

$$
\begin{aligned}
& \alpha x+y+z=\alpha-1 \\
& x+\alpha y+z=\alpha-1 \\
& x+y+z \alpha=\alpha-1 \\
& \Delta=\left|\begin{array}{ccc}
\alpha & 1 & 1 \\
1 & \alpha & 1 \\
1 & 1 & \alpha
\end{array}\right| \\
& =\alpha\left(\alpha^2-1\right)-1(\alpha-1)+1(1-\alpha) \\
& =\alpha(\alpha-1)(\alpha+1)-1(\alpha-1)-1(\alpha-1) \\
& \Rightarrow(\alpha-1)\left[\alpha^2+\alpha-1-1\right]=0 \\
& \Rightarrow(\alpha-1)\left[\alpha^2+\alpha-2\right]=0 \\
& {\left[\alpha^2+2 \alpha-\alpha-2\right]=0} \\
& (\alpha-1)[\alpha(\alpha+2)-1(\alpha+2)]=0 \\
& (\alpha-1)=0, \alpha+2=0 \Rightarrow \alpha=-2,1 ; \text { but } \alpha \neq 1
\end{aligned}
$$

</details>

---

### Q137. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

If the system of linear equations
$x+2 a y+a z=0$     $x+3 b y+b z=0$ 
 $x+4 c y+c z=0$
 has a non-zero solution, then $\mathrm{a}, \mathrm{b}, \mathrm{c}$

**Options:**

- **(A)** satisfy $a+2 b+3 c=0$
- **(B)** are in A.P.
- **(C)** are in G.P.
- **(D)** are in H.P.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) are in H.P.**

**Detailed Solution:**

$\left|\begin{array}{lll}1 & 2 \mathrm{a} & \mathrm{a} \\ 1 & 3 \mathrm{~b} & \mathrm{~b} \\ 1 & 4 \mathrm{c} & \mathrm{c}\end{array}\right|=0 \quad \mathrm{C}_2 \rightarrow \mathrm{C}_2-2 \mathrm{C}_3$
$\left|\begin{array}{ccc}1 & 0 & \mathrm{a} \\ 1 & \mathrm{~b} & \mathrm{~b} \\ 1 & 2 \mathrm{c} & \mathrm{c}\end{array}\right|=0 \quad \mathrm{R}_3 \rightarrow \mathrm{R}_3-\mathrm{R}_2, \mathrm{R}_2 \rightarrow \mathrm{R}_2-\mathrm{R}_1$
$\left|\begin{array}{ccc}1 & 0 & a \\ 0 & b & b-a \\ 0 & 2 c-b & c-b\end{array}\right|=0$
$b(c-b)-(b-a)(2 c-b)=0$
On simplification,
$$
\frac{2}{\mathrm{~b}}=\frac{1}{\mathrm{a}}+\frac{1}{\mathrm{c}}
$$
$\therefore \mathrm{a}, \mathrm{b}, \mathrm{c}$ are in Harmonic Progression.

</details>

---

