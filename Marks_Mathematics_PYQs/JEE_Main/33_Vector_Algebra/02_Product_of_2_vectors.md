# JEE Main Mathematics - Vector Algebra

## Topic 2: Product of 2 vectors

**Total Questions:** 186

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a} = 4\hat{i} - \hat{j} + 3\hat{k}$, $\vec{b} = 10\hat{i} + 2\hat{j} - \hat{k}$ and a vector $\vec{c}$ be such that $2(\vec{a}\times\vec{b}) + 3(\vec{b}\times\vec{c}) = \vec{0}$. If $\vec{a}\cdot\vec{c} = 15$, then $\vec{c}\cdot(\hat{i}+\hat{j}-3\hat{k})$ is equal to:

**Options:**

- **(A)** $-6$
- **(B)** $-5$
- **(C)** $-4$
- **(D)** $-3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-5$**

**Detailed Solution:**

Given $2(\vec{a}\times\vec{b}) + 3(\vec{b}\times\vec{c}) = \vec{0}$

$\Rightarrow 2(\vec{a}\times\vec{b}) - 3(\vec{c}\times\vec{b}) = \vec{0}$

$\Rightarrow (2\vec{a} - 3\vec{c}) \times \vec{b} = \vec{0}$

Since the cross product is zero, the vectors are collinear:

$2\vec{a} - 3\vec{c} = \lambda \vec{b}$

$\Rightarrow 3\vec{c} = 2\vec{a} - \lambda \vec{b}$

Taking the dot product with $\vec{a}$ on both sides:

$3(\vec{a}\cdot\vec{c}) = 2|\vec{a}|^2 - \lambda(\vec{a}\cdot\vec{b})$

We have $\vec{a} = 4\hat{i} - \hat{j} + 3\hat{k}$ and $\vec{b} = 10\hat{i} + 2\hat{j} - \hat{k}$.

$|\vec{a}|^2 = 4^2 + (-1)^2 + 3^2 = 26$

$\vec{a}\cdot\vec{b} = 4(10) + (-1)(2) + 3(-1) = 40 - 2 - 3 = 35$

Given $\vec{a}\cdot\vec{c} = 15$, substituting these values:

$3(15) = 2(26) - 35\lambda$

$45 = 52 - 35\lambda$

$35\lambda = 7 \Rightarrow \lambda = \dfrac{1}{5}$

Substituting $\lambda$ back into the equation for $\vec{c}$:

$3\vec{c} = 2\vec{a} - \dfrac{1}{5}\vec{b}$

We need to find $\vec{c}\cdot(\hat{i}+\hat{j}-3\hat{k})$. Let $\vec{v} = \hat{i}+\hat{j}-3\hat{k}$.

Taking the dot product with $\vec{v}$ on both sides:

$3(\vec{c}\cdot\vec{v}) = 2(\vec{a}\cdot\vec{v}) - \dfrac{1}{5}(\vec{b}\cdot\vec{v})$

Calculating $\vec{a}\cdot\vec{v}$ and $\vec{b}\cdot\vec{v}$:

$\vec{a}\cdot\vec{v} = 4(1) + (-1)(1) + 3(-3) = 4 - 1 - 9 = -6$

$\vec{b}\cdot\vec{v} = 10(1) + 2(1) + (-1)(-3) = 10 + 2 + 3 = 15$

Substituting these values:

$3(\vec{c}\cdot\vec{v}) = 2(-6) - \dfrac{1}{5}(15)$

$3(\vec{c}\cdot\vec{v}) = -12 - 3 = -15$

$\vec{c}\cdot\vec{v} = -5$

Answer: $-5$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a} = 2\hat{i} + 3\hat{j} + 3\hat{k}$ and $\vec{b} = 6\hat{i} + 3\hat{j} + 3\hat{k}$. Then the square of the area of the triangle with adjacent sides determined by the vectors $(2\vec{a} + 3\vec{b})$ and $(\vec{a} - \vec{b})$ is :

**Options:**

- **(A)** $450$
- **(B)** $900$
- **(C)** $1800$
- **(D)** $2400$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1800$**

**Detailed Solution:**

The area of a triangle with adjacent sides $\vec{u}$ and $\vec{v}$ is given by $\Delta = \dfrac{1}{2} |\vec{u} \times \vec{v}|$.

Here, $\vec{u} = 2\vec{a} + 3\vec{b}$ and $\vec{v} = \vec{a} - \vec{b}$.

$\vec{u} \times \vec{v} = (2\vec{a} + 3\vec{b}) \times (\vec{a} - \vec{b})$

$\vec{u} \times \vec{v} = 2(\vec{a} \times \vec{a}) - 2(\vec{a} \times \vec{b}) + 3(\vec{b} \times \vec{a}) - 3(\vec{b} \times \vec{b})$

Since $\vec{a} \times \vec{a} = \vec{0}$, $\vec{b} \times \vec{b} = \vec{0}$, and $\vec{b} \times \vec{a} = -\vec{a} \times \vec{b}$, we get:

$\vec{u} \times \vec{v} = -2(\vec{a} \times \vec{b}) - 3(\vec{a} \times \vec{b}) = -5(\vec{a} \times \vec{b})$

The area of the triangle is $\Delta = \dfrac{1}{2} |-5(\vec{a} \times \vec{b})| = \dfrac{5}{2} |\vec{a} \times \vec{b}|$.

Now, calculating $\vec{a} \times \vec{b}$:

$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 3 & 3 \\ 6 & 3 & 3 \end{vmatrix}$

$\vec{a} \times \vec{b} = \hat{i}(9 - 9) - \hat{j}(6 - 18) + \hat{k}(6 - 18) = 12\hat{j} - 12\hat{k}$

The square of the magnitude is:

$|\vec{a} \times \vec{b}|^2 = 12^2 + (-12)^2 = 144 + 144 = 288$

The square of the area of the triangle is:

$\Delta^2 = \left( \dfrac{5}{2} \right)^2 |\vec{a} \times \vec{b}|^2 = \dfrac{25}{4} \times 288 = 25 \times 72 = 1800$

Answer: $1800$

</details>

---

### Q3. JEE Main 2026 (06 April Shift 1)

*Type:* `numerical` | *Level:* `2`

If $\vec{a} = \hat{i} + \hat{j} + \hat{k}$, $\vec{b} = \hat{j} - \hat{k}$ and $\vec{c}$ be three vectors such that $\vec{a} \times \vec{c} = \vec{b}$ and $\vec{a} \cdot \vec{c} = 3$, then $\vec{c} \cdot (\vec{a} - 2\vec{b})$ is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

Given $\vec{a} \times \vec{c} = \vec{b}$.

Taking the dot product with $\vec{c}$ on both sides:

$(\vec{a} \times \vec{c}) \cdot \vec{c} = \vec{b} \cdot \vec{c}$

Since the scalar triple product with two identical vectors is zero, we get:

$\vec{b} \cdot \vec{c} = 0$

We need to find the value of $\vec{c} \cdot (\vec{a} - 2\vec{b})$. Expanding the dot product:

$\vec{c} \cdot (\vec{a} - 2\vec{b}) = \vec{c} \cdot \vec{a} - 2(\vec{c} \cdot \vec{b})$

It is given that $\vec{a} \cdot \vec{c} = 3$. Substituting the values:

$\vec{c} \cdot (\vec{a} - 2\vec{b}) = 3 - 2(0) = 3$

Answer: $3$

</details>

---

### Q4. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\hat{u}$ and $\hat{v}$ be unit vectors inclined at an acute angle such that $|\hat{u}\times\hat{v}|=\dfrac{\sqrt{3}}{2}$. If $\vec{A}=\lambda\hat{u}+\hat{v}+(\hat{u}\times\hat{v})$, then $\lambda$ is equal to:

**Options:**

- **(A)** $\dfrac{4}{3}(\vec{A}\cdot\hat{u})-\dfrac{2}{3}(\vec{A}\cdot\hat{v})$
- **(B)** $\dfrac{2}{3}(\vec{A}\cdot\hat{u})-\dfrac{1}{3}(\vec{A}\cdot\hat{v})$
- **(C)** $\dfrac{4}{3}(\vec{A}\cdot\hat{u})+\dfrac{2}{3}(\vec{A}\cdot\hat{v})$
- **(D)** $(\vec{A}\cdot\hat{u})-\dfrac{1}{2}(\vec{A}\cdot\hat{v})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{4}{3}(\vec{A}\cdot\hat{u})-\dfrac{2}{3}(\vec{A}\cdot\hat{v})$**

**Detailed Solution:**

Given $|\hat{u}\times\hat{v}| = \dfrac{\sqrt{3}}{2}$ and $\hat{u}, \hat{v}$ are unit vectors.

$\sin\theta = \dfrac{\sqrt{3}}{2}$

Since the angle $\theta$ is acute, $\theta = \dfrac{\pi}{3}$.

$\hat{u}\cdot\hat{v} = \cos\dfrac{\pi}{3} = \dfrac{1}{2}$

Given $\vec{A} = \lambda\hat{u} + \hat{v} + (\hat{u}\times\hat{v})$.

Taking the dot product with $\hat{u}$:

$\vec{A}\cdot\hat{u} = \lambda(\hat{u}\cdot\hat{u}) + \hat{v}\cdot\hat{u} + (\hat{u}\times\hat{v})\cdot\hat{u}$

$\vec{A}\cdot\hat{u} = \lambda(1) + \dfrac{1}{2} + 0 = \lambda + \dfrac{1}{2}$

Taking the dot product with $\hat{v}$:

$\vec{A}\cdot\hat{v} = \lambda(\hat{u}\cdot\hat{v}) + \hat{v}\cdot\hat{v} + (\hat{u}\times\hat{v})\cdot\hat{v}$

$\vec{A}\cdot\hat{v} = \lambda\left(\dfrac{1}{2}\right) + 1 + 0 = \dfrac{\lambda}{2} + 1$

From the first equation, we have $1 = 2(\vec{A}\cdot\hat{u}) - 2\lambda$.

Substituting this into the second equation:

$\vec{A}\cdot\hat{v} = \dfrac{\lambda}{2} + 2(\vec{A}\cdot\hat{u}) - 2\lambda$

$\vec{A}\cdot\hat{v} = 2(\vec{A}\cdot\hat{u}) - \dfrac{3\lambda}{2}$

$\dfrac{3\lambda}{2} = 2(\vec{A}\cdot\hat{u}) - (\vec{A}\cdot\hat{v})$

$\lambda = \dfrac{4}{3}(\vec{A}\cdot\hat{u}) - \dfrac{2}{3}(\vec{A}\cdot\hat{v})$

Answer: $\dfrac{4}{3}(\vec{A}\cdot\hat{u})-\dfrac{2}{3}(\vec{A}\cdot\hat{v})$

</details>

---

### Q5. JEE Main 2026 (04 April Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $\vec{a_k} = (\tan\theta_k)\hat{i} + \hat{j}$ and $\vec{b_k} = \hat{i} - (\cot\theta_k)\hat{j}$, where $\theta_k = \dfrac{2^{k-1}\pi}{2^n + 1}$, for some $n \in \mathbb{N}$, $n > 5$. Then the value of $\dfrac{\displaystyle\sum_{k=1}^{n}|\vec{a_k}|^2}{\displaystyle\sum_{k=1}^{n}|\vec{b_k}|^2}$ is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

Let $\vec{a}_k = \tan\theta_k\,\hat{i} + \hat{j}$ and $\vec{b}_k = \hat{i} - \cot\theta_k\,\hat{j}$, where $\theta_k = \dfrac{2^{k-1}\pi}{2^n + 1}$.

$|\vec{a}_k|^2 = \tan^2\theta_k + 1 = \sec^2\theta_k$
$|\vec{b}_k|^2 = 1 + \cot^2\theta_k = \csc^2\theta_k$

So the required ratio is:
$\dfrac{\displaystyle\sum_{k=1}^n |\vec{a}_k|^2}{\displaystyle\sum_{k=1}^n |\vec{b}_k|^2} = \dfrac{\displaystyle\sum_{k=1}^n \sec^2\theta_k}{\displaystyle\sum_{k=1}^n \csc^2\theta_k}$

Relation between successive angles:
$\theta_{k+1} = \dfrac{2^k\pi}{2^n + 1} = 2\theta_k$

Key identity:
$\sec^2\theta + \csc^2\theta = \dfrac{1}{\cos^2\theta} + \dfrac{1}{\sin^2\theta} = \dfrac{1}{\sin^2\theta\cos^2\theta} = \dfrac{4}{\sin^2 2\theta} = 4\csc^2 2\theta$

Hence:
$\sec^2\theta = 4\csc^2 2\theta - \csc^2\theta$

Evaluating the numerator using this identity and $2\theta_k = \theta_{k+1}$:
$\displaystyle\sum_{k=1}^n \sec^2\theta_k = \sum_{k=1}^n \left(4\csc^2\theta_{k+1} - \csc^2\theta_k\right) = 4\sum_{k=1}^n \csc^2\theta_{k+1} - \sum_{k=1}^n \csc^2\theta_k$

Let $S_b = \displaystyle\sum_{k=1}^n \csc^2\theta_k$. Then:
$\displaystyle\sum_{k=1}^n \csc^2\theta_{k+1} = S_b - \csc^2\theta_1 + \csc^2\theta_{n+1}$

So:
$\displaystyle\sum_{k=1}^n \sec^2\theta_k = 4\left(S_b - \csc^2\theta_1 + \csc^2\theta_{n+1}\right) - S_b = 3S_b - 4\csc^2\theta_1 + 4\csc^2\theta_{n+1}$

Boundary terms:
$\theta_1 = \dfrac{\pi}{2^n + 1}$, $\theta_{n+1} = \dfrac{2^n\pi}{2^n + 1}$

$\theta_1 + \theta_{n+1} = \dfrac{\pi + 2^n\pi}{2^n + 1} = \dfrac{(2^n + 1)\pi}{2^n + 1} = \pi$

So $\theta_{n+1} = \pi - \theta_1$, and since $\csc(\pi - x) = \csc x$:
$\csc^2\theta_{n+1} = \csc^2\theta_1$

Therefore, $-4\csc^2\theta_1 + 4\csc^2\theta_{n+1} = 0$, and:
$\displaystyle\sum_{k=1}^n \sec^2\theta_k = 3S_b = 3\sum_{k=1}^n \csc^2\theta_k$

Hence, the required ratio is:
$\dfrac{3S_b}{S_b} = 3$

Therefore, the answer is $3$.

</details>

---

### Q6. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two adjacent sides of a parallelogram PQRS are given by $\vec{PQ} = \hat{j} + \hat{k}$ and $\vec{PS} = \hat{i} - \hat{j}$. If the side PS is rotated about the point P by an acute angle $\alpha$ in the plane of the parallelogram so that it becomes perpendicular to the side PQ, then $\sin^2\left(\dfrac{5\alpha}{2}\right) - \sin^2\left(\dfrac{\alpha}{2}\right)$ is equal to:

**Options:**

- **(A)** $\dfrac{1}{2}$
- **(B)** $\dfrac{\sqrt{3}}{2}$
- **(C)** $\dfrac{\sqrt{3}}{4}$
- **(D)** $\dfrac{2\sqrt{3}}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\sqrt{3}}{2}$**

**Detailed Solution:**

Let $\theta$ be the angle between the vectors $\vec{PQ}$ and $\vec{PS}$.

$\cos \theta = \dfrac{\vec{PQ} \cdot \vec{PS}}{|\vec{PQ}| |\vec{PS}|}$

$\cos \theta = \dfrac{(\hat{j} + \hat{k}) \cdot (\hat{i} - \hat{j})}{\sqrt{1^2 + 1^2} \sqrt{1^2 + (-1)^2}}$

$\cos \theta = \dfrac{-1}{\sqrt{2} \times \sqrt{2}} = -\dfrac{1}{2}$

$\theta = 120^{\circ}$

The side PS is rotated by an acute angle $\alpha$ in the plane of the parallelogram to become perpendicular to PQ. The new angle between the sides is $90^{\circ}$.

$\alpha = 120^{\circ} - 90^{\circ} = 30^{\circ}$

The given expression is $\sin^2\left(\dfrac{5\alpha}{2}\right) - \sin^2\left(\dfrac{\alpha}{2}\right)$.

Using the trigonometric identity $\sin^2 A - \sin^2 B = \sin(A+B) \sin(A-B)$:

$\sin^2\left(\dfrac{5\alpha}{2}\right) - \sin^2\left(\dfrac{\alpha}{2}\right) = \sin\left(\dfrac{5\alpha}{2} + \dfrac{\alpha}{2}\right) \sin\left(\dfrac{5\alpha}{2} - \dfrac{\alpha}{2}\right)$

$= \sin(3\alpha) \sin(2\alpha)$

Substituting $\alpha = 30^{\circ}$:

$= \sin(90^{\circ}) \sin(60^{\circ})$

$= 1 \times \dfrac{\sqrt{3}}{2} = \dfrac{\sqrt{3}}{2}$

Answer: $\dfrac{\sqrt{3}}{2}$

</details>

---

### Q7. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $P$ be a point in the plane of the vectors $\overrightarrow{A B}=3 \hat{i}+\hat{j}-\hat{k}$ and $\overrightarrow{A C}=\hat{i}-\hat{j}+3 \hat{k}$ such that $P$ is equidistant from the lines AB and AC. If $|\overrightarrow{\mathrm{AP}}|=\frac{\sqrt{5}}{2}$, then the area of the triangle ABP is:

**Options:**

- **(A)** 2
- **(B)** $\frac{\sqrt{30}}{4}$
- **(C)** $\frac{3}{2}$
- **(D)** $\frac{\sqrt{26}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\sqrt{30}}{4}$**

**Detailed Solution:**

Since P is equidistant from lines AB and AC through point A, it lies along the angle bisector direction. The unit vectors are $\hat{u}_{AB} = \frac{3\vec{i} + \vec{j} - \vec{k}}{\sqrt{11}}$ and $\hat{u}_{AC} = \frac{\vec{i} - \vec{j} + 3\vec{k}}{\sqrt{11}}$. 
The bisector direction is proportional to $2\vec{i} + \vec{k}$, so $\vec{AP} = \lambda(2\vec{i} + \vec{k})$. 
From $|\vec{AP}| = \frac{\sqrt{5}}{2}$: $|\lambda|\sqrt{5} = \frac{\sqrt{5}}{2}$, giving $\lambda = \frac{1}{2}$. 
Thus $\vec{AP} = \vec{i} + \frac{1}{2}\vec{k}$. 
Area of triangle ABP = $\frac{1}{2}|\vec{AB} \times \vec{AP}|$. 
Computing: $\vec{AB} \times \vec{AP} = \frac{1}{2}\vec{i} - \frac{5}{2}\vec{j} - \vec{k}$. 
$|\vec{AB} \times \vec{AP}| = \sqrt{\frac{1}{4} + \frac{25}{4} + 1} = \sqrt{\frac{30}{4}} = \frac{\sqrt{30}}{2}$. 
Area = $\frac{\sqrt{30}}{4}$.

</details>

---

### Q8. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For three unit vectors $\vec{a}, \vec{b}, \vec{c}$ satisfying $|\vec{a}-\vec{b}|^{2}+|\vec{b}-\vec{c}|^{2}+|\vec{c}-\vec{a}|^{2}=9$ and $|2 \vec{a}+k \vec{b}+k \vec{c}|=3$, the positive value of k is

**Options:**

- **(A)** 4
- **(B)** 3
- **(C)** 5
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5**

**Detailed Solution:**

Expanding $|\vec{a} - \vec{b}|^2 + |\vec{b} - \vec{c}|^2 + |\vec{c} - \vec{a}|^2 = 9$ with unit vectors gives $6 - 2(\vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{c} + \vec{c} \cdot \vec{a}) = 9$.
So $\vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{c} + \vec{c} \cdot \vec{a} = -3/2$.
For the symmetric case where vectors are equally spaced (e.g., on a circle at 120° intervals), we have $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{c} = \vec{c} \cdot \vec{a} = -1/2$.
Expanding $|2\vec{a} + k\vec{b} + k\vec{c}|^2 = 9$ gives $4 + 2k^2 + 4k(\vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c}) + 2k^2\vec{b} \cdot \vec{c} = 9$.
Substituting the symmetric values: $4 + 2k^2(1/2) + 4k(-1) + 2k^2(-1/2) = 9$, which simplifies to $k^2 - 4k - 5 = 0$.
Factoring: $(k-5)(k+1) = 0$, giving $k = 5$ as the positive solution.

</details>

---

### Q9. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\vec{a}=2 \hat{\mathrm{i}}-5 \hat{\mathrm{j}}+5 \hat{\mathrm{k}}$ and $\vec{b}=\hat{\mathrm{i}}-\hat{\mathrm{j}}+3 \hat{\mathrm{k}}$. If $\vec{c}$ is a vector such that $2(\vec{a} \times \vec{c})+3(\vec{b} \times \vec{c})=\overrightarrow{0}$ and $(\vec{a}-\vec{b}) \cdot \vec{c}=-97$, then $|\vec{c} \times \hat{\mathrm{k}}|^{2}$ is equal to

**Options:**

- **(A)** 233
- **(B)** 218
- **(C)** 193
- **(D)** 205

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 218**

**Detailed Solution:**

$2(\vec{a} \times \vec{c}) + 3(\vec{b} \times \vec{c}) = \vec{0} \Rightarrow (2\vec{a} + 3\vec{b}) \times \vec{c} = \vec{0}$.
So $\vec{c} \parallel (2\vec{a} + 3\vec{b}) = (7, -13, 19)$. Let $\vec{c} = t(7, -13, 19)$.
$\vec{a} - \vec{b} = (1, -4, 2)$.
$(\vec{a} - \vec{b}) \cdot \vec{c} = t(7 + 52 + 38) = 97t = -97 \Rightarrow t = -1$.
$\vec{c} = (-7, 13, -19)$.
$\vec{c} \times \hat{k} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ -7 & 13 & -19 \\ 0 & 0 & 1 \end{vmatrix} = (13, 7, 0)$.
$|\vec{c} \times \hat{k}|^2 = 169 + 49 = 218$.

</details>

---

### Q10. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-2 \hat{\mathrm{k}}, \vec{b}=\hat{\mathrm{i}}+\hat{\mathrm{j}}$ and $\vec{c}=\vec{a} \times \vec{b}$. Let $\vec{d}$ be a vector such that $|\vec{d}-\vec{a}|=\sqrt{11},|\vec{c} \times \vec{d}|=3$ and the angle between $\vec{c}$ and $\vec{d}$ is $\frac{\pi}{4}$. Then $\vec{a} \cdot \vec{d}$ is equal to

**Options:**

- **(A)** 3
- **(B)** 11
- **(C)** 0
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

$\vec{c} = \vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & -2 \\ 1 & 1 & 0 \end{vmatrix} = 2\hat{i} - 2\hat{j} + \hat{k}$
$|\vec{c}| = \sqrt{4+4+1} = 3$, $|\vec{a}| = \sqrt{4+1+4} = 3$
From $|\vec{c} \times \vec{d}| = 3$ and $\cos(\angle(\vec{c}, \vec{d})) = \frac{1}{\sqrt{2}}$:
$|\vec{c}||\vec{d}|\sin\frac{\pi}{4} = 3$ → $3|\vec{d}| \cdot \frac{1}{\sqrt{2}} = 3$ → $|\vec{d}| = \sqrt{2}$
From $|\vec{d} - \vec{a}|^2 = 11$:
$|\vec{d}|^2 - 2\vec{a} \cdot \vec{d} + |\vec{a}|^2 = 11$
$2 - 2\vec{a} \cdot \vec{d} + 9 = 11$
$\vec{a} \cdot \vec{d} = 0$

</details>

---

### Q11. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}, \vec{b}, \vec{c}$ be three vectors such that $\vec{a} \times \vec{b}=2(\vec{a} \times \vec{c})$. If $|\vec{a}|=1,|\vec{b}|=4,|\vec{c}|=2$, and the angle between $\vec{b}$ and $\vec{c}$ is $60^{\circ}$, then $|\vec{a} \cdot \vec{c}|$ is equal to

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 0
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$\vec{a} \times \vec{b} = 2(\vec{a} \times \vec{c}) \Rightarrow \vec{a} \times (\vec{b} - 2\vec{c}) = \vec{0}$, so $\vec{b} - 2\vec{c} = k\vec{a}$.
$\vec{b} \cdot \vec{c} = 4 \cdot 2 \cdot \cos 60° = 4$.
Dot with $\vec{c}$: $4 = 2(4) + k(\vec{a} \cdot \vec{c}) \Rightarrow k(\vec{a} \cdot \vec{c}) = -4$.
Dot with $\vec{a}$: $\vec{a} \cdot \vec{b} = 2(\vec{a} \cdot \vec{c}) + k$.
Dot with $\vec{b}$: $16 = 8 + k\vec{a} \cdot \vec{b} = 8 + k\left(-\frac{8}{k} + k\right) = k^2 \Rightarrow k = \pm 4$.
$\vec{a} \cdot \vec{c} = -\frac{4}{k} = \mp 1 \Rightarrow |\vec{a} \cdot \vec{c}| = 1$.

</details>

---

### Q12. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=\hat{\mathrm{i}}-2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}, \vec{b}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-\hat{\mathrm{k}}, \vec{c}=\lambda \hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}$ and $\vec{v}=\vec{a} \times \vec{b}$. If $\vec{v} \cdot \vec{c}=11$ and the length of the projection of $\vec{b}$ on $\vec{c}$ is $p$, then $9 p^{2}$ is equal to

**Options:**

- **(A)** 12
- **(B)** 6
- **(C)** 4
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 12**

**Detailed Solution:**

$\vec{v} = \vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & -2 & 3 \\ 2 & 1 & -1 \end{vmatrix} = -\hat{i} + 7\hat{j} + 5\hat{k}$.
$\vec{v} \cdot \vec{c} = -\lambda + 7 + 5 = 11 \Rightarrow \lambda = 1$.
$\vec{c} = \hat{i} + \hat{j} + \hat{k}$, $|\vec{c}| = \sqrt{3}$.
$\vec{b} \cdot \vec{c} = 2 + 1 - 1 = 2$.
Projection $p = \frac{|\vec{b} \cdot \vec{c}|}{|\vec{c}|} = \frac{2}{\sqrt{3}}$.
$9p^2 = 9 \times \frac{4}{3} = 12$.

</details>

---

### Q13. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overrightarrow{\mathrm{a}}=-\hat{i}+\hat{j}+2 \hat{k}, \overrightarrow{\mathrm{~b}}=\hat{i}-\hat{j}-3 \hat{k}, \overrightarrow{\mathrm{c}}=\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}$ and $\overrightarrow{\mathrm{d}}=\overrightarrow{\mathrm{c}} \times \overrightarrow{\mathrm{a}}$. Then $(\vec{a}-\vec{b}) \cdot \vec{d}$ is equal to :

**Options:**

- **(A)** -4
- **(B)** 4
- **(C)** 2
- **(D)** -2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -2**

**Detailed Solution:**

$\vec{c} = \vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ -1 & 1 & 2 \\ 1 & -1 & -3 \end{vmatrix} = (-1, -1, 0)$.
$\vec{d} = \vec{c} \times \vec{a} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ -1 & -1 & 0 \\ -1 & 1 & 2 \end{vmatrix} = (-2, 2, -2)$.
$\vec{a} - \vec{b} = (-2, 2, 5)$.
$(\vec{a}-\vec{b}) \cdot \vec{d} = (-2)(-2) + (2)(2) + (5)(-2) = 4 + 4 - 10 = -2$.

</details>

---

### Q14. JEE Main 2026 (22 January Shift 2)

*Type:* `numerical` | *Level:* `3`

Let a vector $\overrightarrow{\mathrm{a}}=\sqrt{2} \hat{i}-\hat{j}+\lambda \hat{k}, \lambda>0$, make an obtuse angle with the vector $\overrightarrow{\mathrm{b}}=-\lambda^{2} \hat{i}+4 \sqrt{2} \hat{j}+4 \sqrt{2} \hat{k}$ and an angle $\theta, \frac{\pi}{6}<\theta<\frac{\pi}{2}$, with the positive $z$-axis. If the set of all possible values of $\lambda$ is $(\alpha, \beta)-\{\gamma\}$, then $\alpha+\beta+\gamma$ is equal to $\_\_\_\_$。

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$\frac{\overrightarrow{\mathrm{a}} . \hat{\mathrm{k}}}{|\overrightarrow{\mathrm{a}}|}=\cos \theta \Rightarrow \frac{\lambda}{\sqrt{3+\lambda^2}}=\cos \theta$
$\Rightarrow 0<\frac{\lambda}{\sqrt{3+\lambda^2}}<\frac{\sqrt{3}}{2}$
$\Rightarrow \lambda>0 \& 4 \lambda^2<9+3 \lambda^2 \Rightarrow \lambda^2<9$
$\Rightarrow \lambda \in(0,3) \quad \quad \ldots .(1)$
$\Rightarrow \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{~b}}<0 \Rightarrow-\sqrt{2} \lambda^2-4 \sqrt{2}+4 \sqrt{2} \lambda<0$
$\Rightarrow \lambda^2-4 \lambda+4>0 \Rightarrow(\lambda-2)^2>0$
$\Rightarrow \lambda \neq 2$
$\text { from }(1) \&(2)$
$\lambda \in(0,3)-\{2\}$
$\therefore \alpha=0, \beta=3, \gamma=2$
$\Rightarrow \alpha+\beta+\gamma=5$

</details>

---

### Q15. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=2 \hat{i}-\hat{j}+\hat{k}$ and $\vec{b}=\lambda \hat{j}+2 \hat{k}, \lambda \in \boldsymbol{Z}$ be two vectors. Let $\vec{c}=\vec{a} \times \vec{b}$ and $\vec{d}$ be a vector of magnitude 2 in $y z$-plane. If $|\overrightarrow{\mathrm{c}}|=\sqrt{53}$, then the maximum possible value of $(\overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{d}})^{2}$ is equal to :

**Options:**

- **(A)** 26
- **(B)** 52
- **(C)** 208
- **(D)** 104

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 208**

**Detailed Solution:**

$\vec{a} = 2\hat{i} - \hat{j} + \hat{k}$
$\vec{b} = \lambda\hat{j} + 2\hat{k}$ ; $\lambda \in Z$
$\vec{c} = \vec{a} \times \vec{b} = (-2 - \lambda)\hat{i} - 4\hat{j} + 2\lambda\hat{k}$
$|\vec{c}| = \sqrt{53}$
$\Rightarrow 5\lambda^2 + 4\lambda - 33 = 0$
$\lambda = 2.2$ or $-3$
$\Rightarrow \boxed{\lambda = -3}$
$\vec{c} = \hat{i} - 4\hat{j} - 6\hat{k}$
let $\vec{d} = y\hat{j} + z\hat{k}$
$|\vec{d}| = 2$
$\Rightarrow y^2 + z^2 = 4$
$(\vec{c} \cdot \vec{d})^2 = (4y + 6z)^2 \leq \left(\sqrt{4^2 + 6^2} \times \sqrt{y^2 + z^2}\right)^2 \leq 208$

</details>

---

### Q16. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\overrightarrow{\mathrm{AB}}=2 \hat{i}+4 \hat{j}-5 \hat{k}$ and $\overrightarrow{\mathrm{AD}}=\hat{i}+2 \hat{j}+\lambda \hat{k}, \lambda \in \mathbb{R}$. Let the projection of the vector $\vec{v}=\hat{i}+\hat{j}+\hat{k}$ on the diagonal $\overrightarrow{\mathrm{AC}}$ of the parallelogram ABCD be of length one unit. If $\alpha, \beta$, where $\alpha>\beta$, be the roots of the equation $\lambda^{2} x^{2}-6 \lambda x+5=0$, then $2 \alpha-\beta$ is equal to

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 1
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

$\vec{AC} = \vec{AB} + \vec{AD} = 3\hat{i} + 6\hat{j} + (\lambda-5)\hat{k}$.
Projection of $\vec{v} = \hat{i}+\hat{j}+\hat{k}$ on $\vec{AC}$: $\frac{|\vec{v} \cdot \vec{AC}|}{|\vec{AC}|} = 1$.
$\vec{v} \cdot \vec{AC} = 3+6+(\lambda-5) = \lambda+4$, $|\vec{AC}| = \sqrt{45+(\lambda-5)^2}$.
$(\lambda+4)^2 = 45 + (\lambda-5)^2$ 
$\Rightarrow 8\lambda+16 = 45-10\lambda+25$ 
$\Rightarrow 18\lambda = 54 \Rightarrow \lambda = 3$.
Equation: $9x^2 - 18x + 5 = 0$ 
$\Rightarrow (3x-1)(3x-5) = 0$ 
$\Rightarrow x = \frac{1}{3}, \frac{5}{3}$.
$\alpha = \frac{5}{3},\ \beta = \frac{1}{3}$.
$2\alpha - \beta = \frac{10}{3} - \frac{1}{3} = 3$.

</details>

---

### Q17. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

For a triangle ABC, let $\overrightarrow{\mathrm{p}}=\overrightarrow{\mathrm{BC}}, \overrightarrow{\mathrm{q}}=\overrightarrow{\mathrm{CA}}$ and $\overrightarrow{\mathrm{r}}=\overrightarrow{\mathrm{BA}}$. If $|\overrightarrow{\mathrm{p}}|=2 \sqrt{3},|\overrightarrow{\mathrm{q}}|=2$ and $\cos \theta=\frac{1}{\sqrt{3}}$, where $\theta$ is the angle between $\vec{p}$ and $\vec{q}$, then $|\vec{p} \times(\vec{q}-3 \vec{r})|^{2}+3|\vec{r}|^{2}$ is equal to :

**Options:**

- **(A)** 410
- **(B)** 340
- **(C)** 200
- **(D)** 220

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 200**

**Detailed Solution:**

Given $|\vec{p}| = 2\sqrt{3}$, $|\vec{q}| = 2$, and $\cos\theta = \frac{1}{\sqrt{3}}$ where $\theta$ is the angle between $\vec{p}$ and $\vec{q}$.
Since $\vec{p} = \overrightarrow{BC}$, $\vec{q} = \overrightarrow{CA}$, and $\vec{r} = \overrightarrow{BA}$, from triangle closure $\vec{r} = \vec{p} + \vec{q}$.
$\vec{p} \cdot \vec{q} = |\vec{p}||\vec{q}|\cos\theta = 2\sqrt{3} \cdot 2 \cdot \frac{1}{\sqrt{3}} = 4$
$|\vec{r}|^2 = |\vec{p}|^2 + |\vec{q}|^2 + 2\vec{p} \cdot \vec{q} = 12 + 4 + 8 = 24$
$\vec{q} - 3\vec{r} = \vec{q} - 3(\vec{p} + \vec{q}) = -3\vec{p} - 2\vec{q}$
$\vec{p} \times (\vec{q} - 3\vec{r}) = -2(\vec{p} \times \vec{q})$
$\sin^2\theta = 1 - \frac{1}{3} = \frac{2}{3}$
$|\vec{p} \times \vec{q}|^2 = 12 \cdot 4 \cdot \frac{2}{3} = 32$
$|\vec{p} \times (\vec{q} - 3\vec{r})|^2 = 4 \cdot 32 = 128$
Result: $128 + 3(24) = 128 + 72 = 200$

</details>

---

### Q18. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overrightarrow{\mathrm{a}}=-\hat{i}+2 \hat{j}+2 \hat{k}, \overrightarrow{\mathrm{~b}}=8 \hat{i}+7 \hat{j}-3 \hat{k}$ and $\overrightarrow{\mathrm{c}}$ be vector such that $\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{c}}=\overrightarrow{\mathrm{b}}$. If $\vec{c} \cdot(\hat{i}+\hat{j}+\hat{k})=4$, then $|\vec{a}+\vec{c}|^{2}$ is equal to :

**Options:**

- **(A)** 27
- **(B)** 33
- **(C)** 35
- **(D)** 30

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 27**

**Detailed Solution:**

