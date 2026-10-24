# JEE Main Mathematics - Limits

## Topic 5: Special Forms

**Total Questions:** 13

---

### Q1. JEE Main 2025 (3 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

If $\operatorname{Lim}_{x \rightarrow 0}\left(\frac{\tan x}{x}\right)^{\frac{1}{x^2}}=p$, then $96 \log _e p$ is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **32**

**Detailed Solution:**

$P=\lim _{x \rightarrow 0}\left(\frac{\tan x}{x}\right)^{\frac{1}{x^2}}$
$\Rightarrow \mathrm{P}=\mathrm{e}^{\lim _{\mathrm{x} \rightarrow 0}\left(\frac{\tan x-\mathrm{x}}{\mathrm{x}^3}\right)}$
$=\mathrm{e}^{\lim _{x \rightarrow 0} \frac{\left(x+\frac{x^3}{3}+\frac{2 x^5}{15}+\ldots . .-x\right)}{x^3}}$
$=e^{1 / 3}$
$\therefore 96 \log _{\mathrm{e}}^{\mathrm{p}}=96 \times \frac{1}{3}=32$

</details>

---

### Q2. JEE Main 2025 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

If $\lim _{\mathrm{t} \rightarrow 0}\left(\int_0^1(3 x+5)^{\mathrm{t}} \mathrm{d} x\right)^{\frac{1}{t}}=\frac{\alpha}{5 \mathrm{e}}\left(\frac{8}{5}\right)^{\frac{2}{3}}$, then $\alpha$ is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **64**

**Detailed Solution:**

$\begin{aligned} \frac{\alpha}{5 e} & =\exp \left(\lim _{t \rightarrow 0} \frac{1}{t}\left(\int_0^1(3 x+5)^t d x-1\right)\right) \\ & =\exp \left(\lim _{t \rightarrow 0} \frac{1}{t}\left(\frac{(3 x+5)^{t+1}}{3(t+1)}\right)_0^1-1\right) \\ & =\exp \left(\lim _{t \rightarrow 0} \frac{1}{t}\left(\frac{8^{t+1}-5^{t+1}}{3(t+1)}-1\right)\right) \\ & =\exp \left(\lim _{t \rightarrow 0} \frac{1}{t}\left(\frac{8^{t+1}-5^{t+1}-3 t-3}{3(t+1)}\right)\right) \\ & =\exp \left(\lim _{t \rightarrow 0}\left(\frac{8^{t+1} \cdot \ln 8-5^{t+1} \ln 5-3}{3(t+1)}\right)\right) \\ & =\exp \left(\frac{\ln 8^8-\ln 5^5-3}{5}\right)\end{aligned}$
$\begin{aligned} & =\left(\frac{8}{5}\right)^{2 / 3} \frac{\alpha}{5 e}=\exp \left(\frac{\ln \left(\frac{8^8}{5^5}\right)}{5}-1\right) \\ & \Rightarrow\left(\frac{8}{5}\right)^{2 / 3} \frac{\alpha}{5}=\left(\frac{8^8}{5^5}\right)^{1 / 3}=\left(\frac{8^6 \cdot 8^2}{5^3 \cdot 5^2}\right)^{1 / 3}=\frac{64}{5}\left(\frac{8}{5}\right)^{2 / 3} \\ & \Rightarrow \alpha=64\end{aligned}$

</details>

---

### Q3. JEE Main 2024 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

If $\alpha=\lim _{x \rightarrow 0^{+}}\left(\frac{\mathrm{e}^{\sqrt{\tan x}}-\mathrm{e}^{\sqrt{x}}}{\sqrt{\tan x}-\sqrt{x}}\right)$ and $\beta=\lim _{x \rightarrow 0}(1+\sin x)^{\frac{1}{2} \cot x}$ are the roots of the quadratic equation $a x^2+b x-\sqrt{\mathrm{e}}=0$, then $12 \log _{\mathrm{e}}(\mathrm{a}+\mathrm{b})$ is equal to__________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

