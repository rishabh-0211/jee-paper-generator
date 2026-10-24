# JEE Advanced Mathematics - Area Under Curves

## Topic 2: Area bounded by two curves

**Total Questions:** 9

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `3`

<strong>Passage:</strong> Consider the ellipses given by $x^2 + 4y^2 = 1$ and $4x^2 + y^2 = 1$.

<strong>Question:</strong> If $\alpha$ is the area of the common region that lies inside both the given ellipses, then the value of $\cot\alpha$ is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.75**

**Detailed Solution:**

The given ellipses are $E_1: x^2 + 4y^2 = 1$ and $E_2: 4x^2 + y^2 = 1$.

By symmetry, the common region is symmetric about both the coordinate axes and the lines $y = x$ and $y = -x$. The total area $\alpha$ is $8$ times the area of the region in the first quadrant bounded by $\theta = 0$ and $\theta = \dfrac{\pi}{4}$.

In polar coordinates, substituting $x = r\cos\theta$ and $y = r\sin\theta$ into the equation of $E_2$ (which is the inner boundary for $0 \le \theta \le \dfrac{\pi}{4}$), we get:
$4r^2\cos^2\theta + r^2\sin^2\theta = 1 \Rightarrow r^2 = \dfrac{1}{4\cos^2\theta + \sin^2\theta}$

The area of this sector is given by:
$A = \dfrac{1}{2} \int_{0}^{\dfrac{\pi}{4}} r^2 d\theta = \dfrac{1}{2} \int_{0}^{\dfrac{\pi}{4}} \dfrac{1}{4\cos^2\theta + \sin^2\theta} d\theta$

Dividing the numerator and the denominator by $\cos^2\theta$:
$A = \dfrac{1}{2} \int_{0}^{\dfrac{\pi}{4}} \dfrac{\sec^2\theta}{4 + \tan^2\theta} d\theta$

Substituting $t = \tan\theta$, we have $dt = \sec^2\theta d\theta$. The limits change from $0$ to $1$:
$A = \dfrac{1}{2} \int_{0}^{1} \dfrac{dt}{4 + t^2} = \dfrac{1}{2} \left[ \dfrac{1}{2} \arctan\left(\dfrac{t}{2}\right) \right]_{0}^{1} = \dfrac{1}{4} \arctan\left(\dfrac{1}{2}\right)$

The total area $\alpha$ of the common region is:
$\alpha = 8A = 8 \times \dfrac{1}{4} \arctan\left(\dfrac{1}{2}\right) = 2 \arctan\left(\dfrac{1}{2}\right)$

We need to find the value of $\cot\alpha$:
$\cot\alpha = \cot\left(2 \arctan\left(\dfrac{1}{2}\right)\right)$

Let $\phi = \arctan\left(\dfrac{1}{2}\right)$, which implies $\tan\phi = \dfrac{1}{2}$.

Using the double angle formula for tangent:
$\tan(2\phi) = \dfrac{2\tan\phi}{1 - \tan^2\phi} = \dfrac{2 \left(\dfrac{1}{2}\right)}{1 - \left(\dfrac{1}{2}\right)^2} = \dfrac{1}{1 - \dfrac{1}{4}} = \dfrac{4}{3}$

Therefore, $\cot\alpha = \dfrac{1}{\tan(2\phi)} = \dfrac{3}{4}$.

Answer: $3/4$

</details>

---

### Q2. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `3`

<strong>Passage:</strong> Consider the curve $C_1$ given by $y = e^{-x}$ for $x \in [0, 10\pi]$, and the curve $C_2$ given by $y = e^{-x}(\sin x + \cos x)$ for $x \in [0, 10\pi]$. Let $n$ be the total number of points of intersection of the curves $C_1$ and $C_2$. Suppose that $\alpha_1, \alpha_2, \ldots, \alpha_n \in [0, 10\pi]$ are the $x$-coordinates of the points of intersection of the curves $C_1$ and $C_2$ such that $\alpha_1 < \alpha_2 < \cdots < \alpha_n$.

