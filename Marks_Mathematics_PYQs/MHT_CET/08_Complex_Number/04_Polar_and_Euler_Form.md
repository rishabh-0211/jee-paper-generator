# MHT CET Mathematics - Complex Number

## Topic 4: Polar and Euler Form

**Total Questions:** 6

---

### Q1. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $n \in Z$, then the value of $\dfrac{2^n}{(1+i)^{2n}} + \dfrac{2^n}{(1-i)^{2n}} + \dfrac{(1+i)^{2n} + (1-i)^{2n}}{2^n}$ is equal to

**Options:**

- **(A)** $4\cos\left(\dfrac{n\pi}{2}\right)$
- **(B)** $2(n+1)\cos\left(\dfrac{n\pi}{2}\right)$
- **(C)** $2[1 + (-1)^n]$
- **(D)** $2(n+2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4\cos\left(\dfrac{n\pi}{2}\right)$**

**Detailed Solution:**

We know that $(1+i)^2 = 1 + i^2 + 2i = 2i$ and $(1-i)^2 = 1 + i^2 - 2i = -2i$.

Raising both to the power of $n$, we get:
$(1+i)^{2n} = (2i)^n = 2^n i^n$
$(1-i)^{2n} = (-2i)^n = 2^n (-i)^n$

Substituting these into the given expression:
$\dfrac{2^n}{2^n i^n} + \dfrac{2^n}{2^n (-i)^n} + \dfrac{2^n i^n + 2^n (-i)^n}{2^n}$

$= \dfrac{1}{i^n} + \dfrac{1}{(-i)^n} + i^n + (-i)^n$

Since $\dfrac{1}{i} = -i$ and $\dfrac{1}{-i} = i$, the expression simplifies to:
$(-i)^n + i^n + i^n + (-i)^n = 2(i^n + (-i)^n)$

Using De Moivre's theorem:
$i^n = \left(\cos\dfrac{\pi}{2} + i\sin\dfrac{\pi}{2}\right)^n = \cos\dfrac{n\pi}{2} + i\sin\dfrac{n\pi}{2}$
$(-i)^n = \left(\cos\left(-\dfrac{\pi}{2}\right) + i\sin\left(-\dfrac{\pi}{2}\right)\right)^n = \cos\dfrac{n\pi}{2} - i\sin\dfrac{n\pi}{2}$

Adding these gives:
$i^n + (-i)^n = 2\cos\dfrac{n\pi}{2}$

Therefore, the value of the given expression is:
$2 \times 2\cos\dfrac{n\pi}{2} = 4\cos\dfrac{n\pi}{2}$

Answer: $4\cos\left(\dfrac{n\pi}{2}\right)$

</details>

---

### Q2. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $z_1 = 3 \cdot e^{\dfrac{5\pi}{12}i}$ and $z_2 = 4 \cdot e^{\dfrac{\pi}{12}i}$ then $z_1 \cdot z_2 = \cdots\cdots$

**Options:**

- **(A)** $12$
- **(B)** $12i$
- **(C)** $e^{\dfrac{\pi}{2}i}$
- **(D)** $e^{\dfrac{\pi}{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $12i$**

**Detailed Solution:**

Given $z_1 = 3 \cdot e^{\dfrac{5\pi}{12}i}$ and $z_2 = 4 \cdot e^{\dfrac{\pi}{12}i}$

$z_1 \cdot z_2 = \left(3 \cdot e^{\dfrac{5\pi}{12}i}\right) \cdot \left(4 \cdot e^{\dfrac{\pi}{12}i}\right)$

$z_1 \cdot z_2 = 12 \cdot e^{\left(\dfrac{5\pi}{12} + \dfrac{\pi}{12}\right)i}$

$z_1 \cdot z_2 = 12 \cdot e^{\dfrac{6\pi}{12}i} = 12 \cdot e^{\dfrac{\pi}{2}i}$

Using Euler's formula, $e^{\dfrac{\pi}{2}i} = \cos\left(\dfrac{\pi}{2}\right) + i\sin\left(\dfrac{\pi}{2}\right) = i$

$z_1 \cdot z_2 = 12i$

Answer: $12i$

</details>

---

### Q3. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $z = \dfrac{\sqrt{3} + i}{2}$, then the value of $z^{69}$ is

**Options:**

- **(A)** $-i$
- **(B)** $i$
- **(C)** $-1$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-i$**

**Detailed Solution:**

Given $z = \dfrac{\sqrt{3} + i}{2}$

Expressing $z$ in polar form:

$z = \cos\left(\dfrac{\pi}{6}\right) + i\sin\left(\dfrac{\pi}{6}\right) = e^{i\pi/6}$

Using De Moivre's theorem to find $z^{69}$:

$z^{69} = \left(e^{i\pi/6}\right)^{69} = e^{i 69\pi/6} = e^{i 23\pi/2}$

Expanding using Euler's formula:

$z^{69} = \cos\left(\dfrac{23\pi}{2}\right) + i\sin\left(\dfrac{23\pi}{2}\right)$

Since $\dfrac{23\pi}{2} = 10\pi + \dfrac{3\pi}{2}$:

$z^{69} = \cos\left(10\pi + \dfrac{3\pi}{2}\right) + i\sin\left(10\pi + \dfrac{3\pi}{2}\right)$

$z^{69} = \cos\left(\dfrac{3\pi}{2}\right) + i\sin\left(\dfrac{3\pi}{2}\right)$

$z^{69} = 0 + i(-1) = -i$

Answer: $-i$

</details>

---

### Q4. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $-1 + \sqrt{-3} = r e^{i\theta}$, then the value of $\theta$ is

**Options:**

- **(A)** $-\dfrac{2\pi}{3}$
- **(B)** $\dfrac{\pi}{3}$
- **(C)** $-\dfrac{\pi}{3}$
- **(D)** $\dfrac{2\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{2\pi}{3}$**

**Detailed Solution:**

Given complex number is $z = -1 + \sqrt{-3} = -1 + i\sqrt{3}$.

Let $z = r e^{i\theta}$, where $r = |z|$ and $\theta = \arg(z)$.

The real part $x = -1$ and the imaginary part $y = \sqrt{3}$.

Since $x < 0$ and $y > 0$, the complex number lies in the second quadrant.

The principal argument $\theta$ is given by $\pi - \tan^{-1}\left(\left|\dfrac{y}{x}\right|\right)$.

$\theta = \pi - \tan^{-1}(\sqrt{3}) = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$.

Answer: $\dfrac{2\pi}{3}$

</details>

---

### Q5. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The Cartesian form of complex number $z=4\left(\cos 300^{\circ}\right)$, where $i=\sqrt{1}$ is

**Options:**

- **(A)** $2-2 \sqrt{3} i$
- **(B)** $1+\sqrt{3} i$
- **(C)** $1-\sqrt{3} i$
- **(D)** $2+2 \sqrt{3} i$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2-2 \sqrt{3} i$**

**Detailed Solution:**

$4\left(\cos 300^{\circ}+i \sin 300^{\circ}\right)=4\left(\frac{1}{2}-\frac{\sqrt{3}}{2} i\right)=2-2 \sqrt{3} i$

</details>

---

### Q6. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The polar co-ordinates of the point, whose Cartesian co-ordinates are $(-2 \sqrt{3}, 2)$, are

**Options:**

- **(A)** $\left(4,\left(\frac{11 \pi}{12}\right)\right)$
- **(B)** $\left(4,\left(\frac{5 \pi}{6}\right)\right)$
- **(C)** $\left(4,\left(\frac{3 \pi}{4}\right)\right)$
- **(D)** $\left(4,\left(\frac{2 \pi}{3}\right)\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(4,\left(\frac{5 \pi}{6}\right)\right)$**

**Detailed Solution:**

$\begin{aligned} & x=-2 \sqrt{3} \text { and } y=2 \\ & r=\sqrt{x^2+y^2}=\sqrt{12+4}=4 \\ & \theta=\pi-\tan ^{-1}\left|\frac{2}{-2 \sqrt{3}}\right|=\pi-\tan ^{-1} \frac{1}{\sqrt{3}}=\pi-\frac{\pi}{6}=\frac{5 \pi}{6}\end{aligned}$

</details>

---

