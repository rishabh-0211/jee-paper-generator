# JEE Main Mathematics - Vector Algebra

## Topic 1: Algebra of Vectors

**Total Questions:** 79

---

### Q1. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $O$ be the origin, $\vec{OP} = \vec{a}$ and $\vec{OQ} = \vec{b}$. If $R$ is the point on $\vec{OP}$ such that $\vec{OP} = 5\vec{OR}$, and $M$ is the point such that $\vec{OQ} = 5\vec{RM}$, then $\vec{PM}$ is equal to :

**Options:**

- **(A)** $\dfrac{1}{5}(\vec{a} - 4\vec{b})$
- **(B)** $\dfrac{1}{5}(\vec{b} - 4\vec{a})$
- **(C)** $\dfrac{1}{5}(-\vec{a} + 4\vec{b})$
- **(D)** $\dfrac{1}{5}(-\vec{b} + 4\vec{a})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{5}(\vec{b} - 4\vec{a})$**

**Detailed Solution:**

Given $\vec{OP} = \vec{a}$ and $\vec{OQ} = \vec{b}$.

Since $\vec{OP} = 5\vec{OR}$, we have $\vec{OR} = \dfrac{\vec{a}}{5}$.

Also, $\vec{OQ} = 5\vec{RM}$, which gives $\vec{RM} = \dfrac{\vec{b}}{5}$.

The position vector of $M$ is given by $\vec{OM} = \vec{OR} + \vec{RM} = \dfrac{\vec{a}}{5} + \dfrac{\vec{b}}{5}$.

Now, we need to find $\vec{PM}$:

$\vec{PM} = \vec{OM} - \vec{OP}$

$\vec{PM} = \left(\dfrac{\vec{a}}{5} + \dfrac{\vec{b}}{5}\right) - \vec{a}$

$\vec{PM} = \dfrac{\vec{b} - 4\vec{a}}{5} = \dfrac{1}{5}(\vec{b} - 4\vec{a})$

Answer: $\dfrac{1}{5}(\vec{b} - 4\vec{a})$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a} = \sqrt{7}\hat{i} + \hat{j} - \hat{k}$ and $\vec{b} = \hat{j} + 2\hat{k}$. If $\vec{r}$ is a vector such that $\vec{r} \times \vec{a} + \vec{a} \times \vec{b} = \vec{0}$ and $\vec{r} \cdot \vec{a} = 0$, then $|3\vec{r}|^2$ is equal to:

**Options:**

- **(A)** $44$
- **(B)** $54$
- **(C)** $86$
- **(D)** $132$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $44$**

**Detailed Solution:**

Given $\vec{r} \times \vec{a} + \vec{a} \times \vec{b} = \vec{0}$

$\Rightarrow \vec{r} \times \vec{a} - \vec{b} \times \vec{a} = \vec{0}$

$\Rightarrow (\vec{r} - \vec{b}) \times \vec{a} = \vec{0}$

$\Rightarrow \vec{r} - \vec{b} = \lambda \vec{a}$

$\Rightarrow \vec{r} = \vec{b} + \lambda \vec{a}$

Taking dot product with $\vec{a}$ on both sides:

$\vec{r} \cdot \vec{a} = \vec{b} \cdot \vec{a} + \lambda |\vec{a}|^2$

Since $\vec{r} \cdot \vec{a} = 0$, we get:

$\lambda = -\dfrac{\vec{b} \cdot \vec{a}}{|\vec{a}|^2}$

We have $\vec{a} = \sqrt{7}\hat{i} + \hat{j} - \hat{k}$ and $\vec{b} = \hat{j} + 2\hat{k}$.

$\vec{b} \cdot \vec{a} = (0)(\sqrt{7}) + (1)(1) + (2)(-1) = -1$

$|\vec{a}|^2 = (\sqrt{7})^2 + (1)^2 + (-1)^2 = 9$

$|\vec{b}|^2 = (1)^2 + (2)^2 = 5$

Substituting these values:

$\lambda = -\dfrac{-1}{9} = \dfrac{1}{9}$

Therefore, $\vec{r} = \vec{b} + \dfrac{1}{9}\vec{a}$

Squaring both sides:

$|\vec{r}|^2 = |\vec{b}|^2 + \dfrac{1}{81}|\vec{a}|^2 + \dfrac{2}{9}(\vec{b} \cdot \vec{a})$

$|\vec{r}|^2 = 5 + \dfrac{1}{81}(9) + \dfrac{2}{9}(-1)$

$|\vec{r}|^2 = 5 + \dfrac{1}{9} - \dfrac{2}{9} = \dfrac{44}{9}$

Finally, $|3\vec{r}|^2 = 9|\vec{r}|^2 = 9 \times \dfrac{44}{9} = 44$

Answer: $44$

</details>

---

### Q3. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the vectors $\vec{a} = -\hat{i} + \hat{j} + 3\hat{k}$ and $\vec{b} = \hat{i} + 3\hat{j} + \hat{k}$. For some $\lambda, \mu \in \mathbb{R}$, let $\vec{c} = \lambda \vec{a} + \mu \vec{b}$. If $\vec{c} \cdot (3\hat{i} - 6\hat{j} + 2\hat{k}) = 10$ and $\vec{c} \cdot (\hat{i} + \hat{j} + \hat{k}) = -2$, then $|\vec{c}|^2$ is equal to:

**Options:**

- **(A)** $8$
- **(B)** $12$
- **(C)** $14$
- **(D)** $15$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $12$**

**Detailed Solution:**

Given $\vec{a} = -\hat{i} + \hat{j} + 3\hat{k}$ and $\vec{b} = \hat{i} + 3\hat{j} + \hat{k}$.

The vector $\vec{c}$ is given by:
$\vec{c} = \lambda \vec{a} + \mu \vec{b} = (-\lambda + \mu)\hat{i} + (\lambda + 3\mu)\hat{j} + (3\lambda + \mu)\hat{k}$

Using the first condition $\vec{c} \cdot (3\hat{i} - 6\hat{j} + 2\hat{k}) = 10$:
$3(-\lambda + \mu) - 6(\lambda + 3\mu) + 2(3\lambda + \mu) = 10$
$-3\lambda + 3\mu - 6\lambda - 18\mu + 6\lambda + 2\mu = 10$
$-3\lambda - 13\mu = 10 \quad \dots (1)$

Using the second condition $\vec{c} \cdot (\hat{i} + \hat{j} + \hat{k}) = -2$:
$(-\lambda + \mu) + (\lambda + 3\mu) + (3\lambda + \mu) = -2$
$3\lambda + 5\mu = -2 \quad \dots (2)$

Adding equation (1) and equation (2):
$-8\mu = 8 \Rightarrow \mu = -1$

Substituting $\mu = -1$ into equation (2):
$3\lambda + 5(-1) = -2$
$3\lambda = 3 \Rightarrow \lambda = 1$

Substituting the values of $\lambda$ and $\mu$ back into $\vec{c}$:
$\vec{c} = (-(1) + (-1))\hat{i} + (1 + 3(-1))\hat{j} + (3(1) + (-1))\hat{k}$
$\vec{c} = -2\hat{i} - 2\hat{j} + 2\hat{k}$

The magnitude squared of $\vec{c}$ is:
$|\vec{c}|^2 = (-2)^2 + (-2)^2 + 2^2$
$|\vec{c}|^2 = 4 + 4 + 4 = 12$

Answer: $12$

</details>

---

### Q4. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{a}$ and $\vec{b}$ are two vectors such that $|\vec{a}| = 2$ and $|\vec{b}| = 3$, then the maximum value of $3\left|\left(3\vec{a} + 2\vec{b}\right)\right| + 4\left|\left(3\vec{a} - 2\vec{b}\right)\right|$ is :

**Options:**

- **(A)** $30$
- **(B)** $36$
- **(C)** $60$
- **(D)** $72$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $60$**

**Detailed Solution:**

Let $\theta$ be the angle between $\vec{a}$ and $\vec{b}$.

We have $|3\vec{a} + 2\vec{b}| = \sqrt{9|\vec{a}|^2 + 4|\vec{b}|^2 + 12|\vec{a}||\vec{b}|\cos\theta}$

Substituting $|\vec{a}| = 2$ and $|\vec{b}| = 3$:

$|3\vec{a} + 2\vec{b}| = \sqrt{9(4) + 4(9) + 12(2)(3)\cos\theta} = \sqrt{36 + 36 + 72\cos\theta}$

$|3\vec{a} + 2\vec{b}| = \sqrt{72(1+\cos\theta)} = \sqrt{144\cos^2\left(\dfrac{\theta}{2}\right)} = 12\cos\left(\dfrac{\theta}{2}\right)$

Similarly, $|3\vec{a} - 2\vec{b}| = \sqrt{9|\vec{a}|^2 + 4|\vec{b}|^2 - 12|\vec{a}||\vec{b}|\cos\theta}$

$|3\vec{a} - 2\vec{b}| = \sqrt{36 + 36 - 72\cos\theta} = \sqrt{72(1-\cos\theta)} = \sqrt{144\sin^2\left(\dfrac{\theta}{2}\right)} = 12\sin\left(\dfrac{\theta}{2}\right)$

The given expression becomes:

$3|3\vec{a} + 2\vec{b}| + 4|3\vec{a} - 2\vec{b}| = 3\left(12\cos\left(\dfrac{\theta}{2}\right)\right) + 4\left(12\sin\left(\dfrac{\theta}{2}\right)\right)$

$= 36\cos\left(\dfrac{\theta}{2}\right) + 48\sin\left(\dfrac{\theta}{2}\right)$

The maximum value of $A\cos x + B\sin x$ is $\sqrt{A^2 + B^2}$.

Maximum value $= \sqrt{36^2 + 48^2} = \sqrt{1296 + 2304} = \sqrt{3600} = 60$

Answer: $60$

</details>

---

### Q5. JEE Main 2026 (28 January Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $P Q R$ be a triangle such that $\overrightarrow{P Q}=-2 \hat{i}-\hat{j}+2 \hat{k}$ and $\overrightarrow{\mathrm{PR}}=a \hat{\mathrm{i}}+b \hat{\mathrm{j}}-4 \hat{\mathrm{k}}, a, b \in \mathbb{Z}$. Let S be the point on QR, which is equidistant from the lines PQ and PR. If $|\overrightarrow{\mathrm{PR}}|=9$ and $\overrightarrow{\mathrm{PS}}=\hat{\mathrm{i}}-7 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}$, then the value of $3 a-4 b$ is $\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **37**

**Detailed Solution:**

Given: $\vec{PQ} = -2\hat{i} - \hat{j} + 2\hat{k}$, $\vec{PR} = a\hat{i} + b\hat{j} - 4\hat{k}$ ($a, b \in \mathbb{Z}$), $\vec{PS} = \hat{i} - 7\hat{j} + 2\hat{k}$, $|\vec{PR}| = 9$
From $|\vec{PR}| = 9$: $a^2 + b^2 + 16 = 81 \Rightarrow a^2 + b^2 = 65$ ...(1)
Since S is on QR equidistant from lines PQ and PR, PS is the angle bisector. So:
$\cos\theta = \frac{\vec{PQ} \cdot \vec{PS}}{|\vec{PQ}||\vec{PS}|} = \frac{-2+7+4}{3 \cdot 3\sqrt{6}} = \frac{9}{9\sqrt{6}} = \frac{1}{\sqrt{6}}$
Similarly: $\frac{1}{\sqrt{6}} = \frac{\vec{PS} \cdot \vec{PR}}{|\vec{PS}||\vec{PR}|} = \frac{a - 7b - 8}{3\sqrt{6} \cdot 9}$
$a - 7b = 35$ ...(2)
From (1) and (2): $a = 7, b = -4$
$3a - 4b = 21 + 16 = 37$ (NTA Answer)
However, $\vec{QS} = 3\hat{i} - 6\hat{j}$ and $\vec{SR} = 6\hat{i} + 3\hat{j} - 6\hat{k}$ are not parallel, so Q, S, R are not collinear. Also $\cos\theta = \frac{2\sqrt{2}}{\sqrt{3}} > 1$, which is impossible. Hence no such triangle exists.
So, this should be a bonus question.

</details>

---

### Q6. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=2 \hat{\mathrm{i}}-\hat{\mathrm{j}}-\hat{\mathrm{k}}, \vec{b}=\hat{\mathrm{i}}+3 \hat{\mathrm{j}}-\hat{\mathrm{k}}$ and $\vec{c}=2 \hat{\mathrm{i}}+\hat{\mathrm{j}}+3 \hat{\mathrm{k}}$. Let $\vec{v}$ be the vector in the plane of the vectors $\vec{a}$ and $\vec{b}$, such that the length of its projection on the vector $\vec{c}$ is $\frac{1}{\sqrt{14}}$. Then $|\vec{v}|$ is equal to

**Options:**

- **(A)** 13
- **(B)** $\frac{\sqrt{35}}{2}$
- **(C)** $\frac{\sqrt{21}}{2}$
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\sqrt{35}}{2}$**

**Detailed Solution:**

$\vec{v} = \lambda\vec{a} + \mu\vec{b} = (2\lambda+\mu,\ -\lambda+3\mu,\ -\lambda-\mu)$.
$\vec{v} \cdot \vec{c} = 2(2\lambda+\mu) + (-\lambda+3\mu) + 3(-\lambda-\mu) = 2\mu$.
$|\vec{c}| = \sqrt{4+1+9} = \sqrt{14}$.
Projection length $= \frac{|2\mu|}{\sqrt{14}} = \frac{1}{\sqrt{14}} \Rightarrow |\mu| = \frac{1}{2}$.
$|\vec{v}|^2 = 6\lambda^2 + 11\mu^2 = 6(1) + \frac{11}{4} = \frac{35}{4}$.
$|\vec{v}| = \frac{\sqrt{35}}{2}$.

</details>

---

### Q7. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}$ and $\vec{b}$ be the vectors of the same magnitude such that $\frac{|\vec{a}+\vec{b}|+|\vec{a}-\vec{b}|}{|\vec{a}+\vec{b}|-|\vec{a}-\vec{b}|}=\sqrt{2}+1$. Then $\frac{|\vec{a}+\vec{b}|^2}{|\vec{a}|^2}$ is :

**Options:**

- **(A)** $2+4 \sqrt{2}$
- **(B)** $1+\sqrt{2}$
- **(C)** $2+\sqrt{2}$
- **(D)** $4+2 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2+\sqrt{2}$**

**Detailed Solution:**

