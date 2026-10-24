# MHT CET Mathematics - Vector Algebra

## Topic 4: Vector Triple Product

**Total Questions:** 31

---

### Q1. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{p}, \bar{q}, \bar{r}$ are unit vectors such that $\bar{p} \times (\bar{q} \times \bar{r}) = \dfrac{1}{7}\bar{q}$, then the angle between $\bar{p}$ and $\bar{r}$ is

**Options:**

- **(A)** $\cos^{-1}(7)$
- **(B)** $\sin^{-1}\left(\dfrac{4\sqrt{3}}{7}\right)$
- **(C)** $\tan^{-1}\left(\dfrac{1}{7}\right)$
- **(D)** $\dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sin^{-1}\left(\dfrac{4\sqrt{3}}{7}\right)$**

**Detailed Solution:**

Using the vector triple product expansion:

$\bar{p} \times (\bar{q} \times \bar{r}) = (\bar{p} \cdot \bar{r})\bar{q} - (\bar{p} \cdot \bar{q})\bar{r}$

Given that $\bar{p} \times (\bar{q} \times \bar{r}) = \dfrac{1}{7}\bar{q}$, we have:

$(\bar{p} \cdot \bar{r})\bar{q} - (\bar{p} \cdot \bar{q})\bar{r} = \dfrac{1}{7}\bar{q}$

Since $\bar{q}$ is a unit vector, $\bar{q} \neq \bar{0}$. If $\bar{q}$ and $\bar{r}$ were collinear, $\bar{q} \times \bar{r} = \bar{0}$, which would imply $\dfrac{1}{7}\bar{q} = \bar{0}$, a contradiction. Thus, $\bar{q}$ and $\bar{r}$ are non-collinear vectors.

Equating the coefficients of $\bar{q}$ and $\bar{r}$ on both sides:

$\bar{p} \cdot \bar{r} = \dfrac{1}{7}$

$\bar{p} \cdot \bar{q} = 0$

Let $\theta$ be the angle between the unit vectors $\bar{p}$ and $\bar{r}$. Then:

$|\bar{p}| |\bar{r}| \cos\theta = \dfrac{1}{7}$

$\cos\theta = \dfrac{1}{7}$

Using the identity $\sin^2\theta + \cos^2\theta = 1$:

$\sin\theta = \sqrt{1 - \cos^2\theta} = \sqrt{1 - \left(\dfrac{1}{7}\right)^2} = \sqrt{\dfrac{48}{49}} = \dfrac{4\sqrt{3}}{7}$

$\theta = \sin^{-1}\left(\dfrac{4\sqrt{3}}{7}\right)$

Answer: $\sin^{-1}\left(\dfrac{4\sqrt{3}}{7}\right)$

</details>

---

### Q2. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{a}, \vec{b}, \vec{c}$ are three non-coplanar vectors and $\vec{p}, \vec{q}, \vec{r}$ are defined as $\vec{p} = \dfrac{\vec{b} \times \vec{c}}{[\vec{a}\ \vec{b}\ \vec{c}]}, \vec{q} = \dfrac{\vec{c} \times \vec{a}}{[\vec{a}\ \vec{b}\ \vec{c}]}, \vec{r} = \dfrac{\vec{a} \times \vec{b}}{[\vec{a}\ \vec{b}\ \vec{c}]}$, then $[(\vec{a} + \vec{b}) \cdot \vec{p} + (\vec{b} + \vec{c}) \cdot \vec{q} + (\vec{c} + \vec{a}) \cdot \vec{r}]$ is equal to

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3$**

**Detailed Solution:**

The given vectors $\vec{p}, \vec{q}, \vec{r}$ are the reciprocal vectors of $\vec{a}, \vec{b}, \vec{c}$.

Using the properties of reciprocal vectors, we have:
$\vec{a} \cdot \vec{p} = \dfrac{\vec{a} \cdot (\vec{b} \times \vec{c})}{[\vec{a}\ \vec{b}\ \vec{c}]} = \dfrac{[\vec{a}\ \vec{b}\ \vec{c}]}{[\vec{a}\ \vec{b}\ \vec{c}]} = 1$
$\vec{b} \cdot \vec{p} = \dfrac{\vec{b} \cdot (\vec{b} \times \vec{c})}{[\vec{a}\ \vec{b}\ \vec{c}]} = 0$

Similarly, for the other dot products:
$\vec{b} \cdot \vec{q} = 1$, $\vec{c} \cdot \vec{q} = 0$
$\vec{c} \cdot \vec{r} = 1$, $\vec{a} \cdot \vec{r} = 0$

Expanding the given expression:
$(\vec{a} + \vec{b}) \cdot \vec{p} + (\vec{b} + \vec{c}) \cdot \vec{q} + (\vec{c} + \vec{a}) \cdot \vec{r}$

$= (\vec{a} \cdot \vec{p} + \vec{b} \cdot \vec{p}) + (\vec{b} \cdot \vec{q} + \vec{c} \cdot \vec{q}) + (\vec{c} \cdot \vec{r} + \vec{a} \cdot \vec{r})$

Substituting the values obtained above:
$= (1 + 0) + (1 + 0) + (1 + 0)$

$= 1 + 1 + 1 = 3$

Answer: $3$

</details>

---

### Q3. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $|\bar{a}| = |\bar{b}| = 1, |\bar{c}| = 2$ and $\bar{a} \times (\bar{a} \times \bar{c}) + \bar{b} = \bar{0}$, then the acute angle between $\bar{a}$ and $\bar{c}$ is $\ldots$

**Options:**

- **(A)** $\dfrac{\pi}{2}$
- **(B)** $\dfrac{\pi}{3}$
- **(C)** $\dfrac{\pi}{4}$
- **(D)** $\dfrac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\pi}{6}$**

**Detailed Solution:**

Given $\bar{a} \times (\bar{a} \times \bar{c}) + \bar{b} = \bar{0}$

Using the vector triple product expansion:

$(\bar{a} \cdot \bar{c})\bar{a} - (\bar{a} \cdot \bar{a})\bar{c} + \bar{b} = \bar{0}$

Since $|\bar{a}| = 1$, we have $\bar{a} \cdot \bar{a} = 1$.

$(\bar{a} \cdot \bar{c})\bar{a} - \bar{c} + \bar{b} = \bar{0}$

$\bar{b} = \bar{c} - (\bar{a} \cdot \bar{c})\bar{a}$

Squaring both sides:

$|\bar{b}|^2 = |\bar{c}|^2 + (\bar{a} \cdot \bar{c})^2|\bar{a}|^2 - 2(\bar{a} \cdot \bar{c})(\bar{a} \cdot \bar{c})$

Substituting $|\bar{a}| = 1$, $|\bar{b}| = 1$, and $|\bar{c}| = 2$:

$1 = 4 + (\bar{a} \cdot \bar{c})^2 - 2(\bar{a} \cdot \bar{c})^2$

$1 = 4 - (\bar{a} \cdot \bar{c})^2$

$(\bar{a} \cdot \bar{c})^2 = 3$

Let $\theta$ be the angle between $\bar{a}$ and $\bar{c}$. Then $\bar{a} \cdot \bar{c} = |\bar{a}||\bar{c}|\cos\theta = 2\cos\theta$.

$(2\cos\theta)^2 = 3$

$4\cos^2\theta = 3 \Rightarrow \cos^2\theta = \dfrac{3}{4}$

Since $\theta$ is an acute angle, $\cos\theta = \dfrac{\sqrt{3}}{2}$.

$\theta = \dfrac{\pi}{6}$

Answer: $\dfrac{\pi}{6}$

</details>

---

### Q4. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}, \bar{b}, \bar{c}$ are three non zero and non-coplanar vectors such that $\bar{a} \times (\bar{b} \times \bar{c}) = \dfrac{\bar{b}}{2}$, then the angle between $\bar{a}$ and $\bar{b}$ is ...

**Options:**

- **(A)** $\dfrac{\pi}{6}$
- **(B)** $\dfrac{\pi}{3}$
- **(C)** $\dfrac{\pi}{2}$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\pi}{2}$**

**Detailed Solution:**

Given $\bar{a} \times (\bar{b} \times \bar{c}) = \dfrac{\bar{b}}{2}$

Using the vector triple product expansion, we have:

$(\bar{a} \cdot \bar{c})\bar{b} - (\bar{a} \cdot \bar{b})\bar{c} = \dfrac{1}{2}\bar{b}$

Rearranging the terms, we get:

$\left(\bar{a} \cdot \bar{c} - \dfrac{1}{2}\right)\bar{b} - (\bar{a} \cdot \bar{b})\bar{c} = \bar{0}$

Since $\bar{a}, \bar{b}, \bar{c}$ are non-coplanar vectors, $\bar{b}$ and $\bar{c}$ must be non-collinear. Therefore, their coefficients must be independently zero:

