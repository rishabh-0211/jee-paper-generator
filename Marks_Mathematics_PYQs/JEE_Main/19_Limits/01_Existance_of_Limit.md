# JEE Main Mathematics - Limits

## Topic 1: Existance of Limit

**Total Questions:** 14

---

### Q1. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\displaystyle\lim_{x \to 2} \dfrac{\sin(x^3 - 5x^2 + ax + b)}{(\sqrt{x-1} - 1)\log_e(x-1)} = m$, then $a + b + m$ is equal to :

**Options:**

- **(A)** $5$
- **(B)** $6$
- **(C)** $8$
- **(D)** $10$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6$**

**Detailed Solution:**

Let $x - 2 = t$. As $x \to 2$, $t \to 0$.

The given limit can be written as:

$\lim_{t \to 0} \dfrac{\sin((t+2)^3 - 5(t+2)^2 + a(t+2) + b)}{(\sqrt{t+1} - 1)\log_e(t+1)} = m$

The denominator can be approximated for small $t$ as:

$\lim_{t \to 0} \dfrac{\sqrt{t+1} - 1}{t} \cdot \dfrac{\log_e(t+1)}{t} \cdot t^2 = \dfrac{1}{2} \cdot 1 \cdot t^2 = \dfrac{t^2}{2}$

For the limit to be finite, the argument of the sine function in the numerator must have $t^2$ as its lowest degree term in its expansion.

Let $P(t) = (t+2)^3 - 5(t+2)^2 + a(t+2) + b$

$P(t) = t^3 + 6t^2 + 12t + 8 - 5(t^2 + 4t + 4) + at + 2a + b$

$P(t) = t^3 + t^2 + (a - 8)t + (2a + b - 12)$

For the limit to exist, the constant and linear terms must be zero:

$a - 8 = 0 \Rightarrow a = 8$

$2a + b - 12 = 0 \Rightarrow 16 + b - 12 = 0 \Rightarrow b = -4$

Substituting $a$ and $b$ back into $P(t)$:

$P(t) = t^3 + t^2$

The limit becomes:

$m = \lim_{t \to 0} \dfrac{\sin(t^3 + t^2)}{t^2 / 2}$

$m = \lim_{t \to 0} \dfrac{\sin(t^2(t+1))}{t^2(t+1)} \cdot \dfrac{t^2(t+1)}{t^2 / 2} = 1 \cdot 2 = 2$

Therefore, $a + b + m = 8 - 4 + 2 = 6$.

Answer: $6$

</details>

---

### Q2. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 0^{+}} \frac{\tan \left(5(x)^{\frac{1}{3}}\right) \log _e\left(1+3 x^2\right)}{\left(\tan ^{-1} 3 \sqrt{x}\right)^2\left(e^{5(x)^{\frac{4}{3}}}-1\right)}$ is equal to

**Options:**

- **(A)** $\frac{1}{15}$
- **(B)** 1
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{5}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{3}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0^{\cdot}}\left(\frac{\tan \left(5 \mathrm{x}^{1 / 3}\right)}{5 \mathrm{x}^{1 / 3}}\right) \cdot\left(\frac{(3 \sqrt{\mathrm{x}})^2}{\left(\tan ^{-1} 3 \sqrt{\mathrm{x}}\right)^2}\right)\left(\frac{\ell\left(1+3 \mathrm{x}^2\right)}{3 \mathrm{x}^2}\right)\left(\frac{5 \mathrm{x}^{4 / 3}}{\mathrm{e}^{5 x^4}-1}\right) \times \frac{5 \mathrm{x}^{1 / 3} \cdot 3 \mathrm{x}^2}{5 \mathrm{x}^{4 / 3} \cdot 9 \mathrm{x}} \\ & =\frac{1}{3}\end{aligned}$

</details>

---