$\frac{|\bar{a}+\bar{b}|+|\bar{a}-\bar{b}|}{|\bar{a}+\bar{b}|-|\bar{a}-\bar{b}|}=\sqrt{2}+1$
Apply componendo and dividendo
$\begin{aligned}
& \Rightarrow \frac{2|\overline{\mathrm{a}}+\overline{\mathrm{b}}|}{2|\overline{\mathrm{a}}-\overline{\mathrm{b}}|}=\frac{\sqrt{2}+2}{\sqrt{2}} \\
& \Rightarrow|\overline{\mathrm{a}}+\overline{\mathrm{b}}|=(1+\sqrt{2})|\overline{\mathrm{a}}-\overline{\mathrm{b}}| \\
& \Rightarrow|\overline{\mathrm{a}}+\overline{\mathrm{b}}|^2=(3+2 \sqrt{2})|\overline{\mathrm{a}}-\overline{\mathrm{b}}|^2 \\
& \Rightarrow 2|\overline{\mathrm{a}}|^2+2 \overline{\mathrm{a}} \cdot \overline{\mathrm{~b}}=(3+2 \sqrt{2})\left(2|\overline{\mathrm{a}}|^2-2 \overline{\mathrm{a}} \cdot \overline{\mathrm{~b}}\right) \\
& \Rightarrow 2|\overline{\mathrm{a}}|^2(2+2 \sqrt{2})=2 \overline{\mathrm{a}} \cdot \overline{\mathrm{~b}}(4+2 \sqrt{2}) \\
& \Rightarrow \frac{\overline{\mathrm{a}} \cdot \overline{\mathrm{~b}}}{|\overline{\mathrm{a}}|^2}=\frac{2+2 \sqrt{2}}{4+2 \sqrt{2}}=\frac{1}{\sqrt{2}}
\end{aligned}$
Now
$\begin{aligned}
& \frac{|\overline{\mathrm{a}}+\overline{\mathrm{b}}|^2}{|\overline{\mathrm{a}}|^2}=1+\frac{|\overline{\mathrm{b}}|^2}{|\overline{\mathrm{a}}|^2}+\frac{2 \overline{\mathrm{a}} \cdot \overline{\mathrm{~b}}}{|\overline{\mathrm{a}}|^2} \\
& =1+1+2\left(\frac{1}{\sqrt{2}}\right)=2+\sqrt{2}
\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (4 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the three sides of a triangle $A B C$ be given by the vectors $2 \hat{i}-\hat{j}+\hat{k}, \quad \hat{i}-3 \hat{j}-5 \hat{k}$ and $3 \hat{i}-4 \hat{j}-4 \hat{k}$. Let $G$ be the centroid of the triangle $A B C$. Then $6\left(|\overrightarrow{\mathrm{AG}}|^2+|\overrightarrow{\mathrm{BG}}|^2+|\overrightarrow{\mathrm{CG}}|^2\right)$ is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **164**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7JdYavacHxYfQ2UaXjpapRMmkiDkf0paaYeZxTOBmfA.original.fullsize.png"/>
By given data
$\overrightarrow{\mathrm{AB}}+\overrightarrow{\mathrm{AC}}=\overrightarrow{\mathrm{CB}}$
Let pv of $\overrightarrow{\mathrm{A}}$ are $\overrightarrow{\mathrm{O}}$ then
$\overrightarrow{\mathrm{AB}}=\overrightarrow{\mathrm{B}}-\overrightarrow{\mathrm{A}}$
i.e. $p v$ of $\overrightarrow{\mathrm{B}}-=2 \hat{\mathrm{i}}-\hat{\mathrm{j}}+\hat{\mathrm{k}}$
$\overrightarrow{\mathrm{CA}}=\overrightarrow{\mathrm{A}}-\overrightarrow{\mathrm{C}}$
i.e. pv of $\overrightarrow{\mathrm{C}}=-(\hat{\mathrm{i}}-3 \hat{\mathrm{j}}-5 \hat{\mathrm{k}})$
Now pv of centroid
$\begin{aligned}
& (\overrightarrow{\mathrm{G}})-=\frac{\overrightarrow{\mathrm{A}}+\overrightarrow{\mathrm{B}}+\overrightarrow{\mathrm{C}}}{3}=\frac{\overrightarrow{0}+(2,-1,1)+(-1,3,5)}{3} \\
& \overrightarrow{\mathrm{G}}=\frac{1}{3}(\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+6 \hat{\mathrm{k}})
\end{aligned}$
Now $\overrightarrow{\mathrm{AG}}=\frac{1}{3}(\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+6 \hat{\mathrm{k}})$
$\Rightarrow|\overrightarrow{\mathrm{AG}}|^2=\frac{1}{9} \times 41$
$\overrightarrow{\mathrm{BG}}=\left(\frac{1}{3}-2\right) \hat{\mathrm{i}}+\left(\frac{2}{3}+1\right) \hat{\mathrm{j}}+(2-1) \hat{\mathrm{k}}$
$\Rightarrow|\overrightarrow{\mathrm{BG}}|^2=\frac{59}{9}$
$\begin{aligned}
& \overrightarrow{\mathrm{CG}}=\left(\frac{1}{3}+1\right) \hat{\mathrm{i}}+\left(\frac{2}{3}-3\right) \hat{\mathrm{j}}+(2-5) \hat{\mathrm{k}} \\
& \Rightarrow|\overrightarrow{\mathrm{CG}}|^2=\frac{146}{9}
\end{aligned}$
Now
$\begin{aligned}
& 6\left[|\overrightarrow{\mathrm{AG}}|^2+|\overrightarrow{\mathrm{BG}}|^2+|\overrightarrow{\mathrm{CG}}|^2\right]=6 \times\left[\frac{41}{9}+\frac{59}{9}+\frac{146}{9}\right] \\
& =6 \times \frac{246}{9}=164
\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let A, B, C be three points in $x y$-plane, whose position vector are given by $\sqrt{3} \hat{i}+\hat{j}, \hat{i}+\sqrt{3} \hat{j}$ and $\mathrm{a} \hat{i}+(1-\mathrm{a}) \hat{j}$ respectively with respect to the origin O . If the distance of the point C from the line bisecting the angle between the vectors $\overrightarrow{\mathrm{OA}}$ and $\overrightarrow{\mathrm{OB}}$ is $\frac{9}{\sqrt{2}}$, then the sum of all the possible values of $a$ is :

**Options:**

- **(A)** $2$
- **(B)** $9 / 2$
- **(C)** $1$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

Equation of line in the internal bisector of $O \dot{A}$ and $O B$ is $(\sqrt{3}+1) \hat{i}+(\sqrt{3}+1) \hat{j}$
$\Rightarrow$ line will be $y=x \Rightarrow x-y=0$
$D=\left|\frac{a-(1-a)}{\sqrt{a^2+(1-a)^2}}\right|=\frac{9}{\sqrt{2}}$
$\begin{aligned} & (2 a-1)^2=\frac{81}{2}\left(a^2+(1-a)^2\right) \\ & \Rightarrow 2\left(4 a^2-4 a+1\right)=81 a^2+81 a^2-162 a-81 \\ & \Rightarrow 162 a^2-162 a+81-8 a^2+8 a-2=0 \\ & \Rightarrow 154 a^2-154 a+79=0 \\ & \text { Sum of values }=-\frac{(-154)}{154}=1\end{aligned}$

</details>

---

### Q10. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=\hat{i}+2 \hat{j}+3 \hat{k}, \vec{b}=3 \hat{i}+\hat{j}-\hat{k}$ and $\vec{c}$ be three vectors such that $\vec{c}$ is coplanar with $\vec{a}$ and $\vec{b}$. If the vector $\vec{C}$ is perpendicular to $\vec{b}$ and $\vec{a} \cdot \vec{c}=5$, then $|\vec{c}|$ is equal to

**Options:**

- **(A)** $\sqrt{\frac{11}{6}}$
- **(B)** $\frac{1}{3 \sqrt{2}}$
- **(C)** $16$
- **(D)** $18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{\frac{11}{6}}$**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{\mathrm{c}}=\lambda(\overrightarrow{\mathrm{b}} \times(\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}})) \\ & =\lambda((\overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{b}}) \overrightarrow{\mathrm{a}}-(\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{b}}) \overrightarrow{\mathrm{b}}) \\ & =\lambda(11 \overrightarrow{\mathrm{a}}-2 \overrightarrow{\mathrm{~b}})=\lambda(11 \mathrm{i}+22 \mathrm{j}+33 \mathrm{k}-6 \mathrm{i}-2 \mathrm{j}+2 \mathrm{k}) \\ & =\lambda(5 \mathrm{i}+20 \mathrm{j}+35 \mathrm{k}) \\ & =5 \lambda(5 \mathrm{i}+4 \mathrm{j}+7 \mathrm{k}) \\ & =\text { Given } \overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{a}}=5 \\ & =5 \lambda(1+8+21)=5 \quad=\lambda=\frac{1}{30} \\ & \Rightarrow \overrightarrow{\mathrm{c}}=\frac{1}{6}(\mathrm{i}+4 \mathrm{j}+7 \mathrm{k}) \\ & \overrightarrow{\mathrm{c}}=\frac{\sqrt{1+16+49}}{6}=\sqrt{\frac{11}{6}}\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let the position vectors of the vertices $A, B$ and $C$ of a tetrahedron $A B C D$ be $\hat{\mathbf{i}}+2 \hat{\mathbf{j}}+\hat{\mathbf{k}}, \hat{\mathbf{i}}+3 \hat{\mathbf{j}}-2 \hat{k}$ and $2 \hat{i}+\hat{j}-\hat{k}$ respectively. The altitude from the vertex $D$ to the opposite face $A B C$ meets the median line segment through $A$ of the triangle $A B C$ at the point $E$. If the length of $A D$ is $\frac{\sqrt{110}}{3}$ and the volume of the tetrahedron is $\frac{\sqrt{805}}{6 \sqrt{2}}$, then the position vector of $E$ is

**Options:**

- **(A)** $\frac{1}{12}(7 \hat{\mathbf{i}}+4 \hat{\mathbf{j}}+3 \hat{k})$
- **(B)** $\frac{1}{2}(\hat{i}+4 \hat{j}+7 \hat{k})$
- **(C)** $\frac{1}{6}(12 \hat{i}+12 \hat{j}+\hat{k})$
- **(D)** $\frac{1}{6}(7 \hat{\mathrm{i}}+12 \hat{\mathrm{j}}+\hat{\mathrm{k}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{6}(7 \hat{\mathrm{i}}+12 \hat{\mathrm{j}}+\hat{\mathrm{k}})$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6edpIRzoaNdW56a2qD2o3bkEs4chCEyxBbuQPYMkN9Y.original.fullsize.png">




Area of $\triangle \mathrm{ABC}=\frac{1}{2}|\overrightarrow{\mathrm{AB}} \times \overrightarrow{\mathrm{AC}}|$
$=\frac{1}{2}|5 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+\hat{\mathrm{k}}|=\frac{1}{2} \sqrt{35}$
volume of tetrahedron
$\begin{aligned}
& =\frac{1}{3} \times \text { Base area } \times \mathrm{h}=\frac{\sqrt{805}}{6 \sqrt{2}} \\
& \frac{1}{3} \times \frac{1}{2} \sqrt{35} \times \mathrm{h}=\frac{\sqrt{805}}{6 \sqrt{2}} \\
& \mathrm{~h}=\sqrt{\frac{23}{2}}
\end{aligned}$
$\mathrm{AE}^2=\mathrm{AD}^2-\mathrm{DE}^2=\frac{13}{18} \therefore \mathrm{AE}=\sqrt{\frac{13}{18}}$

$\begin{aligned} & \overrightarrow{\mathrm{AE}}=|\mathrm{AE}| \cdot\left(\frac{\hat{\mathrm{i}}-5 \hat{\mathrm{k}}}{\sqrt{26}}\right) \\ & =\sqrt{\frac{13}{18}} \cdot\left(\frac{\hat{\mathrm{i}}-5 \hat{\mathrm{k}}}{\sqrt{26}}\right) \\ & =\sqrt{\frac{13}{18}} \cdot\left(\frac{\hat{\mathrm{i}}-5 \hat{\mathrm{k}}}{\sqrt{26}}\right)=\frac{\hat{\mathrm{i}}-5 \hat{\mathrm{k}}}{6} \\ & \text { P.V. of } \mathrm{E}=\frac{\hat{\mathrm{i}}-5 \hat{\mathrm{k}}}{6}+\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+\hat{\mathrm{k}}=\frac{1}{6}(7 \hat{\mathrm{i}}+12 \hat{\mathrm{j}}+\hat{\mathrm{k}})\end{aligned}$

</details>

---

### Q12. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}$ and $\vec{b}$ be two unit vectors such that the angle between them is $\frac{\pi}{3}$. If $\lambda \vec{a}+2 \vec{b}$ and $3 \vec{a}-\lambda \vec{b}$ are perpendicular to each other, then the number of values of $\lambda$ in $[-1,3]$ is :

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** 0
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

$\begin{aligned} & \hat{a} \cdot \hat{b}=\frac{1}{2} \\ & \text { Now }(\lambda \hat{a}+2 \hat{b}) \cdot(3 \hat{a}-\lambda \hat{b})=0 \\ & 3 \lambda \hat{a} \cdot \hat{a}-\lambda^2 \hat{a} \cdot \hat{b}+6 \hat{a} \cdot \hat{b}-2 \lambda \hat{b} \cdot \hat{b}=0 \\ & 3 \lambda-\frac{\lambda^2}{2}+3-2 \lambda=0 \\ & \lambda^2-2 \lambda-6=0 \\ & \lambda=1 \pm \sqrt{7} \\ & \Rightarrow \text { number of values }=0\end{aligned}$

</details>

---

### Q13. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\overrightarrow{\mathrm{a}}=\hat{i}+2 \hat{j}+3 \hat{k}, \overrightarrow{\mathrm{b}}=2 \hat{i}+3 \hat{j}-5 \hat{k}$ and $\overrightarrow{\mathrm{c}}=3 \hat{i}-\hat{j}+\lambda \hat{k}$ be three vectors. Let $\overrightarrow{\mathrm{r}}$ be anit vector along $\vec{b}+\vec{c}$. If $\vec{r} \cdot \vec{a}=3$, then $3 \lambda$ is equal to:

**Options:**

- **(A)** 21
- **(B)** 30
- **(C)** 25
- **(D)** 27

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 25**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{\mathrm{r}}=\mathrm{k}(\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}}) \\ & \overrightarrow{\mathrm{r}} \cdot \overrightarrow{\mathrm{a}}=3 \\ & \overrightarrow{\mathrm{r}} \cdot \overrightarrow{\mathrm{a}}=\mathrm{k}(\overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{a}}) \\ & 3=\mathrm{k}(2+6-15+3-2+3 \lambda)\end{aligned}$
$3=\mathrm{k}(-6+3 \lambda)$   ...(1)
$\overrightarrow{\mathrm{r}}=\mathrm{k}(5 \hat{\mathrm{i}}+2 \hat{\mathrm{j}}-(5-\lambda) \hat{\mathrm{k}})$
$|\vec{r}|=k \sqrt{25+4+25+\lambda^2-10 \lambda}=1$   ...(2)
$\mathrm{k}=\frac{3}{-6+3 \lambda}=\frac{1}{-2+\lambda} \quad$ put in (2)
$\begin{aligned} & 4+\lambda^2-4 \lambda=54+\lambda^2-10 \lambda \\ & 6 \lambda=50 \\ & 3 \lambda=25\end{aligned}$

</details>

---

### Q14. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=4 \hat{i}-\hat{j}+\hat{k}, \vec{b}=11 \hat{i}-\hat{j}+\hat{k}$ and $\vec{c}$ be a vector such that $(\vec{a}+\vec{b}) \times \vec{c}=\vec{c} \times(-2 \vec{a}+3 \vec{b})$. If $(2 \vec{a}+3 \vec{b}) \cdot \vec{c}=1670$, then $|\vec{c}|^2$ is equal to :

**Options:**

- **(A)** 1609
- **(B)** 1618
- **(C)** 1600
- **(D)** 1627

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1618**

**Detailed Solution:**

$\begin{aligned} & (\overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{b}}) \times \overrightarrow{\mathrm{c}}-\overrightarrow{\mathrm{c}} \times(-2 \overrightarrow{\mathrm{a}}+3 \overrightarrow{\mathrm{b}})=0 \\ & (\overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{b}}) \times \overrightarrow{\mathrm{c}}+(-2 \overrightarrow{\mathrm{a}}+3 \overrightarrow{\mathrm{b}}) \times \overrightarrow{\mathrm{c}}=0 \\ & \Rightarrow(\overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{b}})-2 \overrightarrow{\mathrm{a}}+3 \overrightarrow{\mathrm{b}}) \times \overrightarrow{\mathrm{c}}=0 \\ & \Rightarrow \overrightarrow{\mathrm{c}}=\lambda(4 \overrightarrow{\mathrm{b}}-\overrightarrow{\mathrm{a}}) \\ & \Rightarrow=\lambda(44 \hat{\mathrm{i}}-4 \hat{\mathrm{j}}+4 \hat{\mathrm{k}}-4 \hat{\mathrm{i}}+\hat{\mathrm{j}}-\hat{\mathrm{k}}) \\ & =\lambda(40 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+3 \hat{\mathrm{k}})\end{aligned}$
Now
$\begin{aligned}
& (8 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+2 \hat{\mathrm{k}}+33 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}) \cdot \lambda(40 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+3 \hat{\mathrm{k}})=1670 \\
& \Rightarrow(41 \hat{\mathrm{i}}-5 \hat{\mathrm{j}}+5 \hat{\mathrm{k}}) \cdot(40 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}) \times \lambda=1670) \\
& \Rightarrow(1640+15+15) \lambda=1670 \Rightarrow \lambda=1 \\
& \text { so } \overrightarrow{\mathrm{c}}=40 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}-3 \hat{\mathrm{k}} \\
& \Rightarrow|\overrightarrow{\mathrm{c}}|^2=1600+9+9=1618
\end{aligned}$

</details>

---

### Q15. JEE Main 2024 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $\vec{a}=9 \hat{i}-13 \hat{j}+25 \hat{k}, \vec{b}=3 \hat{i}+7 \hat{j}-13 \hat{k}$ and $\vec{c}=17 \hat{i}-2 \hat{j}+\hat{k}$ be three given vectors. If $\vec{r}$ is a vector such that $\vec{r} \times \vec{a}=(\vec{b}+\vec{c}) \times \vec{a}$ and $\vec{r} \cdot(\vec{b}-\vec{c})=0$, then $\frac{|593 \vec{r}+67 \vec{a}|^2}{(593)^2}$ is equal to___________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **569**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{\mathrm{a}}=9 \hat{\mathrm{i}}-13 \hat{\mathrm{j}}+25 \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{b}}=3 \hat{\mathrm{i}}+7 \hat{\mathrm{j}}-13 \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{c}}=17 \hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}}=20 \hat{\mathrm{i}}+5 \hat{\mathrm{j}}-12 \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{b}}-\overrightarrow{\mathrm{c}}=-14 \hat{\mathrm{i}}+9 \hat{\mathrm{j}}-14 \hat{\mathrm{k}} \\ & (\overrightarrow{\mathrm{r}}-(\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}}))_{\times \mathrm{a}}=0 \\ & \mathrm{r}-(\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}})=\lambda \overrightarrow{\mathrm{a}} \\ & \overrightarrow{\mathrm{r}}=\lambda \overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}} \\ & \text { But } \overrightarrow{\mathrm{r}} \cdot(\overrightarrow{\mathrm{b}}-\overrightarrow{\mathrm{c}})=0 \\ & \Rightarrow(\lambda \overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}}) \cdot(\overrightarrow{\mathrm{b}}-\overrightarrow{\mathrm{c}})=0 \\ & \Rightarrow \lambda \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{b}}-\lambda \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{c}}-\overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{c}}-\overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{c}}=0 \\ & \lambda=\frac{\overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{c}}-\overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{b}}}{\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{b}}-\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{c}}}=\frac{294-227}{-389=204}=\frac{-67}{593} \\ & \therefore \overrightarrow{\mathrm{r}}=\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}}-\frac{67}{593} \overrightarrow{\mathrm{a}} \\ & \Rightarrow 593 \overrightarrow{\mathrm{r}}+67 \overrightarrow{\mathrm{a}}=593(\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}}) \\ & \Rightarrow|\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}}|^2=569\end{aligned}$

</details>

---

### Q16. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\overrightarrow{\mathrm{a}}=6 \hat{i}+\hat{j}-\hat{k}$ and $\overrightarrow{\mathrm{b}}=\hat{i}+\hat{j}$. If $\overrightarrow{\mathrm{c}}$ is a is vector such that $|\overrightarrow{\mathrm{c}}| \geq 6, \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{c}}=6|\overrightarrow{\mathrm{c}}|,|\overrightarrow{\mathrm{c}}-\overrightarrow{\mathrm{a}}|=2 \sqrt{2}$ and the angle between $\vec{a} \times \vec{b}$ and $\vec{c}$ is $60^{\circ}$, then $|(\vec{a} \times \vec{b}) \times \vec{c}|$ is equal to:

**Options:**

- **(A)** $\frac{9}{2}(6-\sqrt{6})$
- **(B)** $\frac{3}{2} \sqrt{6}$
- **(C)** $\frac{9}{2}(6+\sqrt{6})$
- **(D)** $\frac{3}{2} \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{9}{2}(6+\sqrt{6})$**

**Detailed Solution:**

