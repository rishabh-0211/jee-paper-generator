# MHT CET Mathematics - Sequences and Series

## Topic 1: Arithmetic Progression

**Total Questions:** 10

---

### Q1. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $a_1, a_2, a_3, \ldots, a_n$ are in arithmetic progression with common difference d, then $\tan\left[\tan^{-1}\left(\dfrac{d}{1 + a_1 a_2}\right) + \tan^{-1}\left(\dfrac{d}{1 + a_2 a_3}\right) + \ldots + \tan^{-1}\left(\dfrac{d}{1 + a_{n-1} a_n}\right)\right] = $ ____

**Options:**

- **(A)** $\dfrac{a_1 - a_n}{1 + a_1 a_n}$
- **(B)** $\dfrac{a_n - a_1}{1 - a_1 a_n}$
- **(C)** $\dfrac{a_n - a_1}{1 + a_1 a_n}$
- **(D)** $\dfrac{a_1 + a_n}{1 + a_1 a_n}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{a_n - a_1}{1 + a_1 a_n}$**

**Detailed Solution:**

Given $a_1, a_2, \ldots, a_n$ are in arithmetic progression with common difference $d$.

$d = a_2 - a_1 = a_3 - a_2 = \ldots = a_n - a_{n-1}$

The general term of the series is:

$\tan^{-1}\left(\dfrac{d}{1 + a_k a_{k+1}}\right) = \tan^{-1}\left(\dfrac{a_{k+1} - a_k}{1 + a_k a_{k+1}}\right)$

Using the identity $\tan^{-1}\left(\dfrac{x - y}{1 + xy}\right) = \tan^{-1} x - \tan^{-1} y$, we get:

$\tan^{-1}\left(\dfrac{a_{k+1} - a_k}{1 + a_k a_{k+1}}\right) = \tan^{-1} a_{k+1} - \tan^{-1} a_k$

Let $S$ be the sum of the inverse trigonometric series:

$S = \sum_{k=1}^{n-1} \tan^{-1}\left(\dfrac{d}{1 + a_k a_{k+1}}\right)$

$S = (\tan^{-1} a_2 - \tan^{-1} a_1) + (\tan^{-1} a_3 - \tan^{-1} a_2) + \ldots + (\tan^{-1} a_n - \tan^{-1} a_{n-1})$

This is a telescoping sum, which simplifies to:

$S = \tan^{-1} a_n - \tan^{-1} a_1$

Applying the inverse tangent difference formula:

$S = \tan^{-1}\left(\dfrac{a_n - a_1}{1 + a_1 a_n}\right)$

The given expression is $\tan(S)$:

$\tan(S) = \tan\left[\tan^{-1}\left(\dfrac{a_n - a_1}{1 + a_1 a_n}\right)\right] = \dfrac{a_n - a_1}{1 + a_1 a_n}$

</details>

---

### Q2. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a right-angled $\triangle ABC$, the measures of the angles are in an Arithmetic Progression (A.P.) If its smallest side is $4$ units, then the area of $\triangle ABC$ is.....

**Options:**

- **(A)** $16$ sq. units
- **(B)** $8\sqrt{3}$ sq. units
- **(C)** $16\sqrt{3}$ sq. units
- **(D)** $32$ sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $8\sqrt{3}$ sq. units**

**Detailed Solution:**

Let the angles of the right-angled triangle be $a - d$, $a$, and $a + d$.

The sum of the angles in a triangle is $180^{\circ}$.

$(a - d) + a + (a + d) = 180^{\circ} \Rightarrow 3a = 180^{\circ} \Rightarrow a = 60^{\circ}$

Since the triangle is right-angled, the largest angle is $90^{\circ}$.

$a + d = 90^{\circ} \Rightarrow 60^{\circ} + d = 90^{\circ} \Rightarrow d = 30^{\circ}$

The angles of the triangle are $30^{\circ}$, $60^{\circ}$, and $90^{\circ}$.

The smallest side is opposite to the smallest angle, which is $30^{\circ}$. Let this side be $x = 4$ units.

The other perpendicular side, opposite to $60^{\circ}$, is $y = x \tan 60^{\circ} = 4\sqrt{3}$ units.

The area of the right-angled triangle is $\dfrac{1}{2} \times x \times y$.

Area $= \dfrac{1}{2} \times 4 \times 4\sqrt{3} = 8\sqrt{3}$ sq. units.

Answer: $8\sqrt{3}$ sq. units

</details>

---

### Q3. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $x, y, \mathrm{z}$ are in Arithmetic Progression and $\tan ^{-1} x, \tan ^{-1} y, \tan ^{-1} z$ are also in Arithmetic progression, where $x, \mathrm{z}\gt0$ and $x \mathrm{z} \lt 1, y \lt 1$, then

**Options:**

