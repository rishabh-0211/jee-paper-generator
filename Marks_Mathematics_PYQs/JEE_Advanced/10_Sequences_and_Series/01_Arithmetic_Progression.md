# JEE Advanced Mathematics - Sequences and Series

## Topic 1: Arithmetic Progression

**Total Questions:** 10

---

### Q1. JEE Advanced 2025 (Paper 1)

*Type:* `numerical` | *Level:* `1`

Let $\mathbb{R}$ denote the set of all real numbers. Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be a function such that $f(x)>0$ for all $x \in \mathbb{R}$, and $f(x+y)=f(x) f(y)$ for all $x, y \in \mathbb{R}$.
Let the real numbers $\mathrm{a}_1, \mathrm{a}_2 \ldots, \mathrm{a}_{50}$ be in an arithmetic progression. If $f\left(\mathrm{a}_{31}\right)=64 f\left(\mathrm{a}_{25}\right)$, and $\sum_{i=1}^{50} f\left(a_i\right)=3\left(2^{25}+1\right)$ then the value of $\sum_{i=6}^{30} f\left(a_i\right)$ is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **96**

**Detailed Solution:**

$\begin{aligned} & \because f(x+y)=f(x) \cdot f(y) \\ & \Rightarrow f(x)=k^x \quad(f(x)>0 \forall x \in R) \\ & \because f\left(a_{31}\right)=64 f\left(a_{25}\right)\end{aligned}$
$\begin{aligned} & \Rightarrow \mathrm{k}^{(\mathrm{a}+30 \mathrm{~d})}=64 \cdot \mathrm{k}^{(\mathrm{a}+24 \mathrm{~d})} \\ & \Rightarrow \mathrm{k}^{6 \mathrm{~d}}=64 \\ & \Rightarrow \mathrm{k}^{\mathrm{d}}=2\end{aligned}$
$\sum_{\mathrm{i}=1}^{50} \mathrm{f}\left(\mathrm{a}_{\mathrm{i}}\right)=\mathrm{f}\left(\mathrm{a}_1\right)+\mathrm{f}\left(\mathrm{a}_2\right)+\ldots \ldots+\mathrm{f}\left(\mathrm{a}_{50}\right)$
$\begin{aligned} & =\mathrm{k}^{\mathrm{a}}+\mathrm{k}^{\mathrm{a}+\mathrm{d}}+\ldots+\mathrm{k}^{\mathrm{a}+49 \mathrm{~d}}=\frac{\mathrm{k}^{\mathrm{a}}\left(\mathrm{k}^{50 \mathrm{~d}}-1\right)}{\mathrm{k}^{\mathrm{d}}-1} \\ & =\mathrm{k}^{\mathrm{a}}\left(2^{50}-1\right)=3\left(2^{25}+1\right)(\text { Given }) \\ & \Rightarrow \mathrm{k}^{\mathrm{a}}=\frac{3}{2^{25}-1}\end{aligned}$
$\begin{aligned} & \therefore \sum_{\mathrm{i}=6}^{30} \mathrm{f}\left(\mathrm{a}_{\mathrm{i}}\right)=\mathrm{k}^{\mathrm{a}+5 \mathrm{~d}}+\mathrm{k}^{\mathrm{a}+6 \mathrm{~d}}+\ldots+\mathrm{k}^{\mathrm{a}+29 \mathrm{~d}} \\ & \quad=\mathrm{k}^{\mathrm{a}+5 \mathrm{~d}} \frac{\left(\mathrm{k}^{25 \mathrm{~d}}-1\right)}{\mathrm{k}^{\mathrm{d}}-1}=\mathrm{k}^{\mathrm{a}} \cdot\left(\mathrm{k}^{\mathrm{d}}\right)^5\left(2^{25}-1\right) \\ & \quad=\frac{3}{2^{25}-1} \cdot 2^5\left(2^{25}-1\right)=96\end{aligned}$

</details>

---

