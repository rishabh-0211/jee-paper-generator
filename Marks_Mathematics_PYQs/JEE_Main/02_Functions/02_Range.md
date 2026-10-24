# JEE Main Mathematics - Functions

## Topic 2: Range

**Total Questions:** 24

---

### Q1. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all the integral values of $p$ such that the equation $3\sin^2 x + 12\cos x - 3 = p$, $x \in \mathbb{R}$, has at least one solution, is:

**Options:**

- **(A)** $-54$
- **(B)** $-60$
- **(C)** $-75$
- **(D)** $-84$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-75$**

**Detailed Solution:**

Given equation: $3\sin^2 x + 12\cos x - 3 = p$

Substituting $\sin^2 x = 1 - \cos^2 x$:

$3(1 - \cos^2 x) + 12\cos x - 3 = p$

$-3\cos^2 x + 12\cos x = p$

Let $\cos x = t$. Since $x \in \mathbb{R}$, $t \in [-1, 1]$.

The equation becomes $p = -3t^2 + 12t$.

Let $f(t) = -3t^2 + 12t$.

Differentiating with respect to $t$:

$f'(t) = -6t + 12 = 6(2 - t)$

For $t \in [-1, 1]$, $f'(t) > 0$, which means $f(t)$ is strictly increasing in the interval $[-1, 1]$.

The minimum value of $f(t)$ occurs at $t = -1$:

$f(-1) = -3(-1)^2 + 12(-1) = -15$

The maximum value of $f(t)$ occurs at $t = 1$:

$f(1) = -3(1)^2 + 12(1) = 9$

Thus, the range of $p$ for which the equation has at least one solution is $[-15, 9]$.

The integral values of $p$ are $-15, -14, -13, \dots, 9$.

The sum of these integral values is:

$\sum_{k=-15}^{9} k = (-15) + (-14) + (-13) + (-12) + (-11) + (-10) + \sum_{k=-9}^{9} k$

Since $\sum_{k=-9}^{9} k = 0$, the sum simplifies to:

$-15 - 14 - 13 - 12 - 11 - 10 = -75$

Answer: $-75$

</details>

---

### Q2. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all the elements in the range of $f(x)=\operatorname{Sgn}(\sin x)+\operatorname{Sgn}(\cos x)+\operatorname{Sgn}(\tan x)+\operatorname{Sgn}(\cot x)$, $x \neq \frac{\mathrm{n} \pi}{2}, \mathrm{n} \in \mathbf{Z}$, where $\operatorname{Sgn}(\mathrm{t})=\left\{\begin{aligned} 1, & \text { if } \mathrm{t}>0 \\ -1, & \text { if } \mathrm{t}<0\end{aligned}\right.$, is :

**Options:**

- **(A)** 2
- **(B)** 0
- **(C)** 4
- **(D)** -2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

$x \in (0, \pi/2) \Rightarrow y = 1 + 1 + 1 + 1 = 4$
$x \in (\pi/2, \pi) \Rightarrow y = 1 - 1 - 1 - 1 = -2$
$x \in (\pi, 3\pi/2) \Rightarrow y = -1 - 1 + 1 + 1 = 0$
$x \in (3\pi/2, 2\pi) \Rightarrow y = -1 + 1 - 1 - 1 = -2$
$\therefore$ Range of y is $\{-2, 0, 4\}$
Required sum $= -2 + 0 + 4 = 2$

</details>

---

### Q3. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the range of the function $f(x)=\frac{5-x}{x^2-3 x+2}$, $x \neq 1,2$, is $(-\infty, \alpha] \cup[\beta, \infty)$, then $\alpha^2+\beta^2$ is equal to :

**Options:**

- **(A)** 190
- **(B)** 192
- **(C)** 188
- **(D)** 194

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 194**

**Detailed Solution:**

$\begin{aligned}
& y=\frac{5-x}{x^2-3 x+2} \\
& y x^2-3 x y+2 y+x-5=0 \\
& y z^2+(-3 y+1) x+(2 y-5)=0
\end{aligned}$
Case I : If $y=0$ (Accepted)
$\Rightarrow x=5$
Case II : If $y \neq 0$
$\begin{aligned}
& \mathrm{D} \geq 0 \\
& (-3 y+1)^2-4(y)(2 y-5) \geq 0 \\
& 9 y^2+1-6 y-8 y^2+20 y \geq 0 \\
& \mathrm{y}^2+14 y+1 \geq 0 \\
& (y+7)^2-48 \geq 0 \\
& |y+7| \geq 4 \sqrt{3} \\
& \Rightarrow y+7 \geq 4 \sqrt{3} \text { or } \mathrm{y}+7 \leq-4 \sqrt{3} \\
& \Rightarrow \mathrm{y} \geq 4 \sqrt{3}-7 \text { or } \mathrm{y} \leq-4 \sqrt{3}-7
\end{aligned}$
From Case I and Case II
$\mathrm{y} \in(-\infty,-4 \sqrt{3}-7] \cup[4 \sqrt{3}-7, \infty)$
So $\alpha=-4 \sqrt{3}-7$
$\beta=4 \sqrt{3}-7$
$\begin{aligned}
\Rightarrow a^2+b^2 & =(-4 \sqrt{3}-7)^2+(4 \sqrt{3}-7)^2 \\
& =2(48+49) \\
& =194
\end{aligned}$

