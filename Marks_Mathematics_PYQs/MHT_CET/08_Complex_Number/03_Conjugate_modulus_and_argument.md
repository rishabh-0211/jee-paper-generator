# MHT CET Mathematics - Complex Number

## Topic 3: Conjugate, modulus and argument

**Total Questions:** 22

---

### Q1. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The modulus and argument of $(1 + i\sqrt{3})^8$ are respectively...

**Options:**

- **(A)** $2$ and $2\pi/3$
- **(B)** $256$ and $7\pi/3$
- **(C)** $256$ and $2\pi/3$
- **(D)** $64$ and $4\pi/3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $256$ and $2\pi/3$**

**Detailed Solution:**

Let $z = 1 + i\sqrt{3}$.

The modulus of $z$ is $|z| = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{4} = 2$.

The argument of $z$ is $\theta = \tan^{-1}(\sqrt{3}/1) = \pi/3$.

Writing $z$ in polar form, $z = 2(\cos(\pi/3) + i\sin(\pi/3))$.

Using De Moivre's theorem, $(1 + i\sqrt{3})^8 = (2(\cos(\pi/3) + i\sin(\pi/3)))^8$

$= 2^8(\cos(8\pi/3) + i\sin(8\pi/3))$

$= 256(\cos(2\pi + 2\pi/3) + i\sin(2\pi + 2\pi/3))$

$= 256(\cos(2\pi/3) + i\sin(2\pi/3))$

Thus, the modulus is $256$ and the principal argument is $2\pi/3$.

Answer: $256$ and $2\pi/3$

</details>

---

### Q2. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $n\in Z$, then the expression $\dfrac{2^n}{(1-i)^{2n}}+\dfrac{(1+i)^{2n}}{2^n}$ is equal to ...

**Options:**

- **(A)** $0$
- **(B)** $2$
- **(C)** $[1+(-1)^n]i^n$
- **(D)** $2i^n$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2i^n$**

**Detailed Solution:**

We first simplify the terms $(1-i)^2$ and $(1+i)^2$:

$(1-i)^2 = 1 - 2i + i^2 = 1 - 2i - 1 = -2i$

$(1+i)^2 = 1 + 2i + i^2 = 1 + 2i - 1 = 2i$

Now, substitute these into the given expression:

$\dfrac{2^n}{(1-i)^{2n}} + \dfrac{(1+i)^{2n}}{2^n} = \dfrac{2^n}{((1-i)^2)^n} + \dfrac{((1+i)^2)^n}{2^n}$

$\Rightarrow \dfrac{2^n}{(-2i)^n} + \dfrac{(2i)^n}{2^n}$

$\Rightarrow \left(\dfrac{2}{-2i}\right)^n + \left(\dfrac{2i}{2}\right)^n$

$\Rightarrow \left(\dfrac{-1}{i}\right)^n + (i)^n$

Since $\dfrac{-1}{i} = \dfrac{-1 \times i}{i \times i} = \dfrac{-i}{-1} = i$, we get:

$\Rightarrow (i)^n + (i)^n = 2i^n$

Answer: $2i^n$

</details>

---

### Q3. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $(1 + i) \cdot (1 + 2i) \ldots\ldots\ldots (1 + ni) = x + iy$ (Where $i = \sqrt{-1}$ ), then the value of $(2) \cdot (5) \cdot (10)\ldots\ldots\ldots(1 + n^2)$

**Options:**

- **(A)** $\dfrac{\sqrt{x} + \sqrt{y}}{2}$
- **(B)** $x^2 + y^2$
- **(C)** $\dfrac{\sqrt{x} + \sqrt{y}}{\sqrt{x} - \sqrt{y}}$
- **(D)** $x^2 - y^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2 + y^2$**

**Detailed Solution:**

Given $(1 + i)(1 + 2i) \dots (1 + ni) = x + iy$

Taking the conjugate on both sides:

$(1 - i)(1 - 2i) \dots (1 - ni) = x - iy$

Multiplying the two equations:

$((1 + i)(1 - i))((1 + 2i)(1 - 2i)) \dots ((1 + ni)(1 - ni)) = (x + iy)(x - iy)$

