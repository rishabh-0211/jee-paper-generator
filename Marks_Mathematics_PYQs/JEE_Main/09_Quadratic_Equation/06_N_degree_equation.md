# JEE Main Mathematics - Quadratic Equation

## Topic 6: N degree equation

**Total Questions:** 25

---

### Q1. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{S}=\left\{x^{3}+a x^{2}+b x+c: a, b, c \in \mathrm{~N}\right.$ and $\left.a, b, c \leq 20\right\}$ be a set of polynomials. Then the number of polynomials in S, which are divisible by $x^{2}+2$, is

**Options:**

- **(A)** 10
- **(B)** 20
- **(C)** 6
- **(D)** 120

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 10**

**Detailed Solution:**

If $x^2 + 2$ divides $x^3 + ax^2 + bx + c$, write $x^3 + ax^2 + bx + c = (x^2 + 2)(x + k)$.
Expanding: $x^3 + kx^2 + 2x + 2k$.
Comparing coefficients: $a = k$, $b = 2$, $c = 2a$.
Constraints: $a \in \mathbb{N}$, $a \leq 20$, and $c = 2a \leq 20 \Rightarrow a \leq 10$.
So $a \in \{1, 2, 3, ..., 10\}$, giving 10 polynomials.

</details>

---

### Q2. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The smallest positive integral value of $a$, for which all the roots of $x^{4}-a x^{2}+9=0$ are real and distinct, is equal to

**Options:**

- **(A)** 4
- **(B)** 9
- **(C)** 3
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 7**

**Detailed Solution:**

Let $t = x^2$, so the equation becomes $t^2 - at + 9 = 0$.
For all four roots of the original equation to be real and distinct, both roots of this quadratic must be positive and distinct.
Discriminant $> 0$: $a^2 - 36 > 0 \Rightarrow |a| > 6$. Since $a > 0$, we need $a > 6$.
Product of roots $= 9 > 0$ and sum of roots $= a > 0$, so both roots are positive.
The smallest positive integer satisfying $a > 6$ is $a = 7$.

</details>

---

### Q3. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The sum of all the real solutions of the equation 
 $\log _{(x+3)}\left(6 x^{2}+28 x+30\right)=5-2 \log _{(6 x+10)}\left(x^{2}+6 x+9\right)$ is equal to

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** 0
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

Note $6x^2+28x+30 = 2(3x+5)(x+3)$,
$x^2+6x+9 = (x+3)^2$,
$6x+10 = 2(3x+5)$.
Let $a = \log_{(x+3)}[2(3x+5)]$. Then LHS $= a + 1$ and $\log_{2(3x+5)}(x+3)^2 = \frac{2}{a}$.
Equation becomes $a + 1 = 5 - \frac{4}{a}$, i.e., $a^2 - 4a + 4 = 0 \Rightarrow a = 2$.
So $\log_{(x+3)}[2(3x+5)] = 2 \Rightarrow (x+3)^2 = 6x+10 \Rightarrow x^2 = 1 \Rightarrow x = 1$ or $x = -1$.
Both satisfy domain conditions (bases $> 0$, $\neq 1$; arguments $> 0$).
Sum $= 1 + (-1) = 0$.

</details>

---

### Q4. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\alpha$ and $\beta(\alpha<\beta)$ are the roots of the equation $(-2+\sqrt{3})(|\sqrt{x}-3|)+(x-6 \sqrt{x})+(9-2 \sqrt{3})=0, x \geqslant 0$, then $\sqrt{\frac{\beta}{\alpha}}+\sqrt{\alpha \beta}$ is equal to :

**Options:**

- **(A)** 8
- **(B)** 11
- **(C)** 9
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 10**

**Detailed Solution:**

Let $t = \sqrt{x} \geq 0$. The equation becomes $(-2+\sqrt{3})|t-3| + (t^2 - 6t) + (9 - 2\sqrt{3}) = 0$.
Since $t^2 - 6t + 9 = (t-3)^2$, we get $(t-3)^2 + (\sqrt{3}-2)|t-3| - 2\sqrt{3} = 0$.
Let $u = |t-3| \geq 0$: $u^2 + (\sqrt{3}-2)u - 2\sqrt{3} = 0$.
Discriminant $= (\sqrt{3}-2)^2 + 8\sqrt{3} = 7 + 4\sqrt{3} = (2+\sqrt{3})^2$.
$u = \frac{(2-\sqrt{3}) \pm (2+\sqrt{3})}{2}$, giving $u = 2$ or $u = -\sqrt{3}$ (rejected).
$|t-3| = 2 \Rightarrow t = 5$ or $t = 1$, so $x = 25$ or $x = 1$.
$\alpha = 1, \beta = 25$.
$\sqrt{\beta/\alpha} + \sqrt{\alpha\beta} = \sqrt{25} + \sqrt{25} = 5 + 5 = 10$.

