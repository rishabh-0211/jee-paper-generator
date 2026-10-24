# JEE Advanced Mathematics - Continuity and Differentiability

## Topic 1: Continuity

**Total Questions:** 8

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `3`

For a real number $\alpha$, let $[\alpha]$ denote the greatest integer less than or equal to $\alpha$. For a finite set $S$, let $|S|$ denote the number of elements in the set $S$.
Consider the functions $f : (-3, 3) \rightarrow (-\infty, \infty)$ and $g : (-3, 3) \rightarrow (-\infty, \infty)$ defined by
$f(x) = [x^3]\log_e(1 + \sin^2(\pi(x - [x])))$
and
$g(x) = x^3 \sin^2(\pi \log_e(1 + x - [x]))$.
Let
$A = \{x \in (-3, 3) : f \text{ is discontinuous at } x\}$
and
$B = \{x \in (-3, 3) : g \text{ is discontinuous at } x\}$.
Then the value of $|A| + 2|B| - |A \cap B|$ is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **56**

**Detailed Solution:**

For the function $f(x) = [x^3]\log_e(1 + \sin^2(\pi(x - [x])))$, we can simplify the argument of the sine function. Since $[x]$ is an integer, $\sin(\pi(x - [x])) = \sin(\pi x - \pi[x]) = \pm \sin(\pi x)$. Thus, $\sin^2(\pi(x - [x])) = \sin^2(\pi x)$.

The function $f(x)$ can be rewritten as $f(x) = [x^3]\log_e(1 + \sin^2(\pi x))$.
The term $\log_e(1 + \sin^2(\pi x))$ is continuous everywhere. The term $[x^3]$ has jump discontinuities where $x^3$ is an integer. For $x \in (-3, 3)$, $x^3 \in (-27, 27)$. The integer values of $x^3$ in this interval are $k \in \{-26, -25, \dots, 26\}$, which gives $53$ points of the form $x = k^{1/3}$.

At these points, $[x^3]$ is discontinuous. For $f(x)$ to be continuous at $x = k^{1/3}$, the continuous factor must be zero:
$\log_e(1 + \sin^2(\pi x)) = 0 \implies \sin^2(\pi x) = 0 \implies x$ is an integer.
The integers in $(-3, 3)$ are $-2, -1, 0, 1, 2$. Their cubes are $-8, -1, 0, 1, 8$, which are $5$ values among the $53$ points. At these $5$ points, $f(x)$ is continuous. At the remaining $53 - 5 = 48$ points, $f(x)$ is discontinuous.
Thus, $|A| = 48$.

For the function $g(x) = x^3 \sin^2(\pi \log_e(1 + x - [x]))$, we can write $x - [x] = \{x\}$, which is the fractional part of $x$.
The function $g(x) = x^3 \sin^2(\pi \log_e(1 + \{x\}))$ is continuous everywhere except possibly at the integers, where $\{x\}$ is discontinuous.
The integers in $(-3, 3)$ are $c \in \{-2, -1, 0, 1, 2\}$.
Let's check the continuity at $x = c$:
Right-hand limit ($x \to c^+$): $\{x\} \to 0$, so $g(x) \to c^3 \sin^2(\pi \log_e 1) = 0$.
Left-hand limit ($x \to c^-$): $\{x\} \to 1$, so $g(x) \to c^3 \sin^2(\pi \log_e 2)$.

For $g(x)$ to be continuous at $x = c$, we must have $c^3 \sin^2(\pi \log_e 2) = 0$. Since $\log_e 2 \approx 0.693$, $\pi \log_e 2$ is not an integer multiple of $\pi$, meaning $\sin^2(\pi \log_e 2) \neq 0$. Therefore, we must have $c^3 = 0 \implies c = 0$.
So, $g(x)$ is continuous at $x = 0$ and discontinuous at $x \in \{-2, -1, 1, 2\}$.
Thus, $B = \{-2, -1, 1, 2\}$ and $|B| = 4$.

Since $A$ contains no integers and $B$ contains only integers, $A \cap B = \emptyset$, which means $|A \cap B| = 0$.

