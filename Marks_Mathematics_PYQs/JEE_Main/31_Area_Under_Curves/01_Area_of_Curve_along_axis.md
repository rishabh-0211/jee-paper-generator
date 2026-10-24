# JEE Main Mathematics - Area Under Curves

## Topic 1: Area of Curve along axis

**Total Questions:** 16

---

### Q1. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The area of the region $\{(x, y): y \leq \pi - |x|, y \leq |x \sin x|, y \geq 0\}$ is:

**Options:**

- **(A)** $1 + \dfrac{\pi^2}{8}$
- **(B)** $2 + \dfrac{\pi^2}{4}$
- **(C)** $\dfrac{\pi^2}{8} - 1$
- **(D)** $4 + \dfrac{\pi^2}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 + \dfrac{\pi^2}{4}$**

**Detailed Solution:**

The given region is defined by the inequalities $y \leq \pi - |x|$, $y \leq |x \sin x|$, and $y \geq 0$.

Since replacing $x$ with $-x$ leaves the inequalities unchanged, the region is symmetric with respect to the y-axis. We can find the area of the region in the first quadrant ($x \geq 0$) and multiply it by $2$.

For $x \geq 0$, the inequalities become:
$y \leq \pi - x$
$y \leq x \sin x$
$y \geq 0$

The condition $y \geq 0$ and $y \leq \pi - x$ restricts $x$ to the interval $[0, \pi]$. In this interval, $\sin x \geq 0$, so $|x \sin x| = x \sin x$.

To find the intersection of the curves $y = \pi - x$ and $y = x \sin x$, we equate them:
$x \sin x = \pi - x \Rightarrow x(1 + \sin x) = \pi$

By inspection, $x = \dfrac{\pi}{2}$ is a solution since $\dfrac{\pi}{2}(1 + 1) = \pi$.

For $x \in \left[0, \dfrac{\pi}{2}\right]$, $x \sin x \leq \pi - x$.
For $x \in \left[\dfrac{\pi}{2}, \pi\right]$, $x \sin x \geq \pi - x$.

The area in the first quadrant, $A_1$, is given by:
$A_1 = \int_{0}^{\pi/2} x \sin x \, dx + \int_{\pi/2}^{\pi} (\pi - x) \, dx$

Evaluating the first integral using integration by parts:
$\int_{0}^{\pi/2} x \sin x \, dx = [-x \cos x]_{0}^{\pi/2} - \int_{0}^{\pi/2} (-\cos x) \, dx$
$= 0 + [\sin x]_{0}^{\pi/2} = 1$

Evaluating the second integral:
$\int_{\pi/2}^{\pi} (\pi - x) \, dx = \left[ -\dfrac{(\pi - x)^2}{2} \right]_{\pi/2}^{\pi} = 0 - \left( -\dfrac{\pi^2}{8} \right) = \dfrac{\pi^2}{8}$

Thus, the area in the first quadrant is:
$A_1 = 1 + \dfrac{\pi^2}{8}$

The total area of the region is twice the area in the first quadrant:
$\text{Total Area} = 2 \times A_1 = 2 \left( 1 + \dfrac{\pi^2}{8} \right) = 2 + \dfrac{\pi^2}{4}$

Answer: $2 + \dfrac{\pi^2}{4}$

</details>

---

### Q2. JEE Main 2026 (23 January Shift 1)

*Type:* `numerical` | *Level:* `2`

Let the area of the region bounded by the curve $y=\max \{\sin x, \cos x\}$, lines $x=0, x=\frac{3 \pi}{2}$, and the $x$-axis be A. Then, $\mathrm{A}+\mathrm{A}^{2}$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/23S1_s_23_1.png">
$A = \int_{0}^{\pi/4} \cos x \, dx + \int_{\pi/4}^{\pi} \sin x \, dx + \int_{\pi}^{5\pi/4} -\sin x \, dx + \int_{5\pi/4}^{3\pi/2} -\cos x \, dx$
$A = (\sin x)_{0}^{\pi/4} + (-\cos x)_{\pi/4}^{\pi} + (\cos x)_{\pi}^{5\pi/4} + (\sin x)_{5\pi/4}^{3\pi/2}$
$A = \dfrac{1}{\sqrt{2}} + \dfrac{1}{\sqrt{2}} + 1 + 1 - \dfrac{1}{\sqrt{2}} + 1 - \dfrac{1}{\sqrt{2}} = 3$
$A^2 + A = 12$

