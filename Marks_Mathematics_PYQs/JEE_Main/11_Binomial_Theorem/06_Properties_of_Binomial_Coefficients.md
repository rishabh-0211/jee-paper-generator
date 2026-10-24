# JEE Main Mathematics - Binomial Theorem

## Topic 6: Properties of Binomial Coefficients

**Total Questions:** 15

---

### Q1. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If for $3 \leq r \leq 30$, $\binom{30}{30-r} + 3\binom{30}{31-r} + 3\binom{30}{32-r} + \binom{30}{33-r} = \binom{m}{r}$, then $m$ equals:

**Options:**

- **(A)** $31$
- **(B)** $32$
- **(C)** $33$
- **(D)** $34$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $33$**

**Detailed Solution:**

Using the property $^{n}C_{r} = ^{n}C_{n-r}$, the given expression can be written as:

$^{30}C_{r} + 3 \cdot ^{30}C_{r-1} + 3 \cdot ^{30}C_{r-2} + ^{30}C_{r-3}$

This expression represents the coefficient of $x^r$ in the expansion of:

$(1+x)^{30} + 3x(1+x)^{30} + 3x^2(1+x)^{30} + x^3(1+x)^{30}$

Taking $(1+x)^{30}$ common, we get:

$(1+x)^{30}(1 + 3x + 3x^2 + x^3)$

$= (1+x)^{30}(1+x)^3$

$= (1+x)^{33}$

The coefficient of $x^r$ in $(1+x)^{33}$ is $^{33}C_{r}$.

Comparing this with $^{m}C_{r}$, we get $m = 33$.

Answer: $33$

</details>

---

### Q2. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of elements in the set $S = \left\{(r, k) : k \in \mathbb{Z} \text{ and } {}^{36}C_{r+1} = \dfrac{6\left({}^{35}C_r\right)}{(k^2 - 3)}\right\}$, is :

**Options:**

- **(A)** $2$
- **(B)** $4$
- **(C)** $8$
- **(D)** $16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4$**

**Detailed Solution:**

Given equation:

$^{36}C_{r+1} = \dfrac{6 \left(^{35}C_r\right)}{k^2 - 3}$

Using the property $^{n}C_r = \dfrac{n}{r} {}^{n-1}C_{r-1}$, we can write:

$^{36}C_{r+1} = \dfrac{36}{r+1} {}^{35}C_r$

Substituting this into the given equation:

$\dfrac{36}{r+1} {}^{35}C_r = \dfrac{6}{k^2 - 3} {}^{35}C_r$

For $^{35}C_r$ to be defined, $r$ must be an integer such that $0 \le r \le 35$. Thus, $^{35}C_r \neq 0$. Dividing both sides by $^{35}C_r$:

$\dfrac{36}{r+1} = \dfrac{6}{k^2 - 3}$

$\dfrac{6}{r+1} = \dfrac{1}{k^2 - 3}$

$k^2 - 3 = \dfrac{r+1}{6}$

$k^2 = 3 + \dfrac{r+1}{6}$

For $k \in \mathbb{Z}$, $k^2$ must be a perfect square integer. This requires $r+1$ to be a multiple of $6$.

Since $0 \le r \le 35$, we have $1 \le r+1 \le 36$.

Let $r+1 = 6m$, where $m \in \{1, 2, 3, 4, 5, 6\}$.

Then $k^2 = 3 + m$.

Checking the possible values of $m$ for which $k^2$ is a perfect square:

For $m = 1$, $k^2 = 4 \Rightarrow k = \pm 2$. (Here $r+1 = 6 \Rightarrow r = 5$)

For $m = 2$, $k^2 = 5$ (not a perfect square).

For $m = 3$, $k^2 = 6$ (not a perfect square).

For $m = 4$, $k^2 = 7$ (not a perfect square).

For $m = 5$, $k^2 = 8$ (not a perfect square).

