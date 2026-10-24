# JEE Main Mathematics - Complex Number

## Topic 3: Conjugate, modulus and argument

**Total Questions:** 70

---

### Q1. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $z_1, z_2 \in \mathbb{C}$ be the distinct solutions of the equation $z^2 + 4z - (1 + 12i) = 0$. Then $|z_1|^2 + |z_2|^2$ is equal to :

**Options:**

- **(A)** $18$
- **(B)** $22$
- **(C)** $29$
- **(D)** $34$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $34$**

**Detailed Solution:**

Given equation is $z^2 + 4z - (1 + 12i) = 0$

Let the roots be $z_1$ and $z_2$.

Sum of roots: $z_1 + z_2 = -4$

Product of roots: $z_1 z_2 = -(1 + 12i)$

We know that $(z_1 - z_2)^2 = (z_1 + z_2)^2 - 4z_1 z_2$

$(z_1 - z_2)^2 = (-4)^2 - 4(-(1 + 12i)) = 16 + 4 + 48i = 20 + 48i$

Taking modulus on both sides:

$|z_1 - z_2|^2 = |20 + 48i| = \sqrt{20^2 + 48^2} = \sqrt{400 + 2304} = \sqrt{2704} = 52$

Using the parallelogram law for complex numbers:

$|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2(|z_1|^2 + |z_2|^2)$

$|-4|^2 + 52 = 2(|z_1|^2 + |z_2|^2)$

$16 + 52 = 2(|z_1|^2 + |z_2|^2)$

$68 = 2(|z_1|^2 + |z_2|^2)$

$|z_1|^2 + |z_2|^2 = 34$

Answer: $34$

</details>

---

### Q2. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $S=\{z \in \mathbb{C}: z^2+4z+16=0\}$. Then $\sum_{z \in S}|z+\sqrt{3}i|^2$ is equal to:

**Options:**

- **(A)** $42$
- **(B)** $23$
- **(C)** $27$
- **(D)** $38$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $38$**

**Detailed Solution:**

Given the equation $z^2 + 4z + 16 = 0$, we find its roots using the quadratic formula:

$z = \dfrac{-4 \pm \sqrt{16 - 64}}{2} = \dfrac{-4 \pm \sqrt{-48}}{2} = -2 \pm 2\sqrt{3}i$

The set $S$ contains two complex numbers: $z_1 = -2 + 2\sqrt{3}i$ and $z_2 = -2 - 2\sqrt{3}i$.

We need to evaluate the sum $\sum_{z \in S} |z + \sqrt{3}i|^2$, which is $|z_1 + \sqrt{3}i|^2 + |z_2 + \sqrt{3}i|^2$.

For $z_1 = -2 + 2\sqrt{3}i$:

$|z_1 + \sqrt{3}i|^2 = |-2 + 2\sqrt{3}i + \sqrt{3}i|^2 = |-2 + 3\sqrt{3}i|^2$

$|-2 + 3\sqrt{3}i|^2 = (-2)^2 + (3\sqrt{3})^2 = 4 + 27 = 31$

For $z_2 = -2 - 2\sqrt{3}i$:

$|z_2 + \sqrt{3}i|^2 = |-2 - 2\sqrt{3}i + \sqrt{3}i|^2 = |-2 - \sqrt{3}i|^2$

$|-2 - \sqrt{3}i|^2 = (-2)^2 + (-\sqrt{3})^2 = 4 + 3 = 7$

Adding these values together:

$\sum_{z \in S} |z + \sqrt{3}i|^2 = 31 + 7 = 38$

Answer: $38$

</details>

---

### Q3. JEE Main 2026 (24 January Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $z=(1+i)(1+2 i)(1+3 i) \ldots(1+n i)$, where $i=\sqrt{-1}$. If $|z|^{2}=44200$, then $n$ is equal to $\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$z = (1 + i)(1 + 2i)(1 + 3i)\cdots(1 + ni)$ where $i = \sqrt{-1}$
$|z|^2 = \prod_{k=1}^{n} |1 + ki|^2 = \prod_{k=1}^{n} (1 + k^2)$
Computing: $(1+1)(1+4)(1+9)(1+16)(1+25) = 2 \times 5 \times 10 \times 17 \times 26$
$= 10 \times 10 \times 17 \times 26 = 100 \times 442 = 44200$
Therefore $n = 5$

</details>

---

### Q4. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $S=\{z: 3 \leqslant|2 z-3(1+i)| \leqslant 7\}$ be a set of complex numbers. Then $\min _{z \in S}\left|\left(z+\frac{1}{2}(5+3 i)\right)\right|$ is equal to :

**Options:**

- **(A)** 2
- **(B)** $\frac{5}{2}$
- **(C)** $\frac{3}{2}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{2}$**

**Detailed Solution:**

$\dfrac{3}{2} \leq \left| z - \dfrac{3}{2}(1+i) \right| \leq \dfrac{7}{2}$
<img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/23S1_s_8_1.png">
$\min_{z \in S} \left| z - \left(\dfrac{-5}{2} - \dfrac{3}{2}i\right) \right| = PB$
$PB = PC - \dfrac{7}{2} \Rightarrow 5 - \dfrac{7}{2} \Rightarrow \dfrac{3}{2}$

</details>

---

### Q5. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $S=\left\{z \in \mathbb{C}: 4 z^{2}+\bar{z}=0\right\}$. Then $\sum_{z \in S}|z|^{2}$ is equal to:

**Options:**

- **(A)** $\frac{5}{64}$
- **(B)** $\frac{1}{16}$
- **(C)** $\frac{3}{16}$
- **(D)** $\frac{7}{64}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{16}$**

**Detailed Solution:**

Let $z=x+iy$. From $4z^2+\bar{z}=0$, separating real and imaginary parts:
Real: $4x^2-4y^2+x=0$, Imaginary: $y(8x-1)=0$.
Case 1: $y=0$
$\Rightarrow x(4x+1)=0$ 
$\Rightarrow z=0$ or $z=-\frac{1}{4}$.
Case 2: $x=\frac{1}{8}$
$\Rightarrow \frac{1}{16}-4y^2+\frac{1}{8}=0$
$\Rightarrow y^2=\frac{3}{64}$.
So $|z|^2=\frac{1}{64}+\frac{3}{64}=\frac{1}{16}$.
$\sum|z|^2=0+\frac{1}{16}+\frac{1}{16}+\frac{1}{16}=\frac{3}{16}$

</details>

---

### Q6. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $z$ be the complex number satisfying $|z-5| \leq 3$ and having maximum positive principal argument. Then $34\left|\frac{5 z-12}{5 \mathrm{i} z+16}\right|^{2}$ is equal to :

**Options:**

- **(A)** 26
- **(B)** 12
- **(C)** 20
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 20**

**Detailed Solution:**

The region $|z - 5| \le 3$ is a disk centered at $(5, 0)$ with radius 3. Maximum positive principal argument from origin occurs at the tangent point from origin to the circle.
$\sin\theta = \frac{3}{5}$, $\cos\theta = \frac{4}{5}$.
The tangent point is the foot of perpendicular from $(5,0)$ to the line $3x - 4y = 0$, giving $z = \frac{16}{5} + \frac{12}{5}i$.
$5z - 12 = 4 + 12i \Rightarrow |5z - 12|^2 = 160$
$5iz + 16 = 4 + 16i \Rightarrow |5iz + 16|^2 = 272$
$34\left|\frac{5z-12}{5iz+16}\right|^2 = 34 \times \frac{160}{272} = 34 \times \frac{10}{17} = 20$.

</details>

---

### Q7. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{A}=$
$\left\{\theta \in[0,2 \pi]: 1+10 \operatorname{Re}\left(\frac{2 \cos \theta+i \sin \theta}{\cos \theta-3 i \sin \theta}\right)=0\right\} .$
Then $\sum_{\theta \in A} \theta^2$ is equal to

**Options:**

- **(A)** $\frac{21}{4} \pi^2$
- **(B)** $8 \pi^2$
- **(C)** $\frac{27}{4} \pi^2$
- **(D)** $6 \pi^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{21}{4} \pi^2$**

**Detailed Solution:**

$\begin{aligned} & 1+10 \operatorname{Re}\left(\frac{2 \cos \theta+i \sin \theta}{\cos \theta-3 i \sin \theta}\right)=0 \\ & \therefore \mathrm{z}+\overline{\mathrm{z}}=2 \operatorname{Re}(\mathrm{z}) \\ & \frac{2 \cos \theta+\mathrm{i} \sin \theta}{\cos \theta-3 \mathrm{i} \sin \theta}+\frac{2 \cos \theta-\mathrm{i} \sin \theta}{\cos \theta+3 \mathrm{i} \sin \theta}=2 \times\left(\frac{-1}{10}\right) \\ & \frac{\left(2 \cos ^2 \theta-3 \sin ^2 \theta\right)+\left(2 \cos ^2 \theta\right)-\left(3 \sin ^2 \theta\right)}{\cos ^2 \theta+9 \sin ^2 \theta}=\frac{-2}{10} \\ & \Rightarrow \frac{2 \cos ^2 \theta-3 \sin ^2 \theta}{\cos ^2 \theta+9 \sin ^2 \theta}=\frac{-1}{10} \\ & \Rightarrow 20 \cos ^2 \theta-30 \sin ^2 \theta=-\cos ^2 \theta-9 \sin ^2 \theta \\ & 21 \cos ^2 \theta-21 \sin ^2 \theta=0 \\ & \Rightarrow \cos 2 \theta=0 \\ & 2 \theta=\frac{\pi}{2}, \frac{3 \pi}{2}, \frac{5 \pi}{2}, \frac{7 \pi}{2} \\ & \Rightarrow \sum \theta^2=\frac{\pi^2}{16}+\frac{9 \pi^2}{16}+\frac{25 \pi^2}{16}+\frac{49 \pi^2}{16}=\frac{84 \pi^2}{16}=\frac{21 \pi^2}{4}\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Among the statements
(S1) : The set $\left\{\mathrm{z} \in \mathbb{C}-\{-\mathrm{i}\}:|\mathrm{z}|=1\right.$ and $\frac{\mathrm{z}-\mathrm{i}}{\mathrm{z}+\mathrm{i}}$ is purely real} contains exactly two elements, and (S2) : The set $\left\{\mathrm{z} \in \mathbb{C}-\{-1\}:|\mathrm{z}|=1\right.$ and $\frac{\mathrm{z}-1}{\mathrm{z}+1}$ is purely imaginary contains infinitely many elements.

**Options:**

- **(A)** both are incorrect
- **(B)** only (S1) is correct
- **(C)** only (S2) is correct
- **(D)** both are correct

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) only (S2) is correct**

**Detailed Solution:**

$\begin{aligned} & \mathrm{S}_1:|\mathrm{z}|=1, \frac{\mathrm{z}-\mathrm{i}}{\mathrm{z}+\mathrm{i}}=\frac{\overline{\mathrm{z}}+\mathrm{i}}{\overline{\mathrm{z}}-\mathrm{i}} \\ & \Rightarrow(\mathrm{z}-\mathrm{i})(\overline{\mathrm{z}}-\mathrm{i})=(\mathrm{z}+\mathrm{i})(\overline{\mathrm{z}}+\mathrm{i}) \\ & |\mathrm{z}|^2-\mathrm{i}(\mathrm{z}+\overline{\mathrm{z}})-1=|\mathrm{z}|^2+\mathrm{i}(\mathrm{z}+\overline{\mathrm{z}})-1 \\ & \mathrm{i}(\mathrm{z}+\overline{\mathrm{z}})=0 \\ & \mathrm{z}+\overline{\mathrm{z}}=2 \cos \theta=0 \Rightarrow \cos \theta=0 \\ & \mathrm{z}=0+0 \mathrm{i},|\mathrm{z}| \neq 1 \\ & \mathrm{~S}_1: \frac{\mathrm{z}-1}{\mathrm{z}+1}+\frac{\overline{\mathrm{z}}-1}{\overline{\mathrm{z}}+1}=0 \\ & (\mathrm{z}-1)(\overline{\mathrm{z}}+1)+(\mathrm{z}+1)(\overline{\mathrm{z}}-1)=0 \\ & \Rightarrow|\mathrm{z}|^2+(\mathrm{z}-\overline{\mathrm{z}})-1+|\mathrm{z}|^2+(\mathrm{z}-\overline{\mathrm{z}})-1=0 \\ & |\mathrm{z}|^2=1\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $O$ be the origin, the point $A$ be $z_1=\sqrt{3}+2 \sqrt{2} i$, the point $B\left(z_2\right)$ be such that $\sqrt{3}\left|z_2\right|=\left|z_1\right|$ and $\arg \left(z_2\right)=\arg \left(z_1\right)+\frac{\pi}{6}$. Then

**Options:**

- **(A)** area of triangle ABO is $\frac{11}{\sqrt{3}}$
- **(B)** ABO is an obtuse angled isosceles triangle
- **(C)** area of triangle ABO is $\frac{11}{4}$
- **(D)** ABO is a scalene triangle

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) ABO is an obtuse angled isosceles triangle**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZTBSY1zNOMLe1r7QW1tWct0LYaWuSXEA0APhoARAPwM.original.fullsize.png">

$\begin{aligned}
& O A=\left|z_1\right|=\sqrt{3+8}=\sqrt{11} \\
& \text { and } O B=\frac{1}{\sqrt{3}}\left|z_1\right|=\sqrt{\frac{11}{3}} \\
& A B^2=O A^2+O B^2-2 \cdot O A \cdot O B \cos \frac{\pi}{6} \\
& \quad=11+\frac{11}{3}-2 \cdot \frac{11}{\sqrt{3}} \cdot \frac{\sqrt{3}}{2} \\
& \therefore \quad A B=\sqrt{\frac{11}{3}} \\
& \therefore \quad \text { Area of } \triangle A B D=\frac{1}{2} \cdot O A \cdot O B \cdot \sin \frac{\pi}{6} \\
& \quad=\frac{11}{4 \sqrt{3}} \text { sq. units }
\end{aligned}$
Here $O B=A B$ and $\angle A=\frac{2 \pi}{3}$
$\therefore \quad \triangle A B D$ is an obtuse angled isosceles triangle.

</details>

---

### Q10. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\alpha$ and $\beta$ are the roots of the equation $2 z^2-3 z-2 \mathrm{i}=0$, where $\mathrm{i}=\sqrt{-1}$, then $16 \cdot \operatorname{Re}\left(\frac{\alpha^{19}+\beta^{19}+\alpha^{11}+\beta^{11}}{\alpha^{15}+\beta^{15}}\right) \cdot \operatorname{lm}\left(\frac{\alpha^{19}+\beta^{19}+\alpha^{11}+\beta^{11}}{\alpha^{15}+\beta^{15}}\right)$ is equal to

**Options:**

- **(A)** $441$
- **(B)** $398$
- **(C)** $312$
- **(D)** $409$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $441$**

**Detailed Solution:**

