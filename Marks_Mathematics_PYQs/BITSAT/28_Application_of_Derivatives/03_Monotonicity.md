# BITSAT Mathematics - Application of Derivatives

## Topic 3: Monotonicity

**Total Questions:** 17

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `2`

Consider the function $f(x)=\frac{|x-1|}{x^2}$, then $f(x)$ is

**Options:**

- **(A)** increasing in $(0,1) \cup(2, \infty)$
- **(B)** increasing in $(-\infty, 0) \cup(0,1)$
- **(C)** decreasing in $(-\infty, 0) \cup(2, \infty)$
- **(D)** decreasing in $(0,1) \cup(2, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) decreasing in $(0,1) \cup(2, \infty)$**

**Detailed Solution:**

Given, $f(x)=\left\{\begin{aligned} \frac{x-1}{x^2} ; & x \geq 1 \\ \frac{-x+1}{x^2} ; & x \lt 1\end{aligned}\right.$
$\begin{aligned}
& f(x)= \begin{cases}\frac{1}{x}-\frac{1}{x^2} ; & x \geq 1 \\
-\frac{1}{x}+\frac{1}{x^2} ; & x \lt 1\end{cases} \\
& f^{\prime}(x)= \begin{cases}\frac{-1}{x^2}+\frac{2}{x^3} ; & x \geq 1 \\
\frac{1}{x^2}-\frac{2}{x^3} ; & x \lt 1\end{cases} \\
& f^{\prime}(x)= \begin{cases}\frac{2-x}{x^3} ; & x \geq 1 \\
\frac{x-2}{x^3} ; & x \lt 1\end{cases}
\end{aligned}$
By observation, $f^{\prime}(x)$ will be<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/mZpWNRtakll5g4R_qPQjO8-Xlgu9YWyJyuF1K2KsqOc.original.fullsize.png"/>
Decreasing in $(0,1) \cup(2, \infty)$
and increasing in $(-\infty, 0) \cup(1,2)$

</details>

---

### Q2. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

The point of inflexion for the curve $y=(x-a)^n$, where n is odd integer and $n \geq 3$ is

**Options:**

- **(A)** $(a, 0)$
- **(B)** $(0, a)$
- **(C)** $(0,0)$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(a, 0)$**

**Detailed Solution:**

Here $\frac{d^2 y}{d x^2}=n(n-1)(x-a)^{n-2}$
Now, $\frac{d^2 y}{d x^2}=0 \Rightarrow x=a$
Differentiating equation of the curve $n$ times,
we get, $\frac{d^n y}{d x^n}=n$ !
$\therefore \quad$ at $x=a, \frac{d^n y}{d x^n} \neq 0$ and $\frac{d^{n-1} y}{d x^{n-1}}=0$,
where $n$ is odd.
Therefore $(a, 0)$ is the point of inflexion

</details>

---

### Q3. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

If $f(x)=\cos x, g(x)=\cos 2 x, h(x)=\cos 3 x$ and $I(x)$ $=\tan x$, then which of the following option is correct?

**Options:**

- **(A)** $f(x)$ and $g(x)$ are strictly decreasing in $(0, \pi /$ 2)
- **(B)** $h(x)$ is neither increasing nor decreasing in $(0, \pi / 2)$
- **(C)** $\mathrm{I}(\mathrm{x})$ is strictly increasing in $(0, \pi / 2)$
- **(D)** All are correct

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) All are correct**

**Detailed Solution:**

(a) Let $f(x)=\cos x$, then $f^{\prime}(x)=-\sin x$.
In interval $\left(0, \frac{\pi}{2}\right), f^{\prime}(x) < 0$
Therefore, $f(x)$ is strictly decreasing on $\left(0, \frac{\pi}{2}\right)$
(b) Let $f(x)=\cos 2 x \Rightarrow f^{\prime}(x)=-2 \sin x 2 x$
In interval $\left(0, \frac{\pi}{2}\right), f^{\prime}(x) < 0$
Because $\sin 2 x$ will either lie in the first or second quadrant which will give a positive value.
Therefore, $f(x)$ is strictly decreasing on $\left(0, \frac{\pi}{2}\right)$
(c) Let $f^{\prime}(x)=\cos 3 x$
$\Rightarrow \mathrm{f}^{\prime}(\mathrm{x})=-3 \sin 3 \mathrm{x}$. In Interval $\left(0, \frac{\pi}{3}\right), \mathrm{f}^{\prime}(\mathrm{x}) < 0$
Because $\sin 3 \mathrm{x}$ will either lie in the first or second quadrant which will give a positive value.
Therefore, $\mathrm{f}(\mathrm{x})$ irstrictly decreasing on $\left(0, \frac{\pi}{3}\right)$.
When $\mathrm{x} \in\left(\frac{\pi}{3}, \frac{\pi}{2}\right)$, then $\mathrm{f}^{\prime}(\mathrm{x})>0$
Because $\sin 3 x$ will lie in the third quadrant. Therefore, $f(x)$ is not strictly decreasing on
$\left(0, \frac{\pi}{2}\right)$
(d) Let $f(x)=\tan x \Rightarrow f^{\prime}(x)=\sec ^2 x$.
In Interval $\mathrm{x} \in\left(0, \frac{\pi}{2}\right), \mathrm{f}^{\prime}(\mathrm{x})>0$
Therefore, $f(x)$ is not strictly decreasing on
$\left(0, \frac{\pi}{2}\right)$