$(1^2 - i^2)(1^2 - (2i)^2) \dots (1^2 - (ni)^2) = x^2 - (iy)^2$

Since $i^2 = -1$, we get:

$(1 + 1)(1 + 4) \dots (1 + n^2) = x^2 + y^2$

$2 \cdot 5 \cdot 10 \dots (1 + n^2) = x^2 + y^2$

Answer: $x^2 + y^2$

</details>

---

### Q4. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a complex number $\mathrm{z}=\frac{4+3 i \sin \theta}{1-2 i \sin \theta}($ where $i=\sqrt{-1})$ is purely real, then the value of $\theta$ is

**Options:**

- **(A)** $n \pi, n \in \mathbb{Z}$
- **(B)** $(\mathrm{n}+1) \frac{\pi}{2}, \mathrm{n} \in \mathbb{Z}$
- **(C)** $(n-1) \frac{\pi}{2}, n \in \mathbb{Z}$
- **(D)** $(2 n+1) \frac{\pi}{4}, n \in \mathbb{Z}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $n \pi, n \in \mathbb{Z}$**

**Detailed Solution:**

Given $z = \dfrac{4+3i\sin\theta}{1-2i\sin\theta}$

Multiplying the numerator and denominator by the complex conjugate of the denominator, we get:

$z = \dfrac{(4+3i\sin\theta)(1+2i\sin\theta)}{(1-2i\sin\theta)(1+2i\sin\theta)}$

$z = \dfrac{4 + 8i\sin\theta + 3i\sin\theta + 6i^2\sin^2\theta}{1^2 - (2i\sin\theta)^2}$

Since $i^2 = -1$, this simplifies to:

$z = \dfrac{4 - 6\sin^2\theta + 11i\sin\theta}{1 + 4\sin^2\theta}$

$z = \left(\dfrac{4 - 6\sin^2\theta}{1 + 4\sin^2\theta}\right) + i\left(\dfrac{11\sin\theta}{1 + 4\sin^2\theta}\right)$

For the complex number $z$ to be purely real, its imaginary part must be zero.

$\dfrac{11\sin\theta}{1 + 4\sin^2\theta} = 0$

$11\sin\theta = 0$

$\sin\theta = 0$

The general solution for $\sin\theta = 0$ is:

$\theta = n\pi, n \in \mathbb{Z}$

Answer: $n \pi, n \in \mathbb{Z}$

</details>

---

### Q5. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let z be the complex number such that $|\mathrm{z}|+\mathrm{z}=3+\mathrm{i}$ where $i=\sqrt{-1}$, then $|\mathrm{z}|=$

**Options:**

- **(A)** $\frac{\sqrt{34}}{3}$
- **(B)** $\frac{5}{3}$
- **(C)** $\frac{\sqrt{41}}{4}$
- **(D)** $\frac{5}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5}{3}$**

**Detailed Solution:**

Let $z = x + iy$, where $x, y \in \mathbb{R}$.

Given $|z| + z = 3 + i$

$\sqrt{x^2 + y^2} + x + iy = 3 + i$

Equating the real and imaginary parts, we get:

$\sqrt{x^2 + y^2} + x = 3$

$y = 1$

Substituting $y = 1$ in the first equation:

$\sqrt{x^2 + 1} = 3 - x$

Squaring both sides:

$x^2 + 1 = (3 - x)^2$

$x^2 + 1 = 9 - 6x + x^2$

$6x = 8 \Rightarrow x = \dfrac{4}{3}$

Now, $|z| = \sqrt{x^2 + y^2} = \sqrt{\left(\dfrac{4}{3}\right)^2 + 1^2}$

$|z| = \sqrt{\dfrac{16}{9} + 1} = \sqrt{\dfrac{25}{9}} = \dfrac{5}{3}$

Answer: $\frac{5}{3}$

</details>

---

### Q6. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Argument of the complex number $\mathrm{z}=\frac{13-5 \mathrm{i}}{4-9 \mathrm{i}}, i=\sqrt{-1}$ is

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{\pi}{6}$
- **(D)** $\frac{\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}$**

**Detailed Solution:**

$z = \dfrac{13 - 5i}{4 - 9i}$