</details>

---

### Q4. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f, \mathrm{~g}:(1, \infty) \rightarrow \mathbb{R}$ be defined as $f(\mathrm{x})=\frac{2 x+3}{5 x+2}$ and $g(x)=\frac{2-3 x}{1-x}$. If the range of the function $f \circ g:[2,4] \rightarrow \mathbb{R}$ is $[\alpha, \beta]$, then $\frac{1}{\beta-\alpha}$ is equal to

**Options:**

- **(A)** 68
- **(B)** 29
- **(C)** 2
- **(D)** 56

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 56**

**Detailed Solution:**

$\begin{aligned}
& \operatorname{fog}(x)=f(g(x)) \\
& =f\left(\frac{2-3 x}{1-x}\right)=\frac{2\left(\frac{2-3 x}{1-x}\right)+3}{5\left(\frac{2-3 x}{1-x}\right)+2} \\
& =\frac{4-6 x+3-3 x}{10-15 x+2-2 x}=\left(\frac{7-9 x}{12-17 x}\right) \\
& \therefore\left[\begin{array}{c}
12-7 x \neq 0 \\
x \neq \frac{12}{17}
\end{array}\right. \\
& {\left[\begin{array}{l}
\operatorname{fog}(2)=\frac{7-9(2)}{12-17(2)}=\frac{-11}{-22}=\frac{1}{2} \\
\operatorname{fog}(4)=\frac{7-9(4)}{12-17(4)}=\frac{-29}{-56}=\frac{29}{56}
\end{array}\right.} \\
& \text { Range of fog : }[\alpha, \beta]=\left[\frac{1}{2}, \frac{29}{56}\right] \\
& \therefore(\beta-\alpha)=\frac{29}{56}-\frac{1}{2}=\frac{29-28}{56}=\frac{1}{56} \\
& \frac{1}{(\beta-\alpha)}=56
\end{aligned}$

</details>

---

### Q5. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let the range of the function $f(x)=6+16 \cos x \cdot \cos \left(\frac{\pi}{3}-x\right) \cdot \cos \left(\frac{\pi}{3}+x\right) \cdot \sin 3 x \cdot \cos 6 x, x \in \mathbf{R}$ be $[\alpha, \beta]$. Then the distance of the point $(\alpha, \beta)$ from the line $3 x+4 y+12=0$ is :

**Options:**

- **(A)** 11
- **(B)** 8
- **(C)** 10
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 11**

**Detailed Solution:**

$\begin{aligned}
& f(x)=6+16 \cos x \cdot \cos \left(\frac{\pi}{3}-x\right) \\
& \qquad \cos \left(\frac{\pi}{3}+x\right) \cdot \sin 3 x \cdot \cos 6 x \\
& f(x)=6+4 \cos 3 x \cdot \sin 3 x \cdot \cos 6 x \\
& \therefore \quad f(x)=6+\sin 12 x \\
& \therefore \quad \text { Range of } f(x)=[5,7] \\
& \therefore \quad[\alpha, \beta]=[5,7]
\end{aligned}$
$\therefore$ Distance of point from $3 x+4 y+12=0$
$\begin{aligned}
& =\left|\frac{3.5+4.7+12}{\sqrt{3^2+4^2}}\right| \\
& =11 \text { units }
\end{aligned}$

</details>

---

### Q6. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the range of the function $f(x)=\frac{1}{2+\sin 3 x+\cos 3 x}, x \in \mathbb{R}$ be $[a, b]$. If $\alpha$ and $\beta$ are respectively the A.M. and the G.M. of $a$ and $b$, then $\frac{\alpha}{\beta}$ is equal to

**Options:**

- **(A)** $\pi$
- **(B)** $\sqrt{\pi}$
- **(C)** 2
- **(D)** $\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{2}$**

**Detailed Solution:**

$\begin{aligned} & f(x) \frac{1}{2+\sin 3 x+\cos 3 x} \\ & {\left[\frac{1}{2+\sqrt{2}}, \frac{1}{2-\sqrt{2}}\right]} \\ & \frac{\alpha}{\beta}=\frac{a+b}{2 \sqrt{a b}}=\frac{1}{2}\left(\sqrt{\frac{a}{b}}+\sqrt{\frac{b}{a}}\right) \\ & =\frac{1}{2}\left(\sqrt{\frac{2-\sqrt{2}}{2+\sqrt{2}}}+\sqrt{\frac{2+\sqrt{2}}{2-\sqrt{2}}}\right) \\ & =\frac{(2-\sqrt{2})+(2+\sqrt{2})}{2 \times \sqrt{2}}=\sqrt{2}\end{aligned}$

</details>

---

### Q7. JEE Main 2024 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

If the range of $f(\theta)=\frac{\sin ^4 \theta+3 \cos ^2 \theta}{\sin ^4 \theta+\cos ^2 \theta}, \theta \in \mathbb{R}$ is $[\alpha, \beta]$, then the sum of the infinite G.P., whose first term is 64 and the common ratio is $\frac{\alpha}{\beta}$, is equal to________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **96**

**Detailed Solution:**

$\begin{aligned} & f(\theta)=\frac{\sin ^4 \theta+3 \cos ^2 \theta}{\sin ^4 \theta+\cos ^2 \theta} \\ & f(\theta)=1+\frac{2 \cos ^2 \theta}{\sin ^4 \theta+\cos ^2 \theta} \\ & f(\theta)=\frac{2 \cos ^2 \theta}{\cos ^4 \theta-\cos ^2 \theta+1}+1 \\ & f(\theta)=\frac{2}{\cos ^2 \theta+\sec ^2 \theta-1}+1 \\ & \left.f(\theta)\right|_{\text {min. }}=1 \\ & f(\theta)_{\text {max. }}=3 \\ & S=\frac{64}{1-1 / 3}=96\end{aligned}$

</details>

---

### Q8. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=\frac{1}{7-\sin 5 x}$ be a function defined on $\mathbf{R}$. Then the range of the function $f(x)$ is equal to ;

**Options:**

- **(A)** $\left[\frac{1}{7}, \frac{1}{6}\right]$
- **(B)** $\left[\frac{1}{8}, \frac{1}{5}\right]$
- **(C)** $\left[\frac{1}{7}, \frac{1}{5}\right]$
- **(D)** $\left[\frac{1}{8}, \frac{1}{6}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\frac{1}{8}, \frac{1}{6}\right]$**

**Detailed Solution:**

$\begin{aligned} & \sin 5 x \in[-1,1] \\ & -\sin 5 x \in[-1,1] \\ & 7-\sin 5 x \in[6,8] \\ & \frac{1}{7-\sin 5 x} \in\left[\frac{1}{8}, \frac{1}{6}\right]\end{aligned}$

</details>

---

### Q9. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the sum of the maximum and the minimum values of the function $f(x)=\frac{2 x^2-3 x+8}{2 x^2+3 x+8}$ be $\frac{\mathrm{m}}{\mathrm{n}}$, where $\operatorname{gcd}(\mathrm{m}, \mathrm{n})=1$. Then $\mathrm{m}+\mathrm{n}$ is equal to :

**Options:**

- **(A)** 195
- **(B)** 201
- **(C)** 217
- **(D)** 182

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 201**

**Detailed Solution:**

$\begin{aligned} & y=\frac{2 x^2-3 x+8}{2 x^2+3 x+8} \\ & x^2(2 y-2)+x(3 y+3)+8 y-8=0 \\ & \text { use } D \geq 0 \\ & (3 y+3)^2-4(2 y-2)(8 y-8) \geq 0 \\ & (11 y-5)(5 y-11) \leq 0 \\ & \Rightarrow y \in\left[\frac{5}{11}, \frac{11}{5}\right] \\ & y=1 \text { is also included }\end{aligned}$

</details>

---

### Q10. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi><mo>]</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mi>&#960;</mi><mo>]</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mi>&#960;</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi><mo>)</mo></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math></p><p>Now taking, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#8804;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>&#60;</mo><mn>1</mn></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#8804;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#8804;</mo><mn>4</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>&#60;</mo><mn>2</mn><mi>&#960;</mi></math></p><p>Hence, the range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mo>)</mo></math></p></blockquote>

</details>

---

### Q11. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> be the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msub><mi>log</mi><mrow><mn>3</mn><mi>x</mi></mrow></msub><mfenced><mfrac><mrow><mn>6</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mn>3</mn></msub><mi>x</mi></mrow><mrow><mo>-</mo><mn>5</mn><mi>x</mi></mrow></mfrac></mfenced></mrow></mfenced></math>. If the range of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>D</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>,</mo></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> is the greatest integer function), is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></mrow></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>5</mn><mi>&#946;</mi></mfrac></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>135</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>46</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>136</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>135</mn></math>**

**Detailed Solution:**

<p>We have been given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msub><mi>log</mi><mrow><mn>3</mn><mi>x</mi></mrow></msub><mfenced><mfrac><mrow><mn>6</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mn>3</mn></msub><mi>x</mi></mrow><mrow><mo>-</mo><mn>5</mn><mi>x</mi></mrow></mfrac></mfenced></mrow></mfenced></math></p><p>We know that the domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mrow><mn>3</mn><mi>x</mi></mrow></msub><mfenced><mfrac><mrow><mn>6</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mn>3</mn></msub><mi>x</mi></mrow><mrow><mo>-</mo><mn>5</mn><mi>x</mi></mrow></mfrac></mfenced><mo>&#8712;</mo><munder><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mrow><mo>-</mo><mfenced><mn>1</mn></mfenced></mrow></munder><mo>,</mo><mo>&#160;</mo><munder><mrow><mn>3</mn><mi>x</mi><mo>&#62;</mo><mn>0</mn></mrow><mrow><mo>-</mo><mfenced><mn>2</mn></mfenced></mrow></munder><mo>,</mo><mo>&#160;</mo><munder><mrow><mn>3</mn><mi>x</mi><mo>&#8800;</mo><mn>1</mn></mrow><mrow><mo>-</mo><mfenced><mn>3</mn></mfenced></mrow></munder><mo>,</mo><mo>&#160;</mo><munder><mfrac><mrow><mn>6</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mn>3</mn></msub><mi>x</mi></mrow><mrow><mo>-</mo><mn>5</mn><mi>x</mi></mrow></mfrac><mrow><mo>-</mo><mfenced><mn>4</mn></mfenced></mrow></munder><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mn>3</mn></msub><mi>x</mi><mo>&#60;</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mn>3</mn></msub><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#60;</mo><msup><mn>3</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>27</mn></mfrac></math> </p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mn>3</mn></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mn>4</mn></mfenced><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>27</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>5</mn></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><msub><mi>log</mi><mrow><mn>3</mn><mi>x</mi></mrow></msub><mfenced><mfrac><mrow><mn>6</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mn>3</mn></msub><mi>x</mi></mrow><mrow><mo>-</mo><mn>5</mn><mi>x</mi></mrow></mfrac></mfenced><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mn>3</mn><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>x</mi></mrow></mfrac><mo>&#8805;</mo><mfrac><mrow><mn>6</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mn>3</mn></msub><mi>x</mi></mrow><mrow><mo>-</mo><mn>5</mn><mi>x</mi></mrow></mfrac><mo>&#8805;</mo><mn>3</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>&#8804;</mo><mn>6</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mn>3</mn></msub><mi>x</mi><mo>&#8804;</mo><mo>-</mo><mn>15</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfrac><mn>23</mn><mn>6</mn></mfrac><mo>&#8804;</mo><msub><mi>log</mi><mn>3</mn></msub><mi>x</mi><mo>&#8804;</mo><mfrac><mrow><mo>-</mo><mn>15</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mrow><mo>-</mo><mfrac><mn>23</mn><mn>6</mn></mfrac></mrow></msup><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><msup><mn>3</mn><mfrac><mrow><mo>-</mo><mn>15</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn></mrow><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><msup><mn>3</mn><mstyle displaystyle="true"><mfrac><mn>23</mn><mn>6</mn></mfrac></mstyle></msup></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mn>1</mn><msup><mn>3</mn><mstyle displaystyle="true"><mfrac><mrow><mn>15</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></mrow><mn>2</mn></mfrac></mstyle></msup></mfrac><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mfrac><mrow><mo>-</mo><mn>23</mn></mrow><mn>6</mn></mfrac></msup><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><msup><mn>3</mn><mstyle displaystyle="true"><mfrac><mrow><mn>15</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></mrow><mn>2</mn></mfrac></mstyle></msup></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>6</mn></mfenced></math>, here <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mfrac><mrow><mo>-</mo><mn>23</mn></mrow><mn>6</mn></mfrac></msup></math> is very small positive quantity,</p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>5</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>6</mn></mfenced><mo>,</mo><mo>&#160;</mo><msup><mn>3</mn><mfrac><mrow><mo>-</mo><mn>23</mn></mrow><mn>6</mn></mfrac></msup><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>27</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> Range <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8712;</mo><mfenced><mrow><msup><mn>3</mn><mfrac><mrow><mo>-</mo><mn>23</mn></mrow><mn>6</mn></mfrac></msup><mo>,</mo><mfrac><mn>1</mn><mn>27</mn></mfrac></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>5</mn><mi>&#946;</mi></mfrac><mo>=</mo><msup><mfenced><msup><mn>3</mn><mfrac><mrow><mo>-</mo><mn>23</mn></mrow><mn>6</mn></mfrac></msup></mfenced><mn>2</mn></msup><mo>+</mo><mfrac><mn>5</mn><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>27</mn></mfrac></mstyle></mfrac><mo>=</mo><msup><mfenced><msup><mn>3</mn><mfrac><mrow><mo>-</mo><mn>23</mn></mrow><mn>6</mn></mfrac></msup></mfenced><mn>2</mn></msup><mo>+</mo><mn>135</mn><mo>&#8776;</mo><mn>135</mn></math></p><p>Note: This question was bonus in Jee Main April 2023 session.</p>

</details>

---

### Q12. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let the sets <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> denote the domain and range respectively of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>x</mi></msqrt></mfrac><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denotes the smallest integer greater than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. Then among the statements</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced><mo>:</mo><mo>&#160;</mo><mi>A</mi><mo>&#8745;</mo><mi>B</mi><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mi mathvariant="normal">&#8469;</mi></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced><mo>:</mo><mo>&#160;</mo><mi>A</mi><mo>&#8746;</mo><mi>B</mi><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo></mrow></mfenced></math></p>

**Options:**

- **(A)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>S</mi><mn>2</mn><mo>)</mo></math> is true
- **(B)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>S</mi><mn>1</mn><mo>)</mo></math> is true
- **(C)** Neither <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is true
- **(D)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Neither <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is true**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>x</mi></msqrt></mfrac></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mi>x</mi></mfenced></math> is fractional part of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> whose value is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mfenced close="}" open="{"><mi>x</mi></mfenced><mo>&#60;</mo><mn>1</mn></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>x</mi><mo>=</mo><mo>-</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></math></p><p>Now putting the value in given function we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>x</mi></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mo>-</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></msqrt></mfrac></math></p><p>Now we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mi>g</mi><mfenced><mi>x</mi></mfenced></msqrt></mfrac></math> is defined when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math>, but <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfenced close="}" open="{"><mi>x</mi></mfenced><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mo>-</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></msqrt></math> is not defined</p><p>Hence, Domain and Range will be<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#981;</mi></math> </p></blockquote>

