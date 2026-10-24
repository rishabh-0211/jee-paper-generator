# JEE Main Mathematics - Definite Integration

## Topic 1: Definite Integration by Parts

**Total Questions:** 18

---

### Q1. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int_{0}^{1}\cot^{-1}(1+x+x^2)dx$ is equal to:

**Options:**

- **(A)** $2\tan^{-1}2+\dfrac{1}{2}\log_e\left(\dfrac{5}{4}\right)+\dfrac{\pi}{2}$
- **(B)** $2\tan^{-1}2+\dfrac{1}{2}\log_e\left(\dfrac{5}{4}\right)-\dfrac{\pi}{2}$
- **(C)** $2\tan^{-1}2-\dfrac{1}{2}\log_e\left(\dfrac{5}{4}\right)+\dfrac{\pi}{2}$
- **(D)** $2\tan^{-1}2-\dfrac{1}{2}\log_e\left(\dfrac{5}{4}\right)-\dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2\tan^{-1}2-\dfrac{1}{2}\log_e\left(\dfrac{5}{4}\right)-\dfrac{\pi}{2}$**

**Detailed Solution:**

$I = \int_{0}^{1}\cot^{-1}(1+x+x^2)dx$

$I = \int_{0}^{1}\tan^{-1}\left(\dfrac{1}{1+x+x^2}\right)dx$

$I = \int_{0}^{1}\tan^{-1}\left(\dfrac{(x+1)-x}{1+(x+1)x}\right)dx$

$I = \int_{0}^{1}(\tan^{-1}(x+1)-\tan^{-1}x)dx$

$I = \int_{0}^{1}\tan^{-1}(x+1)dx - \int_{0}^{1}\tan^{-1}x dx$

Substituting $x+1 = t$ in the first integral:

$I = \int_{1}^{2}\tan^{-1}x dx - \int_{0}^{1}\tan^{-1}x dx$

Using integration by parts, $\int \tan^{-1}x dx = x\tan^{-1}x - \dfrac{1}{2}\log_e(1+x^2)$

$I = \left[x\tan^{-1}x - \dfrac{1}{2}\log_e(1+x^2)\right]_{1}^{2} - \left[x\tan^{-1}x - \dfrac{1}{2}\log_e(1+x^2)\right]_{0}^{1}$

$I = \left(2\tan^{-1}2 - \dfrac{1}{2}\log_e 5 - \left(\dfrac{\pi}{4} - \dfrac{1}{2}\log_e 2\right)\right) - \left(\dfrac{\pi}{4} - \dfrac{1}{2}\log_e 2 - 0\right)$

$I = 2\tan^{-1}2 - \dfrac{1}{2}\log_e 5 - \dfrac{\pi}{2} + \log_e 2$

$I = 2\tan^{-1}2 - \dfrac{1}{2}\log_e 5 + \dfrac{1}{2}\log_e 4 - \dfrac{\pi}{2}$

$I = 2\tan^{-1}2 - \dfrac{1}{2}\log_e\left(\dfrac{5}{4}\right) - \dfrac{\pi}{2}$

Answer: $2\tan^{-1}2-\dfrac{1}{2}\log_e\left(\dfrac{5}{4}\right)-\dfrac{\pi}{2}$

</details>

---

### Q2. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int\left(\frac{1-5 \cos ^{2} x}{\sin ^{5} x \cos ^{2} x}\right) d x=f(x)+\mathrm{C}$, where C is the constant of integration, then $f\left(\frac{\pi}{6}\right)-f\left(\frac{\pi}{4}\right)$ is equal to

**Options:**

- **(A)** $\frac{1}{\sqrt{3}}(26+\sqrt{3})$
- **(B)** $\frac{1}{\sqrt{3}}(26-\sqrt{3})$
- **(C)** $\frac{4}{\sqrt{3}}(8-\sqrt{6})$
- **(D)** $\frac{2}{\sqrt{3}}(4+\sqrt{6})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4}{\sqrt{3}}(8-\sqrt{6})$**

**Detailed Solution:**

$\int \frac{1 - 5\cos^2 x}{\sin^5 x \cos^2 x} dx = \int \frac{dx}{\sin^5 x \cos^2 x} - 5\int \frac{dx}{\sin^5 x}$

$= \int \frac{\sec^2 x \, dx}{\sin^5 x} - 5\int \frac{dx}{\sin^5 x}$

By IBP:
$= \frac{\tan x}{\sin^5 x} - \int \left(-\frac{5}{\sin^6 x}\right) \cos x \cdot \tan x \, dx - 5\int \frac{dx}{\sin^5 x}$

$= \frac{\tan x}{\sin^5 x} + C$

So $f(x) = \frac{\tan x}{\sin^5 x}$

$f\left(\frac{\pi}{6}\right) - f\left(\frac{\pi}{4}\right) = \frac{2^5}{\sqrt{3}} - (\sqrt{2})^5 = \frac{32}{\sqrt{3}} - 4\sqrt{2} = \frac{4}{\sqrt{3}}(8 - \sqrt{6})$

</details>

---

### Q3. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}: \mathbf{R} \rightarrow \mathbf{R}$ be a twice differentiable function such that $f(2)=1$. If $\mathrm{F}(x)=x f(x)$ for all $x \in \mathbf{R}$, $\int_0^2 x \mathrm{~F}^{\prime}(x) \mathrm{d} x=6$ and $\int_0^2 x^2 \mathrm{~F}^{\prime \prime}(x) \mathrm{d} x=40$, then $\mathrm{F}^{\prime}(2)+\int_0^2 \mathrm{~F}(x) \mathrm{d} x$ is equal to :

**Options:**

