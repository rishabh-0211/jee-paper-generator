# BITSAT Mathematics - Area Under Curves

## Topic 3: Area bounded by Miscellaneous Curves

**Total Questions:** 9

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `2`

If $a, c, b$ are in GP, then the area of the triangle formed by the lines $a x+b y+c=0$ with the coordinates axes is equal to

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** $\frac{1}{2}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

Given $a, c, b$ are in GP
$\Rightarrow \quad c^2=a b$...(i)
According to question,
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/IGkrU0wr51ePLRxTWR_E5mha2CU4XxNUbUIUo1KLP64.original.fullsize.png"/>
$\begin{aligned}
\therefore \text { Area of } \triangle O A B & =\left|\frac{1}{2} \times O A \times O B\right| \\
= & \left|\frac{1}{2} \times\left(\frac{-c}{b}\right) \times\left(\frac{-c}{a}\right)\right| \\
& =\frac{1}{2} \times \frac{c^2}{a b}=\frac{1}{2} [by Eq. (i)]
\end{aligned}$

</details>

---

### Q2. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `3`

The line $y=m x$ bisects the area unclosed by lines $x=0, y=0$ and $x=\frac{3}{2}$ and the curve $y=1+4 x-x^2$. Then, the value of $m$ is

**Options:**

- **(A)** $\frac{13}{6}$
- **(B)** $\frac{13}{2}$
- **(C)** $\frac{13}{5}$
- **(D)** $\frac{13}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{13}{6}$**

**Detailed Solution:**

Given, $y=1+4 x-x^2$
$\begin{aligned}
& \Rightarrow \quad \frac{d y}{d x}=4-2 x=0 \Rightarrow x=2 \text{[point of maxima]}\\
& \Rightarrow \quad y_{\max }=1+4 \times 2-4=5
\end{aligned}$
 when, $x=0, y=1$
$\therefore$ Graph according to question and above information
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/QwdnEHXNpPCFPWMPaOVaSmqS7VsEqWQT6S-P2fi4noU.original.fullsize.png"/>
$\begin{aligned} & \Rightarrow \text { If } y=m x \text { bisects the area bounded } \\ & \Rightarrow \quad A_1=A_2 \\ & \Rightarrow \quad \int_0^{3 / 2}\left(1+4 x-x^2\right) d x=2 \int_0^{3 / 2} m x d x \\ & \Rightarrow \quad\left[x+2 x^2-\frac{x^3}{3}\right]_0^{3 / 2}=\left[m x^2\right]_0^{3 / 2} \\ & \Rightarrow \frac{3}{2}+2 \times \frac{9}{4}-\frac{27}{8} \times \frac{1}{3}=m \times \frac{9}{4} \\ & \therefore \quad m=\frac{13}{6}\end{aligned}$

</details>

---

### Q3. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `2`

The area enclosed by the curves $y=\sin x+\cos x$ and $y=|\cos x-\sin x|$ over the interval $\left[0, \frac{\pi}{2}\right]$ is

**Options:**

