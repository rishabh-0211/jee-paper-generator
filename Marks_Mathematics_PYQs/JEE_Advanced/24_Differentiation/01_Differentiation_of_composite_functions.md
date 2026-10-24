# JEE Advanced Mathematics - Differentiation

## Topic 1: Differentiation of composite functions

**Total Questions:** 6

---

### Q1. JEE Advanced 2025 (Paper 2)

*Type:* `numerical` | *Level:* `3`

Let $\mathbb{R}$ denote the set of all real numbers. Let $f: \mathbb{R} \rightarrow \mathbb{R}$ and $g: \mathbb{R} \rightarrow(0,4)$ be functions defined by $f(x)=\log _e\left(x^2+2 x+4\right)$, and $g(x)=\frac{4}{1+e^{-2 x}}$
Define the composite function $f \circ g^{-1}$ by $\left(f \circ g^{-1}\right)(x)=\left(g^{-1}(x)\right)$, where $g^{-1}$ is the inverse of the function $g$.
Then the value of the derivative of the composite function $f \circ g^{-1}$ at $x=2$ is ________ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.25**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{h}(\mathrm{x})=\mathrm{f}\left(\mathrm{g}^{-1}(\mathrm{x})\right) \text { and } \mathrm{g}(0)=2 \\ & \begin{aligned} \mathrm{h}^{\prime}(\mathrm{x}) & =\mathrm{f}^{\prime}\left(\mathrm{g}^{-1}(\mathrm{x})\right) \cdot\left(\mathrm{g}^{-1}(\mathrm{x})\right)^{\prime} \\ \mathrm{h}^{\prime}(2) & =\mathrm{f}^{\prime}\left(\mathrm{g}^{-1}(2) \cdot\left(\mathrm{g}^{-1}\right)^{\prime}(2)\right. \\ & =\mathrm{f}^{\prime}(0) \cdot\left(\mathrm{g}^{-1}\right)^{\prime}(2)\end{aligned}\end{aligned}$
Now
$\begin{aligned}
& f(x)=\log _0\left(x^2+2 x+4\right) \\
& f^{\prime}(x)=\frac{2 x+2}{x^2+2 x+4} \\
& f^{\prime}(0)=\frac{1}{2} \\
& g(x)=\frac{4}{1+e^{-2 x}}, g(0)=2 \\
& g^{-1}(g(x))=x
\end{aligned}$
\begin{array}{l|l}\left(\left(\mathrm{g}^{-1}\right)^{\prime}(\mathrm{g}(\mathrm{x}))\right) \mathrm{g}^{\prime}(\mathrm{x})=1 & \mathrm{~g}(\mathrm{x})=\frac{4}{1+\mathrm{e}^{-2 \mathrm{x}}} \\\left(\mathrm{g}^{-1}\right)^{\prime}(2)=\frac{1}{\mathrm{~g}^{\prime}(0)} & \mathrm{g}^{\prime}(\mathrm{x})=\frac{8 \mathrm{e}^{-2 \mathrm{x}}}{\left(1+\mathrm{e}^{-2 \mathrm{x}}\right)^2} \\=\frac{1}{2} & \mathrm{~g}^{\prime}(0)=\frac{8}{4}=2 \\So \mathrm{h}(2)=\frac{1}{4}=0.25 &\end{array}

</details>

---

### Q2. JEE Advanced 2016 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

Let <math><mi>f</mi><mi>&#160;</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi><mo>,</mo><mi>&#160;</mi><mi>g</mi><mi>&#160;</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> and <math><mi>h</mi><mi>&#160;</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be differentiable functions such that <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi></math> and <math><mi>h</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi></math> , for all <math><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>.</mo></math> Then,

**Options:**

- **(A)** <math><msup>  <mi>g</mi>  <mo>&#x2032;</mo> </msup><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>
- **(B)** <math><msup>  <mi>h</mi>  <mo>&#x2032;</mo> </msup><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo></mo><mo>=</mo><mn>666</mn></math>
- **(C)** <math><mi>h</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>16</mn></math>
- **(D)** <math><mi>h</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>36</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>h</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>16</mn></math>**

**Detailed Solution:**

<p>If <math><msup> <mi>f</mi> <mo>&#8242;</mo> </msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>3</mn></math>
<math><mo>&#8658;</mo><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi mathvariant="italic"> x</mi></math>
<math><mo>&#8658;</mo><msup> <mi>g</mi> <mo>&#8242;</mo> </msup><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup> <mi>f</mi> <mo>&#8242;</mo> </msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfrac></math>
<math><mi mathvariant="italic">Also f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>2&#160;</mn></math>   (<math><mi mathvariant="italic">Put x</mi><mo>=</mo><mn>0</mn></math>)
So, <math><msup> <mi>g</mi> <mo>&#8242;</mo> </msup><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup> <mi>f</mi> <mo>&#8242;</mo> </msup><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced></mrow></mfrac></math> 
<math><mo>&#8658;</mo></math> <math><mi>g</mi><mi>&#8242;</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
If <math><mi>h</mi><mo>(</mo><mi>g</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi></math>
<math><msup> <mi>h</mi> <mo>&#8242;</mo> </msup><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup> <mi>g</mi> <mo>&#8242;</mo> </msup><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>.</mi><msup> <mi>g</mi> <mo>&#8242;</mo> </msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfrac></math>
If, <math><mi>g</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>1</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>)</mo><mo>=</mo><mi>x</mi><mo>&#8658;</mo><msup><mi>g</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>
<math><mo>&#8658;</mo><mi mathvariant="italic">g </mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><msup><mrow><mi>g</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&#8658;</mo><mi mathvariant="italic">g </mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mn>6</mn><mi> </mi></math>
To find, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced separators="|"><mn>6</mn></mfenced></math> use <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> in
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced separators="|"><mrow><mi mathvariant="normal">f</mi><mfenced separators="|"><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mn>1</mn></mfenced></mrow></mfrac></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>f</mo><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>6</mn></math></p><p>To find, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced separators="|"><mn>236</mn></mfenced></math>, use <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>6</mn></math> as
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>6</mn></mfenced><mo>=</mo><mn>236</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>h</mi><mo>&#39;</mo></msup><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced separators="|"><mn>6</mn></mfenced><mi mathvariant="normal">.</mi><msup><mi>g</mi><mo>&#39;</mo></msup><mo>(</mo><mn>236</mn><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mfrac><mn>1</mn><mn>6</mn></mfrac><mi mathvariant="normal">.</mi><mfrac><mn>1</mn><mn>111</mn></mfrac></mrow></mfrac><mo>&#8658;</mo><msup><mi>h</mi><mo>&#39;</mo></msup><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>666</mn></math>
If <math><mi>g</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>g</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mn>0</mn></mfenced><mi>&#160;</mi><mo>&#8658;</mo><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msup><mi>g</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mn>2</mn></mfenced><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><mi>f</mi><mfenced separators="|"><mn>2</mn></mfenced><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><mn>16</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>h</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>16</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><msup><mi>g</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>f</mi><mfenced separators="|"><mn>3</mn></mfenced><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><mn>38</mn></math>
So <math><mi>h</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>38</mn></math></p>

</details>

---

### Q3. JEE Advanced 2013 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `1`

Let <math> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>f</mi><mo>&#8289;</mo> <mfenced close=")" open="(" separators=","> <mrow> <mtext>x</mtext> </mrow> </mfenced> <mo>=</mo> <mtext>x&#160;</mtext> <mtext>sin&#160;</mtext> <mi>&#960;</mi> <mtext>x</mtext> </mrow> </math>, <math> <mrow> <mtext>x</mtext> <mo>&#62;</mo> <mn>0</mn> </mrow> </math>. Then for all natural numbers <math> <mrow> <mtext>n</mtext> <mtext>,&#160;</mtext> <msup> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>f</mi><mo>&#8289;</mo> </mrow> <mo>&#8242;</mo> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mtext>x</mtext> </mrow> </mfenced> </mrow> </math> vanishes at

**Options:**

- **(A)** A unique point in the interval <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mtext>n</mtext> <mtext>, </mtext> <mtext>n</mtext> <mo>+</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>
- **(B)** A unique point in the interval <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mtext>n</mtext> <mo>+</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mtext>, </mtext> <mtext>n</mtext> <mo>+</mo> <mn>1</mn> </mrow> </mfenced> </mrow> </math>
- **(C)** A unique point in the interval (n, n + 1)
- **(D)** Two points in the interval (n, n + 1)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) A unique point in the interval (n, n + 1)**

