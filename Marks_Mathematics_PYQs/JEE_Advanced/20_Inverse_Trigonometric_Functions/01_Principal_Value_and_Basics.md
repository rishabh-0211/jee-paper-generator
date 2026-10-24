# JEE Advanced Mathematics - Inverse Trigonometric Functions

## Topic 1: Principal Value and Basics

**Total Questions:** 3

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Considering only the principal values of the inverse trigonometric functions, the value of

$\cot^{-1}(\cot(-11)) + 10 \sin\left(2 \cos^{-1}\left(\dfrac{1}{\sqrt{2}}\right)\right) + 10 \sin(2 \tan^{-1}(2))$

is

**Options:**

- **(A)** $3\pi + 7$
- **(B)** $7$
- **(C)** $4\pi + 7$
- **(D)** $3\pi - 5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4\pi + 7$**

**Detailed Solution:**

For the first term, $\cot^{-1}(\cot(-11))$:
The principal value branch of $\cot^{-1}(x)$ is $(0, \pi)$.
Since the cotangent function is periodic with period $\pi$, $\cot(-11) = \cot(-11 + 4\pi)$.
Using $\pi \approx 3.14$, we have $4\pi \approx 12.56$, so $-11 + 4\pi \approx 1.56$, which lies in the interval $(0, \pi)$.
Thus, $\cot^{-1}(\cot(-11)) = 4\pi - 11$.

For the second term, $10 \sin\left(2 \cos^{-1}\left(\dfrac{1}{\sqrt{2}}\right)\right)$:
Since $\cos^{-1}\left(\dfrac{1}{\sqrt{2}}\right) = \dfrac{\pi}{4}$, we get:
$10 \sin\left(2 \times \dfrac{\pi}{4}\right) = 10 \sin\left(\dfrac{\pi}{2}\right) = 10(1) = 10$.

For the third term, $10 \sin(2 \tan^{-1}(2))$:
Let $\theta = \tan^{-1}(2) \Rightarrow \tan(\theta) = 2$.
Using the multiple angle formula $\sin(2\theta) = \dfrac{2\tan(\theta)}{1 + \tan^2(\theta)}$, we obtain:
$\sin(2\theta) = \dfrac{2(2)}{1 + 2^2} = \dfrac{4}{5}$.
Therefore, $10 \sin(2 \tan^{-1}(2)) = 10 \times \dfrac{4}{5} = 8$.

Adding the three evaluated terms together:
$(4\pi - 11) + 10 + 8 = 4\pi + 7$.

Answer: $4\pi + 7$

</details>

---

### Q2. JEE Advanced 2024 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

Considering only the principal values of the inverse trigonometric functions, the value of $\tan \left(\sin ^{-1}\left(\frac{3}{5}\right)-2 \cos ^{-1}\left(\frac{2}{\sqrt{5}}\right)\right)$ is

**Options:**

- **(A)** $\frac{7}{24}$
- **(B)** $\frac{-7}{24}$
- **(C)** $\frac{-5}{24}$
- **(D)** $\frac{5}{24}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-7}{24}$**

**Detailed Solution:**

<p>Let $E = \tan\left(\sin^{-1}\left(\frac{3}{5}\right) - 2\cos^{-1}\left(\frac{2}{\sqrt{5}}\right)\right)$.</p><p><strong>Evaluate the inverse trigonometric expressions:</strong> Let $\alpha = \sin^{-1}\left(\frac{3}{5}\right)$, so $\sin\alpha = \frac{3}{5}$ and $\tan\alpha = \frac{3}{4}$. Let $\beta = \cos^{-1}\left(\frac{2}{\sqrt{5}}\right)$, so $\cos\beta = \frac{2}{\sqrt{5}}$ and $\tan\beta = \frac{1}{2}$.</p><p><strong>Compute the double angle:</strong> Using $\tan(2\beta) = \frac{2\tan\beta}{1 - \tan^2\beta}$, we obtain $\tan(2\beta) = \frac{2\cdot\frac{1}{2}}{1 - \left(\frac{1}{2}\right)^2} = \frac{4}{3}$.</p><p><strong>Apply the tangent subtraction formula:</strong> $E = \tan(\alpha - 2\beta) = \frac{\tan\alpha - \tan(2\beta)}{1 + \tan\alpha\tan(2\beta)} = \frac{\frac{3}{4} - \frac{4}{3}}{1 + \frac{3}{4}\cdot\frac{4}{3}} = \frac{-\frac{7}{12}}{2} = -\frac{7}{24}$.</p><p><strong>Final result:</strong> $\boxed{-\frac{7}{24}}$</p>

