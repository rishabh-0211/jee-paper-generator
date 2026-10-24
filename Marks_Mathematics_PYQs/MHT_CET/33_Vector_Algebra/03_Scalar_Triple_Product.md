# MHT CET Mathematics - Vector Algebra

## Topic 3: Scalar Triple Product

**Total Questions:** 95

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If three coterminous edges of a parallelopiped are represented by $\vec{a} - \vec{b}, \vec{b} - \vec{c}$ and $\vec{c} - \vec{a}$ then its volume is

**Options:**

- **(A)** $[\vec{a}\ \vec{b}\ \vec{c}]$
- **(B)** $[\vec{a}\ \vec{b}\ \vec{c}]^2$
- **(C)** $2[\vec{a}\ \vec{b}\ \vec{c}]$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0$**

**Detailed Solution:**

The volume of the parallelepiped with coterminous edges $\vec{x}, \vec{y}, \vec{z}$ is given by the scalar triple product $[\vec{x}\ \vec{y}\ \vec{z}]$.

Here, the edges are $\vec{a} - \vec{b}$, $\vec{b} - \vec{c}$, and $\vec{c} - \vec{a}$.

The required volume is $V = [\vec{a} - \vec{b}\ \ \vec{b} - \vec{c}\ \ \vec{c} - \vec{a}]$.

Expanding the scalar triple product:

$V = (\vec{a} - \vec{b}) \cdot ((\vec{b} - \vec{c}) \times (\vec{c} - \vec{a}))$

$V = (\vec{a} - \vec{b}) \cdot (\vec{b} \times \vec{c} - \vec{b} \times \vec{a} - \vec{c} \times \vec{c} + \vec{c} \times \vec{a})$

Since $\vec{c} \times \vec{c} = \vec{0}$ and $-\vec{b} \times \vec{a} = \vec{a} \times \vec{b}$:

$V = (\vec{a} - \vec{b}) \cdot (\vec{b} \times \vec{c} + \vec{a} \times \vec{b} + \vec{c} \times \vec{a})$

$V = \vec{a} \cdot (\vec{b} \times \vec{c}) + \vec{a} \cdot (\vec{a} \times \vec{b}) + \vec{a} \cdot (\vec{c} \times \vec{a}) - \vec{b} \cdot (\vec{b} \times \vec{c}) - \vec{b} \cdot (\vec{a} \times \vec{b}) - \vec{b} \cdot (\vec{c} \times \vec{a})$

Using the property that the scalar triple product is zero if any two vectors are identical:

$V = [\vec{a}\ \vec{b}\ \vec{c}] + 0 + 0 - 0 - 0 - [\vec{b}\ \vec{c}\ \vec{a}]$

Since $[\vec{b}\ \vec{c}\ \vec{a}] = [\vec{a}\ \vec{b}\ \vec{c}]$:

$V = [\vec{a}\ \vec{b}\ \vec{c}] - [\vec{a}\ \vec{b}\ \vec{c}] = 0$

Alternatively, the sum of the three vectors is $(\vec{a} - \vec{b}) + (\vec{b} - \vec{c}) + (\vec{c} - \vec{a}) = \vec{0}$. Since they are linearly dependent, they are coplanar, and the volume of the parallelepiped is $0$.

Answer: $0$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The scalar triple product of the vectors $[2\bar{a} + 3\bar{b} \ \ 3\bar{b} + \bar{c} \ \ \bar{c} + 2\bar{a}]$ is equal to:

**Options:**

- **(A)** $6[\bar{a} \ \ \bar{b} \ \ \bar{c}]$
- **(B)** $12[\bar{a} \ \ \bar{b} \ \ \bar{c}]$
- **(C)** $5[\bar{a} \ \ \bar{b} \ \ \bar{c}]$
- **(D)** $24[\bar{a} \ \ \bar{b} \ \ \bar{c}]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $12[\bar{a} \ \ \bar{b} \ \ \bar{c}]$**

**Detailed Solution:**

The scalar triple product can be evaluated using the determinant of the coefficients of $\bar{a}$, $\bar{b}$, and $\bar{c}$:

$[2\bar{a} + 3\bar{b} \ \ 3\bar{b} + \bar{c} \ \ \bar{c} + 2\bar{a}] = \begin{vmatrix} 2 & 3 & 0 \\ 0 & 3 & 1 \\ 2 & 0 & 1 \end{vmatrix} [\bar{a} \ \ \bar{b} \ \ \bar{c}]$

Expanding the determinant along the first row:

$\Delta = 2(3 - 0) - 3(0 - 2) + 0$

$\Delta = 6 + 6 = 12$

Thus, the scalar triple product is $12[\bar{a} \ \ \bar{b} \ \ \bar{c}]$.

Answer: $12[\bar{a} \ \ \bar{b} \ \ \bar{c}]$

</details>

---

### Q3. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a} = \hat{i} + 2\hat{j} + 2\hat{k}$, $\bar{b} = 2\hat{i} - 2\hat{j} + \hat{k}$ and $\bar{c}$ is a vector projection of $\bar{a}$ on the line of $\bar{b}$, then the value of $[2\bar{a}\ 3\bar{b}\ \sqrt{3}\bar{c}]$ is

**Options:**

- **(A)** $6\sqrt{3}$
- **(B)** $0$
- **(C)** $\sqrt{3}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0$**

**Detailed Solution:**

Given $\bar{a} = \hat{i} + 2\hat{j} + 2\hat{k}$ and $\bar{b} = 2\hat{i} - 2\hat{j} + \hat{k}$.

The vector projection of $\bar{a}$ on $\bar{b}$ is given by $\bar{c} = \left( \dfrac{\bar{a} \cdot \bar{b}}{|\bar{b}|^2} \right) \bar{b}$.

Since $\bar{c}$ is a scalar multiple of $\bar{b}$, the vectors $\bar{b}$ and $\bar{c}$ are collinear.

The scalar triple product of vectors is zero if any two vectors are collinear, hence $[\bar{a}\ \bar{b}\ \bar{c}] = 0$.

Using the properties of the scalar triple product:

$[2\bar{a}\ 3\bar{b}\ \sqrt{3}\bar{c}] = (2)(3)(\sqrt{3}) [\bar{a}\ \bar{b}\ \bar{c}] = 6\sqrt{3} \times 0 = 0$.

Alternatively, calculating the dot product gives $\bar{a} \cdot \bar{b} = (1)(2) + (2)(-2) + (2)(1) = 0$, meaning $\bar{c} = \bar{0}$, which also directly results in the scalar triple product being $0$.

Answer: $0$

</details>

---

### Q4. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the volume of tetrahedron with its coterminous edges $\bar{a}, \bar{b}, \bar{c}$ is $6$ cu. units then the volume of a tetrahedron with coterminous edges $(\bar{a} \times \bar{b}), (\bar{b} \times \bar{c}), (\bar{c} \times \bar{a})$ is

**Options:**

- **(A)** $6$ cu. units.
- **(B)** $36$ cu. units.
- **(C)** $216$ cu. units.
- **(D)** $648$ cu. units.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $216$ cu. units.**

**Detailed Solution:**

The volume of a tetrahedron with coterminous edges $\bar{a}, \bar{b}, \bar{c}$ is given by $V = \dfrac{1}{6} |[\bar{a} \; \bar{b} \; \bar{c}]|$.

Given $V = 6$, we have:

$\dfrac{1}{6} |[\bar{a} \; \bar{b} \; \bar{c}]| = 6 \Rightarrow |[\bar{a} \; \bar{b} \; \bar{c}]| = 36$

The volume of the new tetrahedron with coterminous edges $\bar{a} \times \bar{b}, \bar{b} \times \bar{c}, \bar{c} \times \bar{a}$ is:

$V' = \dfrac{1}{6} |[\bar{a} \times \bar{b} \quad \bar{b} \times \bar{c} \quad \bar{c} \times \bar{a}]|$

Using the standard property of the scalar triple product, we know that:

$[\bar{a} \times \bar{b} \quad \bar{b} \times \bar{c} \quad \bar{c} \times \bar{a}] = [\bar{a} \; \bar{b} \; \bar{c}]^2$

Substituting this into the volume formula:

$V' = \dfrac{1}{6} [\bar{a} \; \bar{b} \; \bar{c}]^2$

$V' = \dfrac{1}{6} (36)^2 = \dfrac{1296}{6} = 216$ cu. units.

Answer: $216$ cu. units.

</details>

---

### Q5. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}, \bar{b}, \bar{c}$ are vectors such that $[\bar{a}\ \bar{b}\ \bar{c}] = 3$, then $[\bar{a} \times \bar{b}\ \ \bar{b} \times \bar{c}\ \ \bar{c} \times \bar{a}] =$

**Options:**

- **(A)** $6$
- **(B)** $9$
- **(C)** $12$
- **(D)** $15$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $9$**

**Detailed Solution:**

Let $\bar{x} = \bar{a} \times \bar{b}$, $\bar{y} = \bar{b} \times \bar{c}$, and $\bar{z} = \bar{c} \times \bar{a}$.

The scalar triple product is given by:

$[\bar{x}\ \bar{y}\ \bar{z}] = \bar{x} \cdot (\bar{y} \times \bar{z})$

First, evaluating the cross product $\bar{y} \times \bar{z}$:

$\bar{y} \times \bar{z} = (\bar{b} \times \bar{c}) \times (\bar{c} \times \bar{a})$

Using the vector triple product expansion $\bar{p} \times (\bar{q} \times \bar{r}) = (\bar{p} \cdot \bar{r})\bar{q} - (\bar{p} \cdot \bar{q})\bar{r}$ with $\bar{p} = \bar{b} \times \bar{c}$, $\bar{q} = \bar{c}$, and $\bar{r} = \bar{a}$:

$\bar{y} \times \bar{z} = ((\bar{b} \times \bar{c}) \cdot \bar{a})\bar{c} - ((\bar{b} \times \bar{c}) \cdot \bar{c})\bar{a}$

Since the scalar triple product with two identical vectors is zero, $(\bar{b} \times \bar{c}) \cdot \bar{c} = 0$. Also, $(\bar{b} \times \bar{c}) \cdot \bar{a} = [\bar{b}\ \bar{c}\ \bar{a}] = [\bar{a}\ \bar{b}\ \bar{c}]$.

$\bar{y} \times \bar{z} = [\bar{a}\ \bar{b}\ \bar{c}]\bar{c}$

Now, substituting this back into the scalar triple product:

$[\bar{x}\ \bar{y}\ \bar{z}] = (\bar{a} \times \bar{b}) \cdot ([\bar{a}\ \bar{b}\ \bar{c}]\bar{c})$

$[\bar{x}\ \bar{y}\ \bar{z}] = [\bar{a}\ \bar{b}\ \bar{c}] ((\bar{a} \times \bar{b}) \cdot \bar{c})$

$[\bar{x}\ \bar{y}\ \bar{z}] = [\bar{a}\ \bar{b}\ \bar{c}] [\bar{a}\ \bar{b}\ \bar{c}] = [\bar{a}\ \bar{b}\ \bar{c}]^2$

Therefore, the standard identity is $[\bar{a} \times \bar{b}\ \ \bar{b} \times \bar{c}\ \ \bar{c} \times \bar{a}] = [\bar{a}\ \bar{b}\ \bar{c}]^2$.

Given $[\bar{a}\ \bar{b}\ \bar{c}] = 3$, we get:

$[\bar{a} \times \bar{b}\ \ \bar{b} \times \bar{c}\ \ \bar{c} \times \bar{a}] = 3^2 = 9$

Answer: $9$

</details>

---

### Q6. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\vec{a}, \vec{b}, \vec{c}$ represent three concurrent edges of a rectangular parallelopiped whose lengths are $5, 2$ and $3$ units respectively, then $(\vec{a} + \vec{b} + \vec{c}) \cdot (\vec{a} \times \vec{b} + \vec{b} \times \vec{c} + \vec{c} \times \vec{a}) = $

**Options:**

- **(A)** $10$
- **(B)** $90$
- **(C)** $60$
- **(D)** $30$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $90$**

**Detailed Solution:**

Expanding the given expression:

$(\vec{a} + \vec{b} + \vec{c}) \cdot (\vec{a} \times \vec{b} + \vec{b} \times \vec{c} + \vec{c} \times \vec{a})$

$= \vec{a} \cdot (\vec{a} \times \vec{b}) + \vec{a} \cdot (\vec{b} \times \vec{c}) + \vec{a} \cdot (\vec{c} \times \vec{a}) + \vec{b} \cdot (\vec{a} \times \vec{b}) + \vec{b} \cdot (\vec{b} \times \vec{c}) + \vec{b} \cdot (\vec{c} \times \vec{a}) + \vec{c} \cdot (\vec{a} \times \vec{b}) + \vec{c} \cdot (\vec{b} \times \vec{c}) + \vec{c} \cdot (\vec{c} \times \vec{a})$

Since the scalar triple product is zero when any two vectors are identical, the expression simplifies to:

$= \vec{a} \cdot (\vec{b} \times \vec{c}) + \vec{b} \cdot (\vec{c} \times \vec{a}) + \vec{c} \cdot (\vec{a} \times \vec{b})$

$= [\vec{a} \vec{b} \vec{c}] + [\vec{b} \vec{c} \vec{a}] + [\vec{c} \vec{a} \vec{b}]$

Using the cyclic property of the scalar triple product, $[\vec{a} \vec{b} \vec{c}] = [\vec{b} \vec{c} \vec{a}] = [\vec{c} \vec{a} \vec{b}]$, the sum becomes:

$= 3 [\vec{a} \vec{b} \vec{c}]$

Since $\vec{a}, \vec{b}, \vec{c}$ represent the concurrent edges of a rectangular parallelepiped, they are mutually perpendicular. The scalar triple product $[\vec{a} \vec{b} \vec{c}]$ represents the volume of the parallelepiped.

$[\vec{a} \vec{b} \vec{c}] = |\vec{a}| |\vec{b}| |\vec{c}| = 5 \times 2 \times 3 = 30$

Substituting this value back, we get:

$3 [\vec{a} \vec{b} \vec{c}] = 3 \times 30 = 90$

Answer: $90$

</details>

---

### Q7. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the volume of a tetrahedron with coterminous edges $\vec{a}, \vec{b}$ and $\vec{c}$, (where $\vec{a}$ is a unit vector) is $13$ cubic units and the angle between $\vec{a}$ and $\vec{b} \times \vec{c}$ is $\dfrac{\pi}{3}$, then $|\vec{b} \times \vec{c}|$ is

**Options:**

- **(A)** $156$
- **(B)** $78$
- **(C)** $39$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $156$**

**Detailed Solution:**

The volume of a tetrahedron with coterminous edges $\vec{a}$, $\vec{b}$, and $\vec{c}$ is given by $V = \dfrac{1}{6} |[\vec{a}, \vec{b}, \vec{c}]|$.

We know that the scalar triple product is $[\vec{a}, \vec{b}, \vec{c}] = \vec{a} \cdot (\vec{b} \times \vec{c})$.

Using the definition of the dot product, we have:

$\vec{a} \cdot (\vec{b} \times \vec{c}) = |\vec{a}| |\vec{b} \times \vec{c}| \cos \theta$

where $\theta$ is the angle between $\vec{a}$ and $\vec{b} \times \vec{c}$.

Given that $V = 13$, $|\vec{a}| = 1$ (since $\vec{a}$ is a unit vector), and $\theta = \dfrac{\pi}{3}$, we can substitute these values into the volume formula:

$13 = \dfrac{1}{6} \left| |\vec{a}| |\vec{b} \times \vec{c}| \cos \left( \dfrac{\pi}{3} \right) \right|$

$13 = \dfrac{1}{6} \times 1 \times |\vec{b} \times \vec{c}| \times \dfrac{1}{2}$

$13 = \dfrac{1}{12} |\vec{b} \times \vec{c}|$

$|\vec{b} \times \vec{c}| = 13 \times 12 = 156$

Answer: $156$

</details>

---

### Q8. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}, \bar{b}$ and $\bar{c}$ are three non-coplanar vectors and $\lambda$ is a real number such that $[\lambda(\bar{a}+\bar{b})\;\;\lambda^2\bar{b}\;\;\lambda\bar{c}]=[\bar{a}\;\;\bar{b}+\bar{c}\;\;\bar{b}]$, then there is (are) ...

**Options:**

- **(A)** exactly three values of $\lambda$
- **(B)** exactly two values of $\lambda$
- **(C)** exactly one value of $\lambda$
- **(D)** no value of $\lambda$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) no value of $\lambda$**

**Detailed Solution:**

The left hand side of the given equation is:

$[\lambda(\bar{a}+\bar{b})\;\;\lambda^2\bar{b}\;\;\lambda\bar{c}] = \lambda \cdot \lambda^2 \cdot \lambda [\bar{a}+\bar{b}\;\;\bar{b}\;\;\bar{c}]$

$= \lambda^4 ([\bar{a}\;\;\bar{b}\;\;\bar{c}] + [\bar{b}\;\;\bar{b}\;\;\bar{c}])$

$= \lambda^4 ([\bar{a}\;\;\bar{b}\;\;\bar{c}] + 0) = \lambda^4 [\bar{a}\;\;\bar{b}\;\;\bar{c}]$

The right hand side of the given equation is:

$[\bar{a}\;\;\bar{b}+\bar{c}\;\;\bar{b}] = [\bar{a}\;\;\bar{b}\;\;\bar{b}] + [\bar{a}\;\;\bar{c}\;\;\bar{b}]$

$= 0 - [\bar{a}\;\;\bar{b}\;\;\bar{c}] = -[\bar{a}\;\;\bar{b}\;\;\bar{c}]$

Equating both sides, we get:

$\lambda^4 [\bar{a}\;\;\bar{b}\;\;\bar{c}] = -[\bar{a}\;\;\bar{b}\;\;\bar{c}]$

Since $\bar{a}, \bar{b}, \bar{c}$ are non-coplanar vectors, $[\bar{a}\;\;\bar{b}\;\;\bar{c}] \neq 0$. Dividing both sides by $[\bar{a}\;\;\bar{b}\;\;\bar{c}]$, we obtain:

$\lambda^4 = -1$

Since $\lambda$ is a real number, $\lambda^4 \ge 0$. Thus, $\lambda^4 = -1$ has no real solution.

Therefore, there is no value of $\lambda$.

Answer: no value of $\lambda$

</details>

---

### Q9. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{u} = \hat{i} + 2\hat{j} - 2\hat{k}, \vec{v} = 2\hat{i} + \hat{k}$ and $\vec{w}$ is unit vector then the maximum value of scalar triple product $[\vec{u}\ \vec{v}\ \vec{w}]$ is

**Options:**

- **(A)** $-3\sqrt{5}$
- **(B)** $0$
- **(C)** $3\sqrt{5}$
- **(D)** $\sqrt{54}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3\sqrt{5}$**

**Detailed Solution:**

The scalar triple product is given by $[\vec{u}\ \vec{v}\ \vec{w}] = (\vec{u} \times \vec{v}) \cdot \vec{w}$.

First, we find the cross product $\vec{u} \times \vec{v}$:

$\vec{u} \times \vec{v} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & -2 \\ 2 & 0 & 1 \end{vmatrix}$

$\vec{u} \times \vec{v} = \hat{i}(2 - 0) - \hat{j}(1 - (-4)) + \hat{k}(0 - 4)$

$\vec{u} \times \vec{v} = 2\hat{i} - 5\hat{j} - 4\hat{k}$

The magnitude of this vector is:

$|\vec{u} \times \vec{v}| = \sqrt{2^2 + (-5)^2 + (-4)^2} = \sqrt{4 + 25 + 16} = \sqrt{45} = 3\sqrt{5}$

The dot product $(\vec{u} \times \vec{v}) \cdot \vec{w}$ is maximized when the unit vector $\vec{w}$ is in the same direction as $\vec{u} \times \vec{v}$.

Maximum value $= |\vec{u} \times \vec{v}| |\vec{w}| \cos(0^{\circ})$

Since $|\vec{w}| = 1$, the maximum value is $3\sqrt{5} \times 1 \times 1 = 3\sqrt{5}$.

Answer: $3\sqrt{5}$

</details>

---

### Q10. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The volume of the parallelopiped whose coterminous edges are $2\hat{i} + \hat{j} - \hat{k}, 3\hat{i} - \hat{j} - \hat{k}, \hat{j} + 3\hat{k}$ is

**Options:**

- **(A)** $16$ cu. units
- **(B)** $6$ cu. units
- **(C)** $2$ cu. units
- **(D)** $12$ cu. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $16$ cu. units**

**Detailed Solution:**

Let the coterminous edges be $\vec{a} = 2\hat{i} + \hat{j} - \hat{k}$, $\vec{b} = 3\hat{i} - \hat{j} - \hat{k}$, and $\vec{c} = \hat{j} + 3\hat{k}$.

The volume of the parallelopiped is given by the absolute value of the scalar triple product $[\vec{a} \ \vec{b} \ \vec{c}]$.

$[\vec{a} \ \vec{b} \ \vec{c}] = \begin{vmatrix} 2 & 1 & -1 \\ 3 & -1 & -1 \\ 0 & 1 & 3 \end{vmatrix}$

Expanding the determinant along the first row:

$[\vec{a} \ \vec{b} \ \vec{c}] = 2(-3 + 1) - 1(9 - 0) - 1(3 - 0)$

$[\vec{a} \ \vec{b} \ \vec{c}] = -4 - 9 - 3 = -16$

$V = |-16| = 16$ cu. units.

Answer: $16$ cu. units

</details>

---

### Q11. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The volume of the tetrahedron whose vertices are A$(-1, 2, 3)$, B$(3, -2, 1)$, C$(p, 1, 3)$, D$(-1, -2, 4)$ is $\dfrac{16}{3}$ cubic units then the value of p is

**Options:**

- **(A)** $\dfrac{-10}{3}$
- **(B)** $5$
- **(C)** $8$
- **(D)** $10$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{-10}{3}$**

**Detailed Solution:**

The volume of a tetrahedron with vertices $A, B, C, D$ is given by $V = \dfrac{1}{6} |[\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}]|$.

The vectors representing the edges from $A$ are:
$\overrightarrow{AB} = (3 - (-1))\hat{i} + (-2 - 2)\hat{j} + (1 - 3)\hat{k} = 4\hat{i} - 4\hat{j} - 2\hat{k}$
$\overrightarrow{AC} = (p - (-1))\hat{i} + (1 - 2)\hat{j} + (3 - 3)\hat{k} = (p+1)\hat{i} - \hat{j}$
$\overrightarrow{AD} = (-1 - (-1))\hat{i} + (-2 - 2)\hat{j} + (4 - 3)\hat{k} = -4\hat{j} + \hat{k}$

The scalar triple product is:
$[\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}] = \begin{vmatrix} 4 & -4 & -2 \\ p+1 & -1 & 0 \\ 0 & -4 & 1 \end{vmatrix}$

Expanding the determinant:
$= 4(-1 - 0) + 4(p+1 - 0) - 2(-4(p+1) - 0)$
$= -4 + 4p + 4 + 8p + 8$
$= 12p + 8$

Given $V = \dfrac{16}{3}$, we have:
$\dfrac{1}{6} |12p + 8| = \dfrac{16}{3}$

$|12p + 8| = 32$

$12p + 8 = \pm 32$

Taking the positive sign:
$12p + 8 = 32 \Rightarrow 12p = 24 \Rightarrow p = 2$

Taking the negative sign:
$12p + 8 = -32 \Rightarrow 12p = -40 \Rightarrow p = \dfrac{-10}{3}$

Since $p = \dfrac{-10}{3}$ is present in the options, it is the required value.

Answer: $\dfrac{-10}{3}$

</details>

---

### Q12. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}$ and $\bar{b}$ are unit vectors perpendicular to each other, then $\left[\bar{a} + (\bar{a} \times \bar{b})\quad \bar{b} + (\bar{a} \times \bar{b})\quad (\bar{a} \times \bar{b})\right] = \cdots$