- **(A)** $11$
- **(B)** $13$
- **(C)** $15$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $11$**

**Detailed Solution:**

$\begin{aligned}
& \int_0^2 \mathrm{xF}^{\prime}(\mathrm{x}) \mathrm{dx}=6 \\
& =\left.\mathrm{xF}(\mathrm{x})\right|_0 ^2-\int_0^2 \mathrm{f}(\mathrm{x}) \mathrm{dx}=6 \\
& =2 \mathrm{~F}(2)-\int_0^2 \mathrm{xF}(\mathrm{x}) \mathrm{dx}=6[\therefore \mathrm{f}(2)=2 \mathrm{~F}(2)=2] \\
& \int_0^2 \mathrm{xF}(\mathrm{x}) \mathrm{dx}=-2 ...(1)\\
& \Rightarrow \int_0^2 \mathrm{~F}(\mathrm{x}) \mathrm{dx}=-2 ...(2)
\end{aligned}$

Also
$\int_0^2 x^2 F^{\prime \prime}(x) d x=\left.x^2 F^{\prime}(x)\right|_0 ^2-2 \int_0^2 x^{\prime} F^{\prime}(x) d x=40$
$\begin{aligned} & =4 F^{\prime}(2)-2 \times 6=40 \\ & F^{\prime}(2)=13 \\ & \therefore F^{\prime}(2)+\int_0^2 F(x)=13-2=11\end{aligned}$

</details>

---

### Q4. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be a thrice differentiable function in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>5</mn><mo>,</mo><mn>5</mn><mo>)</mo></math>. Let the tangents to the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mi mathvariant="normal">f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>,</mo><mi mathvariant="normal">f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>)</mo></math> make angles <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mn>6</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mn>4</mn></mfrac></math>, respectively with positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi></math>-axis. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><msubsup><mo>∫</mo><mn>1</mn><mn>3</mn></msubsup><mfenced><mrow><msup><mfenced><mrow><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>t</mi></mfenced></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>f</mi><mo>"</mo></msup><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mi>α</mi><mo>+</mo><mi>β</mi><msqrt><mn>3</mn></msqrt><mo>  </mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mo> </mo><mi>β</mi></math> are integers, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mi>β</mi></math> equals

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>14</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>16</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn></math>**

**Detailed Solution:**

<blockquote><p>Given: </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mfenced><mrow><mn>1</mn><mo>,</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced></msub><mo>=</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>tan</mi><mfrac><mi>π</mi><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mfrac><mi>dy</mi><mi>dx</mi></mfrac></mfenced><mfenced><mrow><mn>3</mn><mo>,</mo><mi mathvariant="normal">f</mi><mfenced><mn>3</mn></mfenced></mrow></mfenced></msub><mo>=</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>3</mn></mfenced><mo>=</mo><mi>tan</mi><mfrac><mi>π</mi><mn>4</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>1</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>It is given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><msubsup><mo>∫</mo><mn>1</mn><mn>3</mn></msubsup><mfenced><mrow><msup><mfenced><mrow><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>t</mi></mfenced></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>f</mi><mo>"</mo></msup><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mi>α</mi><mo>+</mo><mi>β</mi><msqrt><mn>3</mn></msqrt></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mn>1</mn><mn>3</mn></msubsup><mfenced><mrow><msup><mfenced><mrow><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>f</mi><mo>"</mo></msup><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>z</mi><mo>⇒</mo><msup><mi>f</mi><mo>"</mo></msup><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mi>d</mi><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><msubsup><mo>∫</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mn>1</mn></msubsup><mfenced><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><msubsup><mfenced><mrow><mfrac><msup><mi>z</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mi>z</mi></mrow></mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>·</mo><mfrac><mn>1</mn><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>10</mn><mrow><mn>9</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>10</mn><mn>27</mn></mfrac><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mi>β</mi><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>27</mn><mfenced><mrow><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>10</mn><mn>27</mn></mfrac><msqrt><mn>3</mn></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mi>β</mi><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>36</mn><mo>-</mo><mn>10</mn><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>36</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mo>-</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mi>β</mi><mo>=</mo><mn>36</mn><mo>-</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mi>β</mi><mo>=</mo><mn>26</mn></math></p></blockquote>

</details>

---

### Q5. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>,</mo><mo> </mo><mi>b</mi><mo>)</mo></math> be the orthocentre of the triangle whose vertices are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>,</mo><mn>1</mn><mo>)</mo></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mi mathvariant="normal">a</mi><mi mathvariant="normal">b</mi></msubsup><mi>xsin</mi><mfenced><mrow><mn>4</mn><mi mathvariant="normal">x</mi><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced><mi>dx</mi><mo>,</mo><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mi mathvariant="normal">a</mi><mi mathvariant="normal">b</mi></msubsup><mi>sin</mi><mfenced><mrow><mn>4</mn><mi mathvariant="normal">x</mi><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced><mi>dx</mi></math> , then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn><mfrac><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mfrac></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>88</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>66</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>**

**Detailed Solution:**

