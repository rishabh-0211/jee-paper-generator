# JEE Main Mathematics - Indefinite Integration

## Topic 2: Integration by Parts

**Total Questions:** 16

---

### Q1. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(t)=\int\left(\frac{1-\sin \left(\log _{e} t\right)}{1-\cos \left(\log _{e} t\right)}\right) d t, t>1$. 
 If $f\left(e^{\pi / 2}\right)=-e^{\pi / 2}$ and $f\left(e^{\pi / 4}\right)=\alpha e^{\pi / 4}$, then $\alpha$ equals

**Options:**

- **(A)** $1+\sqrt{2}$
- **(B)** $-1-\sqrt{2}$
- **(C)** $-1-2 \sqrt{2}$
- **(D)** $-1+\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-1-\sqrt{2}$**

**Detailed Solution:**

Substituting $u = \log t$ with $dt = e^u du$:
$f(t) = \int \frac{1 - \sin u}{1 - \cos u} e^u du$
Express as: $\frac{1 - \sin u}{1 - \cos u} = \frac{1}{2}\csc^2(u/2) - \cot(u/2)$
Using integration by parts and standard techniques:
$f(t) = e^{\log t}\cot(\frac{\log t}{2}) + C = t\cot(\frac{\log t}{2}) + C$
From $f(e^{\pi/2}) = -e^{\pi/2}$:
$e^{\pi/2}\cot(\pi/4) + C = -e^{\pi/2}$ → $e^{\pi/2} + C = -e^{\pi/2}$ → $C = -2e^{\pi/2}$
For $f(e^{\pi/4})$: $f(e^{\pi/4}) = e^{\pi/4}\cot(\pi/8) - 2e^{\pi/2}$
With $\cot(\pi/8) = 1 + \sqrt{2}$: $\alpha = -1 - \sqrt{2}$

</details>

---

### Q2. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=\int \frac{\left(2-x^{2}\right) \cdot \mathrm{e}^{x}}{(\sqrt{1+x})(1-x)^{3 / 2}} \mathrm{~d} x$. If $f(0)=0$, then $f\left(\frac{1}{2}\right)$ is equal to:

**Options:**

- **(A)** $\sqrt{3 \mathrm{e}}-1$
- **(B)** $\sqrt{3 \mathrm{e}}+1$
- **(C)** $\sqrt{2 \mathrm{e}}+1$
- **(D)** $\sqrt{2 \mathrm{e}}-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{3 \mathrm{e}}-1$**

**Detailed Solution:**