For $m = 6$, $k^2 = 9 \Rightarrow k = \pm 3$. (Here $r+1 = 36 \Rightarrow r = 35$)

The possible pairs $(r, k)$ are $(5, 2)$, $(5, -2)$, $(35, 3)$, and $(35, -3)$.

Therefore, the number of elements in the set $S$ is $4$.

Answer: $4$

</details>

---

### Q3. JEE Main 2026 (21 January Shift 2)

*Type:* `numerical` | *Level:* `2`

If $\left(\frac{1}{{ }^{15} \mathrm{C}_{0}}+\frac{1}{{ }^{15} \mathrm{C}_{1}}\right)\left(\frac{1}{{ }^{15} \mathrm{C}_{1}}+\frac{1}{{ }^{15} \mathrm{C}_{2}}\right) \cdots\left(\frac{1}{{ }^{15} \mathrm{C}_{12}}+\frac{1}{{ }^{15} \mathrm{C}_{13}}\right)=\frac{\alpha^{13}}{{ }^{14} \mathrm{C}_{0}{ }^{14} \mathrm{C}_{1} \cdots{ }^{14} \mathrm{C}_{12}}$, then $30 \alpha$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **32**

**Detailed Solution:**

The general term of the product is $T_r = \frac{1}{^{15}C_{r-1}} + \frac{1}{^{15}C_r}$ for $r = 1, 2, \dots, 13$.
Using the formula $^{n}C_r = \frac{n}{r} \cdot ^{n-1}C_{r-1}$, we have $^{15}C_r = \frac{15}{r} \cdot ^{14}C_{r-1}$ and $^{15}C_{r-1} = \frac{15}{15-(r-1)} \cdot ^{14}C_{r-1} = \frac{15}{16-r} \cdot ^{14}C_{r-1}$.
Substituting these into $T_r$:
$T_r = \frac{16-r}{15 \cdot ^{14}C_{r-1}} + \frac{r}{15 \cdot ^{14}C_{r-1}} = \frac{16-r+r}{15 \cdot ^{14}C_{r-1}} = \frac{16}{15 \cdot ^{14}C_{r-1}}$.
The product is $\prod_{r=1}^{13} T_r= \prod_{r=1}^{13} \frac{16}{15\cdot {^{14}C_{r-1}}}= \frac{16^{13}}{15^{13} \cdot \prod_{r=1}^{13}{^{14}C_{r-1}}}$.
The denominator of the product is $15^{13} \cdot (^{14}C_0 \cdot ^{14}C_1 \dots ^{14}C_{12})$.
Comparing this with the given expression $\frac{\alpha^{13}}{^{14}C_0 \cdot ^{14}C_1 \dots ^{14}C_{12}}$, we get:
$\alpha^{13} = \frac{16^{13}}{15^{13}} \implies \alpha = \frac{16}{15}$.
We need to find the value of $30\alpha$:
$30\alpha = 30 \times \frac{16}{15} = 2 \times 16 = 32$.

</details>

---

### Q4. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\sum_{\mathrm{r}=0}^{10}\left(\frac{10^{\mathrm{r}+1}-1}{10^{\mathrm{r}}}\right) \cdot{ }^{11} \mathrm{C}_{\mathrm{r}+1}=\frac{\alpha^{11}-11^{11}}{10^{10}}$, then $\alpha$ is equal to :

**Options:**

- **(A)** $15$
- **(B)** $11$
- **(C)** $24$
- **(D)** $20$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $20$**

**Detailed Solution:**

