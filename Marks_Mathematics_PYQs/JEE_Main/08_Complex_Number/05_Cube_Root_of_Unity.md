# JEE Main Mathematics - Complex Number

## Topic 5: Cube Root of Unity

**Total Questions:** 18

---

### Q1. JEE Main 2026 (22 January Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $\alpha=\frac{-1+i \sqrt{3}}{2}$ and $\beta=\frac{-1-i \sqrt{3}}{2}, i=\sqrt{-1}$. If $(7-7 \alpha+9 \beta)^{20}+(9+7 \alpha-7 \beta)^{20}+(-7+9 \alpha+7 \beta)^{20}+(14+7 \alpha+7 \beta)^{20}=m^{10}$, then $m$ is $\_\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **49**

**Detailed Solution:**

$\alpha = \omega$, $\beta = \omega^2$ (cube roots of unity).
Let $z_1 = 7-7\omega+9\omega^2$, $z_2 = 9+7\omega-7\omega^2$, $z_3 = -7+9\omega+7\omega^2$.
Calculating: $z_1 = 6-8i\sqrt{3}$, $z_2 = 9+7i\sqrt{3}$, $z_3 = -15+i\sqrt{3}$.
All have $|z_k| = \sqrt{228}$.
Verify: $z_2 = z_1\omega$, $z_3 = z_1\omega^2$.
$z_1^{20}+z_2^{20}+z_3^{20} = z_1^{20}(1+\omega^{20}+\omega^{40}) = z_1^{20}(1+\omega^2+\omega) = 0$.
Fourth term: $14+7\omega+7\omega^2 = 14+7(-1) = 7$. So $7^{20} = 49^{10}$.
Total $= 0 + 49^{10} = m^{10} \Rightarrow m = 49$.

</details>

---

### Q2. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x^{2}+x+1=0$, then the value of $\left(x+\frac{1}{x}\right)^{4}+\left(x^{2}+\frac{1}{x^{2}}\right)^{4}+\left(x^{3}+\frac{1}{x^{3}}\right)^{4}+\ldots+\left(x^{25}+\frac{1}{x^{25}}\right)^{4}$ is:

**Options:**

- **(A)** 162
- **(B)** 175
- **(C)** 145
- **(D)** 128

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 145**

**Detailed Solution:**

Given $x^2 + x + 1 = 0$, so $x = \omega$ (primitive cube root of unity) with $x^3 = 1$.
From the equation: $x + \frac{1}{x} = -1$.
Since $x^3 = 1$, value of $x^n + x^{-n}$ has period 3:
$n \equiv 0 \pmod{3}$: $x^n + x^{-n} = 2$
$n \equiv 1, 2 \pmod{3}$: $x^n + x^{-n} = -1$
Fourth powers: $(2)^4 = 16$, $(-1)^4 = 1$.
For $n = 1$ to $25$: 8 multiples of 3 contribute $8 \times 16 = 128$, remaining 17 terms contribute $17 \times 1 = 17$.
Total $= 128 + 17 = 145$.

</details>

---

### Q3. JEE Main 2025 (4 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

If $\alpha$ is a root of the equation $x^2+x+1=0$ and $\sum_{\mathrm{k}=1}^{\mathrm{n}}\left(\alpha^{\mathrm{k}}+\frac{1}{\alpha^{\mathrm{k}}}\right)^2=20$, then n is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11**

**Detailed Solution:**

