# JEE Main Mathematics - Limits

## Topic 6: Miscellaneous

**Total Questions:** 27

---

### Q1. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\lim _{x \rightarrow 0} \frac{\mathrm{e}^{(\mathrm{a}-1) x}+2 \cos \mathrm{~b} x+(\mathrm{c}-2) \mathrm{e}^{-x}}{x \cos x-\log _{\mathrm{e}}(1+x)}=2$, then $\mathrm{a}^{2}+\mathrm{b}^{2}+\mathrm{c}^{2}$ is equal to :

**Options:**

- **(A)** 5
- **(B)** 9
- **(C)** 3
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 7**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{\left(1+(a-1) x+\frac{(a-1)^2 x^2}{2!}\right)+2\left(1-\frac{b^2 x^2}{2!}\right)+(c-2)\left(1-x+\frac{x^2}{2!}\right)}{x\left(1-\frac{x^2}{2!}\right)-\left(x-\frac{x^2}{2} \ldots\right)}=2$
$\lim _{x \rightarrow 0} \frac{(1+2+c-2)+x(a-1-c+2)+x^2\left(\frac{(a-1)^2}{2}-b^2+\left(\frac{c-2}{2}\right)\right)}{\frac{x^2}{2}-\frac{x^3}{2!}+\ldots}=2$
For which
$\because c+1=0 \Rightarrow c=-1$
$\because a-c=-1 \Rightarrow a=-2$
$\because \frac{(a-1)^2}{2}-b^2+\left(\frac{c-2}{2}\right)=1$
$\frac{9}{2}-b^2-\frac{3}{2}=1 \Rightarrow b^2=2$
$a^2+b^2+c^2=4+2+1=7$

</details>

---

### Q2. JEE Main 2026 (21 January Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $[\cdot]$ denote the greatest integer function and $f(x)=\lim _{\mathrm{n} \rightarrow \infty} \frac{1}{\mathrm{n}^{3}} \sum_{\mathrm{k}=1}^{\mathrm{n}}\left[\frac{\mathrm{k}^{2}}{3^{x}}\right]$. Then $12 \sum_{\mathrm{j}=1}^{\infty} f(\mathrm{j})$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

Let [·] denote the greatest integer function. We have $f(x) = \lim_{n \to \infty} \frac{1}{n^3} \sum_{k=1}^n [\frac{k^2}{3^x}]$.
For large $n$: $\sum_{k=1}^n [\frac{k^2}{3^x}] \approx \sum_{k=1}^n \frac{k^2}{3^x} = \frac{1}{3^x} \cdot \frac{n(n+1)(2n+1)}{6} \approx \frac{n^3}{3 \cdot 3^x}$
Therefore: $f(x) = \lim_{n \to \infty} \frac{1}{n^3} \cdot \frac{n^3}{3 \cdot 3^x} = \frac{1}{3^{x+1}}$
Computing the infinite series:
$\sum_{j=1}^\infty f(j) = \sum_{j=1}^\infty \frac{1}{3^{j+1}} = \frac{1}{3^2} + \frac{1}{3^3} + \frac{1}{3^4} + \cdots$
$= \frac{1}{9} \cdot (1 + \frac{1}{3} + \frac{1}{9} + \cdots) = \frac{1}{9} \cdot \frac{1}{1 - 1/3} = \frac{1}{9} \cdot \frac{3}{2} = \frac{1}{6}$
Therefore: $12 \sum_{j=1}^\infty f(j) = 12 \cdot \frac{1}{6} = 2$

</details>

---

### Q3. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\quad \lim _{x \rightarrow 1^{+}} \frac{(x-1)(6+\lambda \cos (x-1))+\mu \sin (1-x)}{(x-1)^3}=-1$, where $\lambda, \mu \in \mathbb{R}$, then $\lambda+\mu$ is equal to

**Options:**

- **(A)** 18
- **(B)** 20
- **(C)** 19
- **(D)** 17

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 18**

**Detailed Solution:**

$\begin{aligned} & \text { Put } x=1+h \\ & \lim _{h \rightarrow 0} \frac{h(6+\lambda \cosh )-\mu \sinh }{h^3}=-1 \\ & \lim _{h \rightarrow 0} \frac{h\left(6+\lambda\left(1-\frac{h^2}{2!}\right)\right)-\mu\left(h-\frac{h^3}{3!}\right)}{h^3}=-1 \\ & 6+\lambda-\mu=0 \text { and }-\frac{\lambda}{2}+\frac{\mu}{6}=-1 \\ & \lambda+\mu=18\end{aligned}$

</details>

---

### Q4. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\lim _{x \rightarrow 0} \frac{\cos (2 x)+a \cos (4 x)-b}{x^4}$ is finite, then $(a+b)$ is equal to :

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $0$
- **(C)** $\frac{3}{4}$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{\cos 2 x+a \cos 4 x-b}{x^4}=$ finite
$\begin{aligned} & L=\frac{\left\{1-\frac{(2 x)^2}{\underline{2}}+\frac{(2 x)^4}{\underline{4} \cdots\}\}+a\left\{1-\frac{(4 x)^2}{\underline{2}}+\frac{(4 x)^4}{\lfloor 4} \ldots \cdot\right\}-b}\right.}{x^4} \\ & L=\frac{(1+a-b)-x^2(2+8 a)+x^4\left(\frac{2}{3}+\frac{32}{3} a\right)+x^6() \ldots}{x^4}\end{aligned}$
$\begin{aligned} & \therefore 1+\mathrm{a}-\mathrm{b}=0 \text { and } 2+8 \mathrm{a}=0 \Rightarrow \mathrm{a}=-\frac{1}{4} \\ & \mathrm{~b}=\mathrm{a}+1 \\ & =-\frac{1}{4}+1=\frac{3}{4} \\ & \therefore \mathrm{a}+\mathrm{b}=-\frac{1}{4}+\frac{3}{4}=\frac{1}{2}\end{aligned}$

</details>

---

