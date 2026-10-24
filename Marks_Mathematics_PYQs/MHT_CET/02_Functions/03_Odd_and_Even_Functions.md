# MHT CET Mathematics - Functions

## Topic 3: Odd and Even Functions

**Total Questions:** 4

---

### Q1. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The function $\mathrm{f}(x)=\sec \left[\log \left(x+\sqrt{1+x^2}\right)\right]$ is _______ function

**Options:**

- **(A)** even
- **(B)** odd
- **(C)** neither even nor odd
- **(D)** square

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) even**

**Detailed Solution:**

Given $f(x) = \sec \left[ \log \left( x + \sqrt{1+x^2} \right) \right]$

Replacing $x$ with $-x$, we get:

$f(-x) = \sec \left[ \log \left( -x + \sqrt{1+(-x)^2} \right) \right]$

$f(-x) = \sec \left[ \log \left( \sqrt{1+x^2} - x \right) \right]$

Multiplying and dividing the argument of the logarithm by $\sqrt{1+x^2} + x$:

$f(-x) = \sec \left[ \log \left( \dfrac{(\sqrt{1+x^2} - x)(\sqrt{1+x^2} + x)}{\sqrt{1+x^2} + x} \right) \right]$

$f(-x) = \sec \left[ \log \left( \dfrac{1+x^2 - x^2}{\sqrt{1+x^2} + x} \right) \right]$

$f(-x) = \sec \left[ \log \left( \dfrac{1}{x + \sqrt{1+x^2}} \right) \right]$

$f(-x) = \sec \left[ \log \left( x + \sqrt{1+x^2} \right)^{-1} \right]$

$f(-x) = \sec \left[ -\log \left( x + \sqrt{1+x^2} \right) \right]$

Since $\sec(-\theta) = \sec(\theta)$:

$f(-x) = \sec \left[ \log \left( x + \sqrt{1+x^2} \right) \right] = f(x)$

Since $f(-x) = f(x)$, the given function is an even function.

Answer: even

</details>

---

### Q2. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the function $\mathrm{g}:(-\infty, \infty) \rightarrow\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ be given by $\mathrm{g}(\mathrm{u})=2 \tan ^{-1}\left(\mathrm{e}^{\mathrm{u}}\right)-\frac{\pi}{2}$. Then g is

**Options:**

- **(A)** even and is strictly increasing in $(0, \infty)$.
- **(B)** odd and is strictly decreasing in $(-\infty, \infty)$.
- **(C)** odd and is strictly increasing in $(-\infty, \infty)$.
- **(D)** neither even nor odd, but is strictly increasing in $(-\infty, \infty)$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) odd and is strictly increasing in $(-\infty, \infty)$.**

**Detailed Solution:**

Given function is $\mathrm{g}(\mathrm{u}) = 2 \tan^{-1}(\mathrm{e}^{\mathrm{u}}) - \dfrac{\pi}{2}$.

To check if the function is even or odd, we find $\mathrm{g}(-\mathrm{u})$:

$\mathrm{g}(-\mathrm{u}) = 2 \tan^{-1}(\mathrm{e}^{-\mathrm{u}}) - \dfrac{\pi}{2}$

Since $\mathrm{e}^{\mathrm{u}} > 0$ for all $\mathrm{u} \in \mathbb{R}$, we can use the property $\tan^{-1}\left(\dfrac{1}{x}\right) = \cot^{-1}(x)$ for $x > 0$.

$\mathrm{g}(-\mathrm{u}) = 2 \cot^{-1}(\mathrm{e}^{\mathrm{u}}) - \dfrac{\pi}{2}$

Using the identity $\tan^{-1}(x) + \cot^{-1}(x) = \dfrac{\pi}{2}$, we get $\cot^{-1}(\mathrm{e}^{\mathrm{u}}) = \dfrac{\pi}{2} - \tan^{-1}(\mathrm{e}^{\mathrm{u}})$.

$\mathrm{g}(-\mathrm{u}) = 2 \left( \dfrac{\pi}{2} - \tan^{-1}(\mathrm{e}^{\mathrm{u}}) \right) - \dfrac{\pi}{2}$

$\mathrm{g}(-\mathrm{u}) = \pi - 2 \tan^{-1}(\mathrm{e}^{\mathrm{u}}) - \dfrac{\pi}{2}$