$\begin{aligned} & |(\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}} \times \overrightarrow{\mathrm{c}})|=|\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}||\overrightarrow{\mathrm{c}}| \frac{\sqrt{3}}{2} \\ & |\overrightarrow{\mathrm{c}}-\overrightarrow{\mathrm{a}}|=2 \sqrt{2} \\ & |\mathrm{c}|^2+|\mathrm{a}|^2-2 \overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{a}}=8 \\ & |\mathrm{z}|^2+38-12|\mathrm{z}|=8 \\ & |\mathrm{z}|^2-12|\mathrm{z}|+30=0 \\ & |\mathrm{z}|=\frac{12 \pm \sqrt{144-120}}{2} \\ & =\frac{12 \pm 2 \sqrt{6}}{2}\end{aligned}$
$\begin{aligned} & |z|=6+\sqrt{6} \\ & \overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}=\left|\begin{array}{ccc}\hat{\ell} & \hat{\mathrm{j}} & \hat{\mathrm{k}} \\ 6 & 1 & -1 \\ 1 & 1 & 0\end{array}\right| \\ & \hat{\ell}-\hat{\mathrm{j}}+5 \hat{\mathrm{k}} \\ & |\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}|=\sqrt{27} \\ & |(\overrightarrow{\mathrm{a}} \times \mathrm{b}) \times \mathrm{z}|=\sqrt{27}(6+\sqrt{6}) \frac{\sqrt{3}}{2} \\ & \frac{9}{2}(6+\sqrt{6})\end{aligned}$

</details>

---

### Q17. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\overrightarrow{\mathrm{a}}=2 \hat{i}+\hat{j}-\hat{k}, \overrightarrow{\mathrm{b}}=((\overrightarrow{\mathrm{a}} \times(\hat{i}+\hat{j})) \times \hat{i}) \times \hat{i}$. Then the square of the projection of $\overrightarrow{\mathrm{a}}$ on $\overrightarrow{\mathrm{b}}$ is :

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{2}{3}$
- **(C)** 2
- **(D)** $\frac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

$\begin{aligned} & \vec{a} \times(\hat{i}+\hat{j})=\left|\begin{array}{ccc}\hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & -1 \\ 1 & 1 & 0\end{array}\right| \\ & =\hat{i}-\hat{j}+\hat{k} \\ & (\vec{a} \times(\hat{i} \times \hat{j})) \times \hat{i}=\hat{k}+\hat{j} \\ & ((\vec{a} \times(\hat{i} \times \hat{j})) \times i) \times \hat{i}=\hat{j}-\hat{k} \\ & \operatorname{projection} \text { of } \vec{a} \text { on } \hat{b}=\frac{\vec{a} \cdot \vec{b}}{|\vec{b}|} \\ & =\frac{1+1}{\sqrt{2}}=\sqrt{2}\end{aligned}$

</details>

---

### Q18. JEE Main 2024 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $\vec{a}=2 \hat{i}-3 \hat{j}+4 \hat{k}, \vec{b}=3 \hat{i}+4 \hat{j}-5 \hat{k}$ and a vector $\vec{c}$ be such that $\vec{a} \times(\vec{b}+\vec{c})+\vec{b} \times \vec{c}=\hat{i}+8 \hat{j}+13 \hat{k}$. If $\vec{a} \cdot \vec{c}=13$, then $(24-\vec{b} \cdot \vec{c})$ is equal to_______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **46**

**Detailed Solution:**

$\begin{aligned} & \vec{a} \times \vec{b}+\vec{a} \times \vec{c}+\vec{b} \times \vec{c}=(1,8,13) \\ & \vec{a} \times(\vec{a} \times \vec{b})+\vec{a} \times(\vec{a} \times \vec{c})+\vec{a} \times(\vec{b} \times \vec{c}) \\ & =\vec{a} \times(\hat{i}+8 \hat{j}+13 \hat{k})\end{aligned}$
$\begin{aligned} & (\vec{a} \cdot \vec{b}) \vec{a}-a^2 \vec{b}+(\vec{a} \cdot \vec{c}) \vec{a}-a^2 \vec{c}+(\vec{a} \cdot \vec{c}) \vec{b}-(\vec{a} \cdot \vec{b}) \vec{c}=\vec{a} \times(\hat{i}+8 \hat{j}+13 \hat{k}) \\ & \Rightarrow-26 \vec{a}-29 \vec{b}+13 \vec{a}-29 \vec{c}+13 \vec{b}+26 \vec{c}=\vec{a} \times(\hat{i}+8 \hat{j}+13 \hat{k})\end{aligned}$
$\begin{aligned}
& \Rightarrow \quad-13 \overrightarrow{\mathrm{a}}-16 \overrightarrow{\mathrm{b}}-3 \overrightarrow{\mathrm{c}}=\overrightarrow{\mathrm{a}} \times(\hat{\mathrm{i}}+8 \hat{\mathrm{j}}+13 \hat{\mathrm{k}}) \\
& \Rightarrow \quad-13 \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{b}}-16 \mathrm{~b}^2-3 \overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{c}}=\{\overrightarrow{\mathrm{a}} \times(\hat{\mathrm{i}}+8 \hat{\mathrm{j}}+13 \hat{\mathrm{k}})\} \cdot \overrightarrow{\mathrm{b}} \\
& \Rightarrow \quad(-13)(-26)-16(50)-3 \overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{c}}=\left|\begin{array}{ccc}
2 & -3 & 4 \\
1 & 8 & 13 \\
3 & 4 & -5
\end{array}\right| \\
& \Rightarrow \quad-462-3 \overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{c}}=-396 \\
& \Rightarrow \quad \overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{c}}=-22
\end{aligned}$
Hence $24-\vec{b} \cdot \vec{c}=46$

</details>

---

### Q19. JEE Main 2024 (05 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $\overrightarrow{\mathrm{a}}=\hat{i}-3 \hat{j}+7 \hat{k}, \overrightarrow{\mathrm{b}}=2 \hat{i}-\hat{j}+\hat{k}$ and $\overrightarrow{\mathrm{c}}$ be a vector such that $(\overrightarrow{\mathrm{a}}+2 \overrightarrow{\mathrm{b}}) \times \overrightarrow{\mathrm{c}}=3(\overrightarrow{\mathrm{c}} \times \overrightarrow{\mathrm{a}})$. If $\vec{a} \cdot \vec{c}=130$, then $\vec{b} \cdot \vec{c}$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

$\begin{aligned} & (\overrightarrow{\mathrm{a}}+2 \overrightarrow{\mathrm{b}}) \times \overrightarrow{\mathrm{c}}=3(\overrightarrow{\mathrm{c}} \times \overrightarrow{\mathrm{a}}) \\ & (2 \overrightarrow{\mathrm{b}}+4 \overrightarrow{\mathrm{a}}) \times \overrightarrow{\mathrm{c}}=0 \\ & \overrightarrow{\mathrm{c}}=\lambda(4 \overrightarrow{\mathrm{a}}+2 \overrightarrow{\mathrm{b}})=\lambda(8 \hat{\mathrm{i}}-14 \hat{\mathrm{j}}+30 \hat{\mathrm{k}}) \\ & \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{c}}=130 \\ & 8 \lambda+42 \lambda+210 \lambda=130 \\ & \lambda=\frac{1}{2} \\ & \overrightarrow{\mathrm{c}}=4 \hat{\mathrm{i}}-7 \hat{\mathrm{j}}+15 \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{c}}=8+7+15=30\end{aligned}$

</details>

---

### Q20. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For $\lambda>0$, let $\theta$ be the angle between the vectors $\vec{a}=\hat{i}+\lambda \hat{j}-3 \hat{k}$ and $\vec{b}=3 \hat{i}-\hat{j}+2 \hat{k}$. If the vectors $\vec{a}+\vec{b}$ and $\vec{a}-\vec{b}$ are mutually perpendicular, then the value of (14 cos $\theta)^2$ is equal to

**Options:**

- **(A)** 50
- **(B)** 40
- **(C)** 25
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 25**

**Detailed Solution:**

$\begin{aligned} & (\vec{a}+\vec{b}) \cdot(\vec{a}-\vec{b})=0, \lambda>0 \\ & |\vec{a}|^2-|\vec{b}|^2=0 \rightarrow 1+\lambda^2+9=9+1+4 \\ & \therefore \lambda=2, \cos \theta=\frac{\vec{a}-\vec{b}}{|\vec{a}| \cdot|\vec{b}|}=\frac{3-\lambda-6}{\sqrt{14} \cdot \sqrt{14}} \\ & 14 \cos \theta=3-8=-5 \\ & \therefore(14 \cos \theta)^2=25\end{aligned}$

</details>

---

### Q21. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=\hat{i}+\hat{j}+\hat{k}, \vec{b}=2 \hat{i}+4 \hat{j}-5 \hat{k}$ and $\vec{c}=x \hat{i}+2 \hat{j}+3 \hat{k}, x \in \mathbb{R}$.
If $\vec{d}$ is the unit vector in the direction of $\vec{b}+\vec{c}$ such that $\vec{a} \cdot \vec{d}=1$, then $(\vec{a} \times \vec{b}) \cdot \vec{c}$ is equal to

**Options:**

- **(A)** 11
- **(B)** 3
- **(C)** 9
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 11**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{\mathrm{d}}=\lambda(\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}}) \\ & \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{d}}=\lambda(\overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{a}}+\overrightarrow{\mathrm{c}} \cdot \overrightarrow{\mathrm{a}}) \\ & 1=\lambda(1+\mathrm{x}+5)\end{aligned}$
$1=\lambda(x+6)$ ...(1)
$\begin{aligned}
& |\overrightarrow{\mathrm{d}}|=1 \\
& |\lambda(\overrightarrow{\mathrm{b}}+\overrightarrow{\mathrm{c}})|=1 \\
& |\lambda((\mathrm{x}+2) \hat{\mathrm{i}}+6 \hat{\mathrm{j}}-2 \hat{\mathrm{k}})|=1 \\
& \lambda^2\left((\mathrm{x}+2)^2+6^2+2^2\right)=1 \\
& \mathrm{x}^2+4 \mathrm{x}+4+36+4=(\mathrm{x}+6)^2 \\
& \mathrm{x}^2+4 \mathrm{x}+44=\mathrm{x}^2+12 \mathrm{x}+36 \\
& 8 \mathrm{x}=8, \mathrm{x}=1 \\
& \left|\begin{array}{ccc}
1 & 1 & 1 \\
2 & 4 & -5 \\
\mathrm{x} & 2 & 3
\end{array}\right|=(\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}) \cdot \overrightarrow{\mathrm{c}} \\
& \left|\begin{array}{ccc}
0 & 0 & 1 \\
-2 & 9 & -4 \\
\mathrm{x}-2 & -1 & 3
\end{array}\right|=2-9(\mathrm{x}-2) \\
& =20-9 \mathrm{x} \\
& \text { at } \mathrm{x}=1 \\
& 20-9=11
\end{aligned}$

</details>

---

### Q22. JEE Main 2024 (04 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $\mathrm{ABC}$ be a triangle of area $15 \sqrt{2}$ and the vectors $\overrightarrow{\mathrm{AB}}=\hat{i}+2 \hat{j}-7 \hat{k}, \overrightarrow{\mathrm{BC}}=\mathrm{a} \hat{i}+\mathrm{b} \hat{j}+\mathrm{ck}$ and $\overrightarrow{\mathrm{AC}}=6 \hat{i}+\mathrm{d} \hat{j}-2 \hat{k}, \mathrm{~d}>0$. Then the square of the length of the largest side of the triangle $\mathrm{ABC}$ is _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **54**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/IRQjQTIz9DWv5vyzrl7Y93lqcbVskPzKnmya9hJQUmE.original.fullsize.png">
$\begin{aligned}
& \text { Area }=\frac{1}{2}\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
1 & 2 & -7 \\
6 & d & -2
\end{array}\right|=15 \sqrt{2} \\
& (-4+7 d) \hat{i}-\hat{j}(-2+42)+\hat{k}(d-12) \\
& (7 d-4)^2+(40)^2+(d-12)^2=1800 \\
& 50 d^2-80 d-40=0 \\
& 5 d^2-8 d-4=0 \\
& 5 d^2-10 d-2 d-4 \\
& 5 d(d-2)+2(d-2)=0 \\
& d=2 \text { or } d=-\frac{2}{5} \\
& \because d>0, d=2 \\
& (a+1) \hat{i}+(b+2) \hat{j}+(c-7) \hat{k}=6 \hat{i}+2 \hat{j}-2 \hat{k} \\
& a+1=6 \& b+2=2, c-7=-2 \\
& a=5 \quad b=0 \quad c=5 \\
& |A B|=\sqrt{1+4+49}=\sqrt{54} \\
& |B C|=\sqrt{25+25}=\sqrt{50} \\
& |A C|=\sqrt{86+4+4}=\sqrt{44}
\end{aligned}$
Ans. 54

</details>

---

### Q23. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let a unit vector which makes an angle of $60^{\circ}$ with $2 \hat{i}+2 \hat{j}-\hat{k}$ and angle $45^{\circ}$ with $\hat{i}-\hat{k}$ be $\overrightarrow{\mathrm{C}}$. Then $\overrightarrow{\mathrm{C}}+\left(-\frac{1}{2} \hat{i}+\frac{1}{3 \sqrt{2}} \hat{j}-\frac{\sqrt{2}}{3} \hat{k}\right)$ is :

**Options:**

- **(A)** $\frac{\sqrt{2}}{3} \hat{i}-\frac{1}{2} \hat{k}$
- **(B)** $\left(\frac{1}{\sqrt{3}}+\frac{1}{2}\right) \hat{i}+\left(\frac{1}{\sqrt{3}}-\frac{1}{3 \sqrt{2}}\right) \hat{j}+\left(\frac{1}{\sqrt{3}}+\frac{\sqrt{2}}{3}\right) \hat{k}$
- **(C)** $\frac{\sqrt{2}}{3} \hat{i}+\frac{1}{3 \sqrt{2}} \hat{j}-\frac{1}{2} \hat{k}$
- **(D)** $-\frac{\sqrt{2}}{3} \hat{i}+\frac{\sqrt{2}}{3} \hat{j}+\left(\frac{1}{2}+\frac{2 \sqrt{2}}{3}\right) \hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\sqrt{2}}{3} \hat{i}-\frac{1}{2} \hat{k}$**

**Detailed Solution:**

$\overrightarrow{\mathrm{C}}=\mathrm{C}_1 \hat{\mathrm{i}}+\mathrm{C}_2 \hat{\mathrm{j}}+\mathrm{C}_3 \hat{\mathrm{k}}$
$\mathrm{C}_1{ }^2+\mathrm{C}_2{ }^2+\mathrm{C}_3{ }^2=1$
$\overrightarrow{\mathrm{C}} \cdot(2 \hat{\mathrm{i}}+2 \hat{\mathrm{j}}-\hat{\mathrm{k}})=|\mathrm{C}| \sqrt{9} \cos 60^{\circ}$
$2 \mathrm{C}_1+2 \mathrm{C}_2-\mathrm{C}_3=\frac{3}{2}$
$\mathrm{C}_1-\mathrm{C}_3=1$
$\mathrm{C}_1+2 \mathrm{C}_2=\frac{1}{2}$
$\mathrm{C}_1=\frac{\sqrt{2}}{3}+\frac{1}{2}$
$\mathrm{C}_2=\frac{-1}{3 \sqrt{2}}$
$\mathrm{C}_3=\frac{\sqrt{2}}{3}-\frac{1}{2}$

</details>

---

### Q24. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>,</mo><mo> </mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover></math> be three non-zero vectors such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover></math> are non-collinear if <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover></math> is collinear with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover><mo>,</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>+</mo><mn>6</mn><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover></math> is collinear with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>+</mo><mi mathvariant="normal">α</mi><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>+</mo><mi mathvariant="normal">β</mi><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover><mo>=</mo><mover><mn>0</mn><mo>→</mo></mover></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">α</mi><mo>+</mo><mi mathvariant="normal">β</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>30</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>25</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover></math> is collinear with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover><mo>,</mo><mo> </mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>+</mo><mn>6</mn><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover></math> is collinear with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>+</mo><mi>α</mi><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>+</mo><mi>β</mi><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover><mo>=</mo><mover><mn>0</mn><mo>→</mo></mover></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>=</mo><mi mathvariant="normal">λ</mi><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>+</mo><mn>6</mn><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover><mo>=</mo><mi mathvariant="normal">μ</mi><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>=</mo><mi mathvariant="normal">λ</mi><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover><mo>-</mo><mn>5</mn><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>+</mo><mn>6</mn><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover></mrow><mi mathvariant="normal">μ</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">λ</mi><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover><mo>-</mo><mn>5</mn><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>=</mo><mfrac><mn>6</mn><mi mathvariant="normal">μ</mi></mfrac><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">μ</mi></mfrac><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover></math></p><p>Comparing both the sides,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">μ</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac><mo>,</mo><mo> </mo><mi mathvariant="normal">λ</mi><mo>=</mo><mo>-</mo><mn>30</mn></math></p><p>Putting these values in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>=</mo><mo>-</mo><mn>30</mn><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>+</mo><mn>30</mn><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover><mo>=</mo><mn>0</mn></math></p><p>Comparing this equation with <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>→</mo></mover><mo>+</mo><mi mathvariant="normal">α</mi><mover><mi mathvariant="normal">b</mi><mo>→</mo></mover><mo>+</mo><mi mathvariant="normal">β</mi><mover><mi mathvariant="normal">c</mi><mo>→</mo></mover><mo>=</mo><mover><mn>0</mn><mo>→</mo></mover></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">α</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">β</mi><mo>=</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">α</mi><mo>+</mo><mi mathvariant="normal">β</mi><mo>=</mo><mn>35</mn></math></p>

</details>

---

