# JEE Advanced Mathematics - Definite Integration

## Topic 3: Properties of Definite Integration

**Total Questions:** 22

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of the definite integral
$\displaystyle\int_{0}^{2} \dfrac{1}{3^{\frac{x+3}{2}}}\, dx$
is

**Options:**

- **(A)** $\dfrac{1}{2}$
- **(B)** $\dfrac{1}{3}$
- **(C)** $\dfrac{\log_e 3}{3}$
- **(D)** $\dfrac{\log_e 3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{3}$**

**Detailed Solution:**

Let $I = \int_{0}^{2} \dfrac{1}{3^x + 3} dx$

Substitute $t = 3^x$, which gives $dt = 3^x \ln 3 dx \Rightarrow dx = \dfrac{dt}{t \ln 3}$.

When $x = 0$, $t = 1$.

When $x = 2$, $t = 9$.

The integral becomes:

$I = \int_{1}^{9} \dfrac{1}{t + 3} \dfrac{dt}{t \ln 3} = \dfrac{1}{\ln 3} \int_{1}^{9} \dfrac{1}{t(t + 3)} dt$

Using partial fractions:

$\dfrac{1}{t(t + 3)} = \dfrac{1}{3} \left( \dfrac{1}{t} - \dfrac{1}{t + 3} \right)$

$I = \dfrac{1}{3 \ln 3} \int_{1}^{9} \left( \dfrac{1}{t} - \dfrac{1}{t + 3} \right) dt$

$I = \dfrac{1}{3 \ln 3} [\ln t - \ln(t + 3)]_{1}^{9}$

$I = \dfrac{1}{3 \ln 3} \left[ \ln\left(\dfrac{t}{t + 3}\right) \right]_{1}^{9}$

$I = \dfrac{1}{3 \ln 3} \left( \ln\left(\dfrac{9}{12}\right) - \ln\left(\dfrac{1}{4}\right) \right)$

$I = \dfrac{1}{3 \ln 3} \left( \ln\left(\dfrac{3}{4}\right) - \ln\left(\dfrac{1}{4}\right) \right)$

$I = \dfrac{1}{3 \ln 3} \ln\left(\dfrac{3/4}{1/4}\right) = \dfrac{1}{3 \ln 3} \ln 3$

$I = \dfrac{1}{3}$

</details>

---

### Q2. JEE Advanced 2025 (Paper 2)

*Type:* `numerical` | *Level:* `3`

If $\alpha=\int_{\frac{1}{2}}^2 \frac{\tan ^{-1} x}{2 x^2-3 x+2} d x$ 
then the value of $\sqrt{7} \tan \left(\frac{2 \alpha \sqrt{7}}{\pi}\right)$ is ____________.
(Here, the inverse trigonometric function $\tan ^{-1} x$ assumes values in $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$.)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **21**

**Detailed Solution:**

$\alpha=\int_{\frac{1}{2}}^2 \frac{\tan ^{-1} x}{2 x^2-3 x+2} d x$ ....(i)
$\begin{aligned} & \text { Let } x=\frac{1}{t} \\ & \qquad d x=-\frac{1}{t^2} d t \\ & \alpha=\int_2^{\frac{1}{2}} \frac{\tan ^{-1}\left(\frac{1}{t}\right)}{\frac{2}{t^2}-\frac{3}{t}+2}\left(\frac{-1}{t^2}\right) d t\end{aligned}$
$\alpha=\int_{\frac{1}{2}}^2 \frac{\cot ^{-1} \mathrm{t}}{2 \mathrm{t}^2-3 \mathrm{t}+2} \mathrm{dt}$ ....(ii)
Now by (i) + (ii)
$\begin{aligned}
& 2 \alpha=\int_{\frac{1}{2}}^2 \frac{\frac{\pi}{2}}{2 x^2-3 x+2} d x \\
& \alpha=\frac{\pi}{8} \int_{\frac{1}{2}}^2 \frac{d x}{x^2-\frac{3 x}{2}+1} \\
& \alpha=\frac{\pi}{8} \int_{\frac{1}{2}}^2\left(x-\frac{3}{4}\right)^2+\frac{7}{16} \\
& \alpha=\frac{\pi}{8 \times \frac{\sqrt{7}}{4}}\left[\tan ^{-1}\left(\frac{x-\frac{3}{4}}{\frac{\sqrt{7}}{4}}\right)\right]_{\frac{1}{2}}^2
\end{aligned}$
$\begin{aligned}
& \alpha=\frac{\pi}{2 \sqrt{7}}\left[\tan ^{-1} \frac{4 x-3}{\sqrt{7}}\right]_{\frac{1}{2}}^2 \\
& \alpha=\frac{\pi}{2 \sqrt{7}}\left[\tan ^{-1} \frac{5}{\sqrt{7}}-\tan ^{-1}\left(-\frac{1}{\sqrt{7}}\right)\right] \\
& \alpha=\frac{\pi}{2 \sqrt{7}} \tan ^{-1} \frac{\left(\frac{5}{\sqrt{7}}+\frac{1}{\sqrt{7}}\right)}{1-\frac{5}{7}} \\
& \alpha=\frac{\pi}{2 \sqrt{7}} \tan ^{-1}(3 \sqrt{7})
\end{aligned}$
Now $\sqrt{7} \tan \left(\frac{2 \sqrt{7} \alpha}{\pi}\right)$
$\begin{aligned}
& \sqrt{7} \times \tan \left(\tan ^{-1}(3 \sqrt{7})\right) \\
& \sqrt{7} \times 3 \sqrt{7} \\
& =21
\end{aligned}$

</details>

---

### Q3. JEE Advanced 2024 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let \(f:\left[0, \frac{\pi}{2}\right] \rightarrow[0,1]\) be the function defined by \(f(x)=\sin ^2 x\) and let \(g:\left[0, \frac{\pi}{2}\right] \rightarrow[0, \infty)\) be the function defined by \(g(x)=\sqrt{\frac{\pi x}{2}-x^2}\).
The value of $\frac{16}{\pi^3} \int_0^{\frac{\pi}{2}} f(x) g(x) d x$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.25**

**Detailed Solution:**

Now $I_1=\int_0^{\frac{\pi}{2}} f(x) \cdot g(x) d x=\frac{1}{2} \int_0^{\frac{\pi}{2}} g(x) d x$ (it is explained in previous question solution)
i.e. $\frac{1}{2} \int_0^{\frac{\pi}{2}} \sqrt{\left(\frac{\pi}{4}\right)^2-\left(x-\frac{\pi}{4}\right)^2} \mathrm{dx}$
Using $\int \sqrt{a^2-x^2}=\frac{1}{2}\left(x \sqrt{a^2-x^2}+a^2 \sin ^{-1}\left(\frac{x}{a}\right)\right)+C$
$\Rightarrow \frac{1}{2}\left[\frac{\left(x-\frac{\pi}{4}\right)}{2} \sqrt{\frac{\pi x}{2}-x^2}+\frac{\frac{\pi^2}{2}}{2} \sin ^{-1}\left(\frac{x-\frac{\pi}{4}}{\frac{\pi}{4}}\right)\right]_0^{\pi / 2}$
$\begin{aligned} & \Rightarrow \frac{1}{2}\left[\left(0+\frac{\pi^3}{64}\right)-\left(0+\left(\frac{-\pi^3}{64}\right)\right)\right] \\ & \Rightarrow \frac{1}{2} \times \frac{\pi^3}{32}\end{aligned}$
Now $\frac{16}{\pi^3} \times \frac{\pi^3}{64}=\frac{1}{4}=0.25$

</details>

---

### Q4. JEE Advanced 2024 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Paragraph: Let \(f:\left[0, \frac{\pi}{2}\right] \rightarrow[0,1]\) be the function defined by \(f(x)=\sin ^2 x\) and let \(g:\left[0, \frac{\pi}{2}\right] \rightarrow[0, \infty)\) be the function defined by \(g(x)=\sqrt{\frac{\pi x}{2}-x^2}\).
Question: The value of $2 \int_0^{\frac{\pi}{2}} f(x) g(x) d x-\int_0^{\frac{\pi}{2}} g(x) d x$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

$I=2 \int_0^{\frac{\pi}{2}} \underbrace{\sin ^2 x \cdot \sqrt{\frac{\pi x}{2}-x^2}}_{I_1}-\int_0^{\frac{\pi}{2}} g(x) d x$
Let $I_1=\int_0^{\frac{\pi}{2}} \sin ^2 x \sqrt{\left(\frac{\pi}{4}\right)^2-\left(x-\frac{\pi}{4}\right)^2}$
(making perfect square)
apply kings
$I_1=\int_0^{\frac{\pi}{2}} \cos ^2 x \sqrt{\left(\frac{\pi}{4}\right)^2-\left(\frac{\pi}{2}-x\right)^2}$
add both
$2 I_1=\int_0^{\frac{\pi}{2}} \sqrt{\left(\frac{\pi}{4}\right)^2-\left(x-\frac{\pi}{4}\right)^2}$
i.e. $2 I_1=\int_0^{\frac{\pi}{2}} g(x)$
Now $I=2 I_1-\int_0^{\frac{\pi}{2}} g(x)=0$

</details>

---

### Q5. JEE Advanced 2022 (Paper 2)

*Type:* `numerical` | *Level:* `2`

The greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mrow><msub><mi>log</mi><mn>2</mn></msub><mn>9</mn></mrow></msubsup><msup><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mi>d</mi><mi>x</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mrow><msub><mi>log</mi><mn>2</mn></msub><mn>9</mn></mrow></msubsup><msup><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mrow><msub><mi>log</mi><mn>2</mn></msub><mn>9</mn></mrow></msubsup><msup><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mi>d</mi><mi>x</mi><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn><mo>=</mo><msup><mi>t</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mi>x</mi></msup><mi>ln</mi><mn>2</mn><mi>d</mi><mi>x</mi><mo>=</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup></mrow><mrow><mfenced><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>ln</mi><mn>2</mn></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mrow><mn>3</mn><msup><mi>t</mi><mn>3</mn></msup></mrow><mrow><mi>ln</mi><mn>2</mn><mfenced><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi></math> </p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mrow><mn>3</mn><msup><mi>t</mi><mn>3</mn></msup></mrow><mrow><mi>ln</mi><mn>2</mn><mfenced><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>t</mi><mo>&#183;</mo><mfrac><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup></mrow><mrow><mfenced><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>ln</mi><mn>2</mn></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mi>t</mi><mo>&#8901;</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msub><mi>log</mi><mn>2</mn></msub><mn>9</mn><mo>-</mo><mn>1</mn><msub><mi>log</mi><mn>2</mn></msub><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msub><mi>log</mi><mn>2</mn></msub><mn>9</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>4</mn><msub><mi>log</mi><mn>2</mn></msub><mn>3</mn><mo>-</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>I</mi></mfenced><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q6. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `3`

For any real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denotes the largest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mfenced close="]" open="["><msqrt><mfrac><mrow><mn>10</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt></mfenced><mi>d</mi><mi>x</mi></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>I</mi></math> is ____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **182**

**Detailed Solution:**

<p>Given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mfenced close="]" open="["><msqrt><mfrac><mrow><mn>10</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt></mfenced><mi>d</mi><mi>x</mi></math></p><p>Check the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> at which the greatest integer function becomes integer.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>10</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>1</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>10</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>4</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>10</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>9</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>9</mn></mfrac></msubsup><mn>0</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mfrac><mn>2</mn><mn>3</mn></mfrac></msubsup><mn>1</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mn>9</mn></msubsup><mn>2</mn><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>9</mn><mn>10</mn></msubsup><mn>3</mn><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>0</mn><mo>+</mo><mo>[</mo><mi>x</mi><msubsup><mo>]</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mfrac><mn>2</mn><mn>3</mn></mfrac></msubsup><mo>+</mo><mo>[</mo><mn>2</mn><mi>x</mi><msubsup><mo>]</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mn>9</mn></msubsup><mo>+</mo><mo>[</mo><mn>3</mn><mi>x</mi><msubsup><mo>]</mo><mn>9</mn><mn>10</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>+</mo><mn>18</mn><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>+</mo><mn>30</mn><mo>-</mo><mn>27</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>21</mn><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>=</mo><mfrac><mn>182</mn><mn>9</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>I</mi><mo>=</mo><mn>182</mn></math></p>

</details>

---

### Q7. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let $g_{i}:\left[\frac{\pi}{8}, \frac{3 \pi}{8}\right] \rightarrow \mathbb{R}, i=1,2$, and $f:\left[\frac{\pi}{8}, \frac{3 \pi}{8}\right] \rightarrow \mathbb{R}$ be functions such that $g_{1}(x)=1, g_{2}(x)=|4 x-\pi|$ and $f(x)=\sin ^{2} x$, for all $x \in\left[\frac{\pi}{8}, \frac{3 \pi}{8}\right]$

Define

$

S_{i}=\int_{\frac{\pi}{8}}^{\frac{3 \pi}{8}} f(x) \cdot g_{i}(x) d x, \quad i=1,2

$

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>48</mn><msub><mi>S</mi><mn>2</mn></msub></mrow><msup><mi>&#960;</mi><mn>2</mn></msup></mfrac></math> is ____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1.5**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac></msubsup><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mfenced close="|" open="|"><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac></msubsup><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mfenced close="|" open="|"><mrow><mn>4</mn><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac></msubsup><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mfenced close="|" open="|"><mrow><mi>&#960;</mi><mo>-</mo><mn>4</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mi>ii</mi></mfenced></math></p><p>From (i) and (ii), we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac></msubsup><mfenced close="|" open="|"><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/05ec2187-483d-40f6-aa6f-8e7af8661afb-image.png" style="width: 420px; height: 300px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">S</mi></mrow><mn>2</mn></msub><mo>=</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>32</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>48</mn><msub><mi>S</mi><mn>2</mn></msub></mrow><msup><mi>&#960;</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>48</mn><mn>32</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>48</mn><msub><mi mathvariant="normal">S</mi><mn>2</mn></msub></mrow><msup><mi>&#960;</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>=</mo><mn>1</mn><mo>.</mo><mn>5</mn></math></p>

</details>

---

### Q8. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let $g_{i}:\left[\frac{\pi}{8}, \frac{3 \pi}{8}\right] \rightarrow \mathbb{R}, i=1,2$, and $f:\left[\frac{\pi}{8}, \frac{3 \pi}{8}\right] \rightarrow \mathbb{R}$ be functions such that $g_{1}(x)=1, g_{2}(x)=|4 x-\pi|$ and $f(x)=\sin ^{2} x$, for all $x \in\left[\frac{\pi}{8}, \frac{3 \pi}{8}\right]$

Define

$$

S_{i}=\int_{\frac{\pi}{8}}^{\frac{3 \pi}{8}} f(x) \cdot g_{i}(x) d x, \quad i=1,2

$$

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>16</mn><msub><mi>S</mi><mn>1</mn></msub></mrow><mi>&#960;</mi></mfrac></math> is ___.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac></msubsup><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>&#183;</mo><mn>1</mn><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac></msubsup><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac></msubsup><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>From (i) and (ii), we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac></msubsup><mn>1</mn><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>16</mn><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">S</mi></mrow><mn>1</mn></msub></mrow><mi>&#960;</mi></mfrac><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q9. JEE Advanced 2019 (Paper 2)

*Type:* `numerical` | *Level:* `3`

The value of the integral <math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mrow><mrow><mi>&#960;</mi></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></munderover><mrow><mfrac><mrow><mn>3</mn><msqrt><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msqrt><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt><mo>+</mo><msqrt><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac><mi>d</mi><mi>&#952;</mi></mrow></mrow></math> equals

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.5**

**Detailed Solution:**

<math><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mn>3</mn><msqrt><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msqrt><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt><mo>+</mo><msqrt><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac></mrow></mrow><mo>.</mo><mi>d</mi><mi>&#952;</mi></math> &hellip;(i)
<math><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mn>3</mn><msqrt><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msqrt><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt><mo>+</mo><msqrt><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac></mrow></mrow><mo>.</mo><mi>d</mi><mi>&#952;</mi></math> &hellip;(ii) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>using</mi><mi mathvariant="normal">&#160;</mi><munderover><mo>&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>.</mo><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo>&#8747;</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>.</mo><mi>d</mi><mi>x</mi></math>
(i) <math><mo>+</mo></math> (ii)
<math><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mn>3</mn><mfenced separators="|"><mrow><msqrt><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt><mo>+</mo><msqrt><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt></mrow></mfenced></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msqrt><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt><mo>+</mo><msqrt><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac><mo>.</mo><mi>d</mi><mi>&#952;</mi></mrow></mrow></math>
<math><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mn>3</mn><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mi>d</mi><mi>&#952;</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msqrt><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt><mo>+</mo><msqrt><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac></mrow></mrow></math>
<math><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>I</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi><mo>.</mo></mrow></mrow><mi>d</mi><mi>&#952;</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msqrt><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></msqrt></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac></mrow></mrow></math>
Put <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi><mo>=</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>
<math><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi><mo>.</mo><mi>d</mi><mi>&#952;</mi><mo>=</mo><mn>2</mn><mi>t</mi><mo>.</mo><mi>d</mi><mi>t</mi></mrow></mrow></math>
when
<math><mtable><mtr><mtd><mi>&#952;</mi><mo>&#8594;</mo><mn>0</mn><mo>,</mo></mtd><mtd><mi>t</mi><mo>&#8594;</mo><mn>0</mn></mtd></mtr></mtable></math>
<math><mtable><mtr><mtd><mi>&#952;</mi><mo>&#8594;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo></mtd><mtd><mi>t</mi><mo>&#8594;</mo><mi>&#8734;</mi></mtd></mtr></mtable></math>
<math><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>I</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><mfrac><mrow><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac></mrow></mrow></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>I</mi><mn>3</mn></mfrac><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mi>&#8734;</mi></munderover><mfrac><mrow><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn></mrow><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced><mn>4</mn></msup></mfrac><mo>.</mo><mi>d</mi><mi>t</mi></math>
<math><mfrac><mrow><mi>I</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac><mo>.</mo><mi>d</mi><mi>t</mi></mrow></mrow></math>
<math><mfrac><mrow><mi>I</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mi>&#8734;</mi></mrow></msubsup></math>
<math><mfrac><mrow><mi>I</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>+</mo><mn>0</mn><mo>-</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow></mfenced></math>
<math><mfrac><mrow><mi>I</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

</details>

---

### Q10. JEE Advanced 2019 (Paper 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mn>2</mn><mi mathvariant="normal">&#960;</mi></mfrac><munderover><mo stretchy="true">&#8747;</mo><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></munderover><mfrac><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">e</mi><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">x</mi></mrow></msup></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi mathvariant="normal">x</mi></mrow></mfenced></mrow></mfrac></math> then find <math><mn>27</mn><msup><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>2</mn></mrow></msup></math> equals____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>&#960;</mi></mrow></mfrac><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>&#8901;</mo><mi>d</mi><mi>x</mi></mrow></mrow></math>
Using <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8747;</mo><mrow><mo>-</mo><mi>a</mi></mrow><mi>a</mi></munderover><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>&#8901;</mo><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>a</mi></munderover><mfenced><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>&#8901;</mo><mi>d</mi><mi>x</mi></math>
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>&#960;</mi></mrow></mfrac><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></munderover><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfrac></mrow></mfenced><mo>&#8901;</mo><mi>d</mi><mi>x</mi></mrow></mrow></math>
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>&#960;</mi></mrow></mfrac><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></munderover><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup></mrow><mrow><mfenced separators="|"><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfrac></mrow></mfenced><mo>&#8901;</mo><mi>d</mi><mi>x</mi></mrow></mrow></math>
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>&#960;</mi></mrow></mfrac><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>x</mi></mrow></mfrac></mrow></mrow></math>
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>&#960;</mi></mrow></mfrac><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>-</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>&#960;</mi></mrow></mfrac><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi></mrow></mfrac></mrow></mrow></mrow></mrow></math>
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>&#960;</mi></mrow></mfrac><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>t</mi><mi>a</mi><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi></mrow></mfrac></mrow></mrow></math>
Put <math><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">&#160;</mi><mi>x</mi><mo>=</mo><mi>t</mi></math>
<math><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></mrow></mrow><mi>&#160;</mi></math>
and when <math><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>0</mn></math>
<math><mi>x</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>1</mn></math>
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>&#960;</mi></mrow></mfrac><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mrow></math>
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>&#960;</mi></mrow></mfrac><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><msqrt><mn>3</mn></msqrt><mi>t</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mrow></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>2</mn><mi>&#960;</mi></mfrac><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><msubsup><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mn>3</mn></msqrt><mi>t</mi></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi mathvariant="normal">&#160;</mi><mfenced><mrow><mo>&#8757;</mo><mtext>&#8201;&#8201;</mtext><munderover><mo stretchy="true">&#8747;</mo><mn>0</mn><mn>1</mn></munderover><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><mi>a</mi></mfrac><mo>+</mo><mi>C</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>2</mn><mrow><msqrt><mn>3</mn></msqrt><mi>&#960;</mi></mrow></mfrac><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><msqrt><mn>3</mn></msqrt></mfenced><mo>-</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mn>0</mn></mfenced></mrow></mfenced></math>
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mn>3</mn></msqrt><mi>&#960;</mi></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
<math><mn>27</mn><msup><mrow><mi>I</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>27</mn><mo>&#215;</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>27</mn></mrow></mfrac><mo>=</mo><mn>4</mn></math>

</details>

---

### Q11. JEE Advanced 2018 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mo>:</mo><mi mathvariant="double-struck">R</mi><mo>&#8594;</mo><mi mathvariant="double-struck">R</mi><mi mathvariant="double-struck">&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi>&#160;</mi><mi>g</mi><mo>:</mo><mi mathvariant="double-struck">R</mi><mo>&#8594;</mo><mi mathvariant="double-struck">R</mi></math> be two non-constant differentiable functions. If <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><msup><mrow><mi>e</mi></mrow><mrow><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>-</mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></msup></mrow></mfenced><msup><mrow><mi>g</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>&#160;</mi><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi><mi>&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">l</mi><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mi mathvariant="double-struck">R</mi></math>, and <math><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mi>g</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math> then which of the following statement(s) is (are) TRUE?

**Options:**

- **(A)** <math><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>&lt;</mo><mn>1</mn><mo>-</mo><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow></math>
- **(B)** <math><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>&gt;</mo><mn>1</mn><mo>-</mo><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow></math>
- **(C)** <math><mi>g</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&gt;</mo><mn>1</mn><mo>-</mo><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow></math>
- **(D)** <math><mi>g</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&lt;</mo><mn>1</mn><mo>-</mo><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>g</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&gt;</mo><mn>1</mn><mo>-</mo><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow></math>**

**Detailed Solution:**

<math><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></msup><msup><mrow><mi>g</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>∀</mo><mi>x</mi><mo>∈</mo><mi mathvariant="double-struck">R</mi></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></msup><mo>.</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></msup><msup><mrow><mi>g</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mrow><mo stretchy="false">∫</mo><mrow><mfenced separators="|"><mrow><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></msup><msup><mrow><mi>f</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></msup><mo>.</mo><msup><mrow><mi>g</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>C</mi></mrow></mrow></math> 
 <math><mo>⇒</mo><mi> </mi><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></msup></mrow></msup><mo>=</mo><mi>C</mi></math> 
 <math><mo>⇒</mo><mi> </mi><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></mrow></msup><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>g</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></mrow></msup><mo>=</mo><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow></msup><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>g</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow></msup></math> 
 <math><mo>⇒</mo><mi> </mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>g</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></mrow></msup><mo>=</mo><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow></msup><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow></msup><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>g</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></mrow></msup><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math> 
 <math><mo>∴</mo><mi> </mi><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow></msup><mo>&lt;</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>e</mi></mrow></mfrac><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>g</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></mrow></msup><mo>&lt;</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math> 
 <math><mo>⇒</mo><mi> </mi><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>&lt;</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow><mo>-</mo><mn>1</mn><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mo>-</mo><mi>g</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&lt;</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow><mo>-</mo><mn>1</mn></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>&gt;</mo><mn>1</mn><mo>-</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><mi>g</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&gt;</mo><mn>1</mn><mo>-</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mn>2</mn></mrow></mrow></math>

</details>

---

### Q12. JEE Advanced 2017 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Let <math><mi>f</mi><mi mathvariant="double-struck">&#160;</mi><mo>:</mo><mi mathvariant="double-struck">&#160;</mi><mi mathvariant="double-struck">R</mi><mo>&#8594;</mo><mi mathvariant="double-struck">R</mi></math> be a differentiable function such that <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>3</mn></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mi>x</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><msup><mi>f</mi><mi>&#8242;</mi></msup><mfenced separators="|"><mi>t</mi></mfenced><mi>c</mi><mi>o</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi>t</mi><mo>-</mo><mi>cot</mi><mi>t</mi><mi>&#160;</mi><mi>c</mi><mi>o</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi>t</mi><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mi>t</mi></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi></math> , for <math><mi>x</mi><mo>&#8712;</mo><mfenced close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> then <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mo>=</mo><mi>&#160;</mi><msubsup><mo>&#8747;</mo><mi>x</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mrow><mo>[</mo><msup><mi>f</mi><mo>'</mo></msup><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mi>c</mi><mi>o</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi>&#160;</mi><mi>t</mi><mo>&#8722;</mo><mi>f</mi><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mi>c</mi><mi>o</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi>&#160;</mi><mi>t</mi><mtext>&#160;cot</mtext><mi>&#160;</mi><mi>t</mi><mo>]</mo></mrow><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>cos</mi><mi>e</mi><mi>c</mi><mi>t</mi></mrow></mfenced><mi>x</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup></math></p><p><math><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mi>c</mi><mi>o</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac><mo>=</mo><mn>3</mn><mo>-</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><mo>-</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow><mrow><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfrac><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced></mrow><mrow><mi>cos</mi><mo>&#8289;</mo><mi>x</mi></mrow></mfrac><mo>;&#160;</mo><mi>a</mi><mi>s</mi><mi>&#160;</mi><msup><mi>f</mi><mi>&#39;</mi></msup><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mn>3</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q13. JEE Advanced 2016 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></mrow></mfrac></mrow></mrow><mi>&#160;</mi><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mn>2</mn></math>
- **(B)** <math><mfrac><mrow><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mn>2</mn></math>
- **(C)** <math><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></math>
- **(D)** <math><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

Let <math> <mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><munderover> <mo>&#8747;</mo> <mrow> <mo>&#8722;</mo><mtext>&#8201;</mtext><mfrac> <mi>x</mi> <mn>2</mn> </mfrac> </mrow> <mrow> <mfrac> <mi>x</mi> <mn>2</mn> </mfrac> </mrow> </munderover> <mrow> <mfrac> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mi>cos</mi><mi>x</mi> </mrow> <mrow> <mn>1</mn><mo>+</mo><msup> <mi>e</mi> <mi>x</mi> </msup> </mrow> </mfrac> <mi>d</mi><mi>x</mi> </mrow> </mrow> </mstyle></math>
Replacing <math><mi>x</mi></math> by <math><mo>-</mo><mi>x</mi></math>
<math> <mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><munderover> <mo>&#8747;</mo> <mrow> <mo>&#8722;</mo><mfrac> <mi>&#960;</mi> <mn>2</mn> </mfrac> </mrow> <mrow> <mfrac> <mi>&#960;</mi> <mn>2</mn> </mfrac> </mrow> </munderover> <mrow> <mrow><mo>(</mo> <mrow> <mfrac> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mi>cos</mi><mi>x</mi> </mrow> <mrow> <mn>1</mn><mo>+</mo><msup> <mi>e</mi> <mrow> <mo>&#8722;</mo><mi>x</mi> </mrow> </msup> </mrow> </mfrac> </mrow> <mo>)</mo><mi>d</mi><mi>x</mi></mrow> </mrow> </mrow> </mstyle> </math>
<math> <mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><munderover> <mo>&#8747;</mo> <mrow> <mo>&#8722;</mo><mfrac> <mi>&#960;</mi> <mn>2</mn> </mfrac> </mrow> <mrow> <mfrac> <mi>&#960;</mi> <mn>2</mn> </mfrac> </mrow> </munderover> <mrow> <mrow><mo>(</mo> <mrow> <mfrac> <mn>1</mn> <mrow> <mn>1</mn><mo>+</mo><msup> <mi>e</mi> <mi>x</mi> </msup> </mrow> </mfrac> <mo>+</mo><mfrac> <mn>1</mn> <mrow> <mn>1</mn><mo>+</mo><msup> <mi>e</mi> <mrow> <mo>&#8722;</mo><mi>x</mi> </mrow> </msup> </mrow> </mfrac> </mrow> <mo>)</mo></mrow><msup> <mi>x</mi> <mn>2</mn> </msup> <mi>cos</mi><mi>x</mi><mtext>&#8201;</mtext><mi>d</mi><mi>x</mi> </mrow> </mrow> </mstyle> </math>
<math> <mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mstyle displaystyle="true"> <mrow><munderover> <mo>&#8747;</mo> <mrow> <mo>&#8722;</mo><mfrac> <mi>&#960;</mi> <mn>2</mn> </mfrac> </mrow> <mrow> <mfrac> <mi>&#960;</mi> <mn>2</mn> </mfrac> </mrow> </munderover> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mi>cos</mi><mi>x</mi><mtext>&#8201;</mtext><mi>d</mi><mi>x</mi> </mrow> </mrow> </mstyle> </math>, (even function)
<math> <mi>I</mi> </math> <math><mo>=</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mi>&#160;</mi><mi>d</mi><mi>x</mi></mrow></mrow><mo>=</mo><msubsup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msubsup><mo>-</mo><mn>2</mn><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mi>x</mi><mo>.</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mi>&#160;</mi><mi>d</mi><mi>x</mi></mrow></mrow></math>
(Using integration by parts, taking <math> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>=</mo><mn>u</mn><mo>,</mo><mi>cos</mi><mtext>&#8201;</mtext><mi>x</mi><mtext>&#8201;</mtext><mi>d</mi><mi>x</mi><mtext>&#8201;</mtext><mo>=</mo><mtext>&#8201;</mtext><mi>d</mi><mi>v</mi> </math> )
<math><mo>=</mo><mfrac><mrow><msup><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><msubsup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>.</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msubsup><mo>+</mo><mi>&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mn>1</mn><mo>.</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow><mrow><mi>d</mi></mrow><mrow><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mn>2</mn></mrow></mfenced></math>

</details>

---

### Q14. JEE Advanced 2015 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

The option(s) with the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> that satisfy the following equation is(are) <math><mfrac><mrow><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>4</mn><mi>&#960;</mi></mrow></munderover><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>6</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>a</mi><mi>t</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>a</mi><mi>t</mi></mrow></mrow></mrow></mrow></mrow></mfenced><mi>&#160;</mi><mi>d</mi><mi>t</mi></mrow></mrow></mrow><mrow><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>&#960;</mi></mrow></munderover><mrow><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>6</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>a</mi><mi>t</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>a</mi><mi>t</mi></mrow></mrow></mrow></mrow></mrow></mfenced><mi>&#160;</mi><mi>d</mi><mi>t</mi></mrow></mrow></mrow></mfrac><mo>=</mo><mi>L</mi><mi>&#160;</mi><mo>?</mo></math>

**Options:**

- **(A)** <math><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi> </mi><mi>L</mi><mo>=</mo><mi> </mi><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>4</mn><mi>π</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>π</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math>
- **(B)** <math><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi> </mi><mi>L</mi><mo>=</mo><mi> </mi><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>4</mn><mi>π</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>π</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mi> </mi></math>
- **(C)** <math><mi>a</mi><mo>=</mo><mn>4</mn><mo>,</mo><mi> </mi><mi>L</mi><mo>=</mo><mi> </mi><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>4</mn><mi>π</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>π</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math>
- **(D)** <math><mi>a</mi><mo>=</mo><mn>4</mn><mo>,</mo><mi> </mi><mi>L</mi><mo>=</mo><mi> </mi><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>4</mn><mi>π</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>π</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>a</mi><mo>=</mo><mn>4</mn><mo>,</mo><mi> </mi><mi>L</mi><mo>=</mo><mi> </mi><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>4</mn><mi>π</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>π</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>l</mi><mo>=</mo><mrow><msubsup><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>4</mn><mi>π</mi></mrow></msubsup><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup><mi> </mi><mfenced separators="|"><mrow><mi>s</mi><mi>i</mi><msup><mrow><mi>n</mi></mrow><mrow><mn>6</mn></mrow></msup><mn>2</mn><mi>t</mi><mo>+</mo><mi>c</mi><mi>o</mi><msup><mrow><mi>s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi> </mi><mn>2</mn><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mrow></math>  =  <math><mi> </mi><mi> </mi><msub><mrow><mi>l</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msub><mi> </mi><msub><mrow><mo>+</mo><mi> </mi><mi>l</mi></mrow><mrow><mn>3</mn></mrow></msub><mi> </mi><msub><mrow><mo>+</mo><mi> </mi><mi>l</mi></mrow><mrow><mn>4</mn></mrow></msub><mi> </mi><mi> </mi></math> 
 <math><mi>W</mi><mi>h</mi><mi>e</mi><mi>r</mi><mi>e</mi><mi> </mi><msub><mrow><mi>l</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mrow><msubsup><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mi>π</mi></mrow></msubsup><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup><mi> </mi><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>6</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow></mrow></mfenced><mi>d</mi><mi>t</mi><mi> </mi><mi> </mi><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><msub><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mrow><msubsup><mo stretchy="false">∫</mo><mrow><mi>π</mi></mrow><mrow><mn>2</mn><mi>π</mi></mrow></msubsup><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup><mi> </mi><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>6</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>t</mi><mo>+</mo><msup><mrow><mi>c</mi><mi>o</mi><mi>s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi> </mi><mn>2</mn><mi>t</mi></mrow></mrow></mrow></mfenced><mi> </mi><mi>d</mi><mi>t</mi><mi> </mi><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><mi> </mi><msub><mrow><mi>l</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mrow><msubsup><mo stretchy="false">∫</mo><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn><mi>π</mi></mrow></msubsup><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>6</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>t</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>t</mi></mrow></mrow></mrow></mrow></mrow></mfenced><mi>d</mi><mi>t</mi><mi> </mi><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><msub><mrow><mi>l</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mrow><msubsup><mo stretchy="false">∫</mo><mrow><mn>3</mn><mi>π</mi></mrow><mrow><mn>4</mn><mi>π</mi></mrow></msubsup><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup><mfenced separators="|"><mrow><msup><mrow><mi>s</mi><mi>i</mi><mi>n</mi></mrow><mrow><mn>6</mn><mi> </mi></mrow></msup><mn>2</mn><mi>t</mi><mo>+</mo><msup><mrow><mi>c</mi><mi>o</mi><mi>s</mi></mrow><mrow><mn>4</mn></mrow></msup><mi> </mi><mn>2</mn><mi>t</mi></mrow></mfenced><mi> </mi><mi>d</mi><mi>t</mi></mrow></mrow></mrow></mrow></mrow></mrow></mrow></mrow></math> 
 <math><mi>t</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>π</mi></math> 
 <math><mi>d</mi><mi>t</mi><mo>=</mo><mi>d</mi><mi>x</mi></math> 
 <math><msub><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mrow><msubsup><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mi>π</mi></mrow></msubsup><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi><mo>+</mo><mi>π</mi></mrow></msup><mi> </mi><mfenced separators="|"><mrow><msup><mrow><mi>s</mi><mi>i</mi><mi>n</mi></mrow><mrow><mn>6</mn></mrow></msup><mi> </mi><mn>2</mn><mi>x</mi><mo>+</mo><msup><mrow><mi>c</mi><mi>o</mi><mi>s</mi></mrow><mrow><mn>4</mn><mi> </mi></mrow></msup><mn>2</mn><mi>x</mi></mrow></mfenced><mi> </mi><mi>d</mi><mi>x</mi><mo>=</mo><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mi>π</mi></mrow></msup><msub><mrow><mi>l</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mrow></math> 
 <math><mi>t</mi><mo>=</mo><mn>2</mn><mi>π</mi><mo>+</mo><mi>x</mi></math>  
 <math><msub><mrow><mi>l</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mi>π</mi></mrow></msup><msub><mrow><mi>l</mi></mrow><mrow><mn>1</mn></mrow></msub></math> 
 <math><msub><mrow><mi>l</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>3</mn><mi>π</mi></mrow></msup><msub><mrow><mi>l</mi></mrow><mrow><mn>1</mn></mrow></msub></math> 
 <math><mi>l</mi><mo>=</mo><msub><mrow><mi>l</mi></mrow><mrow><mn>1</mn></mrow></msub><mi> </mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>π</mi></mrow></msup><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mi>π</mi></mrow></msup><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>3</mn><mi>π</mi></mrow></msup></mrow></mfenced></math>  
 <math><mfrac><mrow><mi>l</mi></mrow><mrow><msub><mrow><mi>l</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>4</mn><mi>π</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>π</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math> 
The same for a = 4.

</details>

---

### Q15. JEE Advanced 2015 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Let <math><mi mathvariant="normal">f</mi><mi mathvariant="normal">&#160;</mi><mo>:</mo><mi mathvariant="double-struck">R</mi><mo>&#8594;</mo><mi mathvariant="double-struck">R</mi><mi mathvariant="normal">&#160;</mi></math> be a function defined by <math><mi mathvariant="normal">f</mi><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi></mrow></mfenced><mo>=</mo><mi mathvariant="normal">&#160;</mi><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mfenced close="]" open="[" separators="|"><mrow><mi mathvariant="normal">x</mi></mrow></mfenced><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mi mathvariant="normal">&#160;</mi><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo>&#62;</mo><mn>2</mn></mtd></mtr></mtable></mrow></mfenced></math> , where <math><mo>[</mo><mi mathvariant="normal">x</mi><mo>]</mo></math> is the greatest integer less than or equal to <math><mi mathvariant="normal">x</mi></math> . If <math><mi mathvariant="normal">I</mi><mo>=</mo><mi mathvariant="normal">&#160;</mi><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></munderover><mrow><mfrac><mrow><mi mathvariant="normal">x</mi><mi mathvariant="normal">f</mi><mo>(</mo><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>)</mo></mrow><mrow><mn>2</mn><mo>+</mo><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi><mo>,</mo></mrow></mrow></math> then the value of <math><mo>(</mo><mn>4</mn><mi mathvariant="normal">I</mi><mo>-</mo><mn>1</mn><mo>)</mo></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfenced open="{" close="" separators="|"><mtable><mtr><mtd><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn><mo>&#62;</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="{" close="" separators="|"><mtable><mtr><mtd><mfenced open="[" close="]" separators="|"><mi mathvariant="normal">x</mi></mfenced><mo>+</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo>&#8804;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo>&#62;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math>
<math><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi mathvariant="normal">x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi mathvariant="normal">x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mn>1</mn><mo>&#60;</mo><mi mathvariant="normal">x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced separators="|"><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfenced><mo>=</mo><mfenced open="{" close="" separators="|"><mtable><mtr><mtd><mfenced open="[" close="]" separators="|"><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfenced><mo>.</mo></mtd><mtd><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>&#62;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="{" close="" separators="|"><mtable><mtr><mtd><mfenced open="[" close="]" separators="|"><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfenced><mo>.</mo></mtd><mtd><mo>|</mo><mi mathvariant="normal">x</mi><mo>|</mo><mo>&#8804;</mo><msqrt><mn>2</mn></msqrt></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mo>|</mo><mi mathvariant="normal">x</mi><mo>|</mo><mo>&#62;</mo><msqrt><mn>2</mn></msqrt></mtd></mtr></mtable></mfenced></math>
<math> <mrow> <mo>=</mo> <mo>{</mo> <mtable> <mtr> <mtd> <mtext>0,</mtext> </mtd> <mtd> <mo>-</mo> <mn>1</mn> <mo>&#8804;</mo> <mtext>x</mtext> <mo>&#60;</mo> <mn>0</mn> </mtd> </mtr> <mtr> <mtd> <mtext>0,</mtext> </mtd> <mtd> <mn>0</mn> <mo>&#8804;</mo> <mtext>x</mtext> <mo>&#60;</mo> <mn>1</mn> </mtd> </mtr> <mtr> <mtd> <mtext>1,</mtext> </mtd> <mtd> <mn>1</mn> <mo>&#8804;</mo> <mtext>x</mtext> <mo>&#60;</mo> <msqrt> <mn>2</mn> </msqrt> </mtd> </mtr> <mtr> <mtd> <mtext>0,</mtext> </mtd> <mtd> <msqrt> <mn>2</mn> </msqrt> <mo>&#60;</mo> <mtext>x</mtext> <mo>&#60;</mo> <mn>2</mn> </mtd> </mtr> </mtable> </mrow> </math>
<math><mi mathvariant="normal">l</mi><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>0</mn></mrow></munderover><mrow><mn>0</mn><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow></mrow><mo>+</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mn>0</mn><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow></mrow><mo>+</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></munderover><mrow><mfrac><mrow><mi mathvariant="normal">x</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mn>0</mn></mrow></mfrac></mrow></mrow><mo>+</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>2</mn></mrow></munderover><mrow><mn>0</mn><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow></mrow></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></msubsup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
<math><mn>4</mn><mi mathvariant="normal">l</mi><mo>=</mo><mn>1</mn></math>
<math><mn>4</mn><mi mathvariant="normal">l</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

</details>

---

### Q16. JEE Advanced 2014 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

Match the following.
 <table border="1">	<tbody>		<tr>			<td> </td>			<td>List &ndash; I</td>			<td> </td>			<td>List &ndash; II</td>		</tr>		<tr>			<td>(A)</td>			<td>The number of polynomials f(x) with non &ndash; negative integer coefficients of degree <math><mo>&#8804;</mo><mn>2</mn><mo>,</mo></math> satisfying f(0) =0 and <math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo></mrow></mrow><mi>&#160;</mi><mi>i</mi><mi>s</mi></math></td>			<td>(P)</td>			<td>8</td>		</tr>		<tr>			<td>(B)</td>			<td>The number of point in the interval <math><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mi>&#160;</mi><msqrt><mn>13</mn></msqrt><mo>,</mo><mi>&#160;</mi><msqrt><mn>13</mn></msqrt></mrow></mfenced></math> at which <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>+</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mrow></mrow></mrow></math> attains its maximum value, is</td>			<td>(Q)</td>			<td>2</td>		</tr>		<tr>			<td>(C)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mrow><mo>-</mo><mn>2</mn></mrow><mn>2</mn></munderover><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi><mi>&#160;</mi></math> equals</td>			<td>(R)</td>			<td>4</td>		</tr>		<tr>			<td>(D)</td>			<td><math><mfrac><mrow><mfenced separators="|"><mrow><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi><mi>&#160;</mi><mo>.</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi><mi>&#160;</mi><mo>.</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow></mrow></mrow></mrow></mfenced></mrow></mfrac></math></td>			<td>(S)</td>			<td>0</td>		</tr>	</tbody></table>

**Options:**

- **(A)** a-r;b-p;c-s;d-q;
- **(B)** a-q;b-r;c-p;d-s;
- **(C)** a-p;b-r;c-q;d-s;
- **(D)** a-q;b-p;c-s;d-r;

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a-q;b-r;c-p;d-s;**

**Detailed Solution:**

<math><mfenced separators="|"><mrow><mi>P</mi></mrow></mfenced><mi> </mi><mi> </mi><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>a</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>,</mo><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi> </mi><mi>d</mi><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mrow></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>6</mn></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi> </mi><mi>b</mi></mrow></mfenced><mo>≡</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mn>2</mn></mrow></mfenced><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mi> </mi><mn>0</mn></mrow></mfenced></math>
<math><mfenced separators="|"><mrow><mi>Q</mi></mrow></mfenced><mi> </mi><mi> </mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mi> </mi></math>
For maximum value, <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mn>2</mn><mi>n</mi><mi>π</mi></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>2</mn><mi>n</mi><mi>π</mi><mo>+</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi>x</mi><mo>=</mo><mo>±</mo><mi> </mi><msqrt><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></msqrt><mo>,</mo><mi> </mi><mo>±</mo><mi> </mi><msqrt><mfrac><mrow><mn>9</mn><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></msqrt></math> as <math><mi>x</mi><mi> </mi><mi>ϵ</mi><mi> </mi><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>,</mo><mi> </mi><msqrt><mn>13</mn></msqrt></mrow></mfenced></math>
<math><mfenced separators="|"><mrow><mi>R</mi></mrow></mfenced><mi> </mi><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>2</mn></mrow></munderover><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow><mrow><munderover><mo stretchy="false">∫</mo><mrow><mn>0</mn></mrow><mrow><mn>2</mn></mrow></munderover><mrow><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mn>8</mn></mrow></mrow></math>
<math><mfenced separators="|"><mrow><mi>S</mi></mrow></mfenced><mi> </mi><mi> </mi><mi> </mi><mrow><munderover><mo stretchy="false">∫</mo><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></munderover><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>x</mi><mi> </mi><mi>I</mi><mi>n</mi><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></mrow></mrow></mrow></mrow></math> as it is an odd function.

</details>

---

### Q17. JEE Advanced 2014 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

<strong> Paragraph: </strong>

Given that for each $a \in(0,1)$,

$\lim _{h \rightarrow 0^{+}} \int_{h}^{1-h} t^{-a}(1-t)^{a-1} d t$

exists. Let this limit be $g(a)$. In addition, it is given that the function $g(a)$ is differentiable on $(0,1)$.


 <strong> Question: </strong>

The value of $g^{\prime}\left(\frac{1}{2}\right)$ is

**Options:**

- **(A)** <math><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mi>&#960;</mi></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

We have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>a</mi></mfenced><mo>=</mo><mi>g</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is differentiable.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>a</mi></mfenced><mo>=</mo><mo>-</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfenced></math>
Hence <math><msup><mrow><mi>g</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math>.

</details>

---

### Q18. JEE Advanced 2014 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

<strong> Paragraph: </strong>

Given that for each $a \in(0,1)$,

$\lim _{h \rightarrow 0^{+}} \int_{h}^{1-h} t^{-a}(1-t)^{a-1} d t$

exists. Let this limit be $g(a)$. In addition, it is given that the function $g(a)$ is differentiable on $(0,1)$.


 <strong> Question: </strong>

The value of $g\left(\frac{1}{2}\right)$ is

**Options:**

- **(A)** <math><mi>&#960;</mi></math>
- **(B)** <math><mn>2</mn><mi>&#960;</mi></math>
- **(C)** <math><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi>&#960;</mi></math>**

**Detailed Solution:**

<math><mi>g</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>h</mi><mo>&#8594;</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder></mrow><mo>&#8289;</mo><mrow><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mi>h</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>h</mi></mrow></munderover><mrow><msup><mrow><mi>t</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow></mrow><mi>&#160;</mi><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow></mrow><mi>&#160;</mi><mi>d</mi><mi>t</mi></math>
<math><mo>=</mo><msubsup><mrow><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msqrt><mi>t</mi><mo>-</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msqrt><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mi>t</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced close="|" open="" separators="|"><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>t</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfrac></mrow></mfenced></mrow></mfenced></mrow></mrow></mrow></mrow></mrow></mrow></mrow><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup></math>
<math><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>1</mn><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>(-1)</mn></mrow></mrow></mrow></mrow><mo>=</mo><mi>&#960;</mi></math>

</details>

---

### Q19. JEE Advanced 2012 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of the integral $\int_{-\pi / 2}^{\pi / 2}\left(x^{2}+\ln \frac{\pi+x}{\pi-x}\right) \cos x d x$ is

**Options:**

- **(A)** 0
- **(B)** $\frac{\pi^{2}}{2}-4$
- **(C)** $\frac{\pi^{2}}{2}+4$
- **(D)** $\frac{\pi^{2}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi^{2}}{2}-4$**

**Detailed Solution:**

$\int_{-\pi / 2}^{\pi / 2}\left[x^{2}+\ln \left(\frac{\pi+x}{\pi-x}\right)\right] \cos x d x$ $=\int_{-\pi / 2}^{\pi / 2} x^{2} \cos x d x+\int_{-\pi / 2}^{\pi / 2} \ln \left(\frac{\pi+x}{\pi-x}\right) \cos x d x$ $=2 \int_{0}^{\pi / 2} x^{2} \cos x d x+0 \quad\left[\because x^{2} \cos x\right.$ is an even function and $\ln \left(\frac{\pi+x}{\pi-x}\right) \cos x$ is an odd function] $=2\left[x^{2} \sin x+2 x \cos x-2 \sin x\right]_{0}^{\pi / 2}=\frac{\pi^{2}}{2}-4$

</details>

---

### Q20. JEE Advanced 2011 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{\sqrt{\log 2}}^{\sqrt{\log 3}} \frac{x \sin x^2}{\sin x^2+\sin \left(\log 6-x^2\right)} d x$ is

**Options:**

- **(A)** $\frac{1}{4} \log \frac{3}{2}$
- **(B)** $\frac{1}{2} \log \frac{3}{2}$
- **(C)** $\log \frac{3}{2}$
- **(D)** $\frac{1}{6} \log \frac{3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{4} \log \frac{3}{2}$**

**Detailed Solution:**

Put $x^2=t \Rightarrow x d x=\frac{d t}{2}$ $\therefore \quad I=\int_{\log 2}^{\log 3} \frac{\sin t \cdot \frac{d t}{2}}{\sin t+\sin (\log 6-t)}$
Using, $\quad \int_a^b f(x) d x=\int_a^b f(a+b-x) d x$
$$
\begin{aligned}
& I=\frac{1}{2} \int_{\log 2}^{\log 3} \frac{\sin (\log 2+\log 3-t)}{\sin (\log 2+\log 3-t)+\sin } d t \\
& I=\frac{1}{2} \int_{\log 2}^{\log 3} \frac{\sin (\log 6-t)}{\sin (\log 6-t)+\sin (t)} d t \\
& \therefore I=\int_{\log 2}^{\log 3} \frac{\sin (\log 6-t)}{\sin (\log 6-t)+\sin t} d t \quad \ldots(\mathrm{li})
\end{aligned}
$$
On adding Eqs. (i) and (ii), we get
$$
2 I=\frac{1}{2} \int_{\log 2}^{\log 3} \frac{\sin t+\sin (\log 6-t)}{\sin (\log 6-t)+\sin t} d t
$$
$$
\begin{gathered}
\therefore \quad 2 I=\frac{1}{2}(t)_{\log 2}^{\log 3}=\frac{1}{2}(\log 3-\log 2) \\
\Rightarrow I=\frac{1}{4} \log \left(\frac{3}{2}\right)
\end{gathered}
$$

</details>

---

### Q21. JEE Advanced 2009 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

If $I_n=\int_{-\pi}^\pi \frac{\sin n x}{\left(1+\pi^x\right) \sin x} d x ; n=0,1,2$, $\ldots$, then

**Options:**

- **(A)** $I_n=I_{n+2}$
- **(B)** $\sum_{m=1}^{10} I_{2 m+1}=10 \pi$
- **(C)** $\sum_{m=1}^{10} I_{2 m}=0$
- **(D)** $I_n=I_{n+1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sum_{m=1}^{10} I_{2 m}=0$**

**Detailed Solution:**

(a)
$$
\begin{aligned}
& I_n=\int_{-\pi}^\pi \frac{\sin n x}{\left(1+\pi^x\right) \sin x} d x \\
& I_n=\int_{-\pi}^\pi \frac{\pi^x \sin n x}{\left(1+\pi^x\right) \sin x} d x \\
& {\left[\because \int_a^b f(x) d x=\int_a^b f(a+b-x) d x\right]} \\
& 2 I_n=\int_{-\pi}^\pi \frac{\sin n x}{\sin x} d x
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow \quad 2 I_n=2 \int_0^\pi \frac{\sin n x}{\sin x} d x \\
& \Rightarrow \quad I_n=\int_0^\pi \frac{\sin n x}{\sin x} d x \\
& \text { Now, } \quad I_{n+2}-I_n \\
& =\int_0^\pi \frac{\sin (n+2) x-\sin n x}{\sin x} d x \\
& =\int_0^\pi \frac{2 \cos (n+1) x \sin x}{\sin x} d x \\
& =2\left[\frac{\sin (n+1) x}{(n+1)}\right]_0^\pi=0 \\
& \Rightarrow \quad I_{n+2}=I_n \\
& \text { (b) As } I_3=I_5=\ldots=I_{21} \\
& \therefore \sum_{m=1}^{10} I_{2 m+1}=10 I_3=10 \int_0^\pi \frac{\sin 3 x}{\sin x} d x \\
& =10 \int_0^\pi\left(3-4 \sin ^2 x\right) d x \\
& =10[3 x-2 x+\sin 2 x]_0^\pi=10 \pi \\
& \text { (c) As } \quad I_2=I_4=\ldots=I_{20} \\
& \therefore \quad \sum_{m=1}^{10} I_{2 m}=10 \int_0^\pi \frac{\sin 2 x}{\sin x} d x \\
& =20[\sin x]_0^\pi=0 \\
&
\end{aligned}
$$

</details>

---

### Q22. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `3`

Match the following.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/UyPhBV62yJ87NM_xRqutVqISAPvRym6ILTSeV_4cma8.original.fullsize.png">

**Options:**

- **(A)** (i) (a), (ii) (b), (iii) (d), (iv) (c)
- **(B)** (i) (c), (ii) (a), (iii) (b), (iv) (d)
- **(C)** (i) (a), (ii) (d), (iii) (b), (iv) (c)
- **(D)** (i) (b), (ii) (a), (iii) (c), (iv) (d)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) (i) (a), (ii) (d), (iii) (b), (iv) (c)**

**Detailed Solution:**

(i) $I=\int_0^{\pi / 2}(\sin x)^{\cos x}\left(\cos x \cot x-\log (\sin x)^{\sin x}\right) d x=\int_0^{\pi / 2} \frac{d}{d x}(\sin x)^{\cos x} d x=1$
(ii) The point of intersection of $-4 y^2=x$ and $x-1=-5 y^2$ is $(-4,-1)$ and $(-4,1)$.
Hence, required area $=2\left\{\int_0^1\left(1-5 y^2\right) d y-\int_0^1-4 y^2 d y\right\}=\frac{4}{3}$.
(iii) The point intersection of $y=3^{x-1} \log x$ and $y=x^x-1$ is $(1,0)$.
Hence, $\quad \frac{d y}{d x}=\frac{3^{x-1}}{x}+3^{x-1} \cdot \log 3 \cdot \log x$
$\therefore \quad\left(\frac{d y}{d x}\right)_{(1,0)}=1$
For
$$
\therefore \quad\left(\frac{d y}{d x}\right)_{(1,0)}=1
$$

If $\theta$ is angle between the curves, then $\tan \theta=0$.
$$
\because \quad \theta=0^{\circ}
$$
(iv)
$$
\begin{aligned}
& \frac{d y}{d x}=\frac{2}{x+y} \Rightarrow \frac{d x}{d y}-\frac{x}{2}=\frac{y}{2} \\
& \Rightarrow \quad x e^{-y / 2}=\frac{1}{2} \cdot \int y \cdot e^{-y / 2} d y \\
& \Rightarrow \quad x+y+2=k e^{y / 2} \\
& \Rightarrow \quad k=3 \\
& \therefore \quad x+y+2=3 e^{y / 2} \\
&
\end{aligned}
$$
[passing through $(1,0)$ ]

</details>

---