$2 z^2-3 z-2 i=0$ ...(i)
$2\left(z-\frac{i}{z}\right)=3$
As $\alpha, \beta$ are roots of (i)
$\begin{aligned}
& \alpha-\frac{i}{\alpha}=\frac{3}{2} \\
& \Rightarrow \alpha^2-\frac{1}{\alpha^2}-2 i=\frac{9}{4} \\
& \Rightarrow \alpha^2-\frac{1}{\alpha^2}=\frac{9}{4}+2 i
\end{aligned}$

Squaring both sides
$\begin{aligned}
& \Rightarrow \alpha^4+\frac{1}{\alpha^4}-2=\frac{81}{16}-4+9 i \\
& \Rightarrow \alpha^4+\frac{1}{\alpha^4}=\frac{49}{16}+9 i
\end{aligned}$

Similarly, $\beta^4+\frac{1}{\beta^4}=\frac{49}{16}+9 i$
$\begin{aligned}
& \frac{\alpha^{19}+\beta^{19}+\alpha^{11}+\beta^{11}}{\alpha^{15}+\beta^{15}} \\
& =\frac{\alpha^{15}\left(\alpha^4+\frac{1}{\alpha^4}\right)+\beta^{15}\left(\beta^4+\frac{1}{\beta^4}\right)}{\alpha^{15}+\beta^{15}} \\
& =\frac{49}{16}+9 i \\
& \operatorname{Re}\left(\frac{\alpha^{19}+\beta^{19}+\alpha^{11}+\beta^{11}}{\alpha^{15}+\beta^{15}}\right)=\frac{49}{16} \\
& \operatorname{Im}\left(\frac{\alpha^{19}+\beta^{19}+\alpha^{11}+\beta^{11}}{\alpha^{15}+\beta^{15}}\right)=9 \\
& \Rightarrow 16 \operatorname{Re}\left(\frac{\alpha^{19}+\beta^{19}+\alpha^{11}+\beta^{11}}{\alpha^{15}+\beta^{15}}\right) \cdot \operatorname{lm}\left(\frac{\alpha^{19}+\beta^{19}+\alpha^{11}+\beta^{11}}{\alpha^{15}+\beta^{15}}\right) \\
& =16 \times \frac{49}{16} \times 9 \\
& =441
\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $z_1, z_2$ and $z_3$ be three complex numbers on the circle $|z|=1$ with $\arg \left(z_1\right)=\frac{-\pi}{4}, \arg \left(z_2\right)=0$ and $\arg \left(z_3\right)=\frac{\pi}{4}$. If $\left|z_1 \bar{z}_2+z_2 \bar{z}_3+z_3 \bar{z}_1\right|^2=\alpha+\beta \sqrt{2}, \alpha, \beta \in \mathbf{Z}$, then the value of $\alpha^2+\beta^2$ is :

**Options:**

- **(A)** $24$
- **(B)** $29$
- **(C)** $41$
- **(D)** $31$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $29$**

**Detailed Solution:**

$\begin{aligned} & |z|=1 \\ & \arg \left(z_1\right)=-\frac{\pi}{4}, \arg \left(z_2\right)=0, \arg \left(z_3\right)=\frac{\pi}{4} \\ & z_1=|1| e^{-\frac{\pi}{4}}=\frac{1}{\sqrt{2}}-\frac{i}{\sqrt{2}} \\ & z_2=1+0 i \\ & z_3=\frac{1}{\sqrt{2}}+\frac{i}{\sqrt{2}} \\ & z_1 \bar{z}_2=\frac{1-i}{\sqrt{2}} \\ & z_2 \bar{z}_3=\frac{1-i}{\sqrt{2}} \\ & z_3 \bar{z}_1=\frac{(1+i)^2}{2} \\ & z_1 \bar{z}_2+z_2 \bar{z}_3+z_3 \bar{z}_1=\sqrt{2}+i(1-\sqrt{2}) \\ & \left|z_1 \bar{z}_2+z_2 \bar{z}_3+z_3 \bar{z}_1\right|^2=5-2 \sqrt{2} \\ & \alpha=5, \beta=-2 \\ & \alpha^2+\beta^2=29\end{aligned}$

</details>

---

### Q12. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $z$ be a complex number such that the real part of $\frac{z-2 i}{z+2 i}$ is zero. Then, the maximum value of $|z-(6+8 i)|$ is equal to

**Options:**

- **(A)** 12
- **(B)** 10
- **(C)** 8
- **(D)** $\infty$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 12**

**Detailed Solution:**

$\begin{aligned} & \frac{\mathrm{z}-2 \mathrm{i}}{\mathrm{z}+2 \mathrm{i}}+\frac{\overline{\mathrm{z}}+2 \mathrm{i}}{\overline{\mathrm{z}}-2 \mathrm{i}}=0 \\ & \mathrm{z} \overline{\mathrm{z}}-2 \mathrm{i} \overline{\mathrm{z}}-2 \mathrm{i} \mathrm{z}+4(-1) \\ & +\mathrm{z} \overline{\mathrm{z}}+2 \mathrm{z} i+2 \overline{\mathrm{z} i}+4(-1)=0 \\ & \Rightarrow 2|\mathrm{z}|^2=8 \Rightarrow|\mathrm{z}|=2 \\ & |\mathrm{z}-(6+8 \mathrm{i})|_{\text {maximum }}=10+2=12\end{aligned}$

</details>

---

### Q13. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

The sum of the square of the modulus of the elements in the set $\{z=\mathrm{a}+\mathrm{ib}: \mathrm{a}, \mathrm{b} \in \mathbf{Z}, z \in \mathbf{C},|z-1| \leq 1,|z-5| \leq|z-5 \mathrm{i}|\}$ is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

$\begin{aligned} & |\mathrm{z}-1| \leq 1 \\ & \Rightarrow|(\mathrm{x}-1)+\mathrm{iy}| \leq 1 \mid \\ & \Rightarrow \sqrt{(\mathrm{x}-1)^2+\mathrm{y}^2} \leq 1 \\ & \Rightarrow(\mathrm{x}-1)^2+\mathrm{y}^2 \leq 1 \ldots(1)\end{aligned}$
$\begin{aligned} & \text { Also }|z-5| \leq|z-5 i| \\ & (x-5)^2+y^2 \leq x^2+(y-5)^2 \\ & -10 x \leq-10 y \\ & \Rightarrow x \geq y.....(2)\end{aligned}$
$\begin{aligned} & \text { Solving (1) and (2) } \\ & \begin{array}{l}\Rightarrow(\mathrm{x}-1)^2+\mathrm{x}^2=1 \\ \Rightarrow 2 \mathrm{x}^2-2 \mathrm{x}=0 \\ \Rightarrow \mathrm{x}(\mathrm{x}-1)=0 \\ \Rightarrow \mathrm{x}=0 \text { or } \mathrm{x}=1 \\ \quad \mathrm{y}=0 \text { or } \mathrm{y}=1\end{array}\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/yfqN9J9mgyiUr2hL4XpJ3vQJhLU_OabRyosBp7A-52s.original.fullsize.png">
Given $\mathrm{x}, \mathrm{y} \in \mathrm{I}$
Points $(0,0),(1,0),(2,0),(1,1),(1,-1)$ to find
$\begin{aligned}
& \left|z_1\right|^2+\left|z_2\right|^2+\left|z_3\right|^2+\left|z_4\right|^2+\left|z_5\right|^2 \\
& =0+1+4+1+1+1+1=9
\end{aligned}$

</details>

---

### Q14. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all possible values of $\theta \in[-\pi, 2 \pi]$, for which $\frac{1+i \cos \theta}{1-2 i \cos \theta}$ is purely imaginary, is equal

**Options:**

- **(A)** $3 \pi$
- **(B)** $2 \pi$
- **(C)** $5 \pi$
- **(D)** $4 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3 \pi$**

**Detailed Solution:**

$\begin{aligned} & Z=\frac{1+i \cos \theta}{1-2 i \cos \theta} \\ & Z=-\bar{Z} \Rightarrow \frac{1+i \cos \theta}{1-2 i \cos \theta}=-\left(\frac{\overline{1+i \cos \theta}}{1-2 i \cos \theta}\right) \\ & (1+i \cos \theta)(\overline{1-2 i \cos \theta})=-(1-2 i \cos \theta)(\overline{1+i \cos \theta}) \\ & (1+i \cos \theta)(1+2 i \cos \theta)=-(1-2 i \cos \theta)(1-i \cos \theta) \\ & 1+3 i \cos \theta-2 \cos ^2 \theta=-\left(1-3 i \cos \theta-2 \cos ^2 \theta\right) \\ & 2-4 \cos ^2 \theta=0 \\ & \Rightarrow \cos ^2 \theta=\frac{1}{2} \Rightarrow \theta=-\frac{\pi}{4},-\frac{3 \pi}{4}, \frac{\pi}{4}, \frac{3 \pi}{4}, \frac{5 \pi}{4}, \frac{7 \pi}{4} \\ & \text { sum }=3 \pi\end{aligned}$

</details>

---

### Q15. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $S_1=\{z \in C:|z| \leq 5\}, S_2=\left\{z \in C: \operatorname{Im}\left(\frac{z+1-\sqrt{3} i}{1-\sqrt{3} i}\right) \geq 0\right\}$ and $S_3=\{z \in C: \operatorname{Re}(z) \geq 0\}$. Then the area of the region $S_1 \cap S_2 \cap S_3$ is :

**Options:**