$\bar{a} \cdot \bar{c} - \dfrac{1}{2} = 0 \Rightarrow \bar{a} \cdot \bar{c} = \dfrac{1}{2}$

$\bar{a} \cdot \bar{b} = 0$

Since $\bar{a}$ and $\bar{b}$ are non-zero vectors, $\bar{a} \cdot \bar{b} = 0$ implies that $\bar{a}$ is perpendicular to $\bar{b}$.

Thus, the angle between $\bar{a}$ and $\bar{b}$ is $\dfrac{\pi}{2}$.

Answer: $\dfrac{\pi}{2}$

</details>

---

### Q5. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}, \bar{b}, \bar{c}$ be three vectors having magnitudes 1, 1 and 2 respectively. If $\bar{a} \times (\bar{a} \times \bar{c}) + \bar{b} = \bar{0}$, then the acute angle between $\bar{a}$ and $\bar{c}$ is

**Options:**

- **(A)** $\dfrac{\pi}{4}$
- **(B)** $\dfrac{\pi}{6}$
- **(C)** $\dfrac{\pi}{3}$
- **(D)** $\dfrac{\pi}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\pi}{6}$**

**Detailed Solution:**

Given $\bar{a} \times (\bar{a} \times \bar{c}) + \bar{b} = \bar{0}$

Using the vector triple product expansion:

$(\bar{a} \cdot \bar{c})\bar{a} - (\bar{a} \cdot \bar{a})\bar{c} + \bar{b} = \bar{0}$

Since $|\bar{a}| = 1$, $\bar{a} \cdot \bar{a} = 1$.

$(\bar{a} \cdot \bar{c})\bar{a} - \bar{c} + \bar{b} = \bar{0}$

$\bar{b} = \bar{c} - (\bar{a} \cdot \bar{c})\bar{a}$

Squaring both sides:

$|\bar{b}|^2 = |\bar{c}|^2 + (\bar{a} \cdot \bar{c})^2 |\bar{a}|^2 - 2(\bar{a} \cdot \bar{c})(\bar{a} \cdot \bar{c})$

$|\bar{b}|^2 = |\bar{c}|^2 - (\bar{a} \cdot \bar{c})^2$

Substituting the given magnitudes $|\bar{a}| = 1$, $|\bar{b}| = 1$, and $|\bar{c}| = 2$:

$1^2 = 2^2 - (|\bar{a}||\bar{c}|\cos\theta)^2$

$1 = 4 - (1 \times 2 \times \cos\theta)^2$

$1 = 4 - 4\cos^2\theta$

$4\cos^2\theta = 3$

$\cos^2\theta = \dfrac{3}{4}$

$\cos\theta = \pm\dfrac{\sqrt{3}}{2}$

For the acute angle, $\cos\theta = \dfrac{\sqrt{3}}{2}$

$\theta = \dfrac{\pi}{6}$

Answer: $\dfrac{\pi}{6}$

</details>

---

### Q6. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}, \overline{\mathrm{~b}}, \overline{\mathrm{c}}$ are three coplanar vectors such that $|\bar{a}|=1,|\overline{\mathrm{~b}}|=2, \overline{\mathrm{~b}} \cdot \overline{\mathrm{c}}=8$ and the angle between $\overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ is $45^{\circ}$ then the value of $|\bar{a} \times(\overline{\mathrm{b}} \times \overline{\mathrm{c}})|$ is

**Options:**

- **(A)** 8
- **(B)** $\sqrt{2}$
- **(C)** 2
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 8**

**Detailed Solution:**

Given $\bar{b} \cdot \bar{c} = 8$ and the angle between $\bar{b}$ and $\bar{c}$ is $45^{\circ}$.

$|\bar{b}| |\bar{c}| \cos 45^{\circ} = 8$

$2 |\bar{c}| \dfrac{1}{\sqrt{2}} = 8 \Rightarrow |\bar{c}| = 4\sqrt{2}$

The magnitude of the cross product $\bar{b} \times \bar{c}$ is:

$|\bar{b} \times \bar{c}| = |\bar{b}| |\bar{c}| \sin 45^{\circ} = 2 \times 4\sqrt{2} \times \dfrac{1}{\sqrt{2}} = 8$

Since $\bar{a}, \bar{b}, \bar{c}$ are coplanar, the vector $\bar{b} \times \bar{c}$ is perpendicular to the plane containing $\bar{b}$ and $\bar{c}$, which means it is also perpendicular to $\bar{a}$.

Thus, the angle between $\bar{a}$ and $\bar{b} \times \bar{c}$ is $90^{\circ}$.

$|\bar{a} \times (\bar{b} \times \bar{c})| = |\bar{a}| |\bar{b} \times \bar{c}| \sin 90^{\circ}$

$|\bar{a} \times (\bar{b} \times \bar{c})| = 1 \times 8 \times 1 = 8$

Answer: 8

</details>

---

### Q7. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}, \bar{b}, \bar{c}$ are three coplanar vectors such that $|\bar{a}|=1,|\bar{b}|=2$, $\overline{\mathrm{b}} \cdot \overline{\mathrm{c}}=8$, the angle between $\overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ is $45^{\circ}$, then $|\bar{a} \times(\bar{b} \times \bar{c})|=$

**Options:**

- **(A)** 8
- **(B)** $4 \sqrt{2}$
- **(C)** $\sqrt{2}$
- **(D)** $8 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 8**

**Detailed Solution:**

Given $\bar{b} \cdot \bar{c} = 8$ and the angle between $\bar{b}$ and $\bar{c}$ is $45^{\circ}$.

$|\bar{b}| |\bar{c}| \cos 45^{\circ} = 8$

$2 |\bar{c}| \left(\dfrac{1}{\sqrt{2}}\right) = 8$

$|\bar{c}| = 4\sqrt{2}$

The magnitude of the cross product of $\bar{b}$ and $\bar{c}$ is:

$|\bar{b} \times \bar{c}| = |\bar{b}| |\bar{c}| \sin 45^{\circ} = 2 \times 4\sqrt{2} \times \dfrac{1}{\sqrt{2}} = 8$

Since $\bar{a}, \bar{b}, \bar{c}$ are coplanar vectors, $\bar{a}$ lies in the plane containing $\bar{b}$ and $\bar{c}$.

The vector $\bar{b} \times \bar{c}$ is perpendicular to the plane containing $\bar{b}$ and $\bar{c}$, which means it is also perpendicular to $\bar{a}$. Thus, the angle between $\bar{a}$ and $(\bar{b} \times \bar{c})$ is $90^{\circ}$.

Now, evaluating the magnitude of the vector triple product:

$|\bar{a} \times (\bar{b} \times \bar{c})| = |\bar{a}| |\bar{b} \times \bar{c}| \sin 90^{\circ}$

$|\bar{a} \times (\bar{b} \times \bar{c})| = 1 \times 8 \times 1 = 8$

Answer: 8

</details>

---

### Q8. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ are unit vectors and $|\bar{a}|=7$, $\bar{a} \times(\bar{b} \times \bar{c})+\bar{b} \times(\bar{c} \times \bar{a})=\frac{1}{2} \bar{a}$, then angle between the vectors $\bar{a}$ and $\overline{\mathrm{c}}$ and angle between the vectors $\overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ are respectively.

**Options:**

- **(A)** $90^{\circ}, 60^{\circ}$
- **(B)** $30^{\circ}, 60^{\circ}$
- **(C)** $90^{\circ}, 120^{\circ}$
- **(D)** $45^{\circ}, 90^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $90^{\circ}, 120^{\circ}$**

**Detailed Solution:**

Given equation is $\vec{a} \times (\vec{b} \times \vec{c}) + \vec{b} \times (\vec{c} \times \vec{a}) = \dfrac{1}{2} \vec{a}$

Using the vector triple product expansion, we have:

$(\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c} + (\vec{b} \cdot \vec{a})\vec{c} - (\vec{b} \cdot \vec{c})\vec{a} = \dfrac{1}{2} \vec{a}$

Since $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$, the terms involving $\vec{c}$ cancel out:

$(\vec{a} \cdot \vec{c})\vec{b} - (\vec{b} \cdot \vec{c})\vec{a} = \dfrac{1}{2} \vec{a}$

$(\vec{a} \cdot \vec{c})\vec{b} = \left( \vec{b} \cdot \vec{c} + \dfrac{1}{2} \right) \vec{a}$

If $\vec{a}$ and $\vec{b}$ were collinear, say $\vec{a} = k\vec{b}$, substituting this would give $k(\vec{b} \cdot \vec{c})\vec{b} = k\left(\vec{b} \cdot \vec{c} + \dfrac{1}{2}\right)\vec{b}$, which implies $k = 0$, contradicting $|\vec{a}| = 7$. Thus, $\vec{a}$ and $\vec{b}$ are non-collinear vectors.

Equating the coefficients of $\vec{a}$ and $\vec{b}$ to zero, we get:

$\vec{a} \cdot \vec{c} = 0$