$\begin{aligned} & \alpha=\lim _{x \rightarrow 0^{+}} e^{\sqrt{x}} \frac{\left(e^{\sqrt{\tan x}-\sqrt{x}}-1\right)}{\sqrt{\tan x}-\sqrt{x}} \\ & =1 \\ & \beta=\lim _{x \rightarrow 0}(1+\sin x)^{\frac{1}{2} \cot x} \\ & =e^{1 / 2} \\ & x^2-(1+\sqrt{e})+\sqrt{e}=0 \\ & a x^2+b x-\sqrt{e}=0 \\ & \text { On comparing } \\ & a=-1, b=\sqrt{e}+1 \\ & 12 \ln (a+b)=12 \times \frac{1}{2}=6\end{aligned}$

</details>

---

### Q4. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mrow><msup><mn>1</mn><mfrac><mn>1</mn><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></mfrac></msup><mo>+</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></mfrac></msup><mo>+</mo><msup><mn>3</mn><mfrac><mn>1</mn><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></mfrac></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mi>n</mi><mfrac><mn>1</mn><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></mfrac></msup></mrow></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mrow><msup><mn>1</mn><mfrac><mn>1</mn><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></mfrac></msup><mo>+</mo><msup><mn>2</mn><mfrac><mn>1</mn><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></mfrac></msup><mo>+</mo><msup><mn>3</mn><mfrac><mn>1</mn><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></mfrac></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mi>n</mi><mfrac><mn>1</mn><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></mfrac></msup></mrow></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mo>=</mo><mi>lim</mi></mrow><mrow><mi>t</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mrow><msup><mn>1</mn><mrow><msup><mi>cosec</mi><mn>2</mn></msup><mi>t</mi></mrow></msup><mo>+</mo><msup><mn>2</mn><mrow><msup><mi>cosec</mi><mn>2</mn></msup><mi>t</mi></mrow></msup><mo>+</mo><msup><mn>3</mn><mrow><msup><mi>cosec</mi><mn>2</mn></msup><mi>t</mi></mrow></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mi>n</mi><mrow><msup><mi>cosec</mi><mn>2</mn></msup><mi>t</mi></mrow></msup></mrow></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mo>=</mo><mi>lim</mi></mrow><mrow><mi>t</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#160;</mo><mo>&#160;</mo><msup><mi>n</mi><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></mfrac></msup><msup><mfenced><mrow><msup><mfenced><mfrac><mn>1</mn><mi>n</mi></mfrac></mfenced><mrow><msup><mi>cosec</mi><mn>2</mn></msup><mi>t</mi></mrow></msup><mo>+</mo><msup><mfenced><mfrac><mn>2</mn><mi>n</mi></mfrac></mfenced><mrow><msup><mi>cosec</mi><mn>2</mn></msup><mi>t</mi></mrow></msup><mo>+</mo><msup><mfenced><mfrac><mn>3</mn><mi>n</mi></mfrac></mfenced><mrow><msup><mi>cosec</mi><mn>2</mn></msup><mi>t</mi></mrow></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>1</mn></mrow></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>t</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#160;</mo><mo>&#160;</mo><msup><mfenced><mrow><mn>0</mn><mo>+</mo><mn>0</mn><mo>+</mo><mn>0</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>1</mn></mrow></mfenced><mn>0</mn></msup><mo>=</mo><mi>n</mi></math></p>

</details>

---

