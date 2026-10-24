# JEE Main Mathematics - Inverse Trigonometric Functions

## Topic 6: Sum and difference of angles

**Total Questions:** 27

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $0 < \alpha < 1$, $\beta = \dfrac{1}{3\alpha}$ and $\tan^{-1}(1-\alpha) + \tan^{-1}(1-\beta) = \dfrac{\pi}{4}$. Then $6(\alpha + \beta)$ is equal to:

**Options:**

- **(A)** $6$
- **(B)** $7$
- **(C)** $8$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $7$**

**Detailed Solution:**

Given $\tan^{-1}(1-\alpha) + \tan^{-1}(1-\beta) = \dfrac{\pi}{4}$

Applying the formula $\tan^{-1}x + \tan^{-1}y = \tan^{-1}\left(\dfrac{x+y}{1-xy}\right)$, we get:

$\dfrac{(1-\alpha) + (1-\beta)}{1 - (1-\alpha)(1-\beta)} = \tan\left(\dfrac{\pi}{4}\right) = 1$

$2 - \alpha - \beta = 1 - (1 - \alpha - \beta + \alpha\beta)$

$2 - \alpha - \beta = \alpha + \beta - \alpha\beta$

$2(\alpha + \beta) = 2 + \alpha\beta$

Given $\beta = \dfrac{1}{3\alpha}$, we have $\alpha\beta = \dfrac{1}{3}$. Substituting this into the equation:

$2(\alpha + \beta) = 2 + \dfrac{1}{3}$

$2(\alpha + \beta) = \dfrac{7}{3}$

$\alpha + \beta = \dfrac{7}{6}$

Therefore, $6(\alpha + \beta) = 6 \times \dfrac{7}{6} = 7$

Answer: $7$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 1)

*Type:* `numerical` | *Level:* `2`

If $\dfrac{\pi}{4} + \displaystyle\sum_{p=1}^{11} \tan^{-1}\left(\dfrac{2^{p-1}}{1 + 2^{2p-1}}\right) = \alpha$, then $\tan\alpha$ is equal to __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2048**

**Detailed Solution:**

The general term of the given series is $T_p = \tan^{-1}\left(\dfrac{2^{p-1}}{1 + 2^{2p-1}}\right)$.

This can be rewritten by expressing the numerator and denominator in terms of $2^p$ and $2^{p-1}$:

$T_p = \tan^{-1}\left(\dfrac{2^p - 2^{p-1}}{1 + 2^p \cdot 2^{p-1}}\right)$

Using the inverse trigonometric identity $\tan^{-1}\left(\dfrac{x - y}{1 + xy}\right) = \tan^{-1}x - \tan^{-1}y$, we get:

$T_p = \tan^{-1}(2^p) - \tan^{-1}(2^{p-1})$

Summing $T_p$ from $p = 1$ to $11$ gives a telescoping series:

$\displaystyle\sum_{p=1}^{11} T_p = \left(\tan^{-1}(2^1) - \tan^{-1}(2^0)\right) + \left(\tan^{-1}(2^2) - \tan^{-1}(2^1)\right) + \dots + \left(\tan^{-1}(2^{11}) - \tan^{-1}(2^{10})\right)$

Canceling the intermediate terms, we obtain:

$\displaystyle\sum_{p=1}^{11} T_p = \tan^{-1}(2^{11}) - \tan^{-1}(2^0)$

Since $2^0 = 1$ and $\tan^{-1}(1) = \dfrac{\pi}{4}$, the sum becomes:

$\displaystyle\sum_{p=1}^{11} T_p = \tan^{-1}(2^{11}) - \dfrac{\pi}{4}$

Substituting this back into the expression for $\alpha$:

$\alpha = \dfrac{\pi}{4} + \tan^{-1}(2^{11}) - \dfrac{\pi}{4}$

$\alpha = \tan^{-1}(2^{11})$

Taking the tangent of both sides, we get:

$\tan\alpha = 2^{11} = 2048$

Answer: $2048$

</details>

---

### Q3. JEE Main 2026 (28 January Shift 1)

*Type:* `numerical` | *Level:* `3`

If $k=\tan \left(\frac{\pi}{4}+\frac{1}{2} \cos ^{-1}\left(\frac{2}{3}\right)\right)+\tan \left(\frac{1}{2} \sin ^{-1}\left(\frac{2}{3}\right)\right)$, then the number of solutions of the equation $\sin ^{-1}(k x-1)=\sin ^{-1} x-\cos ^{-1} x$ is $\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

