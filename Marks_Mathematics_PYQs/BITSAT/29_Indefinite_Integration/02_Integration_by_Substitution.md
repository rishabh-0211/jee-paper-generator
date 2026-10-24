# BITSAT Mathematics - Indefinite Integration

## Topic 2: Integration by Substitution

**Total Questions:** 11

---

### Q1. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int e^{\tan \theta}(\sec \theta-\sin \theta) d \theta$ is

**Options:**

- **(A)** $e^{\tan \theta} \sec \theta+c$
- **(B)** $e^{\tan \theta} \sin \theta+c$
- **(C)** $e^{\tan \theta}(\sec \theta+\sin \theta)+c$
- **(D)** $e^{\tan \theta} \cos \theta+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $e^{\tan \theta} \cos \theta+c$**

**Detailed Solution:**

Let $I=\int e^{\tan \theta}(\sec \theta-\sin \theta) d \theta$
Put $\tan \theta=t \Rightarrow \sec ^2 \theta d \theta=d t \Rightarrow d \theta=\frac{d t}{1+t^2}$
$\Rightarrow I=\int e^t\left(\sqrt{1+t^2}-\frac{t}{\sqrt{1+t^2}}\right) \frac{d t}{1+t^2}$
$=\int e^t\left(\frac{1}{\sqrt{1+t^2}}-\frac{t}{\left(1+t^2\right)^{3 / 2}}\right) d t$
Integrating first part by parts we have,
$=\frac{1}{\sqrt{1+t^2}} e^t+\int \frac{t}{\left(1+t^2\right)^{3 / 2}} \cdot e^t d t$
$-\int \frac{t}{\left(1+t^2\right)^{3 / 2}} e^t d t+c$
$=\frac{e^t}{\sqrt{1+t^2}}+c=e^{\tan \theta} \cos \theta+c$

</details>

---

### Q2. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \sqrt{x+\sqrt{x^2+2}} d x=$

**Options:**

- **(A)** $\frac{3}{2}(x+\sqrt{x+2})^{3 / 2}-2\left(x+\sqrt{x^2+2}\right)^{1 / 4}+C$
- **(B)** $\frac{1}{3}\left(x+\sqrt{x^2+2}\right)^{3 / 2}-2\left(x+\sqrt{x^2+2}\right)^{1 / 4}+C$
- **(C)** $\left(x+\sqrt{x^2+2}\right)^{-3 / 2}-2\left(x+\sqrt{x^2+2}\right)^{-1 / 2}+C$
- **(D)** $\frac{\left(x+\sqrt{x^2+2}\right)^2-6}{3 \sqrt{x+\sqrt{x^2+2}}}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\left(x+\sqrt{x^2+2}\right)^2-6}{3 \sqrt{x+\sqrt{x^2+2}}}+C$**

**Detailed Solution:**

$\int \sqrt{x+\sqrt{x^2+2}} d x$
$\sqrt{x+\sqrt{x^2+2}}=t \Rightarrow x+\sqrt{x^2+2}=t^2$
$\sqrt{x^2+2}=t^2-x$
$\Rightarrow x^2+2=t^4+x^2-2 t^2 x$
$\Rightarrow \mathrm{x}=\frac{\mathrm{t}^4-2}{2 \mathrm{t}^2} \Rightarrow \mathrm{dx}=\frac{\mathrm{t}^4+2}{\mathrm{t}^3} \mathrm{dt}$
$\int \mathrm{t} \cdot \frac{\mathrm{t}^4+2}{\mathrm{t}^3} \mathrm{dt}=\int\left(\mathrm{t}^2+\frac{2}{\mathrm{t}^2}\right) \mathrm{dt}=\frac{\mathrm{t}^3}{3}-\frac{2}{\mathrm{t}}+\mathrm{C}$
$=\frac{t^3}{3}-\frac{2}{t}+C=\frac{t^4-6}{3 t}+C$
$=\frac{\left(x+\sqrt{x^2+2}\right)^2-6}{3 \sqrt{x+\sqrt{x^2+2}}}+C$