$\begin{aligned} & \alpha=\omega \\ & \therefore\left(\omega^k+\frac{1}{\omega^k}\right)^2=\omega^{2 k}+\frac{1}{\omega^{2 k}}+2 \\ & =\omega^{2 k}+\omega^k+2 \quad \because \omega^{3 k}=1\end{aligned}$
$\begin{aligned}
& \therefore \sum_{\mathrm{k}=1}^{\mathrm{n}}\left(\omega^{2 \mathrm{k}}+\omega^{\mathrm{k}}+2\right)=20 \\
& \Rightarrow\left(\omega^2+\omega^4+\omega^6+\ldots+\omega^{2 \mathrm{n}}\right)+\left(\omega+\omega^2+\omega^3+\ldots+\right. \\
& \left.\omega^{\mathrm{n}}\right)+2 \mathrm{n}=20
\end{aligned}$
Now if $n=3 m, \quad m \in I$
Then $0+0+2 \mathrm{n}=20 \Rightarrow \mathrm{n}=10$ (not satisfy)
if $n=3 m+1$, then
$\begin{aligned}
& \omega^2+\omega+2 \mathrm{n}=20 \\
& -1+2 \mathrm{n}=20 \Rightarrow \mathrm{n}=\frac{21}{2}(\text { not possible })
\end{aligned}$
if $n=3 m+2$,
$\begin{aligned}
& \left(\omega^8+\omega^{10}\right)+\left(\omega^4+\omega^5\right)+2 \mathrm{n}=20 \\
& \Rightarrow\left(\omega^2+\omega\right)+\left(\omega+\omega^2\right)+2 \mathrm{n}=20 \\
& 2 \mathrm{n}=22 \\
& \mathrm{n}=11 \text { satisfy } \mathrm{n}=3 \mathrm{~m}+2 \\
& \therefore \mathrm{n}=11
\end{aligned}$

</details>

---

### Q4. JEE Main 2025 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let integers $\mathrm{a}, \mathrm{b} \in[-3,3]$ be such that $\mathrm{a}+\mathrm{b} \neq 0$. Then the number of all possible ordered pairs
(a, b), for which $\left|\frac{z-\mathrm{a}}{z+\mathrm{b}}\right|=1$ and $\left|\begin{array}{ccc}z+1 & \omega & \omega^2 \\ \omega & z+\omega^2 & 1 \\ \omega^2 & 1 & z+\omega\end{array}\right|=1, z \in \mathrm{C}$, where $\omega$ and $\omega^2$ are the roots of $x^2+x+1=0$, is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

$\begin{aligned} & a, b \in I,-3 \leq a, b \leq 3, a+b \neq 0 \\ & |z-a|=|z+b| \\ & \left|\begin{array}{ccc}z+1 & \omega & \omega^2 \\ \omega & z+\omega^2 & 1 \\ \omega^2 & 1 & z+\omega\end{array}\right|=1 \\ & \Rightarrow\left|\begin{array}{ccc}z & z & z \\ \omega & z+\omega^2 & 1 \\ \omega^2 & 1 & z+\omega\end{array}\right|=1\end{aligned}$


$\begin{aligned} & \Rightarrow z\left|\begin{array}{ccc}1 & 1 & 1 \\ \omega & z+\omega^2 & 1 \\ \omega^2 & 1 & z+\omega\end{array}\right|=1 \\ & \Rightarrow z\left|\begin{array}{ccc}1 & 0 & 0 \\ \omega & z+\omega^2-\omega & 1-\omega \\ \omega^2 & 1-\omega^2 & z+\omega-\omega^2\end{array}\right|=1 \\ & \Rightarrow z^3=1 \\ & \Rightarrow z=\omega, \omega^2, 1\end{aligned}$


Now
$\begin{aligned}
& |1-\mathrm{a}|=|1+\mathrm{b}| \\
& \Rightarrow 10 \text { pairs }
\end{aligned}$

</details>

---

