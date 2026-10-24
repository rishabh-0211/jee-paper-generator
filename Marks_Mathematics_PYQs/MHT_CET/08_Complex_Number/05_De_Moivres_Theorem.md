# MHT CET Mathematics - Complex Number

## Topic 5: De Moivres Theorem

**Total Questions:** 6

---

### Q1. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The smallest positive integer $n$ for which $\dfrac{(1 + i)^n}{(1 - i)^{n-2}}$ is a real number, is ...

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

The given expression is $\dfrac{(1 + i)^n}{(1 - i)^{n-2}}$.

This can be rewritten as $\left(\dfrac{1 + i}{1 - i}\right)^n (1 - i)^2$.

Simplifying the term inside the bracket:

$\dfrac{1 + i}{1 - i} = \dfrac{(1 + i)^2}{(1 - i)(1 + i)} = \dfrac{1 + i^2 + 2i}{1^2 - i^2} = \dfrac{2i}{2} = i$

Simplifying the second term:

$(1 - i)^2 = 1 + i^2 - 2i = -2i$

Substituting these back into the expression, we get:

$i^n (-2i) = -2 i^{n+1}$

For this expression to be a real number, $i^{n+1}$ must be a real number. This is possible only when the exponent $n+1$ is an even integer.

$n + 1 = 2k$, where $k$ is an integer.

$n = 2k - 1$

To find the smallest positive integer $n$, substitute $k = 1$:

$n = 2(1) - 1 = 1$

Answer: $1$

</details>

---

### Q2. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\dfrac{(\cos 2\theta + i\sin 2\theta)^7}{(\cos 4\theta + i\sin 4\theta)^3} =$

**Options:**