</details>

---

### Q13. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be real valued function defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow></mfrac></math>. Then range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>21</mn><mn>4</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mfrac><mn>21</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>21</mn><mn>4</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>21</mn><mn>4</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>21</mn><mn>4</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>21</mn><mn>4</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be real valued function defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow></mfrac></math></p><p>Now let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow></mfrac><mo>=</mo><mfrac><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow></mfenced></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now differentiating the above function we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>5</mn><mi>x</mi><mo>-</mo><mn>16</mn></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p>Now by wavy curve method we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8326b3eb-766d-4e35-820b-5b28d62cd025-9896370.png" style="width: 300px; height: 106px;" /></p><p>So Graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>6</mn></mrow></mfenced></mrow></mfrac></math> for given domain will be,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ad3b373e-6630-4e9e-8731-bb5480df8b5a-9896370_2.png" style="width: 500px; height: 250px;" /></p><p> </p><p>So, from graph range is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8712;</mo><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>21</mn><mn>4</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math></p>

</details>

---

### Q14. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mi>x</mi></mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> is greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi></math>, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>2</mn><mo>,</mo><mn>6</mn><mo>)</mo></math>, then its range is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mfrac><mn>5</mn><mn>26</mn></mfrac><mo>,</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mrow><mfrac><mn>9</mn><mn>29</mn></mfrac><mo>,</mo><mfrac><mn>27</mn><mn>109</mn></mfrac><mo>,</mo><mfrac><mn>18</mn><mn>89</mn></mfrac><mo>,</mo><mfrac><mn>9</mn><mn>53</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mfrac><mn>5</mn><mn>26</mn></mfrac><mo>,</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mfrac><mn>5</mn><mn>37</mn></mfrac><mo>,</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mrow><mfrac><mn>9</mn><mn>29</mn></mfrac><mo>,</mo><mfrac><mn>27</mn><mn>109</mn></mfrac><mo>,</mo><mfrac><mn>18</mn><mn>89</mn></mfrac><mo>,</mo><mfrac><mn>9</mn><mn>53</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mfrac><mn>5</mn><mn>37</mn></mfrac><mo>,</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mfrac><mn>5</mn><mn>37</mn></mfrac><mo>,</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mi>x</mi></mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>;</mo></mtd><mtd><mo>&#160;</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></mtd></mtr><mtr><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>3</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>;</mo></mtd><mtd><mo>&#160;</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>)</mo></mtd></mtr><mtr><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>4</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>;</mo></mtd><mtd><mo>&#160;</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>)</mo></mtd></mtr><mtr><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>5</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>;</mo></mtd><mtd><mo>&#160;</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>)</mo></mtd></mtr></mtable></math></p><p> </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d4326bbe-9a55-4ff7-a8f2-29ef4ecc51e5-9896182.png" style="width: 400px; height: 261px;" /></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8712;</mo><mfenced close="]"><mrow><mfrac><mn>5</mn><mn>37</mn></mfrac><mo>,</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q15. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The range of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><mn>3</mn><mo>-</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>2</mn><mo>+</mo><mi>x</mi></msqrt></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msqrt><mn>5</mn></msqrt><mo>,</mo><msqrt><mn>10</mn></msqrt></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>,</mo><msqrt><mn>11</mn></msqrt></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msqrt><mn>5</mn></msqrt><mo>,</mo><msqrt><mn>13</mn></msqrt></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msqrt><mn>2</mn></msqrt><mo>,</mo><msqrt><mn>7</mn></msqrt></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msqrt><mn>5</mn></msqrt><mo>,</mo><msqrt><mn>10</mn></msqrt></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><mn>3</mn><mo>-</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>2</mn><mo>+</mo><mi>x</mi></msqrt></math></p><p>Now differentiation the above function,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>3</mn><mo>-</mo><mi>x</mi></msqrt></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>2</mn><mo>+</mo><mi>x</mi></msqrt></mrow></mfrac></math></p><p>Point of maxima and minima,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msqrt><mn>3</mn><mo>-</mo><mi>x</mi></msqrt><mo>-</mo><msqrt><mn>2</mn><mo>+</mo><mi>x</mi></msqrt></mrow><mrow><mn>2</mn><msqrt><mn>2</mn><mo>+</mo><mi>x</mi></msqrt><msqrt><mn>3</mn><mo>-</mo><mi>x</mi></msqrt></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>2</mn><mo>+</mo><mi>x</mi></msqrt><mo>=</mo><msqrt><mn>3</mn><mo>-</mo><mi>x</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>And domain is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>3</mn><mo>)</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4b21e34b-f1e6-4601-894a-83988abf99a6-9896086.png" style="width: 400px; height: 122px;" /></p><p>So at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>, maxima</p><p>The maximum value of the function,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><msqrt><mfrac><mn>5</mn><mn>2</mn></mfrac></msqrt><mo>+</mo><msqrt><mfrac><mn>5</mn><mn>2</mn></mfrac></msqrt><mo>=</mo><msqrt><mn>10</mn></msqrt></math></p><p>The minimum value of function at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><msqrt><mn>5</mn></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><msqrt><mn>5</mn></msqrt></math></p><p>Therefore, the range of the function,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>Range</mtext><mo>&#8712;</mo><mfenced close="]" open="["><mrow><msqrt><mn>5</mn></msqrt><mo>,</mo><msqrt><mn>10</mn></msqrt></mrow></mfenced></math></p>

