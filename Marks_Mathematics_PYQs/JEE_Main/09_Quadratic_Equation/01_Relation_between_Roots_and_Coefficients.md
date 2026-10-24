# JEE Main Mathematics - Quadratic Equation

## Topic 1: Relation between Roots and Coefficients

**Total Questions:** 135

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider the quadratic equation $(n^2 - 2n + 2)x^2 - 3x + (n^2 - 2n + 2)^2 = 0$, $n \in \mathbb{R}$. Let $\alpha$ be the minimum value of the product of its roots and $\beta$ be the maximum value of the sum of its roots. Then the sum of the first six terms of the G.P., whose first term is $\alpha$ and the common ratio is $\dfrac{\alpha}{\beta}$, is :

**Options:**

- **(A)** $\dfrac{61}{37}$
- **(B)** $\dfrac{121}{81}$
- **(C)** $\dfrac{364}{243}$
- **(D)** $\dfrac{1093}{729}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{364}{243}$**

**Detailed Solution:**

The given quadratic equation is $(n^2 - 2n + 2)x^2 - 3x + (n^2 - 2n + 2)^2 = 0$.

Let $k = n^2 - 2n + 2 = (n-1)^2 + 1$. Since $(n-1)^2 \ge 0$ for all $n \in \mathbb{R}$, the minimum value of $k$ is $1$ at $n=1$.

The product of the roots is given by $P = \dfrac{(n^2 - 2n + 2)^2}{n^2 - 2n + 2} = n^2 - 2n + 2 = k$.

The minimum value of the product of the roots is $\alpha = \min(k) = 1$.

The sum of the roots is given by $S = \dfrac{3}{n^2 - 2n + 2} = \dfrac{3}{k}$.

The maximum value of the sum of the roots occurs when $k$ is minimum. Thus, $\beta = \max\left(\dfrac{3}{k}\right) = \dfrac{3}{1} = 3$.

We are given a Geometric Progression (G.P.) whose first term is $a = \alpha = 1$ and common ratio is $r = \dfrac{\alpha}{\beta} = \dfrac{1}{3}$.

The sum of the first six terms of this G.P. is:

$S_6 = a \dfrac{1 - r^6}{1 - r} = 1 \cdot \dfrac{1 - \left(\dfrac{1}{3}\right)^6}{1 - \dfrac{1}{3}}$

$S_6 = \dfrac{1 - \dfrac{1}{729}}{\dfrac{2}{3}} = \dfrac{\dfrac{728}{729}}{\dfrac{2}{3}}$

$S_6 = \dfrac{728}{729} \times \dfrac{3}{2} = \dfrac{364}{243}$

Answer: $\dfrac{364}{243}$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let one root of the quadratic equation in $x$: $(k^2 - 15k + 27)x^2 + 9(k-1)x + 18 = 0$ be twice the other. Then the length of the latus rectum of the parabola $y^2 = 6kx$ is equal to:

**Options:**

- **(A)** $4$
- **(B)** $6$
- **(C)** $8$
- **(D)** $12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $12$**

**Detailed Solution:**

Let the roots of the given quadratic equation be $\alpha$ and $2\alpha$.

Sum of the roots:
$\alpha + 2\alpha = \dfrac{-9(k-1)}{k^2 - 15k + 27}$
$3\alpha = \dfrac{-9(k-1)}{k^2 - 15k + 27} \Rightarrow \alpha = \dfrac{-3(k-1)}{k^2 - 15k + 27}$

Product of the roots:
$\alpha \cdot 2\alpha = \dfrac{18}{k^2 - 15k + 27}$
$2\alpha^2 = \dfrac{18}{k^2 - 15k + 27} \Rightarrow \alpha^2 = \dfrac{9}{k^2 - 15k + 27}$

Substituting the value of $\alpha$ from the sum into the product equation:
$\left( \dfrac{-3(k-1)}{k^2 - 15k + 27} \right)^2 = \dfrac{9}{k^2 - 15k + 27}$

$\dfrac{9(k-1)^2}{(k^2 - 15k + 27)^2} = \dfrac{9}{k^2 - 15k + 27}$

Since $k^2 - 15k + 27 \neq 0$, we can simplify to:
$(k-1)^2 = k^2 - 15k + 27$

$k^2 - 2k + 1 = k^2 - 15k + 27$

$13k = 26 \Rightarrow k = 2$

The equation of the parabola is $y^2 = 6kx$. Substituting $k = 2$, we get:
$y^2 = 12x$

The length of the latus rectum of a parabola $y^2 = 4ax$ is $4a$, which is the coefficient of $x$.

Therefore, the length of the latus rectum is $12$.

Answer: $12$

</details>

---

### Q3. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha, \beta$ be the roots of the equation $x^2 - x + p = 0$ and $\gamma, \delta$ be the roots the equation $x^2 - 4x + q = 0$; $p, q \in \mathbf{Z}$. If $\alpha, \beta, \gamma, \delta$ are in G.P., then $|p + q|$ equals :

**Options:**

- **(A)** $16$
- **(B)** $32$
- **(C)** $34$
- **(D)** $38$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $34$**

**Detailed Solution:**

Let $\alpha = a, \beta = ar, \gamma = ar^2, \delta = ar^3$ be the terms of the G.P.

From the given quadratic equations, the sum of the roots are:

$\alpha + \beta = 1 \Rightarrow a(1 + r) = 1$

$\gamma + \delta = 4 \Rightarrow ar^2(1 + r) = 4$

Dividing the second equation by the first equation:

$\dfrac{ar^2(1 + r)}{a(1 + r)} = \dfrac{4}{1}$

$r^2 = 4 \Rightarrow r = 2$ or $r = -2$

If $r = 2$, then $a(1 + 2) = 1 \Rightarrow a = \dfrac{1}{3}$.

The product of the roots of the first equation is $p = \alpha \beta = a^2 r = \left(\dfrac{1}{3}\right)^2 \times 2 = \dfrac{2}{9}$. Since $p \in \mathbf{Z}$, $r = 2$ is rejected.

If $r = -2$, then $a(1 - 2) = 1 \Rightarrow a = -1$.

The product of the roots of the first equation is $p = \alpha \beta = a^2 r = (-1)^2 \times (-2) = -2$.

The product of the roots of the second equation is $q = \gamma \delta = (ar^2)(ar^3) = a^2 r^5 = (-1)^2 \times (-2)^5 = -32$.

Both $p$ and $q$ are integers, which satisfies the given condition.

Therefore, $|p + q| = |-2 - 32| = |-34| = 34$.

Answer: $34$

</details>

---

### Q4. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\tan A, \tan B$, where $A, B \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$, be the roots of the quadratic equation $x^2 - 2x - 5 = 0$. Then $20\sin^2\left(\dfrac{A+B}{2}\right)$ is equal to:

**Options:**