### Q2. JEE Advanced 2022 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub><mo>,</mo><msub><mi>l</mi><mn>2</mn></msub><mo>.</mo><mo>.</mo><mo>.</mo><msub><mi>l</mi><mn>100</mn></msub></math> be consecutive terms of an arithmetic progression with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub></math>, and let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mn>1</mn></msub><mo>,</mo><msub><mi>w</mi><mn>2</mn></msub></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8230;</mo><mo>,</mo><msub><mi>w</mi><mn>100</mn></msub></math> be consecutive terms of another arithmetic progression with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>2</mn></msub></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mn>10</mn></math>. For each <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>100</mn></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>i</mi></msub></math> be a rectangle with length <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mi>i</mi></msub></math>, width <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mi>i</mi></msub></math> and area <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>i</mi></msub></math>.If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>51</mn></msub><mo>-</mo><msub><mi>A</mi><mn>50</mn></msub><mo>=</mo><mn>1000</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>100</mn></msub><mo>-</mo><msub><mi>A</mi><mn>90</mn></msub></math> is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18900**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub><mo>,</mo><msub><mi>l</mi><mn>2</mn></msub><mo>.</mo><mo>.</mo><mo>.</mo><msub><mi>l</mi><mn>100</mn></msub></math> are consecutive terms of an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub><mo>=</mo><mi>a</mi></math> and common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>d</mi><mn>1</mn></msub></math> </p><p>And similarly for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mn>1</mn></msub><mo>,</mo><msub><mi>w</mi><mn>2</mn></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><msub><mi>w</mi><mn>100</mn></msub></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub><mo>=</mo><mi>b</mi></math> and common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>d</mi><mn>2</mn></msub></math></p><p>Now given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>51</mn></msub><mo>-</mo><msub><mi>A</mi><mn>50</mn></msub><mo>=</mo><msub><mi>l</mi><mn>51</mn></msub><msub><mi>w</mi><mn>51</mn></msub><mo>-</mo><msub><mi>l</mi><mn>50</mn></msub><msub><mi>w</mi><mn>50</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>50</mn><msub><mi>d</mi><mn>1</mn></msub></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>+</mo><mn>50</mn><msub><mi>d</mi><mn>2</mn></msub></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>49</mn><msub><mi>d</mi><mn>1</mn></msub></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>+</mo><mn>49</mn><msub><mi>d</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>1000</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>50</mn><mi>b</mi><msub><mi>d</mi><mn>1</mn></msub><mo>+</mo><mn>50</mn><mi>a</mi><msub><mi>d</mi><mn>2</mn></msub><mo>+</mo><mn>2500</mn><msub><mi>d</mi><mn>1</mn></msub><msub><mi>d</mi><mn>2</mn></msub><mo>-</mo><mn>49</mn><mi>a</mi><msub><mi>d</mi><mn>2</mn></msub><mo>-</mo><mn>49</mn><mi>b</mi><msub><mi>d</mi><mn>1</mn></msub><mo>-</mo><mn>2401</mn><msub><mi>d</mi><mn>1</mn></msub><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mn>1000</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><msub><mi>d</mi><mn>1</mn></msub><mo>+</mo><mi>a</mi><msub><mi>d</mi><mn>2</mn></msub><mo>+</mo><mn>99</mn><msub><mi>d</mi><mn>1</mn></msub><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mn>1000</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><msub><mi>d</mi><mn>1</mn></msub><mo>+</mo><mi>a</mi><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mn>10</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as&#160;given&#160;</mtext><msub><mi>d</mi><mn>1</mn></msub><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mn>10</mn></mrow></mfenced></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>100</mn></msub><mo>-</mo><msub><mi>A</mi><mn>90</mn></msub><mo>=</mo><msub><mi>l</mi><mn>100</mn></msub><msub><mi>w</mi><mn>100</mn></msub><mo>-</mo><msub><mi>l</mi><mn>90</mn></msub><msub><mi>w</mi><mn>90</mn></msub></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>99</mn><msub><mi>d</mi><mn>1</mn></msub></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>+</mo><mn>99</mn><msub><mi>d</mi><mn>2</mn></msub></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>89</mn><msub><mi>d</mi><mn>1</mn></msub></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>+</mo><mn>89</mn><msub><mi>d</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>99</mn><mi>b</mi><msub><mi>d</mi><mn>1</mn></msub><mo>+</mo><mn>99</mn><mi>a</mi><msub><mi>d</mi><mn>2</mn></msub><mo>+</mo><msup><mn>99</mn><mn>2</mn></msup><msub><mi>d</mi><mn>1</mn></msub><msub><mi>d</mi><mn>2</mn></msub><mo>-</mo><mn>89</mn><mi>b</mi><msub><mi>d</mi><mn>1</mn></msub><mo>-</mo><mn>89</mn><mi>a</mi><msub><mi>d</mi><mn>2</mn></msub><mo>-</mo><msup><mn>89</mn><mn>2</mn></msup><msub><mi>d</mi><mn>1</mn></msub><msub><mi>d</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mfenced><mrow><mi>b</mi><msub><mi>d</mi><mn>1</mn></msub><mo>+</mo><mi>a</mi><msub><mi>d</mi><mn>2</mn></msub></mrow></mfenced><mo>+</mo><mn>1880</mn><msub><mi>d</mi><mn>1</mn></msub><msub><mi>d</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mfenced><mn>10</mn></mfenced><mo>+</mo><mn>18800</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>again&#160;using&#160;</mtext><msub><mi>d</mi><mn>1</mn></msub><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mn>10</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>b</mi><msub><mi>d</mi><mn>1</mn></msub><mo>+</mo><mi>a</mi><msub><mi>d</mi><mn>2</mn></msub><mo>=</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>18900</mn></math></p></blockquote>

