# JEE Main Mathematics - Inverse Trigonometric Functions

## Topic 3: Converting one Inverse T function to other Inverse T

**Total Questions:** 11

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin(\tan^{-1}(x\sqrt{2})) = \cot(\sin^{-1}\sqrt{1-x^2})$, $x \in (0,1)$, then the value of $x$ is :

**Options:**

- **(A)** $\dfrac{1}{2}$
- **(B)** $\dfrac{1}{3}$
- **(C)** $\dfrac{2}{3}$
- **(D)** $\dfrac{5}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{2}$**

**Detailed Solution:**

Let $\alpha = \tan^{-1}(x\sqrt{2}) \Rightarrow \tan\alpha = x\sqrt{2}$

From the right-angled triangle, $\sin\alpha = \dfrac{x\sqrt{2}}{\sqrt{1+2x^2}}$

Let $\beta = \sin^{-1}\sqrt{1-x^2} \Rightarrow \sin\beta = \sqrt{1-x^2}$

From the right-angled triangle, $\cos\beta = \sqrt{1 - (1-x^2)} = x$

$\cot\beta = \dfrac{\cos\beta}{\sin\beta} = \dfrac{x}{\sqrt{1-x^2}}$

Given $\sin\alpha = \cot\beta$, substituting the values:

$\dfrac{x\sqrt{2}}{\sqrt{1+2x^2}} = \dfrac{x}{\sqrt{1-x^2}}$

Since $x \in (0,1)$, $x \neq 0$. Dividing by $x$ and squaring both sides:

$\dfrac{2}{1+2x^2} = \dfrac{1}{1-x^2}$

$2(1-x^2) = 1+2x^2$

$2 - 2x^2 = 1 + 2x^2$

$4x^2 = 1$

$x^2 = \dfrac{1}{4}$

Since $x \in (0,1)$, $x = \dfrac{1}{2}$

Answer: $\dfrac{1}{2}$

</details>

---

### Q2. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\cot ^{-1}\left(\frac{\sqrt{1+\tan ^2(2)}-1}{\tan (2)}\right)-\cot ^{-1}$
$\left(\frac{\sqrt{1+\tan ^2\left(\frac{1}{2}\right)}+1}{\tan \left(\frac{1}{2}\right)}\right) \text { is equal to }$

**Options:**

- **(A)** $\pi-\frac{5}{4}$
- **(B)** $\pi-\frac{3}{2}$
- **(C)** $\pi+\frac{3}{2}$
- **(D)** $\pi+\frac{5}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\pi-\frac{5}{4}$**

**Detailed Solution:**

$\cot ^{-1}\left(\frac{|\sec 2|-1}{\tan 2}\right)-\cot ^{-1}\left(\frac{\left|\sec \frac{1}{2}\right|+1}{\tan \frac{1}{2}}\right)$
$\begin{aligned} & =\cot ^{-1}\left(\frac{-1-\cos 2}{\sin 2}\right)-\cot ^{-1}\left(\frac{1+\cos \frac{1}{2}}{\sin \frac{1}{2}}\right) \\ & =\pi-\cot ^{-1}(\cot 1)-\cot ^{-1}\left(\cot \frac{1}{4}\right) \\ & =\pi-1-\frac{1}{4}=\pi-\frac{5}{4}\end{aligned}$

</details>

---

### Q3. JEE Main 2024 (09 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

Let the inverse trigonometric functions take principal values. The number of real solutions of the equation $2 \sin ^{-1} x+3 \cos ^{-1} x=\frac{2 \pi}{5}$, is _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

$\begin{aligned}
& 2 \sin ^{-1} x+3 \cos ^{-1} x=\frac{2 \pi}{5} \\
& \Rightarrow \quad \pi+\cos ^{-1} x=\frac{2 \pi}{5} \\
& \Rightarrow \quad \cos ^{-1} x=\frac{-3 \pi}{5}
\end{aligned}$
Not possible
Ans. 0

</details>

---