Multiplying the numerator and the denominator by the conjugate of the denominator, $4 + 9i$:

$z = \dfrac{(13 - 5i)(4 + 9i)}{(4 - 9i)(4 + 9i)}$

$z = \dfrac{52 + 117i - 20i - 45i^2}{4^2 - (9i)^2}$

Substituting $i^2 = -1$:

$z = \dfrac{52 + 45 + 97i}{16 + 81}$

$z = \dfrac{97 + 97i}{97}$

$z = 1 + i$

The argument of a complex number $z = x + iy$ in the first quadrant is given by $\theta = \tan^{-1}\left(\dfrac{y}{x}\right)$.

$\theta = \tan^{-1}\left(\dfrac{1}{1}\right) = \dfrac{\pi}{4}$

Answer: $\frac{\pi}{4}$

</details>

---

### Q7. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\mathrm{z}=\frac{3+2 i \sin \theta}{1-2 i \sin \theta}, \quad(i=\sqrt{-1})$ will be purely imaginary if $\theta=$

**Options:**

- **(A)** $2 n \pi \pm \frac{\pi}{8}$, where $n \in \mathbb{Z}$
- **(B)** $\mathrm{n} \pi+\frac{\pi}{8}$, where $\mathrm{n} \in \mathbb{Z}$
- **(C)** $n \pi \pm \frac{\pi}{3}$, where $n \in \mathbb{Z}$
- **(D)** $n \pi$, where $n \in \mathbb{Z}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $n \pi \pm \frac{\pi}{3}$, where $n \in \mathbb{Z}$**

**Detailed Solution:**

Given $z = \dfrac{3+2 i \sin \theta}{1-2 i \sin \theta}$

Multiplying the numerator and denominator by the conjugate of the denominator, we get:

$z = \dfrac{(3+2 i \sin \theta)(1+2 i \sin \theta)}{(1-2 i \sin \theta)(1+2 i \sin \theta)}$

$z = \dfrac{3 + 6 i \sin \theta + 2 i \sin \theta + 4 i^2 \sin^2 \theta}{1^2 - (2 i \sin \theta)^2}$

Since $i^2 = -1$, this simplifies to:

$z = \dfrac{3 - 4 \sin^2 \theta + 8 i \sin \theta}{1 + 4 \sin^2 \theta}$

For $z$ to be purely imaginary, its real part must be zero:

$\dfrac{3 - 4 \sin^2 \theta}{1 + 4 \sin^2 \theta} = 0$

$3 - 4 \sin^2 \theta = 0$

$\sin^2 \theta = \dfrac{3}{4}$

$\sin^2 \theta = \left(\dfrac{\sqrt{3}}{2}\right)^2$

$\sin^2 \theta = \sin^2 \left(\dfrac{\pi}{3}\right)$

The general solution for $\sin^2 \theta = \sin^2 \alpha$ is $\theta = n \pi \pm \alpha$, where $n \in \mathbb{Z}$.

Therefore, $\theta = n \pi \pm \dfrac{\pi}{3}$, where $n \in \mathbb{Z}$.

Answer: $n \pi \pm \frac{\pi}{3}$, where $n \in \mathbb{Z}$

</details>

---

### Q8. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The complex numbers $\sin x+i \cos 2 x$ and $\cos x-i \sin 2 x,(i=\sqrt{-1})$ are conjugate to each other for,

**Options:**

- **(A)** $x=\mathrm{n} \pi, \mathrm{n} \in \mathbb{Z}$
- **(B)** $x=\left(\mathrm{n}+\frac{1}{2}\right) \pi, \mathrm{n} \in \mathbb{Z}$
- **(C)** $\mathrm{x}=(3 \mathrm{n}-1) \pi, \mathrm{n} \in \mathbb{Z}$
- **(D)** No value of $x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) No value of $x$**

**Detailed Solution:**

Let $z_1 = \sin x + i \cos 2x$ and $z_2 = \cos x - i \sin 2x$.

Since $z_1$ and $z_2$ are conjugate to each other, we have $z_1 = \overline{z_2}$.

$\sin x + i \cos 2x = \overline{\cos x - i \sin 2x}$

