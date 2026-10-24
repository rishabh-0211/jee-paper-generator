# JEE Main Mathematics - Functions

## Topic 7: Inverse of a Function

**Total Questions:** 11

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $e$ be the base of natural logarithm and let $f: \{1, 2, 3, 4\} \rightarrow \{1, e, e^2, e^3\}$ and $g: \{1, e, e^2, e^3\} \rightarrow \left\{1, \dfrac{1}{2}, \dfrac{1}{3}, \dfrac{1}{4}\right\}$ be two bijective functions such that $f$ is strictly decreasing and $g$ is strictly increasing. If $\phi(x) = \left[f^{-1}\left\{g^{-1}\left(\dfrac{1}{2}\right)\right\}\right]^x$, then the area of the region $R = \{(x, y): x^2 \leq y \leq \phi(x), 0 \leq x \leq 1\}$ is:

**Options:**

- **(A)** $\dfrac{3 - \log_e(2)}{3\log_e(2)}$
- **(B)** $\dfrac{1}{3\log_e(2)}$
- **(C)** $3 + \log_e(2)$
- **(D)** $\dfrac{3 + \log_e(2)}{2 + \log_e(3)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{3 - \log_e(2)}{3\log_e(2)}$**

**Detailed Solution:**

Given $f: \{1, 2, 3, 4\} \rightarrow \{1, e, e^2, e^3\}$ is a strictly decreasing bijective function.

Arranging the domain and codomain in increasing order, we get $f(1) = e^3$, $f(2) = e^2$, $f(3) = e$, and $f(4) = 1$.

Given $g: \{1, e, e^2, e^3\} \rightarrow \left\{1, \dfrac{1}{2}, \dfrac{1}{3}, \dfrac{1}{4}\right\}$ is a strictly increasing bijective function.

Arranging the domain and codomain in increasing order, we get $g(1) = \dfrac{1}{4}$, $g(e) = \dfrac{1}{3}$, $g(e^2) = \dfrac{1}{2}$, and $g(e^3) = 1$.

Evaluating $\phi(x) = \left[f^{-1}\left\{g^{-1}\left(\dfrac{1}{2}\right)\right\}\right]^x$:

From the mapping of $g$, $g^{-1}\left(\dfrac{1}{2}\right) = e^2$.

From the mapping of $f$, $f^{-1}(e^2) = 2$.

Substituting these values, we get $\phi(x) = 2^x$.

The region $R$ is given by $x^2 \leq y \leq 2^x$ for $0 \leq x \leq 1$.

The area of the region $R$ is:

$\int_{0}^{1} (2^x - x^2) dx = \left[ \dfrac{2^x}{\log_e(2)} - \dfrac{x^3}{3} \right]_{0}^{1}$

$= \left( \dfrac{2}{\log_e(2)} - \dfrac{1}{3} \right) - \left( \dfrac{1}{\log_e(2)} - 0 \right)$

$= \dfrac{1}{\log_e(2)} - \dfrac{1}{3}$

$= \dfrac{3 - \log_e(2)}{3\log_e(2)}$

Answer: $\dfrac{3 - \log_e(2)}{3\log_e(2)}$

</details>

---

### Q2. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

For the function $f:[1,\infty) \rightarrow [1,\infty)$ defined by $f(x)=(x-1)^4+1$, among the two statements:
(I) The set $S=\{x \in [1,\infty): f(x)=f^{-1}(x)\}$ contains exactly two elements, and
(II) The set $S=\{x \in [1,\infty): f(x)=f^{-1}(x+1)\}$ is an empty set,

**Options:**

- **(A)** only (I) is TRUE
- **(B)** only (II) is TRUE
- **(C)** both (I) and (II) are TRUE
- **(D)** neither (I) nor (II) is TRUE

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) only (I) is TRUE**

**Detailed Solution:**

Given $f(x) = (x-1)^4 + 1$ for $x \ge 1$.

To find the inverse function $f^{-1}(x)$, let $y = (x-1)^4 + 1$.