### Q25. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math> be a quadrilateral. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math> are the mid points of the diagonals <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>D</mi></math> respectively and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>-</mo><mo>&#160;</mo><mover><mrow><mi>B</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mfenced><mrow><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover><mo>-</mo><mover><mrow><mi>D</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mi>k</mi><mo>&#160;</mo><mover><mrow><mi>F</mi><mi>E</mi></mrow><mo>&#8594;</mo></mover></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math> be a quadrilateral. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math> are the mid points of the diagonals <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>D</mi></math> respectively and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>-</mo><mo>&#160;</mo><mover><mrow><mi>B</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mfenced><mrow><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover><mo>-</mo><mover><mrow><mi>D</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>=</mo><mi>k</mi><mo>&#160;</mo><mover><mrow><mi>F</mi><mi>E</mi></mrow><mo>&#8594;</mo></mover></math>,</p><p>Now plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/eca13767-e7f3-495a-ac75-da94a4643863.png" style="width: 280px; height: 254px;" /></p><p>Now let position vector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>a</mi><mo>,</mo></mrow><mo>&#8594;</mo></mover><mo>&#160;</mo><mover><mrow><mi>b</mi><mo>,</mo></mrow><mo>&#8594;</mo></mover><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>d</mi><mo>&#8594;</mo></mover></math> respectively</p><p>Now by midpoint formula,</p><p>Position vector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><mover><mrow><mi>O</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover><mrow><mi>O</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>a</mi><mo>&#8594;</mo></mover></mrow><mn>2</mn></mfrac></math></p><p>And Position vector of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mfrac><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>d</mi><mo>&#8594;</mo></mover></mrow><mn>2</mn></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>-</mo><mover><mrow><mi>B</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover><mo>-</mo><mover><mrow><mi>D</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>+</mo><mover><mi>d</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mfenced><mrow><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>d</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>2</mn><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>d</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>d</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mfenced close="]" open="["><mrow><mfrac><mrow><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>d</mi><mo>&#8594;</mo></mover></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>4</mn><mfenced close="]" open="["><mrow><mover><mrow><mi>O</mi><mi>F</mi></mrow><mo>&#8594;</mo></mover><mo>-</mo><mover><mrow><mi>O</mi><mi>E</mi></mrow><mo>&#8594;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mover><mrow><mi>E</mi><mi>F</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>4</mn><mover><mrow><mi>F</mi><mi>E</mi></mrow><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p></blockquote>

</details>

---

### Q26. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi></mrow></mfenced></math> for which the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mrow><mo>&#160;</mo><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#956;</mi><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>=</mo><mn>5</mn></math>, are coplanar, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mfenced><mrow><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi></mrow></mfenced><mo>&#8712;</mo><mi>S</mi></mrow></munder><mn>80</mn><mfenced><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#956;</mi><mn>2</mn></msup></mrow></mfenced></math>  is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2210</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2130</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2290</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2370</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2290</mn></math>**

**Detailed Solution:**

<blockquote><p>The given equations are coplanar.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#955;</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>&#956;</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mfenced close="]" open="["><mrow><mn>10</mn><mo>+</mo><mn>4</mn><mi>&#956;</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced close="]" open="["><mrow><mn>5</mn><mo>-</mo><mn>3</mn><mi>&#956;</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced close="]" open="["><mrow><mo>-</mo><mn>10</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>&#955;</mi><mi>&#956;</mi><mo>+</mo><mn>10</mn><mi>&#955;</mi><mo>-</mo><mn>3</mn><mi>&#956;</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>=</mo><mn>5</mn></math></p><p>So, by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mfenced><mrow><mn>5</mn><mo>+</mo><mi>&#956;</mi></mrow></mfenced><mi>&#956;</mi><mo>+</mo><mn>10</mn><mfenced><mrow><mn>5</mn><mo>+</mo><mi>&#956;</mi></mrow></mfenced><mo>-</mo><mn>3</mn><mi>&#956;</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>&#956;</mi><mn>2</mn></msup><mo>+</mo><mn>27</mn><mi>&#956;</mi><mo>+</mo><mn>45</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>&#956;</mi><mn>2</mn></msup><mo>+</mo><mn>15</mn><mi>&#956;</mi><mo>+</mo><mn>12</mn><mi>&#956;</mi><mo>+</mo><mn>45</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mn>15</mn></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>5</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><munder><mo>&#8721;</mo><mrow><mi>&#955;</mi><mi>&#956;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mn>80</mn><mfenced><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#956;</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>80</mn><mfenced close="]" open="["><mrow><mfenced><mrow><mn>9</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mfrac><mn>225</mn><mn>16</mn></mfrac><mo>+</mo><mfrac><mn>25</mn><mn>16</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>80</mn><mfenced close="]" open="["><mrow><mn>13</mn><mo>+</mo><mfrac><mn>125</mn><mn>8</mn></mfrac></mrow></mfenced><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>229</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2290</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q27. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></math> be three distinct real numbers, none equal to one. If the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>b</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>k</mi><mo>^</mo></mover></math> are coplanar, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>b</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfrac></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given that the vectors are coplanar.</p><p>That means the determinant is equal to zero.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>b</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>&#8211;</mo><msub><mi>R</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>&#8211;</mo><msub><mi>R</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>a</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn><mo>-</mo><mi>b</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>b</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn><mo>-</mo><mi>c</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Expand the determinant along <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>[</mo><mi>c</mi><mo>(</mo><mi>b</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>-</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>c</mi><mo>)</mo><mo>]</mo><mo>+</mo><mn>1</mn><mo>[</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>b</mi><mo>)</mo><mo>&#160;</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>c</mi><mo>)</mo><mo>]</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>(</mo><mi>b</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>-</mo><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>c</mi><mo>)</mo><mo>+</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>b</mi><mo>)</mo><mo>&#160;</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>c</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>(</mo><mn>1</mn><mo>-</mo><mi>a</mi><mo>)</mo><mo>&#160;</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>b</mi><mo>)</mo><mo>+</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>a</mi><mo>)</mo><mo>&#160;</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>c</mi><mo>)</mo><mo>+</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>b</mi><mo>)</mo><mo>&#160;</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>c</mi><mo>)</mo><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>a</mi><mo>)</mo><mo>&#160;</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>b</mi><mo>)</mo><mo>+</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>a</mi><mo>)</mo><mo>&#160;</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>c</mi><mo>)</mo><mo>+</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>b</mi><mo>)</mo><mo>&#160;</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>c</mi><mo>)</mo><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>b</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p>Hence this is the required option.</p>

</details>

---

### Q28. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

For any vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math>, with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mfenced open="|" close="|"><msub><mi>a</mi><mi>i</mi></msub></mfenced><mo>&#60;</mo><mn>1</mn><mo>,</mo><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></math>, consider the following statements:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> : <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>max</mi><mfenced open="{" close="}"><mrow><mfenced open="|" close="|"><msub><mi>a</mi><mn>1</mn></msub></mfenced><mo>,</mo><mfenced open="|" close="|"><msub><mi>a</mi><mn>2</mn></msub></mfenced><mo>,</mo><mfenced open="|" close="|"><msub><mi>a</mi><mn>3</mn></msub></mfenced></mrow></mfenced><mo>&#8804;</mo><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> : <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>|</mo><mo>&#8804;</mo><mn>3</mn><mi>max</mi><mfenced close="}" open="{"><mrow><mfenced close="|" open="|"><msub><mi>a</mi><mn>1</mn></msub></mfenced><mo>,</mo><mfenced close="|" open="|"><msub><mi>a</mi><mn>2</mn></msub></mfenced><mo>,</mo><mfenced close="|" open="|"><msub><mi>a</mi><mn>3</mn></msub></mfenced></mrow></mfenced></math>

**Options:**

- **(A)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> is true
- **(B)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> is true
- **(C)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> are true
- **(D)** Neither <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> are true**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math>, with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mfenced close="|" open="|"><msub><mi>a</mi><mi>i</mi></msub></mfenced><mo>&#60;</mo><mn>1</mn><mo>,</mo><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></math>, </p><p>Let us assume that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><msub><mi>a</mi><mn>1</mn></msub></mfenced><mo>&#8804;</mo><mfenced open="|" close="|"><msub><mi>a</mi><mn>2</mn></msub></mfenced><mo>&#8804;</mo><mfenced open="|" close="|"><msub><mi>a</mi><mn>3</mn></msub></mfenced></math></p><p>Now we know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mn>2</mn></msup></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mn>2</mn></msup><mo>&#8804;</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mn>2</mn></msup></math></p><p>So, combining both above equations we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#8805;</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>&#8805;</mo><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mo>=</mo><mtext>max</mtext><mfenced open="{" close="}"><mrow><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mfenced><mo>,</mo><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mfenced><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> is true</p><p>Now again solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mn>2</mn></msup></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mn>2</mn></msup><mo>&#8804;</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mn>2</mn></msup><mo>&#8804;</mo><mn>3</mn><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mn>2</mn></msup><mo>&#8804;</mo><mn>3</mn><msup><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mover><mi>a</mi><mo>&#8594;</mo></mover></mfenced><mo>&#8804;</mo><mn>3</mn><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced><mo>=</mo><mtext>max</mtext><mfenced open="{" close="}"><mrow><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>1</mn></msub></mfenced><mo>,</mo><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></mfenced><mfenced open="|" close="|"><msub><mover><mi>a</mi><mo>&#8594;</mo></mover><mn>3</mn></msub></mfenced></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> is also true.</p>

</details>

---

### Q29. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> are respectively the circumcenter and the orthocentre of a <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover><mrow><mi>P</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover><mrow><mi>P</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></math> is equal to _______

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mover><mrow><mi>Q</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>Q</mi><mi>P</mi></mrow><mo>&#8594;</mo></mover></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be origin.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b1fb7a0f-342a-4a43-8d3e-3e5bba9ecc8a-9926572.png" style="width: 300px; height: 241px;" /></p><p>Now from the above triangle we can write <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mrow><mi>P</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mrow><mi>P</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math>.</p><p>Also, we know that centroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math> divides orthocentre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> and Circumcentre <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>1</mn></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b2f7ea60-6f36-44ff-a98f-72621683eea0-9926572_2.png" style="width: 350px; height: 92px;" /></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>G</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mfenced><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></mrow><mn>3</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mrow><mi>P</mi><mi>A</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover><mrow><mi>P</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover><mrow><mi>P</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></math></p><p>Therefore, the required answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover></math>.</p></blockquote>

</details>

---

### Q30. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>u</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>a</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><msub><mi>u</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>b</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>u</mi><mn>3</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mi>c</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>&#160;</mo></math> be coplanar. If the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>v</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><msub><mi>v</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mi>a</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>a</mi><mover><mi>k</mi><mo>^</mo></mover></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>3</mn></msub><mo>=</mo><mi>b</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>b</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>c</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math> are also coplanar, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>**

**Detailed Solution:**

<blockquote><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>u</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>a</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><msub><mover><mi>u</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>b</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>u</mi><mo>&#8594;</mo></mover><mn>3</mn></msub><mo>=</mo><mi>c</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> are coplanar.</p><p>Also given that,<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>2</mn></msub><mo>=</mo><mi>a</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>a</mi><mover><mi>k</mi><mo>^</mo></mover></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>v</mi><mo>&#8594;</mo></mover><mn>3</mn></msub><mo>=</mo><mi>b</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>b</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>c</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math> are coplanar.</p><p>Now, using the condition of coplanar we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>b</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Expanding the determinant along <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfenced><mo>+</mo><mi>a</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>b</mi><mi>c</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>2</mn><mo>+</mo><mi>a</mi><mi>b</mi><mi>c</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Again using the coplanar condition we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>a</mi><mo>+</mo><mi>b</mi></mtd><mtd><mi>c</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi><mo>+</mo><mi>c</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi><mo>+</mo><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Apply row transformations, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>R</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>-</mo><mfenced><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>a</mi><mo>+</mo><mi>b</mi></mtd><mtd><mi>c</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi><mo>+</mo><mi>c</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn><mi>a</mi></mtd><mtd><mo>-</mo><mn>2</mn><mi>c</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Expand the determinant along <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><mn>0</mn><mo>+</mo><mn>2</mn><mi>a</mi><mi>c</mi></mrow></mfenced><mo>-</mo><mi>c</mi><mfenced><mrow><mn>0</mn><mo>+</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mi>c</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mi>a</mi><mi>c</mi><mo>+</mo><mn>2</mn><mi>a</mi><mfenced><mrow><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mi>c</mi><mo>+</mo><mn>2</mn><mi>a</mi><mi>b</mi><mi>c</mi><mo>-</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mi>c</mi><mo>-</mo><mn>2</mn><mi>a</mi><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>a</mi><mi>b</mi><mi>c</mi><mo>+</mo><mn>2</mn><mi>a</mi><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mi>b</mi><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>2</mn></math> (From eq <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>6</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mn>12</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q31. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the points with position vectors  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>10</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>13</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mn>6</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>11</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>11</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mn>8</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> are collinear, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>19</mn><mi>&#945;</mi><mo>-</mo><mn>6</mn><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>**

**Detailed Solution:**