Let $\theta = \dfrac{1}{2} \sin^{-1} \dfrac{2}{3}$, then $\dfrac{1}{2} \cos^{-1} \dfrac{1}{3} = \left( \dfrac{\pi}{4} - \theta \right)$
$k = \tan\theta + \cot\theta = \dfrac{1}{\sin\theta \cos\theta} = \dfrac{2}{\sin 2\theta}$
$k = \dfrac{2}{\dfrac{2}{3}} = 3$
$\sin^{-1}(3x - 1) = \sin^{-1}x - \cos^{-1}x$
$\sin^{-1}(3x - 1) = \dfrac{\pi}{2} - 2\cos^{-1}x$
$3x - 1 = \sin\left( \dfrac{\pi}{2} - 2\cos^{-1}x \right)$
$3x - 1 = 2x^2 - 1 \Rightarrow x = 0, \dfrac{3}{2}$ (rejected)
No. of solution $= 1$

</details>

---

### Q4. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of solutions of $\tan^{-1} 4x + \tan^{-1} 6x = \frac{\pi}{6}$, where $-\frac{1}{2\sqrt{6}} < x < \frac{1}{2\sqrt{6}}$, is equal to

**Options:**

- **(A)** 3
- **(B)** 0
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

For $x \in \left(-\frac{1}{2\sqrt{6}}, \frac{1}{2\sqrt{6}}\right)$, $24x^2 < 1$
So $\tan^{-1}(4x) + \tan^{-1}(6x) = \tan^{-1}\left(\frac{10x}{1-24x^2}\right) = \frac{\pi}{6}$.
$\frac{10x}{1-24x^2} = \frac{1}{\sqrt{3}} \Rightarrow 24x^2 + 10\sqrt{3}x - 1 = 0$.
$x = \frac{-10\sqrt{3} \pm \sqrt{300+96}}{48} = \frac{-5\sqrt{3} \pm 3\sqrt{11}}{24}$.
$x_1 = \frac{-5\sqrt{3}+3\sqrt{11}}{24} \approx 0.054$ (valid, lies in range).
$x_2 = \frac{-5\sqrt{3}-3\sqrt{11}}{24} \approx -0.776$ (rejected, outside range).
Number of solutions $= 1$.

</details>

---

### Q5. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Considering the principal values of the inverse trigonometric functions, $\sin ^{-1}\left(\frac{\sqrt{3}}{2} x+\frac{1}{2} \sqrt{1-x^2}\right),-\frac{1}{2} \lt x \lt \frac{1}{\sqrt{2}}$, is equal to

**Options:**

- **(A)** $\frac{\pi}{4}+\sin ^{-1} x$
- **(B)** $\frac{\pi}{6}+\sin ^{-1} x$
- **(C)** $\frac{-5 \pi}{6}-\sin ^{-1} x$
- **(D)** $\frac{5 \pi}{6}-\sin ^{-1} x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{6}+\sin ^{-1} x$**

**Detailed Solution:**

$\begin{aligned} & \sin ^{-1}\left(\frac{\sqrt{3}}{2} x+\frac{1}{2} \sqrt{1-x^2}\right), \frac{-1}{2} \lt x \lt \frac{1}{\sqrt{2}} \\ & \Rightarrow \text { Let } \sin ^{-1}(x)=\theta \quad \frac{-\pi}{6} \lt \theta \lt \frac{\pi}{4} \\ & \Rightarrow x=\sin \theta, \text { then } \\ & \Rightarrow \sin ^{-1}\left(\frac{\sqrt{3}}{2} \sin \theta+\frac{1}{2} \cos \theta\right) \\ & \Rightarrow \sin ^{-1}\left(\sin \left(\theta+\frac{\pi}{6}\right)\right)=\theta+\frac{\pi}{6} \\ & \Rightarrow \sin ^{-1}(x)+\frac{\pi}{6}\end{aligned}$

</details>

---

### Q6. JEE Main 2025 (2 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

If $y=\cos \left(\frac{\pi}{3}+\cos ^{-1} \frac{x}{2}\right)$, then $(x-y)^2+3 y^2$ is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

$\begin{aligned} & y=\cos \left(\cos ^{-1} \frac{1}{2}+\cos ^{-1} \frac{x}{2}\right) \\ & y=\frac{1}{2} \times \frac{x}{2}-\sqrt{1-\frac{1}{4}} \sqrt{1-\frac{x^2}{4}} \\ & 4 y=x-\sqrt{3} \sqrt{4-x^2} \\ & 3\left(4-x^2\right)=x^2+16 y^2-8 x y \\ & 12-3 x^2=x^2+16 y^2-8 x y \\ & 4 x^2+16 y^2-8 x y=12 \\ & x^2+4 y^2-2 x y=3 \\ & x^2+y^2-2 x y-3 y^2=3 \\ & (x-y)^2+3 y^2=3\end{aligned}$