</details>

---

### Q3. JEE Advanced 2019 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Let <math><mi mathvariant="normal">A</mi><mi mathvariant="normal">P</mi><mi mathvariant="normal">&#160;</mi><mfenced separators="|"><mrow><mi mathvariant="normal">a</mi><mo>;</mo><mi mathvariant="normal">d</mi></mrow></mfenced></math> denote the set of all the terms of an infinite arithmetic progression with first term a and common difference <math><mi mathvariant="normal">d</mi><mo>&#62;</mo><mn>0</mn><mo>.</mo></math> If <math><mi mathvariant="normal">A</mi><mi mathvariant="normal">P</mi><mfenced separators="|"><mrow><mn>1</mn><mo>;</mo><mn>3</mn></mrow></mfenced><mo>&#8745;</mo><mi mathvariant="normal">A</mi><mi mathvariant="normal">P</mi><mfenced separators="|"><mrow><mn>2</mn><mo>;</mo><mn>5</mn></mrow></mfenced><mo>&#8745;</mo><mi mathvariant="normal">A</mi><mi mathvariant="normal">P</mi><mfenced separators="|"><mrow><mn>3</mn><mo>;</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mi mathvariant="normal">A</mi><mi mathvariant="normal">P</mi><mfenced separators="|"><mrow><mi mathvariant="normal">a</mi><mo>;</mo><mi mathvariant="normal">d</mi></mrow></mfenced></math> then <math><mi mathvariant="normal">a</mi><mo>+</mo><mi mathvariant="normal">d</mi></math> equals ____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **157**

**Detailed Solution:**