<p>Equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>CE</mi></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mstyle displaystyle="true"><mfrac><mrow><mn>3</mn><mo>-</mo><mn>2</mn></mrow><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfrac></mstyle></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>4</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Similarly, equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mstyle displaystyle="true"><mfrac><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mo>-</mo><mn>3</mn></mrow></mfrac></mstyle></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>4</mn><mo>=</mo><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mo>-</mo><mi>y</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>4</mn><mo>-</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></p><p>So, Orthocentre is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi><mo>≡</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>,</mo><mfrac><mn>7</mn><mn>3</mn></mfrac></mrow></mfenced></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0fa5deeb-0b17-4bc6-bc8e-7dd1df3d7619.png" style="width: 275px; height: 200px;"/></p><p>Orthocentre lies on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>4</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>4</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mi>a</mi><mi>b</mi></msubsup><mi>x</mi><mi>sin</mi><mo>(</mo><mi>x</mi><mo>(</mo><mn>4</mn><mo>-</mo><mi>x</mi><mo>)</mo><mo>)</mo><mi>d</mi><mi>x</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mi>a</mi><mi>b</mi></msubsup><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi><mo>)</mo><mi>sin</mi><mo>(</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>(</mo><mn>4</mn><mo>-</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>)</mo><mo>)</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mi>a</mi><mi>b</mi></msubsup><mo>(</mo><mn>4</mn><mo>-</mo><mi>x</mi><mo>)</mo><mi>sin</mi><mo>(</mo><mi>x</mi><mo>(</mo><mn>4</mn><mo>-</mo><mi>x</mi><mo>)</mo><mo>)</mo><mi>d</mi><mi>x</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>Using, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo><mo> </mo><mo>+</mo><mo> </mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>∫</mo><mi>a</mi><mi>b</mi></msubsup><mn>4</mn><mi>sin</mi><mo>(</mo><mi>x</mi><mo>(</mo><mn>4</mn><mo>-</mo><mi>x</mi><mo>)</mo><mo>)</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msub><mi mathvariant="normal">I</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">I</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>36</mn><msub><mi>I</mi><mn>1</mn></msub></mrow><msub><mi>I</mi><mn>2</mn></msub></mfrac><mo>=</mo><mn>72</mn></math></p>

</details>

---

### Q6. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>e</mi><mrow><mo>-</mo><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></mrow></msup><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>tan</mi><msup><mo>&#160;</mo><mn>50</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></mrow><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>(</mo><msup><mi>tan</mi><mn>49</mn></msup><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mn>51</mn></msup><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi></mrow></mfrac></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>51</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>**

**Detailed Solution:**

<blockquote><p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><msup><mi>e</mi><mrow><mo>-</mo><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></mrow></msup><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>tan</mi><msup><mo>&#160;</mo><mn>50</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></mrow><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mfenced><mrow><msup><mi>tan</mi><mn>49</mn></msup><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mn>51</mn></msup><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>(</mo><msup><mi>tan</mi><mn>49</mn></msup><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mn>51</mn></msup><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi></math></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><msup><mi>tan</mi><mn>50</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></math> using byparts we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><msup><mi>tan</mi><mn>50</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><msup><mi>tan</mi><mn>50</mn></msup><mi>x</mi></mrow></mfenced><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mn>50</mn><msup><mi>tan</mi><mn>49</mn></msup><mi>x</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></msup><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mn>50</mn><msup><mi>tan</mi><mn>49</mn></msup><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></msup><mo>+</mo><mn>50</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfenced><mrow><msup><mi>tan</mi><mn>49</mn></msup><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mn>51</mn></msup><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></msup><mo>+</mo><mn>50</mn><msub><mi>I</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><msup><mi>tan</mi><mn>50</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></msup><mo>=</mo><mn>50</mn><msub><mi>I</mi><mn>1</mn></msub></math></p><p>Now putting the given integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><msup><mi>e</mi><mrow><mo>-</mo><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></mrow></msup><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>tan</mi><msup><mo>&#160;</mo><mn>50</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></mrow><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></msubsup><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mfenced><mrow><msup><mi>tan</mi><mn>49</mn></msup><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mn>51</mn></msup><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mrow><mn>50</mn><msub><mi>I</mi><mn>1</mn></msub></mrow><msub><mi>I</mi><mpadded voffset="+1px"><mn>1</mn></mpadded></msub></mfrac><mo>=</mo><mn>50</mn></math></p></blockquote>

</details>

---

### Q7. JEE Main 2023 (11 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#62;</mo><mn>0</mn></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mfenced><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><msup><mi>t</mi><mi>m</mi></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>t</mi></mrow></mfenced><mi>n</mi></msup><mi>d</mi><mi>t</mi></math>. If ,<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mi>&#945;</mi><mfenced><mrow><mn>10</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mn>18</mn><mi>&#945;</mi><mfenced><mrow><mn>11</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mi>p</mi><msup><mfenced><mn>14</mn></mfenced><mn>6</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **32**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mfenced><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><msup><mi>t</mi><mi>m</mi></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>t</mi></mrow></mfenced><mi>n</mi></msup><mi>d</mi><mi>t</mi></math></p><p>Now using integration by parts we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mfenced><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></mfenced><mo>=</mo><msubsup><mfenced open="" close="|"><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>t</mi></mrow></mfenced><mi>n</mi></msup><mo>&#8901;</mo><mfrac><msup><mi>t</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msup><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mn>0</mn><mn>2</mn></msubsup><mo>&#8722;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>n</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>t</mi></mrow></mfenced><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></msup><mo>&#215;</mo><mn>3</mn><mo>&#8901;</mo><mfrac><msup><mi>t</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msup><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#945;</mi><mfenced><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></mfenced><mo>=</mo><msubsup><mfenced open="" close="|"><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>t</mi></mrow></mfenced><mi>n</mi></msup><mo>&#8901;</mo><mfenced><msup><mi>t</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msup></mfenced></mrow></mfenced><mn>0</mn><mn>2</mn></msubsup><mo>&#8722;</mo><mn>3</mn><mi>n</mi><mfenced><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>t</mi></mrow></mfenced><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></msup><mo>&#215;</mo><msup><mi>t</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#945;</mi><mfenced><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></mfenced><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn></mrow></mfenced><mi>n</mi></msup><mo>&#8901;</mo><mfenced><msup><mn>2</mn><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msup></mfenced><mo>&#8722;</mo><mn>3</mn><mi>n</mi><mfenced><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#945;</mi><mfenced><mrow><mi>m</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#945;</mi><mfenced><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></mfenced><mo>=</mo><msup><mn>7</mn><mi>n</mi></msup><mo>&#183;</mo><msup><mn>2</mn><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>n</mi><mi>&#945;</mi><mfenced><mrow><mi>m</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#945;</mi><mfenced><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mi>n</mi><mi>&#945;</mi><mfenced><mrow><mi>m</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mn>7</mn><mi>n</mi></msup><mo>&#183;</mo><msup><mn>2</mn><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msup></math></p><p>Now put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>6</mn></math> in above equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mi>&#945;</mi><mfenced><mrow><mn>10</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mn>18</mn><mi>&#945;</mi><mfenced><mrow><mn>11</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>=</mo><msup><mn>7</mn><mn>6</mn></msup><mo>&#183;</mo><msup><mn>2</mn><mn>11</mn></msup><mo>=</mo><mn>32</mn><mo>&#215;</mo><msup><mfenced><mn>14</mn></mfenced><mn>6</mn></msup></math></p><p>Hence, on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mi>&#945;</mi><mfenced><mrow><mn>10</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mn>18</mn><mi>&#945;</mi><mfenced><mrow><mn>11</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mi>p</mi><mo>&#215;</mo><msup><mfenced><mn>14</mn></mfenced><mn>6</mn></msup></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mn>32</mn></math></p>