**Options:**

- **(A)** $-1$
- **(B)** $1$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

Let $\bar{c} = \bar{a} \times \bar{b}$.

The given scalar triple product is $[\bar{a} + \bar{c} \quad \bar{b} + \bar{c} \quad \bar{c}]$.

Using the properties of the scalar triple product:

$[\bar{a} + \bar{c} \quad \bar{b} + \bar{c} \quad \bar{c}] = (\bar{a} + \bar{c}) \cdot ((\bar{b} + \bar{c}) \times \bar{c})$

$= (\bar{a} + \bar{c}) \cdot (\bar{b} \times \bar{c} + \bar{c} \times \bar{c})$

Since $\bar{c} \times \bar{c} = \bar{0}$, we get:

$= (\bar{a} + \bar{c}) \cdot (\bar{b} \times \bar{c})$

$= \bar{a} \cdot (\bar{b} \times \bar{c}) + \bar{c} \cdot (\bar{b} \times \bar{c})$

Since the scalar triple product with two identical vectors is zero, $\bar{c} \cdot (\bar{b} \times \bar{c}) = 0$.

$= \bar{a} \cdot (\bar{b} \times \bar{c}) = [\bar{a} \quad \bar{b} \quad \bar{c}]$

Substituting $\bar{c} = \bar{a} \times \bar{b}$ back into the expression:

$[\bar{a} \quad \bar{b} \quad \bar{a} \times \bar{b}] = (\bar{a} \times \bar{b}) \cdot (\bar{a} \times \bar{b}) = |\bar{a} \times \bar{b}|^2$

Since $\bar{a}$ and $\bar{b}$ are unit vectors perpendicular to each other, $|\bar{a}| = 1$, $|\bar{b}| = 1$, and the angle between them is $90^{\circ}$.

$|\bar{a} \times \bar{b}| = |\bar{a}| |\bar{b}| \sin 90^{\circ} = 1 \times 1 \times 1 = 1$

Therefore, $|\bar{a} \times \bar{b}|^2 = 1$.

</details>

---

### Q13. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The maximum volume of a parallelopiped (in cubic units) with vectors $(2a\hat{i} + \hat{k}), (a\hat{j} - a\hat{k})$, and $(3\hat{i} + a\hat{j})$, where $a \in [0, 1]$, as its coterminous edges is...

**Options:**

- **(A)** $\dfrac{1}{\sqrt{2}}$
- **(B)** $\sqrt{2}$
- **(C)** $2$
- **(D)** $2\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{2}$**

**Detailed Solution:**

The volume $V$ of the parallelopiped is given by the absolute value of the scalar triple product of its coterminous edges.

$V = \left| \begin{vmatrix} 2a & 0 & 1 \\ 0 & a & -a \\ 3 & a & 0 \end{vmatrix} \right|$

Expanding the determinant along the first row:

$V = |2a(0 - (-a^2)) - 0 + 1(0 - 3a)|$

$V = |2a^3 - 3a|$

Since $a \in [0, 1]$, $2a^3 \le 3a$, so $V(a) = 3a - 2a^3$.

To find the maximum volume, we differentiate $V(a)$ with respect to $a$ and equate it to zero:

$V'(a) = 3 - 6a^2 = 0$

$a^2 = \dfrac{1}{2} \Rightarrow a = \dfrac{1}{\sqrt{2}}$ (since $a \in [0, 1]$)

To verify it is a maximum, we check the second derivative:

$V''(a) = -12a$

At $a = \dfrac{1}{\sqrt{2}}$, $V''(a) < 0$, which confirms a maximum.

Substituting $a = \dfrac{1}{\sqrt{2}}$ into $V(a)$:

$V_{max} = 3\left(\dfrac{1}{\sqrt{2}}\right) - 2\left(\dfrac{1}{\sqrt{2}}\right)^3$

$V_{max} = \dfrac{3}{\sqrt{2}} - \dfrac{2}{2\sqrt{2}} = \dfrac{3}{\sqrt{2}} - \dfrac{1}{\sqrt{2}} = \dfrac{2}{\sqrt{2}} = \sqrt{2}$

Answer: $\sqrt{2}$

</details>

---

### Q14. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $x$ so that the volume of the parallelopiped formed by the vectors $\hat{i} + x\hat{j} + \hat{k}$, $\hat{j} + x\hat{k}$ and $x\hat{i} + \hat{k}$ is minimum, is

**Options:**

- **(A)** $-3$
- **(B)** $3$
- **(C)** $\dfrac{1}{\sqrt{3}}$
- **(D)** $\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{\sqrt{3}}$**

**Detailed Solution:**

The volume of the parallelopiped formed by the vectors $\vec{a}$, $\vec{b}$, and $\vec{c}$ is given by the absolute value of their scalar triple product, $V = |[\vec{a}, \vec{b}, \vec{c}]|$.

Given vectors:
$\vec{a} = \hat{i} + x\hat{j} + \hat{k}$
$\vec{b} = 0\hat{i} + \hat{j} + x\hat{k}$
$\vec{c} = x\hat{i} + 0\hat{j} + \hat{k}$

Calculating the scalar triple product:
$[\vec{a}, \vec{b}, \vec{c}] = \begin{vmatrix} 1 & x & 1 \\ 0 & 1 & x \\ x & 0 & 1 \end{vmatrix}$

Expanding the determinant along the first row:
$= 1(1 \times 1 - x \times 0) - x(0 \times 1 - x \times x) + 1(0 \times 0 - 1 \times x)$
$= 1(1) - x(-x^2) + 1(-x)$
$= x^3 - x + 1$

So, the volume is $V = |x^3 - x + 1|$.

Let $f(x) = x^3 - x + 1$. To find the critical points for minimum or maximum volume, we set the first derivative to zero:
$f'(x) = 3x^2 - 1 = 0$
$3x^2 = 1 \Rightarrow x = \pm \dfrac{1}{\sqrt{3}}$

Now, checking the second derivative to confirm the minimum:
$f''(x) = 6x$

At $x = \dfrac{1}{\sqrt{3}}$:
$f''\left(\dfrac{1}{\sqrt{3}}\right) = \dfrac{6}{\sqrt{3}} > 0$
Since the second derivative is positive, $x = \dfrac{1}{\sqrt{3}}$ is a point of local minimum.

At $x = -\dfrac{1}{\sqrt{3}}$:
$f''\left(-\dfrac{1}{\sqrt{3}}\right) = -\dfrac{6}{\sqrt{3}} < 0$
Since the second derivative is negative, $x = -\dfrac{1}{\sqrt{3}}$ is a point of local maximum.

Therefore, the volume of the parallelopiped is minimum when $x = \dfrac{1}{\sqrt{3}}$.

Answer: $\dfrac{1}{\sqrt{3}}$

</details>

---

### Q15. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all real values of $\lambda$ for which the vectors $\vec{a} = \lambda\hat{i} + \hat{j} + \hat{k}$, $\vec{b} = \hat{i} + \lambda\hat{j} + 2\hat{k}$, $\vec{c} = 2\hat{i} + 3\hat{j} + \lambda\hat{k}$ are coplanar is...

**Options:**

- **(A)** $9$
- **(B)** $7$
- **(C)** $0$
- **(D)** cant determine

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0$**

**Detailed Solution:**

For the vectors $\vec{a}$, $\vec{b}$, and $\vec{c}$ to be coplanar, their scalar triple product must be zero.

$\begin{vmatrix} \lambda & 1 & 1 \\ 1 & \lambda & 2 \\ 2 & 3 & \lambda \end{vmatrix} = 0$

Expanding the determinant:

$\lambda(\lambda^2 - 6) - 1(\lambda - 4) + 1(3 - 2\lambda) = 0$

$\lambda^3 - 6\lambda - \lambda + 4 + 3 - 2\lambda = 0$

$\lambda^3 - 9\lambda + 7 = 0$

Let $f(\lambda) = \lambda^3 - 9\lambda + 7$.

$f'(\lambda) = 3\lambda^2 - 9 = 0 \Rightarrow \lambda = \pm \sqrt{3}$

$f(\sqrt{3}) = 7 - 6\sqrt{3} < 0$ and $f(-\sqrt{3}) = 7 + 6\sqrt{3} > 0$

Since the local maximum is positive and the local minimum is negative, the cubic equation has three distinct real roots.

The sum of the roots of the cubic equation $A\lambda^3 + B\lambda^2 + C\lambda + D = 0$ is given by $-\dfrac{B}{A}$.

Here, the coefficient of $\lambda^2$ is $0$.

Sum of all real values of $\lambda = -\dfrac{0}{1} = 0$.

Answer: $0$

</details>

---

### Q16. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of the plane passing through the points having position vectors $(\bar{a} + \bar{b}), (\bar{b} + \bar{c})$ and $(\bar{a} + \bar{c})$ is $\ldots$

**Options:**

- **(A)** $\bar{r} \cdot (\bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{c} \times \bar{a}) = [\bar{a}\ \bar{b}\ \bar{c}]$
- **(B)** $\bar{r} \cdot (\bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{c} \times \bar{a}) = 2[\bar{a}\ \bar{b}\ \bar{c}]$
- **(C)** $\bar{r} \cdot (\bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{a} \times \bar{c}) = [\bar{a}\ \bar{b}\ \bar{c}]$
- **(D)** $\bar{r} \cdot (\bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{a} \times \bar{c}) = 2[\bar{a}\ \bar{b}\ \bar{c}]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\bar{r} \cdot (\bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{c} \times \bar{a}) = 2[\bar{a}\ \bar{b}\ \bar{c}]$**

**Detailed Solution:**

Let the given points be $A, B, C$ with position vectors $\bar{A} = \bar{a} + \bar{b}$, $\bar{B} = \bar{b} + \bar{c}$, and $\bar{C} = \bar{a} + \bar{c}$.

Two vectors lying on the plane are:
$\bar{B} - \bar{A} = (\bar{b} + \bar{c}) - (\bar{a} + \bar{b}) = \bar{c} - \bar{a}$
$\bar{C} - \bar{A} = (\bar{a} + \bar{c}) - (\bar{a} + \bar{b}) = \bar{c} - \bar{b}$

A normal vector to the plane is given by the cross product of these two vectors:
$\bar{n} = (\bar{B} - \bar{A}) \times (\bar{C} - \bar{A})$
$\bar{n} = (\bar{c} - \bar{a}) \times (\bar{c} - \bar{b})$
$\bar{n} = \bar{c} \times \bar{c} - \bar{c} \times \bar{b} - \bar{a} \times \bar{c} + \bar{a} \times \bar{b}$

Since $\bar{c} \times \bar{c} = \bar{0}$, $-\bar{c} \times \bar{b} = \bar{b} \times \bar{c}$, and $-\bar{a} \times \bar{c} = \bar{c} \times \bar{a}$, we get:
$\bar{n} = \bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{c} \times \bar{a}$

The equation of the plane passing through $\bar{A}$ with normal $\bar{n}$ is:
$(\bar{r} - \bar{A}) \cdot \bar{n} = 0$
$\bar{r} \cdot \bar{n} = \bar{A} \cdot \bar{n}$

Substituting $\bar{A}$ and $\bar{n}$ into the right-hand side:
$\bar{A} \cdot \bar{n} = (\bar{a} + \bar{b}) \cdot (\bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{c} \times \bar{a})$

Expanding the dot product and using the property that the scalar triple product is zero if any two vectors are equal:
$\bar{A} \cdot \bar{n} = \bar{a} \cdot (\bar{b} \times \bar{c}) + \bar{b} \cdot (\bar{c} \times \bar{a})$
$\bar{A} \cdot \bar{n} = [\bar{a}\ \bar{b}\ \bar{c}] + [\bar{b}\ \bar{c}\ \bar{a}]$

Since $[\bar{b}\ \bar{c}\ \bar{a}] = [\bar{a}\ \bar{b}\ \bar{c}]$ (cyclic permutation), we have:
$\bar{A} \cdot \bar{n} = 2[\bar{a}\ \bar{b}\ \bar{c}]$

Therefore, the equation of the plane is:
$\bar{r} \cdot (\bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{c} \times \bar{a}) = 2[\bar{a}\ \bar{b}\ \bar{c}]$

Answer: $\bar{r} \cdot (\bar{a} \times \bar{b} + \bar{b} \times \bar{c} + \bar{c} \times \bar{a}) = 2[\bar{a}\ \bar{b}\ \bar{c}]$

</details>

---

### Q17. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the volume of the tetrahedron whose coterminous edges are given by the vectors $\bar{a} = -2\hat{i} + 3\hat{j} - 3\hat{k}$, $\bar{b} = 4\hat{i} + 5\hat{j} + (\lambda - 10)\hat{k}$, $\bar{c} = 6\hat{i} + 2\hat{j} - 3\hat{k}$ is 11 cubic units, then the sum of the possible values of $\lambda$ is $\ldots$

**Options:**

- **(A)** $7$
- **(B)** $8$
- **(C)** $1$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $8$**

**Detailed Solution:**

The volume of a tetrahedron with coterminous edges $\bar{a}$, $\bar{b}$, $\bar{c}$ is given by $V = \dfrac{1}{6} |[\bar{a}, \bar{b}, \bar{c}]|$.

Given $V = 11$, we have $|[\bar{a}, \bar{b}, \bar{c}]| = 66$.

Calculating the scalar triple product:

$[\bar{a}, \bar{b}, \bar{c}] = \begin{vmatrix} -2 & 3 & -3 \\ 4 & 5 & \lambda - 10 \\ 6 & 2 & -3 \end{vmatrix}$

$= -2(-15 - 2(\lambda - 10)) - 3(-12 - 6(\lambda - 10)) - 3(8 - 30)$

$= -2(5 - 2\lambda) - 3(48 - 6\lambda) - 3(-22)$

$= -10 + 4\lambda - 144 + 18\lambda + 66$

$= 22\lambda - 88$

Substituting this into the volume equation:

$|22\lambda - 88| = 66$

$22|\lambda - 4| = 66$

$|\lambda - 4| = 3$

This gives $\lambda - 4 = 3 \Rightarrow \lambda = 7$ and $\lambda - 4 = -3 \Rightarrow \lambda = 1$.

The possible values of $\lambda$ are $7$ and $1$.

The sum of the possible values of $\lambda$ is $7 + 1 = 8$.

Answer: $8$

</details>

---

### Q18. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a} = \hat{i} - \hat{k}$, $\bar{b} = x\hat{i} + \hat{j} + (1-x)\hat{k}$ and $\bar{c} = y\hat{i} + x\hat{j} + (1+x-y)\hat{k}$ then $[\bar{a}\ \bar{b}\ \bar{c}]$ depends on

**Options:**

- **(A)** only x
- **(B)** neither x nor y
- **(C)** either x or y
- **(D)** only y

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) neither x nor y**

**Detailed Solution:**

The scalar triple product $[\bar{a}\ \bar{b}\ \bar{c}]$ is given by the determinant of the components of the vectors.

$[\bar{a}\ \bar{b}\ \bar{c}] = \begin{vmatrix} 1 & 0 & -1 \\ x & 1 & 1-x \\ y & x & 1+x-y \end{vmatrix}$

Applying the column operation $C_3 \rightarrow C_3 + C_1$:

$[\bar{a}\ \bar{b}\ \bar{c}] = \begin{vmatrix} 1 & 0 & 0 \\ x & 1 & 1 \\ y & x & 1+x \end{vmatrix}$

Expanding the determinant along the first row:

$[\bar{a}\ \bar{b}\ \bar{c}] = 1 \cdot (1(1+x) - 1(x))$

$[\bar{a}\ \bar{b}\ \bar{c}] = 1 + x - x = 1$

Thus, the scalar triple product is a constant and is independent of both $x$ and $y$.

Answer: neither x nor y

</details>

---

### Q19. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a} = 2\hat{i} - 3\hat{j} + \hat{k},\ \vec{b} = 3\hat{i} + 2\hat{j} + 2\hat{k},\ \vec{c} = 4\hat{i} - 3\hat{j} + \hat{k}$, then the vectors $\vec{a},\ \vec{b},\ \vec{c}$ are

**Options:**

- **(A)** Linearly dependent
- **(B)** Orthogonal
- **(C)** Linearly independent
- **(D)** Coplanar

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Linearly independent**

**Detailed Solution:**

The vectors are $\vec{a} = 2\hat{i} - 3\hat{j} + \hat{k}$, $\vec{b} = 3\hat{i} + 2\hat{j} + 2\hat{k}$, and $\vec{c} = 4\hat{i} - 3\hat{j} + \hat{k}$.

To check for linear independence, we evaluate the scalar triple product $[\vec{a}\ \vec{b}\ \vec{c}]$ which is given by the determinant of their components:

$[\vec{a}\ \vec{b}\ \vec{c}] = \begin{vmatrix} 2 & -3 & 1 \\ 3 & 2 & 2 \\ 4 & -3 & 1 \end{vmatrix}$

Applying the row operation $R_3 \rightarrow R_3 - R_1$:

$[\vec{a}\ \vec{b}\ \vec{c}] = \begin{vmatrix} 2 & -3 & 1 \\ 3 & 2 & 2 \\ 2 & 0 & 0 \end{vmatrix}$

Expanding along the third row:

$[\vec{a}\ \vec{b}\ \vec{c}] = 2((-3)(2) - (1)(2)) = 2(-6 - 2) = -16$

Since $[\vec{a}\ \vec{b}\ \vec{c}] \neq 0$, the vectors are non-coplanar and hence linearly independent.

Answer: Linearly independent

</details>

---

### Q20. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a} = (a_1\hat{i} + a_2\hat{j} + a_3\hat{k}),\ \bar{b} = (b_1\hat{i} + b_2\hat{j} + b_3\hat{k}),\ \bar{c} = (c_1\hat{i} + c_2\hat{j} + c_3\hat{k})$ be three non-zero vectors such that $\bar{a}$ is a unit vector perpendicular to both $\bar{b}$ and $\bar{c}$. If the angle between $\bar{b}$ and $\bar{c}$ is $\dfrac{\pi}{3}$ then $\begin{vmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix}^2 = $

**Options:**

- **(A)** $\dfrac{3}{4}|\bar{b}|^2|\bar{c}|^2$
- **(B)** $1$
- **(C)** $0$
- **(D)** $\dfrac{1}{4}|\bar{b}|^2|\bar{c}|^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{3}{4}|\bar{b}|^2|\bar{c}|^2$**

**Detailed Solution:**

The given determinant represents the scalar triple product of the vectors $\bar{a}$, $\bar{b}$, and $\bar{c}$.

$\begin{vmatrix} a_1 & a_2 & a_3 \\\\ b_1 & b_2 & b_3 \\\\ c_1 & c_2 & c_3 \end{vmatrix} = [\bar{a}\ \bar{b}\ \bar{c}] = \bar{a} \cdot (\bar{b} \times \bar{c})$

Since $\bar{a}$ is perpendicular to both $\bar{b}$ and $\bar{c}$, the vector $\bar{a}$ is collinear with $\bar{b} \times \bar{c}$.

$[\bar{a}\ \bar{b}\ \bar{c}] = \pm |\bar{a}| |\bar{b} \times \bar{c}|$

Given that $\bar{a}$ is a unit vector, $|\bar{a}| = 1$.

$[\bar{a}\ \bar{b}\ \bar{c}]^2 = |\bar{b} \times \bar{c}|^2$

The angle between $\bar{b}$ and $\bar{c}$ is $\dfrac{\pi}{3}$.

$|\bar{b} \times \bar{c}|^2 = \left(|\bar{b}| |\bar{c}| \sin\left(\dfrac{\pi}{3}\right)\right)^2$

$|\bar{b} \times \bar{c}|^2 = |\bar{b}|^2 |\bar{c}|^2 \left(\dfrac{\sqrt{3}}{2}\right)^2 = \dfrac{3}{4}|\bar{b}|^2|\bar{c}|^2$

Answer: $\dfrac{3}{4}|\bar{b}|^2|\bar{c}|^2$

</details>

---

### Q21. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a} = 2\hat{i} + \hat{j} - \hat{k}$, $\bar{b} = \hat{i} + 3\hat{k}$ and $\bar{c}$ is a unit vector, then the maximum value of the scalar triple product $[\bar{a}\ \bar{b}\ \bar{c}]$ is

**Options:**

- **(A)** $\sqrt{10} + \sqrt{6}$
- **(B)** $\sqrt{10}$
- **(C)** $\sqrt{6}$
- **(D)** $\sqrt{59}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{59}$**

**Detailed Solution:**

The scalar triple product is given by $[\bar{a}\ \bar{b}\ \bar{c}] = (\bar{a} \times \bar{b}) \cdot \bar{c}$.

First, calculating the cross product $\bar{a} \times \bar{b}$:

$\bar{a} \times \bar{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & -1 \\ 1 & 0 & 3 \end{vmatrix}$

$= \hat{i}(3 - 0) - \hat{j}(6 - (-1)) + \hat{k}(0 - 1)$

$= 3\hat{i} - 7\hat{j} - \hat{k}$

The scalar triple product becomes $(3\hat{i} - 7\hat{j} - \hat{k}) \cdot \bar{c}$.

Using the dot product formula, $(\bar{a} \times \bar{b}) \cdot \bar{c} = |\bar{a} \times \bar{b}| |\bar{c}| \cos \theta$, where $\theta$ is the angle between $\bar{a} \times \bar{b}$ and $\bar{c}$.

Since $\bar{c}$ is a unit vector, $|\bar{c}| = 1$. The maximum value occurs when $\cos \theta = 1$ (i.e., when $\bar{c}$ is parallel to $\bar{a} \times \bar{b}$).

Maximum value $= |\bar{a} \times \bar{b}|$

$= \sqrt{3^2 + (-7)^2 + (-1)^2}$

$= \sqrt{9 + 49 + 1} = \sqrt{59}$

Answer: $\sqrt{59}$

</details>

---

### Q22. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The volume of a parallelopiped with coterminous edges $\bar{a}, \bar{b}, \bar{c}$ is 3 cubic units. The volume (in cubic units) of a tetrahedron with coterminous edges $(\bar{a} \times \bar{b}), (\bar{a} \times 2\bar{c}), (\bar{b} \times 2\bar{c})$ is...

**Options:**

- **(A)** $6$
- **(B)** $12$
- **(C)** $24$
- **(D)** $36$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6$**

**Detailed Solution:**

The volume of the parallelopiped with coterminous edges $\bar{a}, \bar{b}, \bar{c}$ is given by $|[\bar{a} \bar{b} \bar{c}]| = 3$.

The volume of a tetrahedron with coterminous edges $\bar{x}, \bar{y}, \bar{z}$ is $V = \dfrac{1}{6} |[\bar{x} \bar{y} \bar{z}]|$.

Here, the edges are $\bar{x} = \bar{a} \times \bar{b}$, $\bar{y} = 2(\bar{a} \times \bar{c})$, and $\bar{z} = 2(\bar{b} \times \bar{c})$.

Evaluating the scalar triple product of these edges:

$[\bar{x} \bar{y} \bar{z}] = [\bar{a} \times \bar{b} \quad 2(\bar{a} \times \bar{c}) \quad 2(\bar{b} \times \bar{c})] = 4 [\bar{a} \times \bar{b} \quad \bar{a} \times \bar{c} \quad \bar{b} \times \bar{c}]$

Using the scalar triple product expansion:

$[\bar{a} \times \bar{b} \quad \bar{a} \times \bar{c} \quad \bar{b} \times \bar{c}] = (\bar{a} \times \bar{b}) \cdot ((\bar{a} \times \bar{c}) \times (\bar{b} \times \bar{c}))$

Applying the vector triple product formula:

$(\bar{a} \times \bar{c}) \times (\bar{b} \times \bar{c}) = [\bar{a} \bar{c} \bar{c}] \bar{b} - [\bar{a} \bar{c} \bar{b}] \bar{c}$

Since $[\bar{a} \bar{c} \bar{c}] = 0$ and $[\bar{a} \bar{c} \bar{b}] = -[\bar{a} \bar{b} \bar{c}]$, we get:

$(\bar{a} \times \bar{c}) \times (\bar{b} \times \bar{c}) = [\bar{a} \bar{b} \bar{c}] \bar{c}$

Substituting this back into the scalar triple product:

$(\bar{a} \times \bar{b}) \cdot ([\bar{a} \bar{b} \bar{c}] \bar{c}) = [\bar{a} \bar{b} \bar{c}] ((\bar{a} \times \bar{b}) \cdot \bar{c}) = [\bar{a} \bar{b} \bar{c}]^2$

Therefore, the scalar triple product of the new edges is:

$[\bar{x} \bar{y} \bar{z}] = 4 [\bar{a} \bar{b} \bar{c}]^2$

Since $|[\bar{a} \bar{b} \bar{c}]| = 3$, we have $[\bar{a} \bar{b} \bar{c}]^2 = 9$.

$[\bar{x} \bar{y} \bar{z}] = 4 \times 9 = 36$

The volume of the tetrahedron is $V = \dfrac{1}{6} \times 36 = 6$ cubic units.

Answer: $6$

</details>

---

### Q23. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The volume of a tetrahedron with vertices $5\hat{i} - \hat{j} + \hat{k}, 7\hat{i} - 4\hat{j} + p\hat{k}, \hat{i} - 6\hat{j} + 10\hat{k}$ and $-\hat{i} - 3\hat{j} + 7\hat{k}$ is 11 cubic units, then one of the values of p is

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $0$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

Let the vertices of the tetrahedron be $A(5, -1, 1)$, $B(7, -4, p)$, $C(1, -6, 10)$ and $D(-1, -3, 7)$.

The position vectors of the edges from vertex $A$ are:
$\overrightarrow{AB} = 2\hat{i} - 3\hat{j} + (p - 1)\hat{k}$
$\overrightarrow{AC} = -4\hat{i} - 5\hat{j} + 9\hat{k}$
$\overrightarrow{AD} = -6\hat{i} - 2\hat{j} + 6\hat{k}$

The volume of the tetrahedron is given by $V = \dfrac{1}{6} |[\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}]|$.