Let <math><msub><mrow><mi>T</mi></mrow><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>m</mi></mrow></mfenced></mrow></msub><mo>:</mo></math> <math><msup><mrow><mi>m</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> term of <math><msup><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">t</mi></mrow></msup></math> series <math><mi>A</mi><mfenced separators="|"><mrow><mn>1</mn><mo>;</mo><mn>3</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi>&#160;</mi><mi>n</mi></mrow></mfenced></msub><mo>:</mo></math> <math><msup><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> term of <math><msup><mrow><mn>2</mn></mrow><mrow><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi></mrow></msup></math> series <math><mi>A</mi><mfenced separators="|"><mrow><mn>2</mn><mo>;</mo><mn>5</mn></mrow></mfenced></math>
<math><msub><mrow><mi>T</mi></mrow><mrow><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mi>&#160;</mi><mi>r</mi></mrow></mfenced></mrow></msub><mo>:</mo></math> <math><msup><mrow><mi>r</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> term of <math><msup><mrow><mn>3</mn></mrow><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">d</mi></mrow></msup></math> series <math><mi>A</mi><mo>(</mo><mn>3</mn><mo>;</mo><mn>7</mn><mo>)</mo></math>
For common terms
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mo>(</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>m</mi><mo>)</mo></mrow></msub><mo>=</mo><msub><mi>T</mi><mrow><mo>(</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><mi>n</mi><mo>)</mo></mrow></msub><mo>=</mo><msub><mi>T</mi><mrow><mo>(</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mi>r</mi><mo>)</mo></mrow></msub></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>3</mn><mfenced separators="|"><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mo>+</mo><mn>5</mn><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>3</mn><mo>+</mo><mn>7</mn><mfenced separators="|"><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>m</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>5</mn><mi>n</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>7</mn><mi>r</mi><mo>-</mo><mn>4</mn></math>
<math><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mtext>&#8201;&#8201;&#8201;</mtext><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mtext>&#8201;&#8201;&#8201;</mtext><mi>r</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>7</mn></mrow></mfrac></math>
For <math><mi>&#8216;</mi><mi>m</mi><mi>&#8217;</mi></math> to be a natural number <math><mi>n</mi><mo>=</mo><mn>2,5</mn><mo>,</mo><mn>11</mn><mo>,</mo><mo>&#8230;</mo></math>
And for <math><mi>&#8216;</mi><mi>r</mi><mi>&#8217;</mi></math> to be a natural number <math><mi>n</mi><mo>=</mo><mn>4,11</mn><mo>,</mo><mo>&#8230;</mo></math>
When <math><mi>n</mi><mo>=</mo><mn>11</mn><mo>,</mo><mi>m</mi><mo>=</mo><mn>18</mn></math> and <math><mi>r</mi><mo>=</mo><mn>8</mn></math>
<math><mo>&#8658;</mo></math> For <math><msup><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">t</mi></mrow></msup></math> common term of three series <math><mi>A</mi><mo>(</mo><mi>a</mi><mo>,</mo><mi>d</mi><mo>)</mo></math>
<math><mi>a</mi><mo>=</mo><msup><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">t</mi></mrow></msup></math> term of <math><mi>A</mi><mo>(</mo><mn>1,3</mn><mo>)</mo></math>
<math><mi>a</mi><mo>=</mo><mn>1</mn><mo>+</mo><mo>(</mo><mn>18</mn><mn>1</mn><mo>)</mo><mn>3</mn><mo>=</mo><mn>52</mn></math>
<math><mo>&#8658;</mo></math> Common difference of <math><mi>A</mi><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mi mathvariant="normal">L</mi><mi mathvariant="normal">C</mi><mi mathvariant="normal">M</mi></math> of common difference of <math><mfenced separators="|"><mrow><mi>A</mi><mfenced separators="|"><mrow><mn>1</mn><mo>;</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mi>A</mi><mfenced separators="|"><mrow><mn>2</mn><mo>;</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mi>A</mi><mfenced separators="|"><mrow><mn>3</mn><mo>;</mo><mn>7</mn></mrow></mfenced></mrow></mfenced></math>
<math><mi>d</mi><mo>=</mo><mi mathvariant="normal">L</mi><mi mathvariant="normal">C</mi><mi mathvariant="normal">M</mi><mi>&#160;</mi><mo>(</mo><mn>3</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn><mo>,</mo><mi>&#160;</mi><mn>7</mn><mo>)</mo></math>
<math><mi>d</mi><mo>=</mo><mn>105</mn></math>
Hence, <math><mi>a</mi><mo>+</mo><mi>d</mi><mo>=</mo><mn>52</mn><mo>+</mo><mn>105</mn><mo>=</mo><mn>157</mn></math>

</details>

---