$\begin{aligned} & \sum_{\mathrm{r}=0}^{10}\left(\frac{1 \mathrm{r}^{\mathrm{r}-1}-1}{10^{\mathrm{r}}}\right){ }^{11} \mathrm{C}_{\mathrm{r}+1} \\ & =\sum_{\mathrm{r}=0}^{10}\left(10-\frac{1}{10^{\mathrm{r}}}\right)^{11} \mathrm{C}_{\mathrm{r}+1} \\ & =10 \sum_{\mathrm{r}=0}^{10} \mathrm{C}_{\mathrm{r}+1}-10 \sum\left({ }^{11} \mathrm{C}_{\mathrm{r}+1}\left(\frac{1}{10}\right)^{\mathrm{r}+1}\right) \\ & =10\left[{ }^{11} \mathrm{C}_1+{ }^{11} \mathrm{C}_2+\ldots . .+{ }^{11} \mathrm{C}_{11}\right] \\ & -10\left[{ }^{11} \mathrm{C}_1\left(\frac{1}{10}\right)^1+{ }^{11} \mathrm{C}_2\left(\frac{1}{10}\right)^2+\ldots . .+{ }^{11} \mathrm{C}_{11}\left(\frac{1}{10}\right)^{11}\right] \\ & =10\left[2^{11}-1\right]-10\left[\left(1+\frac{1}{10}\right)^{11}-1\right] \\ & =10(2)^{11}-10-\frac{11^{11}}{10^{10}}+10 \\ & =\frac{(20)^{11}-11^{11}}{10^{10}} \\ & \therefore \alpha=20\end{aligned}$

</details>

---

### Q5. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>Let the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mi>r</mi></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mrow><mi>n</mi><mo>−</mo><mn>2</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mrow><mi>n</mi><mo>−</mo><mn>3</mn></mrow></msup><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>...</mo><mo>+</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msup></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>α</mi><mi>r</mi></msub></math>. If<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∑</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mi>n</mi></munderover><msub><mi>α</mi><mi>r</mi></msub><mo>=</mo><msup><mi>β</mi><mi>n</mi></msup><mo>−</mo><msup><mi>γ</mi><mi>n</mi></msup><mo>,</mo><mi>β</mi><mo>,</mo><mi>γ</mi><mo>∈</mo><mi>N</mi></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>β</mi><mn>2</mn></msup><mo>+</mo><msup><mi>γ</mi><mn>2</mn></msup></math> equals _______.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msup><mo>+</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mrow><mi>n</mi><mo>−</mo><mn>2</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mrow><mi>n</mi><mo>−</mo><mn>3</mn></mrow></msup><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>....</mo><mo>+</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msup></math></p><p>Now, using the sum of G.P formula we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>S</mi><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced><mi>n</mi></msup></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>S</mi><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mi>n</mi></msup><mo>-</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>n</mi></msup></math></p><p>Now, finding the sum of coefficients we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∑</mo><msub><mi>α</mi><mi>r</mi></msub><mo>=</mo><mo>∑</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mi>n</mi></msup><mo>-</mo><mo>∑</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mn>4</mn><mi>n</mi></msup><mo>−</mo><msup><mn>3</mn><mi>n</mi></msup><mo>=</mo><msup><mi>β</mi><mi>n</mi></msup><mo>−</mo><msup><mi>γ</mi><mi>n</mi></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>by taking </mtext><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p>So, on comparing both side we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo> </mo><mi>γ</mi><mo>=</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>β</mi><mn>2</mn></msup><mo>+</mo><msup><mi>γ</mi><mn>2</mn></msup><mo>=</mo><mn>16</mn><mo>+</mo><mn>9</mn><mo>=</mo><mn>25</mn></math></p>

</details>

---