Let $\vec{c} = x\hat{i} + y\hat{j} + z\hat{k}$.
From $\vec{a} \times \vec{c} = \vec{b}$: $z - y = 4$, $z + 2x = 7$, $y + 2x = 3$.
From $\vec{c} \cdot (\hat{i} + \hat{j} + \hat{k}) = 4$: $x + y + z = 4$.
Solving: $y = -1$, $z = 3$, $x = 2$.
$\vec{c} = 2\hat{i} - \hat{j} + 3\hat{k}$.
$\vec{a} + \vec{c} = (-1+2)\hat{i} + (2-1)\hat{j} + (2+3)\hat{k} = \hat{i} + \hat{j} + 5\hat{k}$.
$|\vec{a} + \vec{c}|^2 = 1 + 1 + 25 = 27$.

</details>

---

### Q19. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=\hat{i}+2 \hat{j}+\hat{k}$ and $\vec{b}=2 \hat{i}+\hat{j}-\hat{k}$. Let $\hat{c}$ be a unit vector in the plane of the vectors $\vec{a}$ and $\vec{b}$ and be perpendicular to $\vec{a}$. Then such a vector $\hat{c}$ is :

**Options:**

- **(A)** $\frac{1}{\sqrt{5}}(\hat{\mathrm{j}}-2 \hat{\mathrm{k}})$
- **(B)** $\frac{1}{\sqrt{3}}(-\hat{\mathrm{i}}+\hat{\mathrm{j}}-\hat{\mathrm{k}})$
- **(C)** $\frac{1}{\sqrt{3}}(\hat{\mathrm{i}}-\hat{\mathrm{j}}+\hat{\mathrm{k}})$
- **(D)** $\frac{1}{\sqrt{2}}(-\hat{\mathrm{i}}+\hat{\mathrm{k}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{\sqrt{2}}(-\hat{\mathrm{i}}+\hat{\mathrm{k}})$**

**Detailed Solution:**

Let vector $\vec{p}$ in plane of $\vec{a} \& \vec{b}=K(\vec{a}+\lambda \vec{b})$
$\begin{aligned}
& \overrightarrow{\mathrm{p}} \perp \overrightarrow{\mathrm{a}}=\overrightarrow{\mathrm{p}} \cdot \overrightarrow{\mathrm{a}}=0 \\
& \Rightarrow \mathrm{~K}(\overrightarrow{\mathrm{a}}+\lambda \overrightarrow{\mathrm{b}}) \cdot \overrightarrow{\mathrm{a}}=0 \\
& \Rightarrow \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{a}}+\lambda \overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{a}}=0 \\
& \Rightarrow 6+\lambda(3)=0 \\
& \Rightarrow \lambda=-2 \\
& \Rightarrow \overrightarrow{\mathrm{p}}=(-3 \hat{\mathrm{i}}+3 \hat{\mathrm{k}})
\end{aligned}$
Unit vector $\rightarrow \pm \frac{(-\hat{\mathrm{i}}+\hat{\mathrm{k}})}{\sqrt{2}}$

</details>

---

### Q20. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the angle $\theta, 0 \lt \theta \lt \frac{\pi}{2}$ between two unit vectors $\hat{\mathrm{a}}$ and $\hat{\mathrm{b}}$ be $\sin ^{-1}\left(\frac{\sqrt{65}}{9}\right)$. If the vector $\overrightarrow{\mathrm{c}}=3 \hat{\mathrm{a}}+6 \hat{\mathrm{~b}}+9(\hat{\mathrm{a}} \times \hat{\mathrm{b}}),$ then the value of $9(\overrightarrow{\mathrm{c}} \cdot \hat{\mathrm{a}})-3(\overrightarrow{\mathrm{c}} \cdot \hat{\mathrm{b}})$ is

**Options:**

- **(A)** 31
- **(B)** 27
- **(C)** 29
- **(D)** 24

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 29**

**Detailed Solution:**

$\begin{aligned}
& \overrightarrow{\mathrm{c}}=3 \overrightarrow{\mathrm{a}}+6 \overrightarrow{\mathrm{~b}}+9(\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}) \\
& \sin ^{-1}\left(\frac{\sqrt{65}}{9}\right) \Rightarrow \sin \theta=\frac{\sqrt{65}}{9} \Rightarrow \cos \theta=\frac{4}{9} \\
& \overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{a}}=3|\overrightarrow{\mathrm{a}}|^2+6 \vec{a} \cdot \vec{b}=3+\frac{6 \cdot 4}{9}=\frac{51}{9} \\
& \overrightarrow{\mathrm{c}} \cdot \vec{a}=3 \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{~b}}+6|\overrightarrow{\mathrm{~b}}|^2=\frac{3 \cdot 4}{9}+6=\frac{22}{3} \\
& \therefore 9(\overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{a}})-3(\overrightarrow{\mathrm{c}} \cdot \vec{b})=51-22=29
\end{aligned}$

</details>

---

### Q21. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider two vectors $\overrightarrow{\mathrm{u}}=3 \hat{\mathrm{i}}-\hat{\mathrm{j}}$ and $\overrightarrow{\mathrm{v}}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-\lambda \hat{\mathrm{k}}, \lambda \gt 0$. The angle between them is given by $\cos ^{-1}\left(\frac{\sqrt{5}}{2 \sqrt{7}}\right)$. Let $\overrightarrow{\mathrm{v}}=\overrightarrow{\mathrm{v}}_1+\overrightarrow{\mathrm{v}}_2$, where $\overrightarrow{\mathrm{v}}_1$ is parallel to $\overrightarrow{\mathrm{u}}$ and $\overrightarrow{\mathrm{v}}_2$ is perpendicular to $\overrightarrow{\mathrm{u}}$. Then the value $\left|\overrightarrow{\mathrm{v}}_1\right|^2+\left|\overrightarrow{\mathrm{v}}_2\right|^2$ is equal to

**Options:**

- **(A)** $\frac{23}{2}$
- **(B)** 14
- **(C)** $\frac{25}{2}$
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 14**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{\mathrm{u}}=3 \hat{\mathrm{i}}-\hat{\mathrm{j}}, \overrightarrow{\mathrm{v}}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}-\lambda \hat{\mathrm{k}}, \\ & \Rightarrow \frac{\overrightarrow{\mathrm{u}} \cdot \overrightarrow{\mathrm{v}}}{|\overrightarrow{\mathrm{u}} \| \overrightarrow{\mathrm{v}}|}=\cos \theta \\ & \Rightarrow \frac{5}{\sqrt{10} \sqrt{5+\lambda^2}}=\frac{\sqrt{5}}{2 \sqrt{7}} \\ & \Rightarrow \lambda^2=9 \Rightarrow \lambda=3(\because \lambda \gt 0) \\ & \overrightarrow{\mathrm{v}}=\overrightarrow{\mathrm{v}}_1+\overrightarrow{\mathrm{v}}_2 \\ & \Rightarrow|\overrightarrow{\mathrm{v}}|^2=\overrightarrow{\mathrm{v}}_1^2+\overrightarrow{\mathrm{v}}_2^2+2 \overrightarrow{\mathrm{v}}_1 \cdot \overrightarrow{\mathrm{v}}_2 \\ & \Rightarrow 14=\overrightarrow{\mathrm{v}}_1^2+\overrightarrow{\mathrm{v}}_2^2+0 \quad\left(\because \overrightarrow{\mathrm{v}}_1 \perp \overrightarrow{\mathrm{v}}_2\right) \\ & \Rightarrow\left|\overrightarrow{\mathrm{v}}_1^2\right|+\left|\overrightarrow{\mathrm{v}}_2^2\right|=14\end{aligned}$

</details>

---

### Q22. JEE Main 2025 (3 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

Let $\vec{a}=\hat{i}+2 \hat{j}+\hat{k}, \vec{b}=3 \hat{i}-3 \hat{j}+3 \hat{k}$, $\overrightarrow{\mathrm{c}}=2 \hat{\mathrm{i}}-\hat{\mathrm{j}}+2 \hat{\mathrm{k}}$ and $\overrightarrow{\mathrm{d}}$ be a vector such that $\overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{d}}=\overrightarrow{\mathrm{c}} \times \overrightarrow{\mathrm{d}}$ and $\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{d}}=4$. Then $|(\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{d}})|^2$ is equal to ______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **128**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{d}}=\overrightarrow{\mathrm{c}} \times \overrightarrow{\mathrm{d}} \text {-and } \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{d}}=4 \\ & \Rightarrow \overrightarrow{\mathrm{~d}}=\lambda(\overrightarrow{\mathrm{b}}-\overrightarrow{\mathrm{c}})=\lambda(\hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}}) \\ & \because \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{d}}=4 \Rightarrow \lambda=-2 \\ & \text { Also. }|\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{d}}|^2+|\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{d}}|^2=|\overrightarrow{\mathrm{a}}|^2|\overrightarrow{\mathrm{~d}}|^2 \\ & \Rightarrow|\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{d}}|^2=6 \times 4 \times 6-16=128\end{aligned}$

</details>

---

### Q23. JEE Main 2025 (3 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $\vec{a}=\hat{i}+\hat{j}+\hat{k}, \vec{b}=3 \hat{i}+2 \hat{j}-\hat{k}, \vec{c}=\lambda \hat{j}+\mu \hat{k}$ and $\hat{d}$ be a unit vector such that $\overrightarrow{\mathrm{a}} \times \hat{\mathrm{d}}=\overrightarrow{\mathrm{b}} \times \hat{\mathrm{d}}$ and $\overrightarrow{\mathrm{c}} \cdot \hat{\mathrm{d}}=1$, If $\vec{c}$ is perpendicular to $\vec{a}$, then $|3 \lambda \hat{d}+\mu \overrightarrow{\mathrm{c}}|^2$ is equal to _______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{d}}-\overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{d}}=0 \\ & (\overrightarrow{\mathrm{a}}-\overrightarrow{\mathrm{b}}) \times \overrightarrow{\mathrm{d}}=0 \\ & \overrightarrow{\mathrm{~d}}=\mathrm{t}(\overrightarrow{\mathrm{a}}-\overrightarrow{\mathrm{b}}) \\ & \overrightarrow{\mathrm{d}}=\mathrm{t}(-2 \hat{\mathrm{i}}-\hat{\mathrm{j}}+2 \hat{\mathrm{k}}) \\ & |\overrightarrow{\mathrm{d}}|=1 \\ & |\mathrm{t}|=\frac{1}{3}\end{aligned}$
$\begin{aligned} & \overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{a}}=0 \\ & \lambda+\mu=0 \\ & \mu=-\lambda \\ & \overrightarrow{\mathrm{c}}=\lambda(\hat{\mathrm{j}}-\hat{\mathrm{k}}),|\overrightarrow{\mathrm{c}}|^2=2 \lambda^2 \\ & \overrightarrow{\mathrm{c}} \cdot \hat{\mathrm{d}}=1 \\ & \mathrm{t}(-2,-1,2) \cdot \lambda(0,1,-1)=1 \\ & \lambda \mathrm{t}=\frac{-1}{3} \Rightarrow \lambda^2=1\end{aligned}$
$\begin{aligned} & |3 \lambda \hat{\mathrm{~d}}+\mu \mathrm{c}|^2=9 \lambda^2|\hat{\mathrm{~d}}|^2+\mu^2|\overrightarrow{\mathrm{c}}|^2+6 \lambda \mu(\hat{\mathrm{~d}} \cdot \overrightarrow{\mathrm{c}}) \\ & =3 \lambda^2+2 \lambda^4 \\ & =5\end{aligned}$

</details>

---

### Q24. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=2 \hat{i}-3 \hat{j}+k, \vec{b}=3 \hat{i}+2 \hat{j}+5 k$ and a vector $\vec{c}$ be such that $(\overrightarrow{\mathrm{a}}-\overrightarrow{\mathrm{c}}) \times \overrightarrow{\mathrm{b}}=-18 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+12 \mathrm{k}$ and $\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{c}}=3$. If $\overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{c}}=\overrightarrow{\mathrm{d}}$, then $|\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{d}}|$ is equal to :

**Options:**

- **(A)** $18$
- **(B)** $12$
- **(C)** $9$
- **(D)** $15$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $15$**

**Detailed Solution:**

$\overrightarrow{\mathrm{a}}=2 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+\hat{\mathrm{k}}, \overrightarrow{\mathrm{b}}=3 \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+5 \hat{\mathrm{k}}$
$\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}=\left|\begin{array}{ccc}\mathrm{i} & \mathrm{j} & \mathrm{k} \\ 2 & -3 & 1 \\ 3 & 2 & 5\end{array}\right|$
$\begin{aligned} & =-17 \hat{i}-7 \hat{j}+13 \hat{k} \\ & (\overrightarrow{\mathrm{a}}-\overrightarrow{\mathrm{c}}) \times \overrightarrow{\mathrm{b}}=-18 \hat{\mathrm{i}}-3 \mathrm{j}+12 \hat{k} \\ & \Rightarrow(\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}})-(\overrightarrow{\mathrm{c}} \times \overrightarrow{\mathrm{b}})=-18 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+12 \hat{\mathrm{k}} \\ & \Rightarrow \overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{c}}=(-18 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+12 \hat{k})-(\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}) \\ & =(-18 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+12 \hat{\mathrm{k}})-(-17 \mathrm{i}-7 \hat{\mathrm{j}}+13 \hat{\mathrm{k}}) \\ & \overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{c}}=-\hat{\mathrm{i}}+4 \hat{\mathrm{j}}-\hat{\mathrm{k}} \\ & \therefore \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{d}}=\overrightarrow{\mathrm{a}} \cdot(\overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{c}})=(2 \mathrm{i}-3 \mathrm{j}+\mathrm{k}) \cdot(-\hat{\mathrm{i}}+4 \hat{\mathrm{j}}-\hat{\mathrm{k}}) \\ & =-2-12-1=-15 \\ & \therefore|\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{d}}|=15\end{aligned}$

</details>

---

### Q25. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{a}$ is nonzero vector such that its projections on the vectors $2 \hat{i}-\hat{j}+2 \hat{k}, \hat{i}+2 \hat{j}-2 \hat{k}$ and $\hat{k}$ are equal, then a unit vector along $\vec{a}$ is:

**Options:**

- **(A)** $\frac{1}{\sqrt{155}}(-7 \hat{\mathrm{i}}+9 \hat{\mathrm{j}}+5 \hat{\mathrm{k}})$
- **(B)** $\frac{1}{\sqrt{155}}(-7 \hat{\mathrm{i}}+9 \hat{\mathrm{j}}-5 \hat{\mathrm{k}})$
- **(C)** $\frac{1}{\sqrt{155}}(7 \hat{\mathrm{i}}+9 \hat{\mathrm{j}}+5 \hat{\mathrm{k}})$
- **(D)** $\frac{1}{\sqrt{155}}(7 \hat{\mathrm{i}}+9 \hat{\mathrm{j}}-5 \hat{\mathrm{k}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{\sqrt{155}}(7 \hat{\mathrm{i}}+9 \hat{\mathrm{j}}+5 \hat{\mathrm{k}})$**

**Detailed Solution:**

Let $\overline{\mathrm{a}}=\mathrm{a}_1 \hat{\mathrm{i}}+\mathrm{a}_2 \hat{\mathrm{j}}+\mathrm{a}_3 \hat{\mathrm{k}}$
$\mathrm{a}_1^2+\mathrm{a}_2^2+\mathrm{a}_3^2=1$
Let $\overline{\mathrm{b}}=2 \overrightarrow{\mathrm{i}}-\hat{\mathrm{j}}+2 \hat{\mathrm{k}}, \overline{\mathrm{c}}=\overrightarrow{\mathrm{i}}-2 \hat{\mathrm{j}}-2 \hat{\mathrm{k}}$
$\overline{\mathrm{d}}=\hat{\mathrm{k}}$
$\frac{\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}}{|\mathrm{b}|}=\frac{\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}}{|\mathrm{c}|}=\frac{\overline{\mathrm{a}} \cdot \overline{\mathrm{d}}}{|\mathrm{d}|}$
$\frac{2 \mathrm{a}_1-\mathrm{a}_2+2 \mathrm{a}_3}{3}=\frac{\mathrm{a}_1+2 \mathrm{a}_2-2 \mathrm{a}_3}{3}=\mathrm{a}_3$
By solving
$\mathrm{a}_1=\frac{7}{\sqrt{155}}, \mathrm{a}_2=\frac{9}{\sqrt{155}}, \mathrm{a}_3=\frac{5}{\sqrt{155}}$

</details>

---

### Q26. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $A B C D$ be a tetrahedron such that the edges $\mathrm{AB}, \mathrm{AC}$ and AD are mutually perpendicular. Let the areas of the triangles $\mathrm{ABC}, \mathrm{ACD}$ and ADB be 5,6 and 7 square units respectively. Then the area (in square units) of the $\triangle \mathrm{BCD}$ is equal to :

**Options:**

- **(A)** $\sqrt{340}$
- **(B)** 12
- **(C)** $\sqrt{110}$
- **(D)** $7 \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{110}$**

**Detailed Solution:**

$\operatorname{Ar}(\triangle B C D)$
$=\sqrt{(\operatorname{Ar}(\triangle \mathrm{ABC}))^2+(\mathrm{Ar}(\mathrm{ACD}))^2+(\operatorname{Ar}(\triangle \mathrm{ADB}))^2}$
$=\sqrt{5^2+6^2+7^2}$
$=\sqrt{110}$

</details>

---

### Q27. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\hat{a}$ be a unit vector perpendicular to the vectors $\overrightarrow{\mathrm{b}}=\hat{i}-2 \hat{j}+3 \hat{k}$ and $\overrightarrow{\mathrm{c}}=2 \hat{i}+3 \hat{j}-\hat{k}$, and makes an angle of $\cos ^{-1}\left(-\frac{1}{3}\right)$ with the vector $\hat{i}+\hat{j}+\hat{k}$. If $\hat{\mathrm{a}}$ makes an angle of $\frac{\pi}{3}$ with the vector $\hat{i}+\alpha \hat{j}+\hat{k}$, then the value of $\alpha$ is :

**Options:**

- **(A)** $\sqrt{6}$
- **(B)** $-\sqrt{6}$
- **(C)** $-\sqrt{3}$
- **(D)** $\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\sqrt{6}$**

**Detailed Solution:**

$\begin{aligned}
& \left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
1 & -2 & 3 \\
2 & 3 & -1
\end{array}\right|=\hat{i}(-7)+7 \hat{j}+7 \hat{k} \\
& \hat{a}= \pm \frac{(-7 \hat{i}+7 \hat{j}+7 \hat{k})}{\sqrt{7^2+7^2+7^2}}= \pm\left(\frac{-\hat{i}+\hat{j}+\hat{k}}{\sqrt{3}}\right)
\end{aligned}$
$\begin{aligned}
& \text { Now, } \cos \theta= \pm \frac{(-1+1+1)}{\sqrt{3} \cdot \sqrt{3}}= \pm \frac{1}{3} \\
& \Rightarrow \cos ^{-1}\left(\frac{-1}{3}\right) \Rightarrow \hat{a}=\frac{-(-\hat{i}+\hat{j}+\hat{k})}{\sqrt{3}} \\
& \hat{a}=\frac{\hat{i}-\hat{j}-\hat{k}}{\sqrt{3}}
\end{aligned}$
$\begin{aligned}
& \cos \frac{\pi}{3}=\frac{1-\alpha-1}{\sqrt{3} \cdot \sqrt{\alpha^2+2}} \\
& \frac{1}{2}=\frac{-\alpha}{\sqrt{3} \cdot \sqrt{\alpha^2+2}} \rightarrow \alpha < 0 \\
& 3\left(\alpha^2+2\right)=4 \alpha^2 \\
& 6=\alpha^2 \\
& \alpha= \pm \sqrt{6}
\end{aligned}$

Clearly, $\alpha=-\sqrt{6}$

</details>

---

### Q28. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let \(\overrightarrow{\mathrm{a}}=2 \hat{i}-\hat{j}+3 \hat{k}, \overrightarrow{\mathrm{~b}}=3 \hat{i}-5 \hat{j}+\hat{k}\) and \(\overrightarrow{\mathrm{c}}\) be a vector such that \(\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{c}}=\overrightarrow{\mathrm{c}} \times \overrightarrow{\mathrm{b}}\) and \((\vec{a}+\vec{c}) \cdot(\vec{b}+\vec{c})=168\). Then the maximum value of \(|\vec{c}|^2\) is :

**Options:**

- **(A)** 462
- **(B)** 77
- **(C)** 154
- **(D)** 308

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 308**

**Detailed Solution:**

$\begin{aligned}
& \overrightarrow{\mathrm{a}}=2 \hat{\mathrm{i}}-\hat{\mathrm{j}}+3 \hat{\mathrm{k}} \\
& \overrightarrow{\mathrm{~b}}=3 \hat{\mathrm{i}}-5 \hat{\mathrm{j}}+3 \hat{\mathrm{k}} \\
& \overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{c}}=\overrightarrow{\mathrm{c}} \times \overrightarrow{\mathrm{b}} \\
& \overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{c}}+\overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{c}}=0 \\
& (\overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{b}}) \times \overrightarrow{\mathrm{c}}=0 \\
& \Rightarrow \overrightarrow{\mathrm{c}}=\lambda(\overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{b}}) \\
& \overrightarrow{\mathrm{c}}=\lambda(5 \hat{\mathrm{i}}-6 \hat{\mathrm{j}}+4 \hat{\mathrm{k}}) \ldots . .(1) \\
& |\overrightarrow{\mathrm{c}}|^2=\lambda^2(25+36+16) \\
& |\overrightarrow{\mathrm{c}}|^2=77 \lambda^2 \\
& (\overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{c}}) \cdot(\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}})=168 \\
& \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{~b}}+\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{c}}+\overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{~b}}+|\overrightarrow{\mathrm{c}}|^2=168
\end{aligned}$

$14+\vec{c} \cdot(\vec{a}+\vec{b})+77 \lambda^2=168$
using equation (1)
$\begin{aligned}
& \lambda|5 \hat{\mathrm{i}}-6 \hat{\mathrm{j}}+4 \hat{\mathrm{k}}|^2+77 \lambda^2=154 \\
& 77 \lambda+77 \lambda^2-154=0 \\
& \lambda^2+\lambda-2=0 \\
& \lambda=-2,1
\end{aligned}$
$\therefore$ Maximum value of $|\overrightarrow{\mathrm{c}}|^2$ occurs when $\lambda=-2$
$\begin{aligned}
& |\overrightarrow{\mathrm{c}}|^2=77 \lambda^2 \\
& =77 \times 4 \\
& =308
\end{aligned}$

</details>

---

### Q29. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the components of $\overrightarrow{\mathrm{a}}=\alpha \hat{i}+\beta \hat{j}+\gamma \hat{k}$ along and perpendicular to $\overrightarrow{\mathrm{b}}=3 \hat{i}+\hat{j}-\hat{k}$ respectively, are $\frac{16}{11}(3 \hat{i}+\hat{j}-\hat{k})$ and $\frac{1}{11}(-4 \hat{i}-5 \hat{j}-17 \hat{k})$, then $\alpha^2+\beta^2+\gamma^2$ is equal to :

**Options:**

- **(A)** $26$
- **(B)** $18$
- **(C)** $23$
- **(D)** $16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $26$**

**Detailed Solution:**

let
$\vec{a}_{11}=\text { component of } \vec{a} \text { along } \vec{b}$
$\vec{a}_1=$ component of $\vec{a}$ perpendicular to $\vec{b}$
$\begin{aligned}
& \overrightarrow{\mathrm{a}}_{11}=\frac{16}{11}(3 \hat{\mathrm{i}}+\hat{\mathrm{j}}-\hat{\mathrm{k}}) \\
& \overrightarrow{\mathrm{a}}_1=\frac{1}{11}(-4 \hat{\mathrm{i}}-5 \hat{\mathrm{j}}-17 \hat{\mathrm{k}}) \\
& \because \overrightarrow{\mathrm{a}}=\overrightarrow{\mathrm{a}}_{11}+\overrightarrow{\mathrm{a}}_1
\end{aligned}$
$\begin{aligned} & \begin{array}{l}\therefore \overrightarrow{\mathrm{a}}= \\ \quad=\frac{16}{11}(3 \hat{\mathrm{i}}+\hat{\mathrm{j}}-\hat{\mathrm{k}})+\frac{1}{11}(-4 \hat{\mathrm{i}}-5 \hat{\mathrm{j}}-17 \hat{\mathrm{k}}) \\ \overrightarrow{11} \hat{\mathrm{j}}-\frac{33}{11} \hat{\mathrm{k}}\end{array} \\ & \begin{aligned} \alpha=4 \hat{\mathrm{i}}+\hat{\mathrm{j}}-3 \hat{\mathrm{k}}\end{aligned} \\ & \alpha^2+\beta^2+\gamma^2=16+1+9=26\end{aligned}$

</details>

---

### Q30. JEE Main 2025 (28 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $\vec{a}=\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}, \overrightarrow{\mathrm{b}}=2 \hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}}$ and $\overrightarrow{\mathrm{d}}=\vec{a} \times \overrightarrow{\mathrm{b}}$. If $\overrightarrow{\mathrm{c}}$ is a vector such that $\vec{a} \cdot \overrightarrow{\mathrm{c}}=|\overrightarrow{\mathrm{c}}|$, $|\overrightarrow{\mathrm{c}}-2 \vec{a}|^2=8$ and the angle between $\overrightarrow{\mathrm{d}}$ and $\overrightarrow{\mathrm{c}}$ is $\frac{\pi}{4}$, then $|10-3 \overrightarrow{\mathrm{~b}} \cdot \overrightarrow{\mathrm{c}}|+|\overrightarrow{\mathrm{d}} \times \overrightarrow{\mathrm{c}}|^2$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

$\begin{aligned}
& \vec{a}=\hat{i}+\hat{j}+\hat{k} \\
& \vec{b}=2 \hat{i}+2 \hat{j}+\hat{k} \\
& \vec{d}=\vec{a} \times \vec{b} \\
& =-\hat{i}+\hat{j} \\
& |\vec{c}-2 \vec{a}|^2=8 \\
& |\vec{c}|^2+4|\vec{a}|^2-4 \vec{a} \cdot \vec{c}=8 \\
& |\vec{c}|^2+12-4|\vec{c}|=8 \\
& |\vec{c}|^2-4|\vec{c}|+4=0 \\
& |\vec{c}|^2=2 \\
& \vec{d}=\vec{a} \times \vec{b} \\
& \vec{d} \times \vec{c}=(\vec{a} \times \vec{b}) \times \vec{c} \\
& \left(|\vec{d}| \times|\vec{c}| \sin \frac{\pi}{4}\right)^2=((\vec{a} \cdot \vec{c}) \vec{b}-(\vec{b} \cdot \vec{c}) \vec{a})^2 \\
& 4=4|\vec{b}|^2+(\vec{b} \cdot \vec{c}) 2\left(|\vec{a}|^2\right)-2(\vec{b} \cdot \vec{c})(\vec{a} \cdot \vec{b})
\end{aligned}$
Let $\vec{b} \cdot \vec{c}=x$
$\begin{aligned}
& 4=36+3 x^2-20 x \\
& 3 x^2-20 x+32=0 \\
& x=\frac{8}{3}, 4 \\
& \Rightarrow \vec{b} \cdot \vec{c}=\frac{8}{3}, 4 \\
& \Rightarrow \vec{b} \cdot \vec{c}=\frac{8}{3}
\end{aligned}$
Now, $|10-3 \vec{b} \cdot \vec{c}|+|\vec{d} \times \vec{c}|^2$
$=|10-8|+(2)^2=6$

</details>

---

### Q31. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overrightarrow{\mathrm{a}}=3 \hat{i}-\hat{j}+2 \hat{k}, \overrightarrow{\mathrm{~b}}=\overrightarrow{\mathrm{a}} \times(\hat{i}-2 \hat{k})$ and $\overrightarrow{\mathrm{c}}=\overrightarrow{\mathrm{b}} \times \hat{k}$. Then the projection of $\overrightarrow{\mathrm{c}}-2 \hat{j}$ on $\vec{a}$ is :

**Options:**

- **(A)** $2 \sqrt{14}$
- **(B)** $\sqrt{14}$
- **(C)** $3 \sqrt{7}$
- **(D)** $2 \sqrt{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \sqrt{14}$**

**Detailed Solution:**

$\begin{aligned}
& \overrightarrow{\mathrm{b}}=\overrightarrow{\mathrm{a}} \times(\hat{\mathrm{i}}-3 \hat{\mathrm{k}}) \\
& =\left|\begin{array}{ccc}
\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\
3 & -1 & 2 \\
1 & 0 & -2
\end{array}\right|=2 \hat{\mathrm{i}}+8 \hat{\mathrm{j}}+\hat{\mathrm{k}} \\
& \overrightarrow{\mathrm{c}}=\overrightarrow{\mathrm{b}} \times \hat{\mathrm{k}}=8 \hat{\mathrm{i}}-2 \hat{\mathrm{j}} \\
& \overrightarrow{\mathrm{c}}-2 \hat{\mathrm{j}}=8 \hat{\mathrm{i}}-4 \hat{\mathrm{j}}
\end{aligned}$

Projection of $(\hat{\mathrm{i}}-2 \hat{\mathrm{j}})$ on $\overrightarrow{\mathrm{a}}$
$\begin{aligned}
& (\overrightarrow{\mathrm{c}}-2 \hat{\mathrm{j}}) \cdot \hat{\mathrm{a}}=\frac{\langle 8,-4,0\rangle \cdot\langle 3,-1,2\rangle}{\sqrt{14}} \\
& =\frac{28}{\sqrt{14}}=2 \sqrt{14}
\end{aligned}$

</details>

---

### Q32. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let the position vectors of three vertices of a triangle be $4 \vec{p}+\vec{q}-3 \vec{r},-5 \vec{p}+\vec{q}+2 \vec{r}$ and $2 \overrightarrow{\mathrm{p}}-\overrightarrow{\mathrm{q}}+2 \overrightarrow{\mathrm{r}}$. If the position vectors of the orthocenter and the circumcenter of the triangle are $\frac{\vec{p}+\vec{q}+\vec{r}}{4}$ and $\alpha \vec{p}+\beta \vec{q}+\gamma \vec{r}$ respectively, then $\alpha+2 \beta+5 \gamma$ is equal to :

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 1
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

We know that
<img src="https://cdn.quizrr.in/question-assets/jee_main_pyq/6VyFFR-RqcQQk_iYV9uMv142CsmcnI1YADCzfhVeK-w.original.fullsize.png">
$\begin{aligned}
& \mathrm{O}\text { (orthocentre) } \frac{\overrightarrow{\mathrm{p}}+\overrightarrow{\mathrm{q}}+\overrightarrow{\mathrm{r}}}{4} \\
& \mathrm{C}(\text { circum centre) } \alpha \overrightarrow{\mathrm{p}}+\beta \overrightarrow{\mathrm{q}}+\gamma \overrightarrow{\mathrm{r}} \\
& \mathrm{C} \text { (centroid) }=\frac{\overrightarrow{\mathrm{p}}+\overrightarrow{\mathrm{q}}+\overrightarrow{\mathrm{r}}}{3}
\end{aligned}$
by relation
$\begin{aligned}
& \Rightarrow 2(\alpha \overrightarrow{\mathrm{p}}+\beta \overrightarrow{\mathrm{q}}+\gamma \overrightarrow{\mathrm{r}})+\frac{\overrightarrow{\mathrm{p}}+\overrightarrow{\mathrm{q}}+\overrightarrow{\mathrm{r}}}{4}=3\left(\frac{\overrightarrow{\mathrm{p}}+\overrightarrow{\mathrm{q}}+\overrightarrow{\mathrm{r}}}{3}\right) \\
& \Rightarrow 8(\alpha \overrightarrow{\mathrm{p}}+\beta \overrightarrow{\mathrm{q}}+\gamma \overrightarrow{\mathrm{r}})=3(\overrightarrow{\mathrm{p}}+\overrightarrow{\mathrm{q}}+\overrightarrow{\mathrm{r}}) \\
& \Rightarrow 8 \alpha=3,8 \beta=3,8 \gamma=3 \\
& \alpha=\frac{3}{8}, \beta=\frac{3}{8}, \gamma=\frac{3}{8} \\
& \therefore \alpha+2 \beta+3 \gamma \\
& \frac{3}{8}+\frac{6}{8}+\frac{15}{8}=\frac{24}{8}=3
\end{aligned}$

</details>

---

### Q33. JEE Main 2025 (22 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $\vec{c}$ be the projection vector of $\vec{b}=\lambda \hat{i}+4 \hat{k}, \lambda\gt0$, on the vector $\vec{a}=\hat{i}+2 \hat{j}+2 \hat{k}$. If $|\vec{a}+\vec{c}|=7$, then the area of the parallelogram formed by the vectors $\vec{b}$ and $\vec{c}$ is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

$\vec{c}=\left(\frac{\vec{b} \cdot \vec{a}}{|\vec{b}|}\right) \frac{\vec{a}}{|\vec{a}|}$
$\begin{aligned} & \quad=\left(\frac{\lambda+8}{9}\right)(\hat{i}+2 \hat{j}+2 \hat{k}) \\ & |\vec{a}+\vec{c}|=7 \\ & \left.\Rightarrow\left(\frac{\lambda+8}{9}+1\right) \hat{i}+\left(\frac{2(\lambda+8)}{9}+2\right) \hat{j}+\left(\frac{2(\lambda+8)}{9}+2\right) \hat{k} \right\rvert\,=7 \\ & \left(\frac{\lambda+8}{9}+1\right)^2+\left(\frac{2(\lambda+8)}{9}+2\right)^2+\left(\frac{2(\lambda+8)}{9}+2\right)^2=49\end{aligned}$
$\Rightarrow \lambda=4 \Rightarrow \vec{c}=\frac{4}{3} \hat{i}+\frac{8}{3} \hat{j}+\frac{8}{3} \hat{k}$
Area of parallelogram $=\left|\begin{array}{ccc}\hat{i} & \hat{j} & \hat{k} \\ \frac{4}{3} & \frac{8}{3} & \frac{8}{3} \\ 4 & 0 & 4\end{array}\right|=16$

</details>

---

### Q34. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=2 \hat{i}+\alpha \hat{j}+\hat{k}, \vec{b}=-\hat{i}+\hat{k}, \vec{c}=\beta \hat{j}-\hat{k}$, where $\alpha$ and $\beta$ are integers and $\alpha \beta=-6$. Let the values of the ordered pair $(\alpha, \beta)$, for which the area of the parallelogram of diagonals $\vec{a}+\vec{b}$ and $\vec{b}+\vec{c}$ is $\frac{\sqrt{21}}{2}$, be $\left(\alpha_1, \beta_1\right)$ and $\left(\alpha_2, \beta_2\right)$. Then $\alpha_1^2+\beta_1^2-\alpha_2 \beta_2$ is equal to

**Options:**

- **(A)** 19
- **(B)** 17
- **(C)** 24
- **(D)** 21

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 19**

**Detailed Solution:**

$\begin{aligned} & \text { Area of parallelogram } \left.=\frac{1}{2} \right\rvert\, \overrightarrow{\mathrm{d}}_1 \times \overrightarrow{\mathrm{d}}_2 \\ & \mathrm{~A}=\frac{1}{2}|(\overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{b}}) \times(\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}})|=\frac{\sqrt{21}}{2} \\ & \text { so, } \overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{b}}=\hat{\mathrm{i}}+\alpha \hat{\mathrm{j}}+2 \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}}=-\hat{\mathrm{i}}+\beta \hat{\mathrm{j}} \\ & (\overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{b}}) \times(\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}})=\left|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 1 & \alpha & 2 \\ -1 & \beta & 0\end{array}\right|\end{aligned}$
$\begin{aligned}
& =\hat{\mathrm{i}}(-2 \beta)-\hat{\mathrm{j}}(2)+\hat{\mathrm{k}}(\beta+\alpha) \\
& |(\overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{b}}) \times(\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}})|=\sqrt{4 \beta^2+4+(\alpha+\beta)^2}=\sqrt{21} \\
& 4 \beta^2+4+\alpha^2+\beta^2+2 \alpha \beta=21 \\
& \alpha^2+5 \beta^2-12=17 \\
& \alpha^2+5 \beta^2=29
\end{aligned}$
and $\alpha \beta=-6$
and given $\alpha_{\mathrm{i}} \beta$ are integers
so, $\alpha=-3, \beta=2$
or
$\begin{aligned}
& \alpha=3, \beta=-2 \\
& \left(\alpha_1, \beta_1\right)=(-3,2) \\
& \left(\alpha_2, \beta_2\right)=(3,-2) \\
& \alpha_1^2+\beta_1^2-\alpha_2 \beta_2=9+4+6=19
\end{aligned}$

