# MHT CET Mathematics - Complex Number

## Topic 1: Power of iota

**Total Questions:** 7

---

### Q1. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\displaystyle\sum_{n=1}^{4}(i^n + i^{n+1})$ is

**Options:**

- **(A)** $1$
- **(B)** $i$
- **(C)** $-i$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0$**

**Detailed Solution:**

$\displaystyle\sum_{n=1}^{4}(i^n + i^{n+1}) = \sum_{n=1}^{4} i^n(1 + i)$

$= (1 + i) \sum_{n=1}^{4} i^n$

$= (1 + i) (i + i^2 + i^3 + i^4)$

$= (1 + i) (i - 1 - i + 1)$

$= (1 + i)(0) = 0$

Answer: $0$

</details>

---

### Q2. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $i = \sqrt{-1}$ then $\left[i^{18} + \left(\dfrac{1}{i}\right)^{25}\right]^3 =$

**Options:**

- **(A)** $4 + 4i$
- **(B)** $2 + 2i$
- **(C)** $4 - 4i$
- **(D)** $2 - 2i$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 - 2i$**

**Detailed Solution:**

We know that $i^4 = 1$ and $i^2 = -1$.

Evaluating the first term:

$i^{18} = (i^4)^4 \cdot i^2 = 1 \cdot (-1) = -1$

Evaluating the second term:

$\left(\dfrac{1}{i}\right)^{25} = \dfrac{1}{i^{25}} = \dfrac{1}{(i^4)^6 \cdot i} = \dfrac{1}{i} = -i$

Substituting these values into the given expression:

$\left[i^{18} + \left(\dfrac{1}{i}\right)^{25}\right]^3 = (-1 - i)^3$

$= -(1 + i)^3$

$= -(1^3 + 3(1)^2(i) + 3(1)(i)^2 + i^3)$

$= -(1 + 3i - 3 - i)$

$= -(-2 + 2i)$

$= 2 - 2i$

Answer: $2 - 2i$

</details>

---

### Q3. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $z = \sum_{n=0}^{2026} i^n$, where $i = \sqrt{-1}$, then one of the values of $\sqrt{z}$ is...

**Options:**