<blockquote><p>The given position vectors can be written as</p><ul>	<li><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>13</mn><mo>)</mo></math></li>	<li><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>(</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>11</mn><mo>,</mo><mo>&#160;</mo><mn>11</mn><mo>)</mo></math></li>	<li><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>8</mn></mrow></mfenced></math></li></ul><p>Also given that these three points are collinear.</p><p>Let us assume that the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> divides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mi>C</mi></math> in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>:</mo><mn>1</mn></math>.</p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>C</mi></math> are collinear </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3c98d12c-2be2-4f48-a487-9837dbc39354.png" style="width: 350px; height: 94px;" /></p><p>On applying section formula for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> co-ordinate we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>=</mo><mfrac><mrow><mo>-</mo><mn>8</mn><mi>k</mi><mo>+</mo><mn>13</mn></mrow><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>11</mn><mi>k</mi><mo>+</mo><mn>11</mn><mo>=</mo><mo>-</mo><mn>8</mn><mi>k</mi><mo>+</mo><mn>13</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>19</mn><mi>k</mi><mo>=</mo><mo>&#160;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mn>2</mn><mn>19</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>Ratio<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mn>19</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#945;</mi><mo>&#215;</mo><mn>19</mn><mo>+</mo><mfenced><mstyle displaystyle="true"><mfrac><mn>9</mn><mn>2</mn></mfrac></mstyle></mfenced><mo>&#215;</mo><mn>2</mn></mrow><mrow><mn>2</mn><mo>+</mo><mn>19</mn></mrow></mfrac><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>19</mn><mi>&#945;</mi><mo>=</mo><mn>117</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>117</mn><mn>19</mn></mfrac></math></p><p>Now similarly,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>190</mn></mrow><mn>21</mn></mfrac><mo>=</mo><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>41</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mfenced><mrow><mn>19</mn><mi>&#945;</mi><mo>-</mo><mn>6</mn><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>117</mn><mo>-</mo><mn>123</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>36</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q32. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The sum of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math>, for which the points whose position vectors are <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>8</mn></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> are coplanar, is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>Let the given vectors be <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>A</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>B</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>C</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mi mathvariant="normal">&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mover><mi>D</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>9</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>8</mn></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math></p><p>We know that if the vectors are coplanar then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></mtd><mtd><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mtd><mtd><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>-</mo><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mfenced><mrow><mi mathvariant="normal">&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>-</mo><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mi>&#945;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>9</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>8</mn></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>-</mo><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>8</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mi>k</mi></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>8</mn></mtd><mtd><mi>&#945;</mi><mo>-</mo><mn>6</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mfenced><mrow><mn>6</mn><mo>+</mo><mi>&#945;</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>8</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>&#945;</mi><mo>-</mo><mn>16</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>On Simplifying we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math></p><p>Therefore, sum of the roots is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math>.</p></blockquote>

</details>

---

### Q33. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the position vectors of the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo mathvariant="italic">,</mo><mi>B</mi><mo mathvariant="italic">,</mo><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mi mathvariant="normal">&#955;</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi mathvariant="normal">&#955;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>6</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>.</mo></math> Let the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo mathvariant="italic">=</mo><mo mathvariant="italic">{</mo><mi>&#955;</mi><mo mathvariant="italic">&#8712;</mo><mi>&#8477;</mi><mo mathvariant="italic">:</mo></math> the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo mathvariant="italic">,</mo><mi>B</mi><mo mathvariant="italic">,</mo><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> are coplanar<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>}</mo><mo>.</mo></math> The <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo mathvariant="italic">&#8721;</mo><mrow><mi>&#955;</mi><mo mathvariant="italic">&#8712;</mo><mi>S</mi></mrow></munder><mo mathvariant="italic">(</mo><mi>&#955;</mi><mo>+</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>37</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>41</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>41</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo mathvariant="italic">(</mo><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>2</mn><mi>&#955;</mi><mo mathvariant="italic">)</mo></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mi>&#955;</mi><mo>,</mo><mn>4</mn></mrow></mfenced></math> and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#8801;</mo><mo>(</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>3</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>&#8801;</mo><mo>(</mo><mo>-</mo><mn>7</mn><mo>,</mo><mi>&#955;</mi><mo>-</mo><mn>5</mn><mo>,</mo><mn>4</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover><mo>&#8801;</mo><mo>(</mo><mo>-</mo><mn>6</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>6</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>)</mo></math></p><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>D</mi></math> are coplanar.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>[</mo><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo mathvariant="italic">&#8594;</mo></mover><mo>&#160;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo mathvariant="italic">&#8594;</mo></mover><mo>&#160;</mo><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo mathvariant="italic">&#8594;</mo></mover><mo>]</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>3</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>7</mn></mtd><mtd><mi>&#955;</mi><mo>-</mo><mn>5</mn></mtd><mtd><mn>4</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>6</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Expand the determinant along the first row.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>4</mn><mfenced close="]" open="["><mrow><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mn>6</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mo>-</mo><mn>0</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced close="]" open="["><mrow><mo>-</mo><mn>7</mn><mfenced><mrow><mn>6</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mfenced><mrow><mn>4</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mfenced close="]" open="["><mrow><mn>0</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>5</mn></mrow></mfenced></mrow></mfenced></math></p><p>On solving the above equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#955;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn></math></p><p>We have two values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mo mathvariant="italic">&#8721;</mo><mrow><mi>&#955;</mi><mo mathvariant="italic">&#8712;</mo><mi>s</mi></mrow></munder><mo>(</mo><mi>&#955;</mi><mo>+</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>41</mn></math></p><p>Hence,  <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo mathvariant="italic">&#8721;</mo><mrow><mi>&#955;</mi><mo mathvariant="italic">&#8712;</mo><mi>s</mi></mrow></munder><mo>(</mo><mi>&#955;</mi><mo>+</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>41</mn></math></p></blockquote>

</details>

---

### Q34. JEE Main 2023 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> be three non-zero non-coplanar vectors. Let the position vectors of four points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;&#160;</mo><mi>&#955;</mi><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>3</mn><mover><mi>c</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>4</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>6</mn><mover><mi>c</mi><mo>&#8594;</mo></mover></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover></math> are coplanar, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is :

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math> be three non-zero non-coplanar vectors,</p><p>Also the position vectors of four points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;&#160;</mo><mi>&#955;</mi><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>3</mn><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>3</mn><mover><mi>c</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>4</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>6</mn><mover><mi>c</mi><mo>&#8594;</mo></mover></math> respectively,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>(</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>)</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>2</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>3</mn><mover><mi>c</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>3</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>4</mn><mover><mi>c</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mn>3</mn><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>5</mn><mover><mi>c</mi><mo>&#8594;</mo></mover></math></p><p>Now using the condition of coplanar we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#955;</mi><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>15</mn><mo>-</mo><mn>12</mn><mo>)</mo><mo>+</mo><mn>2</mn><mo>(</mo><mo>-</mo><mn>10</mn><mo>+</mo><mn>4</mn><mo>)</mo><mo>+</mo><mn>3</mn><mo>(</mo><mn>6</mn><mo>-</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q35. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#956;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> are coplanar and the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> on the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>54</mn></msqrt></math> units, then the sum of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#956;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> are coplanar </p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#955;</mi></mtd><mtd><mi>&#956;</mi></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>(</mo><mn>10</mn><mo>)</mo><mo>-</mo><mi>&#956;</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>+</mo><mn>4</mn><mo>(</mo><mo>-</mo><mn>14</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn><mi>&#956;</mi><mo>=</mo><mn>56</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>&#955;</mi><mo>-</mo><mi>&#956;</mi><mo>=</mo><mn>28</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And given projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>54</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover></mrow><mrow><mo>|</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>|</mo></mrow></mfrac><mo>=</mo><msqrt><mn>54</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>4</mn><mi>&#956;</mi><mo>-</mo><mn>8</mn></mrow><msqrt><mn>24</mn></msqrt></mfrac><mo>=</mo><msqrt><mn>54</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>4</mn><mi>&#956;</mi><mo>-</mo><mn>8</mn><mo>=</mo><msqrt><mn>54</mn><mo>&#215;</mo><mn>24</mn></msqrt><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>By solving equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>=</mo><mn>24</mn></math></p>

</details>

---

### Q36. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the four points, whose position vectors are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mo>-</mo><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>&#160;&#160;</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mi>&#945;</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> are coplanar, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>73</mn><mn>17</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>107</mn><mn>17</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>73</mn><mn>17</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>107</mn><mn>17</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>73</mn><mn>17</mn></mfrac></math>**

**Detailed Solution:**

<p>Let the four points be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>:</mo><mo>&#160;</mo><mo>(</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>4</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>:</mo><mo>&#160;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>)</mo></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>:</mo><mo>&#160;</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>:</mo><mo>&#160;</mo><mo>(</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>C</mi><mo>,</mo><mo>&#160;</mo><mi>D</mi></math> are coplanar points, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn><mo>-</mo><mn>3</mn></mtd><mtd><mn>2</mn><mo>+</mo><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn><mo>-</mo><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn><mo>+</mo><mn>4</mn></mtd><mtd><mn>3</mn><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>5</mn><mo>-</mo><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>4</mn></mtd><mtd><mn>4</mn><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>6</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>4</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>146</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>73</mn><mn>17</mn></mfrac></math></p>

</details>

---

### Q37. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mi>&#955;</mi><mo>,</mo><mn>8</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#955;</mi><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> are coplanar, then the product of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>21</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>59</mn><mn>8</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>57</mn><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>95</mn><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>95</mn><mn>8</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>B</mi><mfenced><mrow><mn>5</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>C</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mi>&#955;</mi><mo>,</mo><mn>8</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>D</mi><mfenced><mrow><mi>&#955;</mi><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> are coplanar,</p><p>Now we know that condition of coplanarity is  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></mtd><mtd><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></mtd><mtd><mover><mrow><mi>A</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>8</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>&#955;</mi><mo>-</mo><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#955;</mi><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>6</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mfenced><mrow><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mn>6</mn><mo>+</mo><mi>&#955;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>8</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mfenced><mrow><mo>-</mo><mn>6</mn><mi>&#955;</mi><mo>+</mo><mn>17</mn></mrow></mfenced><mo>+</mo><mn>4</mn><mo>+</mo><mi>&#955;</mi><mo>-</mo><mn>8</mn><mo>+</mo><mn>8</mn><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>18</mn><mi>&#955;</mi><mo>+</mo><mn>51</mn><mo>+</mo><mn>4</mn><mo>+</mo><mi>&#955;</mi><mo>-</mo><mn>8</mn><mo>+</mo><mn>8</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>40</mn><mi>&#955;</mi><mo>+</mo><mn>48</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>57</mn><mi>&#955;</mi><mo>+</mo><mn>95</mn><mo>=</mo><mn>0</mn></math></p><p>So product of roots will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>95</mn><mn>8</mn></mfrac></math></p></blockquote>

</details>

---

### Q38. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">t</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mi>t</mi><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mi>t</mi><mover><mi>j</mi><mo mathvariant="italic">^</mo></mover><mo>+</mo><mover><mi>k</mi><mo mathvariant="italic">^</mo></mover><mo>,</mo><mo>&#160;</mo><mi>t</mi><mo>&#8712;</mo><mi>R</mi></math> be such that for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#947;</mi><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mi>&#946;</mi><mo>=</mo><mi>&#947;</mi><mo>=</mo><mn>0</mn></math>. Then, the set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> is

**Options:**

- **(A)** a non-empty finite set
- **(B)** equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math>
- **(C)** equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math>
- **(D)** equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">t</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo mathvariant="italic">&#8594;</mo></mover><mo>=</mo><mi>t</mi><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mi>t</mi><mover><mi>j</mi><mo mathvariant="italic">^</mo></mover><mo>+</mo><mover><mi>k</mi><mo mathvariant="italic">^</mo></mover><mo>,</mo><mo>&#160;</mo><mi>t</mi><mo>&#8712;</mo><mi>R</mi></math> be such that for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#946;</mi><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>&#947;</mi><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mi>&#946;</mi><mo>=</mo><mi>&#947;</mi><mo>=</mo><mn>0</mn></math>. Then, the set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> is</p><p>By its given condition <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>:</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>,</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math>are linearly independent vectors or they are non-coplanar</p><p>We know that when vectors are non-coplanar then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mover><mi>a</mi><mo>&#8594;</mo></mover></mtd><mtd><mover><mi>b</mi><mo>&#8594;</mo></mover></mtd><mtd><mover><mi>c</mi><mo>&#8594;</mo></mover></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mover><mi>a</mi><mo>&#8594;</mo></mover></mtd><mtd><mover><mi>b</mi><mo>&#8594;</mo></mover></mtd><mtd><mover><mi>c</mi><mo>&#8594;</mo></mover></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>t</mi></mtd><mtd><mn>1</mn><mo>-</mo><mi>t</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>-</mo><mi>t</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>t</mi></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi>t</mi></mtd><mtd><mo>-</mo><mi>t</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><msub><mi>C</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>t</mi></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>-</mo><mi>t</mi></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi>t</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>t</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>-</mo><mi>t</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi>t</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced><mo>+</mo><mi>t</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mn>3</mn><mi>t</mi></mrow></mfenced><mo>=</mo><mn>6</mn><mi>t</mi></math></p><p>Now from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mover><mi>a</mi><mo>&#8594;</mo></mover></mtd><mtd><mover><mi>b</mi><mo>&#8594;</mo></mover></mtd><mtd><mover><mi>c</mi><mo>&#8594;</mo></mover></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mn>0</mn><mo>&#8658;</mo><mi>t</mi><mo>&#8800;</mo><mn>0</mn></math></p></blockquote>

</details>

---

### Q39. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>C</mi></math> be three points whose position vectors respectively are:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#945;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is the smallest positive integer for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> are non-collinear, then the length of the median, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mi>A</mi><mi>B</mi><mi>C</mi></math>, through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>82</mn></msqrt><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>62</mn></msqrt><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>69</mn></msqrt><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>66</mn></msqrt><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>82</mn></msqrt><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Let us assume that vectors are collinear so, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#8741;</mo><mover><mrow><mi>A</mi><mi>C</mi></mrow><mo>&#8594;</mo></mover></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>&#945;</mi><mo>-</mo><mn>4</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn></math> </p><p>Now, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> to be non-collinear smallest positive integer will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn></math></p><p>So, mid-point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>=</mo><mi>M</mi><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>M</mi><mo>=</mo><msqrt><mfrac><mn>9</mn><mn>4</mn></mfrac><mo>+</mo><mn>16</mn><mo>+</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></msqrt><mo>=</mo><mfrac><msqrt><mn>82</mn></msqrt><mn>2</mn></mfrac></math></p>

</details>

---

### Q40. JEE Main 2022 (28 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;&#160;</mo><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>&#160;&#160;</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>c</mi><mn>1</mn></msub><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mover><mi>k</mi><mo>^</mo></mover></math> are coplanar vectors and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>5</mn><mo>,</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#8869;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>122</mn><mfenced><mrow><msub><mi>c</mi><mn>1</mn></msub><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub></mrow></mfenced></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **150**

**Detailed Solution:**

<p>As the given vectors are coplanar, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><msub><mi>c</mi><mn>1</mn></msub></mtd><mtd><msub><mi>c</mi><mn>2</mn></msub></mtd><mtd><msub><mi>c</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><msub><mi>c</mi><mn>1</mn></msub><mo>-</mo><mn>7</mn><msub><mi>c</mi><mn>2</mn></msub><mo>-</mo><mn>3</mn><msub><mi>c</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>5</mn><mo>&#8658;</mo><mn>2</mn><msub><mi>c</mi><mn>1</mn></msub><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mo>+</mo><mn>3</mn><msub><mi>c</mi><mn>3</mn></msub><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>3</mn><msub><mi>c</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>c</mi><mn>2</mn></msub><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Solving the above three equations using Cramer&#39;s rule, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>8</mn></mtd><mtd><mo>-</mo><mn>7</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>122</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>1</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>7</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>2</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>8</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>85</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>&#8710;</mo><mn>3</mn></msub><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>8</mn></mtd><mtd><mo>-</mo><mn>7</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>225</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>122</mn><mfenced><mrow><msub><mi>c</mi><mn>1</mn></msub><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub></mrow></mfenced><mo>=</mo><mn>122</mn><mfenced><mrow><mfrac><mn>10</mn><mn>122</mn></mfrac><mo>-</mo><mfrac><mn>85</mn><mn>122</mn></mfrac><mo>+</mo><mfrac><mn>225</mn><mn>122</mn></mfrac></mrow></mfenced><mo>=</mo><mn>150</mn></math></p><p> </p>

</details>

---

### Q41. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> be distinct positive numbers. If the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>a</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>b</mi><mover><mi>k</mi><mo>^</mo></mover></math> are co-planar, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mrow><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>b</mi></mfrac></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>b</mi></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>a</mi><mi>b</mi></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>a</mi><mi>b</mi></msqrt></math>**

**Detailed Solution:**

<p>Given vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>a</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>c</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>b</mi><mover><mi>k</mi><mo>^</mo></mover></math> are co-planar, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>a</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>c</mi></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mfenced><mrow><mn>0</mn><mo>-</mo><mi>c</mi></mrow></mfenced><mo>-</mo><mi>a</mi><mfenced><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mo>+</mo><mi>c</mi><mfenced><mrow><mi>c</mi><mo>-</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><mi>a</mi><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><msqrt><mi>a</mi><mi>b</mi></msqrt><mo>.</mo></math></p>

</details>

---

### Q42. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mfenced><mrow><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>b</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mi>b</mi><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mi>b</mi><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>+</mo><mi>b</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mi>b</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>b</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>&#8712;</mo><mi>R</mi></math> be co-planar. Then which of the following is true?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>b</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>c</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>b</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>b</mi><mo>+</mo><mn>2</mn><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>=</mo><mi>b</mi><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>b</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<p>If the vectors are co-planar,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mn>2</mn></mtd><mtd><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi></mtd><mtd><mo>-</mo><mi>b</mi><mo>-</mo><mi>c</mi></mtd></mtr><mtr><mtd><mi>b</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>2</mn><mi>b</mi></mtd><mtd><mo>-</mo><mi>b</mi></mtd></mtr><mtr><mtd><mi>b</mi><mo>+</mo><mn>2</mn></mtd><mtd><mn>2</mn><mi>b</mi></mtd><mtd><mn>1</mn><mo>-</mo><mi>b</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>&#8596;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>&#8596;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub><mo>&#160;</mo></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>a</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>a</mi><mo>+</mo><mi>c</mi></mtd><mtd><mo>-</mo><mi>c</mi></mtd></mtr><mtr><mtd><mi>b</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>2</mn><mi>b</mi></mtd><mtd><mo>-</mo><mi>b</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo>)</mo><mn>2</mn><mi>b</mi><mo>-</mo><mo>(</mo><mi>a</mi><mo>+</mo><mi>c</mi><mo>)</mo><mo>(</mo><mn>2</mn><mi>b</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>-</mo><mi>c</mi><mo>(</mo><mo>-</mo><mn>2</mn><mi>b</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mi>b</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>-</mo><mn>2</mn><mi>a</mi><mi>b</mi><mo>-</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mi>c</mi><mo>-</mo><mi>c</mi><mo>+</mo><mn>2</mn><mi>b</mi><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>b</mi><mo>-</mo><mi>a</mi><mo>-</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>2</mn><mi>b</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>c</mi></math></p>

</details>

---

### Q43. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>a</mi><mn>1</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mi>x</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>a</mi><mn>2</mn></msub><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi>y</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mi>z</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> are collinear, then a possible unit vector parallel to the vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi>y</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mi>z</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> is:<gwmw style="display:none;"></gwmw>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mfenced><mrow><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi mathvariant="italic">a</mi><mo mathvariant="italic">&#8594;</mo></mover><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi mathvariant="italic">a</mi><mo mathvariant="italic">&#8594;</mo></mover><mn>2</mn></msub></math> are collinear</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mi>y</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>z</mi></mfrac></math></p><p>Unit vector in direction of</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mi>y</mi><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mi>z</mi><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>=</mo><mo>&#177;</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mfenced><mrow><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math></p>

</details>

---

### Q44. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>35</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mi>&#955;</mi><mo>,</mo><mn>7</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> are coplanar, then the sum of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>44</mn><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>44</mn><mn>5</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>39</mn><mn>5</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>39</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>44</mn><mn>5</mn></mfrac></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>35</mn></mrow></mfenced><mo>,</mo><mi>B</mi><mfenced><mrow><mn>7</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mi>C</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mi>&#955;</mi><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mi>D</mi><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#175;</mo></mover><mo>=</mo><mn>6</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>30</mn><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mrow><mi>B</mi><mi>C</mi></mrow><mo>&#175;</mo></mover><mo>=</mo><mo>-</mo><mn>6</mn><mover><mrow><mi>i</mi><mo>+</mo></mrow><mo>^</mo></mover><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>C</mi><mi>D</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>5</mn><mover><mi>k</mi><mo>^</mo></mover></math></p><p>Points are coplanar
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>6</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>30</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mi>&#955;</mi><mo>-</mo><mn>5</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn><mo>-</mo><mi>&#955;</mi></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mfenced><mrow><mo>-</mo><mn>5</mn><mi>&#955;</mi><mo>+</mo><mn>25</mn><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>30</mn><mfenced><mrow><mo>-</mo><mn>6</mn><mo>+</mo><mn>6</mn><mi>&#955;</mi><mo>-</mo><mfenced><mrow><mn>2</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mi>&#955;</mi><mo>-</mo><mn>10</mn><mi>&#955;</mi><mo>+</mo><mn>5</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mfenced><mrow><mo>-</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>23</mn></mrow></mfenced><mo>-</mo><mn>30</mn><mfenced><mrow><mo>-</mo><mn>2</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>&#955;</mi><mo>-</mo><mn>5</mn><mo>-</mo><mn>6</mn><mo>+</mo><mn>6</mn><mi>&#955;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mfenced><mrow><mo>-</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>23</mn></mrow></mfenced><mo>-</mo><mn>30</mn><mfenced><mrow><mo>-</mo><mn>2</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>17</mn><mi>&#955;</mi><mo>-</mo><mn>11</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mfenced><mrow><mo>-</mo><mn>3</mn><mi>&#955;</mi><mo>+</mo><mn>23</mn><mo>+</mo><mn>10</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>85</mn><mi>&#955;</mi><mo>+</mo><mn>55</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mfenced><mrow><mn>10</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>88</mn><mi>&#955;</mi><mo>+</mo><mn>78</mn></mrow></mfenced><mo>=</mo><mn>12</mn><mfenced><mrow><mn>5</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>44</mn><mi>&#955;</mi><mo>+</mo><mn>39</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>=</mo><mn>12</mn><mfenced><mrow><mn>5</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>44</mn><mi>&#955;</mi><mo>+</mo><mn>39</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>44</mn><mn>5</mn></mfrac></math></p>

</details>

---

### Q45. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A vector <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mfenced separators="|"><mrow><mi>&#945;</mi><mo>,</mo><mi></mi><mi>&#946;</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced></math> lies in the plane of the vectors, <math><mi mathvariant="normal"></mi><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></math> and <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>.</mo></math> If <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></math> bisects the angle between <math><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math> and <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>,</mo><mi></mi></math> then

**Options:**

- **(A)** <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>→</mo></mover><mo>⋅</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>→</mo></mover><mo>⋅</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>→</mo></mover><mo>⋅</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>→</mo></mover><mo>⋅</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>→</mo></mover><mo>⋅</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

As, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> lies in the plane of the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>c</mi><mo>&#8594;</mo></mover></math>, So, <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mi></mi><mfenced separators="|"><mrow><mfrac><mrow><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mrow><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></mrow><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>&#955;</mi></mrow><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mn>3</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>&#955;</mi></mrow><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mn>4</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>
Compare with <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>a</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
<math><mfrac><mrow><mn>2</mn><mi>&#955;</mi></mrow><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math>
<math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
Not in option
So, now consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>&#956;</mi><mfenced separators="|"><mrow><mfrac><mrow><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover accent="true"><mi>j</mi><mo>^</mo></mover></mrow><msqrt><mn>2</mn></msqrt></mfrac><mo>-</mo><mfrac><mrow><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover></mrow><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mi>&#956;</mi><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mfenced separators="|"><mrow><mn>3</mn><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover accent="true"><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover accent="true"><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover accent="true"><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mi>&#956;</mi></mrow><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>
Compare with <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>&#946;</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
<math><mfrac><mrow><mn>4</mn><mi>&#956;</mi></mrow><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mfrac><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
<math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>.</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>

</details>

---

### Q46. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mi>&#945;</mi><mtext>&#8201;</mtext><mo>&#8712;</mo><mi>R</mi></math> and the three vectors <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>,</mo><mtext>&#8201;&#8201;</mtext><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>-</mo><mi>&#945;</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> and <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#945;</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>.</mo></math> Then the set S = {<math><mi>&#945;</mi><mo>:</mo><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>,</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math> and <math><mover accent="true"><mrow><mi>c</mi></mrow><mo>&#8594;</mo></mover></math> are coplanar}

**Options:**

- **(A)** is singleton
- **(B)** contains exactly two positive numbers
- **(C)** is empty
- **(D)** contains exactly two numbers only one of which is positive

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) is empty**