### Q6. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>,</mo><mo> </mo><mi>n</mi><mo>;</mo><msup><mo> </mo><mn>6</mn></msup><msub><mi>C</mi><mi>m</mi></msub><mo>+</mo><mn>2</mn><mfenced><mrow><msup><mrow></mrow><mn>6</mn></msup><msub><mi>C</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow></mfenced><msup><mo>+</mo><mn>6</mn></msup><msub><mi>C</mi><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></msub><msup><mo>&gt;</mo><mn>8</mn></msup><msub><mi>C</mi><mn>3</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msup><msub><mi>P</mi><mn>3</mn></msub><msup><mo>:</mo><mi>n</mi></msup><msub><mi>P</mi><mn>4</mn></msub><mo>=</mo><mn>1</mn><mo>:</mo><mn>8</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mi>n</mi></msup><msub><mi>P</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>+</mo><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mi>m</mi></msub></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>380</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>376</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>384</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>372</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>372</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mn>6</mn></msup><msub><mi>C</mi><mi>m</mi></msub><mo>+</mo><mn>2</mn><mfenced><mrow><msup><mrow></mrow><mn>6</mn></msup><msub><mi>C</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow></mfenced><msup><mo>+</mo><mn>6</mn></msup><msub><mi>C</mi><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></msub><msup><mo>&gt;</mo><mn>8</mn></msup><msub><mi>C</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>⇒</mo><mn>6</mn></msup><msub><mi>C</mi><mi>m</mi></msub><msup><mo>+</mo><mn>6</mn></msup><msub><mi>C</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>+</mo><mn>6</mn></msup><msub><mi>C</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>+</mo><mn>6</mn></msup><msub><mi>C</mi><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></msub><msup><mo>&gt;</mo><mn>8</mn></msup><msub><mi>C</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>⇒</mo><mn>7</mn></msup><msub><mi>C</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>+</mo><mn>7</mn></msup><msub><mi>C</mi><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></msub><msup><mo>&gt;</mo><mn>8</mn></msup><msub><mi>C</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>⇒</mo><mn>8</mn></msup><msub><mi>C</mi><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></msub><msup><mo>&gt;</mo><mn>8</mn></msup><msub><mi>C</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>m</mi><mo>=</mo><mn>2</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msup><msub><mi>P</mi><mn>3</mn></msub><msup><mo>:</mo><mi>n</mi></msup><msub><mi>P</mi><mn>4</mn></msub><mo>=</mo><mn>1</mn><mo>:</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>−</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>−</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>−</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>−</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>⇒</mo><mi>n</mi></msup><msub><mi>P</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>+</mo><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mi>m</mi></msub><msup><mo>=</mo><mn>8</mn></msup><msub><mi>P</mi><mn>3</mn></msub><msup><mo>+</mo><mn>9</mn></msup><msub><mi>C</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>⇒</mo><mi>n</mi></msup><msub><mi>P</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>+</mo><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mi>m</mi></msub><mo>=</mo><mn>8</mn><mo>×</mo><mn>7</mn><mo>×</mo><mn>6</mn><mo>+</mo><mfrac><mrow><mn>9</mn><mo>×</mo><mn>8</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>⇒</mo><mi>n</mi></msup><msub><mi>P</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>+</mo><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mi>m</mi></msub><mo>=</mo><mn>372</mn></math></p>

</details>

---