- **(A)** $10 + \sqrt{10}$
- **(B)** $10 - 2\sqrt{10}$
- **(C)** $10 - 3\sqrt{10}$
- **(D)** $10 - \sqrt{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $10 - 3\sqrt{10}$**

**Detailed Solution:**

Given that $\tan A$ and $\tan B$ are the roots of the quadratic equation $x^2 - 2x - 5 = 0$.

Sum of the roots: $\tan A + \tan B = 2$

Product of the roots: $\tan A \tan B = -5$

Using the tangent addition formula:

$\tan(A+B) = \dfrac{\tan A + \tan B}{1 - \tan A \tan B} = \dfrac{2}{1 - (-5)} = \dfrac{2}{6} = \dfrac{1}{3}$

Since $A, B \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$ and their product $\tan A \tan B = -5 < 0$, one angle is positive and the other is negative. This implies $A+B \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$.

Since $\tan(A+B) = \dfrac{1}{3} > 0$, the angle $A+B$ must lie in the first quadrant, i.e., $A+B \in \left(0, \dfrac{\pi}{2}\right)$. Thus, $\cos(A+B)$ is positive.

$\cos(A+B) = \dfrac{1}{\sqrt{1 + \tan^2(A+B)}} = \dfrac{1}{\sqrt{1 + \left(\dfrac{1}{3}\right)^2}} = \dfrac{3}{\sqrt{10}}$

We need to find the value of $20\sin^2\left(\dfrac{A+B}{2}\right)$. Using the half-angle identity $\sin^2\theta = \dfrac{1 - \cos(2\theta)}{2}$:

$20\sin^2\left(\dfrac{A+B}{2}\right) = 20 \left( \dfrac{1 - \cos(A+B)}{2} \right) = 10(1 - \cos(A+B))$

Substituting the value of $\cos(A+B)$:

$10\left(1 - \dfrac{3}{\sqrt{10}}\right) = 10 - \dfrac{30}{\sqrt{10}} = 10 - 3\sqrt{10}$

Answer: $10 - 3\sqrt{10}$

</details>

---

### Q5. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $a, b \in \mathbb{C}$. Let $\alpha, \beta$ be the roots of the equation $x^2 + ax + b = 0$. If $\beta - \alpha = \sqrt{11}$ and $\beta^2 - \alpha^2 = 3i\sqrt{11}$, then $(\beta^3 - \alpha^3)^2$ is equal to:

**Options:**

- **(A)** $160$
- **(B)** $176$
- **(C)** $194$
- **(D)** $187$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $176$**

**Detailed Solution:**

Given $\beta - \alpha = \sqrt{11}$ and $\beta^2 - \alpha^2 = 3i\sqrt{11}$

$\beta + \alpha = \dfrac{\beta^2 - \alpha^2}{\beta - \alpha} = \dfrac{3i\sqrt{11}}{\sqrt{11}} = 3i$

Using the identity $(\beta - \alpha)^2 = (\beta + \alpha)^2 - 4\alpha\beta$

$(\sqrt{11})^2 = (3i)^2 - 4\alpha\beta$

$11 = -9 - 4\alpha\beta$

$4\alpha\beta = -20 \Rightarrow \alpha\beta = -5$

Now, $\beta^3 - \alpha^3 = (\beta - \alpha)(\beta^2 + \alpha\beta + \alpha^2)$

$\beta^3 - \alpha^3 = (\beta - \alpha)((\beta + \alpha)^2 - \alpha\beta)$

$\beta^3 - \alpha^3 = \sqrt{11}((3i)^2 - (-5))$

$\beta^3 - \alpha^3 = \sqrt{11}(-9 + 5) = -4\sqrt{11}$

Squaring both sides, we get:

$(\beta^3 - \alpha^3)^2 = (-4\sqrt{11})^2 = 16 \times 11 = 176$

Answer: $176$

</details>

---

### Q6. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\alpha=1$ and $\beta=1+i\sqrt{2}$, where $i=\sqrt{-1}$ are two roots of the equation $x^3+ax^2+bx+c=0$, $a,b,c \in \mathbb{R}$, then $\int_{-1}^{1}(x^3+ax^2+bx+c)dx$ is equal to:

**Options:**

- **(A)** $-2$
- **(B)** $-4$
- **(C)** $-8$
- **(D)** $-10$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-8$**

**Detailed Solution:**

Since $a, b, c \in \mathbb{R}$, the complex roots of the equation $x^3+ax^2+bx+c=0$ must occur in conjugate pairs.

Given roots are $\alpha = 1$ and $\beta = 1+i\sqrt{2}$.

The third root must be $\gamma = 1-i\sqrt{2}$.

The polynomial is given by:

$x^3+ax^2+bx+c = (x-1)(x-(1+i\sqrt{2}))(x-(1-i\sqrt{2}))$

$= (x-1)((x-1)^2 - (i\sqrt{2})^2)$

$= (x-1)(x^2 - 2x + 1 + 2)$

$= (x-1)(x^2 - 2x + 3)$

$= x^3 - 3x^2 + 5x - 3$

We need to evaluate the integral:

$I = \int_{-1}^{1} (x^3 - 3x^2 + 5x - 3) dx$

Using the property of definite integrals $\int_{-a}^{a} f(x) dx = 0$ for odd functions and $2\int_{0}^{a} f(x) dx$ for even functions:

$I = \int_{-1}^{1} x^3 dx - 3\int_{-1}^{1} x^2 dx + 5\int_{-1}^{1} x dx - 3\int_{-1}^{1} 1 dx$

$I = 0 - 3(2)\int_{0}^{1} x^2 dx + 0 - 3(2)\int_{0}^{1} 1 dx$

$I = -6 \left[ \dfrac{x^3}{3} \right]_{0}^{1} - 6 \left[ x \right]_{0}^{1}$

$I = -6 \left( \dfrac{1}{3} \right) - 6(1)$

$I = -2 - 6 = -8$

Answer: $-8$

</details>

---

### Q7. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha, \beta$ be the roots of the equation $x^2 - 3x + r = 0$, and $\dfrac{\alpha}{2}, 2\beta$ be the roots of the equation $x^2 + 3x + r = 0$. If the roots of the equation $x^2 + 6x = m$ are $2\alpha + \beta + 2r$ and $\alpha - 2\beta - \dfrac{r}{2}$, then $m$ is equal to:

**Options:**

- **(A)** $-135$
- **(B)** $-567$
- **(C)** $135$
- **(D)** $567$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $567$**

**Detailed Solution:**

From the first equation $x^2 - 3x + r = 0$, the sum and product of the roots are:

$\alpha + \beta = 3$

$\alpha \beta = r$

From the second equation $x^2 + 3x + r = 0$, the sum and product of the roots are:

$\dfrac{\alpha}{2} + 2\beta = -3$

$\left(\dfrac{\alpha}{2}\right)(2\beta) = r \Rightarrow \alpha \beta = r$

We have a system of linear equations in terms of $\alpha$ and $\beta$:

$\alpha + \beta = 3$

$\alpha + 4\beta = -6$

Subtracting the first equation from the second gives:

$3\beta = -9 \Rightarrow \beta = -3$

Substituting $\beta = -3$ into $\alpha + \beta = 3$ gives:

$\alpha = 6$

Now, we can find $r$:

$r = \alpha \beta = 6 \times (-3) = -18$

The roots of the third equation $x^2 + 6x - m = 0$ are given as $2\alpha + \beta + 2r$ and $\alpha - 2\beta - \dfrac{r}{2}$. Let us calculate their values:

$R_1 = 2(6) + (-3) + 2(-18) = 12 - 3 - 36 = -27$

$R_2 = 6 - 2(-3) - \dfrac{-18}{2} = 6 + 6 + 9 = 21$

The product of the roots of the equation $x^2 + 6x - m = 0$ is $-m$. Therefore:

$-m = R_1 R_2 = (-27)(21)$

$-m = -567 \Rightarrow m = 567$

Answer: $567$

</details>

---

### Q8. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\alpha, \beta$, where $\alpha<\beta$, are the roots of the equation $\lambda x^{2}-(\lambda+3) x+3=0$ such that $\frac{1}{\alpha}-\frac{1}{\beta}=\frac{1}{3}$, then the sum of all possible values of $\lambda$ is

**Options:**

- **(A)** 8
- **(B)** 6
- **(C)** 2
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 6**

**Detailed Solution:**

$\alpha + \beta = \frac{\lambda+3}{\lambda}$, $\alpha\beta = \frac{3}{\lambda}$.
$\frac{1}{\alpha} - \frac{1}{\beta} = \frac{\beta - \alpha}{\alpha\beta} = \frac{1}{3}$, so $\beta - \alpha = \frac{\alpha\beta}{3} = \frac{1}{\lambda}$.
$(\beta - \alpha)^2 = (\alpha+\beta)^2 - 4\alpha\beta$:
$\frac{1}{\lambda^2} = \frac{(\lambda+3)^2}{\lambda^2} - \frac{12}{\lambda}$
$1 = (\lambda+3)^2 - 12\lambda = \lambda^2 - 6\lambda + 9$
$\lambda^2 - 6\lambda + 8 = 0 \Rightarrow \lambda = 2$ or $\lambda = 4$.
Both values satisfy $\alpha < \beta$ (verified). Sum $= 2 + 4 = 6$.

</details>

---

### Q9. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha, \beta$ be the roots of the quadratic equation $12 x^{2}-20 x+3 \lambda=0, \lambda \in \mathbf{Z}$. If $\frac{1}{2} \leqslant|\beta-\alpha| \leqslant \frac{3}{2}$, then the sum of all possible values of $\lambda$ is :

**Options:**

- **(A)** 1
- **(B)** 6
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

For $12x^2-20x+3\lambda=0$: $\alpha+\beta=\frac{5}{3}$, $\alpha\beta=\frac{\lambda}{4}$.
$|\beta-\alpha|=\frac{\sqrt{25-9\lambda}}{3}$
Given $\frac{1}{2}\leq\frac{\sqrt{25-9\lambda}}{3}\leq\frac{3}{2}$
$\frac{9}{4}\leq 25-9\lambda\leq\frac{81}{4}$
From left: $\lambda\leq\frac{91}{36}\approx 2.53$
From right: $\lambda\geq\frac{19}{36}\approx 0.53$
Since $\lambda\in\mathbb{Z}$: $\lambda\in\{1,2\}$. Sum $=3$.

</details>

---

### Q10. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all the roots of the equation $(x-1)^{2}-5|x-1|+6=0$, is :

**Options:**

- **(A)** 1
- **(B)** 5
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

Let $t = |x-1|$ where $t \geq 0$.
Equation becomes $t^2 - 5t + 6 = 0$.
$(t-2)(t-3) = 0$ gives $t = 2$ or $t = 3$.
For $|x-1| = 2$: $x = 3$ or $x = -1$.
For $|x-1| = 3$: $x = 4$ or $x = -2$.
Sum of roots $= 3 + (-1) + 4 + (-2) = 4$.

</details>

---

### Q11. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the squares of the roots of $|\mathrm{x}+2|^2+|\mathrm{x}-2|-2=0$ and the squares of the roots of $x^2-2|x-3|-5=0$, is

**Options:**

- **(A)** 26
- **(B)** 36
- **(C)** 30
- **(D)** 24

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 36**

**Detailed Solution:**

$\begin{aligned} & |\mathrm{x}-2|^2+2|\mathrm{x}-2|-|\mathrm{x}-2|-2=0 \\ & \Rightarrow(|\mathrm{x}-2|+2)(|\mathrm{x}-2|-1)=0 \\ & \Rightarrow|\mathrm{x}-2|=1 \\ & \Rightarrow \mathrm{x}=2 \pm 1=3,1 \\ & \Rightarrow \text { sum of square of roots }=9+1=10 \\ & \mathrm{x}^2-2|\mathrm{x}-3|-5=0 \\ & \text { Case-I } \mathrm{x}-3 \geq 0 \\ & \Rightarrow \mathrm{x}^2-2 \mathrm{x}+1=0 \\ & \Rightarrow(\mathrm{x}-1)^2=0 \\ & \Rightarrow \mathrm{x}=1\end{aligned}$
But $x \geq 3$
$\Rightarrow \mathrm{x} \in \phi$
Case-II $\mathrm{x}-3 \lt 0$
$x^2+2 x-11=0, D \gt 0 \Rightarrow$ Real \& distinct roots
$f(x)=x^2+2 x-11$
$\mathrm{f}(3) \gt 0, \frac{-\mathrm{p}}{2 \mathrm{a}}=-1 \lt 3$
$\Rightarrow$ both roots $ \lt 3$, both roots acceptable
Sum of square of roots $=(\alpha+\beta)^2-2 \alpha \beta$
$\begin{aligned}
& =4+22=26 \\
& \Rightarrow \text { Final sum }=10+26=36
\end{aligned}$

</details>

---

### Q12. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of real roots of the equation $\mathrm{x}|\mathrm{x}-2|+3|\mathrm{x}-3|+1=0$ is :

**Options:**

- **(A)** 4
- **(B)** 2
- **(C)** 1
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

$\begin{aligned}
& \text { (I) } x \lt 2 \\
& -x^2+2 x-3 x+9+1=0 \\
& \Rightarrow x^2+x-10=0 \\
& \Rightarrow x=\frac{-1+\sqrt{41}}{2}, \frac{-1-\sqrt{41}}{2} \\
& \quad \times \quad \sqrt{ }
\end{aligned}$
$\begin{aligned}
& \text { (II) } 2 \leq x \lt 3 \\
& \Rightarrow x^2-2 x-3 x+9+1=0 \\
& \Rightarrow x^2-5 x+10=0 \\
& \text { D } \lt 0 \\
& \text { (III) } x \geq 3 \\
& x^2-2 x+3 x-9+2=0 \\
& \Rightarrow x^2+x-8=0 \\
& x=\frac{-1+\sqrt{32}}{2}, \frac{-1-\sqrt{32}}{2} \\
& \quad \times \quad \times
\end{aligned}$
1 real roots

</details>

---

### Q13. JEE Main 2025 (7 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

For $t \gt -1$, let $\alpha_t$ and $\beta_t$ be the roots of the equation
$\left((t+2)^{\frac{1}{7}}-1\right) x^2+\left((t+2)^{\frac{1}{6}}-1\right)$ $x+\left((t+2)^{\frac{1}{21}}-1\right)=0$
If $\lim _{t \rightarrow-1^{+}} \alpha_t=a$ and $\lim _{t \rightarrow-1^{+}} \beta_t=b$, then $72(a+b)^2$ is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **98**

**Detailed Solution:**

$\begin{aligned} & a+b=\lim _{t \rightarrow-1^{+}}(\alpha+\beta)=\lim _{t \rightarrow-1^{+}}-\frac{(t+2)^{\frac{1}{6}}-1}{(t+2)^{\frac{1}{7}}-1} \\ & \text { let } t+2=y \\ & a+b=\lim _{y \rightarrow 1^{+}} \frac{y^{1 / 6}-1}{y^{1 / 7}-1}=\frac{7}{6} \\ & 72(a+b)^2=72 \frac{49}{36}=98\end{aligned}$

</details>

---

### Q14. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the set of all values of $\mathrm{p} \in \mathbb{R}$, for which both the roots of the equation $x^2-(p+2) x+(2 p+9)=0$ are negative real numbers, be the interval $(\alpha, \beta]$. Then $\beta-2 \alpha$ is equal to

**Options:**

- **(A)** 0
- **(B)** 9
- **(C)** 5
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5**

**Detailed Solution:**

Using location of roots :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/IkKJ5KArOmUTtZfkibzvK4GT9ki9hZMHpshthFWfftA.original.fullsize.png"/>
(i) $\mathrm{D} \geq 0$
(ii) $\frac{-\mathrm{b}}{2 \mathrm{a}} \lt 0$
(iii) a. $\mathrm{f}(0) \gt 0$
$\begin{aligned}
& (p+2)^2-4(2 p+9) \geq 0 \\
& (p+4)(p-8) \geq 0 \quad p+2 \lt 0 \quad 2 p+9 \gt 0
\end{aligned}$
Intersection $p \in\left(-\frac{9}{2},-4\right]$
$\therefore \beta-2 \alpha=-4+9=5$

</details>

---

### Q15. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Consider the equation $\mathrm{x}^2+4 \mathrm{x}-\mathrm{n}=0$, where $\mathrm{n} \in[20,100]$ is a natural number. Then the number of all distinct values of $n$, for which the given equation has integral roots, is equal to

**Options:**

- **(A)** 7
- **(B)** 8
- **(C)** 6
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 6**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{x}^2+4 \mathrm{x}+4=\mathrm{n}+4 \\
& (\mathrm{x}+2)^2=\mathrm{n}+4 \\
& \mathrm{x}=-2 \pm \sqrt{\mathrm{n}+4} \\
& \because 20 \leq \mathrm{n} \leq 100 \\
& \sqrt{24} \leq \sqrt{\mathrm{n}+4} \leq \sqrt{104} \\
& \Rightarrow \sqrt{\mathrm{n}+4} \in\{5,6,7,8,9,10\}
\end{aligned}$
$\therefore ' 6$ ' integral values of ' $n$ ' are possible

</details>

---

### Q16. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha$ and $\beta$ be the roots of $x^2+\sqrt{3 x}-16=0$, and $\gamma$ and $\delta$ be the roots of $x^2+3 x-1=0$. If $P_n=\alpha^n+\beta^n$ and $Q_n=\gamma^n+\delta^n$, then $\frac{\mathrm{P}_{25}+\sqrt{3 \mathrm{P}_{24}}}{2 \mathrm{P}_{23}}+\frac{\mathrm{Q}_{25}-\mathrm{Q}_{23}}{\mathrm{Q}_{24}}$ is equal to

**Options:**

- **(A)** $3$
- **(B)** $4$
- **(C)** $5$
- **(D)** $7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5$**

**Detailed Solution:**

$\begin{aligned} & x^2+\sqrt{3} \mathrm{x}-16=0 \lt \beta \\ & \mathrm{P}_{\mathrm{n}}+\sqrt{3} \mathrm{P}_{\mathrm{n}-1}-16 \mathrm{P}_{\mathrm{n}-2}=0 \\ & \mathrm{P}_{25}+\sqrt{3} \mathrm{P}_{24}-16 \mathrm{P}_{23}=0 \\ & \therefore \frac{\mathrm{P}_{25}+\sqrt{3} \mathrm{P}_{24}}{2 \mathrm{P}_{23}}=8\end{aligned}$
Similarly
$x^2+3 x-1=0 \lt \sum_\delta^\gamma \quad Q_n=\gamma^n+\delta^n$
$\begin{aligned}
& \mathrm{Q}_{25}-\mathrm{Q}_{23}=\gamma^{25}+\delta^{25}-\gamma^{23}-\delta^{23} \\
&=\gamma^{23}\left(\gamma^2-1\right)+\delta^{23}\left(\delta^2-1\right) \\
&=\gamma^{23}(-3 \gamma)+\delta^{23}(-3 \gamma) \\
&=-3\left[\gamma^{24}+\delta^{24}\right] \\
&=-3 \mathrm{Q}_{24} \\
& \therefore \frac{\mathrm{Q}_{25}-\mathrm{Q}_{23}}{\mathrm{Q}_{24}}=-3
\end{aligned}$
$\frac{\mathrm{P}_{25}+\sqrt{3} \mathrm{P}_{24}}{2 \mathrm{P}_{23}}+\frac{\mathrm{Q}_{25}-\mathrm{Q}_{23}}{\mathrm{Q}_{24}}=8-3=5$

</details>

---

### Q17. JEE Main 2025 (2 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

If the set of all $\mathrm{a} \in \mathrm{R}-\{1\}$, for which the roots of the equation $(1-a) x^2+2(a-3) x+9=0$ are positive is $(-\infty,-\alpha] \cup[\beta, \gamma)$, then $2 \alpha+\beta+\gamma$ is equal to _______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

Both the roots are positive
$\begin{aligned}
& D \geq 0 \\
& 4(a-3)^2-4 \times 9(1-a) \geq 0 \\
& a^2-6 a+9-9+9 a \geq 0 \\
& a^2+3 a \geq 0 \\
& a(a+3) \geq 0
\end{aligned}$
$\mathrm{a} \in(-\infty,-3] \cup[0, \infty)$   ...(i)
$\begin{aligned} & -\frac{\mathrm{b}}{2 \mathrm{a}} \gt 0 \\ & \frac{2(\mathrm{a}-3)}{2(\mathrm{a}-1)} \gt 0\end{aligned}$
$a \in(-\infty, 1) \cup(3, \infty)$    ...(ii)
$f(0)=9 \gt 0$
Equation (i) $\cap$ (ii)
$\begin{aligned}
& a \in(-\infty,-3] \cup[0,1) \\
& 2 \alpha+\beta+\gamma-6+0+1=7
\end{aligned}$

</details>

---

### Q18. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $P_n=\alpha^n+\beta^n, n \in \mathbf{N}$. If $P_{10}=123, P_9=76$, $P_8=47$ and $P_1=1$, then the quadratic equation having roots $\frac{1}{\alpha}$ and $\frac{1}{\beta}$ is :

**Options:**

- **(A)** $x^2-x+1=0$
- **(B)** $x^2+x-1=0$
- **(C)** $x^2-x-1=0$
- **(D)** $x^2+x+1=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2+x-1=0$**

**Detailed Solution:**

$\begin{aligned} & \alpha^{10}+\beta^{10}=123 \\ & \alpha+\beta=1 \\ & \alpha^9+\beta^9=76 \\ & \alpha^8+\beta^8=47 \\ & P_{10}=P_9+P_8 \\ & x^2=x+1 \Rightarrow x^2-x-1=0 \\ & \alpha+\beta=1, \alpha \beta=-1 \\ & \frac{1}{\alpha}+\frac{1}{\beta}=\frac{\alpha+\beta}{\alpha \beta}=\frac{1}{-1}=-1, \frac{1}{\alpha \beta}=-1\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the set of all $\mathrm{a} \in \mathbf{R}$, for which the equation $2 x^2+(a-5) x+15=3 \mathrm{a}$ has no real root, is the interval $(\alpha, \beta)$, and $X=\{x \in Z: \alpha \lt x \lt \beta\}$, then $\sum_{x \in X} x^2$ is equal to :

**Options:**

- **(A)** 2109
- **(B)** 2129
- **(C)** 2119
- **(D)** 2139

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2139**

**Detailed Solution:**

$\begin{aligned} & (a-5)^2-8(15-3 a) < 0 \\ & a^2+14 a+25-120 < 0 \\ & a^2+14 a-95 < 0 \\ & (a+19)(a-5) < 0 \\ & a \in(-19,5) \\ & \therefore-19 < x < 5 \\ & \therefore \sum_{x \in X} x^2=\left(1^2+2^2+\ldots .+4^2\right)+\left(1^2+2^2+\ldots+18^2\right) \\ & =\frac{4 \times 5 \times 9}{6}+\frac{18 \times 19 \times 37}{6} \\ & =30+2109 \\ & =2139\end{aligned}$

</details>

---

### Q20. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum, of the squares of all the roots of the equation $x^2+|2 x-3|-4=0$, is

**Options:**

- **(A)** $3(3-\sqrt{2})$
- **(B)** $6(3-\sqrt{2})$
- **(C)** $6(2-\sqrt{2})$
- **(D)** $3(2-\sqrt{2})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6(2-\sqrt{2})$**

**Detailed Solution:**

$\begin{aligned} & \text { For } x \geq \frac{3}{2} \\ & x^2+2 x-3-4=0 \\ & x^2+2 x-7=0 \\ & x=\frac{-2 \pm \sqrt{4+28}}{2}=-1 \pm 2 \sqrt{2}\end{aligned}$
Only $2 \sqrt{2}-1$ is acceptable root
For $x < \frac{3}{2}$
$x^2-2 x+3-4=0$
$\begin{aligned}
& x^2-2 x-1=0 \\
& x=\frac{2 \pm \sqrt{4+4}}{2}=1 \pm \sqrt{2}
\end{aligned}$
Only $1-\sqrt{2}$ is acceptable
Sum of the square $=(1-\sqrt{2})^2+(2 \sqrt{2}-1)^2$
$=6(2-\sqrt{2})$

</details>

---

### Q21. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha_\theta$ and $\beta_\theta$ be the distinct roots of $2 x^2+(\cos \theta) x-1=0, \theta \in(0,2 \pi)$. If m and M are the minimum and the maximum values of $\alpha_\theta^4+\beta_\theta^4$, then $16(M+m)$ equals :

**Options:**

- **(A)** 24
- **(B)** 25
- **(C)** 17
- **(D)** 27

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 25**

**Detailed Solution:**

$\begin{aligned} & 2 x^2+(\cos \theta) x-1=0 \\ & \alpha_\theta+\beta_\theta=\frac{-\cos \theta}{2} \\ & \alpha_\theta \cdot \beta_\theta=\frac{-1}{2} \\ & \alpha_\theta^2+\beta_\theta^2=\left(\alpha_\theta+\beta_\theta\right)^2-2 \alpha_\theta \beta_\theta \frac{\cos ^2 \theta}{4}+1\end{aligned}$
$\begin{aligned}
& \alpha_\theta^4+\beta_\theta^4=\left(a_\theta^2+\beta_\theta^2\right)^2-2 \alpha_\theta^2 \beta_\theta^2=\left(\frac{\cos ^2 \theta}{4}+1\right)^2-\frac{2}{4} \\
& =\left(\frac{\cos ^2 \theta}{4}+1\right)^2-\frac{1}{2}
\end{aligned}$

Maximum when $\cos \theta=1$
$\begin{aligned}
& M=\left(\frac{1}{4}+1\right)^2-\frac{1}{2} \\
& M=\frac{17}{16}
\end{aligned}$

Minimum when $\cos \theta=0$
$\begin{aligned}
& m=1-\frac{1}{2}=\frac{1}{2} \\
& 16(M+m)=16\left(\frac{17}{16}+\frac{1}{2}\right)=25
\end{aligned}$

</details>

---

### Q22. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha, \beta ; \alpha>\beta$, be the roots of the equation $x^2-\sqrt{2} x-\sqrt{3}=0$. Let $\mathrm{P}_n=\alpha^n-\beta^n, n \in \mathrm{N}$. Then $(11 \sqrt{3}-10 \sqrt{2}) \mathrm{P}_{10}+(11 \sqrt{2}+10) \mathrm{P}_{11}-11 \mathrm{P}_{12}$ is equal to

**Options:**

- **(A)** $10 \sqrt{3} \mathrm{P}_9$
- **(B)** $11 \sqrt{3} P_9$
- **(C)** $10 \sqrt{2} \mathrm{P}_9$
- **(D)** $11 \sqrt{2} \mathrm{P}_9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $10 \sqrt{3} \mathrm{P}_9$**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{x}^2-\sqrt{2 \mathrm{x}}-\sqrt{3}=0\left\langle_\beta^\alpha\right. \\
& \alpha^{\mathrm{n}+2}-\sqrt{2} \alpha^{\mathrm{n}+1}-\sqrt{3} \alpha^{\mathrm{n}}=0 \\
& \text { and } \beta^{\mathrm{n}+2}-\sqrt{2} \beta^{\mathrm{n}+1}-\sqrt{3} \beta^{\mathrm{n}}=0
\end{aligned}$
Subtracting
$\begin{aligned}
& \left(\alpha^{\mathrm{n}+2}-\beta^{\mathrm{n}+2}\right)-\sqrt{2}\left(\alpha^{\mathrm{n}+1}-\beta^{\mathrm{n}+1}\right)-\sqrt{3}\left(\alpha^{\mathrm{n}}-\beta^{\mathrm{n}}\right)=0 \\
& \Rightarrow \mathrm{P}_{\mathrm{n}+2}-\sqrt{2} \mathrm{P}_{\mathrm{n}+1}-\sqrt{3} \mathrm{P}_{\mathrm{n}}=0
\end{aligned}$
$\begin{aligned} & \text { Put } \mathrm{n}=10 \\ & \mathrm{P}_{12}-\sqrt{2} \mathrm{P}_{11}-\sqrt{3} \mathrm{P}_{10}=0 \\ & \mathrm{n}=9 \\ & \mathrm{P}_{11}-\sqrt{2} \mathrm{P}_{10}-\sqrt{3} \mathrm{P}_9=0 \\ & 11\left(\sqrt{3} \cdot \mathrm{P}_{10}+\sqrt{2} \mathrm{P}_{11}-\mathrm{P}_{11}\right)-10\left(\sqrt{2} \mathrm{P}_{10}-\mathrm{P}_{11}\right) \\ & =0-10\left(-\sqrt{3} \mathrm{P}_9\right)=10 \sqrt{3} \mathrm{P}_9\end{aligned}$

</details>

---

### Q23. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha, \beta$ be the roots of the equation $x^2+2 \sqrt{2} x-1=0$. The quadratic equation, whose roots are $\alpha^4+\beta^4$ and $\frac{1}{10}\left(\alpha^6+\beta^6\right)$, is :

**Options:**

- **(A)** $x^2-190 x+9466=0$
- **(B)** $x^2-180 x+9506=0$
- **(C)** $x^2-195 x+9506=0$
- **(D)** $x^2-195 x+9466=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x^2-195 x+9506=0$**

**Detailed Solution:**

$\begin{aligned} & x^2+2 \sqrt{2} x-1=0 \\ & \alpha+\beta=-2 \sqrt{2} \\ & \alpha \beta=-1 \\ & \alpha^4+\beta^4=\left(\alpha^2+\beta^2\right)^2-2 \alpha^2 \beta^2 \\ & =\left((\alpha+\beta)^2-2 \alpha \beta\right)^2-2(\alpha \beta)^2 \\ & =(8+2)^2-2(-1)^2 \\ & =100-2=98 \\ & \alpha^6+\beta^6=\left(\alpha^3+\beta^3\right)^2-2 \alpha^3 \beta^3 \\ & =\left((\alpha+\beta)\left((\alpha+\beta)^2-3 \alpha \beta\right)^2-2(\alpha \beta)^3\right.\end{aligned}$
$\begin{aligned} & =(-2 \sqrt{2}(8+3))^2+2 \\ & =(8)(121)+2=970 \\ & \frac{1}{10}\left(\alpha^6+\beta^6\right)=97 \\ & x^2-(98+97) x+(98)(97)=0 \\ & \Rightarrow x^2-195 x+9506=0\end{aligned}$

</details>

---

### Q24. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all the solutions of the equation $(8)^{2 x}-16 \cdot(8)^x+48=0$ is :

**Options:**

- **(A)** $1+\log _8(6)$
- **(B)** $1+\log _6(8)$
- **(C)** $\log _8(6)$
- **(D)** $\log _8(4)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1+\log _8(6)$**

**Detailed Solution:**

$\begin{aligned} & (8)^{2 x}-16 \cdot(8)^x+48=0 \\ & \text { Put } 8^{\mathrm{x}}=\mathrm{t} \\ & \mathrm{t}^2-16+48=0 \\ & \Rightarrow \mathrm{t}=4 \text { or } \mathrm{t}=12 \\ & \Rightarrow 8^x=4 \quad 8^x=12 \\ & \Rightarrow \mathrm{x}=\log _8 \mathrm{x} \quad \mathrm{x}=\log _8 12 \\ & \end{aligned}$
sum of solution $=\log _8 4+\log _8 12$
$\begin{aligned} & =\log _8 48=\log _8(6.8) \\ & =1+\log _8 6\end{aligned}$

</details>

---

### Q25. JEE Main 2024 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $\alpha, \beta$ be roots of $x^2+\sqrt{2} x-8=0$. If $\mathrm{U}_{\mathrm{n}}=\alpha^{\mathrm{n}}+\beta^n$, then $\frac{\mathrm{U}_{10}+\sqrt{2} \mathrm{U}_9}{2 \mathrm{U}_8}$ is equal to______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

$\begin{aligned} & \frac{\alpha^{10}+\beta^{10}+\sqrt{2}\left(\alpha^9+\beta^9\right)}{2\left(\alpha^8+\beta^8\right)} \\ & \frac{\alpha^8\left(\alpha^2+\sqrt{2} \alpha\right)+\beta^8\left(\beta^2+\sqrt{2} \beta\right)}{2\left(\alpha^8+\beta^8\right)} \\ & \frac{8 \alpha^8+8 \beta^8}{2\left(\alpha^8+\beta^8\right)}=4\end{aligned}$

</details>

---

### Q26. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha, \beta$ be the distinct roots of the equation $x^2-\left(t^2-5 t+6\right) x+1=0, t \in \mathbb{R}$ and $a_n=\alpha^n+\beta^n$. Then the minimum value of $\frac{a_{2023}+a_{2025}}{a_{2024}}$ is

**Options:**

- **(A)** $-1 / 4$
- **(B)** $-1 / 4$
- **(C)** $-1 / 2$
- **(D)** $1 / 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-1 / 4$**

**Detailed Solution:**

by newton's theorem
$\begin{aligned}
& \mathrm{a}_{\mathrm{n}+2}-\left(\mathrm{t}^2-5 \mathrm{t}+6\right) \mathrm{a}_{\mathrm{n}+1}+\mathrm{a}_{\mathrm{n}}=0 \\
& \therefore \mathrm{a}_{2025}+\mathrm{a}_{2023}=\left(\mathrm{t}^2-5 \mathrm{t}+6\right) \mathrm{a}_{2024} \\
& \therefore \frac{\mathrm{a}_{2025}+\mathrm{a}_{2023}}{\mathrm{a}_{2024}}=\mathrm{t}^2-5 \mathrm{t}+6 \\
& \because \mathrm{t}^2-5 \mathrm{t}+6=\left(\mathrm{t}-\frac{5}{2}\right)^2-\frac{1}{4} \\
& \therefore \text { minimum value }=-\frac{1}{4}
\end{aligned}$

</details>

---

### Q27. JEE Main 2024 (05 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

The number of real solutions of the equation $x|x+5|+2|x+7|-2=0$ is_________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

Case I : $x \geq-5$
$\begin{aligned}
& x^2+5 x+2 x+12=0 \\
& x^2+7 x+12=0 \\
& x=-3,-4
\end{aligned}$
Case II : $-7 < \mathrm{x} < -5$
$-x^2-5 x+2 x+14-2=0$
$\begin{aligned}
& -x^2-3 x+12=0 \\
& x=\frac{-3 \pm \sqrt{9+48}}{2} \\
& =\frac{-3 \pm \sqrt{57}}{2} \\
& x=\frac{-3-\sqrt{57}}{2}, \frac{-3+\sqrt{57}}{2} \text { (rejected) }
\end{aligned}$
Case III : $\mathrm{x} \leq-7$
$\begin{aligned}
& -x^2-5 x-2 x-14-2=0 \\
& x^2+7 x+16=0 \\
& D=49-64 < 0
\end{aligned}$
No solutions
No. of solutions $=3$

</details>

---

### Q28. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If 2 and 6 are the roots of the equation $a x^2+b x+1=0$, then the quadratic equation, whose roots are $\frac{1}{2 a+b}$ and $\frac{1}{6 a+b}$, is :

**Options:**

- **(A)** $2 x^2+11 x+12=0$
- **(B)** $x^2+8 x+12=0$
- **(C)** $4 x^2+14 x+12=0$
- **(D)** $x^2+10 x+16=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2+8 x+12=0$**

**Detailed Solution:**

$\begin{aligned} & \text { Sum }=8=-\frac{b}{a} \\ & \text { Product }=12=\frac{1}{a} \quad \Rightarrow a=\frac{1}{12} \\ & b=-\frac{2}{3} \\ & 2 a+b=\frac{2}{12}-\frac{2}{3}=-\frac{1}{2} \\ & 6 a+b=\frac{6}{12}-\frac{2}{3}=-\frac{1}{6} \\ & \text { sum }=-8 \\ & P=12 \\ & x^2+8 x+12=0\end{aligned}$

</details>

---

### Q29. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>q</mi><mi>x</mi><mo>−</mo><mi>r</mi><mo>=</mo><mn>0</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>≠</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>,</mo><mo> </mo><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> be the consecutive terms of a non-constant G.P and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>α</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>β</mi></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>α</mi><mo>−</mo><mi>β</mi></mrow></mfenced><mn>2</mn></msup></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>80</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>20</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>80</mn><mn>9</mn></mfrac></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo> </mo><mtext>and</mtext><mo> </mo><mi>β</mi></math> be the roots of equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>q</mi><mi>x</mi><mo>-</mo><mi>r</mi><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mi>β</mi><mo>=</mo><mo>-</mo><mfrac><mi>q</mi><mi>p</mi></mfrac><mo>,</mo><mo> </mo><mi>α</mi><mi>β</mi><mo>=</mo><mo>-</mo><mfrac><mi>r</mi><mi>p</mi></mfrac></math></p><p>It is given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>α</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>β</mi></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mstyle displaystyle="true"><mi>α</mi><mo>+</mo><mi>β</mi></mstyle><mstyle displaystyle="true"><mi>α</mi><mi>β</mi></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>3</mn></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mstyle displaystyle="true"><mi>q</mi></mstyle><mstyle displaystyle="true"><mi>r</mi></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>3</mn></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>,</mo><mi>q</mi><mo>,</mo><mi>r</mi></math> are in GP</p><p>So, common ratio of this GP will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>q</mi><mi>p</mi></mfrac><mo>=</mo><mfrac><mi>r</mi><mi>q</mi></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>p</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>q</mi><mi>x</mi><mo>-</mo><mi>r</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mi>q</mi><mi>p</mi></mfrac><mi>x</mi><mo>-</mo><mfrac><mi>r</mi><mi>p</mi></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>x</mi><mo>-</mo><msup><mfenced><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mi>x</mi><mo>-</mo><mn>16</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mi>α</mi><mo>-</mo><mi>β</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>α</mi><mi>β</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mi>α</mi><mo>-</mo><mi>β</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mfrac><mrow><mo>-</mo><mn>12</mn></mrow><mn>9</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mfenced><mfrac><mrow><mo>-</mo><mn>16</mn></mrow><mn>9</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mi>α</mi><mo>-</mo><mi>β</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>16</mn><mn>9</mn></mfrac><mo>+</mo><mfrac><mn>64</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mi>α</mi><mo>-</mo><mi>β</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>80</mn><mn>9</mn></mfrac></math></p>

</details>

---

### Q30. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></math> be the length of three sides of a triangle satisfying the condition <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>b</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>c</mi></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mfenced><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math>. If the set of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi></mrow></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mfenced><mrow><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup></mrow></mfenced></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>b</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mi>x</mi><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>a</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>a</mi><mi>b</mi><mi>x</mi><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>b</mi><mi>c</mi><mi>x</mi><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mi>a</mi><mi>x</mi><mo>−</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>b</mi><mi>x</mi><mo>−</mo><mi>c</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mi>x</mi><mo>−</mo><mi>b</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>b</mi><mi>x</mi><mo>−</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mi>x</mi><mo>=</mo><mi>b</mi><mo>,</mo><mo> </mo><mi>b</mi><mi>x</mi><mo>=</mo><mi>c</mi></math></p><p>Now, we know that the sum of two sides is always greater than the third side of a triangle,</p><p>Now, taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>&gt;</mo><mi>c</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>+</mo><mi>a</mi><mi>x</mi><mo>&gt;</mo><mi>b</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>+</mo><mi>a</mi><mi>x</mi><mo>&gt;</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo>&lt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Similarly, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>+</mo><mi>c</mi><mo>&gt;</mo><mi>a</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>&gt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>∈</mo><mfenced><mrow><mo>-</mo><mo>∞</mo><mo>,</mo><mfrac><mrow><mo>−</mo><mn>1</mn><mo>−</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>∪</mo><mfenced><mrow><mfrac><mrow><mo>−</mo><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mo>∞</mo></mrow></mfenced><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>And for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>+</mo><mi>a</mi><mo>&gt;</mo><mi>b</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>&gt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>∈</mo><mi>R</mi><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>So, from the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mfrac><mrow><msqrt><mn>5</mn></msqrt><mo>−</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mfrac><mrow><msqrt><mn>5</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mfenced><mrow><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>12</mn><mfenced><mfrac><mrow><msup><mfenced><mrow><msqrt><mn>5</mn></msqrt><mo>−</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msqrt><mn>5</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>36</mn></math></p>

</details>

---

### Q31. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&lt;</mo><mi>c</mi><mo>&lt;</mo><mi>b</mi><mo>&lt;</mo><mi>a</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>–</mo><mn>2</mn><mi>c</mi><mo>)</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>(</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>–</mo><mn>2</mn><mi>a</mi><mo>)</mo><mi>x</mi><mo>+</mo><mo>(</mo><mi>c</mi><mo>+</mo><mi>a</mi><mo>–</mo><mn>2</mn><mi>b</mi><mo>)</mo><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>≠</mo><mn>1</mn></math> be one of its root. Then, among the two statements</p><p>(I) If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>∈</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>0</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> cannot be the geometric mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>.</p><p>(II) If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>∈</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo> </mo><mn>1</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> may be the geometric mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>.</p>

**Options:**

- **(A)** Both (I) and (II) are true
- **(B)** Neither (I) nor (II) is true
- **(C)** Only (II) is true
- **(D)** Only (I) is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Both (I) and (II) are true**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>–</mo><mn>2</mn><mi>c</mi><mo>)</mo><mo> </mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>(</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>–</mo><mn>2</mn><mi>a</mi><mo>)</mo><mo> </mo><mi>x</mi><mo>+</mo><mo>(</mo><mi>c</mi><mo>+</mo><mi>a</mi><mo>–</mo><mn>2</mn><mi>b</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>–</mo><mn>2</mn><mi>c</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>–</mo><mn>2</mn><mi>a</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>a</mi><mo>–</mo><mn>2</mn><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p>Using product of roots,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>·</mo><mn>1</mn><mo>=</mo><mfrac><mrow><mi>c</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn><mi>c</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mfrac><mrow><mi>c</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn><mi>c</mi></mrow></mfrac></math></p><p>If, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&lt;</mo><mi>α</mi><mo>&lt;</mo><mn>0</mn></math></p><p>Statement-I:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>1</mn><mo>&lt;</mo><mfrac><mrow><mi>c</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn><mi>c</mi></mrow></mfrac><mo>&lt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>&lt;</mo><mn>2</mn><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>&gt;</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mi>c</mi></mrow><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> cannot be G.M. between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><mi>A</mi><mo>.</mo><mi>M</mi><mo>≥</mo><mi>G</mi><mo>.</mo><mi>M</mi></mrow></mfenced></math></p><p>So, statement I is correct.</p><p>Statement-II:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>0</mn><mo>&lt;</mo><mi>α</mi><mo>&lt;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>0</mn><mo>&lt;</mo><mfrac><mrow><mi>c</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn><mi>c</mi></mrow></mfrac><mo>&lt;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>c</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn><mi>c</mi></mrow></mfrac><mo>&gt;</mo><mn>0</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mfrac><mrow><mi>c</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn><mi>c</mi></mrow></mfrac><mo>&lt;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>c</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn><mi>c</mi></mrow></mfrac><mo>&gt;</mo><mn>0</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mfrac><mrow><mi>c</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mo>-</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>+</mo><mn>2</mn><mi>c</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn><mi>c</mi></mrow></mfrac><mo>&lt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>c</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn><mi>c</mi></mrow></mfrac><mo>&gt;</mo><mn>0</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mfrac><mrow><mn>3</mn><mi>c</mi><mo>-</mo><mn>3</mn><mi>b</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn><mi>c</mi></mrow></mfrac><mo>&lt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>b</mi><mo>&lt;</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mi>c</mi></mrow><mn>2</mn></mfrac><mo> </mo><mo>&amp;</mo><mo> </mo><mi>b</mi><mo>&gt;</mo><mi>c</mi></math>  </p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> may be the G.M. between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><mi>A</mi><mo>.</mo><mi>M</mi><mo>≥</mo><mi>G</mi><mo>.</mo><mi>M</mi></mrow></mfenced></math></p><p>So, statement II is also correct.</p>

</details>

---

### Q32. JEE Main 2024 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let \(\alpha, \beta \in\) be roots of equation \(x^2-70 x+\lambda=0\), where \(\frac{\lambda}{2}, \frac{\lambda}{3} \notin\). If \(\lambda\) assumes the minimum possible value, then \(\frac{(\sqrt{\alpha-1}+\sqrt{\beta-1})(\lambda+35)}{\boldsymbol{|\alpha-\beta|}}\) is equal to :

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **60**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>70</mn><mi>x</mi><mo>+</mo><mi>λ</mi><mo>=</mo><mn>0</mn></math></p><p>Sum of the roots will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mi>β</mi><mo>=</mo><mn>70</mn></math></p><p>Product of roots will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mi>β</mi><mo>=</mo><mi>λ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>(</mo><mn>70</mn><mo>-</mo><mi>α</mi><mo>)</mo><mo>=</mo><mi>λ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>λ</mi></mrow><mrow><mi>d</mi><mi>α</mi></mrow></mfrac><mo>=</mo><mn>70</mn><mo>-</mo><mn>2</mn><mi>α</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math> is increasing for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>≤</mo><mn>35</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> does not divide <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math> so taking  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mn>5</mn></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><mn>70</mn><mo>-</mo><mi>α</mi><mo>=</mo><mn>65</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>As</mtext><mo> </mo><mtext>for</mtext><mo> </mo><mi>α</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mn>69</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mtext>for</mtext><mo> </mo><mi>α</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mn>66</mn></math> which is not possible as they are multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mn>65</mn><mo>,</mo><mo> </mo><mi>λ</mi><mo>=</mo><mn>325</mn></math></p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><msqrt><mi>α</mi><mo>-</mo><mn>1</mn></msqrt><mo>+</mo><msqrt><mi>β</mi><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mfenced><mrow><mi>λ</mi><mo>+</mo><mn>35</mn></mrow></mfenced></mrow><mrow><mo>|</mo><mi>α</mi><mo>-</mo><mi>β</mi><mo>|</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><msqrt><mn>5</mn><mo>-</mo><mn>1</mn></msqrt><mo>+</mo><msqrt><mn>65</mn><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mfenced><mrow><mn>325</mn><mo>+</mo><mn>35</mn></mrow></mfenced></mrow><mrow><mo>|</mo><mn>5</mn><mo>-</mo><mn>65</mn><mo>|</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>2</mn><mo>+</mo><mn>8</mn></mrow></mfenced><mo>·</mo><mn>360</mn></mrow><mn>60</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>60</mn></math></p>

</details>

---

### Q33. JEE Main 2024 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>∣</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mn>2</mn><mi>y</mi></msup><mo>=</mo><mn>2023</mn><mo>,</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>∈</mo><mi mathvariant="normal">ℕ</mi></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>∑</mo><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>∈</mo><mi>C</mi></mrow></munder><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>)</mo></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **46**

**Detailed Solution:**

<p>Given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mn>2</mn><mi>y</mi></msup><mo>=</mo><mn>2023</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><msup><mn>2</mn><mi>y</mi></msup><mo>+</mo><mn>2023</mn></math></p><p>Now, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>2025</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>45</mn></math></p><p>And there is no other value which will satisfy the above equation,</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>45</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mi>y</mi><mo>=</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>∑</mo><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>∈</mo><mi>C</mi></mrow></munder><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>)</mo><mo>=</mo><mn>45</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>46</mn></math></p>

</details>

---

### Q34. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mi>β</mi></math> are the roots of the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mi mathvariant="normal">x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">S</mi><mi mathvariant="normal">n</mi></msub><mo>=</mo><mn>2023</mn><msup><mi>α</mi><mi mathvariant="normal">n</mi></msup><mo>+</mo><mn>2024</mn><msup><mi>β</mi><mi mathvariant="normal">n</mi></msup></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><msub><mi mathvariant="normal">S</mi><mn>12</mn></msub><mo>=</mo><msub><mi mathvariant="normal">S</mi><mn>11</mn></msub><mo>+</mo><msub><mi mathvariant="normal">S</mi><mn>10</mn></msub></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">S</mi><mn>12</mn></msub><mo>=</mo><msub><mi mathvariant="normal">S</mi><mn>11</mn></msub><mo>+</mo><msub><mi mathvariant="normal">S</mi><mn>10</mn></msub></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><msub><mi mathvariant="normal">S</mi><mn>11</mn></msub><mo>=</mo><msub><mi mathvariant="normal">S</mi><mn>12</mn></msub><mo>+</mo><msub><mi mathvariant="normal">S</mi><mn>10</mn></msub></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">S</mi><mn>11</mn></msub><mo>=</mo><msub><mi mathvariant="normal">S</mi><mn>10</mn></msub><mo>+</mo><msub><mi mathvariant="normal">S</mi><mn>12</mn></msub></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">S</mi><mn>12</mn></msub><mo>=</mo><msub><mi mathvariant="normal">S</mi><mn>11</mn></msub><mo>+</mo><msub><mi mathvariant="normal">S</mi><mn>10</mn></msub></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mo> </mo><mi>β</mi></math> are roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mi mathvariant="normal">x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>2</mn></msup><mo>-</mo><mi>α</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>2</mn></msup><mo>=</mo><mi>α</mi><mo>+</mo><mn>1</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">S</mi><mi mathvariant="normal">n</mi></msub><mo>=</mo><mn>2023</mn><msup><mi mathvariant="normal">α</mi><mi mathvariant="normal">n</mi></msup><mo>+</mo><mn>2024</mn><msup><mi mathvariant="normal">β</mi><mi mathvariant="normal">n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">S</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi mathvariant="normal">S</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>2023</mn><msup><mi mathvariant="normal">α</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>2024</mn><msup><mi mathvariant="normal">β</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>2023</mn><msup><mi mathvariant="normal">α</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>+</mo><mn>2024</mn><msup><mi mathvariant="normal">β</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">S</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi mathvariant="normal">S</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>2023</mn><msup><mi mathvariant="normal">α</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">α</mi></mrow></mfenced><mo>+</mo><mn>2024</mn><msup><mi mathvariant="normal">β</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">β</mi></mrow></mfenced></math></p><p>Using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">S</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi mathvariant="normal">S</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>2023</mn><msup><mi mathvariant="normal">α</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msup><mfenced><msup><mi mathvariant="normal">α</mi><mn>2</mn></msup></mfenced><mo>+</mo><mn>2024</mn><msup><mi mathvariant="normal">β</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msup><mfenced><msup><mi mathvariant="normal">β</mi><mn>2</mn></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">S</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi mathvariant="normal">S</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>2023</mn><msup><mi>α</mi><mi mathvariant="normal">n</mi></msup><mo>+</mo><mn>2024</mn><msup><mi mathvariant="normal">β</mi><mi mathvariant="normal">n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">S</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi mathvariant="normal">S</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msub><mo>=</mo><msub><mi mathvariant="normal">S</mi><mi mathvariant="normal">n</mi></msub></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">S</mi><mn>12</mn></msub><mo>=</mo><msub><mi mathvariant="normal">S</mi><mn>11</mn></msub><mo>+</mo><msub><mi mathvariant="normal">S</mi><mn>10</mn></msub></math></p>

</details>

---

### Q35. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of real roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>-</mo><mn>5</mn><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>-</mo><mn>5</mn><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p>Now taking case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>2</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>10</mn><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>16</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>89</mn></msqrt></mrow><mn>2</mn></mfrac></math>, ignoring <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>+</mo><msqrt><mn>89</mn></msqrt></mrow><mn>2</mn></mfrac></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>2</mn></math>, so one solution is possible here,</p><p>Now taking case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>10</mn><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>, ignoring <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>4</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></math></p><p>Now taking case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math>, when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>10</mn><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>+</mo><msqrt><mn>41</mn></msqrt></mrow><mn>2</mn></mfrac></math>, ignoring <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>41</mn></msqrt></mrow><mn>2</mn></mfrac></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math></p><p>So, from all cases we get total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> solutions.</p></blockquote>

</details>

---

### Q36. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></math>  be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msqrt><mn>2</mn><mi>x</mi></msqrt><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>14</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>14</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>64</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>64</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>128</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>128</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>128</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>&#177;</mo><msqrt><mn>6</mn></msqrt><mi>i</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mfenced><mfrac><mrow><mn>1</mn><mo>&#177;</mo><msqrt><mn>3</mn></msqrt><mi>i</mi></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#177;</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>i</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mfenced><mrow><mi>cos</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mo>&#177;</mo><mi>i</mi><mi>sin</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mfenced><mrow><mi>cos</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mo>+</mo><mi>i</mi><mi>sin</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt><msup><mi>e</mi><mfrac><mi>i&#960;</mi><mn>3</mn></mfrac></msup></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mfenced><mrow><mi>cos</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mo>-</mo><mi>i</mi><mi>sin</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mi>i&#960;</mi></mrow><mn>3</mn></mfrac></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>14</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>14</mn></msup><mo>=</mo><msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><msup><mi>e</mi><mfrac><mi>i&#960;</mi><mn>3</mn></mfrac></msup></mrow></mfenced><mn>14</mn></msup><mo>+</mo><msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mi>i&#960;</mi></mrow><mn>3</mn></mfrac></msup></mrow></mfenced><mn>14</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>14</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>14</mn></msup><mo>=</mo><msup><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mn>14</mn></msup><mfenced><mrow><msup><mi>e</mi><mfrac><mrow><mi>i</mi><mn>14</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></msup><mo>+</mo><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mi>i</mi><mn>14</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>14</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>14</mn></msup><mo>=</mo><msup><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mn>14</mn></msup><mfenced><mrow><mi>cos</mi><mfrac><mrow><mn>14</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mi>i</mi><mi>sin</mi><mfrac><mrow><mn>14</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mi>cos</mi><mfrac><mrow><mn>14</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac><mo>-</mo><mi>i</mi><mi>sin</mi><mfrac><mrow><mn>14</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>14</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>14</mn></msup><mo>=</mo><msup><mn>2</mn><mn>7</mn></msup><mfenced><mrow><mn>2</mn><mi>cos</mi><mfrac><mrow><mn>14</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>14</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>14</mn></msup><mo>=</mo><msup><mn>2</mn><mn>8</mn></msup><mfenced><mrow><mi>cos</mi><mfenced><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>14</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>14</mn></msup><mo>=</mo><msup><mn>2</mn><mn>8</mn></msup><mfenced><mrow><mi>cos</mi><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>14</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>14</mn></msup><mo>=</mo><mo>-</mo><msup><mn>2</mn><mn>8</mn></msup><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mn>128</mn></math></p></blockquote>

</details>

---

### Q37. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></math> be the roots of the quadratic equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msqrt><mn>6</mn></msqrt><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>&#945;</mi><mn>23</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>23</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>14</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>14</mn></msup></mrow><mrow><msup><mi>&#945;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>10</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>10</mn></msup></mrow></mfrac></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>81</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>729</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>81</mn></math>**

**Detailed Solution:**

<p>To find the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>&#945;</mi><mn>23</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>23</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>14</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>14</mn></msup></mrow><mrow><msup><mi>&#945;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>10</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>10</mn></msup></mrow></mfrac></math>,</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msup><mi>&#945;</mi><mi>n</mi></msup><mo>+</mo><msup><mi>&#946;</mi><mi>n</mi></msup></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>&#945;</mi><mn>23</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>23</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>14</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>14</mn></msup></mrow><mrow><msup><mi>&#945;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>10</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>10</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mi>a</mi><mn>23</mn></msub><mo>+</mo><msub><mi>a</mi><mn>14</mn></msub></mrow><mrow><msub><mi>a</mi><mn>15</mn></msub><mo>+</mo><msub><mi>a</mi><mn>10</mn></msub></mrow></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msqrt><mn>6</mn></msqrt><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math> has roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#946;</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><msqrt><mn>6</mn></msqrt><mo>&#177;</mo><msqrt><mo>-</mo><mn>6</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msqrt><mn>6</mn></msqrt><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><mi>i</mi></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><mi>i</mi></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><msup><mi>e</mi><mfrac><mrow><mi>i</mi><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><msup><mi>e</mi><mfrac><mrow><mi>i</mi><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></msup></math></p><p>Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>&#945;</mi><mn>23</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>23</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>14</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>14</mn></msup></mrow><mrow><msup><mi>&#945;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>10</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>10</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="[" close="]"><mfrac><mrow><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>23</mn></msup><mfenced><mrow><msup><mi>e</mi><mrow><mi>i</mi><mn>23</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mi>i</mi><mn>23</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup></mrow></mfenced><mo>+</mo><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>14</mn></msup><mfenced><mrow><msup><mi>e</mi><mrow><mi>i</mi><mn>14</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mi>i</mi><mn>14</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup></mrow></mfenced></mrow><mrow><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>15</mn></msup><mfenced><mrow><msup><mi>e</mi><mrow><mi>i</mi><mn>15</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mi>i</mi><mn>15</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup></mrow></mfenced><mo>+</mo><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>10</mn></msup><mfenced><mrow><msup><mi>e</mi><mrow><mi>i</mi><mn>10</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mi>i</mi><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup></mrow></mfenced></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>4</mn></msup><mfenced close="]" open="["><mfrac><mrow><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>9</mn></msup><mfenced><mrow><msup><mi>e</mi><mrow><mi>i</mi><mn>23</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mi>i</mi><mn>23</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>e</mi><mrow><mi>i</mi><mn>14</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mi>i</mi><mn>14</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup></mrow></mfenced></mrow><mrow><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>5</mn></msup><mfenced><mrow><msup><mi>e</mi><mrow><mi>i</mi><mn>15</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mi>i</mi><mn>15</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>e</mi><mrow><mi>i</mi><mn>10</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mi>i</mi><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mstyle></mrow></msup></mrow></mfenced></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>&#215;</mo><mfenced><mfrac><mrow><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>9</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mo>-</mo><mn>1</mn><mo>+</mo><mi>i</mi></mrow><msqrt><mn>2</mn></msqrt></mfrac></mstyle></mfenced><mo>+</mo><mn>0</mn></mrow><mrow><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>5</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mo>-</mo><mn>1</mn><mo>+</mo><mi>i</mi></mrow><msqrt><mn>2</mn></msqrt></mfrac></mstyle></mfenced><mo>+</mo><mn>0</mn></mrow></mfrac></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>21</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>35</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac></mrow></msup><mo>=</mo><mn>0</mn><mo>+</mo><mi>i</mi><mi>sin</mi><mfrac><mrow><mn>21</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mn>0</mn><mo>+</mo><mi>i</mi><mi>sin</mi><mfrac><mrow><mn>35</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mi>i</mi><mo>-</mo><mi>i</mi><mo>=</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>&#215;</mo><mfenced><mfrac><mrow><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>9</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi>i</mi></mrow><msqrt><mn>2</mn></msqrt></mfrac></mstyle></mfenced></mrow><mrow><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>5</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi>i</mi></mrow><msqrt><mn>2</mn></msqrt></mfrac></mstyle></mfenced></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>81</mn></math></p>

</details>

---

### Q38. JEE Main 2023 (11 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>a</mi><mn>21</mn></msup><mo>+</mo><msup><mi>b</mi><mn>21</mn></msup><mo>+</mo><msup><mi>a</mi><mn>17</mn></msup><mo>+</mo><msup><mi>b</mi><mn>17</mn></msup></mrow><mrow><msup><mi>a</mi><mn>19</mn></msup><mo>+</mo><msup><mi>b</mi><mn>19</mn></msup></mrow></mfrac></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **51**

**Detailed Solution:**

<blockquote><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> are roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi>a</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>7</mn><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mn>49</mn><msup><mi>a</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>51</mn><msup><mi>a</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Similarly,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>51</mn><msup><mi>b</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>a</mi><mn>21</mn></msup><mo>+</mo><msup><mi>b</mi><mn>21</mn></msup><mo>+</mo><msup><mi>a</mi><mn>17</mn></msup><mo>+</mo><msup><mi>b</mi><mn>17</mn></msup></mrow><mrow><msup><mi>a</mi><mn>19</mn></msup><mo>+</mo><msup><mi>b</mi><mn>19</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mi>a</mi><mn>17</mn></msup><mfenced><mrow><msup><mi>a</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msup><mi>b</mi><mn>17</mn></msup><mfenced><mrow><msup><mi>b</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mi>a</mi><mn>19</mn></msup><mo>+</mo><msup><mi>b</mi><mn>19</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>51</mn><msup><mi>a</mi><mn>19</mn></msup><mo>+</mo><mn>51</mn><msup><mi>b</mi><mn>19</mn></msup></mrow><mrow><msup><mi>a</mi><mn>19</mn></msup><mo>+</mo><msup><mi>b</mi><mn>19</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>51</mn></math></p></blockquote>

</details>

---

### Q39. JEE Main 2023 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> be the numbers of real roots of the quadratic equations <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>31</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mo>|</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>|</mo><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> respectively, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><mi>m</mi><mi>n</mi><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mn>31</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><munder><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>31</mn></mrow><mo>&#9183;</mo></munder><mrow><mo>&#8805;</mo><mo>-</mo><mn>5</mn></mrow></munder><mo>=</mo><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></math></p><p>Now from above equation we say that, it could have its solution in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>)</mo></math> but it does not exist as at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn></math> as LHS<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math>,</p><p>So no solution, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>0</mn></math></p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p>Taking Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mo>-</mo><mn>2</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>14</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>7</mn><mo>,</mo><mo>-</mo><mn>2</mn></math></p><p>Now taking Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>2</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>10</mn><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>3</mn></math></p><p>So, total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> solution i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>3</mn></math></p><p>So, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><mi>m</mi><mi>n</mi><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>+</mo><mn>0</mn><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>=</mo><mn>9</mn></math></p></blockquote>

</details>

---

### Q40. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>The sum of all the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>15</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>0</mn></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>15</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p>Now taking Case:<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> when,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>15</mn><mo>&#8805;</mo><mn>0</mn><mo>&#8658;</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>5</mn><mo>)</mo><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8804;</mo><mn>3</mn></math> OR <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>15</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>15</mn><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>22</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>5</mn><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mfenced><mtext>rejected</mtext></mfenced></math> </p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>5</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math></p><p>Now taking Case:<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> when,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>15</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>15</mn><mo>&#60;</mo><mn>0</mn><mo>&#8658;</mo><mn>3</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>15</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo><mfenced><mtext>rejected</mtext></mfenced></math> </p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi><mo>=</mo><mn>4</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>9</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math></p></blockquote>

</details>

---

### Q41. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The number of real roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></msqrt><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn></msqrt><mo>=</mo><msqrt><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>14</mn><mi>x</mi><mo>+</mo><mn>6</mn></msqrt></math>, is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></msqrt><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn></msqrt><mo>=</mo><msqrt><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>14</mn><mi>x</mi><mo>+</mo><mn>6</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msqrt><mo>+</mo><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></msqrt><mo>=</mo><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></msqrt><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msqrt><mo>+</mo><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></msqrt><msqrt><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></msqrt><mo>-</mo><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></msqrt><msqrt><mfenced><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></msqrt><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></msqrt><mo>=</mo><mn>0</mn><mo>&#160;</mo><mtext>or&#160;</mtext><mfenced close="]" open="["><mrow><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msqrt><mo>+</mo><msqrt><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></msqrt><mo>-</mo><msqrt><mfenced><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></msqrt></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math> is one solution and also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>3</mn></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msqrt><mo>+</mo><msqrt><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></msqrt><mo>-</mo><msqrt><mfenced><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></msqrt></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msqrt><mo>+</mo><msqrt><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></msqrt><mo>=</mo><msqrt><mfenced><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></msqrt></math></p><p>Now squaring both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>2</mn><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></msqrt><mo>=</mo><mfenced><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msqrt><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></msqrt><mo>=</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>x</mi><mo>=</mo><mn>7</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>7</mn><mn>6</mn></mfrac></math> which does not satisfy the given expression and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>3</mn></math></p><p>So, there is only one solution which is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q42. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8800;</mo><mn>0</mn></math> be a real number. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>31</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#947;</mi></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>53</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#945;</mi></mrow><mi>&#946;</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mi>&#945;</mi></mrow><mi>&#947;</mi></mfrac></math> are the roots of the equation :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>245</mn><mi>x</mi><mo>-</mo><mn>250</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>245</mn><mi>x</mi><mo>+</mo><mn>250</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>245</mn><mi>x</mi><mo>+</mo><mn>250</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>245</mn><mi>x</mi><mo>+</mo><mn>250</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>245</mn><mi>x</mi><mo>+</mo><mn>250</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are roots of the below equation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>31</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>31</mn><mn>14</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#955;</mi></mrow><mn>14</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi></math> are roots of the below equation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>53</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mfrac><mn>53</mn><mn>35</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>3</mn></mfenced></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#947;</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mi>&#955;</mi></mrow><mn>35</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>4</mn></mfenced></math></p><p>On dividing equation<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>  and equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#946;</mi><mi>&#947;</mi></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#215;</mo><mn>35</mn></mrow><mrow><mn>4</mn><mo>&#215;</mo><mn>14</mn></mrow></mfrac><mo>=</mo><mfrac><mn>15</mn><mn>8</mn></mfrac><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>15</mn><mn>8</mn></mfrac><mi>&#947;</mi></math></p><p>On subtracting equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>-</mo><mi>&#947;</mi><mo>=</mo><mfrac><mn>31</mn><mn>14</mn></mfrac><mo>-</mo><mfrac><mn>53</mn><mn>35</mn></mfrac><mo>=</mo><mfrac><mrow><mn>155</mn><mo>-</mo><mn>106</mn></mrow><mn>70</mn></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>15</mn><mn>8</mn></mfrac><mi>&#947;</mi><mo>-</mo><mi>&#947;</mi><mo>=</mo><mfrac><mn>7</mn><mn>10</mn></mfrac><mo>&#8658;</mo><mi>&#947;</mi><mo>=</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>15</mn><mn>8</mn></mfrac><mo>&#215;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mn>31</mn><mn>14</mn></mfrac><mo>-</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>31</mn><mn>14</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>7</mn></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mfrac><mn>14</mn><mn>3</mn></mfrac><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mfrac><mn>14</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>7</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>=</mo><mn>5</mn></math></p><p>So, the sum of the roots of the required equation,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#945;</mi></mrow><mi>&#946;</mi></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mi>&#945;</mi></mrow><mi>&#947;</mi></mfrac><mo>=</mo><mfenced><mfrac><mrow><mn>3</mn><mi>&#945;</mi><mi>&#947;</mi><mo>+</mo><mn>4</mn><mi>&#945;</mi><mi>&#946;</mi></mrow><mrow><mi>&#946;</mi><mi>&#947;</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced><mrow><mn>3</mn><mo>&#215;</mo><mfrac><mrow><mn>4</mn><mi>&#955;</mi></mrow><mn>35</mn></mfrac><mo>+</mo><mn>4</mn><mo>&#215;</mo><mfrac><mrow><mn>3</mn><mi>&#955;</mi></mrow><mn>14</mn></mfrac></mrow></mfenced><mrow><mi>&#946;</mi><mi>&#947;</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>12</mn><mi>&#955;</mi><mfenced><mrow><mn>14</mn><mo>+</mo><mn>35</mn></mrow></mfenced></mrow><mrow><mn>14</mn><mo>&#215;</mo><mn>35</mn><mi>&#946;</mi><mi>&#947;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>49</mn><mo>&#215;</mo><mn>12</mn><mo>&#215;</mo><mn>5</mn></mrow><mrow><mn>490</mn><mo>&#215;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></mrow></mfrac><mo>=</mo><mn>5</mn></math></p><p>And the product of the roots of the required equation,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#945;</mi></mrow><mi>&#946;</mi></mfrac><mo>&#215;</mo><mfrac><mrow><mn>4</mn><mi>&#945;</mi></mrow><mi>&#947;</mi></mfrac><mo>=</mo><mfrac><mrow><mn>12</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mrow><mrow><mi>&#946;</mi><mi>&#947;</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>12</mn><mo>&#215;</mo><mfrac><mn>25</mn><mn>49</mn></mfrac></mrow><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mn>250</mn><mn>49</mn></mfrac></math></p><p>So, the required equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mo>(</mo><mtext>sum&#160;of&#160;roots</mtext><mo>)</mo><mi>x</mi><mo>+</mo><mtext>product&#160;of&#160;roots</mtext><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mfrac><mn>250</mn><mn>49</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>49</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>245</mn><mi>x</mi><mo>+</mo><mn>250</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q43. JEE Main 2023 (25 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>R</mi></math> and let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mn>60</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mi>x</mi><mo>+</mo><mi>a</mi><mo>=</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>4</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>4</mn></msup><mo>=</mo><mo>-</mo><mn>30</mn></math>, then the product of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **45**

**Detailed Solution:**

<p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mn>60</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mi>x</mi><mo>+</mo><mi>a</mi><mo>=</mo><mn>0</mn></math>, therefore</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><msup><mn>60</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mi>a</mi></math></p><p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>4</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>4</mn></msup><mo>=</mo><mo>-</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>&#945;</mi><mn>2</mn></msup><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="}" open="{"><mrow><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="}" open="{"><mrow><msup><mn>60</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><mn>2</mn><mi>a</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>60</mn><mo>+</mo><mn>4</mn><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>a</mi><mo>&#215;</mo><msup><mn>60</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#183;</mo><msup><mn>60</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mi>a</mi><mo>+</mo><mn>90</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>&#183;</mo><msup><mn>60</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mi>a</mi><mo>+</mo><mn>45</mn><mo>=</mo><mn>0</mn></math></p><p>Product of roots<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>45</mn></math></p>

</details>

---

### Q44. JEE Main 2023 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math> and let the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>x</mi><msup><mo>|</mo><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>|</mo><mi>x</mi><mo>|</mo><mo>+</mo><mo>|</mo><mi>&#955;</mi><mo>-</mo><mn>3</mn><mo>|</mo><mo>=</mo><mn>0</mn></math>. Then the largest element in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi>x</mi><mo>+</mo><mi>&#955;</mi><mo>:</mo><mi>x</mi></math> is an integer solution of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>}</mo></math> is ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>x</mi><msup><mo>|</mo><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>|</mo><mi>x</mi><mo>|</mo><mo>+</mo><mo>|</mo><mi>&#955;</mi><mo>-</mo><mn>3</mn><mo>|</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>&#955;</mi><mo>-</mo><mn>3</mn><mo>|</mo><mo>=</mo><mfenced open="|" close="|"><mi>x</mi></mfenced><mfenced><mrow><mn>2</mn><mo>-</mo><mfenced open="|" close="|"><mi>x</mi></mfenced></mrow></mfenced></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>3</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>,</p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>4</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math></p><p>So, maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>&#955;</mi><mo>=</mo><mn>5</mn></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>4</mn></math>.</p>

</details>

---

### Q45. JEE Main 2022 (29 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mfenced><mrow><mi>&#945;</mi><mo>&#62;</mo><mi>&#946;</mi></mrow></mfenced></math> be the roots of the quadratic equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mi>n</mi></msub><mo>=</mo><msup><mi>&#945;</mi><mi>n</mi></msup><mo>-</mo><msup><mi>&#946;</mi><mi>n</mi></msup><mo>,</mo><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>P</mi><mn>15</mn></msub><msub><mi>P</mi><mn>16</mn></msub><mo>-</mo><msub><mi>P</mi><mn>14</mn></msub><msub><mi>P</mi><mn>16</mn></msub><mo>-</mo><msubsup><mi>P</mi><mn>15</mn><mn>2</mn></msubsup><mo>+</mo><msub><mi>P</mi><mn>14</mn></msub><msub><mi>P</mi><mn>15</mn></msub></mrow><mrow><msub><mi>P</mi><mn>13</mn></msub><msub><mi>P</mi><mn>14</mn></msub></mrow></mfrac></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mi>n</mi></msub><mo>=</mo><msup><mi>&#945;</mi><mi mathvariant="normal">n</mi></msup><mo>-</mo><msup><mi>&#946;</mi><mi mathvariant="normal">n</mi></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#946;</mi></math> are roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p>Now putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>-</mo><mn>1</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mi>n</mi></msub><mo>=</mo><msup><mi>&#945;</mi><mi mathvariant="normal">n</mi></msup><mo>-</mo><msup><mi>&#946;</mi><mi mathvariant="normal">n</mi></msup></math> we get,  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mfenced><mrow><msup><mi>&#945;</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><msup><mi>&#946;</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p>Now subtracting <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mi>n</mi></msub><mo>-</mo><msub><mi>P</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mi>n</mi></msub><mo>-</mo><msub><mi>P</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mfenced><mrow><msup><mi>&#945;</mi><mi>n</mi></msup><mo>-</mo><msup><mi>&#946;</mi><mi>n</mi></msup></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mi>&#945;</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><msup><mi>&#946;</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>P</mi><mi>n</mi></msub><mo>-</mo><msub><mi>P</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><msup><mi>&#945;</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>-</mo><msup><mi>&#946;</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mfenced><mrow><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mi>&#946;</mi></mrow></mfenced></math></p><p>Now using the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mi>&#946;</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mi>n</mi></msub><mo>-</mo><msub><mi>P</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>4</mn><mfenced><mrow><msup><mi>&#945;</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><msup><mi>&#946;</mi><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mi>n</mi></msub><mo>-</mo><msub><mi>P</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>4</mn><msub><mi>P</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msub></math></p><p>Now putting the value in given expression </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>P</mi><mn>15</mn></msub><msub><mi>P</mi><mn>16</mn></msub><mo>-</mo><msub><mi>P</mi><mn>14</mn></msub><msub><mi>P</mi><mn>16</mn></msub><mo>-</mo><msubsup><mi>P</mi><mn>15</mn><mn>2</mn></msubsup><mo>+</mo><msub><mi>P</mi><mn>14</mn></msub><msub><mi>P</mi><mn>15</mn></msub></mrow><mrow><msub><mi>P</mi><mn>13</mn></msub><msub><mi>P</mi><mn>14</mn></msub></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msub><mi>P</mi><mn>16</mn></msub><mfenced><mrow><msub><mi>P</mi><mn>15</mn></msub><mo>-</mo><msub><mi>P</mi><mn>14</mn></msub></mrow></mfenced><mo>-</mo><msub><mi>P</mi><mn>15</mn></msub><mfenced><mrow><msub><mi>P</mi><mn>15</mn></msub><mo>-</mo><msub><mi>P</mi><mn>14</mn></msub></mrow></mfenced></mrow><mrow><msub><mi>P</mi><mn>13</mn></msub><msub><mi>P</mi><mn>14</mn></msub></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><msub><mi>P</mi><mn>15</mn></msub><mo>-</mo><msub><mi>P</mi><mn>14</mn></msub></mrow></mfenced><mfenced><mrow><msub><mi>P</mi><mn>16</mn></msub><mo>-</mo><msub><mi>P</mi><mn>15</mn></msub></mrow></mfenced></mrow><mrow><msub><mi>P</mi><mn>13</mn></msub><msub><mi>P</mi><mn>14</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>4</mn><msub><mi>P</mi><mn>13</mn></msub></mrow></mfenced><mfenced><mrow><mn>4</mn><msub><mi>P</mi><mn>14</mn></msub></mrow></mfenced></mrow><mrow><msub><mi>P</mi><mn>13</mn></msub><msub><mi>P</mi><mn>14</mn></msub></mrow></mfrac><mo>=</mo><mn>16</mn></math></p></blockquote>

</details>

---

### Q46. JEE Main 2022 (28 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>+</mo><msqrt><mn>6</mn></msqrt><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>1</mn><mo>,</mo><mfrac><mn>1</mn><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>1</mn></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn></math>. Then the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> are :

**Options:**

- **(A)** non-real complex numbers
- **(B)** real and both negative
- **(C)** real and both positive
- **(D)** real and exactly one of them is positive

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) real and both negative**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>+</mo><msqrt><mn>6</mn></msqrt><mo>=</mo><mn>0</mn></math> </p><p>So sum of roots will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><msqrt><mn>2</mn></msqrt></math> and product of roots will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><msqrt><mn>6</mn></msqrt></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><p>And also given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>1</mn></math> are roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p>So sum of roots will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msup><mi>&#945;</mi><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac><mo>-</mo><mn>2</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And similarly product of roots will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mfrac><mn>1</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now adding equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mfrac><mn>1</mn><msup><mfenced><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>-</mo><mn>1</mn><mo>=</mo><mo>-</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math> {as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><msqrt><mn>6</mn></msqrt></math>}</p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mo>-</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>-</mo><mn>2</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>17</mn><mi>x</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>7</mn><mn>3</mn></mfrac><mo>,</mo><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> are the roots, both roots are real and negative.</p></blockquote>