</details>

---

### Q35. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Between the following two statements:
Statement I : Let $\vec{a}=\hat{i}+2 \hat{j}-3 \hat{k}$ and $\vec{b}=2 \hat{i}+\hat{j}-\hat{k}$. Then the vector $\vec{r}$ satisfying $\vec{a} \times \vec{r}=\vec{a} \times \vec{b}$ and $\vec{a} \cdot \vec{r}=0$ is of magnitude $\sqrt{10}$.
Statement II : In a triangle $A B C, \cos 2 A+\cos 2 B+\cos 2 C \geq-\frac{3}{2}$.

**Options:**

- **(A)** Statement I is incorrect but Statement II is correct.
- **(B)** Both Statement I and Statement II are correct.
- **(C)** Statement I is correct but Statement II is incorrect.
- **(D)** Both Statement I and Statement II are incorrect.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement I is incorrect but Statement II is correct.**

**Detailed Solution:**

$\begin{aligned} & \bar{a}=\hat{i}+2 \hat{j}-3 \hat{k} \\ & \bar{a}=2 \hat{i}+\hat{j}-\hat{k} \\ & \bar{a} \times \bar{r}=\bar{a} \times \bar{b} ; \bar{a} \cdot \bar{r}=0 \\ & \Rightarrow \bar{a} \times(\bar{r}-\bar{b})=\overline{0} \\ & \Rightarrow \bar{a}=\lambda(\bar{r}-\bar{b}) \\ & \bar{a} \cdot \bar{a}=\lambda(\bar{a} \cdot \bar{r}-\bar{a} \cdot \bar{b}) \\ & 14=-7 \lambda \Rightarrow \lambda=-2 \\ & \frac{-\bar{a}}{2}=\bar{r}-\bar{b} \Rightarrow \bar{r}=\bar{b}-\frac{\bar{a}}{2} \\ & =\frac{2 \bar{b}-\bar{a}}{2}=\frac{3 \hat{i}+\hat{k}}{2}\end{aligned}$
Statement (I) is incorrect
$\begin{aligned}
& \cos 2 \mathrm{~A}+\cos 2 \mathrm{~B}+\cos 2 \mathrm{c} \geq-\frac{3}{2} \\
& 2 \mathrm{~A}+2 \mathrm{~B}+2 \mathrm{C}=2 \pi \\
& \cos 2 \mathrm{~A}+\cos 2 \mathrm{~B}+\cos 2 \mathrm{C} \\
& =-1-4 \cos \mathrm{A} \cdot \cos \mathrm{B} \cdot \cos \mathrm{C} \\
& \geq-1-4 \times \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} \\
& =-\frac{3}{2}
\end{aligned}$
Statement (II) is correct.

</details>

---

### Q36. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $\overrightarrow{O A}=2 \vec{a}, \overrightarrow{O B}=6 \vec{a}+5 \vec{b}$ and $\overrightarrow{O C}=3 \vec{b}$, where $O$ is the origin. If the area of the parallelogram with adjacent sides $\overrightarrow{\mathrm{OA}}$ and $\overrightarrow{\mathrm{OC}}$ is 15 sq. units, then the area (in sq. units) of the quadrilateral $\mathrm{OABC}$ is equal to :

**Options:**

- **(A)** 32
- **(B)** 40
- **(C)** 38
- **(D)** 35

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 35**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/R03ZKqUVZMUyO2sKnQw-fpTC9FnOLVQnA-nc6fvNDcI.original.fullsize.png">
Area of parallelogram having sides
$\begin{aligned}
& \overrightarrow{\mathrm{OA}} \& \overrightarrow{\mathrm{OC}}=|\overrightarrow{\mathrm{OA}} \times \overrightarrow{\mathrm{OC}}|=|2 \overrightarrow{\mathrm{a}} \times 3 \overrightarrow{\mathrm{b}}|=15 \\
& 6|\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}|=15 \\
& \Rightarrow|\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}|=\frac{5}{2} \ldots \ldots . .(1)
\end{aligned}$
Area of quadrilateral
$\begin{aligned}
& \mathrm{OABC}=\frac{1}{2}\left|\overrightarrow{\mathrm{d}}_1 \times \overrightarrow{\mathrm{d}}_2\right| \\
& =\frac{1}{2}|\overrightarrow{\mathrm{AC}} \times \overrightarrow{\mathrm{OB}}|=\frac{1}{2}|(3 \overrightarrow{\mathrm{b}}-2 \overrightarrow{\mathrm{a}}) \times(6 \overrightarrow{\mathrm{a}}+5 \overrightarrow{\mathrm{b}})| \\
& =\frac{1}{2}|18 \overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{a}}-10 \overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}|=14|\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}| \\
& =14 \times \frac{5}{2}=35
\end{aligned}$

</details>

---

### Q37. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let three vectors $\overrightarrow{\mathrm{a}}=\alpha \hat{i}+4 \hat{j}+2 \hat{k}, \overrightarrow{\mathrm{b}}=5 \hat{i}+3 \hat{j}+4 \hat{k}, \overrightarrow{\mathrm{c}}=x \hat{i}+y \hat{j}+z \hat{k}$ form a triangle such that $\vec{c}=\vec{a}-\vec{b}$ and the area of the triangle is $5 \sqrt{6}$. If $\alpha$ is a positive real number, then $|\vec{c}|^2$ is equal to:

**Options:**

- **(A)** 16
- **(B)** 14
- **(C)** 12
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 14**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{\mathrm{c}}=\overrightarrow{\mathrm{a}}-\overrightarrow{\mathrm{b}} \\ & \Rightarrow(\mathrm{x}, \mathrm{y}, \mathrm{z})=(\alpha-5,1,-2) \\ & \Rightarrow \mathrm{x}=\alpha-5, \mathrm{y}=1, \mathrm{z}=-2.....(1)\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/M074W3MRgFvR77533axS5ulg6eQ2rQXZAOuQeTd4oR8.original.fullsize.png">
Area of $\Delta=5 \sqrt{6}$ (given)
$\begin{aligned} & \frac{1}{2}|\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{c}}|=5 \sqrt{6} \\ & \left\|\begin{array}{ccc}\hat{\mathrm{i}} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ \alpha & 4 & 2 \\ \mathrm{x} & 1 & -2\end{array}\right\|=10 \sqrt{6}\end{aligned}$
$\begin{aligned} & \Rightarrow|-10 \hat{\mathrm{i}}-\hat{\mathrm{j}}(-2 \alpha-2 \mathrm{x})+\hat{\mathrm{k}}(\alpha-4 \mathrm{x})|=10 \sqrt{6} \\ & \Rightarrow(2 \alpha+2 \alpha-10)^2+(\alpha-4 \alpha+20)^2=500 \\ & \Rightarrow(4 \alpha-10)^2+(20-3 \alpha)^2=500 \\ & \Rightarrow 25 \alpha^2-80 \alpha-120 \alpha=0 \\ & \Rightarrow \alpha(25 \alpha-200)=0 \\ & \Rightarrow \alpha=8 \text { (given } \alpha \text { is +ve number) } \\ & \Rightarrow \mathrm{x}=\alpha-5=3 \\ & |\overrightarrow{\mathrm{c}}|^2=\mathrm{x}^2+\mathrm{y}^2+\mathrm{z}^2 \\ & =9+1+4 \\ & =14\end{aligned}$

</details>

---

### Q38. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The set of all $\alpha$, for which the vectors $\vec{a}=\alpha t \hat{i}+6 \hat{j}-3 \hat{k}$ and $\vec{b}=t \hat{i}-2 \hat{j}-2 \alpha t \hat{k}$ are inclined at an obtuse angle for all $t \in \mathbb{R}$, is

**Options:**

- **(A)** $\left(-\frac{4}{3}, 1\right)$
- **(B)** $[0,1)$
- **(C)** $\left(-\frac{4}{3}, 0\right]$
- **(D)** $(-2,0]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(-\frac{4}{3}, 0\right]$**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{\mathrm{a}}=\alpha \hat{\mathrm{i}}+6 \hat{\mathrm{j}}-3 \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{b}}=\mathrm{t} \hat{\mathrm{i}}-2 \hat{\mathrm{j}}-2 \alpha \hat{\mathrm{k}} \\ & \text { so } \overrightarrow{\mathrm{a}} \overrightarrow{\mathrm{b}} < 0, \forall \mathrm{t} \in \mathrm{R} \\ & \alpha \mathrm{t}^2-12+6 \alpha \mathrm{t} < 0 \\ & \alpha \mathrm{t}^2+6 \alpha \mathrm{t}-12 < 0, \forall \mathrm{t} \in \mathrm{R} \\ & \alpha < 0 \text {, and } \mathrm{D} < 0 \\ & 36 \alpha^2+48 \alpha < 0 \\ & 12 \alpha(3 \alpha+4) < 0 \\ & \frac{-4}{3} < \alpha < 0\end{aligned}$
also for $\mathrm{a}=0, \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{b}} < 0$
hence a $\alpha \in\left(\frac{-4}{3}, 0\right]$

</details>

---

### Q39. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\overrightarrow{\mathrm{a}}=2 \hat{i}+5 \hat{j}-\hat{k}, \overrightarrow{\mathrm{b}}=2 \hat{i}-2 \hat{j}+2 \hat{k}$ and $\overrightarrow{\mathrm{c}}$ be three vectors such that $(\vec{c}+\hat{i}) \times(\vec{a}+\vec{b}+\hat{i})=\vec{a} \times(\vec{c}+\hat{i})$. If $\vec{a} \cdot \vec{c}=-29$, then $\vec{c} \cdot(-2 \hat{i}+\hat{j}+\hat{k})$ is equal to:

**Options:**

- **(A)** 15
- **(B)** 12
- **(C)** 10
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 5**

**Detailed Solution:**

Let's assume
$\begin{aligned}
\vec{v} & =\vec{a}+\vec{b}+\hat{i} \\
& =5 \hat{i}+3 \hat{j}+\hat{k}
\end{aligned}$
and $\overrightarrow{\mathrm{c}}+\hat{\mathrm{i}}=\overrightarrow{\mathrm{p}}$
So,
$\begin{aligned}
& \overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{v}}=\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{p}} \\
& \overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{v}}+\overrightarrow{\mathrm{p}} \times \overrightarrow{\mathrm{a}}=\overrightarrow{0} \\
& \overrightarrow{\mathrm{p}} \times(\overrightarrow{\mathrm{v}}+\overrightarrow{\mathrm{a}})=\overrightarrow{0} \\
& \Rightarrow \overrightarrow{\mathrm{p}}=\lambda(\overrightarrow{\mathrm{v}}+\overrightarrow{\mathrm{a}}) \\
& \overrightarrow{\mathrm{c}}+\mathrm{i}=\lambda(7 \hat{\mathrm{i}}+8 \hat{\mathrm{j}}) \\
& \overline{\mathrm{a}} \cdot \overline{\mathrm{c}}+\overline{\mathrm{a}} \cdot \hat{\mathrm{i}}=\lambda \overline{\mathrm{a}} \cdot(7 \hat{\mathrm{i}}+8 \hat{\mathrm{j}}) \\
& -29+2=\lambda(14+40) \\
& \lambda=-\frac{1}{2}
\end{aligned}$
$\begin{gathered}\overrightarrow{\mathrm{c}} \cdot(-2 \hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}})+\hat{\mathrm{i}} \cdot(-2 \hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}})=\lambda(7 \hat{\mathrm{i}}+8 \hat{\mathrm{j}}) \cdot(-2 \hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}) \\ =-\frac{1}{2}(-14+8)+2=5\end{gathered}$

</details>

---

### Q40. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider three vectors $\vec{a}, \vec{b}, \vec{c}$. Let $|\vec{a}|=2,|\vec{b}|=3$ and $\vec{a}=\vec{b} \times \vec{c}$. If $\alpha \in\left[0, \frac{\pi}{3}\right]$ is the angle between the vectors $\vec{b}$ and $\vec{c}$, then the minimum value of $27|\vec{c}-\vec{a}|^2$ is equal to:

**Options:**

- **(A)** 110
- **(B)** 124
- **(C)** 121
- **(D)** 105

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 124**

**Detailed Solution:**

$\begin{aligned} & |\overrightarrow{\mathrm{c}}-\overrightarrow{\mathrm{a}}|=|\overrightarrow{\mathrm{c}}|^2+|\overrightarrow{\mathrm{a}}|^2-2 \overline{\mathrm{a}} \cdot \overline{\mathrm{c}} \\ & =|\overrightarrow{\mathrm{c}}|^2+4-0 \\ & \because \overrightarrow{\mathrm{a}}=\overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{c}} \\ & |\overrightarrow{\mathrm{a}}|=|\overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{c}}| \\ & 2=3|\overrightarrow{\mathrm{c}}| \sin \alpha \\ & |\overrightarrow{\mathrm{c}}|=\frac{2}{3} \operatorname{cosec} \alpha \quad \alpha \in\left[0, \frac{\pi}{3}\right] \\ & |\overrightarrow{\mathrm{c}}|_{\min }=\frac{2}{3} \times \frac{2}{\sqrt{3}} \quad \operatorname{cosec} \alpha \in\left[\frac{2}{\sqrt{3}}, \infty\right) \\ & \Rightarrow 27|\overrightarrow{\mathrm{c}}-\overrightarrow{\mathrm{a}}|_{\min }^2=27\left(\frac{16}{27}+4\right)=124\end{aligned}$

</details>

---

### Q41. JEE Main 2024 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mo>−</mo><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mn>8</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math> be three vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mover><mi>c</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover></math>. If the angle between the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover></math> and the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>θ</mi></math>, then the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mn>2</mn></msup><mi>θ</mi></math> is:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **38**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>k</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mo>−</mo><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mn>8</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mi>k</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mover><mi>c</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>b</mi><mo>→</mo></mover><mo>−</mo><mover><mi>c</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>b</mi><mo>→</mo></mover><mo>−</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mi>λ</mi><mover><mi>a</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mover><mi>c</mi><mo>→</mo></mover><mo>+</mo><mi>λ</mi><mover><mi>a</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>−</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mi>k</mi><mo>=</mo><mfenced><mrow><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mi>k</mi></mrow></mfenced><mo>+</mo><mi>λ</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>k</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>+</mo><mn>4</mn><mo>=</mo><mo>−</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>λ</mi><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mo>=</mo><mo>−</mo><mn>8</mn><mo>,</mo><mo> </mo><mi>λ</mi><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mo>−</mo><mn>5</mn><mo>,</mo><mo> </mo><msub><mi>c</mi><mn>2</mn></msub><mo>=</mo><mo>−</mo><mn>3</mn><mo>,</mo><mo> </mo><msub><mi>c</mi><mn>3</mn></msub><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mi>k</mi></math></p><p>Now, finding angle we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>·</mo><mfenced><mrow><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><mrow><mfenced close="|" open="|"><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mfenced><mo>⋅</mo><mfenced close="|" open="|"><mfenced><mrow><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><mn>12</mn><mo>−</mo><mn>12</mn><mo>+</mo><mn>7</mn></mrow><mrow><msqrt><mn>26</mn></msqrt><mo>⋅</mo><msqrt><mn>74</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>θ</mi><mo>=</mo><mfrac><mn>7</mn><mrow><msqrt><mn>26</mn></msqrt><mo>⋅</mo><msqrt><mn>74</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>θ</mi><mo>=</mo><mfrac><mn>7</mn><mrow><mn>2</mn><msqrt><mn>481</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sec</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>481</mn></msqrt></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>θ</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mo>×</mo><mn>481</mn></mrow><mn>49</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>θ</mi><mo>=</mo><mfrac><mn>1924</mn><mn>49</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>θ</mi><mo>=</mo><mfrac><mn>1875</mn><mn>49</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>θ</mi><mo>≈</mo><mn>38</mn><mo>.</mo><mn>26</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>θ</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mn>38</mn><mo>.</mo><mn>26</mn></mrow></mfenced><mo>=</mo><mn>38</mn></math></p>

</details>

---

### Q42. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Δ</mi><mi>A</mi><mi>B</mi><mi>C</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced><mrow><mo>−</mo><mn>2</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math>. If the angle bisector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∠</mo><mi>B</mi><mi>A</mi><mi>C</mi></math> meets the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math>, then the length of the projection of the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>→</mo></mover></math> on the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>→</mo></mover></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>37</mn><mrow><mn>2</mn><msqrt><mn>38</mn></msqrt></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>38</mn></msqrt><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>39</mn><mrow><mn>2</mn><msqrt><mn>38</mn></msqrt></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>19</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>37</mn><mrow><mn>2</mn><msqrt><mn>38</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>B</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mi>C</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math></p><p>And angle bisector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∠</mo><mi>B</mi><mi>A</mi><mi>C</mi></math> meets the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math>,</p><p>Now, plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ca9b42a2-c2b6-4861-9917-33a8bde160e1.png" style="width: 300px; height: 194px;"/></p><p>Now, finding</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>→</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>→</mo></mover></mfenced><mo>=</mo><msqrt><mn>4</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>25</mn></msqrt><mo>=</mo><msqrt><mn>38</mn></msqrt></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>→</mo></mover></mfenced><mo>=</mo><msqrt><mn>9</mn><mo>+</mo><mn>25</mn><mo>+</mo><mn>4</mn></msqrt><mo>=</mo><msqrt><mn>38</mn></msqrt></math></p><p>Using angle bisector theorem, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>B</mi><mi>D</mi></mrow><mrow><mi>C</mi><mi>D</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>A</mi><mi>B</mi></mrow><mrow><mi>A</mi><mi>C</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>B</mi><mi>D</mi><mo>:</mo><mi>C</mi><mi>D</mi><mo>=</mo><mn>1</mn><mo>:</mo><mn>1</mn></math></p><p>Using section formula to find coordinates of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>D</mi><mo>≡</mo><mfenced><mrow><mfrac><mrow><mn>1</mn><mo>×</mo><mn>3</mn><mo>+</mo><mn>1</mn><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>,</mo><mo> </mo><mfrac><mrow><mn>1</mn><mo>×</mo><mn>6</mn><mo>+</mo><mn>1</mn><mo>×</mo><mn>8</mn></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>,</mo><mo> </mo><mfrac><mrow><mn>1</mn><mo>×</mo><mn>7</mn><mo>+</mo><mn>1</mn><mo>×</mo><mn>0</mn></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>D</mi><mo>≡</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo> </mo><mn>7</mn><mo>,</mo><mo> </mo><mfrac><mn>7</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>→</mo></mover><mo>=</mo><mo>−</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>8</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Length of projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>→</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>→</mo></mover></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>→</mo></mover><mo>·</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>→</mo></mover></mrow><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>→</mo></mover></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mo>=</mo><mfrac><mn>37</mn><mrow><mn>2</mn><msqrt><mn>38</mn></msqrt></mrow></mfrac></math></p>

</details>

---

### Q43. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mo>−</mo><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo> </mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mfenced><mrow><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover><mo>⋅</mo><mfenced><mrow><mo>−</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>12</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>13</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>15</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>12</mn></math>**

**Detailed Solution:**

<p>Given: </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mo>−</mo><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>j</mi><mo>−</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>⋅</mo><mover><mi>i</mi><mo>^</mo></mover></mrow></mfenced><mover><mi>b</mi><mo>→</mo></mover><mo>−</mo><mfenced><mrow><mover><mi>b</mi><mo>→</mo></mover><mo>⋅</mo><mover><mi>i</mi><mo>^</mo></mover></mrow></mfenced><mover><mi>a</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover><mo>=</mo><mo>−</mo><mn>5</mn><mover><mi>b</mi><mo>→</mo></mover><mo>−</mo><mover><mi>a</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover><mo>=</mo><mfenced><mrow><mfenced><mrow><mfenced><mrow><mo>−</mo><mn>5</mn><mover><mi>b</mi><mo>→</mo></mover><mo>−</mo><mover><mi>a</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover><mo>=</mo><mfenced><mrow><mfenced><mrow><mo>−</mo><mn>11</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>23</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover><mo>=</mo><mfenced><mrow><mn>11</mn><mover><mi>k</mi><mo>^</mo></mover><mo>+</mo><mn>23</mn><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>i</mi><mo>^</mo></mover><mo>=</mo><mfenced><mrow><mn>11</mn><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>23</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>c</mi><mo>→</mo></mover><mo>.</mo><mfenced><mrow><mo>−</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>11</mn><mo>−</mo><mn>23</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>c</mi><mo>→</mo></mover><mo>.</mo><mfenced><mrow><mo>−</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mo>−</mo><mn>12</mn></math></p>

</details>

---

### Q44. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover></math> be a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>+</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>+</mo><mn>24</mn><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>−</mo><mover><mi>b</mi><mo>→</mo></mover><mo>+</mo><mover><mi>i</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mo>−</mo><mn>3</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover><mi>c</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup></math> is equal to _______.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **38**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo> </mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover></math> be a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>+</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>+</mo><mn>24</mn><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></math> </p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>7</mn><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mn>7</mn><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now, solving</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>+</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>+</mo><mn>24</mn><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn><mfenced><mrow><mn>7</mn><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mn>7</mn><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mn>24</mn><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mi>z</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>14</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>10</mn><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>20</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>i</mi><mo>^</mo></mover><mfenced><mrow><mi>z</mi><mo>−</mo><mn>4</mn><mi>y</mi></mrow></mfenced><mo>−</mo><mover><mi>j</mi><mo>^</mo></mover><mfenced><mrow><mn>5</mn><mi>z</mi><mo>−</mo><mn>4</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mfenced><mrow><mn>5</mn><mi>y</mi><mo>−</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>14</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>10</mn><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>20</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now, on comparing both side, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>−</mo><mn>4</mn><mi>y</mi><mo>=</mo><mn>14</mn><mo>,</mo><mo> </mo><mn>4</mn><mi>x</mi><mo>−</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>10</mn><mo>,</mo><mo> </mo><mn>5</mn><mi>y</mi><mo>−</mo><mi>x</mi><mo>=</mo><mo>−</mo><mn>20</mn><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Now, solving </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>−</mo><mover><mi>b</mi><mo>→</mo></mover><mo>+</mo><mover><mi>i</mi><mo>^</mo></mover></mrow></mfenced><mo>·</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mo>−</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>·</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mo>−</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>−</mo><mn>2</mn><mi>z</mi><mo>=</mo><mo>−</mo><mn>3</mn><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now, solving the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mo> </mo><mi>x</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mo>−</mo><mn>3</mn><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced close="|" open="|"><mover><mi>c</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>25</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>38</mn></math></p>

</details>

---

### Q45. JEE Main 2024 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover></math> be two vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>→</mo></mover></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mo>=</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>⋅</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mn>2</mn><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>−</mo><mn>3</mn><mover><mi>b</mi><mo>→</mo></mover></math> and the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover></math> and<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>192</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>α</mi></math> is equal to _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **48**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover></math> be two vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>→</mo></mover></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mo>=</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>⋅</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn></math>.</p><p>Also, given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mn>2</mn><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>−</mo><mn>3</mn><mover><mi>b</mi><mo>→</mo></mover></math></p><p>Taking dot product with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover></math> both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>b</mi><mo>→</mo></mover><mo>⋅</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mn>2</mn><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>⋅</mo><mover><mi>b</mi><mo>→</mo></mover><mo>−</mo><mn>3</mn><msup><mfenced close="|" open="|"><mi>b</mi></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>c</mi><mo>→</mo></mover></mfenced><mi>cos</mi><mi>α</mi><mo>=</mo><mn>0</mn><mo>−</mo><mn>3</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mover><mi>c</mi><mo>→</mo></mover></mfenced><mi>cos</mi><mi>α</mi><mo>=</mo><mo>−</mo><mn>12</mn></math> {as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mo>=</mo><mn>4</mn></math>}</p><p>Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>⋅</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mover><mi>a</mi><mo>→</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mi>cos</mi><mi>θ</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>θ</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>⇒</mo><mi>θ</mi><mo>=</mo><mfrac><mi>π</mi><mn>3</mn></mfrac></math></p><p>Now, solving</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover><mi>c</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mfenced><mrow><mn>2</mn><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>−</mo><mn>3</mn><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced close="|" open="|"><mover><mi>c</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>64</mn><mo>×</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>+</mo><mn>144</mn><mo>=</mo><mn>192</mn></math></p><p>Now, squaring both side of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>c</mi><mo>→</mo></mover></mfenced><mi>cos</mi><mi>α</mi><mo>=</mo><mo>−</mo><mn>12</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover><mi>c</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup><msup><mi>cos</mi><mn>2</mn></msup><mi>α</mi><mo>=</mo><mn>144</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>192</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>α</mi><mo>=</mo><mn>144</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>192</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>α</mi></mrow></mfenced><mo>=</mo><mn>144</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>192</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>α</mi><mo>=</mo><mn>48</mn></math></p>

</details>

---

### Q46. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo> </mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math> be three vectors. If a vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>→</mo></mover></math> satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mover><mi>c</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>→</mo></mover><mo>⋅</mo><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>→</mo></mover><mo>⋅</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>−</mo><mover><mi>j</mi><mo>^</mo></mover><mo>−</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mover><mi>c</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>p</mi><mo>→</mo></mover><mo>-</mo><mover><mi>c</mi><mo>→</mo></mover></mrow></mfenced><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>p</mi><mo>→</mo></mover><mo>-</mo><mover><mi>c</mi><mo>→</mo></mover></mrow></mfenced><mo>|</mo><mo>|</mo><mover><mi>b</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>p</mi><mo>→</mo></mover><mo>-</mo><mover><mi>c</mi><mo>→</mo></mover></mrow></mfenced><mo>=</mo><mi>k</mi><mover><mi>b</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>p</mi><mo>→</mo></mover><mo>=</mo><mi>k</mi><mover><mi>b</mi><mo>→</mo></mover><mo>+</mo><mover><mi>c</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>p</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mn>4</mn><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>k</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>7</mn><mi>k</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>→</mo></mover><mo>.</mo><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mfenced><mrow><mn>4</mn><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>k</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mn>7</mn><mi>k</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>k</mi><mo>=</mo><mo>-</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>p</mi><mo>→</mo></mover><mo>=</mo><mo>-</mo><mn>31</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>11</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>52</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>p</mi><mo>→</mo></mover><mo>.</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mo>-</mo><mn>31</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>52</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>p</mi><mo>→</mo></mover><mo>.</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>32</mn></math></p>

</details>

---

### Q47. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover></math> be two vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>b</mi><mo>→</mo></mover><mo>|</mo><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover><mo>|</mo><mo>=</mo><mn>2</mn></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mo>(</mo><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover><mo>)</mo><mo>-</mo><mover><mi>b</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<blockquote><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mfenced close="|" open="|"><mrow><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p>Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover><mo>-</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mn>2</mn></msup></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover><mo>-</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mrow><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover></mrow></mfenced><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover></math></p><p>Now, we know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover></mrow></mfenced><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover></mrow></mfenced><mo>·</mo><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover><mo>-</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>×</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>b</mi><mo>→</mo></mover><mo>×</mo><mover><mi>a</mi><mo>→</mo></mover><mo>-</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q48. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>α</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>β</mi><mover><mi>k</mi><mo>^</mo></mover><mo> </mo><mo>,</mo><mo> </mo><mi>α</mi><mo>,</mo><mi>β</mi><mo>∈</mo><mi>R</mi></math>. Let a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover></math> be such that the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>6</mn></math>, If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup></mrow></mfenced><mo>|</mo><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>75</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>95</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>85</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn></math>**

**Detailed Solution:**

<blockquote><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>6</mn><mo>,</mo><mo> </mo><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>,</mo><mo> </mo><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>α</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>β</mi><mover><mi>k</mi><mo>^</mo></mover></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>.</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mfenced close="|" open="|"><mover><mi>a</mi><mo>→</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mi>cos</mi><mi>θ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>=</mo><msqrt><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup></msqrt><mfenced><msqrt><mn>6</mn></msqrt></mfenced><mi>cos</mi><mfrac><mi>π</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>=</mo><msqrt><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup></msqrt><mfenced><msqrt><mn>3</mn></msqrt></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>6</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>+</mo><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup><mo>=</mo><mn>5</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mover><mi>a</mi><mo>→</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mi>sin</mi><mi>θ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>=</mo><msqrt><mn>6</mn></msqrt><msqrt><mn>6</mn></msqrt><mi>sin</mi><mfrac><mi>π</mi><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>6</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup></mrow></mfenced><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>5</mn><mo>×</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup></mrow></mfenced><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>90</mn></math></p></blockquote>

</details>

---

### Q49. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><msub><mi>a</mi><mi>i</mi></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><msub><mi>b</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>3</mn></msub><mover><mi>k</mi><mo>^</mo></mover><mo>  </mo></math> be two vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>a</mi><mo>→</mo></mover><mo>|</mo><mo>=</mo><mn>1</mn><mo>;</mo><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>b</mi><mo>→</mo></mover><mo>|</mo><mo>=</mo><mn>4</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn><mo>(</mo><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover><mo>)</mo><mo>-</mo><mn>3</mn><mover><mi>b</mi><mo>→</mo></mover></math>, then the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>a</mi><mo>→</mo></mover><mo>|</mo><mo>=</mo><mn>1</mn><mo>,</mo><mo>|</mo><mover><mi>b</mi><mo>→</mo></mover><mo>|</mo><mo>=</mo><mn>4</mn><mo>,</mo><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mn>2</mn><mo>(</mo><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover><mo>)</mo><mo>-</mo><mn>3</mn><mover><mi>b</mi><mo>→</mo></mover><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Applying dot product with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover></math> on both sides of equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>c</mi><mo>→</mo></mover><mo>·</mo><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mo>-</mo><mn>6</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><mo>(</mo><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover><mo>)</mo><mo>·</mo><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mo>(</mo><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover><mo>)</mo><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>0</mn></mrow></mfenced></math></p><p>Again, applying dot product with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover></math> on both sides of equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>b</mi><mo>→</mo></mover><mo>·</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mo>-</mo><mn>48</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now, using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced close="|" open="|"><mover><mi>c</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>|</mo><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>+</mo><mn>9</mn><mo>|</mo><mover><mi>b</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>-</mo><mn>12</mn><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>.</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>|</mo><mover><mi>c</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>4</mn><mfenced close="]" open="["><mrow><mo>|</mo><mover><mi>a</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>|</mo><mo> </mo><mover><mi>b</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>-</mo><mo>(</mo><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover><msup><mo>)</mo><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mn>9</mn><mo>|</mo><mover><mi>b</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>|</mo><mover><mi>c</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>4</mn><mfenced close="]" open="["><mrow><mo>(</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>4</mn><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mo>(</mo><mn>4</mn><mo>)</mo></mrow></mfenced><mo>+</mo><mn>9</mn><mo>(</mo><mn>16</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>|</mo><mover><mi>c</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>×</mo><mn>12</mn><mo>+</mo><mn>144</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>|</mo><mover><mi>c</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>48</mn><mo>+</mo><mn>144</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>|</mo><mover><mi>c</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>192</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><mover><mi>b</mi><mo>→</mo></mover><mo>·</mo><mover><mi>c</mi><mo>→</mo></mover></mrow><mrow><mo>|</mo><mover><mi>b</mi><mo>→</mo></mover><mo>|</mo><mo>|</mo><mover><mi>c</mi><mo>→</mo></mover><mo>|</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>48</mn></mrow><mrow><msqrt><mn>192</mn></msqrt><mo>×</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>48</mn></mrow><mrow><mn>8</mn><msqrt><mn>3</mn></msqrt><mo>.</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>θ</mi><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></mfenced></math></p>

</details>

---

### Q50. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>(</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo></math> be opposite vertices of a parallelogram <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math> if the diagonal <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>B</mi><mi>D</mi></mrow><mo>→</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> then the area of the parallelogram is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msqrt><mn>410</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msqrt><mn>474</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msqrt><mn>586</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msqrt><mn>306</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msqrt><mn>474</mn></msqrt></math>**

**Detailed Solution:**

<p>Area of the parallelogram is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mrow><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>→</mo></mover><mo>×</mo><mover><mrow><mi>B</mi><mi>D</mi></mrow><mo>→</mo></mover></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Area</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mrow><mfenced><mrow><mo>-</mo><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>×</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Area</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>7</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Area</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mrow><mn>17</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>8</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>11</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Area</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msqrt><mn>289</mn><mo>+</mo><mn>64</mn><mo>+</mo><mn>121</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Area</mi><mo>=</mo><mfrac><msqrt><mn>474</mn></msqrt><mn>2</mn></mfrac></math> square units.</p>

</details>

---

### Q51. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let a unit vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>^</mo></mover><mo>=</mo><mi>x</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>y</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>z</mi><mover><mi>k</mi><mo>^</mo></mover></math> make angles <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>π</mi><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mn>3</mn></mfrac></math> with the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>j</mi><mo>^</mo></mover></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>→</mo></mover><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>k</mi><mo>^</mo></mover></math>, then \(|\hat{u}-\vec{v}|^2\) is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Unit vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>^</mo></mover><mo>=</mo><mi>x</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>y</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>z</mi><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>p</mi><mo>→</mo></mover><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><msub><mover><mi>p</mi><mo>→</mo></mover><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>p</mi><mo>→</mo></mover><mn>3</mn></msub><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>j</mi><mo>^</mo></mover></math></p><p>Now angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>p</mi><mo>→</mo></mover><mn>1</mn></msub><mo>=</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>^</mo></mover><mo>·</mo><msub><mover><mi>p</mi><mo>→</mo></mover><mn>1</mn></msub><mo>=</mo><mn>0</mn><mo>⇒</mo><mfrac><mi>x</mi><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mi>z</mi><msqrt><mn>2</mn></msqrt></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo> </mo><mo>…</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>p</mi><mo>→</mo></mover><mn>2</mn></msub><mo>=</mo><mfrac><mi>π</mi><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>^</mo></mover><mo>·</mo><msub><mover><mi>p</mi><mo>→</mo></mover><mn>2</mn></msub><mo>=</mo><mo>|</mo><mover><mi>u</mi><mo>^</mo></mover><mo>|</mo><mo>·</mo><mfenced close="|" open="|"><msub><mover><mi>p</mi><mo>→</mo></mover><mn>2</mn></msub></mfenced><mi>cos</mi><mfrac><mi>π</mi><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">u</mi><mo>^</mo></mover><mo>·</mo><msub><mover><mi mathvariant="normal">p</mi><mo>→</mo></mover><mn>2</mn></msub><mo>=</mo><mo> </mo><mfrac><mi>y</mi><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mi>z</mi><msqrt><mn>2</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo>…</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>p</mi><mo>→</mo></mover><mn>3</mn></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>^</mo></mover><mo>·</mo><msub><mover><mi>p</mi><mo>→</mo></mover><mn>3</mn></msub><mo>=</mo><mo>|</mo><mover><mi>u</mi><mo>^</mo></mover><mo>|</mo><mo>·</mo><mfenced close="|" open="|"><msub><mover><mi>p</mi><mo>→</mo></mover><mn>3</mn></msub></mfenced><mi>cos</mi><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>x</mi><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mi>y</mi><msqrt><mn>2</mn></msqrt></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mo> </mo><mo>…</mo><mfenced><mi>iii</mi></mfenced></math></p><p>from equation (i), (ii) and (iii) we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mo>,</mo><mo>  </mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>  </mo><mi>z</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p>Thus <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>^</mo></mover><mo>-</mo><mover><mi>v</mi><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>k</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>u</mi><mo>^</mo></mover><mo>-</mo><mover><mi>v</mi><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mover><mi>j</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mo>|</mo><mover><mi>u</mi><mo>^</mo></mover><mo>-</mo><mover><mi>v</mi><mo>→</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><msup><mfenced><msqrt><mfrac><mn>4</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></msqrt></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q52. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>OA</mi><mo>→</mo></mover><mo>=</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>,</mo><mover><mi>OB</mi><mo>→</mo></mover><mo>=</mo><mn>12</mn><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>OC</mi><mo>→</mo></mover><mo>=</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">O</mi></math> is the origin. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is the parallelogram with adjacent sides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>OA</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>OC</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>area</mi><mo> </mo><mi>of</mi><mo> </mo><mi>the</mi><mo> </mo><mi>quadrilateral</mi><mo> </mo><mi>OABC</mi></mrow><mrow><mi>area</mi><mo> </mo><mi>of</mi><mo> </mo><mi mathvariant="normal">S</mi></mrow></mfrac></math> is equal to _____

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/770b7c52-2553-463b-8394-784603ca0e7f.png" style="width: 250px; height: 202px;"/></p><p>Area of parallelogram, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>=</mo><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>×</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>|</mo></math></p><p>Area of quadrilateral = Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>∆</mo><mi>OAB</mi></mrow></mfenced><mo>+</mo></math>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>∆</mo><mi>OBC</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>{</mo><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>×</mo><mo>(</mo><mn>12</mn><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>)</mo><mo>|</mo><mo>+</mo><mo>|</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>×</mo><mo>(</mo><mn>12</mn><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>)</mo><mo>|</mo><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>{</mo><mo>|</mo><mn>4</mn><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>×</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>|</mo><mo>+</mo><mo>|</mo><mn>12</mn><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>×</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>|</mo><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>{</mo><mn>4</mn><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>×</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>|</mo><mo>+</mo><mn>12</mn><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>×</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>|</mo><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>16</mn><mn>2</mn></mfrac><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>×</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>|</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mo>|</mo><mo>(</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>×</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>)</mo><mo>|</mo></math></p><p>Ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>8</mn><mo>|</mo><mo>(</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>×</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>)</mo><mo>|</mo></mrow><mrow><mo>|</mo><mo>(</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>×</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>)</mo><mo>|</mo></mrow></mfrac><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q53. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