</details>

---

### Q3. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the region enclosed by the curves $y=\mathrm{e}^x, y=\left|\mathrm{e}^x-1\right|$ and $y$-axis is:

**Options:**

- **(A)** $1-\log _{\mathrm{e}} 2$
- **(B)** $\log _{\mathrm{e}} 2$
- **(C)** $1+\log _e 2$
- **(D)** $2 \log _e 2-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1-\log _{\mathrm{e}} 2$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/g_2ptiFl2NYU6rlw74V-bVufOA8OSFmao5QJbxD1MPc.original.fullsize.png">

$\begin{aligned} & e^x=1-e^x \Rightarrow 2 e^x=1 \\ & \Rightarrow e^x=\frac{1}{2} \\ & \Rightarrow x=\ln \frac{1}{2} \\ & \int_{\ln (1 / 2)}^0\left[e^x-\left(1-e^x\right)\right] d x \\ & =\int_{\ln 2}^0\left(2 e^x-1\right) d x=2 e^x-\left.x\right|_{-\ln 2} ^0 \\ & =2-(1+\ln 2) \\ & =1-\log _e 2\end{aligned}$

</details>

---

### Q4. JEE Main 2024 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>:</mo><mn>0</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>3</mn><mo>,</mo><mn>0</mn><mo>≤</mo><mi>y</mi><mo>≤</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open=""><mrow><mi>min</mi><mfenced close="}" open="{"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>,</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>A</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **164**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>y</mi><mo>≤</mo><mi>min</mi><mfenced close="}" open="{"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>,</mo><mo> </mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>x</mi><mo>∈</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>Now, plotting the diagram of the above expression we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/29c98c15-55c8-49bd-86a5-c7995393dfc2.png" style="width: 350px; height: 228px;"/></p><p>Now, from above diagram we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mn>2</mn></msubsup><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo mathvariant="italic">d</mo><mi>x</mi><mo>+</mo><msubsup><mo>∫</mo><mn>2</mn><mn>3</mn></msubsup><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo mathvariant="italic">d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>0</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>2</mn><mn>3</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mrow><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>+</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>9</mn><mo>+</mo><mn>6</mn><mo>-</mo><mn>4</mn><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><mfrac><mn>20</mn><mn>3</mn></mfrac><mo>+</mo><mn>7</mn><mo>=</mo><mfrac><mn>41</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>12</mn><mi>A</mi><mo>=</mo><mn>164</mn></math></p>

</details>

---

### Q5. JEE Main 2024 (27 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

If the area of the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>(</mo><mi mathvariant="normal">x</mi><mo>,</mo><mi mathvariant="normal">y</mi><mo>)</mo><mo>:</mo><mn>0</mn><mo>≤</mo><mi mathvariant="normal">y</mi><mo>≤</mo><mi>min</mi><mfenced close="}" open="{"><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>,</mo><mn>6</mn><mi mathvariant="normal">x</mi><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo> </mo><mi mathvariant="normal">A</mi></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **304**

**Detailed Solution:**