</details>

---

### Q47. JEE Main 2022 (28 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

The sum of all real values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mi>x</mi><mo>+</mo><mn>17</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>19</mn></mrow><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow></mfrac></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mi>x</mi><mo>+</mo><mn>17</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>19</mn></mrow><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>10</mn><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>7</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>12</mn><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>7</mn></mrow><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>7</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>7</mn></mrow><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>7</mn></mrow></mfenced><mfenced><mrow><mfrac><mn>1</mn><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>0</mn></math> Or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>12</mn><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>10</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p>Sum of roots<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>12</mn><mn>2</mn></mfrac><mo>=</mo><mn>6</mn></math></p><p>Or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>12</mn><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>No real roots as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>1</mn><mo>-</mo><mn>4</mn><mo>&#60;</mo><mn>0</mn></math></p></blockquote>

</details>

---

### Q48. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mn>5</mn><mo>+</mo><msup><mn>3</mn><msqrt><msub><mi>log</mi><mn>3</mn></msub><mn>5</mn></msqrt></msup><mo>-</mo><msup><mn>5</mn><msqrt><msub><mi>log</mi><mn>5</mn></msub><mn>3</mn></msqrt></msup></mrow></mfenced><mi>x</mi><mo>+</mo><mn>3</mn><mfenced><mrow><msup><mn>3</mn><msup><mfenced><mrow><msub><mi>log</mi><mn>3</mn></msub><mn>5</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></msup><mo>-</mo><msup><mn>5</mn><msup><mfenced><mrow><msub><mi>log</mi><mn>5</mn></msub><mn>3</mn></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> then the equation, whose roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>+</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></math>,

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>20</mn><mi>x</mi><mo>-</mo><mn>12</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>20</mn><mi>x</mi><mo>+</mo><mn>16</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mn>5</mn><mo>+</mo><msup><mn>3</mn><msqrt><msub><mi>log</mi><mn>3</mn></msub><mn>5</mn></msqrt></msup><mo>-</mo><msup><mn>5</mn><msqrt><msub><mi>log</mi><mn>5</mn></msub><mn>3</mn></msqrt></msup></mrow></mfenced><mi>x</mi><mo>+</mo><mn>3</mn><mfenced><mrow><msup><mn>3</mn><msup><mfenced><mrow><msub><mi>log</mi><mn>3</mn></msub><mn>5</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></msup><mo>-</mo><msup><mn>5</mn><msup><mfenced><mrow><msub><mi>log</mi><mn>5</mn></msub><mn>3</mn></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><msqrt><msub><mi>log</mi><mn>3</mn></msub><mn>5</mn></msqrt></msup><mo>-</mo><msup><mn>5</mn><msqrt><msub><mi>log</mi><mn>5</mn></msub><mn>3</mn></msqrt></msup><mo>=</mo><msup><mn>3</mn><msqrt><msub><mi>log</mi><mn>3</mn></msub><mn>5</mn></msqrt></msup><mo>-</mo><msup><mfenced><msup><mn>3</mn><mrow><msub><mi>log</mi><mn>3</mn></msub><mn>5</mn></mrow></msup></mfenced><msqrt><msub><mi>log</mi><mn>5</mn></msub><mn>3</mn></msqrt></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>3</mn><msqrt><msub><mi>log</mi><mn>3</mn></msub><mn>5</mn></msqrt></msup><mo>-</mo><msup><mn>3</mn><msqrt><msub><mi>log</mi><mn>3</mn></msub><mn>5</mn></msqrt></msup><mo>=</mo><mn>0</mn></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><msup><mfenced><mrow><msub><mi>log</mi><mn>3</mn></msub><mn>5</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></msup><mo>-</mo><msup><mn>5</mn><msup><mfenced><mrow><msub><mi>log</mi><mn>5</mn></msub><mn>3</mn></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></msup><mo>=</mo><msup><mn>5</mn><msup><mfenced><mrow><msub><mi>log</mi><mn>5</mn></msub><mn>3</mn></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></msup><mo>-</mo><msup><mn>5</mn><msup><mfenced><mrow><msub><mi>log</mi><mn>5</mn></msub><mn>3</mn></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math></p><p>So, given equation becomes <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math> </p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>5</mn><mo>;</mo><mo>&#160;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>Now if the roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>+</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></math></p><p>i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#945;</mi><mi>&#946;</mi><mo>+</mo><mn>1</mn></mrow><mi>&#946;</mi></mfrac><mo>&#38;</mo><mfrac><mrow><mi>&#945;</mi><mi>&#946;</mi><mo>+</mo><mn>1</mn></mrow><mi>&#945;</mi></mfrac></math> </p><p>i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mi>&#946;</mi></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mi>&#945;</mi></mfrac></math></p><p>Then let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mi>&#945;</mi></mfrac><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mi>t</mi></mfrac></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>&#945;</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mi>t</mi></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mn>5</mn><mfenced><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mi>t</mi></mfrac></mfenced><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>10</mn><mi>t</mi></mfrac><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>t</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p>i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> is the required equation.</p></blockquote>