### Q3. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mi>x</mi><mo>−</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>x</mi><mo> </mo><mtext>is even</mtext><mo>,</mo></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>,</mo><mo> </mo><mi>x</mi><mo> </mo><mtext>is odd</mtext><mo>,</mo></mtd></mtr></mtable></mfenced><mi>x</mi><mo>∈</mo><mi>N</mi></math>. If for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>∈</mo><mi>N</mi><mo>,</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>21</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mi>a</mi><mo>−</mo></msup></mrow></munder><mfenced close="}" open="{"><mrow><mfrac><msup><mfenced close="|" open="|"><mi>x</mi></mfenced><mn>3</mn></msup><mi>a</mi></mfrac><mo>−</mo><mfenced close="]" open="["><mfrac><mi>x</mi><mi>a</mi></mfrac></mfenced></mrow></mfenced><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>, is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>121</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>144</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>169</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>225</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>144</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mi>x</mi><mo>−</mo><mn>1</mn><mo>;</mo><mo> </mo><mi>x</mi><mo> </mo><mtext>is even</mtext></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>:</mo><mo> </mo><mi>x</mi><mo> </mo><mtext>is odd</mtext></mtd></mtr></mtable></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>21</mn></math></p><p>Case-I: If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is even</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>=</mo><mi>a</mi><mo>−</mo><mn>1</mn><mo>=</mo><mtext>Odd</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mi>a</mi><mo>−</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mtext>Even</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>2</mn><mi>a</mi><mo>−</mo><mn>3</mn><mo>=</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>12</mn></math></p><p>Case-II: If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is odd</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>=</mo><mn>2</mn><mi>a</mi><mo>=</mo><mtext>Even</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow></mfenced><mo>=</mo><mn>2</mn><mi>a</mi><mo>−</mo><mn>1</mn><mo>=</mo><mtext>Odd</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>a</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>4</mn><mi>a</mi><mo>−</mo><mn>2</mn><mo>=</mo><mn>21</mn></math> (Not possible)</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>12</mn></math></p><p>Now,<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mn>12</mn><mo>−</mo></msup></mrow></munder><mfenced><mrow><mfrac><msup><mfenced close="|" open="|"><mi>x</mi></mfenced><mn>3</mn></msup><mn>12</mn></mfrac><mo>−</mo><mfenced close="]" open="["><mfrac><mi>x</mi><mn>12</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mn>12</mn><mo>−</mo></msup></mrow></munder><mfrac><msup><mfenced close="|" open="|"><mi>x</mi></mfenced><mn>3</mn></msup><mn>12</mn></mfrac><mo>−</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mn>12</mn><mo>−</mo></msup></mrow></munder><mfenced close="]" open="["><mfrac><mi>x</mi><mn>12</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mn>12</mn><mo>−</mo></msup></mrow></munder><mfenced><mrow><mfrac><msup><mfenced close="|" open="|"><mi>x</mi></mfenced><mn>3</mn></msup><mn>12</mn></mfrac><mo>−</mo><mfenced close="]" open="["><mfrac><mi>x</mi><mn>12</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mn>144</mn><mo>-</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mn>12</mn><mo>−</mo></msup></mrow></munder><mfenced><mrow><mfrac><msup><mfenced close="|" open="|"><mi>x</mi></mfenced><mn>3</mn></msup><mn>12</mn></mfrac><mo>−</mo><mfenced close="]" open="["><mfrac><mi>x</mi><mn>12</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mn>144</mn></math></p>

</details>

---

