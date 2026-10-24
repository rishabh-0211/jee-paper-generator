# JEE Advanced Mathematics - Application of Derivatives

## Topic 2: Monotonicity

**Total Questions:** 21

---

### Q1. JEE Advanced 2025 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

Let $\mathbb{R}$ denote the set of all real numbers. Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be defined by
$f(x)= \begin{cases}\frac{6 x+\sin x}{2 x+\sin x} & \text { if } x \neq 0 \\ \frac{7}{3} & \text { if } x=0\end{cases}$
Then which of the following statements is (are) TRUE?

**Options:**

- **(A)** The point $x=0$ is a point of local maxima of $f$
- **(B)** The point $x=0$ is a point of local minima of $f$
- **(C)** Number of points of local maxima of $f$ in the interval $[\pi, 6 \pi]$ is 3
- **(D)** Number of points of local minima of $f$ in the interval $[2 \pi, 4 \pi]$ is 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Number of points of local minima of $f$ in the interval $[2 \pi, 4 \pi]$ is 1**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/YOAQtF2lIQZbLvMQU2Kb97w_YElrCvhCcyB1fIgG6n0.original.fullsize.png">
since $3>\frac{7}{3} \Rightarrow 3>f(0)$
$\Rightarrow x=0$ is local minima ....option (B) is correct
Now,
$\begin{aligned}
& f(x)=\frac{6 x+\sin x}{2 x+\sin x}=1+\frac{4 x}{2 x+\sin x} \\
& f^{\prime}(x)=\frac{4[(2 x+\sin x) \cdot 1-x(2+\cos x)]}{(2 x+\sin x)^2}=\frac{4(\sin x-x \cos x)}{(2 x+\sin x)^2} \\
& =\frac{4 \cos x(\tan x-x)}{(2 x+\sin x)^2}
\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/zujoepFwVCDbgl5WHjsUd8CnWvhST8OrJOTL61o5Bi4.original.fullsize.png">
Options (C) \& (D) are also correct.

</details>

---

### Q2. JEE Advanced 2025 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathbb{R}$ denote the set of all real numbers. Define the function $f: \mathbb{R \rightarrow \mathbb { R }}$ by
$f(\mathrm{x})=\left\{\begin{array}{cc}2-2 x^2-x^2 \sin \frac{1}{x} & \text { if } x \neq 0 \\ 2 & \text { if } x=0\end{array}\right.$
Then which one of the following statements is TRUE ?

**Options:**

- **(A)** $\text { The function } f \text { is NOT differentiable at } x=0$
- **(B)** There is a positive real number $\delta$, such that $f$ is a decreasing function on the interval $(0, \delta)$
- **(C)** For any positive real number $\delta$, the function $f$ is NOT an increasing function on the interval $(-\delta, 0)$
- **(D)** $x=0$ is a point of local minima of $f$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) For any positive real number $\delta$, the function $f$ is NOT an increasing function on the interval $(-\delta, 0)$**

**Detailed Solution:**

(A)
RHD at $x=0: \lim _{h \rightarrow 0} \frac{\left(2-2 h^2-h^2 \sin \frac{1}{h}\right)-2}{h}=0$
Similarly LHD at $\mathrm{x}=0$ is also equal to 0 .
$\therefore$ Differentiable at $\mathrm{x}=0$
(B) $f^{\prime}(x)=-4 x-2 x \sin \frac{1}{x}-x^2\left(\cos \frac{1}{x}\right)\left(\frac{-1}{x^2}\right)$
$\begin{aligned}
& f^{\prime}(x)=-\left(4 x+2 x \sin \frac{1}{x}\right)+\cos \frac{1}{x} \\
& f^{\prime}(x)=-\left(2 x\left(4-\sin \frac{1}{x}\right)\right)+\cos \frac{1}{x}
\end{aligned}$
for $\mathrm{x} \in(0, \delta)$
$\Rightarrow$ We can't say $f(x)$ is decreasing on $(0, \delta)$ as $\cos \frac{1}{x}$ oscillates.
(C) for $x \in(-\delta, 0)$, for any $\delta>0$
$\Rightarrow f(x)$ is not increasing on $(-\delta, 0)$ as $\cos \frac{1}{x}$ oscillates from -1 to 1.
(D) $f(0)=2$
$\begin{aligned}
& f(0+h) <2 \\
& f(0-h) <2
\end{aligned}$
$\therefore \mathrm{x}=0$ is local maxima

</details>

---

### Q3. JEE Advanced 2024 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let the function $f: \mathbb{R} \rightarrow \mathbb{R}$ be defined by
$f(x)=\frac{\sin x}{e^{\pi x}} \frac{\left(x^{2023}+2024 x+2025\right)}{\left(x^2-x+3\right)}+\frac{2}{e^{\pi x}} \frac{\left(x^{2023}+2024 x+2025\right)}{\left(x^2-x+3\right)}$.
Then the number of solutions of $f(x)=0$ in $\mathbb{R}$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

$f(x)=\frac{\left(x^{2023}+2024 x+2025\right)}{e^{\pi x}\left(x^2-x+3\right)}(\sin x+2)$
$\because(\sin x+2)$ is never zero
$\therefore$ for $x^{2023}+2024 x+2025=0$
$\begin{aligned} & \text { let } \phi(\mathrm{x})=\mathrm{x}^{2023}+2024 \mathrm{x}+2025 \\ & \phi^{\prime}(\mathrm{x})=2023 \mathrm{x}^{2022}+2024>0 \forall \mathrm{x} \in \mathrm{R}\end{aligned}$
$\therefore \phi(\mathrm{x})$ is an Strictly Increasing function
$\therefore \phi(\mathrm{x})=0$ for exactly one value of $\mathrm{x}$
$\therefore \mathrm{f}(\mathrm{x})=0$ has one solution

</details>

---

### Q4. JEE Advanced 2023 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let S be the set of all twice differentiable functions f from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8477;</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8477;</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>f</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>. For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#8712;</mo><mi>S</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>f</mi></msub></math> be the number of points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math>. Then which of the following statements is(are) true?

**Options:**

- **(A)** There exists a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#8712;</mo><mi>S</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>f</mi></msub><mo>=</mo><mn>0</mn></math>
- **(B)** For every function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#8712;</mo><mi>S</mi></math>, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>f</mi></msub><mo>&#8804;</mo><mn>2</mn></math>
- **(C)** There exists a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#8712;</mo><mi>S</mi></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>f</mi></msub><mo>=</mo><mn>2.</mn></math>
- **(D)** There does NOT exist any function f in S such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>f</mi></msub><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) There exists a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#8712;</mo><mi>S</mi></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>f</mi></msub><mo>=</mo><mn>2.</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p>Now let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8722;</mo><mi>x</mi></math></p><p>Now differentiating above equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8722;</mo><mn>1</mn></math></p><p>Again differentiating we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#34;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#62;</mo><mn>0</mn><mo stretchy="false">&#8658;</mo><mtext>&#160;concave&#160;up&#160;</mtext></math></p><p>So, possible graphs will be,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/a79e19ff-20b5-4456-9475-52ae182ac5a0.png" style="width: 300px; height: 279px;" /></p><p>Here in above graph <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>f</mi></msub><mo>=</mo><mn>0</mn></math> as there is no point for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/5f91144b-1001-485a-b8b2-a224e6789540.png" style="width: 350px; height: 271px;" /></p><p>Now here <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>f</mi></msub><mo>&#8804;</mo><mn>2</mn></math> as there will be minimum two points when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi></math> will cut the given graph,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/6397b368-ad8d-4569-9978-091c93cc06da.png" style="width: 350px; height: 263px;" /></p><p>Now in above graph <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>f</mi></msub><mo>=</mo><mn>1</mn></math> so there will minimum one intersection between line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi></math> and the given graph so option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>D</mi></mfenced></math> is wrong.</p>