$\Rightarrow (x-1)^4 = y-1 \Rightarrow x-1 = (y-1)^{1/4} \Rightarrow x = (y-1)^{1/4} + 1$.

Thus, $f^{-1}(x) = (x-1)^{1/4} + 1$.

Evaluating the first statement, since $f'(x) = 4(x-1)^3 \ge 0$ for $x \ge 1$, $f(x)$ is strictly increasing. For a strictly increasing function, the solutions to $f(x) = f^{-1}(x)$ are the same as the solutions to $f(x) = x$.

$(x-1)^4 + 1 = x \Rightarrow (x-1)^4 - (x-1) = 0$.

Let $t = x-1 \ge 0$.

$t^4 - t = 0 \Rightarrow t(t-1)(t^2+t+1) = 0$.

Since $t \ge 0$, the real roots are $t = 0$ and $t = 1$.

$\Rightarrow x-1 = 0 \Rightarrow x = 1$

$\Rightarrow x-1 = 1 \Rightarrow x = 2$

Both $x=1$ and $x=2$ lie in $[1, \infty)$. The set contains exactly two elements, making Statement (I) TRUE.

Evaluating the second statement, the equation is $f(x) = f^{-1}(x+1)$.

$f^{-1}(x+1) = (x+1-1)^{1/4} + 1 = x^{1/4} + 1$.

Equating $f(x)$ and $f^{-1}(x+1)$:

$(x-1)^4 + 1 = x^{1/4} + 1 \Rightarrow (x-1)^4 - x^{1/4} = 0$.

Let $g(x) = (x-1)^4 - x^{1/4}$.

$g(2) = (2-1)^4 - 2^{1/4} = 1 - 2^{1/4} < 0$.

$g(3) = (3-1)^4 - 3^{1/4} = 16 - 3^{1/4} > 0$.

Since $g(x)$ is a continuous function on $[1, \infty)$ and changes sign between $x=2$ and $x=3$, by the Intermediate Value Theorem, there exists at least one real root in the interval $(2, 3)$.

Thus, the set is not empty, making Statement (II) FALSE.

Therefore, only (I) is TRUE.

Answer: only (I) is TRUE

</details>

---

### Q3. JEE Main 2023 (25 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

For some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><mi>x</mi><mo>-</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mi>b</mi></msup><mo>+</mo><mi>c</mi><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>f</mi><mi>o</mi><mi>g</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>7</mn></mrow><mn>2</mn></mfrac></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>f</mi><mo>&#8728;</mo><mi>g</mi></mrow></mfenced><mfenced><mrow><mi>a</mi><mi>c</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>g</mi><mo>&#8728;</mo><mi>f</mi></mrow></mfenced><mfenced><mi>b</mi></mfenced></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2039**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><mi>x</mi><mo>-</mo><mn>3</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mi>b</mi></msup><mo>+</mo><mi>c</mi><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>f</mi><mi>o</mi><mi>g</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>7</mn></mrow><mn>2</mn></mfrac></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></math></p><p>Now, let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>f</mi><mo>&#8728;</mo><mi>g</mi></mrow></mfenced><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>h</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>7</mn></mrow><mn>2</mn></mfrac></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></math></p><p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>7</mn></mrow><mn>2</mn></mfrac></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>3</mn></msup><mo>=</mo><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>7</mn></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn><msup><mi>y</mi><mn>3</mn></msup><mo>+</mo><mn>7</mn></math></p><p>So, inverse of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>7</mn></math> i.e., </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>7</mn></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><mfenced><mrow><msup><mi>x</mi><mi>b</mi></msup><mo>+</mo><mi>c</mi></mrow></mfenced><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><msup><mi>x</mi><mi>b</mi></msup><mo>+</mo><mi>a</mi><mi>c</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>7</mn></math></p><p>On comparing, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>c</mi><mo>=</mo><mn>5</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mspace linebreak="newline"></mspace><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>5</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mi>c</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mn>10</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1005</mn></mfenced><mo>=</mo><mn>2007</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>g</mi><mi>o</mi><mi>f</mi></mrow></mfenced><mfenced><mi>b</mi></mfenced><mo>=</mo><mi>g</mi><mi>o</mi><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>32</mn></math></p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mi>c</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>g</mi><mi>o</mi><mi>f</mi></mrow></mfenced><mfenced><mi>b</mi></mfenced><mo>=</mo><mn>2007</mn><mo>+</mo><mn>32</mn><mo>=</mo><mn>2039</mn></math></p>