### Q4. JEE Main 2024 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mi>x</mi></mfenced></math> denote the fractional part of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mi>cos</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mfenced close="}" open="{"><mi>x</mi></mfenced><mn>2</mn></msup></mrow></mfenced><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>−</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></mrow></mfenced></mrow><mrow><mfenced close="}" open="{"><mi>x</mi></mfenced><mo>−</mo><msup><mfenced close="}" open="{"><mi>x</mi></mfenced><mn>3</mn></msup></mrow></mfrac><mo>,</mo><mi>x</mi><mo>≠</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo> </mo><mtext>and</mtext><mo> </mo><mi>R</mi></math> respectively denotes the left hand limit and the right hand limit of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>32</mn><msup><mi>π</mi><mn>2</mn></msup></mfrac><mfenced><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>+</mo><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced></math> is equal to __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mi>cos</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mfenced close="}" open="{"><mi>x</mi></mfenced><mn>2</mn></msup></mrow></mfenced><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>−</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></mrow></mfenced></mrow><mrow><mfenced close="}" open="{"><mi>x</mi></mfenced><mo>−</mo><msup><mfenced close="}" open="{"><mi>x</mi></mfenced><mn>3</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>RHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mrow><mn>0</mn><mo>+</mo><mi>h</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>RHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mi>h</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>RHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mi>h</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>−</mo><mi>h</mi></mrow></mfenced></mrow><mrow><mi>h</mi><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mi>h</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>RHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mi>h</mi><mn>2</mn></msup></mrow></mfenced></mrow><mi>h</mi></mfrac><mfenced><mfrac><mrow><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mn>1</mn></mrow><mn>1</mn></mfrac></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mi>h</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mi>θ</mi><mo>⇒</mo><mi>cos</mi><mi>θ</mi><mo>=</mo><mn>1</mn><mo>−</mo><msup><mi>h</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>RHL</mi><mo>=</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><munder><mi>lim</mi><mrow><mi>θ</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mi>θ</mi><msqrt><mn>1</mn><mo>−</mo><mi>cos</mi><mi>θ</mi></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>RHL</mi><mo>=</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><munder><mi>lim</mi><mrow><mi>θ</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mn>1</mn><msqrt><mfrac><mrow><mn>1</mn><mo>−</mo><mi>cos</mi><mi>θ</mi></mrow><msup><mi>θ</mi><mn>2</mn></msup></mfrac></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>RHL</mi><mo>=</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><mfrac><mn>1</mn><msqrt><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>RHL</mi><mo>=</mo><mfrac><mi>π</mi><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>R</mi><mo>=</mo><mfrac><mi>π</mi><msqrt><mn>2</mn></msqrt></mfrac></math></p><p>Now finding left hand limit,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>LHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><msup><mn>0</mn><mo>−</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>LHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mrow><mo>−</mo><mi>h</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>LHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mfenced close="}" open="{"><mrow><mo>−</mo><mi>h</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>−</mo><mfenced close="}" open="{"><mrow><mo>−</mo><mi>h</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mfenced close="}" open="{"><mrow><mo>−</mo><mi>h</mi></mrow></mfenced><mo>−</mo><msup><mfenced close="}" open="{"><mrow><mo>−</mo><mi>h</mi></mrow></mfenced><mn>3</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>LHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mfenced><mrow><mo>−</mo><mi>h</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>−</mo><mfenced><mrow><mo>−</mo><mi>h</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></mrow><mrow><mfenced><mrow><mo>−</mo><mi>h</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>−</mo><msup><mfenced><mrow><mo>−</mo><mi>h</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>LHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mo>−</mo><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>h</mi></mrow></mfenced><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>h</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>−</mo><mi>h</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mfenced><mrow><mn>1</mn><mo>−</mo><mi>h</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>LHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mi>π</mi><mn>2</mn></mfrac></mfenced><mfrac><mrow><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>h</mi></mrow><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mfenced><mrow><mn>1</mn><mo>−</mo><mi>h</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>LHL</mi><mo>=</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>h</mi></mrow><mrow><mo>−</mo><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>h</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>LHL</mi><mo>=</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><munder><mi>lim</mi><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>h</mi></mrow><mi>h</mi></mfrac></mfenced><mfenced><mfrac><mn>1</mn><mrow><mo>−</mo><mi>h</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>LHL</mi><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>L</mi><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>32</mn><msup><mi>π</mi><mn>2</mn></msup></mfrac><mfenced><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>+</mo><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mfrac><mn>32</mn><msup><mi>π</mi><mn>2</mn></msup></mfrac><mfenced><mrow><mfrac><msup><mi>π</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>π</mi><mn>2</mn></msup><mn>16</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>32</mn><msup><mi>π</mi><mn>2</mn></msup></mfrac><mfenced><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>+</mo><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>16</mn><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>32</mn><msup><mi>π</mi><mn>2</mn></msup></mfrac><mfenced><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>+</mo><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>18</mn></math></p>

</details>

---