</details>

---

### Q5. JEE Advanced 2021 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

<strong> Paragraph: </strong>

Let $\psi_{1}:[0, \infty) \rightarrow \mathbb{R}, \psi_{2}:[0, \infty) \rightarrow \mathbb{R}, f:[0, \infty) \rightarrow \mathbb{R}$ and $g:[0, \infty) \rightarrow \mathbb{R}$ be functions such that $f(0)=g(0)=0$,

$\psi_{1}(x)=e^{-x}+x, \quad x \geq 0$,

$\psi_{2}(x)=x^{2}-2 x-2 e^{-x}+2, \quad x \geq 0$,

$f(x)=\int_{-x}^{x}\left(|t|-t^{2}\right) e^{-t^{2}} d t, \quad x>0$

and $g(x)=\int_{0}^{x^{2}} \sqrt{t} e^{-t} d t, \quad x>0$


 <strong> Question: </strong>

Which of the following statements is TRUE ?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#968;</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mn>1</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#968;</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mn>0</mn><mo>,</mo></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msup><mi>x</mi><mn>5</mn></msup></math>, for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><msup><mi>x</mi><mn>7</mn></msup></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><msup><mi>x</mi><mn>7</mn></msup></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>(A) Given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#968;</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>x</mi><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><msup><mi>&#968;</mi><mo>&#39;</mo></msup><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><msup><mi>&#968;</mi><mo>&#39;</mo></msup><mn>1</mn></msub><mfenced><mi>x</mi></mfenced></math> is increasing function.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#968;</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><msub><mi>&#968;</mi><mn>1</mn></msub><mfenced><mn>0</mn></mfenced><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#968;</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>1</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math> is incorrect.</p><p>LHS is increasing and unbounded function.</p><p>(B) Given<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#968;</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><msup><mi>&#968;</mi><mo>&#39;</mo></msup><mn>2</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><msup><mi>&#968;</mi><mo>&#39;</mo></msup><mn>2</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msub><mi>&#968;</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>2</mn><mo>&#160;</mo><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#968;</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced></math> is increasing function.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn><mo>&#60;</mo><mn>1</mn></math>
for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math> is incorrect because LHS <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mo>&#8734;</mo></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></math></p><p>(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mrow><mi>t</mi><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mfenced><mrow><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></msup></mrow></mfenced><mn>0</mn><mi>x</mi></msubsup><mo>-</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>t</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>-</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>t</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mfrac><msup><mi>t</mi><mn>4</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#8943;</mo><mo>.</mo><mo>.</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>5</mn></msup></mrow><mn>5</mn></mfrac><mo>&#60;</mo><mn>0</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></msubsup><msqrt><mi>t</mi></msqrt><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>t</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msup><mi>z</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mn>2</mn><msup><mi>z</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>z</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mn>2</mn><msup><mi>z</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mfrac><msup><mi>z</mi><mn>4</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#8230;</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mi>d</mi><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>5</mn></msup></mrow><mn>5</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>7</mn></msup></mrow><mrow><mn>2</mn><mo>.</mo><mn>7</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><mo>&#183;</mo><msup><mi>x</mi><mn>9</mn></msup></mrow><mrow><mn>9</mn><mo>.</mo><mn>6</mn></mrow></mfrac><mo>-</mo><mo>&#8230;</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>5</mn></msup></mrow><mn>5</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>7</mn></msup></mrow><mrow><mn>2</mn><mo>.</mo><mn>7</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>5</mn></msup></mrow><mn>5</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>7</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>9</mn></msup></mrow><mn>6</mn></mfrac><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>-</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>-</mo><mfenced><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>5</mn></msup></mrow></mfenced></math></p><p>(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></msubsup><msqrt><mi>t</mi></msqrt><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></msubsup><msqrt><mi>t</mi></msqrt><mfenced><mrow><mn>1</mn><mo>-</mo><mi>t</mi><mo>+</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><msup><mi>x</mi><mn>7</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></msubsup><msqrt><mi>t</mi></msqrt><mfenced><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><msup><mi>x</mi><mn>5</mn></msup></math></p>

</details>

---

### Q6. JEE Advanced 2021 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

<strong> Paragraph: </strong>

Let $\psi_{1}:[0, \infty) \rightarrow \mathbb{R}, \psi_{2}:[0, \infty) \rightarrow \mathbb{R}, f:[0, \infty) \rightarrow \mathbb{R}$ and $g:[0, \infty) \rightarrow \mathbb{R}$ be functions such that $f(0)=g(0)=0$,

$\psi_{1}(x)=e^{-x}+x, \quad x \geq 0$,

$\psi_{2}(x)=x^{2}-2 x-2 e^{-x}+2, \quad x \geq 0$,

$f(x)=\int_{-x}^{x}\left(|t|-t^{2}\right) e^{-t^{2}} d t, \quad x>0$

and $g(x)=\int_{0}^{x^{2}} \sqrt{t} e^{-t} d t, \quad x>0$


 <strong> Question: </strong>