### Q5. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> is a complex number, then the number of common roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>1985</mn></msup><mo>+</mo><msup><mi>z</mi><mn>100</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>z</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>, is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>1985</mn></msup><mo>+</mo><msup><mi>z</mi><mn>100</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>  </mo><mo>&amp;</mo><mo>  </mo><msup><mi>z</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>z</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>z</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>-</mo><mi>z</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mi>z</mi><mfenced><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>z</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mi>ω</mi><mo>,</mo><mo> </mo><msup><mi>ω</mi><mn>2</mn></msup></math></p><p>Now putting  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">z</mi><mo>=</mo><mi>ω</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>1985</mn></msup><mo>+</mo><msup><mi>z</mi><mn>100</mn></msup><mo>+</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>ω</mi><mn>1985</mn></msup><mo>+</mo><msup><mi>ω</mi><mn>100</mn></msup><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>ω</mi><mn>2</mn></msup><mo>+</mo><mi>ω</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><msup><mi>ω</mi><mrow><mn>3</mn><mi>n</mi></mrow></msup><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">z</mi><mo>=</mo><msup><mi>ω</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>ω</mi><mn>3970</mn></msup><mo>+</mo><msup><mi>ω</mi><mn>200</mn></msup><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>ω</mi><mo>+</mo><msup><mi>ω</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> will not satisfy the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>1985</mn></msup><mo>+</mo><msup><mi>z</mi><mn>100</mn></msup><mo>+</mo><mn>1</mn></math></p><p>Hence, there are two common root</p></blockquote>

</details>

---