<strong>Question:</strong> Let $\beta$ be the area of the region enclosed between the curves $C_1$, $C_2$, and the lines $x = \alpha_1$ and $x = \alpha_4$. Then the value of $-\dfrac{1}{\pi}\log_e\left(\beta - 2 e^{-\frac{\pi}{2}}\right)$ is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2.5**

**Detailed Solution:**

To find the points of intersection of the curves $C_1$ and $C_2$, we equate their equations:

$e^{-x} = e^{-x}(\sin x + \cos x)$

Since $e^{-x} \neq 0$, we have:

$\sin x + \cos x = 1$

$\Rightarrow \sqrt{2}\sin\left(x + \dfrac{\pi}{4}\right) = 1 \Rightarrow \sin\left(x + \dfrac{\pi}{4}\right) = \dfrac{1}{\sqrt{2}}$

The general solution is $x + \dfrac{\pi}{4} = 2k\pi + \dfrac{\pi}{4}$ or $x + \dfrac{\pi}{4} = 2k\pi + \dfrac{3\pi}{4}$ for any integer $k$.

Thus, $x = 2k\pi$ or $x = 2k\pi + \dfrac{\pi}{2}$.

For $x \in [0, 10\pi]$, the first four points of intersection are:

$\alpha_1 = 0$

$\alpha_2 = \dfrac{\pi}{2}$

$\alpha_3 = 2\pi$

$\alpha_4 = 2\pi + \dfrac{\pi}{2} = \dfrac{5\pi}{2}$

The area $\beta$ enclosed between the curves from $x = \alpha_1$ to $x = \alpha_4$ is given by:

$\beta = \int_{0}^{\dfrac{5\pi}{2}} |e^{-x}(\sin x + \cos x - 1)| dx$

We analyze the sign of $\sin x + \cos x - 1$ in the intervals $(0, \dfrac{\pi}{2})$, $(\dfrac{\pi}{2}, 2\pi)$, and $(2\pi, \dfrac{5\pi}{2})$:

For $x \in (0, \dfrac{\pi}{2})$, $\sin x + \cos x > 1$

For $x \in (\dfrac{\pi}{2}, 2\pi)$, $\sin x + \cos x < 1$

For $x \in (2\pi, \dfrac{5\pi}{2})$, $\sin x + \cos x > 1$

Let $I = \int e^{-x}(\sin x + \cos x - 1) dx$. Using integration by parts or standard formulas, we get:

$\int e^{-x}\sin x dx = -\dfrac{e^{-x}}{2}(\sin x + \cos x)$

$\int e^{-x}\cos x dx = \dfrac{e^{-x}}{2}(\sin x - \cos x)$

$\Rightarrow \int e^{-x}(\sin x + \cos x) dx = -e^{-x}\cos x$

Thus, $I = -e^{-x}\cos x + e^{-x} = e^{-x}(1 - \cos x)$.

Now, we evaluate the area $\beta$ by splitting the integral:

$\beta = \int_{0}^{\dfrac{\pi}{2}} e^{-x}(\sin x + \cos x - 1) dx - \int_{\dfrac{\pi}{2}}^{2\pi} e^{-x}(\sin x + \cos x - 1) dx + \int_{2\pi}^{\dfrac{5\pi}{2}} e^{-x}(\sin x + \cos x - 1) dx$

$\beta = \left[ e^{-x}(1 - \cos x) \right]_{0}^{\dfrac{\pi}{2}} - \left[ e^{-x}(1 - \cos x) \right]_{\dfrac{\pi}{2}}^{2\pi} + \left[ e^{-x}(1 - \cos x) \right]_{2\pi}^{\dfrac{5\pi}{2}}$

$\beta = (e^{-\dfrac{\pi}{2}} - 0) - (0 - e^{-\dfrac{\pi}{2}}) + (e^{-\dfrac{5\pi}{2}} - 0)$

$\beta = 2e^{-\dfrac{\pi}{2}} + e^{-\dfrac{5\pi}{2}}$

We are required to find the value of $-\dfrac{1}{\pi}\log_e\left(\beta - 2 e^{-\dfrac{\pi}{2}}\right)$:

$\beta - 2 e^{-\dfrac{\pi}{2}} = e^{-\dfrac{5\pi}{2}}$

$\Rightarrow -\dfrac{1}{\pi}\log_e\left(e^{-\dfrac{5\pi}{2}}\right) = -\dfrac{1}{\pi} \times \left(-\dfrac{5\pi}{2}\right) = \dfrac{5}{2} = 2.5$

Answer: $2.5$

</details>

---

### Q3. JEE Advanced 2025 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathbb{R}$ denote the set of all real numbers. Then the area of the region $\left\{(x, y) \in \mathbb{R} \times \mathbb{R}: x>0, y>\frac{1}{x}, 5 x-4 y-1>0,4 x+4 y-17 <0\right\}$ is

**Options:**

- **(A)** $\frac{17}{16}-\log _e 4$
- **(B)** $\frac{33}{8}-\log _e 4$
- **(C)** $\frac{57}{8}-\log _e 4$
- **(D)** $\frac{17}{2}-\log _e 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{33}{8}-\log _e 4$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/21e79ZxJxfmDejluRgh9UOVAR60QJelNraOiDENbnmw.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/KmSajaHLiIgRQnUz4DtDJVGZSC0F5zf9b7Rg1s_7PnU.original.fullsize.png">
Area $=\frac{13}{8}+\frac{20}{8}-\log _e 4=\left(\frac{33}{8}-\log _e 4\right)$

</details>

---

### Q4. JEE Advanced 2023 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math> be the function defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>5</mn><mn>9</mn></mfrac><mi>x</mi><mo>+</mo><mfrac><mn>17</mn><mn>36</mn></mfrac></math>. Consider the square region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>S</mi><mo>:</mo><mi>y</mi><mo>&#62;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> be called the green region and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>S</mi><mo>:</mo><mi>y</mi><mo>&#60;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> be called the red region. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>h</mi></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>h</mi></mrow></mfenced><mo>&#8712;</mo><mi>S</mi><mo>:</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math> be the horizontal line drawn at a height <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>. Then which of the following statements is(are) true?

**Options:**

- **(A)** <p>There exists an<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced></math> such that the area of the green region above the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>h</mi></msub></math> equals the area of the green region below the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>h</mi></msub></math></p>
- **(B)** There exists an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced></math> such that the area of the red region above the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>h</mi></msub></math> equals the area of the red region below the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>h</mi></msub></math>
- **(C)** There exists an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced></math> such that the area of the green region above the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>h</mi></msub></math> equals the area of the red region below the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>h</mi></msub></math>
- **(D)** There exists an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced></math> such that the area of the red region above the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>h</mi></msub></math> equals the area of the green region below the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>h</mi></msub></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) There exists an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced></math> such that the area of the red region above the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>h</mi></msub></math> equals the area of the green region below the line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>h</mi></msub></math>**

**Detailed Solution:**

<p>Given,</p><p>Function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>5</mn><mn>9</mn></mfrac><mi>x</mi><mo>+</mo><mfrac><mn>17</mn><mn>36</mn></mfrac></math></p><p>Square region <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p>Green region given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>S</mi><mo>:</mo><mi>y</mi><mo>&#62;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p>Red region is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>S</mi><mo>:</mo><mi>y</mi><mo>&#60;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mi>h</mi></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>h</mi></mrow></mfenced><mo>&#8712;</mo><mi>S</mi><mo>:</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math> be the horizontal line drawn at a height <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p>Now plotting the diagram of the above function we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/a3440f96-6c5e-4bef-afa8-d37d1e5fd2d0.png" style="width: 300px; height: 246px;" /></p><p>Now differentiating the function,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>5</mn><mn>9</mn></mfrac><mi>x</mi><mo>+</mo><mfrac><mn>17</mn><mn>36</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mfrac><mn>5</mn><mn>9</mn></mfrac></math></p><p>For maxima/minima, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Now finding the area of red region we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>R</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So, area of the green region will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>G</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>, as total area is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> sq.unit</p><p>Now solving option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">A</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mi>h</mi><mo>=</mo><mi>h</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mi>h</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#62;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>So, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">A</mi></mfenced></math> is incorrect</p><p>For option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">B</mi></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mi>h</mi><mo>&#8658;</mo><mi>h</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p>So, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">B</mi></mfenced></math> is correct as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p>Now solving option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">C</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>h</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">C</mi></mfenced></math> is correct.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">D</mi></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math> Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">C</mi></mfenced></math> is correct <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">D</mi></mfenced></math> is also correct.</p>