- **(A)** $x=y=z$
- **(B)** $2 x=3 y=6 z$
- **(C)** $6 x=3 y=2 z$
- **(D)** $6 x=4 y=3 z$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x=y=z$**

**Detailed Solution:**

Given $x, y, z$ are in Arithmetic Progression:

$2y = x + z$

Given $\tan^{-1} x, \tan^{-1} y, \tan^{-1} z$ are also in Arithmetic Progression:

$2 \tan^{-1} y = \tan^{-1} x + \tan^{-1} z$

Using the inverse trigonometric formulas for $y \lt 1$ and $xz \lt 1$:

$\tan^{-1} \left( \dfrac{2y}{1 - y^2} \right) = \tan^{-1} \left( \dfrac{x + z}{1 - xz} \right)$

Equating the arguments:

$\dfrac{2y}{1 - y^2} = \dfrac{x + z}{1 - xz}$

Substituting $2y = x + z$ into the equation:

$\dfrac{x + z}{1 - y^2} = \dfrac{x + z}{1 - xz}$

Since $x, z \gt 0$, $x + z \neq 0$. Dividing both sides by $x + z$ gives:

$\dfrac{1}{1 - y^2} = \dfrac{1}{1 - xz}$

$1 - y^2 = 1 - xz$

$y^2 = xz$

This shows that $x, y, z$ are also in Geometric Progression. Substituting $y = \dfrac{x + z}{2}$ into $y^2 = xz$ gives:

$\left( \dfrac{x + z}{2} \right)^2 = xz$

$x^2 + 2xz + z^2 = 4xz$

$x^2 - 2xz + z^2 = 0$

$(x - z)^2 = 0$

$x = z$

Substituting $x = z$ into $2y = x + z$ yields $2y = 2x$, so $x = y$.

Therefore, $x = y = z$.

Answer: $x=y=z$

</details>

---

### Q4. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin \left(\theta^{\circ}-\alpha\right), \sin \theta$ and $\sin (\theta+\alpha)$ are in H.P., then the value of $\cos ^2 \theta$ is

**Options:**

- **(A)** $1-2 \cos ^2 \dfrac{\alpha}{2}$
- **(B)** $1+2 \cos ^2 \dfrac{\alpha}{2}$
- **(C)** $1-4 \cos ^2 \dfrac{\alpha}{2}$
- **(D)** $\quad 1+4 \cos ^2 \dfrac{\alpha}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1-2 \cos ^2 \dfrac{\alpha}{2}$**

**Detailed Solution:**

Given that $\sin(\theta - \alpha)$, $\sin\theta$, and $\sin(\theta + \alpha)$ are in H.P., their reciprocals are in A.P.

$\dfrac{2}{\sin\theta} = \dfrac{1}{\sin(\theta - \alpha)} + \dfrac{1}{\sin(\theta + \alpha)}$

$\dfrac{2}{\sin\theta} = \dfrac{\sin(\theta + \alpha) + \sin(\theta - \alpha)}{\sin(\theta - \alpha)\sin(\theta + \alpha)}$

Using the sum-to-product formula in the numerator and the difference of squares formula in the denominator:

$\dfrac{2}{\sin\theta} = \dfrac{2\sin\theta\cos\alpha}{\sin^2\theta - \sin^2\alpha}$

Cross-multiplying gives:

$\sin^2\theta - \sin^2\alpha = \sin^2\theta\cos\alpha$

Rearranging the terms to group $\sin^2\theta$:

$\sin^2\theta(1 - \cos\alpha) = \sin^2\alpha$

Since $\sin^2\alpha = 1 - \cos^2\alpha = (1 - \cos\alpha)(1 + \cos\alpha)$, we can substitute this into the equation:

$\sin^2\theta(1 - \cos\alpha) = (1 - \cos\alpha)(1 + \cos\alpha)$

Assuming $1 - \cos\alpha \neq 0$, we divide both sides by $(1 - \cos\alpha)$:

$\sin^2\theta = 1 + \cos\alpha$

Using the identity $\sin^2\theta = 1 - \cos^2\theta$:

$1 - \cos^2\theta = 1 + \cos\alpha$

$\cos^2\theta = -\cos\alpha$

Using the half-angle identity $\cos\alpha = 2\cos^2\dfrac{\alpha}{2} - 1$:

$\cos^2\theta = -\left(2\cos^2\dfrac{\alpha}{2} - 1\right) = 1 - 2\cos^2\dfrac{\alpha}{2}$

Answer: $1-2 \cos ^2 \dfrac{\alpha}{2}$

</details>

---

### Q5. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Angles of a triangle are in the ratio $4: 1: 1$. Then the ratio of its greatest side to its perimeter is

**Options:**

