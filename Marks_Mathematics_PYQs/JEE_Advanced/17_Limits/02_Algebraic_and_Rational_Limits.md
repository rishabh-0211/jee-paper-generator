# JEE Advanced Mathematics - Limits

## Topic 2: Algebraic and Rational Limits

**Total Questions:** 12

---

### Q1. JEE Advanced 2025 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $x_0$ be the real number such that $e^{x_0}+x_0=0$. For a given real number $\alpha$, define $g(x)=\frac{3 x e^x+3 x-\alpha e^x-\alpha x}{3\left(e^x+1\right)}$
for all real numbers $x$.
Then which one of the following statements is TRUE?

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/h7sx77AU_0lY5AHjMVOUbifoU5blYfN0Um3hH05Ev7I.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/DzcoIwGcoAKpHi3sMNOwWg0iPXfWO1N-ovzgdXGphMA.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/qustdTazrmDDA5bVY1CYmelD3VlbdJJJqPIWlmM8-u4.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/Voccczcm9oFiCjg8PrDyRN3keema4wpNfd6SQguCxX4.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/qustdTazrmDDA5bVY1CYmelD3VlbdJJJqPIWlmM8-u4.original.fullsize.png">**

**Detailed Solution:**

$\begin{aligned} & e^{x_0}+x_0=0 \\ & g(x)=\frac{3 x e^x+3 x-\alpha e^x-\alpha x}{3\left(e^x+1\right)} \\ & g(x)=x-\frac{\alpha\left(e^x+x\right)}{3\left(e^x+1\right)}, g(x)+e^{x_0}=x+e^{x_0}-\frac{\alpha}{3}\left(\frac{e^x+x}{e^x+1}\right) \\ & g(x)+e^{x_0}=\left(x-x_0\right)-\frac{\alpha}{3}\left(\frac{e^x+x}{e^x+1}\right) \\ & \Rightarrow \text { As very clear } g\left(x_0\right)+x_0 \Rightarrow 0\end{aligned}$
$\begin{aligned} & \lim _{x \rightarrow x_0}\left|\frac{g(x)+e^{x_0}}{x-x_0}\right| \frac{0 \uparrow}{0 \uparrow}=\lim _{x \rightarrow x_0}\left|\frac{g^{\prime}(x)}{1}\right|=\left|g^{\prime}\left(x_0\right)\right| \\ & g^{\prime}(x)=1-\frac{\alpha}{3}\left(\frac{\left(e^x+1\right)\left(e^x+1\right)-\left(e^x+x\right) e^x}{\left(e^x+1\right)^2}\right) \\ & g^{\prime}\left(x_0\right)=1-\frac{\alpha}{3}\left(\frac{\left(e^{x_0}+1\right)^2}{\left(e^{x_0}+1\right)^2}\right)=1-\frac{\alpha}{3} \\ & \Rightarrow \lim _{x \rightarrow x_0}\left|\frac{g(x)+e^{x_0}}{x-x_0}\right|=\left|g^{\prime}\left(x_0\right)\right|=\left|1-\frac{\alpha}{3}\right|\end{aligned}$

</details>

---

### Q2. JEE Advanced 2025 (Paper 1)

*Type:* `numerical` | *Level:* `3`