### Q5. JEE Main 2025 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let [t] be the greatest integer less than or equal to t. Then the least value of \(\mathrm{p} \in \mathbf{N}\) for which \(\lim _{x \rightarrow 0^{+}}\left(x\left(\left[\frac{1}{x}\right]+\left[\frac{2}{x}\right]+\ldots+\left[\frac{\mathrm{p}}{x}\right]\right)-x^2\left(\left[\frac{1}{x^2}\right]+\left[\frac{2^2}{x^2}\right]+\ldots+\left[\frac{9^2}{x^2}\right]\right)\right) \geq 1\) is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **24**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0^{+}}\left(x\left(\left[\frac{1}{x}\right]+\left[\frac{2}{x}\right]+\ldots . .+\left[\frac{p}{x}\right]\right)-x^2\left(\left[\frac{1}{x^2}\right]+\left[\frac{2^2}{x^2}\right]+\left[\frac{9^2}{x^2}\right]\right)\right) \geq 1 \\ & \quad(1+2+\ldots \ldots+p)-\left(1^2+2^2+\ldots 9^2\right) \geq 1\end{aligned}$


$\begin{aligned}
& \frac{p(p+1)}{2}-\frac{9.10 .19}{6} \geq 1 \\
& p(p+1) \geq 572
\end{aligned}$

Least natural value of $p$ is 24

</details>

---

### Q6. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $\lim _{n \rightarrow \infty}\left(\frac{n}{\sqrt{n^4+1}}-\frac{2 n}{\left(n^2+1\right) \sqrt{n^4+1}}+\frac{n}{\sqrt{n^4+16}}-\frac{8 n}{\left(n^2+4\right) \sqrt{n^4+16}}\right.$ $\left.+\ldots+\frac{n}{\sqrt{n^4+n^4}}-\frac{2 n \cdot n^2}{\left(n^2+n^2\right) \sqrt{n^4+n^4}}\right)$ be $\frac{\pi}{k}$, using only the principal values of the inverse trigonometric functions. Then $\mathrm{k}^2$ is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **32**

**Detailed Solution:**

$\begin{aligned} & \sum_{\mathrm{r}=1}^{\infty} \frac{\mathrm{n}}{\sqrt{\mathrm{n}^4+\mathrm{r}^4}}-\frac{2 \mathrm{nr}^2}{\left(\mathrm{n}^2+\mathrm{r}^2\right) \sqrt{\mathrm{n}^4+\mathrm{r}^4}} \\ & \sum_{\mathrm{r}=1}^{\infty} \frac{\frac{1}{\mathrm{n}}}{\sqrt{1+\left(\frac{\mathrm{r}}{\mathrm{n}}\right)^4}}-\frac{2\left(\frac{1}{\mathrm{n}}\right)\left(\frac{\mathrm{r}}{\mathrm{n}}\right)^2}{\left(1+\left(\frac{\mathrm{r}}{\mathrm{n}}\right)^2\right) \sqrt{1+\left(\frac{\mathrm{r}}{\mathrm{n}}\right)^4}} \\ & \Rightarrow \int_0^1 \frac{\mathrm{dx}}{\sqrt{1+\mathrm{x}^4}}-\frac{2 \mathrm{x}^2 \mathrm{dx}}{\left(1+\mathrm{x}^2\right) \sqrt{1+\mathrm{x}^4}} \\ & \Rightarrow \int_0^1 \frac{1-\mathrm{x}^2}{\left(1+\mathrm{x}^2\right) \sqrt{1+\mathrm{x}^4}} d x \\ & \Rightarrow \int_0^1 \frac{\frac{1}{\mathrm{x}^2}-1}{\left(\mathrm{x}+\frac{1}{\mathrm{x}}\right) \sqrt{\mathrm{x}^2+\frac{1}{\mathrm{x}^2}}} \mathrm{dx}\end{aligned}$
$\begin{aligned} & \Rightarrow-\int_0^1 \frac{1-\frac{1}{x^2}}{\left(x+\frac{1}{x}\right) \sqrt{\left(x+\frac{1}{x}\right)^2-2}} d x \\ & x+\frac{1}{x}=t \Rightarrow 1-\frac{1}{x^2} d x=d t\end{aligned}$
$\begin{aligned} & \Rightarrow-\int_{\infty}^2 \frac{\mathrm{dt}}{\mathrm{t} \sqrt{\mathrm{t}^2-2}} \\ & \Rightarrow-\int_{\infty}^2 \frac{\mathrm{tdt}}{\mathrm{t}^2 \sqrt{\mathrm{t}^2-2}} \\ & \text { take } \mathrm{t}^2-2=\alpha^2 \\ & \mathrm{tdt}=\alpha \mathrm{d} \alpha \\ & \Rightarrow-\int_{\infty}^{\sqrt{2}} \frac{\alpha \mathrm{d} \alpha}{\left(\alpha^2+2\right) \alpha} \\ & \Rightarrow-\int_{\infty}^{\sqrt{2}} \frac{\mathrm{d} \alpha}{\alpha^2+2}\end{aligned}$
$\begin{aligned}
& \left.\Rightarrow \frac{-1}{\sqrt{2}} \tan ^{-1} \frac{\alpha}{\sqrt{2}}\right]_{\infty}^{\sqrt{2}} \\
& \Rightarrow \frac{-1}{\sqrt{2}}\left\{\tan ^{-1} 1\right\}+\frac{1}{\sqrt{2}} \tan ^{-1} \infty \\
& \Rightarrow \frac{1}{\sqrt{2}}\left\{\frac{\pi}{2}-\frac{\pi}{4}\right\} \\
& \Rightarrow \frac{\pi}{4 \sqrt{2}}=\frac{\pi}{\mathrm{K}}
\end{aligned}$
So $\mathrm{K}=4 \sqrt{2}$
$\mathrm{K}^2=32$

</details>

---