The least positive integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math>, for which the angle between the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mi>α</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> is acute, is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>.</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mfenced close="|" open="|"><mover><mi>a</mi><mo>→</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mi>cos</mi><mi>θ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><mo>(</mo><mi>α</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>)</mo><mo>·</mo><mo>(</mo><mi>α</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mi>α</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>)</mo></mrow><mrow><msqrt><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn></msqrt><msqrt><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><msup><mi>α</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>α</mi><mo>-</mo><mn>4</mn></mrow><mrow><msqrt><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn></msqrt><msqrt><mn>5</mn><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></msqrt></mrow></mfrac></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>θ</mi></math> is acute,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>α</mi><mo>-</mo><mn>4</mn><mo>&gt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>α</mi><mo>+</mo><mn>4</mn><mo>&gt;</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>(</mo><mi>α</mi><mo>-</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>&gt;</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>-</mo><mn>2</mn><mo>&gt;</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>-</mo><mn>2</mn><mo>&lt;</mo><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>&gt;</mo><mn>2</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>&lt;</mo><mn>2</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p><p>So, the least positive integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>.</p>

</details>

---

### Q54. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo> </mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>3</mn><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover></math> be the vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mover><mi>b</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mn>3</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mo>(</mo><mfenced><mrow><mover><mi>c</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>-</mo><mover><mi>b</mi><mo>→</mo></mover><mo>-</mo><mover><mi>c</mi><mo>→</mo></mover><mo>)</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>3</mn><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mover><mi>b</mi><mo>→</mo></mover></math>.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>c</mi><mo>→</mo></mover><mo>=</mo><mover><mi>b</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>c</mi><mo>→</mo></mover></mrow></mfenced><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>→</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>c</mi><mo>→</mo></mover></mrow></mfenced><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><msup><mfenced><mrow><mn>3</mn><msqrt><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>c</mi><mo>→</mo></mover></mrow></mfenced><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>27</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mfenced><mrow><mover><mi>c</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>=</mo><mn>27</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mfenced><mrow><mover><mi>c</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>=</mo><mover><mi>b</mi><mo>→</mo></mover><mo>·</mo><mfenced><mrow><mover><mi>a</mi><mo>→</mo></mover><mo>×</mo><mover><mi>c</mi><mo>→</mo></mover></mrow></mfenced></mrow></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover><mo>=</mo><mn>3</mn><mo>-</mo><mn>6</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mfenced><mrow><mfenced><mrow><mover><mi>c</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>-</mo><mover><mi>b</mi><mo>→</mo></mover><mo>-</mo><mover><mi>c</mi><mo>→</mo></mover></mrow></mfenced><mo>=</mo><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mfenced><mrow><mover><mi>c</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>-</mo><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mover><mi>b</mi><mo>→</mo></mover><mo>-</mo><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mover><mi>c</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mfenced><mrow><mfenced><mrow><mover><mi>c</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>-</mo><mover><mi>b</mi><mo>→</mo></mover><mo>-</mo><mover><mi>c</mi><mo>→</mo></mover></mrow></mfenced><mo>=</mo><mn>27</mn><mo>-</mo><mn>0</mn><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi>a</mi><mo>→</mo></mover><mo>·</mo><mfenced><mrow><mfenced><mrow><mover><mi>c</mi><mo>→</mo></mover><mo>×</mo><mover><mi>b</mi><mo>→</mo></mover></mrow></mfenced><mo>-</mo><mover><mi>b</mi><mo>→</mo></mover><mo>-</mo><mover><mi>c</mi><mo>→</mo></mover></mrow></mfenced><mo>=</mo><mn>24</mn></math></p>

</details>

---

### Q55. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let for a triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>C</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#947;</mi><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>C</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#948;</mi><mover><mi>k</mi><mo>^</mo></mover></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#948;</mi><mo>&#62;</mo><mn>0</mn></math> and the area of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msqrt><mn>6</mn></msqrt></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>C</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mrow><mi>C</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>54</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>108</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>A triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>C</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#947;</mi><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>C</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#948;</mi><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/62617018-39f8-46f5-93d4-a85a7d7ff523.png" style="width: 250px; height: 159px;" /></p><p>Now from triangle law of addition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>C</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mrow><mi>C</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#948;</mi><mover><mi>k</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#947;</mi><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>&#948;</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#947;</mi><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now on comparing both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#947;</mi><mo>=</mo><mi>&#948;</mi><mo>+</mo><mn>3</mn></math></p><p>Now area of triangle is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mrow><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>B</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msqrt><mn>6</mn></msqrt><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mi>&#947;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>5</mn><msqrt><mn>6</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>&#947;</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>6</mn><mo>+</mo><mn>2</mn><mi>&#947;</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>100</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msup><mi>&#947;</mi><mn>2</mn></msup><mo>=</mo><mn>320</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#947;</mi><mn>2</mn></msup><mo>=</mo><mn>64</mn><mo>&#8658;</mo><mi>&#947;</mi><mo>=</mo><mn>8</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#948;</mi><mo>=</mo><mn>8</mn><mo>-</mo><mn>3</mn><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>C</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mrow><mi>C</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#947;</mi><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#948;</mi><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>C</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mrow><mi>C</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>8</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>8</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>40</mn><mo>=</mo><mn>60</mn></math></p></blockquote>

</details>

---

### Q56. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>2</mn><mo>,</mo><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>3</mn></math> and the angle between the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>&#215;</mo><mo>(</mo><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>3</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo><msup><mo>|</mo><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>441</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>482</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>841</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>882</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>882</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>2</mn><mo>,</mo><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>3</mn></math> and the angle between the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>,</p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>&#215;</mo><mo>(</mo><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>3</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo><msup><mo>|</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>|</mo><mo>-</mo><mn>3</mn><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>+</mo><mn>4</mn><mo>(</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>)</mo><msup><mo>|</mo><mn>2</mn></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>|</mo><mn>7</mn><mo>(</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>)</mo><msup><mo>|</mo><mn>2</mn></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>as</mi><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mi>&#215;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mi>&#215;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>49</mn><mo>|</mo><mi>a</mi><msup><mo>|</mo><mn>2</mn></msup><mo>|</mo><mi>b</mi><msup><mo>|</mo><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>49</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>882</mn></math></p></blockquote>

</details>

---

### Q57. JEE Main 2023 (13 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>50</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mn>72</mn><mo>-</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo>.</mo></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **66**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>.</mo></math> </p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>50</mn><mo>,</mo></math></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>|</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt><mo>=</mo><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>&#183;</mo><msqrt><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></msqrt><mo>&#183;</mo><mi>sin</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>11</mn></msqrt><mo>=</mo><msqrt><mn>50</mn></msqrt><mo>&#183;</mo><msqrt><mn>22</mn></msqrt><mo>&#183;</mo><mi>sin</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><msqrt><mn>99</mn></msqrt><mn>10</mn></mfrac></math></p><p>Now solving,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mn>72</mn><mo>-</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mn>72</mn><mo>-</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mn>72</mn><mo>-</mo><mfenced><mrow><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mi>cos</mi><mi>&#952;</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mn>72</mn><mo>-</mo><mfenced><mrow><mn>50</mn><mo>+</mo><mn>22</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>5</mn><msqrt><mn>2</mn></msqrt><mo>.</mo><msqrt><mn>22</mn></msqrt><mfrac><msqrt><mn>99</mn></msqrt><mn>10</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mn>72</mn><mo>-</mo><mfenced close=""><mrow><mn>72</mn><mo>+</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>11</mn><mo>&#215;</mo><mn>3</mn></mrow><mn>10</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mn>66</mn></mfenced><mo>=</mo><mn>66</mn></math></p></blockquote>

</details>

---

### Q58. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="italic">c</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math>. If a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>d</mi><mo>&#8594;</mo></mover></math> satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>24</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mover><mi>d</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>323</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>423</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>313</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>413</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>413</mn></math>**

**Detailed Solution:**

<blockquote><p>We have been given that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#160;&#160;</mo><mo>(</mo><mo>&#8757;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>&#8800;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p>It is given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>24</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mo>+</mo><mi>&#955;</mi><mo>(</mo><mn>3</mn><mo>-</mo><mn>8</mn><mo>+</mo><mn>14</mn><mo>)</mo><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>&#955;</mi><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>8</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>18</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>64</mn><mo>+</mo><mn>25</mn><mo>+</mo><mn>324</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>413</mn></math></p><p>Hence, this is the correct option.</p></blockquote>

</details>

---

### Q59. JEE Main 2023 (12 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let the plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math> meet the co-ordinate axes at the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>C</mi></math>. If the orthocenter of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mfrac><mn>6</mn><mn>7</mn></mfrac></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>98</mn><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup></math> is equal to __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **288**

**Detailed Solution:**

<p>Given,</p><p>The plane <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mi>z</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math> meet the co-ordinate axes at the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>C</mi></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mo>-</mo><mn>6</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>B</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>C</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>And the orthocenter of the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mfrac><mn>6</mn><mn>7</mn></mfrac></mrow></mfenced></math>,</p><p>We know that, circumcentre of triangle is point of intersection of perpendicular bisectors,</p><p>So, plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b8dab166-7883-4d34-8fc8-2b183a0b4e7f.png" style="width: 300px; height: 264px;" /></p><p>Now from diagram we can see that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mtext>&#160;to&#160;midpoint&#160;of</mtext><mo>&#160;</mo><mi>B</mi><mi>C</mi><mo>&#160;</mo><mo>&#8869;</mo><mo>&#160;</mo><mi>B</mi><mi>C</mi></math></p><p>So, by perpendicular vector formula we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><mn>0</mn></mrow></mfenced><mo>&#215;</mo><mn>0</mn><mo>+</mo><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mn>2</mn><mo>+</mo><mfenced><mrow><mi>z</mi><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>6</mn><mi>z</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Similarly, for side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>0</mn></mrow></mfenced><mo>&#215;</mo><mn>0</mn><mo>+</mo><mfenced><mrow><mi>z</mi><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Similarly, for side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mn>2</mn><mo>+</mo><mfenced><mrow><mi>z</mi><mo>-</mo><mn>0</mn></mrow></mfenced><mo>&#215;</mo><mn>0</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>Now from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>3</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>9</mn></mrow><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>z</mi><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mi>z</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mi>z</mi></math></p><p>Now using the relation between centroid, circumcentre and orthocentre, we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3f2ad973-b2ad-4655-ad80-2f3d0c005b54.png" style="width: 450px; height: 134px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>G</mi><mo>=</mo><mfenced><mrow><mfrac><mrow><mi>&#945;</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>9</mn><mn>2</mn></mfrac></mstyle><mo>-</mo><mi>z</mi></mrow><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mi>&#946;</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>2</mn></mfrac></mstyle><mo>-</mo><mn>3</mn><mi>z</mi></mrow><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>6</mn><mn>7</mn></mfrac></mstyle><mo>+</mo><mn>2</mn><mi>z</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mfrac><mrow><mi>&#945;</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>9</mn><mn>2</mn></mfrac></mstyle><mo>-</mo><mi>z</mi></mrow><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mi>&#946;</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>2</mn></mfrac></mstyle><mo>-</mo><mn>3</mn><mi>z</mi></mrow><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>6</mn><mn>7</mn></mfrac><mo>+</mo><mn>2</mn><mi>z</mi></mstyle><mn>3</mn></mfrac></mrow></mfenced></math></p><p>Now on comparing both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mfrac><mn>15</mn><mn>14</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfrac><mn>9</mn><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>98</mn><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>98</mn><mo>&#215;</mo><mfrac><mn>144</mn><mn>49</mn></mfrac><mo>=</mo><mn>288</mn></math></p>

</details>

---

### Q60. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8484;</mi><mo>,</mo><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> be a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>17</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>20</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced><mrow><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>46</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>53</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>62</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>46</mn></math>**

**Detailed Solution:**

<p>Given that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>17</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>20</mn></math></p><p>Now, Take <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mfenced><mrow><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mo>-</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mfenced><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>0</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>17</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mfenced><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>17</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Similarly, on taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>20</mn></math>, we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mo>-</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>9</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>11</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>20</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>Now on solving equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>20</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><mi>&#955;</mi><mo>-</mo><mn>207</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mn>69</mn></mrow><mn>20</mn></mfrac></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>1</mn><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfenced><mrow><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mo>-</mo><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced><mrow><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced><mrow><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>46</mn></math></p><p>Hence this is the correct option.</p>

</details>

---

### Q61. JEE Main 2023 (11 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> is a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>11</mn><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>27</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **285**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math>,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math>,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>11</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>27</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><msqrt><mn>3</mn></msqrt><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced></math></p><p>Now finding, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>c</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>11</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>c</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>c</mi><mn>2</mn></msub><mo>+</mo><mn>3</mn><msub><mi>c</mi><mn>3</mn></msub><mo>=</mo><mn>11</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><msqrt><mn>3</mn></msqrt><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>c</mi><mn>1</mn></msub><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mo>-</mo><msub><mi>c</mi><mn>3</mn></msub><mo>=</mo><mo>-</mo><msqrt><mn>3</mn></msqrt><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>c</mi><mn>1</mn></msub><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mo>-</mo><msub><mi>c</mi><mn>3</mn></msub><mo>=</mo><mo>-</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>27</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mi>c</mi><mn>1</mn></msub><mo>-</mo><mn>4</mn><msub><mi>c</mi><mn>2</mn></msub><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mo>=</mo><mn>27</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math> </p><p>Now on solving equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>3</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>+</mo><mn>4</mn></mtd></mtr></mtable></mfenced><mn>2</mn></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mn>14</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><msup><mn>14</mn><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mn>8</mn><mn>2</mn></msup><mo>=</mo><mn>285</mn></math></p>

</details>

---

### Q62. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> be a non-zero vector parallel to the line of intersection of the two planes described by <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>,</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>,</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> is the angle between the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>6</mn></math>, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#952;</mi><mo>,</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>,</mo><mn>3</mn><msqrt><mn>6</mn></msqrt></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mn>3</mn><msqrt><mn>6</mn></msqrt></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>,</mo><mn>6</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mn>6</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mn>6</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> be a non-zero vector parallel to the line of intersection of the two planes described by <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>,</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math>, </p><p>So finding the normal vector to the above plane, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>n</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And normal vector to planes <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>,</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>n</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mfenced><mrow><msub><mover><mi>n</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#215;</mo><msub><mover><mi>n</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow></mfenced></math></p><p>So, direction ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Hence, direction ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Now given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mo>(</mo><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>6</mn><mo>=</mo><mi>&#955;</mi><mo>(</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now we know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>|</mo><mover><mi>a</mi><mo>&#175;</mo></mover><mo>|</mo><mo>|</mo><mi>b</mi><mo>|</mo><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>&#215;</mo><mn>3</mn><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>Now finding, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>=</mo><mn>6</mn></math></p><p>Hence, ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#952;</mi><mo>,</mo><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mn>6</mn></mrow></mfenced></math></p>

</details>

---

### Q63. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>^</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math>  Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>d</mi><mo>&#8594;</mo></mover></math> be a vector which is perpendicular to both <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>12</mn></math>. Then<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover></mrow></mfenced></math>  is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>44</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>42</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>44</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>^</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> </p><p>And  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>d</mi><mo>&#8594;</mo></mover></math> be a vector which is perpendicular to both <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p>Now finding, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>7</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>35</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>13</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>21</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mfenced><mrow><mn>35</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>13</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>21</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Also given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mi>&#955;</mi><mfenced><mrow><mn>35</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>13</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>21</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>(</mo><mn>35</mn><mo>+</mo><mn>13</mn><mo>-</mo><mn>42</mn><mo>)</mo><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>35</mn></mtd><mtd><mo>-</mo><mn>13</mn></mtd><mtd><mo>-</mo><mn>21</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mfenced><mrow><mn>47</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>91</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>22</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Now finding,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mfenced><mrow><mn>47</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>91</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>22</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>47</mn><mo>+</mo><mn>91</mn><mo>-</mo><mn>22</mn></mrow></mfenced><mo>=</mo><mn>44</mn></math></p></blockquote>

</details>

---

### Q64. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> be the origin and the position vector of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mi>k</mi></math>. If the position vectors of the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mi>k</mi><mo>,</mo><mo>&#160;</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mi>k</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>^</mo><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mi>k</mi></math> respectively, then the projection of the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover></math> on a vector perpendicular to the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> be the origin and the position vector of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Also given the position vectors of the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>^</mo><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> </p><p>Now finding, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><maction mathbackground="#94D8C8" actiontype="toggle"><mn>5</mn></maction><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><maction mathbackground="#94D8C8" actiontype="toggle"><mn>10</mn></maction><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><maction mathbackground="#94D8C8" actiontype="toggle"><mn>10</mn></maction><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now finding the Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover></math> on vector perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></math> we get,</p><p>Projection<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>5</mn><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><mrow><mn>5</mn><msqrt><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn></msqrt></mrow></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn></math></p></blockquote>

</details>

---

### Q65. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An arc <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> of a circle subtends a right angle at its centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math>. The mid point of the arc <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mrow><mi>O</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>v</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>v</mi><mo>&#8594;</mo></mover></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><msup><mi>&#946;</mi><mn>2</mn></msup></math>, are the roots of the equation

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>An arc <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> of a circle subtends a right angle at its centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math>. The mid point of the arc <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>,</p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mrow><mi>O</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>v</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>v</mi><mo>&#8594;</mo></mover></math>, </p><p>So, plotting the diagram of the given value we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fdf3f99a-e865-4e32-9646-6b70f544bfb5.png" style="width: 250px; height: 274px;" /></p><p>Now given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>v</mi><mo>&#8594;</mo></mover></math></p><p>Where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>R</mi><mo>&#160;</mo></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>v</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi><mo>&#160;</mo></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>u</mi><mo>&#8594;</mo></mover></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mrow><mi>O</mi><mi>P</mi><mo>&#160;</mo></mrow><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mfenced close="|" open="|"><mover><mrow><mi>O</mi><mi>Q</mi><mo>&#160;</mo></mrow><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mtext>radius</mtext></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> will lie on angle bisector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover></math></p><p>Now using the perpendicular condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><msup><mfenced close="|" open="|"><mover><mi>u</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mi>&#946;</mi><mo>&#183;</mo><mfenced><mrow><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>u</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><msup><mfenced close="|" open="|"><mover><mi>u</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mi>&#946;</mi><mo>&#183;</mo><mfenced><mrow><mfenced close="|" open="|"><mover><mi>v</mi><mo>&#8594;</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>u</mi><mo>&#8594;</mo></mover></mfenced><mi>cos</mi><msup><mn>45</mn><mo>&#176;</mo></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>&#183;</mo><mi>cos</mi><msup><mn>45</mn><mo>&#176;</mo></msup><mo>=</mo><mn>0</mn><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><mfenced close="|" open="|"><mover><mi>u</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mfenced close="|" open="|"><mover><mi>v</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mtext>radius</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>&#946;</mi></mrow><msqrt><mn>2</mn></msqrt></mfrac></math></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mrow><mi>O</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover></mfenced><mfenced close="|" open="|"><mover><mrow><mi>O</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover></mfenced><mi>cos</mi><msup><mn>45</mn><mo>&#176;</mo></msup><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><msup><mi>r</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#945;</mi><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>v</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mover><mi>v</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mfrac><msup><mi>r</mi><mn>2</mn></msup><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>&#183;</mo><mfrac><msup><mi>r</mi><mn>2</mn></msup><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mi>&#946;</mi><mo>&#183;</mo><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mfrac><msup><mi>r</mi><mn>2</mn></msup><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#945;</mi><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><msqrt><mn>2</mn></msqrt></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>&#946;</mi></mrow><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Now finding the equation with roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p></blockquote>

</details>

---

### Q66. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the quadrilateral <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math> with vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>5</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>C</mi><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>6</mn><mo>,</mo><mo>-</mo><mn>7</mn><mo>)</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msqrt><mn>38</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>54</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msqrt><mn>38</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msqrt><mn>38</mn></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The quadrilateral <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math> with vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>5</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>C</mi><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>6</mn><mo>,</mo><mo>-</mo><mn>7</mn><mo>)</mo></math></p><p>Now finding,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>7</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And plotting the diagram we get,
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4b91b2e8-1eba-44e0-85df-679807f90173-image.png" style="width: 350px; height: 197px;" />
Now we know that,</p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>D</mi></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>7</mn></mtd><mtd><mn>8</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>|</mo><mn>10</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>6</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover><mo>|</mo><mo>=</mo><mn>2</mn><msqrt><mn>38</mn></msqrt></math></p><p>Now finding, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>C</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>C</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover></math>
So, Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>C</mi><mi>B</mi><mi>D</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mo>-</mo><mn>12</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>|</mo><mn>6</mn><mo>(</mo><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>|</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><msqrt><mn>38</mn></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo></math> Area of quadrilateral <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi><mo>=</mo><mn>8</mn><msqrt><mn>38</mn></msqrt></math> square units</p></blockquote>

</details>

---

### Q67. JEE Main 2023 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>9</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>11</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> be vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>12</mn><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>5</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>9</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>11</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> be vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> are parallel vectors,</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>12</mn><mo>&#160;</mo><mo>=</mo><mfenced><mrow><mn>6</mn><mi>&#945;</mi><mo>+</mo><mn>75</mn></mrow></mfenced><mo>+</mo><mi>&#955;</mi><mfenced><mn>261</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>&#160;</mo><mo>+</mo><mn>87</mn><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>29</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mo>)</mo></math></p><p>Now again using <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>6</mn><mi>&#955;</mi></mrow></mfenced><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>(</mo><mn>11</mn><mo>+</mo><mn>9</mn><mi>&#955;</mi><mo>)</mo><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>(</mo><mo>-</mo><mn>2</mn><mo>+</mo><mn>12</mn><mi>&#955;</mi><mo>)</mo></math></p><p>Also given <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>6</mn><mi>&#955;</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mo>(</mo><mn>11</mn><mo>+</mo><mn>9</mn><mi>&#955;</mi><mo>)</mo><mo>+</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>+</mo><mn>12</mn><mi>&#955;</mi><mo>)</mo><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>29</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#945;</mi><mo>&#160;</mo><mo>+</mo><mn>87</mn><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>29</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>23</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>14</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mo>(</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>=</mo><mn>23</mn><mo>+</mo><mn>2</mn><mo>-</mo><mn>14</mn><mo>=</mo><mn>11</mn></math></p></blockquote>

</details>

---

### Q68. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>d</mi><mo>&#8594;</mo></mover></math> is a vector perpendicular to both <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="italic">b</mi><mo mathvariant="italic">&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="italic">a</mi><mo mathvariant="italic">&#8594;</mo></mover><mo mathvariant="italic">&#183;</mo><mover><mi mathvariant="italic">d</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mn>18</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>640</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>680</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>720</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>760</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>720</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>.</mo></math></p><p>Let us find <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mo>-</mo><mn>6</mn><mo>+</mo><mn>8</mn></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>4</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>d</mi><mo>&#8594;</mo></mover></math> is perpendicular to both <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mo>(</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>)</mo></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="italic">a</mi><mo mathvariant="italic">&#8594;</mo></mover><mo mathvariant="italic">&#183;</mo><mover><mi mathvariant="italic">d</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mfenced><mrow><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mo>(</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>)</mo><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>&#955;</mi><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn></math></p><p>Now let us apply LaGrange&#39;s identity which is as follows,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>&#183;</mo><mo>|</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>-</mo><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mn>2</mn></msup><msup><mfenced close="|" open="|"><mrow><mn>4</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mn>18</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>720</mn></math></p></blockquote>

</details>

---

### Q69. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>7</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>&#160;</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math>  be three given vectors. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">r</mi><mo>&#8594;</mo></mover></math> is a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi mathvariant="normal">r</mi><mo>&#8594;</mo></mover><mo>|</mo></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>7</mn></mfrac><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>7</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>5</mn></mfrac><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>914</mn></msqrt><mn>7</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>7</mn></mfrac><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p>Given data as below:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>7</mn><mover><mi mathvariant="italic">j</mi><mo mathvariant="italic">^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="italic">k</mi><mo mathvariant="italic">^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="italic">i</mi><mo mathvariant="italic">^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="italic">j</mi><mo mathvariant="italic">^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="italic">k</mi><mo mathvariant="italic">^</mo></mover></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo mathvariant="italic">&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p>It means <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>)</mo></math> is parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p>From equation (1),</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mo>+</mo><mi>&#955;</mi><mo>(</mo><mn>7</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mn>2</mn><mn>7</mn></mfrac></math></p><p>On putting values in equation (1) we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mfrac><mn>2</mn><mn>7</mn></mfrac><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><mo>(</mo><mn>11</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>11</mn><mover><mi>k</mi><mo mathvariant="italic">^</mo></mover><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mfrac><mrow><mn>11</mn><msqrt><mn>2</mn></msqrt></mrow><mn>7</mn></mfrac></math></p>

</details>

---

### Q70. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math> be two vectors. Then which one of the following statements is TRUE?

**Options:**

- **(A)** Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>13</mn></mrow><msqrt><mn>35</mn></msqrt></mfrac></math> and the direction of the projection vector is opposite to the direction of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math>
- **(B)** Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>17</mn></mrow><msqrt><mn>35</mn></msqrt></mfrac></math> and the direction of the projection vector is opposite to the direction of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math>
- **(C)** Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><msqrt><mn>35</mn></msqrt></mfrac></math> and the direction of the projection vector is opposite to the direction of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math>
- **(D)** Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><msqrt><mn>35</mn></msqrt></mfrac></math> and the direction of the projection vector is opposite to the direction of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>13</mn></mrow><msqrt><mn>35</mn></msqrt></mfrac></math> and the direction of the projection vector is opposite to the direction of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math>**

**Detailed Solution:**

<p>Given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>35</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>35</mn></msqrt></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>5</mn><mo>-</mo><mn>3</mn><mo>-</mo><mn>15</mn><mo>=</mo><mo>-</mo><mn>13</mn></math></p><p>Now finding the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> using the formula we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>13</mn><msqrt><mn>35</mn></msqrt></mfrac></math></p><p>And projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>13</mn><msqrt><mn>35</mn></msqrt></mfrac></math></p><p>Note- The original answer key was dropped by NTA in Jee mains 1st feb 2023, here we have modified the options.</p>

</details>

---

### Q71. JEE Main 2023 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mn>0</mn><mo>,</mo><mi>&#955;</mi></mrow></mfenced><mo>,</mo><mi>C</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mo>&#8804;</mo><mn>5</mn></math> are the vertices of a quadrilateral <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math>. If its area is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math> square units, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>-</mo><mn>6</mn><mi>&#955;</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mn>0</mn><mo>,</mo><mi>&#955;</mi></mrow></mfenced><mo>,</mo><mi>C</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mi>D</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Area of quadrilateral </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="|" close="|"><mrow><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>B</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>B</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mn>36</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>B</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>8</mn></mtd><mtd><mn>5</mn></mtd><mtd><mo>-</mo><mi>&#955;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>B</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>15</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mfenced><mrow><mn>0</mn><mo>+</mo><mn>24</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>0</mn><mo>+</mo><mn>24</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>B</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>15</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>24</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>24</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>B</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><msup><mfenced><mrow><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>15</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>24</mn></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>24</mn></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>225</mn><mo>+</mo><mn>90</mn><mi>&#955;</mi><mo>=</mo><mn>1296</mn><mo>-</mo><mn>1152</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>90</mn><mi>&#955;</mi><mo>-</mo><mn>81</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>10</mn><mi>&#955;</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>9</mn></math></p><p>Since,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mo>&#8804;</mo><mn>5</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>-</mo><mn>6</mn><mi>&#955;</mi><mo>=</mo><mn>5</mn><mo>-</mo><mn>6</mn><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>11</mn></math></p>

</details>

---

### Q72. JEE Main 2023 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> be three vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><mn>31</mn></msqrt><mo>,</mo><mn>4</mn><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>3</mn><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced></math>. If the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfrac></mfenced><mn>2</mn></msup></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><mn>31</mn></msqrt><mo>,</mo><mo>&#160;</mo><mn>4</mn><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>2</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>3</mn><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> and angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> is given as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>3</mn><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p>Means <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></math> are parallel vector,</p><p>So, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover></math></p><p>Now squaring both sides we get,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msup><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>12</mn><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><msup><mi>&#955;</mi><mn>2</mn></msup><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>36</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>12</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>2</mn><mfenced><mrow><mi>cos</mi><mfenced><mrow><mn>2</mn><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mfenced><mn>31</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mi>&#955;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>&#177;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now taking dot product with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> in above equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mo>&#177;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>&#177;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mo>&#177;</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p>Again taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> and sqauring both side,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac><msup><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac><mfenced close="]" open="["><mrow><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mn>31</mn><mn>4</mn></mfrac><mo>-</mo><mfenced><mn>1</mn></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac><mo>&#215;</mo><mfrac><mn>27</mn><mn>4</mn></mfrac><mo>=</mo><mn>3</mn></math></p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>3</mn><mn>1</mn></mfrac><mo>=</mo><mn>3</mn></math>.</p>

</details>

---

### Q73. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math>, be there(three) vector. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover></math> is a vector such that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><msup><mfenced close="|" open="|"><mover><mi>r</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>560</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>339</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>449</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>336</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>339</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p>Hence, we can say that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> is parallel to vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math>,</p><p>Now let , <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>8</mn></mrow><mn>5</mn></mfrac></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>-</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>17</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>7</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>25</mn><msup><mfenced close="|" open="|"><mover><mi>r</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mn>17</mn></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>7</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>25</mn><msup><mfenced close="|" open="|"><mover><mi>r</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>289</mn><mo>+</mo><mn>49</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>339</mn></math></p>

</details>

---

### Q74. JEE Main 2023 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> be two vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><mn>14</mn></msqrt><mo>,</mo><mo>&#160;</mo><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><mn>6</mn></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><msqrt><mn>48</mn></msqrt></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><mn>14</mn></msqrt><mo>,</mo><mo>&#160;</mo><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><mn>6</mn></msqrt><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><msqrt><mn>48</mn></msqrt></math></p><p>Now we know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>48</mn><mo>+</mo><msup><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>14</mn><mo>&#215;</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>84</mn><mo>-</mo><mn>48</mn><mo>=</mo><mn>36</mn></math>.</p>

</details>

---

### Q75. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> be two nonzero vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math>. Consider the following two statement:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced><mo>&#160;</mo><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#8805;</mo><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> are always parallel</p>

**Options:**

- **(A)** only (B) is correct
- **(B)** neither (A) nor (B) is correct
- **(C)** only (A) is correct
- **(D)** both (A) and (B) are correct.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) only (A) is correct**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p>Now squaring both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mfenced open="[" close="]"><mrow><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now here given <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math> which means <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></math> are perpendicular vector, so statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> is false,</p><p>Now statement<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced><mo>:</mo><mo>&#160;</mo><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#8805;</mo><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>&#8805;</mo><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mi>&#955;</mi><msup><mfenced open="|" close="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#8805;</mo><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><msup><mfenced open="|" close="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><msup><mfenced open="|" close="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#8805;</mo><mn>0</mn></math></p><p>This is not always true, since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi></math>.</p><p>Hence, we can say that statement<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> is true and statement <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> is false.</p>

</details>

---

### Q76. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>7</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>|</mo><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p>Also,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math>               (given)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfrac></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mfrac><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfrac><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced open="|" close="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mfenced><mfrac><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfrac></mfenced><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>74</mn><mo>-</mo><mfenced><mfrac><mn>15</mn><mn>3</mn></mfrac></mfenced><mo>&#215;</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>74</mn><mo>-</mo><mn>40</mn><mo>=</mo><mn>34</mn></math></p>

</details>

---

### Q77. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>6</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>x</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>y</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>z</mi><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mi>z</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mfenced><mrow><mi>y</mi><mo>+</mo><mi>z</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mi>z</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfenced><mrow><mi>y</mi><mo>+</mo><mi>z</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mi>z</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>1</mn><mspace linebreak="newline"></mspace><mi>x</mi><mo>+</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>1</mn><mspace linebreak="newline"></mspace><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>y</mi></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>;</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>6</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p>

</details>

---

### Q78. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> is rotated through a right angle, passing through the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis in its way and the resulting vector is <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math>. Then the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><msqrt><mn>2</mn></msqrt><mover><mi>b</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>6</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p>Given,</p><p>The vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> is rotated through a right angle, passing through the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis in its way and the resulting vector is <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p>Now taking, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced></math> {note here we have taken cross vector with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>j</mi><mo>^</mo></mover></math> as it is rotated along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo></math>axis}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Also magnitude of both vector will be equal,</p><p>So,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>&#8658;</mo><msqrt><mn>6</mn></msqrt><mo>=</mo><msqrt><mn>12</mn></msqrt><mo>&#160;</mo><mfenced close="|" open="|"><mi>&#955;</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>&#177;</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p>(Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math> rejected <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><mi mathvariant="italic">b</mi><mo mathvariant="italic">&#8594;</mo></mover></math> makes acute angle with y axis )</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><msqrt><mn>2</mn></msqrt><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Now projection of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><msqrt><mn>2</mn></msqrt><mover><mi>b</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mn>3</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><msqrt><mn>2</mn><mi>b</mi></msqrt></mrow></mfenced><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced></mfrac><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q79. JEE Main 2023 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>k</mi><mo>^</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mi>&#955;</mi><mover><mi>k</mi><mo>^</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>7</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mn>43</mn><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#8741;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math>, hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#956;</mi><mover><mi>c</mi><mo>&#8594;</mo></mover></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi></math> is any scalar.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mi>&#955;</mi><mover><mi>k</mi><mo>^</mo></mover><mo>=</mo><mi>&#956;</mi><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Taking dot product with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mo>+</mo><mn>14</mn><mo>+</mo><mn>2</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>=</mo><mn>7</mn><mi>&#956;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mi>&#956;</mi><mo>=</mo><mn>2</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Taking dot product with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"/><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>6</mn><mo>-</mo><mn>35</mn><mo>-</mo><mn>2</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mfrac><mn>43</mn><mn>2</mn></mfrac><mi>&#956;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>82</mn><mo>+</mo><mn>4</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>=</mo><mn>43</mn><mi>&#956;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>3</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi><mo>=</mo><mn>2</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mo>-</mo><mn>10</mn><mo>-</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q80. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#945;</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math>  and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></math> be parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#945;</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></math> be perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#945;</mi><mo>&#8594;</mo></mover></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>+</mo><msub><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>&#183;</mo><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#945;</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>+</mo><mover><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>since <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></math> is parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#945;</mi><mo>&#8594;</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mi>t</mi><mover><mi>&#945;</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mi>t</mi><mfenced><mrow><mn>4</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>4</mn><mi>t</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mi>t</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mi>t</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Substituting the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#945;</mi><mo>&#8594;</mo></mover></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>-</mo><mfenced><mrow><mn>4</mn><mi>t</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mi>t</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mi>t</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mn>4</mn><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mn>3</mn><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mo>-</mo><mn>4</mn><mo>-</mo><mn>5</mn><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>since <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#945;</mi><mo>&#8594;</mo></mover></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>&#945;</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mn>4</mn><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mn>3</mn><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mo>-</mo><mn>4</mn><mo>-</mo><mn>5</mn><mi>t</mi></mrow></mfenced><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>&#160;</mo></mrow></mfenced><mo>&#183;</mo><mfenced close="]" open="["><mrow><mn>4</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mn>4</mn><mi>t</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><mn>2</mn><mo>-</mo><mn>3</mn><mi>t</mi></mrow></mfenced><mo>+</mo><mn>5</mn><mfenced><mrow><mo>-</mo><mn>4</mn><mo>-</mo><mn>5</mn><mi>t</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mo>-</mo><mn>16</mn><mi>t</mi><mo>+</mo><mn>6</mn><mo>-</mo><mn>9</mn><mi>t</mi><mo>-</mo><mn>20</mn><mo>-</mo><mn>25</mn><mi>t</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>50</mn><mi>t</mi><mo>=</mo><mn>10</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math>, we get  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac><mfenced><mrow><mn>4</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mn>9</mn><mn>5</mn></mfrac><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>13</mn><mn>5</mn></mfrac><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mfenced><mrow><mn>9</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>13</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>15</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>So, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>&#183;</mo><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>(</mo><mn>9</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>13</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>15</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>)</mo><mo>&#183;</mo><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>9</mn><mo>+</mo><mn>13</mn><mo>-</mo><mn>15</mn><mo>=</mo><mn>7</mn></math></p>

</details>

---

### Q81. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mi>R</mi><mo>&#160;</mo></math>be a triangle. The points<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> are on the sides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mi>R</mi><mo>,</mo><mo>&#160;</mo><mi>R</mi><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> respectively such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>Q</mi><mi>A</mi></mrow><mrow><mi>A</mi><mi>R</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>R</mi><mi>B</mi></mrow><mrow><mi>B</mi><mi>P</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>P</mi><mi>C</mi></mrow><mrow><mi>C</mi><mi>Q</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>Area</mi><mfenced><mrow><mo>&#8710;</mo><mi>P</mi><mi>Q</mi><mi>R</mi></mrow></mfenced></mrow><mrow><mi>Area</mi><mfenced><mrow><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></mrow></mfenced></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Let the position vector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>O</mi><mo>&#8594;</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>q</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover></math>.</p><p>Now, position vector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>r</mi><mo>&#8594;</mo></mover></mrow><mn>3</mn></mfrac></math></p><p>Position vector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mover><mi>r</mi><mo>&#8594;</mo></mover></mrow><mn>3</mn></mfrac></math>.</p><p>Position vector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mover><mi>q</mi><mo>&#8594;</mo></mover><mn>3</mn></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>2</mn><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mo>-</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow><mn>3</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced close="]" open="["><mrow><mfenced><mrow><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>2</mn><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced close="]" open="["><mrow><mo>-</mo><mfenced><mrow><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>P</mi><mi>Q</mi><mi>R</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mrow><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mrow><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mrow><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>Area</mi><mo>&#160;</mo><mfenced><mrow><mo>&#8710;</mo><mi>P</mi><mi>Q</mi><mi>R</mi></mrow></mfenced></mrow><mrow><mi>Area</mi><mfenced><mrow><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q82. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>w</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>w</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>v</mi><mo>&#8594;</mo></mover></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>w</mi><mo>&#8594;</mo></mover></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>w</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Taking dot product with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>w</mi><mo>&#8594;</mo></mover></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>w</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>w</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mover><mi>w</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>w</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>v</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>w</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>w</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>v</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>w</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Taking dot product with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>w</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>v</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mn>6</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So, by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>w</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q83. JEE Main 2022 (29 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> be two vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>,</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>75</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn></math></p><p>We know that  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p>Now using the above formula in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p>Now on comparing both side we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>6</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Also given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>75</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>75</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>75</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>75</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>75</mn></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>6</mn></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>9</mn><mo>=</mo><mn>75</mn><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>14</mn></math></p></blockquote>

</details>

---

### Q84. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>^</mo></mover></math> be two unit vectors such that the angle between them is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> is the angle between the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>164</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>+</mo><mn>27</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>+</mo><mn>18</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>+</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>54</mn><mo>+</mo><mn>90</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>+</mo><mn>27</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>^</mo></mover></math> be two unit vectors such that the angle between them is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> is the angle between the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>164</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></math> is equal to</p><p>Now let angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>^</mo></mover><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mi>b</mi><mo>^</mo></mover><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>=</mo><mi>&#981;</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>^</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>^</mo></mover><mo>=</mo><mfenced close="|" open="|"><mover><mi>a</mi><mo>^</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>b</mi><mo>^</mo></mover></mfenced><mi>cos</mi><mi>&#981;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>^</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>^</mo></mover><mo>=</mo><mi>cos</mi><mi>&#981;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p>Now finding angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></mrow><mrow><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></mrow></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now finding the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>2</mn><mo>+</mo><mn>2</mn><mover><mi>a</mi><mo>^</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>^</mo></mover></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></math></p><p>Also value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover><mo>=</mo><mfenced close="|" open="|"><mover><mi>a</mi><mo>^</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>b</mi><mo>^</mo></mover></mfenced><mi>sin</mi><mi>&#981;</mi><mover><mi>n</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover><mo>=</mo><mfrac><mover><mi>n</mi><mo>^</mo></mover><msqrt><mn>2</mn></msqrt></mfrac></math>  when <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>n</mi><mo>^</mo></mover></math> is vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8869;</mo></math>to  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>^</mo></mover></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math> as perpendicular vector dot product is zero.</p><p>Now value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mfrac><mfenced><mn>4</mn></mfenced><mn>2</mn></mfrac><mo>+</mo><mn>4</mn><mover><mi>a</mi><mo>^</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>^</mo></mover><mo>+</mo><mn>8</mn><mover><mi>b</mi><mo>^</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>4</mn><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mo>+</mo><mfrac><mn>4</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>=</mo><mn>7</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p><p>Now finding dot product we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>^</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mover><mi>a</mi><mo>^</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>^</mo></mover><mo>+</mo><mn>0</mn><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>^</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>+</mo><mfrac><mn>3</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p>Now putting all the values in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mfrac><mn>3</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow><mrow><msqrt><mn>2</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></msqrt><msqrt><mn>7</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>9</mn><msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mn>2</mn><mfenced><mrow><mn>2</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mfenced><mrow><mn>7</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mfenced><mfrac><mn>9</mn><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced><mfrac><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>7</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>164</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mfenced><mn>82</mn></mfenced><mfenced><mn>9</mn></mfenced></mrow><msqrt><mn>2</mn></msqrt></mfrac><mfrac><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>7</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></mfrac><mfrac><mfenced><mrow><mn>7</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mfenced><mrow><mn>7</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>164</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mfrac><mfenced><mn>82</mn></mfenced><msqrt><mn>2</mn></msqrt></mfrac><mfrac><mrow><mfenced><mn>9</mn></mfenced><mfenced close="]" open="["><mrow><mn>7</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>4</mn><mo>+</mo><mn>7</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow><mfenced><mn>41</mn></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>164</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mfenced><mrow><mn>9</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mfenced close="]" open="["><mrow><mn>5</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>164</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>90</mn><mo>+</mo><mn>27</mn><msqrt><mn>2</mn></msqrt></math></p></blockquote>

</details>

---

### Q85. JEE Main 2022 (28 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>R</mi></math> for which the angle between the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>a</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>6</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mi>a</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mfenced><mrow><mi>b</mi><mo>&#62;</mo><mn>1</mn></mrow></mfenced></math> is acute. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#934;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>12</mn><mn>7</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#934;</mi></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>a</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>6</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mi>a</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math> </p><p>For angle to be acute <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>u</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>6</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mfenced><mrow><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mi>a</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>12</mn><mo>+</mo><mn>6</mn><mi>a</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8704;</mo><mi>b</mi><mo>&#62;</mo><mn>1</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>a</mi><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>12</mn><mo>+</mo><mn>6</mn><mi>a</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi></mrow></mfenced></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mi>b</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>t</mi><mo>&#62;</mo><mn>0</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>&#62;</mo><mn>1</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>a</mi><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>a</mi><mi>t</mi><mo>-</mo><mn>12</mn><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>t</mi><mo>&#62;</mo><mn>0</mn></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#62;</mo><mn>0</mn></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>D</mi><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>D</mi><mo>=</mo><mn>36</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>48</mn><mi>a</mi><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><mn>3</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#62;</mo><mn>0</mn></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>&#981;</mi></math></p></blockquote>

</details>

---

### Q86. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> has a magnitude <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>. Let a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> be such that for every <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mi>R</mi><mo>&#215;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced></mfenced></math>, the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>y</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> is perpendicular to the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>6</mn><mi>y</mi><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>18</mn><mi>x</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>81</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>9</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>y</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>6</mn><mi>y</mi><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>18</mn><mi>x</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mtext>as&#160;they&#160;are&#160;perpendicular</mtext></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>x</mi><mi>y</mi><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>18</mn><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mn>6</mn><msup><mi>y</mi><mn>2</mn></msup><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>-</mo><mn>18</mn><mi>x</mi><mi>y</mi><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>x</mi><mi>y</mi><mfenced><mrow><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>3</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>This should hold <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8704;</mo><mi mathvariant="normal">x</mi><mo>,</mo><mi>y</mi><mo>&#8712;</mo><mi>R</mi><mo>&#215;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>3</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>3</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mn>90</mn><mo>&#176;</mo></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>as&#160;</mtext><mi>&#952;</mi><mo>=</mo><msup><mn>90</mn><mo>&#176;</mo></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#183;</mo><mfrac><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mn>3</mn></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as&#160;</mtext><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mn>3</mn></mfrac></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfrac><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msqrt><mn>3</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>81</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>=</mo><mn>27</mn><msqrt><mn>3</mn></msqrt></math></p></blockquote>

</details>

---

### Q87. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math> be two vectors, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>9</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover></math>. Then the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>39</mn><mn>5</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>46</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>46</mn><mn>5</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>9</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>&#946;</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mo>+</mo><mn>5</mn><mi>&#946;</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>3</mn><mi>&#946;</mi><mo>-</mo><mn>4</mn><mi>&#945;</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mo>-</mo><mn>5</mn><mi>&#945;</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>9</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now on comparing side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mn>4</mn><mo>+</mo><mn>5</mn><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn><mi>&#946;</mi><mo>-</mo><mn>4</mn><mi>&#945;</mi><mo>=</mo><mn>9</mn><mo>,</mo><mo>-</mo><mn>5</mn><mi>&#945;</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;&#160;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So,<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>11</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#8201;</mo><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>50</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>9</mn><mo>+</mo><mfenced><mrow><mo>-</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mn>4</mn><mo>=</mo><mo>-</mo><mn>18</mn></math></p><p>Now projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> will be </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></mfrac><mo>=</mo><mfrac><mrow><mn>50</mn><mo>-</mo><mn>22</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>18</mn></mrow></mfenced></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>46</mn><mn>5</mn></mfrac></math></p></blockquote>

</details>

---

### Q88. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mi>&#945;</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn></math>. If the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> on the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mi>&#945;</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn></math>. If the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> on the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><msqrt><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mfenced><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mi>&#945;</mi><mo>+</mo><mn>2</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>4</mn></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></math></p><p>Now given length of projection is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>91</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>7</mn><mo>,</mo><mo>-</mo><mfrac><mn>13</mn><mn>2</mn></mfrac></math></p></blockquote>

</details>

---

### Q89. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> be a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn></math>. Then the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> on the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>21</mn></msqrt></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mfrac><mn>3</mn><mn>7</mn></mfrac></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><msqrt><mfrac><mn>7</mn><mn>3</mn></mfrac></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>21</mn></msqrt></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> , <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn></math></p><p>Now using the formula <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfenced><mrow><msup><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#183;</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#183;</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#183;</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#183;</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p>We get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mn>3</mn></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mn>2</mn></msup><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>5</mn><mo>+</mo><mn>9</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>14</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><msqrt><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced></msqrt><mo>=</mo><msqrt><mn>6</mn><mo>+</mo><mfrac><mn>7</mn><mn>3</mn></mfrac><mo>-</mo><mn>6</mn></msqrt><mo>=</mo><msqrt><mfrac><mn>7</mn><mn>3</mn></mfrac></msqrt></math></p><p>Now projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></mrow><mfenced close="|" open="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></mrow><msqrt><mfrac><mn>7</mn><mn>3</mn></mfrac></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>21</mn></msqrt></mfrac></math></p></blockquote>

</details>

---

### Q90. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> be a triangle such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>B</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="italic">a</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>,</mo><mover><mrow><mi>C</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="italic">c</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>,</mo><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>6</mn><msqrt><mn>2</mn></msqrt><mo>,</mo><mfenced close="|" open="|"><mover><mi>b</mi><mo mathvariant="italic">&#8594;</mo></mover></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi mathvariant="italic">c</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mn>12</mn></math> Consider the statements :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math>: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi mathvariant="italic">b</mi><mo mathvariant="italic">&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi mathvariant="italic">b</mi><mo mathvariant="italic">&#8594;</mo></mover></mrow></mfenced></mrow></mfenced><mo>-</mo><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>6</mn><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math>: <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8736;</mo><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mfrac><mn>2</mn><mn>3</mn></mfrac></msqrt></mfenced></math>. Then</p>

**Options:**

- **(A)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math>are true
- **(B)** only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> is true
- **(C)** only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is true
- **(D)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is true**

**Detailed Solution:**

<blockquote><p>We know that by triangle law of vector addition,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi mathvariant="italic">b</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>+</mo><mover><mi mathvariant="italic">c</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>a</mi><mo mathvariant="italic">&#8594;</mo></mover></math></p><p>Squaring both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p>Now putting the given value <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>6</mn><msqrt><mn>2</mn></msqrt><mo>,</mo><mo>&#160;</mo><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>12</mn></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>36</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>c</mi><mo mathvariant="italic">&#8594;</mo></mover></mfenced><mo>=</mo><mn>6</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mn>1</mn><mo>:</mo><mo>&#160;</mo><mfenced close="|" open="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>-</mo><mfenced close="|" open="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>-</mo><mfenced close="|" open="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>-</mo><mn>6</mn><mo>=</mo><mo>-</mo><mn>6</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mn>2</mn><mo>:</mo><mo>&#160;</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>c</mi><mo mathvariant="italic">&#8594;</mo></mover></math></p><p>Squaring both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mi>cos</mi><mfenced><mrow><mo>&#8736;</mo><mi>A</mi><mi>C</mi><mi>B</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>72</mn><mo>+</mo><mn>12</mn><mo>-</mo><mn>24</mn><msqrt><mn>6</mn></msqrt><mi>cos</mi><mfenced><mrow><mo>&#8736;</mo><mi>A</mi><mi>C</mi><mi>B</mi></mrow></mfenced><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mfenced><mrow><mo>&#8736;</mo><mi>A</mi><mi>C</mi><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>48</mn><mrow><mn>24</mn><msqrt><mn>6</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>6</mn></msqrt></mfrac><mo>=</mo><msqrt><mfrac><mn>2</mn><mn>3</mn></mfrac></msqrt></math></p></blockquote>

</details>

---

### Q91. JEE Main 2022 (29 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover accent="true"><mrow><mo>&#160;</mo><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> be a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mo>(</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **29**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover accent="true"><mrow><mo>&#160;</mo><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math>  </p><p>And  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mo>(</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover></math>,</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>x</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>y</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>z</mi><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mi>z</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mfenced><mrow><mn>3</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi></mrow></mfenced><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mfenced><mrow><mi>z</mi><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced></math></p><p>On comparing we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mo>-</mo><mn>5</mn></math> .....(i)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>-</mo><mn>3</mn><mi>x</mi><mo>=</mo><mn>2</mn></math> ............(ii)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> ........(iii)</p><p>On solving equation (i), (ii) and (iii) we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>6</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>8</mn></mrow><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>6</mn></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mrow><mo>-</mo><mn>8</mn></mrow><mn>3</mn></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>6</mn></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mrow><mo>-</mo><mn>8</mn></mrow><mn>3</mn></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mfrac><mn>29</mn><mn>3</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>29</mn></math></p><p>Note: This question appeared in JEE Main 2022, 29th june shift 2. The question was incorrect, so it is modified to make it correct.</p>

</details>

---

### Q92. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mi>&#946;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi>R</mi></math> be three vectors. If the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mn>3</mn></mfrac></math> and<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>10</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover></math> , then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mi>&#946;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi>R</mi></math> be three vectors.<p>Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced></mfrac><mo>=</mo><mfrac><mn>10</mn><mn>3</mn></mfrac></math> (given)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>&#945;</mi><mo>+</mo><mn>6</mn><mo>+</mo><mn>2</mn></mrow><msqrt><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>2</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mi>&#946;</mi></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#946;</mi><mo>-</mo><mn>8</mn><mo>=</mo><mo>-</mo><mn>6</mn><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q93. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> be a vector which is perpendicular to the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>13</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math>, then the projection of the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> on the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>13</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now multiplying both side by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>13</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>6</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>13</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>-</mo><mfenced><mrow><mn>6</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>13</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now, projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> on vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfrac><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q94. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#945;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mi mathvariant="bold-italic">R</mi></math>. If the area of the parallelogram whose adjacent sides are represented by the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>15</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced></msqrt></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>**

**Detailed Solution:**

<p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#945;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math>,</p><p>Area of parallelogram <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover><mo>=</mo><msqrt><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></msqrt></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><msqrt><mn>15</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced></msqrt></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mo>+</mo><msup><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>15</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>13</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>=</mo><mn>13</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>+</mo><mn>1</mn><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow><mo>|</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>|</mo></mrow><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>2</mn><msup><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mo>=</mo><mn>14</mn></math></p>

</details>

---

### Q95. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> be the vectors along the diagonal of a parallelogram having area <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>. Let the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> be acute. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>-</mo><mn>2</mn><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math>, then an angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/63bb97a07ef9050c849f20e5.png">

$\text { Area }=\frac{1}{2}|\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}|=2 \sqrt{2} \Rightarrow|\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}|=4 \sqrt{2}$
$|\overrightarrow{\mathrm{a}}|=1 \text { and }|\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{b}}|=|\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}|$
$\Rightarrow \cos \theta=\sin \theta$
$\Rightarrow \theta=\frac{\pi}{4}$
$\therefore|\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}|=4 \sqrt{2} \Rightarrow|\overrightarrow{\mathrm{a}}||\overrightarrow{\mathrm{b}}| \sin \frac{\pi}{4}=4 \sqrt{2}$
$\Rightarrow|\overrightarrow{\mathrm{b}}|=8$
$\text { Now, } \overrightarrow{\mathrm{c}}=2 \sqrt{2}(\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}})-2 \overrightarrow{\mathrm{b}}$
$|\overrightarrow{\mathrm{c}}|=\sqrt{(2 \sqrt{2})^2|\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}|^2+(2 \mid \overrightarrow{\mathrm{b}})^2}=16 \sqrt{2}$
$\text { Now, } \overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{c}}=-2|\overrightarrow{\mathrm{b}}|^2$
$\Rightarrow 8 \times 16 \sqrt{2} \times \cos \alpha=-2.64$
$\Rightarrow \cos \alpha=-\frac{1}{\sqrt{2}} \Rightarrow \alpha=\frac{3 \pi}{4}$

