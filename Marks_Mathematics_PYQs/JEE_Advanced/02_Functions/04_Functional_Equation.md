# JEE Advanced Mathematics - Functions

## Topic 4: Functional Equation

**Total Questions:** 4

---

### Q1. JEE Advanced 2024 (Paper 2)

*Type:* `numerical` | *Level:* `3`

Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be a function such that $f(x+y)=f(x)+f(y)$ for all $x, y \in \mathbb{R}$, and $g: \mathbb{R} \rightarrow(0, \infty)$ be a function such that $g(x+y)=g(x) g(y)$ for all $x, y \in \mathbb{R}$. If $f\left(\frac{-3}{5}\right)=12$ and $g\left(\frac{-1}{3}\right)=2$, then the value of $\left(f\left(\frac{1}{4}\right)+g(-2)-8\right) g(0)$ is . ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **51**

**Detailed Solution:**

$f(x+y)=f(x)+f(y)$  ...(1)
$\Rightarrow \quad \mathrm{f}(\mathrm{nx})=\operatorname{nf}(\mathrm{x}) \forall \mathrm{n} \in \mathrm{N}$  ...(2)
Now put $y=-x$ in eq.(1)
$\begin{aligned} & \mathrm{f}(\mathrm{x})+\mathrm{f}(-\mathrm{x})=\mathrm{f}(0) \quad\{\mathrm{f}(0)=0\} \\ \Rightarrow \quad & \mathrm{f}(-\mathrm{x})=-\mathrm{f}(\mathrm{x})\end{aligned}$
$\Rightarrow \quad \mathrm{f}$ is odd function from eq. (2)
from eq. (2)
$\begin{aligned} & f(-n x)=\operatorname{nf}(-x) \\ & \Rightarrow \quad \mathrm{f}(-\mathrm{nx})=-n f(\mathrm{x}) \\ & \end{aligned}$
$\Rightarrow \quad \mathrm{f}(\mathrm{mx})=\operatorname{mf}(\mathrm{x}) \forall \mathrm{m} \in \mathrm{Z}$   ...(3)
from eq. (2) and eq. (3)
$\mathrm{f}(\mathrm{nx})=\mathrm{nf}(\mathrm{x}) \forall \mathrm{n} \in \mathrm{Z}$   ...(4)
Now put $x=\frac{p}{q}$ where $\mathrm{p}, \mathrm{q} \in \mathrm{Z}, \mathrm{q} \neq 0$
$\mathrm{f}\left(\frac{\mathrm{np}}{\mathrm{q}}\right)=\operatorname{nf}\left(\frac{\mathrm{p}}{\mathrm{q}}\right) \forall \mathrm{n} \in \mathrm{Z}$
put $\mathrm{n}=\mathrm{q}$
$f(p)=q f\left(\frac{p}{q}\right)$
$\Rightarrow \quad \mathrm{pf}(1)=\mathrm{qf}\left(\frac{\mathrm{p}}{\mathrm{q}}\right) \quad$ {from eq.(4)}
Let $\mathrm{f}(1)=\mathrm{a}$
then $\quad \mathrm{pa}=\mathrm{qf}\left(\frac{\mathrm{p}}{\mathrm{q}}\right)$
$\mathrm{f}\left(\frac{\mathrm{p}}{\mathrm{q}}\right)=\frac{\mathrm{ap}}{q}$
$\Rightarrow \quad \mathrm{f}(\mathrm{x})=\mathrm{ax} \forall \mathrm{x} \in \mathbb{Q}$
Now, $\mathrm{f}\left(\frac{-3}{5}\right)=\mathrm{a}\left(\frac{-3}{5}\right)=12 \Rightarrow \mathrm{a}=-20$
$\Rightarrow \quad \mathrm{f}(\mathrm{x})=-20 \mathrm{x} \forall \mathrm{x} \in \mathbb{Q}$   ...(5)
From the given functional equation it is not possible to find a unique function for irrational values of ' $x$ ', there are infinitely many such functions satisfying given functional equation for irrational values of $x$, but in this problem we finally need the function at rational values of ' $x$ ' only. So, for rational values of $x$ we are getting a unique function mentioned in (5).
Now, $g(x+y)=g(x) \cdot g(y)$
$\Rightarrow \quad \ell \mathrm{n}(\mathrm{g}(\mathrm{x}+\mathrm{y})=\ell \mathrm{n}(\mathrm{g}(\mathrm{x}))+\ell \ln (\mathrm{g}(\mathrm{y}))$
Let $\quad \ln (\mathrm{g}(\mathrm{x}))=\mathrm{h}(\mathrm{x})$
$\begin{array}{ll}\Rightarrow & \mathrm{h}(\mathrm{x}+\mathrm{y})=\mathrm{h}(\mathrm{x})+\mathrm{h}(\mathrm{y}) \\ \Rightarrow & \mathrm{h}(\mathrm{x})=\mathrm{kx} \forall \mathrm{x} \in \mathbb{Q}\end{array}$
$\Rightarrow \quad \mathrm{g}(\mathrm{x})=\mathrm{e}^{\mathrm{kx}} \forall \mathrm{x} \in \mathbb{Q}$   ...(6)
and $\mathrm{g}\left(\frac{-1}{3}\right)=\mathrm{e}^{-\frac{\mathrm{K}}{3}}=2 \quad \Rightarrow \quad \mathrm{K}=-3 \ell \ln 2$
$\Rightarrow \quad \mathrm{K}=\ln \left(\frac{1}{8}\right)$
$\Rightarrow \quad \mathrm{g}(\mathrm{x})=\mathrm{e}^{\ln \left(\frac{1}{8}\right) \cdot \mathrm{x}}=\left(\frac{1}{8}\right)^{\mathrm{x}}=2^{-3 \mathrm{x}} \forall \mathrm{x} \in \mathbb{Q}$
$\begin{aligned} & \text { Now, } f\left(\frac{1}{4}\right)=-5, g(-2)=2^6=64 \\ & g(0)=1\end{aligned}$
$\begin{aligned} & \text { So } \quad\left(\mathrm{f}\left(\frac{1}{4}\right)+\mathrm{g}(-2)-(8) \cdot g(0)\right) \\ & =(-5+64-8)(1)=51 \\ & \end{aligned}$

</details>

---

### Q2. JEE Advanced 2018 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a differentiable function with <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math> and satisfying the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>y</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mi>f</mi><mfenced separators="|"><mi>y</mi></mfenced></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>&#8712;</mo><mi>R</mi></math>. Then, the value of <math><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced></mrow></mfenced></mrow></mrow></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mo>&#160;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>y</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mi>f</mi><mfenced separators="|"><mi>y</mi></mfenced><mo>&#160;</mo><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>&#8712;</mo><mi>R</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mn>0,0</mn></mfenced><mo>:</mo><mo>&#160;</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mn>0</mn></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mn>0</mn></mfenced><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>=</mo><mn>2</mn><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mn>0</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mn>0</mn></mrow></mfenced><mo>:</mo><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>.</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mn>0</mn></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>.</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>x</mi></mrow></msup></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced></mrow></mfenced></mrow></mrow><mo>=</mo><mn>2</mn></math>

</details>

---

### Q3. JEE Advanced 2012 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)=(1-x)^{2} \sin ^{2} x+x^{2}$ for all $x \in I R$ and let $g(x)=\int_{1}^{x}\left(\frac{2(t-1)}{t+1}-\ln t\right) f(t) d t$ for all $x \in(1, \infty)$.

<strong> Question:</strong> Consider the statements:

$P$ : There exists some $x \in \mathrm{R}$ such that $f(x)+2 x$

$=2\left(1+x^{2}\right)$

$Q$ : There exists some $x \in \mathrm{R}$ such that $2 f(x)+1$ $=2 x(1+x)$

Then

**Options:**

- **(A)** both $P$ and $Q$ are true
- **(B)** $P$ is true and $Q$ is false
- **(C)** $P$ is false and $Q$ is true
- **(D)** both $P$ and $Q$ are false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $P$ is false and $Q$ is true**

**Detailed Solution:**

For the statement $P, f(x)+2 x=2\left(1+x^{2}\right)$

$\Rightarrow(1-x)^{2} \sin ^{2} x+x^{2}+2 x=2\left(1+x^{2}\right)$

$\Rightarrow(1-x)^{2} \sin ^{2} x=x^{2}-2 x+1+1$

$\Rightarrow(1-x)^{2} \sin ^{2} x=(1-x)^{2}+1$

$\Rightarrow(1-x)^{2} \cos ^{2} x=-1$, which is not possible for any real value of $x$.

Hence $P$ is not true.

Let $H(x)=2 f(x)+1-2 x(1+x)$

$H(0)=2 f(0)+1-0=1$

and $H(1)=2 f(1)+1-4=-3$

Hence, $H(x)$ has a solution in $(0,1)$

Therefore, $Q$ is true.

</details>

---

### Q4. JEE Advanced 2008 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $g(x)=\log f(x)$, where $f(x)$ is a twice differentiable positive function on $(0, \infty)$ such that $f(x+1)=x f(x)$. Then, for $N=1,2,3, \ldots . g^{\prime \prime}\left(N+\frac{1}{2}\right)-g^{\prime \prime}\left(\frac{1}{2}\right)$ is equal to

**Options:**

- **(A)** $-4\left\{1+\frac{1}{9}+\frac{1}{25}+\ldots+\frac{1}{(2 N-1)^2}\right\}$
- **(B)** $4\left\{1+\frac{1}{9}+\frac{1}{25}+\ldots+\frac{1}{(2 N-1)^2}\right\}$
- **(C)** $-4\left\{1+\frac{1}{9}+\frac{1}{25}+\ldots+\frac{1}{(2 N+1)^2}\right\}$
- **(D)** $4\left\{1+\frac{1}{9}+\frac{1}{25}+\ldots+\frac{1}{(2 N+1)^2}\right\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-4\left\{1+\frac{1}{9}+\frac{1}{25}+\ldots+\frac{1}{(2 N-1)^2}\right\}$**

**Detailed Solution:**

Since, $\quad f(x)=e^{g(x)}$
$$
\begin{aligned}
\Rightarrow \quad e^{g(x+1)} & =f(x+1) \\
& =x f(x) \\
& =x e^{g(x)}
\end{aligned}
$$
and
$$
g(x+1)=\log x+g(x)
$$
$$
\Rightarrow \quad g(x+1)-g(x)=\log x
$$
Replacing $x$ by $x-\frac{1}{2}$, we get
$$
\begin{aligned}
g\left(x+\frac{1}{2}\right)-g\left(x-\frac{1}{2}\right) & =\log \left(x-\frac{1}{2}\right)=\log (2 x-1)-\log 2 \\
\therefore g^{\prime \prime}\left(x+\frac{1}{2}\right)-g^{\prime \prime}\left(x-\frac{1}{2}\right) & =-\frac{4}{(2 x-1)^2}
\end{aligned}
$$
Substituting, $x=1,2,3, \ldots, N$ in Eq. (ii) and adding, we get
$$
g^{\prime \prime}\left(N+\frac{1}{2}\right)-g^{\prime \prime}\left(\frac{1}{2}\right)=-4\left\{1+\frac{1}{9}+\frac{1}{25}+\ldots+\frac{1}{(2 N-1)^2}\right\} .
$$

</details>

---