</details>

---

### Q5. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A building construction work can be completed by two masons A and B together in 22.5 days. Mason A alone can complete the construction work in 24 days less than mason B alone. Then mason A alone will complete the construction work in :

**Options:**

- **(A)** 30 days
- **(B)** 36 days
- **(C)** 24 days
- **(D)** 42 days

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 36 days**

**Detailed Solution:**

Let A take $a$ days and B take $a + 24$ days.
Together: $\frac{1}{a} + \frac{1}{a+24} = \frac{1}{22.5} = \frac{2}{45}$.
$\frac{2a+24}{a(a+24)} = \frac{2}{45}$
$45(2a+24) = 2a(a+24)$
$90a + 1080 = 2a^2 + 48a$
$a^2 - 21a - 540 = 0$
$(a-36)(a+15) = 0 \Rightarrow a = 36$.
Mason A alone completes the work in 36 days.

</details>

---

### Q6. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of solutions of the equation \(\left(\frac{9}{x}-\frac{9}{\sqrt{x}}+2\right)\left(\frac{2}{x}-\frac{7}{\sqrt{x}}+3\right)=0\) is:

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** 1
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

Consider $\frac{1}{\sqrt{\mathrm{x}}}=\alpha \quad \mathrm{x}>0$
$\begin{aligned}
& \left\{9 \alpha^2-9 \alpha+2\right\}\left\{2 \alpha^2-7 \alpha+3\right\}=0 \\
& (3 \alpha-2)(3 \alpha-1)(\alpha-3)(2 \alpha-1)=0 \\
& \alpha=\frac{1}{3}, \frac{1}{2}, \frac{2}{3}, 3 \\
& x=9,4, \frac{9}{4}, \frac{1}{9}
\end{aligned}$

So, no. of solutions $=4$

</details>

---

### Q7. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The product of all the rational roots of the equation $\left(x^2-9 x+11\right)^2-(x-4)(x-5)=3$, is equal to

**Options:**

- **(A)** $14$
- **(B)** $21$
- **(C)** $28$
- **(D)** $7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $14$**

**Detailed Solution:**

$\begin{aligned}
& \left(x^2-9 x+11\right)^2-(x-4)(x-5)=3 \\
& \left(x^2-9 x+11\right)^2-\left(x^2-9 x+20\right)=3
\end{aligned}$
Let $x^2-9 x+11=t$
$\begin{aligned}
& t^2-(t+9)=3 \\
& \Rightarrow t^2-t-12=0 \\
& \Rightarrow t^2-4 t+3 t-12=0 \\
& \Rightarrow t(t-4)+3(t-4)=0 \\
& \Rightarrow t=4 \text { or }-3 \\
& x^2-9 x+11=4 \\
& x^2-9 x+7=0
\end{aligned}$
Here, we will get irrational roots
$\begin{aligned}
& x^2-9 x+11=-3 \\
& x^2-9 x+14=0 \\
& x^2-7 x-2 x+14=0 \\
& \Rightarrow x=7,2 \\
& \Rightarrow \text { Product of all rational roots }=14
\end{aligned}$

</details>

---

### Q8. JEE Main 2024 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $x_1, x_2, x_3, x_4$ be the solution of the equation $4 x^4+8 x^3-17 x^2-12 x+9=0$ and $\left(4+x_1^2\right)\left(4+x_2^2\right)\left(4+x_3^2\right)\left(4+x_4^2\right)=\frac{125}{16} m$. Then the value of $m$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **221**

**Detailed Solution:**