</details>

---

### Q4. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

The function $f(x)=\log (1+x)-\frac{2 x}{2+x}$ is increasing on

**Options:**

- **(A)** $(0, \infty)$
- **(B)** $(-\infty, 0)$
- **(C)** $(-\infty, \infty)$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(0, \infty)$**

**Detailed Solution:**

Given $f(x)=\log (1+x)-\frac{2 x}{2+x}$
$\begin{aligned}
& f^{\prime}(x)=\frac{1}{1+x}-\frac{(2+x)(2)-2 x}{(2+x)^2} \\
& =\frac{1}{1+x}-\frac{4}{(2+x)^2} \\
& =\frac{(2+x)^2-4-4 x}{(1+x)(2+x)^2}=\frac{x^2}{(1+x)(2+x)^2}>0 \text { for all } \\
& x \in(0, \infty)
\end{aligned}$
Thus, given function $\mathrm{f}(\mathrm{x})$ is increasing on $(0$, $\infty)$.

</details>

---

### Q5. BITSAT 2023 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

The function $f(x)=\tan ^{-1}(\sin x+\cos x)$ is an increasing function in

**Options:**

- **(A)** $\left(\frac{\pi}{4}, \frac{\pi}{2}\right)$
- **(B)** $\left(-\frac{\pi}{2}, \frac{\pi}{4}\right)$
- **(C)** $\left(0, \frac{\pi}{2}\right)$
- **(D)** $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(-\frac{\pi}{2}, \frac{\pi}{4}\right)$**

**Detailed Solution:**

Since, $f(x)=\tan ^{-1}(\sin x+\cos x)$
$\therefore \mathrm{f}^{\prime}(\mathrm{x})=\frac{1}{1+(\sin \mathrm{x}+\cos \mathrm{x})^2}(\cos \mathrm{x}-\sin \mathrm{x})$
$=\frac{\sqrt{2} \cos \left(x+\frac{\pi}{4}\right)}{1+(\sin x+\cos x)^2}$
$f(x)$ is increasing if $f^{\prime}(x)>0 \Rightarrow \cos \left(x+\frac{\pi}{4}\right)>0$
$\Rightarrow \quad-\frac{\pi}{2} < x+\frac{\pi}{4} < \frac{\pi}{2} \Rightarrow-\frac{3 \pi}{2} < x+\frac{\pi}{4}$

</details>

---

### Q6. BITSAT 2023 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

The interval in which the function $f(x)=$ $\frac{4 x^2+1}{x}$ is decreasing is :

**Options:**

- **(A)** $\left(-\frac{1}{2}, \frac{1}{2}\right)$
- **(B)** $\left[-\frac{1}{2}, \frac{1}{2}\right]$
- **(C)** $(-1,1)$
- **(D)** $[-1,1]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(-\frac{1}{2}, \frac{1}{2}\right)$**

**Detailed Solution:**

Given $f(x)=\frac{4 x^2+1}{x}$ Thus $f^{\prime}(x)=4-\frac{1}{x^2}$
$\mathrm{f}(\mathrm{x})$ will be decreasing if $\mathrm{f}^{\prime}(\mathrm{x}) < 0$
Thus $4-\frac{1}{x^2} < 0 \Rightarrow \frac{1}{x^2}>4 \Rightarrow \frac{-1}{2} < x < \frac{1}{2}$
Thus interval in which $f(x)$ is decreasing, is $\left(-\frac{1}{2}, \frac{1}{2}\right)$.

</details>

---

### Q7. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `2`

$f(x)=\left(\frac{e^{2 x}-1}{e^{2 x}+1}\right)$ is

**Options:**

- **(A)** an increasing function
- **(B)** a decreasing function
- **(C)** an even function
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) an increasing function**

**Detailed Solution:**

$\begin{array}{l}

\because \mathrm{f}(x)=\left(\frac{e^{2 x}-1}{e^{2 x}+1}\right) \\

\therefore \mathrm{f}(-x)=\frac{e^{-2 x}-1}{e^{-2 x}+1}=\frac{1-e^{2 x}}{1+e^{2 x}} \\

\Rightarrow \mathrm{f}(-x)=\frac{-\left(e^{2 x}-1\right)}{e^{2 x}+1}=-\mathrm{f}(x)