$\vec{b} \cdot \vec{c} + \dfrac{1}{2} = 0$

From $\vec{a} \cdot \vec{c} = 0$, the angle between $\vec{a}$ and $\vec{c}$ is $90^{\circ}$.

From $\vec{b} \cdot \vec{c} = -\dfrac{1}{2}$, and knowing $|\vec{b}| = 1$ and $|\vec{c}| = 1$, we have:

$|\vec{b}| |\vec{c}| \cos \theta = -\dfrac{1}{2}$

$\cos \theta = -\dfrac{1}{2}$

$\theta = 120^{\circ}$

Therefore, the angle between $\vec{a}$ and $\vec{c}$ is $90^{\circ}$, and the angle between $\vec{b}$ and $\vec{c}$ is $120^{\circ}$.

Answer: $90^{\circ}, 120^{\circ}$

</details>

---

### Q9. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

if $\bar{a}, \overline{\mathrm{~b}}, \overline{\mathrm{c}}$ are non coplanar unit vectors such that $\bar{a} \times(\overline{\mathrm{b}} \times \overline{\mathrm{c}})=\frac{\overline{\mathrm{b}}+\overline{\mathrm{c}}}{\sqrt{2}}$ Then the angle between $\bar{a}$ and $\overline{\mathrm{b}}$ is

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{3 \pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3 \pi}{4}$**

**Detailed Solution:**

Using the vector triple product expansion:

$\bar{a} \times (\bar{b} \times \bar{c}) = (\bar{a} \cdot \bar{c})\bar{b} - (\bar{a} \cdot \bar{b})\bar{c}$

Given that:

$\bar{a} \times (\bar{b} \times \bar{c}) = \dfrac{1}{\sqrt{2}}\bar{b} + \dfrac{1}{\sqrt{2}}\bar{c}$

Equating the coefficients of $\bar{b}$ and $\bar{c}$ (since $\bar{a}, \bar{b}, \bar{c}$ are non-coplanar, $\bar{b}$ and $\bar{c}$ are non-collinear):

$\bar{a} \cdot \bar{c} = \dfrac{1}{\sqrt{2}}$

$-(\bar{a} \cdot \bar{b}) = \dfrac{1}{\sqrt{2}} \Rightarrow \bar{a} \cdot \bar{b} = -\dfrac{1}{\sqrt{2}}$

Let $\theta$ be the angle between $\bar{a}$ and $\bar{b}$. Since $\bar{a}$ and $\bar{b}$ are unit vectors, $|\bar{a}| = 1$ and $|\bar{b}| = 1$.

$\bar{a} \cdot \bar{b} = |\bar{a}||\bar{b}|\cos\theta = \cos\theta$

$\cos\theta = -\dfrac{1}{\sqrt{2}}$

$\theta = \dfrac{3\pi}{4}$

Answer: $\frac{3 \pi}{4}$

</details>

---

### Q10. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\begin{aligned} & \text { If } \bar{a}=4 \hat{i}+3 \hat{\mathrm{j}}+\hat{\mathrm{k}}, \quad \overline{\mathrm{b}}=\hat{i}-2 \hat{\mathrm{j}}+2 \hat{\mathrm{k}} \\ & \text { then } \bar{a} \times(\bar{a} \times(\bar{a} \times(\bar{a} \times \overline{\mathrm{b}})))=\end{aligned}$

**Options:**

- **(A)** $676 \bar{a}$
- **(B)** $676 \overline{\mathrm{~b}}$
- **(C)** $625 \bar{a}$
- **(D)** $625 \overline{\mathrm{~b}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $676 \overline{\mathrm{~b}}$**

**Detailed Solution:**

Given $\bar{a} = 4\hat{i} + 3\hat{j} + \hat{k}$ and $\bar{b} = \hat{i} - 2\hat{j} + 2\hat{k}$.

First, we find the dot products $\bar{a} \cdot \bar{a}$ and $\bar{a} \cdot \bar{b}$:

$\bar{a} \cdot \bar{a} = |\bar{a}|^2 = (4)^2 + (3)^2 + (1)^2 = 16 + 9 + 1 = 26$

$\bar{a} \cdot \bar{b} = (4)(1) + (3)(-2) + (1)(2) = 4 - 6 + 2 = 0$

Using the vector triple product expansion, $\bar{a} \times (\bar{a} \times \bar{b}) = (\bar{a} \cdot \bar{b})\bar{a} - (\bar{a} \cdot \bar{a})\bar{b}$.

Substituting the values, we get:

$\bar{a} \times (\bar{a} \times \bar{b}) = (0)\bar{a} - (26)\bar{b} = -26\bar{b}$

Now, we need to evaluate $\bar{a} \times (\bar{a} \times (\bar{a} \times (\bar{a} \times \bar{b})))$:

$\bar{a} \times (\bar{a} \times (\bar{a} \times (\bar{a} \times \bar{b}))) = \bar{a} \times (\bar{a} \times (-26\bar{b}))$

$= -26 [\bar{a} \times (\bar{a} \times \bar{b})]$

$= -26 (-26\bar{b})$

$= 676\bar{b}$

Answer: $676 \overline{\mathrm{~b}}$

</details>

---

### Q11. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overline{\mathrm{a}}, \overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ be three non-zero vectors such that no two of them are collinear and $\left.(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}=\frac{1}{3}|\overline{\mathrm{~b}}| \overline{\mathrm{c}} \right\rvert\, \overline{\mathrm{a}}$. If $\theta$ is the angle between vectors $\bar{b}$ and $\bar{c}$, then the value of $\sin \theta$ is

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{-2 \sqrt{2}}{3}$
- **(C)** $\frac{2 \sqrt{2}}{3}$
- **(D)** $\frac{-\sqrt{2}}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2 \sqrt{2}}{3}$**

**Detailed Solution:**

Using the vector triple product formula:

$(\bar{a} \times \bar{b}) \times \bar{c} = (\bar{a} \cdot \bar{c})\bar{b} - (\bar{b} \cdot \bar{c})\bar{a}$

Given that $(\bar{a} \times \bar{b}) \times \bar{c} = \dfrac{1}{3}|\bar{b}||\bar{c}|\bar{a}$, equating the two expressions gives:

$(\bar{a} \cdot \bar{c})\bar{b} - (\bar{b} \cdot \bar{c})\bar{a} = \dfrac{1}{3}|\bar{b}||\bar{c}|\bar{a}$

Since $\bar{a}$ and $\bar{b}$ are non-collinear vectors, their coefficients on both sides must be equal. Comparing the coefficients of $\bar{a}$ and $\bar{b}$:

$\bar{a} \cdot \bar{c} = 0$

$-(\bar{b} \cdot \bar{c}) = \dfrac{1}{3}|\bar{b}||\bar{c}|$

Using the dot product formula $\bar{b} \cdot \bar{c} = |\bar{b}||\bar{c}|\cos \theta$, where $\theta$ is the angle between $\bar{b}$ and $\bar{c}$:

$-|\bar{b}||\bar{c}|\cos \theta = \dfrac{1}{3}|\bar{b}||\bar{c}|$

$\cos \theta = -\dfrac{1}{3}$

Since $\theta$ is the angle between two vectors, $0 \le \theta \le \pi$, which means $\sin \theta \ge 0$.

$\sin \theta = \sqrt{1 - \cos^2 \theta} = \sqrt{1 - \left(-\dfrac{1}{3}\right)^2}$

$\sin \theta = \sqrt{1 - \dfrac{1}{9}} = \sqrt{\dfrac{8}{9}} = \dfrac{2\sqrt{2}}{3}$

Answer: $\frac{2 \sqrt{2}}{3}$

</details>

---

### Q12. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overline{\mathrm{a}}=2 \hat{i}+\hat{j}-2 \hat{k}$ and $\bar{b}=\hat{i}+\hat{j}$. If $\bar{c}$ is a vector such that $\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=|\overline{\mathrm{c}}|,|\overline{\mathrm{c}}-\overline{\mathrm{a}}|=2 \sqrt{2}$ and the angle between $(\overline{\mathrm{a}} \times \overline{\mathrm{b}})$ and $\overline{\mathrm{c}}$ is $30^{\circ}$, then $|(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}|$ is equal to

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** $\frac{2}{3}$
- **(C)** $-\frac{3}{2}$
- **(D)** $-\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{2}$**

**Detailed Solution:**

Given $\overline{a} = 2\hat{i} + \hat{j} - 2\hat{k}$ and $\overline{b} = \hat{i} + \hat{j}$.

The magnitude of $\overline{a}$ is:
$|\overline{a}| = \sqrt{2^2 + 1^2 + (-2)^2} = \sqrt{9} = 3$

We are given $|\overline{c} - \overline{a}| = 2\sqrt{2}$. Squaring both sides, we get:
$|\overline{c}|^2 + |\overline{a}|^2 - 2(\overline{a} \cdot \overline{c}) = 8$