$\begin{aligned}
& 4 x^4+8 x^3-17 x^2-12 x+9 \\
& =4\left(x-x_1\right)\left(x-x_2\right)\left(x-x_3\right)\left(x-x_4\right)
\end{aligned}$
Put $x=2 i \&-2 i$
$\begin{aligned}
& 64-64 i+68-24 i+9=\left(2 i-x_1\right)\left(2 i-x_2\right)\left(2 i-x_3\right) \\
& \left(2 i-x_4\right) \\
& =141-88 i ....(1)\\
& 64+64 i+68+24 i+9=4\left(-2 i-x_1\right)\left(-2 i-x_2\right)(-2 i \\
& \left.-x_3\right)\left(-2 i-x_4\right) \\
& =141+88 i....(2)
\end{aligned}$
$\begin{aligned}
& \frac{125}{16} \mathrm{~m}=\frac{141^2+88^2}{16} \\
& \mathrm{~m}=221
\end{aligned}$

</details>

---

### Q9. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>x</mi><mo>∈</mo><mi>R</mi><mo>:</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mi>x</mi></msup><mo>+</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>−</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mi>x</mi></msup><mo>=</mo><mn>10</mn></mrow></mfenced></math>. Then the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mi>x</mi></msup><mo>+</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mi>x</mi></msup><mo>=</mo><mn>10</mn></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mi>x</mi></msup><mo>=</mo><mi>t</mi><mo>⇒</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mi>x</mi></msup><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mi>x</mi></msup><mo>+</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mi>x</mi></msup><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>t</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>t</mi><mo>=</mo><mn>5</mn><mo>±</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>t</mi><mo>=</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>,</mo><mo> </mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup></math></p><p>Now, taking <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mi>x</mi></msup><mo>=</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>And equating <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mi>x</mi></msup><mo>=</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p>Hence, the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p>

</details>

---

### Q10. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of solutions, of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup><mo>−</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>−</mo><mi>sin</mi><mi>x</mi></mrow></msup><mo>=</mo><mn>2</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** more than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>t</mi><mo>-</mo><mfrac><mn>2</mn><mi>t</mi></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>t</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>t</mi><mo>=</mo><mn>1</mn><mo>±</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>t</mi><mo>≈</mo><mn>2</mn><mo>.</mo><mn>73</mn><mo>,</mo><mo> </mo><mo>-</mo><mn>0</mn><mo>.</mo><mn>73</mn><mfenced><mtext>not possible</mtext></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>t</mi><mo>≈</mo><mn>2</mn><mo>.</mo><mn>73</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup><mo>≈</mo><mn>2</mn><mo>.</mo><mn>73</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>x</mi><mo>≈</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>2</mn><mo>.</mo><mn>73</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>x</mi><mo>&gt;</mo><mn>1</mn><mo>→</mo><mtext>Not possible</mtext></math></p><p>So no solutions will be possible for the given equation.</p>

</details>

---

### Q11. JEE Main 2024 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

The number of real solutions of the equation \(x\left(x^2+3|x|+5|x-1|+6|x-2|\right)=0\) is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>|</mo><mi>x</mi><mo>|</mo><mo>+</mo><mn>5</mn><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>+</mo><mn>6</mn><mo>|</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>|</mo></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo> </mo><mtext>or</mtext><mo> </mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>|</mo><mi>x</mi><mo>|</mo><mo>+</mo><mn>5</mn><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>+</mo><mn>6</mn><mo>|</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>|</mo><mo>=</mo><mn>0</mn></math></p><p>We know that sum of all positive terms can never be zero,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>|</mo><mi>x</mi><mo>|</mo><mo>+</mo><mn>5</mn><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>+</mo><mn>6</mn><mo>|</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>|</mo></math> can never be zero for any value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>,</p><p>So there is no value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> which satisfies the above equation
Hence, only solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, i.e. number of solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> .</p></blockquote>

</details>

---

### Q12. JEE Main 2023 (11 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

The number of points, where the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>e</mi><mrow><mn>8</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mn>6</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>3</mn><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math> cuts <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis, is equal to............

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>8</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mn>6</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>3</mn><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>3</mn><mo>-</mo><mfrac><mn>1</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup></mfrac><mo>+</mo><mn>2</mn><mo>-</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mfrac></mrow></mfenced><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mfrac></mrow></mfenced><mo>=</mo><mn>3</mn></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mfrac></mrow></mfenced><mo>=</mo><mi>t</mi></math></p><p>So, the equation becomes</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>21</mn></msqrt></mrow><mn>2</mn></mfrac></math>, ignoring negative sign as exponential function are positive,</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>21</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>21</mn></msqrt></mrow><mn>2</mn></mfrac><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> which is quadratic equation in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></math> with upward parabola, </p><p>Now by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>M</mi><mo>&#8805;</mo><mi>G</mi><mo>.</mo><mi>M</mi></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mfrac><mo>&#8805;</mo><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>21</mn></msqrt></mrow><mn>2</mn></mfrac><mo>&#62;</mo><mn>2</mn></math>, hence it will cut at two distinct point,</p><p>Hence, there will be two solution.</p>