### Q5. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The set of values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mfenced><mrow><mfenced open="[" close="]"><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mfenced open="[" close="]"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math>, where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>&#950;</mi></mfenced></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#950;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>7</mn><mo>.</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>6</mn><mo>.</mo><mn>5</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>7</mn><mo>.</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>6</mn><mo>.</mo><mn>5</mn><mo>]</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mn>7</mn><mo>.</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>6</mn><mo>.</mo><mn>5</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>7</mn><mo>.</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>6</mn><mo>.</mo><mn>5</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>7</mn><mo>.</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>6</mn><mo>.</mo><mn>5</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mfenced><mrow><mfenced open="[" close="]"><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mfenced open="[" close="]"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mfenced><mrow><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>-</mo><mn>5</mn><mo>-</mo><mfenced open="[" close="]"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mfenced><mrow><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>-</mo><mfenced open="[" close="]"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mfenced><mrow><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>-</mo><mfenced open="[" close="]"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>7</mn></math></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>I</mi></math> (integer) then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>2</mn><mi>a</mi><mo>=</mo><mn>7</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>7</mn></math></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>I</mi><mo>+</mo><mi>f</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is fraction,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>I</mi><mo>+</mo><mi>f</mi></mrow></mfenced><mo>-</mo><mfenced open="[" close="]"><mrow><mn>2</mn><mi>I</mi><mo>+</mo><mn>2</mn><mi>f</mi></mrow></mfenced><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>+</mo><mfenced open="[" close="]"><mi>f</mi></mfenced><mo>-</mo><mn>2</mn><mi>I</mi><mo>-</mo><mfenced open="[" close="]"><mrow><mn>2</mn><mi>f</mi></mrow></mfenced><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>+</mo><mn>0</mn><mo>-</mo><mn>2</mn><mi>I</mi><mo>-</mo><mfenced open="[" close="]"><mrow><mn>2</mn><mi>f</mi></mrow></mfenced><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mi>I</mi><mo>-</mo><mfenced open="[" close="]"><mrow><mn>2</mn><mi>f</mi></mrow></mfenced><mo>=</mo><mn>7</mn></math></p><p>Now taking case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mi>I</mi><mo>-</mo><mn>0</mn><mo>=</mo><mn>7</mn><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>7</mn><mo>&#8658;</mo><mi>a</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>7</mn><mo>,</mo><mo>-</mo><mn>6</mn><mo>.</mo><mn>5</mn></mrow></mfenced></math></p><p>Now taking case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>I</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>7</mn><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>8</mn><mo>&#8658;</mo><mi>a</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>7</mn><mo>.</mo><mn>5</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math></p><p>Hence, from both the cases we can say that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>7</mn><mo>.</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>6</mn><mo>.</mo><mn>5</mn></mrow></mfenced></math>.</p>

</details>

---

### Q6. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a function defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mfenced close="]" open="["><mi>x</mi></mfenced></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mi>a</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> is the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><mn>1</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced></math> exists, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mfenced close="]" open="["><mi>x</mi></mfenced></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mi>a</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math></p><p>Now given <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><mn>1</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced></math> exists,</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><msup><mn>1</mn><mo>+</mo></msup></mrow></munder><mi>a</mi><mi>sin</mi><mfenced><mrow><mi>&#960;</mi><mfrac><mfenced close="]" open="["><mi>x</mi></mfenced><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>a</mi><mo>+</mo><mn>2</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></munder><mo>asin</mo><mfenced><mrow><mi>&#960;</mi><mfrac><mfenced close="]" open="["><mi>x</mi></mfenced><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>3</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><mn>1</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced></math> exist when <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>a</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>3</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>3</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>3</mn><mn>4</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>4</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mo>-</mo><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mfenced close="]" open="["><mi>x</mi></mfenced></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mo>-</mo><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mfenced close="]" open="["><mi>x</mi></mfenced></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>3</mn></msubsup><mo>-</mo><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mfenced close="]" open="["><mi>x</mi></mfenced></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>3</mn><mn>4</mn></msubsup><mo>-</mo><mi>sin</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mfenced close="]" open="["><mi>x</mi></mfenced></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>0</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>0</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>2</mn><mn>3</mn></msubsup><mfenced><mrow><mn>0</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>3</mn><mn>4</mn></msubsup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q7. JEE Main 2022 (26 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>&#945;</mi><mi>x</mi><mo>-</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>&#945;</mi><mi>x</mi><mfenced><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math> for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>14</mn><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>&#945;</mi><mi>x</mi><mo>-</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>&#945;</mi><mi>x</mi><mfenced><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup></mrow><mrow><mfrac><mrow><mi>&#945;</mi><mi>x</mi><mfenced><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>3</mn><mi>x</mi></mrow></mfrac><mo>&#183;</mo><mn>3</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>&#945;</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup></mrow><mrow><mn>3</mn><mi>&#945;</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mi>&#946;</mi></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow><mi>x</mi></mfrac><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>&#945;</mi><mo>-</mo><mn>3</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup></mrow><mrow><mn>6</mn><mi>&#945;</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>&#946;</mi></math>   [Using L&#39; Hospital rule as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>0</mn><mn>0</mn></mfrac><mo>&#160;</mo><mtext>form</mtext></mrow></mfenced></math>]</p><p>Now for limit to exist, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>3</mn><mo>-</mo><mn>3</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup></mrow><mrow><mn>6</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mi>&#946;</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mo>-</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>6</mn><mi>x</mi></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mo>-</mo><mn>3</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup></mrow><mn>6</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math></p></blockquote>