$[\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}] = \begin{vmatrix} 2 & -3 & p - 1 \\ -4 & -5 & 9 \\ -6 & -2 & 6 \end{vmatrix}$

$= 2(-30 + 18) + 3(-24 + 54) + (p - 1)(8 - 30)$

$= 2(-12) + 3(30) - 22(p - 1)$

$= -24 + 90 - 22p + 22 = 88 - 22p$

Given $V = 11$, we have:
$\dfrac{1}{6} |88 - 22p| = 11$

$|88 - 22p| = 66$

$|4 - p| = 3$

$4 - p = \pm 3$

$p = 1$ or $p = 7$

One of the values of $p$ given in the options is $1$.

Answer: $1$

</details>

---

### Q24. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a} = \hat{i} + \hat{j} + \hat{k}, \bar{b} = \hat{i} - \hat{j} + 2\hat{k}$ and $\bar{c} = x\hat{i} + (x - 2)\hat{j} - \hat{k}$ are three vectors in which $\bar{c}$ lies in the plane of $\bar{a}$ and $\bar{b}$, then $x = \cdots$

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $-4$
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-2$**

**Detailed Solution:**

Since $\bar{c}$ lies in the plane of $\bar{a}$ and $\bar{b}$, the vectors $\bar{a}$, $\bar{b}$, and $\bar{c}$ are coplanar.

Therefore, their scalar triple product is zero: $[\bar{a} \quad \bar{b} \quad \bar{c}] = 0$

$\begin{vmatrix} 1 & 1 & 1 \\ 1 & -1 & 2 \\ x & x - 2 & -1 \end{vmatrix} = 0$

Expanding the determinant along the first row:

$1((-1)(-1) - 2(x - 2)) - 1(1(-1) - 2x) + 1(1(x - 2) - (-1)x) = 0$

$1(1 - 2x + 4) - 1(-1 - 2x) + 1(x - 2 + x) = 0$

$(5 - 2x) + (1 + 2x) + (2x - 2) = 0$

$4 + 2x = 0$

$2x = -4 \Rightarrow x = -2$

Answer: $-2$

</details>

---

### Q25. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $|\bar{a}| = 4, |\bar{b}| = 3$ and $\bar{a} \cdot \bar{b} = 8$ then $[\bar{a}\ \ \bar{a} + \bar{b}\ \ \bar{a} \times \bar{b}] = $

**Options:**

- **(A)** $96$
- **(B)** $80$
- **(C)** $64$
- **(D)** $120$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $80$**

**Detailed Solution:**

Using the properties of the scalar triple product:

$[\bar{a}\ \ \bar{a} + \bar{b}\ \ \bar{a} \times \bar{b}] = [\bar{a}\ \ \bar{a}\ \ \bar{a} \times \bar{b}] + [\bar{a}\ \ \bar{b}\ \ \bar{a} \times \bar{b}]$

Since the scalar triple product is zero when two vectors are identical, $[\bar{a}\ \ \bar{a}\ \ \bar{a} \times \bar{b}] = 0$.

$[\bar{a}\ \ \bar{a} + \bar{b}\ \ \bar{a} \times \bar{b}] = [\bar{a}\ \ \bar{b}\ \ \bar{a} \times \bar{b}]$

This can be written as:

$[\bar{a}\ \ \bar{b}\ \ \bar{a} \times \bar{b}] = (\bar{a} \times \bar{b}) \cdot (\bar{a} \times \bar{b}) = |\bar{a} \times \bar{b}|^2$

Using Lagrange's identity:

$|\bar{a} \times \bar{b}|^2 = |\bar{a}|^2 |\bar{b}|^2 - (\bar{a} \cdot \bar{b})^2$

Substituting the given values $|\bar{a}| = 4$, $|\bar{b}| = 3$, and $\bar{a} \cdot \bar{b} = 8$:

$|\bar{a} \times \bar{b}|^2 = (4)^2 (3)^2 - (8)^2$

$|\bar{a} \times \bar{b}|^2 = 16 \times 9 - 64$

$|\bar{a} \times \bar{b}|^2 = 144 - 64 = 80$

Answer: $80$

</details>

---

### Q26. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $x_0$ be the point of local maxima of $f(x) = \bar{a} \cdot (\bar{b} \times \bar{c})$ where $\bar{a} = x\hat{i} - 2\hat{j} + 3\hat{k}, \bar{b} = -2\hat{i} + x\hat{j} - \hat{k}$ and $\bar{c} = 7\hat{i} - 2\hat{j} + x\hat{k}$ then the value of $\bar{a} \cdot \bar{c}$ at $x = x_0$ is

**Options:**

- **(A)** $26$
- **(B)** $0$
- **(C)** $-15$
- **(D)** $-26$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-26$**

**Detailed Solution:**

The function $f(x)$ is given by the scalar triple product of the vectors $\bar{a}$, $\bar{b}$, and $\bar{c}$.

$f(x) = \begin{vmatrix} x & -2 & 3 \\ -2 & x & -1 \\ 7 & -2 & x \end{vmatrix}$

Expanding the determinant, we get:

$f(x) = x(x^2 - 2) - (-2)(-2x + 7) + 3(4 - 7x)$

$f(x) = x^3 - 2x - 4x + 14 + 12 - 21x$

$f(x) = x^3 - 27x + 26$

To find the critical points, we set the first derivative to zero:

$f'(x) = 3x^2 - 27 = 0$

$x^2 = 9 \Rightarrow x = \pm 3$

To determine the point of local maxima, we check the second derivative:

$f''(x) = 6x$

At $x = 3$, $f''(3) = 18 > 0$ (local minima).

At $x = -3$, $f''(-3) = -18 < 0$ (local maxima).

Thus, the point of local maxima is $x_0 = -3$.

Now, we calculate the dot product $\bar{a} \cdot \bar{c}$:

$\bar{a} \cdot \bar{c} = (x)(7) + (-2)(-2) + (3)(x)$

$\bar{a} \cdot \bar{c} = 7x + 4 + 3x = 10x + 4$

Substituting $x = x_0 = -3$ into the expression:

$\bar{a} \cdot \bar{c} = 10(-3) + 4 = -30 + 4 = -26$

Answer: $-26$

</details>

---

### Q27. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The parallelopiped is determined by vectors $\bar{a} = -2\hat{i} + 5\hat{j} + 3\hat{k}$, $\bar{b} = \hat{i} + 3\hat{j} - 2\hat{k}$, $\bar{c} = -3\hat{i} + \hat{j} + 4\hat{k}$. The altitude of parallelopiped on the parallelogram base determined by vectors $\bar{b}$ and $\bar{c}$ is

**Options:**

- **(A)** $\dfrac{2\sqrt{3}}{5}$
- **(B)** $\dfrac{2}{5}$
- **(C)** $12$
- **(D)** $\dfrac{5\sqrt{3}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2\sqrt{3}}{5}$**

**Detailed Solution:**

The volume of the parallelepiped is given by the scalar triple product $V = |[\bar{a} \ \bar{b} \ \bar{c}]|$.

$V = \left| \begin{matrix} -2 & 5 & 3 \\ 1 & 3 & -2 \\ -3 & 1 & 4 \end{matrix} \right|$

$V = |-2(12 + 2) - 5(4 - 6) + 3(1 + 9)|$

$V = |-28 + 10 + 30| = 12$

The area of the parallelogram base determined by vectors $\bar{b}$ and $\bar{c}$ is $A = |\bar{b} \times \bar{c}|$.

$\bar{b} \times \bar{c} = \left| \begin{matrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 3 & -2 \\ -3 & 1 & 4 \end{matrix} \right|$

$\bar{b} \times \bar{c} = \hat{i}(12 + 2) - \hat{j}(4 - 6) + \hat{k}(1 + 9) = 14\hat{i} + 2\hat{j} + 10\hat{k}$

$A = \sqrt{14^2 + 2^2 + 10^2} = \sqrt{196 + 4 + 100} = \sqrt{300} = 10\sqrt{3}$

The altitude $h$ of the parallelepiped is the volume divided by the area of the base:

$h = \dfrac{V}{A} = \dfrac{12}{10\sqrt{3}} = \dfrac{6}{5\sqrt{3}} = \dfrac{2\sqrt{3}}{5}$

Answer: $\dfrac{2\sqrt{3}}{5}$

</details>

---

### Q28. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $a, b, c$ are distinct non-negative numbers and the vectors $a\hat{i} + a\hat{j} + c\hat{k}, \hat{i} + \hat{k}, c\hat{i} + c\hat{j} + b\hat{k}$ lie in the same plane, then the value of $c$ is...

**Options:**

- **(A)** The arithmetic mean of $a$ and $b$
- **(B)** The geometric mean of $a$ and $b$
- **(C)** The harmonic mean of $a$ and $b$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) The geometric mean of $a$ and $b$**

**Detailed Solution:**

Since the given vectors are coplanar, their scalar triple product is zero.

$\begin{vmatrix} a & a & c \\ 1 & 0 & 1 \\ c & c & b \end{vmatrix} = 0$

Expanding the determinant along the first row:

$a(0 - c) - a(b - c) + c(c - 0) = 0$

$-ac - ab + ac + c^2 = 0$

$c^2 - ab = 0$

$c^2 = ab$

Since $a, b, c$ are non-negative numbers, $c = \sqrt{ab}$.

Thus, $c$ is the geometric mean of $a$ and $b$.

Answer: The geometric mean of $a$ and $b$

</details>

---

### Q29. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The vectors $\overline{\mathrm{p}}=\hat{\mathrm{i}}+a \hat{\mathrm{j}}+a^2 \hat{\mathrm{k}}, \overline{\mathrm{q}}=\hat{\mathrm{i}}+b \hat{\mathrm{j}}+b^2 \hat{\mathrm{k}}$ and $\overline{\mathrm{r}}=\hat{\mathrm{i}}+c \hat{\mathrm{j}}+c^2 \hat{\mathrm{k}}$ are non-coplanar and
$\left|\begin{array}{lll}
a & a^2 & 1+a^3 \\
b & b^2 & 1+b^3 \\
c & c^2 & 1+c^3
\end{array}\right|=0$
then the value of $(a b c)$ is

**Options:**

- **(A)** 0
- **(B)** -1
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -1**

**Detailed Solution:**

Since the vectors $\overline{\mathrm{p}}, \overline{\mathrm{q}}, \overline{\mathrm{r}}$ are non-coplanar, their scalar triple product is non-zero:

$[\overline{\mathrm{p}} \quad \overline{\mathrm{q}} \quad \overline{\mathrm{r}}] = \left|\begin{array}{ccc} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{array}\right| \neq 0$

The given determinant equation is:

$\left|\begin{array}{lll} a & a^2 & 1+a^3 \\ b & b^2 & 1+b^3 \\ c & c^2 & 1+c^3 \end{array}\right|=0$

Splitting the determinant along the third column, we get:

$\left|\begin{array}{lll} a & a^2 & 1 \\ b & b^2 & 1 \\ c & c^2 & 1 \end{array}\right| + \left|\begin{array}{lll} a & a^2 & a^3 \\ b & b^2 & b^3 \\ c & c^2 & c^3 \end{array}\right| = 0$

In the first determinant, interchanging $C_1$ and $C_3$, and then $C_2$ and $C_3$ (two column swaps leave the sign unchanged):

$\left|\begin{array}{lll} a & a^2 & 1 \\ b & b^2 & 1 \\ c & c^2 & 1 \end{array}\right| = \left|\begin{array}{lll} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{array}\right|$

In the second determinant, taking $a, b, c$ common from $R_1, R_2, R_3$ respectively:

$\left|\begin{array}{lll} a & a^2 & a^3 \\ b & b^2 & b^3 \\ c & c^2 & c^3 \end{array}\right| = abc \left|\begin{array}{lll} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{array}\right|$

Substituting these back into the equation:

$\left|\begin{array}{lll} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{array}\right| + abc \left|\begin{array}{lll} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{array}\right| = 0$

$(1 + abc) \left|\begin{array}{lll} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{array}\right| = 0$

Since the determinant is non-zero, we must have:

$1 + abc = 0$

$abc = -1$

Answer: -1

</details>

---

### Q30. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The altitude of the parallelopiped, whose coterminus edges are the vectors $\bar{a}=\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}, \overline{\mathrm{b}}=2 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}-\hat{\mathrm{k}}, \overline{\mathrm{c}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}+3 \hat{\mathrm{k}}$, where $\bar{a}, \overline{\mathrm{~b}}$ are the sides of the base of parallelopiped, is

**Options:**