### Q7. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\lim _{n \rightarrow \infty} \frac{\left(1^2-1\right)(n-1)+\left(2^2-2\right)(n-2)+\cdots+\left((n-1)^2-(n-1)\right) \cdot 1}{\left(1^3+2^3+\cdots \cdots+n^3\right)-\left(1^2+2^2+\cdots \cdots+n^2\right)}$ is equal to :

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{3}{4}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{3}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{n \rightarrow \infty} \frac{\sum_{r=1}^{n-1}\left(r^2-r\right)(n-r)}{\sum_{r=1}^n r^3-\sum_{r=1}^n r^2} \\ & \lim _{\mathrm{n} \rightarrow \infty} \frac{\sum_{\mathrm{r}=1}^{\mathrm{n}-1}\left(-\mathrm{r}^3+\mathrm{r}^2(\mathrm{n}+1)-\mathrm{nr}\right)}{\left(\frac{\mathrm{n}(\mathrm{n}+1)}{2}\right)^2-\frac{\mathrm{n}(\mathrm{n}+1)(2 \mathrm{n}+1)}{6}} \\ & \lim _{n \rightarrow \infty} \frac{\left(\frac{((n-1) n)}{2}\right)^2+\frac{(n+1)(n-1) n(2 n-1)}{6}-\frac{n^2(n-1)}{2}}{\frac{n(n+1)}{2}\left(\frac{n(n+1)}{2}-\frac{2 n+1}{3}\right)} \\ & \lim _{n \rightarrow \infty} \frac{\frac{n(n-1)}{2}\left(\frac{-n(n-1)}{2}+\frac{(n+1)(2 n-1)}{3}-n\right)}{\frac{n(n+1)}{2} \frac{3 n^2+3 n-4 n-2}{6}} \\ & \lim _{n \rightarrow \infty} \frac{(n-1)\left(-3 n^2+3 n+2\left(2 n^2+n-1\right)-6\right)}{(n+1)\left(3 n^2-n-2\right)} \\ & \lim _{n \rightarrow \infty} \frac{(n-1)\left(n^2+5 n-8\right)}{(n+1)\left(3 n^2-n-2\right)}=\frac{1}{3} \\ & \end{aligned}$

</details>

---

### Q8. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $f:(-\infty, \infty)-\{0\} \rightarrow \mathbb{R}$ be a differentiable function such that $f^{\prime}(1)=\lim _{a \rightarrow \infty} a^2 f\left(\frac{1}{a}\right)$. Then $\lim _{a \rightarrow \infty} \frac{a(a+1)}{2} \tan ^{-1}\left(\frac{1}{a}\right)+a^2-2 \log _e a$ is equal to

**Options:**

- **(A)** $\frac{3}{2}+\frac{\pi}{4}$
- **(B)** $\frac{3}{4}+\frac{\pi}{8}$
- **(C)** $\frac{3}{8}+\frac{\pi}{4}$
- **(D)** $\frac{5}{2}+\frac{\pi}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{5}{2}+\frac{\pi}{8}$**

**Detailed Solution:**

$\begin{aligned} & f:(-\infty, \infty)-\{0\} \rightarrow R \\ & f^{\prime}(1)=\lim _{a \rightarrow \infty} a^2 f\left(\frac{1}{a}\right) \\ & \lim _{a \rightarrow \infty} \frac{a(a+1)}{2} \tan ^{-1}\left(\frac{1}{a}\right)+a^2-2 \ln (a) \\ & \lim _{a \rightarrow \infty} a^2\left(\frac{\left(1+\frac{1}{a}\right)}{2} \tan ^{-1}\left(\frac{1}{a}\right)+1-\frac{2}{a^2} \ln (a)\right) \\ & f(x)=\frac{1}{2}(1+x) \tan ^{-1}(x)+1-2 x^2 \ln (x)\end{aligned}$
$\begin{aligned}
& \mathrm{f}^{\prime}(\mathrm{x})=\frac{1}{2}\left(\frac{1+\mathrm{x}}{1+\mathrm{x}^2}+\tan ^{-1}(\mathrm{x})+4 \mathrm{x} \ell(\mathrm{x})\right)+2 \mathrm{x} \\
& \mathrm{f}^{\prime}(1)=\frac{1}{2}\left(1+\frac{\pi}{4}\right)+2 \\
& \mathrm{f}^{\prime}(1)=\frac{5}{2}+\frac{\pi}{8}
\end{aligned}$

</details>

---

### Q9. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)=\int_0^x\left(t+\sin \left(1-e^{\prime}\right)\right) d t, x \in \mathbb{R}$. Then, $\lim _{x \rightarrow 0} \frac{f(x)}{x^3}$ is equal to

**Options:**

- **(A)** $-\frac{1}{6}$
- **(B)** $\frac{2}{3}$
- **(C)** $-\frac{2}{3}$
- **(D)** $\frac{1}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\frac{1}{6}$**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{f(x)}{x^3}$
Using L Hopital Rule.
$\lim _{x \rightarrow 0} \frac{f^{\prime}(x)}{3 x^2}=\lim _{x \rightarrow 0} \frac{x+\sin \left(1-e^x\right)}{3 x^2}$ (Again L Hopital)
Using L.H. Rule
$\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{-\left[\sin \left(1-e^x\right)\left(-e^x\right) \cdot e^x+\cos \left(1-e^x\right) \cdot e^x\right]}{6} \\
& =-\frac{1}{6}
\end{aligned}$

</details>

---

### Q10. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mi>x</mi></msup><mo>−</mo><mi>b</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **81**

**Detailed Solution:**

<p>Given: </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mi>b</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mi>b</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>·</mo><mi>x</mi><mo>·</mo><mstyle displaystyle="true"><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mstyle></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mi>x</mi><mrow><mn>1</mn><mo>!</mo></mrow></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac></mstyle><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>-</mo><mi>b</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mstyle><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>+</mo><mi>c</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>x</mi><mrow><mn>1</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>×</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>+</mo><mfrac><mi>b</mi><mn>2</mn></mfrac><mo>-</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>-</mo><mfrac><mi>c</mi><mn>2</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mfrac><mi>c</mi><mn>2</mn></mfrac></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>-</mo><mfrac><mi>b</mi><mn>3</mn></mfrac><mo>+</mo><mfrac><mi>c</mi><mn>2</mn></mfrac><mo>=</mo><mn>1</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>c</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>c</mi><mn>3</mn></mfrac><mo>+</mo><mfrac><mi>c</mi><mn>2</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>2</mn><mi>c</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>16</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>16</mn><mfenced><mrow><mfrac><mn>9</mn><mn>16</mn></mfrac><mo>+</mo><mfrac><mn>9</mn><mn>4</mn></mfrac><mo>×</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>16</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>81</mn></math></p>

</details>

---