Write $2 - x^2 = (1-x)(1+x) + 1$, so the integrand splits as $e^x\left(\sqrt{\frac{1+x}{1-x}} + \frac{1}{\sqrt{1+x}(1-x)^{3/2}}\right)$.
Let $g(x) = \sqrt{\frac{1+x}{1-x}}$. Then $g'(x) = \frac{1}{\sqrt{1+x}(1-x)^{3/2}}$.
Using $\int e^x(g + g')dx = e^x g + C$: $f(x) = e^x\sqrt{\frac{1+x}{1-x}} + C$.
$f(0) = 1 + C = 0 \Rightarrow C = -1$.
$f(1/2) = e^{1/2}\sqrt{\frac{3/2}{1/2}} - 1 = \sqrt{e}\cdot\sqrt{3} - 1 = \sqrt{3e} - 1$.

</details>

---

### Q3. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\int x^3 \sin x \mathrm{~d} x=g(x)+C$, where $C$ is the constant of integration. If $8\left(g\left(\frac{\pi}{2}\right)+g^{\prime}\left(\frac{\pi}{2}\right)\right)=\alpha \pi^3+\beta \pi^2+\gamma, \alpha, \beta, \gamma \in Z$, then $\alpha+\beta-\gamma$ equals :

**Options:**

- **(A)** 48
- **(B)** 55
- **(C)** 62
- **(D)** 47

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 55**

**Detailed Solution:**

$\begin{aligned}
& \int x^3 \sin x d x=-x^3 \cos x+\int 3 x^2 \cos x d x \\
& =-x^3 \cos x+3 x^2 \sin x-\int 6 x \sin x d x \\
& =-x^3 \cos x+3 x^2 \sin x+6 x \cos x-6 \sin x+c
\end{aligned}$

So $g(x)=-x^3 \cos x+3 x^2 \sin x+6 x \cos x-6 \sin x$
$\begin{aligned}
& \mathrm{g}\left(\frac{\pi}{2}\right)=\frac{3 \pi^2}{4}-6 \\
& \mathrm{~g}^{\prime}(\mathrm{x})=-3 \mathrm{x}^2 \cos \mathrm{x}+\mathrm{x}^3 \sin \mathrm{x}+6 \cos \mathrm{x}-6 \cos \mathrm{x} \\
& \mathrm{~g}^{\prime}\left(\frac{\pi}{2}\right)=\frac{\pi^3}{8} \\
& 8\left(\mathrm{~g}\left(\frac{\pi}{2}\right)+\mathrm{g}^{\prime}\left(\frac{\pi}{2}\right)\right)=\pi^3+6 \pi^2-48
\end{aligned}$

So $\alpha+\beta-\gamma=55$

</details>

---

### Q4. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \mathrm{e}^x\left(\frac{x \sin ^{-1} x}{\sqrt{1-x^2}}+\frac{\sin ^{-1} x}{\left(1-x^2\right)^{3 / 2}}+\frac{x}{1-x^2}\right) \mathrm{d} x=\mathrm{g}(x)+\mathrm{C}$, where C is the constant of integration, then $g\left(\frac{1}{2}\right)$ equals :

**Options:**

- **(A)** $\frac{\pi}{4} \sqrt{\frac{e}{3}}$
- **(B)** $\frac{\pi}{6} \sqrt{\frac{e}{3}}$
- **(C)** $\frac{\pi}{4} \sqrt{\frac{e}{2}}$
- **(D)** $\frac{\pi}{6} \sqrt{\frac{e}{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{6} \sqrt{\frac{e}{3}}$**

**Detailed Solution:**

$\begin{aligned}
& \frac{d}{d x}\left(\frac{x \cdot \sin ^{-1} x}{\sqrt{1-x^2}}\right)-\sin ^{-1} x \cdot\left(\frac{1 \cdot \sqrt{1-x^2}+\frac{x \cdot 2 x}{2 \sqrt{1-x^2}}}{1-x^2}\right) \\
& =\frac{x}{\sqrt{1-x^2}} \cdot \frac{1}{\sqrt{1-x^2}} \\
& =\frac{\sin ^{-1} x}{\left(1-x^2\right)^{3 / 2}}+\frac{x}{1-x^2}
\end{aligned}$
$\begin{aligned}
& \text { Hence, } I=\int e^x\left(f(x)+f^{\prime}(x)\right) d x \\
& =e^x \cdot f(x)+C \\
& I=e^x \cdot \frac{x \cdot \sin ^{-1} x}{\sqrt{1-x^2}}+C=g(x)+C \\
& \Rightarrow g(x)=\frac{x e^x \sin ^{-1} x}{\sqrt{1-x^2}} \text { and } g(1 / 2)=\frac{\pi}{6} \sqrt{\frac{e}{3}}
\end{aligned}$

</details>

---

### Q5. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>e</mi><mfrac><mn>3</mn><mn>4</mn></mfrac></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>e</mi><mfrac><mn>3</mn><mn>4</mn></mfrac></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mi>e</mi><mfrac><mn>3</mn><mn>4</mn></mfrac></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mfrac><mn>3</mn><mn>4</mn></mfrac></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>e</mi><mfrac><mn>3</mn><mn>4</mn></mfrac></msup></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>&#160;</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mi>sin</mi><mn>2</mn><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p>Now let, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mi>t</mi></msup><mfenced><mrow><msqrt><mn>1</mn><mo>-</mo><mi>t</mi></msqrt><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>1</mn><mo>-</mo><mi>t</mi></msqrt></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p>Now comparing with,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mi>t</mi></msup><mfenced><mrow><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>t</mi></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><msup><mi>e</mi><mi>t</mi></msup><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mi>t</mi></msqrt><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>t</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>1</mn><mo>-</mo><mi>t</mi></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>t</mi></msup><msqrt><mn>1</mn><mo>-</mo><mi>t</mi></msqrt><mo>+</mo><mi>c</mi><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>&#183;</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Now using, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>e</mi><mfrac><mn>3</mn><mn>4</mn></mfrac></msup></math></p></blockquote>

</details>

---

### Q6. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>&#160;</mo><msup><mi>sec</mi><mn>2</mn></msup><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mo>(</mo><mi>x</mi><mo>&#160;</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfrac><mrow><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>16</mn></mfrac><mo>+</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>4</mn><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><mo>)</mo></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfrac><mrow><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>16</mn></mfrac><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>4</mn><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><mo>)</mo></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfrac><mrow><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>32</mn></mfrac><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>4</mn><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><mo>)</mo></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfrac><mrow><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>32</mn></mfrac><mo>+</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>4</mn><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><mo>)</mo></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfrac><mrow><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>32</mn></mfrac><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>4</mn><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><mo>)</mo></mrow></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>&#160;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>tan</mi><mi>x</mi></mrow><mrow><mo>(</mo><mi>x</mi><mo>&#160;</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p>Apply Integration by parts.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>g</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8747;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><mo>&#8747;</mo><mfenced><mrow><mi>f</mi><mo>'</mo><mfenced><mi>x</mi></mfenced><mo>&#8747;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8747;</mo><mfenced><mfrac><mrow><mi>x</mi><mo>&#160;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>tan</mi><mi>x</mi></mrow><mrow><mo>(</mo><mi>x</mi><mo>&#160;</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><mo>&#8747;</mo><mfenced><mrow><mfrac><mrow><mo>d</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mo>d</mo><mi>x</mi></mrow></mfrac><mo>&#8747;</mo><mfenced><mfrac><mrow><mi>x</mi><mo>&#160;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>tan</mi><mi>x</mi></mrow><mrow><mo>(</mo><mi>x</mi><mo>&#160;</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>&#160;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>p</mi><mo>=</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>p</mi></mrow><msup><mi>p</mi><mn>2</mn></msup></mfrac><mo>-</mo><mo>&#8747;</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>p</mi></mrow><msup><mi>p</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mo>(</mo><mi>x</mi><mo>&#160;</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac><mo>+</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>&#160;</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>&#8747;</mo><mfrac><mi>x</mi><mrow><mi>x</mi><mo>&#160;</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#8747;</mo><mfrac><mrow><mi>x</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>x</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>x</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mi>t</mi></mfrac><mo>=</mo><mn>2</mn><mi>log</mi><mi>t</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>log</mi><mo>|</mo><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>|</mo><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mi>x</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mo>(</mo><mi>x</mi><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mi>x</mi><mo>&#160;</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mn>2</mn><mi>log</mi><mo>|</mo><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>|</mo><mo>+</mo><mi>c</mi></math></p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>Also,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mfrac><msup><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mn>2</mn></msup><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#215;</mo><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mn>2</mn><mi>log</mi><mfenced close="|" open="|"><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfrac><mrow><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>32</mn></mfrac><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>4</mn><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><mo>)</mo></mrow></mfrac></math></p><p>Hence, this is the correct option.</p></blockquote>

</details>

---

### Q7. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>2022</mn></mrow><mrow><msup><mi>sin</mi><mn>2022</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><msup><mn>2</mn><mn>1011</mn></msup></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>1010</mn></msup><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>-</mo><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>1010</mn></msup><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>-</mo><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>1011</mn></msup><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>-</mo><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>1011</mn></msup><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>-</mo><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>1010</mn></msup><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>-</mo><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>2022</mn></mrow><mrow><msup><mi>sin</mi><mn>2022</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>On rearranging we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><munder><munder><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow><mo>&#9183;</mo></munder><mrow><mi>I</mi><mi>I</mi></mrow></munder><mo>&#183;</mo><munder><munder><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>2022</mn></mrow></msup><mi>x</mi></mrow><mo>&#9183;</mo></munder><mi>I</mi></munder><mi>d</mi><mi>x</mi><mo>-</mo><mn>2022</mn><mo>&#8747;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>2022</mn></mrow></msup><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p>Now using integration by parts we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>tan</mi><mi>x</mi><mo>.</mo><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>2022</mn></mrow></msup><mo>+</mo><mo>&#8747;</mo><mfenced><mn>2022</mn></mfenced><mi>tan</mi><mi>x</mi><mo>&#183;</mo><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>2023</mn></mrow></msup><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>-</mo><mn>2022</mn><mo>&#8747;</mo><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>2022</mn></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>tan</mi><mi>x</mi><mo>.</mo><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>2022</mn></mrow></msup><mo>+</mo><mo>&#8747;</mo><mfenced><mn>2022</mn></mfenced><mi>tan</mi><mi>x</mi><mo>&#183;</mo><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>2022</mn></mrow></msup><mfrac><mrow><mi>cos</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>-</mo><mn>2022</mn><mo>&#8747;</mo><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>2022</mn></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>tan</mi><mi>x</mi><mo>.</mo><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>2022</mn></mrow></msup><mo>+</mo><mo>&#8747;</mo><mfenced><mn>2022</mn></mfenced><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>2022</mn></mrow></msup><mi>d</mi><mi>x</mi><mo>-</mo><mn>2022</mn><mo>&#8747;</mo><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>2022</mn></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>2022</mn></mrow></msup><mo>+</mo><mi>C</mi></math></p><p>Now at  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><msup><mn>2</mn><mn>1011</mn></msup><mo>&#8658;</mo><msup><mn>2</mn><mn>1011</mn></msup><mo>=</mo><mn>1</mn><mo>&#215;</mo><msup><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mrow><mo>-</mo><mn>2022</mn></mrow></msup><mo>+</mo><mi>C</mi><mo>&#160;</mo><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>tan</mi><mi>x</mi></mrow><msup><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>2022</mn></msup></mfrac></math></p><p>Now finding the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><msqrt><mn>3</mn></msqrt><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>2022</mn></msup></mrow></mfrac><mo>=</mo><mfrac><msup><mn>2</mn><mn>2022</mn></msup><msqrt><mn>3</mn></msqrt></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><msup><mfenced><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2022</mn></msup></mfrac><mo>=</mo><mfrac><msup><mn>2</mn><mn>2022</mn></msup><msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mn>2021</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>1010</mn></msup></mfrac><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>1010</mn></msup><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mi>I</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced></math></p></blockquote>

</details>

---

### Q8. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>C</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is a constant, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>3</mn></msup><mi>f</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>8</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>C</mi></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mfrac><mn>2</mn><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>C</mi></math></p><p>On comparing both sides we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;&#39;&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>12</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup></mfrac></math> ,</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;&#39;&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>12</mn><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup></mfrac><mo>=</mo><mfrac><mn>12</mn><mn>16</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p> </p>

</details>

---

### Q9. JEE Main 2022 (25 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="bold-italic">R</mi></math> be a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfenced><mrow><mfrac><mrow><mi>x</mi><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mi mathvariant="normal">e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced><mfenced><mrow><msup><mi mathvariant="normal">e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>-</mo><mi>x</mi><msup><mi mathvariant="normal">e</mi><mi>x</mi></msup></mrow></mfenced></mrow><msup><mfenced><mrow><msup><mi mathvariant="normal">e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>x</mi><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><msup><mi mathvariant="normal">e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mi>C</mi></math>, for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is an arbitrary constant. Then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>-</mo><msup><mi>g</mi><mo>&#39;</mo></msup></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>+</mo><msup><mi>g</mi><mo>&#39;</mo></msup></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>-</mo><msup><mi>g</mi><mo>&#39;</mo></msup></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mi>x</mi><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mo>&#8747;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>-</mo><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup></mrow><msup><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>x</mi><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>-</mo><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup></mrow><msup><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mo>&#8747;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>-</mo><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup></mrow><msup><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p>By comparison, we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt><mfenced close="]" open="["><mrow><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math> so, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#8712;</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>sin</mi><mi>x</mi></math> is an increasing function in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>.</p>

</details>

---

### Q10. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>50</mn></msup></mrow></mfenced><mn>100</mn></msup><mi>d</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>50</mn></msup></mrow></mfenced><mn>101</mn></msup><mi>d</mi><mi>x</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mi>&#945;</mi><msub><mi>I</mi><mn>1</mn></msub></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> equals to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5049</mn><mn>5050</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5050</mn><mn>5049</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5050</mn><mn>5051</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5051</mn><mn>5050</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5050</mn><mn>5051</mn></mfrac></math>**

**Detailed Solution:**

<p>Given </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><msub><mi>I</mi><mn>2</mn></msub><msub><mi>I</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>50</mn></msup></mrow></mfenced><mn>101</mn></msup><mi>d</mi><mi>x</mi></mrow><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>50</mn></msup></mrow></mfenced><mn>100</mn></msup><mi>d</mi><mi>x</mi></mrow></mfrac></math>
Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>50</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>50</mn></msup></mrow></mfenced><mn>100</mn></msup><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msub><mi>x</mi><mo>.</mo></msub><msup><mi>x</mi><mn>49</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>50</mn></msup></mrow></mfenced><mn>100</mn></msup><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub><mo>-</mo><msubsup><mfenced close="]" open="["><mfrac><mrow><mo>-</mo><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>50</mn></msup></mrow></mfenced><mn>101</mn></msup></mrow><mn>5050</mn></mfrac></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>50</mn></msup></mrow></mfenced><mn>101</mn></msup><mn>5050</mn></mfrac><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub><mo>-</mo><mfrac><msub><mi>I</mi><mn>2</mn></msub><mn>5050</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><msub><mi>I</mi><mn>2</mn></msub><msub><mi>I</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mn>5050</mn><mn>5051</mn></mfrac></math></p>

</details>

---

### Q11. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></msup><mi>d</mi><mi>x</mi><mo>=</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><msup><mi>e</mi><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></msup><mo>+</mo><mi>c</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is a constant of integration, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mn>0</mn><mo>)</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></msup><mi>d</mi><mi>x</mi><mo>+</mo><mo>&#8747;</mo><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><msup><mi>e</mi><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><msup><mi>e</mi><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><msup><mi>e</mi><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>x</mi><mo>=</mo><mi>u</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>u</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></msup><mo>+</mo><mi>c</mi><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></msup><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q12. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mn>5</mn></msup><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>+</mo><mi>c</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is a constant of integration, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math>
- **(B)** <math><mo>-</mo><mn>1</mn></math>
- **(C)** <math><mn>1</mn></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>x</mi><mn>5</mn></msup><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>x</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><msup><mi>t</mi><mn>2</mn></msup><msup><mi>e</mi><mi>t</mi></msup><mi>d</mi><mi>t</mi></math></p><p>By using integrating by parts, i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfenced><mrow><mi>u</mi><mo>&#183;</mo><mi>v</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>u</mi><mo>&#8747;</mo><mi>v</mi><mi>d</mi><mi>x</mi><mo>-</mo><mo>&#8747;</mo><mfenced close="]" open="["><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mi>u</mi><mo>&#8747;</mo><mi>v</mi><mi>d</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>&#8747;</mo><msup><mi>e</mi><mi>t</mi></msup><mi>d</mi><mi>t</mi><mo>-</mo><mo>&#8747;</mo><mfenced><mrow><mn>2</mn><mi>t</mi><mo>&#8747;</mo><msup><mi>e</mi><mi>t</mi></msup><mi>d</mi><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>t</mi><mn>2</mn></msup><msup><mi>e</mi><mi>t</mi></msup><mo>-</mo><mn>2</mn><mo>&#8747;</mo><mi>t</mi><msup><mi>e</mi><mi>t</mi></msup><mi>d</mi><mi>t</mi></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>Again, applying integrating by parts, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>t</mi><mn>2</mn></msup><msup><mi>e</mi><mi>t</mi></msup><mo>-</mo><mn>2</mn><mfenced><mrow><mi>t</mi><mo>&#8747;</mo><msup><mi>e</mi><mi>t</mi></msup><mi>d</mi><mi>t</mi><mo>-</mo><mo>&#8747;</mo><mn>1</mn><mo>&#183;</mo><msup><mi>e</mi><mi>t</mi></msup><mi>d</mi><mi>t</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>t</mi><mn>2</mn></msup><msup><mi>e</mi><mi>t</mi></msup><mo>-</mo><mn>2</mn><mfenced><mrow><mi>t</mi><msup><mi>e</mi><mi>t</mi></msup><mo>-</mo><msup><mi>e</mi><mi>t</mi></msup></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>t</mi><mn>2</mn></msup><msup><mi>e</mi><mi>t</mi></msup><mo>-</mo><mn>2</mn><mi>t</mi><msup><mi>e</mi><mi>t</mi></msup><mo>+</mo><mn>2</mn><msup><mi>e</mi><mi>t</mi></msup></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi>e</mi><mi>t</mi></msup><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>x</mi><mn>5</mn></msup><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q13. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>e</mi><mrow><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi></mrow></msup><mfenced><mrow><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi><mi>tan</mi><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mfenced><mrow><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi><mi>tan</mi><mi>x</mi><mo>+</mo><mi>s</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msup><mi>e</mi><mrow><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi></mrow></msup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>C</mi><mo>,</mo></math> then a possible choice of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is:

**Options:**

- **(A)** <math><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi>x</mi><mo>-</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mi>x</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi>x</mi><mo>+</mo><mi>x</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math><mrow><mo stretchy="false">&#8747;</mo><mrow><msup><mrow><mi>e</mi></mrow><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></msup></mrow></mrow><mo>(</mo><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></msup><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>Differentiating both sides w.r.t <math><mi>&#8216;</mi><mi>x</mi><mi>&#8217;</mi></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi></mrow></msup><mfenced><mrow><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi><mi>tan</mi><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mfenced><mrow><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi><mi>tan</mi><mi>x</mi><mo>+</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced><mrow><msup><mi>e</mi><mrow><mi>sec</mi><mi>x</mi></mrow></msup><mo>&#8901;</mo><mi>sec</mi><mi>x</mi><mi>tan</mi><mi>x</mi></mrow></mfenced><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><msup><mi>e</mi><mrow><mi>sec</mi><mi>x</mi></mrow></msup><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>tan</mi><mi>x</mi><mi>sec</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#8712;</mo><mi>R</mi></math>
Hence, possible choice is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q14. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mn>5</mn></msup><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>48</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></msup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><mi>C</mi></math>, where <math><mi>C</mi></math> is a constant of integration, then <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></math>
- **(B)** <math><mo>-</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></math>
- **(C)** <math><mo>-</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>1</mn></math>
- **(D)** <math><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>x</mi><mn>5</mn></msup><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></msup><mi>d</mi><mi>x</mi></math> 

Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mo>-</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mi>t</mi><mn>4</mn></mfrac></mrow></mfenced><msup><mi>e</mi><mi>t</mi></msup><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mn>12</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>48</mn></mfrac><mo>&#8747;</mo><mi>t</mi><msup><mi>e</mi><mi>t</mi></msup><mi>d</mi><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>48</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><mi>t</mi><msup><mi>e</mi><mi>t</mi></msup><mo>-</mo><mo>&#8747;</mo><msup><mi>e</mi><mi>t</mi></msup><mi>d</mi><mi>t</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mi>t</mi></msup></mrow><mn>48</mn></mfrac><mo>+</mo><mi>C</mi><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></msup></mrow><mn>48</mn></mfrac><mo>+</mo><mi>C</mi><mo>,</mo><mo>&#160;</mo></math>
where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is the constant of integration.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q15. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi>f</mi><mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#968;</mi><mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mn>5</mn></msup><mi>f</mi><mrow><mo>(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>)</mo></mrow><mi>d</mi><mi>x</mi></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mi>&#968;</mi><mrow><mo>(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>)</mo></mrow><mo>&#8722;</mo><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>&#968;</mi><mrow><mo>(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>)</mo></mrow><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mrow><mo>[</mo><msup><mi>x</mi><mn>3</mn></msup><mi>&#968;</mi><mrow><mo>(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>)</mo></mrow><mo>&#8722;</mo><mo>&#8747;</mo><msup><mi>x</mi><mn>3</mn></msup><mi>&#968;</mi><mrow><mo>(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>)</mo></mrow><mi>d</mi><mi>x</mi><mo>]</mo></mrow><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mrow><mo>[</mo><msup><mi>x</mi><mn>3</mn></msup><mi>&#968;</mi><mrow><mo>(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>)</mo></mrow><mo>&#8722;</mo><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>&#968;</mi><mrow><mo>(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>)</mo></mrow><mi>d</mi><mi>x</mi><mo>]</mo></mrow><mo>+</mo><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mi>&#968;</mi><mrow><mo>(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>)</mo></mrow><mo>&#8722;</mo><mn>3</mn><mo>&#8747;</mo><msup><mi>x</mi><mn>3</mn></msup><mi>&#968;</mi><mrow><mo>(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>)</mo></mrow><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mi>&#968;</mi><mrow><mo>(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>)</mo></mrow><mo>&#8722;</mo><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>&#968;</mi><mrow><mo>(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>)</mo></mrow><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mn>5</mn></msup><mi>f</mi><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced><mi>d</mi><mi>x</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><msup><mi>x</mi><mn>3</mn></msup><mo>.</mo><msup><mi>x</mi><mn>2</mn></msup><mi>f</mi><mfenced separators="|"><msup><mi>x</mi><mn>3</mn></msup></mfenced><mi>d</mi><mi>x</mi><mi>&#160;</mi></math> </p><p>Applying integration by parts, we get

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>f</mi><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><mo>&#8747;</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>f</mi><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mi>&#968;</mi><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced><mo>-</mo><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>&#968;</mi><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the constant of integration.</p>

</details>

---

### Q16. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x)$ be an indefinite integral of $\cos ^3 x$.
Statement 1: $f(x)$ is a periodic function of period
$\pi$.
Statement 2: $\cos ^3 x$ is a periodic function.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is false.
- **(B)** Both the Statements are true, but Statement 2 is not the correct explanation of Statement 1.
- **(C)** Both the Statements are true, and Statement 2 is correct explanation of Statement 1.
- **(D)** Statement 1 is false, Statement 2 is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement 1 is false, Statement 2 is true.**

**Detailed Solution:**

Statement $-2: \cos ^3 x$ is a periodic function. it is a true statement.
Statement-1
Given $f(x)=\int \cos ^3 x d x$
$$
\begin{aligned}
& =\int\left(\frac{\cos 3 x}{4}+\frac{3 \cos x}{4}\right) d x \\
& =\frac{1}{4} \frac{\sin 3 x}{3}+\frac{3}{4} \sin x \\
& =\frac{1}{12} \sin 3 x+\frac{3}{4} \sin x
\end{aligned}
$$
Now, period of $\frac{1}{12} \sin 3 x=\frac{2 \pi}{3}$
Period of $\frac{3}{4} \sin x=2 \pi$
Hence period of $f(x)=\frac{\text { L.C.M. }(2 \pi, 2 \pi}{\text { HCF of }(1,3)}$

$$
=\frac{2 \pi}{1}=2 \pi
$$
Thus, $f(x)$ is a periodic function of period $2 \pi$.
Hence, Statement $-1$ is false.

</details>

---