Finally, we calculate the required value:
$|A| + 2|B| - |A \cap B| = 48 + 2(4) - 0 = 48 + 8 = 56$.

Answer: $56$

</details>

---

### Q2. JEE Advanced 2026 (Paper 1)

*Type:* `numerical` | *Level:* `3`

Consider the function $f : \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right) \rightarrow (-\infty, \infty)$ defined by

$f(x) = (|x| + |x - 1|) \sin x + [x \sin x]$,

where $[x \sin x]$ is the greatest integer less than or equal to $x \sin x$.

Let $\alpha$ be the total number of points in the interval $\left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$ at which $f$ is NOT continuous, and let $\beta$ be the total number of points in the interval $\left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$ at which $f$ is NOT differentiable.

Then the value of $\alpha + \beta$ is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

Let $f(x) = g(x) + h(x)$, where $g(x) = (|x| + |x - 1|) \sin x$ and $h(x) = [x \sin x]$.

First, we analyze $h(x) = [x \sin x]$ on the interval $\left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$.
The function $y = x \sin x$ is an even function. For $x \in \left[0, \dfrac{\pi}{2}\right)$, $x \sin x$ is strictly increasing. 
At $x = 0$, $x \sin x = 0$.
As $x \to \dfrac{\pi}{2}$, $x \sin x \to \dfrac{\pi}{2} \approx 1.57$.
Thus, $x \sin x \in [0, 1.57)$ for $x \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$.
The value of $[x \sin x]$ will be $0$ when $0 \le x \sin x < 1$, and $1$ when $1 \le x \sin x < \dfrac{\pi}{2}$.
Let $x_1 \in \left(0, \dfrac{\pi}{2}\right)$ be the unique point where $x_1 \sin x_1 = 1$. By symmetry, $-x_1$ is the unique point in $\left(-\dfrac{\pi}{2}, 0\right)$ where $(-x_1) \sin(-x_1) = 1$.
Therefore, $h(x)$ has jump discontinuities at exactly two points: $x = x_1$ and $x = -x_1$.
At $x = 0$, $x \sin x = 0$ and is non-negative in its neighborhood, so $[x \sin x] = 0$ around $x = 0$, making $h(x)$ continuous and differentiable at $x = 0$.

Next, we analyze $g(x) = (|x| + |x - 1|) \sin x$.
The absolute value functions have critical points at $x = 0$ and $x = 1$.
For $x$ in a small neighborhood of $0$ (specifically $x \in (-1, 1)$):
If $x \in [0, 1)$, $g(x) = (x - (x - 1)) \sin x = \sin x \Rightarrow g'(0^+) = \cos 0 = 1$.
If $x \in (-1, 0)$, $g(x) = (-x - (x - 1)) \sin x = (1 - 2x) \sin x \Rightarrow g'(0^-) = -2 \sin 0 + 1 \cdot \cos 0 = 1$.
Since $g'(0^+) = g'(0^-)$, $g(x)$ is differentiable at $x = 0$.

For $x$ in a small neighborhood of $1$:
If $x \in (0, 1]$, $g(x) = \sin x \Rightarrow g'(1^-) = \cos 1$.
If $x \in \left(1, \dfrac{\pi}{2}\right)$, $g(x) = (x + (x - 1)) \sin x = (2x - 1) \sin x \Rightarrow g'(1^+) = 2 \sin 1 + 1 \cdot \cos 1$.
Since $g'(1^-) \neq g'(1^+)$, $g(x)$ is not differentiable at $x = 1$.

Now, combining the results for $f(x) = g(x) + h(x)$:
1. Discontinuities: $g(x)$ is continuous everywhere. $h(x)$ is discontinuous at $x_1$ and $-x_1$. Thus, $f(x)$ is discontinuous at $2$ points. $\Rightarrow \alpha = 2$.
2. Non-differentiability: $f(x)$ is not differentiable where it is discontinuous ($x_1$ and $-x_1$). Additionally, at $x = 1$, $h(x)$ is constant ($0$) because $1 \cdot \sin 1 \approx 0.84 < 1$, meaning $h(x)$ is differentiable at $x = 1$. However, $g(x)$ is not differentiable at $x = 1$. Thus, $f(x)$ is not differentiable at $x = 1$.
This gives $3$ points of non-differentiability: $-x_1, 1, x_1$. $\Rightarrow \beta = 3$.

