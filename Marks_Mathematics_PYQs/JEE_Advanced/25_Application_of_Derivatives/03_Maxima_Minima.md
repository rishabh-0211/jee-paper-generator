# JEE Advanced Mathematics - Application of Derivatives

## Topic 3: Maxima Minima

**Total Questions:** 32

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Consider the function $f: (0, \infty) \rightarrow (-\infty, \infty)$ given by

$f(x) = \sqrt{x}\, \log_e(x) - x + 1$.

Then which one of the following statements is TRUE?

**Options:**

- **(A)** The derivative of the function $f$ is decreasing in the interval $(0, 1)$
- **(B)** The function $f$ has a local maximum at some point $a \in (0, \infty)$
- **(C)** The function $f$ has a local minimum at some point $b \in (0, \infty)$
- **(D)** The function $f$ has NEITHER a point of local maximum NOR a point of local minimum in the interval $(0, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The function $f$ has NEITHER a point of local maximum NOR a point of local minimum in the interval $(0, \infty)$**

**Detailed Solution:**

Given $f(x) = \sqrt{x} \log_e(x) - x + 1$

Differentiating with respect to $x$:

$f'(x) = \dfrac{1}{2\sqrt{x}} \log_e(x) + \sqrt{x} \left(\dfrac{1}{x}\right) - 1$

$f'(x) = \dfrac{\log_e(x)}{2\sqrt{x}} + \dfrac{1}{\sqrt{x}} - 1$

Differentiating again with respect to $x$:

$f''(x) = \dfrac{d}{dx} \left( \dfrac{1}{2} x^{-1/2} \log_e(x) + x^{-1/2} - 1 \right)$

$f''(x) = \dfrac{1}{2} \left( -\dfrac{1}{2} x^{-3/2} \log_e(x) + x^{-1/2} \cdot \dfrac{1}{x} \right) - \dfrac{1}{2} x^{-3/2}$

$f''(x) = -\dfrac{\log_e(x)}{4x^{3/2}} + \dfrac{1}{2x^{3/2}} - \dfrac{1}{2x^{3/2}}$

$f''(x) = -\dfrac{\log_e(x)}{4x^{3/2}}$

For $x \in (0, 1)$, $\log_e(x) < 0$, which implies $f''(x) > 0$. Thus, $f'(x)$ is strictly increasing in $(0, 1)$.

For $x \in (1, \infty)$, $\log_e(x) > 0$, which implies $f''(x) < 0$. Thus, $f'(x)$ is strictly decreasing in $(1, \infty)$.

Therefore, $f'(x)$ attains its maximum value at $x = 1$.

Maximum value of $f'(x) = f'(1) = \dfrac{\log_e(1)}{2} + 1 - 1 = 0$.

Since the maximum value of $f'(x)$ is $0$, we have $f'(x) \le 0$ for all $x \in (0, \infty)$, with equality holding only at $x = 1$.

This means $f(x)$ is a strictly decreasing function on $(0, \infty)$.

Hence, $f(x)$ has neither a point of local maximum nor a point of local minimum in the interval $(0, \infty)$.

Answer: The function $f$ has NEITHER a point of local maximum NOR a point of local minimum in the interval $(0, \infty)$

</details>

---

### Q2. JEE Advanced 2025 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathbb{R}$ denote the set of all real numbers. For a real number $x$, let $[x]$ denote the greatest integer less than or equal to $x$. Let $n$ denote a natural number.
Match each entry in List-I to the correct entry in List-II and choose the correct option.
 <table> <thead> <tr> <th> </th> <th>LIST - I </th> <th> </th> <th>LIST - II </th> </tr> </thead> <tbody> <tr> <td>(P) </td> <td>The minimum value of $n$ for which the function $f(x)=\left[\frac{10 x^3-45 x^2+60 x+35}{n}\right]$ is continuous on the interval $[1,2]$,is </td> <td>(1) </td> <td>8 </td> </tr> <tr> <td>(Q) </td> <td>The minimum value of $n$ for which $g(x)=\left(2 n^2-13 n-15\right)\left(x^3+3 x\right),x \in \mathbb{R}$,is an increasing function on $\mathbb{R}$,is </td> <td>(2) </td> <td>9 </td> </tr> <tr> <td>(R) </td> <td>The smallest natural number $n$ which is greater than 5,such that $x=3$ is a point of local minima of $h(x)=\left(x^2-9\right)^{\mathrm{n}}\left(x^2+2 x+3\right)$,is </td> <td>(3) </td> <td>5 </td> </tr> <tr> <td>(S) </td> <td>Number of $x_0 \in \mathbb{R}$ such that $l(x)=\sum_{k=0}^4\left(\sin |x-k|+\cos \left|x-k+\frac{1}{2}\right|\right),x \in \mathbb{R}$,is NOT differentiable at $x_0$,is </td> <td>(4) </td> <td>6 </td> </tr> <tr> <td> </td> <td> </td> <td>(5) </td> <td>10 </td> </tr> </tbody> </table>

**Options:**

- **(A)** $(\mathrm{P}) \rightarrow(1),(\mathrm{Q}) \rightarrow(3),(\mathrm{R}) \rightarrow(2),(\mathrm{S}) \rightarrow(5)$
- **(B)** $(\mathrm{P}) \rightarrow(2),(\mathrm{Q}) \rightarrow(1),(\mathrm{R}) \rightarrow(4),(\mathrm{S}) \rightarrow(3)$
- **(C)** $(\mathrm{P}) \rightarrow(5),(\mathrm{Q}) \rightarrow(1),(\mathrm{R}) \rightarrow(4),(\mathrm{S}) \rightarrow(3)$
- **(D)** $(\mathrm{P}) \rightarrow(2),(\mathrm{Q}) \rightarrow(3),(\mathrm{R}) \rightarrow(1),(\mathrm{S}) \rightarrow(5)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\mathrm{P}) \rightarrow(2),(\mathrm{Q}) \rightarrow(1),(\mathrm{R}) \rightarrow(4),(\mathrm{S}) \rightarrow(3)$**

**Detailed Solution:**

$\begin{aligned}
& P(x)=10 x^3-45 x^2+60 x+35 \\
& P^{\prime}(x)=30(x-1)(x-2)
\end{aligned}$
$\mathrm{P}(\mathrm{x})$ decreases in $[1,2]$
$\Rightarrow$ Range of $\mathrm{P}(\mathrm{x})=[55,60]$
$f(\mathrm{x})=\left[\frac{\mathrm{P}(\mathrm{x})}{\mathrm{n}}\right] \min$ value of $\mathrm{n}=9$
(Q) For $g(x)$ to be increasing
$2 n^2-13 n-15 \geq 0$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/wjoLAvOi7QC218GUOpA_8ZUcNAvD3rBZeiYnL049_Qg.original.fullsize.png">
(R) $\begin{aligned} & h(x)=\left(x^2-9\right)^n\left(x^2+2 x+3\right) \\ & h^{\prime}(x)=\left(x^2-9\right)^n(2 x+2)+\left(x^2+2 x+3\right) n\left(x^2-9\right)^{n-1} \cdot 2 x \\ & =\left(x^2-9\right)^{n-1}\left[2\left(x^2-9\right)(x+1)+2 n x\left(x^2+2 x+3\right)\right] \\ & =(x+3)^{n-1}(x-3)^{n-1} \cdot q(x)\end{aligned}$
Derivative must change sign at $x=3$
$\begin{aligned}
& \because \mathrm{n}-1=\text { odd } \\
& \mathrm{n}=\text { even } \\
& \mathrm{n}=6
\end{aligned}$
(S) $\cos \left|\mathrm{x}-\mathrm{k}+\frac{1}{2}\right|$ is differentiable everywhere 
$\Rightarrow \sin |\mathrm{x}-\mathrm{k}|$ is NOT diff. at $\mathrm{k}=0,1,2,3,4$

</details>

---

### Q3. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let $f_{1}:(0, \infty) \rightarrow \mathbb{R}$ and $f_{2}:(0, \infty) \rightarrow \mathbb{R}$ be defined by

$$

f_{1}(x)=\int_{0}^{x} \prod_{j=1}^{21}(t-j)^{j} d t, \quad x > 0

$

and

$$

f_{2}(x)=98(x-1)^{50}-600(x-1)^{49}+2450, \quad x > 0

$

where, for any positive integer $n$ and real numbers $a_{1}, a_{2}, \ldots, a_{n}, \prod_{i=1}^{n} a_{i}$ denotes the product of $a_{1}, a_{2}, \ldots, a_{n} .$ Let $m_{i}$ and $n_{i}$, respectively, denote the number of points of local minima and the number of points of local maxima of function $f_{i}, i=1,2$, in the interval $(0, \infty)$.

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msub><mi>m</mi><mn>2</mn></msub><mo>+</mo><mn>4</mn><msub><mi>n</mi><mn>2</mn></msub><mo>+</mo><mn>8</mn><msub><mi>m</mi><mn>2</mn></msub><msub><mi>n</mi><mn>2</mn></msub></math> is ____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>98</mn><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>50</mn></msup><mo>-</mo><mn>600</mn><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>49</mn></msup><mo>+</mo><mn>2450</mn><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>f</mi><mn>2</mn><mo>&#39;</mo></msubsup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>98</mn><mo>&#215;</mo><mn>50</mn><msup><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mn>49</mn></msup><mo>&#8722;</mo><mn>600</mn><mo>&#215;</mo><mn>49</mn><msup><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mn>48</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4900</mn><msup><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mn>48</mn></msup><mfenced><mrow><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mo>&#8722;</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4900</mn><msup><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mn>48</mn></msup><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>7</mn></mrow></mfenced></math></p><p>So extrema is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>7</mn></math> only, which is minima</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msub><mi>m</mi><mn>2</mn></msub><mo>+</mo><mn>4</mn><msub><mi>n</mi><mn>2</mn></msub><mo>+</mo><mn>8</mn><msub><mi>m</mi><mn>2</mn></msub><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q4. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let $f_{1}:(0, \infty) \rightarrow \mathbb{R}$ and $f_{2}:(0, \infty) \rightarrow \mathbb{R}$ be defined by