Substituting $|\overline{a}| = 3$ and the given condition $\overline{a} \cdot \overline{c} = |\overline{c}|$:
$|\overline{c}|^2 + 9 - 2|\overline{c}| = 8$

$|\overline{c}|^2 - 2|\overline{c}| + 1 = 0$

$(|\overline{c}| - 1)^2 = 0 \Rightarrow |\overline{c}| = 1$

Now, we find the cross product $\overline{a} \times \overline{b}$:
$\overline{a} \times \overline{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & -2 \\ 1 & 1 & 0 \end{vmatrix} = \hat{i}(0 - (-2)) - \hat{j}(0 - (-2)) + \hat{k}(2 - 1) = 2\hat{i} - 2\hat{j} + \hat{k}$

The magnitude of $\overline{a} \times \overline{b}$ is:
$|\overline{a} \times \overline{b}| = \sqrt{2^2 + (-2)^2 + 1^2} = \sqrt{9} = 3$

The angle between $(\overline{a} \times \overline{b})$ and $\overline{c}$ is $30^{\circ}$. The magnitude of their cross product is:
$|(\overline{a} \times \overline{b}) \times \overline{c}| = |\overline{a} \times \overline{b}| |\overline{c}| \sin 30^{\circ}$

$|(\overline{a} \times \overline{b}) \times \overline{c}| = 3 \times 1 \times \dfrac{1}{2} = \dfrac{3}{2}$

Answer: $\frac{3}{2}$

</details>

---

### Q13. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}, \bar{b}, \bar{c}$ are non-coplanar unit vectors such that $\overline{\mathrm{a}} \times(\overline{\mathrm{b}} \times \overline{\mathrm{c}})=\frac{(\overline{\mathrm{b}}+\overline{\mathrm{c}})}{\sqrt{2}}$ then the angle between $\overline{\mathrm{a}}$ and $\bar{b}$ is

**Options:**

- **(A)** $\frac{3 \pi}{4}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{2}$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3 \pi}{4}$**

**Detailed Solution:**

Using the vector triple product expansion:

$\bar{a} \times (\bar{b} \times \bar{c}) = (\bar{a} \cdot \bar{c})\bar{b} - (\bar{a} \cdot \bar{b})\bar{c}$

Given that:

$\bar{a} \times (\bar{b} \times \bar{c}) = \dfrac{\bar{b} + \bar{c}}{\sqrt{2}}$

Equating the two expressions:

$(\bar{a} \cdot \bar{c})\bar{b} - (\bar{a} \cdot \bar{b})\bar{c} = \dfrac{1}{\sqrt{2}}\bar{b} + \dfrac{1}{\sqrt{2}}\bar{c}$

Since $\bar{a}, \bar{b}, \bar{c}$ are non-coplanar, $\bar{b}$ and $\bar{c}$ are non-collinear. Equating the coefficients of $\bar{b}$ and $\bar{c}$ on both sides gives:

$\bar{a} \cdot \bar{c} = \dfrac{1}{\sqrt{2}}$

$-(\bar{a} \cdot \bar{b}) = \dfrac{1}{\sqrt{2}} \Rightarrow \bar{a} \cdot \bar{b} = -\dfrac{1}{\sqrt{2}}$

Let $\theta$ be the angle between $\bar{a}$ and $\bar{b}$. Since they are unit vectors, $|\bar{a}| = 1$ and $|\bar{b}| = 1$.

$\bar{a} \cdot \bar{b} = |\bar{a}||\bar{b}|\cos\theta = \cos\theta$

$\cos\theta = -\dfrac{1}{\sqrt{2}}$

$\theta = \dfrac{3\pi}{4}$

Answer: $\frac{3 \pi}{4}$

</details>

---

### Q14. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\bar{a}, \bar{b}$ and $\bar{c}$ be three unit vectors such that $\bar{a} \times(\bar{b} \times \bar{c})=\frac{\sqrt{3}}{2}(\bar{b}+\bar{c})$.
If $\bar{b}$ is not parallel to $\bar{c}$, then the angle between $\bar{a}$ and $\bar{b}$ is

**Options:**