</details>

---

### Q5. JEE Advanced 2019 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

The area of the region <math><mfenced close="}" open="{" separators="|"><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi><mo>,</mo><mi mathvariant="normal">y</mi></mrow></mfenced><mo>:</mo><mi mathvariant="normal">x</mi><mi mathvariant="normal">y</mi><mo>&#8804;</mo><mn>8</mn><mo>,</mo><mi mathvariant="normal">&#160;</mi><mn>1</mn><mo>&#8804;</mo><mi mathvariant="normal">y</mi><mo>&#8804;</mo><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math> is

**Options:**

- **(A)** <math><mn>16</mn><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mn>2</mn><mo>-</mo><mfrac><mrow><mn>14</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mrow></math>
- **(B)** <math><mn>8</mn><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mn>2</mn><mo>-</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mrow></math>
- **(C)** <math><mn>8</mn><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mn>2</mn><mo>-</mo><mfrac><mrow><mn>14</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mrow></math>
- **(D)** <math><mn>16</mn><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mn>2</mn><mo>-</mo><mn>6</mn></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>16</mn><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mn>2</mn><mo>-</mo><mfrac><mrow><mn>14</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mrow></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/cwbmsusgjqhdrjaqfmwqkaqbhfkycqbbpofozssoivqjnnodkr.png"/>
To draw the inequality, let us draw the equation
<math><mi>x</mi><mi>y</mi><mo>=</mo><mn>8</mn></math> and <math><mi>y</mi><mo>=</mo><mn>1</mn></math> and <math><mi>y</mi><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
For point of intersection
(i) <math><mi>x</mi><mi>y</mi><mo>=</mo><mn>8</mn></math> and <math><mi>y</mi><mo>=</mo><mn>1</mn><mo>⇒</mo><mi>A</mi><mo>(</mo><mn>8,1</mn><mo>)</mo></math>
(ii) <math><mi>x</mi><mi>y</mi><mo>=</mo><mn>8</mn></math> and <math><mi>y</mi><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi> </mi><mo>⇒</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>=</mo><mn>8</mn><mi> </mi><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>2</mn><mi> </mi><mo>⇒</mo><mi>B</mi><mo>(</mo><mn>2</mn><mo>,</mo><mi> </mi><mn>4</mn><mo>)</mo></math>
(iii) <math><mi>y</mi><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> and <math><mi>y</mi><mo>=</mo><mn>1</mn><mo>⇒</mo><mi>C</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mn>1</mn></mrow></mfenced></math> and <math><mi>D</mi><mfenced separators="|"><mrow><mi> </mi><mn>1</mn><mo>,</mo><mi> </mi><mn>1</mn></mrow></mfenced></math>
Now <math><mi>x</mi><mi>y</mi><mo>≤</mo><mn>8</mn><mo>⇒</mo></math> region which contains origin
<math><mi>y</mi><mo>≥</mo><mn>1</mn><mo>⇒</mo></math> region above line <math><mi>y</mi><mo>=</mo><mn>1</mn></math>
<math><mi>y</mi><mo>≤</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>⇒</mo></math> region outside the parabola
Now required area
Method I:
Using x-axis:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><munderover><mo stretchy="true">∫</mo><mn>1</mn><mn>2</mn></munderover><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>⋅</mo><mi>d</mi><mi>x</mi><mo>+</mo><munderover><mo stretchy="true">∫</mo><mn>2</mn><mn>8</mn></munderover><mfenced separators="|"><mrow><mfrac><mn>8</mn><mi>x</mi></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mo>⋅</mo><mi>d</mi><mi>x</mi></math>
<math><mi>A</mi><mo>=</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mn>8</mn><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow><mrow><mn>8</mn></mrow></msubsup></math>
<math><mi>A</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>14</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mn>16</mn><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mn>2</mn></math>
Method II:
Using y-axis:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><munderover><mo stretchy="true">∫</mo><mn>1</mn><mn>4</mn></munderover><mfenced separators="|"><mrow><mfrac><mn>8</mn><mi>y</mi></mfrac><mo>-</mo><msqrt><mi>y</mi></msqrt></mrow></mfenced><mo>⋅</mo><mi>d</mi><mi>y</mi></math>
<math><mi>A</mi><mo>=</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mn>8</mn><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mi>y</mi><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msup><mrow><mi>y</mi></mrow><mrow><mfrac bevelled="true"><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></msubsup><mo>⇒</mo><mi>A</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>14</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mn>16</mn><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mn>2</mn></math>
Note: The question should include bounded area term as in <math><msup><mrow><mn>2</mn></mrow><mrow><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi></mrow></msup></math> quadrant there exist a area which satisfy the inequality and is unbounded.

