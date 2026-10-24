# JEE Main Mathematics - Continuity and Differentiability

## Topic 2: Differentiability

**Total Questions:** 81

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For the function $f(x) = e^{\sin|x|} - |x|$, $x \in \mathbb{R}$, consider the following statements:
Statement I: $f$ is differentiable for all $x \in \mathbb{R}$.
Statement II: $f$ is increasing in $\left(-\pi, -\dfrac{\pi}{2}\right)$.
In the light of the above statements, choose the correct answer from the options given below:

**Options:**

- **(A)** Both Statement I and Statement II are true
- **(B)** Both Statement I and Statement II are false
- **(C)** Statement I is true but Statement II is false
- **(D)** Statement I is false but Statement II is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Both Statement I and Statement II are true**

**Detailed Solution:**

For Statement I:
The given function is $f(x) = e^{\sin|x|} - |x|$.
For $x > 0$, $f(x) = e^{\sin x} - x$.
Differentiating with respect to $x$, we get:
$f'(x) = e^{\sin x}\cos x - 1$
The right-hand derivative at $x = 0$ is:
$f'(0^+) = e^{\sin 0}\cos 0 - 1 = 1(1) - 1 = 0$

For $x < 0$, $f(x) = e^{\sin(-x)} - (-x) = e^{-\sin x} + x$.
Differentiating with respect to $x$, we get:
$f'(x) = -e^{-\sin x}\cos x + 1$
The left-hand derivative at $x = 0$ is:
$f'(0^-) = -e^{-\sin 0}\cos 0 + 1 = -1(1) + 1 = 0$

Since $f'(0^+) = f'(0^-) = 0$, the function $f(x)$ is differentiable at $x = 0$. For all other $x \in \mathbb{R}$ ($x \neq 0$), the function is a composition of differentiable functions and is therefore differentiable. Thus, Statement I is true.

For Statement II:
We need to check the monotonicity of $f(x)$ in the interval $\left(-\pi, -\dfrac{\pi}{2}\right)$.
Since $x < 0$ in this interval, the derivative is:
$f'(x) = 1 - e^{-\sin x}\cos x$
In the interval $\left(-\pi, -\dfrac{\pi}{2}\right)$ (which lies in the third quadrant), $\cos x < 0$.
Since $e^{-\sin x} > 0$ and $\cos x < 0$, the term $-e^{-\sin x}\cos x > 0$.
Therefore, $f'(x) = 1 - e^{-\sin x}\cos x > 1 > 0$.
Since $f'(x) > 0$, the function $f(x)$ is strictly increasing in $\left(-\pi, -\dfrac{\pi}{2}\right)$. Thus, Statement II is true.

Both Statement I and Statement II are true.

Answer: Both Statement I and Statement II are true

</details>

---

### Q2. JEE Main 2026 (04 April Shift 1)

*Type:* `numerical` | *Level:* `3`

The number of points, at which the function $f(x) = \max\{6x, 2 + 3x^2\} + |x - 1|\left|\cos\left|x^2 - \dfrac{1}{4}\right|\right|$, $x \in (-\pi, \pi)$, is not differentiable, is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

Let $f(x) = g(x) + h(x)$, where
$g(x) = \max\{6x,\ 2 + 3x^2\}$
$h(x) = |x - 1|\left|\cos\left|x^2 - \dfrac{1}{4}\right|\right|$

We find the points of non-differentiability of each part in $x \in (-\pi, \pi)$.

Non-differentiability of $g(x)$:
$g(x) = \max\{6x,\ 2 + 3x^2\}$ is non-differentiable where the two curves intersect with different slopes.

$6x = 2 + 3x^2 \Rightarrow 3x^2 - 6x + 2 = 0$
$x = \dfrac{6 \pm \sqrt{36 - 24}}{6} = \dfrac{6 \pm 2\sqrt{3}}{6} = 1 \pm \dfrac{1}{\sqrt{3}}$

Both values lie in $(-\pi, \pi)$. At these points, the derivatives of the two inner functions are $6$ and $6x$; since $x \neq 1$, the slopes differ.
So $g(x)$ contributes $2$ points.

Non-differentiability of $h(x)$:
Since $\cos|y| = \cos y$:
$h(x) = |x - 1|\left|\cos\left(x^2 - \dfrac{1}{4}\right)\right|$

An expression of the form $|u(x)|$ is non-differentiable at simple zeros of $u(x)$.

Case A: $x - 1 = 0 \Rightarrow x = 1$
At $x = 1$: $\cos\left(1 - \dfrac{1}{4}\right) = \cos\dfrac{3}{4} \neq 0$, so $x = 1$ is a point of non-differentiability.
Contribution: $1$ point.

Case B: $\cos\left(x^2 - \dfrac{1}{4}\right) = 0$
$x^2 - \dfrac{1}{4} = (2n + 1)\dfrac{\pi}{2} \Rightarrow x^2 = \dfrac{1}{4} + (2n + 1)\dfrac{\pi}{2}$

Domain restriction: $x \in (-\pi, \pi) \Rightarrow x^2 \in [0, \pi^2)$, and $\pi^2 \approx 9.87$.

$n = -1$: $x^2 = 0.25 - \dfrac{\pi}{2} < 0$ (rejected)
$n = 0$: $x^2 \approx 1.82 < 9.87$ (gives $2$ points)
$n = 1$: $x^2 \approx 4.96 < 9.87$ (gives $2$ points)
$n = 2$: $x^2 \approx 8.10 < 9.87$ (gives $2$ points)
$n = 3$: $x^2 \approx 11.25 > 9.87$ (rejected)

Contribution: $2 + 2 + 2 = 6$ points.

Checking for overlap:
The points $x = 1 \pm \dfrac{1}{\sqrt{3}}$ are not equal to $1$, and for these, $x^2 - \dfrac{1}{4} = \dfrac{13}{12} \pm \dfrac{2}{\sqrt{3}}$, which are not odd multiples of $\dfrac{\pi}{2}$. So the non-differentiable points of $g(x)$ and $h(x)$ are disjoint.

Total number of points of non-differentiability:
$2 + 1 + 6 = 9$

Hence, the answer is $9$.

</details>

---

### Q3. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha, \beta \in \mathbb{R}$ be such that the function $f(x)= \begin{cases}2 \alpha\left(x^{2}-2\right)+2 \beta x &, x<1 \\ (\alpha+3) x+(\alpha-\beta) &, x \geq 1\end{cases}$ 
 be differentiable at all $x \in \mathbb{R}$. Then $34(\alpha+\beta)$ is equal to

**Options:**

- **(A)** 36
- **(B)** 24
- **(C)** 84
- **(D)** 48

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 48**

**Detailed Solution:**

$f(x) = \begin{cases} 2\alpha x^2 + 2\beta x - 4\alpha & ; \quad x < 1 \\ (\alpha + 3)x + \alpha - \beta & ; \quad x \geq 1 \end{cases}$
$f(1^-) = 2\alpha - \beta + 3$, $f(1) = -2\alpha + 2\beta$
$2\alpha - \beta + 3 = 2\beta - 2\alpha \Rightarrow 4\alpha - 3\beta + 3 = 0$ ...(1)
$f'(1^+) = 4\alpha + 2\beta$, $f'(1^-) = \alpha + 3$
$4\alpha + 2\beta = \alpha + 3 \Rightarrow 3\alpha + 2\beta - 3 = 0$ ...(2)
Solving (1) & (2)
We get $\alpha = \dfrac{3}{17}$, $\beta = \dfrac{21}{17}$
$\Rightarrow 34(\alpha + \beta) = 34 \times \dfrac{27}{17} = 48$

</details>

---

### Q4. JEE Main 2025 (4 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

Let $m$ and $n$ be the number of points at which the function $f(\mathrm{x})=\max \left\{\mathrm{x}, \mathrm{x}^3, \mathrm{x}^5, \ldots ., \mathrm{x}^{21}\right\}, \mathrm{x} \in \mathbb{R}$, is not differentiable and not continuous, respectively. Then $\mathrm{m}+\mathrm{n}$ is equal to ________ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