### Q11. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> be the sum of all coefficients in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>–</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><msup><mo>)</mo><mn>2023</mn></msup><mo> </mo><mo>(</mo><mn>3</mn><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo> </mo><msup><mo>)</mo><mn>2024</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><mstyle displaystyle="true"><mfrac><mrow><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mrow><mrow><msup><mi>t</mi><mn>2024</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mstyle><mi>d</mi><mi>t</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></math>. If the equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>d</mi><mi>x</mi><mo>+</mo><mi>e</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> have a common root, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>,</mo><mo> </mo><mi>d</mi><mo>,</mo><mo> </mo><mi>e</mi><mo>∈</mo><mi>R</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo> </mo><mo>:</mo><mo> </mo><mi>c</mi><mo> </mo><mo>:</mo><mo> </mo><mi>e</mi></math> equals

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><mo>:</mo><mo> </mo><mn>1</mn><mo> </mo><mo>:</mo><mo> </mo><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo> </mo><mo>:</mo><mo> </mo><mn>1</mn><mo> </mo><mo>:</mo><mo> </mo><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo> </mo><mo>:</mo><mo> </mo><mn>2</mn><mo> </mo><mo>:</mo><mo> </mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo> </mo><mo>:</mo><mo> </mo><mn>1</mn><mo> </mo><mo>:</mo><mo> </mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo> </mo><mo>:</mo><mo> </mo><mn>1</mn><mo> </mo><mo>:</mo><mo> </mo><mn>4</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is the sum of all coefficients in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mpadded voffset="-1px"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mpadded></mrow></mfenced><mn>2023</mn></msup><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mn>2024</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mo>×</mo><mn>1</mn><mo>+</mo><mpadded voffset="-1px"><mn>2</mn><mo>×</mo><mn>1</mn></mpadded></mrow></mfenced><mn>2023</mn></msup><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>4</mn><mo>×</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>×</mo><mn>1</mn></mrow></mfenced><mn>2024</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>1</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><mstyle displaystyle="true"><mfrac><mrow><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mrow><mrow><msup><mi>t</mi><mn>2024</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mstyle><mi>d</mi><mi>t</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p><p>Using L-Hospital's rule and Newton Leibnitz Theorem, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>b</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mfenced><mrow><msup><mi>x</mi><mn>2024</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>b</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mn>1</mn><mrow><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2024</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>b</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>, which gives complex conjugates as roots.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo> </mo><mtext>and</mtext><mo> </mo><menclose notation="top"><mi>α</mi></menclose></math> be those roots.</p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>d</mi><mi>x</mi><mo>+</mo><mi>e</mi><mo>=</mo><mn>0</mn></math> will also have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo> </mo><mtext>and</mtext><mo> </mo><menclose notation="top"><mi>α</mi></menclose></math> as roots.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mo>:</mo><mi>c</mi><mo>:</mo><mi>e</mi><mo>=</mo><mn>1</mn><mo>:</mo><mn>1</mn><mo>:</mo><mn>4</mn></math></p>

</details>

---

### Q12. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>e</mi><mrow><mn>2</mn><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow></msup><mo>-</mo><mn>2</mn><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p>

**Options:**

- **(A)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(B)** does not exist
- **(C)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>e</mi><mrow><mn>2</mn><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow></msup><mo>-</mo><mn>2</mn><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p><p>Now, using the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mrow><mn>1</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>∞</mo></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mfenced close="|" open="|"><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mn>1</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><msup><mfenced close="|" open="|"><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>∞</mo></mrow></mfenced><mo>-</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfrac><msup><mfenced close="|" open="|"><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><msup><mfenced close="|" open="|"><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>∞</mo></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mfrac><msup><mfenced close="|" open="|"><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>∞</mo></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo> </mo><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mtext> and other terms will become zero</mtext></mrow></mfenced></math></p>

</details>

---

### Q13. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow></mfenced><mo>→</mo><mi>R</mi></math> be a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>, If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>x</mi><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>α</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msup><mi>α</mi><mn>2</mn></msup></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>x</mi><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>x</mi><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi></mrow><mrow><mfenced><mfrac><mrow><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mo>-</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mo>×</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup><mo>-</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msubsup><mo>∫</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>d</mi><mi>t</mi></mrow><mi>x</mi></mfrac><mo>  </mo></math></p><p>Applying L-hospital's rule and Newton Leibnitz Theorem we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></math></p><p>It is given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>8</mn><msup><mi>α</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q14. JEE Main 2024 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the slope of the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><mfrac><mrow><mn>9</mn><msub><mi>r</mi><mn>2</mn></msub></mrow><mn>2</mn></mfrac></math> for some <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub><mo>,</mo><mo>  </mo><msub><mi>r</mi><mn>2</mn></msub><mo>∈</mo><mi>R</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>3</mn></mrow></munder><mfenced><mrow><msubsup><mo>∫</mo><mn>3</mn><mi>x</mi></msubsup><mfrac><mrow><mn>8</mn><msup><mi>t</mi><mn>2</mn></msup></mrow><mrow><mfrac><mrow><mn>3</mn><msub><mi>r</mi><mn>2</mn></msub><mi>x</mi></mrow><mn>2</mn></mfrac><mo>-</mo><msub><mi>r</mi><mn>2</mn></msub><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msub><mi>r</mi><mn>1</mn></msub><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfrac><mi>d</mi><mi>t</mi></mrow></mfenced></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<p>We know that,</p><p>The slope of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mi>x</mi><mo>+</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>9</mn></math></p><p>Now, given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><mfrac><mrow><mn>9</mn><msub><mi>r</mi><mn>2</mn></msub></mrow><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p>Now, solving</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>3</mn></mrow></munder><mfrac><mrow><msubsup><mo>∫</mo><mn>3</mn><mi>x</mi></msubsup><mn>8</mn><msup><mi>t</mi><mn>2</mn></msup><mi>d</mi><mi>t</mi></mrow><mrow><mfrac><mrow><mn>3</mn><msub><mi>r</mi><mn>2</mn></msub><mi>x</mi></mrow><mn>2</mn></mfrac><mo>-</mo><msub><mi>r</mi><mn>2</mn></msub><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msub><mi>r</mi><mn>1</mn></msub><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfrac></math></p><p>Applying Newton Leibnitz Theorem and L'Hospital Rule we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>3</mn></mrow></munder><mfrac><mrow><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mfrac><mrow><mn>3</mn><msubsup><mi>r</mi><mn>2</mn><mrow></mrow></msubsup></mrow><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><msub><mi>r</mi><mn>2</mn></msub><mi>x</mi><mo>-</mo><mn>3</mn><msub><mi>r</mi><mn>1</mn></msub><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>L</mi><mo>=</mo><mfrac><mn>72</mn><mrow><mfrac><mrow><mn>3</mn><msub><mi>r</mi><mn>2</mn></msub></mrow><mn>2</mn></mfrac><mo>-</mo><mn>6</mn><msub><mi>r</mi><mn>2</mn></msub><mo>-</mo><mn>27</mn><msub><mi>r</mi><mn>1</mn></msub><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>L</mi><mo>=</mo><mfrac><mn>72</mn><mrow><mo>-</mo><mfrac><mrow><mn>9</mn><msub><mi>r</mi><mn>2</mn></msub></mrow><mn>2</mn></mfrac><mo>-</mo><mn>27</mn><msub><mi>r</mi><mn>1</mn></msub><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><mfrac><mrow><mn>9</mn><msub><mi>r</mi><mn>2</mn></msub></mrow><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mn>9</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>L</mi><mo>=</mo><mfrac><mn>72</mn><mrow><mn>9</mn><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mn>12</mn></math></p>