</details>

---

### Q8. JEE Main 2022 (27 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> denote the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>t</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mi>t</mi></mfenced></math> denote the fractional part of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>. Then integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> for which the left hand limit of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfrac><mrow><msup><mi>&#945;</mi><mrow><mn>2</mn><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></mrow></msup><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></mrow></mfrac></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math> is _____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfrac><mrow><msup><mi>&#945;</mi><mrow><mn>2</mn><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></mrow></msup><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>&#945;</mi><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfrac><mrow><msup><mi>&#945;</mi><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></mrow></msup><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></mrow></mfrac><mo>=</mo><mi>&#945;</mi><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>+</mo><mfrac><mrow><msup><mi>&#945;</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mn>2</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>&#945;</mi><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><mo>=</mo><mi>&#945;</mi><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><mo>=</mo><mfrac><mn>10</mn><mn>3</mn></mfrac></math></p><p>On solving above equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>;</mo><mi>&#945;</mi><mo>&#8712;</mo><mi>I</mi></math></p>

</details>

---

### Q9. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> be an integer such that <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>7</mn></mrow></munder><mfrac><mrow><mn>18</mn><mo>-</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mn>3</mn><mi>a</mi></mrow></mfenced></mfrac></math> exists, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> is greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>t</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>6</mn></math>**

**Detailed Solution:**

<p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>7</mn></mrow></munder><mfrac><mrow><mn>18</mn><mo>-</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mn>3</mn><mi>a</mi></mrow></mfenced></mfrac></math> exists <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>&#8712;</mo><mi mathvariant="normal">&#120128;</mi></mrow></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi mathvariant="normal">L</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">L</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">L</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>18</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced></mrow><mfenced open="[" close="]"><mrow><mn>7</mn><mo>-</mo><mi>h</mi><mo>-</mo><mn>3</mn><mi>a</mi></mrow></mfenced></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>18</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>7</mn></mrow></mfenced></mrow><mfenced open="[" close="]"><mrow><mn>7</mn><mo>+</mo><mi>h</mi><mo>-</mo><mn>3</mn><mi>a</mi></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mn>24</mn><mrow><mfenced><mrow><mn>7</mn><mo>-</mo><mn>3</mn><mi>a</mi></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mo>-</mo><mi>h</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mn>25</mn><mrow><mfenced><mrow><mn>7</mn><mo>-</mo><mn>3</mn><mi>a</mi></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mi>h</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>24</mn><mrow><mn>6</mn><mo>-</mo><mn>3</mn><mi>a</mi></mrow></mfrac><mo>=</mo><mfrac><mn>25</mn><mrow><mn>7</mn><mo>-</mo><mn>3</mn><mi>a</mi></mrow></mfrac></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>6</mn></math></p>

</details>

---