</details>

---

### Q4. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>-</mo><mo>{</mo><mn>3</mn><mo>}</mo><mo>&#8594;</mo><mi>R</mi><mo>-</mo><mo>{</mo><mn>1</mn><mo>}</mo></math> be defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfrac></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be given as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></math>. Then, the sum of all the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>g</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>13</mn><mn>2</mn></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>f</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#38;</mo><mo>&#160;</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>y</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>g</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><msup><mi>f</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>g</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>13</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>13</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math> has roots <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> sum of roots <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q5. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The inverse of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mn>5</mn><mrow><mi>log</mi><mi>x</mi></mrow></msup></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msup><mn>5</mn><mrow><mi>log</mi><mi>y</mi></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msup><mi>y</mi><mrow><mi>log</mi><mn>5</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mfrac><mn>1</mn><mrow><mi>log</mi><mn>5</mn></mrow></mfrac></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msup><mn>5</mn><mfrac><mn>1</mn><mrow><mi>log</mi><mi>y</mi></mrow></mfrac></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mfrac><mn>1</mn><mrow><mi>log</mi><mn>5</mn></mrow></mfrac></msup></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mn>5</mn><mrow><mi>log</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mrow><mi>log</mi><mn>5</mn></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>b</mi><mrow><mi>log</mi><mi>a</mi></mrow></msup><mo>=</mo><msup><mi>a</mi><mrow><mi>log</mi><mi>b</mi></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mfrac><mn>1</mn><mrow><mi>log</mi><mn>5</mn></mrow></mfrac></msup><mo>=</mo><mi>x</mi></math></p><p>Replacing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8594;</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mfrac><mn>1</mn><mrow><mi>log</mi><mn>5</mn></mrow></mfrac></msup><mo>=</mo><mi>y</mi></math></p>

</details>

---

### Q6. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The inverse function of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mn>8</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mn>8</mn><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow><mrow><msup><mn>8</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>8</mn><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo></math> is __________.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><msub><mi>log</mi><mi>e</mi></msub></mfenced><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><msub><mi>log</mi><mn>8</mn></msub><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><msub><mi>log</mi><mn>8</mn></msub><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><msup><mn>8</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mn>8</mn><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow><mrow><msup><mn>8</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>8</mn><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><msup><mn>8</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup><msup><mn>8</mn><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mfrac></math>    (Applying componendo-dividendo)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mn>8</mn><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>y</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>4</mn><mi>x</mi><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mi mathvariant="normal">g</mi><mn>8</mn></msub><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>y</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mi mathvariant="normal">g</mi><mn>8</mn></msub><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mi>s</mi></math></p>

</details>

---

### Q7. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `2`

Let $f: \mathrm{A} \rightarrow$ B be a function defined as $f(x)=$ $\frac{x-1}{x-2}$, where $A=R-\{2\}$ and $B=R-\{1\}$. Then $f$ is

**Options:**

- **(A)** invertible and $f^{-1}(y)=\frac{2 y+1}{y-1}$
- **(B)** invertible and $f^{-1}(y)=\frac{3 y-1}{y-1}$
- **(C)** no invertible
- **(D)** invertible and $f^{-1}(y)=\frac{2 y-1}{y-1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) invertible and $f^{-1}(y)=\frac{2 y-1}{y-1}$**

**Detailed Solution:**

Suppose $y=f(x)$
$$
\begin{aligned}
&\Rightarrow y=\frac{x-1}{x-2} \\
&\Rightarrow y x-2 y=x-1 \\
&\Rightarrow(y-1) x=2 y-1 \\
&\Rightarrow x=f^{-1}(y)=\frac{2 y-1}{y-1}
\end{aligned}
$$
As the function is invertible on the given domain and its inverse can be obtained as above.

