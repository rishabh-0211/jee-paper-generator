# BITSAT Mathematics - Definite Integration

## Topic 1: Definite Integration by Parts

**Total Questions:** 3

---

### Q1. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int \frac{x^2\left(x \sec ^2 x+\tan x\right)}{(x \tan x+1)^2} d x$ is equal to

**Options:**

- **(A)** $-\frac{x^2}{x \tan x+1}+c$
- **(B)** $2 \log _e|x \sin x+\cos x|+c$
- **(C)** $-\frac{x^2}{x \tan x+1}+2 \log _e|x \sin x+\cos x|+c$
- **(D)** $\frac{x^2}{x^2 \tan x-1}-2 \log _e|x \sin x+\cos x|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{x^2}{x \tan x+1}+2 \log _e|x \sin x+\cos x|+c$**

**Detailed Solution:**

(c) We note that
$\frac{d}{d x}(x \tan x+1)=x \sec ^2 x+\tan x$
$\therefore$ integrating by parts with $x^2$ as first function, we get
$\begin{aligned}
& I=\int x^2 \frac{x \sec ^2 x+\tan x}{(x \tan x+1)^2} d x \\
& =x^2\left(-\frac{1}{x \tan x+1}\right)-\int 2 x\left(-\frac{1}{x \tan x+1}\right) d x \\
& =-\frac{x^2}{x \tan x+1}+2 \int \frac{x \cos x}{x \sin x+\cos x} d x \\
& =-\frac{x^2}{x \tan x+1}+2 \log _e|x \sin x+\cos x|+c \\
& \quad\left(\because \frac{d}{d x}(x \sin x+\cos x)=x \cos x\right)
\end{aligned}$

</details>

---

### Q2. BITSAT 2020

*Type:* `singleCorrect` | *Level:* `3`

$\int_{\pi / 3}^{\pi / 2} x \sin (\pi[x]-x) \mathrm{dx}$ is equal to

**Options:**

- **(A)** $\frac{1}{2}+\frac{\pi}{6}$
- **(B)** $1-\frac{\sqrt{3}}{2}+\frac{\pi}{6}$
- **(C)** $-\frac{1}{2}-\frac{\pi}{6}$
- **(D)** $\frac{\sqrt{3}}{2}-1-\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1-\frac{\sqrt{3}}{2}+\frac{\pi}{6}$**

**Detailed Solution:**

In the interval $\frac{\pi}{3}$ to $\frac{\pi}{2},[\mathrm{x}]=1$ $\begin{aligned} \therefore \mathrm{I} &=\int_{\pi / 3}^{\pi / 2} \mathrm{x} \sin (\pi-\mathrm{x}) \mathrm{dx}=\int_{\pi / 3}^{\pi / 2} \mathrm{x} \sin \mathrm{x} \mathrm{d} \mathrm{x} \\ &=[-\mathrm{x} \cos \mathrm{x}+\sin \mathrm{x}]_{\pi / 3}^{\pi / 2}=1-\frac{\sqrt{3}}{2}+\frac{\pi}{6} \end{aligned}$

</details>

---

### Q3. BITSAT 2010

*Type:* `singleCorrect` | *Level:* `3`

\(\int 4 \cos \left(x+\frac{\pi}{6}\right) \cos 2 x \cdot \cos \left(\frac{5 \pi}{6}+x\right) d x\)

**Options:**

- **(A)** \(-\left(x+\frac{\sin 4 x}{4}+\frac{\sin 2 x}{2}\right)+c\)
- **(B)** \(-\left(x+\frac{\sin 4 x}{4}-\frac{\sin 2 x}{2}\right)+c\)
- **(C)** \(-\left(x-\frac{\sin 4 x}{4}+\frac{\sin 2 x}{2}\right)+c\)
- **(D)** \(-\left(x-\frac{\sin 4 x}{4}+\frac{\cos 2 x}{2}\right)+c\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) \(-\left(x+\frac{\sin 4 x}{4}+\frac{\sin 2 x}{2}\right)+c\)**

**Detailed Solution:**

\(\begin{aligned}
& \int 4 \cos \left(x+\frac{\pi}{6}\right) \cos 2 x \cdot \cos \left(\frac{5 \pi}{6}+x\right) d x \\
& =2 \int\left(\cos (2 x+\pi) \cos \frac{2 \pi}{3}\right) \cos 2 x d x \\
& =2 \int\left(-\cos 2 x-\frac{1}{2}\right) \cos 2 x d x \\
& =\int\left(-2 \cos ^2 2 x-\cos 2 x\right) d x \\
& =-\int(1+\cos 4 x+\cos 2 x) d x \\
& =-x-\frac{\sin 4 x}{x}-\frac{\sin 2 x}{2}+c
\end{aligned}\)

</details>

---