### Q4. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int_{1 / 4}^{3 / 4} \cos \left(2 \cot ^{-1} \sqrt{\frac{1-x}{1+x}}\right) d x$ is equal to

**Options:**

- **(A)** $1 / 2$
- **(B)** $-1 / 2$
- **(C)** $-1 / 4$
- **(D)** $1 / 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-1 / 4$**

**Detailed Solution:**

$\begin{aligned} & I=\int_{1 / 4}^{3 / 4} \cos \left(2 \cot ^{-1}\left(\sqrt{\frac{1-x}{1+x}}\right) d x\right) \\ & \int_{1 / 4}^{3 / 4} \cos \left(2\left(\tan ^{-1} \sqrt{\frac{1+x}{1+x}}\right)\right) d x \\ & \left.\int_{1 / 4}^{3 / 4} \frac{1-\tan ^2\left(\tan ^{-1} \sqrt{\frac{1+x}{1-x}}\right)}{1+\tan ^2\left(\tan ^{-1} \sqrt{\frac{1+x}{1-x}}\right.}\right) d x\end{aligned}$
$\begin{aligned} & =\int_{1 / 4}^{3 / 4} \frac{1-\left(\frac{1+x}{1-x}\right)}{1+\left(\frac{1+x}{1-x}\right)} d x=\int_{1 / 4}^{3 / 4} \frac{-2 x}{2} d x \\ & =\int_{1 / 4}^{3 / 4}(-x) d x=-\left(\frac{x^2}{2}\right)_{1 / 4}^{3 / 4} \\ & =-\frac{1}{2}\left[\frac{9}{16}-\frac{1}{16}\right] \\ & =-\frac{1}{4}\end{aligned}$

</details>

---

### Q5. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>(</mo><mi>S</mi><mo>)</mo></math> denotes the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>(</mo><mi mathvariant="normal">S</mi><mo>)</mo><mo>=</mo><mn>2</mn></math> and only one element in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is less then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>(</mo><mi mathvariant="normal">S</mi><mo>)</mo><mo>=</mo><mn>1</mn></math> and the element in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is more than <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>(</mo><mi mathvariant="normal">S</mi><mo>)</mo><mo>=</mo><mn>1</mn></math> and the element in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is less then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>(</mo><mi mathvariant="normal">S</mi><mo>)</mo><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>(</mo><mi mathvariant="normal">S</mi><mo>)</mo><mo>=</mo><mn>1</mn></math> and the element in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is less then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>tan</mi><mfenced><mi>&#952;</mi></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>;</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>&#952;</mi><mo>&#60;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mo>&#160;</mo><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mo>&#160;</mo><mi>&#952;</mi></mrow></mfrac></mfenced><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>tan</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>&#952;</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi>&#952;</mi><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mi>tan</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>&#8756;</mo><mi mathvariant="normal">x</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn><mo>&#8771;</mo><mn>0</mn><mo>.</mo><mn>414</mn><mo>&#60;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q6. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>3</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfrac></mfenced><mo>+</mo><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mfrac><mrow><mn>8</mn><mo>+</mo><mn>4</mn><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>6</mn><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></msqrt><mo>=</mo></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>3</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfrac></mfenced><mo>+</mo><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mfrac><mrow><mn>8</mn><mo>+</mo><mn>4</mn><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>6</mn><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mrow><msqrt><mn>3</mn></msqrt><mfenced><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></mrow></mfrac></mfenced><mo>+</mo><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mfrac><mrow><mn>4</mn><mfenced><mrow><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></mrow><mrow><mn>3</mn><mfenced><mrow><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></mrow></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>+</mo><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mfrac><mn>4</mn><mn>3</mn></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></math></p>

</details>

---

