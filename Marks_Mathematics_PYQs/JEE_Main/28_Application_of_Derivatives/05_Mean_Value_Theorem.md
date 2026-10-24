# JEE Main Mathematics - Application of Derivatives

## Topic 5: Mean Value Theorem

**Total Questions:** 16

---

### Q1. JEE Main 2024 (04 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be a thrice differentiable function such that $f(0)=0, f(1)=1, f(2)=-1, f(3)=2$ and $f(4)=-2$. Then, the minimum number of zeros of $\left(3 f^{\prime} f^{\prime \prime}+f f^{\prime \prime \prime}\right)(x)$ is _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$\begin{aligned} & \left(3 f^{\prime} f^{\prime \prime}+f f^{\prime \prime \prime}\right)(x)=\left(\left(f f^{\prime \prime}+\left(f^{\prime}\right)^2\right)(x)\right)^{\prime} \\ & \left(f f f^{\prime \prime}+\left(f^{\prime}\right)^2\right)(x)=\left(\left(f f^{\prime}\right)(x)\right)^{\prime} \\ & \therefore\left(3 f^{\prime} f^{\prime \prime}+f^{\prime \prime \prime}\right)(x)=\left(f(x) \cdot f^{\prime}(x)\right)^{\prime \prime}\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/AHicBd3TPXeiuGz0infm8IHVPfVeCX47_UvUThhm54I.original.fullsize.png">
$\begin{aligned} & \min \text { roots of } \mathrm{f}(\mathrm{x}) \rightarrow 4 \\ & \therefore \min \text {. roots of } \mathrm{f}^{\prime}(\mathrm{x}) \rightarrow 3 \\ & \therefore \min \text { roots of }\left(\mathrm{f}(\mathrm{x}) \cdot \mathrm{f}^{\prime}(\mathrm{x})\right) \rightarrow 7 \\ & \therefore \min \text { roots of }\left(\mathrm{f}(\mathrm{x}) \cdot \mathrm{f}^{\prime}(\mathrm{x})\right)^{\prime \prime} \rightarrow 5\end{aligned}$

</details>

---

### Q2. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>R</mi><mo>→</mo><mi>R</mi></math> be a non constant twice differentiable such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></math>. If a real valued function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>[</mo><mo> </mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mi>g</mi><mo>(</mo><mn>2</mn><mo>-</mo><mi>x</mi><mo>)</mo><mo>]</mo></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>"</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math> for atleast two <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>"</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math> for exactly one <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>"</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math> for no <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>"</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math> for atleast two <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>g</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>g</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>-</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>g</mi><mo>'</mo></msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mo>-</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>-</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></math> has three roots and thus <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>"</mo></msup><mfenced><mi>x</mi></mfenced></math> will have atleast two roots in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q3. JEE Main 2022 (29 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi></math> be twice differentiable even functions on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></math> Then, the minimum number of solutions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><msup><mi>g</mi><mrow><mo>'</mo><mo>'</mo></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>g</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced></math> roots
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is even <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mo>=</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> has two roots as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mo>=</mo><mi>g</mi><mfenced><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math> (as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is even function)</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> will have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> roots, hence its derivative <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> will have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> roots.</p>

</details>

---

### Q4. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> be any continuous function on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> and twice differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>2</mn><mo>,</mo></math> then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>2</mn></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>x</mi></math></p><p>Clearly <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mi>x</mi></mfenced></math>, will be continuous and twice differentiable on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>h</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>h</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p>By Rolle&#39;s mean value theorem in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mo>&#39;</mo></msup><mfenced><msub><mi>c</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msub><mi>c</mi><mn>1</mn></msub></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msub><mi>c</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>1</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>c</mi><mn>1</mn></msub><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p>Also, in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mo>&#39;</mo></msup><mfenced><msub><mi>c</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mi>&#1472;</mi></msup><mfenced><msub><mi>c</mi><mn>2</mn></msub></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msub><mi>c</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>1</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>c</mi><mn>2</mn></msub><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math></p><p>Now, use Rolle&#39;s theorem on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msub><mi>c</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>c</mi><mn>2</mn></msub></mrow></mfenced></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math>, </p><p> We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mo>&#39;&#39;</mo></msup><mo>(</mo><mi>c</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;&#39;</mo></msup><mo>(</mo><mi>c</mi><mo>)</mo><mo>=</mo><mn>0</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>&#8712;</mo><mfenced><mrow><msub><mi>c</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>c</mi><mn>2</mn></msub></mrow></mfenced></math></p><p>Hence,  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;&#39;</mo></msup><mo>(</mo><mi>c</mi><mo>)</mo><mo>=</mo><mn>0</mn></math> for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>.</p>