### Q5. JEE Main 2022 (28 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mfrac><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></mfenced><mfrac><mn>100</mn><mi>x</mi></mfrac></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<blockquote><p>Given,<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi>l</mi><mi>i</mi><mi>m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mfrac><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>c</mi><mi>o</mi><mi>s</mi><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>c</mi><mi>o</mi><mi>s</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>s</mi><mi>i</mi><mi>n</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>c</mi><mi>o</mi><mi>s</mi><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>s</mi><mi>i</mi><mi>n</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></mfenced><mfrac><mn>100</mn><mi>x</mi></mfrac></msup></math></p><p>Now by putting the value of limit we can see it is in form <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mo>&#8734;</mo></msup></math></p><p>Now we know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></msup></math> when is in form of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mo>&#8734;</mo></msup></math>, we can write this as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></msup></math></p><p>Now using the above rule we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mfenced><mfrac><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mfrac><mn>100</mn><mi>x</mi></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mfrac><mn>100</mn><mi>x</mi></mfrac><mfenced close="]" open="["><mfrac><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></mfenced></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mn>100</mn><mi>x</mi></mfrac><mfenced close="]" open="["><mfenced><mfrac><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mo>-</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>3</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>8</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>3</mn><mi>sin</mi><mn>2</mn></mrow></mfrac></mfenced></mfenced></mrow></msup></math></p><p>Using L-hospital method we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>100</mn><mrow><mn>16</mn><mo>+</mo><mn>3</mn><mi>sin</mi><mn>2</mn></mrow></mfrac><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>3</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>&#215;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>3</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>4</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>3</mn><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mn>1</mn></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>100</mn><mrow><mn>16</mn><mo>+</mo><mn>3</mn><mi>sin</mi><mn>2</mn></mrow></mfrac><mfenced><mfrac><mrow><mn>12</mn><mo>-</mo><mn>3</mn><mfenced><mn>4</mn></mfenced><mo>+</mo><mn>8</mn><mo>&#215;</mo><mn>1</mn><mo>-</mo><mn>8</mn><mo>+</mo><mn>3</mn><mi>cos</mi><mn>2</mn><mo>-</mo><mn>3</mn><mi>cos</mi><mn>2</mn></mrow><mn>1</mn></mfrac></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>100</mn><mrow><mn>16</mn><mo>+</mo><mn>3</mn><mi>sin</mi><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mn>0</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mn>0</mn></msup><mo>=</mo><mn>1</mn></math></p></blockquote>

</details>

---

### Q6. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></munder><mfrac><mrow><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi><mo>-</mo><mi>tan</mi><mi>x</mi></mrow><mrow><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mrow><mi>cot</mi><mi>x</mi></mrow></msup></math> are the roots of the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>,</mo></math> then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>If, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mrow><mi>cot</mi><mi>x</mi></mrow></msup></math>    (<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mrow><mo>&#8734;</mo><mo>&#160;</mo><mo>&#160;</mo></mrow></msup></math>form)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#160;</mo><munder><mrow><mi>lim</mi><mo>&#160;</mo></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>cot</mi><mi>x</mi><mfenced close="]" open="["><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mn>2</mn><mi>sin</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>.</mo><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfrac><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mi>cos</mi><mi>x</mi><mo>.</mo><mi>sin</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow><mrow><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><msup><mi>e</mi><mn>0</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></munder><mfrac><mrow><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi><mo>-</mo><mi>tan</mi><mi>x</mi></mrow><mrow><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></munder><mfrac><mrow><mi>tan</mi><mi>x</mi><mo>(</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>tan</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mrow><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></munder><mi>tan</mi><mi>x</mi><mo>&#215;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></munder><mfenced><mrow><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></munder><mfrac><mrow><mo>(</mo><mi>tan</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mrow><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>&#215;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></munder><mfrac><mrow><mo>(</mo><mi>tan</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mrow><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></munder><mfrac><mrow><mi>tan</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mi>cos</mi><mi>x</mi><mo>.</mo><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></munder><mfrac><mfenced><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mstyle><mi>cos</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mi>cos</mi><mi>x</mi><mo>.</mo><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn></mrow></munder><mfrac><mrow><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow><mrow><mi>cos</mi><mi>x</mi><mo>.</mo><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p>So, the equation whose roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q7. JEE Main 2021 (20 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

