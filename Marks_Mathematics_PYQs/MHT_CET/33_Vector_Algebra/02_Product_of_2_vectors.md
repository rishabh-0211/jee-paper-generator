# MHT CET Mathematics - Vector Algebra

## Topic 2: Product of 2 vectors

**Total Questions:** 203

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A parallelopiped is determined by vectors $\vec{a} = \hat{i} + 2\hat{k}, \vec{b} = \hat{i} + \hat{j} - \hat{k}$ and $\vec{c} = 2\hat{i} + 2\hat{j} + 3\hat{k}$. The length (in units) of its altitude drawn to the base determined by vectors $\vec{b}$ and $\vec{c}$ is

**Options:**

- **(A)** $\sqrt{2}$
- **(B)** $5\sqrt{2}$
- **(C)** $\dfrac{1}{\sqrt{2}}$
- **(D)** $\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{\sqrt{2}}$**

**Detailed Solution:**

The volume of the parallelopiped is given by the scalar triple product $V = |[\vec{a} \quad \vec{b} \quad \vec{c}]|$.

The area of the base determined by vectors $\vec{b}$ and $\vec{c}$ is $A = |\vec{b} \times \vec{c}|$.

The length of the altitude $h$ drawn to this base is $h = \dfrac{V}{A}$.

Calculating the cross product $\vec{b} \times \vec{c}$:

$\vec{b} \times \vec{c} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & -1 \\ 2 & 2 & 3 \end{vmatrix} = \hat{i}(3 + 2) - \hat{j}(3 + 2) + \hat{k}(2 - 2) = 5\hat{i} - 5\hat{j}$

The area of the base is $A = |5\hat{i} - 5\hat{j}| = \sqrt{5^2 + (-5)^2} = \sqrt{50} = 5\sqrt{2}$.

Calculating the volume $V$ by taking the dot product of $\vec{a}$ with $\vec{b} \times \vec{c}$:

$V = |(\hat{i} + 2\hat{k}) \cdot (5\hat{i} - 5\hat{j})| = |1(5) + 0(-5) + 2(0)| = 5$

The length of the altitude is $h = \dfrac{5}{5\sqrt{2}} = \dfrac{1}{\sqrt{2}}$.

Answer: $\dfrac{1}{\sqrt{2}}$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the vector $\bar{r}$ is perpendicular to $\hat{i} - \hat{k}$ and $\bar{r} \times (\hat{i} + x\hat{j} - \hat{k}) = \hat{i} + 2\hat{j} + 3\hat{k}$, then the value of $\bar{r} \cdot (\hat{i} + x\hat{j} - \hat{k}) =$

**Options:**

- **(A)** $-2$
- **(B)** $-1$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-2$**

**Detailed Solution:**

Let $\bar{r} = a\hat{i} + b\hat{j} + c\hat{k}$.

Since $\bar{r}$ is perpendicular to $\hat{i} - \hat{k}$, their dot product is zero:

$\bar{r} \cdot (\hat{i} - \hat{k}) = 0 \Rightarrow a - c = 0 \Rightarrow a = c$

Thus, $\bar{r} = a\hat{i} + b\hat{j} + a\hat{k}$.

We are given $\bar{r} \times (\hat{i} + x\hat{j} - \hat{k}) = \hat{i} + 2\hat{j} + 3\hat{k}$. Expanding the cross product:

$\begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a & b & a \\ 1 & x & -1 \end{vmatrix} = \hat{i} + 2\hat{j} + 3\hat{k}$

$\hat{i}(-b - ax) - \hat{j}(-a - a) + \hat{k}(ax - b) = \hat{i} + 2\hat{j} + 3\hat{k}$

Comparing the coefficients on both sides, we get:

$2a = 2 \Rightarrow a = 1$

$-b - ax = 1 \Rightarrow -b - x = 1$

$ax - b = 3 \Rightarrow x - b = 3$

Adding the equations $-b - x = 1$ and $x - b = 3$ gives:

$-2b = 4 \Rightarrow b = -2$

Substituting $b = -2$ into $x - b = 3$ gives:

$x - (-2) = 3 \Rightarrow x = 1$

Therefore, $\bar{r} = \hat{i} - 2\hat{j} + \hat{k}$ and the second vector is $\hat{i} + \hat{j} - \hat{k}$.

Now, we find the required dot product:

$\bar{r} \cdot (\hat{i} + x\hat{j} - \hat{k}) = (\hat{i} - 2\hat{j} + \hat{k}) \cdot (\hat{i} + \hat{j} - \hat{k})$

$= (1)(1) + (-2)(1) + (1)(-1) = 1 - 2 - 1 = -2$

Answer: $-2$

</details>

---

### Q3. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a} = 2\hat{i} + \hat{k},\ \bar{b} = \hat{i} + \hat{j} + \hat{k},$ and $\bar{c} = 4\hat{i} - 3\hat{j} + 7\hat{k}$. If $\bar{r}$ is a vector such that $\bar{r} \times \bar{b} = \bar{c} \times \bar{b}$ and $\bar{r} \cdot \bar{a} = 0$, then the value of the scalar product $\bar{r} \cdot \hat{i}$ is:

**Options:**

- **(A)** $-1$
- **(B)** $2$
- **(C)** $0$
- **(D)** $-3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-1$**

**Detailed Solution:**

Given $\bar{r} \times \bar{b} = \bar{c} \times \bar{b}$

$(\bar{r} - \bar{c}) \times \bar{b} = 0$

This implies that $\bar{r} - \bar{c}$ is parallel to $\bar{b}$, so we can write:

$\bar{r} - \bar{c} = \lambda \bar{b}$

$\bar{r} = \bar{c} + \lambda \bar{b}$

Taking the dot product with $\bar{a}$ on both sides:

$\bar{r} \cdot \bar{a} = (\bar{c} + \lambda \bar{b}) \cdot \bar{a}$

Since $\bar{r} \cdot \bar{a} = 0$, we get:

$\bar{c} \cdot \bar{a} + \lambda (\bar{b} \cdot \bar{a}) = 0$

Substituting the given vectors $\bar{a} = 2\hat{i} + \hat{k}$, $\bar{b} = \hat{i} + \hat{j} + \hat{k}$, and $\bar{c} = 4\hat{i} - 3\hat{j} + 7\hat{k}$:

$\bar{c} \cdot \bar{a} = (4)(2) + (-3)(0) + (7)(1) = 15$

$\bar{b} \cdot \bar{a} = (1)(2) + (1)(0) + (1)(1) = 3$

Substituting these values into the equation:

$15 + \lambda(3) = 0 \Rightarrow \lambda = -5$

Substituting $\lambda = -5$ back into the expression for $\bar{r}$:

$\bar{r} = \bar{c} - 5\bar{b}$

$\bar{r} = (4\hat{i} - 3\hat{j} + 7\hat{k}) - 5(\hat{i} + \hat{j} + \hat{k})$

$\bar{r} = -\hat{i} - 8\hat{j} + 2\hat{k}$

The scalar product $\bar{r} \cdot \hat{i}$ is the coefficient of $\hat{i}$ in $\bar{r}$:

$\bar{r} \cdot \hat{i} = -1$

Answer: $-1$

</details>

---

### Q4. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the scalar products of a vector $\bar{a} = x\hat{i} + y\hat{j} + z\hat{k}$ with $2\hat{i} + \hat{j} + \hat{k},\ \hat{i} - \hat{j} + \hat{k},\ \hat{i} + 2\hat{j} + 3\hat{k}$ are $5, 3,$ and $5$ respectively, then $x + y + z = \ldots$

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$**

**Detailed Solution:**

Given $\vec{a} = x\hat{i} + y\hat{j} + z\hat{k}$.

The scalar products with the given vectors yield the following system of linear equations:

$2x + y + z = 5$

$x - y + z = 3$

$x + 2y + 3z = 5$

Adding the first and second equations:

$3x + 2z = 8$

Multiplying the second equation by $2$ and adding to the third equation:

$2(x - y + z) + (x + 2y + 3z) = 2(3) + 5$

$3x + 5z = 11$

Subtracting the equation $3x + 2z = 8$ from $3x + 5z = 11$:

$3z = 3 \Rightarrow z = 1$

Substituting $z = 1$ into $3x + 2z = 8$:

$3x + 2(1) = 8 \Rightarrow 3x = 6 \Rightarrow x = 2$

Substituting $x = 2$ and $z = 1$ into $x - y + z = 3$:

$2 - y + 1 = 3 \Rightarrow y = 0$

Therefore, $x + y + z = 2 + 0 + 1 = 3$.

Answer: $3$

</details>

---

### Q5. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For two non-zero, non-collinear, non-orthogonal vectors $\vec{a}$ and $\vec{b}$ where $\theta$ is angle between them, then $\dfrac{(\vec{a} \cdot \vec{b})^2 + |\vec{a} \times \vec{b}|^2}{(\vec{a} \cdot \vec{b})^2 - |\vec{a} \times \vec{b}|^2} =$

**Options:**

- **(A)** $\tan\left(\dfrac{\pi}{4} + \theta\right)$
- **(B)** $\tan\left(\dfrac{\pi}{4} - \theta\right)$
- **(C)** $\sec 2\theta$
- **(D)** $\csc 2\theta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sec 2\theta$**

**Detailed Solution:**

Using the definitions of dot product and cross product magnitude:

$\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos \theta$

$|\vec{a} \times \vec{b}| = |\vec{a}| |\vec{b}| \sin \theta$

Substituting these into the given expression:

Numerator $= (\vec{a} \cdot \vec{b})^2 + |\vec{a} \times \vec{b}|^2$

$= |\vec{a}|^2 |\vec{b}|^2 \cos^2 \theta + |\vec{a}|^2 |\vec{b}|^2 \sin^2 \theta$

$= |\vec{a}|^2 |\vec{b}|^2 (\cos^2 \theta + \sin^2 \theta) = |\vec{a}|^2 |\vec{b}|^2$

Denominator $= (\vec{a} \cdot \vec{b})^2 - |\vec{a} \times \vec{b}|^2$

$= |\vec{a}|^2 |\vec{b}|^2 \cos^2 \theta - |\vec{a}|^2 |\vec{b}|^2 \sin^2 \theta$

$= |\vec{a}|^2 |\vec{b}|^2 (\cos^2 \theta - \sin^2 \theta) = |\vec{a}|^2 |\vec{b}|^2 \cos 2\theta$

Dividing the numerator by the denominator:

$\dfrac{(\vec{a} \cdot \vec{b})^2 + |\vec{a} \times \vec{b}|^2}{(\vec{a} \cdot \vec{b})^2 - |\vec{a} \times \vec{b}|^2} = \dfrac{|\vec{a}|^2 |\vec{b}|^2}{|\vec{a}|^2 |\vec{b}|^2 \cos 2\theta}$

$= \dfrac{1}{\cos 2\theta} = \sec 2\theta$

Answer: $\sec 2\theta$

</details>

---

### Q6. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the vectors $\bar{a} = 2\bar{i} + \bar{j} + 3\bar{k}$ and $\bar{b} = p\bar{i} + 2\bar{j} + 2\bar{k}$ are perpendicular to each other, then ...

**Options:**

- **(A)** $p = -4$
- **(B)** $p = 4$
- **(C)** $p = 2$
- **(D)** $p = -2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $p = -4$**

**Detailed Solution:**

Given vectors are $\vec{a} = 2\hat{i} + \hat{j} + 3\hat{k}$ and $\vec{b} = p\hat{i} + 2\hat{j} + 2\hat{k}$.

Since the vectors are perpendicular to each other, their dot product must be zero.

$\vec{a} \cdot \vec{b} = 0$

$(2)(p) + (1)(2) + (3)(2) = 0$

$2p + 2 + 6 = 0$

$2p + 8 = 0$

$p = -4$

Answer: $p = -4$

</details>

---

### Q7. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The cartesian equation of the line passing through the point $\hat{i} + 2\hat{j} + 3\hat{k}$ and perpendicular to the vectors $\hat{i} + \hat{j} + \hat{k}$ and $2\hat{i} - \hat{j} + \hat{k}$ is

**Options:**

- **(A)** $\dfrac{x+1}{2} = y + 2 = \dfrac{z+3}{3}$
- **(B)** $\dfrac{x-1}{2} = y - 2 = \dfrac{z-3}{3}$
- **(C)** $\dfrac{x-1}{2} = y - 2 = \dfrac{z-3}{-3}$
- **(D)** $\dfrac{x+1}{2} = y + 2 = \dfrac{z+3}{-3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{x-1}{2} = y - 2 = \dfrac{z-3}{-3}$**

**Detailed Solution:**

The line passes through the point with position vector $\hat{i} + 2\hat{j} + 3\hat{k}$, which corresponds to the point $(1, 2, 3)$.

The line is perpendicular to the vectors $\vec{a} = \hat{i} + \hat{j} + \hat{k}$ and $\vec{b} = 2\hat{i} - \hat{j} + \hat{k}$. Therefore, its direction vector $\vec{d}$ is parallel to the cross product of $\vec{a}$ and $\vec{b}$.

$\vec{d} = \vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & 1 \\ 2 & -1 & 1 \end{vmatrix}$

$\vec{d} = \hat{i}(1 - (-1)) - \hat{j}(1 - 2) + \hat{k}(-1 - 2)$

$\vec{d} = 2\hat{i} + \hat{j} - 3\hat{k}$

The direction ratios of the line are $2, 1, -3$.

The cartesian equation of the line passing through $(1, 2, 3)$ with direction ratios $2, 1, -3$ is given by:

$\dfrac{x - 1}{2} = \dfrac{y - 2}{1} = \dfrac{z - 3}{-3}$

This can be written as $\dfrac{x-1}{2} = y - 2 = \dfrac{z-3}{-3}$.

Answer: $\dfrac{x-1}{2} = y - 2 = \dfrac{z-3}{-3}$

</details>

---

### Q8. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $|\vec{a} + \vec{b}| = |\vec{a} - \vec{b}|$ then the angle between $\vec{a}$ and $\vec{b}$ is

**Options:**

- **(A)** $0^\circ$
- **(B)** $45^\circ$
- **(C)** $90^\circ$
- **(D)** $180^\circ$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $90^\circ$**

**Detailed Solution:**

Given $|\vec{a} + \vec{b}| = |\vec{a} - \vec{b}|$

Squaring both sides, we get

$|\vec{a} + \vec{b}|^2 = |\vec{a} - \vec{b}|^2$

$|\vec{a}|^2 + |\vec{b}|^2 + 2\vec{a} \cdot \vec{b} = |\vec{a}|^2 + |\vec{b}|^2 - 2\vec{a} \cdot \vec{b}$

$4\vec{a} \cdot \vec{b} = 0$

$\vec{a} \cdot \vec{b} = 0$

$|\vec{a}| |\vec{b}| \cos \theta = 0$

$\cos \theta = 0$

$\theta = 90^\circ$

Answer: $90^\circ$

</details>

---

### Q9. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{u}$ and $\vec{v}$ be unit vectors such that the angle between them is $\theta = \dfrac{\pi}{6}$. If the adjacent sides of a parallelogram are represented by the vectors $\vec{a} = 2\vec{u} + 3\vec{v}$ and $\vec{b} = \vec{u} - \vec{v}$, then the area of the parallelogram is

**Options:**

- **(A)** $5$
- **(B)** $\dfrac{5\sqrt{3}}{2}$
- **(C)** $2.5$
- **(D)** $16\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2.5$**

**Detailed Solution:**

The area of a parallelogram with adjacent sides $\vec{a}$ and $\vec{b}$ is given by $|\vec{a} \times \vec{b}|$.

Given $\vec{a} = 2\vec{u} + 3\vec{v}$ and $\vec{b} = \vec{u} - \vec{v}$, we find their cross product:

$\vec{a} \times \vec{b} = (2\vec{u} + 3\vec{v}) \times (\vec{u} - \vec{v})$

$\vec{a} \times \vec{b} = 2(\vec{u} \times \vec{u}) - 2(\vec{u} \times \vec{v}) + 3(\vec{v} \times \vec{u}) - 3(\vec{v} \times \vec{v})$

Since the cross product of a vector with itself is zero ($\vec{u} \times \vec{u} = \vec{0}$ and $\vec{v} \times \vec{v} = \vec{0}$) and $\vec{v} \times \vec{u} = -(\vec{u} \times \vec{v})$, we get:

$\vec{a} \times \vec{b} = -2(\vec{u} \times \vec{v}) - 3(\vec{u} \times \vec{v}) = -5(\vec{u} \times \vec{v})$

The area of the parallelogram is the magnitude of this vector:

Area $= |-5(\vec{u} \times \vec{v})| = 5|\vec{u} \times \vec{v}|$

The magnitude of the cross product of two unit vectors is given by $|\vec{u} \times \vec{v}| = |\vec{u}||\vec{v}|\sin\theta$.

Since $\vec{u}$ and $\vec{v}$ are unit vectors, $|\vec{u}| = 1$ and $|\vec{v}| = 1$. The angle between them is $\theta = \dfrac{\pi}{6}$.

$|\vec{u} \times \vec{v}| = (1)(1)\sin\left(\dfrac{\pi}{6}\right) = \dfrac{1}{2}$

Area $= 5 \times \dfrac{1}{2} = 2.5$

Answer: $2.5$

</details>

---

### Q10. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}, \bar{b}$ are unit vectors and $\bar{a} \cdot \bar{b} = 0$, then $(\bar{a} - 2\bar{b}) \cdot \{(2\bar{a} + \bar{b}) \times (\bar{a} \times \bar{b})\} = ...$

**Options:**

- **(A)** $5$
- **(B)** $6$
- **(C)** $8$
- **(D)** $10$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5$**

**Detailed Solution:**

Given $|\bar{a}| = 1$, $|\bar{b}| = 1$, and $\bar{a} \cdot \bar{b} = 0$.

Consider the vector triple product $(2\bar{a} + \bar{b}) \times (\bar{a} \times \bar{b})$.

Using the identity $\bar{A} \times (\bar{B} \times \bar{C}) = (\bar{A} \cdot \bar{C})\bar{B} - (\bar{A} \cdot \bar{B})\bar{C}$, we get:

$(2\bar{a} + \bar{b}) \times (\bar{a} \times \bar{b}) = \{(2\bar{a} + \bar{b}) \cdot \bar{b}\}\bar{a} - \{(2\bar{a} + \bar{b}) \cdot \bar{a}\}\bar{b}$

Evaluating the dot products:

$(2\bar{a} + \bar{b}) \cdot \bar{b} = 2(\bar{a} \cdot \bar{b}) + |\bar{b}|^2 = 2(0) + 1 = 1$

$(2\bar{a} + \bar{b}) \cdot \bar{a} = 2|\bar{a}|^2 + \bar{a} \cdot \bar{b} = 2(1) + 0 = 2$

Substituting these values back, we obtain:

$(2\bar{a} + \bar{b}) \times (\bar{a} \times \bar{b}) = 1\bar{a} - 2\bar{b} = \bar{a} - 2\bar{b}$

Now, substituting this into the original expression:

$(\bar{a} - 2\bar{b}) \cdot \{(2\bar{a} + \bar{b}) \times (\bar{a} \times \bar{b})\} = (\bar{a} - 2\bar{b}) \cdot (\bar{a} - 2\bar{b})$

$= |\bar{a} - 2\bar{b}|^2$

$= |\bar{a}|^2 - 4(\bar{a} \cdot \bar{b}) + 4|\bar{b}|^2$

$= 1 - 4(0) + 4(1) = 5$

Answer: $5$

</details>

---

### Q11. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $|\vec{u}| = 5, |\vec{v}| = 13, |\vec{u} \times \vec{v}| = 25$, then $\vec{u} \cdot \vec{v} = ...$

**Options:**

- **(A)** $15$
- **(B)** $\pm \dfrac{5}{13}$
- **(C)** $\pm 60$
- **(D)** $\pm 65$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\pm 60$**

**Detailed Solution:**

Using Lagrange's identity:

$|\vec{u} \times \vec{v}|^2 + (\vec{u} \cdot \vec{v})^2 = |\vec{u}|^2 |\vec{v}|^2$

Substituting the given values:

$(25)^2 + (\vec{u} \cdot \vec{v})^2 = (5)^2 (13)^2$

$625 + (\vec{u} \cdot \vec{v})^2 = 25 \times 169$

$625 + (\vec{u} \cdot \vec{v})^2 = 4225$

$(\vec{u} \cdot \vec{v})^2 = 4225 - 625 = 3600$

$\vec{u} \cdot \vec{v} = \pm 60$

Answer: $\pm 60$

</details>

---

### Q12. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For any vector, $\bar{a}$ if $\hat{i}\times(\bar{a}\times\hat{i})+\hat{j}\times(\bar{a}\times\hat{j})+\hat{k}\times(\bar{a}\times\hat{k})=m\bar{a}$, then the value of $m$ is ...

**Options:**

- **(A)** $2$
- **(B)** $3$
- **(C)** $1$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2$**

**Detailed Solution:**

Using the vector triple product formula $\vec{A} \times (\vec{B} \times \vec{C}) = (\vec{A} \cdot \vec{C})\vec{B} - (\vec{A} \cdot \vec{B})\vec{C}$

$\hat{i} \times (\bar{a} \times \hat{i}) = (\hat{i} \cdot \hat{i})\bar{a} - (\hat{i} \cdot \bar{a})\hat{i} = \bar{a} - (\bar{a} \cdot \hat{i})\hat{i}$

$\hat{j} \times (\bar{a} \times \hat{j}) = (\hat{j} \cdot \hat{j})\bar{a} - (\hat{j} \cdot \bar{a})\hat{j} = \bar{a} - (\bar{a} \cdot \hat{j})\hat{j}$

$\hat{k} \times (\bar{a} \times \hat{k}) = (\hat{k} \cdot \hat{k})\bar{a} - (\hat{k} \cdot \bar{a})\hat{k} = \bar{a} - (\bar{a} \cdot \hat{k})\hat{k}$

Adding the three equations:

$\hat{i} \times (\bar{a} \times \hat{i}) + \hat{j} \times (\bar{a} \times \hat{j}) + \hat{k} \times (\bar{a} \times \hat{k}) = 3\bar{a} - [(\bar{a} \cdot \hat{i})\hat{i} + (\bar{a} \cdot \hat{j})\hat{j} + (\bar{a} \cdot \hat{k})\hat{k}]$

Since any vector $\bar{a}$ can be written as $\bar{a} = (\bar{a} \cdot \hat{i})\hat{i} + (\bar{a} \cdot \hat{j})\hat{j} + (\bar{a} \cdot \hat{k})\hat{k}$

The sum becomes $3\bar{a} - \bar{a} = 2\bar{a}$

Comparing with $m\bar{a}$, we get $m = 2$

Answer: $2$

</details>

---

### Q13. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Given the following expression
A) $(\vec{a} \times \vec{b}) \cdot \vec{c}$
B) $\vec{a} \times (\vec{b} \cdot \vec{c})$
C) $\vec{a} \cdot (\vec{b} \cdot \vec{c})$
D) $|\vec{a}|(\vec{b} \cdot \vec{c})$
E) $(\vec{a} \cdot \vec{b}) \times (\vec{b} \cdot \vec{c})$
Then which of the following is not correct

**Options:**

- **(A)** B and E are meaningful
- **(B)** A and D are meaningful
- **(C)** B, C and E are meaningless
- **(D)** A is meaningful but B is meaningless

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) B and E are meaningful**

**Detailed Solution:**

Expression A: $(\vec{a} \times \vec{b})$ is a vector. The dot product of a vector with another vector $\vec{c}$ is a scalar. Thus, A is meaningful.

Expression B: $(\vec{b} \cdot \vec{c})$ is a scalar. The cross product is defined only between two vectors. Thus, B is meaningless.

Expression C: $(\vec{b} \cdot \vec{c})$ is a scalar. The dot product is defined only between two vectors. Thus, C is meaningless.

Expression D: $|\vec{a}|$ is a scalar and $(\vec{b} \cdot \vec{c})$ is a scalar. The product of two scalars is a scalar. Thus, D is meaningful.

Expression E: $(\vec{a} \cdot \vec{b})$ and $(\vec{b} \cdot \vec{c})$ are both scalars. The cross product is defined only between two vectors. Thus, E is meaningless.

From the above analysis, A and D are meaningful, while B, C, and E are meaningless.

The statement "B and E are meaningful" is incorrect.

Answer: B and E are meaningful

</details>

---

### Q14. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Two adjacent sides of a parallelogram ABCD are given by $\overline{AB} = 2\hat{i} + 10\hat{j} + 11\hat{k}$ and $\overline{AD} = -\hat{i} + 2\hat{j} + 2\hat{k}$. The side $AD$ is rotated by an acute angle $\alpha$ in the plane of the parallelogram so that $AD$ becomes $AD'$. If $AD'$ makes a right angle with the side $AB$, then the cosine of the angle $\alpha$ is...

**Options:**

- **(A)** $\dfrac{8}{9}$
- **(B)** $\dfrac{\sqrt{17}}{9}$
- **(C)** $\dfrac{1}{9}$
- **(D)** $\dfrac{4\sqrt{5}}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\sqrt{17}}{9}$**

**Detailed Solution:**

Let $\theta$ be the angle between the vectors $\overrightarrow{AB}$ and $\overrightarrow{AD}$.

$\cos\theta = \dfrac{\overrightarrow{AB} \cdot \overrightarrow{AD}}{|\overrightarrow{AB}| |\overrightarrow{AD}|}$

Given $\overrightarrow{AB} = 2\hat{i} + 10\hat{j} + 11\hat{k}$ and $\overrightarrow{AD} = -\hat{i} + 2\hat{j} + 2\hat{k}$, we have:

$\overrightarrow{AB} \cdot \overrightarrow{AD} = (2)(-1) + (10)(2) + (11)(2) = -2 + 20 + 22 = 40$

$|\overrightarrow{AB}| = \sqrt{2^2 + 10^2 + 11^2} = \sqrt{4 + 100 + 121} = \sqrt{225} = 15$

$|\overrightarrow{AD}| = \sqrt{(-1)^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$

$\cos\theta = \dfrac{40}{15 \times 3} = \dfrac{40}{45} = \dfrac{8}{9}$

Since $\cos\theta > 0$, $\theta$ is an acute angle.

The vector $\overrightarrow{AD}$ is rotated by an acute angle $\alpha$ in the plane of the parallelogram to become $\overrightarrow{AD'}$, which is perpendicular to $\overrightarrow{AB}$. This means the angle between $\overrightarrow{AB}$ and $\overrightarrow{AD'}$ is $90^{\circ}$.

Since all vectors lie in the same plane, the angle of rotation $\alpha$ is either $90^{\circ} - \theta$ or $90^{\circ} + \theta$. Because $\alpha$ is given as an acute angle, we must have:

$\alpha = 90^{\circ} - \theta$

Therefore, the cosine of the angle $\alpha$ is:

$\cos\alpha = \cos(90^{\circ} - \theta) = \sin\theta$

Using the identity $\sin\theta = \sqrt{1 - \cos^2\theta}$ (since $\theta$ is acute):

$\cos\alpha = \sqrt{1 - \left(\dfrac{8}{9}\right)^2} = \sqrt{1 - \dfrac{64}{81}} = \sqrt{\dfrac{17}{81}} = \dfrac{\sqrt{17}}{9}$

Answer: $\dfrac{\sqrt{17}}{9}$

</details>

---

### Q15. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\theta \in \left(0, \dfrac{\pi}{2}\right)$ for which vectors $\bar{a} = (\sin\theta)\hat{i} + (\cos\theta)\hat{j}$ and $\bar{b} = \hat{i} - \sqrt{3}\hat{j} + 2\hat{k}$ are perpendicular is

**Options:**

- **(A)** $\theta = \dfrac{\pi}{3}$
- **(B)** $\theta = \dfrac{\pi}{6}$
- **(C)** $\theta = \dfrac{\pi}{4}$
- **(D)** $\theta = \dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\theta = \dfrac{\pi}{3}$**

**Detailed Solution:**

For two vectors $\bar{a}$ and $\bar{b}$ to be perpendicular, their dot product must be zero.

$\bar{a} \cdot \bar{b} = 0$

$((\sin\theta)\hat{i} + (\cos\theta)\hat{j}) \cdot (\hat{i} - \sqrt{3}\hat{j} + 2\hat{k}) = 0$

$\sin\theta(1) + \cos\theta(-\sqrt{3}) + 0(2) = 0$

$\sin\theta - \sqrt{3}\cos\theta = 0$

$\sin\theta = \sqrt{3}\cos\theta$

$\tan\theta = \sqrt{3}$

Since $\theta \in \left(0, \dfrac{\pi}{2}\right)$, we have $\theta = \dfrac{\pi}{3}$.

</details>

---

### Q16. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $|\bar{a} \cdot \bar{b}|^2 + |\bar{a} \times \bar{b}| \cdot |\bar{a} \times \bar{b}|$ is $\ldots$

**Options:**

- **(A)** $-a^2 b^2$
- **(B)** $a^2 b^2$
- **(C)** $a^2 b^2 \cos\theta$
- **(D)** $a^2 b^2 \sin\theta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $a^2 b^2$**

**Detailed Solution:**

Let $\theta$ be the angle between vectors $\bar{a}$ and $\bar{b}$.

The dot product is given by $\bar{a} \cdot \bar{b} = |\bar{a}| |\bar{b}| \cos\theta = a b \cos\theta$.

The magnitude of the cross product is given by $|\bar{a} \times \bar{b}| = |\bar{a}| |\bar{b}| \sin\theta = a b \sin\theta$.

The given expression is $|\bar{a} \cdot \bar{b}|^2 + |\bar{a} \times \bar{b}| \cdot |\bar{a} \times \bar{b}|$.

Substituting the values:

$|\bar{a} \cdot \bar{b}|^2 + |\bar{a} \times \bar{b}|^2 = (a b \cos\theta)^2 + (a b \sin\theta)^2$

$= a^2 b^2 \cos^2\theta + a^2 b^2 \sin^2\theta$

$= a^2 b^2 (\cos^2\theta + \sin^2\theta)$

$= a^2 b^2 (1) = a^2 b^2$

Answer: $a^2 b^2$

</details>

---

### Q17. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a} \cdot \bar{b} = \beta$ and $\bar{a} \times \bar{b} = \bar{c}$ then $\bar{a} = $

**Options:**

- **(A)** $\dfrac{\bar{b} \times \bar{c} - \beta\bar{b}}{|\bar{b}|^2}$
- **(B)** $\dfrac{\bar{b} \times \bar{c} - \beta\bar{c}}{|\bar{b}|^2}$
- **(C)** $\dfrac{\bar{b} \times \bar{c} + \beta\bar{b}}{|\bar{b}|^2}$
- **(D)** $\dfrac{\bar{b} \times \bar{c} + \beta\bar{c}}{|\bar{b}|^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\bar{b} \times \bar{c} + \beta\bar{b}}{|\bar{b}|^2}$**

**Detailed Solution:**

Given $\bar{a} \times \bar{b} = \bar{c}$

Taking cross product with $\bar{b}$ on both sides from the left:

$\bar{b} \times (\bar{a} \times \bar{b}) = \bar{b} \times \bar{c}$

Using the vector triple product expansion $\bar{x} \times (\bar{y} \times \bar{z}) = (\bar{x} \cdot \bar{z})\bar{y} - (\bar{x} \cdot \bar{y})\bar{z}$:

$(\bar{b} \cdot \bar{b})\bar{a} - (\bar{b} \cdot \bar{a})\bar{b} = \bar{b} \times \bar{c}$

Substituting $\bar{b} \cdot \bar{b} = |\bar{b}|^2$ and $\bar{a} \cdot \bar{b} = \beta$:

$|\bar{b}|^2 \bar{a} - \beta \bar{b} = \bar{b} \times \bar{c}$

$|\bar{b}|^2 \bar{a} = \bar{b} \times \bar{c} + \beta \bar{b}$

$\bar{a} = \dfrac{\bar{b} \times \bar{c} + \beta \bar{b}}{|\bar{b}|^2}$

</details>

---

### Q18. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{u}, \bar{v}, \bar{w}$ be three vectors such that $|\bar{u}| = 1, |\bar{v}| = 2, |\bar{w}| = 3$. If the projection of $\bar{v}$ along $\bar{u}$ is equal to the projection of $\bar{w}$ along $\bar{u}$ and $\bar{v}, \bar{w}$ are perpendicular to each other, then $|\bar{u} - \bar{v} + \bar{w}| = $...

**Options:**

- **(A)** $4$
- **(B)** $\sqrt{7}$
- **(C)** $2$
- **(D)** $\sqrt{14}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{14}$**

**Detailed Solution:**

Given $|\vec{u}| = 1$, $|\vec{v}| = 2$, and $|\vec{w}| = 3$.

The projection of $\vec{v}$ along $\vec{u}$ is equal to the projection of $\vec{w}$ along $\vec{u}$.

$\dfrac{\vec{v} \cdot \vec{u}}{|\vec{u}|} = \dfrac{\vec{w} \cdot \vec{u}}{|\vec{u}|}$

$\vec{v} \cdot \vec{u} = \vec{w} \cdot \vec{u}$

Since $\vec{v}$ and $\vec{w}$ are perpendicular to each other, their dot product is zero:

$\vec{v} \cdot \vec{w} = 0$

We need to find the value of $|\vec{u} - \vec{v} + \vec{w}|$. Consider its square:

$|\vec{u} - \vec{v} + \vec{w}|^2 = |\vec{u}|^2 + |-\vec{v}|^2 + |\vec{w}|^2 + 2(\vec{u} \cdot (-\vec{v})) + 2((-\vec{v}) \cdot \vec{w}) + 2(\vec{u} \cdot \vec{w})$

$|\vec{u} - \vec{v} + \vec{w}|^2 = |\vec{u}|^2 + |\vec{v}|^2 + |\vec{w}|^2 - 2(\vec{u} \cdot \vec{v}) - 2(\vec{v} \cdot \vec{w}) + 2(\vec{u} \cdot \vec{w})$

Substituting $\vec{u} \cdot \vec{v} = \vec{u} \cdot \vec{w}$ and $\vec{v} \cdot \vec{w} = 0$ into the expansion:

$|\vec{u} - \vec{v} + \vec{w}|^2 = |\vec{u}|^2 + |\vec{v}|^2 + |\vec{w}|^2 - 2(\vec{u} \cdot \vec{w}) - 2(0) + 2(\vec{u} \cdot \vec{w})$

$|\vec{u} - \vec{v} + \vec{w}|^2 = |\vec{u}|^2 + |\vec{v}|^2 + |\vec{w}|^2$

Substituting the given magnitudes:

$|\vec{u} - \vec{v} + \vec{w}|^2 = (1)^2 + (2)^2 + (3)^2$

$|\vec{u} - \vec{v} + \vec{w}|^2 = 1 + 4 + 9 = 14$

Taking the square root on both sides:

$|\vec{u} - \vec{v} + \vec{w}| = \sqrt{14}$

</details>

---

### Q19. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $|\vec{a} \cdot \vec{b}| = |\vec{a} \times \vec{b}|$, $\vec{a} \cdot \vec{b} < 0$ and $\theta$ is the angle between $\vec{a}$ and $\vec{b}$, then the value of $\sin\theta + \tan\theta$ is...

**Options:**

- **(A)** $\dfrac{\sqrt{2} - 2}{2}$
- **(B)** $\dfrac{\sqrt{2} + 2}{2}$
- **(C)** $\dfrac{1 + \sqrt{2}}{2}$
- **(D)** $\dfrac{2 - \sqrt{2}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\sqrt{2} - 2}{2}$**

**Detailed Solution:**

Given $|\vec{a} \cdot \vec{b}| = |\vec{a} \times \vec{b}|$

$||\vec{a}| |\vec{b}| \cos\theta| = ||\vec{a}| |\vec{b}| \sin\theta|$

$|\cos\theta| = \sin\theta$ (since $\theta \in [0, \pi]$, $\sin\theta \ge 0$)

Also given $\vec{a} \cdot \vec{b} < 0$, which implies $\cos\theta < 0$.

Therefore, $|\cos\theta| = -\cos\theta$.

$-\cos\theta = \sin\theta \Rightarrow \tan\theta = -1$

Since $\theta \in [0, \pi]$, $\theta = \dfrac{3\pi}{4}$.

Now, $\sin\theta + \tan\theta = \sin\left(\dfrac{3\pi}{4}\right) + \tan\left(\dfrac{3\pi}{4}\right)$

$= \dfrac{1}{\sqrt{2}} - 1 = \dfrac{\sqrt{2} - 2}{2}$

Answer: $\dfrac{\sqrt{2} - 2}{2}$

</details>

---

### Q20. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle OAB$, $O(0,0,0),\ A(6,2,-3)$ and $B(4,0,3)$ are the vertices. Let $\vec{a}$ and $\vec{b}$ be position vectors of points $A$ and $B$ respectively and $OM$ is the projection of $\vec{a}$ on $\vec{b}$ then $l(AM)$ is equal to...

**Options:**

- **(A)** $\sqrt{10}\ units$
- **(B)** $2\sqrt{10}\ units$
- **(C)** $10\ units$
- **(D)** $40\ units$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2\sqrt{10}\ units$**

**Detailed Solution:**

Given position vectors $\vec{a} = 6\hat{i} + 2\hat{j} - 3\hat{k}$ and $\vec{b} = 4\hat{i} + 3\hat{k}$.

The magnitude of $\vec{a}$ is:

$|\vec{a}| = \sqrt{6^2 + 2^2 + (-3)^2} = \sqrt{36 + 4 + 9} = \sqrt{49} = 7$

The magnitude of $\vec{b}$ is:

$|\vec{b}| = \sqrt{4^2 + 0^2 + 3^2} = \sqrt{16 + 0 + 9} = \sqrt{25} = 5$

The length of the projection of $\vec{a}$ on $\vec{b}$ is $OM$, which is given by:

$OM = \dfrac{\vec{a} \cdot \vec{b}}{|\vec{b}|}$

Calculating the dot product:

$\vec{a} \cdot \vec{b} = (6)(4) + (2)(0) + (-3)(3) = 24 + 0 - 9 = 15$

Substituting the values to find $OM$:

$OM = \dfrac{15}{5} = 3$

In the right-angled $\triangle OAM$, $OA$ is the hypotenuse with length $|\vec{a}|$. Using the Pythagoras theorem:

$OA^2 = OM^2 + AM^2$

$7^2 = 3^2 + AM^2$

$49 = 9 + AM^2$

$AM^2 = 40$

$AM = \sqrt{40} = 2\sqrt{10}\ units$

Answer: $2\sqrt{10}\ units$

</details>

---

### Q21. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two adjacent sides of a parallelogram ABCD are given by $\overline{AB} = 2\hat{i} + 10\hat{j} + 11\hat{k}$ and $\overline{AD} = -\hat{i} + 2\hat{j} + 2\hat{k}$. The side AD is rotated by an acute angle $\alpha$ in the plane of the parallelogram so that AD becomes AD'. If AD' makes a right angle with the side AB, then the cosine of the angle $\alpha$ is given by

**Options:**

- **(A)** $\dfrac{8}{9}$
- **(B)** $\dfrac{\sqrt{17}}{9}$
- **(C)** $\dfrac{1}{9}$
- **(D)** $\dfrac{4\sqrt{5}}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\sqrt{17}}{9}$**

**Detailed Solution:**

Let $\theta$ be the angle between the vectors $\overrightarrow{AB}$ and $\overrightarrow{AD}$.

Using the dot product formula, we have:
$\cos \theta = \dfrac{\overrightarrow{AB} \cdot \overrightarrow{AD}}{|\overrightarrow{AB}| |\overrightarrow{AD}|}$

Given $\overrightarrow{AB} = 2\hat{i} + 10\hat{j} + 11\hat{k}$ and $\overrightarrow{AD} = -\hat{i} + 2\hat{j} + 2\hat{k}$, we calculate the dot product:
$\overrightarrow{AB} \cdot \overrightarrow{AD} = (2)(-1) + (10)(2) + (11)(2) = -2 + 20 + 22 = 40$

Now, we find the magnitudes of the vectors:
$|\overrightarrow{AB}| = \sqrt{2^2 + 10^2 + 11^2} = \sqrt{4 + 100 + 121} = \sqrt{225} = 15$
$|\overrightarrow{AD}| = \sqrt{(-1)^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$

Substituting these values into the cosine formula:
$\cos \theta = \dfrac{40}{15 \times 3} = \dfrac{40}{45} = \dfrac{8}{9}$

Since $\cos \theta > 0$, the angle $\theta$ is acute. The side AD is rotated by an acute angle $\alpha$ in the plane of the parallelogram to become AD', which is perpendicular to AB. This means the angle between AB and AD' is $90^{\circ}$.

Since both $\theta$ and $\alpha$ are acute, the rotation must satisfy:
$\theta + \alpha = 90^{\circ} \Rightarrow \alpha = 90^{\circ} - \theta$

We need to find $\cos \alpha$:
$\cos \alpha = \cos(90^{\circ} - \theta) = \sin \theta$

Using the identity $\sin \theta = \sqrt{1 - \cos^2 \theta}$:
$\cos \alpha = \sqrt{1 - \left(\dfrac{8}{9}\right)^2} = \sqrt{1 - \dfrac{64}{81}} = \sqrt{\dfrac{17}{81}} = \dfrac{\sqrt{17}}{9}$

Answer: $\dfrac{\sqrt{17}}{9}$

</details>

---

### Q22. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of a line in cartesian form passing through (0, 0, 0) and (4, 3, c) and parallel to $\vec{a} \times \vec{b}$ where $\vec{a} = 2\hat{i} + \hat{j} + 2\hat{k}$, $\vec{b} = 3\hat{i} - 4\hat{j}$ is

**Options:**

- **(A)** $\dfrac{x-4}{8} = \dfrac{y-3}{6} = \dfrac{z + \frac{11}{2}}{11}$
- **(B)** $\dfrac{x-4}{8} = \dfrac{y+3}{6} = \dfrac{z + \frac{11}{2}}{-11}$
- **(C)** $\dfrac{x-4}{8} = \dfrac{y-3}{6} = \dfrac{z + \frac{11}{2}}{-11}$
- **(D)** $\dfrac{x+4}{8} = \dfrac{y-3}{6} = \dfrac{z + \frac{11}{2}}{-11}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{x-4}{8} = \dfrac{y-3}{6} = \dfrac{z + \frac{11}{2}}{-11}$**

**Detailed Solution:**

The direction vector of the line is parallel to $\vec{a} \times \vec{b}$.

$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & 2 \\ 3 & -4 & 0 \end{vmatrix} = \hat{i}(0 - (-8)) - \hat{j}(0 - 6) + \hat{k}(-8 - 3) = 8\hat{i} + 6\hat{j} - 11\hat{k}$

The direction ratios of the line are proportional to $8, 6, -11$.

The line passes through $(0, 0, 0)$ and $(4, 3, c)$. Its direction ratios are $4 - 0, 3 - 0, c - 0$, which is $4, 3, c$.

Since the line is parallel to $\vec{a} \times \vec{b}$, the direction ratios must be proportional:

$\dfrac{4}{8} = \dfrac{3}{6} = \dfrac{c}{-11}$

$\dfrac{1}{2} = \dfrac{c}{-11} \Rightarrow c = -\dfrac{11}{2}$

The line passes through the point $(4, 3, c) = \left(4, 3, -\dfrac{11}{2}\right)$.

The equation of the line in Cartesian form is:

$\dfrac{x - 4}{8} = \dfrac{y - 3}{6} = \dfrac{z - \left(-\dfrac{11}{2}\right)}{-11}$

$\dfrac{x - 4}{8} = \dfrac{y - 3}{6} = \dfrac{z + \dfrac{11}{2}}{-11}$

Answer: $\dfrac{x-4}{8} = \dfrac{y-3}{6} = \dfrac{z + \frac{11}{2}}{-11}$

</details>

---

### Q23. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}, \bar{b}$ and $\bar{c}$ be three coplanar unit vectors. A unit vector $\bar{d}$ is perpendicular to them. If $(\bar{a} \times \bar{b}) \times (\bar{c} \times \bar{d}) = \dfrac{3}{26}\hat{i} - \dfrac{2}{13}\hat{j} + \dfrac{6}{13}\hat{k}$ and the angle between $\bar{a}$ and $\bar{b}$ is $30^\circ$, then $\bar{c}$ is equal to...

**Options:**

- **(A)** $\dfrac{3}{13}\hat{i} - \dfrac{4}{13}\hat{j} + \dfrac{12}{13}\hat{k}$
- **(B)** $\dfrac{3}{13}\hat{i} - \dfrac{2}{13}\hat{j} + \dfrac{6}{13}\hat{k}$
- **(C)** $\dfrac{3}{26}\hat{i} - \dfrac{4}{13}\hat{j} + \dfrac{12}{13}\hat{k}$
- **(D)** $\dfrac{3}{26}\hat{i} - \dfrac{3}{26}\hat{j} + \dfrac{5}{26}\hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{3}{13}\hat{i} - \dfrac{4}{13}\hat{j} + \dfrac{12}{13}\hat{k}$**

**Detailed Solution:**

Using the vector quadruple product expansion:

$(\bar{a} \times \bar{b}) \times (\bar{c} \times \bar{d}) = [\bar{a} \bar{b} \bar{d}]\bar{c} - [\bar{a} \bar{b} \bar{c}]\bar{d}$

Since $\bar{a}, \bar{b}, \bar{c}$ are coplanar, their scalar triple product $[\bar{a} \bar{b} \bar{c}] = 0$.

Thus, the expression simplifies to $[\bar{a} \bar{b} \bar{d}]\bar{c}$.

The scalar triple product is $[\bar{a} \bar{b} \bar{d}] = (\bar{a} \times \bar{b}) \cdot \bar{d}$.

Since $\bar{d}$ is perpendicular to the coplanar vectors $\bar{a}$ and $\bar{b}$, the vector $\bar{a} \times \bar{b}$ is parallel to $\bar{d}$.

The magnitude of $\bar{a} \times \bar{b}$ is given by $|\bar{a}| |\bar{b}| \sin 30^\circ = 1 \times 1 \times \dfrac{1}{2} = \dfrac{1}{2}$.

Since $\bar{d}$ is a unit vector, $(\bar{a} \times \bar{b}) \cdot \bar{d} = \pm |\bar{a} \times \bar{b}| |\bar{d}| = \pm \dfrac{1}{2}$.

Therefore, $\pm \dfrac{1}{2} \bar{c} = \dfrac{3}{26}\hat{i} - \dfrac{2}{13}\hat{j} + \dfrac{6}{13}\hat{k}$.

Multiplying by $\pm 2$ yields:

$\bar{c} = \pm \left( \dfrac{3}{13}\hat{i} - \dfrac{4}{13}\hat{j} + \dfrac{12}{13}\hat{k} \right)$

Taking the positive sign gives the matching option.

Answer: $\dfrac{3}{13}\hat{i} - \dfrac{4}{13}\hat{j} + \dfrac{12}{13}\hat{k}$

</details>

---

### Q24. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a} = \hat{i} + \hat{j}$, $\bar{c} = \hat{i} - \hat{j}$ and a vector $\bar{b}$ be such that $\bar{a} \times \bar{b} = \bar{c}$ and $\bar{a} \cdot \bar{b} = 3$ then $|\bar{b}| =$

**Options:**

- **(A)** $\dfrac{11}{\sqrt{2}}$
- **(B)** $\dfrac{11}{\sqrt{3}}$
- **(C)** $\sqrt{\dfrac{11}{2}}$
- **(D)** $\sqrt{\dfrac{11}{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{\dfrac{11}{2}}$**

**Detailed Solution:**

Given $\bar{a} = \hat{i} + \hat{j}$ and $\bar{c} = \hat{i} - \hat{j}$.

$|\bar{a}|^2 = 1^2 + 1^2 = 2$

$|\bar{c}|^2 = 1^2 + (-1)^2 = 2$

Using Lagrange's identity:

$|\bar{a} \times \bar{b}|^2 + (\bar{a} \cdot \bar{b})^2 = |\bar{a}|^2 |\bar{b}|^2$

Substituting the given values $\bar{a} \times \bar{b} = \bar{c}$ and $\bar{a} \cdot \bar{b} = 3$:

$|\bar{c}|^2 + 3^2 = |\bar{a}|^2 |\bar{b}|^2$

$2 + 9 = 2 |\bar{b}|^2$

$11 = 2 |\bar{b}|^2$

$|\bar{b}| = \sqrt{\dfrac{11}{2}}$

Answer: $\sqrt{\dfrac{11}{2}}$

</details>

---

### Q25. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The acute angle between the vector $2\hat{i} + \hat{j} - 3\hat{k}$ and the plane containing the vectors $2\hat{i} + 3\hat{j} - \hat{k}$ and $\hat{i} - \hat{j} + 2\hat{k}$ is

**Options:**

- **(A)** $\sin^{-1}\left(\dfrac{4}{\sqrt{42}}\right)$
- **(B)** $\cos^{-1}\left(\dfrac{4}{\sqrt{42}}\right)$
- **(C)** $\sin^{-1}\left(\dfrac{3}{\sqrt{42}}\right)$
- **(D)** $\cos^{-1}\left(\dfrac{3}{\sqrt{42}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sin^{-1}\left(\dfrac{4}{\sqrt{42}}\right)$**

**Detailed Solution:**

Let $\vec{v} = 2\hat{i} + \hat{j} - 3\hat{k}$.

The normal to the plane containing $\vec{a} = 2\hat{i} + 3\hat{j} - \hat{k}$ and $\vec{b} = \hat{i} - \hat{j} + 2\hat{k}$ is given by $\vec{n} = \vec{a} \times \vec{b}$.

$\vec{n} = (2\hat{i} + 3\hat{j} - \hat{k}) \times (\hat{i} - \hat{j} + 2\hat{k}) = 5\hat{i} - 5\hat{j} - 5\hat{k}$

A vector parallel to the normal is $\vec{n}' = \hat{i} - \hat{j} - \hat{k}$.

The angle $\theta$ between the vector $\vec{v}$ and the plane is given by $\sin\theta = \dfrac{|\vec{v} \cdot \vec{n}'|}{|\vec{v}| |\vec{n}'|}$.

$\vec{v} \cdot \vec{n}' = (2)(1) + (1)(-1) + (-3)(-1) = 4$

$|\vec{v}| = \sqrt{2^2 + 1^2 + (-3)^2} = \sqrt{14}$

$|\vec{n}'| = \sqrt{1^2 + (-1)^2 + (-1)^2} = \sqrt{3}$

$\sin\theta = \dfrac{4}{\sqrt{14} \sqrt{3}} = \dfrac{4}{\sqrt{42}}$

$\theta = \sin^{-1}\left(\dfrac{4}{\sqrt{42}}\right)$

Answer: $\sin^{-1}\left(\dfrac{4}{\sqrt{42}}\right)$

</details>

---

### Q26. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A unit vector coplanar with $\hat{i} + \hat{j} + 2\hat{k}$ and $\hat{i} + 2\hat{j} + \hat{k}$ and perpendicular to $\hat{i} + \hat{j} + \hat{k}$ is

**Options:**

- **(A)** $\pm\dfrac{1}{\sqrt{3}}(\hat{i} + \hat{j} + \hat{k})$
- **(B)** $\pm\dfrac{1}{\sqrt{3}}(\hat{i} - \hat{j} + \hat{k})$
- **(C)** $\pm\dfrac{1}{\sqrt{2}}(\hat{j} - \hat{k})$
- **(D)** $\pm\dfrac{1}{\sqrt{2}}(\hat{j} + \hat{k})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\pm\dfrac{1}{\sqrt{2}}(\hat{j} - \hat{k})$**

**Detailed Solution:**

Let the required vector be $\vec{v} = x\hat{i} + y\hat{j} + z\hat{k}$.

Since $\vec{v}$ is coplanar with $\vec{a} = \hat{i} + \hat{j} + 2\hat{k}$ and $\vec{b} = \hat{i} + 2\hat{j} + \hat{k}$, it must be perpendicular to their cross product $\vec{a} \times \vec{b}$.

$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & 2 \\ 1 & 2 & 1 \end{vmatrix} = -3\hat{i} + \hat{j} + \hat{k}$

Thus, $\vec{v} \cdot (\vec{a} \times \vec{b}) = 0 \Rightarrow -3x + y + z = 0$

Also, $\vec{v}$ is perpendicular to $\vec{c} = \hat{i} + \hat{j} + \hat{k}$, so $\vec{v} \cdot \vec{c} = 0$.

$x + y + z = 0$

Subtracting the two equations gives $-4x = 0 \Rightarrow x = 0$.

Substituting $x = 0$ into $x + y + z = 0$ gives $y = -z$.

So the vector is of the form $\vec{v} = y\hat{j} - y\hat{k} = y(\hat{j} - \hat{k})$.

Since $\vec{v}$ is a unit vector, $|\vec{v}| = 1$.

$\sqrt{y^2 + (-y)^2} = 1 \Rightarrow \sqrt{2y^2} = 1 \Rightarrow y = \pm \dfrac{1}{\sqrt{2}}$

Therefore, the required unit vector is $\pm \dfrac{1}{\sqrt{2}}(\hat{j} - \hat{k})$.

Answer: $\pm\dfrac{1}{\sqrt{2}}(\hat{j} - \hat{k})$

</details>

---

### Q27. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The altitude of the parallelopiped, whose coterminous edges are the vectors $\vec{a} = \hat{i} + \hat{j} + \hat{k}$, $\vec{b} = 2\hat{i} + 4\hat{j} - \hat{k}$, $\vec{c} = \hat{i} + \hat{j} + 3\hat{k}$, where $\vec{a}$, $\vec{b}$ are the sides of the base of parallelopiped, is

**Options:**

- **(A)** $\dfrac{2\sqrt{2}}{\sqrt{19}}$ units
- **(B)** $\dfrac{\sqrt{2}}{\sqrt{19}}$ units
- **(C)** $\dfrac{\sqrt{19}}{\sqrt{2}}$ units
- **(D)** $\dfrac{\sqrt{19}}{2\sqrt{2}}$ units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2\sqrt{2}}{\sqrt{19}}$ units**

**Detailed Solution:**

The volume of the parallelepiped is given by the scalar triple product $V = |[\vec{a} \vec{b} \vec{c}]|$.

$V = \begin{vmatrix} 1 & 1 & 1 \\ 2 & 4 & -1 \\ 1 & 1 & 3 \end{vmatrix} = 1(12 + 1) - 1(6 + 1) + 1(2 - 4) = 13 - 7 - 2 = 4$

The area of the base formed by $\vec{a}$ and $\vec{b}$ is $A = |\vec{a} \times \vec{b}|$.

$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & 1 \\ 2 & 4 & -1 \end{vmatrix} = \hat{i}(-1 - 4) - \hat{j}(-1 - 2) + \hat{k}(4 - 2) = -5\hat{i} + 3\hat{j} + 2\hat{k}$

$A = \sqrt{(-5)^2 + 3^2 + 2^2} = \sqrt{25 + 9 + 4} = \sqrt{38}$

The altitude $h$ of the parallelepiped is the ratio of the volume to the area of the base.

$h = \dfrac{V}{A} = \dfrac{4}{\sqrt{38}} = \dfrac{4}{\sqrt{2}\sqrt{19}} = \dfrac{2\sqrt{2}}{\sqrt{19}}$ units

</details>

---

### Q28. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let ABCD be a quadrilateral with $\overline{AB} = \vec{a}$, $\overline{AD} = \vec{b}$ and $\overline{AC} = 3\vec{a} + 2\vec{b}$. If its area is $\alpha$ times the area of the parallelogram with AB, AD as adjacent sides, then the value of $\alpha$ is equal to

**Options:**

- **(A)** $\dfrac{3}{2}$
- **(B)** $\dfrac{5}{2}$
- **(C)** $\dfrac{1}{2}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{5}{2}$**

**Detailed Solution:**

The area of the parallelogram with adjacent sides $\overrightarrow{AB}$ and $\overrightarrow{AD}$ is given by:

$\Delta_1 = |\overrightarrow{AB} \times \overrightarrow{AD}| = |\vec{a} \times \vec{b}|$

The area of the quadrilateral $ABCD$ can be calculated using its diagonals $\overrightarrow{AC}$ and $\overrightarrow{BD}$:

$\Delta_2 = \dfrac{1}{2} |\overrightarrow{AC} \times \overrightarrow{BD}|$

The diagonal vector $\overrightarrow{BD}$ is:

$\overrightarrow{BD} = \overrightarrow{AD} - \overrightarrow{AB} = \vec{b} - \vec{a}$

Taking the cross product of the diagonals:

$\overrightarrow{AC} \times \overrightarrow{BD} = (3\vec{a} + 2\vec{b}) \times (\vec{b} - \vec{a})$

$\overrightarrow{AC} \times \overrightarrow{BD} = 3(\vec{a} \times \vec{b}) - 3(\vec{a} \times \vec{a}) + 2(\vec{b} \times \vec{b}) - 2(\vec{b} \times \vec{a})$

Since $\vec{a} \times \vec{a} = \vec{0}$, $\vec{b} \times \vec{b} = \vec{0}$, and $\vec{b} \times \vec{a} = -(\vec{a} \times \vec{b})$:

$\overrightarrow{AC} \times \overrightarrow{BD} = 3(\vec{a} \times \vec{b}) - \vec{0} + \vec{0} + 2(\vec{a} \times \vec{b}) = 5(\vec{a} \times \vec{b})$

Substituting this back into the area formula for the quadrilateral:

$\Delta_2 = \dfrac{1}{2} |5(\vec{a} \times \vec{b})| = \dfrac{5}{2} |\vec{a} \times \vec{b}|$

Given that $\Delta_2 = \alpha \Delta_1$:

$\dfrac{5}{2} |\vec{a} \times \vec{b}| = \alpha |\vec{a} \times \vec{b}|$

$\alpha = \dfrac{5}{2}$

</details>

---

### Q29. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a} = \hat{i} + 2\hat{j} - 2\hat{k}$ and $\vec{b} = \hat{i} - \hat{j} + \hat{k}$. If $\vec{c}$ is a vector such that $\vec{a} \cdot \vec{c} = |\vec{c}|$, $|\vec{c} - \vec{a}| = 2\sqrt{2}$ and the angle between $\vec{a} \times \vec{b}$ and $\vec{c}$ is $60^\circ$, then $|(\vec{a} \times \vec{b}) \times \vec{c}|$ is equal to

**Options:**

- **(A)** $\dfrac{3\sqrt{3}}{2}$
- **(B)** $\sqrt{\dfrac{3}{2}}$
- **(C)** $3\sqrt{\dfrac{3}{2}}$
- **(D)** $\dfrac{9\sqrt{3}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3\sqrt{\dfrac{3}{2}}$**

**Detailed Solution:**

Given $\vec{a} = \hat{i} + 2\hat{j} - 2\hat{k}$ and $\vec{b} = \hat{i} - \hat{j} + \hat{k}$.

The magnitude of $\vec{a}$ is $|\vec{a}| = \sqrt{1^2 + 2^2 + (-2)^2} = 3$.

Squaring the given equation $|\vec{c} - \vec{a}| = 2\sqrt{2}$ yields:

$|\vec{c}|^2 + |\vec{a}|^2 - 2\vec{a} \cdot \vec{c} = 8$

Substituting $|\vec{a}| = 3$ and $\vec{a} \cdot \vec{c} = |\vec{c}|$:

$|\vec{c}|^2 + 9 - 2|\vec{c}| = 8$

$|\vec{c}|^2 - 2|\vec{c}| + 1 = 0$

$(|\vec{c}| - 1)^2 = 0 \Rightarrow |\vec{c}| = 1$

Calculating the cross product $\vec{a} \times \vec{b}$:

$\vec{a} \times \vec{b} = (\hat{i} + 2\hat{j} - 2\hat{k}) \times (\hat{i} - \hat{j} + \hat{k}) = -3\hat{j} - 3\hat{k}$

The magnitude is $|\vec{a} \times \vec{b}| = \sqrt{(-3)^2 + (-3)^2} = 3\sqrt{2}$.

The angle between $\vec{a} \times \vec{b}$ and $\vec{c}$ is $60^\circ$.

Using the definition of the cross product magnitude:

$|(\vec{a} \times \vec{b}) \times \vec{c}| = |\vec{a} \times \vec{b}| |\vec{c}| \sin 60^\circ$

$|(\vec{a} \times \vec{b}) \times \vec{c}| = (3\sqrt{2})(1)\left(\dfrac{\sqrt{3}}{2}\right) = \dfrac{3\sqrt{6}}{2} = 3\sqrt{\dfrac{3}{2}}$

Answer: $3\sqrt{\dfrac{3}{2}}$

</details>

---

### Q30. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}$ and $\bar{b}$ are unit vectors and $\theta$ ($0 < \theta < \pi$) is the angle between them, then the value of $\dfrac{|\bar{a} + \bar{b}|}{|\bar{a} - \bar{b}|}$ is equal to...

**Options:**

- **(A)** $\tan\dfrac{\theta}{2}$
- **(B)** $\sin\dfrac{\theta}{2}$
- **(C)** $\cos\dfrac{\theta}{2}$
- **(D)** $\cot\dfrac{\theta}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\cot\dfrac{\theta}{2}$**

**Detailed Solution:**

Given $|\bar{a}| = 1$ and $|\bar{b}| = 1$.

$|\bar{a} + \bar{b}|^2 = |\bar{a}|^2 + |\bar{b}|^2 + 2\bar{a}\cdot\bar{b} = 1 + 1 + 2\cos\theta = 2(1 + \cos\theta) = 4\cos^2\dfrac{\theta}{2}$

$|\bar{a} - \bar{b}|^2 = |\bar{a}|^2 + |\bar{b}|^2 - 2\bar{a}\cdot\bar{b} = 1 + 1 - 2\cos\theta = 2(1 - \cos\theta) = 4\sin^2\dfrac{\theta}{2}$

Taking the square root, since $0 < \theta < \pi$, we have $\cos\dfrac{\theta}{2} > 0$ and $\sin\dfrac{\theta}{2} > 0$:

$|\bar{a} + \bar{b}| = 2\cos\dfrac{\theta}{2}$

$|\bar{a} - \bar{b}| = 2\sin\dfrac{\theta}{2}$

$\dfrac{|\bar{a} + \bar{b}|}{|\bar{a} - \bar{b}|} = \dfrac{2\cos\dfrac{\theta}{2}}{2\sin\dfrac{\theta}{2}} = \cot\dfrac{\theta}{2}$

Answer: $\cot\dfrac{\theta}{2}$

</details>

---

### Q31. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a} = \hat{i} + \hat{j}$ and $\bar{b} = \hat{i} - \hat{k}$, then the point of intersection of the lines $\bar{r} \times \bar{a} = \bar{b} \times \bar{a}$ and $\bar{r} \times \bar{b} = \bar{a} \times \bar{b}$ is

**Options:**

- **(A)** $(2, 1, -1)$
- **(B)** $(2, -1, 1)$
- **(C)** $(0, 1, 1)$
- **(D)** $(0, -1, 1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(2, 1, -1)$**

**Detailed Solution:**

The given equations of the lines are $\bar{r} \times \bar{a} = \bar{b} \times \bar{a}$ and $\bar{r} \times \bar{b} = \bar{a} \times \bar{b}$.

From the first equation, we can write:
$\bar{r} \times \bar{a} - \bar{b} \times \bar{a} = 0$
$\Rightarrow (\bar{r} - \bar{b}) \times \bar{a} = 0$
This implies that the vector $\bar{r} - \bar{b}$ is parallel to $\bar{a}$. Thus, $\bar{r} = \bar{b} + \lambda \bar{a}$ for some scalar $\lambda$.

Similarly, from the second equation:
$\bar{r} \times \bar{b} - \bar{a} \times \bar{b} = 0$
$\Rightarrow (\bar{r} - \bar{a}) \times \bar{b} = 0$
This implies that the vector $\bar{r} - \bar{a}$ is parallel to $\bar{b}$. Thus, $\bar{r} = \bar{a} + \mu \bar{b}$ for some scalar $\mu$.

At the point of intersection, the position vector $\bar{r}$ must satisfy both conditions:
$\bar{b} + \lambda \bar{a} = \bar{a} + \mu \bar{b}$
$\Rightarrow (\lambda - 1)\bar{a} + (1 - \mu)\bar{b} = 0$

Since $\bar{a} = \hat{i} + \hat{j}$ and $\bar{b} = \hat{i} - \hat{k}$ are non-collinear (linearly independent) vectors, their coefficients must be zero:
$\lambda - 1 = 0 \Rightarrow \lambda = 1$
$1 - \mu = 0 \Rightarrow \mu = 1$

Substituting $\lambda = 1$ into the first equation for $\bar{r}$, we get:
$\bar{r} = \bar{a} + \bar{b}$

Substituting the given vectors $\bar{a}$ and $\bar{b}$:
$\bar{r} = (\hat{i} + \hat{j}) + (\hat{i} - \hat{k}) = 2\hat{i} + \hat{j} - \hat{k}$

Therefore, the point of intersection is $(2, 1, -1)$.

Answer: $(2, 1, -1)$

</details>

---

### Q32. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}$ and $\bar{b}$ have the same magnitude and angle between them is $60^\circ$ and their scalar product is $\dfrac{1}{2}$, then $|\bar{a}|$ is ____

**Options:**

- **(A)** $2$
- **(B)** $3$
- **(C)** $7$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1$**

**Detailed Solution:**

Let $|\bar{a}| = |\bar{b}| = x$.

The scalar product of two vectors is given by $\bar{a} \cdot \bar{b} = |\bar{a}| |\bar{b}| \cos \theta$.

Substituting the given values:

$\dfrac{1}{2} = x^2 \cos 60^\circ$

$\dfrac{1}{2} = x^2 \left(\dfrac{1}{2}\right)$

$x^2 = 1$

Since magnitude cannot be negative, $x = 1$.

Therefore, $|\bar{a}| = 1$.

</details>

---

### Q33. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}, \bar{b}, \bar{c}$ be the unit vectors such that $\bar{a}$ is perpendicular to $\bar{b}$ and the angle between $\bar{b}$ and $\bar{c}$ is $120^\circ$. If $\bar{a} + \bar{c}$ is perpendicular to $\bar{b} + \bar{c}$ then

**Options:**

- **(A)** $(\bar{a} + \bar{c}) \cdot (\bar{b} - \bar{c}) = 1$
- **(B)** $(\bar{a} - \bar{c}) \cdot (\bar{b} - \bar{c}) = -2$
- **(C)** $(\bar{a} - \bar{c}) \cdot (\bar{b} + \bar{c}) = 1$
- **(D)** $(\bar{a} - \bar{c}) \cdot (\bar{b} - \bar{c}) = 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\bar{a} - \bar{c}) \cdot (\bar{b} - \bar{c}) = 2$**

**Detailed Solution:**

Given $|\bar{a}| = |\bar{b}| = |\bar{c}| = 1$

$\bar{a} \cdot \bar{b} = 0$

$\bar{b} \cdot \bar{c} = |\bar{b}||\bar{c}|\cos 120^\circ = -\dfrac{1}{2}$

Since $\bar{a} + \bar{c}$ is perpendicular to $\bar{b} + \bar{c}$, we have:

$(\bar{a} + \bar{c}) \cdot (\bar{b} + \bar{c}) = 0$

$\bar{a} \cdot \bar{b} + \bar{a} \cdot \bar{c} + \bar{c} \cdot \bar{b} + |\bar{c}|^2 = 0$

$0 + \bar{a} \cdot \bar{c} - \dfrac{1}{2} + 1 = 0$

$\bar{a} \cdot \bar{c} = -\dfrac{1}{2}$

Now, evaluating the expression in the options:

$(\bar{a} - \bar{c}) \cdot (\bar{b} - \bar{c}) = \bar{a} \cdot \bar{b} - \bar{a} \cdot \bar{c} - \bar{c} \cdot \bar{b} + |\bar{c}|^2$

$= 0 - \left(-\dfrac{1}{2}\right) - \left(-\dfrac{1}{2}\right) + 1$

$= \dfrac{1}{2} + \dfrac{1}{2} + 1 = 2$

</details>

---

### Q34. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two adjacent sides of a parallelogram ABCD are given by $\overline{\mathrm{AB}}=2 \hat{i}+10 \hat{j}+11 \hat{k}$ and $\overline{\mathrm{AD}}=-\hat{i}+2 \hat{j}+2 \hat{k}$. The side AD is rotated by an acute angle $\alpha$ in the plane of parallelogram so that AD becomes $\mathrm{AD}^{\prime}$. If $\mathrm{AD}^{\prime}$ makes a right angle with the side AB then $\cos \alpha=$

**Options:**

- **(A)** $\frac{\sqrt{17}}{8}$
- **(B)** $\frac{\sqrt{17}}{9}$
- **(C)** $\frac{\sqrt{17}}{13}$
- **(D)** $\frac{\sqrt{17}}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\sqrt{17}}{9}$**

**Detailed Solution:**

Let $\theta$ be the angle between the vectors $\overline{\mathrm{AB}}$ and $\overline{\mathrm{AD}}$.

$\cos \theta = \dfrac{\overline{\mathrm{AB}} \cdot \overline{\mathrm{AD}}}{|\overline{\mathrm{AB}}| |\overline{\mathrm{AD}}|}$

We calculate the dot product and the magnitudes of the vectors:

$\overline{\mathrm{AB}} \cdot \overline{\mathrm{AD}} = (2)(-1) + (10)(2) + (11)(2) = -2 + 20 + 22 = 40$

$|\overline{\mathrm{AB}}| = \sqrt{2^2 + 10^2 + 11^2} = \sqrt{4 + 100 + 121} = \sqrt{225} = 15$

$|\overline{\mathrm{AD}}| = \sqrt{(-1)^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$

Substituting these values, we get:

$\cos \theta = \dfrac{40}{15 \times 3} = \dfrac{40}{45} = \dfrac{8}{9}$

Since $\cos \theta > 0$, $\theta$ is an acute angle.

The vector $\overline{\mathrm{AD}}$ is rotated by an acute angle $\alpha$ in the plane of the parallelogram to become $\mathrm{AD}^{\prime}$, which is perpendicular to $\overline{\mathrm{AB}}$.

Thus, the angle between $\overline{\mathrm{AB}}$ and $\mathrm{AD}^{\prime}$ is $90^{\circ}$. Since the rotation is in the plane of the parallelogram and both $\theta$ and $\alpha$ are acute, we must have:

$\theta + \alpha = 90^{\circ}$

$\alpha = 90^{\circ} - \theta$

Taking cosine on both sides:

$\cos \alpha = \cos(90^{\circ} - \theta) = \sin \theta$

Using the identity $\sin \theta = \sqrt{1 - \cos^2 \theta}$:

$\cos \alpha = \sqrt{1 - \left(\dfrac{8}{9}\right)^2} = \sqrt{1 - \dfrac{64}{81}} = \sqrt{\dfrac{17}{81}} = \dfrac{\sqrt{17}}{9}$

Answer: $\frac{\sqrt{17}}{9}$

</details>

---

### Q35. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{a}}=\frac{1}{\sqrt{10}}(3 \hat{i}+\hat{\mathrm{k}}), \overline{\mathrm{b}}=\frac{1}{7}(2 \hat{i}+3 \hat{\mathrm{j}}-6 \hat{\mathrm{k}})$, then the value of $(\overline{\mathrm{a}}-2 \overline{\mathrm{~b}}) \cdot\{(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times(2 \overline{\mathrm{a}}+\overline{\mathrm{b}})\}$ is

**Options:**

- **(A)** 5
- **(B)** -5
- **(C)** 3
- **(D)** -3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -5**

**Detailed Solution:**

Given vectors:
$\vec{a} = \dfrac{1}{\sqrt{10}}(3\hat{i} + \hat{k})$
$\vec{b} = \dfrac{1}{7}(2\hat{i} + 3\hat{j} - 6\hat{k})$

Calculating their magnitudes squared and dot product:
$|\vec{a}|^2 = \dfrac{1}{10}(3^2 + 1^2) = 1$
$|\vec{b}|^2 = \dfrac{1}{49}(2^2 + 3^2 + (-6)^2) = 1$
$\vec{a} \cdot \vec{b} = \dfrac{1}{7\sqrt{10}}(3 \times 2 + 0 \times 3 + 1 \times (-6)) = 0$

Using the vector triple product formula $(\vec{A} \times \vec{B}) \times \vec{C} = (\vec{A} \cdot \vec{C})\vec{B} - (\vec{B} \cdot \vec{C})\vec{A}$, we expand the second part of the expression:
$(\vec{a} \times \vec{b}) \times (2\vec{a} + \vec{b}) = (\vec{a} \cdot (2\vec{a} + \vec{b}))\vec{b} - (\vec{b} \cdot (2\vec{a} + \vec{b}))\vec{a}$

Expanding the dot products:
$= (2|\vec{a}|^2 + \vec{a} \cdot \vec{b})\vec{b} - (2\vec{a} \cdot \vec{b} + |\vec{b}|^2)\vec{a}$

Substituting $|\vec{a}|^2 = 1$, $|\vec{b}|^2 = 1$, and $\vec{a} \cdot \vec{b} = 0$:
$= (2(1) + 0)\vec{b} - (2(0) + 1)\vec{a} = 2\vec{b} - \vec{a}$

Now, substituting this back into the original expression:
$(\vec{a} - 2\vec{b}) \cdot \{(\vec{a} \times \vec{b}) \times (2\vec{a} + \vec{b})\} = (\vec{a} - 2\vec{b}) \cdot (2\vec{b} - \vec{a})$

Taking the negative sign out:
$= -(\vec{a} - 2\vec{b}) \cdot (\vec{a} - 2\vec{b})$
$= -|\vec{a} - 2\vec{b}|^2$

Expanding the magnitude squared:
$= -(|\vec{a}|^2 - 4\vec{a} \cdot \vec{b} + 4|\vec{b}|^2)$
$= -(1 - 0 + 4(1))$
$= -5$

Answer: -5

</details>

---

### Q36. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\bar{a}, \overline{\mathrm{~b}}, \overline{\mathrm{c}}$ are perpendicular to $\overline{\mathrm{b}}+\overline{\mathrm{c}}, \quad \bar{c}+\bar{a}$ and $\bar{a}+\overline{\mathrm{b}}$ respectively and $|\bar{a}+\bar{b}|=4,|\bar{b}+\bar{c}|=2 \sqrt{6},|\bar{c}+\bar{a}|=4$, then $|\bar{a}+\bar{b}+\bar{c}|=$

**Options:**

- **(A)** $2 \sqrt{7}$
- **(B)** $2 \sqrt{6}$
- **(C)** $3 \sqrt{6}$
- **(D)** $3 \sqrt{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \sqrt{7}$**

**Detailed Solution:**

Given that $\bar{a}$ is perpendicular to $\bar{b}+\bar{c}$, we have:

$\bar{a} \cdot (\bar{b}+\bar{c}) = 0 \Rightarrow \bar{a} \cdot \bar{b} + \bar{a} \cdot \bar{c} = 0$

Similarly, for the other vectors:

$\bar{b} \cdot (\bar{c}+\bar{a}) = 0 \Rightarrow \bar{b} \cdot \bar{c} + \bar{a} \cdot \bar{b} = 0$

$\bar{c} \cdot (\bar{a}+\bar{b}) = 0 \Rightarrow \bar{a} \cdot \bar{c} + \bar{b} \cdot \bar{c} = 0$

Adding the above three equations, we get:

$2(\bar{a} \cdot \bar{b} + \bar{b} \cdot \bar{c} + \bar{a} \cdot \bar{c}) = 0 \Rightarrow \bar{a} \cdot \bar{b} + \bar{b} \cdot \bar{c} + \bar{a} \cdot \bar{c} = 0$

This implies $\bar{a} \cdot \bar{b} = \bar{b} \cdot \bar{c} = \bar{a} \cdot \bar{c} = 0$.

Using the given magnitudes:

$|\bar{a}+\bar{b}|^2 = |\bar{a}|^2 + |\bar{b}|^2 + 2\bar{a} \cdot \bar{b} = |\bar{a}|^2 + |\bar{b}|^2 = 16$

$|\bar{b}+\bar{c}|^2 = |\bar{b}|^2 + |\bar{c}|^2 + 2\bar{b} \cdot \bar{c} = |\bar{b}|^2 + |\bar{c}|^2 = 24$

$|\bar{c}+\bar{a}|^2 = |\bar{c}|^2 + |\bar{a}|^2 + 2\bar{c} \cdot \bar{a} = |\bar{c}|^2 + |\bar{a}|^2 = 16$

Adding these three equations yields:

$2(|\bar{a}|^2 + |\bar{b}|^2 + |\bar{c}|^2) = 16 + 24 + 16 = 56$

$|\bar{a}|^2 + |\bar{b}|^2 + |\bar{c}|^2 = 28$

Now, expanding $|\bar{a}+\bar{b}+\bar{c}|^2$:

$|\bar{a}+\bar{b}+\bar{c}|^2 = |\bar{a}|^2 + |\bar{b}|^2 + |\bar{c}|^2 + 2(\bar{a} \cdot \bar{b} + \bar{b} \cdot \bar{c} + \bar{a} \cdot \bar{c})$

$|\bar{a}+\bar{b}+\bar{c}|^2 = 28 + 0 = 28$

$|\bar{a}+\bar{b}+\bar{c}| = \sqrt{28} = 2\sqrt{7}$

Answer: $2 \sqrt{7}$

</details>

---

### Q37. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\bar{a}=\hat{i}+2 \hat{\mathrm{j}}-2 \hat{\mathrm{k}}$ and $\overline{\mathrm{b}}=\hat{i}-\hat{\mathrm{j}}+\hat{\mathrm{k}}$. If $\overline{\mathrm{c}}$ is a vector such that $\bar{a} \cdot \overline{\mathrm{c}}=|\overline{\mathrm{c}}|$, $|\overline{\mathrm{c}}-\bar{a}|=2 \sqrt{2}$ and the angle between $\overline{\mathrm{a}} \times \overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ is $60^{\circ}$, then $|(\bar{a} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}|$ is equal to

**Options:**

- **(A)** $\frac{3\sqrt{6}}{2}$
- **(B)** $\frac{3\sqrt{2}}{2}$
- **(C)** $\frac{3\sqrt{3}}{2}$
- **(D)** $\frac{\sqrt{6}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3\sqrt{6}}{2}$**

**Detailed Solution:**

Given $\bar{a} = \hat{i} + 2\hat{j} - 2\hat{k}$ and $\bar{b} = \hat{i} - \hat{j} + \hat{k}$.

The magnitude of $\bar{a}$ is:
$|\bar{a}| = \sqrt{1^2 + 2^2 + (-2)^2} = \sqrt{9} = 3$

We are given $|\bar{c} - \bar{a}| = 2\sqrt{2}$. Squaring both sides, we get:
$|\bar{c}|^2 + |\bar{a}|^2 - 2\bar{a} \cdot \bar{c} = 8$

Substituting $|\bar{a}| = 3$ and $\bar{a} \cdot \bar{c} = |\bar{c}|$:
$|\bar{c}|^2 + 9 - 2|\bar{c}| = 8$

$|\bar{c}|^2 - 2|\bar{c}| + 1 = 0$

$(|\bar{c}| - 1)^2 = 0 \Rightarrow |\bar{c}| = 1$

Now, calculating the cross product $\bar{a} \times \bar{b}$:
$\bar{a} \times \bar{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & -2 \\ 1 & -1 & 1 \end{vmatrix}$

$\bar{a} \times \bar{b} = \hat{i}(2 - 2) - \hat{j}(1 - (-2)) + \hat{k}(-1 - 2) = -3\hat{j} - 3\hat{k}$

The magnitude of $\bar{a} \times \bar{b}$ is:
$|\bar{a} \times \bar{b}| = \sqrt{0^2 + (-3)^2 + (-3)^2} = \sqrt{18} = 3\sqrt{2}$

The angle between $\bar{a} \times \bar{b}$ and $\bar{c}$ is $60^{\circ}$. The magnitude of their cross product is:
$|(\bar{a} \times \bar{b}) \times \bar{c}| = |\bar{a} \times \bar{b}| |\bar{c}| \sin 60^{\circ}$

$|(\bar{a} \times \bar{b}) \times \bar{c}| = (3\sqrt{2})(1)\left(\dfrac{\sqrt{3}}{2}\right) = \dfrac{3\sqrt{6}}{2}$

Answer: $\frac{3\sqrt{6}}{2}$

</details>

---

### Q38. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The values of $x$ for which the angle between the vectors $\bar{a}=2 x^2 \hat{i}+4 x \hat{\mathrm{j}}+\hat{\mathrm{k}}$ and $\overline{\mathrm{b}}=7 \hat{i}-2 \hat{\mathrm{j}}+x \hat{\mathrm{k}}$ is obtuse, are

**Options:**

- **(A)** $0 < x < \frac{1}{2}$
- **(B)** $1 < x < 2$
- **(C)** $1 \leqslant x \leqslant 2$
- **(D)** $-1 < x < 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0 < x < \frac{1}{2}$**

**Detailed Solution:**

The angle between two vectors $\bar{a}$ and $\bar{b}$ is obtuse if their dot product is strictly less than zero, i.e., $\bar{a} \cdot \bar{b} < 0$.

Given vectors are $\bar{a} = 2x^2 \hat{i} + 4x \hat{j} + \hat{k}$ and $\bar{b} = 7\hat{i} - 2\hat{j} + x\hat{k}$.

Taking the dot product:

$\bar{a} \cdot \bar{b} = (2x^2)(7) + (4x)(-2) + (1)(x)$

$\bar{a} \cdot \bar{b} = 14x^2 - 8x + x$

$\bar{a} \cdot \bar{b} = 14x^2 - 7x$

For the angle to be obtuse:

$14x^2 - 7x < 0$

$7x(2x - 1) < 0$

$x(2x - 1) < 0$

The roots of the corresponding equation are $x = 0$ and $x = \dfrac{1}{2}$.

The inequality holds for $0 < x < \dfrac{1}{2}$.

Answer: $0 < x < \frac{1}{2}$

</details>

---

### Q39. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The vectors $\bar{a}, \overline{\mathrm{~b}}$ and $\overline{\mathrm{c}}$ are such that $|\bar{a}|=2,|\overline{\mathrm{~b}}|=4,|\overline{\mathrm{c}}|=4$. If the projection of $\overline{\mathrm{b}}$ on $\bar{a}$ is equal to projection of $\overline{\mathrm{c}}$ on $\bar{a}$ and $\overline{\mathrm{b}}$ is perpendicular to $\overline{\mathrm{c}}$, then the value of $|\bar{a}+\overline{\mathrm{b}}-\overline{\mathrm{c}}|$ is

**Options:**

- **(A)** 5
- **(B)** 36
- **(C)** 6
- **(D)** 25

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 6**

**Detailed Solution:**

Given $|\bar{a}| = 2$, $|\bar{b}| = 4$, and $|\bar{c}| = 4$.

The projection of $\bar{b}$ on $\bar{a}$ is equal to the projection of $\bar{c}$ on $\bar{a}$.

$\dfrac{\bar{b} \cdot \bar{a}}{|\bar{a}|} = \dfrac{\bar{c} \cdot \bar{a}}{|\bar{a}|}$

$\bar{b} \cdot \bar{a} = \bar{c} \cdot \bar{a} \Rightarrow \bar{a} \cdot \bar{b} - \bar{a} \cdot \bar{c} = 0$

Since $\bar{b}$ is perpendicular to $\bar{c}$, we have $\bar{b} \cdot \bar{c} = 0$.

Now, consider the square of the required magnitude:

$|\bar{a} + \bar{b} - \bar{c}|^2 = |\bar{a}|^2 + |\bar{b}|^2 + |\bar{c}|^2 + 2(\bar{a} \cdot \bar{b}) - 2(\bar{a} \cdot \bar{c}) - 2(\bar{b} \cdot \bar{c})$

$|\bar{a} + \bar{b} - \bar{c}|^2 = |\bar{a}|^2 + |\bar{b}|^2 + |\bar{c}|^2 + 2(\bar{a} \cdot \bar{b} - \bar{a} \cdot \bar{c}) - 2(\bar{b} \cdot \bar{c})$

Substituting the known values:

$|\bar{a} + \bar{b} - \bar{c}|^2 = (2)^2 + (4)^2 + (4)^2 + 2(0) - 2(0)$

$|\bar{a} + \bar{b} - \bar{c}|^2 = 4 + 16 + 16 = 36$

Taking the square root on both sides:

$|\bar{a} + \bar{b} - \bar{c}| = 6$

Answer: 6

</details>

---

### Q40. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}, \overline{\mathrm{~b}}$ and $\overline{\mathrm{c}}$ be vectors of magnitude 2,3 and 4 respectively. If $\bar{a}$ is perpendicular to $(\overline{\mathrm{b}}+\overline{\mathrm{c}}), \overline{\mathrm{b}}$ is perpendicular to $(\overline{\mathrm{c}}+\bar{a})$ and $\overline{\mathrm{c}}$ is perpendicular to ( $\bar{a}+\bar{b}$ ), then the magnitude of $\bar{a}+\overline{\mathrm{b}}+\overline{\mathrm{c}}$ is

**Options:**

- **(A)** 29
- **(B)** $\sqrt{28}$
- **(C)** $\sqrt{29}$
- **(D)** 28

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{29}$**

**Detailed Solution:**

Given $|\vec{a}| = 2$, $|\vec{b}| = 3$, and $|\vec{c}| = 4$.

Since $\vec{a}$ is perpendicular to $(\vec{b} + \vec{c})$, we have:
$\vec{a} \cdot (\vec{b} + \vec{c}) = 0 \Rightarrow \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c} = 0$

Similarly, $\vec{b}$ is perpendicular to $(\vec{c} + \vec{a})$:
$\vec{b} \cdot (\vec{c} + \vec{a}) = 0 \Rightarrow \vec{b} \cdot \vec{c} + \vec{b} \cdot \vec{a} = 0$

And $\vec{c}$ is perpendicular to $(\vec{a} + \vec{b})$:
$\vec{c} \cdot (\vec{a} + \vec{b}) = 0 \Rightarrow \vec{c} \cdot \vec{a} + \vec{c} \cdot \vec{b} = 0$

Adding the above three equations, we get:
$2(\vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{c} + \vec{c} \cdot \vec{a}) = 0$

The magnitude of $\vec{a} + \vec{b} + \vec{c}$ is given by:
$|\vec{a} + \vec{b} + \vec{c}|^2 = |\vec{a}|^2 + |\vec{b}|^2 + |\vec{c}|^2 + 2(\vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{c} + \vec{c} \cdot \vec{a})$

Substituting the given values:
$|\vec{a} + \vec{b} + \vec{c}|^2 = 2^2 + 3^2 + 4^2 + 0$

$|\vec{a} + \vec{b} + \vec{c}|^2 = 4 + 9 + 16 = 29$

Taking the square root on both sides:
$|\vec{a} + \vec{b} + \vec{c}| = \sqrt{29}$

Answer: $\sqrt{29}$

</details>

---

### Q41. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}=\alpha \hat{i}+3 \hat{\mathrm{j}}-\hat{\mathrm{k}}, \overline{\mathrm{b}}=3 \hat{i}-\hat{\mathrm{j}}+\beta \hat{\mathrm{k}}$ and $\overline{\mathrm{c}}=\hat{i}+2 \hat{\mathrm{j}}-2 \hat{\mathrm{k}}$ where $\alpha, \beta \in \mathbb{R}$, be three vectors. If the projection of $\bar{a}$ on $\bar{c}$ is $\frac{10}{3}$ and $\overline{\mathrm{b}} \times \overline{\mathrm{c}}=-6 \hat{i}+10 \hat{\mathrm{j}}+7 \hat{\mathrm{k}}$, then the value of $(\alpha+\beta)$ is equal to

**Options:**

- **(A)** 5
- **(B)** 3
- **(C)** 4
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 6**

**Detailed Solution:**

The projection of $\bar{a}$ on $\bar{c}$ is given by $\dfrac{\bar{a} \cdot \bar{c}}{|\bar{c}|}$.

$\bar{a} \cdot \bar{c} = (\alpha)(1) + (3)(2) + (-1)(-2) = \alpha + 6 + 2 = \alpha + 8$

$|\bar{c}| = \sqrt{1^2 + 2^2 + (-2)^2} = \sqrt{1 + 4 + 4} = 3$

Given that the projection is $\dfrac{10}{3}$, we have:

$\dfrac{\alpha + 8}{3} = \dfrac{10}{3} \Rightarrow \alpha + 8 = 10 \Rightarrow \alpha = 2$

Next, we calculate the cross product $\bar{b} \times \bar{c}$:

$\bar{b} \times \bar{c} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 3 & -1 & \beta \\ 1 & 2 & -2 \end{vmatrix}$

$= \hat{i}((-1)(-2) - (\beta)(2)) - \hat{j}((3)(-2) - (\beta)(1)) + \hat{k}((3)(2) - (-1)(1))$

$= (2 - 2\beta)\hat{i} + (6 + \beta)\hat{j} + 7\hat{k}$

We are given that $\bar{b} \times \bar{c} = -6 \hat{i} + 10 \hat{j} + 7 \hat{k}$. Comparing the coefficients of $\hat{i}$ and $\hat{j}$:

$2 - 2\beta = -6 \Rightarrow 2\beta = 8 \Rightarrow \beta = 4$

$6 + \beta = 10 \Rightarrow \beta = 4$

Therefore, $\alpha = 2$ and $\beta = 4$.

The value of $(\alpha + \beta) = 2 + 4 = 6$.

Answer: 6

</details>

---

### Q42. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}=\hat{i}+\hat{\mathrm{j}}-\hat{\mathrm{k}}$ and $\bar{c}=5 \hat{i}-3 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}$ and if $\overline{\mathrm{b}} = \overline{\mathrm{c}} \times \bar{a}$ then $|\overline{\mathrm{b}}|=$

**Options:**

- **(A)** $\sqrt{113}$
- **(B)** $\sqrt{117}$
- **(C)** None of these
- **(D)** $\sqrt{114}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{114}$**

**Detailed Solution:**

Given vectors are $\bar{a} = \hat{i} + \hat{j} - \hat{k}$ and $\bar{c} = 5\hat{i} - 3\hat{j} + 2\hat{k}$.

We are given $\bar{b} = \bar{c} \times \bar{a}$.

$\bar{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 5 & -3 & 2 \\ 1 & 1 & -1 \end{vmatrix}$

Expanding the determinant, we get:

$\bar{b} = \hat{i}((-3)(-1) - (2)(1)) - \hat{j}((5)(-1) - (2)(1)) + \hat{k}((5)(1) - (-3)(1))$

$\bar{b} = \hat{i}(3 - 2) - \hat{j}(-5 - 2) + \hat{k}(5 + 3)$

$\bar{b} = \hat{i} + 7\hat{j} + 8\hat{k}$

The magnitude of $\bar{b}$ is:

$|\bar{b}| = \sqrt{1^2 + 7^2 + 8^2}$

$|\bar{b}| = \sqrt{1 + 49 + 64}$

$|\bar{b}| = \sqrt{114}$

Answer: $\sqrt{114}$

</details>

---

### Q43. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The altitude through vertex A of $\triangle \mathrm{ABC}$ with position vectors of points $\mathrm{A}, \mathrm{B}, \mathrm{C}$ as $\bar{a}, \overline{\mathrm{~b}}, \overline{\mathrm{c}}$ respectively is

**Options:**

- **(A)** $\frac{|\bar{b} \times \bar{c}|}{|\bar{c}-\bar{b}|}$
- **(B)** $\frac{|\bar{a} \times \bar{b}+\bar{b} \times \bar{c}+\bar{c} \times \bar{a}|}{|\bar{c}-\bar{b}|}$
- **(C)** $\frac{|\bar{a} \times \bar{b}+\bar{b} \times \bar{c}+\bar{c} \times \bar{a}|}{|\bar{c} \times \bar{b}|}$
- **(D)** $\frac{|\overline{\mathrm{b}} \times \overline{\mathrm{c}}|}{|\bar{a}|}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{|\bar{a} \times \bar{b}+\bar{b} \times \bar{c}+\bar{c} \times \bar{a}|}{|\bar{c}-\bar{b}|}$**

**Detailed Solution:**

The area of $\triangle \mathrm{ABC}$ is given by $\dfrac{1}{2} |\overrightarrow{AB} \times \overrightarrow{AC}|$.

The vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$ are:
$\overrightarrow{AB} = \bar{b} - \bar{a}$
$\overrightarrow{AC} = \bar{c} - \bar{a}$

Taking their cross product:
$\overrightarrow{AB} \times \overrightarrow{AC} = (\bar{b} - \bar{a}) \times (\bar{c} - \bar{a})$
$\overrightarrow{AB} \times \overrightarrow{AC} = \bar{b} \times \bar{c} - \bar{b} \times \bar{a} - \bar{a} \times \bar{c} + \bar{a} \times \bar{a}$

Since $\bar{a} \times \bar{a} = 0$, $\bar{b} \times \bar{a} = -\bar{a} \times \bar{b}$, and $\bar{a} \times \bar{c} = -\bar{c} \times \bar{a}$, we get:
$\overrightarrow{AB} \times \overrightarrow{AC} = \bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{c} \times \bar{a}$

Thus, the area of $\triangle \mathrm{ABC}$ is:
Area $= \dfrac{1}{2} |\bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{c} \times \bar{a}|$

Alternatively, the area of the triangle is also given by $\dfrac{1}{2} \times \text{base} \times \text{height}$.
Taking the base as the side $\mathrm{BC}$, its length is $|\overrightarrow{BC}| = |\bar{c} - \bar{b}|$.
Let $h$ be the altitude through vertex $\mathrm{A}$.

Area $= \dfrac{1}{2} |\bar{c} - \bar{b}| \times h$

Equating the two expressions for the area:
$\dfrac{1}{2} |\bar{c} - \bar{b}| \times h = \dfrac{1}{2} |\bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{c} \times \bar{a}|$

$h = \dfrac{|\bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{c} \times \bar{a}|}{|\bar{c} - \bar{b}|}$

Answer: $\frac{|\bar{a} \times \bar{b}+\bar{b} \times \bar{c}+\bar{c} \times \bar{a}|}{|\bar{c}-\bar{b}|}$

</details>

---

### Q44. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the vectors $\overline{\mathrm{a}}=\mathrm{c}\left(\log _7 x\right) \hat{i}+2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}$ and $\overline{\mathrm{b}}=\left(\log _7 x\right) \hat{i}+3 \mathrm{c}\left(\log _7 x\right) \hat{\mathrm{j}}-4 \hat{\mathrm{k}}$ make obtuse angle for any $x>0$, then c belongs to

**Options:**

- **(A)** $\left(0, \frac{3}{4}\right)$
- **(B)** $\left(\frac{-3}{4}, 0\right)$
- **(C)** $\left(\frac{-4}{3}, 0\right)$
- **(D)** $\left(0, \frac{4}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\frac{-4}{3}, 0\right)$**

**Detailed Solution:**

For the angle between the vectors $\vec{a}$ and $\vec{b}$ to be obtuse, their dot product must be strictly negative.

$\vec{a} \cdot \vec{b} < 0$

Substituting the given vectors:

$c(\log_7 x)^2 + 6c(\log_7 x) - 12 < 0$

Let $\log_7 x = t$. Since $x > 0$, $t \in \mathbb{R}$. The inequality becomes:

$ct^2 + 6ct - 12 < 0$

For a quadratic expression $At^2 + Bt + C < 0$ for all $t \in \mathbb{R}$, the conditions are $A < 0$ and discriminant $D < 0$.

Therefore, $c < 0$ and $D = (6c)^2 - 4(c)(-12) < 0$.

$36c^2 + 48c < 0$

$12c(3c + 4) < 0$

Since $c < 0$, we must have $3c + 4 > 0$, which gives:

$c > \dfrac{-4}{3}$

Combining the conditions, we get $c \in \left(\dfrac{-4}{3}, 0\right)$.

Answer: $\left(\frac{-4}{3}, 0\right)$

</details>

---

### Q45. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\theta$ is an obtuse angle between vector $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$ such that $|\overline{\mathrm{a}}|=5,|\overline{\mathrm{~b}}|=3$ and $|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|=5 \sqrt{5}$ then $\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}=$

**Options:**

- **(A)** $10$
- **(B)** $-10$
- **(C)** $5$
- **(D)** $-5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-10$**

**Detailed Solution:**

Using the identity $|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|^2 + (\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})^2 = |\overline{\mathrm{a}}|^2 |\overline{\mathrm{b}}|^2$

Substituting the given values:

$(5 \sqrt{5})^2 + (\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})^2 = (5)^2 (3)^2$

$125 + (\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})^2 = 225$

$(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})^2 = 100$

$\overline{\mathrm{a}} \cdot \overline{\mathrm{b}} = \pm 10$

Since $\theta$ is an obtuse angle, $\cos \theta < 0$, which implies $\overline{\mathrm{a}} \cdot \overline{\mathrm{b}} < 0$.

Therefore, $\overline{\mathrm{a}} \cdot \overline{\mathrm{b}} = -10$

Answer: $-10$

</details>

---

### Q46. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the area of a parallelogram whose diagonals are represented by vectors $3 \hat{i}+\lambda \hat{j}+2 \hat{k}$ and $\hat{i}-2 \hat{j}+3 \hat{k}$ is $\frac{\sqrt{117}}{2}$ sq. units, then $\lambda=$

**Options:**

- **(A)** $-1$
- **(B)** $-2$
- **(C)** $-3$
- **(D)** $-4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-4$**

**Detailed Solution:**

The area of a parallelogram whose diagonals are $\vec{d}_1$ and $\vec{d}_2$ is given by $\dfrac{1}{2} |\vec{d}_1 \times \vec{d}_2|$.

Given that the area is $\dfrac{\sqrt{117}}{2}$, we have:

$\dfrac{1}{2} |\vec{d}_1 \times \vec{d}_2| = \dfrac{\sqrt{117}}{2}$

$|\vec{d}_1 \times \vec{d}_2| = \sqrt{117}$

Calculating the cross product of the diagonals:

$\vec{d}_1 \times \vec{d}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 3 & \lambda & 2 \\ 1 & -2 & 3 \end{vmatrix}$

$\vec{d}_1 \times \vec{d}_2 = \hat{i}(3\lambda - (-4)) - \hat{j}(9 - 2) + \hat{k}(-6 - \lambda)$

$\vec{d}_1 \times \vec{d}_2 = (3\lambda + 4)\hat{i} - 7\hat{j} - (\lambda + 6)\hat{k}$

Now, finding the magnitude squared:

$|\vec{d}_1 \times \vec{d}_2|^2 = (3\lambda + 4)^2 + (-7)^2 + (-(\lambda + 6))^2$

$117 = (9\lambda^2 + 24\lambda + 16) + 49 + (\lambda^2 + 12\lambda + 36)$

$117 = 10\lambda^2 + 36\lambda + 101$

$10\lambda^2 + 36\lambda - 16 = 0$

Dividing by $2$:

$5\lambda^2 + 18\lambda - 8 = 0$

$5\lambda^2 + 20\lambda - 2\lambda - 8 = 0$

$5\lambda(\lambda + 4) - 2(\lambda + 4) = 0$

$(5\lambda - 2)(\lambda + 4) = 0$

$\lambda = \dfrac{2}{5}$ or $\lambda = -4$

From the given options, $\lambda = -4$.

Answer: $-4$

</details>

---

### Q47. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The position vectors of the points $A, B, C$ are $\hat{i}+2 \hat{j}-\hat{k}, \hat{i}+\hat{j}+\hat{k}$, $2 \hat{i}+3 \hat{j}+2 \hat{k}$ respectively. If $A$ is chosen as the origin, then the cross product of position vectors of $B$ and $C$ are

**Options:**

- **(A)** $-5 \hat{i}+2 \hat{j}+\hat{k}$
- **(B)** $-\hat{i}+0 \hat{j}-\hat{k}$
- **(C)** $\hat{i}-\hat{\mathrm{k}}$
- **(D)** $5 \hat{i}-2 \hat{j}-\hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-5 \hat{i}+2 \hat{j}+\hat{k}$**

**Detailed Solution:**

Let the given position vectors be $\vec{a}, \vec{b}, \vec{c}$.

$\vec{a} = \hat{i} + 2\hat{j} - \hat{k}$

$\vec{b} = \hat{i} + \hat{j} + \hat{k}$

$\vec{c} = 2\hat{i} + 3\hat{j} + 2\hat{k}$

When $A$ is chosen as the origin, the new position vectors of $B$ and $C$ are $\overrightarrow{AB}$ and $\overrightarrow{AC}$.

$\overrightarrow{AB} = \vec{b} - \vec{a} = (\hat{i} + \hat{j} + \hat{k}) - (\hat{i} + 2\hat{j} - \hat{k}) = -\hat{j} + 2\hat{k}$

$\overrightarrow{AC} = \vec{c} - \vec{a} = (2\hat{i} + 3\hat{j} + 2\hat{k}) - (\hat{i} + 2\hat{j} - \hat{k}) = \hat{i} + \hat{j} + 3\hat{k}$

The cross product of the new position vectors is $\overrightarrow{AB} \times \overrightarrow{AC}$.

$\overrightarrow{AB} \times \overrightarrow{AC} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 0 & -1 & 2 \\ 1 & 1 & 3 \end{vmatrix}$

$\overrightarrow{AB} \times \overrightarrow{AC} = \hat{i}(-3 - 2) - \hat{j}(0 - 2) + \hat{k}(0 - (-1))$

$\overrightarrow{AB} \times \overrightarrow{AC} = -5\hat{i} + 2\hat{j} + \hat{k}$

Answer: $-5 \hat{i}+2 \hat{j}+\hat{k}$

</details>

---

### Q48. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A tetrahedron has vertices $O(0,0,0) A(1,2,1) B(2,1,3) C(-1,1,2)$.
Then the angle between the faces $O A B$ and $A B C$ will be

**Options:**

- **(A)** $\cos ^{-1}\left(\frac{19}{35}\right)$
- **(B)** $\cos ^{-1}\left(\frac{1}{35}\right)$
- **(C)** $\cos ^{-1}\left(\frac{9}{35}\right)$
- **(D)** $\cos ^{-1}\left(\frac{4}{35}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\cos ^{-1}\left(\frac{19}{35}\right)$**

**Detailed Solution:**

The angle between two faces of a tetrahedron is the angle between their respective normal vectors.

Let $\vec{n}_1$ be the normal vector to the face $OAB$.
$\vec{OA} = \hat{i} + 2\hat{j} + \hat{k}$
$\vec{OB} = 2\hat{i} + \hat{j} + 3\hat{k}$
$\vec{n}_1 = \vec{OA} \times \vec{OB} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & 1 \\ 2 & 1 & 3 \end{vmatrix} = 5\hat{i} - \hat{j} - 3\hat{k}$

Let $\vec{n}_2$ be the normal vector to the face $ABC$.
$\vec{AB} = \vec{OB} - \vec{OA} = \hat{i} - \hat{j} + 2\hat{k}$
$\vec{AC} = \vec{OC} - \vec{OA} = -2\hat{i} - \hat{j} + \hat{k}$
$\vec{n}_2 = \vec{AB} \times \vec{AC} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & -1 & 2 \\ -2 & -1 & 1 \end{vmatrix} = \hat{i} - 5\hat{j} - 3\hat{k}$

The angle $\theta$ between the faces is given by:
$\cos \theta = \dfrac{|\vec{n}_1 \cdot \vec{n}_2|}{|\vec{n}_1| |\vec{n}_2|}$

Calculating the dot product and magnitudes:
$\vec{n}_1 \cdot \vec{n}_2 = (5)(1) + (-1)(-5) + (-3)(-3) = 5 + 5 + 9 = 19$
$|\vec{n}_1| = \sqrt{5^2 + (-1)^2 + (-3)^2} = \sqrt{25 + 1 + 9} = \sqrt{35}$
$|\vec{n}_2| = \sqrt{1^2 + (-5)^2 + (-3)^2} = \sqrt{1 + 25 + 9} = \sqrt{35}$

Substituting these values:
$\cos \theta = \dfrac{19}{\sqrt{35} \times \sqrt{35}} = \dfrac{19}{35}$

$\theta = \cos^{-1}\left(\dfrac{19}{35}\right)$

Answer: $\cos ^{-1}\left(\frac{19}{35}\right)$

</details>

---

### Q49. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}=\hat{i}+\hat{\mathrm{j}}+\hat{\mathrm{k}}, \overline{\mathrm{b}}=\hat{\mathrm{j}}-\hat{\mathrm{k}}$ then a vector $\overline{\mathrm{c}}$ such that $\bar{a} \times \overline{\mathrm{c}}=\overline{\mathrm{b}}$ and $\bar{a} \cdot \overline{\mathrm{c}}=3$ is

**Options:**

- **(A)** $\frac{5}{3} \hat{i}+\frac{2}{3} \hat{j}+\frac{2}{3} \hat{k}$
- **(B)** $\hat{i}-2 \hat{j}+4 \hat{k}$
- **(C)** $\hat{i}+2 \hat{\mathrm{k}}$
- **(D)** $2 \hat{i}-3 \hat{j}+4 \hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{5}{3} \hat{i}+\frac{2}{3} \hat{j}+\frac{2}{3} \hat{k}$**

**Detailed Solution:**

Given $\bar{a} = \hat{i} + \hat{j} + \hat{k}$ and $\bar{b} = \hat{j} - \hat{k}$.

We have $\bar{a} \times \bar{c} = \bar{b}$.

Taking the cross product with $\bar{a}$ on both sides:

$\bar{a} \times (\bar{a} \times \bar{c}) = \bar{a} \times \bar{b}$

Using the vector triple product expansion:

$(\bar{a} \cdot \bar{c})\bar{a} - (\bar{a} \cdot \bar{a})\bar{c} = \bar{a} \times \bar{b}$

We are given $\bar{a} \cdot \bar{c} = 3$.

Also, $\bar{a} \cdot \bar{a} = |\bar{a}|^2 = (1)^2 + (1)^2 + (1)^2 = 3$.

Substituting these values:

$3\bar{a} - 3\bar{c} = \bar{a} \times \bar{b}$

$3\bar{c} = 3\bar{a} - (\bar{a} \times \bar{b})$

Now, calculating $\bar{a} \times \bar{b}$:

$\bar{a} \times \bar{b} = (\hat{i} + \hat{j} + \hat{k}) \times (\hat{j} - \hat{k})$

$\bar{a} \times \bar{b} = \hat{i}(1(-1) - 1(1)) - \hat{j}(1(-1) - 1(0)) + \hat{k}(1(1) - 1(0))$

$\bar{a} \times \bar{b} = -2\hat{i} + \hat{j} + \hat{k}$

Substituting $\bar{a}$ and $\bar{a} \times \bar{b}$ into the equation for $3\bar{c}$:

$3\bar{c} = 3(\hat{i} + \hat{j} + \hat{k}) - (-2\hat{i} + \hat{j} + \hat{k})$

$3\bar{c} = (3 + 2)\hat{i} + (3 - 1)\hat{j} + (3 - 1)\hat{k}$

$3\bar{c} = 5\hat{i} + 2\hat{j} + 2\hat{k}$

$\bar{c} = \dfrac{5}{3}\hat{i} + \dfrac{2}{3}\hat{j} + \dfrac{2}{3}\hat{k}$

Answer: $\frac{5}{3} \hat{i}+\frac{2}{3} \hat{j}+\frac{2}{3} \hat{k}$

</details>

---

### Q50. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}=\frac{1}{\sqrt{10}}(3 \hat{i}+\hat{\mathrm{k}})$ and $\overline{\mathrm{b}}=\frac{1}{7}(2 \hat{i}+3 \hat{\mathrm{j}}-6 \hat{\mathrm{k}})$ then the value of $(2 \bar{a}-\overline{\mathrm{b}}) \cdot((\bar{a} \times \overline{\mathrm{b}}) \times(\bar{a}+2 \overline{\mathrm{~b}}))=$

**Options:**

- **(A)** 3
- **(B)** -3
- **(C)** 5
- **(D)** -5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -5**

**Detailed Solution:**

Given $\bar{a} = \dfrac{1}{\sqrt{10}}(3 \hat{i} + \hat{k})$ and $\bar{b} = \dfrac{1}{7}(2 \hat{i} + 3 \hat{j} - 6 \hat{k})$.

First, we find the magnitudes and the dot product of the vectors:
$|\bar{a}|^2 = \dfrac{1}{10}(3^2 + 1^2) = \dfrac{10}{10} = 1$
$|\bar{b}|^2 = \dfrac{1}{49}(2^2 + 3^2 + (-6)^2) = \dfrac{49}{49} = 1$
$\bar{a} \cdot \bar{b} = \dfrac{1}{7\sqrt{10}}(3(2) + 0(3) + 1(-6)) = 0$

Using the vector triple product formula, $(\bar{a} \times \bar{b}) \times \bar{c} = (\bar{a} \cdot \bar{c})\bar{b} - (\bar{b} \cdot \bar{c})\bar{a}$.

Let $\bar{c} = \bar{a} + 2\bar{b}$. We evaluate the dot products:
$\bar{a} \cdot \bar{c} = \bar{a} \cdot (\bar{a} + 2\bar{b}) = |\bar{a}|^2 + 2(\bar{a} \cdot \bar{b}) = 1 + 0 = 1$
$\bar{b} \cdot \bar{c} = \bar{b} \cdot (\bar{a} + 2\bar{b}) = \bar{a} \cdot \bar{b} + 2|\bar{b}|^2 = 0 + 2(1) = 2$

Substituting these into the vector triple product formula gives:
$(\bar{a} \times \bar{b}) \times (\bar{a} + 2\bar{b}) = 1\bar{b} - 2\bar{a} = \bar{b} - 2\bar{a}$

Now, substituting this back into the original expression:
$(2\bar{a} - \bar{b}) \cdot ((\bar{a} \times \bar{b}) \times (\bar{a} + 2\bar{b})) = (2\bar{a} - \bar{b}) \cdot (\bar{b} - 2\bar{a})$

Taking the negative sign common from the second bracket:
$(2\bar{a} - \bar{b}) \cdot (-(2\bar{a} - \bar{b})) = -|2\bar{a} - \bar{b}|^2$

Expanding the magnitude squared:
$|2\bar{a} - \bar{b}|^2 = 4|\bar{a}|^2 + |\bar{b}|^2 - 4(\bar{a} \cdot \bar{b}) = 4(1) + 1 - 0 = 5$

Therefore, the value of the given expression is $-5$.

Answer: -5

</details>

---

### Q51. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}, \overline{\mathrm{~b}}, \overline{\mathrm{c}}$ be three vectors such that $\bar{a}+\overline{\mathrm{b}}+\overline{\mathrm{c}}=\overline{0},|\bar{a}|=3,|\overline{\mathrm{~b}}|=4$, $|\overline{\mathrm{c}}|=5$, then $\bar{a} \cdot \overline{\mathrm{~b}}+\overline{\mathrm{b}} \cdot \bar{c}+\overline{\mathrm{c}} \cdot \bar{a}=$

**Options:**

- **(A)** $25$
- **(B)** $-25$
- **(C)** $50$
- **(D)** $-50$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-25$**

**Detailed Solution:**

Given $\bar{a} + \bar{b} + \bar{c} = \bar{0}$

Squaring both sides, we get:

$|\bar{a} + \bar{b} + \bar{c}|^2 = 0$

$|\bar{a}|^2 + |\bar{b}|^2 + |\bar{c}|^2 + 2(\bar{a} \cdot \bar{b} + \bar{b} \cdot \bar{c} + \bar{c} \cdot \bar{a}) = 0$

Substituting the given values $|\bar{a}| = 3$, $|\bar{b}| = 4$, and $|\bar{c}| = 5$:

$(3)^2 + (4)^2 + (5)^2 + 2(\bar{a} \cdot \bar{b} + \bar{b} \cdot \bar{c} + \bar{c} \cdot \bar{a}) = 0$

$9 + 16 + 25 + 2(\bar{a} \cdot \bar{b} + \bar{b} \cdot \bar{c} + \bar{c} \cdot \bar{a}) = 0$

$50 + 2(\bar{a} \cdot \bar{b} + \bar{b} \cdot \bar{c} + \bar{c} \cdot \bar{a}) = 0$

$2(\bar{a} \cdot \bar{b} + \bar{b} \cdot \bar{c} + \bar{c} \cdot \bar{a}) = -50$

$\bar{a} \cdot \bar{b} + \bar{b} \cdot \bar{c} + \bar{c} \cdot \bar{a} = -25$

Answer: $-25$

</details>

---

### Q52. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}=2 \hat{i}+3 \hat{j}+4 \hat{k}, \overline{\mathrm{~b}}=\hat{i}-2 \hat{j}-2 \hat{\mathrm{k}}, \overline{\mathrm{c}}=-\hat{i}+4 \hat{j}+3 \hat{\mathrm{k}}$ and if $\overline{\mathrm{d}}$ is vector perpendicular to both $\overline{\mathrm{b}}$ and $\overline{\mathrm{c}}, \overline{\mathrm{a}} \cdot \overline{\mathrm{d}}=18$, then $|\overline{\mathrm{a}} \times \overline{\mathrm{d}}|^2=$

**Options:**

- **(A)** 640
- **(B)** 680
- **(C)** 720
- **(D)** 740

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 720**

**Detailed Solution:**

Since $\bar{d}$ is perpendicular to both $\bar{b}$ and $\bar{c}$, it is parallel to $\bar{b} \times \bar{c}$.

$\bar{b} \times \bar{c} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & -2 & -2 \\ -1 & 4 & 3 \end{vmatrix} = \hat{i}(-6 + 8) - \hat{j}(3 - 2) + \hat{k}(4 - 2) = 2\hat{i} - \hat{j} + 2\hat{k}$

Let $\bar{d} = \lambda(2\hat{i} - \hat{j} + 2\hat{k})$.

Given $\bar{a} \cdot \bar{d} = 18$, we have:

$(2\hat{i} + 3\hat{j} + 4\hat{k}) \cdot \lambda(2\hat{i} - \hat{j} + 2\hat{k}) = 18$

$\lambda(4 - 3 + 8) = 18 \Rightarrow 9\lambda = 18 \Rightarrow \lambda = 2$

Thus, $\bar{d} = 4\hat{i} - 2\hat{j} + 4\hat{k}$.

Now, we find the magnitudes squared:

$|\bar{a}|^2 = 2^2 + 3^2 + 4^2 = 4 + 9 + 16 = 29$

$|\bar{d}|^2 = 4^2 + (-2)^2 + 4^2 = 16 + 4 + 16 = 36$

Using Lagrange's identity, $|\bar{a} \times \bar{d}|^2 = |\bar{a}|^2 |\bar{d}|^2 - (\bar{a} \cdot \bar{d})^2$

$|\bar{a} \times \bar{d}|^2 = (29)(36) - (18)^2 = 1044 - 324 = 720$

Answer: 720

</details>

---

### Q53. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}=\hat{i}+\hat{j}, \overline{\mathrm{~b}}=2 \hat{i}-\hat{\mathrm{k}}, \overline{\mathrm{c}}=3 \hat{i}-\hat{\mathrm{j}}+\hat{\mathrm{k}}$, then vector $\overline{\mathrm{p}}$ satisfying $\overline{\mathrm{p}} \cdot \bar{a}=0$ and $\overline{\mathrm{p}} \times \overline{\mathrm{b}}=\overline{\mathrm{c}} \times \overline{\mathrm{b}}$ is

**Options:**

- **(A)** $\hat{i}-\hat{j}+\hat{k}$
- **(B)** $\hat{i}-2 \hat{j}+\hat{k}$
- **(C)** $-\hat{i}+\hat{j}+\hat{k}$
- **(D)** $\hat{i}-\hat{\mathrm{j}}+2 \hat{\mathrm{k}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\hat{i}-\hat{\mathrm{j}}+2 \hat{\mathrm{k}}$**

**Detailed Solution:**

Given $\bar{p} \times \bar{b} = \bar{c} \times \bar{b}$

$\Rightarrow \bar{p} \times \bar{b} - \bar{c} \times \bar{b} = \bar{0}$

$\Rightarrow (\bar{p} - \bar{c}) \times \bar{b} = \bar{0}$

This implies that the vector $(\bar{p} - \bar{c})$ is parallel to $\bar{b}$.

$\Rightarrow \bar{p} - \bar{c} = \lambda \bar{b}$ for some scalar $\lambda$

$\Rightarrow \bar{p} = \bar{c} + \lambda \bar{b}$

It is also given that $\bar{p} \cdot \bar{a} = 0$. Substituting the expression for $\bar{p}$:

$\Rightarrow (\bar{c} + \lambda \bar{b}) \cdot \bar{a} = 0$

$\Rightarrow \bar{c} \cdot \bar{a} + \lambda (\bar{b} \cdot \bar{a}) = 0$

Now, we calculate the dot products $\bar{c} \cdot \bar{a}$ and $\bar{b} \cdot \bar{a}$:

$\bar{c} \cdot \bar{a} = (3\hat{i} - \hat{j} + \hat{k}) \cdot (\hat{i} + \hat{j}) = 3(1) + (-1)(1) + 1(0) = 2$

$\bar{b} \cdot \bar{a} = (2\hat{i} - \hat{k}) \cdot (\hat{i} + \hat{j}) = 2(1) + 0(1) + (-1)(0) = 2$

Substituting these values into the equation:

$2 + \lambda (2) = 0$

$\Rightarrow 2\lambda = -2$

$\Rightarrow \lambda = -1$

Substituting $\lambda = -1$ back into the equation for $\bar{p}$:

$\bar{p} = \bar{c} - \bar{b}$

$\bar{p} = (3\hat{i} - \hat{j} + \hat{k}) - (2\hat{i} - \hat{k})$

$\bar{p} = \hat{i} - \hat{j} + 2\hat{k}$

Answer: $\hat{i}-\hat{\mathrm{j}}+2 \hat{\mathrm{k}}$

</details>

---

### Q54. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\bar{a}, \overline{\mathrm{~b}}, \overline{\mathrm{c}}$ are three vectors such that $|\bar{a}|=\sqrt{31}, 4|\overline{\mathrm{~b}}|=|\overline{\mathrm{c}}|=2$ and $2(\bar{a} \times \bar{b})=3\left(\bar{c} \times \bar{a}\right.$ )and if the angle between $\bar{b}$ and $\bar{c}$ is $\frac{2 \pi}{3}$ then $\left|\frac{\bar{a} \times \bar{c}}{\bar{a} \cdot \bar{b}}\right|^2=$

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 11

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

Given $|\bar{a}| = \sqrt{31}$ and $4|\bar{b}| = |\bar{c}| = 2 \Rightarrow |\bar{b}| = \dfrac{1}{2}, |\bar{c}| = 2$.

We are given the relation:

$2(\bar{a} \times \bar{b}) = 3(\bar{c} \times \bar{a})$

$2(\bar{a} \times \bar{b}) = -3(\bar{a} \times \bar{c})$

$\bar{a} \times (2\bar{b} + 3\bar{c}) = \bar{0}$

This implies that $\bar{a}$ is parallel to $2\bar{b} + 3\bar{c}$, so $\bar{a} = \lambda(2\bar{b} + 3\bar{c})$ for some scalar $\lambda$.

Now, we find $|2\bar{b} + 3\bar{c}|^2$:

$|2\bar{b} + 3\bar{c}|^2 = 4|\bar{b}|^2 + 9|\bar{c}|^2 + 12(\bar{b} \cdot \bar{c})$

Since the angle between $\bar{b}$ and $\bar{c}$ is $\dfrac{2\pi}{3}$,

$\bar{b} \cdot \bar{c} = |\bar{b}||\bar{c}|\cos\left(\dfrac{2\pi}{3}\right) = \left(\dfrac{1}{2}\right)(2)\left(-\dfrac{1}{2}\right) = -\dfrac{1}{2}$

$|2\bar{b} + 3\bar{c}|^2 = 4\left(\dfrac{1}{4}\right) + 9(4) + 12\left(-\dfrac{1}{2}\right) = 1 + 36 - 6 = 31$

Since $|\bar{a}|^2 = 31$, we have $\lambda^2(31) = 31 \Rightarrow \lambda^2 = 1$.

Next, we find $|\bar{a} \times \bar{c}|^2$:

$\bar{a} \times \bar{c} = \lambda(2\bar{b} + 3\bar{c}) \times \bar{c} = 2\lambda(\bar{b} \times \bar{c})$

$|\bar{a} \times \bar{c}|^2 = 4\lambda^2|\bar{b} \times \bar{c}|^2 = 4(1)\left(|\bar{b}|^2|\bar{c}|^2\sin^2\left(\dfrac{2\pi}{3}\right)\right)$

$|\bar{a} \times \bar{c}|^2 = 4\left(\dfrac{1}{4}\right)(4)\left(\dfrac{\sqrt{3}}{2}\right)^2 = 4 \times \dfrac{3}{4} = 3$

Now, we find $(\bar{a} \cdot \bar{b})^2$:

$\bar{a} \cdot \bar{b} = \lambda(2\bar{b} + 3\bar{c}) \cdot \bar{b} = \lambda(2|\bar{b}|^2 + 3\bar{b} \cdot \bar{c})$

$\bar{a} \cdot \bar{b} = \lambda\left(2\left(\dfrac{1}{4}\right) + 3\left(-\dfrac{1}{2}\right)\right) = \lambda\left(\dfrac{1}{2} - \dfrac{3}{2}\right) = -\lambda$

$(\bar{a} \cdot \bar{b})^2 = (-\lambda)^2 = \lambda^2 = 1$

Finally,

$\left|\dfrac{\bar{a} \times \bar{c}}{\bar{a} \cdot \bar{b}}\right|^2 = \dfrac{|\bar{a} \times \bar{c}|^2}{(\bar{a} \cdot \bar{b})^2} = \dfrac{3}{1} = 3$

Answer: 3

</details>

---

### Q55. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area of the rectangle having vertices $\mathrm{P}, \mathrm{Q}, \mathrm{R}, \mathrm{S}$ with position vectors $-\hat{i}+\hat{j}+\hat{k}, \hat{i}+\hat{j}+\hat{k}, \hat{i}-\hat{j}+\hat{k},-\hat{i}-\hat{j}+\hat{k}$ respectively is

**Options:**

- **(A)** 1 square unit
- **(B)** 2 square units
- **(C)** 3 square units
- **(D)** 4 square units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4 square units**

**Detailed Solution:**

The position vectors of the vertices are:

$\vec{p} = -\hat{i} + \hat{j} + \hat{k}$

$\vec{q} = \hat{i} + \hat{j} + \hat{k}$

$\vec{r} = \hat{i} - \hat{j} + \hat{k}$

$\vec{s} = -\hat{i} - \hat{j} + \hat{k}$

The adjacent sides of the rectangle are represented by the vectors $\overrightarrow{PQ}$ and $\overrightarrow{PS}$.

$\overrightarrow{PQ} = \vec{q} - \vec{p} = (\hat{i} + \hat{j} + \hat{k}) - (-\hat{i} + \hat{j} + \hat{k}) = 2\hat{i}$

$\overrightarrow{PS} = \vec{s} - \vec{p} = (-\hat{i} - \hat{j} + \hat{k}) - (-\hat{i} + \hat{j} + \hat{k}) = -2\hat{j}$

The area of the rectangle is given by $|\overrightarrow{PQ} \times \overrightarrow{PS}|$.

$\overrightarrow{PQ} \times \overrightarrow{PS} = (2\hat{i}) \times (-2\hat{j}) = -4(\hat{i} \times \hat{j}) = -4\hat{k}$

Area $= |-4\hat{k}| = 4$ square units.

Answer: 4 square units

</details>

---

### Q56. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\bar{a}=\hat{i}+\hat{\mathrm{j}}+\hat{\mathrm{k}}, \overline{\mathrm{b}}$ and $\overline{\mathrm{c}}=\hat{\mathrm{j}}-\hat{\mathrm{k}}$ be three vectors such that $\bar{a} \times \overline{\mathrm{b}}=\overline{\mathrm{c}}$ and $\bar{a} \cdot \bar{c}=0$. If the length of projection vector of the vector $\overline{\mathrm{b}}$ on the vector $\bar{a} \times \overline{\mathrm{c}}$ is $l$, then the value of $3 l^2$ is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 4
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

Given $\bar{a} = \hat{i} + \hat{j} + \hat{k}$ and $\bar{c} = \hat{j} - \hat{k}$.

We have $|\bar{a}|^2 = 1^2 + 1^2 + 1^2 = 3$ and $|\bar{c}|^2 = 0^2 + 1^2 + (-1)^2 = 2$.

Also, $\bar{a} \cdot \bar{c} = (1)(0) + (1)(1) + (1)(-1) = 0$, which means $\bar{a}$ and $\bar{c}$ are perpendicular.

The length of the projection of $\bar{b}$ on $\bar{a} \times \bar{c}$ is given by:

$l = \dfrac{|\bar{b} \cdot (\bar{a} \times \bar{c})|}{|\bar{a} \times \bar{c}|}$

Using the properties of the scalar triple product, we can rewrite the numerator:

$\bar{b} \cdot (\bar{a} \times \bar{c}) = (\bar{b} \times \bar{a}) \cdot \bar{c} = -(\bar{a} \times \bar{b}) \cdot \bar{c}$

Since it is given that $\bar{a} \times \bar{b} = \bar{c}$, we get:

$-(\bar{a} \times \bar{b}) \cdot \bar{c} = -\bar{c} \cdot \bar{c} = -|\bar{c}|^2 = -2$

So, the absolute value in the numerator is $|-2| = 2$.

For the denominator, since $\bar{a}$ and $\bar{c}$ are perpendicular ($\theta = 90^\circ$):

$|\bar{a} \times \bar{c}| = |\bar{a}| |\bar{c}| \sin 90^\circ = \sqrt{3} \times \sqrt{2} \times 1 = \sqrt{6}$

Substituting these values into the projection formula:

$l = \dfrac{2}{\sqrt{6}}$

Squaring both sides gives:

$l^2 = \dfrac{4}{6} = \dfrac{2}{3}$

Therefore, the value of $3l^2$ is:

$3l^2 = 3 \times \dfrac{2}{3} = 2$

Answer: 2

</details>

---

### Q57. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the lengths of three vectors $\bar{a}, \overline{\mathrm{~b}}$ and $\overline{\mathrm{c}}$ are 5,12,13 units respectively, and each one is perpendicular to the sum of the other two, then $|\bar{a}+\overline{\mathrm{b}}+\overline{\mathrm{c}}|=\ldots \ldots$

**Options:**

- **(A)** $\sqrt{338}$
- **(B)** $169$
- **(C)** $338$
- **(D)** $676$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{338}$**

**Detailed Solution:**

Given $|\bar{a}| = 5$, $|\bar{b}| = 12$, and $|\bar{c}| = 13$.

Since each vector is perpendicular to the sum of the other two, we have:
$\bar{a} \cdot (\bar{b} + \bar{c}) = 0 \Rightarrow \bar{a} \cdot \bar{b} + \bar{a} \cdot \bar{c} = 0$
$\bar{b} \cdot (\bar{a} + \bar{c}) = 0 \Rightarrow \bar{b} \cdot \bar{a} + \bar{b} \cdot \bar{c} = 0$
$\bar{c} \cdot (\bar{a} + \bar{b}) = 0 \Rightarrow \bar{c} \cdot \bar{a} + \bar{c} \cdot \bar{b} = 0$

Adding these three equations, we get:
$2(\bar{a} \cdot \bar{b} + \bar{b} \cdot \bar{c} + \bar{c} \cdot \bar{a}) = 0$

The square of the magnitude of the sum of the vectors is given by:
$|\bar{a} + \bar{b} + \bar{c}|^2 = |\bar{a}|^2 + |\bar{b}|^2 + |\bar{c}|^2 + 2(\bar{a} \cdot \bar{b} + \bar{b} \cdot \bar{c} + \bar{c} \cdot \bar{a})$

Substituting the given values:
$|\bar{a} + \bar{b} + \bar{c}|^2 = 5^2 + 12^2 + 13^2 + 0$
$|\bar{a} + \bar{b} + \bar{c}|^2 = 25 + 144 + 169 = 338$

Taking the square root on both sides:
$|\bar{a} + \bar{b} + \bar{c}| = \sqrt{338}$

Answer: $\sqrt{338}$

</details>

---

### Q58. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the area of parallelogram, whose diagonals are $\hat{i}-\hat{j}+2 \hat{k}$ and $2 \hat{i}+3 \hat{j}+\alpha \hat{k}$ is $\frac{\sqrt{93}}{2}$ sq. unit, then $\alpha=$

**Options:**

- **(A)** $-4,2$
- **(B)** $-3,-2$
- **(C)** 2,1
- **(D)** 4,2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-4,2$**

**Detailed Solution:**

The area of a parallelogram with diagonals $\vec{d}_1$ and $\vec{d}_2$ is given by $\dfrac{1}{2} |\vec{d}_1 \times \vec{d}_2|$.

Given diagonals are $\vec{d}_1 = \hat{i} - \hat{j} + 2\hat{k}$ and $\vec{d}_2 = 2\hat{i} + 3\hat{j} + \alpha\hat{k}$.

Calculating the cross product:
$\vec{d}_1 \times \vec{d}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & -1 & 2 \\ 2 & 3 & \alpha \end{vmatrix}$

$\vec{d}_1 \times \vec{d}_2 = \hat{i}(-\alpha - 6) - \hat{j}(\alpha - 4) + \hat{k}(3 - (-2))$

$\vec{d}_1 \times \vec{d}_2 = (-\alpha - 6)\hat{i} + (4 - \alpha)\hat{j} + 5\hat{k}$

The magnitude of the cross product is:
$|\vec{d}_1 \times \vec{d}_2| = \sqrt{(-\alpha - 6)^2 + (4 - \alpha)^2 + 5^2}$

$|\vec{d}_1 \times \vec{d}_2| = \sqrt{\alpha^2 + 12\alpha + 36 + 16 - 8\alpha + \alpha^2 + 25}$

$|\vec{d}_1 \times \vec{d}_2| = \sqrt{2\alpha^2 + 4\alpha + 77}$

Given that the area is $\dfrac{\sqrt{93}}{2}$:
$\dfrac{1}{2} \sqrt{2\alpha^2 + 4\alpha + 77} = \dfrac{\sqrt{93}}{2}$

Squaring both sides:
$2\alpha^2 + 4\alpha + 77 = 93$

$2\alpha^2 + 4\alpha - 16 = 0$

Dividing by 2:
$\alpha^2 + 2\alpha - 8 = 0$

$(\alpha + 4)(\alpha - 2) = 0$

$\alpha = -4, 2$

Answer: $-4,2$

</details>

---

### Q59. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{p}}=2 \hat{i}+\hat{\mathrm{k}}, \quad \overline{\mathrm{q}}=\hat{i}+\hat{\mathrm{j}}+\hat{\mathrm{k}}, \quad \overline{\mathrm{r}}=4 \hat{i}-3 \hat{\mathrm{j}}+7 \hat{\mathrm{k}}$ and a vector $\overline{\mathrm{m}}$ is such that $\overline{\mathrm{m}} \times \overline{\mathrm{q}}=\overline{\mathrm{r}} \times \overline{\mathrm{q}}, \overline{\mathrm{m}} \cdot \overline{\mathrm{p}}=0$, then $\overline{\mathrm{m}}=\ldots$.

**Options:**

- **(A)** $\hat{i}-8 \hat{j}-2 \hat{k}$
- **(B)** $-10 \hat{i}+3 \hat{j}+7 \hat{k}$
- **(C)** $-\hat{i}-8 \hat{j}+2 \hat{k}$
- **(D)** $2 \hat{i}+4 \hat{j}+\hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\hat{i}-8 \hat{j}+2 \hat{k}$**

**Detailed Solution:**

Given $\overline{\mathrm{m}} \times \overline{\mathrm{q}} = \overline{\mathrm{r}} \times \overline{\mathrm{q}}$

$(\overline{\mathrm{m}} - \overline{\mathrm{r}}) \times \overline{\mathrm{q}} = \overline{0}$

This implies that $\overline{\mathrm{m}} - \overline{\mathrm{r}}$ is parallel to $\overline{\mathrm{q}}$, so $\overline{\mathrm{m}} - \overline{\mathrm{r}} = \lambda \overline{\mathrm{q}}$ for some scalar $\lambda$.

$\overline{\mathrm{m}} = \overline{\mathrm{r}} + \lambda \overline{\mathrm{q}}$

Taking the dot product with $\overline{\mathrm{p}}$ on both sides:

$\overline{\mathrm{m}} \cdot \overline{\mathrm{p}} = \overline{\mathrm{r}} \cdot \overline{\mathrm{p}} + \lambda (\overline{\mathrm{q}} \cdot \overline{\mathrm{p}})$

Since $\overline{\mathrm{m}} \cdot \overline{\mathrm{p}} = 0$, we get:

$0 = \overline{\mathrm{r}} \cdot \overline{\mathrm{p}} + \lambda (\overline{\mathrm{q}} \cdot \overline{\mathrm{p}})$

$\lambda = -\dfrac{\overline{\mathrm{r}} \cdot \overline{\mathrm{p}}}{\overline{\mathrm{q}} \cdot \overline{\mathrm{p}}}$

Now, calculating the dot products:

$\overline{\mathrm{r}} \cdot \overline{\mathrm{p}} = (4\hat{i} - 3\hat{j} + 7\hat{k}) \cdot (2\hat{i} + \hat{k}) = 4(2) + (-3)(0) + 7(1) = 8 + 7 = 15$

$\overline{\mathrm{q}} \cdot \overline{\mathrm{p}} = (\hat{i} + \hat{j} + \hat{k}) \cdot (2\hat{i} + \hat{k}) = 1(2) + 1(0) + 1(1) = 2 + 1 = 3$

Substituting these values:

$\lambda = -\dfrac{15}{3} = -5$

Therefore, $\overline{\mathrm{m}} = \overline{\mathrm{r}} - 5\overline{\mathrm{q}}$

$\overline{\mathrm{m}} = (4\hat{i} - 3\hat{j} + 7\hat{k}) - 5(\hat{i} + \hat{j} + \hat{k})$

$\overline{\mathrm{m}} = (4 - 5)\hat{i} + (-3 - 5)\hat{j} + (7 - 5)\hat{k}$

$\overline{\mathrm{m}} = -\hat{i} - 8\hat{j} + 2\hat{k}$

Answer: $-\hat{i}-8 \hat{j}+2 \hat{k}$

</details>

---

### Q60. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of a parallelogram whose diagonals are the vectors $2 \bar{a}-\bar{b}$ and $4 \bar{a}-5 \bar{b}$, where $\bar{a}$ and $\overline{\mathrm{b}}$ are unit vectors forming an angle of $45^{\circ}$ is

**Options:**

- **(A)** $3 \sqrt{2}$ sq. units
- **(B)** $\frac{3}{\sqrt{2}}$ sq. units
- **(C)** $\sqrt{2}$ sq. units
- **(D)** $\frac{\sqrt{2}}{3}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{\sqrt{2}}$ sq. units**

**Detailed Solution:**

The area of a parallelogram with diagonals $\vec{d}_1$ and $\vec{d}_2$ is given by $\dfrac{1}{2} |\vec{d}_1 \times \vec{d}_2|$.

Given $\vec{d}_1 = 2\bar{a} - \bar{b}$ and $\vec{d}_2 = 4\bar{a} - 5\bar{b}$.

$\vec{d}_1 \times \vec{d}_2 = (2\bar{a} - \bar{b}) \times (4\bar{a} - 5\bar{b})$

$= 8(\bar{a} \times \bar{a}) - 10(\bar{a} \times \bar{b}) - 4(\bar{b} \times \bar{a}) + 5(\bar{b} \times \bar{b})$

Since $\bar{a} \times \bar{a} = \vec{0}$, $\bar{b} \times \bar{b} = \vec{0}$ and $\bar{b} \times \bar{a} = -(\bar{a} \times \bar{b})$:

$\vec{d}_1 \times \vec{d}_2 = -10(\bar{a} \times \bar{b}) + 4(\bar{a} \times \bar{b}) = -6(\bar{a} \times \bar{b})$

The area of the parallelogram is:

$A = \dfrac{1}{2} |-6(\bar{a} \times \bar{b})| = 3 |\bar{a} \times \bar{b}|$

Since $\bar{a}$ and $\bar{b}$ are unit vectors with an angle of $45^{\circ}$ between them:

$|\bar{a} \times \bar{b}| = |\bar{a}| |\bar{b}| \sin 45^{\circ} = (1)(1) \left(\dfrac{1}{\sqrt{2}}\right) = \dfrac{1}{\sqrt{2}}$

Therefore, the area is:

$A = 3 \times \dfrac{1}{\sqrt{2}} = \dfrac{3}{\sqrt{2}}$ sq. units.

Answer: $\frac{3}{\sqrt{2}}$ sq. units

</details>

---

### Q61. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\bar{a}=\hat{i}-\hat{\mathrm{j}}, \overline{\mathrm{b}}=\hat{\mathrm{j}}-\hat{\mathrm{k}}, \overline{\mathrm{c}}=\hat{\mathrm{k}}-\hat{i}$ then a unit vector $\overline{\mathrm{d}}$ such that $\bar{a} \cdot \bar{d}=0=[\bar{b} \bar{c} \bar{d}]$ is

**Options:**

- **(A)** $\pm\left(\frac{\hat{i}+\hat{j}+3 \hat{k}}{\sqrt{11}}\right)$
- **(B)** $\pm\left(\frac{-\hat{\mathrm{j}}+\hat{\mathrm{k}}}{\sqrt{2}}\right)$
- **(C)** $\pm\left(\frac{\hat{i}+\hat{j}+\hat{k}}{\sqrt{3}}\right)$
- **(D)** $\pm\left(\frac{\hat{i}+\hat{j}-2 \hat{k}}{\sqrt{6}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pm\left(\frac{\hat{i}+\hat{j}-2 \hat{k}}{\sqrt{6}}\right)$**

**Detailed Solution:**

Let $\bar{d} = x\hat{i} + y\hat{j} + z\hat{k}$.

Given $\bar{a} \cdot \bar{d} = 0$, we have:
$(\hat{i} - \hat{j}) \cdot (x\hat{i} + y\hat{j} + z\hat{k}) = 0$
$x - y = 0 \Rightarrow x = y$

Given $[\bar{b} \bar{c} \bar{d}] = 0$, the vectors $\bar{b}$, $\bar{c}$, and $\bar{d}$ are coplanar. Their scalar triple product is zero:
$\begin{vmatrix} 0 & 1 & -1 \\ -1 & 0 & 1 \\ x & y & z \end{vmatrix} = 0$

Expanding the determinant:
$0 - 1(-z - x) - 1(-y) = 0$
$x + y + z = 0$

Substituting $y = x$ into the above equation:
$x + x + z = 0 \Rightarrow z = -2x$

Since $\bar{d}$ is a unit vector, $|\bar{d}| = 1$:
$x^2 + y^2 + z^2 = 1$
$x^2 + x^2 + (-2x)^2 = 1$
$6x^2 = 1 \Rightarrow x = \pm \dfrac{1}{\sqrt{6}}$

Substituting the values of $x, y, z$ back into $\bar{d}$:
$\bar{d} = \pm \left( \dfrac{1}{\sqrt{6}}\hat{i} + \dfrac{1}{\sqrt{6}}\hat{j} - \dfrac{2}{\sqrt{6}}\hat{k} \right)$
$\bar{d} = \pm \left( \dfrac{\hat{i} + \hat{j} - 2\hat{k}}{\sqrt{6}} \right)$

Answer: $\pm\left(\frac{\hat{i}+\hat{j}-2 \hat{k}}{\sqrt{6}}\right)$

</details>

---

### Q62. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $m \in \mathbb{R}$, when angle between the vectors $\bar{p}=m y \hat{i}-6 \hat{j}+3 \hat{k}$ and $\bar{q}=y \hat{i}+2 \hat{j}+2 m y \hat{k}$ is obtuse angle for all $y \in \mathbb{R}$, is

**Options:**

- **(A)** $\mathrm{m} < -\frac{4}{2}$
- **(B)** $\mathrm{m}=1$
- **(C)** $m>0$
- **(D)** $-\frac{4}{3} < \mathrm{m} \le 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{4}{3} < \mathrm{m} \le 0$**

**Detailed Solution:**

For the angle between the vectors $\bar{p}$ and $\bar{q}$ to be obtuse, their dot product must be strictly less than zero for all $y \in \mathbb{R}$.

$\bar{p} \cdot \bar{q} < 0$

$(m y \hat{i} - 6 \hat{j} + 3 \hat{k}) \cdot (y \hat{i} + 2 \hat{j} + 2 m y \hat{k}) < 0$

$m y^2 - 12 + 6 m y < 0$

$m y^2 + 6 m y - 12 < 0$

This inequality must hold for all $y \in \mathbb{R}$.

Case 1: If $m = 0$, the inequality becomes $-12 < 0$, which is true for all $y \in \mathbb{R}$. Thus, $m = 0$ is a valid solution.

Case 2: If $m \neq 0$, the quadratic expression $A y^2 + B y + C < 0$ for all $y \in \mathbb{R}$ requires $A < 0$ and discriminant $D < 0$.

Therefore, $m < 0$ and $(6m)^2 - 4(m)(-12) < 0$.

$36 m^2 + 48 m < 0$

$12 m (3 m + 4) < 0$

Since $m < 0$, we must have $3 m + 4 > 0$, which gives $m > -\dfrac{4}{3}$.

So, $-\dfrac{4}{3} < m < 0$.

Combining both cases, we get $-\dfrac{4}{3} < m \le 0$.

Answer: $-\frac{4}{3} < \mathrm{m} \le 0$

</details>

---

### Q63. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\bar{a}, \overline{\mathrm{~b}}, \overline{\mathrm{c}}$ are nonzero vectors such that $\bar{a}$ is perpendicular to $\overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$, $|\bar{a}|=1,|\bar{b}|=2,|\bar{c}|=1$ and $\bar{b} \cdot \bar{c}=1$. There is nonzero vector $\bar{d}$ coplanar with $\bar{a}+\overline{\mathrm{b}}$ and $2 \overline{\mathrm{~b}}-\overline{\mathrm{c}}$. If $\overline{\mathrm{d}} \cdot \bar{a}=1$, then $|\overline{\mathrm{d}}|^2=$
(Note that \(x\) and \(y\) are parameters involved when we write \(d=x(a+b)+y(2 b-c))\)

**Options:**

- **(A)** $13 y^2+14 y+5$
- **(B)** $y^2+14 y+5$
- **(C)** $y^2-14 y-5$
- **(D)** $y^2-14 y+5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $13 y^2+14 y+5$**

**Detailed Solution:**

Given that $\bar{a}$ is perpendicular to $\bar{b}$ and $\bar{c}$, we have $\bar{a} \cdot \bar{b} = 0$ and $\bar{a} \cdot \bar{c} = 0$.

Also given: $|\bar{a}| = 1$, $|\bar{b}| = 2$, $|\bar{c}| = 1$, and $\bar{b} \cdot \bar{c} = 1$.

Since $\bar{d}$ is coplanar with $\bar{a}+\bar{b}$ and $2\bar{b}-\bar{c}$, we can write:

$\bar{d} = x(\bar{a}+\bar{b}) + y(2\bar{b}-\bar{c})$

Taking the dot product with $\bar{a}$ on both sides:

$\bar{d} \cdot \bar{a} = x(\bar{a} \cdot \bar{a} + \bar{b} \cdot \bar{a}) + y(2\bar{b} \cdot \bar{a} - \bar{c} \cdot \bar{a})$

Substituting the known dot products:

$1 = x(|\bar{a}|^2 + 0) + y(0 - 0)$

$1 = x(1)^2 \Rightarrow x = 1$

Now substitute $x = 1$ back into the expression for $\bar{d}$:

$\bar{d} = 1(\bar{a}+\bar{b}) + y(2\bar{b}-\bar{c}) = \bar{a} + (1+2y)\bar{b} - y\bar{c}$

To find $|\bar{d}|^2$, we take the dot product of $\bar{d}$ with itself:

$|\bar{d}|^2 = (\bar{a} + (1+2y)\bar{b} - y\bar{c}) \cdot (\bar{a} + (1+2y)\bar{b} - y\bar{c})$

Since $\bar{a} \cdot \bar{b} = 0$ and $\bar{a} \cdot \bar{c} = 0$, the cross terms involving $\bar{a}$ vanish:

$|\bar{d}|^2 = |\bar{a}|^2 + (1+2y)^2|\bar{b}|^2 + y^2|\bar{c}|^2 - 2(1+2y)y(\bar{b} \cdot \bar{c})$

Substitute the given magnitudes and dot product:

$|\bar{d}|^2 = 1^2 + (1+2y)^2(2)^2 + y^2(1)^2 - 2(1+2y)y(1)$

$|\bar{d}|^2 = 1 + 4(1 + 4y + 4y^2) + y^2 - 2y - 4y^2$

$|\bar{d}|^2 = 1 + 4 + 16y + 16y^2 + y^2 - 2y - 4y^2$

$|\bar{d}|^2 = 13y^2 + 14y + 5$

Answer: $13 y^2+14 y+5$

</details>

---

### Q64. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}$ and $\overline{\mathrm{b}}$ are unit vectors such that $|\bar{a}+\overline{\mathrm{b}}|=\sqrt{3}$, then the angle between $\bar{a}$ and $\overline{\mathrm{b}}$ is

**Options:**

- **(A)** $\frac{\pi}{6}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{3}$**

**Detailed Solution:**

Given $|\bar{a}| = 1$ and $|\bar{b}| = 1$.

The magnitude of the sum of two vectors is given by $|\bar{a}+\bar{b}|^2 = |\bar{a}|^2 + |\bar{b}|^2 + 2|\bar{a}||\bar{b}|\cos\theta$, where $\theta$ is the angle between $\bar{a}$ and $\bar{b}$.

Substituting the given values:

$(\sqrt{3})^2 = 1^2 + 1^2 + 2(1)(1)\cos\theta$

$3 = 2 + 2\cos\theta$

$2\cos\theta = 1$

$\cos\theta = \dfrac{1}{2}$

$\theta = \dfrac{\pi}{3}$

Answer: $\frac{\pi}{3}$

</details>

---

### Q65. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}, \overline{\mathrm{~b}}$, and $\overline{\mathrm{c}}$ be unit vectors. Suppose that $\bar{a} \cdot \overline{\mathrm{~b}}=\bar{a} \cdot \bar{c}=0$ and if the angle between $\overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ is $\frac{\pi}{6}$, then $\bar{a}$ is

**Options:**

- **(A)** $\pm(\overline{\mathrm{b}} \times \overline{\mathrm{c}})$
- **(B)** $\pm \frac{1}{2}(\overline{\mathrm{~b}} \times \overline{\mathrm{c}})$
- **(C)** $\pm 2(\overline{\mathrm{~b}} \times \overline{\mathrm{c}})$
- **(D)** $\pm 4(\overline{\mathrm{~b}} \times \overline{\mathrm{c}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\pm 2(\overline{\mathrm{~b}} \times \overline{\mathrm{c}})$**

**Detailed Solution:**

Given $\bar{a} \cdot \bar{b} = 0$ and $\bar{a} \cdot \bar{c} = 0$, the vector $\bar{a}$ is perpendicular to both $\bar{b}$ and $\bar{c}$.

Therefore, $\bar{a}$ is parallel to $\bar{b} \times \bar{c}$.

We can write $\bar{a} = \lambda (\bar{b} \times \bar{c})$ for some scalar $\lambda$.

Taking the magnitude on both sides, we get $|\bar{a}| = |\lambda| |\bar{b} \times \bar{c}|$.

Since $\bar{a}, \bar{b}, \bar{c}$ are unit vectors, $|\bar{a}| = |\bar{b}| = |\bar{c}| = 1$.

The magnitude of $\bar{b} \times \bar{c}$ is $|\bar{b} \times \bar{c}| = |\bar{b}| |\bar{c}| \sin \theta$, where $\theta = \dfrac{\pi}{6}$.

$|\bar{b} \times \bar{c}| = (1)(1) \sin\left(\dfrac{\pi}{6}\right) = \dfrac{1}{2}$.

Substituting this into the magnitude equation, we get $1 = |\lambda| \left(\dfrac{1}{2}\right)$.

$|\lambda| = 2 \Rightarrow \lambda = \pm 2$.

Thus, $\bar{a} = \pm 2(\bar{b} \times \bar{c})$.

Answer: $\pm 2(\overline{\mathrm{~b}} \times \overline{\mathrm{c}})$

</details>

---

### Q66. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{a}}=\frac{1}{\sqrt{10}}(3 \hat{i}+\hat{\mathrm{k}})$ and $\overline{\mathrm{b}}=\frac{1}{7}(2 \hat{i}+3 \hat{\mathrm{j}}-6 \hat{\mathrm{k}})$ then the value of $(2 \bar{a}-\bar{b}) \cdot[(\bar{a} \times \bar{b}) \times(\bar{a}+2 \bar{b})]=$

**Options:**

- **(A)** $\frac{1}{5}$
- **(B)** $-5$
- **(C)** $5$
- **(D)** $-\frac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-5$**

**Detailed Solution:**

Given vectors are $\overline{a} = \dfrac{1}{\sqrt{10}}(3\hat{i} + \hat{k})$ and $\overline{b} = \dfrac{1}{7}(2\hat{i} + 3\hat{j} - 6\hat{k})$.

First, we find the magnitudes of $\overline{a}$ and $\overline{b}$:
$|\overline{a}|^2 = \dfrac{1}{10}(3^2 + 0^2 + 1^2) = \dfrac{10}{10} = 1$
$|\overline{b}|^2 = \dfrac{1}{49}(2^2 + 3^2 + (-6)^2) = \dfrac{49}{49} = 1$

Now, we find the dot product $\overline{a} \cdot \overline{b}$:
$\overline{a} \cdot \overline{b} = \dfrac{1}{7\sqrt{10}} (3 \times 2 + 0 \times 3 + 1 \times (-6)) = \dfrac{1}{7\sqrt{10}} (6 - 6) = 0$
Thus, $\overline{a}$ and $\overline{b}$ are orthogonal unit vectors.

We need to evaluate the expression:
$E = (2\overline{a} - \overline{b}) \cdot [(\overline{a} \times \overline{b}) \times (\overline{a} + 2\overline{b})]$

Using the distributive property of the cross product:
$(\overline{a} \times \overline{b}) \times (\overline{a} + 2\overline{b}) = (\overline{a} \times \overline{b}) \times \overline{a} + 2(\overline{a} \times \overline{b}) \times \overline{b}$

Using the vector triple product formula $(\vec{x} \times \vec{y}) \times \vec{z} = (\vec{x} \cdot \vec{z})\vec{y} - (\vec{y} \cdot \vec{z})\vec{x}$:
$(\overline{a} \times \overline{b}) \times \overline{a} = (\overline{a} \cdot \overline{a})\overline{b} - (\overline{b} \cdot \overline{a})\overline{a} = |\overline{a}|^2\overline{b} - 0 = \overline{b}$
$(\overline{a} \times \overline{b}) \times \overline{b} = (\overline{a} \cdot \overline{b})\overline{b} - (\overline{b} \cdot \overline{b})\overline{a} = 0 - |\overline{b}|^2\overline{a} = -\overline{a}$

Substituting these back into the expression:
$(\overline{a} \times \overline{b}) \times (\overline{a} + 2\overline{b}) = \overline{b} + 2(-\overline{a}) = \overline{b} - 2\overline{a}$

Now, substitute this into $E$:
$E = (2\overline{a} - \overline{b}) \cdot (\overline{b} - 2\overline{a})$
$E = -(2\overline{a} - \overline{b}) \cdot (2\overline{a} - \overline{b})$
$E = -|2\overline{a} - \overline{b}|^2$

Expanding the magnitude squared:
$|2\overline{a} - \overline{b}|^2 = 4|\overline{a}|^2 + |\overline{b}|^2 - 4(\overline{a} \cdot \overline{b})$
$|2\overline{a} - \overline{b}|^2 = 4(1) + 1 - 4(0) = 5$

Therefore, $E = -5$.

Answer: $-5$

</details>

---

### Q67. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}$ and $\overline{\mathrm{b}}$ are unit vectors and $\theta$ is the angle between them, then $\tan \theta / 2=$

**Options:**

- **(A)** $|\bar{a}-\bar{b}|$
- **(B)** $|\bar{a}+\bar{b}|$
- **(C)** $\frac{|\bar{a}+\bar{b}|}{|\bar{a}-\bar{b}|}$
- **(D)** $\frac{|\bar{a}-\bar{b}|}{|\bar{a}+\bar{b}|}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{|\bar{a}-\bar{b}|}{|\bar{a}+\bar{b}|}$**

**Detailed Solution:**

Given $|\bar{a}| = 1$ and $|\bar{b}| = 1$.

Consider $|\bar{a} - \bar{b}|^2 = |\bar{a}|^2 + |\bar{b}|^2 - 2|\bar{a}||\bar{b}|\cos\theta$

$|\bar{a} - \bar{b}|^2 = 1 + 1 - 2(1)(1)\cos\theta = 2(1 - \cos\theta)$

Using the half-angle formula $1 - \cos\theta = 2\sin^2(\dfrac{\theta}{2})$:

$|\bar{a} - \bar{b}|^2 = 4\sin^2(\dfrac{\theta}{2}) \Rightarrow |\bar{a} - \bar{b}| = 2\sin(\dfrac{\theta}{2})$

Similarly, consider $|\bar{a} + \bar{b}|^2 = |\bar{a}|^2 + |\bar{b}|^2 + 2|\bar{a}||\bar{b}|\cos\theta$

$|\bar{a} + \bar{b}|^2 = 1 + 1 + 2(1)(1)\cos\theta = 2(1 + \cos\theta)$

Using the half-angle formula $1 + \cos\theta = 2\cos^2(\dfrac{\theta}{2})$:

$|\bar{a} + \bar{b}|^2 = 4\cos^2(\dfrac{\theta}{2}) \Rightarrow |\bar{a} + \bar{b}| = 2\cos(\dfrac{\theta}{2})$

Dividing the two expressions:

$\dfrac{|\bar{a} - \bar{b}|}{|\bar{a} + \bar{b}|} = \dfrac{2\sin(\dfrac{\theta}{2})}{2\cos(\dfrac{\theta}{2})} = \tan(\dfrac{\theta}{2})$

Answer: $\frac{|\bar{a}-\bar{b}|}{|\bar{a}+\bar{b}|}$

</details>

---

### Q68. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the projection of $\bar{a}$ on $\bar{b}+\bar{c}$ is twice the projection of $\bar{b}+\bar{c}$ on $\bar{a}$ also if $|\bar{b}|=2 \sqrt{2},|\bar{c}|=4$ and the angle between $\bar{b}$ and $\bar{c}$ is $\frac{\pi}{4}$ then $|\bar{a}|=$

**Options:**

- **(A)** $2 \sqrt{10}$
- **(B)** $3 \sqrt{10}$
- **(C)** $4 \sqrt{10}$
- **(D)** $5 \sqrt{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 \sqrt{10}$**

**Detailed Solution:**

The scalar projection of $\bar{a}$ on $\bar{b}+\bar{c}$ is given by $\dfrac{\bar{a} \cdot (\bar{b}+\bar{c})}{|\bar{b}+\bar{c}|}$.

The scalar projection of $\bar{b}+\bar{c}$ on $\bar{a}$ is given by $\dfrac{(\bar{b}+\bar{c}) \cdot \bar{a}}{|\bar{a}|}$.

According to the given condition:

$\dfrac{\bar{a} \cdot (\bar{b}+\bar{c})}{|\bar{b}+\bar{c}|} = 2 \dfrac{(\bar{b}+\bar{c}) \cdot \bar{a}}{|\bar{a}|}$

Assuming $\bar{a} \cdot (\bar{b}+\bar{c}) \neq 0$, we can cancel it from both sides to get:

$\dfrac{1}{|\bar{b}+\bar{c}|} = \dfrac{2}{|\bar{a}|} \Rightarrow |\bar{a}| = 2|\bar{b}+\bar{c}|$

Now, we find the magnitude of $\bar{b}+\bar{c}$ using the formula:

$|\bar{b}+\bar{c}|^2 = |\bar{b}|^2 + |\bar{c}|^2 + 2|\bar{b}||\bar{c}|\cos\theta$

Substitute the given values $|\bar{b}| = 2\sqrt{2}$, $|\bar{c}| = 4$, and $\theta = \dfrac{\pi}{4}$:

$|\bar{b}+\bar{c}|^2 = (2\sqrt{2})^2 + (4)^2 + 2(2\sqrt{2})(4)\cos\left(\dfrac{\pi}{4}\right)$

$|\bar{b}+\bar{c}|^2 = 8 + 16 + 16\sqrt{2} \times \dfrac{1}{\sqrt{2}}$

$|\bar{b}+\bar{c}|^2 = 8 + 16 + 16 = 40$

$|\bar{b}+\bar{c}| = \sqrt{40} = 2\sqrt{10}$

Therefore, the magnitude of $\bar{a}$ is:

$|\bar{a}| = 2(2\sqrt{10}) = 4\sqrt{10}$

Answer: $4 \sqrt{10}$

</details>

---

### Q69. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle ABC with usual notations if $|\overline{\mathrm{BC}}|=8,|\overline{\mathrm{CA}}|=7,|\overline{\mathrm{AB}}|=10$ then the projection of $\overline{\mathrm{AB}}$ on $\overline{\mathrm{AC}}$ is

**Options:**

- **(A)** $\frac{14}{85}$ units
- **(B)** $\frac{1}{85}$ units
- **(C)** $\frac{85}{14}$ units
- **(D)** $\frac{7}{85}$ units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{85}{14}$ units**

**Detailed Solution:**

Given $a = |\overline{\mathrm{BC}}| = 8$, $b = |\overline{\mathrm{CA}}| = 7$, and $c = |\overline{\mathrm{AB}}| = 10$.

The projection of $\overline{\mathrm{AB}}$ on $\overline{\mathrm{AC}}$ is given by $c \cos A$.

Using the cosine rule for $\cos A$:

$\cos A = \dfrac{b^2 + c^2 - a^2}{2bc}$

$\cos A = \dfrac{7^2 + 10^2 - 8^2}{2(7)(10)}$

$\cos A = \dfrac{49 + 100 - 64}{140} = \dfrac{85}{140}$

The projection of $\overline{\mathrm{AB}}$ on $\overline{\mathrm{AC}}$ is:

$c \cos A = 10 \times \dfrac{85}{140} = \dfrac{85}{14}$ units

Answer: $\frac{85}{14}$ units

</details>

---

### Q70. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}$ and $\bar{b}$ be two vectors such that. $|\bar{a}|=1,|\bar{b}|=4, \bar{a} \cdot \bar{b}=2$. If $\overline{\mathrm{c}}=(2 \bar{a} \times \bar{b})-3 \bar{b}$, then the angle between $\overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ is

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $\frac{3 \pi}{4}$
- **(D)** $\frac{5 \pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{5 \pi}{6}$**

**Detailed Solution:**

Given $|\bar{a}|=1$, $|\bar{b}|=4$, and $\bar{a} \cdot \bar{b}=2$.

Let $\alpha$ be the angle between $\bar{b}$ and $\bar{c}$. Then $\cos \alpha = \dfrac{\bar{b} \cdot \bar{c}}{|\bar{b}||\bar{c}|}$.

We have $\bar{c} = 2(\bar{a} \times \bar{b}) - 3\bar{b}$.

Taking the dot product with $\bar{b}$:

$\bar{b} \cdot \bar{c} = \bar{b} \cdot (2(\bar{a} \times \bar{b}) - 3\bar{b}) = 2(\bar{b} \cdot (\bar{a} \times \bar{b})) - 3|\bar{b}|^2$

Since $\bar{b} \cdot (\bar{a} \times \bar{b}) = 0$, we get:

$\bar{b} \cdot \bar{c} = -3(4)^2 = -48$

Now, to find $|\bar{c}|$, we square the expression for $\bar{c}$:

$|\bar{c}|^2 = |2(\bar{a} \times \bar{b}) - 3\bar{b}|^2 = 4|\bar{a} \times \bar{b}|^2 + 9|\bar{b}|^2 - 12((\bar{a} \times \bar{b}) \cdot \bar{b})$

Using Lagrange's identity, $|\bar{a} \times \bar{b}|^2 = |\bar{a}|^2|\bar{b}|^2 - (\bar{a} \cdot \bar{b})^2 = (1)^2(4)^2 - (2)^2 = 16 - 4 = 12$.

Substituting this value:

$|\bar{c}|^2 = 4(12) + 9(16) - 0 = 48 + 144 = 192$

$|\bar{c}| = \sqrt{192} = 8\sqrt{3}$

Now, substituting the values into the cosine formula:

$\cos \alpha = \dfrac{-48}{4 \times 8\sqrt{3}} = \dfrac{-48}{32\sqrt{3}} = \dfrac{-3}{2\sqrt{3}} = -\dfrac{\sqrt{3}}{2}$

$\alpha = \dfrac{5\pi}{6}$

Answer: $\frac{5 \pi}{6}$

</details>

---

### Q71. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overline{\mathrm{u}}, \overline{\mathrm{v}}, \overline{\mathrm{w}}$ be the vectors such that $|\overline{\mathrm{u}}|=1,|\overline{\mathrm{v}}|=2,|\overline{\mathrm{w}}|=3$. If the projection $\overline{\mathrm{v}}$ along $\overline{\mathrm{u}}$ is equal to that of $\overline{\mathrm{w}}$ along $\overline{\mathrm{u}}$ and the vectors $\overline{\mathrm{v}}$, $\overline{\mathrm{w}}$ are perpendicular to each other then $|\overline{\mathrm{u}}-\overline{\mathrm{v}}+\overline{\mathrm{w}}|$ equals

**Options:**

- **(A)** $\sqrt{14}$
- **(B)** $14$
- **(C)** $\sqrt{7}$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{14}$**

**Detailed Solution:**

Given $|\overline{\mathrm{u}}|=1$, $|\overline{\mathrm{v}}|=2$, $|\overline{\mathrm{w}}|=3$.

The projection of $\overline{\mathrm{v}}$ along $\overline{\mathrm{u}}$ is $\dfrac{\overline{\mathrm{v}} \cdot \overline{\mathrm{u}}}{|\overline{\mathrm{u}}|}$.

The projection of $\overline{\mathrm{w}}$ along $\overline{\mathrm{u}}$ is $\dfrac{\overline{\mathrm{w}} \cdot \overline{\mathrm{u}}}{|\overline{\mathrm{u}}|}$.

Equating the two projections, we get $\overline{\mathrm{v}} \cdot \overline{\mathrm{u}} = \overline{\mathrm{w}} \cdot \overline{\mathrm{u}}$.

Since $\overline{\mathrm{v}}$ and $\overline{\mathrm{w}}$ are perpendicular to each other, $\overline{\mathrm{v}} \cdot \overline{\mathrm{w}} = 0$.

Now, consider $|\overline{\mathrm{u}}-\overline{\mathrm{v}}+\overline{\mathrm{w}}|^2$:

$|\overline{\mathrm{u}}-\overline{\mathrm{v}}+\overline{\mathrm{w}}|^2 = |\overline{\mathrm{u}}|^2 + |\overline{\mathrm{v}}|^2 + |\overline{\mathrm{w}}|^2 - 2(\overline{\mathrm{u}} \cdot \overline{\mathrm{v}}) + 2(\overline{\mathrm{u}} \cdot \overline{\mathrm{w}}) - 2(\overline{\mathrm{v}} \cdot \overline{\mathrm{w}})$

Substituting the values and relations:

$|\overline{\mathrm{u}}-\overline{\mathrm{v}}+\overline{\mathrm{w}}|^2 = 1^2 + 2^2 + 3^2 - 2(\overline{\mathrm{u}} \cdot \overline{\mathrm{v}}) + 2(\overline{\mathrm{u}} \cdot \overline{\mathrm{v}}) - 2(0)$

$|\overline{\mathrm{u}}-\overline{\mathrm{v}}+\overline{\mathrm{w}}|^2 = 1 + 4 + 9 = 14$

Taking the square root, we get $|\overline{\mathrm{u}}-\overline{\mathrm{v}}+\overline{\mathrm{w}}| = \sqrt{14}$.

Answer: $\sqrt{14}$

</details>

---

### Q72. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\overline{\mathrm{a}}=\hat{\mathrm{i}}-2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}$ and $\overline{\mathrm{b}}=2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}-\hat{\mathrm{k}}$ are two vectors, then the angle between the vectors $3 \bar{a}+5 \bar{b}$ and $5 \bar{a}+3 \bar{b}$ is

**Options:**

- **(A)** $\cos ^{-1}\left(\frac{10}{19}\right)$
- **(B)** $\cos ^{-1}\left(\frac{11}{19}\right)$
- **(C)** $\cos ^{-1}\left(\frac{13}{19}\right)$
- **(D)** $\cos ^{-1}\left(\frac{14}{19}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\cos ^{-1}\left(\frac{13}{19}\right)$**

**Detailed Solution:**

Let $\vec{u} = 3\bar{a} + 5\bar{b}$ and $\vec{v} = 5\bar{a} + 3\bar{b}$.

Substituting the given vectors $\bar{a} = \hat{i} - 2\hat{j} + 3\hat{k}$ and $\bar{b} = 2\hat{i} + 3\hat{j} - \hat{k}$:

$\vec{u} = 3(\hat{i} - 2\hat{j} + 3\hat{k}) + 5(2\hat{i} + 3\hat{j} - \hat{k})$
$\vec{u} = (3\hat{i} - 6\hat{j} + 9\hat{k}) + (10\hat{i} + 15\hat{j} - 5\hat{k})$
$\vec{u} = 13\hat{i} + 9\hat{j} + 4\hat{k}$

$\vec{v} = 5(\hat{i} - 2\hat{j} + 3\hat{k}) + 3(2\hat{i} + 3\hat{j} - \hat{k})$
$\vec{v} = (5\hat{i} - 10\hat{j} + 15\hat{k}) + (6\hat{i} + 9\hat{j} - 3\hat{k})$
$\vec{v} = 11\hat{i} - \hat{j} + 12\hat{k}$

The dot product of $\vec{u}$ and $\vec{v}$ is:
$\vec{u} \cdot \vec{v} = (13)(11) + (9)(-1) + (4)(12)$
$\vec{u} \cdot \vec{v} = 143 - 9 + 48 = 182$

The magnitudes of $\vec{u}$ and $\vec{v}$ are:
$|\vec{u}| = \sqrt{13^2 + 9^2 + 4^2} = \sqrt{169 + 81 + 16} = \sqrt{266}$
$|\vec{v}| = \sqrt{11^2 + (-1)^2 + 12^2} = \sqrt{121 + 1 + 144} = \sqrt{266}$

The angle $\theta$ between the vectors is given by $\cos \theta = \dfrac{\vec{u} \cdot \vec{v}}{|\vec{u}| |\vec{v}|}$:
$\cos \theta = \dfrac{182}{\sqrt{266} \times \sqrt{266}} = \dfrac{182}{266}$

Simplifying the fraction:
$\cos \theta = \dfrac{91}{133} = \dfrac{13 \times 7}{19 \times 7} = \dfrac{13}{19}$

$\theta = \cos^{-1}\left(\dfrac{13}{19}\right)$

Answer: $\cos ^{-1}\left(\frac{13}{19}\right)$

</details>

---

### Q73. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$ are two unit vectors such that $\overline{\mathrm{a}}+2 \overline{\mathrm{~b}}$ and $5 \bar{a}-4 \bar{b}$ are perpendicular to each other, then the angle between $\bar{a}$ and $\bar{b}$ is

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\cos ^{-1}\left(\frac{1}{3}\right)$
- **(D)** $\quad \cos ^{-1}\left(\frac{3}{7}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{3}$**

**Detailed Solution:**

Given $|\vec{a}| = 1$ and $|\vec{b}| = 1$.

Since the vectors $\vec{a} + 2\vec{b}$ and $5\vec{a} - 4\vec{b}$ are perpendicular, their dot product is zero.

$(\vec{a} + 2\vec{b}) \cdot (5\vec{a} - 4\vec{b}) = 0$

$5|\vec{a}|^2 - 4(\vec{a} \cdot \vec{b}) + 10(\vec{b} \cdot \vec{a}) - 8|\vec{b}|^2 = 0$

$5(1)^2 + 6(\vec{a} \cdot \vec{b}) - 8(1)^2 = 0$

$5 + 6|\vec{a}||\vec{b}|\cos\theta - 8 = 0$

$6\cos\theta - 3 = 0$

$\cos\theta = \dfrac{1}{2}$

$\theta = \dfrac{\pi}{3}$

Answer: $\frac{\pi}{3}$

</details>

---

### Q74. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the vectors $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}$ be such that $|\bar{a}|=2 ;|\vec{b}|=4$ and $|\bar{c}|=4$. If the projection of $\bar{b}$ on $\bar{a}$ is equal to the projection of $\bar{c}$ on $\bar{a}$ and $\bar{b}$ is perpendicular to $\bar{c}$, then the value of $|\bar{a}+\bar{b}-\bar{c}|$ is

**Options:**

- **(A)** $2 \sqrt{5}$
- **(B)** 6
- **(C)** 4
- **(D)** $4 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 6**

**Detailed Solution:**

Given $|\bar{a}| = 2$, $|\bar{b}| = 4$, and $|\bar{c}| = 4$.

The projection of $\bar{b}$ on $\bar{a}$ is equal to the projection of $\bar{c}$ on $\bar{a}$.

$\dfrac{\bar{b} \cdot \bar{a}}{|\bar{a}|} = \dfrac{\bar{c} \cdot \bar{a}}{|\bar{a}|}$

$\bar{a} \cdot \bar{b} = \bar{a} \cdot \bar{c}$

Since $\bar{b}$ is perpendicular to $\bar{c}$, we have $\bar{b} \cdot \bar{c} = 0$.

Consider the square of the required magnitude:

$|\bar{a} + \bar{b} - \bar{c}|^2 = |\bar{a}|^2 + |\bar{b}|^2 + |\bar{c}|^2 + 2(\bar{a} \cdot \bar{b}) - 2(\bar{a} \cdot \bar{c}) - 2(\bar{b} \cdot \bar{c})$

Substituting $\bar{a} \cdot \bar{b} = \bar{a} \cdot \bar{c}$ and $\bar{b} \cdot \bar{c} = 0$:

$|\bar{a} + \bar{b} - \bar{c}|^2 = |\bar{a}|^2 + |\bar{b}|^2 + |\bar{c}|^2 + 2(\bar{a} \cdot \bar{b}) - 2(\bar{a} \cdot \bar{b}) - 0$

$|\bar{a} + \bar{b} - \bar{c}|^2 = |\bar{a}|^2 + |\bar{b}|^2 + |\bar{c}|^2$

Substituting the given magnitudes:

$|\bar{a} + \bar{b} - \bar{c}|^2 = (2)^2 + (4)^2 + (4)^2$

$|\bar{a} + \bar{b} - \bar{c}|^2 = 4 + 16 + 16 = 36$

$|\bar{a} + \bar{b} - \bar{c}| = 6$

Answer: 6

</details>

---

### Q75. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{u}=\hat{i}+\hat{j}, \bar{v}=\hat{i}-\hat{j}$ and $\bar{w}=\hat{i}+2 \hat{j}+3 \hat{k}$. If $\hat{n}$ is a unit vector such that $\overline{\mathrm{u}} \cdot \hat{\mathrm{n}}=0$ and $\overline{\mathrm{v}} \cdot \hat{\mathrm{n}}=0$, then $|\overline{\mathrm{w}} \cdot \hat{\mathrm{n}}|$ is equal to

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

Let $\hat{n} = x\hat{i} + y\hat{j} + z\hat{k}$.

Given $\bar{u} = \hat{i} + \hat{j}$ and $\bar{u} \cdot \hat{n} = 0$, we have $x + y = 0$.

Given $\bar{v} = \hat{i} - \hat{j}$ and $\bar{v} \cdot \hat{n} = 0$, we have $x - y = 0$.

Solving these two equations, we get $x = 0$ and $y = 0$.

Since $\hat{n}$ is a unit vector, its magnitude is $1$.

$x^2 + y^2 + z^2 = 1$

$0 + 0 + z^2 = 1 \Rightarrow z = \pm 1$

Thus, $\hat{n} = \pm \hat{k}$.

We are given $\bar{w} = \hat{i} + 2\hat{j} + 3\hat{k}$.

$\bar{w} \cdot \hat{n} = (\hat{i} + 2\hat{j} + 3\hat{k}) \cdot (\pm \hat{k}) = \pm 3$

Therefore, $|\bar{w} \cdot \hat{n}| = |\pm 3| = 3$.

Answer: 3

</details>

---

### Q76. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the vectors $\bar{a}=\hat{i}-\hat{j}+2 \hat{k}, \bar{b}=2 \hat{i}+4 \hat{j}+\hat{k}$ and $\overline{\mathrm{c}}=\mathrm{p} \hat{\mathrm{i}}+\hat{\mathrm{j}}+\mathrm{q} \hat{\mathrm{k}}$ are mutually orthogonal, then $(\mathrm{p}, \mathrm{q})$ is equal to

**Options:**

- **(A)** $(3,-2)$
- **(B)** $(-2,3)$
- **(C)** $(-3,2)$
- **(D)** $(2,-3)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(-3,2)$**

**Detailed Solution:**

Since the vectors are mutually orthogonal, their dot products with each other must be zero. Therefore, $\bar{a} \cdot \bar{c} = 0$ and $\bar{b} \cdot \bar{c} = 0$.

$\bar{a} \cdot \bar{c} = (\hat{i} - \hat{j} + 2\hat{k}) \cdot (p\hat{i} + \hat{j} + q\hat{k}) = 0$

$p - 1 + 2q = 0 \Rightarrow p + 2q = 1$

$\bar{b} \cdot \bar{c} = (2\hat{i} + 4\hat{j} + \hat{k}) \cdot (p\hat{i} + \hat{j} + q\hat{k}) = 0$

$2p + 4 + q = 0 \Rightarrow 2p + q = -4$

Multiplying the first equation by $2$, we get:

$2p + 4q = 2$

Subtracting the second equation from this gives:

$(2p + 4q) - (2p + q) = 2 - (-4)$

$3q = 6 \Rightarrow q = 2$

Substituting $q = 2$ into the first equation:

$p + 2(2) = 1 \Rightarrow p = -3$

Therefore, $(p, q) = (-3, 2)$.

Answer: $(-3,2)$

</details>

---

### Q77. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$ are two unit vectors such that $5 \bar{a}+4 \bar{b}$ and $\bar{a}-2 \bar{b}$ are perpendicular to each other, then the angle between $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$ is

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{2 \pi}{3}$
- **(C)** $\cos ^{-1}\left(\frac{2}{3}\right)$
- **(D)** $\quad \cos ^{-1}\left(\frac{1}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2 \pi}{3}$**

**Detailed Solution:**

Since $5\bar{a} + 4\bar{b}$ and $\bar{a} - 2\bar{b}$ are perpendicular to each other, their dot product is zero.

$(5\bar{a} + 4\bar{b}) \cdot (\bar{a} - 2\bar{b}) = 0$

$5(\bar{a} \cdot \bar{a}) - 10(\bar{a} \cdot \bar{b}) + 4(\bar{b} \cdot \bar{a}) - 8(\bar{b} \cdot \bar{b}) = 0$

Since $\bar{a}$ and $\bar{b}$ are unit vectors, $|\bar{a}| = 1$ and $|\bar{b}| = 1$. Let $\theta$ be the angle between them, so $\bar{a} \cdot \bar{b} = |\bar{a}||\bar{b}|\cos\theta = \cos\theta$.

$5(1)^2 - 6\cos\theta - 8(1)^2 = 0$

$-3 - 6\cos\theta = 0$

$\cos\theta = -\dfrac{1}{2}$

$\theta = \dfrac{2\pi}{3}$

Answer: $\frac{2 \pi}{3}$

</details>

---

### Q78. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $\overline{\mathrm{a}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}, \overline{\mathrm{b}}=\hat{\mathrm{i}}-\hat{\mathrm{j}}+\hat{\mathrm{k}}$ and $\overline{\mathrm{c}}=\hat{\mathrm{i}}-\hat{\mathrm{j}}-\hat{\mathrm{k}}$ be three vectors. A vector $\overline{\mathrm{v}}$ in the plane of $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$, whose projection on $\overline{\mathrm{c}}$ is $\frac{1}{\sqrt{3}}$, is given by

**Options:**

- **(A)** $\hat{i}-3 \hat{j}+3 \hat{k}$
- **(B)** $-3 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}-\hat{\mathrm{k}}$
- **(C)** $\quad 3 \hat{i}-\hat{j}+3 \hat{k}$
- **(D)** $\hat{i}+3 \hat{j}-3 \hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\quad 3 \hat{i}-\hat{j}+3 \hat{k}$**

**Detailed Solution:**

Let the vector $\overline{\mathrm{v}}$ in the plane of $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$ be given by:

$\overline{\mathrm{v}} = x\overline{\mathrm{a}} + y\overline{\mathrm{b}}$

Substituting the given vectors $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$:

$\overline{\mathrm{v}} = x(\hat{\mathrm{i}} + \hat{\mathrm{j}} + \hat{\mathrm{k}}) + y(\hat{\mathrm{i}} - \hat{\mathrm{j}} + \hat{\mathrm{k}})$

$\overline{\mathrm{v}} = (x+y)\hat{\mathrm{i}} + (x-y)\hat{\mathrm{j}} + (x+y)\hat{\mathrm{k}}$

The projection of $\overline{\mathrm{v}}$ on $\overline{\mathrm{c}}$ is given by $\dfrac{\overline{\mathrm{v}} \cdot \overline{\mathrm{c}}}{|\overline{\mathrm{c}}|}$.

We have $\overline{\mathrm{c}} = \hat{\mathrm{i}} - \hat{\mathrm{j}} - \hat{\mathrm{k}}$, so $|\overline{\mathrm{c}}| = \sqrt{1^2 + (-1)^2 + (-1)^2} = \sqrt{3}$.

Now, compute the dot product $\overline{\mathrm{v}} \cdot \overline{\mathrm{c}}$:

$\overline{\mathrm{v}} \cdot \overline{\mathrm{c}} = (x+y)(1) + (x-y)(-1) + (x+y)(-1)$

$\overline{\mathrm{v}} \cdot \overline{\mathrm{c}} = x + y - x + y - x - y = y - x$

Given that the projection is $\dfrac{1}{\sqrt{3}}$:

$\dfrac{y - x}{\sqrt{3}} = \dfrac{1}{\sqrt{3}} \Rightarrow y - x = 1$

From the expression for $\overline{\mathrm{v}}$, the coefficients of $\hat{\mathrm{i}}$ and $\hat{\mathrm{k}}$ must be equal (both are $x+y$). Checking the given options, only $3\hat{\mathrm{i}} - \hat{\mathrm{j}} + 3\hat{\mathrm{k}}$ has equal $\hat{\mathrm{i}}$ and $\hat{\mathrm{k}}$ components.

Let's verify this option:

$x + y = 3$

$x - y = -1$

Subtracting the second equation from the first gives $2y = 4 \Rightarrow y = 2$, and adding them gives $2x = 2 \Rightarrow x = 1$.

This satisfies $y - x = 2 - 1 = 1$.

Thus, the required vector is $3\hat{\mathrm{i}} - \hat{\mathrm{j}} + 3\hat{\mathrm{k}}$.

Answer: $\quad 3 \hat{i}-\hat{j}+3 \hat{k}$

</details>

---

### Q79. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the vectors $\overline{\mathrm{a}}=\hat{\mathrm{i}}-\hat{\mathrm{j}}+2 \hat{\mathrm{k}}, \overline{\mathrm{b}}=2 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+\hat{\mathrm{k}}$ and $\overline{\mathrm{c}}=\lambda \hat{\mathrm{i}}+\hat{\mathrm{j}}+\mu \hat{\mathrm{k}}$ are mutually orthogonal, then $(\lambda, \mu) \equiv$

**Options:**

- **(A)** $(-3,2)$
- **(B)** $(-2,3)$
- **(C)** $(2,-3)$
- **(D)** $(3,-2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-3,2)$**

**Detailed Solution:**

Since the vectors $\overline{\mathrm{a}}$, $\overline{\mathrm{b}}$, and $\overline{\mathrm{c}}$ are mutually orthogonal, $\overline{\mathrm{c}}$ must be perpendicular to both $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$.

$\overline{\mathrm{a}} \cdot \overline{\mathrm{c}} = 0 \Rightarrow (\hat{\mathrm{i}}-\hat{\mathrm{j}}+2 \hat{\mathrm{k}}) \cdot (\lambda \hat{\mathrm{i}}+\hat{\mathrm{j}}+\mu \hat{\mathrm{k}}) = 0 \Rightarrow \lambda - 1 + 2\mu = 0 \Rightarrow \lambda + 2\mu = 1$

$\overline{\b} \cdot \overline{\mathrm{c}} = 0 \Rightarrow (2 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+\hat{\mathrm{k}}) \cdot (\lambda \hat{\mathrm{i}}+\hat{\mathrm{j}}+\mu \hat{\mathrm{k}}) = 0 \Rightarrow 2\lambda + 4 + \mu = 0 \Rightarrow 2\lambda + \mu = -4$

Solving the two equations:

Multiply the first equation by $2$: $2\lambda + 4\mu = 2$

Subtract the second equation: $(2\lambda + 4\mu) - (2\lambda + \mu) = 2 - (-4) \Rightarrow 3\mu = 6 \Rightarrow \mu = 2$

Substitute $\mu = 2$ in the first equation: $\lambda + 2(2) = 1 \Rightarrow \lambda = -3$

Therefore, $(\lambda, \mu) \equiv (-3, 2)$.

Answer: $(-3,2)$

</details>

---

### Q80. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of unit vectors perpendicular to $\overline{\mathrm{a}}=(1,1,0)$ and $\overline{\mathrm{b}}=(0,1,1)$ is

**Options:**

- **(A)** one.
- **(B)** two.
- **(C)** three.
- **(D)** infinite.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) two.**

**Detailed Solution:**

Given vectors are $\overline{a} = \hat{i} + \hat{j}$ and $\overline{b} = \hat{j} + \hat{k}$.

A vector perpendicular to both $\overline{a}$ and $\overline{b}$ is given by their cross product $\overline{a} \times \overline{b}$.

$\overline{a} \times \overline{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{vmatrix} = \hat{i}(1 - 0) - \hat{j}(1 - 0) + \hat{k}(1 - 0) = \hat{i} - \hat{j} + \hat{k}$

The magnitude of this vector is $|\overline{a} \times \overline{b}| = \sqrt{1^2 + (-1)^2 + 1^2} = \sqrt{3}$.

The unit vectors perpendicular to both $\overline{a}$ and $\overline{b}$ are given by $\pm \dfrac{\overline{a} \times \overline{b}}{|\overline{a} \times \overline{b}|}$.

$\pm \dfrac{1}{\sqrt{3}}(\hat{i} - \hat{j} + \hat{k})$

Thus, there are exactly two such unit vectors.

Answer: two.

</details>

---

### Q81. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\hat{a}=\frac{1}{\sqrt{10}}(3 \hat{i}+\hat{k})$ and $\hat{b}=\frac{1}{7}(2 \hat{i}+3 \hat{j}-6 \hat{k})$, then the value of $(2 \hat{a}-\hat{b}) \cdot[(\hat{a} \times \hat{b}) \times(\hat{a}+2 \hat{b})]$ is

**Options:**

- **(A)** 5
- **(B)** 3
- **(C)** -5
- **(D)** -3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -5**

**Detailed Solution:**

First, let us find the magnitudes of the given vectors $\hat{a}$ and $\hat{b}$:

$|\hat{a}| = \sqrt{\left(\dfrac{3}{\sqrt{10}}\right)^2 + \left(\dfrac{1}{\sqrt{10}}\right)^2} = \sqrt{\dfrac{9}{10} + \dfrac{1}{10}} = 1$

$|\hat{b}| = \sqrt{\left(\dfrac{2}{7}\right)^2 + \left(\dfrac{3}{7}\right)^2 + \left(\dfrac{-6}{7}\right)^2} = \sqrt{\dfrac{4}{49} + \dfrac{9}{49} + \dfrac{36}{49}} = 1$

Thus, $\hat{a}$ and $\hat{b}$ are unit vectors.

Now, let us find the dot product $\hat{a} \cdot \hat{b}$:

$\hat{a} \cdot \hat{b} = \dfrac{1}{\sqrt{10}} \times \dfrac{1}{7} [3(2) + 0(3) + 1(-6)] = \dfrac{1}{7\sqrt{10}} (6 - 6) = 0$

Since $\hat{a} \cdot \hat{b} = 0$, the vectors $\hat{a}$ and $\hat{b}$ are perpendicular.

Using the vector triple product formula $(\vec{x} \times \vec{y}) \times \vec{z} = (\vec{x} \cdot \vec{z})\vec{y} - (\vec{y} \cdot \vec{z})\vec{x}$, we can expand the second part of the given expression:

$(\hat{a} \times \hat{b}) \times (\hat{a} + 2\hat{b}) = [\hat{a} \cdot (\hat{a} + 2\hat{b})]\hat{b} - [\hat{b} \cdot (\hat{a} + 2\hat{b})]\hat{a}$

Evaluating the dot products inside the brackets:

$\hat{a} \cdot (\hat{a} + 2\hat{b}) = |\hat{a}|^2 + 2(\hat{a} \cdot \hat{b}) = 1 + 0 = 1$

$\hat{b} \cdot (\hat{a} + 2\hat{b}) = (\hat{a} \cdot \hat{b}) + 2|\hat{b}|^2 = 0 + 2(1) = 2$

Substituting these values back, we get:

$(\hat{a} \times \hat{b}) \times (\hat{a} + 2\hat{b}) = 1\hat{b} - 2\hat{a} = \hat{b} - 2\hat{a}$

Now, substitute this into the original expression:

$(2\hat{a} - \hat{b}) \cdot [(\hat{a} \times \hat{b}) \times (\hat{a} + 2\hat{b})] = (2\hat{a} - \hat{b}) \cdot (\hat{b} - 2\hat{a})$

Taking the negative sign out:

$= -(2\hat{a} - \hat{b}) \cdot (2\hat{a} - \hat{b}) = -|2\hat{a} - \hat{b}|^2$

Expanding the magnitude squared:

$|2\hat{a} - \hat{b}|^2 = 4|\hat{a}|^2 + |\hat{b}|^2 - 4(\hat{a} \cdot \hat{b}) = 4(1) + 1 - 0 = 5$

Therefore, the value of the given expression is $-5$.

Answer: -5

</details>

---

### Q82. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$ are two unit vectors such that $5 \bar{a}+4 \bar{b}$ and $\bar{a}-2 \bar{b}$ are perpendicular to each other, then the between $\bar{a}$ and $\bar{b}$ is

**Options:**

- **(A)** $\frac{2 \pi}{3}$
- **(B)** $\cos ^{-1}\left(\frac{2}{3}\right)$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\cos ^{-1}\left(\frac{1}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2 \pi}{3}$**

**Detailed Solution:**

Given $|\bar{a}| = 1$ and $|\bar{b}| = 1$.

Since the vectors $5\bar{a} + 4\bar{b}$ and $\bar{a} - 2\bar{b}$ are perpendicular, their dot product is zero.

$(5\bar{a} + 4\bar{b}) \cdot (\bar{a} - 2\bar{b}) = 0$

$5|\bar{a}|^2 - 10(\bar{a} \cdot \bar{b}) + 4(\bar{b} \cdot \bar{a}) - 8|\bar{b}|^2 = 0$

Substituting $|\bar{a}| = 1$ and $|\bar{b}| = 1$:

$5(1)^2 - 6(\bar{a} \cdot \bar{b}) - 8(1)^2 = 0$

$-3 - 6(\bar{a} \cdot \bar{b}) = 0$

$\bar{a} \cdot \bar{b} = -\dfrac{1}{2}$

Using the definition of dot product, $\bar{a} \cdot \bar{b} = |\bar{a}||\bar{b}|\cos\theta$:

$(1)(1)\cos\theta = -\dfrac{1}{2}$

$\cos\theta = -\dfrac{1}{2}$

$\theta = \dfrac{2\pi}{3}$

Answer: $\frac{2 \pi}{3}$

</details>

---

### Q83. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\overline{\mathrm{a}}=2 \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}, \quad \overline{\mathrm{b}}=-\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}}$ and $\overline{\mathrm{c}}=3 \hat{\mathrm{i}}+\hat{\mathrm{j}}$ such that $\bar{b}+\lambda \bar{a}$ is perpendicular to $\bar{c}$, then $\lambda$ is

**Options:**

- **(A)** $\dfrac{1}{2}$
- **(B)** $\dfrac{1}{4}$
- **(C)** $\dfrac{1}{6}$
- **(D)** $\dfrac{1}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{8}$**

**Detailed Solution:**

Given vectors are $\vec{a} = 2\hat{i} + 2\hat{j} + 3\hat{k}$, $\vec{b} = -\hat{i} + 2\hat{j} + \hat{k}$, and $\vec{c} = 3\hat{i} + \hat{j}$.

Since $\vec{b} + \lambda \vec{a}$ is perpendicular to $\vec{c}$, their dot product must be zero:

$(\vec{b} + \lambda \vec{a}) \cdot \vec{c} = 0$

$\vec{b} \cdot \vec{c} + \lambda (\vec{a} \cdot \vec{c}) = 0$

Calculating the dot products:

$\vec{b} \cdot \vec{c} = (-\hat{i} + 2\hat{j} + \hat{k}) \cdot (3\hat{i} + \hat{j}) = -3 + 2 = -1$

$\vec{a} \cdot \vec{c} = (2\hat{i} + 2\hat{j} + 3\hat{k}) \cdot (3\hat{i} + \hat{j}) = 6 + 2 = 8$

Substituting these values into the equation:

$-1 + \lambda(8) = 0$

$8\lambda = 1$

$\lambda = \dfrac{1}{8}$

Answer: $\dfrac{1}{8}$

</details>

---

### Q84. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}=\hat{j}-\hat{k}$ and $\bar{c}=\hat{i}-\hat{j}-\hat{k}$, then the vector $\bar{b}$ satisfying $\bar{a} \times \bar{b}+\bar{c}=\overline{0}$ and $\bar{a} \cdot \bar{b}=3$ is

**Options:**

- **(A)** $-\hat{i}+2 \hat{j}-2 \hat{k}$
- **(B)** $\mathrm{-\hat{i} + \hat{j} - 2\hat{k}}$
- **(C)** $-\hat{i}-\hat{j}+\hat{k}$
- **(D)** $\hat{i}+\hat{j}+\hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{-\hat{i} + \hat{j} - 2\hat{k}}$**

**Detailed Solution:**

Given $\bar{a} \times \bar{b} + \bar{c} = \overline{0}$, we have $\bar{a} \times \bar{b} = -\bar{c}$.

Taking the cross product with $\bar{a}$ on both sides:

$\bar{a} \times (\bar{a} \times \bar{b}) = -\bar{a} \times \bar{c}$

Using the vector triple product expansion:

$(\bar{a} \cdot \bar{b})\bar{a} - (\bar{a} \cdot \bar{a})\bar{b} = -\bar{a} \times \bar{c}$

We are given $\bar{a} \cdot \bar{b} = 3$. Also, $\bar{a} \cdot \bar{a} = |\hat{j} - \hat{k}|^2 = 1^2 + (-1)^2 = 2$.

Now, calculate $\bar{a} \times \bar{c}$:

$\bar{a} \times \bar{c} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 0 & 1 & -1 \\ 1 & -1 & -1 \end{vmatrix} = \hat{i}(-1 - 1) - \hat{j}(0 - (-1)) + \hat{k}(0 - 1) = -2\hat{i} - \hat{j} - \hat{k}$

Substitute these values into the expanded equation:

$3(\hat{j} - \hat{k}) - 2\bar{b} = -(-2\hat{i} - \hat{j} - \hat{k})$

$3\hat{j} - 3\hat{k} - 2\bar{b} = 2\hat{i} + \hat{j} + \hat{k}$

$2\bar{b} = -2\hat{i} + 2\hat{j} - 4\hat{k}$

$\bar{b} = -\hat{i} + \hat{j} - 2\hat{k}$

Answer: $\mathrm{-\hat{i} + \hat{j} - 2\hat{k}}$

</details>

---

### Q85. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The shortest distance between lines $\bar{r}=(\hat{i}+2 \hat{j}-\hat{k})+\lambda(2 \hat{i}+\hat{j}-3 \hat{k})$ and $\bar{r}=(2 \hat{i}-\hat{j}+2 \hat{k})+\mu(\hat{i}-\hat{j}+\hat{k})$ is

**Options:**

- **(A)** $\dfrac{4 \sqrt{2}}{19}$ units
- **(B)** $\dfrac{3 \sqrt{2}}{\sqrt{19}}$ units
- **(C)** $\dfrac{5 \sqrt{2}}{\sqrt{19}}$ units
- **(D)** $\dfrac{2 \sqrt{2}}{\sqrt{19}}$ units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{2 \sqrt{2}}{\sqrt{19}}$ units**

**Detailed Solution:**

The given lines are $\vec{r} = \vec{a}_1 + \lambda \vec{b}_1$ and $\vec{r} = \vec{a}_2 + \mu \vec{b}_2$, where:
$\vec{a}_1 = \hat{i} + 2\hat{j} - \hat{k}$
$\vec{b}_1 = 2\hat{i} + \hat{j} - 3\hat{k}$
$\vec{a}_2 = 2\hat{i} - \hat{j} + 2\hat{k}$
$\vec{b}_2 = \hat{i} - \hat{j} + \hat{k}$

The vector connecting the points on the lines is:
$\vec{a}_2 - \vec{a}_1 = (2 - 1)\hat{i} + (-1 - 2)\hat{j} + (2 - (-1))\hat{k} = \hat{i} - 3\hat{j} + 3\hat{k}$

The cross product of the direction vectors is:
$\vec{b}_1 \times \vec{b}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & -3 \\ 1 & -1 & 1 \end{vmatrix} = \hat{i}(1 - 3) - \hat{j}(2 + 3) + \hat{k}(-2 - 1) = -2\hat{i} - 5\hat{j} - 3\hat{k}$

The magnitude of the cross product is:
$|\vec{b}_1 \times \vec{b}_2| = \sqrt{(-2)^2 + (-5)^2 + (-3)^2} = \sqrt{4 + 25 + 9} = \sqrt{38}$

The dot product of $(\vec{a}_2 - \vec{a}_1)$ and $(\vec{b}_1 \times \vec{b}_2)$ is:
$(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2) = (1)(-2) + (-3)(-5) + (3)(-3) = -2 + 15 - 9 = 4$

The shortest distance $d$ between the two skew lines is given by:
$d = \dfrac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|}$

$d = \dfrac{4}{\sqrt{38}} = \dfrac{4}{\sqrt{2} \times \sqrt{19}} = \dfrac{2\sqrt{2}}{\sqrt{19}}$ units

Answer: $\dfrac{2 \sqrt{2}}{\sqrt{19}}$ units

</details>

---

### Q86. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The vector of magnitude 6 units and perpendicular to vectors $2 \hat{i}+\hat{j}-3 \hat{k}$ and $\hat{i}-2 \hat{j}+\hat{k}$ is

**Options:**

- **(A)** $\quad 2 \sqrt{3}(-\hat{i}+\hat{j}+\hat{k})$
- **(B)** $\quad 2 \sqrt{3}(\hat{\mathrm{i}}-\hat{\mathrm{j}}+\hat{\mathrm{k}})$
- **(C)** $2 \sqrt{3}(\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}})$
- **(D)** $\quad 2 \sqrt{3}(-\hat{\mathrm{i}}-\hat{\mathrm{j}}+\hat{\mathrm{k}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 \sqrt{3}(\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}})$**

**Detailed Solution:**

Let $\vec{a} = 2\hat{i} + \hat{j} - 3\hat{k}$ and $\vec{b} = \hat{i} - 2\hat{j} + \hat{k}$.

A vector perpendicular to both $\vec{a}$ and $\vec{b}$ is given by their cross product $\vec{a} \times \vec{b}$.

$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & -3 \\ 1 & -2 & 1 \end{vmatrix}$

$= \hat{i}(1 - 6) - \hat{j}(2 + 3) + \hat{k}(-4 - 1)$

$= -5\hat{i} - 5\hat{j} - 5\hat{k}$

The magnitude of this vector is $\sqrt{(-5)^2 + (-5)^2 + (-5)^2} = \sqrt{75} = 5\sqrt{3}$.

The unit vector perpendicular to both $\vec{a}$ and $\vec{b}$ is $\hat{n} = \pm \dfrac{-5\hat{i} - 5\hat{j} - 5\hat{k}}{5\sqrt{3}} = \mp \dfrac{\hat{i} + \hat{j} + \hat{k}}{\sqrt{3}}$.

The required vector of magnitude $6$ is $6\hat{n} = \pm 6 \left( \dfrac{\hat{i} + \hat{j} + \hat{k}}{\sqrt{3}} \right) = \pm 2\sqrt{3}(\hat{i} + \hat{j} + \hat{k})$.

Comparing with the given options, $2\sqrt{3}(\hat{i} + \hat{j} + \hat{k})$ is the correct choice.

Answer: $2 \sqrt{3}(\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}})$

</details>

---

### Q87. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $\overline{\mathrm{A}}, \overline{\mathrm{B}}, \overline{\mathrm{C}}$ be vectors of lengths 3 units, 4 units, 5 units respectively. let $\bar{A}$ be perpendicular to $\overline{\mathrm{B}}+\overline{\mathrm{C}}, \overline{\mathrm{B}}$ be perpendicular to $\overline{\mathrm{C}}+\overline{\mathrm{A}}$ and $\overline{\mathrm{C}}$ be perpendicular to $\overline{\mathrm{A}}+\overline{\mathrm{B}}$, then the length of vector $\overline{\mathrm{A}}+\overline{\mathrm{B}}+\overline{\mathrm{C}}$ is

**Options:**

- **(A)** $2 \sqrt{5}$
- **(B)** $\sqrt{30}$
- **(C)** $\sqrt{45}$
- **(D)** $5 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5 \sqrt{2}$**

**Detailed Solution:**

Given $|\vec{A}| = 3$, $|\vec{B}| = 4$, $|\vec{C}| = 5$.

Since $\vec{A}$ is perpendicular to $\vec{B} + \vec{C}$:
$\vec{A} \cdot (\vec{B} + \vec{C}) = 0 \Rightarrow \vec{A} \cdot \vec{B} + \vec{A} \cdot \vec{C} = 0$

Since $\vec{B}$ is perpendicular to $\vec{C} + \vec{A}$:
$\vec{B} \cdot (\vec{C} + \vec{A}) = 0 \Rightarrow \vec{B} \cdot \vec{C} + \vec{B} \cdot \vec{A} = 0$

Since $\vec{C}$ is perpendicular to $\vec{A} + \vec{B}$:
$\vec{C} \cdot (\vec{A} + \vec{B}) = 0 \Rightarrow \vec{C} \cdot \vec{A} + \vec{C} \cdot \vec{B} = 0$

Adding the above three equations, we get:
$2(\vec{A} \cdot \vec{B} + \vec{B} \cdot \vec{C} + \vec{C} \cdot \vec{A}) = 0$

Using the identity for the magnitude of the sum of three vectors:
$|\vec{A} + \vec{B} + \vec{C}|^2 = |\vec{A}|^2 + |\vec{B}|^2 + |\vec{C}|^2 + 2(\vec{A} \cdot \vec{B} + \vec{B} \cdot \vec{C} + \vec{C} \cdot \vec{A})$

Substituting the given values:
$|\vec{A} + \vec{B} + \vec{C}|^2 = 3^2 + 4^2 + 5^2 + 0$

$|\vec{A} + \vec{B} + \vec{C}|^2 = 9 + 16 + 25 = 50$

$|\vec{A} + \vec{B} + \vec{C}| = \sqrt{50} = 5\sqrt{2}$

Answer: $5 \sqrt{2}$

</details>

---

### Q88. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $|\bar{a}|=2,|\bar{b}|=3$ and $\bar{a}, \bar{b}$ are mutually perpendicular vectors, then the area of the triangle whose vertices are $0, a+2 b, a-2 b$ is

**Options:**

- **(A)** 6 sq.units
- **(B)** 12 sq.units
- **(C)** $24$ sq.units
- **(D)** 8 sq.units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 12 sq.units**

**Detailed Solution:**

The area of a triangle with vertices at the origin $\bar{0}$, $\bar{u}$, and $\bar{v}$ is given by $\dfrac{1}{2} |\bar{u} \times \bar{v}|$.

Here, the vertices are $\bar{0}$, $\bar{a} + 2\bar{b}$, and $\bar{a} - 2\bar{b}$.

Let $\bar{u} = \bar{a} + 2\bar{b}$ and $\bar{v} = \bar{a} - 2\bar{b}$.

Calculating the cross product:

$\bar{u} \times \bar{v} = (\bar{a} + 2\bar{b}) \times (\bar{a} - 2\bar{b})$

$\bar{u} \times \bar{v} = \bar{a} \times \bar{a} - 2(\bar{a} \times \bar{b}) + 2(\bar{b} \times \bar{a}) - 4(\bar{b} \times \bar{b})$

Since $\bar{a} \times \bar{a} = \bar{0}$, $\bar{b} \times \bar{b} = \bar{0}$, and $\bar{b} \times \bar{a} = -(\bar{a} \times \bar{b})$:

$\bar{u} \times \bar{v} = -2(\bar{a} \times \bar{b}) - 2(\bar{a} \times \bar{b}) = -4(\bar{a} \times \bar{b})$

The magnitude of the cross product is:

$|\bar{u} \times \bar{v}| = |-4| |\bar{a} \times \bar{b}| = 4 |\bar{a}| |\bar{b}| \sin \theta$

Since $\bar{a}$ and $\bar{b}$ are mutually perpendicular, $\theta = 90^{\circ}$ and $\sin 90^{\circ} = 1$.

$|\bar{u} \times \bar{v}| = 4(2)(3)(1) = 24$

The area of the triangle is:

$\text{Area} = \dfrac{1}{2} |\bar{u} \times \bar{v}| = \dfrac{1}{2}(24) = 12 \text{ sq.units}$

Answer: 12 sq.units

</details>

---

### Q89. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}, \bar{b}$ and $\bar{c}$ be three vectors having magnitudes 1,1 and 2 respectively. If $\overline{\mathrm{a}} \times(\overline{\mathrm{a}} \times \overline{\mathrm{c}})+\overline{\mathrm{b}}=\overline{0}$, then the acute angle between $\overline{\mathrm{a}}$ and $\overline{\mathrm{c}}$ is

**Options:**

- **(A)** $\dfrac{\pi}{3}$
- **(B)** $\dfrac{\pi}{6}$
- **(C)** $\dfrac{\pi}{4}$
- **(D)** $\dfrac{\pi}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\pi}{6}$**

**Detailed Solution:**

Given $|\bar{a}| = 1$, $|\bar{b}| = 1$, $|\bar{c}| = 2$.

The given equation is $\bar{a} \times (\bar{a} \times \bar{c}) + \bar{b} = \bar{0}$.

Using the vector triple product expansion, we have:

$(\bar{a} \cdot \bar{c})\bar{a} - (\bar{a} \cdot \bar{a})\bar{c} + \bar{b} = \bar{0}$

Since $|\bar{a}| = 1$, $\bar{a} \cdot \bar{a} = 1$. Substituting this, we get:

$(\bar{a} \cdot \bar{c})\bar{a} - \bar{c} + \bar{b} = \bar{0}$

$\bar{b} = \bar{c} - (\bar{a} \cdot \bar{c})\bar{a}$

Squaring both sides, we get:

$|\bar{b}|^2 = |\bar{c}|^2 + (\bar{a} \cdot \bar{c})^2 |\bar{a}|^2 - 2(\bar{a} \cdot \bar{c})(\bar{c} \cdot \bar{a})$

Substituting the given magnitudes $|\bar{b}| = 1$, $|\bar{c}| = 2$, and $|\bar{a}| = 1$:

$1^2 = 2^2 + (\bar{a} \cdot \bar{c})^2 (1)^2 - 2(\bar{a} \cdot \bar{c})^2$

$1 = 4 - (\bar{a} \cdot \bar{c})^2$

$(\bar{a} \cdot \bar{c})^2 = 3$

We know that $\bar{a} \cdot \bar{c} = |\bar{a}||\bar{c}|\cos\theta = (1)(2)\cos\theta = 2\cos\theta$, where $\theta$ is the angle between $\bar{a}$ and $\bar{c}$.

$(2\cos\theta)^2 = 3$

$4\cos^2\theta = 3$

$\cos^2\theta = \dfrac{3}{4}$

$\cos\theta = \pm \dfrac{\sqrt{3}}{2}$

Since we need the acute angle, we take $\cos\theta = \dfrac{\sqrt{3}}{2}$.

$\theta = \dfrac{\pi}{6}$

Answer: $\dfrac{\pi}{6}$

</details>

---

### Q90. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\hat{a}$ and $\hat{b}$ be two unit vectors. If the vectors $\bar{c}=\hat{a}+2 \hat{b}$ and $\bar{d}=5 \hat{a}+4 \hat{b}$ are perpendicular to each other, then the angle between $\hat{a}$ and $\hat{b}$ is

**Options:**

- **(A)** $\dfrac{\pi}{6}$
- **(B)** $\cos ^{-1}\left(\dfrac{13}{14}\right)$
- **(C)** $\dfrac{\pi}{3}$
- **(D)** $\quad \cos ^{-1}\left(\dfrac{-13}{14}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\quad \cos ^{-1}\left(\dfrac{-13}{14}\right)$**

**Detailed Solution:**

Given $\bar{c} = \hat{a} + 2\hat{b}$ and $\bar{d} = 5\hat{a} + 4\hat{b}$.

Since $\bar{c}$ and $\bar{d}$ are perpendicular, their dot product is zero:

$\bar{c} \cdot \bar{d} = 0$

$(\hat{a} + 2\hat{b}) \cdot (5\hat{a} + 4\hat{b}) = 0$

$5|\hat{a}|^2 + 4(\hat{a} \cdot \hat{b}) + 10(\hat{b} \cdot \hat{a}) + 8|\hat{b}|^2 = 0$

Since $\hat{a}$ and $\hat{b}$ are unit vectors, $|\hat{a}| = 1$ and $|\hat{b}| = 1$. Let $\theta$ be the angle between $\hat{a}$ and $\hat{b}$, so $\hat{a} \cdot \hat{b} = \cos \theta$.

$5(1) + 14 \cos \theta + 8(1) = 0$

$13 + 14 \cos \theta = 0$

$\cos \theta = \dfrac{-13}{14}$

$\theta = \cos^{-1}\left(\dfrac{-13}{14}\right)$

Answer: $\quad \cos ^{-1}\left(\dfrac{-13}{14}\right)$

</details>

---

### Q91. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\overline{\mathrm{a}}=3 \hat{\mathrm{i}}-\alpha \hat{\mathrm{j}}+\hat{\mathrm{k}}$ and $\overline{\mathrm{b}}=\hat{\mathrm{i}}+\alpha \hat{\mathrm{j}}+3 \hat{\mathrm{k}}$. If the area of the parallelogram whose adjacent sides are represented by the vectors $\bar{a}$ and $\bar{b}$, is $8 \sqrt{3}$ sq. units, then $\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}$ is equal to

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

The given vectors are $\vec{a} = 3\hat{i} - \alpha\hat{j} + \hat{k}$ and $\vec{b} = \hat{i} + \alpha\hat{j} + 3\hat{k}$.

The area of the parallelogram with adjacent sides $\vec{a}$ and $\vec{b}$ is given by $|\vec{a} \times \vec{b}|$.

$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 3 & -\alpha & 1 \\ 1 & \alpha & 3 \end{vmatrix}$

$\vec{a} \times \vec{b} = \hat{i}(-3\alpha - \alpha) - \hat{j}(9 - 1) + \hat{k}(3\alpha - (-\alpha))$

$\vec{a} \times \vec{b} = -4\alpha\hat{i} - 8\hat{j} + 4\alpha\hat{k}$

The magnitude is:

$|\vec{a} \times \vec{b}| = \sqrt{(-4\alpha)^2 + (-8)^2 + (4\alpha)^2}$

$|\vec{a} \times \vec{b}| = \sqrt{16\alpha^2 + 64 + 16\alpha^2} = \sqrt{32\alpha^2 + 64}$

Given that the area is $8\sqrt{3}$ sq. units:

$\sqrt{32\alpha^2 + 64} = 8\sqrt{3}$

Squaring both sides:

$32\alpha^2 + 64 = 64 \times 3$

$32\alpha^2 + 64 = 192$

$32\alpha^2 = 128$

$\alpha^2 = 4$

Now, calculating the dot product $\vec{a} \cdot \vec{b}$:

$\vec{a} \cdot \vec{b} = (3)(1) + (-\alpha)(\alpha) + (1)(3)$

$\vec{a} \cdot \vec{b} = 3 - \alpha^2 + 3 = 6 - \alpha^2$

Substituting $\alpha^2 = 4$:

$\vec{a} \cdot \vec{b} = 6 - 4 = 2$

Answer: 2

</details>

---

### Q92. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\overline{\mathrm{a}}, \overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ be vectors of magnitude 2,3 and 4 respectively. If $\bar{a}$ is perpendicular to $(\bar{b}+\bar{c}), \bar{b}$ is perpendicular to $(\bar{c}+\bar{a})$ and $\vec{c}$ is perpendicular to $(\bar{a}+\bar{b})$, then the magnitude of $\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}$ is equal to

**Options:**

- **(A)** 29
- **(B)** $\sqrt{29}$
- **(C)** 26
- **(D)** $\sqrt{26}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{29}$**

**Detailed Solution:**

Given $|\vec{a}| = 2$, $|\vec{b}| = 3$, and $|\vec{c}| = 4$.

Since $\vec{a}$ is perpendicular to $(\vec{b}+\vec{c})$, we have:

$\vec{a} \cdot (\vec{b} + \vec{c}) = 0 \Rightarrow \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c} = 0$

Similarly, for the other two conditions:

$\vec{b} \cdot (\vec{c} + \vec{a}) = 0 \Rightarrow \vec{b} \cdot \vec{c} + \vec{b} \cdot \vec{a} = 0$

$\vec{c} \cdot (\vec{a} + \vec{b}) = 0 \Rightarrow \vec{c} \cdot \vec{a} + \vec{c} \cdot \vec{b} = 0$

Adding the above three equations, we get:

$2(\vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{c} + \vec{c} \cdot \vec{a}) = 0$

The square of the magnitude of $\vec{a} + \vec{b} + \vec{c}$ is given by:

$|\vec{a} + \vec{b} + \vec{c}|^2 = |\vec{a}|^2 + |\vec{b}|^2 + |\vec{c}|^2 + 2(\vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{c} + \vec{c} \cdot \vec{a})$

Substituting the given values:

$|\vec{a} + \vec{b} + \vec{c}|^2 = 2^2 + 3^2 + 4^2 + 0$

$|\vec{a} + \vec{b} + \vec{c}|^2 = 4 + 9 + 16 = 29$

Taking the square root, we get:

$|\vec{a} + \vec{b} + \vec{c}| = \sqrt{29}$

Answer: $\sqrt{29}$

</details>

---

### Q93. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the area of the parallelogram with $\bar{a}$ and $\bar{b}$ as two adjacent sides is 15 square units, then the area (in square units) of the parallelogram, having $3 \bar{a}+2 \bar{b}$ and $\bar{a}+3 \bar{b}$ as two adjacent sides, is

**Options:**

- **(A)** 45
- **(B)** 75
- **(C)** 105
- **(D)** 120

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 105**

**Detailed Solution:**

The area of the parallelogram with adjacent sides $\bar{a}$ and $\bar{b}$ is given by $|\bar{a} \times \bar{b}| = 15$.

The area of the new parallelogram with adjacent sides $3\bar{a} + 2\bar{b}$ and $\bar{a} + 3\bar{b}$ is $|(3\bar{a} + 2\bar{b}) \times (\bar{a} + 3\bar{b})|$.

Expanding the cross product:

$(3\bar{a} + 2\bar{b}) \times (\bar{a} + 3\bar{b}) = 3(\bar{a} \times \bar{a}) + 9(\bar{a} \times \bar{b}) + 2(\bar{b} \times \bar{a}) + 6(\bar{b} \times \bar{b})$

Since $\bar{a} \times \bar{a} = \bar{0}$, $\bar{b} \times \bar{b} = \bar{0}$, and $\bar{b} \times \bar{a} = -(\bar{a} \times \bar{b})$, we get:

$= \bar{0} + 9(\bar{a} \times \bar{b}) - 2(\bar{a} \times \bar{b}) + \bar{0}$

$= 7(\bar{a} \times \bar{b})$

The required area is $|7(\bar{a} \times \bar{b})| = 7|\bar{a} \times \bar{b}|$.

Substituting the given value:

$= 7 \times 15 = 105$ square units.

Answer: 105

</details>

---

### Q94. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\overline{\mathrm{a}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}, \overline{\mathrm{a}} \cdot \overline{\mathrm{b}}=1$ and $\overline{\mathrm{a}} \times \overline{\mathrm{b}}=\hat{\mathrm{j}}-\hat{\mathrm{k}}$, then $\overline{\mathrm{b}}$ is

**Options:**

- **(A)** $\hat{i}-\hat{j}+\hat{k}$
- **(B)** $2 \hat{j}-\hat{k}$
- **(C)** $\hat{\mathrm{i}}$
- **(D)** $2 \hat{\mathrm{i}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\hat{\mathrm{i}}$**

**Detailed Solution:**

Given $\vec{a} = \hat{i} + \hat{j} + \hat{k}$, $\vec{a} \cdot \vec{b} = 1$, and $\vec{a} \times \vec{b} = \hat{j} - \hat{k}$.

Taking the cross product with $\vec{a}$ on both sides of the equation $\vec{a} \times \vec{b} = \hat{j} - \hat{k}$:

$\vec{a} \times (\vec{a} \times \vec{b}) = \vec{a} \times (\hat{j} - \hat{k})$

Using the vector triple product expansion $\vec{a} \times (\vec{a} \times \vec{b}) = (\vec{a} \cdot \vec{b})\vec{a} - (\vec{a} \cdot \vec{a})\vec{b}$:

$(\vec{a} \cdot \vec{b})\vec{a} - |\vec{a}|^2\vec{b} = (\hat{i} + \hat{j} + \hat{k}) \times (\hat{j} - \hat{k})$

We are given $\vec{a} \cdot \vec{b} = 1$ and we can calculate $|\vec{a}|^2 = 1^2 + 1^2 + 1^2 = 3$.

Evaluating the cross product on the right side:

$(\hat{i} + \hat{j} + \hat{k}) \times (\hat{j} - \hat{k}) = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & 1 \\ 0 & 1 & -1 \end{vmatrix} = \hat{i}(-1 - 1) - \hat{j}(-1 - 0) + \hat{k}(1 - 0) = -2\hat{i} + \hat{j} + \hat{k}$

Substituting these values back into the equation:

$(1)(\hat{i} + \hat{j} + \hat{k}) - 3\vec{b} = -2\hat{i} + \hat{j} + \hat{k}$

$3\vec{b} = (\hat{i} + \hat{j} + \hat{k}) - (-2\hat{i} + \hat{j} + \hat{k})$

$3\vec{b} = 3\hat{i}$

$\vec{b} = \hat{i}$

Answer: $\hat{\mathrm{i}}$

</details>

---

### Q95. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\overline{\mathrm{a}}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-2 \hat{\mathrm{k}}$ and $\overline{\mathrm{b}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}$ If $\overline{\mathrm{c}}$ is a vector such that $\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=|\overline{\mathrm{c}}|$, $|\overline{\mathrm{c}}-\overline{\mathrm{a}}|=2 \sqrt{2}$ and the angle between $(\overline{\mathrm{a}} \times \overline{\mathrm{b}})$ and $\overline{\mathrm{c}}$ is $60^{\circ}$, then the value of $|(\bar{a} \times \bar{b}) \times \bar{c}|$ is

**Options:**

- **(A)** $\dfrac{\sqrt{3}}{2}$
- **(B)** $\dfrac{3 \sqrt{3}}{2}$
- **(C)** $\dfrac{5 \sqrt{3}}{2}$
- **(D)** $\dfrac{\sqrt{3}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3 \sqrt{3}}{2}$**

**Detailed Solution:**

Given $\vec{a} = 2\hat{i} + \hat{j} - 2\hat{k}$, we have $|\vec{a}| = \sqrt{2^2 + 1^2 + (-2)^2} = 3$.

Given $|\vec{c} - \vec{a}| = 2\sqrt{2}$, squaring both sides gives:

$|\vec{c}|^2 + |\vec{a}|^2 - 2\vec{a} \cdot \vec{c} = 8$

Substituting $|\vec{a}| = 3$ and $\vec{a} \cdot \vec{c} = |\vec{c}|$:

$|\vec{c}|^2 + 9 - 2|\vec{c}| = 8$

$|\vec{c}|^2 - 2|\vec{c}| + 1 = 0$

$(|\vec{c}| - 1)^2 = 0 \Rightarrow |\vec{c}| = 1$

Now, we find $\vec{a} \times \vec{b}$:

$\vec{a} \times \vec{b} = (2\hat{i} + \hat{j} - 2\hat{k}) \times (\hat{i} + \hat{j}) = 2\hat{i} - 2\hat{j} + \hat{k}$

The magnitude is $|\vec{a} \times \vec{b}| = \sqrt{2^2 + (-2)^2 + 1^2} = 3$.

The angle between $(\vec{a} \times \vec{b})$ and $\vec{c}$ is $60^{\circ}$.

The magnitude of the cross product is:

$|(\vec{a} \times \vec{b}) \times \vec{c}| = |\vec{a} \times \vec{b}| |\vec{c}| \sin 60^{\circ}$

Substituting the values:

$|(\vec{a} \times \vec{b}) \times \vec{c}| = 3 \times 1 \times \dfrac{\sqrt{3}}{2} = \dfrac{3\sqrt{3}}{2}$

Answer: $\dfrac{3 \sqrt{3}}{2}$

</details>

---

### Q96. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{a}}, \overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ are three non-coplanar vectors, then $(\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}) \cdot[(\overline{\mathrm{a}}+\overline{\mathrm{b}}) \times(\overline{\mathrm{a}}+\overline{\mathrm{c}})]$ equals

**Options:**

- **(A)** 0
- **(B)** $[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$
- **(C)** $2[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$
- **(D)** $-[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$**

**Detailed Solution:**

Expanding the cross product term:

$(\overline{\mathrm{a}}+\overline{\mathrm{b}}) \times(\overline{\mathrm{a}}+\overline{\mathrm{c}}) = \overline{\mathrm{a}} \times \overline{\mathrm{a}} + \overline{\mathrm{a}} \times \overline{\mathrm{c}} + \overline{\mathrm{b}} \times \overline{\mathrm{a}} + \overline{\mathrm{b}} \times \overline{\mathrm{c}}$

Since the cross product of a vector with itself is zero ($\overline{\mathrm{a}} \times \overline{\mathrm{a}} = \overline{0}$), this simplifies to:

$\overline{\mathrm{a}} \times \overline{\mathrm{c}} + \overline{\mathrm{b}} \times \overline{\mathrm{a}} + \overline{\mathrm{b}} \times \overline{\mathrm{c}}$

Taking the dot product with $(\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}})$:

$(\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}) \cdot (\overline{\mathrm{a}} \times \overline{\mathrm{c}} + \overline{\mathrm{b}} \times \overline{\mathrm{a}} + \overline{\mathrm{b}} \times \overline{\mathrm{c}})$

Using the distributive property and the fact that the scalar triple product is zero if any two vectors are identical (e.g., $\overline{\mathrm{a}} \cdot (\overline{\mathrm{a}} \times \overline{\mathrm{c}}) = 0$), we get:

$\overline{\mathrm{a}} \cdot (\overline{\mathrm{b}} \times \overline{\mathrm{c}}) + \overline{\mathrm{b}} \cdot (\overline{\mathrm{a}} \times \overline{\mathrm{c}}) + \overline{\mathrm{c}} \cdot (\overline{\mathrm{b}} \times \overline{\mathrm{a}})$

Writing these in scalar triple product notation:

$[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}] + [\overline{\mathrm{b}} \overline{\mathrm{a}} \overline{\mathrm{c}}] + [\overline{\mathrm{c}} \overline{\mathrm{b}} \overline{\mathrm{a}}]$

Using the properties of the scalar triple product, swapping any two adjacent vectors changes the sign:

$[\overline{\mathrm{b}} \overline{\mathrm{a}} \overline{\mathrm{c}}] = -[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$

$[\overline{\mathrm{c}} \overline{\mathrm{b}} \overline{\mathrm{a}}] = -[\overline{\mathrm{c}} \overline{\mathrm{a}} \overline{\mathrm{b}}] = -[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$

Substituting these values back into the expression:

$[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}] - [\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}] - [\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}] = -[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$

Answer: $-[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$

</details>

---

### Q97. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overline{\mathrm{a}}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-2 \hat{\mathrm{k}}$ and $\overline{\mathrm{b}}=\hat{i}+\hat{\mathrm{j}}$. Let $\overline{\mathrm{c}}$ be a vector such that $|\bar{c}-\bar{a}|=3$ and $|(\bar{a} \times \bar{b}) \times \bar{c}|=3$ and the angle between $\overline{\mathrm{c}}$ and $\overline{\mathrm{a}} \times \overline{\mathrm{b}}$ is $30^{\circ}$, then $\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}$ is equal to

**Options:**

- **(A)** $\dfrac{2 \sqrt{2}}{3}$
- **(B)** 5
- **(C)** $-\dfrac{1}{8}$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

Given $\overline{\mathrm{a}} = 2\hat{\mathrm{i}} + \hat{\mathrm{j}} - 2\hat{\mathrm{k}}$ and $\overline{\mathrm{b}} = \hat{\mathrm{i}} + \hat{\mathrm{j}}$.

First, we find the cross product $\overline{\mathrm{a}} \times \overline{\mathrm{b}}$:

$\overline{\mathrm{a}} \times \overline{\mathrm{b}} = \begin{vmatrix} \hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 2 & 1 & -2 \\ 1 & 1 & 0 \end{vmatrix} = \hat{\mathrm{i}}(0 - (-2)) - \hat{\mathrm{j}}(0 - (-2)) + \hat{\mathrm{k}}(2 - 1) = 2\hat{\mathrm{i}} - 2\hat{\mathrm{j}} + \hat{\mathrm{k}}$

The magnitude of $\overline{\mathrm{a}} \times \overline{\mathrm{b}}$ is:

$|\overline{\mathrm{a}} \times \overline{\mathrm{b}}| = \sqrt{2^2 + (-2)^2 + 1^2} = \sqrt{9} = 3$

We are given that $|(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}| = 3$ and the angle between $\overline{\mathrm{c}}$ and $\overline{\mathrm{a}} \times \overline{\mathrm{b}}$ is $30^{\circ}$. Using the formula for the magnitude of a cross product:

$|\overline{\mathrm{a}} \times \overline{\mathrm{b}}| |\overline{\mathrm{c}}| \sin(30^{\circ}) = 3$

$3 \times |\overline{\mathrm{c}}| \times \dfrac{1}{2} = 3$

$|\overline{\mathrm{c}}| = 2$

We are also given $|\overline{\mathrm{c}} - \overline{\mathrm{a}}| = 3$. Squaring both sides, we get:

$|\overline{\mathrm{c}}|^2 + |\overline{\mathrm{a}}|^2 - 2(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) = 9$

We know $|\overline{\mathrm{a}}| = \sqrt{2^2 + 1^2 + (-2)^2} = \sqrt{9} = 3$, so $|\overline{\mathrm{a}}|^2 = 9$. Substituting the known values:

$2^2 + 3^2 - 2(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) = 9$

$4 + 9 - 2(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) = 9$

$2(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) = 4$

$\overline{\mathrm{a}} \cdot \overline{\mathrm{c}} = 2$

Answer: 2

</details>

---

### Q98. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}$ are non-coplanar vectors and $\overline{\mathrm{p}}=\dfrac{\overline{\mathrm{b}} \times \overline{\mathrm{c}}}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]}, \overline{\mathrm{q}}=\dfrac{\overline{\mathrm{c}} \times \overline{\mathrm{a}}}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]}, \overline{\mathrm{r}}=\dfrac{\overline{\mathrm{a}} \times \overline{\mathrm{b}}}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]}, \quad$ then $2 \overline{\mathrm{a}} \cdot \overline{\mathrm{p}}+\overline{\mathrm{b}} \cdot \overline{\mathrm{q}}+\overline{\mathrm{c}} \cdot \overline{\mathrm{r}}=$

**Options:**

- **(A)** 0
- **(B)** 3
- **(C)** 4
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

Given $\overline{\mathrm{p}}=\dfrac{\overline{\mathrm{b}} \times \overline{\mathrm{c}}}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]}$, taking the dot product with $\overline{\mathrm{a}}$ gives:

$\overline{\mathrm{a}} \cdot \overline{\mathrm{p}} = \dfrac{\overline{\mathrm{a}} \cdot (\overline{\mathrm{b}} \times \overline{\mathrm{c}})}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]} = \dfrac{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]} = 1$

Similarly, for $\overline{\mathrm{q}}=\dfrac{\overline{\mathrm{c}} \times \overline{\mathrm{a}}}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]}$, taking the dot product with $\overline{\mathrm{b}}$ gives:

$\overline{\mathrm{b}} \cdot \overline{\mathrm{q}} = \dfrac{\overline{\mathrm{b}} \cdot (\overline{\mathrm{c}} \times \overline{\mathrm{a}})}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]} = \dfrac{[\overline{\mathrm{b}} \overline{\mathrm{c}} \overline{\mathrm{a}}]}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]} = \dfrac{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]} = 1$

And for $\overline{\mathrm{r}}=\dfrac{\overline{\mathrm{a}} \times \overline{\mathrm{b}}}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]}$, taking the dot product with $\overline{\mathrm{c}}$ gives:

$\overline{\mathrm{c}} \cdot \overline{\mathrm{r}} = \dfrac{\overline{\mathrm{c}} \cdot (\overline{\mathrm{a}} \times \overline{\mathrm{b}})}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]} = \dfrac{[\overline{\mathrm{c}} \overline{\mathrm{a}} \overline{\mathrm{b}}]}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]} = \dfrac{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]} = 1$

Substituting these values into the given expression:

$2 \overline{\mathrm{a}} \cdot \overline{\mathrm{p}} + \overline{\mathrm{b}} \cdot \overline{\mathrm{q}} + \overline{\mathrm{c}} \cdot \overline{\mathrm{r}} = 2(1) + 1 + 1 = 4$

Answer: 4

</details>

---

### Q99. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}=\hat{i}-2 \hat{j}+3 \hat{k}$ and $\bar{b}=2 \hat{i}+3 \hat{j}-\hat{k}$, then the angle between the vectors $(2 \bar{a}+\bar{b})$ and $(\bar{a}+2 \bar{b})$ is

**Options:**

- **(A)** $\dfrac{\pi}{6}$
- **(B)** $\dfrac{\pi}{3}$
- **(C)** $\dfrac{\pi}{4}$
- **(D)** $\dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\pi}{3}$**

**Detailed Solution:**

Given $\bar{a} = \hat{i} - 2\hat{j} + 3\hat{k}$ and $\bar{b} = 2\hat{i} + 3\hat{j} - \hat{k}$

Evaluating the vector $(2\bar{a} + \bar{b})$:
$2\bar{a} + \bar{b} = 2(\hat{i} - 2\hat{j} + 3\hat{k}) + (2\hat{i} + 3\hat{j} - \hat{k}) = 4\hat{i} - \hat{j} + 5\hat{k}$

Evaluating the vector $(\bar{a} + 2\bar{b})$:
$\bar{a} + 2\bar{b} = (\hat{i} - 2\hat{j} + 3\hat{k}) + 2(2\hat{i} + 3\hat{j} - \hat{k}) = 5\hat{i} + 4\hat{j} + \hat{k}$

Let $\theta$ be the angle between $(2\bar{a} + \bar{b})$ and $(\bar{a} + 2\bar{b})$. Using the dot product formula:
$\cos\theta = \dfrac{(2\bar{a} + \bar{b}) \cdot (\bar{a} + 2\bar{b})}{|2\bar{a} + \bar{b}| |\bar{a} + 2\bar{b}|}$

$\cos\theta = \dfrac{(4)(5) + (-1)(4) + (5)(1)}{\sqrt{4^2 + (-1)^2 + 5^2} \sqrt{5^2 + 4^2 + 1^2}}$

$\cos\theta = \dfrac{20 - 4 + 5}{\sqrt{16 + 1 + 25} \sqrt{25 + 16 + 1}}$

$\cos\theta = \dfrac{21}{\sqrt{42} \sqrt{42}} = \dfrac{21}{42} = \dfrac{1}{2}$

$\theta = \dfrac{\pi}{3}$

Answer: $\dfrac{\pi}{3}$

</details>

---

### Q100. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $|\vec{a}|=\sqrt{27},|\bar{b}|=7$ and $|\vec{a} \times \bar{b}|=35$, then $\bar{a} \cdot \bar{b}$ is equal to

**Options:**

- **(A)** $\sqrt{\dfrac{35}{2}}$
- **(B)** $\dfrac{\sqrt{35}}{2}$
- **(C)** $7 \sqrt{2}$
- **(D)** $\sqrt{35}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $7 \sqrt{2}$**

**Detailed Solution:**

Using Lagrange's identity:

$|\vec{a} \times \vec{b}|^2 + (\vec{a} \cdot \vec{b})^2 = |\vec{a}|^2 |\vec{b}|^2$

Substituting the given values:

$(35)^2 + (\vec{a} \cdot \vec{b})^2 = (\sqrt{27})^2 (7)^2$

$1225 + (\vec{a} \cdot \vec{b})^2 = 27 \times 49$

$1225 + (\vec{a} \cdot \vec{b})^2 = 1323$

$(\vec{a} \cdot \vec{b})^2 = 1323 - 1225 = 98$

$\vec{a} \cdot \vec{b} = \pm \sqrt{98} = \pm 7\sqrt{2}$

Answer: $7 \sqrt{2}$

</details>

---

### Q101. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The area (in sq. units) of the parallelogram whose diagonals are along the vectors $8 \hat{i}-6 \hat{j}$ and $3 \hat{i}+4 \hat{j}-12 \hat{k}$, is

**Options:**

- **(A)** 52
- **(B)** 26
- **(C)** 65
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 65**

**Detailed Solution:**

The area of a parallelogram whose diagonals are given by vectors $\vec{d}_1$ and $\vec{d}_2$ is $\dfrac{1}{2} |\vec{d}_1 \times \vec{d}_2|$.

Given diagonals are:
$\vec{d}_1 = 8\hat{i} - 6\hat{j}$
$\vec{d}_2 = 3\hat{i} + 4\hat{j} - 12\hat{k}$

Calculating the cross product:
$\vec{d}_1 \times \vec{d}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 8 & -6 & 0 \\ 3 & 4 & -12 \end{vmatrix}$

$\vec{d}_1 \times \vec{d}_2 = \hat{i}((-6)(-12) - 0) - \hat{j}(8(-12) - 0) + \hat{k}(8(4) - (-6)(3))$

$\vec{d}_1 \times \vec{d}_2 = 72\hat{i} + 96\hat{j} + 50\hat{k}$

Now, finding the magnitude of the cross product:
$|\vec{d}_1 \times \vec{d}_2| = \sqrt{72^2 + 96^2 + 50^2}$

$|\vec{d}_1 \times \vec{d}_2| = \sqrt{5184 + 9216 + 2500}$

$|\vec{d}_1 \times \vec{d}_2| = \sqrt{16900} = 130$

Therefore, the area of the parallelogram is:
$\text{Area} = \dfrac{1}{2} \times 130 = 65 \text{ sq. units}$

Answer: 65

</details>

---

### Q102. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the triangle, whose vertices are $\mathrm{A} \equiv(1,-1,2), \mathrm{B} \equiv(2,1,-1)$ and $\mathrm{C} \equiv(3,-1,2)$, is

**Options:**

- **(A)** $2 \sqrt{3}$ sq.units
- **(B)** $4 \sqrt{13}$ sq.units
- **(C)** $\sqrt{13}$ sq.units
- **(D)** $4 \sqrt{3}$ sq.units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{13}$ sq.units**

**Detailed Solution:**

The vertices of the triangle are given as $A(1, -1, 2)$, $B(2, 1, -1)$, and $C(3, -1, 2)$.

The vectors representing the sides $\overrightarrow{AB}$ and $\overrightarrow{AC}$ are:
$\overrightarrow{AB} = (2 - 1)\hat{i} + (1 - (-1))\hat{j} + (-1 - 2)\hat{k} = \hat{i} + 2\hat{j} - 3\hat{k}$
$\overrightarrow{AC} = (3 - 1)\hat{i} + (-1 - (-1))\hat{j} + (2 - 2)\hat{k} = 2\hat{i}$

The area of the triangle is given by $\dfrac{1}{2} |\overrightarrow{AB} \times \overrightarrow{AC}|$.

Calculating the cross product:
$\overrightarrow{AB} \times \overrightarrow{AC} = (\hat{i} + 2\hat{j} - 3\hat{k}) \times (2\hat{i})$
$\overrightarrow{AB} \times \overrightarrow{AC} = 2(\hat{i} \times \hat{i}) + 4(\hat{j} \times \hat{i}) - 6(\hat{k} \times \hat{i})$
$\overrightarrow{AB} \times \overrightarrow{AC} = 0 - 4\hat{k} - 6\hat{j} = -6\hat{j} - 4\hat{k}$

Now, finding the magnitude of the cross product:
$|\overrightarrow{AB} \times \overrightarrow{AC}| = \sqrt{(-6)^2 + (-4)^2} = \sqrt{36 + 16} = \sqrt{52} = 2\sqrt{13}$

Area of the triangle $= \dfrac{1}{2} \times 2\sqrt{13} = \sqrt{13}$ sq.units.

Answer: $\sqrt{13}$ sq.units

</details>

---

### Q103. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If C is a given non-zero scalar and $\overline{\mathrm{A}}$ and $\overline{\mathrm{B}}$ are given non-zero vectors such that $\overline{\mathrm{A}}$, is perpendicular to $\overline{\mathrm{B}}$. If vector $\overline{\mathrm{X}}$ is such that $\overline{\mathrm{A}} \cdot \overline{\mathrm{X}}=\mathrm{C}$ and $\overline{\mathrm{A}} \times \overline{\mathrm{X}}=\overline{\mathrm{B}}$ then $\overline{\mathrm{X}}$ is given by

**Options:**

- **(A)** $\dfrac{C \bar{A}+\bar{A} \times \bar{B}}{|\overline{\mathrm{~A}}|^2}$
- **(B)** $\dfrac{\mathrm{C} \overline{\mathrm{A}} \times \overline{\mathrm{B}}}{|\overline{\mathrm{A}}|^2}$
- **(C)** $\dfrac{\mathrm{C} \overline{\mathrm{A}}-\overline{\mathrm{A}} \times \overline{\mathrm{B}}}{|\overline{\mathrm{A}}|^2}$
- **(D)** $\dfrac{C \bar{A}+\bar{B}}{|\overline{\mathrm{~A}}|^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\mathrm{C} \overline{\mathrm{A}}-\overline{\mathrm{A}} \times \overline{\mathrm{B}}}{|\overline{\mathrm{A}}|^2}$**

**Detailed Solution:**

Given $\overline{\mathrm{A}} \times \overline{\mathrm{X}} = \overline{\mathrm{B}}$

Taking the cross product with $\overline{\mathrm{A}}$ on both sides:

$\overline{\mathrm{A}} \times (\overline{\mathrm{A}} \times \overline{\mathrm{X}}) = \overline{\mathrm{A}} \times \overline{\mathrm{B}}$

Using the vector triple product expansion $\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}$:

$(\overline{\mathrm{A}} \cdot \overline{\mathrm{X}})\overline{\mathrm{A}} - (\overline{\mathrm{A}} \cdot \overline{\mathrm{A}})\overline{\mathrm{X}} = \overline{\mathrm{A}} \times \overline{\mathrm{B}}$

We are given $\overline{\mathrm{A}} \cdot \overline{\mathrm{X}} = C$ and we know $\overline{\mathrm{A}} \cdot \overline{\mathrm{A}} = |\overline{\mathrm{A}}|^2$. Substituting these values:

$C\overline{\mathrm{A}} - |\overline{\mathrm{A}}|^2 \overline{\mathrm{X}} = \overline{\mathrm{A}} \times \overline{\mathrm{B}}$

Rearranging the terms to solve for $\overline{\mathrm{X}}$:

$|\overline{\mathrm{A}}|^2 \overline{\mathrm{X}} = C\overline{\mathrm{A}} - \overline{\mathrm{A}} \times \overline{\mathrm{B}}$

$\overline{\mathrm{X}} = \dfrac{C\overline{\mathrm{A}} - \overline{\mathrm{A}} \times \overline{\mathrm{B}}}{|\overline{\mathrm{A}}|^2}$

Answer: $\dfrac{\mathrm{C} \overline{\mathrm{A}}-\overline{\mathrm{A}} \times \overline{\mathrm{B}}}{|\overline{\mathrm{A}}|^2}$

</details>

---

### Q104. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overline{\mathrm{A}}=2 \hat{i}+\hat{k}, \overline{\mathrm{~B}}=\hat{i}+\hat{j}+\hat{k}$ and $\overline{\mathrm{C}}=4 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+7 \hat{\mathrm{k}}$. If a vector $\bar{R}$ satisfies $\bar{R} \times \bar{B}=\bar{C} \times \bar{B}$ and $\overline{\mathrm{R}} \cdot \overline{\mathrm{A}}=0$, then $\overline{\mathrm{R}}$ is given by

**Options:**

- **(A)** $\hat{\mathrm{i}}-8 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}$
- **(B)** $\hat{i}+8 \hat{j}+2 \hat{k}$
- **(C)** $-\hat{\mathrm{i}}-8 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}$
- **(D)** $\quad-\hat{i}-8 \hat{j}-2 \hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\hat{\mathrm{i}}-8 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}$**

**Detailed Solution:**

Given $\vec{R} \times \vec{B} = \vec{C} \times \vec{B}$, we can rewrite this as:

$\vec{R} \times \vec{B} - \vec{C} \times \vec{B} = \vec{0}$

$(\vec{R} - \vec{C}) \times \vec{B} = \vec{0}$

This implies that the vector $(\vec{R} - \vec{C})$ is parallel to $\vec{B}$. Therefore, we can write:

$\vec{R} - \vec{C} = \lambda \vec{B}$

$\vec{R} = \vec{C} + \lambda \vec{B}$

We are also given that $\vec{R} \cdot \vec{A} = 0$. Substituting the expression for $\vec{R}$ into this equation gives:

$(\vec{C} + \lambda \vec{B}) \cdot \vec{A} = 0$

$\vec{C} \cdot \vec{A} + \lambda (\vec{B} \cdot \vec{A}) = 0$

Now, we calculate the dot products $\vec{C} \cdot \vec{A}$ and $\vec{B} \cdot \vec{A}$:

$\vec{C} \cdot \vec{A} = (4\hat{i} - 3\hat{j} + 7\hat{k}) \cdot (2\hat{i} + \hat{k}) = (4)(2) + (-3)(0) + (7)(1) = 8 + 0 + 7 = 15$

$\vec{B} \cdot \vec{A} = (\hat{i} + \hat{j} + \hat{k}) \cdot (2\hat{i} + \hat{k}) = (1)(2) + (1)(0) + (1)(1) = 2 + 0 + 1 = 3$

Substituting these values back into the equation:

$15 + \lambda (3) = 0$

$3\lambda = -15 \Rightarrow \lambda = -5$

Finally, substitute $\lambda = -5$ into the expression for $\vec{R}$:

$\vec{R} = \vec{C} - 5\vec{B}$

$\vec{R} = (4\hat{i} - 3\hat{j} + 7\hat{k}) - 5(\hat{i} + \hat{j} + \hat{k})$

$\vec{R} = (4 - 5)\hat{i} + (-3 - 5)\hat{j} + (7 - 5)\hat{k}$

$\vec{R} = -\hat{i} - 8\hat{j} + 2\hat{k}$

Answer: $-\hat{\mathrm{i}}-8 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}$

</details>

---

### Q105. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For all real $x$, the vectors $C x \hat{i}-6 \hat{j}-3 \hat{k}$ and $x \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+2 \mathrm{C} x \hat{\mathrm{k}}$ make an obtuse angle with each other, then the value of C can be in

**Options:**

- **(A)** $(0,1)$
- **(B)** $\left(-2, \dfrac{-4}{3}\right)$
- **(C)** $\left(\dfrac{-4}{3}, 0\right)$
- **(D)** $\left(0, \dfrac{4}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\dfrac{-4}{3}, 0\right)$**

**Detailed Solution:**

Let the given vectors be $\vec{a} = C x \hat{i} - 6 \hat{j} - 3 \hat{k}$ and $\vec{b} = x \hat{i} + 2 \hat{j} + 2 C x \hat{k}$.

For the angle between the vectors to be obtuse for all real $x$, their dot product must be strictly negative for all real $x$.

$\vec{a} \cdot \vec{b} < 0$

$(C x)(x) + (-6)(2) + (-3)(2 C x) < 0$

$C x^2 - 6 C x - 12 < 0$

This inequality must hold true for all $x \in \mathbb{R}$.

Case 1: If $C = 0$, the inequality becomes $-12 < 0$, which is always true for all real $x$.

Case 2: If $C \neq 0$, for the quadratic expression to be negative for all real $x$, the leading coefficient must be negative and the discriminant must be negative.

$C < 0$ and $D < 0$

$D = (-6 C)^2 - 4(C)(-12) < 0$

$36 C^2 + 48 C < 0$

$12 C (3 C + 4) < 0$

Since $C < 0$, we must have $3 C + 4 > 0$, which gives $C > -\dfrac{4}{3}$.

Thus, $C \in \left(-\dfrac{4}{3}, 0\right)$.

Combining both cases, the complete set of values for $C$ is $\left(-\dfrac{4}{3}, 0\right]$. Among the given options, the value of $C$ can be in $\left(-\dfrac{4}{3}, 0\right)$.

Answer: $\left(\dfrac{-4}{3}, 0\right)$

</details>

---

### Q106. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $x_0$ is the point of local minima of $\mathrm{f}(x)=\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})$ where $\overline{\mathrm{a}}=x \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}$, $\overline{\mathrm{b}}=-2 \hat{\mathrm{i}}+x \hat{\mathrm{j}}-\hat{\mathrm{k}}$, $\overline{\mathrm{c}}=7 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+x \hat{\mathrm{k}}$, then value of $\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}$ at $x=x_0$ is

**Options:**

- **(A)** -3
- **(B)** -15
- **(C)** -12
- **(D)** -9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -15**

**Detailed Solution:**

The function $\mathrm{f}(x)$ is given by the scalar triple product of the vectors $\vec{a}$, $\vec{b}$, and $\vec{c}$:

$\mathrm{f}(x) = \begin{vmatrix} x & -2 & 3 \\ -2 & x & -1 \\ 7 & -2 & x \end{vmatrix}$

Expanding the determinant, we get:

$\mathrm{f}(x) = x(x^2 - 2) - (-2)(-2x + 7) + 3(4 - 7x)$

$\mathrm{f}(x) = x^3 - 2x - 4x + 14 + 12 - 21x$

$\mathrm{f}(x) = x^3 - 27x + 26$

To find the points of local extrema, we differentiate $\mathrm{f}(x)$ with respect to $x$ and set it to zero:

$\mathrm{f}'(x) = 3x^2 - 27 = 0$

$x^2 = 9 \Rightarrow x = \pm 3$

Now, we check the second derivative to determine the nature of the extrema:

$\mathrm{f}''(x) = 6x$

For $x = 3$, $\mathrm{f}''(3) = 18 > 0$, which implies a local minima.

For $x = -3$, $\mathrm{f}''(-3) = -18 < 0$, which implies a local maxima.

Thus, the point of local minima is $x_0 = 3$.

We need to find the value of $\vec{a} \cdot \vec{b}$ at $x = 3$. First, we compute the dot product:

$\vec{a} \cdot \vec{b} = (x)(-2) + (-2)(x) + (3)(-1)$

$\vec{a} \cdot \vec{b} = -2x - 2x - 3 = -4x - 3$

Substituting $x = 3$:

$\vec{a} \cdot \vec{b} = -4(3) - 3 = -12 - 3 = -15$

Answer: -15

</details>

---

### Q107. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}=(2 \hat{i}+2 \hat{j}+3 \hat{k}), \bar{b}=(-\hat{i}+2 \hat{j}+\hat{k}) \quad$ and $\overline{\mathrm{c}}=(3 \hat{\mathrm{i}}+\hat{\mathrm{j}})$ such that $(\overline{\mathrm{a}}+\lambda \overline{\mathrm{b}})$ is perpendicular to $\bar{c}$, then the value of $\lambda$ is

**Options:**

- **(A)** -8
- **(B)** 8
- **(C)** 10
- **(D)** $\dfrac{8}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 8**

**Detailed Solution:**

Given vectors are $\bar{a} = 2\hat{i} + 2\hat{j} + 3\hat{k}$, $\bar{b} = -\hat{i} + 2\hat{j} + \hat{k}$, and $\bar{c} = 3\hat{i} + \hat{j}$.

The vector $(\bar{a} + \lambda \bar{b})$ is given by:

$\bar{a} + \lambda \bar{b} = (2 - \lambda)\hat{i} + (2 + 2\lambda)\hat{j} + (3 + \lambda)\hat{k}$

Since $(\bar{a} + \lambda \bar{b})$ is perpendicular to $\bar{c}$, their dot product must be zero:

$(\bar{a} + \lambda \bar{b}) \cdot \bar{c} = 0$

$((2 - \lambda)\hat{i} + (2 + 2\lambda)\hat{j} + (3 + \lambda)\hat{k}) \cdot (3\hat{i} + \hat{j}) = 0$

$3(2 - \lambda) + 1(2 + 2\lambda) = 0$

$6 - 3\lambda + 2 + 2\lambda = 0$

$8 - \lambda = 0$

$\lambda = 8$

Answer: 8

</details>

---

### Q108. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the vectors $\bar{a}=\hat{i}-\hat{j}+2 \hat{k}, \bar{b}=2 \hat{i}+4 \hat{j}+\hat{k}$ and $\overline{\mathrm{c}}=\mathrm{mi}+\mathrm{j}+\mathrm{nk}$ are mutually perpendicular, then $(\mathrm{m}, \mathrm{n})$ is

**Options:**

- **(A)** $(3,-2)$
- **(B)** $(-2,3)$
- **(C)** $(2,-3)$
- **(D)** $(-3,2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(-3,2)$**

**Detailed Solution:**

Given vectors are $\bar{a} = \hat{i} - \hat{j} + 2\hat{k}$, $\bar{b} = 2\hat{i} + 4\hat{j} + \hat{k}$, and $\bar{c} = m\hat{i} + \hat{j} + n\hat{k}$.

Since the vectors are mutually perpendicular, their dot products with each other must be zero.

$\bar{a} \cdot \bar{c} = 0$

$(1)(m) + (-1)(1) + (2)(n) = 0$

$m + 2n = 1$

$\bar{b} \cdot \bar{c} = 0$

$(2)(m) + (4)(1) + (1)(n) = 0$

$2m + n = -4$

Solving the two equations $m + 2n = 1$ and $2m + n = -4$:

Multiplying the first equation by $2$, we get $2m + 4n = 2$.

Subtracting the second equation from this gives $3n = 6 \Rightarrow n = 2$.

Substituting $n = 2$ in the first equation gives $m + 4 = 1 \Rightarrow m = -3$.

Thus, $(m, n) = (-3, 2)$.

Answer: $(-3,2)$

</details>

---

### Q109. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\overline{\mathrm{a}}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-2 \hat{\mathrm{k}}$ and $\overline{\mathrm{b}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}$. Let $\overline{\mathrm{c}}$ be a vector such that $|\bar{c}-\bar{a}|=3$ and $|(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}|=3$ and the angle between $\overline{\mathrm{c}}$ and $\overline{\mathrm{a}} \times \overline{\mathrm{b}}$ is $30^{\circ}$, then $\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}$ is equal to

**Options:**

- **(A)** 2
- **(B)** $-\dfrac{1}{8}$
- **(C)** $\dfrac{25}{8}$
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

Given $\vec{a} = 2\hat{i} + \hat{j} - 2\hat{k}$ and $\vec{b} = \hat{i} + \hat{j}$.

First, we find the cross product $\vec{a} \times \vec{b}$:

$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & -2 \\ 1 & 1 & 0 \end{vmatrix} = \hat{i}(0 - (-2)) - \hat{j}(0 - (-2)) + \hat{k}(2 - 1) = 2\hat{i} - 2\hat{j} + \hat{k}$

The magnitude of $\vec{a} \times \vec{b}$ is:

$|\vec{a} \times \vec{b}| = \sqrt{2^2 + (-2)^2 + 1^2} = \sqrt{4 + 4 + 1} = 3$

We are given that $|(\vec{a} \times \vec{b}) \times \vec{c}| = 3$ and the angle between $\vec{c}$ and $\vec{a} \times \vec{b}$ is $30^{\circ}$. Using the formula for the magnitude of a cross product:

$|\vec{a} \times \vec{b}| |\vec{c}| \sin(30^{\circ}) = 3$

Substituting the known values:

$3 \times |\vec{c}| \times \dfrac{1}{2} = 3 \Rightarrow |\vec{c}| = 2$

We are also given that $|\vec{c} - \vec{a}| = 3$. Squaring both sides, we get:

$|\vec{c}|^2 + |\vec{a}|^2 - 2(\vec{a} \cdot \vec{c}) = 9$

We calculate the magnitude of $\vec{a}$:

$|\vec{a}| = \sqrt{2^2 + 1^2 + (-2)^2} = \sqrt{4 + 1 + 4} = 3 \Rightarrow |\vec{a}|^2 = 9$

Substituting $|\vec{c}|^2 = 4$ and $|\vec{a}|^2 = 9$ into the equation:

$4 + 9 - 2(\vec{a} \cdot \vec{c}) = 9$

$13 - 2(\vec{a} \cdot \vec{c}) = 9$

$2(\vec{a} \cdot \vec{c}) = 4$

$\vec{a} \cdot \vec{c} = 2$

Answer: 2

</details>

---

### Q110. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $|\overline{\mathrm{a}}|=3 ;|\overline{\mathrm{b}}|=5 ; \overline{\mathrm{b}} \cdot \overline{\mathrm{c}}=10$, angle between $\overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ is $\frac{\pi}{3}, \overline{\mathrm{a}}$ is perpendicular to $\overline{\mathrm{b}} \times \overline{\mathrm{c}}$. Then the value of $|\overline{\mathrm{a}} \times(\overline{\mathrm{b}} \times \overline{\mathrm{c}})|$ is

**Options:**

- **(A)** $20$
- **(B)** $30$
- **(C)** $60$
- **(D)** $40$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $30$**

**Detailed Solution:**

No Solution Available

</details>

---

### Q111. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $x_0$ be the point of local minima of $\mathrm{f}(x)=\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})$ where $\overline{\mathrm{a}}=x \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}$, $\overline{\mathrm{b}}=-2 \hat{\mathrm{i}}+x \hat{\mathrm{j}}-\hat{\mathrm{k}}, \quad \overline{\mathrm{c}}=7 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+x \hat{\mathrm{k}}$, then value of $\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}$ at $x=x_0$ is

**Options:**

- **(A)** 15
- **(B)** -15
- **(C)** 12
- **(D)** -12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -15**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{f}(x)=\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}}) \\
& \quad=\left|\begin{array}{ccc}
x & -2 & 3 \\
-2 & x & -1 \\
7 & -2 & x
\end{array}\right| \\
& \quad=x\left(x^2-2\right)+2(-2 x+7)+3(4-7 x) \\
& \quad \mathrm{f}(x)=x^3-27 x+26 \\
& \quad \text { Now, } \mathrm{f}^{\prime}(x)=0 \\
& \Rightarrow 3 x^2-27=0 \\
& \Rightarrow x^2=9 \\
& \Rightarrow x= \pm 3 \\
& \mathrm{f}^{\prime \prime}(x)=6 x \\
& \Rightarrow \mathrm{f}^{\prime \prime}(x)=18>0
\end{aligned}$
$\therefore \quad \mathrm{f}(x)$ has local minimum at $x=3$.
$\begin{aligned}
\therefore \quad \overline{\mathrm{a}}= & 3 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}} \\
\overline{\mathrm{b}} & =-2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}-\hat{\mathrm{k}} \\
\therefore \quad \overline{\mathrm{a}} \cdot \overline{\mathrm{b}} & =(3 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}) \cdot(-2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}-\hat{\mathrm{k}}) \\
& =3(-2)+(-2)(3)+3(-1) \\
& =-15
\end{aligned}$

</details>

---

### Q112. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\overline{\mathrm{a}}=\hat{\mathrm{i}}+2 \hat{\mathrm{j}}-\hat{\mathrm{k}}$ and $\overline{\mathrm{b}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}-\hat{\mathrm{k}}$ be two vectors. If $\overline{\mathrm{c}}$ is a vector such that $\overline{\mathrm{b}} \times \overline{\mathrm{c}}=\overline{\mathrm{b}} \times \overline{\mathrm{a}}$ and $\overline{\mathrm{c}} \cdot \overline{\mathrm{a}}=0$, then $\overline{\mathrm{c}} \cdot \overline{\mathrm{b}}$ is

**Options:**

- **(A)** $\frac {1}{2}$
- **(B)** $\frac {3}{2}$
- **(C)** $\frac {-3}{2}$
- **(D)** $\frac {-1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac {-1}{2}$**

**Detailed Solution:**

$\begin{aligned}
& \text { Given, } \overline{\mathrm{b}} \times \overline{\mathrm{c}}=\overline{\mathrm{b}} \times \overline{\mathrm{a}} \\
& \Rightarrow \overline{\mathrm{b}} \times(\overline{\mathrm{c}}-\overline{\mathrm{a}})=\overline{0}
\end{aligned}$
$\Rightarrow \overline{\mathrm{b}}$ is parallel to $(\overline{\mathrm{c}}-\overline{\mathrm{a}})$.
$\begin{aligned} & \Rightarrow \overline{\mathrm{c}}-\overline{\mathrm{a}}=\lambda \overline{\mathrm{b}} \text { for some scalar } \lambda \\ & \Rightarrow \overline{\mathrm{c}}=\overline{\mathrm{a}}+\lambda \overline{\mathrm{b}}... (i)) \\ & \Rightarrow \overline{\mathrm{c}} \cdot \overline{\mathrm{a}}=\overline{\mathrm{a}} \cdot \overline{\mathrm{a}}+\lambda(\overline{\mathrm{b}} \cdot \overline{\mathrm{a}})\end{aligned}$
$\Rightarrow 0=|\overline{\mathrm{a}}|^2+\lambda(\overline{\mathrm{b}} \cdot \overline{\mathrm{a}}), \quad \cdots[\because \overline{\mathrm{c}} \cdot \overline{\mathrm{a}}=0$ (given) $]$
$\begin{aligned}
& \Rightarrow 0=6 \pm 4 \lambda \\
& \Rightarrow \lambda=-\frac{3}{2}
\end{aligned}$
Substitutifing the value of $\lambda$ in (i), we get
$\begin{aligned}
\bar{c} & =(\hat{i}+2 \hat{j}-\hat{k})-\frac{3}{2}(\hat{i}+\hat{j}-\hat{k}) \\
= & -\frac{1}{2}(\hat{i}-\hat{j}-\hat{k}) \\
\therefore \quad \bar{c} \cdot \bar{b} & =-\frac{1}{2}(\hat{i}-\hat{j}-\hat{k}) \cdot(\hat{i}+\hat{j}-\hat{k}) \\
& =-\frac{1}{2}(1-1+1)=-\frac{1}{2}
\end{aligned}$

</details>

---

### Q113. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overline{\mathrm{a}}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-2 \hat{\mathrm{k}}$ and $\overline{\mathrm{b}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}$. If $\overline{\mathrm{c}}$ is a vector such that $\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=|\overline{\mathrm{c}}|,|\overline{\mathrm{c}}-\overline{\mathrm{a}}|=2 \sqrt{2}$ and the angle between $\overline{\mathrm{a}} \times \overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ is $\frac{2 \pi}{3}$, then $|(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}|=$

**Options:**

- **(A)** $\frac{\sqrt{3}}{2}$
- **(B)** $\frac{3\sqrt{3}}{2}$
- **(C)** ${3\sqrt{3}}$
- **(D)** ${4\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3\sqrt{3}}{2}$**

**Detailed Solution:**

$\begin{aligned} & |\overline{\mathrm{c}}-\overline{\mathrm{a}}|=2 \sqrt{2} \\ & \Rightarrow|\overrightarrow{\mathrm{c}}|^2+|\overrightarrow{\mathrm{a}}|^2-2(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})=8 \\ & \left.\Rightarrow|\overline{\mathrm{c}}|^2+9-2|\overrightarrow{\mathrm{c}}|=8 \quad \ldots[\because \overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=|\overline{\mathrm{c}}| \text { (given })\right] \\ & \Rightarrow(|\overrightarrow{\mathrm{c}}|-1)^2=0 \\ & \Rightarrow \mid \overrightarrow{\mathrm{c}}=1\end{aligned}$
Now, $\begin{aligned}|(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}| & =|\overline{\mathrm{a}} \times \overline{\mathrm{b}}||\overrightarrow{\mathrm{c}}| \sin \frac{2 \pi}{3} \\ & =|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|(1)\left(\frac{\sqrt{3}}{2}\right) \\ & =\frac{3 \sqrt{3}}{2} \\ & \ldots[\because \overline{\mathrm{a}} \times \overline{\mathrm{b}}=2 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}}]\end{aligned}$

</details>

---

### Q114. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}$ are three vectors with magnitudes $\sqrt{3}$, 1,2 respectively, such that $\overline{\mathrm{a}} \times(\overline{\mathrm{a}} \times \overline{\mathrm{c}})+3 \overline{\mathrm{b}}=\overline{0}$, if $\theta$ is the angle between $\bar{a}$ and $\bar{c}$, then $\sec ^2 \theta$ is

**Options:**

- **(A)** $1$
- **(B)** $\frac{3}{2}$
- **(C)** $\frac{4}{3}$
- **(D)** $\frac{2}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4}{3}$**

**Detailed Solution:**

$\begin{aligned} & \text { Given }|\overline{\mathrm{a}}|=\sqrt{3},|\overline{\mathrm{b}}|=1,|\overline{\mathrm{c}}|=2 \\ & \overline{\mathrm{a}} \times(\overline{\mathrm{a}} \times \overline{\mathrm{c}})+3 \overline{\mathrm{b}}=\overline{0} \\ & \Rightarrow(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) \overline{\mathrm{a}}-(\overline{\mathrm{a}} \cdot \overline{\mathrm{a}}) \overline{\mathrm{c}}+3 \overline{\mathrm{b}}=\overline{0} \\ & \Rightarrow(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) \overline{\mathrm{a}}-3 \overline{\mathrm{c}}=-3 \overline{\mathrm{b}} \quad \ldots\left[\overline{\mathrm{a}} \cdot \overline{\mathrm{a}}=|\overline{\mathrm{a}}|^2=3\right] \\ & \Rightarrow|(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) \overline{\mathrm{a}}-3 \overline{\mathrm{c}}|=|-3 \overline{\mathrm{b}}| \\ & \Rightarrow\left|(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})^{-} \overline{\mathrm{a}}-3 \overline{\mathrm{c}}\right|^2=|-3 \overline{\mathrm{b}}|^2 \\ & \Rightarrow\left|(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})^{-}\right|^2+9|\overline{\mathrm{c}}|^2-6\{(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})\}=9|\overline{\mathrm{b}}|^2 \\ & \Rightarrow(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})^2|\overline{\mathrm{a}}|^2+9|\overline{\mathrm{c}}|^2-6(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})=9|\overline{\mathrm{b}}|^2 \\ & \Rightarrow(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})^2\left(|\overline{\mathrm{a}}|^2-6\right)+9|\overline{\mathrm{c}}|^2=9|\overline{\mathrm{b}}|^2 \\ & \Rightarrow(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})^2(3-6)+9(2)^2=9(1)^2\end{aligned}$
$\begin{aligned} & \Rightarrow-3(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})^2=-27 \\ & \Rightarrow(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})^2=9 \\ & \Rightarrow \overline{\mathrm{a}} \cdot \overline{\mathrm{c}}= \pm 3 \\ & \Rightarrow|\overline{\mathrm{a}}||\overline{\mathrm{c}}| \cos \theta= \pm 3 \\ & \Rightarrow(\sqrt{3})(2) \cos \theta= \pm 3 \\ & \Rightarrow \cos \theta= \pm \frac{\sqrt{3}}{2} \\ & \Rightarrow \sec \theta= \pm \frac{2}{\sqrt{3}} \\ & \Rightarrow \sec ^2 \theta=\frac{4}{3}\end{aligned}$

</details>

---

### Q115. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}$ are unit vectors and $\theta$ is angle between $\overline{\mathrm{a}}$ and $\overline{\mathrm{c}}$ and $\overline{\mathrm{a}}+2 \overline{\mathrm{b}}+2 \overline{\mathrm{c}}=\overline{0}$, then $|\overline{\mathrm{a}} \times \overline{\mathrm{c}}|=$

**Options:**

- **(A)** $\frac{\sqrt{15}}{2}$
- **(B)** $\frac{\sqrt{15}}{4}$
- **(C)** $\sqrt{15}$
- **(D)** $\frac{\sqrt{15}}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\sqrt{15}}{4}$**

**Detailed Solution:**

$$
\begin{aligned}
& \overline{\mathrm{a}}+2 \overline{\mathrm{b}}+2 \overline{\mathrm{c}}=\overline{0} \\
& \Rightarrow \mathrm{a}+2 \overline{\mathrm{c}}=-2 \overline{\mathrm{b}}
\end{aligned}
$$

Squaring on both sides, we get
$$
\begin{aligned}
& |\overline{\mathrm{a}}|^2+4 \overline{\mathrm{a}} \cdot \overline{\mathrm{c}}+4|\overline{\mathrm{c}}|^2=4|\overline{\mathrm{b}}|^2 \\
& \Rightarrow 1+4|\overline{\mathrm{a}}||\overrightarrow{\mathrm{c}}| \cos \theta+4=4 \\
& \Rightarrow \cos \theta=-\frac{1}{4} \\
& \Rightarrow \sin \theta=\frac{\sqrt{15}}{4} \\
& |\overline{\mathrm{a}} \times \overline{\mathrm{c}}|=|\overline{\mathrm{a}}||\overline{\mathrm{c}}| \sin \theta \\
& \quad=(1)(1)\left(\frac{\sqrt{15}}{4}\right)=\frac{\sqrt{15}}{4}
\end{aligned}
$$

</details>

---

### Q116. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}$ be three vectors such that $|\overline{\mathrm{a}}|=\sqrt{3}$, $|\bar{b}|=5, \bar{b} \cdot \bar{c}=10$ and the angle between $\bar{b}$ and $\bar{c}$ is $\frac{\pi}{3}$. If $\overline{\mathrm{a}}$ is perpendicular to the vector $\overline{\mathrm{b}} \times \overline{\mathrm{c}}$, then $|\overline{\mathrm{a}} \times(\overline{\mathrm{b}} \times \overline{\mathrm{c}})|$ is equal to

**Options:**

- **(A)** $10 \sqrt{3}$
- **(B)** $5 \sqrt{3}$
- **(C)** $60$
- **(D)** $30$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $30$**

**Detailed Solution:**

$\begin{aligned} & \overline{\mathrm{b}} \cdot \overline{\mathrm{c}}=10 \\ & \Rightarrow|\overline{\mathrm{b}}||\overline{\mathrm{c}}| \cos \frac{\pi}{3}=10 \\ & \Rightarrow(5)|\overline{\mathrm{c}}|\left(\frac{1}{2}\right)=10 \\ & \Rightarrow|\overline{\mathrm{c}}|=4\end{aligned}$
$\begin{aligned} & |\overline{\mathrm{a}} \times(\overline{\mathrm{b}} \times \overline{\mathrm{c}})|=|\overline{\mathrm{a}}||\overline{\mathrm{b}} \times \overline{\mathrm{c}}| \sin \frac{\pi}{2} \\ & =|\overline{\mathrm{a}}||\overline{\mathrm{b}} \times \overline{\mathrm{c}}| \\ & =|\overline{\mathrm{a}}||\overline{\mathrm{b}}||\overline{\mathrm{c}}| \sin \frac{\pi}{3} \\ & =(\sqrt{3})(5)(4)\left(\frac{\sqrt{3}}{2}\right) \\ & =30\end{aligned}$

</details>

---

### Q117. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

45. If $\overline{\mathrm{a}}=\frac{1}{\sqrt{10}}(3 \hat{\mathrm{i}}+\hat{\mathrm{k}}), \overline{\mathrm{b}}=\frac{1}{7}(2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}-6 \hat{\mathrm{k}})$, then the value of $(2 \overline{\mathrm{a}}-\overline{\mathrm{b}}) \cdot[(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times(\overline{\mathrm{a}}+2 \overline{\mathrm{b}})]$ is

**Options:**

- **(A)** $-3$
- **(B)** 5
- **(C)** 3
- **(D)** $-5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-5$**

**Detailed Solution:**

Since $\bar{a} \cdot \bar{b}=0$
$\therefore \quad \overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$ are perpendicular unit vectors.
Now, $(2 \overline{\mathrm{a}}-\overline{\mathrm{b}}) \cdot[(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times(\overline{\mathrm{a}}+2 \overline{\mathrm{b}})]$
$\begin{aligned} & =[2 \overline{\mathrm{a}}-\overline{\mathrm{b}} \overline{\mathrm{a}} \times \overline{\mathrm{b}} \overline{\mathrm{a}}+2 \overline{\mathrm{b}}] \\ & =-[\overline{\mathrm{a}} \times \overline{\mathrm{b}} 2 \overline{\mathrm{a}}-\overline{\mathrm{b}} \overline{\mathrm{a}}+2 \overline{\mathrm{b}}] \\ & =-(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \cdot\{(2 \overline{\mathrm{a}}-\overline{\mathrm{b}}) \times(\overline{\mathrm{a}}+2 \overline{\mathrm{b}})\} \\ & =-5(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \cdot(\overline{\mathrm{a}} \times \overline{\mathrm{b}})\end{aligned}$
$\begin{array}{ll}=-5|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|^2=-5|\overline{\mathrm{a}}|^2|\overline{\mathrm{b}}|^2 & \ldots . \cdot[\because \overline{\mathrm{a}} \perp \overline{\mathrm{b}}] \\ =-5 & \ldots . \cdot[\because|\overline{\mathrm{a}}|=|\overline{\mathrm{b}}|=1]\end{array}$

</details>

---

### Q118. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\overline{\mathrm{a}}=2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+4 \hat{\mathrm{k}}, \quad \overline{\mathrm{b}}=\hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}}, \quad \overline{\mathrm{c}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}-\hat{\mathrm{k}}$ are three vectors. For a vector $\overline{\mathrm{r}}$ with $\overline{\mathrm{r}} \times \overline{\mathrm{a}}=\overline{\mathrm{b}}$ and $\overline{\mathrm{r}} \cdot \overline{\mathrm{c}}=3,|\overline{\mathrm{r}}|$ is

**Options:**

- **(A)** $\sqrt{55}$
- **(B)** $\sqrt{155}$
- **(C)** $\sqrt{138}$
- **(D)** $\sqrt{170}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{155}$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \overline{\mathrm{r}}=x \hat{\mathrm{i}}+y \hat{\mathrm{j}}+\mathrm{z} \hat{\mathrm{k}} \\ & \overline{\mathrm{r}} \times \overline{\mathrm{a}}=\overline{\mathrm{b}} \\ & \Rightarrow\left|\begin{array}{llr}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ x & y & \mathrm{z} \\ 2 & 3 & 4\end{array}\right|=\overline{\mathrm{b}} \\ & \Rightarrow(4 y-3 \mathrm{z}) \hat{\mathrm{i}}-(4 x-2 \mathrm{z}) \hat{\mathrm{j}}+(3 x-2 y) \hat{\mathrm{k}}=\hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}}\end{aligned}$
$\left.\begin{array}{r}4 y-3 z=1 \\ 4 x-2 z=2 \\ 3 x-2 y=1\end{array}\right)$    ...(i)
$\begin{aligned} & \overline{\mathrm{r}} \cdot \overline{\mathrm{c}}=3 \\ & \Rightarrow(x \hat{\mathrm{i}}+y \hat{\mathrm{j}}+\mathrm{z} \hat{\mathrm{k}}) \cdot(\hat{\mathrm{i}}+\hat{\mathrm{j}}-\hat{\mathrm{k}})=3\end{aligned}$
$\Rightarrow x+y-z=3$             ...(ii)
$x=5, y=7, z=9$
$\begin{aligned} \therefore \quad \overline{\mathrm{r}}= & 5 \hat{\mathrm{i}}+7 \hat{\mathrm{j}}+9 \hat{\mathrm{k}} \\ \Rightarrow|\overline{\mathrm{r}}| & =\sqrt{5^2+7^2+9^2} \\ & =\sqrt{155}\end{aligned}$

</details>

---

### Q119. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\theta$ is angle between the vectors $\bar{a}$ and $\bar{b}$ where $|\bar{a}|=4, \quad|\bar{b}|=3 \quad$ and $\theta \in\left(\frac{\pi}{4}, \frac{\pi}{3}\right)$, then $|(\bar{a}-\bar{b}) \times(\bar{a}+\bar{b})|^2+4(\bar{a} \cdot \bar{b})^2$ has the value

**Options:**

- **(A)** 576
- **(B)** 24
- **(C)** 144
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 576**

**Detailed Solution:**

$\begin{aligned} & |(\overline{\mathrm{a}}-\overline{\mathrm{b}}) \times(\overline{\mathrm{a}}+\overline{\mathrm{b}})|^2+4(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})^2 \\ & =|(\overline{\mathrm{a}} \times \overline{\mathrm{a}})+(\overline{\mathrm{a}} \times \overline{\mathrm{b}})-(\overline{\mathrm{b}} \times \overline{\mathrm{a}})-(\overline{\mathrm{b}} \times \overline{\mathrm{b}})|^2+4(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})^2 \\ & =|(\overline{\mathrm{a}} \times \overline{\mathrm{b}})-(\overline{\mathrm{b}} \times \overline{\mathrm{a}})|^2+4(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})^2 \\ & =|2(\overline{\mathrm{a}} \times \overline{\mathrm{b}})|^2+4(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})^2 \ldots[(\overline{\mathrm{a}} \times \overline{\mathrm{b}})=-(\overline{\mathrm{b}} \times \overline{\mathrm{a}})] \\ & =4|(\overline{\mathrm{a}} \times \overline{\mathrm{b}})|^2+4(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})^2 \\ & =4\left[|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|^2+(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})^2\right] \\ & =4|\overline{\mathrm{a}}|^2|\overline{\mathrm{b}}|^2 \\ & =4(4)^2(3)^2 \\ & =576\end{aligned}$

</details>

---

### Q120. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/9QXW4b_ChkUqDmtwXmxm9Me5IzTPw8zpuLCbdtJUJmM.original.fullsize.png">

**Options:**

- **(A)** $96$
- **(B)** $80$
- **(C)** $42$
- **(D)** $48$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $48$**

**Detailed Solution:**

$\begin{aligned}|\overline{\mathrm{u}} \times \overline{\mathrm{v}}| & =|\overline{\mathrm{u}}||\overline{\mathrm{v}}| \sin \left(150^{\circ}\right) \\ & =8 \times 12 \times \frac{1}{2} \\ & =48\end{aligned}$

</details>

---

### Q121. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The unit vector perpendicular to each of the vectors $\bar{a}+\bar{b}$ and $\bar{a}-\bar{b}$, where $\bar{a}=\hat{i}+\hat{j}+\hat{k}$ and $\overline{\mathrm{b}}=3 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+5 \hat{\mathrm{k}}$ is

**Options:**

- **(A)** $\frac{-14 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+10 \hat{\mathrm{k}}}{\sqrt{312}}$
- **(B)** $\frac{14 \hat{\mathrm{i}}-4 \hat{\mathrm{j}}+10 \hat{\mathrm{k}}}{\sqrt{312}}$
- **(C)** $\frac{14 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+10 \hat{\mathrm{k}}}{\sqrt{312}}$
- **(D)** $\frac{-14 \hat{\mathrm{i}}-4 \hat{\mathrm{j}}+10 \hat{\mathrm{k}}}{\sqrt{312}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-14 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+10 \hat{\mathrm{k}}}{\sqrt{312}}$**

**Detailed Solution:**

$\begin{aligned} \bar{a}+\bar{b} & =(\hat{i}+\hat{j}+\hat{k})+(3 \hat{i}-2 \hat{j}+5 \hat{k}) \\ & =4 \hat{i}-\hat{j}+6 \hat{k} \\ \bar{a}-\bar{b} & =(\hat{i}+\hat{j}+\hat{k})-(3 \hat{i}-2 \hat{j}+5 \hat{k}) \\ & =-2 \hat{i}+3 \hat{j}-4 \hat{k}\end{aligned}$
$\therefore \quad$ Vector perpendicular to $(\bar{a}+\bar{b})$ and $(\bar{a}-\bar{b})$ is
$\left|\begin{array}{ccc}
\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\
4 & -1 & 6 \\
-2 & 3 & -4
\end{array}\right|=-14 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+10 \hat{\mathrm{k}}$
$\therefore \quad$ Required unit vector is
$\frac{-14 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+10 \hat{\mathrm{k}}}{\sqrt{(-14)^2+4^2+(10)^2}}=\frac{-14 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+10 \hat{\mathrm{k}}}{\sqrt{312}}$

</details>

---

### Q122. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\quad \overline{\mathrm{a}}=\hat{\mathrm{i}}+4 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}, \overline{\mathrm{b}}=3 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+7 \hat{\mathrm{k}}, \overline{\mathrm{c}}=2 \hat{\mathrm{i}}-\hat{\mathrm{j}}+4 \hat{\mathrm{k}}$, then a vector $\bar{d}$ which is parallel to vector $\bar{a} \times \bar{b}$ and which $\overline{\mathrm{c}} \cdot \overline{\mathrm{d}}=15$, is

**Options:**

- **(A)** $30 \hat{\mathrm{i}}-\hat{\mathrm{j}}-14 \hat{\mathrm{k}}$
- **(B)** $90 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}-42 \hat{\mathrm{k}}$
- **(C)** $90 \hat{\mathrm{i}}+\hat{\mathrm{j}}-7 \hat{\mathrm{k}}$
- **(D)** $30 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+7 \hat{\mathrm{k}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $90 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}-42 \hat{\mathrm{k}}$**

**Detailed Solution:**

Here, $\bar{c}=2 \hat{i}-\hat{j}+4 \hat{k}$
And given that $\vec{c} \cdot \vec{d}=15$
We verify given options one by one to satisfy the above condition.
Consider option (B),
For $\overline{\mathrm{d}}=90 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}-42 \hat{\mathrm{k}}$
$\begin{aligned}
\overline{\mathrm{c}} \cdot \overline{\mathrm{d}} & =(2)(90)+(-1)(-3)+(4)(-42) \\
& =180+3-168=15
\end{aligned}$
$\therefore \quad$ Option (B) is correct.

</details>

---

### Q123. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}$ and $\bar{b}$ are two unit vectors such that $\bar{a}+2 \bar{b}$ and $5 \bar{a}-4 \bar{b}$ are perpendicular to each other, then the angle between $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$ is

**Options:**

- **(A)** $\left(\frac{\pi}{4}\right)$
- **(B)** $\left(\frac{\pi}{3}\right)$
- **(C)** $\cos ^{-1}\left(\frac{1}{3}\right)$
- **(D)** $\cos ^{-1}\left(\frac{2}{7}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\frac{\pi}{3}\right)$**

**Detailed Solution:**

Since $\overline{\mathrm{a}}+2 \overline{\mathrm{b}}$ and $5 \overline{\mathrm{a}}-4 \overline{\mathrm{b}}$ are perpendicular to each other
$$
\begin{aligned}
& \therefore \quad(\overline{\mathrm{a}}+2 \overline{\mathrm{b}}) \cdot(5 \overline{\mathrm{a}}-4 \overline{\mathrm{b}})=0 \\
& \Rightarrow 5|\overline{\mathrm{a}}|^2-8|\overline{\mathrm{b}}|^2+6 \overline{\mathrm{a}} \cdot \overline{\mathrm{b}}=0 \\
& \Rightarrow-3+6|\overline{\mathrm{a}}||\overline{\mathrm{b}}| \cos \theta=0 \quad \ldots[\because|\overline{\mathrm{a}}|=|\overline{\mathrm{b}}|=1] \\
& \Rightarrow \cos \theta=\frac{1}{2} \\
& \Rightarrow \theta=\frac{\pi}{3}
\end{aligned}
$$

</details>

---

### Q124. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\quad \overline{\mathrm{a}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}, \quad \overline{\mathrm{b}}=2 \hat{\mathrm{j}}-\hat{\mathrm{k}} \quad$ and $\quad \overline{\mathrm{r}} \times \overline{\mathrm{a}}=\overline{\mathrm{b}} \times \overline{\mathrm{a}}$, $\overline{\mathrm{r}} \times \overline{\mathrm{b}}=\overline{\mathrm{a}} \times \overline{\mathrm{b}}$, then the value $\frac{\overline{\mathrm{r}}}{|\overline{\mathrm{r}}|}$ is

**Options:**

- **(A)** $\frac{\hat{\mathrm{i}}+3 \hat{\mathrm{j}}+\hat{\mathrm{k}}}{\sqrt{11}}$
- **(B)** $\frac{\hat{\mathrm{i}}-3 \hat{\mathrm{j}}+\hat{\mathrm{k}}}{\sqrt{11}}$
- **(C)** $\frac{\hat{\mathrm{i}}-3 \hat{\mathrm{j}}-\hat{\mathrm{k}}}{\sqrt{11}}$
- **(D)** $\frac{\hat{\mathrm{i}}+3 \hat{\mathrm{j}}-\hat{\mathrm{k}}}{\sqrt{11}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\hat{\mathrm{i}}+3 \hat{\mathrm{j}}-\hat{\mathrm{k}}}{\sqrt{11}}$**

**Detailed Solution:**

Let $\overline{\mathrm{r}}=x \hat{\mathrm{i}}+y \hat{\mathrm{j}}+z \hat{\mathrm{k}}$ then
$$
\begin{aligned}
& \overline{\mathrm{r}} \times \overline{\mathrm{a}}=\overline{\mathrm{b}} \times \overline{\mathrm{a}} \quad \Rightarrow(\overline{\mathrm{r}}-\overline{\mathrm{b}}) \times \overline{\mathrm{a}}=\overline{0} \\
& \therefore \quad\left|\begin{array}{ccc}
\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\
x & y-2 & \mathrm{z}+1 \\
1 & 1 & 0
\end{array}\right|=\overline{0} \\
& \Rightarrow(-\mathrm{z}-1) \hat{\mathrm{i}}-(-\mathrm{z}-1) \hat{\mathrm{j}}+(x-y+2) \hat{\mathrm{k}}=\overline{0} \\
& \Rightarrow \mathrm{z}=-1, x-y=-2
\end{aligned}
$$

Now, $\overline{\mathrm{r}} \times \overline{\mathrm{b}}=\overline{\mathrm{a}} \times \overline{\mathrm{b}}=(\overline{\mathrm{r}}-\overline{\mathrm{a}}) \times \overline{\mathrm{b}}=\overline{0}$
$$
\begin{aligned}
\therefore \quad & \left|\begin{array}{ccc}
\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\
x-1 & y-1 & z \\
0 & 2 & -1
\end{array}\right|=\overline{0} \\
& \Rightarrow(1-y-2 \mathrm{z}) \hat{\mathrm{i}}-(1-x) \hat{\mathrm{j}}+(2 x-2) \hat{\mathrm{k}}=\overline{0} \\
& \Rightarrow 1-y-2 z=0, x=1
\end{aligned}
$$

Solving (i) and (ii), we get
$$
\begin{aligned}
& x=1, y=3, z=-1 \\
\therefore \quad & \bar{r}=\hat{i}+3 \hat{j}-\hat{k} \\
& |\bar{r}|=\sqrt{1+9+1}=\sqrt{11} \\
\therefore \quad & \frac{\bar{r}}{\left|-\frac{\mathrm{r}}{-}\right|}=\frac{\hat{\mathrm{i}}+3 \hat{\mathrm{j}}-\hat{\mathrm{k}}}{\sqrt{11}}
\end{aligned}
$$

</details>

---

### Q125. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}$ are three vectors such that $\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}}+\overline{\mathrm{c}})+\overline{\mathrm{b}} \cdot(\overline{\mathrm{c}}+\overline{\mathrm{a}})+\overline{\mathrm{c}} \cdot(\overline{\mathrm{a}}+\overline{\mathrm{b}})=0$ and $|\overline{\mathrm{a}}|=1$, $|\overline{\mathrm{b}}|=8$ and $|\overline{\mathrm{c}}|=4$, then $|\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}|$ has the value

**Options:**

- **(A)** $81$
- **(B)** $9$
- **(C)** $5$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $9$**

**Detailed Solution:**

$$
\begin{aligned}
& |\bar{a}|=1,|\bar{b}|=8,|\bar{c}|=4, \text { and } \\
& \bar{a} \cdot(\bar{b}+\bar{c})+\bar{b} \cdot(\bar{c}+\bar{a})+\bar{c} \cdot(\bar{a}+\bar{b})=0 \\
& \Rightarrow 2(\bar{a} \cdot \bar{b}+\bar{b} \cdot \bar{c}+\bar{c} \cdot \bar{a})=0
\end{aligned}
$$

Now,
$$
\begin{aligned}
& |\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}|^2=|\overline{\mathrm{a}}|^2+|\overline{\mathrm{b}}|^2+|\overline{\mathrm{c}}|^2+2(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}+\overline{\mathrm{b}} \cdot \overline{\mathrm{c}}+\overline{\mathrm{c}} \cdot \overline{\mathrm{a}}) \\
& \Rightarrow|\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}|^2=1+64+16+0 \quad \ldots[\text { From (i) }] \\
& \Rightarrow|\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}|^2=81 \\
& \Rightarrow|\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}|=9
\end{aligned}
$$

</details>

---

### Q126. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}$ and $\bar{b}$ are two unit vectors such that $\bar{a}+2 \bar{b}$ and $5 \bar{a}-4 \bar{b}$ are perpendicular to each other, then the angle between $\bar{a}$ and $\bar{b}$ is

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $\frac{2 \pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{3}$**

**Detailed Solution:**

Given that, $\overline{\mathrm{a}}+2 \overline{\mathrm{b}}$ and $5 \overline{\mathrm{a}}-4 \overline{\mathrm{b}}$ are perpendicular to each other.
$\begin{array}{ll}
\therefore \quad(\overline{\mathrm{a}}+2 \overline{\mathrm{b}}) \cdot(5 \overline{\mathrm{a}}-4 \overline{\mathrm{b}})=0 \\
\Rightarrow 5|-\overline{\mathrm{a}}|^2-8|\overline{\mathrm{b}}|^2-4 \overline{\mathrm{a}} \cdot \overline{\mathrm{b}}+10 \overline{\mathrm{b}} \cdot \overline{\mathrm{a}}=0 \\
\Rightarrow-3+6 \overline{\mathrm{a}} \cdot \overline{\mathrm{b}}=0 \ldots[|\bar{a}|=|\bar{b}|=1]\\
\Rightarrow 6|\overline{\mathrm{a}}||\overline{\mathrm{b}}| \cos \theta=3 \\
\Rightarrow \cos \theta=\frac{1}{2} \\
\Rightarrow \theta=\frac{\pi}{3}
\end{array}$

</details>

---

### Q127. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\overline{\mathrm{p}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}$ and $\overline{\mathrm{q}}=\hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}}$. Then a vector of magnitude $5 \sqrt{3}$ units perpendicular to the vector $\overline{\mathrm{q}}$ and coplanar with $\overline{\mathrm{p}}$ and $\overline{\mathrm{q}}$ is

**Options:**

- **(A)** $5(\hat{\mathrm{i}}-\hat{\mathrm{j}}+\hat{\mathrm{k}})$
- **(B)** $5(\hat{i}+\hat{j}-\hat{k})$
- **(C)** $5(\hat{\mathrm{i}}-\hat{\mathrm{j}}-\hat{\mathrm{k}})$
- **(D)** $5(\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5(\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}})$**

**Detailed Solution:**

Let $\bar{r}=a \hat{i}+b \hat{j}+c \hat{k}$
As $\overline{\mathrm{r}}$ is perpendicular to $\overline{\mathrm{q}}$.
$\begin{array}{ll}
\therefore \quad \bar{r} \cdot \bar{q}=0 \\
\quad \Rightarrow a-2 b+c=0 ...(i)
\end{array}$
Also, $\bar{r}$ is coplanar with vectors $\bar{p}$ and $\bar{q}$
$\begin{aligned}
\therefore \quad & {\left[\begin{array}{ccc}
\bar{p} & \overline{\mathrm{q}} & -\mathrm{r}
\end{array}\right]=0 } \\
& \Rightarrow\left|\begin{array}{ccc}
1 & 1 & 1 \\
1 & -2 & 1 \\
\mathrm{a} & \mathrm{b} & \mathrm{c}
\end{array}\right|=0 \\
& \Rightarrow 3 \mathrm{a}-3 \mathrm{c}=0 \\
& \Rightarrow \mathrm{a}-\mathrm{c}=0 \\
& \Rightarrow \mathrm{a}=\mathrm{c}...(ii)
\end{aligned}$
From (i) and (ii), we get
$\mathrm{b}=\mathrm{c}$
$\therefore \quad-\overline{\mathrm{r}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}^{\mathrm{s}}$
Now, the magnitude of required vector is $5 \sqrt{3}$ units.
$\begin{aligned}
\text { Required vector } & =5 \sqrt{3} \times \frac{r}{\sqrt{r}} \\
& =5 \sqrt{3} \times \frac{\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}}{\sqrt{3}}=5(\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}})
\end{aligned}$

</details>

---

### Q128. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $(\bar{a} \times \bar{b}) \times \bar{c}=-5 \bar{a}+4 \bar{b}$ and $\bar{a} \cdot \bar{b}=3$, then the value of $\bar{a} \times(\bar{b} \times \bar{c})$ is

**Options:**

- **(A)** $3 \bar{b}-4 \bar{c}$
- **(B)** $4 \overline{\mathrm{a}}-3 \overline{\mathrm{b}}$
- **(C)** $4 \overline{\mathrm{b}}-3 \overline{\mathrm{c}}$
- **(D)** $3 \bar{a}-4 \bar{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 \overline{\mathrm{b}}-3 \overline{\mathrm{c}}$**

**Detailed Solution:**

$\begin{aligned}
& (\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}=(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) \overline{\mathrm{b}}-(\overline{\mathrm{b}} \cdot \overline{\mathrm{c}}) \overline{\mathrm{a}} \\
& \text { But, }(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}=-5 \overline{\mathrm{a}}+4 \overline{\mathrm{b}} \\
\therefore \quad & -5 \overline{\mathrm{a}}+4 \overline{\mathrm{b}}=(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) \overline{\mathrm{b}}-(\overline{\mathrm{b}} \cdot \overline{\mathrm{c}}) \overline{\mathrm{a}}
\end{aligned}$
Comparing, we get
$\begin{aligned}
\therefore \quad \overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=4 & \\
\overline{\mathrm{a}} \times(\overline{\mathrm{b}} \times \overline{\mathrm{c}}) & =(\overline{\mathrm{a} \cdot} \cdot \overline{\mathrm{c}}) \overline{\mathrm{b}}-(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}) \overline{\mathrm{c}} \\
& =4 \overline{\mathrm{b}}-3 \overline{\mathrm{c}} \quad \ldots[\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}=3 \text { (given) }]
\end{aligned}$

</details>

---

### Q129. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}$ be three non-zero vectors, such that no two of them are collinear and $(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}=\frac{1}{3}|\overline{\mathrm{b}}||\overline{\mathrm{c}}| \overline{\mathrm{a}}$. If $\theta$ is the angle between the vectors $\bar{b}$ and $\bar{c}$, then the value of $\sin \theta$ is

**Options:**

- **(A)** $\frac{2 \sqrt{2}}{3}$
- **(B)** $\frac{-\sqrt{2}}{3}$
- **(C)** $\frac{\sqrt{2}}{3}$
- **(D)** $\sqrt{\frac{2}{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2 \sqrt{2}}{3}$**

**Detailed Solution:**

Given: $(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}=\frac{1}{3}|\overline{\mathrm{b}}||\overline{\mathrm{c}}|^{-}$
We know that,
$(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}=(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) \overline{\mathrm{b}}-(\overline{\mathrm{b}} \cdot \overline{\mathrm{c}}) \overline{\mathrm{a}}^{-}$
On comparing, we get
$\begin{aligned}
& \frac{1}{3}|\overline{\mathrm{b}}||\overrightarrow{\mathrm{c}}|=-\overline{\mathrm{b}} \cdot \overline{\mathrm{c}} \\
\Rightarrow & \frac{1}{3}|\overline{\mathrm{b}}||\overrightarrow{\mathrm{c}}|=-|\overline{\mathrm{b}}||\overrightarrow{\mathrm{c}}| \cos \theta \\
\Rightarrow \cos \theta & =\frac{-1}{3} \\
\Rightarrow \cos ^2 \theta & =\frac{1}{9} \\
\sin ^2 \theta & =1-\cos ^2 \theta \\
& =1-\frac{1}{9} \\
\therefore \quad & \sin ^2 \theta=\frac{8}{9} \\
\therefore \quad & \sin \theta=\sqrt{\frac{8}{9}}=\frac{2 \sqrt{2}}{3}
\end{aligned}$

</details>

---

### Q130. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}=\hat{i}+2 \hat{j}+\hat{k}, \bar{b}=\hat{i}-\hat{j}+\hat{k}, \bar{c}=\hat{i}+\hat{j}-\hat{k}$, then a vector in the plane of $\bar{a}$ and $\bar{b}$, whose projection on $\overline{\mathrm{c}}$ is $\frac{1}{\sqrt{3}}$, is

**Options:**

- **(A)** $\hat{i}+\hat{j}-2 \hat{k}$
- **(B)** $3 \hat{i}+\hat{j}-3 \hat{k}$
- **(C)** $4 \hat{\mathrm{i}}-\hat{\mathrm{j}}+4 \hat{\mathrm{k}}$
- **(D)** $2 \hat{i}+3 \hat{j}-\hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 \hat{\mathrm{i}}-\hat{\mathrm{j}}+4 \hat{\mathrm{k}}$**

**Detailed Solution:**

Let $\overline{\mathrm{r}}$ be the vector coplanar to $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$. Then,
$\begin{aligned}
\overline{\mathrm{r}} & =\overline{\mathrm{a}}+\mathrm{m} \overline{\mathrm{b}} \\
& =(\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}})+\mathrm{m}(\hat{\mathrm{i}}-\hat{\mathrm{j}}+\hat{\mathrm{k}}) \\
& =\hat{\mathrm{i}}(1+\mathrm{m})+\hat{\mathrm{j}}(2-\mathrm{m})+\hat{\mathrm{k}}(1+\mathrm{m})
\end{aligned}$
Since the projection of $\overline{\mathrm{r}}$ along $\overline{\mathrm{c}}$ is $\frac{1}{\sqrt{3}}$,
$\begin{aligned}
& \frac{\overline{\mathrm{r}} \cdot \overline{\mathrm{c}}}{\overline{\mathrm{c}}}= \pm \frac{1}{\sqrt{3}} \\
& \Rightarrow \frac{(1+\mathrm{m})+(2-\mathrm{m})-(1+\mathrm{m})}{\sqrt{3}}= \pm \frac{1}{\sqrt{3}} \\
& \Rightarrow(1+\mathrm{m})+(2-\mathrm{m})-(1+\mathrm{m})= \pm 1 \\
\therefore \quad & \mathrm{m}=3 \text { or } \mathrm{m}=1
\end{aligned}$
Substituting $\mathrm{m}=3$ in equation (i), we get
$\begin{aligned}
& \overline{\mathrm{r}}=\hat{\mathrm{i}}(1+3)+\hat{\mathrm{j}}(2-3)+\hat{\mathrm{k}}(1+3) \\
& \Rightarrow \overline{\mathrm{r}}=4 \hat{\mathrm{i}}-\hat{\mathrm{j}}+4 \hat{\mathrm{k}}
\end{aligned}$

</details>

---

### Q131. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The vectors are $\bar{a}=2 \hat{i}+\hat{j}-2 \hat{k}, \bar{b}=\hat{i}+\hat{j}$. If $\bar{c}$ is a vector such that $\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=|\overline{\mathrm{c}}|$ and $|\overline{\mathrm{c}}-\overline{\mathrm{a}}|=2 \sqrt{2}$, angle between $\overline{\mathrm{a}} \times \overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ is $\frac{\pi}{4}$, then $|(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}|$ is

**Options:**

- **(A)** 3
- **(B)** $\frac{3}{\sqrt{2}}$
- **(C)** $3 \sqrt{2}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{\sqrt{2}}$**

**Detailed Solution:**

Given that angle between $\overline{\mathrm{a}} \times \overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ is $\frac{\pi}{4}$
$\therefore \quad|(\bar{a} \times \bar{b}) \times \bar{c}|=|(\bar{a} \times \bar{b})||\bar{c}| \sin \frac{\pi}{4}$... (i)
Now, $\overline{\mathrm{a}} \times \overline{\mathrm{b}}=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 2 & 1 & -2 \\ 1 & 1 & 0\end{array}\right|$
$\begin{aligned}
& =\hat{\mathrm{i}}(0+2)-\hat{\mathrm{j}}(0+2)+\hat{\mathrm{k}}(2-1) \\
& =2 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}} \\
\therefore \quad \mid & |\overline{\mathrm{a}} \times \overrightarrow{\mathrm{b}}|=\sqrt{2^2+(-2)^2+1}=3
\end{aligned}$
Given, $\overline{\mathrm{a}}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-2 \hat{\mathrm{k}}$
$|\vec{a}|=\sqrt{2^2+1^2+(-2)^2}=3$
Given, $|\overline{\mathrm{c}}-\mathrm{a}|=2 \sqrt{2}$
Squaring on both sides, we get
$\begin{aligned}
& |\overline{\mathrm{c}}|^2+\mid-\mathrm{a}^2-2-\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=8 \\
& \Rightarrow\left|\mathrm{c}^2+3^2-2\right| \mathrm{c} \mid=8 \quad \ldots[\because \cdot \overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=|\overline{\mathrm{c}}|]
\end{aligned}$
$\begin{aligned}
& \Rightarrow|\bar{c}|^2-2|\vec{c}|+1=0 \\
& \Rightarrow(|\bar{c}|-1)^2=0 \\
& \Rightarrow|\vec{c}|=1
\end{aligned}$
From (i),
$\begin{aligned}
|(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}| & =|(\overline{\mathrm{a}} \times \overline{\mathrm{b}})||\overline{\mathrm{c}}| \cdot \sin \frac{\pi}{4} \\
& =3 \times 1 \times \frac{1}{\sqrt{2}} \\
& =\frac{3}{\sqrt{2}}
\end{aligned}$

</details>

---

### Q132. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The vector projection of $\overline{\mathrm{AB}}$ on $\overline{\mathrm{CD}}$, where $A \equiv(2,-3,0), B \equiv(1,-4,-2), C \equiv(4,6,8)$ and $\mathrm{D} \equiv(7,0,10)$, is

**Options:**

- **(A)** $\frac{1}{49}(3 \hat{\mathrm{i}}-6 \hat{\mathrm{j}}+2 \hat{\mathrm{k}})$
- **(B)** $\frac{1}{6}(-\hat{i}-\hat{j}-2 \hat{k})$
- **(C)** $-\frac{1}{49}(3 \hat{i}-6 \hat{j}+2 \hat{k})$
- **(D)** $-\frac{1}{6}(-\hat{\mathrm{i}}-\hat{\mathrm{j}}-2 \hat{\mathrm{k}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{1}{49}(3 \hat{i}-6 \hat{j}+2 \hat{k})$**

**Detailed Solution:**

$\begin{aligned}
& \overline{\mathrm{AB}}=-\hat{\mathrm{i}}-\hat{\mathrm{j}}-2 \hat{\mathrm{k}} \\
& \overline{\mathrm{CD}}=3 \hat{\mathrm{i}}-6 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}
\end{aligned}$
Vector projection of $\overline{\mathrm{AB}}$ on $\overline{\mathrm{CD}}$
$\begin{aligned}
& =(\overline{\mathrm{AB}} \cdot \overline{\mathrm{CD}}) \frac{\overline{\mathrm{CD}}}{|\overline{\mathrm{CD}}|^2} \\
& =(-3+6-4) \frac{(3 \hat{\mathrm{i}}-6 \hat{\mathrm{j}}+2 \hat{\mathrm{k}})}{\left(\sqrt{3^2+(-6)^2+2^2}\right)^2} \\
& =\frac{-1}{49}(3 \hat{\mathrm{i}}-6 \hat{\mathrm{j}}+2 \hat{\mathrm{k}})
\end{aligned}$

</details>

---

### Q133. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\overline{\mathrm{a}}=2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}, \overline{\mathrm{b}}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-\hat{\mathrm{k}}$ and $\overline{\mathrm{c}}=\hat{\mathrm{i}}+3 \hat{\mathrm{j}}$ are such that $(\bar{a}+\lambda \bar{b})$ is perpendicular to $\bar{c}$, then the value of $\lambda$ is

**Options:**

- **(A)** $\frac{5}{11}$
- **(B)** $\frac{11}{5}$
- **(C)** $\frac{-11}{5}$
- **(D)** $\frac{-5}{11}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-11}{5}$**

**Detailed Solution:**

Let $\overline{\mathrm{d}}=\overline{\mathrm{a}}+\lambda \overline{\mathrm{b}}$
$\begin{aligned}
\overline{\mathrm{d}} & =(2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+2 \hat{\mathrm{k}})+\lambda(2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-\hat{\mathrm{k}}) \\
& =2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}+2 \lambda \hat{\mathrm{i}}+\lambda \hat{\mathrm{j}}-\lambda \hat{\mathrm{k}} \\
& =(2 \lambda+2) \hat{\mathrm{i}}+(3+\lambda) \hat{\mathrm{j}}+(2-\lambda) \hat{\mathrm{k}}
\end{aligned}$
Now, $\overline{\mathrm{d}}$ is perpendicular to $\overline{\mathrm{c}}$.
$\begin{aligned}
& \therefore \quad \overline{\mathrm{c}} \cdot \overline{\mathrm{d}}=0 \\
& \Rightarrow(\hat{\mathrm{i}}+3 \hat{\mathrm{j}}) \cdot[(2 \lambda+2) \hat{\mathrm{i}}+(3+\lambda) \hat{\mathrm{j}}+(2-\lambda) \hat{\mathrm{k}}]=0 \\
& \Rightarrow 1(2 \lambda+2)+3(3+\lambda)=0 \\
& \Rightarrow 2 \lambda+2+9+3 \lambda=0 \\
& \Rightarrow 5 \lambda+11=0 \\
& \Rightarrow \lambda=\frac{-11}{5}
\end{aligned}$

</details>

---

### Q134. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Scalar projection of the line segment joining the points $\mathrm{A}(-2,0,3), \mathrm{B}(1,4,2)$ on the line whose direction ratios are $6,-2,3$ is

**Options:**

- **(A)** $\frac{23}{7}$
- **(B)** 1
- **(C)** 7
- **(D)** $\frac{1}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

Let $\bar{a}$ be the vector joining $\mathrm{A}(-2,0,3)$ and $\mathrm{B}(1,4,2)$.
$\begin{aligned}
& \therefore \quad \overline{\mathrm{a}}=(1-(-2)) \hat{\mathrm{i}}+(4-0) \hat{\mathrm{j}}+(2-3) \hat{\mathrm{k}} \\
& =3 \hat{i}+4 \hat{j}-\hat{k} \\
& \text { and } \bar{b}=6 \hat{i}-2 \hat{j}+3 \hat{k} \\
& \therefore \quad \text { Projection }=\frac{\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}}{|\overline{\mathrm{b}}|}=\frac{3 \times 6+4 \times(-2)-1 \times 3}{\sqrt{6^2+(-2)^2+3^2}} \\
& =\frac{18-8-3}{\sqrt{49}} \\
& =\frac{7}{7} \\
& =1 \\
&
\end{aligned}$

</details>

---

### Q135. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Vectors $\bar{i}$ and $\bar{b}$ are such that $|\bar{a}|=1 ;|\bar{b}|=4$ and $\bar{a} \cdot \bar{b}-2$. If $\bar{c}-2 \bar{a} \times \bar{b}-3 \bar{b}$, then the angle between $\bar{b}$ and $\bar{c}$ is

**Options:**

- **(A)** $\frac{\pi}{6}$
- **(B)** $\frac{5 \pi}{6}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{2 \pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5 \pi}{6}$**

**Detailed Solution:**

$\begin{aligned}
& \text { Given: }|\overline{\mathrm{a}}|=1,|\overline{\mathrm{b}}|=4 \text { and } \overline{\mathrm{a}} \cdot \overline{\mathrm{b}}=2 \text {, } \\
& \overline{\mathrm{c}}=2 \overline{\mathrm{a}} \times \overline{\mathrm{b}}-3 \overline{\mathrm{b}}
\end{aligned}$
Now that, $|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|^2=|\overline{\mathrm{a}}|^2|\overline{\mathrm{b}}|^2-|\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}|^2$
$\therefore \quad|\bar{a} \times \bar{b}|^2=16-4=12$
Given that $\overline{\mathrm{c}}=2 \overline{\mathrm{a}} \times \overline{\mathrm{b}}-3 \overline{\mathrm{b}}$
$\begin{aligned}
& |\bar{c}|^2=(2 \bar{a} \times \bar{b}-3 \bar{b})^2 \\
& |\bar{c}|^2=4|\bar{a} \times \bar{b}|^2+9|\bar{b}|^2
\end{aligned}$
$\begin{aligned}
& |\vec{c}|^2=4(12)+9(16) \\
& |\vec{c}|^2=192 \\
& |\vec{c}|=8 \sqrt{3}
\end{aligned}$
Now, $\overline{\mathrm{b}} \cdot \overline{\mathrm{c}}=\mathrm{b} \cdot(2 \overline{\mathrm{a}} \times \overline{\mathrm{b}}-3 \overline{\mathrm{b}})$
$\therefore \quad \overline{\mathrm{b}} \cdot \overline{\mathrm{c}}=-3|\overline{\mathrm{b}}|^2=-48$
Angle between $b$ and $c$ is given by
$\cos \theta=\frac{(\bar{b} \cdot \bar{c})}{(|\mathrm{b} \| \mathrm{c}|)}=\frac{-48}{(4 \times 8 \sqrt{3})}$
$\cos \theta=\frac{-\sqrt{3}}{2}$
$\theta=\cos ^4\left(\frac{-\sqrt{3}}{2}\right)$
$\theta=\frac{5 \pi}{6}$

</details>

---

### Q136. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $|\bar{a}|=5,|\bar{b}|=13$ and $|\bar{a} \times \bar{b}|=25$. If $\frac{\pi}{2} < \theta < \pi$ where $\theta$ is angle between $\bar{a}, \bar{b}$ then $\bar{a} \cdot \bar{b}$ has the value

**Options:**

- **(A)** -60
- **(B)** -30
- **(C)** 60
- **(D)** 30

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -60**

**Detailed Solution:**

$\begin{aligned} & |\vec{a} \times \vec{b}|=|\vec{a} \times \vec{b}| \sin \theta \\ & \Rightarrow 25=5 \times 13 \sin \theta \\ & \Rightarrow \sin \theta=\frac{5}{13} \\ & \Rightarrow \cos \theta=\frac{-12}{13} \quad\left[\because \frac{\pi}{2} < \theta < \pi\right] \\ & \text { now } \vec{a} \cdot \vec{b}=|\vec{a}||\vec{b}| \cos \theta=5 \times 13 \times \frac{-12}{13}=-60\end{aligned}$

</details>

---

### Q137. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The vector projection of $\overline{P Q}$ on $\overline{A B}$, where $P \equiv(-2,1,3), Q \equiv(3,2,5), A \equiv(4,-3,5)$ and $B \equiv(7,-5,-1)$ is

**Options:**

- **(A)** $\frac{1}{49}(3 \hat{i}-2 \hat{j}-6 \hat{k})$
- **(B)** $\frac{1}{7}(3 \hat{i}-2 \hat{j}+6 \hat{k})$
- **(C)** $(3 \hat{i}-2 \hat{j}-6 \hat{k})$
- **(D)** $\frac{1}{7}(3 \hat{i}-2 \hat{j}-6 \hat{k})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{49}(3 \hat{i}-2 \hat{j}-6 \hat{k})$**

**Detailed Solution:**

$\begin{aligned}
& \overline{P Q}=(3+2) \hat{i}+(2-1) \hat{j}+(5-3) \hat{k}=5 \hat{i}+\hat{j}+2 \widehat{k} \\
& \overline{A B}=(7-4) \hat{i}+(-5+3) \hat{j}+(-1-5) \hat{k}=3 \hat{i}-2 \hat{j}-6 \hat{k}
\end{aligned}$
now vector projection of $\overrightarrow{P Q}$ on $\overrightarrow{A B}$ is $\frac{(\overrightarrow{P Q} \cdot \overrightarrow{A B}) \overrightarrow{A B}}{|\overrightarrow{A B}|^2}$
$=\frac{\{5 \times 3+1 \times(-1)+2 \times(-6)\}(3 \hat{i}-2 \hat{j}-6 \hat{k})}{3^2+(-2)^2+(-6)^2}=\frac{1}{49}(3 \hat{i}-2 \hat{j}-6 \hat{k})$

</details>

---

### Q138. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the vectors $2 \hat{i}-3 \hat{j}+6 \hat{k}$ and $\bar{b}$ are collinear and $|\bar{b}|=14$, then $\bar{b}$ has the value

**Options:**

- **(A)** $4 \hat{i}+6 \hat{j}+12 \hat{k}$
- **(B)** $-4 \hat{i}-6 \hat{j}-12 \hat{k}$
- **(C)** $4 \hat{i}-6 \hat{j}+12 \hat{k}$
- **(D)** $12 \hat{i}+5 \hat{j}+\sqrt{17} \widehat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 \hat{i}-6 \hat{j}+12 \hat{k}$**

**Detailed Solution:**

$\vec{b}=14\left(\frac{2 \hat{i}-3 \hat{j}+6 \hat{k}}{\sqrt{2^2+(-3)^2+6^2}}\right)=14\left(\frac{2 \hat{i}-3 \hat{j}+6 \hat{k}}{7}\right)=4 \hat{i}-6 \hat{j}+12 \hat{k}$

</details>

---

### Q139. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_0^1 \frac{8 \log (1+x)}{1+x^2} \mathrm{~d} x=$

**Options:**

- **(A)** $\frac{\pi}{2} \log 2$
- **(B)** $\pi \log 2$
- **(C)** $-\pi \log 2$
- **(D)** $\frac{-\pi}{2} \log 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pi \log 2$**

**Detailed Solution:**

$\begin{aligned} & \text { let } x=\tan \theta \\ & \Rightarrow \mathrm{d} x=\sec ^2 \theta \mathrm{d} \theta \text {, when } x=0, \theta=0 \text {; when } x=1 \text {, } \\ & \theta=\frac{\pi}{4}\end{aligned}$
$I=\int_0^{\frac{\pi}{4}} 8 \frac{\log (1+\tan \theta)}{1+\tan ^2 \theta} \cdot \sec ^2 \theta d \theta=\int_0^{\frac{\pi}{4}} 8 \log (1+\tan \theta) \mathrm{d} \theta \quad \ldots \ldots(\mathrm{i})$
$\Rightarrow \mathrm{I}=\int_0^{\frac{\pi}{4}} 8 \log \left(1+\tan \left(\frac{\pi}{4}-\theta\right) \mathrm{d} \theta\left[\because \int_0^a f(x) \mathrm{d} x=\int_0^a f(a-x) \mathrm{d} x\right]\right.$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/wjW5ze7nd7Ve1Aa0mMEMeb5JFkDj9tN5jPUhq5etkoY.original.fullsize.png">

$\left[\because \tan \left(\frac{\pi}{4}-\theta\right)=\frac{1-\tan \theta}{1+\tan \theta}\right]$
from (i) $+($ ii $)$
$\begin{aligned}
& 2 I=\int_0^{\pi / 4} 8 \log \left\{(1+\tan \theta) \times \frac{2}{(1+\tan \theta)}\right\} d \theta \\
& \Rightarrow 2 \mathrm{I}=8 \int_0^{\pi / 4} \log 2 \mathrm{~d} \theta=8 \log 2[\theta]_0^{\pi / 4}=8 \log 2 \times \frac{\pi}{4}
\end{aligned}$
$\Rightarrow \mathrm{I}=\pi \log 2$

</details>

---

### Q140. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A unit vector $\hat{a}$ makes angles $\frac{\pi}{3}$ with $\hat{i}, \frac{\pi}{4}$ with $\hat{j}$ and $\theta \in(\theta, \pi)$ with $\widehat{k}$, then a value of $\theta$ is

**Options:**

- **(A)** $\frac{2 \pi}{3}$
- **(B)** $\frac{5 \pi}{12}$
- **(C)** $\frac{5 \pi}{6}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2 \pi}{3}$**

**Detailed Solution:**

$\begin{aligned} & \alpha=\frac{\pi}{3}, \beta=\frac{\pi}{4} \text { and } \gamma=0 \\ & \because \cos ^2 \alpha+\cos ^2 \beta+\cos ^2 \gamma=1 \\ & \Rightarrow \cos ^2 \frac{\pi}{3}+\cos ^2 \frac{\pi}{4}+\cos ^2 \theta=1 \\ & \Rightarrow \frac{1}{4}+\frac{1}{2}+\cos ^2 \theta=1\end{aligned}$
$\Rightarrow \cos ^2 \theta=\frac{1}{4}$
$\Rightarrow \cos \theta= \pm \frac{1}{2}$
$\Rightarrow \theta=\frac{\pi}{3}$ or $\frac{2 \pi}{3}$ as $\theta \in(0, \pi)$

</details>

---

### Q141. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\bar{a}=3 \hat{i}+2 \hat{j}+x \hat{k}$ and $\bar{b}=\hat{i}-\hat{j}+\widehat{k}$, for some real $x$. Then $|\bar{a} \times \bar{b}|=r$ is possible, if

**Options:**

- **(A)** $0<r \leq \sqrt{\frac{3}{2}}$
- **(B)** $r \geq 5 \sqrt{\frac{3}{2}}$
- **(C)** $3 \sqrt{\frac{3}{2}}<r<5 \sqrt{\frac{3}{2}}$
- **(D)** $\sqrt{\frac{3}{2}} \leq r \leq 3 \sqrt{\frac{3}{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $r \geq 5 \sqrt{\frac{3}{2}}$**

**Detailed Solution:**

$\begin{aligned} & \vec{a} \times \vec{b}=\left|\begin{array}{ccc}\hat{i} & \hat{j} & \hat{k} \\ 3 & 2 & x \\ 1 & -1 & 1\end{array}\right|=(2+x) \hat{i}+(x-3) \hat{j}+(-3-2) \hat{k} \\ & \text { now } r=|\vec{a} \times \vec{b}|=\sqrt{(2+x)^2+(x-3)^2+(-5)^2} \\ & =\sqrt{2 x^2-2 x+38} \\ & =\sqrt{2\left(x-\frac{1}{2}\right)^2+\frac{75}{2}} \\ & \Rightarrow r_{\min }=\sqrt{\frac{75}{2}} \text { at } x=\frac{1}{2} \\ & \Rightarrow r \geq 5 \cdot \sqrt{\frac{3}{2}}\end{aligned}$

</details>

---

### Q142. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\quad \bar{a}=\hat{i}+\hat{j}+\hat{k}, \vec{b}=-\hat{i}+2 \hat{j}-2 \hat{k} \quad$ and $\quad \bar{c}=2 \hat{i}-\hat{j}+2 \hat{k} \quad$ then $(\bar{a}-\bar{b}) \cdot[(\bar{a} \times \bar{b}) \times(\bar{a} \times \bar{c})]$ is

**Options:**

- **(A)** $-18$
- **(B)** 18
- **(C)** 12
- **(D)** -18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -18**

**Detailed Solution:**

$\begin{aligned} & (\vec{a}-\vec{b}) \cdot[(\vec{a} \times \vec{b}) \times(\vec{a} \times \vec{c})] \\ & =(\vec{a}-\vec{b}) \cdot\{[\vec{a} \vec{b} \vec{c}] \vec{a}-[\vec{a} \vec{b} \vec{a}] \vec{c}\} \\ & =(\vec{a}-\vec{b}) \cdot \vec{a}\{[\vec{a} \vec{b} \vec{c}]\} \\ & =(\vec{a} \cdot \vec{a}-\vec{b} \cdot \vec{a})[\vec{a} \vec{b} \vec{c}]\end{aligned}$
$\begin{aligned} & =\left\{\left(1^2+1^2+1^2\right)-(-1+2-2)\right\}\left|\begin{array}{ccc}1 & 1 & 1 \\ -1 & 2 & -2 \\ 2 & -1 & 2\end{array}\right| \\ & =4 \times\left|\begin{array}{ccc}1 & 0 & 0 \\ -1 & 3 & -1 \\ 2 & -3 & 0\end{array}\right| \\ & =4 \times 1 \times(0-3)=-12\end{aligned}$

</details>

---

### Q143. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}=\hat{i}+\hat{j}, \bar{b}=2 \hat{i}-\hat{k}$, then point of intersection of the lines $\bar{r} \times \bar{a}=\bar{b} \times \bar{a}$ and $\bar{r} \times \bar{b}=\bar{a} \times \bar{b}$ is

**Options:**

- **(A)** $(-3,1,-1)$
- **(B)** $(-3,-1,1)$
- **(C)** $(3,1,-1)$
- **(D)** $(3,1,1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(3,1,-1)$**

**Detailed Solution:**

$\vec{r} \times \vec{a}=\vec{b} \times \vec{a}$ and $\vec{r} \times \vec{b}=\vec{a} \times \vec{b}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/KXoO-Fq-N5ce6WV2HUOecSL48KIgguCOpG1viud4i9s.original.fullsize.png">
$\begin{aligned} & \Rightarrow \vec{r} \times \vec{a}=-\vec{r} \times \vec{b} \quad \text { [from (i) and (ii)] } \\ & \Rightarrow \vec{r} \times(\vec{a}+\vec{b})=\overrightarrow{0} \\ & \Rightarrow \vec{r} \| \vec{a}+\vec{b} \\ & \Rightarrow \vec{r}=\lambda(\vec{a}+\vec{b})=\lambda(3 \hat{i}+\hat{j}-\hat{k})\end{aligned}$
Taking $\lambda=1, \vec{r}=3 \hat{i}+\hat{j}-\widehat{k} \equiv(3,1,-1)$

</details>

---

### Q144. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{a}, \vec{b}, \vec{c}$ are unit vectors such that $\vec{a}+\vec{b}+\vec{c}=\overrightarrow{0}$, then the value of $\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a}$ is

**Options:**

- **(A)** $0$
- **(B)** $\frac{-1}{2}$
- **(C)** $2$
- **(D)** $\frac{-3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{-3}{2}$**

**Detailed Solution:**

$\begin{aligned} & |\vec{a}+\vec{b}+\vec{c}|=|\vec{a}|^2+|\vec{b}|^2+|\vec{c}|^2+2(\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a}) \\ & \Rightarrow 0=1^2+1^2+1^2+2(\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a}) \\ & \Rightarrow \vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a}=-\frac{3}{2}\end{aligned}$

</details>

---

### Q145. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $O$ be the origin and let $P Q R$ be an arbitrary triangle. The point $S$ $\overline{O P} \cdot \overline{O Q}+\overline{O R} \cdot \overline{O S}=\overline{O R} \cdot \overline{O P}+\overline{O Q} \cdot \overline{O S}=\overline{O Q} \overline{O Q} \cdot \overline{O R}+\overline{O P} \cdot \overline{O S}$ that $\overline{O P} \cdot \overline{O Q}+\overline{O R} \cdot \overline{O S}=\overline{O R} \cdot \overline{O P}+\overline{O Q} \cdot \overline{O S}=\overline{O Q} \cdot \overline{O R}+\overline{O P} \cdot \overline{O S}$, then the triangle $P Q R$ has $S$ as its

**Options:**

- **(A)** Incentre.
- **(B)** Centroid.
- **(C)** Orthocentre.
- **(D)** Circumcentre.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Orthocentre.**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{O P} \cdot \overrightarrow{O Q}+\overrightarrow{O R} \cdot \overrightarrow{O S}=\overrightarrow{O R} \cdot \overrightarrow{O P}+\overrightarrow{O Q} \cdot \overrightarrow{O S} \\ & \Rightarrow \overrightarrow{O P} \cdot(\overrightarrow{O Q}-\overrightarrow{O R})=\overrightarrow{O S} \cdot(\overrightarrow{O Q}-\overrightarrow{O R}) \\ & \Rightarrow \overrightarrow{O P} \cdot \overrightarrow{R Q}=\overrightarrow{O S} \cdot \overrightarrow{R Q} \\ & \Rightarrow \overrightarrow{R Q} \cdot(\overrightarrow{O P}-\overrightarrow{O S})=0 \\ & \Rightarrow \overrightarrow{R Q} \cdot \overrightarrow{P S}=0 \\ & \Rightarrow \overrightarrow{P S} \perp \overrightarrow{Q R}\end{aligned}$
Similarly $\overrightarrow{Q S} \perp \overrightarrow{P R}$ and $\overrightarrow{R S} \perp \overrightarrow{P Q}$
i.e., $S$ is the orthocenter

</details>

---

### Q146. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the area of the parallelogram with $\vec{a}$ and $\vec{b}$ as two adjacent sides is 15 sq. units, then the area of the parallelogram having $3 \vec{a}+\vec{b}$ and $\vec{a}+3 \vec{b}$ as two adjacent sides, in square units, is

**Options:**

- **(A)** $135$
- **(B)** 90
- **(C)** 150
- **(D)** 120

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 120**

**Detailed Solution:**

Area of parallelogram $=|\vec{a} \times \vec{b}|=15$ [given]
Area of second parallelogram $=|(3 \vec{a}+\vec{b}) \times(\vec{a}+3 \vec{b})|$
$\begin{aligned} & =|3 \vec{a} \times \vec{a}+9 \vec{a} \times \vec{b}+\vec{b} \times \vec{a}+3 \vec{b} \times \vec{b}| \\ & =|0+9 \vec{a} \times \vec{b}-\vec{a} \times \vec{b}+0| \\ & =|8 \vec{a} \times \vec{b}|=8|\vec{a} \times \vec{b}|=8 \times 15=120\end{aligned}$

</details>

---

### Q147. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For non-zero vectors $\bar{a}, \bar{b}, \bar{c},|(\bar{a} \times \bar{b}) \cdot \bar{c}|=|\bar{a}||\bar{b}||\bar{c}|$ holds and only if

**Options:**

- **(A)** $\bar{b} \cdot \bar{c}=0, \bar{c} \cdot \bar{a}=0$
- **(B)** $\bar{c} \cdot \bar{a}=0, \bar{a} \cdot \bar{b}=0$
- **(C)** $\bar{a} \cdot \bar{b}=\bar{b} \cdot \bar{c}=\bar{c} \cdot \bar{a}=0$
- **(D)** $\bar{a} \times \bar{b}=0, \bar{b} \times \bar{c}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\bar{a} \cdot \bar{b}=\bar{b} \cdot \bar{c}=\bar{c} \cdot \bar{a}=0$**

**Detailed Solution:**

$\begin{aligned} & |(\vec{a} \times \vec{b}) \cdot \vec{c}| \\ & =|\vec{a}||\vec{b}||\vec{c}| \\ & \Rightarrow|\vec{a} \times \vec{b}||\vec{c}| \cos \theta=|\vec{a}||\vec{b}||\vec{c}| \\ & \Rightarrow|\vec{a}||\vec{b}| \sin \phi|\vec{c}| \cos \theta=|\vec{a}||\vec{b}||\vec{c}| \\ & \Rightarrow \sin \phi=1 \text { and } \cos \theta=1 \\ & \phi=90^{\circ} \text { and } \theta=0^{\circ} \\ & \text { where } \phi \text { is the angle between } \vec{a} \text { and } \vec{b} \text { and } \theta \text { is the angle between } \vec{c} \text { and } \\ & \text { normal to the plane containing } \vec{a} \text { and } \vec{b} \\ & \Rightarrow \vec{a} \perp \vec{b}, \vec{b} \perp \vec{c} \text {, and } \vec{c} \perp \vec{a} \\ & \Rightarrow \vec{a} \cdot \vec{b}=\vec{b} \cdot \vec{c}=\vec{c} \cdot \vec{a}=0\end{aligned}$

</details>

---

### Q148. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}$ and $\bar{b}$ are vectors such that $|\bar{a}+\bar{b}|=\sqrt{29}$ and $\bar{a} \times(2 \hat{i}+3 \hat{j}+4 \hat{k})=(2 \hat{i}+3 \hat{j}+4 \hat{k}) \times \bar{b}$, then a possible value of $(\bar{a}+\bar{b}) \cdot(-7 \hat{i}+2 \hat{j}+3 \hat{k})$ is

**Options:**

- **(A)** 4
- **(B)** 0
- **(C)** 1
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 4**

**Detailed Solution:**

$\begin{aligned} & \vec{a} \times(2 \hat{i}+3 \hat{j}+4 \widehat{k})=(2 \hat{i}+3 \hat{j}+4 \widehat{k}) \times \vec{b}=-\vec{b} \times(2 \hat{i}+3 \hat{j}+4 \widehat{k}) \\ & \Rightarrow(\vec{a}+\vec{b}) \times(2 \hat{i}+3 \hat{j}+4 \widehat{k})=\overrightarrow{0} \\ & \Rightarrow(\vec{a}+\vec{b}) \| 2 \widehat{i}+3 \hat{j}+4 \widehat{k} \\ & \Rightarrow \vec{a}+\vec{b}=\lambda(2 \hat{i}+3 \hat{j}+4 \widehat{k}) \\ & \Rightarrow|\vec{a}+\vec{b}|=\lambda \sqrt{2^2+3^2+4^2} \\ & \Rightarrow \sqrt{29}= \pm \lambda \sqrt{29} \\ & \Rightarrow \lambda= \pm 1 \\ & \Rightarrow \vec{a}+\vec{b}= \pm(2 \hat{i}+3 \hat{j}+4 \widehat{k}) \\ & \Rightarrow(\vec{a}+\vec{b}) \cdot(-7 \hat{i}+2 \hat{j}+3 \hat{k})= \pm(2 \hat{i}+3 \hat{j}+4 \widehat{k}) \cdot(-7 \hat{i}+2 \hat{j}+3 \hat{k}) \\ & = \pm(-14+6+12) \\ & = \pm 4\end{aligned}$

</details>

---

### Q149. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the vector $\bar{a}=2 \hat{i}+2 \hat{j}+3 \hat{k}, \bar{b}=-\hat{i}+2 \hat{j}+\hat{k}$ and $\bar{c}=3 \hat{i}+\hat{j}$ are such that $(\bar{a}+\lambda \bar{b})$ is perpendicular to $\bar{c}$, then the value of $\lambda$ is

**Options:**

- **(A)** -8
- **(B)** 10
- **(C)** 8
- **(D)** $\frac{8}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 8**

**Detailed Solution:**

$\begin{aligned} & \because \vec{a}+\lambda \vec{b} \perp \vec{c} \\ & \Rightarrow(\vec{a}+\lambda \vec{b}) \cdot \vec{c}=0 \\ & \Rightarrow\{(2 \widehat{i}+2 \widehat{j}+3 \widehat{k})+\lambda(-\hat{i}+2 \hat{j}+\hat{k})\} \cdot(3 \hat{i}+\hat{j})=0 \\ & \Rightarrow\{(2-\lambda) \hat{i}+(2+2 \lambda) \hat{j}+(3+\lambda) \widehat{k}\} \cdot(3 \hat{i}+\hat{j})=0 \\ & \Rightarrow(2-\lambda) \times 3+(2+2 \lambda) \times 1+(3+\lambda) \times 0=0 \\ & \Rightarrow \lambda=8\end{aligned}$

</details>

---

### Q150. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}+2 \bar{b}+3 \bar{c}=\overline{0}$ and $(\bar{b} \times \bar{b})+(\bar{b} \times \bar{c})+(\bar{c} \times \bar{a})=\lambda(\bar{b} \times \bar{c})$, then $\lambda$ has the value

**Options:**

- **(A)** 4
- **(B)** 5
- **(C)** 3
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 6**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/4Mo4xnT4uqKSDSbq1J_8rFuIGsiKNIdJqY-Ou9MLsuo.original.fullsize.png">

$\begin{aligned}
& \Rightarrow(\vec{a}+\vec{b}+\vec{c}) \times(\vec{a}+2 \vec{b}+3 \vec{c})=\overrightarrow{0} \\
& \Rightarrow 2 \vec{a} \times \vec{b}+3 \vec{a} \times \vec{c}+\vec{b} \times \vec{a}+3 \vec{b} \times \vec{c}+\vec{c} \times \vec{a}+2 \vec{c} \times \vec{b}=\overrightarrow{0} \\
& \Rightarrow \vec{a} \times \vec{b}+\vec{b} \times \vec{c}-2 \vec{c} \times \vec{a}=\overrightarrow{0} \\
& \Rightarrow \vec{a} \times \vec{b}+\vec{b} \times \vec{c}+\vec{c} \times \vec{a}=3 \vec{c} \times \vec{a}=3 \vec{c} \times(-2 \vec{b}-3 \vec{c}) \quad[\text { from (1)] } \\
& \Rightarrow \vec{a} \times \vec{b}+\vec{b} \times \vec{c}+\vec{c} \times \vec{a}=-6 \vec{c} \times \vec{b} \\
& \Rightarrow \vec{a} \times \vec{b}+\vec{b} \times \vec{c}+\vec{c} \times \vec{a}=6 \vec{b} \times \vec{c} \\
& \Rightarrow \lambda=6
\end{aligned}$

</details>

---

### Q151. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the area of the triangle with vertices $\hat{i}+y \hat{j}, \hat{i}+2 \hat{k}$ and $3 \hat{j}+\hat{k}$ is $\sqrt{6}$ sq. units, then the values of $y$ are

**Options:**

- **(A)** 2,4
- **(B)** 3,4
- **(C)** -2,4
- **(D)** 2,-4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2,4**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{A B}=(\hat{i}+2 \hat{k})-(\hat{i}+y \hat{j})=0 \hat{i}-y \hat{j}+2 \widehat{k} \\ & \overrightarrow{B C}=(3 \hat{j}+\hat{k})-(\hat{i}+2 \hat{k})=-\hat{i}+3 \hat{j}-\hat{k} \\ & \text { Now area of triangle }=\frac{1}{2}|\overrightarrow{A B} \times \overrightarrow{B C}|=\sqrt{6} \\ & \Rightarrow \frac{1}{2}\left|\begin{array}{ccc}\hat{i} & \hat{j} & \widehat{k} \\ 0 & -y & 2 \\ -1 & 3 & -1\end{array}\right|=\sqrt{6} \\ & \Rightarrow|(y-6) \hat{i}-2 \hat{j}-y \hat{k}|=2 \sqrt{6} \\ & \Rightarrow(y-6)^2+(-2)^2+(-y)^2=(2 \sqrt{6})^2 \\ & \Rightarrow y^2-12 y+36+4+y^2=24 \\ & \Rightarrow y^2-6 y+8=0 \\ & \Rightarrow y=2,4\end{aligned}$

</details>

---

### Q152. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{u}, \bar{v}$ are two vectors represented in the following figure, then the value of $|\bar{u} \times \bar{v}|=$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/F2do0bT_s2K87od6CmtEdWh84ahvc9tLTUQhhy0UEDc.original.fullsize.png">

**Options:**

- **(A)** $20$
- **(B)** $10 \sqrt{3}$
- **(C)** $10$
- **(D)** $5 \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $10$**

**Detailed Solution:**

$\vec{u} \times \vec{v}|=| \vec{u}|| \vec{v} \mid \sin \theta=4 \times 5 \times \sin 150^{\circ}=20 \times \frac{1}{2}=10$

</details>

---

### Q153. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $|\bar{a}|=\sqrt{26},|\bar{b}|=7$ and $|\bar{a} \times \bar{b}|=35$, then $\bar{a} \cdot \bar{b}=$

**Options:**

- **(A)** $\pm 5 \sqrt{26}$
- **(B)** $\pm \sqrt{26}$
- **(C)** $\pm 7$
- **(D)** $\pm 7 \sqrt{26}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\pm 7$**

**Detailed Solution:**

$\begin{aligned} & |\vec{a}|=\sqrt{26},|\vec{b}|=7,|\vec{a} \times \vec{b}|=|\vec{a}||\vec{b}| \sin \theta=35 \\ & \Rightarrow \sqrt{26} \times 7 \sin \theta=35 \\ & \Rightarrow \sin \theta=\frac{5}{\sqrt{26}} \\ & \Rightarrow \cos \theta= \pm \frac{1}{\sqrt{26}}\end{aligned}$
Now $\vec{a} \cdot \vec{b}=|\vec{a}||\vec{b}| \cos \theta=\sqrt{26} \times 7 \times \frac{ \pm 1}{\sqrt{26}}= \pm 7$

</details>

---

### Q154. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $|\bar{a}|=3,|\bar{b}|=5$ and $|\bar{c}|=7$ and $\bar{a}+\bar{b}+\bar{c}=\overline{0}$, then the angle between $\bar{a}$ and $\bar{b}$ is

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{3}$**

**Detailed Solution:**

$\begin{aligned} & \vec{a}+\vec{b}+\vec{c}=0 \\ & \Rightarrow \vec{a}+\vec{b}=-\vec{c} \\ & \Rightarrow|\vec{a}+\vec{b}|^2=|\vec{c}|^2 \\ & \Rightarrow|\vec{a}|^2+|\vec{b}|^2+2|\vec{a}||\vec{b}| \cos \theta=|\vec{c}|^2 \\ & \Rightarrow 3^2+5^2+2 \times 3 \times 5 \cos \theta=7^2 \\ & \Rightarrow \cos \theta=\frac{15}{30}=\frac{1}{2}=\cos \frac{\pi}{3} \\ & \Rightarrow \theta=\frac{\pi}{3}\end{aligned}$

</details>

---

### Q155. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Given three vectors $\bar{a}, \bar{b}, \bar{c}$, two of which are collinear. If $\bar{a}+\bar{b}$ is collinear with $\bar{c}$ and $\bar{b}+\bar{c}$ is collinear with $|\bar{a}|=|\bar{b}|=|\bar{c}|=\sqrt{2}$, then $\bar{a} \cdot \bar{b}+\bar{b} \cdot \bar{c}+\bar{c} \cdot \bar{a}=$

**Options:**

- **(A)** $5$
- **(B)** $-3$
- **(C)** $3$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-3$**

**Detailed Solution:**

$\begin{aligned} & \vec{a}+\vec{b}=\lambda \vec{c} \quad \ldots(i) \text { and } \vec{b}+\vec{c}=\mu \vec{a} \quad \ldots(i i) \\ & \Rightarrow \vec{a}-\vec{c}=\lambda \vec{c}-\mu \vec{a} \quad \text { form (i) and (ii) } \\ & \Rightarrow(1+\mu) \vec{a}=(1+\lambda) \vec{c} \\ & \Rightarrow \mu=\lambda=-1 \\ & \Rightarrow \vec{a}+\vec{b}+\vec{c}=0 \\ & \Rightarrow|\vec{a}+\vec{b}+\vec{c}|^2=|\vec{a}|^2+|\vec{b}|^2+|\vec{c}|^2+2(\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a}) \\ & \Rightarrow 0=2+2+2+2(\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a}) \\ & \Rightarrow \vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a}=-3\end{aligned}$

</details>

---

### Q156. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}$ and $\bar{b}$ are two vectors such that $|\vec{a}|=|\vec{b}|=\sqrt{2}$ with $\vec{a} \cdot \vec{b}=-1$, then the angle between $\bar{a}$ and $\bar{b}$ is

**Options:**

- **(A)** $\frac{3 \pi}{4}$
- **(B)** $\frac{5 \pi}{6}$
- **(C)** $\frac{5 \pi}{9}$
- **(D)** $\frac{2 \pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2 \pi}{3}$**

**Detailed Solution:**

$\theta=\cos ^{-1}\left(\frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}\right)=\cos ^{-1}\left(\frac{-1}{\sqrt{2} \sqrt{2}}\right)=\cos ^{-1}\left(\frac{-1}{2}\right)=\frac{2 \pi}{3}$

</details>

---

### Q157. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=\hat{i}-2 \hat{j}+\hat{k}$ and $\vec{b}=\hat{i}-\hat{j}+\hat{k}$ be two vectors. If $\vec{c}$ is a vector such that $\vec{b} \times \vec{c}=\vec{b} \times \vec{a}$ and $\vec{c} \cdot \vec{a}$ then $\vec{c} \cdot \vec{b}$ is equal to

**Options:**

- **(A)** $-\frac{1}{2}$
- **(B)** $-\frac{3}{2}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\frac{1}{2}$**

**Detailed Solution:**

$\begin{aligned} & \vec{b} \times \vec{c}=\vec{b} \times \vec{a} \\ & \Rightarrow \vec{b} \times \vec{c}-\vec{b} \times \vec{a}=\overrightarrow{0} \\ & \Rightarrow \vec{b} \times(\vec{c}-\vec{a})=\overrightarrow{0} \\ & \Rightarrow \vec{c}-\vec{a} \| \vec{b} \\ & \Rightarrow \vec{c}-\vec{a}=\lambda \vec{b} \\ & \Rightarrow \vec{c}=\vec{a}+\lambda \vec{b} \\ & \because \vec{c} \cdot \vec{a}=0 \Rightarrow(\vec{a}+\lambda \vec{b}) \cdot \vec{a}=0 \Rightarrow \vec{a} \cdot \vec{b}+\lambda \vec{b} \cdot \vec{a}=0 \\ & \Rightarrow 11^2+(-2)^2+1^2+\lambda(1 \times 1+(-2) \times(-1)+1 \times 1) \\ & \Rightarrow \lambda=-\frac{3}{2}\end{aligned}$
$\begin{aligned} & \text { Now } \vec{c} \cdot \vec{b}=(\vec{a}+\lambda \vec{b}) \cdot \vec{b} \\ & =\vec{a} \cdot \vec{b}+\lambda \vec{b} \cdot \vec{b} \\ & =4-\frac{3}{2} \times 3=4-\frac{9}{2}=-\frac{1}{2}\end{aligned}$

</details>

---

### Q158. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\vec{a}=\hat{i}+\hat{j}+\hat{k}$, and $\vec{b}=\hat{i}-\hat{j}+\widehat{k}$ and $\vec{c}=\hat{i}-\hat{j}-\hat{k}$ are three vectors then vector $\overline{\mathrm{r}}$ in the plane of $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$, whose projection on $\overline{\mathrm{c}}$ is $\frac{1}{\sqrt{3}}$, is given by

**Options:**

- **(A)** $(2 \hat{\mathrm{i}}-1) \hat{\mathrm{i}}-\hat{\mathrm{j}}+(2 \mathrm{t}+1) \widehat{\mathrm{k}}, \forall \mathrm{t} \in \mathrm{R}$
- **(B)** $(2 \mathrm{t}+1) \hat{\mathrm{i}}-\hat{\mathrm{j}}+(2 \mathrm{t}+1) \widehat{\mathrm{k}}, \forall \mathrm{t} \in \mathrm{R}$
- **(C)** $(2 t-1) \hat{i}-\hat{j}+(2 t-1) \widehat{k}, \forall t \in R$
- **(D)** $(2 t+1) \hat{i}-\hat{j}+(2 t-1) \widehat{k}, \forall t \in R$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(2 \mathrm{t}+1) \hat{\mathrm{i}}-\hat{\mathrm{j}}+(2 \mathrm{t}+1) \widehat{\mathrm{k}}, \forall \mathrm{t} \in \mathrm{R}$**

**Detailed Solution:**

$\vec{r}=t \vec{a}+u \vec{b}$ [as vector lies in the plane of $\vec{a}$ and $\vec{b}$ where $t$ and $u$ are scalars]
$\begin{aligned} & \Rightarrow \vec{r}=t(\hat{i}+\hat{j}+\hat{k})+u(\hat{i}-\hat{j}+\hat{k}) \\ & =(t+u) \hat{i}+(t-u) \hat{j}+(t+u) \hat{k} \ldots(i) \\ & \frac{\vec{r} \cdot \vec{c}}{|\vec{c}|}=\frac{1}{\sqrt{3}} \Rightarrow \frac{(t+u)-(t-u)-(t+u)}{\sqrt{3}}=\frac{1}{\sqrt{3}} \\ & \Rightarrow-(t-u)=1 \Rightarrow u=t+1 \ldots \ldots . .(i i)\end{aligned}$
from (i) and (ii)
$\vec{r}=(2 t+1) \hat{i}-\hat{j}+(2 t+1) \widehat{k}$

</details>

---

### Q159. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\bar{a}, \bar{b}, \bar{c}$ are the three unit vectors such that $|\bar{a}+\bar{b}+\bar{c}|=1$ and $\bar{b}$ is perpendicular to $\bar{c}$. If $\bar{a}$ makes angles $\alpha, \beta$ with $\bar{b}$ and $\bar{c}$ respectively, then $\cos \alpha+\cos \beta$ has the value

**Options:**

- **(A)** $-1$
- **(B)** $-2$
- **(C)** 4
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-1$**

**Detailed Solution:**

$\begin{aligned} & |\overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}}|^2=|\overrightarrow{\mathrm{a}}|^2+|\overrightarrow{\mathrm{b}}|^2+|\overrightarrow{\mathrm{c}}|^2+2 \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{b}}+2 \overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{c}}+2 \overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{a}} \\ & \Rightarrow 1^2=1^2+1^2+1^2+2 \\ & |\overrightarrow{\mathrm{a}}||\overrightarrow{\mathrm{b}}| \cos \alpha+2|\overrightarrow{\mathrm{b}}||\overrightarrow{\mathrm{c}}| \cos 90^{\circ}+2|\overrightarrow{\mathrm{c}}||\overrightarrow{\mathrm{a}}| \cos \beta \\ & \Rightarrow 1+3+2 \cos \alpha+2 \times 0+2 \cos \beta \\ & \Rightarrow \cos \alpha+\cos \beta=-1\end{aligned}$

</details>

---

### Q160. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}=\hat{i}+\hat{j}+\widehat{k}, \bar{b}=\hat{i}-\hat{j}+\widehat{k}$ and $\bar{c}=\hat{i}-\hat{j}-\widehat{k}$ be three vectors. A vector $\overline{\mathrm{V}}$ in the plane of $\overline{\mathrm{a}}$ and $\overline{\mathrm{b}}$, whose projection on $\overline{\mathrm{c}}$ is $\frac{1}{\sqrt{3}}$ is given by

**Options:**

- **(A)** $\hat{i}+3 \hat{j}-3 \widehat{k}$
- **(B)** $3 \hat{i}-\hat{j}+3 \hat{k}$
- **(C)** $\hat{i}-3 \hat{j}+3 \hat{k}$
- **(D)** $-3 \hat{i}-3 \widehat{j}-\widehat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 \hat{i}-\hat{j}+3 \hat{k}$**

**Detailed Solution:**

Any vector in the plane of $\vec{a}$ and $\vec{b}$ can be written as
$$
\vec{v}=\vec{a}+\lambda \vec{b}=(\hat{i}+\hat{j}+\widehat{k})+\lambda(\hat{i}-\hat{j}+\widehat{k})
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/_pS_8KDs5oFr_fotUTo1lo9RsKQxus90XJAf4kXIiJM.original.fullsize.png">
$\frac{\mathrm{A}}{\mathrm{Q}}$ Its projection on $\overrightarrow{\mathrm{c}}$ is $\frac{1}{\sqrt{3}}$
$$
\begin{aligned}
& \Rightarrow \frac{(\vec{a}+\lambda \vec{b}) \cdot \vec{c}}{|\vec{c}|}=\frac{1}{\sqrt{3}} \\
& \Rightarrow \frac{(1+\lambda)-(1-\lambda)-(1+\lambda)}{\sqrt{1^2+(-1)^2+(-1)^2}}=\frac{1}{\sqrt{3}} \\
& \Rightarrow \lambda=2
\end{aligned}
$$
Putting $\lambda=2$ in eq. (1) we get
$$
\vec{v}=3 \hat{i}-2 \hat{j}+3 \widehat{k}
$$

</details>

---

### Q161. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}$ and $\bar{b}$ are vectors such that $|\bar{a}|=3,|\bar{b}|=2$ and $\bar{a} \cdot \bar{b}=5$, then $=$ $|\bar{a}-\bar{b}|=$

**Options:**

- **(A)** $\sqrt{23}$
- **(B)** $\sqrt{3}$
- **(C)** 5
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{3}$**

**Detailed Solution:**

$|\overrightarrow{\mathrm{a}}-\overrightarrow{\mathrm{b}}|=\sqrt{|\overrightarrow{\mathrm{a}}|^2+|\overrightarrow{\mathrm{b}}|^2-2 \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{b}}}=\sqrt{3^2+2^2-2 \times 5}=\sqrt{3}$

</details>

---

### Q162. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If angle between the vectors $\bar{a}=2 \lambda 2 \hat{i}+4 \lambda \hat{j}+\widehat{k}$ and $\bar{b}=7 \hat{i}-2 \hat{j}+\lambda \widehat{k} i$ obtuse, then the values of $\lambda$ lie in

**Options:**

- **(A)** $\left(\frac{1}{2}, \infty\right)$
- **(B)** $\left[0, \frac{1}{2}\right]$
- **(C)** $\left(0, \frac{1}{2}\right)$
- **(D)** $(-\infty, 0)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(0, \frac{1}{2}\right)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/j1CkMDCTxPa3IFITROsxEpW-JnBlb7DpUm7cuz7RSsg.original.fullsize.png">
Angle between $\vec{a}$ and $\vec{b}$ is obtuse
$\begin{aligned} & \Rightarrow(2 \lambda 2 \hat{i}+4 \lambda \hat{j}+\widehat{k}) \cdot(7 \hat{i}-2 \hat{j}+\lambda \widehat{k})<0 \\ & \Rightarrow 14 \lambda^2-8 \lambda+\lambda<0 \\ & \Rightarrow 7 \lambda(2 \lambda-1)<0 \\ & \Rightarrow \lambda \in\left(0, \frac{1}{2}\right)\end{aligned}$

</details>

---

### Q163. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For any two non-zero vectors $\bar{a}$ and $\bar{b},(a \bar{b}+b \bar{a}) \cdot(a \bar{b}-b \bar{a})$ is

**Options:**

- **(A)** $2|\overline{\mathrm{b}}| 2$
- **(B)** $0$
- **(C)** $|\overline{\mathrm{a}}|^2$
- **(D)** $|\overline{\mathrm{a}}|^2+|\overline{\mathrm{b}}|^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0$**

**Detailed Solution:**

$\begin{aligned} & (a \vec{b}+b \vec{a}) \cdot(a \vec{b}-b \vec{a}) \\ & =a^2(\vec{b} \cdot \vec{b})-b^2(\vec{a} \cdot \vec{a}) \\ & =a^2 b^2-b^2 a^2 \\ & =0\end{aligned}$

</details>

---

### Q164. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $|\bar{a}|=\sqrt{26},|\bar{b}|=7$ and $|\bar{a} \times \bar{b}|=35$, then $\bar{a} \cdot \bar{b}$ is-

**Options:**

- **(A)** $7 \sqrt{26}$
- **(B)** $7$
- **(C)** $\frac{\sqrt{26}}{7}$
- **(D)** $\frac{7}{\sqrt{26}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $7$**

**Detailed Solution:**

$\begin{aligned} & \because|\vec{a} \times \vec{b}|=|\vec{a}||\vec{b}| \sin \theta \\ & \Rightarrow 35=\sqrt{26} \times 7 \times \sin \theta \\ & \Rightarrow \sin \theta=\frac{5}{\sqrt{26}} \\ & \Rightarrow \cos \theta=\frac{1}{\sqrt{26}}\end{aligned}$
Now, $\vec{a} \cdot \vec{b}=|\vec{a}||\vec{b}| \cos \theta$
$\begin{aligned} & =\sqrt{26} \times 7 \times \frac{1}{\sqrt{26}} \\ & =7\end{aligned}$

</details>

---

### Q165. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\vec{a}=2 \hat{i}+\hat{j}-2 \hat{k}, \vec{b}=\hat{i}+\hat{j}$ and $\vec{c}$ be a vector such that $|\vec{c}-\vec{a}|=3$. If $\overrightarrow{\mathrm{p}}=\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}$, then the angle between $\overrightarrow{\mathrm{p}}$ and $\overrightarrow{\mathrm{c}}$ is $\frac{\pi}{6}$ and $|\overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{c}}|=3$. Thus $\vec{a} . \vec{c}$ is equal to-

**Options:**

- **(A)** $\frac{1}{8}$
- **(B)** $1$
- **(C)** $2$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

Given $\vec{a}=2 \hat{i}+\hat{j}-2 \widehat{k}, \vec{b}=\hat{i}+\hat{j},|\vec{c}-\vec{a}|=3$
$\vec{p}=\vec{a} \times \vec{b},|\vec{p} \times \vec{c}|=3$ and angle between $\vec{p}$ and $\vec{c}$ is $\frac{\pi}{6}$
Here, $\vec{p}=\vec{a} \times \vec{b}=\left|\begin{array}{ccc}\hat{i} & \hat{j} & \widehat{k} \\ 2 & 1 & -2 \\ 1 & 1 & 0\end{array}\right|=2 \hat{i}-2 \hat{j}+\widehat{k} \Rightarrow|\vec{p}|=3$
also $|\vec{a}|=3$ and $|\vec{b}|=\sqrt{2}$
$\begin{aligned} & \text { Now } \because|\vec{p} \times \vec{c}|=3 \Rightarrow|\vec{p}||\vec{c}| \sin \frac{\pi}{6}=3 \\ & \Rightarrow 3|\vec{c}| \times \frac{1}{2}=3 \\ & \Rightarrow|\vec{c}|=2 \\ & \text { and }|\vec{c}-\vec{a}|=3 \Rightarrow|\vec{c}-\vec{a}|^2=9 \\ & \Rightarrow|\vec{c}|^2+|\vec{a}|^2-2 \vec{c} \cdot \vec{a}=9 \\ & \Rightarrow 4+9-2 \vec{a} \cdot \vec{c}=9\end{aligned}$
$\Rightarrow \vec{a} \cdot \vec{c}=2$

</details>

---

### Q166. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the angle between the vectors $\bar{a}=2 \lambda^2 \hat{i}+4 \lambda \hat{j}+\hat{k}$ and $\overline{\mathrm{b}}=7 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\lambda \hat{\mathrm{k}}$ is obtuse, then $\lambda \in$

**Options:**

- **(A)** $\left(0, \frac{1}{2}\right]$
- **(B)** $\left(0, \frac{1}{2}\right)$
- **(C)** $\left[0, \frac{1}{2}\right]$
- **(D)** $\left[0, \frac{1}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(0, \frac{1}{2}\right)$**

**Detailed Solution:**

We have $\bar{a}=2 \lambda^2 \hat{i}+4 \lambda \hat{j}+\hat{k}$ and $\bar{b}=7 \hat{i}-2 \hat{j}+\lambda \hat{k}$ $\bar{a} \cdot \bar{b}=|\bar{a}| \cdot|\bar{b}| \cdot \cos \theta$, where $\theta$ is angle between $\bar{a}$ and $\bar{b}$.
$\therefore \quad \cos \theta=\frac{\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}}{|\overline{\mathrm{a}}| \cdot|\overline{\mathrm{b}}|} < 0$, as $\theta$ is an obtuse angle.
$\therefore \quad|\overline{\mathrm{a}}| \cdot|\overline{\mathrm{b}}| < 0$
$\therefore \quad\left(2 \lambda^2\right)(7)+(4 \lambda)(-2)+(1)(\lambda) < 0$
$\therefore \quad 14 \lambda^2-7 \lambda < 0 \Rightarrow 7 \lambda(2 \lambda-1) < 0 \Rightarrow \lambda(2 \lambda-1) < 0$
$\therefore \quad 0 < \lambda < \frac{1}{2}$ i.e. $\lambda \in\left(0, \frac{1}{2}\right)$

</details>

---

### Q167. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}=2 \hat{i}+3 \hat{j}-\hat{k}, \bar{b}=-\hat{i}+2 \hat{j}-4 \hat{k}$ and $\bar{c}=\hat{i}+\hat{j}-2 \hat{k}$, then $(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \cdot(\overline{\mathrm{a}} \times \overline{\mathrm{c}})=$

**Options:**

- **(A)** -30
- **(B)** 84
- **(C)** 70
- **(D)** 984

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 70**

**Detailed Solution:**

$\begin{aligned} & \overline{\mathrm{a}} \times \overline{\mathrm{b}}=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 2 & 3 & -1 \\ -1 & 2 & -4\end{array}\right|=\hat{\mathrm{i}}(-10)-\hat{\mathrm{j}}(-9)+\hat{\mathrm{k}}(7)=-10 \hat{\mathrm{i}}+9 \hat{\mathrm{j}}+7 \hat{\mathrm{k}} \\ & \overline{\mathrm{a}} \times \overline{\mathrm{c}}=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 2 & 3 & -1 \\ 1 & 1 & -2\end{array}\right|=\hat{\mathrm{i}}(-5)-\hat{\mathrm{j}}(-3)+\hat{\mathrm{k}}(-1)=-5 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}-\hat{\mathrm{k}} \\ & (\overline{\mathrm{a}} \times \overline{\mathrm{b}})(\overline{\mathrm{a}} \times \overline{\mathrm{c}})=(-10 \hat{\mathrm{i}}+9 \hat{\mathrm{j}}+7 \hat{\mathrm{k}}) \cdot(-5 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}-\hat{\mathrm{k}})=50+27-7=70\end{aligned}$

</details>

---

### Q168. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The projection of $\bar{a}=\hat{i}-2 \hat{j}+\hat{k}$ on $\bar{b}=2 \hat{i}-\hat{j}+\hat{k}$ is

**Options:**

- **(A)** 5
- **(B)** $5 \sqrt{6}$
- **(C)** $\frac{5}{\sqrt{6}}$
- **(D)** $\sqrt{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{5}{\sqrt{6}}$**

**Detailed Solution:**

Projection $\bar{a}$ on $\bar{b}$
$$
=\frac{\bar{a} \cdot \bar{b}}{|\bar{b}|}=\frac{(\hat{i}-2 \hat{j}+\hat{k}) \cdot(2 \hat{i}-\hat{j}+\hat{k})}{\sqrt{(2)^2+(-1)^2+(1)^2}}=\frac{2+2+1}{\sqrt{6}}=\frac{5}{\sqrt{6}}
$$

</details>

---

### Q169. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}=2 \hat{i}+\hat{j}-2 \hat{k}$ and $\bar{b}=\hat{i}+\hat{j}$. If $\bar{c}$ is a vector such that $\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=|\overline{\mathrm{c}}|,|\overline{\mathrm{c}}-\overline{\mathrm{a}}|=2 \sqrt{2}$ and the angle between $\overline{\mathrm{a}} \times \overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ is $60^{\circ}$. Then $|(\bar{a} \times \bar{b}) \times \bar{c}|=$

**Options:**

- **(A)** $\frac{3 \sqrt{3}}{2}$
- **(B)** $\frac{3}{2}$
- **(C)** $3 \sqrt{3}$
- **(D)** $\frac{\sqrt{3}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3 \sqrt{3}}{2}$**

**Detailed Solution:**

$\begin{aligned} & \overline{\mathrm{a}} \times \overline{\mathrm{b}}=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 2 & 1 & -2 \\ 1 & 1 & 0\end{array}\right|=2 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}} \\ & \therefore|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|=\sqrt{4+4+1}=3 \text {. Also }|\overline{\mathrm{a}}|=\sqrt{4+1+4}=3 \\ & \overline{\mathrm{c}}-\overline{\mathrm{a}}=2 \sqrt{2} \Rightarrow(\overline{\mathrm{c}}-\overline{\mathrm{a}})^2=8 \\ & \therefore \quad \overline{\mathrm{c}}-\overline{\mathrm{a}}=2 \sqrt{2} \Rightarrow(\overline{\mathrm{c}}-\overline{\mathrm{a}})^2=8 \\ & \therefore \quad|\overline{\mathrm{c}}|^2+|\overline{\mathrm{a}}|^2=2 \overline{\mathrm{c}} \cdot \overline{\mathrm{a}}=8 \\ & \therefore \quad|\overline{\mathrm{c}}|^2+9-2|\overline{\mathrm{c}}|=8 \\ & \therefore \quad|\overline{\mathrm{c}}|^2-2|\overline{\mathrm{c}}|+1=0 \Rightarrow(|\overline{\mathrm{c}}|-1)^2=0 \Rightarrow|\overline{\mathrm{c}}|=1 \\ & |(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}|=|\overline{\mathrm{a}} \times \overline{\mathrm{b}}| \cdot|\overline{\mathrm{c}}| \cdot \sin 60^{\circ}=(3)(1)\left(\frac{\sqrt{3}}{2}\right)=\frac{3 \sqrt{3}}{2}\end{aligned}$

</details>

---

### Q170. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{A}(3,2,-1), \mathrm{B}(-2,2,-3)$ and $\mathrm{D}(-2,5,-4)$ are the vertices of a parallelogram, then the area of the parallelogram is

**Options:**

- **(A)** 296 sq. units
- **(B)** $\sqrt{286}$ sq. units
- **(C)** 300 sq. units
- **(D)** $\sqrt{300}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{286}$ sq. units**

**Detailed Solution:**

We have $\mathrm{A} \equiv(3,2,-1), \mathrm{B} \equiv(-2,2,-3)$ and $\mathrm{D} \equiv(-2,5,-4)$
$$
\therefore \overline{\mathrm{AB}}=-5 \hat{\mathrm{i}}-2 \hat{\mathrm{k}} \text { and } \overline{\mathrm{AD}}=-5 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}-3 \hat{\mathrm{k}}
$$
Area of parallelogram $=|\overline{\mathrm{AB}} \times \overline{\mathrm{AD}}|$
Now
$$
\begin{aligned}
& \overline{\mathrm{AB}} \times \overline{\mathrm{AD}}=\left|\begin{array}{ccc}
\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\
-5 & 0 & -2 \\
-5 & 3 & -3
\end{array}\right|=\hat{\mathrm{i}}(6)-\hat{\mathrm{j}}(5)+\hat{\mathrm{k}}(-15)=6 \hat{\mathrm{i}}-5 \hat{\mathrm{j}}-15 \hat{\mathrm{k}} \\
& \therefore \text { Area }=\sqrt{(6)^2+(-5)^2+(-15)^2}
\end{aligned}
$$

</details>

---

### Q171. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If â is a unit vector such that $(\bar{x}-\hat{a}) \cdot(\bar{x}+\hat{a})=8$, then $|\bar{x}|=$

**Options:**

- **(A)** $\pm 3$
- **(B)** $2 \sqrt{2}$
- **(C)** 3
- **(D)** $\pm \sqrt{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

We have $(\overline{\mathrm{x}}-\hat{\mathrm{a}}) \cdot(\overline{\mathrm{x}}+\hat{\mathrm{a}})=8$
$$
\therefore|\overline{\mathrm{x}}|^2-|\hat{\mathrm{a}}|^2=8 \Rightarrow|\overline{\mathrm{x}}|^2=8+1=9 \Rightarrow|\overline{\mathrm{x}}|=3
$$

</details>

---

### Q172. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{a}=\hat{i}+2 \hat{j}+3 \hat{k}, \vec{b}=-\hat{\imath}+2 \hat{\jmath}+\hat{k}, \vec{c}=3 \hat{i}+\hat{j}$ and $\bar{a}+\lambda \bar{b}$ is perpendicular to $\overline{\mathrm{c}}$, then $\lambda=$

**Options:**

- **(A)** 5
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 5**

**Detailed Solution:**

$\begin{aligned} & (\bar{a}+\lambda \bar{b}) \cdot \bar{c}=0 \\ & \therefore[(1-\lambda) \hat{i}+(2+2 \lambda) \hat{j}+(3+\lambda) \hat{k}] \cdot[3 \hat{i}+\hat{j}]=0 \\ & \therefore(1-\lambda)(3)+(2+2 \lambda)(1)=0 \Rightarrow \lambda=5\end{aligned}$

</details>

---

### Q173. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{a}=\hat{i}+\hat{j}+\hat{k}, \vec{c}=\hat{j}-\hat{k}, \vec{a} \times \vec{b}=\vec{c}$ and $\vec{a} \cdot \vec{b}=1$, then $\vec{b}$

**Options:**

- **(A)** $\hat{\mathrm{i}}$
- **(B)** $-\hat{\mathrm{i}}$
- **(C)** $\hat{\mathrm{j}}$
- **(D)** $\hat{\mathrm{k}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\hat{\mathrm{i}}$**

**Detailed Solution:**

Let $\vec{b}=x \hat{i}+y \hat{j}+z \hat{k}$ and we have $\vec{a} \cdot \vec{b}=1$
$$
\begin{aligned}
& \therefore(\hat{i}+\hat{j}+\hat{k})(x \hat{i}+y \hat{j}+z \hat{k})=1 \Rightarrow x+y+z=1 \\
& \vec{a} \times \vec{b}=\vec{c} \Rightarrow\left|\begin{array}{lll}
\hat{i} & \hat{j} & \hat{k} \\
1 & 1 & 1 \\
x & y & z
\end{array}\right|=\hat{j}-\hat{k} \\
& \therefore(z-y) \hat{i}-(z-x) \hat{j}+(y-x) \hat{k}=\hat{j}-\hat{k} \\
& \therefore z-y=0, x-z=1, y-x=-1 \\
& \therefore y=z, z=x-1, y=x-1 \\
& \text { Thus } \vec{b}=x \hat{i}+(x-1) \hat{j}+(x-1) \hat{k} \\
& \therefore x+(x-1)+(x-1)=1 \\
& \Rightarrow x=1, y=0, z=0 \\
& \therefore \vec{b}=\hat{i}
\end{aligned}
$$

</details>

---

### Q174. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $|\vec{a}|=4,|\vec{b}|=5$, then the values of $k$ for which $\vec{a}+k \vec{b}$ is perpendicular to $\vec{a}-k \vec{b}$ are

**Options:**

- **(A)** $\pm \frac{5}{4}$
- **(B)** $\pm \frac{2}{5}$
- **(C)** $\pm \frac{16}{25}$
- **(D)** $\pm \frac{4}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pm \frac{4}{5}$**

**Detailed Solution:**

$\begin{aligned} & (\vec{a}+k \vec{b}) \cdot(\vec{a}-k \vec{b})=0 \\ & \therefore|a|^2-k^2|b|^2=0 \\ & \therefore(4)^2-k^2(5)^2=0 \Rightarrow k= \pm \frac{4}{5}\end{aligned}$

</details>

---

### Q175. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area of triangle with vertices $(1,2,0),(1,0, a)$ and $(0,3,1)$ is $\sqrt{6}$ sq. units, then the values of ' $a$ ' are

**Options:**

- **(A)** -8,1
- **(B)** 2,-4
- **(C)** -2,4
- **(D)** 8,-1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2,-4**

**Detailed Solution:**

Refer figure
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/lBuUdCwboftULXw6VbZSEruEQeBnCqmA9RPpnCP23Sw.original.fullsize.png">

$$
\mathrm{A}(\Delta \mathrm{ABC})=\frac{1}{2}|\overline{\mathrm{BA}} \times \overline{\mathrm{BC}}|
$$
Here $\quad \overline{B A}=2 \hat{j}-a \hat{k}$
$$
\overline{\mathrm{BC}}=-\hat{\mathrm{i}}+3 \hat{\mathrm{j}}+(1-a) \hat{\mathrm{k}}
$$
Now $\overline{\mathrm{BA}} \times \overline{\mathrm{BC}}=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 0 & 2 & -\mathrm{a} \\ -1 & 3 & 1-\mathrm{a}\end{array}\right|$
$$
\begin{aligned}
& =\hat{i}(2-2 a+3 a)-\hat{j}(-a)+\hat{k}(2)=(a+2) \hat{i}+(a) \hat{j}+2 \hat{k} \\
\therefore & |\overline{B A} \times \overline{B C}|=\sqrt{(a+2)^2+(a)^2+(2)^2}
\end{aligned}
$$
From given data, we write
$$
\begin{aligned}
& \sqrt{6}=\frac{1}{2} \sqrt{2 a^2+4 a+8} \\
& \therefore 4(6)=2 a^2+4 a+8 \Rightarrow a^2+2 a-8 \\
& \Rightarrow(a+4)(a-2)=0 \\
& \Rightarrow a=-4,2
\end{aligned}
$$

</details>

---

### Q176. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}=\overline{0}$ with $|\overline{\mathrm{a}}|=3,|\overline{\mathrm{b}}|=5$ and $|\overline{\mathrm{c}}|=7$, then angle between $\bar{a}$ and $\bar{b}$ is

**Options:**

- **(A)** $\left(\frac{\pi}{3}\right)^c$
- **(B)** $\left(\frac{4 \pi}{3}\right)^c$
- **(C)** $\left(\frac{2 \pi}{3}\right)^c$
- **(D)** $\pi^{\mathrm{c}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(\frac{\pi}{3}\right)^c$**

**Detailed Solution:**

$\begin{aligned} & \overline{\mathrm{a}}+\overline{\mathrm{b}}=-\overline{\mathrm{c}} \Rightarrow|\overline{\mathrm{a}}+\overline{\mathrm{b}}|^2=|\overline{\mathrm{c}}|^2 \\ & \therefore|\overline{\mathrm{a}}|^2+|\overline{\mathrm{b}}|^2+2|\overline{\mathrm{a}}||\overline{\mathrm{b}}| \cos \theta=|\overline{\mathrm{c}}|^2 \\ & \therefore(3)^2+(5)^2+2(3)(5) \cos \theta=(7)^2 \\ & \therefore \cos \theta=\frac{49-34}{30}=\frac{1}{2} \Rightarrow \theta=\frac{\pi}{3}\end{aligned}$

</details>

---

### Q177. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the parallelogram whose diagonals are represented by the vectors $\bar{a}=3 \hat{i}-\hat{j}-2 \hat{k}$ and $\bar{b}=-\hat{i}+3 \hat{j}-3 \hat{k}$ is

**Options:**

- **(A)** $\sqrt{266}$ sq. units
- **(B)** $\frac{1}{2} \sqrt{266}$ sq. units
- **(C)** 266 sq. units
- **(D)** 122 sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2} \sqrt{266}$ sq. units**

**Detailed Solution:**

Let $\overrightarrow{\mathrm{d}_1}=3 \hat{\mathrm{i}}-\hat{\mathrm{j}}-2 \hat{\mathrm{k}}$ and $\overrightarrow{\mathrm{d}_2}=-\hat{\mathrm{i}}+3 \hat{\mathrm{j}}-3 \hat{\mathrm{k}}$
$\therefore\left|\overrightarrow{\mathrm{d}_1}\right|=\sqrt{14}$ and $\left|\overrightarrow{\mathrm{d}_2}\right|=\sqrt{19}$
$$
\begin{aligned}
& \text { Also } \overrightarrow{\mathrm{d}_1} \times \overrightarrow{\mathrm{d}_2}=\left|\begin{array}{ccc}
\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\
3 & -1 & -2 \\
-1 & 3 & -3
\end{array}\right|=9 \hat{\mathrm{i}}+11 \hat{\mathrm{j}}+8 \hat{\mathrm{k}} \\
& \therefore\left|\overrightarrow{\mathrm{d}_1} \times \overrightarrow{\mathrm{d}_2}\right|=\sqrt{81+121+64}=\sqrt{266} \\
& \left|\mathrm{~d}_1 \times \mathrm{d}_2\right|^2=\left|\mathrm{d}_1\right|^2\left|\mathrm{~d}_2\right|^2 \sin ^2 \theta \\
& \therefore 266=(14)(19) \sin ^2 \theta \\
& \therefore \sin ^2 \theta=1 \quad \Rightarrow \sin \theta=1 \quad \ldots\left[\because 0 < \theta \leq \frac{\pi}{2}\right]
\end{aligned}
$$
Area of parallelogram $=\frac{1}{2}\left|\mathrm{~d}_1\right|\left|\mathrm{d}_2\right| \sin \theta$
$$
=\frac{\sqrt{266}}{2}
$$

</details>

---

### Q178. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The plane $\frac{x}{2}+\frac{y}{3}+\frac{z}{4}=1$ cuts the $\mathrm{X}$-axis at A, Y-axis at C, then the area of $\triangle \mathrm{ABC}=$

**Options:**

- **(A)** $\sqrt{71}$ sq. units
- **(B)** $\sqrt{29}$ sq. units
- **(C)** $\sqrt{41}$ sq. units
- **(D)** $\sqrt{61}$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{61}$ sq. units**

**Detailed Solution:**

The vertices of triangle $\mathrm{ABC}$ are
$$
\begin{aligned}
& \mathrm{A}=(2,0,0) ; \mathrm{B}=(0,3,0) ; \mathrm{C}=(0,0,4) \\
& \overline{\mathrm{AB}}=-2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}} \text { and } \overline{\mathrm{AC}}=-2 \hat{\mathrm{i}}+4 \hat{\mathrm{k}} \\
& \overline{\mathrm{AB}} \times \overline{\mathrm{AC}}=\left|\begin{array}{ccc}
\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\
-2 & 3 & 0 \\
-2 & 0 & 4
\end{array}\right|=\hat{\mathrm{i}}(12)-\hat{\mathrm{j}}(-8)+\hat{\mathrm{k}}(6)=12 \hat{\mathrm{i}}+8 \hat{\mathrm{j}}+6 \hat{\mathrm{k}} \\
& \therefore \mathrm{A}(\triangle \mathrm{ABC})=\frac{1}{2}|\overline{\mathrm{AB}} \times \overline{\mathrm{AC}}| \\
& =\frac{1}{2}(\sqrt{144+64+36}) \\
& =\sqrt{61} \text { sq. units } \\
&
\end{aligned}
$$

</details>

---

### Q179. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The shortest distance between lines $\overline{\mathrm{r}}=(2 \hat{\mathrm{i}}-\hat{\mathrm{j}})+\lambda(2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-3 \hat{\mathrm{k}})$ and $\overline{\mathrm{r}}=(\hat{\mathrm{r}}-\hat{\mathrm{j}}+2 \hat{\mathrm{k}})+\mu(2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-5 \hat{\mathrm{k}})$ is

**Options:**

- **(A)** $\frac{1}{\sqrt{5}}$
- **(B)** 3 units
- **(C)** $\sqrt{5}$ units
- **(D)** 2 units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\sqrt{5}}$**

**Detailed Solution:**

We have lines $\overline{\mathrm{r}}=(2 \hat{\mathrm{i}}-\hat{\mathrm{j}})+\lambda(2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-3 \hat{\mathrm{k}})$
and $\overline{\mathrm{r}}=(\hat{\mathrm{r}}-\hat{\mathrm{j}}+2 \hat{\mathrm{k}})+\mu(2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-5 \hat{\mathrm{k}})$
Let $\bar{a}=2 \hat{i}-\hat{j}$ and $\bar{b}=\hat{i}-\hat{j}+2 \hat{k}$
$$
\therefore \overline{\mathrm{AB}}=-\hat{\mathrm{i}}+2 \hat{\mathrm{k}}
$$
Vector perpendicular to given lines is
$$
\overline{\mathrm{n}}=\left|\begin{array}{ccc}
\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\
2 & 1 & -3 \\
2 & 1 & -5
\end{array}\right|=\hat{\mathrm{i}}(-5+3)-\hat{\mathrm{j}}(-10+6)+\hat{\mathrm{k}}(2-2)=-2 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}
$$
Shortest distance between given lines
$$
=\overline{\mathrm{AB}} \cdot \frac{\overline{\mathrm{n}}}{|\overline{\mathrm{n}}|}=\frac{(-\hat{\mathrm{i}}+2 \hat{\mathrm{k}}) \cdot(-2 \hat{\mathrm{i}}+4 \hat{\mathrm{j}})}{\sqrt{(-2)^2+(4)^2}}=\frac{2}{\sqrt{20}}=\frac{1}{\sqrt{5}}
$$

</details>

---

### Q180. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}, \bar{b}, \bar{c}$ are mutually perpendicular vectors having magnitudes 1,2,3 respectively, then $[\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}} \overline{\mathrm{b}}-\overline{\mathrm{a}} \overline{\mathrm{c}}]=$

**Options:**

- **(A)** 12
- **(B)** 18
- **(C)** 0
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 12**

**Detailed Solution:**

$\begin{aligned} & {[\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}} \quad \overline{\mathrm{b}}-\overline{\mathrm{a}} \quad \overline{\mathrm{c}}]} \\ & =(\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}) \cdot[(\overline{\mathrm{b}}-\overline{\mathrm{a}}) \times \overline{\mathrm{c}}] \\ & =(\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}) \cdot[(\overline{\mathrm{b}} \times \overline{\mathrm{c}})-(\overline{\mathrm{a}} \times \overline{\mathrm{c}})] \\ & =\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})-\overline{\mathrm{b}} \cdot(\overline{\mathrm{a}} \times \overline{\mathrm{c}})=\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})+\overline{\mathrm{b}} \cdot(\overline{\mathrm{c}} \times \overline{\mathrm{a}}) \\ & =2 \overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})=2(1)(2)(3)=12\end{aligned}$

</details>

---

### Q181. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $|\bar{a} \times \bar{b}|^2+(\bar{a} \cdot \bar{b})^2=144$ and $|\bar{a}|=4$, then $|\bar{b}|=$

**Options:**

- **(A)** 8
- **(B)** 12
- **(C)** 3
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

$\begin{aligned} & |\overline{\mathrm{a}} \times \overline{\mathrm{b}}|^2+(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})^2=144 \text { and }|\overline{\mathrm{a}}|=4 \\ & \therefore\left(|\overline{\mathrm{a}}|^2 \cdot|\overline{\mathrm{b}}|^2 \cdot \sin ^2 \theta\right)+\left(|\overline{\mathrm{a}}|^2|\overline{\mathrm{b}}|^2 \cos ^2 \theta\right)=144 \\ & \therefore|\overline{\mathrm{a}}|^2|\overline{\mathrm{b}}|^2\left(\cos ^2 \theta+\sin ^2 \theta\right)=144 \\ & \therefore(4)^2|\overline{\mathrm{b}}|^2=144 \Rightarrow|\overline{\mathrm{b}}|^2=9 \Rightarrow|\overline{\mathrm{b}}|=3\end{aligned}$

</details>

---

### Q182. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\frac{\pi}{2} < \theta \leq$ and $|\overline{\mathrm{a}}|=5,|\overline{\mathrm{b}}|=13,|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|=25$, then the value of $\bar{a} \cdot \bar{b}$ is

**Options:**

- **(A)** -12
- **(B)** 60
- **(C)** -60
- **(D)** -13

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -60**

**Detailed Solution:**

$\begin{aligned} & |\overline{\mathrm{a}} \times \overline{\mathrm{b}}|=25 \\ & \therefore|\overline{\mathrm{a}}| \cdot|\overline{\mathrm{b}}| \cdot \sin \theta=(5)(13) \sin \theta=25 \\ & \therefore \sin \theta=\frac{5}{13} \Rightarrow \cos \theta=\frac{-12}{13} \\ & \overline{\mathrm{a}} \cdot \overline{\mathrm{b}}=|\overline{\mathrm{a}}| \cdot|\overline{\mathrm{b}}| \cdot \cos \theta \\ & =(5)(13)\left(\frac{-12}{13}\right)=-60\end{aligned}$

</details>

---

### Q183. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}=\hat{i}+2 \hat{j}-3 \hat{k}, \bar{b}=3 \hat{i}+\hat{j}+2 \hat{k}, \bar{c}=\hat{i}+3 \hat{j}+\hat{k}$ and $\bar{a}+\lambda \bar{b}$ is perpendicular to $\overline{\mathrm{c}}$, then $\lambda=$

**Options:**

- **(A)** -2
- **(B)** 4
- **(C)** -4
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -2**

**Detailed Solution:**

$$
\begin{aligned}
& \bar{a}+\lambda \bar{b}=(\hat{i}+2 \hat{j}-3 \hat{k})+\lambda(3 \hat{i}-\hat{j}+2 \hat{k}) \\
& =(1+3 \lambda) \hat{i}+(2-\lambda) \hat{j}+(-3+2 \lambda) \hat{k}
\end{aligned}
$$
Since $\overline{\mathrm{a}}+\lambda \overline{\mathrm{b}}$ is $\perp$ er to $\overline{\mathrm{c}}$, we write
$$
\begin{aligned}
& (1)(1+3 \lambda)+(3)(2-\lambda)+(1)(-3+2 \lambda) \\
& \therefore 1+3 \lambda+6-3 \lambda-3+2 \lambda=0 \Rightarrow \lambda=-2
\end{aligned}
$$

</details>

---

### Q184. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the parallelogram with vertices $\mathrm{A}(1,2,3), \mathrm{B}(1,3, \mathrm{a})$, $C(3,8,6)$ and $D(3,7,3)$ is $\sqrt{265}$ sq. units, then $a=$

**Options:**

- **(A)** -5,2
- **(B)** 6
- **(C)** -6,0
- **(D)** 6,0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 6**

**Detailed Solution:**

Refer figure<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/aqfqOJ8LjgmZO3lRkWp0DXORc33QeNSmStIhrLp4EfQ.original.fullsize.png">

$$
\begin{gathered}
\mathrm{A}(\triangle \mathrm{ABC})=\frac{\mathrm{A}(\square \mathrm{ABCD})}{2} \\
=\frac{\sqrt{265}}{2}
\end{gathered}
$$
Also $\mathrm{A}(\triangle \mathrm{ABC})=\frac{1}{2}|\overline{\mathrm{BA}} \times \overline{\mathrm{BC}}|$
Here $\overline{\mathrm{BA}}=-\hat{\mathrm{j}}+(3-\mathrm{a}) \hat{\mathrm{k}}$ and $\overline{\mathrm{BC}}=2 \hat{\mathrm{i}}+5 \hat{\mathrm{j}}+(6-\mathrm{a}) \hat{\mathrm{k}}$
$$
\begin{aligned}
& \text { Now } \overline{B A} \times \overline{B C}=\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
0 & -1 & (3-a) \\
2 & 5 & (6-a)
\end{array}\right| \\
& =\hat{i}(-6+a-15+5 a)-\hat{j}(-6+2 a)+\hat{k}(2) \\
& =(6 a-21) \hat{i}-(2 a-6) \hat{j}+2 \hat{k}
\end{aligned}
$$
Magnitude of $\overline{\mathrm{BA}} \times \overline{\mathrm{BC}}=\sqrt{(6 \mathrm{a}-21)^2+(2 \mathrm{a}-6)^2+4}$
$$
\begin{aligned}
& \therefore \frac{1}{2} \sqrt{(6 a-21)^2+(2 a-6)^2+4}=\frac{\sqrt{265}}{2} \\
& \therefore(6 a-21)^2+(2 a-6)^2+4=265 \\
& \therefore 40 a^2-276 a+216=0
\end{aligned}
$$<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/866-RPtijSPRKxmxJ7xiIZFbDgiRkJVoClbjs0q6mLk.original.fullsize.png">

$\therefore a=6$ from option given.

</details>

---

### Q185. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $|\bar{a}|=3,|\bar{b}|=4,|\bar{a}-\bar{b}|=5$, then $|\bar{a}+\bar{b}|=$

**Options:**

- **(A)** 9
- **(B)** 25
- **(C)** 5
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5**

**Detailed Solution:**

$$
\begin{aligned}
& |\overline{\mathrm{a}}+\overline{\mathrm{b}}|^2=|\overline{\mathrm{a}}-\overline{\mathrm{b}}|^2+4 \cdot \overline{\mathrm{a}} \cdot \overline{\mathrm{b}} \\
& \text { Now }|\overline{\mathrm{a}}-\overline{\mathrm{b}}|^2=|\overline{\mathrm{a}}|^2+|\overline{\mathrm{b}}|^2-2 \overline{\mathrm{a}} \cdot \overline{\mathrm{b}} \\
& \therefore(5)^2=(3)^2+(4)^2-2 \overline{\mathrm{a}} \cdot \overline{\mathrm{b}} \Rightarrow \overline{\mathrm{a}} \cdot \overline{\mathrm{b}}=0
\end{aligned}
$$
Substituting in (1), we get
$$
|\overline{\mathrm{a}}+\overline{\mathrm{b}}|^2=|\overline{\mathrm{a}}-\overline{\mathrm{b}}|^2 \Rightarrow|\overline{\mathrm{a}}+\overline{\mathrm{b}}|=5
$$

</details>

---

### Q186. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\overline{\mathrm{a}}=3 \hat{\mathrm{i}}-5 \hat{\mathrm{j}}, \overline{\mathrm{b}}=6 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}$ are two vectors and $\overline{\mathrm{c}}$ is vector such that $\bar{c}=\bar{a} \times \bar{b}$, then $a: b: c$ is

**Options:**

- **(A)** $\sqrt{34}: \sqrt{45}: \sqrt{39}$
- **(B)** $\sqrt{34}: \sqrt{45}: 39$
- **(C)** $34: 39: 45$
- **(D)** $39: 35: 34$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{34}: \sqrt{45}: 39$**

**Detailed Solution:**

$$
\begin{aligned}
& \overline{\mathrm{c}}=\overline{\mathrm{a}} \times \overline{\mathrm{b}}=\left|\begin{array}{ccc}
\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\
3 & -5 & 0 \\
6 & 3 & 0
\end{array}\right|=\hat{\mathrm{i}}(0)-\hat{\mathrm{j}}(0)+\hat{\mathrm{k}}(9+30)=39 \hat{\mathrm{k}} \\
& |\overline{\mathrm{a}}|=\sqrt{(3)^2+(-5)^2}=\sqrt{34} \text { and }|\overline{\mathrm{b}}|=\sqrt{(6)^2+(3)^2}=\sqrt{45} \\
& |\overline{\mathrm{c}}|=\sqrt{39^2}=39 \\
& \therefore \mathrm{a}: \mathrm{b}: \mathrm{c}=\sqrt{34}: \sqrt{45}: 39
\end{aligned}
$$

</details>

---

### Q187. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If vectors $\bar{a}=2 \hat{i}+2 \hat{j}+3 \hat{k}, \bar{b}=-\hat{i}+2 \hat{j}+\hat{k}$ and $\bar{c}=-3 \hat{i}+\hat{j}+2 \hat{k}$ are such that, $\overline{\mathrm{a}}+\lambda \overline{\mathrm{b}}$ is perpendicular to $\overline{\mathrm{c}}$, then $\lambda=$

**Options:**

- **(A)** -14
- **(B)** 14
- **(C)** 2
- **(D)** -2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -14**

**Detailed Solution:**

From given data, we write
$$
\bar{a}+\lambda \bar{b}=(2-\lambda) 
\hat{i}+(2+2 \lambda) 
\hat{j}+(3+\lambda) 
\hat{k}
$$
Since (1) is $\perp$ er to $\bar{c}$, we write
$$
\begin{aligned}
& (2-\lambda)(3)+(2+2 \lambda)(1)+(3+\lambda)(2)=0 \\
& \therefore 6-3 \lambda+2+2 \lambda+6+2 \lambda=0 \Rightarrow \lambda=-14
\end{aligned}
$$

</details>

---

### Q188. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If area of the parallelogram with $\bar{a}$ and $\bar{b}$ as two adjacent sides is 20 square units, then the area of the parallelogram having $3 \bar{a}$ $+\overline{\mathrm{b}}$ and $2 \overline{\mathrm{a}}+3 \overline{\mathrm{b}}$ as two adjacent sides in square units is

**Options:**

- **(A)** 105
- **(B)** 120
- **(C)** 75
- **(D)** 140

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 140**

**Detailed Solution:**

We have $|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|=20$ and we have to find value of
$$
\begin{aligned}
& |(3 \overline{\mathrm{a}}+\overline{\mathrm{b}}) \times(2 \overline{\mathrm{a}}+3 \overline{\mathrm{b}})| \\
& (3 \overline{\mathrm{a}}+\overline{\mathrm{b}}) \times(2 \overline{\mathrm{a}}+3 \overline{\mathrm{b}}) \\
& =6(\overline{\mathrm{a}} \times \overline{\mathrm{b}})+9(\overline{\mathrm{a}} \times \overline{\mathrm{b}})+2(\overline{\mathrm{b}} \times \overline{\mathrm{a}})+3(\overline{\mathrm{b}} \times \overline{\mathrm{b}}) \\
& =0+9(\overline{\mathrm{a}} \times \overline{\mathrm{b}})-2(\overline{\mathrm{a}} \times \overline{\mathrm{b}})+0=7(\overline{\mathrm{a}} \times \overline{\mathrm{b}})
\end{aligned}
$$
Hence area of the required parallelogram $=7 \times 20=140$

</details>

---

### Q189. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\bar{a}, \bar{b}, \bar{c}$ are vectors such that $|\bar{a}|=5,|\bar{b}|=4,|\bar{c}|=3$ and each is perpendicular to the sum of the other two, then $|\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}|^2=$

**Options:**

- **(A)** 60
- **(B)** 12
- **(C)** 47
- **(D)** 50

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 50**

**Detailed Solution:**

We have $\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}}+\overline{\mathrm{c}})=0 \cdot \overline{\mathrm{b}} \cdot(\overline{\mathrm{c}}+\overline{\mathrm{a}})=0$ and $\overline{\mathrm{c}} \cdot(\overline{\mathrm{a}}+\overline{\mathrm{b}})=0$
$$
\begin{aligned}
\therefore \quad & \overline{\mathrm{a}} \cdot \overline{\mathrm{b}}+\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=0 \\
& \overline{\mathrm{b}} \cdot \overline{\mathrm{c}}+\overline{\mathrm{b}} \cdot \overline{\mathrm{a}}=0 \\
& \overline{\mathrm{c}} \cdot \overline{\mathrm{a}}+\overline{\mathrm{c}} \cdot \overline{\mathrm{b}}=0
\end{aligned}
$$
From (1), (2) and (3), we get
$$
\begin{aligned}
& 2(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}+\overline{\mathrm{b}} \cdot \overline{\mathrm{c}}+\overline{\mathrm{c}} \cdot \overline{\mathrm{a}})=0 \\
& \text { Now }|\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}|^2=|\overline{\mathrm{a}}|^2+|\overline{\mathrm{b}}|^2+|\overline{\mathrm{c}}|^2+2(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}+\overline{\mathrm{b}} \cdot \overline{\mathrm{c}}+\overline{\mathrm{c}} \cdot \overline{\mathrm{a}}) \\
& \therefore|\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}|^2=(5)^2+(4)^2+(3)^2+2(0)=50
\end{aligned}
$$

</details>

---

### Q190. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{e}}_1, \overline{\mathrm{e}}_2$ and $\overline{\mathrm{e}}_1+\overline{\mathrm{e}}_2$ are unit vectors, then the angle between $\overline{\mathrm{e}}_1$ and $\bar{e}_2$ is

**Options:**

- **(A)** $150^{\circ}$
- **(B)** $120^{\circ}$
- **(C)** $90^{\circ}$
- **(D)** $135^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $120^{\circ}$**

**Detailed Solution:**

$\begin{aligned} & \left|\overline{\mathrm{e}}_1+\overline{\mathrm{e}}_2\right|^2=\left|\overline{\mathrm{e}}_1^2\right|+\left|\overline{\mathrm{e}}_2^2\right|+2 \overline{\mathrm{e}}_1 \overline{\mathrm{e}}_2 \cos \theta \\ & \text { Here }\left|\overline{\mathrm{e}}_1\right|=1,\left|\overline{\mathrm{e}}_2\right|=1 \text { and }\left|\overline{\mathrm{e}}_1+\overline{\mathrm{e}}_2\right|=1 \\ & \therefore(1)=(2)^2+(1)^2+2(1)(1) \cos \theta \\ & \therefore \frac{-1}{2}=\cos \theta \Rightarrow \theta=120^{\circ}\end{aligned}$

</details>

---

### Q191. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}, \bar{b}, \bar{c}$ are three vectors which are perpendicular to $\overline{\mathrm{b}}+\overline{\mathrm{c}}, \overline{\mathrm{c}}+\overline{\mathrm{a}}$, and $\overline{\mathrm{a}}+\overline{\mathrm{b}}$ respectively, such that $|\overline{\mathrm{a}}|=2|\overline{\mathrm{b}}|=3,|\overline{\mathrm{c}}|=4$, then $|\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}|=$

**Options:**

- **(A)** 29
- **(B)** 3
- **(C)** 9
- **(D)** $\sqrt{29}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{29}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/wtSqsAlI5A-ql9f2u8BsHoU6ZQRtwnrgTYzFYcLWNhI.original.fullsize.png">

</details>

---

### Q192. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$(2 \hat{i}+6 \hat{i}+27 \hat{k}) \times(\hat{i}+\lambda \hat{j}+\mu \hat{k})=\overline{0}$, then $\lambda$ and $\mu$ are respectively

**Options:**

- **(A)** $\frac{17}{2}, 3$
- **(B)** $3, \frac{17}{2}$
- **(C)** $3, \frac{27}{2}$
- **(D)** $\frac{27}{2}, 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3, \frac{27}{2}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/tA5DtZjNOyIKvjThlKIebZ9lkrDEfVv0ud8pCS_15Fg.original.fullsize.png">

</details>

---

### Q193. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The direction ratios of the line perpendicular to the lines having direction ratios $2,3,1$
and $1,2,1$ are

**Options:**

- **(A)** $-2,1,1$
- **(B)** $1,1,1$
- **(C)** $1,-1,1$
- **(D)** $2,2,-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1,-1,1$**

**Detailed Solution:**

(D)
Let $\bar{a}$ and $\bar{b}$ be the vectors along the lines whose direction ratios are $2,3,1$ and $1,2,1$ respectively.
$\therefore \overline{\mathrm{a}}=2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+\hat{\mathrm{k}} \quad \text { and } \quad \overline{\mathrm{b}}=\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}}$
A vector perpendicular to both $\bar{a}$ and $\bar{b}$ is given by,
$\bar{a} \times \bar{b}=\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
2 & 3 & 1 \\
1 & 2 & 1
\end{array}\right|=\hat{i}(3-2)-\hat{j}(2-1)+\hat{k}(4-3)=\hat{i}-\hat{j}+\hat{k}$
Hence d.r.s are $1,-1,1$

</details>

---

### Q194. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}=\hat{\imath}+5 \hat{k}, \bar{b}=2 \hat{\imath}+3 \hat{k}, \bar{c}=4 \hat{\imath}-\hat{\jmath}+2 \hat{k}$ and $\bar{d}=\hat{\imath}-\hat{\jmath}$,
then $(\bar{c}-\bar{a}) \cdot(\bar{b} \times \bar{d})=$

**Options:**

- **(A)** $12$
- **(B)** $20$
- **(C)** $30$
- **(D)** $10$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $12$**

**Detailed Solution:**

$\bar{b} \times \bar{d}=\left|\begin{array}{ccc}\hat{i} & \hat{j} & \hat{k} \\ 2 & 0 & 3 \\ 1 & -1 & 0\end{array}\right|=\hat{i}(3)-\hat{j}(0-3)+\hat{k}(-2)$
$\bar{b} \times \bar{d}=3 \hat{i}+3 \hat{j}-2 \hat{k}$
and $\bar{c}-\bar{a}=3 \hat{i}-\hat{j}-3 \hat{k}$
then $(\bar{c}-\bar{a}) \cdot(\bar{b} \times \bar{d})=3(3)+(-1)(3)+(-3)(-2)$
$=9-3+6=12$

</details>

---

### Q195. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}=2 i+3 j-\hat{k}, \bar{b}=-i+2 j-4 \hat{k}$ and $\bar{c}=i+j+\hat{k}$, then $(\bar{a} \times \bar{b}) \cdot(\bar{a} \times \bar{c})=$

**Options:**

- **(A)** $-74$
- **(B)** 64
- **(C)** $-64$
- **(D)** 74

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-74$**

**Detailed Solution:**

$\bar{a} \times \bar{b}=\left|\begin{array}{ccc}\hat{i} & \hat{j} & \hat{k} \\ 2 & 3 & -1 \\ -1 & 2 & -4\end{array}\right|=\hat{i}(-12+2)-\hat{j}(-8-1)+\hat{k}(4+3)=-10 \hat{i}+9 \hat{j}+7 \hat{k}$
$\begin{aligned} \bar{a} \times \bar{c} &=\left|\begin{array}{ccc}\hat{i} & \hat{j} & \hat{k} \\ 2 & 3 & -1 \\ 1 & 1 & 1\end{array}\right|=\hat{i}(3+1)-\hat{j}(2+1)+\hat{k}(2-3)=4 \hat{i}-3 \hat{j}-\hat{k} \\ \text { Here } \quad(\bar{a} \times \bar{b}) \cdot(\bar{a} \times \bar{c}) &=(-10 \hat{i}+9 \hat{j}+7 \hat{k}) \cdot(4 \hat{i}-3 \hat{j}-\hat{k}) \\ &=(-10)(4)+9(-3)+7(-1) \\ &=-40-27-7=-74 \end{aligned}$

</details>

---

### Q196. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{P}(3,2,6), \mathrm{Q}(1,4,5)$ and $\mathrm{R}(3,5,3)$ are the vertices of $\Delta \mathrm{PQR}$, then $\mathrm{m} \angle \mathrm{PQR}$ is

**Options:**

- **(A)** $90^{\circ}$
- **(B)** $50^{\circ}$
- **(C)** $70^{\circ}$
- **(D)** $30^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $90^{\circ}$**

**Detailed Solution:**

We have $P \equiv(3,2,6) ; Q \equiv(1,4,5)$ and $R \equiv(3,5,3)$ 
d.r. of $\mathrm{PQ}$ are $-2,2,-1$ and d.r. of $\mathrm{QR}$ are $2,1,-2$ 
We find that : $(-2)(2)+2(1)+(-1)(-2)=-4+2+2=0$ 
$\therefore \mathrm{PQ} \perp \mathrm{QR} \Rightarrow \mathrm{m} \angle \mathrm{PQR}=90^{\circ}$

</details>

---

### Q197. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{u}=\mathrm{a}-\mathrm{b}$ and $\mathrm{v}=\mathrm{a}+\mathrm{b}$ and $|\mathrm{a}|=|\mathrm{b}|=2$, then
$|\mathbf{u} \times \mathbf{v}|$ is equal to

**Options:**

- **(A)** $2 \sqrt{16-(a \cdot b)^{2}}$
- **(B)** $\sqrt{16-(\mathrm{a} \cdot \mathbf{b})^{2}}$
- **(C)** $2 \sqrt{4-(\mathbf{a} \cdot \mathbf{b})^{2}}$
- **(D)** $2 \sqrt{4+(\mathbf{a} \cdot \mathbf{b})^{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \sqrt{16-(a \cdot b)^{2}}$**

**Detailed Solution:**

$|\mathbf{u} \times \mathbf{v}|=|(\mathbf{a}-\mathbf{b}) \times(\mathbf{a}+\mathbf{b})|$
$$
=2|\mathbf{a} \times \mathbf{b}| \quad(\because \mathbf{a} \times \mathbf{a}=\mathbf{b} \times \mathbf{b}=0)
$$
and $|\mathbf{a} \times \mathbf{b}|^{2}+(\mathbf{a} \cdot \mathbf{b})^{2}=(a b \sin \theta)^{2}+(a b \cos \theta)^{2}$
$$
=a^{2} b^{2}
$$
$$
\begin{array}{l}
\Rightarrow \quad|\mathbf{a} \times \mathbf{b}|=\sqrt{a^{2} b^{2}-(\mathbf{a} \cdot \mathbf{b})^{2}} \\
\text { So, } \quad|\mathbf{u} \times \mathbf{v}|=2|\mathbf{a} \times \mathbf{b}|
\end{array}
$$
$$
\begin{array}{l}
=2 \sqrt{a^{2} b^{2}-(\mathbf{a} \cdot \mathbf{b})^{2}} \\
=2 \sqrt{2^{2} 2^{2}-(\mathbf{a} \cdot \mathbf{b})^{2}} \\
\left.=2 \sqrt{16-(\mathbf{a} \cdot \mathbf{b})^{2}} \because|\mathbf{a}|=|\mathbf{b}|=2\right)
\end{array}
$$

</details>

---

### Q198. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

The position vectors of vertices of a $\Delta A B C$ are $\begin{array}{lll}4 \hat{\mathbf{i}}-2 \hat{\mathbf{j}}, & \hat{\mathbf{i}}+4 \hat{\mathbf{j}}-3 \hat{\mathbf{k}} \quad \text { and } & -\hat{\mathbf{i}}+5 \hat{\mathbf{j}}+\hat{\mathbf{k}}\end{array}$
respectively, then $\angle A B C$ is equal to

**Options:**

- **(A)** $\frac{\pi}{6}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{2}$**

**Detailed Solution:**

Here $, \overrightarrow{\mathbf{A B}}=-3 \hat{\mathbf{i}}+6 \hat{\mathbf{j}}-3 \hat{\mathbf{k}}, \overrightarrow{\mathbf{B C}}=-2 \hat{\mathbf{i}}+\hat{\mathbf{j}}+4 \hat{\mathbf{k}}$
and $\overrightarrow{\mathbf{A B}} \cdot \overrightarrow{\mathbf{B C}}=6+6-12=0$
$$
\angle A B C=\frac{\pi}{2}
$$

</details>

---

### Q199. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

If $|\overrightarrow{\mathbf{a}}|=2,|\overrightarrow{\mathbf{b}}|=3$ and $\overrightarrow{\mathbf{a}}, \overrightarrow{\mathbf{b}}$ are mutually
perpendicular, then the area of the triangle whose vertices are $\overrightarrow{\mathbf{0}}, \overrightarrow{\mathbf{a}}+\overrightarrow{\mathbf{b}}, \overrightarrow{\mathbf{a}}-\overrightarrow{\mathbf{b}}$ is

**Options:**

- **(A)** 5
- **(B)** 1
- **(C)** 6
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 6**

**Detailed Solution:**

Let the position vectors of the points $A, B, C$ are
$$
\begin{array}{l}
\mathbf{0}, \mathbf{a}+\mathbf{b}, \mathbf{a}-\mathbf{b} \text { and } \theta=90^{\circ} . \\
\therefore \text { Area of triangle }=\frac{1}{2}|\overrightarrow{\mathbf{A B}} \times \overrightarrow{\mathbf{A C}}| \\
\left.\quad=\frac{1}{2} \mid \overrightarrow{\mathbf{a}}+\overrightarrow{\mathbf{b}}\right) \times(\overrightarrow{\mathbf{a}}-\overrightarrow{\mathbf{b}}) \mid \\
=\frac{1}{2}|2 \overrightarrow{\mathbf{b}} \times \overrightarrow{\mathbf{a}}| \\
=|\overrightarrow{\mathbf{b}}||\overrightarrow{\mathbf{a}}| \sin \theta \\
=3 \times 2 \sin 90^{\circ} \\
=6
\end{array}
$$

</details>

---

### Q200. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

If the vectors $\hat{\mathbf{i}}-3 \hat{\mathbf{j}}+2 \hat{\mathbf{k}},-\hat{\mathbf{i}}+2 \hat{\mathbf{j}}$ represents
the diagonals of a parallelogram, then its area will be

**Options:**

- **(A)** $\sqrt{21}$
- **(B)** $\frac{\sqrt{21}}{2}$
- **(C)** $2 \sqrt{21}$
- **(D)** $\frac{\sqrt{21}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\sqrt{21}}{2}$**

**Detailed Solution:**

Let 
$\overrightarrow{\mathbf{a}}=\hat{\mathbf{i}}-3 \hat{\mathbf{j}}+2 \hat{\mathbf{k}}, \overrightarrow{\mathbf{b}}=-\hat{\mathbf{i}}+2 \hat{\mathbf{j}}$
Now, $\overrightarrow{\mathbf{a}} \times \overrightarrow{\mathbf{b}}=\left|\begin{array}{rrr}\hat{\mathbf{i}} & \hat{\mathbf{j}} & \mathbf{k} \\ 1 & -3 & 2 \\ -1 & 2 & 0\end{array}\right|$
$=-4 \hat{\mathbf{i}}-2 \hat{\mathbf{j}}-\hat{\mathbf{k}}$
Hence, required area $=\frac{1}{2}|\overrightarrow{\mathbf{a}} \times \overrightarrow{\mathbf{b}}|$
$=\frac{1}{2} \sqrt{16+4+1}=\frac{\sqrt{21}}{2}$

</details>

---

### Q201. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

If $\overrightarrow{\mathbf{a}} \cdot \hat{\mathbf{i}}=4$, then $(\overrightarrow{\mathbf{a}} \times \hat{\mathbf{j}}) \cdot(2 \hat{\mathbf{j}}-3 \hat{\mathbf{k}})$ is equal to

**Options:**

- **(A)** 12
- **(B)** 2
- **(C)** 0
- **(D)** $-12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-12$**

**Detailed Solution:**

$(\overrightarrow{\mathbf{a}} \times \hat{\mathbf{j}}) \cdot(2 \hat{\mathbf{j}}-3 \hat{\mathbf{k}})=\overrightarrow{\mathbf{a}} \cdot\{\hat{\mathbf{j}} \times(2 \hat{\mathbf{j}}-3 \hat{\mathbf{k}})\}$
$$
\begin{array}{l}
=\overrightarrow{\mathbf{a}} \cdot\{-3(\hat{\mathbf{j}} \times \hat{\mathbf{k}})\} \\
=-3(\overrightarrow{\mathbf{a}} \cdot \hat{\mathbf{i}}) \\
=-12 \quad(\because \overrightarrow{\mathbf{a}} \cdot \hat{\mathbf{i}}=4 \text { given })
\end{array}
$$

</details>

---

### Q202. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

If the constant forces $2 \hat{\mathbf{i}}-5 \hat{\mathbf{j}}+6 \hat{\mathbf{k}}$ and $-\hat{\mathbf{i}}+2 \hat{\mathbf{j}}-\hat{\mathbf{k}}$ act on a particle due to which it is displaced from a point $A(4,-3,-2)$ to a point $B(6,1,-3)$, then the work done by the forces is

**Options:**

- **(A)** 15 unit
- **(B)** 9 unit
- **(C)** $-15$ unit
- **(D)** $-9$ unit

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-15$ unit**

**Detailed Solution:**

Resultant force,
$$
\overrightarrow{\mathbf{F}}=(2 \hat{\mathbf{i}}-5 \hat{\mathbf{j}}+6 \hat{\mathbf{k}})+(-\hat{\mathbf{i}}+2 \hat{\mathbf{j}}-\hat{\mathbf{k}})=\hat{\mathbf{i}}-3 \mathbf{j}+5 \hat{\mathbf{k}}
$$
Displacement,
$$
\begin{aligned}
\overrightarrow{\mathbf{d}}=\overrightarrow{\mathbf{A B}} &=(6 \hat{\mathbf{i}}+\hat{\mathbf{j}}-3 \hat{\mathbf{k}})-(4 \hat{\mathbf{i}}-3 \hat{\mathbf{j}}-2 \hat{\mathbf{k}}) \\
&=2 \hat{\mathbf{i}}+4 \hat{\mathbf{j}}-\hat{\mathbf{k}} \\
W &=\overrightarrow{\mathbf{F}} \cdot \overrightarrow{\mathbf{d}}=(\hat{\mathbf{i}}-3 \hat{\mathbf{j}}+5 \hat{\mathbf{k}}) \cdot(2 \hat{\mathbf{i}}+4 \hat{\mathbf{j}}-\hat{\mathbf{k}}) \\
&=2-12-5=-15 \text { unit }
\end{aligned}
$$

</details>

---

### Q203. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `2`

If $\overrightarrow{\mathbf{a}}+\overrightarrow{\mathbf{b}}+\overrightarrow{\mathbf{c}}=\overrightarrow{\mathbf{0}},|\overrightarrow{\mathbf{a}}|=3,|\overrightarrow{\mathbf{b}}|=5,|\overrightarrow{\mathbf{c}}|=7$, then
the angle between $\overrightarrow{\mathbf{a}}$ and $\overrightarrow{\mathbf{b}}$ is

**Options:**

- **(A)** $\pi / 6$
- **(B)** $2 \pi / 3$
- **(C)** $5 \pi / 3$
- **(D)** $\pi / 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pi / 3$**

**Detailed Solution:**

Given, $\overrightarrow{\mathbf{a}}+\overrightarrow{\mathbf{b}}+\overrightarrow{\mathbf{c}}=\overrightarrow{\mathbf{0}}$
$$
\begin{array}{ll}
\therefore \quad & \overrightarrow{\mathbf{c}}=-(\overrightarrow{\mathbf{a}}+\overrightarrow{\mathbf{b}}) \\
\Rightarrow & |\overrightarrow{\mathbf{c}}|^{2}=\overrightarrow{\mathbf{c}} \overrightarrow{\mathbf{c}}=(\overrightarrow{\mathbf{a}}+\overrightarrow{\mathbf{b}}) \cdot(\overrightarrow{\mathbf{a}}+\overrightarrow{\mathbf{b}})
\end{array}
$$
$$
\begin{array}{l}
\Rightarrow \quad|\overrightarrow{\mathbf{c}}|^{2}=|\overrightarrow{\mathbf{a}}|^{2}+|\overrightarrow{\mathbf{b}}|^{2}+2 \overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{b}} \\
\Rightarrow \quad|\overrightarrow{\mathbf{c}}|^{2}=|\overrightarrow{\mathbf{a}}|^{2}+|\overrightarrow{\mathbf{b}}|^{2}+2|\overrightarrow{\mathbf{a}}||\overrightarrow{\mathbf{b}}| \cos \theta \\
\Rightarrow \quad 49=9+25+2 \times 3 \times 5 \cos \theta \\
\Rightarrow \quad \quad 15=30 \cos \theta \quad \Rightarrow \quad \cos \theta=\frac{1}{2} \\
\Rightarrow \quad \theta=\frac{\pi}{3}
\end{array}
$$

</details>

---