</details>

---

### Q8. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></msubsup><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></msqrt></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>(</mo><mn>2</mn><mo>+</mo><msqrt><mn>5</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></msqrt></mfrac></mfenced><mo>-</mo><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mo>(</mo><mn>2</mn><mo>+</mo><msqrt><mn>5</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></msqrt></mfrac></mfenced><mo>+</mo><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>2</mn><mo>(</mo><mn>2</mn><mo>+</mo><msqrt><mn>5</mn></msqrt><mo>)</mo></mrow><msqrt><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></msqrt></mfrac></mfenced><mo>-</mo><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>(</mo><mn>3</mn><mo>-</mo><msqrt><mn>5</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></msqrt></mfrac></mfenced><mo>+</mo><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>(</mo><mn>2</mn><mo>+</mo><msqrt><mn>5</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></msqrt></mfrac></mfenced><mo>-</mo><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></msubsup><msup><mi>e</mi><mi>x</mi></msup><mfenced close="]" open="["><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></msqrt></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Let us substitute <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p>Lower limit <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>2</mn></mfenced></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Upper limit <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>2</mn></mfenced></mrow></msup><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>2</mn></msubsup><mn>1</mn><mo>&#215;</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced close="]" open="["><mrow><mi>t</mi><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></msqrt></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p>Apply integration by-parts.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi>u</mi><mfenced><mi>t</mi></mfenced><mi>v</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mi>u</mi><mfenced><mi>t</mi></mfenced><mo>&#8747;</mo><mi>v</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>-</mo><mo>&#8747;</mo><mfenced><mrow><mi>u</mi><mo>&#39;</mo><mfenced><mi>t</mi></mfenced><mo>&#8747;</mo><mi>v</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p>Take <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced close="]" open="["><mrow><mi>t</mi><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></msqrt></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>v</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>u</mi><mo>&#39;</mo><mfenced><mi>t</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mi>t</mi><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></msqrt></mrow></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>2</mn><mi>t</mi></mrow><mrow><mn>2</mn><msqrt><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></msqrt></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mi>t</mi><mi>ln</mi><mfenced><mrow><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>2</mn></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow><mn>2</mn></msubsup><mfrac><mi>t</mi><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mi>t</mi><mi>ln</mi><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mi>t</mi><mo>-</mo><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="[" close="]"><mrow><mn>2</mn><mi>ln</mi><mfenced><mrow><msqrt><mn>5</mn></msqrt><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow></mfenced><mo>-</mo><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mrow><msqrt><mfrac><mn>5</mn><mn>2</mn></mfrac></msqrt><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><msqrt><mfrac><mn>5</mn><mn>2</mn></mfrac></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>ln</mi><mfenced><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>(</mo><mn>2</mn><mo>+</mo><msqrt><mn>5</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></msqrt></mfrac></mfenced><mo>-</mo><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q9. JEE Main 2023 (25 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mn>3</mn></msubsup><mfenced open="|" close="|"><mrow><msub><mi>log</mi><mi>e</mi></msub><mi mathvariant="normal">x</mi></mrow></mfenced><mi>dx</mi><mo>=</mo><mfrac><mi mathvariant="normal">m</mi><mi mathvariant="normal">n</mi></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><msup><mi mathvariant="normal">n</mi><mn>2</mn></msup><mi mathvariant="normal">e</mi></mfrac></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi></math> are coprime natural numbers, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">n</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mn>3</mn></msubsup><mfenced close="|" open="|"><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mn>1</mn></msubsup><mfenced open="|" close="|"><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>3</mn></msubsup><mfenced open="|" close="|"><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><msubsup><mo>&#8747;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mn>1</mn></msubsup><mi>ln</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>3</mn></msubsup><mi>ln</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mi>x</mi><mo>&#60;</mo><mn>0</mn><mo>&#160;</mo><mi>for</mi><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><msubsup><mfenced close="]" open="["><mrow><mi>x</mi><mi>ln</mi><mi>x</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac><mn>1</mn></msubsup><mo>+</mo><msubsup><mfenced close="]" open="["><mrow><mi>x</mi><mi>ln</mi><mi>x</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>1</mn><mn>3</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mn>0</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>ln</mi><mn>3</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>3</mn><mi>ln</mi><mn>3</mn><mo>-</mo><mn>3</mn><mo>-</mo><mfenced><mrow><mn>0</mn><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>ln</mi><mn>3</mn><mo>+</mo><mn>3</mn><mi>ln</mi><mn>3</mn><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mi>ln</mi><mn>3</mn><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mfenced><mrow><mn>2</mn><mi>ln</mi><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mfenced><mrow><mi>ln</mi><msup><mn>3</mn><mn>2</mn></msup><mo>-</mo><mi>ln</mi><mi>e</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>ln</mi><mfenced><mfrac><msup><mn>3</mn><mn>2</mn></msup><mi>e</mi></mfrac></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mo>=</mo><mn>16</mn><mo>+</mo><mn>9</mn><mo>-</mo><mn>5</mn><mo>=</mo><mn>20</mn></math></p>