</details>

---

### Q3. JEE Advanced 2015 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

If <math><mi>&#945;</mi><mo>=</mo><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>6</mn></mrow><mrow><mn>11</mn></mrow></mfrac></mrow></mfenced><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><mi>&#946;</mi><mo>=</mo><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfenced><mo>,</mo></mrow></mrow></mrow></mrow></math> where the inverse trigonometric functions take only the principal values, then the correct options(s) is(are)

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>β</mi><mo>&gt;</mo><mn>0</mn></mrow></mrow></math>
- **(B)** <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>β</mi></mrow></mrow><mo>&lt;</mo><mn>0</mn></math>
- **(C)** <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>α</mi><mo>+</mo><mi>β</mi></mrow></mfenced></mrow></mrow><mo>&gt;</mo><mn>0</mn></math>
- **(D)** <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>α</mi><mo>&lt;</mo><mn>0</mn></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>α</mi><mo>&lt;</mo><mn>0</mn></mrow></mrow></math>**

**Detailed Solution:**

<math><mi>α</mi><mo>=</mo><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>6</mn></mrow><mrow><mn>11</mn></mrow></mfrac></mrow></mrow></math> 
Since   <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>&gt;</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>6</mn></mrow><mrow><mn>11</mn></mrow></mfrac><mo>&gt;</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mrow></math> 
 <math><mfrac><mrow><mn>3</mn><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>&gt;</mo><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>6</mn></mrow><mrow><mn>11</mn></mrow></mfrac><mo>&gt;</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></math> 
 <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>α</mi><mo>&lt;</mo><mn>0</mn></mrow></mrow></math> 
 <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mrow></mrow></mfenced><mo>=</mo><mn>4</mn><mo>×</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>3</mn><mo>×</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mrow></math> 
 <math><mo>=</mo><mfrac><mrow><mn>4</mn><mo>×</mo><mn>64</mn></mrow><mrow><mn>729</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>12</mn></mrow><mrow><mn>9</mn></mrow></mfrac></math> 
 <math><mo>=</mo><mfrac><mrow><mn>256</mn><mo>-</mo><mn>12</mn><mo>×</mo><mn>81</mn></mrow><mrow><mn>72</mn></mrow></mfrac><mo>&lt;</mo><mn>0</mn></math> 
 <math><mfrac><mrow><mn>5</mn><mi>π</mi></mrow><mrow><mn>12</mn></mrow></mfrac><mo>&gt;</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>&gt;</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mrow></math> 
 <math><mfrac><mrow><mn>5</mn><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>&gt;</mo><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>&gt;</mo><mi>π</mi></mrow></mrow></math> 
 <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>3</mn><mfrac><mrow><mi>c</mi><mi>o</mi><msup><mrow><mi>s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>&lt;</mo><mn>0</mn></math> 
 <math><mfrac><mrow><mn>3</mn><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>&gt;</mo><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>6</mn></mrow><mrow><mn>11</mn></mrow></mfrac><mo>&gt;</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></math> 
 <math><mfrac><mrow><mn>5</mn><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>&gt;</mo><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>&gt;</mo><mi>π</mi></mrow></mrow></math> 
 <math><mn>2</mn><mi>π</mi><mo>&gt;</mo><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>6</mn></mrow><mrow><mn>11</mn></mrow></mfrac><mo>+</mo><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>&gt;</mo><mfrac><mrow><mn>3</mn><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></mrow></mrow></math> 
 <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>6</mn></mrow><mrow><mn>11</mn></mrow></mfrac><mo>+</mo><mn>3</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mrow></mrow></mrow></mrow></mfenced></mrow></mrow><mo>&gt;</mo><mn>0</mn></math>

</details>

---