Finally, $\alpha + \beta = 2 + 3 = 5$.

Answer: $5$

</details>

---

### Q3. JEE Advanced 2026 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let $\mathbb{R}$ denote the set of all real numbers. Let $f : \mathbb{R} \rightarrow \mathbb{R}$ be an arbitrary function and let $g : \mathbb{R} \rightarrow \mathbb{R}$ be the function defined by

$g(x) = x f(x)$, for all $x \in \mathbb{R}$.

Then which of the following statements is (are) TRUE?

**Options:**

- **(A)** The function $g$ is always continuous at $x = 0$
- **(B)** If $f$ is continuous at $x = 0$, then $g$ is differentiable at $x = 0$
- **(C)** If $g$ is differentiable at $x = 0$, then $f$ is continuous at $x = 0$
- **(D)** If $g$ is differentiable at $x = 0$, then $\lim_{x \to 0} f(x)$ exists

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) If $g$ is differentiable at $x = 0$, then $\lim_{x \to 0} f(x)$ exists**

**Detailed Solution:**

Given $g(x) = x f(x)$ for all $x \in \mathbb{R}$.

For option A:
Let $f(x) = \dfrac{1}{x}$ for $x \neq 0$ and $f(0) = 0$.
Then $g(x) = 1$ for $x \neq 0$ and $g(0) = 0$.
$\lim_{x \to 0} g(x) = 1 \neq g(0)$.
Thus, $g$ is not necessarily continuous at $x = 0$. Option A is false.

For option B:
The derivative of $g$ at $x = 0$ is given by:
$g'(0) = \lim_{x \to 0} \dfrac{g(x) - g(0)}{x - 0} = \lim_{x \to 0} \dfrac{x f(x) - 0}{x} = \lim_{x \to 0} f(x)$.
If $f$ is continuous at $x = 0$, then $\lim_{x \to 0} f(x) = f(0)$.
Since $f(0)$ is a finite real number, $g'(0)$ exists and $g$ is differentiable at $x = 0$. Option B is true.

For option C:
Let $f(x) = 0$ for $x \neq 0$ and $f(0) = 1$.
Then $g(x) = 0$ for all $x \in \mathbb{R}$.
Here, $g$ is differentiable at $x = 0$ with $g'(0) = 0$.
However, $\lim_{x \to 0} f(x) = 0 \neq f(0)$, so $f$ is not continuous at $x = 0$. Option C is false.

For option D:
If $g$ is differentiable at $x = 0$, then $g'(0)$ exists.
Since $g'(0) = \lim_{x \to 0} \dfrac{g(x) - g(0)}{x} = \lim_{x \to 0} f(x)$, the limit $\lim_{x \to 0} f(x)$ must exist. Option D is true.

Answer: If $f$ is continuous at $x = 0$, then $g$ is differentiable at $x = 0$; If $g$ is differentiable at $x = 0$, then $\lim_{x \to 0} f(x)$ exists

</details>

---

### Q4. JEE Advanced 2023 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be the function defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><mrow><mn>4</mn><mi>x</mi></mrow></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. Then which of the following is(are) true?

**Options:**