Which of the following statements is TRUE ?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msqrt><mi>ln</mi><mn>3</mn></msqrt></mfenced><mo>+</mo><mi>g</mi><mfenced><msqrt><mi>ln</mi><mn>3</mn></msqrt></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(B)** For every <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>1</mn></math>, there exists an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mi>x</mi></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#968;</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mi>&#945;</mi><mi>x</mi></math>
- **(C)** For every <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>, there exists a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>x</mi></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#968;</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mfenced><mrow><msub><mi>&#968;</mi><mn>1</mn></msub><mfenced><mi>&#946;</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is an increasing function on the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) For every <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>, there exists a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>x</mi></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#968;</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mfenced><mrow><msub><mi>&#968;</mi><mn>1</mn></msub><mfenced><mi>&#946;</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>(A) Given</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mrow><mi>t</mi><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>t</mi><mo>;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></msubsup><msqrt><mi>t</mi></msqrt><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>t</mi><mo>;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>
put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msup><mi>u</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>u</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>u</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>u</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>t</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>t</mi></math></p><p>now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mn>2</mn><mi>t</mi><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>t</mi><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><msqrt><mi>ln</mi><mn>3</mn></msqrt><mo>)</mo><mo>+</mo><mi mathvariant="normal">g</mi><mo>(</mo><msqrt><mi>ln</mi><mn>3</mn></msqrt><mo>)</mo><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>ln</mi><mn>3</mn></mrow></msup><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>(B) for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mi>x</mi><mo>)</mo><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#968;</mi><mn>1</mn></msub><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>+</mo><mi>&#945;</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>-</mo><mi>&#945;</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>x</mi><mo>(</mo><mi>&#945;</mi><mo>-</mo><mn>1</mn><mo>)</mo></math>
Which is not possible because LHS <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#60;</mo><mn>0</mn></math> &amp; RHS <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#62;</mo><mn>0</mn></math></p><p>(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#968;</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mfenced><mrow><msub><mi>&#968;</mi><mn>1</mn></msub><mfenced><mi>&#946;</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><msup><mi>&#968;</mi><mo>'</mo></msup><mn>2</mn></msub><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2</mn><msub><mi>&#968;</mi><mn>1</mn></msub><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><mn>2</mn></math></p><p>from LMVT, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>&#968;</mi><mn>2</mn></msub><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>-</mo><msub><mi>&#968;</mi><mn>2</mn></msub><mo>(</mo><mn>0</mn><mo>)</mo></mrow><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mn>0</mn></mrow></mfrac><mo>=</mo><msubsup><mi>&#968;</mi><mn>2</mn><mo>'</mo></msubsup><mfenced><mi>&#946;</mi></mfenced></math> for atleast one <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#8712;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#968;</mi><mn>2</mn></msub><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><mn>2</mn><mi mathvariant="normal">x</mi><mfenced><mrow><msub><mi>&#968;</mi><mn>1</mn></msub><mo>(</mo><mi>&#946;</mi><mo>)</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>(D) Given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>x</mi></mrow><mi>x</mi></msubsup><mfenced><mrow><mfenced close="|" open="|"><mi>t</mi></mfenced><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>t</mi><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>0</mn><mo>&#160;</mo><mtext>for</mtext><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> So, increasing in this interval.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mn>0</mn><mo>&#160;</mo><mtext>for</mtext><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math> So, decreasing in this interval.</p>

</details>

---

### Q7. JEE Advanced 2018 (Paper 1)

*Type:* `numerical` | *Level:* `3`

The number of real solutions of the equation <math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><msup><mrow><mi>x</mi></mrow><mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>-</mo><mi>x</mi></mrow></mrow><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>i</mi></mrow></msup></mrow></mrow></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>&#8734;</mi><mi>&#160;</mi></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>i</mi></mrow></msup><mo>-</mo><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mi>i</mi></mrow></msup></mrow></mrow></mrow></mrow></mrow></mfenced></mrow></mrow></mrow></mrow></math> lying in the interval <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> is____.
(Here, the inverse trigonometric functions <math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mo>&#160;</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></math> assume values in <math><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mi>&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math>
respectively.)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><math><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><msup><mrow><mi>x</mi></mrow><mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow></msup></mrow></mrow><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></math>
<math><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>i</mi></mrow></msup><mo>=</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mrow></mrow></math>
<math><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>i</mi></mrow></msup><mo>=</mo><mfrac><mrow><mo>-</mo><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mrow></mrow></math>
<math><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mi>i</mi></mrow></msup></mrow></mrow><mo>=</mo><mfrac><mrow><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></math>
For the given equation to have real solutions
<math><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><msup><mrow><mi>x</mi></mrow><mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow></msup></mrow></mrow><mo>-</mo><mi>x</mi><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>i</mi></mrow></msup><mo>=</mo><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>i</mi></mrow></msup><mo>-</mo><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mi>i</mi></mrow></msup></mrow></mrow></mrow></mrow></mrow></mrow></math>
<math><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></math>
<math><mi>x</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mi>i</mi><mi>s</mi><mo>&#160;</mo><mi>a</mi><mo>&#160;</mo><mi>s</mi><mi>o</mi><mi>l</mi><mi>u</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>,</mo><mi>a</mi><mi>l</mi><mi>s</mi><mi>o</mi><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>2</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>5</mn><mspace linebreak="newline"></mspace><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>D</mi><mo>=</mo><mn>16</mn><mo>-</mo><mn>60</mn><mo>=</mo><mo>-</mo><mn>44</mn><mo>&#60;</mo><mn>0</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>f</mi><mo>&#160;</mo><mi>i</mi><mi>s</mi><mo>&#160;</mo><mi>s</mi><mi>t</mi><mi>r</mi><mi>i</mi><mi>c</mi><mi>t</mi><mi>l</mi><mi>y</mi><mo>&#160;</mo><mi>i</mi><mi>n</mi><mi>c</mi><mi>r</mi><mi>e</mi><mi>a</mi><mi>sin</mi><mi>g</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>n</mi><mi>d</mi><mo>&#160;</mo><mo>&#8757;</mo><mo>&#160;</mo><mi>f</mi><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>.</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi><mi>e</mi><mi>n</mi><mi>c</mi><mi>e</mi><mo>&#160;</mo><mi>t</mi><mi>w</mi><mi>o</mi><mo>&#160;</mo><mi>s</mi><mi>o</mi><mi>l</mi><mi>u</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mo>&#160;</mo><mi>e</mi><mi>x</mi><mi>i</mi><mi>s</mi><mi>t</mi><mo>.</mo></math></p>

</details>

---

### Q8. JEE Advanced 2017 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mi>x</mi><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></msub></mrow><mo>&#8289;</mo><mrow><mi>x</mi><mo>,</mo></mrow></mrow><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced><mo>.</mo><mi>&#160;</mi></math>
<math> <mrow> <mo>&#8226;</mo> </mrow> </math>   Column 1 contains information about zeros of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>.</mo></math>
<math> <mrow> <mo>&#8226;</mo> </mrow> </math>   Column 2 contains information about the limiting behaviour of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> at infinity.
<math> <mrow> <mo>&#8226;</mo> </mrow> </math>   Column 3 contains information about increasing-decreasing nature of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>.</mo></math>
 <table border="1">	<tbody>		<tr>			<td>Column 1</td>			<td>Column 2</td>			<td>Column 3</td>		</tr>		<tr>			<td>(I) <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for some <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math></td>			<td>(i) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder></mrow><mo>&#8289;</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math></td>			<td>(P) <math><mi>f</mi></math> is increasing in (0, 1)</td>		</tr>		<tr>			<td>(II) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for some <math><mi>x</mi><mi>&#160;</mi><mi>i</mi><mi>n</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>e</mi></mrow></mfenced></math></td>			<td>(ii) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder></mrow><mo>&#8289;</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mo>-</mo><mi>&#8734;</mi></math></td>			<td>(Q) <math><mi>f</mi></math> is decreasing in <math><mfenced separators="|"><mrow><mi>e</mi><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td>(III) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for some <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math></td>			<td>(iii) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder></mrow><mo>&#8289;</mo><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mo>-</mo><mi>&#8734;</mi></math></td>			<td>(R) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup></math> is increasing in (0, 1)</td>		</tr>		<tr>			<td>(IV) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for some <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>e</mi></mrow></mfenced></math></td>			<td>(iv) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder></mrow><mo>&#8289;</mo><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math></td>			<td>(S) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup></math> is decreasing in <math><mfenced separators="|"><mrow><mi>e</mi><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>	</tbody></table>Which of the following options is the only Correct combination?