- **(A)** $\frac{4}{\sqrt{38}}$
- **(B)** $\frac{4}{\sqrt{19}}$
- **(C)** $\frac{5}{\sqrt{38}}$
- **(D)** $\frac{5}{\sqrt{19}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{4}{\sqrt{38}}$**

**Detailed Solution:**

The volume of the parallelepiped is given by the scalar triple product $V = |[\bar{a} \quad \bar{b} \quad \bar{c}]|$.

$V = \begin{vmatrix} 1 & 1 & 1 \\ 2 & 4 & -1 \\ 1 & 1 & 3 \end{vmatrix}$

$V = 1(12 + 1) - 1(6 + 1) + 1(2 - 4) = 13 - 7 - 2 = 4$

The area of the base formed by $\bar{a}$ and $\bar{b}$ is $A = |\bar{a} \times \bar{b}|$.

$\bar{a} \times \bar{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & 1 \\ 2 & 4 & -1 \end{vmatrix} = \hat{i}(-1 - 4) - \hat{j}(-1 - 2) + \hat{k}(4 - 2) = -5\hat{i} + 3\hat{j} + 2\hat{k}$

$A = \sqrt{(-5)^2 + 3^2 + 2^2} = \sqrt{25 + 9 + 4} = \sqrt{38}$

The altitude of the parallelepiped is $h = \dfrac{V}{A} = \dfrac{4}{\sqrt{38}}$.

Answer: $\frac{4}{\sqrt{38}}$

</details>

---

### Q31. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The volume of tetrahedron with co-terminus edges $\bar{a}, \overline{\mathrm{~b}}, \overline{\mathrm{c}}$ is $\frac{64}{3}$ cubic units, then volume of parallelopiped considering coterminus edges given by the vectors $\bar{a}+\bar{b}, \bar{b}+\bar{c}, \bar{c}+\bar{a}$ is ... cubic units.

**Options:**

- **(A)** 384
- **(B)** $\frac{128}{3}$
- **(C)** 256
- **(D)** $\frac{32}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 256**

**Detailed Solution:**

The volume of a tetrahedron with coterminous edges $\bar{a}, \bar{b}, \bar{c}$ is given by:

$V_{\text{tetrahedron}} = \dfrac{1}{6} |[\bar{a}, \bar{b}, \bar{c}]|$

Given that $V_{\text{tetrahedron}} = \dfrac{64}{3}$, we have:

$\dfrac{1}{6} |[\bar{a}, \bar{b}, \bar{c}]| = \dfrac{64}{3}$

$|[\bar{a}, \bar{b}, \bar{c}]| = \dfrac{64}{3} \times 6 = 128$

The volume of a parallelepiped with coterminous edges $\bar{a}+\bar{b}, \bar{b}+\bar{c}, \bar{c}+\bar{a}$ is given by:

$V_{\text{parallelepiped}} = |[\bar{a}+\bar{b}, \bar{b}+\bar{c}, \bar{c}+\bar{a}]|$

Using the scalar triple product property $[\bar{a}+\bar{b}, \bar{b}+\bar{c}, \bar{c}+\bar{a}] = 2[\bar{a}, \bar{b}, \bar{c}]$, we get:

$V_{\text{parallelepiped}} = 2|[\bar{a}, \bar{b}, \bar{c}]|$

$V_{\text{parallelepiped}} = 2 \times 128 = 256$ cubic units

Answer: 256

</details>

---

### Q32. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}, \overline{\mathrm{~b}}, \overline{\mathrm{c}}, \overline{\mathrm{d}}$ are vectors such that $\bar{a} \times \overline{\mathrm{b}}=2 \hat{i}+3 \hat{\mathrm{j}}-\hat{\mathrm{k}}$ and $\overline{\mathrm{c}} \times \overline{\mathrm{d}}=3 \hat{i}+2 \hat{\mathrm{j}}+\lambda \hat{\mathrm{k}}$ and if $\left|\begin{array}{cc}\bar{a} \cdot \overline{\mathrm{c}} & \overline{\mathrm{b}} \cdot \overline{\mathrm{c}} \\ \bar{a} \cdot \overline{\mathrm{~d}} & \overline{\mathrm{~b}} \cdot \overline{\mathrm{~d}}\end{array}\right|=0$, then $\lambda=$

**Options:**

- **(A)** $6$
- **(B)** $-6$
- **(C)** $12$
- **(D)** $-12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $12$**

**Detailed Solution:**

The given determinant is:

$\left|\begin{array}{cc}\bar{a} \cdot \bar{c} & \bar{b} \cdot \bar{c} \\ \bar{a} \cdot \bar{d} & \bar{b} \cdot \bar{d}\end{array}\right|=0$

Expanding the determinant, we get:

$(\bar{a} \cdot \bar{c})(\bar{b} \cdot \bar{d}) - (\bar{b} \cdot \bar{c})(\bar{a} \cdot \bar{d}) = 0$

We know the vector identity for the dot product of two cross products:

$(\bar{a} \times \bar{b}) \cdot (\bar{c} \times \bar{d}) = (\bar{a} \cdot \bar{c})(\bar{b} \cdot \bar{d}) - (\bar{a} \cdot \bar{d})(\bar{b} \cdot \bar{c})$

Therefore, the given condition implies:

$(\bar{a} \times \bar{b}) \cdot (\bar{c} \times \bar{d}) = 0$

Substituting the given vectors $\bar{a} \times \bar{b} = 2 \hat{i} + 3 \hat{j} - \hat{k}$ and $\bar{c} \times \bar{d} = 3 \hat{i} + 2 \hat{j} + \lambda \hat{k}$:

$(2 \hat{i} + 3 \hat{j} - \hat{k}) \cdot (3 \hat{i} + 2 \hat{j} + \lambda \hat{k}) = 0$

$(2)(3) + (3)(2) + (-1)(\lambda) = 0$

$6 + 6 - \lambda = 0$

$\lambda = 12$

Answer: $12$

</details>

---

### Q33. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The length of the altitude through the point D of tetrahedron where the vertices of the tetrahedron are $\mathrm{A}(2,3,1), \mathrm{B}(4,1,-2), \mathrm{C}(6,3,7)$, $D(-5,-4,8)$, is

**Options:**

- **(A)** 5.5 units
- **(B)** 22 units
- **(C)** 33 units
- **(D)** 11 units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 11 units**

**Detailed Solution:**

The position vectors of the vertices are $\vec{a} = 2\hat{i} + 3\hat{j} + \hat{k}$, $\vec{b} = 4\hat{i} + \hat{j} - 2\hat{k}$, $\vec{c} = 6\hat{i} + 3\hat{j} + 7\hat{k}$, and $\vec{d} = -5\hat{i} - 4\hat{j} + 8\hat{k}$.

The vectors representing the edges from vertex A are:
$\vec{AB} = \vec{b} - \vec{a} = 2\hat{i} - 2\hat{j} - 3\hat{k}$
$\vec{AC} = \vec{c} - \vec{a} = 4\hat{i} + 0\hat{j} + 6\hat{k}$
$\vec{AD} = \vec{d} - \vec{a} = -7\hat{i} - 7\hat{j} + 7\hat{k}$

The volume of the tetrahedron is given by $V = \dfrac{1}{6} |[\vec{AB}, \vec{AC}, \vec{AD}]|$.
Also, the volume is $V = \dfrac{1}{3} \times \text{Area of base ABC} \times h$, where $h$ is the altitude from D.
Therefore, $h = \dfrac{|[\vec{AB}, \vec{AC}, \vec{AD}]|}{|\vec{AB} \times \vec{AC}|}$.

First, we find $\vec{AB} \times \vec{AC}$:
$\vec{AB} \times \vec{AC} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & -2 & -3 \\ 4 & 0 & 6 \end{vmatrix}$
$\vec{AB} \times \vec{AC} = \hat{i}(-12 - 0) - \hat{j}(12 - (-12)) + \hat{k}(0 - (-8))$
$\vec{AB} \times \vec{AC} = -12\hat{i} - 24\hat{j} + 8\hat{k}$

The magnitude of this vector is:
$|\vec{AB} \times \vec{AC}| = \sqrt{(-12)^2 + (-24)^2 + 8^2} = \sqrt{144 + 576 + 64} = \sqrt{784} = 28$

Next, we find the scalar triple product $[\vec{AB}, \vec{AC}, \vec{AD}]$:
$[\vec{AB}, \vec{AC}, \vec{AD}] = (\vec{AB} \times \vec{AC}) \cdot \vec{AD}$
$= (-12\hat{i} - 24\hat{j} + 8\hat{k}) \cdot (-7\hat{i} - 7\hat{j} + 7\hat{k})$
$= (-12)(-7) + (-24)(-7) + (8)(7)$
$= 84 + 168 + 56 = 308$

Finally, the length of the altitude $h$ is:
$h = \dfrac{308}{28} = 11 \text{ units}$

Answer: 11 units

</details>

---

### Q34. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The volume of the tetrahedron whose coterminus edges are represented by $\bar{a}=-12 \hat{i}+\mathrm{p} \hat{\mathrm{k}}, \overline{\mathrm{b}}=3 \hat{\mathrm{j}}-\hat{\mathrm{k}}, \overline{\mathrm{c}}=2 \hat{i}+\hat{\mathrm{j}}-15 \hat{\mathrm{k}}$, is 570 cu. units, then $\mathrm{p}=$

**Options:**

- **(A)** $7$
- **(B)** $-12$
- **(C)** $-482$
- **(D)** $482$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-482$**

**Detailed Solution:**

The volume of a tetrahedron with coterminous edges $\bar{a}$, $\bar{b}$, and $\bar{c}$ is given by $V = \dfrac{1}{6} |[\bar{a}, \bar{b}, \bar{c}]|$.

First, we find the scalar triple product $[\bar{a}, \bar{b}, \bar{c}]$:

$[\bar{a}, \bar{b}, \bar{c}] = \begin{vmatrix} -12 & 0 & p \\ 0 & 3 & -1 \\ 2 & 1 & -15 \end{vmatrix}$

Expanding the determinant along the first row:

$[\bar{a}, \bar{b}, \bar{c}] = -12(3(-15) - (-1)(1)) - 0 + p(0(1) - 3(2))$

$[\bar{a}, \bar{b}, \bar{c}] = -12(-45 + 1) + p(-6)$

$[\bar{a}, \bar{b}, \bar{c}] = -12(-44) - 6p = 528 - 6p$

Given that the volume is $570$ cu. units:

$\dfrac{1}{6} |528 - 6p| = 570$

$|528 - 6p| = 3420$

This gives two possible equations:

$528 - 6p = 3420 \quad \text{or} \quad 528 - 6p = -3420$

Solving the first equation:

$-6p = 3420 - 528$

$-6p = 2892$

$p = -482$

Solving the second equation:

$-6p = -3420 - 528$

$-6p = -3948$

$p = 658$

Since $-482$ is among the given options, we have $p = -482$.

Answer: $-482$

</details>

---

### Q35. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three vectors $\hat{i}-\hat{\mathrm{k}}, \lambda \hat{i}+\hat{\mathrm{j}}+(1-\lambda) \hat{\mathrm{k}}$ and $\mu \hat{i}+\lambda \hat{\mathrm{j}}+(1+\lambda-\mu) \hat{\mathrm{k}}$ represents conterminus edges of a parallelopiped, then the volume of the parallelopiped depends on.

**Options:**

- **(A)** only $\lambda$
- **(B)** only $\mu$
- **(C)** $\operatorname{both} \lambda$ and $\mu$
- **(D)** neither $\lambda$ nor $\mu$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) neither $\lambda$ nor $\mu$**

**Detailed Solution:**

Let the coterminous edges of the parallelepiped be represented by the vectors:

$\vec{a} = \hat{i} - \hat{k}$

$\vec{b} = \lambda \hat{i} + \hat{j} + (1-\lambda) \hat{k}$

$\vec{c} = \mu \hat{i} + \lambda \hat{j} + (1+\lambda-\mu) \hat{k}$

The volume of the parallelepiped is given by the scalar triple product $V = |[\vec{a} \quad \vec{b} \quad \vec{c}]|$.

$[\vec{a} \quad \vec{b} \quad \vec{c}] = \begin{vmatrix} 1 & 0 & -1 \\ \lambda & 1 & 1-\lambda \\ \mu & \lambda & 1+\lambda-\mu \end{vmatrix}$

Expanding the determinant along the first row:

$= 1[1(1+\lambda-\mu) - \lambda(1-\lambda)] - 0 - 1[\lambda(\lambda) - 1(\mu)]$

$= [1 + \lambda - \mu - \lambda + \lambda^2] - [\lambda^2 - \mu]$

$= 1 - \mu + \lambda^2 - \lambda^2 + \mu$

$= 1$

The volume is $1$, which is a constant. Therefore, the volume of the parallelepiped depends on neither $\lambda$ nor $\mu$.

Answer: neither $\lambda$ nor $\mu$

</details>

---

### Q36. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\bar{a}$ and $\bar{c}$ be unit vectors at an angle $\frac{\pi}{3}$ with each other. If $(\bar{a} \times(\bar{b} \times \bar{c})) \cdot(\bar{a} \times \bar{c})=5$, then $\left[\begin{array}{lll}\bar{a} & \bar{b} & \bar{c}\end{array}\right]=$

**Options:**

- **(A)** $10$
- **(B)** $-10$
- **(C)** $9$
- **(D)** $-9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-10$**

**Detailed Solution:**

Using the vector triple product expansion:

$\bar{a} \times (\bar{b} \times \bar{c}) = (\bar{a} \cdot \bar{c})\bar{b} - (\bar{a} \cdot \bar{b})\bar{c}$

Substituting this into the given equation:

$((\bar{a} \cdot \bar{c})\bar{b} - (\bar{a} \cdot \bar{b})\bar{c}) \cdot (\bar{a} \times \bar{c}) = 5$

Distributing the dot product, we get:

$(\bar{a} \cdot \bar{c})(\bar{b} \cdot (\bar{a} \times \bar{c})) - (\bar{a} \cdot \bar{b})(\bar{c} \cdot (\bar{a} \times \bar{c})) = 5$

Since the scalar triple product of vectors with a repeated vector is zero, $\bar{c} \cdot (\bar{a} \times \bar{c}) = 0$. The equation simplifies to:

$(\bar{a} \cdot \bar{c})[\bar{b} \bar{a} \bar{c}] = 5$

We are given that $\bar{a}$ and $\bar{c}$ are unit vectors with an angle of $\dfrac{\pi}{3}$ between them. Thus:

$\bar{a} \cdot \bar{c} = |\bar{a}||\bar{c}|\cos\left(\dfrac{\pi}{3}\right) = 1 \times 1 \times \dfrac{1}{2} = \dfrac{1}{2}$

Substituting this value into the simplified equation:

$\dfrac{1}{2}[\bar{b} \bar{a} \bar{c}] = 5$

$[\bar{b} \bar{a} \bar{c}] = 10$

Using the properties of the scalar triple product, swapping two adjacent vectors changes the sign:

$[\bar{a} \bar{b} \bar{c}] = -[\bar{b} \bar{a} \bar{c}]$

Therefore, $[\bar{a} \bar{b} \bar{c}] = -10$

Answer: $-10$

</details>

---

### Q37. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The maximum value and minimum value of the volume of the parallelopiped having coterminous edges $\hat{i}+x \hat{j}+\hat{\mathrm{k}}, \hat{\mathrm{j}}+x \hat{\mathrm{k}}$ and $x \hat{i}+\hat{\mathrm{k}}$ for $x \in [-1, 1]$ are respectively

**Options:**

- **(A)** $\frac{1}{3 \sqrt{3}}+1, \frac{-1}{3 \sqrt{3}}+1$
- **(B)** $\frac{2}{3 \sqrt{3}}+1, \frac{-2}{3 \sqrt{3}}+1$
- **(C)** $\frac{1}{\sqrt{3}}+1, \frac{-1}{\sqrt{3}}+1$
- **(D)** $\frac{2}{\sqrt{3}}+1, \frac{-2}{\sqrt{3}}+1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{3 \sqrt{3}}+1, \frac{-2}{3 \sqrt{3}}+1$**

**Detailed Solution:**

The volume of the parallelepiped with coterminous edges $\vec{a}$, $\vec{b}$, and $\vec{c}$ is given by the absolute value of their scalar triple product:

$V = \left| \begin{vmatrix} 1 & x & 1 \\ 0 & 1 & x \\ x & 0 & 1 \end{vmatrix} \right|$

Expanding the determinant, we get a function $f(x)$:

$f(x) = 1(1 - 0) - x(0 - x^2) + 1(0 - x) = x^3 - x + 1$

To find the maximum and minimum values of the volume for $x \in [-1, 1]$, we differentiate $f(x)$ with respect to $x$:

$f'(x) = 3x^2 - 1$

Setting $f'(x) = 0$ to find the critical points:

$3x^2 - 1 = 0 \Rightarrow x = \pm \dfrac{1}{\sqrt{3}}$

Now, we evaluate $f(x)$ at the critical points and the endpoints of the interval $[-1, 1]$:

At $x = \dfrac{1}{\sqrt{3}}$:

$f\left(\dfrac{1}{\sqrt{3}}\right) = \left(\dfrac{1}{\sqrt{3}}\right)^3 - \dfrac{1}{\sqrt{3}} + 1 = \dfrac{1}{3\sqrt{3}} - \dfrac{1}{\sqrt{3}} + 1 = 1 - \dfrac{2}{3\sqrt{3}}$

At $x = -\dfrac{1}{\sqrt{3}}$:

$f\left(-\dfrac{1}{\sqrt{3}}\right) = \left(-\dfrac{1}{\sqrt{3}}\right)^3 - \left(-\dfrac{1}{\sqrt{3}}\right) + 1 = -\dfrac{1}{3\sqrt{3}} + \dfrac{1}{\sqrt{3}} + 1 = 1 + \dfrac{2}{3\sqrt{3}}$

At the endpoints $x = 1$ and $x = -1$:

$f(1) = 1^3 - 1 + 1 = 1$

$f(-1) = (-1)^3 - (-1) + 1 = 1$

Since $1 - \dfrac{2}{3\sqrt{3}} > 0$, the value of $f(x)$ is always positive in this interval, meaning the volume is simply $V = f(x)$.

Comparing the obtained values, the maximum volume is $\dfrac{2}{3\sqrt{3}} + 1$ and the minimum volume is $\dfrac{-2}{3\sqrt{3}} + 1$.

Answer: $\frac{2}{3 \sqrt{3}}+1, \frac{-2}{3 \sqrt{3}}+1$

</details>

---

### Q38. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\bar{a}, \bar{b}, \bar{c}, \bar{d}$ are unit vectors such that $\bar{a} \cdot \bar{b}=\frac{1}{2}, \bar{c} \cdot \bar{d}=\frac{1}{2}$ and the angle between $\bar{a} \times \bar{b}$ and $\bar{c} \times \overline{\mathrm{d}}$ is $\frac{\pi}{6}$, then the value of $|[\bar{a} \overline{\mathrm{~b}} \mathrm{~d}] \bar{c}-[\bar{a} \overline{\mathrm{~b}} \bar{c}] \mathrm{d}|=$

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** $\frac{3}{4}$
- **(C)** $\frac{3}{8}$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{8}$**

**Detailed Solution:**

The given expression is $|[\bar{a} \bar{b} \bar{d}] \bar{c} - [\bar{a} \bar{b} \bar{c}] \bar{d}|$.

Using the vector quadruple product formula, we have:

$(\bar{a} \times \bar{b}) \times (\bar{c} \times \bar{d}) = ((\bar{a} \times \bar{b}) \cdot \bar{d}) \bar{c} - ((\bar{a} \times \bar{b}) \cdot \bar{c}) \bar{d} = [\bar{a} \bar{b} \bar{d}] \bar{c} - [\bar{a} \bar{b} \bar{c}] \bar{d}$

Thus, the required value is the magnitude of $(\bar{a} \times \bar{b}) \times (\bar{c} \times \bar{d})$:

$|(\bar{a} \times \bar{b}) \times (\bar{c} \times \bar{d})| = |\bar{a} \times \bar{b}| |\bar{c} \times \bar{d}| \sin \theta$

where $\theta$ is the angle between $\bar{a} \times \bar{b}$ and $\bar{c} \times \bar{d}$. We are given $\theta = \dfrac{\pi}{6}$.

Since $\bar{a}$ and $\bar{b}$ are unit vectors and $\bar{a} \cdot \bar{b} = \dfrac{1}{2}$:

$|\bar{a}| |\bar{b}| \cos \alpha = \dfrac{1}{2} \Rightarrow \cos \alpha = \dfrac{1}{2} \Rightarrow \sin \alpha = \dfrac{\sqrt{3}}{2}$

Therefore, $|\bar{a} \times \bar{b}| = |\bar{a}| |\bar{b}| \sin \alpha = \dfrac{\sqrt{3}}{2}$.

Similarly, $\bar{c}$ and $\bar{d}$ are unit vectors and $\bar{c} \cdot \bar{d} = \dfrac{1}{2}$:

$|\bar{c}| |\bar{d}| \cos \beta = \dfrac{1}{2} \Rightarrow \cos \beta = \dfrac{1}{2} \Rightarrow \sin \beta = \dfrac{\sqrt{3}}{2}$

Therefore, $|\bar{c} \times \bar{d}| = |\bar{c}| |\bar{d}| \sin \beta = \dfrac{\sqrt{3}}{2}$.

Substituting these values into the magnitude formula:

$|(\bar{a} \times \bar{b}) \times (\bar{c} \times \bar{d})| = \left(\dfrac{\sqrt{3}}{2}\right) \left(\dfrac{\sqrt{3}}{2}\right) \sin \dfrac{\pi}{6}$

$= \dfrac{3}{4} \times \dfrac{1}{2} = \dfrac{3}{8}$

Answer: $\frac{3}{8}$

</details>

---

### Q39. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The volume of the tetrahedron whose co-terminus edges are $\bar{a}, \overline{\mathrm{~b}}, \overline{\mathrm{c}}$ is 12 cubic units. If the scalar projection of $\bar{a}$ on $\overline{\mathrm{b}} \times \overline{\mathrm{c}}$ is 4 , then $|\overline{\mathrm{b}} \times \overline{\mathrm{c}}|=$

**Options:**

- **(A)** $18$
- **(B)** $\frac{1}{18}$
- **(C)** $16$
- **(D)** $\frac{1}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $18$**

**Detailed Solution:**

The volume of a tetrahedron with co-terminus edges $\bar{a}$, $\bar{b}$, and $\bar{c}$ is given by:

$V = \dfrac{1}{6} |\bar{a} \cdot (\bar{b} \times \bar{c})|$

Given $V = 12$, we have:

$\dfrac{1}{6} |\bar{a} \cdot (\bar{b} \times \bar{c})| = 12$

$|\bar{a} \cdot (\bar{b} \times \bar{c})| = 72$

The scalar projection of $\bar{a}$ on $\bar{b} \times \bar{c}$ is given by:

$\text{Projection} = \dfrac{|\bar{a} \cdot (\bar{b} \times \bar{c})|}{|\bar{b} \times \bar{c}|}$

Given that the scalar projection is $4$, we substitute the value of the scalar triple product:

$\dfrac{72}{|\bar{b} \times \bar{c}|} = 4$

$|\bar{b} \times \bar{c}| = \dfrac{72}{4} = 18$

Answer: $18$

</details>

---

### Q40. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\quad \bar{a}=a_1 \hat{i}+a_2 \hat{j}+a_3 \hat{k}, \quad \bar{b}=b_1 \hat{i}+b_2 \hat{j}+b_3 \hat{k}$, $\overline{\mathrm{c}}=\mathrm{c}_1 \hat{i}+\mathrm{c}_2 \hat{\mathrm{j}}+\mathrm{c}_3 \hat{\mathrm{k}}$ and
$\left[\begin{array}{lll}3 \overline{\mathrm{a}}+\overline{\mathrm{b}} & 3 \overline{\mathrm{~b}}+\overline{\mathrm{c}} & 3 \overline{\mathrm{c}}+\overline{\mathrm{a}}\end{array}\right]$
$=\lambda\left|\begin{array}{lll}\overline{\mathrm{a}} \cdot \hat{\mathrm{i}} & \overline{\mathrm{a}} \cdot \hat{\mathrm{j}} & \overline{\mathrm{a}} \cdot \hat{\mathrm{k}} \\ \overline{\mathrm{b}} \cdot \hat{\mathrm{i}} & \overline{\mathrm{b}} \cdot \hat{\mathrm{j}} & \overline{\mathrm{b}} \cdot \hat{\mathrm{k}} \\ \overline{\mathrm{c}} \cdot \hat{\mathrm{i}} & \overline{\mathrm{c}} \cdot \hat{\mathrm{j}} & \overline{\mathrm{c}} \cdot \hat{\mathrm{k}}\end{array}\right|$
then the value of $\lambda$ is

**Options:**

- **(A)** $27$
- **(B)** 28
- **(C)** 4
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 28**

**Detailed Solution:**

The scalar triple product on the left hand side can be expanded as:

$[3 \bar{a}+\bar{b} \quad 3 \bar{b}+\bar{c} \quad 3 \bar{c}+\bar{a}] = (3 \bar{a}+\bar{b}) \cdot ((3 \bar{b}+\bar{c}) \times (3 \bar{c}+\bar{a}))$

$= (3 \bar{a}+\bar{b}) \cdot (9 (\bar{b} \times \bar{c}) + 3 (\bar{b} \times \bar{a}) + 3 (\bar{c} \times \bar{c}) + (\bar{c} \times \bar{a}))$

Since $\bar{c} \times \bar{c} = 0$, the expression simplifies to:

$= (3 \bar{a}+\bar{b}) \cdot (9 (\bar{b} \times \bar{c}) + 3 (\bar{b} \times \bar{a}) + (\bar{c} \times \bar{a}))$

Distributing the dot product yields:

$= 27 [\bar{a} \quad \bar{b} \quad \bar{c}] + 9 [\bar{a} \quad \bar{b} \quad \bar{a}] + 3 [\bar{a} \quad \bar{c} \quad \bar{a}] + 9 [\bar{b} \quad \bar{b} \quad \bar{c}] + 3 [\bar{b} \quad \bar{b} \quad \bar{a}] + [\bar{b} \quad \bar{c} \quad \bar{a}]$

Since the scalar triple product is zero when any two vectors are identical, and $[\bar{b} \quad \bar{c} \quad \bar{a}] = [\bar{a} \quad \bar{b} \quad \bar{c}]$, we get:

$= 27 [\bar{a} \quad \bar{b} \quad \bar{c}] + 0 + 0 + 0 + 0 + [\bar{a} \quad \bar{b} \quad \bar{c}] = 28 [\bar{a} \quad \bar{b} \quad \bar{c}]$

For the right hand side, evaluating the dot products with the unit vectors gives:

$\bar{a} \cdot \hat{i} = a_1, \quad \bar{a} \cdot \hat{j} = a_2, \quad \bar{a} \cdot \hat{k} = a_3$

Similarly for $\bar{b}$ and $\bar{c}$. The determinant becomes:

$\left|\begin{array}{lll}a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3\end{array}\right| = [\bar{a} \quad \bar{b} \quad \bar{c}]$

Equating the left hand side and the right hand side:

$28 [\bar{a} \quad \bar{b} \quad \bar{c}] = \lambda [\bar{a} \quad \bar{b} \quad \bar{c}]$

Comparing both sides, we obtain $\lambda = 28$.

Answer: 28

</details>

---

### Q41. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}$ is perpendicular to $\bar{b}$ and $\bar{c},|\vec{a}|=2$, $|\bar{b}|=3,|\bar{c}|=4$ and the angle between $\bar{b}$ and $\bar{c}$ is $\frac{\pi}{3}$, then $\left|\left[\begin{array}{lll}\overline{\mathrm{a}} & \overline{\mathrm{b}} & \overline{\mathrm{c}}\end{array}\right]\right|=$

**Options:**

- **(A)** $4 \sqrt{3}$
- **(B)** $6 \sqrt{3}$
- **(C)** $24 \sqrt{3}$
- **(D)** $12 \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $12 \sqrt{3}$**

**Detailed Solution:**

The scalar triple product is given by $[\bar{a} \quad \bar{b} \quad \bar{c}] = \bar{a} \cdot (\bar{b} \times \bar{c})$.

Since $\bar{a}$ is perpendicular to both $\bar{b}$ and $\bar{c}$, the vector $\bar{a}$ is parallel to $\bar{b} \times \bar{c}$.

Therefore, the angle between $\bar{a}$ and $\bar{b} \times \bar{c}$ is either $0$ or $\pi$.

We have $|[\bar{a} \quad \bar{b} \quad \bar{c}]| = |\bar{a}| |\bar{b} \times \bar{c}| = |\bar{a}| |\bar{b}| |\bar{c}| \sin \theta$, where $\theta$ is the angle between $\bar{b}$ and $\bar{c}$.

Substituting the given values $|\bar{a}| = 2$, $|\bar{b}| = 3$, $|\bar{c}| = 4$, and $\theta = \dfrac{\pi}{3}$:

$|[\bar{a} \quad \bar{b} \quad \bar{c}]| = 2 \times 3 \times 4 \times \sin\left(\dfrac{\pi}{3}\right)$

$= 24 \times \dfrac{\sqrt{3}}{2} = 12\sqrt{3}$

Answer: $12 \sqrt{3}$

</details>

---

### Q42. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\left[\begin{array}{llll}\bar{a} \times \bar{b} & \bar{b} \times \bar{c} & \bar{c} \times \bar{a}\end{array}\right]=\lambda\left[\begin{array}{lll}\bar{a} & \bar{b} & \bar{c}\end{array}\right]^2$, then $\lambda$ is equal to

**Options:**

- **(A)** 3
- **(B)** 0
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

The scalar triple product is given by:

$[\bar{a} \times \bar{b} \quad \bar{b} \times \bar{c} \quad \bar{c} \times \bar{a}] = (\bar{a} \times \bar{b}) \cdot ((\bar{b} \times \bar{c}) \times (\bar{c} \times \bar{a}))$

Using the vector triple product expansion $\bar{p} \times (\bar{q} \times \bar{r}) = (\bar{p} \cdot \bar{r})\bar{q} - (\bar{p} \cdot \bar{q})\bar{r}$, let $\bar{p} = \bar{b} \times \bar{c}$, $\bar{q} = \bar{c}$, and $\bar{r} = \bar{a}$.

$(\bar{b} \times \bar{c}) \times (\bar{c} \times \bar{a}) = ((\bar{b} \times \bar{c}) \cdot \bar{a})\bar{c} - ((\bar{b} \times \bar{c}) \cdot \bar{c})\bar{a}$

Since the scalar triple product with two identical vectors is zero, $(\bar{b} \times \bar{c}) \cdot \bar{c} = 0$. The expression simplifies to:

$[\bar{b} \quad \bar{c} \quad \bar{a}]\bar{c} = [\bar{a} \quad \bar{b} \quad \bar{c}]\bar{c}$

Substituting this back into the original scalar triple product:

$[\bar{a} \times \bar{b} \quad \bar{b} \times \bar{c} \quad \bar{c} \times \bar{a}] = (\bar{a} \times \bar{b}) \cdot ([\bar{a} \quad \bar{b} \quad \bar{c}]\bar{c})$

Since $[\bar{a} \quad \bar{b} \quad \bar{c}]$ is a scalar, it can be factored out:

$[\bar{a} \times \bar{b} \quad \bar{b} \times \bar{c} \quad \bar{c} \times \bar{a}] = [\bar{a} \quad \bar{b} \quad \bar{c}] ((\bar{a} \times \bar{b}) \cdot \bar{c})$

$[\bar{a} \times \bar{b} \quad \bar{b} \times \bar{c} \quad \bar{c} \times \bar{a}] = [\bar{a} \quad \bar{b} \quad \bar{c}] [\bar{a} \quad \bar{b} \quad \bar{c}]$

$[\bar{a} \times \bar{b} \quad \bar{b} \times \bar{c} \quad \bar{c} \times \bar{a}] = [\bar{a} \quad \bar{b} \quad \bar{c}]^2$

Comparing this with the given equation $[\bar{a} \times \bar{b} \quad \bar{b} \times \bar{c} \quad \bar{c} \times \bar{a}] = \lambda[\bar{a} \quad \bar{b} \quad \bar{c}]^2$, we get $\lambda = 1$.

Answer: 1

</details>

---

### Q43. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\overline{\mathrm{a}}, \overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ are unit coplanar vectors, then the scalar triple product $\left[\begin{array}{lll}2 \bar{a}-\bar{b} & 2 \bar{b}-\bar{c} & 2 \bar{c}-\bar{a}\end{array}\right]$ has the value

**Options:**

- **(A)** 0
- **(B)** $-\sqrt{3}$
- **(C)** 1
- **(D)** $\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Since the vectors $\bar{a}$, $\bar{b}$, and $\bar{c}$ are coplanar, their scalar triple product is zero:

$[\bar{a} \quad \bar{b} \quad \bar{c}] = 0$

The given scalar triple product can be expanded using the properties of the scalar triple product as a determinant of the coefficients:

$[2\bar{a}-\bar{b} \quad 2\bar{b}-\bar{c} \quad 2\bar{c}-\bar{a}] = \begin{vmatrix} 2 & -1 & 0 \\ 0 & 2 & -1 \\ -1 & 0 & 2 \end{vmatrix} [\bar{a} \quad \bar{b} \quad \bar{c}]$

Evaluating the determinant:

$\begin{vmatrix} 2 & -1 & 0 \\ 0 & 2 & -1 \\ -1 & 0 & 2 \end{vmatrix} = 2(4 - 0) - (-1)(0 - 1) + 0$

$= 8 - 1 = 7$

Therefore, the expression becomes:

$7 [\bar{a} \quad \bar{b} \quad \bar{c}]$

Substituting $[\bar{a} \quad \bar{b} \quad \bar{c}] = 0$ into the expression:

$7 \times 0 = 0$

Answer: 0

</details>

---

### Q44. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\overline{\mathrm{u}}, \overline{\mathrm{v}}$ and $\overline{\mathrm{w}}$ are three non-coplanar vectors, then $(\bar{u}+\bar{v}-\bar{w}) \cdot[(\bar{u}-\bar{v}) \times(\bar{v}-\bar{w})]$ is equal to

**Options:**

- **(A)** $\overline{\mathrm{u}} \cdot(\overline{\mathrm{v}} \times \overline{\mathrm{w}})$
- **(B)** $\overline{\mathrm{u}} \cdot(\overline{\mathrm{w}} \times \overline{\mathrm{v}})$
- **(C)** $3 \overline{\mathrm{u}} \cdot(\overline{\mathrm{v}} \times \overline{\mathrm{w}})$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\overline{\mathrm{u}} \cdot(\overline{\mathrm{v}} \times \overline{\mathrm{w}})$**

**Detailed Solution:**

Expanding the cross product term:

$(\bar{u}-\bar{v}) \times(\bar{v}-\bar{w}) = \bar{u} \times \bar{v} - \bar{u} \times \bar{w} - \bar{v} \times \bar{v} + \bar{v} \times \bar{w}$

Since the cross product of a vector with itself is zero ($\bar{v} \times \bar{v} = 0$), this simplifies to:

$\bar{u} \times \bar{v} - \bar{u} \times \bar{w} + \bar{v} \times \bar{w}$

Taking the dot product of $(\bar{u}+\bar{v}-\bar{w})$ with this result:

$(\bar{u}+\bar{v}-\bar{w}) \cdot (\bar{u} \times \bar{v} - \bar{u} \times \bar{w} + \bar{v} \times \bar{w})$

Distributing the dot product and writing in terms of the scalar triple product $[\bar{a} \ \bar{b} \ \bar{c}]$:

$= \bar{u} \cdot (\bar{u} \times \bar{v}) - \bar{u} \cdot (\bar{u} \times \bar{w}) + \bar{u} \cdot (\bar{v} \times \bar{w}) + \bar{v} \cdot (\bar{u} \times \bar{v}) - \bar{v} \cdot (\bar{u} \times \bar{w}) + \bar{v} \cdot (\bar{v} \times \bar{w}) - \bar{w} \cdot (\bar{u} \times \bar{v}) + \bar{w} \cdot (\bar{u} \times \bar{w}) - \bar{w} \cdot (\bar{v} \times \bar{w})$

The scalar triple product is zero if any two vectors are identical. Thus, the expression reduces to:

$= 0 - 0 + [\bar{u} \ \bar{v} \ \bar{w}] + 0 - [\bar{v} \ \bar{u} \ \bar{w}] + 0 - [\bar{w} \ \bar{u} \ \bar{v}] + 0 - 0$

Using the properties of the scalar triple product, $[\bar{v} \ \bar{u} \ \bar{w}] = -[\bar{u} \ \bar{v} \ \bar{w}]$ and $[\bar{w} \ \bar{u} \ \bar{v}] = [\bar{u} \ \bar{v} \ \bar{w}]$:

$= [\bar{u} \ \bar{v} \ \bar{w}] - (-[\bar{u} \ \bar{v} \ \bar{w}]) - [\bar{u} \ \bar{v} \ \bar{w}]$

$= [\bar{u} \ \bar{v} \ \bar{w}] + [\bar{u} \ \bar{v} \ \bar{w}] - [\bar{u} \ \bar{v} \ \bar{w}]$

$= [\bar{u} \ \bar{v} \ \bar{w}]$

$= \bar{u} \cdot (\bar{v} \times \bar{w})$

Answer: $\overline{\mathrm{u}} \cdot(\overline{\mathrm{v}} \times \overline{\mathrm{w}})$

</details>

---

### Q45. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the volume of tetrahedron whose vertices are $\mathrm{A} \equiv(1,-6,10), \mathrm{B} \equiv(-1,-3,7), \mathrm{C} \equiv(5,-1, \mathrm{k})$ and $D \equiv(7,-4,7)$ is 11 cu . units, then the value of $k$ is

**Options:**

- **(A)** 7
- **(B)** 5
- **(C)** 3
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 7**

**Detailed Solution:**

The volume of a tetrahedron with vertices $A, B, C, D$ is given by $V = \dfrac{1}{6} |[\overrightarrow{AB} \quad \overrightarrow{AC} \quad \overrightarrow{AD}]|$.

First, we find the vectors $\overrightarrow{AB}, \overrightarrow{AC}$, and $\overrightarrow{AD}$:
$\overrightarrow{AB} = (-1 - 1)\hat{i} + (-3 - (-6))\hat{j} + (7 - 10)\hat{k} = -2\hat{i} + 3\hat{j} - 3\hat{k}$
$\overrightarrow{AC} = (5 - 1)\hat{i} + (-1 - (-6))\hat{j} + (k - 10)\hat{k} = 4\hat{i} + 5\hat{j} + (k - 10)\hat{k}$
$\overrightarrow{AD} = (7 - 1)\hat{i} + (-4 - (-6))\hat{j} + (7 - 10)\hat{k} = 6\hat{i} + 2\hat{j} - 3\hat{k}$

The scalar triple product is given by the determinant:
$[\overrightarrow{AB} \quad \overrightarrow{AC} \quad \overrightarrow{AD}] = \begin{vmatrix} -2 & 3 & -3 \\ 4 & 5 & k-10 \\ 6 & 2 & -3 \end{vmatrix}$

Expanding the determinant:
$= -2(-15 - 2(k-10)) - 3(-12 - 6(k-10)) - 3(8 - 30)$
$= -2(-15 - 2k + 20) - 3(-12 - 6k + 60) - 3(-22)$
$= -2(5 - 2k) - 3(48 - 6k) + 66$
$= -10 + 4k - 144 + 18k + 66$
$= 22k - 88$

Given that the volume is $11$ cubic units:
$\dfrac{1}{6} |22k - 88| = 11$
$|22k - 88| = 66$
$22|k - 4| = 66$
$|k - 4| = 3$

This gives $k - 4 = 3$ or $k - 4 = -3$.
$k = 7$ or $k = 1$

From the given options, $k = 7$.

Answer: 7

</details>

---

### Q46. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}$ are mutually perpendicular vectors having magnitudes $1,2,3$ respectively, then the value of $\left[\begin{array}{lll}\bar{a}+\bar{b}+\bar{c} & \bar{b}-\bar{a} & \bar{c}\end{array}\right]$ is

**Options:**

- **(A)** 0
- **(B)** 6
- **(C)** 12
- **(D)** 18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 12**

**Detailed Solution:**

The given expression is $[\bar{a}+\bar{b}+\bar{c} \quad \bar{b}-\bar{a} \quad \bar{c}]$.

Using the properties of the scalar triple product, we can expand this as:

$[\bar{a}+\bar{b}+\bar{c} \quad \bar{b}-\bar{a} \quad \bar{c}] = [\bar{a} \quad \bar{b}-\bar{a} \quad \bar{c}] + [\bar{b} \quad \bar{b}-\bar{a} \quad \bar{c}] + [\bar{c} \quad \bar{b}-\bar{a} \quad \bar{c}]$

Expanding further by separating the second term in each bracket:

$= ([\bar{a} \quad \bar{b} \quad \bar{c}] - [\bar{a} \quad \bar{a} \quad \bar{c}]) + ([\bar{b} \quad \bar{b} \quad \bar{c}] - [\bar{b} \quad \bar{a} \quad \bar{c}]) + ([\bar{c} \quad \bar{b} \quad \bar{c}] - [\bar{c} \quad \bar{a} \quad \bar{c}])$

Since the scalar triple product is zero if any two vectors are identical, we get:

$= [\bar{a} \quad \bar{b} \quad \bar{c}] - 0 + 0 - [\bar{b} \quad \bar{a} \quad \bar{c}] + 0 - 0$

Using the property $[\bar{b} \quad \bar{a} \quad \bar{c}] = -[\bar{a} \quad \bar{b} \quad \bar{c}]$:

$= [\bar{a} \quad \bar{b} \quad \bar{c}] - (-[\bar{a} \quad \bar{b} \quad \bar{c}]) = 2[\bar{a} \quad \bar{b} \quad \bar{c}]$

Since $\bar{a}, \bar{b}, \bar{c}$ are mutually perpendicular vectors, the volume of the parallelepiped formed by them is the product of their magnitudes:

$[\bar{a} \quad \bar{b} \quad \bar{c}] = |\bar{a}||\bar{b}||\bar{c}|$

Given $|\bar{a}| = 1$, $|\bar{b}| = 2$, and $|\bar{c}| = 3$:

$[\bar{a} \quad \bar{b} \quad \bar{c}] = 1 \times 2 \times 3 = 6$

Substituting this value back:

$2[\bar{a} \quad \bar{b} \quad \bar{c}] = 2 \times 6 = 12$

Answer: 12

</details>

---

### Q47. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{a}} \cdot$ and $\overline{\mathrm{c}}$ are unit vectors inclined at $\dfrac{\pi}{3}$ with each other and $(\overline{\mathrm{a}} \times(\overline{\mathrm{b}} \times \overline{\mathrm{c}})) \cdot(\overline{\mathrm{a}} \times \overline{\mathrm{c}})=5$, then the value of $5[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]=$

**Options:**

- **(A)** -10
- **(B)** 10
- **(C)** 50
- **(D)** -50

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -50**

**Detailed Solution:**

Given vectors $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}$ are unit vectors inclined at $\dfrac{\pi}{3}$ with each other.

