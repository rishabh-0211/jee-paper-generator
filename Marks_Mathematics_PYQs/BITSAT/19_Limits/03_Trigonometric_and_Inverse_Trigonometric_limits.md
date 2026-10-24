# BITSAT Mathematics - Limits

## Topic 3: Trigonometric and Inverse Trigonometric limits

**Total Questions:** 7

---

### Q1. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Given a real valued function ' $f$ ' such that
$f(x)=\left\{\begin{array}{cc}\frac{\tan ^2\{x\}}{x^2-[x]^2} & \text { for } x\gt0 \\ 1 & \text { for } x=0 \\ \sqrt{\{x\} \cot \{x\}} & \text { for } x \lt 0\end{array}\right.$
then

**Options:**

- **(A)** $\mathrm{LHL}=1$
- **(B)** $\mathrm{RHL}=\sqrt{\cot 1}$
- **(C)** $\lim _{x \rightarrow 0} f(x)$ exist
- **(D)** $\lim _{x \rightarrow 0} f(x)$ does not exists

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\lim _{x \rightarrow 0} f(x)$ does not exists**

**Detailed Solution:**

$\lim _{x \rightarrow 0^{-}} f(x)=\lim _{h \rightarrow 0} \sqrt{\{-h\} \cot \{-h\}}$
$=\lim _{h \rightarrow 0} \sqrt{(1-h) \cot (1-h)}=\sqrt{\cot 1}$
$\lim _{x \rightarrow 0^{+}} f(x)=\lim _{h \rightarrow 0} \frac{\tan ^2\{h\}}{h^2-[h]^2}=\lim _{h \rightarrow 0} \frac{\tan ^2 h}{h^2}=1$
$\therefore \lim _{x \rightarrow 0} f(x)$ does not exist.

</details>

---

### Q2. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x)=\sin x, g(x)=\cos x, h(x)=x^2$ then
$\lim _{x \rightarrow 1} \frac{f(g(h(x)))-f(g(h(1)))}{x-1}=$

**Options:**

- **(A)** $0$
- **(B)** $-2 \sin 1 \cos (\cos 1)$
- **(C)** $\infty$
- **(D)** $-2 \sin 1 \cos 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-2 \sin 1 \cos (\cos 1)$**

**Detailed Solution:**

Given $f(x)=\sin x, g(x)=\cos x, h(x)=x^2$
$\lim _{x \rightarrow 1} \frac{f(g(h(x)))-f(g(h(1)))}{x-1}$
When limit it applied, it gives $\frac{0}{0}$ form, so we apply L'Hospital rule.
$\Rightarrow \lim _{x \rightarrow 1} \frac{\cos \left(\cos x^2\right)\left(-\sin x^2\right)(2 x)-0}{1-0}$
Apply the limit,
$\Rightarrow-2(1) \sin (1) \cos (\cos 1)$
$=-2 \sin (1) \cos (\cos 1)$

</details>

---

### Q3. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `3`

The value of $\lim _{x \rightarrow 0} \frac{1-\cos (1-\cos x)}{x^4}$ is

**Options:**

- **(A)** $\frac{1}{6}$
- **(B)** $\frac{1}{8}$
- **(C)** $\frac{1}{10}$
- **(D)** $\frac{1}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{8}$**

**Detailed Solution:**

$1-\cos (1-\cos x)=2 \sin ^2\left(\frac{1-\cos x}{2}\right)$
$=2 \sin ^2\left(\sin ^2 \frac{x}{2}\right)$
$\therefore \lim _{x \rightarrow 0} \frac{1-\cos (1-\cos x)}{x^4}=\lim _{x \rightarrow 0} \frac{2 \sin ^2\left(\sin ^2 \frac{x}{2}\right)}{x^4}$
$=\lim _{x \rightarrow 0} \frac{2 \sin ^2\left(\sin ^2 \frac{x}{2}\right)}{\left(\sin ^2 \frac{x}{2}\right)^2} \times \frac{\sin ^4 \frac{x}{2}}{\left(\frac{x}{2}\right)^4 \times 16}$
$=\frac{1}{8}$

</details>

---

### Q4. BITSAT 2019

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mi>cos</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mi>cos</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mfenced close="]" open="["><mrow><mo>(</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mo>(</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></munder><mfrac><mrow><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mfenced open="{" close="}"><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></munder><mn>2</mn><mi>sin</mi><mi>x</mi><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q5. BITSAT 2015

*Type:* `singleCorrect` | *Level:* `1`

If $\lim _{x \rightarrow} x \sin \left(\frac{1}{x}\right)=A$ and $\lim _{x \rightarrow 0} x \sin \left(\frac{1}{x}\right)=B$,

then which one of the following is correct?

**Options:**

- **(A)** $A=1$ and $B=0$
- **(B)** $\quad A=0$ and $B=1$
- **(C)** $A=0$ and $B=0$
- **(D)** $A=1$ and $B=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $A=1$ and $B=0$**

**Detailed Solution:**

As given,

$$

\mathrm{A}=\lim _{\mathrm{x} \rightarrow \infty} \mathrm{x} \sin \left(\frac{1}{\mathrm{x}}\right)=\lim _{\mathrm{x} \rightarrow \infty} \frac{\sin \left(\frac{1}{\mathrm{x}}\right)}{\left(\frac{1}{\mathrm{x}}\right)}

$$

Let $\mathrm{t}=\frac{1}{\mathrm{x}}$ when $\mathrm{x} \rightarrow \alpha, \mathrm{t} \rightarrow 0$

$$

\begin{aligned}

\Rightarrow \mathrm{A} &=\lim _{t \rightarrow \infty} \frac{\sin \mathrm{t}}{\mathrm{t}}=1 \\

&\left[\because \lim _{\mathrm{t} \rightarrow 0} \frac{\sin \mathrm{x}}{\mathrm{x}}=1\right]

\end{aligned}

$$

and $\mathrm{B}=\lim _{\mathrm{x} \rightarrow 0} \mathrm{x} \sin \left(\frac{1}{\mathrm{x}}\right)$

$$

\Rightarrow \mathrm{B}=\lim _{\mathrm{x} \rightarrow 0} \mathrm{x} \cdot \lim _{\mathrm{x} \rightarrow 0} \sin \left(\frac{1}{\mathrm{x}}\right)

$$

$$

\Rightarrow \mathrm{B}=0

$$

$\therefore \quad A=1$ and $B=0$ is correct

</details>

---

### Q6. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow \pi / 2} \frac{\left(1-\tan \left(\frac{x}{2}\right)\right)(1-\sin x)}{\left(1+\tan \left(\frac{x}{2}\right)\right)(\pi-2 x)^{3}}=?$

**Options:**

- **(A)** $1 / 8$
- **(B)** 0
- **(C)** $1 / 32$
- **(D)** $\infty$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1 / 32$**

**Detailed Solution:**

Put $x=\frac{\pi}{2}-h$ as $x \rightarrow \frac{\pi}{2}, h \rightarrow 0$
$\therefore$ Given limit
$=\lim _{h \rightarrow 0} \frac{1-\tan \left(\frac{\pi}{4}-\frac{\mathrm{h}}{2}\right)}{1+\tan \left(\frac{\pi}{4}-\frac{\mathrm{h}}{2}\right)} \cdot \frac{(1-\cosh )}{(2 \mathrm{~h})^{3}}$
$=\lim _{\mathrm{h} \rightarrow 0} \tan \frac{\mathrm{h}}{2} \frac{2 \sin ^{2} \frac{\mathrm{h}}{2}}{8 \mathrm{~h}^{3}}$
$=\lim _{\mathrm{h} \rightarrow 0} \frac{1}{4} \cdot \frac{\tan \frac{\mathrm{h}}{2}}{\frac{\mathrm{h}}{2} \times 2}\left(\frac{\sin \frac{\mathrm{h}}{2}}{\frac{\mathrm{h}}{2}}\right)^{2} \times \frac{1}{4}$
$=\lim _{\mathrm{h} \rightarrow 0} \frac{1}{32} \cdot\left(\frac{\tan \frac{\mathrm{h}}{2}}{\frac{\mathrm{h}}{2} \times 2}\right)\left(\frac{\sin \frac{\mathrm{h}}{2}}{\frac{\mathrm{h}}{2}}\right)^{2}=\frac{1}{32}$

</details>

---

### Q7. BITSAT 2011

*Type:* `singleCorrect` | *Level:* `3`

Evaluate \(\lim _{x \rightarrow \infty} \frac{\sqrt{1+\sin 3 x}-1}{\ln (1+\tan 2 x)}\);

**Options:**

- **(A)** \(1 / 2\)
- **(B)** \(3 / 2\)
- **(C)** \(3 / 4\)
- **(D)** \(1 / 4\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) \(3 / 4\)**

**Detailed Solution:**

\(\begin{aligned}
& \lim _{x \rightarrow 0} \frac{\sqrt{1+\sin 3 x}-1}{\ln (1+\tan 2 x)} \\
= & \lim _{x \rightarrow 0} \frac{(1+\sin 3 x)-1}{\{\sqrt{1+\sin 3 x+1}) \ln (1+\tan 2 x)} \\
= & \lim _{x \rightarrow 0} \frac{1}{(\sqrt{1+\sin 3 x}+1)} \cdot \frac{\sin 3 x}{\ln (1+\tan 2 x)^{\frac{1}{\tan 2 x}}\times \frac{1}{\tan 2 x}}
\end{aligned}\)
\(\begin{aligned} & =\lim _{x \rightarrow 0} \frac{1}{(\sqrt{1+\sin 3 x}+1)} \cdot\left(\frac{\sin 3 x}{3 x}\right)\left(\frac{2 x}{\tan 2 x}\right) \\ & \times \frac{3}{\tan 2 x} \cdot \frac{1}{\ln (1+\tan 2 x)^{\frac{1}{\tan 2 x}}} \\ & =\left(\frac{1}{1+1}\right)(1)(1)\left(\frac{3}{2}\right) \frac{1}{\ln e}=\frac{3}{4} .\end{aligned}\)

</details>

---

