# JEE Main Mathematics - Differentiation

## Topic 9: Functional Equation

**Total Questions:** 7

---

### Q1. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)$ and $g(x)$ be twice differentiable functions satisfying $f''(x) = g''(x)$ for all $x \in \mathbf{R}$, $f'(1) = 2g'(1) = 4$ and $g(2) = 3f(2) = 9$. Then $f(25) - g(25)$ is equal to :

**Options:**

- **(A)** $20$
- **(B)** $40$
- **(C)** $-20$
- **(D)** $-40$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $40$**

**Detailed Solution:**

Given $f''(x) = g''(x)$ for all $x \in \mathbf{R}$.

Let $h(x) = f(x) - g(x)$.

Taking the second derivative, $h''(x) = f''(x) - g''(x) = 0$.

Integrating with respect to $x$, $h'(x) = c_1$.

Given $f'(1) = 4$ and $g'(1) = 2$, $h'(1) = f'(1) - g'(1) = 4 - 2 = 2$.

Therefore, $c_1 = 2$, which gives $h'(x) = 2$.

Integrating again with respect to $x$, $h(x) = 2x + c_2$.

Given $3f(2) = 9 \Rightarrow f(2) = 3$ and $g(2) = 9$, $h(2) = f(2) - g(2) = 3 - 9 = -6$.

Substituting $x = 2$ in $h(x)$, $h(2) = 2(2) + c_2 = -6 \Rightarrow c_2 = -10$.

Thus, $h(x) = 2x - 10$.

Substituting $x = 25$, $h(25) = f(25) - g(25) = 2(25) - 10 = 40$.

Answer: $40$

</details>

---

### Q2. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f$ be a real polynomial of degree $n$ such that $f(x) = f'(x) f''(x)$, for all $x \in \mathbb{R}$. If $f(0) = 0$, then $36\left(f'(2) + f''(2) + \int_0^2 f(x)\,dx\right)$ is equal to:

**Options:**

- **(A)** $42$
- **(B)** $46$
- **(C)** $56$
- **(D)** $66$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $56$**

**Detailed Solution:**

Let the degree of the polynomial $f(x)$ be $n$.

The degree of $f'(x)$ is $n-1$ and the degree of $f''(x)$ is $n-2$.

Since $f(x) = f'(x) f''(x)$, equating the degrees on both sides gives:

$n = (n-1) + (n-2) \Rightarrow n = 3$

Let $f(x) = ax^3 + bx^2 + cx + d$.

Given $f(0) = 0$, we get $d = 0$. Thus, $f(x) = ax^3 + bx^2 + cx$.

Differentiating $f(x)$ with respect to $x$:

$f'(x) = 3ax^2 + 2bx + c$

$f''(x) = 6ax + 2b$

Substituting these into the given equation $f(x) = f'(x) f''(x)$:

$ax^3 + bx^2 + cx = (3ax^2 + 2bx + c)(6ax + 2b)$

$ax^3 + bx^2 + cx = 18a^2x^3 + 18abx^2 + (4b^2 + 6ac)x + 2bc$

Comparing the coefficients of corresponding powers of $x$:

For $x^3$: $a = 18a^2 \Rightarrow a = \dfrac{1}{18}$ (since $a \neq 0$ for a cubic polynomial)

For the constant term: $0 = 2bc$

For $x$: $c = 4b^2 + 6ac$

Substituting $a = \dfrac{1}{18}$ into the $x$ coefficient equation:

$c = 4b^2 + \dfrac{c}{3} \Rightarrow \dfrac{2c}{3} = 4b^2 \Rightarrow c = 6b^2$

From $0 = 2bc$, either $b = 0$ or $c = 0$. In either case, since $c = 6b^2$, we get $b = 0$ and $c = 0$.

Thus, the polynomial is $f(x) = \dfrac{1}{18}x^3$.

Now, finding the required values:

$f'(x) = \dfrac{1}{6}x^2 \Rightarrow f'(2) = \dfrac{4}{6} = \dfrac{2}{3}$

$f''(x) = \dfrac{1}{3}x \Rightarrow f''(2) = \dfrac{2}{3}$

$\int_0^2 f(x)\,dx = \int_0^2 \dfrac{1}{18}x^3\,dx = \dfrac{1}{18} \left[ \dfrac{x^4}{4} \right]_0^2 = \dfrac{16}{72} = \dfrac{2}{9}$

Substituting these into the given expression:

