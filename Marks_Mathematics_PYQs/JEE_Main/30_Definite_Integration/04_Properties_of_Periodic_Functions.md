# JEE Main Mathematics - Definite Integration

## Topic 4: Properties of Periodic Functions

**Total Questions:** 8

---

### Q1. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_0^{20\pi} (\sin^4 x + \cos^4 x) \, dx$ is equal to:

**Options:**

- **(A)** $\dfrac{15\pi}{2}$
- **(B)** $25\pi$
- **(C)** $15\pi$
- **(D)** $\dfrac{25\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $15\pi$**

**Detailed Solution:**

Let $I = \int_0^{20\pi} (\sin^4 x + \cos^4 x) \, dx$

Using the algebraic identity $a^2 + b^2 = (a+b)^2 - 2ab$, the integrand can be simplified:

$\sin^4 x + \cos^4 x = (\sin^2 x + \cos^2 x)^2 - 2\sin^2 x \cos^2 x$

Since $\sin^2 x + \cos^2 x = 1$ and $2\sin x \cos x = \sin 2x$:

$\sin^4 x + \cos^4 x = 1 - \dfrac{1}{2} (2\sin x \cos x)^2 = 1 - \dfrac{1}{2} \sin^2 2x$

Using the half-angle formula $\sin^2 \theta = \dfrac{1 - \cos 2\theta}{2}$:

$\sin^4 x + \cos^4 x = 1 - \dfrac{1}{2} \left( \dfrac{1 - \cos 4x}{2} \right) = 1 - \dfrac{1}{4} + \dfrac{1}{4} \cos 4x = \dfrac{3}{4} + \dfrac{1}{4} \cos 4x$

Substituting this back into the integral:

$I = \int_0^{20\pi} \left( \dfrac{3}{4} + \dfrac{1}{4} \cos 4x \right) \, dx$

$I = \left[ \dfrac{3}{4} x + \dfrac{1}{16} \sin 4x \right]_0^{20\pi}$

Evaluating the limits:

$I = \left( \dfrac{3}{4} (20\pi) + \dfrac{1}{16} \sin(80\pi) \right) - (0 + 0)$

Since $\sin(80\pi) = 0$:

$I = 15\pi$

Answer: $15\pi$

</details>

---

### Q2. JEE Main 2022 (26 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>20</mn><mi>&#960;</mi></mrow></msubsup><msup><mfenced><mrow><mfenced open="|" close="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced open="|" close="|"><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mi>d</mi><mi>x</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mn>4</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>20</mn><mi>&#960;</mi></mrow></msubsup><msup><mfenced><mrow><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mi>d</mi><mi>x</mi></math></p><p>We know that the period of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>40</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>40</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>40</mn><msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mn>0</mn><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msubsup><mo>=</mo><mn>40</mn><mfenced><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>cos&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mi>cos</mi><mn>0</mn></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>20</mn><mfenced close="]" open="["><mrow><mi>&#960;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p></blockquote>

</details>

---

### Q3. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>t</mi></mfenced></math> denote the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>. Then the value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>3</mn></mrow><mn>101</mn></msubsup><mfenced><mrow><mfenced open="[" close="]"><mrow><mi>sin</mi><mfenced><mrow><mi>&#960;</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><msup><mi>e</mi><mfenced open="[" close="]"><mrow><mi>cos</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mi>x</mi></mrow></mfenced></mrow></mfenced></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>52</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow></mfenced></mrow><mi>e</mi></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>52</mn><mi>e</mi></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>52</mn><mfenced><mrow><mn>2</mn><mo>+</mo><mi>e</mi></mrow></mfenced></mrow><mi>e</mi></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>104</mn><mi>e</mi></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>52</mn><mi>e</mi></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>3</mn></mrow><mn>101</mn></msubsup><mfenced><mrow><mfenced close="]" open="["><mrow><mi>sin</mi><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>e</mi><mfenced close="]" open="["><mrow><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></mrow></mfenced></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>3</mn></mrow><mn>101</mn></msubsup><mfenced close="]" open="["><mrow><mi>sin</mi><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>3</mn></mrow><mn>101</mn></msubsup><msup><mi>e</mi><mfenced close="]" open="["><mrow><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></mrow></mfenced></msup><mi>d</mi><mi>x</mi></math></p><p>Now checking periodicity of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>sin</mi><mi>&#960;</mi><mi>x</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mi>sin</mi><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mi>sin</mi><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>sin</mi><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mo>&#8594;</mo></math> periodic with period 2</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mn>52</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced close="]" open="["><mrow><mi>sin</mi><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>52</mn><mfenced close="]" open="["><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mn>0</mn><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mo>-</mo><mn>1</mn><mi>d</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>52</mn></math></p><p>Now checking periodicity of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></mrow></mfenced></math> has periodicity of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>104</mn><mfenced><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msubsup><msup><mi>e</mi><mn>0</mn></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfrac><mn>3</mn><mn>4</mn></mfrac></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mn>1</mn></msubsup><msup><mi>e</mi><mn>0</mn></msup><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>104</mn><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>e</mi></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>52</mn><mo>+</mo><mfrac><mn>52</mn><mi>e</mi></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>52</mn><mi>e</mi></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>3</mn></mrow><mn>101</mn></msubsup><mfenced><mrow><mfenced close="]" open="["><mrow><mi>sin</mi><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>e</mi><mfenced close="]" open="["><mrow><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></mrow></mfenced></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>52</mn><mi>e</mi></mfrac></math></p></blockquote>

</details>

---

### Q4. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>For any real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denote the largest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> be a real-valued function defined on the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>-</mo><mn>10</mn><mo>,</mo><mn>10</mn></mrow></mfenced></math> by  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>,</mo></mtd><mtd><mtext>if</mtext><mo>&#160;</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>&#160;</mo><mtext>is&#160;odd</mtext></mtd></mtr><mtr><mtd><mn>1</mn><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mtext>if</mtext><mo>&#160;</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>&#160;</mo><mtext>is&#160;even</mtext></mtd></mtr></mtable></mfenced></math></p><p>Then, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mn>10</mn></mfrac><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>10</mn></mrow><mn>10</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mi>cos&#960;</mi><mi>x</mi><mi>d</mi><mi>x</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mrow><mtable columnalign="left"><mtr><mtd><mi>x</mi><mo>-</mo><mn>1</mn><mo>,</mo></mtd></mtr><mtr><mtd><mn>1</mn><mo>-</mo><mi>x</mi><mo>,</mo></mtd></mtr></mtable><mtable columnalign="left"><mtr><mtd><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math></p><p><img height="121" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e9e0342f-0edd-4275-89a3-56619fe12899-image.png" width="333" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is periodic with period <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, and is even.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>10</mn></mrow><mn>10</mn></msubsup><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mi>cos&#960;</mi><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>10</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mi>cos&#960;</mi><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>5</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mi>cos&#960;</mi><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mo>&#160;</mo><mfenced close="]" open="["><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mi>cos&#960;</mi><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mi>cos&#960;</mi><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>10</mn><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mi>cos&#960;</mi><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>t</mi><mi>cos&#960;</mi><mi>t</mi><mi>d</mi><mi>t</mi><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mi>cos&#960;</mi><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>x</mi><mi>cos</mi><mfenced><mrow><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>I</mi><mo>=</mo><mn>10</mn><mfenced close="]" open="["><mrow><mo>-</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>x</mi><mi>cos&#960;</mi><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>20</mn><msubsup><mfenced close="]" open="["><mrow><mi>x</mi><mfrac><mrow><mi>sin&#960;</mi><mi>x</mi></mrow><mi mathvariant="normal">&#960;</mi></mfrac><mo>+</mo><mfrac><mrow><mi>cos&#960;</mi><mi>x</mi></mrow><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>20</mn><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>40</mn><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mn>10</mn></mfrac><mi>I</mi><mo>=</mo><mn>4</mn></math></p></blockquote>

</details>

---

### Q5. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="bold-italic">R</mi><mo>&#8594;</mo><mi mathvariant="bold-italic">R</mi></math> be continuous function satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mi>n</mi></math>, for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="bold-italic">R</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is a positive integer. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>4</mn><mi>n</mi><mi>k</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>k</mi></mrow><mrow><mn>3</mn><mi>k</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>4</mn><mi>n</mi><mi>k</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mi>n</mi><mi>k</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><mi>n</mi><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>4</mn><msup><mi>n</mi><mn>2</mn></msup><mo>&#160;</mo><mi>K</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><mi>n</mi><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>6</mn><msup><mi>n</mi><mn>2</mn></msup><mi>k</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><mi>n</mi><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>4</mn><msup><mi>n</mi><mn>2</mn></msup><mo>&#160;</mo><mi>K</mi></math>**

**Detailed Solution:**

<p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mi>n</mi></math> ....(i)</p><p>Replacing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mi>x</mi><mo>+</mo><mi>k</mi></math> in above equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>k</mi></mrow></mfenced><mo>=</mo><mi>n</mi></math> .....(ii)</p><p>Subtraction equation (i) from equation (ii) we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>k</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is periodic with period <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>k</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>4</mn><mi>n</mi><mi>k</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>n</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>k</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mi>k</mi></mrow><mrow><mn>3</mn><mi>k</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>k</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p>Now integrating both side of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mi>n</mi></math> with limit <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>k</mi></msubsup></math>  we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>k</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>k</mi></msubsup><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>n</mi><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>k</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mi>k</mi><mrow><mn>2</mn><mi>k</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>n</mi><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>2</mn><mi>k</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>n</mi><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mi>k</mi><mo>,</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mi>n</mi><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><mi>n</mi><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>4</mn><msup><mi>n</mi><mn>2</mn></msup><mi>k</mi></math></p>

</details>

---

### Q6. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>100</mn><mi>&#960;</mi></mrow></msubsup><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mi>e</mi><mfenced><mrow><mstyle displaystyle="true"><mfrac><mi>x</mi><mi mathvariant="normal">&#960;</mi></mfrac><mo>-</mo></mstyle><mfenced open="[" close="]"><mstyle displaystyle="true"><mfrac><mi>x</mi><mi mathvariant="normal">&#960;</mi></mfrac></mstyle></mfenced></mrow></mfenced></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>&#945;</mi><msup><mi>&#960;</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfrac><mo>,</mo><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>x</mi></mfenced></math> is the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>100</mn><mi>&#960;</mi></mrow></msubsup><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mi>e</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>x</mi><mi>&#960;</mi></mfrac><mo>-</mo><mfenced close="]" open="["><mfrac><mi>x</mi><mi>&#960;</mi></mfrac></mfenced></mstyle></mfenced></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p>We know that if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is a periodic function, with period <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>n</mi><mi>T</mi></mrow></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>n</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>T</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>Z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>100</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mi>e</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>x</mi><mi>&#960;</mi></mfrac><mo>-</mo><mfenced close="]" open="["><mfrac><mi>x</mi><mi>&#960;</mi></mfrac></mfenced></mstyle></mfenced></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p>For, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mi>&#960;</mi><mo>,</mo><mn>0</mn><mo>&#60;</mo><mfrac><mi>x</mi><mi>&#960;</mi></mfrac><mo>&#60;</mo><mn>1</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mfrac><mi>x</mi><mi>&#960;</mi></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>100</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mi>e</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>x</mi><mi>&#960;</mi></mfrac></mstyle></mfenced></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>100</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mn>2</mn></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>100</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mo>&#183;</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>50</mn><mfenced close="}" open="{"><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mo>&#183;</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mi>&#960;</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup></mrow></mfenced><mn>0</mn><mi>&#960;</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mi>&#960;</mi><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mi mathvariant="normal">&#960;</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mn>0</mn></msup></mrow></mfenced><mo>=</mo><mi>&#960;</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p>And, let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mo>&#183;</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p>By using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>L</mi><mi>A</mi><mi>T</mi><mi>E</mi></math> rule,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mi>cos</mi><mn>2</mn><mi>x</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p>Now, using integration by parts, i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfenced><mrow><mi>u</mi><mo>&#183;</mo><mi>v</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>u</mi><mo>&#8747;</mo><mi>v</mi><mi>d</mi><mi>x</mi><mo>-</mo><mo>&#8747;</mo><mfenced close="]" open="["><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mi>u</mi></mfenced><mo>&#8747;</mo><mi>v</mi><mi>d</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mi>&#960;</mi><msubsup><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mo>&#183;</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mn>0</mn><mi>&#960;</mi></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi mathvariant="normal">&#960;</mi></msubsup><mfenced><mrow><mo>-</mo><mi>&#960;</mi><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mo>&#183;</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mi>&#960;</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mo>-</mo><mn>2</mn><mi>&#960;</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mi>sin</mi><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p>Again, applying integration by parts, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open=""><mrow><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mi>&#960;</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mo>-</mo><mn>2</mn><mi>&#960;</mi><mo>{</mo><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mi>&#960;</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mn>0</mn><mi>&#960;</mi></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#960;</mi></msubsup><mo>-</mo><mi>&#960;</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi><mo>/</mo><mi>&#960;</mi></mrow></msup><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mi>&#960;</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mo>-</mo><mn>4</mn><msup><mi>&#960;</mi><mn>2</mn></msup><msub><mi>I</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mi>&#960;</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mn>50</mn><mfenced><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mn>50</mn><mfenced close="}" open="{"><mrow><mi>&#960;</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mo>-</mo><mfrac><mrow><mi>&#960;</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mrow><mn>200</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><msup><mi>&#960;</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><mi>&#945;</mi><msup><mi>&#960;</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>&#945;</mi><msup><mi>&#960;</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>200</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><msup><mi>&#960;</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>&#960;</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>200</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q7. JEE Main 2021 (16 Mar Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a continuous function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>8</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>I</mi><mn>2</mn></msub></math> is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p>Replace <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mtext>by</mtext><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p>By subtracting the equations, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is periodic with period <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>8</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>4</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>8</mn></math></p><p>Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>4</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>16</mn></math></p>

</details>

---

### Q8. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<div>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><msubsup><mo>&#8747;</mo><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></msup><mi>d</mi><mi>x</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> is the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi><mo>,</mo></math> is:</div>

**Options:**

- **(A)** <div><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></div>
- **(B)** <div><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mi>e</mi></math></div>
- **(C)** <div><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow></mfenced></math></div>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mi>e</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <div><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></div>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><msubsup><mo>&#8747;</mo><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msup><mi>e</mi><mfenced close="}" open="{"><mi>x</mi></mfenced></msup><mi>d</mi><mi>x</mi><mo>,</mo></math> period of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>e</mi><mfenced close="}" open="{"><mi>x</mi></mfenced></msup><mi>d</mi><mi>x</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>100</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