**Options:**

- **(A)** (I) (i) (P)
- **(B)** (II) (ii) (Q)
- **(C)** (IV) (iv) (S)
- **(D)** (III) (iii) (R)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (II) (ii) (Q)**

**Detailed Solution:**

<p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>ℓ</mi><mi>n</mi><mi>x</mi><mo>-</mo><mi>x</mi><mi>ℓ</mi><mi>n</mi><mi>x</mi><mo>,</mo><mi> </mi><mi>x</mi><mo>></mo><mn>0</mn></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mi>ℓ</mi><mi>n</mi><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/52_to_54_solu_math_pap1.jpg"/></p><p>(I)  <math><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo><</mo><mn>0</mn></math>, so true.</p><p>(II)   <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mi> </mi><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>e</mi></mrow></mfenced><mo><</mo><mn>0</mn></math>, so true.</p><p>(III) Graph of <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>, so (III) is false.</p><p>(IV) Is false.</p><p>As   <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mi> </mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mi mathvariant="script"> </mi><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mo>-</mo><mi>∞</mi></math></p><p><math><mo>∴</mo></math>  (i) is false (ii) is true.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder><mo>⁡</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mi>∞</mi></math>, so (iii) is true.</p><p><math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math>,so (iv) is true.</p><p>(P)  <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>   is positive in (0, 1) so true</p><p>(Q)  <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo><</mo><mn>0</mn></math>  for in <math><mfenced separators="|"><mrow><mi>e</mi><mo>,</mo><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math> so true</p><p>As  <math><msup><mrow><mi>f</mi></mrow><mrow><mi>"</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo><</mo><mn>0</mn><mi> </mi><mo>∀</mo><mi> </mi><mi>x</mi><mo>></mo><mn>0</mn></math> therefore, R is false, S is true.</p><p><strong>Alternate:</strong></p><p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi> </mi><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi><mo>-</mo><mi>x</mi><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi><mo>=</mo><mn>0</mn></math> at <math><mi>x</mi><mo>=</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>0</mn></mrow></msub></math> where <math><msub><mrow><mi>x</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>∈</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mi>e</mi></mrow></mfenced></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo><</mo><mn>0</mn><mi> </mi><mo>∀</mo><mi> </mi><mi>x</mi><mo>></mo><mn>0</mn><mi> </mi><mo>⇒</mo><mi> </mi><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  concave down</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/52_to_54_solu_math_pap1_2.jpg"/></p>

</details>

---

### Q9. JEE Advanced 2017 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mi>x</mi><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></msub></mrow><mo>&#8289;</mo><mrow><mi>x</mi><mo>,</mo></mrow></mrow><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced><mo>.</mo><mi>&#160;</mi></math>
<math> <mrow> <mo>&#8226;</mo> </mrow> </math>   Column 1 contains information about zeros of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>.</mo></math>
<math> <mrow> <mo>&#8226;</mo> </mrow> </math>   Column 2 contains information about the limiting behaviour of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> at infinity.
<math> <mrow> <mo>&#8226;</mo> </mrow> </math>   Column 3 contains information about increasing-decreasing nature of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>.</mo></math>
 <table border="1">	<tbody>		<tr>			<td>Column 1</td>			<td>Column 2</td>			<td>Column 3</td>		</tr>		<tr>			<td>(I) <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for some <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math></td>			<td>(i) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder></mrow><mo>&#8289;</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math></td>			<td>(P) <math><mi>f</mi></math> is increasing in (0, 1)</td>		</tr>		<tr>			<td>(II) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for some <math><mi>x</mi><mi>&#160;</mi><mi>i</mi><mi>n</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>e</mi></mrow></mfenced></math></td>			<td>(ii) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder></mrow><mo>&#8289;</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mo>-</mo><mi>&#8734;</mi></math></td>			<td>(Q) <math><mi>f</mi></math> is decreasing in <math><mfenced separators="|"><mrow><mi>e</mi><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td>(III) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for some <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math></td>			<td>(iii) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder></mrow><mo>&#8289;</mo><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mo>-</mo><mi>&#8734;</mi></math></td>			<td>(R) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup></math> is increasing in (0, 1)</td>		</tr>		<tr>			<td>(IV) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for some <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>e</mi></mrow></mfenced></math></td>			<td>(iv) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder></mrow><mo>&#8289;</mo><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math></td>			<td>(S) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup></math> is decreasing in <math><mfenced separators="|"><mrow><mi>e</mi><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>	</tbody></table>Which of the following options is the only Incorrect combination?

**Options:**

- **(A)** (II) (iv) (Q)
- **(B)** (III) (i) (R)
- **(C)** (I) (iii) (P)
- **(D)** (II) (iii) (P)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (III) (i) (R)**

**Detailed Solution:**

<p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>ℓ</mi><mi>n</mi><mi>x</mi><mo>-</mo><mi>x</mi><mi>ℓ</mi><mi>n</mi><mi>x</mi><mo>,</mo><mi> </mi><mi>x</mi><mo>></mo><mn>0</mn></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mi>ℓ</mi><mi>n</mi><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/52_to_54_solu_math_pap1.jpg"/></p><p>(I)  <math><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo><</mo><mn>0</mn></math>, so true.</p><p>(II) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mi> </mi><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>e</mi></mrow></mfenced><mo><</mo><mn>0</mn></math>,so true.</p><p>(III) Graph of <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> , so (III) is false as the curve does not intersect X-axis i.e, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>'</mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>≠</mo><mn>0</mn></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math></p><p>(IV) Is false. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>'</mo><mo>'</mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>≠</mo><mn>0</mn><mo> </mo></math>as tangent to the curve of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>'</mo><mo>(</mo><mi>x</mi><mo>)</mo></math> is not parallel to X-axis.</p><p>As   <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mi> </mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mi mathvariant="script"> </mi><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mo>-</mo><mi>∞</mi></math></p><p><math><mo>∴</mo></math>  (i) is false (ii) is true</p><p><math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mi> </mi><mo>-</mo><mi>∞</mi></math>, so (iii) is true</p><p><math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math> , so (iv) is true.</p><p>(P)  <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>, is positive in<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo> </mo><mn>1</mn><mo>)</mo></math>, so true.</p><p>(Q)  <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo><</mo><mn>0</mn></math>, for in <math><mfenced separators="|"><mrow><mi>e</mi><mo>,</mo><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>, so true.</p><p>As  <math><msup><mrow><mi>f</mi></mrow><mrow><mi>"</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo><</mo><mn>0</mn><mi> </mi><mo>∀</mo><mi> </mi><mi>x</mi><mo>></mo><mn>0</mn></math> therefore, R is false, S is true.</p><p><strong>Alternate:</strong></p><p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi> </mi><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi><mo>-</mo><mi>x</mi><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi><mo>=</mo><mn>0</mn></math> at <math><mi>x</mi><mo>=</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>0</mn></mrow></msub></math> where <math><msub><mrow><mi>x</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>∈</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mi>e</mi></mrow></mfenced></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo><</mo><mn>0</mn><mi> </mi><mo>∀</mo><mi> </mi><mi>x</mi><mo>></mo><mn>0</mn><mi> </mi><mo>⇒</mo><mi> </mi><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  concave down</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/52_to_54_solu_math_pap1_2.jpg"/></p>