</details>

---

### Q49. JEE Main 2022 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi></math> be two non-zero real numbers. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>a</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>a</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mi>b</mi><mi>x</mi><mo>+</mo><mn>6</mn><mi>b</mi><mo>=</mo><mn>0</mn></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>p</mi></mfrac><mo>,</mo><mfrac><mn>1</mn><mi>q</mi></mfrac><mo>,</mo><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><mo>&#160;</mo><mi>s</mi></mrow></mfrac></math> are in A.P., then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><msup><mi>b</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **38**

**Detailed Solution:**

<blockquote><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>,</mo><mo>&#160;</mo><mi>r</mi></math> are roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>a</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>a</mi><mo>=</mo><mn>0</mn></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>,</mo><mi>s</mi></math> are the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mi>b</mi><mi>x</mi><mo>+</mo><mn>6</mn><mi>b</mi><mo>=</mo><mn>0</mn></math> </p><p>So the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>a</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> has roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>p</mi></mfrac><mo>,</mo><mfrac><mn>1</mn><mi>r</mi></mfrac></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mi>b</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> has roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>q</mi></mfrac><mo>,</mo><mfrac><mn>1</mn><mi>s</mi></mfrac></math>.</p><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>p</mi></mfrac><mo>,</mo><mfrac><mn>1</mn><mi>q</mi></mfrac><mo>,</mo><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>,</mo><mfrac><mn>1</mn><mi>s</mi></mfrac></math> are in A.P.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>p</mi></mfrac><mo>=</mo><mi>&#945;</mi><mo>-</mo><mn>3</mn><mi>&#946;</mi><mo>,</mo><mfrac><mn>1</mn><mi>q</mi></mfrac><mo>=</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>,</mo><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>=</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>s</mi></mfrac><mo>=</mo><mi>&#945;</mi><mo>+</mo><mn>3</mn><mi>&#946;</mi></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>p</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>=</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>2</mn><mi>&#946;</mi><mo>=</mo><mn>4</mn></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>q</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>s</mi></mfrac><mo>=</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>p</mi></mfrac><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mi>q</mi></mfrac><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mi>s</mi></mfrac><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p>Now </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>p</mi></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>a</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>5</mn><mo>&#8658;</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>=</mo><mo>-</mo><mn>10</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>q</mi></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mi>s</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>6</mn><mi>b</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>8</mn><mo>&#8658;</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>=</mo><mo>-</mo><mn>48</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><msup><mi>b</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mo>-</mo><mn>10</mn><mo>+</mo><mn>48</mn><mo>=</mo><mn>38</mn></math></p></blockquote>

</details>

---

### Q50. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> be a root of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup><mo>=</mo><mn>0</mn></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>1011</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>2022</mn></msup><mo>-</mo><msup><mi>&#945;</mi><mn>3033</mn></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>&#945;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mi>&#945;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Using the formula <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>4</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><mi>&#969;</mi><mo>,</mo><mo>&#160;</mo><mo>&#177;</mo><msup><mi>&#969;</mi><mn>2</mn></msup></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><msup><mn>1</mn><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></math> and imaginary.</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>1011</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>2022</mn></msup><mo>-</mo><msup><mi>&#945;</mi><mn>3033</mn></msup><mo>=</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q51. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> be a quadratic polynomial such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>0</mn></math>. If one of the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>, then the sum of the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>12</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>14</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mn>9</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>13</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mn>2</mn><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math> is a root of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math>. So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>On solving equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>0</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfrac><mi>b</mi><mi>a</mi></mfrac><mo>=</mo><mfrac><mn>11</mn><mn>3</mn></mfrac></math></p><p>Now, we know that sum of the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mi>b</mi></mrow><mi>a</mi></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> The sum of the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>3</mn></mfrac></math>.</p>

</details>

---

### Q52. JEE Main 2022 (27 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>&#955;</mi><mi>x</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#947;</mi></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced><mi mathvariant="normal">x</mi><mo>+</mo><mn>7</mn><mo>+</mo><mn>3</mn><mi>&#955;</mi><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mn>2</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **98**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#946;</mi></math> are roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>&#955;</mi><mi>x</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>4</mn><mi>&#955;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mn>5</mn></math> .......(i)</p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#947;</mi></math> are roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced><mrow><mn>7</mn><mo>+</mo><mn>3</mn><mi>&#955;</mi><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#947;</mi><mo>=</mo><mn>7</mn><mo>+</mo><mn>3</mn><mi>&#955;</mi><msqrt><mn>3</mn></msqrt></math> .........(ii)</p><p>Given, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>&#160;&#160;</mo></math></p><p>So, from equation (i) and (ii) we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><msqrt><mn>3</mn></msqrt></math> and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>2</mn><mi>&#955;</mi><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>&#160;</mo></math>, Now by product of roots we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mo>=</mo><mn>5</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#946;</mi><mo>+</mo><mi>&#955;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mo>&#160;</mo><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#955;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>4</mn><mi>&#955;</mi><mo>+</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>7</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>98</mn></math></p>

</details>

---

### Q53. JEE Main 2022 (26 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> are real number such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><msup><mi>p</mi><mn>4</mn></msup><mo>+</mo><msup><mi>q</mi><mn>4</mn></msup><mo>=</mo><mn>369</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>1</mn><mi>p</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>q</mi></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mn>4</mn></msup><mo>+</mo><msup><mi>q</mi><mn>4</mn></msup><mo>=</mo><mn>369</mn><mo>&#8658;</mo><msup><mfenced><mrow><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mfenced><mrow><mi>p</mi><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>369</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msup><mfenced><mrow><mi>p</mi><mo>+</mo><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>p</mi><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mfenced><mrow><mi>p</mi><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>369</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>9</mn><mo>-</mo><mn>2</mn><mi>p</mi><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mfenced><mrow><mi>p</mi><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>369</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>p</mi><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>18</mn><mfenced><mrow><mi>p</mi><mi>q</mi></mrow></mfenced><mo>-</mo><mn>144</mn><mo>=</mo><mn>0</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mi>q</mi><mo>=</mo><mn>24</mn><mo>(</mo><mtext>rejected</mtext><mo>)</mo><mo>,</mo><mo>-</mo><mn>6</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>1</mn><mi>p</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>q</mi></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>=</mo><mfrac><msup><mfenced><mrow><mi>p</mi><mi>q</mi></mrow></mfenced><mn>2</mn></msup><msup><mfenced><mrow><mi>p</mi><mo>+</mo><mi>q</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><msup><mfenced><mrow><mi>p</mi><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mn>9</mn></mfrac><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q54. JEE Main 2022 (25 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

For a natural number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mi>n</mi></msub><mo>=</mo><msup><mn>19</mn><mi>n</mi></msup><mo>-</mo><msup><mn>12</mn><mi>n</mi></msup></math>. Then, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>31</mn><msub><mi>&#945;</mi><mn>9</mn></msub><mo>-</mo><msub><mi>&#945;</mi><mn>10</mn></msub></mrow><mrow><mn>57</mn><msub><mi>&#945;</mi><mn>8</mn></msub></mrow></mfrac></math> is ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>2</mn></msub></math> are roots of the quadratic <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><msub><mi>r</mi><mn>1</mn></msub><mi>n</mi></msup><mo>=</mo><mn>31</mn><msup><msub><mi>r</mi><mn>1</mn></msub><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>228</mn><msup><msub><mi>r</mi><mn>1</mn></msub><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><msub><mi>r</mi><mn>2</mn></msub><mi>n</mi></msup><mo>=</mo><mn>31</mn><msup><msub><mi>r</mi><mn>2</mn></msub><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>228</mn><msup><msub><mi>r</mi><mn>2</mn></msub><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><msub><mi>r</mi><mn>1</mn></msub><mi>n</mi></msup><mo>-</mo><msup><msub><mi>r</mi><mn>2</mn></msub><mi>n</mi></msup><mo>=</mo><mn>31</mn><mfenced><mrow><msup><msub><mi>r</mi><mn>1</mn></msub><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><msup><msub><mi>r</mi><mn>2</mn></msub><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mo>-</mo><mn>228</mn><mfenced><mrow><msup><msub><mi>r</mi><mn>1</mn></msub><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><msup><msub><mi>r</mi><mn>2</mn></msub><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p>Or <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>-</mo><mn>31</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><mn>228</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msup><msub><mi>r</mi><mn>1</mn></msub><mi>n</mi></msup><mo>-</mo><msup><msub><mi>r</mi><mn>2</mn></msub><mi>n</mi></msup></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>12</mn></math> are the roots of the quadratic <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>31</mn><mi>x</mi><mo>+</mo><mn>228</mn><mo>=</mo><mn>0</mn></math> </p><p>we know, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>-</mo><mn>31</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><mn>228</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math></p><p>Now, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>10</mn><mo>,</mo><mo>&#160;&#160;</mo><msub><mi>&#945;</mi><mn>10</mn></msub><mo>-</mo><mn>31</mn><msub><mi>&#945;</mi><mn>3</mn></msub><mo>+</mo><mn>228</mn><msub><mi>&#945;</mi><mn>8</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>31</mn><msub><mi>&#945;</mi><mn>9</mn></msub><mo>-</mo><msub><mi>&#945;</mi><mn>10</mn></msub></mrow><mrow><mn>57</mn><msub><mi>&#945;</mi><mn>8</mn></msub></mrow></mfrac><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q55. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the sum of the squares of the reciprocals of the roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>&#955;</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msup><mfenced><mrow><msup><mi>&#945;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>3</mn></msup></mrow></mfenced><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>46</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>15</mn></math></p><p>For equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>&#955;</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>&#955;</mi></mrow><mn>3</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math></p><p>then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#945;</mi><mi>&#946;</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mi>&#955;</mi><mn>2</mn></msup><mn>9</mn></mfrac><mo>-</mo><mn>2</mn><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><msup><mi>&#955;</mi><mn>2</mn></msup><mn>9</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></mrow><mn>9</mn></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>15</mn><mo>&#8658;</mo><mfrac><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mrow><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></mrow><mn>9</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>15</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></mrow><mn>9</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>9</mn></mfrac></mstyle></mfrac><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mo>=</mo><mn>15</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>&#177;</mo><mn>3</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msup><mfenced><mrow><msup><mi>&#945;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>3</mn></msup></mrow></mfenced><mn>2</mn></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><msup><mfenced><mrow><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><msup><mfenced><mrow><mfrac><mn>15</mn><mn>9</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><msup><mfenced><mn>2</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>24</mn></math></p>

</details>

---

### Q56. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of pairs <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> of real numbers, such that whenever <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is a root of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></math> is also a root of this equation, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

<p>Consider the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p>It has two roots (not necessarily real <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math>)</p><p>Either <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mi>&#946;</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8800;</mo><mi>&#946;</mi></math></p><p><strong>Case (1)</strong> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mi>&#946;</mi></math>, then it is repeated root. Given than <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></math> is also root</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p><strong>Case (2)</strong> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8800;</mo><mi>&#946;</mi></math>, then four possibilities are there</p><p><strong>(I)</strong> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mo>-</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>,</mo><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><strong>(II)</strong> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></math></p><p>Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mi>&#945;</mi></mrow></mfenced></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8800;</mo><mi>&#946;</mi></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#945;</mi><mi>&#946;</mi><mo>-</mo><mn>4</mn></math></p><p>Thus <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>&#945;</mi><mi>&#946;</mi><mo>-</mo><mn>4</mn></math> which implies</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>. Therefore <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mo>-</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>,</mo><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><strong>(III)</strong> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>=</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8800;</mo><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mi>&#946;</mi></math></p><p>Thus <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn></math></p><p>Therefore <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><strong>(IV)</strong> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>=</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8800;</mo><mi>&#946;</mi></math> is same as (III)</p><p>Therefore we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> pairs of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math></p><p>Which are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q57. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#62;</mo><mo>-</mo><mn>1</mn></math>, for which the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mo>(</mo><mi>k</mi><mo>+</mo><mn>1</mn><mo>)</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><msup><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math> has real roots, is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mn>1</mn><mo>,</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mo>{</mo><mn>1</mn><mo>}</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mn>1</mn><mo>,</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mi>t</mi></mfenced><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>k</mi><msup><mfenced><mi>t</mi></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>1</mn><mo>-</mo><mo>(</mo><mi>k</mi><mo>+</mo><mn>1</mn><mo>)</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mo>(</mo><mi>k</mi><mo>+</mo><mn>1</mn><mo>)</mo><mi>t</mi><mo>+</mo><mi>k</mi><msup><mi>t</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>1</mn><mo>-</mo><mi>k</mi><mi>t</mi><mo>-</mo><mi>t</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>t</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Replacing the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> again</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mfenced><mfrac><mrow><mn>2</mn><mi>k</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p>For real roots, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>16</mn><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mfenced><mfrac><mrow><mn>2</mn><mi>k</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>6</mn><mi>k</mi><mo>-</mo><mn>9</mn></mrow><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mn>4</mn><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mfenced><mrow><mn>2</mn><mi>k</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac><mo>&#8804;</mo><mn>0</mn><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>&#8712;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>]</mo></math></p><p> </p></blockquote>

</details>

---

### Q58. JEE Main 2021 (26 Aug Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8800;</mo><mn>0</mn></math> be in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>27</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#946;</mi><mi>&#947;</mi></mrow><mi>&#955;</mi></mfrac></math> is equal to ________.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mn>2</mn><mi>&#955;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>iii</mi></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#947;</mi><mo>=</mo><mn>9</mn><mi>&#955;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>iv</mi></mfenced></math>
from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>iv</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#947;</mi><mi>&#946;</mi></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">v</mi></mfenced></math></p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>iii</mi></mfenced><mo>-</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mn>7</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>vi</mi></mfenced></math></p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">v</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>vi</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>,</mo><mi>&#947;</mi><mo>=</mo><mn>3</mn></math>
from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced><mo>&#160;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math>
So <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#946;</mi><mi>&#947;</mi></mrow><mi>&#955;</mi></mfrac><mo>=</mo><mfrac><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mn>3</mn></mrow><mfrac><mn>1</mn><mn>9</mn></mfrac></mfrac><mo>=</mo><mn>18</mn></math></p>

</details>

---

### Q59. JEE Main 2021 (26 Aug Shift 1)

*Type:* `numerical` | *Level:* `1`

