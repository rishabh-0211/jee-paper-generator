# JEE Advanced Mathematics - Definite Integration

## Topic 7: Definite as Limit of Sum

**Total Questions:** 3

---

### Q1. JEE Advanced 2022 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

For positive integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>, define <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mi>n</mi><mo>+</mo><mfrac><mrow><mn>16</mn><mo>+</mo><mn>5</mn><mi>n</mi><mo>-</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>32</mn><mo>+</mo><mi>n</mi><mo>-</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mn>8</mn><mi>n</mi><mo>+</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>48</mn><mo>-</mo><mn>3</mn><mi>n</mi><mo>-</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mn>12</mn><mi>n</mi><mo>+</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mrow><mn>25</mn><mi>n</mi><mo>-</mo><mn>7</mn><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mn>7</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac></math>. Then, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>f</mi><mfenced><mi>n</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>7</mn><mn>3</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>7</mn><mn>3</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>7</mn><mn>3</mn></mfrac></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mi>n</mi><mo>+</mo><mfrac><mrow><mn>16</mn><mo>+</mo><mn>5</mn><mi>n</mi><mo>-</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>32</mn><mo>+</mo><mi>n</mi><mo>-</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mn>8</mn><mi>n</mi><mo>+</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><mrow><mn>25</mn><mi>n</mi><mo>-</mo><mn>7</mn><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mn>7</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mfrac><mrow><mn>16</mn><mo>+</mo><mn>5</mn><mi>n</mi><mo>-</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mrow><mn>32</mn><mo>+</mo><mi>n</mi><mo>-</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mn>8</mn><mi>n</mi><mo>+</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><mfrac><mrow><mn>25</mn><mi>n</mi><mo>-</mo><mn>7</mn><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mn>7</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mfrac><mrow><mn>9</mn><mi>n</mi><mo>+</mo><mn>16</mn></mrow><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>9</mn><mi>n</mi><mo>+</mo><mn>32</mn></mrow><mrow><mn>8</mn><mi>n</mi><mo>+</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mrow><mn>25</mn><mi>n</mi></mrow><mrow><mn>7</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mrow><mn>9</mn><mi>n</mi><mo>+</mo><mn>16</mn><mi>r</mi></mrow><mrow><mn>4</mn><mi>r</mi><mi>n</mi><mo>+</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mrow><mn>9</mn><mo>+</mo><mn>16</mn><mfenced><mfrac><mi>r</mi><mi>n</mi></mfrac></mfenced></mrow><mrow><mn>4</mn><mfenced><mfrac><mi>r</mi><mi>n</mi></mfrac></mfenced><mo>+</mo><mn>3</mn></mrow></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mn>9</mn><mo>+</mo><mn>16</mn><mi>x</mi></mrow><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mfenced><mrow><mn>16</mn><mi>x</mi><mo>+</mo><mn>12</mn></mrow></mfenced><mo>-</mo><mn>3</mn></mrow><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="|" open=""><mfenced><mrow><mn>4</mn><mi>x</mi><mo>&#8722;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mi>ln</mi><mfenced close="|" open="|"><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfenced></mfenced><mn>0</mn><mn>1</mn></msubsup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mi>ln</mi><mfrac><mn>7</mn><mn>3</mn></mfrac></math></p></blockquote>

</details>

---

### Q2. JEE Advanced 2013 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

<p>For <math> <mrow> <mtext>a</mtext> <mo>&#8712;</mo> <mtext>R</mtext> </mrow> </math> (the set of all real numbers), <math> <mrow> <mtext>a</mtext> <mo>&#8800;</mo> <mo>-</mo> <mn>1</mn> </mrow> </math>, <math> <mrow> <munder> <mtext>lim</mtext> <mrow> <mtext>n</mtext> <mo>&#8594;</mo> <mo>&#8734;</mo> </mrow> </munder> <mfrac> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mn>1</mn> <mtext>a</mtext> </msup> <mo>+</mo> <msup> <mn>2</mn> <mtext>a</mtext> </msup> <mo>+</mo> <mo>&#8230;</mo> <mo>+</mo> <msup> <mtext>n</mtext> <mtext>a</mtext> </msup> </mrow> </mfenced> </mrow> <mrow> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mtext>n</mtext> <mo>+</mo> <mn>1</mn> </mrow> </mfenced> </mrow> <mrow> <mtext>a</mtext> <mo>-</mo> <mn>1</mn> </mrow> </msup> <mfenced close="]" open="[" separators=","> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mtext>na</mtext> <mo>+</mo> <mn>1</mn> </mrow> </mfenced> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mtext>na</mtext> <mo>+</mo> <mn>2</mn> </mrow> </mfenced> <mo>+</mo> <mo>&#8230;</mo><mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mtext>na</mtext> <mo>+</mo> <mtext>n</mtext> </mrow> </mfenced> </mrow> </mfenced> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>6</mn> <mn>0</mn> </mrow> </mfrac> </mrow> </math> Then a =</p>

**Options:**