\end{array}$

$\therefore \mathrm{f}(x)$ is an odd function.

Again, $\mathrm{f}^{\prime}(x)=\frac{4 e^{2 x}}{\left(1+e^{2 x}\right)^{2}}>0, \forall x \in R$ $\Rightarrow \mathrm{f}(x)$ is an increasing function.

</details>

---

### Q8. BITSAT 2018

*Type:* `singleCorrect` | *Level:* `1`

For which interval the given function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>1</mn></math> is decreasing?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>18</mn><mi>x</mi><mo>-</mo><mn>12</mn></math></p><p>To be decreasing <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>18</mn><mi>x</mi><mo>-</mo><mn>12</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>Therefore, either <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p>Hence, option (d) correct.</p>

</details>

---

### Q9. BITSAT 2017

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi><mo>]</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#960;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#960;</mi></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi></math></p><p>For maximum or minimum value, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>2</mn><mi>n</mi><mi>&#960;</mi><mo>&#177;</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mi>n</mi><mi>&#960;</mi><mo>&#177;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math></p><p>Find <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>,</mo><mi>f</mi><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mn>2</mn><mi>&#960;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mi>f</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>,</mo><mi>f</mi><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>-</mo><mn>0</mn><mo>.</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mn>0</mn><mo>.</mo><mn>8</mn><mo>,</mo><mi>f</mi><mfenced><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>-</mo><mn>0</mn><mo>.</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi>&#960;</mi><mo>+</mo><mn>0</mn><mo>=</mo><mn>2</mn><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>&#960;</mi></math></p>

</details>

---

### Q10. BITSAT 2017

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>21</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>60</mn><mi>x</mi><mo>+</mo><mn>41</mn></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>21</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>60</mn><mi>x</mi><mo>+</mo><mn>41</mn></math></p><p>On differentiating w.r.t. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>42</mn><mi>x</mi><mo>-</mo><mn>60</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>6</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>6</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn></math> i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is decreasing</p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math> i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing</p>

</details>

---

### Q11. BITSAT 2016

*Type:* `singleCorrect` | *Level:* `1`

Consider the following statements in respect of the function $f(x)=x^{3}-1, x \in[-1,1]$

I. $f(x)$ is increasing in [-1,1] 

II. $f(x)$ has no root in (-1,1) . 

Which of the statements given above is/are correct?

**Options:**

- **(A)** Only I
- **(B)** Only II
- **(C)** Both I and II
- **(D)** Neither I nor II

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Only I**

**Detailed Solution:**

Since $f(x)$ is an increasing function in [-1,1] and it has a root in (-1,1) $\therefore \quad$ Only statement $I$ is correct.

</details>

---

### Q12. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `2`

The interval in which the function $2 \mathrm{x}^{3}+15$ increases less rapidly than the function $9 x^{2}-12 x,$ is $-$

**Options:**

- **(A)** $(-\infty, 1)$
- **(B)** (1,2)
- **(C)** $(2, \infty)$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (1,2)**

**Detailed Solution:**

Let $f(x)=2 x^{3}+15$ and $g(x)=9 x^{2}-12 x$ then $\mathrm{f}^{\prime}(\mathrm{x})=6 \mathrm{x}^{2} \forall \mathrm{x} \in \mathrm{R}$

$\therefore \mathrm{f}(\mathrm{x})$ is increasing function $\forall \mathrm{x} \in \mathrm{R}$

$$

\text { Also, } g^{\prime}(x)>0 \Rightarrow 18 x-12>0 \Rightarrow x>\frac{2}{3}

$$

Thus, $\mathrm{f}(\mathrm{x})$ and $\mathrm{g}(\mathrm{x})$ both increases for $\mathrm{x}>\frac{2}{3}$

$$

\text { Let } F(x)=f(x)-g(x), F^{\prime}(x)<0

$$

$(\because \mathrm{f}(\mathrm{x})$ increases less rapidly than the function $\mathrm{g}(\mathrm{x}))$

$$

\Rightarrow 6 \mathrm{x}^{2}-18 \mathrm{x}+12<0 \Rightarrow 1<\mathrm{x}<2

$$

</details>

---

### Q13. BITSAT 2013

*Type:* `singleCorrect` | *Level:* `2`

The function $\mathrm{f}(\mathrm{x})=(\mathrm{x}(\mathrm{x}-2))^{2}$ is increasing in the set

**Options:**

- **(A)** $(-\infty, 0) \cup(2, \infty)$
- **(B)** $(-\infty, 1)$
- **(C)** (0,1)$\cup(2, \infty)$
- **(D)** (1,2)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) (0,1)$\cup(2, \infty)$**

**Detailed Solution:**

$$

\text { } \begin{array}{l}