### Q6. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math> satisfies the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mi>α</mi><msup><mo>)</mo><mn>7</mn></msup><mo>=</mo><mi mathvariant="normal">A</mi><mo>+</mo><mi mathvariant="normal">B</mi><mi>α</mi><mo>+</mo><mi mathvariant="normal">C</mi><msup><mi>α</mi><mn>2</mn></msup><mo>,</mo><mo> </mo><mi mathvariant="normal">A</mi><mo>,</mo><mo> </mo><mi mathvariant="normal">B</mi><mo>,</mo><mi mathvariant="normal">C</mi><mo>≥</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>(</mo><mn>3</mn><mo> </mo><mi mathvariant="normal">A</mi><mo>-</mo><mn>2</mn><mo> </mo><mi mathvariant="normal">B</mi><mo>-</mo><mi mathvariant="normal">C</mi><mo>)</mo></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>ω</mi><mo>+</mo><msup><mi>ω</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math>.</p><p>So, the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ω</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ω</mi><mn>2</mn></msup></math>.</p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mi>ω</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>α</mi></mrow></mfenced><mn>7</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>ω</mi></mrow></mfenced><mn>7</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>α</mi></mrow></mfenced><mn>7</mn></msup><mo>=</mo><msup><mfenced><mrow><mo>-</mo><msup><mi>ω</mi><mn>2</mn></msup></mrow></mfenced><mn>7</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>α</mi></mrow></mfenced><mn>7</mn></msup><mo>=</mo><mo>-</mo><msup><mi>ω</mi><mn>14</mn></msup></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ω</mi><mrow><mn>3</mn><mi>n</mi></mrow></msup><mo>=</mo><mn>1</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>α</mi></mrow></mfenced><mn>7</mn></msup><mo>=</mo><mo>-</mo><msup><mi>ω</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>+</mo><mi>ω</mi></math></p><p>Now, on comparing with equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">A</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">B</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi mathvariant="normal">C</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>5</mn><mfenced><mrow><mn>3</mn><mi mathvariant="normal">A</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">B</mi><mo>-</mo><mi mathvariant="normal">C</mi></mrow></mfenced><mo>=</mo><mn>5</mn><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn><mo>-</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>5</mn><mfenced><mrow><mn>3</mn><mi mathvariant="normal">A</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">B</mi><mo>-</mo><mi mathvariant="normal">C</mi></mrow></mfenced><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q7. JEE Main 2022 (26 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>z</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>,</mo><mi>z</mi><mo>&#8712;</mo><mi>C</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msup><mfenced><mrow><msup><mi>z</mi><mi>n</mi></msup><mo>+</mo><mo>(</mo><mo>-</mo><mn>1</mn><msup><mo>)</mo><mi>a</mi></msup><mfrac><mn>1</mn><msup><mi>z</mi><mi>n</mi></msup></mfrac></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>z</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mi>w</mi><mo>,</mo><msup><mi>w</mi><mn>2</mn></msup></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msup><mfenced><mrow><msup><mi>z</mi><mi mathvariant="normal">n</mi></msup><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><msup><mi>z</mi><mi>n</mi></msup></mfrac></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><mfenced><mrow><msup><mi>z</mi><mrow><mn>2</mn><mi>n</mi></mrow></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>z</mi><mrow><mn>2</mn><mi>n</mi></mrow></msup></mfrac><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msup><mi>w</mi><mrow><mn>2</mn><mi>n</mi></mrow></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>w</mi><mrow><mn>2</mn><mi>n</mi></mrow></msup></mfrac><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mfrac><mrow><msup><mi>w</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>w</mi><mn>30</mn></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>w</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mfrac><mn>1</mn><msup><mi>w</mi><mn>2</mn></msup></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mi>w</mi><mn>30</mn></msup></mfrac></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mi>w</mi><mn>2</mn></msup></mfrac></mrow></mfrac><mo>+</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mfrac><mrow><msup><mi>w</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>w</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mfrac><mn>1</mn><msup><mi>w</mi><mn>2</mn></msup></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mi>w</mi><mn>2</mn></msup></mfrac></mrow></mfrac><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mn>0</mn><mo>+</mo><mn>0</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q8. JEE Main 2021 (26 Aug Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn><mo>+</mo><msup><mfenced><mrow><mi>z</mi><mo>+</mo><mfrac><mn>1</mn><mi>z</mi></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>z</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced><mrow><msup><mi>z</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>z</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mfenced><mrow><msup><mi>z</mi><mn>21</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>z</mi><mn>21</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup></math> is______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **13**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mo>-</mo><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mo>&#8722;</mo><mi>&#969;</mi></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi></math> is the cube root of unity. So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>&#969;</mi><mo>+</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#969;</mi><mn>3</mn></msup><mo>=</mo><mn>1</mn></math></p><p>Now, let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msup><mfenced separators="|"><mrow><mi>z</mi><mo>+</mo><mfrac><mn>1</mn><mi>z</mi></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>z</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><msup><mi>z</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>z</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mfenced separators="|"><mrow><msup><mi>z</mi><mn>21</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>z</mi><mn>21</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><msup><mfenced separators="|"><mrow><mo>&#8722;</mo><mi>&#969;</mi><mo>&#8722;</mo><mfrac><mn>1</mn><mi>&#969;</mi></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><msup><mi>&#969;</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>&#969;</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mo>&#8722;</mo><msup><mi>&#969;</mi><mn>3</mn></msup><mo>&#8722;</mo><mfrac><mn>1</mn><msup><mi>&#969;</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mfenced separators="|"><mrow><mo>&#8722;</mo><msup><mi>&#969;</mi><mn>21</mn></msup><mo>&#8722;</mo><mfrac><mn>1</mn><msup><mi>&#969;</mi><mn>21</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mo>-</mo><msup><mfenced separators="|"><mfrac><mrow><msup><mi>&#969;</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mi>&#969;</mi></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mfrac><mrow><msup><mi>&#969;</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow><msup><mi>&#969;</mi><mn>2</mn></msup></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mo>&#8722;</mo><mn>1</mn><mo>&#8722;</mo><mfrac><mn>1</mn><mn>1</mn></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mfenced separators="|"><mrow><mo>&#8722;</mo><msup><mi>&#969;</mi><mn>21</mn></msup><mo>&#8722;</mo><mfrac><mn>1</mn><msup><mi>&#969;</mi><mn>21</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mo>-</mo><msup><mfenced separators="|"><mfrac><mrow><mo>-</mo><mi>&#969;</mi></mrow><mi>&#969;</mi></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mfrac><mrow><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup></mrow><msup><mi>&#969;</mi><mn>2</mn></msup></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mo>&#8722;</mo><mn>1</mn><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mfenced separators="|"><mrow><mo>&#8722;</mo><msup><mi>&#969;</mi><mn>21</mn></msup><mo>&#8722;</mo><mfrac><mn>1</mn><msup><mi>&#969;</mi><mn>21</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msup><mfenced separators="|"><mrow><mo>&#8722;</mo><mn>1</mn><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msup><mfenced separators="|"><mrow><mo>&#8722;</mo><mn>1</mn><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mfenced separators="|"><mrow><mo>&#8722;</mo><mn>1</mn><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>3</mn><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><msup><mfenced separators="|"><mrow><mo>&#8722;</mo><mn>1</mn><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mo>&#8722;</mo><mn>8</mn></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn><mo>+</mo><mi>A</mi><mo>=</mo><mn>21</mn><mo>&#8722;</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>13</mn></math></p>

