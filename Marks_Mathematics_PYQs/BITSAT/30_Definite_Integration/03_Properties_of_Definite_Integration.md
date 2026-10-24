# BITSAT Mathematics - Definite Integration

## Topic 3: Properties of Definite Integration

**Total Questions:** 7

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `1`

The value of definite integral $\int_0^{\pi / 2} \log (\tan x) d x$ is

**Options:**

- **(A)** 0
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{2}$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Let $I=\int_0^{\frac{\pi}{2}} \log (\tan x) d x$....(i)
By applying property,
$\begin{aligned}
\int_a^b f(x) d x & =\int_a^b f(a+b-x) d x \\
I & =\int_0^{\frac{\pi}{2}} \log \left(\tan \left(\frac{\pi}{2}-x\right)\right) d x \\
I & =\int_0^{\frac{\pi}{2}} \log (\cot x) d x\ldots(ii)
\end{aligned}$
Adding Eqs. (i) and (ii),
$\begin{aligned}
& 2 I=\int_0^{\frac{\pi}{2}}[\log (\tan x)+\log (\cot x)] d x \\
& 2 I=\int_0^{\frac{\pi}{2}} \log 1 d x=0
\end{aligned}$

</details>

---

### Q2. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_5^9 \frac{\log 3 x^2}{\log 3 x^2+\log \left(588-84 x+3 x^2\right)} d x$ is equal to

**Options:**

- **(A)** $2$
- **(B)** $1$
- **(C)** $\frac{1}{2}$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2$**

**Detailed Solution:**

Let
$I=\int_5^9 \frac{\log 3 x^2 d x}{\log 3 x^2+\log \left(588-84 x+3 x^2\right)}$  ...(i)
$\begin{aligned} & =\int_5^9 \frac{\log 3 x^2 d x}{\log 3 x^2+\log 3(14-x)^2} \\ & =\int_5^9 \frac{\log 3(14-x)^2 d x}{\log 3(14-x)^2+\log 3(14-(14-x))^2} \\ & \quad\left[\int_a^b f(x) d x=\int_a^b f(a+b-x) d x\right]\end{aligned}$
$I=\int_5^9 \frac{\log 3(14-x)^2 d x}{\log 3(14-x)^2+\log 3 x^2}$  ...(ii)
Adding Eqs. (i) and (ii), we get
$\begin{aligned}
& 2 I=\int_5^9 \frac{\log 3 x^2+\log 3(14-x)^2}{\log 3(14-x)^2+\log 3 x^2} d x \\
& 2 \mathrm{I}=\int_5^9 d x=9-5=4 \Rightarrow I=2
\end{aligned}$

</details>

---

### Q3. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\frac{\pi}{2}} \frac{\sin \left(\frac{\pi}{4}+x\right)+\sin \left(\frac{3 \pi}{4}+x\right)}{\cos x+\sin x} d x=$

**Options:**

