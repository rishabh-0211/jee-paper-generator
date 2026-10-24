# JEE Advanced Mathematics - Limits

## Topic 3: Trigonometric and Inverse Trigonometric limits

**Total Questions:** 4

---

### Q1. JEE Advanced 2024 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let $S$ be the set of all $(\alpha, \beta) \in \mathbb{R} \times \mathbb{R}$ such that
$\lim _{x \rightarrow \infty} \frac{\sin \left(x^2\right)\left(\log _e x\right)^\alpha \sin \left(\frac{1}{x^2}\right)}{x^{\alpha \beta}\left(\log _e(1+x)\right)^\beta}=0$.
Then which of the following is (are) correct?

**Options:**

- **(A)** $(-1,3) \in S$
- **(B)** $(-1,1) \in S$
- **(C)** $(1,-1) \in S$
- **(D)** $(1,-2) \in S$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(1,-1) \in S$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow \infty} \frac{\sin x^2 \cdot\left(\log _e x\right)^\alpha \cdot \sin \frac{1}{x^2}}{x^{\alpha \beta} \cdot\left(\log _e(1+x)\right)^\beta}=0 \\ & \lim _{x \rightarrow \infty} \frac{\left(\log _e x\right)^\alpha}{\left(\log _e(x+1)\right)^\beta \cdot x^{\alpha \beta+2}}=0\end{aligned}$
$\begin{aligned} & \lim _{x \rightarrow \infty}\left(\frac{\log _e x}{\log _e(x+1)}\right)^\beta \cdot \frac{\left(\log _e x\right)^{\alpha-\beta}}{x^{\alpha \beta+2}}=0 \\ & \lim _{x \rightarrow \infty} \frac{\left(\log _e x\right)^{\alpha-\beta}}{x^{\alpha \beta+2}}=0 \quad \text { Put } \log _e x=t \\ & \lim _{t \rightarrow \infty} \frac{t^{\alpha-\beta}}{\left(e^t\right)^{\alpha \beta+2}}=0\end{aligned}$
As we know $\lim _{x \rightarrow \infty} \frac{x}{e^x}=0$
$\alpha \beta+2>0 \Rightarrow \alpha \beta>-2$

</details>

---

### Q2. JEE Advanced 2024 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $k \in \mathbb{R}$. If $\lim _{x \rightarrow 0^+}(\sin (\sin k x)+\cos x+x)^{\frac{2}{x}}=e^6$, then the value of $k$ is

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

\(\begin{aligned} & l=\lim _{x \rightarrow 0^{+}}(\sin (\sin k x)+\cos x+x)^{\frac{2}{x}}=e^6 \\ & \Rightarrow \ln l=\lim _{x \rightarrow 0^{+}} \frac{2}{x}(\sin (\sin k x)+\cos x+x-1) \\ & \Rightarrow \ln l=\lim _{x \rightarrow 0^{+}} 2\left(\frac{\sin (\sin k x)}{\sin k x} \cdot \frac{\sin k x}{k x} \cdot \frac{k x}{x}+1-\frac{(1-\cos x)}{x^2} \cdot x\right) \\ & \Rightarrow \ln l=2(k+1) \\ & \Rightarrow l=e^{2(k+1)}=e^6 \\ & k+1=3 \\ & \Rightarrow k=2\end{aligned}\)

</details>

---

### Q3. JEE Advanced 2020 (Paper 2)

*Type:* `numerical` | *Level:* `2`

<p>The value of the limit <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><mfrac><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><mfenced><mrow><mi>sin</mi><mn>3</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mfenced><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi><mi>sin</mi><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mi>cos</mi><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>cos</mi><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></mrow></mfrac></math> is _________</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn><mo>&#160;</mo></msqrt><mi>sin</mi><mn>2</mn><mi>x</mi><mo>&#183;</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mi>cos</mi><mfrac><mrow><mn>7</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mi>cos</mi><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>&#183;</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>cos</mi><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn><mo>&#160;</mo></msqrt><mi>sin</mi><mn>2</mn><mi>x</mi><mo>&#183;</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mi>cos</mi><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>cos</mi><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mi>cos</mi><mfrac><mrow><mn>7</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><mfrac><mrow><mn>16</mn><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mo>&#183;</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mi>sin</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mi>sin</mi><mn>3</mn><mi>x</mi><mi>sin</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><mfrac><mrow><mn>16</mn><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mo>&#183;</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mn>2</mn><mi>sin</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mn>3</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><mfrac><mrow><mn>16</mn><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>x</mi><mo>&#160;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>2</mn><mi>sin</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi><mo>&#183;</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></munder><mfrac><mrow><mn>16</mn><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>x</mi></mrow><mrow><mn>2</mn><mi>sin</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle><mo>.</mo><mn>4</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>16</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>16</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mn>8</mn></math>.</p>

</details>

---

### Q4. JEE Advanced 2016 (Paper 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi>R</mi></math> be such that <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi>&#946;</mi><mi>x</mi></mrow></mfenced></mrow></mrow></mrow><mrow><mi>&#945;</mi><mi>x</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mrow><mo>=</mo><mn>1</mn><mo>.</mo></math> Then <math><mn>6</mn><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced></math> equals

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<p>If <math><mi>&#945;</mi><mo>&#8800;</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>x</mi><mi>sin</mi><mfenced><mrow><mi>&#946;</mi><mi>x</mi></mrow></mfenced></mrow><mfenced><mfrac><mrow><mi>&#945;</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mfenced></mfrac><mo>=</mo><mn>0</mn></math>
<math><mo>&#8756;</mo></math> <math><mi>&#945;</mi><mo>=</mo><mn>1</mn></math>
<math><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>&#946;</mi><msup><mi>x</mi><mn>3</mn></msup><mfenced><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi>&#946;</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mi>&#946;</mi><mi>x</mi></mrow></mfrac></mfenced></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac></mfenced></mrow></mfrac><mo>=</mo><mfrac><mfrac><mi>&#946;</mi><mn>1</mn></mfrac><mn>6</mn></mfrac></math></p><p>Using,<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mi>sinx</mi></mrow><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#160;&#38;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mi mathvariant="italic">sinx</mi><mi>x</mi></mfrac><mo>=</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>&#946;</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>7</mn></math></p><p> </p>

</details>

---