</details>

---

### Q13. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi></math> be the three  roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mi>&#947;</mi><mo>=</mo><mn>1</mn><mo>=</mo><mo>-</mo><mi>&#945;</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mi>c</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>&#945;</mi><mn>3</mn></msup><mo>-</mo><mn>6</mn><msup><mi>&#946;</mi><mn>3</mn></msup><mo>-</mo><mn>8</mn><msup><mi>&#947;</mi><mn>3</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>155</mn><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>169</mn><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi></math></p><p>Also given that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mi>&#947;</mi><mo>=</mo><mn>1</mn><mo>=</mo><mo>-</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math></p><p>Now let us apply the relation between the roots of the cubic equation with the coefficients.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>0</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>ii</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mi>&#946;</mi><mi>&#947;</mi><mo>=</mo><mo>-</mo><mi>c</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>iii</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>c</mi><mo>=</mo><mn>1</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>iv</mi><mo>)</mo></math></p><p>On substituting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> in eq <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>1</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">v</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>+</mo><mi>&#946;</mi><mi>&#947;</mi><mo>+</mo><mi>&#947;</mi><mi>&#945;</mi><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mo>+</mo><mi>&#946;</mi><mi>&#947;</mi><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>b</mi><mo>=</mo><mn>0</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>vi</mi><mo>)</mo></math></p><p>Hence, equation will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Whose roots will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mi>&#969;</mi><mo>,</mo><mo>&#160;</mo><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>&#969;</mi><mo>+</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mi>&#969;</mi><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>vii</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#946;</mi><mn>3</mn></msup><mo>=</mo><mo>-</mo><msup><mi>&#969;</mi><mn>3</mn></msup><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#947;</mi><mn>3</mn></msup><mo>=</mo><mo>-</mo><msup><mi>&#969;</mi><mn>6</mn></msup><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Hence the value of </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mi>c</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>&#945;</mi><mn>3</mn></msup><mo>-</mo><mn>6</mn><msup><mi>&#946;</mi><mn>3</mn></msup><mo>-</mo><mn>8</mn><msup><mi>&#947;</mi><mn>3</mn></msup></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>19</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q14. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>x</mi><mo>:</mo><mi>x</mi><mo>&#8712;</mo><mi>&#8477;</mi><mtext>&#160;and&#160;</mtext><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></msup><mo>+</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><mn>10</mn></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>S</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>x</mi><mo>:</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></msup><mo>+</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><mn>10</mn></mrow></mfenced></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>=</mo><mfrac><mrow><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></msup><mo>+</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></msup><mo>+</mo><msup><mfenced><mfrac><mn>1</mn><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><mn>10</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><mi>u</mi></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>+</mo><mfrac><mn>1</mn><mi>u</mi></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>u</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>u</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>u</mi><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#177;</mo><msqrt><mn>100</mn><mo>-</mo><mn>4</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>u</mi><mo>=</mo><mn>5</mn><mo>&#177;</mo><msqrt><mn>24</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>u</mi><mo>=</mo><mn>5</mn><mo>&#177;</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>u</mi><mo>=</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>&#177;</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>&#177;</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><msup><mfenced><mfrac><mn>1</mn><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><msqrt><mn>6</mn></msqrt><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><msqrt><mn>2</mn></msqrt></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><msqrt><mn>6</mn></msqrt><mo>,</mo><mo>&#160;</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mo>&#160;</mo><mo>-</mo><msqrt><mn>6</mn></msqrt><mo>,</mo><mo>&#160;</mo><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>S</mi></mfenced><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q15. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>8</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>13</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>8</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> has :

**Options:**