- **(A)** $\frac{\pi}{\sqrt{2}}$
- **(B)** $\frac{\pi}{2 \sqrt{2}}$
- **(C)** $\frac{\pi}{3 \sqrt{2}}$
- **(D)** $\frac{\pi}{4 \sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{2 \sqrt{2}}$**

**Detailed Solution:**

Let $I=\int_0^{\frac{\pi}{2}} \frac{\sin \left(\frac{\pi}{4}+x\right)+\sin \left(\frac{3 \pi}{4}+x\right)}{\cos x+\sin x} d x$
$\Rightarrow I=\int_0^{\pi / 2} \frac{\sin \left(\frac{3 \pi}{4}-x\right)+\sin \left(\frac{5 \pi}{4}-x\right)}{\sin x+\cos x} d x$
$\Rightarrow I=\int_0^{\pi / 2} \frac{\sin \left(\frac{\pi}{4}+x\right)-\sin \left(\frac{3 \pi}{4}+x\right)}{\cos x+\sin x} d x$
Now $I+I=\int_0^{\pi / 2} \frac{2 \sin \left(\frac{\pi}{4}+x\right)}{\cos x+\sin x} d x$
$\Rightarrow I=\int_0^{\pi / 2} \frac{\frac{1}{\sqrt{2}} \cos x+\frac{1}{\sqrt{2}} \sin x}{\cos x-\sin x} d x=\frac{\pi}{2 \sqrt{2}}$

</details>

---

### Q4. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `2`

Evaluate: $\int_{0}^{\pi} \frac{1}{5+4 \cos x} d x$

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{3}$**

**Detailed Solution:**

We have, $\int_{0}^{\pi} \frac{1}{5+4 \cos x} d x$

$=\int_{0}^{\pi} \frac{1}{5+4\left(\frac{1-\tan ^{2} \frac{x}{2}}{1+\tan ^{2} \frac{x}{2}}\right)} d x$

$=\int_{0}^{\pi} \frac{1+\tan ^{2} \frac{x}{2}}{5\left(1+\tan ^{2} \frac{x}{2}\right)+4\left(1-\tan ^{2} \frac{x}{2}\right)} d x$

$=\int_{0}^{\pi} \frac{1+\tan ^{2} \frac{x}{2}}{9+\tan ^{2} \frac{x}{2}} \mathrm{dx}=\int_{0}^{\pi} \frac{\sec ^{2} \frac{x}{2}}{9+\tan ^{2} \frac{x}{2}} \mathrm{dx}$

Let $\tan \frac{x}{2}=t \Rightarrow \frac{1}{2} \sec ^{2} \frac{x}{2} d x=d t$

Also, $x=0 \Rightarrow t=0$ and $x=\pi \Rightarrow t=\infty$

$\therefore \mathrm{I}=\int_{0}^{\infty} \frac{\mathrm{dt}}{9+t^{2}}$

$\therefore \mathrm{I}=2 \int_{0}^{\infty} \frac{\mathrm{dt}}{9+t^{2}}$

$\therefore \mathrm{I}=\frac{2}{3}\left[\tan ^{-1} \frac{t}{3}\right]_{0}^{\infty}=\frac{2}{3}\left[\tan ^{-1} \infty-\tan ^{-1} 0\right]$

$=\frac{2}{3}\left(\frac{\pi}{2}-0\right)=\frac{\pi}{3}$

</details>

---

### Q5. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `1`

$\int_{-a}^{4}\left(x^{8}-x^{4}+x^{2}+1\right) d x=2 \int_{0}^{4}\left(x^{8}-x^{4}+x^{2}+1\right) d x$ then $a=$

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 6
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 4**

**Detailed Solution:**

If $\mathrm{f}(x)$ is an even function then

$\int_{-a}^{a} f(x) d x=2 \int_{0}^{a} f(x) d x$

Here $\mathrm{f}(x)=x^{8}-x^{4}+x^{2}+1$ is an even function, therefore $a=4$.

</details>

---

### Q6. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `2`

$\int_{0}^{10} \frac{x^{10}}{(10-x)^{10}+x^{10}} d x$ is equal to

**Options:**

- **(A)** 10
- **(B)** 5
- **(C)** 2
- **(D)** $\frac{1}{0}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5**

**Detailed Solution:**

Let $I=\int_{0}^{10} \frac{x^{10}}{(10-x)^{10}+x^{10}} d x$...(1)

$I=\int_{0}^{10} \frac{(10-x)^{10}}{(10-x)^{10}+x^{10}} d x$...(2)

Adding

(1) and (2), we get

$2 I=\int_{0}^{10} d x \Rightarrow 2 I=10 \Rightarrow I=5$

</details>

---

### Q7. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{\pi / 2} \frac{2^{\sin x}}{2^{\sin x}+2^{\cos x}} d x$ equals

**Options:**

- **(A)** 2
- **(B)** $\pi$
- **(C)** $\pi / 4$
- **(D)** $\pi / 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\pi / 4$**

**Detailed Solution:**

$\mathrm{I}=\int_{0}^{\pi / 2} \frac{2^{\sin \mathrm{x}}}{2^{\sin x}+2^{\cos \mathrm{x}} \mathrm{dx}}$
$\mathrm{I}=\int_{0}^{\pi / 2} \frac{2^{\sin (\pi / 2-\mathrm{x})}}{2^{\sin (\pi / 2-\mathrm{x})}+2^{\cos (\pi / 2-\mathrm{x})} \mathrm{dx}}$
$=\int \frac{2^{\cos \mathrm{x}}}{2^{\cos \mathrm{x}}+2^{\sin \mathrm{x}}} \mathrm{dx} \Rightarrow 21=\int_{0}^{\pi / 2} \mathrm{~d} \mathrm{x}=\frac{\pi}{2} \Rightarrow 1=\frac{\pi}{4}$

</details>

---