$$

f_{1}(x)=\int_{0}^{x} \prod_{j=1}^{21}(t-j)^{j} d t, \quad x>0

$$

and

$

f_{2}(x)=98(x-1)^{50}-600(x-1)^{49}+2450, \quad x>0

$

where, for any positive integer $n$ and real numbers $a_{1}, a_{2}, \ldots, a_{n}, \prod_{i=1}^{n} a_{i}$ denotes the product of $a_{1}, a_{2}, \ldots, a_{n} .$ Let $m_{i}$ and $n_{i}$, respectively, denote the number of points of local minima and the number of points of local maxima of function $f_{i}, i=1,2$, in the interval $(0, \infty)$.

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>m</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>m</mi><mn>1</mn></msub><msub><mi>n</mi><mn>1</mn></msub></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **57**

**Detailed Solution:**

<p>Given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mi>x</mi></munderover><mfenced><mrow><mi>t</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><msup><mfenced><mrow><mi>t</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mn>......</mn><msup><mfenced><mrow><mi>t</mi><mo>&#8722;</mo><mn>2</mn><mi>t</mi></mrow></mfenced><mn>21</mn></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msub><msup><mi>f</mi><mo>&#39;</mo></msup><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><msup><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mn>.....</mn><msup><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>21</mn></mrow></mfenced><mn>21</mn></msup></math></p><p>Checking critical points</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/96d8ba46-cf0d-4b82-ad3b-c1cd70463a9a-image.png" style="width: 400px; height: 81px;" /></p><p>At all odd integers from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> will have an extrema with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>13</mn><mo>,</mo><mn>17</mn><mo>,</mo><mn>21</mn></math> being points of minima &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>,</mo><mn>15</mn><mo>,</mo><mn>19</mn></math> being points of maxima.</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mn>1</mn></msub><mo>=</mo><mn>6</mn></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>5</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>m</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>m</mi><mn>1</mn></msub><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>57</mn></math></p>

</details>

---

### Q5. JEE Advanced 2021 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>6</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfrac></math></p><p>Then which of the following statements is(are) TRUE?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is decreasing in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is increasing in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is onto
- **(D)** Range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is increasing in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>6</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>20</mn><mi>x</mi></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mi>x</mi><mo>(</mo><mi>x</mi><mo>+</mo><mn>4</mn><mo>)</mo></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/0de6bb8c-70ea-48e9-a43f-3b29dca08fa0-image.png" style="width: 140px; height: 58px;" /></p><p>Hence, it is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>4</mn><mo>]</mo><mo>&#8746;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math></p><p> </p><p>Now as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mo>-</mo><mo>&#8734;</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo></math>also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/5db986cf-14a3-460c-b7d6-d0a97afbd93f-image.png" style="width: 318px; height: 250px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>16</mn><mo>+</mo><mn>12</mn><mo>-</mo><mn>6</mn></mrow><mrow><mn>16</mn><mo>-</mo><mn>8</mn><mo>+</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mn>22</mn><mn>12</mn></mfrac><mo>=</mo><mfrac><mn>11</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p><p>Hence, range is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>11</mn><mn>6</mn></mfrac></mrow></mfenced></math>, and the function is into.</p>

</details>

---

### Q6. JEE Advanced 2020 (Paper 2)

*Type:* `numerical` | *Level:* `1`

<p>Let the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mn>4</mn></msup></math>. Suppose the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> has a local minimum at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> precisely when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mi>&#960;</mi><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>&#955;</mi><mi>r</mi></msub><mi>&#960;</mi></mrow></mfenced><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mn>1</mn></msub><mo>&#60;</mo><mo>&#8943;</mo><mo>&#60;</mo><msub><mi>&#955;</mi><mi>r</mi></msub><mo>&#60;</mo><mn>1</mn><mo>.</mo></math> Then the value of  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><mo>&#8943;</mo><mo>+</mo><msub><mi>&#955;</mi><mi>r</mi></msub></math> is_______</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.5**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>-</mo><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mfrac><mn>7</mn><mn>4</mn></mfrac></math></p><p>It has minima when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mi>sin</mi><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac><mo>,</mo><mo>&#160;</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>sum</mo><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>.</p>

</details>

---

### Q7. JEE Advanced 2020 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider all rectangles lying in the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><mo>&#215;</mo><mi>R</mi><mo>:</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mtext>&#8201;</mtext><mi>a</mi><mi>n</mi><mi>d</mi><mtext>&#8201;</mtext><mn>0</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mn>2</mn><mi>sin</mi><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfenced></math> and having one side on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis. The area of the rectangle which has the maximum perimeter among all such rectangles, is

**Options:**

- **(A)** <math> <mrow>  <mfrac>   <mrow>    <mn>3</mn><mi>&#960;</mi></mrow>   <mn>2</mn>  </mfrac>  </mrow></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#960;</mi></math>
- **(C)** <math> <mrow> <mfrac> <mi>&#960;</mi> <mrow> <mn>2</mn><msqrt> <mn>3</mn> </msqrt> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow>  <mfrac>   <mrow>    <mi>&#960;</mi><msqrt>     <mn>3</mn>    </msqrt>    </mrow>   <mn>2</mn>  </mfrac>  </mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math> <mrow> <mfrac> <mi>&#960;</mi> <mrow> <mn>2</mn><msqrt> <mn>3</mn> </msqrt> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/bc70f854-3c94-45b0-b70d-0a0b6930ee83-image.png"/>

<math> <mrow> <mn>2</mn><mi>sin</mi><mn>2</mn><msub> <mi>θ</mi> <mn>1</mn> </msub> <mo>=</mo><mn>2</mn><mi>sin</mi><mn>2</mn><msub> <mi>θ</mi> <mn>2</mn> </msub> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msub><mi>θ</mi><mn>1</mn></msub><mo>=</mo><mi>π</mi><mo>−</mo><mn>2</mn><msub><mi>θ</mi><mn>2</mn></msub></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>θ</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>−</mo><msub><mi>θ</mi><mn>1</mn></msub><mtext> </mtext><mo>…</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math>
Now perimeter <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mfenced><mrow><msub><mi>θ</mi><mn>1</mn></msub><mo>,</mo><mo> </mo><msub><mi>θ</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced close="}" open="{"><mrow><mfenced><mrow><msub><mi>θ</mi><mn>2</mn></msub><mo>−</mo><msub><mi>θ</mi><mn>1</mn></msub></mrow></mfenced><mo>+</mo><mn>2</mn><mi>sin</mi><mn>2</mn><msub><mi>θ</mi><mn>1</mn></msub></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>p</mi><mfenced><msub><mi>θ</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>−</mo><mn>2</mn><msub><mi>θ</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><mi>sin</mi><mn>2</mn><msub><mi>θ</mi><mn>1</mn></msub></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>p</mi><mo>'</mo></msup><mfenced><msub><mi>θ</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mo>−</mo><mn>2</mn><mo>+</mo><mn>4</mn><mi>cos</mi><mn>2</mn><msub><mi>θ</mi><mn>1</mn></msub></mrow></mfenced></math>

Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mo>"</mo></msup><mfenced><msub><mi>θ</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mo>−</mo><mn>8</mn><mi>sin</mi><mn>2</mn><msub><mi>θ</mi><mn>1</mn></msub></mrow></mfenced><mo><</mo><mn>0</mn></math>

For maximum perimeter,

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mo>'</mo></msup><mfenced><msub><mi>θ</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>0</mn><mo>&</mo><mo> </mo><msup><mi>p</mi><mo>"</mo></msup><mfenced><msub><mi>θ</mi><mn>1</mn></msub></mfenced><mo><</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mn>2</mn><msub><mi>θ</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>⇒</mo><mn>2</mn><msub><mi>θ</mi><mn>1</mn></msub><mo>=</mo><mfrac><mi>π</mi><mn>3</mn></mfrac><mo>⇒</mo><msub><mi>θ</mi><mn>1</mn></msub><mo>=</mo><mfrac><mi>π</mi><mn>6</mn></mfrac></math>

Now area at <math> <mrow> <msub> <mi>θ</mi> <mn>1</mn> </msub> <mo>=</mo><mfrac> <mi>π</mi> <mn>6</mn> </mfrac> </mrow> </math> will be 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>θ</mi><mn>2</mn></msub><mo>−</mo><msub><mi>θ</mi><mn>1</mn></msub></mrow></mfenced><mo>×</mo><mn>2</mn><mi>sin</mi><mn>2</mn><msub><mi>θ</mi><mn>1</mn></msub></math>

<math> <mrow> <mo>=</mo><mfenced> <mrow> <mfrac> <mi>π</mi> <mn>2</mn> </mfrac> <mo>−</mo><mn>2</mn><msub> <mi>θ</mi> <mn>1</mn> </msub> </mrow> </mfenced><mo>⋅</mo><mn>2</mn><mi>sin</mi><mn>2</mn><msub> <mi>θ</mi> <mn>1</mn> </msub> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>−</mo><mfrac><mi>π</mi><mn>3</mn></mfrac></mrow></mfenced><mo>×</mo><mn>2</mn><mi>sin</mi><mfrac><mi>π</mi><mn>3</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>π</mi><mn>6</mn></mfrac><mo>⋅</mo><msqrt><mn>3</mn></msqrt><mo>=</mo><mfrac><mi>π</mi><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>