</details>

---

### Q6. JEE Advanced 2018 (Paper 1)

*Type:* `numerical` | *Level:* `1`

A farmer <math><msub><mrow><mi>F</mi></mrow><mrow><mn>1</mn></mrow></msub></math> has a land in the shape of a triangle with vertices at <math><mi>P</mi><mo>(</mo><mn>0, 0</mn><mo>)</mo><mo>,</mo><mi>Q</mi><mo>(</mo><mn>1, 1</mn><mo>)</mo></math> and <math> <mi>R</mi><mo>(</mo><mn>2, 0</mn><mo>)</mo><mo>.</mo></math> From this land, a neighbouring farmer <math><msub><mrow><mi>F</mi></mrow><mrow><mn>2</mn></mrow></msub></math> takes away the region which lies between the side <math><mi>P</mi><mi>Q</mi></math> and a curve of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mi>n</mi></msup><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#62;</mo><mn>1</mn></math>. If the area of the region taken away by the farmer <math><msub><mrow><mi>F</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is exactly <math> <mrow> <mn>30%</mn> </mrow> </math> of the area of <math><mo>&#8710;</mo><mi>P</mi><mi>Q</mi><mi>R</mi><mo>,</mo></math> then the value of <math> <mi>n</mi> </math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/wwtfwinnnqffqrvboqskhnaazwphrqxvpzuklhcdbezuudeyyl.jpeg"/>
Area <math><mo>=</mo><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></mfrac></mrow></mrow></math>
<math><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math>
<math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math> <math><mo>∴</mo><mi> </mi><mi> </mi><mi>n</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>5</mn></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi>n</mi><mo>=</mo><mn>4</mn></math>

</details>

---

### Q7. JEE Advanced 2017 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

If the line <math><mi>x</mi><mo>=</mo><mi>&#945;</mi></math> divides the area of the region <math><mi>R</mi><mo>=</mo><mo>{</mo><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>:</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mi>x</mi><mo>,</mo><mi>&#160;</mi><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn><mo>}</mo></math> into two equal parts, then

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&lt;</mo><mi>α</mi><mo>&lt;</mo><mn>1</mn></math>
- **(B)** <math><msup><mrow><mi>α</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>4</mn><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mn>0</mn><mo>&lt;</mo><mi>α</mi><mo>≤</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mn>2</mn><msup><mrow><mi>α</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mn>4</mn><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>2</mn><msup><mrow><mi>α</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mn>4</mn><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/49_solu_chem_pa_2.jpg"/></p><p><math><mi>A</mi><mo>=</mo><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math></p><p>Area of curvilinear triangle <math><mi>O</mi><mi>P</mi><mi>Q</mi><mo>=</mo><mfrac><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math></p><p><math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mi>1</mi></mrow></munderover><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac><mi> </mi><mo>⇒</mo><mi> </mi><mi> </mi><mn>2</mn><msup><mrow><mi>α</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mn>4</mn><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi><mo>⇒</mo><mi> </mi><mi> </mi><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p>so α lies between 0.5 and 1

</details>

---