</details>

---

### Q8. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=x^2-x+5, x>\frac{1}{2}$, and $\mathrm{g}(\mathrm{x})$ is its inverse function, then $\mathrm{g}^{\prime}(7)$ equals:

**Options:**

- **(A)** $-\frac{1}{3}$
- **(B)** $\frac{1}{13}$
- **(C)** $\frac{1}{3}$
- **(D)** $-\frac{1}{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{3}$**

**Detailed Solution:**

$f(x)=y=x^2-x+5$
$$
\begin{aligned}
&x^2-x+\frac{1}{4}-\frac{1}{4}+5=y \\
&\left(x-\frac{1}{2}\right)^2+\frac{19}{4}=y \\
&\left(x-\frac{1}{2}\right)^2=y-\frac{19}{4} \\
&x-\frac{1}{2}=\pm \sqrt{y-\frac{19}{4}}
\end{aligned}
$$

$$
\begin{aligned}
&x=\frac{1}{2} \pm \sqrt{y-\frac{19}{4}} \\
&\text { As } x>\frac{1}{2} \\
&x=\frac{1}{2}+\sqrt{y-\frac{19}{4}} \\
&g(x)=\frac{1}{2}+\sqrt{x-\frac{19}{4}} \\
&g^{\prime}(x)=\frac{1}{2 \sqrt{x-\frac{19}{4}}}
\end{aligned}
$$

$$
g^{\prime}(7)=\frac{1}{2 \sqrt{7-\frac{19}{4}}}=\frac{1}{2 \frac{\sqrt{28-19}}{2}}=\frac{1}{3}
$$

</details>

---

### Q9. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is the inverse of a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>5</mn></msup></mrow></mfrac><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mfenced open="{" close="}"><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mn>5</mn></msup></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mfenced open="{" close="}"><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mn>5</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>5</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msup><mi>x</mi><mn>4</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mfenced open="{" close="}"><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mn>5</mn></msup></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is the inverse of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> i.e.  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mi>x</mi></mfenced><mi>&#160;</mi></math>

<math><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi></math>

Differentiating both the sides w.r.t <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> , we get

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mo>.</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced></mrow></mfrac></math>as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>&#160;</mi><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>5</mn></msup></mrow></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mfenced separators="|"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mn>5</mn></msup></mrow></mfrac></mfenced></mfrac><mi>&#160;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><msup><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mn>5</mn></msup></math></p></blockquote>

</details>

---

### Q10. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=(x+1)^2-1, x \geq-1$
Statement-1: The set $\left\{x: f(x)=f^{-1}(x)\right\}=\{0,-1\}$
Statement-2 : $\mathrm{f}$ is a bijection.

**Options:**

- **(A)** Statement-1 is true, Statement-2 is true; Statement-2 is a correct explanation for Statement-1
- **(B)** Statement-1 is true, Statement-2 is true; Statement-2 is not a correct explanation for Statement-1
- **(C)** Statement-1 is true, Statement-2 is false
- **(D)** Statement-1 is false, Statement-2 is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement-1 is true, Statement-2 is false**

**Detailed Solution:**

There is no information about co-domain therefore $f(x)$ is not necessarily onto.

</details>

---

### Q11. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

Let $f: N \rightarrow Y$ be a function defined as $f(x)=4 x+3$, where $Y=\{y \in N: y=4 x+3$ for some $x \in N\}$. Show that $\mathrm{f}$ is invertible and its inverse is

**Options:**

- **(A)** $g(y)=\frac{3 y+4}{3}$
- **(B)** $g(y)=4+\frac{y+3}{4}$
- **(C)** $g(y)=\frac{y+3}{4}$
- **(D)** $g(y)=\frac{y-3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $g(y)=\frac{y-3}{4}$**

**Detailed Solution:**

Function is increasing
$$
x=\frac{y-3}{4}=g(y)
$$

</details>

---