$\mathrm{g}(-\mathrm{u}) = \dfrac{\pi}{2} - 2 \tan^{-1}(\mathrm{e}^{\mathrm{u}}) = -\left( 2 \tan^{-1}(\mathrm{e}^{\mathrm{u}}) - \dfrac{\pi}{2} \right) = -\mathrm{g}(\mathrm{u})$

Therefore, $\mathrm{g}(\mathrm{u})$ is an odd function.

Now, to check the monotonicity, we find the derivative $\mathrm{g}'(\mathrm{u})$:

$\mathrm{g}'(\mathrm{u}) = \dfrac{d}{d\mathrm{u}} \left( 2 \tan^{-1}(\mathrm{e}^{\mathrm{u}}) - \dfrac{\pi}{2} \right)$

$\mathrm{g}'(\mathrm{u}) = 2 \left( \dfrac{1}{1 + (\mathrm{e}^{\mathrm{u}})^2} \right) \cdot \mathrm{e}^{\mathrm{u}} = \dfrac{2\mathrm{e}^{\mathrm{u}}}{1 + \mathrm{e}^{2\mathrm{u}}}$

Since $\mathrm{e}^{\mathrm{u}} > 0$ for all $\mathrm{u} \in \mathbb{R}$, we have $\mathrm{g}'(\mathrm{u}) > 0$ for all $\mathrm{u} \in (-\infty, \infty)$.

Thus, $\mathrm{g}(\mathrm{u})$ is strictly increasing in $(-\infty, \infty)$.

Answer: odd and is strictly increasing in $(-\infty, \infty)$.

</details>

---

### Q3. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\frac{2 x+3}{3 x-2}, x \neq \frac{2}{3}$ then f of is

**Options:**

- **(A)** an even function
- **(B)** not defined for all $x \in R$
- **(C)** a constant function
- **(D)** an odd function

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) an odd function**

**Detailed Solution:**

We have, $\mathrm{f}(\mathrm{x})=\frac{2 \mathrm{x}+3}{3 \mathrm{x}-2}$
$\therefore(\mathrm{fof})(\mathrm{x})=\mathrm{f}[\mathrm{f}(\mathrm{x})]=\mathrm{f}\left(\frac{2 \mathrm{x}+3}{3 \mathrm{x}-2}\right)$
$=\frac{2\left(\frac{2 \mathrm{x}+3}{3 \mathrm{x}-2}\right)+3}{3\left(\frac{2 \mathrm{x}+3}{3 \mathrm{x}-2}\right)-2}=\frac{2(2 \mathrm{x}+3)+3(3 \mathrm{x}-2)}{3(2 \mathrm{x}+3)-2(3 \mathrm{x}-2)}$
$=\frac{4 \mathrm{x}+6+9 \mathrm{x}-6}{6 \mathrm{x}+9-6 \mathrm{x}+4}=\frac{13 \mathrm{x}}{13}=\mathrm{x} \quad \ldots$ is an odd function

</details>

---

### Q4. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}: \mathrm{R} \rightarrow \mathrm{R}$, such that $f(x)=\frac{e^{x}+e^{-x}}{e^{x}-e^{-x}}$, then $\mathrm{f}$ is

**Options:**

- **(A)** a periodic function
- **(B)** an even function
- **(C)** an odd function
- **(D)** a neither even nor odd function

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) an odd function**

**Detailed Solution:**

$f(x)=\frac{e^{x}+e^{-x}}{e^{x}-e^{-x}}$
$=\frac{e^{x}+\frac{1}{e^{x}}}{e^{x}-\frac{1}{e^{x}}}=\frac{e^{2 x}+1}{e^{2 x}-1}$
$f(-x)=\frac{e^{-x}+e^{x}}{e^{-x}-e^{x}}$
$=\frac{\frac{1}{e^{x}}+e^{x}}{\frac{1}{e^{x}}-e^{x}}=\frac{1+e^{2 x}}{1-e^{2 x}}=\frac{1+e^{2 x}}{-\left(e^{2 x}-1\right)}$
$\therefore f(-x)=-f(x)$
$\therefore \mathrm{f}(\mathrm{x})$ is an odd function.

</details>

---

