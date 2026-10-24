# JEE Main Mathematics - Definite Integration

## Topic 10: Miscellaneous

**Total Questions:** 27

---

### Q1. JEE Main 2026 (02 April Shift 1)

*Type:* `numerical` | *Level:* `2`

If $\alpha = \displaystyle\int_0^{2\sqrt{3}} \log_2(x^2 + 4)\,dx + \displaystyle\int_2^4 \sqrt{2^x - 4}\,dx$, then $\alpha^2$ is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **192**

**Detailed Solution:**

Let $f(x) = \log_2(x^2 + 4)$ for $x \ge 0$.

To find the inverse function $f^{-1}(x)$, we set $y = \log_2(x^2 + 4)$ and solve for $x$:

$2^y = x^2 + 4$

$x^2 = 2^y - 4$

$x = \sqrt{2^y - 4}$

Thus, $f^{-1}(x) = \sqrt{2^x - 4}$.

The given expression is $\alpha = \displaystyle\int_0^{2\sqrt{3}} f(x)\,dx + \displaystyle\int_2^4 f^{-1}(x)\,dx$.

We observe the limits of the first integral and evaluate the function at these points:

$f(0) = \log_2(0 + 4) = 2$

$f(2\sqrt{3}) = \log_2((2\sqrt{3})^2 + 4) = \log_2(12 + 4) = \log_2(16) = 4$

These exactly match the limits of the second integral. Using the standard property of definite integrals for inverse functions:

$\displaystyle\int_a^b f(x)\,dx + \displaystyle\int_{f(a)}^{f(b)} f^{-1}(x)\,dx = b f(b) - a f(a)$

Substituting $a = 0$ and $b = 2\sqrt{3}$:

$\alpha = 2\sqrt{3} \cdot f(2\sqrt{3}) - 0 \cdot f(0)$

$\alpha = 2\sqrt{3} \cdot 4 - 0 = 8\sqrt{3}$

Therefore, $\alpha^2 = (8\sqrt{3})^2 = 64 \times 3 = 192$.

Answer: $192$

</details>

---

### Q2. JEE Main 2024 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $[t]$ denote the largest integer less than or equal to $t$. If $\int_0^3\left(\left[x^2\right]+\left[\frac{x^2}{2}\right]\right) \mathrm{d} x=\mathrm{a}+\mathrm{b} \sqrt{2}-\sqrt{3}-\sqrt{5}+\mathrm{c} \sqrt{6}-\sqrt{7}$, where $\mathrm{a}, \mathrm{b}, \mathrm{c} \in \mathbf{Z}$, then $\mathrm{a}+\mathrm{b}+\mathrm{c}$ is equal to_______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **23**

**Detailed Solution:**

$\begin{aligned} & \int_0^3\left[x^2\right] d x+\int_0^3\left[\frac{x^2}{2}\right] d x \\ & =\int_0^1 0 d x+\int_1^{12} 1 d x+\int_{\sqrt{2}}^{\sqrt{3}} 2 d x\end{aligned}$
$\begin{aligned} & +\int_{\sqrt{3}}^2 3 \mathrm{dx}+\int_2^{\sqrt{5}} 4 \mathrm{dx}+\int_{\sqrt{5}}^{\sqrt{6}} 5 \mathrm{dx} \\ & +\int_{\sqrt{6}}^{\sqrt{7}} 6 \mathrm{dx}+\int_{\sqrt{7}}^{\sqrt{8}} 7 \mathrm{dx}+\int_{\sqrt{8}}^3 8 \mathrm{dx} \\ & +\int_0^{\sqrt{2}} 0 \mathrm{dx}+\int_{\sqrt{2}}^2 1 \mathrm{dx} \\ & +\int_2^{\sqrt{6}} 2 \mathrm{dx}+\int_{\sqrt{6}}^{\sqrt{8}} 3 \mathrm{dx}+\int_{\sqrt{8}}^3 4 \mathrm{dx}=31-6 \sqrt{2}-\sqrt{3}-\sqrt{5} \\ & -2 \sqrt{6}-\sqrt{7} \\ & \mathrm{a}=31 \quad \mathrm{~b}=-6 \quad \mathrm{c}=-2 \\ & \mathrm{a}+\mathrm{b}+\mathrm{c}=31-6-2=23\end{aligned}$

</details>

---

### Q3. JEE Main 2024 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $r_k=\frac{\int_0^1\left(1-x^7\right)^k d x}{\int_0^1\left(1-x^7\right)^{k+1} d x}, k \in \mathbb{N}$. Then the value of $\sum_{k=1}^{10} \frac{1}{7\left(r_k-1\right)}$ is equal to________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **65**

**Detailed Solution:**

$\begin{aligned} & I_K=\int 1 \cdot\left(1-x^7\right)^K d x \\ & I_K=\left.\left(1-x^7\right)^K x\right|_0 ^1+7 K \int_0^1\left(1-x^7\right)^{K-1} x^6 \cdot x d x \\ & I_K=-7 K \int_0^1\left(1-x^7\right)^{K-1}\left(\left(1-x^7\right)-1\right) d x \\ & I_K=-7 K I_K+7 K I_{K-1} \\ & \Rightarrow \frac{I_K}{I_{K+1}}=\frac{7 K+8}{7 K+7}\end{aligned}$
$\begin{aligned} & r_K=\frac{7 K+8}{7 \mathrm{~K}+7} \\ & \mathrm{r}_{\mathrm{K}}-1=\frac{1}{7(\mathrm{~K}+1)} \\ & \Rightarrow 7\left(\mathrm{r}_{\mathrm{K}}-1\right)=\frac{1}{\mathrm{~K}+1} \\ & \sum_{\mathrm{K}=1}^{10}(\mathrm{~K}+1)=11(6)-1=65\end{aligned}$

</details>

---

### Q4. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\beta(\mathrm{m}, \mathrm{n})=\int_0^1 x^{\mathrm{m}-1}(1-x)^{\mathrm{n}-1} \mathrm{~d} x, \mathrm{~m}, \mathrm{n}>0$. If $\int_0^1\left(1-x^{10}\right)^{20} \mathrm{~d} x=\mathrm{a} \times \beta(\mathrm{b}, \mathrm{c})$, then $100(\mathrm{a}+\mathrm{b}+\mathrm{c})$ equals____

**Options:**

- **(A)** 1021
- **(B)** 2120
- **(C)** 2012
- **(D)** 1120

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2120**

**Detailed Solution:**

$I=\int_0^1 1 \cdot\left(1-x^{10}\right)^{20} d x$
$x^{10}=t$
$x=t^{1 / 10}$
$d x=\frac{1}{10}(t)^{-9 / 10} d t$
$I=\int_0^1(1-t)^{20} \frac{1}{10}(t)^{-9 / 10} d t$
$I=\frac{1}{10} \int_0^1 t^{-9 / 10}(1-t)^{20} d t$
$a=\frac{1}{10} \quad b=\frac{1}{10} \quad c=21$