</details>

---

### Q96. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math>. Then the number of vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>10</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>i</mi><mo>+</mo><mi>j</mi><mo>-</mo><mi>k</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mi>i</mi><mo>-</mo><mn>3</mn><mi>j</mi><mo>+</mo><mn>2</mn><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>&#8230;</mo><mo>&#8230;</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> as well as <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> , so <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math> as they are perpendicular.</p><p>Now checking <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mo>-</mo><mn>3</mn><mo>-</mo><mn>2</mn><mo>=</mo><mo>-</mo><mn>3</mn><mo>&#8800;</mo><mn>0</mn></math></p><p>This <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> is not possible.</p><p>So, number of vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q97. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> be the three given vectors. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover></math> be a vector in the plane of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> whose projection on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>j</mi><mo>^</mo></mover><mo>=</mo><mn>7</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<p>Since vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> are coplanar then,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>&#955;</mi><mn>1</mn></msub><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mn>1</mn></msub><mo>,</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>&#955;</mi><mn>2</mn></msub></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mo>-</mo><mn>3</mn><msub><mi>&#955;</mi><mn>2</mn></msub></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#955;</mi><mn>2</mn></msub></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math> Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>&#955;</mi><mn>2</mn></msub><mo>-</mo><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>&#955;</mi><mn>2</mn></msub><mo>+</mo><mn>2</mn><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#955;</mi><mn>2</mn></msub></mrow><msqrt><mn>3</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>&#955;</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>j</mi><mo>^</mo></mover><mo>=</mo><mn>7</mn><mo>&#8658;</mo><msub><mi>&#955;</mi><mn>1</mn></msub><mo>-</mo><mn>3</mn><msub><mi>&#955;</mi><mn>2</mn></msub><mo>=</mo><mn>7</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>&#955;</mi><mn>2</mn></msub></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mo>-</mo><mn>3</mn><msub><mi>&#955;</mi><mn>2</mn></msub></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#955;</mi><mn>2</mn></msub></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>&#955;</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#955;</mi><mn>1</mn></msub><mo>-</mo><mn>3</mn><msub><mi>&#955;</mi><mn>2</mn></msub><mo>=</mo><mn>7</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>
From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn><mo>,</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>2</mn><mo>+</mo><mn>7</mn><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q98. JEE Main 2022 (25 Jun Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mi>&#955;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> is a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>13</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>21</mn><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>k</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mfenced><mrow><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>x</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>y</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>z</mi><mover><mi>k</mi><mo>^</mo></mover></math></p><p>So,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mi>z</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mfenced><mrow><mi>&#955;</mi><mi>y</mi><mo>-</mo><mi>z</mi></mrow></mfenced><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mfenced><mrow><mi>z</mi><mo>-</mo><mi>&#955;</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced></math></p><p>On comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>13</mn><mo>,</mo><mi>z</mi><mo>-</mo><mi>&#955;</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>&#955;</mi><mi>z</mi><mo>=</mo><mo>-</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> Clearly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mo>-</mo><mn>7</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>10</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mover accent="true"><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>k</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mfenced><mrow><mover accent="true"><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>11</mn><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>14</mn></math></p>

</details>

---

### Q99. JEE Main 2022 (25 Jun Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> be the angle between the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>4</mn><mo>,</mo><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></math> is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **576**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mrow><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced open="|" close="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#8722;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#8722;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mfenced close="]" open="["><mrow><msup><mfenced close="|" open="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>4</mn><msup><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>16</mn><mo>=</mo><mn>576</mn></math></p>

</details>

---

### Q100. JEE Main 2022 (25 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mi>i</mi></msub><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></math> be a vector which makes equal angles with the coordinate axes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>X</mi><mo>,</mo><mi>O</mi><mi>Y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>Z</mi></math>. Also, let the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> on the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> . Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> be a vector obtained by rotating <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>&#176;</mo></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis are coplanar, then projection of a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>7</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math></p>Since the vector makes equal angles with the coordinate axes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>X</mi><mo>,</mo><mi>O</mi><mi>Y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>Z</mi></math>, so<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="italic">a</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mfrac><mi>&#955;</mi><msqrt><mn>3</mn></msqrt></mfrac><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Now projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math>on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="italic">b</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#955;</mi><msqrt><mn>3</mn></msqrt></mfrac><mfrac><mrow><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced></mrow><mn>5</mn></mfrac><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>5</mn><msqrt><mn>3</mn></msqrt></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>5</mn><mfenced><mrow><mover><mover><mi>i</mi><mo>^</mo></mover><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>5</mn><mi>&#945;</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="bold-italic">k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>&#946;</mi><mfenced><mover><mi>i</mi><mo>^</mo></mover></mfenced></math></p><p>Since both vectors are perpendicular <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="italic">a</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>25</mn><mi>&#945;</mi><mfenced><mn>3</mn></mfenced><mo>+</mo><mn>5</mn><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>15</mn><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>15</mn><mi>&#945;</mi></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>5</mn><mi>&#945;</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>5</mn><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>&#177;</mo><mfrac><mn>5</mn><msqrt><mn>2</mn></msqrt></mfrac><mfenced><mrow><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="italic">b</mi><mo mathvariant="italic">&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced></mrow><mn>5</mn></mfrac><mo>=</mo><mo>&#177;</mo><mfrac><mn>5</mn><msqrt><mn>2</mn></msqrt></mfrac><mfenced><mfrac><mrow><mo>-</mo><mn>6</mn><mo>+</mo><mn>4</mn></mrow><mn>5</mn></mfrac></mfenced><mo>=</mo><mo>&#177;</mo><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q101. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> be two unit vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mi>a</mi><mo>&#215;</mo><mi>b</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>2</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math> is the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">b</mi><mo>^</mo></mover></math>, then among the statements:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced><mo>:</mo><mn>2</mn><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>-</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> : The projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>^</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

**Options:**

- **(A)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> is true.
- **(B)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is true.
- **(C)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are true.
- **(D)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are false.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are true.**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math></p><p>Squaring both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mfenced close="|" open="|"><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></mfenced><mn>2</mn></msup><mo>+</mo><mn>0</mn><mo>=</mo><mn>4</mn></math></p><p>Let the angle be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>^</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>^</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced close="|" open="|"><mover><mi>a</mi><mo>^</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>b</mi><mo>^</mo></mover></mfenced><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mn>4</mn><mfenced><mrow><mfenced close="|" open="|"><mover><mi>a</mi><mo>^</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>b</mi><mo>^</mo></mover></mfenced><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mi>&#952;</mi><mo>-</mo><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mi>t</mi></math> then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>t</mi><mo>+</mo><mi>t</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>t</mi><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>1</mn></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mn>1</mn></math> which is not possible as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="box"><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></menclose></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mfenced close="|" open="|"><mrow><mi>a</mi><mo>&#215;</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi>sin</mi><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>-</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><msqrt><mn>1</mn><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>cos</mi><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>2</mn><mo>-</mo><mn>2</mn><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> is correct.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>^</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>.</mo><mfenced><mrow><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover></mrow></mfenced></mrow><mrow><mo>&#8739;</mo><mover><mi>a</mi><mo>^</mo></mover><mo>+</mo><mover><mi>b</mi><mo>^</mo></mover><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced></mrow><msqrt><mn>2</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><msqrt><mn>1</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Which is true, So both are true.</p>

</details>

---

### Q102. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>^</mo></mover></math> be unit vectors. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></math> be a vector such that the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>^</mo></mover><mo>=</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mfenced><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>^</mo></mover></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mn>6</mn><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mfenced><mrow><mn>3</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mfenced><mrow><mn>3</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mfenced><mrow><mn>3</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>^</mo></mover><mo>=</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mfenced><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>^</mo></mover></mrow></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>^</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>^</mo></mover><mo>=</mo><mfenced><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mfenced><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mfenced><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>=</mo><mfenced><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mn>2</mn><mfenced><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>4</mn><mfenced><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>=</mo><msup><mfenced open="|" close="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>0</mn><mo>+</mo><mn>0</mn><mo>+</mo><msup><mfenced open="|" close="|"><mrow><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>^</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>&#160;</mo></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>=</mo><msup><mfenced open="|" close="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mfenced open="|" close="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>^</mo></mover></mfenced><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>=</mo><msup><mfenced open="|" close="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mfenced open="|" close="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>=</mo><msup><mfenced open="|" close="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>=</mo><msup><mfenced open="|" close="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mfenced open="[" close="]"><mrow><mn>3</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="|" close="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>36</mn><msup><mfenced open="|" close="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>3</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mn>6</mn></mfrac><mo>&#215;</mo><mn>36</mn><mo>=</mo><mn>6</mn><mfenced><mrow><mn>3</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math></p>

</details>

---

### Q103. JEE Main 2021 (01 Sep Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>.</mo></math> Let a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover></math> be in the plane containing <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover></math> is perpendicular to the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> and its projection on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math> units, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mn>2</mn><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1494**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> are coplanar</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#956;</mi><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>2</mn><mi mathvariant="normal">&#955;</mi><mo>+</mo><mi>&#956;</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mi>&#956;</mi><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p>given <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>&#8869;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mfenced><mrow><mn>2</mn><mi mathvariant="normal">&#955;</mi><mo>+</mo><mi>&#956;</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mi>&#956;</mi><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>.</mo><mo>(</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>=</mo><mn>0</mn><mspace linebreak="newline"></mspace></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>(</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>)</mo><mo>+</mo><mn>2</mn><mo>(</mo><mn>2</mn><mi>&#956;</mi><mo>-</mo><mi>&#955;</mi><mo>)</mo><mo>-</mo><mo>(</mo><mn>2</mn><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>4</mn><mi mathvariant="normal">&#956;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math></p><p>and also <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>^</mo></mover><mo>=</mo><mn>19</mn><mo>&#8658;</mo><mn>9</mn><mi mathvariant="normal">&#955;</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">&#956;</mi><mo>=</mo><mn>57</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>ii</mi><mo>)</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mover><mi mathvariant="normal">v</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>21</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>18</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>27</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mn>2</mn><mover><mi mathvariant="normal">v</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>441</mn><mo>+</mo><mn>324</mn><mo>+</mo><mn>729</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1494</mn></math></p>

</details>

---

### Q104. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> be two vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mn>2</mn><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mo>|</mo><mn>3</mn><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo></math> and the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>&#176;</mo><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> is a unit vector, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo></math> is equal to : </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p>Given that </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac><mover><mi>a</mi><mo>&#8594;</mo></mover></math> is a unit vector.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>8</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mn>2</mn><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mo>|</mo><mn>3</mn><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup></math></p><p>We know that<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#183;</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>&#160;</mo><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>&#160;</mo><mi>cos</mi><mo>&#160;</mo><mi>&#952;</mi><mo>&#160;</mo><mo>,</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mo>|</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>+</mo><mn>9</mn><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>+</mo><mn>12</mn><mo>|</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mi>cos</mi><mn>60</mn><mo>&#176;</mo><mo>=</mo><mn>9</mn><mo>|</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>+</mo><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>+</mo><mn>6</mn><mo>|</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mi>cos</mi><mn>60</mn><mo>&#176;</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mo>|</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>8</mn><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>+</mo><mn>6</mn><mo>|</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>|</mo><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#8739;</mo><mi>cos</mi><mn>60</mn><mo>&#176;</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mfenced><mn>64</mn></mfenced><mo>=</mo><mn>8</mn><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>+</mo><mn>6</mn><mfenced><mn>8</mn></mfenced><mo>&#183;</mo><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open=""><mrow><mo>&#8658;</mo><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>-</mo><mn>40</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced><mrow><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>+</mo><mn>8</mn></mrow></mfenced><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q105. JEE Main 2021 (27 Aug Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#945;</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> be three vectors such that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>5</mn><msqrt><mn>3</mn></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>.</mo></math> Then the greatest amongst the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup></math> is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **90**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>15</mn><mo>+</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>16</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Also, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>75</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>10</mn><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfenced><mo>&#183;</mo><mn>14</mn><mo>-</mo><msup><mfenced><mrow><mn>5</mn><mo>-</mo><mn>3</mn><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>75</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mn>30</mn><mi>&#946;</mi><mo>+</mo><mn>40</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow><mn>2</mn></msubsup><mo>=</mo><msub><mfenced><mrow><mn>26</mn><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfenced><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub><mo>=</mo><mn>90</mn></math></p>

</details>

---

### Q106. JEE Main 2021 (26 Aug Shift 2)

*Type:* `numerical` | *Level:* `1`

If the projection of the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> on the sum of the two vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Sum of two vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover><mo>+</mo><mo>(</mo><mo>-</mo><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>=</mo><mo>(</mo><mn>2</mn><mo>-</mo><mi>&#955;</mi><mo>)</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math>
Projection <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>=</mo><mfrac><mrow><mn>1</mn><mo>(</mo><mn>2</mn><mo>-</mo><mi>&#955;</mi><mo>)</mo><mo>+</mo><mn>2</mn><mo>(</mo><mn>6</mn><mo>)</mo><mo>+</mo><mn>1</mn><mo>&#215;</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>)</mo></mrow><msqrt><mo>(</mo><mn>2</mn><mo>-</mo><mi>&#955;</mi><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>12</mn><mo>-</mo><mi>&#955;</mi></mrow><msqrt><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>+</mo><mn>44</mn></msqrt></mfrac><mo>=</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>12</mn><mo>-</mo><mi>&#955;</mi><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>+</mo><mn>44</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>144</mn><mo>+</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>24</mn><mi>&#955;</mi><mo>=</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>+</mo><mn>44</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>100</mn><mo>=</mo><mn>20</mn><mi>&#955;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q107. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>A hall has a square floor of dimension <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#215;</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> (see the figure) and vertical walls. If the angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>P</mi><mi>H</mi></math> between the diagonals <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>G</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>H</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>,</mo></math> then the height of the hall (in meters) is:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/49ec7a08-0c7f-447c-9b56-f662ddafb3e8-image.png" style="width: 272px; height: 268px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msqrt><mn>10</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c8b4c7dc-c109-467b-a999-3305fc581d95-8220e67b-9820-4944-84b8-13cfe792bb7b-image.png" style="width: 440px; height: 375px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>AG</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>10</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi mathvariant="normal">h</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>10</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>BH</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>10</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi>h</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>10</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>100</mn><mo>+</mo><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><mn>100</mn></mrow><msup><mfenced><msqrt><mn>200</mn><mo>+</mo><msup><mi>h</mi><mn>2</mn></msup></msqrt></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>=</mo><mfrac><msup><mi>h</mi><mn>2</mn></msup><mrow><mn>200</mn><mo>+</mo><msup><mi>h</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn><mo>=</mo><mn>4</mn><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">h</mi></mrow><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">h</mi><mn>2</mn></msup><mo>=</mo><mn>50</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>h</mi><mo>=</mo><mn>5</mn><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q108. JEE Main 2021 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mi>&#945;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mi>&#945;</mi><mover><mi>k</mi><mo>^</mo></mover><mo>&#160;</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are integers. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>10</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mi>&#946;</mi><mo>,</mo><mo>-</mo><mi>&#945;</mi></mrow></mfenced></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mo>-</mo><mi>&#945;</mi><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>;</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#8658;</mo><mn>3</mn><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>3</mn><mi>&#945;</mi><mo>-</mo><mn>2</mn><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>From equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mfrac><mn>2</mn><mi>&#945;</mi></mfrac><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>+</mo><mn>5</mn><mi>&#945;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>&#945;</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>&#945;</mi><mo>+</mo><mi>&#945;</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math> is neglected since<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>&#945;</mi></math> is an integer.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mover><mi>b</mi><mo>&#8594;</mo></mover><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mfenced><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mn>3</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mo>-</mo><mn>6</mn><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>9</mn><mo>.</mo></math></p>

</details>

---

### Q109. JEE Main 2021 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> be three vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>1</mn><mo>.</mo></math> If the length of projection vector of the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> on the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>l</mi><mn>2</mn></msup></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><msqrt><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt></mfenced><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#8467;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mfenced open="|" close="|"><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfenced><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced></mfrac><mo>=</mo><mi>&#8467;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mfenced open="|" close="|"><mrow><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><msqrt><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn></msqrt></mfrac><mo>=</mo><mi>&#8467;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#8467;</mi><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>6</mn></msqrt></mfrac><mo>&#8658;</mo><msup><mi>&#8467;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>4</mn><mn>6</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>&#8467;</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q110. JEE Main 2021 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

If  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> are unit vectors and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>3</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>7</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>5</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>4</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>7</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>,</mo></math> then the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> (in degrees) is _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **60**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>3</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#8869;</mo><mfenced><mrow><mn>7</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>5</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>3</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>7</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>5</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>15</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>16</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>4</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>7</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>8</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>30</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mrow><mn>2</mn><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mn>60</mn><mo>&#176;</mo><mo>.</mo></math></p>

</details>

---

### Q111. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>8</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>5</mn></math> </p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>8</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mo>&#177;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mo>.</mo><mfenced><mrow><mo>&#177;</mo><mfrac><mn>3</mn><mn>5</mn></mfrac></mrow></mfenced><mo>=</mo><mo>&#177;</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>6</mn><mo>.</mo></math></p>

</details>

---

### Q112. JEE Main 2021 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> be two vectors. If a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mi>&#945;</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mi>&#947;</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math> is perpendicular to each of the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>)</mo></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><msqrt><mn>3</mn></msqrt></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>&#945;</mi><mo>|</mo><mo>+</mo><mo>|</mo><mi>&#946;</mi><mo>|</mo><mo>+</mo><mo>|</mo><mi>&#947;</mi><mo>|</mo></math> is equal to <u>            </u></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="italic">q</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>q</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mfenced><mrow><mn>0</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mfenced><mrow><mn>0</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mfenced><mrow><mn>3</mn><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>&#177;</mo><msqrt><mn>3</mn></msqrt><mfrac><mrow><mo>(</mo><mo>(</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>&#215;</mo><mo>(</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>)</mo></mrow><mrow><mo>|</mo><mo>(</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>&#215;</mo><mo>(</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>q</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>|</mo></mrow></mfrac><mo>=</mo><mo>&#177;</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>(</mo><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>)</mo></mrow><msqrt><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mo>&#177;</mo><mfenced><mrow><mo>-</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>According to question </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="italic">r</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mi>&#947;</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>&#945;</mi><mo>|</mo><mo>=</mo><mn>1</mn><mo>,</mo><mo>|</mo><mi>&#946;</mi><mo>|</mo><mo>=</mo><mn>1</mn><mo>,</mo><mo>|</mo><mi>&#947;</mi><mo>|</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>&#945;</mi><mo>|</mo><mo>+</mo><mo>|</mo><mi>&#946;</mi><mo>|</mo><mo>+</mo><mo>|</mo><mi>&#947;</mi><mo>|</mo><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q113. JEE Main 2021 (20 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover></math> is obtained by rotating the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><msqrt><mn>3</mn></msqrt><mi>p</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover></math> by an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> about origin in counter clockwise direction. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><mfenced><mrow><mi>&#945;</mi><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn></mrow></mfenced></mfrac></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><msqrt><mn>3</mn></msqrt><mi>p</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><mfenced><mrow><mi>&#945;</mi><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn></mrow></mfenced></mfrac></math></p><p> </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/45afb39f-27f9-4f49-872e-4ac88781aec1-image.png" style="width: 230px; height: 200px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mfenced><mo>=</mo><mfenced close="|" open="|"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>4</mn><mo>+</mo><mo>(</mo><mi>p</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mi>p</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></math> (rejected)</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><msub><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>&#183;</mo><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mrow><mrow><mfenced close="|" open="|"><msub><mover accent="true"><mi>v</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mfenced><mo>&#183;</mo><mfenced close="|" open="|"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mi>p</mi><mo>+</mo><mo>(</mo><mi>p</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><msqrt><mo>(</mo><mi>p</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>4</mn></msqrt><msqrt><mn>3</mn><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn></mrow><mrow><msqrt><mn>13</mn></msqrt><msqrt><mn>13</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn></mrow><mn>13</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><msqrt><mn>112</mn><mo>-</mo><mn>24</mn><msqrt><mn>3</mn></msqrt></msqrt><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><msqrt><msup><mfenced><mrow><mn>6</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>6</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>2</mn></mrow><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>&#945;</mi><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>2</mn></mrow><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q114. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mo>,</mo></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mrow><mi>B</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>3</mn><mo>,</mo><mo>|</mo><mover><mrow><mi>C</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mrow><mi>B</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>7</mn><mo>,</mo></math> then the projection of the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>B</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>B</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>We have,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/169a73ae-e3e6-42c7-a5bf-08aaa5d8ccf3-image.png" style="width: 299px; height: 200px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>3</mn><mo>,</mo><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>5</mn><mo>,</mo><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>7</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></mrow><mrow><mn>2</mn><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mfenced close="|" open="|"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>9</mn><mo>+</mo><mn>49</mn><mo>-</mo><mn>25</mn></mrow><mrow><mn>2</mn><mo>&#183;</mo><mn>3</mn><mo>&#183;</mo><mn>7</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>11</mn><mn>14</mn></mfrac></math></p><p>Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>|</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>|</mo><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mo>&#215;</mo><mfrac><mn>11</mn><mn>14</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>11</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q115. JEE Main 2021 (20 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> be three mutually perpendicular vectors of the same magnitude and equally inclined at an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math>, with the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p>Since, vectors are mutually perpendicular and of equally magnitude, hence let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>j</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi>i</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi>i</mi><mo>^</mo></mover><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>&#183;</mo><mn>1</mn><mo>&#183;</mo><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><mn>0</mn><mo>+</mo><mn>0</mn><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>&#183;</mo><mn>1</mn><mo>&#183;</mo><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>3</mn></msqrt><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>36</mn><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q116. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></math> is a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>|</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>,</mo><mo>|</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math> and the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>3</mn><mo>=</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced open="|" close="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mi>c</mi></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mfenced open="|" close="|"><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><mo>-</mo><mn>2</mn><mfenced><mi>c</mi></mfenced><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>c</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>c</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mfenced><mrow><mi>c</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>1</mn><mo>=</mo><mfenced open="|" close="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><msqrt><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt><mo>=</mo><mn>3</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mfenced open="|" close="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mi>sin</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>3</mn><mo>&#183;</mo><mn>1</mn><mo>&#183;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q117. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> be two non-zero vectors perpendicular to each other and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo></math>, If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo></math>, then the angle between the vectors
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>6</mn></msqrt></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>,</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>,</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#8869;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>&#8658;</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mi>sin</mi><mn>90</mn><mo>&#176;</mo><mo>=</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>&#8658;</mo><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>1</mn><mo>=</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math> are mutually perpendicular unit vectors.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>j</mi><mo>^</mo></mover><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mo>(</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mover><mi>i</mi><mo>^</mo></mover></mrow><mrow><msqrt><mn>3</mn></msqrt><msqrt><mn>1</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced></math></p>

</details>

---

### Q118. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mrow><mi>B</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>8</mn><mo>,</mo><mo>|</mo><mover><mrow><mi>C</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>7</mn><mo>,</mo><mo>|</mo><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>10</mn></math>, then the projection of the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>85</mn><mn>14</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>127</mn><mn>20</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>115</mn><mn>16</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>85</mn><mn>14</mn></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c7b9d899-bdbc-4049-b03a-15c7d5554619-image.png" style="width: 267px; height: 198px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>8</mn><mo>,</mo><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>7</mn><mo>,</mo><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>+</mo><mo>|</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>-</mo><mo>|</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup></mrow><mrow><mn>2</mn><mo>|</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>|</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>|</mo></mrow></mfrac><mo>=</mo><mfrac><mn>17</mn><mn>28</mn></mfrac></math></p><p>Projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>|</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>|</mo><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mo>&#215;</mo><mfrac><mn>17</mn><mn>28</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>85</mn><mn>14</mn></mfrac></math></p>

</details>

---

### Q119. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> has components <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>p</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> with respect to a rectangular cartesian system. This system is rotated through a certain angle about the origin in the counter clockwise sense. If, with respect to new system, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> has components <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>+</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>10</mn></msqrt><mo>,</mo></math> then a value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>5</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>5</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/388d8e15-a48c-446b-8be7-147d3e27551f-image.png" style="width: 365px; height: 300px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mi>Old</mi></msub><mo>=</mo><mn>3</mn><mi>p</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mi>New</mi></msub><mo>=</mo><mo>(</mo><mi>p</mi><mo>+</mo><mn>1</mn><mo>)</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msqrt><mn>10</mn></msqrt><mover><mi>j</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mi>Old</mi></msub></mfenced><mo>=</mo><mfenced close="|" open="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mi>New</mi></msub></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>p</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>10</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mi>p</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>4</mn><mi>p</mi><mo>-</mo><mn>5</mn><mo>)</mo><mo>(</mo><mi>p</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac><mo>,</mo><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q120. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> be the origin. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>x</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>y</mi><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mi>x</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><msqrt><mn>20</mn></msqrt></math> and the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi mathvariant="normal">z</mi><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>7</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> is coplanar with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<p>If two vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math> are perpendicular, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><msub><mi>b</mi><mn>2</mn></msub><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><msub><mi>c</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>.</mo></math><gwmw style="display:none;"></gwmw></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>&#8869;</mo><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>3</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>-</mo><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mi>y</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><mn>20</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><msup><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mo>-</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>20</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mi>y</mi><mo>-</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mn>1</mn><mo>+</mo><mn>3</mn><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>20</mn></math></p><p>Put the value from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo></math> to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mn>1</mn><mo>+</mo><mn>3</mn><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>14</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>14</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn><mo>,</mo></math> but given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mo>.</mo></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mrow><mi>O</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>,</mo><mover><mrow><mi>O</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover></math> are coplanar and we know that the three vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>3</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math> are coplanar, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd><mtd><msub><mi>b</mi><mn>3</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mi>z</mi></mtd><mtd><mo>-</mo><mn>7</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mi>z</mi></mtd><mtd><mo>-</mo><mn>7</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>(</mo><mo>-</mo><mn>14</mn><mo>-</mo><mn>3</mn><mi>z</mi><mo>)</mo><mo>-</mo><mn>2</mn><mo>(</mo><mn>7</mn><mo>-</mo><mn>9</mn><mo>)</mo><mo>-</mo><mn>1</mn><mo>(</mo><mo>-</mo><mi>z</mi><mo>-</mo><mn>6</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">z</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>9</mn><mo>.</mo></math></p>

</details>

---

### Q121. JEE Main 2021 (17 Mar Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#8594;</mo></mover></math> be a vector in the plane containing vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>.</mo></math> If the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#8594;</mo></mover></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo></math> and its projection on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>17</mn><msqrt><mn>6</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mover><mi>x</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **486**

**Detailed Solution:**

<blockquote><p>A plane containing two vectors can be expressed as a linear combination of the vectors.</p><p>Hence, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#956;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>(</mo><mi>&#955;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi></math> are scalars<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>(</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>)</mo><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>(</mo><mn>2</mn><mi>&#956;</mi><mo>-</mo><mi>&#955;</mi><mo>)</mo><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>(</mo><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>)</mo></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#8594;</mo></mover></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>(</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>)</mo><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>(</mo><mn>2</mn><mi>&#956;</mi><mo>-</mo><mi>&#955;</mi><mo>)</mo><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>(</mo><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>)</mo></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>(</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>)</mo><mo>+</mo><mn>2</mn><mo>(</mo><mn>2</mn><mi>&#956;</mi><mo>-</mo><mi>&#955;</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>8</mn><mi>&#956;</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Also, the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>x</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>17</mn><msqrt><mn>6</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow><mrow><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>17</mn><msqrt><mn>6</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>(</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>)</mo><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>(</mo><mn>2</mn><mi>&#956;</mi><mo>-</mo><mi>&#955;</mi><mo>)</mo><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>(</mo><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>)</mo></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><msqrt><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><mfrac><mrow><mn>17</mn><msqrt><mn>6</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mo>(</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>)</mo><mo>-</mo><mo>(</mo><mn>2</mn><mi>&#956;</mi><mo>-</mo><mi>&#955;</mi><mo>)</mo><mo>+</mo><mo>(</mo><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>)</mo></mrow><msqrt><mn>6</mn></msqrt></mfrac><mo>=</mo><mfrac><mrow><mn>17</mn><msqrt><mn>6</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>=</mo><mn>51</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>On solving the equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo><mo>,</mo></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>.</mo></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>13</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>14</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>11</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mover><mi>x</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><msup><mn>13</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>14</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mn>11</mn><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mover><mi>x</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>486</mn><mo>.</mo></math></p></blockquote>

</details>

---

### Q122. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>7</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mo>(</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mo>(</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mfenced><mrow><mo>-</mo><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>10</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mfenced><mrow><mo>-</mo><mn>5</mn><mo>-</mo><mn>8</mn><mo>+</mo><mn>10</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>1</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>5</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>10</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>10</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>10</mn><mo>=</mo><mn>12</mn></math></p>

</details>

---

### Q123. JEE Main 2021 (16 Mar Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> be a vector perpendicular to the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mo>(</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>=</mo><mn>8</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mo>(</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo></math> is equal to</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **28**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mo>(</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>=</mo><mi>&#955;</mi><mo>(</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>&#183;</mo><mo>(</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo><mn>8</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>=</mo><mn>28</mn></math></p>

</details>

---

### Q124. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mi>&#945;</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mo>(</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mi>&#945;</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>)</mo><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> then the value of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mo>|</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#8658;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>&#955;</mi><mo>&#8594;</mo></mover><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#8658;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>&#955;</mi><mo>&#8594;</mo></mover><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>&#955;</mi><mo>&#8594;</mo></mover><mfenced><mrow><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mo>(</mo><mi>&#945;</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>)</mo><mo>=</mo><mn>3</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#955;</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mrow><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mi>&#945;</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>r</mi><mo>&#8594;</mo></mover></math> from (1)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#955;</mi><mi>&#945;</mi><mo>-</mo><mi>&#955;</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>Solve <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#955;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>14</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mo>|</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>15</mn></math></p>

</details>

---

### Q125. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#945;</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi mathvariant="normal">&#946;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></math> be obtained by rotating the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></math> by an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>&#176;</mo></math> about the origin in counterclockwise direction in the first quadrant. Then the area (in sq. units) of triangle having vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#946;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c45890e2-aea4-4f64-8690-7d0eb66017a9-image.png" style="width: 282px; height: 186px;" /></p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi><mfenced><mrow><msup><mi>OA</mi><mo>&#39;</mo></msup><mi mathvariant="normal">B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>OA</mi><mo>&#39;</mo></msup><mi>cos</mi><mn>15</mn><mo>&#176;</mo><mo>&#215;</mo><msup><mi>OA</mi><mo>&#39;</mo></msup><mi>sin</mi><mn>15</mn><mo>&#176;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mfenced><msup><mi>OA</mi><mo>&#39;</mo></msup></mfenced><mn>2</mn></msup><mfrac><mrow><mi>sin</mi><mn>30</mn><mo>&#176;</mo></mrow><mn>2</mn></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>O</mi><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>O</mi><msup><mi>A</mi><mo>&#39;</mo></msup></mrow></mfenced></math>, since rotation will not change the magnitude.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> sq. units</p>

</details>

---

### Q126. JEE Main 2021 (25 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi>&#945;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mi>&#945;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math>. If the area of the parallelogram whose adjacent sides are represented by the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msqrt><mn>3</mn></msqrt></math> square units, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is equal to ___ .<gwmw style="display:none;"></gwmw>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi>&#945;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mi>&#945;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p>area of parallelogram <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>8</mn><msqrt><mn>3</mn></msqrt></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mfenced><mrow><mn>4</mn><mi>&#945;</mi></mrow></mfenced><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mn>8</mn></mrow></mfenced><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mn>4</mn><mi>&#945;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><msqrt><mn>64</mn><mo>+</mo><mn>32</mn><msup><mi>&#945;</mi><mn>2</mn></msup></msqrt><mo>=</mo><mn>8</mn><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>6</mn><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q127. JEE Main 2021 (25 Feb Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="italic">a</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="italic">j</mi><mo mathvariant="italic">^</mo></mover><mo>-</mo><mover><mi mathvariant="italic">k</mi><mo mathvariant="italic">^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi mathvariant="italic">b</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="italic">i</mi><mo mathvariant="italic">^</mo></mover><mo>-</mo><mover><mi mathvariant="italic">j</mi><mo mathvariant="italic">^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="italic">i</mi><mo mathvariant="italic">^</mo></mover><mo>-</mo><mover><mi mathvariant="italic">j</mi><mo mathvariant="italic">^</mo></mover><mo>-</mo><mover><mi mathvariant="italic">k</mi><mo mathvariant="italic">^</mo></mover></math> be three given vectors. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="italic">r</mi><mo mathvariant="italic">&#8594;</mo></mover></math> is a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="italic">r</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>&#215;</mo><mover><mi mathvariant="italic">a</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="italic">c</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>&#215;</mo><mover><mi mathvariant="italic">a</mi><mo mathvariant="italic">&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="italic">r</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover></math></p><p>taking dot product with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><msup><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>12</mn></math></p>

</details>

---

### Q128. JEE Main 2020 (06 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">x</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">y</mi><mo>&#8594;</mo></mover></math> be two non-zero vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mover><mi mathvariant="normal">x</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">y</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mover><mi>x</mi><mo>&#8594;</mo></mover></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mover><mi mathvariant="normal">x</mi><mo>&#8594;</mo></mover><mo>+</mo><mi mathvariant="normal">&#955;</mi><mover><mi mathvariant="normal">y</mi><mo>&#8594;</mo></mover></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>y</mi><mo>&#8594;</mo></mover></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#955;</mi></math> is ...... .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>y</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>x</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mfenced close="|" open="|"><mover><mi>y</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>y</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math> .....(1)</p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>y</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>.</mo><mover><mi>y</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn><mi>s</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#955;</mi><msup><mfenced close="|" open="|"><mover><mi>y</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>y</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math>  .....(2)</p><p>by (1) and (2) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q129. JEE Main 2020 (06 Sep Shift 1)

*Type:* `numerical` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover></math> are unit vectors, then the greatest value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>+</mo><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>|</mo></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Let angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi></math>.
So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>+</mo><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><msqrt><mn>3</mn></msqrt><msqrt><mn>2</mn><mo>+</mo><mn>2</mn><mi>cos&#945;</mi></msqrt><mo>+</mo><msqrt><mn>2</mn><mo>-</mo><mn>2</mn><mi>cos&#945;</mi></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>3</mn></msqrt><msqrt><mn>2</mn><mo>&#215;</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mfrac><mi>&#945;</mi><mn>2</mn></mfrac></msqrt><mo>+</mo><msqrt><mn>2</mn><mo>&#215;</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mfrac><mi>&#945;</mi><mn>2</mn></mfrac></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><msqrt><mn>3</mn></msqrt><mfenced close="|" open="|"><mrow><mi>cos</mi><mfrac><mi>&#945;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>sin</mi><mfrac><mi>&#945;</mi><mn>2</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mi mathvariant="normal">&#960;</mi></mrow></mfenced><mo>&#8658;</mo><mfrac><mi>&#945;</mi><mn>2</mn></mfrac><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p>So, given expression is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><msqrt><mn>3</mn></msqrt><mi>cos</mi><mfrac><mi>&#945;</mi><mn>2</mn></mfrac><mo>+</mo><mi>sin</mi><mfrac><mi>&#945;</mi><mn>2</mn></mfrac></mrow></mfenced></math>
Thus, maximum value is<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msqrt><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q130. JEE Main 2020 (05 Sep Shift 2)

*Type:* `numerical` | *Level:* `1`

Let the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>2</mn><mo>,</mo><mo>|</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>4</mn><mo>.</mo></math> If the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover></math> is equal to the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>|</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8230;</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover></mrow></mfenced><msup><mrow/><mn>2</mn></msup><mo>=</mo><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>+</mo><mo>|</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>+</mo><mo>|</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>2</mn><mo>(</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>0</mn><mo>-</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>)</mo><mo>=</mo><mn>36</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>=</mo><mn>6</mn></math>

</details>

---

### Q131. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#8712;</mo><mi>R</mi></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mi>b</mi><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mi>c</mi><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></math>,where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>9</mn></mfrac></math>, then the angle between the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>b</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>a</mi><mover><mi>k</mi><mo>^</mo></mover></math> is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>9</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mi>b</mi><mi>cos</mi><mo>&#160;</mo><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mi>c</mi><mi>cos</mi><mo>&#160;</mo><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mi>k</mi><mrow><mi>cos</mi><mi>&#952;</mi></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mfrac><mi>k</mi><mrow><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mfrac><mi>k</mi><mrow><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>a</mi><mo>=</mo><msup><mi>k</mi><mn>2</mn></msup><mfrac><mrow><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced><mo>+</mo><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced></mrow><mrow><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced><mi>cos</mi><mi>&#952;</mi><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>k</mi><mn>2</mn></msup><mfenced close="]" open="["><mfrac><mrow><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mfenced><mrow><mi mathvariant="normal">&#952;</mi><mo>+</mo><mi mathvariant="normal">&#960;</mi></mrow></mfenced><mo>.</mo><mi>cos</mi><mfenced><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></mstyle></mfenced></mrow><mrow><mi>cos</mi><mi>&#952;</mi><mo>.</mo><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced><mo>.</mo><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>k</mi><mn>2</mn></msup><mfenced close="]" open="["><mfrac><mrow><mi>cos</mi><mi>&#952;</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mi>&#952;</mi><mo>.</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mrow><mrow><mi>cos</mi><mi>&#952;</mi><mo>.</mo><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced><mo>.</mo><mi>cos</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi></math> be the angle between two given vectors.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>cos</mi><mi>&#981;</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mi>a</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>b</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>.</mo><mfenced><mrow><mi>b</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>a</mi><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><mrow><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>&#160;</mo></msqrt><mo>&#183;</mo><msqrt><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>&#160;</mo></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>a</mi></mrow><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#981;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p>

</details>

---

### Q132. JEE Main 2020 (02 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the position vectors of points &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>&#39; and &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>&#39; be <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo></math> respectively. A point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#39;</mo><mi>P</mi><mo>&#39;</mo></math> divides the line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> internally in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>:</mo><mn>1</mn><mfenced><mrow><mi>&#955;</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">O</mi></math> is the origin and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>OB</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>OP</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>3</mn><msup><mfenced close="|" open="|"><mrow><mover><mi>OA</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>OP</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>6</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.8**

**Detailed Solution:**

<p>Position vector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>O</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow><mrow><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;&#160;</mo><mover><mi>OB</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>OP</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>3</mn><mo>|</mo><mover><mi>OA</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>OP</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mfenced><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow><mrow><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>-</mo><mn>3</mn><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow><mrow><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>6</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mo>|</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup></mrow><mrow><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn><msup><mi>&#955;</mi><mn>2</mn></msup></mrow><mrow><mo>(</mo><mi>&#955;</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mrow><mn>6</mn><mo>+</mo><mi>&#955;</mi><mo>.</mo><mn>14</mn></mrow><mrow><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn><msup><mi>&#955;</mi><mn>2</mn></msup></mrow><mrow><mo>(</mo><mi>&#955;</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><mo>&#183;</mo><mn>6</mn><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mrow><mn>18</mn><msup><mi>&#955;</mi><mn>2</mn></msup></mrow><mrow><mo>(</mo><mi>&#955;</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mn>6</mn><mo>=</mo><mn>6</mn><mo>+</mo><mfrac><mrow><mn>8</mn><mi>&#955;</mi></mrow><mrow><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>18</mn><msup><mfenced><mfrac><mi>&#955;</mi><mrow><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mfrac><mrow><mn>8</mn><mi>&#955;</mi></mrow><mrow><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mi>&#955;</mi><mrow><mi>&#955;</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#8800;</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>10</mn><mi>&#955;</mi><mo>=</mo><mn>8</mn><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>&#955;</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>8</mn></math></p>

</details>

---

### Q133. JEE Main 2020 (02 Sep Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> be three unit vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>8</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msup><mfenced close="|" open="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q134. JEE Main 2020 (09 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>,</mo><mi></mi><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math> and <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover></math> be three vectors such that <math><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>,</mo><mi></mi><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>5</mn><mo>,</mo><mi></mi><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>&#8729;</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>10</mn></math> and the angle between <math><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math> and <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover></math> is <math><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>.</mo></math> If <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></math> is perpendicular to the vector <math><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>,</mo></math> then <math><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfenced></math> is equal to ____________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>10</mn><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mfenced close="|" open="|" separators="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mi>cos</mi><mo>&#8289;</mo><mrow><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mn>10</mn><mo>&#8658;</mo><mn>5</mn><mo>.</mo><mfenced close="|" open="|" separators="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mo>.</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mn>10</mn></mrow></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>4</mn></math></p><p>Also, <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>.</mo><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mi></mi><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced separators="|"><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced open="|" close="|" separators="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mfenced open="|" close="|" separators="|"><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mi>sin</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>3</mn></msqrt><mo>&#215;</mo><mfenced open="|" close="|" separators="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mfenced open="|" close="|" separators="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mi>sin</mi><mo>&#8289;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>&#215;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>3</mn></msqrt><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>=</mo><mn>30</mn></math></p>

</details>

---

### Q135. JEE Main 2020 (09 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

If the vectors, <math><mover accent="true"><mrow><mi>p</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>a</mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>a</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>,</mo><mi></mi><mover accent="true"><mrow><mi>q</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>a</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>a</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> and <math><mover accent="true"><mrow><mi>r</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>a</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>a</mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mi></mi><mfenced separators="|"><mrow><mi>a</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced></math> are coplanar and <math><mn>3</mn><msup><mrow><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>p</mi></mrow><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mrow><mi>q</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>&#955;</mi><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>r</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>q</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math> , then the value of <math><mi>&#955;</mi></math> is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>a</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>a</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mi>a</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mi>a</mi></mtd><mtd><mi>a</mi><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn><mi></mi><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi>a</mi><mo>+</mo><mi>a</mi><mo>=</mo><mn>0</mn><mi></mi><mo>&#8658;</mo><mi></mi><mi></mi><mi>a</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>  
<math><mover accent="true"><mrow><mi>P</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>  
<math><mover accent="true"><mrow><mi>Q</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced separators="|"><mrow><mo>-</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>  
<math><mover accent="true"><mrow><mi>R</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi></mi><mfenced separators="|"><mrow><mo>-</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>  
<math><mover accent="true"><mrow><mi>P</mi></mrow><mo>→</mo></mover><mo>.</mo><mover accent="true"><mrow><mi>Q</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mi></mi><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>2</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi></mi></math>  
<math><mover accent="true"><mrow><mi>R</mi></mrow><mo>→</mo></mover><mo>×</mo><mover accent="true"><mrow><mi>Q</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mi></mi><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>i</mi></mtd><mtd><mi>j</mi></mtd><mtd><mi>k</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mfenced separators="|"><mrow><mi>i</mi><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>j</mi><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>k</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>3</mn><mi>i</mi><mo>+</mo><mn>3</mn><mi>j</mi><mo>+</mo><mn>3</mn><mi>k</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>i</mi><mo>+</mo><mi>j</mi><mo>+</mo><mi>k</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>  
<math><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>R</mi></mrow><mo>→</mo></mover><mo>×</mo><mover accent="true"><mrow><mi>Q</mi></mrow><mo>→</mo></mover></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msqrt><mn>3</mn></msqrt><mi></mi><mo>&#8658;</mo><mi></mi><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>R</mi></mrow><mo>→</mo></mover><mo>×</mo><mover accent="true"><mrow><mi>Q</mi></mrow><mo>→</mo></mover></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math> <math><mn>3</mn><msup><mrow><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>P</mi></mrow><mo>→</mo></mover><mo>.</mo><mi></mi><mover accent="true"><mrow><mi>Q</mi></mrow><mo>→</mo></mover></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>λ</mi><mi></mi><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>R</mi></mrow><mo>→</mo></mover><mo>×</mo><mover accent="true"><mrow><mi>Q</mi></mrow><mo>→</mo></mover></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math>  
<math><mn>3</mn><mi></mi><mo>.</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>-</mo><mi>λ</mi><mi></mi><mo>.</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mn>0</mn><mi></mi><mo>&#8658;</mo><mi>λ</mi><mo>=</mo><mn>1</mn></math>

</details>

---

### Q136. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover accent="true"><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover accent="true"><mi>k</mi><mo>^</mo></mover></math>, be two vectors. If <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover></math>, is a vector such that <math><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></math> and <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn><mo>,</mo><mi></mi></math> then <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math>, is equal to.

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced separators="|"><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced separators="|"><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfenced separators="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mfenced separators="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math></p><p>Using given information <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover accent="true"><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover accent="true"><mi>k</mi><mo>^</mo></mover></math> , we can write <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>6</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>4</mn><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>6</mn><mfenced separators="|"><mrow><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover accent="true"><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>-</mo><mn>4</mn><mfenced separators="|"><mrow><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover accent="true"><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>4</mn><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover accent="true"><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>.</p>

</details>

---

### Q137. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>,</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math> and <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover></math>, be three unit vectors such that <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mn>0</mn></mrow><mo>&#8594;</mo></mover></math>. If <math><mi>&#955;</mi><mo>=</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mtext>d</mtext><mo>&#8594;</mo></mover><mo>=</mo><mover><mtext>a</mtext><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mtext>b</mtext><mo>&#8594;</mo></mover><mo>+</mo><mover><mtext>b</mtext><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mtext>c</mtext><mo>&#8594;</mo></mover><mo>+</mo><mover><mtext>c</mtext><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mtext>a</mtext><mo>&#8594;</mo></mover></math>, then the order pair, <math><mfenced separators="|"><mrow><mi>&#955;</mi><mo>,</mo><mover accent="true"><mrow><mi>d</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></math>, is equal to.

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>3</mn><mover accent="true"><mrow><mi>a</mi></mrow><mo>→</mo></mover><mo>×</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>→</mo></mover></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>3</mn><mover accent="true"><mrow><mtext>c</mtext></mrow><mo mathvariant="normal">→</mo></mover><mo>×</mo><mover accent="true"><mrow><mtext>b</mtext></mrow><mo mathvariant="normal">→</mo></mover></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>3</mn><mover accent="true"><mrow><mi>b</mi></mrow><mo>→</mo></mover><mo>×</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>→</mo></mover></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>3</mn><mover accent="true"><mrow><mtext>a</mtext></mrow><mo mathvariant="normal">→</mo></mover><mo>×</mo><mover accent="true"><mrow><mtext>b</mtext></mrow><mo mathvariant="normal">→</mo></mover></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mn>3</mn><mover accent="true"><mrow><mtext>a</mtext></mrow><mo mathvariant="normal">→</mo></mover><mo>×</mo><mover accent="true"><mrow><mtext>b</mtext></mrow><mo mathvariant="normal">→</mo></mover></mrow></mfenced></math>**

**Detailed Solution:**

<math><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mn>2</mn><mfenced separators="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced separators="|"><mrow><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></math>
<math><mo>=</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math>
<math><mover accent="true"><mrow><mi>d</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></math>.

</details>

---

### Q138. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> and <math><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> be two vectors. If a vector perpendicular to both the vectors <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math> and <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mi>&#160;</mi></math> has the magnitude <math><mn>12</mn></math> then one such vector is:

**Options:**

- **(A)** <math><mn>4</mn><mo>(</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>)</mo></math>
- **(B)** <math><mn>4</mn><mo>(</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>)</mo></math>
- **(C)** <math><mn>4</mn><mo>(</mo><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>)</mo></math>
- **(D)** <math><mn>4</mn><mo>(</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>4</mn><mo>(</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>)</mo></math>**

**Detailed Solution:**

<math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>,</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>i</mi><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
<math><mo>&#8757;</mo><mtext>&#8201;</mtext><mover accent="true"><mrow><mi>&#945;</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></math>
<math><mtext>&#8201;</mtext><mover accent="true"><mrow><mi>&#946;</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
<math><mo>&#8756;</mo><mtext>&#8201;</mtext><mover accent="true"><mrow><mi>&#945;</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>&#946;</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mfenced separators="|"><mrow><mn>16</mn></mrow></mfenced><mo>-</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mfenced separators="|"><mrow><mn>16</mn></mrow></mfenced><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mfenced separators="|"><mrow><mo>-</mo><mn>8</mn></mrow></mfenced><mo>=</mo><mn>16</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>16</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
<math><mo>&#8756;</mo></math> Unit vector perpendicular to <math><mtext>&#8201;</mtext><mover accent="true"><mrow><mi>&#945;</mi></mrow><mo>&#8594;</mo></mover><mo>&#38;</mo><mtext>&#8201;</mtext><mover accent="true"><mrow><mi>&#946;</mi></mrow><mo>&#8594;</mo></mover></math> is
<math><mover accent="true"><mrow><mi>n</mi></mrow><mo>^</mo></mover><mo>=</mo><mfrac><mrow><mover accent="true"><mrow><mi>&#945;</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>&#946;</mi></mrow><mo>&#8594;</mo></mover></mrow><mrow><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>&#945;</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>&#946;</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mo>&#8756;</mo></math> Required vector <math><mo>=</mo><mn>12</mn><mfrac><mrow><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mn>4</mn><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>

</details>

---

### Q139. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The distance of the point having position vector <math><mo>-</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> from the straight line passing through the point <math><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi mathvariant="normal">&#160;</mi><mn>3</mn><mo>,</mo><mi mathvariant="normal">&#160;</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math> and parallel to the vector, <math><mn>6</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> is

**Options:**

- **(A)** <math><mn>4</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math><mn>6</mn></math>
- **(C)** <math><mn>2</mn><msqrt><mn>13</mn></msqrt></math>
- **(D)** <math><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>7</mn></math>**

**Detailed Solution:**

<p>Let, the given point be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8801;</mo><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8801;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>4</mn></mrow></mfenced><mo>,</mo></math> hence the position vector of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fc2571d9-cfc2-4112-9c5e-307c00cd1f6c-image.png" style="width: 491px; height: 310px;" /></p><p>We know that the vector joining two points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>1</mn></msub></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><msub><mi>z</mi><mn>2</mn></msub><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo></math></p><p>Hence, the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>6</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>A</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>10</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi></math> is the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover></math> on the given line i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>We know that the projection of a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> on a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="|" open="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi><mo>=</mo><mfrac><mfenced close="|" open="|"><mrow><mover accent="true"><mrow><mi>A</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><mi>n</mi><mo>&#8594;</mo></mover></mrow></mfenced><mfenced close="|" open="|" separators="|"><mover accent="true"><mi>n</mi><mo>&#8594;</mo></mover></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mi>D</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mo>-</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>10</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><msqrt><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mi>D</mi><mo>=</mo><mfrac><mfenced close="|" open="|"><mrow><mo>-</mo><mn>18</mn><mo>-</mo><mn>3</mn><mo>-</mo><mn>40</mn></mrow></mfenced><msqrt><mn>36</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>16</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mi>D</mi><mo>=</mo><msqrt><mn>61</mn></msqrt></math> units</p><p>The distance between the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>1</mn></msub></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>-</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></msqrt></math></p><p>Thus, <math><mi>A</mi><mi>P</mi><mo>=</mo><msqrt><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mn>6</mn><mo>+</mo><mn>4</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>=</mo><msqrt><mn>110</mn></msqrt></math> units</p><p>Now, in triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi><mi>P</mi><mo>,</mo></math> by Pythagoras theorem, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mi>P</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>P</mi><mi>D</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>A</mi><mi>D</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mi>D</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mi>A</mi><mi>P</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><mi>A</mi><mi>D</mi></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>110</mn><mo>-</mo><mn>61</mn></msqrt><mo>=</mo><mn>7</mn></math> units.</p>

</details>

---

### Q140. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mi mathvariant="normal">&#160;</mi><mi>B</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> be the vertices of a triangle and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> be the mid-point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math> divides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>M</mi></math> in the ratio, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>1</mn></math> , then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfenced><mrow><mi mathvariant="normal">&#8736;</mi><mi>G</mi><mi>O</mi><mi>A</mi></mrow></mfenced></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> being the origin) is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>30</mn></msqrt></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn><msqrt><mn>10</mn></msqrt></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>15</mn></msqrt></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>15</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>15</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/26479c85-ea6a-4a23-9363-002fbc78b6c2-image.png" style="width: 309px; height: 239px;" />
<math><mo>&#8757;</mo><mi>&#160;</mi><mi>&#160;</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is mid point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>G</mi></math> divides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>M</mi></math> in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>1</mn></math> internally</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>G</mi></math> is centroid of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>G</mi><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>0</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>10</mn></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>6</mn></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mover accent="true"><mrow><mi>O</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover accent="true"><mi>i</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>0</mn><mover accent="true"><mi>j</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>k</mi><mo>&#8594;</mo></mover><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><mover accent="true"><mrow><mi>O</mi><mi>G</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover accent="true"><mi>i</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mi>j</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mi>k</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>cos</mi><mi>&#8736;</mi><mi>G</mi><mi>O</mi><mi>A</mi><mo>=</mo><mfrac><mrow><mover accent="true"><mrow><mi>O</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mrow><mi>O</mi><mi>G</mi></mrow><mo>&#8594;</mo></mover></mrow><mrow><mfenced close="|" open="|" separators="|"><mover accent="true"><mrow><mi>O</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover></mfenced><mfenced close="|" open="|" separators="|"><mover accent="true"><mrow><mi>O</mi><mi>G</mi></mrow><mo>&#8594;</mo></mover></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>6</mn><mo>-</mo><mn>2</mn></mrow><mrow><msqrt><mn>10</mn></msqrt><msqrt><mn>24</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mrow><msqrt><mn>10</mn></msqrt><mi>&#160;</mi><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow></mfrac></math></p><p><math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>15</mn></msqrt></mrow></mfrac></math></p>

</details>

---

### Q141. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If a unit vector <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></math> makes angles <math><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>i</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math> with <math><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math> with <math><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>,</mo></math> then a value of <math><mi>&#952;</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>5</mn><mi>π</mi></mrow><mrow><mn>12</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>The unit vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> makes angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>i</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>j</mi><mo>^</mo></mover><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mover><mi>k</mi><mo>^</mo></mover></math> respectively.</p><p>Hence, the direction cosines of the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#945;</mi><mo>=</mo><mi>cos</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>cos</mi><mi>&#946;</mi><mo>=</mo><mi>cos</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#947;</mi><mo>=</mo><mi>cos</mi><mi>&#952;</mi></math></p><p>For a line having direction cosines as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>cos</mi><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>cos</mi><mi>&#947;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mn>2</mn></msup><mi>&#945;</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mn>2</mn></msup><mi>&#946;</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mn>2</mn></msup><mi>&#947;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mo>&#177;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q142. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mover><mrow><mi>&#945;</mi></mrow><mrow><mo>&#8594;</mo></mrow></mover><mo>=</mo><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>-</mo><mover><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover></math> is parallel to <math><mover><mrow><mi>&#945;</mi></mrow><mrow><mo>&#8594;</mo></mrow></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#945;</mi><mo>&#8594;</mo></mover><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>(</mo><mo>-</mo><mn>3</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>9</mn><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover><mo>)</mo></math>
- **(B)** <math><mi mathvariant="normal"> </mi><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>9</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
- **(C)** <math><mo>-</mo><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>9</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><mn>3</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>9</mn><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>(</mo><mo>-</mo><mn>3</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>9</mn><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover><mo>)</mo></math>**

**Detailed Solution:**

<p>If two vectors are parallel then they are proportional.</p><p>So, let <math><mover accent="true"><mrow><msub><mrow><mi>&#946;</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>k</mi><mover accent="true"><mrow><mi>&#945;</mi></mrow><mo>&#8594;</mo></mover></math></p><p>Given <math><mover accent="true"><mrow><mi>&#946;</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><msub><mrow><mi>&#946;</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mrow><msub><mrow><mi>&#946;</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover accent="true"><mi>&#945;</mi><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><mi>&#946;</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>&#945;</mi><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>&#945;</mi><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#945;</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>&#946;</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>5</mn></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>&#945;</mi><mo>&#8594;</mo></mover></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>,</mo></math> hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>&#945;</mi><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>&#945;</mi><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>&#945;</mi><mo>&#8594;</mo></mover><mo>&#8901;</mo><mfenced><mrow><mi>k</mi><mover accent="true"><mi>&#945;</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mi>k</mi><msup><mfenced><mover accent="true"><mi>&#945;</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mi>k</mi><msup><mfenced close="|" open="|"><mover accent="true"><mi>&#945;</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover><mi>&#945;</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>10</mn></msqrt></math></p><p>Put, all these values in the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo></math> to get <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>=</mo><mi>k</mi><mo>&#215;</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math><mo>&#8756;</mo><mtext>&#8201;</mtext><mover accent="true"><mrow><msub><mrow><mi>&#946;</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>(</mo><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>)</mo></math></p><p><math><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>&#946;</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mover accent="true"><msub><mi>&#946;</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><msub><mi>&#946;</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mover accent="true"><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover accent="true"><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover accent="true"><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mover accent="true"><mi>i</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced><mo>-</mo><mover accent="true"><mi>j</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mover accent="true"><mi>k</mi><mo>^</mo></mover><mfenced><mrow><mfrac><mn>9</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mover accent="true"><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>(</mo><mo>-</mo><mn>3</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>9</mn><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover><mo>)</mo><mo>.</mo></math></p>

</details>

---

### Q143. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>x</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mi>&#160;</mi></math> and <math><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>,</mo></math> for some real <math><mi>x</mi></math>. Then the condition for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mi>&#160;</mi></mrow></mfenced><mo>=</mo><mi>r</mi><mi mathvariant="normal">&#160;</mi></math>to follow

**Options:**

- **(A)** <math><mn>0</mn><mo>&lt;</mo><mi>r</mi><mo>≤</mo><mi> </mi><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>
- **(B)** <math><mi>r</mi><mo>≥</mo><mi> </mi><mn>5</mn><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>
- **(C)** <math><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt><mo>&lt;</mo><mi>r</mi><mo>≤</mo><mn>3</mn><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>
- **(D)** <math><mn>3</mn><mi mathvariant="normal"> </mi><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt><mo>&lt;</mo><mi mathvariant="normal">r</mi><mo>&lt;</mo><mn>5</mn><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>r</mi><mo>≥</mo><mi> </mi><mn>5</mn><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<p>As, We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover></math></p><p><math><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><msqrt><mn>4</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>9</mn><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>25</mn></msqrt></math></p><p><math><mo>=</mo><msqrt><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>38</mn></msqrt></math></p><p>Therefore, we have
<math><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#8805;</mo><msqrt><mfrac><mrow><mn>75</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math></p><p><math><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#8805;</mo><mn>5</mn><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math></p>

</details>

---

### Q144. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The magnitude of the projection of the vector <math><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> on the vector perpendicular to the plane containing the vectors <math><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> and <math><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>,</mo></math> is:

**Options:**

- **(A)** <math><mi> </mi><mn>3</mn><msqrt><mn>6</mn></msqrt></math>
- **(B)** <math><mi mathvariant="normal"> </mi><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>
- **(C)** <math><msqrt><mn>6</mn></msqrt></math>
- **(D)** <math><mi mathvariant="normal"> </mi><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi mathvariant="normal"> </mi><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<p>Vector perpendicular to <math><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> and <math><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math></p><p><math><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math></p><p><math><mo>&#8756;</mo></math> Required projection</p><p><math><mo>=</mo><mfrac><mrow><mo>|</mo><mo>(</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>)</mo><mo>&#8901;</mo><mtext>&#8201;</mtext><mo>(</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>)</mo><mo>|</mo></mrow><mrow><mo>|</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>|</mo></mrow></mfrac></math></p><p><math><mo>=</mo><mfrac><mrow><mo>|</mo><mn>2</mn><mo>-</mo><mn>6</mn><mo>+</mo><mn>1</mn><mo>|</mo></mrow><mrow><msqrt><mn>6</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><msqrt><mn>6</mn></msqrt></mrow></mfrac><mo>=</mo><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math></p>

</details>

---

### Q145. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\sqrt{3} \hat{i}+\hat{j}, \hat{i}+\sqrt{3} \hat{j}$ and $\beta \hat{i}+(1-\beta) \hat{j}$ respectively be the

position vectors of the points $\mathrm{A}, \mathrm{B}$ and $\mathrm{C}$ with respect to the origin $\mathrm{O}$. If the distance of $\mathrm{C}$ from the bisector of the

acute angle between $\mathrm{OA}$ and $\mathrm{OB}$ is $\frac{3}{\sqrt{2}},$ then the sum of

all possible values of $\beta$ is:

**Options:**

- **(A)** 4
- **(B)** 3
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

Since, the angle bisector of acute angle between $O A$

and $O B$ would be $y=x$

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/HfNimb0QWKAItrxDgDc5lVqtwo3UfnpsmqIovw-oZ3Q.original.fullsize.png">


Since, the distance of $C$ from bisector $=\frac{3}{\sqrt{2}}$

$\Rightarrow\left|\frac{\beta-(1-\beta)}{\sqrt{2}}\right|=\frac{3}{\sqrt{2}}=2 \beta=\pm 3+1$

$\beta=2$ or $\beta=-1$

Hence, the sum of all possible value of $\beta=2+(-1)=1$

</details>

---

### Q146. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a point on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>&#956;</mi></mrow></mfenced><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mi>&#956;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mn>5</mn><mi>&#956;</mi></mrow></mfenced><mover accent="true"><mi>k</mi><mo>^</mo></mover></math> and <math><mi>B</mi><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>6</mn></mrow></mfenced></math> be a point in the space. Then the value of <math><mi>&#956;</mi></math> for which the vector <math><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></math> is parallel to the plane <math><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>1</mn></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let <math><mi>A</mi></math> is <math><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>&#956;</mi><mo>,</mo><mi>&#160;</mi><mi>&#956;</mi><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>+</mo><mn>5</mn><mi>&#956;</mi></mrow></mfenced></math></p><p>We know that the vector joining two points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>1</mn></msub></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><msub><mi>z</mi><mn>2</mn></msub><mo>-</mo><msub><mi>z</mi><mn>1</mn></msub></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mn>3</mn><mi>&#956;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mn>5</mn><mi>&#956;</mi></mrow></mfenced><mover accent="true"><mi>k</mi><mo>^</mo></mover></math> which is parallel to plane <math><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mfenced separators="|"><mrow><mn>3</mn><mi>&#956;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>4</mn><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mn>5</mn><mi>&#956;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>&#956;</mi><mo>+</mo><mn>2</mn><mo>-</mo><mn>12</mn><mo>+</mo><mn>4</mn><mi>&#956;</mi><mo>+</mo><mn>12</mn><mo>-</mo><mn>15</mn><mi>&#956;</mi><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mo>-</mo><mn>8</mn><mi>&#956;</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q147. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>&#955;</mi><mn>1</mn></msub><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover><mo>,</mo><mi>&#160;</mi><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><msub><mi>&#955;</mi><mn>2</mn></msub></mrow></mfenced><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><msub><mi>&#955;</mi><mn>3</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mover accent="true"><mi>k</mi><mo>^</mo></mover></math> be three vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></math> and <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></math> is perpendicular to <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>.</mo></math> Then a possible value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mo>,</mo><msub><mrow><mi>&#160;</mi><mi>&#955;</mi></mrow><mn>2</mn></msub><mo>,</mo><mi>&#160;</mi><msub><mi>&#955;</mi><mn>3</mn></msub></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>0</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mn>4</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>0</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo></math> so <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><msub><mi>&#955;</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn><mo>-</mo><mn>2</mn><msub><mi>&#955;</mi><mn>1</mn></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>We know that if two vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math> are perpendicular, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub><msub><mi>b</mi><mn>2</mn></msub><mo>+</mo><msub><mi>c</mi><mn>1</mn></msub><msub><mi>c</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math></p><p>Since, <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></math> is perpendicular to <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover></math> so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>+</mo><mn>6</mn><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><mfenced separators="|"><mrow><msub><mi>&#955;</mi><mn>3</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mo>+</mo><mn>6</mn><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>&#955;</mi><mn>3</mn></msub><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#955;</mi><mn>3</mn></msub><mo>=</mo><mo>-</mo><mn>1</mn><mo>-</mo><mn>2</mn><msub><mi>&#955;</mi><mn>1</mn></msub><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>From equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mo>,</mo><mi>&#160;</mi><msub><mi>&#955;</mi><mn>2</mn></msub><mo>,</mo><mi>&#160;</mi><msub><mi>&#955;</mi><mn>3</mn></msub></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mo>,</mo><mi>&#160;</mi><mn>3</mn><mo>-</mo><mn>2</mn><msub><mi>&#955;</mi><mn>1</mn></msub><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>1</mn><mo>-</mo><mn>2</mn><msub><mi>&#955;</mi><mn>1</mn></msub></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mn>1</mn></msub><mo>&#8712;</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>0</mn></mrow></mfenced></math> satisfies the above triplet.</p>

</details>

---

### Q148. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><msqrt><mn>2</mn></msqrt><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>b</mi><mn>1</mn></msub><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><msqrt><mn>2</mn></msqrt><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>5</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><msqrt><mn>2</mn></msqrt><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> be three vectors such that the projection vector of <math><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math> on <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced></math> . If <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math> is perpendicular to <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover></math> , then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced></math> is equal to:

**Options:**

- **(A)** <math><msqrt><mn>22</mn></msqrt></math>
- **(B)** <math><msqrt><mn>32</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

<blockquote><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover></math>, hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>5</mn><msub><mi>b</mi><mn>1</mn></msub><mo>+</mo><msubsup><mi>b</mi><mn>2</mn><mi>&#160;</mi></msubsup><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msub><mi>b</mi><mn>1</mn></msub><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mn>10</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math> </p><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mrow><mfenced open="|" close="|" separators="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced></mfrac><mo>=</mo><mfenced open="|" close="|" separators="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo>&#8757;</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>r</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi>s</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mi>t</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>&#8658;</mo><mfenced open="|" close="|"><mover><mi>p</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><msup><mi>s</mi><mn>2</mn></msup><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>b</mi><mn>1</mn></msub><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mo>+</mo><mn>2</mn><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>b</mi><mn>1</mn></msub><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math> </p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><msub><mi>b</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced close="|" open="|" separators="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><mn>9</mn><mo>+</mo><mn>25</mn><mo>+</mo><mn>2</mn></msqrt><mo>=</mo><mn>6</mn></math></p></blockquote>

</details>

---

### Q149. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math> and a vector <math><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced></math> equals

**Options:**

- **(A)** <math><mfrac><mrow><mn>11</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>11</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(C)** <math><msqrt><mfrac><mrow><mn>11</mn></mrow><mrow><mn>3</mn></mrow></mfrac></msqrt></math>
- **(D)** <math><mfrac><mrow><msqrt><mn>11</mn></msqrt></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msqrt><mfrac><mrow><mn>11</mn></mrow><mrow><mn>3</mn></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mfenced separators="|"><mrow><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>-</mo><mfenced separators="|"><mrow><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mtable><mtr></mtr><mtr></mtr><mtr></mtr></mtable></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mi mathvariant="normal">&#160;</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced separators="|"><mrow><mn>5</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;</mo><mfenced close="|" open="|" separators="|"><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mfrac><msqrt><mn>25</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn></msqrt><mn>3</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><msqrt><mfrac><mn>11</mn><mn>3</mn></mfrac></msqrt></math></p>

</details>

---

### Q150. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `1`

An angle between the lines whose direction cosines are given by the equations, $l+3 m+5 n=$ 0 and $5 l m-2 m n+6 n l=0$, is

**Options:**

- **(A)** $\cos ^{-1}\left(\frac{1}{8}\right)$
- **(B)** $\cos ^{-1}\left(\frac{1}{6}\right)$
- **(C)** $\cos ^{-1}\left(\frac{1}{3}\right)$
- **(D)** $\cos ^{-1}\left(\frac{1}{4}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\cos ^{-1}\left(\frac{1}{6}\right)$**

**Detailed Solution:**

Given
$$
\begin{aligned}
&l+3 m+5 n=0 \\
&\text { and } 5 l m-2 m n+6 n l=0
\end{aligned}
$$
From eq. (1) we have
$$
l=-3 m-5 n
$$
Put the value of $l$ in eq. (2), we get;
$$
\begin{aligned}
&5(-3 m-5 n) m-2 m n+6 n(-3 m-5 n)=0 \\
&\Rightarrow 15 m^2+45 m n+30 n^2=0 \\
&\Rightarrow m^2+3 m n+2 n^2=0 \\
&\Rightarrow m^2+2 m n+m n+2 n^2=0 \\
&\Rightarrow(m+n)(m+2 n)=0 \\
&\therefore m=-n \text { or } m=-2 n \\
&\text { For } m=-n, l=-2 n \\
&\text { And for } m=-2 n, l=n
\end{aligned}
$$

$$
\begin{aligned}
&\therefore(l, m, n)=(-2 n,-n, n) \text { Or }(l, m, n) \\
&=(n,-2 n, n) \\
&\Rightarrow(l, m, n)=(-2,-1,1) \text { Or }(l, m, n) \\
&=(1,-2,1)
\end{aligned}
$$
Therefore, angle between the lines is given as:
$$
\begin{aligned}
&\cos (\theta)=\frac{(-2)(1)+(-1) \cdot(-2)+(1)(1)}{\sqrt{6} \cdot \sqrt{6}} \\
&\Rightarrow \cos (\theta)=\frac{1}{6} \Rightarrow \theta=\cos ^{-1}\left(\frac{1}{6}\right)
\end{aligned}
$$

</details>

---

### Q151. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `2`

If the position vectors of the vertices $A, B$ and $C$ of a $\triangle \mathrm{ABC}$ are respectively $4 \hat{i}+7 \hat{j}+8 \hat{k}, 2 \hat{i}+3 \hat{j}+4 \hat{k}$ and $2 \hat{i}+5 \hat{j}+7 \hat{k}$, then the position vector of the point, where the bisector of $\angle A$ meets $B C$ is

**Options:**

- **(A)** $\frac{1}{2}(4 \hat{i}+8 \hat{j}+11 \hat{k})$
- **(B)** $\frac{1}{3}(6 \hat{i}+13 \hat{j}+18 \hat{k})$
- **(C)** $\frac{1}{4}(8 \hat{i}+14 \hat{j}+9 \hat{k})$
- **(D)** $\frac{1}{3}(6 \hat{i}+11 \hat{j}+15 \hat{k})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{3}(6 \hat{i}+13 \hat{j}+18 \hat{k})$**

**Detailed Solution:**

Suppose angular bisector of $A$ meets $B C$ at $\mathrm{D}(x, y, z)$
Using angular bisector theorem,
$$
\begin{aligned}
\frac{A B}{A C} &=\frac{B D}{D C} \\
\frac{B D}{D C} &=\frac{\sqrt{(4-2)^2+(7-3)^2+(8-4)^2}}{\sqrt{(4-2)^2+(7-5)^2+(8-7)^2}} \\
&=\frac{\sqrt{2^2+4^2+4^2}}{\sqrt{2^2+2^2+1^2}}=\frac{6}{3}=2
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0TZCAnZYDBpG_nY4XcqcHomME8DVm3v_mFHLkeezwy4.original.fullsize.png">

$$
D(x, y, z)=\left(\frac{6}{3}, \frac{13}{3}, \frac{18}{3}\right)
$$
Therefore, position vector of point
$$
P=\frac{1}{3}(6 i+13 j+18 k)
$$

</details>

---

### Q152. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> are unit vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>15</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><msqrt><mn>15</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><msqrt><mn>15</mn></msqrt></mrow><mrow><mn>16</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><msqrt><mn>15</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover></math></p><p>Squaring both sides,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|" separators="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mfenced close="|" open="|" separators="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><msup><mfenced close="|" open="|" separators="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn><mi>cos</mi><mo>&#8289;</mo><mi>&#952;</mi><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mi>cos</mi><mo>&#8289;</mo><mi>&#952;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>sin</mi><mo>&#8289;</mo><mi>&#952;</mi><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi></msqrt><mo>=</mo><mfrac><msqrt><mn>15</mn></msqrt><mn>4</mn></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfenced open="|" close="|" separators="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mfenced open="|" close="|" separators="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mi>sin</mi><mo>&#8289;</mo><mi>&#952;</mi><mo>=</mo><mfrac><msqrt><mn>15</mn></msqrt><mn>4</mn></mfrac></math></p>

</details>

---

### Q153. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{a}, \vec{b}$, and $\overrightarrow{\mathrm{c}}$ are unit vectors such that $\vec{a}+2 \vec{b}+2 \overrightarrow{\mathbf{c}}=\overrightarrow{0}$, then $|\vec{a} \times \overrightarrow{\mathbf{c}}|$ is equal to

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{\sqrt{15}}{4}$
- **(C)** $\frac{15}{16}$
- **(D)** $\frac{\sqrt{15}}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\sqrt{15}}{4}$**

**Detailed Solution:**

$\begin{aligned} & \because \vec{a}+2 \vec{b}+2 \overrightarrow{\mathrm{c}}=\overrightarrow{0} \text { [Given] } \\ \Rightarrow & \vec{a}+2 \overrightarrow{\mathrm{c}}=-2 \vec{b} \\ \Rightarrow &(\vec{a}+2 \mathrm{c} \overrightarrow{)} \cdot(\vec{a}+2 \overrightarrow{\mathrm{c}})=(-2 \vec{b})(-2 \overrightarrow{\mathrm{b}})\\ \Rightarrow \vec{a} \cdot \vec{a}+4 \vec{c} \cdot \vec{c}+4 \vec{a} \cdot \vec{c}=4 \vec{b} \cdot \vec{b} \\ \Rightarrow & 1+4+4 \vec{a} \cdot \overrightarrow{\mathrm{c}}=4 \\ \Rightarrow & \vec{a} \cdot \overrightarrow{\mathrm{c}}=\frac{-1}{4} \\ \because &|\vec{a} \cdot \overrightarrow{\mathrm{c}}|^2+|\vec{a} \times \vec{c}|^2=1(\vec{a} \text { is unit vector }) \\ & \frac{1}{16}+|\vec{a} \times \vec{c}|^2=1 \\ &|\vec{a} \times \vec{c}|^2=\frac{15}{16} \\ &|\vec{a} \times \vec{c}|^2=\frac{\sqrt{15}}{4} \end{aligned}$

</details>

---

### Q154. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mover accent="true"><mrow><mi>u</mi></mrow><mo>&#8594;</mo></mover></math> be a vector coplanar with the vectors <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> and <math><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#160;</mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> . If <math><mover accent="true"><mrow><mi>u</mi></mrow><mo>&#8594;</mo></mover></math> is perpendicular to <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>u</mi><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>24</mn></math>, then <math><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>u</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>84</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>336</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>315</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>256</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>336</mn></math>**

**Detailed Solution:**

As <math> <mrow> <mover accent="true"> <mi>u</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>=</mo><mi>&#955;</mi><mrow><mo>[</mo> <mrow> <mover accent="true"> <mi>a</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>&#215;</mo><mo stretchy="false">(</mo><mover accent="true"> <mi>a</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>&#215;</mo><mover accent="true"> <mi>b</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo stretchy="false">)</mo> </mrow> <mo>]</mo></mrow> </mrow> </math>

<math> <mrow> <mover accent="true"> <mi>u</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>=</mo><mi>&#955;</mi><mrow><mo>[</mo> <mrow> <mrow><mo>[</mo> <mrow> <mover accent="true"> <mi>a</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>.</mo><mover accent="true"> <mi>b</mi> <mo stretchy="true">&#8594;</mo> </mover> </mrow> <mo>]</mo></mrow><mover accent="true"> <mi>a</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>&#8722;</mo><mo>|</mo><mover accent="true"> <mi>a</mi> <mo stretchy="true">&#8594;</mo> </mover> <msup> <mo>|</mo> <mn>2</mn> </msup> <mover accent="true"> <mi>b</mi> <mo stretchy="true">&#8594;</mo> </mover> </mrow> <mo>]</mo></mrow> </mrow> </math>

<math> <mrow> <mover accent="true"> <mi>u</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>=</mo><mi>&#955;</mi><mrow><mo>[</mo> <mrow> <mn>2</mn><mover accent="true"> <mi>a</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>&#8722;</mo><mn>14</mn><mover accent="true"> <mi>b</mi> <mo stretchy="true">&#8594;</mo> </mover> </mrow> <mo>]</mo></mrow> </mrow> </math>

<math> <mrow> <mover accent="true"> <mi>u</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>.</mo><mover accent="true"> <mi>b</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>=</mo><mn>2</mn><mi>&#955;</mi><mrow><mo>[</mo> <mrow> <mover accent="true"> <mi>a</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>.</mo><mtext>&#8201;</mtext><mover accent="true"> <mi>b</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>&#8722;</mo><mn>7</mn><mo>|</mo><mover accent="true"> <mi>b</mi> <mo stretchy="true">&#8594;</mo> </mover> <msup> <mo>|</mo> <mn>2</mn> </msup> </mrow> <mo>]</mo></mrow> </mrow> </math>

<math> <mrow> <mo>=</mo><mn>2</mn><mi>&#955;</mi><mrow><mo>[</mo> <mrow> <mn>2</mn><mo>&#8722;</mo><mn>14</mn> </mrow> <mo>]</mo></mrow> </mrow> </math>

<math> <mrow> <mn>24</mn><mo>=</mo><mo>&#8722;</mo><mn>24</mn><mi>&#955;</mi> </mrow> </math>

<math> <mrow> <mi>&#955;</mi><mo>=</mo><mo>&#8722;</mo><mn>1</mn> </mrow> </math>

<math> <mrow> <mover accent="true"> <mi>u</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>=</mo><mn>14</mn><mover accent="true"> <mi>b</mi> <mo stretchy="true">&#8594;</mo> </mover> <mo>&#8722;</mo><mn>2</mn><mover accent="true"> <mi>a</mi> <mo stretchy="true">&#8594;</mo> </mover> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>u</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>4</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>8</mn><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>16</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover></math>

<math> <mrow> <mo>|</mo><mover accent="true"> <mi>u</mi> <mo stretchy="true">&#8594;</mo> </mover> <msup> <mo>|</mo> <mn>2</mn> </msup> <mo>=</mo><msup> <mn>4</mn> <mn>2</mn> </msup> <mo>+</mo><msup> <mn>8</mn> <mn>2</mn> </msup> <mo>+</mo><msup> <mrow> <mn>16</mn> </mrow> <mn>2</mn> </msup> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>336</mn></math>

</details>

---

### Q155. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If the vector <math><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> is written as the sum of a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>b</mi><mn>1</mn></msub><mo>&#8594;</mo></mover></math>,<mo></mo><mrow><mn></mn></mrow> parallel to <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#160;</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>&#160;</mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></math> and a vector <math><msub><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo></math> perpendicular to <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>,</mo></math> then <math><msub><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></mrow><mrow><mn>1</mn></mrow></msub><mo>&#215;</mo><msub><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></mrow><mrow><mn>2</mn></mrow></msub></math> is equal to :

**Options:**

- **(A)** <math><mn>6</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>6</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
- **(B)** <math><mo>-</mo><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>9</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
- **(C)** <math><mo>-</mo><mn>6</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
- **(D)** <math><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>9</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>6</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>6</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7754a782-c4cf-463c-9974-c05c5432c15b-image.png" style="width: 180px; height: 159px;" />

<math><msub><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&rarr;</mo></mover></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&rarr;</mo></mover><mi> </mi><mo>&sdot;</mo><mi> </mi><mover accent="true"><mrow><mi>a</mi></mrow><mo>&rarr;</mo></mover></mrow></mfenced><mover accent="true"><mrow><mi>a</mi></mrow><mo>^</mo></mover></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>

<math><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mfrac><mrow><mfenced separators="|"><mrow><mn>3</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>&sdot;</mo><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mi> </mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mrow></mfenced></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mi> </mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced></math>

<math><mo>=</mo><mfrac><mrow><mn>3</mn><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mi> </mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mrow></mfenced></mrow><mrow><msqrt><mn>2</mn></msqrt><mo>&times;</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mi> </mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><msub><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&rarr;</mo></mover></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&rarr;</mo></mover></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mover accent="true"><mrow><mi>b</mi></mrow><mo>&rarr;</mo></mover></math>

<math><msub><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&rarr;</mo></mover></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mover accent="true"><mrow><mi>b</mi></mrow><mo>&rarr;</mo></mover><mo>-</mo><mi> </mi><msub><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&rarr;</mo></mover></mrow><mrow><mn>1</mn></mrow></msub></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi> </mi><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced></math>

<math><msub><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&rarr;</mo></mover></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>

<math><msub><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&rarr;</mo></mover></mrow><mrow><mn>1</mn></mrow></msub><mo>&times;</mo><msub><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&rarr;</mo></mover></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mtd><mtd><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mtd></mtr><mtr><mtd><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&rArr;</mo><mover><mi>i</mi><mo>^</mo></mover><mfenced separators="|"><mn>6</mn></mfenced><mo>-</mo><mi> </mi><mover><mi>j</mi><mo>^</mo></mover><mfenced separators="|"><mn>6</mn></mfenced><mo>+</mo><mi> </mi><mover><mi>k</mi><mo>^</mo></mover><mfenced separators="|"><mrow><mfrac><mn>9</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></mrow></mfenced><mspace linebreak="newline"></mspace><mo>=</mo><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>6</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mover><mi>k</mi><mo>^</mo></mover></math>

</details>

---

### Q156. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The area (in sq. units) of the parallelogram whose diagonals are along the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>6</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>12</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>65</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>65</mn></math>**

**Detailed Solution:**

Let the given diagonals be <math> <mrow> <mover accent="true"> <mrow> <msub> <mi>d</mi> <mn>1</mn> </msub> </mrow> <mo stretchy="true">&#8594;</mo> </mover> </mrow> </math> and <math> <mrow> <mover accent="true"> <mrow> <msub> <mi>d</mi> <mn>2</mn> </msub> </mrow> <mo stretchy="true">&#8594;</mo> </mover> </mrow> </math> , then

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub><mo>&#215;</mo><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mtd><mtd><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>8</mn></mtd><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>12</mn></mtd></mtr></mtable></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>72</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mfenced separators="|"><mrow><mo>-</mo><mn>96</mn></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>50</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mrow><msub><mi>d</mi><mn>1</mn></msub><mo>&#215;</mo><msub><mi>d</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><msqrt><msup><mn>72</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>96</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>50</mn></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>5184</mn><mo>+</mo><mn>9216</mn><mo>+</mo><mn>2500</mn></msqrt></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mrow><msub><mi>d</mi><mn>2</mn></msub><mo>&#215;</mo><msub><mi>d</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mi>&#160;</mi><msqrt><mn>16900</mn></msqrt><mo>=</mo><mn>130</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Area</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="|" close="|" separators="|"><mrow><msub><mi>d</mi><mn>1</mn></msub><mo>&#215;</mo><msub><mi>d</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>130</mn></math>

<math><mo>=</mo><mn>65</mn></math>

</details>

---

### Q157. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `1`

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#160;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>.</mo></math> Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> be a vector such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mi>&#160;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mfenced close="|" open="|" separators="|"><mrow><mfenced separators="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>3</mn></math> and the angle between <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#176;</mo></math> . Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>8</mn></mfrac></math>
- **(B)** <math><mn>2</mn></math>
- **(C)** <math><mn>5</mn></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>3</mn></math></p><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mrow><mfenced separators="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#215;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mfenced close="|" open="|" separators="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mi>sin</mi><mn>30</mn><mo>&#176;</mo><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>2</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|" separators="|"><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|" separators="|"><mover><mi>c</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|" separators="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced separators="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q158. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math>, right angle at vertex <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>, if the position vectors of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> are respectively <math><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>&#160;</mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mi>&#160;</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>,</mo><mi>&#160;</mi><mo>-</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>p</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> and <math><mn>5</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>q</mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> , then the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>p</mi><mo>,</mo><mi>q</mi></mrow></mfenced></math> lies on a line:

**Options:**

- **(A)** Making an obtuse angle with the positive direction of <math><mi>x</mi><mo>-</mo><mi>a</mi><mi>x</mi><mi>i</mi><mi>s</mi></math>
- **(B)** Parallel to  <math><mi>x</mi><mo>-</mo><mi>a</mi><mi>x</mi><mi>i</mi><mi>s</mi></math>
- **(C)** Parallel to  <math><mi>y</mi><mo>-</mo><mi>a</mi><mi>x</mi><mi>i</mi><mi>s</mi></math>
- **(D)** Making an acute angle with the positive direction of <math><mi>x</mi><mo>-</mo><mi>a</mi><mi>x</mi><mi>i</mi><mi>s</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Making an acute angle with the positive direction of <math><mi>x</mi><mo>-</mo><mi>a</mi><mi>x</mi><mi>i</mi><mi>s</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e2bccc4e-684e-4c35-8dc8-295be7ac53a2-image.png" style="width: 207px; height: 150px;" />

<math><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#160;</mi><mo>-</mo><mn>4</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math></p><p><math><mover accent="true"><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#160;</mi><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mi>q</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math></p><p><math><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#8869;</mo><mover accent="true"><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></math></p><p><math><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mi>&#160;</mi><mo>&#183;</mo><mi>&#160;</mi><mover accent="true"><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math>

<math><mo>-</mo><mn>8</mn><mo>+</mo><mn>2</mn><mfenced separators="|"><mrow><mi>q</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mn>3</mn><mi>p</mi><mo>-</mo><mn>2</mn><mi>q</mi><mo>+</mo><mn>13</mn><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>p</mi><mo>,</mo><mi>q</mi></mrow></mfenced></math> lies on <math><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>13</mn><mo>=</mo><mn>0</mn></math>

Slope <math><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mo>&#8756;&#160;&#160;</mo></math>The required line makes an acute angle with the positive direction of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis.</p>

</details>

---

### Q159. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

In a parallelogram <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi><mo>,</mo><mi>&#160;</mi><mfenced open="|" close="|" separators="|"><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mi>a</mi><mo>,</mo><mi>&#160;</mi><mfenced open="|" close="|" separators="|"><mover accent="true"><mrow><mi>A</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mi>b</mi><mo>&#160;</mo><mo>&#38;</mo><mi>&#160;</mi><mfenced open="|" close="|" separators="|"><mover accent="true"><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mi>c</mi></math>. <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mrow><mi>D</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></math> has the value:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mfenced separators="|"><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced separators="|"><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a3cb9cbc-5f9a-4d09-8864-08cdbae5a38f-image.png" style="width: 300px; height: 142px;" /></p><p><math><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mi>a</mi></math>

<math><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>A</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mi>b</mi></math>

<math><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mi>c</mi></math>

Squaring both side <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|" separators="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|" separators="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><msup><mi>c</mi><mn>2</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#8230;</mo><mfenced separators="|"><mn>1</mn></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mrow><mi>D</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced separators="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced separators="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></math>

<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>(</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>)</mo></math></p>

</details>

---

### Q160. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mi>&#160;</mi></math>be two unit vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mo>(</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>)</mo></math> , then <math><mn>2</mn><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math><msqrt><mn>51</mn></msqrt></math>
- **(B)** <math><msqrt><mn>37</mn></msqrt></math>
- **(C)** <math><msqrt><mn>43</mn></msqrt></math>
- **(D)** <math><msqrt><mn>55</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msqrt><mn>55</mn></msqrt></math>**

**Detailed Solution:**

As <math><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>a</mi></mrow><mo>→</mo></mover><mi> </mi><mo>+</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>→</mo></mover><mi> </mi></mrow></mfenced><mo>=</mo><mi> </mi><msqrt><mn>3</mn></msqrt></math>

Squaring both the sides 

<math><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>a</mi></mrow><mo>→</mo></mover></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi> </mi><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mover accent="true"><mrow><mi>b</mi></mrow><mo>→</mo></mover></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>a</mi></mrow><mo>→</mo></mover><mo>⋅</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>→</mo></mover><mo>=</mo><mn>3</mn></math>

<math><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi> </mi><mo>⋅</mo><mn>1</mn><mo>⋅</mo><mn>1</mn><mo>⋅</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi><mo>=</mo><mn>3</mn></mrow></mrow></math>

<math><mn>2</mn><mi>c</mi><mi>o</mi><mi>s</mi><mi>θ</mi><mo>=</mo><mn>1</mn></math>

<math><mi>c</mi><mi>o</mi><mi>s</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mi>θ</mi><mo>=</mo><mn>60°</mn></math>

<math><mo>∴</mo><mi> </mi><mi> </mi></math> Angle between <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>→</mo></mover><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><mover accent="true"><mrow><mi>b</mi></mrow><mo>→</mo></mover><mi> </mi><mi>i</mi><mi>s</mi><mi> </mi><msup><mrow><mn>60</mn></mrow><mrow><mi>o</mi></mrow></msup></math>

Now, 

<math> <mrow> <mo>|</mo><mover accent="true"> <mi>c</mi> <mo stretchy="true">→</mo> </mover> <mo>|</mo><mtext> </mtext><mo>=</mo><mtext> </mtext><mo>|</mo><mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> <mtext> </mtext><mo>+</mo><mtext> </mtext><mn>2</mn><mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <mtext> </mtext><mo>+</mo><mtext> </mtext><mn>3</mn><mo stretchy="false">(</mo><mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> <mtext> </mtext><mo>×</mo><mtext> </mtext><mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <mo stretchy="false">)</mo><mo>|</mo> </mrow> </math>

Squaring both the sides 

<math> <mrow> <mo>|</mo><mover accent="true"> <mi>c</mi> <mo stretchy="true">→</mo> </mover> <msup> <mo>|</mo> <mn>2</mn> </msup> <mtext> </mtext><mo>=</mo><mtext> </mtext><mo>|</mo><mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> <mtext> </mtext><msup> <mo>|</mo> <mn>2</mn> </msup> <mo>+</mo><mtext> </mtext><mn>4</mn><mo>|</mo><mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <mo>|</mo><mtext> </mtext><mo>+</mo><mtext> </mtext><mn>9</mn><mo>|</mo><mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> <mtext> </mtext><mo>×</mo><mtext> </mtext><mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <msup> <mo>|</mo> <mn>2</mn> </msup> <mo>+</mo><mtext> </mtext><mn>4</mn><mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> <mo>.</mo><mo stretchy="false">(</mo><mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <mo stretchy="false">)</mo><mo>+</mo><mn>3</mn><mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> <mo>.</mo><mo stretchy="false">(</mo><mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> <mtext> </mtext><mo>×</mo><mtext> </mtext><mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <mo stretchy="false">)</mo><mo>+</mo><mn>6</mn><mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <mo>.</mo><mo stretchy="false">(</mo><mover accent="true"> <mi>a</mi> <mo stretchy="true">→</mo> </mover> <mtext> </mtext><mo>×</mo><mtext> </mtext><mover accent="true"> <mi>b</mi> <mo stretchy="true">→</mo> </mover> <mo stretchy="false">)</mo> </mrow> </math>

<math> <mrow> <mo>|</mo><mover accent="true"> <mi>c</mi> <mo stretchy="true">→</mo> </mover> <msup> <mo>|</mo> <mn>2</mn> </msup> <mtext> </mtext><mo>=</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>9</mn><msup> <mrow> <mi>sin</mi> </mrow> <mn>2</mn> </msup> <mi>θ</mi><mo>+</mo><mn>4</mn><mi>cos</mi><mi>θ</mi><mo>+</mo><mn>0</mn><mo>+</mo><mn>0</mn> </mrow> </math>

<math> <mrow> <mo>|</mo><mover accent="true"> <mi>c</mi> <mo stretchy="true">→</mo> </mover> <msup> <mo>|</mo> <mn>2</mn> </msup> <mtext> </mtext><mo>=</mo><mn>5</mn><mo>+</mo><mn>9.</mn><mfrac> <mn>3</mn> <mn>4</mn> </mfrac> <mo>+</mo><mn>4.</mn><mfrac> <mn>1</mn> <mn>2</mn> </mfrac> <mo>=</mo><mfrac> <mrow> <mn>55</mn> </mrow> <mn>4</mn> </mfrac> </mrow> </math>

<math> <mrow> <mo>∴</mo><mtext> </mtext><mtext> </mtext><mn>2</mn><mtext> </mtext><mo>|</mo><mover accent="true"> <mi>c</mi> <mo stretchy="true">→</mo> </mover> <mo>|</mo><mtext> </mtext><mo>=</mo><msqrt> <mrow> <mn>55</mn> </mrow> </msqrt> </mrow> </math>

</details>

---

### Q161. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If $\hat{x}, \hat{y}$ and $\hat{z}$ are three unit vectors in threedimensional space, then the minimum value of $|\hat{x}+\hat{y}|^2+|\hat{y}+\hat{z}|^2+|\hat{z}+\hat{x}|^2$

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** 3
- **(C)** $3 \sqrt{3}$
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3**

**Detailed Solution:**

$(\hat{x}+\hat{y}+\hat{z})^2 \geq 0$
$$
\begin{aligned}
&\Rightarrow 3+2 \Sigma \hat{x} \cdot \hat{y} \geq 0 \\
&\Rightarrow 2 \Sigma \hat{x} \cdot \hat{y} \geq-3
\end{aligned}
$$
Now, $|\hat{x}+\hat{y}|^2+|\hat{y}+\hat{z}|^2+|\hat{z}+\hat{x}|^2$ $=6+2 \sum \hat{x} . \hat{y} \geq 6+(-3)$
$$
\Rightarrow|\hat{x}+\hat{y}|^2+|\hat{y}+\hat{z}|^2+|\hat{z}+\hat{x}|^2 \geq 3
$$

</details>

---

### Q162. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If $|\vec{c}|^2=60$ and $\vec{c} \times(\hat{i}+2 \hat{j}+5 \hat{k})=\overrightarrow{0}$, then a value of $\vec{c} \cdot(-7 \hat{i}+2 \hat{j}+3 \hat{k})$ is:

**Options:**

- **(A)** $4 \sqrt{2}$
- **(B)** 12
- **(C)** 24
- **(D)** $12 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $12 \sqrt{2}$**

**Detailed Solution:**

Let, $\vec{c}=a \hat{i}+b \hat{j}+c \hat{k}$
Given, $\vec{c} \times(\hat{i}+2 \hat{j}+5 \hat{k})=\overrightarrow{0}$
$$
\begin{aligned}
&\Rightarrow\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
a & b & c \\
1 & 2 & 5
\end{array}\right|=\overrightarrow{0} \\
&\Rightarrow(5 b-2 c) \hat{i}-(5 a-c) \hat{j}+(2 a-b) \hat{k} \\
&=0 \hat{i}+0 \hat{j}+0 \hat{k}
\end{aligned}
$$
Comparing both sides, we get $5 b-2 c=0 ; 5 a-c=0 ; 2 a-b=0$ or $5 b=2 c ; 5 a=c ; 2 a=b$
Also given $|\vec{c}|^2=60$
$$
\Rightarrow a^2+b^2+c^2=60
$$
Putting the value of $b$ and $c$ in above eqn., we get

$$
\begin{aligned}
&a^2+(2 a)^2+(5 a)^2=60 \\
&\Rightarrow a^2+4 a^2+25 a^2=60 \Rightarrow 30 a^2=60 \\
&a^2=2 \\
&a=\pm \sqrt{2} ; b=2 \sqrt{2} ; c=5 \sqrt{2}
\end{aligned}
$$
Now, $\vec{c}=a \hat{i}+b \hat{j}+c \hat{k}$
$$
\therefore \vec{c}=\sqrt{2} \hat{i}+2 \sqrt{2} \hat{j}+5 \sqrt{2} \hat{k}
$$
Value of $\vec{c} \cdot(-7 \hat{i}+2 \hat{j}+3 \hat{k})$ is
$$
\begin{aligned}
&(\sqrt{2} \hat{i}+2 \sqrt{2} \hat{j}+5 \sqrt{2} \hat{k}) \cdot(-7 \hat{i}+2 \hat{j}+3 \hat{k}) \\
&=-7 \sqrt{2}+4 \sqrt{2}+15 \sqrt{2}=12 \sqrt{2}
\end{aligned}
$$

</details>

---

### Q163. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mfenced close="|" open="|"><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mn>2</mn><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>5</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mn>2</mn><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> equals :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;&#160;</mo><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;&#160;</mo><mfenced open="|" close="|"><mrow><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>5</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mrow><mn>2</mn><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfenced><mrow><mn>2</mn><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>2</mn><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mfenced open="[" close="]"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><msup><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mrow><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><mfenced open="[" close="]"><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><msup><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Adding equation (i) and equation (ii), we get

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mrow><mn>2</mn><mo>&#160;</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><mrow><mn>2</mn><mo>&#160;</mo><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>8</mn><msup><mfenced open="|" close="|"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>+</mo><msup><mrow><mn>2</mn><mfenced open="|" close="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced></mrow><mn>2</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;</mo><msup><mfenced open="|" close="|"><mrow><mn>2</mn><mo>&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup><mo>=</mo><mn>8</mn><mfenced><msup><mn>2</mn><mn>2</mn></msup></mfenced><mo>+</mo><mn>2</mn><mfenced><msup><mn>3</mn><mn>2</mn></msup></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;</mo><msup><mfenced open="|" close="|"><mrow><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>32</mn><mo>+</mo><mn>18</mn><mo>-</mo><mn>25</mn></math><math> <mrow> <mo>=</mo> <mn>2</mn> <mn>5</mn> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><mfenced open="|" close="|"><mrow><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q164. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $\hat{a}, \hat{b}$ and $\hat{c}$ are unit vectors satisfying $\hat{a}-\sqrt{3} \hat{b}+\hat{c}=\overrightarrow{0}$, then the angle between the vectors $\hat{a}$ and $\hat{c}$ is :

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{\pi}{6}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{3}$**

**Detailed Solution:**

Let angle between $\hat{a}$ and $\hat{c}$ be $\theta$.
Now, $\hat{a}-\sqrt{3} \hat{b}+\hat{c}=\overrightarrow{0}$
$$
\begin{aligned}
& \Rightarrow(\hat{a}+\hat{c})=\sqrt{3} \hat{b} \\
& \Rightarrow(\hat{a}+\hat{c}) \cdot(\hat{a}+\hat{c})=3(\hat{b} \cdot \hat{b}) \\
& \Rightarrow \hat{a} \cdot \hat{a}+\hat{a} \cdot \hat{c}+\hat{c} \cdot \hat{a}+\hat{c} \cdot \hat{c}=3 \times 1 \\
& \Rightarrow 1+2 \cos \theta+1=3 \\
& \Rightarrow \cos \theta=\frac{1}{2} \Rightarrow \theta=\frac{\pi}{3}
\end{aligned}
$$

</details>

---

### Q165. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

A vector $\vec{n}$ is inclined to $x$-axis at $45^{\circ}$, to $y$-axis at $60^{\circ}$ and at an acute angle to $z$-axis. If $\vec{n}$ is a normal to a plane passing through the point $(\sqrt{2},-1,1)$ then the equation of the plane is :

**Options:**

- **(A)** $4 \sqrt{2} x+7 y+z-2$
- **(B)** $2 x+y+2 z=2 \sqrt{2}+1$
- **(C)** $3 \sqrt{2} x-4 y-3 z=7$
- **(D)** $\sqrt{2} x-y-z=2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 x+y+2 z=2 \sqrt{2}+1$**

**Detailed Solution:**

Direction cosines of $\vec{n}$ are $\frac{1}{2}, \frac{1}{4}, \frac{1}{2}$.
Equation of the plane,
$$
\begin{aligned}
& \frac{1}{2}(x-\sqrt{2})+\frac{1}{4}(y+1)+\frac{1}{2}(z-1)=0 \\
\Rightarrow & 2(x-\sqrt{2})+(y+1)+2(z-1)=0 \\
\Rightarrow & 2 x+y+2 z=2 \sqrt{2}-1+2 \\
\Rightarrow & 2 x+y+2 z=2 \sqrt{2}+1
\end{aligned}
$$

</details>

---

### Q166. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Statement 1: The vectors $\vec{a}, \vec{b}$ and $\vec{c}$ lie in the same plane if and only if $\vec{a} \cdot(\vec{b} \times \vec{c})=0$
Statement 2: The vectors $\vec{u}$ and $\vec{v}$ are perpendicular if and only if $\vec{u} \cdot \vec{v}=0$ where $\vec{u} \times \vec{v}$ is a vector perpendicular to the plane of $\vec{u}$ and $\vec{v}$

**Options:**

- **(A)** Statement 1 is false, Statement 2 is true.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is correct explanation for Statement 1.
- **(C)** Statement 1 is true, Statement 2 is false.
- **(D)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation for Statement 1.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement 1 is true, Statement 2 is false.**

**Detailed Solution:**

Statement - 1
The vectors $\vec{a}, \vec{b}$ and $\vec{c}$ lie in the same plane.
$\Rightarrow \vec{a}, \vec{b}$ and $\vec{c}$ are coplanar.
We know, the necessary and sufficient conditions for three vectors to be coplanar is that $[\vec{a} \vec{b} \vec{c}]=0$
i.e. $\vec{a} \cdot(\vec{b} \times \vec{c})=0$
Hence, statement-1 is true.

</details>

---

### Q167. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `1`

If $a+b+c=0,|\vec{a}|=3,|\vec{b}|=5$ and $|\vec{c}|=7$, then the angle between $\vec{a}$ and $\vec{b}$ is

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{6}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{3}$**

**Detailed Solution:**

Let $a+b+c=0 \Rightarrow(a+b)=-c$ $\Rightarrow(a+b)^2=c^2$
$$
\begin{aligned}
& \Rightarrow a^2+b^2+2 a \cdot b=c^2 \\
& \Rightarrow 9+25+2.3 .5 \cos \theta=49 \\
& (\because|\vec{a}|=3,|\vec{b}|=5 \text { and }|\vec{c}|=7) \\
& \therefore \cos \theta=\frac{1}{2} \Rightarrow \theta=\frac{\pi}{3}
\end{aligned}
$$

</details>

---

### Q168. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `1`

Let $\hat{a}$ and $\hat{b}$ be two unit vectors. If the vectors $\vec{c}=\hat{a}+2 \hat{b}$ and $\vec{d}=5 \hat{a}-4 \hat{b}$ are perpendicular to each other, then the angle between $\hat{\mathrm{a}}$ and $\hat{\mathrm{b}}$ is

**Options:**

- **(A)** $\frac{\pi}{6}$
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{3}$**

**Detailed Solution:**

$\overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{d}}=\overrightarrow{0} \quad \Rightarrow 5|\overrightarrow{\mathrm{a}}|^2+6 \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{b}}-8|\overrightarrow{\mathrm{b}}|^2=0$
$\Rightarrow 6 \vec{a} \cdot \vec{b}=3 \quad \Rightarrow \vec{a} \cdot \vec{b}=\frac{1}{2} \quad \Rightarrow(\vec{a} \cdot \vec{b})=\frac{\pi}{3}$

</details>

---

### Q169. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `3`

The vector $\vec{a}$ and $\vec{b}$ are not perpendicular and $\vec{c}$ and $\vec{d}$ are two vectors satisfying: $\vec{b} \times \vec{c}=\vec{b} \times \vec{d}$ and $\vec{a} \cdot \vec{d}=0$. Then the vector $\vec{d}$ is equal to

**Options:**

- **(A)** $\vec{c}+\left(\frac{\vec{a} \cdot \vec{c}}{\vec{a} \cdot \vec{b}}\right) \vec{b}$
- **(B)** $\vec{b}+\left(\frac{\vec{b} \cdot \vec{c}}{\vec{a} \cdot \vec{b}}\right) \vec{c}$
- **(C)** $\vec{c}-\left(\frac{\vec{a} \cdot \vec{c}}{\vec{a} \cdot \vec{b}}\right) \vec{b}$
- **(D)** $\vec{b}-\left(\frac{\vec{b} \cdot \vec{c}}{\vec{a} \cdot \vec{b}}\right) \vec{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\vec{c}-\left(\frac{\vec{a} \cdot \vec{c}}{\vec{a} \cdot \vec{b}}\right) \vec{b}$**

**Detailed Solution:**

$\overline{\mathrm{b}} \times \overline{\mathrm{c}}=\overline{\mathrm{b}} \times \overline{\mathrm{d}}$
$\Rightarrow \overline{\mathrm{a}} \times(\overline{\mathrm{b}} \times \overline{\mathrm{c}})=\overline{\mathrm{a}} \times(\overline{\mathrm{b}} \times \overline{\mathrm{d}})$
$\Rightarrow(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) \overline{\mathrm{b}}-(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}) \overline{\mathrm{c}}=(\overline{\mathrm{a}} \cdot \overline{\mathrm{d}}) \overline{\mathrm{b}}-(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}) \overline{\mathrm{d}}$
$\Rightarrow(\overline{\mathrm{a}} \cdot \overline{\mathrm{c}}) \overline{\mathrm{b}}-(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}) \overline{\mathrm{c}}=-(\overline{\mathrm{a}} \cdot \overline{\mathrm{b}}) \overline{\mathrm{d}}$
$\therefore \overline{\mathrm{d}}=\overline{\mathrm{c}}-\left(\frac{\overline{\mathrm{a}} \cdot \overline{\bar{c}}}{\overline{\mathrm{a}} \overline{\mathrm{b}}}\right) \overline{\mathrm{b}}$

</details>

---

### Q170. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `3`

If the vectors $\overrightarrow{\mathrm{a}}=\hat{\mathrm{i}}-\hat{\mathrm{j}}+2 \hat{\mathrm{k}}, \overrightarrow{\mathrm{b}}=2 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+\hat{\mathrm{k}}$ and $\overrightarrow{\mathrm{c}}=\lambda \hat{\mathrm{i}}+\hat{\mathrm{j}}+\mu \hat{\mathrm{k}}$ are mutually orthogonal, then $(\lambda, \mu)=$

**Options:**

- **(A)** $(2,-3)$
- **(B)** $(-2,3)$
- **(C)** $(3,-2)$
- **(D)** $(-3,2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(-3,2)$**

**Detailed Solution:**

$$
\begin{aligned}
& \vec{a} \cdot \vec{b}=0, \quad \vec{b} \cdot \vec{c}=0, \quad \vec{c} \cdot \vec{a}=0 \\
& \Rightarrow 2 \lambda+4+\mu=0 \quad \lambda-1+2 \mu=0 \\
&
\end{aligned}
$$
Solving we get: $\lambda=-3, \mu=2$

</details>

---

### Q171. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=\hat{j}-\hat{k}$ and $\vec{c}=\hat{i}-\hat{j}-\hat{k}$. Then vector $\vec{b}$ satisfying $\vec{a} \times \vec{b}+\vec{c}=\overrightarrow{0}$ and $\vec{a} \cdot \vec{b}=3$ is

**Options:**

- **(A)** $2 \hat{i}-\hat{j}+2 \hat{k}$
- **(B)** $\hat{i}-\hat{j}-2 \hat{k}$
- **(C)** $\hat{i}+\hat{j}-2 \hat{k}$
- **(D)** $-\hat{i}+\hat{j}-2 \hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\hat{i}+\hat{j}-2 \hat{k}$**

**Detailed Solution:**

$\overrightarrow{\mathrm{c}}=\overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{a}}$
$\Rightarrow \overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{c}}=0$
$\Rightarrow\left(\mathrm{b}_1 \hat{\mathrm{i}}+\mathrm{b}_2 \hat{j}+\mathrm{b}_3 \hat{\mathrm{k}}\right) \cdot(\hat{\mathrm{i}}-\hat{\mathrm{j}}-\hat{\mathrm{k}})=0$
$\mathrm{~b}_1-\mathrm{b}_2-\mathrm{b}_3=0$
and $\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{b}}=3$
$\Rightarrow \mathrm{b}_2-\mathrm{b}_3=3$
$\mathrm{~b}_1=\mathrm{b}_2+\mathrm{b}_3=3+2 \mathrm{~b}_3$
$\overrightarrow{\mathrm{b}}=\left(3+2 \mathrm{~b}_3\right) \hat{\mathrm{i}}+\left(3+\mathrm{b}_3\right) \hat{\mathrm{j}}+\mathrm{b}_3 \hat{\mathrm{k}}$