- **(A)** $4(\sqrt{2}-1)$
- **(B)** $2 \sqrt{2}(\sqrt{2}-1)$
- **(C)** $2(\sqrt{2}+1)$
- **(D)** $2 \sqrt{2}(\sqrt{2}+1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \sqrt{2}(\sqrt{2}-1)$**

**Detailed Solution:**

Given, $y=\sin x+\cos x, x \in[0, \pi / 2]$
$\frac{d y}{d x}=\cos x-\sin x$
$\begin{aligned} y & =|\cos x-\sin x| \\ & =\left[\begin{array}{cc}\cos x-\sin x & x \in[0, \pi / 4] \\ \sin x-\cos x & x \in[\pi / 4, \pi / 2]\end{array}\right]\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/Bqoq95Rpm-j5ycIe8E3qOccP5zZI1leuKUG20Kyp-38.original.fullsize.png">

$\therefore$ Required area
$\begin{aligned}
&=\int_0^{\pi / 4}|(\sin x+\cos x)-(\cos x-\sin x)| d x+\int_{\pi / 4}^{\pi / 2}|2 \cos x| d x
\end{aligned}$
$=\int_0^{\pi / 4}|2 \sin x| d x+\int_{\pi / 4}^{\pi / 2}|2 \cos x| d x$
$=2(-\cos x)_0^{\pi / 4}+2(\sin x)_{\pi / 4}^{\pi / 2}$
$=2\left[-\frac{1}{\sqrt{2}}+1+1-\frac{1}{\sqrt{2}}\right]$<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/h0i2UrjkiqoD78hh_1S802WjWVfCXjP7KBP5OpVWwrA.original.fullsize.png">

$\begin{aligned}= & 2\left(2-\frac{2}{\sqrt{2}}\right) \\ = & 2(2-\sqrt{2}) \\ = & 4-2 \sqrt{2} \\ = & 2 \sqrt{2}(\sqrt{2}-1)\end{aligned}$

</details>

---

### Q4. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `1`

The area of the region bounded by the parabola $(y-2)^2=(x-1)$, the tangent to the parabola at the point $(2,3)$ and the $X$-axis is

**Options:**

- **(A)** 3
- **(B)** 6
- **(C)** 9
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 9**

**Detailed Solution:**

The equation of the parabola is $y^2-4 y-x+5=0$ The equation of tangent at $(2,3)$ is
$$
\begin{aligned}
3 y-2(y+3)-\frac{x+2}{2}+5 & =0 \\
2 y-x-4 & =0
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/9b_OFOiPC-yESmoX1Lqx_VI1P1QvG9cP_LVngQLK6ac.original.fullsize.png">

$\therefore$ Required area $A$ is given by
$$
\begin{aligned}
& A=\int_0^3\left(x_2-x_1\right) d y \\
& \Rightarrow \quad A=\int_0^3\left[\left\{(y-2)^2+1\right\}-\{2 y-4\}\right] d y \\
& \Rightarrow \quad A=\int_0^3\left(y^2-6 y+9\right) d y=\int_0^3(3-y)^2 d y \\
& =-\left[\frac{(3-y)^3}{3}\right]_0^3=9 \\
&
\end{aligned}
$$

</details>

---

### Q5. BITSAT 2019

*Type:* `singleCorrect` | *Level:* `2`

Area bounded by two branches of the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>4</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>&#160;</mo><mi>unit</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>&#160;</mo><mi>unit</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>&#160;</mo><mi>unit</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>&#160;</mo><mi>unit</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>&#160;</mo><mi>unit</mi></math>**

**Detailed Solution:**

<p>Given, curve is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>y</mi><mo>-</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><mi>x</mi><msqrt><mi>x</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>x</mi><mo>&#177;</mo><mi>x</mi><msqrt><mi>x</mi></msqrt></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/90b534b6-e3c4-4b5a-bf86-c78cbdd9038c-d43.png" style="width: 301px; height: 300px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Area bounded <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mi>x</mi><msqrt><mi>x</mi></msqrt></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>x</mi><msqrt><mi>x</mi></msqrt></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mi>d</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi>sq</mi><mo>&#160;</mo><mi>unit</mi></math></p>

</details>

---

### Q6. BITSAT 2019

*Type:* `singleCorrect` | *Level:* `2`

The point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>[</mo><mi>P</mi><mo>+</mo><mn>1</mn><mo>]</mo><mo>,</mo><mo>[</mo><mi>P</mi><mo>]</mo><mo>)</mo></math> (where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> is the greatest integer function) lying inside the region bounded by the circle <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>15</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>)</mo><mo>-</mo><mo>{</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>}</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>]</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) None of these**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>P</mi><mo>+</mo><mn>1</mn><mo>]</mo><mo>=</mo><mo>[</mo><mi>P</mi><mo>]</mo><mo>+</mo><mn>1</mn></math>, Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>P</mi><mo>]</mo><mo>=</mo><mi>n</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is integer</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>(</mo><mo>[</mo><mi>P</mi><mo>+</mo><mn>1</mn><mo>]</mo><mo>,</mo><mo>[</mo><mi>P</mi><mo>]</mo><mo>)</mo><mo>=</mo><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi>n</mi><mo>)</mo></math> lie inside the region of circles</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>15</mn><mo>=</mo><mn>0</mn><mo>,</mo><msub><mi>C</mi><mn>1</mn></msub><mo>=</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn><mo>,</mo><msub><mi>C</mi><mn>2</mn></msub><mo>=</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p><p>Both circles are concentric. </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>-</mo><mn>7</mn><mo>&#62;</mo><mn>0</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>-</mo><mn>15</mn><mo>&#60;</mo><mn>0</mn><mo>&#8658;</mo><mn>4</mn><mo>&#60;</mo><msup><mi>n</mi><mn>2</mn></msup><mo>&#60;</mo><mn>8</mn></math></p><p>Which is not possible for any integer.</p>