- **(A)** The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is discontinuous exactly at one point in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math>
- **(B)** There is exactly one point in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> at which the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous but NOT differentiable
- **(C)** The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is NOT differentiable at more than three points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math>
- **(D)** The minimum value of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>512</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) There is exactly one point in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> at which the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous but NOT differentiable**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mn>4</mn><mi>x</mi></mrow></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>4</mn><mi>x</mi></mrow></mfenced></math> will be discontinuous function at integer points,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>critical point&#160;</mtext><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>And function will be discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math> because for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup></math> will make the function continuos</p><p>Hence, the function is discontinuous exactly at one point in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>, so option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> is correct,</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mtd></mtr><mtr><mtd><mn>1</mn><mo>&#183;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mn>2</mn><mo>&#183;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mtd></mtr><mtr><mtd><mn>3</mn><mo>&#183;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now differentiating the above function we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mtd></mtr><mtr><mtd><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mn>4</mn><mo>&#183;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mtd></mtr><mtr><mtd><mn>3</mn><mo>&#183;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>6</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now from above function we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo></msup></mfenced><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo></msup></mfenced><mo>=</mo><mn>0</mn></math> so function is differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo></msup></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>&#38;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo></msup></mfenced><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math> so function is non-differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>, hence option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> is correct,</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>-</mo></msup></mfenced><mo>=</mo><mn>4</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>+</mo></msup></mfenced><mo>=</mo><mn>3</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mn>6</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p>Hence, the function is not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p>So, function non-differentiable at two points so option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>C</mi></mfenced></math> is not correct.</p><p>Now plotting the graph from the above value we get,</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/61a98865-8d84-478f-b0b9-4c2166748046.png" style="width: 304px; height: 172px;" /></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> will be minimum between <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mfrac><mn>5</mn><mn>4</mn></mfrac></mrow></mfenced></math></p><p>Now critical points will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac></math></p><p>Now putting the value in first derivative we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>-</mo></msup></mfenced><mo>&#60;</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>+</mo></msup></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac></math> is point of minima,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><msub><mfenced><mfrac><mn>5</mn><mn>12</mn></mfrac></mfenced><mrow><mi>m</mi><mi>i</mi><mi>n</mi></mrow></msub><mo>=</mo><msup><mfenced><mrow><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>432</mn></mfrac></math></p><p>Hence, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>D</mi></mfenced></math> is wrong.</p>

</details>

---

### Q5. JEE Advanced 2017 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `1`

Let <math><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced></math> be the greatest integer less than or equals to <math><mi>x</mi></math>. Then, at which of the following point(s) the function <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi>&#960;</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></mrow></mrow></math> is discontinuous?

**Options:**

- **(A)** <math><mi>x</mi><mo>=</mo><mn>1</mn></math>
- **(B)** <math><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>**

**Detailed Solution:**

<p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi>&#960;</mi><mi>x</mi><mo>+</mo><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>&#960;</mi></mrow></mfenced></mrow></mrow></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced close="]" open="[" separators="|"><mi>x</mi></mfenced></msup><mi>x</mi><mi>cos</mi><mfenced><mrow><mi>&#960;</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> is discontinuous at all integers and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>cos</mi><mi>&#960;</mi><mi>x</mi></math> is continuous everywhere.</p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math>, so it&#39;s continuous.</p><p>At other integral points, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is discontinuous.</p>

</details>

---

### Q6. JEE Advanced 2014 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mo>:</mo><mfenced close="]" open="[" separators="|"><mrow><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi></mrow></mfenced><mo>&#8594;</mo><mfenced open="[" separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced></math> be a continuous function and let <math><mi>g</mi><mi>&#160;</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as
<math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mi>i</mi><mi>f</mi></mtd><mtd><mi>x</mi><mo>&#60;</mo><mi>a</mi><mo>,</mo></mtd></mtr><mtr><mtd><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mi>a</mi></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mrow></mtd><mtd><mi>i</mi><mi>f</mi></mtd><mtd><mi>a</mi><mi>&#160;</mi><mo>&#8804;</mo><mi>x</mi><mi>&#160;</mi><mo>&#8804;</mo><mi>b</mi><mo>,</mo></mtd></mtr><mtr><mtd><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mrow></mtd><mtd><mi>i</mi><mi>f</mi></mtd><mtd><mi>x</mi><mo>&#62;</mo><mi>b</mi></mtd></mtr></mtable></mrow></mfenced></math> . Then

**Options:**