</details>

---

### Q16. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a function defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><msqrt><mi>m</mi></msqrt></msub><mo>&#160;</mo><mfenced close="}" open="{"><mrow><msqrt><mn>2</mn></msqrt><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>m</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>, for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>, such that the range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is _____ .

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a function defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><msqrt><mi>m</mi></msqrt></msub><mo>&#160;</mo><mfenced close="}" open="{"><mrow><msqrt><mn>2</mn></msqrt><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>m</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>, for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>,</p><p>Also given the range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>,</p><p>Now we know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>&#8804;</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi><mo>&#8804;</mo><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mo>&#8804;</mo><msqrt><mn>2</mn></msqrt><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>&#8804;</mo><mn>2</mn></math></p><p>(Assuming <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi>k</mi></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mi>k</mi><mo>&#8804;</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now taking function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><msqrt><mi mathvariant="normal">m</mi></msqrt></msub><mfenced><mrow><mi>k</mi><mo>+</mo><mi>m</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#8804;</mo><msub><mi>log</mi><msqrt><mi>m</mi></msqrt></msub><mfenced><mrow><mi>k</mi><mo>+</mo><mi>m</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#8804;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>&#8804;</mo><mi>k</mi><mo>+</mo><mi>m</mi><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mi>m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mi>m</mi><mo>+</mo><mn>3</mn><mo>&#8804;</mo><mi>k</mi><mo>&#8804;</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now from equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>m</mi><mo>+</mo><mn>3</mn><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">m</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q17. JEE Main 2022 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