</details>

---

### Q15. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow></munder><mfenced><mrow><mfrac><mn>1</mn><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup></mfrac><msubsup><mo>∫</mo><msup><mi>x</mi><mn>3</mn></msup><msup><mfenced><mfrac><mi>π</mi><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></msubsup><mi>cos</mi><mfenced><mfrac><mn>1</mn><msup><mi>t</mi><mn>3</mn></msup></mfrac></mfenced><mi>d</mi><mi>t</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>π</mi></mrow><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msup><mi>π</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msup><mi>π</mi><mn>2</mn></msup></mrow><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>π</mi></mrow><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msup><mi>π</mi><mn>2</mn></msup></mrow><mn>8</mn></mfrac></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow></munder><mfrac><mrow><msubsup><mo>∫</mo><msup><mi>x</mi><mn>3</mn></msup><mstyle displaystyle="true"><msup><mfenced><mfrac><mi>π</mi><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></mstyle></msubsup><mi>cos</mi><msup><mi>t</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup><mi>d</mi><mi>t</mi></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mi>π</mi><mn>2</mn></mfrac></mstyle></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msubsup><mo>∫</mo><msup><mfenced><mstyle displaystyle="true"><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>-</mo><mi>h</mi></mstyle></mfenced><mn>3</mn></msup><mstyle displaystyle="true"><msup><mfenced><mfrac><mi>π</mi><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></mstyle></msubsup><mi>cos</mi><msup><mi>t</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup><mi>d</mi><mi>t</mi></mrow><msup><mfenced><mstyle displaystyle="true"><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>-</mo><mi>h</mi><mo>-</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mstyle></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><msubsup><mo>∫</mo><msup><mfenced><mstyle displaystyle="true"><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>-</mo><mi>h</mi></mstyle></mfenced><mn>3</mn></msup><mstyle displaystyle="true"><msup><mfenced><mfrac><mi>π</mi><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></mstyle></msubsup><mi>cos</mi><msup><mi>t</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup><mi>d</mi><mi>t</mi></mrow><msup><mi>h</mi><mn>2</mn></msup></mfrac></mfenced></math></p><p>Applying L-Hospital's rule and Newton Leibnitz Theorem we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mn>0</mn><mo>+</mo><mi>cos</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>-</mo><mi>h</mi></mstyle></mfenced><mo>×</mo><mn>3</mn><mo>×</mo><msup><mfenced><mrow><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>-</mo><mi>h</mi></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>h</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mi>sin</mi><mstyle displaystyle="true"><mi>h</mi></mstyle><mo>×</mo><mn>3</mn><mo>×</mo><msup><mfenced><mrow><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>-</mo><mi>h</mi></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>h</mi></mrow></mfrac></mfenced></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mi>sin</mi><mi>h</mi></mrow><mi>h</mi></mfrac></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mn>3</mn><mo>×</mo><msup><mfenced><mrow><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>-</mo><mi>h</mi></mrow></mfenced><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>3</mn><msup><mi>π</mi><mn>2</mn></msup></mrow><mn>8</mn></mfrac></math></p>

</details>

---