</details>

---

### Q10. JEE Advanced 2017 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><mi>x</mi><mo>-</mo><mi>x</mi><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mo>&#8289;</mo><mi>x</mi><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced></math>
<math> <mrow> <mo>&#8226;</mo> </mrow> </math>   Column 1 contains information about zeros of <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> </math> , <math> <mrow> <mi>f</mi><mo>&#39;</mo><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> </math> and <math> <mrow> <mi>f</mi><mo>&#39;</mo><mo>&#39;</mo><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> </math>
<math> <mrow> <mo>&#8226;</mo> </mrow> </math>   Column 2 contains information about the limiting behaviour of <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> </math> , <math> <mrow> <mi>f</mi><mo>&#39;</mo><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> </math> and <math> <mrow> <mi>f</mi><mo>&#39;</mo><mo>&#39;</mo><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> </math> at infinity.
<math> <mrow> <mo>&#8226;</mo> </mrow> </math>   Column 3 contains information about increasing-decreasing nature of <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> </math> and <math> <mrow> <mi>f</mi><mo>&#39;</mo><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> </math><table border="1">	<tbody>		<tr>			<td>Column 1</td>			<td>Column 2</td>			<td>Column 3</td>		</tr>		<tr>			<td>(I) <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for some <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math></td>			<td>(i) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder></mrow><mo>&#8289;</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math></td>			<td>(P) <math><mi>f</mi></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo></math></td>		</tr>		<tr>			<td>(II) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for some <math><mi>x</mi><mi>&#160;</mi><mi>i</mi><mi>n</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>e</mi></mrow></mfenced></math></td>			<td>(ii) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder></mrow><mo>&#8289;</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mo>-</mo><mi>&#8734;</mi></math></td>			<td>(Q) <math><mi>f</mi></math> is decreasing in <math><mfenced separators="|"><mrow><mi>e</mi><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td>(III) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for some <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math></td>			<td>(iii) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder></mrow><mo>&#8289;</mo><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mo>-</mo><mi>&#8734;</mi></math></td>			<td>(R) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo></math></td>		</tr>		<tr>			<td>(IV) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> for some <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>e</mi></mrow></mfenced></math></td>			<td>(iv) <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder></mrow><mo>&#8289;</mo><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math></td>			<td>(S) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup></math> is decreasing in <math><mfenced separators="|"><mrow><mi>e</mi><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>	</tbody></table>

**Options:**

- **(A)** (III) (iv) (P)
- **(B)** (I) (ii) (R)
- **(C)** (II) (iii) (S)
- **(D)** (IV) (i) (S)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) (II) (iii) (S)**

**Detailed Solution:**

<p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>ℓ</mi><mi>n</mi><mi>x</mi><mo>-</mo><mi>x</mi><mi>ℓ</mi><mi>n</mi><mi>x</mi><mo>,</mo><mi> </mi><mi>x</mi><mo>></mo><mn>0</mn></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mi>ℓ</mi><mi>n</mi><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math></p><p>In Column 1,</p><p>(I)  <math><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo><</mo><mn>0</mn></math> so true</p><p>(II)   <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mi> </mi><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>e</mi></mrow></mfenced><mo><</mo><mn>0</mn></math> so true</p><p>(III)   <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is always positive for <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> so it cannot be zero. So (III) is false.</p><p>(IV) Is false</p><p>In Column 2</p><p>As   <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mi> </mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mi mathvariant="script"> </mi><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mo>-</mo><mi>∞</mi></math></p><p><math><mo>∴</mo></math> (i)  is false (ii) is true</p><p><math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mi> </mi><mo>-</mo><mi>∞</mi></math> ,so (iii) is true.</p><p><math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder></mrow><mo>⁡</mo><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mn>0</mn></math>, so (iv) is true.</p><p>(P)  <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is positive in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo> </mo><mn>1</mn><mo>)</mo></math>,so true.</p><p>(Q)  <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo><</mo><mn>0</mn></math> ,for in <math><mfenced separators="|"><mrow><mi>e</mi><mo>,</mo><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math> ,so true.</p><p>As  <math><msup><mrow><mi>f</mi></mrow><mrow><mi>''</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo><</mo><mn>0</mn><mi> </mi><mo>∀</mo><mi> </mi><mi>x</mi><mo>></mo><mn>0</mn></math> therefore, R is false, S is true.</p><p><strong>Alternate Solution:</strong></p><p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi> </mi><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi><mo>-</mo><mi>x</mi><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mi>ℓ</mi><mi>n</mi><mi> </mi><mi>x</mi><mo>=</mo><mn>0</mn></math> at <math><mi>x</mi><mo>=</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>0</mn></mrow></msub></math> where <math><msub><mrow><mi>x</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>∈</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mi>e</mi></mrow></mfenced></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo><</mo><mn>0</mn><mi> </mi><mo>∀</mo><mi> </mi><mi>x</mi><mo>></mo><mn>0</mn><mi> </mi><mo>⇒</mo><mi> </mi><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  concave down</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/52_to_54_solu_math_pap1_2.jpg"/></p>

</details>

---

### Q11. JEE Advanced 2017 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> , be a continuous function then, which of the following function(s), has(have) the values zero at some point in the interval, (0,1)?

**Options:**

- **(A)** <math><mi>x</mi><mo>-</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi>x</mi></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced></mrow></mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>t</mi></mrow></mrow><mi>d</mi><mi>t</mi></math>
- **(B)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>9</mn></mrow></msup><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>
- **(C)** <math><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>-</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced></mrow></mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>t</mi></mrow></mrow><mi>d</mi><mi>t</mi></math>
- **(D)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced></mrow></mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>t</mi></mrow></mrow><mi>d</mi><mi>t</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msup><mrow><mi>x</mi></mrow><mrow><mn>9</mn></mrow></msup><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>**

**Detailed Solution:**

