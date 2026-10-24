# BITSAT Mathematics - Differentiation

## Topic 7: Functional Equation

**Total Questions:** 4

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `2`

If $x \sqrt{1+y}+y \sqrt{1+x}=0$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{x+1}{x}$
- **(B)** $\frac{1}{1+x}$
- **(C)** $\frac{-1}{(1+x)^2}$
- **(D)** $\frac{x}{1+x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-1}{(1+x)^2}$**

**Detailed Solution:**

$\begin{aligned}
& \text {  Given, } x \sqrt{1+y}+y \sqrt{1+x}=0 \\
& \Rightarrow \quad x \sqrt{1+y}=-y \sqrt{1+x} \\
& \Rightarrow \quad(x \sqrt{1+y})^2=(-y \sqrt{1+x})^2
\end{aligned}$
$\begin{array}{lr}
\Rightarrow & x^2(1+y)=y^2(1+x) \\
\Rightarrow & x^2-y^2=y^2 x-x^2 y \\
\Rightarrow & (x-y)(x+y)=x y(y-x) \\
\Rightarrow & x+y=-x y \\
\Rightarrow & x+y+x y=0 \\
\Rightarrow & y=\frac{-x}{1+x}=-1+\frac{1}{1+x}
\end{array}$
Differentiating w.r.t, $x$
$\frac{d y}{d x}=-\frac{1}{(1+x)^2}$

</details>

---

### Q2. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(\mathrm{x})=\sqrt{1+\cos ^2\left(\mathrm{x}^2\right)}$, then the value of $f^{\prime}\left(\frac{\sqrt{\pi}}{2}\right)$

**Options:**

- **(A)** $\frac{\sqrt{\pi}}{6}$
- **(B)** $-\sqrt{\frac{\pi}{6}}$
- **(C)** $\frac{1}{\sqrt{6}}$
- **(D)** $\frac{\pi}{\sqrt{6}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\sqrt{\frac{\pi}{6}}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/_NTjqRT8hKJ5THfUNdP4T3sWIILr9OmymI6oIXX4-EQ.original.fullsize.png">

On differentiating (i) w.r.t.x, we get
$f^{\prime}(x)=\frac{-2 \sin x^2 \cos x^2}{\sqrt{1+\cos ^2 x^2}}(x)$<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/EdpMz33XoOBGACcfTnTZM5cxVVi4UlbFmlVTJTu-wOM.original.fullsize.png">

Put, $x=\frac{\sqrt{\pi}}{2}$ in (ii), we get
$\begin{aligned}
& \mathrm{f}^{\prime}\left(\frac{\sqrt{\pi}}{2}\right)=-\frac{\sqrt{\pi}}{2} \cdot \frac{\sin 2\left(\frac{\pi}{4}\right)}{\sqrt{1+\frac{1}{2}}} \\
& =-\frac{\sqrt{\pi}}{2} \cdot \frac{\sin \frac{\pi}{2}}{\sqrt{\frac{3}{2}}}=-\sqrt{\frac{\pi}{6}}
\end{aligned}$

</details>

---

### Q3. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `2`

For the function
$f(x)=\frac{x^{100}}{100}+\frac{x^{99}}{99}+\ldots \frac{x^{2}}{2}+x+1$
$\mathrm{f}^{\prime}(1)=\mathrm{mf}^{\prime}(0),$ where $\mathrm{m}$ is equal to

**Options:**

- **(A)** 50
- **(B)** 0
- **(C)** 100
- **(D)** 200

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 100**

**Detailed Solution:**

Given, $f(x)=\frac{x^{100}}{100}+\frac{x^{99}}{99}+\ldots+\frac{x^{2}}{2}+x+1$
$\Rightarrow \quad f^{\prime}(x)=\frac{100 x^{99}}{100}+\frac{99 x^{98}}{99}+\ldots+\frac{2 x}{2}+1+0$
$\left[\because \mathrm{f}(\mathrm{x})=\mathrm{x}^{\mathrm{n}} \Rightarrow \mathrm{f}^{\prime}(\mathrm{x})=\mathrm{nx}^{\mathrm{n}-1}\right]$
$\Rightarrow \mathrm{f}^{\prime}(\mathrm{x})=\mathrm{x}^{99}+\mathrm{x}^{98}+\ldots+\mathrm{x}+1$ ...(i)
Putting $\mathrm{x}=1$, we get $f^{\prime}(1)=\underbrace{(1)^{99}+1^{98}+\ldots+1+1}_{100 \text { times }}=\underbrace{1+1+1 \ldots+1+1}_{100 \text { times }}$
$\Rightarrow \quad \mathrm{f}^{\prime}(1)=100$ ...(ii)
Again, putting $\mathrm{x}=0$, we get $\mathrm{f}^{\prime}(0)=0+0+\ldots+0+1 \quad \Rightarrow \mathrm{f}^{\prime}(0)=1$ ...(iii)
From eqs. (ii) and(iii), we get; $\mathrm{f}^{\prime}(1)=100 \mathrm{f}^{\prime}(0)$ Hence, $m=100$

</details>

---

### Q4. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x+y)=f(x) \cdot f(y)$ for all $x, y$ where $f(0) \neq 0$ If $f(5)=2$ and $f^{\prime}(0)=3,$ then $f^{\prime}(5)$ is equal to-

**Options:**

- **(A)** 6
- **(B)** 0
- **(C)** 1
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 6**

**Detailed Solution:**

$f^{\prime}(5)=\lim _{h \rightarrow 0} \frac{f(5+h)-f(5)}{h}$
$=\lim _{h \rightarrow 0} \frac{f(5+h)-f(5+0)}{h}$
$=\lim _{h \rightarrow 0} \frac{f(5) \cdot f(h)-f(5)+f(0)}{h}$
$(\because f(x+y)=f(x), f(y)$ for all $x, y)$
$=\left(\lim _{h \rightarrow 0} \frac{f(h)-f(0)}{h}\right) \cdot f(5)=f^{\prime}(0) \cdot f(5)$
$=3 \times 2=6$

</details>

---