$\sin x + i \cos 2x = \cos x + i \sin 2x$

Equating the real and imaginary parts, we get:

$\sin x = \cos x$

$\cos 2x = \sin 2x$

From the first equation, $\tan x = 1$, which gives $x = n\pi + \dfrac{\pi}{4}$, where $n \in \mathbb{Z}$.

For these values of $x$, $2x = 2n\pi + \dfrac{\pi}{2}$.

Substituting this into the second equation, we get:

$\cos\left(2n\pi + \dfrac{\pi}{2}\right) = \sin\left(2n\pi + \dfrac{\pi}{2}\right)$

$0 = 1$

This is a contradiction. Thus, there is no value of $x$ that satisfies both equations simultaneously.

Answer: No value of $x$

</details>

---

### Q9. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The modulus of the square root of the conjugate of $-7+24 \sqrt{-1}$ is ....

**Options:**

- **(A)** $3$
- **(B)** $4$
- **(C)** $16$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5$**

**Detailed Solution:**

Let $z = -7 + 24i$.

The conjugate of $z$ is $\bar{z} = -7 - 24i$.

We need to find $\left| \sqrt{\bar{z}} \right|$.

Using the property of modulus, $\left| \sqrt{\bar{z}} \right| = \sqrt{|\bar{z}|}$.

Now, $|\bar{z}| = \sqrt{(-7)^2 + (-24)^2} = \sqrt{49 + 576} = \sqrt{625} = 25$.

Therefore, $\left| \sqrt{\bar{z}} \right| = \sqrt{25} = 5$.

Answer: $5$

</details>

---

### Q10. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $z_1=5-2 i$ and $z_2=3+i$, where $i=\sqrt{-1}$, then $\arg \left(\frac{z_1+z_2}{z_1-z_2}\right)$ is

**Options:**