### Q7. JEE Main 2022 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>, let the solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mi>cot</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>k</mi><mo>,</mo><mn>0</mn><mo>&#60;</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>&#60;</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math>, where the inverse trigonometric functions take only principal values. If the solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>b</mi><mi>x</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>0</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>b</mi><msup><mi>k</mi><mn>2</mn></msup></mfrac></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mi>cot</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>k</mi></math></p><p>Now simplifying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mi>cos</mi><mfenced><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mi>cot</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>k</mi></math></p><p>becomes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mi>cot</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>k</mi></math></p><p>And now solving  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cot</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced><mo>=</mo><msup><mi>cotcot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></msqrt></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mi>cot</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>k</mi></math> becomes </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>x</mi><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>k</mi></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>x</mi><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></mfenced></mrow></mfenced><mo>=</mo><mfrac><msqrt><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><msup><mi>k</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p>So, roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><msqrt><mfrac><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfrac></msqrt><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mo>-</mo><msqrt><mfrac><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfrac></msqrt><mo>&#8658;</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>2</mn><mfenced><mfrac><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>So, sum of roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>b</mi><mi>x</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>0</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mn>1</mn><mo>=</mo><mi>b</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Product of roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>b</mi><mi>x</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>0</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><msup><mi>&#945;</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac><mo>=</mo><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>=</mo><mn>5</mn><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mi>Put</mi><mo>&#160;</mo><mi>in</mi><mo>&#160;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mn>1</mn><mo>=</mo><mn>5</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>b</mi><msup><mi>k</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>4</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></mfrac><mo>=</mo><mn>12</mn></math></p></blockquote>

</details>

---

### Q8. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#960;</mi><mo>-</mo><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>4</mn><mn>5</mn></mfrac><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>5</mn><mn>13</mn></mfrac><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>16</mn><mn>65</mn></mfrac></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>4</mn><mn>5</mn></mfrac><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>5</mn><mn>13</mn></mfrac><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>16</mn><mn>65</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>16</mn><mn>63</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>3</mn></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>12</mn></mfrac></mstyle></mrow><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>3</mn></mfrac></mstyle><mo>&#183;</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>12</mn></mfrac></mstyle></mrow></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>16</mn><mn>63</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>63</mn><mn>16</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>16</mn><mn>63</mn></mfrac><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac></math></p>

</details>

---

### Q9. JEE Main 2020 (02 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><mi>k</mi><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="}" open="{"><mrow><mfrac><mn>3</mn><mn>5</mn></mfrac><mi>cos</mi><mi>k</mi><mi>x</mi><mo>-</mo><mfrac><mn>4</mn><mn>5</mn></mfrac><mi>sin</mi><mi>k</mi><mi>x</mi></mrow></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **91**

**Detailed Solution:**

<p>For, small values near <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>, i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>&#60;</mo><mo>&#60;</mo><mo>.</mo><mo>.</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><mi>k</mi><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mi>k</mi><mi>x</mi><mo>&#183;</mo><mi>cos</mi><mi>&#945;</mi><mo>-</mo><mi>sin</mi><mi>k</mi><mi>x</mi><mo>&#183;</mo><mi>sin</mi><mi>&#945;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><mi>k</mi><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mfenced><mrow><mi>k</mi><mi>x</mi><mo>+</mo><mi>&#945;</mi></mrow></mfenced></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><mi>k</mi><mfenced><mrow><mi>k</mi><mi>x</mi><mo>+</mo><mi>&#945;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><mfenced><mrow><msup><mi mathvariant="normal">k</mi><mn>2</mn></msup><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">k</mi><mi>&#945;</mi></mrow></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>6</mn><mfenced><mn>7</mn></mfenced><mfenced><mn>13</mn></mfenced></mrow><mn>6</mn></mfrac><mo>=</mo><mn>91</mn></math> </p>

</details>

---

### Q10. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Statement I: The equation $\left(\sin ^{-1} \mathrm{x}\right)^3+$ $\left(\cos ^{-1} \mathrm{x}\right)^3-\mathrm{a} \pi^3=0$ has a solution for all $\mathrm{a} \geq \frac{1}{32}$.
Statement II: For any $\mathrm{x} \in \mathrm{R}$,
$\sin ^{-1} x+\cos ^{-1} x=\frac{\pi}{2}$ and $0 \leq\left(\sin ^{-1} x-\frac{\pi}{4}\right)^2 \leq \frac{9 \pi^2}{16}$