- **(A)** $\frac{3 \pi}{4}$
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{2 \pi}{3}$
- **(D)** $\frac{5 \pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{5 \pi}{6}$**

**Detailed Solution:**

Using the vector triple product expansion, we have:

$\bar{a} \times (\bar{b} \times \bar{c}) = (\bar{a} \cdot \bar{c})\bar{b} - (\bar{a} \cdot \bar{b})\bar{c}$

Equating this to the given expression:

$(\bar{a} \cdot \bar{c})\bar{b} - (\bar{a} \cdot \bar{b})\bar{c} = \dfrac{\sqrt{3}}{2}\bar{b} + \dfrac{\sqrt{3}}{2}\bar{c}$

Since $\bar{b}$ and $\bar{c}$ are not parallel, they are linearly independent. We can equate their respective coefficients:

$\bar{a} \cdot \bar{c} = \dfrac{\sqrt{3}}{2}$

$-(\bar{a} \cdot \bar{b}) = \dfrac{\sqrt{3}}{2} \Rightarrow \bar{a} \cdot \bar{b} = -\dfrac{\sqrt{3}}{2}$

Let $\theta$ be the angle between $\bar{a}$ and $\bar{b}$. Since $\bar{a}$ and $\bar{b}$ are unit vectors, $|\bar{a}| = 1$ and $|\bar{b}| = 1$.

$\bar{a} \cdot \bar{b} = |\bar{a}||\bar{b}|\cos\theta = \cos\theta$

$\cos\theta = -\dfrac{\sqrt{3}}{2}$

$\theta = \dfrac{5\pi}{6}$

Answer: $\frac{5 \pi}{6}$

</details>

---

### Q15. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{a}}=\dfrac{1}{\sqrt{10}}(4 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+\hat{\mathrm{k}}), \overline{\mathrm{b}}=\dfrac{1}{5}(\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+2 \hat{\mathrm{k}})$, then the value of $(2 \bar{a}-\bar{b}) \cdot\{(\bar{a} \times \bar{b}) \times(\bar{a}+2 \bar{b})\}$ is

**Options:**

- **(A)** 5
- **(B)** -3
- **(C)** -5
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -5**

**Detailed Solution:**

Given $\overline{a} = \dfrac{1}{\sqrt{10}}(4\hat{i} - 3\hat{j} + \hat{k})$ and $\overline{b} = \dfrac{1}{5}(\hat{i} + 2\hat{j} + 2\hat{k})$.

First, we find the dot product $\overline{a} \cdot \overline{b}$:

$\overline{a} \cdot \overline{b} = \dfrac{1}{5\sqrt{10}} (4(1) - 3(2) + 1(2)) = \dfrac{1}{5\sqrt{10}} (4 - 6 + 2) = 0$

Next, simplify the vector triple product expression:

$\overline{v} = (\overline{a} \times \overline{b}) \times (\overline{a} + 2\overline{b}) = (\overline{a} \times \overline{b}) \times \overline{a} + 2(\overline{a} \times \overline{b}) \times \overline{b}$

Using the vector triple product expansion $(\overline{x} \times \overline{y}) \times \overline{z} = (\overline{x} \cdot \overline{z})\overline{y} - (\overline{y} \cdot \overline{z})\overline{x}$:

$(\overline{a} \times \overline{b}) \times \overline{a} = (\overline{a} \cdot \overline{a})\overline{b} - (\overline{b} \cdot \overline{a})\overline{a} = |\overline{a}|^2 \overline{b}$

$(\overline{a} \times \overline{b}) \times \overline{b} = (\overline{a} \cdot \overline{b})\overline{b} - (\overline{b} \cdot \overline{b})\overline{a} = -|\overline{b}|^2 \overline{a}$

Thus, $\overline{v} = |\overline{a}|^2 \overline{b} - 2|\overline{b}|^2 \overline{a}$.

Now, compute the dot product with $(2\overline{a} - \overline{b})$:

$(2\overline{a} - \overline{b}) \cdot \overline{v} = (2\overline{a} - \overline{b}) \cdot (|\overline{a}|^2 \overline{b} - 2|\overline{b}|^2 \overline{a})$

Expanding the dot product:

$= 2|\overline{a}|^2 (\overline{a} \cdot \overline{b}) - 4|\overline{a}|^2 |\overline{b}|^2 - |\overline{a}|^2 |\overline{b}|^2 + 2|\overline{b}|^2 (\overline{a} \cdot \overline{b})$

Since $\overline{a} \cdot \overline{b} = 0$, this reduces to:

$= -5|\overline{a}|^2 |\overline{b}|^2$

Assuming the intended vectors are unit vectors (as is standard when such typos occur in magnitudes in the problem statement), we have $|\overline{a}|^2 = 1$ and $|\overline{b}|^2 = 1$.

Therefore, the value is $-5(1)(1) = -5$.

Answer: -5

</details>

---

### Q16. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\overline{\mathrm{a}}=\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}$ and $\bar{b}=\hat{i} \times(\bar{a} \times \hat{i})+\hat{j} \times(\bar{a} \times \hat{j})+\hat{k} \times(\bar{a} \times \hat{k})$ then $|\vec{b}|$ is

**Options:**

- **(A)** $\sqrt{12}$
- **(B)** $2 \sqrt{12}$
- **(C)** $3 \sqrt{14}$
- **(D)** $2 \sqrt{14}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 \sqrt{14}$**

**Detailed Solution:**

Using the vector triple product formula $\vec{x} \times (\vec{y} \times \vec{z}) = (\vec{x} \cdot \vec{z})\vec{y} - (\vec{x} \cdot \vec{y})\vec{z}$, we can expand each term in the expression for $\vec{b}$.

$\hat{i} \times (\vec{a} \times \hat{i}) = (\hat{i} \cdot \hat{i})\vec{a} - (\hat{i} \cdot \vec{a})\hat{i} = \vec{a} - a_1 \hat{i}$

$\hat{j} \times (\vec{a} \times \hat{j}) = (\hat{j} \cdot \hat{j})\vec{a} - (\hat{j} \cdot \vec{a})\hat{j} = \vec{a} - a_2 \hat{j}$

$\hat{k} \times (\vec{a} \times \hat{k}) = (\hat{k} \cdot \hat{k})\vec{a} - (\hat{k} \cdot \vec{a})\hat{k} = \vec{a} - a_3 \hat{k}$

Adding these three expressions gives:

$\vec{b} = 3\vec{a} - (a_1 \hat{i} + a_2 \hat{j} + a_3 \hat{k})$

Since $a_1 \hat{i} + a_2 \hat{j} + a_3 \hat{k} = \vec{a}$, we get:

$\vec{b} = 3\vec{a} - \vec{a} = 2\vec{a}$

Given $\vec{a} = \hat{i} + 2\hat{j} + 3\hat{k}$, its magnitude is:

$|\vec{a}| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{1 + 4 + 9} = \sqrt{14}$

Therefore, the magnitude of $\vec{b}$ is:

$|\vec{b}| = |2\vec{a}| = 2|\vec{a}| = 2\sqrt{14}$

Answer: $2 \sqrt{14}$

</details>

---

### Q17. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\hat{a}, \hat{b}$, and $\hat{c}$ are three unit vectors such that $\hat{a} \times(\hat{b} \times \hat{c})=\dfrac{\sqrt{3}}{2}(\hat{b}+\hat{c})$. If $\vec{b}$ is not parallel to $\hat{c}$, then the angle between $\hat{a}$ and $\hat{b}$ is

**Options:**

- **(A)** $\dfrac{5 \pi}{6}$
- **(B)** $\dfrac{\pi}{6}$
- **(C)** $\dfrac{\pi}{3}$
- **(D)** $\dfrac{2 \pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{5 \pi}{6}$**

**Detailed Solution:**

Given the equation:

$\hat{a} \times (\hat{b} \times \hat{c}) = \dfrac{\sqrt{3}}{2}(\hat{b} + \hat{c})$

Using the vector triple product expansion formula, $\vec{A} \times (\vec{B} \times \vec{C}) = (\vec{A} \cdot \vec{C})\vec{B} - (\vec{A} \cdot \vec{B})\vec{C}$, we can expand the left side:

$(\hat{a} \cdot \hat{c})\hat{b} - (\hat{a} \cdot \hat{b})\hat{c} = \dfrac{\sqrt{3}}{2}\hat{b} + \dfrac{\sqrt{3}}{2}\hat{c}$

Since $\hat{b}$ and $\hat{c}$ are not parallel, they are linearly independent vectors. We can equate their respective coefficients on both sides:

$\hat{a} \cdot \hat{c} = \dfrac{\sqrt{3}}{2}$

$-(\hat{a} \cdot \hat{b}) = \dfrac{\sqrt{3}}{2} \Rightarrow \hat{a} \cdot \hat{b} = -\dfrac{\sqrt{3}}{2}$

Let $\theta$ be the angle between the unit vectors $\hat{a}$ and $\hat{b}$. Then:

$|\hat{a}| |\hat{b}| \cos\theta = -\dfrac{\sqrt{3}}{2}$

Since $|\hat{a}| = 1$ and $|\hat{b}| = 1$:

$\cos\theta = -\dfrac{\sqrt{3}}{2}$

$\theta = \dfrac{5\pi}{6}$

Answer: $\dfrac{5 \pi}{6}$

</details>

---

### Q18. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A, B, C, D are four points in a plane with position vectors $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}, \overline{\mathrm{d}}$ respectively such that $(\overline{\mathrm{a}}-\overline{\mathrm{d}}) \cdot(\overline{\mathrm{b}}-\overline{\mathrm{c}})=(\overline{\mathrm{b}}-\overline{\mathrm{d}}) \cdot(\overline{\mathrm{c}}-\overline{\mathrm{a}})=0$. The point $\mathrm{D}$, then is the of $\triangle \mathrm{ABC}$

**Options:**

- **(A)** centroid
- **(B)** circumcentre
- **(C)** incentre
- **(D)** orthocentre

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) orthocentre**

**Detailed Solution:**

$\begin{aligned} & (\overline{\mathrm{a}}-\overline{\mathrm{d}}) \cdot(\overline{\mathrm{b}}-\overline{\mathrm{c}})=(\overline{\mathrm{b}}-\overline{\mathrm{d}})(\overline{\mathrm{c}}-\overline{\mathrm{a}})=0 \\ & \overline{\mathrm{AD}} \cdot \overline{\mathrm{BC}}=\overline{\mathrm{BD}} \cdot \overline{\mathrm{CA}}=0 \\ & \Rightarrow \overline{\mathrm{AD}} \perp \overline{\mathrm{BC}} \text { and } \overline{\mathrm{BD}} \perp \overline{\mathrm{CA}}\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/NwONFZQr6tyVmjmZ56MuONLm46lIj0-5FSx2eCG1l20.original.fullsize.png">

$\Rightarrow D$ is the orthocentre of $\triangle A B C$.

</details>

---

### Q19. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Two adjacent sides of a parallelogram $\mathrm{ABCD}$ are given by $\overline{\mathrm{AB}}=2 \hat{\mathrm{i}}+10 \hat{\mathrm{j}}+11 \hat{\mathrm{k}}$ and $\overline{\mathrm{AD}}=-\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}$. The side $\mathrm{AD}$ is potated by an acute angle $\alpha$ in the plane of parallelogram so that $\mathrm{AD}$ becomes $\mathrm{AD}^{\prime}$. If $\mathrm{AD}^{\prime}$ makes a right angle with side $\mathrm{AB}$, then the cosine of the angle $\alpha$ is given by

**Options:**

- **(A)** $\frac{8}{9}$
- **(B)** $\frac{\sqrt{17}}{9}$
- **(C)** $\frac{1}{9}$
- **(D)** $\frac{4 \sqrt{5}}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\sqrt{17}}{9}$**

**Detailed Solution:**

Let $\theta$ be the angle between $\overline{\mathrm{AB}}$ and $\overline{\mathrm{AD}}$
$$
\begin{aligned}
\therefore \quad \cos \theta & =\frac{\overline{\mathrm{AB}} \cdot \overline{\mathrm{AD}}}{|\overline{\mathrm{AB}}||\overline{\mathrm{AD}}|} \\
& =\frac{(2 \hat{\mathrm{i}}+10 \hat{\mathrm{j}}+11 \hat{\mathrm{k}}) \cdot(-\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+2 \hat{\mathrm{k}})}{\sqrt{4+100+121} \sqrt{1+4+4}} \\
& =\frac{-2+20+22}{\sqrt{225} \sqrt{9}} \\
& =\frac{40}{45} \\
& =\frac{8}{9} \\
\therefore \quad \sin \theta & =\sqrt{1-\left(\frac{8}{9}\right)^2}=\frac{\sqrt{17}}{9}
\end{aligned}
$$
$\alpha$ is the angle of rotation of $A D$.
$\therefore \quad$ The angle between side $\mathrm{AB}$ and $\mathrm{AD}$
$$
\begin{aligned}
& =\alpha+\theta \\
& =90^{\circ}
\end{aligned}
$$
$$
\begin{aligned}
& \therefore \quad \cos (\alpha+\theta)=\cos \left(90^{\circ}\right) \\
& \therefore \quad \cos \alpha \cos \theta-\sin \alpha \sin \theta=0 \\
& \therefore \quad 8 \cos \alpha=\sqrt{17} \sin \alpha \\
& \therefore \quad 64 \cos ^2 \alpha=17\left(1-\cos ^2 \alpha\right) \\
& \therefore \quad 81 \cos ^2 \alpha=17 \\
& \therefore \quad \cos \alpha=\frac{\sqrt{17}}{9}
\end{aligned}
$$