</details>

---

### Q8. JEE Advanced 2019 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be given by <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>.</mo></math> Define <math><mi>F</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>.</mo></mrow></mrow></math> Then which of the following options is/are correct?

**Options:**

- **(A)** <math><mi>F</mi></math> has a local minimum at <math><mi>x</mi><mo>=</mo><mn>1</mn></math>
- **(B)** <math><mi>F</mi></math> has a local maximum at <math><mi>x</mi><mo>=</mo><mn>2</mn></math>
- **(C)** <math><mi>F</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>≠</mo><mn>0</mn></math> for all <math><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mn>5</mn></mrow></mfenced></math>
- **(D)** <math><mi>F</mi></math> has two local maxima and one local minimum in <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mi>∞</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>F</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>≠</mo><mn>0</mn></math> for all <math><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mn>5</mn></mrow></mfenced></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mi>x</mi></munderover><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mo>.</mo><mi>d</mi><mi>t</mi></math>
<math><msup><mrow><mi>F</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/7ee4711f-f024-4fd5-9bd0-8574b04c363c-image2.png"/>
<math><mo>⇒</mo><mi>F</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> has maxima at <math><mi>x</mi><mo>=</mo><mn>2</mn></math>
and minima at <math><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math><mi>x</mi><mo>=</mo><mn>5</mn></math>
now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced separators="|"><mn>2</mn></mfenced><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mn>2</mn></munderover><mfenced separators="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>17</mn><mi>x</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mo>.</mo><mi>d</mi><mi>x</mi></math>
<math><mo>=</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>8</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>17</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>10</mn><mi>x</mi></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mn>2</mn></mrow></msubsup></math>
<math><mi>F</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math> which is a maxima in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mn>5</mn></mrow></mfenced></math>
<math><mi>F</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/98bf389d-7b99-411d-bc48-e31281a3378b-image3.png"/>
Hence <math><mi>F</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo><</mo><mn>0</mn><mo>∀</mo><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mn>5</mn></mrow></mfenced></math>

</details>

---

### Q9. JEE Advanced 2019 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

Let <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#960;</mi><mi>x</mi></mrow></mrow></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>.</mo></math>
Let <math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>&#60;</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&#60;</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#60;</mo><mo>&#8230;</mo><mo>&#60;</mo><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>&#60;</mo><mo>&#8230;</mo></math> be all the points of local maximum of <math><mi>f</mi></math> and <math><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>&#60;</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&#60;</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#60;</mo><mo>&#8230;</mo><mo>&#60;</mo><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>&#60;</mo><mo>&#8230;</mo></math> be all the points of local minimum of <math><mi>f</mi><mo>.</mo></math>
Then which of the following options is/are correct?

**Options:**

- **(A)** <math><mfenced open="|" close="|" separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>-</mo><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi></mrow></msub></mrow></mfenced><mo>&gt;</mo><mn>1</mn></math> for every <math><mi>n</mi></math>
- **(B)** <math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>&lt;</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></math>
- **(C)** <math><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>∈</mo><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>,</mo><mi> </mi><mn>2</mn><mi>n</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> for every <math><mi>n</mi></math>
- **(D)** <math><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>&gt;</mo><mn>2</mn></math> for every <math><mi>n</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>&gt;</mo><mn>2</mn></math> for every <math><mi>n</mi></math>**

**Detailed Solution:**

<math><mi>f</mi><mi>'</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>π</mi></mrow></mrow><mi>x</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>π</mi></mrow></mrow><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac></math> …(i)
<math><mo>⇒</mo></math> for maxima/minima <math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><mtable><mtr><mtd><mo>⇒</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>π</mi><mi>x</mi><mo>=</mo><mn>0</mn></mrow></mrow></mtd><mtd><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi><mfrac><mrow><mi>π</mi><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>π</mi><mi>x</mi></mrow></mrow></mtd></mtr></mtable></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mo>∵</mo><mi>cos</mi><mo>⁡</mo><mi>π</mi><mi>x</mi><mo>≠</mo><mn>0</mn></mtd><mtd></mtd><mtd><mfenced close="}" open="{" separators="|"><mrow><mo>∵</mo><mi>tan</mi><mo>⁡</mo><mi>π</mi><mi>x</mi><mi> </mi><mi>will</mi><mi mathvariant="normal"> </mi><mi>not</mi><mi mathvariant="normal"> </mi><mi>be</mi><mi mathvariant="normal"> </mi><mi>defined</mi></mrow></mfenced></mtd></mtr></mtable></math>
<math><mo>∴</mo><mi> </mi></math> maxima/minima will occur
Where <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>π</mi><mi>x</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/9c45441c-1882-44d6-b338-482d514c074e-image1.png"/>
Case <math><mi mathvariant="normal">I</mi><mo>:</mo></math>
<math><mfenced separators="|"><mrow><mi mathvariant="normal">i</mi></mrow></mfenced></math> For example
In <math><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>,</mo><mi> </mi><mn>2</mn><mi>n</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> at point <math><msub><mrow><mi>P</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi> </mi><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
<math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><mi>x</mi></mrow></mfenced><mo>></mo><mn>0</mn></mrow></mrow></math>
and at <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>P</mi><mn>2</mn><mo>+</mo></msubsup><mo>,</mo><mo> </mo><mi>tan</mi><mo>⁡</mo><mfenced separators="|"><mrow><mi>π</mi><mi>x</mi></mrow></mfenced><mo>></mo><mfrac><mrow><mi>π</mi><mi>x</mi></mrow><mn>2</mn></mfrac></math>
at <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>P</mi><mn>2</mn><mo>-</mo></msubsup><mo>,</mo><mo> </mo><mi>tan</mi><mo>⁡</mo><mfenced separators="|"><mrow><mi>π</mi><mi>x</mi></mrow></mfenced><mo><</mo><mfrac><mrow><mi>π</mi><mi>x</mi></mrow><mn>2</mn></mfrac></math>
hence from equation (i)
in <math><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>,</mo><mi> </mi><mn>2</mn><mi>n</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>,</mo><mi> </mi><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> goes from positive to negative
hence <math><msub><mrow><mi>P</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is maxima
Similarly <math><msub><mrow><mi>P</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi> </mi><msub><mrow><mi>P</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>,</mo><mi> </mi><msub><mrow><mi>P</mi></mrow><mrow><mn>6</mn></mrow></msub></math> … are point of maxima and all lies in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>,</mo><mi> </mi><mn>2</mn><mi>n</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
Case <math><mi mathvariant="normal">I</mi><mi mathvariant="normal">I</mi></math>
In <math><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>2</mn><mi>n</mi><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
<math><mfenced separators="|"><mrow><mi mathvariant="normal">i</mi><mi mathvariant="normal">i</mi></mrow></mfenced></math> for example at <math><msub><mrow><mi>P</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi> </mi><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
<math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><mi>x</mi></mrow></mfenced><mo><</mo><mn>0</mn></mrow></mrow></math>
at <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>P</mi><mn>1</mn><mo>+</mo></msubsup><mo>,</mo><mo> </mo><mi>tan</mi><mo>⁡</mo><mfenced separators="|"><mrow><mi>π</mi><mi>x</mi></mrow></mfenced><mo>></mo><mfrac><mrow><mi>π</mi><mi>x</mi></mrow><mn>2</mn></mfrac></math>
and at <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>P</mi><mn>1</mn><mo>-</mo></msubsup><mo>,</mo><mo> </mo><mi>tan</mi><mo>⁡</mo><mfenced separators="|"><mrow><mi>π</mi><mi>x</mi></mrow></mfenced><mo><</mo><mfrac><mrow><mi>π</mi><mi>x</mi></mrow><mn>2</mn></mfrac></math>
hence from equation (i)
in <math><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>2</mn><mi>n</mi><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>,</mo><mi> </mi><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> goes from negative to positive
<math><mo>⇒</mo></math> so, for the minima <math><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>:</mo><mn>1</mn><mo><</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo><</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>:</mo><mn>3</mn><mo><</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub><mo><</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><msub><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>:</mo><mn>5</mn><mo><</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msub><mo><</mo><mfrac><mrow><mn>11</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
and for the maxima <math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>:</mo><mn>2</mn><mo><</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo><</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>:</mo><mn>4</mn><mo><</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo><</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><msub><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>:</mo><mn>6</mn><mo><</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msub><mo><</mo><mfrac><mrow><mn>13</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
Hence <math><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>></mo><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi></mrow></msub></math> … <math><mfenced separators="|"><mrow><mi mathvariant="normal">a</mi></mrow></mfenced></math>
<math><mo>⇒</mo><mi> </mi></math> now,
<math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>></mo><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></math>
<math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced><mo>></mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></mrow></mrow></mrow></mrow></math>
<math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced><mo>></mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><mo>+</mo><mi>π</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></mrow></mrow></mrow></mrow></math>
<math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced><mo>></mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></mrow></mfenced></mrow></mrow></mrow></mrow></math>
<math><mi>π</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>></mo><mi>π</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></math>
<math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>></mo><mn>1</mn><mo>+</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></math>
Similarly, <math><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>></mo><mn>1</mn><mo>+</mo><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi></mrow></msub></math>
<math><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>-</mo><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>></mo><mn>1</mn></math> …(b)
<math><mfenced close="|" open="|" separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>-</mo><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi></mrow></msub></mrow></mfenced><mo>></mo><mn>1</mn></math>
<math><mo>⇒</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>></mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub></math>
<math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced><mo>></mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></mrow></mrow></mrow></mrow></math>
<math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced><mo>></mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>π</mi><mo>+</mo><mi>π</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced><mo>⇒</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>></mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>1</mn></mrow></mrow></mrow></mrow></math>
<math><mo>⇒</mo><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>></mo><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>+</mo><mn>1</mn></math>
Therefore <math><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo><</mo><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo><</mo><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>⇒</mo><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>></mo><mn>1</mn></math> …(c)
Now consider <math><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>=</mo><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub></mrow></mfenced></math>
From (b) and (c)
<math><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>></mo><mn>2</mn></math>

