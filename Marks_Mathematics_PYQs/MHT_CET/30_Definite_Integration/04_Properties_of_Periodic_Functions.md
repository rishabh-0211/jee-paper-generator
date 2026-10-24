# MHT CET Mathematics - Definite Integration

## Topic 4: Properties of Periodic Functions

**Total Questions:** 6

---

### Q1. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x) = x - [x]$ for every real number $x$, where $[x]$ is integral part of $x$. then $\int\limits_{-1}^{1} f(x)\, dx$ is

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $1/2$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

Given $f(x) = x - [x]$

The integral is $\int_{-1}^{1} (x - [x]) \, dx$

This can be separated as $\int_{-1}^{1} x \, dx - \int_{-1}^{1} [x] \, dx$

Since $x$ is an odd function, $\int_{-1}^{1} x \, dx = 0$

For the second integral, we split the limits at the integer value $0$:

$\int_{-1}^{1} [x] \, dx = \int_{-1}^{0} [x] \, dx + \int_{0}^{1} [x] \, dx$

In the interval $(-1, 0)$, $[x] = -1$ and in the interval $(0, 1)$, $[x] = 0$

$\int_{-1}^{1} [x] \, dx = \int_{-1}^{0} (-1) \, dx + \int_{0}^{1} 0 \, dx$

$= -1[x]_{-1}^{0} + 0$

$= -1(0 - (-1)) = -1$

Substituting these back, we get:

$\int_{-1}^{1} (x - [x]) \, dx = 0 - (-1) = 1$

Answer: $1$

</details>

---

### Q2. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \frac{\sin ^2 x}{1+2^x} \mathrm{~d} x$ is

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{8}$
- **(C)** $\frac{\pi}{2}$
- **(D)** $4 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}$**

**Detailed Solution:**

Let $I = \int_{-\dfrac{\pi}{2}}^{\dfrac{\pi}{2}} \dfrac{\sin ^2 x}{1+2^x} \mathrm{~d} x$

Using the property $\int_{a}^{b} f(x) \mathrm{~d} x = \int_{a}^{b} f(a+b-x) \mathrm{~d} x$, we replace $x$ with $-\dfrac{\pi}{2} + \dfrac{\pi}{2} - x = -x$:

$I = \int_{-\dfrac{\pi}{2}}^{\dfrac{\pi}{2}} \dfrac{\sin ^2 (-x)}{1+2^{-x}} \mathrm{~d} x$

$I = \int_{-\dfrac{\pi}{2}}^{\dfrac{\pi}{2}} \dfrac{2^x \sin ^2 x}{2^x+1} \mathrm{~d} x$

Adding the two expressions for $I$, we get:

$2I = \int_{-\dfrac{\pi}{2}}^{\dfrac{\pi}{2}} \dfrac{(1+2^x)\sin ^2 x}{1+2^x} \mathrm{~d} x$

$2I = \int_{-\dfrac{\pi}{2}}^{\dfrac{\pi}{2}} \sin ^2 x \mathrm{~d} x$

Since $\sin ^2 x$ is an even function, we can write:

$2I = 2 \int_{0}^{\dfrac{\pi}{2}} \sin ^2 x \mathrm{~d} x$

$I = \int_{0}^{\dfrac{\pi}{2}} \sin ^2 x \mathrm{~d} x$

Using the identity $\sin ^2 x = \dfrac{1-\cos 2x}{2}$:

$I = \int_{0}^{\dfrac{\pi}{2}} \dfrac{1-\cos 2x}{2} \mathrm{~d} x$

$I = \left[ \dfrac{x}{2} - \dfrac{\sin 2x}{4} \right]_{0}^{\dfrac{\pi}{2}}$

$I = \dfrac{\pi}{4} - 0 = \dfrac{\pi}{4}$

Answer: $\frac{\pi}{4}$

</details>

---

### Q3. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\frac{\pi}{4}} \frac{\sec ^2 x}{(1+\tan x)(2+\tan x)} d x=$

**Options:**

