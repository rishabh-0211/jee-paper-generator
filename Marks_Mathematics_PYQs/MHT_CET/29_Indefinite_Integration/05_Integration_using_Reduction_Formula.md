# MHT CET Mathematics - Indefinite Integration

## Topic 5: Integration using Reduction Formula

**Total Questions:** 3

---

### Q1. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \tan ^4 x \mathrm{dx}=a \tan ^3 x+\mathrm{b} \tan x+\mathrm{c} x+\mathrm{k}$ (where k is the constant of integration) then the value of $a-b+c=$

**Options:**

- **(A)** $\frac{7}{3}$
- **(B)** $\frac{5}{3}$
- **(C)** $\frac{4}{3}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{7}{3}$**

**Detailed Solution:**

Let $I = \int \tan^4 x \, dx$

We can write $\tan^4 x = \tan^2 x \cdot \tan^2 x$

Using the identity $\tan^2 x = \sec^2 x - 1$, we get:

$I = \int \tan^2 x (\sec^2 x - 1) \, dx$

$I = \int \tan^2 x \sec^2 x \, dx - \int \tan^2 x \, dx$

Again using $\tan^2 x = \sec^2 x - 1$ for the second integral:

$I = \int \tan^2 x \sec^2 x \, dx - \int (\sec^2 x - 1) \, dx$

$I = \int \tan^2 x \sec^2 x \, dx - \int \sec^2 x \, dx + \int 1 \, dx$

For the first integral, substituting $u = \tan x \Rightarrow du = \sec^2 x \, dx$, we get $\int u^2 \, du = \dfrac{u^3}{3} = \dfrac{1}{3} \tan^3 x$.

Integrating the remaining terms, we get:

$I = \dfrac{1}{3} \tan^3 x - \tan x + x + k$

Comparing this with the given expression $a \tan^3 x + b \tan x + c x + k$, we find:

$a = \dfrac{1}{3}$, $b = -1$, $c = 1$

Therefore, the value of $a - b + c$ is:

$a - b + c = \dfrac{1}{3} - (-1) + 1 = \dfrac{1}{3} + 2 = \dfrac{7}{3}$

Answer: $\frac{7}{3}$

</details>

---

### Q2. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}(x)=\frac{\sin ^2 \pi x}{1+\pi^x}$, then
$\int(\mathrm{f}(x)+\mathrm{f}(-x)) \mathrm{d} x$ is equal to

**Options:**

- **(A)** $\frac{x}{2}-\frac{\sin \pi x}{2 \pi}+\mathrm{c}$, (where c is a constant of integration)
- **(B)** $\frac{1}{2} x-\frac{\sin 2 \pi x}{4 \pi}+\mathrm{c}$, (where c is a constant of integration)
- **(C)** $\frac{x}{2}-\frac{\cos \pi x}{2 \pi}+\mathrm{c}$, (where c is a constant of integration)
- **(D)** $\frac{1}{1+\pi^x}+\frac{\cos ^2 \pi x}{2 \pi}+\mathrm{c}$, (where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2} x-\frac{\sin 2 \pi x}{4 \pi}+\mathrm{c}$, (where c is a constant of integration)**

**Detailed Solution:**

Given $\mathrm{f}(x) = \dfrac{\sin^2 \pi x}{1 + \pi^x}$

$\mathrm{f}(-x) = \dfrac{\sin^2(-\pi x)}{1 + \pi^{-x}} = \dfrac{\sin^2 \pi x}{1 + \dfrac{1}{\pi^x}} = \dfrac{\pi^x \sin^2 \pi x}{\pi^x + 1}$

Adding $\mathrm{f}(x)$ and $\mathrm{f}(-x)$:

$\mathrm{f}(x) + \mathrm{f}(-x) = \dfrac{\sin^2 \pi x}{1 + \pi^x} + \dfrac{\pi^x \sin^2 \pi x}{1 + \pi^x} = \dfrac{(1 + \pi^x) \sin^2 \pi x}{1 + \pi^x} = \sin^2 \pi x$

Now, integrating the sum:

$\int (\mathrm{f}(x) + \mathrm{f}(-x)) \mathrm{d}x = \int \sin^2 \pi x \mathrm{d}x$

Using the identity $\sin^2 \theta = \dfrac{1 - \cos 2\theta}{2}$:

$\int \sin^2 \pi x \mathrm{d}x = \int \dfrac{1 - \cos 2\pi x}{2} \mathrm{d}x$

$= \dfrac{1}{2} \int (1 - \cos 2\pi x) \mathrm{d}x$

$= \dfrac{1}{2} \left( x - \dfrac{\sin 2\pi x}{2\pi} \right) + \mathrm{c}$

$= \dfrac{1}{2} x - \dfrac{\sin 2\pi x}{4\pi} + \mathrm{c}$

Answer: $\frac{1}{2} x-\frac{\sin 2 \pi x}{4 \pi}+\mathrm{c}$, (where c is a constant of integration)

</details>

---

### Q3. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{\cos \theta}{5+7 \sin \theta-2 \cos ^2 \theta} d \theta=A \log _e|f(\theta)|+c$ (where $\mathrm{c}$ is a constant of integration), then $\frac{f(\theta)}{A}$ can be

**Options:**

- **(A)** $\frac{2 \sin \theta+1}{\sin \theta+3}$
- **(B)** $\frac{2 \sin \theta+1}{5(\sin \theta+3)}$
- **(C)** $\frac{5(\sin \theta+3)}{2 \sin \theta+1}$
- **(D)** $\frac{5(2 \sin \theta+1)}{\sin \theta+3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{5(2 \sin \theta+1)}{\sin \theta+3}$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } I=\int \frac{\cos \theta}{5+7 \sin \theta-2 \cos ^2 \theta} d \theta \\ & =\int \frac{\cos \theta}{5+7 \sin \theta-2\left(1-\sin ^2 \theta\right)} d \theta \\ & =\int \frac{\cos \theta}{2 \sin ^2 \theta+7 \sin \theta+3} d \theta \\ & =\int \frac{\cos \theta}{(\sin \theta+3)(2 \sin \theta+1)} d \theta \\ & \text { Put } \sin \theta=t \\ & \Rightarrow \cos \theta d \theta=d t\end{aligned}$
$\begin{aligned} \therefore \quad I & =\int \frac{d t}{(t+3)(2 t+1)} \\ & =\int\left[\frac{2}{5(2 t+1)}-\frac{1}{5(t+3)}\right] d t \\ & =\frac{2}{5} \cdot \frac{\log |2 t+1|}{2}-\frac{1}{5} \log |t+3|+c \\ & =\frac{1}{5} \log |2 \sin \theta+1|-\frac{1}{5} \log |\sin \theta+3|+c \\ & =\frac{1}{5} \log \left|\frac{2 \sin \theta+1}{\sin \theta+3}\right|+c\end{aligned}$
$\begin{aligned} & \therefore \quad \mathrm{A}=\frac{1}{5}, \mathrm{f}(\theta)=\frac{2 \sin \theta+1}{\sin \theta+3} \\ & \therefore \quad \frac{\mathrm{f}(\theta)}{\mathrm{A}}=\frac{5(2 \sin \theta+1)}{\sin \theta+3}\end{aligned}$

</details>

---