- **(A)** $\frac{125 \pi}{12}$
- **(B)** $\frac{125 \pi}{4}$
- **(C)** $\frac{125 \pi}{24}$
- **(D)** $\frac{125 \pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{125 \pi}{12}$**

**Detailed Solution:**

$S_1: x^2+y^2 \leq 25...(1)$
$\begin{aligned} & S_2: \operatorname{lm} \text { of } \frac{z+(1-\sqrt{3} i)}{(1-\sqrt{3} i)} \geq 0 \\ & \operatorname{lm} \text { of }\left(\frac{x+i y}{1-\sqrt{3} i}+1\right) \geq 0 \\ & \operatorname{lm} \text { of }\left(\frac{(x+i y)(1+\sqrt{3} i)}{4}\right) \geq 0 \\ & \Rightarrow \sqrt{3} x+y \geq 0 ...(2)\\ & S_3: x \geq 0 ...(3)\\ & \text { Area }=\frac{5}{12}\left(\pi(5)^2\right)\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/H4vdqHJiqR70dn4Bv8tsNJWS2YnLcgsojEe2KJvZQX0.original.fullsize.png">

</details>

---

### Q16. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the region $S=\{z \in \mathbb{C}:|z-1| \leq 2 ;(z+\bar{z})+i(z-\bar{z}) \leq 2, \operatorname{Im}(z) \geq 0\}$ is

**Options:**

- **(A)** $\frac{7 \pi}{3}$
- **(B)** $\frac{7 \pi}{4}$
- **(C)** $\frac{17 \pi}{8}$
- **(D)** $\frac{3 \pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3 \pi}{2}$**

**Detailed Solution:**

Put $z=x+i y$
$|z-1| \leq 2 \Rightarrow(x-1)^2+y^2 \leq 4$ ...(i)
$\Rightarrow x-y \leq 1$ ...(ii)
$\operatorname{Im}(\mathrm{z}) \geq 0 \Rightarrow \mathrm{y} \geq 0$ ...(iii)
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/44NeRiJ51psaA1AJU1-WwgVrc-T_Un6nP6nbucOHcM4.original.fullsize.png">
$\begin{aligned} & \text { Required area } \\ & =\text { Area of semi-circle }- \text { area of sector A } \\ & \frac{1}{2} \pi(2)^2-\frac{\pi}{2} \\ & =\frac{3 \pi}{2}\end{aligned}$

</details>

---

### Q17. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha$ and $\beta$ be the sum and the product of all the non-zero solutions of the equation $(\bar{z})^2+|z|=0$, $z \in$ C. Then $4\left(\alpha^2+\beta^2\right)$ is equal to :

**Options:**

- **(A)** 6
- **(B)** 8
- **(C)** 2
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

$\begin{array}{ll}z=x+i y & \\ \bar{z}=x-i y & \\ \bar{z}^2=x^2-y^2-2 i x y & \\ \Rightarrow x^2-y^2-2 i x y+\sqrt{x^2+y^2}=0 \\ \Rightarrow x=0 \quad \text { or } & y=0 \\ -y^2+|y|=0 & x^2+|x|=0 \\ |y|=|y|^2 & \Rightarrow x=0 \\ y=0, \pm 1 & \Rightarrow \alpha=i-i=0 \\ \Rightarrow i,-i & \beta=i(-i)=1 \\ \text { are roots } & 4(0+1)=4\end{array}$

</details>

---

### Q18. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> is a complex number such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>≤</mo><mn>1</mn></math>, then the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>3</mn><mo>+</mo><mn>4</mn><mi>i</mi></mrow></mfenced></mrow></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>+</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>4</mn><mi>i</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>;</mo><mo> </mo><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>≤</mo><mn>1</mn></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>=</mo><mn>1</mn></math> gives <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math>, which represents a circle having centre at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> and radius as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> unit.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>+</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>4</mn><mi>i</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></math> gives the distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e3b676ba-6614-4edb-8982-0848c4c19e53.png" style="width: 330px; height: 246px;"/></p><p>So, we need to find the minimum distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>P</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mi>P</mi><mo>=</mo><mi>O</mi><mi>P</mi><mo>-</mo><mi>O</mi><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mi>P</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>0</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mi>P</mi><mo>=</mo><msqrt><mfrac><mn>9</mn><mn>4</mn></mfrac><mo>+</mo><mn>4</mn></msqrt><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mi>P</mi><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mi>P</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q19. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>2</mn></msub></math> be two complex number such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>z</mi><mn>1</mn><mn>3</mn></msubsup><mo>+</mo><msubsup><mi>z</mi><mn>2</mn><mn>3</mn></msubsup><mo>=</mo><mn>20</mn><mo>+</mo><mn>15</mn><mi>i</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msubsup><mi>z</mi><mn>1</mn><mn>4</mn></msubsup><mo>+</mo><msubsup><mi>z</mi><mn>2</mn><mn>4</mn></msubsup></mrow></mfenced></math> equals-

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>75</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><msqrt><mn>15</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>75</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn><mo> </mo><mo>&amp;</mo><mo> </mo><msup><msub><mi>z</mi><mn>1</mn></msub><mn>3</mn></msup><mo>+</mo><msup><msub><mi>z</mi><mn>2</mn></msub><mn>3</mn></msup><mo>=</mo><mn>20</mn><mo>+</mo><mn>15</mn><mi>i</mi></math></p><p>Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><msub><mi>z</mi><mn>1</mn></msub><mn>3</mn></msup><mo>+</mo><msup><msub><mi>z</mi><mn>2</mn></msub><mn>3</mn></msup><mo>=</mo><mn>20</mn><mo>+</mo><mn>15</mn><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mn>3</mn></msup><mo>-</mo><mn>3</mn><msub><mi>z</mi><mn>1</mn></msub><msub><mi>z</mi><mn>2</mn></msub><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>20</mn><mo>+</mo><mn>15</mn><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mn>5</mn></mfenced><mn>3</mn></msup><mo>-</mo><mn>3</mn><msub><mi>z</mi><mn>1</mn></msub><msub><mi>z</mi><mn>2</mn></msub><mfenced><mn>5</mn></mfenced><mo>=</mo><mn>20</mn><mo>+</mo><mn>15</mn><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>125</mn><mo>-</mo><mn>15</mn><msub><mi>z</mi><mn>1</mn></msub><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><mn>20</mn><mo>+</mo><mn>15</mn><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>z</mi><mn>1</mn></msub><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><mn>7</mn><mo>-</mo><mi>i</mi></math></p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><msub><mi>z</mi><mn>1</mn></msub><mn>4</mn></msup><mo>+</mo><msup><msub><mi>z</mi><mn>2</mn></msub><mn>4</mn></msup><mo>=</mo><msup><mfenced><mrow><msup><msub><mi>z</mi><mn>1</mn></msub><mn>2</mn></msup><mo>+</mo><msup><msub><mi>z</mi><mn>2</mn></msub><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><msub><mi>z</mi><mn>1</mn></msub><mn>4</mn></msup><mo>+</mo><msup><msub><mi>z</mi><mn>2</mn></msub><mn>4</mn></msup><mo>=</mo><msup><mfenced><mrow><msup><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msub><mi>z</mi><mn>1</mn></msub><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><msub><mi>z</mi><mn>1</mn></msub><mn>4</mn></msup><mo>+</mo><msup><msub><mi>z</mi><mn>2</mn></msub><mn>4</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>25</mn><mo>-</mo><mn>2</mn><mfenced><mrow><mn>7</mn><mo>-</mo><mi>i</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mfenced><mrow><mn>7</mn><mo>-</mo><mi>i</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><msub><mi>z</mi><mn>1</mn></msub><mn>4</mn></msup><mo>+</mo><msup><msub><mi>z</mi><mn>2</mn></msub><mn>4</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>11</mn><mo>+</mo><mn>2</mn><mi>i</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mrow><mn>48</mn><mo>-</mo><mn>14</mn><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><msub><mi>z</mi><mn>1</mn></msub><mn>4</mn></msup><mo>+</mo><msup><msub><mi>z</mi><mn>2</mn></msub><mn>4</mn></msup><mo>=</mo><mfenced><mrow><mn>121</mn><mo>-</mo><mn>4</mn><mo>+</mo><mn>44</mn><mi>i</mi></mrow></mfenced><mo>-</mo><mn>96</mn><mo>+</mo><mn>28</mn><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><msub><mi>z</mi><mn>1</mn></msub><mn>4</mn></msup><mo>+</mo><msup><msub><mi>z</mi><mn>2</mn></msub><mn>4</mn></msup><mo>=</mo><mn>21</mn><mo>+</mo><mn>72</mn><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><msup><msub><mi>z</mi><mn>1</mn></msub><mn>4</mn></msup><mo>+</mo><msup><msub><mi>z</mi><mn>2</mn></msub><mn>4</mn></msup></mrow></mfenced><mo>=</mo><msqrt><msup><mn>21</mn><mn>2</mn></msup><mo>+</mo><msup><mn>72</mn><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><msup><msub><mi>z</mi><mn>1</mn></msub><mn>4</mn></msup><mo>+</mo><msup><msub><mi>z</mi><mn>2</mn></msub><mn>4</mn></msup></mrow></mfenced><mo>=</mo><msqrt><mn>5625</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><msup><msub><mi>z</mi><mn>1</mn></msub><mn>4</mn></msup><mo>+</mo><msup><msub><mi>z</mi><mn>2</mn></msub><mn>4</mn></msup></mrow></mfenced><mo>=</mo><mn>75</mn></math></p>

</details>

---

### Q20. JEE Main 2024 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math> denotes the number of solutions of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mn>1</mn><mo>−</mo><mi>i</mi></mrow></mfenced><mi>x</mi></msup><mo>=</mo><msup><mn>2</mn><mi>x</mi></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><mfenced><mfrac><mfenced close="|" open="|"><mi>z</mi></mfenced><mrow><mi>arg</mi><mfenced><mi>z</mi></mfenced></mrow></mfrac></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced><mn>4</mn></msup><mfenced><mrow><mfrac><mrow><mn>1</mn><mo>−</mo><msqrt><mi>π</mi></msqrt><mo>·</mo><mi>i</mi></mrow><mrow><msqrt><mi>π</mi></msqrt><mo>+</mo><mi>i</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><msqrt><mi>π</mi></msqrt><mo>−</mo><mi>i</mi></mrow><mrow><mn>1</mn><mo>+</mo><msqrt><mi>π</mi></msqrt><mo>·</mo><mi>i</mi></mrow></mfrac></mrow></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><msqrt><mo>−</mo><mn>1</mn></msqrt></math>, then the distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>α</mi><mo>,</mo><mo> </mo><mi>β</mi></mrow></mfenced></math> from the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>−</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>7</mn></math> is ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mn>1</mn><mo>−</mo><mi>i</mi></mrow></mfenced><mi>x</mi></msup><mo>=</mo><msup><mn>2</mn><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mi>x</mi></msup><mo>=</mo><msup><mn>2</mn><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p>Hence, the number of solutions will be one, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mn>1</mn></math></p><p>Now, solving</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced><mn>4</mn></msup><mfenced><mrow><mfrac><mrow><mn>1</mn><mo>−</mo><msqrt><mi>π</mi></msqrt><mo>·</mo><mi>i</mi></mrow><mrow><msqrt><mi>π</mi></msqrt><mo>+</mo><mi>i</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><msqrt><mi>π</mi></msqrt><mo>−</mo><mi>i</mi></mrow><mrow><mn>1</mn><mo>+</mo><msqrt><mi>π</mi></msqrt><mo>·</mo><mi>i</mi></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>z</mi><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced><mn>4</mn></msup><mfenced close="]" open="["><mrow><mfrac><mrow><msqrt><mi>π</mi></msqrt><mo>−</mo><mi>π</mi><mi>i</mi><mo>−</mo><mi>i</mi><mo>−</mo><msqrt><mi>π</mi></msqrt></mrow><mrow><mi>π</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msqrt><mi>π</mi></msqrt><mo>−</mo><mi>i</mi><mo>−</mo><mi>π</mi><mi>i</mi><mo>−</mo><msqrt><mi>π</mi></msqrt></mrow><mrow><mn>1</mn><mo>+</mo><mi>π</mi></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>z</mi><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced><mn>4</mn></msup><mfenced close="]" open="["><mfrac><mrow><mo>−</mo><mn>2</mn><mi>π</mi><mi>i</mi><mo>−</mo><mn>2</mn><mi>i</mi></mrow><mrow><mi>π</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>z</mi><mo>=</mo><mfrac><mrow><mi>π</mi><mi>i</mi></mrow><mn>2</mn></mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>z</mi><mo>=</mo><mo>−</mo><mfrac><mrow><mi>π</mi><mi>i</mi></mrow><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mn>4</mn><mi>i</mi><mo>+</mo><mn>6</mn><msup><mi>i</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>i</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>z</mi><mo>=</mo><mn>2</mn><mi>π</mi><mi>i</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>r</mi><mi>g</mi><mfenced><mi>z</mi></mfenced><mo>=</mo><mfrac><mi mathvariant="normal">π</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>β</mi><mo>=</mo><mfrac><mfenced close="|" open="|"><mi>z</mi></mfenced><mstyle displaystyle="true"><mi>a</mi><mi>r</mi><mi>g</mi><mfenced><mi>z</mi></mfenced></mstyle></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mstyle displaystyle="true"><mfrac><mi>π</mi><mn>2</mn></mfrac></mstyle></mfrac><mo>=</mo><mn>4</mn></math></p><p>Hence, the distance from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>α</mi><mo>,</mo><mi>β</mi></mrow></mfenced><mo>≡</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo> </mo><mn>4</mn></mrow></mfenced></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>−</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>7</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mrow><mn>4</mn><mo>-</mo><mn>3</mn><mo>×</mo><mn>4</mn><mo>-</mo><mn>7</mn></mrow><msqrt><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mn>15</mn><mn>5</mn></mfrac><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q21. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi><mo>,</mo><mi>x</mi><mi>y</mi><mo>≠</mo><mn>0</mn></math>, satisfies the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>i</mi><mover><mi>z</mi><mo>¯</mo></mover><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msup><mi>z</mi><mn>2</mn></msup></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>i</mi><menclose notation="top"><mi>z</mi></menclose><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>z</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mi>i</mi><menclose notation="top"><mi>z</mi></menclose></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>i</mi><mi>x</mi><mi>y</mi><mo>=</mo><mo>-</mo><mi>i</mi><mi>x</mi><mo>-</mo><mi>y</mi></math></p><p>Now on comparing both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mi>y</mi><mo> </mo><mo>&amp;</mo><mo> </mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mo>-</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mi>y</mi><mo> </mo><mo>&amp;</mo><mo> </mo><mi>x</mi><mfenced><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mo>-</mo><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mo>±</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo> </mo><mo>&amp;</mo><mo> </mo><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mo>±</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo> </mo><mo>+</mo><mi>i</mi><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>z</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo> </mo><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>±</mo><mn>2</mn><mi>i</mi><mfenced><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mfenced><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>z</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo> </mo><mo>±</mo><mi>i</mi><mfenced><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><msup><mi>z</mi><mn>2</mn></msup></mfenced><mo>=</mo><msup><mfenced><msqrt><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></msqrt></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q22. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>i</mi></math>, is such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>z</mi><mo>+</mo><mn>1</mn><mo>|</mo><mo>=</mo><mi>α</mi><mi>z</mi><mo>+</mo><mi>β</mi><mo>(</mo><mn>1</mn><mo>+</mo><mi>i</mi><mo>)</mo><mo>,</mo><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mi>β</mi><mo>∈</mo><mi mathvariant="normal">R</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mi>β</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>α</mi><mi>z</mi><mo>+</mo><mi>β</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>i</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>α</mi><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>i</mi></mrow></mfenced><mo>+</mo><mi>β</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>i</mi></mrow></mfenced><mo>=</mo><mfrac><mi>α</mi><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>α</mi><mi>i</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>β</mi><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msqrt><mfrac><mn>9</mn><mn>4</mn></mfrac><mo>+</mo><mn>4</mn></msqrt><mo>=</mo><mfenced><mrow><mfrac><mi>α</mi><mn>2</mn></mfrac><mo>+</mo><mi>β</mi></mrow></mfenced><mo>+</mo><mi>i</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mi>α</mi><mo>+</mo><mi>β</mi></mrow></mfenced></math></p><p>Now, on comparing real and imaginary part we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>=</mo><mfenced><mrow><mfrac><mi>α</mi><mn>2</mn></mfrac><mo>+</mo><mi>β</mi></mrow></mfenced><mo>+</mo><mi>i</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mi>α</mi><mo>+</mo><mi>β</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>α</mi><mo>=</mo><mi>β</mi><mo>,</mo><mo> </mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>=</mo><mfenced><mrow><mfrac><mi>α</mi><mn>2</mn></mfrac><mo>+</mo><mi>β</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>α</mi><mo>=</mo><mi>β</mi><mo>,</mo><mo> </mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mi>α</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mi>β</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q23. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>z</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8450;</mi><mo>:</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mi>i</mi><mfenced><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mo>Re</mo><mo>(</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>)</mo></mrow></mfenced></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>z</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mo>|</mo><mi>z</mi><msup><mo>|</mo><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mi>i</mi><mfenced><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mo>Re</mo><mo>(</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>)</mo></mrow></mfenced></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mi>x</mi><mo>-</mo><mi>i</mi><mi>y</mi></math></p><p>Now putting the value in, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mi>i</mi><mfenced><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mo>Re</mo><mo>(</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>)</mo></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mi>i</mi><mfenced><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mo>Re</mo><mo>(</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>)</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>-</mo><mi>i</mi><mi>y</mi><mo>=</mo><mi>i</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>i</mi><mi>x</mi><mi>y</mi><mo>+</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>-</mo><mi>i</mi><mi>y</mi><mo>=</mo><mi>i</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi></math></p><p>Now comparing real part we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>&#8658;</mo><mi>x</mi><mo>(</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And imaginary part we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now taking Case (I) when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mi>y</mi><mo>=</mo><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>i</mi></math></p><p>Now taking Case (II) when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>i</mi><mo>,</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>i</mi></math></p><p>Now finding, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8721;</mo><mo>|</mo><mi>z</mi><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>+</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>=</mo><mn>4</mn></math></p></blockquote>

</details>

---

### Q24. JEE Main 2023 (11 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>z</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8450;</mi><mo>-</mo><mo>{</mo><mi>i</mi><mo>,</mo><mn>2</mn><mi>i</mi><mo>}</mo><mo>:</mo><mfrac><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>i</mi><mi>z</mi><mo>-</mo><mn>15</mn></mrow><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>i</mi><mi>z</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></mrow></mfenced></math>. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mfrac><mn>13</mn><mn>11</mn></mfrac><mi>i</mi><mo>&#8712;</mo><mi>S</mi><mo>,</mo><mi>&#945;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi><mo>-</mo><mo>{</mo><mn>0</mn><mo>}</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>242</mn><msup><mi>&#945;</mi><mn>2</mn></msup></math> is equal to</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1680**

**Detailed Solution:**

<p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math> in the given expression and equate the imaginary part to zero.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>i</mi><mi>z</mi><mo>-</mo><mn>15</mn></mrow><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>i</mi><mi>z</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>i</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mo>-</mo><mn>15</mn></mrow><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>i</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>y</mi><mo>-</mo><mn>15</mn><mo>+</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>8</mn><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mo>+</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>y</mi><mo>-</mo><mn>15</mn><mo>+</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>8</mn><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mo>+</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>&#215;</mo><mfrac><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mo>-</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mo>-</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>y</mi><mo>-</mo><mn>15</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>8</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>8</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>y</mi><mo>-</mo><mn>15</mn></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Im</mi><mfenced><mfrac><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>i</mi><mi>z</mi><mo>-</mo><mn>15</mn></mrow><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>i</mi><mi>z</mi><mo>-</mo><mn>2</mn></mrow></mfrac></mfenced><mo>=</mo><mn>0</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>y</mi><mo>-</mo><mn>15</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>8</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>8</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>8</mn><mi>y</mi><mo>+</mo><mn>15</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>8</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>11</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>11</mn><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>24</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>30</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>45</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>24</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>16</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>11</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>26</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>61</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>11</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>26</mn><mi>y</mi><mo>-</mo><mn>61</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>&#8800;</mo><mn>0</mn></math></p><p>So, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mfrac><mn>13</mn><mn>11</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#945;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mo>&#183;</mo><mfrac><msup><mn>13</mn><mn>2</mn></msup><msup><mn>11</mn><mn>2</mn></msup></mfrac><mo>-</mo><mn>26</mn><mo>&#183;</mo><mfrac><mn>13</mn><mn>11</mn></mfrac><mo>-</mo><mn>61</mn><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>121</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>840</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>242</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>1680</mn></math></p><p>Hence this is the required answer.</p>

</details>

---

### Q25. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mn>1</mn></msub></math> be the point obtained by the rotation of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><mn>5</mn><mo>+</mo><mn>4</mn><mi>i</mi></math> about the origin through a right angle in the anticlockwise direction, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mn>2</mn></msub></math> be the point obtained by the rotation of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn><mo>+</mo><mn>5</mn><mi>i</mi></math> about the origin through a right angle in the clockwise direction. Then the principal argument <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mn>1</mn></msub><mo>-</mo><msub><mi>w</mi><mn>2</mn></msub></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>8</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#960;</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>33</mn><mn>5</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#960;</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>8</mn><mn>9</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>33</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>8</mn><mn>9</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Two complex numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mn>1</mn></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>w</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>+</mo><mn>5</mn><mi>i</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn><mo>+</mo><mn>4</mn><mi>i</mi></math> are both rotated by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>90</mn><mo>&#176;</mo></msup></math> with respect to origin anticlock-wise and clockwise respectively,</p><p>So by concept of rotation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mn>3</mn></msub><mo>=</mo><mi>i</mi><msub><mi>w</mi><mn>1</mn></msub><mo>=</mo><mi>i</mi><mfenced><mrow><mn>3</mn><mo>+</mo><mn>5</mn><mi>i</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>5</mn><mo>+</mo><mn>3</mn><mi>i</mi></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mn>4</mn></msub><mo>=</mo><mo>-</mo><mi>i</mi><msub><mi>w</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mi>i</mi><mfenced><mrow><mn>5</mn><mo>+</mo><mn>4</mn><mi>i</mi></mrow></mfenced><mo>=</mo><mn>4</mn><mo>-</mo><mn>5</mn><mi>i</mi></math></p><p>Now principal argument of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mn>3</mn></msub><mo>-</mo><msub><mi>w</mi><mn>4</mn></msub><mo>=</mo><mo>-</mo><mn>9</mn><mo>+</mo><mn>8</mn><mi>i</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#960;</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>8</mn><mn>9</mn></mfrac></math> {as complex number is in second quadrant so principal argument is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#960;</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="|" open="|"><mfrac><mi mathvariant="normal">y</mi><mi mathvariant="normal">x</mi></mfrac></mfenced></math>}</p></blockquote>

</details>

---

### Q26. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="" open="{"><mrow><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi><mo>:</mo><mfrac><mrow><mn>2</mn><mi>z</mi><mo>-</mo><mn>3</mn><mi>i</mi></mrow><mrow><mn>4</mn><mi>z</mi><mo>+</mo><mn>2</mn><mi>i</mi></mrow></mfrac></mrow></mfenced></math> is a real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>}</mo></math>. Then which of the following is <strong>NOT</strong> correct?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8800;</mo><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>=</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>=</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>z</mi><mo>-</mo><mn>3</mn><mi>i</mi></mrow><mrow><mn>4</mn><mi>z</mi><mo>+</mo><mn>2</mn><mi>i</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Z</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>y</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mi>i</mi><mfenced><mrow><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Z</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>y</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mi>i</mi><mfenced><mrow><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mi>i</mi><mfenced><mrow><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mi>i</mi><mfenced><mrow><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Z</mi><mo>=</mo><mfrac><mrow><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>y</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mi>i</mi><mfenced close="]" open="["><mrow><mn>4</mn><mi>x</mi><mfenced><mrow><mn>2</mn><mi>y</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>8</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>4</mn><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi></math> is purely real, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mi>x</mi><mfenced><mrow><mn>2</mn><mi>y</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>8</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>4</mn><mi>x</mi></mrow></mfenced></mrow><mrow><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>8</mn><mi>x</mi><mi>y</mi><mo>-</mo><mfenced><mrow><mn>8</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>4</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mi>i</mi><mfenced><mrow><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>i</mi><mfenced><mrow><mn>4</mn><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#8800;</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Hence this is the required option.</p></blockquote>

</details>

---

### Q27. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the complex number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>z</mi><mo>-</mo><mn>3</mn><mi>i</mi></mrow><mrow><mn>2</mn><mi>z</mi><mo>+</mo><mi>i</mi></mrow></mfrac></math> is purely imaginary. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>4</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mi>y</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The complex number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>z</mi><mo>-</mo><mn>3</mn><mi>i</mi></mrow><mrow><mn>2</mn><mi>z</mi><mo>+</mo><mi>i</mi></mrow></mfrac></math> is purely imaginary,</p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>z</mi><mo>-</mo><mn>3</mn><mi>i</mi></mrow><mrow><mn>2</mn><mi>z</mi><mo>+</mo><mi>i</mi></mrow></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mo>-</mo><mn>3</mn><mi>i</mi></mrow><mrow><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mo>+</mo><mi>i</mi></mrow></mfrac><mo>=</mo><mfrac><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>y</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></mfrac><mfrac><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></mfrac></math></p><p>Now taking real part as,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>2</mn><mi>y</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>y</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mi>y</mi><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p>Now using,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>x</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mi>y</mi><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>4</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mi>y</mi><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>4</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mi>y</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p></blockquote>

</details>

---

### Q28. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow></mfenced><mo>:</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfrac><mo>&#160;</mo><mi>is</mi><mo>&#160;</mo><mi>purely</mi><mo>&#160;</mo><mi>imaginary</mi></mrow></mfenced></math> Then the sum of the elements is in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi mathvariant="normal">&#960;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi mathvariant="normal">&#960;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#960;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">&#960;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi mathvariant="normal">&#960;</mi></math>**

**Detailed Solution:**

<blockquote><p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>3</mn><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac></mfenced><mo>+</mo><mi>i</mi><mfenced><mfrac><mrow><mn>3</mn><mi>sin</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac></mfenced></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> is a purely imaginary number, so real part must be zero, hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac></math>, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>Sum of all values <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>16</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac><mo>=</mo><mn>4</mn><mi mathvariant="normal">&#960;</mi></math></p></blockquote>

</details>

---

### Q29. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mfenced close="|" open="|"><mrow><mi>z</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>z</mi><mo>+</mo><mn>4</mn><mo>(</mo><mn>1</mn><mo>+</mo><mi>i</mi><mo>)</mo><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi></math> are the roots of the equation

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>12</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>12</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>12</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>&#946;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced close="|" open="|"><mrow><mi>z</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>z</mi><mo>+</mo><mn>4</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>&#946;</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>z</mi><mo>+</mo><mn>4</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>z</mi><mo>+</mo><mn>4</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup></msqrt><mo>=</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mi>i</mi><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>4</mn></mrow></mfenced></math></p><p>Now on comparing real and imaginary part, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mo>(</mo><mi>&#945;</mi><mo>+</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup></msqrt><mo>=</mo><mi>&#945;</mi><mo>+</mo><mn>4</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mo>)</mo></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo></math></p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mo>(</mo><mi>&#945;</mi><mo>+</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>16</mn></msqrt><mo>=</mo><mi>&#945;</mi><mo>+</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>&#945;</mi><mo>+</mo><mn>20</mn><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>&#945;</mi><mo>+</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p>We know that quadratic equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mtext>sum&#160;of&#160;roots</mtext></mfenced><mi>x</mi><mo>+</mo><mfenced><mtext>product&#160;of&#160;roots</mtext></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, equation with roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>12</mn><mo>=</mo><mn>0</mn></math></p></blockquote>

</details>

---

### Q30. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8800;</mo><mi>b</mi></math> be two non-zero real numbers. Then the number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>z</mi><mo>&#8712;</mo><mi>C</mi><mo>:</mo><mi>Re</mi><mfenced><mrow><mi>a</mi><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>z</mi></mrow></mfenced><mo>=</mo><mi>a</mi><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mi>Re</mi><mfenced><mrow><mi>b</mi><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>z</mi></mrow></mfenced><mo>=</mo><mi>b</mi></mrow></mfenced></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>z</mi><mo>&#8712;</mo><mi>C</mi><mo>:</mo><mi>Re</mi><mfenced><mrow><mi>a</mi><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>z</mi></mrow></mfenced><mo>=</mo><mi>a</mi><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mi>Re</mi><mfenced><mrow><mi>b</mi><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>z</mi></mrow></mfenced><mo>=</mo><mi>b</mi></mrow></mfenced></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>Re</mi><mfenced><mrow><mi>a</mi><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>z</mi></mrow></mfenced><mo>=</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Re</mi><mfenced><mrow><mi>a</mi><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mi>b</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Re</mi><mfenced><mrow><mi>a</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>i</mi><mi>x</mi><mi>y</mi></mrow></mfenced><mo>+</mo><mi>b</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mi>b</mi><mi>x</mi><mo>=</mo><mi>a</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>Re</mi><mfenced><mrow><mi>b</mi><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>z</mi></mrow></mfenced><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Re</mi><mfenced><mrow><mi>b</mi><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mi>a</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Re</mi><mfenced><mrow><mi>b</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>i</mi><mi>x</mi><mi>y</mi></mrow></mfenced><mo>+</mo><mi>a</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>b</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mi>a</mi><mi>x</mi><mo>=</mo><mi>b</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>-</mo><mfenced><mi>ii</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>-</mo><mi>x</mi><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mi>a</mi><mo>-</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi>iii</mi></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>+</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> (Note: here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>&#8800;</mo><mn>0</mn></math> is considered but it is not clear from the question)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi>iv</mi></mfenced></math></p><p>Now from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>iii</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>iv</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>1</mn></math> (No solution)</p></blockquote>

</details>

---

### Q31. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi></math> be two real numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>&#60;</mo><mn>0</mn></math>. If the complex number <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>i</mi></mrow><mrow><mi>b</mi><mo>+</mo><mi>i</mi></mrow></mfrac></math> is of unit modulus and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>i</mi><mi>b</mi></math> lies on the circle <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mn>2</mn><mi>z</mi></mrow></mfenced></math>, then a possible value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mfenced close="]" open="["><mi>a</mi></mfenced></mrow><mrow><mn>4</mn><mi>b</mi></mrow></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> is greatest integer function, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi></math> be two real numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>&#60;</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>i</mi></mrow><mrow><mi>b</mi><mo>+</mo><mi>i</mi></mrow></mfrac></mfenced><mo>=</mo><mn>1</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>i</mi><mi>b</mi></math> lies on the circle <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mn>2</mn><mi>z</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>&#60;</mo><mn>0</mn></math></p><p>Now using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>i</mi></mrow><mrow><mi>b</mi><mo>+</mo><mi>i</mi></mrow></mfrac></mfenced><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>i</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>b</mi><mo>+</mo><mi>i</mi></mrow></mfenced></math></p><p>Now squaring both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>i</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mi>b</mi><mo>+</mo><mi>i</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>i</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi><mi>i</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mi>b</mi><mo>+</mo><mi>i</mi></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>-</mo><mi>i</mi></mrow></mfenced><mo>&#160;</mo><mfenced close="}" open="{"><mrow><msup><mfenced close="|" open="|"><mi>z</mi></mfenced><mn>2</mn></msup><mo>=</mo><mi>z</mi><mover><mi>z</mi><mo>&#175;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>&#177;</mo><mi>b</mi><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mi>a</mi></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>&#60;</mo><mn>0</mn></math></p><p>Now given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> lies on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi mathvariant="normal">z</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi mathvariant="normal">z</mi></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mo>+</mo><mi>i</mi><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced close="|" open="|"><mrow><mi>a</mi><mo>+</mo><mi>i</mi><mi>b</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mrow><mi>a</mi><mo>-</mo><mn>1</mn><mo>+</mo><mi>i</mi><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><msup><mfenced close="|" open="|"><mrow><mi>a</mi><mo>+</mo><mi>i</mi><mi>b</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mfenced><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mi>a</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>a</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#177;</mo><msqrt><mn>28</mn></msqrt></mrow><mn>12</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>7</mn></msqrt></mrow><mn>6</mn></mfrac></math></p><p>Taking positive sign we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mrow><msqrt><mn>7</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mn>6</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>7</mn></msqrt></mrow><mn>6</mn></mfrac><mo>&#160;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mi>a</mi></mrow></mfenced></math></p><p>Now the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>a</mi></mfenced><mo>=</mo><mn>0</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mfrac><mrow><msqrt><mn>7</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mn>6</mn></mfrac><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mfenced close="]" open="["><mi>a</mi></mfenced></mrow><mrow><mn>4</mn><mi>b</mi></mrow></mfrac><mo>=</mo><mfrac><mn>6</mn><mrow><mn>4</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msqrt><mn>7</mn></msqrt></mrow></mfenced></mrow></mfrac><mo>=</mo><mo>-</mo><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>7</mn></msqrt></mrow><mn>4</mn></mfrac></mfenced></math></p><p>Now taking negative sign we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>-</mo><msqrt><mn>7</mn></msqrt></mrow><mn>6</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mfrac><mrow><msqrt><mn>7</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mn>6</mn></mfrac></math></p><p>Now  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>a</mi></mfenced><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>&#60;</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>-</mo><msqrt><mn>7</mn></msqrt></mrow><mn>6</mn></mfrac><mo>&#60;</mo><mn>0</mn></mrow></mfenced></math></p><p>So, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mfenced close="]" open="["><mi>a</mi></mfenced></mrow><mrow><mn>4</mn><mi>b</mi></mrow></mfrac><mo>=</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>4</mn><mi>b</mi></mrow></mfrac><mo>=</mo><mfrac><mn>0</mn><mrow><mn>4</mn><mi>b</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p>Note- Official answer key was drop by NTA, here we have modified the option.</p>

</details>

---

### Q32. JEE Main 2023 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi>i</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">i</mi><mover><mi mathvariant="italic">z</mi><mo mathvariant="italic">&#175;</mo></mover></mrow><mrow><mover><mi mathvariant="italic">z</mi><mo mathvariant="italic">&#175;</mo></mover><mo>(</mo><mn>1</mn><mo>-</mo><mi>z</mi><mo>)</mo><mo>+</mo><mfrac><mn>1</mn><mi>z</mi></mfrac></mrow></mfrac><mo>&#183;</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>12</mn><mi>&#960;</mi></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>arg</mi><mfenced><msub><mi>z</mi><mn>1</mn></msub></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mn>1</mn><mo>-</mo><mi>i</mi></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>z</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>i</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>i</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>i</mi></mrow><mn>2</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mover><mi>z</mi><mo mathvariant="italic">&#175;</mo></mover></mrow><mrow><mover><mi>z</mi><mo mathvariant="italic">&#175;</mo></mover><mo>(</mo><mn>1</mn><mo>-</mo><mi>z</mi><mo>)</mo><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">z</mi></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mo>-</mo><msup><mi>i</mi><mn>2</mn></msup></mrow><mrow><mo>(</mo><mn>1</mn><mo>-</mo><mi>i</mi><mo>)</mo><mo>(</mo><mo>-</mo><mi>i</mi><mo>)</mo><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>i</mi></mrow><mn>2</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mo>-</mo><msup><mi>i</mi><mn>2</mn></msup></mrow><mrow><mo>-</mo><mi>i</mi><mo>+</mo><msup><mi>i</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mstyle displaystyle="true"><mfrac><mi>i</mi><mn>2</mn></mfrac></mstyle></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mo>+</mo><mi>i</mi></mrow><mfrac><mrow><mo>-</mo><mn>3</mn><mi>i</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mo>+</mo><mn>2</mn><mi>i</mi></mrow><mrow><mo>-</mo><mn>3</mn><mi>i</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mo>(</mo><mn>4</mn><mo>+</mo><mn>2</mn><mi>i</mi><mo>)</mo><mo>(</mo><mn>3</mn><mi>i</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mrow><mo>(</mo><mn>3</mn><mi>i</mi><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mo>(</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>12</mn><mi>i</mi><mo>-</mo><mn>4</mn><mo>+</mo><mn>6</mn><msup><mi>i</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>i</mi></mrow><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>10</mn><mi>i</mi><mo>-</mo><mn>10</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mi>i</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Arg</mo><mfenced><msub><mi>z</mi><mn>1</mn></msub></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mn>12</mn><mi>&#960;</mi></mfrac><mi>arg</mi><mfenced><msub><mi mathvariant="normal">z</mi><mn>1</mn></msub></mfenced><mo>=</mo><mfrac><mn>12</mn><mi>&#960;</mi></mfrac><mo>&#215;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q33. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>&#8800;</mo><mn>0</mn></math> be a complex number such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><mfrac><mn>1</mn><mi>z</mi></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn></math>, then the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>z</mi></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><mfrac><mn>1</mn><mi>z</mi></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>-</mo><mfrac><mn>1</mn><mfenced close="|" open="|"><mi>z</mi></mfenced></mfrac></mrow></mfenced><mo>&#8804;</mo><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><mfrac><mn>1</mn><mi>z</mi></mfrac></mrow></mfenced><mo>&#8804;</mo><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mfrac><mn>1</mn><mfenced close="|" open="|"><mi>z</mi></mfenced></mfrac></math> Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>=</mo><mi>r</mi></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>r</mi><mo>-</mo><mfrac><mn>1</mn><mi>r</mi></mfrac></mrow></mfenced><mo>&#8804;</mo><mn>2</mn></math> and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>+</mo><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>&#8805;</mo><mn>2</mn></math> which is always true.</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>r</mi><mo>-</mo><mfrac><mn>1</mn><mi>r</mi></mfrac></mrow></mfenced><mo>&#8804;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>-</mo><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>&#8805;</mo><mo>-</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>r</mi><mo>-</mo><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>&#8804;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mn>2</mn><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>&#8804;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>-</mo><mn>1</mn><mo>&#8804;</mo><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msub><mfenced close="|" open="|"><mi>z</mi></mfenced><mi>max</mi></msub><mo>=</mo><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></math></p></blockquote>

</details>

---

### Q34. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>2</mn><mo>+</mo><mn>3</mn><mi>i</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>5</mn></msup><mo>+</mo><msup><mfenced><mover><mi>z</mi><mo>&#175;</mo></mover></mfenced><mn>5</mn></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>244</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>224</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>245</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>265</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>244</mn></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>2</mn><mo>+</mo><mn>3</mn><mi>i</mi></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>5</mn></msup><mo>+</mo><msup><mfenced><mover><mi>z</mi><mo>&#175;</mo></mover></mfenced><mn>5</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mn>3</mn><mi>i</mi></mrow></mfenced><mn>5</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mo>-</mo><mn>3</mn><mi>i</mi></mrow></mfenced><mn>5</mn></msup></math></p><p>Applying binomial expansion we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><msup><mn>2</mn><mn>5</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><msup><mn>2</mn><mn>3</mn></msup><msup><mfenced><mrow><mn>3</mn><mi>i</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><msup><mn>2</mn><mn>1</mn></msup><msup><mfenced><mrow><mn>3</mn><mi>i</mi></mrow></mfenced><mn>4</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mn>32</mn><mo>+</mo><mn>10</mn><mo>&#215;</mo><mn>8</mn><mfenced><mrow><mo>-</mo><mn>9</mn></mrow></mfenced><mo>+</mo><mn>5</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>81</mn></mrow></mfenced><mo>=</mo><mn>244</mn></math></p></blockquote>

</details>

---

### Q35. JEE Main 2022 (28 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">z</mi><mo>=</mo><mi mathvariant="normal">a</mi><mo>+</mo><mi>i</mi><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">b</mi><mo>&#8800;</mo><mn>0</mn></math> be complex numbers satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">z</mi><mn>2</mn></msup><mo>=</mo><mover><mi mathvariant="normal">z</mi><mo>&#175;</mo></mover><mo>&#183;</mo><msup><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mfenced open="|" close="|"><mi>z</mi></mfenced></mrow></msup></math>. Then the least value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mi>n</mi></msup><mo>=</mo><msup><mfenced><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup></math>, is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>=</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>&#183;</mo><msup><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mfenced close="|" open="|"><mi>z</mi></mfenced></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>On taking modulus both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="|" close="|"><mi>z</mi></mfenced><mn>2</mn></msup><mo>=</mo><mfenced open="|" close="|"><menclose notation="top"><mi>z</mi></menclose></mfenced><mo>&#183;</mo><msup><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mfenced open="|" close="|"><mi>z</mi></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>=</mo><msup><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mfenced close="|" open="|"><mi>z</mi></mfenced></mrow></msup><mo>,</mo><mo>&#160;&#160;</mo><mo>&#8757;</mo><mo>&#160;</mo><mi>b</mi><mo>&#8800;</mo><mn>0</mn><mo>&#8658;</mo><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p>So comparing both side we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>i</mi><mi>b</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></msqrt><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>3</mn></mfenced></math></p><p>Now again from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> we get:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mi>i</mi><mn>2</mn><mi>a</mi><mi>b</mi><mo>=</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mi>i</mi><mi>b</mi></mrow></mfenced><msup><mn>2</mn><mn>0</mn></msup><mo>=</mo><mi>a</mi><mo>-</mo><mi>i</mi><mi>b</mi></math></p><p>Now on comaparing imagenary and real part we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mi>b</mi><mo>=</mo><mo>-</mo><mi>b</mi></math></p><p>Now solving we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mo>&#177;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>i</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>i</mi></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mi>n</mi></msup><mo>=</mo><msup><mfenced><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><mo>&#8658;</mo><msup><mfenced><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mi>z</mi></mfrac></mfenced><mi>n</mi></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>z</mi></mfrac></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt><mi>i</mi></mrow><mn>2</mn></mfrac></mfenced><mi>n</mi></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mn>1</mn></math>, then minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is <span style="background-color:null;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></span></p></blockquote>

</details>

---

### Q36. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>,</mo><mi>&#960;</mi><mo>&#60;</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#60;</mo><mn>2</mn><mi>&#960;</mi></math>, for which the complex number <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>i</mi><mi>sin</mi><mi>&#945;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi><mi>sin</mi><mi>&#945;</mi></mrow></mfrac></math> is purely imaginary and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mi>cos</mi><mi>&#946;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>i</mi><mi>cos</mi><mi>&#946;</mi></mrow></mfrac></math> is purely real. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Z</mi><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></msub><mo>=</mo><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>cos</mi><mn>2</mn><mi>&#946;</mi><mo>,</mo><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>&#8712;</mo><mi>S</mi></math>.
Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>&#8712;</mo><mi>S</mi></mrow></munder><mfenced><mrow><mi>i</mi><msub><mi>Z</mi><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></msub><mo>+</mo><mfrac><mn>1</mn><mrow><mi>i</mi><msub><mover><mi>Z</mi><mo>&#175;</mo></mover><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></msub></mrow></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>i</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><mi>i</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>&#60;</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#60;</mo><mn>2</mn><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>i</mi><mi>sin</mi><mi>&#945;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>&#945;</mi></mrow></mfenced></mrow></mfrac></math> is purely imaginary</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>i</mi><mi>sin</mi><mi>&#945;</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>&#945;</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#945;</mi></mrow></mfrac></math> is purely imaginary</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#945;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mi>cos</mi><mi>&#946;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mi>cos</mi><mi>&#946;</mi></mrow></mfenced></mrow></mfrac></math> is purely real</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mi>cos</mi><mi>&#946;</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi><mi>cos</mi><mi>&#946;</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#946;</mi></mrow></mfrac></math> is purely real</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>cos</mi><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Z</mi><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></msub><mo>=</mo><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>cos</mi><mn>2</mn><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>Z</mi><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></msub><mo>=</mo><mi>sin</mi><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mi>i</mi><mi>cos</mi><mn>3</mn><mi>&#960;</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>i</mi></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Z</mi><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></msub><mo>=</mo><mi>sin</mi><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mi>i</mi><mi>cos</mi><mn>3</mn><mi>&#960;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>-</mo><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>&#8712;</mo><mi>S</mi></mrow></munder><mfenced><mrow><mi>i</mi><msub><mi>Z</mi><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></msub><mo>+</mo><mfrac><mn>1</mn><mrow><mi>i</mi><msub><mover><mi>Z</mi><mo>&#175;</mo></mover><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></msub></mrow></mfrac></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><mi>i</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>i</mi></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mrow><mi>i</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced></mrow></mfrac></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mi>i</mi><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>i</mi></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mrow><mi>i</mi><mfenced><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><mi>i</mi><mo>+</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mi>i</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>i</mi></mrow></mfenced></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mo>-</mo><mi>i</mi><mo>+</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mi>i</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>1</mn></math></p></blockquote>

</details>

---

### Q37. JEE Main 2022 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>z</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8450;</mi><mo>:</mo><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mn>0</mn></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>z</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mfenced><mrow><mo>Re</mo><mfenced><mi>z</mi></mfenced><mo>+</mo><mo>Im</mo><mfenced><mi>z</mi></mfenced></mrow></mfenced></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>z</mi><mo>&#8712;</mo><mi>C</mi><mo>:</mo><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mn>0</mn></mrow></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>i</mi><mi>x</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mi>x</mi><mo>-</mo><mi>i</mi><mi>y</mi></math></p><p>Now putting the value in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now on comparing both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Now if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mtext>then&#160;</mtext><mi>y</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>z</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mfenced><mrow><mo>Re</mo><mfenced><mi>z</mi></mfenced><mo>+</mo><mo>Im</mo><mfenced><mi>z</mi></mfenced><mo>=</mo><mfenced><mrow><mn>0</mn><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mn>0</mn><mo>+</mo><mn>0</mn><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math></p></blockquote>

</details>

---

### Q38. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the minimum value <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mn>0</mn></msub></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><msup><mfenced open="|" close="|"><mi>z</mi></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="|" close="|"><mrow><mi>z</mi><mo>-</mo><mn>6</mn><mi>i</mi></mrow></mfenced><mn>2</mn></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8450;</mi></math> is attained at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><msub><mi>z</mi><mn>0</mn></msub></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mn>2</mn><msubsup><mi>z</mi><mn>0</mn><mn>2</mn></msubsup><mo>-</mo><msubsup><mover><mi>z</mi><mo>&#175;</mo></mover><mn>0</mn><mn>3</mn></msubsup><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1024</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1105</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1196</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math>**

**Detailed Solution:**

<blockquote><p>Given, the minimum value <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mn>0</mn></msub></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><msup><mfenced close="|" open="|"><mi>z</mi></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><mn>6</mn><mi>i</mi></mrow></mfenced><mn>2</mn></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8450;</mi></math> is attained at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><msub><mi>z</mi><mn>0</mn></msub></math>,</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>9</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>y</mi><mo>+</mo><mn>36</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>15</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>min</mi></msub></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi><mo>=</mo><msub><mi>z</mi><mn>0</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mn>0</mn></msub><mo>=</mo><mn>30</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mn>2</mn><msubsup><mi>z</mi><mn>0</mn><mn>2</mn></msubsup><mo>-</mo><msubsup><mover><mi>z</mi><mo>&#175;</mo></mover><mn>0</mn><mn>3</mn></msubsup><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msubsup><mi>v</mi><mn>0</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>i</mi></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>900</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mo>-</mo><mn>6</mn><mo>+</mo><mn>8</mn><mi>i</mi><mo>-</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mn>8</mn><mi>i</mi><mo>-</mo><mn>6</mn><mi>i</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>900</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mn>8</mn><mo>+</mo><mn>6</mn><mi>i</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>900</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1000</mn></math></p></blockquote>

</details>

---

### Q39. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8450;</mi></math> if the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfenced open="|" close="|"><mrow><mi>z</mi><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>+</mo><mfenced open="|" close="|"><mrow><mi>z</mi><mo>-</mo><mi>p</mi><msqrt><mn>2</mn></msqrt><mi>i</mi></mrow></mfenced></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msqrt><mn>2</mn></msqrt></math>, then a value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is _______.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<blockquote><p>Note that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math> is the distance between the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>,</mo><mn>0</mn></mrow></mfenced></math> on argand plane.</p><p>Note that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><mi>p</mi><msqrt><mn>2</mn></msqrt><mi>i</mi></mrow></mfenced></math> is the distance between the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mi>p</mi><msqrt><mn>2</mn></msqrt></mrow></mfenced></math> on argand plane.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ba6c7191-3d0e-4094-b2a0-b7d1f2ccdec3-image.png" style="width: 257px; height: 140px;" />​​​​​​​</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><mi>p</mi><msqrt><mn>2</mn></msqrt><mi>i</mi></mrow></mfenced></math> is sum of distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>,</mo><mn>0</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mi>p</mi><msqrt><mn>2</mn></msqrt></mrow></mfenced></math></p><p>For minimising the sum, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> should lie on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> should be equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msqrt><mn>2</mn></msqrt></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mi>B</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>18</mn><mo>+</mo><mn>2</mn><msup><mi>p</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&rArr;</mo><mn>18</mn><mo>+</mo><mn>2</mn><msup><mi>p</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>5</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&rArr;</mo><msup><mi>p</mi><mn>2</mn></msup><mo>=</mo><mn>16</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mo>&plusmn;</mo><mn>4</mn></math></p></blockquote>

</details>

---

### Q40. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>2</mn><mi>i</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>. Then, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>&#945;</mi><mn>8</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>8</mn></msup></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>250</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1250</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1550</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>**

**Detailed Solution:**

<p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>i</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>2</mn><mi>i</mi><mo>+</mo><mn>1</mn><mo>=</mo><msup><mi>&#946;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>4</mn></msup><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>2</mn><mi>i</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><msup><mi>i</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><mn>4</mn><mi>i</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>-</mo><mn>4</mn><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>8</mn></msup><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>3</mn><mo>-</mo><mn>4</mn><mi>i</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>7</mn><mo>+</mo><mn>24</mn><mi>i</mi></math></p><p>Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mn>8</mn></msup><mo>=</mo><mo>-</mo><mn>7</mn><mo>+</mo><mn>24</mn><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced close="|" open="|"><mrow><msup><mi>&#945;</mi><mn>8</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>8</mn></msup></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mn>14</mn><mo>+</mo><mn>48</mn><mi>i</mi></mrow></mfenced><mo>=</mo><mn>50</mn></math></p>

</details>

---

### Q41. JEE Main 2022 (28 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Sum of squares of modulus of all the complex numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mi>i</mi><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup><mo>-</mo><mi>z</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">z</mi><mo>+</mo><mover><mi mathvariant="normal">z</mi><mo>&#175;</mo></mover><mo>=</mo><msup><mi>izz</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">z</mi><mn>2</mn></msup></math></p><p>Consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>=</mo><mfenced><mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi><mi>i</mi></mrow></mfenced></math></p><p>On comparing real and imaginary part we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>=</mo><mo>-</mo><mn>4</mn><mi>x</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p>Case 1: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>2</mn><mo>&#215;</mo><mn>0</mn><mo>=</mo><mfenced><mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mn>0</mn><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>0</mn><mo>&#215;</mo><mi>y</mi><mi>i</mi></mrow></mfenced><mi>y</mi><mo>=</mo><mn>0</mn></math> </p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p>Case 2: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mo>&#177;</mo><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>&#177;</mo><msqrt><mn>2</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>i</mi><mn>2</mn></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>i</mi><mn>2</mn></mfrac></math></p><p>Sum of squares of modulus of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>+</mo><mfrac><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>4</mn></mfrac><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q42. JEE Main 2022 (25 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>2</mn></msub></math> be two complex numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>z</mi><mo>&#175;</mo></mover><mn>1</mn></msub><mo>=</mo><mi>i</mi><msub><mover><mi>z</mi><mo>&#175;</mo></mover><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>arg</mi><mfenced><mfrac><msub><mi>z</mi><mn>1</mn></msub><msub><mover><mi>z</mi><mo>&#175;</mo></mover><mn>2</mn></msub></mfrac></mfenced><mo>=</mo><mi>&#960;</mi></math>, then the argument of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>arg</mtext><mo>&#160;</mo><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>arg</mtext><mo>&#160;</mo><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>arg</mtext><mo>&#160;</mo><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>arg</mtext><mo>&#160;</mo><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>arg</mtext><mo>&#160;</mo><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>z</mi><mo>&#175;</mo></mover><mn>1</mn></msub><mo>=</mo><mi>i</mi><msub><mover><mi>z</mi><mo>&#175;</mo></mover><mn>2</mn></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mi>i</mi><msub><mi>z</mi><mn>2</mn></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mi>i</mi><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><msub><mi>z</mi><mn>2</mn></msub><mo>&#8658;</mo><msup><mi>e</mi><mfrac><mrow><mi>i</mi><mi>&#960;</mi></mrow><mn>2</mn></mfrac></msup><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><msub><mi>z</mi><mn>2</mn></msub></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>arg</mi><mfenced><mfrac><msub><mi>z</mi><mn>1</mn></msub><msub><mover><mi>z</mi><mo>&#175;</mo></mover><mn>2</mn></msub></mfrac></mfenced><mo>=</mo><mi>&#960;</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><mi>r</mi><msup><mi>e</mi><mrow><mi>i</mi><mi>&#952;</mi></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mover><msub><mi>z</mi><mn>2</mn></msub><mo>&#175;</mo></mover><mo>=</mo><mi>r</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>i</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mi>&#952;</mi></mrow></mfenced></mrow></msup></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>arg</mi><mfenced><msup><mi>e</mi><mrow><mi>i</mi><mfenced><mrow><mn>2</mn><mi>&#952;</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></mrow></msup></mfenced><mo>=</mo><mi>&#960;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn><mi>&#952;</mi><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>=</mo><mi mathvariant="normal">&#960;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p>

</details>

---

### Q43. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> is a complex number such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>z</mi><mo>-</mo><mi>i</mi></mrow><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math> is purely imaginary, then the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>z</mi><mo>-</mo><mo>(</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>&#160;</mo><mi>i</mi><mo>)</mo><mo>|</mo></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mi>i</mi></mrow><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math> is purely imaginary.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>arg</mi><mfenced><mfrac><mrow><mi>z</mi><mo>-</mo><mi>i</mi></mrow><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mi>n</mi><mi>&#960;</mi><mo>;</mo><mi>n</mi><mo>&#8712;</mo><mi>I</mi></math></p><p>Geometrically, the locus of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> is the circle with end points of diameter is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and centre is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>.So the nearest point to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> on the circle is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a35641e8-1e2b-43ec-88b0-28240d321060-image.png" style="width: 347px; height: 200px;" /></p><p>Minimum distance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>P</mi><mo>=</mo><mi>O</mi><mi>P</mi><mo>-</mo><mi>O</mi><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></msqrt><mo>-</mo><msqrt><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q44. JEE Main 2021 (27 Aug Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>2</mn></msub></math> be two complex numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>arg</mi><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>-</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>,</mo><msub><mi>z</mi><mn>2</mn></msub></math> satisfy the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>z</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mo>Re</mo><mo>(</mo><mi>z</mi><mo>)</mo></math>. Then the imaginary part <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mi>i</mi><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mi>i</mi><msub><mi>y</mi><mn>2</mn></msub></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>-</mo><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mo>+</mo><mi>i</mi><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>arg</mi><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>-</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mo>-</mo><mo>-</mo><mo>-</mo><mo>(</mo><mn>1</mn><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mo>Re</mo><mfenced><msub><mi>z</mi><mn>1</mn></msub></mfenced><mo>&#8658;</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msubsup><mi>y</mi><mn>1</mn><mn>2</mn></msubsup><mo>=</mo><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mi>z</mi><mn>2</mn></msub><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mo>Re</mo><mfenced><msub><mi>z</mi><mn>2</mn></msub></mfenced><mo>&#8658;</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msubsup><mi>y</mi><mn>2</mn><mn>2</mn></msubsup><mo>=</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mfenced><mrow><msubsup><mi>y</mi><mn>1</mn><mn>2</mn></msubsup><mo>-</mo><msubsup><mi>y</mi><mn>2</mn><mn>2</mn></msubsup></mrow></mfenced><mo>=</mo><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup><mo>-</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mn>6</mn><mo>+</mo><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mn>6</mn></math>

</details>

---

### Q45. JEE Main 2021 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

If the real part of the complex number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">z</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfrac><mo>,</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math> is zero, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mn>3</mn><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfrac><mo>,</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mn>9</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mfrac><mfenced><mrow><mn>3</mn><mo>-</mo><mn>6</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>11</mn><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mrow><mn>1</mn><mo>+</mo><mn>9</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Re</mo><mfenced><mi>z</mi></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mn>6</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mn>9</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>-</mo><mn>6</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mfrac><mn>3</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mo>&#177;</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>&#8757;</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mn>3</mn><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mi>sin</mi><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>cos</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mi>sin</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>cos</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q46. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> denote the number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mn>0</mn><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> is a complex number. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><msup><mi>n</mi><mi>k</mi></msup></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mn>0</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi><mo>,</mo></math> then we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mi>x</mi><mo>-</mo><mi>i</mi><mi>y</mi><mo>,</mo></math> hence, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>i</mi><mn>2</mn></msup><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>i</mi><mi>x</mi><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>i</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p>We also, know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>i</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo></math> hence, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>i</mi><mi>x</mi><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>i</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mi>i</mi><mo>(</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>)</mo><mo>=</mo><mn>0</mn><mo>+</mo><mi>i</mi><mn>0</mn></math></p><p>On comparing the real and imaginary parts, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mi>y</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>y</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>,</mo></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>27</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>&#177;</mo><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>.</mo></math></p><p>Now, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> in the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>,</mo></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>3</mn><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> No of solutions<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mo>=</mo><mn>4</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mfrac><mn>1</mn><msup><mi>n</mi><mi>k</mi></msup></mfrac></mfenced><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mfrac><mn>1</mn><msup><mn>4</mn><mi>k</mi></msup></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>1</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>64</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo></math></p><p>The above progression is a geometric progression, with first term <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1</mn></math> and common ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math> and the sum of infinite terms of the geometric progression is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mrow><mn>1</mn><mo>-</mo><mi>r</mi></mrow></mfrac></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mfrac><mn>1</mn><msup><mi>n</mi><mi>k</mi></msup></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>4</mn></mfrac></mstyle></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>4</mn></mfrac></mstyle></mfenced></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q47. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The least value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>z</mi></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> is complex number which satisfies the inequality <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mfenced><mrow><mfrac><mrow><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mfenced close="|" open="|"><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></mrow></mfenced></msup><mo>&#8805;</mo><msub><mi>log</mi><msqrt><mn>2</mn></msqrt></msub><mfenced close="|" open="|"><mrow><mn>5</mn><msqrt><mn>7</mn></msqrt><mo>+</mo><mn>9</mn><mi>i</mi></mrow></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt><mo>,</mo></math> is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>5</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mfenced><mrow><mfrac><mrow><mfenced><mrow><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mfenced open="|" close="|"><mrow><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></mrow></mfenced></msup><mo>&#8805;</mo><msub><mi>log</mi><msqrt><mn>2</mn></msqrt></msub><mfenced open="|" close="|"><mrow><mn>5</mn><msqrt><mn>7</mn></msqrt><mo>+</mo><mn>9</mn><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mfrac><mrow><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></msup><mo>&#8805;</mo><mi>l</mi><mi>o</mi><msub><mi>g</mi><msqrt><mn>2</mn></msqrt></msub><mfenced><mn>16</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mfrac><mrow><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></msup><mo>&#8805;</mo><msup><mn>2</mn><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>&#8805;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8805;</mo><mn>3</mn><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mi>z</mi></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>-</mo><mn>3</mn><mo>&#8805;</mo><mn>3</mn><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mi>z</mi></mfenced><mn>2</mn></msup><mo>+</mo><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>-</mo><mn>6</mn><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8805;</mo><mn>0</mn><mo>&#8658;</mo><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>-</mo><mn>3</mn><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>&#8805;</mo><mn>3</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo><msub><mfenced close="|" open="|"><mi>z</mi></mfenced><mi>min</mi></msub><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q48. JEE Main 2021 (24 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

If the least and the largest real values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo></math> for which the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>+</mo><mi>&#945;</mi><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mi>i</mi><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>z</mi><mo>&#8712;</mo><mi>C</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced></math> has a solution, are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> respectively; then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">4</mi><mfenced><mrow><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></mrow></mfenced></math> is equal to_______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi><mo>+</mo><mi>&#945;</mi><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mi>i</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>+</mo><mi>&#945;</mi><msqrt><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>+</mo><mi>i</mi><mfenced><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>+</mo><mn>0</mn><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>y</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>&#945;</mi><msqrt><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfrac><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mn>5</mn><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mn>5</mn><mn>4</mn></mfrac></mrow></mfenced><mo>&#8658;</mo><mi>&#945;</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac><mo>,</mo><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>p</mi><mo>=</mo><mo>-</mo><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac><mo>;</mo><mi>q</mi><mo>=</mo><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>4</mn><mfenced><mrow><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>4</mn><mfenced><mrow><mfrac><mn>5</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mn>10</mn></math></p>

</details>

---

### Q49. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">z</mi><mo>=</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi>iy</mi></math> be a non-zero complex number such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">z</mi><mn>2</mn></msup><mo>=</mo><mi mathvariant="normal">i</mi><msup><mfenced close="|" open="|"><mi mathvariant="normal">z</mi></mfenced><mn>2</mn></msup></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">z</mi></math> lies on the :

**Options:**

- **(A)** line, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mo>-</mo><mi mathvariant="normal">x</mi></math>
- **(B)** imaginary axis
- **(C)** line, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">x</mi></math>
- **(D)** real axis

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) line, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">x</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mi>i</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>i</mi><mi>x</mi><mi>y</mi><mo>=</mo><mi>i</mi><mo>(</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>)</mo></math></p><p>compare real and imaginary parts</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>y</mi></math></p>