The sum of all integral values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>(</mo><mi>k</mi><mo>&#8800;</mo><mn>0</mn><mo>)</mo></math> for which the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mi>k</mi></mfrac></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> has no real roots, is_____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **66**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mi>k</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mi>k</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mi>k</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mi>x</mi><mo>-</mo><mn>3</mn><mi>k</mi><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mo>(</mo><mn>6</mn><mo>+</mo><mi>k</mi><mo>)</mo><mi>x</mi><mo>+</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p> For no real roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#60;</mo><mn>0</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>6</mn><mo>+</mo><mi>k</mi><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>8</mn><mo>(</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>4</mn><mo>)</mo><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mi>k</mi><mo>+</mo><mn>36</mn><mo>-</mo><mn>24</mn><mi>k</mi><mo>-</mo><mn>32</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>6</mn><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>32</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>k</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mo>&#60;</mo><msqrt><mn>32</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mo>-</mo><msqrt><mn>32</mn></msqrt><mo>&#60;</mo><mi>k</mi><mo>&#60;</mo><mn>6</mn><mo>+</mo><msqrt><mn>32</mn></msqrt></math></p><p>Integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>11</mn></math></p><p>Sum<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>11</mn><mo>&#215;</mo><mn>12</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>66</mn></math></p>

</details>

---

### Q60. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><munder><mi>max</mi><mrow><mi>x</mi><mo>&#8712;</mo><mi>R</mi></mrow></munder><mfenced open="{" close="}"><mrow><msup><mn>8</mn><mrow><mn>2</mn><mi>sin</mi><mn>3</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><msup><mn>4</mn><mrow><mn>4</mn><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></msup></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><munder><mi>min</mi><mrow><mi>x</mi><mo>&#8712;</mo><mi>R</mi></mrow></munder><mfenced open="{" close="}"><mrow><msup><mn>8</mn><mrow><mn>2</mn><mi>sin</mi><mn>3</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><msup><mn>4</mn><mrow><mn>4</mn><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></msup></mrow></mfenced><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> is a quadratic equation whose roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mrow><mn>1</mn><mo>/</mo><mn>5</mn></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mrow><mn>1</mn><mo>/</mo><mn>5</mn></mrow></msup><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>-</mo><mi>b</mi></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>42</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>47</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>43</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>42</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mi>max</mi><mfenced close="}" open="{"><mrow><msup><mn>8</mn><mrow><mn>2</mn><mi>sin</mi><mn>3</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><msup><mn>4</mn><mrow><mn>4</mn><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>max</mi><mfenced close="}" open="{"><mrow><msup><mn>2</mn><mrow><mn>6</mn><mi>sin</mi><mn>3</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><msup><mn>2</mn><mrow><mn>8</mn><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>max</mi><mfenced close="}" open="{"><msup><mn>2</mn><mrow><mn>6</mn><mi>sin</mi><mn>3</mn><mi>x</mi><mo>+</mo><mn>8</mn><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></msup></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mi>min</mi><mfenced close="}" open="{"><mrow><msup><mn>8</mn><mrow><mn>2</mn><mi>sin</mi><mn>3</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><msup><mn>4</mn><mrow><mn>4</mn><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></msup></mrow></mfenced><mo>=</mo><mi>min</mi><mfenced close="}" open="{"><msup><mn>2</mn><mrow><mn>6</mn><mi>sin</mi><mn>3</mn><mi>x</mi><mo>+</mo><mn>8</mn><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></msup></mfenced></math></p><p>Now range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>sin</mi><mn>3</mn><mi>x</mi><mo>+</mo><mn>8</mn><mi>cos</mi><mn>3</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><mo>-</mo><msqrt><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><msup><mn>8</mn><mn>2</mn></msup></msqrt><mo>,</mo><mo>+</mo><msqrt><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><msup><mn>8</mn><mn>2</mn></msup></msqrt></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>10</mn><mo>,</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><msup><mn>2</mn><mn>10</mn></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><msup><mn>2</mn><mrow><mo>-</mo><mn>10</mn></mrow></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mrow><mn>1</mn><mo>/</mo><mn>5</mn></mrow></msup><mo>=</mo><msup><mn>2</mn><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#946;</mi><mrow><mn>1</mn><mo>/</mo><mn>5</mn></mrow></msup><mo>=</mo><msup><mn>2</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p>The quadratic <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>,</mo></math></p><p>sum of roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mi>b</mi></mrow><mn>8</mn></mfrac></math> and product of roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>c</mi><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>c</mi><mo>-</mo><mi>b</mi><mo>=</mo><mn>8</mn><mo>&#215;</mo><mo>[</mo></math> (product of roots<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo><mo>+</mo><mo>(</mo></math>sum of roots<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo><mo>]</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mo>&#215;</mo><mfenced close="]" open="["><mrow><mn>4</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mn>4</mn><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mn>8</mn><mo>&#215;</mo><mfenced close="]" open="["><mfrac><mn>21</mn><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>42</mn></math></p>

</details>

---

### Q61. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> be two roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>20</mn></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup><mi>x</mi><mo>+</mo><msup><mfenced><mn>5</mn></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>8</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>8</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>160</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>**

**Detailed Solution:**

<p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>20</mn></mfenced><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup><mi>x</mi><mo>+</mo><msup><mfenced><mn>5</mn></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced><msqrt><mn>5</mn></msqrt></mfenced><mo>=</mo><mo>-</mo><mi>x</mi><msup><mfenced><mn>20</mn></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msqrt><mn>20</mn></msqrt><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>5</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#215;</mo><msqrt><mn>5</mn></msqrt><mo>=</mo><msqrt><mn>20</mn></msqrt><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>4</mn></msup><mo>=</mo><mo>-</mo><mn>5</mn><mo>&#8658;</mo><msup><mi>x</mi><mn>8</mn></msup><mo>=</mo><mn>25</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>8</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>8</mn></msup><mo>=</mo><mn>25</mn><mo>+</mo><mn>25</mn><mo>=</mo><mn>50</mn></math></p>

</details>

---

### Q62. JEE Main 2021 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>a</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mo>=</mo><mn>3</mn><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>4</mn></msup><mo>+</mo><msup><mi>b</mi><mn>4</mn></msup><mo>+</mo><msup><mi>c</mi><mn>4</mn></msup></math> is equal to:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **13**

**Detailed Solution:**

We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>a</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mo>=</mo><mn>3</mn></math><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#931;</mi><mi>a</mi><mi>b</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>a</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mi>&#931;</mi><msup><mfenced><mrow><mi>a</mi><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>a</mi><mi>b</mi><mi>c</mi><mi>&#931;</mi><mi mathvariant="normal">a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#931;</mi><msup><mfenced><mrow><mi>a</mi><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>4</mn></msup><mo>+</mo><msup><mi>b</mi><mn>4</mn></msup><mo>+</mo><msup><mi>c</mi><mn>4</mn></msup><mo>=</mo><msup><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#931;</mi><msup><mfenced><mrow><mi>a</mi><mi>b</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>-</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>13</mn><mo>.</mo></math></p>

</details>

---

### Q63. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of real solutions of the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>-</mo><mn>12</mn><mo>=</mo><mn>0</mn></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mi>x</mi></mfenced><mn>2</mn></msup><mo>-</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>-</mo><mn>12</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mi>x</mi></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mn>3</mn><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>-</mo><mn>12</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mn>4</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>&#8800;</mo><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><mn>2</mn></math></p><p>Hence, number of real solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo></math></p>

</details>

---

### Q64. JEE Main 2021 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> are roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mi>x</mi><mo>+</mo><mn>10</mn><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#945;</mi><mo>&#62;</mo><mi>&#946;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mi>n</mi></msub><mo>=</mo><msup><mi>&#945;</mi><mi>n</mi></msup><mo>-</mo><msup><mi>&#946;</mi><mi>n</mi></msup></math> for each positive integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><msub><mi>P</mi><mn>17</mn></msub><msub><mi>P</mi><mn>20</mn></msub><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><msub><mi>P</mi><mn>17</mn></msub><msub><mi>P</mi><mn>19</mn></msub></mrow><mrow><msub><mi>P</mi><mn>18</mn></msub><msub><mi>P</mi><mn>19</mn></msub><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><msubsup><mi>P</mi><mn>18</mn><mn>2</mn></msubsup></mrow></mfrac></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><mi>x</mi><mo>+</mo><mn>10</mn><mo>=</mo><mn>0</mn></math></p><p>and  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mi>n</mi></msub><mo>=</mo><msup><mi>&#945;</mi><mi>n</mi></msup><mo>-</mo><msup><mi>&#946;</mi><mi>n</mi></msup></math> </p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>P</mi><mn>17</mn></msub><msub><mi>P</mi><mn>20</mn></msub><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><msub><mi>P</mi><mn>17</mn></msub><msub><mi>P</mi><mn>19</mn></msub></mrow><mrow><msub><mi>P</mi><mn>18</mn></msub><msub><mi>P</mi><mn>19</mn></msub><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><msubsup><mi>P</mi><mn>18</mn><mn>2</mn></msubsup></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mi>P</mi><mn>17</mn></msub><mfenced><mrow><msub><mi>P</mi><mn>20</mn></msub><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><msub><mi>P</mi><mn>19</mn></msub></mrow></mfenced></mrow><mrow><msub><mi>P</mi><mn>18</mn></msub><mfenced><mrow><msub><mi>P</mi><mn>19</mn></msub><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><msub><mi>P</mi><mn>18</mn></msub></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msub><mi>P</mi><mn>17</mn></msub><mfenced><mrow><msup><mi>&#945;</mi><mn>20</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>20</mn></msup><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><mfenced><mrow><msup><mi>&#945;</mi><mn>19</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>19</mn></msup></mrow></mfenced></mrow></mfenced></mrow><mrow><msub><mi>P</mi><mn>18</mn></msub><mfenced><mrow><msup><mi>&#945;</mi><mn>19</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>19</mn></msup><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><mfenced><mrow><msup><mi>&#945;</mi><mn>18</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>18</mn></msup></mrow></mfenced></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msub><mi>P</mi><mn>17</mn></msub><mfenced><mrow><msup><mi>&#945;</mi><mn>19</mn></msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>-</mo><msup><mi>&#946;</mi><mn>19</mn></msup><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow></mfenced></mrow><mrow><msub><mi>P</mi><mn>18</mn></msub><mfenced><mrow><msup><mi>&#945;</mi><mn>18</mn></msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>-</mo><msup><mi>&#946;</mi><mn>18</mn></msup><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow></mfenced></mrow></mfrac></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><mo>=</mo><mo>-</mo><mn>10</mn><mo>/</mo><mi>&#945;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#38;</mo><mo>&#160;</mo><mi>&#946;</mi><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><mo>=</mo><mo>-</mo><mn>10</mn><mo>/</mo><mi>&#946;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now put these values in above expression</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>P</mi><mn>17</mn></msub><mfenced><mrow><msup><mi>&#945;</mi><mn>19</mn></msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>-</mo><msup><mi>&#946;</mi><mn>19</mn></msup><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow></mfenced></mrow><mrow><msub><mi>P</mi><mn>18</mn></msub><mfenced><mrow><msup><mi>&#945;</mi><mn>18</mn></msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>-</mo><msup><mi>&#946;</mi><mn>18</mn></msup><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>10</mn><msub><mi>P</mi><mn>17</mn></msub><msub><mi>P</mi><mn>18</mn></msub></mrow><mrow><mo>-</mo><mn>10</mn><msub><mi>P</mi><mn>18</mn></msub><msub><mi>P</mi><mn>17</mn></msub></mrow></mfrac><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q65. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are the distinct roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>3</mn></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mi>x</mi><mo>+</mo><msup><mn>3</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>=</mo><mn>0</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>96</mn></msup><mfenced><mrow><msup><mi>&#945;</mi><mn>12</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msup><mi>&#946;</mi><mn>96</mn></msup><mfenced><mrow><msup><mi>&#946;</mi><mn>12</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>56</mn><mo>&#215;</mo><msup><mn>3</mn><mn>25</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>56</mn><mo>&#215;</mo><msup><mn>3</mn><mn>24</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn><mo>&#215;</mo><msup><mn>3</mn><mn>24</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn><mo>&#215;</mo><msup><mn>3</mn><mn>25</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn><mo>&#215;</mo><msup><mn>3</mn><mn>24</mn></msup></math>**

**Detailed Solution:**

We have,<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>3</mn></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mi>x</mi><mo>+</mo><msup><mn>3</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>=</mo><mn>0</mn></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is the root, therefore <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>=</mo><mo>-</mo><msup><mfenced><mn>3</mn></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>&#183;</mo><mi>&#945;</mi></math></p><p>On squaring, both sides we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>&#945;</mi><mn>4</mn></msup><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt><msup><mi>&#945;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><mo>=</mo><mo>-</mo><msqrt><mn>3</mn></msqrt><msup><mi>&#945;</mi><mn>2</mn></msup></math></p><p>On squaring, both sides we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>8</mn></msup><mo>+</mo><mn>6</mn><msup><mi>&#945;</mi><mn>4</mn></msup><mo>+</mo><mn>9</mn><mo>=</mo><mn>3</mn><msup><mi>&#945;</mi><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>8</mn></msup><mo>=</mo><mo>-</mo><mn>9</mn><mo>-</mo><mn>3</mn><msup><mi>&#945;</mi><mn>4</mn></msup></math></p><p>Multiply by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>4</mn></msup></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>12</mn></msup><mo>=</mo><mo>-</mo><mn>9</mn><msup><mi>&#945;</mi><mn>4</mn></msup><mo>-</mo><mn>3</mn><msup><mi>&#945;</mi><mn>8</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>&#945;</mi><mn>12</mn></msup><mo>=</mo><mo>-</mo><mn>9</mn><msup><mi>&#945;</mi><mn>4</mn></msup><mo>-</mo><mn>3</mn><mfenced><mrow><mo>-</mo><mn>9</mn><mo>-</mo><mn>3</mn><msup><mi>&#945;</mi><mn>4</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>12</mn></msup><mo>=</mo><mn>27</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><msup><mi>&#945;</mi><mn>12</mn></msup></mfenced><mn>8</mn></msup><mo>=</mo><msup><mfenced><mn>27</mn></mfenced><mn>8</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>96</mn></msup><mo>=</mo><msup><mfenced><mn>3</mn></mfenced><mn>24</mn></msup></math></p><p>Similarly,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mn>96</mn></msup><mo>=</mo><msup><mfenced><mn>3</mn></mfenced><mn>24</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>&#945;</mi><mn>96</mn></msup><mfenced><mrow><msup><mi>&#945;</mi><mn>12</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msup><mi>&#946;</mi><mn>96</mn></msup><mfenced><mrow><msup><mi>&#946;</mi><mn>12</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfenced><mn>3</mn></mfenced><mrow><msup><mrow/><mn>24</mn></msup><mo>+</mo><mfenced><mrow><mn>27</mn><mo>+</mo><mn>27</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><msup><mfenced><mn>3</mn></mfenced><mn>24</mn></msup></mrow><mo>&#215;</mo><mn>52</mn></math>
 </p>

</details>

---

### Q66. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>+</mo><mo>&#8230;</mo><mo>&#8734;</mo></mrow></mfrac></mrow></mfrac></mrow></mfrac></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>+</mo><mo>&#8230;</mo><mo>&#8734;</mo></mrow></mfrac></mrow></mfrac></mrow></mfrac></mrow></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfrac><mo>=</mo><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><mfrac><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mi>x</mi></mfrac></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mfrac><mi>x</mi><mrow><mo>(</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>12</mn><mo>&#177;</mo><msqrt><mo>(</mo><mn>12</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>12</mn><mo>&#215;</mo><mn>4</mn></msqrt></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>12</mn><mo>&#177;</mo><msqrt><mn>12</mn><mo>(</mo><mn>16</mn><mo>)</mo></msqrt></mrow><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>12</mn><mo>&#177;</mo><mn>4</mn><mo>&#215;</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>8</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#177;</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#177;</mo><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#177;</mo><msqrt><mn>3</mn></msqrt><mo>.</mo></math></p><p>But only positive value is accepted</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>5</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math></p>

</details>

---

### Q67. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8734;</mo></mrow></mfrac></mrow></mfrac></mrow></mfrac></mrow></mfrac></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msqrt><mn>30</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><mfrac><mn>4</mn><msqrt><mn>5</mn></msqrt></mfrac><msqrt><mn>30</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>+</mo><mfrac><mn>4</mn><msqrt><mn>5</mn></msqrt></mfrac><msqrt><mn>30</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msqrt><mn>30</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msqrt><mn>30</mn></msqrt></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>4</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>+</mo><munder><munder><mfrac><mn>1</mn><mrow><mn>4</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8734;</mo></mrow></mfrac></mrow></mfrac></mrow></mfrac><mo>&#9183;</mo></munder><mi>y</mi></munder></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>4</mn><mo>+</mo><mfrac><mn>1</mn><mfenced><mrow><mn>5</mn><mo>+</mo><mfrac><mn>1</mn><mi>y</mi></mfrac></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>-</mo><mn>4</mn><mo>=</mo><mfrac><mi>y</mi><mrow><mo>(</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>20</mn><mi>y</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>20</mn><mo>&#177;</mo><msqrt><msup><mfenced><mrow><mo>-</mo><mn>20</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#183;</mo><mn>5</mn><mo>&#183;</mo><mfenced><mrow><mo>-</mo><mn>4</mn></mrow></mfenced></msqrt></mrow><mrow><mn>2</mn><mo>&#183;</mo><mn>5</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>20</mn><mo>&#177;</mo><msqrt><mn>480</mn></msqrt></mrow><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>2</mn><mo>-</mo><msqrt><mfrac><mn>480</mn><mn>100</mn></mfrac></msqrt></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo></math>rejected</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mo>+</mo><msqrt><mfrac><mn>480</mn><mn>100</mn></mfrac></msqrt><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msqrt><mn>30</mn></msqrt></math></p><p>Correct with Option (A).</p>

</details>

---

### Q68. JEE Main 2021 (26 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> be two real numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>p</mi><mi>n</mi></msub><mo>=</mo><msup><mfenced><mi>&#945;</mi></mfenced><mi>n</mi></msup><mo>+</mo><msup><mfenced><mi>&#946;</mi></mfenced><mi>n</mi></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>p</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>11</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>p</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>29</mn></math> for some integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#10878;</mo><mn>1</mn></math>. Then, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>p</mi><mi>n</mi><mn>2</mn></msubsup></math> is______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **324**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="bottom"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>&#945;</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mi>&#945;</mi><mi>n</mi></msup><mo>+</mo><msup><mi>&#945;</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mspace linebreak="newline"></mspace><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mi>&#946;</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>&#946;</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mi>&#946;</mi><mi>n</mi></msup><mo>+</mo><msup><mi>&#946;</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mspace linebreak="newline"></mspace><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>+</mo></menclose><mspace linebreak="newline"></mspace><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi>p</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msub><mi>p</mi><mi>n</mi></msub><mo>+</mo><msub><mi>p</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>29</mn><mo>=</mo><msub><mi>p</mi><mi>n</mi></msub><mo>+</mo><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>p</mi><mi>n</mi></msub><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>p</mi><mi>n</mi><mn>2</mn></msubsup><mo>=</mo><mn>324</mn></math></p>

</details>

---

### Q69. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi>R</mi></math> are such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mn>2</mn><mi>i</mi></math> (here <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>i</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>1</mn></math>) is a root of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>&#8658;</mo></math> other root is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo></math>( sum of roots )<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi mathvariant="normal">i</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi mathvariant="normal">i</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo></math>product of roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>i</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi></mrow></mfenced><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>7</mn></math></p><p>option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p>

</details>

---

### Q70. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> be the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msup><mi>&#945;</mi><mi>n</mi></msup><mo>-</mo><msup><mi>&#946;</mi><mi>n</mi></msup></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#10878;</mo><mn>1</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>a</mi><mn>10</mn></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mn>8</mn></msub></mrow><mrow><mn>3</mn><msub><mi>a</mi><mn>9</mn></msub></mrow></mfrac></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>&#945;</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><msup><mi>&#945;</mi><mn>10</mn></msup><mo>-</mo><mn>6</mn><msup><mi>&#945;</mi><mn>9</mn></msup><mo>-</mo><mn>2</mn><msup><mi>&#945;</mi><mn>8</mn></msup><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><menclose notation="bottom"><msup><mi>&#946;</mi><mn>10</mn></msup><mo>-</mo><mn>6</mn><msup><mi>&#946;</mi><mn>9</mn></msup><mo>-</mo><mn>2</mn><msup><mi>&#946;</mi><mn>8</mn></msup><mo>=</mo><mn>0</mn></menclose></mtd></mtr><mtr><mtd><mfenced><mrow><msup><mi>&#945;</mi><mn>10</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>10</mn></msup></mrow></mfenced><mo>-</mo><mn>6</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>9</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>9</mn></msup></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>8</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>8</mn></msup></mrow></mfenced><mo>=</mo><mn>0</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>10</mn></msub><mo>-</mo><mn>6</mn><msub><mi>a</mi><mn>9</mn></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mn>8</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msub><mi>a</mi><mn>10</mn></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mn>8</mn></msub></mrow><mrow><mn>3</mn><msub><mi>a</mi><mn>9</mn></msub></mrow></mfrac><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q71. JEE Main 2021 (24 Feb Shift 2)

*Type:* `numerical` | *Level:* `1`

The number of the real roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>|</mo><mi>x</mi><mo>-</mo><mn>5</mn><mo>|</mo><mo>=</mo><mfrac><mn>27</mn><mn>4</mn></mfrac></math> is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Case-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8804;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mfrac><mn>27</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p>Case-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mfrac><mn>27</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfrac><mn>51</mn><mn>4</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>52</mn></msqrt></mrow><mn>2</mn></mfrac></math> (rejected as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>5</mn></math>)</p><p>So, the equation have two real root.</p>

</details>

---

### Q72. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> be two positive numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mn>4</mn></msup><mo>+</mo><msup><mi>q</mi><mn>4</mn></msup><mo>=</mo><mn>272</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> are roots of the equation:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>136</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>16</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>16</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

Consider <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>p</mi><mn>2</mn></msup><msup><mi>q</mi><mn>2</mn></msup><mo>=</mo><mn>272</mn></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mfenced><mrow><mi>p</mi><mo>+</mo><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>p</mi><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>p</mi><mn>2</mn></msup><msup><mi>q</mi><mn>2</mn></msup><mo>=</mo><mn>272</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>-</mo><mn>16</mn><mi>p</mi><mi>q</mi><mo>+</mo><mn>2</mn><msup><mi>p</mi><mn>2</mn></msup><msup><mi>q</mi><mn>2</mn></msup><mo>=</mo><mn>272</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>p</mi><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>p</mi><mi>q</mi><mo>-</mo><mn>128</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>p</mi><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>p</mi><mi>q</mi><mo>-</mo><mn>128</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mi>q</mi><mo>=</mo><mfrac><mrow><mn>8</mn><mo>&#177;</mo><mn>24</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>16</mn><mo>,</mo><mo>-</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mi>p</mi><mi>q</mi><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo></math>Required equation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>:</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mn>2</mn></mfenced><mi>x</mi><mo>+</mo><mn>16</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q73. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#946;</mi></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">x</mi><mfenced><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#946;</mi></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">&#945;</mi><mfenced><mrow><mi mathvariant="normal">&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi mathvariant="normal">&#945;</mi><mfenced><mrow><mi mathvariant="normal">&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">&#945;</mi><mfenced><mrow><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi mathvariant="normal">&#945;</mi><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi mathvariant="normal">&#945;</mi><mfenced><mrow><mi mathvariant="normal">&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> .........(1)</p><p>roots of equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p>are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mi>&#945;</mi></math>   ........(2)</p><p>and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>&#945;</mi><mn>2</mn></mfrac></math> .........(3)</p><p>now</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>&#945;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mi>&#945;</mi><mo>=</mo><mi>&#946;</mi></math></p>

</details>

---

### Q74. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> be two roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>64</mn><mi>x</mi><mo>+</mo><mn>256</mn><mo>=</mo><mn>0</mn><mo>.</mo></math> Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><msup><mi>&#945;</mi><mn>3</mn></msup><msup><mi>&#946;</mi><mn>5</mn></msup></mfrac></mfenced><mfrac><mn>1</mn><mn>8</mn></mfrac></msup><mo>+</mo><msup><mfenced><mfrac><msup><mi>&#946;</mi><mn>3</mn></msup><msup><mi>&#945;</mi><mn>5</mn></msup></mfrac></mfenced><mfrac><mn>1</mn><mn>8</mn></mfrac></msup></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Given equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>64</mn><mi>x</mi><mo>+</mo><mn>256</mn><mo>=</mo><mn>0</mn></math> whose roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>64</mn><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mn>256</mn></math>
Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><msup><mi>&#945;</mi><mn>3</mn></msup><msup><mi>&#946;</mi><mn>5</mn></msup></mfrac></mfenced><mfrac><mn>1</mn><mn>8</mn></mfrac></msup><mo>+</mo><msup><mfenced><mfrac><msup><mi>&#946;</mi><mn>3</mn></msup><msup><mi>&#945;</mi><mn>5</mn></msup></mfrac></mfenced><mfrac><mn>1</mn><mn>8</mn></mfrac></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mi>&#945;</mi><mrow><mfrac><mn>3</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>8</mn></mfrac></mrow></msup><mo>+</mo><msup><mi>&#946;</mi><mrow><mfrac><mn>3</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>8</mn></mfrac></mrow></msup></mrow><mrow><mo>(</mo><mi>&#945;</mi><mi>&#946;</mi><msup><mo>)</mo><mrow><mn>5</mn><mo>/</mo><mn>8</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow><mrow><mo>(</mo><mi>&#945;</mi><mi>&#946;</mi><msup><mo>)</mo><mrow><mn>5</mn><mo>/</mo><mn>8</mn></mrow></msup></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>64</mn><mrow><mo>(</mo><mn>256</mn><msup><mo>)</mo><mrow><mn>5</mn><mo>/</mo><mn>8</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mn>64</mn><mn>32</mn></mfrac><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q75. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are the roots of the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>,</mo></math> then the value of<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mrow><mn>1</mn><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mi>&#946;</mi><mrow><mn>1</mn><mo>-</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfrac></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>27</mn><mn>32</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>24</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>27</mn><mn>16</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>27</mn><mn>16</mn></mfrac></math>**

**Detailed Solution:**

Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are the roots of the equation,<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>,</mo></math> then <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mo>&#160;</mo><mo>;</mo><mo>&#160;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>7</mn></mfrac></math></p><p>Now </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mrow><mn>1</mn><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mi>&#946;</mi><mrow><mn>1</mn><mo>-</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo></mrow><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo></mrow><mrow><mn>1</mn><mo>+</mo><mo>(</mo><mi>&#945;</mi><mi>&#946;</mi><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo></mrow><mrow><mn>1</mn><mo>+</mo><mo>(</mo><mi>&#945;</mi><mi>&#946;</mi><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>&#945;</mi><mi>&#946;</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mfrac><mn>3</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>7</mn></mfrac><mfenced><mfrac><mn>3</mn><mn>7</mn></mfrac></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mfenced><mfrac><mn>2</mn><mn>7</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mfrac><mn>3</mn><mn>7</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mfrac><mn>2</mn><mn>7</mn></mfrac></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>27</mn><mn>16</mn></mfrac></math></p>

</details>

---

### Q76. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The product of the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>18</mn><mo>|</mo><mi>x</mi><mo>|</mo><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>81</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>27</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>9</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>81</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#8757;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mo>|</mo><mi>x</mi><msup><mo>|</mo><mn>2</mn></msup></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msup><mfenced open="|" close="|"><mi>x</mi></mfenced><mn>2</mn></msup><mo>-</mo><mn>18</mn><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>3</mn><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>3</mn><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>-</mo><mn>5</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>x</mi><mo>|</mo><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mn>3</mn></mfrac></math></p><p>product of roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mfenced><mfrac><mn>5</mn><mn>3</mn></mfrac></mfenced><mfenced><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>25</mn><mn>81</mn></mfrac></math></p>

</details>

---

### Q77. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> be the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>p</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#948;</mi></math> be the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>0</mn><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi><mo>,</mo><mi>&#948;</mi></math> from a geometric progression. Then ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi>q</mi><mo>+</mo><mi>p</mi><mo>)</mo><mo>:</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi>q</mi><mo>-</mo><mi>p</mi><mo>)</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>:</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>:</mo><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>:</mo><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn><mo>:</mo><mn>31</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>:</mo><mn>7</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mi>a</mi><mo>,</mo><mtext>&#8201;</mtext><mi>&#946;</mi><mo>=</mo><mi>a</mi><mi>r</mi><mo>,</mo><mtext>&#8201;</mtext><mi>&#947;</mi><mo>=</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>,</mo><mtext>&#8201;</mtext><mi>&#948;</mi><mo>=</mo><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>3</mn><mtext>&#8201;&#8201;</mtext><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>a</mi><mi>r</mi><mo>=</mo><mn>3</mn></math>  ...........<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi><mo>+</mo><mi>&#948;</mi><mo>=</mo><mn>6</mn><mtext>&#8201;</mtext><mo>&#8658;</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mn>6</mn></math>   .........<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p>By <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;</mtext><mfrac><mrow><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>r</mi></mrow></mfenced></mrow><mrow><mi>a</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>r</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>6</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;</mtext><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>q</mi><mo>+</mo><mi>p</mi></mrow><mrow><mn>2</mn><mi>q</mi><mo>&#8722;</mo><mi>p</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#947;</mi><mi>&#948;</mi><mo>+</mo><mi>&#945;</mi><mi>&#946;</mi></mrow><mrow><mn>2</mn><mi>&#947;</mi><mi>&#948;</mi><mo>&#8722;</mo><mi>&#945;</mi><mi>&#946;</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><msup><mi>r</mi><mn>5</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mi>r</mi></mrow><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><msup><mi>r</mi><mn>5</mn></msup><mo>&#8722;</mo><msup><mi>a</mi><mn>2</mn></msup><mi>r</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>r</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mi>r</mi><mn>4</mn></msup><mo>&#8722;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>8</mn><mo>+</mo><mn>1</mn></mrow><mrow><mn>8</mn><mo>&#8722;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>7</mn></mfrac></math></p>

</details>

---

### Q78. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi mathvariant="normal">t</mi></mfenced></math> denote the greatest integer<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi mathvariant="normal">t</mi></math>. Then the equation in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>,</mo><mo>&#160;</mo><msup><mfenced open="[" close="]"><mi mathvariant="normal">x</mi></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced open="[" close="]"><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn></math> has :

**Options:**

- **(A)** exactly two solutions
- **(B)** exactly four integral solutions
- **(C)** no integral solution
- **(D)** infinitely many solutions

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) infinitely many solutions**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="[" close="]"><mi>x</mi></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced open="[" close="]"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8722;</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="[" close="]"><mi>x</mi></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8722;</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>t</mi><mo>&#8722;</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>1</mn><mo>,</mo><mtext>&#8201;</mtext><mo>&#8722;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mo>&#8722;</mo><mn>3</mn><mo>,</mo><mtext>&#8201;</mtext><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mn>1</mn><mo>,</mo><mtext>&#8201;</mtext><mn>2</mn></mrow></mfenced></math></p><p>Hence, equation has infinitely many solutions.</p>

</details>

---

### Q79. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>p</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>q</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mrow></mfenced><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></mrow></mfenced><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac><mfenced><mrow><mn>9</mn><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac><mfenced><mrow><mn>9</mn><mo>-</mo><msup><mi>q</mi><mn>2</mn></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac><mfenced><mrow><mn>9</mn><mo>+</mo><msup><mi>p</mi><mn>2</mn></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac><mfenced><mrow><mn>9</mn><mo>-</mo><msup><mi>p</mi><mn>2</mn></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac><mfenced><mrow><mn>9</mn><mo>-</mo><msup><mi>p</mi><mn>2</mn></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></math> are roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>p</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mi>p</mi><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><mo>,</mo><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></math> are roots of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>q</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></math> are roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>q</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>q</mi><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>p</mi><mo>=</mo><mn>2</mn><mi>q</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mrow></mfenced><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mfrac><mn>1</mn><mi>&#946;</mi></mfrac></mrow></mfenced><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac></mrow></mfenced><mo>=</mo><mfenced open="{" close="}"><mrow><mi>&#945;</mi><mi>&#946;</mi><mo>-</mo><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac><mo>-</mo><mfrac><mi>&#946;</mi><mi>&#945;</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></mfrac></mrow></mfenced><mo>&#183;</mo><mfenced open="{" close="}"><mrow><mi>&#945;</mi><mi>&#946;</mi><mo>+</mo><mfrac><mn>1</mn><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="{" close="}"><mrow><mn>2</mn><mo>-</mo><mfenced><mfrac><mrow><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#945;</mi><mi>&#946;</mi></mrow><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#183;</mo><mfenced open="{" close="}"><mrow><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="{" close="}"><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>-</mo><mfenced><mfrac><mrow><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mo>&#183;</mo><mfenced open="{" close="}"><mfrac><mn>9</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>9</mn><mn>4</mn></mfrac><mfenced><mrow><mn>9</mn><mo>-</mo><msup><mi>p</mi><mn>2</mn></msup></mrow></mfenced></math> or, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac><mfenced><mrow><mn>9</mn><mo>-</mo><mn>4</mn><msup><mi>q</mi><mn>2</mn></msup></mrow></mfenced></math></p>

</details>

---

### Q80. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Consider the two sets:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mi>m</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo></math> both the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mo>(</mo><mi>m</mi><mo>+</mo><mn>1</mn><mo>)</mo><mi>x</mi><mo>+</mo><mi>m</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> are real <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>}</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mo>[</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>)</mo></math>
Which of the following is not true?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>-</mo><mi>B</mi><mo>=</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>5</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mi>B</mi><mo>=</mo><mo>{</mo><mo>-</mo><mn>3</mn><mo>}</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>-</mo><mi>A</mi><mo>=</mo><mo>(</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8746;</mo><mi>B</mi><mo>=</mo><mi>R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>-</mo><mi>B</mi><mo>=</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>5</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>**

**Detailed Solution:**

<p>Since both roots are real <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mfenced><mrow><mi>m</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>m</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>m</mi><mo>-</mo><mn>15</mn><mo>&#8805;</mo><mn>0</mn><mo>&#8658;</mo><mfenced><mrow><mi>m</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mi>m</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn><mo>]</mo><mo>&#8746;</mo><mo>[</mo><mn>5</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn><mo>]</mo><mo>&#8746;</mo><mo>[</mo><mn>5</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>-</mo><mi>B</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#8746;</mo><mo>[</mo><mn>5</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>-</mo><mi>A</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8746;</mo><mi>B</mi><mo>=</mo><mi>R</mi></math></p><p> </p><p> </p>

</details>

---

### Q81. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> be the roots of the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><msup><mi>&#945;</mi><mi>n</mi></msup><mo>+</mo><msup><mi>&#946;</mi><mi>n</mi></msup><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo></math> then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msub><mi>S</mi><mn>6</mn></msub><mo>+</mo><mn>5</mn><msub><mi>S</mi><mn>5</mn></msub><mo>=</mo><mn>2</mn><msub><mi>S</mi><mn>4</mn></msub></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mi>S</mi><mn>6</mn></msub><mo>+</mo><mn>6</mn><msub><mi>S</mi><mn>5</mn></msub><mo>+</mo><mn>2</mn><msub><mi>S</mi><mn>4</mn></msub><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mi>S</mi><mn>6</mn></msub><mo>+</mo><mn>6</mn><msub><mi>S</mi><mn>5</mn></msub><mo>=</mo><mn>2</mn><msub><mi>S</mi><mn>4</mn></msub></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msub><mi>S</mi><mn>6</mn></msub><mo>+</mo><mn>5</mn><msub><mi>S</mi><mn>5</mn></msub><mo>+</mo><mn>2</mn><msub><mi>S</mi><mn>4</mn></msub><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mi>S</mi><mn>6</mn></msub><mo>+</mo><mn>6</mn><msub><mi>S</mi><mn>5</mn></msub><mo>=</mo><mn>2</mn><msub><mi>S</mi><mn>4</mn></msub></math>**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></math> are roots of quadratic equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>5</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>&#945;</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mn>5</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>&#945;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>5</mn><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>&#946;</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mn>5</mn><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>&#946;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mi>S</mi><mn>6</mn></msub><mo>+</mo><mn>6</mn><msub><mi>S</mi><mn>5</mn></msub><mo>=</mo><mn>5</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>6</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>6</mn></msup></mrow></mfenced><mo>+</mo><mn>6</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>5</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>5</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>&#945;</mi><mn>4</mn></msup><mfenced><mrow><mn>5</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>&#945;</mi></mrow></mfenced><mo>+</mo><msup><mi>&#946;</mi><mn>4</mn></msup><mfenced><mrow><mn>5</mn><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>&#946;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>4</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>4</mn></msup></mrow></mfenced><mo>=</mo><mn>2</mn><msub><mi>S</mi><mn>4</mn></msub></math></p>

</details>

---

### Q82. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mi>S</mi></math>, be the set of all real roots of the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mi>x</mi></msup><mfenced separators="|"><mrow><msup><mn>3</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><msup><mn>3</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|" separators="|"><mrow><msup><mn>3</mn><mi>x</mi></msup><mo>-</mo><mn>2</mn></mrow></mfenced></math>, then

**Options:**

- **(A)** contains exactly two elements.
- **(B)** is a singleton.
- **(C)** is an empty set.
- **(D)** contains at least four elements.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) is a singleton.**

**Detailed Solution:**

