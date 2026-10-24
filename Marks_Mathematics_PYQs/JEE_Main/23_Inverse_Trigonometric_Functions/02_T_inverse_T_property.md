# JEE Main Mathematics - Inverse Trigonometric Functions

## Topic 2: T inverse T property

**Total Questions:** 11

---

### Q1. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \tan^{-1}\left(\dfrac{3\cos x - 4\sin x}{4\cos x + 3\sin x}\right) + 2\tan^{-1}\left(\dfrac{x}{1+\sqrt{1-x^2}}\right)$, then $\dfrac{dy}{dx}$ at $x = \dfrac{\sqrt{3}}{2}$ is equal to:

**Options:**

- **(A)** $3$
- **(B)** $-1$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

Let $y = y_1 + y_2$

$y_1 = \tan^{-1}\left(\dfrac{3\cos x - 4\sin x}{4\cos x + 3\sin x}\right)$

Dividing the numerator and denominator by $4\cos x$:

$y_1 = \tan^{-1}\left(\dfrac{\dfrac{3}{4} - \tan x}{1 + \dfrac{3}{4}\tan x}\right)$

Using the formula $\tan^{-1}\left(\dfrac{A - B}{1 + AB}\right) = \tan^{-1}A - \tan^{-1}B$:

$y_1 = \tan^{-1}\left(\dfrac{3}{4}\right) - \tan^{-1}(\tan x) = \tan^{-1}\left(\dfrac{3}{4}\right) - x$

Differentiating with respect to $x$:

$\dfrac{dy_1}{dx} = -1$

Now, $y_2 = 2\tan^{-1}\left(\dfrac{x}{1+\sqrt{1-x^2}}\right)$

Substituting $x = \sin \theta$:

$y_2 = 2\tan^{-1}\left(\dfrac{\sin \theta}{1+\cos \theta}\right)$

$y_2 = 2\tan^{-1}\left(\dfrac{2\sin(\theta/2)\cos(\theta/2)}{2\cos^2(\theta/2)}\right)$

$y_2 = 2\tan^{-1}\left(\tan\dfrac{\theta}{2}\right) = 2\left(\dfrac{\theta}{2}\right) = \theta = \sin^{-1}x$

Differentiating with respect to $x$:

$\dfrac{dy_2}{dx} = \dfrac{1}{\sqrt{1-x^2}}$

At $x = \dfrac{\sqrt{3}}{2}$:

$\dfrac{dy_2}{dx} = \dfrac{1}{\sqrt{1 - \left(\dfrac{\sqrt{3}}{2}\right)^2}} = \dfrac{1}{\sqrt{1 - \dfrac{3}{4}}} = \dfrac{1}{\sqrt{\dfrac{1}{4}}} = 2$

Therefore, $\dfrac{dy}{dx} = \dfrac{dy_1}{dx} + \dfrac{dy_2}{dx} = -1 + 2 = 1$

Answer: $1$

</details>

---

### Q2. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Using the principal values of the inverse trigonometric functions, the sum of the maximum and the minimum values of $16\left(\left(\sec ^{-1} x\right)^2+\left(\operatorname{cosec}^{-1} x\right)^2\right)$ is :

**Options:**

- **(A)** $24 \pi^2$
- **(B)** $22 \pi^2$
- **(C)** $31 \pi^2$
- **(D)** $18 \pi^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $22 \pi^2$**

**Detailed Solution:**

$\begin{aligned} & 16\left(\sec ^{-1} x\right)^2+\left(\operatorname{cosec}^{-1} x\right)^2 \\ & \operatorname{Sec}^{-1} x=a \in[0, \pi]-\left\{\frac{\pi}{2}\right\} \\ & \operatorname{cosec}^{-1} x=\frac{\pi}{2}-a \\ & =16\left[a^2+\left(\frac{\pi}{2}-a\right)^2\right]=16\left[2 a^2-\pi a+\frac{\pi^2}{4}\right] \\ & \max ]_{a=\pi}=16\left[2 \pi^2-\pi^2+\pi \frac{2}{4}\right]=20 \pi^2 \\ & \min ]_{a=\frac{\pi}{4}}=16\left[\frac{2 \times \pi^2}{16}-\frac{\pi^2}{4}+\frac{\pi^2}{4}\right]=2 \pi^2 \\ & \operatorname{Sum}=22 \pi^2\end{aligned}$