The sum of the maximum and minimum values of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mfrac><mn>5</mn><mn>4</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> is the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>t</mi></math>, is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **15**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfenced><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mtext>as&#160;</mtext><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mtext>=</mtext><mfenced close="]" open="["><mi>x</mi></mfenced><mtext>-1&#160;where&#160;</mtext><mfenced close="]" open="["><mo>.</mo></mfenced><mtext>&#160;is&#160;greatest&#160;integer&#160;function</mtext></mrow></mfenced></math></p><p>Now critical points of</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>7</mn><mn>5</mn></mfrac><mo>,</mo><msqrt><mn>5</mn></msqrt><mo>-</mo><mn>1</mn><mo>,</mo><msqrt><mn>6</mn></msqrt><mo>-</mo><mn>1</mn><mo>,</mo><msqrt><mn>7</mn></msqrt><mo>-</mo><mn>1</mn><mo>,</mo><msqrt><mn>8</mn></msqrt><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Maximum or minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> occur at critical points or boundary points.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>f</mi><mfenced><mfrac><mn>5</mn><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>+</mo><mn>4</mn><mo>=</mo><mfrac><mn>19</mn><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>7</mn><mn>5</mn></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>4</mn></math></p><p>As both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></math> are increasing in nature after <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>7</mn><mn>5</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>10</mn><mo>-</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>4</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>3</mn><mo>+</mo><mn>8</mn><mo>=</mo><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>f</mi><msub><mfenced><mfrac><mn>7</mn><mn>5</mn></mfrac></mfenced><mi>min</mi></msub><mo>=</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><msub><mfenced><mn>2</mn></mfenced><mi>max</mi></msub><mo>=</mo><mn>11</mn></math></p><p>So sum of minimum and maximum value is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>+</mo><mn>11</mn><mo>=</mo><mn>15</mn></math></p></blockquote>