</details>

---

### Q172. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

The non-zero verctors $\vec{a}, \vec{b}$ and $\vec{c}$ are related by $\vec{a}=8 \vec{b}$ and $\vec{c}=-7 \vec{b}$. Then the angle between $\vec{a}$ and $\overrightarrow{\mathrm{c}}$ is

**Options:**

- **(A)** 0
- **(B)** $\pi / 4$
- **(C)** $\pi / 2$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\pi$**

**Detailed Solution:**

Since $\vec{a}=8 \vec{b}$
$$
\overrightarrow{\mathrm{c}}=-7 \overrightarrow{\mathrm{b}}
$$
$\therefore \vec{a}$ and $\vec{b}$ are like vectors and $\vec{b}$ and $\vec{c}$ are unlike.
$\Rightarrow \vec{a}$ and $\vec{c}$ will be unlike
Hence, angle between $\vec{a}$ and $\vec{c}=\pi$.

</details>

---

### Q173. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

Let $\overline{\mathrm{a}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}}, \overline{\mathrm{b}}=\hat{\mathrm{i}}-\hat{\mathrm{j}}+2 \hat{\mathrm{k}}$ and $\overline{\mathrm{c}}=\mathrm{x} \hat{\mathrm{i}}+(\mathrm{x}-2) \hat{\mathrm{j}}-\hat{\mathrm{k}}$. If the vector $\overline{\mathrm{c}}$ lies in the plane of $\bar{a}$ and $\bar{b}$, then $x$ equals

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $-4$
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-2$**