<p>For option (i),</p><p>Let  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>x</mi></mrow></msubsup><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mo>&#183;</mo><mi>cos</mi><mi>t</mi><mi>&#160;</mi><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>M</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mo>.</mo><mi>cos</mi><mi>t</mi><mi>&#160;</mi><mi>d</mi><mi>t</mi><mo>&#60;</mo><mn>0</mn></math></p><p>Also,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></msubsup><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mo>.</mo><mi>cost&#160;</mi><mi>d</mi><mi>t</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>M</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>.</mo><mi>&#160;</mi><mi>M</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math>     (so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> can be zero)</p><p>For option (ii),</p><p>Let,   <math><mi>k</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>9</mn></mrow></msup><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math></p><p>Now,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mo>-</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>&#60;</mo><mn>0</mn></math>, as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mi>f</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math></p><p>Also,  <math><mi>k</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mi>A</mi><mi>s</mi><mi>&#160;</mi><mi>f</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0,1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math><mo>&#8658;&#160;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>k</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>.</mo><mi>&#160;</mi><mi>k</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math>     (so <math> <mrow> <mi>k</mi><mo stretchy="false">(</mo><mi>x</mi><mo stretchy="false">)</mo> </mrow> </math> can be zero)</p><p>For option (iii),</p><p>Let  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mi>si</mi><mi mathvariant="normal">n</mi><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>g</mi><mo>&#39;</mo><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>&#183;</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math>    (as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#183;</mo><mtext>sin&#160;x</mtext></math> , is less than 1)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced></math> is strictly increasing function.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>&#62;</mo><mn>1</mn><mi>&#160;</mi><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math></p><p>Also,  <math><mi>g</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>, (so <math> <mrow> <mi>g</mi><mo stretchy="false">(</mo><mi>x</mi><mo stretchy="false">)</mo> </mrow> </math> is, never zero)</p><p>For option (iv),</p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mo>.</mo><mi>sin</mi><mi>t</mi><mi>&#160;</mi><mi>d</mi><mi>t</mi></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>T</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn><mi>&#160;</mi><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mi>A</mi><mi>s</mi><mi>&#160;</mi><mi>f</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></mrow></mfenced></math>     (so <math> <mrow> <mi>T</mi><mo stretchy="false">(</mo><mi>x</mi><mo stretchy="false">)</mo> </mrow> </math> can not be zero)</p><p> </p>

</details>

---

### Q12. JEE Advanced 2016 (Paper 1)

*Type:* `numerical` | *Level:* `3`

The total number of distinct <math><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math> for which, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><msup><mi>t</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>4</mn></msup></mrow></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><msup><mi>t</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>4</mn></msup></mrow></mfrac><mi>d</mi><mi>t</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></math>
<math><mo>&#8658;</mo></math> <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac><mo>-</mo><mn>2</mn></math>
As <math><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>&#160;</mi><mo>&#8805;</mo><mn>2</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfrac><mo>&#8804;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
<math><mo>&#8658;</mo></math> <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>&#160;</mi><mo>&#8804;</mo><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mo>&#8658;</mo></math> <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is continuous and decreasing
<math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mfenced><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><msup><mi>t</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>4</mn></msup></mrow></mfrac><mi>d</mi><mi>t</mi></mrow></mfenced><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mn>-1</mn><mn>2</mn></mfrac></math>
By intermediate value theorem (IVT),<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>possesses exactly one solution in [0, 1]. As <math> <mrow> <mi>f</mi><mo stretchy="false">(</mo><mn>0</mn><mo stretchy="false">)</mo><mi>f</mi><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo><mo>&#60;</mo><mn>0</mn>&#160;</mrow></math>

</details>

---

### Q13. JEE Advanced 2015 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

<strong> Paragraph: </strong>

Let $F: \mathbb{R} \rightarrow \mathbb{R}$ be a thrice differentiable function. Suppose that $F(1)=0, F(3)=-4$ and $F^{\prime}(x)<0$ for all $x \in(1 / 2,3)$. Let $f(x)=x F(x)$ for all $x \in \mathbb{R}$.


 <strong> Question: </strong>

The correct statement(s) is(are)

**Options:**

- **(A)** <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&lt;</mo><mn>0</mn></math>
- **(B)** <math><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>&lt;</mo><mn>0</mn></math>
- **(C)** <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>≠</mo><mn>0</mn><mi> </mi><mi>f</mi><mi>o</mi><mi>r</mi><mi> </mi><mi>a</mi><mi>n</mi><mi>y</mi><mi> </mi><mi>x</mi><mo>∈</mo><mo>(</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>3</mn><mo>)</mo></math>
- **(D)** <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mi> </mi><mi>f</mi><mi>o</mi><mi>r</mi><mi> </mi><mi>s</mi><mi>o</mi><mi>m</mi><mi>e</mi><mi> </mi><mi>x</mi><mo>∈</mo><mo>(</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>3</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>≠</mo><mn>0</mn><mi> </mi><mi>f</mi><mi>o</mi><mi>r</mi><mi> </mi><mi>a</mi><mi>n</mi><mi>y</mi><mi> </mi><mi>x</mi><mo>∈</mo><mo>(</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>3</mn><mo>)</mo></math>**

**Detailed Solution:**

<math><mi>F</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>F</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced><mo>=</mo><mi> </mi><mo>-</mo><mn>4</mn></math> 
 <math><msup><mrow><mi>F</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&lt;</mo><mn>0</mn></math> 
 <math><mi>F</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>  is decreasing, also  <math><mi>F</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&lt;</mo><mn>0</mn></math> 
Now,   <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mi>F</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> 
 <math><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi> </mi><mn>3</mn></mrow></mfenced><mi> </mi><mi>x</mi><mi>F</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&lt;</mo><mn>0</mn></math> 
 <math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>&lt;</mo><mn>0</mn></math> 
Also,
 <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><msup><mrow><mi>F</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mi>F</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> 
 <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mrow><mi>F</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&lt;</mo><mn>0</mn></math> 
Also,  <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>  is strictly decreasing
Now,   <math><mi>F</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mi>F</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> 
 <math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>≠</mo><mn>0</mn><mi> </mi><mi> </mi><mi> </mi><mi>a</mi><mi>s</mi><mi> </mi><msup><mrow><mi>F</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&lt;</mo><mn>0</mn><mi> </mi><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is decreasing.

</details>

---

### Q14. JEE Advanced 2015 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mo>,</mo><mi>&#160;</mi><mi>g</mi><mi>&#160;</mi><mo>:</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="double-struck">&#160;</mi><mi mathvariant="double-struck">R</mi></math>   be continuous functions which are twice differentiable on the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>. Let the values of <math><mi>f</mi></math> and <math><mi>g</mi></math> at the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> be as given in the following table:
 <table border="1">	<tbody>		<tr>			<td> </td>			<td><math><mi>x</mi><mo>=</mo><mi>&#160;</mi><mo>-</mo><mn>1</mn></math></td>			<td><math><mi>x</mi><mi>&#160;</mi><mo>=</mo><mi>&#160;</mi><mn>0</mn></math></td>			<td><math><mi>x</mi><mi>&#160;</mi><mo>=</mo><mi>&#160;</mi><mn>2</mn></math></td>		</tr>		<tr>			<td><math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math></td>			<td>3</td>			<td>6</td>			<td>0</td>		</tr>		<tr>			<td><math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math></td>			<td>0</td>			<td>1</td>			<td>-1</td>		</tr>	</tbody></table>
In each of the intervals <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>f</mi><mo>-</mo><mn>3</mn><mi>g</mi><mo>)</mo><mo>&#34;</mo></math> never vanishes. Then the correct statement(s) is(are)