</details>

---

### Q50. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The region represented by <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi><mo>&#8712;</mo><mi>C</mi><mo>:</mo><mo>|</mo><mi>z</mi><mo>|</mo><mo>-</mo><mo>Re</mo><mo>(</mo><mi>z</mi><mo>)</mo><mo>&#8804;</mo><mn>1</mn><mo>}</mo></math> is also given by the inequality

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>&#8805;</mo><mn>2</mn><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>&#8805;</mo><mi>x</mi><mo>+</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>-</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>&#8804;</mo><mi>x</mi><mo>+</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></math>

</details>

---

### Q51. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the four complex numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>,</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>,</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>-</mo><mn>2</mn><mo>Re</mo><mfenced><mover><mi>z</mi><mo>&#175;</mo></mover></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>-</mo><mn>2</mn><mo>Re</mo><mfenced><mi>z</mi></mfenced></math> represent the vertices of a square of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> units in the Argand plane, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>z</mi></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c7627491-aad2-4334-8e7d-b2f60338f2a1-image.png" style="width: 384px; height: 204px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> length of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math></p><p>then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><mover><mi>z</mi><mo>&#175;</mo></mover></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mn>2</mn><mi>i</mi><mi>y</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>y</mi></mfenced><mo>=</mo><mn>2</mn></math></p><p>also <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>-</mo><mfenced><mrow><mi>z</mi><mo>-</mo><mn>2</mn><mo>Re</mo><mfenced><mi>z</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>=</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q52. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>z</mi><mn>2</mn></msub></math> are complex numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Re</mo><mfenced><msub><mi>z</mi><mn>1</mn></msub></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Re</mo><mfenced><msub><mi>z</mi><mn>2</mn></msub></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><msub><mi>z</mi><mn>2</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>arg</mi><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>-</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>m</mi><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced></math> is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mrow><mn>1</mn><mo>&#160;</mo></mrow></msub><mo>=</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mi>i</mi><msub><mi>y</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mi>i</mi><msub><mi>y</mi><mn>2</mn></msub></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>R</mi><mi>e</mi><mfenced><msub><mi>z</mi><mn>1</mn></msub></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msubsup><mi>y</mi><mn>1</mn><mn>2</mn></msubsup><mo>=</mo><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>y</mi><mn>1</mn><mn>2</mn></msubsup><mo>-</mo><mn>2</mn><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mi>z</mi><mn>2</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>R</mi><mi>e</mi><mfenced><msub><mi>z</mi><mn>2</mn></msub></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msubsup><mi>y</mi><mn>2</mn><mn>2</mn></msubsup><mo>=</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>y</mi><mn>2</mn><mn>2</mn></msubsup><mo>&#160;</mo><mo>-</mo><mn>2</mn><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Subtracting equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>y</mi><mn>1</mn><mn>2</mn></msubsup><mo>-</mo><msubsup><mi>y</mi><mn>2</mn><mn>2</mn></msubsup><mo>-</mo><mn>2</mn><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mo>&#160;</mo><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mfenced><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfrac></mfenced><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>Also given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>r</mi><mi>g</mi><mo>&#160;</mo><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>-</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>Putting equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>&#8658;</mo><mi>I</mi><mi>m</mi><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math></p>