$\Rightarrow \overline{\mathrm{a}} \cdot \overline{\mathrm{c}} = |\overline{\mathrm{a}}||\overline{\mathrm{c}}|\cos\left(\dfrac{\pi}{3}\right) = 1 \times 1 \times \dfrac{1}{2} = \dfrac{1}{2}$

Consider the given expression:

$(\overline{\mathrm{a}} \times (\overline{\mathrm{b}} \times \overline{\mathrm{c}})) \cdot (\overline{\mathrm{a}} \times \overline{\mathrm{c}}) = 5$

Using the vector triple product expansion $\overline{\mathrm{a}} \times (\overline{\mathrm{b}} \times \overline{\mathrm{c}}) = (\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})\overline{\mathrm{b}} - (\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})\overline{\mathrm{c}}$, we get:

$((\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})\overline{\mathrm{b}} - (\overline{\mathrm{a}} \cdot \overline{\mathrm{b}})\overline{\mathrm{c}}) \cdot (\overline{\mathrm{a}} \times \overline{\mathrm{c}}) = 5$

Distributing the dot product:

$(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) (\overline{\mathrm{b}} \cdot (\overline{\mathrm{a}} \times \overline{\mathrm{c}})) - (\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}) (\overline{\mathrm{c}} \cdot (\overline{\mathrm{a}} \times \overline{\mathrm{c}})) = 5$

Since the scalar triple product with repeated vectors is zero, $\overline{\mathrm{c}} \cdot (\overline{\mathrm{a}} \times \overline{\mathrm{c}}) = 0$. Thus, the equation simplifies to:

$(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) [\overline{\mathrm{b}} \overline{\mathrm{a}} \overline{\mathrm{c}}] = 5$

Using the property of scalar triple products, $[\overline{\mathrm{b}} \overline{\mathrm{a}} \overline{\mathrm{c}}] = -[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$. Substituting this and $\overline{\mathrm{a}} \cdot \overline{\mathrm{c}} = \dfrac{1}{2}$:

$\dfrac{1}{2} (-[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]) = 5$

$-[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}] = 10$

$[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}] = -10$

Therefore, the value of $5[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$ is:

$5(-10) = -50$

Answer: -50

</details>

---

### Q48. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\quad \overline{\mathrm{a}}=\hat{\mathrm{i}}-\hat{\mathrm{k}}, \overline{\mathrm{b}}=x \hat{\mathrm{i}}+\hat{\mathrm{j}}+(1-x) \hat{\mathrm{k}} \quad$ and $\overline{\mathrm{c}}=y \hat{\mathrm{i}}+x \hat{\mathrm{j}}+(1+x-y) \hat{\mathrm{k}}$ then $\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})$ depends on

**Options:**

- **(A)** only $x$
- **(B)** only $y$
- **(C)** neither $x$ nor $y$
- **(D)** both $x$ and $y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) neither $x$ nor $y$**

**Detailed Solution:**

The scalar triple product $\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})$ is given by the determinant of the components of the vectors $\overline{\mathrm{a}}$, $\overline{\mathrm{b}}$, and $\overline{\mathrm{c}}$.

$\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}}) = \begin{vmatrix} 1 & 0 & -1 \\ x & 1 & 1-x \\ y & x & 1+x-y \end{vmatrix}$

Expanding the determinant along the first row:

$= 1 [1(1+x-y) - x(1-x)] - 0 + (-1) [x(x) - y(1)]$

$= [1 + x - y - x + x^2] - [x^2 - y]$

$= 1 - y + x^2 - x^2 + y$

$= 1$

Since the value is a constant, it depends on neither $x$ nor $y$.

Answer: neither $x$ nor $y$

</details>

---

### Q49. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overline{\mathrm{a}}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-2 \hat{\mathrm{k}}$ and $\overline{\mathrm{b}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}$. If $\overline{\mathrm{c}}$ is a vector such that $\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=|\overline{\mathrm{c}}|,|\overline{\mathrm{c}}-\overline{\mathrm{a}}|=2 \sqrt{2}$ and the angle between $(\overline{\mathrm{a}} \times \overline{\mathrm{b}})$ and $\overline{\mathrm{c}}$ is $30^{\circ}$, then the value of $|(\bar{a} \times \bar{b}) \times \bar{c}|$ is equal to

**Options:**

- **(A)** $\dfrac{\sqrt{3}}{2}$
- **(B)** $\dfrac{3}{2}$
- **(C)** $\dfrac{1}{\sqrt{2}}$
- **(D)** $\dfrac{\sqrt{3}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3}{2}$**

**Detailed Solution:**

Given $\bar{a} = 2\hat{i} + \hat{j} - 2\hat{k}$, we have $|\bar{a}| = \sqrt{2^2 + 1^2 + (-2)^2} = 3$.

We are given $|\bar{c} - \bar{a}| = 2\sqrt{2}$.

Squaring both sides, we get:

$|\bar{c}|^2 + |\bar{a}|^2 - 2\bar{a} \cdot \bar{c} = 8$

Substitute $|\bar{a}| = 3$ and $\bar{a} \cdot \bar{c} = |\bar{c}|$:

$|\bar{c}|^2 + 9 - 2|\bar{c}| = 8$

$|\bar{c}|^2 - 2|\bar{c}| + 1 = 0$

$(|\bar{c}| - 1)^2 = 0 \Rightarrow |\bar{c}| = 1$

Now, we find $\bar{a} \times \bar{b}$:

$\bar{a} \times \bar{b} = (2\hat{i} + \hat{j} - 2\hat{k}) \times (\hat{i} + \hat{j}) = 2\hat{i} - 2\hat{j} + \hat{k}$

The magnitude of this cross product is:

$|\bar{a} \times \bar{b}| = \sqrt{2^2 + (-2)^2 + 1^2} = 3$

The magnitude of the required vector is:

$|(\bar{a} \times \bar{b}) \times \bar{c}| = |\bar{a} \times \bar{b}| |\bar{c}| \sin 30^{\circ}$

$= 3 \times 1 \times \dfrac{1}{2} = \dfrac{3}{2}$

Answer: $\dfrac{3}{2}$

</details>

---

### Q50. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The volume of parallelopiped formed by vectors $\hat{i}+m \hat{j}+\hat{k}, \hat{j}+m \hat{k}$ and $m \hat{i}+\hat{k}$ becomes minimum when $m$ is

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** $\sqrt{3}$
- **(D)** $\dfrac{1}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{\sqrt{3}}$**

**Detailed Solution:**

The volume of the parallelopiped formed by the vectors $\vec{a}$, $\vec{b}$, and $\vec{c}$ is given by the scalar triple product $V = |[\vec{a} \quad \vec{b} \quad \vec{c}]|$.

Given vectors are:
$\vec{a} = \hat{i} + m\hat{j} + \hat{k}$
$\vec{b} = 0\hat{i} + \hat{j} + m\hat{k}$
$\vec{c} = m\hat{i} + 0\hat{j} + \hat{k}$

Calculating the scalar triple product:
$V = \left| \begin{matrix} 1 & m & 1 \\ 0 & 1 & m \\ m & 0 & 1 \end{matrix} \right|$

Expanding the determinant along the first row:
$V = |1(1 - 0) - m(0 - m^2) + 1(0 - m)|$
$V = |1 + m^3 - m|$

To find the minimum volume, we differentiate $V$ with respect to $m$ and equate it to zero:
$\dfrac{dV}{dm} = 3m^2 - 1 = 0$
$m^2 = \dfrac{1}{3}$
$m = \pm \dfrac{1}{\sqrt{3}}$

Now, checking the second derivative:
$\dfrac{d^2V}{dm^2} = 6m$

At $m = \dfrac{1}{\sqrt{3}}$, $\dfrac{d^2V}{dm^2} = \dfrac{6}{\sqrt{3}} > 0$, which indicates a local minimum.

Therefore, the volume becomes minimum when $m = \dfrac{1}{\sqrt{3}}$.

Answer: $\dfrac{1}{\sqrt{3}}$

</details>

---

### Q51. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The scalar $\overline{\mathrm{a}} \cdot[(\overline{\mathrm{b}}+\overline{\mathrm{c}}) \times(\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}})]$ equals

**Options:**

- **(A)** 0
- **(B)** $[\bar{a} \overline{\mathrm{~b}} \overline{\mathrm{c}}]+[\overline{\mathrm{b}} \overline{\mathrm{c}} \overline{\mathrm{a}}]$
- **(C)** $[\bar{a} \overline{\mathrm{~b}} \overline{\mathrm{c}}]$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

The given expression is $\overline{\mathrm{a}} \cdot [(\overline{\mathrm{b}} + \overline{\mathrm{c}}) \times (\overline{\mathrm{a}} + \overline{\mathrm{b}} + \overline{\mathrm{c}})]$.

Expanding the cross product, we get:

$(\overline{\mathrm{b}} + \overline{\mathrm{c}}) \times (\overline{\mathrm{a}} + \overline{\mathrm{b}} + \overline{\mathrm{c}}) = (\overline{\mathrm{b}} + \overline{\mathrm{c}}) \times \overline{\mathrm{a}} + (\overline{\mathrm{b}} + \overline{\mathrm{c}}) \times (\overline{\mathrm{b}} + \overline{\mathrm{c}})$

Since the cross product of any vector with itself is zero, $(\overline{\mathrm{b}} + \overline{\mathrm{c}}) \times (\overline{\mathrm{b}} + \overline{\mathrm{c}}) = 0$.

Thus, the expression simplifies to:

$\overline{\mathrm{a}} \cdot [(\overline{\mathrm{b}} + \overline{\mathrm{c}}) \times \overline{\mathrm{a}}]$

This represents the scalar triple product $[\overline{\mathrm{a}} \quad \overline{\mathrm{b}} + \overline{\mathrm{c}} \quad \overline{\mathrm{a}}]$.

Since two vectors in the scalar triple product are identical, its value is $0$.

Answer: 0

</details>

---

### Q52. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider $\overrightarrow{\mathrm{r}}, \overrightarrow{\mathrm{a}}, \overrightarrow{\mathrm{b}}$ and $\overrightarrow{\mathrm{c}}$ are non-zero vectors such that $\overrightarrow{\mathrm{r}} \cdot \overrightarrow{\mathrm{a}}=0$, $|\overrightarrow{\mathrm{r}} \times \overrightarrow{\mathrm{b}}|=|\overrightarrow{\mathrm{r}}||\overrightarrow{\mathrm{b}}|,|\overrightarrow{\mathrm{r}} \times \overrightarrow{\mathrm{c}}|=|\overrightarrow{\mathrm{r}}||\overrightarrow{\mathrm{c}}|$, then $[\overrightarrow{\mathrm{a}} \overrightarrow{\mathrm{b}} \overrightarrow{\mathrm{c}}]$ is

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** 4
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

Here, it is given in problem $|\overrightarrow{\mathrm{r}} \times \overrightarrow{\mathrm{b}}|=|\overrightarrow{\mathrm{r}}||\overrightarrow{\mathrm{b}}|$
So, it is clear that angle between $\overrightarrow{\mathrm{r}}$ and $\overrightarrow{\mathrm{b}}$ is $\frac{\pi}{2}$ $\overrightarrow{\mathrm{r}} \cdot \overrightarrow{\mathrm{a}}=0 \Rightarrow \overrightarrow{\mathrm{r}}$ is perpendicular to $\overrightarrow{\mathrm{a}}$. $|\overrightarrow{\mathrm{r}} \times \overrightarrow{\mathrm{c}}|=|\overrightarrow{\mathrm{r}}| \cdot|\overrightarrow{\mathrm{c}}| \Rightarrow \overrightarrow{\mathrm{r}}$ is perpendicular to $\overrightarrow{\mathrm{c}}$. Thus, $\overrightarrow{\mathrm{r}}$ is perpendicular to $\overrightarrow{\mathrm{a}}, \overrightarrow{\mathrm{b}}$ and $\overrightarrow{\mathrm{c}}$.
Hence, $\vec{a}, \vec{b}$ and $\vec{c}$ are coplanar.
$\Rightarrow[\overrightarrow{\mathrm{a}} \overrightarrow{\mathrm{b}} \overrightarrow{\mathrm{c}}]=0$

</details>

---

### Q53. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The scalar product of vectors $\bar{a}=\hat{i}+2 \hat{j}+\hat{k}$ and a unit vector along the sum of vectors $\overline{\mathrm{b}}=2 \hat{\mathrm{i}}-4 \hat{\mathrm{j}}+5 \hat{\mathrm{k}}$ and $\overline{\mathrm{c}}=\lambda \hat{\mathrm{i}}+2 \hat{\mathrm{j}}-3 \hat{\mathrm{k}}$ is one, then the value of $\lambda$ is

**Options:**

- **(A)** 1
- **(B)** -2
- **(C)** -3
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -3**

**Detailed Solution:**