</details>

---

### Q7. BITSAT 2018

*Type:* `singleCorrect` | *Level:* `3`

The area of the region included between the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfenced open="|" close="|"><mi>x</mi></mfenced></msqrt><mo>+</mo><msqrt><mfenced open="|" close="|"><mi>y</mi></mfenced></msqrt><mo>=</mo><msqrt><mi>a</mi></msqrt><mfenced><mrow><mi>a</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><msup><mi>a</mi><mn>2</mn></msup></math> sq units
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>-</mo><mi>&#960;</mi></mrow></mfenced><msup><mi>a</mi><mn>2</mn></msup></math> sq units
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mi>a</mi><mn>2</mn></msup></math> sq units
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><msup><mi>a</mi><mn>2</mn></msup></math> sq units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><msup><mi>a</mi><mn>2</mn></msup></math> sq units**

**Detailed Solution:**

<p>Given curves are</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfenced close="|" open="|"><mi>x</mi></mfenced></msqrt><mo>+</mo><msqrt><mfenced close="|" open="|"><mi>y</mi></mfenced></msqrt><mo>=</mo><msqrt><mi>a</mi></msqrt><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/92c79c76-2fd3-47b1-8567-d7127f1e10c3-image.png" style="width: 234px; height: 270px;" /></p><p>Now, required areas <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math>[shaded area in the first quadrant]</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mfenced close="]" open="["><mrow><mfrac><mrow><mi>&#960;</mi><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><msup><mfenced><mrow><msqrt><mi>a</mi></msqrt><mo>-</mo><msqrt><mi>x</mi></msqrt></mrow></mfenced><mn>2</mn></msup><mi>d</mi><mi>x</mi></mrow></mfenced></math>  [from Eqs. (i) and (ii)]</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mfenced close="]" open="["><mrow><mfrac><mrow><mi>&#960;</mi><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>x</mi><mo>-</mo><mn>2</mn><msqrt><mi>a</mi></msqrt><msqrt><mi>x</mi></msqrt></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mfrac><mrow><mi>&#960;</mi><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>-</mo><mn>4</mn><msubsup><mfenced close="]" open="["><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msqrt><mi>a</mi></msqrt><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfenced><mn>0</mn><mi>a</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><msup><mi>a</mi><mn>2</mn></msup></math> sq units</p><p>Hence, option (a) is correct.</p>

</details>

---

### Q8. BITSAT 2017

*Type:* `singleCorrect` | *Level:* `2`

The area under the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced open="|" close="|"><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>,</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math> and above <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>-axis, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

<p>Required area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced close="|" open="|"><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></msubsup><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced open="[" close="]"><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></msubsup><mo>+</mo><msubsup><mfenced open="[" close="]"><mrow><mo>-</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></math></p>

</details>

---

### Q9. BITSAT 2016

*Type:* `singleCorrect` | *Level:* `2`

A wire $34 \mathrm{~cm}$ long is to be bent in the form of a quadrilateral of which each angle is $90^{\circ} .$ What is the maximum area which can be enclosed inside the quadrilateral?

**Options:**

- **(A)** $68 \mathrm{~cm}^{2}$
- **(B)** $70 \mathrm{~cm}^{2}$
- **(C)** $71.25 \mathrm{~cm}^{2}$
- **(D)** $72.25 \mathrm{~cm}^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $72.25 \mathrm{~cm}^{2}$**

**Detailed Solution:**

Let one side of quadrilateral be $\mathrm{x}$ and another side be $y$ so, $2(x+y)=34$

or $(x+y)=17$

We know from the basic principle that for a given perimeter square has the maximum area, $\mathrm{so}, \mathrm{x}=\mathrm{y}$ and putting this value in equation (i)

$\mathrm{x}=\mathrm{y}=\frac{17}{2}$

Area $=x \cdot y=\frac{17}{2} \times \frac{17}{2}=\frac{289}{4}=72.25$

</details>

---