</details>

---

### Q3. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Value of $\int \frac{d x}{\sqrt{x(a-x)}}$ is

**Options:**

- **(A)** $2 \sin ^{-1} \sqrt{\frac{x}{a}}+c$
- **(B)** $-2 \sin ^{-1} \sqrt{\frac{x}{a}}+c$
- **(C)** $2 \sin ^{-1} \frac{\sqrt{x}}{a}+c$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \sin ^{-1} \sqrt{\frac{x}{a}}+c$**

**Detailed Solution:**

Let $\mathrm{x}=\mathrm{a} \sin ^2 \theta$
then $d x=2 a \sin \theta \cos \theta d \theta$
$\begin{aligned}
\therefore \quad I & =\int \frac{2 a \sin \theta \cdot \cos \theta}{\sqrt{a \sin ^2 \theta \cdot a \cos ^2 \theta}} d \theta \\
& =2 \int d \theta=2 \theta+c \\
& =2 \sin ^{-1}(\sqrt{x / a})+c
\end{aligned}$

</details>

---

### Q4. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{e^{x}(1+x)}{\cos ^{2}\left(e^{x} x\right)} \mathrm{dx}$ equals

**Options:**

- **(A)** $-\cot \left(e x^{x}\right)+\mathrm{C}$
- **(B)** $\tan \left(x e^{x}\right)+\mathrm{C}$
- **(C)** $\tan \left(e^{x}\right)+\mathrm{C}$
- **(D)** $\cot \left(e^{x}\right)+\mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan \left(x e^{x}\right)+\mathrm{C}$**

**Detailed Solution:**

$\int \frac{e^{x}(1+x)}{\cos ^{2}\left(e^{x} x\right)} \mathrm{dx}$

Let $x e^{x}=t$

$\Rightarrow\left(x e^{x}+e^{x}\right)=\frac{\mathrm{dt}}{\mathrm{dx}}$

$\Rightarrow d x=\frac{\mathrm{dt}}{e^{x}(x+1)}$

$\therefore \int \frac{e^{x}(1+x)}{\cos ^{2}\left(e^{x} x\right)} \mathrm{dx}=\int \frac{e^{x}(1+x)}{\cos ^{2} t} \times \frac{d t}{e^{x}(1+x)}=\int \frac{1}{\cos ^{2} t} \mathrm{dt}=\int \sec ^{2} t \mathrm{dt}=$$\tan t+\mathrm{C}=\tan \left(x e^{x}\right)+\mathrm{C}$

</details>

---

### Q5. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \cos (\log x) \mathrm{d} \mathrm{x}$ is :

**Options:**

- **(A)** $\frac{1}{2}[\sin (\log x)+\cos (\log x)]+C$
- **(B)** $\frac{x}{2}[\sin (\log x)+\cos (\log x)]+C$
- **(C)** $\frac{x}{2}[\sin (\log x)-\cos (\log x)]+C$
- **(D)** $\frac{1}{2}[\sin (\log x)-\cos (\log x)]+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{x}{2}[\sin (\log x)+\cos (\log x)]+C$**

**Detailed Solution:**

Let

\(\mathrm{I}=\int \cos (\log \mathrm{x}) \cdot 1 \mathrm{~d} \mathrm{x} \ldots . . \text { (i) }\)

Use integral by parts,

\(\begin{aligned} &I=\cos (\log x) \cdot x-\int[-\sin (\log x)] \cdot \frac{1}{x} \cdot x d x \\ &=x \cdot \cos (\log x)+\int \sin (\log x) \cdot 1 d x \\ &=x \cdot \cos (\log x)+\left[\sin (\log x) \cdot x-\int \cos (\log x) \cdot \frac{1}{x} \cdot x d x\right]+C \\ &=x \cdot(\log x)+\left[x \sin (\log x)-\int \cos (\log x) d x\right]+C \\ &=x\{\sin (\log x)+\cos (\log x)\}-I+C[f r o m \text { Eq. (i) }] \\ &\Rightarrow I=\frac{x}{2}\{\sin (\log x)+\cos (\log x)\}+C \end{aligned}\)