$36\left(f'(2) + f''(2) + \int_0^2 f(x)\,dx\right) = 36\left(\dfrac{2}{3} + \dfrac{2}{3} + \dfrac{2}{9}\right)$

$= 36\left(\dfrac{4}{3} + \dfrac{2}{9}\right) = 36\left(\dfrac{14}{9}\right) = 4 \times 14 = 56$

Answer: $56$

</details>

---

### Q3. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=x^{3}+x^{2} f^{\prime}(1)+2 x f^{\prime \prime}(2)+f^{\prime \prime \prime}(3), x \in \mathbf{R}$. Then the value of $f^{\prime}(5)$ is:

**Options:**

- **(A)** $\frac{117}{5}$
- **(B)** $\frac{657}{5}$
- **(C)** $\frac{2}{5}$
- **(D)** $\frac{62}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{117}{5}$**

**Detailed Solution:**

Let $a = f'(1)$, $b = f''(2)$, $c = f'''(3)$. Then $f(x) = x^3 + ax^2 + 2bx + c$.
Taking derivatives: $f'(x) = 3x^2 + 2ax + 2b$, $f''(x) = 6x + 2a$, $f'''(x) = 6$.
From $f'(1) = a$: $3 + 2a + 2b = a$ gives $a = -3 - 2b$.
From $f''(2) = b$: $12 + 2a = b$.
From $f'''(3) = c$: $c = 6$.
Substituting the first into the second: $b = 12 + 2(-3 - 2b) = 6 - 4b$ gives $5b = 6$, so $b = \frac{6}{5}$.
Then $a = -3 - \frac{12}{5} = -\frac{27}{5}$.
$f(x) = x^3 - \frac{27}{5}x^2 + \frac{12}{5}x + 6$
$f'(x) = 3x^2 - \frac{54}{5}x + \frac{12}{5}$
$f'(5) = 75 - 54 + \frac{12}{5} = \frac{117}{5}$

</details>

---

### Q4. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $f: \mathbf{R} \rightarrow \mathbf{R}$ be a twice differentiable function such that $(\sin x \cos y)(f(2 x+2 y)-f(2 x-2 y))=(\cos x$ $\sin \mathrm{y})(f(2 \mathrm{x}+2 \mathrm{y})+f(2 \mathrm{x}-2 \mathrm{y}))$, for all $\mathrm{x}, \mathrm{y} \in \mathbf{R}$.
If $f^{\prime}(0)=\frac{1}{2}$, then the value of $24 f^{\prime \prime}\left(\frac{5 \pi}{3}\right)$ is:

**Options:**

- **(A)** 2
- **(B)** $-3$
- **(C)** 3
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-3$**

**Detailed Solution:**

$\begin{aligned} & (\sin x \cos y)(f(2 x+2 y)-f(2 x-2 y))=(\cos x \sin y) \\ & (f(2 x+2 y)+f(2 x-2 y)) \\ & f(2 x+2 y)(\sin (x-y))=f(2 x-2 y) \sin (x+y) \\ & \frac{f(2 x+2 y)}{\sin (x+y)}=\frac{f(2 x-2 y)}{\sin (x-y)} \\ & \text { Put } 2 x+2 y=m, 2 x-2 y=n \\ & \frac{f(m)}{\sin \left(\frac{m}{2}\right)}=\frac{f(n)}{\sin \left(\frac{n}{2}\right)}=\mathrm{K} \\ & \Rightarrow f(m)=K \sin \left(\frac{m}{2}\right) \\ & \therefore f(x)=K \sin \left(\frac{x}{2}\right) \\ & f^{\prime}(x)=\frac{K}{2} \cos \left(\frac{x}{2}\right) \\ & P_{\text {Put }} x=0 ; \frac{1}{2}=\frac{K}{2} \Rightarrow K=1 \\ & f^{\prime}(x)=\frac{1}{2} \cos \frac{x}{2}\end{aligned}$
$\begin{aligned} & f^{\prime \prime}(x)=-\frac{1}{4} \sin \frac{x}{2} \\ & 4 f^{\prime \prime}\left(\frac{5 \pi}{3}\right)=\left(-\frac{1}{4} \sin \left(\frac{5 \pi}{6}\right)\right) 24 \\ & =\frac{-24}{8}=-3\end{aligned}$

</details>

---

### Q5. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x)=a x^3+b x^2+c x+41$ be such that $f(1)=40, f^{\prime}(1)=2$ and $f^{\prime}(1)=4$. Then $\mathrm{a}^2+\mathrm{b}^2+\mathrm{c}^2$ is equal to:

**Options:**

- **(A)** 73
- **(B)** 62
- **(C)** 51
- **(D)** 54

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 51**

**Detailed Solution:**

$\begin{aligned} & f(x)=a x^3+b x^2+c x+41 \\ & f^{\prime}(x)=3 a x^2+2 b x+c x \\ & \Rightarrow f^{\prime}(1)=3 a+2 b+c=2 \ldots(1)\end{aligned}$
$\begin{aligned} & \mathrm{f}^{\prime \prime}(\mathrm{n})=6 \mathrm{ax}+2 \mathrm{~b} \\ & \Rightarrow \mathrm{f}^{\prime \prime}(1)=6 \mathrm{a}+2 \mathrm{~b}=4 \\ & 3 \mathrm{a}+\mathrm{b}=2 \ldots \ldots \ldots .(2)\end{aligned}$
$\begin{aligned} & (1)-(2) \\ & b+c=0...(3)\end{aligned}$
$\begin{aligned}
& \mathrm{f}(1)=40 \\
& \mathrm{a}+\mathrm{b}+\mathrm{c}+41=40
\end{aligned}$
use (3)
$a+41=40$
by (2)
$\begin{aligned}
& -3+b=2 \Rightarrow b=5 \& c=-5 \\
& a^2+b^2+c^2=1+25+25=51
\end{aligned}$

</details>

---

### Q6. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>x</mi><msup><mi>f</mi><mo>"</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo><mo>+</mo><msup><mi>f</mi><mo>'''</mo></msup><mo>(</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo> </mo><mi>x</mi><mo>∈</mo><mi>R</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>10</mn><mo>)</mo></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **202**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>x</mi><msup><mi>f</mi><mo>"</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo><mo>+</mo><msup><mi>f</mi><mo>'''</mo></msup><mo>(</mo><mn>3</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><msup><mi>f</mi><mo>"</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>"</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'''</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'''</mo></msup><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>6</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>"</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>12</mn><mo>+</mo><mn>2</mn><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Putting this value in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>3</mn><mo>+</mo><mn>2</mn><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mn>12</mn><mo>+</mo><mn>2</mn><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>0</mn><mo>=</mo><mn>15</mn><mo>+</mo><mn>3</mn><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mo>-</mo><mn>5</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>"</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>12</mn><mo>+</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>"</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>2</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>v</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>·</mo><mo>(</mo><mo>-</mo><mn>5</mn><mo>)</mo><mo>+</mo><mi>x</mi><mo>·</mo><mo>(</mo><mn>2</mn><mo>)</mo><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>10</mn><mo>)</mo><mo>=</mo><mn>300</mn><mo>-</mo><mn>100</mn><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>10</mn><mo>)</mo><mo>=</mo><mn>202</mn></math></p>