</details>

---

### Q9. JEE Main 2021 (18 Mar Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> are two polynomials such that the polynomial <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>f</mi><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced><mo>+</mo><mi>x</mi><mi>g</mi><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mn>1</mn><mo>)</mo></math> is equal to ___ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>f</mi><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced><mo>+</mo><mi>x</mi><mi>g</mi><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>g</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>Q</mi><mo>(</mo><mi>x</mi><mo>)</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>&#969;</mi><mo>)</mo><mo>=</mo><mn>0</mn><mo>=</mo><mi>P</mi><mfenced><msup><mi>&#969;</mi><mn>2</mn></msup></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>,</mo><msup><mi>&#969;</mi><mn>2</mn></msup></math> are non-real cube roots of units</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>f</mi><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced><mo>+</mo><mi>x</mi><mi>g</mi><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>&#969;</mi><mo>)</mo><mo>=</mo><mi>f</mi><mfenced><msup><mi>&#969;</mi><mn>3</mn></msup></mfenced><mo>+</mo><mi>&#969;</mi><mi>g</mi><mfenced><msup><mi>&#969;</mi><mn>3</mn></msup></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>&#969;</mi><mi>g</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msup><mi>&#969;</mi><mn>2</mn></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mi>&#969;</mi><mn>6</mn></msup></mfenced><mo>+</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mi>g</mi><mfenced><msup><mi>&#969;</mi><mn>6</mn></msup></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mi>g</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo><mo>+</mo><mo>(</mo><mn>3</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mfenced><mrow><mi>&#969;</mi><mo>+</mo><msup><mi>&#969;</mi><mn>2</mn></msup></mrow></mfenced><mi>g</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>g</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo><mo>-</mo><mo>(</mo><mn>3</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#969;</mi><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup></mrow></mfenced><mi>g</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>=</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo></math>   from <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>4</mn><mo>)</mo></math></p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>g</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q10. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>1</mn><mo>-</mo><mi>i</mi></mrow></mfrac></mfenced><mn>30</mn></msup></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>6</mn><mn>5</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>15</mn></msup></math> i
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mn>2</mn><mn>15</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mn>2</mn><mn>15</mn></msup></math>i

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mn>2</mn><mn>15</mn></msup></math>i**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt><mi>i</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>i</mi></mrow></mfrac></mfenced><mn>30</mn></msup><mo>=</mo><msup><mfenced><mfrac><mrow><mn>2</mn><mi>cos</mi><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced><mo>+</mo><mi>i</mi><mi>sin</mi><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced></mrow><mrow><msqrt><mn>2</mn></msqrt><mfenced><mrow><mi>cos</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>i</mi><mi>sin</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac></mfenced><mn>30</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mn>30</mn></msup><mo>(</mo><mi>cos</mi><mn>20</mn><mi>&#960;</mi><mo>+</mo><mi>i</mi><mi>sin</mi><mn>20</mn><mi>&#960;</mi><mo>)</mo></mrow><mrow><msup><mn>2</mn><mn>15</mn></msup><mfenced><mrow><mi>cos</mi><mfrac><mrow><mn>15</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mi>i</mi><mi>sin</mi><mfrac><mrow><mn>15</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mn>15</mn></msup><mo>(</mo><mn>1</mn><mo>+</mo><mn>0</mn><mi>i</mi><mo>)</mo></mrow><mrow><mo>(</mo><mn>0</mn><mo>+</mo><mi>i</mi><mo>)</mo></mrow></mfrac><mo>=</mo><mo>-</mo><msup><mn>2</mn><mn>15</mn></msup><mi>i</mi></math></p>

</details>

---

### Q11. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> are real numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mn>4</mn></msup><mo>=</mo><mi>a</mi><mo>+</mo><mi>b</mi><mi>&#945;</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>57</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><msup><mrow></mrow><mn>4</mn></msup><mo>=</mo><mi>a</mi><mo>+</mo><mi>b</mi><mi>&#945;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>4</mn><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mi>a</mi><mo>+</mo><mi>b</mi><mi>&#945;</mi></math></p><p>Now using, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mo>&#8658;</mo><msup><mfenced><mrow><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mi>&#945;</mi><mo>=</mo><msup><mfenced><mrow><mn>4</mn><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>1</mn><mo>+</mo><mn>4</mn><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mi>&#945;</mi><mo>=</mo><msup><mfenced><mrow><mn>3</mn><mo>+</mo><mn>3</mn><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mi>&#945;</mi><mo>=</mo><mn>9</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>9</mn><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>9</mn><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q12. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math>. If <math><mi>a</mi><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mrow><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mrow><mn>100</mn></mrow></munderover><mrow><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn><mi>k</mi></mrow></msup></mrow></mrow></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mn>100</mn></munderover><msup><mi>&#945;</mi><mrow><mn>3</mn><mi>k</mi></mrow></msup></math>, then <math><mi>a</mi></math> and <math><mi>b</mi></math>, are the roots of the quadratic equation.

**Options:**

- **(A)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>101</mn><mi>x</mi><mo>+</mo><mn>100</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>102</mn><mi>x</mi><mo>+</mo><mn>101</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>101</mn><mi>x</mi><mo>+</mo><mn>100</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>102</mn><mi>x</mi><mo>+</mo><mn>101</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>102</mn><mi>x</mi><mo>+</mo><mn>101</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math><mi>a</mi><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mrow><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mrow><mn>100</mn></mrow></munderover><mrow><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn><mi>k</mi></mrow></msup></mrow></mrow></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mn>100</mn></munderover><msup><mi>&#945;</mi><mrow><mn>3</mn><mi>k</mi></mrow></msup></math></p><p>Now</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mi>&#969;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>;</mo><mo>&#160;</mo><mi>&#969;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p>Using this <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> can be written as 
<math><mi>a</mi><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>&#969;</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>198</mn></mrow></msup><mo>+</mo><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>200</mn></mrow></msup></mrow></mfenced></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>&#969;</mi></mrow></mfenced><mfrac><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>101</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>&#969;</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>&#969;</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p>Similarly,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>1</mn><mo>+</mo><msup><mi>&#969;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#969;</mi><mn>6</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>&#969;</mi><mn>300</mn></msup><mo>=</mo><mn>101</mn></math>
So, the required quadratic equation is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mi>a</mi><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>102</mn><mi>x</mi><mo>+</mo><mn>101</mn><mo>=</mo><mn>0</mn></math>.</p>

</details>

---

### Q13. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>i</mi><mn>2</mn></mfrac><mi>&#160;</mi><mfenced separators="|"><mrow><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mo>,</mo><mi>&#160;</mi></math> then <math><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mi>z</mi><mo>+</mo><msup><mrow><mi>z</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>+</mo><mi>i</mi><msup><mrow><mi>z</mi></mrow><mrow><mn>8</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup></math> is equal to:

**Options:**

- **(A)** <math><mo>-</mo><mn>1</mn></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** <math><mn>0</mn><mi> </mi></math>
- **(D)** <math><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<math><mi>z</mi><mo>=</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>i</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi><mi> </mi><mo>∴</mo><mi>i</mi><mi>z</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mi>i</mi><mo>=</mo><mi>ω</mi></math>  
<math><mo>∴</mo><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>i</mi><mi>z</mi><mo>+</mo><msup><mrow><mi>z</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>+</mo><mi>i</mi><msup><mrow><mi>z</mi></mrow><mrow><mn>8</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>ω</mi><mo>+</mo><mfrac><mrow><msup><mrow><mi>ω</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow><mrow><msup><mrow><mi>i</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac><mo>+</mo><mi>i</mi><mo>×</mo><mfrac><mrow><msup><mrow><mi>ω</mi></mrow><mrow><mn>8</mn></mrow></msup></mrow><mrow><msup><mrow><mi>i</mi></mrow><mrow><mn>8</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup><mi> </mi></math>  
<math><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>ω</mi><mo>-</mo><mi>i</mi><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>i</mi><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup></math>  
<math><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup><mo>=</mo><mo>-</mo><msup><mrow><mi>ω</mi></mrow><mrow><mn>18</mn></mrow></msup></math>  
<math><mo>=</mo><mi> </mi><mo>-</mo><mn>1</mn></math>

</details>

---

### Q14. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><msub><mrow><mi>z</mi></mrow><mrow><mn>0</mn></mrow></msub></math> be a root of quadratic equation, <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>.</mo><mtext>&#160;</mtext></math> If <math><mi>z</mi><mo>=</mo><mn>3</mn><mo>+</mo><mn>6</mn><mi>i</mi><msubsup><mrow><mi>z</mi></mrow><mrow><mn>0</mn></mrow><mrow><mn>81</mn></mrow></msubsup><mo>-</mo><mn>3</mn><mi>i</mi><msubsup><mrow><mi>z</mi></mrow><mrow><mn>0</mn></mrow><mrow><mn>93</mn></mrow></msubsup></math> , then <math><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">g</mi></math> <math><mfenced separators="|"><mrow><mi>z</mi></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><msub><mrow><mi>z</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mi>w</mi></math> or <math><msup><mrow><mi>w</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

When <math><msub><mrow><mi>z</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mi>w</mi></math>

<math><mi>z</mi><mo>=</mo><mn>3</mn><mo>+</mo><mn>6</mn><mi>i</mi><mo>&#215;</mo><msup><mrow><mi>w</mi></mrow><mrow><mn>81</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>i</mi><mo>&#215;</mo><msup><mrow><mi>w</mi></mrow><mrow><mn>93</mn></mrow></msup></math>

<math><mo>=</mo><mn>3</mn><mo>+</mo><mn>6</mn><mi>i</mi><mo>-</mo><mn>3</mn><mi>i</mi><mo>=</mo><mn>3</mn><mo>+</mo><mn>3</mn><mi>i</mi></math>

When <math><msub><mrow><mi>z</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><msup><mrow><mi>w</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mi>z</mi><mo>=</mo><mn>3</mn><mo>+</mo><mn>6</mn><mi>i</mi><mo>&#215;</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>w</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>81</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>i</mi><mo>&#215;</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>w</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>93</mn></mrow></msup></math>

<math><mo>=</mo><mn>3</mn><mo>+</mo><mn>6</mn><mi>i</mi><mo>-</mo><mn>3</mn><mi>i</mi><mo>=</mo><mn>3</mn><mo>+</mo><mn>3</mn><mi>i</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>arg</mi><mo>&#8289;</mo><mfenced separators="|"><mi>z</mi></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>I</mi><mi>m</mi><mfenced><mi>z</mi></mfenced></mrow><mrow><mi>R</mi><mi>e</mi><mfenced><mi>z</mi></mfenced></mrow></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced separators="|"><mfrac><mn>3</mn><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>

</details>

---

### Q15. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>α</mi><mo>,</mo><mi> </mi><mi>β</mi><mo>∈</mo><mi>C</mi></math> are the distinct roots of the equation <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math><msup><mrow><mi>α</mi></mrow><mrow><mn>101</mn></mrow></msup><mo>+</mo><msup><mrow><mi>β</mi></mrow><mrow><mn>107</mn></mrow></msup></math> is equal to

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mo>-</mo><mn>1</mn></math>
- **(C)** <math><mn>0</mn></math>
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>1</mn></math>**

**Detailed Solution:**

<p><math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

Roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#969;</mi><mo>,</mo><mi>&#160;</mi><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup></math>.

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>101</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>107</mn></msup><mo>=</mo><msup><mfenced separators="|"><mrow><mo>-</mo><mi>&#969;</mi></mrow></mfenced><mn>101</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup></mrow></mfenced><mn>107</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mo>-</mo><mi>&#969;</mi><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><msup><mi>&#969;</mi><mn>3</mn></msup><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced><mrow><msup><mi>&#969;</mi><mn>2</mn></msup><mo>+</mo><mi>&#969;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mn>1</mn><mo>+</mo><mi>&#969;</mi><mo>+</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></mrow></mfenced></math></p>

</details>

---

### Q16. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `2`

If $\omega(\neq 1)$ is a cube root of unity, and $(1+\omega)^7=A+B \omega$. Then $(A, B)$ equals

**Options:**

- **(A)** $(1,1)$
- **(B)** $(1,0)$
- **(C)** $(-1,1)$
- **(D)** $(0,1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(1,1)$**

**Detailed Solution:**

$1+\omega=-\omega^2$
$(1+\omega)^7=\left(-\omega^2\right)^7=-\omega^{14}=-\omega^2=1+\omega=A+B \omega \Rightarrow(A, B)=(1,1)$

</details>

---

### Q17. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `3`

If $z^2+z+1=0$, where $z$ is a complex number, then the value of
$$
\left(z+\frac{1}{z}\right)^2+\left(z^2+\frac{1}{z^2}\right)^2+\left(z^3+\frac{1}{z^3}\right)^2+\cdots+\left(z^6+\frac{1}{z^6}\right)^2
$$

**Options:**

- **(A)** 18
- **(B)** 54
- **(C)** 6
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 12**

**Detailed Solution:**

$z^2+z+1=0 \quad \Rightarrow z=\omega$ or $\omega^2$ so, $z+\frac{1}{z}=\omega+\omega^2=-1, z^2+\frac{1}{z^2}=\omega^2+\omega=-1, z^3+\frac{1}{z^3}=\omega^3+\omega^3=2$ $z^4+\frac{1}{z^4}=-1, z^5+\frac{1}{z^5}=-1$ and $z^6+\frac{1}{z^6}=2$ $\therefore$ The given sum $=1+1+4+1+1+4=12$

</details>

---

### Q18. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

If the cube roots of unity are $1, \omega, \omega^2$ then the roots of the equation $(x-1)^3+8=0$, are

**Options:**

- **(A)** $-1,-1+2 \omega,-1-2 \omega^2$
- **(B)** $-1,-1,-1$
- **(C)** $-1,1-2 \omega, 1-2 \omega^2$
- **(D)** $-1,1+2 \omega, 1+2 \omega^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-1,1-2 \omega, 1-2 \omega^2$**

**Detailed Solution:**

$(x-1)^3+8=0 \Rightarrow(x-1)=(-2)(1)^{1 / 3}$ $\Rightarrow x-1=-2$ or $-2 \omega$ or $-2 \omega^2$ or $n=-1$ or $1-2 \omega$ or $1-2 \omega^2$.

</details>

---