</details>

---

### Q6. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{\sin x}{\sin (x-\alpha)} \mathrm{d} \mathrm{x}=\mathrm{A} x+\mathrm{B} \log \sin (x-\alpha)+\mathrm{C}$, then value of $(A, B)$ is

**Options:**

- **(A)** $(-\cos \alpha, \sin \alpha)$
- **(B)** $(\cos \alpha, \sin \alpha)$
- **(C)** $(-\sin \alpha, \cos \alpha)$
- **(D)** $(\sin \alpha, \cos \alpha)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\cos \alpha, \sin \alpha)$**

**Detailed Solution:**

$\int \frac{\sin x}{\sin (x-\alpha)} \mathrm{dx}=\int \frac{\sin (x-\alpha+\alpha}{\sin (x-\alpha)} \mathrm{dx}$

$=\int \frac{\sin (x-\alpha) \cos \alpha+\cos (x-\alpha) \sin \alpha}{\sin (x-\alpha)} \mathrm{d} \mathrm{x}$

$=\int\{\cos \alpha+\sin \alpha \cot (x-\alpha)\} \mathrm{d} \mathrm{x}$

$=(\cos \alpha) x+(\sin \alpha) \log \sin (x-\alpha)+\mathrm{C}$

$\therefore \mathrm{A}=\cos \alpha, \mathrm{B}=\sin \alpha$

</details>

---

### Q7. BITSAT 2019

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<p>We have, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><mo>&#8747;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><mo>&#8747;</mo><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>-</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>C</mi></math></p>

</details>

---

### Q8. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `3`

Evaluate: $\int \frac{1}{1+3 \sin ^{2} x+8 \cos ^{2} x} \mathrm{dx}$

**Options:**

- **(A)** $\frac{1}{6} \tan ^{-1}(2 \tan \mathrm{x})+\mathrm{C}$
- **(B)** $\tan ^{-1}(2 \tan \mathrm{x})+\mathrm{C}$
- **(C)** $\frac{1}{6} \tan ^{-1}\left(\frac{2 \tan \mathrm{x}}{3}\right)+\mathrm{C}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{6} \tan ^{-1}\left(\frac{2 \tan \mathrm{x}}{3}\right)+\mathrm{C}$**

**Detailed Solution:**

$\mathrm{I}=\int \frac{1}{1+3 \sin ^{2} \mathrm{x}+8 \cos ^{2} \mathrm{x}} \mathrm{dx}$

Dividing the numerator and denominator by $\cos ^{2} \mathrm{x},$ we get

$$

I=\int \frac{\sec ^{2} x}{\sec ^{2} x+3 \tan ^{2} x+8} d x=\int \frac{\sec ^{2} x}{4 \tan ^{2} x+9} d x

$$

Putting $\tan x=t \Rightarrow \sec ^{2} x d x=d t,$ we get

$\mathrm{I}=\int \frac{\mathrm{dt}}{4 \mathrm{t}^{2}+9}=\frac{1}{4} \int \frac{\mathrm{dt}}{\mathrm{t}^{2}+(3 / 2)^{2}}=\frac{1}{4} \times \frac{1}{3 / 2} \tan ^{-1}\left(\frac{\mathrm{t}}{3 / 2}\right)+\mathrm{C}$

$\Rightarrow \mathrm{I}=\frac{1}{6} \tan ^{-1}\left(\frac{2 \mathrm{t}}{3}\right)+\mathrm{C}=\frac{1}{6} \tan ^{-1}\left(\frac{2 \tan \mathrm{x}}{3}\right)+\mathrm{C}$

</details>

---

### Q9. BITSAT 2013

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{\left(\mathrm{x}^{2}-1\right)}{\left(\mathrm{x}^{2}+1\right) \sqrt{\mathrm{x}^{4}+1}} \mathrm{dx}$ is equal to

**Options:**

- **(A)** $\sec ^{-1}\left(\frac{x^{2}+1}{\sqrt{2} x}\right)+c$
- **(B)** $\frac{1}{\sqrt{2}} \sec ^{-1}\left(\frac{x^{2}+1}{\sqrt{2} x}\right)+c$
- **(C)** $\frac{1}{\sqrt{2}} \sec ^{-1}\left(\frac{x^{2}+1}{\sqrt{2}}\right)+c$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{\sqrt{2}} \sec ^{-1}\left(\frac{x^{2}+1}{\sqrt{2} x}\right)+c$**

**Detailed Solution:**

$\mathrm{I}=\int \frac{\mathrm{x}^{2}\left(1-\frac{1}{\mathrm{x}^{2}}\right) \mathrm{dx}}{\mathrm{x}^{2}\left(\mathrm{x}+\frac{1}{\mathrm{x}}\right)\left(\mathrm{x}^{2}+\frac{1}{\mathrm{x}^{2}}\right)^{1 / 2}}$

Let $\mathrm{x}+\frac{1}{\mathrm{x}}=\mathrm{p} \Rightarrow\left(1-\frac{1}{\mathrm{x}^{2}}\right) \mathrm{d} \mathrm{x}=\mathrm{dp}$

$\mathrm{I}=\int \frac{\mathrm{dp}}{\mathrm{p} \sqrt{\mathrm{p}^{2}-2}}=\frac{1}{\sqrt{2}} \mathrm{sec}^{-1} \frac{\mathrm{p}}{\sqrt{2}}$

$=\frac{1}{\sqrt{2}} \sec ^{-1}\left(\frac{\mathrm{x}^{2}+1}{\sqrt{2} \mathrm{x}}\right)+\mathrm{c}$

</details>

---

### Q10. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `2`

Evaluate: $\int \sqrt{\frac{\mathrm{x}}{4-\mathrm{x}^{3}}} \mathrm{dx}$

**Options:**

- **(A)** $\frac{2}{3} \sin ^{-1}\left(\frac{x^{3 / 2}}{2}\right)+c$
- **(B)** $\frac{2}{3} \sin ^{-1}\left(x^{3 / 2}\right)+c$
- **(C)** $2 \sin ^{-1}\left(\frac{x^{3 / 2}}{2}\right)+c$
- **(D)** $\frac{1}{3} \sin ^{-1}\left(\frac{\mathrm{x}^{3 / 2}}{2}\right)+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2}{3} \sin ^{-1}\left(\frac{x^{3 / 2}}{2}\right)+c$**