### Q8. JEE Advanced 2016 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><msup><mi>R</mi><mn>2</mn></msup><mo>:</mo><mo>&#160;</mo><mi>y</mi><mo>&#8805;</mo><msqrt><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></msqrt><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>y</mi><mo>&#8804;</mo><mi>x</mi><mo>+</mo><mn>9</mn><mo>&#8804;</mo><mn>15</mn><mo>}</mo></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>If <math> <mi>x</mi><mo>+</mo><mn>3</mn><mo><</mo><mn>0</mn><mo>⇒</mo><mi>y</mi><mo>≥</mo><msqrt> <mrow> <mo>−</mo><mo stretchy="false">(</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo stretchy="false">)</mo> </mrow> </msqrt> <mtext> </mtext><mtext> </mtext><mtext> </mtext><mo>&</mo><mi> y</mi><mo>≥</mo><mn>0</mn> </math>
If <math> <mi>x</mi><mo>+</mo><mn>3</mn><mo>≥</mo><mn>0</mn><mo>⇒</mo><mi>y</mi><mo>≥</mo><msqrt> <mrow> <mo stretchy="false">(</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo stretchy="false">)</mo> </mrow> </msqrt> <mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mo>&</mo><mi> y</mi><mo>≥</mo><mn>0</mn> </math>
Also
<math> <mn>5</mn><mi>y</mi><mo>≤</mo><mi>x</mi><mo>+</mo><mn>9</mn><mo>≤</mo><mn>15</mn> </math>
<math> <mo>⇒</mo><mi>x</mi><mo>−</mo><mn>5</mn><mi>y</mi><mo>+</mo><mn>9</mn><mo>≥</mo><mn>0</mn><mtext> </mtext><mtext> </mtext><mtext> </mtext><mo>&</mo><mtext> </mtext><mtext> </mtext><mtext> </mtext><mi>x</mi><mo>≤</mo><mn>6</mn> </math>
Intersection point of line & parabolas
<math> <mn>5</mn><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>9</mn><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mo>&</mo><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><msup> <mi>y</mi> <mn>2</mn> </msup> <mo>=</mo><mrow><mo>|</mo> <mrow> <mi>x</mi><mo>+</mo><mn>3</mn> </mrow> <mo>|</mo></mrow><mtext> </mtext><mo stretchy="false">(</mo><mi>y</mi><mo>≥</mo><mn>0</mn><mo stretchy="false">)</mo> </math>
<math> <msup> <mrow><mo>(</mo> <mrow> <mfrac> <mrow> <mi>x</mi><mo>+</mo><mn>9</mn> </mrow> <mn>5</mn> </mfrac> </mrow> <mo>)</mo></mrow> <mn>2</mn> </msup> <mo>=</mo><mrow><mo>|</mo> <mrow> <mi>x</mi><mo>+</mo><mn>3</mn> </mrow> <mo>|</mo></mrow> </math>
<math> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>18</mn><mi>x</mi><mo>+</mo><mn>81</mn><mo>=</mo><mn>25</mn><mi>x</mi><mo>+</mo><mn>75</mn><mtext> </mtext><mtext> </mtext><mi>o</mi><mi>r</mi><mtext> </mtext><mtext> </mtext><mo>−</mo><mn>25</mn><mi>x</mi><mo>−</mo><mn>75</mn> </math>
<math> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>−</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn><mtext> </mtext><mtext> </mtext><mi>o</mi><mi>r</mi><mtext> </mtext><mtext> </mtext><msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>43</mn><mi>x</mi><mo>+</mo><mn>156</mn><mo>=</mo><mn>0</mn> </math>
<math> <mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>6</mn><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mi>o</mi><mi>r</mi><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mi>x</mi><mo>=</mo><mo>−</mo><mn>39</mn><mo>,</mo><mo>−</mo><mn>4</mn> </math>
So Clearly,  <math> <mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>2</mn> </math>
and when  <math> <mi>x</mi><mo>=</mo><mo>−</mo><mn>4</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>1</mn> </math> are required points
Drawing all these, we get this graph.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/Maths_38_solu.jpg"/>
Shaded portion is required area.
Clearly required area = area (trapezium ABCD) - <math><mfenced separators="|"><mrow><msub><mrow><mi>A</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced></math> .......(i)
area (trapezium ABCD) <math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>5</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><msub><mrow><mi>A</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mo>-</mo><mn>4</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></munderover><mrow><msqrt><mo>-</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></msqrt></mrow></mrow><mi>d</mi><mi>x</mi></math>
<math><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
and <math><msub><mrow><mi>A</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mo>-</mo><mn>3</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>16</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mo>∴</mo></math> From equation (i), we get required area <math><mo>=</mo><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>16</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math></p>

