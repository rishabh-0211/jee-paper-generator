# JEE Advanced Mathematics - Indefinite Integration

## Topic 2: Miscellaneous Forms

**Total Questions:** 2

---

### Q1. JEE Advanced 2008 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $I=\int \frac{e^x}{e^{4 x}+e^{2 x}+1} d x, J=\int \frac{e^{-x}}{e^{-4 x}+e^{-2 x}+1} d x$.
Then, for an arbitrary constant $C$, the value of $J-I$ equals

**Options:**

- **(A)** $\frac{1}{2} \log \left|\frac{e^{4 x}-e^{2 x}+1}{e^{4 x}+e^{2 x}+1}\right|+C$
- **(B)** $\frac{1}{2} \log \left|\frac{e^{2 x}+e^x+1}{e^{2 x}-e^x+1}\right|+C$
- **(C)** $\frac{1}{2} \log \left|\frac{e^{2 x}-e^x+1}{e^{2 x}+e^x+1}\right|+C$
- **(D)** $\frac{1}{2} \log \left|\frac{e^{4 x}+e^{2 x}+1}{e^{4 x}-e^{2 x}+1}\right|+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2} \log \left|\frac{e^{2 x}-e^x+1}{e^{2 x}+e^x+1}\right|+C$**

**Detailed Solution:**

Since, $J=\int \frac{e^{3 x}}{1+e^{2 x}+e^{4 x}} d x$
$$
\begin{aligned}
\therefore J-I & =\int \frac{\left(e^{3 x}-e^x\right)}{1+e^{2 x}+e^{4 x}} d x=\int \frac{\left(u^2-1\right)}{1+u^2+u^4} d u \\
& =\int \frac{\left(1-\frac{1}{u^2}\right)}{1+\frac{1}{u^2}+u^2} d u=\int \frac{\left(1-\frac{1}{u^2}\right)}{\left(u+\frac{1}{u}\right)^2-1} d u \\
& =\int \frac{d t}{t^2-1} \\
& =\frac{1}{2} \log \left|\frac{t-1}{t+1}\right|+C \\
& =\frac{1}{2} \log \left|\frac{u^2-u+1}{u^2+u+1}\right|+C=\frac{1}{2} \log \left|\frac{e^{2 x}-e^x+1}{e^{2 x}+e^x+1}\right|+C
\end{aligned}
$$

</details>

---

### Q2. JEE Advanced 2007 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)=\frac{x}{\left(1+x^n\right)^{1 / n}}$ for $n \geq 2$ and $g(x)=\underbrace{(f \circ f o \ldots o f)}_{f \text { occurs } n \text { times }}(x)$. Then, $\int x^{n-2} g(x) d x$ equals

**Options:**

- **(A)** $\frac{1}{n(n-1)}\left(1+n x^n\right)^{1-\frac{1}{n}}+k$
- **(B)** $\frac{1}{n-1}\left(1+n x^n\right)^{1-\frac{1}{n}}+k$
- **(C)** $\frac{1}{n(n+1)}\left(1+n x^n\right)^{1+\frac{1}{n}}+k$
- **(D)** $\frac{1}{n+1}\left(1+n x^n\right)^{1+\frac{1}{n}}+k$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{n(n-1)}\left(1+n x^n\right)^{1-\frac{1}{n}}+k$**

**Detailed Solution:**

Here, $\begin{array}{rlrl} & \text { and } & f f(x) & =\frac{f(x)}{\left[1+f(x)^n\right]^{1 / n}}=\frac{x}{\left(1+2 x^n\right)^{1 / n}} \\ & \therefore \quad f f f(x) & =\frac{x}{\left(1+3 x^n\right)^{1 / n}} \\ & \text { Let } & g(x) & =\underbrace{(f \circ f o \ldots o f)}_{n \text { times }}(x)=\frac{x}{\left(1+n x^n\right)^{1 / n}} \\ I & =\int x^{n-2} g(x) d x=\int \frac{x^{n-1} d x}{\left(1+n x^n\right)^{1 / n}} \\ & & =\frac{1}{n^2} \int \frac{n^2 x^{n-1} d x}{\left(1+n x^n\right)^{1 / n}}=\frac{1}{n^2} \int \frac{\frac{d}{d x}\left(1+n x^n\right)}{\left(1+n x^n\right)^{1 / n}} d x\end{array}$
$\therefore \quad I=\frac{1}{n(n-1)}\left(1+n x^n\right)^{1-\frac{1}{n}}+k$.

</details>

---

