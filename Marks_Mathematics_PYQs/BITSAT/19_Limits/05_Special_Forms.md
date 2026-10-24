# BITSAT Mathematics - Limits

## Topic 5: Special Forms

**Total Questions:** 2

---

### Q1. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `2`

The value of $\lim _{x \rightarrow 0} \frac{(1+x)^{\frac{1}{x}}-e+\frac{1}{2} e x}{x^2}$ is

**Options:**

- **(A)** $\frac{11}{24} e$
- **(B)** $-\frac{11}{24} e$
- **(C)** $\frac{e}{24}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{11}{24} e$**

**Detailed Solution:**

Let $y=(1+x)^{1 / x}$
$\Rightarrow \log y=\frac{1}{x} \log (1+x)=\frac{1}{x}\left[x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\ldots\right]$
$=1-\frac{x}{2}+\frac{x^2}{3}-\frac{x^3}{4}+\ldots$
$\begin{aligned} y & =e^{\left(1-\frac{x}{2}+\frac{x^2}{3}+\ldots .\right)}=e e^{\left(\frac{-x}{2}+\frac{x^2}{3} \ldots . .\right)} \\ & =e\left[1+\left(-\frac{x}{2}+\frac{x^2}{3}-\ldots\right)+\frac{1}{2 !}\left(-\frac{x}{2}+\frac{x^2}{3}-\ldots\right)^2+\ldots\right]\end{aligned}$
$y-e+\frac{1}{2} e x=e x^2\left[\frac{1}{3}+0(x)+\frac{1}{2}\left(-\frac{1}{2}+0(x)\right)^2+\ldots.\right]$
$[\because 0(x)$ in terms containing $x]$
$\lim \frac{y-e+\frac{1}{2} e x}{x^2}=e\left[\frac{1}{3}+\frac{1}{8}\right]=\frac{11}{24} e$

</details>

---

### Q2. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0}(\operatorname{cosec} x)^{1 / \log x}$ is equal to :

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $\frac{1}{e}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{e}$**

**Detailed Solution:**

Let $y=\lim _{x \rightarrow 0}(\operatorname{cosec} x)^{1 / \log x}$

Taking $\log$ on both sides, we get

$\log y=\lim _{x \rightarrow 0} \frac{\log \operatorname{cosec} x}{\log x}\left[\frac{\infty}{\infty}\right.$ form $]$

$=\lim _{x \rightarrow 0} \frac{-\cot x}{1 / x} \quad$ (ByL' Hospital rule)

$=-\lim _{x \rightarrow 0} \frac{x}{\tan x} \quad\left(\because \cot x=\frac{1}{\tan x}\right)$

$\Rightarrow \log y=-1$

$\Rightarrow y=e^{-1}=\frac{1}{e}$

Hence, required limit $=\frac{1}{e}$

</details>

---