- **(A)** four solutions two of which are negative
- **(B)** two solutions and both are negative
- **(C)** no solution
- **(D)** two solutions and only one of them is negative

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) two solutions and both are negative**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>8</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>13</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>8</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>t</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>8</mn><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>13</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>t</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Now divide complete equation by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>8</mn><mfenced><mrow><mi>t</mi><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mo>+</mo><mn>13</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>t</mi><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>8</mn><mfenced><mrow><mi>t</mi><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mo>+</mo><mn>15</mn><mo>=</mo><mn>0</mn></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>=</mo><mi>z</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>z</mi><mo>+</mo><mn>15</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>5</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>=</mo><mo>-</mo><mn>3</mn></math>  or   <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>=</mo><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>t</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>  or   <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>t</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mo>&#177;</mo><msqrt><mn>13</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>5</mn><mo>&#177;</mo><msqrt><mn>29</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mo>+</mo><msqrt><mn>13</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>5</mn><mo>+</mo><msqrt><mn>29</mn></msqrt></mrow><mn>2</mn></mfrac><mo>=</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></math> (rejecting negative values as exponential is positive function)</p><p>And both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>3</mn><mo>+</mo><msqrt><mn>13</mn></msqrt></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>5</mn><mo>+</mo><msqrt><mn>29</mn></msqrt></mrow><mn>2</mn></mfrac><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>ln</mi><mfenced><mi>&#945;</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>ln</mi><mfenced><mi>&#946;</mi></mfenced></math> are both negative,</p><p>Hence, there are two solution and both are negative.</p>

</details>

---