</details>

---

### Q20. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\bar{a}=2 \hat{i}+\hat{j}-2 \hat{k}, \bar{b}=\hat{i}+\hat{j}$ and $\bar{c}$ be a vector such that $|\overline{\mathrm{c}}-\overline{\mathrm{a}}|=4, \quad|(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}|=3$ and the angle between $\overline{\mathrm{c}}$ and $\overline{\mathrm{a}} \times \overline{\mathrm{b}}$ is $\frac{\pi}{6}$, then $\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}$ is equal to

**Options:**

- **(A)** $-3$
- **(B)** $\frac{3}{2}$
- **(C)** $3$
- **(D)** $\frac{-3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{-3}{2}$**

**Detailed Solution:**

$\begin{array}{ll} & \overline{\mathrm{a}}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-2 \hat{\mathrm{k}}, \overline{\mathrm{b}}=\hat{\mathrm{i}}+\hat{\mathrm{j}} \\ \therefore \quad & |\overline{\mathrm{a}}|=\sqrt{4+1+4}=3 \\ & \overline{\mathrm{a}} \times \overline{\mathrm{b}}=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 2 & 1 & -2 \\ 1 & 1 & 0\end{array}\right|=2 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}} \\ \therefore \quad & |\overline{\mathrm{a}} \times \overline{\mathrm{b}}|=\sqrt{4+4+1}=3\end{array}$
$\text { Angle between } \overline{\mathrm{c}} \text { and } \overline{\mathrm{a}} \times \overline{\mathrm{b}} \text { is } \frac{\pi}{6} \quad \ldots \text { [Given] }$
$\begin{aligned} \therefore \quad & \sin \frac{\pi}{6}=\frac{|(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}|}{|\overline{\mathrm{a}} \times \overline{\mathrm{b}} \| \overline{\mathrm{c}}|} \\ & \frac{1}{2}=\frac{3}{3 \times|\overline{\mathrm{c}}|} \Rightarrow|\overline{\mathrm{c}}|=2\end{aligned}$
Now, $|\bar{c}-\bar{a}|=4$.. [Given]
$\begin{aligned} & \Rightarrow|\bar{c}|^2+|\bar{a}|^2-2 \bar{a} \cdot \bar{c}=16 \\ & \Rightarrow 4+9-2 a \cdot c=16 \\ & \Rightarrow a \cdot c=\frac{-3}{2}\end{aligned}$

</details>

---

### Q21. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overline{\mathrm{a}}, \overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ be three unit vectors such that $\overline{\mathrm{a}} \times(\overline{\mathrm{b}} \times \overline{\mathrm{c}})=\frac{\sqrt{3}}{2}(\overline{\mathrm{b}}+\overline{\mathrm{c}})$. If $\overline{\mathrm{b}}$ is not parallel to $\overline{\mathrm{c}}$, then the angle between $\bar{a}$ and $\bar{b}$ is

**Options:**

- **(A)** $\frac{5 \pi}{6}$
- **(B)** $\frac{2 \pi}{3}$
- **(C)** $\frac{\pi}{6}$
- **(D)** $\frac{\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{5 \pi}{6}$**

**Detailed Solution:**

$$
\begin{aligned}
& \overline{\mathrm{a}} \times(\overline{\mathrm{b}} \times \overline{\mathrm{c}})=\frac{\sqrt{3}}{2}(\overline{\mathrm{b}}+\overline{\mathrm{c}}) \\
& \Rightarrow(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) \overline{\mathrm{b}}-(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}) \overline{\mathrm{c}}=\frac{\sqrt{3}}{2} \overline{\mathrm{b}}+\frac{\sqrt{3}}{2} \overline{\mathrm{c}}
\end{aligned}
$$

On comparing, we get
$$
\begin{aligned}
& \overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=\frac{\sqrt{3}}{2} \text { and } \overline{\mathrm{a}} \cdot \overline{\mathrm{b}}=-\frac{\sqrt{3}}{2} \\
& \Rightarrow|\overline{\mathrm{a}}||\overline{\mathrm{b}}| \cos \theta=-\frac{\sqrt{3}}{2} \\
& \Rightarrow \cos \theta=-\frac{\sqrt{3}}{2} \\
& \Rightarrow \theta=\frac{5 \pi}{6}
\end{aligned}
$$

</details>

---

### Q22. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\overline{\mathrm{a}}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-2 \hat{\mathrm{k}}$ and $\overline{\mathrm{b}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}$. If $\overline{\mathrm{c}}$ is a vector such that $\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}=|\overline{\mathrm{c}}|,|\overline{\mathrm{c}}-\overline{\mathrm{a}}|=2 \sqrt{2}$ and the angle between $(\overline{\mathrm{a}} \times \overline{\mathrm{b}})$ and $\overline{\mathrm{c}}$ is $\frac{\pi}{6}$, then $|(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}|$ is

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** $\frac{2}{3}$
- **(C)** $1$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{2}$**

**Detailed Solution:**

$$
\begin{aligned}
& |\overline{\mathrm{c}}-\overline{\mathrm{a}}|^2=2 \sqrt{2} \\
& \Rightarrow|\overline{\mathrm{c}}|^2+|\overline{\mathrm{a}}|^2-2(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}})=8 \\
& \Rightarrow|\overline{\mathrm{c}}|^2+9-2|\overline{\mathrm{c}}|=8 \\
& \Rightarrow\left(|\overline{\mathrm{c}}|^{-1}\right)^2=0 \\
& \Rightarrow|\overline{\mathrm{c}}|^2=1
\end{aligned}
$$

Now,
$$
\begin{aligned}
|(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}| & =|(\overline{\mathrm{a}} \times \overline{\mathrm{b}})||\overline{\mathrm{c}}| \sin \frac{\pi}{6} \\
& =|\overline{\mathrm{a}} \times \overline{\mathrm{b}}|(1)\left(\frac{1}{2}\right) \quad \ldots[\text { From (i) }] \\
& =\frac{3}{2} \quad \ldots[\because \overline{\mathrm{a}} \times \overline{\mathrm{b}}=2 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}}]
\end{aligned}
$$

</details>

---

### Q23. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $[\bar{a} \bar{b} \bar{c}]=4$, then the volume (in cubic units) of the parallelepiped with $\overline{\mathrm{a}}+2 \overline{\mathrm{b}}, \overline{\mathrm{b}}+2 \overline{\mathrm{c}}$ and $\overline{\mathrm{c}}+2 \overline{\mathrm{a}}$ as coterminal edges, is

**Options:**

- **(A)** 32
- **(B)** 16
- **(C)** 9
- **(D)** 36

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 36**

**Detailed Solution:**

We have $\bar{a} \cdot(\bar{b} \times \bar{c})=4$
Volume of required parallelepiped is
$$
\begin{aligned}
& (\overline{\mathrm{a}}+2 \overline{\mathrm{b}}) \cdot[(\overline{\mathrm{b}}+2 \overline{\mathrm{c}}) \times \overline{\mathrm{c}}+2 \overline{\mathrm{a}}] \\
& =(\overline{\mathrm{a}}+2 \overline{\mathrm{b}}) \cdot[(\overline{\mathrm{b}} \times \overline{\mathrm{c}})+2(\overline{\mathrm{c}} \times \overline{\mathrm{c}})+2(\overline{\mathrm{b}} \times \overline{\mathrm{a}})+4(\overline{\mathrm{c}} \times \overline{\mathrm{a}})] \\
& =\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})+\overline{\mathrm{a}}(0)+2 \overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{a}})+4 \overline{\mathrm{a}} \cdot(\overline{\mathrm{c}} \times \overline{\mathrm{a}})+2 \overline{\mathrm{b}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}}) \\
& +4 \overline{\mathrm{b}}(0)+4 \overline{\mathrm{b}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{a}})+8 \overline{\mathrm{b}} \cdot(\overline{\mathrm{c}} \times \overline{\mathrm{a}}) \\
& =\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})+0+0+0+0+0+0+8 \overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}}) \\
& =9[\overline{\mathrm{a}} \cdot(\overline{\mathrm{b}} \times \overline{\mathrm{c}})]=9(4)=36
\end{aligned}
$$

</details>

---

### Q24. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mover accent="true"><mrow><mi>p</mi></mrow><mo>-</mo></mover><mo>,</mo><mi></mi><mi></mi><mover accent="true"><mrow><mi>q</mi></mrow><mo>-</mo></mover></math> and <math><mover accent="true"><mrow><mi>r</mi></mrow><mo>-</mo></mover></math> are non-zero, non-coplanar vectors, then <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>p</mi></mrow><mo>-</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>q</mi></mrow><mo>-</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>r</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>p</mi></mrow><mo>-</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>q</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>q</mi></mrow><mo>-</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>r</mi></mrow><mo>-</mo></mover></mtd></mtr></mtable></mrow></mfenced><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mn>3</mn><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>p</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>q</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>r</mi></mrow><mo>-</mo></mover></mtd></mtr></mtable></mrow></mfenced></math>
- **(B)** <math><mn>0</mn></math>
- **(C)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>p</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>q</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>r</mi></mrow><mo>-</mo></mover></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>p</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>q</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>r</mi></mrow><mo>-</mo></mover></mtd></mtr></mtable></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>p</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>q</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>r</mi></mrow><mo>-</mo></mover></mtd></mtr></mtable></mrow></mfenced></math>**