</details>

---

### Q10. JEE Advanced 2019 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be given by <math> <mrow> <mi>f</mi><mfenced> <mi>x</mi> </mfenced></mrow> </math> <math><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>+</mo><mn>5</mn><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>10</mn><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>10</mn><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>3</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo>&#60;</mo><mn>0</mn><mo>;</mo></mtd></mtr><mtr><mtd><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi mathvariant="normal">x</mi><mo>&#60;</mo><mn>1</mn><mo>;</mo></mtd></mtr><mtr><mtd><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>4</mn><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>7</mn><mi mathvariant="normal">x</mi><mo>-</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo></mtd><mtd><mn>1</mn><mo>&#8804;</mo><mi mathvariant="normal">x</mi><mo>&#60;</mo><mn>3</mn><mo>;</mo></mtd></mtr><mtr><mtd><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo>&#8805;</mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>
Then which of the following options is/are correct?

**Options:**

- **(A)** <math><mi mathvariant="normal">f</mi><mi mathvariant="normal">&prime;</mi></math>  is NOT differentiable at  <math><mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn></math>
- **(B)** <math><mi mathvariant="normal">f</mi></math> is increasing on <math><mfenced separators="|"><mrow><mo>-</mo><mi mathvariant="normal">∞</mi><mo>,</mo><mtext> </mtext><mn>0</mn></mrow></mfenced></math>
- **(C)** <math><mi mathvariant="normal">f</mi></math> is onto
- **(D)** <math><mi mathvariant="normal">f</mi><mi mathvariant="normal">′</mi></math> has a local maximum at <math><mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi mathvariant="normal">f</mi><mi mathvariant="normal">′</mi></math> has a local maximum at <math><mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>As given <math><mi mathvariant="normal">f</mi><mo>:</mo><mi mathvariant="normal">R</mi><mo>→</mo><mi mathvariant="normal">R</mi></math>
<math> <mrow> <mi>f</mi><mfenced> <mi>x</mi> </mfenced></mrow> </math><math><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>+</mo><mn>5</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>10</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>10</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>x</mi><mo><</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>0</mn><mo>≤</mo><mi>x</mi><mo><</mo><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>7</mn><mi>x</mi><mo>-</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mtd><mtd><mn>1</mn><mo>≤</mo><mi>x</mi><mo><</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>-</mo><mi>x</mi><mo>+</mo><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mtd><mtd><mi>x</mi><mo>≥</mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math><mi> </mi><mi>f</mi><mo>(</mo><msup><mrow><mn>0</mn></mrow><mrow></mrow></msup><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>1</mn></math>
<math><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><msup><mrow><mn>1</mn></mrow><mrow></mrow></msup></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><msup><mrow><mn>1</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>
<math><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><msup><mrow><mn>3</mn></mrow><mrow></mrow></msup></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><msup><mrow><mn>3</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
Hence <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is continuous everywhere.
Now, <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>∞</mi></math> and <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mo>+</mo><mi>∞</mi></math>
Hence, range of <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is <math><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mi>∞</mi></mrow></mfenced></math>
Consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>'</mo><mfenced><mi>x</mi></mfenced></math> <math><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mn>5</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>20</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>30</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>20</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>5</mn><msup><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mn>2</mn></mtd><mtd><mi>x</mi><mo><</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn><mo><</mo><mi>x</mi><mo><</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>7</mn></mtd><mtd><mn>1</mn><mo><</mo><mi>x</mi><mo><</mo><mn>3</mn></mtd></mtr><mtr><mtd><mi>l</mi><mi>n</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo></mtd><mtd><mi>x</mi><mo>></mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>
Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>B</mi><mo>)</mo><mo>:</mo></math>
For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo><</mo><mn>0</mn><mi> </mi><msup><mi>f</mi><mi>′</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>5</mn><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup><mi> </mi><mo>-</mo><mn>2</mn><mo>,</mo></math> which takes both positive and negative values.
Hence, <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is non-monotonic for <math><mi>x</mi><mo><</mo><mn>0</mn></math>
Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>A</mi><mo>)</mo><mo>:</mo></math>
<math> <mrow> <msup> <mi>f</mi> <mo>″</mo> </msup> <mfenced> <mi>x</mi> </mfenced></mrow> </math> <math><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mn>20</mn><msup><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mn>3</mn></mrow></msup></mtd><mtd><mi>x</mi><mo><</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn><mo><</mo><mi>x</mi><mo><</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn></mtd><mtd><mn>1</mn><mo><</mo><mi>x</mi><mo><</mo><mn>3</mn></mtd></mtr><mtr><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></mtd><mtd><mi>x</mi><mo>></mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>
Now, <math><mi>f</mi><mi>”</mi><mfenced separators="|"><mrow><msup><mrow><mn>1</mn></mrow><mrow><mi>′</mi></mrow></msup></mrow></mfenced><mo>=</mo><mi> </mi><mn>4</mn><mo><</mo><mn>0</mn></math> and <math><mi>f</mi><mi>”</mi><mfenced separators="|"><mrow><msup><mrow><mn>1</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></mfenced><mo>=</mo><mn>2</mn><mo>></mo><mn>0</mn></math>
Given of <math><mi>f</mi><mi>′</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> in <math><mi>x</mi><mo>∈</mo><mfenced separators="|"><mrow><mn>0,3</mn></mrow></mfenced></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ztefblhrtscbegodiotqbwcrmzzsaxequgujmexuteasspllul.png"/>
<math><mi>x</mi><mo>=</mo><mn>1</mn></math> is maxima for <math><msup><mrow><mi>f</mi></mrow><mrow><mi>′</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> -----Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>D</mi></mfenced></math>
and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>′</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is not differential at <math><mi>x</mi><mo>=</mo><mn>1</mn></math>
Option <math><mo>(</mo><mi mathvariant="normal">C</mi><mo>)</mo><mo>:</mo></math>
<math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mrow><mo>-</mo><mi>x</mi><mo>+</mo><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>∞</mi></mrow></munder><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mi>∞</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mo>-</mo><mi>∞</mi></mrow></munder><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mi>∞</mi></math>
Hence, range of f  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∈</mo><mfenced separators="|"><mrow><mi> </mi><mo>-</mo><mi>∞</mi><mo>,</mo><mi> </mi><mi>∞</mi></mrow></mfenced></math></p>

</details>

---

### Q11. JEE Advanced 2017 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow></mtd><mtd><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow></mtd><mtd><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow></mtd></mtr><mtr><mtd><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mtd><mtd><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mtd><mtd><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mtd></mtr><mtr><mtd><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mtd><mtd><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mtd><mtd><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mtd></mtr></mtable></mrow></mfenced><mo>,</mo></math> then

**Options:**

- **(A)** <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">x</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">y</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">p</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi> </mi><mo>(</mo><mo>-</mo><mi>π</mi><mo>,</mo><mi>π</mi><mo>)</mo></math>
- **(B)** <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> attains its maxima at <math><mi>x</mi><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>  attains its minima at  <math><mi>x</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math><msup><mrow><mi>f</mi></mrow><mrow><mi>′</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">p</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi> </mi><mo>(</mo><mo>-</mo><mi>π</mi><mo>,</mo><mi>π</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msup><mrow><mi>f</mi></mrow><mrow><mi>′</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">p</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi> </mi><mo>(</mo><mo>-</mo><mi>π</mi><mo>,</mo><mi>π</mi><mo>)</mo></math>**

**Detailed Solution:**

<p>Expansion of determinant</p><p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><mrow><mi mathvariant="normal">cos </mi></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos </mi></mrow><mo>⁡</mo><mrow><mn>4</mn><mi>x</mi></mrow></mrow></math></p><p><math><mrow><msup><mi>f</mi><mo>'</mo></msup><mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mo>=</mo><mi> </mi><mo>−</mo><mn>2</mn><mi>sin</mi><mi> </mi><mn>2</mn><mi>x</mi><mo>−</mo><mn>4</mn><mtext>sin </mtext><mn>4</mn><mi>x</mi><mo>=</mo><mo>−</mo><mn>2</mn><mtext>sin </mtext><mn>2</mn><mi>x</mi><mrow><mo>(</mo><mrow><mn>1</mn><mo>+</mo><mn>4</mn><mi>cos</mi><mi> </mi><mn>2</mn><mi>x</mi></mrow><mo>)</mo></mrow></mrow></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/46_solu_chem_pa_2.jpg"/></p><p><math><mo>∴</mo></math>    maxima at <math><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mi> </mi><mi> </mi><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><math> <mrow> <mtext>sin</mtext> <mn>2</mn> <mi>x</mi> <mo>=</mo> <mn>0</mn> <mo>∴</mo> <mi>x</mi> <mo>=</mo> <mn>0</mn> <mtext>,</mtext> <mfrac> <mrow> <mi>π</mi> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mtext>,</mtext> <mo>-</mo> <mfrac> <mrow> <mi>π</mi> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math> </math>
and <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow><mo>=</mo><mi> </mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math> has 4 solutions in <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mi>π</mi> <mtext>,</mtext> <mspace width="0.5em"></mspace> <mi>π</mi> </mrow> </mfenced> </mrow> </math></p><math> <mrow> <mo>∴</mo> <msup> <mtext>f</mtext> <mo> ′</mo> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mi>x</mi> </mrow> </mfenced> <mo>=</mo> <mn>0</mn> </mrow> </math> has more than three solutions