</details>

---

### Q3. JEE Main 2024 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

For $n \in \mathrm{N}$, if $\cot ^{-1} 3+\cot ^{-1} 4+\cot ^{-1} 5+\cot ^{-1} n=\frac{\pi}{4}$, then $n$ is equal to_____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **47**

**Detailed Solution:**

$\begin{aligned} & \cot ^{-1} 3+\cot ^{-1} 4+\cot ^{-1} 5+\cot ^1 n=\frac{\pi}{4} \\ & \tan ^{-1} \frac{1}{3}+\tan ^{-1} \frac{1}{4}+\tan ^{-1} \frac{1}{5}+\tan ^{-1} \frac{1}{\mathrm{n}}=\frac{\pi}{4} \\ & \tan ^{-1}\left(\frac{46}{48}\right)+\tan ^{-1} \frac{1}{\mathrm{n}}=\frac{\pi}{4} \\ & \tan ^{-1}\left(\frac{23}{24}\right)+\tan ^{-1} \frac{1}{\mathrm{n}}=\frac{\pi}{4} \\ & \tan ^{-1} \frac{1}{\mathrm{n}}=\tan ^{-1} 1-\tan ^{-1} \frac{23}{24}\end{aligned}$
$\begin{aligned} & \tan ^{-1} \frac{1}{n}=\tan ^{-1} 1-\tan ^{-1} \frac{23}{24} \\ & \tan ^{-1} \frac{1}{n}=\tan ^{-1}\left(\frac{1-\frac{23}{24}}{1+\frac{23}{24}}\right) \\ & \tan ^{-1} \frac{1}{n}=\tan ^{-1}\left(\frac{\frac{1}{24}}{\frac{47}{24}}\right) \\ & \tan ^{-1} \frac{1}{n}=\tan ^{-1} \frac{1}{47} \\ & n=47\end{aligned}$

</details>

---

### Q4. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8834;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced></math> be the largest interval for which <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>-</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn><mo>,</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced></math>, holds . If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>&#946;</mi><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><mi>b</mi><mo>-</mo><mi>a</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to;

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>48</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>16</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>-</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn><mo>,</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>&#952;</mi></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>&#952;</mi></mfenced><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>&#62;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#8658;</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/15670a4f-1afb-4513-8515-25b81b592034-9896338.png" style="width: 400px; height: 297px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced><mo>&#8658;</mo><mi>b</mi><mo>-</mo><mi>a</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>-</mo><mi>a</mi><mo>=</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>&#946;</mi><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now defining <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>10</mn><mo>=</mo><mn>1</mn><mo>+</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>&#8805;</mo><mn>1</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math> is the only possible solution</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn><mi>&#946;</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>On solving equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math></p>

</details>

---

### Q5. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>tan</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>11</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>17</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>31</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>11</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>tan</mi><mfenced><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mfenced></math></p><p>Now simplifying each term we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>sin</mi><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced><mo>=</mo><mi>&#960;</mi><mo>-</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn><mi>&#960;</mi><mo>-</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>tan</mi><mfenced><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>-</mo><mi>&#960;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>cos</mi><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>tan</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>6</mn></mfrac><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>11</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math></p>

</details>

---

### Q6. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the inverse trigonometric functions take principal values, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mfrac><mn>3</mn><mn>10</mn></mfrac><mi>cos</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced></mrow></mfenced><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>sin</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced></mrow></mfenced></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced><mo>=</mo><mi>&#952;</mi><mo>&#8658;</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"></math><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4449f062-a2f6-473e-b1c4-62766ef7c9b4-image.png" style="width: 140px; height: 120px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="}" open="{"><mrow><mfrac><mn>3</mn><mn>10</mn></mfrac><mi>cos</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>sin</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="}" open="{"><mrow><mfrac><mn>3</mn><mn>10</mn></mfrac><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="}" open="{"><mrow><mfrac><mn>3</mn><mn>10</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>&#215;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="}" open="{"><mrow><mfrac><mn>9</mn><mn>50</mn></mfrac><mo>+</mo><mfrac><mn>8</mn><mn>25</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math></p>