**Detailed Solution:**

$\vec{a}=\hat{i}+\hat{j}+\hat{k}, \vec{b}=\hat{i}-\hat{j}+2 \hat{k}$ and $\vec{c}=x \hat{i}+(x-2) \hat{j}-\hat{k}$
$\left|\begin{array}{ccr}x & x-2 & -1 \\ 1 & 1 & 1 \\ 1 & -1 & 2\end{array}\right|=0$
$3 x+2-x+2=0$
$2 x=-4$
$x=-2$.

</details>

---

### Q174. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

If $\hat{u}$ and $\hat{v}$ are unit vectors and $\theta$ is the acute angle between them, then $2 \hat{u} \times 3 \hat{v}$ is a unit vector for

**Options:**

- **(A)** exactly two values of $\theta$
- **(B)** more than two values of $\theta$
- **(C)** no value of $\theta$
- **(D)** exactly one value of $\theta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) exactly one value of $\theta$**

**Detailed Solution:**

$|2 \hat{u} \times 3 \hat{v}|=1$
$\begin{aligned}
& 6|\hat{u}\|\hat{v} \| \sin \theta|=1 \\
& \sin \theta=\frac{1}{6}
\end{aligned}$
Hence there is exactly one value of $\theta$ for which $2 \hat{u} \times 3 \hat{v}$ is a unit vector.