</details>

---

### Q5. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be twice differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>x</mi></msubsup><mi>g</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math> for a differentiable function <u><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>.</mo></math></u> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> has exactly five distinct roots in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> has at least :

**Options:**

- **(A)** twelve roots in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math>
- **(B)** five roots in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math>
- **(C)** seven roots in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math>
- **(D)** three roots in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) seven roots in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math>**

**Detailed Solution:**

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be twice differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>x</mi></msubsup><mi>g</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math> for a differentiable function <u><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>,</mo></math></u><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c775a83d-7acf-4b2c-b16d-a31d4ff4b6b8-image.png" style="width: 282px; height: 105px;" /></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>x</mi></msubsup><mi>g</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> roots</p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> has atleast <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> roots</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> has atleast <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> roots</p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> has atleast <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> roots.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></math> has atleast <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> roots.</p>

</details>

---

### Q6. JEE Main 2021 (25 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If Rolle&#39;s theorem holds for the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>-</mo><mn>4</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math>, then ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>8</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>5</mn><mo>,</mo><mn>8</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>8</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mo>-</mo><mn>8</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>8</mn></mrow></mfenced></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>1</mn><mo>-</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>8</mn><mo>-</mo><mn>4</mn><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>3</mn><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mn>7</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math> (given)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mrow><mi>x</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mn>16</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>8</mn><mi>a</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>8</mn><mi>a</mi><mo>-</mo><mn>3</mn><mi>b</mi><mo>-</mo><mn>16</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q7. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

For all twice differentiable functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>&#160;</mo><mo>:</mo><mo mathvariant="bold">&#160;</mo><mi mathvariant="bold">R</mi><mo mathvariant="bold">&#8594;</mo><mi mathvariant="bold">R</mi></math>, with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi mathvariant="normal">f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi mathvariant="normal">f</mi><mo>&#39;</mo><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math>,

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>&#34;</mo><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>&#8800;</mo><mn>0</mn></math> at every point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>&#949;</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>&#34;</mo><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mn>0</mn></math>, for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&#160;</mo><mi>&#949;</mi><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>&#34;</mo><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>&#34;</mo><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mn>0</mn></math>, at every point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&#160;</mo><mi>&#949;</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>&#34;</mo><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mn>0</mn></math>, at every point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&#160;</mo><mi>&#949;</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Applying Rolle&#39;s theorem in [0,1] for function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><mi>c</mi></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#160;</mo><mi>&#949;</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>again applying Rolle&#39;s theorem in [0, c] for function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>'</mo><mo>(</mo><mi>x</mi><mo>)</mo></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>'</mo><mo>'</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p> </p>

</details>

---

### Q8. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> be a twice differentiable function on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>, If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>4</mn><mo>,</mo></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>, then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>5</mn></mfenced><mo>&#8804;</mo><mn>26</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>5</mn></mfenced><mo>&#8805;</mo><mn>28</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>5</mn></mfenced><mo>+</mo><mi>f</mi><mo>'</mo><mo>'</mo><mfenced><mn>5</mn></mfenced><mo>&#8804;</mo><mn>20</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>&#8804;</mo><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>5</mn></mfenced><mo>&#8805;</mo><mn>28</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;&#8201;</mtext><munderover><mo>&#8747;</mo><mn>2</mn><mn>5</mn></munderover><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>&#8805;</mo><munderover><mo>&#8747;</mo><mn>2</mn><mn>5</mn></munderover><mn>1</mn><mo>.</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mn>2</mn><mn>5</mn></msubsup><mo>&#8805;</mo><msubsup><mfenced><mi>x</mi></mfenced><mn>2</mn><mn>5</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>&#8722;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>&#8805;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>&#8805;</mo><mn>11</mn></math>      ....<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>4</mn><mo>&#8658;</mo><munderover><mo>&#8747;</mo><mn>2</mn><mn>5</mn></munderover><mi>f</mi><mo>&#39;</mo><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>&#8805;</mo><munderover><mo>&#8747;</mo><mn>2</mn><mn>5</mn></munderover><mn>4</mn><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced><mrow><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced></mrow></mfenced><mn>2</mn><mn>5</mn></msubsup><mo>&#8805;</mo><msubsup><mfenced><mrow><mn>4</mn><mi>x</mi></mrow></mfenced><mn>2</mn><mn>5</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;&#8201;</mtext><mi>f</mi><mo>&#39;</mo><mfenced><mn>5</mn></mfenced><mo>&#8722;</mo><mi>f</mi><mo>&#39;</mo><mfenced><mn>2</mn></mfenced><mo>&#8805;</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;&#8201;</mtext><mi>f</mi><mo>&#39;</mo><mfenced><mn>5</mn></mfenced><mo>&#8805;</mo><mn>17</mn></math>    ....<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>+</mo><mfenced><mn>2</mn></mfenced><mo>&#8658;</mo><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>+</mo><mi>f</mi><mo>&#39;</mo><mfenced><mn>5</mn></mfenced><mo>&#8805;</mo><mn>28</mn></math>.</p>