</details>

---

### Q7. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>cos</mi><mo>(</mo><mo>-</mo><mn>5</mn><mo>)</mo><mo>)</mo><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>sin</mi><mo>(</mo><mn>6</mn><mo>)</mo><mo>)</mo><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>tan</mi><mo>(</mo><mn>12</mn><mo>)</mo><mo>)</mo></math> is equal to :
(The inverse trigonometric functions take the principal values)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>&#960;</mi><mo>+</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>&#960;</mi><mo>-</mo><mn>11</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#960;</mi><mo>-</mo><mn>11</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#960;</mi><mo>-</mo><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#960;</mi><mo>-</mo><mn>11</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>cos</mi><mo>(</mo><mo>-</mo><mn>5</mn><mo>)</mo><mo>)</mo><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close=""><mrow><mi>sin</mi><mo>(</mo><mn>6</mn><mo>)</mo><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>tan</mi><mo>(</mo><mn>12</mn><mo>)</mo><mo>)</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>&#960;</mi><mo>-</mo><mn>5</mn><mo>+</mo><mo>(</mo><mo>-</mo><mn>2</mn><mi>&#960;</mi><mo>+</mo><mn>6</mn><mo>)</mo><mo>-</mo><mo>(</mo><mn>12</mn><mo>-</mo><mn>4</mn><mi>&#960;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mi>&#960;</mi><mo>-</mo><mn>11</mn></math></p>

</details>

---

### Q8. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>x</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>10</mn></mrow></mrow></mrow></mfenced><mi mathvariant="normal">&#160;</mi></math> and <math><mtext>&#8201;</mtext><mi>y</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mtext>&#8201;</mtext><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>10</mn></mrow></mrow></mrow></mfenced><mo>,</mo></math> then <math><mi>y</mi><mo>-</mo><mi>x</mi></math> is equal to:

**Options:**

- **(A)** <math><mn>10</mn></math>
- **(B)** <math><mi>π</mi></math>
- **(C)** <math><mn>0</mn></math>
- **(D)** <math><mn>7</mn><mi>π</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>π</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/vulinsbzhjdkqpfhcrzrklhhdhgebunqdxbuhuvsgsuxdtekod.png" />

From the graph of <math><mi>y</mi><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow><mo>,</mo></math> it is clear that <math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mo>(</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>10</mn><mo>)</mo></mrow></mrow></mrow></mrow><mo>=</mo><mn>3</mn><mi>&#960;</mi><mo>-</mo><mn>10</mn></math>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/iihagccbvavbobdwhplicjqnpvamweljhayqirxvazttvjlpzy.png" />

From the graph of <math><mi>y</mi><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></math>

It is clear that <math><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>10</mn></mrow></mrow></mrow></mfenced><mo>=</mo><mn>4</mn><mi>&#960;</mi><mo>-</mo><mn>10</mn></mrow></mrow></math>

Hence <math><mi>y</mi><mo>-</mo><mi>x</mi><mo>=</mo><mfenced separators="|"><mrow><mn>4</mn><mi>&#960;</mi><mo>-</mo><mn>10</mn><mi>&#160;</mi></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mn>3</mn><mi>&#960;</mi><mo>-</mo><mn>10</mn></mrow></mfenced><mo>=</mo><mi>&#960;</mi></math></p>

</details>

---

### Q9. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced open="[" close="]" separators="|"><mfrac><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mi>&#160;</mi><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mi>&#160;</mi><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfrac></mfenced><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced><mo>&#60;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo></math> is equal to:

**Options:**

- **(A)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>
- **(B)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>
- **(C)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>
- **(D)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></math>**

**Detailed Solution:**