</details>

---

### Q7. JEE Main 2022 (26 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> satisfy <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mi>x</mi></msup><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>+</mo><msup><mn>4</mn><mi>y</mi></msup><mo>(</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>,</mo><mo>&#8704;</mo><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>3</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>&#183;</mo><mfrac><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>4</mn></mfenced></mrow><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>2</mn></mfenced></mrow></mfrac></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **248**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mi>x</mi></msup><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>+</mo><msup><mn>4</mn><mi>y</mi></msup><mo>(</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mi>x</mi></msup><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>16</mn><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>16</mn><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>3</mn><mo>&#215;</mo><msup><mn>2</mn><mi>x</mi></msup><mi>ln</mi><mn>2</mn></math></p><p>Now put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>16</mn><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>2</mn></mfenced><mo>+</mo><mn>12</mn><mi>ln</mi><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>4</mn><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>+</mo><mn>3</mn><mo>&#215;</mo><msup><mn>4</mn><mi>y</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>4</mn><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>y</mi></mfenced><mo>+</mo><mn>3</mn><mo>&#215;</mo><msup><mn>4</mn><mi>y</mi></msup><mi>ln</mi><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>4</mn><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>2</mn></mfenced><mo>+</mo><mn>96</mn><mi>ln</mi><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mi>ii</mi></mfenced></math></p><p>solving eq. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>7</mn><mi>ln</mi><mn>2</mn></math></p><p>from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>124</mn><mi>ln</mi><mn>2</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>14</mn><mo>&#215;</mo><mfrac><mrow><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>4</mn></mfenced></mrow><mrow><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>2</mn></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>&#215;</mo><mfrac><mrow><mn>124</mn><mi>ln</mi><mn>2</mn></mrow><mrow><mn>7</mn><mi>ln</mi><mn>2</mn></mrow></mfrac><mo>=</mo><mn>248</mn></math></p>

</details>

---