- **(A)** 5
- **(B)** 7
- **(C)** <math> <mrow> <mfrac> <mrow> <mo>-</mo> <mn>1</mn> <mn>5</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mo>-</mo> <mn>1</mn> <mn>7</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mrow> <mfrac> <mrow> <mo>-</mo> <mn>1</mn> <mn>7</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<p>This numerical can be solved by using the concept of Definite integral as limit of sum.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mtext>Lim</mtext><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mstyle displaystyle="true"><munderover><mrow><mo>&#8721;</mo><msup><mi>r</mi><mi>a</mi></msup></mrow><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover></mstyle><mrow><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mrow><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mo>(</mo><mi>n</mi><mi>a</mi><mo>+</mo><mi>r</mi><mo>)</mo></mrow></mfenced></mrow></mfrac></math></p><p>Divide Numerator and Denominator by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mi>a</mi></msup></math> and rearranging the terms</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mtext>Lim</mtext><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mfenced><mfrac><mi>r</mi><mi>n</mi></mfrac></mfenced><mi>a</mi></msup></mstyle><mstyle displaystyle="true"><mfenced><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mfenced close="]" open="["><mrow><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfenced><mrow><mi>a</mi><mo>+</mo><mfrac><mi>r</mi><mi>n</mi></mfrac></mrow></mfenced></mrow></mfenced></mstyle></mfrac></math></p><p>Now Multiply Numerator and denominator by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mtext>Lim</mtext><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mfenced><mfrac><mi>r</mi><mi>n</mi></mfrac></mfenced><mi>a</mi></msup><mo>&#215;</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle><mstyle displaystyle="true"><mfenced><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mfenced close="]" open="["><mrow><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfenced><mrow><mi>a</mi><mo>+</mo><mfrac><mi>r</mi><mi>n</mi></mfrac></mrow></mfenced></mrow></mfenced><mo>&#215;</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></mfrac></math></p><p>Now Replace <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>n</mi></mfrac></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mi>n</mi></mfrac></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and the lower limit and upper limit will be <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>,</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mi>n</mi><mi>n</mi></mfrac><mo>=</mo><mn>1</mn></math>,and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow></mrow><mrow></mrow></munderover></math> will be replaced by <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow></mrow><mrow></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msubsup><mo>&#8747;</mo><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><mn>1</mn></msubsup><msup><mi>x</mi><mi>a</mi></msup><mo>d</mo><mi>x</mi></mrow><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>x</mi></mrow></mfenced><mo>d</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac><mspace linebreak="newline"></mspace><mfrac><mstyle displaystyle="true"><msubsup><mfenced close="]" open="["><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></msup><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mstyle></mfenced><mn>0</mn><mn>1</mn></msubsup></mstyle><mstyle displaystyle="true"><msubsup><mfenced close="]" open="["><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mstyle></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></mstyle></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac><mspace linebreak="newline"></mspace><mfrac><mstyle displaystyle="true"><mfrac><mn>1</mn><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mn>0</mn></mstyle><mrow><mi>a</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle><mo>-</mo><mn>0</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac><mspace linebreak="newline"></mspace><mfrac><mn>2</mn><mrow><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mstyle displaystyle="true"><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mstyle></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac><mspace linebreak="newline"></mspace><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>120</mn><mspace linebreak="newline"></mspace><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>a</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>120</mn><mspace linebreak="newline"></mspace><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>a</mi><mo>-</mo><mn>119</mn><mo>=</mo><mn>0</mn><mspace linebreak="newline"></mspace><mi>a</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mo>&#177;</mo><msqrt><mn>9</mn><mo>+</mo><mn>8</mn><mo>&#215;</mo><mn>119</mn></msqrt></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>2</mn></mrow></mfrac><mspace linebreak="newline"></mspace><mi>a</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mo>&#177;</mo><mn>31</mn></mrow><mn>4</mn></mfrac><mspace linebreak="newline"></mspace><mi>a</mi><mo>=</mo><mfrac><mn>28</mn><mn>4</mn></mfrac><mo>&#160;</mo><mi>o</mi><mi>r</mi><mo>&#160;</mo><mo>-</mo><mfrac><mn>34</mn><mn>4</mn></mfrac><mspace linebreak="newline"></mspace><mi>a</mi><mo>=</mo><mn>7</mn><mo>&#160;</mo><mi>o</mi><mi>r</mi><mo>&#160;</mo><mo>-</mo><mfrac><mn>17</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q3. JEE Advanced 2008 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let $S_n=\sum_{k=0}^n \frac{n}{n^2+k n+k^2}$ and $T_n=\sum_{k=0}^{n-1} \frac{n}{n^2+k n+k^2}$, for $n=1,2,3, \ldots$, then

**Options:**

- **(A)** $S_n < \frac{\pi}{3 \sqrt{3}}$
- **(B)** $S_n>\frac{\pi}{3 \sqrt{3}}$
- **(C)** $T_n < \frac{\pi}{3 \sqrt{3}}$
- **(D)** $T_n>\frac{\pi}{3 \sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $T_n>\frac{\pi}{3 \sqrt{3}}$**

**Detailed Solution:**

Given,
$$
\begin{aligned}
S_n & =\sum_{k=0}^n \frac{n}{n^2+k n+k^2} \\
& =\sum_{k=0}^n \frac{1}{n} \cdot\left(\frac{1}{1+\frac{k}{n}+\frac{k^2}{n^2}}\right) < \lim _{n \rightarrow \infty} \sum_{k=0}^n \frac{1}{n}\left(\frac{1}{1+\frac{k}{n}+\left(\frac{k}{n}\right)^2}\right) \\
& =\int_0^1 \frac{1}{1+x+x^2} d x=\left[\frac{2}{\sqrt{3}} \tan ^{-1}\left(\frac{2}{\sqrt{3}}\left(x+\frac{1}{2}\right)\right)\right]_0^1 \\
& =\frac{2}{\sqrt{3}} \cdot\left(\frac{\pi}{3}-\frac{\pi}{6}\right)=\frac{\pi}{3 \sqrt{3}}
\end{aligned}
$$
i.e., $\quad S_n < \frac{\pi}{3 \sqrt{3}}$
Similarly, $T_n>\frac{\pi}{3 \sqrt{3}}$.

</details>

---