</details>

---

### Q10. JEE Main 2022 (28 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><mn>1</mn><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup></mfrac><mi>d</mi><mi>t</mi><mo>,</mo><mi>n</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo></math> Then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><msub><mi>I</mi><mn>6</mn></msub><mo>-</mo><mn>9</mn><msub><mi>I</mi><mn>5</mn></msub><mo>=</mo><mi>x</mi><msubsup><mi>I</mi><mn>5</mn><mo>'</mo></msubsup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><msub><mi>I</mi><mn>6</mn></msub><mo>-</mo><mn>11</mn><msub><mi>I</mi><mn>5</mn></msub><mo>=</mo><mi>x</mi><msubsup><mi>I</mi><mn>5</mn><mo>'</mo></msubsup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><msub><mi>I</mi><mn>6</mn></msub><mo>-</mo><mn>9</mn><msub><mi>I</mi><mn>5</mn></msub><mo>=</mo><msubsup><mi>I</mi><mn>5</mn><mo>'</mo></msubsup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><msub><mi>I</mi><mn>6</mn></msub><mo>-</mo><mn>11</mn><msub><mi>I</mi><mn>5</mn></msub><mo>=</mo><msubsup><mi>I</mi><mn>5</mn><mo>'</mo></msubsup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><msub><mi>I</mi><mn>6</mn></msub><mo>-</mo><mn>9</mn><msub><mi>I</mi><mn>5</mn></msub><mo>=</mo><mi>x</mi><msubsup><mi>I</mi><mn>5</mn><mo>'</mo></msubsup></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup></mfrac></math></p><p>Applying integration by parts we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mfenced close="]" open="["><mfrac><mi>t</mi><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup></mfrac></mfenced><mn>0</mn><mi>x</mi></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>n</mi><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mrow><mo>-</mo><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>&#183;</mo><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup></mfrac><mo>+</mo><mn>2</mn><mi>n</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><msup><mi>t</mi><mn>2</mn></msup><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup></mfrac><mo>+</mo><mn>2</mn><mi>n</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><mrow><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mn>5</mn></mrow><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup></mfrac><mo>+</mo><mn>2</mn><mi>n</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup></mfrac><mo>-</mo><mn>10</mn><mi>n</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup></mfrac><mo>+</mo><mn>2</mn><mi>n</mi><msub><mi>I</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>10</mn><mi>n</mi><msub><mi>I</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mi>n</mi><msub><mi>I</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mfenced><mi>x</mi></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>n</mi></mrow></mfenced><msub><mi>I</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mi>n</mi><msub><mi>I</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mfenced><mi>x</mi></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>n</mi></mrow></mfenced><msub><mi>I</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><msub><msup><mi>I</mi><mo>&#39;</mo></msup><mi>n</mi></msub></math> {where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><msup><mi>I</mi><mo>&#39;</mo></msup><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup></mfrac></math> we get by differentiating <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup></mfrac></math> }</p><p>Now put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>5</mn></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><msub><mi>I</mi><mn>6</mn></msub><mo>-</mo><mn>9</mn><msub><mi>I</mi><mn>5</mn></msub><mo>=</mo><mi>x</mi><msubsup><mi>I</mi><mn>5</mn><mo>&#39;</mo></msubsup></math></p></blockquote>

</details>

---

### Q11. JEE Main 2022 (26 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mrow><mn>2</mn><mi>n</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mn>1177</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>x</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **24**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mrow><mn>2</mn><mi>n</mi></mrow></msup><mi>d</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>x</mi></math></p><p>Now on solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>&#183;</mo><mn>1</mn><mi>d</mi><mi>x</mi></math></p><p>Now on using by parts integration we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>.</mo><msubsup><menclose notation="right"><mi>x</mi></menclose><mn>0</mn><mn>1</mn></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mrow><mn>2</mn><mi>n</mi></mrow></msup><mfenced><mrow><mo>-</mo><mi>n</mi><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced close="}" open="{"><mrow><msub><mi>I</mi><mn>2</mn></msub><mo>-</mo><msub><mi>I</mi><mn>1</mn></msub></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as&#160;</mtext><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mrow><mn>2</mn><mi>n</mi></mrow></msup><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msub><mi>I</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>Given&#160;</mtext><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mrow><mn>2</mn><mi>n</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mn>1177</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1177</mn><mrow><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi><mo>-</mo><mn>1176</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>1</mn><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1176</mn></msqrt></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>9409</mn></msqrt></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><mn>97</mn></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>24</mn><mo>&#160;</mo><mi>o</mi><mi>r</mi><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mn>49</mn></mrow><mn>2</mn></mfrac></math></p><p>But given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math> so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>24</mn></math></p></blockquote>

</details>

---