**Options:**

- **(A)** <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mn>3</mn><msup><mrow><mi>g</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>  has exactly three solutions in  <math><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>0</mn></mrow></mfenced><mi> </mi><mo>∪</mo><mo>(</mo><mn>0</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>)</mo></math>
- **(B)** <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mn>3</mn><msup><mrow><mi>g</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>  has exactly one solution in (-1, 0)
- **(C)** <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mn>3</mn><msup><mrow><mi>g</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>  has exactly one solution in (0, 2)
- **(D)** <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mn>3</mn><msup><mrow><mi>g</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>  has exactly two solutions in (-1, 0) and exactly two solutions in (0, 2)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mn>3</mn><msup><mrow><mi>g</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>  has exactly one solution in (0, 2)**

**Detailed Solution:**

<math><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mn>3</mn><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> 
    <math><mi>h</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>3</mn><mo>-</mo><mn>0</mn><mo>=</mo><mn>3</mn></math> 
    <math><mi>h</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>6</mn><mo>-</mo><mn>3</mn><mo>=</mo><mn>3</mn></math> 
    <math><mi>h</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>3</mn></math> 
 <math><mi>h</mi><mi>&prime;</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>  has at least one root is  <math><mfenced separators="|"><mrow><mo>-</mo><mn>1,0</mn></mrow></mfenced></math> 
And  <math><msup><mrow><mi>h</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  has at least one in  <math><mo>(</mo><mn>0,2</mn><mo>)</mo></math> 
Hence  <math><msup><mrow><mi>h</mi></mrow><mrow><mi>&prime;</mi><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  atleast one root in  <math><mo>(</mo><mo>-</mo><mn>1,2</mn><mo>)</mo></math>  but
Also,  <math><msup><mrow><mfenced separators="|"><mrow><mi>f</mi><mo>-</mo><mn>3</mn><mi>g</mi></mrow></mfenced></mrow><mrow><mi>&prime;</mi><mi>&prime;</mi></mrow></msup><mo>≠</mo><mn>0</mn><mi> </mi><mi>i</mi><mi>n</mi><mi> </mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>0</mn></mrow></mfenced><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><mo>(</mo><mn>0</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>)</mo></math> 
    <math><msup><mrow><mi>h</mi></mrow><mrow><mi>&prime;</mi><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mi> </mi><mi>o</mi><mi>n</mi><mi>l</mi><mi>y</mi><mi> </mi><mi>a</mi><mi>t</mi><mi> </mi><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>s</mi><mi>o</mi></math> 
 <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mn>3</mn><msup><mrow><mi>g</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  has exactly one solution in (-1, 0) and (0, 2)

</details>

---

### Q15. JEE Advanced 2014 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mi>&#160;</mi><mo>:</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be given by <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow><mrow><mi>x</mi></mrow></munderover><mrow><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac></mrow></mfenced></mrow></msup></mrow></mrow><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>t</mi></mrow></mfrac><mo>,</mo></math> then

**Options:**

- **(A)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is monotonically increasing on  <math><mfenced open="[" separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mi>∞</mi></mrow></mfenced></math>
- **(B)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is monotonically decreasing on (0, 1)
- **(C)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math>  for all  <math><mi>x</mi><mi> </mi><mo>∈</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mi>∞</mi></mrow></mfenced></math>
- **(D)** <math><mi>f</mi><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mi>x</mi></mrow></msup></mrow></mfenced></math>  is an odd function of  <math><mi>x</mi></math>  on R

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>f</mi><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mi>x</mi></mrow></msup></mrow></mfenced></math>  is an odd function of  <math><mi>x</mi></math>  on R**

**Detailed Solution:**

<math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></msup></mrow><mrow><mi>x</mi></mrow></mfrac></math> 
Which is increasing in  <math><mfenced open="[" separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mi>∞</mi></mrow></mfenced></math> 
Also,   <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math> 
 <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mi>x</mi></mrow></msup></mrow></mfenced><mo>=</mo><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mi>x</mi></mrow></msup></mrow></munderover><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac></mrow></mfenced></mrow></msup></mrow><mrow><mi>t</mi></mrow></mfrac></mrow></mrow><mi> </mi><mi>d</mi><mi>t</mi></math> 
 <math><mi>g</mi><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><msup><mrow><mn>2</mn></mrow><mrow><mi>x</mi></mrow></msup></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></munderover><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac></mrow></mfenced></mrow></msup></mrow><mrow><mi>t</mi></mrow></mfrac></mrow></mrow><mi> </mi><mi>d</mi><mi>t</mi><mo>=</mo><mi> </mi><mo>-</mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> 
Hence, an odd function

</details>

---

### Q16. JEE Advanced 2011 (Paper 2)

*Type:* `numerical` | *Level:* `2`

The number of distinct real roots of $x^4-4 x^3+12 x^2+x-1=0$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

$f(x)=x^4-4 x^3+12 x^2+x-1$
$$
\begin{aligned}
f^{\prime}(x) & =4 x^3-12 x^2+24 x+1 \\
f^{\prime \prime}(x) & =12 x^2-24 x+24 \\
& =12\left(x^2-2 x+2\right) \\
& =12\left\{(x-1)^2+1\right\}>0, \text { for all } x
\end{aligned}
$$
$\Rightarrow f^{\prime}(x)$ is increasing.
Since, $f^{\prime}(x)$ is cubic and increasing. $\Rightarrow f^{\prime}(x)$ has only one real root and two imaginary roots.
$\therefore f(x)$ cannot have all distinct root.
$\Rightarrow$ Atmost 2 real roots.
Now, $f(-1)=15$,
$f(0)=-1$ and $f(1)=9$
$\therefore f(x)$ must have one root in $(-1,0)$ and other in $(0,1)$.
$\Rightarrow 2$ real roots.

</details>

---

### Q17. JEE Advanced 2008 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Consider the function $f:(-\infty, \infty) \rightarrow(-\infty, \infty)$ defined by $f(x)=\frac{x^2-a x+1}{x^2+a x+1} ; 0 < a < 2$<strong>Question:</strong>
Let $g(x)=\int_0^{e^x} \frac{f^{\prime}(t)}{1+t^2} d t$. Which of the following is true ?

**Options:**