</details>

---

### Q7. JEE Main 2025 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let \(\mathrm{S}=\left\{x: \cos ^{-1} x=\pi+\sin ^{-1} x+\sin ^{-1}(2 x+1)\right\}\). Then \(\sum_{x \in \mathrm{~S}}(2 x-1)^2\) is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$\begin{aligned} & \cos ^{-1} x=\pi+\sin ^{-1} x+\sin ^{-1}(2 x+1) \\ & 2 \cos ^{-1} x-\sin ^{-1}(2 x+1)=\frac{3 \pi}{2} \\ & 2 \alpha-\beta=\frac{3 \pi}{2} \text { where } \cos ^{-1} x=\alpha, \sin ^{-1}(2 x+1)=\beta \\ & 2 \alpha=\frac{3 \pi}{2}+\beta \\ & \cos 2 \alpha=\sin \beta \\ & 2 \cos ^2 \alpha-1=\sin \beta \\ & 2 x^2-1=2 x+1 \\ & x^2-x-1=0\end{aligned}$
$\begin{aligned} & \Rightarrow \mathrm{n}=\frac{1 \pm \sqrt{5}}{2}=\left[\begin{array}{c}\mathrm{n}=\frac{1+\sqrt{5}}{2} \text { rejected } \\ \mathrm{n}=\frac{1-\sqrt{5}}{2}\end{array}\right. \\ & \therefore 4 \mathrm{x}^2-4 \mathrm{x}=4 \\ & (2 \mathrm{x}-1)^2=5\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\cos \left(\sin ^{-1} \frac{3}{5}+\sin ^{-1} \frac{5}{13}+\sin ^{-1} \frac{33}{65}\right)$ is equal to:

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** $\frac{32}{65}$
- **(D)** $\frac{33}{65}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

$\begin{aligned} & \cos \left(\sin ^{-1} \frac{3}{5}+\sin ^{-1} \frac{5}{13}+\sin ^{-1} \frac{33}{65}\right) \\ & \cos \left(\tan ^{-1} \frac{3}{4}+\tan ^{-1} \frac{5}{12}+\tan ^{-1} \frac{33}{56}\right) \\ & \cos \left(\tan ^{-1}\left(\frac{\frac{3}{4}+\frac{5}{12}}{1+\frac{3}{4} \cdot \frac{5}{12}}\right)+\tan ^{-1} \frac{33}{56}\right) \\ & \cos \left(\tan ^{-1} \frac{56}{33}+\cot ^{-1} \frac{56}{33}\right) \\ & \cos \left(\frac{\pi}{2}\right)=0\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\alpha\gt\beta\gt\gamma\gt0$, then the expression $\cot ^{-1}\left\{\beta+\frac{\left(1+\beta^2\right)}{(\alpha-\beta)}\right\}+\cot ^{-1}\left\{\gamma+\frac{\left(1+\gamma^2\right)}{(\beta-\gamma)}\right\}+\cot ^{-1}\left\{\alpha+\frac{\left(1+\alpha^2\right)}{(\gamma-\alpha)}\right\}$ is equal to :

**Options:**

- **(A)** $\pi$
- **(B)** 0
- **(C)** $\frac{\pi}{2}-(\alpha+\beta+\gamma)$
- **(D)** $3 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\pi$**

**Detailed Solution:**

$\begin{aligned} & \Rightarrow \cot ^{-1}\left(\frac{\alpha \beta+1}{\alpha-\beta}\right)+\cot ^{-1}\left(\frac{\beta \gamma+1}{\beta-\gamma}\right)+\cot ^{-1}\left(\frac{\alpha \gamma+1}{\gamma-\alpha}\right) \\ & \Rightarrow \tan ^{-1}\left(\frac{\alpha-\beta}{1+\alpha \beta}\right)+\tan ^{-1}\left(\frac{\beta-\gamma}{1+\beta \gamma}\right)+\pi+\tan ^{-1}\left(\frac{\gamma-\alpha}{1+\gamma \alpha}\right) \\ & \Rightarrow\left(\tan ^{-1} \alpha-\tan ^{-1} \beta\right)+\left(\tan ^{-1} \beta-\tan ^{-1} \gamma\right)+\left(\pi+\tan ^{-1} \gamma-\tan ^{-1} \alpha\right) \\ & \Rightarrow \pi\end{aligned}$

</details>

---

### Q10. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi><mo>≠</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>α</mi><mo>+</mo><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>β</mi><mo>+</mo><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>γ</mi><mo>=</mo><mi>π</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi></mrow></mfenced><mfenced><mrow><mi>α</mi><mo>−</mo><mi>γ</mi><mo>+</mo><mi>β</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mi>α</mi><mi>β</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>γ</mi></math> equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>α</mi><mo>+</mo><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>β</mi><mo>+</mo><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>γ</mi><mo>=</mo><mi>π</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>α</mi><mo>=</mo><mi>A</mi><mo>,</mo><mo> </mo><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>β</mi><mo>=</mo><mi>B</mi><mo>,</mo><mo> </mo><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>γ</mi><mo>=</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>+</mo><mi>B</mi><mo>+</mo><mi>C</mi><mo>=</mo><mi>π</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mi>sin</mi><mi>A</mi><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mi>sin</mi><mi>B</mi><mo>,</mo><mo> </mo><mi>γ</mi><mo>=</mo><mi>sin</mi><mi>C</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>It is given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi></mrow></mfenced><mn>2</mn></msup><mo>−</mo><msup><mi>γ</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mi>α</mi><mi>β</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup><mo>−</mo><msup><mi>γ</mi><mn>2</mn></msup><mo>=</mo><mi>α</mi><mi>β</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>A</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>B</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>C</mi><mo>=</mo><mi>sin</mi><mi>A</mi><mi>sin</mi><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>A</mi><mo>+</mo><mi>sin</mi><mfenced><mrow><mi>B</mi><mo>+</mo><mi>C</mi></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>B</mi><mo>-</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mi>sin</mi><mi>A</mi><mi>sin</mi><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>A</mi><mo>+</mo><mi>sin</mi><mfenced><mrow><mi>π</mi><mo>-</mo><mi>A</mi></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>B</mi><mo>-</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mi>sin</mi><mi>A</mi><mi>sin</mi><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>A</mi><mo>+</mo><mi>sin</mi><mi>A</mi><mi>sin</mi><mfenced><mrow><mi>B</mi><mo>-</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mi>sin</mi><mi>A</mi><mi>sin</mi><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>A</mi><mfenced close="]" open="["><mrow><mi>sin</mi><mi>A</mi><mo>+</mo><mi>sin</mi><mfenced><mrow><mi>B</mi><mo>-</mo><mi>C</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>sin</mi><mi>A</mi><mi>sin</mi><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>A</mi><mfenced close="]" open="["><mrow><mi>sin</mi><mi>A</mi><mo>+</mo><mi>sin</mi><mfenced><mrow><mi>B</mi><mo>-</mo><mi>C</mi></mrow></mfenced></mrow></mfenced><mo>-</mo><mi>sin</mi><mi>A</mi><mi>sin</mi><mi>B</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>A</mi><mfenced close="]" open="["><mrow><mi>sin</mi><mi>A</mi><mo>+</mo><mi>sin</mi><mfenced><mrow><mi>B</mi><mo>-</mo><mi>C</mi></mrow></mfenced><mo>-</mo><mi>sin</mi><mi>B</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>A</mi><mfenced close="]" open="["><mrow><mi>sin</mi><mfenced><mrow><mi>B</mi><mo>+</mo><mi>C</mi></mrow></mfenced><mo>+</mo><mi>sin</mi><mfenced><mrow><mi>B</mi><mo>-</mo><mi>C</mi></mrow></mfenced><mo>-</mo><mi>sin</mi><mi>B</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>A</mi><mfenced close="]" open="["><mrow><mn>2</mn><mi>sin</mi><mi>B</mi><mi>cos</mi><mi>C</mi><mo>-</mo><mi>sin</mi><mi>B</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>A</mi><mi>sin</mi><mi>B</mi><mfenced close="]" open="["><mrow><mn>2</mn><mi>cos</mi><mi>C</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>A</mi><mo>=</mo><mn>0</mn><mo> </mo><mtext>or</mtext><mo> </mo><mi>sin</mi><mi>B</mi><mo>=</mo><mn>0</mn><mo> </mo><mtext>or</mtext><mo> </mo><mi>cos</mi><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>It is given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi><mo>≠</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>C</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>γ</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p>

</details>

---

### Q11. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Considering only the principal values of inverse trigonometric functions, the number of positive real values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>)</mo><mo>=</mo><mfrac><mi mathvariant="normal">π</mi><mn>4</mn></mfrac></math> is :

**Options:**

- **(A)** More than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Let, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi mathvariant="normal">x</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mi mathvariant="normal">x</mi></math></p><p>Now, differentiating the above function we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">f</mi><mo>'</mo></msup><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>&gt;</mo><mn>0</mn><mo>;</mo><mo> </mo><mo>∀</mo><mi mathvariant="normal">x</mi><mo>∈</mo><mi mathvariant="normal">R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>→</mo><mo>∞</mo></mrow></munder><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mi mathvariant="normal">π</mi><mo> </mo><mtext>and</mtext><mo> </mo><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>→</mo><mo>-</mo><mo>∞</mo></mrow></munder><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mo>-</mo><mi mathvariant="normal">π</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></math> is monotonically increasing for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>∈</mo><mi mathvariant="normal">R</mi></math> and the range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mi mathvariant="normal">π</mi><mo>,</mo><mi mathvariant="normal">π</mi></mrow></mfenced></math>.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfrac><mi mathvariant="normal">π</mi><mn>4</mn></mfrac></math> has exactly one solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&gt;</mo><mn>0</mn></math>.</p>

</details>

---

### Q12. JEE Main 2023 (13 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi><mo>:</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></msqrt></mfrac></mfenced><mo>-</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>x</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>x</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mfenced><mrow><mi>sin</mi><mfenced><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mi>cos</mi><mfenced><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mi>&#960;</mi></mrow></mfenced></mrow></mfenced></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></msqrt></mfrac></mfenced><mo>-</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>x</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>2</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>2</mn></msqrt></mfrac></mfenced><mo>=</mo><mi>sin</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>2</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>&#215;</mo><mfrac><mi>x</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>2</mn></msqrt></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msqrt><mn>2</mn></msqrt><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>2</mn></msqrt></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>2</mn></msqrt><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>&#183;</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></math></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>2</mn></msqrt><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>&#183;</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math> {rejected as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> will not satisfy the given equation}</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>n</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mfenced><mrow><mi>sin</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>cos</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mi>&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mi>sin</mi><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mi>cos</mi><mn>5</mn><mi>&#960;</mi><mo>+</mo><mi>sin</mi><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mi>cos</mi><mn>5</mn><mi>&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>4</mn></math></p></blockquote>

</details>

---

### Q13. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfenced><mo>=</mo><mi>&#960;</mi><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>x</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>-</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Given equation is:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfenced><mo>=</mo><mi>&#960;</mi><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>It is possible if</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mi mathvariant="normal">&#960;</mi></math>    ....(1)</p><p>and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfenced><mo>=</mo><mn>0</mn></math>    ....(2)</p><p>From equation (1), <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> which is not satisfying equation (2).</p><p>So, no such <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> exists.</p>

</details>

---

### Q14. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> represent a parabola with focus <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math> and directrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi><mo>:</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msqrt><mi>f</mi><mfenced><mi>x</mi></mfenced></msqrt><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>1</mn></msqrt></mfenced></mrow></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>:</mo></math>

**Options:**

- **(A)** contains exactly two elements
- **(B)** contains exactly one element
- **(C)** is an infinite set
- **(D)** is an empty set

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) contains exactly two elements**