### Q12. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="bold-italic">R</mi><mo>&#8594;</mo><mi mathvariant="bold-italic">R</mi></math> be a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mi>f</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>1</mn></math> and let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mi>x</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfenced><mrow><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>t</mi></mfenced><mi>sec</mi><mi>t</mi><mo>+</mo><mi>tan</mi><mi>t</mi><mi>sec</mi><mi>t</mi><mi>f</mi><mfenced><mi>t</mi></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>-</mo></msup></mrow></munder><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mi>x</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mfenced><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>t</mi></mfenced><mi>sec</mi><mi>t</mi><mo>+</mo><mi>tan</mi><mi>t</mi><mi>sec</mi><mi>t</mi><mi>f</mi><mfenced><mi>t</mi></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mi>x</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup><mi>d</mi><mfenced><mrow><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>&#183;</mo><mi>sec</mi><mi>t</mi></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mfenced open="[" close="]"><mrow><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>sec</mi><mi>t</mi></mrow></mfenced><mi>x</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mi>sec</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><mi>sec</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>sec</mi><mi>x</mi><mo>=</mo><mn>2</mn><mo>-</mo><mfenced><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac></mfenced></math></p><p>Now taking limit both side, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>-</mo></msup></mrow></munder><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mo>-</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>-</mo></msup></mrow></munder><mfenced><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac></mfenced></math></p><p>Using L&#39;Hospital Rule</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>-</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>-</mo></msup></mrow></munder><mfrac><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow><mfenced><mrow><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced></mrow><mrow><mi>sin</mi><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfrac><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>1</mn></mfrac><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q13. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>1</mn></msubsup><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

Let<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>1</mn></msubsup><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><munder><munder><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt></mrow></mfenced></mrow><mo>&#9183;</mo></munder><mi>I</mi></munder><mo>&#183;</mo><munder><munder><mn>1</mn><mo>&#9183;</mo></munder><mrow><mi>I</mi><mi>I</mi></mrow></munder><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><mfenced open="[" close="]"><mrow><msubsup><mfenced><mrow><mi>x</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt></mrow></mfenced></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>x</mi><mo>&#183;</mo><mfenced><mfrac><mn>1</mn><mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt></mrow></mfrac></mfenced><mo>&#183;</mo><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><msqrt><mn>2</mn></msqrt><mo>-</mo><mfrac><mn>2</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced open="{" close="}"><mfrac><mrow><mi>x</mi><mfenced><mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>-</mo><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt></mrow></mfenced></mrow><mrow><mfenced><mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt></mrow></mfenced><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><msqrt><mn>2</mn></msqrt><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced close="}" open="{"><mfrac><mrow><mi>x</mi><msup><mfenced><mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>-</mo><msqrt><mn>1</mn><mo>+</mo><mi>x</mi></msqrt></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mo>-</mo><mn>2</mn><mi>x</mi><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mfenced><mrow><mn>2</mn><mo>-</mo><mn>2</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfenced><mo>+</mo><msubsup><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfenced><mrow><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></mrow></mfenced><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q14. JEE Main 2021 (17 Mar Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>e</mi></msubsup><msup><mi>x</mi><mn>19</mn></msup><mo>(</mo><mi>log</mi><mo>|</mo><mi>x</mi><mo>|</mo><msup><mo>)</mo><mi>n</mi></msup><mi>d</mi><mi>x</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>. If  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>20</mn></mfenced><msub><mi>I</mi><mn>10</mn></msub><mo>=</mo><mi>&#945;</mi><msub><mi>I</mi><mn>9</mn></msub><mo>+</mo><mi>&#946;</mi><msub><mi>I</mi><mn>8</mn></msub><mo>,</mo></math> for natural numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></math> equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>e</mi></msubsup><msup><mi>x</mi><mn>19</mn></msup><mo>(</mo><mi>log</mi><mo>|</mo><mi>x</mi><mo>|</mo><msup><mo>)</mo><mi>n</mi></msup><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>e</mi></msubsup><msup><mi>x</mi><mn>19</mn></msup><msup><mfenced><mrow><mi>log</mi><mi>x</mi></mrow></mfenced><mi>n</mi></msup><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mo>&#8757;</mo></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mi>e</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p>Integrating by using by parts rule, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mfenced><mrow><mi>u</mi><mo>&#183;</mo><mi>v</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mi>u</mi><mo>&#8747;</mo><mi>v</mi><mi>d</mi><mi>x</mi></mrow></mfenced><mi>a</mi><mi>b</mi></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mfenced close="]" open="["><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mi>u</mi></mfenced><mo>&#8747;</mo><mi>v</mi><mi>d</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>,</mo></math> taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>=</mo><mi>log</mi><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>v</mi><mo>=</mo><msup><mi>x</mi><mn>19</mn></msup><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>n</mi></msub><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi>log</mi><mi>x</mi></mrow></mfenced><mi>n</mi></msup><mo>&#8747;</mo><msup><mi>x</mi><mn>19</mn></msup><mi>d</mi><mi>x</mi></mrow></mfenced><mn>1</mn><mi>e</mi></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>e</mi></msubsup><mfenced close="]" open="["><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><msup><mfenced><mrow><mi>log</mi><mi>x</mi></mrow></mfenced><mi>n</mi></msup><mo>&#8747;</mo><msup><mi>x</mi><mn>19</mn></msup><mi>d</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mi>n</mi></msub><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi>log</mi><mi>x</mi></mrow></mfenced><mi>n</mi></msup><mfenced><mfrac><msup><mi>x</mi><mn>20</mn></msup><mn>20</mn></mfrac></mfenced></mrow></mfenced><mn>1</mn><mi>e</mi></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>e</mi></msubsup><mfenced close="]" open="["><mrow><mi>n</mi><msup><mfenced><mrow><mi>log</mi><mi>x</mi></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>&#215;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>&#215;</mo><mfenced><mfrac><msup><mi>x</mi><mn>20</mn></msup><mn>20</mn></mfrac></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mi>n</mi></msub><mo>=</mo><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi>log</mi><mi>e</mi></mrow></mfenced><mi>n</mi></msup><mfenced><mfrac><msup><mi>e</mi><mn>20</mn></msup><mn>20</mn></mfrac></mfenced><mo>-</mo><mn>0</mn></mrow></mfenced><mo>-</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>e</mi></msubsup><mfenced close="]" open="["><mrow><mi>n</mi><msup><mfenced><mrow><mi>log</mi><mi>x</mi></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>&#215;</mo><mfenced><mfrac><msup><mi>x</mi><mn>19</mn></msup><mn>20</mn></mfrac></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mi>n</mi></msub><mo>=</mo><mfenced><mfrac><msup><mi>e</mi><mn>20</mn></msup><mn>20</mn></mfrac></mfenced><mo>-</mo><mfrac><mi>n</mi><mn>20</mn></mfrac><msubsup><mo>&#8747;</mo><mn>1</mn><mi>e</mi></msubsup><msup><mi>x</mi><mn>19</mn></msup><msup><mfenced><mrow><mi>log</mi><mi>x</mi></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>20</mn><msub><mi>I</mi><mi>n</mi></msub><mo>=</mo><msup><mi>e</mi><mn>20</mn></msup><mo>-</mo><mi>n</mi><msub><mi>I</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></math></p><p>Hence, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><msub><mi>I</mi><mn>10</mn></msub><mo>=</mo><msup><mi>e</mi><mn>20</mn></msup><mo>-</mo><mn>10</mn><msub><mi>I</mi><mn>9</mn></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><msub><mi>I</mi><mn>9</mn></msub><mo>=</mo><msup><mi>e</mi><mn>20</mn></msup><mo>-</mo><mn>9</mn><msub><mi>I</mi><mn>8</mn></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>On subtracting the above two equations, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><msub><mi>I</mi><mn>10</mn></msub><mo>-</mo><mn>20</mn><msub><mi>I</mi><mn>9</mn></msub><mo>=</mo><mo>-</mo><mn>10</mn><msub><mi>I</mi><mn>9</mn></msub><mo>+</mo><mn>9</mn><msub><mi>I</mi><mn>8</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>20</mn><msub><mi>I</mi><mn>10</mn></msub><mo>=</mo><mn>10</mn><msub><mi>I</mi><mn>9</mn></msub><mo>+</mo><mn>9</mn><msub><mi>I</mi><mn>8</mn></msub></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><msub><mi>I</mi><mn>10</mn></msub><mo>=</mo><mi>&#945;</mi><msub><mi>I</mi><mn>9</mn></msub><mo>+</mo><mi>&#946;</mi><msub><mi>I</mi><mn>8</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>9</mn></math> and hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn><mo>.</mo></math></p>