\text { Here, } \mathrm{f}(\mathrm{x})=(\mathrm{x}(\mathrm{x}-2))^{2} \\

\Rightarrow \mathrm{f}^{\prime}(\mathrm{x})=4 \mathrm{x}(\mathrm{x}-2)(\mathrm{x}-1)

\end{array}

$$

For $\mathrm{f}(\mathrm{x})$ as increasing, $\mathrm{f}^{\prime}(\mathrm{x})>0$

$$

\text { So, } 4 x(x-1)(x-2)>0 \Rightarrow x(x-1)(x-2)>0

$$

<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/lSKQqu4_r-O0TQCuFzGXYtr4R0q6W-FA-qe_tBAQ7TI.original.fullsize.png">


From the above figure required interval is, (0,1)$\cup(2, \infty)$

</details>

---

### Q14. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(\mathrm{x})=\frac{\mathrm{a}^{2}-1}{\mathrm{a}^{2}+1} \mathrm{x}^{3}-3 \mathrm{x}+5$ is a decreasing
function of $\mathrm{x}$ in $\mathbf{R}$, then the set of possible values of a (independent of $\mathrm{x}$ ) is

**Options:**

- **(A)** $(1, \infty)$
- **(B)** $(-\infty,-1)$
- **(C)** [-1,1]
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) [-1,1]**

**Detailed Solution:**

$f^{\prime}(x)=3\left(\frac{a^{2}-1}{a^{2}+1}\right) x^{2}-3$
$\mathrm{f}^{\prime}(\mathrm{x})<0$ for all $\mathrm{x}$ if $\mathrm{a}^{2}-1 \leq 0 \Rightarrow-1 \leq \mathrm{a} \leq 1$

</details>

---

### Q15. BITSAT 2011

*Type:* `singleCorrect` | *Level:* `1`

The function \(f(x)=\sin x-k x-c\), where \(k\) and \(c\) are constants, decreases always when

**Options:**

- **(A)** \(k > 1\)
- **(B)** \(k \geq 1\)
- **(C)** \(k  < 1\)
- **(D)** \(k \leq 1\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) \(k \geq 1\)**

**Detailed Solution:**

Let \(f(x)=\sin x-k x-c\) where \(k\) and \(c\) are constants. \(f^{\prime}(x)=\cos x-k\)
\(\therefore f\) decreases if \(\cos x \leq k\)
Thus, \(f(x)=\sin x-k x-c\) decrease always when \(k \geq 1\).

</details>

---

### Q16. BITSAT 2010

*Type:* `singleCorrect` | *Level:* `2`

If a circular plate is heated uniformly, its area expands \(3 c\) times as fast as its radius, then the value of \(c\) when the radius is 6 units, is

**Options:**

- **(A)** \(4 \pi\)
- **(B)** \(2 \pi\)
- **(C)** \(6 \pi\)
- **(D)** \(3 \pi\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) \(4 \pi\)**

**Detailed Solution:**

Let \(A\) sq. units in the area measure when the radius is \(r\) units.
their \(A=\pi r^2\)
Differentiate both side w.r.t ' \(t\) '
\(\frac{d A}{d t}=2 \pi r \frac{d r}{d t}\) ...(i))
We have, \(\frac{d A}{d t}=3 c \frac{d r}{d t}\)
From eqn (i), we get
\(3 c \cdot \frac{d r}{d t}=2 \pi r \cdot \frac{d r}{d t} \Rightarrow 3 c=2 \pi r\)
Now, \(c=\frac{2}{3} \pi(6)=4 \pi\) when \(r=6\)

</details>

---

### Q17. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of the function \(y=x^4-2 x^2+1\) in the interval \(\left[\frac{1}{2}, 2\right]\) is

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** 8
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

\(\frac{\mathrm{dy}}{\mathrm{dx}}=\frac{\mathrm{d}}{\mathrm{dx}}\left(\mathrm{x}^4-2 \mathrm{x}^2+1\right)=4 \mathrm{x}\left(\mathrm{x}^2-1\right)\)
For \(\max\). or \(\min , \frac{\mathrm{dy}}{\mathrm{dx}}=0\)
\(4 \mathrm{x}\left(\mathrm{x}^2-1\right)=0 ;\), either \(\mathrm{x}=0\) or \(\mathrm{x}= \pm 1\)
\(x=0\) and \(x=-1\) does not belong to \(\left[\frac{1}{2}, 2\right]\)
\(\frac{d^2 y}{d x^2}=12 x^2-4 \therefore\left(\frac{d^2 y}{d x^2}\right)_{x=1}\)
\(=12(1)^2-4=8 > 0\)
\(\therefore \quad\) there is minimum value of function at \(\mathrm{x}=1\)
\(\therefore \quad\) minimum value is
\(y(1)=1^4-2(1)^2+1=1-2+1=0\)

</details>

---