**Detailed Solution:**

Since, <math><mi>p</mi><mo>,</mo><mi></mi><mi>q</mi><mo>,</mo><mi></mi><mi>r</mi></math> non-zero, non-coplanar vectors then, <math><mfenced close="]" open="[" separators="|"><mrow><mover accent="false"><mrow><mi>p</mi></mrow><mo>¯</mo></mover><mo>+</mo><mover accent="false"><mrow><mi>q</mi></mrow><mo>¯</mo></mover><mo>-</mo><mover accent="false"><mrow><mi>r</mi><mo>,</mo></mrow><mo>¯</mo></mover><mover accent="false"><mrow><mi mathvariant="normal"></mi><mi>p</mi></mrow><mo>¯</mo></mover><mo>-</mo><mover accent="false"><mrow><mi>q</mi><mo>,</mo></mrow><mo>¯</mo></mover><mover accent="false"><mrow><mi mathvariant="normal"></mi><mi>q</mi></mrow><mo>¯</mo></mover><mo>-</mo><mover accent="false"><mrow><mi>r</mi></mrow><mo>¯</mo></mover></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable columnalign="left"><mtr><mtd><mn>1</mn><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mn>1</mn><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mo>-</mo><mn>1</mn><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mn>1</mn><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi>p</mi></mtd><mtd><mi>q</mi></mtd><mtd><mi>r</mi></mtd></mtr></mtable></mrow></mfenced></math>  
<math><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi>p</mi></mtd><mtd><mi>q</mi></mtd><mtd><mi>r</mi></mtd></mtr></mtable></mrow></mfenced></math>  
<math><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi>p</mi></mtd><mtd><mi>q</mi></mtd><mtd><mi>r</mi></mtd></mtr></mtable></mrow></mfenced></math>

</details>

---

### Q25. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>-</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>-</mo></mover><mo>,</mo><mi></mi><mover accent="true"><mrow><mi></mi><mi>b</mi></mrow><mo>-</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>-</mo></mover></math> and <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>-</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>-</mo></mover></math> are coterminous edges of a parallelepiped, then its volume is ________

**Options:**

- **(A)** <math><mn>3</mn><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>a</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>c</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>b</mi></mrow><mo>-</mo></mover></mtd></mtr></mtable></mrow></mfenced></math>
- **(B)** <math><mn>0</mn></math>
- **(C)** <math><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>a</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>b</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>c</mi></mrow><mo>-</mo></mover></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math><mn>4</mn><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>b</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>a</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>c</mi></mrow><mo>-</mo></mover></mtd></mtr></mtable></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>a</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>b</mi></mrow><mo>-</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>c</mi></mrow><mo>-</mo></mover></mtd></mtr></mtable></mrow></mfenced></math>**

**Detailed Solution:**

<math><mo>∵</mo></math> Volume of a parallelelopiped whose, Coterminous edges are <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>-</mo></mover><mo>,</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>-</mo></mover><mo>,</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>-</mo></mover><mo> </mo><mo> </mo><mi>i</mi><mi>s</mi></math>  
<math><mi>v</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mover accent="true"><mrow><mi>a</mi></mrow><mo>-</mo></mover><mi></mi><mover accent="true"><mrow><mi>b</mi></mrow><mo>-</mo></mover><mi></mi><mover accent="true"><mrow><mi>c</mi></mrow><mo>-</mo></mover></mrow></mfenced></math> …  (1) 
Then, required volume = <math><mfenced close="]" open="[" separators="|"><mrow><mover accent="true"><mrow><mi>a</mi></mrow><mo>-</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>-</mo></mover><mo>,</mo><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mover accent="true"><mrow><mi>b</mi></mrow><mo>-</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>-</mo></mover><mo>,</mo><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mover accent="true"><mrow><mi>c</mi></mrow><mo>-</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>-</mo></mover></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><mover accent="true"><mrow><mi>a</mi></mrow><mo>-</mo></mover><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mover accent="true"><mrow><mi>b</mi></mrow><mo>-</mo></mover><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mover accent="true"><mrow><mi>c</mi></mrow><mo>-</mo></mover></mrow></mfenced></math>

</details>

---

### Q26. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following is not equal to <math><mi></mi><mi>w</mi><mo>.</mo><mfenced separators="|"><mrow><mi>u</mi><mo>×</mo><mi>v</mi></mrow></mfenced><mo>?</mo></math>

**Options:**

- **(A)** <math><mi>u</mi><mo>.</mo><mfenced separators="|"><mrow><mi>v</mi><mo>×</mo><mi>w</mi></mrow></mfenced></math>
- **(B)** <math><mi>v</mi><mo>.</mo><mfenced separators="|"><mrow><mi>w</mi><mo>×</mo><mi>u</mi></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mi>u</mi><mo>×</mo><mi>v</mi></mrow></mfenced><mo>.</mo><mi>w</mi></math>
- **(D)** <math><mi>v</mi><mo>.</mo><mfenced separators="|"><mrow><mi>u</mi><mo>×</mo><mi>w</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>v</mi><mo>.</mo><mfenced separators="|"><mrow><mi>u</mi><mo>×</mo><mi>w</mi></mrow></mfenced></math>**

**Detailed Solution:**

Key Idea Use 
<math><mfenced separators="|"><mrow><mi>a</mi><mo>×</mo><mi>b</mi></mrow></mfenced><mo>.</mo><mi>c</mi><mo>=</mo><mfenced separators="|"><mrow><mi>b</mi><mo>×</mo><mi>c</mi></mrow></mfenced><mo>.</mo><mi>a</mi><mo>=</mo><mfenced separators="|"><mrow><mi>c</mi><mo>×</mo><mi>a</mi></mrow></mfenced><mo>.</mo><mi>b</mi></math>  
<math><mo>∴</mo><mi>w</mi><mo>.</mo><mfenced separators="|"><mrow><mi>u</mi><mo>×</mo><mi>v</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>v</mi><mo>.</mo><mfenced separators="|"><mrow><mi>u</mi><mo>×</mo><mi>w</mi></mrow></mfenced></math>

</details>

---

### Q27. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If A, B, C and D are <math><mfenced separators="|"><mrow><mn>3,7</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced separators="|"><mrow><mn>5</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced separators="|"><mrow><mo>-</mo><mn>4,5</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math> and <math><mfenced separators="|"><mrow><mn>1,2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> respectively, then the volume of the parallelepiped with AB, AC and AD as the co-terminus edges, is ….cubic units.

**Options:**

- **(A)** 91
- **(B)** 94
- **(C)** 92
- **(D)** 93

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 92**

**Detailed Solution:**

We have 
<math><mi>A</mi><mi>B</mi><mo>=</mo><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>  
<math><mo>=</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>9</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>  
<math><mi>A</mi><mi>C</mi><mo>=</mo><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mn>6</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>  
<math><mo>=</mo><mo>-</mo><mn>7</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>  
and <math><mi>A</mi><mi>D</mi><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>  
<math><mo>=</mo><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>  
<math><mo>∴</mo></math> Volume of the parallelepiped with AB, AC and AD on the co-terminus edges 
<math><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>A</mi><mi>B</mi><mi>A</mi><mi>C</mi><mi>A</mi><mi>D</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>9</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>7</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></mrow></mfenced></math>  
<math><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mn>2</mn><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mn>10</mn></mrow></mfenced><mo>+</mo><mn>9</mn><mfenced separators="|"><mrow><mn>7</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced separators="|"><mrow><mn>35</mn><mo>-</mo><mn>4</mn></mrow></mfenced></mrow></mfenced></math>  
<math><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mn>2</mn><mfenced separators="|"><mrow><mn>12</mn></mrow></mfenced><mo>+</mo><mn>9</mn><mfenced separators="|"><mrow><mn>11</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced separators="|"><mrow><mn>31</mn></mrow></mfenced></mrow></mfenced></math>  
<math><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mn>24</mn><mo>+</mo><mn>99</mn><mo>-</mo><mn>31</mn></mrow></mfenced></math>  
<math><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mn>92</mn></mrow></mfenced><mo>=</mo><mn>92</mn></math> cubic units

</details>

---

### Q28. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The vector equation of the plane <math><mi>r</mi><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>λ</mi><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>μ</mi><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced></math> in scalar product from is <math><mi>r</mi><mo>.</mo><mfenced separators="|"><mrow><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mi>α</mi><mi></mi></math> , then <math><mi>α</mi><mo>=</mo></math> …

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** 1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