### Q7. JEE Main 2024 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mi>n</mi></munderover><mfenced><mfrac><msup><mfenced><mmultiscripts><mi mathvariant="normal">C</mi><mi>k</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mfenced><mn>2</mn></msup><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mfenced><mfrac><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mi>k</mi><none></none><mprescripts></mprescripts><none></none><mi mathvariant="italic">n</mi></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mrow><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>α</mi><mo>=</mo><mn>6</mn><mi>β</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> equals

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<blockquote><p>Given,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mi>n</mi></munderover><mfenced><mfrac><msup><mfenced><mmultiscripts><mi mathvariant="normal">C</mi><mi>k</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mfenced><mn>2</mn></msup><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mi>n</mi></munderover><mfrac><mrow><mmultiscripts><mi>C</mi><mi>k</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mi>k</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mrow><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>·</mo><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>=</mo><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>·</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mi>n</mi></munderover><mmultiscripts><mi>C</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mi>k</mi></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mi>n</mi></munderover><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>·</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Now, solving </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mmultiscripts><mi>C</mi><mi>k</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>·</mo><mfrac><mmultiscripts><mi>C</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>β</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mi>k</mi></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mi>n</mi></munderover><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>β</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>·</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now, dividing equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> and using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mfrac><mo>=</mo><mfrac><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mi>r</mi></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>β</mi><mi>α</mi></mfrac><mo>=</mo><mfrac><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>-</mo><mo>(</mo><mi>n</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>+</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>β</mi><mi>α</mi></mfrac><mo>=</mo><mfrac><mi>n</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>=</mo><mn>10</mn></math></p></blockquote>

</details>

---

### Q8. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mmultiscripts><mo>=</mo><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn></mrow></mfenced><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math> if and only if :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>&lt;</mo><mi>k</mi><mo>≤</mo><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>&lt;</mo><mi mathvariant="normal">k</mi><mo>≤</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>&lt;</mo><mi mathvariant="normal">k</mi><mo>&lt;</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>&lt;</mo><mi mathvariant="normal">k</mi><mo>&lt;</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>&lt;</mo><mi>k</mi><mo>≤</mo><mn>3</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mmultiscripts><mo>=</mo><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn></mrow></mfenced><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munder><munder><mrow><mi>r</mi><mo>+</mo><mn>1</mn><mo>≥</mo><mn>0</mn><mo>,</mo><mo>  </mo><mi>r</mi><mo>≥</mo><mn>0</mn></mrow><mo>⏟</mo></munder><mrow><mi>r</mi><mo>≥</mo><mn>0</mn></mrow></munder></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mmultiscripts><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mfrac><mo>=</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mstyle displaystyle="true"><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow><mrow><mi>r</mi><mo>!</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mstyle></mfrac><mo>=</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mi>n</mi></mfrac><mo>=</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mo>&gt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>(</mo><mi>k</mi><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>&gt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>k</mi><mo>∈</mo><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>∪</mo><mo>(</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>,</mo><mo>∞</mo><mo>)</mo><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo></math></p><p>Using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>≥</mo><mi>r</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mi>n</mi></mfrac><mo>≤</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mo>≤</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mo>≤</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>3</mn><mo>≤</mo><mi mathvariant="normal">k</mi><mo>≤</mo><mn>3</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>∈</mo><mo>[</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>∪</mo><mo>(</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>,</mo><mn>3</mn><mo>]</mo></math></p>

</details>

---

### Q9. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>2</mn><mi>n</mi></mrow></mmultiscripts><mo>:</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mn>10</mn><mo>:</mo><mn>1</mn><mo>,</mo></math> then the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi></mrow></mfenced><mo>:</mo><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn><mo>:</mo><mn>16</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><mo>:</mo><mn>11</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>65</mn><mo>:</mo><mn>37</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>1</mn></math>**

**Detailed Solution:**

<blockquote><p>We have been given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mrow><mn>2</mn><mi>n</mi></mrow></mmultiscripts><mo>:</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mn>10</mn></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mi>r</mi><mo>!</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mstyle></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>3</mn><mo>!</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mrow><mrow><mi>n</mi><mo>!</mo></mrow></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mrow><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mrow><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mn>4</mn></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mi>n</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>10</mn><mi>n</mi><mo>-</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>8</mn></math></p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi></mrow><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mn>8</mn><mn>2</mn></msup><mo>+</mo><mn>3</mn><mfenced><mn>8</mn></mfenced></mrow><mrow><msup><mn>8</mn><mn>2</mn></msup><mo>-</mo><mn>3</mn><mfenced><mn>8</mn></mfenced><mo>+</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mn>88</mn><mn>44</mn></mfrac><mo>=</mo><mn>2</mn></math></p><p>Therefore, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi></mrow><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>1</mn></math>.</p></blockquote>

</details>

---

### Q10. JEE Main 2023 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>P</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>:</mo><mmultiscripts><mi>P</mi><mi>n</mi><none/><mprescripts/><none/><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mmultiscripts><mo>=</mo><mn>11</mn><mo>:</mo><mn>21</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi><mo>+</mo><mn>15</mn></math> is equal to :

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **45**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>P</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mmultiscripts><mi>P</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>11</mn><mn>21</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mn>11</mn><mn>21</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>21</mn><mo>&#215;</mo><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>=</mo><mn>11</mn><mo>&#215;</mo><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>21</mn><mo>&#215;</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>11</mn><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>11</mn><mn>42</mn></mfrac></math></p><p>Now on comparing both side we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>5</mn></math></p><p>So, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi><mo>+</mo><mn>15</mn><mo>=</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><mn>5</mn><mo>+</mo><mn>15</mn><mo>=</mo><mn>45</mn></math></p>

</details>

---

### Q11. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If  <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>P</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>P</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>P</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>P</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mi>n</mi></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mi>n</mi></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mi>r</mi><mo>!</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mi>r</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn><mo>=</mo><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>2</mn><mi>r</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>r</mi><mo>-</mo><mn>1</mn><mo>-</mo><mi>r</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>2</mn><mo>.</mo></math></p>

</details>

---

### Q12. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mo>&#8901;</mo><mn>1</mn></msup><msub><mi>P</mi><mn>0</mn></msub><mo>&#8722;</mo><mn>3</mn><msup><mo>&#8901;</mo><mn>2</mn></msup><msub><mi>P</mi><mn>1</mn></msub><mo>+</mo><mn>4</mn><msup><mo>&#8901;</mo><mn>3</mn></msup><msub><mi>P</mi><mn>2</mn></msub><mo>&#8722;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> up to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>51</mn><mi>th</mi></msup></math> term)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo></math>( <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>!</mo><mo>&#8722;</mo><mn>2</mn><mo>!</mo><mo>+</mo><mn>3</mn><mo>!</mo><mo>&#8722;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> up to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>51</mn><mi>th</mi></msup></math> term) is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mn>51</mn><mfenced><mn>51</mn></mfenced><mo>!</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfenced><mn>51</mn></mfenced><mo>!</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfenced><mn>52</mn></mfenced><mo>!</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfenced><mn>52</mn></mfenced><mo>!</mo></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#183;</mo><mmultiscripts><mi>P</mi><mn>0</mn><none/><mprescripts/><none/><mn>1</mn></mmultiscripts><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfrac><mrow><mn>1</mn><mo>!</mo></mrow><mrow><mn>1</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>2</mn><mo>!</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#183;</mo><mmultiscripts><mi>P</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>=</mo><mn>3</mn><mo>&#215;</mo><mfrac><mrow><mn>2</mn><mo>!</mo></mrow><mrow><mn>1</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>3</mn><mo>!</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#183;</mo><mmultiscripts><mi>P</mi><mn>2</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mo>=</mo><mn>4</mn><mo>&#215;</mo><mfrac><mrow><mn>3</mn><mo>!</mo></mrow><mrow><mn>1</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>4</mn><mo>!</mo></math></p><p>By this observation given question can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>2</mn><mo>!</mo><mo>-</mo><mn>3</mn><mo>!</mo><mo>+</mo><mn>4</mn><mo>!</mo><mo>-</mo><mn>5</mn><mo>!</mo><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mn>51</mn><mo>!</mo><mo>+</mo><mn>52</mn><mo>!</mo></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>!</mo><mo>-</mo><mn>2</mn><mo>!</mo><mo>+</mo><mn>3</mn><mo>!</mo><mo>-</mo><mn>4</mn><mo>!</mo><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mn>50</mn><mo>!</mo><mo>+</mo><mn>51</mn><mo>!</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>!</mo><mo>+</mo><mn>52</mn><mo>!</mo><mo>=</mo><mn>1</mn><mo>+</mo><mn>52</mn><mo>!</mo></math></p>

</details>

---

### Q13. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>a</mi><mo>,</mo><mi></mi><mi>b</mi></math> and <math><mi>c</mi></math> are the greatest values of <math><mmultiscripts><mrow><msub><mrow><mi>C</mi></mrow><mrow><mi>p</mi></mrow></msub></mrow><mprescripts></mprescripts><none></none><mrow><mn>19</mn></mrow></mmultiscripts><mo>,</mo><mi></mi><mmultiscripts><mrow><msub><mrow><mi>C</mi></mrow><mrow><mi>q</mi></mrow></msub></mrow><mprescripts></mprescripts><none></none><mrow><mn>20</mn></mrow></mmultiscripts></math> and <math><mmultiscripts><mrow><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub></mrow><mprescripts></mprescripts><none></none><mrow><mn>21</mn></mrow></mmultiscripts></math> respectively, then:

**Options:**

- **(A)** <math><mfrac><mrow><mi>a</mi></mrow><mrow><mn>11</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>b</mi></mrow><mrow><mn>22</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>c</mi></mrow><mrow><mn>21</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>a</mi></mrow><mrow><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>b</mi></mrow><mrow><mn>11</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>c</mi></mrow><mrow><mn>21</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>a</mi></mrow><mrow><mn>11</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>b</mi></mrow><mrow><mn>22</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>c</mi></mrow><mrow><mn>42</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>a</mi></mrow><mrow><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>b</mi></mrow><mrow><mn>11</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>c</mi></mrow><mrow><mn>42</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mi>a</mi></mrow><mrow><mn>11</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>b</mi></mrow><mrow><mn>22</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>c</mi></mrow><mrow><mn>42</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>We know that, <math><msup><mrow><mo>&#8201;</mo></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub></math> is maximum at middle term.</p><p><math><mi>a</mi><mo>=</mo><mo>&#8201;</mo><msup><mrow><mo>&#8201;</mo></mrow><mrow><mn>19</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>p</mi></mrow></msub><mo>=</mo><msup><mrow><mo>&#8201;</mo></mrow><mrow><mn>19</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>10</mn></mrow></msub><mo>=</mo><msup><mrow><mo>&#8201;</mo></mrow><mrow><mn>19</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>9</mn></mrow></msub></math></p><p><math><mi>b</mi><mo>=</mo><mo>&#8201;</mo><msup><mrow><mo>&#8201;</mo></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>q</mi></mrow></msub><mo>=</mo><msup><mrow><mo>&#8201;</mo></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>10</mn></mrow></msub></math></p><p><math><mi>c</mi><mo>=</mo><mo>&#8201;</mo><msup><mrow><mo>&#8201;</mo></mrow><mrow><mn>21</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>6</mn></mrow></msub><mo>=</mo><msup><mrow><mo>&#8201;</mo></mrow><mrow><mn>21</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>10</mn></mrow></msub><mo>=</mo><msup><mrow><mo>&#8201;</mo></mrow><mrow><mn>21</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>11</mn></mrow></msub></math></p><p>Hence,</p><p><math><mfrac><mrow><mi>a</mi></mrow><mrow><msup><mrow><mo>&#8201;</mo></mrow><mrow><mn>19</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>9</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>a</mi></mrow><mrow><mfrac><mrow><mn>20</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>.</mo><msup><mrow><mo>&#8201;</mo></mrow><mrow><mn>19</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>9</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>a</mi></mrow><mrow><mfrac><mrow><mn>21</mn></mrow><mrow><mn>11</mn></mrow></mfrac><mo>.</mo><mfrac><mrow><mn>20</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>.</mo><msup><mrow><mo>&#8201;</mo></mrow><mrow><mn>19</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>9</mn></mrow></msub></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>b</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>c</mi><mfenced><mstyle displaystyle="true"><mfrac><mn>42</mn><mn>11</mn></mfrac></mstyle></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><mn>11</mn></mfrac><mo>=</mo><mfrac><mi>b</mi><mn>22</mn></mfrac><mo>=</mo><mfrac><mi>c</mi><mn>42</mn></mfrac></math></p>

</details>

---

### Q14. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of ordered pairs <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>r</mi><mo>,</mo><mi>k</mi></mrow></mfenced></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mmultiscripts><msub><mi>C</mi><mi>r</mi></msub><mprescripts></mprescripts><none></none><mn>35</mn></mmultiscripts><mo>=</mo><mfenced separators="|"><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn></mrow></mfenced><mo>.</mo><mmultiscripts><msub><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mprescripts></mprescripts><none></none><mn>36</mn></mmultiscripts><mo>,</mo></math> where <math><mi>k</mi></math> is an integer is

**Options:**

- **(A)** <math><mn>3</mn></math>
- **(B)** <math><mn>2</mn></math>
- **(C)** <math><mn>6</mn></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>4</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mmultiscripts><msub><mi>C</mi><mi>r</mi></msub><mprescripts/><none/><mn>35</mn></mmultiscripts><mo>=</mo><mfenced separators="|"><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn></mrow></mfenced><mo>.</mo><mmultiscripts><msub><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mprescripts/><none/><mn>36</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>36</mn><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac><msup><mo>&#215;</mo><mn>35</mn></msup><msub><mi>C</mi><mi>r</mi></msub><mfenced separators="|"><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>6</mn><msup><mo>&#215;</mo><mn>35</mn></msup><msub><mi>C</mi><mi>r</mi></msub></math>, using properties of binomial coefficient.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mo>=</mo><mfrac><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mo>+</mo><mfrac><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mn>6</mn></mfrac></math></p><p><math><mi>r</mi></math> can be <math><mn>5,35</mn></math></p><p>For <math><mi>r</mi><mo>=</mo><mn>5</mn><mo>,</mo><mi></mi><mi>k</mi><mo>=</mo><mo>&#177;</mo><mn>2</mn></math></p><p><math><mi>r</mi><mo>=</mo><mn>35</mn><mo>,</mo><mi></mi><mi>k</mi><mo>=</mo><mo>&#177;</mo><mn>3</mn></math></p><p>Hence, number of solution <math><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q15. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mi>n</mi></msup><msub><mi>C</mi><mn>4</mn></msub><mo>,</mo><msup><mi>&#160;</mi><mi>n</mi></msup><msub><mi>C</mi><mn>5</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mi>n</mi></msup><msub><mi>C</mi><mn>6</mn></msub></math> are in A.P., then <math><mi>n</mi></math> can be

**Options:**

- **(A)** <math><mn>9</mn></math>
- **(B)** <math><mi> </mi><mn>14</mn></math>
- **(C)** <math><mi> </mi><mn>12</mn></math>
- **(D)** <math><mi> </mi><mn>11</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi> </mi><mn>14</mn></math>**

**Detailed Solution:**

<p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mi>n</mi></msup><msub><mi>C</mi><mn>4</mn></msub><mo>,</mo><msup><mi>&#160;</mi><mi>n</mi></msup><msub><mi>C</mi><mn>5</mn></msub><mo>,</mo><msup><mi>&#160;</mi><mi>n</mi></msup><msub><mi>C</mi><mn>6</mn></msub></math> are in A.P.

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mo>&#215;</mo><mi>n</mi></msup><msub><mi>C</mi><mn>5</mn></msub><msup><mo>=</mo><mi>n</mi></msup><msub><mi>C</mi><mn>4</mn></msub><msup><mo>+</mo><mi>n</mi></msup><msub><mi>C</mi><mn>6</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#215;</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mn>5</mn><mo>!</mo><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mn>4</mn><mo>!</mo><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mn>6</mn><mo>!</mo><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>2</mn><mrow><mn>5</mn><mo>!</mo><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>30</mn><mo>+</mo><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></mfenced></mrow><mrow><mn>6</mn><mo>!</mo><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mo>&#215;</mo><mn>2</mn><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>30</mn><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mi>n</mi><mo>+</mo><mn>20</mn></math></p><p><math><mo>&#8658;</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>21</mn><mi>n</mi><mo>+</mo><mn>98</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>14</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>7</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math></p>

</details>

---