**Detailed Solution:**

<p>Equation of parabola with focus <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>)</mo></math> and directrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> is:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfenced><mrow><mi>y</mi><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Also,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>By <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> element.</p>

</details>

---

### Q15. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>&#945;</mi><mn>17</mn></mfrac><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>4</mn><mn>5</mn></mfrac><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>77</mn><mn>36</mn></mfrac><mo>=</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>&#60;</mo><mi>&#945;</mi><mo>&#60;</mo><mn>13</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mi>&#945;</mi></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mi>&#945;</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>-</mo><mn>5</mn><mi>&#960;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>&#945;</mi><mn>17</mn></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>77</mn><mn>36</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>&#945;</mi><mn>17</mn></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>77</mn><mn>36</mn></mfrac></mfenced><mo>-</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>&#945;</mi><mn>17</mn></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>77</mn><mn>36</mn></mfrac></mfenced><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>&#945;</mi><mn>17</mn></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mfrac><mn>77</mn><mn>36</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow><mrow><mn>1</mn><mo>+</mo><mfrac><mn>77</mn><mn>36</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>&#945;</mi><mn>17</mn></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>8</mn><mn>15</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>&#945;</mi><mn>17</mn></mfrac></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>8</mn><mn>17</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>8</mn></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mi>&#945;</mi></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mi>&#945;</mi></mrow></mfenced><mspace linebreak="newline"/><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mi>&#945;</mi></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mi>&#945;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mn>8</mn></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mn>8</mn></mrow></mfenced><mo>=</mo><mn>3</mn><mi mathvariant="normal">&#960;</mi><mo>-</mo><mn>8</mn><mo>+</mo><mn>8</mn><mo>-</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mo>=</mo><mi mathvariant="normal">&#960;</mi></math></p>

