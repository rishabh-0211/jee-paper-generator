# JEE Advanced Mathematics - Differential Equations

## Topic 3: Homogeneous DE

**Total Questions:** 3

---

### Q1. JEE Advanced 2025 (Paper 2)

*Type:* `numerical` | *Level:* `1`

Let $y(x)$ be the solution of the differential equation
$x^2 \frac{d y}{d x}+x y=x^2+y^2, x>\frac{1}{e}$
satisfying $y(1)=0$. Then the value of $2 \frac{(y(e))^2}{y\left(e^2\right)}$ is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.75**

**Detailed Solution:**

Put $\mathrm{y}=\mathrm{vx} \Rightarrow \frac{d y}{d x}=v+x \frac{d v}{d x}$
D.E.
$\begin{aligned}
& \mathrm{x}^2\left(v+\mathrm{x} \frac{\mathrm{~d} v}{\mathrm{dx}}\right)+\mathrm{x}^2 v=\mathrm{x}^2\left(1+v^2\right) \\
& \Rightarrow v+x \frac{d v}{d x}+v=1+v^2 \\
& \Rightarrow x \frac{d v}{d x}=1+v^2-2 v \\
& \Rightarrow \int \frac{d v}{(v-1)^2}=\int \frac{d x}{x} \\
& \Rightarrow-\frac{1}{v-1}=\ln |x|+\mathrm{C}
\end{aligned}$
$\Rightarrow \frac{\mathrm{x}}{\mathrm{x}-\mathrm{y}}=\ln |x|+\mathrm{C}=\ln \mathrm{x}+\mathrm{C} \quad\left(\right.$ Since $\left.\mathrm{x}>\frac{1}{\mathrm{e}}\right)$
Given $y(1)=0$
$\Rightarrow C=1$
So $\frac{x}{x-y}=\ln (e x)$
Now $y(e)=\frac{e}{2}$ and $y\left(e^2\right)=\frac{2 e^2}{3}$
$\therefore \frac{2(y(e))^2}{y\left(e^2\right)}=\frac{2 \cdot \frac{e^2}{4}}{\frac{2 e^2}{3}}=\frac{3}{4}=0.75$

</details>

---

### Q2. JEE Advanced 2013 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

A curve passes through the point <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mo>,</mo> <mfrac> <mrow> <mi>&#960;</mi> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>. Let the slope of the curve at each point <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mtext>x</mtext> <mo>,</mo> <mtext>y</mtext> </mrow> </mfenced> </mrow> </math> be <math> <mrow> <mfrac> <mrow> <mtext>y</mtext> </mrow> <mrow> <mtext>x</mtext> </mrow> </mfrac> <mo>+</mo> <mtext>sec</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mtext>y</mtext> </mrow> <mrow> <mtext>x</mtext> </mrow> </mfrac> </mrow> </mfenced> <mo>, x</mo> <mo>&#160;&#62;&#160;</mo> <mn>0</mn> </mrow> </math>. Then the equation of the curve is

**Options:**