- **(A)** $e^{i\frac{\pi}{4}}$
- **(B)** $\dfrac{1}{\sqrt{2}}e^{i\frac{\pi}{4}}$
- **(C)** $e^{i\frac{\pi}{2}}$
- **(D)** $\dfrac{1}{\sqrt{2}}e^{i\frac{\pi}{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $e^{i\frac{\pi}{4}}$**

**Detailed Solution:**

The given series is a geometric progression with $2027$ terms, first term $1$, and common ratio $i$.

Using the sum formula for a geometric progression:

$z = \dfrac{1(1 - i^{2027})}{1 - i}$

Since $2027 = 4 \times 506 + 3$, we have $i^{2027} = (i^4)^{506} \cdot i^3 = 1 \cdot (-i) = -i$.

Substituting this into the expression for $z$:

$z = \dfrac{1 - (-i)}{1 - i} = \dfrac{1 + i}{1 - i}$

Multiplying the numerator and denominator by the conjugate of the denominator, $1 + i$:

$z = \dfrac{(1 + i)^2}{(1 - i)(1 + i)} = \dfrac{1 + i^2 + 2i}{1^2 - i^2}$

Since $i^2 = -1$:

$z = \dfrac{1 - 1 + 2i}{1 - (-1)} = \dfrac{2i}{2} = i$

In exponential form, $i$ can be written as $e^{i\left(\dfrac{\pi}{2} + 2k\pi\right)}$ where $k$ is an integer.

Therefore, the square root of $z$ is:

$\sqrt{z} = \left(e^{i\left(\dfrac{\pi}{2} + 2k\pi\right)}\right)^{\dfrac{1}{2}} = e^{i\left(\dfrac{\pi}{4} + k\pi\right)}$

For $k = 0$, one of the values is $e^{i\dfrac{\pi}{4}}$.

Answer: $e^{i\frac{\pi}{4}}$

</details>

---

### Q4. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\frac{\mathrm{i}^{248}+\mathrm{i}^{246}+\mathrm{i}^{244}+\mathrm{i}^{242}+\mathrm{i}^{240}}{\mathrm{i}^{249}+\mathrm{i}^{247}+\mathrm{i}^{245}+\mathrm{i}^{243}+\mathrm{i}^{241}}$, $(\mathrm{i}=\sqrt{-1})$ is

**Options:**

- **(A)** $\mathrm{i}$
- **(B)** 1
- **(C)** -1
- **(D)** $-\mathrm{i}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\mathrm{i}$**

**Detailed Solution:**

$\begin{aligned} & \frac{i^{245}+i^{246}+i^{244}+i^{242}+i^{240}}{i^{243}+i^{247}+i^{245}+i^{243}+i^{241}} \\ & =\frac{i^{240}\left(i^8+i^6+i^4+i^2+1\right)}{i^{241}\left(i^8+i^6+i^4+i^2+1\right)} \\ & =\frac{i^{200}}{i^{241}} \\ & =\frac{1}{i} \\ & =\frac{i}{i^2}=-i\end{aligned}$

</details>

---

### Q5. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $Z_1=4 \mathrm{i}^{40}-5 \mathrm{i}^{35}+6 \mathrm{i}^{17}+2, \mathrm{Z}_2=-1+\mathrm{i}$, where $\mathrm{i}=\sqrt{-1}$, then $\left|\mathrm{Z}_1+\mathrm{Z}_2\right|=$

**Options:**

- **(A)** 5
- **(B)** 13
- **(C)** 12
- **(D)** 15

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 13**

**Detailed Solution:**

$\begin{aligned} & \mathrm{Z}_1=4 \mathrm{i}^{40}-5 \mathrm{i}^{35}+6 \mathrm{i}^{17}+2 \\ & \mathrm{Z}_1=6+11 \mathrm{i} \\ & \mathrm{Z}_2=-1+\mathrm{i} \\ \therefore \quad \mathrm{Z}_1 & +\mathrm{Z}_2=6+11 \mathrm{i}-1+\mathrm{i} \\ & =5+12 \mathrm{i} \\ \therefore \quad & \left|\mathrm{Z}_1+\mathrm{Z}_2\right|=\sqrt{(5)^2+(12)^2}=\sqrt{169}=13\end{aligned}$

</details>

---

### Q6. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\frac{i^{592}+i^{590}+i^{588}+i^{586}+i^{584}}{i^{582}+i^{580}+i^{578}+i^{576}+i^{574}}-1=$

**Options:**

- **(A)** $-1$
- **(B)** $-2$
- **(C)** $-3$
- **(D)** $-4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-2$**

**Detailed Solution:**

$\begin{aligned} & \frac{i^{584}\left(i^8+i^6+i^4+i^2+1\right)}{i^{574}\left(i^8+i^6+i^4+i^2+1\right)}-1=\frac{i^{584}}{i^{574}}-1 \\ & \quad=i^{10}-1=-1-1=-2\end{aligned}$

</details>

---

### Q7. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $(1+i)^5(1-i)^7$

**Options:**

- **(A)** -64
- **(B)** -64 i
- **(C)** 64 i
- **(D)** 64

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -64 i**

**Detailed Solution:**

$\begin{aligned} & (1+i)^5(1-i)^7 \\ = & (1+i)^5(1-i)^5(1-i)^2=[(1+i)(1+i)(1-i)]^5\left(1-2 i+i^2\right) \\ = & \left(1-i^2\right)^5(-2 i)=(2)^5(-2 i)=-64 i \ldots\left[\because i^2=-1\right]\end{aligned}$

</details>

---