$$
\begin{aligned}
& \overline{\mathrm{b}}+\overline{\mathrm{c}}=(2+\lambda) \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+2 \hat{\mathrm{k}} \\
& \text { Unit vector }=\frac{\overline{\mathrm{b}}+\overline{\mathrm{c}}}{\sqrt{\overline{\mathrm{b}}+\overline{\mathrm{c}}}} \\
& =\frac{(2+\lambda) \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}}{\sqrt{(2+\lambda)^2+(-2)^2+2^2}} \\
& =\frac{(2+\lambda) \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}}{\sqrt{\lambda^2+4 \lambda+12}}
\end{aligned}
$$
According to the given condition,
$$
\begin{aligned}
& (\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}}) \cdot\left(\frac{(2+\lambda) \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}}{\sqrt{\lambda^2+4 \lambda+12}}\right)=1 \\
& \Rightarrow \frac{(2+\lambda)-4+2}{\sqrt{\lambda^2+4 \lambda+12}}=1 \\
& \Rightarrow \lambda=\sqrt{\lambda^2+4 \lambda+12} \\
& \Rightarrow \lambda^2=\lambda^2+4 \lambda+12 \\
& \Rightarrow 4 \lambda=-12 \\
& \Rightarrow \lambda=-3
\end{aligned}
$$

</details>

---

### Q54. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the volume of tetrahedron, whose vertices are $\mathrm{A}(1,2,3), \mathrm{B}(-3,-1,1), \mathrm{C}(2,1,3)$ and $\mathrm{D}(-1,2, x)$ is $\frac{11}{6}$ cubic units, then the value of $x$ is

**Options:**

- **(A)** $3$
- **(B)** $-2$
- **(C)** $4$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4$**

**Detailed Solution:**

$\begin{aligned} & \overline{\mathrm{AB}}=-4 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}-2 \hat{\mathrm{k}} \\ & \overline{\mathrm{AC}}=\hat{\mathrm{i}}-\hat{\mathrm{j}} \\ & \overline{\mathrm{AD}}=-2 \hat{\mathrm{i}}+(x-3) \hat{\mathrm{k}} \\ & \text { Volume }=\frac{1}{6}\left|\begin{array}{ccc}-4 & -3 & -2 \\ 1 & -1 & 0 \\ -2 & 0 & x-3\end{array}\right| \\ \therefore \quad & 11=4(x-3)+3(x-3)-2(-2) \\ \therefore \quad & 11=7 x-17\end{aligned}$

</details>

---

### Q55. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The centroid of tetrahedron with vertices at $A(-1,2,3), B(3,-2,1), C(2,1,3)$ and $D(-1,-2,4)$ is

**Options:**

- **(A)** $\left(\frac{3}{4}, \frac{-1}{4}, \frac{11}{4}\right)$
- **(B)** $\left(\frac{5}{4}, \frac{-3}{4}, \frac{7}{4}\right)$
- **(C)** $\left(\frac{-3}{4}, \frac{-1}{4}, \frac{11}{4}\right)$
- **(D)** $\left(\frac{-5}{4}, \frac{-3}{4}, \frac{-7}{4}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(\frac{3}{4}, \frac{-1}{4}, \frac{11}{4}\right)$**

**Detailed Solution:**

Centroid of tetrahedron
$$
\begin{aligned}
& \equiv\left(\frac{-1+3+2-1}{4}, \frac{2-2+1-2}{4}, \frac{3+1+3+4}{4}\right) \\
& \equiv\left(\frac{3}{4}, \frac{-1}{4}, \frac{11}{4}\right)
\end{aligned}
$$

</details>

---

### Q56. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the volume of the parallelopiped is $158 \mathrm{cu}$. units whose coterminus edges are given by the vectors $\bar{a}=(\hat{i}+\hat{j}+n \hat{k}), \bar{b}=2 \hat{i}+4 \hat{j}-n \hat{k}$ and $\bar{c}=\hat{i}+n \hat{j}+3 \hat{k}$, where $n \geq 0$, then the value of $n$ is

**Options:**

- **(A)** $8$
- **(B)** $\frac{19}{3}$
- **(C)** $7$
- **(D)** $19$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $8$**

**Detailed Solution:**

$\begin{aligned} & \text { Volume of parallelopiped }=\left|\begin{array}{ccc}1 & 1 & n \\ 2 & 4 & -n \\ 1 & n & 3\end{array}\right|=158 \\ & \Rightarrow 1\left(12+n^2\right)-1(6+n)+n(2 n-4)-158 \\ & \Rightarrow 3 n^2-5 n-152=0 \\ & \Rightarrow(3 n+19)(n-8)=0 \\ & \Rightarrow n=8\end{aligned}$

</details>

---

### Q57. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\alpha$, so that the volume of parallelopiped formed by $\hat{i}+\alpha \hat{j}+\hat{k}, \hat{j}+\alpha \hat{k}$ and $\alpha \hat{\mathrm{i}}+\hat{\mathrm{k}}$ becomes minimum, is

**Options:**

- **(A)** $-3$
- **(B)** $3$
- **(C)** $\frac{1}{\sqrt{3}}$
- **(D)** $-\frac{1}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{\sqrt{3}}$**

**Detailed Solution:**

Volume of parallelopiped $=\left|\begin{array}{ccc}1 & \alpha & 1 \\ 0 & 1 & \alpha \\ \alpha & 0 & 1\end{array}\right|$
$\therefore \quad \mathrm{V}=1+\alpha^3-\alpha$
For maxima or minima,
$\begin{aligned}
& \frac{\mathrm{dV}}{\mathrm{d} \alpha}=0 \\
& \Rightarrow 3 \alpha^2-1=0 \\
& \Rightarrow \alpha= \pm \frac{1}{\sqrt{3}}
\end{aligned}$
Now, $\frac{\mathrm{d}^2 \mathrm{~V}}{\mathrm{~d} \alpha^2}=6 \alpha$
For $\alpha=\frac{1}{\sqrt{3}}$,
$\frac{\mathrm{d}^2 \mathrm{~V}}{\mathrm{~d} x^2}>0$
$\therefore \quad \mathrm{V}$ is minimum at $\alpha=\frac{1}{\sqrt{3}}$.

</details>

---

### Q58. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the volume of tetrahedron, whose vertices are with position vectors $\hat{i}-6 \hat{j}+10 \hat{k},-\hat{i}-3 \hat{j}+7 \hat{k}$, $5 \hat{i}-\hat{j}+\lambda \hat{k}$ and $7 \hat{i}-4 \hat{j}+7 \hat{k}$ is 11 cubic units, then value of $\lambda$ is

**Options:**

- **(A)** $4$
- **(B)** $5$
- **(C)** $7$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $7$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \overline{\mathrm{a}}=\hat{\mathrm{i}}-6 \hat{\mathrm{j}}+10 \hat{\mathrm{k}} \text {, } \\ & \overline{\mathrm{b}}=-\hat{\mathrm{i}}-3 \hat{\mathrm{j}}+7 \hat{\mathrm{k}} \text {, } \\ & \overline{\mathrm{c}}=5 \hat{\mathrm{i}}-\hat{\mathrm{j}}+\lambda \hat{\mathrm{k}} \text {, } \\ & \overline{\mathrm{d}}=7 \hat{\mathrm{i}}-4 \hat{\mathrm{j}}+7 \hat{\mathrm{k}} \\ & \therefore \quad \overline{\mathrm{AB}}=-2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}-3 \hat{\mathrm{k}} \\ & \overline{\mathrm{AC}}=4 \hat{\mathrm{i}}+5 \hat{\mathrm{j}}+(\lambda-10) \hat{\mathrm{k}} \\ & \overline{\mathrm{AD}}=6 \hat{\mathrm{i}}+2 \hat{\mathrm{j}}-3 \hat{\mathrm{k}} \\ & \therefore \quad \text { Volume of tetrahedron }=\frac{1}{6}\left[\begin{array}{lll}\overline{\mathrm{AB}} & \overline{\mathrm{AC}} & \overline{\mathrm{AD}}\end{array}\right] \\ & \Rightarrow 11=\frac{1}{6}\left|\begin{array}{ccc}-2 & 3 & -3 \\ 4 & 5 & \lambda-10 \\ 6 & 2 & -3\end{array}\right| \\ & \Rightarrow 11=\frac{1}{6}\{-2(-15-2 \lambda+20)-3(-12-6 \lambda+60) \\  & -3(8-30)\} \\ & \Rightarrow \lambda=7& \end{aligned}$

</details>

---

### Q59. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}, \bar{b}$ and $\bar{c}$ are any three non-zero vectors, then $(\bar{a}+2 \bar{b}+\bar{c}) \cdot[(\bar{a}-\bar{b}) \times(\bar{a}-\bar{b}-\bar{c})]=$

**Options:**

- **(A)** $\left[\begin{array}{lll}\bar{a} & \bar{b} & \bar{c}\end{array}\right]$
- **(B)** $2\left[\begin{array}{lll}-\bar{a} & \bar{b} & \bar{c}\end{array}\right]$
- **(C)** $3\left[\begin{array}{lll}\bar{a} & \bar{b} & \bar{c}\end{array}\right]$
- **(D)** $4\left[\begin{array}{lll}\vec{a} & \bar{b} & \bar{c}\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3\left[\begin{array}{lll}\bar{a} & \bar{b} & \bar{c}\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & (\bar{a}+2 \bar{b}+\bar{c}) \cdot[(\bar{a}-\bar{b}) \times(\bar{a}-\bar{b}-\bar{c})] \\ & =(\bar{a}+2 \bar{b}+\bar{c}) \cdot(\bar{a} \times \bar{a}-\bar{a} \times \bar{b}-\bar{a} \times \bar{c}-\bar{b} \times \bar{a}+\bar{b} \times \bar{b}+\bar{b} \times \bar{c}) \\ & =(\bar{a}+2 \bar{b}+\bar{c}) \cdot(\overline{0}-\bar{a} \times \bar{b}-\bar{a} \times \bar{c}+\bar{a} \times \bar{b}+\overline{0}+\bar{b} \times \bar{c}) \\ & =(\overline{\mathrm{a}}+2 \overline{\mathrm{b}}+\overline{\mathrm{c}}) \cdot(\overline{\mathrm{c}} \times \overline{\mathrm{a}}+\overline{\mathrm{b}} \times \overline{\mathrm{c}}) \\ & =\bar{a} \cdot(\bar{c} \times \bar{a})+\bar{a} \cdot(\bar{b} \times \bar{c})+2 \bar{b} \cdot(\bar{c} \times \bar{a})+2 \bar{b} \cdot(\bar{b} \times \bar{c}) \\ & +\overline{\mathrm{c}} \cdot(\overline{\mathrm{c}} \times \overline{\mathrm{a}})+\overline{\mathrm{c}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}}) \\ & =\overline{0}+\bar{a} \cdot(\bar{b} \times \bar{c})+2 \bar{b} \cdot(\bar{c} \times \bar{a})+2 \times 0-0-0 \\ & =\left[\begin{array}{lll}\overline{\mathrm{a}} & \overline{\mathrm{b}} & \overline{\mathrm{c}}\end{array}\right]+2\left[\begin{array}{lll}\overline{\mathrm{b}} & \overline{\mathrm{c}} & \overline{\mathrm{a}}\end{array}\right] \\ & =\left[\begin{array}{lll}\overline{\mathrm{a}} & \overline{\mathrm{b}} & \overline{\mathrm{c}}\end{array}\right]+2\left[\begin{array}{lll}\overline{\mathrm{a}} & \overline{\mathrm{b}} & \overline{\mathrm{c}}\end{array}\right] \\ & =3\left[\begin{array}{lll}\overline{\mathrm{a}} & \overline{\mathrm{b}} & \overline{\mathrm{c}}\end{array}\right] \\ & \end{aligned}$

</details>

---

### Q60. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The volume of parallelopiped, whose coterminous edges are given by $\bar{u}=\hat{i}+\hat{j}+\lambda \hat{k}$, $\bar{v}=\hat{i}+\hat{j}+3 \hat{k}, \bar{w}=2 \hat{i}+\hat{j}+\hat{k}$ is 1 cu. units. If $\theta$ is the angle between $\bar{u}$ and $\bar{w}$, then the value of $\cos \theta$ is

**Options:**

- **(A)** $\frac{3}{4}$
- **(B)** $\frac{5}{6}$
- **(C)** $\frac{1}{5}$
- **(D)** $\frac{1}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5}{6}$**

**Detailed Solution:**

$\begin{aligned} & \text { Volume of parallelepiped }=\left[\begin{array}{lll}\overrightarrow{\mathrm{u}} & \overrightarrow{\mathrm{v}} & \overrightarrow{\mathrm{w}}\end{array}\right] \\ & \quad\left|\begin{array}{lll}1 & 1 & \lambda \\ 1 & 1 & 3 \\ 2 & 1 & 1\end{array}\right|=1 \\ & \Rightarrow \lambda=2 \\ & \therefore \quad \cos \theta=\frac{2+1+2}{\sqrt{6} \cdot \sqrt{6}}=\frac{5}{6}\end{aligned}$

</details>

---

### Q61. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $[(\overline{\mathrm{a}}+2 \overline{\mathrm{b}}+3 \overline{\mathrm{c}}) \times(\overline{\mathrm{b}}+2 \overline{\mathrm{c}}+3 \overline{\mathrm{a}})] \cdot(\overline{\mathrm{c}}+2 \overline{\mathrm{a}}+3 \overline{\mathrm{b}})=54$, then the value of $\left[\begin{array}{lll}\bar{a} & \bar{b} & \bar{c}\end{array}\right]$ is

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 3
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

R.H.S. of the given equality can be written as
$\begin{aligned}
&(2 \overline{\mathrm{a}}+3 \overline{\mathrm{b}}+\overline{\mathrm{c}}) \cdot[(\overline{\mathrm{a}}+2 \overline{\mathrm{b}}+3 \overline{\mathrm{c}}) \times(3 \overline{\mathrm{a}}+\overline{\mathrm{b}}+2 \overline{\mathrm{c}})] \\
&=(2 \overline{\mathrm{a}}+3 \overline{\mathrm{b}}+\overline{\mathrm{c}}) \cdot[3(\overline{\mathrm{a}} \times \overline{\mathrm{a}})+(\overline{\mathrm{a}} \times \overline{\mathrm{b}})+2(\overline{\mathrm{a}} \times \overline{\mathrm{c}}) \\
&+6(\overline{\mathrm{b}} \times \overline{\mathrm{a}})+2(\overline{\mathrm{b}} \times \overline{\mathrm{b}})+4(\overline{\mathrm{b}} \times \overline{\mathrm{c}}) \\
&+9(\overline{\mathrm{c}} \times \overline{\mathrm{a}})+3(\overline{\mathrm{c}} \times \overline{\mathrm{b}})+6(\overline{\mathrm{c}} \times \overline{\mathrm{c}})] \\
&=(2 \overline{\mathrm{a}}+3 \overline{\mathrm{b}}+\overline{\mathrm{c}})[0+(\overline{\mathrm{a}} \times \overline{\mathrm{b}})+2(\overline{\mathrm{a}} \times \overline{\mathrm{c}}) \\
&-6(\overline{\mathrm{a}} \times \overline{\mathrm{b}})+0+4(\overline{\mathrm{b}} \times \overline{\mathrm{c}}) \\
&=(2 \overline{\mathrm{a}}+3 \overline{\mathrm{b}}+\overline{\mathrm{c}})[-5(\overline{\mathrm{a}} \times \overline{\mathrm{c}})-3(\overline{\mathrm{b}} \times \overline{\mathrm{c}})+(\overline{\mathrm{b}} \times \overline{\mathrm{c}})-7(\overline{\mathrm{a}} \times \overline{\mathrm{c}})] \\
&=-10[\overline{\mathrm{a}} \cdot(\overline{\mathrm{a}} \times \overline{\mathrm{b}})]+2[\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})]-14[\overline{\mathrm{a}} \cdot(\overline{\mathrm{a}} \times \overline{\mathrm{c}})] \\
&-15[\overline{\mathrm{b}} \cdot(\overline{\mathrm{a}} \times \overline{\mathrm{b}})]+3[\overline{\mathrm{b}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})]-21[\overline{\mathrm{b}} \cdot(\overline{\mathrm{a}} \times \overline{\mathrm{c}})] \\
&-5[\overline{\mathrm{c}} \cdot(\overline{\mathrm{a}} \times \overline{\mathrm{b}})]+[\overline{\mathrm{c}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})]-7[\overline{\mathrm{c}} \cdot(\overline{\mathrm{a}} \times \overline{\mathrm{c}})] \\
&= 0+2[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]+0 \\
&+0+0 \\
&=-5[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]+0+21[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}] \\
&= 18[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}} \overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]=54
\end{aligned}$
$\Rightarrow[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]=3$

</details>

---

### Q62. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The scalar product of the vector $\hat{i}+\hat{j}+\hat{k}$ with a unit vector along the sum of the vectors $2 \hat{i}+4 \hat{j}-5 \hat{k}$ and $\lambda \hat{i}+2 \hat{j}+3 \hat{k}$ is equal to 1 , then value of $\lambda$ is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$(2 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}-5 \hat{\mathrm{k}})+(\lambda \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}})=(2+\lambda) \hat{\mathrm{i}}+6 \hat{\mathrm{j}}-2 \hat{\mathrm{k}}$
Unit vector along the above vector is
$\frac{(2+\lambda) \hat{i}+6 \hat{j}-2 \hat{k}}{\sqrt{(2+\lambda)^2+6^2+(-2)^2}}=\frac{(2+\lambda) \hat{i}+6 \hat{j}-2 \hat{k}}{\sqrt{\lambda^2+4 \lambda+44}}$
Scalar product of $(\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}})$ with this unit vector is 1 .
$\begin{aligned}
\therefore \quad & (\hat{i}+\hat{j}+\hat{k}) \cdot \frac{(2+\lambda) \hat{i}+6 \hat{j}-2 \hat{k}}{\sqrt{\lambda^2+4 \lambda+44}}=1 \\
& \frac{(2+\lambda)+6-2}{\sqrt{\lambda^2+4 \lambda+44}}=1 \\
& \sqrt{\lambda^2+4 \lambda+44}=\lambda+6 \\
\therefore \quad & \lambda^2+4 \lambda+44=(\lambda+6)^2 \\
& 8 \lambda=8 \\
& \lambda=1
\end{aligned}$

</details>

---

### Q63. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\alpha$, so that the volume of the parallelopiped formed by $\hat{i}+\alpha \hat{j}+\hat{k}, \hat{j}+\alpha \hat{k}$ and $\alpha \hat{\mathrm{i}}+\hat{\mathrm{k}}$ becomes maximum, is

**Options:**

- **(A)** $\frac{-1}{\sqrt{3}}$
- **(B)** $\frac{1}{\sqrt{3}}$
- **(C)** $-\sqrt {3}$
- **(D)** $\sqrt {3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-1}{\sqrt{3}}$**

**Detailed Solution:**

Volume of parallelopiped is $[\vec{a} \vec{b} \vec{c}]$
$\begin{aligned}
\therefore \quad V & =\left|\begin{array}{ccc}
1 & \alpha & 1 \\
0 & 1 & \alpha \\
\alpha & 0 & 1
\end{array}\right| \\
& =1-\alpha\left(-\alpha^2\right)-\alpha \\
& =1+\alpha^3-\alpha
\end{aligned}$
Differentiating w.r.t. $\alpha$, we get
$\begin{aligned}
& \frac{\mathrm{dV}}{\mathrm{d} \alpha}=3 \alpha^2-1 \\
\therefore \quad & \frac{\mathrm{d}^2 \mathrm{~V}}{\mathrm{~d} \alpha^2}=6 \alpha \\
& \text { Let } \frac{\mathrm{dV}}{\mathrm{d} \alpha}=0 \\
\therefore \quad & 3 \alpha^2-1=0 \\
\therefore \quad & \alpha= \pm \frac{1}{\sqrt{3}} \\
& \text { at } \alpha=\frac{-1}{\sqrt{3}}, \\
& \frac{\mathrm{d}^2 \mathrm{~V}}{\mathrm{~d} \alpha^2}=\frac{-6}{\sqrt{3}} < 0
\end{aligned}$
$\therefore \quad \mathrm{V}$ is maximum at $\alpha=\frac{-1}{\sqrt{3}}$

</details>

---

### Q64. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$|\vec{a}|=\sqrt{3},|\vec{b}|=5, \vec{b} \cdot \vec{c}=10$ and angle between $\bar{b}$ and $\bar{c}$ is $\left(\frac{\pi}{3}\right)$. If $\vec{a}$ is perpendicular to $\vec{b} \times \vec{c}$, then value of $|\vec{a} \times(\vec{b} \times \vec{c})|$ is

**Options:**

- **(A)** $15$
- **(B)** $10 \sqrt{3}$
- **(C)** $30$
- **(D)** $10$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $30$**

**Detailed Solution:**

$|\vec{a} \times(\vec{b} \times \vec{c})|=|\vec{a}| \times|\vec{b} \times \vec{c}| \sin \frac{\pi}{2}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Po6Dq17N8cMNtx6KzyQHteRyvRyClFSs0XXhzWfyeL8.original.fullsize.png">
from (i) and (ii) $|\vec{a} \times(\vec{b} \times \vec{c})|=\frac{15}{2} \times 4=30$

</details>

---

### Q65. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $a$, so that the volume of parallelepiped formed by $\hat{i}+a \hat{j}+\hat{k}, \hat{j}+a \hat{k}$ and $a \hat{i}+\hat{k}$ becomes minimum is

**Options:**

- **(A)** $\frac{1}{\sqrt{3}}$
- **(B)** 3
- **(C)** -3
- **(D)** $\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\sqrt{3}}$**

**Detailed Solution:**

Volume of parallelepiped $=\left|\begin{array}{lll}1 & a & 1 \\ 0 & 1 & a \\ a & 0 & 1\end{array}\right|=a^3-a+1=V(a)$
Now $V^{\prime}(a)=3 a^2-1$
$\stackrel{+}{\stackrel{\max .}{1}-\min _1^1+\frac{1}{\sqrt{3}} \frac{1}{\sqrt{3}}}$
$\Rightarrow$ volume is minimum at $x=\frac{1}{\sqrt{3}}$

</details>

---

### Q66. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The volume of the tetrahedron having vertices $(1,-6,10)$, $(-1,-3,7),(5,-1, \lambda)$ and $(7,-4,7)$ is $11 \mathrm{cu}$. Units, then $\lambda=$

**Options:**

- **(A)** 3
- **(B)** 1
- **(C)** 5
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 7**

**Detailed Solution:**

$\begin{aligned} & \text { Volume of a tetrahedron }=\frac{1}{6}\left|\begin{array}{lll}x_2-x_1 & y_2-y_1 & z_2-z_1 \\ x_3-x_1 & y_3-y_1 & z_3-z_1 \\ x_4-x_1 & y_4-y_1 & z_4-z_1\end{array}\right| \\ & =\frac{1}{6}\left|\begin{array}{ccc}-2 & 3 & -3 \\ 4 & 5 & \lambda-10 \\ 6 & 2 & -3\end{array}\right| \\ & \Rightarrow 11=\frac{1}{6}\{22 \lambda-88\} \Rightarrow \lambda=7\end{aligned}$

</details>

---

### Q67. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{a}=\hat{i}-\hat{k}, \vec{b}=x \hat{i}+\hat{j}+(1-x) \hat{k} \quad$ and $\quad \vec{c}=y \hat{i}+x \hat{j}+(1+x-y) \hat{k}$ then $[\vec{a} \vec{b} \vec{c}]$ depends on

**Options:**

- **(A)** neither $x$ nor $y$
- **(B)** only $x$
- **(C)** only $y$
- **(D)** both $x$ and $y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) neither $x$ nor $y$**

**Detailed Solution:**

$\begin{aligned} & {[\vec{a} \vec{b} \vec{c}]=\left|\begin{array}{ccc}1 & 0 & -1 \\ x & 1 & 1-x \\ y & x & 1+x-y\end{array}\right|=\left|\begin{array}{ccc}0 & 0 & -1 \\ 1 & 1 & 1-x \\ 1+x & x & 1+x-y\end{array}\right|} \\ & =-1(x-1-x) \\ & =1 \text { which is independent of both } x \text { and } y\end{aligned}$