**Detailed Solution:**

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mover><mi>c</mi><mo>&#8594;</mo></mover></math> are coplanar then, 
<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mn>3</mn><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>18</mn><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mi>&#945;</mi><mo>&#8712;</mo><mi>&#981;</mi></math>

</details>

---

### Q47. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The sum of the distinct real values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi></math> for which the vectors <math><mi>&#956;</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>,</mo><mi>&#160;</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>&#956;</mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>,</mo><mi>&#160;</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>&#956;</mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> are co-planar, is

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** <math><mo>-</mo><mn>1</mn></math>
- **(C)** <math><mn>1</mn></math>
- **(D)** <math><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Given the three vectors are coplanar.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mi>&#956;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#956;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>&#956;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mfenced><mrow><msup><mi>&#956;</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mi>&#956;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mfenced><mrow><mi>&#956;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#956;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mi>&#956;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#956;</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#956;</mi><mo>&#160;</mo><mfenced><mrow><mi>&#956;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#956;</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>&#956;</mi><mn>2</mn></msup><mo>+</mo><mi>&#956;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#956;</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#956;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#956;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn></math></p><p>Therefore, the sum of the distinct real values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>1</mn></math>.</p>

</details>

---

### Q48. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}=\hat{i}+2 \hat{j}+4 \hat{k}, \vec{b}=\hat{i}+\lambda \hat{j}+4 \hat{k}$ and

$\vec{c}=2 \hat{i}+4 \hat{j}+\left(\lambda^{2}-1\right) \hat{k}$ be coplanar vectors. Then the

non-zero vector $\vec{a} \times \vec{c}$ is:

**Options:**

- **(A)** $-10 \hat{i}-5 \hat{j}$
- **(B)** $-14 \hat{i}-5 \hat{j}$
- **(C)** $-14 \hat{i}+5 \hat{j}$
- **(D)** $-10 \hat{i}+5 \hat{j}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-10 \hat{i}+5 \hat{j}$**

**Detailed Solution:**

$\because \bar{a}, \bar{b}$ and $\bar{c}$ are coplanar

$\therefore\left|\begin{array}{ccc}1 & 2 & 4 \\ 1 & \lambda & 4 \\ 2 & 4 & \left(\lambda^{2}-1\right)\end{array}\right|=0$

$\Rightarrow \quad \lambda^{3}-\lambda-16+2\left(8-\lambda^{2}+1\right)+4(4-2 \lambda)=0$

$\Rightarrow \quad \lambda^{3}-2 \lambda^{2}-9 \lambda+18=0$

i.e. $\quad(\lambda-2)(\lambda-3)(\lambda+3)=0$

For $\lambda=2, \vec{c}=2 \hat{i}+4 \hat{j}+3 \hat{k}$

$\therefore \quad \vec{a} \times \vec{c}=\left|\begin{array}{ccc}\hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & 4 \\ 2 & 4 & 3\end{array}\right|=-10 \hat{i}+5 \hat{j}$

For $\lambda=3$ or $-3, \bar{c}=2 \bar{a} \Rightarrow \bar{a} \times \bar{c}=0$ (Rejected)

</details>

---

### Q49. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mover accent="true"><mrow><mi>&#945;</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mi>&#955;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>&#160;</mi><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>&#946;</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>&#160;</mi><mover accent="true"><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mn>3</mn><mover accent="true"><mi>b</mi><mo>&#8594;</mo></mover><mo>,</mo></math> be two given vectors where vectors <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></math> and <math><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math> are non-collinear. The value of <math><mi>&#955;</mi></math> for which vectors <math><mover accent="true"><mrow><mi>&#945;</mi></mrow><mo>&#8594;</mo></mover></math> and <math><mover accent="true"><mrow><mi>&#946;</mi></mrow><mo>&#8594;</mo></mover></math> are collinear, is:

**Options:**

- **(A)** <math><mo>-</mo><mn>4</mn></math>
- **(B)** <math><mo>-</mo><mn>3</mn></math>
- **(C)** <math><mn>4</mn></math>
- **(D)** <math><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>-</mo><mn>4</mn></math>**

**Detailed Solution:**

<math><mo>&#8757;</mo><mover accent="true"><mrow><mi>&#945;</mi></mrow><mo>&#8594;</mo></mover><mo>,</mo><mtext>&#8201;</mtext><mover accent="true"><mrow><mi>&#946;</mi></mrow><mo>&#8594;</mo></mover></math> are collinear then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#955;</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>4</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>4</mn></math>.

</details>

---

### Q50. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The number of distinct real values of <math><mi>&#955;</mi></math>, for which the lines <math><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>3</mn></mrow><mrow><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math> and <math><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> , are coplanar is

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mn>4</mn></math>
- **(C)** <math><mn>3</mn></math>
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>3</mn></math>**

**Detailed Solution:**

<math><mo>&#8757;</mo></math> Lines are coplanar

<math><mo>&#8756;</mo></math> <math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>3</mn><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn><mo>-</mo><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math> <math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math> <math><mn>2</mn><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfenced><mo>+</mo><mn>4</mn><mfenced separators="|"><mrow><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math> <math><mn>4</mn><mo>-</mo><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math> <math><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math> <math><mi>&#955;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><msqrt><mn>2</mn></msqrt><mo>,</mo><mi>&#160;</mi><mo>-</mo><msqrt><mn>2</mn></msqrt></math>

</details>

---

### Q51. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>6</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,&#160;</mo><mover><mi>y</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>z</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>1</mn><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></math>, then the magnitude of the projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>y</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>z</mi><mo>&#8594;</mo></mover></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>6</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi>y</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>3</mn><mover><mi>k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>z</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>y</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mover><mi>i</mi><mo>^</mo></mover></mtd><mtd><mover><mi>j</mi><mo>^</mo></mover></mtd><mtd><mover><mi>k</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mfenced><mrow><mn>18</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mfenced><mrow><mo>-</mo><mn>9</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mfenced><mrow><mn>12</mn><mo>+</mo><mn>6</mn></mrow></mfenced><mo>=</mo><mn>22</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>8</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>18</mn><mover><mi>k</mi><mo>^</mo></mover><mo>=</mo><mn>2</mn><mfenced><mrow><mn>11</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>9</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Now, we know that the projection of a vector <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> is defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow><mfenced close="|" open="|"><mover><mi>b</mi><mo>&#8594;</mo></mover></mfenced></mfrac></math></p><p>Hence, the magnitude of projection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>y</mi><mo>&#8594;</mo></mover></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>z</mi><mo>&#8594;</mo></mover></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>y</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi>z</mi><mo>&#8594;</mo></mover></mrow><mfenced close="|" open="|"><mover><mi>z</mi><mo>&#8594;</mo></mover></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced close="|" open="|"><mrow><mn>2</mn><mfenced><mrow><mn>11</mn><mi>i</mi><mo>+</mo><mn>4</mn><mi>j</mi><mo>+</mo><mn>9</mn><mi>k</mi></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced><mfenced close="|" open="|"><mrow><mn>3</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mn>4</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>12</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced close="|" open="|"><mrow><mn>2</mn><mfenced><mrow><mn>3</mn><mn>3</mn><mo>-</mo><mn>1</mn><mn>6</mn><mo>-</mo><mn>1</mn><mn>0</mn><mn>8</mn></mrow></mfenced></mrow></mfenced><msqrt><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><mn>1</mn><msup><mn>2</mn><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>9</mn><mn>1</mn></mrow><msqrt><mn>169</mn></msqrt></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>9</mn><mn>1</mn></mrow><mrow><mn>1</mn><mn>3</mn></mrow></mfrac><mo>=</mo><mn>1</mn><mn>4</mn><mo>.</mo></math></p>

</details>

---

### Q52. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{a}$ and $\vec{b}$ are non-collinear vectors, then the value of $\alpha$ for which the vectors $\vec{u}=(\alpha-2) \vec{a}+\vec{b}$ and $\vec{v}=(2+3 \alpha) \vec{a}-3 \vec{b}$ are collinear is :

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** $\frac{2}{3}$
- **(C)** $-\frac{3}{2}$
- **(D)** $-\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{3}$**

**Detailed Solution:**

Since, $\vec{u}$ and $\vec{v}$ are collinear, therefore
$$
\begin{aligned}
& \vec{u}+\vec{v}=0 \\
\Rightarrow & {[k(\alpha-2)+2+3 \alpha] \vec{a}+(k-3) \vec{b}=0 }
\end{aligned}
$$
Since $\vec{a}$ and $\vec{b}$ are non-collinear, then for some constant $m$ and $n$,

$$
m \vec{a}+n \vec{b}=0 \Rightarrow m=0, n=0
$$
Hence from equation (i)
$$
\begin{aligned}
& k-3=0 \Rightarrow k=3 \\
& \text { And } k(\alpha-2)+2+3 \alpha=0 \\
& \Rightarrow 3(\alpha-2)+2+3 \alpha=0 \Rightarrow \alpha=\frac{2}{3}
\end{aligned}
$$

</details>

---

### Q53. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $\vec{a}=2 \hat{i}-\hat{j}+\hat{k}, \vec{b}=\hat{i}+2 \hat{j}-\hat{k}$ and $\vec{c}=\hat{i}+\hat{j}-2 \hat{k}$ be three vectors. A vector of the type $\vec{b}+\lambda \vec{c}$ for some scalar $\lambda$, whose projection on $\vec{a}$ is of magnitude $\sqrt{\frac{2}{3}}$ is :

**Options:**

- **(A)** $2 \hat{i}+\hat{j}+5 \hat{k}$
- **(B)** $2 \hat{i}+3 \hat{j}-3 \hat{k}$
- **(C)** $2 \hat{i}-\hat{j}+5 \hat{k}$
- **(D)** $2 \hat{i}+3 \hat{j}+3 \hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \hat{i}+3 \hat{j}-3 \hat{k}$**

**Detailed Solution:**

Let $\vec{d}=\vec{b}+\lambda \vec{c}$
$$
\begin{aligned}
& \therefore \vec{d}=\hat{i}+2 \hat{j}-\hat{k}+\lambda(\hat{i}+\hat{j}-2 \hat{k}) \\
& =(1+\lambda) \hat{i}+(2+\lambda) \hat{j}-(1+2 \lambda) \hat{k}
\end{aligned}
$$
If $\theta$ be the angle between $\vec{d}$ and $\vec{a}$, then projection of $\vec{d}$ or $(\vec{b}+\lambda \vec{c})$ on $\vec{a}$
$$
\begin{aligned}
& =|\vec{d}| \cos \theta \\
& =|\vec{d}|\left(\frac{\vec{d} \cdot \vec{a}}{|\vec{d}||\vec{a}|}\right)=\frac{\vec{d} \cdot \vec{a}}{|\vec{a}|} \\
& =\frac{2(\lambda+1)-(\lambda+2)-(2 \lambda+1)}{\sqrt{4+1+1}} \\
& =\frac{-\lambda-1}{\sqrt{6}}
\end{aligned}
$$
But projection of $\vec{d}$ on $\vec{a}=\sqrt{\frac{2}{3}}$
$$
\therefore-\frac{\lambda+1}{\sqrt{6}}=\sqrt{\frac{2}{3}} \Rightarrow \frac{\lambda^2+2 \lambda+1}{6}=\frac{2}{3}
$$
$$
\begin{aligned}
& \Rightarrow \lambda^2+2 \lambda-3=0 \Rightarrow \lambda^2+3 \lambda-\lambda-3=0 \\
& \Rightarrow \lambda(\lambda+3)-1(\lambda+3)=0, \Rightarrow \lambda=1,-3
\end{aligned}
$$
when $\lambda=1$, then $\vec{b}+\lambda \vec{c}=2 \hat{i}+3 \hat{j}-3 \hat{k}$
when $\lambda=-3$, then $\vec{b}+\lambda \vec{c}=-2 \hat{i}-\hat{j}+5 \hat{k}$

</details>

---

### Q54. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `3`

If the vectors <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>AB</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>AC</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>5</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>4</mn><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> are the sides of a triangle <math> <mrow> <mi>A</mi><mi>B</mi><mi>C</mi><mo>,</mo> </mrow> </math> then the length of the median through <math> <mi>A</mi> </math> is:

**Options:**

- **(A)** <math> <mrow> <msqrt> <mn>3</mn> <mn>3</mn> </msqrt> </mrow> </math>
- **(B)** <math> <mrow> <msqrt> <mn>4</mn> <mn>5</mn> </msqrt> </mrow> </math>
- **(C)** <math> <mrow> <msqrt> <mn>1</mn> <mn>8</mn> </msqrt> </mrow> </math>
- **(D)** <math> <mrow> <msqrt> <mn>7</mn> <mn>2</mn> </msqrt> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <msqrt> <mn>3</mn> <mn>3</mn> </msqrt> </mrow> </math>**

**Detailed Solution:**

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM0010333_Ansexp1_1.jpg" style="width: 300px; height: 224px;" />

Length of median <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mover accent="true"><mi>AB</mi><mo>&#8594;</mo></mover><mo>+</mo><mover accent="true"><mi>AC</mi><mo>&#8594;</mo></mover></mrow><mn>2</mn></mfrac></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>8</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>8</mn><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow><mn>2</mn></mfrac></mfenced></math>

<math> <mrow><mo>=</mo> <msqrt> <mn>3</mn> <mn>3</mn> </msqrt> </mrow> </math>

</details>

---

### Q55. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `1`

Statement 1: If the points $(1,2,2),(2,1,2)$ and $(2,2, z)$ and $(1,1,1)$ are coplanar, then $z=2$.
Statement 2: If the 4 points $P, Q, R$ and $S$ are coplanar, then the volume of the tetrahedron $P Q R S$ is 0.

**Options:**

- **(A)** Statement 1 is false,, Statement 2 is true.
- **(B)** Statement 1 is true, Statement 2 is false.
- **(C)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation of Statement 1.
- **(D)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation of Statement 1.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement 1 is false,, Statement 2 is true.**

**Detailed Solution:**

Statement-1
Points (1, 2, 2), (2, 1, 2), (2, 2, z) and (1, 1, 1) are coplanar then $z=2$ which is false.
$$
\begin{aligned}
& \because\left|\begin{array}{ccc}
1 & -1 & 0 \\
1 & 0 & z-2 \\
0 & -1 & -1
\end{array}\right|=0 \\
& \Rightarrow 1(z-2)+1(-1)=0 \Rightarrow z=3
\end{aligned}
$$
Statement $-2$ is the true statement.

</details>

---

### Q56. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{a}=\hat{i}-2 \hat{j}+3 \hat{k}, \vec{b}=2 \hat{i}+3 \hat{j}-\hat{k}$ and $\vec{c}=\lambda \hat{i}+\hat{j}+(2 \lambda-1 \hat{k})$ are coplanar vectors, then $\lambda$ is equal to

**Options:**

- **(A)** 0
- **(B)** $-1$
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Since $\vec{a}=\hat{i}-2 \hat{j}+3 \hat{k}, \vec{b}=2 \hat{i}+3 \hat{j}-\hat{k}$ and $\vec{c}=\lambda \hat{i}+\hat{j}+(2 \lambda-1 \hat{k})$ are coplanar therefore $[\vec{a} \vec{b} \vec{c}]=0$
$$
\begin{aligned}
& \text { i.e., }\left|\begin{array}{ccc}
1 & 2 & \lambda \\
-2 & 3 & 1 \\
3 & -1 & 2 \lambda-1
\end{array}\right|=0 \\
& \Rightarrow 1(6 \lambda-2)-2(-4 \lambda-1)+\lambda(-7)=0 \\
& \Rightarrow(6 \lambda-2)+8 \lambda+2+2+2 \lambda-9 \lambda=0 \\
& \Rightarrow 7 \lambda=0 \Rightarrow \lambda=0
\end{aligned}
$$

</details>

---

### Q57. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `2`