### Q16. JEE Main 2023 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>1</mn></msub><mo>,</mo><msub><mi>&#945;</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>&#945;</mi><mn>7</mn></msub></math><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>1</mn></msub><mo>,</mo><msub><mi>&#945;</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>&#945;</mi><mn>7</mn></msub></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>5</mn></msup><mo>-</mo><mn>13</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>15</mn><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>1</mn></msub></mfenced><mo>&#8805;</mo><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>2</mn></msub></mfenced><mo>&#8805;</mo><mo>&#8230;</mo><mo>&#8805;</mo><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>7</mn></msub></mfenced></math>.
Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>1</mn></msub><msub><mi>&#945;</mi><mn>2</mn></msub><mo>-</mo><msub><mi>&#945;</mi><mn>3</mn></msub><msub><mi>&#945;</mi><mn>4</mn></msub><mo>+</mo><msub><mi>&#945;</mi><mn>5</mn></msub><msub><mi>&#945;</mi><mn>6</mn></msub></math> is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>5</mn></msup><mo>-</mo><mn>13</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>15</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>6</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>13</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> is one of the root.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>6</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>13</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>t</mi></math>, then we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>13</mn><mi>t</mi><mo>-</mo><mn>15</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>t</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>t</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>t</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>t</mi><mo>=</mo><mo>-</mo><mn>5</mn></math></p><p>Now we are getting </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mo>,</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><msqrt><mn>3</mn></msqrt><mo>,</mo><mo>&#160;</mo><mo>&#177;</mo><mi>i</mi><mo>,</mo><mo>&#177;</mo><msqrt><mn>5</mn></msqrt><mi>i</mi></math></p><p>From the given condition <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>1</mn></msub></mfenced><mo>&#8805;</mo><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>2</mn></msub></mfenced><mo>&#8805;</mo><mo>&#8230;</mo><mo>.</mo><mo>&#8805;</mo><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>7</mn></msub></mfenced></math></p><p>We can clearly say that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>7</mn></msub></mfenced><mo>=</mo><mn>0</mn></math> and</p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>6</mn></msub></mfenced><mo>=</mo><msqrt><mn>5</mn></msqrt><mo>=</mo><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>5</mn></msub></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>4</mn></msub></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>=</mo><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>3</mn></msub></mfenced></math> and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>1</mn><mo>=</mo><mfenced close="|" open="|"><msub><mi>&#945;</mi><mn>1</mn></msub></mfenced></math></p><p>So we can have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>1</mn></msub><mo>=</mo><msqrt><mn>5</mn></msqrt><mi>i</mi><mo>,</mo><mo>&#160;</mo><msub><mi>&#945;</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><msqrt><mn>5</mn></msqrt><mi>i</mi><mo>,</mo><mo>&#160;</mo><msub><mi>&#945;</mi><mn>3</mn></msub><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>4</mn></msub><mo>=</mo><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>,</mo><mo>&#160;</mo><msub><mi>&#945;</mi><mn>5</mn></msub><mo>=</mo><mi>i</mi><mo>,</mo><mo>&#160;</mo><msub><mi>&#945;</mi><mn>6</mn></msub><mo>=</mo><mo>-</mo><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>7</mn></msub><mo>=</mo><mn>0</mn></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>1</mn></msub><msub><mi>&#945;</mi><mn>2</mn></msub><mo>-</mo><msub><mi>&#945;</mi><mn>3</mn></msub><msub><mi>&#945;</mi><mn>4</mn></msub><mo>+</mo><msub><mi>&#945;</mi><mn>5</mn></msub><msub><mi>&#945;</mi><mn>6</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q17. JEE Main 2023 (25 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>&#945;</mi><mo>:</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msup><mn>9</mn><mrow><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>4</mn></mrow></msup><mo>+</mo><mn>13</mn></mrow></mfenced><mo>-</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>&#183;</mo><msup><mn>3</mn><mrow><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>4</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn></mrow></mfenced><mo>.</mo></math> Then the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> for which the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mfenced><mrow><munder><mo>&#8721;</mo><mrow><mi>&#945;</mi><mo>&#8712;</mo><mi>s</mi></mrow></munder><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup><mi mathvariant="normal">x</mi><mo>+</mo><munder><mo>&#8721;</mo><mrow><mi>a</mi><mo>&#8712;</mo><mi>s</mi></mrow></munder><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mi>&#946;</mi><mo>=</mo><mn>0</mn></math> has real roots, is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msup><mn>9</mn><mrow><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>4</mn></mrow></msup><mo>+</mo><mn>13</mn></mrow></mfenced><mo>-</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msup><mn>3</mn><mrow><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>4</mn></mrow></msup><mo>&#183;</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><mi>t</mi></math>, so the equation becomes,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>13</mn></mrow></mfenced><mo>-</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mfrac><mrow><mn>5</mn><mi>t</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mn>2</mn></msub><mfrac><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>13</mn></mrow></mfenced><mfenced><mrow><mstyle displaystyle="true"><mfrac><mrow><mn>5</mn><mi>t</mi></mrow><mn>2</mn></mfrac></mstyle><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>13</mn></mrow></mfenced><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>5</mn><mi>t</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mstyle></mfenced></mfrac><mo>=</mo><msup><mn>2</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>13</mn><mo>=</mo><mn>10</mn><mi>t</mi><mo>+</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>t</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mn>9</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><mn>1</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mrow><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><msup><mn>3</mn><mn>0</mn></msup><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><msup><mn>3</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mfenced><mrow><munder><mo>&#8721;</mo><mrow><mi>&#945;</mi><mo>&#8712;</mo><mi>s</mi></mrow></munder><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup><mi mathvariant="normal">x</mi><mo>+</mo><munder><mo>&#8721;</mo><mrow><mi>a</mi><mo>&#8712;</mo><mi>s</mi></mrow></munder><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup></mrow></mfenced><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>50</mn><mi>x</mi><mo>+</mo><mn>25</mn><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p>Now for real roots </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>50</mn><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>25</mn><mi>&#946;</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>50</mn><mo>-</mo><mn>2</mn><mi>&#946;</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>&#8804;</mo><mn>25</mn></math></p><p>So, maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>.</p>

</details>

---

### Q18. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of real solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac></mrow></mfenced><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Given equation is:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac></mrow></mfenced><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p>We know,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mo>&#160;</mo><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>(</mo><mtext>using&#160;algebraic&#160;identities</mtext><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfrac><mo>=</mo><msup><mfenced><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn></math></p><p>So, we can write the given equation as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac></mrow></mfenced><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac><mo>=</mo><mi mathvariant="normal">t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mfenced><mrow><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi mathvariant="normal">t</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>3</mn><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mo>-</mo><mn>2</mn><mi mathvariant="normal">t</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi mathvariant="normal">t</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>3</mn><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi mathvariant="normal">t</mi><mo>+</mo><mi mathvariant="normal">t</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi mathvariant="normal">t</mi><mfenced><mrow><mi mathvariant="normal">t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mo>(</mo><mi mathvariant="normal">t</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced><mrow><mn>3</mn><mi mathvariant="normal">t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi mathvariant="normal">t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">t</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><mi mathvariant="normal">t</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Case</mi><mo>&#160;</mo><mi mathvariant="normal">I</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>Here</mtext><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">D</mi><mo>=</mo><msqrt><mo>-</mo><mn>3</mn></msqrt><mtext>&#160;i.e.&#160;no&#160;real&#160;solution</mtext><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Case</mi><mo>&#160;</mo><mi>II</mi><mspace linebreak="newline"></mspace><mo>&#160;</mo><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mi mathvariant="normal">x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>Here</mtext><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">D</mi><mo>=</mo><msqrt><mo>-</mo><mn>35</mn></msqrt><mo>&#160;</mo><mtext>i.e.&#160;no&#160;real&#160;solution</mtext></math></p><p>Hence, we don&#39;t have real solutions.</p>