Let $\alpha$ and $\beta$ be the real numbers such that $\lim _{x \rightarrow 0} \frac{1}{x^3}\left(\frac{\alpha}{2} \int_0^x \frac{1}{1-t^2} d t+\beta x \cos x\right)=2$. Then the value of $\alpha+\beta$ is _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2.4**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{\frac{\alpha}{2} \int_0^x \frac{1}{1-t^2} d t+\beta x \cos x}{x^3}$
$\begin{aligned} & =\lim _{x \rightarrow 0} \frac{\frac{\alpha}{2}\left(\frac{1}{1-x^2}\right)+\beta \cos x-\beta x \sin x}{3 x^2} \\ & =\frac{\frac{\alpha}{2}\left(1-x^2\right)^{-1}+\beta\left(1-\frac{x^2}{2!}+\frac{x^4}{4!} \ldots\right)-\beta x\left(x-\frac{x^3}{3!}+\frac{x^5}{5!} \ldots\right)}{3 x^2} \\ & =\frac{\frac{\alpha}{2}\left(1+x^2+x^4 \ldots\right)+\beta\left(1-\frac{x^2}{2!}+\frac{x^4}{4!} \ldots\right)-\beta\left(x^2-\frac{x^4}{3!} \ldots\right)}{3 x^2}\end{aligned}$
$\begin{aligned} & =\frac{\left(\frac{\alpha}{2}+\beta\right)+\mathrm{x}^2\left(\frac{\alpha}{2}-\frac{\beta}{2}-\beta\right)+\mathrm{x}^4() \ldots}{3 \mathrm{x}^2}=2(\text { Given }) \\ & \therefore \frac{\alpha}{2}+\beta=0 \text { and } \frac{\alpha-3 \beta}{6}=2 \\ & \Rightarrow \alpha=-2 \beta \text { and } \alpha=12+3 \beta \\ & \Rightarrow \beta=-\frac{12}{5} \text { and } \alpha=\frac{24}{5}\end{aligned}$
$\therefore \alpha+\beta=\frac{12}{5}=2.40$

</details>

---