</details>

---

### Q175. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

The values of $a$, for which the points $A, B, C$ with position vectors $2 \hat{i}-\hat{j}+\hat{k}, \hat{i}-3 \hat{j}-5 \hat{k}$ and $a \hat{i}-3 \hat{j}+\hat{k}$ respectively are the vertices of a right-angled triangle with $C=\frac{\pi}{2}$ are

**Options:**

- **(A)** 2 and 1
- **(B)** −2 and −1
- **(C)** −2 and 1
- **(D)** 2 and −1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2 and 1**

**Detailed Solution:**

$\Rightarrow \overrightarrow{B A}=\hat{i}-2 \hat{j}+6 \hat{k}$
$\overrightarrow{C A}=(2-a) \hat{i}+2 \hat{j}$
$\overrightarrow{C B}=(1-a) \hat{i}-6 \hat{k}$
$\overrightarrow{C A} \cdot \overrightarrow{C B}=0 \Rightarrow(2-a)(1-a)=0$
$\Rightarrow a=2,1$

</details>

---

### Q176. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

For any vectora a the value of $(\vec{a} \times \hat{i})^2+(\vec{a} \times \hat{j})^2+(\vec{a} \times \hat{k})^2$ is equal to

**Options:**

- **(A)** $3 \vec{a}^2$
- **(B)** $\vec{a}^2$
- **(C)** $2 \vec{a}^2$
- **(D)** $4 \vec{a}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 \vec{a}^2$**

**Detailed Solution:**

Let $\vec{a}=x \hat{i}+y \hat{j}+z \hat{k}$
$$
\begin{aligned}
& \vec{a} \times \hat{\mathbf{i}}=z \hat{\mathbf{j}}-y \hat{\mathbf{k}} \\
& \Rightarrow(\vec{a} \times \hat{\mathbf{i}})^2=y^2+z^2
\end{aligned}
$$
similarly $(\vec{a} \times \hat{j})^2=x^2+z^2$
and $(\vec{a} \times \hat{k})^2=x^2+y^2 \Rightarrow(\vec{a} \times \hat{i})^2=y^2+z^2$
similarly $(\vec{a} \times \hat{j})^2=x^2+z^2$
and $(\vec{a} \times \hat{k})^2=x^2+y^2$
$$
\Rightarrow(\vec{a} \times \hat{i})^2+(\vec{a} \times \hat{j})^2+(\vec{a} \times \hat{k})^2=2\left(x^2+y^2+z^2\right)=2 \vec{a}^2 .
$$

</details>

---

### Q177. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

With two forces acting at a point, the maximum effect is obtained when their resultant is $4 \mathrm{~N}$. If they act at right angles, then their resultant is $3 \mathrm{~N}$. Then the forces are

**Options:**

- **(A)** $(2+\sqrt{2}) N$ and $(2-\sqrt{2}) N$
- **(B)** $(2+\sqrt{3}) \mathrm{N}$ and $(2-\sqrt{3}) \mathrm{N}$
- **(C)** $\left(2+\frac{1}{2} \sqrt{2}\right) \mathrm{N}$ and $\left(2-\frac{1}{2} \sqrt{2}\right) \mathrm{N}$
- **(D)** $\left(2+\frac{1}{2} \sqrt{3}\right) \mathrm{N}$ and $\left(2-\frac{1}{2} \sqrt{3}\right) \mathrm{N}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(2+\frac{1}{2} \sqrt{2}\right) \mathrm{N}$ and $\left(2-\frac{1}{2} \sqrt{2}\right) \mathrm{N}$**

**Detailed Solution:**

$P+Q=4, P^2+Q^2=9 \Rightarrow P=\left(2+\frac{1}{2} \sqrt{2}\right) N$ and $Q=\left(2-\frac{1}{2} \sqrt{2}\right) N$

</details>

---

### Q178. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

A particle is acted upon by constant forces $4 I+J-3 k$ and $3 I+J-k$ which displace it from a point $\hat{i}+2 \hat{j}+3 \hat{k}$ to the point $5 \hat{i}+4 \hat{j}+\hat{k}$. The work done in standard units by the forces is given by

**Options:**

- **(A)** 40
- **(B)** 30
- **(C)** 25
- **(D)** 15

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 40**

**Detailed Solution:**

Work done by the forces $\vec{F}_1$ and $\vec{F}_2$ is $\left(\vec{F}_1+\vec{F}_2\right) \cdot \vec{d}$, where $\vec{d}$ is displacement According to question $\vec{F}_1+\vec{F}_2=(4 \hat{i}+\hat{j}-3 \hat{k})+(3 \hat{i}+\hat{j}-\hat{k})=7 \hat{i}+2 \hat{j}-4 \hat{k}$ and $\vec{d}=(5 \hat{i}+4 \hat{j}+\hat{k})-(\hat{i}+2 \hat{j}+3 \hat{k})=4 \hat{i}+2 \hat{j}-2 \hat{k}$. Hence $\left(\vec{F}_1+\vec{F}_2\right) \cdot \vec{d}$ is 40

</details>

---

### Q179. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

A particle acted on by constant forces $4 \hat{i}+\hat{j}-3 \hat{k}$ and $3 \hat{i}+\hat{j}-\hat{k}$ to the point $5 \hat{i}+4 \hat{j}-\hat{k}$. The total work done by the forces is

**Options:**

- **(A)** 50 units
- **(B)** 20 units
- **(C)** 30 units
- **(D)** 40 units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 40 units**

**Detailed Solution:**

$\overrightarrow{\mathrm{F}}+\overrightarrow{\mathrm{F}}_1+\overrightarrow{\mathrm{F}}_2=7 \mathrm{i}+2 \mathrm{j}-4 \mathrm{k}$
$\overrightarrow{\mathrm{d}}=\mathrm{P} \cdot \mathrm{V}$ of $\overrightarrow{\mathrm{B}}-\mathrm{P} \cdot \mathrm{V}$ of $\overrightarrow{\mathrm{A}}=4 \mathrm{i}+2 \mathrm{j}-2 \mathrm{k}$
$\mathrm{W}=\overrightarrow{\mathrm{F}} \cdot \overrightarrow{\mathrm{d}}=28+4+8=40$ unit

</details>

---

### Q180. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

A couple is of moment $\overrightarrow{\mathrm{G}}$ and the force forming the couple is $\overrightarrow{\mathrm{P}}$. If $\overrightarrow{\mathrm{P}}$ is turned through a right angle the moment of the couple thus formed is $\overrightarrow{\mathrm{H}}$. If instead, the force $\overrightarrow{\mathrm{P}}$ are turned through an angle $\alpha$, then the moment of couple becomes

**Options:**

- **(A)** $\overrightarrow{\mathrm{H}} \sin \alpha-\overrightarrow{\mathrm{G}} \cos \alpha$
- **(B)** $\overrightarrow{\mathrm{G}} \sin \alpha-\overrightarrow{\mathrm{H}} \cos \alpha$
- **(C)** $\overrightarrow{\mathrm{H}} \sin \alpha+\overrightarrow{\mathrm{G}} \cos \alpha$
- **(D)** $\overrightarrow{\mathrm{G}} \sin \alpha+\overrightarrow{\mathrm{H}} \cos \alpha$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\overrightarrow{\mathrm{G}} \sin \alpha-\overrightarrow{\mathrm{H}} \cos \alpha$**

**Detailed Solution:**

$\overrightarrow{\mathrm{a}}=\overrightarrow{\mathrm{r}} \times \overrightarrow{\mathrm{p}} ;|\overrightarrow{\mathrm{a}}|=\mathrm{rp} \sin \theta$
$|\overrightarrow{\mathrm{H}}|=\operatorname{rpcos} \theta \quad\left[\because \sin \left(90^{\circ}+\theta\right)=\cos \theta\right\rfloor$
$\mathrm{G}=\mathrm{rp} \sin \theta$    <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bZ2TMQvs7yvx903HbGehOo03z84s2gZes4IsJKhUDpc.original.fullsize.png">

$\mathrm{H}=\mathrm{rp} \cos \theta$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/oaeImHZfMjatvwKqHOebcDpCsYNWNKqq4JHN5K6GPHM.original.fullsize.png">

$\mathrm{x}=\mathrm{rp} \sin (\theta+\alpha)$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5Q2DxuZaYX-BHM-iis7RZtLZP2jU170OhxaeMOVnVHA.original.fullsize.png">

From (1), (2) \& (3),
$\mathrm{x}=\overrightarrow{\mathrm{a}} \cos \alpha+\overrightarrow{\mathrm{H}} \sin \alpha$

</details>

---

### Q181. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{a} \times \vec{b}=\vec{b} \times \vec{c}=\vec{c} \times \vec{a}$ then $\vec{a}+\vec{b}+\vec{c}=$

**Options:**

- **(A)** abc
- **(B)** -1
- **(C)** 0
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

No Solution Available

</details>

---

### Q182. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `1`

$\vec{a}=3 \hat{i}-5 \hat{j}$ and $\vec{b}=6 \hat{i}+3 \hat{j}$ are two vectors and $\vec{c}$ is a vector such that $\vec{c}=\vec{a} \times \vec{b}$ then
$$
|\vec{a}|:|\vec{b}|:|\vec{c}|
$$

**Options:**

- **(A)** $\sqrt{34}: \sqrt{45}: \sqrt{39}$
- **(B)** $\sqrt{34}: \sqrt{45}: 39$
- **(C)** $34: 39: 45$
- **(D)** $39: 35: 34$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{34}: \sqrt{45}: 39$**

**Detailed Solution:**

We have $\vec{a} \times \vec{b}=39 \vec{k}=\vec{c}$
Also $|\vec{a}|=\sqrt{34},|\vec{b}|=\sqrt{45},|\vec{c}|=39 \therefore \quad|\vec{a}|:|\vec{b}|:|\vec{c}|=\sqrt{34}: \sqrt{45}: 39$

</details>

---

### Q183. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

$3 \lambda \vec{c}+2 \mu(\vec{a} \times \vec{b})=0$ then

**Options:**

- **(A)** $3 \lambda+2 \mu=0$
- **(B)** $3 \lambda=2 \mu$
- **(C)** $\lambda=\mu$
- **(D)** $\lambda+\mu=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 \lambda=2 \mu$**

**Detailed Solution:**

No Solution Available

</details>

---

### Q184. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `1`

If $|a|=5,|b|=4,|c|=3$ thus what will be the value of $|a \cdot b+b . c+c . a|$, given that $\vec{a}+\vec{b}+\vec{c}=0$

**Options:**

- **(A)** 25
- **(B)** 50
- **(C)** -25
- **(D)** -50

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 25**

**Detailed Solution:**

We have, $\vec{a}+\vec{b}+\vec{c}=\overrightarrow{0} \Rightarrow(\vec{a}+\vec{b}+\vec{c})^2=0$
$\Rightarrow|\vec{a}|^2+|\vec{b}|^2+|\vec{c}|^2+2(\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a})=0 \Rightarrow 25+16+9+2(\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a})=0$
$\Rightarrow(\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a})=-25 \quad \therefore|\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a}|=25$

</details>

---

### Q185. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `1`

If $\vec{a}, \vec{b}, \vec{c}$ are vectors such that $\vec{a}+\vec{b}+\vec{c}=0$ and $|\vec{a}|=7,|\vec{b}|=5,|\vec{c}|=3$ then angle between vector $\vec{b}$ and $\vec{c}$ is

**Options:**

- **(A)** $60^{\circ}$
- **(B)** $30^{\circ}$
- **(C)** $45^{\circ}$
- **(D)** $90^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $60^{\circ}$**

**Detailed Solution:**

$\vec{a}+\vec{b}+\vec{c}=0 \Rightarrow \vec{b}+\vec{c}=-\vec{a} \Rightarrow(\vec{b}+\vec{c})^2=(\vec{a})^2=5^2+3^2+2 \vec{b} \vec{c}=7^2$
$\Rightarrow 2|\vec{b}||\vec{c}| \cos \theta=49-34=15 \Rightarrow 2 \times 5 \times 3 \cos \theta=15 \Rightarrow \cos \theta=1 / 2 \Rightarrow \theta=\frac{\pi}{3}=60^{\circ}$

</details>

---

### Q186. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `1`

If $|\vec{a}|=4,|\vec{b}|=2$ and the angle between $\vec{a}$ and $\vec{b}$ is $\pi / 6$ then $(\vec{a} \times \vec{b})^2=2$ is equal to

**Options:**

- **(A)** 48
- **(B)** 16
- **(C)** $\vec{a}$
- **(D)** none of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 16**

**Detailed Solution:**

We have, $\vec{a} \cdot \vec{b}=|\vec{a}||\vec{b}| \cos \frac{\pi}{6}=4 \times 2 \times \frac{\sqrt{3}}{2}=4 \sqrt{3}$
Now, $(\vec{a} \times \vec{b})^2+(\vec{a} \cdot \vec{b})^2=a^2 b^2 \Rightarrow(\vec{a} \times \vec{b})^2+48=16 \times 4 \Rightarrow(\vec{a} \times \vec{b})^2=16$

</details>

---