<p>Solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo> </mo><mtext>and</mtext><mo> </mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>6</mn><mi mathvariant="normal">x</mi><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>=</mo><mn>6</mn><mi mathvariant="normal">x</mi><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi mathvariant="normal">x</mi><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">x</mi><mfenced><mrow><mn>4</mn><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi mathvariant="normal">x</mi><mo>,</mo><mi mathvariant="normal">y</mi></mrow></mfenced><mo>≡</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>8</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8eaf27a9-25ca-4407-b709-157d9081a739.png" style="width: 300px; height: 209px;"/></p><p>So, the required area is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>×</mo><mn>4</mn><mo>×</mo><mn>8</mn><mo>+</mo><msubsup><mo>∫</mo><mn>4</mn><mn>6</mn></msubsup><mfenced><mrow><mn>6</mn><mi mathvariant="normal">x</mi><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">A</mi><mo>=</mo><mn>16</mn><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mfrac><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mn>4</mn><mn>6</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">A</mi><mo>=</mo><mfrac><mn>76</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>12</mn><mi mathvariant="normal">A</mi><mo>=</mo><mn>304</mn></math></p>

</details>

---

### Q6. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The area of the region enclosed by the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>max</mi><mo>{</mo><mi>sin</mi><mi>x</mi><mo>,</mo><mi>cos</mi><mi>x</mi><mo>}</mo><mo>,</mo><mo>-</mo><mi>&#960;</mi><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mi>&#960;</mi></math> and the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>(</mo><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><msqrt><mn>2</mn></msqrt></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<blockquote><p>Plotting the required diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b682d0a5-b724-4eab-ab5d-4182ed86ad8e.png" style="width: 350px; height: 257px;" /></p><p>Now from diagram we can say that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi></math> is maximum for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mi mathvariant="normal">&#960;</mi><mo>,</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mi mathvariant="normal">&#960;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi></math> is maximum for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p>So, area of the region is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="|" open="|"><mrow><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>&#960;</mi></mrow><mfrac><mrow><mo>-</mo><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></msubsup><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>&#960;</mi></msubsup><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac></msubsup><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mn>2</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mn>2</mn><mo>-</mo><mfrac><mn>2</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>=</mo><mn>4</mn></math></p><p>Hence this is the required option.</p></blockquote>

</details>

---

### Q7. JEE Main 2023 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let the area enclosed by the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> and the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>min</mi><mfenced close="}" open="{"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mn>1</mn><mo>+</mo><mo>[</mo><mi>x</mi><mo>]</mo></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi></math>, be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>A</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> and the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>min</mi><mfenced close="}" open="{"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mn>1</mn><mo>+</mo><mo>[</mo><mi>x</mi><mo>]</mo></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi></math>,</p><p>Now plotting the diagram of given function we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fdb8d311-2bf4-431f-8c32-80078e0a6d92-image.png" style="width: 400px; height: 334px;" /></p><p> </p><p>Now from above diagram, the area enclosed is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#215;</mo><mn>1</mn><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>12</mn><mi>A</mi><mo>=</mo><mn>17</mn></math></p></blockquote>

</details>

---

### Q8. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The area bounded by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<blockquote><p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>3</mn><mo>-</mo><mn>2</mn><mi>x</mi><mo>:</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn><mspace linebreak="newline"></mspace><mn>1</mn><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>Let us draw diagram of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>3</mn></math> we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fffa10be-f7d1-4bd4-a9cf-a20cf2f6aaeb-image.png" style="width: 375px; height: 191px;" /></p><p>Required area is the area of trapezium which is</p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#215;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math> sq. units</p></blockquote>

</details>

---

### Q9. JEE Main 2023 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be the area bounded by the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math>, the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis and the ordinates <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi>A</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **62**

**Detailed Solution:**