**Detailed Solution:**

$I=\int \sqrt{\frac{x}{4-x^{3}}} d x=\int \frac{\sqrt{x} d x}{\sqrt{4-x^{3}}}$
Here integral of $\sqrt{x}=\frac{2}{3} x^{3 / 2}$ and $4-x^{3}=4-\left(x^{3 / 2}\right)^{2}$
Put $x^{3 / 2}=t \Rightarrow \sqrt{x} d x=\frac{2}{3} d t$
So $I=\frac{2}{3} \int \frac{d t}{\sqrt{4-t^{2}}}=\frac{2}{3} \sin ^{-1}\left(\frac{x^{3 / 2}}{2}\right)+c$

</details>

---

### Q11. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `1`

The equation of tangent to the curve \(y=\sin x\) at the point \((\pi, 0)\) is

**Options:**

- **(A)** \(x+y=0\)
- **(B)** \(x+y=\pi\)
- **(C)** \(x-y=\pi\)
- **(D)** \(x-y=0\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) \(x+y=\pi\)**

**Detailed Solution:**

\(y=\sin x \Rightarrow \frac{d y}{d x}=\cos x \Rightarrow\left(\frac{d y}{d x}\right)_{(\pi, 0)}=-1\)
Therefore the equation of tangent at \((\pi, 0)\) is given by
\(y-0=-1(x-\pi) \Rightarrow x+y=\pi\)

</details>

---