<p>Let <math><msup><mrow><mn>3</mn></mrow><mrow><mi>x</mi></mrow></msup><mo>=</mo><mi>t</mi></math>
<math><mi>t</mi><mfenced separators="|"><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|" separators="|"><mrow><mi>t</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mn>2</mn><mo>=</mo><mfenced open="|" close="|" separators="|"><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced open="|" close="|" separators="|"><mrow><mi>t</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>g</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mfenced open="|" close="|" separators="|"><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced open="|" close="|" separators="|"><mrow><mi>t</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a8de9093-09d7-4fac-94e8-df3a9839b03f.png" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>g</mi><mfenced><mi>t</mi></mfenced></math> has a solution at <math><mi>t</mi><mo>=</mo><mi>a</mi></math>.
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mi>x</mi></msup><mo>=</mo><mi>a</mi><mo>&#160;</mo><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msub><mi>log</mi><mn>3</mn></msub><mo>&#8289;</mo><mi>a</mi></math>.
So, it is a singleton set.</p>

</details>

---

### Q83. JEE Main 2020 (08 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

The least positive value of &lsquo; <math><mi>a</mi></math> &rsquo; for which the equation, <math><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mfrac><mrow><mn>33</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>2</mn><mi>a</mi></math> has real roots is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<math><mi>D</mi><mo>≥</mo><mn>0</mn></math>  
<math><msup><mrow><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>10</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mfrac><mrow><mn>33</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>2</mn><mi>a</mi></mrow></mfenced><mo>≥</mo><mn>0</mn></math>  
<math><msup><mrow><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>10</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mfenced separators="|"><mrow><mn>33</mn><mo>-</mo><mn>4</mn><mi>a</mi></mrow></mfenced><mo>≥</mo><mn>0</mn></math>  
<math><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mi>a</mi><mo>-</mo><mn>32</mn><mo>≥</mo><mn>0</mn><mo>&#8658;</mo><mi>a</mi><mo>∈</mo><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced><mo>∪</mo><mfenced open="[" separators="|"><mrow><mn>8</mn><mo>,</mo><mo> </mo><mi>∞</mi></mrow></mfenced></math>

</details>

---

### Q84. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>&#945;</mi></math> and <math><mi>&#946;</mi></math> be the roots of the equation <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> . If <math><msub><mrow><mi>p</mi></mrow><mrow><mi>k</mi></mrow></msub><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mi>&#945;</mi></mrow></mfenced></mrow><mrow><mi>k</mi></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>&#946;</mi></mrow></mfenced></mrow><mrow><mi>k</mi></mrow></msup><mo>,</mo><mi></mi><mi>k</mi><mo>&#8805;</mo><mn>1</mn><mo>,</mo></math> then which one of the following statements is not true?

**Options:**

- **(A)** <math><msub><mrow><mi>p</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><msub><mrow><mi>p</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>-</mo><msub><mrow><mi>p</mi></mrow><mrow><mn>4</mn></mrow></msub></math>
- **(B)** <math><msub><mrow><mi>p</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>=</mo><mn>11</mn></math>
- **(C)** <math><mfenced separators="|"><mrow><msub><mrow><mi>p</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>p</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msub><mrow><mi>p</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>p</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>+</mo><msub><mrow><mi>p</mi></mrow><mrow><mn>5</mn></mrow></msub></mrow></mfenced><mo>=</mo><mn>26</mn></math>
- **(D)** <math><msub><mrow><mi>p</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>=</mo><msub><mrow><mi>p</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>⋅</mo><msub><mrow><mi>p</mi></mrow><mrow><mn>3</mn></mrow></msub></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msub><mrow><mi>p</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>=</mo><msub><mrow><mi>p</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>⋅</mo><msub><mrow><mi>p</mi></mrow><mrow><mn>3</mn></mrow></msub></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>5</mn></msup><mo>=</mo><mn>5</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">&#946;</mi><mn>5</mn></msup><mo>=</mo><mn>5</mn><mi mathvariant="normal">&#946;</mi><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">P</mi><mn>5</mn></msub><mo>=</mo><mn>5</mn><mfenced separators="|"><mrow><mi mathvariant="normal">&#945;</mi><mo>+</mo><mi mathvariant="normal">&#946;</mi></mrow></mfenced><mo>+</mo><mn>6</mn></math>
<math><mo>=</mo><mn>5</mn><mi></mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>+</mo><mn>6</mn></math>
<math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>=</mo><mn>11</mn></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">P</mi><mn>2</mn></msub><mo>=</mo><msup><mi mathvariant="normal">&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">&#946;</mi><mn>2</mn></msup><mo>=</mo><mi mathvariant="normal">&#945;</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi mathvariant="normal">&#946;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>3</mn></math>
 and <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><msup><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mi mathvariant="normal">&#946;</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#945;</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi mathvariant="normal">&#946;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mo>=</mo><mn>4</mn></math>
<math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&#215;</mo><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>12</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">P</mi><mn>5</mn></msub><mo>=</mo><mn>11</mn><mo>&#8658;</mo><msub><mi mathvariant="normal">P</mi><mn>5</mn></msub><mo>&#8800;</mo><msub><mi mathvariant="normal">P</mi><mn>2</mn></msub><mo>&#215;</mo><msub><mi mathvariant="normal">P</mi><mn>3</mn></msub></math></p>

</details>

---

### Q85. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>&#945;</mi></math> and <math><mi>&#946;</mi></math> be two real roots of the equation <math><mfenced separators="|"><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>&#8901;</mo><mi>&#955;</mi><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>k</mi></mrow></mfenced><mo>,</mo><mi mathvariant="normal"></mi></math> where <math><mi>k</mi><mfenced separators="|"><mrow><mo>&#8800;</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> and <math><mi>&#955;</mi></math> are real numbers. If <math><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>50</mn><mo>,</mo><mi></mi></math> then a value of <math><mi>&#955;</mi></math> is

**Options:**

- **(A)** <math><mn>10</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math><mn>10</mn></math>
- **(C)** <math><mn>5</mn></math>
- **(D)** <math><mn>5</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>10</mn></math>**

**Detailed Solution:**

<math><mfenced separators="|"><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>&#955;</mi><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></mrow></mrow></mrow></mrow></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>&#8289;</mo><mi>&#945;</mi><mo>+</mo><mi>tan</mi><mo>&#8289;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mi>&#955;</mi></mrow><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math>
<math><mi>t</mi><mi>a</mi><mi>n</mi><mi>&#945;</mi><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mrow></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfrac><mfrac><mrow><msqrt><mn>2</mn></msqrt><mi>&#955;</mi></mrow><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mi>&#955;</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>&#955;</mi><msqrt><mn>2</mn></msqrt></mfrac></math>
<math><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>50</mn></mrow></mrow></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mo>&#177;</mo><mn>10</mn></math>

</details>

---

### Q86. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>&#945;</mi><mi>&#160;</mi></math>and <math><mi>&#946;</mi></math> are the roots of the equation <math><mn>375</mn><mi>&#160;</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>25</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>n</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><mo>&#160;</mo><mo>&#160;</mo><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mi>&#945;</mi><mi>r</mi></msup><mo>+</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>n</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><mo>&#160;</mo><mo>&#160;</mo><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mi>&#946;</mi><mi>r</mi></msup></math> is equal to:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>21</mn></mrow><mrow><mn>346</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>116</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>29</mn></mrow><mrow><mn>358</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>For given quadratic <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>375</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>25</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>,</mo></math> its roots are,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mn>25</mn><mo>&#177;</mo><msqrt><msup><mn>25</mn><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>375</mn></msqrt></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>375</mn></mrow></mfrac><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mi>&#945;</mi></mfenced><mo>&#60;</mo><mn>1</mn><mo>,</mo><mfenced close="|" open="|" separators="|"><mi>&#946;</mi></mfenced><mo>&#60;</mo><mn>1</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>25</mn><mn>375</mn></mfrac><mo>,</mo><mi>&#160;</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>375</mn></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>n</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mi>&#945;</mi><mi>r</mi></msup><mo>+</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>n</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mi>&#946;</mi><mi>r</mi></msup></math></p><p><math><mo>=</mo><mfrac><mrow><mi>&#945;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>&#946;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>&#946;</mi></mrow></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mi>a</mi><mo>+</mo><mi>a</mi><mi>r</mi><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mi mathvariant="normal">&#8201;</mi><mi>infinite</mi><mo>&#8201;&#8201;</mo><mi>terms</mi></mtd></mtr><mtr><mtd><mo>=</mo><mfrac><mi>a</mi><mrow><mn>1</mn><mo>-</mo><mi>r</mi></mrow></mfrac><mi>&#8201;</mi><mi>&#8201;</mi><mo>&#8201;&#8201;</mo><mi>if</mi><mi>&#8201;</mi><mi>&#8201;</mi><mfenced close="|" open="|" separators="|"><mi>r</mi></mfenced><mo>&#60;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mi>&#945;</mi><mi>&#946;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mi>&#945;</mi><mi>&#946;</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mfrac><mn>25</mn><mn>375</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><mn>375</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>25</mn><mn>375</mn></mfrac><mo>-</mo><mfrac><mn>2</mn><mn>375</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mn>29</mn><mn>348</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math></p>

</details>

---

### Q87. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of real roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mfenced close="|" open="|" separators="|"><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mi>x</mi></msup><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>2</mn></mrow></mfenced></math> is : <math><mi mathvariant="normal">&#160;</mi></math>

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><mn>1</mn></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>1</mn></math>**

**Detailed Solution:**

<p>Let <math><msup><mrow><mn>2</mn></mrow><mrow><mi>x</mi></mrow></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mfenced close="|" open="|" separators="|"><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mfenced close="|" open="|" separators="|"><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mi>g</mi><mfenced><mi>t</mi></mfenced></mrow></munder><mo>=</mo><munder><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>t</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mrow><mi>f</mi><mfenced><mi>t</mi></mfenced></mrow></munder></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>x</mi></msup><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>&#8658;</mo><mi>t</mi><mo>&#62;</mo><mn>0</mn></math></p><p>From the graph, we have</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d4b486c9-75dd-4cdb-99b7-be704a37d47e-image.png" style="width: 311px; height: 200px;" /></p><p>It is clear from the graph that the two graphs have only one point of intersection.</p><p>So, number of real roots of the given equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo></math></p>

</details>

---

### Q88. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>&#945;</mi></math> and <math><mi>&#946;</mi></math> are the roots of the quadratic equation <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal">&#160;</mi><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mi mathvariant="normal">&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> , then <math><mfrac><mrow><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>12</mn></mrow></msup><mo>+</mo><msup><mrow><mi>&#946;</mi></mrow><mrow><mn>12</mn></mrow></msup></mrow><mrow><mo>(</mo><msup><mrow><mi>&#945;</mi></mrow><mrow><mo>-</mo><mn>12</mn></mrow></msup><mo>+</mo><msup><mrow><mi>&#946;</mi></mrow><mrow><mo>-</mo><mn>12</mn></mrow></msup><mo>)</mo><msup><mrow><mo>.</mo><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo></mrow><mrow><mn>24</mn></mrow></msup></mrow></mfrac></math> is equal to :

**Options:**

- **(A)** <math><mfrac><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>6</mn></mrow></msup></mrow><mrow><msup><mrow><mo>(</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>+</mo><mn>8</mn><mo>)</mo></mrow><mrow><mn>12</mn></mrow></msup></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>12</mn></mrow></msup></mrow><mrow><msup><mrow><mo>(</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>-</mo><mn>4</mn><mo>)</mo></mrow><mrow><mn>12</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>12</mn></mrow></msup></mrow><mrow><msup><mrow><mo>(</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>+</mo><mn>8</mn><mo>)</mo></mrow><mrow><mn>12</mn></mrow></msup></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>12</mn></mrow></msup></mrow><mrow><msup><mrow><mo>(</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>-</mo><mn>8</mn><mo>)</mo></mrow><mrow><mn>6</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>12</mn></mrow></msup></mrow><mrow><msup><mrow><mo>(</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>+</mo><mn>8</mn><mo>)</mo></mrow><mrow><mn>12</mn></mrow></msup></mrow></mfrac></math>**

**Detailed Solution:**

Let <math><mi>E</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>12</mn></mrow></msup><mo>+</mo><msup><mrow><mi>&#946;</mi></mrow><mrow><mn>12</mn></mrow></msup></mrow><mrow><mfenced separators="|"><mrow><msup><mrow><mi>&#945;</mi></mrow><mrow><mo>-</mo><mn>12</mn></mrow></msup><mo>+</mo><msup><mrow><mi>&#946;</mi></mrow><mrow><mo>-</mo><mn>12</mn></mrow></msup></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced></mrow><mrow><mn>24</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>12</mn></mrow></msup><mo>+</mo><msup><mrow><mi>&#946;</mi></mrow><mrow><mn>12</mn></mrow></msup></mrow><mrow><mfrac><mrow><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>12</mn></mrow></msup><mo>+</mo><msup><mrow><mi>&#946;</mi></mrow><mrow><mn>12</mn></mrow></msup></mrow><mrow><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>12</mn></mrow></msup><mo>&#215;</mo><msup><mrow><mi>&#946;</mi></mrow><mrow><mn>12</mn></mrow></msup></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced></mrow><mrow><mn>24</mn></mrow></msup></mrow></mfrac></math>
<math><mi>E</mi><mo>=</mo><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced></mrow><mrow><mn>12</mn></mrow></msup></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced></mrow><mrow><mn>24</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced></mrow><mrow><mn>12</mn></mrow></msup></mrow><mrow><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced></mrow><mrow><mn>12</mn></mrow></msup></mrow></mfrac></math>
Now <math><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#952;</mi></math>
<math><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#952;</mi></math>
<math><mo>&#8756;</mo><mi>E</mi><mo>=</mo><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mn>12</mn></mrow></msup></mrow><mrow><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#952;</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>12</mn></mrow></msup></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>12</mn></mrow></msup></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>8</mn><mo>+</mo><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mn>12</mn></mrow></msup></mrow></mfrac></math>

</details>

---

### Q89. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>m</mi></math> is chosen in the quadratic equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><msup><mfenced separators="|"><mrow><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math> such that the sum of its roots is greatest, then the absolute difference of the cubes of its roots is:

**Options:**

- **(A)** <math><mn>4</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math><mn>10</mn><msqrt><mn>5</mn></msqrt></math>
- **(C)** <math><mn>8</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math><mn>8</mn><msqrt><mn>5</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>8</mn><msqrt><mn>5</mn></msqrt></math>**

**Detailed Solution:**

<p>Let, the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><msup><mfenced><mrow><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math><mi>&#946;</mi></math></p><p>We know that the sum and product of roots of a quadratic equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>&#8800;</mo><mn>0</mn></math> are respectively <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>b</mi><mi>a</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>c</mi><mi>a</mi></mfrac><mo>.</mo></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>3</mn><mrow><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mfrac><msup><mfenced><mrow><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>=</mo><mfenced><mrow><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is maximum, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>m</mi><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8756;</mo></math> the equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mn>1</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>3</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>3</mn></msup><mo>=</mo><mfenced separators="|"><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mfenced separators="|"><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><msup><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>&#945;</mi><mi>&#946;</mi></msqrt><mfenced separators="|"><mrow><msup><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>9</mn><mo>-</mo><mn>4</mn></msqrt><mo>&#160;</mo><mfenced separators="|"><mrow><mn>9</mn><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><msqrt><mn>5</mn></msqrt><mo>.</mo></math></p>

</details>

---

### Q90. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mi>p</mi><mo>,</mo><mi>&#160;</mi><mi>q</mi><mo>&#8712;</mo><mi>&#160;</mi><mi>Q</mi><mi>&#160;</mi><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math> is a root of the quadratic equation <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>p</mi><mi>x</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> then

**Options:**

- **(A)** <math><msup><mrow><mi>p</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>–</mo><mn>4</mn><mi>q</mi><mo>+</mo><mn>12</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>q</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>p</mi><mo>+</mo><mn>14</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mn>2</mn></msup><mo>&#8211;</mo><mn>4</mn><mi>q</mi><mo>&#8211;</mo><mn>12</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>–</mo><mn>4</mn><mi>p</mi><mo>–</mo><mn>16</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mn>2</mn></msup><mo>&#8211;</mo><mn>4</mn><mi>q</mi><mo>&#8211;</mo><mn>12</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>In given equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>p</mi><mi>x</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>p</mi><mo>,</mo><mo>&#160;</mo><mi>q</mi><mo>&#8712;</mo><mi>Q</mi><mo>.</mo></math></p><p>And, we know that the irrational roots of a quadratic equation exist in conjugate pair, if the coefficients are rational.</p><p>Thus, if one root of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>p</mi><mi>x</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>,</mo></math> then, the other root will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>.</mo></math></p><p>We know that the sum and product of the roots of a quadratic equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> are respectively <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>b</mi><mi>a</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>c</mi><mi>a</mi></mfrac><mo>.</mo></math></p><p>Therefore, the sum of roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>=</mo><mo>-</mo><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p>And, the product of roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>=</mo><mi>q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>q</mi><mo>=</mo><msup><mn>2</mn><mn>2</mn></msup><mo>-</mo><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p>Thus, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>q</mi><mo>-</mo><mn>12</mn><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>1</mn><mo>-</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>16</mn><mo>-</mo><mn>16</mn><mo>=</mo><mn>0</mn><mo>.</mo></math></p><p>Thus, the answer is, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>q</mi><mo>-</mo><mn>12</mn><mo>=</mo><mn>0</mn><mo>.</mo></math></p>

</details>

---

### Q91. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of integral values of <math><mi>m</mi></math> for which the equation, <math><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>m</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>8</mn><mi>m</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> has no real root, is

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** Infinitely many
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Infinitely many**

**Detailed Solution:**

Since the given equation has no real solution.
<math><mo>&#8658;</mo><mi>D</mi><mo>&#60;</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>m</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#215;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>m</mi><mn>2</mn></msup></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>8</mn><mi>m</mi></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>9</mn><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>6</mn><mi>m</mi></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>8</mn><mi>m</mi><mo>+</mo><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>8</mn><msup><mrow><mi>m</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mi>m</mi><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>m</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>&#60;</mo><mn>0</mn></math>
Clearly, for infinite values of <math><mi>m</mi></math> given condition is true.

</details>

---

### Q92. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The sum of the solutions of the equation <math><mfenced close="|" open="|" separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><msqrt><mi>x</mi></msqrt><mfenced separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>,</mo><mfenced separators="|"><mrow><mi>x</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced><mi>&#160;</mi></math> is equal to

**Options:**

- **(A)** <math><mn>10</mn></math>
- **(B)** <math><mn>9</mn></math>
- **(C)** <math><mn>12</mn></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>10</mn></math>**

**Detailed Solution:**

<p>Given,</p><p>     <math><mfenced close="|" open="|" separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><msqrt><mi>x</mi></msqrt><mfenced separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>x</mi><mo>-</mo><mn>4</mn><msqrt><mi>x</mi></msqrt><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn><mi>&#160;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><msup><mfenced separators="|"><msqrt><mi>x</mi></msqrt></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><msqrt><mi>x</mi></msqrt><mo>+</mo><mn>4</mn><mo>=</mo><mn>2</mn></math>       (Adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> on both sides)
<math><mo>&#8658;</mo><msup><mrow><mfenced separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfenced close="|" open="|" separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math>
<math><mo>&#8658;</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>t</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn><mi>&#160;</mi></math>; <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>t</mi><mo>&#160;</mo><mo>;</mo><mo>&#160;</mo><mfenced><mrow><mi>t</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>1</mn></math>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mo>-</mo><mn>2</mn></math> ; Rejected because <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#62;</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>
<math><mo>&#8658;</mo><msqrt><mi>x</mi></msqrt><mo>=</mo><mn>3</mn></math> or <math><msqrt><mi>x</mi></msqrt><mo>=</mo><mn>1</mn></math>
<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>9</mn></math> or <math><mi>x</mi><mo>=</mo><mn>1</mn></math>
Hence, the required sum <math><mo>=</mo><mn>10</mn></math>.</p>

</details>

---

### Q93. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>&#955;</mi></math> be the ratio of the roots of the quadratic equation in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mi>&#160;</mi><mn>3</mn><msup><mi>m</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>m</mi><mfenced separators="|"><mrow><mi>m</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>, then the least value of <math><mi>m</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>+</mo><mfrac><mn>1</mn><mi>&#955;</mi></mfrac><mo>=</mo><mn>1</mn></math>, is :

**Options:**

- **(A)** <math><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math><mo>-</mo><mn>2</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math><mn>4</mn><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math><mn>4</mn><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>4</mn><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p>Let <math><mi>&#945;</mi></math> and <math><mi>&#946;</mi></math> are the roots of given equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>m</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>m</mi><mfenced separators="|"><mrow><mi>m</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi>m</mi><mfenced><mrow><mi>m</mi><mo>-</mo><mn>4</mn></mrow></mfenced></mrow><mrow><mn>3</mn><msup><mi>m</mi><mn>2</mn></msup></mrow></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mfrac><mn>2</mn><mrow><mn>3</mn><msup><mi>m</mi><mn>2</mn></msup></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac><mo>=</mo><mi>&#955;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>+</mo><mfrac><mn>1</mn><mi>&#955;</mi></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac><mo>+</mo><mfrac><mi>&#946;</mi><mi>&#945;</mi></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>3</mn><mi>&#945;</mi><mi>&#946;</mi></math></p><p>Using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mfrac><mrow><mo>-</mo><mi>m</mi><mfenced separators="|"><mrow><mi>m</mi><mo>-</mo><mn>4</mn></mrow></mfenced></mrow><mrow><mn>3</mn><msup><mi>m</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#215;</mo><mn>2</mn></mrow><mrow><mn>3</mn><msup><mi>m</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mn>4</mn><mo>&#177;</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math></p><p>Hence, the least value of <math><mi>m</mi></math> is <math><mn>4</mn><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math>.</p>

</details>

---

### Q94. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\alpha$ and $\beta$ be the roots of the quadratic equation $x^{2} \sin \theta-x(\sin \theta \cos \theta+1)+\cos \theta=0\left(0  < \theta < 45^{\circ}\right),$ and

$\alpha < \beta .$ Then $\sum_{n=0}^{\infty}\left(\alpha^{n}+\frac{(-1)^{n}}{\beta^{n}}\right)$ is equal to :

**Options:**

- **(A)** $\frac{1}{1-\cos \theta}-\frac{1}{1+\sin \theta}$
- **(B)** $\frac{1}{1+\cos \theta}+\frac{1}{1-\sin \theta}$
- **(C)** $\frac{1}{1-\cos \theta}+\frac{1}{1+\sin \theta}$
- **(D)** $\frac{1}{1+\cos \theta}-\frac{1}{1-\sin \theta}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{1-\cos \theta}+\frac{1}{1+\sin \theta}$**

**Detailed Solution:**

$x^{2} \sin \theta-x(\sin \theta \cdot \cos \theta+1)+\cos \theta=0$.

$x^{2} \sin \theta-x \sin \theta \cdot \cos \theta-x+\cos \theta=0$

$x \sin \theta(x-\cos \theta)-1(x-\cos \theta)=0$

$(x-\cos \theta)(x \sin \theta-1)=0$

$\therefore x=\cos \theta, \operatorname{cosec} \theta, \theta \in\left(0,45^{\circ}\right)$

$\therefore \alpha=\cos \theta, \beta=\operatorname{cosec} \theta$

$\sum_{n=0}^{\infty} \alpha^{n}=1+\cos \theta+\cos ^{2} \theta+\ldots \infty=\frac{1}{1-\cos \theta}$

$\sum_{n=0}^{\infty} \frac{(-1)^{n}}{\beta^{n}}=1-\frac{1}{\operatorname{cosec} \theta}+\frac{1}{\operatorname{cosec}^{2} \theta}-\frac{1}{\operatorname{cosec}^{3} \theta}+\ldots \infty$

$=1-\sin \theta+\sin ^{2} \theta-\sin ^{3} \theta+\ldots \infty$

$=\frac{1}{1+\sin \theta}$

$\therefore \quad \sum_{n=0}^{\infty}\left(\alpha^{n}+\frac{(-1)^{n}}{\beta^{n}}\right)=\sum_{n=0}^{\infty} \alpha^{n}+\sum_{n=0}^{\infty} \frac{(-1)^{n}}{\beta^{n}}$

$=\frac{1}{1-\cos \theta}+\frac{1}{1+\sin \theta} .$

</details>

---

### Q95. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If one real root of the quadratic equation $81 x^{2}+k x+256=0$ is cube of the other root, then a value of $\mathrm{k}$ is :

**Options:**

- **(A)** -81
- **(B)** 100
- **(C)** 144
- **(D)** -300

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -300**

**Detailed Solution:**

Let $\alpha$ and $\beta$ be the roots of the equation, $81 x^{2}+k x+256=0$

Given $(\alpha)^{\frac{1}{3}}=\beta \Rightarrow \alpha=\beta^{3}$

$\because \quad$ Product of the roots $=\frac{256}{81}$

$\therefore \quad(\alpha)(\beta)=\frac{256}{81}$

$\Rightarrow \quad \beta^{4}=\left(\frac{4}{3}\right)^{4} \Rightarrow \beta=\frac{4}{3} \Rightarrow \alpha=\frac{64}{27}$

$\because$ Sum of the roots $=-\frac{k}{81}$

$\therefore \quad \alpha+\beta=-\frac{k}{81} \Rightarrow \frac{4}{3}+\frac{64}{27}=-\frac{k}{81}$

$\Rightarrow \quad k=-300$

</details>

---

### Q96. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of all possible positive integral value of <math><mi>&#945;</mi></math> for which the roots of the quadratic equation <math><mn>6</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>11</mn><mi>x</mi><mo>+</mo><mi>&#945;</mi><mo>=</mo><mn>0</mn></math> are rational numbers is:

**Options:**

- **(A)** <math><mn>5</mn></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><mn>4</mn></math>
- **(D)** <math><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>3</mn></math>**

**Detailed Solution:**

<p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>a</mi><mi>c</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>121</mn><mo>-</mo><mn>24</mn><mi>&#945;</mi></math>
For rational roots, <math><mi>D</mi></math> must be perfect square.
<math><mo>&#8756;</mo><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn></math>
<math><mo>&#8756;</mo></math> Number of values of <math><mi>&#945;</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q97. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>&#945;</mi></math> and <math><mi>&#946;</mi></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>15</mn></msup></math> is equal to

**Options:**

- **(A)** <math><mo>-</mo><mn>512</mn></math>
- **(B)** <math><mn>128</mn></math>
- **(C)** <math><mn>512</mn></math>
- **(D)** <math><mo>-</mo><mn>256</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mo>-</mo><mn>256</mn></math>**

**Detailed Solution:**

Let the two roots of  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#177;</mo><msqrt><mn>4</mn><mo>-</mo><mn>8</mn></msqrt></mrow><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#177;</mo><mi>i</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mo>&#177;</mo><mi>i</mi><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>2</mn></msqrt><mfenced separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>&#177;</mo><mi>i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>15</mn></msup><mo>=</mo><msup><mfenced open="[" close="]" separators="|"><mrow><msqrt><mn>2</mn></msqrt><mfenced separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mi>i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></mrow></mfenced><mn>15</mn></msup><mo>+</mo><msup><mfenced open="[" close="]" separators="|"><mrow><msqrt><mn>2</mn></msqrt><mfenced separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfrac><mrow><mi>&#160;</mi><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>-</mo><mi>i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></mrow></mfenced><mn>15</mn></msup></math>

       <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>15</mn></msup><mo>=</mo><msup><mn>2</mn><mfrac><mn>15</mn><mn>2</mn></mfrac></msup><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfrac><mrow><mn>45</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mi>i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mn>45</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfrac><mrow><mn>45</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>-</mo><mi>i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mn>45</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>15</mn></msup><mo>=</mo><msup><mn>2.2</mn><mfrac><mn>15</mn><mn>2</mn></mfrac></msup><mo>.</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfrac><mrow><mn>45</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>=</mo><msup><mn>2</mn><mfrac><mn>17</mn><mn>2</mn></mfrac></msup><mo>.</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>=</mo><mo>-</mo><msup><mn>2</mn><mfrac><mn>17</mn><mn>2</mn></mfrac></msup><mo>.</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>15</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>15</mn></msup><mo>=</mo><mo>-</mo><mn>256</mn></math>