</details>

---

### Q68. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $|\overline{\mathrm{a}}|=5,|\overline{\mathrm{b}}|=3,|\overline{\mathrm{c}}|=4$ and $\overline{\mathrm{a}}$ is perpendicular to $\overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ such that angle between $\bar{b}$ and $\bar{c}$ is $\frac{5 \pi}{6}$, then $[\bar{a} \bar{b} \bar{c}]=$

**Options:**

- **(A)** 25
- **(B)** 10
- **(C)** 30
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 30**

**Detailed Solution:**

$[\vec{a} \vec{b} \vec{c}]=|\vec{a}||\vec{b}||\vec{c}| \cdot(\cos$ of angle between $\vec{a}$ and $\vec{b} \times \vec{c})$.(sin of angle between $\vec{b}$ and $\vec{c}$ )
$\begin{aligned} & =5 \times 3 \times 4 \times \cos 0 \times \sin \left(\frac{5 \pi}{6}\right) \\ & =60 \times 1 \times \frac{1}{2}=30\end{aligned}$

</details>

---

### Q69. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A plane is parallel to two lines direction ratios are $(1,0,-1)$ and $(-1,1,0)$ and it contains the point $(1,1,1)$. If it cuts the co-ordinate axes at A, B, C, then the volume of the tetrahedron $\mathrm{OABC}$ is cu. units.

**Options:**

- **(A)** $9$
- **(B)** $27$
- **(C)** $\frac{9}{4}$
- **(D)** $\frac{9}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{9}{2}$**

**Detailed Solution:**

Direction ration of normal to the plane can be obtained by
$\begin{aligned} & \frac{\mathrm{a}}{0 \times 0-1 \times(-1)}=\frac{\mathrm{b}}{(-1) \times(-1)-1 \times 0}=\frac{\mathrm{c}}{1 \times 1-(-1) \times 0} \\ & \Rightarrow\langle\mathrm{a}, \mathrm{b}, \mathrm{c}\rangle \equiv\langle 1,1,1\rangle\end{aligned}$
Hence equation of the plane $1(x-1)+1(y-1)+1(z-1)=0$
$\begin{aligned} & \Rightarrow x+y+z=3 \\ & \Rightarrow \frac{x}{3}+\frac{y}{3}+\frac{z}{3}=1\end{aligned}$
$\Rightarrow$ The plane intersects the co-ordinate axes at $(3,0,0),(0,3,0)$ and $(0,0,3)$
Hence, volume of tetrahedron OABC is

</details>

---

### Q70. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For any non-zero vectors $\bar{a}, \bar{b}, \bar{c}$, the value $\overline{\mathrm{a}} \cdot[(\overline{\mathrm{b}} \times \overline{\mathrm{c}}) \times(\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}})]$ is

**Options:**

- **(A)** $2[\bar{a} \bar{b} \bar{c}]$
- **(B)** $[\bar{a} \bar{b} \bar{c}]$
- **(C)** $[\overline{\mathrm{a}} \overline{\mathrm{c}} \overline{\mathrm{b}}]$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

$\begin{aligned} & \bar{a} \cdot[(\bar{b} \times \bar{c}) \times(\bar{a}+\bar{b}+\bar{c})] \\ & =\bar{a} \cdot[(\bar{b} \times \bar{a})+(\bar{b} \times \bar{b})+(\bar{b} \times \bar{c})+(\bar{c} \times \bar{a})+(\bar{c} \times \bar{b})+(\bar{c} \times \bar{c})] \\ & =\bar{a} \cdot(\bar{b} \times \bar{a})+\bar{a} \cdot(0)+\bar{a} \cdot(\bar{b} \times \bar{c})+\bar{a} \cdot(\bar{c} \times \bar{a})+\bar{a} \cdot(\bar{c} \times \bar{b})+\bar{a} \cdot(0) \\ & =0+\bar{a} \cdot(\bar{b} \times \bar{c})+0-\bar{a} \cdot(\bar{b} \times \bar{c})=0\end{aligned}$

</details>

---

### Q71. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\bar{a}+\bar{b}, \bar{b}+\bar{c}, \bar{c}+\bar{a}$ are coterminous edges of a parallelepiped, then its volume is

**Options:**

- **(A)** 0
- **(B)** $4[\overline{\mathrm{b}} \overline{\mathrm{a}} \overline{\mathrm{c}}]$
- **(C)** $3[\bar{a} \bar{c} \bar{b}]$
- **(D)** $2[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$**

**Detailed Solution:**

The volume of required parallelepiped
$\begin{aligned}
& =(\bar{a}+\bar{b}) \cdot[(\bar{b}+\bar{c}) \times(\bar{c}+\bar{a})] \\
& =(\bar{a}+\bar{b}) \cdot[(\bar{b} \times \bar{c})+(\bar{b} \times \bar{a})+(\bar{c} \times \bar{c})+(\bar{c} \times \bar{a})] \\
& =[\bar{a} \cdot(\bar{b} \times \bar{c})]+[\bar{a} \cdot(\bar{b} \times \bar{a})]+0+[\bar{a} \times(\bar{c} \times \bar{a})] \\
& +[\bar{b} \cdot(\bar{b} \times \bar{a})]+0+[\bar{b} \cdot(\bar{c} \times \bar{a})] \\
& =[\bar{a} \cdot(\bar{b} \times \bar{c})]+0+0+0+0+0+0+[\bar{b} \cdot(\bar{c} \times \bar{a})] \\
& =2 \bar{a} \cdot(\bar{b} \times \bar{c})
\end{aligned}$

</details>

---

### Q72. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{v}=2 \hat{i}+2 \hat{j}-\hat{k}$ and $\bar{w}=\hat{i}+3 \hat{k}$. If $\bar{u}$ is a unit vector, then the maximum value of the scalar triple product $[\overline{\mathrm{u}} \overline{\mathrm{v}} \overline{\mathrm{W}}]$ is

**Options:**

- **(A)** $\sqrt{6}$
- **(B)** $\sqrt{10}$
- **(C)** $\sqrt{13}$
- **(D)** $\sqrt{89}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{89}$**

**Detailed Solution:**

$\begin{aligned} & \overline{\mathrm{v}} \times \overline{\mathrm{w}}=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 2 & 2 & -1 \\ 1 & 0 & 3\end{array}\right|=\hat{\mathrm{i}}(6)-\hat{\mathrm{j}}(7)+\hat{\mathrm{k}}(-2)=6 \hat{\mathrm{i}}-7 \hat{\mathrm{j}}-2 \hat{\mathrm{k}} \\ & \therefore|\overline{\mathrm{v}} \times \overline{\mathrm{w}}|=\sqrt{(6)^2+(7)^2+(2)^2}=\sqrt{89} \\ & \text { Also }|\overline{\mathrm{u}}|=1 \\ & \therefore[\overline{\mathrm{u}} \overline{\mathrm{v}} \overline{\mathrm{w}}]=\sqrt{89}\end{aligned}$

</details>

---

### Q73. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the volume of a tetrahedron whose conterminous edges are $\bar{a}+\bar{b}, \bar{b}+\bar{c}, \bar{c}+\bar{a}$ is 24 cubic units, then the volume of parallelepiped whose coterminous edges are $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}$ is

**Options:**

- **(A)** 48 cubic units
- **(B)** 144 cubic units
- **(C)** 72 cubic units
- **(D)** 10 cubic units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 72 cubic units**

**Detailed Solution:**

As per data given, we write
$$
\begin{aligned}
& 24=\frac{1}{6}\{(\overline{\mathrm{a}}+\overline{\mathrm{b}}) \cdot[(\overline{\mathrm{b}}+\overline{\mathrm{c}}) \times(\overline{\mathrm{c}}+\overline{\mathrm{a}})]\} \\
& =\frac{1}{6}\{(\overline{\mathrm{a}}+\overline{\mathrm{b}}) \cdot[(\overline{\mathrm{b}} \times \overline{\mathrm{c}})+(\overline{\mathrm{b}}+\overline{\mathrm{a}})+(\overline{\mathrm{c}} \times \overline{\mathrm{a}})]\} \quad \ldots[\because \overline{\mathrm{c}} \times \overline{\mathrm{c}}=0] \\
& \therefore 144=[\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})]+[\overline{\mathrm{b}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})]+[\overline{\mathrm{b}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{a}})]+[\overline{\mathrm{a}} \cdot(\overline{\mathrm{c}} \times \overline{\mathrm{a}})]+[\overline{\mathrm{b}} \cdot(\overline{\mathrm{c}} \times \overline{\mathrm{a}})] \\
& =[\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})]+0+0+0+0[\overline{\mathrm{b}}(\overline{\mathrm{c}} \times \overline{\mathrm{a}})] \\
& =2[\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})] \quad \ldots[\because \overline{\mathrm{b}}(\overline{\mathrm{c}} \times \overline{\mathrm{a}})=\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})] \\
& \therefore \overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})=72, \text { i.e. volume of parallelepiped with } \\
& \text { conterminous edges } \overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}} .
\end{aligned}
$$

</details>

---

### Q74. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}, \bar{b}, \bar{c}$ are non $-$ coplanar vectos and $(\overline{\mathrm{a}}+\overline{\mathrm{b}}+\overline{\mathrm{c}}) \cdot(\overline{\mathrm{a}} \times \overline{\mathrm{b}}+\overline{\mathrm{b}} \times \overline{\mathrm{c}}+\overline{\mathrm{c}} \times \overline{\mathrm{a}})=\mathrm{k}[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]$,
then value of $\mathrm{k}$ is

**Options:**

- **(A)** 4
- **(B)** 1
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

$\begin{aligned} &(\bar{a}+\bar{b}+\bar{c}) \cdot[(\bar{a} \times \bar{b})+(\mathrm{b} \times \bar{c})+(\bar{c} \times \bar{a})] \\=&[\bar{a} \cdot(\bar{a} \times \bar{b})]+[\bar{a} \cdot(\bar{b} \times \bar{c})]+[\bar{a} \cdot(\bar{c} \times \bar{a})]+[\bar{b} \cdot(\bar{a} \times \bar{b})]+[\bar{b} \cdot(\bar{b} \times \bar{c})] \\ &+[\bar{b} \cdot(\bar{c} \times \bar{a})]+[\bar{c} \cdot(\bar{a} \times \bar{b})]+[\bar{c} \cdot(\bar{b} \times \bar{c})]+[\bar{c} \cdot(\bar{c} \times \bar{a})] \\=& 0+[\bar{a} \cdot(\bar{b} \times \bar{c})]+0+0+0+[\bar{b} \cdot(\bar{c} \times \bar{a})]+[\bar{c} \cdot(\bar{a} \times \bar{b})]+0+0 \\=& 3[\bar{a} \cdot(\bar{b} \times \bar{c})]=3\left[\begin{array}{lll}a & \bar{b} & \bar{c}\end{array}\right] \Rightarrow \mathrm{k}=3 \end{aligned}$

</details>

---

### Q75. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}, \bar{b}, \bar{c}$ are non-coplanar vectors and $\bar{p}=\frac{\bar{b} \times \bar{c}}{[\bar{a} \bar{b} \bar{c}]}, \bar{q}=\frac{\bar{c} \times \bar{a}}{[a} \bar{b} \overline{c]}, \bar{r}=\frac{\bar{a} \times \bar{b}}{[\bar{a} \bar{b} \bar{c}]}$,
then $\bar{a} \cdot \bar{p}+\bar{b} \cdot \bar{q}+\bar{c} \cdot \bar{r}=$

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** 0
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

(C)
Given that,
$\overline{\mathrm{p}}=\frac{\overline{\mathrm{b}} \times \overline{\mathrm{c}}}{\left[\begin{array}{ccc}\overline{\mathrm{a}} & \overline{\mathrm{b}} & \overline{\mathrm{c}}\end{array}\right]}, \quad \overline{\mathrm{q}}=\frac{\overline{\mathrm{c}} \times \overline{\mathrm{a}}}{\left[\begin{array}{ccc}\overline{\mathrm{a}} & \overline{\mathrm{b}} & \overline{\mathrm{c}}\end{array}\right], \quad \mathrm{r}}=\frac{\overline{\mathrm{a}} \times \overline{\mathrm{b}}}{\left[\begin{array}{lll}\overline{\mathrm{a}} & \overline{\mathrm{b}} & \overline{\mathrm{c}}\end{array}\right]}$
$\bar{a} \cdot \bar{p}=\frac{\bar{a} \cdot(\bar{b} \times \bar{c})}{\left[\begin{array}{lll}\bar{a} & \bar{b} & \bar{c}\end{array}\right]}=1$...(1)
Similarly, $\overline{\mathrm{b}} \cdot \overline{\mathrm{q}}=\frac{\mathrm{b} \cdot(\overline{\mathrm{c}} \times \overline{\mathrm{a}})}{[\overline{\mathrm{a}} \overline{\mathrm{b}} \overline{\mathrm{c}}]}=1$...(2) and $\overline{\mathrm{c}} \cdot \overline{\mathrm{r}}=\frac{(\overline{\mathrm{a}} \times \overline{\mathrm{b}})}{\left[\begin{array}{ccc}\overline{\mathrm{a}} & \overline{\mathrm{b}} & \overline{\mathrm{c}}\end{array}\right]}=1$..(3)
$\therefore \overline{\mathrm{a}} \cdot \overline{\mathrm{p}}+\overline{\mathrm{b}} \cdot \overline{\mathrm{q}}+\overline{\mathrm{c}} \cdot \overline{\mathrm{r}}=1+1+1=3 \quad \ldots[$ from $(1),(2) \&(3)]$

</details>

---

### Q76. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\bar{a}, \bar{b}, \bar{c}$ are nonzero vectors along the coterminus edges of a parallelopiped with
volume 7 cubic units, then the volume of a parallelopiped with $\overline{\mathrm{a}}+\overline{\mathrm{b}}, \overline{\mathrm{b}}+\overline{\mathrm{c}}, \overline{\mathrm{c}}+\overline{\mathrm{a}}$ as
the coterminus edges is

**Options:**

- **(A)** 49 cubic units
- **(B)** 2 cubic units
- **(C)** 14 cubic units
- **(D)** 7 cubic units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 14 cubic units**

**Detailed Solution:**

(A)
We have $[\bar{a} \cdot(\bar{b} \times \bar{c})]=7$
$[\bar{a}+\bar{b} \quad \bar{b}+\bar{c} \quad \bar{c}+\bar{a}]$
$=(\bar{a}+\bar{b}) \cdot[(\bar{b}+\bar{c}) \times(\bar{c}+\bar{a})]$
$=(\bar{a}+\bar{b}) \cdot[(\bar{b} \times \bar{c})+(\bar{b} \times \bar{a})+(\bar{c} \times \bar{c})+(\bar{c} \times \bar{a})]$
$=[\bar{a} \cdot(\bar{b} \times \bar{c})]+[\bar{a} \cdot(\bar{b} \times \bar{a})]+[\bar{a}(\bar{c} \times \bar{a})]+[\bar{b} \cdot(\bar{b} \times \bar{c})]+[\bar{b} \cdot(\bar{b} \times \bar{a})]+[\bar{b} \cdot(\bar{c} \times \bar{a})]$
$=[\bar{a} \cdot(\bar{b} \times \bar{c})]+0+[\bar{b} \cdot(\bar{c} \times \bar{a})]$
$=[\bar{a} \cdot(\bar{b} \times \bar{c})]+[\bar{a} \cdot(\bar{b} \times \bar{c})]=2[\bar{a} \cdot(\bar{b} \times \bar{c})]$
$=2(7)=14$

</details>

---

### Q77. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the volume of the parallelopiped whose conterminus edges are along the vectors $\bar{a}, \overline{\mathrm{b}}, \overline{\mathrm{c}}$ is 12, then the volume of the tetrahedron whose conterminus edges are $\bar{a}+\overline{\mathrm{b}}, \overline{\mathrm{b}}+\overline{\mathrm{c}}$ and $\overline{\mathrm{c}}+\overline{\mathrm{a}}$ is

**Options:**