### Q16. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>3</mn><mo>+</mo><mi>α</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>β</mi><mi>cos</mi><mi>x</mi><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>)</mo></mrow><mrow><mn>3</mn><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>α</mi><mo>-</mo><mi>β</mi></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>3</mn><mo>+</mo><mi>αsinx</mi><mo>+</mo><mi>βcosx</mi><mo>+</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mo>(</mo><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi><mo>)</mo></mrow><mrow><mn>3</mn><msup><mi>tan</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>3</mn><mo>+</mo><mi mathvariant="normal">α</mi><mfenced close="]" open="["><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mfrac><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>…</mo></mrow></mfenced><mo>+</mo><mi mathvariant="normal">β</mi><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mfrac><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><msup><mi mathvariant="normal">x</mi><mn>4</mn></msup><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>…</mo></mrow></mfenced><mo>+</mo><mfenced><mrow><mo>-</mo><mi mathvariant="normal">x</mi><mo>-</mo><mfrac><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>…</mo></mrow></mfenced></mrow><mrow><mn>3</mn><msup><mi>tan</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mo>(</mo><mn>3</mn><mo>+</mo><mi mathvariant="normal">β</mi><mo>)</mo><mo>+</mo><mo>(</mo><mi mathvariant="normal">α</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi mathvariant="normal">x</mi><mo>+</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mi mathvariant="normal">β</mi><mn>2</mn></mfrac></mrow></mfenced><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mo>…</mo><mo>.</mo></mrow><mrow><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfrac><mo>×</mo><mfrac><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>The coefficient of all the powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi></math> except <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">β</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal">α</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mi mathvariant="normal">β</mi><mn>2</mn></mfrac></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">β</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mi mathvariant="normal">α</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi mathvariant="normal">α</mi><mo>-</mo><mi mathvariant="normal">β</mi><mo>=</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q17. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>e</mi><mrow><mi>a</mi><mi>x</mi></mrow></msup><mo>-</mo><mi>cos</mi><mo>(</mo><mi>b</mi><mi>x</mi><mo>)</mo><mo>-</mo><mfrac><mrow><mi>c</mi><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>c</mi><mi>x</mi></mrow></msup></mrow><mn>2</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mo>(</mo><mn>2</mn><mi>x</mi><mo>)</mo></mrow></mfrac><mo>=</mo><mn>17</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>68</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>76</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>68</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>e</mi><mrow><mi>a</mi><mi>x</mi></mrow></msup><mo>-</mo><mi>cos</mi><mo>(</mo><mi>b</mi><mi>x</mi><mo>)</mo><mo>-</mo><mfrac><mrow><mi>c</mi><mi>x</mi></mrow><mn>2</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>c</mi><mi>x</mi></mrow></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mn>17</mn></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mi>a</mi><mi>x</mi></mrow></msup><mo>=</mo><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mfrac><mrow><mo>(</mo><mi>a</mi><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><mi>b</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mo>(</mo><mi>b</mi><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mfrac><msup><mfenced><mrow><mi>a</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><msup><mfenced><mrow><mi>b</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>-</mo><mfrac><mrow><mi>c</mi><mi>x</mi></mrow><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfenced><mrow><mi>c</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mfrac><msup><mfenced><mrow><mi>c</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mo>&#8230;</mo></mrow></mfenced></mrow><mrow><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac></mfenced><mo>&#215;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mi>a</mi><mo>-</mo><mfrac><mi>c</mi><mn>2</mn></mfrac></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo></mrow><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>17</mn></math></p><p>Now for limit to exist, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mfrac><mi>c</mi><mn>2</mn></mfrac><mo>=</mo><mn>0</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>2</mn><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo></mrow><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>=</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mn>68</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>68</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q18. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced close="}" open="{"><mrow><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfenced><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>5</mn></mfrac></msup></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msup></mrow></mfenced></mrow></mfenced></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced close="}" open="{"><mrow><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfenced><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>5</mn></mfrac></msup></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msup></mrow></mfenced></mrow></mfenced></math></p><p>Now,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>5</mn></mfrac></msup><mo>&#60;</mo><mn>1</mn></math></p><p>--------------------</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msup><mo>&#60;</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8704;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfenced><mi>n</mi></msup><mo>&#60;</mo><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfenced><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>5</mn></mfrac></msup></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msup></mrow></mfenced><mo>&#60;</mo><msup><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msup></mrow></mfenced><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfenced><mi>n</mi></msup><mo>&#60;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced close="}" open="{"><mrow><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfenced><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>5</mn></mfrac></msup></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msup></mrow></mfenced></mrow></mfenced><mo>&#60;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msup></mrow></mfenced><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfenced><mi>n</mi></msup><mo>&#60;</mo><mi>L</mi><mo>&#60;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msup></mrow></mfenced><mi>n</mi></msup></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msup></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><mo>&#160;</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>&#60;</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msup><mo>&#60;</mo><mn>1</mn><mo>&#160;</mo></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced close="}" open="{"><mrow><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfenced><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mn>5</mn></mfrac></msup></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msup></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p></blockquote>

</details>

---

### Q19. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><msup><mfenced><mrow><msqrt><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><msqrt><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup><mo>+</mo><msup><mfenced><mrow><msqrt><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><msqrt><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup></mrow><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup></mrow></mfrac><msup><mi>x</mi><mn>3</mn></msup></math>

**Options:**

- **(A)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>27</mn><mn>2</mn></mfrac></math>
- **(B)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** does not exist
- **(D)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi>lim</mi><mo>&#160;</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><msup><mfenced><mrow><msqrt><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><msqrt><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup><mo>+</mo><msup><mfenced><mrow><msqrt><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><msqrt><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup></mrow><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup></mrow></mfrac></math></p><p>We know the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mi>n</mi></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mi>n</mi></msup></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mi>n</mi></msup><msup><mi>b</mi><mn>0</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>b</mi><mn>1</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mn>0</mn></msup><msup><mi>b</mi><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mi>n</mi></msup><msup><mi>b</mi><mn>0</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>b</mi><mn>1</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mn>0</mn></msup><msup><mi>b</mi><mi>n</mi></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mn>6</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mn>6</mn></msup><mo>=</mo><mn>2</mn><mfenced><mrow><msub><mi>T</mi><mn>1</mn></msub><mo>+</mo><msub><mi>T</mi><mn>3</mn></msub><mo>+</mo><msub><mi>T</mi><mn>5</mn></msub><mo>+</mo><msub><mi>T</mi><mn>7</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mi>a</mi><mn>6</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mi>a</mi><mn>4</mn></msup><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mmultiscripts><mi>c</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mi>a</mi><mn>2</mn></msup><msup><mi>b</mi><mn>4</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mi>b</mi><mn>6</mn></msup></mrow></mfenced></math></p><p>From equation (1) we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi>lim</mi><mo>&#160;</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mfenced><mrow><mn>2</mn><msup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>30</mn><msup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>30</mn><mfenced><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mrow></mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>6</mn></msup><mo>+</mo><mn>30</mn><msup><mi>x</mi><mn>4</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>30</mn><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><msup><mi>x</mi><mn>6</mn></msup><mfenced close="" open="["><mrow><mn>2</mn><msup><mfenced><mrow><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>30</mn><msup><mfenced><mrow><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mn>3</mn><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>+</mo><mn>30</mn><mfenced><mrow><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mn>3</mn></msup></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn>6</mn></msup><mfenced close="" open="["><mrow><mn>2</mn><mo>+</mo><mn>30</mn><mfenced close="]"><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mstyle><mo>+</mo><mn>30</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mstyle></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mstyle></mrow></mfenced><mn>3</mn></msup></mrow></mfenced></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mfenced><mn>3</mn></mfenced><mn>3</mn></msup><mo>+</mo><mn>30</mn><msup><mfenced><mn>3</mn></mfenced><mn>3</mn></msup><mo>+</mo><mn>30</mn><msup><mfenced><mn>3</mn></mfenced><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mn>3</mn></mfenced><mn>3</mn></msup></mrow><mrow><mn>2</mn><mo>+</mo><mn>30</mn><mo>+</mo><mn>30</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><msup><mfenced><mn>3</mn></mfenced><mn>3</mn></msup><mo>=</mo><mn>27</mn></math></p>

</details>

---