### Q3. JEE Advanced 2024 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let the function $f:[1, \infty) \rightarrow \mathbb{R}$ be defined by
$f(t)=\left\{\begin{array}{cc}(-1)^{n+1} 2, & \text { if } t=2 n-1, n \in \mathbb{N}, \\ \frac{(2 n+1-t)}{2} f(2 n-1)+\frac{(t-(2 n-1))}{2} f(2 n+1), & \text { if } 2 n-1 < t < 2 n+1, n \in \mathbb{N} .\end{array}\right.$
Define $g(x)=\int_1^x f(t) d t, x \in(1, \infty)$. Let $\alpha$ denote the number of solutions of the equation $g(x)=0$ in the interval $(1,8]$ and $\beta=\lim _{x \rightarrow 1^+} \frac{g(x)}{x-1}$. Then the value of $\alpha+\beta$ is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$\mathrm{f}(\mathrm{t})=\left\{\begin{array}{ccc}2 & ; & \mathrm{t}=1 \\ 4-2 \mathrm{t} & ; & 1 < \mathrm{t} < 3 \\ -2 & ; & \mathrm{t}=3 \\ -8-2 \mathrm{t} & ; & 3 < \mathrm{t} < 5 \\ 2 & ; & \mathrm{t}=5 \\ 12-2 \mathrm{t} & ; & 5 < \mathrm{t} < 7 \\ -2 & ; & \mathrm{t}=7 \\ -16+2 \mathrm{t} & ; & 7 < \mathrm{t} < 9\end{array}\right.$
$g(x)=\int_1^x f(t) d t \Rightarrow g^{\prime}(x)=f(x)$
for $x \in(1,8]$
$g(x)=0 \Rightarrow x=3,5,7 \therefore \alpha=3$
$\beta=\lim _{x \rightarrow 1^{+}} \frac{g(x)}{x-1}$
Apply L'Hospital's
$\begin{aligned} & =\frac{g^{\prime}\left(1^{+}\right)}{1}=f\left(1^{+}\right) \\ & \beta=2 \\ & \therefore \alpha+\beta=5\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/I0sWyNMHg9B3JNA01Y5dAGJ51buGeJ1hbCxfMeea924.original.fullsize.png">

</details>

---

### Q4. JEE Advanced 2024 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)$ be a continuously differentiable function on the interval $(0, \infty)$ such that $f(1)=2$ and $\underset{t \rightarrow x}{\lim} \frac{t^{10} f(x)-x^{10} f(t)}{t^9-x^9}=1$ for each $x>0$. Then, for all $x>0, f(x)$ is equal to

**Options:**

- **(A)** $\frac{31}{11 x}-\frac{9}{11} x^{10}$
- **(B)** $\frac{9}{11 x}+\frac{13}{11} x^{10}$
- **(C)** $\frac{-9}{11 x}+\frac{31}{11} x^{10}$
- **(D)** $\frac{13}{11 x}+\frac{9}{11} x^{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{9}{11 x}+\frac{13}{11} x^{10}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{t \rightarrow x} \frac{t^{10} f(x)-x^{10} f(t)}{t^9-x^9}=1 \\ & \Rightarrow \lim _{t \rightarrow x} \frac{10 t^9 f(x)-x^{10} f^{\prime}(t)}{9 t^8}=1\end{aligned}$
$\begin{aligned} & \Rightarrow 10 x f(x)-x^2 f^{\prime}(x)=9 \\ & \Rightarrow x^2 f^{\prime}(x)=10 x f(x)-9 \\ & \Rightarrow f^{\prime}(x)=\frac{10 f(x)}{x}-\frac{9}{x^2} \\ & \Rightarrow \frac{d y}{d x}-\frac{10}{x} y=-\frac{9}{x^2} \\ & \Rightarrow y \cdot \frac{1}{x^{10}}=\int-\frac{9}{x^2} \cdot \frac{1}{x^{10}} d x \\ & \Rightarrow \frac{y}{x^{10}}=\frac{9}{11 x^{11}}+c...(1)\end{aligned}$
$\begin{aligned} & \because \mathrm{f}(1)=2 \Rightarrow \frac{2}{1}=\frac{9}{11}+\mathrm{c} \Rightarrow \mathrm{c}=\frac{13}{11} \\ & \therefore \mathrm{f}(\mathrm{x})=\frac{9}{11 \mathrm{x}}+\frac{13}{11} \mathrm{x}^{10}\end{aligned}$
$\Rightarrow$ Option (2) is correct.

</details>

---

### Q5. JEE Advanced 2023 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be the function defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><mi>n</mi></msqrt></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>)</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>x</mi></msubsup><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow><mi>t</mi></mfrac></msqrt><mi>d</mi><mi>t</mi><mo>&#60;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>2</mn><msqrt><mi>x</mi></msqrt></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></math>

**Options:**

- **(A)** Does NOT exist
- **(B)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be the function defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><mi>n</mi></msqrt></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>)</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>x</mi></msubsup><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow><mi>t</mi></mfrac></msqrt><mi>d</mi><mi>t</mi><mo>&#60;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>2</mn><msqrt><mi>x</mi></msqrt></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>. </p><p>Now we need to solve <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> sided limit here to get some answer, as  <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder></math> doesn&rsquo;t exist here (not in domain)</p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mo>&#160;</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>&#8805;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>&#62;</mo><mo>&#160;</mo><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>&#8805;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>-</mo><mn>1</mn><mo>&#8658;</mo><msqrt><mi>n</mi></msqrt><mo>&#8805;</mo><msqrt><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>-</mo><mn>1</mn></msqrt></math></p><p>So, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>-</mo><mn>1</mn></msqrt></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mo>&#183;</mo></mfenced><mo>=</mo></math> least integer function</p><p>Now multiplying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>x</mi></msubsup><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow><mi>t</mi></mfrac></msqrt><mi>d</mi><mi>t</mi><mo>&#60;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>2</mn><msqrt><mi>x</mi></msqrt></math> and taking limit we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><msubsup><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>x</mi></msubsup><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow><mi>t</mi></mfrac></msqrt><mi>d</mi><mi>t</mi><mo>&#183;</mo><msqrt><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>-</mo><mn>1</mn></msqrt><mo>&#8804;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><msqrt><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>-</mo><mn>1</mn></msqrt><mo>&#215;</mo><mn>2</mn><msqrt><mi>x</mi></msqrt></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><msqrt><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>-</mo><mn>1</mn></msqrt><mo>&#215;</mo><mn>2</mn><msqrt><mi>x</mi></msqrt><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mn>2</mn><msqrt><mi>x</mi></msqrt><msqrt><mfenced close="]" open="["><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></msqrt><mo>&#160;&#160;</mo><mfenced><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>&#8713;</mo><mi>Z</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mn>2</mn><msqrt><mi>x</mi><mfenced><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>-</mo><mfenced close="}" open="{"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced></msqrt><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mn>2</mn><msqrt><mn>1</mn><mo>-</mo><mi>x</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></msqrt><mo>=</mo><mn>2</mn><mo>;</mo><mo>&#160;</mo><mfenced><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>&#8713;</mo><mi>Z</mi></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><msubsup><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>x</mi></msubsup><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow><mi>t</mi></mfrac></msqrt><mi>d</mi><mi>t</mi><mo>&#183;</mo><msqrt><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>-</mo><mfenced close="}" open="{"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></msqrt><mo>=</mo><mfrac><mrow><msubsup><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>x</mi></msubsup><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow><mi>t</mi></mfrac></msqrt><mi>d</mi><mi>t</mi><mo>&#183;</mo><msqrt><mn>1</mn><mo>-</mo><mi>x</mi><mfenced close="}" open="{"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></msqrt></mrow><msqrt><mi>x</mi></msqrt></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><msubsup><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>x</mi></msubsup><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow><mi>t</mi></mfrac></msqrt><mi>d</mi><mi>t</mi></mrow><msqrt><mi>x</mi></msqrt></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mi>x</mi></mfrac></msqrt><mo>-</mo><mn>2</mn><mi>x</mi><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></msqrt></mrow><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mi>x</mi></msqrt></mrow></mfrac></mfrac></math></p><p>{Using L-hospital rule}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mn>2</mn><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>-</mo><mn>4</mn><msqrt><mi>x</mi></msqrt><mo>&#183;</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mn>2</mn></math></p><p>Similarly for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>&#8712;</mo><mi>Z</mi></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>.</p></blockquote>

</details>

---

### Q6. JEE Advanced 2016 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mi mathvariant="double-struck">&#160;</mi><mo>:</mo><mi mathvariant="double-struck">R</mi><mo>&#8594;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced></math> and <math><mi>g</mi><mi mathvariant="double-struck">&#160;</mi><mo>:</mo><mi mathvariant="double-struck">R</mi><mo>&#8594;</mo><mi mathvariant="double-struck">R</mi></math> be twice differentiable functions such that <math><msup> <mi>f</mi> <mo>&#8243;</mo></msup></math> and <math><msup> <mi>g</mi> <mo>&#8243;</mo> </msup></math> are continuous functions on <math><mi mathvariant="double-struck">R</mi></math> . Suppose <math> <mrow> <msup> <mi>f</mi> <mo>&#8242;</mo> </msup><mrow><mo>(</mo> <mn>2</mn> <mo>)</mo></mrow><mo>=</mo><mi>g</mi><mrow><mo>(</mo> <mn>2</mn> <mo>)</mo></mrow><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><msup> <mi>f</mi> <mo>&#8243;</mo></msup><mrow><mo>(</mo> <mn>2</mn> <mo>)</mo></mrow><mo>&#8800;</mo><mn>0</mn></mrow></math> and <math><msup> <mi>g</mi> <mo>&#8242;</mo> </msup><mrow><mo>(</mo> <mn>2</mn> <mo>)</mo></mrow><mi>&#160;</mi><mo>&#8800;</mo><mn>0.</mn><munder> <mrow> <mi>lim</mi> </mrow> <mrow> <mi>x</mi><mo>&#8594;</mo><mn>2</mn> </mrow> </munder> <mfrac> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mi>&#160;</mi><mi>g</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> <mrow> <msup> <mi>f</mi> <mo>&#8242;</mo> </msup><mi>&#160;</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mi>&#160;</mi><msup> <mi>g</mi> <mo>&#8242;</mo> </msup><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> </mfrac> <mo>=</mo><mn>1</mn><mo>,</mo> </math> then

**Options:**

- **(A)** <math><mi>f</mi></math> has a local minimum at <math><mi>x</mi><mo>=</mo><mn>2</mn></math>
- **(B)** <math><mi>f</mi></math>  has a local maximum at  <math><mi>x</mi><mo>=</mo><mn>2</mn></math>
- **(C)** <math><msup><mrow><mi>f</mi></mrow><mrow><mo>&#x2033;</mo></mrow></msup><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>&gt;</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></math>
- **(D)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><msup><mrow><mi>f</mi></mrow><mrow><mo>″</mo></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mn>0</mn></math> for at least one <math><mi>x</mi><mo>∈</mo><mi mathvariant="double-struck">R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><msup><mrow><mi>f</mi></mrow><mrow><mo>″</mo></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mn>0</mn></math> for at least one <math><mi>x</mi><mo>∈</mo><mi mathvariant="double-struck">R</mi></math>**

**Detailed Solution:**

Using L'Hospital Rule <math> <mrow> <mrow><mo>(</mo> <mrow> <mi>a</mi><mi>s</mi><mtext> </mtext><mtext> </mtext><mi>i</mi><mi>t</mi><mtext> </mtext><mtext> </mtext><mi>i</mi><mi>s</mi><mtext> </mtext><mtext> </mtext><mfrac> <mn>0</mn> <mn>0</mn> </mfrac> <mtext> </mtext><mtext> </mtext><mi>f</mi><mi>o</mi><mi>r</mi><mi>m</mi> </mrow> <mo>)</mo></mrow> </mrow> </math>
<math> <mrow> <munder> <mrow> <mi>lim</mi> </mrow> <mrow> <mi>x</mi><mo>→</mo><mn>2</mn> </mrow> </munder> <mfrac> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mi> </mi><mi>g</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>+</mo><mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mi> </mi><msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> <mrow> <msup> <mi>f</mi> <mo>″</mo> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mi> </mi><msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>+</mo><msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mi> </mi><msup> <mi>g</mi> <mo>″</mo> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> </mfrac> <mo>=</mo><mn>1</mn> </mrow> </math>
<math> <mrow> <mo>⇒</mo><mfrac> <mrow> <mi>f</mi><mi> </mi><mrow><mo>(</mo> <mn>2</mn> <mo>)</mo></mrow><mi> </mi><msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mn>2</mn> <mo>)</mo></mrow> </mrow> <mrow> <msup> <mi>f</mi> <mo>″</mo> </msup> <mi> </mi><mrow><mo>(</mo> <mn>2</mn> <mo>)</mo></mrow><mi> </mi><msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mn>2</mn> <mo>)</mo></mrow> </mrow> </mfrac> <mo>=</mo><mn>1</mn><mo>⇒</mo><msup> <mi>f</mi> <mo>″</mo> </msup> <mrow><mo>(</mo> <mn>2</mn> <mo>)</mo></mrow><mo>=</mo><mi>f</mi><mrow><mo>(</mo> <mn>2</mn> <mo>)</mo></mrow><mo>&gt;</mo><mn>0</mn> </mrow> </math>
<math> <mrow> <mi>A</mi><mi>l</mi><mi>s</mi><mi>o</mi><mtext> </mtext><msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mn>2</mn> <mo>)</mo></mrow><mo>=</mo><mn>0</mn><mtext> and </mtext><msup> <mi>f</mi> <mo>″</mo> </msup> <mrow><mo>(</mo> <mn>2</mn> <mo>)</mo></mrow><mo>&gt;</mo><mn>0</mn> </mrow> </math>
<math><mo>∴</mo></math> <math><mi>x</mi><mo>=</mo><mn>2</mn></math> is local minima.