</details>

---

### Q16. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Considering the principal values of the inverse trigonometric functions, the sum of all the solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><mn>2</mn><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><mi>&#960;</mi><mo>+</mo><mn>2</mn><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><mi>&#960;</mi><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi></math> both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mfenced><mrow><mn>3</mn><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mi>cos</mi><mfenced><mrow><mi>&#960;</mi><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mfenced><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mo>-</mo><mi>cos</mi><mfenced><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#177;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>All will satisfy the original equation,</p><p>So, sum of all the solution will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mn>0</mn></math></p></blockquote>

</details>

---

### Q17. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mrow><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>+</mo><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mrow><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>+</mo><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mfenced><mrow><mn>2</mn><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mfenced><mrow><mn>2</mn><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>40</mn></mfrac></mstyle></mrow></mfrac></mrow></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mfenced close="]" open="["><mrow><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><msup><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></mfenced><mn>2</mn></msup></mrow></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>8</mn></mfrac></mstyle></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tantan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>4</mn></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>8</mn></mfrac></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tantan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q18. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mrow><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>5</mn></mfrac></mfenced><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>5</mn><mn>13</mn></mfrac></mfenced></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>181</mn></mrow><mn>69</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>220</mn><mn>21</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>291</mn></mrow><mn>76</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>151</mn><mn>63</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>220</mn><mn>21</mn></mfrac></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mrow><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>5</mn></mfrac></mfenced><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>5</mn><mn>13</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>5</mn></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>5</mn></mfrac></mfenced><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>5</mn><mn>13</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>5</mn></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>5</mn></mfrac></mstyle></mrow><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>9</mn><mn>25</mn></mfrac></mstyle></mrow></mfrac></mfenced><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>5</mn><mn>13</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mstyle displaystyle="true"><mn>15</mn></mstyle><mstyle displaystyle="true"><mn>8</mn></mstyle></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>5</mn><mn>12</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mfrac><mrow><mfrac><mn>15</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>12</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>15</mn><mn>8</mn></mfrac><mo>&#183;</mo><mfrac><mn>5</mn><mn>12</mn></mfrac></mrow></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>220</mn><mn>21</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>220</mn><mn>21</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>220</mn><mn>21</mn></mfrac></math></p>