</details>

---

### Q12. JEE Advanced 2016 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

The least value of <math><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi></math> for which, <math><mn>4</mn><mi>&#945;</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mi>&#160;</mi><mo>&#8805;</mo><mn>1</mn><mo>,</mo></math> for all <math><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>64</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>32</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>27</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>27</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>4</mn><mi>&#945;</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>8</mn><mi>&#945;</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mn>8</mn><mi>&#945;</mi><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math> attains its minimum at <math><mi>x</mi><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn><mi>&#945;</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced open="{" close="}"><msup><mfenced separators="|"><mfrac><mn>1</mn><mrow><mn>8</mn><mi>&#945;</mi></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mfenced><mo>=</mo><mn>1</mn></math>
<math><mo>&#8658;</mo></math> <math><mn>4</mn><mi>&#945;</mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn><mi>&#945;</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mn>8</mn><mi>&#945;</mi></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>=</mo><mn>1</mn></math>
<math><mo>&#8658;</mo></math> <math><mn>3</mn><msup><mrow><mi>&#945;</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>=</mo><mn>1</mn><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>27</mn></mrow></mfrac></math>

</details>

---

### Q13. JEE Advanced 2015 (Paper 1)

*Type:* `numerical` | *Level:* `2`

A cylindrical container is to be made from certain solid material with the following constraints: It has a fixed inner volume of <math><mi mathvariant="normal">V</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><msup><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mn>3</mn></mrow></msup></math>, has a 2 mm thick solid wall and is open at the top. The bottom of the container is a solid circular disc of thickness 2mm and is of radius equal to the outer radius of the container.
If the volume of the material used to make the container is minimum when the inner radius of the container is 10mm, then the value of <math><mfrac><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>250</mn><mi mathvariant="normal">&#960;</mi></mrow></mfrac><mi mathvariant="normal">&#160;</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

Volume of material used
 <math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mi mathvariant="normal">π</mi><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">h</mi><mo>-</mo><mi mathvariant="normal">π</mi><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">h</mi><mo>+</mo><mi mathvariant="normal">π</mi><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>.</mo><mn>2</mn></math> 
 <math><mo>=</mo><mn>4</mn><mi mathvariant="normal">π</mi><mi mathvariant="normal">h</mi><mfenced separators="|"><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mi mathvariant="normal">π</mi><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math> 
 <math><mo>=</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">V</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mfenced separators="|"><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mi mathvariant="normal">π</mi><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math> 
 <math><mfenced separators="|"><mrow><mo>∵</mo><mi mathvariant="normal">h</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mi mathvariant="normal">π</mi><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math> 
 <math><mfrac><mrow><mi mathvariant="normal">d</mi><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi></mrow></mfrac><mo>=</mo><mn>4</mn><mi mathvariant="normal">V</mi><mi mathvariant="normal"> </mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mo>+</mo><mn>4</mn><mi mathvariant="normal">π</mi><mfenced separators="|"><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math> 
Where  <math><mi mathvariant="normal">r</mi><mo>=</mo><mn>10</mn><mo>,</mo><mfrac><mrow><mi mathvariant="normal">d</mi><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><mn>4</mn><mi mathvariant="normal">V</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>100</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mn>1000</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mn>48</mn><mi mathvariant="normal">π</mi><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><mn>4</mn><mi mathvariant="normal">V</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>12</mn></mrow><mrow><mn>1000</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>48</mn><mi mathvariant="normal">π</mi></math> 
 <math><mo>∴</mo><mfrac><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>250</mn><mi mathvariant="normal">π</mi></mrow></mfrac><mo>=</mo><mn>4</mn></math>

</details>

---

### Q14. JEE Advanced 2013 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

A line L : <math> <mrow> <mi>y</mi> <mo>=</mo> <mtext mathvariant="italic">m</mtext> <mi>x</mi> <mo>+</mo> <mn>3</mn> </mrow> </math> meets <math> <mrow> <mi>y</mi> <mo>-</mo> <mi mathvariant="normal">a</mi> <mi mathvariant="normal">x</mi> <mtext mathvariant="normal">is</mtext> </mrow> </math> at E(0,3) and the arc of the parabola <math> <mrow> <msup> <mi>y</mi> <mn>2</mn> </msup> <mo>=</mo> <mn>1</mn> <mn>6</mn> <mi>x</mi> <mtext>,</mtext> <mspace width="0.5em"></mspace> <mn>0</mn> <mo>&#8804;</mo> <mi>y</mi> <mo>&#8804;</mo> <mn>6</mn> </mrow> </math> at the point <math> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>F</mi><mo>&#8289;</mo> <mfenced close=")" open="(" separators=","> <mrow> <msub> <mi>x</mi> <mn>0</mn> </msub> </mrow> <mrow> <msub> <mi>y</mi> <mn>0</mn> </msub> </mrow> </mfenced> </mrow> </math>.The tangent to the parabola at <math> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>F</mi><mo>&#8289;</mo> <mfenced close=")" open="(" separators=","> <mrow> <msub> <mi>x</mi> <mn>0</mn> </msub> </mrow> <mrow> <msub> <mi>y</mi> <mn>0</mn> </msub> </mrow> </mfenced> </mrow> </math> intersects the y-axis at <math> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>G</mi><mo>&#8289;</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>0</mn> </mrow> <mrow> <msub> <mi>y</mi> <mn>1</mn> </msub> </mrow> </mfenced> </mrow> </math>.The slope m of the line L is chosen such that the area of the triangle EFG has a local maximum.
Match List I with List II and select the correct answer using the code given below the lists :
 <table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td>List I</td>			<td> </td>			<td>List II</td>		</tr>		<tr>			<td>A.</td>			<td>m = </td>			<td>P.</td>			<td><math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math></td>		</tr>		<tr>			<td>B.</td>			<td>Maximum area of &Delta;EFG is</td>			<td>Q.</td>			<td>4</td>		</tr>		<tr>			<td>C.</td>			<td>y<sub>0</sub>​ =</td>			<td>R.</td>			<td>2</td>		</tr>		<tr>			<td>D.</td>			<td>y<sub>1</sub><sub> </sub>=<sub> </sub></td>			<td>S.</td>			<td>1</td>		</tr>	</tbody></table>

**Options:**

- **(A)** a-p;b-q;c-s;d-r;
- **(B)** a-s;b-p;c-q;d-r;
- **(C)** a-r;b-q;c-s;d-p;
- **(D)** a-p;b-q;c-s;d-r;

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a-s;b-p;c-q;d-r;**

**Detailed Solution:**

tangent at F      yt = c + 4t<sup>2</sup>
a : x = 0        y = 4t   (0,4t)
(4t<sup>2</sup>,8t) satisfies the line
8t = 4mt<sup>2</sup> + 3
4mt<sup>2</sup> - 8t + 3 = 0
<math> <mrow> <mtext>Area</mtext> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfenced close="|" open="|" separators=","> <mrow> <mtable> <mtr> <mtd> <mn>0</mn> </mtd> <mtd> <mn>3</mn> </mtd> <mtd> <mn>1</mn> </mtd> </mtr> <mtr> <mtd> <mn>0</mn> </mtd> <mtd> <mn>4</mn> <mi>t</mi> </mtd> <mtd> <mn>1</mn> </mtd> </mtr> <mtr> <mtd> <mn>4</mn> <msup> <mi>t</mi> <mn>2</mn> </msup> </mtd> <mtd> <mn>8</mn> <mi>t</mi> </mtd> <mtd> <mn>1</mn> </mtd> </mtr> </mtable> </mrow> </mfenced> </mrow> </math>
<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM00012667_AnsExp_1.jpg" style="width: 300px; height: 165px;" />
<math> <mrow> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfenced close=")" open="(" separators=","> <mrow> <mn>4</mn> <msup> <mi>t</mi> <mn>2</mn> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mn>3</mn> <mo>-</mo> <mn>4</mn> <mi>t</mi> </mrow> </mfenced> </mrow> </mfenced> </mrow> </math>
<math> <mrow> <mo>=</mo> <mn>2</mn> <msup> <mi>t</mi> <mn>2</mn> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mn>3</mn> <mo>-</mo> <mn>4</mn> <mi>t</mi> </mrow> </mfenced> </mrow> </math>
<math> <mrow> <mtext>A</mtext> <mo>=</mo> <mn>2</mn> <mspace></mspace> <mfenced close="]" open="[" separators=","> <mrow> <mn>3</mn> <msup> <mi>t</mi> <mn>2</mn> </msup> <mo>-</mo> <mn>4</mn> <msup> <mi>t</mi> <mn>3</mn> </msup> </mrow> </mfenced> </mrow> </math>
<math> <mrow> <mo>=</mo> <mfrac> <mrow> <mtext>dA</mtext> </mrow> <mrow> <mtext>dt</mtext> </mrow> </mfrac> <mo>=</mo> <mn>2</mn> <mfenced close="]" open="[" separators=","> <mrow> <mn>6</mn> <mi>t</mi> <mo>-</mo> <mn>1</mn> <mn>2</mn> <msup> <mi>t</mi> <mn>2</mn> </msup> </mrow> </mfenced> </mrow> </math>
= 24 t(1 - 2t)
<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/58_question_number.jpg" style="width: 291px; height: 117px;" />​
t = 1/2 maxima
<math> <mrow> <mtext>G</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mn>0</mn> </mrow> <mrow> <mn>4</mn> <mi>t</mi> </mrow> </mfenced> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mo>⇒</mo> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mtext>G</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mn>0</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfenced> </mrow> </math>
y<sub>1</sub> = 2
<math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <msub> <mi>x</mi> <mn>0</mn> </msub> </mrow> <mrow> <msub> <mi>y</mi> <mn>0</mn> </msub> </mrow> </mfenced> <mo>=</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>4</mn> <msup> <mi>t</mi> <mn>2</mn> </msup> </mrow> <mrow> <mn>8</mn> <mi>t</mi> </mrow> </mfenced> <mo>=</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfenced> </mrow> </math>
<math> <mrow> <msub> <mi>y</mi> <mn>0</mn> </msub> <mo>=</mo> <mn>4</mn> </mrow> </math>
<math> <mrow> <mtext>Area</mtext> <mo>=</mo> <mn>2</mn> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </mfenced> <mo>=</mo> <mn>2</mn> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mn>3</mn> <mo>-</mo> <mn>2</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </mfenced> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>