</details>

---

### Q7. JEE Advanced 2015 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let m and n be two positive integers greater than 1. If <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>&#945;</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mo>&#8289;</mo><mo>(</mo><msup><mrow><mi>&#945;</mi></mrow><mrow><mi>n</mi></mrow></msup><mi>&#160;</mi><mo>)</mo></mrow></msup><mo>-</mo><mi>e</mi></mrow><mrow><msup><mrow><mi>&#945;</mi></mrow><mrow><mi>m</mi></mrow></msup></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mo>-</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math> then the value of <math><mfrac><mrow><mi>m</mi></mrow><mrow><mi>n</mi></mrow></mfrac></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>α</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><msup><mrow><mi>α</mi></mrow><mrow><mi>n</mi></mrow></msup></mrow></mrow></mrow></msup><mo>-</mo><mi>e</mi></mrow><mrow><msup><mrow><mi>α</mi></mrow><mrow><mi>m</mi></mrow></msup></mrow></mfrac><mo>=</mo><mi> </mi><mo>-</mo><mfrac><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi></math>  Using L'Hospital's Rule

 <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>α</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><msup><mrow><mi>α</mi></mrow><mrow><mi>n</mi></mrow></msup></mrow></mfenced></mrow></mrow></mrow></msup><mo>&sdot;</mo><mi> </mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><msup><mrow><mi>α</mi></mrow><mrow><mi>n</mi></mrow></msup></mrow></mfenced></mrow></mrow><mi> </mi><mo>&sdot;</mo><mi>n</mi><msup><mrow><mi>α</mi></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><mrow><mi>m</mi><mi> </mi><mo>&sdot;</mo><msup><mrow><mi>α</mi></mrow><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfrac></mrow></mrow><mo>=</mo><mi> </mi><mfrac><mrow><mo>-</mo><mi>e</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math> 
 <math><mo>⇒</mo><mi> </mi><mfrac><mrow><mi>m</mi></mrow><mrow><mi>n</mi></mrow></mfrac><mo>=</mo><mn>2</mn></math> .