</details>

---

### Q19. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>]</mo></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo></math> is :<gwmw style="display:none;"></gwmw>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** Infinite

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Given equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math> is defined if <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#60;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><mn>3</mn></mfrac><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Also, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced></math> is defined if <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><mo>&#8804;</mo><mn>1</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#60;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>So, from <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo></math> we can conclude <span style="color:null;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></span></p><p><span style="color:null;">Case -<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>:</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></span></p><p><span style="color:null;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mn>0</mn><mo>)</mo><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></span></p><p><span style="color:null;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>+</mo><mi>&#960;</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></span></p><p><span style="color:null;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>&#960;</mi></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>&#8713;</mo><mfenced open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced></math></span></p><p><span style="color:null;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> No value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#39;</mo><mi>x</mi><mo>&#39;</mo></math></span></p><p><span style="color:null;">Case - <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>I</mi><mo>:</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></span></p><p><span style="color:null;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></span></p><p><span style="color:null;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>=</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></math></span></p><p><span style="color:null;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>&#960;</mi></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>&#8713;</mo><mfenced open="["><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>,</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></mrow></mfenced></math></span></p><p><span style="color:null;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> No value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#39;</mo><mi>x</mi><mo>&#39;</mo></math></span></p><p><span style="color:null;">So, number of solutions of the equation is zero.</span></p>

</details>

---

### Q20. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>8</mn><mn>31</mn></mfrac></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>32</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>31</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>30</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>33</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>32</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>8</mn><mn>31</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>8</mn><mn>31</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8756;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>8</mn><mn>31</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>8</mn><mn>31</mn></mfrac></math></p><p>Taking tangent both the sides we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>+</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mrow><mn>1</mn><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>31</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>2</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>31</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>31</mn><mi>x</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>8</mn><mo>,</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p>But, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>&#8712;</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>LHS</mi><mo>&#62;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>RHS</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math> (Not possible)</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>8</mn><mo>=</mo><mo>-</mo><mfrac><mn>32</mn><mn>4</mn></mfrac><mo>.</mo><mo>&#160;</mo></math></p><p> </p>