- **(A)** $g^{\prime}(x)$ is positive on $(-\infty, 0)$ and negative on $(0, \infty)$
- **(B)** $g^{\prime}(x)$ is negative on $(-\infty, 0)$ and positive on $(0, \infty)$
- **(C)** $g^{\prime}(x)$ changes sign on both $(-\infty, 0)$ and $(0, \infty)$
- **(D)** $g^{\prime}(x)$ does not change sign on $(-\infty, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $g^{\prime}(x)$ is negative on $(-\infty, 0)$ and positive on $(0, \infty)$**

**Detailed Solution:**

$\because g^{\prime}(x)=\frac{f^{\prime}\left(e^x\right)}{1+\left(e^x\right)^2} \cdot e^x=2 a\left[\frac{e^{2 x}-1}{\left(e^{2 x}+a e^x+1\right)^2}\right]\left(\frac{e^x}{1+e^{2 x}}\right)$ $\begin{aligned} & g^{\prime}(x)=0 \text {, if } e^{2 x}-1 & =0, \\ \text { i.e., } & & x=0 \\ \text { If } & & x < 0, e^{2 x} < 1 \Rightarrow g^{\prime}(x) < 0 .\end{aligned}$

</details>

---

### Q18. JEE Advanced 2008 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

<strong>Paragraph:</strong>
Consider the function $f:(-\infty, \infty) \rightarrow(-\infty, \infty)$ defined by $f(x)=\frac{x^2-a x+1}{x^2+a x+1} ; 0 < a < 2$<strong>Question:</strong>
Which of the following is true?

**Options:**

- **(A)** $f(x)$ is decreasing on $(-1,1)$ and has a local minimum at $x=1$
- **(B)** $f(x)$ is increasing on $(-1,1)$ and has a local maximum at $x=1$
- **(C)** $f(x)$ is increasing on $(-1,1)$ but has neither a local maximum nor a local minimum at $x=1$
- **(D)** $f(x)$ is decreasing on $(-1,1)$ but has neither a local maximum nor a local minimum at $x=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $f(x)$ is decreasing on $(-1,1)$ and has a local minimum at $x=1$**

**Detailed Solution:**

When $x \in(-1,1)$
$$
x^2 < 1 \Rightarrow x^2-1 < 0
$$
$\therefore \quad f^{\prime}(x) < 0 \Rightarrow f(x)$ is decreasing.
Also, at $x=1, f^{\prime \prime}(1)=\frac{4 a}{(a+2)^2>0}$
$[\because 0 < a < 2]$
$\therefore f(x)$ has a local minimum at $x=1$.

</details>

---

### Q19. JEE Advanced 2008 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the function $g:(-\infty, \infty) \rightarrow\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ be given by $g(u)=2 \tan ^{-1}\left(e^u\right)-\frac{\pi}{2}$. Then, $g$ is

**Options:**

- **(A)** even and is strictly increasing in $(0, \infty)$
- **(B)** odd and is strictly decreasing in $(-\infty, \infty)$
- **(C)** odd and is strictly increasing in $(-\infty, \infty)$
- **(D)** Neither even nor odd, but is strictly increasing in $(-\infty, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) odd and is strictly increasing in $(-\infty, \infty)$**

**Detailed Solution:**

$\therefore \quad g(u)=2 \tan ^{-1}\left(e^u\right)-\frac{\pi}{2}$
for $\quad u \in(-\infty, \infty)$
and
$$
\begin{aligned}
g(-u) & =2 \tan ^{-1}\left(e^{-u}\right)-\frac{\pi}{2} \\
& =2\left(\cot ^{-1}\left(e^u\right)\right)-\frac{\pi}{2} \\
& =2\left(\frac{\pi}{2}-\tan ^{-1}\left(e^u\right)\right)-\frac{\pi}{2} \\
& =\frac{\pi}{2}-2 \tan ^{-1}\left(e^u\right)=-g(u)
\end{aligned}
$$
$\therefore \quad g(-u)=-g(u)$
$\Rightarrow g(u)$ is an odd function.

</details>

---

### Q20. JEE Advanced 2008 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

Let $f(x)$ be a non-constant twice differentiable function defined on $(-\infty, \infty)$, such that $f(x)=f(1-x)$ and $f^{\prime}\left(\frac{1}{4}\right)=0$. Then,

**Options:**

- **(A)** $f^{\prime}(x)$ vanishes atleast twice on $[0,1]$
- **(B)** $f^{\prime}\left(\frac{1}{2}\right)=0$
- **(C)** $\int_{\frac{1}{2}}^{\frac{1}{2}} f\left(x+\frac{1}{2}\right) \sin x d x=0$
- **(D)** $\int_0^{\frac{1}{2}} f(t) e^{\sin \pi t} d t=\int_{\frac{1}{2}}^1 f(1-t) e^{\sin \pi t} d t$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\int_0^{\frac{1}{2}} f(t) e^{\sin \pi t} d t=\int_{\frac{1}{2}}^1 f(1-t) e^{\sin \pi t} d t$**

**Detailed Solution:**

Given that, $f(x)=f(1-x)$
On differentiating w.r.t. $x$, we get
$$
f^{\prime}(x)=-f^{\prime}(1-x)
$$
Let us put $\quad x=\frac{1}{2}$
$$
\Rightarrow \quad 2 f^{\prime}\left(\frac{1}{2}\right)=0 \Rightarrow f^{\prime}\left(\frac{1}{2}\right)=0
$$
Since, $f^{\prime}\left(\frac{1}{2}\right)=0$ and $f^{\prime}\left(\frac{1}{4}\right)=0$
$\Rightarrow f^{\prime \prime}(x)=0$ at two points in $[0,1]$.
Now, $\int_{-1 / 2}^{1 / 2} f\left(x+\frac{1}{2}\right) \sin x d x=0$
As, $f\left(x+\frac{1}{2}\right) \sin x$ is an odd function which is clear from the following explanation.
Let $g(x)=f\left(x+\frac{1}{2}\right) \sin x$,
$$
g(-x)=f\left(\frac{1}{2}-x\right) \sin (-x)=-\sin x f\left(1-\left(\frac{1}{2}-x\right)\right)=-\sin x f\left(\frac{1}{2}+x\right)=-g(x)
$$
Moreover, $\int_{1 / 2}^1 f(1-t) e^{\sin (\pi t)} d t=\int_0^{1 / 2} f(u) \cdot e^{\sin \pi u} d u$ where, $1-t=u$.

</details>

---

### Q21. JEE Advanced 2007 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)=\frac{x^2-6 x+5}{x^2-5 x+6}$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/5LpElX78gcLAqJVL43i4iELoQ4DU2RBjX9Jh8inUrTA.original.fullsize.png">

**Options:**

- **(A)** A-p; B-q; C-q; D-p
- **(B)** A-r; B-s; C-q; D-r
- **(C)** A-s; B-p; C-q; D-p
- **(D)** A-r; B-q; C-p; D-r

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A-p; B-q; C-q; D-p**

**Detailed Solution:**

$$
f(x)=\frac{(x-1)(x-5)}{(x-2)(x-3)}
$$
The graph of $f(x)$ is shown
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/wvp0nANowQRUUqEKwDE04wK9eFTqRImRXTt4B2hjHOM.original.fullsize.png">

(A) If $-1 < x < 1 \Rightarrow 0 < f(x) < 1$
(B) If $1 < x < 2 \Rightarrow f(x) < 0$
(C) If $3 < x < 5 \Rightarrow f(x) < 0$
(D) If $x>5 \Rightarrow 0 < f(x) < 1$

</details>

---

