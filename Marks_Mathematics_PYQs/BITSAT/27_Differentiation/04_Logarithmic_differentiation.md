# BITSAT Mathematics - Differentiation

## Topic 4: Logarithmic differentiation

**Total Questions:** 2

---

### Q1. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

If $y^x=e^{y-x}$, then $\frac{d y}{d x}$ is equal to

**Options:**

- **(A)** $\frac{1+\log y}{y \log y}$
- **(B)** $\frac{(1+\log y)^2}{y \log y}$
- **(C)** $\frac{1+\log y}{(\log y)^2}$
- **(D)** $\frac{(1+\log y)^2}{\log y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{(1+\log y)^2}{\log y}$**

**Detailed Solution:**

Here, $\mathrm{y}^{\mathrm{x}}=\mathrm{e}^{\mathrm{y}-\mathrm{x}}$
Taking log on both sides, we get
$\begin{aligned}
& \log y^x=\log e^{y-x} \\
& \quad\left(\because \log a^b=b \log a \text { and } \log e=1\right)
\end{aligned}$
$\Rightarrow x \log y=(y-x) \log e \Rightarrow x \log y=y-x \ldots(i)$
On differentiating w.r.t. $x$, we get
$\frac{d}{d x}(x \log y)=\frac{d}{d x}(y-x)$
(using product rule)
$\begin{aligned}
& \Rightarrow x\left(\frac{1}{y}\right) \frac{d y}{d x}+\log y(1)=\frac{d y}{d x}-1 \\
& \Rightarrow \frac{d y}{d x}\left(\frac{x}{y}-1\right)=-1-\log y \\
& \Rightarrow \frac{d y}{d x}\left[\frac{y}{(1+\log y) y}-1\right]=-(1+\log y) \\
& \qquad \quad\left[\because \text { from eq. }(i) \cdot x=\frac{y}{(1+\log y)}\right] \\
& \Rightarrow \frac{d y}{d x}\left[\frac{1-1-\log y}{1+\log y}\right]=-(1+\log y)
\end{aligned}$
$\Rightarrow \frac{d y}{d x}=-\frac{(1+\log y)^2}{-\log y}$
$\Rightarrow \frac{d y}{d x}=\frac{(1+\log y)^2}{\log y}$

</details>

---

### Q2. BITSAT 2011

*Type:* `singleCorrect` | *Level:* `2`

If \(y=x^{x^2}\), then \(\frac{d y}{d x}\) is equal to

**Options:**

- **(A)** \((2 \ln x)\)
- **(B)** \((2 \ln x+1)\)
- **(C)** \((\ln \ln x+1) x^{x^2}\)
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) None of these**

**Detailed Solution:**

Consider \(y=x^{x^2} \Rightarrow \ln y=x^2 \ln x\)
\(\begin{aligned}
& \frac{1}{y} \frac{d y}{d x}=2 x \ln x+x^2 \cdot \frac{1}{x}=x(1+2 \ln x) \\
& \frac{d y}{d x}=x^{x^2} \cdot x(1+2 \ln x)=x^{x^2+1}(1+2 \ln x)
\end{aligned}\)

</details>

---