</details>

---

### Q15. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><msup><mi>cot</mi><mi>n</mi></msup><mi>x</mi><mi>d</mi><mi>x</mi></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><msub><mi>I</mi><mn>4</mn></msub><mo>,</mo><msup><mfenced><mrow><msub><mi>I</mi><mn>3</mn></msub><mo>+</mo><msub><mi>I</mi><mn>5</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>,</mo><msub><mi>I</mi><mn>4</mn></msub><mo>+</mo><msub><mi>I</mi><mn>6</mn></msub></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">G</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><msub><mi>I</mi><mn>4</mn></msub><mo>,</mo><msub><mi>I</mi><mn>3</mn></msub><mo>+</mo><msub><mi>I</mi><mn>5</mn></msub><mo>,</mo><msub><mi>I</mi><mn>4</mn></msub><mo>+</mo><msub><mi>I</mi><mn>6</mn></msub></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><msub><mi>I</mi><mn>4</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>I</mi><mn>3</mn></msub><mo>+</mo><msub><mi>I</mi><mn>5</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>I</mi><mn>4</mn></msub><mo>+</mo><msub><mi>I</mi><mn>6</mn></msub></mrow></mfrac></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><msub><mi>I</mi><mn>4</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>I</mi><mn>3</mn></msub><mo>+</mo><msub><mi>I</mi><mn>5</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>I</mi><mn>4</mn></msub><mo>+</mo><msub><mi>I</mi><mn>6</mn></msub></mrow></mfrac></math>  are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">G</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><msub><mi>I</mi><mn>4</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>I</mi><mn>3</mn></msub><mo>+</mo><msub><mi>I</mi><mn>5</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>I</mi><mn>4</mn></msub><mo>+</mo><msub><mi>I</mi><mn>6</mn></msub></mrow></mfrac></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><msup><mi>cot</mi><mi>n</mi></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><msup><mi>cot</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mi>x</mi><mfenced><mrow><msup><mo>cosec</mo><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mfenced open="" close="]"><mrow><mo>=</mo><mo>-</mo><mfrac><mrow><msup><mi>cot</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mrow><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mo>-</mo><msub><mi>I</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><msub><mi>I</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mi>n</mi></msub><mo>+</mo><msub><mi>I</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>3</mn></msub><mo>+</mo><msub><mi>I</mi><mn>5</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub><mo>+</mo><msub><mi>I</mi><mn>6</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mn>1</mn><mrow><msub><mi>I</mi><mn>2</mn></msub><mo>+</mo><msub><mi>I</mi><mn>4</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>I</mi><mn>3</mn></msub><mo>+</mo><msub><mi>I</mi><mn>5</mn></msub></mrow></mfrac><mo>,</mo><mfrac><mn>1</mn><mrow><msub><mi>I</mi><mn>4</mn></msub><mo>+</mo><msub><mi>I</mi><mn>6</mn></msub></mrow></mfrac></math>  are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math></p>