</details>

---

### Q19. JEE Main 2022 (28 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of real solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>4</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>58</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>4</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>4</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>58</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>4</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mfrac><mo>+</mo><mn>4</mn><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>e</mi><mi>x</mi></msup></mfrac></mrow></mfenced><mo>-</mo><mn>58</mn></mrow></mfenced></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>e</mi><mi>x</mi></msup></mfrac><mo>=</mo><mi>t</mi></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>t</mi><mo>-</mo><mn>58</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn><mo>&#177;</mo><msqrt><mn>16</mn><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>58</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn><mo>&#177;</mo><mn>2</mn><msqrt><mn>62</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn><msqrt><mn>62</mn></msqrt></math> is possible and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>-</mo><mn>2</mn><msqrt><mn>62</mn></msqrt></math> is not possible as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#8805;</mo><mn>2</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">e</mi><mi>x</mi></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">e</mi><mi>x</mi></msup></mfrac><mo>=</mo><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn><msqrt><mn>62</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn><msqrt><mn>62</mn></msqrt></mrow></mfenced><msup><mi mathvariant="normal">e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>For real solution, discriminant <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>248</mn><mo>-</mo><mn>8</mn><msqrt><mn>62</mn></msqrt><mo>&#62;</mo><mn>0</mn></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mi>b</mi></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn><msqrt><mn>62</mn></msqrt></mrow><mn>2</mn></mfrac><mo>=</mo><msqrt><mn>62</mn></msqrt><mo>-</mo><mn>1</mn><mo>&#62;</mo><mn>0</mn></math></p><p>Hence, both roots of the equation are positive real roots.</p>

</details>

---

### Q20. JEE Main 2022 (26 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

The sum of the cubes of all the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Dividing by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>+</mo><mfrac><mn>3</mn><mi>x</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>-</mo><mn>3</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>3</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>=</mo><mn>0</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>=</mo><mn>3</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>,</mo></mtd><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> let the roots are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#948;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>+</mo><mi>&#948;</mi><mo>=</mo><mn>3</mn><mo>,</mo></mtd><mtd><mi>&#947;</mi><mi>&#948;</mi><mo>=</mo><mo>-</mo><mn>1</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#947;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#948;</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>+</mo><mfenced><mrow><mi>&#947;</mi><mo>+</mo><mi>&#948;</mi></mrow></mfenced><mfenced><mrow><msup><mfenced><mrow><mi>&#947;</mi><mo>+</mo><mi>&#948;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>&#947;</mi><mi>&#948;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mfenced><mrow><mn>9</mn><mo>-</mo><mn>3</mn><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>36</mn></math></p>

</details>

---

### Q21. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all real roots of equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mn>6</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>5</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>ln</mi><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>ln</mi><mn>3</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>t</mi></math>  so, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup></math></p><p>So, the given equation becomes, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mn>6</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> (or) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>t</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn></math>   (or) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>t</mi><mo>-</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mo>&#177;</mo><mn>2</mn></math> (or) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>t</mi><mfenced><mrow><mn>2</mn><mo>&#160;</mo><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>2</mn><mo>&#160;</mo><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mo>&#177;</mo><mn>2</mn></math> (or)  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mo>&#177;</mo><mn>2</mn></math> (or) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math> (or) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>But, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>t</mi><mo>&#62;</mo><mn>0</mn><mo>&#160;&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>&#62;</mo><mn>0</mn><mo>;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>  Only possible values for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>2</mn></mfenced></math> (or) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mn>2</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>ln</mi><mn>3</mn></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;&#160;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>ln</mi><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>  The sum of roots of given equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>ln</mi><mn>2</mn><mo>-</mo><mi>ln</mi><mn>3</mn><mo>-</mo><mi>ln</mi><mn>2</mn><mo>=</mo><mo>-</mo><mi>ln</mi><mn>3</mn></math>.</p>