</details>

---

### Q9. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>c</mi></math> is a point at which Rolle&rsquo;s theorem holds for the function, <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></msub></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>&#945;</mi></mrow><mrow><mn>7</mn><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow></math> in the interval <math><mfenced close="]" open="[" separators="|"><mrow><mn>3</mn><mo>,</mo><mi></mi><mn>4</mn></mrow></mfenced><mo>,</mo></math> where <math><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> then <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>c</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>24</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>7</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced><mo>&#8658;</mo><mi>α</mi><mo>=</mo><mn>12</mn></math>  
<math><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>12</mn></mrow><mrow><mi>x</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>12</mn></mrow></mfenced></mrow></mfrac></math>  
<math><mo>∴</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>c</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><mo>∴</mo><mi>c</mi><mo>=</mo><msqrt><mn>12</mn></msqrt></math>  
<math><mo>∴</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>c</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>

</details>

---

### Q10. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>, in the Lagrange&rsquo;s mean value theorem for the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>11</mn><mo>,</mo></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mn>0,1</mn></mfenced></math>, is

**Options:**

- **(A)** <math><mfrac><mrow><mn>4</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>4</mn><mo>-</mo><msqrt><mn>7</mn></msqrt></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><msqrt><mn>7</mn></msqrt><mo>-</mo><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>4</mn><mo>-</mo><msqrt><mn>7</mn></msqrt></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math>, is polynomial function, so it is continuous and differentiable in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mn>0,1</mn></mfenced></math>.</p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>11</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mn>4</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>11</mn><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>f</mi><mo>.</mo></msup><mfenced separators="|"><mi>c</mi></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mn>0</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>16</mn><mo>-</mo><mn>11</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mn>3</mn><msup><mi>c</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>c</mi><mo>+</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>c</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>c</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math><mi>c</mi><mo>=</mo><mfrac><mrow><mn>8</mn><mo>&#177;</mo><mn>2</mn><msqrt><mn>7</mn></msqrt></mrow><mrow><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mo>&#177;</mo><msqrt><mn>7</mn></msqrt></mrow><mrow><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>c</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mo>-</mo><msqrt><mn>7</mn></msqrt></mrow><mn>3</mn></mfrac><mo>&#8712;</mo><mfenced separators="|"><mn>0,1</mn></mfenced></math>.</p>

</details>

---

### Q11. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the function <math><mo>,</mo><mi mathvariant="normal"></mi><mi>f</mi><mo>:</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mn>7</mn><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be continuous on <math><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mn>7</mn><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced></math> and differentiable on <math><mfenced separators="|"><mrow><mo>-</mo><mn>7</mn><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced><mo>.</mo></math> If <math><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>3</mn></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#8804;</mo><mn>2</mn></math> for all <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mn>7</mn><mo>,</mo><mi></mi><mn>0</mn></mrow></mfenced><mo>,</mo><mi></mi></math> then for all such functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced></math> lies in the interval

**Options:**

- **(A)** <math><mfenced close="]" separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mi></mi><mn>20</mn></mrow></mfenced></math>
- **(B)** <math><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mi></mi><mn>11</mn></mrow></mfenced></math>
- **(C)** <math><mfenced close="]" separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mi></mi><mn>11</mn></mrow></mfenced></math>
- **(D)** <math><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mn>6</mn><mo>,</mo><mi></mi><mn>20</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfenced close="]" separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mi></mi><mn>20</mn></mrow></mfenced></math>**

**Detailed Solution:**

Lets use LMVT for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mn>7</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>
<math><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>7</mn></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>7</mn></mrow></mfenced></mrow></mfrac><mo>&#8804;</mo><mn>2</mn></math>
<math><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>&#8804;</mo><mn>2</mn><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mn>9</mn></math>
Lets use LMVT for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mn>7</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>
<math><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>7</mn></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><mn>0</mn><mo>+</mo><mn>7</mn></mrow></mfenced></mrow></mfrac><mo>&#8804;</mo><mn>2</mn></math>
<math><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>+</mo><mn>3</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mo>&#8804;</mo><mn>2</mn><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>&#8804;</mo><mn>11</mn></math> <math><mo>&#8756;</mo><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mn>20</mn></math>