</details>

---

### Q98. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> of a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi><mi>A</mi><mi>B</mi><mi>C</mi></math> satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>cos</mi><mi>A</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>, then the roots of the quadratic equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>27</mn><mi>x</mi><mo>+</mo><mn>20</mn><mo>=</mo><mn>0</mn></math> are

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sec</mi><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>cot</mi><mi>A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sec</mi><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>tan</mi><mi>A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>cos</mi><mi>A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>sec</mi><mi>A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sec</mi><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>tan</mi><mi>A</mi></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>cos</mi><mi>A</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>cos</mi><mi>A</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>5</mn></mfrac></math></p><p>Clearly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>90</mn><mo>&#176;</mo><mo>,</mo><mn>180</mn><mo>&#176;</mo></mrow></mfenced></math></p><p>Now, roots of equation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>27</mn><mi>x</mi><mo>+</mo><mn>20</mn><mo>=</mo><mn>0</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>27</mn><mo>&#177;</mo><msqrt><mn>729</mn><mo>-</mo><mn>720</mn></msqrt></mrow><mn>18</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>27</mn><mo>&#177;</mo><mn>3</mn></mrow><mn>18</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>=</mo><mi>sec</mi><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>=</mo><mi>tan</mi><mi>A</mi></math>.</p><p>Hence, the roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sec</mi><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>A</mi></math>.</p>

</details>

---

### Q99. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>,</mo><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> be real numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>p</mi><mo>&#8800;</mo><mi>q</mi><mo>,</mo><mi>r</mi><mo>&#8800;</mo><mn>0</mn></mrow></mfenced></math>, such that the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>x</mi><mo>+</mo><mi>p</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>+</mo><mi>q</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>r</mi></mfrac></math> are equal in magnitude but opposite in sign, then the sum of squares of these roots is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced separators="|"><mrow><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<p>Given quadratic equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>x</mi><mo>+</mo><mi>p</mi><mi>&#160;</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>+</mo><mi>q</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>r</mi></mfrac></math>.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> be the roots of given equation.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mi>p</mi><mo>+</mo><mi>q</mi></mrow></mfenced><mi>r</mi><mo>=</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mi>p</mi></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mi>q</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mi>q</mi><mo>-</mo><mn>2</mn><mi>r</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mi>p</mi><mi>q</mi><mo>-</mo><mi>p</mi><mi>r</mi><mo>-</mo><mi>q</mi><mi>r</mi><mo>=</mo><mn>0</mn></math></p><p>Now, sum of roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mi>b</mi></mrow><mi>a</mi></mfrac><mo>=</mo><mo>-</mo><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mi>q</mi><mo>-</mo><mn>2</mn><mi>r</mi></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mi>q</mi><mo>-</mo><mn>2</mn><mi>r</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>    (<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math>Given that roots are equal in magnitude and opposite in sign)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>2</mn><mi>r</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Product of roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfrac><mi>c</mi><mi>a</mi></mfrac><mo>=</mo><mi>p</mi><mi>q</mi><mo>-</mo><mi>p</mi><mi>r</mi><mo>-</mo><mi>q</mi><mi>r</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#945;</mi><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>-</mo><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><mi>p</mi><mi>q</mi><mo>-</mo><mi>p</mi><mi>r</mi><mo>-</mo><mi>q</mi><mi>r</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mi>p</mi><mi>q</mi><mo>+</mo><mn>2</mn><mi>r</mi><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mi>q</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><mi>p</mi><mi>q</mi><mo>+</mo><msup><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mi>q</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mn>1</mn></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></math></p>

</details>

---

### Q100. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>&#8289;</mo><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>&#8289;</mo><mi>B</mi></math> are the roots of the quadratic equation <math><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>-</mo><mn>25</mn><mo>=</mo><mn>0</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>-</mo><mn>10</mn><mi>sin</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mi>cos</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>-</mo><mn>25</mn><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>25</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(C)** <math><mo>-</mo><mn>10</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>25</mn></math>**

**Detailed Solution:**

<p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>&#8289;</mo><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>&#8289;</mo><mi>B</mi></math> are roots of the equation <math><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>-</mo><mn>25</mn><mo>=</mo><mn>0</mn></math>.</p><p>So, <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>A</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>B</mi></mrow></mrow><mo>=</mo><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math> and <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>A</mi></mrow></mrow><mo>.</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>B</mi></mrow></mrow><mo>=</mo><mo>-</mo><mfrac><mrow><mn>25</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>tan</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>tan</mi><mo>&#8289;</mo><mi>A</mi><mo>+</mo><mi>tan</mi><mo>&#8289;</mo><mi>B</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mo>&#8289;</mo><mi>A</mi><mo>.</mo><mi>tan</mi><mo>&#8289;</mo><mi>B</mi></mrow></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>10</mn><mn>3</mn></mfrac></mstyle><mrow><mn>1</mn><mo>+</mo><mfrac><mn>25</mn><mn>3</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mn>10</mn><mn>28</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>14</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>&#177;</mo><mn>5</mn></mrow><msqrt><mn>221</mn></msqrt></mfrac><mo>&#38;</mo><mo>&#160;</mo><mi>cos</mi><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>&#177;</mo><mn>14</mn></mrow><msqrt><mn>221</mn></msqrt></mfrac></math></p><p>(Note that either both are negative or both positive)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>-</mo><mn>10</mn><mi>sin</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>.</mo><mi>cos</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>-</mo><mn>25</mn><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>&#215;</mo><mfrac><mn>25</mn><mn>221</mn></mfrac><mo>-</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>14</mn></mrow><mn>221</mn></mfrac><mo>-</mo><mn>25</mn><mo>&#215;</mo><mfrac><msup><mn>14</mn><mn>2</mn></msup><mn>221</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>25</mn><mn>221</mn></mfrac><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mn>28</mn><mo>-</mo><mn>196</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>25</mn></math></p>

</details>

---

### Q101. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi></math> is such that the sum of the cubes of the roots of the equation <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mn>10</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> is minimum, then the magnitude of the difference of the roots of this equation is :

**Options:**

- **(A)** <math><mn>4</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math><mn>20</mn></math>
- **(C)** <math><mn>2</mn><msqrt><mn>5</mn></msqrt></math>
- **(D)** <math><mn>2</mn><msqrt><mn>7</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>2</mn><msqrt><mn>5</mn></msqrt></math>**

**Detailed Solution:**

<p><math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mn>10</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mi>&#955;</mi><mo>-</mo><mn>2</mn><mo>&#38;</mo><mo>&#160;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mn>10</mn><mo>-</mo><mi>&#955;</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Let roots are <math><mi>&#945;</mi><mi>&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi>&#160;</mi><mi>&#946;</mi></math>.</p><p><math><mo>&#8658;</mo><mi>&#160;</mi><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mi>&#946;</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>&#945;</mi><mi>&#946;</mi><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo></math></p><p><math><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mi>&#955;</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>3</mn><mfenced separators="|"><mrow><mn>10</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mo>(</mo><mi>&#955;</mi><mo>-</mo><mn>2</mn><mo>)</mo></math></p><p><math><mo>=</mo><mi>&#160;</mi><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><msup><mrow><mn>6</mn><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>12</mn><mi>&#955;</mi><mo>-</mo><mn>8</mn><mo>-</mo><mn>3</mn><mo>(</mo><mn>10</mn><mi>&#955;</mi><mo>-</mo><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>20</mn><mo>+</mo><mn>2</mn><mi>&#955;</mi><mo>)</mo></math></p><p><math><mo>=</mo><mi>&#160;</mi><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><msup><mrow><mn>3</mn><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>24</mn><mi>&#955;</mi><mo>+</mo><mn>52</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>z</mi></mrow><mrow><mi>d</mi><mi>&#955;</mi></mrow></mfrac><mo>=</mo><mn>3</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>&#955;</mi><mo>-</mo><mn>24</mn><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>8</mn></mrow></mfenced></math> (where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><msup><mi>&#945;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>3</mn></msup></math>)</p><p>For maximum and critical points, derivative must be zero.</p><p><math><mo>&#8658;</mo><mi>&#160;</mi><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>&#955;</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>&#955;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>2,</mn><mo>&#160;</mo><mn>4</mn></math></p><p>Now, <math><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>z</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>6</mn><mi>&#955;</mi><mo>-</mo><mn>6</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>z</mi></mrow><mrow><mi>d</mi><msup><mi>&#955;</mi><mn>2</mn></msup></mrow></mfrac><mo>&#60;</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>3</mn></msup></math> is maximum and</p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#955;</mi><mo>=</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>z</mi></mrow><mrow><mi>d</mi><msup><mi>&#955;</mi><mn>2</mn></msup></mrow></mfrac><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>3</mn></msup></math> is minimum.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>Equation will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math>.</p><p>Using quadratic formula, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#177;</mo><msqrt><msup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>6</mn></msqrt></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#177;</mo><msqrt><mo>-</mo><mn>20</mn></msqrt></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#177;</mo><mn>2</mn><msqrt><mn>5</mn></msqrt><mi>i</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>5</mn></msqrt><mi>i</mi></math></p><p>Thus, difference of roots is <math><mfenced close="|" open="|" separators="|"><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>5</mn></msqrt></math></p>

</details>

---

### Q102. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `1`

If $\lambda \in \mathrm{R}$ is such that the sum of the cubes of the roots of the equation, $x^2+(2-\lambda) x+(10-\lambda)=0$ is minimum, then the magnitude of the difference of the roots of this equation is

**Options:**

- **(A)** 20
- **(B)** $2 \sqrt{5}$
- **(C)** $2 \sqrt{7}$
- **(D)** $4 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \sqrt{5}$**

**Detailed Solution:**

Let, the roots of the equation, $x^2+(2-\lambda) x+(10-\lambda)=0$ are $\alpha$ and $\beta$.
Also roots of the given equation are
$$
\frac{\lambda-2 \pm \sqrt{4-4 \lambda+\lambda^2-40+4 \lambda}}{2}=\frac{\lambda-2 \pm \sqrt{\lambda^2-36}}{2}
$$
The magnitude of the difference of the roots is $\left|\sqrt{\lambda^2-36}\right|$

So, $\alpha^3+\beta^3=\frac{(\lambda-2)^3}{4}+\frac{3(\lambda-2)\left(\lambda^2-36\right)}{4}$
$$
\begin{aligned}
=\frac{(\lambda-2)\left(4 \lambda^2-4 \lambda-104\right)}{4} \\
=&(\lambda-2)\left(\lambda^2-\lambda-26\right)=f(\lambda)
\end{aligned}
$$
As $f(\lambda)$ attains its minimum value at $\lambda=4$.
Therefore, the magintude of the difference of the

</details>

---

### Q103. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `3`

If, for a positive integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>, the quadratic equation,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mo>.</mo><mo>..</mo><mo>+</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mover accent="true"><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mo>&#175;</mo></mover></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mn>10</mn><mi>n</mi></math> 

has two consecutive integral solutions, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>**

**Detailed Solution:**

<p>On simplifying we get the quadratic equations as
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><munder><munder><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mo>&#9183;</mo></munder><mrow><mi>n</mi><mo>&#160;</mo><mtext>times</mtext></mrow></munder></mfenced><mo>+</mo><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>5</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced open="[" close="]"><mrow><mn>1</mn><mo>.</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>.</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></mrow></mfenced><mo>=</mo><mn>10</mn><mi>n</mi></math>
<math><mi>n</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi><mo>+</mo><mfrac><mrow><mi>n</mi><mfenced separators="|"><mrow><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mn>10</mn><mi>n</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi><mi>x</mi><mo>+</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>31</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></math> are the roots of the above equation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mi>n</mi><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>31</mn></mrow><mn>3</mn></mfrac></math>

Now, the difference of roots<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mfenced close="|" open="|" separators="|"><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mi>&#160;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><msup><mfenced separators="|"><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mn>1</mn></math>

<math><mo>&#8658;</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced separators="|"><mrow><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>31</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>

<math><mo>&#8658;</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>121</mn></math>

<math><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>11</mn></math></p>

</details>

---

### Q104. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>x</mi></math> is a solution of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><mi>&#160;</mi><msqrt><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mi>x</mi><mo>&#8805;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math> , then <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></math>  is equal to :

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><mi>&#160;</mi><msqrt><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>-</mo><mn>2</mn><msqrt><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt><mo>=</mo><mn>1</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>2</mn><msqrt><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mi>x</mi><mo>=</mo><mn>5</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>5</mn><mn>8</mn></mfrac></math> which satisfies equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p>

</details>

---

### Q105. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If the equations <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> and <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn></math> have a common root different from <math><mo>-</mo><mn>1</mn><mo>,</mo></math> then <math><mfenced close="|" open="|" separators="|"><mrow><mi>b</mi></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

Let common root be <math><mi>x</mi></math>
<math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>     ...<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>

<math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn></math>       ...<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>-</mo><mfenced><mn>2</mn></mfenced></math>, we get <math><mi>x</mi><mo>=</mo><mfrac><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math>

Put <math><mi>x</mi></math> in Equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, we get

<math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>&#160;+&#160;</mo><mfenced separators="|"><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>b</mi><msup><mfenced separators="|"><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math> <math><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>b</mi><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn><mo>+</mo><mi>b</mi><mfenced separators="|"><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math> <math><mn>2</mn><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>b</mi><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>2</mn><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo>&#160; </math> <math><msup><mrow><mi>b</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo>&#160;&#160;</math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mfenced separators="|"><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>3</mn></math>

When  <math><mi>b</mi><mo>=</mo><mn>0</mn></math> then common root <math><mi>x</mi><mo>=</mo><mi> </mi><mo>-</mo><mn>1</mn></math>
But the given common root <math><mi>x</mi><mo>&#8800;</mo><mo>-</mo><mn>1</mn></math>

<math><mo>&#8756;&#160;</mo></math><math><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>&#160;</mi><mo>-</mo><mn>3</mn></math>

<math><mi>b</mi><mo>=</mo><mi>&#160;</mi><mo>&#177;</mo><mi>&#160;</mi><msqrt><mn>3</mn></msqrt><mi>i</mi></math>

<math><mfenced close="|" open="|" separators="|"><mrow><mi>b</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><msqrt><mn>3</mn></msqrt></math>

</details>

---

### Q106. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `1`

The sum of all real values of <math><mi>x</mi></math> satisfying the equation <math><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>60</mn></mrow></msup><mo>=</mo><mn>1</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

The given equation will be true in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> cases.

<strong>Case 1:</strong> when <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>1</mn><mi>&#160;</mi><mi>&#160;</mi></math>

<math><mo>&#8658;</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn></math>

<strong>Case 2:</strong> when <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>60</mn><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>6</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>10</mn></math>

<strong>Case 3:</strong> when <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>60</mn><mo>&#8712;</mo></math> even integers

Now, <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>=</mo><mo>-</mo><mn>1</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi></math>

<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn></math>

Only <math><mi>x</mi><mo>=</mo><mn>2</mn></math> satisfies the given condition,

Hence, sum of all real values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>6</mn><mo>-</mo><mn>10</mn><mo>+</mo><mn>2</mn></math><math><mo>=</mo><mn>3</mn><mi>&#160;</mi></math>

</details>

---

### Q107. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If the two roots of the equation, <math><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math> are real and distinct, then the set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is equal to

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced><mi> </mi><mo>∪</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mi> </mi><mo>∪</mo><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi> </mi><mi>∞</mi></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi> </mi><mn>0</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced><mi> </mi><mo>∪</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><math><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math>

<math><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>(</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>&#160;</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mi>a</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>a</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;&#160;</mo><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mi>a</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>

If two Roots are real

Then, roots of <math><mi>a</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>+</mo><mi>a</mi><mo>=</mo><mn>0</mn></math> should be real &amp; distinct.

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>1</mn><mo>-</mo><mn>4</mn><msup><mi>a</mi><mn>2</mn></msup><mo>&#62;</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>a</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>a</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/105a7a06-f678-4337-bb10-8de396cd5a71-image.png" style="width: 262px; height: 100px;" /></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8800;</mo><mn>0</mn></math> therefore

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced><mi>&#160;</mi><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q108. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> be the roots of equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msup><mi>&#945;</mi><mi>n</mi></msup><mo>-</mo><msup><mi>&#946;</mi><mi>n</mi></msup><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>n</mi><mo>&#8805;</mo><mn>1</mn><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>a</mi><mrow><mn>1</mn><mn>0</mn></mrow></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mn>8</mn></msub></mrow><mrow><mn>2</mn><msub><mi>a</mi><mn>9</mn></msub></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></math> are roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>&#945;</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>&#946;</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>=</mo><mn>6</mn><mi>&#945;</mi></math> and<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>=</mo><mn>6</mn><mi>&#946;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>a</mi><mrow><mn>1</mn><mn>0</mn></mrow></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mn>8</mn></msub></mrow><mrow><mn>2</mn><msub><mi>a</mi><mn>9</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced><mrow><msup><mi>&#945;</mi><mn>10</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>10</mn></msup></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>8</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>8</mn></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>9</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>9</mn></msup></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><msup><mi>&#945;</mi><mrow><mn>1</mn><mn>0</mn></mrow></msup><mo>-</mo><mn>2</mn><msup><mi>&#945;</mi><mn>8</mn></msup></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mi>&#946;</mi><mrow><mn>1</mn><mn>0</mn></mrow></msup><mo>-</mo><mn>2</mn><msup><mi>&#946;</mi><mn>8</mn></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>9</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>9</mn></msup></mrow></mfenced></mrow></mfrac></math></p><p><math> <mrow> <mo>=</mo> <mfrac> <mrow> <msup> <mi>&#945;</mi> <mn>8</mn> </msup> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mi>&#945;</mi> <mn>2</mn> </msup> <mo>-</mo> <mn>2</mn> </mrow> </mfenced> <mo>-</mo> <msup> <mi>&#946;</mi> <mn>8</mn> </msup> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mi>&#946;</mi> <mn>2</mn> </msup> <mo>-</mo> <mn>2</mn> </mrow> </mfenced> </mrow> <mrow> <mn>2</mn> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mi>&#945;</mi> <mn>9</mn> </msup> <mo>-</mo> <msup> <mi>&#946;</mi> <mn>9</mn> </msup> </mrow> </mfenced> </mrow> </mfrac> </mrow> </math></p><p><math> <mrow> <mo>=</mo> <mfrac> <mrow> <msup> <mi>&#945;</mi> <mn>8</mn> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mn>6</mn> <mi>&#945;</mi> </mrow> </mfenced> <mo>-</mo> <msup> <mi>&#946;</mi> <mn>8</mn> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mn>6</mn> <mi>&#946;</mi> </mrow> </mfenced> </mrow> <mrow> <mn>2</mn> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mi>&#945;</mi> <mn>9</mn> </msup> <mo>-</mo> <msup> <mi>&#946;</mi> <mn>9</mn> </msup> </mrow> </mfenced> </mrow> </mfrac> </mrow> </math>       [<math> <mrow> <mo>&#8757;</mo> </mrow> </math> From (1)]</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>6</mn><msup><mi>&#945;</mi><mn>9</mn></msup><mo>-</mo><mn>6</mn><msup><mi>&#946;</mi><mn>9</mn></msup></mrow><mrow><mn>2</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>9</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>9</mn></msup></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q109. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>5</mn></msqrt><mo>=</mo><mi>x</mi><mo>-</mo><mn>3</mn></math>, where <math> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>x</mi><mo>&#8289;</mo> </mrow> </math> is real, has

**Options:**

- **(A)** no solution
- **(B)** exactly four solutions
- **(C)** exactly one solution
- **(D)** exactly two solutions

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) no solution**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>5</mn></msqrt><mo>=</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>We know that for a quadratic expression <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> if discriminant i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>a</mi><mi>c</mi><mo>&#60;</mo><mn>0</mn><mo>,</mo></math> then the quadratic is always positive for all real values of the variable.</p><p>Now, consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>5</mn></math></p><p>We have, discriminant <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>a</mi><mi>c</mi><mo>=</mo><mn>1</mn><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>5</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>5</mn><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>Squaring <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>,</mo></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>5</mn><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>5</mn><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>4</mn><mi mathvariant="normal">,</mi><mo>&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>3</mn><mo>&#60;</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Hence, the equation has no solution.</p>

</details>

---

### Q110. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The sum of the roots of the equation, $\mathrm{x}^2+|2 \mathrm{x}-3|-4=0$, is:

**Options:**

- **(A)** 2
- **(B)** $-2$
- **(C)** $\sqrt{2}$
- **(D)** $-\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{2}$**

**Detailed Solution:**

$$
\begin{aligned}
&x^2+|2 x-3|-4=0 \\
&|2 x-3|=\left\{\begin{array}{lll}
(2 x-3) & \text { if } & \mathrm{x}>\frac{3}{2} \\
-(2 x-3) & \text { if } & \mathrm{x} < \frac{3}{2}
\end{array}\right.
\end{aligned}
$$

$$
\begin{aligned}
&\text { for } x>\frac{3}{2}, \quad x^2+2 x-3-4=0 \\
&x^2+2 x-7=0 \\
&x=\frac{-2 \pm \sqrt{4+28}}{2} \\
&=\frac{-2 \pm 4 \sqrt{2}}{2}=-1 \pm 2 \sqrt{2} \\
&\text { Here } x=2 \sqrt{2}-1 \\
&\left\{2 \sqrt{2}-1 < \frac{3}{2}\right\} \\
&\text { for } x < \frac{3}{2} \\
&x^2-2 x+3-4=0 \\
&\Rightarrow x^2-2 x-1=0 \\
&\Rightarrow x=\frac{2 \pm \sqrt{4+4}}{2}=\frac{2 \pm 2 \sqrt{2}}{2}=1 \pm \sqrt{2} \\
&\text { Here } x=1-\sqrt{2} \quad\left\{(1-\sqrt{2}) < \frac{3}{2}\right\}
\end{aligned}
$$
Sum of roots: $(2 \sqrt{2}-1)+(1-\sqrt{2})=\sqrt{2}$

</details>

---

### Q111. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If $\alpha$ and $\beta$ are roots of the equation, $x^2-4 \sqrt{2} k x+2 e^{4 \ln k}-1=0$ for some $k$, and $\alpha^2+\beta^2=66$, then $\alpha^3+\beta^3$ is equal to:

**Options:**

- **(A)** $248 \sqrt{2}$
- **(B)** $280 \sqrt{2}$
- **(C)** $-32 \sqrt{2}$
- **(D)** $-280 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-280 \sqrt{2}$**

**Detailed Solution:**

$x^2-4 \sqrt{2} k x+2 e^{4 \ln k}-1=0$ or, $x^2-4 \sqrt{2} k x+2 k^4-1=0$ $\alpha+\beta=4 \sqrt{2} k$ and $\alpha \cdot \beta=2 k^4-1$ Squaring both sides, we get
$$
\begin{aligned}
&(\alpha+\beta)^2=(4 \sqrt{2} k)^2 \\
&\Rightarrow \alpha^2+\beta^2+2 \alpha \beta=32 k^2 \\
&66+2 \alpha \beta=32 k^2 \\
&66+2\left(2 k^4-1\right)=32 k^2 \\
&66+4 k^4-2=32 k^2 \\
&\Rightarrow 4 k^4-32 k^2+64=0 \\
&\text { or, } k^4-8 k^2+16=0 \\
&\Rightarrow\left(k^2\right)^2-8 k^2+16=0 \\
&\Rightarrow\left(k^2-4\right)\left(k^2-4\right)=0 \\
&\Rightarrow k^2=4, k^2=4 \\
&\Rightarrow k=\pm 2
\end{aligned}
$$
Now, $\alpha^3+\beta^3=(\alpha+\beta)\left(\alpha^2+\beta^2-\alpha \beta\right)$
$$
\therefore \alpha^3+\beta^3=(4 \sqrt{2} k)\left[66-\left(2 k^4-1\right)\right]
$$
Putting $k=-2,(k=+2$ cannot be taken because it does not satisfy the above equation)
$\therefore \alpha^3+\beta^3=(4 \sqrt{2}(-2))\left[66-2(-2)^4-1\right]$
$\alpha^3+\beta^3=(-8 \sqrt{2})(66-32+1)=$
$(-8 \sqrt{2})(35)$
$\therefore \alpha^3+\beta^3=-280 \sqrt{2}$

</details>

---

### Q112. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mi>&#945;</mi></msqrt></mfrac><mo>,</mo><mfrac><mn>1</mn><msqrt><mi>&#946;</mi></msqrt></mfrac></math>  are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced></math>, then the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msup><mi>b</mi><mn>3</mn></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>a</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>a</mi><mi>b</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> has roots:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>&#945;</mi><mi>&#946;</mi></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><msup><mi>&#946;</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mi>&#946;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> has roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mi>&#945;</mi></msqrt></mfrac><mo>,</mo><mfrac><mn>1</mn><msqrt><mi>&#946;</mi></msqrt></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><mfrac><mn>1</mn><msqrt><mi>&#945;</mi></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><mi>&#946;</mi></msqrt></mfrac><mo>=</mo><mo>-</mo><mfrac><mi>b</mi><mi>a</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msqrt><mi>&#945;</mi></msqrt><msqrt><mi>&#946;</mi></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msup><mi>b</mi><mn>3</mn></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>a</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>a</mi><mi>b</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><msup><mi>b</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>a</mi><mi>b</mi></mrow></mfenced><mi>x</mi><mo>+</mo><msup><mi>a</mi><mn>3</mn></msup><mo>=</mo><mn>0</mn></math></p><p>Multiply and divide with <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>3</mn></msup></math>, we get

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>3</mn></msup><mfenced open="{" close="}"><mrow><mfenced><mfrac><msup><mi>b</mi><mn>3</mn></msup><msup><mi>a</mi><mn>3</mn></msup></mfrac></mfenced><mo>-</mo><mn>3</mn><mfrac><mn>1</mn><mi>a</mi></mfrac><mfenced><mfrac><mi>b</mi><mi>a</mi></mfrac></mfenced></mrow></mfenced><mi>x</mi><mo>+</mo><msup><mi>a</mi><mn>3</mn></msup><mo>=</mo><mn>0</mn></math>
From equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><msup><mfenced><mrow><msup><mi>&#945;</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><msup><mi>&#946;</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfenced><mn>3</mn></msup><msup><mfenced><msqrt><mi>&#945;</mi><mi>&#946;</mi></msqrt></mfenced><mn>3</mn></msup></mfrac><mo>-</mo><mn>3</mn><mfrac><mn>1</mn><msqrt><mi>&#945;</mi><mi>&#946;</mi></msqrt></mfrac><mfrac><mrow><msqrt><mi>&#945;</mi></msqrt><mo>+</mo><msqrt><mi>&#946;</mi></msqrt></mrow><msqrt><mi>&#945;</mi><mi>&#946;</mi></msqrt></mfrac></mrow></mfenced><mi>x</mi><mo>+</mo><msup><mfenced><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><msup><mi>&#945;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><msup><mi>&#946;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfenced><mi>x</mi><mo>+</mo><msup><mi>&#945;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mi>&#946;</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math>

Roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mtext>&#160;and&#160;</mtext><msup><mi>&#946;</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></math>.</p>

</details>

---

### Q113. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Let <math> <mrow> <mi>&#945;</mi> <mtext>&#160;and&#160;</mtext> <mi>&#946;</mi> </mrow> </math> be the roots of equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>q</mi><mi>x</mi><mo>+</mo><mi>r</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>&#8800;</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>,</mo><mo>&#160;</mo><mi>q</mi><mo>,</mo><mo>&#160;</mo><mi>r</mi><mo>&#160;</mo></math>are in A.P. and <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mi>&#945;</mi> </mrow> </mfrac> <mo>+</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mi>&#946;</mi> </mrow> </mfrac> <mo>=</mo> <mn>4</mn> </mrow> </math>, then the value of <math> <mrow> <mfenced close="|" open="|" separators=","> <mrow> <mi>&#945;</mi> <mo>-</mo> <mi>&#946;</mi> </mrow> </mfenced> </mrow> </math> is

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <msqrt> <mn>3</mn> <mn>4</mn> </msqrt> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mn>2</mn> <msqrt> <mn>1</mn> <mn>3</mn> </msqrt> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <msqrt> <mn>6</mn> <mn>1</mn> </msqrt> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>2</mn> <msqrt> <mn>1</mn> <mn>7</mn> </msqrt> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math> <mrow> <mfrac> <mrow> <mn>2</mn> <msqrt> <mn>1</mn> <mn>3</mn> </msqrt> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<p><math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mi>&#945;</mi> </mrow> </mfrac> <mo>+</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mi>&#946;</mi> </mrow> </mfrac> <mo>=</mo> <mn>4</mn> </mrow> </math>

   <math> <mrow> <mfrac> <mrow> <mi>&#945;</mi> <mo>+</mo> <mi>&#946;</mi> </mrow> <mrow> <mi>&#945;</mi> <mi>&#946;</mi> </mrow> </mfrac> <mo>=</mo> <mn>4</mn> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;&#160;</mo><mfrac><mrow><mo>-</mo><mfrac><mi>q</mi><mi>p</mi></mfrac></mrow><mfrac><mi>r</mi><mi>p</mi></mfrac></mfrac><mo>=</mo><mn>4</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;&#160;-</mo><mfrac><mi>q</mi><mi>r</mi></mfrac><mo>=</mo><mn>4</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>,</mo><mo>&#160;</mo><mi>q</mi><mo>,</mo><mo>&#160;</mo><mi>r</mi></math> are in A.P.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mi>a</mi><mo>-</mo><mi>d</mi><mo>&#160;</mo><mo>;</mo><mo>&#160;</mo><mi>q</mi><mo>=</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>r</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>d</mi></math>.

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;&#160;</mo><mfrac><mrow><mo>-</mo><mfenced><mi>a</mi></mfenced></mrow><mrow><mi>a</mi><mo>+</mo><mi>d</mi></mrow></mfrac><mo>=</mo><mn>4</mn><mo>&#160;&#160;&#8658;&#160;&#160;</mo><mo>-</mo><mi>a</mi><mo>=</mo><mn>4</mn><mi>a</mi><mo>+</mo><mn>4</mn><mi>d</mi><mo>&#160;&#160;&#8658;&#160;&#160;</mo><mi>d</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>5</mn><mi>a</mi></mrow><mn>4</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mi>a</mi><mo>+</mo><mfrac><mrow><mn>5</mn><mi>a</mi></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mn>9</mn><mi>a</mi></mrow><mn>4</mn></mfrac><mo>;</mo><mo>&#160;</mo><mi>q</mi><mo>=</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>r</mi><mo>=</mo><mi>a</mi><mo>-</mo><mfrac><mrow><mn>5</mn><mi>a</mi></mrow><mn>4</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mi>a</mi><mn>4</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;&#160;</mo><mfrac><mn>9</mn><mn>4</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>4</mn><mn>4</mn></mfrac><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;&#160;9</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

<math> <mrow> <msup> <mrow> <mfenced close="|" open="|" separators=","> <mrow> <mi>&#945;</mi> <mo>-</mo> <mi>&#946;</mi> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> <mo>=</mo> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#945;</mi> <mo>+</mo> <mi>&#946;</mi> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> <mo>-</mo> <mn>4</mn> <mi>&#945;</mi> <mi>&#946;</mi> </mrow> </math>

           <math> <mrow> <mo>=</mo> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mo>-</mo> <mn>4</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> <mo>-</mo> <mn>4</mn> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mtext>9</mtext> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>

           <math> <mrow> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> <mn>6</mn> </mrow> <mrow> <mn>8</mn> <mn>1</mn> </mrow> </mfrac> <mo>+</mo> <mfrac> <mrow> <mn>4</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>5</mn> <mn>2</mn> </mrow> <mrow> <mn>8</mn> <mn>1</mn> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <mo>&#8756;&#160;&#160;&#160;</mo> <mfenced close="|" open="|" separators=","> <mrow> <mi>&#945;</mi> <mo>-</mo> <mi>&#946;</mi> </mrow> </mfenced> <mo>=</mo> <mfrac> <mrow> <mn>2</mn> <msqrt> <mn>1</mn> <mn>3</mn> </msqrt> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </math>.</p><p>Hence, the correct answer is <math> <mrow> <mfrac> <mrow> <mn>2</mn> <msqrt> <mn>1</mn> <mn>3</mn> </msqrt> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </math>.</p>

</details>

---

### Q114. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mo>&#8712;&#160;</mo><mi>R</mi><mo>&#160;</mo></math> and the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn><mo>(</mo><mi>x</mi><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mo>[</mo><mi>x</mi><mo>]</mo><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>(</mo><mi>x</mi><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>)</mo><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn></math> (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> denotes the greatest integer <math> <mrow> <mo>&#8804;</mo> </mrow> </math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>x</mi></math>) has no integral solution, then all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> lie in the interval

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>)</mo></math>
- **(B)** <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mo></mo><mo>-</mo><mo>&infin;</mo> <mtext>,</mtext> <mo>-</mo> <mn>2</mn> </mrow> </mfenced> <mo>&cup;</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>2</mn> <mtext>,</mtext> <mo>&infin;</mo> </mrow> </mfenced> </mrow> </math>
- **(C)** <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mn>1</mn> <mtext>, </mtext> <mn>0</mn> </mrow> </mfenced> <mo>&cup;</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>0</mn> <mtext>, </mtext> <mn>1</mn> </mrow> </mfenced> </mrow> </math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mn>1</mn> <mtext>, </mtext> <mn>0</mn> </mrow> </mfenced> <mo>&cup;</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>0</mn> <mtext>, </mtext> <mn>1</mn> </mrow> </mfenced> </mrow> </math>**