### Q20. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>&#945;</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>&#946;</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>&#947;</mi><mi>sin</mi><mi>x</mi></mrow><mrow><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi><mo>&#8712;</mo><mi>R</mi></math>, then which of the following is NOT correct?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#947;</mi><mn>2</mn></msup><mo>=</mo><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>+</mo><mi>&#946;</mi><mi>&#947;</mi><mo>+</mo><mi>&#947;</mi><mi>&#945;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mi>&#946;</mi><msup><mi>&#947;</mi><mn>2</mn></msup><mo>+</mo><mi>&#947;</mi><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#947;</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mi>&#946;</mi><msup><mi>&#947;</mi><mn>2</mn></msup><mo>+</mo><mi>&#947;</mi><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>&#945;</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>&#946;</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>&#947;</mi><mi>sin</mi><mi>x</mi></mrow><mrow><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>&#945;</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>&#946;</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>&#947;</mi><mi>sin</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><mstyle displaystyle="true"><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mstyle></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>&#945;</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>&#946;</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>&#947;</mi><mi>sin</mi><mi>x</mi></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>Now using expansion of given function in terms of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>&#945;</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>+</mo><mi>&#946;</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>+</mo><mi>&#947;</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac></math></p><p>Now for limit to exist constant terms should be zero</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Also coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> should be zero</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Also coefficient  of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup></math> should be zero</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#945;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#946;</mi><mn>2</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>So limit becomes, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup><mfenced><mrow><mfrac><mi>&#945;</mi><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mfrac><mi>&#946;</mi><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mfrac><mi>&#947;</mi><mrow><mn>3</mn><mo>!</mo></mrow></mfrac></mrow></mfenced><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup><mfenced><mrow><mfrac><mi>&#945;</mi><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mfrac><mi>&#946;</mi><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mfrac><mi>&#947;</mi><mrow><mn>3</mn><mo>!</mo></mrow></mfrac></mrow></mfenced></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>Now putting the value of limit we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mn>6</mn></mfrac><mo>-</mo><mfrac><mi>&#946;</mi><mn>6</mn></mfrac><mo>-</mo><mfrac><mi>&#947;</mi><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>Now on solving equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>4</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Now putting these in all option we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mi>&#946;</mi><msup><mi>&#947;</mi><mn>2</mn></msup><mo>+</mo><mi>&#947;</mi><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p></blockquote>

</details>

---

### Q21. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></math> are the distinct roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#946;</mi></mrow></munder><mfrac><mrow><msup><mi>e</mi><mrow><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced></mrow></msup><mo>-</mo><mn>1</mn><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced></mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mi>&#946;</mi><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>c</mi></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>c</mi></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>c</mi></mrow></mfenced></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#946;</mi></mrow></munder><mfrac><mrow><msup><mi>e</mi><mrow><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced></mrow></msup><mo>-</mo><mn>1</mn><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mspace linebreak="newline"/><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#946;</mi></mrow></munder><mfrac><mrow><mn>1</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>!</mo></mrow></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><msup><mn>2</mn><mn>2</mn></msup><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac></mstyle><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>-</mo><mn>1</mn><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mspace linebreak="newline"/><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#946;</mi></mrow></munder><mfrac><mrow><mn>2</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mn>2</mn></msup></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mspace linebreak="newline"/><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#946;</mi></mrow></munder><mfrac><mrow><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mspace linebreak="newline"/><mn>2</mn><msup><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>2</mn><mfenced><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>c</mi></mrow></mfenced></math>

</details>

---