- **(A)** <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is continuous but not differentiable at a
- **(B)** <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is differentiable on R
- **(C)** <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is continuous but not differentiable at b
- **(D)** <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is continuous and differentiable at either a or b but not both

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is continuous but not differentiable at b**

**Detailed Solution:**

Since  <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi> </mi><mo>≥</mo><mn>1</mn><mi> </mi><mo>∀</mo><mi> </mi><mi>x</mi><mi> </mi><mo>∈</mo><mfenced close="]" open="[" separators="|"><mrow><mi>a</mi><mo>,</mo><mi> </mi><mi>b</mi></mrow></mfenced></math>  for  <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> 
LHD at  <math><mi>x</mi><mo>=</mo><mi>a</mi></math>  is zero
And RHD at  <math><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mi>a</mi></mrow></mfenced><mo>=</mo><mi> </mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mi>a</mi></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder></mrow><mo>⁡</mo><mrow><mfrac><mrow><mrow><munderover><mo stretchy="false">∫</mo><mrow><mi>a</mi></mrow><mrow><mi>x</mi></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi><mo>-</mo><mn>0</mn></mrow></mrow></mrow><mrow><mi>x</mi><mo>-</mo><mi>a</mi></mrow></mfrac></mrow></mrow><mo>=</mo><mi> </mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mi>a</mi></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder></mrow><mo>⁡</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi> </mi><mo>≥</mo><mn>1</mn></mrow></mrow></math> 
Hence  <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is not differentiable at  <math><mi>x</mi><mo>=</mo><mi>a</mi></math> 
Similarly LHD at  <math><mi>x</mi><mo>=</mo><mi>b</mi></math>  is greater than 1
 <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is not differentiable at  <math><mi>x</mi><mo>=</mo><mi>b</mi></math>

</details>

---

### Q7. JEE Advanced 2012 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

For every integer $n$, let $a_{n}$ and $b_{n}$ be real numbers. Let function $f: I R \rightarrow I R$ be given by