Given, equation of plane
<math><mi>r</mi><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>λ</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>μ</mi><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mtext>    </mtext><mo>…</mo></math> (i)
<math><mi mathvariant="normal">H</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi></math> , plane (i) passing through a (let) <math><mo>=</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> and parallel to vector b (let) <math><mo>=</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></math> and <math><mi>c</mi><mo>=</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
We know that equation of plane passing through a point a and parallel to non-parallel vectors b and c is <math><mi>r</mi><mo>.</mo><mfenced separators="|"><mrow><mi>b</mi><mo>×</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mi>a</mi><mo>.</mo><mfenced separators="|"><mrow><mi>b</mi><mo>×</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mi>a</mi><mtext> </mtext><mi>b</mi><mtext> </mtext><mi>c</mi></mrow></mfenced></math>
Now, <math><mfenced close="]" open="[" separators="|"><mrow><mi>a</mi><mtext> </mtext><mi>b</mi><mtext> </mtext><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>-</mo><mn>0</mn><mo>+</mo><mn>1</mn><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math>
and <math><mi>b</mi><mo>×</mo><mi>c</mi><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
<math><mo>∴</mo><mi>r</mi><mfenced separators="|"><mrow><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>2</mn></math>
<math><mi mathvariant="normal">T</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi></math> , <math><mi>α</mi><mo>=</mo><mn>2</mn></math>

</details>

---

### Q29. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

If <math> <mrow> <mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> <mo>,</mo><mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <mo>,</mo><mover accent="true"> <mi>c</mi> <mo stretchy="true">→</mo> </mover> </mrow> </math> are mutually perpendicular vectors having magnitude <math> <mrow> <mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn> </mrow> </math> respectively, then <math> <mrow><mo>[</mo> <mrow> <mtable> <mtr> <mtd> <mrow> <mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> <mo>+</mo><mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <mo>+</mo><mover accent="true"> <mi>c</mi> <mo stretchy="true">→</mo> </mover> </mrow> </mtd> <mtd> <mrow> <mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <mo>−</mo><mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> </mrow> </mtd> <mtd> <mrow> <mover accent="true"> <mi>c</mi> <mo stretchy="true">→</mo> </mover> </mrow> </mtd> </mtr> </mtable> </mrow> <mo>]</mo></mrow><mo>=</mo> </math>

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** <math><mn>6</mn></math>
- **(C)** <math><mn>12</mn></math>
- **(D)** <math><mn>18</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>12</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo></mrow><mo>=</mo><mn>1</mn><mo>,</mo><mtext>&#8201;</mtext><mrow><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo></mrow><mo>=</mo><mn>2</mn><mo>,</mo><mtext>&#8201;</mtext><mrow><mo>|</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>|</mo></mrow><mo>=</mo><mn>3</mn></math> and 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></math> (as the three vectors are mutually perpendicular)</p><p>So, 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>[</mo><mrow><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>)</mo></mrow><mo>&#215;</mo><mrow><mo>(</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#8722;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>)</mo></mrow><mo>]</mo></mrow><mo>.</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>=</mo><mrow><mo>[</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#8722;</mo><mn>0</mn><mo>+</mo><mn>0</mn><mo>&#8722;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mrow></mrow><mo>&#8594;</mo></mover></mrow><mo>]</mo></mrow><mo>.</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mrow><mo>[</mo><mn>2</mn><mrow><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo></mrow><mo>.</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mrow><mo>(</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo></mrow><mo>.</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#8722;</mo><mrow><mo>(</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>)</mo></mrow><mo>.</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>]</mo></mrow></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mrow><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo></mrow><mo>.</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>0</mn><mo>&#8722;</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mrow><mo>[</mo><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#160;</mo></mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>]</mo></mrow></math>
<math> <mrow> <mo>=</mo> <mn>2</mn> <mo>&#183;</mo> <mn>1</mn> <mo>&#183;</mo> <mn>2</mn> <mo>&#183;</mo> <mn>3</mn> </mrow> </math>
<math> <mrow> <mo>=</mo> <mn>1</mn> <mn>2</mn> </mrow> </math></p>

</details>

---

### Q30. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

If <math> <mrow> <mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> <mo>=</mo><mover accent="true"> <mi>i</mi> <mo stretchy="true">^</mo> </mover> <mo>+</mo><mover accent="true"> <mi>j</mi> <mo stretchy="true">^</mo> </mover> <mo>+</mo><mover accent="true"> <mi>k</mi> <mo stretchy="true">^</mo> </mover> <mo>,</mo><mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <mo>=</mo><mn>2</mn><mover accent="true"> <mi>i</mi> <mo stretchy="true">^</mo> </mover> <mo>+</mo><mi>λ</mi><mo>+</mo><mover accent="true"> <mi>k</mi> <mo stretchy="true">^</mo> </mover> <mo>,</mo><mover accent="true"> <mi>c</mi> <mo stretchy="true">→</mo> </mover> <mo>=</mo><mover accent="true"> <mi>i</mi> <mo stretchy="true">^</mo> </mover> <mo>−</mo><mover accent="true"> <mi>j</mi> <mo stretchy="true">^</mo> </mover> <mo>+</mo><mn>4</mn><mover accent="true"> <mi>k</mi> <mo stretchy="true">^</mo> </mover> </mrow> </math> and <math> <mrow> <mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> <mo>.</mo><mrow><mo>(</mo> <mrow> <mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <mo>×</mo><mover accent="true"> <mi>c</mi> <mo stretchy="true">→</mo> </mover> </mrow> <mo>)</mo></mrow><mo>=</mo><mn>10</mn><mo>,</mo> </mrow> </math> then <math><mi>λ</mi></math> is equal to

**Options:**

- **(A)** <math> <mn>6</mn></math>
- **(B)** <math> <mn>7</mn></math>
- **(C)** <math> <mn>9</mn></math>
- **(D)** <math> <mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mn>6</mn></math>**

**Detailed Solution:**

<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>λ</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>10</mn></math>
<math><mn>1</mn><mfenced separators="|"><mrow><mn>4</mn><mi>λ</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced separators="|"><mrow><mn>8</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mi>λ</mi></mrow></mfenced><mo>=</mo><mn>10</mn></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mn>4</mn><mi>λ</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>7</mn><mo>-</mo><mn>2</mn><mo>-</mo><mi>λ</mi><mo>=</mo><mn>10</mn></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mn>3</mn><mi>λ</mi><mo>=</mo><mn>18</mn></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi>λ</mi><mo>=</mo><mn>6</mn></math>

</details>

---

### Q31. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

$\overrightarrow{\mathbf{a}} \times[\overrightarrow{\mathbf{a}} \times(\overrightarrow{\mathbf{a}} \times \overrightarrow{\mathbf{b}})]$ is equal to

**Options:**

- **(A)** $(\overrightarrow{\mathbf{a}} \times \overrightarrow{\mathbf{a}}) \cdot(\overrightarrow{\mathbf{b}} \times \overrightarrow{\mathbf{a}})$
- **(B)** $\overrightarrow{\mathbf{a}} \cdot(\overrightarrow{\mathbf{b}} \times \overrightarrow{\mathbf{a}})-\overrightarrow{\mathbf{b}}(\overrightarrow{\mathbf{a}} \times \overrightarrow{\mathbf{b}})$
- **(C)** $[\overrightarrow{\mathbf{a}} \cdot(\overrightarrow{\mathbf{a}} \times \overrightarrow{\mathbf{b}})] \overrightarrow{\mathbf{a}}$
- **(D)** $(\overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{a}})(\overrightarrow{\mathbf{b}} \times \overrightarrow{\mathbf{a}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{a}})(\overrightarrow{\mathbf{b}} \times \overrightarrow{\mathbf{a}})$**

**Detailed Solution:**

$\begin{aligned} \overrightarrow{\mathbf{a}} \times[\overrightarrow{\mathbf{a}}&\times(\overrightarrow{\mathbf{a}} \times \overrightarrow{\mathbf{b}})] \\ &=\overrightarrow{\mathbf{a}} \times\{(\overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{b}}) \overrightarrow{\mathbf{a}}-(\overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{a}}) \overrightarrow{\mathbf{b}}\} \\ &=(\overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{b}})(\overrightarrow{\mathbf{a}} \times \overrightarrow{\mathbf{a}})-(\overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{a}})(\overrightarrow{\mathbf{a}} \times \overrightarrow{\mathbf{b}}) \\ &=(\overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{b}}) 0+(\overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{a}})(\overrightarrow{\mathbf{b}} \times \overrightarrow{\mathbf{a}}) \\ &=(\overrightarrow{\mathbf{a}} \cdot \overrightarrow{\mathbf{a}})(\overrightarrow{\mathbf{b}} \times \overrightarrow{\mathbf{a}}) \end{aligned}$

</details>

---