$A B C D$ is parallelogram. The position vectors of $A$ and $C$ are respectively, $3 \hat{i}+3 \hat{j}+5 \hat{k}$ and $\hat{i}-5 \hat{j}-5 \hat{k}$. If $M$ is the midpoint of the diagonal $D B$, then the magnitude of the projection of $\overrightarrow{O M}$ on $\overrightarrow{O C}$, where $O$ is the origin, is

**Options:**

- **(A)** $7 \sqrt{51}$
- **(B)** $\frac{7}{\sqrt{50}}$
- **(C)** $7 \sqrt{50}$
- **(D)** $\frac{7}{\sqrt{51}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{7}{\sqrt{51}}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1on52u1k3uk4Dsw1bv5uijnhxp0nNOwPKwg9D7R94ck.original.fullsize.png">

In a parallelogram, diagonals bisect each other. So, mid point of $D B$ is also the midpoint of $A C$.
Mid-point of $M=2 \hat{i}-\hat{j}$
Direction ratio of $O C=(1,-5,-5)$
Direction ratio of $O M=(2,-1,0)$
Angle $\theta$ between $O M$ and $O C$ is given by
$$
\left.\cos \theta=\frac{(1 \times 2+)-5(-1)(+-5) 0(}{\sqrt{2^2+(-1)^2} \sqrt{()^2+(-5)^2+(-5)^2}}\right)()
$$

$$
=\frac{2+5}{\sqrt{5} \sqrt{51}}=\frac{7}{\sqrt{5} \sqrt{51}}
$$
Projection of $\overrightarrow{O M}$ on $\overrightarrow{O C}$ is given by
$$
|O M| \cdot \cos \theta=\sqrt{5} \times \frac{7}{\sqrt{5} \times \sqrt{51}}=\frac{7}{\sqrt{51}}
$$

</details>

---

### Q58. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `3`

Let $A B C D$ be a parallelogram such that $\overrightarrow{A B}=\overrightarrow{\mathrm{q}}, \overrightarrow{A D}=\vec{p}$ and $\angle B A D$ be an acute angle. If $\vec{r}$ is the vector that coincides with the altitude directed from the vertex $B$ to the side $A D$, then $\vec{r}$ is given by

**Options:**

- **(A)** $\vec{r}=3 \vec{q}-\frac{3(\vec{p} \cdot \vec{q})}{(\vec{p} \cdot \vec{p})} \vec{p}$
- **(B)** $\vec{r}=-\overrightarrow{\mathrm{q}}+\left(\frac{\overrightarrow{\mathrm{p}} \cdot \overrightarrow{\mathrm{q}}}{\overrightarrow{\mathrm{p}} \cdot \overrightarrow{\mathrm{p}}}\right) \overrightarrow{\mathrm{p}}$
- **(C)** $\vec{r}=\vec{q}-\left(\frac{\vec{p} \cdot \vec{q}}{\vec{p} \cdot \vec{p}}\right) \vec{p}$
- **(D)** $\vec{r}=-3 \vec{q}+\frac{3(\vec{p} \cdot \vec{q})}{(\vec{p} \cdot \vec{p})} \vec{p}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\vec{r}=-\overrightarrow{\mathrm{q}}+\left(\frac{\overrightarrow{\mathrm{p}} \cdot \overrightarrow{\mathrm{q}}}{\overrightarrow{\mathrm{p}} \cdot \overrightarrow{\mathrm{p}}}\right) \overrightarrow{\mathrm{p}}$**

**Detailed Solution:**

$\overrightarrow{\mathrm{AE}}=$ vector component of $\overrightarrow{\mathrm{q}}$ on $\overrightarrow{\mathrm{p}}$
$\overrightarrow{\mathrm{AE}}=\frac{(\overrightarrow{\mathrm{p}} \cdot \overrightarrow{\mathrm{q}})}{(\overrightarrow{\mathrm{p}} \cdot \overrightarrow{\mathrm{q}})} \overrightarrow{\mathrm{p}} \quad \therefore$ From $\triangle \mathrm{ABE} ; \overrightarrow{\mathrm{AB}}+\overrightarrow{\mathrm{BE}}=\overrightarrow{\mathrm{AE}}$
$\Rightarrow \overrightarrow{\mathrm{q}}+\overrightarrow{\mathrm{r}}=\frac{(\overrightarrow{\mathrm{p}} \cdot \overrightarrow{\mathrm{q}}) \overrightarrow{\mathrm{p}}}{(\overrightarrow{\mathrm{p}} \cdot \overrightarrow{\mathrm{q}})} \quad \Rightarrow \overrightarrow{\mathrm{r}}=-\overrightarrow{\mathrm{q}}+\frac{(\overrightarrow{\mathrm{p}} \cdot \overrightarrow{\mathrm{q}})}{(\overrightarrow{\mathrm{p}} \cdot \overrightarrow{\mathrm{p}})} \overrightarrow{\mathrm{p}}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/-JPZaU-KfikZttVnXRDQ5uyXuvNvhVptDHXD7m2BFEs.original.fullsize.png">

</details>

---

### Q59. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

The resultant of two forces $\mathrm{P~N}$ and $3 \mathrm{~N}$ is a force of $7 \mathrm{~N}$. If the direction of $3 \mathrm{~N}$ force were reversed, the resultant would be $\sqrt{19} \mathrm{~N}$. The value of $\mathrm{P}$ is

**Options:**

- **(A)** $5 \mathrm{~N}$
- **(B)** $6 \mathrm{~N}$
- **(C)** $3 \mathrm{~N}$
- **(D)** $4 \mathrm{~N}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5 \mathrm{~N}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/zSxUTGY5QCK2424Wy8kFzqI5moFKhrWdXKSHmMhrxTQ.original.fullsize.png">

$\begin{aligned}
& 7^2=P^2+3^2+2 \times 3 \times P \cos \theta \quad \dots(1)\\
& (\sqrt{19})^2=P^2+(-3)^2+2 \times(-3) \times P \cos \theta \quad \dots (2)
\end{aligned}$
adding we get
$68=2 P^2+18 \Rightarrow P=5$.

</details>

---

### Q60. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

A particle has two velocities of equal magnitude inclined to each other at an angle $\theta$. If one of them is halved, the angle between the other and the original resultant velocity is bisected by the new resultant. Then $\theta$ is

**Options:**

- **(A)** $90^{\circ}$
- **(B)** $120^{\circ}$
- **(C)** $45^{\circ}$
- **(D)** $60^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $120^{\circ}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/_GUQrma8dLPeZmZj-KZWkpLjOkuwVa3_TEZyZy6I9WU.original.fullsize.png">

$\tan \frac{\theta}{4}=\frac{\frac{u}{2} \sin \theta}{u+\frac{u}{2} \cos \theta}$
$\Rightarrow \sin \frac{\theta}{4}+\frac{1}{2} \sin \frac{\theta}{4} \cos \theta=\frac{1}{2} \sin \theta \cos \frac{\theta}{4}$
$\therefore 2 \sin \frac{\theta}{4}=\sin \frac{3 \theta}{4}=3 \sin \frac{\theta}{4}-4 \sin ^3 \frac{\theta}{4}$
$\therefore \sin ^2 \frac{\theta}{4}=\frac{1}{4} \Rightarrow \frac{\theta}{4}=30^{\circ}$ or $\theta=120^{\circ}$

</details>

---

### Q61. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

$A B C$ is a triangle, right angled at $A$. The resultant of the forces acting along $\overrightarrow{A B}, \overrightarrow{A C}$ with magnitudes $\frac{1}{A B}$ and $\frac{1}{A C}$ respectively is the force along $\overrightarrow{A D}$, where $D$ is the foot of the perpendicular from $\mathrm{A}$ onto $\mathrm{BC}$. The magnitude of the resultant is

**Options:**

- **(A)** $\frac{A B^2+A C^2}{(A B)^2(A C)^2}$
- **(B)** $\frac{(A B)(A C)}{A B+A C}$
- **(C)** $\frac{1}{A B}+\frac{1}{A C}$
- **(D)** $\frac{1}{\mathrm{AD}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{\mathrm{AD}}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/J0NfjRN0dQ9H6KoTHx873U7FABgHDz89d0B4gHURfII.original.fullsize.png">

Magnitude of resultant
$$
\begin{aligned}
& =\sqrt{\left(\frac{1}{A B}\right)^2+\left(\frac{1}{A C}\right)^2}=\frac{\sqrt{A B^2+A C^2}}{A B \cdot A C} \\
& =\frac{B C}{A B \cdot A C}=\frac{B C}{A D \cdot B C}=\frac{1}{A D}
\end{aligned}
$$

</details>

---

### Q62. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

The resultant $R$ of two forces acting on a particle is at right angles to one of them and its magnitude is one third of the other force. The ratio of larger force to smaller one is

**Options:**

- **(A)** $2: 1$
- **(B)** $3: \sqrt{2}$
- **(C)** $3: 2$
- **(D)** $3: 2 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3: 2 \sqrt{2}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/88H2wz8D5yxrNSja2_u3kk-jmC2VAk5yF8WBaFfBDVs.original.fullsize.png">

$\mathrm{F}^{\prime}=3 \mathrm{~F} \cos \theta$
$\mathrm{F}=3 \mathrm{~F} \sin \theta$
$\Rightarrow \mathrm{F}^{\prime}=2 \sqrt{2} \mathrm{~F}$
$\mathrm{~F}: \mathrm{F}^{\prime}:: 3: 2 \sqrt{2}$.

</details>

---

### Q63. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

If $\vec{a}, \vec{b}, \vec{c}$ are non-coplanar vectors and $\lambda$ is a real number then $\left[\lambda(\vec{a}+\vec{b}) \lambda^2 \vec{b} \lambda \vec{c}\right]=[\vec{a} \vec{b}+\vec{c} \vec{b}]$ for

**Options:**

- **(A)** exactly one value of $\lambda$
- **(B)** no value of $\lambda$
- **(C)** exactly three values of $\lambda$
- **(D)** exactly two values of $\lambda$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) no value of $\lambda$**

**Detailed Solution:**

$$
\begin{aligned}
& {\left[\begin{array}{lll}
\lambda(\vec{a}+\vec{b}) & \lambda^2 \vec{b} & \lambda \vec{c}
\end{array}\right]=\left[\begin{array}{lll}
\vec{a} & \vec{b}+\vec{c} & \vec{b}
\end{array}\right]} \\
& \left|\begin{array}{ccc}
\lambda & \lambda & 0 \\
0 & \lambda^2 & 0 \\
0 & 0 & \lambda
\end{array}\right|=\left|\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 1 \\
0 & 1 & 0
\end{array}\right| \\
& \Rightarrow \lambda^4=-1 \\
&
\end{aligned}
$$
Hence no real value of $\lambda$.

</details>

---

### Q64. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

If $C$ is the mid point of $A B$ and $P$ is any point outside $A B$, then

**Options:**

- **(A)** $\overrightarrow{\mathrm{PA}}+\overrightarrow{\mathrm{PB}}=2 \overrightarrow{\mathrm{PC}}$
- **(B)** $\overrightarrow{\mathrm{PA}}+\overrightarrow{\mathrm{PB}}+2 \overrightarrow{\mathrm{PC}}=0$
- **(C)** $\overrightarrow{\mathrm{PA}}+\overrightarrow{\mathrm{PB}}+ \overrightarrow{\mathrm{PC}}=0$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\overrightarrow{\mathrm{PA}}+\overrightarrow{\mathrm{PB}}=2 \overrightarrow{\mathrm{PC}}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/343ZBMNJb57jLTF3_r9SpTDNsQPuJdL1GYCOTbGkYpQ.original.fullsize.png">

$$
\begin{aligned}
& \overrightarrow{\mathrm{PA}}+\overrightarrow{\mathrm{AC}}+\overrightarrow{\mathrm{CP}}=0 \\
& \overline{\mathrm{PB}}+\overrightarrow{\mathrm{BC}}+\overrightarrow{\mathrm{CP}}=0
\end{aligned}
$$
Adding, we get
$$
\overrightarrow{\mathrm{PA}}+\overrightarrow{\mathrm{PB}}+\overrightarrow{\mathrm{AC}}+\overrightarrow{\mathrm{BC}}+2 \overrightarrow{\mathrm{CP}}=0
$$
Since $\overrightarrow{A C}=-\overrightarrow{B C}$
$$
\begin{aligned}
& \& \overrightarrow{\mathrm{CP}}=-\overrightarrow{\mathrm{PC}} \\
& \Rightarrow \overrightarrow{\mathrm{PA}}+\overrightarrow{\mathrm{PB}}-2 \overrightarrow{\mathrm{PC}}=0 .
\end{aligned}
$$

</details>

---

### Q65. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

A velocity $\frac{1}{4} \mathrm{~m} / \mathrm{s}$ is resolved into two components along $\mathrm{OA}$ and $\mathrm{OB}$ making angles $30^{\circ}$ and $45^{\circ}$ respectively with the given velocity. Then the component along $\mathrm{OB}$ is

**Options:**

- **(A)** $\frac{1}{8} \mathrm{~m} / \mathrm{s}$
- **(B)** $\frac{1}{4}(\sqrt{3}-1) \mathrm{m} / \mathrm{s}$
- **(C)** $\frac{1}{4} \mathrm{~m} / \mathrm{s}$
- **(D)** $\frac{1}{8}(\sqrt{6}-\sqrt{2}) \mathrm{m} / \mathrm{s}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{8}(\sqrt{6}-\sqrt{2}) \mathrm{m} / \mathrm{s}$**

**Detailed Solution:**

Component along $\mathrm{OB}=\frac{\frac{1}{4} \sin 30^{\circ}}{\sin \left(45^{\circ}+30^{\circ}\right)}=\frac{1}{8}(\sqrt{6}-\sqrt{2}) \mathrm{m} / \mathrm{s}$.

</details>

---

### Q66. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

Three forces $\vec{P}, \vec{Q}$ and $\vec{R}$ acting along IA, IB and IC, where I is the incentre of a $\triangle A B C$, are in equilibrium. Then $\vec{P}: \vec{Q}: \vec{R}$ is

**Options:**

- **(A)** $\cos \frac{A}{2}: \cos \frac{B}{2}: \cos \frac{C}{2}$
- **(B)** $\sin \frac{A}{2}: \sin \frac{B}{2}: \sin \frac{C}{2}$
- **(C)** $\sec \frac{A}{2}: \sec \frac{B}{2}: \sec \frac{C}{2}$
- **(D)** $\operatorname{cosec} \frac{A}{2}: \operatorname{cosec} \frac{B}{2}: \operatorname{cosec} \frac{C}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\cos \frac{A}{2}: \cos \frac{B}{2}: \cos \frac{C}{2}$**

**Detailed Solution:**

By Lami's theorem
$$
\begin{aligned}
& \vec{P}: \vec{Q}: \vec{R}=\sin \left(90^{\circ}+\frac{A}{2}\right): \sin \left(90^{\circ}+\frac{B}{2}\right): \sin \left(90^{\circ}+\frac{C}{2}\right) \\
& \Rightarrow \cos \frac{A}{2}: \cos \frac{B}{2}: \cos \frac{C}{2} .
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EJGWEbzIzvbKED_KCAj_rG8c6xAHxABi4MG2luhcbUo.original.fullsize.png">

</details>

---

### Q67. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

In a right angle $\triangle \mathrm{ABC}, \angle \mathrm{A}=90^{\circ}$ and sides a, b, c are respectively, $5 \mathrm{~cm}, 4 \mathrm{~cm}$ and $3 \mathrm{~cm}$. If a force $\vec{F}$ has moments 0,9 and 16 in $N$ cm. units respectively about vertices $A, B$ and $C$, then magnitude of $\vec{F}$ is

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 5
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5**

**Detailed Solution:**

$\mathrm{F} \cdot 3 \sin \theta=9$
$\mathrm{~F} \cdot 4 \cos \theta=16$
$\Rightarrow \mathrm{F}=5$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9WJucfMi4S6ULrzpXQTjXKhHofPbMl4j2a9njmHKhWo.original.fullsize.png">

</details>

---

### Q68. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

Let $\overline{\mathrm{a}}, \overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$ be non-zero vectors such that $(\overline{\mathrm{a}} \times \overline{\mathrm{b}}) \times \overline{\mathrm{c}}=\frac{1}{3}|\overline{\mathrm{b}}||\overline{\mathrm{c}}| \overline{\mathrm{a}}$. If $\theta$ is the acute angle between the vectors $\overline{\mathrm{b}}$ and $\overline{\mathrm{c}}$, then $\sin \theta$ equals

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{\sqrt{2}}{3}$
- **(C)** $\frac{2}{3}$
- **(D)** $\frac{2 \sqrt{2}}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2 \sqrt{2}}{3}$**

**Detailed Solution:**

$(\overrightarrow{\mathrm{a}} \times \overrightarrow{\mathrm{b}}) \times \overrightarrow{\mathrm{c}}=\frac{1}{3}|\overrightarrow{\mathrm{b}}||\overline{\mathrm{c}}| \overline{\mathrm{a}} \Rightarrow(\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{c}}) \overrightarrow{\mathrm{b}}-(\overrightarrow{\mathrm{b}} \cdot \overrightarrow{\mathrm{c}}) \overrightarrow{\mathrm{a}}=\frac{1}{3}|\overline{\mathrm{b}}||\overline{\mathrm{c}}| \overline{\mathrm{a}}$
$\Rightarrow(\overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{c}}) \overrightarrow{\mathrm{b}}=\left(\frac{1}{3}|\overline{\mathrm{b}}||\overline{\mathrm{c}}|+(\overline{\mathrm{b}} \cdot \overline{\mathrm{c}})\right) \overrightarrow{\mathrm{a}} \Rightarrow \overrightarrow{\mathrm{a}} \cdot \overrightarrow{\mathrm{c}}=0$ and $\frac{1}{3}|\overline{\mathrm{b}}||\overline{\mathrm{c}}|+(\overline{\mathrm{b}} \cdot \overline{\mathrm{c}})=0$
$\Rightarrow|\overline{\mathrm{b}}||\overline{\mathrm{c}}|\left(\frac{1}{3}+\cos \theta\right)=0 \Rightarrow \cos \theta=-1 / 3 \Rightarrow \sin \theta=\frac{2 \sqrt{2}}{3}$