</details>

---

### Q18. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The range of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msub><mi>log</mi><msqrt><mn>5</mn></msqrt></msub><mfenced><mrow><mn>3</mn><mo>+</mo><mi>cos</mi><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>cos</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>cos</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>cos</mi><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>,</mo><mo>&#160;</mo><msqrt><mn>5</mn></msqrt></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>]</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msqrt><mn>5</mn></msqrt><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>]</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>]</mo></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msub><mi>log</mi><msqrt><mn>5</mn></msqrt></msub><mo>(</mo><mn>3</mn><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>x</mi><mo>+</mo><msqrt><mn>2</mn></msqrt><mi>cos</mi><mi>x</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mo>(</mo><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>x</mi><mo>+</mo><msqrt><mn>2</mn></msqrt><mi>cos</mi><mi>x</mi><mo>)</mo><mo>&#8804;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>&#8804;</mo><mo>(</mo><mn>3</mn><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>x</mi><mo>+</mo><msqrt><mn>2</mn></msqrt><mi>cos</mi><mi>x</mi><mo>)</mo><mo>&#8804;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><msqrt><mn>5</mn></msqrt></msub><mn>1</mn><mo>&#8804;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8804;</mo><msub><mi>log</mi><msqrt><mn>5</mn></msqrt></msub><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#8804;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8804;</mo><mn>2</mn></math></p>