<p>Plotting the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bbf502b1-ee0b-4f91-8a19-25146a46eb10-e5603b07-a5c8-4549-bba8-c03ddc09bf6f-9889529.png" style="width: 300px; height: 250px;" /></p><p>Now area of the above region is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="|" close="|"><mrow><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced close="|" open="|"><msubsup><mfenced close="]" open="["><mrow><mn>3</mn><mo>&#215;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow><mn>0</mn></msubsup></mfenced><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mn>3</mn><mo>&#215;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mn>0</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mn>11</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>11</mn><mo>+</mo><mn>20</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>31</mn><mn>6</mn></mfrac></math></p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>A</mi><mo>=</mo><mn>62</mn></math></p>

</details>

---

### Q10. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Consider a curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> in the first quadrant as shown in the figure. Let the area <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math> is twice the area <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub></math>. Then the normal to the curve perpendicular to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>12</mn><mi>y</mi><mo>=</mo><mn>15</mn></math> does NOT pass through the point __</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5773680b-efcd-4dd4-b0f2-f0df922b3d63-image.png" style="width: 373px; height: 250px;" />​​​​​​​</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>6</mn><mo>,</mo><mn>21</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>8</mn><mo>,</mo><mn>9</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>10</mn><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>12</mn><mo>,</mo><mo>-</mo><mn>15</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>10</mn><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><msub><mi>A</mi><mn>2</mn></msub></math></p><p>Now, from the graph</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mi>x</mi><mo>&#215;</mo><mi>y</mi><mo>-</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mi>x</mi><mi>y</mi><mo>-</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#160;</mo><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><mi>x</mi><mi>y</mi><mo>-</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>x</mi><mi>y</mi><mo>-</mo><mfrac><mn>16</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>4</mn><mi>x</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>x</mi><mi>y</mi><mo>-</mo><mfrac><mn>16</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced><mrow><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>ln</mi><mi>y</mi><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>ln</mi><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>c</mi><mi>x</mi></math> </p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>x</mi></math> is the given curve.</p><p>Given that the slope of normal <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>6</mn></math></p><p>So the equation of normal will be </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mn>6</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msup><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>+</mo><mn>54</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>+</mo><mn>6</mn><mi>x</mi><mo>=</mo><mn>57</mn></math></p><p>Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>10</mn><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced></math> does not satisfy from the given options.</p></blockquote>

</details>

---

### Q11. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The odd natural number a, such that the area of the region bounded by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>=</mo><msup><mi>y</mi><mi>a</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>364</mn><mn>3</mn></mfrac></math>, equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<blockquote><p>Plotting the graph of the given functions, we get the shaded region as the area bounded by the curves.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dec5b7b5-87ca-4f94-9315-a2e4e2392e1c-image.png" style="width: 289px; height: 180px;" /></p><p>Given, area of shaded region <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>364</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>3</mn></msubsup><msup><mi>y</mi><mi>a</mi></msup><mi>d</mi><mi>y</mi><mo>=</mo><mfrac><mn>364</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mfenced close="]" open="["><mfrac><msup><mi>y</mi><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></msup><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mn>1</mn><mn>3</mn></msubsup><mo>=</mo><mfrac><mn>364</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mn>3</mn><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>364</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>729</mn><mo>-</mo><mn>1</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><msup><mn>3</mn><mn>6</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q12. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the bounded region enclosed by the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn><mo>-</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math> and the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>45</mn><mn>16</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>27</mn><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>63</mn><mn>16</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>27</mn><mn>8</mn></mfrac></math>**

**Detailed Solution:**

<p>Plotting the graph of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>3</mn><mo>-</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis, we get</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/32aaadea-fd8c-439d-aa69-c3e11c1794f1-image.png" style="width: 300px; height: 151px;" /></p><p>Now applying the formula of area of trapezium which is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mtext>height</mtext><mo>&#215;</mo><mfenced><mtext>sum&#160;of&#160;parallel&#160;sides</mtext></mfenced></math> we get,</p><p>Required area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Trap</mi><mfenced><mrow><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>27</mn><mn>8</mn></mfrac></math></p>

</details>

---

### Q13. JEE Main 2021 (16 Mar Shift 1)

*Type:* `numerical` | *Level:* `1`

Let the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>. If the numerical value of area bounded by the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><msqrt><mn>8</mn></msqrt></mrow><mn>3</mn></mfrac></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced></math> is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mi>d</mi><mi>y</mi><mo>=</mo><mo>&#8747;</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><msqrt><mn>8</mn></msqrt></mrow><mn>3</mn></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/27c49707-df39-40fb-a2e5-f26b7ddcc385-image.png" style="width: 376px; height: 200px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><mi>C</mi></msqrt></mrow></msubsup><mfenced><mrow><mo>-</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mi>C</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>4</mn><msqrt><mn>8</mn></msqrt></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mi>C</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><mi>C</mi></msqrt></mrow></msubsup><mo>=</mo><mfrac><mrow><mn>4</mn><msqrt><mn>8</mn></msqrt></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mo>-</mo><msqrt><mn>1</mn><mo>-</mo><mi>C</mi></msqrt></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>C</mi><mo>-</mo><mn>3</mn><mi>C</mi><msqrt><mn>1</mn><mo>-</mo><mi>C</mi></msqrt><mo>-</mo><mn>3</mn><mi>C</mi><mo>-</mo><mn>3</mn><mo>+</mo><mn>3</mn><msqrt><mn>1</mn><mo>-</mo><mi>C</mi></msqrt><mo>+</mo><mn>3</mn><mo>=</mo><mn>2</mn><msqrt><mn>8</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q14. JEE Main 2021 (26 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

The area bounded by the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>2</mn></mrow></mfenced></math> and $y=2$ is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>The area bounded by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/782c67d7-f6a9-4b9d-94f7-747dd9d2606e-image.png" style="width: 304px; height: 200px;" /></p><p>Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo><mn>4</mn><mo>.</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>8</mn></math> sq unit.</p>

</details>

---

### Q15. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>S</mi><mfenced separators="|"><mrow><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>&#8804;</mo><mi>x</mi><mo>,</mo><mi>&#160;</mi><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mi>&#945;</mi></mrow></mfenced><mi>&#160;</mi></math> and <math><mi mathvariant="normal">A</mi><mfenced separators="|"><mrow><mi>&#945;</mi></mrow></mfenced></math> is area of the region <math><mi>S</mi><mfenced separators="|"><mrow><mi>&#945;</mi></mrow></mfenced><mo>.</mo></math> If for a <math><mi>&#955;</mi><mo>,</mo><mn>0</mn><mo>&#60;</mo><mi>&#955;</mi><mo>&#60;</mo><mn>4</mn><mo>,</mo><mi>&#160;</mi><mi mathvariant="normal">A</mi><mfenced separators="|"><mrow><mi>&#955;</mi></mrow></mfenced><mo>:</mo><mi mathvariant="normal">A</mi><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mo>:</mo><mn>5</mn><mo>,</mo><mi>&#160;</mi></math>then <math><mi>&#955;</mi></math> equals:

**Options:**

- **(A)** <math><mn>4</mn><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>
- **(B)** <math><mn>2</mn><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>25</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>
- **(C)** <math><mn>4</mn><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>25</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>
- **(D)** <math><mn>2</mn><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>4</mn><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>25</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b12215d5-5ab0-448f-9f36-28ec66d57d0b-image8.jpeg"> 
<math><mi>S</mi><mfenced separators="|"><mrow><mi>λ</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mrow><munderover><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mi>λ</mi></mrow></munderover><mrow><msqrt><mi>x</mi></msqrt><mtext> </mtext><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><msubsup><mrow><mfenced open="[" close="]" separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mi>λ</mi></mrow></msubsup></mrow></mrow></math>  
<math><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msup><mrow><mi>λ</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></math>  
<math><mo>∴</mo><mi>S</mi><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></math>  
Given <math><mfrac><mrow><mi>S</mi><mfenced separators="|"><mrow><mi>λ</mi></mrow></mfenced></mrow><mrow><mi>S</mi><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>⇒</mo><mfrac><mrow><msup><mrow><mi>λ</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow><mrow><msup><mrow><mn>4</mn></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>  
<math><mo>⇒</mo><mi>λ</mi><mo>=</mo><mn>4</mn><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>25</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>

</details>

---

### Q16. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

The area enclosed between the curve $y=\log _e(x+e)$ and the coordinate axes is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Required area }(O A B)=\int_{1-e}^0 \ln (x+e) d x \\
& =\left[x \ln (x+e)-\int \frac{1}{x+e} x d x\right]_0^1=1 .
\end{aligned}
$$

</details>

---