</details>

---

### Q8. JEE Advanced 2012 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha(a)$ and $\beta(a)$ be the roots of the equation $(\sqrt[3]{1+a}-1) x^{2}+(\sqrt{1+a}-1) x+(\sqrt[6]{1+a}-1)=0$ where $a$ $>-1$. Then $\lim _{a \rightarrow 0^{+}} \alpha(a)$ and $\lim _{x \rightarrow 0^{+}} \beta(a)$ are

**Options:**

- **(A)** $-\frac{5}{2}$ and 1
- **(B)** $-\frac{1}{2}$ and $-1$
- **(C)** $-\frac{7}{2}$ and 2
- **(D)** $-\frac{9}{2}$ and 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{1}{2}$ and $-1$**

**Detailed Solution:**

$(\sqrt[3]{1+a}-1) x^{2}+(\sqrt{1+a}-1) x+(\sqrt[6]{1+a}-1)=0$

Let $a+1=y$, then equation reduces to $\left(y^{1 / 3}-1\right) x^{2}+\left(y^{1 / 2}-1\right) x+\left(y^{1 / 6}-1\right)=0$

On dividing both sides by $y-1$, we get $\left(\frac{y^{1 / 3}-1}{y-1}\right) x^{2}+\left(\frac{y^{1 / 2}-1}{y-1}\right) x+\left(\frac{y^{1 / 6}-1}{y-1}\right)=0$