</details>

---

### Q9. JEE Advanced 2013 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>The area enclosed by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></math> and <math> <mrow> <mtext>y</mtext> <mo>=</mo> <mfenced close="|" open="|" separators=","> <mrow> <mtext>cos x</mtext> <mo>-</mo> <mtext>sin x</mtext> </mrow> </mfenced> </mrow> </math> over the interval <math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <mn>0</mn> <mtext>,</mtext> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math> is</p>

**Options:**

- **(A)** <math><mrow>  <mn>4</mn>  <mfenced open="(" close=")" separators=",">    <mrow>      <msqrt>        <mn>2</mn>      </msqrt>      <mo>-</mo>      <mn>1</mn>    </mrow>  </mfenced></mrow></math>
- **(B)** <math> <mrow> <mn>2</mn> <msqrt> <mn>2</mn> </msqrt> <mfenced close=")" open="(" separators=","> <mrow> <msqrt> <mn>2</mn> </msqrt> <mo>-</mo> <mn>1</mn> </mrow> </mfenced> </mrow> </math>
- **(C)** <math><mrow>  <mn>2</mn>  <mfenced open="(" close=")" separators=",">    <mrow>      <msqrt>        <mn>2</mn>      </msqrt>      <mo>+</mo>      <mn>1</mn>    </mrow>  </mfenced></mrow></math>
- **(D)** <math><mrow>  <mn>2</mn>  <msqrt>    <mn>2</mn>  </msqrt>  <mfenced open="(" close=")" separators=",">    <mrow>      <msqrt>        <mn>2</mn>      </msqrt>      <mo>+</mo>      <mn>1</mn>    </mrow>  </mfenced></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math> <mrow> <mn>2</mn> <msqrt> <mn>2</mn> </msqrt> <mfenced close=")" open="(" separators=","> <mrow> <msqrt> <mn>2</mn> </msqrt> <mo>-</mo> <mn>1</mn> </mrow> </mfenced> </mrow> </math>**

**Detailed Solution:**

<p>The given curves are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></math></p><p><math> <mrow> <msub> <mtext>y</mtext> <mn>1</mn> </msub> <mo>=</mo> <mtext>sin x</mtext> <mo>+</mo> <mtext>cos x</mtext> <mo>=</mo> <msqrt> <mn>2</mn> </msqrt> <mtext>&#160;sin</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mtext>x</mtext> <mo>+</mo> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>
<math> <mrow> <msub> <mtext>y</mtext> <mn>2</mn> </msub> <mo>=</mo> <msqrt> <mn>2</mn> </msqrt> <mo>|</mo> <mtext>sin</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mo>-</mo> <mtext>x</mtext> </mrow> </mfenced> <mo>|</mo> </mrow> </math>
So, Required Area<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mfenced><mrow><mfenced><mrow><mtext>sin x</mtext><mo>+</mo><mtext>cos x</mtext></mrow></mfenced><mo>-</mo><mfenced><mrow><mtext>cos x</mtext><mo>-</mo><mtext>sin x</mtext></mrow></mfenced></mrow></mfenced><mtext>dx</mtext><mo>+</mo><munderover><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></munderover><mfenced><mrow><mfenced><mrow><mtext>sin x</mtext><mo>+</mo><mtext>cos x</mtext></mrow></mfenced><mo>-</mo><mfenced><mrow><mtext>sin x</mtext><mo>-</mo><mtext>cos x</mtext></mrow></mfenced></mrow></mfenced><mtext>dx</mtext></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></msubsup><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math>.</p>

</details>

---