- **(A)** $\tan ^{-1}\left(\frac{22}{19}\right)$
- **(B)** $\tan ^{-1}\left(\frac{22}{13}\right)$
- **(C)** $\tan ^{-1}\left(\frac{21}{19}\right)$
- **(D)** $\tan ^{-1}\left(\frac{19}{22}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan ^{-1}\left(\frac{22}{19}\right)$**

**Detailed Solution:**

Given $z_1 = 5 - 2i$ and $z_2 = 3 + i$.

$z_1 + z_2 = (5 - 2i) + (3 + i) = 8 - i$

$z_1 - z_2 = (5 - 2i) - (3 + i) = 2 - 3i$

Now, $\dfrac{z_1 + z_2}{z_1 - z_2} = \dfrac{8 - i}{2 - 3i}$

Multiply the numerator and the denominator by the complex conjugate of the denominator:

$\dfrac{8 - i}{2 - 3i} = \dfrac{(8 - i)(2 + 3i)}{(2 - 3i)(2 + 3i)}$

$= \dfrac{16 + 24i - 2i - 3i^2}{2^2 + 3^2}$

$= \dfrac{16 + 22i + 3}{4 + 9}$

$= \dfrac{19 + 22i}{13} = \dfrac{19}{13} + i\dfrac{22}{13}$

The argument of a complex number $x + iy$ in the first quadrant ($x > 0, y > 0$) is $\tan^{-1}\left(\dfrac{y}{x}\right)$.

$\arg\left(\dfrac{z_1 + z_2}{z_1 - z_2}\right) = \tan^{-1}\left(\dfrac{22/13}{19/13}\right) = \tan^{-1}\left(\dfrac{22}{19}\right)$

Answer: $\tan ^{-1}\left(\frac{22}{19}\right)$

</details>

---

### Q11. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $z$ be a complex number such that $|z|+z=2+i$, where $i=\sqrt{-1}$, then $|z|$ is equal to

**Options:**

- **(A)** $\frac{4}{5}$
- **(B)** $\frac{5}{4}$
- **(C)** $\frac{5}{3}$
- **(D)** $\frac{\sqrt{41}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5}{4}$**

**Detailed Solution:**

Let $z = x + iy$, where $x, y \in \mathbb{R}$.

Given $|z| + z = 2 + i$

$\sqrt{x^2 + y^2} + x + iy = 2 + i$

Equating real and imaginary parts, we get:

$\sqrt{x^2 + y^2} + x = 2$

$y = 1$

Substituting $y = 1$ in the first equation:

$\sqrt{x^2 + 1} = 2 - x$

Squaring both sides:

$x^2 + 1 = (2 - x)^2$

$x^2 + 1 = 4 - 4x + x^2$

$4x = 3 \Rightarrow x = \dfrac{3}{4}$

Now, $|z| = \sqrt{x^2 + y^2} = \sqrt{\left(\dfrac{3}{4}\right)^2 + 1^2} = \sqrt{\dfrac{9}{16} + 1} = \sqrt{\dfrac{25}{16}} = \dfrac{5}{4}$

Answer: $\frac{5}{4}$

</details>

---

### Q12. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $Z$ be a complex number such that $|Z|+Z=2+i($ where $i=\sqrt{-1})$, then $|Z|$ is equal to

**Options:**

- **(A)** $\frac{4}{5}$
- **(B)** $\frac{\sqrt{41}}{4}$
- **(C)** $\frac{5}{3}$
- **(D)** $\frac{5}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{5}{4}$**

**Detailed Solution:**

Let $Z = x + iy$, where $x, y \in \mathbb{R}$.

Given $|Z| + Z = 2 + i$

$\sqrt{x^2 + y^2} + x + iy = 2 + i$

Equating real and imaginary parts, we get:

$\sqrt{x^2 + y^2} + x = 2$

$y = 1$

Substituting $y = 1$ into the first equation:

$\sqrt{x^2 + 1} + x = 2$

$\sqrt{x^2 + 1} = 2 - x$

Squaring both sides:

$x^2 + 1 = (2 - x)^2$

$x^2 + 1 = 4 - 4x + x^2$

$4x = 3 \Rightarrow x = \dfrac{3}{4}$

Now, $|Z| = \sqrt{x^2 + y^2} = \sqrt{\left(\dfrac{3}{4}\right)^2 + 1^2} = \sqrt{\dfrac{9}{16} + 1} = \sqrt{\dfrac{25}{16}} = \dfrac{5}{4}$

Answer: $\frac{5}{4}$

</details>

---

### Q13. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $z =\dfrac{-2}{1+\sqrt{3} i}, i=\sqrt{-1}$, then the value of $\arg Z$ is

**Options:**

- **(A)** $\dfrac{2 \pi}{3}$
- **(B)** $\dfrac{\pi}{3}$
- **(C)** $-\dfrac{\pi}{3}$
- **(D)** $\dfrac{4 \pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2 \pi}{3}$**

**Detailed Solution:**

Given $z = \dfrac{-2}{1+\sqrt{3} i}$

Multiplying the numerator and the denominator by the conjugate of the denominator, we get:

$z = \dfrac{-2(1-\sqrt{3} i)}{(1+\sqrt{3} i)(1-\sqrt{3} i)}$

$z = \dfrac{-2(1-\sqrt{3} i)}{1^2 - (\sqrt{3} i)^2}$

$z = \dfrac{-2(1-\sqrt{3} i)}{1 - 3(-1)}$

$z = \dfrac{-2(1-\sqrt{3} i)}{4}$

$z = -\dfrac{1}{2} + \dfrac{\sqrt{3}}{2} i$

The real part is $-\dfrac{1}{2}$ and the imaginary part is $\dfrac{\sqrt{3}}{2}$. Since the real part is negative and the imaginary part is positive, the complex number lies in the second quadrant.

The argument of $z$ is given by:

$\arg(z) = \pi - \tan^{-1}\left(\left|\dfrac{\text{Im}(z)}{\text{Re}(z)}\right|\right)$

$\arg(z) = \pi - \tan^{-1}\left(\left|\dfrac{\sqrt{3}/2}{-1/2}\right|\right)$

$\arg(z) = \pi - \tan^{-1}(\sqrt{3})$

$\arg(z) = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$

Answer: $\dfrac{2 \pi}{3}$

</details>

---

### Q14. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $|z|=1$ and $w=\dfrac{z-1}{z+1}$ (where $z \neq-1$ ), then $\operatorname{Re}(\mathrm{w})$ is

**Options:**

- **(A)** 0
- **(B)** $\quad-\dfrac{1}{|z+1|^2}$
- **(C)** $\left|\dfrac{z}{z+1}\right| \cdot \dfrac{1}{|z+1|^2}$
- **(D)** $\dfrac{\sqrt{2}}{|z+1|^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Given $|z| = 1$, which implies $z \overline{z} = 1$, so $\overline{z} = \dfrac{1}{z}$.

We have $w = \dfrac{z-1}{z+1}$.

Taking the conjugate of $w$:

$\overline{w} = \dfrac{\overline{z}-1}{\overline{z}+1}$

Substituting $\overline{z} = \dfrac{1}{z}$:

$\overline{w} = \dfrac{\dfrac{1}{z}-1}{\dfrac{1}{z}+1} = \dfrac{1-z}{1+z} = -\left(\dfrac{z-1}{z+1}\right) = -w$

Since $\overline{w} = -w$, the complex number $w$ is purely imaginary.

Therefore, $\operatorname{Re}(w) = 0$.

Answer: 0

</details>

---

### Q15. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{a}\gt0$ and $\mathrm{z}=\dfrac{(1+\mathrm{i})^2}{\mathrm{a}-\mathrm{i}}, \mathrm{i}=\sqrt{-1}$, has magnitude $\sqrt{\dfrac{2}{5}}$, then $\overline{\mathrm{z}}$ is equal to

**Options:**

- **(A)** $\dfrac{1}{5}-\dfrac{3}{5} \mathrm{i}$
- **(B)** $-\dfrac{1}{5}-\dfrac{3}{5} \mathrm{i}$
- **(C)** $-\dfrac{1}{5}+\dfrac{3}{5} \mathrm{i}$
- **(D)** $\quad-\dfrac{3}{5}-\dfrac{1}{5} \mathrm{i}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\dfrac{1}{5}-\dfrac{3}{5} \mathrm{i}$**

**Detailed Solution:**

Given $z = \dfrac{(1+\mathrm{i})^2}{\mathrm{a}-\mathrm{i}}$

$z = \dfrac{1 + \mathrm{i}^2 + 2\mathrm{i}}{\mathrm{a}-\mathrm{i}} = \dfrac{2\mathrm{i}}{\mathrm{a}-\mathrm{i}}$

$|z| = \left| \dfrac{2\mathrm{i}}{\mathrm{a}-\mathrm{i}} \right| = \dfrac{2}{\sqrt{\mathrm{a}^2+1}}$

Given $|z| = \sqrt{\dfrac{2}{5}}$

$\dfrac{2}{\sqrt{\mathrm{a}^2+1}} = \sqrt{\dfrac{2}{5}}$

Squaring both sides:

$\dfrac{4}{\mathrm{a}^2+1} = \dfrac{2}{5}$

$20 = 2(\mathrm{a}^2+1)$

$\mathrm{a}^2+1 = 10 \Rightarrow \mathrm{a}^2 = 9$

Since $\mathrm{a} > 0$, $\mathrm{a} = 3$

Substituting $\mathrm{a} = 3$ in $z$:

$z = \dfrac{2\mathrm{i}}{3-\mathrm{i}} = \dfrac{2\mathrm{i}(3+\mathrm{i})}{(3-\mathrm{i})(3+\mathrm{i})} = \dfrac{6\mathrm{i}-2}{10} = -\dfrac{1}{5} + \dfrac{3}{5}\mathrm{i}$

Therefore, $\overline{\mathrm{z}} = -\dfrac{1}{5} - \dfrac{3}{5}\mathrm{i}$

Answer: $-\dfrac{1}{5}-\dfrac{3}{5} \mathrm{i}$

</details>

---

### Q16. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{a}>0$ and $\mathrm{z}=\frac{(1+\mathrm{i})^2}{\mathrm{a}-\mathrm{i}}, \mathrm{i}=\sqrt{-1}$, has magnitude $\frac{2}{\sqrt{5}}$, then $\bar{z}$ is

**Options:**

- **(A)** $-\frac{2}{5}-\frac{4}{5} \mathrm{i}$
- **(B)** $-\frac{2}{5}+\frac{4}{5} i$
- **(C)** $\frac{2}{5}-\frac{4}{5} \mathrm{i}$
- **(D)** $\frac{2}{5}+\frac{4}{5} \mathrm{i}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\frac{2}{5}-\frac{4}{5} \mathrm{i}$**

**Detailed Solution:**

$\begin{aligned} z & =\frac{(1+i)^2}{a-i} \\ & =\frac{2 i}{a-i}=\frac{2 i(a+i)}{a^2+1} \\ \therefore \quad|z| & =\sqrt{\frac{-2+2 a i}{a^2+1}} \\ \Rightarrow & \frac{2}{\sqrt{5}}=\frac{2 a^2}{\sqrt{a^2+1}}\end{aligned}$
$\Rightarrow \mathrm{a}=2 \quad \ldots[\because \mathrm{a}>0]$
$\begin{aligned} \therefore \quad z & =\frac{-2+4 i}{5}=\frac{-2}{5}+\frac{4}{5} i \\ & \Rightarrow \bar{z}=-\frac{2}{5}-\frac{4}{5} \mathrm{i}\end{aligned}$

</details>

---

### Q17. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $(3 x+2)-(5 y-3) \mathrm{i}$ and $(6 x+3)+(2 y-4) \mathrm{i}$ are conjugates of each other, then the value of $\frac{x-y}{x+y}$ is (where $\mathrm{i}=\sqrt{-1}, x, y \in \mathrm{R}$ )

**Options:**

- **(A)** $-1$
- **(B)** 0
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

$(3 x+2)-(5 y-3) \mathrm{i}$ and $(6 x+3)+(2 y-4) \mathrm{i}$ are conjugates of each other.
$\Rightarrow 3 x+2=6 x+3$ and $5 y-3=2 y-4$
$\Rightarrow 3 x=-1$ and $3 y=-1$
$\Rightarrow x=-\frac{1}{3}$ and $y=-\frac{1}{3}$
$\therefore \quad \frac{x-y}{x+y}=0$

</details>

---

### Q18. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The argument of $\frac{1+i \sqrt{3}}{\sqrt{3}+i}, i=\sqrt{-1}$ is

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{6}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{6}$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } z=\frac{1+i \sqrt{3}}{\sqrt{3}+i} \\ = & \frac{(1+i \sqrt{3})(\sqrt{3}-i)}{(\sqrt{3}+i)(\sqrt{3}-i)} \\ \therefore \quad z & =\frac{\sqrt{3}}{2}+\frac{1}{2} i\end{aligned}$
Argument of
$\begin{aligned}
z & =\tan ^{-1}\left(\frac{b}{a}\right) \\
& =\tan ^{-1}\left(\frac{\frac{1}{2}}{\frac{\sqrt{3}}{2}}\right) \\
& =\tan ^{-1}\left(\frac{1}{\sqrt{3}}\right) \\
& =\frac{\pi}{6}
\end{aligned}$

</details>

---

### Q19. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $Z_1=2+i$ and $Z_2=3-4 i$ and $\frac{\overline{Z_1}}{Z_1}=a+b i$, then the value of $-7 a+b$ is (where $i=\sqrt{-1}$ and $\mathrm{a}, \mathrm{b} \in \mathbb{R})$

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** $\frac{-3}{25}$
- **(D)** $\frac{-9}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -1**

**Detailed Solution:**

$\begin{aligned} & \mathrm{Z}_1=2+\mathrm{i} \quad \mathrm{Z}_2=3-4 \mathrm{i} \\ & \overline{Z_1}=2-\mathrm{i} \quad \overline{Z_2}=3+4 \mathrm{i} \\ & \frac{\overline{Z_1}}{\overline{Z_2}}=\frac{2-\mathrm{i}}{3+4 \mathrm{i}} \\ & =\frac{(2-i)(3-4 i)}{(3+4 i)(3-4 i)} \\ & =\frac{6-8 i-3 i+4 i^2}{(3)^2-(4 i)^2} \\ & =\frac{6-1 \mathrm{li}-4}{9+16} \quad \ldots\left[\mathrm{i}^2=-1\right] \\ & \mathrm{a}+\mathrm{bi}=\frac{2-1 \mathrm{li}}{25} \\ & \therefore \quad a=\frac{2}{25}, b=\frac{-11}{25} \\ & \end{aligned}$
$\begin{aligned} & \text { Now }-7 \mathrm{a}+\mathrm{b} \\ & =-7\left(\frac{2}{25}\right)-\frac{11}{25} \\ & =\frac{-14-11}{25} \\ & =\frac{-25}{25}=-1\end{aligned}$

</details>

---

### Q20. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Argument of $\frac{1-i \sqrt{3}}{1+i \sqrt{3}}$ is

**Options:**

- **(A)** $210^{\circ}$
- **(B)** $120^{\circ}$
- **(C)** $240^{\circ}$
- **(D)** $60^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $240^{\circ}$**

**Detailed Solution:**

$z=\frac{1-i \sqrt{3}}{1+i \sqrt{3}} \times \frac{1-i \sqrt{3}}{1-i \sqrt{3}}=\frac{-2-2 \sqrt{3} i}{4}=-\frac{1}{2}-\frac{1}{2} \sqrt{3} i$
$\begin{aligned} & \text { Now Arg }(Z)=\pi+\tan ^{-1}\left|\frac{\operatorname{Im}(Z)}{\operatorname{Re}(Z)}\right| \\ & =180^{\circ}+\tan ^{-1}(\sqrt{3})=180^{\circ}+60^{\circ}=240^{\circ}\end{aligned}$

</details>

---

### Q21. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\arg (\mathrm{z})<0$, then $\arg (-\mathrm{z})-\arg (\mathrm{z})$ equals

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $-\frac{\pi}{2}$
- **(C)** $\pi$
- **(D)** $-\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\pi$**

**Detailed Solution:**

$\begin{aligned} & \arg (-\mathrm{z})-\arg (\mathrm{z}) \\ & =\arg (-1 \times \mathrm{z})-\arg (\mathrm{z}) \\ & =\arg (-1)+\arg (\mathrm{z})-\arg (\mathrm{z}) \\ & =\pi\end{aligned}$

</details>

---

### Q22. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The complex number with argument $\frac{5 \pi^c}{6}$ at a distance of 2 units from the origin is

**Options:**

- **(A)** $\sqrt{3}-\mathrm{i}$
- **(B)** $\sqrt{3}+\mathrm{i}$
- **(C)** $-\sqrt{3}-\mathrm{i}$
- **(D)** $-\sqrt{3}+\mathrm{i}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\sqrt{3}+\mathrm{i}$**

**Detailed Solution:**

Let $\mathrm{z}=\mathrm{a}+\mathrm{ib}$ and we have
$\frac{\mathrm{b}}{\mathrm{a}}=\tan \left(\frac{5 \pi}{6}\right)$ and $\sqrt{\mathrm{a}^2+\mathrm{b}^2}=2$
$\therefore \frac{\mathrm{b}}{\mathrm{a}}=\tan \left(\pi-\frac{\pi}{6}\right)=-\tan \frac{\pi}{6}=\frac{-1}{\sqrt{3}}$ and $\mathrm{a}^2+\mathrm{b}^2=4$
$\therefore \mathrm{b}=\frac{-\mathrm{a}}{\sqrt{3}}$ and $\mathrm{a}^2+\mathrm{b}^2+4$
$\therefore \mathrm{a}^2+\frac{\mathrm{a}^2}{3}=4 \Rightarrow 4 \mathrm{a}^2=12 \Rightarrow \mathrm{a}^2=3 \Rightarrow \mathrm{a}= \pm \sqrt{3}$
Also $\mathrm{b}=\frac{-\mathrm{a}}{\sqrt{3}}=\frac{ \pm \sqrt{3}}{\sqrt{3}}= \pm 1$
Since complex number lies in $2^{\text {nd }}$ quadrant, $\mathrm{a}=-\sqrt{3}$ and $\mathrm{b}=1 \Rightarrow \mathrm{z}=-\sqrt{3}+\mathrm{i}$

</details>

---

