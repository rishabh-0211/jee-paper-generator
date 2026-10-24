# BITSAT Mathematics - Differential Equations

## Topic 2: Formation of Differential Equation

**Total Questions:** 2

---

### Q1. BITSAT 2016

*Type:* `singleCorrect` | *Level:* `1`

For any differentiable function $y$ of $x$, $\frac{d^{2} x}{d y^{2}}\left(\frac{d y}{d x}\right)^{3}+\frac{d^{2} y}{d x^{2}}=$

**Options:**

- **(A)** 0
- **(B)** $y$
- **(C)** $-y$
- **(D)** $x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

$\frac{d y}{d x}=\left(\frac{d x}{d y}\right)^{-1}$

$\Rightarrow \frac{d^{2} y}{d x^{2}}=-1\left(\frac{d x}{d y}\right)^{-2}\left\{\frac{d}{d x}\left(\frac{d x}{d y}\right)\right\}$

$\Rightarrow \frac{d^{2} y}{d x^{2}}=(-1)\left(\frac{d x}{d y}\right)^{-2}\left\{\frac{d}{d y}\left(\frac{d x}{d y}\right) \frac{d y}{d x}\right\}$

$=(-1)\left(\frac{d y}{d x}\right)^{2}\left\{\frac{d^{2} x}{d y^{2}} \cdot \frac{d y}{d x}\right\}=-\left(\frac{d y}{d x}\right)^{3}\left\{\frac{d^{2} x}{d y^{2}}\right\}$

$\Rightarrow \frac{d^{2} x}{d y^{2}}\left(\frac{d y}{d x}\right)^{3}+\frac{d^{2} y}{d x^{2}}=0$

</details>

---

### Q2. BITSAT 2015

*Type:* `singleCorrect` | *Level:* `2`

If $y=\left(x+\sqrt{1+x^{2}}\right)^{n},$ then $\left(1+x^{2}\right) \frac{d^{2} y}{d x^{2}}+x \frac{d y}{d x}$ is

**Options:**

- **(A)** $n^{2} y$
- **(B)** $-n^{2} y$
- **(C)** $-y$
- **(D)** $2 x^{2} y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $n^{2} y$**

**Detailed Solution:**

$y=\left(x+\sqrt{1+x^{2}}\right)^{n}$

$$

\begin{array}{c}

\frac{d y}{d x}=n\left(x+\sqrt{1+x^{2}}\right)^{n-1}\left(1+\frac{1}{2}\left(1+x^{2}\right)^{-1 / 2} \cdot 2 x\right) \\

\qquad \begin{array}{c}

\frac{d y}{d x}=n\left(x+\sqrt{1+x^{2}}\right)^{n-1} \frac{\left(\sqrt{1+x^{2}}+x\right)}{\sqrt{1+x^{2}}} \\

=\frac{n\left(\sqrt{1+x^{2}}+x\right)^{n}}{\sqrt{1+x^{2}}}

\end{array}

\end{array}

$$

or $\sqrt{1+x^{2}} \frac{d y}{d x}=n y$ or $\sqrt{1+x^{2}} y_{1}=n y$

$$

\left(y_{1}=\frac{d y}{d x}\right)

$$

Squaring, $\left(1+x^{2}\right) y_{1}^{2}=n^{2} y^{2}$

Differentiating,

$$

\left(1+x^{2}\right) 2 y_{1} y_{2}+y_{1}^{2} \cdot 2 x=n^{2} \cdot 2 y y_{1}

$$

or $\left(1+x^{2}\right) y_{2}+x y_{1}=n^{2} y$

</details>

---