</details>

---

### Q53. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mn>45</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#8712;</mo><mi>R</mi></math> has conjugate complex roots and they satisfy <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>10</mn></msqrt><mo>,</mo></math> then

**Options:**

- **(A)** <math><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>b</mi><mo>=</mo><mn>30</mn></math>
- **(B)** <math><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>b</mi><mo>=</mo><mn>72</mn></math>
- **(C)** <math><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>b</mi><mo>=</mo><mn>42</mn></math>
- **(D)** <math><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>b</mi><mo>=</mo><mn>12</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>b</mi><mo>=</mo><mn>30</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>&#946;</mi></math> be one of the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mn>45</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#8712;</mo><mi>R</mi></math>.</p><p>So, its other conjugate complex root will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mover><mrow><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>&#946;</mi></mrow><mo>&#175;</mo></mover><mo>=</mo><mi>&#945;</mi><mo>-</mo><mi>i</mi><mi>&#946;</mi></math>.</p><p>We know that for a quadratic equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>B</mi><mi>x</mi><mo>+</mo><mi>C</mi><mo>=</mo><mn>0</mn></math>, the sum and product of its roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>B</mi><mi>A</mi></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfrac><mi>C</mi><mi>A</mi></mfrac></math> respectively.</p><p>So, the sum of roots of the given equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>i</mi><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mi>b</mi><mn>1</mn></mfrac><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>=</mo><mo>-</mo><mi>b</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math>.</p><p>Also, the product of roots of the given equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>&#946;</mi></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>i</mi><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfrac><mn>45</mn><mn>1</mn></mfrac><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mn>45</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math>.</p><p>Now, given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>10</mn></msqrt></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>&#945;</mi><mo>&#177;</mo><mi>i</mi><mi>&#946;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>10</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup></msqrt><mo>=</mo><mn>2</mn><msqrt><mn>10</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mn>40</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>iii</mi></mfenced></math></p><p>Subtracting equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math> from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>iii</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>5</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>&#8757;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>6</mn></math></p><p>Comparing from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>, we get</p><p><math><mi>b</mi><mo>=</mo><mi></mi><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mi>b</mi><mo>=</mo><msup><mn>6</mn><mn>2</mn></msup><mo>-</mo><mn>6</mn><mo>=</mo><mn>36</mn><mo>-</mo><mn>6</mn><mo>=</mo><mn>30</mn></math>.</p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mo>=</mo><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><mn>6</mn><mo>=</mo><mn>36</mn><mo>+</mo><mn>6</mn><mo>=</mo><mn>42</mn></math>.</p><p>Hence, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>a</mi></mfenced></math> is correct.</p>