### Q22. JEE Main 2021 (20 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mfrac><mrow><mi>&#945;</mi><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mi>&#946;</mi><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo><mo>+</mo><mi>&#947;</mi><msup><mi>x</mi><mn>2</mn></msup><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mrow><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>&#8712;</mo><mi>R</mi></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></math> is __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mfrac><mrow><mi>&#945;</mi><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mi>&#946;</mi><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo><mo>+</mo><mi>&#947;</mi><msup><mi>x</mi><mn>2</mn></msup><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mrow><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mfrac><mrow><mi>&#945;</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo></mstyle></mrow></mfenced><mo>-</mo><mi>&#946;</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mstyle><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>+</mo><mi>&#947;</mi><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac></mstyle><mo>-</mo><mo>.</mo><mo>.</mo></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mstyle></mfenced></mrow></mfrac></mfenced><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="[" close="]"><mfrac><mrow><mi>&#945;</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mstyle></mrow></mfenced><mo>-</mo><mi>&#946;</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mstyle></mrow></mfenced><mo>+</mo><mi>&#947;</mi><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac></mfenced><mo>=</mo><mn>10</mn></math></p><p>Neglecting higher powers.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>x</mi><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mfrac><mi>&#946;</mi><mn>2</mn></mfrac><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mfenced><mrow><mfrac><mi>&#945;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>&#946;</mi><mn>3</mn></mfrac><mo>-</mo><mi>&#947;</mi></mrow></mfenced></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>=</mo><mn>10</mn></math></p><p>For limit to exist</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mfrac><mi>&#946;</mi><mn>2</mn></mfrac><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>&#946;</mi><mn>3</mn></mfrac><mo>-</mo><mi>&#947;</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mi>&#945;</mi><mo>,</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#945;</mi></mrow><mn>2</mn></mfrac></math></p><p>Putting in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>&#945;</mi><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>&#945;</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#945;</mi><mn>6</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>&#945;</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>&#945;</mi><mo>+</mo><mn>9</mn><mi>&#945;</mi></mrow><mn>6</mn></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>6</mn></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>6</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mn>6</mn><mo>,</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q23. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mrow><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>6</mn><mi>L</mi><mo>+</mo><mn>1</mn><mo>)</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mrow><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>&#8230;</mo></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>&#8230;</mo></mrow></mfenced></mrow><mrow><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>&#8230;</mo></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac><mo>&#8230;</mo></mrow></mfenced></mrow><mrow><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math> (Use L&#39;Hospital rule <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>0</mn><mn>0</mn></mfrac></math> form)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mfrac><mrow><mn>6</mn><mi>x</mi></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mfrac><mrow><mn>6</mn><mi>x</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced></mrow><mrow><mn>18</mn><mi>x</mi></mrow></mfrac></math>  (Use L&#39;Hospital rule <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>0</mn><mn>0</mn></mfrac></math> form)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mfrac><mn>6</mn><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mfrac><mn>6</mn><mn>3</mn></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced></mrow><mn>18</mn></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow><mn>18</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p>Given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mrow><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mi>L</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>=</mo><mi>L</mi><mo>&#8658;</mo><mn>6</mn><mi>L</mi><mo>=</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>L</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q24. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><mfenced close="]" open="["><mi>r</mi></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mi>r</mi></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced close="]" open="["><mrow><mi>n</mi><mi>r</mi></mrow></mfenced></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is non-zero real number and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>r</mi></mfenced></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>,</mo></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>r</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#8804;</mo><mfenced close="]" open="["><mi>r</mi></mfenced><mo>&#60;</mo><mi>r</mi><mo>+</mo><mn>1</mn></math><gwmw style="display:none;"></gwmw></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>r</mi><mo>&#8804;</mo><mfenced close="]" open="["><mrow><mn>2</mn><mi>r</mi></mrow></mfenced><mo>&#60;</mo><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>r</mi><mo>&#8804;</mo><mfenced close="]" open="["><mrow><mn>3</mn><mi>r</mi></mrow></mfenced><mo>&#60;</mo><mn>3</mn><mi>r</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>r</mi><mo>&#8804;</mo><mfenced close="]" open="["><mrow><mi>n</mi><mi>r</mi></mrow></mfenced><mo>&#60;</mo><mi>n</mi><mi>r</mi><mo>+</mo><mn>1</mn></math></p><p>On adding all the above inequalities, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>+</mo><mn>2</mn><mi>r</mi><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>n</mi><mi>r</mi><mo>&#8804;</mo><mfenced close="]" open="["><mi>r</mi></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mi>r</mi></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced close="]" open="["><mrow><mi>n</mi><mi>r</mi></mrow></mfenced><mo>&#60;</mo><mi>r</mi><mo>+</mo><mn>2</mn><mi>r</mi><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mi>n</mi><mi>r</mi><mo>+</mo><mi>n</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>&#183;</mo><mi>r</mi><mo>&#8804;</mo><mfenced close="]" open="["><mi>r</mi></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mi>r</mi></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced close="]" open="["><mrow><mi>n</mi><mi>r</mi></mrow></mfenced><mo>&#60;</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>&#183;</mo><mi>r</mi><mo>+</mo><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mstyle><mo>&#183;</mo><mi>r</mi></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac><mo>&#8804;</mo><mfrac><mrow><mfenced close="]" open="["><mi>r</mi></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mi>r</mi></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced close="]" open="["><mrow><mi>n</mi><mi>r</mi></mrow></mfenced></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac><mo>&#60;</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mstyle><mo>&#183;</mo><mi>r</mi><mo>+</mo><mi>n</mi></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>&#183;</mo><mi>r</mi></mrow><mrow><mn>2</mn><mo>&#183;</mo><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></mrow></mfenced><mo>&#183;</mo><mi>r</mi></mrow><mrow><mn>2</mn><mo>&#183;</mo><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mi>r</mi><mn>2</mn></mfrac></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><mstyle displaystyle="true"><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mstyle><mo>&#183;</mo><mi>r</mi><mo>+</mo><mi>n</mi></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></mrow></mfenced><mo>&#183;</mo><mi>r</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></mrow></mfenced></mrow><mrow><mn>2</mn><mo>&#183;</mo><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mi>r</mi><mn>2</mn></mfrac></math></p><p>So, by Sandwich Theorem, we can conclude that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><mfenced close="]" open="["><mi>r</mi></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mi>r</mi></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced close="]" open="["><mrow><mi>n</mi><mi>r</mi></mrow></mfenced></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mi>r</mi><mn>2</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q25. JEE Main 2021 (16 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mi>b</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mi>c</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mrow><mi>x</mi><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></math> is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mi>b</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mi>c</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mrow><mi>x</mi><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#8230;</mo></mrow></mfenced><mo>-</mo><mi>b</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>+</mo><mi>c</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac></mrow></mfenced></mrow><mrow><mfenced><mfrac><mrow><mi>x</mi><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mfenced><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#8230;</mo></mrow></mfenced><mo>-</mo><mi>b</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>+</mo><mi>c</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac></mrow></mfenced></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p>For the given limit to exist numerator should be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mtext>when&#160;</mtext><mi>x</mi><mo>&#8594;</mo><mn>0</mn><mo>.</mo></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math></p><p>Applying L&#39;Hospital&#39;s rule, we get </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#8230;</mo></mrow></mfenced><mo>-</mo><mi>b</mi><mfenced><mrow><mo>-</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>+</mo><mi>c</mi><mfenced><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn></math></p><p>Again, for the given limit to exist numerator should be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mtext>when</mtext><mo>&#160;</mo><mi>x</mi><mo>&#8594;</mo><mn>0</mn><mo>.</mo><mo>&#160;</mo></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Applying, L&#39;Hospital&#39;s rule, we get </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>-</mo><mi>b</mi><mfenced><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>+</mo><mi>c</mi><mfenced><mn>1</mn></mfenced></mrow><mn>2</mn></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q26. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `3`

Let $f: R \rightarrow R$ be a positive increasing function with $\lim _{x \rightarrow \infty} \frac{f(3 x)}{f(x)}=1$. Then $\lim _{x \rightarrow \infty} \frac{f(2 x)}{f(x)}=$

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{3}{2}$
- **(C)** 3
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

$f(x)$ is a positive increasing function
$$
\begin{aligned}
& \Rightarrow 0 < f(x) < f(2 x) < f(3 x) \\
& \Rightarrow 0 < 1 < \frac{f(2 x)}{f(x)} < \frac{f(3 x)}{f(x)} \\
& \Rightarrow \lim _{x \rightarrow \infty} 1 \leq \lim _{x \rightarrow \infty} \frac{f(2 x)}{f(x)} \leq \lim _{x \rightarrow \infty} \frac{f(3 x)}{f(x)}
\end{aligned}
$$
By sandwich theorem.
$$
\Rightarrow \lim _{x \rightarrow \infty} \frac{f(2 x)}{f(x)}=1
$$

</details>

---

### Q27. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `3`

$\lim _{n \rightarrow \infty} \sum_{r=1}^n \frac{1}{n} e^{\frac{-}{n}}$ is

**Options:**

- **(A)** e
- **(B)** $e-1$
- **(C)** $1-e$
- **(D)** $e+1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $e-1$**

**Detailed Solution:**

$\lim _{n \rightarrow \infty} \sum_{r=1}^n \frac{1}{n} e^{\frac{r}{n}}=\int_0^1 e^x d x=(e-1)$

</details>

---

