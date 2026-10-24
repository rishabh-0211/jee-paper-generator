# JEE Main Mathematics - Differentiation

## Topic 1: Differentiation of composite functions

**Total Questions:** 26

---

### Q1. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\log _e y=3 \sin ^{-1} x$, then $\left(1-x^2\right) y^{\prime \prime}-x y^{\prime}$ at $x=\frac{1}{2}$ is equal to

**Options:**

- **(A)** $3 e^{\pi / 6}$
- **(B)** $9 e^{\pi / 2}$
- **(C)** $3 e^{\pi / 2}$
- **(D)** $9 e^{\pi / 6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $9 e^{\pi / 2}$**

**Detailed Solution:**

$\begin{aligned} & \ln (y)=3 \sin ^{-1} x \\ & \frac{1}{y} \cdot y^{\prime}=3\left(\frac{1}{\sqrt{1-x^2}}\right) \\ & \Rightarrow y^{\prime}=\frac{3 y}{\sqrt{1-x^2}} \text { at } x=\frac{1}{2} \\ & \Rightarrow y^{\prime}=\frac{3 e^{3\left(\frac{\pi}{6}\right)}}{\frac{\sqrt{3}}{2}}=2 \sqrt{3} e^{\frac{\pi}{2}} \\ & \Rightarrow y^{\prime \prime}=3\left(\frac{\sqrt{1-x^2} y^{\prime}-y \frac{1}{2 \sqrt{1-x^2}}(-2 x)}{\left(1-x^2\right)}\right)\end{aligned}$
$\begin{aligned} & \Rightarrow\left(1-x^2\right) y^{\prime \prime}=3\left(3 y+\frac{x y}{\sqrt{1-x^2}}\right) \\ & \downarrow \text { at } x=\frac{1}{2}, y=e^{3 \sin ^{-1}\left(\frac{1}{2}\right)}=\mathrm{e}^{3\left(\frac{\pi}{6}\right)}=\mathrm{e}^{\frac{\pi}{2}}\end{aligned}$
$\begin{aligned} & \left.\left(1-x^2\right) y^{\prime \prime}\right|_{\text {at } x=\frac{1}{2}}=3\left(3 \mathrm{e}^{\frac{\pi}{2}}+\frac{\frac{1}{2}\left(e^{\frac{\pi}{2}}\right)}{\frac{\sqrt{3}}{2}}\right) \\ & =3 \mathrm{e}^{\frac{\pi}{2}}\left(3+\frac{1}{\sqrt{3}}\right) \\ & \left(1-x^2\right) y^{\prime \prime}-\left.x y^{\prime}\right|_{\text {atx } x=\frac{1}{2}} \\ & =3 \mathrm{e}^{\frac{\pi}{2}}\left(3+\frac{1}{\sqrt{3}}\right)-\frac{1}{2}\left(2 \sqrt{3} \mathrm{e}^{\frac{\pi}{2}}\right)=9 \mathrm{e}^{\frac{\pi}{2}}\end{aligned}$

</details>

---

### Q2. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Suppose for a differentiable function $h, h(0)=0, h(1)=1$ and $h^{\prime}(0)=h^{\prime}(1)=2$. If $\mathrm{g}(x)=h\left(\mathrm{e}^x\right) \mathrm{e}^{h(x)}$, then $g^{\prime}(0)$ is equal to:

**Options:**

- **(A)** 5
- **(B)** 4
- **(C)** 8
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 4**

**Detailed Solution:**

$\begin{aligned} & g(x)=h\left(e^x\right) \cdot e^{h(x)} \\ & g^{\prime}(x)=h\left(e^x\right) \cdot e^{h(x)} \cdot h^{\prime}(x)+e^{h(x)} h^{\prime}\left(e^x\right) \cdot e^x \\ & g^{\prime}(0)=h(1) e^{h(0)} h^{\prime}(0)+e^{h(0)} h^{\prime}(1) \\ & =2+2=4\end{aligned}$

</details>

---

### Q3. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\left\{\begin{array}{l}x^3 \sin \left(\frac{1}{x}\right), x \neq 0 \\ 0 \quad, x=0\end{array}\right.$ then

**Options:**

- **(A)** $f^{\prime \prime}\left(\frac{2}{\pi}\right)=\frac{24-\pi^2}{2 \pi}$
- **(B)** $f^{\prime \prime}\left(\frac{2}{\pi}\right)=\frac{12-\pi^2}{2 \pi}$
- **(C)** $f^{\prime \prime}(0)=1$
- **(D)** $f^{\prime \prime}(0)=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $f^{\prime \prime}\left(\frac{2}{\pi}\right)=\frac{24-\pi^2}{2 \pi}$**

**Detailed Solution:**

$\begin{aligned} & f^{\prime}(x)=3 x^2 \sin \left(\frac{1}{x}\right)-x \cos \left(\frac{1}{x}\right) \\ & f^{\prime \prime}(x)=6 x \sin \left(\frac{1}{x}\right)-3 \cos \left(\frac{1}{x}\right)-\cos \left(\frac{1}{x}\right)-\frac{\sin \left(\frac{1}{x}\right)}{x} \\ & f^{\prime \prime}\left(\frac{2}{\pi}\right)=\frac{12}{\pi}-\frac{\pi}{2}=\frac{24-\pi^2}{2 \pi}\end{aligned}$

</details>

---

### Q4. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)=x^5+2 \mathrm{e}^{x / 4}$ for all $x \in \mathbf{R}$. Consider a function $g(x)$ such that $(g \circ f)(x)=x$ for all $x \in \mathbf{R}$. Then the value of $8 g^{\prime}(2)$ is :

**Options:**

- **(A)** 2
- **(B)** 8
- **(C)** 4
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 16**

**Detailed Solution:**

$\begin{aligned} & f(x)=2 \\ & \text { when } x=0 \\ & \because g^{\prime}(f(x)) f^{\prime}(x)=1 \\ & g^{\prime}(2)=\frac{1}{f^{\prime}(0)} \\ & \because f^{\prime}(x)=5 x^4+\frac{2}{4} e^{x / 4} \\ & g^{\prime}(2)=2 \\ & \text { Ans }=16 \\ & \text { Option (1) }\end{aligned}$

</details>

---

### Q5. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>+</mo><msup><mn>2</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mi>tan</mi><mi>x</mi><msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt></mrow><msup><mfenced><mrow><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>π</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>π</mi></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>π</mi></msqrt></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>+</mo><msup><mn>2</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mi>tan</mi><mi>x</mi><msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt></mrow><msup><mfenced><mrow><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mi>h</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></mrow><mi>h</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfrac><mrow><mfenced><mrow><msup><mn>2</mn><mi>h</mi></msup><mo>+</mo><msup><mn>2</mn><mrow><mo>-</mo><mi>h</mi></mrow></msup></mrow></mfenced><mi>tan</mi><mi>h</mi><msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi>h</mi><mn>2</mn></msup><mo>-</mo><mi>h</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt></mrow><msup><mfenced><mrow><mn>7</mn><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>h</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mo>-</mo><mfrac><mrow><mfenced><mrow><msup><mn>2</mn><mn>0</mn></msup><mo>+</mo><msup><mn>2</mn><mn>0</mn></msup></mrow></mfenced><mi>tan</mi><mn>0</mn><msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>0</mn><mo>-</mo><mn>0</mn><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt></mrow><msup><mfenced><mrow><mn>0</mn><mo>+</mo><mn>0</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac></mrow><mi>h</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><msup><mn>2</mn><mi>h</mi></msup><mo>+</mo><msup><mn>2</mn><mrow><mo>-</mo><mi>h</mi></mrow></msup></mrow></mfenced><mi>tan</mi><mi>h</mi><msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi>h</mi><mn>2</mn></msup><mo>-</mo><mi>h</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt></mrow><mrow><mi>h</mi><msup><mfenced><mrow><mn>7</mn><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>h</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><msup><mn>2</mn><mi>h</mi></msup><mo>+</mo><msup><mn>2</mn><mrow><mo>-</mo><mi>h</mi></mrow></msup></mrow></mfenced><msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi>h</mi><mn>2</mn></msup><mo>-</mo><mi>h</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt></mrow><msup><mfenced><mrow><mn>7</mn><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>h</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><msup><mn>2</mn><mn>0</mn></msup><mo>+</mo><msup><mn>2</mn><mn>0</mn></msup></mrow></mfenced><msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>1</mn></mfenced></msqrt></mrow><msup><mfenced><mrow><mn>0</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><mfenced><mn>2</mn></mfenced><msqrt><mfrac><mi>π</mi><mn>4</mn></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><msqrt><mi>π</mi></msqrt></math></p>

</details>

---

### Q6. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let for a differentiable function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>∞</mo><mo>)</mo><mo>→</mo><mi>R</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>≥</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mi>x</mi><mi>y</mi></mfrac></mfenced><mo>+</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>,</mo><mo>∀</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>∈</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>∞</mo></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><msup><mi>n</mi><mn>2</mn></msup></mfrac></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2890**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>≥</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mi>x</mi><mi>y</mi></mfrac></mfenced><mo>+</mo><mi>x</mi><mo>-</mo><mi>y</mi></math></p><p>Now, taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>h</mi><mo> </mo><mo>&amp;</mo><mo> </mo><mi>y</mi><mo>=</mo><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>≥</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>h</mi></mrow><mi>x</mi></mfrac></mfenced><mo>+</mo><mi>x</mi><mo>+</mo><mi>h</mi><mo>-</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>≥</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>h</mi></mrow><mi>x</mi></mfrac></mfenced><mo>+</mo><mi>h</mi></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mi>h</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>h</mi></mrow><mi>x</mi></mfrac></mfenced><mo>+</mo><mi>h</mi></mrow><mi>h</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi>h</mi><mi>x</mi></mfrac></mrow></mfenced></mrow><mrow><mi>x</mi><mo>·</mo><mfenced><mstyle displaystyle="true"><mfrac><mi>h</mi><mi>x</mi></mfrac></mstyle></mfenced></mrow></mfrac><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><munderover><mo>∑</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><munderover><mo>∑</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>20</mn><mo>×</mo><mn>21</mn><mo>×</mo><mn>41</mn></mrow><mn>6</mn></mfrac><mo>+</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mn>2870</mn><mo>+</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mn>2890</mn></math></p>

</details>

---

### Q7. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mn>3</mn></msup><mfenced><mrow><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mfenced><mrow><mi>cos</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><msup><mfenced><mrow><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mrow></mfenced></mrow></mfenced></mrow></mfenced></math>. Then, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>,</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>y</mi><mo>'</mo></msup><mo>+</mo><msqrt><mn>3</mn></msqrt><msup><mi>&#960;</mi><mn>2</mn></msup><mi>y</mi><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>y</mi><mo>'</mo></msup><mo>+</mo><mn>3</mn><msup><mi>&#960;</mi><mn>2</mn></msup><mi>y</mi><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><msup><mi>y</mi><mo>'</mo></msup><mo>-</mo><mn>3</mn><msup><mi>&#960;</mi><mn>2</mn></msup><mi>y</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>'</mo></msup><mo>+</mo><mn>3</mn><msup><mi>&#960;</mi><mn>2</mn></msup><mi>y</mi><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>y</mi><mo>'</mo></msup><mo>+</mo><mn>3</mn><msup><mi>&#960;</mi><mn>2</mn></msup><mi>y</mi><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>The given equation can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>sin</mi><mn>3</mn></msup><mfenced><mrow><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mi>cos</mi><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> </p><p>where,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><msup><mfenced><mrow><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><msup><mfenced><mrow><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mfenced><mrow><mo>-</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>10</mn><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mrow><mi>&#960;</mi><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mi mathvariant="normal">&#960;</mi></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>&#39;</mo></msup><mo>=</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mi>cos</mi><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#215;</mo><mi>cos</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mi>cos</mi><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>&#215;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mfenced><mrow><mo>-</mo><mi>sin</mi><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mo>&#183;</mo><mi>cos</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>&#183;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mfenced><mrow><mo>-</mo><mi>sin</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#183;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mfenced><mfrac><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></mfenced><mfenced><mrow><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><msup><mi>&#960;</mi><mn>2</mn></msup></mrow><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><msup><mi>sin</mi><mn>3</mn></msup><mfenced><mrow><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mi>cos</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>y</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>3</mn><msup><mi>&#960;</mi><mn>2</mn></msup><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q8. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mi>y</mi><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math> then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>'</mo><mo>'</mo><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>y</mi><mo>'</mo><mo>(</mo><mn>0</mn><mo>)</mo></mrow></mfenced><mo>+</mo><mfenced open="|" close="|"><mrow><mi>y</mi><mo>&#34;</mo><mo>(</mo><mn>0</mn><mo>)</mo></mrow></mfenced><mo>=</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>y</mi><mo>&#34;</mo><mo>(</mo><mn>0</mn><mo>)</mo></mrow></mfenced><mo>=</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>y</mi><mo>'</mo><mo>(</mo><mn>0</mn><mo>)</mo></mrow></mfenced><mo>+</mo><mfenced open="|" close="|"><mrow><mi>y</mi><mo>&#34;</mo><mo>(</mo><mn>0</mn><mo>)</mo></mrow></mfenced><mo>=</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>y</mi><mo>&#34;</mo><mo>(</mo><mn>0</mn><mo>)</mo></mrow></mfenced><mo>=</mo><mn>2</mn></math>**

**Detailed Solution:**

<p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mi>y</mi></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mo>&#183;</mo><mi>y</mi><mo>&#39;</mo><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>&#183;</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mfenced><mrow><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi>y</mi><mo>&#39;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>y</mi><mo>&#183;</mo><mi>y</mi><mo>&#39;</mo><mo>-</mo><mn>2</mn><mi>tan</mi><mi>x</mi><mo>=</mo><mi>y</mi><mo>&#39;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#39;</mo><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#38;</mo><mi>y</mi><mo>=</mo><mn>1</mn></math>.</p><p>Differentiating <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mo>&#183;</mo><mi>y</mi><mo>&#39;</mo><mo>&#39;</mo><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mi>y</mi><mo>&#39;</mo></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>s</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mi>y</mi><mo>&#39;</mo><mo>&#39;</mo></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><mo>-</mo><mn>2</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>2</mn></math>, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced close="|" open="|"><mrow><mi>y</mi><mo>&#39;</mo><mo>&#39;</mo><mfenced><mn>0</mn></mfenced></mrow></mfenced><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q9. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>f</mi></math> be any function continuous on <math><mfenced close="]" open="[" separators="|"><mrow><mi>a</mi><mo>,</mo><mi></mi><mi>b</mi></mrow></mfenced></math> and twice differentiable on <math><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> . If all <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#60;</mo><mn>0</mn><mi></mi></math> , then for any <math><mi>c</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>c</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>a</mi></mrow></mfenced></mrow><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>b</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>c</mi></mrow></mfenced></mrow></mfrac></math>

**Options:**

- **(A)** <math><mfrac><mrow><mi>b</mi><mo>+</mo><mi>a</mi></mrow><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfrac></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** <math><mfrac><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow><mrow><mi>c</mi><mo>-</mo><mi>a</mi></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>c</mi><mo>-</mo><mi>a</mi></mrow><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mi>c</mi><mo>-</mo><mi>a</mi></mrow><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let&rsquo;s use LMVT for <math><mi>x</mi><mi></mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mi>a</mi><mo>,</mo><mi></mi><mi>c</mi></mrow></mfenced></math></p><p><math><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>c</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mo>(</mo><mi>a</mi><mo>)</mo></mrow><mrow><mi>c</mi><mo>-</mo><mi>a</mi></mrow></mfrac><mo>=</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>&#945;</mi></mrow></mfenced><mo>,</mo><mi></mi><mi>&#945;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mi>a</mi><mi></mi><mo>,</mo><mi>c</mi></mrow></mfenced></math></p><p>Also use LMVT for <math><mi>x</mi><mi></mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mi>c</mi><mi></mi><mo>,</mo><mi></mi><mi>b</mi></mrow></mfenced></math></p><p><math><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>b</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mo>(</mo><mi>c</mi><mo>)</mo></mrow><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfrac><mo>=</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>&#946;</mi></mrow></mfenced><mo>,</mo><mi></mi><mi>&#946;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mi>c</mi><mi></mi><mo>,</mo><mi></mi><mi>b</mi></mrow></mfenced></math></p><p><math><mo>&#8757;</mo><mi></mi><mi></mi><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#60;</mo><mn>0</mn><mi></mi><mo>&#8658;</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is decreasing</p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>&#945;</mi></mrow></mfenced><mo>&#62;</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>&#946;</mi></mrow></mfenced></math></p><p><math><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>c</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mo>(</mo><mi>a</mi><mo>)</mo></mrow><mrow><mi>c</mi><mo>-</mo><mi>a</mi></mrow></mfrac><mo>&#62;</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>b</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mo>(</mo><mi>c</mi><mo>)</mo></mrow><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfrac></math></p><p><math><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>c</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mo>(</mo><mi>a</mi><mo>)</mo></mrow><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>b</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mo>(</mo><mi>c</mi><mo>)</mo></mrow></mfrac><mo>&#62;</mo><mfrac><mrow><mi>c</mi><mo>-</mo><mi>a</mi></mrow><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfrac><mi></mi></math> ( <math><mo>&#8757;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is increasing)</p>

</details>

---

### Q10. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mi>&#945;</mi></mfenced><mo>=</mo><msqrt><mn>2</mn><mfenced separators="|"><mfrac><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>&#945;</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">t</mi><mi>&#945;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mn>2</mn></msup><mi>&#945;</mi></mrow></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mi mathvariant="normal">n</mi><mn>2</mn></msup><mi>&#945;</mi></mrow></mfrac></msqrt><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>&#945;</mi></mrow></mfrac></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

Simplifying using Trigonometric Identity, we get,<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mn>1</mn><mo>+</mo><mi>cot</mi><mfenced><mi>&#945;</mi></mfenced></mrow></mfenced></math></p><p>or, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><mo>-</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cot</mi><mfenced><mi>&#945;</mi></mfenced></mrow></mfenced></math>, as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mi>cos</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><menclose notation="right"><mo>&#8756;</mo><mo>&#160;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>&#945;</mi></mrow></mfrac></menclose><mrow><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mrow></msub><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q11. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><msup><mi>f</mi><mi>&#39;</mi></msup><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>3</mn></math>, then the derivative of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>+</mo><msup><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mn>2</mn></msup></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>+</mo><msup><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mn>2</mn></msup></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>&#215;</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mo>&#215;</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>&#215;</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mfenced separators="|"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow></msub><mo>=</mo><mi>f</mi><mi>'</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced></mrow></mfenced></mrow></mfenced><mo>&#215;</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced></mrow></mfenced><mo>&#215;</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mn>1</mn></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>&#215;</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced></mrow></mfenced><mo>&#215;</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mn>1</mn></mfenced><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mn>1</mn></mfenced><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>27</mn><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>33</mn></math></p>

</details>

---

### Q12. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>f</mi></math> be a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> for all <math><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced></math> is equal to :

**Options:**

- **(A)** <math><mn>4</mn><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(B)** <math><mn>2</mn><mi>e</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mn>4</mn><mi>e</mi></math>
- **(D)** <math><mn>2</mn><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mn>4</mn><mi>e</mi></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>h</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mo>.</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>h</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mo>.</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math> (as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math>) </p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced></mrow><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p>Integrating both sides with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced close="|" open="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>k</mi><mo>.</mo><msup><mi>e</mi><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>2</mn><mi>e</mi></mfrac><mo>.</mo><mi>&#160;</mi><msup><mi>e</mi><mi>x</mi></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced><mo>&#160;</mo><mo>&#160;</mo><mfenced close="]" open="["><mrow><mo>&#8757;</mo><mo>&#160;</mo><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></mrow></mfenced></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mo>'</mo></msup><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced><mo>.</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>.</mo><mn>2</mn><mo>=</mo><mn>2</mn><mo>.</mo><mfrac><mn>2</mn><mi>e</mi></mfrac><msup><mi>e</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>e</mi></math> (using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>)</p>

</details>

---

### Q13. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\sin ^{-1}\left(\frac{2 \times 3^x}{1+9^x}\right)$, then $f^{\prime}\left(-\frac{1}{2}\right)$ equals.

**Options:**

- **(A)** $\sqrt{3} \log _e \sqrt{3}$
- **(B)** $-\sqrt{3} \log _e \sqrt{3}$
- **(C)** $-\sqrt{3} \log _e 3$
- **(D)** $\sqrt{3} \log _e 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{3} \log _e \sqrt{3}$**

**Detailed Solution:**

Since $f(x)=\sin \left(\frac{2 \times 3^x}{1+9^x}\right)$
Suppose $3^x=\tan t$
$$
\begin{aligned}
&\Rightarrow f(x)=\sin ^{-1}\left(\frac{2 \tan t}{1+\tan ^2 t}\right) \\
&=\sin ^{-1}(\sin 2 t)=2 t=2 \tan ^{-1}(3 x) \\
&\text { So, } f^{\prime}(x)=\frac{2}{1+\left(3^x\right)^2} \times 3^x \cdot \log _e 3 \\
&\therefore \quad f^{\prime}\left(-\frac{1}{2}\right)=\frac{2}{1+\left(3^{-\frac{1}{2}}\right)^2} \times 3^{-\frac{1}{2}} \cdot \log _e 3 \\
&=\frac{1}{2} \times \sqrt{3} \times \log _e 3=\sqrt{3} \times \log _e \sqrt{3}
\end{aligned}
$$

</details>

---

### Q14. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mn>2</mn><mi>x</mi><mo>=</mo><msup><mrow><mi>y</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>&#955;</mi><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>k</mi><mi>y</mi><mo>=</mo><mn>0</mn></math>, then <math><mi>&#955;</mi><mo>+</mo><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math><mn>26</mn></math>
- **(B)** <math><mo>-</mo><mn>24</mn></math>
- **(C)** <math><mo>-</mo><mn>23</mn></math>
- **(D)** <math><mo>-</mo><mn>26</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mo>-</mo><mn>24</mn></math>**

**Detailed Solution:**

<p>Given <math><msup><mrow><mi>y</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></msup><mo>=</mo><mn>2</mn><mi>x</mi></math>

<math><mo>&#8658;</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><msup><mrow><mi>y</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><msup><mrow><mi>y</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>&#160;</mi></math>

<math><mo>&#8658;</mo><msup><mrow><mi>y</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><msup><mrow><mi>y</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></msup><mo>-</mo><msup><mrow><mi>y</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></msup></mrow></mfenced><mo>=</mo><mn>10</mn><mi>y</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mi>&#8242;</mi></msup><mi>&#160;</mi><mfenced separators="|"><mrow><mn>2</mn><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mo>=</mo><mn>10</mn><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mi>&#8242;</mi></msup><mi>&#160;</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt><mo>=</mo><mn>5</mn><mi>y</mi></math>

Differentiating again

<math><msup><mrow><mi>y</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mn>2</mn><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mn>2</mn><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>2</mn><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac><mo>=10y&#39;</mo></math>

<math><mo>&#8658;</mo><msup><mrow><mi>y</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>x</mi><msup><mrow><mi>y</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mo>=</mo><mn>5</mn><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt><mi>&#160;</mi><mfenced separators="|"><mrow><msup><mrow><mi>y</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup></mrow></mfenced></math>

<math><mo>&#8658;</mo><msup><mrow><mi>y</mi></mrow><mrow><mi>&#8242;</mi><mi>&#8242;</mi></mrow></msup><mi>&#160;</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>x</mi><msup><mrow><mi>y</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mo>-</mo><mn>25</mn><mi>y</mi><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>k</mi><mo>=</mo><mo>-</mo><mn>25</mn></math></p>

</details>

---

### Q15. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mfenced open="[" close="]" separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>15</mn></msup><mo>+</mo><msup><mfenced open="[" close="]" separators="|"><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>15</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>224</mn><mi>&#160;</mi><msup><mi>y</mi><mn>2</mn></msup></math>
- **(B)** <math><mn>125</mn><mi> </mi><mi>y</mi></math>
- **(C)** <math><mn>225</mn><mi> </mi><mi>y</mi></math>
- **(D)** <math><mn>225</mn><mi> </mi><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>225</mn><mi> </mi><mi>y</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mfenced close="}" open="{" separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>15</mn></msup><mo>+</mo><msup><mfenced close="}" open="{" separators="|"><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>15</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>15</mn><msup><mfenced close="}" open="{" separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>14</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfrac></mrow></mfenced><mo>+</mo><mn>15</mn><msup><mfenced close="}" open="{" separators="|"><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>14</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>x</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>15</mn><msup><mfenced close="}" open="{" separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>14</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfrac></mfenced><mo>+</mo><mn>15</mn><msup><mfenced close="}" open="{" separators="|"><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>14</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>15</mn><mfenced open="[" close="]"><mrow><msup><mfenced open="{" close="}" separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>15</mn></msup><mo>-</mo><msup><mfenced open="{" close="}" separators="|"><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>15</mn></msup></mrow></mfenced></mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfrac></math>

<math> <mo>&#8658;</mo> </math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt><mi>&#160;</mi><mo>.</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>15</mn><mfenced open="[" close="]"><mrow><msup><mfenced open="{" close="}" separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>15</mn></msup><mo>-</mo><msup><mfenced open="{" close="}" separators="|"><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>15</mn></msup></mrow></mfenced></math>

<math> <mo>&#8658;</mo> </math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfrac><mi>&#160;</mi><mo>.</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>&#160;</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>15</mn><mo>&#215;</mo><mfrac><mrow><mn>15</mn><mi>y</mi></mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfrac></math>

<math> <mo>&#8658;</mo> </math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>y</mi><mi>&#160;</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>15</mn><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt><mo>&#215;</mo><mfrac><mrow><mn>15</mn><mi>y</mi></mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfrac><mo>=</mo><mn>225</mn><mi>y</mi></math></p>

</details>

---

### Q16. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let $f$ and $g$ be two differentiable functions on $R$ such that $f^{\prime}(x)>0$ and $g^{\prime}(x) < 0$ for all $x \in R$. Then for all $\mathrm{x}$ :

**Options:**

- **(A)** $f(g(x))>f(g(x-1))$
- **(B)** $f(g(x))>f(g(x+1))$
- **(C)** $g(f(x))>g(f(x-1))$
- **(D)** $g(f(x)) < g(f(x+1))$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $f(g(x))>f(g(x+1))$**

**Detailed Solution:**

Since $f^{\prime}(x)>0$ and $g^{\prime}(x) < 0$, therefore $f(x)$ is increasing function and $g(x)$ is decreasing function.
$\Rightarrow f(x+1)>f(x)$ and $g(x+1) < g(x)$
$\Rightarrow g[f(x+1)] < g[f(x)]$ and $f[g(x+$
1) $] < f[g(x)]$
Hence option (b) is correct.

</details>

---

### Q17. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>e</mi><mrow><mi>n</mi><mi>x</mi></mrow></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>.</mo><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mi>d</mi><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></math>  is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>n</mi><mi>x</mi></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>n</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>n</mi><mi>x</mi></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><msup><mi>e</mi><mrow><mi>n</mi><mi>x</mi></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>n</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>n</mi><mi>x</mi></mrow></msup></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>e</mi><mrow><mi>n</mi><mi>x</mi></mrow></msup><mo>&#160;&#8658;&#160;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>n</mi><msup><mi>e</mi><mrow><mi>n</mi><mi>x</mi></mrow></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>&#8757;</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><msup><mi>e</mi><mrow><mi>a</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>a</mi><msup><mi>e</mi><mrow><mi>a</mi><mi>x</mi></mrow></msup></mrow></mfenced></math>

    <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;</mo><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><msup><mi>n</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mi>n</mi><mi>x</mi></mrow></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>n</mi><msup><mi>e</mi><mrow><mi>n</mi><mi>x</mi></mrow></msup><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mi>n</mi><msup><mi>e</mi><mrow><mi>n</mi><mi>x</mi></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>n</mi><mi>x</mi></mrow></msup></math>

           <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mi>d</mi><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mfenced><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac></mfenced></math>

             <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac></mfenced><mo>&#183;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac></math>

               <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>n</mi><mi>x</mi></mrow></msup></mrow></mfenced><mo>&#183;</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>n</mi><mi>x</mi></mrow></msup><mi>n</mi></mfrac></math>

               <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><mfenced><mrow><mo>-</mo><mi>n</mi></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>n</mi><mi>x</mi></mrow></msup><mo>&#183;</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>n</mi><mi>x</mi></mrow></msup><mi>n</mi></mfrac></math>

               <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>n</mi><mi>x</mi></mrow></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;&#160;</mo><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>.</mo><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mi>d</mi><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><msup><mi>n</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mi>n</mi><mi>x</mi></mrow></msup><mo>&#215;</mo><mfenced><mfrac><mrow><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>n</mi><mi>x</mi></mrow></msup></mrow><mi>n</mi></mfrac></mfenced></math>

                       <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mi>n</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>n</mi><mi>x</mi></mrow></msup></math>

</details>

---

### Q18. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\sin (\sin x)$ and $f^{\prime \prime}(x)+\tan x f^{\prime}(x)+g(x)$ $=0$, then $g(x)$ is :

**Options:**

- **(A)** $\cos ^2 x \cos (\sin x)$
- **(B)** $\sin ^2 x \cos (\cos x)$
- **(C)** $\sin ^2 x \sin (\cos x)$
- **(D)** $\cos ^2 x \sin (\sin x)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\cos ^2 x \sin (\sin x)$**

**Detailed Solution:**

$$
\begin{aligned}
& \text { } f(x)=\sin (\sin x) \\
& \Rightarrow f^{\prime}(x)=\cos (\sin x) \cdot \cos x \\
& \Rightarrow f^{\prime \prime}(x)=-\sin (\sin x) \cdot \cos ^2 x+\cos (\sin x) \text {. } \\
& (-\sin x) \\
& =-\cos ^2 x \cdot \sin (\sin x)-\sin x \cdot \cos (\sin x) \\
& \text { Now } f^{\prime \prime}(x)+\tan x . f^{\prime}(x)+g(x)=0 \\
& \Rightarrow g(x)=\cos ^2 x \cdot \sin (\sin x)+\sin x \cdot \cos (\sin x) \\
& -\tan x \cdot \cos x \cdot \cos (\sin x) \\
& \Rightarrow g(x)=\cos ^2 x \cdot \sin (\sin x) \text {. } \\
&
\end{aligned}
$$

</details>

---

### Q19. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

For $a>0, t \in\left(0, \frac{\pi}{2}\right)$, let $x=\sqrt{a^{\sin ^{-1} t}}$ and $y=\sqrt{a^{\cos ^{-1} t}}$, Then, $1+\left(\frac{d y}{d x}\right)^2$ equals :

**Options:**

- **(A)** $\frac{x^2}{y^2}$
- **(B)** $\frac{y^2}{x^2}$
- **(C)** $\frac{x^2+y^2}{y^2}$
- **(D)** $\frac{x^2+y^2}{x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{x^2+y^2}{x^2}$**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Let } x=\sqrt{a^{\sin ^{-1} t}} \\
& \Rightarrow \quad x^2=a^{\sin ^{-1} t} \Rightarrow 2 \log x=\sin ^{-1} t \cdot \log a \\
& \Rightarrow \quad \frac{2}{x}=\frac{\log a}{\sqrt{1-t^2}} \cdot \frac{d t}{d x} \\
& \Rightarrow \quad \frac{2 \sqrt{1-t^2}}{x \log a}=\frac{d t}{d x}
\end{aligned}
$$
Now, let $y=\sqrt{a^{\cos ^{-1} t}}$
$$
\begin{aligned}
& \Rightarrow 2 \log y=\cos ^{-1} t \cdot \log a \\
& \Rightarrow \quad \frac{2}{y} \cdot \frac{d y}{d x}=\frac{-\log a}{\sqrt{1-t^2}} \cdot \frac{d t}{d x}
\end{aligned}
$$
$\Rightarrow \frac{2}{y} \cdot \frac{d y}{d x}=\frac{-\log a}{\sqrt{1-t^2}} \times \frac{2 \sqrt{1-t^2}}{x \log a} \quad$ (from(1)
$$
\Rightarrow \frac{d y}{d x}=-\frac{y}{x}
$$
Hence, $1+\left(\frac{d y}{d x}\right)^2=1+\left(\frac{-y}{x}\right)^2=\frac{x^2+y^2}{x^2}$

</details>

---

### Q20. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `3`

If $f^{\prime}(x)=\sin (\log x)$ and $y=f\left(\frac{2 x+3}{3-2 x}\right)$, then $\frac{d y}{d x}$ equals

**Options:**

- **(A)** $\sin \left[\log \left(\frac{2 x+3}{3-2 x}\right)\right]$
- **(B)** $\frac{12}{\left(3-2 x^2\right)}$
- **(C)** $\frac{12}{\left(3-2 x^2\right)} \sin \left[\log \left(\frac{2 x+3}{3-2 x}\right)\right]$
- **(D)** $\frac{12}{\left(3-2 x^2\right.} \cos \left[\log \left(\frac{2 x+3}{3-2 x}\right)\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{12}{\left(3-2 x^2\right)} \sin \left[\log \left(\frac{2 x+3}{3-2 x}\right)\right]$**

**Detailed Solution:**

Let $f^{\prime}(x)=\sin [\log x]$ and $y=f\left(\frac{2 x+3}{3-2 x}\right)$
Now, $\frac{d y}{d x}=f^{\prime}\left(\frac{2 x+3}{3-2 x}\right) \cdot \frac{d}{d x}\left(\frac{2 x+3}{3-2 x}\right)$
$$
\begin{aligned}
& =\sin \left[\log \left(\frac{2 x+3}{3-2 x}\right)\right] \frac{[(6-4 x-)-4 x-6]}{\left(3-2 x^2\right)} \\
& =\frac{12}{\left(3-2 x^2\right.} \cdot \sin \left[\log \left(\frac{2 x+3}{3-2 x}\right)\right]
\end{aligned}
$$

</details>

---

### Q21. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `3`

$\frac{d^2 x}{d y^2}$ equals

**Options:**

- **(A)** $-\left(\frac{d^2 y}{d x^2}\right)^{-1}\left(\frac{d y}{d x}\right)^{-3}$
- **(B)** $\left(\frac{d^2 y}{d x^2}\right)\left(\frac{d y}{d x}\right)^{-2}$
- **(C)** $-\left(\frac{d^2 y}{d x^2}\right)\left(\frac{d y}{d x}\right)^{-3}$
- **(D)** $\left(\frac{d^2 y}{d x^2}\right)^{-1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\left(\frac{d^2 y}{d x^2}\right)\left(\frac{d y}{d x}\right)^{-3}$**

**Detailed Solution:**

$\frac{d}{d y}\left(\frac{d x}{d y}\right)=\frac{d}{d y}\left(\frac{1}{\left(\frac{d y}{d x}\right)}\right)=-\frac{1}{\left(\frac{d y}{d x}\right)^2} \frac{d}{d y}\left(\frac{d y}{d x}\right)^2$
$=-\left(\frac{d y}{d x}\right)^{-2} \frac{1}{\left(\frac{d y}{d x}\right)} \frac{d}{d x}\left(\frac{d y}{d x}\right)=-\left(\frac{d^2 y}{d x^2}\right)\left(\frac{d y}{d x}\right)^{-3}$

</details>

---

### Q22. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `3`

Let $f:(-1,1) \rightarrow R$ be a differentiable function with $f(0)=-1$ and $f^{\prime}(0)=1$. Let $g(x)=[f(2 f(x)+2)]^2$. Then $g^{\prime}(0)=$

**Options:**

- **(A)** $-4$
- **(B)** 0
- **(C)** $-2$
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-4$**

**Detailed Solution:**

No Solution Available

</details>

---

### Q23. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `3`

If $x^m \cdot y^n=(x+y)^{m+n}$, then $\frac{d y}{d x}$ is

**Options:**

- **(A)** $\frac{y}{x}$
- **(B)** $\frac{x+y}{x y}$
- **(C)** xy
- **(D)** $\frac{x}{y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{y}{x}$**

**Detailed Solution:**

$x^m \cdot y^n=(x+y)^{m+n} \Rightarrow m \ln x+n \ln y=(m+n) \ln (x+y)$
$\therefore \frac{m}{x}+\frac{n}{y} \frac{d y}{d x}=\frac{m+n}{x+y}\left(1+\frac{d y}{d x}\right) \Rightarrow\left(\frac{m}{x}-\frac{m+n}{x+y}\right)=\left(\frac{m+n}{x+y}-\frac{n}{y}\right) \frac{d y}{d x}$
$\quad \frac{m y-n x}{x(x+y)}=\left(\frac{m y-n x}{y(x+y)}\right) \frac{d y}{d x} \Rightarrow \frac{d y}{d x}=\frac{y}{x}$

</details>

---

### Q24. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

Suppose $f(x)$ is differentiable $x=1$ and $\lim _{h \rightarrow 0} \frac{1}{h} f(1+h)=5$, then $f^{\prime}(1)$ equals

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 5
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5**

**Detailed Solution:**

$f^{\prime}(1)=\lim _{h \rightarrow 0} \frac{f(1+h)-f(1)}{h}$; As function is differentiable so it is continuous as it is given that $\lim _{h \rightarrow 0} \frac{f(1+h)}{h}=5$ and hence $f(1)=0$
Hence $f^{\prime}(1)=\lim _{h \rightarrow 0} \frac{f(1+h)}{h}=5$
Hence (C) is the correct answer.

</details>

---

### Q25. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

If $x=e^{y+e^{y+. .10 \infty}}, x>0$, then $\frac{d y}{d x}$ is

**Options:**

- **(A)** $\frac{\mathrm{x}}{1+\mathrm{x}}$
- **(B)** $\frac{1}{x}$
- **(C)** $\frac{1-x}{x}$
- **(D)** $\frac{1+x}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1-x}{x}$**

**Detailed Solution:**

$x=e^{y+e^{y+e^{y+\ldots \ldots \infty}}} \Rightarrow x=e^{y+x}$
$\Rightarrow \ln x-x=y \Rightarrow \frac{d y}{d x}=\frac{1}{x}-1=\frac{1-x}{x}$

</details>

---

### Q26. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

If $y=\left(x+\sqrt{1+x^2}\right)^n$, then $\left(1+x^2\right) \frac{d^2 y}{d x^2}+x \frac{d y}{d x}$ is

**Options:**

- **(A)** $\mathrm{n}^2 \mathrm{y}$
- **(B)** $-n^2 y$
- **(C)** $-y$
- **(D)** $2 x^2 y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{n}^2 \mathrm{y}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Lppg6wMWIwQE6sWL6_NTaE7tMOHGkYUfuRLYCd_Yavs.original.fullsize.png">

</details>

---