</details>

---

### Q15. JEE Advanced 2013 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext mathvariant="italic">f</mtext><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mfenced close="|" open="|"><mrow><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced close="|" open="|"><mi>x</mi></mfenced></mrow></mfenced></math> has a local minimum or a local maximum at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mfenced close="|" open="|"><mrow><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced close="|" open="|"><mi>x</mi></mfenced></mrow></mfenced></math></p><p><u>CASE 1:</u></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8804;</mo><mo>-</mo><mn>2</mn><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>&#8757;</mo><mo>&#160;</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#60;</mo><mn>0</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>-</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>+</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>&#160;</mo><mo>(</mo><mo>&#8757;</mo><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>&#60;</mo><mn>0</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><u>CASE 2:</u></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mi>x</mi><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>&#160;</mo><mo>(</mo><mo>&#8757;</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#62;</mo><mn>0</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>-</mo><mfenced close="|" open="|"><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>-</mo><mfenced close="|" open="|"><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="}" open="{"><mtable><mtr><mtd><mo>-</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>+</mo><mo>(</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>-</mo><mo>(</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="}" open="{"><mtable><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn><mi>x</mi><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p><u>CASE 3:</u></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>-</mo><mfenced close="|" open="|"><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>-</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="}" open="{"><mtable><mtr><mtd><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>-</mo><mo>(</mo><mo>-</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>+</mo><mo>(</mo><mo>-</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="}" open="{"><mtable><mtr><mtd><mn>4</mn><mi>x</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>3</mn><mo>)</mo></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mn>2</mn><mo>)</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>(</mo><mn>3</mn><mo>)</mo><mo>,</mo></math> we get
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext mathvariant="italic">f</mtext><mtext>(</mtext><mtext mathvariant="italic">x</mtext><mtext>)=</mtext><mfenced close="}" open="{"><mtable><mtr><mtd><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>,</mo></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn><mi>x</mi><mo>,</mo></mtd><mtd><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn><mi>x</mi><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM00012613_AnsExp_1.jpg" style="width: 250px; height: 216px;" />
From graph, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> has local minima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></math> and local maxima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q16. JEE Advanced 2013 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

<p>A rectangular sheet of fixed perimeter with sides having their lengths in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>:</mo><mn>15</mn></math> is converted into an open rectangular box by folding after removing squares of equal area from all four corners. If the total area of removed squares is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>, the resulting box has maximum volume. Then the lengths of the sides of the rectangular sheet are:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM00012563_AnsExp_1.jpg"/>
​
Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo> = </mo><mn>8</mn><mi>x</mi><mi>,</mi><mspace width="0.5em"></mspace><mi>b</mi><mo> = </mo><mn>15</mn><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo></math> Volume<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>8</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>a</mi></mrow></mfenced><mfenced><mrow><mn>15</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>a</mi></mrow></mfenced><mfenced><mi>a</mi></mfenced><mo>=</mo><mn>4</mn><msup><mi>a</mi><mn>3</mn></msup><mo>-</mo><mn>46</mn><msup><mi>a</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>120</mn><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>a</mi></mrow></mfrac><mo> = </mo><mn>6</mn><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>46</mn><mi>a</mi><mi>x</mi><mo>+</mo><mn>60</mn><msup><mi>x</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>a</mi></mrow></mfrac></mfenced><mrow><mi>a</mi><mi>t</mi><mo> </mo><mo>a</mo><mo> = </mo><mn>5</mn></mrow></msub><mo> = </mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi>x</mi><mo> = </mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>6</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>V</mi></mrow><mrow><mi>d</mi><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo> = </mo><mn>6</mn><mi>a</mi><mo>-</mo><mn>23</mn><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>V</mi></mrow><mrow><mi>d</mi><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mrow><mi>a</mi><mi>t</mi><mo> </mo><mo>a</mo><mo> = </mo><mn>5</mn><mspace width="0.5em"></mspace><mi>&</mi><mspace width="0.5em"></mspace><mi>x</mi><mo> = </mo><mn>3</mn></mrow></msub><mo><</mo><mn>0</mn></math>
So, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math>, it gives maxima:
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>V</mi></mrow><mrow><mi>d</mi><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mrow><mi>a</mi><mi>t</mi><mo> </mo><mo>a</mo><mo> = </mo><mn>5</mn><mspace width="0.5em"></mspace><mi>&</mi><mspace width="0.5em"></mspace><mi>x</mi><mo> = </mo><mfrac><mn>5</mn><mn>6</mn></mfrac></mrow></msub><mo>></mo><mn>0</mn></math>
So, at <math> <mrow> <mtext>x</mtext> <mo> = </mo> <mfrac> <mrow> <mn>5</mn> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> </mrow> </math> , it gives minima.
So by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math> (for max volume):
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>x</mi><mo> </mo><mo>=</mo><mo> </mo><mn>24</mn><mo>,</mo><mo> </mo><mn>15</mn><mi>x</mi><mo> </mo><mo>=</mo><mo> </mo><mn>45</mn></math>

</details>

---

### Q17. JEE Advanced 2012 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

If $f(x)=\int_{0}^{x} e^{t^{2}}(t-2)(t-3) d t$ for all $x \in(0, \infty)$, then

**Options:**

- **(A)** $f$ has a local maximum at $x=2$
- **(B)** $f$ is decreasing on $(2,3)$
- **(C)** there exists some $c \in(0, \infty)$, such that $f^{\prime \prime}(c)=0$
- **(D)** $f$ has a local minimum at $x=3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $f$ has a local minimum at $x=3$**

**Detailed Solution:**

$f(x)=\int_{0}^{x} e^{t^{2}}(t-2)(t-3) d t$

$\Rightarrow f^{\prime}(x)=e^{x^{2}} \cdot(x-2)(x-3)$

Put $f^{\prime}(x)=0 \Rightarrow x=2,3$

$f^{\prime \prime}(x)=e^{x^{2}} \cdot 2 x\left(x^{2}-5 x+6\right)+e^{x^{2}}(2 x-5)$

$f^{\prime \prime}(2)=-$ ve and $f^{\prime \prime}(3)=+$ ve

$\therefore \quad x=2$ is a point of local maxima.

and $x=3$ is a point of local minima.

Also for $x \in(2,3), f^{\prime}(x) < 0$

$\Rightarrow \quad f$ is decreasing on $(2,3)$.

Also we observe $f^{\prime \prime}(0) < 0$ and $f^{\prime \prime}(1)>0$

$\therefore \quad$ There exists some $C \in(0,1)$ such that $f^{\prime \prime}(C)=0$

Hence all the options are correct.

</details>

---

### Q18. JEE Advanced 2012 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)=(1-x)^{2} \sin ^{2} x+x^{2}$ for all $x \in I R$ and let $g(x)=\int_{1}^{x}\left(\frac{2(t-1)}{t+1}-\ln t\right) f(t) d t$ for all $x \in(1, \infty)$.

<strong> Question:</strong> Which of the following is true?

**Options:**