**Options:**

- **(A)** Both statements I and II are true.
- **(B)** Both statements I and II are false.
- **(C)** Statement $\mathrm{I}$ is true and statement $\mathrm{II}$ is false.
- **(D)** Statement $\mathrm{I}$ is false and statement II is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Both statements I and II are true.**

**Detailed Solution:**

$$
\begin{aligned}
&\sin ^{-1} x \in\left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \\
&\Rightarrow-\frac{3 \pi}{4} \leq\left(\sin ^{-1} x-\frac{\pi}{4}\right) \leq \frac{\pi}{4} \\
&0 \leq\left(\sin ^{-1} x-\frac{\pi}{4}\right)^2 \leq \frac{9}{16} \pi^2
\end{aligned}
$$
Statement II is true
$$
\begin{aligned}
&\left(\sin ^{-1} x\right)^3+\left(\cos ^{-1} x\right)^3=a \pi^3 \\
\Rightarrow &\left(\sin ^{-1} x+\cos ^{-1} x\right)\left[\left(\sin ^{-1} x+\cos ^{-1} x\right)^2-\right.\\
&\left.3 \sin ^{-1} x \cos ^{-1} x\right]=a \pi^3 \\
\Rightarrow & \frac{\pi^2}{4}-3 \sin ^{-1} x \cos ^{-1} x=2 a \pi^2 \\
\Rightarrow & \sin ^{-1} x\left(\frac{\pi}{2}-\sin ^{-1} x\right)=\frac{\pi^2}{12}(1-8 a) \\
\Rightarrow &\left(\sin ^{-1} x-\frac{\pi}{4}\right)^2=\frac{\pi^2}{12}(8 a-1)+\frac{\pi^2}{16} \\
\Rightarrow &\left(\sin ^{-1} x-\frac{\pi}{4}\right)^2=\frac{\pi^2}{48}(32 a-1)
\end{aligned}
$$
Putting this value in equation (1)
$$
0 \leq \frac{\pi^2}{48}(32 a-1) \leq \frac{9}{16} \pi^2
$$

$$
\begin{aligned}
&\Rightarrow 0 \leq 32 a-1 \leq 27 \\
&\frac{1}{32} \leq a \leq \frac{7}{8}
\end{aligned}
$$
Statement-I is also true.

</details>

---

### Q11. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

The trigonometric equation $\sin ^{-1} x=2 \sin ^{-1}$ a has a solution for

**Options:**

- **(A)** $|\mathrm{a}| \geq \frac{1}{\sqrt{2}}$
- **(B)** $\frac{1}{2} < |\mathrm{a}| < \frac{1}{\sqrt{2}}$
- **(C)** all real values of a
- **(D)** $|a| < \frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) all real values of a**

**Detailed Solution:**

$\sin ^{-1} x=2 \sin ^{-1} a$
$-\frac{\pi}{2} \leq \sin ^{-1} \mathrm{x} \leq \frac{\pi}{2} ; \therefore-\frac{\pi}{2} \leq 2 \sin ^{-1} \mathrm{a} \leq \frac{\pi}{2} \quad-\frac{\pi}{4} \leq \sin ^{-1} \mathrm{a} \leq \frac{\pi}{4}$ or $\frac{-1}{\sqrt{2}} \leq \mathrm{a} \leq \frac{1}{\sqrt{2}}$
$\therefore|\mathrm{a}| \leq \frac{1}{\sqrt{2}}\left(\right.$ As $\frac{1}{\sqrt{2}}>\frac{1}{2}$ ). Out of given four option no one is absolutely correct but (c) could be taken into consideration. $\rightarrow|\mathrm{a}| \leq \frac{1}{\sqrt{2}}$ is correct, if $\mathrm{a} < \frac{1}{\sqrt{2}}$ is taken as correct then it domain satisfy for $\mathrm{a}=\frac{1}{\sqrt{3}}$ but equation is satisfied. $\frac{1}{\sqrt{2}}>\frac{1}{\sqrt{3}}>\frac{1}{2}$

</details>

---