</details>

---

### Q69. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

If $\bar{a}, \bar{b}, \bar{c}$ are non-coplanar vectors and $\lambda$ is a real number, then the vectors $\overline{\mathrm{a}}+2 \overline{\mathrm{b}}+3 \overline{\mathrm{c}}, \lambda \overline{\mathrm{b}}+4 \overline{\mathrm{c}}$ and $(2 \lambda-1) \overline{\mathrm{c}}$ are non-coplanar for

**Options:**

- **(A)** all values of $\lambda$
- **(B)** all except one value of $\lambda$
- **(C)** all except two values of $\lambda$
- **(D)** no value of $\lambda$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) all except two values of $\lambda$**

**Detailed Solution:**

Condition for given three vectors to be coplanar is $\left|\begin{array}{ccc}1 & 2 & 3 \\ 0 & \lambda & 4 \\ 0 & 0 & 2 \lambda-1\end{array}\right|=0 \Rightarrow \lambda=0,1 / 2$
Hence given vectors will be non coplanar for all real values of $\lambda$ except $0,1 / 2$

</details>

---

### Q70. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

Let $\vec{a}, \vec{b}$ and $\vec{c}$ be three non-zero vectors such that no two of these are collinear. If the vector $\vec{a}+2 \vec{b}$ is collinear with $\vec{c}$ and $\vec{b}+3 \vec{c}$ is collinear with $\vec{a}$ ( $\lambda$ being some non-zero scalar) then $\vec{a}+2 \vec{b}+6 \vec{c}$ equals

**Options:**

- **(A)** $\lambda \vec{a}$
- **(B)** $\lambda \vec{b}$
- **(C)** $\lambda \overrightarrow{\mathbf{c}}$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

$(\vec{a}+2 b)=t_1 \vec{c}$
and $\vec{b}+3 \vec{c}=t_2 \vec{a}$
$(1)-2 \times(2) \Rightarrow \vec{a}\left(1+2 t_2\right)+\vec{c}\left(-t_1-6\right)=0 \Rightarrow 1+2 t_2=0 \Rightarrow t_2=-1 / 2 \& t_1=-6$.
Since $\vec{a}$ and $\vec{c}$ are non-collinear.
Putting the value of $t_1$ and $t_2$ in (1) and (2), we get $\vec{a}+2 \vec{b}+6 \vec{c}=\overrightarrow{0}$

</details>

---

### Q71. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

If the straight lines $x=1+s, y=-3-\lambda s, z=1+\lambda s$ and $x=\frac{t}{2}, y=1+t, z=2-t$ with parameters $s$ and $t$ respectively, are co-planar then $\lambda$ equals

**Options:**

- **(A)** $-2$
- **(B)** $-1$
- **(C)** $-\frac{1}{2}$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-2$**

**Detailed Solution:**

Given lines $\frac{x-1}{1}=\frac{y+s}{-\lambda}=\frac{z-1}{\lambda}=s$ and $\frac{x}{1 / 2}=\frac{y-1}{1}=\frac{z-2}{-1}=t$ are coplanar then plan passing through these lines has normal perpendicular to these lines $\Rightarrow a-b \lambda+c \lambda=0 \quad$ and $\frac{a}{2}+b-c=0$ (where $a, b, c$ are direction ratios of the normal to the plan) On solving, we get $\lambda=-2$

</details>

---

### Q72. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

If $\vec{u}, \vec{v}$ and $\vec{w}$ are three non-coplanar vectors, then $(\vec{u}+\vec{v}-\vec{w}) .(\vec{u}-\vec{v}) \times(\vec{v}-\vec{w})$ equals

**Options:**

- **(A)** $3 \vec{u} . \vec{v} \times \vec{w}$
- **(B)** 0
- **(C)** $\overrightarrow{\mathrm{u}} \cdot \overrightarrow{\mathrm{v}} \times \overrightarrow{\mathrm{w}}$
- **(D)** $\overrightarrow{\mathrm{u}} \cdot \overrightarrow{\mathrm{w}} \times \overrightarrow{\mathrm{v}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\overrightarrow{\mathrm{u}} \cdot \overrightarrow{\mathrm{v}} \times \overrightarrow{\mathrm{w}}$**

**Detailed Solution:**

$(\overrightarrow{\mathrm{u}}+\overrightarrow{\mathrm{v}}-\overrightarrow{\mathrm{w}}) \cdot(\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{v}}-\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{w}}-\overrightarrow{\mathrm{v}} \times \overrightarrow{\mathrm{v}}+\overrightarrow{\mathrm{v}} \times \overrightarrow{\mathrm{w}})$
$(\overrightarrow{\mathrm{u}}+\overrightarrow{\mathrm{v}}-\overrightarrow{\mathrm{w}}) \cdot(\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{v}}-\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{w}}+\overrightarrow{\mathrm{v}} \times \overrightarrow{\mathrm{w}})=\frac{\overrightarrow{\mathrm{u}} \cdot(\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{v}})}{0}$
$-\frac{\overrightarrow{\mathrm{u}} .(\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{w}})}{0}+\overrightarrow{\mathrm{u}} .(\overrightarrow{\mathrm{v}} \times \overrightarrow{\mathrm{w}})+\frac{\overrightarrow{\mathrm{v}} \cdot(\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{v}})}{0}-\overrightarrow{\mathrm{v}} \cdot(\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{w}})$
$+\frac{\overrightarrow{\mathrm{v}} \cdot(\overrightarrow{\mathrm{v}} \times \overrightarrow{\mathrm{w}})}{0}-\overrightarrow{\mathrm{w}} \cdot(\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{v}})+\frac{\overrightarrow{\mathrm{w}} \cdot(\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{w}})}{0}-\frac{\overrightarrow{\mathrm{w}} \cdot(\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{w}})}{0}=\overrightarrow{\mathrm{u}} \cdot(\overrightarrow{\mathrm{v}} \times \overrightarrow{\mathrm{w}})-\overrightarrow{\mathrm{v}} \cdot(\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{w}})-\overrightarrow{\mathrm{w}} \cdot(\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{v}})$
$=[\overrightarrow{\mathrm{u}} \overrightarrow{\mathrm{v}} \overrightarrow{\mathrm{w}}]+[\overrightarrow{\mathrm{v}} \overrightarrow{\mathrm{w}} \overrightarrow{\mathrm{u}}]-[\overrightarrow{\mathrm{w}} \overrightarrow{\mathrm{u}} \overrightarrow{\mathrm{v}}]=\overrightarrow{\mathrm{u}} .(\overrightarrow{\mathrm{v}} \times \overrightarrow{\mathrm{w}})$

</details>

---

### Q73. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

Consider points A, B, C and D with position vectors $7 \hat{\mathrm{i}}-4 \hat{\mathrm{j}}+7 \hat{\mathrm{k}}, \hat{\mathrm{i}}-6 \hat{\mathrm{j}}+10 \hat{\mathrm{k}},-\hat{\mathrm{i}}-3 \hat{\mathrm{j}}+4 \hat{\mathrm{k}}$ and $5 \hat{\mathrm{i}}-\hat{\mathrm{j}}+5 \hat{\mathrm{k}}$ respectively. Then $\mathrm{ABCD}$ is a

**Options:**

- **(A)** parallelogram but not a rhombus
- **(B)** square
- **(C)** rhombus
- **(D)** rectangle

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) rhombus**

**Detailed Solution:**

No option satisfied wrong.
$\mathrm{A}=(7,-4,7), \mathrm{B}=(1,-6,10), \mathrm{C}=(-1,-3,4)$ and $\mathrm{D}=(5,-1,5)$
$A B=\sqrt{(7-1)^2+(-4+6)^2+(7-10)^2}=\sqrt{36+4+9}=7$
Similarly $\mathrm{BC}=7, \mathrm{CD}=\sqrt{41}, \mathrm{DA}=\sqrt{17}$

</details>

---

### Q74. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

If $\left|\begin{array}{lll}a & a^2 & 1+a^3 \\ b & b^2 & 1+b^3 \\ c & c^2 & 1+c^3\end{array}\right|=0$ and vectors $\left(1, a, a^2\right),\left(a, b, b^2\right)$ and $\left(a, c, c^2\right)$ are non-coplanar, then the product abc equals

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** $-1$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-1$**

**Detailed Solution:**

$\left|\begin{array}{lll}\mathrm{a} & \mathrm{a}^2 & 1+\mathrm{a}^3 \\ \mathrm{~b} & \mathrm{~b}^2 & 1+\mathrm{b}^3 \\ \mathrm{c} & \mathrm{c}^2 & 1+\mathrm{c}^3\end{array}\right|=0 \Rightarrow\left|\begin{array}{lll}\mathrm{a} & \mathrm{a}^2 & 1 \\ \mathrm{~b} & \mathrm{~b}^2 & 1 \\ \mathrm{c} & \mathrm{c}^2 & 1\end{array}\right|+\left|\begin{array}{ccc}\mathrm{a} & \mathrm{a}^2 & \mathrm{a}^3 \\ \mathrm{~b} & \mathrm{~b}^2 & \mathrm{~b}^3 \\ \mathrm{c} & \mathrm{c}^2 & \mathrm{c}^3\end{array}\right|=0$
$(a-b)(b-c)(c-a)+a b c(a-b)(b-c)(c-a)=0$
$(a b c+1)[(a-b)(b-c)(c-a)]=0$
As $\left|\begin{array}{lll}1 & \mathrm{a} & \mathrm{a}^2 \\ 1 & \mathrm{~b} & \mathrm{~b}^2 \\ 1 & \mathrm{c} & \mathrm{c}^2\end{array}\right| \neq 0$ (given condition) $\quad \therefore \mathrm{abc}=-1$

</details>

---

### Q75. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

$\vec{a}, \vec{b}, \vec{c}$ are 3 vectors, such that $\vec{a}+\vec{b}+\vec{c}=0,|\vec{a}|=1,|\vec{b}|=2 \mid \vec{a}$ then $\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a}$ is equal to

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** $-7$
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-7$**

**Detailed Solution:**

$\vec{a}+\vec{b}+\vec{c}=0 \Rightarrow(\vec{a}+\vec{b}+\vec{c}) \cdot(\vec{a}+\vec{b}+\vec{c})=0$
$|\vec{a}|^2+|\vec{b}|^2+|\vec{c}|^2+2(\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a})=0$
$\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a}=\frac{-1-4-9}{2}=-7$

</details>

---

### Q76. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

The lines $\frac{\mathrm{x}-2}{1}=\frac{\mathrm{y}-3}{1}=\frac{\mathrm{z}-4}{-\mathrm{k}}$ and $\frac{\mathrm{x}-1}{\mathrm{k}}=\frac{\mathrm{y}-4}{1}=\frac{\mathrm{z}-5}{1}$ are coplanar if

**Options:**

- **(A)** $\mathrm{k}=3$ or $-2$
- **(B)** $\mathrm{k}=0$ or $-1$
- **(C)** $\mathrm{k}=1$ or $-1$
- **(D)** $\mathrm{k}=0$ or $-3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{k}=0$ or $-3$**

**Detailed Solution:**

$\left|\begin{array}{ccc}\mathrm{x}_2-\mathrm{x}_1 & \mathrm{y}_2-\mathrm{y}_1 & \mathrm{z}_2-\mathrm{z}_1 \\ \mathrm{l}_1 & \mathrm{~m}_1 & \mathrm{n}_1 \\ \mathrm{l}_2 & \mathrm{~m}_2 & \mathrm{n}_2\end{array}\right|=0$
$\left|\begin{array}{ccc}1 & -1 & -1 \\ 1 & 1 & -\mathrm{k} \\ \mathrm{k} & 2 & 1\end{array}\right|=0 \Rightarrow\left|\begin{array}{ccc}0 & 0 & -1 \\ 2 & 1+\mathrm{k} & -\mathrm{k} \\ \mathrm{k}+2 & 1 & 1\end{array}\right|=0$
$\mathrm{k}^2+3 \mathrm{k}^2=0 \Rightarrow \mathrm{k}(\mathrm{k}+3)=0$ or $\mathrm{k}=0$ or $-3$

</details>

---

### Q77. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

Let $\overrightarrow{\mathrm{u}}=\hat{\mathrm{i}}+\hat{\mathrm{j}}, \overrightarrow{\mathrm{v}}=\hat{\mathrm{i}}-\hat{\mathrm{j}}$ and $\overrightarrow{\mathrm{w}}=\hat{\mathrm{i}}+2 \hat{\mathrm{j}}+3 \hat{\mathrm{k}}$. If $\hat{\mathrm{n}}$ is a unit vector such that $\vec{u} \cdot \hat{n}=0$ and $\overrightarrow{\mathrm{v}} \cdot \hat{\mathrm{n}}=0$, then $|\overrightarrow{\mathrm{w}} \cdot \hat{\mathrm{n}}|$ is equal to

**Options:**

- **(A)** 3
- **(B)** 0
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

Since $\overrightarrow{\mathrm{n}}$ is perpendicular $\overrightarrow{\mathrm{u}}$ and $\overrightarrow{\mathrm{v}}, \overrightarrow{\mathrm{n}}=\overrightarrow{\mathrm{u}} \times \overrightarrow{\mathrm{v}}$
$\hat{\mathrm{n}}=\frac{\left|\begin{array}{ccc}\mathrm{i} & \mathrm{j} & \mathrm{k} \\ 1 & 1 & 0 \\ 1 & -1 & 0\end{array}\right|}{\sqrt{2} \times \sqrt{2}}=\frac{-2 \hat{\mathrm{k}}}{2}=-\hat{\mathrm{k}}$
$|\vec{\omega} \cdot \hat{n}|=|(\mathrm{i}+2 \mathrm{j}+3 \mathrm{k}) \cdot(-\mathrm{k})|=|-3|=3$

</details>

---

### Q78. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

The resultant of forces $\overrightarrow{\mathrm{P}}$ and $\overrightarrow{\mathrm{Q}}$ is $\overrightarrow{\mathrm{R}}$. If $\overrightarrow{\mathrm{Q}}$ is doubled then $\overrightarrow{\mathrm{R}}$ is doubled. If the direction of $\overrightarrow{\mathrm{Q}}$ is reversed, then $\overrightarrow{\mathrm{R}}$ is again doubled. Then $\mathrm{P}^2: \mathrm{Q}^2: \mathrm{R}^2$ is

**Options:**

- **(A)** $2: 3: 1$
- **(B)** $3: 1: 1$
- **(C)** $2: 3: 2$
- **(D)** $1: 2: 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2: 3: 2$**

**Detailed Solution:**

$\mathrm{R}^2=\mathrm{P}^2+\mathrm{Q}^2+2 \mathrm{PQ} \cos \theta$   <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/PdScUAByTN7sn94K5p9Hc9cjEEXHW-PHjdKwLWiAfbY.original.fullsize.png">

$4 \mathrm{R}^2=\mathrm{P}^2+4 \mathrm{Q}^2+4 \mathrm{PQ} \cos \theta$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/_FHkg6ewJ3DFjGfjI4YVFBLaKuOk2buq4meeZBkdhPE.original.fullsize.png">

$4 \mathrm{R}^2=\mathrm{P}^2+\mathrm{Q}^2-2 \mathrm{PQ} \cos \theta$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cPFJ9843Sj6Od3Amb5MDGrcBB_usOHPhHk4EE2gmesM.original.fullsize.png">

$\mathrm{On}(1)+(2), 5 \mathrm{R}^2=2 \mathrm{P}^2+2 \mathrm{Q}^2$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/wmg7jCNcZ0fokDgVXL2dsoQp-j9GOYlEMreClYYm2Pg.original.fullsize.png">

$\mathrm{On}(3) \times 2+(2), 12 \mathrm{R}^2=3 \mathrm{P}^2+6 \mathrm{Q}^2$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3qkvJk1g4i83h5QG7_9xDn_lDV3wd7haiWCJUWSzYBM.original.fullsize.png">

$2 \mathrm{P}^2+2 \mathrm{Q}^2-5 \mathrm{R}^2=0$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/OQmuio8EOPK6elll3ZYLb31BjXLR9q89AOKAqY7N3p8.original.fullsize.png">

$3 \mathrm{P}^2+6 \mathrm{Q}^2-12 \mathrm{R}^2=0$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7NIW9RLHahH9SaJjL5yh6uyZ4jZsZMnBQsKEdk4H_QI.original.fullsize.png">

$\frac{\mathrm{P}^2}{-24+30}=\frac{\mathrm{Q}^2}{24-15}=\frac{\mathrm{R}^2}{12-6}$
$\frac{\mathrm{P}^2}{6}=\frac{\mathrm{Q}^2}{9}=\frac{\mathrm{R}^2}{6}$ or $\mathrm{P}^2: \mathrm{Q}^2: \mathrm{R}^2=2: 3: 2$

</details>

---

### Q79. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

The sum of two forces is 18 N and resultant whose direction is at right angles to the smaller force is 12 N. The magnitude of the two forces are

**Options:**

- **(A)** 13, 5
- **(B)** 12, 6
- **(C)** 14, 4
- **(D)** 11, 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 13, 5**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/roNZaIRq2FOecWERkk1hnSe9QJK8Rdzo3sixtbuY1G4.original.fullsize.png">

Let two forces be $P$ and $Q$. Given $P+Q=18$ and $P \hat{a}+Q \hat{b}=12 \hat{c} \Rightarrow P \hat{a}-12 \hat{c}=\bar{Q} \hat{b}$
$$
\begin{aligned}
& \Rightarrow P^2+144=Q^2=(18-P)^2 ; \Rightarrow P^2+144=324-36 P+P^2 \\
& \Rightarrow 36 P=180 \Rightarrow P=5 \text { and } Q=13
\end{aligned}
$$
(where $\vec{a}$ and $\vec{b}$ are unit vectors along $P$ and $Q$ ).

</details>

---