</details>

---

### Q21. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Given that the inverse trigonometric functions take principal values only. Then, the number of real values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> which satisfy <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>5</mn></mfrac></mfenced><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>5</mn></mfrac></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>5</mn></mfrac><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>5</mn></mfrac><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>5</mn></mfrac><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>25</mn></mfrac></msqrt><mo>+</mo><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>5</mn></mfrac><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>25</mn></mfrac></msqrt></mrow></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>5</mn></mfrac><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>25</mn></mfrac></msqrt><mo>+</mo><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>5</mn></mfrac><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>25</mn></mfrac></msqrt><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><msqrt><mn>25</mn><mo>-</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mn>4</mn><msqrt><mn>25</mn><mo>-</mo><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>25</mn><mo>-</mo><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mn>25</mn><mo>-</mo><mn>3</mn><msqrt><mn>25</mn><mo>-</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt></math> </p><p>squaring we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mfenced><mrow><mn>25</mn><mo>-</mo><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>625</mn><mo>+</mo><mn>9</mn><mfenced><mrow><mn>25</mn><mo>-</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mn>150</mn><msqrt><mn>25</mn><mo>-</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn><mo>=</mo><mn>625</mn><mo>+</mo><mn>225</mn><mo>-</mo><mn>150</mn><msqrt><mn>25</mn><mo>-</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>25</mn><mo>-</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mn>3</mn><mo>&#8658;</mo><mn>25</mn><mo>-</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></math> in the original equation We see that all values satisfy the original equation.</p><p>Number of solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q22. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mi>a</mi></mfrac><mo>=</mo><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mi>b</mi></mfrac><mo>=</mo><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow><mi>c</mi></mfrac><mo>;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>c</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfrac></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mi>y</mi><msqrt><mi>y</mi></msqrt></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>y</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mi>r</mi></mfrac><mo>=</mo><mi>a</mi><mo>,</mo><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mi>r</mi></mfrac><mo>=</mo><mi>b</mi><mo>,</mo><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow><mi>r</mi></mfrac><mo>=</mo><mi>c</mi></math><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mfrac><mi>&#960;</mi><mrow><mn>2</mn><mi>r</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi>c</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfrac></mfenced><mo>=</mo><mi>cos</mi><mfenced><mfrac><mrow><mi>&#960;</mi><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow><mrow><mfrac><mi>&#960;</mi><mrow><mn>2</mn><mi>r</mi></mrow></mfrac><mi>r</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>cos</mi><mfenced><mrow><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow></mfenced><mo>,</mo></math> let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>=</mo><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>cos</mi><mfenced><mrow><mn>2</mn><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></math></p>

</details>

---

### Q23. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>cosec</mo><mfenced open="[" close="]"><mrow><mn>2</mn><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>5</mn></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>65</mn><mn>56</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>75</mn><mn>56</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>65</mn><mn>33</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>56</mn><mn>33</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>65</mn><mn>56</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>cosec</mo><mfenced close="]" open="["><mrow><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>5</mn></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>cosec</mo><mfenced open="[" close="]"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mfenced><mstyle displaystyle="true"><mfrac bevelled="true"><mn>1</mn><mn>5</mn></mfrac></mstyle></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mfenced><mfrac bevelled="true"><mn>1</mn><mn>25</mn></mfrac></mfenced></mrow></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></mrow></mfenced><mspace linebreak="newline"/></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>cosec</mo><mfenced open="[" close="]"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>5</mn><mn>12</mn></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>cosec</mo><mfenced open="[" close="]"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>cosec</mo><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>56</mn><mn>33</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>65</mn><mn>56</mn></mfrac></math></p><p>option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p>

</details>

---

### Q24. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>12</mn></mrow><mrow><mn>13</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></mrow></mrow></math> is equal to:

**Options:**

- **(A)** <math><mi>π</mi><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>33</mn></mrow><mrow><mn>65</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(B)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>9</mn></mrow><mrow><mn>65</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(C)** <math><mi>π</mi><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>63</mn></mrow><mrow><mn>65</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(D)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>56</mn></mrow><mrow><mn>65</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>56</mn></mrow><mrow><mn>65</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>**

**Detailed Solution:**