</details>

---

### Q19. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mi>sin</mi><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>2</mn><mrow><mi>cos</mi><mi>x</mi></mrow></msup></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></msup></math>**

**Detailed Solution:**

<p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">M</mi><mo>&#8805;</mo><mi mathvariant="normal">G</mi><mo>.</mo><mi mathvariant="normal">M</mi><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mn>2</mn><mi>sinx</mi></msup><mo>+</mo><msup><mn>2</mn><mi>cosx</mi></msup></mrow><mn>2</mn></mfrac><mo>&#8805;</mo><msqrt><msup><mn>2</mn><mi>sinx</mi></msup><mo>&#183;</mo><msup><mn>2</mn><mi>cosx</mi></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mi>sinx</mi></msup><mo>+</mo><msup><mn>2</mn><mi>cosx</mi></msup><mo>&#8805;</mo><msup><mn>2</mn><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>sinx</mi><mo>+</mo><mi>cosx</mi></mrow><mn>2</mn></mfrac></mrow></msup></math></p><p>Now    <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>&#8804;</mo><mi>sinx</mi><mo>+</mo><mi>cosx</mi><mo>&#8804;</mo><msqrt><mn>2</mn></msqrt></math></p><p>So minimum value of </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>sinx</mi></msup><mo>+</mo><msup><mn>2</mn><mi>cosx</mi></msup><mo>=</mo><msup><mn>2</mn><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></msup><mo>=</mo><msup><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></msup></math>  </p>

</details>

---

### Q20. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mo>:</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi></mi><mtext>&#8201;</mtext><mn>3</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math>, be a function defined by <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>,</mo><mi></mi></math> where <math><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced></math>, denotes the greatest integer <math><mo>&#8804;</mo><mi>x</mi><mo>.</mo></math> Then the range of <math><mi>f</mi></math>, is

**Options:**

