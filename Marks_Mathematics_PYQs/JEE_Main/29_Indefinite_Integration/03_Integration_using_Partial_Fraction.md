# JEE Main Mathematics - Indefinite Integration

## Topic 3: Integration using Partial Fraction

**Total Questions:** 3

---

### Q1. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\int \frac{1}{x^{1 / 4}\left(1+x^{1 / 4}\right)} \mathrm{d} x, f(0)=-6$, then $f(1)$ is equal to :

**Options:**

- **(A)** $4\left(\log _e 2-2\right)$
- **(B)** $2-\log _{e^2} 2$
- **(C)** $\log _{\mathrm{e}} 2+2$
- **(D)** $4\left(\log _e 2+2\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4\left(\log _e 2-2\right)$**

**Detailed Solution:**

$\begin{aligned} & \text { Put } x^{1 / 4}=t \Rightarrow d x=4 t^3 d t \\ & \int \frac{4 t^3 d t}{t(t+1)}=4 \int\left(\frac{t^2-1}{t+1}+\frac{1}{t+1}\right) d t \\ & f(x)=4\left[\frac{x^{1 / 2}}{2}-x^{1 / 4}+\ln \left|x^{1 / 4}+1\right|\right]+C\end{aligned}$
$\begin{aligned} & f(0)=-6 \\ & \Rightarrow C=-6 \\ & \Rightarrow \quad f(1)=4\left(\log _e 2-2\right)\end{aligned}$

</details>

---

### Q2. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mo>&#8734;</mo></msubsup><mfrac><mn>6</mn><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>6</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>11</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>6</mn></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>32</mn><mn>27</mn></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>512</mn><mn>81</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>256</mn><mn>81</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>302</mn><mn>27</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>32</mn><mn>27</mn></mfrac></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mo>&#8734;</mo></msubsup><mfenced><mfrac><mn>6</mn><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>6</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>11</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>6</mn></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mo>&#8734;</mo></msubsup><mfrac><mn>6</mn><mrow><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Using partial fraction, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>6</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mo>&#8734;</mo></msubsup><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mrow><mn>2</mn><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>2</mn></mrow></mfenced></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>6</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mo>&#8734;</mo></msubsup><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mrow><mn>2</mn><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></mrow></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>6</mn><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>3</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mn>0</mn><mo>&#8734;</mo></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>6</mn><mfenced close="]" open="["><mrow><mn>0</mn><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>4</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>3</mn><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>-</mo><mn>3</mn><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>5</mn><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>-</mo><mn>3</mn><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>32</mn><mn>27</mn></mfrac></mfenced></math></p></blockquote>

</details>

---

### Q3. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>5</mn><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mn>6</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>17</mn><mo>-</mo><msub><mi>log</mi><mi mathvariant="normal">c</mi></msub><mn>19</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>17</mn><mo>-</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>18</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msub><mi>log</mi><mi mathvariant="normal">c</mi></msub><mn>19</mn><mo>-</mo><msub><mi>log</mi><mi mathvariant="normal">c</mi></msub><mn>17</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">c</mi></msub><mn>19</mn><mo>-</mo><msub><mi>log</mi><mi mathvariant="normal">c</mi></msub><mn>20</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>17</mn><mo>-</mo><msub><mi>log</mi><mi mathvariant="normal">c</mi></msub><mn>19</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>t</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mn>2</mn><mrow><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>t</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfenced><mrow><mfrac><mn>1</mn><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>t</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mi>ln</mi><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>ln</mi><mfenced><mrow><mi>t</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mi>ln</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>ln</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mi>ln</mi><mn>5</mn><mo>-</mo><mi>ln</mi><mn>6</mn></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mi>ln</mi><mn>10</mn><mo>-</mo><mi>ln</mi><mn>12</mn></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mi>ln</mi><mn>5</mn><mo>-</mo><mi>ln</mi><mn>6</mn></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mi>ln</mi><mn>2</mn><mo>+</mo><mi>ln</mi><mn>5</mn><mo>-</mo><mi>ln</mi><mn>2</mn><mo>-</mo><mi>ln</mi><mn>6</mn></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mi>ln</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>ln</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>ln</mi><mn>17</mn><mo>-</mo><mi>ln</mi><mn>19</mn></mrow></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>17</mn><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mn>19</mn></mrow></mfenced></math></p>

</details>

---