</details>

---

### Q5. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=\left\{\begin{array}{lr}-2, & -2 \leq x \leq 0 \\ x-2, & 0 < x \leq 2\end{array}\right.$ and $h(x)=f(|x|)+|f(x)|$. Then $\int_{-2}^2 h(x) \mathrm{d} x$ is equal to :

**Options:**

- **(A)** 1
- **(B)** 6
- **(C)** 4
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/_wTtb51XRkzBlctq3MgM6PuxkQpuoGAWkX4RHpNhWys.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/G6J7lax-dyrGR9LbqafRvFPZrkK9zwmYb0XjRSr73mo.original.fullsize.png">
$h(x)=\left\{\begin{array}{cc}x-2+2-x=0, & 0 \leq x \leq 2 \\ -x-2+2=-x & -2 \leq x < 0\end{array}\right.$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/LdGJd85PxPC_0l0fHOesAWikty9K_gg5qnm8TJx84kA.original.fullsize.png">
$\Rightarrow \int_0^2 \mathrm{~h}(\mathrm{x}) \mathrm{dx}=0$ and $\int_{-2}^0 \mathrm{~h}(\mathrm{x}) \mathrm{dx}=2$

</details>

---

### Q6. JEE Main 2024 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

If the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>525</mn><munderover><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></munderover><mi>sin</mi><mn>2</mn><mi>x</mi><mo> </mo><msup><mi>cos</mi><mfrac><mn>11</mn><mn>2</mn></mfrac></msup><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mfrac><mn>5</mn><mn>2</mn></mfrac></msup><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mi>d</mi><mi>x</mi></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>n</mi><msqrt><mn>2</mn></msqrt><mo>−</mo><mn>64</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **176**

**Detailed Solution:**

<p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>∫</mo><mn>0</mn><mfrac><mi>π</mi><mn>2</mn></mfrac></munderover><mi>sin</mi><mn>2</mn><mi>x</mi><mo> </mo><msup><mi>cos</mi><mfrac><mn>11</mn><mn>2</mn></mfrac></msup><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mfrac><mn>5</mn><mn>2</mn></mfrac></msup><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup><mo>⇒</mo><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>t</mi><mo> </mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>4</mn><munderover><mo>∫</mo><mn>1</mn><mn>0</mn></munderover><msup><mi>t</mi><mn>2</mn></msup><mo>⋅</mo><msup><mi>t</mi><mn>11</mn></msup><msqrt><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>5</mn></msup></mrow></mfenced></msqrt><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>4</mn><munderover><mo>∫</mo><mn>0</mn><mn>1</mn></munderover><msup><mi>t</mi><mn>14</mn></msup><msqrt><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>5</mn></msup></mrow></mfenced></msqrt><mi>d</mi><mi>t</mi></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>5</mn></msup><mo>=</mo><msup><mi>k</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>5</mn><msup><mi>t</mi><mn>4</mn></msup><mi>d</mi><mi>t</mi><mo>=</mo><mn>2</mn><mi>k</mi><mo> </mo><mi>d</mi><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mi>I</mi><mo>=</mo><mn>4</mn><mo>⋅</mo><munderover><mo>∫</mo><mn>1</mn><msqrt><mn>2</mn></msqrt></munderover><msup><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>−</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>⋅</mo><mi>k</mi><mo>·</mo><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mn>5</mn></mfrac><mi>d</mi><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><munderover><mo>∫</mo><mn>1</mn><msqrt><mn>2</mn></msqrt></munderover><msup><mi>k</mi><mn>6</mn></msup><mo>−</mo><mn>2</mn><msup><mi>k</mi><mn>4</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo> </mo><mi>d</mi><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><mfrac><msup><mi>k</mi><mn>7</mn></msup><mn>7</mn></mfrac><mo>−</mo><mfrac><mrow><mn>2</mn><msup><mi>k</mi><mn>5</mn></msup></mrow><mn>5</mn></mfrac><mo>+</mo><mfrac><msup><mi>k</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mn>1</mn><msqrt><mn>2</mn></msqrt></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt></mrow><mn>7</mn></mfrac><mo>−</mo><mfrac><mrow><mn>8</mn><msqrt><mn>2</mn></msqrt></mrow><mn>5</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mn>3</mn></mfrac><mo>−</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>−</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mrow><mn>22</mn><msqrt><mn>2</mn></msqrt></mrow><mn>105</mn></mfrac><mo>−</mo><mfrac><mn>8</mn><mn>105</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>525</mn><mo>⋅</mo><mi>I</mi><mo>=</mo><mn>176</mn><msqrt><mn>2</mn></msqrt><mo>−</mo><mn>64</mn></math></p><p>Hence, on comparing we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>176</mn></math></p>

</details>

---

### Q7. JEE Main 2023 (13 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mi>sin</mi><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mo>(</mo><mn>2</mn><mi>k</mi><mo>-</mo><mn>1</mn><mo>)</mo><msup><mi>sin</mi><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>21</mn></msub><mo>-</mo><msub><mi>f</mi><mn>20</mn></msub></math> is equal to</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **41**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mi>sin</mi><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mo>(</mo><mn>2</mn><mi>k</mi><mo>-</mo><mn>1</mn><mo>)</mo><msup><mi>sin</mi><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p>Now let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mo>(</mo><mi>t</mi><msup><mo>)</mo><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mo>(</mo><mn>2</mn><mi>k</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>t</mi><msup><mo>)</mo><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>f</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>t</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>5</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>t</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p>Now multiply and divide by <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>t</mi></msqrt></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>f</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mfenced><mrow><msup><mi>t</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></msup><mo>+</mo><msup><mi>t</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup><mo>+</mo><msup><mi>t</mi><mfrac><mn>5</mn><mn>2</mn></mfrac></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>t</mi><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mstyle></msup></mrow></mfenced><msqrt><mi>t</mi></msqrt></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>5</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>t</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>f</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msup><mi>t</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>+</mo><msup><mi>t</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><msup><mi>t</mi><mfrac><mn>5</mn><mn>2</mn></mfrac></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>t</mi><mfrac><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></msup></mrow></mfenced><mfenced><mrow><msup><mi>t</mi><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></msup><mo>+</mo><mn>3</mn><msup><mi>t</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>+</mo><mn>5</mn><msup><mi>t</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>t</mi><mfrac><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></msup></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>+</mo><msup><mi>t</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><msup><mi>t</mi><mfrac><mn>5</mn><mn>2</mn></mfrac></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>t</mi><mfrac><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></msup><mo>=</mo><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msup><mi>t</mi><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></msup><mo>+</mo><mn>3</mn><msup><mi>t</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>+</mo><mn>5</mn><msup><mi>t</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>t</mi><mfrac><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></msup></mrow></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mi>d</mi><mi>z</mi></math></p><p>Hence, the integral becomes,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>f</mi><mi>n</mi></msub><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>n</mi></msubsup><mi>z</mi><mi>d</mi><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>f</mi><mi>n</mi></msub><mo>=</mo><msubsup><mfenced close="]" open="["><msup><mi>z</mi><mn>2</mn></msup></mfenced><mn>0</mn><mi>n</mi></msubsup><mo>=</mo><msup><mi>n</mi><mn>2</mn></msup></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>21</mn></msub><mo>-</mo><msub><mi>f</mi><mn>20</mn></msub><mo>=</mo><msup><mn>21</mn><mn>2</mn></msup><mo>-</mo><msup><mn>20</mn><mn>2</mn></msup><mo>=</mo><mn>41</mn></math></p></blockquote>

</details>

---

### Q8. JEE Main 2023 (13 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi><mo>,</mo><mo>&#160;</mo><msub><mi>S</mi><mn>0</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><msub><mi>S</mi><mi>k</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>C</mi><mi>k</mi></msub><mi>x</mi><mo>+</mo><mi>k</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msub><mi>S</mi><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msub><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>0</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>C</mi><mi>k</mi></msub><mo>=</mo><mn>1</mn><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msub><mi>S</mi><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msub><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mfenced><mn>3</mn></mfenced><mo>+</mo><mn>6</mn><msub><mi>C</mi><mn>3</mn></msub></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>0</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><msub><mi>S</mi><mi>k</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>C</mi><mi>k</mi></msub><mi>x</mi><mo>+</mo><mi>k</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msub><mi>S</mi><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msub><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math> </p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>0</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>,</mo><msub><mi>C</mi><mn>0</mn></msub><mo>=</mo><mn>1</mn></math></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mi>k</mi></msub><mo>=</mo><mn>1</mn><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msub><mi>S</mi><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msub><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Now putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>1</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>k</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>C</mi><mi>k</mi></msub><mi>x</mi><mo>+</mo><mi>k</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msub><mi>S</mi><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msub><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>&#183;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>2</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>7</mn><mn>12</mn></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>7</mn><mn>12</mn></mfrac><mi>x</mi><mo>+</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mfenced><mrow><mfrac><mi>t</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>7</mn><mi>x</mi></mrow><mn>12</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>3</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>3</mn></msub><mo>=</mo><mn>1</mn><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mfrac><mrow><mn>7</mn><mi>x</mi></mrow><mn>12</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>11</mn><mn>24</mn></mfrac></math></p><p>Now finding the value of<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mfenced><mn>3</mn></mfenced><mo>+</mo><mn>6</mn><mo>&#183;</mo><msub><mi>C</mi><mn>3</mn></msub></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mfenced><mn>3</mn></mfenced><mo>+</mo><mn>6</mn><mo>&#183;</mo><msub><mi>C</mi><mn>3</mn></msub><mo>=</mo><mfrac><mrow><mn>7</mn><mo>&#215;</mo><mn>3</mn></mrow><mn>12</mn></mfrac><mo>+</mo><mfrac><msup><mn>3</mn><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mn>3</mn><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mn>6</mn><mo>&#215;</mo><mfrac><mn>11</mn><mn>24</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>2</mn></msub><mfenced><mn>3</mn></mfenced><mo>+</mo><mn>6</mn><mo>&#183;</mo><msub><mi>C</mi><mn>3</mn></msub><mo>=</mo><mfrac><mn>61</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>11</mn><mn>4</mn></mfrac><mo>=</mo><mn>18</mn></math></p></blockquote>

</details>

---

### Q9. JEE Main 2023 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></msup></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#62;</mo><mn>2</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>n</mi></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>(</mo><mi>f</mi><mi>o</mi><mi>f</mi><mi>o</mi><mi>f</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> times) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>x</mi></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mfenced><mrow><msup><mi>f</mi><mi>n</mi></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math> is equal to</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

<blockquote><p>Given,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></msup></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#62;</mo><mn>2</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>n</mi></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>(</mo><mi>f</mi><mi>o</mi><mi>f</mi><mi>o</mi><mi>f</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> times) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>x</mi></mfenced></math>,</p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><msup><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><msup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mi>n</mi></msup></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfrac><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></msup></mfrac><msup><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><msup><mfenced><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></msup></mfrac></mfenced><mi>n</mi></msup></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></msup></mfrac></math></p><p>Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>n</mi></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>n</mi><mo>&#160;</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></msup></mfrac></math></p><p>Now solving the integral we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>n</mi><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p>Now let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>n</mi><msup><mi>x</mi><mi>n</mi></msup><mo>=</mo><msup><mi>t</mi><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>n</mi><mn>2</mn></msup><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mi>n</mi><msup><mi>t</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfenced><mfrac><mn>1</mn><mi>n</mi></mfrac></msup></msubsup><mo>&#160;</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle><msup><mi>t</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi>d</mi><mi>t</mi></mrow><mi>t</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><mfrac><msup><mi>t</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mn>1</mn><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfenced><mfrac><mn>1</mn><mi>n</mi></mfrac></msup></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mfenced><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Now solving the limit we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mfrac><mn>1</mn><mi>h</mi></mfrac></math> so the limit changes to,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>h</mi></mfrac></mrow></mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mi>h</mi></mstyle></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mfrac><mn>1</mn><mi>h</mi></mfrac><mfenced><mrow><mfrac><mn>1</mn><mi>h</mi></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>h</mi></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mi>h</mi></mrow></mfenced></mrow></mfenced><mo>-</mo><mn>1</mn></mrow><mrow><mfrac><mn>1</mn><mi>h</mi></mfrac><mfenced><mrow><mfrac><mn>1</mn><mi>h</mi></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mi>h</mi></mrow></mfenced><mfenced><mrow><mfrac><mn>1</mn><mi>h</mi></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>h</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>h</mi></mrow></mfenced></mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>h</mi></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>h</mi><mo>=</mo><mn>0</mn></math></p></blockquote>

</details>

---

### Q10. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><msup><mi>x</mi><mi>n</mi></msup><mi>n</mi></mfrac><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>. Then the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mfrac><msup><mi>t</mi><mn>50</mn></msup><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfrac><mi>d</mi><mi>t</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>-</mo><msub><mi>P</mi><mn>50</mn></msub><mfenced><mi>&#945;</mi></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><msub><mi>P</mi><mn>50</mn></msub><mfenced><mi>&#945;</mi></mfenced></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>50</mn></msub><mfenced><mi>&#945;</mi></mfenced><mo>-</mo><mi>&#946;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>+</mo><msub><mi>P</mi><mn>50</mn></msub><mfenced><mi>&#945;</mi></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><msub><mi>P</mi><mn>50</mn></msub><mfenced><mi>&#945;</mi></mfenced></mrow></mfenced></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mfrac><msup><mi>t</mi><mn>50</mn></msup><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>50</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfrac></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>50</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfrac></mfenced><mi>d</mi><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mfenced><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfrac></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>&#945;</mi></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>t</mi><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>t</mi><mn>49</mn></msup></mrow></mfenced><mi>d</mi><mi>t</mi><mo>-</mo><msubsup><mfenced open="[" close="]"><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced></mrow></mfenced><mn>0</mn><mi>&#945;</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><msubsup><mfenced open="[" close="]"><mrow><mi>t</mi><mo>+</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>t</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><msup><mi>t</mi><mn>50</mn></msup><mn>50</mn></mfrac></mrow></mfenced><mn>0</mn><mi>&#945;</mi></msubsup><mo>-</mo><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfenced open="[" close="]"><mrow><mi>&#945;</mi><mo>+</mo><mfrac><msup><mi>&#945;</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>&#945;</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><msup><mi>&#945;</mi><mn>50</mn></msup><mn>50</mn></mfrac></mrow></mfenced><mo>-</mo><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><msub><mi>P</mi><mn>50</mn></msub><mfenced><mi>&#945;</mi></mfenced></mrow></mfenced></math></p>

</details>

---

### Q11. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mfrac><mrow><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>t</mi><mn>6</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mi>d</mi><mi>t</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>8</mn><mo>-</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>8</mn><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>8</mn><mo>-</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>8</mn><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>8</mn><mo>-</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mrow><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>t</mi><mn>6</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mrow><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow><mrow><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>t</mi><mn>4</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><msup><mi>a</mi><mn>3</mn></msup><mo>+</mo><msup><mi>b</mi><mn>3</mn></msup><mo>=</mo><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>)</mo><mo>(</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mi>a</mi><mi>b</mi><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>)</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mrow><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow><mrow><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>t</mi><mn>4</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced close="]" open="["><mrow><mfrac><mrow><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow><mrow><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>t</mi><mn>4</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mrow><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>t</mi><mn>4</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></mrow></mfenced><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>+</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mrow><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>t</mi><mn>4</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></mrow></mfenced><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>+</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mrow><msup><mi>t</mi><mn>6</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mn>1</mn><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mi>d</mi><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><msup><mi>t</mi><mn>2</mn></msup><mrow><msup><mfenced><msup><mi>t</mi><mn>3</mn></msup></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfrac><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup></mrow><mrow><msup><mfenced><msup><mi>t</mi><mn>3</mn></msup></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>t</mi><mn>3</mn></msup></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>8</mn><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>8</mn><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>8</mn></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mo>+</mo><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>8</mn></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></math></p>

</details>

---

### Q12. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mi>a</mi><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mi>sin</mi><mi>x</mi><mo>+</mo><mfrac><mi>b</mi><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mi>cos</mi><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math> be a function which satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mi>f</mi><mfenced><mi>y</mi></mfenced><mi>d</mi><mi>y</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced></math>
is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#960;</mi><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>&#960;</mi><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>&#960;</mi><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#960;</mi><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>&#960;</mi><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mi>f</mi><mfenced><mi>y</mi></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mrow><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>y</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mi>sin</mi><mi>y</mi></mrow></mfenced><mi>f</mi><mfenced><mi>y</mi></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mrow><mfenced><mrow><mi>cos</mi><mi>y</mi><mi>f</mi><mfenced><mi>y</mi></mfenced><mi>d</mi><mi>y</mi></mrow></mfenced><mi>sin</mi><mi>x</mi><mo>+</mo><mfenced><mrow><mi>sin</mi><mi>y</mi><mi>f</mi><mfenced><mi>y</mi></mfenced><mi>d</mi><mi>y</mi></mrow></mfenced><mi>cos</mi><mi>x</mi></mrow></mfenced></math></p><p>And,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mi>a</mi><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mi>sin</mi><mi>x</mi><mo>+</mo><mfrac><mi>b</mi><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mi>cos</mi><mi>x</mi><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math></p><p>On comparing both the equations of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mi>cos</mi><mi>y</mi><mi>f</mi><mfenced><mi>y</mi></mfenced><mi>d</mi><mi>y</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>b</mi><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mi>sin</mi><mi>y</mi><mi>f</mi><mfenced><mi>y</mi></mfenced><mi>d</mi><mi>y</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Adding equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mrow><mi>sin</mi><mi>y</mi><mo>+</mo><mi>cos</mi><mi>y</mi></mrow></mfenced><mi>f</mi><mfenced><mi>y</mi></mfenced><mi>d</mi><mi>y</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>d</mo><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mo>(</mo><mi>a</mi><mo>-</mo><mi>x</mi><mo>)</mo><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mrow><mi>sin</mi><mi>y</mi><mo>+</mo><mi>cos</mi><mi>y</mi></mrow></mfenced><mi>f</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>y</mi></mrow></mfenced><mi>d</mi><mi>y</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>4</mn></mfenced></math></p><p>Add equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> and equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced></mrow><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mrow><mi>sin</mi><mi>y</mi><mo>+</mo><mi>cos</mi><mi>y</mi></mrow></mfenced><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mfenced><mrow><mi>sin</mi><mi>y</mi><mo>+</mo><mi>cos</mi><mi>y</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced></mrow><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mi>&#960;</mi><mo>+</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow><mrow><msup><mi>&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#960;</mi><mfenced><mrow><mi>&#960;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q13. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The minimum value of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><msup><mi>e</mi><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mi>t</mi></mrow></mfenced></msup><mi>d</mi><mi>t</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>e</mi><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><msup><mi>e</mi><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mi>t</mi></mrow></mfenced></msup><mi>d</mi><mi>t</mi></math></p><p>Now For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><msup><mi>e</mi><mrow><mi>t</mi><mo>-</mo><mi>x</mi></mrow></msup><mi>d</mi><mi>t</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mfenced><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>And for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mi>t</mi></mrow></msup><mi>d</mi><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mi>x</mi><mn>2</mn></msubsup><msup><mi>e</mi><mrow><mi>t</mi><mo>-</mo><mi>x</mi></mrow></msup><mi>d</mi><mi>t</mi><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><mn>2</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&#8805;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mi>t</mi></mrow></msup><mi>d</mi><mi>t</mi><mo>=</mo><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></msup><mfenced><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8804;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is decreasing as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math> is decreasing function and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></msup></math> is increasing function,</p><p>So, minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> lies in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Applying A.M <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8805;</mo></math> G.M in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></msup></math>we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></msup></mrow><mn>2</mn></mfrac><mo>&#8805;</mo><msqrt><msup><mi>e</mi><mi>x</mi></msup><mo>&#215;</mo><msup><mi>e</mi><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></msup><mo>&#8805;</mo><mn>2</mn><mi>e</mi></math></p><p>Hence, the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>e</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>2</mn><mfenced><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q14. JEE Main 2022 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mi>n</mi></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>3</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>n</mi></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math> for every <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>. Then the sum of all the elements of the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">N</mi><mo>:</mo><msub><mi>a</mi><mi>n</mi></msub><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>30</mn></mrow></mfenced></mrow></mfenced></math> is _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mi>n</mi></msubsup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>3</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>n</mi></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mfrac><msup><mi>x</mi><mi>n</mi></msup><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow><mi>n</mi></msubsup></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><msup><mn>1</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mrow><msup><mi>n</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mrow><msup><mi>n</mi><mn>4</mn></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>4</mn><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mrow><msup><mi>n</mi><mi>n</mi></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mo>+</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>+</mo><mfrac><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>4</mn><mo>+</mo><mn>2</mn><mo>+</mo><mfrac><mn>28</mn><mn>9</mn></mfrac><mo>=</mo><mfrac><mn>100</mn><mn>9</mn></mfrac><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>4</mn></msub><mo>=</mo><mn>5</mn><mo>+</mo><mfrac><mn>15</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>65</mn><mn>9</mn></mfrac><mo>+</mo><mfrac><mn>255</mn><mn>16</mn></mfrac><mo>&#62;</mo><mn>31</mn><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>30</mn></mrow></mfenced></math>, so the required set is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>  sum of all elements <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn></math>.</p></blockquote>

</details>

---

### Q15. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> be a real valued continuous function on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>t</mi></mrow></mfenced><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math>. Then which of the following points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced></math> lies on the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math>?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>17</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></mrow></mfenced><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>t</mi><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>A</mi><mi>x</mi><mo>-</mo><mi>B</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>1</mn><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mn>1</mn><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mi>A</mi><mi>t</mi><mo>-</mo><mi>B</mi></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>B</mi></mrow></mfenced><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>t</mi><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mi>A</mi><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup><mo>-</mo><mi>B</mi><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mi>B</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>18</mn><mn>13</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mfrac><mn>4</mn><mn>13</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>18</mn><mn>13</mn></mfrac><mi>x</mi><mo>-</mo><mfrac><mn>4</mn><mn>13</mn></mfrac></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>6</mn></mfenced><mo>=</mo><mfrac><mrow><mn>18</mn><mo>&#215;</mo><mn>6</mn><mo>-</mo><mn>4</mn></mrow><mn>13</mn></mfrac><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q16. JEE Main 2022 (24 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>Max</mo><mrow><mn>0</mn><mo>&#10877;</mo><mi>x</mi><mo>&#10877;</mo><mn>2</mn></mrow></munder><mfenced close="}" open="{"><mfrac><mrow><mn>9</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>5</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>Min</mi><mrow><mn>0</mn><mo>&#10877;</mo><mi>x</mi><mo>&#10877;</mo><mn>2</mn></mrow></munder><mfenced close="}" open="{"><mfrac><mrow><mn>9</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>5</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mi>&#946;</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mi>&#946;</mi><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></mrow><mrow><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></msubsup><mo>Max</mo><mfenced close="}" open="{"><mrow><mfrac><mrow><mn>9</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>5</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>,</mo><mi>x</mi></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi><mo>=</mo><msub><mi>&#945;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#945;</mi><mn>2</mn></msub><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>8</mn><mn>15</mn></mfrac></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#945;</mi><mn>2</mn></msub></math> is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **34**

**Detailed Solution:**

<p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mn>9</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>5</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mn>5</mn><mo>+</mo><mi>x</mi><mo>+</mo><mfrac><mn>16</mn><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>16</mn><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mfrac><mn>16</mn><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn></math></p><p>So critical point is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Now we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mfrac><mn>9</mn><mn>5</mn></mfrac><mo>,</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></msubsup><mi>max</mi><mfenced><mrow><mfrac><mrow><mn>9</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>5</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>,</mo><mi>x</mi></mrow></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mfrac><mn>9</mn><mn>5</mn></mfrac></msubsup><mfenced><mrow><mn>5</mn><mo>+</mo><mi>x</mi><mo>+</mo><mfrac><mn>16</mn><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mn>9</mn><mn>5</mn></mfrac><mn>3</mn></msubsup><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced open="[" close="]"><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mn>16</mn><mi>ln</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow><mfrac><mn>9</mn><mn>5</mn></mfrac></msubsup><mo>+</mo><msubsup><mfenced open="[" close="]"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mfrac><mn>9</mn><mn>5</mn></mfrac><mn>3</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>18</mn><mo>+</mo><mn>16</mn><mi>ln</mi><mfenced><mfrac><mn>8</mn><mn>15</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>1</mn></msub><mo>=</mo><mn>18</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>2</mn></msub><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#945;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#945;</mi><mn>2</mn></msub><mo>=</mo><mn>34</mn></math></p>

</details>

---

### Q17. JEE Main 2022 (24 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><mo>=</mo><mi>sin</mi><mi>&#952;</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>t</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><mi>d</mi><mi>&#952;</mi></mrow></mfenced></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><mo>=</mo><mi>sin</mi><mi>&#952;</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>t</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><mo>=</mo><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>sin</mi><mi>&#952;</mi><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>t</mi><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>,</mo><mo>&#160;&#160;</mo><mi mathvariant="normal">B</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>t</mi><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><mo>=</mo><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>A</mi><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>B</mi><mi>cos</mi><mi>&#952;</mi></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><mo>=</mo><mfenced><mrow><mi>A</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>B</mi><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mfenced><mrow><mi>A</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>sin</mi><mi>t</mi><mo>+</mo><mi>B</mi><mi>cos</mi><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced><mrow><mi>A</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mo>&#160;</mo><mi>sin</mi><mi>t</mi><mi>d</mi><mi>t</mi><mo>+</mo><mi>B</mi><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mo>&#160;</mo><mi>cos</mi><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>2</mn><mi>B</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>t</mi><mfenced><mrow><mfenced><mrow><mi>A</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>sin</mi><mi>t</mi><mo>+</mo><mi>B</mi><mi>cos</mi><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>B</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>t</mi><mfenced><mrow><mi>A</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>sin</mi><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>B</mi><mo>=</mo><mfenced><mrow><mi>A</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>t</mi><mi>sin</mi><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>B</mi><mo>=</mo><mfenced><mrow><mi>A</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>A</mi><mo>+</mo><mn>2</mn><mo>-</mo><mi>B</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p>After solving</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><mi>d</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mi>d</mi><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>sin</mi><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>cos</mi><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q18. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>,</mo></math> that satisfies the condition <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mi>&#960;</mi><mo>/</mo><mn>2</mn></mrow></msubsup><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>y</mi><mi>f</mi><mo>(</mo><mi>y</mi><mo>)</mo><mi mathvariant="normal">d</mi><mi>y</mi><mo>,</mo></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mi>sin</mi><mi>x</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>2</mn><mo>)</mo><mi>sin</mi><mi>x</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>(</mo><mi>&#960;</mi><mo>-</mo><mn>2</mn><mo>)</mo><mi>sin</mi><mi>x</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mo>(</mo><mi>&#960;</mi><mo>-</mo><mn>2</mn><mo>)</mo><mi>sin</mi><mi>x</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mo>(</mo><mi>&#960;</mi><mo>-</mo><mn>2</mn><mo>)</mo><mi>sin</mi><mi>x</mi></math>**

**Detailed Solution:**

<p>Given the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>sin</mi><mi>x</mi><mo>&#183;</mo><mi>cos</mi><mi>y</mi><mi>f</mi><mfenced><mi>y</mi></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>k</mi><mi>sin</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>=</mo><mi>y</mi><mo>+</mo><mi>k</mi><mi>sin</mi><mi>y</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>k</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>cos</mi><mi>y</mi><mi>f</mi><mfenced><mi>y</mi></mfenced><mi>d</mi><mi>y</mi></math></p><p>From equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>y</mi><mfenced><mrow><mi>y</mi><mo>+</mo><mi>k</mi><mi>sin</mi><mi>y</mi></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>y</mi><mi>cos</mi><mi>y</mi><mi>d</mi><mi>y</mi><mo>+</mo><mfrac><mi>k</mi><mn>2</mn></mfrac><mi>sin</mi><mi>x</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>sin</mi><mn>2</mn><mi>y</mi><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mfenced close="]" open="["><mrow><mi>y</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>cos</mi><mi>y</mi><mi>d</mi><mi>y</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mfenced close="}" open="{"><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mi>y</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>cos</mi><mi>y</mi><mi>d</mi><mi>y</mi></mrow></mfenced><mi>d</mi><mi>y</mi></mrow></mfenced><mo>+</mo><mfrac><mi>k</mi><mn>2</mn></mfrac><mi>sin</mi><mi>x</mi><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></msubsup><mi>sin</mi><mn>2</mn><mi>y</mi><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mfenced close="]" open="["><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mi>k</mi><mn>2</mn></mfrac><mi>sin</mi><mi>x</mi><mo>&#215;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mrow><mo>(</mo><mi>&#960;</mi><mo>-</mo><mn>2</mn><mo>)</mo><mi>sin</mi><mi>x</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mi>k</mi><mi>sin</mi><mi>x</mi></mrow><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>i</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>i</mi><mi>i</mi><mi>i</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">k</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mi mathvariant="normal">k</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">k</mi><mo>=</mo><mi>&#960;</mi><mo>-</mo><mn>2</mn></math></p><p>Hence,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mo>(</mo><mi>&#960;</mi><mo>-</mo><mn>2</mn><mo>)</mo><mi>sin</mi><mi>x</mi></math></p>

</details>

---

### Q19. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>J</mi><mrow><mi>n</mi><mo>,</mo><mi>m</mi></mrow></msub><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msubsup><mfrac><msup><mi>x</mi><mi>n</mi></msup><mrow><msup><mi>x</mi><mi>m</mi></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#8704;</mo><mi>n</mi><mo>&#62;</mo><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>&#8712;</mo><mi>N</mi><mo>.</mo></math> Consider a matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msub><mfenced close="]" open="["><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced><mrow><mn>3</mn><mo>&#215;</mo><mn>3</mn></mrow></msub></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><msub><mi mathvariant="normal">J</mi><mrow><mn>6</mn><mo>+</mo><mi>i</mi><mo>,</mo><mn>3</mn></mrow></msub><mo>-</mo><msub><mi mathvariant="normal">J</mi><mrow><mi>i</mi><mo>+</mo><mn>3</mn><mo>,</mo><mn>3</mn></mrow></msub></mtd><mtd><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mi>i</mi><mo>&#8804;</mo><mi>j</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>,</mo><mo>&#160;&#160;</mo><mi>i</mi><mo>&#62;</mo><mi>j</mi></mtd></mtr></mtable></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mo>adj</mo><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>15</mn><msup><mo>)</mo><mn>2</mn></msup><mo>&#215;</mo><msup><mn>2</mn><mn>34</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>15</mn><msup><mo>)</mo><mn>2</mn></msup><mo>&#215;</mo><msup><mn>2</mn><mn>42</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>105</mn><msup><mo>)</mo><mn>2</mn></msup><mo>&#215;</mo><msup><mn>2</mn><mn>36</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>105</mn><msup><mo>)</mo><mn>2</mn></msup><mo>&#215;</mo><msup><mn>2</mn><mn>38</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>105</mn><msup><mo>)</mo><mn>2</mn></msup><mo>&#215;</mo><msup><mn>2</mn><mn>38</mn></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><msub><mi>a</mi><mn>11</mn></msub></mtd><mtd><msub><mi>a</mi><mn>12</mn></msub></mtd><mtd><msub><mi>a</mi><mn>13</mn></msub></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msub><mi>a</mi><mn>22</mn></msub></mtd><mtd><msub><mi>a</mi><mn>23</mn></msub></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><msub><mi>a</mi><mn>33</mn></msub></mtd></mtr></mtable></mfenced><mo>&#8658;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><msub><mi>a</mi><mn>11</mn></msub><msub><mi>a</mi><mn>22</mn></msub><msub><mi>a</mi><mn>33</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi mathvariant="normal">A</mi><mo>|</mo><mo>=</mo><mfenced><mrow><msub><mi mathvariant="normal">J</mi><mrow><mn>7</mn><mo>,</mo><mn>3</mn></mrow></msub><mo>-</mo><msub><mi mathvariant="normal">J</mi><mrow><mn>4</mn><mo>,</mo><mn>3</mn></mrow></msub></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msub><mi mathvariant="normal">J</mi><mrow><mn>8</mn><mo>,</mo><mn>3</mn></mrow></msub><mo>-</mo><msub><mi mathvariant="normal">J</mi><mrow><mn>5</mn><mo>,</mo><mn>3</mn></mrow></msub></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><msub><mi mathvariant="normal">J</mi><mrow><mn>9</mn><mo>,</mo><mn>3</mn></mrow></msub><mo>-</mo><msub><mi mathvariant="normal">J</mi><mrow><mn>6</mn><mo>,</mo><mn>3</mn></mrow></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>7</mn></msup><mo>-</mo><msup><mi>x</mi><mn>4</mn></msup></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi><mo>&#183;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>8</mn></msup><mo>-</mo><msup><mi>x</mi><mn>5</mn></msup></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi><mo>&#183;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msubsup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>9</mn></msup><mo>-</mo><msup><mi>x</mi><mn>6</mn></msup></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msubsup><msup><mi>x</mi><mn>4</mn></msup><mi>d</mi><mi>x</mi><mo>&#183;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msubsup><msup><mi>x</mi><mn>5</mn></msup><mi>d</mi><mi>x</mi><mo>&#183;</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msubsup><msup><mi>x</mi><mn>6</mn></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mn>210</mn><mo>)</mo><mo>&#183;</mo><mo>(</mo><mn>2</mn><msup><mo>)</mo><mn>18</mn></msup></mrow></mfrac></math></p><p>Now</p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mo>adj</mo><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mo>=</mo><msup><mfenced open="|" close="|"><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mrow><mo>|</mo><mi>A</mi><msup><mo>|</mo><mn>2</mn></msup></mrow></mfrac><mo>=</mo><msup><mfenced><mrow><mo>(</mo><mn>210</mn><mo>)</mo><mo>&#183;</mo><mfenced><msup><mn>2</mn><mn>18</mn></msup></mfenced></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mo>(</mo><mn>105</mn><msup><mo>)</mo><mn>2</mn></msup><mo>&#183;</mo><mo>(</mo><mn>2</mn><msup><mo>)</mo><mn>38</mn></msup></math>

</details>

---

### Q20. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>f</mi><mo>:</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>)</mo><mo>&#8594;</mo><mi>R</mi></math> be a continuous function. If <math><mrow><msubsup><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></msubsup><mrow><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mrow><mi>&#160;</mi><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mi>x</mi><mo>,</mo></math> then <math><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><msqrt><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>s</mi><mi>i</mi><mi>n</mi><mi>x</mi></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mi>&#160;</mi><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow><mi>&#160;</mi><mi>x</mi><mo>.</mo></math>

Differentiating w.r.t <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> both the sides,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mrow><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mrow></mfenced><mo>&#183;</mo><mi>cos</mi><mo>&#8289;</mo><mi>x</mi><mo>=</mo><mi>&#160;</mi><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math>

Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mi>&#960;</mi><mi>&#160;</mi></mrow><mn>3</mn></mfrac></math>.

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mi>f</mi><mi>&#160;</mi><mfenced separators="|"><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt></math>.

</details>

---

### Q21. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>4</mn><mo>+</mo><mi>x</mi></mrow></mfenced></math>, for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>0</mn><mn>2</mn></munderover><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>5</mn></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8747;</mo><mn>10</mn><mn>50</mn></munderover><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>125</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mo>(</mo><mn>4</mn><mo>+</mo><mi>x</mi><mo>)</mo></math>

Then curve is symmetric about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math>

<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi></math> The curve is periodic with period <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

Given <math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>2</mn></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>5</mn></mrow></mrow></math>

<math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>4</mn></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow><mo>=</mo><mn>2</mn><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>2</mn></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow><mo>=</mo><mn>10</mn></math>

<math><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>10</mn></mrow><mrow><mn>50</mn></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow><mo>=</mo><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>2</mn><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced><mo>+</mo><mn>2</mn></mrow><mrow><mn>12</mn><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced><mo>+</mo><mn>2</mn></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math>

<math><mo>=</mo><mfenced separators="|"><mrow><mn>12</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mrow><munderover><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>4</mn></mrow></munderover><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math>

<math><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>100</mn></math>

</details>

---

### Q22. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let, the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfrac><msup><mi>e</mi><mi>t</mi></msup><mi>t</mi></mfrac><mi>d</mi><mi>t</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> then the value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfrac><msup><mi>e</mi><mi>t</mi></msup><mrow><mi>t</mi><mo>+</mo><mi>a</mi></mrow></mfrac><mi>d</mi><mi>t</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>a</mi></msup><mfenced open="[" close="]"><mrow><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>F</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow></mfenced></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>a</mi></mrow></msup><mfenced open="[" close="]"><mrow><mi>F</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mi>F</mi><mfenced><mi>a</mi></mfenced></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>a</mi></msup><mfenced open="[" close="]"><mrow><mi>F</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mi>F</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow></mfenced></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>a</mi></mrow></msup><mfenced open="[" close="]"><mrow><mi>F</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mi>F</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow></mfenced></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>a</mi></mrow></msup><mfenced open="[" close="]"><mrow><mi>F</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mi>F</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow></mfenced></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfrac><msup><mi>e</mi><mi>t</mi></msup><mi>t</mi></mfrac><mi>d</mi><mi>t</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><mfrac><msup><mi>e</mi><mi>t</mi></msup><mrow><mi>t</mi><mo>+</mo><mi>a</mi></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>+</mo><mi>a</mi><mo>=</mo><mi>y</mi></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mi>t</mi><mo>=</mo><mi>d</mi><mi>y</mi></math>

Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>1</mn><mo>&#160;&#8658;</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mi>x</mi><mo>&#160;&#8658;</mo><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;&#160;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></msubsup><mfrac><msup><mi>e</mi><mrow><mi>y</mi><mo>-</mo><mi>a</mi></mrow></msup><mi>y</mi></mfrac><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>a</mi></mrow></msup><msubsup><mo>&#8747;</mo><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></msubsup><mfrac><msup><mi>e</mi><mi>y</mi></msup><mi>y</mi></mfrac><mi>d</mi><mi>y</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>a</mi></mrow></msup><msubsup><mo>&#8747;</mo><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></msubsup><mfrac><msup><mi>e</mi><mi>t</mi></msup><mi>t</mi></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>a</mi></mrow></msup><mfenced open="[" close="]"><mrow><msubsup><mo>&#8747;</mo><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow></msubsup><mfrac><msup><mi>e</mi><mi>t</mi></msup><mi>t</mi></mfrac><mi>d</mi><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></msubsup><mfrac><msup><mi>e</mi><mi>t</mi></msup><mi>t</mi></mfrac><mi>d</mi><mi>t</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow></msubsup><mfrac><msup><mi>e</mi><mi>t</mi></msup><mi>t</mi></mfrac><mi>d</mi><mi>t</mi></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mi>b</mi><mi>c</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>c</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>&#60;</mo><mi>c</mi><mo>&#60;</mo><mi>b</mi><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>a</mi></mrow></msup><mfenced open="[" close="]"><mrow><msubsup><mo>&#8747;</mo><mn>1</mn><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></msubsup><mfrac><msup><mi>e</mi><mi>t</mi></msup><mi>t</mi></mfrac><mi>d</mi><mi>t</mi><mo>-</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow></msubsup><mfrac><msup><mi>e</mi><mi>t</mi></msup><mi>t</mi></mfrac><mi>d</mi><mi>t</mi></mrow></mfenced></math></p><p>Using, the given relation, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>a</mi></mrow></msup><mfenced open="[" close="]"><mrow><mi>F</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mo>-</mo><mi>F</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow></mfenced></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q23. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `2`

Let $p(x)$ be a function defined on $R$ such that $p^{\prime}(x)=p^{\prime}(1-x)$, for all $x \in[0,1], p(0)=1$ and $p(1)=41$. Then $\int_0^1 p(x) d x$ equals

**Options:**

- **(A)** 21
- **(B)** 41
- **(C)** 42
- **(D)** $\sqrt{41}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 21**

**Detailed Solution:**

$\mathrm{p}^{\prime}(\mathrm{x})=\mathrm{p}^{\prime}(1-\mathrm{x})$
$\Rightarrow \mathrm{p}(\mathrm{x})=-\mathrm{p}(1-\mathrm{x})+\mathrm{c}$
at $x=0$
$\mathrm{p}(0)=-\mathrm{p}(1)+\mathrm{c} \quad \Rightarrow 42=\mathrm{c}$
now $\mathrm{p}(\mathrm{x})=-\mathrm{p}(1-\mathrm{x})+42$
$\Rightarrow \mathrm{p}(\mathrm{x})+\mathrm{p}(1-\mathrm{x})=42$
$\mathrm{I}=\int_0^1 \mathrm{p}(\mathrm{x}) \mathrm{dx}=\int_0^1 \mathrm{p}(1-\mathrm{x}) \mathrm{dx}$
$2 \mathrm{I}=\int_0^1(42) \mathrm{dx} \quad \Rightarrow \mathrm{I}=21$

</details>

---

### Q24. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{I}=\int_0^1 \frac{\sin \mathrm{x}}{\sqrt{\mathrm{x}}} \mathrm{dx}$ and $\mathrm{J}=\int_0^1 \frac{\cos \mathrm{x}}{\sqrt{\mathrm{x}}} \mathrm{dx}$. Then which one of the following is true?

**Options:**

- **(A)** $\mathrm{I}>\frac{2}{3}$ and $\mathrm{J}>2$
- **(B)** $I < \frac{2}{3}$ and $J < 2$
- **(C)** $\mathrm{I} < \frac{2}{3}$ and $\mathrm{J}>2$
- **(D)** $I>\frac{2}{3}$ and $\mathrm{J} < 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $I < \frac{2}{3}$ and $J < 2$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{I}=\int_0^1 \frac{\sin x}{\sqrt{x}} \mathrm{dx} < \int_0^1 \frac{\mathrm{x}}{\sqrt{\mathrm{x}}} \mathrm{dx}=\int_0^1 \sqrt{\mathrm{x}} \mathrm{dx}=\left.\frac{2}{3} \mathrm{x}^{3 / 2}\right|_0 ^1=\frac{2}{3} \\
& \Rightarrow \mathrm{I} < \frac{2}{3} \\
& \mathrm{~J}=\int_0^1 \frac{\cos x}{\sqrt{\mathrm{x}}} \mathrm{dx} < \int_0^1 \frac{1}{\sqrt{\mathrm{x}}} \mathrm{dx}=\left.2 \sqrt{\mathrm{x}}\right|_0 ^1=2 \\
& \therefore \mathrm{J} \leq 2 .
\end{aligned}
$$

</details>

---

### Q25. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{I}_1=\int_0^1 2^{x^2} d x, I_2=\int_0^1 2^{x^3} d x, I_3=\int_1^2 2^{x^2} d x$ and $I_4=\int_1^2 2^{x^3} d x$ then

**Options:**

- **(A)** $I_2>I_1$
- **(B)** $I_1>I_2$
- **(C)** $I_3=I_4$
- **(D)** $I_3>I_4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $I_1>I_2$**

**Detailed Solution:**

$$
\begin{aligned}
& l_1=\int_0^1 2^{x^2} d x, l_2=\int_0^1 2^{x^3} d x, I_3=\int_0^1 2^{x^2} d x, I_4=\int_0^1 2^{x^3} d x \\
& \forall 0 < x < 1, x^2>x^3 \\
& \Rightarrow \int_0^1 2^{x^2} d x>\int_0^1 2^{x^3} d x \\
& \Rightarrow I_1>I_2 .
\end{aligned}
$$

</details>

---

### Q26. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `3`

Let $\frac{d}{d x} F(x)=\left(\frac{e^{\text {sinx }}}{x}\right) x>0$. If $\int_1^4 \frac{3}{x} e^{\text {sin }^3} d x=F(k)-F(1)$ then one of the possible values of $k$, is

**Options:**

- **(A)** 64
- **(B)** 15
- **(C)** 16
- **(D)** 63

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 64**

**Detailed Solution:**

$$
\frac{d}{d x} F(x)=\frac{e^{\sin x}}{x} \text { or } \int_1^4 \frac{3}{x} e^{\sin x^3} d x=\int_1^4 \frac{3 x^2}{x^3} e^{\sin x^3} d x
$$
Let $\mathrm{x}^3=\mathrm{t}, 3 \mathrm{x}^2 \mathrm{dx}=\mathrm{dt}$
when $x=1, t=1 \& x-4, t=64$
$$
\begin{aligned}
& \mathrm{F}(\mathrm{t})=\int_1^{64} \frac{\mathrm{e}^{\sin t}}{\mathrm{t}} \mathrm{dt}=\int_1^{64} \mathrm{~F}(\mathrm{t}) \mathrm{dt}=\mathrm{F}(64)-\mathrm{F}(1) \\
& \mathrm{K}=64
\end{aligned}
$$

</details>

---

### Q27. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

If $y=f(x)$ makes $+v e$ intercept of 2 and 0 unit on $x$ and $y$ axes and encloses an area of $3 / 4$ square unit with the axes then $\int_0^2 x f^{\prime}(x) d x ~~is$

**Options:**

- **(A)** 3/2
- **(B)** 1
- **(C)** 5/4
- **(D)** -3/4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -3/4**

**Detailed Solution:**

We have $\int_0^2 f(x) d x=\frac{3}{4} ;$ Now, $\int_0^2 x f^{\prime}(x) d x=x \int_0^2 f^{\prime}(x) d x-\int_0^2 f(x) d x$
$=[x f(x)]_0^2-\frac{3}{4}=2 f(2)-\frac{3}{4}=0-\frac{3}{4}(\because f(2)=0)=-\frac{3}{4}$

</details>

---