</details>

---

### Q54. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mo>+</mo><mi>i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi></mrow><mrow><mn>4</mn><mo>-</mo><mi>i</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#952;</mi></mrow></mfrac><mo>,</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mrow><mn>0</mn><mo>,2</mo><mi>&#960;</mi></mrow></mfenced><mo>,</mo></math> is a real number, then an argument of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>+</mo><mi>i</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#952;</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mfenced separators="|"><mrow><mn>3</mn><mo>+</mo><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfenced></mfrac><mo>&#215;</mo><mfrac><mfenced separators="|"><mrow><mn>4</mn><mo>+</mo><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>4</mn><mo>+</mo><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Im</mi><mo>(</mo><mi>z</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mn>3</mn><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mn>4</mn><mi>sin</mi><mi>&#952;</mi></mrow><mrow><mn>16</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac></math>
As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> is purely real <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mn>4</mn><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">g</mi><mfenced separators="|"><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>i</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mi>&#960;</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mrow><mi>cos</mi><mi>&#952;</mi></mrow><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfrac></mfenced><mo>=</mo><mi>&#960;</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mi>&#960;</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced></math></p>

</details>

---

### Q55. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>z</mi><mo>&#8712;</mo><mi>C</mi></math> with <math><mi mathvariant="normal">I</mi><mi mathvariant="normal">m</mi><mo>(</mo><mi>z</mi><mo>)</mo><mo>=</mo><mn>10</mn></math> and it satisfies <math><mfrac><mrow><mn>2</mn><mtext>&#8201;</mtext><mi>z</mi><mo>-</mo><mi>n</mi></mrow><mrow><mn>2</mn><mtext>&#8201;</mtext><mi>z</mi><mo>+</mo><mi>n</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>i</mi><mo>-</mo><mn>1</mn></math> for some natural number <math><mi>n</mi><mo>.</mo></math> Then

