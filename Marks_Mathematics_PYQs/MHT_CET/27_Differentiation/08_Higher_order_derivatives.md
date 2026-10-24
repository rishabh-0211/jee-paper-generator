# MHT CET Mathematics - Differentiation

## Topic 8: Higher order derivatives

**Total Questions:** 28

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $y^2 = a\cos^2 x + b\sin^2 x$ be such that $a + b = 2024$ and $a > 0, b > 0$ follows $y^4 + y^3 y'' = k$. If $\lambda$ is the maximum possible value of $k$, then $\lambda =$

**Options:**

- **(A)** $(506)^2$
- **(B)** $506$
- **(C)** $(1012)^2$
- **(D)** $1012$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(1012)^2$**

**Detailed Solution:**

Given $y^2 = a \cos^2 x + b \sin^2 x$

Rewriting in terms of $\cos 2x$:

$y^2 = a\left(\dfrac{1 + \cos 2x}{2}\right) + b\left(\dfrac{1 - \cos 2x}{2}\right)$

$y^2 = \dfrac{a + b}{2} + \dfrac{a - b}{2} \cos 2x$

Let $A = \dfrac{a + b}{2}$ and $B = \dfrac{a - b}{2}$, then $y^2 = A + B \cos 2x$

Differentiating with respect to $x$:

$2yy' = -2B \sin 2x \Rightarrow yy' = -B \sin 2x$

Squaring both sides:

$y^2(y')^2 = B^2 \sin^2 2x$

Differentiating $yy' = -B \sin 2x$ with respect to $x$:

$(y')^2 + yy'' = -2B \cos 2x$

Multiplying by $y^2$ on both sides:

$y^2(y')^2 + y^3y'' = -2By^2 \cos 2x$

Substituting $y^2(y')^2 = B^2 \sin^2 2x$ and $y^2 = A + B \cos 2x$:

$B^2 \sin^2 2x + y^3y'' = -2B(A + B \cos 2x) \cos 2x$

$y^3y'' = -2AB \cos 2x - 2B^2 \cos^2 2x - B^2 \sin^2 2x$

$y^3y'' = -2AB \cos 2x - B^2 \cos^2 2x - B^2$

Now, expanding $y^4$:

$y^4 = (A + B \cos 2x)^2 = A^2 + 2AB \cos 2x + B^2 \cos^2 2x$

Therefore, $k = y^4 + y^3y''$

$k = (A^2 + 2AB \cos 2x + B^2 \cos^2 2x) + (-2AB \cos 2x - B^2 \cos^2 2x - B^2)$

$k = A^2 - B^2$

Substituting $A$ and $B$:

$k = \left(\dfrac{a + b}{2}\right)^2 - \left(\dfrac{a - b}{2}\right)^2 = ab$

Given $a + b = 2024$ and $a > 0, b > 0$. To find the maximum value of $k = ab$, we apply the AM-GM inequality:

$\dfrac{a + b}{2} \ge \sqrt{ab}$

$\sqrt{ab} \le \dfrac{2024}{2} = 1012$

$ab \le (1012)^2$

Thus, the maximum possible value of $k$ is $\lambda = (1012)^2$.

</details>

---

### Q2. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $y = \dfrac{1}{3x - 5}$ and if $\dfrac{d^4 y}{dx^4} = 1944$, then the value of $x$ is

**Options:**

- **(A)** $2$
- **(B)** $\dfrac{1}{2}$
- **(C)** $3$
- **(D)** $\dfrac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2$**

**Detailed Solution:**

Given $y = (3x - 5)^{-1}$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = -1(3x - 5)^{-2} \cdot 3 = -3(3x - 5)^{-2}$

$\dfrac{d^2 y}{dx^2} = -3(-2)(3x - 5)^{-3} \cdot 3 = 18(3x - 5)^{-3}$

$\dfrac{d^3 y}{dx^3} = 18(-3)(3x - 5)^{-4} \cdot 3 = -162(3x - 5)^{-4}$

$\dfrac{d^4 y}{dx^4} = -162(-4)(3x - 5)^{-5} \cdot 3 = 1944(3x - 5)^{-5}$

Given $\dfrac{d^4 y}{dx^4} = 1944$

$1944(3x - 5)^{-5} = 1944$

$(3x - 5)^{-5} = 1$

$3x - 5 = 1$

$3x = 6$

$x = 2$

Answer: $2$

</details>

---

### Q3. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = x - e^x$, then $\dfrac{d^2 x}{dy^2} = $ ...

**Options:**

- **(A)** $-\dfrac{e^x}{(1 - e^x)^3}$
- **(B)** $\dfrac{e^x}{(e^x - 1)^3}$
- **(C)** $\dfrac{1}{(1 - e^x)^3}$
- **(D)** $\dfrac{e^x}{(1 - e^x)^3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{e^x}{(1 - e^x)^3}$**

**Detailed Solution:**

Given $y = x - e^x$

Differentiating with respect to $x$, we get:

$\dfrac{dy}{dx} = 1 - e^x$

Therefore, $\dfrac{dx}{dy} = \dfrac{1}{1 - e^x}$

Differentiating again with respect to $y$, we use the chain rule $\dfrac{d}{dy} = \dfrac{dx}{dy} \cdot \dfrac{d}{dx}$:

$\dfrac{d^2 x}{dy^2} = \dfrac{d}{dy} \left( \dfrac{1}{1 - e^x} \right)$

$\dfrac{d^2 x}{dy^2} = \dfrac{dx}{dy} \cdot \dfrac{d}{dx} \left( (1 - e^x)^{-1} \right)$

$\dfrac{d^2 x}{dy^2} = \left( \dfrac{1}{1 - e^x} \right) \cdot \left( -1(1 - e^x)^{-2}(-e^x) \right)$

$\dfrac{d^2 x}{dy^2} = \dfrac{e^x}{(1 - e^x)^3}$

Answer: $\dfrac{e^x}{(1 - e^x)^3}$

</details>

---

### Q4. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x), g(x)$ be twice differentiable functions, satisfying $f''(x) = g''(x), f'(1) = 2g'(1) = 4$ and $f(2) = 3g(2) = 9$ then $f(x) - g(x)$ at $x = 4$ is equal to

**Options:**

- **(A)** $0$
- **(B)** $10$
- **(C)** $8$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $10$**

**Detailed Solution:**

Let $h(x) = f(x) - g(x)$.

Given $f''(x) = g''(x)$, we have $h''(x) = 0$.

Integrating with respect to $x$, we get $h'(x) = c_1$.

We are given $f'(1) = 4$ and $2g'(1) = 4 \Rightarrow g'(1) = 2$.

Thus, $h'(1) = f'(1) - g'(1) = 4 - 2 = 2$.

Since $h'(x)$ is constant, $h'(x) = 2$.

Integrating again with respect to $x$, we get $h(x) = 2x + c_2$.

We are given $f(2) = 9$ and $3g(2) = 9 \Rightarrow g(2) = 3$.

Thus, $h(2) = f(2) - g(2) = 9 - 3 = 6$.

Substituting $x = 2$ into $h(x) = 2x + c_2$, we get $4 + c_2 = 6 \Rightarrow c_2 = 2$.

Therefore, $h(x) = 2x + 2$.

At $x = 4$, $h(4) = 2(4) + 2 = 10$.

Answer: $10$

</details>

---

### Q5. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \dfrac{1}{3x + 5}$, then the value of $\dfrac{d^9 y}{dx^9}$ is..

**Options:**

- **(A)** $\dfrac{9! \times 3^9}{(3x + 5)^9}$
- **(B)** $\dfrac{(-1)^8 \times 9! \times 3^9}{(3x + 5)^9}$
- **(C)** $\dfrac{(-1)^9 \times 9! \times 3^9}{(3x + 5)^{10}}$
- **(D)** $\dfrac{(-1)^8 \times 8! \times 3^9}{(3x + 5)^{10}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{(-1)^9 \times 9! \times 3^9}{(3x + 5)^{10}}$**

**Detailed Solution:**

Given $y = (3x + 5)^{-1}$

Differentiating with respect to $x$, we get:

$\dfrac{dy}{dx} = -1(3x + 5)^{-2} \times 3$

$\dfrac{d^2y}{dx^2} = (-1)(-2)(3x + 5)^{-3} \times 3^2$

$\dfrac{d^3y}{dx^3} = (-1)(-2)(-3)(3x + 5)^{-4} \times 3^3$

Generalizing for the $n$-th derivative:

$\dfrac{d^ny}{dx^n} = (-1)^n n! (3x + 5)^{-(n+1)} \times 3^n$

Substituting $n = 9$:

$\dfrac{d^9y}{dx^9} = (-1)^9 9! (3x + 5)^{-10} \times 3^9 = \dfrac{(-1)^9 \times 9! \times 3^9}{(3x + 5)^{10}}$

Answer: $\dfrac{(-1)^9 \times 9! \times 3^9}{(3x + 5)^{10}}$

</details>

---

### Q6. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \left(\dfrac{ax+b}{cx+d}\right)$, then $2\dfrac{dy}{dx} \cdot \dfrac{d^3 y}{dx^3}$ is equal to

**Options:**

- **(A)** $\left(\dfrac{d^2 y}{dx^2}\right)^2$
- **(B)** $3\dfrac{d^2 y}{dx^2}$
- **(C)** $3\left(\dfrac{d^2 y}{dx^2}\right)^2$
- **(D)** $3\dfrac{d^2 x}{dy^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3\left(\dfrac{d^2 y}{dx^2}\right)^2$**

**Detailed Solution:**

Given $y = \dfrac{ax+b}{cx+d}$

Differentiating with respect to $x$, we get

$\dfrac{dy}{dx} = \dfrac{a(cx+d) - c(ax+b)}{(cx+d)^2} = \dfrac{ad-bc}{(cx+d)^2}$

Let $ad-bc = k$. Then $\dfrac{dy}{dx} = k(cx+d)^{-2}$

Differentiating again with respect to $x$, we get

$\dfrac{d^2 y}{dx^2} = -2kc(cx+d)^{-3}$

Differentiating once more with respect to $x$, we get

$\dfrac{d^3 y}{dx^3} = 6kc^2(cx+d)^{-4}$

Evaluating $2\dfrac{dy}{dx} \cdot \dfrac{d^3 y}{dx^3}$:

$2\dfrac{dy}{dx} \cdot \dfrac{d^3 y}{dx^3} = 2 \left( k(cx+d)^{-2} \right) \left( 6kc^2(cx+d)^{-4} \right) = 12k^2 c^2 (cx+d)^{-6}$

Evaluating $3\left(\dfrac{d^2 y}{dx^2}\right)^2$:

$3\left(\dfrac{d^2 y}{dx^2}\right)^2 = 3 \left( -2kc(cx+d)^{-3} \right)^2 = 12k^2 c^2 (cx+d)^{-6}$

Therefore, $2\dfrac{dy}{dx} \cdot \dfrac{d^3 y}{dx^3} = 3\left(\dfrac{d^2 y}{dx^2}\right)^2$

Answer: $3\left(\dfrac{d^2 y}{dx^2}\right)^2$

</details>

---

### Q7. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \sqrt{x^2 + 8x + 3}$, then the value of $\dfrac{d^2 y}{dx^2}$ at $x = 3$ is

**Options:**

- **(A)** $\dfrac{-13}{216}$
- **(B)** $\dfrac{13}{216}$
- **(C)** $\dfrac{15}{216}$
- **(D)** $\dfrac{-15}{216}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{-13}{216}$**

**Detailed Solution:**

Given $y = \sqrt{x^2 + 8x + 3}$

Squaring both sides:

$y^2 = x^2 + 8x + 3$

Differentiating with respect to $x$:

$2y \dfrac{dy}{dx} = 2x + 8 \Rightarrow y \dfrac{dy}{dx} = x + 4$

Differentiating again with respect to $x$:

$y \dfrac{d^2 y}{dx^2} + \left(\dfrac{dy}{dx}\right)^2 = 1$

At $x = 3$, $y = \sqrt{3^2 + 8(3) + 3} = \sqrt{36} = 6$

Substituting $x = 3$ and $y = 6$ in the first derivative equation:

$6 \dfrac{dy}{dx} = 3 + 4 \Rightarrow \dfrac{dy}{dx} = \dfrac{7}{6}$

Substituting $y = 6$ and $\dfrac{dy}{dx} = \dfrac{7}{6}$ in the second derivative equation:

$6 \dfrac{d^2 y}{dx^2} + \left(\dfrac{7}{6}\right)^2 = 1$

$6 \dfrac{d^2 y}{dx^2} = 1 - \dfrac{49}{36} = \dfrac{-13}{36}$

$\dfrac{d^2 y}{dx^2} = \dfrac{-13}{216}$

Answer: $\dfrac{-13}{216}$

</details>

---

### Q8. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=3 x^2+2 x \mathrm{f}^{\prime}(1)+\mathrm{f}^{\prime \prime}(2)$, then $\mathrm{f}(x)=$ ______

**Options:**

- **(A)** $3 x^2+8 x+4$
- **(B)** $3 x^2+12 x+12$
- **(C)** $3 x^2-12 x+6$
- **(D)** $3 x^2-18 x+5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3 x^2-12 x+6$**

**Detailed Solution:**

Let $f'(1) = a$ and $f''(2) = b$.

$f(x) = 3x^2 + 2ax + b$

Differentiating with respect to $x$, we get:

$f'(x) = 6x + 2a$

Differentiating again with respect to $x$, we get:

$f''(x) = 6$

Since $f''(x) = 6$ for all $x$, we have $f''(2) = 6$, which gives $b = 6$.

Substitute $x = 1$ in $f'(x)$:

$f'(1) = 6(1) + 2a$

$a = 6 + 2a$

$a = -6$

Substituting the values of $a$ and $b$ in $f(x)$, we get:

$f(x) = 3x^2 + 2(-6)x + 6$

$f(x) = 3x^2 - 12x + 6$

Answer: $3 x^2-12 x+6$

</details>

---

### Q9. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\frac{x^2}{a^2}+\frac{\mathrm{y}^2}{\mathrm{~b}^2}=1$, then $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}$ is

**Options:**

- **(A)** $\frac{-\mathrm{b}^4}{a}$
- **(B)** $\frac{b^4}{a^2}$
- **(C)** $\frac{-\mathrm{b}^4}{\mathrm{y}^3}$
- **(D)** $\frac{-b^4}{a^2 \cdot y^3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{-b^4}{a^2 \cdot y^3}$**

**Detailed Solution:**

Given $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$

Differentiating with respect to $x$:

$\dfrac{2x}{a^2} + \dfrac{2y}{b^2} \dfrac{dy}{dx} = 0$

$\dfrac{dy}{dx} = -\dfrac{b^2 x}{a^2 y}$

Differentiating again with respect to $x$:

$\dfrac{d^2 y}{dx^2} = -\dfrac{b^2}{a^2} \left( \dfrac{y \cdot 1 - x \dfrac{dy}{dx}}{y^2} \right)$

Substituting $\dfrac{dy}{dx} = -\dfrac{b^2 x}{a^2 y}$:

$\dfrac{d^2 y}{dx^2} = -\dfrac{b^2}{a^2} \left( \dfrac{y - x \left( -\dfrac{b^2 x}{a^2 y} \right)}{y^2} \right)$

$\dfrac{d^2 y}{dx^2} = -\dfrac{b^2}{a^2} \left( \dfrac{a^2 y^2 + b^2 x^2}{a^2 y^3} \right)$

From the given equation, $b^2 x^2 + a^2 y^2 = a^2 b^2$. Substituting this in the numerator:

$\dfrac{d^2 y}{dx^2} = -\dfrac{b^2}{a^2} \left( \dfrac{a^2 b^2}{a^2 y^3} \right) = \dfrac{-b^4}{a^2 y^3}$

Answer: $\frac{-b^4}{a^2 \cdot y^3}$

</details>

---

### Q10. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=3 x^3+2 x^2 \mathrm{f}^{\prime}(1)+x \mathrm{f}^{\prime \prime}(2)+\mathrm{f}^{\prime \prime \prime}(3)$ then $\mathrm{f}(x)=$ $\qquad$

**Options:**

- **(A)** $\frac{1}{7}\left(3 x^3-90 x^2+72 x+18\right)$
- **(B)** $\frac{1}{7}\left(21 x^3-90 x^2+72 x+126\right)$
- **(C)** $3 x^3-90 x^2+72 x+18$
- **(D)** $3 x^3-45 x^2+36 x+9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{7}\left(21 x^3-90 x^2+72 x+126\right)$**

**Detailed Solution:**

Let $f'(1) = a$, $f''(2) = b$, and $f'''(3) = c$.

The given function can be written as:
$f(x) = 3x^3 + 2ax^2 + bx + c$

Differentiating with respect to $x$, we get:
$f'(x) = 9x^2 + 4ax + b$
$f''(x) = 18x + 4a$
$f'''(x) = 18$

From the third derivative, we have:
$c = f'''(3) = 18$

From the second derivative, we have:
$b = f''(2) = 18(2) + 4a = 36 + 4a$

From the first derivative, we have:
$a = f'(1) = 9(1)^2 + 4a(1) + b$
$a = 9 + 4a + b$
$3a + b = -9$

Substituting $b = 36 + 4a$ into the equation $3a + b = -9$:
$3a + 36 + 4a = -9$
$7a = -45$
$a = -\dfrac{45}{7}$

Now, substituting the value of $a$ to find $b$:
$b = 36 + 4\left(-\dfrac{45}{7}\right) = \dfrac{252 - 180}{7} = \dfrac{72}{7}$

Substituting $a$, $b$, and $c$ back into the original function:
$f(x) = 3x^3 + 2\left(-\dfrac{45}{7}\right)x^2 + \left(\dfrac{72}{7}\right)x + 18$
$f(x) = 3x^3 - \dfrac{90}{7}x^2 + \dfrac{72}{7}x + 18$
$f(x) = \dfrac{1}{7}(21x^3 - 90x^2 + 72x + 126)$

Answer: $\frac{1}{7}\left(21 x^3-90 x^2+72 x+126\right)$

</details>

---

### Q11. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For $N \in \mathbb{N}$,
$\frac{\mathrm{d}^{\mathrm{n}}}{\mathrm{~d} x^{\mathrm{n}}}(\log x)=$

**Options:**

- **(A)** $\frac{(n-1)!}{x^n}$
- **(B)** $\frac{\mathrm{n}!}{x^{\mathrm{n}}}$
- **(C)** $\frac{(\mathrm{n}-2)!}{x^{\mathrm{n}}}$
- **(D)** $(-1)^{\mathrm{n}-1} \frac{(\mathrm{n}-1)!}{x^{\mathrm{n}}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(-1)^{\mathrm{n}-1} \frac{(\mathrm{n}-1)!}{x^{\mathrm{n}}}$**

**Detailed Solution:**

Let $y = \log x$

Differentiating with respect to $x$,

$y_1 = \dfrac{1}{x} = x^{-1}$

$y_2 = -1 \cdot x^{-2} = \dfrac{-1}{x^2}$

$y_3 = (-1)(-2) x^{-3} = \dfrac{2}{x^3}$

$y_4 = (-1)(-2)(-3) x^{-4} = \dfrac{-6}{x^4}$

Observing the pattern, the $n$-th derivative is given by:

$y_n = (-1)^{n-1} \dfrac{(n-1)!}{x^n}$

Answer: $(-1)^{\mathrm{n}-1} \frac{(\mathrm{n}-1)!}{x^{\mathrm{n}}}$

</details>

---

### Q12. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}=a^x \cdot \mathrm{~b}^{2 x-1}$, then $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}$ is equal to

**Options:**

- **(A)** $\mathrm{y}\left(\log \left(a \mathrm{~b}^2\right)\right)$
- **(B)** $\mathrm{y}^2\left(\log \left(a \mathrm{~b}^2\right)\right)$
- **(C)** $\mathrm{y}\left(\log \left(a \mathrm{~b}^2\right)\right)^2$
- **(D)** $y^2(\log (a b))^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{y}\left(\log \left(a \mathrm{~b}^2\right)\right)^2$**

**Detailed Solution:**

Given $y = a^x \cdot b^{2x-1}$

Taking logarithm on both sides:

$\log y = \log(a^x \cdot b^{2x-1})$

$\log y = x \log a + (2x-1) \log b$

$\log y = x \log a + 2x \log b - \log b$

$\log y = x(\log a + \log b^2) - \log b$

$\log y = x \log(a b^2) - \log b$

Differentiating with respect to $x$:

$\dfrac{1}{y} \dfrac{dy}{dx} = \log(a b^2)$

$\dfrac{dy}{dx} = y \log(a b^2)$

Differentiating again with respect to $x$:

$\dfrac{d^2 y}{dx^2} = \dfrac{dy}{dx} \log(a b^2)$

Substituting $\dfrac{dy}{dx} = y \log(a b^2)$:

$\dfrac{d^2 y}{dx^2} = y \log(a b^2) \cdot \log(a b^2)$

$\dfrac{d^2 y}{dx^2} = y(\log(a b^2))^2$

Answer: $\mathrm{y}\left(\log \left(a \mathrm{~b}^2\right)\right)^2$

</details>

---

### Q13. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For $\mathrm{n} \in \mathbb{N}$ if $\mathrm{y}=a x^{\mathrm{n}+1}+\mathrm{b} x^{-\mathrm{n}}$, then $x^2 \frac{\mathrm{~d}^2 \mathrm{y}}{\mathrm{d} x^2}=$

**Options:**

- **(A)** $n(n-1) y$
- **(B)** $(n-1) y$
- **(C)** $\mathrm{n}(\mathrm{n}+1) \mathrm{y}$
- **(D)** $(\mathrm{n}+1) \mathrm{y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{n}(\mathrm{n}+1) \mathrm{y}$**

**Detailed Solution:**

Given $y = a x^{n+1} + b x^{-n}$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = a(n+1)x^n - bn x^{-n-1}$

Differentiating again with respect to $x$:

$\dfrac{d^2 y}{dx^2} = a(n+1)n x^{n-1} - bn(-n-1) x^{-n-2}$

$\dfrac{d^2 y}{dx^2} = a n(n+1) x^{n-1} + b n(n+1) x^{-n-2}$

Multiplying both sides by $x^2$:

$x^2 \dfrac{d^2 y}{dx^2} = x^2 \left( a n(n+1) x^{n-1} + b n(n+1) x^{-n-2} \right)$

$x^2 \dfrac{d^2 y}{dx^2} = a n(n+1) x^{n+1} + b n(n+1) x^{-n}$

$x^2 \dfrac{d^2 y}{dx^2} = n(n+1) \left( a x^{n+1} + b x^{-n} \right)$

Substituting $y = a x^{n+1} + b x^{-n}$:

$x^2 \dfrac{d^2 y}{dx^2} = n(n+1) y$

Answer: $\mathrm{n}(\mathrm{n}+1) \mathrm{y}$

</details>

---

### Q14. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x^2+y^2=\mathrm{t}+\frac{1}{\mathrm{t}}, x^4+y^4=\mathrm{t}^2+\frac{1}{\mathrm{t}^2}$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}=$

**Options:**

- **(A)** $\frac{1}{x^3 y}$
- **(B)** $\frac{1}{x y^3}$
- **(C)** $-\frac{1}{x y^3}$
- **(D)** $-\frac{1}{x^3 y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{1}{x^3 y}$**

**Detailed Solution:**

Given $x^2+y^2=t+\dfrac{1}{t}$ and $x^4+y^4=t^2+\dfrac{1}{t^2}$

Squaring the first equation on both sides, we get:

$(x^2+y^2)^2 = \left(t+\dfrac{1}{t}\right)^2$

$x^4+y^4+2x^2y^2 = t^2+\dfrac{1}{t^2}+2$

Substituting $x^4+y^4 = t^2+\dfrac{1}{t^2}$ into the above equation:

$t^2+\dfrac{1}{t^2}+2x^2y^2 = t^2+\dfrac{1}{t^2}+2$

$2x^2y^2 = 2$

$x^2y^2 = 1$

$y^2 = x^{-2}$

Differentiating both sides with respect to $x$:

$2y \dfrac{\mathrm{d} y}{\mathrm{d} x} = -2x^{-3}$

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = -\dfrac{1}{x^3 y}$

Answer: $-\frac{1}{x^3 y}$

</details>

---

### Q15. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\mathrm{ax}^{\mathrm{n}+1}+\mathrm{b} x^{-\mathrm{n}}$, then $x^2 \dfrac{\mathrm{~d}^2 y}{\mathrm{~d} x^2}=$

**Options:**

- **(A)** $\mathrm{n}(\mathrm{n}+1) y$
- **(B)** $(\mathrm{n}+1)(\mathrm{n}-2) y$
- **(C)** $\mathrm{n}(\mathrm{n}-2) y$
- **(D)** $(\mathrm{n}+1) y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{n}(\mathrm{n}+1) y$**

**Detailed Solution:**

Given $y = a x^{n+1} + b x^{-n}$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = a(n+1)x^n - bn x^{-n-1}$

Differentiating again with respect to $x$:

$\dfrac{d^2 y}{dx^2} = a(n+1)n x^{n-1} - bn(-n-1) x^{-n-2}$

$\dfrac{d^2 y}{dx^2} = an(n+1) x^{n-1} + bn(n+1) x^{-n-2}$

Multiplying both sides by $x^2$:

$x^2 \dfrac{d^2 y}{dx^2} = an(n+1) x^{n+1} + bn(n+1) x^{-n}$

$x^2 \dfrac{d^2 y}{dx^2} = n(n+1) (a x^{n+1} + b x^{-n})$

Substituting the value of $y$:

$x^2 \dfrac{d^2 y}{dx^2} = n(n+1) y$

Answer: $\mathrm{n}(\mathrm{n}+1) y$

</details>

---

### Q16. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\mathrm{A} \cos \mathrm{n} x+\mathrm{B} \sin \mathrm{n} x$, then $\dfrac{\mathrm{d}^2 y}{\mathrm{~d} x^2}=$

**Options:**

- **(A)** $-\mathrm{n}^2 y$
- **(B)** $\mathrm{n}^2 y$
- **(C)** $\mathrm{n}^2 x$
- **(D)** $\mathrm{n}^2 x^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\mathrm{n}^2 y$**

**Detailed Solution:**

Given $y = \mathrm{A} \cos \mathrm{n} x + \mathrm{B} \sin \mathrm{n} x$

Differentiating with respect to $x$, we get

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = -\mathrm{A}\mathrm{n} \sin \mathrm{n} x + \mathrm{B}\mathrm{n} \cos \mathrm{n} x$

Differentiating again with respect to $x$, we get

$\dfrac{\mathrm{d}^2 y}{\mathrm{d} x^2} = -\mathrm{A}\mathrm{n}^2 \cos \mathrm{n} x - \mathrm{B}\mathrm{n}^2 \sin \mathrm{n} x$

$\dfrac{\mathrm{d}^2 y}{\mathrm{d} x^2} = -\mathrm{n}^2 (\mathrm{A} \cos \mathrm{n} x + \mathrm{B} \sin \mathrm{n} x)$

Substituting $y = \mathrm{A} \cos \mathrm{n} x + \mathrm{B} \sin \mathrm{n} x$, we get

$\dfrac{\mathrm{d}^2 y}{\mathrm{d} x^2} = -\mathrm{n}^2 y$

Answer: $-\mathrm{n}^2 y$

</details>

---

### Q17. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f: R \rightarrow R$ be a function such that $\mathrm{f}(x)=x^3+x^2 \mathrm{f}^{\prime}(1)+x \mathrm{f}^{\prime \prime}(2)+6, x \in \mathrm{R}$, then $\mathrm{f}(2)$ equals

**Options:**

- **(A)** $30$
- **(B)** $-4$
- **(C)** $-2$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-2$**

**Detailed Solution:**

$\begin{array}{ll} & \mathrm{f}(x)=x^3+x^2 \mathrm{f}^{\prime}(1)+x \mathrm{f}^{\prime \prime}(2)+6 \\ \therefore \quad & \mathrm{f}^{\prime}(x)=3 x^2+2 x \mathrm{f}^{\prime}(1)+\mathrm{f}^{\prime \prime}(2) \\ \therefore \quad & \mathrm{f}^{\prime \prime}(x)=6 x+2 \mathrm{f}^{\prime}(1)\end{array}$
Substituting $x=1$ in (i), we get
$$
\begin{aligned}
& \mathrm{f}^{\prime}(1)=3(1)^2+2(1) \mathrm{f}^{\prime}(1)+\mathrm{f}^{\prime \prime}(2) \\
& \Rightarrow \mathrm{f}^{\prime}(1)+\mathrm{f}^{\prime \prime}(2)=-3
\end{aligned}
$$

Substituting $x=2$ in (ii), we get
$$
\begin{aligned}
& \mathrm{f}^{\prime \prime}(2)=6(2)+2 \mathrm{f}^{\prime}(1) \\
& \Rightarrow \mathrm{f}^{\prime \prime}(2)=12+2 \mathrm{f}^{\prime}(1)
\end{aligned}
$$

From (iii) and (iv), we get
$$
\begin{aligned}
& \mathrm{f}^{\prime}(1)+12+2 \mathrm{f}^{\prime}(1)=-3 \\
& \Rightarrow 3 \mathrm{f}^{\prime}(1)=-15 \\
& \Rightarrow \mathrm{f}^{\prime}(1)=-5 \\
& \text { From (iii) },-5+\mathrm{f}^{\prime \prime}(2)=-3 \\
& \Rightarrow \mathrm{f}^{\prime \prime}(2)=2
\end{aligned}
$$
$\begin{aligned} \therefore \quad \mathrm{f}(2) & =2^3+2^2(-5)+2(2)^{\prime}+6 \\ & =8-20+4+6 \\ & =-2\end{aligned}$

</details>

---

### Q18. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $f: R \rightarrow R$ be a function such that $\mathrm{f}(x)=x^3+x^2 \mathrm{f}^{\prime}(1)+x \mathrm{f}^{\prime \prime}(2)+6, x \in \mathrm{R}$, then $\mathrm{f}(2)$ equals

**Options:**

- **(A)** 30
- **(B)** $-2$
- **(C)** $-4$
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-2$**

**Detailed Solution:**

$\mathrm{f}(x)=x^3+x^2 \mathrm{f}^{\prime}(1)+x \mathrm{f}^{\prime \prime}(2)+6$
$\therefore \quad \mathrm{f}^{\prime}(x)=3 x^2+2 x \mathrm{f}^{\prime}(1)+\mathrm{f}^{\prime \prime}(2)$...(i)
$\therefore \quad \mathrm{f}^{\prime \prime}(x)=6 x+2 \mathrm{f}^{\prime}(1)$    ...(ii)
Substituting $x=1$ in (i), we get
$f^{\prime}(1)=3(1)^2+2(1) f^{\prime}(1)+f^{\prime \prime}(2)$
$\Rightarrow \mathrm{f}^{\prime}(1)+\mathrm{f}^{\prime \prime}(2)=-3$       ...(iii)
Substituting $x=2$ in (ii), we get
$f^{\prime \prime}(2)=6(2)+2 f^{\prime}(1)$
$\Rightarrow \mathrm{f}^{\prime \prime}(2)=12+2 \mathrm{f}^{\prime}(1)$                           ...(iv)
From (iii) and (iv), we get
$$
\begin{aligned}
& \mathrm{f}^{\prime}(1)+12+2 \mathrm{f}^{\prime}(1)=-3 \\
& \Rightarrow 3 \mathrm{f}^{\prime}(1)=-15 \\
& \Rightarrow \mathrm{f}^{\prime}(1)=-5 \\
& \text { From (iii) },-5+\mathrm{f}^{\prime \prime}(2)=-3 \\
& \Rightarrow \mathrm{f}^{\prime \prime}(2)=2
\end{aligned}
$$
$\begin{aligned} \therefore \quad f(2) & =2^3+2^2(-5)+2(2)+6 \\ & =8-20+4+6 \\ & =-2\end{aligned}$

</details>

---

### Q19. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{f}: \mathrm{R} \rightarrow \mathrm{R}$ be a function such that $\mathrm{f}(x)=x^3+x^2 \mathrm{f}^{\prime}(1)+x \mathrm{f}^{\prime \prime}(2)+6, x \in \mathrm{R}$, then $\mathrm{f}(2)$ is

**Options:**

- **(A)** 30
- **(B)** -4
- **(C)** -2
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -2**

**Detailed Solution:**

$$
\begin{array}{ll} 
& \mathrm{f}(x)=x^3+x^2 \mathrm{f}^{\prime}(1)+x \mathrm{f}^{\prime \prime}(2)+6 \\
\therefore \quad & \mathrm{f}^{\prime}(x)=3 x^2+2 x \mathrm{f}^{\prime}(1)+\mathrm{f}^{\prime \prime}(2) \\
\therefore \quad & \mathrm{f}^{\prime \prime}(x)=6 x+2 \mathrm{f}^{\prime}(1)
\end{array}
$$
Substituting $x=1$ in (i), we get
$$
\begin{aligned}
& \mathrm{f}^{\prime}(1)=3(1)^2+2(1) \mathrm{f}^{\prime}(1)+\mathrm{f}^{\prime \prime}(2) \\
& \Rightarrow \mathrm{f}^{\prime}(1)+\mathrm{f}^{\prime \prime}(2)=-3
\end{aligned}
$$
Substituting $x=2$ in (ii), we get
$$
\begin{aligned}
& \mathrm{f}^{\prime \prime}(2)=6(2)+2 \mathrm{f}^{\prime}(1) \\
& \Rightarrow \mathrm{f}^{\prime \prime}(2)=12+2 \mathrm{f}^{\prime}(1)
\end{aligned}
$$
From (iii) and (iv), we get
$$
\begin{aligned}
& \mathrm{f}^{\prime}(1)+12+2 \mathrm{f}^{\prime}(1)=-3 \\
& \Rightarrow 3 \mathrm{f}^{\prime}(1)=-15 \\
& \Rightarrow \mathrm{f}^{\prime}(1)=-5
\end{aligned}
$$
From (iii), $-5+\mathrm{f}^{\prime \prime}(2)=-3$
$\Rightarrow \mathrm{f}^{\prime \prime}(2)=2$
$$
\begin{aligned}
\therefore \quad \mathrm{f}(2) & =2^3+2^2(-5)+2(2)+6 \\
& =8-20+4+6=-2
\end{aligned}
$$

</details>

---

### Q20. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\cos ^2\left(\frac{5 x}{2}\right)-\sin ^2\left(\frac{5 x}{2}\right)$, then $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}=$

**Options:**

- **(A)** -25y
- **(B)** $\frac{25}{2} y$
- **(C)** $-\frac{25}{2} y$
- **(D)** 25y

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -25y**

**Detailed Solution:**

$y=\cos ^2 \frac{5 x}{2}-\sin ^2 \frac{5 x}{2}=\cos 5 x$
$\Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=-5 \sin 5 x$
$\Rightarrow \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}=-25 \cos 5 x=-25 y$

</details>

---

### Q21. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=e^{4 x}+2 e^{-x}$ satisfies the equation $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}+A \frac{\mathrm{d} y}{\mathrm{~d} x}+\mathrm{By}=o$ then values of and $B$ are respectively

**Options:**

- **(A)** 3,4
- **(B)** -3,-4
- **(C)** 4,3
- **(D)** -4,-3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -3,-4**

**Detailed Solution:**

$\begin{aligned} & y=e^{4 x}+2 e^{-x} \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=4 \cdot e^{4 x}-2 \cdot e^{-x} \\ & \Rightarrow \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}=16 e^{4 x}+2 e^{-x} \\ & \Rightarrow \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}-3 \frac{\mathrm{d} y}{\mathrm{~d} x}-4 y=0 \\ & \Rightarrow A=-3 \text { and } B=-4\end{aligned}$

</details>

---

### Q22. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y^2=a x^2+b x+c$, where $a, b, c$ are constants, then $y^3 \frac{d^2 y}{d x^2}$ is equal to

**Options:**

- **(A)** functions of $y$
- **(B)** function of both $\mathrm{x}$ and $\mathrm{y}$
- **(C)** constant
- **(D)** function of $x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) function of $x$**

**Detailed Solution:**

$$
y^2=a x^2+b x+c
$$
Differentiating w.r.t. $x$, we get
$$
\begin{aligned}
& 2 y \frac{d y}{d x}=2 a x+b \quad \Rightarrow 2 y \frac{d^2 y}{d x^2}+2\left(\frac{d y}{d x}\right)^2=2 a \\
& \therefore y \frac{d^2 y}{d x^2}+\left(\frac{d y}{d x}\right)^2=a \\
& \therefore y^3 \frac{d^2 y}{d x^2}=\left(a x^2+b x+c\right)\left[\left(\frac{2 a x+b}{2}\right)^2-a\right]
\end{aligned}
$$
R.H.S. of eq. (1) is a function of ' $x$ ' only.

</details>

---

### Q23. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=2 \sin x+3 \cos x$ and $y+A \frac{d^2 y}{d x^2}=B$, then the values of $A$, $\mathrm{B}$ are respectively

**Options:**

- **(A)** 0,1
- **(B)** 0,-1
- **(C)** -1,0
- **(D)** 1,0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1,0**

**Detailed Solution:**

$$
\begin{aligned}
& y=2 \sin x+3 \cos x \\
& \therefore \frac{d y}{d x}=2 \cos x-3 \sin x \\
& \therefore \frac{d^2 y}{d x^2}=-2 \sin x-3 \cos x=-(2 \sin x+3 \cos x)=-y \\
& \therefore y+\frac{d^2 y}{d x^2}=0
\end{aligned}
$$
We have $y+A \frac{d^2 y}{d x^2}=B \Rightarrow A=1, B=0$

</details>

---

### Q24. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{y}=\cos ^{2}\left(\frac{5 x}{2}\right)-\sin ^{2}\left(\frac{5 x}{2}\right)$, then $\left(\frac{\mathrm{d}^{2} \mathrm{y}}{\mathrm{d} x^{2}}\right)=$

**Options:**

- **(A)** $-5 \sqrt{1-y^{2}}$
- **(B)** $5 \sqrt{1-y^{2}}$
- **(C)** $25 y$
- **(D)** $-25 y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-25 y$**

**Detailed Solution:**

Given
$$
\begin{aligned}
y &=\cos ^{2}\left(\frac{5 x}{2}\right)-\sin ^{2}\left(\frac{5 x}{2}\right) \\
y &=\cos \left(2 \times \frac{5 x}{2}\right) \Rightarrow y=\cos 5 x \\
\therefore \frac{d y}{d x} &=-5 \sin 5 x \Rightarrow \frac{d^{2} y}{d x^{2}} \\
&=-25 \cos 5 x=-25 y
\end{aligned}
$$

</details>

---

### Q25. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sqrt{x+y}+\sqrt{y-x}=5$, then $\left(\frac{d^{2} y}{d x^{2}}\right)=$

**Options:**

- **(A)** $\frac{2}{25}$
- **(B)** $\frac{2}{5}$
- **(C)** $\frac{-2}{5}$
- **(D)** $\frac{-2}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2}{25}$**

**Detailed Solution:**

(D)
Given $\sqrt{x+y}+\sqrt{y-x}=5 \Rightarrow \sqrt{y-x}=5-\sqrt{x+y}$
On squaring both side, we get
$$
y-x=25+x+y-10 \sqrt{x+y} \Rightarrow 10 \sqrt{x+y}-2 x=25
$$
Differentiating w.r.t. $x$,
$10 \times \frac{1}{2 \sqrt{x+y}}\left(1+\frac{d y}{d x}\right)-2 \times 1=0 \Rightarrow \frac{5}{\sqrt{x+y}}\left(1+\frac{d y}{d x}\right)=2$
$$
\therefore 1+\frac{d y}{d x}=\frac{2 \sqrt{x+y}}{5}....(1)
$$
Differentiating w.r.t. $x$,
$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} &=\frac{2}{5} \times \frac{1}{2 \sqrt{x+y}}\left(1+\frac{d y}{d x}\right)=\frac{1}{5 \sqrt{x+y}} \times \frac{2 \sqrt{x+y}}{5} \quad \ldots[\because \text { From (1) }] \\
&=\frac{2}{25}
\end{aligned}
$$

</details>

---

### Q26. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x=a(1-\cos \theta), \quad y=a(\theta-\sin \theta)$, then $\frac{d^{2} y}{d x^{2}}=$

**Options:**

- **(A)** $\frac{\cos ^{2}\left(\frac{\theta}{2}\right)}{2 \operatorname{acosec} \theta}$
- **(B)** $\frac{\operatorname{cosec} \theta}{2 a \cos ^{2}\left(\frac{\theta}{2}\right)}$
- **(C)** $\frac{\cos \left(\frac{\theta}{2}\right)}{2 \operatorname{asin} \theta}$
- **(D)** $\frac{\sin \left(\frac{\theta}{2}\right)}{2 \mathrm{a} \cos \theta}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\operatorname{cosec} \theta}{2 a \cos ^{2}\left(\frac{\theta}{2}\right)}$**

**Detailed Solution:**

$\frac{d x}{d \theta}=a \sin \theta, \frac{d y}{d \theta}=a(1-\cos \theta)$
$\frac{d y}{d x}=\frac{a(1-\cos \theta)}{a \sin \theta}=\frac{2 \sin ^{2} \frac{\theta}{2}}{2 \sin \frac{\theta}{2} \cos \frac{\theta}{2}}=\tan \frac{\theta}{2}$
$\frac{d^{2} y}{d x^{2}}=\frac{1}{2} \sec ^{2} \frac{\theta}{2} \cdot \frac{d \theta}{d x}$
$=\frac{1}{2} \sec ^{2} \frac{\theta}{2} \times \frac{1}{a \sin \theta}=\frac{\operatorname{cosec} \theta}{2 \cos ^{2} \frac{\theta}{2}}$

</details>

---

### Q27. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x^{2}+y^{2}=1$, then $\frac{d^{2} x}{d y^{2}}=$

**Options:**

- **(A)** $x^{3}$
- **(B)** $y^{3}$
- **(C)** $-\frac{1}{x^{3}}$
- **(D)** $-y^{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{1}{x^{3}}$**

**Detailed Solution:**

We have $x^{2}+y^{2}=1$
$\begin{array}{l}
2 x+2 y \frac{d y}{d x}=0 \Rightarrow 2 y \frac{d y}{d x}=-2 x \\
\frac{d y}{d x}=-\frac{x}{y} \Rightarrow \frac{d x}{d y}=-\frac{y}{x}
\end{array}$
Differentiating w.r.t. $\mathrm{y}$ we get
$\frac{d^{2} x}{d y^{2}}=\left[\frac{x(1)-y \frac{d x}{d y}}{x^{2}}\right]=-\left[\frac{x-y\left(\frac{-y}{x}\right)}{x^{2}}\right]=-\left[\frac{x^{2}+y^{2}}{x^{3}}\right]$
$=-\frac{1}{x^{3}} \quad \cdots\left[\because x^{2}+y^{2}=1\right.$, given $]$

</details>

---

### Q28. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=e^{4 x} \cos 5 x$, then $\frac{d^{2} y}{d x^{2}}$ at $x=0$ is

**Options:**

- **(A)** $-9$
- **(B)** 9
- **(C)** 8
- **(D)** $-8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-9$**

**Detailed Solution:**

Given $y=e^{4 x} \cos 5 x$
$\begin{aligned}
\therefore & \frac{\mathrm{dy}}{\mathrm{dx}}=\mathrm{e}^{4 \mathrm{x}}(-5 \sin 5 \mathrm{x})+\cos 5 \mathrm{x}\left(4 \mathrm{e}^{4 \mathrm{x}}\right) \quad=\mathrm{e}^{4 \mathrm{x}}(-5 \sin 5 \mathrm{x}+4 \cos 5 \mathrm{x}) \\
& \frac{\mathrm{d}^{2} \mathrm{y}}{\mathrm{dx}^{2}}=\left[\mathrm{e}^{4 \mathrm{x}}(-25 \cos 5 \mathrm{x}-20 \sin 5 \mathrm{x})\right]+\left[(-5 \sin 5 \mathrm{x}+4 \cos 5 \mathrm{x}) \cdot\left(4 \mathrm{e}^{4} \mathrm{x}\right)\right] \\
&\left(\frac{\mathrm{d}^{2} \mathrm{y}}{\mathrm{dx}^{2}}\right)_{\mathrm{x}=0}=-25+(4 \times 4)=-25+16=-9
\end{aligned}$

</details>

---