</details>

---

### Q22. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>32</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>32</mn><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mn>81</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>32</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>32</mn><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mn>81</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>32</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>32</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mn>81</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>32</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>+</mo><mn>32</mn><mo>.</mo><msup><mn>32</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mn>81</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn><mo>&#215;</mo><msup><mn>32</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mn>81</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>32</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mfrac><mn>27</mn><mn>11</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><msub><mi>ln</mi><mn>32</mn></msub><mfenced><mfrac><mn>27</mn><mn>11</mn></mfrac></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>=</mo><msqrt><msub><mi>ln</mi><mn>32</mn></msub><mfenced><mfrac><mn>27</mn><mn>11</mn></mfrac></mfenced></msqrt><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
One solution in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q23. JEE Main 2021 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

The number of real roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>4</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>4</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>t</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>4</mn></msup><mo>-</mo><msup><mi>t</mi><mn>3</mn></msup><mo>-</mo><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Divide with <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup></math> on both sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>-</mo><mn>4</mn><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"></math>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>&#8805;</mo><mn>2</mn></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn></math> (reject)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>=</mo><mn>3</mn><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#177;</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#177;</mo><mn>2</mn><mo>.</mo><mn>23</mn></mrow><mn>2</mn></mfrac><mfenced><mrow><mo>&#8757;</mo><msqrt><mn>5</mn></msqrt><mo>&#8776;</mo><mn>2</mn><mo>.</mo><mn>23</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mfrac><mrow><mn>5</mn><mo>.</mo><mn>23</mn></mrow><mn>2</mn></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>77</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mn>2</mn><mo>.</mo><mn>615</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mn>0</mn><mo>.</mo><mn>385</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2908dcfc-f408-48f0-96ac-49861c85e1b4-image.png" style="width: 400px; height: 300px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> The number of real roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>.</mo></math></p>

</details>

---

### Q24. JEE Main 2021 (26 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

The sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>162</mn><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> power of the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> satisfying the equation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>1</mn></math> is factor of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mfrac><mstyle displaystyle="true"><mn>1</mn><mo>+</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac><mo>,</mo><mfrac><mstyle displaystyle="true"><mn>1</mn><mo>-</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mo>,</mo><mo>-</mo><mi>&#969;</mi></math></p><p>sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>162</mn><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> power of roots</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mn>1</mn></mfenced><mn>162</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup></mrow></mfenced><mn>162</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mi>&#969;</mi></mrow></mfenced><mn>162</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><msup><mfenced><mi>&#969;</mi></mfenced><mn>324</mn></msup><mo>+</mo><msup><mfenced><mi>&#969;</mi></mfenced><mn>162</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q25. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of real roots of the equation, <math><msup><mrow><mi>e</mi></mrow><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>4</mn><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> is:

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><mn>2</mn></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>1</mn></math>**

**Detailed Solution:**

Let <math><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>=</mo><mi>t</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi></mi><mi>&#8734;</mi></mrow></mfenced></math>
Given equation
<math><msup><mrow><mi>t</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>4</mn><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>t</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
<math><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>t</mi><mo>-</mo><mn>4</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>0</mn></math>
<math><mfenced separators="|"><mrow><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac></mrow></mfenced><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
Let <math><mi>t</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>t</mi></mrow></mfrac><mo>=</mo><mi>&#945;</mi></math>
<math><mfenced separators="|"><mrow><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>&#945;</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
<math><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>&#945;</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math>
<math><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>&#945;</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math>
<math><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>3</mn><mi></mi><mo>,</mo><mi></mi><mn>2</mn><mi></mi><mi></mi><mo>&#8658;</mo><mi></mi><mi></mi><mi>&#945;</mi><mo>=</mo><mn>2</mn><mi></mi><mo>&#8658;</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>=</mo><mn>2</mn></math>
<math><mi>x</mi><mo>=</mo><mn>0</mn></math> is the only solution.

</details>

---