### Q10. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>t</mi></mfenced></math> denote the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>t</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#160;</mo><mi>&#949;</mi><mo>&#160;</mo><mi>R</mi><mo>&#8722;</mo><mfenced open="{" close="}"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="|" close="|"><mfrac><mrow><mn>1</mn><mo>&#8722;</mo><mi>x</mi><mo>+</mo><mfenced open="|" close="|"><mi>x</mi></mfenced></mrow><mrow><mi>&#955;</mi><mo>&#8722;</mo><mi>x</mi><mo>+</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></mrow></mfrac></mfenced><mo>=</mo><mi>L</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>&#8722;</mo><mi>x</mi><mo>+</mo><mfenced close="|" open="|"><mi>x</mi></mfenced></mrow><mrow><mi>&#955;</mi><mo>&#8722;</mo><mi>x</mi><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></mfrac></mfenced><mo>=</mo><mi>L</mi></math></p><p>Let&#39;s find left-hand and right-hand limit.</p><p>For left-hand limit</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>-</mo><mi>h</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8594;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>h</mi><mo>&#8594;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mi>h</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mi>H</mi><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>&#8722;</mo><mfenced><mrow><mo>-</mo><mi>h</mi></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mi>h</mi></mrow></mfenced></mrow><mrow><mi>&#955;</mi><mo>&#8722;</mo><mfenced><mrow><mo>-</mo><mi>h</mi></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mo>-</mo><mi>h</mi></mrow></mfenced></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>L</mi><mi>H</mi><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>h</mi><mo>-</mo><mfenced><mrow><mo>-</mo><mi>h</mi></mrow></mfenced></mrow><mrow><mi>&#955;</mi><mo>+</mo><mi>h</mi><mo>+</mo><mfenced close="]" open="["><mrow><mo>-</mo><mi>h</mi></mrow></mfenced></mrow></mfrac></mfenced></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mi>h</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>L</mi><mi>H</mi><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>h</mi><mo>+</mo><mi>h</mi></mrow><mrow><mi>&#955;</mi><mo>+</mo><mi>h</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mfenced close="|" open="|"><mrow><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p>For right-hand limit</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>+</mo><mi>h</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8594;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>h</mi><mo>&#8594;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mi>h</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mi>H</mi><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>&#8722;</mo><mi>h</mi><mo>+</mo><mfenced close="|" open="|"><mi>h</mi></mfenced></mrow><mrow><mi>&#955;</mi><mo>&#8722;</mo><mi>h</mi><mo>+</mo><mfenced close="]" open="["><mi>h</mi></mfenced></mrow></mfrac></mfenced></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mfenced close="]" open="["><mi>h</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>R</mi><mi>H</mi><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>h</mi><mo>+</mo><mi>h</mi></mrow><mrow><mi>&#955;</mi><mo>+</mo><mi>h</mi><mo>+</mo><mn>0</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mfenced close="|" open="|"><mi>&#955;</mi></mfenced></mfrac></math></p><p>For existence of limit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mi>H</mi><mi>L</mi><mo>=</mo><mi>R</mi><mi>H</mi><mi>L</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mfenced close="|" open="|"><mrow><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac><mo>=</mo><mfrac><mn>1</mn><mfenced close="|" open="|"><mi>&#955;</mi></mfenced></mfrac></math></p><p>Cross multiply and square both side.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>&#160;</mo><mo>&#8658;</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>=</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Limit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mfrac><mn>1</mn><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mfrac><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q11. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>,</mo><mtext>&#8201;</mtext><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> where <math><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced></math> denotes the greatest integer function, then:

**Options:**