**Options:**

- **(A)** <math><mi>n</mi><mo>=</mo><mn>20</mn></math> and <math><mi mathvariant="normal">R</mi><mi mathvariant="normal">e</mi><mo>(</mo><mi>z</mi><mo>)</mo><mo>=</mo><mn>10</mn></math>
- **(B)** <math><mi>n</mi><mo>=</mo><mn>40</mn><mi> </mi></math> and <math><mi> </mi><mi mathvariant="normal">R</mi><mi mathvariant="normal">e</mi><mo>(</mo><mi>z</mi><mo>)</mo><mo>=</mo><mn>10</mn></math>
- **(C)** <math><mi>n</mi><mo>=</mo><mn>20</mn></math> and <math><mi mathvariant="normal">R</mi><mi mathvariant="normal">e</mi><mo>(</mo><mi>z</mi><mo>)</mo><mo>=</mo><mo>-</mo><mn>10</mn></math>
- **(D)** <math><mi>n</mi><mo>=</mo><mn>40</mn></math> and <math><mi mathvariant="normal">R</mi><mi mathvariant="normal">e</mi><mo>(</mo><mi>z</mi><mo>)</mo><mo>=</mo><mo>-</mo><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>n</mi><mo>=</mo><mn>40</mn></math> and <math><mi mathvariant="normal">R</mi><mi mathvariant="normal">e</mi><mo>(</mo><mi>z</mi><mo>)</mo><mo>=</mo><mo>-</mo><mn>10</mn></math>**

**Detailed Solution:**

Put <math><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>10</mn><mi>i</mi></math>  
<math><mo>∴</mo><mtext> </mtext><mn>2</mn><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>10</mn><mi>i</mi></mrow></mfenced><mo>-</mo><mi>n</mi><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mi>i</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>⋅</mo><mfenced open="[" close="]" separators="|"><mrow><mn>2</mn><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>10</mn><mi>i</mi></mrow></mfenced><mo>+</mo><mi>n</mi></mrow></mfenced></math>  
compare real and imaginary coefficients 
<math><mi>x</mi><mo>=</mo><mo>-</mo><mn>10</mn><mo>,</mo><mtext> </mtext><mi>n</mi><mo>=</mo><mn>40</mn></math>

</details>

---

### Q56. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>a</mi><mo>&#62;</mo><mn>0</mn></math> and <math><mi>z</mi><mo>=</mo><mfrac><mrow><msup><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>i</mi><mo>)</mo></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>a</mi><mo>-</mo><mi>i</mi></mrow></mfrac></math> , has magnitude <math><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></msqrt></math> , then <math><mover accent="true"><mrow><mi>z</mi></mrow><mo>-</mo></mover></math> is equal to:

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>i</mi></math>
- **(B)** <math><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>i</mi></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>i</mi></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>i</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>i</mi></math>**

**Detailed Solution:**

<math><mi>Z</mi><mo>=</mo><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>a</mi><mo>-</mo><mi>i</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>i</mi></mrow><mrow><mi>a</mi><mo>-</mo><mi>i</mi></mrow></mfrac></math>
<math><mfenced close="|" open="|" separators="|"><mrow><mi>z</mi></mrow></mfenced><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></msqrt><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mn>2</mn><mi>i</mi></mrow><mrow><mi>a</mi><mo>-</mo><mi>i</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></msqrt></math>
<math><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>3</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mo>&#8757;</mo><mi>a</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math>
So, <math><mover accent="true"><mrow><mi>z</mi></mrow><mo>-</mo></mover><mo>=</mo><mover accent="true"><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn><mi>i</mi></mrow><mrow><mn>3</mn><mo>-</mo><mi>i</mi></mrow></mfrac></mrow></mfenced></mrow><mo>-</mo></mover><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mo>-</mo><mn>2</mn><mi>i</mi></mrow><mrow><mn>3</mn><mo>+</mo><mi>i</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mi>i</mi></mrow><mrow><mn>3</mn><mo>+</mo><mi>i</mi></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mi>i</mi></mrow><mrow><mn>3</mn><mo>-</mo><mi>i</mi></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mo>-</mo><mn>6</mn><mi>i</mi><mo>-</mo><mn>2</mn></mrow><mrow><msup><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>i</mi></math>

</details>

---

### Q57. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>z</mi><mi>&#160;</mi><mo>-</mo><mi>&#160;</mi><mi>&#945;</mi></mrow><mrow><mi>z</mi><mi>&#160;</mi><mo>+</mo><mi>&#160;</mi><mi>&#945;</mi></mrow></mfrac><mfenced separators="|"><mrow><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced></math> is a purely imaginary number and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mi>z</mi></mfenced><mo>=</mo><mn>2</mn></math>, then a value of <math><mi>&#945;</mi></math> is :

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>2</mn></math>**

**Detailed Solution:**

<p>If a complex number is purely imaginary, then it must be equal to negative of its conjugate.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mi>&#945;</mi></mrow><mrow><mi>z</mi><mo>+</mo><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfenced><menclose notation="top"><mfrac><mrow><mi>z</mi><mo>-</mo><mi>&#945;</mi></mrow><mrow><mi>z</mi><mo>+</mo><mi>&#945;</mi></mrow></mfrac></menclose></mfenced><mo>&#8658;</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mi>&#945;</mi></mrow><mrow><mi>z</mi><mo>+</mo><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfenced separators="|"><mfrac><mrow><mover><mi>z</mi><mo>-</mo></mover><mo>-</mo><mi>&#945;</mi></mrow><mrow><mover><mi>z</mi><mo>-</mo></mover><mo>+</mo><mi>&#945;</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>z</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mfenced><mrow><mover><mi>z</mi><mo>-</mo></mover><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mi>z</mi><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mfenced><mrow><mover><mi>z</mi><mo>-</mo></mover><mo>-</mo><mi>&#945;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>z</mi><mover><mi>z</mi><mo>-</mo></mover><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>-</mo><mi>&#945;</mi><mover><mi>z</mi><mo>-</mo></mover><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mfenced separators="|"><mrow><mi>z</mi><mover><mi>z</mi><mo>-</mo></mover><mo>-</mo><mi>&#945;</mi><mi>z</mi><mo>+</mo><mi>&#945;</mi><mover><mi>z</mi><mo>-</mo></mover><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|" separators="|"><mi>z</mi></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>&#160;</mo><mfenced close="]" open="["><mrow><mo>&#8757;</mo><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>=</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>&#177;</mo><mn>2</mn></math></p>

</details>

---

### Q58. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $z$ be a complex number such that $|z|+z=3+i$

$($ where $i=\sqrt{-1})$

Then $|\mathrm{z}|$ is equal to :

**Options:**

- **(A)** $\frac{\sqrt{34}}{3}$
- **(B)** $\frac{5}{3}$
- **(C)** $\frac{\sqrt{41}}{4}$
- **(D)** $\frac{5}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5}{3}$**

**Detailed Solution:**

Since, $|z|+z=3+i$

Let $z=a+i b,$ then

$$

|z|+z=3+i \Rightarrow \sqrt{a^{2}+b^{2}}+a+i b=3+i

$$

Compare real and imaginary coefficients on both sides

$$

\begin{array}{l}

b=1, \sqrt{a^{2}+b^{2}}+a=3 \\

\sqrt{a^{2}+1}=3-a \\

a^{2}+1=a^{2}+9-6 a \\

6 a=8 \Rightarrow a=\frac{4}{3}

\end{array}

$$

Then,

$$

|z|=\sqrt{\left(\frac{4}{3}\right)^{2}+1}=\sqrt{\frac{16}{9}+1}=\frac{5}{3}

$$

</details>

---

### Q59. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mi>z</mi><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>i</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>i</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced separators="|"><mi>z</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced separators="|"><mi>z</mi></mfenced></math> respectively denote the real and imaginary parts of <math><mi>z</mi><mo>,</mo></math> then

**Options:**

- **(A)** <math><mi>I</mi><mfenced separators="|"><mrow><mi>z</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>
- **(B)** <math><mi>R</mi><mfenced separators="|"><mrow><mi>z</mi></mrow></mfenced><mo>&lt;</mo><mn>0</mn></math>  and  <math><mi>I</mi><mfenced separators="|"><mrow><mi>z</mi></mrow></mfenced><mo>&gt;</mo><mn>0</mn></math>
- **(C)** <math><mi>R</mi><mfenced separators="|"><mrow><mi>z</mi></mrow></mfenced><mo>&gt;</mo><mn>0</mn></math>  and  <math><mi>I</mi><mfenced separators="|"><mrow><mi>z</mi></mrow></mfenced><mo>&gt;</mo><mn>0</mn></math>
- **(D)** <math><mi>R</mi><mfenced separators="|"><mrow><mi>z</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi>I</mi><mfenced separators="|"><mrow><mi>z</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Let <math><mi>&#945;</mi><mo>=</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>i</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><msup><mi>&#945;</mi><mn>5</mn></msup><mo>+</mo><msup><mfenced><mover><mi>&#945;</mi><mo>&#175;</mo></mover></mfenced><mn>5</mn></msup><mo>&#160;</mo></math></p><p>We know <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mover><mi>z</mi><mo>&#175;</mo></mover><mi>n</mi></msup><mo>=</mo><msup><mover><mi>z</mi><mo>&#175;</mo></mover><mi>n</mi></msup><mo>&#160;</mo></math>, </p><p>then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>2</mn><mi>R</mi><mi>e</mi><mfenced><msup><mi>&#945;</mi><mn>5</mn></msup></mfenced><mo>&#160;</mo></math></p><p>Hence, <math><mi>I</mi><mfenced separators="|"><mrow><mi>z</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>.</p>

</details>

---

### Q60. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><msub><mrow><mi>z</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi>z</mi></mrow><mrow><mn>2</mn></mrow></msub></math> be any two non-zero complex numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced open="|" close="|"><msub><mi>z</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>4</mn><mfenced open="|" close="|"><msub><mi>z</mi><mn>2</mn></msub></mfenced><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mrow><mn>3</mn><msub><mi>z</mi><mn>1</mn></msub></mrow><mrow><mn>2</mn><msub><mi>z</mi><mn>2</mn></msub></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><msub><mi>z</mi><mn>2</mn></msub></mrow><mrow><mn>3</mn><msub><mi>z</mi><mn>1</mn></msub></mrow></mfrac></math> then maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>z</mi></mfenced></math> is

Note: In actual paper value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mi>z</mi></mfenced></math> was asked. Hence, none of the options given were correct. So we have modified the question as well as options.

**Options:**