On taking limit as $y \rightarrow 1$ i.e. $a \rightarrow 0$ on both sides, we get $\frac{1}{3} x^{2}+\frac{1}{2} x+\frac{1}{6}=0 \Rightarrow 2 x^{2}+3 x+1=0$

$\Rightarrow x=-1,-\frac{1}{2}$ (roots of the equation)

$\therefore \quad \lim _{a \rightarrow 0^{+}} \alpha(a)=-1, \lim _{a \rightarrow 0^{+}} \beta(a)=-\frac{1}{2}$

</details>

---

### Q9. JEE Advanced 2012 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\lim _{x \rightarrow \infty}\left(\frac{x^{2}+x+1}{x+1}-a x-b\right)=4$, then

**Options:**

- **(A)** $a=1, b=4$
- **(B)** $a=1, b=-4$
- **(C)** $a=2, b=-3$
- **(D)** $a=2, b=3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $a=1, b=-4$**

**Detailed Solution:**

Given: $\lim _{x \rightarrow \infty}\left(\frac{x^{2}+x+1}{x+1}-a x-b\right)=4$

$\begin{array}{l}

\Rightarrow \lim _{x \rightarrow \infty} \frac{x^{2}+x+1-a x^{2}-a x-b x-b}{x+1}=4 \\

\Rightarrow \lim _{x \rightarrow \infty} \frac{(1-a) x^{2}+(1-a-b) x+(1-b)}{x+1}=4

\end{array}$

For this limit to be finite $1-a=0 \Rightarrow a=1$ then given limit reduces to

$\lim _{x \rightarrow \infty} \frac{-b x+(1-b)}{x+1}=4 \Rightarrow \lim _{x \rightarrow \infty} \frac{-b+\frac{(1-b)}{x}}{1+\frac{1}{x}}=4$

$\Rightarrow-b=4$ or $b=-4, \therefore a=1, b=-4$

</details>

---

### Q10. JEE Advanced 2010 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\lim _{x \rightarrow 0} \frac{1}{x^3} \int_0^x \frac{t \log (1+t)}{t^4+4} d t$ is

**Options:**

