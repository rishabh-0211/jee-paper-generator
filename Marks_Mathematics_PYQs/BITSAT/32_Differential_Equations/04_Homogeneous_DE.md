# BITSAT Mathematics - Differential Equations

## Topic 4: Homogeneous DE

**Total Questions:** 2

---

### Q1. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `2`

If the slope of the tangent to the curve at any point $\mathrm{P}(x, y)$ is $\frac{y}{x}-\cos ^{2} \frac{y}{x}$, then the equation of a curve passing through $\left(1, \frac{\pi}{4}\right)$ is

**Options:**

- **(A)** $\tan \left(\frac{y}{x}\right)+\log x=1$
- **(B)** $\tan \left(\frac{y}{x}\right)+\log y=1$
- **(C)** $\tan \left(\frac{x}{y}\right)+\log x=1$
- **(D)** $\tan \left(\frac{x}{y}\right)+\log y=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan \left(\frac{y}{x}\right)+\log x=1$**

**Detailed Solution:**

According to the condition,

$\frac{\mathrm{dy}}{\mathrm{dx}}=\frac{y}{x}-\cos ^{2} \frac{y}{x} \ldots \text { (i) }$

This is a homogeneous differential equation Substituting $y=v x$, we get

$\begin{array}{l}

v+x \frac{\mathrm{dv}}{\mathrm{dx}}=v-\cos ^{2} v \\

\Rightarrow x \frac{\mathrm{dv}}{\mathrm{dx}}=-\cos ^{2} v \\

\Rightarrow \int \sec ^{2} \mathrm{vdv}=-\int \frac{\mathrm{dx}}{\mathrm{x}} \\

\Rightarrow \tan v=-\log x+\mathrm{C} \\

\Rightarrow \tan \frac{y}{x}+\log x=\mathrm{C}

\end{array}$

Substituting $\mathrm{x}=1, y=\frac{\pi}{4}$, we get $\mathrm{C}=1$

Thus, we get

$\tan \left(\frac{y}{x}\right)+\log x=1$

which is the required solution.

</details>

---

### Q2. BITSAT 2015

*Type:* `singleCorrect` | *Level:* `3`

If $\phi(\mathrm{x})$ is a differential function, then the solution of the differential equation $\mathrm{dy}+\left\{\mathrm{y} \phi^{\prime}(\mathrm{x})-\phi(\mathrm{x})\right.$

$\left.\phi^{\prime}(x)\right\} d x=0,$ is

**Options:**

- **(A)** $y=\{\phi(x)-1\}+C e^{-\phi(x)}$
- **(B)** $y \phi(x)=\{\phi(x)\}^{2}+C$
- **(C)** $y e^{\varphi(x)}=\phi(x) e^{\phi(x)}+C$
- **(D)** $y-\phi(x)=\phi(x) e^{-\phi(x)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $y=\{\phi(x)-1\}+C e^{-\phi(x)}$**

**Detailed Solution:**

Given differential equation is

$\mathrm{dy}+\left\{y \phi^{\prime}(x)-\phi(x) \phi^{\prime}(x)\right\} d x=0$

$\Rightarrow \frac{\mathrm{dy}}{\mathrm{dx}}+\phi^{\prime}(\mathrm{x}) \mathrm{y}=\phi(\mathrm{x}) \phi^{\prime}(\mathrm{x})$

which is a linear differential equation with $\quad P=\phi^{\prime}(x), Q=\phi(x) \cdot \phi^{\prime}(x)$ and

$I \cdot F=e^{\int \phi^{\prime}(x) d x}=e^{\phi(x)}$

$\therefore$ Solution is $y \cdot e^{\phi(x)}=\int \phi(x) \cdot \phi^{\prime}(x) e^{\phi(x)} d x+C$

$\Rightarrow y \cdot e^{\phi(x)}=\int \phi(x) \cdot e^{\phi(x)} \phi^{\prime}(x) d x+C$

$\Rightarrow y \cdot e^{\phi(x)}=\phi(x) e^{\phi(x)}-\int \phi^{\prime}(x) e^{\phi(x)} d x+C$

$\Rightarrow y \cdot e^{\phi(x)}=\phi(x) e^{\phi(x)}-e^{\phi(x)}+C$

$\Rightarrow y=\lceil\phi(x)-1]+C e^{-\phi(x)}$

</details>

---