- **(A)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msqrt><mfrac><mrow><mn>17</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>r</mi><mi>g</mi><mfenced separators="|"><mfrac><mrow><mn>3</mn><msub><mi>z</mi><mn>1</mn></msub></mrow><mrow><mn>2</mn><msub><mi>z</mi><mn>2</mn></msub></mrow></mfrac></mfenced><mo>=</mo><mi>&#952;</mi><mo>,</mo></math> and we know that, if the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>r</mi><mi>g</mi><mfenced><mi>z</mi></mfenced><mo>=</mo><mi>&#945;</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>r</mi><mi>g</mi><mfenced><mfrac><mn>1</mn><mi>z</mi></mfrac></mfenced><mo>=</mo><mo>-</mo><mi>&#945;</mi><mo>.</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>a</mi><mi>r</mi><mi>g</mi><mfenced separators="|"><mfrac><mrow><mn>2</mn><msub><mi>z</mi><mn>2</mn></msub></mrow><mrow><mn>3</mn><msub><mi>z</mi><mn>1</mn></msub></mrow></mfrac></mfenced><mo>=</mo><mo>-</mo><mi>&#952;</mi></math></p><p>Also, we know that a complex number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi></math> can be expressed as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi><mo>=</mo><mfenced close="|" open="|"><mi>w</mi></mfenced><mfenced><mrow><mi>cos</mi><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>sin</mi><mi>&#945;</mi></mrow></mfenced><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is the argument of the complex number.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mfenced close="|" open="|" separators="|"><mfrac><msub><mi>z</mi><mn>1</mn></msub><msub><mi>z</mi><mn>2</mn></msub></mfrac></mfenced><mfenced separators="|"><mrow><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced close="|" open="|" separators="|"><mfrac><msub><mi>z</mi><mn>2</mn></msub><msub><mi>z</mi><mn>1</mn></msub></mfrac></mfenced><mfenced separators="|"><mrow><mi>cos</mi><mi>&#952;</mi><mo>-</mo><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced close="|" open="|"><msub><mi>z</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>4</mn><mfenced close="|" open="|"><msub><mi>z</mi><mn>2</mn></msub></mfenced><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mfenced close="|" open="|"><mfrac><msub><mi>z</mi><mn>1</mn></msub><msub><mi>z</mi><mn>2</mn></msub></mfrac></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mfenced separators="|"><mrow><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mfenced separators="|"><mrow><mi>cos</mi><mi>&#952;</mi><mo>-</mo><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><mi>cos</mi><mi>&#952;</mi><mo>-</mo><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mfenced separators="|"><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfenced close="|" open="|" separators="|"><mi>z</mi></mfenced><mo>=</mo><msqrt><mfrac><mn>25</mn><mn>4</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mfrac><mn>9</mn><mn>4</mn></mfrac><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></msqrt></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>1</mn><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mi>z</mi></mfenced><mo>=</mo><msqrt><mfrac><mn>25</mn><mn>4</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mfrac><mn>9</mn><mn>4</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>=</mo><msqrt><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></msqrt></math></p><p>And, we know that the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msub><mfenced close="|" open="|" separators="|"><mi>z</mi></mfenced><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">x</mi></mrow></msub><mo>=</mo><msqrt><mn>4</mn><mo>+</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></msqrt><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>.</mo></math></p></blockquote>

</details>

---

### Q61. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mi>A</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi>&#960;</mi></mrow></mfenced><mo>:</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>i</mi><mo>&#8201;</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>i</mi><mi>&#160;</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi></mrow></mfrac><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">p</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">y</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">g</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">y</mi><mi>&#160;</mi></mrow></mfenced><mo>.</mo></math> Then the sum of the elements in <math><mi>A</mi></math> is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>5</mn><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(B)** <math><mi mathvariant="normal">π</mi></math>
- **(C)** <math><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>3</mn><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

Given complex number is  <math><mi>z</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mrow></mfrac></math> 

         <math><mo>⇒</mo><mi>z</mi><mo>=</mo><mfrac><mrow><mo>(</mo><mn>3</mn><mo>+</mo><mn>2</mn><mi>i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>)</mo><mo>(</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>)</mo></mrow><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mn>4</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi><mo>)</mo></mrow></mfrac></math> 

        Since given complex number is purely imaginary

         <math><mo>⇒</mo><mi mathvariant="normal">R</mi><mi mathvariant="normal">e</mi><mo>(</mo><mi>z</mi><mo>)</mo><mo>=</mo><mn>0</mn></math> 

         <math><mo>⇒</mo><mn>3</mn><mo>-</mo><mn>4</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi><mo>=</mo><mn>0</mn></math> 

         <math><mo>⇒</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>=</mo><mo>±</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math> 

         <math><mo>⇒</mo><mi>θ</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math> 

         <math><mo>⇒</mo></math>  sum of all possible values of  <math><mi>θ</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math> .

</details>

---

### Q62. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{z}_1, \mathrm{z}_2$ and $\mathrm{z}_3, \mathrm{z}_4$ are 2 pairs of complex conjugate numbers, then $\arg \left(\frac{z_1}{z_4}\right)+\arg \left(\frac{z_2}{z_3}\right)$ equals:

**Options:**

- **(A)** 0
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{3 \pi}{2}$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Consider $\arg \left(\frac{z_1}{z_4}\right)+\arg \left(\frac{z_2}{z_3}\right)$
$$
=\arg \left(z_1\right)-\arg \left(z_4\right)+\arg \left(z_2\right)-\arg \left(z_3\right)
$$

$$
\begin{aligned}
&=\left(\arg \left(z_1\right)+\arg \left(z_2\right)\right)-\left(\arg \left(z_3\right)+\arg \left(z_4\right)\right) \\
&\quad \operatorname{given}\left(\begin{array}{l}
z_2=\bar{z}_1 \ \\
z_4=\bar{z}_3
\end{array}\right) \\
&=\left(\arg \left(z_1\right)+\arg \left(\bar{z}_1\right)\right)-\left(\arg \left(z_3\right)+\arg \left(\bar{z}_3\right)\right) \\
&\qquad\left\{\begin{array}{l}
\operatorname{also}\left(\arg \left(\bar{z}_1\right)=-\arg \left(z_1\right)\right. \\
\arg \left(\bar{z}_3\right)=-\arg \left(z_3\right)
\end{array}\right\} \\
&=\left(\arg \left(z_1\right)-\arg \left(z_1\right)\right)-\left(\arg \left(z_3\right)-\arg \left(z_3\right)\right) \\
&=0-0=0
\end{aligned}
$$

</details>

---

### Q63. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let $z$ satisfy $|z|=1$ and $z=1-\bar{z}$.
Statement $1: z$ is a real number.
Statement 2 : Principal argument of z is $\frac{\pi}{3}$

**Options:**

- **(A)** Statement 1 is true Statement 2 is true; Statement 2 is a correct explanation for Statement 1 .
- **(B)** Statement 1 is false; Statement 2 is true
- **(C)** Statement 1 is true, Statement 2 is false.
- **(D)** Statement 1 is true; Statement 2 is true; Statement 2 is not a correct explanation for Statement 1 .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement 1 is false; Statement 2 is true**

**Detailed Solution:**

Let $z=x+i y, \bar{z}=x-i y$
$$
\begin{aligned}
& \text { Now, } z=1-\bar{z} \\
\Rightarrow & x+i y=1-(x-i y) \\
\Rightarrow & 2 x=1 \Rightarrow x=\frac{1}{2} \\
& \text { Now, }|z|=1 \Rightarrow x^2+y^2=1 \Rightarrow y^2=1-x^2 \\
\Rightarrow & y=\pm \frac{\sqrt{3}}{2}
\end{aligned}
$$
Now, $\tan \theta=\frac{y}{x} \quad(\theta$ is the argument $)$
$$
=\frac{\sqrt{3}}{2} \div \frac{1}{2}
$$
(+ve since only principal argument)
$$
\begin{gathered}
\quad=\sqrt{3} \\
\Rightarrow \quad \theta=\tan ^{-1} \sqrt{3}=\frac{\pi}{3}
\end{gathered}
$$
Hence, $z$ is not a real number
So, statement-1 is false and 2 is true.

</details>

---

### Q64. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> is a complex number of unit modulus and argument <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math>, then arg <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>z</mi></mrow><mrow><mn>1</mn><mo>+</mo><mover><mi>z</mi><mo>-</mo></mover></mrow></mfrac></mfenced></math> can be equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>given</mi><mi>&#160;</mi><mi>z</mi><mo>&#8800;</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>

**Options:**

- **(A)** <math> <mrow> <mi>θ</mi> </mrow> </math>
- **(B)** <math><mrow>  <mi>&pi;</mi>  <mo>-</mo>  <mi>&theta;</mi></mrow></math>
- **(C)** <math><mrow>  <mo>-</mo>  <mi>&theta;</mi></mrow></math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mi>&pi;</mi> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>-</mo> <mn>&theta;</mn> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mi>θ</mi> </mrow> </math>**

**Detailed Solution:**

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>cos</mi><mo>&#160;</mo><mi>&#952;</mi><mo>+</mo><mi>i</mi><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi></math>

Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>z</mi></mrow><mrow><mn>1</mn><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mo>&#160;</mo><mi>&#952;</mi><mo>+</mo><mi>i</mi><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mo>&#160;</mo><mi>&#952;</mi><mo>-</mo><mi>i</mi><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#160;</mo><msup><mi>cos</mi><mn>2</mn></msup><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mo>+</mo><mi>i</mi><mo>&#183;</mo><mn>2</mn><mo>&#160;</mo><mi>sin</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mi>cos</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow><mrow><mn>2</mn><mo>&#160;</mo><msup><mi>cos</mi><mn>2</mn></msup><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mo>-</mo><mi>i</mi><mo>&#183;</mo><mn>2</mn><mo>&#160;</mo><mi>sin</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mi>cos</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>cos</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mo>+</mo><mi>i</mi><mo>&#160;</mo><mi>sin</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow><mrow><mi>cos</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mo>-</mo><mi>i</mi><mo>&#160;</mo><mi>sin</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mi>cos</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mo>+</mo><mi mathvariant="normal">i</mi><mo>&#160;</mo><mi>sin</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>cos</mi><mo>&#160;</mo><mi>&#952;</mi><mo>+</mo><mi mathvariant="normal">i</mi><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>a</mi><mi>r</mi><mi>g</mi><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mi>z</mi></mrow><mrow><mn>1</mn><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover></mrow></mfrac></mfenced><mo>=</mo><mi>a</mi><mi>r</mi><mi>g</mi><mo>&#160;</mo><mfenced><mi>z</mi></mfenced></math>

<math><mo>=</mo><mi>&#952;</mi></math>

</details>

---

### Q65. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `3`

Let $Z$ and $W$ be complex numbers such that $|Z|=|W|$, and $\arg Z$ denotes the principal argument of $Z$.
Statement 1:If $\arg Z+\arg W=\pi$, then $Z=-\bar{W}$.
Statement 2: $|Z|=|W|$, implies arg $Z-\arg \bar{W}=\pi$.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is false.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation for Statement 1.
- **(C)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation for Statement 1.
- **(D)** Statement 1 is false, Statement 2 is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement 1 is true, Statement 2 is false.**

**Detailed Solution:**

Let $|Z|=|\mathrm{W}|=r$
$$
\Rightarrow Z=r e^{i \theta}, \mathrm{W}=r e^{i \phi}
$$
where $\theta+\phi=\pi$
$$
\therefore \quad \bar{W}=r e^{-i \phi}
$$
Now, $Z=r e^{i(\pi-\phi)}=r e^{i \pi} \times e^{-i \phi}=-r e^{-i \phi}$
$$
=-\bar{W}
$$
Thus, statement-1 is true but statement- 2 is false.

</details>

---

### Q66. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `1`

The conjugate of a complex number is $\frac{1}{i-1}$. Then the complex number is

**Options:**

- **(A)** $\frac{-1}{i-1}$
- **(B)** $\frac{1}{i+1}$
- **(C)** $\frac{-1}{i+1}$
- **(D)** $\frac{1}{i-1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-1}{i+1}$**

**Detailed Solution:**

Put $-i$ in place of $i$
Hence $\frac{-1}{i+1}$.

</details>

---

### Q67. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

If $z_1$ and $z_2$ are two non-zero complex numbers such that $\left|z_1+z_2\right|=\left|z_1\right|+\left|z_2\right|$ then $\arg z_1-\arg z_2$ is equal to

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $-\pi$
- **(C)** 0
- **(D)** $-\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

$\left|z_1+z_2\right|=\left|z_1\right|+\left|z_2\right| \Rightarrow z_1$ and $z_2$ are collinear and are to the same side of origin; hence $\arg z_1-\arg z_2=0$.

</details>

---

### Q68. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

Let $z$, $w$ be complex numbers such that $\bar{z}+i \bar{w}=0$ and $\arg z w=\pi$. Then arg $z$ equals

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{5 \pi}{4}$
- **(C)** $\frac{3 \pi}{4}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3 \pi}{4}$**

**Detailed Solution:**

Here $\omega=\frac{z}{i} \Rightarrow \arg \left(z \cdot \frac{z}{i}\right)=\pi \Rightarrow 2 \arg (z)-\arg (i)=\pi \Rightarrow \arg (z)=\frac{3 \pi}{4}$.

</details>

---

### Q69. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{z}$ and $\omega$ are two non-zero complex numbers such that $|z \omega|=1$ and $\operatorname{Arg}(z)-\operatorname{Arg}(\omega)=\frac{\pi}{2}$, then $\bar{z} \omega$ is equal to

**Options:**

- **(A)** $-\mathrm{i}$
- **(B)** 1
- **(C)** $-1$
- **(D)** i.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\mathrm{i}$**

**Detailed Solution:**

$|z \omega|=1$    <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/TuMhRqFvtS40ZwPsoKyC5qCeDD_jVvNeN0qS7WCy7-8.original.fullsize.png">

$$
\text { As, } \operatorname{Arg}\left(\frac{z}{\omega}\right)=\frac{\pi}{2} \text { therefore } \frac{z}{\omega}=i
$$
$\therefore\left|\frac{z}{\omega}\right|=1$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/omZ6fg5NNW1gEPTi0tsCc2HjgDIm55Br5R3waH7stuc.original.fullsize.png">

From (1) \& (2), $|z|=|\omega|=1$ and $\frac{z}{\omega}+\frac{\bar{z}}{\omega}=0 ; z \bar{\omega}+\bar{z} \omega=0$
$\bar{z} \omega=-z \bar{\omega}=\frac{-z}{\omega} \cdot \bar{\omega} \cdot \omega ; \bar{z} \omega=-i|\omega|^2=-\mathrm{i}$

</details>

---

### Q70. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

$z$ and $w$ are two non zero complex no.s such that $|z|=|w|$ and $\operatorname{Arg} z+\operatorname{Arg} w=\pi$ then $z$ equals

**Options:**

- **(A)** $\overline{\mathrm{W}}$
- **(B)** -$\overline{\mathrm{W}}$
- **(C)** $\mathrm{W}$
- **(D)** -$\mathrm{W}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -$\overline{\mathrm{W}}$**

**Detailed Solution:**

Let $|\mathrm{z}|=|\omega|=\mathrm{r} \quad \therefore \mathrm{z}=\mathrm{re}^{\mathrm{i} \theta}, \omega=\mathrm{re}^{\mathrm{i} \phi}$ where $\theta+\phi=\pi \quad \therefore \bar{\omega}=\mathrm{re}^{-\mathrm{i \phi}}$ $\therefore z=\mathrm{re}^{i(\pi-\phi)}=\mathrm{re}^{\mathrm{i} \pi} \cdot \mathrm{e}^{-i \phi}=-\mathrm{re}^{-i \phi}=-\bar{\omega}$

</details>

---