If the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mrow><mn>2</mn><mo>-</mo><mi>cos</mi><mi>x</mi><msqrt><mi>cos</mi><mn>2</mn><mi>x</mi></msqrt></mrow></mfenced><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></msup></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>a</mi></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is equal to_____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mrow><mn>2</mn><mo>-</mo><mi>cos</mi><mi>x</mi><msqrt><mi>cos</mi><mn>2</mn><mi>x</mi></msqrt></mrow></mfenced><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></msup><mo>&#8594;</mo><msup><mn>1</mn><mo>&#8734;</mo></msup></math></p><p>Hence,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mi>x</mi><msqrt><mi>cos</mi><mn>2</mn><mi mathvariant="normal">x</mi></msqrt></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mo>&#215;</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></msup></math>
Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mi>x</mi><msqrt><mi>cos</mi><mn>2</mn><mi mathvariant="normal">x</mi></msqrt></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mo>&#8594;</mo><mfenced><mfrac><mn>0</mn><mn>0</mn></mfrac></mfenced></math></p><p>Using L&#39;Hospital Rule</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="}" open="{"><mfrac><mrow><mi>sin</mi><mi>x</mi><msqrt><mi>cos</mi><mn>2</mn><mi>x</mi></msqrt><mo>-</mo><mi>cos</mi><mi>x</mi><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mi>cos</mi><mn>2</mn><mi>x</mi></msqrt></mrow></mfrac></mstyle><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mfenced></math>
 </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="}" open="{"><mfrac><mrow><mi>sin</mi><mi>x</mi><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>&#183;</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mn>2</mn><mi>x</mi><msqrt><mi>cos</mi><mn>2</mn><mi>x</mi></msqrt></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="}" open="{"><mfrac><mrow><mi>sin</mi><mn>3</mn><mi>x</mi></mrow><mrow><mn>2</mn><mi>x</mi><msqrt><mi>cos</mi><mn>2</mn><mi>x</mi></msqrt></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="}" open="{"><mfrac><mrow><mi>sin</mi><mn>3</mn><mi>x</mi></mrow><mrow><mn>3</mn><mi>x</mi></mrow></mfrac></mfenced><mo>&#215;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="}" open="{"><mfrac><mn>1</mn><msqrt><mi>cos</mi><mn>2</mn><mi>x</mi></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="}" open="{"><mfrac><mrow><mi>sin</mi><mn>3</mn><mi>x</mi></mrow><mrow><mn>3</mn><mi>x</mi></mrow></mfrac></mfenced><mo>&#215;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mi>x</mi><msqrt><mi>cos</mi><mn>2</mn><mi>x</mi></msqrt></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>2</mn></mrow></msup><mo>=</mo><msup><mi>e</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><menclose notation="box"><mi>a</mi><mo>=</mo><mn>3</mn></menclose></math></p>

</details>

---

### Q8. JEE Main 2021 (25 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>n</mi></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>e</mi></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>It is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mo>&#8734;</mo></msup></math> form</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><msup><mi>e</mi><mrow><munder><mrow><mi>l</mi><mi>i</mi><mi>m</mi></mrow><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mfrac><mfenced open=""><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mi>n</mi></mfrac></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>L</mi><mo>=</mo><msup><mi>e</mi><mrow><munder><mrow><mi>l</mi><mi>i</mi><mi>m</mi></mrow><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>n</mi></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>L</mi><mo>=</mo><msup><mi>e</mi><mfenced><mrow><mn>0</mn><mo>+</mo><mn>0</mn><mo>+</mo><mn>0</mn><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>0</mn></mrow></mfenced></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><msup><mi>e</mi><mn>0</mn></msup><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q9. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mrow><mi>tan</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mi>x</mi></mrow></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced><mrow><mi>tan</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mi>x</mi></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mfenced><mn>1</mn></mfenced><mo>&#8734;</mo></msup></math>form</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mfenced><mrow><mi>tan</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mi>x</mi></mfrac></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><msup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></msup><mo>=</mo><msup><mi>e</mi><mfenced><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mi>g</mi><mfenced><mi>x</mi></mfenced><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></msup><mo>,</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mfenced><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mi>x</mi></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>2</mn><mi>tan</mi><mi>x</mi></mrow><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mi>x</mi></mrow></mfenced></mrow></mfrac></mrow></msup><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mi>tan</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mfenced><mfenced><mfrac><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mi>x</mi></mrow></mfrac></mfenced></mrow></msup></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mfenced><mn>1</mn></mfenced><mfenced><mfrac><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mn>0</mn></mrow></mfrac></mfenced></mrow></msup><mo>=</mo><msup><mi>e</mi><mn>2</mn></msup></math></p>