### Q4. JEE Advanced 2018 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Let <math><mi>X</mi></math> be the set consisting of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2018</mn></math> terms of the arithmetic progression <math><mn>1,6</mn><mo>,</mo><mn>11</mn><mo>,</mo><mo>&#8230;</mo><mi>&#160;</mi><mo>,</mo></math> and <math><mi>Y</mi></math> be the set consisting of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2018</mn></math> terms of the arithmetic progression <math><mn>9,16,23</mn><mo>,</mo><mo>&#8230;</mo><mi>&#160;</mi></math> . Then, the number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>&#8746;</mo><mi>Y</mi></math> is___.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3748**

**Detailed Solution:**

<math><mi>X</mi><mo>:</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>6</mn><mo>,</mo><mi>&#160;</mi><mn>11</mn><mo>,</mo><mi>&#160;</mi><mo>&#8230;</mo><mo>,</mo><mn>10086</mn></math>
<math><mi>Y</mi><mo>:</mo><mn>9</mn><mo>,</mo><mi>&#160;</mi><mn>16</mn><mo>,</mo><mi>&#160;</mi><mn>23</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>,</mo><mn>14128</mn></math>
<math><mi>X</mi><mo>&#8745;</mo><mi>Y</mi><mo>:</mo><mn>16</mn><mo>,</mo><mi>&#160;</mi><mn>51</mn><mo>,</mo><mi>&#160;</mi><mn>86</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo></math>
Let <math><mi>m</mi><mo>=</mo><mi>n</mi><mfenced separators="|"><mrow><mi>X</mi><mo>&#8745;</mo><mi>Y</mi></mrow></mfenced></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mn>16</mn><mo>+</mo><mfenced separators="|"><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mn>35</mn><mo>&#8804;</mo><mn>10086</mn></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>m</mi><mo>&#8804;</mo><mn>288.71</mn></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>m</mi><mo>=</mo><mn>288</mn></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>n</mi><mfenced separators="|"><mrow><mi>X</mi><mo>&#8746;</mo><mi>Y</mi></mrow></mfenced><mo>=</mo><mi>n</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mo>+</mo><mi>n</mi><mfenced separators="|"><mrow><mi>Y</mi></mrow></mfenced><mo>-</mo><mi>n</mi><mfenced separators="|"><mrow><mi>X</mi><mo>&#8745;</mo><mi>Y</mi></mrow></mfenced></math>
<math><mo>=</mo><mi>&#160;</mi><mi>&#160;</mi><mn>2018</mn><mo>+</mo><mn>2018</mn><mo>-</mo><mn>288</mn><mo>=</mo><mn>3748</mn></math>

</details>

---

### Q5. JEE Advanced 2017 (Paper 1)

*Type:* `numerical` | *Level:* `2`

The sides of a right-angled triangle are in arithmetic progression. If the triangle has area 24 square units, then what is the length of its smallest side?

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p>Let three sides of triangle be: <math><mi>a</mi><mo>-</mo><mi>d</mi><mo>,</mo><mi mathvariant="italic"> a</mi><mo>,</mo><mi mathvariant="italic"> a</mi><mo>+</mo><mi>d</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/46_solu_math_pap1.jpg"/></p><p>Where, <math><mi>d</mi><mo>></mo><mn>0</mn><mo>,</mo><mi> </mi><mi>a</mi><mo>></mo><mn>0</mn></math>.</p><p><math><mo>⇒</mo></math>  length of smallest side <math><mo>=</mo><mi>a</mi><mo>-</mo><mi>d</mi></math> units</p><p>Now,  <math> <mrow> <msup> <mrow> <mrow><mo>(</mo> <mrow> <mi>a</mi><mo>+</mo><mi>d</mi> </mrow> <mo>)</mo></mrow> </mrow> <mn>2</mn> </msup> <mo>=</mo><msup> <mi>a</mi> <mn>2</mn> </msup> <mo>+</mo><msup> <mrow> <mrow><mo>(</mo> <mrow> <mi>a</mi><mo>−</mo><mi>d</mi> </mrow> <mo>)</mo></mrow> </mrow> <mn>2</mn> </msup> </mrow> </math></p><p><math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi>a</mi><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>4</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi>a</mi><mo>=</mo><mn>4</mn><mi>d</mi></math>        .....(i)</p><p>(As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo> </mo><mo>=</mo><mo> </mo><mn>0</mn></math> is rejected)</p><p>Also,    <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>a</mi><mo>.</mo><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mn>24</mn></math></p><p><math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi>a</mi><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mn>48</mn></math>        .....(ii)</p><p><math><mo>∴</mo></math>     From (i) and (ii), we get  <math><mi>a</mi><mo>=</mo><mn>8</mn><mo>,</mo><mi> </mi><mi>d</mi><mo>=</mo><mn>2</mn></math></p><p>Hence, length of smallest side is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mn>8</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>6</mn></math>units</p>