**Detailed Solution:**

<p><math> <mrow> <mtext>f</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mtext>x</mtext> </mrow> </mfenced> <mo>=</mo> <mtext>x sin </mtext> <mi>π</mi> <mtext>x</mtext> <mo>,</mo> <mtext>x</mtext> <mo>></mo> <mn>0</mn> </mrow> </math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>'</mo><mfenced><mi>x</mi></mfenced></math> vanishes,
<math> <mrow> <msup> <mtext>f</mtext> <mo>′</mo> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mtext>x</mtext> </mrow> </mfenced> <mo>=</mo> <mtext>sin </mtext> <mi>π</mi> <mtext>x</mtext> <mo>+</mo> <mi>π</mi> <mo>x cos</mo> <mi>π</mi> <mtext>x</mtext> <mo>=</mo> <mn>0</mn> </mrow> </math>
<math> <mrow> <mtext>tan</mtext> <mi>π</mi> <mtext>x</mtext> <mo>=</mo> <mo>-</mo> <mi>π</mi> <mtext>x</mtext> </mrow> </math></p><p>We will draw the graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tanπ</mi><mi>x</mi><mo> </mo><mo>&</mo><mo> </mo><mo>-</mo><mi>πx</mi></math>.</p><p>And their intersection points will be the points, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>'</mo><mfenced><mi>x</mi></mfenced></math> vanishes.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM0012559_AnsExp1_1.jpg"/></p>