- **(A)** 4 (units) $^{3}$
- **(B)** 24 (units) $^{3}$
- **(C)** 6 (units) $^{3}$
- **(D)** 12 (units) $^{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 4 (units) $^{3}$**

**Detailed Solution:**

(C)
Volume of parallelepiped $=[\bar{a} \bar{b} \bar{c}]=12$
$\left[\begin{array}{lll}\bar{a} & \bar{b} & \bar{c}\end{array}\right]=12$$\ldots(1)$
volume of tetrahedrom
$=\frac{1}{6}\left[\begin{array}{lll}
\bar{a}+\bar{b} & \bar{b}+\bar{c} & \bar{c}+\bar{a}
\end{array}\right]$
$=\frac{1}{6}(\bar{a}+\bar{b}) \cdot[(\bar{b}+\bar{c}) \times(\bar{c}+\bar{a})]=\frac{1}{6}(\bar{a}+\bar{b}) \cdot[(\bar{b} \times \bar{c})+(\bar{b} \times \bar{a})+(\bar{c} \times \bar{c})+(\bar{c} \times \bar{a})]$
$=\frac{1}{6}\{\bar{a} \cdot(\bar{b} \times \bar{c})+\bar{a}(\bar{b} \times \bar{a})+\bar{a}(\bar{c} \times \bar{a})+\bar{b} \cdot(\bar{b} \times \bar{c})+\bar{b} \cdot(\bar{b} \times \bar{a})+\bar{b}(\bar{c} \times \bar{a})\} \quad \ldots[\because \bar{c} \times \bar{c}=0]$
$=\frac{1}{6}[\bar{a} \cdot(\bar{b} \times \bar{c})+0+\bar{b} \cdot(\bar{c} \times \bar{a})]=\frac{1}{6}\{[\bar{a} \bar{b} \bar{c}]+[\bar{a} \bar{b} \bar{c}]\}$
$=\frac{2}{6}[\bar{a} \bar{b} \bar{c}]=\frac{1}{3}(12)=4$

</details>

---

### Q78. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For any non - zero vectors $\bar{a}$ and $\overline{\mathrm{b}},\left[\begin{array}{lll}\overline{\mathrm{b}} & \overline{\mathrm{a}} \times \overline{\mathrm{b}} & \overline{\mathrm{a}}\end{array}\right]=$

**Options:**

- **(A)** $|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|$
- **(B)** $|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|^{2}$
- **(C)** 0
- **(D)** $\overline{\mathrm{a}} \times \overline{\mathrm{b}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|^{2}$**

**Detailed Solution:**

(B)
$\left[\begin{array}{lll}\bar{b} & \bar{a} \times \bar{b} & \bar{a}\end{array}\right]=\bar{b} \cdot[(\bar{a} \times \bar{b}) \times \bar{a}]$
$=-\bar{b}\left[\begin{array}{l}\bar{a} \times(\bar{a} \times \bar{b})\end{array}\right]$
$=-\bar{b}[(\mathrm{a} \cdot \mathrm{b}) \cdot \mathrm{a}-(\mathrm{a} \cdot \mathrm{a}) \cdot \mathrm{b}]=0$

</details>

---

### Q79. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $[\bar{a} \bar{b} \bar{c}] \neq 0$, then $\frac{[\bar{a}+\bar{b} \quad \bar{b}+\bar{c} \quad \bar{c}+\bar{a}]}{[\bar{b} \bar{c} \bar{a}]}=$

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 2
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

(D)
$\left[\begin{array}{lll}\bar{a}+\bar{b} & \bar{b}+\bar{c} & \bar{c}+\bar{a}\end{array}\right]$
$=(\bar{a}+\bar{b}) \cdot[(\bar{b}+\bar{c}) \times(\bar{c}+\bar{a})]$
$=(\bar{a}+\bar{b}) \cdot[(\bar{b} \times \bar{c})+(\bar{b} \times \bar{a})+(\bar{c} \times \bar{c})+(\bar{c} \times \bar{a})]$
$=[\bar{a} \cdot(\bar{b} \times \bar{c})]+[\bar{a} \cdot(\bar{b} \times \bar{a})]+[\bar{a} \cdot(\bar{c} \times \bar{a})]+[\bar{b} \cdot(\bar{b} \times \bar{c})]+[\bar{b} \cdot(\bar{b} \times \bar{a})]+[\bar{b} \cdot(\bar{c} \times \bar{a})]$
$=[\bar{a} \cdot(\bar{b} \times \bar{c})]+[\bar{b} \cdot(\bar{c} \times \bar{a})]$
$=2[\bar{a} \cdot(\bar{b} \times \bar{c})] \quad=2\left[\begin{array}{lll}\bar{a} & \bar{b} & \bar{c}\end{array}\right]$
Hence give expression $=\frac{2[\bar{a} \bar{b} \bar{c}]}{[\bar{a} \bar{b} \bar{c}]}=2$

</details>

---

### Q80. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the vectors $\hat{\imath}+\hat{\jmath}+\hat{k}, \hat{\imath}-\hat{\jmath}+\hat{k}$ and $2 \hat{\imath}+3 \hat{\jmath}+m \hat{k}$ are coplanar, then $m=$

**Options:**

- **(A)** 3
- **(B)** -2
- **(C)** 2
- **(D)** -3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

(C)
Since given vectors are coplanar, we write
$\begin{array}{l}
\left|\begin{array}{ccc}
1 & 1 & 1 \\
1 & -1 & 1 \\
2 & 3 & \mathrm{~m}
\end{array}\right|=0 \\
\therefore(-\mathrm{m}-3)-(\mathrm{m}-2)+(3+2)=0 \Rightarrow 2 \mathrm{~m}=4 \Rightarrow \mathrm{m}=2
\end{array}$

</details>

---

### Q81. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The volume of a tetrahedron whose vertices are $\mathrm{A} \equiv(-1,2,3), \mathrm{B} \equiv(3,-2,1)$, $\mathrm{C} \equiv(2,1,3)$ and $\mathrm{D} \equiv(-1,-2,4)$ is

**Options:**

- **(A)** $\frac{14}{3}$ cu. units
- **(B)** $\frac{16}{3}$ cu. units
- **(C)** $\frac{17}{3}$ cu. units
- **(D)** $\frac{15}{3}$ cu. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{16}{3}$ cu. units**

**Detailed Solution:**

Here $\overline{\mathrm{AB}}=4 \hat{\mathrm{i}}-4 \hat{\mathrm{j}}-2 \hat{\mathrm{k}}, \overline{\mathrm{AC}}=3 \hat{\mathrm{i}}-\hat{\mathrm{j}}$ and $\overline{\mathrm{AD}}=-4 \hat{\mathrm{j}}+\hat{\mathrm{k}}$ Volume of tetrahedron
$$
\begin{array}{l}
=\frac{1}{6} \overline{\mathrm{AB}} \cdot(\overline{\mathrm{AC}} \times \overline{\mathrm{AD}}) \\
=\frac{1}{6}\left|\begin{array}{ccc}
4 & -4 & -2 \\
3 & -1 & 0 \\
0 & -4 & 1
\end{array}\right|=\frac{1}{6}[4(-1)+4(3)-2(-12)] \\
\quad=\frac{1}{6}(32)=\frac{16}{3} \text { cu.units }
\end{array}
$$

</details>

---

### Q82. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $[\bar{a} \bar{b} \bar{c}]=3$, then the volume of the parallelopiped with $2 \bar{a}+\bar{b}, 2 \bar{b}+\bar{c}, 2 \bar{c}+\bar{a}$ as coterminus edges is

**Options:**

- **(A)** 22 cubic units
- **(B)** 15 cubic units
- **(C)** 27 cubic units
- **(D)** 25 cubic units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 27 cubic units**

**Detailed Solution:**

Volume of parallelepiped
$$
\begin{array}{l}
=(2 \bar{a}+\bar{b}) \cdot[(2 \bar{b}+\bar{c}) \times(2 \bar{c}+\bar{a})] \\
=(2 \bar{a}+\bar{b}) \cdot[(4 \bar{b} \times \bar{c})+(2 \bar{b} \times \bar{a})+(2 \bar{c} \times \bar{c})+(\bar{c} \times \bar{a})] \\
=[8 \bar{a} \cdot(\bar{b} \times \bar{c})]+[4 \bar{a} \cdot(\bar{b} \times \bar{a})]+[2 \bar{a} \cdot(\bar{c} \times \bar{a})]+[4 \bar{b} \cdot(\bar{b} \times \bar{c})]+[2 \bar{b} \cdot(\bar{b} \times \bar{a})]+[\bar{b} \cdot(\bar{c} \times \bar{a})] \\
=[8 \bar{a} \cdot(\bar{b} \times \bar{c})]+0+[\bar{b} \cdot(\bar{c} \times \bar{a})] \\
=8[\bar{a} \cdot(\bar{b} \times \bar{c})]+[\bar{a} \cdot(\bar{b} \times \bar{c})]=9 \bar{a} \cdot(\bar{b} \times \bar{c}) \\
=9[\bar{a} \quad \bar{b} \quad \bar{c}]=9(3)=27
\end{array}
$$

</details>

---

### Q83. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}(-1,2,3), \mathrm{B}(3,-2,1), \mathrm{C}(2,1,3)$ and $\mathrm{D}(-1,-2,4)$ are the vertices of a
tetrahedron, then its volume is

**Options:**

- **(A)** $\frac{16}{3}$ Cu. units
- **(B)** $\frac{13}{6}$ cu. units
- **(C)** $\frac{16}{31}$ CU. units
- **(D)** $\frac{31}{6}$ cu. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{16}{3}$ Cu. units**

**Detailed Solution:**

We have $\overline{A B}=4 \hat{i}-4 \hat{j}-2 \hat{k}, \overline{A C}=3 \hat{i}-\hat{j}$ and $\overline{A D}=-4 \bar{j}+\bar{k}$
Volume of tetrahedron $=\frac{1}{6}[\overline{\mathrm{AB}} \overline{\mathrm{AC}} \overline{\mathrm{AD}}]$
$$
\begin{array}{l}
=\frac{1}{6}\left|\begin{array}{ccc}
4 & -4 & -2 \\
3 & -1 & 0 \\
0 & -4 & 1
\end{array}\right| \\
=\frac{1}{6}[4(-1)+4(3)-2(-12)]=\frac{1}{6}(-4+12+24)=\frac{32}{6}=\frac{16}{3}
\end{array}
$$

</details>

---

### Q84. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the vectors $\bar{a}, \bar{b}, \bar{c}$ are non coplanar, then $\frac{[\bar{a}+2 \bar{b} \quad \bar{b}+2 \bar{c} \quad \bar{c}+2 \bar{a}]}{[\bar{a} \bar{b} \bar{c}]}=$

**Options:**

- **(A)** 8
- **(B)** 3
- **(C)** 9
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 9**

**Detailed Solution:**

Here
$\left[\begin{array}{ccc}\bar{a}+2 \bar{b} & \bar{b}+2 \bar{c} & \bar{c}+2 \bar{a}\end{array}\right]$
$\begin{aligned}[\bar{a}&+2 \bar{b} \quad \bar{b}+2 \bar{c} \quad \bar{c}+2 \bar{a}] \\ &=(\bar{a}+2 \bar{b}) \cdot[(\bar{b}+2 \bar{c}) \times(\bar{c}+2 \bar{a})] \\ &=(\bar{a}+2 \bar{b}) \cdot[(\bar{b} \times \bar{c})+(2 \bar{b} \times \bar{a})+(2 \bar{c} \times \bar{c})+(4 \bar{c} \times \bar{a})] \\ &=(\bar{a}+2 \bar{b}) \cdot[(\bar{b} \times \bar{c})+2(\bar{b} \times \bar{a})+0+4(\bar{c} \times \bar{a})] \\ &=[\bar{a}(\bar{b} \times \bar{c})]+0+0+0+0+8[\bar{b}(\bar{c} \times \bar{a})] \\ &=9[\bar{a}(\bar{b} \times \bar{c})] \\ &=9\left[\begin{array}{lll}\bar{a} & \bar{b} & \bar{c}\end{array}\right] \end{aligned}$
Now
$$
\frac{\left[\begin{array}{lll}
\bar{a}+2 \bar{b} & \bar{b}+2 \bar{c} & \bar{c}+2 \bar{a}
\end{array}\right]}{\left[\begin{array}{lll}
\bar{a} & \bar{b} & \bar{c}
\end{array}\right]}=\frac{9[\bar{a} \bar{b} \bar{c}]}{[\bar{a} \bar{b} \bar{c}]}=9
$$

</details>

---

### Q85. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{u}=\hat{\imath}-2 \hat{\jmath}+\hat{k}, \bar{v}=3 \hat{\imath}+\hat{k}$ and $\bar{w}=\hat{\jmath}-\hat{k}$, then the volume of the parallelopiped
with $\bar{u} \times \bar{v}, \bar{u}+\bar{w}$ and $\bar{v}+\bar{w}$ as coterminus edges is

**Options:**

- **(A)** 12 cubic units
- **(B)** 10 cubic units
- **(C)** 24 cubic units
- **(D)** 20 cubic units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 24 cubic units**

**Detailed Solution:**

$\bar{u} \times \bar{v}=\left|\begin{array}{ccc}\hat{i} & \hat{j} & \hat{k} \\ 1 & -2 & 1 \\ 3 & 0 & 1\end{array}\right|=\hat{i}(-2)-\hat{j}(1-3)+\hat{k}(0+6)=-2 \hat{i}+2 \hat{j}+6 \hat{k}$
$\hat{u}+\hat{w}=\hat{i}-\hat{j}$
$\hat{v}+\hat{w}=3 \hat{i}+\hat{j}$
$\begin{aligned} \text { Volume of parallelopiped } &=(\bar{u} \times \bar{v}) \cdot[(\bar{u}+\bar{w}) \times(\bar{v}+\bar{w})] \\ &=\left|\begin{array}{ccc}-2 & 2 & 6 \\ 1 & -1 & 0 \\ 3 & 0 & 1\end{array}\right|=|-2(-1)-2(1)+6(-3)|=18 \end{aligned}$

</details>

---

### Q86. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $m$, if the vectors $\hat{\imath}-\hat{\jmath}-6 \hat{k}, \hat{\imath}-3 \hat{\jmath}+4 \hat{k}$ and $2 \hat{\imath}-5 \hat{\jmath}+m \hat{k}$ are
coplanar, is

**Options:**

- **(A)** 1
- **(B)** $-3$
- **(C)** 3
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

$\bar{a}=\hat{i}-\hat{j}-6 \hat{k}, \bar{b}=\hat{i}-3 \hat{j}+4 \hat{k}, \bar{c}=2 \hat{i}-5 \hat{j}+m \hat{k}$ are coplanar
$\begin{aligned}
\therefore &\left|\begin{array}{rrr}
1 & -1 & -6 \\
1 & -3 & 4 \\
2 & -5 & \mathrm{~m}
\end{array}\right|=0 \\
& 1(-3 \mathrm{~m}+20)+1(\mathrm{~m}-8)-6(-5+6)=0 \\
&-3 \mathrm{~m}+20+\mathrm{m}-8+30-36=0 \Rightarrow-2 \mathrm{~m}+6=0 \quad \Rightarrow \mathrm{m}=3
\end{aligned}$

</details>

---

### Q87. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $[\bar{a} \quad \bar{b} \quad \bar{c}]=4$, then volume of parallelopiped with coterminus edges $\bar{a}+2 \bar{b}$,
$\bar{b}+2 \bar{c}, \quad \bar{c}+2 \bar{a}$ is

**Options:**

- **(A)** 36 units $^{3}$
- **(B)** 32 units $^{3}$
- **(C)** 20 units $^{3}$
- **(D)** 40 units $^{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 36 units $^{3}$**

**Detailed Solution:**

Given $\bar{a} \cdot(\bar{b} \times \bar{c})=4$
$\therefore$ Volume of parallelopiped
$\begin{array}{l}
=(\overline{\mathrm{a}}+2 \overline{\mathrm{b}}) \cdot[(\overline{\mathrm{b}}+2 \overline{\mathrm{c}}) \times(\overline{\mathrm{c}}+2 \overline{\mathrm{a}})] \\
=(\overline{\mathrm{a}}+2 \overline{\mathrm{b}}) \cdot[(\overline{\mathrm{b}} \times \overline{\mathrm{c}})+2(\overline{\mathrm{b}} \times \overline{\mathrm{a}})+2(\overline{\mathrm{c}} \times \overline{\mathrm{c}})+4(\overline{\mathrm{c}} \times \overline{\mathrm{a}})] \\
=[\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})]+[2 \overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{a}})]+[4 \overline{\mathrm{a}} \cdot(\overline{\mathrm{c}} \times \overline{\mathrm{a}})]+ \\
=[2 \overline{\mathrm{b}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})]+[4 \overline{\mathrm{b}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{a}})]+[8 \overline{\mathrm{b}} \cdot(\overline{\mathrm{c}} \times \overline{\mathrm{a}})] \\
=[\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})]+0+[8 \overline{\mathrm{b}} \cdot(\overline{\mathrm{c}} \times \overline{\mathrm{a}})] \\
=9[\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})]=9(4)=36
\end{array}$

</details>

---

### Q88. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}=\frac{1}{\sqrt{10}}(3 \hat{\imath}+\hat{k}), \overline{\mathrm{b}}=\frac{1}{7}(2 \hat{\imath}+3 \hat{\jmath}-6 \hat{k})$, then the value of
$(2 \bar{a}-\bar{b}) \cdot[(\bar{a} \times \bar{b}) \times(\bar{a}+2 \bar{b})]$ is

**Options:**

- **(A)** 7
- **(B)** -5
- **(C)** 5
- **(D)** -7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -5**

**Detailed Solution:**

Given vectors $\bar{a} \& \bar{b}$ are unit vectors.
$\begin{array}{l}
\text { Now }(2 \bar{a}-\bar{b}) \cdot[(\bar{a} \times \bar{b}) \times(\bar{a}+2 \bar{b})] \\
\quad=-(2 \bar{a}-\bar{b}) \cdot[(\bar{a}+2 \bar{b}) \times(\bar{a} \times \bar{b})] \\
\quad=-(2 \bar{a}-\bar{b}) \cdot[\bar{a} \times(\bar{a} \times \bar{b})+2 \bar{b} \times(\bar{a} \times \bar{b})] \\
\quad=-(2 \bar{a}-\bar{b})[(\bar{a} \cdot \bar{b}) \cdot \bar{a}-(\bar{a} \cdot \bar{a}) \cdot \bar{b}+2(\bar{b} \cdot \bar{b}) \cdot \bar{a}-2(\bar{b} \cdot \bar{a}) \cdot \bar{b}] \\
\quad=-(2 \bar{a}-\bar{b})[(\bar{a} \cdot \bar{b}) \bar{a}-\bar{b}+2 \bar{a}-2(\bar{b} \cdot \bar{a}) \bar{b}] \\
\text { Here } \quad \bar{a} \cdot \bar{b}=\frac{3(2)}{7 \sqrt{10}}-\frac{1(6)}{7 \sqrt{10}}=0
\end{array}$
Hence given expression becomes
$\begin{array}{l}
=-(2 \bar{a}-\bar{b})[-\bar{b}+2 \bar{a}]=-(2 \bar{a}-\bar{b})^{2} \\
=-\left[4 \bar{a}^{2}+\bar{b}^{2}-4 \bar{a} \cdot \bar{b}\right]=-(4+1)=-5
\end{array}$

</details>

---

### Q89. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For any non-zero vector, a, b, c

<math><mi>a</mi><mo>.</mo><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mo>×</mo><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mo>…</mo><mo>.</mo></math>

**Options:**

- **(A)** 0
- **(B)** <math><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><mi>a</mi><mtext> </mtext><mi>b</mi><mtext> </mtext><mi>c</mi></mrow></mfenced></math>
- **(C)** <math><mfenced close="]" open="[" separators="|"><mrow><mi>a</mi><mtext> </mtext><mi>b</mi><mtext> </mtext><mi>c</mi></mrow></mfenced></math>
- **(D)** <math><mfenced close="]" open="[" separators="|"><mrow><mi>a</mi><mtext> </mtext><mi>c</mi><mtext> </mtext><mi>b</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

We have, <math><mi>a</mi><mo>.</mo><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mo>×</mo><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced></mrow></mfenced></math>  
<math><mo>=</mo><mi>a</mi><mo>.</mo><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mi>b</mi><mo>×</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>×</mo><mi>b</mi><mo>+</mo><mi>b</mi><mo>×</mo><mi>c</mi><mo>+</mo><mi>c</mi><mo>×</mo><mi>a</mi><mo>+</mo><mi>c</mi><mo>×</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>×</mo><mi>c</mi></mrow></mfenced></mrow></mfenced></math>  
<math><mo>=</mo><mi>a</mi><mo>.</mo><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mi>b</mi><mo>×</mo><mi>a</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>b</mi><mo>×</mo><mi>c</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>c</mi><mo>×</mo><mi>a</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>c</mi><mo>×</mo><mi>b</mi></mrow></mfenced></mrow></mfenced></math>  
<math><mo>=</mo><mi>a</mi><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mi>b</mi><mo>×</mo><mi>a</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>b</mi><mo>×</mo><mi>c</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>c</mi><mo>×</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mi>b</mi><mo>×</mo><mi>c</mi></mrow></mfenced></mrow></mfenced></math>  
<math><mo>=</mo><mi>a</mi><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mi>b</mi><mo>×</mo><mi>a</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>c</mi><mo>×</mo><mi>a</mi></mrow></mfenced></mrow></mfenced></math>  
<math><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mi>a</mi><mtext> </mtext><mi>b</mi><mtext> </mtext><mi>a</mi></mrow></mfenced><mo>+</mo><mfenced close="]" open="[" separators="|"><mrow><mi>a</mi><mtext> </mtext><mi>c</mi><mtext> </mtext><mi>a</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mo>+</mo><mn>0</mn><mo>=</mo><mn>0</mn></math>

</details>

---

### Q90. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the scalar triple product of the vectors <math><mo>-</mo><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>,</mo><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>7</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>λ</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mi></mi></math> and <math><mn>7</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> is 272 then <math><mi>λ</mi><mo>=</mo></math> …

**Options:**

- **(A)** 9
- **(B)** 11
- **(C)** 8
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 11**

**Detailed Solution:**

Scalar triple product of the given vectors is 272. 
<math><mo>∴</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>7</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>7</mn></mtd><mtd><mi>λ</mi></mtd></mtr><mtr><mtd><mn>7</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>272</mn></math> ( <math><mo>∵</mo></math> scalar triple product of the vectors a, b and c is [a b c]) 
<math><mo>&#8658;</mo><mo>-</mo><mn>3</mn><mfenced separators="|"><mrow><mn>21</mn><mo>+</mo><mn>5</mn><mi>λ</mi></mrow></mfenced><mo>-</mo><mn>7</mn><mfenced separators="|"><mrow><mo>-</mo><mn>9</mn><mo>-</mo><mn>7</mn><mi>λ</mi></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced separators="|"><mrow><mo>-</mo><mn>15</mn><mo>+</mo><mn>49</mn></mrow></mfenced><mo>=</mo><mn>272</mn></math>  
<math><mo>&#8658;</mo><mo>-</mo><mn>63</mn><mo>-</mo><mn>15</mn><mi>λ</mi><mo>+</mo><mn>63</mn><mo>+</mo><mn>49</mn><mi>λ</mi><mo>-</mo><mn>102</mn><mo>=</mo><mn>272</mn></math>  
<math><mo>&#8658;</mo><mn>34</mn><mi>λ</mi><mo>-</mo><mn>102</mn><mo>=</mo><mn>272</mn></math>  
<math><mo>&#8658;</mo><mn>34</mn><mi>λ</mi><mo>=</mo><mn>37</mn><mn>4</mn></math>  
<math><mo>&#8658;</mo><mi>λ</mi><mo>=</mo><mn>1</mn><mn>1</mn></math>

</details>

---

### Q91. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `1`

$\mathbf{i} \cdot(\mathbf{j} \times \mathbf{k})+\mathbf{j} \cdot(\mathbf{k} \times \mathbf{i})+\mathbf{k} \cdot(\mathbf{j} \times \mathbf{i})$ is equal to

**Options:**

- **(A)** 3
- **(B)** 2
- **(C)** 1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

Given, 
$\begin{aligned} \mathbf{i} \cdot(\mathbf{j} \times \mathbf{k}) &+\mathbf{j} \cdot(\mathbf{k} \times \mathbf{i})+\mathbf{k} \cdot(\mathbf{j} \times \mathbf{i}) \\=& \mathbf{i} \cdot(\mathbf{i})+\mathbf{j} \cdot(\mathbf{j})+\mathbf{k} \cdot(-\mathbf{k}) \\=&(\mathbf{i} \cdot \mathbf{i})+(\mathbf{j} \cdot \mathbf{j})-(\mathbf{k} \cdot \mathbf{k}) \\=& 1+1-1=1 \end{aligned}$

</details>

---

### Q92. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `1`

If the position vectors of the vertices $A, B$ and $C$ are 6i, $6 \mathbf{j}$ and $\mathbf{k}$ respectively w.r.t. origin $O$, then the volume of the tetrahedron $O A B C$ is

**Options:**

- **(A)** 6
- **(B)** 3
- **(C)** $\frac{1}{6}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 6**

**Detailed Solution:**

Given that, the position vectors of the vertices $A, B$ and $C$ are
$$
\begin{array}{l}
\mathbf{O A}=6 \mathbf{i}=6 \mathbf{i}+0 \mathbf{j}+0 \mathbf{k} \\
\mathbf{O B}=6 \mathbf{j}=0 \mathbf{i}+6 \mathbf{j}+0 \mathbf{k} \\
\mathbf{O C}=\mathbf{k}=0 \mathbf{i}+0 \mathbf{j}+\mathbf{k}
\end{array}
$$
Now, volume of the tetrahedron
$$
\begin{array}{l}
=\frac{1}{6}[\mathbf{O A} \mathbf{O B} \mathbf{O C}] \\
=\frac{1}{6}\left|\begin{array}{lll}
6 & 0 & 0 \\
0 & 6 & 0 \\
0 & 0 & 1
\end{array}\right| \\
=\frac{1}{6}(6 \times 6 \times 1)=6
\end{array}
$$

</details>

---

### Q93. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

The volume of a parallelopiped whose coterminous edges are $2 \overrightarrow{\mathbf{a}}, 2 \overrightarrow{\mathbf{b}}, 2 \overrightarrow{\mathbf{c}}$, is

**Options:**

- **(A)** $2[\overrightarrow{\mathbf{a}} \overrightarrow{\mathbf{b}} \overrightarrow{\mathbf{c}}]$
- **(B)** $4[\overrightarrow{\mathbf{a}} \overrightarrow{\mathbf{b}} \overrightarrow{\mathbf{c}}]$
- **(C)** $8[\overrightarrow{\mathbf{a}} \overrightarrow{\mathbf{b}} \overrightarrow{\mathbf{c}}]$
- **(D)** $[\overrightarrow{\mathbf{a}} \overrightarrow{\mathbf{b}} \overrightarrow{\mathbf{c}}]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8[\overrightarrow{\mathbf{a}} \overrightarrow{\mathbf{b}} \overrightarrow{\mathbf{c}}]$**

**Detailed Solution:**

Volume of parallelopiped $=[2 \overrightarrow{\mathbf{a}} 2 \overrightarrow{\mathbf{b}} 2 \overrightarrow{\mathbf{c}}]$
$$
=8[\overrightarrow{\mathbf{a}} \overrightarrow{\mathbf{b}} \overrightarrow{\mathbf{c}}]
$$

</details>

---

### Q94. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

If $\overrightarrow{\mathbf{a}}, \overrightarrow{\mathbf{b}}, \overrightarrow{\mathbf{c}}$ are three non coplanar vectors and $\overrightarrow{\mathbf{p}}, \overrightarrow{\mathbf{q}}, \overrightarrow{\mathbf{r}}$ are defined by the relations
$\overrightarrow{\mathbf{p}}=\frac{\overrightarrow{\mathbf{b}} \times \overrightarrow{\mathbf{c}}}{[\overrightarrow{\mathbf{a}} \overrightarrow{\mathbf{b}} \overrightarrow{\mathbf{c}}]}, \quad \overrightarrow{\mathbf{q}}=\frac{\overrightarrow{\mathbf{c}} \times \overrightarrow{\mathbf{a}}}{[\overrightarrow{\mathbf{a}} \overrightarrow{\mathbf{b}} \overrightarrow{\mathbf{c}}]}$ and $\overrightarrow{\mathbf{r}}=\frac{\overrightarrow{\mathbf{b}} \times \overrightarrow{\mathbf{a}}}{[\overrightarrow{\mathbf{a}} \overrightarrow{\mathbf{b}} \overrightarrow{\mathbf{c}}]}$
then $\overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{p}}+\overrightarrow{\mathbf{b}} \cdot \overrightarrow{\mathbf{q}}+\overrightarrow{\mathbf{c}} \cdot \overrightarrow{\mathbf{r}}$ is equal to

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

$\overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{p}}+\overrightarrow{\mathbf{b}} \cdot \overrightarrow{\mathbf{q}}+\overrightarrow{\mathbf{c}} \cdot \overrightarrow{\mathbf{r}}$
$$
\begin{aligned}
&=\frac{\overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{b}} \times \overrightarrow{\mathbf{c}}}{[\overrightarrow{\mathbf{a}} \overrightarrow{\mathbf{b}} \overrightarrow{\mathbf{c}}]}+\frac{\overrightarrow{\mathbf{b}} \cdot \overrightarrow{\mathbf{c}} \times \overrightarrow{\mathbf{a}}}{[\overrightarrow{\mathbf{a}} \overrightarrow{\mathbf{b}} \overrightarrow{\mathbf{c}}]}+\frac{\overrightarrow{\mathbf{c}} \cdot \overrightarrow{\mathbf{b}} \times \overrightarrow{\mathbf{a}}}{[\overrightarrow{\mathbf{a}} \overrightarrow{\mathbf{b}} \overrightarrow{\mathbf{c}}]} \\
=& 1+1-1=1
\end{aligned}
$$

</details>

---

### Q95. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

Volume of the parallelopiped having vertices at $O \equiv(0,0,0), A \equiv(2,-2,1), B \equiv(5,-4,4)$
and $C=(1,-2,4)$ is

**Options:**

- **(A)** 5 cu unit
- **(B)** 10 cu unit
- **(C)** 15 cu unit
- **(D)** 20 cu unit

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 10 cu unit**

**Detailed Solution:**

$\begin{array}{ll}\text {  } & \text { Given, } \overrightarrow{\mathbf{O A}}=2 \hat{\mathbf{i}}-2 \hat{\mathbf{j}}+\hat{\mathbf{k}} \\ & \overrightarrow{\mathbf{O B}}=5 \hat{\mathbf{i}}-4 \hat{\mathbf{j}}+4 \hat{\mathbf{k}} \text { and } \overrightarrow{\mathbf{O C}}=\hat{\mathbf{i}}-2 \hat{\mathbf{j}}+4 \hat{\mathbf{k}}\end{array}$
Volume of parallelopiped $=[\overrightarrow{\mathrm{OA}} \overrightarrow{\mathrm{OB}} \overrightarrow{\mathrm{OC}}]$
$=\left|\begin{array}{ccc}2 & -2 & 1 \\ 5 & -4 & 4 \\ 1 & -2 & 4\end{array}\right|$
$=2(-16+8)+2(20-4)+1(-10+4)$
$=10 \mathrm{cu}$ unit

</details>

---