Assume that ,
<math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>&#952;</mi></mrow></mrow><mo>;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><msup><mrow><mi>cos</mi></mrow><mrow><mn>-1</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>tan</mi><mo>- 1</mo></msup><mo>&#8289;</mo><mfenced open="[" close="]" separators="|"><mfrac><mrow><msqrt><mn>1</mn><mo>+</mo><mi>cos</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi></msqrt><mo>+</mo><mi>&#160;</mi><msqrt><mn>1</mn><mo>-</mo><mi>cos</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi></msqrt></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><mi>cos</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi></msqrt><mo>-</mo><mi>&#160;</mi><msqrt><mn>1</mn><mo>-</mo><mi>cos</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi></msqrt></mrow></mfrac></mfenced><mspace linebreak="newline"/><mo>=</mo><msup><mi>tan</mi><mo>- 1</mo></msup><mo>&#8289;</mo><mfenced open="[" close="]" separators="|"><mfrac><mrow><msqrt><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></msqrt><mo>+</mo><mi>&#160;</mi><msqrt><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></msqrt></mrow><mrow><msqrt><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></msqrt><mo>-</mo><mi>&#160;</mi><msqrt><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></msqrt></mrow></mfrac></mfenced><mspace linebreak="newline"/><mo>=</mo><msup><mi>tan</mi><mo>- 1</mo></msup><mo>&#8289;</mo><mfenced open="[" close="]" separators="|"><mfrac><mrow><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mi>&#160;</mi><mi>sin</mi><mi>&#952;</mi></mrow><mrow><msup><mi>cos</mi><mrow/></msup><mi>&#952;</mi><mo>-</mo><mi>&#160;</mi><msup><mi>sin</mi><mrow/></msup><mi>&#952;</mi></mrow></mfrac></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced close="]" open="[" separators="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mo>&#8289;</mo><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfrac></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced close="]" open="[" separators="|"><mrow><mi>tan</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>&#952;</mi></mrow></mfenced></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><msup><mi>x</mi><mn>2</mn></msup></math>

</details>

---

### Q10. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn><mo>&#160;</mo></mrow></msup><mi>y</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn><mo>&#160;</mo></mrow></msup><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>&#60;</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math>,Then a value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>**

**Detailed Solution:**

Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn><mo>&#160;</mo></mrow></msup><mi>y</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn><mo>&#160;</mo></mrow></msup><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mtext>,&#160;</mtext><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>&#60;</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn><mo>&#160;</mo></mrow></msup><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn><mo>&#160;</mo></mrow></msup><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn><mo>&#160;</mo></mrow></msup><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn><mo>&#160;</mo></mrow></msup><mi>y</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>3</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>

</details>

---

### Q11. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let $S=\left\{\left(\begin{array}{ll}a_{11} & a_{12} \\ a_{21} & a_{22}\end{array}\right): a_{i j} \in\{0,1,2\}, a_{11}=a_{22}\right\}$
Then the number of non-singular matrices in the set $S$ is :

**Options:**

- **(A)** 27
- **(B)** 24
- **(C)** 10
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 20**

**Detailed Solution:**

The matrices in the form
$$
\left[\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right], a_{i j} \in\{0,1,2\}, a_{11}=a_{12} \text { are }
$$
$$
\left[\begin{array}{cc}
0 & 0 / 1 / 2 \\
0 / 1 / 2 & 0
\end{array}\right],\left[\begin{array}{cc}
1 & 0 / 1 / 2 \\
0 / 1 / 2 & 1
\end{array}\right],\left[\begin{array}{cc}
2 & 0 / 1 / 2 \\
0 / 1 / 2 & 2
\end{array}\right]
$$
At any place, $0 / 1 / 2$ means 0,1 or 2 will be the element at that place.

Hence there are total $27=3 \times 3+3 \times 3+3 \times 3$ ) matrices of the above form. Out of which the matrices which are singular are
$$
\left[\begin{array}{cc}
0 & 0 / 1 / 2 \\
0 & 0
\end{array}\right],\left[\begin{array}{cc}
0 & 0 \\
1 / 2 & 0
\end{array}\right],\left[\begin{array}{ll}
1 & 1 \\
1 & 1
\end{array}\right],\left[\begin{array}{ll}
2 & 2 \\
2 & 2
\end{array}\right]
$$
Hence there are total $7(=3+2+1+1)$ singular matrices.

Therefore number of all non-singular matrices in the given form $=27-7=20$

</details>

---