- **(A)** $3:(2+\sqrt{3})$
- **(B)** $\sqrt{3}:(2+\sqrt{3})$
- **(C)** $\sqrt{3}:(2-\sqrt{3})$
- **(D)** $1:(2+\sqrt{3})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{3}:(2+\sqrt{3})$**

**Detailed Solution:**

Let the angles of the triangle be $4 x, x$ and $x$.
$$
\therefore 4 x+x+x=180^{\circ} \Rightarrow 6 x=180^{\circ} \Rightarrow x=30^{\circ}
$$
By sine rule,
$$
\begin{aligned}
& \frac{\sin 120^{\circ}}{\mathrm{a}}=\frac{\sin 30^{\circ}}{\mathrm{b}}=\frac{\sin 30^{\circ}}{\mathrm{c}} \\
\therefore \quad & \mathrm{a}:(\mathrm{a}+\mathrm{b}+\mathrm{c}) \\
& =\left(\sin 120^{\circ}\right):\left(\sin 120^{\circ}+\sin 30^{\circ}+\sin 30^{\circ}\right) \\
& =\frac{\sqrt{3}}{2}: \frac{\sqrt{3}+2}{2}=\sqrt{3}: \sqrt{3}+2
\end{aligned}
$$

</details>

---

### Q6. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The sides of a triangle are three consecutive natural numbers and its largest angle is twice the smallest one, then the sides of the triangle (in units) are

**Options:**

- **(A)** $3,4,5$
- **(B)** $4,5,6$
- **(C)** $5,6,7$
- **(D)** $2,3,4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4,5,6$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/lpHZd4XcROiL8d3saNHyzfeqPuWQbWKprNbZBBB-OME.original.fullsize.png">


Let $\mathrm{AC}=\mathrm{n}, \mathrm{AB}=\mathrm{n}+1, \mathrm{BC}=\mathrm{n}+2$
$\therefore \quad$ Largest angle is $\mathrm{A}$ and smallest angle is $\mathrm{B}$.
$$
\therefore \quad \mathrm{A}=2 \mathrm{~B}
$$
Since $\mathrm{A}+\mathrm{B}+\mathrm{C}=180^{\circ}$
$\therefore \quad 3 \mathrm{~B}+\mathrm{C}=180^{\circ}$
$$
\begin{aligned}
& \Rightarrow \mathrm{C}=180^{\circ}-3 \mathrm{~B} \\
& \Rightarrow \sin \mathrm{C}=\sin \left(180^{\circ}-3 \mathrm{~B}\right)=\sin 3 \mathrm{~B}
\end{aligned}
$$
By sine rule,
$$
\begin{aligned}
& \frac{\sin A}{n+2}=\frac{\sin B}{n}=\frac{\sin C}{n+1} \\
& \Rightarrow \frac{\sin 2 B}{n+2}=\frac{\sin B}{n}=\frac{\sin 3 B}{n+1} \\
& \Rightarrow \frac{2 \sin B \cos B}{n+2}=\frac{\sin B}{n}=\frac{3 \sin B-4 \sin ^3 B}{n+1} \\
& \Rightarrow \frac{2 \cos B}{n+2}=\frac{1}{n}=\frac{3-4 \sin ^2 B}{n+1} \\
\therefore & \cos B=\frac{n+2}{2 n}, 3-4 \sin ^2 B=\frac{n+1}{n} \\
\therefore \quad & 3-4\left(1-\cos ^2 B\right)=\frac{n+1}{n} \\
\therefore \quad & -4+4\left(\frac{n+2}{2 n}\right)^2=\frac{n+1}{n} \\
& \Rightarrow-1+\frac{n^2+4 n+4}{n^2}=\frac{n+1}{n} \\
& \Rightarrow-n^2+n^2+4 n+4=n^2+n \\
& \Rightarrow n^2-3 n-4=0 \\
& \Rightarrow(n+1)(n-4)=0 \\
& \Rightarrow n=-1 \text { or } n=4
\end{aligned}
$$
But $\mathrm{n}$ cannot be negative.
$$
\therefore \mathrm{n}=4
$$
$\therefore \quad$ The sides of the $\Delta$ are $4,5,6$.

</details>

---

### Q7. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The lengths of sides of a triangle are three consecutive natural numbers and its largest angle is twice the smallest one. Then the length of the sides of the triangle (in units) are

**Options:**

- **(A)** $3,4,5$
- **(B)** $4,5,6$
- **(C)** $5,6,7$
- **(D)** $2,3,4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4,5,6$**

**Detailed Solution:**

Let $a, a+1, a+2$ be the sides of the triangle and $\mathrm{A}, \mathrm{B}, \mathrm{C}$ be the angles opposite to them respectively.

According to the given condition,
$$
\mathrm{C}=2 \mathrm{~A}
$$
$$
\begin{aligned}
\therefore \quad \sin C & =\sin 2 A \\
\sin C & =2 \sin A \cos A
\end{aligned}
$$