- **(A)** $g$ is increasing on $(1, \infty)$
- **(B)** $g$ is decreasing on $(1, \infty)$
- **(C)** $g$ is increasing on $(1,2)$ and decreasing on $(2, \infty)$
- **(D)** $g$ is decreasing on $(1,2)$ and increasing on $(2, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $g$ is decreasing on $(1, \infty)$**

**Detailed Solution:**

$g(x)=\int_{1}^{x}\left(\frac{2(t-1)}{t+1}-\ln t\right) f(t) d t$, $\therefore \quad g^{\prime}(x)=\left[\frac{2(x-1)}{x+1}-\ln x\right] f(x)$

Here $f(x)>0, \forall x \in(1, \infty)$

Let $h(x)=\frac{2(x-1)}{x+1}-\ln x$

$\therefore \quad h^{\prime}(x)=\frac{4}{(x+1)^{2}}-\frac{1}{x}=\frac{-(x-1)^{2}}{(x+1)^{2} x} < 0, x \in(1, \infty)$

$\Rightarrow h(x)$ is decreasing function.

Hence, for $x>1, h(x) < h(1) \Rightarrow h(x) < 0 \forall x>1$

$\Rightarrow g^{\prime}(x) < 0 \forall x \in(1, \infty)$

Therefore, $g(x)$ is decreasing on $(1, \infty)$.

</details>

---

### Q19. JEE Advanced 2012 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Let $p(x)$ be a real polynomial of least degree which has a local maximum at $x=1$ and a local minimum at $x=3$. If $p(1)=6$ and $p(3)=2$, then $p^{\prime}(0)$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

Since, $p(x)$ has a local maximum at $x=1$ and a local minimum at $x=3$ and $p(x)$ is a real polynomial of least degree.

Hence, let $p^{\prime}(x)=k(x-1)(x-3)=k\left(x^{2}-4 x+3\right)$

$\Rightarrow p(x)=k\left(\frac{x^{3}}{3}-2 x^{2}+3 x\right)+c$

Now, $p(1)=6$ and $p(3)=2$

$\begin{array}{l}

\Rightarrow \frac{4}{3} k+C=6 \text { and } 0+C=2 \Rightarrow k=3 \\

\therefore \quad p^{\prime}(x)=3(x-1)(x-3) \Rightarrow p^{\prime}(0)=9

\end{array}$

</details>

---

### Q20. JEE Advanced 2012 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Let $f: I R \rightarrow I R$ be defined as $f(x)=|x|+\left|x^{2}-1\right|$. The total number of points at which $f$ attains either a local maximum or a local minimum is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$f(x)=|x|+\left|x^{2}-1\right|=\left\{\begin{array}{c}-x+x^{2}-1, x < -1 \\ -x-x^{2}+1,-1 \leq x \leq 0 \\ x-x^{2}+1,0 < x < 1 \\ x^{2}+x-1, \quad x \geq 1\end{array}\right.$

$\therefore \quad f^{\prime}(x)=\left[\begin{array}{ccc}

2 x-1 & , & x < -1 \\

-2 x-1 & , & -1 \leq x \leq 0 \\

-2 x+1 & , & 0 < x < 1 \\

2 x+1 & , & x>1

\end{array}\right.$

Critical points are $\frac{1}{2}, \frac{-1}{2},-1,0$ and 1 .

We observe at five points $f^{\prime}(x)$ changes its sign $\therefore$ There are 5 points at which either local maximum or local minimum.

</details>

---

### Q21. JEE Advanced 2010 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Consider the polynomial $f(x)=1+2 x+3 x^2+4 x^3$. Let $s$ be the sum of all distinct real roots of $f(x)$ and let $t=|s|$.<strong>Question:</strong>
The function $f^{\prime}(x)$ is

**Options:**

- **(A)** increasing in $\left(-t,-\frac{1}{4}\right)$ and decreasing in $\left(-\frac{1}{4}, t\right)$
- **(B)** decreasing in $\left(-t,-\frac{1}{4}\right)$ and increasing in $\left(-\frac{1}{4}, t\right)$
- **(C)** increasing in $(-t, t)$
- **(D)** decreasing in $(-t, t)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) decreasing in $\left(-t,-\frac{1}{4}\right)$ and increasing in $\left(-\frac{1}{4}, t\right)$**

**Detailed Solution:**

Figure is self explanatory
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/Yf8F0vDp7puZQLSSihCgSEcJFmQDlRj7xCZcbdgaFhU.original.fullsize.png">

</details>

---

### Q22. JEE Advanced 2010 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Consider the polynomial $f(x)=1+2 x+3 x^2+4 x^3$. Let $s$ be the sum of all distinct real roots of $f(x)$ and let $t=|s|$.<strong>Question:</strong>
The real number $s$ lies in the interval

**Options:**

- **(A)** $\left(-\frac{1}{4}, 0\right)$
- **(B)** $\left(-11,-\frac{3}{4}\right)$
- **(C)** $\left(-\frac{3}{4},-\frac{1}{2}\right)$
- **(D)** $\left(0, \frac{1}{4}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(-\frac{3}{4},-\frac{1}{2}\right)$**

**Detailed Solution:**

Given, $f(x)=4 x^3+3 x^2+2 x+1$
$$
\begin{aligned}
& f^{\prime}(x)=2\left(6 x^2+3 x+1\right) \\
& D=9-24 < 0
\end{aligned}
$$
Hence, $f(x)=0$ has only one real root.
$$
\begin{aligned}
f\left(-\frac{1}{2}\right) & =1-1+\frac{3}{4}-\frac{4}{8}>0 \\
f\left(-\frac{3}{4}\right) & =1-\frac{6}{4}+\frac{27}{16}-\frac{108}{64} \\
& =\frac{64-96+108-108}{64} < 0
\end{aligned}
$$
$f(x)$ changes its sign in $\left(-\frac{3}{4}, \frac{-1}{2}\right)$, hence $f(x)=0$ has a root in $\left(\frac{-3}{4}, \frac{-1}{2}\right)$.

</details>

---

### Q23. JEE Advanced 2010 (Paper 2)

*Type:* `numerical` | *Level:* `3`

Let $f$ be a function defined on $R$ (the set of all real numbers) such that $f^{\prime}(x)=2010(x-2009)$ $(x-2010)^2(x-2011)^3(x-2012)^4$, for all $x \in R$. If $g$ is a function defined on $R$ with values in the interval $(0, \infty)$ such that $f(x)=\ln (g(x))$, for all $x \in R$, then the number of points in $R$ at which $g$ has a local maximum is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

Let $g(x)=e^{f(x)}, \forall x \in R$
$$
\Rightarrow g^{\prime}(x)=e^{f(x)} \cdot f^{\prime}(x)
$$
$\Rightarrow f^{\prime}(x)$ changes its sign from positive to negative in the neighbourhood of $x=2009$
$\Rightarrow f(x)$ has local maxima at $x=2009$
So, the number of local maximum is one.

</details>

---

### Q24. JEE Advanced 2010 (Paper 1)

*Type:* `numerical` | *Level:* `1`

The maximum value of the expression $\frac{1}{\sin ^2 \theta+3 \sin \theta \cos \theta+5 \cos ^2 \theta}$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

Let
$$
\begin{aligned}
& f(\theta)=\frac{1}{\sin ^2 \theta+3 \sin \theta \cos \theta+5 \cos ^2 \theta} \\
& \text { Again let } \\
& g(\theta)=\sin ^2 \theta+3 \sin \theta \cos \theta+5 \cos ^2 \theta \\
& =\frac{1-\cos 2 \theta}{2}+5\left(\frac{1+\cos 2 \theta}{2}\right)+\frac{3}{2} \sin 2 \theta \\
& =3+2 \cos 2 \theta+\frac{3}{2} \sin 2 \theta \\
& \therefore \quad g(\theta)_{\min }=3-\sqrt{4+\frac{9}{4}}=3-\frac{5}{2}=\frac{1}{2} \\
& \therefore \quad f(\theta)=\frac{1}{g(\theta)_{\min }}=2
\end{aligned}
$$

</details>

---

### Q25. JEE Advanced 2010 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $f, g$ and $h$ be real-valued functions defined on the interval $[0,1]$ by $f(x)=e^{x^2}+e^{-x^2}, \quad g(x)=x e^{x^2}+e^{-x^2}$ and $h(x)=x^2 e^{x^2}+e^{-x^2}$. If $a, b$ and $c$ denote respectively, the absolute maximum of $f, g$ and $h$ on $[0,1]$, then

**Options:**

- **(A)** $a=b$ and $c \neq b$
- **(B)** $a=c$ and $a \neq b$
- **(C)** $a \neq b$ and $c \neq b$
- **(D)** $a=b=c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a=b=c$**

**Detailed Solution:**

Given function,
$$
\begin{aligned}
& f(x)=e^{x^2}+e^{-x^2}, \\
& g(x)=x e^{x^2}+e^{-x^2} \text { and } \\
& h(x)=x^2 e^{x^2}+e^{-x^2} \text { are } \quad \text { strictly }
\end{aligned}
$$
increasing on $[0,1]$. Hence, at $x=1$, the given function attains absolute maximum all equal to $e+\frac{1}{e}$.
$$
\Rightarrow \quad a=b=c
$$

</details>

---

### Q26. JEE Advanced 2009 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let $p(x)$ be a polynomial of degree 4 having extremum at $x=1,2$ and $\lim _{x \rightarrow 0}\left[1+\frac{p(x)}{x^2}\right]=2$. Then, the value of $p(2)$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

Let $p(x)=a x^4+b x^3+c x^2+d x+e$
$$
\Rightarrow \quad p^{\prime}(x)=4 a x^3+3 b x^2+2 c x+d
$$
$$
\therefore \quad p^{\prime}(1)=4 a+3 b+2 c+d=0
$$
and $p^{\prime}(2)=32 a+12 b+4 c+d=0$
Since, $\lim _{x \rightarrow 0}\left(1+\frac{p(x)}{x^2}\right)=2 \quad$ [given]
$$
\lim _{x \rightarrow 0} \frac{a x^4+b x^3+(c+1) x^2+d x+e}{x^2}=2
$$

$$
\begin{array}{rlrl}
\Rightarrow & & x+1=2, d & =0, e=0 \\
\Rightarrow & c & =1
\end{array}
$$
From Eqs. (i) and (ii)
$$
\begin{array}{rlrl} 
& & 4 a+3 b=-2 & \text { and } 32 a+12 b=-4 \\
\Rightarrow & & a=\frac{1}{4} \text { and } b=-1 \\
\therefore & & p(x)=\frac{x^4}{4}-x^3+x^2 \\
\Rightarrow & & p(2)=\frac{16}{4}-8+4
\end{array}
$$

</details>

---

### Q27. JEE Advanced 2009 (Paper 2)

*Type:* `numerical` | *Level:* `3`

The maximum value of the function $f(x)=2 x^3-15 x^2+36 x-48$ on the set $A=\left\{x \mid x^2+20 \leq 9 x\right\}$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

Given, $\quad A=\left\{x \mid x^2+20 \leq 9 x\right\}$ $=\{x \mid x \in[4,5]\}$
Now, $f^{\prime}(x)=6\left(x^2-5 x+6\right)$
Put $\quad f^{\prime}(x)=0 \Rightarrow x=2,3$
$f(2)=-20, f(3)=-21$,
$f(4)=-16, f(5)=7$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/mEW_vIq8xq9QBru_tFUMUU1wi-RfOrrWT0nYPgn4aLo.original.fullsize.png">

From graph, maximum of $f(x)$ on set $A$ is $f(5)=7$.

</details>

---

### Q28. JEE Advanced 2009 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

For the function $f(x)=x \cos \frac{1}{x}, x \geq 1$,

**Options:**

- **(A)** for atleast one $x$ in the interval $[1, \infty)$, $f(x+2)-f(x) < 2$
- **(B)** $\lim _{x \rightarrow \infty} f^{\prime}(x)=1$
- **(C)** for all $x$ in the interval $[1, \infty)$, $f(x+2)-f(x)>2$
- **(D)** $f^{\prime}(x)$ is strictly decreasing in the interval $[1, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $f^{\prime}(x)$ is strictly decreasing in the interval $[1, \infty)$**

**Detailed Solution:**

Given, $f(x)=x \cos \frac{1}{x}, x \geq 1$
$$
\begin{aligned}
& \Rightarrow \quad f^{\prime}(x)=\frac{1}{x} \sin \frac{1}{x}+\cos \frac{1}{x} \\
& \Rightarrow \quad f^{\prime \prime}(x)=-\frac{1}{x^3} \cos \left(\frac{1}{x}\right)
\end{aligned}
$$
Now, $\lim _{x \rightarrow \infty} f^{\prime}(x)=0+1=1$
$\Rightarrow$ Option (b) is correct.
Now, $\quad x \in[1, \infty) \Rightarrow \frac{1}{x} \in(0,1]$
$\Rightarrow f^{\prime \prime}(x) < 0 \Rightarrow$ Option (d) is correct.
As $f^{\prime}(1)=\sin 1+\cos 1>1$
$f^{\prime}(x)$ is strictly decreasing and $\lim _{x \rightarrow \infty} f^{\prime}(x)=1$
So, graph of $f^{\prime}(x)$ is shown as below.<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/hS4edZSTwmV2Y_WsflnxEkx7RVsGq8BZPllC_0llCFk.original.fullsize.png">

Now, in $[x, x+2], x \in[1, \infty), f(x)$ is continuous and differentiable so by LMVT,
$$
f^{\prime}(x)=\frac{f(x+2)-f(x)}{2}
$$
As $f^{\prime}(x)>1$ for all $x \in[1, \infty)$
$$
\begin{aligned}
& \Rightarrow \quad \frac{f(x+2)-f(x)}{2}>1 \\
& \Rightarrow f(x+2)-f(x)>2 \quad \text { for all } x \in[1, \infty)
\end{aligned}
$$

</details>

---

### Q29. JEE Advanced 2008 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

The total number of local maxima and local minima of the function $f(x)=\left\{\begin{array}{lc}(2+x)^3 ; & -3 < x \leq-1 \\ x^{\frac{2}{3}} ; & -1 < x < 2\end{array}\right.$ is

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

Given that, $f(x)=\left\{\begin{array}{l}(2+x)^3 ;-3 < x \leq-1 \\ x^{2 / 3} ; \quad-1 < x < 2\end{array}\right.$
$$
\Rightarrow \quad f^{\prime}(x)=\left\{\begin{array}{l}
3(2+x)^2 ;-3 < x \leq 1 \\
\frac{2}{3} x^{-\frac{1}{3}} ; \quad-1 < x < 2
\end{array}\right.
$$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/O3q5lbRV0bbl0iS0OWGpiOvzf4DQr3JZZm7V5HR-HEY.original.fullsize.png">

Clearly, $f^{\prime}(x)$ changes its sign at $x=-1$ from $+$ ve to -ve and so $f(x)$ has local maxima at $x=-1$.
Also, $f^{\prime}(0)$ does not exist but $f^{\prime}\left(0^{-}\right) < 0$ and $f^{\prime}\left(0^{+}\right) < 0$.
It can only be inferred that $f(x)$ has a possibility of a minima at $x=0$.
Hence, the given function has one local maxima at $x=-1$ and one local minima at $x=0$.

</details>

---

### Q30. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `1`

<strong>Paragraph:</strong>
Read the following passage and answer the questions.
For every function $f(x)$ which is twice differentiable, these will be good approximation of $\int_a^b f(x) d x \cong\left(\frac{b-a}{2}\right)\{f(a)+f(b)\}$. Now, if we take $c=\frac{a+b}{2}$, then using above again, we get $\int_a^b f(x) d x=\int_a^c f(x) d x+\int_c^b f(x) d x \cong \frac{b-a}{4}\{f(a)+f(b)+2 f(c)\}$ and so on.
We get approximation for value of $\int_a^b f(x) d x$.<strong>Question:</strong>
If $f^{\prime \prime}(x) < 0, \forall x \in(a, b), c(c, f(c))$ is point of maxima where $c \in(a, b)$, then $f^{\prime}(c)$ is

**Options:**

- **(A)** $\frac{f(b)-f(a)}{b-a}$
- **(B)** $3\left(\frac{f(b)-f(a)}{b-a}\right)$
- **(C)** $2\left(\frac{f(b)-f(a)}{b-a}\right)$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

$f^{\prime}(c)=0$.

</details>

---

### Q31. JEE Advanced 2006

*Type:* `multipleCorrect` | *Level:* `2`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/5J9jOFz5SPHXym-2E7yNW6FpxEcbDxNYH9Z-gh2VeMk.original.fullsize.png">

**Options:**

- **(A)** $g(x)$ has local maxima at $x=1+\log _e 2$ and local minima at $x=e$
- **(B)** $f(x)$ has local maxima at $x=1$, and local minima at $x=2$
- **(C)** $g(x)$ has no local minima
- **(D)** $f(x)$ has no local maxima

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $f(x)$ has local maxima at $x=1$, and local minima at $x=2$**

**Detailed Solution:**

Here, $f(x)=\left\{\begin{array}{cc}e^x, & 0 \leq x \leq 1 \\ 2-e^{x-1}, & 1 < x \leq 2 \\ x-e, & 2 < x \leq 3\end{array}\right.$ and $\quad g(x)=\int_0^x f(t) d t$
$$
\Rightarrow \quad g^{\prime}(x)=f(x)
$$
where, $g^{\prime}(x)=0$
$\Rightarrow \quad x=1+\log _e 2$
and $\quad x=e$.
Also, $\quad g(x)=\left\{\begin{array}{cc}-e^{x-1}, & 1 < x \leq 2 \\ 1, & 2 < x \leq 3\end{array}\right.$
$g\left(1+\log _e 2\right)=-e^{\log _e 2} < 0$, hence at $x=1+\log _e 2, g(x)$ has a local maximum.
Also, $g(e)=1>0$, hence at $x=e, g(x)$ has a local minima.
$\because f(x)$ is discontinuous at $x=1$, then we get
Local maxima at $x=1$ and local minima at $x=2$.

</details>

---

### Q32. JEE Advanced 2006

*Type:* `multipleCorrect` | *Level:* `3`

If $f(x)$ is cubic polynomial which has local maximum at $x=-1$. If $f(2)=18, f(1)=-1$ and $f^{\prime}(x)$ has local minimum at $x=0$, then

**Options:**

- **(A)** the distance between $(-1,2)$ and $(a, f(a))$ where $x=a$ is the point of local minima is $2 \sqrt{5}$
- **(B)** $f(x)$ is increasing for $x \in[1,2 \sqrt{5}]$
- **(C)** $f(x)$ has local minima at $x=1$
- **(D)** the value of $f(0)=5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $f(x)$ has local minima at $x=1$**

**Detailed Solution:**

Since $f(x)$ has local maxima at $x=-1$ and $f^{\prime}(x)$ has local minima at $x=0$.
$$
\begin{aligned}
f \wedge(x) & =\lambda x \\
f^{\prime}(x) & =\lambda \frac{x^2}{2}+c \\
\frac{\lambda}{2}+c & =0 \Rightarrow \lambda=-2 c
\end{aligned}
$$
$$
\left[f^{\prime}(-1)=0\right]
$$
Again, On integrating both sides, we get
$$
\begin{aligned}
& f(x)=\lambda \frac{x^3}{6}+c x+d \\
& f(2)=\lambda\left(\frac{8}{6}\right)+2 c+d=18 \\
& f(1)=\frac{\lambda}{6}+c+d=-1
\end{aligned}
$$
and
$\therefore$ Using Eqs. (i), (ii) and (iii), we get
$$
\begin{aligned}
f(x) & =\frac{1}{4}\left(19 x^3-57 x+34\right) \\
\therefore \quad f^{\prime}(x) & =\frac{1}{4}\left(57 x^2-57\right) \\
& =\frac{57}{4}(x-1)(x+1), \text { using number line rule }
\end{aligned}
$$
$\therefore f(x)$ is increasing for $[1,2 \sqrt{5}]$ and $f(x)$ is increasing for $[1,2 \sqrt{5}]$ and $f(x)$ has local maximum at $x=-1$ and $f(x)$ has local minimum at $C x=1$.
Also,
$$
f(0)=\frac{34}{4} \text {. }
$$

</details>

---