<math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>12</mn></mrow><mrow><mn>13</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></mrow></mrow></math>
<math><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>12</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mi>&#160;</mi></math> <math><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mfenced></mrow></mrow></mrow></mfenced></math>
<math><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mfrac><mrow><mn>12</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>12</mn><mo>&#215;</mo><mn>3</mn></mrow><mrow><mn>5</mn><mo>&#215;</mo><mn>4</mn></mrow></mfrac></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
<math><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>33</mn></mrow><mrow><mn>56</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
<math><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>33</mn></mrow><mrow><mn>65</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
<math><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>56</mn></mrow><mrow><mn>65</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>56</mn></mrow><mrow><mn>65</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>

</details>

---

### Q25. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><msup><mi>cos</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mi>&#945;</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mi>y</mi><mo>&#8804;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>,</mo></math> then for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mi>y</mi><mi>cos</mi><mi>&#945;</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#945;</mi><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><msup><mi>y</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#945;</mi><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><msup><mi>y</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi mathvariant="normal">&#945;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi mathvariant="normal">&#945;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi mathvariant="normal">&#945;</mi></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>A</mi><mo>-</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>B</mi><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>A</mi><mi>B</mi><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>A</mi><mn>2</mn></msup></msqrt><msqrt><mn>1</mn><mo>-</mo><msup><mi>B</mi><mn>2</mn></msup></msqrt></mrow></mfenced><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mfrac><mrow><mi>x</mi><mi>y</mi></mrow><mn>2</mn></mfrac><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>&#215;</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac></msqrt></mrow></mfenced><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>x</mi><mi>y</mi></mrow><mn>2</mn></mfrac><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>&#215;</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac></msqrt><mo>=</mo><mi>cos</mi><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#945;</mi><mo>-</mo><mfrac><mrow><mi>x</mi><mi>y</mi></mrow><mn>2</mn></mfrac><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>&#215;</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac></msqrt></math></p><p>Squaring both sides, we get
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mn>2</mn></msup><mi>&#945;</mi><mo>+</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>-</mo><mi>x</mi><mi>y</mi><mi>cos</mi><mi>&#945;</mi><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#945;</mi><mo>+</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>-</mo><mi>x</mi><mi>y</mi><mi>cos</mi><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mi>y</mi><mi>cos</mi><mi>&#945;</mi><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mi>y</mi><mi>cos</mi><mi>&#945;</mi><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>=</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mi>y</mi><mi>cos</mi><mi>&#945;</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#945;</mi><mo>.</mo></math></p>

</details>

---

### Q26. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>&#945;</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math> , <math><mi>&#946;</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math> , where <math><mn>0</mn><mo>&#60;</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#60;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo></math> then <math><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></math> is equal to

**Options:**

- **(A)** <math><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>9</mn></mrow><mrow><mn>14</mn></mrow></mfrac></mrow></mfenced></math>
- **(B)** <math><mi mathvariant="normal"> </mi><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>9</mn></mrow><mrow><mn>5</mn><msqrt><mn>10</mn></msqrt></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>9</mn></mrow><mrow><mn>5</mn><msqrt><mn>10</mn></msqrt></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(D)** <math><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>9</mn></mrow><mrow><mn>5</mn><msqrt><mn>10</mn></msqrt></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>9</mn></mrow><mrow><mn>5</mn><msqrt><mn>10</mn></msqrt></mrow></mfrac></mrow></mfenced></mrow></mrow></math>**

**Detailed Solution:**

<p>     <math><mi>&#945;</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mo>&#8756;</mo><mi>a</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfrac></math>
<math><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mn>1</mn></mrow><mrow><mfrac><mrow><mn>13</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>9</mn><mn>13</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced separators="|"><mfrac><mn>9</mn><mrow><mn>5</mn><msqrt><mn>10</mn></msqrt></mrow></mfrac></mfenced></math></p>

</details>

---

### Q27. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Considering only the principal values of inverse functions, the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mi>x</mi><mo>&#8805;</mo><mn>0</mn><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>3</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math>

**Options:**

- **(A)** Is an empty set
- **(B)** Contains more than two elements
- **(C)** Contains two elements
- **(D)** Is a singleton

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Is a singleton**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>3</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi><mo>&#215;</mo><mn>3</mn><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>Applying tangent on both sides,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mfenced close="]" open="["><mrow><mo>&#8757;</mo><mi>tan</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>x</mi><mo>=</mo><mn>1</mn><mo>-</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>-</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p>But, since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math>.</p><p>Hence, <math><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>A</mi></math> has only one element and thus, it is a singleton.</p>

</details>

---