</details>

---

### Q12. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If Rolle&#39;s theorem holds for the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>c</mi><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> at the point <math><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo></math> then <math><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Since, Rolle&#39;s theorem is satisfied in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>]</mo></math> and corresponding to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> we have  <math> <mi>f</mi><mo stretchy="false">(</mo><mo>&#8722;</mo><mn>1</mn><mo stretchy="false">)</mo><mo>=</mo><mi>f</mi><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo> </math>   &amp;   <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math> <mo>&#8722;</mo><mn>2</mn><mo>+</mo><mi>b</mi><mo>&#8722;</mo><mi>c</mi><mo>=</mo><mn>2</mn><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi> </math></p><p><math> <mo>&#8658;</mo> <mi>c</mi><mo>=</mo><mo>&#8722;</mo><mn>2</mn> </math></p><p>Further <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Put <math><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mi>&#160;</mi><mi>&#160;</mi></math></p><p><math><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math></p><p>Hence, <math><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q13. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If the Rolle&#39;s theorem holds for the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>&#8722;</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> for the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>, then the value of <math> <mrow> <mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi> </mrow> </math> is:

**Options:**

- **(A)** <math><mo>-1</mo></math>
- **(B)** <math><mo>2</mo></math>
- **(C)** <math><mo>1</mo></math>
- **(D)** <math><mo>-2</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>-1</mo></math>**

**Detailed Solution:**

<p>Given that the function holds Rolle&#39;s theorem in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>&#8722;</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8722;</mo><mn>2</mn><mo>+</mo><mi>a</mi><mo>&#8722;</mo><mi>b</mi><mo>=</mo><mn>2</mn><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>6</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mi>a</mi><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q14. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#38;</mo><mo>&#160;</mo><mi>g</mi></math> are differentiable functions in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>]</mo><mo>&#160;</mo></math>satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>2</mn><mo>=</mo><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>,</mo><mo>&#160;</mo><mi>g</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo></math> then for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>&#8712;]0,&#160;1[</mo></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>c</mi></mfenced><mo>=</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>c</mi></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>c</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>c</mi></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>c</mi></mfenced><mo>=</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>c</mi></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>c</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>c</mi></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>c</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>c</mi></mfenced></math>**

**Detailed Solution:**

Let <math><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> clearly <math><mi>h</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mi>h</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></math>

Also <math><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is continuous and differentiable.

Hence <math><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> satisfy all conditions of Rolle&#39;s theorem in <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math>. According to Rolle&#39;s theorem there exist atleast one <math><mi>c</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>-</mo><mn>2</mn><msup><mi>g</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>c</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>g</mi><mo>'</mo></msup><mfenced separators="|"><mi>c</mi></mfenced></math>.

</details>

---

### Q15. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

A value of $C$ for which the conclusion of Mean Value Theorem holds for the function $f(x)=$ $\log _{\mathrm{e}} x$ on the interval $[1,3]$ is

**Options:**

- **(A)** $2 \log _3 e$
- **(B)** $\frac{1}{2} \log _{\mathrm{e}} 3$
- **(C)** $\log _3 e$
- **(D)** $\log _e 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \log _3 e$**

**Detailed Solution:**

Using mean value theorem
$\begin{aligned}
& f^{\prime}(c)=\frac{f(3)-f(1)}{3-1} \\
& \Rightarrow \frac{1}{c}=\frac{\log 3-\log 1}{2} \\
& \Rightarrow c=\frac{2}{\log _e 3}=2 \log _3 e.
\end{aligned}$

</details>

---

### Q16. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

Let $f$ be differentiable for all $x$. If $f(1)=-2$ and $f^{\prime}(x) \geq 2$ for $x \in[1,6]$, then

**Options:**

- **(A)** $f(6) \geq 8$
- **(B)** $f(6) < 8$
- **(C)** $f(6) < 5$
- **(D)** $f(6)=5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $f(6) \geq 8$**

**Detailed Solution:**

As $f(1)=-2 \quad \& f^{\prime}(x) \geq 2 \quad \forall x \in[1,6]$
Applying Lagrange's mean value theorem
$$
\begin{aligned}
& \frac{f(6)-f(1)}{5}=f^{\prime}(c) \geq 2 \\
& \Rightarrow f(6) \geq 10+f(1) \\
& \Rightarrow f(6) \geq 10-2 \\
& \Rightarrow f(6) \geq 8 .
\end{aligned}
$$

</details>

---

