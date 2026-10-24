# BITSAT Mathematics - Differentiation

## Topic 2: Differentiation of implicit functions

**Total Questions:** 3

---

### Q1. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

At $x=\frac{\pi^2}{4}, \frac{d}{d x}\left(\tan ^{-1}(\cos \sqrt{x})+\sec ^{-1}\left(e^x\right)\right)=$

**Options:**

- **(A)** $\frac{1}{\sqrt{\mathrm{e}^{\frac{\pi^2}{2}}}-1}-\frac{1}{\pi}$
- **(B)** $\frac{\pi}{4}+\frac{1}{\sqrt{\mathrm{e}^{\pi^2}+\mathrm{e}^{\pi^2 / 2}}}$
- **(C)** $\frac{1}{\sqrt{\mathrm{e}^{\pi^2}+\mathrm{e}^{\pi^2 / 2}}}+\frac{2}{\pi} \cot \left(\frac{\sqrt{\pi}}{2}\right)$
- **(D)** $\frac{1}{\sqrt{\mathrm{e}^\pi}}+\frac{1}{\pi}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\sqrt{\mathrm{e}^{\frac{\pi^2}{2}}}-1}-\frac{1}{\pi}$**

**Detailed Solution:**

$\frac{d}{d x}\left(\tan ^{-1}(\cos \sqrt{x})+\sec ^{-1}\left(\mathrm{e}^x\right)\right)$
$=\frac{(-\sin \sqrt{x})}{1+\cos ^2 \sqrt{x}} \cdot\left(\frac{1}{2 \sqrt{x}}\right)+\frac{1}{e^x \sqrt{e^{2 x}-1}} \cdot e^x$
but when $x=\frac{\pi^2}{4}$
$=-\frac{-\sin \frac{\pi}{2}}{1+\cos ^2 \frac{\pi}{2}}\left(\frac{1}{2}\right)\left(\frac{2}{\pi}\right)+\frac{1}{\sqrt{e^{\pi^2 / 2}-1}}$
$=-\frac{1}{\pi}+\frac{1}{\sqrt{e^{\pi^2 / 2}-1}}$

</details>

---

### Q2. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `2`

$\text { If } 2^{x}+2^{y}=2^{x+y} \text {, then } \frac{d y}{d x}=$

**Options:**

- **(A)** $2^{x-y} \frac{2^{y}-1}{2^{x}-1}$
- **(B)** $2^{x-y} \frac{2^{y}-1}{1-2^{x}}$
- **(C)** $\frac{2^{x}+2^{y}}{2^{x}-2^{y}}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) None of these**

**Detailed Solution:**

On differentiating

$\begin{array}{l}

2^{x} \log 2+2^{y} \log 2 \cdot \frac{\mathrm{dy}}{\mathrm{dx}} \\

=2^{x} \cdot 2^{y} \frac{\mathrm{dy}}{\mathrm{dx}} \cdot \log 2+2^{y} \cdot 2^{x} \log 2 \\

\Rightarrow 2^{x}+2^{y} \frac{\mathrm{dy}}{\mathrm{dx}}=2^{x+y} \frac{\mathrm{dy}}{\mathrm{dx}}+2^{x+y} \\

\Rightarrow \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{2^{x+y}-2^{x}}{2^{y}-2^{x+y}} \\

\Rightarrow \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{2^{x}+2^{y}-2^{x}}{2^{y}-2^{x}-2^{y}}=-2^{y-x}

\end{array}$

</details>

---

### Q3. BITSAT 2020

*Type:* `singleCorrect` | *Level:* `2`

If $x y+y^{2}=\tan x+y,$ then find $\frac{d y}{d x}$ is

**Options:**

- **(A)** $\frac{\sec ^{2} x}{x+2 y}$
- **(B)** $\frac{\sec ^{2} x-y}{(x+2 y-1)}$
- **(C)** $(x+2 y-1) \sec ^{2} x$
- **(D)** $\sec ^{2} x \cdot y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\sec ^{2} x-y}{(x+2 y-1)}$**

**Detailed Solution:**

The given relation is $x y+y^{2}=\tan x+y$. Differentiating both sides with respect to $x$, we get

$\frac{d}{d x}(x y)+\frac{d}{d x}\left(y^{2}\right)=\frac{d}{d x}(\tan x)+\frac{d y}{d x}$

or $\left[y \cdot 1+x \cdot \frac{d y}{d x}\right]+2 y \frac{d y}{d x}=\sec ^{2} x+\frac{d y}{d x}$

or $(x+2 y-1) \frac{d y}{d x}=\sec ^{2} x-y$

$\therefore \frac{d y}{d x}=\frac{\sec ^{2} x-y}{(x+2 y-1)}$

</details>

---