$f(x)=\left\{\begin{array}{lll}

a_{n}+\sin \pi x, & \text { for } & x \in[2 n, 2 n+1] \\

b_{n}+\cos \pi x, & \text { for } & x \in(2 n-1,2 n)

\end{array}\right.$

for all integers $n$. If $f$ is continuous, then which of the following hold $(s)$ for all $n$ ?

**Options:**

- **(A)** $a_{n-1}-b_{n-1}=0$
- **(B)** $a_{n}-b_{n}=1$
- **(C)** $a_{n}-b_{n+1}=1$
- **(D)** $a_{n-1}-b_{n}=-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a_{n-1}-b_{n}=-1$**

**Detailed Solution:**

Given : $f(x)=\left\{\begin{array}{ll}a_{n}+\sin \pi x, & x \in[2 n, 2 n+1] \\ b_{n}+\cos \pi x, & x \in(2 n-1,2 n)\end{array}\right.$

$\because f$ is continuous for all $n$

$\therefore$ At $x=2 n, \mathrm{LHL}=\mathrm{RHL}=f(2 n)$

$\Rightarrow b_{n}+\cos 2 \pi n=a_{n}+\sin 2 \pi n=a_{n}+\sin 2 \pi n$

$\Rightarrow b_{n}+1=a_{n} \Rightarrow a_{n}-b_{n}=1, \therefore$ option (b) is correct.

Also at $x=2 n+1, \mathrm{LHL}=\mathrm{RHL}=f(2 n+1)$

$\Rightarrow \lim _{h \rightarrow 0} a_{n}+\sin \pi(2 n+1-h)$

$=\lim _{h \rightarrow 0} b_{n+1}+\cos \pi(2 n+1-h)=a_{n}+\sin (2 n+1) \pi$

$\Rightarrow a_{n}=b_{n+1}-1=a_{n} \Rightarrow a_{n}-b_{n+1}=-1$

$\therefore$ option (c) is incorrect.

$\Rightarrow a_{n-1}-b_{n}=-1, \therefore$ option (d) is correct.

</details>

---

### Q8. JEE Advanced 2012 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\int(x)=\left\{\begin{array}{r}x^{2}\left|\cos \frac{\pi}{x}\right|, \quad x \neq 0 \\ 0, \quad x=0\end{array}, x \in R\right.$ then $\int$ is

**Options:**

- **(A)** differentiable both at $x=0$ and at $x=2$
- **(B)** differentiable at $x=0$ but not differentiable at $x=2$
- **(C)** not differentiable at $x=0$ but differentiable at $x=2$
- **(D)** differentiable neither at $x=0$ nor at $x=2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) differentiable at $x=0$ but not differentiable at $x=2$**

**Detailed Solution:**

$f^{\prime}\left(0^{+}\right)=\lim _{h \rightarrow 0} \frac{f(0+h)-f(0)}{h}$

$\begin{aligned}

=\lim _{h \rightarrow 0} \frac{h^{2}\left|\cos \frac{\pi}{h}\right|}{h} &=\lim _{h \rightarrow 0} h\left|\cos \frac{\pi}{h}\right| \\

&=0 \times \text { some finite value }=0

\end{aligned}$

$\begin{array}{c}

=0 \times \text { some finite value }=0 \\

\text { and } f^{\prime}\left(0^{-}\right)=\lim _{h \rightarrow 0} \frac{f(0-h)-f(0)}{-h}=\lim _{h \rightarrow 0} \frac{h^{2}\left|\cos \frac{\pi}{-h}\right|}{-h} \\

=\lim _{h \rightarrow 0}-h\left|\cos \frac{\pi}{h}\right|=0 \times \text { some finite value }=0

\end{array}$

$\begin{array}{l}

\because f^{\prime}\left(0^{+}\right)=f^{\prime}\left(0^{-}\right) \therefore f \text { is differentiable at } x=0 \\

\text { Now } f^{\prime}\left(2^{+}\right)=\lim _{h \rightarrow 0} \frac{f(2+h)-f(2)}{h} \\

\quad=\lim _{h \rightarrow 0} \frac{(2+h)^{2}\left|\cos \frac{\pi}{2+h}\right|-4\left|\cos \frac{\pi}{2}\right|}{h}

\end{array}$

$=\lim _{h \rightarrow 0} \frac{(2+h)^{2}\left(\cos \frac{\pi}{2+h}\right)}{h}$

$=\lim _{h \rightarrow 0} \frac{(2+h)^{2}}{h} \sin \left(\frac{\pi}{2}-\frac{\pi}{2+h}\right)$

$=\lim _{h \rightarrow 0} \frac{(2+h)^{2}}{h} \sin \left(\frac{\pi h}{2(2+h)}\right)$

$=\lim _{h \rightarrow 0} \frac{(2+h)^{2}}{h} \times \frac{\sin \left(\frac{\pi h}{2(2+h)}\right)}{\left(\frac{\pi h}{2(2+h)}\right)} \times \frac{\pi h}{2(2+h)}=\pi$

and $f^{\prime}\left(2^{-}\right)=\lim _{h \rightarrow 0} \frac{f(2-h)-f(2)}{-h}$

$=\lim _{h \rightarrow 0} \frac{(2-h)^{2}\left|\cos \left(\frac{\pi}{2-h}\right)\right|-0}{-h}$

$=\lim _{h \rightarrow 0} \frac{-(2-h)^{2} \cos \left(\frac{\pi}{2-h}\right)}{-h}$

$=\lim _{h \rightarrow 0} \frac{(2-h)^{2} \sin \left(\frac{\pi}{2}-\frac{\pi}{2-h}\right)}{h}$

$=\lim _{h \rightarrow 0} \frac{(2-h)^{2}}{h} \times \frac{\sin \left(\frac{-\pi h}{2(2-h)}\right)}{\left(\frac{-\pi h}{2(2-h)}\right)} \times\left(\frac{-\pi h}{2(2-h)}\right)=-\pi$

$\because f^{\prime}\left(2^{+}\right) \neq f^{\prime}\left(2^{-}\right), \therefore f$ is not differentiable at $x=2 .$

</details>

---