$f(x)=\left\{\begin{array}{cc}
x, & x \lt -1 \\
x^{21}, & -1 \leq x \lt 0 \\
x, & 0 \leq x \lt 1 \\
x^{21}, & x \geq 1
\end{array}\right.$
$f(x)$ is continuous everywhere.
$\begin{aligned}
& \therefore \mathrm{n}=0 \\
& \mathrm{f}^{\prime}(\mathrm{x})=\left\{\begin{array}{cc}
1, & \mathrm{x} \lt -1 \\
21 \mathrm{x}^{20}, & -1 \leq \mathrm{x} \lt 0 \\
1, & 0 \lt \mathrm{x} \lt 1 \\
21 \mathrm{x}^{20}, & \mathrm{x} \geq 1
\end{array}\right.
\end{aligned}$
$\therefore \mathrm{f}(\mathrm{x})$ is non-differentiable at $\mathrm{x}=-1,0,1$
$\begin{aligned}
& \therefore \mathrm{m}=3 \\
& \mathrm{~m}+\mathrm{n}=3
\end{aligned}$

</details>

---

### Q5. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let the function $f(x)=\left(x^2+1\right)\left|x^2-a x+2\right|+\cos |x|$ be not differentiable at the two points $x=\alpha=2$ and $x=\beta$. Then the distance of the point $(\alpha, \beta)$ from the line $12 x+5 y+10=0$ is equal to :

**Options:**

- **(A)** 5
- **(B)** 4
- **(C)** 3
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

$f(x)=\left(x^2+1\right)\left|x^2-a x+2\right|+\cos |x|$

Notice that $\cos (-x)=\cos x=\cos |x|$ which means $\cos |x|$ is differentiable
everywhere in $x \in R$
$\begin{aligned}
& \Rightarrow f(x) \text { can be non differentiable where }\left|x^2-a x+2\right| \\
& =0
\end{aligned}$
$\Rightarrow x^2-a x+2=0$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/J81bsNezDBmjuu9xkLrPJ_2cfOo9GqqgDXoHpc-FJdI.original.fullsize.png">

$\Rightarrow 4-2 a+2=0 \Rightarrow a=3$
$\Rightarrow \quad\left(x^2-3 x+2\right)=0 \quad \Rightarrow \quad x=1,2$
$\beta=1$
distance of $(\alpha, \beta)$ from line
$\begin{aligned}
& 12 x+5 y+10=0 \\
& \Rightarrow \frac{|2(12)+5(1)+10|}{13}=\frac{39}{13}=3
\end{aligned}$

</details>

---

### Q6. JEE Main 2025 (28 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $\mathrm{f}(x)=\left\{\begin{array}{lc}3 x, & x \lt 0 \\ \min \{1+x+[x], x+2[x]\}, & 0 \leq x \leq 2 \\ 5, & x\gt2,\end{array}\right.$
where [.] denotes greatest integer function. If $\alpha$ and $\beta$ are the number of points, where f is not continuous and is not differentiable, respectively, then $\alpha+\beta$ equals __________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$f(x)=\left\{\begin{array}{ccc}3 x & ; & x < 0 \\ \min \{1+x, x\} & ; & 0 \leq x < 1 \\ \min \{2+x, x+2\} & ; & 1 \leq x < 2 \\ 5 & ; & x>2\end{array}\right.$


$f(x)=\left\{\begin{array}{ccc}3 x & ; & x < 0 \\ x & ; & 0 \leq x < 1 \\ x+2 & ; & 1 \leq x < 2 \\ 5 & ; & x>2\end{array}\right.$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/yFhkl0cGiD9nzQDlf2924dqpIXbTDW8o2p9T1HcmV3U.original.fullsize.png">




Not continuous at $\mathrm{x} \in\{1,2\} \Rightarrow \alpha=2$
Not diff. at $x \in\{0,1,2\} \Rightarrow \beta=3$ $\alpha+\beta=5$

</details>

---

### Q7. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $[x]$ denote the greatest integer function, and let m and n respectively be the numbers of the points, where the function $f(x)=[x]+|x-2|,-2 \lt x \lt 3$, is not continuous and not differentiable. Then $\mathrm{m}+\mathrm{n}$ is equal to :

**Options:**

- **(A)** 6
- **(B)** 8
- **(C)** 9
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 8**

**Detailed Solution:**

$\begin{aligned}
& f(x)=[x]+|x-2|,-2 < x < 3 \\
& \therefore f(x)=\left\{\begin{array}{l}
-x,-2 < x < -1 \\
1-x,-1 \leq x < 0 \\
2-x, 0 \leq x < 1 \\
3-x, 1 \leq x < 2 \\
x, 2 \leq x < 3
\end{array}\right.
\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5K_XhL9qqwvZMjVbmbQCViT-bnkWlXG8yBSqjJbI4hs.original.fullsize.png">

It is clearly discontinues at 4 points and nondifferentiable at 4 points.
$\therefore \quad m+n=8$

</details>

---

### Q8. JEE Main 2025 (22 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let the function,
$f(x)= \begin{cases}-3 a x^2-2, & x \lt 1 \\ a^2+b x, & x \geqslant 1\end{cases}$
be differentiable for all $x \in \mathbf{R}$, where $\mathbf{a}\gt1, \mathbf{b} \in \mathbf{R}$. If the area of the region enclosed by $y=f(x)$ and the line $y=-20$ is $\alpha+\beta \sqrt{3}, \alpha, \beta \in Z$, then the value of $\alpha+\beta$ is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **34**

**Detailed Solution:**

$f(x)$ is continuous and differentiable
$\begin{aligned}
& \text { at } x=1, \mathrm{LHL}=\mathrm{RHL}, \mathrm{LHD}=\mathrm{RHD} \\
& -3 a-2=a^2+b,-6 a=b \\
& a=2 ; b=-12 \\
& f(x)=\left\{\begin{array}{cc}
-6 x^2-2, & x < 1 \\
4-12 x, & x \geq 1
\end{array}\right.
\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cH2y87Qs33gJnKyjgjIsHWd143usH7znLTX-mL0kNuE.original.fullsize.png">

$\begin{aligned} & \left.\text { Area }=\int_{-\sqrt{3}}^1\left(-6 x^2-2+20\right) d x+\int_1^2(4-12 x+20) d x\right] \\ & =16+12 \sqrt{3}+6=22+12 \sqrt{3} \\ & \therefore \quad \alpha+\beta=34\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)$ be a real differentiable function such that $f(0)=1$ and $f(x+y)=f(x) f^{\prime}(y)+f^{\prime}(x) f(y)$ for all $x, y \in \mathbf{R}$. Then $\sum_{\mathrm{n}=1}^{100} \log _{\mathrm{e}} f(\mathrm{n})$ is equal to :

**Options:**

- **(A)** $2525$
- **(B)** $5220$
- **(C)** $2384$
- **(D)** $2406$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2525$**

**Detailed Solution:**

$\because f(x+y)=f(x) \cdot f(y)+f(x) \cdot f(y), \forall x, y \in R$ ....(i)
And $f(0)=1$   ....(ii)
Now replace $x$ by zero and $y$ by zero we get
$\begin{aligned}
& f(0)=f(0) f(0)+f(0) f(0) \\
& 1=f(0)+f(0) \\
& \therefore \quad f^{\prime}(0)=\frac{1}{2} ...(iii)
\end{aligned}$
Now replace $y$ by zero in equation (i), we get
$f(x)=\frac{1}{2} f(x)+f^{\prime}(x)$
or, $\frac{1}{2} f(x)=f^{\prime}(x)$
then $\frac{f^{\prime}(x)}{f(x)}=\frac{1}{2}$
hence $\ln |f(x)|=\frac{x}{2}+c$
Put $x=0$, we get $c=0$
$\therefore \quad \ln |f(x)|=\frac{x}{2}$
Then $\sum_{n=1}^{100} \ln (f(\eta))=\left(\frac{1}{2}+\frac{2}{2}+\frac{3}{2}+\ldots+\frac{100}{2}\right)$
$=\frac{5050}{2}=2525$

</details>

---

### Q10. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>-</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>x</mi><mo>∈</mo><mi>R</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> denote the number of points where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not continuous and not differentiable respectively, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>−</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>-</mo><mi>x</mi><mo>−</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfenced></math></p><p>Graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfenced></math> is given below:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/da42c516-3a6c-4709-a25d-3d48e1d0094a.png" style="width: 280px; height: 143px;"/></p><p>Graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>-</mo><mn>3</mn></mrow></mfenced></math> is given below:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b79187f6-a2ae-4556-aea3-e8308d46215a.png" style="width: 280px; height: 261px;"/></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mi>R</mi></math> and non-differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>±</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>0</mn></math></p><p>So, number of points of discontinuity<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>=</mo><mi>m</mi></math></p><p>Also, number of points of non-discontinuity<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>=</mo><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q11. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>→</mo><mi>R</mi></math> be defined as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mfrac><mrow><mi>a</mi><mo>−</mo><mi>b</mi><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>;</mo><mi>x</mi><mo>&lt;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>c</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>;</mo><mn>0</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>;</mo><mi>x</mi><mo>&gt;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous everywhere in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is the number of points where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is NOT differential then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo> </mo><mo>+</mo><mo> </mo><mi>a</mi><mo> </mo><mo>+</mo><mo> </mo><mi>b</mi><mo> </mo><mo>+</mo><mo> </mo><mi>c</mi></math> equals:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><msup><mn>1</mn><mo>−</mo></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mn>1</mn><mo>+</mo></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn><mo>+</mo><mi>c</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><msup><mn>1</mn><mo>+</mo></msup></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mi>h</mi></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><msup><mn>1</mn><mo>+</mo></msup></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mn>3</mn><mo>+</mo><mn>2</mn><mi>h</mi><mo>=</mo><mn>3</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><msup><mn>0</mn><mo>−</mo></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced><mo>=</mo><mn>2</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>0</mn><mo>−</mo></msup></mfenced></math> has to be equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><mo>−</mo><mi>b</mi><mi>cos</mi><mfenced><mrow><mn>2</mn><mi>h</mi></mrow></mfenced></mrow><msup><mi>h</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><mo>−</mo><mi>b</mi><mfenced close="}" open="{"><mrow><mn>1</mn><mo>−</mo><mfrac><mrow><mn>4</mn><msup><mi>h</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>16</mn><msup><mi>h</mi><mn>4</mn></msup></mrow><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>.</mo><mo>..</mo></mrow></mfenced></mrow><msup><mi>h</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><mo>−</mo><mi>b</mi><mo>+</mo><mi>b</mi><mfenced close="}" open="{"><mrow><mn>2</mn><msup><mi>h</mi><mn>2</mn></msup><mo>−</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>h</mi><mn>4</mn></msup><mo>.</mo><mo>..</mo></mrow></mfenced></mrow><msup><mi>h</mi><mn>2</mn></msup></mfrac></math></p><p>For limit to exist <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>−</mo><mi>b</mi><mo>=</mo><mn>0</mn></math> and limit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>b</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>v</mi></mfenced></math></p><p>Using, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mi>v</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mi>b</mi><mo>=</mo><mn>1</mn></math></p><p>Checking differentiability at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>L</mi><mi>H</mi><mi>D</mi><mo>:</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfrac><mrow><mn>1</mn><mo>−</mo><mi>cos</mi><mn>2</mn><mi>h</mi></mrow><msup><mi>h</mi><mn>2</mn></msup></mfrac><mo>−</mo><mn>2</mn></mrow><mrow><mo>−</mo><mi>h</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>1</mn><mo>−</mo><mfenced><mrow><mn>1</mn><mo>−</mo><mfrac><mrow><mn>4</mn><msup><mi>h</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>16</mn><msup><mi>h</mi><mn>4</mn></msup></mrow><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mo>.</mo><mo>..</mo></mrow></mfenced><mo>−</mo><mn>2</mn><msup><mi>h</mi><mn>2</mn></msup></mrow><mrow><mo>−</mo><msup><mi>h</mi><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>R</mi><mi>H</mi><mi>D</mi><mo>:</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mfenced><mrow><mn>0</mn><mo>+</mo><mi>h</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>−</mo><mn>2</mn></mrow><mi>h</mi></mfrac><mo>=</mo><mn>0</mn></math></p><p>Function is differentiable at every point in its domain</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi>m</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>m</mi><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>m</mi><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q12. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Consider the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>∞</mi></mrow></mfenced><mo>→</mo><mi>R</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>−</mo><mfenced close="|" open="|"><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced></mrow></msup></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> be respectively the number of points at which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not continuous and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not differentiable, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>log</mi><mi>x</mi></mrow></mfenced></math> is continuous in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>∞</mo></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>log</mi><mfenced close="|" open="|"><mi>x</mi></mfenced></mrow></msup></math> is continuous in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>∞</mo></mrow></mfenced></math></p><p>Thus, the number of points where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is discontinuous is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>m</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left left"><mtr><mtd><msup><mi>e</mi><mrow><mi>log</mi><mi>x</mi></mrow></msup><mo>,</mo></mtd><mtd><mn>0</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>1</mn></mtd></mtr><mtr><mtd><msup><mi>e</mi><mrow><mo>-</mo><mi>log</mi><mi>x</mi></mrow></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>≥</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left left"><mtr><mtd><mi>x</mi><mo>,</mo></mtd><mtd><mn>0</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>≥</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left left"><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mn>0</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>≥</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><msup><mn>1</mn><mo>-</mo></msup></mfenced><mo>=</mo><mn>1</mn><mo> </mo><mo>&amp;</mo><mo> </mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><msup><mn>1</mn><mo>+</mo></msup></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>So, the number of points where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is non-differentiable is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q13. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> be a linear function and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>,</mo></mtd><mtd><mi>x</mi><mo>≤</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&gt;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>, is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mo>−</mo><mn>1</mn></mrow></mfenced></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>3</mn></mfenced></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>4</mn><mrow><mn>9</mn><msup><mi>e</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup></mrow></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>4</mn><mn>9</mn></mfrac></mfenced><mo>+</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>4</mn><mn>9</mn></mfrac></mfenced><mo>−</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>4</mn><mrow><mn>9</mn><msup><mi>e</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup></mrow></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>4</mn><mrow><mn>9</mn><msup><mi>e</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup></mrow></mfrac></mfenced></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></math></p><p>Now function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> in continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><msup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></msup><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>0</mn><mo>=</mo><mi>b</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><mi>x</mi></math></p><p>Now, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&gt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>log</mi><msup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>log</mi><mfenced><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfrac><mo>×</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mstyle></mfenced><mo>-</mo><mfenced close="]" open="["><mrow><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>log</mi><mfenced><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mfenced close="}" open="{"><mfrac><mrow><mi>x</mi><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mstyle></mfenced><mo>-</mo><mfenced close="]" open="["><mrow><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>log</mi><mfenced><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mfenced close="}" open="{"><mfrac><mrow><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></mfenced><mo>-</mo><mfenced close="]" open="["><mrow><mi>log</mi><mfenced><mn>2</mn></mfenced><mo>-</mo><mi>log</mi><mfenced><mn>3</mn></mfenced></mrow></mfenced></mrow><msup><mn>1</mn><mn>2</mn></msup></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced close="}" open="{"><mrow><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>-</mo><mi>log</mi><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced></mrow></mfenced></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>−</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>g</mi><mfenced><mrow><mo>−</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>−</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>log</mi><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mo>−</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math></p><p>Now,  finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>3</mn><mi>a</mi><mo>+</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>2</mn><mi>log</mi><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mo>−</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mi>log</mi><mfenced><mfrac><mn>4</mn><mrow><mn>9</mn><mo>⋅</mo><msup><mi>e</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup></mrow></mfrac></mfenced></math></p>

</details>

---

### Q14. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>-</mo><mo>{</mo><mn>0</mn><mo>}</mo><mo>→</mo><mi>R</mi></math> be a function satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mi>x</mi><mi>y</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mrow><mi>f</mi><mo>(</mo><mi>y</mi><mo>)</mo></mrow></mfrac></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mi>f</mi><mo>(</mo><mi>y</mi><mo>)</mo><mo>≠</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>2024</mn></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>2024</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>2024</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2024</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><mn>2023</mn><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>2024</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mi>x</mi><mi>y</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mi>y</mi></mfenced></mrow></mfrac></math></p><p>And we know that, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mi>x</mi><mi>y</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mi>y</mi></mfenced></mrow></mfrac></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mi>n</mi></msup></math>.</p><p>So, differentiating the function we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>n</mi><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math> and given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2024</mn></math>.</p><p>Hence, on comparing we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>2024</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>×</mo><mn>2024</mn><msup><mi>x</mi><mn>2023</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2024</mn><msup><mi>x</mi><mn>2024</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>2024</mn><msup><mi>x</mi><mn>2024</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>2024</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p></blockquote>

</details>

---

### Q15. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">b</mi></math> be real constants such that the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>a</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>≤</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>b</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&gt;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> be differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>. Then, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math> equals

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>**

**Detailed Solution:**

<blockquote><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left left"><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>a</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>≤</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>b</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&gt;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now, for function to be continuous,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mn>1</mn></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>×</mo><mn>1</mn><mo>+</mo><mi>a</mi><mo>=</mo><mi>b</mi><mo>×</mo><mn>1</mn><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mo>+</mo><mi>a</mi><mo>=</mo><mi>b</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Now, differentiating and putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>3</mn><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>b</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>1</mn></msubsup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>∫</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mi>b</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>1</mn></msubsup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>∫</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>2</mn></mrow><mn>1</mn></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>8</mn></mrow><mn>3</mn></mfrac><mo>+</mo><mn>6</mn><mo>-</mo><mn>6</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mfrac><mrow><mn>5</mn><mo>×</mo><mn>4</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mo>×</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mn>3</mn><mo>+</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>14</mn><mo>-</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>15</mn><mn>2</mn></mfrac><mo>+</mo><mn>14</mn><mo>-</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msubsup><mo>∫</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>17</mn></math></p></blockquote>

</details>

---

### Q16. JEE Main 2024 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mn>1</mn><mrow><mo>|</mo><mi>x</mi><mo>|</mo></mrow></mfrac><mo>,</mo></mtd><mtd><mo>|</mo><mi>x</mi><mo>|</mo><mo>≥</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>b</mi><mo>,</mo></mtd><mtd><mo>|</mo><mi>x</mi><mo>|</mo><mo>&lt;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math> is differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>)</mo></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **15**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>,</mo><mo> </mo><mi>x</mi><mo>≥</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo> </mo><mi>b</mi><mo>,</mo><mo> </mo><mo>-</mo><mn>2</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>,</mo><mo> </mo><mi>x</mi><mo>≤</mo><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>Also given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math></p><p>So, finding LHD and RHD at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>2</mn><mi>a</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mn>4</mn><mi mathvariant="normal">a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">a</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>16</mn></mfrac></math></p><p>Now, for function to be continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mn>4</mn><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><mn>16</mn></mfrac><mo>+</mo><mn>2</mn><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>b</mi><mo>=</mo><mfrac><mn>3</mn><mn>8</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>48</mn><mfenced><mrow><mfrac><mn>3</mn><mn>8</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>16</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>48</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>48</mn><mfenced><mfrac><mn>5</mn><mn>16</mn></mfrac></mfenced><mo>=</mo><mn>15</mn></math></p>

</details>

---

### Q17. JEE Main 2024 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><munder><mi>lim</mi><mrow><mi>r</mi><mo>→</mo><mi>x</mi></mrow></munder><mfenced close="}" open="{"><mrow><mfrac><mrow><mn>2</mn><msup><mi>r</mi><mn>2</mn></msup><mfenced close="]" open="["><mrow><mo>(</mo><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo></mrow></mfenced></mrow><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>-</mo><msup><mi>r</mi><mn>3</mn></msup><msup><mi>e</mi><mfrac><mrow><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo></mrow><mi>r</mi></mfrac></msup></mrow></mfenced></msqrt></math> be differentiable in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mn>0</mn><mo>)</mo><mo>∪</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>∞</mo><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>e</mi></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>a</mi><mo>)</mo><mo>=</mo><mn>0</mn></math>, is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>f</mi><mo>(</mo><mi>a</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><munder><mi>lim</mi><mrow><mi>r</mi><mo>→</mo><mi>x</mi></mrow></munder><mfenced close="}" open="{"><mrow><mfrac><mrow><mn>2</mn><msup><mi>r</mi><mn>2</mn></msup><mfenced close="]" open="["><mrow><mo>(</mo><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo></mrow></mfenced></mrow><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>-</mo><msup><mi>r</mi><mn>3</mn></msup><msup><mi>e</mi><mfrac><mrow><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo></mrow><mi>r</mi></mfrac></msup></mrow></mfenced></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mn>2</mn></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><munder><mi>lim</mi><mrow><mi>r</mi><mo>→</mo><mi>x</mi></mrow></munder><mfenced><mrow><mfrac><mrow><mn>2</mn><msup><mi>r</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>f</mi><mn>2</mn></msup><mo>(</mo><mi>r</mi><mo>)</mo><mo>-</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo></mrow></mfenced></mrow><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>-</mo><msup><mi>r</mi><mn>3</mn></msup><msup><mi>e</mi><mfrac><mrow><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo></mrow><mi>r</mi></mfrac></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mn>2</mn></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><munder><mi>lim</mi><mrow><mi>r</mi><mo>→</mo><mi>x</mi></mrow></munder><mfenced><mrow><mfrac><mrow><mn>2</mn><msup><mi>r</mi><mn>2</mn></msup><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo></mrow><mrow><mi>r</mi><mo>+</mo><mi>x</mi></mrow></mfrac><mfrac><mrow><mo>(</mo><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo><mo>-</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo></mrow><mrow><mi>r</mi><mo>-</mo><mi>x</mi></mrow></mfrac><mo>-</mo><msup><mi>r</mi><mn>3</mn></msup><msup><mi>e</mi><mfrac><mrow><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo></mrow><mi>r</mi></mfrac></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mn>2</mn></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mrow><mi>x</mi><mo>+</mo><mi>x</mi></mrow></mfrac><mfenced><mrow><munder><mi>lim</mi><mrow><mi>r</mi><mo>→</mo><mi>x</mi></mrow></munder><mfrac><mrow><mo>(</mo><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo><mo>-</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo></mrow><mrow><mi>r</mi><mo>-</mo><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup><msup><mi>e</mi><mfrac><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mi>x</mi></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mn>2</mn></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup><msup><mi>e</mi><mfrac><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mi>x</mi></mfrac></msup></math></p><p>Now, taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>y</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>x</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup><msup><mi>e</mi><mfrac><mi>y</mi><mi>x</mi></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi></mfrac><msup><mi>e</mi><mfrac><mi>y</mi><mi>x</mi></mfrac></msup></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>v</mi><mi>x</mi><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>v</mi><mo>=</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mi>x</mi><mi>v</mi></mfrac><msup><mi>e</mi><mi>v</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><msup><mi>e</mi><mi>v</mi></msup><mi>v</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>v</mi></mrow></msup><mi>v</mi><mi>d</mi><mi>v</mi><mo>=</mo><mi>d</mi><mi>x</mi></math></p><p>Integrating both side</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>v</mi></msup><mo>(</mo><mi>x</mi><mo>+</mo><mi>c</mi><mo>)</mo><mo>+</mo><mn>1</mn><mo>+</mo><mi>v</mi><mo>=</mo><mn>0</mn></math></p><p>Now using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mi>e</mi></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>v</mi></msup><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mi>e</mi></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mo>+</mo><mi>v</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>e</mi><mfrac><mi>y</mi><mi>x</mi></mfrac></msup><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mi>e</mi></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mo>+</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>=</mo><mn>0</mn></math></p><p>Now taking, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>a</mi><mo> </mo><mo>&amp;</mo><mo> </mo><mi>y</mi><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>0</mn></msup><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mi>e</mi></mfrac><mo>+</mo><mi>a</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mo>+</mo><mn>0</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mfrac><mn>2</mn><mi>e</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mi>e</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q18. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Consider the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>:</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>2</mn><mo>)</mo><mo>→</mo><mi mathvariant="normal">R</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><mfrac><mi mathvariant="normal">x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mi mathvariant="normal">x</mi></mfrac></math> and the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mtext>min</mtext><mo>{</mo><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">t</mi><mo>)</mo><mo>}</mo><mo>,</mo></mtd><mtd><mn>0</mn><mo>&lt;</mo><mi mathvariant="normal">t</mi><mo>≤</mo><mi mathvariant="normal">x</mi><mtext> and </mtext><mn>0</mn><mo>&lt;</mo><mi mathvariant="normal">x</mi><mo>≤</mo><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mi mathvariant="normal">x</mi><mo>,</mo></mtd><mtd><mn>1</mn><mo>&lt;</mo><mi mathvariant="normal">x</mi><mo>&lt;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math>. Then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi></math> is continuous but not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi></math> is not continuous for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>∈</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi></math> is neither continuous nor differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi></math> is continuous and differentiable for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>∈</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi></math> is continuous but not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>:</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>2</mn><mo>)</mo><mo>→</mo><mi mathvariant="normal">R</mi><mo>;</mo><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><mfrac><mi mathvariant="normal">x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mi mathvariant="normal">x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>2</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow><mrow><mn>2</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></math> is decreasing in domain <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6d1d452d-21f6-4392-b5d7-bdf699a69082.png" style="width: 300px; height: 223px;"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfrac><mi mathvariant="normal">x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mi mathvariant="normal">x</mi></mfrac><mo> </mo><mo> </mo><mo> </mo><mn>0</mn><mo>&lt;</mo><mi mathvariant="normal">x</mi><mo>≤</mo><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mi mathvariant="normal">x</mi><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mn>1</mn><mo>&lt;</mo><mi mathvariant="normal">x</mi><mo>&lt;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>1</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">g</mi><mfenced><msup><mn>1</mn><mo>+</mo></msup></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></math> is continuous in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">g</mi><mo>'</mo></msup><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>,</mo><mo> </mo><mn>0</mn><mo>&lt;</mo><mi mathvariant="normal">x</mi><mo>≤</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mn>1</mn><mo>&lt;</mo><mi mathvariant="normal">x</mi><mo>&lt;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>≠</mo><msup><mi mathvariant="normal">g</mi><mo>'</mo></msup><mfenced><msup><mn>1</mn><mo>+</mo></msup></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></math> is not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6fd6b6b8-f4b8-4c2c-af3f-e200e490e61a.png" style="width: 300px; height: 257px;"/></p>

</details>

---

### Q19. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denote the greatest integer function and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>max</mi><mfenced open="{" close="}"><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>+</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mfenced open="[" close="]"><mi>x</mi></mfenced></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not continuous and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> be the number of points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not differentiable. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>max</mi><mfenced close="}" open="{"><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>+</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left left"><mtr><mtd><mi>max</mi><mfenced close="}" open="{"><mrow><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi></mrow></mfenced></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>max</mi><mfenced close="}" open="{"><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mtd><mtd><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>max</mi><mfenced close="}" open="{"><mrow><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced></mtd><mtd><mi>x</mi><mo>=</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo></mtd><mtd><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>6</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mi>x</mi><mo>=</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>2</mn><mo>-</mo></msup></mfenced><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>6</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is differentiable in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn></math> is a linear function,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>m</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>3</mn></math></p><p>Hence this is the required option.</p></blockquote>

</details>

---

### Q20. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> be two functions defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>.Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>g</mi><mi>o</mi><mi>f</mi></mrow></mfenced><mfenced><mi>x</mi></mfenced></math> is

**Options:**

- **(A)** Continuous everywhere but not differentiable exactly at one point
- **(B)** Continuous everywhere but not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>
- **(C)** Differentiable everywhere
- **(D)** Not continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Continuous everywhere but not differentiable exactly at one point**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mrow><mtable columnalign="left center"><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>-</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>1</mn></mtd></mtr></mtable><mo>&#38;</mo><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></mrow></mfenced></math>
     </p><p>Now, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>o</mi><mi>f</mi><mfenced><mi>x</mi></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>g</mi><mi>o</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>,</mo></mtd><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>g</mi><mi>o</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now plotting the diagram we get,
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c0062bd7-4730-4705-a3bd-6a3140876343.png" style="width: 250px; height: 156px;" />
Now from above diagram we can say that function is continuous but not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> due to sharp corner.</p>

</details>

---

### Q21. JEE Main 2023 (10 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>&#8594;</mo><mi>&#8477;</mi></math> be defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mi>x</mi><mfenced close="]" open="["><mi>x</mi></mfenced></mtd><mtd><mo>,</mo></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced close="]" open="["><mi>x</mi></mfenced></mtd><mtd><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denotes the greatest integer function. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> respectively are the number of points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8211;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> at which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is not continuous and not differentiable, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi></math> is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>&#8594;</mo><mi>&#8477;</mi></math> be defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mi>x</mi><mfenced close="]" open="["><mi>x</mi></mfenced></mtd><mtd><mo>,</mo></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced close="]" open="["><mi>x</mi></mfenced></mtd><mtd><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mtable><mtr><mtd><mo>-</mo><mn>2</mn><mi>x</mi><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr></mtable></mtd></mtr><mtr><mtd><mtable><mtr><mtd><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced></math></p><p>Now plotting the diagram of the above function we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f15fb658-5a5c-4c31-bee1-0fbf199bafc7.png" style="width: 350px; height: 232px;" /></p><p>Now from above diagram we can say that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is same as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p>Hence, the function is not continuous at one point and non differentiable at three points, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>4</mn></math></p></blockquote>

</details>

---

### Q22. JEE Main 2023 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> be positive real numbers such that the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>k</mi><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>m</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> is differentiable for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>8</mn><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mn>8</mn><mo>)</mo></mrow><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mn>1</mn><mn>8</mn></mfrac></mfenced></mrow></mfrac></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **309**

**Detailed Solution:**

<blockquote><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>k</mi><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>;</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>m</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> is differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>, so function must be continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>, hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHL</mi><mo>=</mo><mi>RHL</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mi>k</mi><msqrt><mn>2</mn></msqrt><mo>=</mo><mi>m</mi><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mi>k</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>m</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>6</mn><mi>x</mi><mo>+</mo><mfrac><mi>k</mi><mrow><mn>2</mn><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac><mo>;</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>m</mi><mi>x</mi><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mn>1</mn><mo>-</mo></msup></mfenced><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mn>1</mn><mo>+</mo></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mo>+</mo><mfrac><mi>k</mi><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mn>2</mn><mi>m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mn>3</mn><mo>+</mo><mfrac><mi>k</mi><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Putting in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mi>k</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>3</mn><mo>+</mo><mfrac><mi>k</mi><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mfrac><mn>1</mn><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced><mi>k</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mfenced><mfrac><mrow><mn>7</mn><msqrt><mn>2</mn></msqrt></mrow><mn>8</mn></mfrac></mfenced><mi>k</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mfenced><mrow><mi>k</mi><mo>-</mo><mfrac><mrow><mn>7</mn><msqrt><mn>2</mn></msqrt></mrow><mn>8</mn></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mrow><mn>7</mn><msqrt><mn>2</mn></msqrt></mrow><mn>8</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mi>k</mi><mrow><mn>12</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>7</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>96</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>103</mn><mn>96</mn></mfrac></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>6</mn><mi>x</mi><mo>+</mo><mfrac><mrow><mn>7</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>16</mn><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac><mo>;</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mrow><mn>103</mn><mi>x</mi></mrow><mn>16</mn></mfrac><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>8</mn></mfenced></mrow><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>8</mn></mfrac></mstyle></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>103</mn><mo>&#215;</mo><mn>8</mn></mrow><mn>16</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mfenced><mrow><mstyle displaystyle="true"><mfrac><mn>6</mn><mn>8</mn></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>7</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>16</mn><msqrt><mstyle displaystyle="true"><mfrac><mn>9</mn><mn>8</mn></mfrac></mstyle></msqrt></mrow></mfrac></mstyle></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>8</mn></mfenced></mrow><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>8</mn></mfrac></mstyle></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>103</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>8</mn><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>8</mn></mfenced></mrow><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>8</mn></mfrac></mstyle></mfenced></mrow></mfrac><mo>=</mo><mn>309</mn></math></p></blockquote>

</details>

---

### Q23. JEE Main 2023 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8484;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>t</mi></mfenced></math> be the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>t</mi></math>, then the number of points, where the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><mrow><mi>a</mi><mo>+</mo><mn>13</mn><mo>&#160;</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math> is not differentiable, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi>a</mi><mo>+</mo><mn>13</mn><mo>&#160;</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mo>[</mo><mn>13</mn><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>]</mo><mo>+</mo><mi>a</mi></math>, as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mtext>Integer</mtext></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>13</mn><mo>&#160;</mo><mi>sinx</mi></math>, now plotting the diagram of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>13</mn><mi>sin</mi><mi>x</mi></math> we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/48e8d165-bbd6-4d68-97b0-8b669c4ea32f-image.png" style="width: 350px; height: 311px;" /></p><p>Now from above diagram we can see that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfenced close="]" open="["><mrow><mn>13</mn><mo>&#160;</mo><mi>sinx</mi></mrow></mfenced></math> is not differentiable at intersection points of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>k</mi><mo>,</mo><mo>&#160;</mo><mi>k</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mn>13</mn><mo>]</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>k</mi><mo>&#8712;</mo><mi>Z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>Points of non-differentiability<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>12</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>25</mn></math></p></blockquote>

</details>

---

### Q24. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> be twice differentiable functions on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> such that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>6</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>4</mn><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>-</mo><mn>3</mn><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>g</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>12</mn></math></p><p>Then which of the following is NOT true ?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>20</mn></math>
- **(B)** If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#60;</mo><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#60;</mo><mn>6</mn><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math>
- **(D)** There exists <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>0</mn></msub><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msub><mi>x</mi><mn>0</mn></msub></mfenced><mo>=</mo><mi>g</mi><mfenced><msub><mi>x</mi><mn>0</mn></msub></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#60;</mo><mn>8</mn></math>**

**Detailed Solution:**

<p>Given functions are:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>6</mn><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>4</mn><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>-</mo><mn>3</mn><mo>=</mo><mn>9</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>g</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>12</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>3</mn></mfenced></math></p><p>By integrating <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, we get
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>C</mi></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>3</mn><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mo>=</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>+</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></math></p><p>Again by integrating, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>D</mi></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mi>g</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mn>8</mn><mo>+</mo><mn>3</mn><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>D</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>12</mn><mo>=</mo><mn>4</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>6</mn><mo>+</mo><mi>D</mi><mo>&#8658;</mo><mi>D</mi><mo>=</mo><mo>-</mo><mn>6</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>6</mn></math></p><p>Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math>:</p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>20</mn><mo>&#160;&#160;</mo></math></p><p>So, this option is true.</p><p>Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>h</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>h</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math> for all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#60;</mo><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mi>h</mi><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>10</mn><mo>&#60;</mo><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>h</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#60;</mo><mn>10</mn></math>     </p><p>So, this option is NOT true.</p><p>Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>C</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>h</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#60;</mo><mn>6</mn><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#60;</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>&#60;</mo><mn>6</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>6</mn><mo>&#60;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>&#62;</mo><mo>-</mo><mn>3</mn><mfenced><mrow><mi>always</mi><mo>&#160;</mo><mi>true</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math>        </p><p>So, If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#60;</mo><mn>6</mn></math></p><p>So, this option is true.</p><p>Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>D</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>6</mn></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mi>ve</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mo>+</mo><mi>ve</mi></math></p><p>So, there exists <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>0</mn></msub><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msub><mi>x</mi><mn>0</mn></msub></mfenced><mo>=</mo><mi>g</mi><mfenced><msub><mi>x</mi><mn>0</mn></msub></mfenced></math> </p><p>So, this option is true.</p>

</details>

---

### Q25. JEE Main 2023 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Suppose f is a function satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">y</mi><mo>)</mo><mo>=</mo><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>+</mo><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">y</mi><mo>)</mo></math> for  all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>,</mo><mi mathvariant="normal">y</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mi>m</mi></munderover><mfrac><mrow><mi>f</mi><mo>(</mo><mi>n</mi><mo>)</mo></mrow><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>n</mi><mo>+</mo><mn>2</mn><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></math></p><p>Now solving the given functional equation by taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>as&#160;</mtext><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></mrow></mfenced></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>&#8658;</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>5</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><mn>5</mn></mfrac></math></p><p>Now solving  <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mi>m</mi></munderover><mfrac><mrow><mi>f</mi><mfenced><mi>n</mi></mfenced></mrow><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mi>m</mi></munderover><mfrac><mstyle displaystyle="true"><mfrac><mi>n</mi><mn>5</mn></mfrac></mstyle><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mi>m</mi></munderover><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mi>m</mi></munderover><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mfenced open="[" close="]"><mrow><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mn>2</mn></mfrac><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mn>3</mn></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mn>3</mn></mfrac><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mn>4</mn></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mn>4</mn></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mfenced open="[" close="]"><mrow><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mn>2</mn></mfrac><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="[" close="]"><mfrac><mstyle displaystyle="true"><mi>m</mi></mstyle><mrow><mn>2</mn><mfenced><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>12</mn><mi>m</mi><mo>=</mo><mn>10</mn><mfenced><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mn>10</mn></math></p>

</details>

---

### Q26. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>, then at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous but not differentiable
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous but <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup></math> is not continuous
- **(C)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup></math> are continuous
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup></math> is continuous but not differentiable

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous but <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup></math> is not continuous**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mi>x</mi><mn>2</mn></msup><mo>&#215;</mo><mfenced close="]" open="["><mrow><mi>number</mi><mo>&#160;</mo><mi>between</mi><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mi>to</mi><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>RHD</mi><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mfrac><mrow><mi>f</mi><mfenced><mrow><mn>0</mn><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></mrow><mi>h</mi></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>RHD</mi><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mfrac><mrow><msup><mi>h</mi><mn>2</mn></msup><mi>sin</mi><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>h</mi></mfrac></mstyle></mfenced><mo>-</mo><mn>0</mn></mrow><mi>h</mi></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>RHD</mi><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mi>h</mi><mi>sin</mi><mfenced><mfrac><mn>1</mn><mi>h</mi></mfrac></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHD</mi><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mn>0</mn><mo>-</mo></msup></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mfrac><mrow><mi>f</mi><mfenced><mrow><mn>0</mn><mo>-</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></mrow><mrow><mo>-</mo><mi>h</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>LHD</mi><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mn>0</mn><mo>-</mo></msup></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mfrac><mrow><mo>-</mo><msup><mi>h</mi><mn>2</mn></msup><mi>sin</mi><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>h</mi></mfrac></mstyle></mfenced><mo>-</mo><mn>0</mn></mrow><mrow><mo>-</mo><mi>h</mi></mrow></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHD</mi><mo>=</mo><mi>RHD</mi><mo>=</mo><mi>finite</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>2</mn><mi>x</mi><mi>sin</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>-</mo><mi>cos</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mn>2</mn><mi>x</mi><mi>sin</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>-</mo><mi>cos</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mn>2</mn><mi>x</mi><mfenced close="}" open="{"><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mfrac><mn>1</mn><msup><mi>x</mi><mn>5</mn></msup></mfrac><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mfrac><mn>1</mn><msup><mi>x</mi><mn>4</mn></msup></mfrac><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mfenced close="}" open="{"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mfrac><mn>1</mn><msup><mi>x</mi><mn>4</mn></msup></mfrac><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mfrac><mn>1</mn><msup><mi>x</mi><mn>4</mn></msup></mfrac><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced></mrow></mfenced></math></p><p>This limit does not exists finitely, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> is discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>.</p>

</details>

---

### Q27. JEE Main 2022 (29 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>t</mi></mfenced></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>t</mi></math>, then number of points, at which the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><mfenced open="|" close="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mfenced open="[" close="]"><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mn>12</mn><mfenced open="[" close="]"><mrow><mi>x</mi><mo>+</mo><mn>20</mn></mrow></mfenced></math> is not differentiable in the open interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>20</mn><mo>,</mo><mn>20</mn></mrow></mfenced></math>, is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **79**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><mfenced close="|" open="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>9</mn><mfenced close="]" open="["><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mn>12</mn><mfenced close="]" open="["><mrow><mi>x</mi><mo>+</mo><mn>20</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>20</mn><mo>,</mo><mn>20</mn></mrow></mfenced></math></p><p>Now we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> is non-differentiable when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>I</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mfenced close="]" open="["><mrow><mi>x</mi><mo>+</mo><mn>20</mn></mrow></mfenced></math> is not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>I</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>19</mn><mo>,</mo><mo>-</mo><mn>18</mn><mo>,</mo><mo>&#8230;</mo><mn>0</mn><mo>,</mo><mo>&#8230;</mo><mn>19</mn></mrow></mfenced><mo>=</mo><mn>39</mn></math></p><p>Now  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mfenced close="]" open="["><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math> is not differentiable when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>I</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So, here also total non-differentiable points are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>39</mn></math></p><p>Now checking modulus function</p><p>We know that modulus function are non-differentiable at point where modulus function is zero,</p><p>So at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math> modulus function is zero</p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math>  at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math> is not continuous and non-differentiable,</p><p>So, number of point of non-differentiability<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>39</mn><mo>+</mo><mn>39</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>79</mn></math></p></blockquote>

</details>

---

### Q28. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The number of points, where the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>sin</mi><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></math>, is NOT differentiable, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>sin</mi><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>sin</mi><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced close="]" open="["><mrow><mi>cos</mi><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>sin</mi><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced></mrow></mfenced></math></p><p>We know that modulus function is not differentiable at values where modulus function is zero</p><p>So, we can say that function is non-differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math>.</p></blockquote>

</details>

---

### Q29. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mo>+</mo><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>-</mo><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>.</p><p>Consider</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced><mo>:</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced><mo>:</mo><mo>&#160;</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>12</mn></math></p><p>Then,</p>

**Options:**

- **(A)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are correct
- **(B)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are wrong
- **(C)** only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> is correct
- **(D)** only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is correct

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is correct**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mo>+</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>-</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mo>-</mo><mi>x</mi></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn></mtd><mtd><mo>,</mo></mtd><mtd><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mtd><mtd><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mn>4</mn></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>,</mo></mtd><mtd><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>4</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> is incorrect.</p></blockquote><blockquote><p>Now  <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mfrac><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mfrac><msup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mn>6</mn></mfrac></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mfrac><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>25</mn><mn>6</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><mn>6</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>18</mn><mo>-</mo><mfrac><mn>25</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>11</mn><mn>2</mn></mfrac><mo>=</mo><mn>12</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is correct.</p><p> </p></blockquote>

</details>

---

### Q30. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be defined as:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnspacing="1.4ex" columnalign="left"><mtr><mtd><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mrow><mn>5</mn><mo>-</mo><mfenced open="|" close="|"><mrow><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>4</mn></mtd></mtr><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math>, then which of the following statements is NOT true?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>3</mn></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>5</mn></mfenced><mo>=</mo><mfrac><mn>35</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> has a local minima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mrow><mn>5</mn><mo>-</mo><mfenced close="|" open="|"><mrow><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>4</mn></mtd></mtr><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p>Also given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>4</mn><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>4</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>4</mn></mfenced></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>+</mo><mn>4</mn><mi>b</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>3</mn></msubsup><mfenced><mrow><mn>2</mn><mo>-</mo><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>3</mn><mn>4</mn></msubsup><mfenced><mrow><mn>8</mn><mo>-</mo><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>16</mn><mo>+</mo><mn>4</mn><mi>b</mi><mo>=</mo><msubsup><mfenced><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mn>0</mn><mn>3</mn></msubsup><mo>+</mo><msubsup><mfenced><mrow><mn>8</mn><mi>t</mi><mo>-</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mn>3</mn><mn>4</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>16</mn><mo>+</mo><mn>4</mn><mi>b</mi><mo>=</mo><mn>15</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></math></p><p>Now differentiating <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><mfenced><mrow><mn>5</mn><mo>-</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mi>b</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p>Now at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHD</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>31</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>RHD</mi><mo>=</mo><mn>5</mn><mo>-</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHD</mi><mo>&#8800;</mo><mi>RHD</mi></math></p><p>So, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> is true</p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>3</mn></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>5</mn></mfenced><mo>=</mo><mfrac><mn>23</mn><mn>4</mn></mfrac><mo>+</mo><mn>3</mn><mo>=</mo><mfrac><mn>35</mn><mn>4</mn></mfrac></math></p><p>So, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> is true</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mi>x</mi><mn>4</mn></mfrac></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8804;</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p>Thus the function is not increasing in the interval in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced></math></p><p>So, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>C</mi></mfenced></math> is NOT TRUE.</p><p>And function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is also have local minima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math> so option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>D</mi></mfenced></math> is also true.</p></blockquote>

</details>

---

### Q31. JEE Main 2022 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mfenced open="|" close="|"><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mi>if</mi><mo>&#160;</mo><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#8805;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced open="[" close="]"><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mi>if</mi><mo>&#160;</mo><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#60;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>&#945;</mi></mfenced></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math>. Then the number of points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not differentiable is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfenced close="|" open="|"><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mi>if</mi><mo>&#160;</mo><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#8805;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced close="]" open="["><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mi>if</mi><mo>&#160;</mo><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#60;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>,</mo></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>&#8722;</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></mtd></mtr><mtr><mtd><mfenced close="]" open="["><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mrow><mtable><mtr><mtd><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>5</mn></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]"><mrow><mo>&#8722;</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mo>&#8722;</mo><msqrt><mn>2</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mfrac><mrow><mn>2</mn><mo>&#8722;</mo><msqrt><mn>2</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></mtd></mtr></mtable><mtable equalcolumns="true" equalrows="true"><mtr></mtr><mtr></mtr><mtr></mtr></mtable></mrow></mfenced></math></p><p>Now plotting the graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/64bf9c97-51c3-4b6e-98e0-32d420433319-image.png" style="width: 390px; height: 249px;" /></p><p>We can see <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> (where<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow><mn>2</mn></mfrac></math>)</p></blockquote>

</details>

---

### Q32. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a function defined by : <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><munder><mi>max</mi><mrow><mi>t</mi><mo>&#8804;</mo><mi>x</mi></mrow></munder><mfenced open="{" close="}"><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>t</mi></mrow></mfenced><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>6</mn><mo>;</mo></mtd><mtd><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mfenced open="[" close="]"><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>9</mn><mo>;</mo></mtd><mtd><mn>3</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>;</mo><mo>&#160;</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>5</mn></mtd></mtr></mtable></mfenced></math>
Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> is the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> be the number of points where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not differentiable and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math>. Then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>m</mi><mo>,</mo><mi>I</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mfrac><mn>27</mn><mn>4</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mfrac><mn>23</mn><mn>4</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mfrac><mn>27</mn><mn>4</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mfrac><mn>23</mn><mn>4</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mfrac><mn>27</mn><mn>4</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>,</mo><mi>x</mi><mo>&#8804;</mo><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>6</mn><mo>,</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>9</mn><mo>,</mo><mn>3</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>10</mn><mo>,</mo><mn>4</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>11</mn><mo>,</mo><mi>x</mi><mo>=</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi>x</mi><mo>&#62;</mo><mn>5</mn></mtd></mtr></mtable></mfenced></math></p><p>Clearly <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msubsup><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></msubsup><mn>2</mn><mo>&#183;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>27</mn><mn>4</mn></mfrac></math></p><p>Hence the ordered pair is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mfrac><mn>27</mn><mn>4</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q33. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>min</mi><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>1</mn><mo>+</mo><mi>x</mi><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>,</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn><mi>&#960;</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is the number of points, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not differentiable and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is the number of points, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not continuous, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>min</mi><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>1</mn><mo>+</mo><mi>x</mi><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>1</mn><mo>,</mo><mo>&#160;&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mi>&#960;</mi></mtd></mtr><mtr><mtd><mn>1</mn><mo>+</mo><mi>x</mi><mi>sin</mi><mi>x</mi><mo>,</mo><mi>&#960;</mi><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn><mi>&#960;</mi></mtd></mtr></mtable></mfenced></math></p><p>Now, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#960;</mi><mo>,</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>&#960;</mi><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>&#960;</mi><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced></math></p><p>So, number of points of discontinuity is zero or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>0</mn></math></p><p>Now, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#960;</mi></math></p><p>L.H.D <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>&#960;</mi></mfenced></mrow><mrow><mo>-</mo><mi>h</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p>R.H.D <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>&#960;</mi></mfenced></mrow><mi>h</mi></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>1</mn><mo>-</mo><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mi>sin</mi><mi>h</mi><mo>-</mo><mn>1</mn></mrow><mi>h</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#960;</mi></math> so, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p>

</details>

---

### Q34. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>,</mo><mi>g</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be two real valued function defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mo>-</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>e</mi><mi>x</mi></msup></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msub><mi>k</mi><mn>1</mn></msub><mi>x</mi></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn><mi>x</mi><mo>+</mo><msub><mi>k</mi><mn>2</mn></msub></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>k</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>k</mi><mn>2</mn></msub></math> are real constants. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>o</mi><mi>f</mi></math> is differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>o</mi><mi>f</mi><mfenced><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mo>+</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>o</mi><mi>f</mi><mfenced><mn>4</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><mrow><msup><mi>e</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mn>2</mn><msup><mi>e</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>e</mi><mn>4</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mn>2</mn><msup><mi>e</mi><mn>4</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mn>2</mn><msup><mi>e</mi><mn>4</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="}" open="{"><mtable columnalign="left"><mtr><mtd><mi>x</mi><mo>+</mo><mn>3</mn></mtd><mtd><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>;</mo></mtd><mtd><mo>-</mo><mn>3</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>e</mi><mi>x</mi></msup></mtd><mtd><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="}" open="{"><mtable columnalign="left"><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msub><mi>k</mi><mn>1</mn></msub><mi>x</mi></mtd><mtd><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn><mi>x</mi><mo>+</mo><msub><mi>k</mi><mn>2</mn></msub></mtd><mtd><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced close="}" open="{"><mtable columnalign="left"><mtr><mtd><mi>f</mi><msup><mfenced><mi>x</mi></mfenced><mn>2</mn></msup><mo>+</mo><msub><mi>k</mi><mn>1</mn></msub><mi>f</mi><mfenced><mi>x</mi></mfenced></mtd><mtd><mo>;</mo></mtd><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msub><mi>k</mi><mn>2</mn></msub></mtd><mtd><mo>;</mo></mtd><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced close="}" open="{"><mtable><mtr><mtd><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msub><mi>k</mi><mn>1</mn></msub><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msub><mi>k</mi><mn>1</mn></msub><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>;</mo></mtd><mtd><mo>-</mo><mn>3</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msub><mi>k</mi><mn>2</mn></msub></mtd><mtd><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>For continuity at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">gof</mo><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><msup><mn>0</mn><mo>-</mo></msup></mfenced></mrow></mfenced><mo>=</mo><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced></mrow></mfenced></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>+</mo><msub><mi>k</mi><mn>2</mn></msub><mo>=</mo><mn>9</mn><mo>-</mo><mn>3</mn><msub><mi>k</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn><mo>+</mo><msub><mi>k</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msub><mi>k</mi><mn>1</mn></msub><mo>+</mo><msub><mi>k</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mi>i</mi></mfenced></math></p><p>Now differentiating, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>&#39;</mo></msup><mo>=</mo><mfenced close="}" open="{"><mtable><mtr><mtd><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><msub><mi>k</mi><mn>1</mn></msub></mtd><mtd><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>-</mo><msub><mi>k</mi><mn>1</mn></msub></mtd><mtd><mo>;</mo></mtd><mtd><mo>-</mo><mn>3</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn><msup><mi>e</mi><mi>x</mi></msup></mtd><mtd><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>-</mo><msub><mi>k</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>k</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi>k</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><msub><mi>k</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mn>1</mn></math> (from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>)</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">gof</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="}" open="{"><mtable><mtr><mtd><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mo>;</mo></mtd><mtd><mo>-</mo><mn>3</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mtd><mtd><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">gof</mo><mfenced><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mo mathvariant="italic">gof</mo><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>4</mn><msup><mi>e</mi><mn>4</mn></msup><mo>-</mo><mn>2</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mn>2</mn><msup><mi>e</mi><mn>4</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q35. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnspacing="1.4ex 1.4ex" columnalign="left left"><mtr><mtd><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></mrow></mfenced></mrow><mrow><mi>x</mi><mo>-</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></mrow></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mi>max</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mo>,</mo><mn>3</mn><mfenced open="[" close="]"><mfenced open="|" close="|"><mi>x</mi></mfenced></mfenced></mrow></mfenced><mo>,</mo></mtd><mtd><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mi>otherwise</mi></mtd></mtr></mtable></mfenced></math>
where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> denotes greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>t</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is the number of points where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not continuous and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is the number of points where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not differentiable, the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left left" columnspacing="1.4ex 1.4ex"><mtr><mtd><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></mfenced></mrow><mrow><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mi>max</mi><mfenced><mrow><mn>2</mn><mi>x</mi><mo>,</mo><mn>3</mn><mfenced close="]" open="["><mfenced close="|" open="|"><mi>x</mi></mfenced></mfenced></mrow></mfenced><mo>,</mo></mtd><mtd><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mi>otherwise</mi></mtd></mtr></mtable></mfenced></math></p><p>On simplifying we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="center left"><mtr><mtd><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mi>max</mi><mfenced close="}" open="{"><mrow><mn>2</mn><mi>x</mi><mo>,</mo><mn>0</mn></mrow></mfenced></mtd><mtd><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>otherwise</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><msup><mn>2</mn><mo>+</mo></msup></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mo>+</mo><mi>h</mi></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mo>+</mo><mi>h</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mo>-</mo><mn>2</mn><mo>+</mo><mi>h</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mi>sinh</mi><mi>h</mi></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>h</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>h</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mfrac><mo>=</mo><mi>sin</mi><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mo>-</mo><msup><mn>1</mn><mo>*</mo></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>1</mn><mo>+</mo></msup></mfenced><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mfenced><msup><mn>1</mn><mo>-</mo></msup></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>f</mi></math> is not continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous but not diff. at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open=""><mtable columnalign="right"><mtr><mtd><mo>&#8658;</mo><mi mathvariant="normal">f</mi><mo>&#160;</mo><mi>is</mi><mo>&#160;</mo><mi>discontinuous</mi><mo>&#160;</mo><mi>at</mi><mo>&#160;</mo><mi mathvariant="normal">x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mo>&#160;</mo><mi>is</mi><mo>&#160;</mo><mi>not</mi><mo>&#160;</mo><mi>diff</mi><mo>.</mo><mo>&#160;</mo><mi>at</mi><mo>&#160;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#8658;</mo><mtable><mtr><mtd><mi>m</mi><mo>=</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>n</mi><mo>=</mo><mn>3</mn></mtd></mtr></mtable></math></p>

</details>

---

### Q36. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#183;</mo><msup><mi mathvariant="normal">e</mi><mrow><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></msup></math> is not differentiable at exactly :

**Options:**

- **(A)** Four points
- **(B)** Two points
- **(C)** three points
- **(D)** one point

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Two points**

**Detailed Solution:**

<p>Given that<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><msup><mi>e</mi><mfenced><mrow><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></msup></math></p><p>Differentiating on both sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>.</mo><msup><mi>e</mi><mfenced><mrow><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></msup><mo>.</mo><mfenced><mrow><mn>18</mn><mi>x</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mfrac><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfrac><mo>.</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>.</mo><msup><mi>e</mi><mfenced><mrow><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>'</mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>.</mo><msup><mi>e</mi><mfenced><mrow><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></msup><mo>&#160;</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mn>18</mn><mi>x</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mo>+</mo><mfrac><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>'</mo><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>.</mo><msup><mi>e</mi><mfenced><mrow><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></msup><mo>.</mo><mfrac><mfenced open="{" close="}"><mrow><mn>18</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>36</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>54</mn><mi>x</mi><mo>-</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>24</mn><mi>x</mi><mo>+</mo><mn>36</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>'</mo><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>.</mo><msup><mi>e</mi><mfenced><mrow><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></msup><mo>.</mo><mfrac><mfenced open="{" close="}"><mrow><mn>18</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>48</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>28</mn><mi>x</mi><mo>+</mo><mn>34</mn></mrow></mfenced><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>'</mo><mfenced><mi>x</mi></mfenced></math> is not defined at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>3</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo></math>is not differentiable at two points.</p><p> </p>

</details>

---

### Q37. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced open="["><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>&#8594;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> be a function defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mi>max</mi><mfenced open="{" close="}"><mrow><mi>sin</mi><mi>t</mi><mo>:</mo><mn>0</mn><mo>&#8804;</mo><mi>t</mi><mo>&#8804;</mo><mi>&#960;</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mi mathvariant="normal">&#960;</mi></mrow></mfenced></mtd></mtr><mtr><mtd><mn>2</mn><mo>+</mo><mi>cos</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mi>&#960;</mi></mtd></mtr></mtable></mfenced></math>. Then which of the following is true ?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous everywhere but not differentiable exactly at one point in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is differentiable everywhere in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not continuous exactly at two points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous everywhere but not differentiable exactly at two points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is differentiable everywhere in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>**

**Detailed Solution:**

<p>Graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>max</mi><mfenced close="}" open="{"><mrow><mi>sin</mi><mi>t</mi><mo>:</mo><mn>0</mn><mo>&#8804;</mo><mi>t</mi><mo>&#8804;</mo><mi>x</mi></mrow></mfenced></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/abb4563a-c619-42f1-ba79-d6cacc1c892a-05545eb3-cdc3-4eae-b4e0-1ca692972787-image.png" style="width: 300px; height: 197px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#38;</mo></math> the graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mo>+</mo><mi>cos</mi><mi>x</mi></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mi>&#960;</mi><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/86b84935-fd96-4bf4-a1b6-0ce1cea41692-d161592b-65a8-4598-8eb8-63d94282451b-image.png" style="width: 300px; height: 240px;" /></p><p>So graph of</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mi>sin</mi><mi>x</mi><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mi mathvariant="normal">&#960;</mi></mtd></mtr><mtr><mtd><mn>2</mn><mo>+</mo><mi>cos</mi><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mi>&#960;</mi></mtd></mtr></mtable></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/05545eb3-cdc3-4eae-b4e0-1ca692972787-image.png" style="width: 305px; height: 200px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is differentiable everywhere in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p>

</details>

---

### Q38. JEE Main 2021 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>min</mi><mfenced close="}" open="{"><mrow><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>,</mo><mn>1</mn><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>x</mi></mfenced></math> is the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>.</mo></math> Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> denote the set containing all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is discontinuous, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> denote the set containing all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not differentiable. Then the sum of number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>min</mi><mfenced open="{" close="}"><mrow><mi>x</mi><mo>-</mo><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>,</mo><mn>1</mn><mo>+</mo><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p>So, the graph of the function is </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/aa4f9dee-c4a5-4336-8b9e-4cd3ab8d6faa-image.png" style="width: 289px; height: 129px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfenced open="{" close="}"><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b92dee34-e409-4a53-9b7f-857722830bbd-image.png" style="width: 325px; height: 130px;" /></p><p>From the graph we can say that the function is continuous at all points in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>.</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mn>0</mn></math></p><p>Again, from the diagram, we can say that at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn><mo>,</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mn>2</mn><mo>,</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>,</mo></math> there are sharp edges.</p><p>So, the function is non differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn><mo>,</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mn>2</mn><mo>,</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mn>5</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>+</mo><mi>Q</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q39. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mrow><mn>5</mn><mo>+</mo><mfenced open="|" close="|"><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>5</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mo>,</mo></math> then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is not continuous at<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is everywhere differentiable
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous but not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous but not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mrow><mn>5</mn><mo>+</mo><mfenced close="|" open="|"><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>5</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>5</mn><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfenced><mrow><mn>5</mn><mo>+</mo><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfenced><mrow><mn>4</mn><mi>t</mi><mo>+</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><msubsup><mo>|</mo><mn>1</mn><mi>x</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>11</mn><mn>2</mn></mfrac><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mn>4</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>2</mn><mo>+</mo></msup></mfenced><mo>=</mo><mn>2</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>11</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mn>2</mn><mo>-</mo></msup></mfenced><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>11</mn></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>2</mn><mo>+</mo></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mn>2</mn><mo>-</mo></msup></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p>Clearly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHD</mi><mo>&#160;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><msup><mn>2</mn><mo>-</mo></msup></mfenced><mo>=</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>RHD</mi><mo>&#160;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><msup><mn>2</mn><mo>+</mo></msup></mfenced><mo>=</mo><mn>6</mn></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q40. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo><mo>&#8594;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced close="]" open="["><mi>y</mi></mfenced><mi>d</mi><mi>y</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> is the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. Which of the following is true?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous at every point in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math> and
differentiable except at the integer points.
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is both continuous and differentiable except at the integer points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>.
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous everywhere except at the integer points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>.
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is differentiable at every point in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous at every point in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math> and
differentiable except at the integer points.**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo><mo>&#8594;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced close="]" open="["><mi>y</mi></mfenced><mi>d</mi><mi>y</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>n</mi><mo>+</mo><mi>f</mi><mo>,</mo><mi>f</mi><mo>&#8712;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>=</mo><mi>n</mi><mo>,</mo><mo>&#160;</mo><mfenced open="{" close="}"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi></math>.</p><p>So</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced open="[" close="]"><mi>y</mi></mfenced><mi>d</mi><mi>y</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced open="[" close="]"><mi>y</mi></mfenced><mi>d</mi><mi>y</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>3</mn></msubsup><mfenced open="[" close="]"><mi>y</mi></mfenced><mi>d</mi><mi>y</mi><mo>+</mo><mspace linebreak="newline"/><mo>&#8230;</mo><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mi>n</mi></msubsup><mfenced open="[" close="]"><mi>y</mi></mfenced><mi>d</mi><mi>y</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mi>n</mi><mrow><mi>n</mi><mo>+</mo><mi>f</mi></mrow></msubsup><mfenced open="[" close="]"><mi>y</mi></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>0</mn><mi>d</mi><mi>y</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mn>1</mn><mi>d</mi><mi>y</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>3</mn></msubsup><mn>2</mn><mi>d</mi><mi>y</mi><mo>+</mo><mspace linebreak="newline"/><mo>&#8230;</mo><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mi>n</mi></msubsup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>y</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mi>n</mi><mrow><mi>n</mi><mo>+</mo><mi>f</mi></mrow></msubsup><mi>n</mi><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mfenced open="[" close="]"><mrow><mn>1</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced open="[" close="]"><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced open="[" close="]"><mrow><mn>3</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mspace linebreak="newline"/><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced open="[" close="]"><mrow><mi>n</mi><mo>-</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>n</mi><mfenced open="[" close="]"><mrow><mi>n</mi><mo>+</mo><mi>f</mi><mo>-</mo><mi>n</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>n</mi><mi>f</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mo>+</mo><mi>n</mi><mi>f</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>[</mo><mi>x</mi><mo>]</mo><mo>(</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mfenced close="}" open="{"><mi>x</mi></mfenced></math></p><p>Note <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>n</mi><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>n</mi><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mfenced><mrow><mi>n</mi><mo>&#8712;</mo><msub><mi>N</mi><mn>0</mn></msub></mrow></mfenced></math></p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is continuous <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8704;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math> and differentiable except at integer.&#39;</p>

</details>

---

### Q41. JEE Main 2021 (22 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a function defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mo>|</mo><mi>x</mi><mo>|</mo></mrow><mn>2</mn></mfrac></mrow></mfenced></mtd><mtd><mtext>if</mtext></mtd><mtd><mo>|</mo><mi>x</mi><mo>|</mo><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mtext>if</mtext></mtd><mtd><mo>|</mo><mi>x</mi><mo>|</mo><mo>&#62;</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mo>.</mo></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>-</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> denote the number of points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is not continuous and not differentiable, respectively, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>+</mo><mi>m</mi></math> is equal to ________.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>The given function is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mo>|</mo><mi>x</mi><mo>|</mo></mrow><mn>2</mn></mfrac></mrow></mfenced></mtd><mtd><mi>i</mi><mi>f</mi></mtd><mtd><mo>|</mo><mi>x</mi><mo>|</mo><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>i</mi><mi>f</mi></mtd><mtd><mo>|</mo><mi>x</mi><mo>|</mo><mo>&#62;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>By using the definition of modulus function, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left left"><mtr><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> and also, we know that if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>&#8804;</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mo>-</mo><mi>a</mi><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mi>a</mi></math> and if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>&#62;</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mi>a</mi><mo>&#160;</mo><mi>o</mi><mi>r</mi><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mi>a</mi><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mn>3</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#62;</mo><mi>x</mi><mo>&#160;</mo><mi>o</mi><mi>r</mi><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>3</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#62;</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>o</mi><mi>r</mi><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>&#62;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>6</mn><mo>-</mo><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>,</mo></mtd><mtd><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#62;</mo><mi>x</mi><mo>&#160;</mo><mi>o</mi><mi>r</mi><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>3</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#8804;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#62;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi>o</mi><mi>r</mi><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#62;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>6</mn><mo>+</mo><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>,</mo></mtd><mtd><mo>-</mo><mn>4</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>,</mo></mtd><mtd><mo>-</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mo>-</mo><mn>4</mn><mo>&#62;</mo><mi>x</mi><mo>&#160;</mo><mi>o</mi><mi>r</mi><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>-</mo><mn>4</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>4</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>4</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></mtd></mtr></mtable></mfenced></math></p><p>The graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is given below</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b64de73f-6986-40f6-99d8-e9bdabc2c92d-image.png" style="width: 329px; height: 304px;" /></p><p>From the graph we can observe that the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is continuous everywhere, hence the number of points where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is not continuos is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>0</mn></math> and the graph has sharp corners at the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math> thus the number of points where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is not differentiable are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>+</mo><mi>m</mi><mo>=</mo><mn>4</mn><mo>.</mo></math></p>

</details>

---

### Q42. JEE Main 2021 (20 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>Let a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be defined as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><munder><mrow><mi>max</mi><mo>&#160;</mo><mfenced close="}" open="{"><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>-</mo><mn>6</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>0</mn><mo>&#8804;</mo><mi>t</mi><mo>&#8804;</mo><mi>x</mi></mrow></munder><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>4</mn><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mn>3</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p>then the number of points in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is NOT differentiable, is _________.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><munder><mrow><mi>max</mi><mo>&#160;</mo><mfenced close="}" open="{"><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>-</mo><mn>6</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>0</mn><mo>&#8804;</mo><mi>t</mi><mo>&#8804;</mo><mi>x</mi></mrow></munder><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>4</mn><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mn>3</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><mi>x</mi><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>3</mn><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>)</mo></math></p><p>For critical points:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>12</mn></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>6</mn><mo>-</mo><mn>12</mn><mo>=</mo><mo>-</mo><mn>6</mn><mo>&#60;</mo><mn>0</mn></math>(maxima)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>6</mn><mo>&#62;</mo><mn>0</mn></math>(minima)</p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="[" close=""><mtable columnalign="right left"><mtr><mtd><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>4</mn><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mn>3</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7c4aca3f-2b56-40e6-b006-ccd2c17177b9-image.png" style="width: 421px; height: 200px;" /></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is continuous function.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="["><mtable><mtr><mtd><mn>3</mn><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn><mo>,</mo></mtd><mtd><mn>3</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p>Clearly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is non-differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math>.</p>

</details>

---

### Q43. JEE Main 2021 (18 Mar Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mi mathvariant="normal">R</mi></math> satisfy the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#183;</mo><mi>f</mi><mo>(</mo><mi>y</mi><mo>)</mo></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mi>y</mi><mo>&#8712;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8800;</mo><mn>0</mn></math> for any <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>. If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>3</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mn>1</mn><mi>h</mi></mfrac><mfenced><mrow><mi>f</mi><mfenced><mi>h</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></math> is equal to ___ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#183;</mo><mi>f</mi><mo>(</mo><mi>y</mi><mo>)</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>3</mn></math> then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>a</mi><mi>x</mi></msup><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>a</mi><mi>x</mi></msup><mo>&#183;</mo><mi>l</mi><mi>n</mi><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>l</mi><mi>n</mi><mi>a</mi><mo>=</mo><mn>3</mn><mo>&#8658;</mo><mi mathvariant="normal">a</mi><mo>=</mo><msup><mi mathvariant="normal">e</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><msup><mi>e</mi><mn>3</mn></msup></mfenced><mi>x</mi></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><mn>1</mn></mrow><mi>x</mi></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mrow><mfrac><mrow><msup><mi mathvariant="normal">e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn><mi>x</mi></mrow></mfrac><mo>&#215;</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q44. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="center left left"><mtr><mtd><mfrac><mn>1</mn><mrow><mo>|</mo><mi>x</mi><mo>|</mo></mrow></mfrac></mtd><mtd><mo>;</mo></mtd><mtd><mo>|</mo><mi>x</mi><mo>|</mo><mo>&#8805;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi></mtd><mtd><mo>;</mo></mtd><mtd><mo>|</mo><mi>x</mi><mo>|</mo><mo>&#60;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> is differentiable at every point of the domain, then the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> are respectively:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="center left"><mtr><mtd><mfrac><mn>1</mn><mrow><mo>|</mo><mi>x</mi><mo>|</mo></mrow></mfrac><mo>,</mo></mtd><mtd><mo>|</mo><mi>x</mi><mo>|</mo><mo>&#8805;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mo>,</mo></mtd><mtd><mo>|</mo><mi>x</mi><mo>|</mo><mo>&#60;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> function must be continuous</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>=</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>differentiability at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow></msub><mo>=</mo><mo>(</mo><mn>2</mn><mo>&#183;</mo><mi>a</mi><mi>x</mi><msub><mo>)</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>=</mo><mn>2</mn><mi>a</mi><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Put in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q45. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let the functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><msup><mi>x</mi><mn>3</mn></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Then, the number of points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>f</mi><mi>o</mi><mi>g</mi></mrow></mfenced><mfenced><mi>x</mi></mfenced></math> is NOT differentiable is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>2</mn><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mn>2</mn></msup><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>x</mi><mn>6</mn></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></mtd></mtr><mtr><mtd><msup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>'</mo></msup><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>6</mn><msup><mi>x</mi><mn>5</mn></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></mtd></mtr><mtr><mtd><mn>2</mn><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#215;</mo><mn>3</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></mtd></mtr></mtable></mfenced></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">L</mi><mo>.</mo><mo>&#8800;</mo><mi mathvariant="normal">R</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">L</mi><mo>.</mo></math>  (Discontinuous)</p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">L</mi><mo>.</mo><mo>=</mo><mi mathvariant="normal">R</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">L</mi><mo>.</mo></math>  (continuous)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>.</mo><mo>=</mo><mn>6</mn><mo>=</mo><mi mathvariant="normal">R</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is differentiable for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mn>0</mn></mfenced></math></p>

</details>

---

### Q46. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> be any function defined on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> and let it satisfy the condition: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>y</mi></mfenced></mrow></mfenced><mo>&#8804;</mo><mfenced close="|" open="|"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfenced><mo>,</mo><mo>&#8704;</mo><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn><mo>,</mo></math> then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> can take any value in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn><mo>,</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>y</mi></mfenced></mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced></mfrac></mfenced><mo>&#8804;</mo><mfenced close="|" open="|"><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced></mfenced></math><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mi>h</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>y</mi><mo>+</mo><mi>h</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="|" open="|"><mfrac><mrow><mi>f</mi><mfenced><mrow><mi>y</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>y</mi></mfenced></mrow><mi>h</mi></mfrac></mfenced><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>y</mi></mfenced></mrow></mfenced><mo>&#8804;</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>y</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>=</mo><mi>k</mi></math>   (constant)</p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math> given</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q47. JEE Main 2021 (25 Feb Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>A function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is defined on <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>3</mn><mo>]</mo></math> as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mi>min</mi><mfenced close="}" open="{"><mrow><mo>|</mo><mi>x</mi><mo>|</mo><mo>,</mo><mn>2</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>,</mo><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>[</mo><mo>|</mo><mi>x</mi><mo>|</mo><mo>]</mo><mo>&#160;&#160;</mo><mo>,</mo><mo>&#160;&#160;</mo><mn>2</mn><mo>&#60;</mo><mo>|</mo><mi>x</mi><mo>|</mo><mo>&#8804;</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi></math>. The number of points, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not differentiable in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> is ___ .</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mi>min</mi><mfenced close="}" open="{"><mrow><mo>|</mo><mi>x</mi><mo>|</mo><mo>,</mo><mn>2</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>,</mo><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>[</mo><mo>|</mo><mi>x</mi><mo>|</mo><mo>]</mo><mo>&#160;&#160;</mo><mo>,</mo><mo>&#160;&#160;</mo><mn>2</mn><mo>&#60;</mo><mo>|</mo><mi>x</mi><mo>|</mo><mo>&#8804;</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>]</mo></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3c2ee47f-364f-4177-bd8d-5aaa1371b271-6b26fcaf-8404-4ecf-a33d-172e7e5ca787-image.png" style="width: 419px; height: 227px;" /></p><p>Number of points of non-differentiability in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q48. JEE Main 2021 (25 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of points, at which the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> is not differentiable, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p>Critical points are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></math></p><p>but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn></math> is making a zero twice in product so, points of non differentiability are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Number of points of non-differentiability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q49. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a function defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>max</mi><mo>&#160;</mo><mfenced open="{" close="}"><mrow><mi>x</mi><mo>,</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></math>.Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> denote the set of all points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>,where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not differentiable.Then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mn>0</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#981;</mi></math> (an empty set)
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mn>1</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3c9c5ea3-6f41-4824-bda3-4576921867c8-image.png" style="width: 371px; height: 222px;" /></p><p>From the graph we can say <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>max</mi><mfenced close="}" open="{"><mrow><mi>x</mi><mo>,</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> sharp corners at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>1</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> Function is non-derivable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>1</mn></math></p>

</details>

---

### Q50. JEE Main 2020 (06 Sep Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><msup><mi>x</mi><mn>5</mn></msup><mi>sin</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>x</mi><mn>5</mn></msup><mi>cos</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mi>&#955;</mi><msup><mi>x</mi><mn>2</mn></msup></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mn>0</mn><mo>)</mo></math> exists, is___.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>5</mn><msup><mi>x</mi><mn>4</mn></msup><mo>&#183;</mo><mi>sin</mi><mo>(</mo><mn>1</mn><mo>/</mo><mi>x</mi><mo>)</mo><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup><mi>cos</mi><mo>(</mo><mn>1</mn><mo>/</mo><mi>x</mi><mo>)</mo><mo>+</mo><mn>10</mn><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>5</mn><msup><mi>x</mi><mn>4</mn></msup><mo>&#183;</mo><mi>cos</mi><mo>(</mo><mn>1</mn><mo>/</mo><mi>x</mi><mo>)</mo><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mi>sin</mi><mo>(</mo><mn>1</mn><mo>/</mo><mi>x</mi><mo>)</mo><mo>+</mo><mn>2</mn><mi>&#955;</mi><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>
Differentiating two times.<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="right left"><mtr><mtd><mn>20</mn><msup><mi>x</mi><mn>3</mn></msup><mo>&#183;</mo><mi>sin</mi><mo>(</mo><mn>1</mn><mo>/</mo><mi>x</mi><mo>)</mo><mo>-</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mi>cos</mi><mo>(</mo><mn>1</mn><mo>/</mo><mi>x</mi><mo>)</mo><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mi>cos</mi><mo>(</mo><mn>1</mn><mo>/</mo><mi>x</mi><mo>)</mo><mo>-</mo><mi>x</mi><mi>sin</mi><mo>(</mo><mn>1</mn><mo>/</mo><mi>x</mi><mo>)</mo><mo>+</mo><mn>10</mn><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>20</mn><msup><mi>x</mi><mn>3</mn></msup><mo>&#183;</mo><mi>cos</mi><mo>(</mo><mn>1</mn><mo>/</mo><mi>x</mi><mo>)</mo><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mo>(</mo><mn>1</mn><mo>/</mo><mi>x</mi><mo>)</mo><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mo>(</mo><mn>1</mn><mo>/</mo><mi>x</mi><mo>)</mo><mo>-</mo><mi>x</mi><mi>cos</mi><mo>(</mo><mn>1</mn><mo>/</mo><mi>x</mi><mo>)</mo><mo>+</mo><mn>2</mn><mi>&#955;</mi><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> 
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced><mo>=</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><msup><mn>0</mn><mo>-</mo></msup></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#955;</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>=</mo><mn>5</mn></math>

</details>

---

### Q51. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="center left"><mtr><mtd><msub><mi>k</mi><mn>1</mn></msub><mo>(</mo><mi>x</mi><mo>-</mo><mi>&#960;</mi><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mi>&#960;</mi></mtd></mtr><mtr><mtd><msub><mi>k</mi><mn>2</mn></msub><mi>cos</mi><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mi>&#960;</mi></mtd></mtr></mtable></mfenced></math> is twice differentiable, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>k</mi><mn>1</mn></msub><mo>,</mo><msub><mi>k</mi><mn>2</mn></msub></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo></math> is differentiable then will also continuous then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>&#960;</mi><mo>)</mo><mo>=</mo><msub><mi>k</mi><mn>1</mn></msub><msup><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mi>&#960;</mi><mo>+</mo></msup></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msub><mi>k</mi><mn>2</mn></msub><mi>cos</mi><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mo>=</mo><mo>-</mo><msub><mi>k</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mi>&#960;</mi><mo>+</mo></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>&#960;</mi></mfenced><mo>&#8658;</mo><msub><mi>k</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math>,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced close="}" open="{"><mrow><msub><mi>k</mi><mn>1</mn></msub><mo>(</mo><mi>x</mi><mo>-</mo><mi>&#960;</mi><msup><mo>)</mo><mn>2</mn></msup></mrow></mfenced><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mi>&#960;</mi></mtd></mtr><mtr><mtd><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced close="}" open="{"><mrow><msub><mi>k</mi><mn>2</mn></msub><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mi>&#960;</mi></mtd></mtr></mtable></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>2</mn><msub><mi>k</mi><mn>1</mn></msub><mo>(</mo><mi>x</mi><mo>-</mo><mi>&#960;</mi><mo>)</mo><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mi>&#960;</mi></mtd></mtr><mtr><mtd><mo>-</mo><msub><mi>k</mi><mn>2</mn></msub><mi>sin</mi><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mi>&#960;</mi></mtd></mtr></mtable></mfenced></math></p><p>then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><msup><mi>&#960;</mi><mo>-</mo></msup></mfenced><mo>=</mo><mn>2</mn><msub><mi>k</mi><mn>1</mn></msub><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><msup><mi>&#960;</mi><mo>+</mo></msup></mfenced><mo>=</mo><mo>-</mo><msub><mi>k</mi><mn>2</mn></msub><mi>sin</mi><mfenced><mi>&#960;</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>&#39;</mo><mfenced><msup><mi>&#960;</mi><mo>-</mo></msup></mfenced><mo>=</mo><mi>f</mi><mo>&#39;</mo><mfenced><msup><mi>&#960;</mi><mo>+</mo></msup></mfenced><mo>=</mo><mn>0</mn></math></p><p>Similarly, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mo>&#39;</mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>2</mn><msub><mi>k</mi><mn>1</mn></msub><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mi>&#960;</mi></mtd></mtr><mtr><mtd><mo>-</mo><msub><mi>k</mi><mn>2</mn></msub><mi>cos</mi><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mi>&#960;</mi></mtd></mtr></mtable></mfenced></math></p><p>As the function is twice differentiable, the second-order derivatives, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mi>H</mi><mi>D</mi><mo>=</mo><mi>R</mi><mi>H</mi><mi>D</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>'</mo><mo>'</mo><mfenced><msup><mi>&#960;</mi><mo>-</mo></msup></mfenced><mo>=</mo><mi>f</mi><mo>'</mo><mo>'</mo><mfenced><msup><mi>&#960;</mi><mo>+</mo></msup></mfenced><mo>&#8658;</mo><mn>2</mn><msub><mi>k</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><msub><mi>k</mi><mn>2</mn></msub><mi>cos&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msub><mi>k</mi><mn>1</mn></msub><mo>=</mo><msub><mi>k</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>k</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> (from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>)</p>

</details>

---

### Q52. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo><mo>&#8594;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math> be a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>e</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mi>x</mi></mrow></munder><mfrac><mrow><msup><mi>t</mi><mn>2</mn></msup><msup><mi>f</mi><mn>2</mn></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>f</mi><mn>2</mn></msup><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mrow><mi>t</mi><mo>-</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>.</mo></math> If<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>e</mi></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>e</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mi>e</mi></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>e</mi></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mi>x</mi></mrow></munder><mfrac><mrow><msup><mi>t</mi><mn>2</mn></msup><msup><mi>f</mi><mn>2</mn></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>f</mi><mn>2</mn></msup><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mrow><mi>t</mi><mo>-</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>
Using L&#39;Hospital</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mi>x</mi></mrow></munder><mfrac><mrow><mn>2</mn><mi>t</mi><msup><mi>f</mi><mn>2</mn></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mn>1</mn></mfrac><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><msup><mi>f</mi><mn>2</mn></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>[</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>]</mo><mo>=</mo><mn>0</mn></math>
But <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8800;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>y</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><mi>d</mi><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></math>
Integration gives</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mi>y</mi><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>ln</mi><mi>c</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>c</mi><mi>x</mi><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>c</mi><mi>x</mi></math>
Now</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>c</mi><mo>=</mo><mi>e</mi></math> (given)</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>e</mi><mo>&#160;</mo><mi>x</mi></math>
Now if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>e</mi></mfrac></math></p>

</details>

---

### Q53. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>,</mo></mtd><mtd><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>&#8804;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>&#62;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> is :

**Options:**

- **(A)** continuous on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mn>1</mn></mfenced></math> and differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>.
- **(B)** both continuous and differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mn>1</mn></mfenced></math>
- **(C)** continuous on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math>and differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** both continuous and differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) continuous on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mn>1</mn></mfenced></math> and differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>.**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>,</mo></mtd><mtd><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>&#8804;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>&#62;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Making graph</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2fcc3c53-0302-44cb-b00d-ec2fbf5f3135-image.png" style="width: 277px; height: 200px;" /></p><p>Clearly, function is continuous on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>&#8211;</mo><mfenced open="{" close="}"><mn>1</mn></mfenced></math> and differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>&#8211;</mo><mfenced open="{" close="}"><mrow><mo>&#8211;</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>.</p>

</details>

---

### Q54. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>S</mi></math>, be the set of all functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced open="[" close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math>, which are continuous on <math><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi></mi><mn>1</mn></mrow></mfenced></math>, and differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>. Then for every <math><mi>f</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>, there exists <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>, depending on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math>, such that.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>c</mi></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced></mrow></mfenced><mo>&#60;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfenced><mfenced open="|" close="|" separators="|"><mrow><msup><mi>f</mi><mi>'</mi></msup><mfenced><mi>c</mi></mfenced></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mi>c</mi></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfrac><mo>=</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced><mi>c</mi></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>c</mi></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced></mrow></mfenced><mo>&#60;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>c</mi></mrow></mfenced><mfenced open="|" close="|" separators="|"><mrow><msup><mi>f</mi><mi>'</mi></msup><mfenced><mi>c</mi></mfenced></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>c</mi></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced></mrow></mfenced><mo>&#60;</mo><mfenced open="|" close="|" separators="|"><mrow><msup><mi>f</mi><mi>'</mi></msup><mfenced><mi>c</mi></mfenced></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mi>c</mi></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfrac><mo>=</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced><mi>c</mi></mfenced></math>**

**Detailed Solution:**

<p>Let us consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math>, a constant function, as constant functions are continuous and differentiable everywhere.</p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>c</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mo>'</mo><mfenced><mi>c</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mi>c</mi></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mi>c</mi></mrow></mfrac><mo>=</mo><mi>f</mi><mo>'</mo><mfenced><mi>c</mi></mfenced><mo>=</mo><mn>0</mn></math>.</p>

</details>

---

### Q55. JEE Main 2020 (07 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math><mi>S</mi></math> be the set of points where the function <math><mo>,</mo><mi mathvariant="normal"></mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mo>|</mo><mn>2</mn><mo>-</mo><mo>|</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>|</mo><mo>,</mo><mi></mi><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mi></mi></math> is not differentiable. Then <math><mrow><munder><mo stretchy="true">&#8721;</mo><mrow><mi>x</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mrow></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>Check non-differentiability of function, we get,</p><p><math><mo>&#8757;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is non differentiable at <math><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi></mi><mn>3</mn><mo>,</mo><mi></mi><mn>5</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8721;</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mn>3</mn></mfenced></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mn>5</mn></mfenced></mrow></mfenced></mrow></math>
<math><mo>=</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn></math>
<math><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q56. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>&#8712;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>c</mi></mfenced><mo>=</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math>, then at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>c</mi><mo>,</mo><mi>&#160;</mi><mi>g</mi></math> is:

**Options:**

- **(A)** not differentiable
- **(B)** not differentiable if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>c</mi></mfenced><mo>=</mo><mn>0</mn></math>
- **(C)** differentiable if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>c</mi></mfenced><mo>=</mo><mn>0</mn></math>
- **(D)** differentiable if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>c</mi></mfenced><mo>&#8800;</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) differentiable if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>c</mi></mfenced><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>c</mi></mfenced><mo>=</mo><mn>0</mn></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mi>&#39;</mi></msup><mfenced separators="|"><msup><mi>c</mi><mo>+</mo></msup></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>c</mi><mo>+</mo></msup></mrow></munder><mfrac><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mi>c</mi></mfenced></mrow><mrow><mi>x</mi><mo>-</mo><mi>c</mi></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>c</mi><mo>+</mo></msup></mrow></munder><mfenced close="|" open="|"><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mo>(</mo><mi>c</mi><mo>)</mo></mrow><mrow><mi>x</mi><mo>-</mo><mi>c</mi></mrow></mfrac></mfenced><mo>,</mo><mo>&#160;</mo><mi>as</mi><mo>&#160;</mo><mi mathvariant="normal">x</mi><mo>&#62;</mo><mi mathvariant="normal">c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mi>&#39;</mi></msup><mfenced separators="|"><msup><mi>c</mi><mo>+</mo></msup></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><msup><mi>f</mi><mi>&#39;</mi></msup><mfenced separators="|"><mi>c</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><msup><mi>c</mi><mo>-</mo></msup></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>c</mi><mo>-</mo></msup></mrow></munder><mfrac><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mi>c</mi></mfenced></mrow><mrow><mi>x</mi><mo>-</mo><mi>c</mi></mrow></mfrac><mo>=</mo><mo>-</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>c</mi><mo>-</mo></msup></mrow></munder><mfenced close="|" open="|"><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mo>(</mo><mi>c</mi><mo>)</mo></mrow><mrow><mi>x</mi><mo>-</mo><mi>c</mi></mrow></mfrac></mfenced><mo>,</mo><mo>&#160;</mo><mi>as</mi><mo>&#160;</mo><mi mathvariant="normal">x</mi><mo>&#60;</mo><mi mathvariant="normal">c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mi>&#39;</mi></msup><mfenced separators="|"><msup><mi>c</mi><mo>-</mo></msup></mfenced><mo>=</mo><mo>-</mo><mfenced close="|" open="|"><mrow><msup><mi>f</mi><mi>&#39;</mi></msup><mfenced separators="|"><mi>c</mi></mfenced></mrow></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> to be differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>c</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>&#39;</mi></msup><mfenced separators="|"><mi>c</mi></mfenced></math> must be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>. Else, it is non-differentiable.</p>

</details>

---

### Q57. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>f</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mn>16</mn><mfenced separators="|"><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo></math> where the function <math><mi>f</mi></math> satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>f</mi><mfenced separators="|"><mi>y</mi></mfenced></math> for all natural numbers <math><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>2</mn><mo>.</mo></math> Then the natural number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>'</mi><mi>a</mi><mi>'</mi></math> is:

**Options:**

- **(A)** <math><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(C)** <math><mn>4</mn></math>
- **(D)** <math><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>3</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced separators="|"><mi>y</mi></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mn>2</mn></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><msup><mn>2</mn><mn>2</mn></msup></math></p><p>Now, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mn>3</mn></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced separators="|"><mn>2</mn></mfenced><mo>=</mo><msup><mn>2</mn><mn>3</mn></msup></math></p><p>Now, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mn>4</mn></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced separators="|"><mn>3</mn></mfenced><mo>=</mo><msup><mn>2</mn><mn>4</mn></msup></math></p><p>Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>10</mn></mfenced><mo>=</mo><msup><mn>2</mn><mn>10</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mn>16</mn><mfenced separators="|"><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>f</mi><mfenced separators="|"><mi>a</mi></mfenced><mi>f</mi><mfenced separators="|"><mi>k</mi></mfenced><mo>=</mo><mn>16</mn><mfenced separators="|"><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>a</mi></mfenced><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>f</mi><mfenced separators="|"><mi>k</mi></mfenced><mo>=</mo><mn>16</mn><mfenced separators="|"><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>a</mi></mfenced><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mn>2</mn></mfenced><mo>&#8230;</mo><mo>+</mo><mi>f</mi><mfenced separators="|"><mn>10</mn></mfenced></mrow></mfenced><mo>=</mo><mn>16</mn><mfenced separators="|"><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>a</mi></mfenced><mfenced separators="|"><mrow><msup><mn>2</mn><mn>1</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mn>2</mn><mn>10</mn></msup></mrow></mfenced><mo>=</mo><mn>16</mn><mfenced separators="|"><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Using the sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> terms of a geometric progression, i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>a</mi><mi>r</mi><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>a</mi><msup><mi>r</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mrow><mi>a</mi><mfenced><mrow><msup><mi>r</mi><mi>n</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>a</mi></mfenced><mfrac><mrow><mn>2</mn><mfenced separators="|"><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>16</mn><mfenced separators="|"><mrow><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>a</mi></mfenced><mo>=</mo><mn>8</mn><mo>=</mo><msup><mn>2</mn><mn>3</mn></msup></math></p><p>Also, we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>a</mi></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>3</mn><mo>.</mo></math></p>

</details>

---

### Q58. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>15</mn><mo>&#8211;</mo><mfenced open="|" close="|" separators="|"><mrow><mi>x</mi><mi>&#160;</mi><mo>&#8211;</mo><mn>10</mn></mrow></mfenced><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>.</mo></math> Then the set of all values of <math><mi>x</mi></math>, at which the function <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mo>(</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>)</mo></math> is not differentiable, is:

**Options:**

- **(A)** <math><mo>{</mo><mn>5</mn><mo>,</mo><mi> </mi><mn>10</mn><mo>,</mo><mi> </mi><mn>15</mn><mo>}</mo></math>
- **(B)** <math><mo>{</mo><mn>10</mn><mo>}</mo></math>
- **(C)** <math><mo>{</mo><mn>10</mn><mo>,</mo><mi> </mi><mn>15</mn><mo>}</mo></math>
- **(D)** <math><mo>{</mo><mn>5</mn><mo>,</mo><mi> </mi><mn>10</mn><mo>,</mo><mi> </mi><mn>15</mn><mo>,</mo><mi> </mi><mn>20</mn><mo>}</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>{</mo><mn>5</mn><mo>,</mo><mi> </mi><mn>10</mn><mo>,</mo><mi> </mi><mn>15</mn><mo>}</mo></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>15</mn><mo>-</mo><mfenced open="|" close="|" separators="|"><mrow><mi>x</mi><mo>-</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>15</mn><mo>-</mo><mfenced open="|" close="|" separators="|"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>15</mn><mo>-</mo><mfenced open="|" close="|"><mrow><mn>15</mn><mo>-</mo><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mo>-</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>15</mn><mo>-</mo><mfenced open="|" close="|" separators="|"><mrow><mn>5</mn><mo>-</mo><mfenced open="|" close="|" separators="|"><mrow><mi>x</mi><mo>-</mo><mn>10</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>15</mn><mo>-</mo><mfenced open="|" close="|" separators="|"><mrow><mfenced open="|" close="|" separators="|"><mrow><mi>x</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mrow><mtable><mtr><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr></mtable><mtable columnalign="left"><mtr/></mtable></mrow></mfenced></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>15</mn><mo>-</mo><mfenced close="|" open="|"><mrow><mn>10</mn><mo>-</mo><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>15</mn><mo>-</mo><mfenced open="|" close="|"><mrow><mn>5</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p>Now if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mn>5</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>15</mn><mo>-</mo><mn>5</mn><mo>+</mo><mi>x</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>10</mn></math></p><p>And if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>5</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>15</mn><mo>+</mo><mn>5</mn><mo>-</mo><mi>x</mi><mo>=</mo><mn>20</mn><mo>-</mo><mi>x</mi></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>15</mn><mo>-</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>10</mn><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>15</mn><mo>-</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>15</mn></mrow></mfenced></math></p><p>Now if <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>15</mn><mo>-</mo><mn>15</mn><mo>+</mo><mi>x</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>15</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>15</mn><mo>-</mo><mi>x</mi><mo>+</mo><mn>15</mn><mo>=</mo><mn>30</mn><mo>-</mo><mi>x</mi></math></p><p> 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left left"><mtr><mtd><mi>x</mi><mo>+</mo><mn>10</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>20</mn><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mn>5</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>10</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>,</mo></mtd><mtd><mn>10</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>15</mn></mtd></mtr><mtr><mtd><mn>30</mn><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>15</mn></mtd></mtr></mtable></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2de302ca-f260-4426-9c02-67407aa0b963-image.png" style="width: 400px; height: 194px;" /></p><p>Now, it is clear from the graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> has sharp corners at<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>15</mn></math> and hence this function is not differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>15</mn><mo>.</mo></math></p>

</details>

---

### Q59. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>S</mi></math> be the set of all points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mi>&#960;</mi><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math> at which the function, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>min</mi><mfenced close="}" open="{" separators="|"><mrow><mi>sin</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></math> is not differentiable. Then <math><mi>S</mi></math> is a subset of which of the following?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{" separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mi>&#160;</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mi>&#160;</mi><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{" separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/54f80512-5ec4-43f2-9ef3-af4478b9dffe-image.png" style="width: 370px; height: 200px;" /></p><p> Sharp points are at <math><mfrac><mrow><mo>-</mo><mn>3</mn><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math> and <math><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>.</p><p><math><mo>&#8756;</mo></math> Set of non-differentiable points of function are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{" separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math> which is a subset of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{" separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mi>&#160;</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mi>&#160;</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math>.</p>

</details>

---

### Q60. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{K}$ be the set of all real values of $x$ where the function $f(x)=\sin |x|-|x|+2(x-\pi) \cos |x|$ is not differentiable.

Then the set $K$ is equal to :

**Options:**

- **(A)** $\phi$ (an empty set)
- **(B)** $(\pi\}$
- **(C)** $\{0\}$
- **(D)** $\{0, \pi\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\phi$ (an empty set)**

**Detailed Solution:**

$f(x)=\sin |x|-|x|+2(x-\pi) \cos |x|$

There are two cases,

Case $(1), x>0$

$f(x)=\sin x-x+2(x-\pi) \cos x$

$f^{\prime}(x)=\cos x-1+2(1-0) \cos x-2 \sin (x-\pi)$

$f^{\prime}(x)=3 \cos x-2(x-\pi) \sin x-1$

Then, function $f(x)$ is differentiable for all $x>0$

Case $(2) x  < 0$

$f(x)=-\sin x+x+2(x-\pi) \cos x$

$f^{\prime}(x)=-\cos x+1-2(x-\pi) \sin x+2 \cos x$

$f^{\prime}(x)=\cos x+1-2(x-\pi) \sin x$

Then, function $f(x)$ is differentiable for all $x < 0$

Now check for $x=0$

$f^{\prime}\left(0^{*}\right) \mathrm{R} \cdot \mathrm{HD}=3-1=2$

$f^{\prime}(0) \mathrm{L} . \mathrm{H.D.}=1+1=2$

$\mathrm{L} . \mathrm{HD}=\mathrm{R} . \mathrm{H.D}$

Then, function $f(x)$ is differentiable for $x=0 .$ So it is

differentiable everywhere

Hence, $k=\phi$

</details>

---

### Q61. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=\left\{\begin{array}{cl}-1, & -2 \leq x  < 0 \\ x^{2}-1, & 0 \leq x \leq 2\end{array}\right.$ and

$g(x)=|\eta(x)|+f(x \mid) .$ Then, in the interval $(-2,2), g$ is:

**Options:**

- **(A)** differentiable at all points
- **(B)** not continuous
- **(C)** not differentiable at two points
- **(D)** not differentiable at one point

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) not differentiable at one point**

**Detailed Solution:**

$f(x)=\left\{\begin{array}{cc}-1, & -2 \leq x  < 0 \\ x^{2}-1, & 0 \leq x \leq 2\end{array}\right.$

$\text { Then, } f(x \mid)=\left\{\begin{array}{cc}

-1, & -2 \leq|x| < 0 \\

|x|^{2}-1, & 0 \leq|x| \leq 2

\end{array}\right.$

$\Rightarrow f(|x|)=x^{2}-1,-2 \leq x \leq 2$

$\Rightarrow g(x)=\left\{\begin{aligned} 1+x^{2}-1, &-2 \leq x < 0 \\\left(x^{2}-1\right)+\left|x^{2}-1\right|, & 0 \leq x \leq 2 \end{aligned}\right.$

$=\left\{\begin{array}{cc}x^{2}, & -2 \leq x < 0 \\ 0, & 0 \leq x < 1 \\ 2\left(x^{2}-1\right), & 1 \leq x \leq 2\end{array}\right.$

$g^{\prime}\left(0^{-}\right)=0, g^{\prime}\left(0^{*}\right)=0, g^{\prime}\left(1^{-}\right)=0, g^{\prime}\left(1^{+}\right)=4$

$\Rightarrow g(x)$ is non-differentiable at $x=1$ $\Rightarrow g(x)$ is not differentiable at one point.

</details>

---

### Q62. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be a function defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>m</mi><mi>a</mi><mi>x</mi><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mo>,</mo><mi>&#160;</mi><mo>-</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced><mo>.</mo></math> If <math><mi>K</mi></math> be the set of all points at which <math><mi>f</mi></math> is not differentiable, then <math><mi>K</mi></math> has exactly

**Options:**

- **(A)** two elements
- **(B)** one element
- **(C)** three elements
- **(D)** five elements

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) three elements**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dunkgpjjdhepqgkhyvfflzzpbczipvoljvyqlbjqnplunpyxwx.png" /></p><p>From the graph, it can be concluded that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is non-differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#177;</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo></math>At <math><mn>3</mn></math> points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>.</p>

</details>

---

### Q63. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close="" separators="|"><mrow><mtable><mtr><mtd><mi>m</mi><mi>a</mi><mi>x</mi><mfenced separators="|"><mrow><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mo>,</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>,</mo></mtd><mtd><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>8</mn><mo>-</mo><mn>2</mn><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mo>,</mo></mtd><mtd><mn>2</mn><mo>&#60;</mo><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mo>&#8804;</mo><mn>4</mn></mtd></mtr></mtable><mo>.</mo></mrow></mfenced></math> Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of points in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></math> at which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not differentiable. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>

**Options:**

- **(A)** equals <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(B)** equals <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** is an empty set
- **(D)** equal <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) equals <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given function is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close="" separators="|"><mtable><mtr><mtd><mi>m</mi><mi>a</mi><mi>x</mi><mfenced separators="|"><mrow><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mo>,</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>,</mo></mtd><mtd><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>8</mn><mo>-</mo><mn>2</mn><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mo>,</mo></mtd><mtd><mn>2</mn><mo>&#60;</mo><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mo>&#8804;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p>The graph of the function, is</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0586fe52-962a-400c-b729-b64749754feb-139.png" style="width: 350px; height: 210px;" /></p><p>We know that, a function is not differentiable at a point where its graph has a sharp corner.</p><p>And, from the graph we can easily conclude that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math> is non-derivable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></math></p><p>Hence, the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q64. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>f</mi></math> be a differentiable function from <math><mi>R</mi></math> to <math><mi>R</mi></math> such that <math><mfenced close="|" open="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>y</mi></mrow></mfenced></mrow></mfenced><mo>&#8804;</mo><mn>2</mn><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced></mrow><mrow><mrow><mrow><mn>3</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup><mo>,</mo></math> for all <math><mi>x</mi><mo>,</mo><mi>y</mi><mo>&#8712;</mo><mi>R</mi><mtext>.</mtext><mtext>&#160;</mtext></math> If <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math> then <math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><msup><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** <math><mn>2</mn></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>1</mn></math>**

**Detailed Solution:**

Given functional equality is

<math><mfenced close="|" open="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>y</mi></mrow></mfenced></mrow></mfenced><mo>&#8804;</mo><mn>2</mn><mi>&#160;</mi><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced></mrow><mrow><mrow><mrow><mn>3</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup><mi>&#160;</mi></math>

Put <math><mi>x</mi><mo>=</mo><mi>y</mi><mo>+</mo><mi>h</mi><mo>,</mo><mi>&#160;</mi></math> we get

<math><mfenced close="|" open="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mi>h</mi></mrow></mfenced></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>y</mi></mrow></mfenced><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mo>&#8804;</mo><mn>2</mn><mo>.</mo><mi>&#160;</mi><mo>|</mo><mi>h</mi></mrow></mfenced></mrow><mrow><mrow><mrow><mn>3</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup></math>

<math><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mo>(</mo><mi>y</mi><mo>)</mo></mrow><mrow><mi>h</mi></mrow></mfrac></mrow></mfenced><mo>&#8804;</mo><mn>2</mn><mi>&#160;</mi><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>h</mi></mrow></mfenced></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup></math>

<math><mo>&#8658;</mo><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>y</mi></mrow></mfenced></mrow><mrow><mi>h</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>&#8804;</mo><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>&#160;</mi><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>h</mi></mrow></mfenced></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup></mrow></mrow></math>

<math><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>y</mi></mrow></mfenced></mrow></mfenced><mo>&#8804;</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>y</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>f</mi><mi>&#8242;</mi><mfenced separators="|"><mrow><mi>y</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>y</mi></mrow></mfenced><mo>=</mo><mi>c</mi></math>

<math><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>y</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mi>&#160;</mi></math> (since <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math> )

Now <math><mrow><msubsup><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mrow><msup><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#160;</mi><mrow><msubsup><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mrow><mn>1</mn></mrow></mrow><mi>&#160;</mi><mi>d</mi><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mrow></math>.

</details>

---

### Q65. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mo>{</mo><mfenced separators="|"><mrow><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><mo>&#215;</mo><mi>R</mi><mi>&#160;</mi><mo>:</mo><mo>&#160;</mo><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mo>=</mo><mfenced separators="|"><mrow><mfenced open="|" close="|" separators="|"><mrow><mi>&#955;</mi><mi>&#160;</mi></mrow></mfenced><msup><mi>e</mi><mfenced open="|" close="|" separators="|"><mi>t</mi></mfenced></msup><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mi>sin</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>2</mn><mfenced open="|" close="|" separators="|"><mi>t</mi></mfenced></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>t</mi><mo>&#8712;</mo><mi>R</mi></math> is a differential function}. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is a subset of :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mi>&#8734;</mi><mo>,&#160;</mo><mn>0</mn></mrow></mfenced><mo>&#215;</mo><mi>R</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>&#215;</mo><mfenced open="[" close="" separators="|"><mrow><mn>0</mn><mo>,&#160;</mo><mi>&#8734;</mi><mo>)</mo></mrow></mfenced></math>
- **(C)** <math><mfenced close="" open="[" separators="|"><mrow><mn>0</mn><mo>, </mo><mi>∞</mi><mo>)</mo></mrow></mfenced><mo>×</mo><mi>R</mi></math>
- **(D)** <math><mi mathvariant="normal">R</mi><mo>×</mo><mfenced separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>, </mo><mn>0</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>&#215;</mo><mfenced open="[" close="" separators="|"><mrow><mn>0</mn><mo>,&#160;</mo><mi>&#8734;</mi><mo>)</mo></mrow></mfenced></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mfenced><mrow><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><mo>&#215;</mo><mi>R</mi></mrow></mfenced></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced><mo>=</mo><mfenced separators="|"><mrow><mfenced open="|" close="|" separators="|"><mi>&#955;</mi></mfenced><msup><mi>e</mi><mfenced open="|" close="|" separators="|"><mi>t</mi></mfenced></msup><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mo>.</mo><mi mathvariant="normal">&#160;</mi><mi>sin</mi><mo>&#8289;</mo><mn>2</mn><mfenced open="|" close="|" separators="|"><mi>t</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mi>H</mi><mi>D</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mn>0</mn></mrow><mi>h</mi></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfenced separators="|"><mrow><mfenced open="|" close="|" separators="|"><mi>&#955;</mi></mfenced><msup><mi>e</mi><mi>h</mi></msup><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mo>&#8289;</mo><mi>h</mi></mrow><mi>h</mi></mfrac><mo>=</mo><mn>2</mn><mo>(</mo><mfenced open="|" close="|" separators="|"><mi>&#955;</mi></mfenced><mo>-</mo><mi>&#956;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mi>H</mi><mi>D</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn><mo>-</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mn>0</mn></mrow><mrow><mo>-</mo><mi>h</mi></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfenced separators="|"><mrow><mfenced open="|" close="|" separators="|"><mi>&#955;</mi></mfenced><msup><mi>e</mi><mi>h</mi></msup><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mo>&#8289;</mo><mi>h</mi></mrow><mrow><mo>-</mo><mi>h</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn><mo>(</mo><mfenced open="|" close="|" separators="|"><mi>&#955;</mi></mfenced><mo>-</mo><mi>&#956;</mi><mo>)</mo></math></p><p>Now, <math><mi>L</mi><mi>H</mi><mi>D</mi><mo>=</mo><mi>R</mi><mi>H</mi><mi>D</mi></math> if <math><mfenced close="|" open="|" separators="|"><mrow><mi>&#955;</mi></mrow></mfenced><mo>=</mo><mi>&#956;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mo>&#8805;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi></math></p>

</details>

---

### Q66. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `3`

Let $S=\left\{(\lambda, \mu) \in R \times R: f(t)=\left(|\lambda| e^t-\mu\right) \cdot \sin (2|t|)\right.$, $t \in R$, is a differentiable function $\}$. Then $S$ is a subest of?

**Options:**

- **(A)** $R \times[0, \infty)$
- **(B)** $(-\infty, 0) \times R$
- **(C)** $[0, \infty) \times R$
- **(D)** $R \times(-\infty, 0)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $R \times[0, \infty)$**

**Detailed Solution:**

$$
\begin{aligned}
&\quad S=\left\{(\lambda, \mu) \in \mathrm{R} \times \mathrm{R}: \mathrm{f}(\mathrm{t})=\left(|\lambda| \mathrm{e}^{\mid t}-\mu\right) \sin (2 \mathrm{t} \mid),\right. \\
&t \in R \\
&f(t)=\left(|\lambda| \mathrm{e}^{|t|}-\mu\right) \sin (2|t|) \\
&\left\{\begin{array}{l}
\left(|\lambda| e^t-\mu\right) \sin 2 t \quad t>0 \\
\left(|\lambda| e^{-t}-\mu\right)(-\sin 2 t) t < 0
\end{array}\right. \\
&f^{\prime}(t) \\
&\left\{\begin{array}{l}
\left(|\lambda| \mathrm{e}^t\right) \sin 2 t+\left(|\lambda| \mathrm{e}^t-\mu\right)(2 \cos 2 t) t>0 \\
|\lambda| \mathrm{e}^{-t} \sin 2 t+\left(|\lambda| e^{-t}-\mu\right)(-2 \cos 2 t) < t < 0
\end{array}\right. \\
&\text { As, } f(t) \text { is differentiable } \\
&\therefore \text { LHD }=\mathrm{RHD} \text { at } t=0 \\
&|\lambda| \cdot \sin 2(0)+\left(|\lambda| \mathrm{e}^0-\mu\right) 2 \cos (0) \\
&=|\lambda| \mathrm{e}^{-0} \cdot \sin 2(0)-2 \cos (0)\left(|\lambda| \mathrm{e}^{-0}-\mu\right) \\
&\Rightarrow 0+(|\lambda|-\mu) 2=0-2(|\lambda|-\mu) \\
&\quad 4(|\lambda|-\mu)=0 \\
&\quad|\lambda|=\mu
\end{aligned}
$$
So, $S \equiv(\lambda, \mu)=\{\lambda \in R \& \mu \in[0, \infty)\}$
Therefore set $\mathrm{S}$ is subset of $R \times[0, \infty)$

</details>

---

### Q67. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mi>t</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|" separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mi>&#160;</mi><mo>&#8901;</mo><mfenced separators="|"><mrow><msup><mi>e</mi><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>sin</mi><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mi>&#160;</mi><mtext>is&#160;not&#160;differentiable&#160;at</mtext><mi>&#160;</mi><mi>t</mi></mrow></mfenced><mo>.</mo></math> Then, the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is equal to:

**Options:**

- **(A)** <math><mfenced close="}" open="{" separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mi>π</mi></mrow></mfenced></math>
- **(B)** <math><mi>ϕ</mi></math> (an empty set)
- **(C)** <math><mfenced close="}" open="{" separators="|"><mrow><mn>0</mn></mrow></mfenced></math>
- **(D)** <math><mfenced close="}" open="{" separators="|"><mrow><mi>π</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>ϕ</mi></math> (an empty set)**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>.</mo><mfenced separators="|"><mrow><msup><mi>e</mi><mfenced close="|" open="|" separators="|"><mi>x</mi></mfenced></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>.</mo><mi>sin</mi><mfenced close="|" open="|" separators="|"><mi>x</mi></mfenced></math></p><p>In the neighbourhood of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#960;</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>.</mo><mfenced separators="|"><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>.</mo><mi>sin</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><msup><mi>f</mi><mi>&#8242;</mi></msup><mfenced separators="|"><mi>&#960;</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>&#960;</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mi>&#960;</mi></mfenced></mrow><mi>h</mi></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced close="|" open="|" separators="|"><mi>h</mi></mfenced><mi>sin</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>&#960;</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mfenced separators="|"><mrow><msup><mi>e</mi><mrow><mi>&#960;</mi><mo>+</mo><mi>h</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mi>h</mi></mfrac><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><msup><mi>f</mi><mi>&#8242;</mi></msup><mfenced separators="|"><mi>&#960;</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>&#960;</mi></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>&#960;</mi><mo>-</mo><mi>h</mi></mrow></mfenced></mrow><mi>h</mi></mfrac><mo>=</mo><mo>-</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced close="|" open="|" separators="|"><mrow><mo>-</mo><mi>h</mi></mrow></mfenced><mi>sin</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>&#960;</mi><mo>-</mo><mi>h</mi></mrow></mfenced><mfenced separators="|"><mrow><msup><mi>e</mi><mrow><mi>&#960;</mi><mo>-</mo><mi>h</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mi>h</mi></mfrac><mo>=</mo><mn>0</mn></math>

Differentiable at <math><mi>x</mi><mo>=</mo><mi>&#960;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><msup><mi>f</mi><mi>&#8242;</mi></msup><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>h</mi></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced></mrow><mi>h</mi></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="|" open="|" separators="|"><mrow><mi>h</mi><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>&#215;</mo><mfrac><mrow><mi>sin</mi><mfenced close="|" open="|" separators="|"><mi>h</mi></mfenced><mfenced><mrow><msup><mi>e</mi><mfenced close="|" open="|"><mi>h</mi></mfenced></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mi>h</mi></mfrac><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><msup><mi>f</mi><mi>&#8242;</mi></msup><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mi>h</mi></mrow></mfenced></mrow><mi>h</mi></mfrac><mo>=</mo><mo>-</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="|" open="|" separators="|"><mrow><mo>-</mo><mi>h</mi><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>&#215;</mo><mfrac><mrow><mi>sin</mi><mfenced close="|" open="|" separators="|"><mrow><mo>-</mo><mi>h</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mfenced close="|" open="|"><mrow><mo>-</mo><mi>h</mi></mrow></mfenced></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mi>h</mi></mfrac><mo>=</mo><mn>0</mn></math>

Differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>

Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is differentiable everywhere.

<math><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mi>&#981;</mi></math></p>

</details>

---

### Q68. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If the function <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>a</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>,</mo></mrow></mrow></mtd><mtd><mn>1</mn><mi>&#160;</mi><mo>&#8804;</mo><mi>x</mi><mi>&#160;</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr></mtable></mrow></mfenced></math> is differentiable at <math><mi>x</mi><mo>=</mo><mn>1</mn></math>, then <math><mfrac><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mi>π</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>π</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mo>-</mo><mi>π</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mn>1</mn><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mo>(</mo><mn>2</mn><mo>)</mo></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>π</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mi>x</mi></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>a</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>b</mi></mrow></mfenced></mrow></mrow></mtd><mtd><mn>1</mn><mi>&#160;</mi><mo>&#8804;</mo><mi>x</mi><mi>&#160;</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr></mtable></mrow></mfenced></math>

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>.

<math> <mrow> <mo>&#8658;</mo><munder> <mrow> <mi>lim</mi> </mrow> <mrow> <mi>x</mi><mo>&#8594;</mo><mn>1</mn> </mrow> </munder> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><munder> <mrow> <mi>lim</mi> </mrow> <mrow> <mi>x</mi><mo>&#8594;</mo><msup> <mn>1</mn> <mo>+</mo> </msup> </mrow> </munder> <mrow><mo>(</mo> <mrow> <mi>a</mi><mo>+</mo><msup> <mrow> <mi>cos</mi> </mrow> <mrow> <mo>&#8722;</mo><mn>1</mn> </mrow> </msup> <mrow><mo>(</mo> <mrow> <mi>x</mi><mo>+</mo><mi>b</mi> </mrow> <mo>)</mo></mrow> </mrow> <mo>)</mo></mrow><mo>=</mo><mi>f</mi><mrow><mo>(</mo> <mn>1</mn> <mo>)</mo></mrow> </mrow> </math>

<math><mo>&#8658;</mo></math> <math><mo>-</mo><mn>1</mn><mo>=</mo><mi>a</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+b</mo></mrow></mfenced></mrow></mrow></math>

<math><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>b</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mo>-</mo><mn>1</mn><mo>-</mo><mi>a</mi></math> ........<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>.

<math><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHD</mi><mo>=</mo><mi>RHD</mi></math>

<math><mo>&#8658;</mo></math> <math><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>b</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></math>

<math><mo>&#8658;</mo></math> <math><mn>1</mn><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>b</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>1</mn></math>

<math><mo>&#8658;</mo></math> <math><mi>b</mi><mo>=</mo><mi>&#160;</mi><mo>-</mo><mn>1</mn></math> ......<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math>

From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> <math><mo>&#8658;</mo></math> <math><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mo>(</mo><mn>0</mn><mo>)</mo></mrow></mrow><mo>=</mo><mi>&#160;</mi><mo>-</mo><mn>1</mn><mo>-</mo><mi>a</mi></math>

<math><mo>&#8756;</mo></math> <math><mo>-</mo><mn>1</mn><mo>-</mo><mi>a</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mi>a</mi><mo>=</mo><mi>&#160;</mi><mo>-</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mi>a</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> ......<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>iii</mi></mfenced></math>

<math><mo>&#8756;</mo></math> <math><mfrac><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>&#960;</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

</details>

---

### Q69. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `2`

For <math><mi>x</mi><mo>∈</mo><mi>R</mi><mo>,</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></math> and <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>'</mo></msup><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mo>-</mo><mi>cos</mi><mo>⁡</mo><mfenced separators="|"><mrow><mi>log</mi><mo>⁡</mo><mn>2</mn></mrow></mfenced></math>
- **(B)** <math><mi>g</mi><mi> </mi></math> is differentiable at <math><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>'</mo></msup><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mo>-</mo><mi>sin</mi><mo>⁡</mo><mfenced separators="|"><mrow><mi>log</mi><mo>⁡</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math><mi>g</mi></math>  is not differentiable at  <math><mi>x</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>'</mo></msup><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mi>cos</mi><mo>⁡</mo><mfenced separators="|"><mrow><mi>log</mi><mo>⁡</mo><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>'</mo></msup><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mi>cos</mi><mo>⁡</mo><mfenced separators="|"><mrow><mi>log</mi><mo>⁡</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

In the neighborhood of <math><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>

<math><mo>∴</mo></math> <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mo>(</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>)</mo><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mrow></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>log</mi><mo>⁡</mo><mn>2</mn><mo>-</mo><mi>sin</mi><mi> </mi><mfenced separators="|"><mrow><mi>log</mi><mo>⁡</mo><mn>2</mn><mo>-</mo><mi>sin</mi><mo>⁡</mo><mi>x</mi></mrow></mfenced></math>

<math><mo>∴</mo></math> <math><msup><mrow><mi>g</mi></mrow><mrow><mi>′</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow><mi> </mi><mfenced separators="|"><mrow><mo>–</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></math>

<math><mo>∴</mo></math> <math><msup><mrow><mi>g</mi></mrow><mrow><mi>′</mi></mrow></msup><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow></mrow></mfenced></mrow></mrow></math>

</details>

---

### Q70. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `1`

If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>g</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>{</mo><mtable><mtr><mtd><mi>k</mi><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mtext>&#160;&#160;,&#160;&#160;</mtext></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mi>m</mi><mi>x</mi><mo>+</mo><mn>2&#160;&#160;</mn><mtext>,&#160;&#160;</mtext></mtd><mtd><mn>3</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>5</mn></mtd></mtr></mtable></math>   is differentiable, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>+</mo><mi>m</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>16</mi><mn>5</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>10</mi><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

LHD at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math>

<math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#10230;</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>k</mi><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><mn>2</mn><mi>k</mi></mrow><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>

<math><mo>=</mo><mi>&#160;</mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder></mrow><mo>&#8289;k</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>.</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mrow></math>

RHD at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math>

<math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><mfenced separators="|"><mrow><mi>m</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi>k</mi></mrow><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfrac></mrow></mrow></math>

Since this limit exists if <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>m</mi><mo>+</mo><mn>2</mn><mo>-</mo><mn>2</mn><mi>k</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>0</mn><mn>0</mn></mfrac></math> form)

So,<math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><mfenced separators="|"><mrow><mi>m</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mn>3</mn><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mi>m</mi></mrow></mrow></math>

Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mfrac><mi>k</mi><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi>ii</mi></mfenced></math>

From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math>

<math><mi>m</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><mi>k</mi><mo>=</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>k</mi><mo>+</mo><mi>m</mi><mo>=</mo><mn>2</mn></math>

</details>

---

### Q71. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>&#160;</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>.</mo></math> Then, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is

**Options:**

- **(A)** differentiable but not continuous
- **(B)** neither continuous nor differentiable
- **(C)** continuous as well as differentiable
- **(D)** continuous but not differentiable

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) continuous as well as differentiable**

**Detailed Solution:**

<p>We know that if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8804;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mo>-</mo><mi>k</mi><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mi>k</mi><mo>,</mo><mo>&#160;</mo><mi>k</mi><mo>&#8712;</mo><mi>R</mi><mo>.</mo></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>&#160;</mi><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced separators="|"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math></p><p>Hence, by using sandwich theorem, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p>Further <math><mfenced close="|" open="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced></mrow></mfenced><mo>&#8804;</mo><mn>0</mn><mi>&#160;</mi><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p>Hence, <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p>Now, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfenced separators="|"><mi>x</mi></mfenced><mo>&#8804;</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow><mfenced separators="|"><mi>x</mi></mfenced></mfrac><mo>&#8804;</mo><mfenced separators="|"><mi>x</mi></mfenced></math></p><p>Thus, by using sandwich theorem, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>-</mo><mfenced separators="|"><mi>x</mi></mfenced><mo>&#8804;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow><mfenced separators="|"><mi>x</mi></mfenced></mfrac><mo>&#8804;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced separators="|"><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#8804;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow><mfenced separators="|"><mi>x</mi></mfenced></mfrac><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow><mfenced separators="|"><mi>x</mi></mfenced></mfrac><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>We know that a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is differentiable at a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>a</mi><mo>,</mo></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mrow><mi>a</mi><mo>-</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mfenced><mi>a</mi></mfenced></mrow><mrow><mo>-</mo><mi>h</mi></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mfenced><mi>a</mi></mfenced></mrow><mi>h</mi></mfrac></math></p><p>Now, the left-hand derivative at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mrow><mn>0</mn><mo>-</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></mrow><mrow><mo>-</mo><mi>h</mi></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mrow><mo>-</mo><mi>h</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mi>h</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>,</mo></math> ( by using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>) </p><p>And, the right-hand derivative at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mrow><mn>0</mn><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></mrow><mi>h</mi></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mi>h</mi></mfenced></mrow><mi>h</mi></mfrac><mo>=</mo><mn>0</mn><mo>,</mo></math> ( by using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>)

Hence, <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>.</mo></math></p>

</details>

---

### Q72. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}, \mathrm{g}: \mathrm{R} \rightarrow \mathrm{R}$ be two functions defined by $f(x)= \begin{cases}x \sin \left(\frac{1}{x}\right) & , x \neq 0 \\ 0, & , x=0\end{cases}$ and $g(x)=x f(x)$
Statement I: $f$ is a continuous function at $\mathrm{x}=0$.
Statement II: $g$ is a differentiable function at $x=0$.

**Options:**

- **(A)** Both statement I and II are false.
- **(B)** Both statement I and II are true.
- **(C)** Statement $\mathrm{I}$ is true, statement $\mathrm{II}$ is false.
- **(D)** Statement $\mathrm{I}$ is false, statement $\mathrm{II}$ is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Both statement I and II are true.**

**Detailed Solution:**

$$
\begin{aligned}
&f(x)= \begin{cases}x \sin \left(\frac{1}{x}\right), & x \neq 0 \\
0, & x=0\end{cases} \\
&\text { and } g(x)=x f(x) \\
&\text { For } f(x) \\
&\mathrm{LHL}=\lim _{h \rightarrow 0^{-}}\left\{-h \sin \left(-\frac{1}{h}\right)\right\}
\end{aligned}
$$
$=0 \times$ a finite quantity between $-1$ and 1
$$
=0
$$
$$
\mathrm{RHL}=\lim _{h \rightarrow 0^{+}} h \sin \frac{1}{h}=0
$$
Also, $f(0)=0$
Thus $\mathrm{LHL}=\mathrm{RHL}=f(0)$
$\therefore f(x)$ is continuous at $x=0$
$$
g(x)= \begin{cases}x^2 \sin \frac{1}{x}, & x \neq 0 \\ 0, & x=0\end{cases}
$$
For $g(x)$

$$
\mathrm{LHL}=\lim _{h \rightarrow 0^{-}}\left\{-h^2 \sin \left(\frac{1}{h}\right)\right\}
$$
$=0^2 \times$ a finite quantity between $-1$ and $1=0$
$$
\text { RHL }=\lim _{h \rightarrow 0^{+}} h^2 \sin \left(\frac{1}{h}\right)=0
$$
Also $g(0)=0$
$\therefore g(x)$ is continuous at $x=0$

</details>

---

### Q73. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x)=x|x|, g(x)=\sin x$ and $h(x)=(g \circ f)(x)$. Then

**Options:**

- **(A)** $\mathrm{h}(\mathrm{x})$ is not differentiable at $\mathrm{x}=0$.
- **(B)** $\mathrm{h}(\mathrm{x})$ is differentiable at $\mathrm{x}=0$, but $\mathrm{h}^{\prime}(\mathrm{x})$ is not continuous at $x=0$
- **(C)** $\mathrm{h}^{\prime}(\mathrm{x})$ is continuous at $\mathrm{x}=0$ but it is not differentiable at $x=0$
- **(D)** $\mathrm{h}^{\prime}(\mathrm{x})$ is differentiable at $\mathrm{x}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{h}^{\prime}(\mathrm{x})$ is continuous at $\mathrm{x}=0$ but it is not differentiable at $x=0$**

**Detailed Solution:**

Let $f(x)=x|x|=x|x|, g(x)=\sin x$ and $h(x)=g o f(x)=g[f(x)]$
$$
\begin{aligned}
&\therefore h(x)= \begin{cases}\sin x^2, & x \geq 0 \\
-\sin x^2, & x < 0\end{cases} \\
&\text { Now, } h^{\prime}(x)=\left\{\begin{array}{cc}
2 x \cos x^2, & x \geq 0 \\
-2 x \cos x^2, & x < 0
\end{array}\right.
\end{aligned}
$$
Since, L.H.L and R.H.L at $x=0$ of $h^{\prime}(x)$ is equal to 0 therefore $h^{\prime}(x)$ is continuous at $x=0$
Now, suppose $h^{\prime}(x)$ is differentiable
$$
\begin{aligned}
&\therefore h^{\prime \prime}(x) \\
&= \begin{cases}2\left(\cos x^2+2 x^2\left(-\sin x^2\right),\right. & x \geq 0 \\
2\left(-\cos x^2+2 x^2 \sin x^2\right), & x < 0\end{cases}
\end{aligned}
$$
Since, L.H.L and R.H.L at $x=0$ of $h^{\prime \prime}(x)$ are different therefore $h^{\prime \prime}(x)$ is not continuous.
$\Rightarrow h^{\prime \prime}(x)$ is not differentiable
$\Rightarrow$ our assumption is wrong
Hence $h^{\prime}(x)$ is not differentiable at $x=0$.

</details>

---

### Q74. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=a|\sin x|+b e^{|x|}+c|x|^3$, where $a, b, c \in R$, is differentiable at $x=0$, then

**Options:**

- **(A)** $a=0, b$ and $c$ are any real numbers
- **(B)** $c=0, a=0, b$ is any real number
- **(C)** $b=0, c=0, a$ is any real number
- **(D)** $a=0, b=0, c$ is any real number

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a=0, b=0, c$ is any real number**

**Detailed Solution:**

$|\sin x|$ and $e^{|x|}$ are not differentiable at $x=0$ and $|x|^3$ is differentiable at $x=0$. $\therefore$ for $f(x)$ to be differentiable at $x=0$, we must have $a=0, b=0$ and $c$ is any real number.

</details>

---

### Q75. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `3`

If $x+|y|=2 y$, then $y$ as a function of $x$, at $x=0$ is

**Options:**

- **(A)** differentiable but not continuous
- **(B)** continuous but not differentiable
- **(C)** continuous as well as differentiable
- **(D)** neither continuous nor differentiable

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) continuous but not differentiable**

**Detailed Solution:**

Given $x+|y|=2 y$
$$
\begin{aligned}
& \Rightarrow \quad x+y=2 y \text { or } x-y=2 y \\
& \Rightarrow \quad x=y \text { or } x=3 y
\end{aligned}
$$
This represent a straight line which passes through origin.
Hence, $x+|y|=2 y$ is continuous at $x=0$. Now, we check differentiability at $x=0$
$$
\begin{gathered}
x+|y|=2 y \Rightarrow x+y=2 y, y \geq 0 \\
x-y=2 y, y < 0
\end{gathered}
$$
Thus, $f(x)=\left\{\begin{array}{ll}x, & y < 0 \\ x / 3, & y \geq 0\end{array}\right\}$

$$
\begin{aligned}
& \text { Now, L.H.D. }=\lim _{h \rightarrow 0^{-}} \frac{f(x+h-) f x}{-h}(\quad) \\
& =\lim _{h \rightarrow 0^{-}} \frac{x+h-x}{-h}=-1 \\
& \text { R.H.D }=\lim _{h \rightarrow 0^{+}} \frac{f(x+h-) f x}{h}(\quad) \\
& =\lim _{h \rightarrow 0^{+}} \frac{\frac{x+h}{3}-\frac{x}{3}}{h}=\lim _{h \rightarrow 0^{+}} \frac{1}{3}=\frac{1}{3} \\
&
\end{aligned}
$$
Since, L.H.D $\neq$ R.H.D. at $x=0$
$\therefore$ given function is not differentiable at $x=0$

</details>

---

### Q76. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `2`

Consider the function $f(x)=|x-2|+|x-5|, x \in R$.
Statement $1$: $f^{\prime}(4)=0$
Statement $2$: $f$ is continuous in $[2,5]$, differentiable in $(2,5)$ and $f(2)=f(5)$.

**Options:**

- **(A)** Statement $1$ is false, statement $2$ is true
- **(B)** Statement $1$ is true, statement $2$ is true; statement $2$ is a correct explanation for statement $1$
- **(C)** Statement $1$ is true, statement $2$ is true; statement $2$ is not a correct explanation for statement $1$
- **(D)** Statement $1$ is true, statement $2$ is false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement $1$ is true, statement $2$ is true; statement $2$ is a correct explanation for statement $1$**

**Detailed Solution:**

$f(x) =7-2 x ; x < 2$ 
$=3$ ; $\quad2 \leq x \leq 5$ 
$=2 x-7 ; x>5$
$f(x)$ is constant function in $[2,5]$
$f$ is continuous in $[2,5]$ and differentiable in $(2,5)$ and $f(2)=f(5)$
by Rolle's theorem $f^{\prime}(4)=0$
$\therefore$ Statement $2$ and statement $1$ both are true and statement $2$ is correct explanation for statement $1$.

</details>

---

### Q77. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=x|x|$ and $g(x)=\sin x$.
Statement-1 : gof is differentiable at $x=0$ and its derivative is continuous at that point.
Statement-2 : gof is twice differentiable at $x=0$.

**Options:**

- **(A)** Statement-1 is true, Statement-2 is true; Statement-2 is a correct explanation for Statement-1
- **(B)** Statement-1 is true, Statement-2 is true; Statement-2 is not a correct explanation for Statement-1
- **(C)** Statement-1 is true, Statement-2 is false
- **(D)** Statement-1 is false, Statement-2 is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement-1 is true, Statement-2 is false**

**Detailed Solution:**

$$
\begin{aligned}
& f(x)=x|x| \text { and } g(x)=\sin x \\
& g \circ f(x)=\sin (x|x|)=\left\{\begin{array}{cc}
-\sin x^2 & , x < 0 \\
\sin x^2 & , x \geq 0
\end{array}\right. \\
& \therefore \text { (gof })^{\prime}(x)=\left\{\begin{array}{cc}
-2 x \cos x^2 & , x < 0 \\
2 x \cos x^2 & , x \geq 0
\end{array}\right.
\end{aligned}
$$
Clearly, L(gof )' $(0)=0=\mathrm{R}(\text { gof })^{\prime}(0)$
$\therefore$ gof is differentiable at $x=0$ and also its derivative is continuous at $x=0$
$$
\begin{aligned}
& \text { Now, (gof)" }(\mathrm{x})=\left\{\begin{array}{cc}
-2 \cos \mathrm{x}^2+4 \mathrm{x}^2 \sin \mathrm{x}^2 & , \mathrm{x} < 0 \\
2 \cos \mathrm{x}^2-4 \mathrm{x}^2 \sin \mathrm{x}^2 & , \mathrm{x} \geq 0
\end{array}\right. \\
& \therefore \mathrm{L}(\text { gof })^{\prime \prime}(0)=-2 \text { and } \mathrm{R}(\text { gof })^{\prime \prime}(0)=2 \\
& \therefore \mathrm{L}(\text { gof })^{\prime \prime}(0) \neq \mathrm{R}(\text { gof })^{\prime \prime}(0)
\end{aligned}
$$
$\therefore g o f(x)$ is not twice differentiable at $x=0$.

</details>

---

### Q78. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=\left\{\begin{array}{ll}(x-1) \sin \left(\frac{1}{x-1}\right), & \text { if } x \neq 1 \\ 0, & \text { if } x=1\end{array}\right.$. Then which one of the following is true?

**Options:**

- **(A)** $f$ is neither differentiable at $x=0$ nor at $x=1$
- **(B)** $f$ is differentiable at $x=0$ and at $x=1$
- **(C)** $\mathrm{f}$ is differentiable at $\mathrm{x}=0$ but not at $\mathrm{x}=1$
- **(D)** $\mathrm{f}$ is differentiable at $\mathrm{x}=1$ but not at $\mathrm{x}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $f$ is neither differentiable at $x=0$ nor at $x=1$**

**Detailed Solution:**

$$
f^{\prime}(1)=\lim _{h \rightarrow 0} \frac{f(1+h)-f(1)}{h}
$$

$$
\begin{aligned}
& \Rightarrow f^{\prime}(1)=\lim _{h \rightarrow 0} \frac{(1+h-1) \sin \left(\frac{1}{1+h-1}\right)-0}{h}=\lim _{h \rightarrow 0} \frac{h}{h} \sin \left(\frac{1}{h}\right) \\
& \Rightarrow f^{\prime}(1)=\lim _{h \rightarrow 0} \sin \left(\frac{1}{h}\right)
\end{aligned}
$$
$\therefore \mathrm{f}$ is not differentiable at $x=1$.
Similarly, $f^{\prime}(0)=\lim _{h \rightarrow 0} \frac{f(h)-f(0)}{h}$ $\Rightarrow f^{\prime}(0)=\lim _{h \rightarrow 0} \frac{(h-1) \sin \left(\frac{1}{h-1}\right)-\sin (1)}{h}$
$\Rightarrow \mathrm{f}$ is also not differentiable at $\mathrm{x}=0$.

</details>

---

### Q79. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

Let $f: R \rightarrow R$ be a function defined by $f(x)=\operatorname{Min}\{x+1,|x|+1\}$. Then which of the following is true?

**Options:**

- **(A)** $f(x) \geq 1$ for all $x \in R$
- **(B)** $f(x)$ is not differentiable at $x=1$
- **(C)** $f(x)$ is differentiable everywhere
- **(D)** $f(x)$ is not differentiable at $x=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $f(x)$ is differentiable everywhere**

**Detailed Solution:**

$f(x)=\min \{x+1,|x|+1\}$
$f(x)=x+1 \forall x \in R$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/PM6pTJ_Cv1cfSaOXPCyxKRt8G3SnRBjS7rvYa2iBQgc.original.fullsize.png">

</details>

---

### Q80. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

The set of points where $f(x)=\frac{x}{1+|x|}$ is differentiable is

**Options:**

- **(A)** $(-\infty, 0) \cup(0, \infty)$
- **(B)** $(-\infty,-1) \cup(-1, \infty)$
- **(C)** $(-\infty, \infty)$
- **(D)** $(0, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(-\infty, \infty)$**

**Detailed Solution:**

$$
f(x)=\left\{\begin{array}{ll}
\frac{x}{1-x}, & x < 0 \\
\frac{x}{1+x}, & x \geq 0
\end{array} \quad \Rightarrow f^{\prime}(x)= \begin{cases}\frac{1}{(1-x)^2}, & x < 0 \\
\frac{1}{(1+x)^2}, & x \geq 0\end{cases}\right.
$$
$\therefore f^{\prime}(x)$ exist at everywhere.

</details>

---

### Q81. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)= \begin{cases}x e^{-\left(\frac{1}{|x|}+\frac{1}{x}\right)}, & x \neq 0 \text { then } f(x) \text { is } \\ 0 & , x=0\end{cases}$

**Options:**

- **(A)** discontinuous every where
- **(B)** continuous as well as differentiable for all $x$
- **(C)** continuous for all $x$ but not differentiable at $x=0$
- **(D)** neither differentiable nor continuous at $x=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) continuous for all $x$ but not differentiable at $x=0$**

**Detailed Solution:**

$f(0)=0 ; f(x)=x e^{-\left(\frac{1}{|x|}+\frac{1}{x}\right)}$
R.H.L. $\lim _{h \rightarrow 0}(0+h) \mathrm{e}^{-2 / h}=\lim _{h \rightarrow 0} \frac{h}{\mathrm{e}^{2 / h}}=0$
L.H.L $\operatorname{Lim}_{h \rightarrow 0}(0-h) e^{-\left(\frac{1}{h}-\frac{1}{h}\right)}=0$
Therefore, $f(x)$ is continuous
R.H.D. $\lim _{h \rightarrow 0} \frac{(0+h) e^{-\left(\frac{1}{h}+\frac{1}{h}\right)}-h e^{-\left(\frac{1}{h}+\frac{1}{h}\right)}}{h}=0$
L.H.D. $\operatorname{Lim}_{h \rightarrow 0} \frac{(0-h) \mathrm{e}^{-\left(\frac{1}{h}-\frac{1}{h}\right)}-h e^{-\left(\frac{1}{h}+\frac{1}{h}\right)}}{-h}=1$
Therefore, L.H.D. $\neq$ R.H.D.
$\mathrm{f}(\mathrm{x})$ is not differentiable at $\mathrm{x}=0$.

</details>

---