- **(A)** <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>4</mn><mo>+</mo></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> exists but <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>4</mn><mo>-</mo></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> does not exist
- **(B)** <math><mi>f</mi></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math>
- **(C)** <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>4</mn><mo>-</mo></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> exists but <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>4</mn><mo>+</mo></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> does not exist
- **(D)** Both <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>4</mn><mo>-</mo></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> and <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>4</mn><mo>+</mo></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> exist but are not equal

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>f</mi></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>.</mo><mi>H</mi><mo>.</mo><mi>L</mi><mo>.</mo><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>4</mn><mo>+</mo></msup></mrow></munder><mfenced open="[" close="]" separators="|"><mi>x</mi></mfenced><mo>-</mo><mfenced open="[" close="]" separators="|"><mfrac><mi>x</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>4</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>.</mo><mi>H</mi><mo>.</mo><mi>L</mi><mo>.</mo><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>4</mn><mo>-</mo></msup></mrow></munder><mfenced open="[" close="]" separators="|"><mi>x</mi></mfenced><mo>-</mo><mfenced open="[" close="]" separators="|"><mfrac><mi>x</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>3</mn><mo>-</mo><mn>0</mn><mo>=</mo><mn>3</mn></math></p><p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>4</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>.</mo><mi>H</mi><mo>.</mo><mi>L</mi><mo>.</mo><mo>=</mo><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mi>R</mi><mo>.</mo><mi>H</mi><mo>.</mo><mi>L</mi><mo>.</mo></math></p><p>Hence, given function is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn><mo>.</mo></math></p>

</details>

---

### Q12. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For each <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>, let <math><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced></math> be the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><mi>x</mi><mfenced separators="|"><mrow><mfenced open="[" close="]" separators="|"><mi>x</mi></mfenced><mo>+</mo><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced></mrow></mfenced><mi>sin</mi><mo>&#8289;</mo><mfenced open="[" close="]" separators="|"><mi>x</mi></mfenced></mrow><mfenced open="|" close="|" separators="|"><mi>x</mi></mfenced></mfrac></math> is equal to

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mn>0</mn></math>
- **(C)** <math><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>1</mn></mrow></mrow></math>
- **(D)** <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mn>1</mn></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>1</mn></mrow></mrow></math>**

**Detailed Solution:**

<math><mo>=</mo><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><mi>x</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow></mrow><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfrac></mrow></mrow></math>

<math><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder><mfrac><mrow><mi>x</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mrow></mrow><mrow><mo>-</mo><mi>x</mi></mrow></mfrac></math>     <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo></mrow></mfenced></math>

<math><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder><mo>-</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>1</mn></mrow></mrow></math>       <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>sin</mi><mfenced><mrow><mo>-</mo><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math>

<math><mo>=</mo><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>1</mn></mrow></mrow></math>.

</details>

---

### Q13. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `3`

For each <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mi>t</mi></mfenced></math> be the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>. Then<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>x</mi><mfenced separators="|"><mrow><mfenced open="[" close="]" separators="|"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mfenced open="[" close="]" separators="|"><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfenced open="[" close="]" separators="|"><mfrac><mn>15</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced></math>

**Options:**

- **(A)** does not exist <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>in</mi><mo>&#160;</mo><mi>R</mi></mrow></mfenced></math>
- **(B)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>
- **(D)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math>**

**Detailed Solution:**

<p>We know that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>&#8722;</mo><mn>1</mn><mo>&#60;</mo><mfenced close="]" open="["><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>&#8804;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></math></p><p>Hence, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>. . .</mo><mo>+</mo><mn>15</mn></mrow><mi>x</mi></mfrac><mo>&#8722;</mo><mn>15</mn><mo>&#60;</mo><mfenced close="]" open="["><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mfenced close="]" open="["><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mn>....</mn><mo>+</mo><mfenced close="]" open="["><mfrac><mn>15</mn><mi>x</mi></mfrac></mfenced><mo>&#8804;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>...</mn><mo>+</mo><mn>15</mn></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>x</mi><mfenced><mrow><mfenced close="]" open="["><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mfenced close="]" open="["><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mo>.</mo><mo>...</mo><mo>+</mo><mfenced close="]" open="["><mfrac><mn>15</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>=</mo><mn>15</mn><mfenced><mfrac><mn>16</mn><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>120</mn></math></p>

</details>

---

### Q14. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

$\operatorname{Lim}_{x \rightarrow 0} \frac{\log x^n-[x]}{[x]}, \mathrm{n} \in \mathrm{N}([\mathrm{x}]$ denotes greatest integer less than or equal to $\mathrm{x})$

**Options:**

- **(A)** has value -1
- **(B)** has value 0
- **(C)** has value 1
- **(D)** does not exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) does not exist**

**Detailed Solution:**

Since $\operatorname{Lim}_{x \rightarrow 0}[x]$ does not exist, hence the required limit does not exist

</details>

---