**Detailed Solution:**

Let    <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>=</mo><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;&#160;-3</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>t</mi><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math>

As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is not an integer, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#8800;0</mo></math>     <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mi>a</mi><mo>&#8800;0</mo></math>

For a root of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> to exist at least one of the roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> should be between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>.

Roots    <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">=</mi><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#177;</mo><msqrt><mn>4</mn><mo>-</mo><mfenced><mn>4</mn></mfenced><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced><msup><mi>a</mi><mn>2</mn></msup></msqrt></mrow><mrow><mo>-</mo><mn>6</mn></mrow></mfrac></math>

              <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#177;</mo><msqrt><mn>4</mn><mo>+</mo><mn>1</mn><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></msqrt></mrow><mrow><mo>-</mo><mn>6</mn></mrow></mfrac></math>

              <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup></msqrt></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>&#8723;</mo><msqrt><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup></msqrt></mrow><mn>3</mn></mfrac></math>

As we observe, one root is surely less than zero,

i.e.,   <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup></msqrt></mrow><mn>3</mn></mfrac></math>

<math> <mrow> <mo>&#8756;</mo> </mrow> </math>   For a solution to exist,

       <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup></msqrt></mrow><mn>3</mn></mfrac><mo>&#60;</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;&#160;&#160;</mo><mn>1</mn><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup></msqrt><mo>&#60;</mo><mn>3</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;&#160;&#160;</mo><msqrt><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup></msqrt><mo>&#60;</mo><mn>2</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;&#160;&#160;</mo><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup><mo>&#60;</mo><mn>4</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;&#160;&#160;</mo><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup><mo>&#60;</mo><mn>3</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;&#160;&#160;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>&#60;</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;&#160;&#160;</mo><mi>a</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo largeop="true">&#8746;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>.     <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>&#8757;&#160;&#160;&#160;</mo><mi>a</mi><mo>&#8800;</mo><mn>0</mn></mrow></mfenced></math>

</details>

---

### Q115. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $p$ and $q$ are non-zero real numbers and $\alpha^3+\beta^3=-p, \alpha \beta=q$, then a quadratic equation whose roots are $\frac{\alpha^2}{\beta}, \frac{\beta^2}{\alpha}$ is :

**Options:**

- **(A)** $p x^2-q x+p^2=0$
- **(B)** $q x^2+p x+q^2=0$
- **(C)** $p x^2+q x+p^2=0$
- **(D)** $q x^2-p x+q^2=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $q x^2+p x+q^2=0$**

**Detailed Solution:**

Given $\alpha^3+\beta^3=-p$ and $\alpha \beta=q$
Let $\frac{\alpha^2}{\beta}$ and $\frac{\beta^2}{\alpha}$ be the root of required quadratic equation.
So, $\frac{\alpha^2}{\beta}+\frac{\beta^2}{\alpha}=\frac{\alpha^3+\beta^3}{\alpha \beta}=\frac{-p}{q}$
and $\frac{\alpha^2}{\beta} \times \frac{\beta^2}{\alpha}=\alpha \beta=q$
Hence, required quadratic equation is
$$
\begin{aligned}
&x^2-\left(\frac{-p}{q}\right) x+q=0 \\
&\Rightarrow x^2+\frac{p}{q} x+q=0 \Rightarrow q x^2+p x+q^2=0
\end{aligned}
$$

</details>

---

### Q116. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $\alpha$ and $\beta$ are roots of the equation $x^2+p x+\frac{3 p}{4}=0$, such that $|\alpha-\beta|=\sqrt{10}$, then $p$ belongs to the set :

**Options:**

- **(A)** $\{2,-5\}$
- **(B)** $\{-3,2\}$
- **(C)** $\{-2,5\}$
- **(D)** $\{3,-5\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\{-2,5\}$**

**Detailed Solution:**

Given quadratic eqn. is
$$
x^2+p x+\frac{3 p}{4}=0
$$
So, $\alpha+\beta=-p, \alpha \beta=\frac{3 p}{4}$
Now, given $|\alpha-\beta|=\sqrt{10}$
$$
\begin{aligned}
& \Rightarrow \alpha-\beta=\pm \sqrt{10} \\
& \Rightarrow(\alpha-\beta)^2=10 \Rightarrow \alpha^2+\beta^2-2 \alpha \beta=10 \\
& \Rightarrow(\alpha+\beta)^2-4 \alpha \beta=10 \\
& \Rightarrow p^2-4 \times \frac{3 p}{4}=10 \Rightarrow p^2-3 p-10=0 \\
& \Rightarrow p=-2,5 \Rightarrow p \in\{-2,5\}
\end{aligned}
$$

</details>

---

### Q117. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The values of ' $a$ ' for which one root of the equation $x^2-(a+1) x+a^2+a-8=0$ exceeds 2 and the other is lesser than 2 , are given by :

**Options:**

- **(A)** $3 < a < 10$
- **(B)** $a \geq 10$
- **(C)** $-2 < a < 3$
- **(D)** $a \leq-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-2 < a < 3$**

**Detailed Solution:**

$$
x^2-(a+1) x+a^2+a-8=0
$$
Since roots are different, therefore $\mathrm{D}>0$
$$
\begin{aligned}
& \Rightarrow(a+1)^2-4\left(a^2+a-8\right)>0 \\
& \Rightarrow(a-3)(3 a+1) < 0
\end{aligned}
$$
There are two cases arises.
Case I. $a-3>0$ and $3 a+1 < 0$
$\Rightarrow a>3$ and $a < -\frac{11}{3}$
Hence, no solution in this case
Case II : $a-3 < 0$ and $3 a+11>0$
$\Rightarrow a < 3$ and $a>-\frac{11}{3}$
$\therefore \quad-\frac{11}{3} < a < 3 \Rightarrow-2 < a < 3$

</details>

---

### Q118. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If $a, b, c \in \mathrm{R}$ and 1 is a root of equation $a x^2+b x$ $+c=0$, then the curve $y=4 a x^2+3 b x+2 c, a \neq 0$ intersect $x$-axis at

**Options:**

- **(A)** two distinct points whose coordinates are always rational numbers
- **(B)** no point
- **(C)** exactly two distinct points
- **(D)** exactly one point

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) exactly one point**

**Detailed Solution:**

Given $a x^2+b x+c=0$
$$
\begin{aligned}
& \Rightarrow a x^2=-b x-c \\
& \text { Now, consider } \\
& y=4 a x^2+3 b x+2 c \\
& =4[-b x-c]+3 b x+2 c \\
& =-4 b x-4 c+3 b x+2 c \\
& =-b x-2 c
\end{aligned}
$$
Since, this curve intersects $x$-axis
$\therefore$ put $y=0$, we get
$$
\begin{aligned}
& -b x-2 c=0 \Rightarrow-b x=2 c \\
& \Rightarrow x=\frac{-2 c}{b}
\end{aligned}
$$
Thus, given curve intersects $x$-axis at exactly one point.

</details>

---

### Q119. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Let $p, q, r \in R$ and $r>p>0$. If the quadratic equation $p x^2+q x+r=0$ has two complex roots $\alpha$ and $\beta$, then $|\alpha|+|\beta|$ is

**Options:**

- **(A)** equal to 1
- **(B)** less than 2 but not equal to 1
- **(C)** greater than 2
- **(D)** equal to 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) greater than 2**

**Detailed Solution:**

Given quadratic equation is
$$
\begin{aligned}
& p x^2+q x+r=0 \\
& D=q^2-4 p r
\end{aligned}
$$
Since $\alpha$ and $\beta$ are two complex root
$$
\begin{array}{ll}
\therefore \beta=\bar{\alpha} \Rightarrow|\beta|=|\bar{\alpha}| \Rightarrow|\beta|=|\alpha| \\
(\because|\bar{\alpha}|=|\alpha|) \\
\text { Consider } \\
|\alpha|+|\beta|=|\alpha|+|\alpha| & (\because|\beta|=|\alpha|) \\
=2|\alpha|>2.1=2 & (\because|\alpha|>1)
\end{array}
$$
Hence, $|\alpha|+|\beta|$ is greater than 2 .

</details>

---

### Q120. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `1`

If the sum of the square of the roots of the equation $x^2-(\sin \alpha-2) x-(1+\sin \alpha)=0$ is least, then $\alpha$ is equal to

**Options:**

- **(A)** $\frac{\pi}{6}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{2}$**

**Detailed Solution:**

Given equation is
$$
x^2-(\sin \alpha-2) x-(1+\sin \alpha)=0
$$
Let $x_1$ and $x_2$ be two roots of quadratic equation.
$$
\begin{aligned}
& \therefore x_1+x_2=\sin \alpha-2 \text { and } x_1 x_2=-(1+\sin \alpha) \\
& \left(x_1+x_2\right)^2=(\sin \alpha-2)^2=\sin ^2 \alpha+4-4 \sin \alpha
\end{aligned}
$$
$$
\begin{aligned}
& \Rightarrow \quad x_1^2+x_2^2=\sin ^2 \alpha+4-4 \sin \alpha-2 x_1 x_2 \\
& =\sin ^2 \alpha+4-4 \sin \alpha+2(1+\sin \alpha) \\
& =\sin ^2 \alpha-2 \sin \alpha+6
\end{aligned}
$$
Now, By putting
$\alpha=\frac{\pi}{6}, \alpha=\frac{\pi}{4}, \alpha=\frac{\pi}{3}$ and $\alpha=\frac{\pi}{2}$ in (A) one by one
We get least value of $x_1^2+x_2^2$ at $\frac{\pi}{2}$
Hence, $\alpha=\frac{\pi}{2}$

</details>

---

### Q121. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\mathrm{k}$ for which the equation $(K-2) x^2+8 x+K+4=0$ has both roots real, distinct and negative is

**Options:**

- **(A)** 6
- **(B)** 3
- **(C)** 4
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3**

**Detailed Solution:**

$(K-2) x^2+8 x+K+4=0$
If real roots then,
$$
\begin{aligned}
& 8^2-4(K-2)(K+4)>0 \\
\Rightarrow & K^2+2 K-8 < 16 \\
\Rightarrow & K^2+6 K-4 K-24 < 0 \\
\Rightarrow & (K+6)(K-4) < 0 \\
\Rightarrow & -6 < K < 4
\end{aligned}
$$
If both roots are negative then $\alpha \beta$ is $+v e$
$$
\begin{aligned}
& \Rightarrow \frac{K+4}{K-2}>0 \Rightarrow K>-4 \\
& \text { Also, } \frac{K-2}{K+4}>0 \Rightarrow K>2
\end{aligned}
$$
Roots are real so, $-6 < K < 4$
So, 6 and 4 are not correct.
Since, $K>2$, so 1 is also not correct value of $K$.
$$
\therefore K=3
$$

</details>

---

### Q122. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `1`

If $\alpha$ and $\beta$ are the roots of the equation $x^2-x+1=0$, then $\alpha^{2009}+\beta^{2009}=$

**Options:**

- **(A)** $-1$
- **(B)** 1
- **(C)** 2
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

$x^2-x+1=0 \quad \Rightarrow x=\frac{1 \pm \sqrt{1-4}}{2}$
$x=\frac{1 \pm \sqrt{3} i}{2}$
$\alpha=\frac{1}{2}+i \frac{\sqrt{3}}{2}, \quad \beta=\frac{1}{2}-\frac{i \sqrt{3}}{2}$
$\alpha=\cos \frac{\pi}{3}+i \sin \frac{\pi}{3}, \quad \beta=\cos \frac{\pi}{3}-i \sin \frac{\pi}{3}$
$\alpha^{2009}+\beta^{2009}=2 \cos 2009\left(\frac{\pi}{3}\right)$
$=2 \cos \left[668 \pi+\pi+\frac{2 \pi}{3}\right]=2 \cos \left(\pi+\frac{2 \pi}{3}\right)$
$=-2 \cos \frac{2 \pi}{3}=-2\left(-\frac{1}{2}\right)=1$

</details>

---

### Q123. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `1`

If the roots of the equation $b x^2+c x+a=0$ be imaginary, then for all real values of $x$, the expression $3 b^2 x^2+6 b c x+2 c^2$ is

**Options:**

- **(A)** greater than $4 a b$
- **(B)** less than $4 a b$
- **(C)** greater than $-4 a b$
- **(D)** less than - 4ab

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) greater than $-4 a b$**

**Detailed Solution:**

$$
b x^2+c x+a=0
$$
Roots are imaginary $\Rightarrow c^2-4 a b < 0 \Rightarrow c^2 < 4 a b \Rightarrow-c^2>-4 a b$ $3 b^2 x^2+6 b c x+2 c^2$
since $3 b^2>0$
Given expression has minimum value
Minimum value $=\frac{4\left(3 b^2\right)\left(2 c^2\right)-36 b^2 c^2}{4\left(3 b^2\right)}=-\frac{12 b^2 c^2}{12 b^2}=-c^2>-4 a b$.

</details>

---

### Q124. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

If the roots of the quadratic equation $x^2+p x+q=0$ are $\tan 30^{\circ}$ and $\tan 15^{\circ}$, respectively then the value of $2+q-p$ is

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** 0
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3**

**Detailed Solution:**

$x^2+p x+q=0$
$\tan 30^{\circ}+\tan 15^{\circ}=-p$
$\tan 30^{\circ} \cdot \tan 15^{\circ}=q$
$\tan 45^{\circ}=\frac{\tan 30^{\circ}+\tan 15^{\circ}}{1-\tan 30^{\circ} \tan 15^{\circ}}=\frac{-p}{1-q}=1$
$\Rightarrow-p=1-q$
$\Rightarrow q-p=1 \quad \therefore 2+q-p=3$.

</details>

---

### Q125. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

If roots of the equation $x^2-b x+c=0$ be two consectutive integers, then $b^2-4 c$ equals

**Options:**

- **(A)** $-2$
- **(B)** 3
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

Let $\alpha, \alpha+1$ be roots
$$
\begin{aligned}
& \alpha+\alpha+1=b \\
& \alpha(\alpha+1)=c \\
& \therefore b^2-4 c=(2 \alpha+1)^2-4 \alpha(\alpha+1)=1 .
\end{aligned}
$$

</details>

---

### Q126. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

The value of $\alpha$ for which the sum of the squares of the roots of the equation $x^2-(a-2) x-a-1=0$ assume the least value is

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** 3
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$$
\begin{aligned}
& x^2-(a-2) x-a-1=0 \\
& \Rightarrow \alpha+\beta=a-2 \\
& \alpha \beta=-(a+1) \\
& \alpha^2+\beta^2=(\alpha+\beta)^2-2 \alpha \beta \\
& \quad=a^2-2 a+6=(a-1)^2+5 \\
& \Rightarrow a=1 .
\end{aligned}
$$

</details>

---

### Q127. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

If one root of the equation $x^2+p x+12=0$ is 4 , while the equation $x^2+p x+q=0$ has equal roots, then the value of ' $q$ ' is

**Options:**

- **(A)** $\frac{49}{4}$
- **(B)** 4
- **(C)** 3
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{49}{4}$**

**Detailed Solution:**

Since 4 is one of the root of $x^2+p x+12=0 \Rightarrow 16+4 p+12=0 \Rightarrow p=-7$ and equation $x^2+p x+q=0$ has equal roots
$$
\Rightarrow D=49-4 q=0 \Rightarrow q=\frac{49}{4}
$$

</details>

---

### Q128. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

If $(1-p)$ is a root of quadratic equation $x^2+p x+(1-p)=0$, then its roots are

**Options:**

- **(A)** 0,1
- **(B)** $-1,2$
- **(C)** $0,-1$
- **(D)** $-1,1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0,-1$**

**Detailed Solution:**

(3)
$$
\begin{aligned}
& (1-p)^2+p(1-p)+(1-p)=0 \quad\left(\text { since }(1-p) \text { is a root of the equation } x^2+p x+(1-p)=0\right) \\
& \Rightarrow(1-p)(1-p+p+1)=0 \\
& \Rightarrow 2(1-p)=0 \Rightarrow(1-p)=0 \Rightarrow p=1 \\
& \text { sum of root is } \alpha+\beta=-p \text { and product } \alpha \beta=1-p=0 \quad \text { (where } \beta=1-p=0) \\
& \Rightarrow \alpha+0=-1 \Rightarrow \alpha=-1 \Rightarrow \text { Roots are } 0,-1
\end{aligned}
$$

</details>

---

### Q129. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

Let two numbers have arithmetic mean 9 and geometric mean 4. Then these numbers are the roots of the quadratic equation

**Options:**

- **(A)** $x^2+18 x+16=0$
- **(B)** $x^2-18 x-16=0$
- **(C)** $x^2+18 x-16=0$
- **(D)** $x^2-18 x+16=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x^2-18 x+16=0$**

**Detailed Solution:**

Let numbers be $a, b \Rightarrow a+b=18, \sqrt{a b}=4 \quad \Rightarrow a b=16, a$ and $b$ are roots of the equation
$\Rightarrow \quad x^2-18 x+16=0$

</details>

---

### Q130. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

The number of real solutions of the equation $x^2-3|x|+2=0$ is

**Options:**

- **(A)** 3
- **(B)** 2
- **(C)** 4
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

$x^2-3|x|+2=0 \quad$ or $(|x|-2)(|x|-1)=0$
$|x|=1,2$ or $x=\pm 1, \pm 2$ or $\therefore$ No. of solution $=4$

</details>

---

### Q131. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

The value of ' $a$ ' for which one root of the quadratic equation $\left(a^2-5 a+3\right) x^3+(3 a-1) x+2=0$ is twice as large as the other is

**Options:**

- **(A)** $-\frac{1}{3}$
- **(B)** $\frac{2}{3}$
- **(C)** $-\frac{2}{3}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{3}$**

**Detailed Solution:**

$3 \alpha=\frac{1-3 a}{a^2-5 a+3} \& 2 \alpha^2=\frac{2}{a^2-5 a+3}$
$2\left[\frac{1}{9} \frac{(1-3 a)^2}{\left(a^2-5 a+3\right)^2}\right]=\frac{2}{a^2-5 a+3}$
$\frac{(1-3 a)^2}{\left(a^2-5 a+3\right)}=9$ or $9 a^2-6 a+1$
$=9 a^2-45 a+27$ or $39 a=26$ or $a=\frac{2}{3}$

</details>

---

### Q132. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

If the sum of the roots of the quadratic equation $a x^2+b x+c=0$ is equal to the sum of the squares of their reciprocals, then $\frac{\mathrm{a}}{\mathrm{c}}, \frac{\mathrm{b}}{\mathrm{a}}$ and $\frac{\mathrm{c}}{\mathrm{b}}$ are in

**Options:**

- **(A)** Arithmetic - Geometric Progression
- **(B)** Arithmetic Progression
- **(C)** Geometric Progression
- **(D)** Harmonic Progression

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Harmonic Progression**

**Detailed Solution:**

$a x^2+b x+c=0, \alpha+\beta=\frac{-b}{a}, \alpha \beta=\frac{c}{a}$
As for given condition, $\alpha+\beta=\frac{1}{\alpha^2}+\frac{1}{\beta^2}$
$\alpha+\beta=-\frac{\alpha^2+\beta^2}{\alpha^2 \beta^2}-\frac{b}{a}=\frac{\frac{b^2}{a^2}-\frac{2 c}{a}}{\frac{c^2}{a^2}}$
On simplification $2 a^2 c=a b^2+b c^2$
$\Rightarrow \frac{2 \mathrm{a}}{\mathrm{b}}=\frac{\mathrm{c}}{\mathrm{a}}+\frac{\mathrm{b}}{\mathrm{c}} \quad \therefore \frac{\mathrm{a}}{\mathrm{b}}, \frac{\mathrm{b}}{\mathrm{a}}, \& \frac{\mathrm{c}}{\mathrm{b}}$ are in H.P.

</details>

---

### Q133. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

If $p$ and $q$ are the roots of the equation $x^2+p x+q=0$, then

**Options:**

- **(A)** p =1, q = -2
- **(B)** p = 0, q = 1
- **(C)** p = -2, q = 0
- **(D)** p = -2, q = 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) p =1, q = -2**

**Detailed Solution:**

$p+q=-p$ and $p q=q \Rightarrow q(p-1)=0 \Rightarrow q=0$ or $p=1$
If $q=0$, then $p=0$. i.e. $p=q \quad \therefore p=1$ and $q=-2$

</details>

---

### Q134. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

Product of real roots of the equation $t^2 x^2+|x|+9=0$

**Options:**

- **(A)** is always positive
- **(B)** is always negative
- **(C)** does not exist
- **(D)** none of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) does not exist**

**Detailed Solution:**

No Solution Available

</details>

---

### Q135. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `1`

If $\alpha \neq \beta$ but $\alpha^2=5 \alpha-3$ and $\beta^2=5 \beta-3$ then the equation having $\alpha / \beta$ and $\beta / \alpha$ as its roots is

**Options:**

- **(A)** $3 x^2-19 x+3=0$
- **(B)** $3 x^2+19 x-3=0$
- **(C)** $3 x^2-19 x-3=0$
- **(D)** $x^2-5 x+3=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3 x^2-19 x+3=0$**

**Detailed Solution:**

We have $\alpha^2=5 \alpha-3$
$$
\begin{aligned}
& \Rightarrow \alpha^2-5 \alpha+3=0 \Rightarrow \alpha=\frac{5 \pm \sqrt{13}}{2} \text {. Similarly, } \beta^2=5 \beta-3 \Rightarrow \alpha=\frac{5 \pm \sqrt{13}}{2} \\
& \therefore \alpha=\frac{5+\sqrt{13}}{2} \text { and } \beta=\frac{5-\sqrt{13}}{2} \text { or vice - versa } \\
& \alpha^2+\beta^2=\frac{50+26}{4}=19 \& \alpha \beta=\frac{1}{4}(25-13)=3
\end{aligned}
$$
Thus, the equation having $\frac{\alpha}{\beta} \& \frac{\beta}{\alpha}$ as its roots is
$$
x^2-x\left(\frac{\alpha}{\beta}+\frac{\beta}{\alpha}\right)+\frac{\alpha \beta}{\alpha \beta}=0 \Rightarrow x^2-x\left(\frac{\alpha^2+\beta^2}{\alpha \beta}\right)+1=0 \text { or } 3 x^2-19 x+1=0
$$

</details>

---