</details>

---

### Q10. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced separators="|"><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow><mrow><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></msup></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math><mi>e</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mfenced separators="|"><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow><mrow><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mfenced close="}" open="{" separators="|"><mrow><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow><mrow><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="}" open="{" separators="|"><mfrac><mrow><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><msup><mi>e</mi><mn>2</mn></msup></mfrac></math></p>

</details>

---

### Q11. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a differentiable function satisfying <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced><mo>+</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>.</mo></math> Then <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup></math> is equal to

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mi mathvariant="normal">e</mi></math>
- **(C)** <math><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>1</mn></math>**

**Detailed Solution:**

<p>This limit is <math><msup><mrow><mn>1</mn></mrow><mrow><mi>&#8734;</mi></mrow></msup></math> form</p><p><math><mo>&#8756;</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></msup></math></p><p><math><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow></mfrac></mrow></mfenced></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mn>0</mn></mrow><mrow><mn>0</mn></mrow></mfrac><mtext>&#8201;</mtext><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">m</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>&#160;</mi><mfrac><mrow><msup><mi>f</mi><mi>&#39;</mi></msup><mfenced separators="|"><mrow><mn>3</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>f</mi><mi>&#39;</mi></msup><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi><mfenced separators="|"><mrow><mo>-</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mn>2</mn></mfenced></mrow></mfenced></mrow></mfrac></mrow></msup></math></p><p><math><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>0</mn></mrow></msup><mo>=</mo><mn>1</mn></math>.</p>

</details>

---

### Q12. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><mo>&#8289;</mo><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mi>a</mi><mi>x</mi></mfrac><mo>-</mo><mfrac><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mn>3</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is equal to

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mi>a</mi><mn mathvariant="italic">x</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mrow><mn>2</mn><mi>x</mi></mrow></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msup><mn>1</mn><mi>&#8734;</mi></msup><mi>&#160;</mi></math>form<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mfenced open="[" close="]" separators="|"><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mi>a</mi><mi>x</mi></mfrac><mo>-</mo><mfrac><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn><mi>x</mi></mrow></mfenced></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>2</mn><mi>a</mi><mo>-</mo><mfrac><mn>8</mn><mi>x</mi></mfrac></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>a</mi></mrow></msup></mrow></msup></math>

<math><mo>&#8756;&#160;&#160;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>2</mn><mi>a</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>=</mo><mn>3</mn><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>a</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q13. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><msqrt><mi>x</mi></msqrt><mi>&#160;</mi></mrow></mfenced><mfrac><mn>1</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mi>P</mi></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mn>2</mn></math>
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><msqrt><mi>x</mi></msqrt></mrow></mfenced><mfrac><mn>1</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>(</mo><msup><mn>1</mn><mo>&#8734;</mo></msup></math> form<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><msup><mfenced close="]" open="["><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></msup><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8594;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8594;</mo><mo>&#8734;</mo><mo>,</mo></math> then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mfenced close="]" open="["><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#183;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>P</mi><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#183;</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>P</mi><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mfenced separators="|"><mfrac><mrow><mi>tan</mi><msqrt><mi>x</mi></msqrt></mrow><msqrt><mi>x</mi></msqrt></mfrac></mfenced><mn>2</mn></msup></mrow></msup></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mi>tan</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><msup><mi mathvariant="normal">e</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>log</mi><mi>P</mi><mo>=</mo><mi>log</mi><mfenced><msup><mi>e</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>.
 </p>

</details>

---