- **(A)** $\cos 2\theta + i\sin 2\theta$
- **(B)** $(\cos 2\theta + i\sin 2\theta)^4$
- **(C)** $\cos 4\theta + i\sin 4\theta$
- **(D)** $(\cos 4\theta + i\sin 4\theta)^{-2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\cos 2\theta + i\sin 2\theta$**

**Detailed Solution:**

Using De Moivre's theorem, $(\cos \theta + i\sin \theta)^n = \cos n\theta + i\sin n\theta$.

The numerator is $(\cos 2\theta + i\sin 2\theta)^7 = \cos 14\theta + i\sin 14\theta$.

The denominator is $(\cos 4\theta + i\sin 4\theta)^3 = \cos 12\theta + i\sin 12\theta$.

The given expression becomes $\dfrac{\cos 14\theta + i\sin 14\theta}{\cos 12\theta + i\sin 12\theta}$.

Using the property $\dfrac{\cos \alpha + i\sin \alpha}{\cos \beta + i\sin \beta} = \cos(\alpha - \beta) + i\sin(\alpha - \beta)$, we get:

$\cos(14\theta - 12\theta) + i\sin(14\theta - 12\theta) = \cos 2\theta + i\sin 2\theta$.

Answer: $\cos 2\theta + i\sin 2\theta$

</details>

---

### Q3. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $n$ is a positive integer, then $(1 + i\sqrt{3})^{2n} + (1 - i\sqrt{3})^{2n}$ is equal to .........

**Options:**

- **(A)** $2^{2n+1}\cos\left(\dfrac{2n\pi}{3}\right)$
- **(B)** $2^{2n}\cos\left(\dfrac{n\pi}{3}\right)$
- **(C)** $2^{2n+1}\cos\left(\dfrac{n\pi}{3}\right)$
- **(D)** $2^n\cos\left(\dfrac{2n\pi}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2^{2n+1}\cos\left(\dfrac{2n\pi}{3}\right)$**

**Detailed Solution:**

Let $z = 1 + i\sqrt{3}$.

Converting to polar form, we have $r = \sqrt{1^2 + (\sqrt{3})^2} = 2$ and $\theta = \tan^{-1}(\sqrt{3}) = \dfrac{\pi}{3}$.

Thus, $1 + i\sqrt{3} = 2\left(\cos\dfrac{\pi}{3} + i\sin\dfrac{\pi}{3}\right)$.

Similarly, $1 - i\sqrt{3} = 2\left(\cos\dfrac{\pi}{3} - i\sin\dfrac{\pi}{3}\right)$.

Using De Moivre's theorem, we get:

$(1 + i\sqrt{3})^{2n} = 2^{2n}\left(\cos\dfrac{2n\pi}{3} + i\sin\dfrac{2n\pi}{3}\right)$

$(1 - i\sqrt{3})^{2n} = 2^{2n}\left(\cos\dfrac{2n\pi}{3} - i\sin\dfrac{2n\pi}{3}\right)$

Adding the two expressions:

$(1 + i\sqrt{3})^{2n} + (1 - i\sqrt{3})^{2n} = 2^{2n}\left(2\cos\dfrac{2n\pi}{3}\right) = 2^{2n+1}\cos\dfrac{2n\pi}{3}$.

Answer: $2^{2n+1}\cos\left(\dfrac{2n\pi}{3}\right)$

</details>

---

### Q4. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\frac{(\cos \theta+i \sin \theta)^4}{(\sin \theta+i \cos \theta)^5}=$ where $i=\sqrt{-1}$

**Options:**

- **(A)** $\cos \theta-i \sin \theta$
- **(B)** $\cos 9 \theta-\mathrm{i} \sin 9 \theta$
- **(C)** $\sin \theta-i \cos \theta$
- **(D)** $\sin 9 \theta-i \cos 9 \theta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sin 9 \theta-i \cos 9 \theta$**

**Detailed Solution:**

Using Euler's formula, $\cos \theta + i \sin \theta = e^{i\theta}$.

The numerator is $(\cos \theta + i \sin \theta)^4 = (e^{i\theta})^4 = e^{i4\theta}$.

For the denominator, we factor out $i$:

$\sin \theta + i \cos \theta = i(\cos \theta - i \sin \theta) = i e^{-i\theta}$

Thus, the denominator is $(\sin \theta + i \cos \theta)^5 = (i e^{-i\theta})^5 = i^5 e^{-i5\theta} = i e^{-i5\theta}$.

Substituting these into the given expression:

$\dfrac{(\cos \theta+i \sin \theta)^4}{(\sin \theta+i \cos \theta)^5} = \dfrac{e^{i4\theta}}{i e^{-i5\theta}}$

$= \dfrac{1}{i} e^{i4\theta} e^{i5\theta} = -i e^{i9\theta}$

$= -i (\cos 9\theta + i \sin 9\theta)$

$= -i \cos 9\theta - i^2 \sin 9\theta$

$= \sin 9\theta - i \cos 9\theta$

Answer: $\sin 9 \theta-i \cos 9 \theta$

</details>

---

### Q5. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\begin{aligned} & \mathrm{f}(x)=(\cos x+\mathrm{i} \sin x) \cdot(\cos 3 x+\mathrm{i} \sin 3 x) \cdots \cdots[\cos (2 \mathrm{n}-1) x+\mathrm{i} \sin (2 \mathrm{n}-1) x], \\ & \mathrm{n} \in \mathbb{N} \text { Then } \mathrm{f}^{\prime \prime}(x)=,(\text { Where } i=\sqrt{-1})\end{aligned}$

**Options:**

- **(A)** $\mathrm{n}^2 \mathrm{f}(x)$
- **(B)** $-\mathrm{n}^4 \mathrm{f}(x)$
- **(C)** $-\mathrm{n}^2 \mathrm{f}(x)$
- **(D)** $\mathrm{n}^4 \mathrm{f}(x)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\mathrm{n}^4 \mathrm{f}(x)$**

**Detailed Solution:**

Using Euler's formula, $\cos \theta + \mathrm{i} \sin \theta = e^{\mathrm{i}\theta}$.

$\mathrm{f}(x) = e^{\mathrm{i}x} \cdot e^{\mathrm{i}3x} \cdots e^{\mathrm{i}(2\mathrm{n}-1)x}$

$\mathrm{f}(x) = e^{\mathrm{i}(1 + 3 + 5 + \dots + (2\mathrm{n}-1))x}$

The sum of the first $\mathrm{n}$ odd natural numbers is $\mathrm{n}^2$.

$\mathrm{f}(x) = e^{\mathrm{i}\mathrm{n}^2 x}$

Differentiating with respect to $x$:

$\mathrm{f}^{\prime}(x) = \mathrm{i} \mathrm{n}^2 e^{\mathrm{i}\mathrm{n}^2 x}$

Differentiating again with respect to $x$:

$\mathrm{f}^{\prime\prime}(x) = (\mathrm{i} \mathrm{n}^2)^2 e^{\mathrm{i}\mathrm{n}^2 x}$

$\mathrm{f}^{\prime\prime}(x) = \mathrm{i}^2 \mathrm{n}^4 e^{\mathrm{i}\mathrm{n}^2 x}$

Since $\mathrm{i}^2 = -1$ and $e^{\mathrm{i}\mathrm{n}^2 x} = \mathrm{f}(x)$:

$\mathrm{f}^{\prime\prime}(x) = -\mathrm{n}^4 \mathrm{f}(x)$

Answer: $-\mathrm{n}^4 \mathrm{f}(x)$

</details>

---

### Q6. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{z}=x+\mathrm{i} y$ and $\mathrm{z}^{1 / 3}=\mathrm{p}+\mathrm{iq}$, where $x, y, \mathrm{p}$, $\mathrm{q} \in \mathrm{R}$ and $\mathrm{i}=\sqrt{-1}$, then value of $\left(\frac{x}{\mathrm{p}}+\frac{y}{\mathrm{q}}\right)$ is

**Options:**

- **(A)** $p^2-q^2$
- **(B)** $4\left(p^2-q^2\right)$
- **(C)** $\mathrm{p}^2+\mathrm{q}^2$
- **(D)** $4\left(p^2+q^2\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4\left(p^2-q^2\right)$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{z}^{\frac{1}{3}}=\mathrm{p}+\mathrm{iq} \\ & \Rightarrow \mathrm{z}=(\mathrm{p}+\mathrm{iq})^3 \\ & \Rightarrow x+\mathrm{i} y=\mathrm{p}^3+3 \mathrm{p}^2 \mathrm{qi}+3 \mathrm{p}(\mathrm{iq})^2+(\mathrm{iq})^3 \\ & \Rightarrow x+\mathrm{i} y=\left(\mathrm{p}^3-3 \mathrm{pq}^2\right)+\left(3 \mathrm{p}^2 \mathrm{q}-\mathrm{q}^3\right) \mathrm{i} \\ & \Rightarrow x=\mathrm{p}^3-3 \mathrm{pq}^2 \text { and } y=3 \mathrm{p}^2 \mathrm{q}-\mathrm{q}^3 \\ & \\ & \Rightarrow \frac{x}{\mathrm{p}}=\mathrm{p}^2-3 \mathrm{q}^2 \text { and } \frac{y}{\mathrm{q}}=3 \mathrm{p}^2-\mathrm{q}^2 \\ & \therefore \quad\left(\frac{x}{\mathrm{p}}+\frac{y}{\mathrm{q}}\right)=4 \mathrm{p}^2-4 \mathrm{q}^2=4\left(\mathrm{p}^2-\mathrm{q}^2\right)\end{aligned}$

</details>

---