- **(A)** 0
- **(B)** $\frac{1}{12}$
- **(C)** $\frac{1}{24}$
- **(D)** $\frac{1}{64}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{12}$**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{1}{x^3} \int_0^{x t} \frac{\log (1+t)}{4+t^4} d t$
Using L' Hospital's rule,
$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{\frac{x \log (1+x)}{4+x^4}}{3 x^2} \\
= & \lim _{x \rightarrow 0} \frac{\log (1+x)}{3 x} \cdot \frac{1}{4+x^4} \\
= & \frac{1}{3} \cdot \frac{1}{4}=\frac{1}{12}\left[\text { using, } \lim _{x \rightarrow 0} \frac{\log (1+x)}{x}=1\right]
\end{aligned}
$$

</details>

---

### Q11. JEE Advanced 2008 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $g(x)=\frac{(x-1)^n}{\log \cos ^m(x-1)} ; 0 < x < 2, m$ and $n$ are integers, $m \neq 0, n>0$ and let $p$ be the left hand derivative of $|x-1|$ at $x=1$. If $\lim _{x \rightarrow 1^{+}} g(x)=p$, then

**Options:**

- **(A)** $n=1, m=1$
- **(B)** $n=1, m=-1$
- **(C)** $n=2, m=2$
- **(D)** $n>2, m=n$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $n=2, m=2$**

**Detailed Solution:**

Given, $g(x)=\frac{(x-1)^n}{\log \cos ^m(x-1)} ; 0 < x < 2, m \neq 0, n$ are integers and $|x-1|=\left\{\begin{array}{l}x-1 ; x \geq 1 \\ 1-x ; x < 1\end{array}\right.$
The left hand derivative of $|x-1|$ at $x=1$ is $p=-1$.
Also,
$$
\begin{aligned}
& \Rightarrow \quad \lim _{h \rightarrow 0} \frac{(1+h-1)^n}{\log \cos ^m(1+h-1)}=-1 \Rightarrow \lim _{h \rightarrow 0} \frac{h^n}{\log \cos ^m h}=-1 \\
& \Rightarrow \quad \lim _{h \rightarrow 0} \frac{h^n}{m \log \cos h}=-1
\end{aligned}
$$
[Using L' Hospital rule]
$$
\begin{array}{ll}
\Rightarrow & \quad \lim _{h \rightarrow 0} \frac{n \cdot h^{n-1}}{m \frac{1}{\cos h}(-\sin h)}=-1 \\
\Rightarrow \quad & \quad \lim _{h \rightarrow 0}\left(-\frac{n}{m}\right) \cdot \frac{h^{n-2}}{\left(\frac{\tan h}{h}\right)}=-1 \\
\Rightarrow \quad & \quad\left(\frac{n}{m}\right) \lim _{h \rightarrow 0} \frac{h^{n-2}}{\left(\frac{\tan h}{h}\right)}=1 \\
\Rightarrow & n=2 \text { and } \frac{n}{m}=1 \\
\therefore & \quad m=n=2
\end{array}
$$

</details>

---

### Q12. JEE Advanced 2007 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow \frac{\pi}{4}} \frac{\int_2^{\sec ^2 x} f(t) d t}{x^2-\frac{\pi^2}{16}}$ equals

**Options:**

- **(A)** $\frac{8}{\pi} f(2)$
- **(B)** $\frac{2}{\pi} f(2)$
- **(C)** $\frac{2}{\pi} f\left(\frac{1}{2}\right)$
- **(D)** $4 f(2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{8}{\pi} f(2)$**

**Detailed Solution:**

$\lim _{x \rightarrow \frac{x}{4}} \frac{\int_2^{\sec ^2 x} f(t) d t}{x^2-\frac{\pi^2}{16}}$ $\left[\therefore \frac{0}{0}\right.$ form $]$
Let
$$
\begin{array}{ll}
\text { Let } & L=\lim _{x \rightarrow \frac{x}{4}} \frac{f\left(\sec ^2 x\right) 2 \sec x \sec x \tan x}{2 x} \\
\therefore & L=\frac{2 f(2)}{\pi / 4}=\frac{8 f(2)}{\pi}
\end{array}
$$

</details>

---