</details>

---

### Q16. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>x</mi><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">t</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mi>e</mi></msub><mn>2</mn></math>
- **(B)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mn>2</mn></math>
- **(C)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mn>2</mn></math>
- **(D)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mi>e</mi></msub><mn>2</mn></math>**

**Detailed Solution:**

<p>Given integral, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>x</mi><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Put <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>t</mi><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>t</mi><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>t</mi><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mrow><mi>t</mi><mo>-</mo><mfenced separators="|"><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi><mfenced separators="|"><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></mfenced><mi>d</mi><mi>t</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>a</mi><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>b</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mo>&#183;</mo><mi>b</mi></mrow></mfrac></mfenced><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mo>-</mo><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mfenced></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mo>-</mo><mi>a</mi></mrow></mfenced><mo>=</mo><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>a</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi><mi>d</mi><mi>t</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8901;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p>Now applying the integration by parts i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mfenced><mrow><mi>u</mi><mo>&#183;</mo><mi>v</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>u</mi><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>v</mi><mi>d</mi><mi>x</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mfenced close="]" open="["><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mi>u</mi></mfenced><mo>&#8747;</mo><mi>v</mi><mi>d</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mrow><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi><mo>&#8901;</mo><mi>t</mi><mo>|</mo></mrow><mn>0</mn><mn>1</mn></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>&#8901;</mo><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup><mo>=</mo><mi>u</mi><mo>,</mo><mo>&#160;</mo><mo>&#8658;</mo><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi><mo>=</mo><mi>d</mi><mi>u</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>1</mn></mfenced><mo>&#8901;</mo><mn>1</mn><mo>-</mo><mn>0</mn></mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mfrac><mn>1</mn><mi>u</mi></mfrac></mfenced><mi>d</mi><mi>u</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mn>2</mn></msub><mfenced separators="|"><mi>u</mi></mfenced><msubsup><mfenced open="" close="|" separators="|"><mi mathvariant="normal">&#8203;</mi></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>.</mo></math></p>

</details>

---

### Q17. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `3`

The value of the integral
$$
\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \sin ^4 x\left(1+\log \left(\frac{2+\sin x}{2-\sin x}\right)\right) d x \text { is }
$$

**Options:**

- **(A)** $\frac{3}{16} \pi$
- **(B)** 0
- **(C)** $\frac{3}{8} \pi$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{8} \pi$**

**Detailed Solution:**

Let
$$
\begin{aligned}
I &=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \sin ^4 x\left(1+\log \left(\frac{2+\sin x}{2-\sin x}\right)\right) d x \ldots .(1) \\
\Rightarrow I &\left.=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \sin ^4(-x)\right)\left(1+\log \left(\frac{2+\sin (-x)}{2-\sin (-x)}\right)\right) \cdot d x \\
&=\left[\because \int_a^b f(x) . d x=\int_a^b f(a+b-x) \cdot d x\right]
\end{aligned}
$$
$$
\begin{aligned}
&=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\left(\sin ^4 x\right)\left(1+\log \left(\frac{2-\sin x}{2+\sin x}\right)\right) \cdot d x \\
&=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \sin ^4 x\left(1-\log \left(\frac{2+\sin x}{2-\sin x}\right)\right) \cdot d x \ldots .(2)
\end{aligned}
$$
After adding equation (1) and (2) we get,
$$
\begin{aligned}
&2 I=2 \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \sin ^4 x \cdot d x \\
&2 I=4 \int_0^{\frac{\pi}{2}} \sin ^4 x \cdot d x \\
&I=2 \int_0^{\frac{\pi}{2}} \sin ^4 x \cdot d x=\frac{\frac{3}{2} \times \frac{1}{2} \times \pi}{2 \times 2}=\frac{3 \pi}{8} \\
&{[\text { By Gamma function] }}
\end{aligned}
$$

</details>

---

### Q18. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The integral $\int_{7 \pi / 4}^{7 \pi / 3} \sqrt{\tan ^2 x} d x$ is equal to :

**Options:**

- **(A)** $\log 2 \sqrt{2}$
- **(B)** $\log 2$
- **(C)** $2 \log 2$
- **(D)** $\log \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log \sqrt{2}$**

**Detailed Solution:**

Let $\mathrm{I}=\int_{7 \pi / 4}^{7 \pi / 3} \sqrt{\tan ^2 x} d x$
$$
=\int_{7 \pi / 4}^{7 \pi / 3} \tan x d x=-\left.\log \cos x\right|_{7 \pi / 4} ^{7 \pi / 3}
$$
$=-\left[\log \cos \frac{7 \pi}{3}-\log \cos \frac{7 \pi}{4}\right]$
$=\log \cos \frac{7 \pi}{4}-\log \cos \frac{7 \pi}{3}$
$=\log \left[\frac{\cos \frac{7 \pi}{4}}{\cos \frac{7 \pi}{3}}\right]=\log \left[\frac{\cos \left(2 \pi-\frac{\pi}{4}\right)}{\cos \left(2 \pi+\frac{\pi}{3}\right)}\right]$
$=\log \left(\frac{\cos \frac{\pi}{4}}{\cos \frac{\pi}{3}}\right)=\log \left(\frac{\frac{1}{\sqrt{2}}}{\frac{1}{2}}\right)$
$=\log \left(\frac{2}{\sqrt{2}}\right)=\log \sqrt{2}$.

</details>

---