- **(A)** <math><mfenced close="]" separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo><mi></mi><mtext> </mtext><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced><mo>∪</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>,</mo><mi></mi><mtext> </mtext><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo><mi></mi><mtext> </mtext><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>∪</mo><mfenced close="]" separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo><mi></mi><mtext> </mtext><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math><mfenced close="]" separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo><mi></mi><mtext> </mtext><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo><mi></mi><mtext> </mtext><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo><mi></mi><mtext> </mtext><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>∪</mo><mfenced close="]" separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo><mi></mi><mtext> </mtext><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#160;</mo><mo>:</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mfenced close="]" open="["><mi>x</mi></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfrac><mi mathvariant="normal">x</mi><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>)</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mn>1</mn></mfenced><mo>-</mo><mi>x</mi><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mn>2</mn></mfenced><mo>-</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mfrac><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is decreasing function.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msub><mi mathvariant="normal">R</mi><mi mathvariant="normal">f</mi></msub><mo>&#160;</mo><mo>&#8712;</mo><mfenced><mrow><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced close="]"><mrow><mfrac><mn>6</mn><mn>10</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q21. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $f: R \rightarrow R$ be defined by $f(x)=\frac{x}{1+x^{2}}, x \in R .$ Then the range of $f$ is

**Options:**

- **(A)** $\left[-\frac{1}{2}, \frac{1}{2}\right]$
- **(B)** $R-[-1,1]$
- **(C)** $R-\left[-\frac{1}{2}, \frac{1}{2}\right]$
- **(D)** $(-1,1)-\{0\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[-\frac{1}{2}, \frac{1}{2}\right]$**

**Detailed Solution:**

$f(x)=\frac{x}{1+x^{2}}, x \in R$

Let, $y=\frac{x}{1+x^{2}}$

$\Rightarrow y x^{2}-x+y=0 \Rightarrow x=\frac{1 \pm \sqrt{1-4 y^{2}}}{2}$

$\Rightarrow 1-4 y^{2} \geq 0$

$\Rightarrow 1 \geq 4 y^{2}$

$\Rightarrow|y| \leq \frac{1}{2}$

$\Rightarrow \quad-\frac{1}{2} \leq y \leq \frac{1}{2}$

$\Rightarrow$ The range of $f$ is $\left[-\frac{1}{2}, \frac{1}{2}\right]$.

</details>

---

### Q22. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=\sin x, g(x)=x$.
Statement 1: $f(x) \leqslant g x($ for $) \mathrm{x}$ in $(0, \infty)$
Statement 2: $f(x) \leq 1$ for $x$ in $(0, \infty)$ but $g(x) \rightarrow \infty$ as $x \rightarrow \infty$.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is false.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation for Statement 1.
- **(C)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation for Statement 1.
- **(D)** Statement 1 is false, Statement 2 is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation for Statement 1.**

**Detailed Solution:**

Let $f(x)=\sin x$ and $g(x)=x$
Statement-1: $f(x) \leq g \quad x(\forall x) \in 0, \infty(\quad)$
i.e., $\sin x \leq x \forall x \in(0, \infty)$
which is true
Statement-2: $f(x) \leq 1 \forall x \in 0, \infty(\quad)$
i.e., $\sin x \leq 1 \forall x \in(0, \infty)$
It is true and
$g(x)=x \rightarrow \infty$ as $x \rightarrow \infty$ also true.

</details>

---

### Q23. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `2`

The range of the function $f(x)=\frac{x}{1+|x|}, x \in R$, is

**Options:**

- **(A)** $R$
- **(B)** $(-1,1)$
- **(C)** $R-\{0\}$
- **(D)** $[-1,1]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(-1,1)$**

**Detailed Solution:**

$f(x)=\frac{x}{1+|x|}, x \in R$
If $x>0,|x|=x \Rightarrow f(x)=\frac{x}{1+x}$ which is not defined for $x=-1$
If $x < 0,|x|=-x \Rightarrow f(x)=\frac{x}{1-x}$ which is not defined for $x=1$ Thus $f(x)$ defined for all values of $\mathrm{R}$ except 1 and $-1$
Hence, range $=(-1,1)$.

</details>

---

### Q24. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

The range of the function $f(x)={ }^{7-x} P_{x-3}$ is

**Options:**

- **(A)** $\{1,2,3\}$
- **(B)** $\{1,2,3,4,5\}$
- **(C)** $\{1,2,3,4\}$
- **(D)** $\{1,2,3,4,5,6\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\{1,2,3\}$**

**Detailed Solution:**

$f(x)={ }^{7-x} P_{x-3}$
$7-x \geq 0 \Rightarrow x \leq 7$
$x-3 \geq 0 \Rightarrow x \geq 3$,
and $7-x \geq x-3 \Rightarrow x \leq 5$
$\Rightarrow 3 \leq x \leq 5 \Rightarrow x=3,4,5 \Rightarrow$ Range is $\{1,2,3\}$

</details>

---