- **(A)** <math> <mrow> <mtext>sin</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mtext>y</mtext> </mrow> <mrow> <mtext>x</mtext> </mrow> </mfrac> </mrow> </mfenced> <mo>=</mo> <mtext>log x</mtext> <mo>+</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mtext>cosec </mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mtext>y</mtext> </mrow> <mrow> <mtext>x</mtext> </mrow> </mfrac> </mrow> </mfenced> <mo>=</mo> <mtext>log x</mtext> <mo>+</mo> <mn>2</mn> </mrow> </math>
- **(C)** <math> <mrow> <mtext>sec </mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mtext>2y</mtext> </mrow> <mrow> <mtext>x</mtext> </mrow> </mfrac> </mrow> </mfenced> <mo>=</mo> <mtext>log x</mtext> <mo>+</mo> <mn>2</mn> </mrow> </math>
- **(D)** <math> <mrow> <mtext>cos </mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mtext>2y</mtext> </mrow> <mrow> <mtext>x</mtext> </mrow> </mfrac> </mrow> </mfenced> <mo>=</mo> <mtext>log x</mtext> <mo>+</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mtext>sin</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mtext>y</mtext> </mrow> <mrow> <mtext>x</mtext> </mrow> </mfrac> </mrow> </mfenced> <mo>=</mo> <mtext>log x</mtext> <mo>+</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<p>Given slope at (x, y) is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mtext>dy</mtext><mtext>dx</mtext></mfrac><mo>=</mo><mfrac><mtext>y</mtext><mtext>x</mtext></mfrac><mo>+</mo><mtext>sec</mtext><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced></math>......<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>
let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mtext>y</mtext><mtext>x</mtext></mfrac><mo>=</mo><mtext>t</mtext><mo>&#8658;</mo><mtext>y</mtext><mo>=</mo><mtext>xt</mtext></math> </p><p>Differentiating this wrt <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mspace width="0.5em"/><mo>&#8658;</mo><mspace width="0.5em"/><mspace width="0.5em"/><mfrac><mtext>dy</mtext><mtext>dx</mtext></mfrac><mo>=</mo><mtext>t</mtext><mo>+</mo><mtext>x</mtext><mfrac><mtext>dt</mtext><mtext>dx</mtext></mfrac></math>......<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>, we have
<math> <mrow> <mtext>t</mtext> <mo>+</mo> <mtext>x</mtext> <mfrac> <mrow> <mtext>dt</mtext> </mrow> <mrow> <mtext>dx</mtext> </mrow> </mfrac> <mo>=</mo> <mtext>t</mtext> <mo>+</mo> <mtext>sec</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mtext>t</mtext> </mrow> </mfenced> </mrow> </math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>sec</mi><mfenced><mi>t</mi></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p>Integrating both sides.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi>cos</mi><mfenced><mi>t</mi></mfenced><mtext>dt</mtext><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mtext>x</mtext></mfrac><mtext>dx</mtext></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mi>ln</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mtext>c</mtext></math> </p><p>Now Put value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> in above equation.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>sin</mtext><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>=</mo><mi>ln</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mtext>c</mtext></math>.....<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math>
Given that curve passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mtext>,&#160;</mtext><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></math> so put in above equation.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>sin</mtext><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mi>ln</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mtext>c</mtext><mo>&#8658;</mo><mtext>c</mtext><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Now, put the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>sin</mtext><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>=</mo><mi>ln</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q3. JEE Advanced 2012 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

If $y(x)$ satisfies the differential equation $y^{\prime}-y \tan x$ $=2 x \sec x$ and $y(0)=0$, then

**Options:**

- **(A)** $y\left(\frac{\pi}{4}\right)=\frac{\pi^{2}}{8 \sqrt{2}}$
- **(B)** $y^{\prime}\left(\frac{\pi}{4}\right)=\frac{\pi^{2}}{18}$
- **(C)** $y\left(\frac{\pi}{3}\right)=\frac{\pi^{2}}{9}$
- **(D)** $y^{\prime}\left(\frac{\pi}{3}\right)=\frac{4 \pi}{3}+\frac{2 \pi^{2}}{3 \sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y^{\prime}\left(\frac{\pi}{3}\right)=\frac{4 \pi}{3}+\frac{2 \pi^{2}}{3 \sqrt{3}}$**

**Detailed Solution:**

$\frac{d y}{d x}-y \tan x=2 x \sec x$

I.F. $=e^{-\int \tan x d x}=\cos x$

$\therefore \quad y \cdot \cos x=\int 2 x d x=x^{2}+c$

Now, $y(0)=0 \Rightarrow c=0, \therefore y=x^{2} \sec x$

$\Rightarrow y^{\prime}=2 x \sec x+x^{2} \sec x \tan x$

Now, $y\left(\frac{\pi}{4}\right)=\frac{\pi^{2}}{16} \times \sqrt{2}=\frac{\pi^{2}}{8 \sqrt{2}}$

$y\left(\frac{\pi}{3}\right)=\frac{\pi^{2}}{9} \times 2=\frac{2 \pi^{2}}{9}$

$y^{\prime}\left(\frac{\pi}{4}\right)=\frac{2 \pi}{4} \times \sqrt{2}+\frac{\pi^{2}}{8 \sqrt{2}} \times 1=\frac{\pi^{2}}{8 \sqrt{2}}+\frac{\pi}{\sqrt{2}}$

$y^{\prime}\left(\frac{\pi}{3}\right)=\frac{2 \pi}{3} \times 2+\frac{2 \pi^{2}}{9} \times \sqrt{3}=\frac{2 \pi^{2}}{3 \sqrt{3}}+\frac{4 \pi}{3}$

</details>

---