</details>

---

### Q4. JEE Advanced 2010 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f$ be a real-valued function defined on the interval $(-1,1)$ such that $e^{-x} f(x)=2+\int_0^x \sqrt{t^4+1} d t, \quad$ for all $x \in(-1,1)$ and let $f^{-1}$ be the inverse function of $f$. Then $\left(f^{-1}\right)^{\prime}(2)$ is equal to

**Options:**

- **(A)** 1
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{1}{e}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{3}$**

**Detailed Solution:**

We have, $e^{-x} f(x)=2+\int_0^x \sqrt{t^4+1} d t x \in(-1,1)$
On differentiating w.r.t. $x$, we get
$$
\begin{array}{ll} 
& e^{-x}\left(f^{\prime}(x)-f(x)\right)=\sqrt{x^4+1} \\
\Rightarrow \quad & f^{\prime}(x)=f(x)+\sqrt{x^4+1} e^x \\
\because & f^{-1} \text { is the inverse of } f \\
\therefore & f^{-1}(f(x))=x \\
\Rightarrow & f^{-1^{\prime}}(f(x)) f^{\prime}(x)=1 \\
\Rightarrow & f^{-1^{\prime}}(f(x))=\frac{1}{f^{\prime}(x)} \\
\Rightarrow \quad & f^{-1^{\prime}}(f(x))=\frac{1}{f(x)+\sqrt{x^4+1} e^x} \\
\text { At } \quad & x=0, f(x)=2 \\
& f^{-1^{\prime}}(2)=\frac{1}{2+1}=\frac{1}{3}
\end{array}
$$

</details>

---

### Q5. JEE Advanced 2009 (Paper 2)

*Type:* `numerical` | *Level:* `1`

If the function $f(x)=x^3+e^{\frac{x}{2}}$ and $g(x)=f^{-1}(x)$, then the value of $g^{\prime}(1)$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

Given, $g\{f(x)\}=x$
$$
\begin{array}{lc}
\Rightarrow & g^{\prime}\{f(x)\} f^{\prime}(x)=1 \\
\text { If } & f(x)=1 \Rightarrow x=0, f(0)=1
\end{array}
$$
Substitute $x=0$ in Eq. (i), we get
$$
\begin{aligned}
& g^{\prime}(1)=\frac{1}{f^{\prime}(0)} \\
& \Rightarrow \quad g^{\prime}(1)=2 \\
& {\left[\because f^{\prime}(x)=3 x^2+\frac{1}{2} e^{x / 2} \Rightarrow f^{\prime}(0)=\frac{1}{2}\right]} \\
&
\end{aligned}
$$

</details>

---

### Q6. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `2`

If $f^{\prime \prime}(x)=-f(x)$, where $f(x)$ is a continuous double differentiable function and $g(x)=f^{\prime}(x)$. If $F(x)=\left(f\left(\frac{x}{2}\right)\right)^2+\left(g\left(\frac{x}{2}\right)\right)^2$ and $F(5)=5$, then $F(10)$ is

**Options:**

- **(A)** 0
- **(B)** 5
- **(C)** 10
- **(D)** 25

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5**

**Detailed Solution:**

As, $f(x)=-f(x) \Rightarrow \frac{d}{d x}\left(f^{\prime}(x)\right)=-f(x)$ $\Rightarrow \quad g^{\prime}(x)=-f(x)$ and $f^{\prime}(x)=g(x)$ where, $\therefore \quad F^{\prime}(x)=2\left(f\left(\frac{x}{2}\right)\right) \cdot f^{\prime}\left(\frac{x}{2}\right) \cdot \frac{1}{2}+2\left(g\left(\frac{x}{2}\right)\right) \cdot g^{\prime}\left(\frac{x}{2}\right) \cdot \frac{1}{2}=0$ [using Eq. (1)] $\therefore F(x)$ is constant $\Rightarrow F(10)=F(5)=5$

</details>

---