Note that $\frac{\sin A}{a}=\frac{\sin C}{a+2}=k$
$$
\begin{aligned}
& \begin{array}{l}
\Rightarrow \sin A=k a \text { and } \sin C=k(a+2) \\
\text { Also, } \cos A=\frac{(a+1)^2+(a+2)^2-a^2}{2(a+1)(a+2)} \\
=\frac{a^2+2 a+1+a^2+4 a+4-a^2}{2\left(a^2+3 a+2\right)} \\
=\frac{a^2+6 a+5}{2\left(a^2+3 a+2\right)} \\
\therefore \quad(i) \Rightarrow k(a+2)=2 \times k a \times \frac{a^2+6 a+5}{2\left(a^2+3 a+2\right)} \\
\therefore \quad a+2=\frac{a\left(a^2+6 a+5\right)}{\left(a^2+3 a+2\right)} \\
\therefore \quad(a+2)\left(a^2+3 a+2\right)=a^3+6 a^2+5 a
\end{array}
\end{aligned}
$$
$$
\begin{array}{ll}
\therefore & a^3+5 a^2+8 a+4=a^3+6 a^2+5 a \\
\therefore & a^2-3 a-4=0 \\
\therefore & (a-4)(a+1)=0 \\
& \Rightarrow a=4 \text { or }-1
\end{array}
$$

But $\mathrm{a}=-1$ is not possible.
$\therefore \quad 4,5,6$ are the lengths of the sides of the triangle.

</details>

---

### Q8. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x, y, \mathrm{z}$ are in A.P. and $\tan ^{-1} x, \tan ^{-1} y$ and $\tan ^{-1} z$ are also in A.P., then

**Options:**

- **(A)** $x=y=\mathrm{z}$
- **(B)** $2 x=3 y=6 z$
- **(C)** $6 x=3 y=2 z$
- **(D)** $6 x=4 y=3 z$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x=y=\mathrm{z}$**

**Detailed Solution:**

Given, $x, y, \mathrm{z}$ are in A.P.
$\therefore \quad 2 y=x+z... (i)$
Also,
$\begin{aligned}
& \tan ^{-1} x, \tan ^{-1} y, \tan ^{-1} z \text { are in A.P. } \\
\therefore \quad & 2 \tan ^{-1} y=\tan ^{-1} x+\tan ^{-1} z \\
& \Rightarrow \tan ^{-1}\left(\frac{2 y}{1-y^2}\right)=\tan ^{-1}\left(\frac{x+z}{1-x z}\right) \\
& \Rightarrow \frac{2 y}{1-y^2}=\frac{x+z}{1-x z} \\
& \Rightarrow \frac{2 y}{1-y^2}=\frac{2 y}{1-x z}... [From (i)] \\
& \Rightarrow 1-y^2=1-x z \\
& \Rightarrow y^2=x z
\end{aligned}$
$\therefore \quad x, y, \mathrm{z} \text { are in G.P. }... (ii)$
From (i) and (ii), 
we get $x=y=\mathrm{z}$

</details>

---

### Q9. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If for an Arithmetic progression, 9 times nineth term is equal to 13 times thirteenth term, then value of twenty second term is

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** 4
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Let the first term and common difference of given $\mathrm{AP}$ be a and d, respectively.
Given
$\begin{array}{l}
9 . a_{9}=13 . a_{13} \\
\Rightarrow 9[a+(9-1) d]=13[a+(13-1) d] \\
\Rightarrow 9[a+8 d]=13[a+12 d] \\
\Rightarrow 9 a+72 d=13 a+156 d \\
\Rightarrow 4 a+84 d=0 \\
\Rightarrow 4[a+21 d]=0 \\
\Rightarrow 4[a+(22-1) d=0 \\
\Rightarrow a+(22-1) d=0 \\
\Rightarrow a_{22}=0
\end{array}$

</details>

---

### Q10. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For a sequence if $S_{n}=\frac{5^{n}-2^{n}}{2^{n}}$, then its fourth term is

**Options:**

- **(A)** $\frac{375}{16}$
- **(B)** $\frac{375}{8}$
- **(C)** $\frac{251}{8}$
- **(D)** $\frac{251}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{375}{16}$**

**Detailed Solution:**

$s_{n}=\frac{5^{n}-2^{n}}{2^{n}} ; s_{n-1}=\frac{5^{n-1}-2^{n-1}}{2^{n-1}}$
$\begin{aligned} T_{n} &=s_{n}-s_{n-1} \\ T_{n} &=\frac{5^{n}-2^{n} \cdot 5^{n-1}}{2^{n}} \\ T_{4} &=\frac{5^{4}-2 \cdot 5^{3}}{2^{4}} \\ &=\frac{625-250}{16} \\ &=\frac{375}{16} \end{aligned}$

</details>

---