- **(A)** $\log \left(\frac{3}{4}\right)$
- **(B)** $\frac{1}{3} \log \left(\frac{4}{3}\right)$
- **(C)** $\quad \log \left(\frac{4}{3}\right)$
- **(D)** $\frac{1}{4} \log \left(\frac{3}{4}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\quad \log \left(\frac{4}{3}\right)$**

**Detailed Solution:**

Let $I = \int_0^{\dfrac{\pi}{4}} \dfrac{\sec^2 x}{(1+\tan x)(2+\tan x)} dx$

Substitute $\tan x = t$, which gives $\sec^2 x dx = dt$

When $x = 0$, $t = 0$
When $x = \dfrac{\pi}{4}$, $t = 1$

The integral becomes:
$I = \int_0^1 \dfrac{1}{(1+t)(2+t)} dt$

Using partial fractions:
$I = \int_0^1 \left( \dfrac{1}{1+t} - \dfrac{1}{2+t} \right) dt$

Integrating with respect to $t$:
$I = \left[ \log(1+t) - \log(2+t) \right]_0^1$

$I = \left[ \log\left(\dfrac{1+t}{2+t}\right) \right]_0^1$

Substituting the limits:
$I = \log\left(\dfrac{2}{3}\right) - \log\left(\dfrac{1}{2}\right)$

$I = \log\left(\dfrac{2/3}{1/2}\right)$

$I = \log\left(\dfrac{4}{3}\right)$

Answer: $\quad \log \left(\frac{4}{3}\right)$

</details>

---

### Q4. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $g(x)=\int_0^x \cos ^4 t \mathrm{~d} t$, then $g(x+\pi)$ equals

**Options:**

- **(A)** $g(x)+g(\pi)$
- **(B)** $g(x)-g(\pi)$
- **(C)** $\frac{g(x)}{g(\pi)}$
- **(D)** $g(x) \cdot g(\pi)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $g(x)+g(\pi)$**

**Detailed Solution:**

$\begin{aligned}
& g(x)=\int_0^x \cos ^4 t \mathrm{~d} t \\
& \Rightarrow g(x+\pi)=\int_0^{x+\pi} \cos ^4 t \mathrm{~d} t=\int_0^x \cos ^4 t \mathrm{~d} t+\int_x^{x+\pi} \cos ^4 t \mathrm{~d} t \\
& =g(x)+\int_x^{x+\pi} \cos ^4 t \mathrm{~d} t \\
& =g(x)+\int_0^\pi \cos ^4 t \mathrm{~d} t
\end{aligned}$
[as $\cos ^4 t$ is a periodic function with period $\left.\pi\right]=g(x)+g(\pi)$

</details>

---

### Q5. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_0^{2 \pi}(\sin x+|\sin x|) d x=$

**Options:**

- **(A)** 0
- **(B)** 8
- **(C)** 4
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

$\begin{aligned} & \int_0^{2 \pi}(\sin x+|\sin x|) d x= \\ & =\int_0^\pi(\sin x+\sin x) d x+\int_0^\pi(\sin x-\sin x) d x \\ & =\int_0^\pi 2 \sin x d x+0 \\ & =[-2 \cos x]_0^\pi=4\end{aligned}$

</details>

---

### Q6. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$$
\int_0^{\frac{\pi}{2}} \frac{\sin x-\cos x}{1-\sin x \cos x} d x=
$$

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{2}{\pi}$
- **(C)** 0
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

Let $I=\int_0^{\pi / 2} \frac{\sin x-\cos x}{1-\sin x \cos x} d x$
$$
\begin{aligned}
& \therefore I=\int_0^{\frac{\pi}{2}} \frac{\sin \left(\frac{\pi}{2}-x\right)-\cos \left(\frac{\pi}{2}-x\right)}{1-\sin \left(\frac{\pi}{2}-x\right) \cos \left(\frac{\pi}{2}-x\right)} d x \\
& =\int_0^{\pi / 2} \frac{\cos x-\sin x}{1-\cos x \sin x} d x
\end{aligned}
$$
Eq. (1) $+(2)$ gives
$$
2 \mathrm{I}=\int_0^{\frac{\pi}{2}} 0 \mathrm{dx} \Rightarrow \mathrm{I}=0
$$

</details>

---

