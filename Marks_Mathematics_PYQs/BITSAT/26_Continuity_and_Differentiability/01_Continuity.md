# BITSAT Mathematics - Continuity and Differentiability

## Topic 1: Continuity

**Total Questions:** 9

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `2`

Let $f$ be the function defined by
$f(x)=\left\{\begin{array}{cc}
\frac{x^2-1}{x^2-2|x-1|-1}, & x \neq 1 \\
\frac{1}{2}, & x=1
\end{array}\right.$

**Options:**

- **(A)** The function is continuous for all values of $x$
- **(B)** The function is continuous only for $x\gt1$
- **(C)** The function is continuous at $x=1$
- **(D)** The function is not continuous at $x=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The function is not continuous at $x=1$**

**Detailed Solution:**

$f(x)=\left\{\begin{array}{cc}\frac{x^2-1}{x^2-2 x+1} ; & x\gt1 \\ \frac{1}{2} \quad ; & x=1 \\ \frac{x^2-1}{x^2+2 x-3} ; & x \lt 1\end{array}\right.$
$\because \quad x^2+3 x-x-3$
$=x(x+3)-1(x+3)$
Lets Find
LHL, $\lim _{x \rightarrow 1^{-}} \frac{x^2-1}{x^2-2 x+1}$ and RHL, $\lim _{x \rightarrow 1^{+}} \frac{x^2-1}{x^2+2 x-3}$
$\begin{aligned}
& \Rightarrow \lim _{x \rightarrow 1^{-}} \frac{(x-1)(x+1)}{(x-1)^2} \Rightarrow \lim _{x \rightarrow 1^{+}} \frac{(x-1)(x+1)}{(x+3)(x-1)} \\
& \Rightarrow \lim _{x \rightarrow 1^{-}} \frac{x+1}{x-1}=\infty \Rightarrow \lim _{x \rightarrow 1^{+}} \frac{x+1}{x+3}=\frac{2}{4}=\frac{1}{2}
\end{aligned}$
$\therefore$ LHL $\neq f(1) \Rightarrow f(x)$ is not continuous at $x=1$

</details>

---

### Q2. BITSAT 2020

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{f}$ be the function defined by $f(x)=\left\{\begin{array}{ll}\frac{x^{2}-1}{x^{2}-2|x-1|-1}, & x \neq 1 \\ 1 / 2, & x=1\end{array}\right.$

**Options:**

- **(A)** The function is continuous for all values of x
- **(B)** The function is continuous only for $x>1$
- **(C)** The function is continuous at $\mathrm{x}=1$
- **(D)** The function is not continuous at $x=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The function is not continuous at $x=1$**

**Detailed Solution:**

For $x<1, f(x)=\frac{x^{2}-1}{x^{2}+2 x-3}=\frac{x+1}{x+3}$

$\therefore \lim _{x \rightarrow 1^{-}} \mathrm{f}(\mathrm{x})=\frac{1}{2}$

For $x>1, f(x)=\frac{x^{2}-1}{x^{2}-2 x+1}=\frac{x+1}{x-1}$

$\therefore \lim _{x \rightarrow 1^{+}} f(x)=\infty$

$\therefore$ The function is not continuous at $\mathrm{x}=1$.

</details>

---

### Q3. BITSAT 2018

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mtable><mtr><mtd><msup><mi>x</mi><mi>p</mi></msup><mi>sin</mi><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr></mtable></mtd></mtr><mtr><mtd><mtable><mtr><mtd><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous but not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, if

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>&#60;</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>p</mi><mo>&#8804;</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>&#8805;</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>p</mi><mo>&#8804;</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mtable><mtr><mtd><msup><mi>x</mi><mi>p</mi></msup><mi>sin</mi><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr></mtable></mtd></mtr><mtr><mtd><mtable><mtr><mtd><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> to be continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mrow><msup><mi>x</mi><mi>p</mi></msup><mi>sin</mi><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><msup><mi>x</mi><mi>p</mi></msup></mfenced><mo>&#215;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mrow><mi>sin</mi><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><msup><mi>x</mi><mi>p</mi></msup></mfenced><mo>&#215;</mo><mfenced><mrow><mtext>value&#160;between&#160;</mtext><mo>-</mo><mn>1</mn><mtext>&#160;to</mtext><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>p</mi><mo>&#62;</mo><mn>0</mn></math></p><p>Now,</p><p>RHD at <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>RHD&#160;at&#160;</mtext><mfenced><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="[" close="]"><mfrac><mrow><msup><mi>h</mi><mi>p</mi></msup><mi>sin</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>h</mi></mfrac></mstyle><mo>-</mo><mn>0</mn></mrow><mi>h</mi></mfrac></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="[" close="]"><mrow><msup><mi>h</mi><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>sin</mi><mfrac><mn>1</mn><mi>h</mi></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>LHD&#160;at&#160;</mtext><mfenced><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="[" close="]"><mfrac><mrow><msup><mfenced><mrow><mo>-</mo><mi>h</mi></mrow></mfenced><mi>p</mi></msup><mi>sin</mi><mfenced><mrow><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>h</mi></mfrac></mstyle></mrow></mfenced><mo>-</mo><mn>0</mn></mrow><mrow><mo>-</mo><mi>h</mi></mrow></mfrac></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="[" close="]"><mrow><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>p</mi></msup><msup><mfenced><mrow><mo>-</mo><mi>h</mi></mrow></mfenced><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>sin</mi><mfenced><mfrac><mn>1</mn><mi>h</mi></mfrac></mfenced></mrow></mfenced></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, therefore</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>&#8804;</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>p</mi><mo>&#8804;</mo><mn>1</mn></math>.</p>

</details>

---

### Q4. BITSAT 2017

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo></math>, so that the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfrac></math> is continuous at each point in its domain, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>,</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> are continuous functions, so the
function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is clearly continuous at each point of its domain except possibly at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>.</p><p>So, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> to be continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>2</mn><mo>-</mo><mfrac><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mi>x</mi></mfrac></mrow><mrow><mn>2</mn><mo>+</mo><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mi>x</mi></mfrac></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>&#8757;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mi>x</mi></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mi>x</mi></mfrac><mo>=</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q5. BITSAT 2016

*Type:* `singleCorrect` | *Level:* `1`

The number of points at which the function $\mathrm{f}(\mathrm{x})=\frac{1}{\log |\mathrm{x}|}$ is discontinuous is:

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

The function $\log |x|$ is not defined at $x=0$, so, $\mathrm{x}=0$ is a point of discontinuity. Also for $\mathrm{f}(\mathrm{x})$ to be defined, $\log |\mathrm{x}| \neq 0 \Rightarrow \mathrm{x} \neq\pm 1$

Hence, 0,1,-1 are three points of discontinuity.

</details>

---

### Q6. BITSAT 2015

*Type:* `singleCorrect` | *Level:* `2`

Let $f: R \rightarrow R$ be a function such that $f(x+y)=f(x)+f(y), \forall x, y \in \mathbb{R}$

If $\mathrm{f}(\mathrm{x})$ is differentiable at $\mathrm{x}=0$, then which one of the following is incorrect?

**Options:**

- **(A)** $\mathrm{f}(\mathrm{x})$ is continuous, $\forall \mathrm{x} \in \mathrm{R}$
- **(B)** $\mathrm{f}^{\prime}(\mathrm{x})$ is constant, $\forall \mathrm{x} \in \mathrm{R}$
- **(C)** $\mathrm{f}(\mathrm{x})$ is differentiable, $\forall \mathrm{x} \in \mathrm{R}$
- **(D)** $\mathrm{f}(\mathrm{x})$ is differentiable only in a finite interval containing zera.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{f}(\mathrm{x})$ is differentiable only in a finite interval containing zera.**

**Detailed Solution:**

Let $f(x+y)=f(x)+f(y), \forall x, y \in R$

Put $x=0=y$

$\Rightarrow f(0)=f(0)+f(0)$

$\Rightarrow f(0)=0$

Now, $f^{\prime}(0)=\lim _{h \rightarrow 0} \frac{f(0+h)-f(0)}{h}$

$f^{\prime \prime}(0)=\lim _{h \rightarrow 0} \frac{f(h)}{h}$

Now, $f(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}$

$=\lim _{h \rightarrow 0} \frac{f(x)+f(h)-f(x)}{h}$

$$

\begin{array}{l}

\Rightarrow \mathrm{f}^{\prime}(\mathrm{x})=\lim _{\mathrm{h} \rightarrow 0} \frac{\mathrm{f}(\mathrm{h})}{\mathrm{h}}=\mathrm{f}^{\prime}(0) \\

\Rightarrow \mathrm{f}(\mathrm{x})=\mathrm{x} \mathrm{f}(0)+\mathrm{C}

\end{array}

$$

But $f(0)=0$

$$

\therefore \mathrm{C}=0

$$

Hence, $f(x)=x f(0), \forall x \in R$

Clearly, $\mathrm{f}(\mathrm{x})$ is everywhere continuous and differentiable and $\mathrm{f}^{\prime}(\mathrm{x})$ is constant.

$\forall \mathrm{x} \in \mathrm{R}$

</details>

---

### Q7. BITSAT 2015

*Type:* `singleCorrect` | *Level:* `3`

If a function $f(x)$ is given by

$f(x)=\frac{x}{1+x}+\frac{x}{(x+1)(2 x+1)}$

$+\frac{x}{(2 x+1)(3 x+1)}+\ldots, \infty$, then at $x=0, f(x)$

**Options:**

- **(A)** has no limit
- **(B)** is not continuous
- **(C)** is continuous but not differentiable
- **(D)** is differentiable

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) is not continuous**

**Detailed Solution:**

Let

$f(x)=\frac{x}{1+x}+\frac{x}{(x+1)(2 x+1)}+\frac{x}{(2 x+1)(3 x+1)}+\ldots \infty$

$=\lim _{n \rightarrow \infty} \sum_{r=1}^{n} \frac{x}{[(r-1) x+1](r x+1)}$

$=\lim _{x \rightarrow \infty} \sum_{\mathrm{r}=1}^{\mathrm{n}}\left[\frac{\mathrm{x}}{[(\mathrm{r}-1) \mathrm{x}+1]}-\frac{1}{\mathrm{rx}+1}\right]$

$=\lim _{n \rightarrow \infty}\left[1-\frac{1}{n x+1}\right]=1$

For $x=0,$ we have $f(x)=0$

Thus, we have $f(x)=\left\{\begin{array}{ll}1, & x \neq 0 \\ 0, & x=0\end{array}\right.$

Clearly, $\lim _{x \rightarrow 0^{-}} \mathrm{f}(\mathrm{x})=\lim _{\mathrm{x} \rightarrow 0^{+}} \mathrm{f}(\mathrm{x}) \neq \mathrm{f}(0)$

So, $\mathrm{f}(\mathrm{x})$ is not continuous at $\mathrm{x}=0$.

</details>

---

### Q8. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}(\mathrm{x})=\left\{\begin{array}{l}\frac{1-\sin ^{3} \mathrm{x}}{3 \cos ^{2} \mathrm{x}}, \mathrm{x}<\frac{\pi}{2} \\ \mathrm{p}, \quad \mathrm{x}=\frac{\pi}{2} \\ \frac{\mathrm{q}(1-\sin \mathrm{x})}{(\pi-2 \mathrm{x})^{2}}, \mathrm{x}>\frac{\pi}{2}\end{array}\right.$

If $f(x)$ is continuous at $x=\frac{\pi}{2},(p, q)=$

**Options:**

- **(A)** (1,4)
- **(B)** $\left(\frac{1}{2}, 2\right)$
- **(C)** $\left(\frac{1}{2}, 4\right)$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\frac{1}{2}, 4\right)$**

**Detailed Solution:**

$\mathrm{f}\left[(\pi / 2)^{-}\right]=\lim _{\mathrm{h} \rightarrow 0} \frac{1-\sin ^{3}[(\pi / 2)-\mathrm{h}]}{3 \cos ^{2}[(\pi / 2)-\mathrm{h}]}$

$\quad=\lim _{\mathrm{h} \rightarrow 0} \frac{1-\cos ^{3} \mathrm{~h}}{3 \sin ^{2} \mathrm{~h}}=\frac{1}{2}$

$\mathrm{f}\left[(\pi / 2)^{+}\right]=\lim _{\mathrm{h} \rightarrow 0} \frac{\mathrm{q}[1-\sin \{(\pi / 2)+\mathrm{h}\}]}{[\pi-2\{(\pi / 2)+\mathrm{h}\}]^{2}}$

$=\lim _{\mathrm{h} \rightarrow 0} \frac{\mathrm{q}(1-\cosh )}{4 \mathrm{~h}^{2}}=\frac{\mathrm{q}}{8}$

$\therefore \mathrm{p}=\frac{1}{2}=\frac{\mathrm{q}}{8} \Rightarrow \mathrm{p}=\frac{1}{2}, \mathrm{q}=4$

</details>

---

### Q9. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `1`

If the function $f(x)=\begin{cases}A x-B, & x \leq 1 \\ 3 x & , 1<x<2 \\ B x^{2}-A, & x \geq 2\end{cases}$
is continuous at $x=2$ and $4,$ then the values of a and $b$ are

**Options:**

- **(A)** 3,5
- **(B)** 3,-5
- **(C)** 0,3
- **(D)** 0,5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3,-5**

**Detailed Solution:**

Since $\mathrm{f}(\mathrm{x})$ is continuous at $\mathrm{x}=2$
$\therefore \mathrm{f}(2)=\lim _{\mathrm{x} \rightarrow 2^{+}} \mathrm{f}(\mathrm{x}) \Rightarrow 1=\lim _{\mathrm{x} \rightarrow 2^{+}}(\mathrm{ax}+\mathrm{b})$
$\therefore 1=2 \mathrm{a}+\mathrm{b}$
Again $\mathrm{f}(\mathrm{x})$ is continuous at $\mathrm{x}=4$
$\therefore \mathrm{f}(4)=\lim _{x \rightarrow 4^{-}} \mathrm{f}(\mathrm{x}) \Rightarrow 7=\lim _{\mathrm{x} \rightarrow 4^{-}}(\mathrm{ax}+\mathrm{b})$
$\therefore 7=4 \mathrm{a}+\mathrm{b}$
Solving (1) and $(2),$ we get $a=3, b=-5$

</details>

---