</details>

---

### Q6. JEE Advanced 2015 (Paper 2)

*Type:* `numerical` | *Level:* `1`

Suppose that all the terms of an arithmetic progression (A.P.) are natural numbers. If the ratio of the sum of the first seven terms to the sum of the first eleven terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>:</mo><mn>11</mn></math> and the seventh terms lies in between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>130</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>140</mn></math>, then the common difference of this A.P. is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<math><mfrac><mrow><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>[</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>6</mn><mi>d</mi><mo>]</mo></mrow><mrow><mfrac><mrow><mn>11</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>[</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>10</mn><mi>d</mi><mo>]</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mn>11</mn></mrow></mfrac></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mfrac><mrow><mi>a</mi><mo>+</mo><mn>3</mn><mi>d</mi></mrow><mrow><mi>a</mi><mo>+</mo><mn>5</mn><mi>d</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math> 
 <math><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>9</mn><mi>d</mi></math> 
Also   <math><mn>130</mn><mo>&lt;</mo><mi>a</mi><mo>+</mo><mn>6</mn><mi>d</mi><mo>&lt;</mo><mn>140</mn></math> 
 <math><mn>130</mn><mo>&lt;</mo><mn>15</mn><mi>d</mi><mo>&lt;</mo><mn>140</mn></math> 
 <math><mo>⇒</mo><mi>d</mi><mo>=</mo><mn>9</mn></math>

</details>

---

### Q7. JEE Advanced 2011 (Paper 1)

*Type:* `numerical` | *Level:* `1`

Let $a_1, a_2, a_3, \ldots ., a_{100}$ be an arithmetic progression with $a_1=3$ and $S_p=\sum_{i=1}^p a_i$, $1 \leq p \leq 100$. For any integer $n$ with $1 \leq n \leq 20$, let $m=5 n$. If $\frac{S_m}{S_n}$ does not depend on $n$, then $a_2$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

Given, $a_1=3, m=5 n$ and $a_1, a_2, \ldots$ are in AP. $\therefore \frac{S_m}{S_n}=\frac{S_{5 n}}{S_n}$ is independent of $n$. Now, $\quad \frac{\frac{5 n}{2}[2 \times 3+(5 n-1) d]}{\frac{n}{2}[2 \times 3+(n-1) d]}$ $\Rightarrow \quad \frac{f\{(6-d)+5 n\}}{(6-d)+n}$ independent of $n$, if $\begin{aligned} \quad 6-d= & 0 \Rightarrow d=6 \\ \therefore \quad a_2= & a_1+d=3+6=9 \\ & \text { Or }\end{aligned}$
If $d=0$ $\frac{S_m}{S_n}$ is independent of $n$.
$$
\therefore \quad a_2=3
$$

</details>

---

### Q8. JEE Advanced 2010 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let $a_1, a_2, a_3, \ldots, a_{11}$ be real numbers satisfying $a_1=15,27-2 a_2>0$ and $a_k=2 a_{k-1}-a_{k-2}$ for $k=3,4, \ldots, 11$.
If $\frac{a_1^2+a_2^2+\ldots+a_{11}^2}{11}=90$, then the value of $\frac{a_1+a_2+\ldots+a_{11}}{11}$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

