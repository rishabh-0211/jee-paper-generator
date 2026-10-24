# JEE Main Mathematics - Three Dimensional Geometry

## Topic 3: Line in Space

**Total Questions:** 183

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `numerical` | *Level:* `2`

Let a line $L_1$ pass through the origin and be perpendicular to the lines
$L_2: \vec{r} = (3+t)\hat{i} + (2t-1)\hat{j} + (2t+4)\hat{k}$ and
$L_3: \vec{r} = (3+2s)\hat{i} + (3+2s)\hat{j} + (2+s)\hat{k}$, $t, s \in \mathbb{R}$.
If $(a, b, c)$, $a \in \mathbb{Z}$, is the point on $L_3$ at a distance of $\sqrt{17}$ from the point of intersection of $L_1$ and $L_2$, then $(a+b+c)^2$ is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

The direction vectors of the given lines $L_2$ and $L_3$ are $\vec{d_2} = \hat{i} + 2\hat{j} + 2\hat{k}$ and $\vec{d_3} = 2\hat{i} + 2\hat{j} + \hat{k}$ respectively.

Since line $L_1$ is perpendicular to both $L_2$ and $L_3$, its direction vector $\vec{d_1}$ is given by the cross product of $\vec{d_2}$ and $\vec{d_3}$:
$\vec{d_1} = \vec{d_2} \times \vec{d_3} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & 2 \\ 2 & 2 & 1 \end{vmatrix} = -2\hat{i} + 3\hat{j} - 2\hat{k}$

Since $L_1$ passes through the origin, its equation is:
$\vec{r} = \lambda(-2\hat{i} + 3\hat{j} - 2\hat{k})$

Let the point of intersection of $L_1$ and $L_2$ be $P$. The coordinates of $P$ can be written as $(-2\lambda, 3\lambda, -2\lambda)$ from $L_1$ and $(3+t, 2t-1, 2t+4)$ from $L_2$. Equating the respective coordinates:
$-2\lambda = 3 + t$
$3\lambda = 2t - 1$
$-2\lambda = 2t + 4$

From the first and third equations, we get:
$3 + t = 2t + 4 \Rightarrow t = -1$

Substituting $t = -1$ into the first equation gives $-2\lambda = 2 \Rightarrow \lambda = -1$. This also satisfies the second equation. Thus, the point of intersection is $P(2, -3, 2)$.

Let the point on $L_3$ be $Q(a, b, c) = (3+2s, 3+2s, 2+s)$. The distance between $P$ and $Q$ is given as $\sqrt{17}$.
$PQ^2 = 17$
$(3+2s - 2)^2 + (3+2s - (-3))^2 + (2+s - 2)^2 = 17$
$(2s + 1)^2 + (2s + 6)^2 + s^2 = 17$
$4s^2 + 4s + 1 + 4s^2 + 24s + 36 + s^2 = 17$
$9s^2 + 28s + 37 = 17$
$9s^2 + 28s + 20 = 0$
$9s^2 + 18s + 10s + 20 = 0$
$(9s + 10)(s + 2) = 0$

This gives $s = -2$ or $s = -\dfrac{10}{9}$.

Since $a = 3 + 2s$ must be an integer ($a \in \mathbb{Z}$), we must choose $s = -2$.

Substituting $s = -2$ into the coordinates of $Q$:
$a = 3 + 2(-2) = -1$
$b = 3 + 2(-2) = -1$
$c = 2 + (-2) = 0$

Therefore, $(a, b, c) = (-1, -1, 0)$.

We need to find the value of $(a+b+c)^2$:
$(a+b+c)^2 = (-1 - 1 + 0)^2 = (-2)^2 = 4$

Answer: $4$

</details>

---

### Q2. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the foot of perpendicular from the point $(\lambda, 2, 3)$ on the line $\dfrac{x-4}{1} = \dfrac{y-9}{2} = \dfrac{z-5}{1}$ be the point $(1, \mu, 2)$. Then the distance between the lines $\dfrac{x-1}{2} = \dfrac{y-2}{3} = \dfrac{z+4}{6}$ and $\dfrac{x-\lambda}{2} = \dfrac{y-\mu}{3} = \dfrac{z+5}{6}$ is equal to:

**Options:**

- **(A)** $\dfrac{12}{7}$
- **(B)** $\dfrac{\sqrt{145}}{7}$
- **(C)** $\dfrac{\sqrt{146}}{7}$
- **(D)** $\dfrac{\sqrt{143}}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\sqrt{146}}{7}$**

**Detailed Solution:**

Since the point $(1, \mu, 2)$ lies on the line $\dfrac{x-4}{1} = \dfrac{y-9}{2} = \dfrac{z-5}{1}$, we substitute its coordinates into the line equation:

$\dfrac{1-4}{1} = \dfrac{\mu-9}{2} = \dfrac{2-5}{1}$

$-3 = \dfrac{\mu-9}{2} = -3 \Rightarrow \mu - 9 = -6 \Rightarrow \mu = 3$

The direction ratios of the given line are $(1, 2, 1)$. The direction ratios of the perpendicular from $(\lambda, 2, 3)$ to $(1, 3, 2)$ are $(1-\lambda, 3-2, 2-3) = (1-\lambda, 1, -1)$.

Since the lines are perpendicular, their dot product is zero:

$1(1-\lambda) + 2(1) + 1(-1) = 0$

$1 - \lambda + 2 - 1 = 0 \Rightarrow \lambda = 2$

Substituting $\lambda = 2$ and $\mu = 3$ into the equations of the two lines, we get:

$L_1: \dfrac{x-1}{2} = \dfrac{y-2}{3} = \dfrac{z+4}{6}$

$L_2: \dfrac{x-2}{2} = \dfrac{y-3}{3} = \dfrac{z+5}{6}$

These are parallel lines with direction vector $\vec{b} = 2\hat{i} + 3\hat{j} + 6\hat{k}$. The lines pass through the points $\vec{a}_1 = \hat{i} + 2\hat{j} - 4\hat{k}$ and $\vec{a}_2 = 2\hat{i} + 3\hat{j} - 5\hat{k}$ respectively.

The distance $d$ between two parallel lines is given by $d = \dfrac{|(\vec{a}_2 - \vec{a}_1) \times \vec{b}|}{|\vec{b}|}$.

We have $\vec{a}_2 - \vec{a}_1 = (2-1)\hat{i} + (3-2)\hat{j} + (-5 - (-4))\hat{k} = \hat{i} + \hat{j} - \hat{k}$.

Now, we compute the cross product:

$(\vec{a}_2 - \vec{a}_1) \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & -1 \\ 2 & 3 & 6 \end{vmatrix}$

$= \hat{i}(6 - (-3)) - \hat{j}(6 - (-2)) + \hat{k}(3 - 2) = 9\hat{i} - 8\hat{j} + \hat{k}$

The magnitude of this vector is:

$|9\hat{i} - 8\hat{j} + \hat{k}| = \sqrt{9^2 + (-8)^2 + 1^2} = \sqrt{81 + 64 + 1} = \sqrt{146}$

The magnitude of the direction vector $\vec{b}$ is:

$|\vec{b}| = \sqrt{2^2 + 3^2 + 6^2} = \sqrt{4 + 9 + 36} = \sqrt{49} = 7$

Therefore, the distance between the lines is:

$d = \dfrac{\sqrt{146}}{7}$

Answer: $\dfrac{\sqrt{146}}{7}$

</details>

---

### Q3. JEE Main 2026 (06 April Shift 2)

*Type:* `numerical` | *Level:* `3`

Let the image of the point $P(0, -5, 0)$ in the line $\dfrac{x-1}{2} = \dfrac{y}{1} = \dfrac{z+1}{-2}$ be the point $R$ and the image of the point $Q\left(0, \dfrac{-1}{2}, 0\right)$ in the line $\dfrac{x-1}{-1} = \dfrac{y+9}{4} = \dfrac{z+1}{1}$ be the point $S$. Then the square of the area of the parallelogram $PQRS$ is __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **162**

**Detailed Solution:**

Let $M_1$ be the foot of the perpendicular from $P(0, -5, 0)$ to the first line $L_1: \dfrac{x-1}{2} = \dfrac{y}{1} = \dfrac{z+1}{-2}$.
A general point on $L_1$ is $M_1(2\lambda + 1, \lambda, -2\lambda - 1)$.
The direction ratios of $PM_1$ are $(2\lambda + 1, \lambda + 5, -2\lambda - 1)$.
Since $PM_1$ is perpendicular to $L_1$, their dot product is zero:
$2(2\lambda + 1) + 1(\lambda + 5) - 2(-2\lambda - 1) = 0$
$4\lambda + 2 + \lambda + 5 + 4\lambda + 2 = 0 \Rightarrow 9\lambda + 9 = 0 \Rightarrow \lambda = -1$
Thus, $M_1$ is $(-1, -1, 1)$.

Let $M_2$ be the foot of the perpendicular from $Q\left(0, \dfrac{-1}{2}, 0\right)$ to the second line $L_2: \dfrac{x-1}{-1} = \dfrac{y+9}{4} = \dfrac{z+1}{1}$.
A general point on $L_2$ is $M_2(-\mu + 1, 4\mu - 9, \mu - 1)$.
The direction ratios of $QM_2$ are $\left(-\mu + 1, 4\mu - \dfrac{17}{2}, \mu - 1\right)$.
Since $QM_2$ is perpendicular to $L_2$, their dot product is zero:
$-1(-\mu + 1) + 4\left(4\mu - \dfrac{17}{2}\right) + 1(\mu - 1) = 0$
$\mu - 1 + 16\mu - 34 + \mu - 1 = 0 \Rightarrow 18\mu - 36 = 0 \Rightarrow \mu = 2$
Thus, $M_2$ is $(-1, -1, 1)$.

Since $M_1$ and $M_2$ are the same point $M(-1, -1, 1)$, the diagonals $PR$ and $QS$ of the quadrilateral $PQRS$ bisect each other at $M$. Therefore, $PQRS$ is a parallelogram.

The area of the parallelogram is given by $\dfrac{1}{2} |\overrightarrow{PR} \times \overrightarrow{QS}|$.
We have:
$\overrightarrow{PR} = 2\overrightarrow{PM} = 2(-1 - 0, -1 - (-5), 1 - 0) = (-2, 8, 2)$
$\overrightarrow{QS} = 2\overrightarrow{QM} = 2\left(-1 - 0, -1 - \left(\dfrac{-1}{2}\right), 1 - 0\right) = (-2, -1, 2)$

Now, compute the cross product $\overrightarrow{PR} \times \overrightarrow{QS}$:
$\overrightarrow{PR} \times \overrightarrow{QS} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ -2 & 8 & 2 \\ -2 & -1 & 2 \end{vmatrix} = \hat{i}(16 - (-2)) - \hat{j}(-4 - (-4)) + \hat{k}(2 - (-16)) = 18\hat{i} + 18\hat{k}$

The area of the parallelogram is:
$\text{Area} = \dfrac{1}{2} |18\hat{i} + 18\hat{k}| = \dfrac{1}{2} \sqrt{18^2 + 18^2} = \dfrac{18\sqrt{2}}{2} = 9\sqrt{2}$

The square of the area is $(9\sqrt{2})^2 = 162$.

Answer: $162$

</details>

---

### Q4. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The shortest distance between the lines $\dfrac{x-4}{1} = \dfrac{y-3}{2} = \dfrac{z-2}{-3}$ and $\dfrac{x+2}{2} = \dfrac{y-6}{4} = \dfrac{z-5}{-5}$ is :

**Options:**

- **(A)** $\dfrac{5\sqrt{6}}{6}$
- **(B)** $2\sqrt{5}$
- **(C)** $3\sqrt{5}$
- **(D)** $4\sqrt{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3\sqrt{5}$**

**Detailed Solution:**

The given lines are $L_1: \dfrac{x-4}{1} = \dfrac{y-3}{2} = \dfrac{z-2}{-3}$ and $L_2: \dfrac{x+2}{2} = \dfrac{y-6}{4} = \dfrac{z-5}{-5}$.

For $L_1$, a point on the line is $\vec{a}_1 = 4\hat{i} + 3\hat{j} + 2\hat{k}$ and its direction vector is $\vec{b}_1 = \hat{i} + 2\hat{j} - 3\hat{k}$.

For $L_2$, a point on the line is $\vec{a}_2 = -2\hat{i} + 6\hat{j} + 5\hat{k}$ and its direction vector is $\vec{b}_2 = 2\hat{i} + 4\hat{j} - 5\hat{k}$.

The shortest distance $d$ between two skew lines is given by $d = \dfrac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|}$.

We have $\vec{a}_2 - \vec{a}_1 = (-2 - 4)\hat{i} + (6 - 3)\hat{j} + (5 - 2)\hat{k} = -6\hat{i} + 3\hat{j} + 3\hat{k}$.

The cross product of the direction vectors is:

$\vec{b}_1 \times \vec{b}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & -3 \\ 2 & 4 & -5 \end{vmatrix} = \hat{i}(-10 + 12) - \hat{j}(-5 + 6) + \hat{k}(4 - 4) = 2\hat{i} - \hat{j}$.

The magnitude of the cross product is $|\vec{b}_1 \times \vec{b}_2| = \sqrt{2^2 + (-1)^2 + 0^2} = \sqrt{5}$.

The dot product is $(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2) = (-6)(2) + (3)(-1) + (3)(0) = -12 - 3 = -15$.

Therefore, the shortest distance is $d = \dfrac{|-15|}{\sqrt{5}} = \dfrac{15}{\sqrt{5}} = 3\sqrt{5}$.

Answer: $3\sqrt{5}$

</details>

---

### Q5. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let a line $L$ be perpendicular to both the lines $L_1: \dfrac{x+1}{3} = \dfrac{y+3}{5} = \dfrac{z+5}{7}$ and $L_2: \dfrac{x-2}{1} = \dfrac{y-4}{4} = \dfrac{z-6}{7}$. If $\theta$ is the acute angle between the lines $L$ and $L_3: \dfrac{x - \dfrac{8}{7}}{2} = \dfrac{y - \dfrac{4}{7}}{1} = \dfrac{z}{2}$, then $\tan\theta$ is equal to:

**Options:**

- **(A)** $\dfrac{3}{2}\sqrt{2}$
- **(B)** $\dfrac{5}{2}\sqrt{2}$
- **(C)** $\dfrac{5}{3}\sqrt{2}$
- **(D)** $\dfrac{4}{3}\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{5}{2}\sqrt{2}$**

**Detailed Solution:**

The direction vector of line $L_1$ is $\vec{d_1} = 3\hat{i} + 5\hat{j} + 7\hat{k}$.

The direction vector of line $L_2$ is $\vec{d_2} = \hat{i} + 4\hat{j} + 7\hat{k}$.

Since line $L$ is perpendicular to both $L_1$ and $L_2$, its direction vector $\vec{d}$ is given by the cross product of $\vec{d_1}$ and $\vec{d_2}$:

$\vec{d} = \vec{d_1} \times \vec{d_2} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 3 & 5 & 7 \\ 1 & 4 & 7 \end{vmatrix}$

$\vec{d} = \hat{i}(35 - 28) - \hat{j}(21 - 7) + \hat{k}(12 - 5) = 7\hat{i} - 14\hat{j} + 7\hat{k}$

The direction ratios of $L$ are proportional to $1, -2, 1$.

The direction vector of line $L_3$ is $\vec{d_3} = 2\hat{i} + \hat{j} + 2\hat{k}$.

The acute angle $\theta$ between $L$ and $L_3$ is given by:

$\cos\theta = \dfrac{|\vec{d} \cdot \vec{d_3}|}{|\vec{d}| |\vec{d_3}|}$

$\cos\theta = \dfrac{|(1)(2) + (-2)(1) + (1)(2)|}{\sqrt{1^2 + (-2)^2 + 1^2} \sqrt{2^2 + 1^2 + 2^2}}$

$\cos\theta = \dfrac{|2 - 2 + 2|}{\sqrt{6} \sqrt{9}} = \dfrac{2}{3\sqrt{6}}$

From $\cos\theta = \dfrac{2}{3\sqrt{6}}$, considering a right-angled triangle with adjacent side $2$ and hypotenuse $3\sqrt{6}$:

The opposite side is $\sqrt{(3\sqrt{6})^2 - 2^2} = \sqrt{54 - 4} = \sqrt{50} = 5\sqrt{2}$.

Therefore, $\tan\theta = \dfrac{5\sqrt{2}}{2}$.

Answer: $\dfrac{5}{2}\sqrt{2}$

</details>

---

### Q6. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let the image of the point $P(1, 6, a)$ in the line $L: \dfrac{x}{1} = \dfrac{y-1}{2} = \dfrac{z-a+1}{b}$, $b > 0$, be $\left(\dfrac{a}{3}, 0, a+c\right)$. If $S(\alpha, \beta, \gamma)$, $\alpha > 0$, is the point on $L$ such that the distance of $S$ from the foot of perpendicular from the point $P$ on $L$ is $2\sqrt{14}$, then $\alpha + \beta + \gamma$ is equal to:

**Options:**

- **(A)** $19$
- **(B)** $20$
- **(C)** $21$
- **(D)** $22$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $21$**

**Detailed Solution:**

Let the foot of the perpendicular from $P(1, 6, a)$ to the line $L$ be $M$. Since the image of $P$ is $P'\left(\dfrac{a}{3}, 0, a+c\right)$, $M$ is the midpoint of $P$ and $P'$.

$M = \left(\dfrac{1 + \dfrac{a}{3}}{2}, \dfrac{6 + 0}{2}, \dfrac{a + a + c}{2}\right) = \left(\dfrac{a+3}{6}, 3, a + \dfrac{c}{2}\right)$

Since $M$ lies on the line $L: \dfrac{x}{1} = \dfrac{y-1}{2} = \dfrac{z-a+1}{b}$, we substitute its coordinates into the equation of the line:

$\dfrac{\dfrac{a+3}{6}}{1} = \dfrac{3-1}{2} = \dfrac{a + \dfrac{c}{2} - a + 1}{b}$

$\dfrac{a+3}{6} = 1 = \dfrac{\dfrac{c}{2} + 1}{b}$

From $\dfrac{a+3}{6} = 1$, we get $a = 3$.

From $\dfrac{\dfrac{c}{2} + 1}{b} = 1$, we get $2b = c + 2 \Rightarrow c = 2b - 2$.

The vector $\overrightarrow{PP'}$ is perpendicular to the direction vector of the line $L$, which is $\vec{v} = \hat{i} + 2\hat{j} + b\hat{k}$.

$\overrightarrow{PP'} = \left(\dfrac{a}{3} - 1\right)\hat{i} + (0 - 6)\hat{j} + (a+c - a)\hat{k} = \left(\dfrac{3}{3} - 1\right)\hat{i} - 6\hat{j} + c\hat{k} = -6\hat{j} + c\hat{k}$

Taking the dot product $\overrightarrow{PP'} \cdot \vec{v} = 0$:

$0(1) - 6(2) + c(b) = 0 \Rightarrow bc = 12$

Substituting $c = 2b - 2$ into $bc = 12$:

$b(2b - 2) = 12 \Rightarrow 2b^2 - 2b - 12 = 0 \Rightarrow b^2 - b - 6 = 0$

$(b-3)(b+2) = 0$

Since $b > 0$, we have $b = 3$. Then $c = 2(3) - 2 = 4$.

The coordinates of $M$ are $\left(\dfrac{3+3}{6}, 3, 3 + \dfrac{4}{2}\right) = (1, 3, 5)$.

The equation of the line $L$ is $\dfrac{x}{1} = \dfrac{y-1}{2} = \dfrac{z-2}{3}$. Any point $S$ on the line can be written as $(t, 2t+1, 3t+2)$.

The distance $SM$ is given as $2\sqrt{14}$.

$SM^2 = (t-1)^2 + (2t+1-3)^2 + (3t+2-5)^2 = 56$

$(t-1)^2 + 4(t-1)^2 + 9(t-1)^2 = 56$

$14(t-1)^2 = 56 \Rightarrow (t-1)^2 = 4 \Rightarrow t - 1 = \pm 2$

$t = 3$ or $t = -1$

Since $S(\alpha, \beta, \gamma) = (t, 2t+1, 3t+2)$ and $\alpha > 0$, we must have $t = 3$.

Thus, $S = (3, 7, 11)$.

$\alpha + \beta + \gamma = 3 + 7 + 11 = 21$

</details>

---

### Q7. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the distance of the point $(a, 2, 5)$ from the image of the point $(1, 2, 7)$ in the line $\dfrac{x}{1} = \dfrac{y-1}{1} = \dfrac{z-2}{2}$ is $4$, then the sum of all possible values of $a$ is equal to :

**Options:**

- **(A)** $11$
- **(B)** $9$
- **(C)** $6$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6$**

**Detailed Solution:**

Let $P(1, 2, 7)$ be the given point and the given line be $L: \dfrac{x}{1} = \dfrac{y-1}{1} = \dfrac{z-2}{2} = \lambda$.

Any point on the line can be written as $F(\lambda, \lambda+1, 2\lambda+2)$.

If $F$ is the foot of the perpendicular from $P$ to the line, the direction ratios of $PF$ are $(\lambda-1, \lambda-1, 2\lambda-5)$.

Since $PF$ is perpendicular to the line, the dot product of their direction ratios is zero:

$1(\lambda-1) + 1(\lambda-1) + 2(2\lambda-5) = 0$

$6\lambda - 12 = 0 \Rightarrow \lambda = 2$

Thus, the foot of the perpendicular is $F(2, 3, 6)$.

Let the image of $P$ in the line be $P'(x', y', z')$. Since $F$ is the midpoint of $P$ and $P'$:

$\dfrac{x'+1}{2} = 2 \Rightarrow x' = 3$

$\dfrac{y'+2}{2} = 3 \Rightarrow y' = 4$

$\dfrac{z'+7}{2} = 6 \Rightarrow z' = 5$

The image point is $P'(3, 4, 5)$.

The distance of the point $Q(a, 2, 5)$ from $P'(3, 4, 5)$ is given as $4$.

$\sqrt{(a-3)^2 + (2-4)^2 + (5-5)^2} = 4$

$(a-3)^2 + 4 = 16$

$(a-3)^2 = 12$

$a^2 - 6a - 3 = 0$

The sum of all possible values of $a$ is the sum of the roots of this quadratic equation, which is $6$.

Answer: $6$

</details>

---

### Q8. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let a triangle $PQR$ be such that $P$ and $Q$ lie on the line $\dfrac{x+3}{8} = \dfrac{y-4}{2} = \dfrac{z+1}{2}$ and are at a distance of $6$ units from $R(1, 2, 3)$. If $(\alpha, \beta, \gamma)$ is the centroid of $\triangle PQR$, then $\alpha + \beta + \gamma$ is equal to :

**Options:**

- **(A)** $4$
- **(B)** $5$
- **(C)** $6$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6$**

**Detailed Solution:**

The equation of the given line is $\dfrac{x+3}{8} = \dfrac{y-4}{2} = \dfrac{z+1}{2}$.

Let $\dfrac{x+3}{4} = \dfrac{y-4}{1} = \dfrac{z+1}{1} = \lambda$.

Any point on this line can be taken as $S(4\lambda - 3, \lambda + 4, \lambda - 1)$.

Since the points $P$ and $Q$ lie on this line and are at a distance of $6$ units from $R(1, 2, 3)$, we have $RS^2 = 36$.

$(4\lambda - 3 - 1)^2 + (\lambda + 4 - 2)^2 + (\lambda - 1 - 3)^2 = 36$

$(4\lambda - 4)^2 + (\lambda + 2)^2 + (\lambda - 4)^2 = 36$

$16(\lambda^2 - 2\lambda + 1) + (\lambda^2 + 4\lambda + 4) + (\lambda^2 - 8\lambda + 16) = 36$

$18\lambda^2 - 36\lambda + 36 = 36$

$18\lambda(\lambda - 2) = 0 \Rightarrow \lambda = 0 \text{ or } \lambda = 2$

For $\lambda = 0$, the point is $P(-3, 4, -1)$.

For $\lambda = 2$, the point is $Q(5, 6, 1)$.

The centroid $(\alpha, \beta, \gamma)$ of $\triangle PQR$ is given by:

$\alpha = \dfrac{-3 + 5 + 1}{3} = 1$

$\beta = \dfrac{4 + 6 + 2}{3} = 4$

$\gamma = \dfrac{-1 + 1 + 3}{3} = 1$

Therefore, $\alpha + \beta + \gamma = 1 + 4 + 1 = 6$.

Answer: $6$

</details>

---

### Q9. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The square of the distance of the point of intersection of the lines $\vec{r} = (\hat{i} + \hat{j} - \hat{k}) + \lambda(a\hat{i} - \hat{j})$, $a \neq 0$ and $\vec{r} = (4\hat{i} - \hat{k}) + \mu(2\hat{i} + a\hat{k})$ from the origin is:

**Options:**

- **(A)** $5$
- **(B)** $10$
- **(C)** $17$
- **(D)** $26$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $17$**

**Detailed Solution:**

Equating the position vectors of the two lines for intersection:

$(1 + a\lambda)\hat{i} + (1 - \lambda)\hat{j} - \hat{k} = (4 + 2\mu)\hat{i} + 0\hat{j} + (-1 + a\mu)\hat{k}$

Comparing the coefficients of $\hat{i}, \hat{j}, \hat{k}$:

$1 - \lambda = 0 \Rightarrow \lambda = 1$

$-1 = -1 + a\mu \Rightarrow a\mu = 0$

Since $a \neq 0$, we get $\mu = 0$.

Substituting $\lambda = 1$ and $\mu = 0$ in the $\hat{i}$ component equation:

$1 + a(1) = 4 + 2(0) \Rightarrow a = 3$

The position vector of the point of intersection is obtained by substituting $\mu = 0$ in the second line:

$\vec{r} = 4\hat{i} - \hat{k}$

The coordinates of the point of intersection are $(4, 0, -1)$.

The square of the distance from the origin is $4^2 + 0^2 + (-1)^2 = 16 + 1 = 17$.

Answer: $17$

</details>

---

### Q10. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The square of the distance of the point $P(5, 6, 7)$ from the line $\dfrac{x-2}{2} = \dfrac{y-5}{3} = \dfrac{z-2}{4}$ is equal to:

**Options:**

- **(A)** $3$
- **(B)** $5$
- **(C)** $6$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6$**

**Detailed Solution:**

Let the foot of the perpendicular from $P(5, 6, 7)$ to the given line be $Q$.

Any point on the line $\dfrac{x-2}{2} = \dfrac{y-5}{3} = \dfrac{z-2}{4} = \lambda$ is $Q(2\lambda + 2, 3\lambda + 5, 4\lambda + 2)$.

The direction ratios of $PQ$ are $(2\lambda - 3, 3\lambda - 1, 4\lambda - 5)$.

Since $PQ$ is perpendicular to the line, the dot product of their direction ratios is zero:

$2(2\lambda - 3) + 3(3\lambda - 1) + 4(4\lambda - 5) = 0$

$4\lambda - 6 + 9\lambda - 3 + 16\lambda - 20 = 0$

$29\lambda - 29 = 0 \Rightarrow \lambda = 1$

Substituting $\lambda = 1$, the coordinates of $Q$ are $(4, 8, 6)$.

The square of the distance $PQ^2$ is $(5 - 4)^2 + (6 - 8)^2 + (7 - 6)^2 = 1 + 4 + 1 = 6$.

Answer: $6$

</details>

---

### Q11. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\left(2\alpha+1, \alpha^2-3\alpha, \dfrac{\alpha-1}{2}\right)$ is the image of $(\alpha, 2\alpha, 1)$ in the line $\dfrac{x-2}{3}=\dfrac{y-1}{2}=\dfrac{z}{1}$, then the possible value(s) of $\alpha$ is (are)

**Options:**

- **(A)** Only $3$
- **(B)** Only $3$ and $-1$
- **(C)** Only $3$, $\dfrac{1}{4}$ and $-1$
- **(D)** Only $3$ and $\dfrac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Only $3$**

**Detailed Solution:**

Let the given point be $P = (\alpha, 2\alpha, 1)$ and its image be $P' = \left(2\alpha+1, \alpha^2-3\alpha, \dfrac{\alpha-1}{2}\right)$.

For $P'$ to be the image of $P$ in the given line $L: \dfrac{x-2}{3}=\dfrac{y-1}{2}=\dfrac{z}{1}$, two conditions must be satisfied:
1. The midpoint of $P$ and $P'$ must lie on the line $L$.
2. The line segment $PP'$ must be perpendicular to the line $L$.

The midpoint $M$ of $P$ and $P'$ is:
$M = \left( \dfrac{\alpha + 2\alpha + 1}{2}, \dfrac{2\alpha + \alpha^2 - 3\alpha}{2}, \dfrac{1 + \dfrac{\alpha-1}{2}}{2} \right) = \left( \dfrac{3\alpha + 1}{2}, \dfrac{\alpha^2 - \alpha}{2}, \dfrac{\alpha + 1}{4} \right)$

Since $M$ lies on $L$, its coordinates must satisfy the equation of the line:
$\dfrac{\dfrac{3\alpha + 1}{2} - 2}{3} = \dfrac{\dfrac{\alpha^2 - \alpha}{2} - 1}{2} = \dfrac{\dfrac{\alpha + 1}{4}}{1}$

Simplifying the terms, we get:
$\dfrac{\alpha - 1}{2} = \dfrac{\alpha^2 - \alpha - 2}{4} = \dfrac{\alpha + 1}{4}$

Equating the first and third parts:
$\dfrac{\alpha - 1}{2} = \dfrac{\alpha + 1}{4}$

$2(\alpha - 1) = \alpha + 1 \Rightarrow 2\alpha - 2 = \alpha + 1 \Rightarrow \alpha = 3$

Substituting $\alpha = 3$ into the middle part to verify:
$\dfrac{3^2 - 3 - 2}{4} = \dfrac{4}{4} = 1$
The first and third parts also equal $1$, so $\alpha = 3$ satisfies the midpoint condition.

Now, let us check the perpendicularity condition. The direction ratios of $\overrightarrow{PP'}$ are:
$\left(2\alpha+1 - \alpha, \alpha^2-3\alpha - 2\alpha, \dfrac{\alpha-1}{2} - 1\right) = \left(\alpha+1, \alpha^2-5\alpha, \dfrac{\alpha-3}{2}\right)$

The direction ratios of the line $L$ are $(3, 2, 1)$. The dot product must be zero:
$3(\alpha+1) + 2(\alpha^2-5\alpha) + 1\left(\dfrac{\alpha-3}{2}\right) = 0$

Multiplying by 2 to clear the denominator:
$6(\alpha+1) + 4(\alpha^2-5\alpha) + (\alpha-3) = 0$

$6\alpha + 6 + 4\alpha^2 - 20\alpha + \alpha - 3 = 0$

$4\alpha^2 - 13\alpha + 3 = 0$

Factoring the quadratic equation:
$4\alpha^2 - 12\alpha - \alpha + 3 = 0$

$4\alpha(\alpha - 3) - 1(\alpha - 3) = 0$

$(4\alpha - 1)(\alpha - 3) = 0 \Rightarrow \alpha = \dfrac{1}{4} \text{ or } \alpha = 3$

For $P'$ to be the image of $P$, both the midpoint and perpendicularity conditions must hold simultaneously. The only common value satisfying both conditions is $\alpha = 3$.

Answer: Only $3$

</details>

---

### Q12. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The shortest distance between the lines $\vec{r}=\left(\dfrac{1}{3}\hat{i}+2\hat{j}+\dfrac{8}{3}\hat{k}\right)+\lambda(2\hat{i}-5\hat{j}+6\hat{k})$ and $\vec{r}=\left(-\dfrac{2}{3}\hat{i}-\dfrac{1}{3}\hat{k}\right)+\mu(\hat{j}-\hat{k})$, $\lambda,\mu \in \mathbb{R}$, is:

**Options:**

- **(A)** $\sqrt{5}$
- **(B)** $3$
- **(C)** $2\sqrt{3}$
- **(D)** $\sqrt{15}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3$**

**Detailed Solution:**

The given lines are $\vec{r} = \vec{a}_1 + \lambda \vec{b}_1$ and $\vec{r} = \vec{a}_2 + \mu \vec{b}_2$, where:

$\vec{a}_1 = \dfrac{1}{3}\hat{i} + 2\hat{j} + \dfrac{8}{3}\hat{k}$

$\vec{b}_1 = 2\hat{i} - 5\hat{j} + 6\hat{k}$

$\vec{a}_2 = -\dfrac{2}{3}\hat{i} - \dfrac{1}{3}\hat{k}$

$\vec{b}_2 = \hat{j} - \hat{k}$

The shortest distance between two skew lines is given by $d = \dfrac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|}$.

First, finding the vector $\vec{a}_2 - \vec{a}_1$:

$\vec{a}_2 - \vec{a}_1 = \left(-\dfrac{2}{3} - \dfrac{1}{3}\right)\hat{i} + (0 - 2)\hat{j} + \left(-\dfrac{1}{3} - \dfrac{8}{3}\right)\hat{k} = -\hat{i} - 2\hat{j} - 3\hat{k}$

Next, finding the cross product $\vec{b}_1 \times \vec{b}_2$:

$\vec{b}_1 \times \vec{b}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & -5 & 6 \\ 0 & 1 & -1 \end{vmatrix} = \hat{i}(5 - 6) - \hat{j}(-2 - 0) + \hat{k}(2 - 0) = -\hat{i} + 2\hat{j} + 2\hat{k}$

The magnitude of the cross product is:

$|\vec{b}_1 \times \vec{b}_2| = \sqrt{(-1)^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = 3$

Now, finding the dot product $(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)$:

$(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2) = (-\hat{i} - 2\hat{j} - 3\hat{k}) \cdot (-\hat{i} + 2\hat{j} + 2\hat{k})$

$= (-1)(-1) + (-2)(2) + (-3)(2) = 1 - 4 - 6 = -9$

Finally, the shortest distance is:

$d = \dfrac{|-9|}{3} = \dfrac{9}{3} = 3$

Answer: $3$

</details>

---

### Q13. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The square of the distance of the point $(-2, -8, 6)$ from the line $\dfrac{x-1}{1} = \dfrac{y-1}{2} = \dfrac{z}{-1}$ along the line $\dfrac{x+5}{1} = \dfrac{y+5}{-1} = \dfrac{z}{2}$ is equal to:

**Options:**

- **(A)** $3$
- **(B)** $6$
- **(C)** $8$
- **(D)** $12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6$**

**Detailed Solution:**

Let the given point be $P(-2, -8, 6)$.

The distance is measured along the line $\dfrac{x+5}{1} = \dfrac{y+5}{-1} = \dfrac{z}{2}$, which has direction ratios $(1, -1, 2)$.

The equation of the line passing through $P$ and parallel to this line is:
$\dfrac{x+2}{1} = \dfrac{y+8}{-1} = \dfrac{z-6}{2} = \lambda$

Any point on this line can be written as $Q(\lambda - 2, -\lambda - 8, 2\lambda + 6)$.

Since $Q$ lies on the line $\dfrac{x-1}{1} = \dfrac{y-1}{2} = \dfrac{z}{-1}$, we substitute the coordinates of $Q$ into its equation:
$\dfrac{\lambda - 2 - 1}{1} = \dfrac{-\lambda - 8 - 1}{2} = \dfrac{2\lambda + 6}{-1}$

$\dfrac{\lambda - 3}{1} = \dfrac{-\lambda - 9}{2} = \dfrac{2\lambda + 6}{-1}$

Taking the first two parts:
$2(\lambda - 3) = -\lambda - 9$
$2\lambda - 6 = -\lambda - 9$
$3\lambda = -3 \Rightarrow \lambda = -1$

Substituting $\lambda = -1$ into the coordinates of $Q$, we get:
$Q(-1 - 2, -(-1) - 8, 2(-1) + 6) \equiv Q(-3, -7, 4)$

The square of the distance between $P(-2, -8, 6)$ and $Q(-3, -7, 4)$ is:
$PQ^2 = (-3 - (-2))^2 + (-7 - (-8))^2 + (4 - 6)^2$
$PQ^2 = (-1)^2 + (1)^2 + (-2)^2$
$PQ^2 = 1 + 1 + 4 = 6$

Answer: $6$

</details>

---

### Q14. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A line with direction ratios $1, -1, 2$ intersects the lines $\dfrac{x}{2} = \dfrac{y}{3} = \dfrac{z+1}{3}$ and $\dfrac{x+1}{-1} = \dfrac{y-2}{1} = \dfrac{z}{4}$ at the points $P$ and $Q$, respectively. If the length of the line segment $PQ$ is $\alpha$, then $225\alpha^2$ is equal to:

**Options:**

- **(A)** $1024$
- **(B)** $1014$
- **(C)** $1104$
- **(D)** $1204$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1014$**

**Detailed Solution:**

Let the coordinates of $P$ on the first line be $(2\lambda, 3\lambda, 3\lambda - 1)$.

Let the coordinates of $Q$ on the second line be $(-\mu - 1, \mu + 2, 4\mu)$.

The direction ratios of the line segment $PQ$ are proportional to $1, -1, 2$. Thus, we can write:

$\dfrac{-\mu - 1 - 2\lambda}{1} = \dfrac{\mu + 2 - 3\lambda}{-1} = \dfrac{4\mu - 3\lambda + 1}{2} = k$

This gives the system of equations:

$-\mu - 2\lambda - 1 = k$

$\mu - 3\lambda + 2 = -k$

$4\mu - 3\lambda + 1 = 2k$

Adding the first two equations gives:

$-5\lambda + 1 = 0 \Rightarrow \lambda = \dfrac{1}{5}$

Substituting $\lambda = \dfrac{1}{5}$ into the first and third equations:

$-\mu - \dfrac{7}{5} = k \Rightarrow \mu + k = -\dfrac{7}{5}$

$4\mu + \dfrac{2}{5} = 2k \Rightarrow 2\mu - k = -\dfrac{1}{5}$

Adding these two equations gives:

$3\mu = -\dfrac{8}{5} \Rightarrow \mu = -\dfrac{8}{15}$

Substituting $\mu = -\dfrac{8}{15}$ into $\mu + k = -\dfrac{7}{5}$:

$-\dfrac{8}{15} + k = -\dfrac{21}{15} \Rightarrow k = -\dfrac{13}{15}$

The vector $\overrightarrow{PQ}$ is $(k, -k, 2k)$. The length of the line segment $PQ$ is $\alpha = \sqrt{k^2 + (-k)^2 + (2k)^2} = \sqrt{6k^2}$.

Thus, $\alpha^2 = 6k^2 = 6 \left(-\dfrac{13}{15}\right)^2 = 6 \times \dfrac{169}{225} = \dfrac{1014}{225}$.

Therefore, $225\alpha^2 = 1014$.

Answer: $1014$

</details>

---

### Q15. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the point A be the foot of perpendicular drawn from the point $P(a, b, 0)$ on the line $\dfrac{x-1}{2} = \dfrac{y-2}{1} = \dfrac{z-\alpha}{3}$. If the midpoint of the line segment PA is $\left(0, \dfrac{3}{4}, \dfrac{-1}{4}\right)$, then the value of $a^2 + b^2 + \alpha^2$ is equal to:

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $6$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

Let $P = (a, b, 0)$ and the midpoint of $PA$ be $M = \left(0, \dfrac{3}{4}, -\dfrac{1}{4}\right)$.

Using the midpoint formula, the coordinates of $A$ are given by $2M - P$:

$A = \left(-a, \dfrac{3}{2} - b, -\dfrac{1}{2}\right)$

Since $A$ lies on the given line $\dfrac{x-1}{2} = \dfrac{y-2}{1} = \dfrac{z-\alpha}{3} = \lambda$, we can write:

$\dfrac{-a-1}{2} = \lambda \Rightarrow a = -2\lambda - 1$

$\dfrac{\dfrac{3}{2}-b-2}{1} = \lambda \Rightarrow b = -\lambda - \dfrac{1}{2}$

$\dfrac{-\dfrac{1}{2}-\alpha}{3} = \lambda \Rightarrow \alpha = -3\lambda - \dfrac{1}{2}$

The direction ratios of the line segment $PA$ are the differences in coordinates of $A$ and $P$:

$\vec{PA} = \left(-2a, \dfrac{3}{2} - 2b, -\dfrac{1}{2}\right)$

Since $PA$ is perpendicular to the given line, the dot product of their direction ratios must be zero. The direction ratios of the line are $(2, 1, 3)$.

$2(-2a) + 1\left(\dfrac{3}{2} - 2b\right) + 3\left(-\dfrac{1}{2}\right) = 0$

$-4a + \dfrac{3}{2} - 2b - \dfrac{3}{2} = 0$

$-4a - 2b = 0 \Rightarrow 2a + b = 0$

Substituting the expressions for $a$ and $b$ in terms of $\lambda$:

$2(-2\lambda - 1) + \left(-\lambda - \dfrac{1}{2}\right) = 0$

$-4\lambda - 2 - \lambda - \dfrac{1}{2} = 0$

$-5\lambda - \dfrac{5}{2} = 0 \Rightarrow \lambda = -\dfrac{1}{2}$

Now, substituting $\lambda = -\dfrac{1}{2}$ back to find $a, b,$ and $\alpha$:

$a = -2\left(-\dfrac{1}{2}\right) - 1 = 0$

$b = -\left(-\dfrac{1}{2}\right) - \dfrac{1}{2} = 0$

$\alpha = -3\left(-\dfrac{1}{2}\right) - \dfrac{1}{2} = \dfrac{3}{2} - \dfrac{1}{2} = 1$

Finally, calculating the required value:

$a^2 + b^2 + \alpha^2 = 0^2 + 0^2 + 1^2 = 1$

Answer: $1$

</details>

---

### Q16. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let a line $L$ passing through the point $(1, 1, 1)$ be perpendicular to both the vectors $2\hat{i} + 2\hat{j} + \hat{k}$ and $\hat{i} + 2\hat{j} + 2\hat{k}$. If $P(a, b, c)$ is the foot of perpendicular from the origin on the line $L$, then the value of $34(a + b + c)$ is :

**Options:**

- **(A)** $50$
- **(B)** $80$
- **(C)** $100$
- **(D)** $120$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $100$**

**Detailed Solution:**

The direction vector of the line $L$ is given by the cross product of the two vectors to which it is perpendicular:

$\vec{d} = (2\hat{i} + 2\hat{j} + \hat{k}) \times (\hat{i} + 2\hat{j} + 2\hat{k}) = 2\hat{i} - 3\hat{j} + 2\hat{k}$

The equation of the line $L$ passing through $(1, 1, 1)$ is:

$\dfrac{x - 1}{2} = \dfrac{y - 1}{-3} = \dfrac{z - 1}{2} = \lambda$

Any point $P$ on the line $L$ has coordinates $(2\lambda + 1, -3\lambda + 1, 2\lambda + 1)$.

Since $P(a, b, c)$ is the foot of the perpendicular from the origin $(0, 0, 0)$ to the line $L$, the vector $\overrightarrow{OP}$ is perpendicular to the direction vector $\vec{d}$ of the line. Thus, their dot product is zero:

$\overrightarrow{OP} \cdot \vec{d} = 0$

$2(2\lambda + 1) - 3(-3\lambda + 1) + 2(2\lambda + 1) = 0$

$4\lambda + 2 + 9\lambda - 3 + 4\lambda + 2 = 0$

$17\lambda + 1 = 0 \Rightarrow \lambda = -\dfrac{1}{17}$

Substituting $\lambda = -\dfrac{1}{17}$ into the coordinates of $P$, we get:

$a = 2\left(-\dfrac{1}{17}\right) + 1 = \dfrac{15}{17}$

$b = -3\left(-\dfrac{1}{17}\right) + 1 = \dfrac{20}{17}$

$c = 2\left(-\dfrac{1}{17}\right) + 1 = \dfrac{15}{17}$

The sum of the coordinates is:

$a + b + c = \dfrac{15}{17} + \dfrac{20}{17} + \dfrac{15}{17} = \dfrac{50}{17}$

Therefore, the value of $34(a + b + c)$ is:

$34 \times \dfrac{50}{17} = 100$

Answer: $100$

</details>

---

### Q17. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the point of intersection of the lines $\dfrac{x+1}{3} = \dfrac{y+a}{5} = \dfrac{z+b+1}{7}$ and $\dfrac{x-2}{1} = \dfrac{y-b}{4} = \dfrac{z-2a}{7}$ lies on $xy$-plane, then the value of $a + b$ is :

**Options:**

- **(A)** $2$
- **(B)** $5$
- **(C)** $7$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $7$**

**Detailed Solution:**

Let the point of intersection be $(x, y, 0)$ since it lies on the $xy$-plane.

For the first line, equating the coordinates to a parameter $\lambda$:

$\dfrac{x+1}{3} = \dfrac{y+a}{5} = \dfrac{0+b+1}{7} = \lambda$

This gives $x = \dfrac{3b+3}{7} - 1$ and $y = \dfrac{5b+5}{7} - a$.

For the second line, equating the coordinates to a parameter $\mu$:

$\dfrac{x-2}{1} = \dfrac{y-b}{4} = \dfrac{0-2a}{7} = \mu$

This gives $x = \dfrac{-2a}{7} + 2$ and $y = \dfrac{-8a}{7} + b$.

Equating the $x$-coordinates from both lines:

$\dfrac{3b+3}{7} - 1 = \dfrac{-2a}{7} + 2$

$\dfrac{3b-4}{7} = \dfrac{-2a+14}{7}$

$2a + 3b = 18$

Equating the $y$-coordinates from both lines:

$\dfrac{5b+5}{7} - a = \dfrac{-8a}{7} + b$

$5b + 5 - 7a = -8a + 7b$

$a - 2b = -5$

Solving the two linear equations $2a + 3b = 18$ and $a - 2b = -5$:

From the second equation, $a = 2b - 5$. Substituting this into the first equation:

$2(2b - 5) + 3b = 18$

$4b - 10 + 3b = 18$

$7b = 28 \Rightarrow b = 4$

Substituting $b = 4$ into $a = 2b - 5$:

$a = 2(4) - 5 = 3$

Therefore, $a + b = 3 + 4 = 7$.

Answer: $7$

</details>

---

### Q18. JEE Main 2026 (28 January Shift 2)

*Type:* `numerical` | *Level:* `3`

If the distance of the point $\mathrm{P}(43, \alpha, \beta), \beta<0$, from the line $\overrightarrow{\mathrm{r}}=4 \hat{i}-\hat{k}+\mu(2 \hat{i}+3 \hat{k}), \mu \in \mathbf{R}$ along a line with direction ratios $3,-1,0$ is $13 \sqrt{10}$, then $\alpha^{2}+\beta^{2}$ is equal to $\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **170**

**Detailed Solution:**

Point P(43, α, β) has distance $13\sqrt{10}$ from line $\vec{r} = 4\vec{i} - \vec{k} + \mu(2\vec{i} + 3\vec{k})$.
The line passes through A(4, 0, -1) with direction $\vec{d} = (2, 0, 3)$.
Using distance formula: $d = \frac{|\vec{AP} \times \vec{d}|}{|\vec{d}|}$.
With $\vec{AP} = (39, α, β+1)$, the cross product gives $\vec{AP} \times \vec{d} = (3α, 2β - 115, -2α)$.
Thus $|\vec{AP} \times \vec{d}| = \sqrt{13α^2 + (2β - 115)^2}$ and $|\vec{d}| = \sqrt{13}$.
Setting $\frac{\sqrt{13α^2 + (2β - 115)^2}}{\sqrt{13}} = 13\sqrt{10}$ gives $α^2 + \frac{(2β - 115)^2}{13} = 1690$.
Solving with the constraint β < 0: α = 5, β = -13, hence $α^2 + β^2 = 25 + 169 = 170$.

</details>

---

### Q19. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{Q}(\mathrm{a}, \mathrm{b}, \mathrm{c})$ be the image of the point $\mathrm{P}(3,2,1)$ in the line $\frac{x-1}{1}=\frac{y}{2}=\frac{z-1}{1}$. Then the distance of Q from the line $\frac{x-9}{3}=\frac{y-9}{2}=\frac{z-5}{-2}$ is

**Options:**

- **(A)** 8
- **(B)** 5
- **(C)** 7
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7**

**Detailed Solution:**

Line 1 passes through (1, 0, 1) with direction $(1, 2, 1)$. Point on line: $(1+t, 2t, 1+t)$. 
For projection Q of P(3, 2, 1): $(t-2, 2t-2, t) \cdot (1, 2, 1) = 0$ gives $6t = 6$, so $t = 1$. 
Thus Q = (2, 2, 2). 
Distance from Q to line 2 (passing through (9, 9, 5) with direction $(3, 2, -2)$): 
$\vec{QR} = (7, 7, 3)$. 
$\vec{QR} \times \vec{d} = -20\vec{i} + 23\vec{j} - 7\vec{k}$. 
$|\vec{QR} \times \vec{d}| = \sqrt{400 + 529 + 49} = \sqrt{978}$. 
$|\vec{d}| = \sqrt{17}$. 
Distance = $\frac{\sqrt{978}}{\sqrt{17}} = \sqrt{57.53} \approx 7.59 \approx 7$.

</details>

---

### Q20. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the distances of the point $(1,2, a)$ from the line $\frac{x-1}{1}=\frac{y}{2}=\frac{z-1}{1}$ along the lines $\mathrm{L}_{1}: \frac{x-1}{3}=\frac{y-2}{4}=\frac{z-a}{b}$ and $\mathrm{L}_{2}: \frac{x-1}{1}=\frac{y-2}{4}=\frac{z-a}{c}$ are equal, then $a+b+c$ is equal to

**Options:**

- **(A)** 5
- **(B)** 7
- **(C)** 4
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 7**

**Detailed Solution:**

Line $L$: $\frac{x-1}{1} = \frac{y}{2} = \frac{z-1}{1}$

$L_1$: $\frac{x-1}{3} = \frac{y-2}{4} = \frac{z-a}{b} = \lambda$

$L_2$: $\frac{x-1}{1} = \frac{y-2}{4} = \frac{z-a}{c} = \mu$

Point $A(3\lambda+1, 4\lambda+2, b\lambda+a)$ lies on $L$:
$\frac{3\lambda}{1} = \frac{4\lambda+2}{2} = \frac{b\lambda+a-1}{1}$

$\lambda = 1$, $a + b - 1 = 3 \Rightarrow a + b = 4$ ...(1), $A = (4, 6, 4)$

Point $B(\mu+1, 4\mu+2, c\mu+a)$ lies on $L$:
$2\mu = 4\mu+2 \Rightarrow \mu = -1$, $a - c - 1 = -1 \Rightarrow a = c$ ...(2), $B = (0, -2, 0)$

Since $PA = PB$ where $P = (1, 2, a)$:
$9 + 16 + (a-4)^2 = 1 + 16 + a^2$
$\Rightarrow a = 3$, so $c = 3$, $b = 1$

$a + b + c = 7$

</details>

---

### Q21. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The sum of all values of $\alpha$, for which the shortest distance between the lines $\frac{x+1}{\alpha}=\frac{y-2}{-1}=\frac{z-4}{-\alpha}$ and $\frac{x}{\alpha}=\frac{y-1}{2}=\frac{z-1}{2 \alpha}$ is $\sqrt{2}$, is

**Options:**

- **(A)** 6
- **(B)** 8
- **(C)** -8
- **(D)** -6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -6**

**Detailed Solution:**

The given lines are $L_1: \frac{x+1}{\alpha} = \frac{y-2}{-1} = \frac{z-4}{-\alpha}$ and $L_2: \frac{x}{\alpha} = \frac{y-1}{2} = \frac{z-1}{2\alpha}$.
For $L_1$, point $\vec{a}_1 = (-1, 2, 4)$ and direction $\vec{b}_1 = (\alpha, -1, -\alpha)$.
For $L_2$, point $\vec{a}_2 = (0, 1, 1)$ and direction $\vec{b}_2 = (\alpha, 2, 2\alpha)$.
The shortest distance $d$ is given by $d = \frac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|}$.
$\vec{a}_2 - \vec{a}_1 = (1, -1, -3)$.
$\vec{b}_1 \times \vec{b}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \alpha & -1 & -\alpha \\ \alpha & 2 & 2\alpha \end{vmatrix} = \hat{i}(-2\alpha + 2\alpha) - \hat{j}(2\alpha^2 + \alpha^2) + \hat{k}(2\alpha + \alpha) = (0, -3\alpha^2, 3\alpha)$.
$|\vec{b}_1 \times \vec{b}_2| = \sqrt{0 + 9\alpha^4 + 9\alpha^2} = 3|\alpha|\sqrt{\alpha^2 + 1}$.
$(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2) = (1)(0) + (-1)(-3\alpha^2) + (-3)(3\alpha) = 3\alpha^2 - 9\alpha$.
Given $d = \sqrt{2}$, so $\frac{|3\alpha^2 - 9\alpha|}{3|\alpha|\sqrt{\alpha^2 + 1}} = \sqrt{2} \Rightarrow \frac{|\alpha - 3|}{\sqrt{\alpha^2 + 1}} = \sqrt{2}$.
Squaring both sides: $(\alpha - 3)^2 = 2(\alpha^2 + 1) \Rightarrow \alpha^2 - 6\alpha + 9 = 2\alpha^2 + 2$.
$\alpha^2 + 6\alpha - 7 = 0$.
The values of $\alpha$ are the roots of this quadratic equation.
Sum of values of $\alpha = -\frac{6}{1} = -6$.

</details>

---

### Q22. JEE Main 2026 (24 January Shift 1)

*Type:* `numerical` | *Level:* `3`

Let a line L passing through the point $\mathrm{P}(1,1,1)$ be perpendicular to the lines $\frac{x-4}{4}=\frac{y-1}{1}=\frac{z-1}{1}$ and $\frac{x-17}{1}=\frac{y-71}{1}=\frac{z}{0}$. Let the line L intersect the $y z-$ plane at the point Q. Another line parallel to L and passing through the point $\mathrm{S}(1,0,-1)$ intersects the $y z$-plane at the point R. Then the square of the area of the parallelogram PQRS is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

Line L passes through P(1,1,1) perpendicular to two lines with directions $(4, 1, 1)$ and $(1, 1, 0)$.
Direction of L: $(4, 1, 1) \times (1, 1, 0) = (-1, 1, 3)$
Line L: $(x, y, z) = (1, 1, 1) + t(-1, 1, 3)$
Q is intersection with yz-plane (x=0): Setting $1-t=0$ gives $t=1$, so Q = (0, 2, 4)
Line through S(1,0,-1) parallel to L: $(x, y, z) = (1, 0, -1) + s(-1, 1, 3)$
R is intersection with yz-plane: Setting $1-s=0$ gives $s=1$, so R = (0, 1, 2)
For parallelogram PQRS: $\vec{PQ} = (-1, 1, 3)$ and $\vec{PS} = (0, -1, -2)$
Area = $|\vec{PQ} \times \vec{PS}| = |(1, -2, 1)| = \sqrt{1+4+1} = \sqrt{6}$
Square of area = 6

</details>

---

### Q23. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let the lines $\mathrm{L}_{1}: \vec{r}=\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}+\lambda(2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+4 \hat{\mathrm{k}}), \lambda \in \mathbb{R}$ and $\mathrm{L}_{2}: \vec{r}=(4 \hat{\mathrm{i}}+\hat{\mathrm{j}})+\mu(5 \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}}), \mu \in \mathbb{R}$, intersect at the point R. Let P and Q be the points lying on lines $\mathrm{L}_{1}$ and $\mathrm{L}_{2}$, respectively, such that $|\overrightarrow{\mathrm{PR}}|=\sqrt{29}$ and $|\overrightarrow{\mathrm{PQ}}|=\sqrt{\frac{47}{3}}$. If the point P lies in the first octant, then $27(\mathrm{QR})^{2}$ is equal to

**Options:**

- **(A)** 348
- **(B)** 340
- **(C)** 320
- **(D)** 360

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 360**

**Detailed Solution:**

Find R by solving $L_1 = L_2$:
From $1+2\lambda = 4+5\mu$, $2+3\lambda = 1+2\mu$, $3+4\lambda = \mu$ we get $\lambda = -1$, $\mu = -1$, so $R = (-1, -1, -1)$
Point P on $L_1$: $P = (1+2\lambda_P, 2+3\lambda_P, 3+4\lambda_P)$ with $|\overrightarrow{PR}|^2 = 29$
$4(1+\lambda_P)^2 + 9(1+\lambda_P)^2 + 16(1+\lambda_P)^2 = 29$ → $29(1+\lambda_P)^2 = 29$ → $\lambda_P = 0$ (first octant)
Thus $P = (1, 2, 3)$
Point Q on $L_2$: $Q = (4+5\mu_Q, 1+2\mu_Q, \mu_Q)$ with $|\overrightarrow{PQ}|^2 = \frac{47}{3}$
$(3+5\mu_Q)^2 + (-1+2\mu_Q)^2 + (\mu_Q-3)^2 = \frac{47}{3}$
$30\mu_Q^2 + 20\mu_Q + 19 = \frac{47}{3}$ → $9\mu_Q^2 + 6\mu_Q + 1 = 0$ → $\mu_Q = -\frac{1}{3}$
So $Q = (\frac{7}{3}, \frac{1}{3}, -\frac{1}{3})$
$|QR|^2 = \frac{100+16+4}{9} = \frac{120}{9} = \frac{40}{3}$
$27(QR)^2 = 360$

</details>

---

### Q24. JEE Main 2026 (23 January Shift 2)

*Type:* `numerical` | *Level:* `2`

If the image of the point $\mathrm{P}(a, 2, a)$ in the line $\frac{x}{2}=\frac{y+a}{1}=\frac{z}{1}$ is Q and the image of Q in the line $\frac{x-2 b}{2}=\frac{y-a}{1}=\frac{z+2 b}{-5}$ is P, then $a+b$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/23S2_s_24_1.png">
Now,
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/23S2_s_24_2.png">
$\dfrac{2\lambda - a + a}{2} = -5\mu - 2b$
and $\dfrac{a + 4\lambda - a}{2} = 2\mu + 2b$
and $\dfrac{2\lambda - 2a - 2 + 2}{2} = \mu + a$
$\Rightarrow \lambda - \mu = b$
$\lambda - \mu = 2a$
$\lambda + 5\mu = -2b$
$\Rightarrow b = 2a$ and $\lambda = a$, $\mu = -a$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/23S2_s_24_3.png">
$(a\hat{i} - 2\hat{j} + 0\hat{k}) \cdot (2\hat{i} + \hat{j} + \hat{k}) = 0$
$2a - 2 = 0$
$a = 1$
$b = 2a = 2 \times 1 = 2$
$a + b = 1 + 2 = 3$

</details>

---

### Q25. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The vertices B and C of a triangle ABC lie on the line $\frac{x}{1}=\frac{1-y}{-2}=\frac{\mathrm{z}-2}{3}$. The coordinates of A and B are $(1,6,3)$ and $(4,9, \alpha)$ respectively and C is at a distance of 10 units from B. The area (in sq. units) of $\triangle \mathrm{ABC}$ is :

**Options:**

- **(A)** $20 \sqrt{13}$
- **(B)** $5 \sqrt{13}$
- **(C)** $15 \sqrt{13}$
- **(D)** $10 \sqrt{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $5 \sqrt{13}$**

**Detailed Solution:**

$\dfrac{4}{1} = \dfrac{9-1}{2} = \dfrac{\alpha - 2}{3} \Rightarrow \alpha = 14$
<img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/23S1_s_18_1.png">
$\overrightarrow{AD} \cdot (\hat{i} + 2\hat{j} + 3\hat{k}) = 0$
$(\lambda - 1)\hat{i} + (2\lambda - 5)\hat{j} + (3\lambda - 1)\hat{k} = \overrightarrow{AD}$
$\Rightarrow \lambda - 1 + 4\lambda - 10 + 9\lambda - 3 = 0$
$\Rightarrow 14\lambda = 14 \Rightarrow \lambda = 1$
$D = (1, 3, 5)$
$AD = \sqrt{3^2 + 2^2} = \sqrt{13}$
$Ar(\triangle ABC) = \dfrac{1}{2} \times \sqrt{13} \times 10 = 5\sqrt{13}$

</details>

---

### Q26. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let L be the line $\frac{x+1}{2}=\frac{y+1}{3}=\frac{z+3}{6}$ and let S be the set of all points $(\mathrm{a}, \mathrm{b}, \mathrm{c})$ on L, whose distance from the line $\frac{x+1}{2}=\frac{y+1}{3}=\frac{z-9}{0}$ along the line $L$ is 7. Then $\sum_{(a, b, c) \in S}(a+b+c)$ is equal to :

**Options:**

- **(A)** 6
- **(B)** 34
- **(C)** 40
- **(D)** 28

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 34**

**Detailed Solution:**

M is the point of intersection of $L_1$ & $L_2$
$\Rightarrow 2\lambda - 1 = 2\mu - 1, 3\lambda - 1 = 3\mu - 1, 6\lambda - 3 = 9$
$\Rightarrow \lambda = 2 = \mu$
$\Rightarrow M(3, 5, 9)$
Now let point P be $(2K - 1, 3K - 1, 6K - 3)$ on $L_2$
such that $PM = 7$
$\Rightarrow \sqrt{(2K - 4)^2 + (3K - 6)^2 + (6K - 12)^2} = 7$
$\Rightarrow 49K^2 + 196 - 196K = 49$
$\Rightarrow K^2 + 4 - 4K = 1$
$\Rightarrow K^2 - 4K + 3 = 0$
$\Rightarrow K = 1, 3$
So points P & Q are $(1, 2, 3)$ & $(5, 8, 15)$
So sum of all co-ordinates of P & Q $= 34$

</details>

---

### Q27. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{P}(\alpha, \beta, \gamma)$ be the point on the line $\frac{x-1}{2}=\frac{y+1}{-3}=z$ at a distance $4 \sqrt{14}$ from the point $(1,-1,0)$ and nearer to the origin. Then the shortest distance, between the lines $\frac{x-\alpha}{1}=\frac{y-\beta}{2}=\frac{z-\gamma}{3}$ and $\frac{x+5}{2}=\frac{y-10}{1}=\frac{z-3}{1}$, is equal to

**Options:**

- **(A)** $4 \sqrt{\frac{7}{5}}$
- **(B)** $2 \sqrt{\frac{7}{4}}$
- **(C)** $7 \sqrt{\frac{5}{4}}$
- **(D)** $4 \sqrt{\frac{5}{7}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4 \sqrt{\frac{7}{5}}$**

**Detailed Solution:**

Let $P(2\lambda + 1, -3\lambda - 1, \lambda)$
Then $4\lambda^2 + 9\lambda^2 + \lambda^2 = 16 \cdot 14 \Rightarrow \lambda = \pm 4 \Rightarrow -4$
(nearer to origin)
$\therefore P(-7, 11, -4)$
$\therefore$ Shortest distance $= \dfrac{\begin{vmatrix} 2 & -1 & 7 \\ 1 & 2 & 3 \\ 2 & 1 & 1 \end{vmatrix}}{\left| \hat{i} \quad \hat{j} \quad k \right| \begin{vmatrix} 1 & 2 & 3 \\ 2 & 1 & 1 \end{vmatrix}}$
$= \dfrac{28}{\sqrt{1 + 25 + 9}} = \dfrac{4\sqrt{7}}{\sqrt{5}}$

</details>

---

### Q28. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the image of the point $\mathrm{P}(1,2, a)$ in the line $\frac{x-6}{3}=\frac{y-7}{2}=\frac{7-\mathrm{z}}{2}$ is $\mathrm{Q}(5, b, \mathrm{c})$, then $a^{2}+b^{2}+c^{2}$ is equal to

**Options:**

- **(A)** 298
- **(B)** 293
- **(C)** 264
- **(D)** 283

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 298**

**Detailed Solution:**

Line: point $(6,7,7)$, direction $(3,2,-2)$.
General point on line: $(6+3t, 7+2t, 7-2t)$.
Foot of perpendicular from $P(1,2,a)$: $\vec{PM} \cdot (3,2,-2) = 0$.
$3(5+3t)+2(5+2t)-2(7-2t-a) = 0$
$\Rightarrow 17t+11+2a = 0$.
Image $Q = 2M - P = (11+6t, 12+4t, 14-4t-a)$.
Given $Q_x = 5$: $11+6t = 5 \Rightarrow t = -1$.
From $17(-1)+11+2a = 0 \Rightarrow a = 3$.
$b = 12+4(-1) = 8$, $c = 14-4(-1)-3 = 15$.
$a^2+b^2+c^2 = 9+64+225 = 298$.

</details>

---

### Q29. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let the line $\mathrm{L}_{1}$ be parallel to the vector $-3 \hat{i}+2 \hat{j}+4 \hat{k}$ and pass through the point (2,6,7), and the line $\mathrm{L}_{2}$ be parallel to the vector $2 \hat{i}+\hat{j}+3 \hat{k}$ and pass through the point $(4,3,5)$. If the line $\mathrm{L}_{3}$ is parallel to the vector $-3 \hat{i}+5 \hat{j}+16 \hat{k}$ and intersects the lines $\mathrm{L}_{1}$ and $\mathrm{L}_{2}$ at the points C and D, respectively, then $|\overrightarrow{C D}|^{2}$ is equal to :

**Options:**

- **(A)** 89
- **(B)** 312
- **(C)** 171
- **(D)** 290

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 290**

**Detailed Solution:**

$L_1 : \dfrac{x-2}{-3} = \dfrac{y-6}{2} = \dfrac{z-7}{4}$
Point C on $L_1$: $(-3\lambda_1 + 2, 2\lambda_1 + 6, 4\lambda_1 + 7)$
$L_2 : \dfrac{x-4}{2} = \dfrac{y-3}{1} = \dfrac{z-5}{3}$
Point D on $L_2$: $(2\lambda_2 + 4, \lambda_2 + 3, 3\lambda_2 + 5)$
Dr's of line $L_3$ :
$L_3 : \dfrac{2\lambda_2 + 3\lambda_1 + 2}{-3} = \dfrac{\lambda_2 - 2\lambda_1 - 3}{5} = \dfrac{3\lambda_2 - 4\lambda_1 - 2}{16}$
$\lambda_1 = -3, \lambda_2 = 2$
$C(11, 0, -5)$
$D(8, 5, 11)$
$|\overrightarrow{CD}|^2 = 3^2 + 5^2 + 16^2 = 290$

</details>

---

### Q30. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the line $L$ pass through the point $(-3,5,2)$ and make equal angles with the positive coordinate axes. If the distance of L from the point $(-2, \mathrm{r}, 1)$ is $\sqrt{\frac{14}{3}}$, then the sum of all possible values of r is :

**Options:**

- **(A)** 10
- **(B)** 6
- **(C)** 12
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 10**

**Detailed Solution:**

Line $L$ through $(-3, 5, 2)$ making equal angles with axes has direction $(1, 1, 1)$.
Point $Q = (-2, r, 1)$, $\vec{PQ} = (1, r-5, -1)$.
$\vec{PQ} \times \vec{d} = (r-4, -2, 6-r)$.
$|\vec{PQ} \times \vec{d}|^2 = (r-4)^2 + 4 + (6-r)^2 = 2r^2 - 20r + 56$.
Distance $= \sqrt{\frac{2r^2 - 20r + 56}{3}} = \sqrt{\frac{14}{3}}$.
$2r^2 - 20r + 56 = 14 \Rightarrow r^2 - 10r + 21 = 0 \Rightarrow r = 3$ or $r = 7$.
Sum $= 3 + 7 = 10$.

</details>

---

### Q31. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $(\alpha, \beta, \gamma)$ be the co-ordinates of the foot of the perpendicular drawn from the point $(5,4,2)$ on the line $\overrightarrow{\mathrm{r}}=(-\hat{i}+3 \hat{j}+\hat{k})+\lambda(2 \hat{i}+3 \hat{j}-\hat{k})$. 
 Then the length of the projection of the vector $\alpha \hat{i}+\beta \hat{j}+\gamma \hat{k}$ on the vector $6 \hat{i}+2 \hat{j}+3 \hat{k}$ is :

**Options:**

- **(A)** $\frac{15}{7}$
- **(B)** 4
- **(C)** $\frac{18}{7}$
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{18}{7}$**

**Detailed Solution:**

Line: $\vec{r} = (-1, 3, 1) + \lambda(2, 3, -1)$, Point P = (5, 4, 2).
Any point on line: $Q = (-1 + 2\lambda, 3 + 3\lambda, 1 - \lambda)$.
$\vec{PQ} = (-6 + 2\lambda, -1 + 3\lambda, -1 - \lambda)$.
For perpendicular: $\vec{PQ} \cdot (2, 3, -1) = 0$ gives $14\lambda - 14 = 0$, so $\lambda = 1$.
Foot $(\alpha, \beta, \gamma) = (1, 6, 0)$.
Projection of $(1, 6, 0)$ on $(6, 2, 3)$: $\frac{|6 + 12 + 0|}{\sqrt{49}} = \frac{18}{7}$.

</details>

---

### Q32. JEE Main 2025 (8 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the area of the triangle formed by the lines $x+2=y-1=z, \frac{x-3}{5}=\frac{y}{-1}=\frac{z-1}{1}$ and $\frac{x}{-3}=\frac{y-3}{3}=\frac{z-2}{1}$ be $A$. Then $A^2$ is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **56**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{L}_1: \mathrm{x}+2=\mathrm{y}-1=\mathrm{z}=\ell \\
& \mathrm{L}_2: \frac{\mathrm{x}-3}{5}=\frac{\mathrm{y}}{-1}=\frac{\mathrm{z}-1}{1}=\mathrm{m} \\
& \mathrm{~L}_3: \frac{\mathrm{x}}{-3}=\frac{\mathrm{y}-3}{5}=\frac{\mathrm{z}-2}{1}=\mathrm{n}
\end{aligned}$
Point of intersection of $L_1$ and $L_2$
$\left.\begin{array}{r}
\ell-2=5 \mathrm{~m}+3 \\
\ell+1=-\mathrm{m} \\
\ell=\mathrm{m}+1
\end{array}\right\} \ell=0, \mathrm{~m}=-1 \quad \mathrm{~A}(-2,1,0)$
Point of intersection of $L_2$ and $L_3$
$\left.\begin{array}{l}
5 \mathrm{~m}+3=-3 \mathrm{n} \\
-\mathrm{m}=3 \mathrm{n}+3 \\
\mathrm{~m}+1=\mathrm{n}+2
\end{array}\right\} \mathrm{m}=0, \mathrm{n}=-1, B(3,0,1)$
Point of intersection $L_3$ and $L_4$
$\left.\begin{array}{r}
-3 \mathrm{n}=\ell-2 \\
3 \mathrm{n}+3=\ell+1 \\
\mathrm{n}+2=\ell
\end{array}\right\} \ell=2, \mathrm{n}=0, \mathrm{C}(0,3,2)$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0ojT2pARDslA5Mdkbyg13q6OJ-exSqiBGRGxVsLFwUE.original.fullsize.png"/>
$\begin{aligned} & \operatorname{Ar}(\Delta \mathrm{ABC})=\left|\frac{1}{2}\right| \begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ -5 & 1 & -1 \\ -3 & 3 & 1\end{array}| | \\ & \mathrm{A}=\frac{1}{2}|\hat{\mathrm{i}}(4)-\hat{\mathrm{j}}(-8)+\hat{\mathrm{k}}(-12)| \\ & \mathrm{A}=\frac{1}{2} \sqrt{16+64+144}=\sqrt{56} \\ & \mathrm{~A}^2=56\end{aligned}$

</details>

---

### Q33. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the values of $\lambda$ for which the shortest distance between the lines $\frac{x-1}{2}=\frac{y-2}{3}=\frac{z-3}{4}$ and $\frac{x-\lambda}{3}=\frac{y-4}{4}=\frac{z-5}{5}$ is $\frac{1}{\sqrt{6}}$ be $\lambda_1$ and $\lambda_2$. Then the radius of the circle passing through the points $(0,0),\left(\lambda_1, \lambda_2\right)$ and $\left(\lambda_2, \lambda_1\right)$ is

**Options:**

- **(A)** $\frac{5 \sqrt{2}}{3}$
- **(B)** 4
- **(C)** $\frac{\sqrt{2}}{3}$
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{5 \sqrt{2}}{3}$**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{\mathrm{p}}=2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+4 \hat{\mathrm{k}}, \overrightarrow{\mathrm{q}}=3 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+5 \hat{\mathrm{k}} \\ & \Rightarrow \overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{q}}=\left|\begin{array}{lll}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 2 & 3 & 4 \\ 3 & 4 & 5\end{array}\right|=-\hat{\mathrm{i}}+2 \hat{\mathrm{j}}-\hat{\mathrm{k}} \\ & \mathrm{A} \equiv(1,2,3) B \equiv(\lambda, 4,5) \\ & \text { Shortest Distance }=\left|\frac{\overrightarrow{\mathrm{AB}} \cdot(\overrightarrow{\mathrm{P}} \times \overrightarrow{\mathrm{q}})}{|\overrightarrow{\mathrm{P}} \times \overrightarrow{\mathrm{q}}|}\right|\end{aligned}$
$\begin{aligned}
& \frac{1}{\sqrt{6}}=\left|\frac{((\lambda-1) \hat{i}+2 \hat{j}+2 \hat{k}) \cdot(-\hat{i}+2 \hat{j}-\hat{k})}{\sqrt{6}}\right| \\
& \Rightarrow|-\lambda+1+4-2|=1 \Rightarrow|\lambda-3|=1 \\
& \Rightarrow \lambda=3 \pm 1=4,2
\end{aligned}$
Radius of circle passing through points
$\begin{aligned}
& (0,0),(4,2) \&(2,4) \\
& =\frac{\text { abc }}{4 \Delta}=\frac{\sqrt{20} \times \sqrt{20} \times \sqrt{8}}{4 \times \frac{1}{2}\left|\begin{array}{lll}
1 & 1 & 1 \\
0 & 4 & 2 \\
0 & 2 & 4
\end{array}\right|}=\frac{20 \times 2 \sqrt{2}}{2 \times 12} \\
& =\frac{5 \sqrt{2}}{3}
\end{aligned}$

</details>

---

### Q34. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If the equation of the line passing through the point $\left(0,-\frac{1}{2}, 0\right)$ and perpendicular to the lines $\vec{r}=\lambda(\hat{i}+a \hat{j}+b \hat{k})$ and
$\overrightarrow{\mathrm{r}}=(\hat{\mathrm{i}}-\hat{\mathrm{j}}-6 \hat{\mathrm{k}})+\mu(-b \hat{\mathrm{i}}+\mathrm{a} \hat{\mathrm{j}}+5 \hat{\mathrm{k}})$
is $\frac{\mathrm{x}-1}{-2}=\frac{\mathrm{y}+4}{\mathrm{~d}}=\frac{\mathrm{z}-\mathrm{c}}{-4}$, then $\mathrm{a}+\mathrm{b}+\mathrm{c}+\mathrm{d}$ is equal to :

**Options:**

- **(A)** 10
- **(B)** 14
- **(C)** 13
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 14**

**Detailed Solution:**

Line is $\perp^{\mathrm{r}}$ to 2 line $\Rightarrow$ line will be parallel to
$(i+a \hat{j}+b \hat{k}) \times(-b \hat{i}+a \hat{j}+5 \hat{k})$
Parallel vector along the required line is
$\hat{\mathrm{i}}(5 \mathrm{a}-\mathrm{ab})-\hat{\mathrm{j}}\left(\mathrm{~b}^2+5\right)+\hat{\mathrm{k}}(\mathrm{a}+\mathrm{ab})$
Dr's of required line $\alpha(5 a-a b),-\left(b^2+5\right),(a+a b)$
Also Dr's of required line $\alpha-2, \mathrm{~d},-4$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/XXhZzGYxoN-VV6XsK_d_RPtT0KLIB9zA0xnxji3eMcE.original.fullsize.png"/>
Also point $\left(0, \frac{-1}{2}, 0\right)$ will lie on $\frac{\mathrm{x}-1}{-2}=\frac{\mathrm{y}+4}{\mathrm{~d}}=\frac{\mathrm{z}-\mathrm{c}}{-4}$
$\frac{0-1}{-2}=\frac{\frac{-1}{2}+4}{d}=\frac{0-c}{-4} \Rightarrow d=7, c=2$
$\begin{aligned}
&\text { From (1) } \frac{5 \mathrm{a}-\mathrm{ab}}{-2}=\frac{-\mathrm{b}^2-5}{7}=\frac{\mathrm{a}+\mathrm{ab}}{-4}\\
&\frac{5 \mathrm{a}-\mathrm{ab}}{-2}=\frac{\mathrm{a}+\mathrm{ab}}{-4} ; \frac{-\mathrm{b}^2-5}{7}=\frac{\mathrm{a}+\mathrm{ab}}{-4}
\end{aligned}$
\begin{array}{c|c}-20 a+4 a b=-2 a-2 a b & 4 b^2+20=70+7 a b \\18 a=6 a b & 36+20=70+21 a \\b=3 & 56=28 a \Rightarrow a=2\end{array}
$a+b+c+d=2+3+2+7=14$

</details>

---

### Q35. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Consider the lines $\mathrm{L}_1: \mathrm{x}-1=\mathrm{y}-2=\mathrm{z}$ and $\mathrm{L}_2: \mathrm{x}-2=\mathrm{y}=\mathrm{z}-1$. Let the feet of the perpendiculars from the point $\mathrm{P}(5,1,-3)$ on the lines $\mathrm{L}_1$ and $\mathrm{L}_2$ be $Q$ and $R$ respectively. If the area of the triangle PQR is A , then $4 \mathrm{~A}^2$ is equal to :

**Options:**

- **(A)** 139
- **(B)** 147
- **(C)** 151
- **(D)** 143

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 147**

**Detailed Solution:**

$\begin{aligned} & \mathrm{L}_1: \frac{\mathrm{x}-1}{1}=\frac{\mathrm{y}-2}{1}=\frac{\mathrm{z}-0}{2} \\ & \text { Let } \mathrm{Q}(\lambda+1, \lambda+2, \lambda) \\ & \overrightarrow{\mathrm{PQ}}=(\lambda-4, \lambda-1, \lambda+3) \\ & \overrightarrow{\mathrm{PQ}} \cdot \overrightarrow{\mathrm{m}}=0\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/jeC_KZJ4HAjm2D0wnmAAeSX2r0tvXXWhtrAGs1ApF7s.original.fullsize.png"/>
$\begin{aligned} \Rightarrow & \lambda-4+\lambda+1, \lambda+3=0 \\ \Rightarrow & 3 \lambda=0 \\ & \lambda=0\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Uc442f6L0xxVWk7wnRWPnaxOnTm4B_9mif7mpoh1e9g.original.fullsize.png"/>
$\begin{aligned} & L_2: \frac{x-2}{1}=\frac{y-0}{1}=\frac{z-1}{2} \\ & \text { Let } \mathrm{R}(\mu+2, \mu, \mu+1) \overrightarrow{\mathrm{PR}}=(\mu-3, \mu-1, \mu+4) \\ & \overrightarrow{\mathrm{PR}} \cdot \overrightarrow{\mathrm{n}}=0 \\ & \mu-3+\mu-1+\mu+4=0 \\ & \neq \mu=0\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/MQ4x6zNubW0qK-ii-tO9ztn3HHpRGOYzIynVjum4iOc.original.fullsize.png"/>
$\begin{aligned} & \text { Area of } \triangle \mathrm{PQR}(\mathrm{A})=\frac{1}{2}|\overrightarrow{\mathrm{PQ}} \times \overrightarrow{\mathrm{PR}}| \\ & \mathrm{A}=\frac{1}{2}|(-4 \hat{\mathrm{i}}+\hat{\mathrm{j}}+3 \hat{\mathrm{k}}) \times(-3 \hat{\mathrm{i}}+\hat{\mathrm{j}}+4 \hat{\mathrm{k}})| \\ & \mathrm{A}=\frac{1}{2}|7(\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}})| \\ & \left|\begin{array}{crr}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ -4 & 1 & 3 \\ -3 & -1 & 4\end{array}\right| \\ & =7 \hat{\mathrm{i}}+7 \hat{\mathrm{j}}+7 \hat{\mathrm{k}} \\ & 4 \mathrm{~A}^2=49 \times 3=147\end{aligned}$

</details>

---

### Q36. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the line L pass through $(1,1,1)$ and intersect the lines $\frac{x-1}{2}=\frac{y+1}{3}=\frac{z-1}{4}$ and $\frac{x-3}{1}=\frac{y-4}{2}=\frac{z}{1}$ . Then, which of the following points lies on the line L ?

**Options:**

- **(A)** $(4,22,7)$
- **(B)** $(5,4,3)$
- **(C)** $(10,-29,-50)$
- **(D)** $(7,15,13)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(7,15,13)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/CDcU0duSunsrkhCgO0swlIxk-h0CM8zK51nxljBR7Jg.original.fullsize.png"/>
$\begin{aligned}
& \text { Dr's of } \mathrm{AC} \Rightarrow 2 \lambda, 3 \lambda-2,4 \lambda \\
& \text { Dr's of } \mathrm{BC} \Rightarrow \mu+2,2 \mu+3, \mu-1 \\
& \Rightarrow \frac{\mu+2}{2 \lambda}=\frac{2 \mu+3}{3 \lambda-2}=\frac{\mu-1}{4 \lambda} \\
& \Rightarrow 2(\mu+2)=\mu-1 \Rightarrow \mu=-5 \\
& \Rightarrow \text { Dr's of } \mathrm{BC} \Rightarrow 3,7,6 \\
& \Rightarrow \text { equation of } \mathrm{L} \Rightarrow \frac{\mathrm{x}-1}{3}=\frac{\mathrm{y}-1}{7}=\frac{\mathrm{z}-1}{6}
\end{aligned}$
$(7,15,13) \text { satisfies. }$

</details>

---

### Q37. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the shortest distance between the lines $\frac{x-1}{2}=\frac{y-2}{3}=\frac{z-3}{4}$ and $\frac{x}{1}=\frac{y}{\alpha}=\frac{z-5}{1}$ is $\frac{5}{\sqrt{6}}$, then the sum of all possible values of $\alpha$ is

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** $-\frac{3}{2}$
- **(C)** 3
- **(D)** -3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -3**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qklevskaGfrd03QPj_rQHq0ZPOB5L1sF-kb9MChveWc.original.fullsize.png"/>
$\begin{aligned} & L_1: \frac{x-1}{2}=\frac{y-2}{3}=\frac{z-3}{4} \\ & L_1: \frac{x}{1}=\frac{y}{\alpha}=\frac{z-5}{1} \\ & \vec{x}=\left|\begin{array}{ccc}\hat{i} & \hat{j} & \hat{k} \\ 2 & 3 & 4 \\ 1 & \alpha & 1\end{array}\right|=\hat{\mathrm{i}}(3-4 \alpha)-\hat{\mathrm{j}}(-2)+\hat{\mathrm{k}}(2 \alpha-3) \\ & \text { S.D. }=\left|\frac{\overrightarrow{\mathrm{BA}} \cdot \overrightarrow{\mathrm{n}}}{|\overrightarrow{\mathrm{n}}|}\right|=\left|\frac{(\hat{\mathrm{i}}+2 \hat{\mathrm{j}}-2 \hat{\mathrm{k}}) \cdot \vec{n}}{|\overrightarrow{\mathrm{n}}|}\right| \\ & \Rightarrow 6(13-8 \alpha)^2=25\left((4 \alpha-3)^2+(2 \alpha-3)^2+16\right) \\ & 6\left(64 a^2-280 \alpha+169\right)=25\left(20 \alpha^2-36 \alpha+34\right) \\ & \Rightarrow 116 \alpha^2+348 \alpha-164=0 \\ & \alpha_1+\alpha_2=\frac{-348}{116}=-3\end{aligned}$

</details>

---

### Q38. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A$ be the point of intersection of the lines $L_1: \frac{x-7}{1}=\frac{y-5}{0}=\frac{z-3}{-1}$ and $L_2: \frac{x-1}{3}=\frac{y+3}{4}=\frac{z+7}{5}$. Let $B$ and $C$ be the point on the lines $L_1$ and $L_2$ respectively such that $\mathrm{AB}=\mathrm{AC}=\sqrt{15}$. Then the square of the area of the triangle ABC is :

**Options:**

- **(A)** $54$
- **(B)** $63$
- **(C)** $57$
- **(D)** $60$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $54$**

**Detailed Solution:**

Angle between both lines
$\begin{aligned}
& \cos \theta=\left|\frac{3+0-5}{\sqrt{2} \sqrt{50}}\right| \\
& \sin \theta=\frac{2}{10}=\frac{1}{5} \\
& \sin \theta=\frac{\sqrt{24}}{5} \\
& \text { area }=\frac{1}{2} a b \sin \theta \\
& \frac{1}{2} \sqrt{15} \sqrt{15} \frac{\sqrt{24}}{5}
\end{aligned}$
square of area $\frac{15.15 .24}{4.25}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZcRAmHdBjzJJ5v3hdjAx18kzES6v61r7YtwiyX_nhw8.original.fullsize.png"/>
option (1)

</details>

---

### Q39. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the values of p , for which the shortest distance between the lines $\frac{x+1}{3}=\frac{y}{4}=\frac{z}{5}$ and $\overrightarrow{\mathrm{r}}=(\mathrm{p} \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}})+\lambda(2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+4 \hat{\mathrm{k}})$ is $\frac{1}{\sqrt{6}}$, be $\mathrm{a}, \mathrm{b}$, $(a \lt b)$. Then the length of the latus rectum of the ellipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ is :-

**Options:**

- **(A)** $9$
- **(B)** $\frac{3}{2}$
- **(C)** $\frac{2}{3}$
- **(D)** $18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{3}$**

**Detailed Solution:**

$\text { shortest distance }=\frac{|(\overline{\mathrm{a}}-\overline{\mathrm{b}})| \cdot(\overline{\mathrm{p}} \times \overline{\mathrm{q}})}{|\overline{\mathrm{p}} \times \overline{\mathrm{q}}|}$
where
$\begin{aligned}
& \overline{\mathrm{a}}=-\hat{\mathrm{i}}+0 \hat{\mathrm{j}}+0 \hat{\mathrm{k}} \\
& \overline{\mathrm{~b}}=\mathrm{p} \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}} \\
& \overline{\mathrm{p}}=3 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+5 \hat{\mathrm{k}}-\overline{\mathrm{b}}=(-1-\mathrm{p}) \hat{\mathrm{i}}-2 \hat{\mathrm{j}}-\hat{\mathrm{k}} \\
& \overline{\mathrm{q}}=2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+4 \hat{\mathrm{k}} \\
& \frac{1}{16}=\frac{|-1-\mathrm{p}+4-1|}{\sqrt{6}} \\
& |-\mathrm{p}+2|=1 \\
& \mathrm{p}=3 \\
& \frac{\mathrm{x}^2}{1^2}+\frac{\mathrm{y}^2}{3^3}=1 \\
& \mathrm{~L} \cdot \mathrm{R}=\frac{2 \mathrm{a}^2}{\mathrm{~b}}=\frac{2 \times 1}{3}=\frac{2}{3}
\end{aligned}$
option (3)

</details>

---

### Q40. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let A and B be two distinct points on the line $\mathrm{L}: \frac{\mathrm{x}-6}{3}=\frac{\mathrm{y}-7}{2}=\frac{\mathrm{z}-7}{-2}$. Both A and B are at a distance $2 \sqrt{17}$ from the foot of perpendicular drawn from the point $(1,2,3)$ on the line L . If O is the origin, then $\overrightarrow{O A} \cdot \overrightarrow{O B}$ is equal to:

**Options:**

- **(A)** 49
- **(B)** 47
- **(C)** 21
- **(D)** 62

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 47**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4wR5uA4PZrJZtaeU5x8HWLQSJIycknRSJv5hFubs9TE.original.fullsize.png"/>
$\begin{aligned}
& \overrightarrow{\mathrm{PQ}} \cdot \overrightarrow{\mathrm{~b}}=0 \\
& \Rightarrow 3(3 \lambda+5)+2(2 \lambda+5)-2(-2 \lambda+4) \\
& \Rightarrow 17 \lambda=-17 \Rightarrow \lambda=-1 \\
& \mathrm{Q}(3,5,9)
\end{aligned}$
Let A $(3 \mu+6,2 \mu+7,-2 \mu+7)$
$(3 \mu+3)^2+(2 \mu+2)^2+(-2 \mu-2)^2=68$
$\Rightarrow \mu^2+2 \mu-3=0 \mu=-3 \text { or } \mu=1$
A $(-3,1,13)$ and $B(9,9,5)$
$\overrightarrow{\mathrm{OA}} \cdot \overrightarrow{\mathrm{OB}}=-27+9+65=47$

</details>

---

### Q41. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the shortest distance between the lines $\frac{x-3}{3}=\frac{y-\alpha}{-1}=\frac{z-3}{1}$ and $\frac{x+3}{-3}=\frac{y+7}{2}=\frac{z-\beta}{4}$ be $3 \sqrt{30}$. Then the positive value of $5 \alpha+\beta$ is

**Options:**

- **(A)** 42
- **(B)** 46
- **(C)** 48
- **(D)** 40

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 46**

**Detailed Solution:**

$\begin{aligned} & {\mathrm{A}(3, \alpha, 3) \& B(-3,-7, \beta)} \\ & \overrightarrow{\mathrm{BA}}=6 \hat{\mathrm{i}}+(\alpha+7) \hat{\mathrm{j}}+(3-\beta) \hat{\mathrm{k}} \\ \end{aligned}$
$\overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{q}}=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 3 & -1 & 1 \\ -3 & 2 & 4\end{array}\right|$
$\frac{|\overrightarrow{\mathrm{BA}} \cdot(\overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{q}})|}{|\overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{q}}|}=3 \sqrt{30}$
$36+15(\alpha+7)-3(3-\beta)=(3 \sqrt{30})^2$
$\begin{aligned} & 36+15 \alpha+105-9+3 \beta=270 \\ & 15 \alpha+3 \beta=138 \\ & 5 \alpha+\beta=46\end{aligned}$

</details>

---

### Q42. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The distance of the point $(7,10,11)$ from the line $\frac{x-4}{1}=\frac{y-4}{0}=\frac{z-2}{3}$ along the line $\frac{x-9}{2}=\frac{y-13}{3}=\frac{z-17}{6}$ is

**Options:**

- **(A)** $18$
- **(B)** $14$
- **(C)** $12$
- **(D)** $16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $14$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/aPNH2OD6-UrcO0q04mm2kt8Z1NqJI-9cQy6D6AVY--c.original.fullsize.png"/>
$\because$ line $P Q$ is parallel to line $\frac{x-9}{2}=\frac{y-3}{3}=\frac{z-17}{6}$
$\begin{aligned}
& \therefore \frac{\lambda-3}{2}=\frac{-6}{3}=\frac{3 \lambda-9}{6} \Rightarrow \lambda=-1 \\
& Q=(3,4,-1) \\
& \therefore P Q=\sqrt{16+36+144}=14
\end{aligned}$

</details>

---

### Q43. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Line $L_1$ passes through the point $(1,2,3)$ and is parallel to Z -axis. Line $\mathrm{L}_2$ passes through the point $(\lambda, 5,6)$ and is parallel to $y$-axis. Let for $\lambda=\lambda_1, \lambda_2, \lambda_2 \lt \lambda_1$, the shortest distance between the two lines be 3 . Then the square of the distance of the point $\left(\lambda_1, \lambda_2, 7\right)$ from the line $\mathrm{L}_1$ is

**Options:**

- **(A)** $40$
- **(B)** $32$
- **(C)** $25$
- **(D)** $37$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $25$**

**Detailed Solution:**

$\begin{aligned} & L_1 \equiv \frac{x-1}{0}=\frac{y-2}{0}=\frac{z-3}{1} \\ & L_2 \equiv \frac{x-\lambda}{0}=\frac{y-5}{1}=\frac{z-6}{0}\end{aligned}$
$\mathrm{SD}=\frac{\left|\begin{array}{ccc}\lambda-1 & 3 & 3 \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{array}\right|}{\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{array}\right|}$
$=|\lambda-1|=3$
$\begin{aligned}
& \lambda=4,-2 \\
& \lambda_1=4 \\
& \lambda_2=-2
\end{aligned}$
Let foot of perpendicular from
$\begin{aligned}
& \mathrm{P}(4,-2,7) \text { is } \mathrm{Q}(1,2, \mathrm{t}+3) \\
& \mathrm{So}(3,-4,4-\mathrm{t}) \cdot(0,0,1)=0 \\
& \mathrm{t}=4
\end{aligned}$
$\begin{aligned}
& \mathrm{So} \mathrm{Q}(1,2,7) \\
& \mathrm{PQ}^2=9+16 \\
& \mathrm{PQ}^2=25
\end{aligned}$

</details>

---

### Q44. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let a line passing through the point $(4,1,0)$ intersect the line $L_1 ; \frac{x-1}{2}=\frac{y-2}{3}=\frac{z-3}{4}$ at the point $\mathrm{A} \quad(\alpha, \beta, \gamma)$ and the line $L_2: x-6=y=-z+4$ at the point $B(a, b, c)$.
Then $\left|\begin{array}{lll}1 & 0 & 1 \\ \alpha & \beta & \gamma \\ \mathrm{a} & \mathrm{b} & \mathrm{c}\end{array}\right|$ is equal to

**Options:**

- **(A)** $8$
- **(B)** $16$
- **(C)** $12$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $8$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/s-NV8NFU4tJw4XhKtXizAkNAIlr9ZnTwopOLZDwBMCA.original.fullsize.png"/>
$\begin{aligned} & L_1=\frac{x-1}{2}=\frac{y-2}{3}=\frac{z-3}{4}=p \\ & L_2=\frac{x-6}{1}=\frac{y}{1}=\frac{z-4}{-1}=q \\ & A(2 p+1,3 p+2,4 p+3) \\ & B(q+6, q, 4-q) \\ & \text { D.R. of } P A=2 p-3,3 P+1,4 p+3 \\ & \text { D.R. of } P B=q+2, q-1,4-q \\ & \frac{2 p-3}{q+2}=\frac{3 p+1}{q-1}=\frac{4 p+3}{4-q}\end{aligned}$
$\begin{aligned}
& 2 p q-2 p-3 q+3=3 p q+6 p+q+2 \\
& \mathrm{pq}+\mathrm{rp}+4 \mathrm{q}-1=0 \\
& 12 p-3 p q+4-q=4 p q+3 q-4 p-3 \\
& 7 p q-16 p+4 q-7=0 \\
& 8 p-2 p q-12+3 q=4 p q+8 p+3 q+6 \\
& 6 \mathrm{pq}=-18 \quad \therefore \mathrm{pq}=-3 \\
& 8 p+4 q=4 \quad \Rightarrow 2 p+q=1 \\
& -21-16 p+4 q-7 \quad \Rightarrow 4 p-q=-7 \\
& 16 \mathrm{p}-4 \mathrm{q}=-28 \quad \therefore \mathrm{p}=-1, \mathrm{q}=3 \\
& \mathrm{~A}(-1,-1,-1) \quad \mathrm{B}(9,3,1)
\end{aligned}$
$\left|\begin{array}{ccc}1 & 0 & 1 \\ -1 & -1 & -1 \\ 9 & 3 & 1\end{array}\right|=\left|\begin{array}{ccc}0 & -1 & 0 \\ -1 & -1 & -1 \\ 9 & 3 & 1\end{array}\right|=1(-1+9)=8$

</details>

---

### Q45. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the image of the point $\mathrm{P}(1,0,3)$ in the line joining the points $\mathrm{A}(4,7,1)$ and $\mathrm{B}(3,5,3)$ is $\mathrm{Q}(\alpha, \beta, \gamma)$, then $\alpha+\beta+\gamma$ is equal to

**Options:**

- **(A)** $\frac{47}{3}$
- **(B)** $\frac{46}{3}$
- **(C)** $18$
- **(D)** $13$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{46}{3}$**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{P}(1,0,3) \\
& \mathrm{A}(4,7,1), \mathrm{B}(3,5,3) \\
& \text { Line } \mathrm{AB} \Rightarrow \frac{\mathrm{x}-3}{1}=\frac{\mathrm{y}-5}{2}=\frac{\mathrm{z}-3}{-2}=\lambda
\end{aligned}$
Let foot of perpendicular of P on AB be
$\begin{aligned} & \mathrm{R} \equiv(\lambda+3,2 \lambda+5,-2 \lambda+3) \\ & \Rightarrow(\lambda+3-1)(1)+(2 \lambda+5-0)(2)+(-2 \lambda+3-3) \\ & (-2)=0 \\ & \Rightarrow \lambda+2+4 \lambda+10+4 \lambda=0 \\ & \Rightarrow \lambda=-\frac{4}{3} \\ & \Rightarrow \mathrm{R} \equiv\left(\frac{5}{3}, \frac{7}{3}, \frac{17}{3}\right) \\ & \mathrm{Q} \equiv\left(\frac{10}{3}-1, \frac{14}{3}-0, \frac{34}{3}-3\right) \equiv\left(\frac{7}{3}, \frac{14}{3}, \frac{25}{3}\right) \\ & \Rightarrow \alpha+\beta+\gamma=\frac{7+14+25}{3}=\frac{46}{3}\end{aligned}$

</details>

---

### Q46. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The line $L_1$ is parallel to the vector $\vec{a}=-3 \hat{i}+2 \hat{j}+4 \hat{k}$ and passes through the point $(7,6,2)$ and the line $L_2$ is parallel to the vector $\vec{b}=2 \hat{i}+\hat{j}+3 \hat{k}$ and passes through the point $(5,3,4)$. The shortest distance between the lines $L_1$ and $L_2$ is :

**Options:**

- **(A)** $\frac{23}{\sqrt{38}}$
- **(B)** $\frac{21}{\sqrt{57}}$
- **(C)** $\frac{23}{\sqrt{57}}$
- **(D)** $\frac{21}{\sqrt{38}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{23}{\sqrt{38}}$**

**Detailed Solution:**

$\begin{aligned} & L_1:(7 \hat{i}+6 \hat{j}+2 k)+\lambda(-3 \hat{i}+2 \hat{j}+4 k) \\ & L_2:(5 \hat{i}+3 \hat{j}+4 k)+\lambda(2 \hat{i}+\hat{j}+3 k)\end{aligned}$
Distance between skew lines
$\begin{aligned} & =\frac{(2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}-2 \hat{\mathrm{k}}) \cdot(2 \hat{\mathrm{i}}+17 \hat{\mathrm{j}}-7 \hat{\mathrm{k}})}{\sqrt{342}} \\ & =\frac{69}{\sqrt{342}}=\frac{69}{3 \sqrt{38}}=\frac{23}{\sqrt{38}}\end{aligned}$

</details>

---

### Q47. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the vertices $Q$ and $R$ of the triangle $P Q R$ lie on the line $\frac{x+3}{5}=\frac{y-1}{2}=\frac{z+4}{3}, Q R=5$ and the coordinates of the point $P$ be $(0,2,3)$. If the area of the triangle $P Q R$ is $\frac{m}{n}$ then :

**Options:**

- **(A)** $\mathrm{m}-5 \sqrt{21} \mathrm{n}=0$
- **(B)** $2 \mathrm{~m}-5 \sqrt{21} \mathrm{n}=0$
- **(C)** $5 \mathrm{~m}-2 \sqrt{21} \mathrm{n}=0$
- **(D)** $5 m-21 \sqrt{2} n=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \mathrm{~m}-5 \sqrt{21} \mathrm{n}=0$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/n82HzxhTcZnoqId4AkS1dZNJzt0P74BrZMZ11auEfM8.original.fullsize.png"/>
$\mathrm{M}(5 \lambda-3,2 \lambda+1,3 \lambda-4)$
Drs of PM $\Rightarrow 5 \lambda-3,2 \lambda-1,3 \lambda-7$
Drs of line $L \Rightarrow 5,2,3$
$\mathrm{PM} \perp \mathrm{L}$
$\Rightarrow(5 \lambda-3) 5+(2 \lambda-1) 2+(3 \lambda-7) 3=0$
$\Rightarrow \lambda=1$
$\therefore \mathrm{M}(2,3,-1)$
$P M=\sqrt{4+1+16}=\sqrt{21}$
Area $=\frac{1}{2} \times 5 \times \sqrt{21}=\frac{\mathrm{m}}{\mathrm{n}}$
$2 \mathrm{~m}-5 \sqrt{21} \mathrm{n}=0$

</details>

---

### Q48. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let a straight line $L$ pass through the point $P(2,-1,3)$ and be perpendicular to the lines $\frac{x-1}{2}=\frac{y+1}{1}=\frac{z-3}{-2}$ and $\frac{x-3}{1}=\frac{y-2}{3}=\frac{z+2}{4}$. If the line $L$ intersects the $y z$-plane at the point $Q$, then the distance between the points $P$ and $Q$ is :

**Options:**

- **(A)** $\sqrt{10}$
- **(B)** $2 \sqrt{3}$
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

Vector parallel to $L$
$\begin{aligned}
& =\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
2 & 1 & -2 \\
1 & 3 & 4
\end{array}\right|=10 \hat{i}-10 \hat{j}+5 \hat{k} \\
& =5(2 \hat{i}-2 \hat{j}+\hat{k})
\end{aligned}$

Equation of ' $L$ '
$\frac{x-2}{2}=\frac{y+1}{-2}=\frac{z-3}{1}=\lambda(\text { say })$

Let $Q(2 \lambda+2,-2 \lambda-1, \lambda+3)$
$\begin{aligned}
& \Rightarrow \quad 2 \lambda+2=0 \Rightarrow \lambda=-1 \\
& \Rightarrow Q(0,1,2) \\
& d(P, Q)=3
\end{aligned}$

</details>

---

### Q49. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let P be the foot of the perpendicular from the point $(1,2,2)$ on the line $\mathrm{L}: \frac{x-1}{1}=\frac{y+1}{-1}=\frac{z-2}{2}$. Let the line $\vec{r}=(-\hat{i}+\hat{j}-2 \hat{k})+\lambda(\hat{i}-\hat{j}+\hat{k}), \lambda \in \mathbf{R}$, intersect the line L at Q . Then $2(\mathrm{PQ})^2$ is equal to :

**Options:**

- **(A)** 25
- **(B)** 19
- **(C)** 29
- **(D)** 27

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 27**

**Detailed Solution:**

General point on line $\mathrm{L}: \frac{x-1}{1}=\frac{y+1}{-1}=\frac{z-2}{2}$ 
is $(\lambda+1,-\lambda-1,2 \lambda+2)$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/q-IzyI23ics2s6SZ8UVSrT4riuTV4gVowaUuQHOOjSs.original.fullsize.png">

DR's of PM are $(\lambda,-\lambda-3,2 \lambda)$
$P M \perp L$
$\begin{aligned}
& \Rightarrow \lambda+(-1)(-\lambda-3)+2(2 \lambda)=0 \\
& \Rightarrow 6 \lambda+3=0
\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/s6yglrev1chd9M6aBk0I05FzcWUkL7_4X8hwLADHGek.original.fullsize.png">

$P\left(\frac{1}{2}, \frac{-1}{2}, 1\right)$

Let another line $L^{\prime}: \frac{x+1}{1}=\frac{y-1}{-1}=\frac{z+2}{1}$
General point on line $L^{\prime}$ is $(\mu-1,-\mu+1, \mu-2)$ 
Point of intersection of line $L$ and $L^{\prime}$ is
$\begin{array}{l|l}
\lambda+1=\mu-1 & 2 \lambda+2=\mu-2 \\
\Rightarrow \mu-\lambda=2 \ldots(1) & \Rightarrow 2 \lambda=\mu-4
\end{array}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/tv00fIUHl_p5piJ_sZzeDfj2UVox06HIZYHs0AXJfoI.original.fullsize.png">

$\begin{aligned} & Q(-1,1,-2) \\ & 2(P Q)^2=2\left(\left(\frac{1}{2}+1\right)^2+\left(\frac{-1}{2}-1\right)^2+(1+2)^2\right) \\ & =2\left(\frac{9}{4}+\frac{9}{4}+9\right) \\ & =27\end{aligned}$

</details>

---

### Q50. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let \(\mathrm{L}_1: \frac{x-1}{1}=\frac{y-2}{-1}=\frac{z-1}{2}\) and \(\mathrm{L}_2: \frac{x+1}{-1}=\frac{y-2}{2}=\frac{z}{1}\) be two lines.
Let \(L_3\) be a line passing through the point \((\alpha, \beta, \gamma)\) and be perpendicular to both \(L_1\) and \(L_2\). If \(L_3\) intersects \(\mathrm{L}_1\), then \(|5 \alpha-11 \beta-8 \gamma|\) equals :

**Options:**

- **(A)** 20
- **(B)** 18
- **(C)** 25
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 25**

**Detailed Solution:**

$\begin{aligned} & \text { DR's of } L_3=\overrightarrow{\mathrm{m}} \times \overrightarrow{\mathrm{n}}=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 1 & -1 & 2 \\ -1 & 2 & 1\end{array}\right| \\ & =-5 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+\hat{\mathrm{k}} \\ & L_3: \frac{x-\alpha}{-5}=\frac{y-\beta}{-3}=\frac{z-\gamma}{1}=\lambda \\ & \quad A(\alpha-5 \lambda, \beta-3 \lambda, \gamma+\lambda) \\ & L_1: \frac{x-1}{1}=\frac{y-2}{-1}=\frac{z-1}{2}=k\end{aligned}$


$\mathrm{B}(\mathrm{k}+1,-\mathrm{k}+2,2 \mathrm{k}+1)$

Now
$\begin{aligned}
& \alpha-5 \lambda=\mathrm{k}+1 \Rightarrow \alpha=5 \lambda+\mathrm{k}+1 \\
& \beta-3 \lambda=-\mathrm{k}+2 \Rightarrow \beta=3 \lambda-\mathrm{k}+2 \\
& \gamma+\lambda=2 \mathrm{k}-1 \Rightarrow \gamma=-\lambda+2 \mathrm{k}+1 \\
& |5 \alpha-11 \beta-8 \gamma|=|-25| \\
& =25
\end{aligned}$

</details>

---

### Q51. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let \(\overrightarrow{\mathrm{a}}=\hat{i}+2 \hat{j}+\hat{k}\) and \(\quad \overrightarrow{\mathrm{b}}=2 \hat{i}+7 \hat{j}+3 \hat{k} . \quad\) Let \(\mathrm{L}_1: \overrightarrow{\mathrm{r}}=(-\hat{i}+2 \hat{j}+\hat{k})+\lambda \overrightarrow{\mathrm{a}}, \lambda \in \mathbf{R}\) and \(\mathrm{L}_2: \overrightarrow{\mathrm{r}}=(\hat{j}+\hat{k})+\mu \overrightarrow{\mathrm{b}}, \mu \in \mathbf{R}\) be two lines. If the line \(\mathrm{L}_3\) passes through the point of intersection of \(\mathrm{L}_1\) and \(L_2\), and is parallel to \(\vec{a}+\vec{b}\), then \(L_3\) passes through the point :

**Options:**

- **(A)** \((5,17,4)\)
- **(B)** \((2,8,5)\)
- **(C)** \((8,26,12)\)
- **(D)** \((-1,-1,1)\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) \((8,26,12)\)**

**Detailed Solution:**

$\begin{aligned} & L_1: \overrightarrow{\mathrm{r}}=(-\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}})+\lambda(\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}}) \\ & \Rightarrow \overrightarrow{\mathrm{r}}=(\lambda-1) \hat{\mathrm{i}}+2(\lambda+1) \hat{\mathrm{j}}+(\lambda+1) \hat{\mathrm{k}} \\ & \mathrm{L}_2: \overrightarrow{\mathrm{r}}=(\hat{\mathrm{j}}+\hat{\mathrm{k}})+\mu(2 \hat{\mathrm{i}}+7 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}) \\ & \Rightarrow \overrightarrow{\mathrm{r}}=2 \mu \hat{\mathrm{i}}+(1+7 \mu) \hat{\mathrm{j}}+(1+3 \mu) \hat{\mathrm{k}}\end{aligned}$


For point of intersection equating respective components
$\begin{aligned}
& \Rightarrow \lambda-1=2 \mu \\
& 2(\lambda+1)=1+7 \mu \\
& \lambda+1=1+3 \mu
\end{aligned}$

We get
$\begin{aligned}
& \Rightarrow \lambda=3 \text { and } \mu=1 \\
& \Rightarrow \vec{a}+\vec{b}=3 \hat{i}+9 \hat{j}+4 \hat{k}
\end{aligned}$
$\mathrm{L}_3: \overrightarrow{\mathrm{r}}=2 \hat{\mathrm{i}}+8 \hat{\mathrm{j}}+4 \hat{\mathrm{k}}+\alpha(3 \hat{\mathrm{i}}+9 \hat{\mathrm{j}}+4 \hat{\mathrm{k}})$

For $\alpha=2, \overrightarrow{\mathrm{r}}=8 \hat{\mathrm{i}}+26 \hat{\mathrm{j}}+12 \hat{\mathrm{k}}$

</details>

---

### Q52. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The square of the distance of the point $\left(\frac{15}{7}, \frac{32}{7}, 7\right)$ from the line $\frac{x+1}{3}=\frac{y+3}{5}=\frac{z+5}{7}$ in the direction of the vector $\hat{i}+4 \hat{j}+7 \hat{k}$ is :

**Options:**

- **(A)** $54$
- **(B)** $44$
- **(C)** $41$
- **(D)** $66$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $66$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/BZVOD45mPAqEbSZ_2z1MdVvcPgi4E_UZcvCHJao-EyI.original.fullsize.png">




$\begin{aligned} & L=\frac{x+1}{3}=\frac{y+3}{5}=\frac{z+5}{7} \\ & P Q=\frac{x-\frac{15}{7}}{1}=\frac{y-\frac{32}{7}}{4}=\frac{z-7}{7}=\lambda\end{aligned}$


$\Rightarrow \mathrm{Q}\left(\lambda+\frac{15}{7}, 4 \lambda+\frac{32}{7}, 7 \lambda+7\right)$

Since Q lies on line L
$\begin{aligned}
& \text { So, } \frac{\lambda+\frac{15}{7}+1}{3}=\frac{7 \lambda+7+5}{7} \\
& \Rightarrow 7 \lambda+22=21 \lambda+36 \\
& \Rightarrow \lambda=-1 \\
& \therefore \text { Point } Q\left(\frac{8}{7}, \frac{4}{7}, 0\right) \\
& \mathrm{PQ}=\sqrt{\left(\frac{15}{7}-\frac{8}{7}\right)^2+\left(\frac{32}{7}-\frac{4}{7}\right)^2+(7-0)} \\
& \mathrm{PQ}=\sqrt{66} \\
& \Rightarrow(\mathrm{PQ})^2=66
\end{aligned}$

</details>

---

### Q53. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the image of the point $(4,4,3)$ in the line $\frac{x-1}{2}=\frac{y-2}{1}=\frac{z-1}{3}$ is $(\alpha, \beta, \gamma)$, then $\alpha+\beta+\gamma$ is equal to

**Options:**

- **(A)** 9
- **(B)** 12
- **(C)** 7
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 9**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/tnuqsCY_sIiIPOh46oSG6vZUBZGbO8Xns8UMTzWH9cQ.original.fullsize.png">

Let coordinate of $R=(2 r+1, r+2,3 r+1)$
$\because \quad P R$ is perpendicular to given line.
$\therefore(2 r-3) \cdot 2+(r-2) \cdot 1+(3 r-2) \cdot 3=0$
$\therefore r=1$
$\therefore$ Coordinate of $R=(3,3,4)$
$\therefore \quad(\alpha, \beta, \gamma)=(2,2,5)$
$\therefore \alpha+\beta+\gamma=9$

</details>

---

### Q54. JEE Main 2025 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let P be the image of the point $\mathrm{Q}(7,-2,5)$ in the line $\mathrm{L}: \frac{x-1}{2}=\frac{y+1}{3}=\frac{z}{4}$ and $\mathrm{R}(5, \mathrm{p}, \mathrm{q})$ be a point on $L$. Then the square of the area of $\triangle P Q R$ is  ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **957**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/W5CvPNvA0o048BJgmPnLbMDXsqxy2kN42ach3SBKatA.original.fullsize.png">




$\begin{aligned} & \text { Let } \mathrm{R}(2 \lambda+1,3 \lambda-1,4 \lambda) \\ & 2 \lambda+1=5 \\ & \lambda=2 \\ & \mathrm{R}(5,5,8) \\ & \text { let } \mathrm{T}(2 \lambda+1,3 \lambda-1,4 \lambda) \\ & \overrightarrow{\mathrm{QT}}=(2 \lambda-6) \hat{\mathrm{i}}+(3 \lambda+1) \hat{\mathrm{j}}+(4 \lambda-5) \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{b}}=2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+4 \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{QT}} \cdot \overrightarrow{\mathrm{b}}=0 \\ & 4 \lambda-12+9 \lambda+3+16 \lambda-20=0\end{aligned}$



$\begin{aligned} & \lambda=1 \\ & \mathrm{~T}(3,2,4) \\ & \mathrm{QT}=\sqrt{33} \quad \mathrm{RT}=\sqrt{29} \\ & (\text { area of } \Delta \mathrm{PQR})^2=\left(\frac{1}{2} \sqrt{29} \cdot 2 \sqrt{33}\right)^2 \\ & =957\end{aligned}$

</details>

---

### Q55. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the line passing through the points $(-1,2,1)$ and parallel to the line $\frac{x-1}{2}=\frac{y+1}{3}=\frac{z}{4}$ intersect the line $\frac{x+2}{3}=\frac{y-3}{2}=\frac{z-4}{1}$ at the point $P$. Then the distance of $P$ from the point $Q(4,-5,1)$ is

**Options:**

- **(A)** $5$
- **(B)** $5 \sqrt{5}$
- **(C)** $5 \sqrt{6}$
- **(D)** $10$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $5 \sqrt{5}$**

**Detailed Solution:**

Equation of line through point $(-1,2,1)$ is $\rightarrow$
<img src="https://cdn.quizrr.in/question-assets/jee_main_pyq/9wiWdk1uICGLSVsSPtwgw4t6RXm67rHLxA2-TTO7Hvk.original.fullsize.png">
$\begin{aligned} & \Rightarrow \frac{x+1}{2}=\frac{y-2}{3}=\frac{z-1}{4}=\lambda-(2) \\ & \text {So, }\left[\begin{array}{l}x=2 \lambda-1 \\ y=3 \lambda+2 \\ z=4 \lambda+1\end{array}\right.\end{aligned}$
$\operatorname{By}(1) \rightarrow \frac{x+2}{3}=\frac{y-3}{2}=\frac{z-4}{1}=\mu($ Let $)$
So, $\left[\begin{array}{l}x=3 \mu-2 \\ y=2 \mu+3 \\ z=\mu+4\end{array}\right.$
For intersection point ' P '
$\begin{aligned}
& \mathrm{x}=2 \lambda-1=3 \mu-2 \\
& \mathrm{y}=3 \lambda+2=2 \mu+3 \\
& \mathrm{z}=4 \lambda+1=\mu+4
\end{aligned}$
So, point $\mathrm{P}(\mathrm{x}, \mathrm{y}, \mathrm{z})=(1,5,5)$
& $\mathrm{Q}(4,-5,1)$
$\begin{aligned}
& \therefore P Q=\sqrt{9+100+16} \\
& =\sqrt{125}=5 \sqrt{5}
\end{aligned}$

</details>

---

### Q56. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let in a $\triangle A B C$, the length of the side $A C$ be 6 , the vertex $B$ be $(1,2,3)$ and the vertices $A, C$ lie on the line $\frac{x-6}{3}=\frac{y-7}{2}=\frac{z-7}{-2}$. Then the area (in sq. units) of $\triangle \mathrm{ABC}$ is:

**Options:**

- **(A)** $17$
- **(B)** $21$
- **(C)** $56$
- **(D)** $42$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $21$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3Q6xNiUeREIPTwKuGiNat0syzRL8Nl1aKJuFkGpUyF4.original.fullsize.png">


$\begin{aligned} & \text { Let } \mathrm{M}(3 \lambda+6,2 \lambda+7,-2 \lambda+7) \\ & \overrightarrow{\mathrm{BM}}=(3 \lambda+5) \hat{\mathrm{i}}+(2 \lambda+5) \hat{\mathrm{j}}+(-2 \lambda+4) \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{AC}} \cdot \overrightarrow{\mathrm{BM}}=0=3(3 \lambda+5)+2(2 \lambda+5)-2(-2 \lambda+4) \\ & \overrightarrow{\mathrm{BM}}=2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+6 \hat{\mathrm{k}} \\ & \mid \overrightarrow{\mathrm{BM}}=7 \\ & \text { Area }=\frac{1}{2} \times 6 \times 7=21\end{aligned}$

</details>

---

### Q57. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the square of the shortest distance between the lines $\frac{x-2}{1}=\frac{y-1}{2}=\frac{z+3}{-3}$ and $\frac{x+1}{2}=\frac{y+3}{4}=\frac{z+5}{-5}$ is $\frac{\mathrm{m}}{\mathrm{n}}$, where $\mathrm{m}, \mathrm{n}$ are coprime numbers, then $\mathrm{m}+\mathrm{n}$ is equal to :

**Options:**

- **(A)** 21
- **(B)** 9
- **(C)** 14
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 9**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{\mathrm{a}}=(2,1,-3) \\ & \overrightarrow{\mathrm{b}}=(-1,-3,-5) \\ & \overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{q}}=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 1 & 2 & -3 \\ 2 & 4 & -5\end{array}\right| \\ & =2 \hat{\mathrm{i}}-\hat{\mathrm{j}}\end{aligned}$
$\begin{aligned} & \overrightarrow{\mathrm{b}}-\overrightarrow{\mathrm{a}}=-3 \hat{\mathrm{i}}-4 \hat{\mathrm{j}}-2 \hat{\mathrm{k}} \\ & \mathrm{S}_{\mathrm{d}}=\frac{|(\overrightarrow{\mathrm{b}}-\overrightarrow{\mathrm{a}}) \cdot(\overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{q}})|}{|\overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{q}}|}- \\ & =\frac{2}{\sqrt{5}} \\ & \left(\mathrm{~S}_{\mathrm{d}}\right)^2=\frac{4}{5} \\ & \mathrm{~m}=4, \mathrm{n}=5 \Rightarrow \mathrm{~m}+\mathrm{n}=9\end{aligned}$

</details>

---

### Q58. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The distance of the line $\frac{x-2}{2}=\frac{y-6}{3}=\frac{z-3}{4}$ from the point $(1,4,0)$ along the line $\frac{x}{1}=\frac{y-2}{2}=\frac{z+3}{3}$ is :

**Options:**

- **(A)** $\sqrt{17}$
- **(B)** $\sqrt{15}$
- **(C)** $\sqrt{14}$
- **(D)** $\sqrt{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{14}$**

**Detailed Solution:**

Line passing through $(1,4,0)$ and parallel to $\frac{x}{1}=\frac{y-2}{2}=\frac{z+3}{3}$ is $L: \frac{x-1}{1}=\frac{y-4}{2}=\frac{z}{3}$
Any point on $L:(\lambda+1,2 \lambda+4,3 \lambda)$
Any point on $\frac{x-2}{2}=\frac{y-6}{3}=\frac{z-3}{4}$ is $(2 \mu+2,3 \mu+6,4 \mu+3)$
$\left.\begin{array}{l}
\lambda+1=2 \mu+2 \\
2 \lambda+4=3 \mu+6 \\
3 \lambda=4 \mu+3
\end{array}\right\} \lambda=1 \mu=0$
Point: $(2,6,3)$
$\begin{aligned}
& \text { Distance }=\sqrt{(2-1)^2+(6-4)^2+(3-0)^2} \\
& =\sqrt{1+4+9}=\sqrt{14}
\end{aligned}$

</details>

---

### Q59. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $P$ be the foot of the perpendicular from the point $Q(10,-3,-1)$ on the line $\frac{x-3}{7}=\frac{y-2}{-1}=\frac{z+1}{-2}$. Then the area of the right angled triangle $P Q R$, where $R$ is the point $(3,-2,1)$, is

**Options:**

- **(A)** $9 \sqrt{15}$
- **(B)** $\sqrt{30}$
- **(C)** $8 \sqrt{15}$
- **(D)** $3 \sqrt{30}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3 \sqrt{30}$**

**Detailed Solution:**

<img src="https://cdn.quizrr.in/question-assets/jee_main_pyq/N6AY-e_ilcleaUBp105pn4vdNn1IG20dx427cO8pHSk.original.fullsize.png">
$\begin{aligned}
& \frac{\mathrm{x}-3}{7}=\frac{\mathrm{y}-2}{-1}=\frac{\mathrm{z}+1}{-2}=\lambda \\
& \Rightarrow 7 \lambda+3,-\lambda+2,-2 \lambda-1 \\
& \text {dr's of QP } \Rightarrow 7 \lambda-7,-\lambda+5,-2 \lambda
\end{aligned}$
Now
$\begin{aligned}
& (7 \lambda-7) \cdot 7-(-\lambda+5)+(2 \lambda) \cdot 2=0 \\
& 54 \lambda-54=0 \Rightarrow \lambda=1 \\
& \therefore \mathrm{P}=(10,1,-3) \\
& \overrightarrow{\mathrm{PQ}}=-4 \hat{\mathrm{j}}+2 \hat{\mathrm{k}} \\
& \overrightarrow{\mathrm{PR}}=-7 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+4 \hat{\mathrm{k}} \\
& \text {Area } =\frac{1}{2}\left| \begin{array}{ccc}
\mathrm{i} & \mathrm{j} & \mathrm{k} \\
0 & -4 & 2 \\
-7 & -3 & 4
\end{array} \right|=3 \sqrt{30}
\end{aligned}$

</details>

---

### Q60. JEE Main 2025 (22 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the distance between two parallel lines be 5 units and a point $P$ lie between the lines at a unit distance from one of them. An equilateral triangle $P Q R$ is formed such that $Q$ lies on one of the parallel lines, while $R$ lies on the other. Then $(Q R)^2$ is equal to _______ -.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **28**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/QJQMvG1aD6ROk5-CofF9WFOO1f1uwIzSixEPH_iDDQM.original.fullsize.png">




$P R=\operatorname{cosec} \theta, P Q=4 \sec (30+\theta)$

For equilateral
$\begin{aligned}
& \mathrm{d}=\mathrm{PR}=\mathrm{PQ} \\
& \Rightarrow \cos \left(\theta+30^{\circ}\right)=4 \sin \theta \\
& \Rightarrow \frac{\sqrt{3}}{2} \cos \theta-\frac{1}{2} \sin \theta=4 \sin \theta \\
& \Rightarrow \tan \theta=\frac{1}{3 \sqrt{3}} \\
& \mathrm{QR}^2=\mathrm{d}^2=\operatorname{cosec}^2 \theta=28
\end{aligned}$

</details>

---

### Q61. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The perpendicular distance, of the line $\frac{x-1}{2}=\frac{y+2}{-1}=\frac{z+3}{2}$ from the point $\mathrm{P}(2,-10,1)$, is :

**Options:**

- **(A)** 6
- **(B)** $5 \sqrt{2}$
- **(C)** $4 \sqrt{3}$
- **(D)** $3 \sqrt{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3 \sqrt{5}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/CYRrWAIzJQ0eqdr_Q5Cks64tJO7nBi8021kTOezNHYw.original.fullsize.png">




$\begin{aligned} & \left.\frac{\mathrm{x}-1}{2}=\frac{\mathrm{y}+2}{-1}=\frac{\mathrm{z}+3}{2}=\lambda \text { (let }\right) \\ & (2 \lambda+1,-\lambda-2,2 \lambda-3) \\ & \because \overrightarrow{\mathrm{PA}} \cdot \overrightarrow{\mathrm{n}}=0 \\ & \Rightarrow(2 \lambda-1) 2+(-\lambda+8)(-1)+(2 \lambda-4) 2=0 \\ & \Rightarrow 4 \lambda-2+\lambda-8+4 \lambda-8=0 \\ & \Rightarrow 9 \lambda-18=0 \Rightarrow \lambda=2 \\ & \therefore \mathrm{~A}(5,-4,1) \\ & \therefore \mathrm{AP}=\sqrt{3^2+6^2+0^2}=\sqrt{45}=3 \sqrt{5}\end{aligned}$

</details>

---

### Q62. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let a line pass through two distinct points $P(-2,-1,3)$ and $Q$, and be parallel to the vector $3 \hat{i}+2 \hat{j}+2 \hat{k}$. If the distance of the point Q from the point $\mathrm{R}(1,3,3)$ is 5 , then the square of the area of $\triangle P Q R$ is equal to :

**Options:**

- **(A)** 148
- **(B)** 136
- **(C)** 144
- **(D)** 140

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 136**

**Detailed Solution:**

Equation of line $P Q$ is:
$\frac{x+2}{3}=\frac{y+1}{2}=\frac{z-3}{2}=r(\text { say })$
Let coordinate of $Q=(3 r-2,2 r-1,2 r+3)$
$\because P R=5$
Then
$\begin{aligned}
& (3 r-2-1)^2+(2 r-1-3)^2+(2 r+3-3)^2=25 \\
& \therefore r=0 \text { or } 2 \\
& \therefore \quad \text { Coordinate of } Q=(4,3,7)
\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/rqb504h80KVh-fyd1na6UkkMrhLtPjb3xZsxOBonzSc.original.fullsize.png">

$\begin{aligned} \therefore & \text { square of area of } \triangle P Q R=\left|\frac{1}{2}(\overrightarrow{P Q} \times \overrightarrow{P R})\right|^2 \\ & =\left|\frac{1}{2}(6 \hat{i}+4 \hat{j}+4 \hat{k}) \times(3 \hat{i}+4 \hat{j})\right|^2 \\ & =|-8 \hat{i}+6 \hat{j}+6 \hat{k}|^2=136\end{aligned}$

</details>

---

### Q63. JEE Main 2025 (22 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $\mathrm{L}_1: \frac{x-1}{3}=\frac{y-1}{-1}=\frac{z+1}{0}$ and $\mathrm{L}_2: \frac{x-2}{2}=\frac{y}{0}=\frac{z+4}{\alpha}, \alpha \in \mathbf{R}$, be two lines, which intersect at the point $B$. If $P$ is the foot of perpendicular from the point $A(1,1,-1)$ on $L_2$, then the value of $26 \alpha(\mathrm{~PB})^2$ is _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **216**

**Detailed Solution:**

Point $B$
$\begin{aligned}
& (3 \lambda+1,-\lambda+1,-1) \equiv(2 \mu+2,0, \alpha \mu-4) \\
& 3 \lambda+1=2 \mu+2 \\
& -\lambda+1=0 \\
& -1=\alpha \mu-4 \\
& \lambda=1, \mu=1, \alpha=3 \\
& B(4,0,-1)
\end{aligned}$
$\text { Let Point ' } P \text { ' is }(2 \delta+2,0,3 \delta-4)$
$\text { Dr's of AP } < 2 \delta+1,-1,3 \delta-3>$
$A P \perp L_2 \Rightarrow \delta=\frac{7}{13}$
$P\left(\frac{40}{13}, 0, \frac{-31}{13}\right)$
$\therefore 26 \alpha(P B)^2=26 \times 3 \times\left(\frac{144}{169}+\frac{324}{169}\right)$
$=216$

</details>

---

### Q64. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{L}_1: \frac{x-1}{2}=\frac{y-2}{3}=\frac{z-3}{4}$ and $\mathrm{L}_2: \frac{x-2}{3}=\frac{y-4}{4}=\frac{z-5}{5}$ be two lines. Then which of the following points lies on the line of the shortest distance between $L_1$ and $L_2$ ?

**Options:**

- **(A)** $\left(\frac{14}{3},-3, \frac{22}{3}\right)$
- **(B)** $\left(-\frac{5}{3},-7,1\right)$
- **(C)** $\left(2,3, \frac{1}{3}\right)$
- **(D)** $\left(\frac{8}{3},-1, \frac{1}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(\frac{14}{3},-3, \frac{22}{3}\right)$**

**Detailed Solution:**

$\begin{aligned} & L_1: \frac{x-1}{2}=\frac{y-2}{3}=\frac{z-3}{4} \\ & L_2: \frac{x-2}{3}=\frac{y-4}{4}=\frac{z-5}{5}\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/mVgHYwd6wB3HIvZT1RzsF9SQox6wtSh80h3P80782Ho.original.fullsize.png">

$\begin{aligned}
& P(2 \lambda+1,3 \lambda+2,4 \lambda+3) \\
& Q(3 \mu+2,4 \mu+4,5 \mu+5)
\end{aligned}$

Dr's of $P Q < 2 \lambda-3 \mu-1,3 \lambda-4 \mu-2$,
$\begin{aligned}
& 4 \lambda-5 \mu-2> \\
& P Q=\left|\begin{array}{lll}
\hat{i} & \hat{j} & \hat{k} \\
2 & 3 & 4 \\
3 & 4 & 5
\end{array}\right|=-\hat{i}+2 \hat{j}-\hat{k} \\
& \Rightarrow \frac{2 \lambda-3 \mu-1}{-1}=\frac{3 \lambda-4 \mu-2}{2}=\frac{4 \lambda-5 \mu-2}{-1} \\
& \Rightarrow \lambda=\frac{1}{3} \mu=\frac{-1}{6} \\
& \Rightarrow P\left(\frac{5}{3}, 3, \frac{13}{3}\right) \quad Q\left(\frac{3}{2}, \frac{10}{3}, \frac{25}{6}\right)
\end{aligned}$
Dr's $P Q\langle 1,-2,1\rangle$
$\therefore \quad \text { Line }$
$\frac{y-\frac{5}{3}}{1}=\frac{y-3}{-2}=\frac{y-\frac{13}{3}}{1}$

</details>

---

### Q65. JEE Main 2024 (09 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

The square of the distance of the image of the point $(6,1,5)$ in the line $\frac{x-1}{3}=\frac{y}{2}=\frac{z-2}{4}$, from the origin is _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **62**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/F8Io616TuO1IT3ZjmDAf1GUnJCGEx3mVzZHax8sG0RY.original.fullsize.png">
Let $\mathrm{M}(3 \lambda+1,2 \lambda, 4 \lambda+2)$
$\overrightarrow{\mathrm{AM}} \cdot \overrightarrow{\mathrm{b}}=0$
$\Rightarrow \quad 9 \lambda-15+4 \lambda-2+16 \lambda-12=0$
$\Rightarrow \quad 29 \lambda=29$
$\Rightarrow \quad \lambda=1$
$\mathrm{M}(4,2,6), \mathrm{I}=(2,3,7)$
Required Distance $=\sqrt{4+9+49}=\sqrt{62}$
Ans. 62

</details>

---

### Q66. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Consider the line $L$ passing through the points $(1,2,3)$ and $(2,3,5)$. The distance of the point $\left(\frac{11}{3}, \frac{11}{3}, \frac{19}{3}\right)$ from the line $\mathrm{L}$ along the line $\frac{3 x-11}{2}=\frac{3 y-11}{1}=\frac{3 z-19}{2}$ is equal to

**Options:**

- **(A)** 6
- **(B)** 5
- **(C)** 4
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

$\begin{aligned} & \frac{x-1}{2-1}=\frac{y-2}{3-2}=\frac{z-3}{5-3} \\ & \Rightarrow \frac{x-1}{1}=\frac{y-2}{1}=\frac{z-3}{2}=\lambda\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/SkiV1V73g-LsFz-bLRwo2_cgTKM37ZoEJF-FE-oGDHE.original.fullsize.png">
$\begin{aligned} & \mathrm{B}(1+\lambda, 2+\lambda, 3+2 \lambda) \\ & \text { D.R. of } \mathrm{AB}= < \frac{3 \lambda-8}{3}, \frac{3 \lambda-5}{3}, \frac{6 \lambda-10}{3}> \\ & \mathrm{B}\left(\frac{5}{3}, \frac{8}{3}, \frac{13}{3}\right) \frac{3 \lambda-8}{3 \lambda-5}=\frac{2}{1} \Rightarrow 3 \lambda-8=6 \lambda-10 \\ & 3 \lambda=2 \\ & \lambda=\frac{2}{3} \\ & \mathrm{AB}=\frac{\sqrt{36+9+36}}{3}=\frac{9}{3}=3\end{aligned}$

</details>

---

### Q67. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The shortest distance between the lines $\frac{x-3}{4}=\frac{y+7}{-11}=\frac{z-1}{5}$ and $\frac{x-5}{3}=\frac{y-9}{-6}=\frac{z+2}{1}$ is:

**Options:**

- **(A)** $\frac{178}{\sqrt{563}}$
- **(B)** $\frac{187}{\sqrt{563}}$
- **(C)** $\frac{185}{\sqrt{563}}$
- **(D)** $\frac{179}{\sqrt{563}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{187}{\sqrt{563}}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/KabFt9tuw2NPTNLqS6LffFn0gdfzk8K6WAJa0BoUhb8.original.fullsize.png">
$\begin{aligned} & \overrightarrow{\mathrm{n}}=\overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{q}} \\ & \overrightarrow{\mathrm{n}}=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 4 & -11 & 5 \\ 3 & -6 & 1\end{array}\right|=19 \hat{\mathrm{i}}+11 \hat{\mathrm{j}}+9 \hat{\mathrm{k}} \\ & \text { S.d. }=\text { projection of } \overrightarrow{\mathrm{AB}} \text { on } \overrightarrow{\mathrm{n}} \\ & =\left|\frac{\overrightarrow{\mathrm{AB}} \cdot \overrightarrow{\mathrm{n}}}{|\overrightarrow{\mathrm{n}}|}\right|=\left|\frac{(2 \hat{\mathrm{i}}+16 \hat{\mathrm{j}}-3 \hat{\mathrm{k}}) \cdot(19 \hat{\mathrm{i}}+11 \hat{\mathrm{j}}+9 \hat{\mathrm{k}})}{\sqrt{361+121+81}}\right| \\ & =\frac{38+176-27}{\sqrt{563}} \\ & \text { S.d. }=\frac{187}{\sqrt{563}}\end{aligned}$

</details>

---

### Q68. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the line $\mathrm{L}$ intersect the lines $x-2=-y=z-1,2(x+1)=2(y-1)=z+1$ and be parallel to the line $\frac{x-2}{3}=\frac{y-1}{1}=\frac{z-2}{2}$. Then which of the following points lies on L?

**Options:**

- **(A)** $\left(-\frac{1}{3}, 1,-1\right)$
- **(B)** $\left(-\frac{1}{3},-1,1\right)$
- **(C)** $\left(-\frac{1}{3}, 1,1\right)$
- **(D)** $\left(-\frac{1}{3},-1,-1\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(-\frac{1}{3}, 1,-1\right)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0rlfeOPXqxguMQPlEVBjKaHPA6pL8Ow4Tww8NK61xnQ.original.fullsize.png">
$\mathrm{L}_1: \frac{\mathrm{x}-2}{1}=\frac{\mathrm{y}}{-1}=\frac{\mathrm{z}-1}{1}=\lambda$
$\mathrm{L}_2: \frac{\mathrm{x}+1}{\frac{1}{2}}=\frac{\mathrm{y}-1}{\frac{1}{2}}=\frac{\mathrm{z}+1}{1}=\mu$
dr of line MN will be
$ < 3+\lambda-\frac{\mu}{2},-1-\lambda-\frac{\mu}{2}, 2+\lambda-\mu>\&$ it will be proportional to $ < 3,1,2>$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/G_qDLKpr4_fG5FsM76b2ygdnGfdax8jk25Mka06LfAc.original.fullsize.png">
$\Rightarrow \lambda=-\frac{4}{3} \& \mu=-\frac{2}{3}$
$\therefore$ Coordinate of $\mathrm{M}$ will be $ < \left(\frac{2}{3}, \frac{4}{3},-\frac{1}{3}\right)$ and equation of required line will be.
$\frac{\mathrm{x}-\frac{2}{3}}{3}=\frac{\mathrm{y}-\frac{4}{3}}{1}=\frac{\mathrm{z}+\frac{1}{3}}{2}=\mathrm{k}$
So any point on this line will be
$\begin{aligned}
& \left(\frac{2}{3}+3 \mathrm{k}, \frac{4}{3}+\mathrm{k},-\frac{1}{3}+2 \mathrm{k}\right) \\
& \because \frac{2}{3}+3 \mathrm{k}=-\frac{1}{3} \Rightarrow \mathrm{k}=-\frac{1}{3}
\end{aligned}$
$\therefore$ Point lie on the line for
$\mathrm{k}=-\frac{1}{3} \text { is }\left(-\frac{1}{3}, 1,-1\right)$

</details>

---

### Q69. JEE Main 2024 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

Let $\mathrm{P}(\alpha, \beta, \gamma)$ be the image of the point $\mathrm{Q}(1,6,4)$ in the line $\frac{x}{1}=\frac{y-1}{2}=\frac{z-2}{3}$. Then $2 \alpha+\beta+\gamma$ is equal to_______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/797ENzyRUi_JOQzarMl7qmClcCureZO-KwBckSAarA8.original.fullsize.png">
$\begin{aligned} & \mathrm{A}(\mathrm{t}, 2 \mathrm{t}+1,3 \mathrm{t}+2) \\ & \overrightarrow{\mathrm{QA}}=(\mathrm{t}-1) \hat{\mathrm{i}}+(2 \mathrm{t}-5) \hat{\mathrm{j}}+(3 \mathrm{t}-2) \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{QA}} \cdot \overrightarrow{\mathrm{b}}=0 \\ & (\mathrm{t}-1)+2(2 \mathrm{t}-5)+3(3 \mathrm{t}-2)=0 \\ & 14 \mathrm{t}=17 \\ & \alpha=\frac{20}{14} \quad \beta=\frac{12}{14} \quad \gamma=\frac{102}{14} \\ & 2 \alpha+\beta+\gamma=\frac{154}{14}=11\end{aligned}$

</details>

---

### Q70. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the shortest distance between the lines $\frac{x-\lambda}{2}=\frac{y-4}{3}=\frac{z-3}{4}$ and $\frac{x-2}{4}=\frac{y-4}{6}=\frac{z-7}{8}$ is $\frac{13}{\sqrt{29}}$, then a value of $\lambda$ is :

**Options:**

- **(A)** -1
- **(B)** $-\frac{13}{25}$
- **(C)** $\frac{13}{25}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

$\left.\begin{array}{l}\overline{\mathrm{r}}_1=(\lambda \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+3 \hat{\mathrm{k}})+\alpha(2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+4 \hat{\mathrm{k}}) \\ \overline{\mathrm{r}}_2=(2 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+7 \hat{\mathrm{k}})+\beta(2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+4 \hat{\mathrm{k}})\end{array}\right\} \begin{gathered}\overline{\mathrm{b}}=2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+4 \hat{\mathrm{k}} \\ \overline{\mathrm{a}}_2+\lambda \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+3 \hat{\mathrm{k}} \\ \mathrm{a}_2=2 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+7 \hat{\mathrm{k}}\end{gathered}$
Shortest dist. $=\frac{\left|\overline{\mathrm{b}} \times\left(\overline{\mathrm{a}}_2-\overline{\mathrm{a}}_1\right)\right|}{|\mathrm{b}|}=\frac{13}{\sqrt{29}}$
$\begin{aligned} & \left\lvert\, \frac{|(2 \hat{i}+3 \hat{j}+4 \hat{k}) \times((2-\lambda) \hat{i}+4 \hat{k})|}{\sqrt{29}}=\frac{13}{\sqrt{29}}\right. \\ & |-8 \hat{\mathrm{j}}-3(2-\lambda) \hat{k}+12 \hat{i}+4(2-\lambda) \hat{j}|=13 \\ & |12 \hat{i}-4 \lambda \hat{j}+(3 \lambda-6) \hat{k}|=13\end{aligned}$
$\begin{aligned} & 144+16 \lambda^2+(3 \lambda-6)^2=169 \\ & 16 \lambda^2+(3 \lambda-6)^2=25=\lambda \Rightarrow=1\end{aligned}$

</details>

---

### Q71. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the shortest distance between the lines
$\begin{array}{ll}
L_1: \vec{r}=(2+\lambda) \hat{i}+(1-3 \lambda) \hat{j}+(3+4 \lambda) \hat{k}, & \lambda \in \mathbb{R} \\
L_2: \vec{r}=2(1+\mu) \hat{i}+3(1+\mu) \hat{j}+(5+\mu) \hat{k}, \quad \mu \in \mathbb{R}
\end{array}$
is $\frac{m}{\sqrt{n}}$, where $\operatorname{gcd}(m, n)=1$, then the value of $m+n$ equals

**Options:**

- **(A)** 390
- **(B)** 384
- **(C)** 377
- **(D)** 387

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 387**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/SEiZ2FHN5nBOGuvE1e4Ad7JTLIqVOliJ2X9O6edGkn0.original.fullsize.png">
Shortes distance (CD) $=\left|\frac{\overline{\mathrm{AB}} \cdot \overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{q}}}{|\overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{q}}|}\right|$
$\begin{aligned} & =\left|\frac{(0 \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}) \cdot(-15 \hat{\mathrm{i}}+7 \hat{\mathrm{j}}+9 \hat{\mathrm{k}})}{\sqrt{355}}\right| \\ & =\frac{0+14+18}{\sqrt{355}}=\frac{32}{\sqrt{355}} \\ & \therefore \mathrm{m}+\mathrm{n}=32+355=387\end{aligned}$

</details>

---

### Q72. JEE Main 2024 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

If the shortest distance between the lines $\frac{x-\lambda}{3}=\frac{y-2}{-1}=\frac{z-1}{1}$ and $\frac{x+2}{-3}=\frac{y+5}{2}=\frac{z-4}{4}$ is $\frac{44}{\sqrt{30}}$, then the largest possible value of $|\lambda|$ is equal to _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **43**

**Detailed Solution:**

$\begin{aligned} & \overline{\mathrm{a}}_1=\lambda \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}} \\ & \overline{\mathrm{a}}_2=-2 \hat{\mathrm{i}}-5 \hat{\mathrm{j}}+4 \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{p}}-=3 \hat{\mathrm{i}}-\hat{\mathrm{j}}+\hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{q}}-=-3 \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+4 \hat{\mathrm{k}} \\ & (\lambda+2) \hat{\mathrm{i}}+7 \hat{\mathrm{j}}-3 \hat{\mathrm{k}}=\overline{\mathrm{a}}_1-\overline{\mathrm{a}}_2 \\ & \overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{q}}-=-6 \hat{\mathrm{i}}-15 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}\end{aligned}$
$\begin{aligned}
& \frac{44}{\sqrt{30}}=\frac{|-6 \lambda-12-105-9|}{\sqrt{(-6)^2+(-15)^2+3^2}} \\
& \frac{44}{\sqrt{30}}=\frac{|6 \lambda+126|}{3 \sqrt{30}} \\
& 132=|6 \lambda+126| \\
& \lambda=1, \lambda=-43 \\
& |\lambda|=43
\end{aligned}$

</details>

---

### Q73. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{P}(\alpha, \beta, \gamma)$ be the image of the point $\mathrm{Q}(3,-3,1)$ in the line $\frac{x-0}{1}=\frac{y-3}{1}=\frac{z-1}{-1}$ and $\mathrm{R}$ be the point $(2,5,-1)$. If the area of the triangle $P Q R$ is $\lambda$ and $\lambda^2=14 K$, then $K$ is equal to :

**Options:**

- **(A)** 36
- **(B)** 81
- **(C)** 72
- **(D)** 18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 81**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/XRAL-vVxUnITJjy0NeEtE86nXQhzLuwWajSTQwhrKtQ.original.fullsize.png">
$\begin{aligned} & \mathrm{RQ}=\sqrt{1+64+4}=\sqrt{69} \\ & \overrightarrow{\mathrm{RQ}}=\hat{\ell}-8 \hat{\mathrm{j}}+2 \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{RS}}=\hat{\ell}+\hat{\mathrm{j}}-\hat{\mathrm{k}} \\ & \cos \theta=\frac{\overrightarrow{\mathrm{RQ}} \cdot \overrightarrow{\mathrm{RS}}}{|\overrightarrow{\mathrm{RQ}}||\overrightarrow{\mathrm{RS}}|}=\left|\frac{1-8-2}{\sqrt{69} \sqrt{3}}\right|=\frac{9}{3 \sqrt{23}} \\ & \cos \theta=\frac{3}{\sqrt{23}}=\frac{\mathrm{RS}}{\mathrm{RQ}}=\frac{\mathrm{RS}}{\sqrt{69}} \\ & \mathrm{RS}=3 \sqrt{3} \\ & \sin \theta=\frac{\sqrt{14}}{\sqrt{23}}=\frac{\mathrm{QS}}{\sqrt{69}}\end{aligned}$
$\begin{aligned} & \mathrm{QS}=\sqrt{42} \\ & \text { area }=\frac{1}{2} \cdot 2 \mathrm{QS} \cdot \mathrm{RS}=\sqrt{42} \cdot 3 \sqrt{3} \\ & \lambda=9 \sqrt{14} \\ & \lambda^2=81.14=14 \mathrm{k} \\ & \mathrm{k}=81\end{aligned}$

</details>

---

### Q74. JEE Main 2024 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $P$ be the point $(10,-2,-1)$ and $Q$ be the foot of the perpendicular drawn from the point $R(1,7,6)$ on the line passing through the points $(2,-5,11)$ and $(-6,7,-5)$. Then the length of the line segment $P Q$ is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **13**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/csS08pWurazn2jKyxiXPwwHabxHlTd2qIP_6b0Nevvk.original.fullsize.png">
Line : $\frac{x+6}{-8}=\frac{y-7}{12}=\frac{z+5}{-16}$
$\begin{aligned}
& \frac{\mathrm{x}+6}{2}=\frac{\mathrm{y}-7}{-3}=\frac{\mathrm{z}+5}{4}=\lambda \\
& \mathrm{Q}(2 \lambda-6,7-3 \lambda, 4 \lambda-5) \\
& \overline{\mathrm{QR}}(2 \lambda-7,-3 \lambda, 4 \lambda-11) \\
& \overline{\mathrm{QR}} \cdot \text { dr's of line }=0 \\
& 4 \lambda-14+9 \lambda+16 \lambda-44=0 \\
& 29 \lambda=58 \Rightarrow \lambda=2 \\
& \mathrm{Q}(-2,1,3) \\
& \mathrm{PQ}=\sqrt{144+9+16}=\sqrt{169}=13
\end{aligned}$

</details>

---

### Q75. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The shortest distance between the lines $\frac{x-3}{2}=\frac{y+15}{-7}=\frac{z-9}{5}$ and $\frac{x+1}{2}=\frac{y-1}{1}=\frac{z-9}{-3}$ is

**Options:**

- **(A)** $8 \sqrt{3}$
- **(B)** $4 \sqrt{3}$
- **(C)** $5 \sqrt{3}$
- **(D)** $6 \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4 \sqrt{3}$**

**Detailed Solution:**

$\begin{aligned} & \frac{x-3}{2}=\frac{y+15}{-7}=\frac{z-9}{5} \& \frac{x+1}{2}=\frac{y-1}{1}=\frac{z-9}{-3} \\ & \text { S.D }=\frac{\left|\left(\overline{\mathrm{a}}_2 \cdot \overline{\mathrm{a}}_1\right) \cdot\left(\overline{\mathrm{b}}_1 \cdot \overline{\mathrm{b}}_2\right)\right|}{\left|\overline{\mathrm{b}}_1 \times \overline{\mathrm{b}}_2\right|} \\ & a_1=3,-15,9 \\ & \mathrm{~b}_1=2,-7,5 \\ & \mathrm{a}_2=-1,1,9 \\ & \mathrm{~b}_2=2,1,-3 \\ & a_2-a_1=-4,16,0 \\ & \overline{\mathrm{b}}_1 \times \overline{\mathrm{b}}_2=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 2 & -7 & 5 \\ 2 & 1 & -3\end{array}\right|=\hat{\mathrm{i}}(16)-\hat{\mathrm{j}}(-16)+\hat{\mathrm{k}}(16) \\ & 16(\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}) \\ & \left|\overline{\mathrm{b}}_1 \times \overline{\mathrm{b}}_2\right|=16 \sqrt{3} \\ & \therefore\left(\overline{\mathrm{a}}_2-\overline{\mathrm{a}}_1\right) \cdot\left(\overline{\mathrm{b}}_1-\overline{\mathrm{b}}_2\right)=16[-4+16]=(16)(12) \\ & \text { S.D. }=\frac{(16)(12)}{16 \sqrt{3}}=4 \sqrt{3} \\ & \end{aligned}$

</details>

---

### Q76. JEE Main 2024 (05 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the point $(-1, \alpha, \beta)$ lie on the line of the shortest distance between the lines $\frac{x+2}{-3}=\frac{y-2}{4}=\frac{z-5}{2}$ and $\frac{x+2}{-1}=\frac{y+6}{2}=\frac{z-1}{0}$. Then $(\alpha-\beta)^2$ is equal to___________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/11PT6YQUyi-liU4vS2EEUaSdfY6IMneNlEsFgn4dKB8.original.fullsize.png">
$\begin{aligned}
& \mathrm{P}(-3 \lambda-2,4 \lambda+2,2 \lambda+5) \\
& \mathrm{Q}(-\mu-2,2 \mu-6,1) \\
& \mathrm{DRS} \text { of } \mathrm{PQ}=(3 \lambda-\mu, 2 \mu-4 \lambda-8,-2 \lambda-4) \\
& \mathrm{DRS} \text { of } \mathrm{PQ}=\left|\begin{array}{ccc}
\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\
-1 & 2 & 0 \\
-3 & 4 & 2
\end{array}\right| \\
& =(4 \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+2 \hat{\mathrm{k}})
\end{aligned}$
OR
$\begin{aligned}
& (2,1,1) \\
& \frac{3 \lambda-\mu}{2}=\frac{2 \mu-4 \lambda-8}{1}=\frac{-2 \lambda-4}{1} \\
& \Rightarrow \mu=\lambda+2 \& 7 \lambda=\mu-8 \\
& \lambda=-1 \quad \mu=1 \\
& Q:(-3,-4,1) \\
& L_{P Q}=\frac{x+3}{2}=\frac{y+4}{1}=\frac{z-1}{1} \\
& (-1, \alpha, \beta) \Rightarrow 1=\frac{\alpha+4}{1}=\frac{\beta-1}{1} \\
& \Rightarrow \alpha=-3, \beta=2 \\
& (\alpha-\beta)^2=25
\end{aligned}$

</details>

---

### Q77. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $(\alpha, \beta, \gamma)$ be the image of the point $(8,5,7)$ in the line $\frac{x-1}{2}=\frac{y+1}{3}=\frac{z-2}{5}$. Then $\alpha+\beta+\gamma$ is equal to :

**Options:**

- **(A)** 16
- **(B)** 20
- **(C)** 14
- **(D)** 18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 14**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/nS_VQPtPBxTOXI3nCdNQDX62Hqoq6420WFLBvvIyC6g.original.fullsize.png">
$\begin{aligned} & \overrightarrow{\mathrm{AM}} \cdot(2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+5 \hat{\mathrm{k}})=0 \\ & (2 \lambda-7)(2)+(3 \lambda-6)(3)+(5 \lambda-5)(5)=0 \\ & 38 \lambda=57 \\ & \lambda=\frac{3}{2} \\ & \mathrm{M}\left(4, \frac{7}{2}, \frac{19}{2}\right) \\ & \mathrm{A}^{\prime}(0,2,12)\end{aligned}$

</details>

---

### Q78. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{d}$ be the distance of the point of intersection of the lines $\frac{x+6}{3}=\frac{y}{2}=\frac{z+1}{1}$ and $\frac{x-7}{4}=\frac{y-9}{3}=\frac{z-4}{2}$ from the point $(7,8,9)$. Then $\mathrm{d}^2+6$ is equal to :

**Options:**

- **(A)** 69
- **(B)** 78
- **(C)** 72
- **(D)** 75

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 75**

**Detailed Solution:**

$\begin{aligned} & \frac{x+6}{3}=\frac{y}{2}=\frac{z+1}{1}=\lambda....(1)\\ & x=3 \lambda-6, y=2 \lambda, z=\lambda-1 \\ & \frac{x-7}{4}=\frac{y-9}{3}=\frac{z-4}{2}=\mu....(2)\end{aligned}$
$\mathrm{x}=4 \mu+7, \mathrm{y}=3 \mu+9, \mathrm{z}=2 \mu+4$
$3 \lambda-6=4 \mu+7 \Rightarrow 3 \lambda-4 \mu=13$ $\ldots(3) \times 2$
$2 \lambda=3 \mu+9 \Rightarrow 2 \lambda-3 \mu=9$ $\ldots(4) \times 3$
$\begin{array}{c}
6 \lambda-8 \mu=26 \\
6 \lambda-9 \mu=27 \\
-\quad+\quad- \\
\hline\mu=-1
\end{array}$
$\begin{gathered}
\Rightarrow 3 \lambda-4(-1)=13 \\
3 \lambda=9 \\
\lambda=3
\end{gathered}$
int. point $(3,6,2) ;(7,8,9)$
$\mathrm{d}^2=16+4+49=69$
Ans. $\mathrm{d}^2+6=69+6=75$

</details>

---

### Q79. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the line $\frac{2-x}{3}=\frac{3 y-2}{4 \lambda+1}=4-z$ makes a right angle with the line $\frac{x+3}{3 \mu}=\frac{1-2 y}{6}=\frac{5-z}{7}$, then $4 \lambda+9 \mu$ is equal to :

**Options:**

- **(A)** 4
- **(B)** 13
- **(C)** 5
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 6**

**Detailed Solution:**

$\frac{2-x}{3}=\frac{3 y-2}{4 \lambda+1}=4-z...(1)$
$\frac{x-2}{(-3)}=\frac{y-\frac{2}{3}}{\left(\frac{4 \lambda+1}{3}\right)}=\frac{z-4}{(-1)}$
$\begin{aligned} & \frac{x+3}{3 \mu}=\frac{1-2 y}{6}=\frac{5-z}{7}...(2) \\ & \frac{x+3}{3 \mu}=\frac{y-\frac{1}{2}}{(-3)}=\frac{z-5}{(-7)} \\ & \text { Right angle } \Rightarrow(-3)(3 \mu)+\left(\frac{4 \lambda+1}{3}\right)(-3)+(-1)(-7)=0 \\ & -9 \mu-4 \lambda-1+7=0 \\ & 4 \lambda+9 \mu=6\end{aligned}$

</details>

---

### Q80. JEE Main 2024 (04 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

Consider a line $\mathrm{L}$ passing through the points $\mathrm{P}(1,2,1)$ and $\mathrm{Q}(2,1,-1)$. If the mirror image of the point $\mathrm{A}(2,2,2)$ in the line $\mathrm{L}$ is $(\alpha, \beta, \gamma)$, then $\alpha+\beta+6 \gamma$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/FtP5mst7qEdhDW382ASYXoivC_8lq3zqjWl4oZbZT48.original.fullsize.png">
DR's of Line $L \equiv-1: 1: 2$
DR's of $\mathrm{AB} \equiv \alpha-2: \beta-2: \gamma-2$
$\begin{aligned}
& \mathrm{AB} \perp_{\mathrm{ar}} \mathrm{L} \Rightarrow 2-\alpha+\beta-2+2 \gamma-4=0 \\
& 2 \gamma+\beta-\alpha=4
\end{aligned}$
Let $C$ is mid-point of $A B$
$\begin{aligned}
& \mathrm{C}\left(\frac{\alpha+2}{2}, \frac{\beta+2}{2}, \frac{\gamma+2}{2}\right) \\
& \text { DR's of PC }=\frac{\alpha}{2}: \frac{\beta-2}{2}: \frac{\gamma}{2} \\
& \text { line L } \left\lvert\, \mathrm{PC} \Rightarrow \frac{-\alpha}{2}=\frac{\beta-2}{2}=\frac{\gamma}{4}=\mathrm{K}(\text { let) }\right.
\end{aligned}$
$\begin{aligned}
& \alpha=-2 \mathrm{~K} \\
& \beta=2 \mathrm{~K}+2 \\
& \gamma=4 \mathrm{~K}
\end{aligned}$
use in (1) $\Rightarrow K=\frac{1}{6}$
value of $\alpha+\beta+6 \gamma=24 \mathrm{~K}+2=6$

</details>

---

### Q81. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{P}$ be the point of intersection of the lines $\frac{x-2}{1}=\frac{y-4}{5}=\frac{z-2}{1}$ and $\frac{x-3}{2}=\frac{y-2}{3}=\frac{z-3}{2}$. Then, the shortest distance of P from the line $4 x=2 y=z$ is

**Options:**

- **(A)** $\frac{5 \sqrt{14}}{7}$
- **(B)** $\frac{3 \sqrt{14}}{7}$
- **(C)** $\frac{ \sqrt{14}}{7}$
- **(D)** $\frac{6 \sqrt{14}}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3 \sqrt{14}}{7}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/MHMHkaL8ex-086NSQI72Px-oyKdysWNm7r38isFMjsM.original.fullsize.png">
$\begin{aligned}
& \mathrm{L}_1 \equiv \frac{\mathrm{x}-2}{1}=\frac{\mathrm{y}-4}{5}=\frac{\mathrm{z}-2}{1}=\lambda \\
& \mathrm{P}(\lambda+2,5 \lambda+4, \lambda+2) \\
& \mathrm{L}_2 \equiv \frac{\mathrm{x}-3}{2}=\frac{\mathrm{y}-2}{3}=\frac{\mathrm{z}-3}{2} \\
& \mathrm{P}(2 \mu+3,3 \mu+2,2 \mu+3) \\
& \lambda+2=2 \mu+3 \quad 3 \mu+2=5 \lambda+4 \\
& \lambda=2 \mu+1 \quad 3 \mu=5 \lambda+2 \\
& 3 \mu=5(2 \mu+1)+2 \\
& 3 \mu=10 \mu+7 \quad \\
& \mu=-1 \quad \lambda=-1
\end{aligned}$
Both satisfies (P)
$\begin{aligned}
& \mathrm{P}(1,-1,1) \\
& \mathrm{L}_3 \equiv \frac{\mathrm{x}}{1 / 4}=\frac{\mathrm{y}}{1 / 2}=\frac{\mathrm{z}}{1} \\
& \mathrm{~L}_3=\frac{\mathrm{x}}{\mathrm{l}}=\frac{\mathrm{y}}{2}=\frac{\mathrm{z}}{4}=\mathrm{k}
\end{aligned}$
Coordinates of $\mathrm{Q}(\mathrm{k}, 2 \mathrm{k}, 4 \mathrm{k})$
$\mathrm{DR}$ 's $\mathrm{PQ}=\langle\mathrm{k}-1,2 \mathrm{k}+1,4 \mathrm{k}-1>$
$\mathrm{PQ} \perp$ to $\mathrm{L}_3$
$\begin{aligned}
& (\mathrm{k}-1)+2(2 \mathrm{k}+1)+4(4 \mathrm{k}-1)=0 \\
& \mathrm{k}-1+4 \mathrm{k}+2+16 \mathrm{k}-4=0 \\
& \mathrm{k}=\frac{1}{7} \\
& \mathrm{Q}\left(\frac{1}{7}, \frac{2}{7}, \frac{4}{7}\right) \\
& \mathrm{PQ}=\sqrt{\left(1-\frac{1}{7}\right)^2+\left(-1-\frac{2}{7}\right)^2+\left(1-\frac{4}{7}\right)^2} \\
& =\sqrt{\frac{36}{49}+\frac{81}{49}+\frac{9}{49}}=\frac{\sqrt{126}}{7} \\
& P Q=\frac{3 \sqrt{14}}{7}
\end{aligned}$

</details>

---

### Q82. JEE Main 2024 (04 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

If the shortest distance between the lines $\frac{x+2}{2}=\frac{y+3}{3}=\frac{z-5}{4}$ and $\frac{x-3}{1}=\frac{y-2}{-3}=\frac{z+4}{2}$ is $\frac{38}{3 \sqrt{5}} \mathrm{k}$, and $\int_0^{\mathrm{k}}\left[x^2\right] \mathrm{d} x=\alpha-\sqrt{\alpha}$, where $[x]$ denotes the greatest integer function, then $6 \alpha^3$ is equal to________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **48**

**Detailed Solution:**

$\begin{aligned} & \frac{38}{3 \sqrt{5}} \hat{\mathrm{k}}=\frac{(5 \hat{\mathrm{i}}+5 \hat{\mathrm{j}}-9 \hat{\mathrm{k}})}{\sqrt{5}} \cdot\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 2 & 3 & 4 \\ 1 & -3 & 2\end{array}\right| \\ & \frac{38}{3 \sqrt{5}} \hat{\mathrm{k}}=\frac{19}{\sqrt{5}} \\ & \mathrm{k}=\frac{19}{\sqrt{5}} \\ & \mathrm{k}=\frac{3}{2} \\ & \int_0^{3 / 2}\left[\mathrm{x}^2\right]=\int_0^1 0+\int_1^{\sqrt{2}} 1+\int_{\sqrt{2}}^{3 / 2} 2 \\ & =\sqrt{2}-1+2\left(\frac{3}{2}-\sqrt{2}\right) \\ & =2-\sqrt{2} \\ & \alpha=2 \\ & \Rightarrow 6 \alpha^3=48\end{aligned}$

</details>

---

### Q83. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo> </mo><mtext>and</mtext><mo> </mo><mi>Q</mi></math> be the points on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>8</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>−</mo><mn>4</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math> which are at a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> units from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math>. If the centroid of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mi>R</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi></mrow></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup><mo>+</mo><msup><mi>γ</mi><mn>2</mn></msup></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>8</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>−</mo><mn>4</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mi>λ</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>8</mn><mi>λ</mi><mo>-</mo><mn>3</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>λ</mi><mo>+</mo><mn>4</mn><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mn>2</mn><mi>λ</mi><mo>-</mo><mn>1</mn></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>≡</mo><mfenced><mrow><mn>8</mn><mi>λ</mi><mo>-</mo><mn>3</mn><mo>,</mo><mo> </mo><mn>2</mn><mi>λ</mi><mo>+</mo><mn>4</mn><mo>,</mo><mo> </mo><mn>2</mn><mi>λ</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>.</p><p>Now, given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>R</mi><mo>=</mo><mn>6</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mi>Q</mi><mi>R</mi><mo>=</mo><mn>6</mn></math>.</p><p>So, by distance formula we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mn>8</mn><mi>λ</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mi>λ</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mi>λ</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>64</mn><msup><mi>λ</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><mo>-</mo><mn>64</mn><mi>λ</mi><mo>+</mo><mn>4</mn><msup><mi>λ</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>+</mo><mn>8</mn><mi>λ</mi><mo>+</mo><mn>4</mn><msup><mi>λ</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><mo>-</mo><mn>16</mn><mi>λ</mi><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>72</mn><msup><mi>λ</mi><mn>2</mn></msup><mo>-</mo><mn>72</mn><mi>λ</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>≡</mo><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mi>Q</mi><mo>≡</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Hence, centroid of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>△</mo><mi>P</mi><mi>Q</mi><mi>R</mi></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi></mrow></mfenced><mo>≡</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup><mo>+</mo><msup><mi>γ</mi><mn>2</mn></msup><mo>=</mo><mn>18</mn></math></p>

</details>

---

### Q84. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the mirror image of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>9</mn><mo>)</mo></math> in the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>−</mo><mn>2</mn></mrow><mn>1</mn></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi></mrow></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi></mrow></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>102</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>138</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>108</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>132</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>108</mn></math>**

**Detailed Solution:**

<p>The given point is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>9</mn><mo>)</mo></math>.</p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi></mrow></mfenced></math> be the image of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>9</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>'</mo><mi>O</mi><mo>'</mo></math> be the mid-point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> which is on the given line </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mi>y</mi><mo>+</mo><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mi>z</mi><mo>-</mo><mn>2</mn></mstyle><mstyle displaystyle="true"><mn>1</mn></mstyle></mfrac><mo>=</mo><mi>λ</mi></math> (say)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>3</mn><mi>λ</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>λ</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mi>λ</mi><mo>+</mo><mn>2</mn></math> </p><p>let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mi>λ</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn><mi>λ</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>λ</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math> be the co-ordinates of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math>.</p><p>Direction ratios of the line is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo> </mo><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><msub><mi>c</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn></math></p><p>Also, direction ratios of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>O</mi></math> are</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mi>λ</mi><mo>-</mo><mn>2</mn><mo>,</mo><mo> </mo><mn>2</mn><mi>λ</mi><mo>-</mo><mn>5</mn><mo>,</mo><mo> </mo><mi>λ</mi><mo>-</mo><mn>7</mn></mrow></mfenced></math></p><p>As, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>O</mi></math> is perpendicular to the line</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mn>3</mn><mi>λ</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>λ</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mi>λ</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>14</mn><mi>λ</mi><mo>-</mo><mn>23</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mfrac><mn>23</mn><mn>14</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> point is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>·</mo><mfrac><mn>23</mn><mn>14</mn></mfrac><mo>+</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>·</mo><mfrac><mn>23</mn><mn>14</mn></mfrac><mo>-</mo><mn>1</mn><mo>,</mo><mo> </mo><mfrac><mn>23</mn><mn>14</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> is mid-point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mfenced><mrow><mn>3</mn><mo>·</mo><mfrac><mn>23</mn><mn>14</mn></mfrac><mo>+</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>·</mo><mfrac><mn>23</mn><mn>14</mn></mfrac><mo>-</mo><mn>1</mn><mo>,</mo><mo> </mo><mfrac><mn>23</mn><mn>14</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mfrac><mrow><mn>3</mn><mo>+</mo><mi>α</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>4</mn><mo>+</mo><mi>β</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>9</mn><mo>+</mo><mi>γ</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p>So, on comparing both side and solving we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mfrac><mn>62</mn><mn>7</mn></mfrac><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mfrac><mn>4</mn><mn>7</mn></mfrac><mo>,</mo><mo> </mo><mi>γ</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>12</mn></mrow><mn>7</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mfenced><mrow><mi>α</mi><mo>+</mo><mo> </mo><mi>β</mi><mo>+</mo><mi>γ</mi></mrow></mfenced><mo>=</mo><mn>108</mn></math></p>

</details>

---

### Q85. JEE Main 2024 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Let the line of the shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mover><mi>r</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>λ</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mover><mi>r</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>μ</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> intersect <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi></mrow></mfenced></math> is the midpoint of the line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi></mrow></mfenced></math> is equal to___________</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **21**

**Detailed Solution:**

<p>Let point on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>λ</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mi>λ</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mi>λ</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> and point on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mfenced><mrow><mn>4</mn><mo>+</mo><mi>μ</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>5</mn><mo>+</mo><mi>μ</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>6</mn><mo>-</mo><mi>μ</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mi>λ</mi><mo>-</mo><mi>μ</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mo>-</mo><mi>λ</mi><mo>-</mo><mi>μ</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>λ</mi><mo>+</mo><mi>μ</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>→</mo></mover><mo> </mo><mo>⊥</mo><mo> </mo><msub><mi>L</mi><mn>1</mn></msub><mo>,</mo><mo> </mo><msub><mi>L</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>λ</mi><mo>-</mo><mi>μ</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>λ</mi><mo>+</mo><mi>μ</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>λ</mi><mo>+</mo><mi>μ</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mi>λ</mi><mo>+</mo><mi>μ</mi><mo>=</mo><mn>3</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>λ</mi><mo>-</mo><mi>μ</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mo>-</mo><mi>λ</mi><mo>-</mo><mi>μ</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mo>-</mo><mi>λ</mi><mo>-</mo><mi>μ</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mi>λ</mi><mo>-</mo><mn>3</mn><mi>μ</mi><mo>=</mo><mn>3</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now, solving above equations we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mi>λ</mi><mo>+</mo><mi>μ</mi><mo>-</mo><mn>3</mn><mi>λ</mi><mo>-</mo><mn>9</mn><mi>μ</mi><mo>=</mo><mn>3</mn><mo>+</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>8</mn><mi>μ</mi><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>μ</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>≡</mo><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo><mo> </mo><mi>Q</mi><mo>≡</mo><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>15</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>So, mid-point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>,</mo><mn>2</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mo>+</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi></mrow></mfenced><mo>=</mo><mn>21</mn></math></p>

</details>

---

### Q86. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>−</mo><mi>λ</mi></mrow><mrow><mo>−</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>−</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>−</mo><mn>1</mn></mrow><mn>1</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>−</mo><msqrt><mn>3</mn></msqrt></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>−</mo><mn>1</mn></mrow><mrow><mo>−</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>−</mo><mn>2</mn></mrow><mn>1</mn></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>, then the sum of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p>Given: Equations of line,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>λ</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mi>y</mi><mo>-</mo><mn>2</mn></mstyle><mstyle displaystyle="true"><mn>1</mn></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mi>z</mi><mo>-</mo><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>1</mn></mstyle></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mstyle displaystyle="true"><mi>x</mi><mo>-</mo><msqrt><mn>3</mn></msqrt></mstyle><mstyle displaystyle="true"><mn>1</mn></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mi>y</mi><mo>-</mo><mn>1</mn></mstyle><mstyle displaystyle="true"><mo>-</mo><mn>2</mn></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mi>z</mi><mo>-</mo><mn>2</mn></mstyle><mstyle displaystyle="true"><mn>1</mn></mstyle></mfrac></math></p><p>Now, we know that shortest distance between two lines is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>S.D</mtext><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><msub><mover><mi>a</mi><mo>→</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi>a</mi><mo>→</mo></mover><mn>1</mn></msub></mrow></mfenced><mo>·</mo><mover><msub><mi>b</mi><mn>1</mn></msub><mo>→</mo></mover><mo>×</mo><mover><msub><mi>b</mi><mn>2</mn></msub><mo>→</mo></mover></mrow><mfenced close="|" open="|"><mrow><mover><msub><mi>b</mi><mn>1</mn></msub><mo>→</mo></mover><mo>×</mo><mover><msub><mi>b</mi><mn>2</mn></msub><mo>→</mo></mover></mrow></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>=</mo><mfenced close="|" open="|"><mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mi>λ</mi><mo>-</mo><msqrt><mn>3</mn></msqrt></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><mi>λ</mi><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mn>3</mn><mo>+</mo><mn>3</mn><mo>-</mo><mn>3</mn></mrow><mfenced close="|" open="|"><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mfenced><mrow><mi>λ</mi><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math></p><p>Hence, the sum is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math></p>

</details>

---

### Q87. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

A line passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mo>−</mo><mn>6</mn><mo>,</mo><mo>−</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mn>16</mn><mo>,</mo><mo>−</mo><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>. The point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></math> are non-negative integers, on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> lies at a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math> units, from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. The distance between the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mo>−</mo><mn>12</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **22**

**Detailed Solution:**

<p>Given,</p><p>A line passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mo>−</mo><mn>6</mn><mo>,</mo><mo>−</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mn>16</mn><mo>,</mo><mo>−</mo><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>,</p><p>So, the equation of line will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>−</mo><mn>4</mn></mrow><mn>12</mn></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>6</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>2</mn></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>x</mi><mo>−</mo><mn>4</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>6</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac></math></p><p>So, the direction cosines will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><msqrt><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></msqrt></mfrac><mo>,</mo><mfrac><mstyle displaystyle="true"><mn>2</mn></mstyle><mstyle displaystyle="true"><msqrt><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></msqrt></mstyle></mfrac><mo>,</mo><mfrac><mstyle displaystyle="true"><mn>3</mn></mstyle><mstyle displaystyle="true"><msqrt><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></msqrt></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>≡</mo><mfrac><mn>6</mn><mn>7</mn></mfrac><mo>,</mo><mfrac><mstyle displaystyle="true"><mn>2</mn></mstyle><mstyle displaystyle="true"><mn>7</mn></mstyle></mfrac><mo>,</mo><mfrac><mstyle displaystyle="true"><mn>3</mn></mstyle><mstyle displaystyle="true"><mn>7</mn></mstyle></mfrac></math></p><p>Now, given point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></math> lies on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> and at a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math> from point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></p><p>So, by using the equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>a</mi><mo>−</mo><mn>4</mn></mrow><mstyle displaystyle="true"><mfrac><mn>6</mn><mn>7</mn></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mrow><mi>b</mi><mo>+</mo><mn>6</mn></mrow><mstyle displaystyle="true"><mfrac><mn>2</mn><mn>7</mn></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mrow><mi>c</mi><mo>+</mo><mn>2</mn></mrow><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>7</mn></mfrac></mstyle></mfrac><mo>=</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mn>21</mn><mo>×</mo><mfrac><mn>6</mn><mn>7</mn></mfrac><mo>+</mo><mn>4</mn><mo>,</mo><mfrac><mn>2</mn><mn>7</mn></mfrac><mo>×</mo><mn>21</mn><mo>−</mo><mn>6</mn><mo>,</mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mo>×</mo><mn>21</mn><mo>−</mo><mn>2</mn></mrow></mfenced><mo>≡</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mn>22</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>≡</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></math></p><p>Hence, the distance between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>22</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mi>Q</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mo>-</mo><mn>12</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>324</mn><mo>+</mo><mn>144</mn><mo>+</mo><mn>16</mn></msqrt><mo>=</mo><mn>22</mn></math></p>

</details>

---

### Q88. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The shortest distance between lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>−</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>4</mn></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> is the line passing through the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mo>−</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>B</mi><mfenced><mrow><mo>−</mo><mn>1</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> and perpendicular to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>−</mo><mn>3</mn></mrow><mrow><mo>−</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>−</mo><mn>1</mn></mrow><mn>1</mn></mfrac></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>121</mn><msqrt><mn>221</mn></msqrt></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>24</mn><msqrt><mn>117</mn></msqrt></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>141</mn><msqrt><mn>221</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>42</mn><msqrt><mn>117</mn></msqrt></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>141</mn><msqrt><mn>221</mn></msqrt></mfrac></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mi>B</mi><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>−</mo><mn>4</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>−</mo><mn>3</mn></mrow><mn>0</mn></mfrac></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>4</mn></mrow><mn>2</mn></mfrac></math></p><p>We know that, shortest distance between <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mo> </mo><mfrac><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow><msub><mi>a</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow><msub><mi>b</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub></mrow><msub><mi>c</mi><mn>1</mn></msub></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mo> </mo><mfrac><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow><msub><mi>a</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow><msub><mi>b</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><msub><mi>z</mi><mn>2</mn></msub></mrow><msub><mi>c</mi><mn>2</mn></msub></mfrac></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mtd><mtd><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mtd><mtd><msub><mi>z</mi><mn>2</mn></msub><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced><msqrt><msup><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><msub><mi>b</mi><mn>2</mn></msub><mo>-</mo><msub><mi>a</mi><mn>2</mn></msub><msub><mi>b</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msub><mi>b</mi><mn>1</mn></msub><msub><mi>c</mi><mn>2</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub><msub><mi>c</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msub><mi>c</mi><mn>1</mn></msub><msub><mi>a</mi><mn>2</mn></msub><mo>-</mo><msub><mi>c</mi><mn>2</mn></msub><msub><mi>a</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac></mfenced></math>.</p><p>So, shortest distance, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mfenced close="|" open="|"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mo>-</mo><mn>4</mn><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn><mo>+</mo><mn>4</mn></mtd><mtd><mn>4</mn><mo>+</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>−</mo><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><msqrt><msup><mfenced><mrow><mn>4</mn><mo>+</mo><mn>9</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>0</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>6</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mfenced close="|" open="|"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>7</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>−</mo><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><msqrt><mn>169</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>36</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>31</mn><mo>×</mo><mn>3</mn><mo>+</mo><mn>48</mn></mrow><msqrt><mn>221</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>D</mi><mo>=</mo><mfrac><mn>141</mn><msqrt><mn>221</mn></msqrt></mfrac></math></p>

</details>

---

### Q89. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi></mrow></mfenced></math> be mirror image of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> in the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>−</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>−</mo><mn>3</mn></mrow><mn>4</mn></mfrac></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>α</mi><mo>+</mo><mn>3</mn><mi>β</mi><mo>+</mo><mn>4</mn><mi>γ</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>≡</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>≡</mo><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi></mrow></mfenced></math>.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4cd3bb04-e91d-458a-a719-b6454581e206.png" style="width: 250px; height: 208px;"/></p><p>Now, direction ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>R</mi><mo>=</mo><mi>α</mi><mo>-</mo><mn>2</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>-</mo><mn>3</mn><mo>,</mo><mo> </mo><mi>γ</mi><mo>-</mo><mn>5</mn></math></p><p>And the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac></math> will be perpendicular,</p><p>So, using perpendicular condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>α</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>×</mo><mn>2</mn><mo>+</mo><mfenced><mrow><mi>β</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>×</mo><mn>3</mn><mo>+</mo><mfenced><mrow><mi>γ</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>×</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>α</mi><mo>-</mo><mn>4</mn><mo>+</mo><mn>3</mn><mi>β</mi><mo>-</mo><mn>9</mn><mo>+</mo><mn>4</mn><mi>γ</mi><mo>-</mo><mn>20</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi>α</mi><mo>+</mo><mn>3</mn><mi>β</mi><mo>+</mo><mn>4</mn><mi>γ</mi></mrow></mfenced><mo>=</mo><mn>33</mn></math></p>

</details>

---

### Q90. JEE Main 2024 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be the feet of perpendiculars from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mo> </mo><mi>a</mi><mo>,</mo><mo> </mo><mi>a</mi></mrow></mfenced></math> on the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>−</mo><mi>y</mi><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mo>−</mo><mn>1</mn></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∠</mo><mi>Q</mi><mi>P</mi><mi>R</mi></math> is a right angle, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><msup><mi>a</mi><mn>2</mn></msup></math> is equal to ________</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<p>Given,</p><p>Equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>−</mo><mn>1</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mi>r</mi></math></p><p>Now, let any point on the above line be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mi>r</mi><mo>,</mo><mo> </mo><mi>r</mi><mo>,</mo><mo> </mo><mn>1</mn></mrow></mfenced></math></p><p>Similarly, for line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>−</mo><mi>y</mi><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mo>−</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>−</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mi>k</mi></math></p><p>So, any point on the above line will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mrow><mi>k</mi><mo>,</mo><mo> </mo><mo>−</mo><mi>k</mi><mo>,</mo><mo> </mo><mo>−</mo><mn>1</mn></mrow></mfenced></math></p><p>Now, the direction ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mi>r</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mi>r</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mn>1</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now, finding foot of perpendicular from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> on line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>−</mo><mn>1</mn></mrow><mn>0</mn></mfrac></math> using perpendicular condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>r</mi><mo>+</mo><mi>a</mi><mo>−</mo><mi>r</mi><mo>+</mo><mn>0</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>a</mi><mo>=</mo><mn>2</mn><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mi>r</mi></math></p><p>Hence, point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>a</mi><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>And similarly, the direction ratio of </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>R</mi></mrow><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mi>k</mi></mrow></mfenced><mi>i</mi><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And again, finding foot of perpendicular from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> on line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>−</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mn>0</mn></mfrac></math> using perpendicular condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>−</mo><mi>k</mi><mo>−</mo><mi>a</mi><mo>−</mo><mi>k</mi><mo>=</mo><mn>0</mn><mo>⇒</mo><mi>k</mi><mo>=</mo><mn>0</mn></math></p><p>Hence, point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Also, given <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>→</mo></mover><mo>⊥</mo><mover><mrow><mi>P</mi><mi>R</mi></mrow><mo>→</mo></mover></math></p><p>Now, using perpendicular condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>−</mo><mi>r</mi></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>−</mo><mi>k</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mi>r</mi></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>−</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>a</mi><mo>−</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mn>12</mn></math></p>

</details>

---

### Q91. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>(</mo><mn>0</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>,</mo><mo> </mo><mo>–</mo><mn>2</mn><mo>)</mo></math> form the line passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mn>5</mn><mo>,</mo><mo> </mo><mo>–</mo><mn>4</mn><mo>,</mo><mo> </mo><mn>3</mn><mo>)</mo></math> and perpendicular to the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mo>−</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>λ</mi><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mo> </mo><mi>λ</mi><mo>∈</mo><mi>ℝ</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>μ</mi><mfenced><mrow><mo>−</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mo> </mo><mi>μ</mi><mo>∈</mo><mi>ℝ</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>86</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>20</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>54</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>74</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>74</mn></msqrt></math>**

**Detailed Solution:**

<p>Plotting the diagram of the given data we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b103b635-3b5b-4a9d-be30-babebff9dcdd.png" style="width: 250px; height: 196px;"/></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></math> be the DR's of the line perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>λ</mi><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>μ</mi><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>+</mo><mn>5</mn><mi>c</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mo>-</mo><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>+</mo><mn>2</mn><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>+</mo><mn>5</mn><mi>c</mi><mo>=</mo><mn>0</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mo>-</mo><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>+</mo><mn>2</mn><mi>c</mi><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>a</mi><mrow><mo>-</mo><mn>9</mn></mrow></mfrac><mo>=</mo><mfrac><mi>b</mi><mrow><mo>-</mo><mn>9</mn></mrow></mfrac><mo>=</mo><mfrac><mi>c</mi><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>a</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>b</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>c</mi><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p>So, the equation will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>4</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be the foot of perpendicular from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo> </mo><mtext>to</mtext><mo> </mo><mfenced><mi>i</mi></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>4</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mi>k</mi><mo>+</mo><mn>5</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mi>k</mi><mo>-</mo><mn>4</mn><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mo>-</mo><mi>k</mi><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>R</mi><mo>≡</mo><mfenced><mrow><mi>k</mi><mo>+</mo><mn>5</mn><mo>,</mo><mo> </mo><mi>k</mi><mo>-</mo><mn>4</mn><mo>,</mo><mo> </mo><mo>-</mo><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p>So, DR's of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mi>R</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>k</mi><mo>+</mo><mn>5</mn><mo>,</mo><mo> </mo><mi>k</mi><mo>-</mo><mn>6</mn><mo>,</mo><mo> </mo><mn>5</mn><mo>-</mo><mi>k</mi></mrow></mfenced></math>.</p><p>Now, using perpendicular condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mfenced><mrow><mi>k</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mi>k</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>5</mn><mo>-</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>k</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>R</mi><mo>≡</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Q</mi><mi>R</mi><mo>=</mo><msqrt><mn>49</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>9</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Q</mi><mi>R</mi><mo>=</mo><msqrt><mn>74</mn></msqrt></math></p>

</details>

---

### Q92. JEE Main 2024 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let a line passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> intersect the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>(</mo><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>)</mo></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>(</mo><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi><msup><mo>)</mo><mn>2</mn></msup></mrow><mrow><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></math> equals ________________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **196**

**Detailed Solution:**

<blockquote><p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mi>λ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>M</mi><mo>(</mo><mn>3</mn><mi>λ</mi><mo>+</mo><mn>1</mn><mo>,</mo><mn>2</mn><mi>λ</mi><mo>+</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>2</mn><mi>λ</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>≡</mo><mi>M</mi><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi><mo>=</mo><mn>3</mn><mi>λ</mi><mo>+</mo><mn>2</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mi>μ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>N</mi><mo>(</mo><mo>-</mo><mn>3</mn><mi>μ</mi><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>2</mn><mi>μ</mi><mo>+</mo><mn>2</mn><mo>,</mo><mn>4</mn><mi>μ</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>≡</mo><mi>N</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mo>-</mo><mi>μ</mi><mo>+</mo><mn>1</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/61c8f678-be18-49f8-89bd-117fd39ac857.png" style="width: 400px; height: 190px;"/></p><p>Now, from the above diagram, we can see <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>N</mi></math> lie on the same line,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>λ</mi><mo>+</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>3</mn><mi>μ</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>λ</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi>μ</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mi>λ</mi><mo>-</mo><mn>4</mn></mrow><mrow><mn>4</mn><mi>μ</mi><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p>Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>λ</mi><mo>+</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>3</mn><mi>μ</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>λ</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi>μ</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mi>λ</mi><mi>μ</mi><mo>+</mo><mn>2</mn><mi>μ</mi><mo>=</mo><mn>3</mn><mi>λ</mi><mi>μ</mi><mo>+</mo><mi>λ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>μ</mi><mo>=</mo><mi>λ</mi><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>λ</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi>μ</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mi>λ</mi><mo>-</mo><mn>4</mn></mrow><mrow><mn>4</mn><mi>μ</mi><mo>-</mo><mn>2</mn></mrow></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>λ</mi><mi>μ</mi><mo>-</mo><mi>λ</mi><mo>=</mo><mi>λ</mi><mi>μ</mi><mo>+</mo><mn>2</mn><mi>μ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mi>μ</mi><mo>=</mo><mi>λ</mi><mo>+</mo><mn>2</mn><mi>μ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mi>μ</mi><mo>=</mo><mn>2</mn><mi>λ</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><mn>2</mn><mi>μ</mi><mo>=</mo><mi>λ</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>μ</mi><mo>=</mo><mn>2</mn><mo>  </mo><mo>(</mo><mi>λ</mi><mo>≠</mo><mn>0</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mn>4</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>from equation</mtext><mo> </mo><mfenced><mi>i</mi></mfenced></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi><mo>=</mo><mn>14</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>(</mo><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi><msup><mo>)</mo><mn>2</mn></msup></mrow><mrow><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>196</mn></math></p></blockquote>

</details>

---

### Q93. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mover><mi>r</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>λ</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mo> </mo><mi>λ</mi><mo>∈</mo><mi>R</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mover><mi>r</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>μ</mi><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>p</mi><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mo> </mo><mi>μ</mi><mo>∈</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub><mo>:</mo><mover><mi>r</mi><mo>→</mo></mover><mo>=</mo><mi>δ</mi><mo>(</mo><mi>l</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>m</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>n</mi><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>,</mo><mo> </mo><mi>δ</mi><mo>∈</mo><mi>R</mi></math> be three lines such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub></math> is perpendicular to both <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math>. Then the point which lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>4</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>7</mn><mo>,</mo><mn>4</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>7</mn><mo>,</mo><mo>-</mo><mn>4</mn><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>7</mn><mo>,</mo><mn>4</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>4</mn><mo>)</mo></math>**

**Detailed Solution:**

<blockquote><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>⊥</mo><msub><mi>L</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>p</mi><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>p</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>p</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub><mo>⊥</mo><msub><mi>L</mi><mn>1</mn></msub><mo>,</mo><mo> </mo><msub><mi>L</mi><mn>2</mn></msub></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub><mo>∥</mo><mfenced><mrow><msub><mi>L</mi><mn>1</mn></msub><mo>×</mo><msub><mi>L</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>L</mi><mn>1</mn></msub><mo>×</mo><msub><mi>L</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>L</mi><mn>1</mn></msub><mo>×</mo><msub><mi>L</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>On comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub><mo>:</mo><mover><mi>r</mi><mo>→</mo></mover><mo>=</mo><mi>δ</mi><mo>(</mo><mi>l</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>m</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>n</mi><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo></math>, we get that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mi>δ</mi><mo>,</mo><mn>7</mn><mi>δ</mi><mo>,</mo><mn>4</mn><mi>δ</mi><mo>)</mo></math> will lie on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub></math>.</p><p>Now, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>δ</mi><mo>=</mo><mn>1</mn></math> the point will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>4</mn><mo>)</mo></math>.</p></blockquote>

</details>

---

### Q94. JEE Main 2024 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub></math> is the shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>2</mn><mo> </mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>12</mn><mo> </mo><mi>z</mi><mo>,</mo><mo> </mo><mi>x</mi><mo>=</mo><mi>y</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>6</mn><mo> </mo><mi>z</mi><mo>-</mo><mn>6</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>2</mn></msub></math> is the shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>8</mn></mrow><mrow><mo>-</mo><mn>7</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>4</mn></mrow><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>32</mn><msqrt><mn>3</mn></msqrt><mo> </mo><msub><mi mathvariant="normal">d</mi><mn>1</mn></msub></mrow><mrow><mo> </mo><msub><mi mathvariant="normal">d</mi><mn>2</mn></msub></mrow></mfrac></math> is :

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mi>z</mi><mstyle displaystyle="true"><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>12</mn></mfrac></mstyle></mfrac><mo>,</mo></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mfrac><mn>1</mn><mn>6</mn></mfrac></mfrac></math></p><p>Now, given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo></math> shortest distance between <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math></p><p>Now using the formula of shortest distance we get,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><msub><mover><mi>a</mi><mo>→</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi>a</mi><mo>→</mo></mover><mn>1</mn></msub></mrow></mfenced><mo>·</mo><mfenced><mrow><msub><mover><mi>b</mi><mo>→</mo></mover><mn>1</mn></msub><mo>×</mo><msub><mover><mi>b</mi><mo>→</mo></mover><mn>2</mn></msub></mrow></mfenced></mrow><mfenced close="|" open="|"><mfenced><mrow><msub><mover><mi>b</mi><mo>→</mo></mover><mn>1</mn></msub><mo>×</mo><msub><mover><mi>b</mi><mo>→</mo></mover><mn>2</mn></msub></mrow></mfenced></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>·</mo><mfenced><mrow><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>1</mn><mn>12</mn></mfrac><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>×</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>1</mn><mn>12</mn></mfrac><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>×</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>·</mo><mfenced><mrow><mfrac><mover><mi>i</mi><mo>^</mo></mover><mn>6</mn></mfrac><mo>-</mo><mfrac><mover><mi>j</mi><mo>^</mo></mover><mn>4</mn></mfrac><mo>+</mo><mfrac><mover><mi>k</mi><mo>^</mo></mover><mn>2</mn></mfrac></mrow></mfenced></mrow><mfenced close="|" open="|"><mfenced><mrow><mfrac><mover><mi>i</mi><mo>^</mo></mover><mn>6</mn></mfrac><mo>-</mo><mfrac><mover><mi>j</mi><mo>^</mo></mover><mn>4</mn></mfrac><mo>+</mo><mfrac><mover><mi>k</mi><mo>^</mo></mover><mn>2</mn></mfrac></mrow></mfenced></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><msqrt><mfrac><mn>49</mn><mn>144</mn></mfrac></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mfrac><mfrac><mn>7</mn><mn>6</mn></mfrac><mfrac><mn>7</mn><mn>12</mn></mfrac></mfrac></mfenced><mo>=</mo><mn>2</mn></math></p><p>Now, let </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>8</mn></mrow><mrow><mo>-</mo><mn>7</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>4</mn></mrow><mn>5</mn></mfrac><mo>,</mo><mo> </mo><msub><mi>L</mi><mn>4</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p>Similarly finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo></math> shortest distance between <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>4</mn></msub></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><mn>10</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>·</mo><mfenced><mrow><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>7</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>×</mo><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></mrow><mfenced close="|" open="|"><mfenced><mrow><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>7</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>×</mo><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><mn>10</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>·</mo><mfenced><mrow><mn>16</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>16</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>16</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><mfenced close="|" open="|"><mfenced><mrow><mn>16</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>16</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>16</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>160</mn><mo>+</mo><mn>32</mn></mrow><mrow><mn>16</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mfrac><mn>12</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>32</mn><msqrt><mn>3</mn></msqrt><mo> </mo><msub><mi>d</mi><mn>1</mn></msub></mrow><mrow><mo> </mo><msub><mi>d</mi><mn>2</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>32</mn><msqrt><mn>3</mn></msqrt><mo>×</mo><mn>2</mn></mrow><mfrac><mn>12</mn><msqrt><mn>3</mn></msqrt></mfrac></mfrac><mo>=</mo><mn>16</mn></math></p>

</details>

---

### Q95. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi><mo>)</mo></math> be the foot of perpendicular from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>4</mn></mrow><mn>3</mn></mfrac></math>. then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mo>(</mo><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi><mo>)</mo></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>102</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>101</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>99</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>101</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi></mrow></mfenced></math> be the foot of the perpendicular from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>4</mn></mrow><mn>3</mn></mfrac></math> </p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>4</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mi>λ</mi></math></p><p>So, any point on the line is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mi>λ</mi><mo>-</mo><mn>3</mn><mo>,</mo><mo> </mo><mn>2</mn><mi>λ</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>3</mn><mi>λ</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math>, so let the point be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>5</mn><mi>λ</mi><mo>-</mo><mn>3</mn><mo>,</mo><mo> </mo><mn>2</mn><mi>λ</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>3</mn><mi>λ</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p>Now, direction ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><mfenced><mrow><mn>5</mn><mi>λ</mi><mo>-</mo><mn>4</mn><mo>,</mo><mo> </mo><mn>2</mn><mi>λ</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>3</mn><mi>λ</mi><mo>-</mo><mn>7</mn></mrow></mfenced></math></p><p>Now, the line and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> will be perpendicular,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mfenced><mrow><mn>5</mn><mi>λ</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>λ</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><mn>3</mn><mi>λ</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>38</mn><mi>λ</mi><mo>-</mo><mn>43</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mfrac><mn>43</mn><mn>38</mn></mfrac></math></p><p>So, the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mn>5</mn><mo>×</mo><mfrac><mn>43</mn><mn>38</mn></mfrac><mo>-</mo><mn>3</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>×</mo><mfrac><mn>43</mn><mn>38</mn></mfrac><mo>+</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>3</mn><mo>×</mo><mfrac><mn>43</mn><mn>38</mn></mfrac><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p>Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi></mrow></mfenced><mo>=</mo><mn>19</mn><mfenced close="]" open="["><mrow><mn>5</mn><mo>×</mo><mfrac><mn>43</mn><mn>38</mn></mfrac><mo>-</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>×</mo><mfrac><mn>43</mn><mn>38</mn></mfrac><mo>+</mo><mn>1</mn><mo>+</mo><mo> </mo><mn>3</mn><mo>×</mo><mfrac><mn>43</mn><mn>38</mn></mfrac><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>19</mn><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi></mrow></mfenced><mo>=</mo><mn>19</mn><mfenced close="]" open="["><mfrac><mrow><mn>101</mn><mo>+</mo><mn>124</mn><mo>-</mo><mn>23</mn></mrow><mn>38</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>19</mn><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi></mrow></mfenced><mo>=</mo><mn>101</mn></math></p>

</details>

---

### Q96. JEE Main 2024 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> be the origin, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> be the points on the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>8</mn></mrow><mn>12</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>11</mn></mrow><mn>9</mn></mfrac></math> respectively such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>N</mi></math> is the shortest distance between the given lines. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>M</mi></mrow><mo>→</mo></mover><mo>·</mo><mover><mrow><mi>O</mi><mi>N</mi></mrow><mo>→</mo></mover></math> is equal to _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mi>λ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>M</mi><mo>(</mo><mn>4</mn><mi>λ</mi><mo>+</mo><mn>5</mn><mo>,</mo><mi>λ</mi><mo>+</mo><mn>4</mn><mo>,</mo><mn>3</mn><mi>λ</mi><mo>+</mo><mn>5</mn><mo>)</mo></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>8</mn></mrow><mn>12</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>11</mn></mrow><mn>9</mn></mfrac><mo>=</mo><mi>μ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>N</mi><mo>(</mo><mn>12</mn><mi>μ</mi><mo>-</mo><mn>8</mn><mo>,</mo><mn>5</mn><mi>μ</mi><mo>-</mo><mn>2</mn><mo>,</mo><mn>9</mn><mi>μ</mi><mo>-</mo><mn>11</mn><mo>)</mo></math></p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>M</mi><mi>N</mi></mrow><mo>→</mo></mover><mo>=</mo><mo>(</mo><mn>4</mn><mi>λ</mi><mo>-</mo><mn>12</mn><mi>μ</mi><mo>+</mo><mn>13</mn><mo>,</mo><mi>λ</mi><mo>-</mo><mn>5</mn><mi>μ</mi><mo>+</mo><mn>6</mn><mo>,</mo><mn>3</mn><mi>λ</mi><mo>-</mo><mn>9</mn><mi>μ</mi><mo>+</mo><mn>16</mn><mo>)</mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>…</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now finding cross product of direction ratios of line we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>→</mo></mover><mn>1</mn></msub><mo>×</mo><msub><mover><mi>b</mi><mo>→</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>12</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>9</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>8</mn><mover><mi>k</mi><mo>^</mo></mover><mo> </mo><mo> </mo><mo> </mo><mo>…</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now, solving the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mfenced><mn>2</mn></mfenced></math> as they are parallel vectors, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mfrac><mrow><mn>4</mn><mi>λ</mi><mo>-</mo><mn>12</mn><mi>μ</mi><mo>+</mo><mn>13</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>λ</mi><mo>-</mo><mn>5</mn><mi>μ</mi><mo>+</mo><mn>6</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi>λ</mi><mo>-</mo><mn>9</mn><mi>μ</mi><mo>+</mo><mn>16</mn></mrow><mn>8</mn></mfrac></math></p><p>Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mi>λ</mi><mo>-</mo><mn>12</mn><mi>μ</mi><mo>+</mo><mn>13</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>λ</mi><mo>-</mo><mn>5</mn><mi>μ</mi><mo>+</mo><mn>6</mn></mrow><mn>0</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>-</mo><mn>5</mn><mi>μ</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn><mo> </mo><mo> </mo><mo> </mo><mo>…</mo><mfenced><mn>3</mn></mfenced></math></p><p>Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mi>λ</mi><mo>-</mo><mn>12</mn><mi>μ</mi><mo>+</mo><mn>13</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi>λ</mi><mo>-</mo><mn>9</mn><mi>μ</mi><mo>+</mo><mn>16</mn></mrow><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>-</mo><mn>3</mn><mi>μ</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo>…</mo><mfenced><mn>4</mn></mfenced></math></p><p>Solve <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>μ</mi><mo>=</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>(</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>2</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>(</mo><mn>4</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>M</mi></mrow><mo>→</mo></mover><mo>·</mo><mover><mrow><mi>O</mi><mi>N</mi></mrow><mo>→</mo></mover><mo>=</mo><mn>4</mn><mo>+</mo><mn>9</mn><mo>-</mo><mn>4</mn><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q97. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>(</mo><mn>3</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>,</mo><mi mathvariant="normal">Q</mi><mo>(</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>2</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>(</mo><mn>7</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>2</mn><mo>)</mo></math> be the vertices of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∆</mo><mi>PQR</mi></math>. Then, the angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∠</mo><mi>QPR</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>7</mn><mn>18</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>18</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9e44ff45-7f96-4758-bddf-6aed2eda3048.png" style="width: 350px; height: 278px;"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>QP</mi><mo>→</mo></mover><mo>=</mo><mo>-</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>RP</mi><mo>→</mo></mover><mo>=</mo><mo>-</mo><mn>4</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mo>∠</mo><mi>QPR</mi><mo>=</mo><mfrac><mrow><mover><mi>QP</mi><mo>→</mo></mover><mo>·</mo><mover><mi>RP</mi><mo>→</mo></mover></mrow><mrow><mfenced close="|" open="|"><mover><mi>QP</mi><mo>→</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>RP</mi><mo>→</mo></mover></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mo>∠</mo><mi>QPR</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>1</mn></msqrt><msqrt><mn>16</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mo>∠</mo><mi>QPR</mi><mo>=</mo><mfrac><mn>9</mn><mn>18</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∠</mo><mi>QPR</mi><mo>=</mo><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac></math></p>

</details>

---

### Q98. JEE Main 2024 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

A line with direction ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></math> meets the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mi mathvariant="normal">y</mi><mo>+</mo><mn>2</mn><mo>=</mo><mi mathvariant="normal">z</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>2</mn><mi mathvariant="normal">y</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">z</mi></math> respectively at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Q</mi></math>. if the length of the perpendicular from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>12</mn><mo>)</mo></math> to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>PQ</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>l</mi><mn>2</mn></msup></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **65**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mfenced><mrow><mi mathvariant="normal">t</mi><mo>,</mo><mo> </mo><mi mathvariant="normal">t</mi><mo>-</mo><mn>2</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">t</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Q</mi><mfenced><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mo>-</mo><mn>2</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">s</mi><mo>,</mo><mo> </mo><mi mathvariant="normal">s</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>DR</mi><mo>'</mo><mi mathvariant="normal">s</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>PQ</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo> </mo><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>2</mn><mo> </mo><mi mathvariant="normal">s</mi><mo>-</mo><mn>2</mn><mo>-</mo><mi mathvariant="normal">t</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mo>-</mo><mi mathvariant="normal">t</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mo>-</mo><mi mathvariant="normal">t</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mo>-</mo><mn>2</mn><mo>-</mo><mi mathvariant="normal">t</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mo>-</mo><mi mathvariant="normal">t</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi mathvariant="normal">s</mi><mo>-</mo><mn>2</mn><mo>-</mo><mi mathvariant="normal">t</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">s</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">t</mi><mo>+</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">t</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mo>-</mo><mi mathvariant="normal">t</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mo>-</mo><mi mathvariant="normal">t</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mo>-</mo><mn>6</mn><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mo>-</mo><mn>6</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi mathvariant="normal">s</mi><mo>-</mo><mn>8</mn><mo>=</mo><mi mathvariant="normal">s</mi><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">s</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">P</mi><mfenced><mrow><mn>6</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Q</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>,</mo><mo> </mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>PQ</mi><mo>:</mo><mfrac><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mi mathvariant="normal">λ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">x</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">λ</mi><mo>+</mo><mn>2</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">λ</mi><mo>+</mo><mn>2</mn><mo> </mo><mtext>and</mtext><mo> </mo><mi mathvariant="normal">z</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">λ</mi><mo>+</mo><mn>2</mn></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">F</mi><mo>(</mo><mn>2</mn><mi mathvariant="normal">λ</mi><mo>+</mo><mn>2</mn><mo>,</mo><mi mathvariant="normal">λ</mi><mo>+</mo><mn>2</mn><mo>,</mo><mn>2</mn><mi mathvariant="normal">λ</mi><mo>+</mo><mn>2</mn><mo>)</mo></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2acdd6e3-2ba4-4d2b-97d2-f229f5d6c906.png" style="width: 250px; height: 146px;"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>12</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>AF</mi><mo>→</mo></mover><mo>·</mo><mover><mi>PQ</mi><mo>→</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi mathvariant="normal">λ</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mi mathvariant="normal">λ</mi></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi mathvariant="normal">λ</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi mathvariant="normal">λ</mi><mo>+</mo><mn>2</mn><mo>+</mo><mi mathvariant="normal">λ</mi><mo>+</mo><mn>4</mn><mi mathvariant="normal">λ</mi><mo>-</mo><mn>20</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">λ</mi><mo>=</mo><mn>2</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">F</mi><mfenced><mrow><mn>6</mn><mo>,</mo><mo> </mo><mn>4</mn><mo>,</mo><mo> </mo><mn>6</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AF</mi><mo>=</mo><msqrt><mn>65</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>l</mi><mn>2</mn></msup><mo>=</mo><mn>65</mn></math></p>

</details>

---

### Q99. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mi>R</mi></math> be a triangle with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>. Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>)</mo></math> is the mid point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math>. The distance of the centroid of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∆</mo><mi>P</mi><mi>Q</mi><mi>R</mi></math> from the point of intersection of the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mn>1</mn></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>69</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>69</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>99</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>69</mn></msqrt></math>**

**Detailed Solution:**

<p>Given: </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>k</mi><mfenced><mtext>let</mtext></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>k</mi><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mo>-</mo><mi>k</mi><mo>+</mo><mn>3</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mi>λ</mi><mfenced><mtext>let</mtext></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mi>λ</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>3</mn><mi>λ</mi><mo>-</mo><mn>3</mn><mo>.</mo><mo> </mo><mi>z</mi><mo>=</mo><mi>λ</mi><mo>-</mo><mn>1</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mo>=</mo><mi>λ</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn><mi>k</mi><mo>=</mo><mo>-</mo><mn>3</mn><mi>λ</mi><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn><mi>k</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>k</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>6</mn><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p>So, the intersection point of two given lines is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>-</mo><mn>6</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7376d08a-1c72-4fd4-9b79-516e0c2d82e0.png" style="width: 380px; height: 253px;"/></p><p>Now, we know that centroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math> divides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>R</mi></math> (median) in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo> </mo><mo>:</mo><mo> </mo><mn>2</mn></math>.</p><p>So, by using section formula, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mo>≡</mo><mfenced><mrow><mfrac><mrow><mn>1</mn><mo>×</mo><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>×</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn><mo>×</mo><mn>4</mn><mo>+</mo><mn>2</mn><mo>×</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn><mo>×</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>×</mo><mn>2</mn></mrow><mn>3</mn></mfrac></mrow></mfenced></math></p><p>So, centroid is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mo>(</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>)</mo></math>.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be the point of intersection of given lines.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mi>G</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mn>6</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mi>G</mi><mo>=</mo><msqrt><mn>1</mn><mo>+</mo><mn>64</mn><mo>+</mo><mn>4</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mi>G</mi><mo>=</mo><msqrt><mn>69</mn></msqrt></math></p>

</details>

---

### Q100. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the image of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>7</mn><mo>)</mo></math> in the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></math> be the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">α</mi><mo>,</mo><mi mathvariant="normal">β</mi><mo>,</mo><mi mathvariant="normal">γ</mi><mo>)</mo></math>. Then which one of the following points lies on the line passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">α</mi><mo>,</mo><mi mathvariant="normal">β</mi><mo>,</mo><mi mathvariant="normal">γ</mi><mo>)</mo></math> and making angles <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi mathvariant="normal">π</mi></mrow><mn>4</mn></mfrac></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>-</mo></math>axis and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">z</mi><mo>-</mo></math>axis respectively and an acute angle with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>-</mo></math>axis?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>4</mn><mo>,</mo><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>)</mo></math>**

**Detailed Solution:**

<p>Given: </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">L</mi><mn>1</mn></msub><mo>≡</mo><mfrac><mi mathvariant="normal">x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mi mathvariant="normal">λ</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8b18f193-0fc1-4d3e-8924-09fb7ad77578.png" style="width: 250px; height: 201px;"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">M</mi><mo>(</mo><mi mathvariant="normal">λ</mi><mo>,</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi mathvariant="normal">λ</mi><mo>,</mo><mn>2</mn><mo>+</mo><mn>3</mn><mi mathvariant="normal">λ</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>PM</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mi mathvariant="normal">λ</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi mathvariant="normal">λ</mi></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>3</mn><mi mathvariant="normal">λ</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>PM</mi><mo>→</mo></mover></math> is perpendicular to line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">L</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>PM</mi><mo>→</mo></mover><mo>·</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>PM</mi><mo>→</mo></mover><mo>.</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>=</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mi mathvariant="normal">λ</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi mathvariant="normal">λ</mi></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>3</mn><mi mathvariant="normal">λ</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">λ</mi><mo>-</mo><mn>1</mn><mo>+</mo><mn>4</mn><mi mathvariant="normal">λ</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>9</mn><mi mathvariant="normal">λ</mi><mo>-</mo><mn>15</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>14</mn><mi mathvariant="normal">λ</mi><mo>=</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">λ</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">M</mi><mo>=</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>)</mo></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> is midpoint of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">P</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">Q</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>≡</mo><mfenced><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">α</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>0</mn><mo>+</mo><mi mathvariant="normal">β</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mo>+</mo><mi mathvariant="normal">γ</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">α</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mfrac><mi mathvariant="normal">β</mi><mn>2</mn></mfrac><mo>=</mo><mn>3</mn><mo>,</mo><mo> </mo><mfrac><mrow><mn>7</mn><mo>+</mo><mi mathvariant="normal">γ</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">α</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">β</mi><mo>=</mo><mn>6</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">γ</mi><mo>=</mo><mn>3</mn></math></p><p>Now, required line having direction cosine <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">l</mi><mo>,</mo><mi mathvariant="normal">m</mi><mo>,</mo><mi mathvariant="normal">n</mi></mrow></mfenced></math>, where given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mi>cos</mi><mfenced><mfrac><mrow><mo>-</mo><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo> </mo><mo>&amp;</mo><mo> </mo><mi>n</mi><mo>=</mo><mi>cos</mi><mfenced><mfrac><mrow><mn>3</mn><mi mathvariant="normal">π</mi></mrow><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">l</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">n</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">l</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">l</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">l</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>[Line make acute angle with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>-</mo></math>axis]</p><p>So, the equation of line passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> will be given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">r</mi><mo>→</mo></mover><mo>=</mo><mo>(</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>)</mo><mo>+</mo><mi mathvariant="normal">μ</mi><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math> satisfying for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">μ</mi><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q101. JEE Main 2024 (27 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

The lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mi mathvariant="normal">y</mi><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>-</mo><mn>7</mn></mrow><mn>16</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac></math> intersect at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi></math>. If the distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi></math> from the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><msup><mi>l</mi><mn>2</mn></msup></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **108**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mi mathvariant="normal">y</mi><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>-</mo><mn>7</mn></mrow><mn>16</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mi mathvariant="normal">y</mi><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>-</mo><mn>7</mn></mrow><mn>8</mn></mfrac><mo>=</mo><mi mathvariant="normal">λ</mi><mo> </mo><mfenced><mtext>let</mtext></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mi mathvariant="normal">k</mi><mo> </mo><mfenced><mtext>let</mtext></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">x</mi><mo>=</mo><mi mathvariant="normal">λ</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>4</mn><mi mathvariant="normal">k</mi><mo>-</mo><mn>3</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">y</mi><mo>=</mo><mo>-</mo><mi mathvariant="normal">λ</mi><mo>=</mo><mn>3</mn><mi mathvariant="normal">k</mi><mo>-</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">z</mi><mo>=</mo><mn>8</mn><mi mathvariant="normal">λ</mi><mo>+</mo><mn>7</mn><mo>=</mo><mi mathvariant="normal">k</mi><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">λ</mi><mo>=</mo><mo>-</mo><mn>5</mn><mo>+</mo><mn>4</mn><mi mathvariant="normal">k</mi><mo>,</mo><mo> </mo><mi mathvariant="normal">λ</mi><mo>=</mo><mo>-</mo><mn>3</mn><mi mathvariant="normal">k</mi><mo>+</mo><mn>2</mn><mo>,</mo><mo> </mo><mn>8</mn><mi mathvariant="normal">λ</mi><mo>-</mo><mi mathvariant="normal">k</mi><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>5</mn><mo>+</mo><mn>4</mn><mi mathvariant="normal">k</mi><mo>=</mo><mo>-</mo><mn>3</mn><mi mathvariant="normal">k</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>7</mn><mi mathvariant="normal">k</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">k</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">λ</mi><mo>=</mo><mo>-</mo><mn>3</mn><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>2</mn><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">z</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">P</mi><mo>≡</mo><mo>(1,1,-1)</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/050a89b7-ae8e-422d-98ea-34a394bb8f3f.png" style="width: 350px; height: 211px;"/></p><p>Projection of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>PQ</mi><mo>≡</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>QR</mi></math> line with direction ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> is given by, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>QR</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mo>-</mo><mn>2</mn></mrow><msqrt><mn>4</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>1</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>14</mn></msqrt></mfrac></math></p><p>Now, in triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>PQR</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><msup><mi>l</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mo>-</mo><mfrac><mn>4</mn><mn>14</mn></mfrac><mo>=</mo><mfrac><mn>108</mn><mn>14</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>14</mn><msup><mi>l</mi><mn>2</mn></msup><mo>=</mo><mn>108</mn></math></p>

</details>

---

### Q102. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mrow><mo>-</mo><mn>3</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>λ</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>5</mn></mrow></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><msqrt><mn>5</mn></msqrt></mfrac></math>, then the sum of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mrow><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>λ</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>5</mn></mrow></mfrac></math></p><p>The shortest distance between the lines
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mo>(</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>-</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>)</mo><mo>·</mo><mfenced><mrow><mover><msub><mi mathvariant="normal">d</mi><mn>1</mn></msub><mo>→</mo></mover><mo>×</mo><mover><msub><mi mathvariant="normal">d</mi><mn>2</mn></msub><mo>→</mo></mover></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><mover><msub><mi mathvariant="normal">d</mi><mn>1</mn></msub><mo>→</mo></mover><mo>×</mo><mover><msub><mi mathvariant="normal">d</mi><mn>2</mn></msub><mo>→</mo></mover></mrow></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>≡</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>b</mi><mo>≡</mo><mfenced><mrow><mi>λ</mi><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>a</mi><mo>→</mo></mover><mo>-</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>λ</mi><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>a</mi><mo>→</mo></mover><mo>-</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mn>4</mn><mo>-</mo><mi>λ</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So, the shortest distance is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mi>λ</mi><mo>-</mo><mn>4</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr></mtable></mfenced><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr></mtable></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mo>(</mo><mi>λ</mi><mo>-</mo><mn>4</mn><mo>)</mo><mo>(</mo><mo>-</mo><mn>10</mn><mo>+</mo><mn>12</mn><mo>)</mo><mo>-</mo><mn>0</mn><mo>+</mo><mn>2</mn><mo>(</mo><mn>4</mn><mo>-</mo><mn>4</mn><mo>)</mo></mrow><mrow><mo>|</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>1</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi>k</mi><mo>^</mo></mover><mo>|</mo></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>6</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>2</mn><mo>(</mo><mi>λ</mi><mo>-</mo><mn>4</mn><mo>)</mo></mrow><msqrt><mn>5</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mo>=</mo><mo>|</mo><mi>λ</mi><mo>-</mo><mn>4</mn><mo>|</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>-</mo><mn>4</mn><mo>=</mo><mo>±</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mn>7</mn><mo>,</mo><mn>1</mn></math></p><p>So, sum of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>.</p>

</details>

---

### Q103. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The distance, of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>7</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>11</mn><mo>)</mo></math> from the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>8</mn></mrow><mn>3</mn></mfrac></math> along the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>6</mn></mfrac></math>, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>**

**Detailed Solution:**

<p>Given lines are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>8</mn></mrow><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>6</mn></mfrac></math>.</p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> be a line parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>6</mn></mfrac></math> which intersects <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>8</mn></mrow><mn>3</mn></mfrac></math> at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>≡</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>11</mn></mrow></mfenced></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/51ff028d-d6cc-44ef-afc4-24f91a8f4059.png" style="width: 300px; height: 212px;"/></p><p>So, equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>7</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>11</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mi>λ</mi><mfenced><mtext>let</mtext></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>2</mn><mi>λ</mi><mo>+</mo><mn>7</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>3</mn><mi>λ</mi><mo>-</mo><mn>2</mn><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mn>6</mn><mi>λ</mi><mo>+</mo><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>B</mi><mo>≡</mo><mo>(</mo><mn>2</mn><mi>λ</mi><mo>+</mo><mn>7</mn><mo>,</mo><mo>-</mo><mn>3</mn><mi>λ</mi><mo>-</mo><mn>2</mn><mo>,</mo><mn>6</mn><mi>λ</mi><mo>+</mo><mn>11</mn><mo>)</mo></math></p><p>Also, the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>8</mn></mrow><mn>3</mn></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>2</mn><mi>λ</mi><mo>+</mo><mn>7</mn><mo>-</mo><mn>6</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mi>λ</mi><mo>-</mo><mn>2</mn><mo>-</mo><mn>4</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mn>6</mn><mi>λ</mi><mo>+</mo><mn>11</mn><mo>-</mo><mn>8</mn></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>3</mn><mi>λ</mi><mo>-</mo><mn>2</mn><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>3</mn><mi>λ</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>B</mi><mo>≡</mo><mo>(</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>AB</mi><mo>=</mo><msqrt><mo>(</mo><mn>7</mn><mo>-</mo><mn>3</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mn>4</mn><mo>+</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mn>11</mn><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>AB</mi><mo>=</mo><msqrt><mn>16</mn><mo>+</mo><mn>36</mn><mo>+</mo><mn>144</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>AB</mi><mo>=</mo><msqrt><mn>196</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>AB</mi><mo>=</mo><mn>14</mn></math></p>

</details>

---

### Q104. JEE Main 2023 (15 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

If the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>=</mo><mi>z</mi></math> intersects the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mi>A</mi><mo>+</mo><mi>y</mi><mo>&#160;</mo><mi>sin</mi><mi>B</mi><mo>+</mo><mi>z</mi><mo>&#160;</mo><mi>sin</mi><mi>C</mi><mo>-</mo><mn>18</mn><mo>=</mo><mn>0</mn><mo>=</mo><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mn>2</mn><mi>A</mi><mo>+</mo><mi>y</mi><mo>&#160;</mo><mi>sin</mi><mn>2</mn><mi>B</mi><mo>+</mo><mi>z</mi><mi>sin</mi><mn>2</mn><mi>C</mi><mo>-</mo><mn>9</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>C</mi></math> are the angles of a triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn><mfenced><mrow><mi>sin</mi><mfrac><mi>A</mi><mn>2</mn></mfrac><mi>sin</mi><mfrac><mi>B</mi><mn>2</mn></mfrac><mi>sin</mi><mfrac><mi>C</mi><mn>2</mn></mfrac></mrow></mfenced></math> is equal to _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>=</mo><mi>z</mi></math> intersects the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mi>A</mi><mo>+</mo><mi>y</mi><mo>&#160;</mo><mi>sin</mi><mi>B</mi><mo>+</mo><mi>z</mi><mo>&#160;</mo><mi>sin</mi><mi>C</mi><mo>-</mo><mn>18</mn><mo>=</mo><mn>0</mn><mo>=</mo><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mn>2</mn><mi>A</mi><mo>+</mo><mi>y</mi><mo>&#160;</mo><mi>sin</mi><mn>2</mn><mi>B</mi><mo>+</mo><mi>z</mi><mi>sin</mi><mn>2</mn><mi>C</mi><mo>-</mo><mn>9</mn></math></p><p>So, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>=</mo><mi>z</mi><mo>=</mo><mi>k</mi></math></p><p>Now putting the value in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mi>A</mi><mo>+</mo><mi>y</mi><mo>&#160;</mo><mi>sin</mi><mi>B</mi><mo>+</mo><mi>z</mi><mo>&#160;</mo><mi>sin</mi><mi>C</mi><mo>=</mo><mn>18</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mfenced><mrow><mi>sin</mi><mi>A</mi><mo>+</mo><mi>sin</mi><mi>B</mi><mo>+</mo><mi>sin</mi><mi>C</mi></mrow></mfenced><mo>=</mo><mn>18</mn></math></p><p>Now we know that, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>C</mi></math> are angles of triangle then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>A</mi><mo>+</mo><mi>sin</mi><mi>B</mi><mo>+</mo><mi>sin</mi><mi>C</mi><mo>=</mo><mn>4</mn><mi>cos</mi><mfrac><mi>A</mi><mn>2</mn></mfrac><mo>&#183;</mo><mi>cos</mi><mfrac><mi>B</mi><mn>2</mn></mfrac><mo>&#183;</mo><mi>cos</mi><mfrac><mi>C</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mfenced><mrow><mn>4</mn><mi>cos</mi><mfrac><mi>A</mi><mn>2</mn></mfrac><mo>&#183;</mo><mi>cos</mi><mfrac><mi>B</mi><mn>2</mn></mfrac><mo>&#183;</mo><mi>cos</mi><mfrac><mi>C</mi><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>18</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mfenced><mrow><mi>sin</mi><mn>2</mn><mi>A</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>A</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>A</mi></mrow></mfenced><mo>=</mo><mn>9</mn></math></p><p>And similalry <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>2</mn><mi>A</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>A</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>A</mi><mo>=</mo><mn>4</mn><mi>sin</mi><mi>A</mi><mo>&#183;</mo><mi>sin</mi><mi>B</mi><mo>&#183;</mo><mi>sin</mi><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mfenced><mrow><mn>4</mn><mi>sin</mi><mi>A</mi><mo>&#183;</mo><mi>sin</mi><mi>B</mi><mo>&#183;</mo><mi>sin</mi><mi>C</mi></mrow></mfenced><mo>=</mo><mn>9</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Now dividing equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi>sin</mi><mfrac><mi>A</mi><mn>2</mn></mfrac><mo>&#183;</mo><mi>sin</mi><mfrac><mi>B</mi><mn>2</mn></mfrac><mo>&#183;</mo><mi>sin</mi><mfrac><mi>C</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>18</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>80</mn><mo>&#160;</mo><mi>sin</mi><mfrac><mi>A</mi><mn>2</mn></mfrac><mo>&#183;</mo><mi>sin</mi><mfrac><mi>B</mi><mn>2</mn></mfrac><mo>&#183;</mo><mi>sin</mi><mfrac><mi>C</mi><mn>2</mn></mfrac><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q105. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math>, for which the shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>&#955;</mi></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>6</mn></mrow><mn>1</mn></mfrac></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mi>&#955;</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mn>0</mn></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mfenced close="|" open="|"><mrow><munder><mo>&#8721;</mo><mrow><mi>&#955;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mi>&#955;</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>306</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>304</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>308</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>302</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>306</mn></math>**

**Detailed Solution:**

<blockquote><p>The given lines are<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>&#955;</mi></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>6</mn></mrow><mn>1</mn></mfrac></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mi>&#955;</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mn>0</mn></mfrac></math></p><p>We know that the shortest distance between two lines is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msub><mover><mi>n</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>n</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><msub><mover><mi>n</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>n</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mfrac></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mn>13</mn><mo>&#160;</mo><mfenced><mtext>given</mtext></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mover><mi>n</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>n</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now using the above formula of distance we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mfrac><mrow><mo>(</mo><mn>2</mn><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>&#183;</mo><mo>(</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo></mrow><msqrt><mn>16</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>144</mn></msqrt></mfrac></mfenced><mo>=</mo><mn>13</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mfrac><mrow><mo>(</mo><mn>2</mn><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>&#183;</mo><mo>(</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo></mrow><mn>13</mn></mfrac></mfenced><mo>=</mo><mn>13</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>8</mn><mi>&#955;</mi><mo>+</mo><mn>9</mn><mo>+</mo><mn>144</mn></mrow></mfenced><mo>=</mo><mn>169</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>8</mn><mi>&#955;</mi><mo>+</mo><mn>153</mn></mrow></mfenced><mo>=</mo><mn>169</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mi>&#955;</mi><mo>=</mo><mo>&#177;</mo><mn>169</mn><mo>-</mo><mn>153</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mn>16</mn><mn>8</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mn>322</mn></mrow><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mfenced close="|" open="|"><mrow><munder><mo>&#8721;</mo><mrow><mi>&#955;</mi><mo>&#8712;</mo><mi>s</mi></mrow></munder><mi>&#955;</mi></mrow></mfenced><mo>=</mo><mn>8</mn><mfenced close="|" open="|"><mrow><mfrac><mn>16</mn><mn>8</mn></mfrac><mo>-</mo><mfrac><mn>322</mn><mn>8</mn></mfrac></mrow></mfenced><mo>=</mo><mn>306</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q106. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> be the foot of perpendicular from the point<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>P</mi><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> on the line passing through the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>8</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>7</mn><mo>,</mo><mn>5</mn><mo>)</mo></math>. Then the distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> from the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> be the foot of perpendicular from the point<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>P</mi><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> on the line passing through the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>8</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>7</mn><mo>,</mo><mn>5</mn><mo>)</mo></math>,</p><p>Now finding direction ratio of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>-</mo><mn>1</mn><mo>,</mo><mn>5</mn><mo>+</mo><mn>7</mn><mo>,</mo><mn>8</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>12</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Hence, the equation of Line will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>7</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mi>r</mi></math></p><p>Now let point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>&#8801;</mo><mo>(</mo><mi>r</mi><mo>+</mo><mn>1</mn><mo>,</mo><mn>4</mn><mi>r</mi><mo>-</mo><mn>7</mn><mo>,</mo><mi>r</mi><mo>+</mo><mn>5</mn><mo>)</mo></math></p><p>And given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8801;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math></p><p>So, direction ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>N</mi><mo>(</mo><mi>r</mi><mo>,</mo><mo>&#160;</mo><mn>4</mn><mi>r</mi><mo>-</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi>r</mi><mo>+</mo><mn>2</mn><mo>)</mo></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>N</mi><mo>&#8869;</mo><mi>L</mi></math> so by perpendicular condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>+</mo><mn>4</mn><mo>(</mo><mn>4</mn><mi>r</mi><mo>-</mo><mn>5</mn><mo>)</mo><mo>+</mo><mo>(</mo><mi>r</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>&#8801;</mo><mo>(</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>6</mn><mo>)</mo></math></p><p>Now finding, distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>(</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>6</mn><mo>)</mo></math> from plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>Distance</mtext><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>4</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>5</mn></mrow><msqrt><mn>4</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>1</mn></msqrt></mfrac></mfenced><mo>=</mo><mn>7</mn></math></p></blockquote>

</details>

---

### Q107. JEE Main 2023 (11 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let a line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> pass through the origin and be perpendicular to the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>11</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math> and
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>&#956;</mi><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is the point of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"/>,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math> is the foot of perpendicular from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced></math> is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Given,</p><p>A line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> pass through the origin and be perpendicular to the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>11</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math> and
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>&#956;</mi><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math></p><p>So, direction ratio of line will be,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Hence, the equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> which passes through origin will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>:</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#963;</mi><mo>(</mo><mo>-</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo></math></p><p>Now finding the intersection point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>4</mn><mi>&#963;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>11</mn><mo>+</mo><mn>2</mn><mi>&#955;</mi><mo>=</mo><mn>5</mn><mi>&#963;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn><mo>+</mo><mn>3</mn><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#963;</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>So, from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>3</mn></mfenced></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>14</mn><mo>+</mo><mn>6</mn><mi>&#955;</mi><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#963;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Hence, point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8801;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>-</mo><mn>5</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Now finding the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> which is foot of perpendicular from point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mo>-</mo><mn>5</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> on line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mo>&#8201;</mo><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>&#956;</mi><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> we get,</p><p>Now any point on line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mfenced><mrow><mn>2</mn><mi>&#956;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mi>&#956;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>&#956;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Now direction ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>5</mn><mo>+</mo><mn>2</mn><mi>&#956;</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mi>&#956;</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>&#956;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover><mo>=</mo><mn>0</mn></math></p><p>Now using the perpendicular condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>(</mo><mo>-</mo><mn>5</mn><mo>+</mo><mn>2</mn><mi>&#956;</mi><mo>)</mo><mo>+</mo><mn>2</mn><mo>(</mo><mn>2</mn><mi>&#956;</mi><mo>+</mo><mn>5</mn><mo>)</mo><mo>+</mo><mn>1</mn><mo>(</mo><mi>&#956;</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/260b1c22-478c-4717-9592-51ef6923ebed-image.png" style="width: 250px; height: 187px;" /></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>2</mn><mi>&#956;</mi><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>&#956;</mi><mo>+</mo><mi>&#956;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>5</mn><mi>&#956;</mi><mo>=</mo><mfrac><mn>5</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q108. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mn>6</mn><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>8</mn></mrow><mn>5</mn></mfrac></math> intersect the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>7</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac></math>  and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mi>y</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mn>1</mn></mfrac></math> at the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> respectively. Then the distance of the mid-point of the line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> from the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>14</mn></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mn>6</mn><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>8</mn></mrow><mn>5</mn></mfrac></math> intersect the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>7</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac></math>  and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mi>y</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mn>1</mn></mfrac></math> at the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> respectively,</p><p>Now plotting the diagram, we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d54d331a-574b-4286-b25e-515b4a5ec878.png" style="width: 450px; height: 235px;" /></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>6</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>8</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mi>&#955;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>7</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mi>t</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8801;</mo><mo>(</mo><mi>&#955;</mi><mo>,</mo><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>6</mn><mo>,</mo><mn>5</mn><mi>&#955;</mi><mo>-</mo><mn>8</mn><mo>)</mo><mo>&#8801;</mo><mo>(</mo><mn>4</mn><mi>t</mi><mo>+</mo><mn>5</mn><mo>,</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>7</mn><mo>,</mo><mi>t</mi><mo>-</mo><mn>2</mn><mo>)</mo></math></p><p>Now comparing both side and solving we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#955;</mi><mo>=</mo><mn>1</mn></math></p><p>Hence, point<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>A</mi><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mo>&#8211;</mo><mn>3</mn><mo>)</mo></math></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>6</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>8</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mi>&#956;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mi>k</mi></math> we get,</p><p>For point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8801;</mo><mo>(</mo><mi>&#956;</mi><mo>,</mo><mo>-</mo><mn>2</mn><mi>&#956;</mi><mo>+</mo><mn>6</mn><mo>,</mo><mn>5</mn><mi>&#956;</mi><mo>-</mo><mn>8</mn><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8801;</mo><mo>(</mo><mn>6</mn><mi>k</mi><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>3</mn><mo>,</mo><mi>k</mi><mo>+</mo><mn>6</mn><mo>)</mo></math></p><p>Now comparing both side and solving we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#956;</mi><mo>=</mo><mn>3</mn></math></p><p>Hence, point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>(</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>)</mo></math></p><p>So, mid-point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mi>M</mi><mo>(</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>)</mo></math></p><p>Now finding, distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> from the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>&#160;</mo><mo>&#8211;</mo><mo>&#160;</mo><mn>2</mn><mi>y</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>z</mi><mo>&#160;</mo><mo>&#8211;</mo><mo>&#160;</mo><mn>14</mn><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mrow><mn>4</mn><mo>-</mo><mn>4</mn><mo>+</mo><mn>2</mn><mo>-</mo><mn>14</mn></mrow><msqrt><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt></mfrac></mfenced><mo>=</mo><mfenced close="|" open="|"><mfrac><mstyle displaystyle="true"><mo>-</mo><mn>12</mn></mstyle><mstyle displaystyle="true"><mn>3</mn></mstyle></mfrac></mfenced><mo>=</mo><mn>4</mn></math></p></blockquote>

</details>

---

### Q109. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>3</mn></mrow><mn>0</mn></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>3</mn></mrow><mn>0</mn></mfrac></math></p><p>Now we know that,</p><p>Shortest distance between two skew lines is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><mover><msub><mi>a</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>-</mo><mover><msub><mi>a</mi><mn>1</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced><mfenced><mrow><mover><msub><mi>n</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>n</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><mover><msub><mi>n</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>n</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced></mfrac></mfenced></math></p><p>Now finding, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>n</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>n</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><msub><mi>n</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>n</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>a</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>-</mo><mover><msub><mi>a</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mo>-</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now putting the value in formula we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mfenced><mrow><mo>-</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><msqrt><mn>16</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>4</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mo>-</mo><mn>24</mn><mo>+</mo><mn>2</mn><mo>-</mo><mn>32</mn></mrow><mn>6</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>54</mn><mn>6</mn></mfrac><mo>=</mo><mn>9</mn></math></p></blockquote>

</details>

---

### Q110. JEE Main 2023 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>&#955;</mi><mn>2</mn></msub></math> be the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> for which the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math> are at equal distance  from the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>6</mn><mi>z</mi><mo>+</mo><mn>7</mn></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mn>1</mn></msub><mo>&#62;</mo><msub><mi>&#955;</mi><mn>2</mn></msub></math></p><p>then the distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mo>-</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mo>,</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mo>,</mo><msub><mi>&#955;</mi><mn>1</mn></msub></mrow></mfenced></math> from the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>7</mn></mrow><mn>2</mn></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>&#955;</mi><mn>2</mn></msub></math> be the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> for which the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math> are at equal distance  from the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>6</mn><mi>z</mi><mo>+</mo><mn>7</mn></math>,</p><p>So, by using distance formula of a point from a plane we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mrow><mo>-</mo><mn>4</mn><mo>+</mo><mn>0</mn><mo>-</mo><mn>6</mn><mo>+</mo><mn>7</mn></mrow><msqrt><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>6</mn><mn>2</mn></msup></msqrt></mfrac></mfenced><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>5</mn><mo>+</mo><mn>3</mn><mo>-</mo><mn>6</mn><mi>&#955;</mi><mo>+</mo><mn>7</mn></mrow><msqrt><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>6</mn><mn>2</mn></msup></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mfrac><mrow><mo>-</mo><mn>4</mn><mo>+</mo><mn>0</mn><mo>-</mo><mn>6</mn><mo>+</mo><mn>7</mn></mrow><mn>7</mn></mfrac></mfenced><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>5</mn><mo>+</mo><mn>3</mn><mo>-</mo><mn>6</mn><mi>&#955;</mi><mo>+</mo><mn>7</mn></mrow><mn>7</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>15</mn><mo>-</mo><mn>6</mn><mi>&#955;</mi></mrow><mn>7</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#955;</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mn>1</mn></msub><mo>&#62;</mo><mo>&#160;</mo><msub><mi>&#955;</mi><mn>2</mn></msub></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mo>-</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>&#955;</mi><mn>1</mn></msub></mrow></mfenced><mo>=</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math></p><p>Now finding the distance of point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> from the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>7</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mi>&#955;</mi></math> we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2878d2a3-0260-44d4-ba97-5f06f97d2e02.png" style="width: 300px; height: 251px;" /></p><p>Now form diagram we can see that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>M</mi></mrow><mo>&#8594;</mo></mover></math> is perpendicular to given line,</p><p>So, by perpendicular condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>M</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>&#955;</mi><mo>=</mo><mn>18</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn></math></p><p>Hence, the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mfenced><mrow><mn>7</mn><mo>,</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p>So, the distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mover><mrow><mi>P</mi><mi>M</mi></mrow><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>6</mn><mn>2</mn></msup></msqrt><mo>=</mo><mn>9</mn></math></p></blockquote>

</details>

---

### Q111. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>3</mn></mrow><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>4</mn></mrow><mn>2</mn></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>6</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>6</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>6</mn></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>3</mn></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>4</mn></mrow><mn>2</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mspace linebreak="newline"></mspace><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mo>-</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced><mo>=</mo><msqrt><msup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>1</mn></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>1</mn></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>6</mn></msqrt></math></p><p>Shortest distance between the lines </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><mo>-</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><msqrt><mn>6</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>6</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>7</mn></mrow><msqrt><mn>6</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>3</mn></mrow><msqrt><mn>6</mn></msqrt></mfrac><mo>&#160;</mo><mi>units</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><msqrt><mn>6</mn></msqrt><mo>&#160;</mo><mi>units</mi></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q112. JEE Main 2023 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>If the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>-</mo><mi>y</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mi>&#945;</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mi>&#946;</mi></mfrac></math> intersect, then the magnitude of the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>&#945;</mi><mi>&#946;</mi></math> is _____.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

<blockquote><p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mi>&#945;</mi></mfrac><mo>=</mo><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>0</mn></mrow><mi>&#946;</mi></mfrac><mo>=</mo><mi>&#956;</mi></math></p><p>For point of intersection</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>5</mn><mi>&#956;</mi><mo>+</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>2</mn><mi>&#956;</mi><mo>+</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#955;</mi><mo>+</mo><mn>3</mn><mo>=</mo><mi>&#946;</mi><mi>&#956;</mi><mo>+</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi>iii</mi></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>&#955;</mi><mo>=</mo><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Now, from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>iii</mi></mfenced></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><mn>3</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>8</mn><mi>&#945;</mi><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>8</mn><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>8</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>&#945;</mi><mo>+</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></mrow></mfenced><mo>-</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>8</mn><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>18</mn></math></p><p>So, Minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mn>18</mn></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p></blockquote>

</details>

---

### Q113. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> pass through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>)</mo><mo>,</mo></math> intersect the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac></math> and be parallel to the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>4</mn></math>. Then the distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#8211;</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>)</mo></math> from the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>74</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>69</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>54</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>74</mn></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> pass through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>)</mo><mo>,</mo></math> intersect the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac></math> and be parallel to the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>4</mn></math>,</p><p>Now plotting the diagram of above data we have,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8c01d75b-9126-4997-8fea-f6241da8d038-image.png" style="width: 459px; height: 227px;" /></p><p>Now let the direction of line which passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></math></p><p>Now the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>L</mi><mn>1</mn></msub></math> are coplanar,</p><p>So coplanar condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mn>2</mn><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn><mo>-</mo><mn>2</mn></mtd><mtd><mn>4</mn><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> is perpendicular to the normal vector of the plane, </p><p>So by perpendicular condition we get,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>3</mn><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>So, from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>b</mi><mo>=</mo><mi>c</mi></math></p><p>So, equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mi>&#955;</mi></math></p><p>So any point on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> can be taken as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>+</mo><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>+</mo><mi>&#955;</mi></mrow></mfenced></math>,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/99f21a49-4599-4831-9b07-464452ae9a08-image.png" style="width: 150px; height: 173px;" /></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover></math> will be perpendicular to the direction ratio of the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math>,</p><p>So, again by perpendicular condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>+</mo><mi>&#955;</mi><mo>+</mo><mn>10</mn><mo>+</mo><mi>&#955;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>Hence,<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>A</mi><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>P</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math></p><p>So, by distance formula we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>P</mi><mo>=</mo><msqrt><mn>74</mn></msqrt></math></p></blockquote>

</details>

---

### Q114. JEE Main 2023 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Let the image of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>)</mo></math> in the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>&#8211;</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>9</mn></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>.</mo></math> If the coordinates of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>)</mo><mo>,</mo></math> then the square of the area of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mi>R</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo>.</mo></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **594**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The image of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>)</mo></math> in the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>&#8211;</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>9</mn></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>,</p><p>The coordinates of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>)</mo><mo>,</mo></math> </p><p>Now plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d349cccb-230e-408b-a564-dfc357abe6ef-image.png" style="width: 250px; height: 231px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> lies on plane as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>6</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math> satisfy the plane equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>&#8211;</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>9</mn></math></p><p>Now length of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>R</mi><mo>=</mo><msqrt><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mn>8</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>105</mn></msqrt></math></p><p>Now finding the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>R</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>P</mi><mi>M</mi></math>(which is normal vector to plane) we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mover><mrow><mi>P</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mrow><mi>P</mi><mi>M</mi></mrow><mo>&#8594;</mo></mover></mrow><mrow><mfenced close="|" open="|"><mover><mrow><mi>P</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover></mfenced><mo>&#183;</mo><mfenced close="|" open="|"><mover><mrow><mi>P</mi><mi>M</mi></mrow><mo>&#8594;</mo></mover></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mo>(</mo><mn>5</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>8</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>)</mo><mo>(</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>)</mo></mrow><mrow><msqrt><mn>105</mn></msqrt><msqrt><mn>6</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>6</mn><msqrt><mn>630</mn></msqrt></mfrac></math></p><p>Now Area<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>&#8710;</mo><mi>P</mi><mi>Q</mi><mi>R</mi><mo>)</mo><mo>=</mo><mn>2</mn><mo>area</mo><mo>(</mo><mo>&#8710;</mo><mi>P</mi><mi>M</mi><mi>R</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mi>P</mi><mi>Q</mi><mi>R</mi><mo>=</mo><mn>2</mn><mo>&#183;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mi>P</mi><mi>R</mi><mi>sin</mi><mi>&#952;</mi><mo>&#183;</mo><mi>P</mi><mi>R</mi><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mi>P</mi><mi>Q</mi><mi>R</mi><mo>=</mo><mn>2</mn><mo>&#183;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>(</mo><mi>P</mi><mi>R</mi><msup><mo>)</mo><mn>2</mn></msup><mi>sin</mi><mi>&#952;</mi><mo>&#160;</mo><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mi>P</mi><mi>Q</mi><mi>R</mi><mo>=</mo><mn>105</mn><mo>&#183;</mo><mfrac><mn>6</mn><msqrt><mn>630</mn></msqrt></mfrac><mo>&#183;</mo><mfrac><msqrt><mn>594</mn></msqrt><msqrt><mn>630</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mi>P</mi><mi>Q</mi><mi>R</mi><mo>=</mo><msqrt><mn>594</mn></msqrt></math></p><p>Hence, area of the square will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>594</mn></math></p></blockquote>

</details>

---

### Q115. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>One vertex of a rectangular parallelopiped is at the origin <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> and the lengths of its edges along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo mathvariant="italic">,</mo><mo mathvariant="italic">&#160;</mo><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> axes are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> units respectively. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be the vertex <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>)</mo><mo>.</mo></math> Then the shortest distance between the diagonal <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>P</mi></math> and an edge parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> axis, not passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>12</mn><msqrt><mn>5</mn></msqrt></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><msqrt><mn>5</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>12</mn><mrow><mn>5</mn><msqrt><mn>5</mn></msqrt></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>12</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>12</mn><mn>5</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>One vertex of a rectangular parallelopiped is at the origin <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> and the lengths of its edges along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo mathvariant="italic">,</mo><mo mathvariant="italic">&#160;</mo><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> axes are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> units respectively,</p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be the vertex <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>)</mo></math>,</p><p>Now plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3e426258-f693-4be4-b3c4-590874194337-image.png" style="width: 320px; height: 226px;" /></p><p>Now equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>P</mi><mo>:</mo><mfrac><mi>x</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>4</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>5</mn></mfrac></math></p><p>And equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>0</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac></math></p><p>Now finding, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>n</mi><mn>1</mn></msub><mo mathvariant="italic">&#8594;</mo></mover><mo mathvariant="italic">&#215;</mo><mover><msub><mi>n</mi><mn>2</mn></msub><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><msub><mi>n</mi><mn>1</mn></msub><mo mathvariant="italic">&#8594;</mo></mover><mo mathvariant="italic">&#215;</mo><mover><msub><mi>n</mi><mn>2</mn></msub><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mfenced><mn>4</mn></mfenced><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mfenced><mn>3</mn></mfenced><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mfenced><mn>0</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><msub><mi>n</mi><mn>1</mn></msub><mo mathvariant="italic">&#8594;</mo></mover><mo mathvariant="italic">&#215;</mo><mover><msub><mi>n</mi><mn>2</mn></msub><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mn>4</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></math></p><p>Now we know that,</p><p>Shortest Distance, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mover><msub><mi>a</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>-</mo><mover><msub><mi>a</mi><mn>1</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><msub><mi>n</mi><mn>1</mn></msub><mo mathvariant="italic">&#8594;</mo></mover><mo mathvariant="italic">&#215;</mo><mover><msub><mi>n</mi><mn>2</mn></msub><mo mathvariant="italic">&#8594;</mo></mover></mrow></mfenced></mrow><mfenced open="|" close="|"><mrow><mover><msub><mi>n</mi><mn>1</mn></msub><mo mathvariant="italic">&#8594;</mo></mover><mo mathvariant="italic">&#215;</mo><mover><msub><mi>n</mi><mn>2</mn></msub><mo mathvariant="italic">&#8594;</mo></mover></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>-</mo><mn>0</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>4</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>4</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>=</mo><mfrac><mn>12</mn><mn>5</mn></mfrac></math></p></blockquote>

</details>

---

### Q116. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>4</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>5</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>5</mn></mrow></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p>Shortest distance between two lines</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow><msub><mi>a</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow><msub><mi>b</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub></mrow><msub><mi>c</mi><mn>1</mn></msub></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow><msub><mi>a</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow><msub><mi>b</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><msub><mi>z</mi><mn>2</mn></msub></mrow><msub><mi>c</mi><mn>2</mn></msub></mfrac></math> is given as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced open="|" close="|"><mtable><mtr><mtd><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mtd><mtd><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mtd><mtd><msub><mi>z</mi><mn>1</mn></msub><mo>-</mo><msub><mi>z</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced><msqrt><msup><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><msub><mi>b</mi><mn>2</mn></msub><mo>-</mo><msub><mi>a</mi><mn>2</mn></msub><msub><mi>b</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msub><mi>b</mi><mn>1</mn></msub><msub><mi>c</mi><mn>2</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub><msub><mi>c</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msub><mi>c</mi><mn>1</mn></msub><msub><mi>a</mi><mn>2</mn></msub><mo>-</mo><msub><mi>c</mi><mn>2</mn></msub><msub><mi>a</mi><mn>1</mn></msub></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mn>5</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>&#160;</mo><mn>2</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>5</mn></mrow></mfenced><mo>&#160;</mo></mtd><mtd><mn>4</mn><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr></mtable></mfenced><msqrt><msup><mfenced><mrow><mn>4</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>10</mn><mo>+</mo><mn>12</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>3</mn><mo>+</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mn>8</mn></mtd><mtd><mn>7</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr></mtable></mfenced><msqrt><msup><mfenced><mn>2</mn></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>2</mn></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>2</mn></mfenced><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced close="|" open="|"><mrow><mn>8</mn><mfenced><mrow><mo>-</mo><mn>10</mn><mo>+</mo><mn>12</mn></mrow></mfenced><mo>-</mo><mn>7</mn><mfenced><mrow><mo>-</mo><mn>5</mn><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><mn>4</mn><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><msqrt><mn>4</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>16</mn><mo>+</mo><mn>14</mn><mo>+</mo><mn>6</mn></mrow><msqrt><mn>12</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>36</mn><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>18</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>=</mo><mn>6</mn><msqrt><mn>3</mn></msqrt></math></p>

</details>

---

### Q117. JEE Main 2023 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>1</mn></mfrac></math> intersect the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>16</mn></math> at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>. Let the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> be the foot of perpendicular from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math> on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is the area of triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mi>R</mi></math>. then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **180**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mi>&#955;</mi></math></p><p>Any point on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfenced></math></p><p>It lies on plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>16</mn></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>&#955;</mi><mo>+</mo><mn>10</mn><mo>=</mo><mn>16</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>P</mi><mo>&#8801;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mfenced><mrow><mn>2</mn><mi>&#956;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mo>-</mo><mi>&#956;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>&#956;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfenced></math></p><p>Direction ratios of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mi>R</mi></math> is</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="&#60;" close="&#62;"><mrow><mn>2</mn><mi>&#956;</mi><mo>,</mo><mo>-</mo><mi>&#956;</mi><mo>,</mo><mi>&#956;</mi><mo>+</mo><mn>6</mn></mrow></mfenced></math></p><p>Direction ratios of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="&#60;" close="&#62;"><mrow><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>.</p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mi>R</mi><mo>&#8869;</mo><mi>L</mi></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#956;</mi><mo>+</mo><mi>&#956;</mi><mo>+</mo><mi>&#956;</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>&#8801;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/725bd237-8b9e-4f5e-8d8b-861bb31d61b4-9896285.png" style="width: 300px; height: 224px;" /></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>Q</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover><mo>&#160;</mo><mspace linebreak="newline"/><mover><mrow><mi>Q</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>Q</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>Q</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>12</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>24</mn><mover><mi>j</mi><mo>^</mo></mover></math></p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><msqrt><mn>144</mn><mo>+</mo><mn>576</mn></msqrt><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>720</mn><mn>4</mn></mfrac><mo>=</mo><mn>180</mn></math></p>

</details>

---

### Q118. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mi>&#955;</mi></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mi>&#955;</mi></mrow><mn>1</mn></mfrac><mo>,</mo><mi>&#955;</mi><mo>&#8805;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">L</mi><mn>1</mn></msub><mo>:</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>4</mn><mo>-</mo><mi>z</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>6</mn></msqrt></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi><mo>)</mo></math> lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math>, then which of the following is NOT possible?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#947;</mi><mo>=</mo><mn>24</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#945;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#945;</mi><mo>-</mo><mi>&#947;</mi><mo>=</mo><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mn>2</mn><mi>&#947;</mi><mo>=</mo><mn>19</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#947;</mi><mo>=</mo><mn>24</mn></math>**

**Detailed Solution:**

<p>Given equations of lines are</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>:</mo><mo>&#160;</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mi>&#955;</mi></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mi>&#955;</mi></mrow><mn>1</mn></mfrac><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mo>&#160;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>4</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p>Here,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>b</mi><mn mathvariant="italic">1</mn></msub><mo mathvariant="italic">&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi>i</mi><mo mathvariant="italic">^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><msub><mi>b</mi><mn mathvariant="italic">1</mn></msub><mo mathvariant="italic">&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>a</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>-</mo><mover><msub><mi>a</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math> Shortest distance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>6</mn></msqrt></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msqrt><mn>6</mn></msqrt><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mo>-</mo><mn>6</mn><mo>-</mo><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>8</mn></mrow><msqrt><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>4</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>&#955;</mi><mo>+</mo><mn>3</mn><mo>|</mo><mo>=</mo><mn>12</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>9</mn><mo>,</mo><mo>-</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>k</mi><mo>+</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>=</mo><mi>k</mi><mo>-</mo><mi>&#955;</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#947;</mi><mo>=</mo><mn>5</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>13</mn><mo>,</mo><mo>&#160;</mo><mn>35</mn></math></p>

</details>

---

### Q119. JEE Main 2023 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let a line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> pass through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> and be parallel to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>=</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi></math>. If the distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>5</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>8</mn><mo>)</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>&#945;</mi><mn>2</mn></msup></math> is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **158**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>=</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi></math></p><p>Now direction ratio is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="italic">k</mi><mo mathvariant="italic">^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>4</mn><mover><mi mathvariant="italic">i</mi><mo mathvariant="italic">^</mo></mover><mo>-</mo><mn>4</mn><mover><mi mathvariant="italic">j</mi><mo mathvariant="italic">^</mo></mover><mo>-</mo><mn>4</mn><mover><mi mathvariant="italic">k</mi><mo mathvariant="italic">^</mo></mover></math></p><p>So, Equation of line will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>k</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>5</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>8</mn><mo>)</mo></math> and foot of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8869;</mo></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> on this line be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>&#8801;</mo><mo>(</mo><mi>k</mi><mo>+</mo><mn>2</mn><mo>,</mo><mo>-</mo><mi>k</mi><mo>+</mo><mn>3</mn><mo>,</mo><mo>-</mo><mi>k</mi><mo>+</mo><mn>1</mn><mo>)</mo></math></p><p>So, direction ratio of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mi>R</mi></math> will be (<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mi>k</mi><mo>,</mo><mo>-</mo><mi>k</mi><mo>-</mo><mn>7</mn></math>),</p><p>Now using the perpendicular condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>+</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mo>-</mo><mi>k</mi><mo>)</mo><mo>+</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mo>-</mo><mi>k</mi><mo>-</mo><mn>7</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mfrac><mn>13</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mn>17</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>474</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>158</mn></math></p>

</details>

---

### Q120. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub></math> passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and is perpendicular to the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>10</mn></math>. Then the shortest distance between the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub></math> and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>4</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>2</mn></mfrac></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<p>The line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub></math> passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>)</mo></math> and is perpendicular to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>10</mn></math> then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub><mo>:</mo><mo>&#160;</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>6</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac></math> </p><p>Let the shortest distance between <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub></math> and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>4</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>2</mn></mfrac></math> is S.D.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9f5a553f-9f3c-4925-8269-6927a3fb2edb-9895820.png" style="width: 300px; height: 218px;" /></p><p>S.D. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mrow><mi>M</mi><mi>N</mi></mrow><mo>&#8594;</mo></mover></mrow><mfenced open="|" close="|"><mover><mrow><mi>M</mi><mi>N</mi></mrow><mo>&#8594;</mo></mover></mfenced></mfrac></mfenced></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>10</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>M</mi><mi>N</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mover><mrow><mi>M</mi><mi>N</mi></mrow><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><mn>16</mn><mo>+</mo><mn>64</mn><mo>+</mo><mn>64</mn></msqrt><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mrow><mi>M</mi><mi>N</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>12</mn><mo>-</mo><mn>80</mn><mo>-</mo><mn>16</mn><mo>=</mo><mo>-</mo><mn>108</mn></math></p><p>So, shortest distance (S.D.) </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><mo>-</mo><mn>108</mn></mrow><mn>12</mn></mfrac></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mo>-</mo><mn>9</mn></mrow></mfenced><mo>=</mo><mn>9</mn></math> units</p>

</details>

---

### Q121. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>3</mn></mrow><mn>1</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>a</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>1</mn></mfrac></math> intersects at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>, then the distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> from the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>a</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>3</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mi>&#955;</mi></math></p><p>Point on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>&#8801;</mo><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>,</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn><mo>,</mo><mi>&#955;</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mi>a</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mi>&#956;</mi></math></p><p>Point on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>&#8801;</mo><mfenced><mrow><mn>2</mn><mi>&#956;</mi><mo>+</mo><mi>a</mi><mo>,</mo><mn>3</mn><mi>&#956;</mi><mo>-</mo><mn>2</mn><mo>,</mo><mi>&#956;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p>For finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>, we must have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>-</mo><mn>3</mn><mo>=</mo><mi>&#956;</mi><mo>+</mo><mn>3</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mi>&#956;</mi><mo>+</mo><mn>6</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>3</mn><mi>&#956;</mi><mo>-</mo><mn>2</mn><mo>&#8658;</mo><mn>2</mn><mi>&#955;</mi><mo>=</mo><mn>3</mn><mi>&#956;</mi><mo>-</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>22</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mn>16</mn></math></p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8801;</mo><mfenced><mrow><mn>23</mn><mo>,</mo><mn>46</mn><mo>,</mo><mn>19</mn></mrow></mfenced></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#956;</mi><mo>+</mo><mi>a</mi><mo>=</mo><mi>&#955;</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>32</mn><mo>+</mo><mi>a</mi><mo>=</mo><mn>22</mn><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p>Distance of point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>23</mn><mo>,</mo><mn>46</mn><mo>,</mo><mn>19</mn></mrow></mfenced></math> from the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>0</mn></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><mn>19</mn><mo>+</mo><mn>9</mn></mrow><msqrt><msup><mn>0</mn><mn>2</mn></msup><mo>+</mo><msup><mn>0</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt></mfrac></mfenced><mo>=</mo><mn>28</mn></math> units</p>

</details>

---

### Q122. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Shortest distance between the lines
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>8</mn></mrow><mrow><mo>-</mo><mn>7</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>4</mn></mrow><mn>5</mn></mfrac><mtext>&#160;and&#160;</mtext><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mtext>&#160;is&#160;</mtext></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p>Given lines are</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>8</mn></mrow><mrow><mo>-</mo><mn>7</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>4</mn></mrow><mn>5</mn></mfrac></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p>Corresponding vectors are:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>7</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>.</mo><mi>D</mi><mo>.</mo><mo>=</mo><mfrac><mrow><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>|</mo></mrow><mrow><mo>|</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>|</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>10</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>]</mo><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>10</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>7</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>-</mo><mo>(</mo><mo>-</mo><mn>10</mn><mo>)</mo><mo>(</mo><mo>-</mo><mn>6</mn><mo>-</mo><mn>10</mn><mo>)</mo><mo>+</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>(</mo><mn>2</mn><mo>+</mo><mn>14</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>-</mo><mn>160</mn><mo>-</mo><mn>32</mn><mo>=</mo><mo>-</mo><mn>192</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mo>[</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>]</mo><mo>|</mo><mo>=</mo><mn>192</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>7</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mfenced><mn>16</mn></mfenced><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mn>16</mn></mrow></mfenced><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mfenced><mn>16</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>16</mn><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>16</mn><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>.</mo><mi>D</mi><mo>.</mo><mo>=</mo><mfrac><mrow><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>|</mo></mrow><mrow><mo>|</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>|</mo></mrow></mfrac><mo>=</mo><mfrac><mn>192</mn><mrow><mn>16</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>12</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>=</mo><mn>4</mn><msqrt><mn>3</mn></msqrt></math></p>

</details>

---

### Q123. JEE Main 2023 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Let the co-ordinates of one vertex of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mn>0</mn><mo>,</mo><mn>2</mn><mo>,</mo><mi>&#945;</mi><mo>)</mo></math> and the other two vertices lie on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mi>&#945;</mi></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>+</mo><mn>4</mn></mrow><mn>3</mn></mfrac></math>. For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8484;</mi></math>, if the area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mo>&#160;</mo><mi>units</mi></math> and the line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math> has length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>21</mn></msqrt></math> units, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup></math> is equal to _______.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>Given,</p><p>The co-ordinates of one vertex of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mn>0</mn><mo>,</mo><mn>2</mn><mo>,</mo><mi>&#945;</mi><mo>)</mo></math> and the other two vertices lie on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mi>&#945;</mi></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>+</mo><mn>4</mn></mrow><mn>3</mn></mfrac></math></p><p>Now plotting the diagram we get,</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5852485c-e812-4825-ba42-7bbd4a508d66-9894843_re.PNG" style="width: 346px; height: 150px;" /></p><p>Now any point on the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mi>&#945;</mi></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">z</mi><mo>+</mo><mn>4</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mi>k</mi></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mi>k</mi><mo>-</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>k</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mi>k</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p>Now direction ratio of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi></math> is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mi>k</mi><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>k</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mi>k</mi><mo>-</mo><mn>4</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8801;</mo><mfenced><mrow><mn>5</mn><mi>k</mi><mo>-</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>k</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mi>k</mi><mo>-</mo><mn>4</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mfenced><mrow><mn>5</mn><mi>k</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><mn>3</mn><mi>k</mi><mo>-</mo><mn>4</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>19</mn><mi>k</mi><mo>-</mo><mn>4</mn><mi>&#945;</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Also given area, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>2</mn><msqrt><mn>21</mn></msqrt><mo>&#215;</mo><mi>A</mi><mi>D</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mi>D</mi><mo>=</mo><msqrt><mn>21</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>5</mn><mi>k</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>2</mn><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>3</mn><mi>k</mi><mo>-</mo><mn>4</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>19</mn><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>k</mi><mi>&#945;</mi><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>14</mn><mi>k</mi><mo>+</mo><mn>4</mn><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now on solving equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn></math>.</p>

</details>

---

### Q124. JEE Main 2023 (25 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

If the shortest distance between the line joining the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>, and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mn>0</mn></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn><msup><mi>&#945;</mi><mn>2</mn></msup></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

<p>Equation of line joining <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Also, vector equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>&#956;</mi><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mn>0</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced><mo>=</mo><msqrt><mn>14</mn></msqrt></math></p><p>Required shortest distance is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mfenced open="|" close="|"><mrow><mfenced><mrow><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mfenced open="|" close="|"><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><mfenced><mrow><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><msqrt><mn>14</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><mo>-</mo><mn>6</mn><mo>+</mo><mn>3</mn></mrow><msqrt><mn>14</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mn>3</mn><msqrt><mn>14</mn></msqrt></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>228</mn><mo>&#215;</mo><mfrac><mn>9</mn><mn>14</mn></mfrac><mo>=</mo><mn>18</mn></math>.</p>

</details>

---

### Q125. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The foot of perpendicular of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math>. Then. Which of the following is NOT correct?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow><mi>&#947;</mi></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>15</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac><mo>=</mo><mo>-</mo><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#946;</mi><mi>&#947;</mi></mfrac><mo>=</mo><mo>-</mo><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#947;</mi><mi>&#945;</mi></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#946;</mi><mi>&#947;</mi></mfrac><mo>=</mo><mo>-</mo><mn>5</mn></math>**

**Detailed Solution:**

<p>Given line is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>:</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>&#955;</mi></math> (let)</p><p> </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ac4c95fa-8542-43ee-8c87-cee9919b1f51-9894424.png" style="width: 400px; height: 229px;" /></p><p>Let foot of perpendicular is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>2</mn><mi mathvariant="normal">&#955;</mi><mo>-</mo><mn>1</mn><mo>,</mo><mn>5</mn><mi mathvariant="normal">&#955;</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>-</mo><mi mathvariant="normal">&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mfenced><mrow><mn>5</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>6</mn><mo>+</mo><mi>&#955;</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Direction ratio of line is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>&#8869;</mo><mi>L</mi></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mo>-</mo><mn>5</mn><mfenced><mrow><mn>5</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>6</mn><mo>+</mo><mi>&#955;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>25</mn><mi>&#955;</mi><mo>-</mo><mn>5</mn><mo>-</mo><mn>6</mn><mo>-</mo><mi>&#955;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>30</mn><mi>&#955;</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>,</mo><mn>5</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8801;</mo><mi>P</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></mrow></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#8658;</mo><mo>&#160;</mo><menclose notation="box"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></menclose></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>5</mn><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></mrow></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#8658;</mo><menclose notation="box"><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></menclose></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi><mo>=</mo><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>-</mo><mn>1</mn><mo>&#8658;</mo><mo>&#160;</mo><menclose notation="box"><mi>&#947;</mi><mo>=</mo><mo>-</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></menclose></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#946;</mi><mi>&#947;</mi></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>&#8800;</mo><mo>-</mo><mn>5</mn></math></p><p> </p>

</details>

---

### Q126. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>12</mn><mi>z</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>6</mn><mi>z</mi><mo>-</mo><mn>6</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Given,</p><p>Equation of the lines</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>12</mn><mi>z</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>6</mn><mi>z</mi><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></mfrac><mo>=</mo><mfrac><mi>z</mi><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>12</mn></mfrac></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mfrac><mn>1</mn><mn>6</mn></mfrac></mfrac></math></p><p>We know that, shortest distance between the lines is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mfenced open="|" close="|"><mrow><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow></mfenced></mfrac></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mover><mi>j</mi><mo>^</mo></mover><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow><mn>12</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mover><mi>k</mi><mo>^</mo></mover><mn>6</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfrac><mfenced><mrow><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow></mfenced><mfenced open="|" close="|"><mrow><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow></mfenced></mfrac></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>&#8801;</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>12</mn></mfrac></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mfrac><mn>1</mn><mn>6</mn></mfrac></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>&#8801;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>&#8801;</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><msqrt><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>6</mn><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><mo>-</mo><mn>14</mn></mrow><mn>7</mn></mfrac></mfenced><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q127. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Consider the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>3</mn></mfrac></math></p><p>A line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub></math> having direction ratios <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn></math>, intersects <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> at the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> respectively. Then the length of line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>6</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>6</mn></msqrt></math>**

**Detailed Solution:**

<p>Given,</p><p>The lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>3</mn></mfrac></math></p><p>Now any point on line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi>&#955;</mi><mo>+</mo><mn>3</mn><mo>,</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p>And any point on line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfenced><mrow><mi>&#956;</mi><mo>+</mo><mn>2</mn><mo>,</mo><mn>2</mn><mi>&#956;</mi><mo>+</mo><mn>2</mn><mo>,</mo><mn>3</mn><mi>&#956;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p>Now equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub></math> which passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mfenced><mrow><mi>&#956;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mfenced><mrow><mn>2</mn><mi>&#956;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mfenced><mrow><mn>3</mn><mi>&#956;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p>Now it also passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>, so we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>&#955;</mi><mo>-</mo><mn>2</mn><mi>&#956;</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>3</mn><mi>&#956;</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p>Now on solving above equations we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mi>&#956;</mi><mo>=</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>7</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>8</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Q</mi><mfenced><mrow><mn>5</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>12</mn></mrow></mfenced></math></p><p>So, the distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></math></p>

</details>

---

### Q128. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math> from the line passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> and parallel to a line with direction ratios <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>1</mn></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>6</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>14</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>14</mn></msqrt></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a9ce171a-9e43-413c-a1c7-3a1777f92b29-9894244.PNG" style="width: 180px; height: 128px;" /></p><p>The equation of line passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> and parallel to a line with direction ratios <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>1</mn></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>&#955;</mi></math></p><p>Now let any point on the line will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>3</mn><mo>,</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced></math></p><p>We know the direction ratios of the line joining the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><msub><mi>z</mi><mn>1</mn></msub></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><msub><mi>y</mi><mn>2</mn></msub><mo>,</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced></math> is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><msub><mi>z</mi><mn>2</mn></msub><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub></mrow></mfenced></math></p><p>Therefore, the direction ratios of line PM,</p><p>D.R of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>PM</mi><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>7</mn><mo>,</mo><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>PM</mi></math> is perpendicular to the line</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>3</mn><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>5</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi mathvariant="normal">M</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Now distance of point P from point M,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>PM</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>8</mn><mo>-</mo><mn>6</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>PM</mi><mo>=</mo><msqrt><mn>14</mn></msqrt></math></p>

</details>

---

### Q129. JEE Main 2023 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

If the shortest distance between the lines  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><msqrt><mn>6</mn></msqrt></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><msqrt><mn>6</mn></msqrt></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><msqrt><mn>6</mn></msqrt></mrow><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>&#955;</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow><mn>5</mn></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>, then sum of squares of all possible values(s) of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **384**

**Detailed Solution:**

<p>Given equations are</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>&#955;</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow><mn>5</mn></mfrac></math> is passing through a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#955;</mi><mo>,</mo><mn>2</mn><msqrt><mn>6</mn></msqrt><mo>,</mo><mn>3</mn><msqrt><mn>6</mn></msqrt></mrow></mfenced></math> and it&#39;s direction ratios are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></math>.</p><p>So, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><msqrt><mn>6</mn></msqrt><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><msqrt><mn>6</mn></msqrt><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><msqrt><mn>6</mn></msqrt></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><msqrt><mn>6</mn></msqrt></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><msqrt><mn>6</mn></msqrt></mrow><mn>4</mn></mfrac></math> is passing through a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><msqrt><mn>6</mn></msqrt><mo>,</mo><msqrt><mn>6</mn></msqrt><mo>,</mo><msqrt><mn>6</mn></msqrt></mrow></mfenced></math> and it&#39;s direction ratios are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mo>-</mo><msqrt><mn>6</mn></msqrt><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msqrt><mn>6</mn></msqrt><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msqrt><mn>6</mn></msqrt><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mfenced><mrow><mo>-</mo><msqrt><mn>6</mn></msqrt><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msqrt><mn>6</mn></msqrt><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msqrt><mn>6</mn></msqrt><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><msqrt><mn>6</mn></msqrt><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><msqrt><mn>6</mn></msqrt><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mo>-</mo><mfenced><mrow><msqrt><mn>6</mn></msqrt><mo>+</mo><mi>&#955;</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><msqrt><mn>6</mn></msqrt><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><msqrt><mn>6</mn></msqrt><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced><mo>=</mo><msqrt><mn>6</mn></msqrt></math></p><p>We know that the shortest distance between two skew lines is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="|" open="|"><mrow><mfenced><mrow><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mfenced close="|" open="|"><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mfrac><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mfrac><mrow><mfenced><mrow><mfenced><mrow><mo>-</mo><msqrt><mn>6</mn></msqrt><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><msqrt><mn>6</mn></msqrt><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><msqrt><mn>6</mn></msqrt><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><msqrt><mn>6</mn></msqrt></mfrac></mfenced><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mfrac><mrow><mn>4</mn><msqrt><mn>6</mn></msqrt><mo>-</mo><mi>&#955;</mi></mrow><msqrt><mn>6</mn></msqrt></mfrac></mfenced><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>10</mn><msqrt><mn>6</mn></msqrt><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></math></p><p>So, required sum is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>10</mn><msqrt><mn>6</mn></msqrt><mo>-</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>384</mn></math></p>

</details>

---

### Q130. JEE Main 2023 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

The shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>8</mn></mrow><mn>0</mn></mfrac></math> is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<p>Given equations are</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mn>2</mn></mfrac></math> is passing through a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math> and it&#39;s direction ratios are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn></math>.</p><p>So, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>8</mn></mrow><mn>0</mn></mfrac></math> is passing through a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>6</mn><mo>,</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>8</mn></mrow></mfenced></math> and it&#39;s direction ratios are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>14</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced><mo>=</mo><msqrt><mn>16</mn><mo>+</mo><mn>36</mn><mo>+</mo><mn>144</mn></msqrt><mo>=</mo><mn>14</mn></math></p><p>We know that the shortest distance between two skew lines is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="|" open="|"><mrow><mfenced><mrow><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mfenced close="|" open="|"><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><mfenced><mrow><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>14</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><mn>14</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced open="|" close="|"><mrow><mn>16</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>168</mn></mrow></mfenced><mn>14</mn></mfrac><mo>=</mo><mn>14</mn></math> units</p>

</details>

---

### Q131. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the length of the perpendicular drawn from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mn>4</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mi>a</mi><mo>&#62;</mo><mn>0</mn></math> on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>6</mn></msqrt></math> units and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><msub><mi>&#945;</mi><mn>1</mn></msub><mo>,</mo><msub><mi>&#945;</mi><mn>2</mn></msub><mo>,</mo><msub><mi>&#945;</mi><mn>3</mn></msub></mrow></mfenced></math> is the image of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> in this line, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>3</mn></munderover><msub><mi>&#945;</mi><mi>i</mi></msub></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<blockquote><p>Let a point on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>&#955;</mi></math> be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>3</mn><mo>,</mo><mo>-</mo><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>and the DR&#39;s of the line are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="&#62;" open="&#60;"><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/413a0384-dfd5-4368-a4b0-dfbbfd7eaf81-image.png" style="width: 240px; height: 150px;" /></p><p>The DR&#39;s of line joining the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>3</mn><mo>,</mo><mo>-</mo><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mn>4</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="&#62;" open="&#60;"><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>-</mo><mi>a</mi><mo>,</mo><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Now its perpendicular to the given line, so<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mn>2</mn><mo>+</mo><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn><mo>+</mo><mfenced><mrow><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn><mo>-</mo><mn>2</mn><mi mathvariant="normal">a</mi><mo>+</mo><mn>9</mn><mi>&#955;</mi><mo>-</mo><mn>3</mn><mo>+</mo><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>14</mn><mi>&#955;</mi><mo>-</mo><mn>4</mn><mo>-</mo><mn>2</mn><mi mathvariant="normal">a</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn><mo>-</mo><mi>a</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>7</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn><mo>=</mo><mi>a</mi></math></p><p>and,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>5</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>35</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>14</mn><mi>&#955;</mi><mo>-</mo><mn>21</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>35</mn><mi>&#955;</mi><mo>+</mo><mn>21</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>For, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>1</mn><mo>;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mn>5</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>&#8801;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><msub><mi>&#945;</mi><mn>1</mn></msub><mo>,</mo><msub><mi>&#945;</mi><mn>2</mn></msub><mo>,</mo><msub><mi>&#945;</mi><mn>3</mn></msub></mrow></mfenced></math> is the image of point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mfrac><mrow><msub><mi>&#945;</mi><mn>1</mn></msub><mo>+</mo><mn>5</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>1</mn><mo>;</mo></mtd><mtd><mfrac><mrow><msub><mi>&#945;</mi><mn>2</mn></msub><mo>+</mo><mn>4</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>6</mn><mo>;</mo></mtd><mtd><mfrac><mrow><msub><mi>&#945;</mi><mn>3</mn></msub><mo>+</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>0</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtable><mtr><mtd><msub><mi>&#945;</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mn>3</mn><mo>;</mo></mtd><mtd><msub><mi>&#945;</mi><mn>2</mn></msub><mo>=</mo><mn>8</mn><mo>;</mo></mtd><mtd><msub><mi>&#945;</mi><mn>3</mn></msub><mo>=</mo><mo>-</mo><mn>2</mn></mtd></mtr></mtable></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><msub><mi>&#945;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#945;</mi><mn>2</mn></msub><mo>+</mo><msub><mi>&#945;</mi><mn>3</mn></msub><mo>=</mo><mn>8</mn></math></p></blockquote>

</details>

---

### Q132. JEE Main 2022 (26 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be two points on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math> at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>26</mn></msqrt></math> from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math>. Then the square of the area of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mi>R</mi></math> is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **153**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>:</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p>Plotting the diagram of given value&#39;s in question we have,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/54c5de49-51e0-4cef-ae42-427552030d55-image.png" style="width: 311px; height: 200px;" /></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> be any point on line whose coordinates are  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mfenced><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn><mi>t</mi><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>T</mi><mo>&#8869;</mo><mi>Q</mi><mi>R</mi></math> by diagram,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><mn>3</mn><mi>t</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>17</mn><mi>t</mi><mo>=</mo><mn>34</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>2</mn></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math></p><p>Now the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>P</mi><mi>T</mi></mrow></mfenced><mo>=</mo><msqrt><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn></msqrt><mo>=</mo><mn>3</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>Q</mi><mi>T</mi></mrow></mfenced><mo>=</mo><msqrt><mn>26</mn><mo>-</mo><mn>9</mn></msqrt><mo>=</mo><msqrt><mn>17</mn></msqrt></math> {by using pythagorus theorem}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>P</mi><mi>Q</mi><mi>R</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>2</mn><msqrt><mn>17</mn></msqrt><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>3</mn><msqrt><mn>17</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Square of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>ar</mo><mfenced><mrow><mo>&#8710;</mo><mi>P</mi><mi>Q</mi><mi>R</mi></mrow></mfenced><mo>=</mo><mn>153</mn><mo>.</mo></math></p></blockquote>

</details>

---

### Q133. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The length of the perpendicular from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> on the line passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> and parallel to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>=</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>-</mo><mn>5</mn></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>21</mn><mn>2</mn></mfrac></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>9</mn><mn>2</mn></mfrac></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>73</mn><mn>2</mn></mfrac></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>21</mn><mn>2</mn></mfrac></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given line is parallel to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>=</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>-</mo><mn>5</mn></math> is:</p><p>So, direction ratio of the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So, equation of line passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>&#955;</mi><mo>,</mo><mn>2</mn><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>,</mo><mn>4</mn><mo>-</mo><mn>3</mn><mi>&#955;</mi></mrow></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover></math> and line are perpendicular,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>4</mn><mo>-</mo><mn>4</mn><mi>&#955;</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>&#955;</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>-</mo><mn>16</mn><mo>+</mo><mn>16</mn><mi>&#955;</mi><mo>+</mo><mn>3</mn><mo>+</mo><mn>9</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mn>13</mn><mn>26</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>&#8801;</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>2</mn><mo>,</mo><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>P</mi><mi>Q</mi></mrow></mfenced><mo>=</mo><msqrt><mfrac><mn>21</mn><mn>2</mn></mfrac></msqrt></math></p></blockquote>

</details>

---

### Q134. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>7</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>6</mn></mrow><mn>7</mn></mfrac><mo>=</mo><mi>z</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>7</mn><mo>-</mo><mi>x</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mi>y</mi><mo>-</mo><mn>2</mn><mo>=</mo><mi>z</mi><mo>-</mo><mn>6</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>29</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>37</mn><mn>29</mn></mfrac></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>29</mn></msqrt><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>29</mn></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>7</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>6</mn></mrow><mn>7</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>0</mn></mrow><mn>1</mn></mfrac></math></p><p>Let any point on it is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mfenced><mrow><mo>-</mo><mn>7</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> is parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mfenced><mrow><mo>-</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Also given line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>7</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mn>1</mn></mfrac></math></p><p>Let any point on it be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mfenced><mrow><mn>7</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> is parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mn>7</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now shortest distance between <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><msub><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msub><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><msub><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mfrac></mfenced><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><mo>-</mo><mn>14</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><msqrt><mn>9</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>16</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msqrt><mn>29</mn></msqrt></math></p></blockquote>

</details>

---

### Q135. JEE Main 2022 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

The line of shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>5</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac></math> makes an angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mfrac><mn>2</mn><mn>27</mn></mfrac></msqrt></mfenced></math> with the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>:</mo><mi>a</mi><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math>. If the image of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>5</mn></mrow></mfenced></math> in the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>-</mo><mi>&#947;</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<blockquote><p>Given lines, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>5</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac></math></p><p>Now direction ratio of line of shortest distance will be, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now given angle between line and plane is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mfrac><mn>2</mn><mn>27</mn></mfrac></msqrt><mo>=</mo><mi>&#945;</mi></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#945;</mi><mo>=</mo><msqrt><mfrac><mn>2</mn><mn>27</mn></mfrac></msqrt></math></p><p>Now direction ratio of normal to plane is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#945;</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mo>-</mo><mi>a</mi><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn></mrow><mrow><msqrt><mn>4</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>1</mn></msqrt><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></mfenced><mo>=</mo><mfrac><msqrt><mn>2</mn></msqrt><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>3</mn></msqrt><mfenced close="|" open="|"><mi>a</mi></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mfenced><mrow><mtext>as</mtext><mo>&#160;</mo><mi>a</mi><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mtext>given</mtext></mrow></mfenced></math></p><p>Now equation of plane will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn></math> and image of point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>5</mn></mrow></mfenced></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>5</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn><mfrac><mfenced><mrow><mn>2</mn><mo>-</mo><mn>1</mn><mo>+</mo><mn>5</mn></mrow></mfenced><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>5</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>-</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>3</mn></math></p><p> </p><p>Note: This question was bonus in JEE mains 25th july 2022 paper, we have done some modification to the original question.</p></blockquote>

</details>

---

### Q136. JEE Main 2022 (28 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the image of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> in the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>. let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math> be a point that divides internally the line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>3</mn></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **125**

**Detailed Solution:**

<p>Plotting the rough graph of the given data we have,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c4747631-1cec-4028-864b-038fabb26451-image.png" style="width: 258px; height: 173px;" /></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> be the mid-point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>M</mi><mo>=</mo><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>6</mn><mo>,</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>,</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>M</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mover><mrow><mi>P</mi><mi>M</mi></mrow><mo>&#8594;</mo></mover><mo>&#8869;</mo><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>3</mn><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mn>11</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>M</mi><mfenced><mrow><mfrac><mn>51</mn><mn>11</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>11</mn></mfrac><mo>,</mo><mfrac><mn>7</mn><mn>11</mn></mfrac></mrow></mfenced></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is mid-point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>M</mi></math></p><p>So by using midpoint formula in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>M</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced><mrow><mfrac><mn>62</mn><mn>22</mn></mfrac><mo>,</mo><mfrac><mn>23</mn><mn>22</mn></mfrac><mo>,</mo><mfrac><mn>40</mn><mn>22</mn></mfrac></mrow></mfenced></math>, now comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mn>62</mn><mn>22</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>23</mn><mn>22</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#947;</mi><mo>=</mo><mfrac><mn>40</mn><mn>22</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mo>=</mo><mn>125</mn></math></p>

</details>

---

### Q137. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>6</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>3</mn></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>18</mn><msqrt><mn>5</mn></msqrt></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>22</mn><mrow><mn>3</mn><msqrt><mn>5</mn></msqrt></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>46</mn><mrow><mn>3</mn><msqrt><mn>5</mn></msqrt></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>18</mn><msqrt><mn>5</mn></msqrt></mfrac></math>**

**Detailed Solution:**

<p>Given equation of lines<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></math> &amp; </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>6</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>3</mn></mfrac></math></p><p>Now let the point be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> on first line</p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> on second line, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>B</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>6</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And direction ratio&#39;s be <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>n</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> &amp;</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>n</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>n</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>n</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>We know that shortest Distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced open="[" close="]"><mtable><mtr><mtd><mover><mrow><mi>B</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover></mtd><mtd><mover><msub><mi>n</mi><mn>1</mn></msub><mo>&#8594;</mo></mover></mtd><mtd><mover><msub><mi>n</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mtd></mtr></mtable></mfenced><mfenced open="|" close="|"><mrow><mover><msub><mi>n</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>n</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"/><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mover><mrow><mi>B</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover></mtd><mtd><mover><msub><mi>n</mi><mn>1</mn></msub><mo>&#8594;</mo></mover></mtd><mtd><mover><msub><mi>n</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mrow><mn>6</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mfenced><mrow><mn>10</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>60</mn><mo>+</mo><mn>32</mn><mo>+</mo><mn>16</mn><mo>=</mo><mn>108</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><msub><mi>n</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>n</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><msqrt><mn>100</mn><mo>+</mo><mn>64</mn><mo>+</mo><mn>16</mn></msqrt><mo>=</mo><msqrt><mn>180</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>.</mo><mi>D</mi><mo>=</mo><mfrac><mn>108</mn><msqrt><mn>180</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>108</mn><mrow><mn>6</mn><msqrt><mn>5</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>18</mn><msqrt><mn>5</mn></msqrt></mfrac></math></p>

</details>

---

### Q138. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the foot of the perpendicular from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mn>3</mn></mfrac></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>. Then the distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> from the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>12</mn><mi>z</mi><mo>+</mo><mn>23</mn><mo>=</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>50</mn><mn>13</mn></mfrac></math>
- **(B)** $\frac{63}{13}$
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>65</mn><mn>13</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>65</mn><mn>13</mn></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be foot of perpendicular of point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e43ce106-1a79-4ddc-94b6-744ecb36798f-image.png" style="width: 330px; height: 123px;" /></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mi>&#955;</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi>z</mi><mo>=</mo><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></math></p><p>Then coordinates of point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>,</mo><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Now direction ratios of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mi>P</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="&#62;" open="&#60;"><mrow><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="&#62;" open="&#60;"><mrow><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>3</mn><mo>,</mo><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p>and D.R&#39;s of line will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="&#62;" open="&#60;"><mrow><mn>4</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> and line are perpendicular</p><p>so, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><mrow><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>&#955;</mi><mo>=</mo><mn>1</mn></math></p><p>Putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8801;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Now distance of point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> from plane<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>12</mn><mi>z</mi><mo>+</mo><mn>23</mn><mo>=</mo><mn>0</mn></math> will be  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>12</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>23</mn></mrow><msqrt><mn>9</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>144</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mn>65</mn><mn>13</mn></mfrac></math></p>

</details>

---

### Q139. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the two lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>,</mo><mi>z</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn></mrow><mi>&#945;</mi></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>5</mn></mrow><mn>2</mn></mfrac></math> are perpendicular, then an angle between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>3</mn></msub><mo>:</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>4</mn></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>29</mn><mn>4</mn></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>29</mn><mn>4</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>2</mn><mn>29</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>2</mn><msqrt><mn>29</mn></msqrt></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>29</mn><mn>4</mn></mfrac></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mn>0</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mrow><mstyle displaystyle="true"><mfrac><mi>&#945;</mi><mn>2</mn></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>5</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>3</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>0</mn></mrow><mn>4</mn></mfrac></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="|" open="|"><mrow><mn>3</mn><mo>-</mo><mi>&#945;</mi><mo>+</mo><mn>0</mn></mrow></mfenced><mrow><msqrt><mn>13</mn></msqrt><msqrt><mn>1</mn><mo>+</mo><mfrac><msup><mi>&#945;</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>4</mn></msqrt></mrow></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>3</mn></math></p><p>Now for angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>3</mn></msub></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mfenced open="|" close="|"><mrow><mn>1</mn><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>)</mo><mfenced><mstyle displaystyle="true"><mfrac><mi>&#945;</mi><mn>2</mn></mfrac></mstyle></mfenced><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn></mrow></mfenced><mrow><msqrt><mn>1</mn><mo>+</mo><mfrac><msup><mi>&#945;</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>4</mn></msqrt><msqrt><mn>9</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>16</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mfenced close="|" open="|"><mrow><mo>-</mo><mn>3</mn><mo>-</mo><mi>&#945;</mi><mo>+</mo><mn>8</mn></mrow></mfenced><mrow><msqrt><mn>5</mn><mo>+</mo><mfrac><msup><mi>&#945;</mi><mn>2</mn></msup><mn>4</mn></mfrac></msqrt><msqrt><mn>29</mn></msqrt></mrow></mfrac></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>2</mn><mrow><msqrt><mfrac><mn>29</mn><mn>4</mn></mfrac></msqrt><msqrt><mn>29</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>29</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>4</mn><mn>29</mn></mfrac></mfenced><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>29</mn><mn>4</mn></mfrac></mfenced></math></p>

</details>

---

### Q140. JEE Main 2022 (25 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub></math> be the line in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi></math>-plane with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> intercepts <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math> respectively, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub></math> be the line in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mi>x</mi></math>-plane with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> intercepts <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mrow><mn>6</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> is the shortest distance between the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>d</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **51**

**Detailed Solution:**

<p>Given,</p><p>Line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow><mfrac><mn>1</mn><mn>8</mn></mfrac></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>0</mn></mfrac></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>0</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow><mrow><mo>-</mo><mn>6</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>0</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>8</mn></mfrac></math></p><p>Shortest distance between two lines is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>d</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>d</mi><mo>&#8594;</mo></mover></mrow></mfenced></mfrac></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mover><mi>i</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><msqrt><mn>6</mn></msqrt><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><msqrt><msup><mfenced><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>3</mn><msqrt><mn>6</mn></msqrt></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msqrt><mn>2</mn></msqrt><msqrt><mn>32</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>54</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>51</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>d</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>=</mo><mn>51</mn></math></p>

</details>

---

### Q141. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mi>&#955;</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>5</mn></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math>, then the sum of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>**

**Detailed Solution:**

<p>We know that, shortest distance between two line is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced open="|" close="|"><mrow><mfenced><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msub><mi>b</mi><mn>1</mn></msub><mo>&#215;</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mfenced open="|" close="|"><mrow><msub><mi>b</mi><mn>1</mn></msub><mo>&#215;</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfenced></mfrac></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So, S.D. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced close="|" open="|"><mrow><mfenced><mrow><mfenced><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>4</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>5</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mfenced close="|" open="|"><mrow><msub><mi>b</mi><mn>1</mn></msub><mo>&#215;</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfenced></mfrac></math></p><p>Calculating <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mfenced><mrow><mn>15</mn><mo>-</mo><mn>4</mn><mi>&#955;</mi></mrow></mfenced><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mfenced><mn>5</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>15</mn><mo>-</mo><mn>4</mn><mi>&#955;</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced><mo>=</mo><msqrt><msup><mfenced><mrow><mn>15</mn><mo>-</mo><mn>4</mn><mi>&#955;</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>25</mn></msqrt></math></p><p>Now again, </p><p>S.D. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced close="|" open="|"><mrow><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mn>15</mn><mo>-</mo><mn>4</mn><mi>&#955;</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mi>k</mi></mrow></mfenced></mrow></mfenced><msqrt><msup><mfenced><mrow><mn>15</mn><mo>-</mo><mn>4</mn><mi>&#955;</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>25</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="|" open="|"><mrow><mn>15</mn><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>20</mn><mo>+</mo><mn>10</mn></mrow></mfenced><msqrt><msup><mfenced><mrow><mn>15</mn><mo>-</mo><mn>4</mn><mi>&#955;</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>25</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p>squaring both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mfenced><mrow><mn>5</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>225</mn><mo>+</mo><mn>16</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>120</mn><mi>&#955;</mi><mo>+</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>100</mn><mo>-</mo><mn>20</mn><mi>&#955;</mi><mo>+</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>75</mn><mo>-</mo><mn>60</mn><mi>&#955;</mi><mo>=</mo><mn>17</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>140</mn><mi>&#955;</mi><mo>+</mo><mn>350</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>80</mn><mi>&#955;</mi><mo>+</mo><mn>275</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>16</mn><mi>&#955;</mi><mo>+</mo><mn>55</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>11</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>5</mn><mo>,</mo><mn>11</mn></math></p><p>So sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mn>11</mn><mo>=</mo><mn>16</mn></math></p>

</details>

---

### Q142. JEE Main 2022 (24 Jun Shift 1)

*Type:* `numerical` | *Level:* `1`

If the shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mi mathvariant="normal">a</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>&#956;</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>2</mn><mn>3</mn></mfrac></msqrt></math>, then the integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is equal to _____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>D.R. &#39;s of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>D.R. &#39;s of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>D.R. &#39;s of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mi mathvariant="normal">a</mi><mo>,</mo><mn>0</mn></mrow></mfenced></math> </p><p>D.R. &#39;s of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> </p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi mathvariant="italic">i</mi><mo mathvariant="italic">^</mo></mover></mtd><mtd><mover><mi mathvariant="italic">j</mi><mo mathvariant="italic">^</mo></mover></mtd><mtd><mover><mi mathvariant="italic">k</mi><mo mathvariant="italic">^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi mathvariant="normal">a</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><mover><msub><mi mathvariant="normal">b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><msub><mi mathvariant="normal">b</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi mathvariant="normal">b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msqrt></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mover accent="true"><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>-</mo><msub><mover accent="true"><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msub><mover accent="true"><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover accent="true"><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>2</mn><mo>-</mo><mn>2</mn><mi>a</mi></math></p><p>Shortest distance between the lines, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced></mrow><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><msqrt><mfrac><mn>2</mn><mn>3</mn></mfrac></msqrt></math></p><p>Squaring on both the sides, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mi>a</mi><mo>+</mo><mn>1</mn></math></p><p> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q143. JEE Main 2022 (24 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

Let a line having direction ratios <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>-</mo><mn>4</mn><mo>,</mo><mn>2</mn></math> intersect the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>7</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>2</mn></mrow><mn>1</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>7</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac></math> at the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mi>B</mi></mrow></mfenced><mn>2</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **84**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>7</mn><mo>,</mo><mo>-</mo><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi>&#955;</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>&#956;</mi><mo>,</mo><mn>3</mn><mi>&#956;</mi><mo>+</mo><mn>7</mn><mo>,</mo><mi>&#956;</mi></mrow></mfenced></math></p><p>DR&#39;s of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn><mi>&#956;</mi><mo>+</mo><mn>7</mn><mo>,</mo><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>3</mn><mi>&#956;</mi><mo>-</mo><mn>6</mn><mo>,</mo><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p>Now, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn><mi>&#956;</mi><mo>+</mo><mn>7</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>3</mn><mi>&#956;</mi><mo>-</mo><mn>6</mn></mrow><mrow><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>12</mn><mi>&#955;</mi><mo>+</mo><mn>8</mn><mi>&#956;</mi><mo>-</mo><mn>28</mn><mo>=</mo><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>3</mn><mi>&#956;</mi><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mi>&#956;</mi><mo>-</mo><mn>2</mn></math></p><p>Also </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>6</mn><mi>&#956;</mi><mo>-</mo><mn>12</mn><mo>=</mo><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>+</mo><mn>4</mn><mi>&#956;</mi><mo>+</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>5</mn><mi>&#956;</mi><mo>+</mo><mn>10</mn></math></p><p>After solving above two equations, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>5</mn><mo>,</mo><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mn>8</mn><mo>,</mo><mn>6</mn><mo>,</mo><mo>-</mo><mn>7</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mn>6</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mi>B</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>+</mo><mn>64</mn><mo>+</mo><mn>16</mn><mo>=</mo><mn>84</mn></math></p>

</details>

---

### Q144. JEE Main 2021 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

The distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> from the point of intersection of the line joining the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>5</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>7</mn><mo>,</mo></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<p>We have, point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>Equation of line joining the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>5</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>4</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>5</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mi>r</mi></math></p><p>Any point on above line is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mi>r</mi><mo>+</mo><mn>3</mn><mo>,</mo><mi>r</mi><mo>-</mo><mn>4</mn><mo>,</mo><mn>6</mn><mi>r</mi><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p>Now, satisfying it in the given plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>7</mn><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mo>-</mo><mi>r</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>r</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>6</mn><mi>r</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>2</mn></math></p><p>So, required point of intersection is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>.</mo></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>T</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>4</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>4</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mn>7</mn><mo>.</mo></math></p>

</details>

---

### Q145. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For real numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo></math> if the point of intersection of the straight lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mi>&#946;</mi></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>6</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>7</mn></mrow><mn>3</mn></mfrac></math> lies on the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>8</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mi>&#946;</mi></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>6</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>7</mn></mrow><mn>3</mn></mfrac></math> lies on the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>8</mn></math>.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mo>&#8709;</mo></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mi>&#946;</mi></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>6</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>7</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mi>q</mi></math></p><p>Any point on the first line can be considered as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#981;</mi><mo>+</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>&#981;</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mi>&#981;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>and a point on the second line can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>q</mi><mi>&#946;</mi><mo>+</mo><mn>4</mn><mo>,</mo><mn>3</mn><mi>q</mi><mo>+</mo><mn>6</mn><mo>,</mo><mn>3</mn><mi>q</mi><mo>+</mo><mn>7</mn></mrow></mfenced><mo>.</mo></math></p><p>For intersection of the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>+</mo><mi>&#945;</mi><mo>=</mo><mi>q</mi><mi>&#946;</mi><mo>+</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#981;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>3</mn><mi>q</mi><mo>+</mo><mn>6</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>&#981;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>3</mn><mi>q</mi><mo>+</mo><mn>7</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>&#160;&#38;&#160;</mo><mfenced><mn>3</mn></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=1,</mo><mi>q</mi><mo>=-</mo><mn>1</mn></math></p><p>So, from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>3</mn></math></p><p>Now, point of intersection is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>It lies on the given plane, therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>-</mo><mn>4</mn><mo>=</mo><mn>8</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>5</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><mn>5</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>7</mn></math></p>

</details>

---

### Q146. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the shortest distance between the straight lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>6</mn><mo>(</mo><mi>y</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>2</mn><mo>(</mo><mi>z</mi><mo>-</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>2</mn><mo>(</mo><mi>y</mi><mo>-</mo><mi>&#955;</mi><mo>)</mo><mo>=</mo><mo>(</mo><mi>z</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>38</mn></msqrt></mfrac><mo>,</mo></math> then the integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>The given lines are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>6</mn><mo>(</mo><mi>y</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>2</mn><mo>(</mo><mi>z</mi><mo>-</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>2</mn><mo>(</mo><mi>y</mi><mo>-</mo><mi>&#955;</mi><mo>)</mo><mo>=</mo><mo>(</mo><mi>z</mi><mo>-</mo><mn>3</mn><mo>)</mo></math></p><p>And, they can be written as <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mo>(</mo><mi>y</mi><mo>-</mo><mn>2</mn><mo>)</mo></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mo>(</mo><mi>z</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>3</mn></mfrac></math> and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mi>&#955;</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>.</mo></math></p><p>The lines are in the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow><mi>l</mi></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow><mi>m</mi></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub></mrow><mi>n</mi></mfrac><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>1</mn></msub></mrow></mfenced></math> is a point on the line and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi></math> are the direction ratios of the vector parallel to the line.</p><p>Thus, the position vectors of the points on the line are respectively <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>a</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><msub><mi>a</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> and direction of the lines are along the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>r</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover><mo>.</mo></math></p><p>Thus, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><msub><mi>a</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>-</mo><mover><msub><mi>a</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover><mo>.</mo></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/92118926-8319-4e35-992a-a9444ed227e3-62559c28-4feb-45ed-b838-0ea6c4559a9c-image.png" style="width: 300px; height: 170px;" /></p><p>Shortest distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>r</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>r</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfenced><mfenced close="|" open="|"><mrow><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>r</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>r</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>r</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mfenced><mrow><mn>4</mn><mo>-</mo><mn>6</mn></mrow></mfenced><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mfenced><mrow><mn>8</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mfenced><mrow><mn>4</mn><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>r</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>r</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><msqrt><msup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>4</mn><mo>+</mo><mn>25</mn><mo>+</mo><mn>9</mn></msqrt><mo>=</mo><msqrt><mn>38</mn></msqrt></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#955;</mi><mo>-</mo><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>1</mn><mfenced><mrow><mn>4</mn><mo>-</mo><mn>6</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>8</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>4</mn><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi><mo>+</mo><mn>10</mn><mo>+</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>14</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi></mrow></mfenced></math></p><p>Given, the shortest distance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>38</mn></msqrt></mfrac><mo>,</mo></math> hence, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>38</mn></msqrt></mfrac><mo>=</mo><mfrac><mfenced close="|" open="|"><mrow><mn>14</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi></mrow></mfenced><msqrt><mn>38</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>14</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>14</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi><mo>=</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mn>13</mn><mn>5</mn></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Integral value is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>.</mo></math></p>

</details>

---

### Q147. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>a</mi><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mi>z</mi><mo>-</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mo>=</mo><mi>b</mi><mi>z</mi><mo>-</mo><mn>2</mn><mo>,</mo><mo>(</mo><mi>a</mi><mi>b</mi><mo>&#8800;</mo><mn>0</mn><mo>)</mo></math> are coplanar, if:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>a</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mo>{</mo><mn>0</mn><mo>}</mo></math>
- **(B)** <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mo>{</mo><mn>0</mn><mo>}</mo></math></p>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>a</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mo>{</mo><mn>0</mn><mo>}</mo></math>**

**Detailed Solution:**

<p>Given lines can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mi>a</mi></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>0</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mi>a</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>0</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>0</mn></mrow><mstyle displaystyle="true"><mfrac><mn>3</mn><mi>b</mi></mfrac></mstyle></mfrac></math></p><p>We know that lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow><msub><mi>a</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow><msub><mi>b</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub></mrow><msub><mi>c</mi><mn>1</mn></msub></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow><msub><mi>a</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow><msub><mi>b</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><msub><mi>z</mi><mn>2</mn></msub></mrow><msub><mi>c</mi><mn>2</mn></msub></mfrac></math> are coplanar if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mtd><mtd><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mtd><mtd><msub><mi>z</mi><mn>2</mn></msub><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math>.</p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mfrac><mn>3</mn><mi>b</mi></mfrac></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>&#8800;</mo><mn>0</mn><mo>&#8658;</mo><mi>a</mi><mo>&#8800;</mo><mn>0</mn></math>, since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>&#8800;</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfenced><mrow><mfrac><mn>3</mn><mrow><mo>&#160;</mo><mi>b</mi></mrow></mfrac><mo>-</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mi>a</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>-</mo><mfrac><mn>3</mn><mi>b</mi></mfrac><mo>-</mo><mi>a</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>b</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>a</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mn>0</mn></mfenced></math></p>

</details>

---

### Q148. JEE Main 2021 (20 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

If the shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>r</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>+</mo><mi>&#956;</mi><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi><mo>&#8712;</mo><mi>R</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to_____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>r</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>r</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>+</mo><mi>&#956;</mi><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>d</mi><mo>&#8594;</mo></mover></math>, then shortest distance between two lines is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mfenced open="|" close="|"><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover></mrow></mfenced></mfrac></math></p><p>Here,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>8</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>8</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>4</mn><mo>&#183;</mo><mn>3</mn></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>So, shortest distance is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mn>4</mn><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><mrow><mn>4</mn><mo>&#183;</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mn>4</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>27</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q149. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>If the foot of the perpendicular from point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>8</mn></mrow></mfenced></math> on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mi>a</mi></mrow><mi>l</mi></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mi>b</mi></mrow><mn>4</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>&#8800;</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo></math> then the shortest distance between the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>5</mn></mfrac></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>6</mn></msqrt></mfrac></math>
- **(C)** <p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>2</mn><mn>3</mn></mfrac></msqrt></math></p>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>6</mn></msqrt></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math> satisfy the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mo>-</mo><mi>a</mi></mrow><mi>&#8467;</mi></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn><mo>-</mo><mi>b</mi></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mo>-</mo><mi>a</mi></mrow><mi>&#8467;</mi></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfrac><mrow><mn>7</mn><mo>-</mo><mi>b</mi></mrow><mn>4</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>&#8467;</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mfenced open="&#60;" close="&#62;"><mrow><mn>4</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>-</mo><mfenced open="&#60;" close="&#62;"><mrow><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mfenced close="&#62;" open="&#60;"><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced close="&#62;" open="&#60;"><mrow><mi>&#8467;</mi><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#183;</mo><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#8467;</mi><mo>-</mo><mn>6</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#8467;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>&#8467;</mi><mo>=</mo><mn>3</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="&#62;" open="&#60;"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="&#62;" open="&#60;"><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="&#62;" open="&#60;"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p>Shortest distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mfenced open="|" close="|"><mrow><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow></mfenced></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>6</mn></msqrt></mfrac></math></p>

</details>

---

### Q150. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let the position vectors of two points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math>, respectively. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be two points such that the direction ratios of lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mi>S</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math>, respectively. Let lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mi>S</mi></math> intersect at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math>. If the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>T</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover></math> is perpendicular to both <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>Q</mi><mi>S</mi></mrow><mo>&#8594;</mo></mover></math> and the length of vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>T</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>5</mn></msqrt></math> units, then the modulus of a position vector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>482</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>171</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>5</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>227</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>171</mn></msqrt></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#8214;</mo><mo>&#160;</mo><mn>4</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>Q</mi><mi>S</mi></mrow><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#8214;</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p>Dr&#39;s of normal to the plane containing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>,</mo><mi>T</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> will be proportional to : </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>4</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7a89a7b3-39a0-4765-9643-1eefe6731e6e-image.png" style="width: 213px; height: 164px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfrac><mi>&#8467;</mi><mn>0</mn></mfrac><mo>=</mo><mfrac><mi>m</mi><mn>4</mn></mfrac><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac></math></p><p>For point, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> : <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>T</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>Q</mi><mi>T</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>4</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mi>&#956;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>&#8801;</mo><mfenced><mrow><mn>4</mn><mi>&#955;</mi><mo>+</mo><mn>3</mn><mo>,</mo><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>&#8801;</mo><mfenced><mrow><mn>2</mn><mi>&#956;</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi>&#956;</mi><mo>+</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>2</mn><mi>&#956;</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#955;</mi><mo>+</mo><mn>3</mn><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#956;</mi><mo>+</mo><mn>1</mn><mo>&#8658;</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn></math></p><p>So point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>:</mo><mfenced><mrow><mn>11</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi mathvariant="italic">O</mi><mi mathvariant="italic">A</mi></mrow><mo mathvariant="italic">&#8594;</mo></mover><mo mathvariant="italic">=</mo><mfenced><mrow><mn>11</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#177;</mo><mfenced><mfrac><mrow><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow><msqrt><mn>5</mn></msqrt></mfrac></mfenced><msqrt><mn>5</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>11</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#177;</mo><mfenced><mrow><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>11</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mrow><mi>O</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><mn>121</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>49</mn></msqrt><mo>=</mo><msqrt><mn>171</mn></msqrt></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>81</mn><mo>+</mo><mn>25</mn><mo>+</mo><mn>25</mn></msqrt><mo>=</mo><msqrt><mn>131</mn></msqrt></math></p>

</details>

---

### Q151. JEE Main 2021 (25 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>A line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> passing through origin is perpendicular to the lines</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub><mo>:</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>4</mn><mo>+</mo><mn>2</mn><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub><mo>:</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>s</mi></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>s</mi></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mi>s</mi></mrow></mfenced><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p>If the co-ordinates of the point in the first octant on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub></math> at a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>17</mn></msqrt></math> from the point of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced></math> is equal to ___ .</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **44**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub><mo>:</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>4</mn><mo>+</mo><mn>2</mn><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub><mo>:</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>s</mi></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>s</mi></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mi>s</mi></mrow></mfenced><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>DR</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub><mo>&#8801;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>DR</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub><mo>&#8801;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub><mo>&#215;</mo><msub><mi>l</mi><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>i</mi></mtd><mtd><mi>j</mi></mtd><mtd><mi>k</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mi>j</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mi>k</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><mi>i</mi><mo>+</mo><mn>3</mn><mi>j</mi><mo>-</mo><mn>2</mn><mi>k</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>DR</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> ( line <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8869;</mo></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>l</mi><mn>2</mn></msub></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>l</mi><mo>:</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#956;</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mi>&#956;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mi>&#956;</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p>for intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>l</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mi>t</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#956;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>t</mi><mo>=</mo><mn>3</mn><mi>&#956;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>+</mo><mn>2</mn><mi mathvariant="normal">t</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#956;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">t</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Point of intersection <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8801;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math></p><p>Let point on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>s</mi><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>+</mo><mn>2</mn><mi>s</mi><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>+</mo><mi>s</mi></mrow></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><msqrt><mn>17</mn></msqrt><mo>&#160;</mo><mo>&#8658;</mo><msup><mfenced><mrow><mi>P</mi><mi>Q</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>2</mn><mi>s</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>6</mn><mo>+</mo><mn>2</mn><mi>s</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mi>s</mi></mfenced><mn>2</mn></msup><mo>=</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><msup><mi>s</mi><mn>2</mn></msup><mo>+</mo><mn>28</mn><mi>s</mi><mo>+</mo><mn>20</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">s</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mfrac><mn>10</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi><mo>&#8800;</mo><mo>-</mo><mn>2</mn></math> as point lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mrow><mi>s</mi><mi>t</mi></mrow></msup></math> octant.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>a</mi><mo>=</mo><mn>3</mn><mo>+</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mfrac><mn>10</mn><mn>9</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>7</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>3</mn><mo>+</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mfrac><mn>10</mn><mn>9</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>7</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>2</mn><mo>+</mo><mfenced><mrow><mo>-</mo><mfrac><mn>10</mn><mn>9</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>8</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>18</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mn>18</mn><mfenced><mfrac><mn>22</mn><mn>9</mn></mfrac></mfenced><mo>=</mo><mn>44</mn></math></p>

</details>

---

### Q152. JEE Main 2021 (25 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The equation of the line through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and perpendicular to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mi>r</mi></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>P</mi><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mi>z</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn><mo>,</mo><mn>3</mn><mi>r</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>Q</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>&#8869;</mo><mfenced><mrow><mn>2</mn><mover><mi mathvariant="italic">i</mi><mo mathvariant="italic">^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="italic">j</mi><mo mathvariant="italic">^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="italic">k</mi><mo mathvariant="italic">^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>4</mn><mi>r</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>9</mn><mi>r</mi><mo>-</mo><mn>6</mn><mo>+</mo><mn>4</mn><mi>r</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>r</mi><mo>=</mo><mfrac><mn>2</mn><mn>17</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>P</mi><mfenced><mrow><mfrac><mn>21</mn><mn>17</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>11</mn></mrow><mn>17</mn></mfrac><mo>,</mo><mfrac><mn>13</mn><mn>17</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mover><mrow><mi mathvariant="italic">P</mi><mi mathvariant="italic">Q</mi></mrow><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mn>21</mn><mover><mi mathvariant="italic">i</mi><mo mathvariant="italic">^</mo></mover><mo>-</mo><mn>28</mn><mover><mi mathvariant="italic">j</mi><mo mathvariant="italic">^</mo></mover><mo>-</mo><mn>21</mn><mover><mi mathvariant="italic">k</mi><mo mathvariant="italic">^</mo></mover></mrow><mn>17</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi mathvariant="italic">Q</mi><mi mathvariant="italic">P</mi></mrow><mo mathvariant="italic">&#8594;</mo></mover><mo>:</mo><mfrac><mi>x</mi><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></math></p>

</details>

---

### Q153. JEE Main 2021 (24 Feb Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> be an integer. If the shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>2</mn><mi>z</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>&#955;</mi><mo>=</mo><mi>z</mi><mo>-</mo><mi>&#955;</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>7</mn></msqrt><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>&#955;</mi></mfenced></math> is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>&#955;</mi></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mfrac><mn>1</mn><mn>2</mn></mfrac></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>0</mn></mrow><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>0</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn><mi>&#955;</mi></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mi>&#955;</mi></mrow><mn>1</mn></mfrac></math></p><p>Shortest distance<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><mover><msub><mi>a</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>-</mo><mover><msub><mi>a</mi><mn>1</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><msub><mi>b</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><mover><msub><mi>b</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>b</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced><mrow><mover><msub><mi>b</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced><mfenced close="|" open="|"><mrow><mover><msub><mi>b</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow><msqrt><mn>14</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mover><msub><mi>a</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>-</mo><mover><msub><mi>a</mi><mn>1</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><msub><mi>b</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mfenced open="|" close="|"><mrow><mover><msub><mi>b</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><msub><mi>b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced></mfrac><mo>=</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mi>&#955;</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mfrac><mrow><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow><msqrt><mn>14</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>6</mn><mi>&#955;</mi><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mi>&#955;</mi></mrow><msqrt><mn>14</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><msqrt><mn>7</mn></msqrt><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mn>5</mn><mi>&#955;</mi><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>&#955;</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#177;</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>&#955;</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math></p>

</details>

---

### Q154. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mi>R</mi><mo>.</mo></math> If the mirror image of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn></mrow></mfenced></math> with respect to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mn>7</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>9</mn></mrow></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>20</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>-</mo><mi>a</mi><mo>-</mo><mn>9</mn></mrow></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>|</mo></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>86</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>84</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>88</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>88</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mn>7</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>9</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfenced><mrow><mn>20</mn><mo>,</mo><mi>b</mi><mo>,</mo><mo>-</mo><mi>a</mi><mo>-</mo><mn>9</mn></mrow></mfenced></math></p><p>Mid point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><mfenced><mrow><mfrac><mrow><mi>a</mi><mo>+</mo><mn>20</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mi>b</mi><mo>+</mo><mn>6</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>-</mo><mfrac><mi>a</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p>lies on line</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfrac><mrow><mn>20</mn><mo>+</mo><mi>a</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mn>3</mn></mrow><mn>7</mn></mfrac><mo>=</mo><mfrac><mrow><mfrac><mrow><mi>b</mi><mo>+</mo><mn>6</mn></mrow><mn>2</mn></mfrac><mo>-</mo><mn>2</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mfrac><mi>a</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>9</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"/><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>+</mo><mn>20</mn><mo>-</mo><mn>6</mn></mrow><mn>14</mn></mfrac><mo>=</mo><mfrac><mrow><mi>b</mi><mo>+</mo><mn>6</mn><mo>-</mo><mn>4</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mi>a</mi><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>18</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>14</mn><mo>+</mo><mi>a</mi></mrow><mn>14</mn></mfrac><mo>=</mo><mfrac><mrow><mi>b</mi><mo>+</mo><mn>2</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow><mn>18</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>+</mo><mn>14</mn></mrow><mn>14</mn></mfrac><mo>=</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow><mn>18</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mi>a</mi><mo>+</mo><mn>252</mn><mo>=</mo><mn>14</mn><mi>a</mi><mo>+</mo><mn>28</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>a</mi><mo>=</mo><mo>-</mo><mn>224</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mn>56</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>b</mi><mo>+</mo><mn>2</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow><mn>18</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>b</mi><mo>+</mo><mn>2</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>54</mn></mrow><mn>18</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>b</mi><mo>+</mo><mn>2</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mo>-</mo><mn>3</mn><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>32</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>|</mo><mo>=</mo><mo>|</mo><mo>-</mo><mn>56</mn><mo>-</mo><mn>32</mn><mo>|</mo><mo>=</mo><mn>88</mn></math></p>

</details>

---

### Q155. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>)</mo></math> is the image of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>)</mo></math> in the line, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/74a3b160-da13-4a87-948f-fa1fc4a3da27-image.png" style="width: 481px; height: 226px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>(</mo><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi mathvariant="normal">r</mi><mo>,</mo><mn>3</mn><mo>-</mo><mn>2</mn><mi mathvariant="normal">r</mi><mo>,</mo><mo>-</mo><mi mathvariant="normal">r</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>r</mi><mo>&#39;</mo><mi>s</mi><mo>&#160;</mo><mi>o</mi><mi>f</mi><mo>&#160;</mo><mi>P</mi><mi>R</mi><mo>&#160;</mo><mi>a</mi><mi>r</mi><mi>e</mi><mo>&#160;</mo><mo>(</mo><mn>2</mn><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>r</mi><mo>,</mo><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi>r</mi><mo>,</mo><mo>-</mo><mn>3</mn><mo>+</mo><mi>r</mi><mo>)</mo></math></p><p>Then,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>(</mo><mn>2</mn><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>r</mi><mo>)</mo><mo>+</mo><mn>2</mn><mo>(</mo><mn>1</mn><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>r</mi><mo>)</mo><mo>+</mo><mn>1</mn><mo>(</mo><mn>3</mn><mo>-</mo><mi>r</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>-</mo><mn>9</mn><mi>r</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mi>r</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>)</mo></math></p><p>then  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>,</mo><mi>b</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>-</mo><mn>3</mn><mo>=</mo><mo>-</mo><mn>2</mn></math> i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi mathvariant="normal">b</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">c</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>2</mn></math></p><p> </p>

</details>

---

### Q156. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> be the centroid of the triangle with vertices <math><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mi mathvariant="normal"></mi><mo>-</mo><mn>1</mn></mrow></mfenced></math> , <math><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi mathvariant="normal"></mi><mn>3</mn></mrow></mfenced></math> and <math><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi mathvariant="normal"></mi><mn>4</mn></mrow></mfenced></math> . Let <math><mi mathvariant="normal">P</mi></math> be the point of intersection of the lines <math><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>10</mn></math> and <math><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> . Then, the line passing through the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> and <math><mi mathvariant="normal">P</mi></math> also passes through the point:

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mo>-</mo><mn>9</mn><mo>,</mo><mo>-</mo><mn>6</mn></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mn>9,7</mn></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mn>7,6</mn></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mo>-</mo><mn>9</mn><mo>,</mo><mo>-</mo><mn>7</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfenced separators="|"><mrow><mo>-</mo><mn>9</mn><mo>,</mo><mo>-</mo><mn>6</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Centroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>2</mn></msub><mo>+</mo><msub><mi>y</mi><mn>3</mn></msub></mrow><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math><mi>D</mi><mfenced separators="|"><mrow><mn>2</mn><mi></mi><mo>,</mo><mi></mi><mn>2</mn></mrow></mfenced></math>
Point of intersection <math><mi>P</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi></mi><mo>,</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>
Equation of line <math><mi>D</mi><mi>P</mi></math> <math><mn>8</mn><mi>x</mi><mo>-</mo><mn>11</mn><mi>y</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math>.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>9</mn><mo>,</mo><mo>-</mo><mn>6</mn></mrow></mfenced></math> satisfy above equation.</p>

</details>

---

### Q157. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The shortest distance between the lines <math><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>8</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mrow><mn>1</mn></mrow></mfrac></math> and <math><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>6</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math> is

**Options:**

- **(A)** <math><mn>2</mn><msqrt><mn>30</mn></msqrt></math>
- **(B)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msqrt><mn>30</mn></msqrt></math>
- **(C)** <math><mn>3</mn><msqrt><mn>30</mn></msqrt></math>
- **(D)** <math><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>3</mn><msqrt><mn>30</mn></msqrt></math>**

**Detailed Solution:**

<math><mover accent="true"><mrow><mi>w</mi></mrow><mo>→</mo></mover><mi></mi><mo>=</mo><mi></mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>–</mo><mn>3</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>  
<math><mi></mi><mover accent="true"><mrow><mi>p</mi></mrow><mo>→</mo></mover><mo>=</mo><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>  
<math><mover accent="true"><mrow><mi>q</mi></mrow><mo>→</mo></mover><mo>=</mo><mo>-</mo><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>  
<math><mover accent="true"><mrow><mi>p</mi></mrow><mo>→</mo></mover><mo>×</mo><mover accent="true"><mrow><mi>q</mi></mrow><mo>→</mo></mover><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>i</mi></mtd><mtd><mi>j</mi></mtd><mtd><mi>k</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>6</mn><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>15</mn><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></math>  
<math><mi>S</mi><mo>.</mo><mi>D</mi><mo>.</mo><mo>=</mo><mfrac><mrow><mo>|</mo><mi>A</mi><mi>B</mi><mo>.</mo><mfenced separators="|"><mrow><mi>p</mi><mo>×</mo><mi>q</mi></mrow></mfenced><mo>|</mo></mrow><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>p</mi><mo>×</mo><mi>q</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced close="|" open="|" separators="|"><mrow><mn>36</mn><mo>+</mo><mn>225</mn><mo>+</mo><mn>9</mn></mrow></mfenced></mrow><mrow><msqrt><mn>36</mn><mo>+</mo><mn>225</mn><mo>+</mo><mn>9</mn></msqrt></mrow></mfrac><mo>=</mo><mn>3</mn><msqrt><mn>30</mn></msqrt></math>

</details>

---

### Q158. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the length of the perpendicular from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>&#946;</mi><mo>,</mo><mn>0</mn><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>,</mo><mfenced separators="|"><mrow><mi>&#946;</mi><mo>&#8800;</mo><mn>0</mn></mrow></mfenced></math> to the line, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></math> is <math><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math> , then <math><mi>&#946;</mi></math> is equal to

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mo>-</mo><mn>1</mn></math>
- **(C)** <math><mo>-</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/025c3c5e-bcb1-40e1-b847-91fe955f496a-image.png" style="width: 506px; height: 277px;" /></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfenced separators="|"><mrow><mi>&#955;</mi><mo>,</mo><mn>1</mn><mo>,</mo><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Direction ratio&#39;s of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>&#8801;</mo><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mi>&#946;</mi><mo>,</mo><mn>1</mn><mo>-</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>-</mo><mi>&#946;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>P</mi><mi>Q</mi></math> is perpendicular to given line, hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mfenced separators="|"><mrow><mi>&#955;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mn>0</mn><mfenced separators="|"><mn>1</mn></mfenced><mo>-</mo><mn>1</mn><mfenced separators="|"><mrow><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>&#955;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>P</mi><mi>Q</mi><mo>=</mo><mi>&#160;</mi><msqrt><msup><mfenced separators="|"><mrow><mi>&#955;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mfrac><mn>3</mn><mn>2</mn></mfrac></msqrt><mi>&#160;</mi></math></p><p><math><mo>&#8658;</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi>&#946;</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>1</mn><mo>-</mo><mi>&#946;</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math></p><p><math><mo>&#8658;</mo><msup><mrow><mi>&#946;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mi>&#946;</mi><mo>+</mo><mn>1</mn><mo>+</mo><msup><mrow><mi>&#946;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>&#946;</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>0</mn><mi>&#160;</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q159. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The vertices <math><mi>B</mi></math> and <math><mi>C</mi></math> of a <math><mi>&#916;</mi><mi>A</mi><mi>B</mi><mi>C</mi></math> lie on the line, <math><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>0</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math> such that <math><mi>B</mi><mi>C</mi><mo>=</mo><mn>5</mn></math> units. Then the area (in sq. units) of this triangle, given the point <math><mi>A</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mtext>&#8201;</mtext><mo>-</mo><mn>1</mn><mo>,</mo><mtext>&#8201;</mtext><mn>2</mn></mrow></mfenced><mo>,</mo></math> is

**Options:**

- **(A)** <math><mn>6</mn></math>
- **(B)** <math><mn>2</mn><msqrt><mn>34</mn></msqrt></math>
- **(C)** <math><msqrt><mn>34</mn></msqrt></math>
- **(D)** <math><mn>5</mn><msqrt><mn>17</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msqrt><mn>34</mn></msqrt></math>**

**Detailed Solution:**

<p>The points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> lie on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>4</mn></mfrac><mo>.</mo></math></p><p>Draw perpendicular <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi></math> on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c4c8106e-d669-4aee-b446-30514ec1f230-image1.png" style="width: 251px; height: 135px;" />
Clearly area of <math><mi>&#916;</mi><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#8901;</mo><mi>A</mi><mi>D</mi><mo>&#8901;</mo><mi>B</mi><mi>C</mi></math></p><p>To find a point on the line, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>4</mn></mfrac><mo>=</mo><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>3</mn><mi>r</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>4</mn><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>3</mn><mi>r</mi><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>4</mn><mi>r</mi></math></p><p>Thus, the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#8801;</mo><mfenced separators="|"><mrow><mn>3</mn><mi>r</mi><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mi>r</mi></mrow></mfenced></math></p><p>The direction ratios of a line joining two points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>1</mn></msub></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#60;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>2</mn></msub><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub><mo>&#62;</mo></math></p><p>Thus, the direction ratios of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#60;</mo><mn>3</mn><mi>r</mi><mo>-</mo><mn>2</mn><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>+</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn><mi>r</mi><mo>-</mo><mn>2</mn><mo>&#62;</mo><mo>=</mo><mo>&#60;</mo><mn>3</mn><mi>r</mi><mo>-</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn><mi>r</mi><mo>-</mo><mn>2</mn><mo>&#62;</mo></math></p><p>Since <math><mi>A</mi><mi>D</mi></math> is perpendicular to given line, hence the dot product of their direction ratios is zero.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>&#183;</mo><mfenced separators="|"><mrow><mn>3</mn><mi>r</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>0</mn><mo>&#183;</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>&#183;</mo><mfenced separators="|"><mrow><mn>4</mn><mi>r</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>r</mi><mo>-</mo><mn>9</mn><mo>+</mo><mn>16</mn><mi>r</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>25</mn><mi>r</mi><mo>-</mo><mn>17</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mn>17</mn><mn>25</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>D</mi><mo>&#8801;</mo><mfenced><mrow><mn>3</mn><mo>&#215;</mo><mfrac><mn>17</mn><mn>25</mn></mfrac><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>&#215;</mo><mfrac><mn>17</mn><mn>25</mn></mfrac></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>25</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>68</mn><mn>25</mn></mfrac></mrow></mfenced></math></p><p>The distance between the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>1</mn></msub></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>-</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mi>D</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mfrac><mn>1</mn><mn>25</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mfrac><mn>68</mn><mn>25</mn></mfrac><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mi>D</mi><mo>=</mo><msqrt><mfrac><mn>576</mn><mn>625</mn></mfrac><mo>+</mo><mn>4</mn><mo>+</mo><mfrac><mn>324</mn><mn>625</mn></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mi>D</mi><mo>=</mo><msqrt><mfrac><mn>136</mn><mn>25</mn></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mi>D</mi><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msqrt><mn>34</mn></msqrt></math> units</p><p>Hence, the area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8901;</mo><mfenced><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><msqrt><mn>34</mn></msqrt></mrow></mfenced><mo>&#8901;</mo><mn>5</mn><mo>=</mo><msqrt><mn>34</mn></msqrt></math> sq units.</p>

</details>

---

### Q160. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The length of the perpendicular from the point <math><mo>(</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn><mo>)</mo></math> on the straight line <math><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn><mi>&#160;</mi></mrow><mrow><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>7</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi></mrow><mrow><mn>1</mn></mrow></mfrac></math> is

**Options:**

- **(A)** greater than <math><mn>3</mn></math> but less than <math><mn>4</mn></math>
- **(B)** greater than <math><mn>4</mn></math>
- **(C)** less than <math><mn>2</mn></math>
- **(D)** greater than <math><mn>2</mn></math> but less than <math><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) greater than <math><mn>3</mn></math> but less than <math><mn>4</mn></math>**

**Detailed Solution:**

<p>Let <math><mi>P</mi><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mo>-</mo><mn>1,4</mn></mrow></mfenced></math></p><p>Now, any point Q on line <math><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn><mi>&#160;</mi></mrow><mrow><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>7</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mi>&#955;</mi></math> is</p><p><math><mi>Q</mi><mo>=</mo><mfenced separators="|"><mrow><mn>10</mn><mi>&#955;</mi><mo>-</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>7</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn><mi>&#160;</mi><mo>,</mo><mi>&#955;</mi></mrow></mfenced></math></p><p>Direction Ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> </p><p><math><mo>=</mo><mfenced separators="|"><mrow><mn>10</mn><mi>&#955;</mi><mo>-</mo><mn>3</mn><mo>-</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>7</mn><mi>&#955;</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#955;</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mn>10</mn><mi>&#955;</mi><mo>-</mo><mn>5</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>7</mn><mi>&#955;</mi><mo>+</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mi>&#955;</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math><mo>&#8757;</mo><mi>P</mi><mi>Q</mi><mi>&#160;</mi></math> is perpendicular to given line</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>10</mn><mfenced separators="|"><mrow><mn>10</mn><mi>&#955;</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mn>7</mn><mfenced separators="|"><mrow><mo>-</mo><mn>7</mn><mi>&#955;</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mi>&#955;</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mn>150</mn><mi>&#160;</mi><mi>&#955;</mi><mo>=</mo><mn>75</mn><mi>&#160;</mi><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>Q</mi><mo>&#8801;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><msqrt><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>49</mn><mn>4</mn></mfrac></msqrt><mo>=</mo><mfrac><mn>5</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>&#8776;</mo><mn>3</mn><mo>.</mo><mn>53</mn></math> which lies in <math><mfenced separators="|"><mrow><mn>3,4</mn></mrow></mfenced></math>.</p>

</details>

---

### Q161. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two lines $\frac{x-3}{1}=\frac{y+1}{3}=\frac{z-6}{-1}$ and $\frac{x+5}{7}=\frac{y-2}{-6}=\frac{z-3}{4}$

intersect at the point $R$. The reflection of $R$ in the $x y$ - plane has coordinates:

**Options:**

- **(A)** (2,-4,-7)
- **(B)** (2,4,7)
- **(C)** (2,-4,7)
- **(D)** (-2,4,7)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) (2,-4,-7)**

**Detailed Solution:**

Let the coordinate of $P$ with respect to line

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/PUbFBkS-EyPE1cJdRyElrUEXVKKyFGY-qKpoAmcSIQU.original.fullsize.png">


$\frac{x-3}{1}=\frac{y+1}{3}=\frac{z-6}{-1}=\lambda$

$\frac{x+5}{7}=\frac{y-2}{-6}=\frac{z-3}{4}=\mu$

$L_{1}=(\lambda+3,3 \lambda-1,-\lambda+6)$

and coordinate of $P$ w.r.t.

line $L_{2}=(7 \mu-5,-6 \mu+2,4 \mu+3)$

$\therefore \quad \lambda-7 \mu=-8,3 \lambda+6 \mu=3, \lambda+4 \mu=3$

From above equation : $\lambda=-1, \mu=1$

$\therefore \quad$ Coordinate of point of intersection $R=(2,-4,7)$

Image of $R$ w.r.t. $x y$ plane $=(2,-4,-7)$

</details>

---

### Q162. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the lines <math><mi>x</mi><mo>=</mo><mi>a</mi><mi>y</mi><mo>+</mo><mi>b</mi><mo>,</mo><mi>z</mi><mo>=</mo><mi>c</mi><mi>y</mi><mo>+</mo><mi>d</mi></math> and <math><mi>x</mi><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mi>z</mi><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mo>,</mo><mtext>&#8201;&#8201;</mtext><mi>y</mi><mo>=</mo><msup><mrow><mi>c</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mtext>&#8201;&#8201;</mtext><mi>z</mi><mo>+</mo><msup><mrow><mi>d</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup></math> are perpendicular, then

**Options:**

- **(A)** <math><mi>c</mi><mi>c</mi><mi>’</mi><mo>+</mo><mi>a</mi><mo>+</mo><mi>a</mi><mi>’</mi><mo>=</mo><mn>0</mn></math>
- **(B)** <math><mi>a</mi><mi>a</mi><mi>’</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>c</mi><mi>’</mi><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mi>b</mi><mi>b</mi><mi>’</mi><mo>+</mo><mi>c</mi><mi>c</mi><mi>’</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math><mi>a</mi><mi>b</mi><mi>’</mi><mo>+</mo><mi>b</mi><mi>c</mi><mi>’</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>a</mi><mi>a</mi><mi>’</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>c</mi><mi>’</mi><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

Direction Ratios of the first line
<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>a</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>c</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi>a</mi><mi>&#160;</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mi>&#160;</mi></math>
Hence, Direction Ratios of the first line are <math><mi>a</mi><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>c</mi><mo>.</mo></math>
For Direction Ratios of the second line
<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><msup><mrow><mi>c</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
Hence, Direction Ratios of the <math><msup><mrow><mn>2</mn></mrow><mrow><mi>n</mi><mi>d</mi></mrow></msup></math> line <math><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>c</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mo>,</mo><mi>&#160;</mi><mn>1</mn></math>
Since, both the lines are perpendicular,
<math><mi>a</mi><mo>.</mo><msup><mrow><mi>a</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>

</details>

---

### Q163. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The equation of the line passing through <math><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced><mo>,</mo></math> parallel to the plane <math><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>0</mn></math> and intersecting the line <math><mfrac><mrow><mi>x</mi><mi>&#160;</mi><mo>+</mo><mi>&#160;</mi><mn>1</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn></mrow></mfrac></math>**

**Detailed Solution:**

A variable point on line  <math><mfrac><mrow><mi>x</mi><mi> </mi><mo>+</mo><mi> </mi><mn>1</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></math>  is  <math><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn><mi>t</mi><mo>-</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>2</mn><mi>t</mi><mo>+</mo><mn>3</mn><mo>,</mo><mo>-</mo><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math> 

         <math><mo>∴</mo><mi>D</mi><mi>R</mi></math>  of variable point &  <math><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mi> </mi><mn>3</mn><mo>,</mo><mi> </mi><mn>1</mn></mrow></mfenced></math>  is

         <math><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>3</mn><mo>,</mo><mtext> </mtext><mn>2</mn><mi>t</mi><mo>,</mo><mtext> </mtext><mo>-</mo><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math> 

        Since line is parallel to  <math><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>0</mn></math> 

         <math><mo>∴</mo><mo>-</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>3</mn><mo>+</mo><mn>4</mn><mi>t</mi><mo>+</mo><mi>t</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> 

         <math><mo>⇒</mo><mi>t</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> 

         <math><mo>∴</mo><mi>D</mi><mi>R</mi></math>  of line is  <math><mfenced separators="|"><mrow><mn>6</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mi> </mi><mn>2</mn></mrow></mfenced></math>  or  <math><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mi> </mi><mo>-</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>1</mn></mrow></mfenced></math> 

         <math><mo>∴</mo></math>  Equation of line is  <math><mfrac><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn></mrow></mfrac></math>

</details>

---

### Q164. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If the angle between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>-</mo><mi>x</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn><mi>y</mi><mo>-</mo><mn>14</mn></mrow><mi>P</mi></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>7</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>7</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given lines are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>-</mo><mi>x</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn><mi>y</mi><mo>-</mo><mn>14</mn></mrow><mi>p</mi></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mfenced><mstyle displaystyle="true"><mfrac><mi>P</mi><mn>7</mn></mfrac></mstyle></mfenced></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac></math></p><p>We know that the angle between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow><msub><mi>a</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow><msub><mi>b</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub></mrow><msub><mi>c</mi><mn>1</mn></msub></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow><msub><mi>a</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow><msub><mi>b</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><msub><mi>z</mi><mn>2</mn></msub></mrow><msub><mi>c</mi><mn>2</mn></msub></mfrac></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced open="|" close="|"><mfrac><mrow><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><msub><mi>b</mi><mn>2</mn></msub><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><msub><mi>c</mi><mn>2</mn></msub></mrow><mrow><msqrt><msubsup><mi>a</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>b</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>c</mi><mn>1</mn><mn>2</mn></msubsup></msqrt><mo>&#215;</mo><msqrt><msubsup><mi>a</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>b</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>c</mi><mn>2</mn><mn>2</mn></msubsup></msqrt></mrow></mfrac></mfenced></math></p><p>Given, the angle between both lines is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mstyle displaystyle="true"><mn>2</mn><mo>&#215;</mo><mfrac><mi>P</mi><mn>7</mn></mfrac></mstyle><mo>+</mo><mn>1</mn><mo>&#215;</mo><mn>4</mn></mrow><mrow><msqrt><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt><mo>&#215;</mo><msqrt><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced><mstyle displaystyle="true"><mfrac><mi>P</mi><mn>7</mn></mfrac></mstyle></mfenced><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup></msqrt></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi>P</mi></mrow><mn>7</mn></mfrac></mstyle><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn><mo>&#215;</mo><msqrt><mn>4</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><msup><mi>P</mi><mn>2</mn></msup><mn>49</mn></mfrac></mstyle><mo>+</mo><mn>16</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>56</mn><mo>+</mo><mn>2</mn><mi>P</mi></mrow><mrow><mn>3</mn><mo>&#215;</mo><msqrt><msup><mi>P</mi><mn>2</mn></msup><mo>+</mo><mn>980</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><msup><mi>P</mi><mn>2</mn></msup><mo>+</mo><mn>980</mn></msqrt><mo>=</mo><mi>P</mi><mo>+</mo><mn>28</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mn>2</mn></msup><mo>+</mo><mn>980</mn><mo>=</mo><msup><mfenced><mrow><mi>P</mi><mo>+</mo><mn>28</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mn>2</mn></msup><mo>+</mo><mn>980</mn><mo>=</mo><msup><mi>P</mi><mn>2</mn></msup><mo>+</mo><mn>56</mn><mi>P</mi><mo>+</mo><mn>784</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>56</mn><mi>P</mi><mo>=</mo><mn>196</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>=</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q165. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The sum of the intercepts on the coordinate axes of the plane passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8211;</mo><mn>2</mn><mo>,</mo><mo>&#8211;</mo><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and containing the line joining the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#8211;</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>**

**Detailed Solution:**

Equation of plane is

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn></mtd><mtd><mi>y</mi><mo>+</mo><mn>2</mn></mtd><mtd><mi>z</mi><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>6</mn><mfenced separators="|"><mrow><mi>z</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>6</mn><mi>z</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>

<math><mo>&#8756;</mo></math> Sum of intercepts<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>8</mn><mo>+</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>8</mn><mn>6</mn></mfrac><mo>=</mo><mo>-</mo><mn>4</mn></math>

</details>

---

### Q166. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn><mo>,</mo><mo>-</mo><mn>7</mn></mrow></mfenced></math> from the plane passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> , having normal perpendicular to both the lines <math><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math> and <math><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>7</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac></math> , is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>20</mn></mrow><mrow><msqrt><mn>74</mn></msqrt></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>10</mn></mrow><mrow><msqrt><mn>83</mn></msqrt></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><msqrt><mn>83</mn></msqrt></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>10</mn></mrow><mrow><msqrt><mn>74</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>10</mn></mrow><mrow><msqrt><mn>83</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b2eb0c0e-5a94-43a1-bbb9-b63106b1d8b7-image.png" style="width: 264px; height: 180px;" /></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi></math> be the direction cosines of the line normal to the plane, then

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>-</mo><mn>2</mn><mi>m</mi><mo>+</mo><mn>3</mn><mi>n</mi><mo>=</mo><mn>0</mn></math> and <math><mn>2</mn><mi>l</mi><mo>-</mo><mi>m</mi><mo>-</mo><mi>n</mi><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>l</mi><mrow><mn>2</mn><mo>+</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mi>m</mi><mrow><mn>6</mn><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mi>n</mi><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mi>&#955;</mi></math>

<math><mo>&#8658;</mo><mi mathvariant="script"><mi>l</mi></mi><mo>=</mo><mn>5</mn><mi>&#955;</mi><mo>,</mo><mi>&#160;</mi><mi>m</mi><mo>=</mo><mn>7</mn><mi>&#955;</mi><mo>,</mo><mi>&#160;</mi><mi>n</mi><mo>=</mo><mn>3</mn><mi>&#955;</mi></math>

<math><mo>&#8756;</mo></math> The equation of the plane is

<math><mn>5</mn><mi>x</mi><mo>+</mo><mn>7</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>d</mi><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>&#160;</mi></math>it passes through<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<math><mo>&#8658;</mo><mn>5</mn><mo>-</mo><mn>7</mn><mo>-</mo><mn>3</mn><mo>+</mo><mi>d</mi><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mn>5</mn></math>

Hence, the equation of the plane is <math><mn>5</mn><mi>x</mi><mo>+</mo><mn>7</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math>

Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>P</mi><mi>Q</mi></mrow></mfenced><mo>=</mo><mfrac><mfenced close="|" open="|" separators="|"><mrow><mn>5</mn><mo>+</mo><mn>21</mn><mo>-</mo><mn>21</mn><mo>+</mo><mn>5</mn></mrow></mfenced><msqrt><msup><mfenced separators="|"><mn>5</mn></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced separators="|"><mn>7</mn></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced separators="|"><mn>3</mn></mfenced><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>P</mi><mi>Q</mi></mrow></mfenced><mo>=</mo><mfrac><mn>10</mn><msqrt><mn>25</mn><mo>+</mo><mn>49</mn><mo>+</mo><mn>9</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>P</mi><mi>Q</mi></mrow></mfenced><mo>=</mo><mfrac><mn>10</mn><msqrt><mn>83</mn></msqrt></mfrac></math></p>

</details>

---

### Q167. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The shortest distance between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>4</mn></mrow><mn>8</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>5</mn></mrow><mn>4</mn></mfrac><mo>,</mo></math> lies in the interval:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" separators="|"><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" separators="|"><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" separators="|"><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" separators="|"><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Let the direction vectors of the two lines be given by-<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><mover><mi>k</mi><mo>^</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mover><mi>k</mi><mo>^</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>8</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>The shortest distance between the two lines is given by-</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><msub><mi>z</mi><mn>2</mn></msub><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mfenced close="]" open="["><mrow><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><msub><mi>a</mi><mn>2</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><msub><mi>a</mi><mn>2</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>x</mi><mn>2</mn></msub><mo>&#8722;</mo><msub><mi>x</mi><mn>1</mn></msub></mtd><mtd><msub><mi>y</mi><mn>2</mn></msub><mo>-&#8201;</mo><msub><mi>y</mi><mn>1</mn></msub></mtd><mtd><msub><mi>z</mi><mn>2</mn></msub><mo>&#8722;</mo><msub><mi>z</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced><mfenced close="|" open="|"><mtable><mtr><mtd><mi>i</mi></mtd><mtd><mi>j</mi></mtd><mtd><mi>k</mi></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mo>&#8722;</mo><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>&#8722;</mo><mn>1</mn></mtd><mtd><mn>8</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mfenced close="|" open="|"><mtable><mtr><mtd><mi>i</mi></mtd><mtd><mi>j</mi></mtd><mtd><mi>k</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>&#8722;</mo><mn>1</mn></mtd><mtd><mn>8</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></mfrac></mfenced><mo>=</mo><mfrac><mn>54</mn><msqrt><msup><mn>9</mn><mn>2</mn></msup><mo>+</mo><msup><mn>18</mn><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><mfrac><mn>6</mn><msqrt><mn>5</mn></msqrt></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><msqrt><mn>9</mn></msqrt></mfrac><mo>&#60;</mo><mfrac><mn>6</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>&#60;</mo><mfrac><mn>6</mn><msqrt><mn>4</mn></msqrt></mfrac><mo>&#8658;</mo><mn>2</mn><mo>&#60;</mo><mfrac><mn>6</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>&#60;</mo><mn>3</mn></math></p>

</details>

---

### Q168. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The shortest distance between the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> - axis and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>-</mo><mn>4</mn><mo>,</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>We have,</p><p><math><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>-</mo><mn>4</mn></math></p><p>Change it into symmetrical form</p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>1</mn><mo>,</mo></math> then</p><p><math><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p>On solving, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>2</mn><mi>&#160;</mi><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math></p><p>Direction ratio of the line is</p><p><math><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math></p><p>Hence, equation of line in symmetrical form is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac></math></p><p>Equation of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> axis is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>0</mn></mfrac><mo>=</mo><mi>&#160;</mi><mfrac><mi>y</mi><mn>0</mn></mfrac><mo>=</mo><mi>&#160;</mi><mfrac><mi>z</mi><mn>1</mn></mfrac><mi>&#160;</mi></math></p><p>Shortest Distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|" separators="|"><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><mrow><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover></mrow></mfrac></mfenced><mo>=</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q169. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If the shortest distance between the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mi>&#945;</mi></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac><mo>,</mo><mfenced><mrow><mi>&#945;</mi><mo>&#8800;</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>+</mo><mn>3</mn><mi>&#160;</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math>,then value of <math><mi>&#945;</mi></math> is :

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>19</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>32</mn></mrow><mrow><mn>19</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>16</mn></mrow><mrow><mn>19</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>19</mn></mrow><mrow><mn>32</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>32</mn></mrow><mrow><mn>19</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let us change the line into symmetric form. </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>+</mo><mn>3</mn></math></p><p>Put <math><mi>z</mi><mo>=</mo><mn>1</mn></math> , so we get <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> and <math><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0&#160;</mn></math></p><p>We will get  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>, <math><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8756;</mo></math> The point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> lies on the line and perpendicular vector will come from  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So the equation of line would be <math><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac></math>
And the other line <math><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi></mrow><mrow><mn>1</mn></mrow></mfrac></math>
Shortest distance would be    <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">D</mi><mo>=</mo><mfrac><mfenced open="|" close="|" separators="|"><mrow><mfenced separators="|"><mrow><mover accent="true"><msub><mi>a</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><msub><mi>a</mi><mn>1</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced separators="|"><mrow><mover accent="true"><msub><mi>b</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><msub><mi>b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfenced><mfenced open="|" close="|" separators="|"><mfenced separators="|"><mrow><mover accent="true"><msub><mi>b</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><msub><mi>b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></mrow></mfenced></mfenced></mfrac></math></p><p>When   <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>a</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>1</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>a</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>b</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>b</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math><mi mathvariant="normal">D</mi><mo>=</mo></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mfrac><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mn>1</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mi mathvariant="normal">&#945;</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mi>&#160;</mi><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mn>1</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mi mathvariant="normal">&#945;</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mn>1</mn></mtd></mtr></mtable></mfenced></mfrac></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">&#160;</mi><mfrac><mfenced open="|" close="|" separators="|"><mrow><mn>3</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mn>3</mn><mi mathvariant="normal">&#945;</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mi mathvariant="normal">&#945;</mi></mrow></mfenced></mrow></mfenced><mfenced open="|" close="|" separators="|"><mrow><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="italic">j</mi><mo mathvariant="italic">^</mo></mover><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mn>3</mn><mi mathvariant="normal">&#945;</mi></mrow></mfenced><mo>+</mo><mover><mi mathvariant="italic">k</mi><mo mathvariant="italic">^</mo></mover><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mi mathvariant="normal">&#945;</mi></mrow></mfenced></mrow></mfenced></mfrac></math></p><p><math><mo>&#8658;</mo></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mfrac><mrow><mo>-</mo><mn>6</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>2</mn><mo>+</mo><mi>&#945;</mi></mrow><msqrt><mn>4</mn><mo>+</mo><msup><mrow><mo>(</mo><mn>2</mn><mo>+</mo><mn>3</mn><mi>&#945;</mi><mo>)</mo></mrow><mn>2</mn></msup><mo>+</mo><msup><mrow><mo>(</mo><mn>2</mn><mo>+</mo><mi>&#945;</mi><mo>)</mo></mrow><mn>2</mn></msup></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced open="|" close="|" separators="|"><mrow><mn>4</mn><mi>&#945;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><msqrt><mn>4</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>12</mn><mi>&#945;</mi><mo>+</mo><mn>9</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn><mi>&#945;</mi><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mfrac><mrow><mn>4</mn><mi>&#945;</mi><mo>-</mo><mn>2</mn></mrow><msqrt><mn>10</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><mi>&#945;</mi><mo>+</mo><mn>12</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>2&#945;</mi><mfenced separators="|"><mrow><mn>19</mn><mi>&#945;</mi><mo>-</mo><mn>32</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>32</mn><mn>19</mn></mfrac></math></p>

</details>

---

### Q170. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Equation of the line of the shortest distance between the lines <math> <mrow> <mfrac> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>x</mi><mo>&#8289;</mo> </mrow> <mrow> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>y</mi><mo>&#8289;</mo> </mrow> <mrow> <mo>-</mo> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>z</mi><mo>&#8289;</mo> </mrow> <mrow> <mn>1</mn> </mrow> </mfrac> </mrow> </math> and <math> <mrow> <mfrac> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>x</mi><mo>&#8289;</mo> <mo>-</mo> <mn>1</mn> </mrow> <mrow> <mn>0</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>y</mi><mo>&#8289;</mo> <mo>+</mo> <mn>1</mn> </mrow> <mrow> <mo>-</mo> <mn>2</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>z</mi><mo>&#8289;</mo> </mrow> <mrow> <mn>1</mn> </mrow> </mfrac> </mrow> </math> is

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mi></mi><mi>x</mi><mo>⁡</mo> </mrow> <mrow> <mo>-</mo> <mn>2</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi>y</mi><mo>⁡</mo> </mrow> <mrow> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi>z</mi><mo>⁡</mo> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mi></mi><mi>x</mi><mo>⁡</mo> </mrow> <mrow> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi>y</mi><mo>⁡</mo> </mrow> <mrow> <mo>-</mo> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi>z</mi><mo>⁡</mo> </mrow> <mrow> <mo>-</mo> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>x</mi><mo>⁡</mo> <mo>-</mo> <mn>1</mn> </mrow> <mrow> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>y</mi><mo>⁡</mo> <mo>+</mo> <mn>1</mn> </mrow> <mrow> <mo>-</mo> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>z</mi><mo>⁡</mo> </mrow> <mrow> <mo>-</mo> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mi></mi><mi>x</mi><mo>⁡</mo> <mo>-</mo> <mn>1</mn> </mrow> <mrow> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi>y</mi><mo>⁡</mo> <mo>+</mo> <mn>1</mn> </mrow> <mrow> <mo>-</mo> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi>z</mi><mo>⁡</mo> </mrow> <mrow> <mn>1</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math> <mrow> <mfrac> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>x</mi><mo>⁡</mo> <mo>-</mo> <mn>1</mn> </mrow> <mrow> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>y</mi><mo>⁡</mo> <mo>+</mo> <mn>1</mn> </mrow> <mrow> <mo>-</mo> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>z</mi><mo>⁡</mo> </mrow> <mrow> <mo>-</mo> <mn>2</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<p>The equation of a line of the shortest distance between the given lines will be along the perpendicular to both the lines.</p><p>A line perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:&#160;</mo><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:&#160;</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac></math> is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mfenced><mrow><mn>1</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mn>2</mn><mo>+</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>&#8722;</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>&#8722;</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mi>&#945;</mi></math></p><p>Thus, a point on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mo>&#8722;</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>)</mo></math></p><p>Similarly, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>0</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mn>1</mn></mfrac><mo>=</mo><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mi>&#955;</mi></math></p><p>Thus, a point on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#8722;</mo><mn>1</mn><mo>&#8722;</mo><mn>2</mn><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi><mo>)</mo></math></p><p>Now, a vector joining the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Q</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>&#8722;</mo><mn>1</mn><mo>)</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mo>(</mo><mn>2</mn><mi>&#955;</mi><mo>&#8722;</mo><mi>&#945;</mi><mo>+</mo><mn>1</mn><mo>)</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mo>(</mo><mi>&#945;</mi><mo>&#8722;</mo><mi>&#955;</mi><mo>)</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p>Let, the vector joining the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Q</mi></math> is along perpendicular to the two lines.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>&#8722;</mo><mn>1</mn><mo>)</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mo>(</mo><mn>2</mn><mi>&#955;</mi><mo>&#8722;</mo><mi>&#945;</mi><mo>+</mo><mn>1</mn><mo>)</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mo>(</mo><mi>&#945;</mi><mo>&#8722;</mo><mi>&#955;</mi><mo>)</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>&#8722;</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>&#8722;</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> are </p><p>proportional and hence on comparing, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>&#945;</mi><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>&#955;</mi><mo>-</mo><mi>&#945;</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>-</mo><mn>1</mn><mo>=</mo><mi>&#945;</mi><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>0</mn></math></p><p>Hence, point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math></p><p>The equation of a line passing through a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>1</mn></msub></mrow></mfenced></math> and parallel to a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>b</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>k</mi><mo>^</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow><mi>a</mi></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow><mi>b</mi></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub></mrow><mi>c</mi></mfrac></math></p><p>So, the equation of required line is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow><mrow><mo>&#8722;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mi>z</mi><mrow><mo>&#8722;</mo><mn>2</mn></mrow></mfrac><mo>.</mo></math></p>

</details>

---

### Q171. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If the lines $\frac{x+1}{2}=\frac{y-1}{1}=\frac{z+1}{3}$ and $\frac{x+2}{2}=\frac{y-k}{3}=\frac{z}{4}$ are coplanar, then the value of $k$ is :

**Options:**

- **(A)** $\frac{11}{2}$
- **(B)** $-\frac{11}{2}$
- **(C)** $\frac{9}{2}$
- **(D)** $-\frac{9}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{11}{2}$**

**Detailed Solution:**

Two given planes are coplanar, if
$$
\begin{aligned}
& \left|\begin{array}{ccc}
-2-(-1) & k-1 & 0-(-1) \\
2 & 1 & 3 \\
2 & 3 & 4
\end{array}\right|=0 \\
\Rightarrow & \left|\begin{array}{ccc}
-1 & k-1 & 1 \\
2 & 1 & 3 \\
2 & 3 & 4
\end{array}\right|=0 \\
\Rightarrow & (-1)(4-9)-(k-1)(8-6)+6-2=0 \\
\Rightarrow & k=\frac{11}{2}
\end{aligned}
$$

</details>

---

### Q172. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

The distance of the point $-\hat{i}+2 \hat{j}+6 \hat{k}$ from the straight line that passes through the point $2 \hat{i}+3 \hat{j}-4 \hat{k}$ and is parallel to the vector $6 \hat{i}+3 \hat{j}-4 \hat{k}$ is

**Options:**

- **(A)** 9
- **(B)** 8
- **(C)** 7
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7**

**Detailed Solution:**

Point is $(-1,2,6)$
Line passes through the point $(2,3,-4)$ parallel to vector whose direction ratios is $6,3,-4$.
Equation is $\frac{x-2}{6}=\frac{y-3}{3}=\frac{z+4}{-4}=\lambda$
Any point on this line is given by $x=6$ $\lambda+2, y=3 \lambda+3, z=-4 \lambda-4$
Now, d. Rs of line passing through $(-1,2,6)$ and $\perp$ to this line is $\{(x+1),(y-2),(z-6)\}$
So, $6(x+1)+3(y-2)-4(z-6)=0$ $\Rightarrow 6 x+3 y-4 z+24=0$
Now, $6(6 \lambda+2)+3(3 \lambda+3)+4(4 \lambda+4)$ $+24=0$
$\Rightarrow 61 \lambda+61=0 \Rightarrow \lambda=-1$
So, $x=-4, y=0, z=0$
Now, distance between $(-1,2,6)$ and $(-4,0,0)$ is
$\sqrt{9+4+36}=\sqrt{49}=7$

</details>

---

### Q173. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Statement 1: The shortest distance between the lines $\frac{x}{2}=\frac{y}{-1}=\frac{z}{2}$ and $\frac{x-1}{4}=\frac{y-1}{-2}=\frac{z-1}{4}$ is $\sqrt{2}$.
Statement 2: The shortest distance between two parallel lines is the perpendicular distance from any point on one of the lines to the other line.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is false.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation for Statement 1.
- **(C)** Statement 1 is false, Statement 2 is true.
- **(D)** Statement 1 is true, Statement 2 is true, , Statement 2 is not a correct explanation for Statement 1.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement 1 is false, Statement 2 is true.**

**Detailed Solution:**

On solving we will get shortest distance
$$
\neq \sqrt{2}
$$

</details>

---

### Q174. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `1`

The coordinates of the foot perpendicular from the point $(1,0,0)$ to the line
$$
\frac{x-1}{2}=\frac{y+1}{-3}=\frac{z+10}{8} \text { are }
$$

**Options:**

- **(A)** $(2,-3,8)$
- **(B)** $(1,-1,-10)$
- **(C)** $(5,-8,-4)$
- **(D)** $(3,-4,-2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(3,-4,-2)$**

**Detailed Solution:**

Let the equation of $A B$ is
$$
\frac{x-1}{2}=\frac{y-(-1)}{-3}=\frac{z-(-10)}{8}=k
$$
Let $L$ be the foot of the perpendicular drawn form $P(1,0,0)$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dN-HiLm7IeRbe503iPRJMUHJ1d4rNqo_FUfMyvRRv3I.original.fullsize.png">

$\therefore \quad L=(2 k+1,-3 \mathrm{k}-1,8 k-10)$.
Now, direction ratio of $P L=(2 k,-3 k-1,8$ $-10)$ and direction ratio of $A B=(2,-3,8)$ Since, $P L$ is perpendicular to $A B$
$$
\therefore \quad 2(2 k)-3(-3 k-1)+8(8 k-10)=0
$$
Now, $k=\frac{2(1-1)+(-3)(0+1)+8(0+10)}{(2)^2+(-3)^2+(8)^2}$
$$
=\frac{0-3+80}{4+9+64}=\frac{77}{77}=1
$$
$\therefore \quad$ Required co-ordinate
$$
=L=(2+1,-3-1,8-10)=(3,-4,-2) \text {. }
$$

</details>

---

### Q175. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `2`

A unit vector which is perpendicular to the vector $2 \hat{i}-\hat{j}+2 \hat{k}$ and is coplanar with the vectors $\hat{i}+\hat{j}-\hat{k}$ and $2 \hat{i}+2 \hat{j}-\hat{k}$ is

**Options:**

- **(A)** $\frac{2 \hat{j}+\hat{k}}{\sqrt{5}}$
- **(B)** $\frac{3 \hat{i}+2 \hat{j}-2 \hat{k}}{\sqrt{17}}$
- **(C)** $\frac{3 \hat{i}+2 \hat{j}+2 \hat{k}}{\sqrt{17}}$
- **(D)** $\frac{2 \hat{i}+2 \hat{j}-\hat{k}}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2 \hat{i}+2 \hat{j}-\hat{k}}{3}$**

**Detailed Solution:**

Let $x \hat{i}+y \hat{j}+z \hat{k}$ be the required unit vector.
Since $\hat{a}$ is perpendicular to $(2 \hat{i}-\hat{j}+2 \hat{k})$.
$$
\therefore \quad 2 x-y+2 z=0
$$


Since vector $x \hat{i}+y \hat{j}+z \hat{k}$ is coplanar with the vector $\hat{i}+\hat{j}-\hat{k}$ and $2 \hat{i}+2 \hat{j}-\hat{k}$.
$$
\begin{aligned}
\therefore \quad x \hat{i} & +y \hat{j}+z \hat{k} \\
& =p(\hat{i}+\hat{j}-\hat{k})+q(2 \hat{i}+2 \hat{j}-\hat{k}),
\end{aligned}
$$
where $p$ and $q$ are some scalars.
$$
\begin{aligned}
& \Rightarrow x \hat{i}+y \hat{j}+z \hat{k} \\
& =(p+2 q) \hat{i}+(p+2 q) \hat{j}-(p+q) \hat{k} \\
& \Rightarrow x=p+2 q, y=p+2 q, z=-p-q
\end{aligned}
$$
Now from equation (i),
$$
\begin{aligned}
& 2 p+4 q-p-2 q-2 p-2 q=0 \\
\Rightarrow & -p=0 \Rightarrow p=0 \\
\therefore & x=2 q, y=2 q, z=-q
\end{aligned}
$$
Since vector $x \hat{i}+y \hat{j}+z \hat{k}$ is a unit vector, therefore
$$
\begin{aligned}
& |x \hat{i}+y \hat{j}+z \hat{k}|=1 \\
\Rightarrow & \sqrt{x^2+y^2+z^2}=1 \\
\Rightarrow & x^2+y^2+z^2=1 \\
\Rightarrow & 4 q^2+4 q^2+q^2=1
\end{aligned}
$$
$$
\Rightarrow 9 q^2=1 \Rightarrow q=\pm \frac{1}{3}
$$
When $q=\frac{1}{3}$, then $x=\frac{2}{3}, y=\frac{2}{3}$,
$$
z=-\frac{1}{3}
$$
When $q=-\frac{1}{3}$, then $x=-\frac{2}{3}, y=-\frac{2}{3}$,
$$
z=\frac{1}{3}
$$
Here required unit vector is $\frac{2}{3} \hat{i}+\frac{2}{3} \hat{j}-\frac{1}{3} \hat{k}$ or $-\frac{2}{3} \hat{i}-\frac{2}{3} \hat{j}+\frac{1}{3} \hat{k}$.

</details>

---

### Q176. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `2`

If the lines $\frac{x-1}{2}=\frac{y+1}{3}=\frac{z-1}{4}$ and $\frac{x-3}{1}=\frac{y-k}{2}=\frac{z}{1}$ intersect, then $k$ is equal to

**Options:**

- **(A)** $-1$
- **(B)** $\frac{2}{9}$
- **(C)** $\frac{9}{2}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{9}{2}$**

**Detailed Solution:**

Any point on $\frac{x-1}{2}=\frac{y+1}{3}=\frac{z-1}{4}=t$ is $(2 t+1,3 t-1,4 t+1)$ 
And any point on $\frac{x-3}{1}=\frac{y-k}{2}=\frac{z}{1}=\mathrm{s}$ is $(s+3,2 s+k, s)$
Given lines are intersecting
$\Rightarrow \mathrm{t}=-\frac{3}{2} \text { and } \mathrm{s}=-5 \quad \therefore \mathrm{k}=\frac{9}{2}$

</details>

---

### Q177. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `3`

This question has Statement $-1$ and Statement $-2$. Of the four choices given after the statements, choose the one that best describes the two statements.
Statement-1 : The point $A(1,0,7)$ is the mirror image of the point $B(1,6,3)$ in the line $\frac{x}{1}=\frac{y-1}{2}=\frac{z-2}{3}$.
Statement-2 : The line: $\frac{x}{1}=\frac{y-1}{2}=\frac{z-2}{3}$ bisects the line segment joining $A(1,0,7)$ and $B(1,6,3)$.

**Options:**

- **(A)** Statement $-1$ is true, Statement-2 is true; Statement $-2$ is not a correct explanation for Statement $-1$
- **(B)** Statement $-1$ is true, Statement $-2$ is false.
- **(C)** Statement $-1$ is false, Statement $-2$ is true.
- **(D)** Statement $-1$ is true, Statement $-2$ is true; Statement $-2$ is a correct explanation for Statement $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement $-1$ is true, Statement-2 is true; Statement $-2$ is not a correct explanation for Statement $-1$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/BF9tTqor66xoJOaiagwYma1yUfE-sFSyHfAu_rd0hDM.original.fullsize.png">

Statement $-1: A B$ is perpendicular to given line and mid point of $A B$ lies on line Statement $-2$ is true but it is not correct explanation as it is bisector only. If it is perpendicular bisector then only statement $-2$ is correct explanation.

</details>

---

### Q178. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `3`

A line $A B$ in three-dimensional space makes angles $45^{\circ}$ and $120^{\circ}$ with the positive $x$-axis and the positive $y$-axis respectively. If $A B$ makes an acute angle $\theta$ with the positive $z$-axis, then $\theta$ equals

**Options:**

- **(A)** $45^{\circ}$
- **(B)** $60^{\circ}$
- **(C)** $75^{\circ}$
- **(D)** $30^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $60^{\circ}$**

**Detailed Solution:**

$$
\begin{aligned}
& \ell=\cos 45^{\circ}=\frac{1}{\sqrt{2}} \\
& m=\cos 120^{\circ}=-\frac{1}{2} \\
& n=\cos \theta
\end{aligned}
$$
where $\theta$ is the angle which line makes with positive z-axis.
Now $\ell^2+m^2+n^2=1$
$$
\begin{aligned}
& \Rightarrow \frac{1}{2}+\frac{1}{4}+\cos ^2 \theta=1 \\
& \cos ^2 \theta=\frac{1}{4} \\
& \Rightarrow \cos \theta=\frac{1}{2} ( $\theta$ Being acute)\\
& \Rightarrow \theta=\frac{\pi}{3}
\end{aligned}
$$

</details>

---

### Q179. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `3`

If the straight lines $\frac{x-1}{k}=\frac{y-2}{2}=\frac{z-3}{3}$ and $\frac{x-2}{3}=\frac{y-3}{k}=\frac{z-1}{2}$ intersect at a point, then the integer $k$ is equal to

**Options:**

- **(A)** $-5$
- **(B)** 5
- **(C)** 2
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-5$**

**Detailed Solution:**

$\frac{x-1}{k}=\frac{y-2}{2}=\frac{z-3}{3}$ and $\frac{x-2}{3}=\frac{y-3}{k}=\frac{z-1}{2}$
Since lines intersect in a point
$$
\begin{aligned}
& \left|\begin{array}{ccc}
k & 2 & 3 \\
3 & k & 2 \\
1 & 1 & -2
\end{array}\right|=0 \\
& \therefore 2 k^2+5 k-25=0 \\
& k=-5,5 / 2 .
\end{aligned}
$$
Directions: Questions number 17 to 21 are Assertion-Reason type questions. Each of these questions contains two statements : Statement - 1 (Assertion) and Statement-2 (Reason). Each of these questions also has four alternative choices, only one of which is the correct answer. You have to select the correct choice.

</details>

---

### Q180. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

The line passing through the points $(5,1, a)$ and $(3, b, 1)$ crosses the $y z-$ plane at the point $\left(0, \frac{17}{2}, \frac{-13}{2}\right)$. Then

**Options:**

- **(A)** $a=2, b=8$
- **(B)** $a=4, b=6$
- **(C)** $a=6, b=4$
- **(D)** $a=8, b=2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $a=6, b=4$**

**Detailed Solution:**

Equation of line passing through $(5,1, a)$ and $(3, b, 1)$ is
$$
\frac{x-5}{2}=\frac{y-1}{1-b}=\frac{z-a}{a-1}=\lambda
$$
If line crosses $y z-$ plane i.e., $x=0$
$$
\begin{aligned}
& x=2 \lambda+5=0 \\
& \Rightarrow \lambda=-5 / 2,
\end{aligned}
$$
Since, $y=\lambda(1-b)+1=\frac{17}{2}$
$$
\begin{aligned}
& -\frac{5}{2}(1-b)+1=\frac{17}{2} \\
& b=4
\end{aligned}
$$
Also, $z=\lambda(a-1)+a=-\frac{13}{2}$
$$
\begin{aligned}
& -\frac{5}{2}(a-1)+a=-\frac{13}{2} \\
& \Rightarrow a=6
\end{aligned}
$$

</details>

---

### Q181. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

If a line makes an angle of $\frac{\pi}{4}$ with the positive directions of each of $x$-axis and $y$-axis, then the angle that the line makes with the positive direction of the $z-$axis is

**Options:**

- **(A)** $\frac{\pi}{6}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{2}$**

**Detailed Solution:**

$\mathrm{l}=\cos \frac{\pi}{4}, m=\cos \frac{\pi}{4}$
we know $\mathrm{l}^2+\mathrm{m}^2+\mathrm{n}^2=1$
$\begin{aligned}
& \frac{1}{2}+\frac{1}{2}+n^2=1 \\
& \Rightarrow n=0
\end{aligned}$
Hence angle with positive direction of $\mathrm{z-}$ axis is $\frac{\pi}{2}$.

</details>

---

### Q182. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `3`

The line parallel to the $x$-axis and passing through the intersection of the lines ax $+$ $2 b y+3 b=0$ and $b x-2 a y-3 a=0$, where $(a, b) \neq(0,0)$ is

**Options:**

- **(A)** below the $x$-axis at a distance of $\frac{3}{2}$ from it
- **(B)** below the $x$-axis at a distance of $\frac{2}{3}$ from it
- **(C)** above the $x$-axis at a distance of $\frac{3}{-}$ from it
- **(D)** above the $x$-axis at a distance of $\frac{2}{3}$ from it

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) below the $x$-axis at a distance of $\frac{3}{2}$ from it**

**Detailed Solution:**

$$
\begin{aligned}
& a x+2 b y+3 b+\lambda(b x-2 a y-3 a)=0 \\
& \Rightarrow(a+b \lambda) x+(2 b-2 a \lambda) y+3 b-3 \lambda a=0 \\
& a+b \lambda=0 \Rightarrow \lambda=-a / b \\
& \Rightarrow a x+2 b y+3 b-\frac{a}{b}(b x-2 a y-3 a)=0 \\
& \Rightarrow a x+2 b y+3 b-a x+\frac{2 a^2}{b} y+\frac{3 a^2}{b}=0 \\
& y\left(2 b+\frac{2 a^2}{b}\right)+3 b+\frac{3 a^2}{b}=0 \\
& y\left(\frac{2 b^2+2 a^2}{b}\right)=-\left(\frac{3 b^2+3 a^2}{b}\right) \\
& y=\frac{-3\left(a^2+b^2\right)}{2\left(b^2+a^2\right)}=\frac{-3}{2} \\
&
\end{aligned}
$$
$y=-\frac{3}{2}$ so it is $3 / 2$ units below $x$-axis.

</details>

---

### Q183. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

The two lines $x=a y+b, z=c y+d$ and $x=a^{\prime} y+b^{\prime} z=c^{\prime} y+d^{\prime}$ will be perpendicular, if and only if

**Options:**

- **(A)** $a a^{\prime}+c c^{\prime}+1=0$
- **(B)** $\mathrm{a} \mathrm{a}^{\prime}+\mathrm{b} \mathrm{b}^{\prime}+\mathrm{c} \mathrm{c}^{\prime}+1=0$
- **(C)** $\mathrm{a}^{\prime}+\mathrm{b} \mathrm{b}^{\prime}+\mathrm{c} \mathrm{c}^{\prime}=0$
- **(D)** $\left(a+a^{\prime}\right)\left(b+b^{\prime}\right)+\left(c+c^{\prime}\right)=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $a a^{\prime}+c c^{\prime}+1=0$**

**Detailed Solution:**

$\frac{\mathrm{x}-\mathrm{b}}{\mathrm{a}}=\frac{\mathrm{y}}{1}=\frac{3-\mathrm{d}}{\mathrm{c}} ; \frac{\mathrm{x}-\mathrm{b}^{\prime}}{\mathrm{a}^{\prime}}=\frac{\mathrm{y}}{1}=\frac{3-\mathrm{d}^{\prime}}{\mathrm{c}^{\prime}}$
For perpendicular $\mathrm{aa}^{\prime}+1+\mathrm{cc}^{\prime}=0$

</details>

---