$$
\text { } \begin{aligned}
& a_k=2 a_{k-1}-a_{k-2} \\
& \Rightarrow \quad a_1, a_2, \ldots, a_{11} \text { are in AP } \\
& \therefore \frac{a_1^2+a_2^2+\ldots+a_{11}^2}{11} \\
&=\frac{11 a^2+35 \times 11 d^2+10 a d}{11}=90 \\
& \Rightarrow \quad 225+35 d^2+150 d=90 \\
& 35 d^2+150 d+135=0 \\
& \Rightarrow \quad d=-3,-\frac{9}{7}
\end{aligned}
$$
Given, $a_2 < \frac{27}{2} \therefore d=-3$ and $d \neq-\frac{9}{7}$
$$
\Rightarrow \quad \frac{a_1+a_2+\ldots+a_{11}}{11}
$$
$$
=\frac{11}{2}[30-10 \times 3]=0
$$

</details>

---

### Q9. JEE Advanced 2007 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Let $V_r$ denotes the sum of the first $r$ terms of an arithmetic progression $(A P)$ whose first term is $r$ and the common difference is $(2 r-1)$. Let $T_r=V_{r+1}-V_r-2$ and $Q_r=T_{r+1}-T_r$ for $r=1,2, \ldots$<strong>Question:</strong>
Which one of the following is a correct statement?

**Options:**

- **(A)** $Q_1, Q_2, Q_3, \ldots$ are in AP with common difference 5
- **(B)** $Q_1, Q_2, Q_3, \ldots$ are in AP with common difference 6
- **(C)** $Q_1, Q_2, Q_3, \ldots$ are in AP with common difference 11
- **(D)** $Q_1=Q_2=Q_3=\ldots$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $Q_1, Q_2, Q_3, \ldots$ are in AP with common difference 6**

**Detailed Solution:**

Since, $T_r=3 r^2+2 r-1$
$$
\begin{array}{rlrl} 
& \therefore & T_{r+1} & =3(r+1)^2+2(r+1)-1 \\
& \therefore & Q_r & =T_{r+1}-T_r=3[2 r+1]+2[1] \\
\Rightarrow & Q_r & =6 r+5 \\
\Rightarrow & Q_{r+1} & =6(r+1)+5
\end{array}
$$
Common difference $=Q_{r+1}-Q_r=6$

</details>

---

### Q10. JEE Advanced 2007 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Let $V_r$ denotes the sum of the first $r$ terms of an arithmetic progression $(A P)$ whose first term is $r$ and the common difference is $(2 r-1)$. Let $T_r=V_{r+1}-V_r-2$ and $Q_r=T_{r+1}-T_r$ for $r=1,2, \ldots$<strong>Question:</strong>
The sum $V_1+V_2+\ldots+V_n$ is

**Options:**

- **(A)** $\frac{1}{12} n(n+1)\left(3 n^2-n+1\right)$
- **(B)** $\frac{1}{12} n(n+1)\left(3 n^2+n+2\right)$
- **(C)** $\frac{1}{2} n\left(2 n^2-n+1\right)$
- **(D)** $\frac{1}{3}\left(2 n^3-2 n+3\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{12} n(n+1)\left(3 n^2+n+2\right)$**

**Detailed Solution:**

$$
\begin{aligned}
& V_r=\frac{r}{2}[2 r+(r-1)(2 r-1)]=\frac{1}{2}\left(2 r^3-r^2+r\right) \\
& \therefore \quad \Sigma V_r=\frac{1}{2}\left[2 \Sigma r^3-\Sigma r^2+\Sigma r\right] \\
& =\frac{1}{2}\left[2\left(\frac{n(n+1)}{2}\right)^2-\frac{n(n+1)(2 n+1)}{6}+\frac{n(n+1)}{2}\right] \\
& =\frac{1}{12} n(n+1)\left(3 n^2+n+2\right) \text {. } \\
&
\end{aligned}
$$

</details>

---

