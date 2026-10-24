# MHT CET Mathematics - Continuity and Differentiability

## Topic 1: Continuity

**Total Questions:** 108

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \begin{cases} \dfrac{x - e^x + \cos 2x}{x^2}, & \text{if } x \neq 0 \\ k, & \text{if } x = 0 \end{cases}$ is continuous at $x = 0$, then the value of $k$ is...

**Options:**

- **(A)** $2$
- **(B)** $-2$
- **(C)** $\dfrac{-5}{2}$
- **(D)** $\dfrac{5}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{-5}{2}$**

**Detailed Solution:**

For $f(x)$ to be continuous at $x = 0$, we must have $\lim_{x \to 0} f(x) = f(0) = k$.

$\lim_{x \to 0} \dfrac{x - e^x + \cos 2x}{x^2}$

This is a $\dfrac{0}{0}$ form. Applying L'Hopital's rule:

$\lim_{x \to 0} \dfrac{1 - e^x - 2\sin 2x}{2x}$

This is again a $\dfrac{0}{0}$ form. Applying L'Hopital's rule once more:

$\lim_{x \to 0} \dfrac{-e^x - 4\cos 2x}{2}$

Substituting $x = 0$:

$\dfrac{-e^0 - 4\cos 0}{2} = \dfrac{-1 - 4}{2} = \dfrac{-5}{2}$

Therefore, $k = \dfrac{-5}{2}$.

Answer: $\dfrac{-5}{2}$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \begin{cases} \dfrac{1 - \sin^5 x}{5 \cos^2 x} & , x < \dfrac{\pi}{2} \\ a & , \text{at } x = \dfrac{\pi}{2} \\ \dfrac{b(1 - \sin x)}{8(\pi - 2x)^2} & , x > \dfrac{\pi}{2} \end{cases}$ is continuous at $x = \dfrac{\pi}{2}$, then $\left(\dfrac{b}{a}\right)^{\frac{5}{3}} = \ldots$

**Options:**

- **(A)** $(4)^4$
- **(B)** $(64)^2$
- **(C)** $(32)^2$
- **(D)** $(16)^3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(32)^2$**

**Detailed Solution:**

For continuity at $x = \dfrac{\pi}{2}$, the left-hand limit, right-hand limit, and the function value must be equal.

Evaluating the left-hand limit:

$\lim_{x \to \pi/2^-} \dfrac{1 - \sin^5 x}{5 \cos^2 x} = \lim_{x \to \pi/2^-} \dfrac{1 - \sin^5 x}{5(1 - \sin^2 x)}$

Factoring the numerator and denominator:

$\lim_{x \to \pi/2^-} \dfrac{(1 - \sin x)(1 + \sin x + \sin^2 x + \sin^3 x + \sin^4 x)}{5(1 - \sin x)(1 + \sin x)}$

Canceling the common factor $(1 - \sin x)$ and substituting $\sin x = 1$:

$\dfrac{1 + 1 + 1 + 1 + 1}{5(1 + 1)} = \dfrac{5}{10} = \dfrac{1}{2}$

Since $f\left(\dfrac{\pi}{2}\right) = a$, we get $a = \dfrac{1}{2}$.

Evaluating the right-hand limit:

$\lim_{x \to \pi/2^+} \dfrac{b(1 - \sin x)}{8(\pi - 2x)^2}$

Substituting $x = \dfrac{\pi}{2} + h$ where $h \to 0^+$:

$\lim_{h \to 0} \dfrac{b(1 - \sin(\pi/2 + h))}{8(\pi - 2(\pi/2 + h))^2} = \lim_{h \to 0} \dfrac{b(1 - \cos h)}{8(-2h)^2}$

$\lim_{h \to 0} \dfrac{b(1 - \cos h)}{32h^2} = \dfrac{b}{32} \times \dfrac{1}{2} = \dfrac{b}{64}$

Equating the right-hand limit to $a$:

$\dfrac{b}{64} = \dfrac{1}{2} \Rightarrow b = 32$

Now, calculating the required expression:

$\left(\dfrac{b}{a}\right)^{\dfrac{5}{3}} = \left(\dfrac{32}{1/2}\right)^{\dfrac{5}{3}} = (64)^{\dfrac{5}{3}}$

$(4^3)^{\dfrac{5}{3}} = 4^5 = 1024$

From the given options, $(32)^2 = 1024$.

Answer: $(32)^2$

</details>

---

### Q3. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x) = \dfrac{12^x - 4^x - 3^x + 1}{1 - \cos 2x}$, for $x \neq 0$. If $f(x)$ is continuous at $x = 0$ and $f(0) = \dfrac{(\log a) \cdot (\log 3)}{4k}$, then the value of $a$ in terms of $k$ is:

**Options:**

- **(A)** $a = 2^{4k}$
- **(B)** $a = 2^{3k}$
- **(C)** $a = 3^{4k}$
- **(D)** $a = 4^{4k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $a = 2^{4k}$**

**Detailed Solution:**

Given $f(x) = \dfrac{12^x - 4^x - 3^x + 1}{1 - \cos 2x}$

For $f(x)$ to be continuous at $x = 0$, $f(0) = \lim_{x \to 0} f(x)$.

$\lim_{x \to 0} \dfrac{12^x - 4^x - 3^x + 1}{1 - \cos 2x} = \lim_{x \to 0} \dfrac{4^x(3^x - 1) - 1(3^x - 1)}{2 \sin^2 x}$

$= \lim_{x \to 0} \dfrac{(4^x - 1)(3^x - 1)}{2 \sin^2 x}$

Dividing the numerator and the denominator by $x^2$:

$= \lim_{x \to 0} \dfrac{1}{2} \left( \dfrac{4^x - 1}{x} \right) \left( \dfrac{3^x - 1}{x} \right) \left( \dfrac{x}{\sin x} \right)^2$

Using the standard limit $\lim_{x \to 0} \dfrac{a^x - 1}{x} = \log a$:

$= \dfrac{1}{2} (\log 4) (\log 3) (1)^2$

$= \dfrac{1}{2} (2 \log 2) (\log 3) = (\log 2) (\log 3)$

It is given that $f(0) = \dfrac{(\log a) \cdot (\log 3)}{4k}$.

Equating the two values:

$\dfrac{(\log a) \cdot (\log 3)}{4k} = (\log 2) (\log 3)$

$\log a = 4k \log 2$

$\log a = \log (2^{4k})$

$a = 2^{4k}$

Answer: $a = 2^{4k}$

</details>

---

### Q4. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \dfrac{1 - \cos\left(\dfrac{p\pi x}{2}\right)}{x^2}$ is continuous at $x = 0$ and $f(0) = \dfrac{9\pi^2}{32}$, then the value of $p$ is

**Options:**

- **(A)** $p = \pm\dfrac{3}{2}$
- **(B)** $p = \pm\dfrac{3}{4}$
- **(C)** $p = \pm\dfrac{2}{3}$
- **(D)** $p = \pm\dfrac{4}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $p = \pm\dfrac{3}{2}$**

**Detailed Solution:**

Since $f(x)$ is continuous at $x = 0$, we have $\lim_{x \to 0} f(x) = f(0)$.

$\lim_{x \to 0} \dfrac{1 - \cos\left(\dfrac{p\pi x}{2}\right)}{x^2} = \lim_{x \to 0} \dfrac{2\sin^2\left(\dfrac{p\pi x}{4}\right)}{x^2}$

$= 2 \lim_{x \to 0} \left( \dfrac{\sin\left(\dfrac{p\pi x}{4}\right)}{\dfrac{p\pi x}{4}} \right)^2 \times \left(\dfrac{p\pi}{4}\right)^2$

$= 2 \times 1 \times \dfrac{p^2\pi^2}{16} = \dfrac{p^2\pi^2}{8}$

Given $f(0) = \dfrac{9\pi^2}{32}$, we equate the limit to $f(0)$:

$\dfrac{p^2\pi^2}{8} = \dfrac{9\pi^2}{32}$

$p^2 = \dfrac{9}{4}$

$p = \pm\dfrac{3}{2}$

Answer: $p = \pm\dfrac{3}{2}$

</details>

---

### Q5. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of points of discontinuity of the function $f(x) = \dfrac{1}{\log|x^2 - 1|}$ (where $|\cdot|$ denotes the modulus function) is:

**Options:**

- **(A)** $5$
- **(B)** $4$
- **(C)** $3$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5$**

**Detailed Solution:**

For the function $f(x) = \dfrac{1}{\log|x^2 - 1|}$ to be defined and continuous, the argument of the logarithm must be strictly positive and the denominator must not be zero.

Condition 1: The argument of the logarithm must be positive.
$|x^2 - 1| > 0 \Rightarrow x^2 - 1 \neq 0 \Rightarrow x \neq \pm 1$

Condition 2: The denominator must not be zero.
$\log|x^2 - 1| \neq 0 \Rightarrow |x^2 - 1| \neq 1$

This gives two cases:
$x^2 - 1 = 1 \Rightarrow x^2 = 2 \Rightarrow x = \pm \sqrt{2}$
$x^2 - 1 = -1 \Rightarrow x^2 = 0 \Rightarrow x = 0$

The points where $f(x)$ is not defined (and hence discontinuous) are $x = 0, 1, -1, \sqrt{2}, -\sqrt{2}$.

Therefore, there are $5$ points of discontinuity.

Answer: $5$

</details>

---

### Q6. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \begin{cases} \dfrac{\tan x - \cot x}{x - \frac{\pi}{4}}, & x \neq \frac{\pi}{4} \\ a, & x = \frac{\pi}{4} \end{cases}$, then the value of $'a'$ so that $f(x)$ is continuous at $x = \pi/4$ is...

**Options:**

- **(A)** $2$
- **(B)** $4$
- **(C)** $3$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4$**

**Detailed Solution:**

For $f(x)$ to be continuous at $x = \dfrac{\pi}{4}$, we must have $f\left(\dfrac{\pi}{4}\right) = \lim_{x \to \pi/4} f(x)$.

$a = \lim_{x \to \pi/4} \dfrac{\tan x - \cot x}{x - \dfrac{\pi}{4}}$

This limit is of the $\dfrac{0}{0}$ form. Applying L'Hopital's rule:

$a = \lim_{x \to \pi/4} \dfrac{\sec^2 x + \csc^2 x}{1}$

Substituting $x = \dfrac{\pi}{4}$:

$a = \sec^2\left(\dfrac{\pi}{4}\right) + \csc^2\left(\dfrac{\pi}{4}\right)$

$a = (\sqrt{2})^2 + (\sqrt{2})^2$

$a = 2 + 2 = 4$

Answer: $4$

</details>

---

### Q7. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)$ be a function defined by $f(x)=\begin{cases}\int_0^x(|t-2|+3)\,dt, & x>4\\2x+8, & x\leq 4\end{cases}$ then $f(x)$ is ...

**Options:**

- **(A)** continuous and differentiable everywhere
- **(B)** neither continuous nor differentiable at $x=4$
- **(C)** continuous everywhere, but not differentiable at $x=4$
- **(D)** Differentiable at $x=4$, but not continuous.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) continuous everywhere, but not differentiable at $x=4$**

**Detailed Solution:**

For $x \leq 4$, $f(x) = 2x+8$.

At $x=4$, $f(4) = 2(4)+8 = 16$.

For $x > 4$, $f(x) = \int_0^x (|t-2|+3)\,dt$.

$\lim_{x \to 4^+} f(x) = \int_0^4 (|t-2|+3)\,dt = \int_0^2 (-(t-2)+3)\,dt + \int_2^4 ((t-2)+3)\,dt$

$= \int_0^2 (5-t)\,dt + \int_2^4 (t+1)\,dt$

$= \left[5t - \dfrac{t^2}{2}\right]_0^2 + \left[\dfrac{t^2}{2} + t\right]_2^4$

$= (10 - 2) + (8 + 4 - (2 + 2)) = 8 + 8 = 16$.

Since $\lim_{x \to 4^-} f(x) = \lim_{x \to 4^+} f(x) = f(4) = 16$, $f(x)$ is continuous at $x=4$.

Now, checking differentiability at $x=4$:

Left hand derivative (LHD) at $x=4$:

$f'(4^-) = \dfrac{d}{dx}(2x+8) \Big|_{x=4} = 2$.

Right hand derivative (RHD) at $x=4$:

Using Leibniz rule for $x > 4$, $f'(x) = \dfrac{d}{dx} \int_0^x (|t-2|+3)\,dt = |x-2|+3$.

$f'(4^+) = |4-2|+3 = 5$.

Since LHD $\neq$ RHD, $f(x)$ is not differentiable at $x=4$.

For all other points, $f(x)$ is defined by polynomials, hence continuous and differentiable everywhere except at $x=4$.

Answer: continuous everywhere, but not differentiable at $x=4$

</details>

---

### Q8. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function defined by
$f(x)=\begin{cases}ax^2+bx+1, & |2x-3|\geq 2\\3x+2, & \dfrac{1}{2}<x<\dfrac{5}{2}\end{cases}$
is continuous in its domain, then the values of $a$ and $b$ respectively are ...

**Options:**

- **(A)** $\dfrac{-4}{5}, \dfrac{27}{5}$
- **(B)** $\dfrac{5}{4}, -\dfrac{27}{5}$
- **(C)** $1, \dfrac{27}{5}$
- **(D)** $3, 11$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{-4}{5}, \dfrac{27}{5}$**

**Detailed Solution:**

The condition $|2x-3| \geq 2$ gives $2x-3 \leq -2$ or $2x-3 \geq 2$, which means $x \leq \dfrac{1}{2}$ or $x \geq \dfrac{5}{2}$.

For the function to be continuous in its domain, it must be continuous at the boundary points $x = \dfrac{1}{2}$ and $x = \dfrac{5}{2}$.

At $x = \dfrac{1}{2}$:

$\lim_{x \to \dfrac{1}{2}^-} f(x) = \lim_{x \to \dfrac{1}{2}^+} f(x)$

$a\left(\dfrac{1}{2}\right)^2 + b\left(\dfrac{1}{2}\right) + 1 = 3\left(\dfrac{1}{2}\right) + 2$

$\dfrac{a}{4} + \dfrac{b}{2} + 1 = \dfrac{7}{2}$

$a + 2b = 10$

At $x = \dfrac{5}{2}$:

$\lim_{x \to \dfrac{5}{2}^-} f(x) = \lim_{x \to \dfrac{5}{2}^+} f(x)$

$3\left(\dfrac{5}{2}\right) + 2 = a\left(\dfrac{5}{2}\right)^2 + b\left(\dfrac{5}{2}\right) + 1$

$\dfrac{19}{2} = \dfrac{25a}{4} + \dfrac{5b}{2} + 1$

$25a + 10b = 34$

Multiplying the first equation by $5$ gives $5a + 10b = 50$. Subtracting this from the second equation:

$20a = -16 \Rightarrow a = \dfrac{-4}{5}$

Substituting $a$ into the first equation:

$\dfrac{-4}{5} + 2b = 10 \Rightarrow 2b = 10 + \dfrac{4}{5} = \dfrac{54}{5} \Rightarrow b = \dfrac{27}{5}$

Answer: $\dfrac{-4}{5}, \dfrac{27}{5}$

</details>

---

### Q9. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the function $f(x)$ defined by $f(x) = \begin{cases} ax + 1 & \text{if } x \leq 3 \\ bx + 3 & \text{if } x > 3 \end{cases}$ is continuous at $x = 3$, then $(a - b) =$ ..........

**Options:**

- **(A)** $\dfrac{2}{3}$
- **(B)** $\dfrac{3}{2}$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2}{3}$**

**Detailed Solution:**

For the function $f(x)$ to be continuous at $x = 3$, the left-hand limit must be equal to the right-hand limit and the value of the function at $x = 3$.

$\lim_{x \to 3^-} f(x) = \lim_{x \to 3^+} f(x) = f(3)$

Evaluating the left-hand limit:

$\lim_{x \to 3^-} (ax + 1) = 3a + 1$

Evaluating the right-hand limit:

$\lim_{x \to 3^+} (bx + 3) = 3b + 3$

Equating the limits:

$3a + 1 = 3b + 3$

$3a - 3b = 2$

$3(a - b) = 2$

$a - b = \dfrac{2}{3}$

Answer: $\dfrac{2}{3}$

</details>

---

### Q10. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $[x]$ denotes the greatest integer less than or equal to x and $f(x) = [\tan^2 x]$, then which of the following is true ?

**Options:**

- **(A)** $\lim\limits_{x \to 0} f(x)$ does not exist
- **(B)** $f(x)$ is continuous at $x = 0$
- **(C)** $f(x)$ is not differentiable at $x = 0$
- **(D)** $f'(0) = 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $f(x)$ is continuous at $x = 0$**

**Detailed Solution:**

For $x \in (-\pi/4, \pi/4)$, we have $-1 < \tan x < 1$.

Squaring both sides, we get $0 \le \tan^2 x < 1$.

Therefore, $f(x) = [\tan^2 x] = 0$ for all $x \in (-\pi/4, \pi/4)$.

Since $f(x) = 0$ in a neighborhood of $x = 0$, we have $\lim\limits_{x \to 0} f(x) = 0$ and $f(0) = 0$.

Thus, $f(x)$ is continuous at $x = 0$.

Furthermore, since $f(x)$ is constant in this neighborhood, $f'(0) = 0$, meaning $f(x)$ is differentiable at $x = 0$.

Answer: $f(x)$ is continuous at $x = 0$

</details>

---

### Q11. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x) = \left(\dfrac{5x - 8}{8 - 3x}\right)^{\frac{3}{2x - 4}}$, for $x \neq 2$ is continuous at $x = 2$, then the value of $f(2)$ is...

**Options:**

- **(A)** $e^{12}$
- **(B)** $e^6$
- **(C)** $e^3$
- **(D)** $e^{\frac{3}{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $e^6$**

**Detailed Solution:**

Since $f(x)$ is continuous at $x = 2$, $f(2) = \lim_{x \to 2} f(x)$.

$f(2) = \lim_{x \to 2} \left(\dfrac{5x - 8}{8 - 3x}\right)^{\dfrac{3}{2x - 4}}$

As $x \to 2$, the base approaches $1$ and the exponent approaches $\infty$, so this is of the form $1^{\infty}$.

Using the standard limit $\lim_{x \to a} [h(x)]^{g(x)} = e^{\lim_{x \to a} g(x)[h(x) - 1]}$ for $1^{\infty}$ form:

$f(2) = e^{\lim_{x \to 2} \dfrac{3}{2x - 4} \left(\dfrac{5x - 8}{8 - 3x} - 1\right)}$

$f(2) = e^{\lim_{x \to 2} \dfrac{3}{2(x - 2)} \left(\dfrac{5x - 8 - (8 - 3x)}{8 - 3x}\right)}$

$f(2) = e^{\lim_{x \to 2} \dfrac{3}{2(x - 2)} \left(\dfrac{8x - 16}{8 - 3x}\right)}$

$f(2) = e^{\lim_{x \to 2} \dfrac{3}{2(x - 2)} \dfrac{8(x - 2)}{8 - 3x}}$

$f(2) = e^{\lim_{x \to 2} \dfrac{12}{8 - 3x}}$

Substituting $x = 2$:

$f(2) = e^{\dfrac{12}{8 - 6}} = e^6$

Answer: $e^6$

</details>

---

### Q12. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \dfrac{3^x + 3^{-x} - 2}{\tan x \cdot \log(1+x)}$ for $x \neq 0$, is continuous at $x = 0$, then the value of $f(0)$ is equal to $\ldots$

**Options:**

- **(A)** $2\log 3$
- **(B)** $(\log 3)^2$
- **(C)** $\dfrac{1}{2}\log 3$
- **(D)** $\log \dfrac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\log 3)^2$**

**Detailed Solution:**

Since $f(x)$ is continuous at $x = 0$, $f(0) = \lim_{x \to 0} f(x)$.

$f(0) = \lim_{x \to 0} \dfrac{3^x + 3^{-x} - 2}{\tan x \cdot \log(1+x)}$

$f(0) = \lim_{x \to 0} \dfrac{3^{2x} + 1 - 2 \cdot 3^x}{3^x \tan x \cdot \log(1+x)}$

$f(0) = \lim_{x \to 0} \dfrac{(3^x - 1)^2}{3^x \tan x \cdot \log(1+x)}$

Dividing the numerator and the denominator by $x^2$:

$f(0) = \lim_{x \to 0} \dfrac{\left(\dfrac{3^x - 1}{x}\right)^2}{3^x \left(\dfrac{\tan x}{x}\right) \left(\dfrac{\log(1+x)}{x}\right)}$

Using the standard limits $\lim_{x \to 0} \dfrac{a^x - 1}{x} = \log a$, $\lim_{x \to 0} \dfrac{\tan x}{x} = 1$, and $\lim_{x \to 0} \dfrac{\log(1+x)}{x} = 1$:

$f(0) = \dfrac{(\log 3)^2}{1 \cdot 1 \cdot 1} = (\log 3)^2$

Answer: $(\log 3)^2$

</details>

---

### Q13. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of point / points where the function $f(x) = \dfrac{1}{x^2-5|x|+6}$ is discontinuous is......

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $2$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4$**

**Detailed Solution:**

The function $f(x) = \dfrac{1}{x^2-5|x|+6}$ is discontinuous at the points where its denominator is zero.

$x^2 - 5|x| + 6 = 0$

Since $x^2 = |x|^2$, the equation can be written as:

$|x|^2 - 5|x| + 6 = 0$

$(|x| - 2)(|x| - 3) = 0$

$|x| = 2 \Rightarrow x = \pm 2$

$|x| = 3 \Rightarrow x = \pm 3$

The points of discontinuity are $x = -3, -2, 2, 3$.

The number of points where the function is discontinuous is $4$.

Answer: $4$

</details>

---

### Q14. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x) = \dfrac{4\sqrt{2}(\sin 3x + \sin x)}{2\sin 2x\sin\dfrac{3x}{2} + \cos\dfrac{5x}{2} - \cos\dfrac{3x}{2}}$ for $x \neq \dfrac{\pi}{2}$ is continuous at $x = \dfrac{\pi}{2}$, then the value of $f\left(\dfrac{\pi}{2}\right)$ is equal to

**Options:**

- **(A)** $(2)^2$
- **(B)** $(3)^2$
- **(C)** $4\sqrt{2}$
- **(D)** $2\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(2)^2$**

**Detailed Solution:**

Given the function:

$f(x) = \dfrac{4\sqrt{2}(\sin 3x + \sin x)}{2\sin 2x\sin\dfrac{3x}{2} + \cos\dfrac{5x}{2} - \cos\dfrac{3x}{2}}$

Using the sum-to-product formula $\sin C + \sin D = 2\sin\dfrac{C+D}{2}\cos\dfrac{C-D}{2}$, the numerator simplifies to:

$4\sqrt{2}(2\sin 2x \cos x) = 8\sqrt{2}\sin 2x \cos x$

For the denominator, using the formula $\cos C - \cos D = -2\sin\dfrac{C+D}{2}\sin\dfrac{C-D}{2}$, we get:

$\cos\dfrac{5x}{2} - \cos\dfrac{3x}{2} = -2\sin 2x \sin\dfrac{x}{2}$

Substituting this back into the denominator:

$2\sin 2x\sin\dfrac{3x}{2} - 2\sin 2x \sin\dfrac{x}{2} = 2\sin 2x \left(\sin\dfrac{3x}{2} - \sin\dfrac{x}{2}\right)$

Using the formula $\sin C - \sin D = 2\cos\dfrac{C+D}{2}\sin\dfrac{C-D}{2}$, the expression inside the parenthesis becomes:

$\sin\dfrac{3x}{2} - \sin\dfrac{x}{2} = 2\cos x \sin\dfrac{x}{2}$

So, the denominator simplifies to:

$2\sin 2x (2\cos x \sin\dfrac{x}{2}) = 4\sin 2x \cos x \sin\dfrac{x}{2}$

Now, substituting the simplified numerator and denominator back into $f(x)$:

$f(x) = \dfrac{8\sqrt{2}\sin 2x \cos x}{4\sin 2x \cos x \sin\dfrac{x}{2}}$

For $x \neq \dfrac{\pi}{2}$, we can cancel $\sin 2x \cos x$ from the numerator and denominator:

$f(x) = \dfrac{2\sqrt{2}}{\sin\dfrac{x}{2}}$

Since $f(x)$ is continuous at $x = \dfrac{\pi}{2}$, its value at this point is equal to its limit as $x \to \dfrac{\pi}{2}$:

$f\left(\dfrac{\pi}{2}\right) = \lim_{x \to \pi/2} \dfrac{2\sqrt{2}}{\sin\dfrac{x}{2}} = \dfrac{2\sqrt{2}}{\sin\dfrac{\pi}{4}} = \dfrac{2\sqrt{2}}{\dfrac{1}{\sqrt{2}}} = 4$

Therefore, $f\left(\dfrac{\pi}{2}\right) = 4 = (2)^2$.

Answer: $(2)^2$

</details>

---

### Q15. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Which of the following function is discontinuous at $x = 0$ ?

**Options:**

- **(A)** $f(x) = (1 + x)^{\frac{2}{x}},$ for $x \neq 0$
$= e^2,$ for $x = 0$
- **(B)** $f(x) = \sin x - \cos x,$ for $x \neq 0$
$= -1,$ for $x = 0$
- **(C)** $f(x) = \dfrac{e^{\frac{1}{x}} - 1}{e^{\frac{1}{x}} + 1},$ for $x \neq 0$
$= -1,$ for $x = 0$
- **(D)** $f(x) = \dfrac{e^{5x} - e^{2x}}{\sin 3x},$ for $x \neq 0$
$= 1,$ for $x = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $f(x) = \dfrac{e^{\frac{1}{x}} - 1}{e^{\frac{1}{x}} + 1},$ for $x \neq 0$
$= -1,$ for $x = 0$**

**Detailed Solution:**

Let us check the continuity of each function at $x = 0$ by evaluating the limits.

For the first function:
$\lim_{x \to 0} (1 + x)^{\dfrac{2}{x}} = e^{\lim_{x \to 0} \dfrac{2}{x} \ln(1+x)} = e^2 = f(0)$
The function is continuous at $x = 0$.

For the second function:
$\lim_{x \to 0} (\sin x - \cos x) = \sin 0 - \cos 0 = -1 = f(0)$
The function is continuous at $x = 0$.

For the third function:
Right-hand limit (RHL):
$\lim_{x \to 0^+} \dfrac{e^{\dfrac{1}{x}} - 1}{e^{\dfrac{1}{x}} + 1} = \lim_{x \to 0^+} \dfrac{1 - e^{-\dfrac{1}{x}}}{1 + e^{-\dfrac{1}{x}}} = \dfrac{1 - 0}{1 + 0} = 1$
Left-hand limit (LHL):
$\lim_{x \to 0^-} \dfrac{e^{\dfrac{1}{x}} - 1}{e^{\dfrac{1}{x}} + 1} = \dfrac{0 - 1}{0 + 1} = -1$
Since LHL $\neq$ RHL, the limit does not exist. The function is discontinuous at $x = 0$.

For the fourth function:
$\lim_{x \to 0} \dfrac{e^{5x} - e^{2x}}{\sin 3x} = \lim_{x \to 0} e^{2x} \left( \dfrac{e^{3x} - 1}{3x} \right) \left( \dfrac{3x}{\sin 3x} \right) = 1 \times 1 \times 1 = 1 = f(0)$
The function is continuous at $x = 0$.

Answer: $f(x) = \dfrac{e^{\frac{1}{x}} - 1}{e^{\frac{1}{x}} + 1},$ for $x \neq 0$
$= -1,$ for $x = 0$

</details>

---

### Q16. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function f is continuous at $x = \pi$, where $f(x) = \dfrac{1 - \cos[7(x - \pi)]}{5(x - \pi)^2}$, for $x \neq \pi$, then $f(\pi) = $

**Options:**

- **(A)** $\dfrac{49}{4}$
- **(B)** $\dfrac{4}{49}$
- **(C)** $\dfrac{49}{10}$
- **(D)** $\dfrac{10}{49}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{49}{10}$**

**Detailed Solution:**

Since the function $f(x)$ is continuous at $x = \pi$, $f(\pi) = \lim_{x \rightarrow \pi} f(x)$.

Substituting $t = x - \pi$, as $x \rightarrow \pi$, $t \rightarrow 0$.

$f(\pi) = \lim_{t \rightarrow 0} \dfrac{1 - \cos(7t)}{5t^2}$

Using the identity $1 - \cos \theta = 2 \sin^2\left(\dfrac{\theta}{2}\right)$:

$f(\pi) = \lim_{t \rightarrow 0} \dfrac{2 \sin^2\left(\dfrac{7t}{2}\right)}{5t^2}$

$f(\pi) = \dfrac{2}{5} \lim_{t \rightarrow 0} \left( \dfrac{\sin\left(\dfrac{7t}{2}\right)}{t} \right)^2$

$f(\pi) = \dfrac{2}{5} \times \left(\dfrac{7}{2}\right)^2 \lim_{t \rightarrow 0} \left( \dfrac{\sin\left(\dfrac{7t}{2}\right)}{\dfrac{7t}{2}} \right)^2$

Since $\lim_{\theta \rightarrow 0} \dfrac{\sin \theta}{\theta} = 1$:

$f(\pi) = \dfrac{2}{5} \times \dfrac{49}{4} \times 1 = \dfrac{49}{10}$

Answer: $\dfrac{49}{10}$

</details>

---

### Q17. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the derivative of the function $f(x) = \begin{cases} ax^2 + b & \text{if } x < -1 \\ bx^2 + ax + 4 & \text{if } x \geq -1 \end{cases}$ is continuous everywhere then

**Options:**

- **(A)** $a = 2, b = 3$
- **(B)** $a = 3, b = 2$
- **(C)** $a = -2, b = 3$
- **(D)** $a = -3, b = -2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $a = 2, b = 3$**

**Detailed Solution:**

For $f(x)$ to have a continuous derivative everywhere, $f(x)$ must be differentiable and hence continuous at $x = -1$.

Equating the left-hand and right-hand limits of $f(x)$ at $x = -1$:

$a(-1)^2 + b = b(-1)^2 + a(-1) + 4$

$a + b = b - a + 4$

$2a = 4 \Rightarrow a = 2$

The derivative of the function is:

$f'(x) = \begin{cases} 2ax & \text{if } x < -1 \\ 2bx + a & \text{if } x > -1 \end{cases}$

Since $f'(x)$ is continuous at $x = -1$, its left-hand and right-hand limits at $x = -1$ must be equal:

$2a(-1) = 2b(-1) + a$

$-2a = -2b + a$

$2b = 3a$

Substituting $a = 2$:

$2b = 3(2) \Rightarrow b = 3$

Answer: $a = 2, b = 3$

</details>

---

### Q18. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of f(0) so that the function $f(x) = \dfrac{(256 - 8x)^{\frac{1}{4}} - 4}{16 - 4(64 + 3x)^{\frac{1}{3}}}$, $x \neq 0$ is continuous at $x = 0$, is

**Options:**

- **(A)** $-\dfrac{1}{8}$
- **(B)** $\dfrac{1}{8}$
- **(C)** $\dfrac{1}{64}$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{8}$**

**Detailed Solution:**

For $f(x)$ to be continuous at $x = 0$, we must have $f(0) = \lim_{x \to 0} f(x)$.

$\lim_{x \to 0} \dfrac{(256 - 8x)^{\dfrac{1}{4}} - 4}{16 - 4(64 + 3x)^{\dfrac{1}{3}}}$

This is a $\dfrac{0}{0}$ indeterminate form. Applying L'Hospital's rule:

$\lim_{x \to 0} \dfrac{\dfrac{1}{4}(256 - 8x)^{-\dfrac{3}{4}} \times (-8)}{-4 \times \dfrac{1}{3}(64 + 3x)^{-\dfrac{2}{3}} \times 3}$

$= \lim_{x \to 0} \dfrac{-2(256 - 8x)^{-\dfrac{3}{4}}}{-4(64 + 3x)^{-\dfrac{2}{3}}}$

Substituting $x = 0$:

$= \dfrac{-2(256)^{-\dfrac{3}{4}}}{-4(64)^{-\dfrac{2}{3}}}$

$= \dfrac{-2(4^4)^{-\dfrac{3}{4}}}{-4(4^3)^{-\dfrac{2}{3}}}$

$= \dfrac{-2(4^{-3})}{-4(4^{-2})}$

$= \dfrac{-2 \times \dfrac{1}{64}}{-4 \times \dfrac{1}{16}}$

$= \dfrac{-\dfrac{1}{32}}{-\dfrac{1}{4}} = \dfrac{1}{8}$

Answer: $\dfrac{1}{8}$

</details>

---

### Q19. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function f is continuous at $x = 1$, where $f(x) = \dfrac{1 + \cos(\pi x)}{\pi(1-x)^2}$, for $x \neq 1$, then the value of $f(1)$ is....

**Options:**

- **(A)** $\dfrac{\pi}{2}$
- **(B)** $\dfrac{\pi}{4}$
- **(C)** $\dfrac{\pi}{6}$
- **(D)** $\dfrac{\pi}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\pi}{2}$**

**Detailed Solution:**

Since $f(x)$ is continuous at $x = 1$, $f(1) = \lim_{x \rightarrow 1} f(x)$.

$f(1) = \lim_{x \rightarrow 1} \dfrac{1 + \cos(\pi x)}{\pi(1-x)^2}$

This is a $\dfrac{0}{0}$ form. Applying L'Hospital's rule:

$f(1) = \lim_{x \rightarrow 1} \dfrac{-\pi \sin(\pi x)}{-2\pi(1-x)}$

$f(1) = \lim_{x \rightarrow 1} \dfrac{\sin(\pi x)}{2(1-x)}$

This is again a $\dfrac{0}{0}$ form. Applying L'Hospital's rule once more:

$f(1) = \lim_{x \rightarrow 1} \dfrac{\pi \cos(\pi x)}{-2}$

Substituting $x = 1$:

$f(1) = \dfrac{\pi \cos(\pi)}{-2} = \dfrac{\pi(-1)}{-2} = \dfrac{\pi}{2}$

Answer: $\dfrac{\pi}{2}$

</details>

---

### Q20. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)$ is continuous at $x = 0$, where $f(x) = \dfrac{8^x - 2^x}{k^x - 1}$, for $x \neq 0$ and $f(0) = 2$, then the value of $k$ is ...

**Options:**

- **(A)** $0$
- **(B)** $4$
- **(C)** $-2$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2$**

**Detailed Solution:**

Since $f(x)$ is continuous at $x = 0$, we must have $\lim_{x \to 0} f(x) = f(0)$.

$\lim_{x \to 0} \dfrac{8^x - 2^x}{k^x - 1} = 2$

Dividing the numerator and the denominator by $x$:

$\lim_{x \to 0} \dfrac{\dfrac{8^x - 1}{x} - \dfrac{2^x - 1}{x}}{\dfrac{k^x - 1}{x}} = 2$

Using the standard limit $\lim_{x \to 0} \dfrac{a^x - 1}{x} = \ln a$:

$\dfrac{\ln 8 - \ln 2}{\ln k} = 2$

$\dfrac{\ln \left(\dfrac{8}{2}\right)}{\ln k} = 2$

$\dfrac{\ln 4}{\ln k} = 2$

$\ln 4 = 2 \ln k$

$\ln 4 = \ln(k^2)$

$k^2 = 4$

Since $k > 0$ for the exponential function $k^x$ to be defined for all real $x$, we get $k = 2$.

</details>

---

### Q21. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \begin{cases} \dfrac{(8 - 2x)^{\frac{1}{3}} - 2}{3 - (243 + 5x)^{\frac{1}{5}}}, & \text{if } x \neq 0 \\ k, & \text{if } x = 0 \end{cases}$ is continuous at $x = 0$, then $k =$

**Options:**

- **(A)** $\dfrac{5}{2}$
- **(B)** $-\dfrac{5}{2}$
- **(C)** $\dfrac{27}{2}$
- **(D)** $\dfrac{-27}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{27}{2}$**

**Detailed Solution:**

Since the function $f(x)$ is continuous at $x = 0$, we have $k = \lim_{x \to 0} f(x)$.

$k = \lim_{x \to 0} \dfrac{(8 - 2x)^{1/3} - 2}{3 - (243 + 5x)^{1/5}}$

This is a $\dfrac{0}{0}$ form. Applying L'Hospital's Rule, we differentiate the numerator and the denominator with respect to $x$:

$k = \lim_{x \to 0} \dfrac{\dfrac{1}{3}(8 - 2x)^{-2/3}(-2)}{-\dfrac{1}{5}(243 + 5x)^{-4/5}(5)}$

Substituting $x = 0$ into the expression:

$k = \dfrac{\dfrac{1}{3}(8)^{-2/3}(-2)}{-(243)^{-4/5}}$

$k = \dfrac{-\dfrac{2}{3} \times \dfrac{1}{4}}{-\dfrac{1}{81}}$

$k = \dfrac{-\dfrac{1}{6}}{-\dfrac{1}{81}}$

$k = \dfrac{81}{6} = \dfrac{27}{2}$

</details>

---

### Q22. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the function f be defined by $f(x) = \dfrac{x - |x|}{x}$, for $x \neq 0$ and $f(0) = 2$ then f is

**Options:**

- **(A)** continuous nowhere
- **(B)** continuous for all $x$ except at $x = 0$
- **(C)** continuous everywhere
- **(D)** continuous for all $x$ except at $x = 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) continuous for all $x$ except at $x = 0$**

**Detailed Solution:**

Given $f(x) = \dfrac{x - |x|}{x}$ for $x \neq 0$ and $f(0) = 2$

For $x > 0$, $|x| = x$, so $f(x) = \dfrac{x - x}{x} = 0$

For $x < 0$, $|x| = -x$, so $f(x) = \dfrac{x - (-x)}{x} = \dfrac{2x}{x} = 2$

Left-hand limit at $x = 0$ is $\lim_{x \to 0^-} f(x) = 2$

Right-hand limit at $x = 0$ is $\lim_{x \to 0^+} f(x) = 0$

Since $\lim_{x \to 0^-} f(x) \neq \lim_{x \to 0^+} f(x)$, the function is discontinuous at $x = 0$.

For $x \neq 0$, the function is constant ($0$ for $x > 0$ and $2$ for $x < 0$), hence it is continuous for all $x \neq 0$.

Thus, $f(x)$ is continuous for all $x$ except at $x = 0$.

Answer: continuous for all $x$ except at $x = 0$

</details>

---

### Q23. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the function $f(x)$ be defined as:
$f(x) = \begin{cases} \left[\tan\left(\dfrac{\pi}{4} + x\right)\right]^{\dfrac{1}{x}}, & x \neq 0 \\ k, & x = 0 \end{cases}$
If $f(x)$ is continuous at $x = 0$, then the value of $k$ is...

**Options:**

- **(A)** $e$
- **(B)** $e^2$
- **(C)** $\dfrac{1}{e^2}$
- **(D)** $\dfrac{1}{e}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $e^2$**

**Detailed Solution:**

For $f(x)$ to be continuous at $x = 0$, we must have $f(0) = \lim_{x \to 0} f(x)$.

$k = \lim_{x \to 0} \left[\tan\left(\dfrac{\pi}{4} + x\right)\right]^{\dfrac{1}{x}}$

This limit is of the form $1^{\infty}$. Using the standard limit $\lim_{x \to a} f(x)^{g(x)} = e^{\lim_{x \to a} g(x)(f(x) - 1)}$, we get:

$k = e^{\lim_{x \to 0} \dfrac{1}{x} \left[ \tan\left(\dfrac{\pi}{4} + x\right) - 1 \right]}$

Using the identity $\tan\left(\dfrac{\pi}{4} + x\right) = \dfrac{1 + \tan x}{1 - \tan x}$, we have:

$\tan\left(\dfrac{\pi}{4} + x\right) - 1 = \dfrac{1 + \tan x}{1 - \tan x} - 1 = \dfrac{2\tan x}{1 - \tan x}$

Substituting this back into the limit:

$k = e^{\lim_{x \to 0} \dfrac{1}{x} \left( \dfrac{2\tan x}{1 - \tan x} \right)}$

$k = e^{\lim_{x \to 0} \left( \dfrac{\tan x}{x} \right) \left( \dfrac{2}{1 - \tan x} \right)}$

Since $\lim_{x \to 0} \dfrac{\tan x}{x} = 1$ and $\lim_{x \to 0} \tan x = 0$, we get:

$k = e^{1 \times \dfrac{2}{1 - 0}} = e^2$

Answer: $e^2$

</details>

---

### Q24. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)= \begin{cases}-2 \sin x & , \quad x \leqslant-\frac{\pi}{2} \\ a \sin x+\mathrm{b} & , \quad \frac{-\pi}{2} < x < \frac{\pi}{2} \\ \cos x & , \quad x \geqslant \frac{\pi}{2}\end{cases}$ is continuous at $\mathrm{x}=\frac{-\pi}{2}$ and $x=\frac{\pi}{2}$, then the value of $2 a+\mathrm{b}$ is

**Options:**

- **(A)** $-1$
- **(B)** $1$
- **(C)** $0$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-1$**

**Detailed Solution:**

For the function to be continuous at $x = -\dfrac{\pi}{2}$, the left-hand limit must equal the right-hand limit:

$\lim_{x \to -\dfrac{\pi}{2}^{-}} f(x) = \lim_{x \to -\dfrac{\pi}{2}^{+}} f(x)$

$-2 \sin\left(-\dfrac{\pi}{2}\right) = a \sin\left(-\dfrac{\pi}{2}\right) + b$

$-2(-1) = a(-1) + b$

$-a + b = 2$

For the function to be continuous at $x = \dfrac{\pi}{2}$, the left-hand limit must equal the right-hand limit:

$\lim_{x \to \dfrac{\pi}{2}^{-}} f(x) = \lim_{x \to \dfrac{\pi}{2}^{+}} f(x)$

$a \sin\left(\dfrac{\pi}{2}\right) + b = \cos\left(\dfrac{\pi}{2}\right)$

$a(1) + b = 0$

$a + b = 0$

Adding the two equations $-a + b = 2$ and $a + b = 0$ gives:

$2b = 2 \Rightarrow b = 1$

Substituting $b = 1$ into $a + b = 0$ gives:

$a + 1 = 0 \Rightarrow a = -1$

The value of $2a + b$ is:

$2(-1) + 1 = -2 + 1 = -1$

Answer: $-1$

</details>

---

### Q25. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}(x)= \begin{cases}\frac{x^4-5 x^2+4}{|(x-1)(x-2)|} & , x \neq 1,2 \\ 6 & , x=1 \\ 12 & , x=2\end{cases}$ then $\mathrm{f}(x)$ is continuous on the set

**Options:**

- **(A)** $\mathbb{R}-\{1\}$
- **(B)** $\mathbb{R}-\{2\}$
- **(C)** $\mathbb{R}$
- **(D)** $\mathbb{R}-\{1,2\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathbb{R}-\{1,2\}$**

**Detailed Solution:**

For $x \neq 1, 2$, the function can be simplified by factoring the numerator:

$\mathrm{f}(x) = \dfrac{x^4 - 5x^2 + 4}{|(x-1)(x-2)|} = \dfrac{(x^2-1)(x^2-4)}{|(x-1)(x-2)|} = \dfrac{(x-1)(x+1)(x-2)(x+2)}{|(x-1)(x-2)|}$

Let us check the continuity at $x = 1$ by evaluating the left-hand limit (LHL) and right-hand limit (RHL).

For $x \to 1^-$, we have $x < 1$, which means $(x-1) < 0$ and $(x-2) < 0$. Thus, $(x-1)(x-2) > 0$, and $|(x-1)(x-2)| = (x-1)(x-2)$.

$\lim_{x \to 1^-} \mathrm{f}(x) = \lim_{x \to 1^-} (x+1)(x+2) = (1+1)(1+2) = 6$

For $x \to 1^+$, we have $1 < x < 2$, which means $(x-1) > 0$ and $(x-2) < 0$. Thus, $(x-1)(x-2) < 0$, and $|(x-1)(x-2)| = -(x-1)(x-2)$.

$\lim_{x \to 1^+} \mathrm{f}(x) = \lim_{x \to 1^+} -(x+1)(x+2) = -(1+1)(1+2) = -6$

Since $\lim_{x \to 1^-} \mathrm{f}(x) \neq \lim_{x \to 1^+} \mathrm{f}(x)$, the limit does not exist at $x=1$. Therefore, $\mathrm{f}(x)$ is discontinuous at $x=1$.

Now, let us check the continuity at $x = 2$.

For $x \to 2^-$, we have $1 < x < 2$, so $(x-1)(x-2) < 0$, and $|(x-1)(x-2)| = -(x-1)(x-2)$.

$\lim_{x \to 2^-} \mathrm{f}(x) = \lim_{x \to 2^-} -(x+1)(x+2) = -(2+1)(2+2) = -12$

For $x \to 2^+$, we have $x > 2$, so $(x-1)(x-2) > 0$, and $|(x-1)(x-2)| = (x-1)(x-2)$.

$\lim_{x \to 2^+} \mathrm{f}(x) = \lim_{x \to 2^+} (x+1)(x+2) = (2+1)(2+2) = 12$

Since $\lim_{x \to 2^-} \mathrm{f}(x) \neq \lim_{x \to 2^+} \mathrm{f}(x)$, the limit does not exist at $x=2$. Therefore, $\mathrm{f}(x)$ is discontinuous at $x=2$.

For all other real values of $x$, the function is a composition of continuous functions and the denominator is non-zero, making it continuous.

Thus, $\mathrm{f}(x)$ is continuous on the set $\mathbb{R}-\{1,2\}$.

Answer: $\mathbb{R}-\{1,2\}$

</details>

---

### Q26. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The function $\mathrm{f}(x)=2 x-\left|x-x^2\right|$ is

**Options:**

- **(A)** continuous at $x=1$.
- **(B)** discontinuous at $x=1$.
- **(C)** not defined at $x=1$.
- **(D)** discontinuous at $x=0$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) continuous at $x=1$.**

**Detailed Solution:**

The given function is $\mathrm{f}(x) = 2x - \left|x - x^2\right|$.

We know that polynomial functions are continuous everywhere. Therefore, $2x$ and $x - x^2$ are continuous for all $x \in \mathbb{R}$.

The absolute value function is also continuous everywhere, which implies that $\left|x - x^2\right|$ is continuous for all $x \in \mathbb{R}$.

Since the difference of two continuous functions is continuous, $\mathrm{f}(x)$ is continuous for all $x \in \mathbb{R}$.

Let us verify the continuity at $x = 1$:

$\mathrm{f}(1) = 2(1) - \left|1 - 1^2\right| = 2 - 0 = 2$

$\lim_{x \to 1} \mathrm{f}(x) = \lim_{x \to 1} \left(2x - \left|x - x^2\right|\right) = 2(1) - \left|1 - 1^2\right| = 2$

Since $\lim_{x \to 1} \mathrm{f}(x) = \mathrm{f}(1)$, the function is continuous at $x = 1$.

Answer: continuous at $x=1$.

</details>

---

### Q27. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function $\mathrm{f}(x)=\left\{\begin{array}{ccc}x+a \sqrt{2} \sin x & \text { if } & 0 \leq x \leq \frac{\pi}{4} \\ 2 x \cot x+\mathrm{b} & \text { if } & \frac{\pi}{4} < x \leq \frac{\pi}{2} \\ a \cos 2 x-\mathrm{bsin} x & \text { if } & \frac{\pi}{2} < x \leq \pi\end{array}\right.$ is continuous in $[0, \pi]$ then $a-b=$

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{12}$
- **(C)** $\frac{5 \pi}{12}$
- **(D)** $\frac{7 \pi}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}$**

**Detailed Solution:**

For the function to be continuous in $[0, \pi]$, it must be continuous at $x = \dfrac{\pi}{4}$ and $x = \dfrac{\pi}{2}$.

At $x = \dfrac{\pi}{4}$, the left-hand limit is:

$\lim_{x \to \dfrac{\pi}{4}^-} f(x) = \dfrac{\pi}{4} + a \sqrt{2} \sin\left(\dfrac{\pi}{4}\right) = \dfrac{\pi}{4} + a \sqrt{2} \left(\dfrac{1}{\sqrt{2}}\right) = \dfrac{\pi}{4} + a$

The right-hand limit at $x = \dfrac{\pi}{4}$ is:

$\lim_{x \to \dfrac{\pi}{4}^+} f(x) = 2\left(\dfrac{\pi}{4}\right) \cot\left(\dfrac{\pi}{4}\right) + b = \dfrac{\pi}{2}(1) + b = \dfrac{\pi}{2} + b$

Equating the left-hand limit and right-hand limit for continuity at $x = \dfrac{\pi}{4}$:

$\dfrac{\pi}{4} + a = \dfrac{\pi}{2} + b$

$a - b = \dfrac{\pi}{2} - \dfrac{\pi}{4}$

$a - b = \dfrac{\pi}{4}$

Answer: $\frac{\pi}{4}$

</details>

---

### Q28. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\mathrm{f}(x)= \begin{cases}{\left[x^2\right]-\left[-x^2\right],} & x \neq 3 \\ \mathrm{k} & , x=3\end{cases}$
is continuous at $x=3$, then $\mathrm{k}=$ where $[\cdot]$ is greatest integer function

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $-1$
- **(D)** No choice of \(k\) makes \(f(x)\) continuous at \(x=3\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) No choice of \(k\) makes \(f(x)\) continuous at \(x=3\)**

**Detailed Solution:**

For the function $f(x)$ to be continuous at $x=3$, the left-hand limit (LHL) and right-hand limit (RHL) at $x=3$ must exist and be equal to $f(3) = k$.

Evaluating the left-hand limit as $x \rightarrow 3^-$:
As $x \rightarrow 3^-$, $x^2 \rightarrow 9^-$. This means $x^2$ is slightly less than $9$ (e.g., $8.99$).
Therefore, $[x^2] = 8$ and $[-x^2] = -9$.
$\lim_{x \rightarrow 3^-} f(x) = 8 - (-9) = 17$

Evaluating the right-hand limit as $x \rightarrow 3^+$:
As $x \rightarrow 3^+$, $x^2 \rightarrow 9^+$. This means $x^2$ is slightly greater than $9$ (e.g., $9.01$).
Therefore, $[x^2] = 9$ and $[-x^2] = -10$.
$\lim_{x \rightarrow 3^+} f(x) = 9 - (-10) = 19$

Since $\lim_{x \rightarrow 3^-} f(x) \neq \lim_{x \rightarrow 3^+} f(x)$, the limit $\lim_{x \rightarrow 3} f(x)$ does not exist.

Thus, no choice of $k$ can make $f(x)$ continuous at $x=3$.

Answer: No choice of \(k\) makes \(f(x)\) continuous at \(x=3\)

</details>

---

### Q29. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(\mathrm{x})=\left\{\begin{array}{ll}\mathrm{m} x+1, & x \leq \frac{\pi}{2} \\ \sin x+\mathrm{n}, & x>\frac{\pi}{2}\end{array}\right.$, is continuous at $x=\frac{\pi}{2},(\mathrm{~m}, \mathrm{n} \in \mathbb{R})$
then

**Options:**

- **(A)** $\mathrm{m}=1, \mathrm{n}=0$
- **(B)** $\mathrm{m}=\frac{\mathrm{n} \pi}{2}$
- **(C)** $\mathrm{m}=\mathrm{n}=\frac{\pi}{2}$
- **(D)** $\mathrm{n}=\frac{\mathrm{m} \pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{n}=\frac{\mathrm{m} \pi}{2}$**

**Detailed Solution:**

Given $f(x)$ is continuous at $x = \dfrac{\pi}{2}$.

$\lim_{x \to \dfrac{\pi}{2}^-} f(x) = \lim_{x \to \dfrac{\pi}{2}^+} f(x) = f\left(\dfrac{\pi}{2}\right)$

$\lim_{x \to \dfrac{\pi}{2}^-} (mx + 1) = m\left(\dfrac{\pi}{2}\right) + 1 = \dfrac{m\pi}{2} + 1$

$\lim_{x \to \dfrac{\pi}{2}^+} (\sin x + n) = \sin\left(\dfrac{\pi}{2}\right) + n = 1 + n$

Equating the left hand limit and right hand limit:

$\dfrac{m\pi}{2} + 1 = 1 + n$

$n = \dfrac{m\pi}{2}$

Answer: $\mathrm{n}=\frac{\mathrm{m} \pi}{2}$

</details>

---

### Q30. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)$ is continuous at point $x=0$ where
$\mathrm{f}(x)=\left\{\begin{array}{cl}\frac{3 \sin x+5 \tan x}{a^x-1} & , x < 0 \\ \frac{2}{\log 2} & , x=0 \\ \frac{8 x+2 x \cos x}{\mathbf{b}^x-1} & , x>0\end{array}\right.$
then the values of $a$ and b , respectively, are

**Options:**

- **(A)** 4,5
- **(B)** 16,32
- **(C)** 8,10
- **(D)** 16,16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 16,32**

**Detailed Solution:**

Since $\mathrm{f}(x)$ is continuous at $x=0$, we have $\lim_{x \to 0^-} \mathrm{f}(x) = \lim_{x \to 0^+} \mathrm{f}(x) = \mathrm{f}(0)$.

Evaluating the left-hand limit:

$\lim_{x \to 0^-} \dfrac{3 \sin x + 5 \tan x}{a^x - 1}$

Dividing the numerator and denominator by $x$:

$\lim_{x \to 0^-} \dfrac{3 \left(\dfrac{\sin x}{x}\right) + 5 \left(\dfrac{\tan x}{x}\right)}{\dfrac{a^x - 1}{x}} = \dfrac{3(1) + 5(1)}{\log a} = \dfrac{8}{\log a}$

Equating this to $\mathrm{f}(0)$:

$\dfrac{8}{\log a} = \dfrac{2}{\log 2} \Rightarrow \log a = 4 \log 2 = \log 16 \Rightarrow a = 16$

Evaluating the right-hand limit:

$\lim_{x \to 0^+} \dfrac{8 x + 2 x \cos x}{b^x - 1}$

Dividing the numerator and denominator by $x$:

$\lim_{x \to 0^+} \dfrac{8 + 2 \cos x}{\dfrac{b^x - 1}{x}} = \dfrac{8 + 2(1)}{\log b} = \dfrac{10}{\log b}$

Equating this to $\mathrm{f}(0)$:

$\dfrac{10}{\log b} = \dfrac{2}{\log 2} \Rightarrow \log b = 5 \log 2 = \log 32 \Rightarrow b = 32$

Thus, $a = 16$ and $b = 32$.

Answer: 16,32

</details>

---

### Q31. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function f defined on $\left(\frac{\pi}{6}, \frac{\pi}{3}\right)$ by
$f(x)=\left\{\begin{array}{cc}
\frac{\sqrt{2} \cos x-1}{\cot x-1}, & x \neq \frac{\pi}{4} \\
\mathrm{k}, & x=\frac{\pi}{4}
\end{array}\right.$
is continuous, then k is equal to

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** 2
- **(C)** 1
- **(D)** $\frac{1}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

Since the function is continuous at $x = \dfrac{\pi}{4}$, we have $k = \lim_{x \to \pi/4} f(x)$.

$k = \lim_{x \to \pi/4} \dfrac{\sqrt{2} \cos x - 1}{\cot x - 1}$

This limit is of the form $\dfrac{0}{0}$. Using L'Hospital's rule, we differentiate the numerator and the denominator with respect to $x$:

$k = \lim_{x \to \pi/4} \dfrac{-\sqrt{2} \sin x}{-\csc^2 x}$

$k = \lim_{x \to \pi/4} \sqrt{2} \sin^3 x$

Substituting $x = \dfrac{\pi}{4}$:

$k = \sqrt{2} \left(\dfrac{1}{\sqrt{2}}\right)^3$

$k = \sqrt{2} \times \dfrac{1}{2\sqrt{2}} = \dfrac{1}{2}$

Answer: $\frac{1}{2}$

</details>

---

### Q32. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}(x)=\frac{1-\tan x}{4 x-\pi}, x \neq \frac{\pi}{4}, x \in\left[0, \frac{\pi}{2}\right]$. $f(x)$ is continuous in $\left[0, \frac{\pi}{2}\right]$, then $\mathrm{f}\left(\frac{\pi}{4}\right)$ is

**Options:**

- **(A)** $-\frac{1}{2}$
- **(B)** $\frac{1}{2}$
- **(C)** 1
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\frac{1}{2}$**

**Detailed Solution:**

Since $\mathrm{f}(x)$ is continuous at $x = \dfrac{\pi}{4}$, we have:

$\mathrm{f}\left(\dfrac{\pi}{4}\right) = \lim_{x \to \dfrac{\pi}{4}} \mathrm{f}(x)$

$\mathrm{f}\left(\dfrac{\pi}{4}\right) = \lim_{x \to \dfrac{\pi}{4}} \dfrac{1 - \tan x}{4x - \pi}$

This is in the $\dfrac{0}{0}$ form. Applying L'Hopital's rule, we differentiate the numerator and the denominator with respect to $x$:

$\mathrm{f}\left(\dfrac{\pi}{4}\right) = \lim_{x \to \dfrac{\pi}{4}} \dfrac{-\sec^2 x}{4}$

Substituting $x = \dfrac{\pi}{4}$:

$\mathrm{f}\left(\dfrac{\pi}{4}\right) = \dfrac{-\sec^2\left(\dfrac{\pi}{4}\right)}{4}$

$\mathrm{f}\left(\dfrac{\pi}{4}\right) = \dfrac{-(\sqrt{2})^2}{4}$

$\mathrm{f}\left(\dfrac{\pi}{4}\right) = \dfrac{-2}{4} = -\dfrac{1}{2}$

Answer: $-\frac{1}{2}$

</details>

---

### Q33. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If the function $f(x)= \begin{cases}-2 \sin x & \text {, if } x \leq \frac{-\pi}{2} \\ A \sin x+B & , \text { if } \frac{-\pi}{2} \lt x \lt \frac{\pi}{2} \\ \cos x & , \text { if } x \geq \frac{\pi}{2}\end{cases}$ is continuous everywhere, then the values of A and B are respectively

**Options:**

- **(A)** $1,-1$.
- **(B)** $-1,1$.
- **(C)** 1,1 .
- **(D)** $-1,-1$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-1,1$.**

**Detailed Solution:**

For $f(x)$ to be continuous everywhere, it must be continuous at the points where the definition of the function changes, i.e., at $x = \dfrac{-\pi}{2}$ and $x = \dfrac{\pi}{2}$.

For continuity at $x = \dfrac{-\pi}{2}$:
$\lim_{x \to \dfrac{-\pi}{2}^{-}} f(x) = \lim_{x \to \dfrac{-\pi}{2}^{+}} f(x)$

$-2 \sin\left(\dfrac{-\pi}{2}\right) = A \sin\left(\dfrac{-\pi}{2}\right) + B$

$-2(-1) = A(-1) + B$

$-A + B = 2$

For continuity at $x = \dfrac{\pi}{2}$:
$\lim_{x \to \dfrac{\pi}{2}^{-}} f(x) = \lim_{x \to \dfrac{\pi}{2}^{+}} f(x)$

$A \sin\left(\dfrac{\pi}{2}\right) + B = \cos\left(\dfrac{\pi}{2}\right)$

$A(1) + B = 0$

$A + B = 0$

Adding the two equations:
$(-A + B) + (A + B) = 2 + 0$

$2B = 2 \Rightarrow B = 1$

Substituting $B = 1$ into $A + B = 0$:
$A + 1 = 0 \Rightarrow A = -1$

Therefore, the values of $A$ and $B$ are $-1$ and $1$ respectively.

Answer: $-1,1$.

</details>

---

### Q34. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}(x)=\left\{\begin{array}{cc}\frac{1-\cos 4 x}{x^2} & , x \lt 0 \\ \mathrm{a} & , x=0 \\ \frac{\sqrt{x}}{\sqrt{16+\sqrt{x}}-4} & , x\gt0 .\end{array}\right.$
If $\mathrm{f}(x)$ is continuous at $x=0$, then the value of a is

**Options:**

- **(A)** 8
- **(B)** 4
- **(C)** $12$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 8**

**Detailed Solution:**

For the function to be continuous at $x=0$, the left-hand limit, right-hand limit, and the value of the function at $x=0$ must be equal.

$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} \dfrac{1-\cos 4x}{x^2}$

Using the identity $1-\cos \theta = 2\sin^2\left(\dfrac{\theta}{2}\right)$:

$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} \dfrac{2\sin^2 2x}{x^2} = 2 \lim_{x \to 0^-} \left(\dfrac{\sin 2x}{2x} \times 2\right)^2 = 2 \times 4 = 8$

Evaluating the right-hand limit:

$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \dfrac{\sqrt{x}}{\sqrt{16+\sqrt{x}}-4}$

Rationalizing the denominator:

$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \dfrac{\sqrt{x}(\sqrt{16+\sqrt{x}}+4)}{(\sqrt{16+\sqrt{x}}-4)(\sqrt{16+\sqrt{x}}+4)}$

$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \dfrac{\sqrt{x}(\sqrt{16+\sqrt{x}}+4)}{16+\sqrt{x}-16}$

$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \dfrac{\sqrt{x}(\sqrt{16+\sqrt{x}}+4)}{\sqrt{x}}$

$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} (\sqrt{16+\sqrt{x}}+4) = \sqrt{16+0}+4 = 8$

Since $\lim_{x \to 0^-} f(x) = \lim_{x \to 0^+} f(x) = f(0)$, we get $a = 8$.

Answer: 8

</details>

---

### Q35. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\left\{\begin{array}{cc}\frac{\mathrm{a}}{2}(x-|x|), & \text { for } x \lt 0 \\ 0, & \text { for } x=0 \\ b x^2 \sin \left(\frac{1}{x}\right), & \text { for } x\gt0\end{array}\right.$ is continuous at $x=0$, then

**Options:**

- **(A)** a is any real value and b is any real value
- **(B)** $a$ is only rational value and $b$ is any real value
- **(C)** a is only irrational value and b is any real value
- **(D)** a is only rational value and b is only rational value

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) a is any real value and b is any real value**

**Detailed Solution:**

For $x < 0$, $|x| = -x$.

$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} \dfrac{a}{2}(x - (-x)) = \lim_{x \to 0^-} ax = 0$

This limit is $0$ for any real value of $a$.

For $x > 0$, $f(x) = bx^2 \sin\left(\dfrac{1}{x}\right)$.

$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} bx^2 \sin\left(\dfrac{1}{x}\right)$

Since $-1 \le \sin\left(\dfrac{1}{x}\right) \le 1$, the term $\sin\left(\dfrac{1}{x}\right)$ is bounded. As $x \to 0^+$, $x^2 \to 0$.

$\lim_{x \to 0^+} bx^2 \sin\left(\dfrac{1}{x}\right) = 0$

This limit is $0$ for any real value of $b$.

Since $\lim_{x \to 0^-} f(x) = \lim_{x \to 0^+} f(x) = f(0) = 0$ for all real $a$ and $b$, the function is continuous at $x = 0$ for any real values of $a$ and $b$.

Answer: a is any real value and b is any real value

</details>

---

### Q36. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The values of $a$ and $b$, so that the function
$\mathrm{f}(x)= \begin{cases}x+\mathrm{a} \sqrt{2} \sin x & , 0 \leq x \leq \dfrac{\pi}{4} \\ 2 x \cot x+\mathrm{b} & , \dfrac{\pi}{4} \leq x \leq \dfrac{\pi}{2} \\ \mathrm{a} \cos 2 x-\mathrm{b} \sin x & , \dfrac{\pi}{2} \lt x \leq \pi\end{cases}$
is continuous for $0 \leq x \leq \pi$, are respectively given by

**Options:**

- **(A)** $+\dfrac{\pi}{12},-\dfrac{\pi}{6}$
- **(B)** $-\dfrac{\pi}{6},-\dfrac{\pi}{12}$
- **(C)** $\dfrac{\pi}{6}, \dfrac{\pi}{12}$
- **(D)** $\dfrac{\pi}{6},-\dfrac{\pi}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\pi}{6},-\dfrac{\pi}{12}$**

**Detailed Solution:**

For the function to be continuous in $0 \leq x \leq \pi$, it must be continuous at $x = \dfrac{\pi}{4}$ and $x = \dfrac{\pi}{2}$.

For continuity at $x = \dfrac{\pi}{4}$:

$\lim_{x \to \dfrac{\pi}{4}^{-}} f(x) = \lim_{x \to \dfrac{\pi}{4}^{+}} f(x)$

$\dfrac{\pi}{4} + a \sqrt{2} \sin\left(\dfrac{\pi}{4}\right) = 2\left(\dfrac{\pi}{4}\right) \cot\left(\dfrac{\pi}{4}\right) + b$

$\dfrac{\pi}{4} + a = \dfrac{\pi}{2} + b$

$a - b = \dfrac{\pi}{4}$

For continuity at $x = \dfrac{\pi}{2}$:

$\lim_{x \to \dfrac{\pi}{2}^{-}} f(x) = \lim_{x \to \dfrac{\pi}{2}^{+}} f(x)$

$2\left(\dfrac{\pi}{2}\right) \cot\left(\dfrac{\pi}{2}\right) + b = a \cos\left(2 \times \dfrac{\pi}{2}\right) - b \sin\left(\dfrac{\pi}{2}\right)$

$b = -a - b$

$a = -2b$

Substituting $a = -2b$ into $a - b = \dfrac{\pi}{4}$:

$-2b - b = \dfrac{\pi}{4}$

$-3b = \dfrac{\pi}{4} \Rightarrow b = -\dfrac{\pi}{12}$

Substituting $b = -\dfrac{\pi}{12}$ into $a = -2b$:

$a = -2\left(-\dfrac{\pi}{12}\right) = \dfrac{\pi}{6}$

The values of $a$ and $b$ are $\dfrac{\pi}{6}$ and $-\dfrac{\pi}{12}$ respectively.

Answer: $\dfrac{\pi}{6},-\dfrac{\pi}{12}$

</details>

---

### Q37. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{f}(x)=x\left[\dfrac{x}{2}\right]$, for $-10 \lt x \lt 10$, where $[\mathrm{t}]$ denotes the greatest integer function. Then the number of points of discontinuity of $f$ is equal to

**Options:**

- **(A)** 10
- **(B)** 9
- **(C)** 6
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 8**

**Detailed Solution:**

The given function is $f(x) = x \left[ \dfrac{x}{2} \right]$ for $x \in (-10, 10)$.

The greatest integer function $\left[ \dfrac{x}{2} \right]$ is discontinuous at all points where $\dfrac{x}{2}$ is an integer.

Let $\dfrac{x}{2} = k$, where $k \in \mathbb{Z}$. Then $x = 2k$.

For $x \in (-10, 10)$, the possible points of discontinuity are $x = -8, -6, -4, -2, 0, 2, 4, 6, 8$.

Checking the continuity at $x = 2k$:

Left hand limit (LHL) at $x = 2k$:
$\lim_{x \to 2k^-} f(x) = \lim_{x \to 2k^-} x \left[ \dfrac{x}{2} \right] = 2k(k - 1) = 2k^2 - 2k$

Right hand limit (RHL) at $x = 2k$:
$\lim_{x \to 2k^+} f(x) = \lim_{x \to 2k^+} x \left[ \dfrac{x}{2} \right] = 2k(k) = 2k^2$

For $f(x)$ to be continuous at $x = 2k$, the LHL must equal the RHL:
$2k^2 - 2k = 2k^2$
$-2k = 0 \implies k = 0$

Thus, $f(x)$ is continuous at $k = 0$, which corresponds to $x = 0$.

For all other values of $k \in \{-4, -3, -2, -1, 1, 2, 3, 4\}$, the function is discontinuous.

Therefore, the points of discontinuity are $x = -8, -6, -4, -2, 2, 4, 6, 8$.

The number of points of discontinuity is $8$.

Answer: 8

</details>

---

### Q38. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let k be a non-zero real number.
If $\mathrm{f}(x)=\left\{\begin{array}{cc}\dfrac{\left(\mathrm{e}^x-1\right)^2}{\sin \left(\dfrac{x}{\mathrm{k}}\right) \log \left(1+\dfrac{x}{4}\right)} & , x \neq 0 \\ 12 & , x=0\end{array}\right.$
is a continuous function, then the value of $k$ is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 4
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

For the function to be continuous at $x = 0$, we must have $\lim_{x \to 0} f(x) = f(0)$.

Given $f(0) = 12$, we evaluate the limit:

$\lim_{x \to 0} \dfrac{(e^x - 1)^2}{\sin\left(\dfrac{x}{k}\right) \log\left(1 + \dfrac{x}{4}\right)}$

Dividing the numerator and the denominator by $x^2$, we get:

$\lim_{x \to 0} \dfrac{\left(\dfrac{e^x - 1}{x}\right)^2}{\left[\dfrac{\sin\left(\dfrac{x}{k}\right)}{x}\right] \left[\dfrac{\log\left(1 + \dfrac{x}{4}\right)}{x}\right]}$

Multiplying and dividing the terms in the denominator to use standard limits:

$\lim_{x \to 0} \dfrac{\left(\dfrac{e^x - 1}{x}\right)^2}{\dfrac{1}{k}\left[\dfrac{\sin\left(\dfrac{x}{k}\right)}{\dfrac{x}{k}}\right] \cdot \dfrac{1}{4}\left[\dfrac{\log\left(1 + \dfrac{x}{4}\right)}{\dfrac{x}{4}}\right]}$

Using the standard limits $\lim_{x \to 0} \dfrac{e^x - 1}{x} = 1$, $\lim_{x \to 0} \dfrac{\sin x}{x} = 1$, and $\lim_{x \to 0} \dfrac{\log(1 + x)}{x} = 1$, we get:

$= \dfrac{1^2}{\left(\dfrac{1}{k} \cdot 1\right) \cdot \left(\dfrac{1}{4} \cdot 1\right)} = 4k$

Equating the limit to the function value at $x = 0$:

$4k = 12$

$k = 3$

Answer: 3

</details>

---

### Q39. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\dfrac{x+x^2+x^3+\ldots \ldots \ldots \ldots+x^{\mathrm{n}}-\mathrm{n}}{x-1}$, for $x \neq 1$ is continuous at $x=1$, then $\mathrm{f}(1)=$

**Options:**

- **(A)** $\dfrac{\mathrm{n}(\mathrm{n}+1)(4 \mathrm{n}-1)}{6}$
- **(B)** $\dfrac{\mathrm{n}(\mathrm{n}+1)}{2}$
- **(C)** $\dfrac{\mathrm{n}(\mathrm{n}+1)(2 \mathrm{n}+1)}{6}$
- **(D)** $\dfrac{\mathrm{n}(2 \mathrm{n}+1)}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\mathrm{n}(\mathrm{n}+1)}{2}$**

**Detailed Solution:**

Since $\mathrm{f}(x)$ is continuous at $x=1$, we have $\mathrm{f}(1) = \lim_{x \to 1} \mathrm{f}(x)$.

$\mathrm{f}(1) = \lim_{x \to 1} \dfrac{x+x^2+x^3+\ldots+x^{\mathrm{n}}-\mathrm{n}}{x-1}$

This is a $\dfrac{0}{0}$ indeterminate form. Applying L'Hospital's rule:

$\mathrm{f}(1) = \lim_{x \to 1} \dfrac{\dfrac{d}{dx}(x+x^2+x^3+\ldots+x^{\mathrm{n}}-\mathrm{n})}{\dfrac{d}{dx}(x-1)}$

$\mathrm{f}(1) = \lim_{x \to 1} \dfrac{1+2x+3x^2+\ldots+\mathrm{n}x^{\mathrm{n}-1}}{1}$

Substituting $x=1$:

$\mathrm{f}(1) = 1+2+3+\ldots+\mathrm{n}$

$\mathrm{f}(1) = \dfrac{\mathrm{n}(\mathrm{n}+1)}{2}$

Answer: $\dfrac{\mathrm{n}(\mathrm{n}+1)}{2}$

</details>

---

### Q40. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $a, b \in \mathbb{R}$ ($a \neq 0$). If the function $f$ is defined as

$f(x) = \begin{cases} \dfrac{2x^2}{a} & , 0 \leq x < 1 \\ a & , 1 \leq x < \sqrt{2} \\ \dfrac{2b^2 - 4b}{x^3} & , \sqrt{2} \leq x < \infty \end{cases}$

is continuous in the interval $[0, \infty)$, then an ordered pair $(a, b)$ is

**Options:**

- **(A)** $(-\sqrt{2}, 1-\sqrt{3})$
- **(B)** $(\sqrt{2},-1+\sqrt{3})$
- **(C)** $(\sqrt{2}, 1-\sqrt{3})$
- **(D)** $(-\sqrt{2}, 1+\sqrt{3})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(\sqrt{2}, 1-\sqrt{3})$**

**Detailed Solution:**

For the function $f(x)$ to be continuous in $[0, \infty)$, it must be continuous at $x = 1$ and $x = \sqrt{2}$.

Continuity at $x = 1$:

$\lim_{x \to 1^-} f(x) = \lim_{x \to 1^+} f(x) = f(1)$

$\lim_{x \to 1^-} \dfrac{2x^2}{a} = \dfrac{2}{a}$

Since $f(1) = a$, we have $\dfrac{2}{a} = a \Rightarrow a^2 = 2 \Rightarrow a = \pm \sqrt{2}$.

Continuity at $x = \sqrt{2}$:

$\lim_{x \to \sqrt{2}^-} f(x) = \lim_{x \to \sqrt{2}^+} f(x) = f(\sqrt{2})$

$\lim_{x \to \sqrt{2}^-} a = a$

$\lim_{x \to \sqrt{2}^+} \dfrac{2b^2 - 4b}{x^3} = \dfrac{2b^2 - 4b}{(\sqrt{2})^3} = \dfrac{2b^2 - 4b}{2\sqrt{2}} = \dfrac{b^2 - 2b}{\sqrt{2}}$

Equating the limits, we get $a = \dfrac{b^2 - 2b}{\sqrt{2}} \Rightarrow b^2 - 2b = a\sqrt{2}$.

Case 1: $a = \sqrt{2}$

$b^2 - 2b = (\sqrt{2})(\sqrt{2}) = 2$

$b^2 - 2b - 2 = 0$

$b = \dfrac{2 \pm \sqrt{4 - 4(1)(-2)}}{2} = \dfrac{2 \pm 2\sqrt{3}}{2} = 1 \pm \sqrt{3}$

Case 2: $a = -\sqrt{2}$

$b^2 - 2b = (-\sqrt{2})(\sqrt{2}) = -2$

$b^2 - 2b + 2 = 0$

The discriminant is $D = 4 - 8 = -4 < 0$, which gives no real values for $b$.

Thus, the possible ordered pairs $(a, b)$ are $(\sqrt{2}, 1+\sqrt{3})$ and $(\sqrt{2}, 1-\sqrt{3})$.

From the given options, $(\sqrt{2}, 1-\sqrt{3})$ is the correct choice.

Answer: $(\sqrt{2}, 1-\sqrt{3})$

</details>

---

### Q41. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function $\mathrm{f}(x)=\left(\dfrac{5 x-8}{8-3 x}\right)^{\dfrac{3}{2 x-4}}$ if $x \neq 2$. $=\mathrm{k} \quad$ if $x=2$. is continuous at $x=2$, then $\mathrm{k}=$

**Options:**

- **(A)** $e^6$
- **(B)** $\mathrm{e}^2$
- **(C)** $\mathrm{e}^{-6}$
- **(D)** $\mathrm{e}^{-2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $e^6$**

**Detailed Solution:**

For the function to be continuous at $x=2$, we must have $k = \lim_{x \to 2} f(x)$.

$k = \lim_{x \to 2} \left(\dfrac{5x-8}{8-3x}\right)^{\dfrac{3}{2x-4}}$

This limit is of the form $1^{\infty}$. Using the standard limit formula $\lim_{x \to a} f(x)^{g(x)} = e^{\lim_{x \to a} (f(x)-1)g(x)}$, we get:

$k = e^{\lim_{x \to 2} \left(\dfrac{5x-8}{8-3x} - 1\right) \left(\dfrac{3}{2x-4}\right)}$

$k = e^{\lim_{x \to 2} \left(\dfrac{5x-8-8+3x}{8-3x}\right) \left(\dfrac{3}{2(x-2)}\right)}$

$k = e^{\lim_{x \to 2} \left(\dfrac{8x-16}{8-3x}\right) \left(\dfrac{3}{2(x-2)}\right)}$

$k = e^{\lim_{x \to 2} \left(\dfrac{8(x-2)}{8-3x}\right) \left(\dfrac{3}{2(x-2)}\right)}$

$k = e^{\lim_{x \to 2} \dfrac{12}{8-3x}}$

Substituting $x = 2$:

$k = e^{\dfrac{12}{8-6}} = e^6$

Answer: $e^6$

</details>

---

### Q42. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}(x)=\dfrac{1-\tan x}{4 x-\pi}, x \neq \dfrac{\pi}{4}, x \in\left[0, \dfrac{1}{2}\right], \quad \mathrm{f}(x)$ is continuous in $\left[0, \dfrac{\pi}{2}\right)$, then $f\left(\dfrac{\pi}{4}\right)$ is

**Options:**

- **(A)** $-\dfrac{1}{2}$
- **(B)** $\dfrac{1}{2}$
- **(C)** 1
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\dfrac{1}{2}$**

**Detailed Solution:**

For the function to be continuous at $x = \dfrac{\pi}{4}$, the value of the function at $x = \dfrac{\pi}{4}$ must be equal to its limit as $x$ approaches $\dfrac{\pi}{4}$.

$f\left(\dfrac{\pi}{4}\right) = \lim_{x \rightarrow \pi/4} \dfrac{1-\tan x}{4x-\pi}$

Since substituting $x = \dfrac{\pi}{4}$ gives a $\dfrac{0}{0}$ form, applying L'Hopital's rule by differentiating the numerator and the denominator with respect to $x$:

$f\left(\dfrac{\pi}{4}\right) = \lim_{x \rightarrow \pi/4} \dfrac{-\sec^2 x}{4}$

Substituting $x = \dfrac{\pi}{4}$:

$f\left(\dfrac{\pi}{4}\right) = \dfrac{-\sec^2(\pi/4)}{4} = \dfrac{-(\sqrt{2})^2}{4} = -\dfrac{2}{4} = -\dfrac{1}{2}$

Answer: $-\dfrac{1}{2}$

</details>

---

### Q43. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $k$, for which the function
$f(x)= \begin{cases}\left(\dfrac{4}{5}\right)^{\dfrac{\tan 4 x}{\tan 5 x}} & , 0 \lt x \lt \dfrac{\pi}{2} \\ \mathrm{k}+\dfrac{2}{5} & , x=\dfrac{\pi}{2}\end{cases}$
is continuous at $x=\dfrac{\pi}{2}$, is

**Options:**

- **(A)** $\dfrac{17}{20}$
- **(B)** $\dfrac{3}{5}$
- **(C)** $-\dfrac{2}{5}$
- **(D)** $\dfrac{2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3}{5}$**

**Detailed Solution:**

For the function $f(x)$ to be continuous at $x = \dfrac{\pi}{2}$, we must have:

$\lim_{x \to \dfrac{\pi}{2}^-} f(x) = f\left(\dfrac{\pi}{2}\right)$

First, we evaluate the limit of the exponent as $x \to \dfrac{\pi}{2}^-$. Let $x = \dfrac{\pi}{2} - h$, where $h \to 0^+$:

$\lim_{x \to \dfrac{\pi}{2}^-} \dfrac{\tan 4x}{\tan 5x} = \lim_{h \to 0^+} \dfrac{\tan\left(4\left(\dfrac{\pi}{2} - h\right)\right)}{\tan\left(5\left(\dfrac{\pi}{2} - h\right)\right)}$

$\Rightarrow \lim_{h \to 0^+} \dfrac{\tan(2\pi - 4h)}{\tan\left(\dfrac{5\pi}{2} - 5h\right)}$

Using trigonometric identities, $\tan(2\pi - \theta) = -\tan \theta$ and $\tan\left(\dfrac{5\pi}{2} - \theta\right) = \cot \theta$:

$\Rightarrow \lim_{h \to 0^+} \dfrac{-\tan 4h}{\cot 5h} = \lim_{h \to 0^+} (-\tan 4h \tan 5h)$

As $h \to 0^+$, both $\tan 4h \to 0$ and $\tan 5h \to 0$. Thus:

$\lim_{h \to 0^+} (-\tan 4h \tan 5h) = 0$

Now, substituting this back into the limit of the function:

$\lim_{x \to \dfrac{\pi}{2}^-} f(x) = \left(\dfrac{4}{5}\right)^0 = 1$

We are given that $f\left(\dfrac{\pi}{2}\right) = k + \dfrac{2}{5}$. Equating the limit to the function value:

$k + \dfrac{2}{5} = 1$

$k = 1 - \dfrac{2}{5} = \dfrac{3}{5}$

Answer: $\dfrac{3}{5}$

</details>

---

### Q44. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The function $\mathrm{f}$ defined on $\left(-\frac{1}{3}, \frac{1}{3}\right)$ by
$\mathrm{f}(x)=\left\{\begin{array}{cc}
\frac{1}{x} \log \left(\frac{1+3 x}{1-2 x}\right), & x \neq 0 \\
\mathrm{k} & , \quad x=0
\end{array}\right.$
is continuous at $x=0$, then $\mathrm{k}$ is

**Options:**

- **(A)** 6
- **(B)** 1
- **(C)** 5
- **(D)** -5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5**

**Detailed Solution:**

$\mathrm{f}$ is continuous at $x=0$.
$\begin{aligned}
\therefore \quad \mathrm{f}(0) & =\lim _{x \rightarrow 0} \mathrm{f}(x) \\
\therefore \quad \mathrm{k} & =\lim _{x \rightarrow 0}\left(\frac{1}{x} \log (1+3 x)-\frac{1}{x} \log (1-2 x)\right) \\
& =\lim _{x \rightarrow 0}\left(\frac{3 \log (1+3 x)}{3 x}+\frac{2 \log (1-2 x)}{-2 x}\right) \\
& =3+2=5
\end{aligned}$

</details>

---

### Q45. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The function $\mathrm{f}(x)=[x] \cdot \cos \left(\frac{2 x-1}{2}\right) \pi$, where $[\cdot]$ denotes the greatest integer function, is discontinuous at

**Options:**

- **(A)** (A) all irrational numbers $x$.
- **(B)** no $x$.
- **(C)** all integer points.
- **(D)** every rational $x$ which is not an integer.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) all integer points.**

**Detailed Solution:**

Greatest integer function is discontinuous on integer values.
$\therefore \quad \mathrm{f}(x)$ is discontinuous at all integer points.

</details>

---

### Q46. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The c.d.f. $\mathrm{F}(x)$ associated with p.d.f. $\mathrm{f}(x)$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/oTT94zRgqcR_vXsybdI_OcslR_BTQVKlRs5oHlNAzeQ.original.fullsize.png">

is

**Options:**

- **(A)** (A) $\quad \mathrm{F}(x)=4 x^3+3 x^4$
- **(B)** $\mathrm{F}(x)=4 x^3-3 x^4$
- **(C)** $\mathrm{F}(x)=-4 x^3-3 x^4$
- **(D)** $\mathrm{F}(x)=-4 x^3+3 x^4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{F}(x)=4 x^3-3 x^4$**

**Detailed Solution:**

$\begin{aligned} \mathrm{F}(x) & =\int_0^x 12 x^2(1-x) \mathrm{d} x \\ & =12 \int_0^x\left(x^2-x^3\right) \mathrm{d} x \\ & =12\left[\frac{x^3}{3}-\frac{x^4}{4}\right]_0^x \\ & =12\left[\frac{x^3}{3}-\frac{x^4}{4}\right] \\ & =4 x^3-3 x^4\end{aligned}$

</details>

---

### Q47. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)$ is continuous on its domain $[-2,2]$, where
$$
\mathrm{f}(x)= \begin{cases}\frac{\sin a x}{x}+3 & , \text { for }-2 \leq x < 0 \\ 2 x+7 & , \text { for } 0 \leq x \leq 1 \\ \sqrt{x^2+8}-\mathrm{b}, & \text { for } 1 < x \leq 2\end{cases}
$$
then the value of $2 a+3 b$ is

**Options:**

- **(A)** $-12$
- **(B)** $-10$
- **(C)** 10
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-10$**

**Detailed Solution:**

Since $\mathrm{f}(x)$ is continuous in $[-2,2]$, it is continuous at $x=0$ and $x=1$.
$\therefore \quad \lim _{x \rightarrow 0^{-}} \mathrm{f}(x)=\lim _{x \rightarrow 0^{+}} \mathrm{f}(x)$
$\Rightarrow \lim _{x \rightarrow 0^{-}}\left(\frac{\sin a x}{x}+3\right)=\lim _{x \rightarrow 0^{+}}(2 x+7)$
$\begin{aligned} & \Rightarrow a+3=0+7 \\ & \Rightarrow a=4\end{aligned}$
Also, $\lim _{x \rightarrow 1^{-}} \mathrm{f}(x)=\lim _{x \rightarrow 1^{+}} \mathrm{f}(x)$
$\Rightarrow \lim _{x \rightarrow 1^{-}}(2 x+7)=\lim _{x \rightarrow 1^{+}}\left(\sqrt{x^2+8}-b\right)$
$\begin{aligned} & \Rightarrow 2(1)+7=\sqrt{1+8}-b \\ & \Rightarrow 9=3-b \\ & \Rightarrow b=-6\end{aligned}$
$\therefore \quad 2 a+3 b=8-18=-10$

</details>

---

### Q48. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If a continuous random variable $\mathrm{X}$ has probability density function $\mathrm{f}(x)$ given by
$$
f(x)=\left\{\begin{array}{cc}
a x & , \text { if } 0 \leq x < 1 \\
a & , \text { if } 1 \leq x < 2 \\
3 a-a x & \text { if } 2 \leq x \leq 3 \\
0 & \text {, otherwise }
\end{array},\right.
$$
then a has the value

**Options:**

- **(A)** $\frac{1}{5}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{1}{2}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

Since $\mathrm{f}(x)$ is the p.d.f. of $\mathrm{X}$,
$$
\begin{aligned}
& \int_{-\infty}^{\infty} \mathrm{f}(x) \mathrm{d} x=1 \\
& \Rightarrow \int_0^1 \mathrm{a} x \mathrm{~d} x+\int_1^2 \mathrm{ad} x+\int_2^3(3 \mathrm{a}-\mathrm{ax}) \mathrm{d} x=1 \\
& \Rightarrow \mathrm{a}\left[\frac{x^2}{2}\right]_0^1+\mathrm{a}[x]_1^2+\left[3 \mathrm{a} x-\frac{\mathrm{a} x^2}{2}\right]_2^3=1
\end{aligned}
$$
$\begin{aligned} & \Rightarrow \mathrm{a}\left(\frac{1}{2}\right)+\mathrm{a}(1)+\left(\frac{9 \mathrm{a}}{2}-4 \mathrm{a}\right)=1 \\ & \Rightarrow 2 \mathrm{a}=1 \\ & \Rightarrow \mathrm{a}=\frac{1}{2}\end{aligned}$

</details>

---

### Q49. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The function $\mathrm{f}(\mathrm{t})=\frac{1}{\mathrm{t}^2+\mathrm{t}-2}$ where $\mathrm{t}=\frac{1}{x-1}$ is discontinuous at

**Options:**

- **(A)** $-2,1$
- **(B)** $2, \frac{1}{2}$
- **(C)** $\frac{1}{2}, 1$
- **(D)** 2,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2, \frac{1}{2}$**

**Detailed Solution:**

$$
f(t)=\frac{1}{t^2+t-2}=\frac{1}{(t+2)(t-1)}
$$
$\mathrm{f}(\mathrm{t})$ is not defined at $\mathrm{t}=-2$ and $\mathrm{t}=1$.
$$
\begin{aligned}
& \mathrm{t}=-2 \\
& \Rightarrow \frac{1}{x-1}=-2 \\
& \Rightarrow x=\frac{1}{2} \\
& \mathrm{t}=1 \\
& \Rightarrow \frac{1}{x-1}=1 \\
& \Rightarrow x=2
\end{aligned}
$$
$\therefore \quad$ The function $\mathrm{f}(\mathrm{t})$ is discontinuous at $x=\frac{1}{2}$ and $x=2$.

</details>

---

### Q50. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given $\mathrm{f}(x)=\left\{\begin{array}{cc}\frac{1-\cos 4 x}{x^2} & , \text { if } x < 0 \\ \mathrm{a} & , \text { if } x=0 \\ \frac{\sqrt{x}}{\sqrt{16-\sqrt{x}-4}}, & \text { if } x>0\end{array}\right.$
If $\mathrm{f}(x)$ is continuous at $x=0$, then value of $\mathrm{a}$ is

**Options:**

- **(A)** $-8$
- **(B)** $2$
- **(C)** $-2$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $8$**

**Detailed Solution:**

As $\mathrm{f}(x)$ is continuous at $x=0$, we get
$$
\begin{array}{ll} 
& \lim _{x \rightarrow 0^{-}} \mathrm{f}(x)=\mathrm{a}=\lim _{x \rightarrow 0^{+}} \mathrm{f}(x) \\
\therefore \quad & \lim _{x \rightarrow 0^{-}} \mathrm{f}(x)=\mathrm{a} \\
\therefore \quad & \lim _{x \rightarrow 0} \frac{1-\cos 4 x}{x^2}=\mathrm{a} \\
\therefore \quad & \lim _{x \rightarrow 0} 4 \frac{2 \sin ^2 2 x}{(2 x)^2}=\mathrm{a} \\
\therefore \quad & 8=\mathrm{a}
\end{array}
$$

</details>

---

### Q51. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The values of $a$ and $b$, so that the function
$$
f(x)=\left\{\begin{array}{l}
x+\mathrm{a} \sqrt{2} \sin x, 0 \leq x \leq \frac{\pi}{4} \\
2 x \cot x+\mathrm{b}, \frac{\pi}{4} \leq x \leq \frac{\pi}{2} \\
\operatorname{acos} 2 x-\mathrm{b} \sin x, \frac{\pi}{2} < x \leq \pi
\end{array}\right.
$$
is continuous for $0 \leq x \leq \pi$, are respectively given by

**Options:**

- **(A)** $-\frac{\pi}{12}, \frac{\pi}{6}$
- **(B)** $-\frac{\pi}{6},-\frac{\pi}{12}$
- **(C)** $\frac{\pi}{6}, \frac{\pi}{12}$
- **(D)** $\frac{\pi}{6},-\frac{\pi}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{6},-\frac{\pi}{12}$**

**Detailed Solution:**

As the given function is continuous at $x=\frac{\pi}{4}$ and $\frac{\pi}{2}$, we get
$$
\begin{array}{ll} 
& \lim _{x \rightarrow \frac{\pi^{-}}{4}} \mathrm{f}(x)=\lim _{x \rightarrow \frac{\pi^{+}}{4}} \mathrm{f}(x) \\
\therefore \quad & \lim _{x \rightarrow \frac{\pi}{4}}(x+\mathrm{a} \sqrt{2} \sin x)=\lim _{x \rightarrow \frac{\pi}{4}}(2 x \cot x+\mathrm{b}) \\
\therefore \quad & \frac{\pi}{4}+\mathrm{a}=\frac{2 \pi}{4}+\mathrm{b} \\
\therefore \quad & \mathrm{a}-\mathrm{b}=\frac{\pi}{4} \\
& \text { Also, } \lim _{x \rightarrow \frac{\pi^{-}}{2}} \mathrm{f}(x)=\lim _{x \rightarrow \frac{\pi^{+}}{2}} \mathrm{f}(x) \\
& \lim _{x \rightarrow \frac{\pi}{2}} 2 x \cot x+\mathrm{b}=\lim _{x \rightarrow \frac{\pi}{2}} \mathrm{a} \cos 2 x-\mathrm{b} \sin x \\
\therefore \quad & 0+\mathrm{b}=-\mathrm{a}-\mathrm{b} . \\
\therefore \quad & \mathrm{a}+2 \mathrm{~b}=0
\end{array}
$$
Solving equations (i) and (ii), we get $a=\frac{\pi}{6}$ and $b=\frac{-\pi}{12}$

</details>

---

### Q52. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}:[-1,2] \rightarrow[0, \infty)$ be a continuous function such that $\mathrm{f}(x)=\mathrm{f}(1-x), \forall x \in[-1,2]$
Let $\mathrm{R}_1=\int_{-1}^2 x \mathrm{f}(x) \mathrm{d} x$ and $\mathrm{R}_2$ be the area of the region bounded by $y=\mathrm{f}(x), x=-1, x=2$ and the $\mathrm{X}$-axis, then $\mathrm{R}_2$ is

**Options:**

- **(A)** $\frac{1}{2} R_1$
- **(B)** $2 R_1$
- **(C)** $3 R_1$
- **(D)** $\frac{1}{3} R_1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 R_1$**

**Detailed Solution:**

Given that $\mathrm{f}(x)=\mathrm{f}(1-x)$ and $\mathrm{R}_1=\int_{-1}^2 x \mathrm{f}(x) \mathrm{d} x$
$\begin{aligned}
& \therefore \quad \mathrm{R}_1=\int_{-1}^2(1-x) \mathrm{f}(1-x) \mathrm{d} x \\
& \quad \cdots\left[\because \int_{\mathrm{a}}^{\mathrm{b}} \mathrm{f}(x) \mathrm{d} x=\int_1^b \mathrm{f}(\mathrm{a}+\mathrm{b}-x) \mathrm{d} x\right]
\end{aligned}$
$\mathrm{R}_1=\int_{-1}^2 \mathrm{f}(x) \mathrm{d} x-\int_{-1}^2 x \mathrm{f}(x) \mathrm{d} x$
... $[\because f(x)=f(1-x)]$
$\therefore \quad \mathrm{R}_1=\int_{-1}^2 \mathrm{f}(x) \overline{\mathrm{d} x}-\mathrm{R}_1$
$\therefore \quad 2 \mathrm{R}_1=\int_{-1}^2 \mathrm{f}(x) \mathrm{d} x$
Note that $\mathrm{R}_2=\int_{-1}^2 \mathrm{f}(x) \mathrm{d} x=2 \mathrm{R}_1$

</details>

---

### Q53. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Nz5t-CR-SHXa5od01rK9GxGZCsg9tBz9ci_5ZltmmwE.original.fullsize.png">

Is continuous at $x=3$, then the value of $\mathrm{a}-\mathrm{b}$ is

**Options:**

- **(A)** $-1$
- **(B)** $0$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2$**

**Detailed Solution:**

If $x < 3$, then
$\frac{x-3}{|x-3|}+\mathrm{a}=\frac{x-3}{-(x-3)}+\mathrm{a}=\mathrm{a}-1$
If $x>3$, then $\frac{|x-3|}{x-3}+\mathrm{b}=\frac{x-3}{x-3}+\mathrm{b}=1+\mathrm{b}$
$\therefore \quad$ Given function can be written as
$\mathrm{f}(x)=\left\{\begin{array}{l}
\mathrm{a}-1, x < 3 \\
\mathrm{a}+\mathrm{b}, x=3 \\
1+\mathrm{b}, x>3
\end{array}\right.$
As $\mathrm{f}(x)$ is continuous at $x=3$, we get
$\begin{array}{ll} 
& \lim _{x \rightarrow 3^{-}} \mathrm{f}(x)=\mathrm{f}(3) \text { and } \lim _{x \rightarrow 3^{+}} \mathrm{f}(x)=\mathrm{f}(3) \\
\therefore \quad & \mathrm{a}-1=\mathrm{a}+\mathrm{b} \quad \text { and } 1+\mathrm{b}=\mathrm{a}+\mathrm{b} \\
\therefore \quad & \mathrm{b}=-1 \quad \text { and } \mathrm{a}=1 \\
\therefore \quad & \mathrm{a}-\mathrm{b}=2
\end{array}$

</details>

---

### Q54. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(x)=\left\{\begin{array}{ll}\frac{\sqrt{1+\mathrm{m} x}-\sqrt{1-\mathrm{m} x}}{x} & ,-1 \leq x < 0 \\ \frac{2 x+1}{x-2} & , 0 \leq x \leq 1\end{array}\right.$ is continuous in the interval $[-1,1]$, then $\mathrm{m}$ is equal to

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $-\frac{1}{2}$
- **(C)** $-1$
- **(D)** $-\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{1}{2}$**

**Detailed Solution:**

Since $\mathrm{f}(x)$ is continuous in $[-1,1]$, it is continuous at $x=0$.
$$
\begin{aligned}
\therefore \quad & \lim _{x \rightarrow 0^{-}} \mathrm{f}(x)=\lim _{x \rightarrow 0^{+}} \mathrm{f}(x) \\
& \Rightarrow \lim _{x \rightarrow 0} \frac{\sqrt{1+\mathrm{m} x}-\sqrt{1-\mathrm{m} x}}{x}=\lim _{x \rightarrow 0} \frac{2 x+1}{x-2} \\
& \Rightarrow \lim _{x \rightarrow 0} \frac{(1+\mathrm{m} x-1+\mathrm{m} x)}{x(\sqrt{1+\mathrm{m} x}+\sqrt{1-\mathrm{m} x})}=\frac{2(0)+1}{0-2} \\
& \Rightarrow \frac{2 \mathrm{~m}}{1+1}=\frac{1}{-2} \\
& \Rightarrow \mathrm{m}=\frac{-1}{2}
\end{aligned}
$$

</details>

---

### Q55. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}(x)=\frac{4}{x^4}\left[1-\cos \frac{x}{2}-\cos \frac{x}{4}+\cos \frac{x}{2} \cdot \cos \frac{x}{4}\right]$ is continuous at $x=0$, then $\mathrm{f}(0)$ is

**Options:**

- **(A)** $\frac{1}{32}$
- **(B)** $\frac{1}{16}$
- **(C)** $\frac{1}{8}$
- **(D)** $\frac{1}{64}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{64}$**

**Detailed Solution:**

$\begin{aligned}
f(x) & =\frac{4}{x^4}\left[1-\cos \frac{x}{2}-\cos \frac{x}{4}+\cos \frac{x}{2} \cdot \cos \frac{x}{4}\right] \\
& =\frac{4}{x^4}\left[\left(1-\cos \frac{x}{2}\right)-\cos \frac{x}{4}\left(1-\cos \frac{x}{2}\right)\right] \\
& =\frac{4}{x^4}\left[\left(1-\cos \frac{x}{2}\right)\left(1-\cos \frac{x}{4}\right)\right]
\end{aligned}$
$\mathrm{f}(x)$ is continuous at $x=0...[Given]$.
$\begin{aligned}
\therefore(0) & =\lim _{x \rightarrow 0} \mathrm{f}(x) \\
& =\lim _{x \rightarrow 0} \frac{4}{x^4}\left(1-\cos \frac{x}{2}\right)\left(1-\cos \frac{x}{4}\right) \\
& =4 \lim _{x \rightarrow 0}\left(\frac{2 \sin ^2 \frac{x}{4}}{x^2}\right) \times\left(\frac{2 \sin ^2 \frac{x}{8}}{x^2}\right) \\
& =16 \lim _{x \rightarrow 0}\left(\frac{\sin ^2 \frac{x}{4}}{\frac{x^2}{16}}\right) \times \frac{1}{16} \times \lim _{x \rightarrow 0}\left(\frac{\sin ^2 \frac{x}{8}}{\frac{x^2}{64}}\right) \times \frac{1}{64} \\
& =16 \times \frac{1}{16} \times \frac{1}{64} \lim _{x \rightarrow 0}\left(\frac{\sin \frac{x}{4}}{\frac{x}{4}}\right)^2 \times \lim _{x \rightarrow 0}\left(\frac{\sin \frac{x}{8}}{\frac{x}{8}}\right)^2 \\
& =\frac{1}{64} \times 1 \times 1 \\
& =\frac{1}{64}
\end{aligned}$

</details>

---

### Q56. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the function $\mathrm{f}(x)$ is continuous in $0 \leq x \leq \pi$, then the value of $2 a+3 b$ is where
$f(x)= \begin{cases}x+a \sqrt{2} \sin x & \text { if } 0 \leq x < \frac{\pi}{4} \\ 2 x \cot x+b & \text { if } \frac{\pi}{4} \leq x \leq \frac{\pi}{2} \\ a \cos 2 x-b \sin x & \text { if } \frac{\pi}{2} < x \leq \pi\end{cases}$

**Options:**

- **(A)** $\frac{\pi}{12}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $\frac{\pi}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{12}$**

**Detailed Solution:**

$\mathrm{f}(x)$ is continuous in $0 \leq x \leq \pi$
$\therefore \quad \mathrm{f}(x)$ is continuous at $x=\frac{\pi}{4}$.
$\begin{aligned}
\therefore \quad & \lim _{x \rightarrow \frac{\pi^{-}}{4}} \mathrm{f}(x)=\lim _{x \rightarrow \frac{\pi^{+}}{4}} \mathrm{f}(x) \\
& \Rightarrow \lim _{x \rightarrow \frac{\pi}{4}^{-}}(x+\mathrm{a} \sqrt{2} \sin x)=\lim _{x \rightarrow \frac{\pi^{+}}{4}}(2 x \cot x+\mathrm{b}) \\
& \Rightarrow \frac{\pi}{4}+\mathrm{a} \sqrt{2} \times \sin \frac{\pi}{4}=2 \times \frac{\pi}{4} \cdot \cot \frac{\pi}{4}+\mathrm{b} \\
& \Rightarrow \frac{\pi}{4}+\mathrm{a}=\frac{\pi}{2}+\mathrm{b} \\
& \Rightarrow \mathrm{a}-\mathrm{b}=\frac{\pi}{4}... (i)
\end{aligned}$
Also, $\mathrm{f}(x)$ is continuous at $x=\frac{\pi}{2}$.
$\begin{aligned}
\therefore \quad & \lim _{x \rightarrow \frac{\pi^{-}}{2}} \mathrm{f}(x)=\lim _{x \rightarrow \frac{\pi^{+}}{2}} \mathrm{f}(x) \\
& \Rightarrow \lim _{x \rightarrow \frac{\pi^{-}}{2}}(2 x \cot x+\mathrm{b})=\lim _{x \rightarrow \frac{\pi^{+}}{2}}(\mathrm{a} \cos 2 x-\mathrm{b} \sin x) \\
& \Rightarrow 2 \times \frac{\pi}{2} \times \cot \frac{\pi}{2}+\mathrm{b}=\mathrm{a} \cos \left(2 \times \frac{\pi}{2}\right)-\mathrm{b} \sin \frac{\pi}{2} \\
& \Rightarrow \mathrm{b}=-\mathrm{a}-\mathrm{b} \\
& \Rightarrow \mathrm{a}=-2 \mathrm{~b}
\end{aligned}$
Substituting $a=-2 b$ in equation (i), we get
$\begin{aligned}
& -2 b-b=\frac{\pi}{4} \\
& \Rightarrow b=\frac{-\pi}{12} \\
& \Rightarrow a=-2 \times \frac{-\pi}{12}=\frac{\pi}{6}
\end{aligned}$
Now, $\begin{aligned} 2 \mathrm{a}+3 \mathrm{~b} & =2\left(\frac{\pi}{6}\right)+3\left(\frac{-\pi}{12}\right) \\ & =\frac{\pi}{3}-\frac{\pi}{4}=\frac{\pi}{12}\end{aligned}$

</details>

---

### Q57. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\mathrm{f}(x)=\left\{\begin{array}{ll}\frac{1-\cos k x}{x^2}, & \text { if } x \leq 0 \\ \frac{\sqrt{x}}{\sqrt{16+\sqrt{x}}-4}, & \text { if } x>0\end{array}\right.$ is continuous at $x=0$, then the value of $\mathrm{k}$ is

**Options:**

- **(A)** 4
- **(B)** 2
- **(C)** -1
- **(D)** -3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 4**

**Detailed Solution:**

$\mathrm{f}(x)$ is continuous at $x=0$
$\begin{aligned}
\therefore \quad \text { L.H.L. } & =\lim _{x \rightarrow 0} \frac{1-\cos k x}{x^2} \\
& =\lim _{x \rightarrow 0} \frac{2 \sin ^2 \frac{\mathrm{k} x}{2}}{x^2} \\
& =2 \lim _{x \rightarrow 0} \frac{\sin ^2 \frac{\mathrm{k} x}{2}}{\frac{\mathrm{k}^2 x^2}{4} \times 4} \cdot \mathrm{k}^2 \\
& =\frac{1}{2} \mathrm{k}^2 \lim _{x \rightarrow 0}\left(\frac{\sin \frac{\mathrm{k} x}{2}}{\frac{\mathrm{k} x}{2}}\right)^2 \\
\therefore \quad \text { L.H.L. } & =\frac{1}{2} \mathrm{k}^2
\end{aligned}$
$\begin{aligned}
\therefore \quad \text { R.H.L. } & =\lim _{x \rightarrow 0} \frac{\sqrt{x}}{\sqrt{16+\sqrt{x}}-4} \\
& =\lim _{x \rightarrow 0} \frac{(\sqrt{x})(\sqrt{16+\sqrt{x}}+4)}{(\sqrt{16+\sqrt{x}}-4)(\sqrt{16+\sqrt{x}}+4)} \\
& =\lim _{x \rightarrow 0} \frac{\sqrt{x}(\sqrt{16+\sqrt{x}}+4)}{16+\sqrt{x}-16} \\
& =\sqrt{16+\sqrt{0}+4}
\end{aligned}$
$\therefore \quad$ R.H.L. $=8$
$\mathrm{f}(x)$ is continuous at $x=0$... [Given]
$\begin{array}{ll}
\therefore \quad & \text { L.H.L. }=\text { R.H.L } \\
\therefore \quad & \frac{1}{2} \mathrm{k}^2=8 \\
\therefore \quad & \mathrm{k}^2=16 \\
\therefore \quad \mathrm{k}= \pm 4
\end{array}$

</details>

---

### Q58. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of discontinuities of the greatest integer function $\mathrm{f}(x)=[x], x \in\left(-\frac{7}{2}, 100\right)$

**Options:**

- **(A)** 104
- **(B)** 100
- **(C)** 102
- **(D)** 103

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 103**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{f}(x)=[x] \\
& x \in\left(\frac{-7}{2}, 100\right) \\
& x \in(-3.5,100)
\end{aligned}$
As we know greatest integer is discontinuous on integer values in given interval, the integer values are $\{-3,-2,-1,0 \ldots 99\}$
$\therefore \quad$ Total number of discontinuities are 103 .

</details>

---

### Q59. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x)$ is continuous on its domain $[-2,2]$ where $f(x)=\frac{\sin a x}{x}+3,-2 \leq x < 0=x+5,0 \leq x \leq 1=\sqrt{x^2+8}-b, 1 < x \leq 2$, then $7 a+b+1$ is equal to

**Options:**

- **(A)** 10
- **(B)** 11
- **(C)** 14
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 12**

**Detailed Solution:**

for continuity at $x=0, \lim _{x \rightarrow 0}-\frac{\sin a x}{x}+3=5$
$\begin{aligned}
& \Rightarrow a+3=5 \\
& \Rightarrow a=2
\end{aligned}$
for continuity at $x=1$,
$\begin{aligned}
& 6=\lim _{x \rightarrow 1}+\sqrt{x^2+8}-b \\
& \Rightarrow 6=\sqrt{1^2+8}-b \\
& \Rightarrow b=-3
\end{aligned}$
Now $7 a+b+1=7 \times 2-3+1=12$

</details>

---

### Q60. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The function $(f)(x)=[x]^2-\left[x^2\right]$
(where, $[x]$ is the greatest integer less than or equal to $x$ ), is discontinuous at

**Options:**

- **(A)** all integers.
- **(B)** all integers except 0 .
- **(C)** all integers except 0 and 1 .
- **(D)** all integers except 1 .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) all integers except 1 .**

**Detailed Solution:**

for $x=0$
$\left.\begin{array}{l}\text { L.H.L }=\left[O^{-}\right]^2-\left[\left(O^{-}\right)^2\right]=(-1)^2-(0)=1 \\ \text { R.H.L }=\left[O^{+}\right]^2-\left[O^{+}\right]^2=0^2-(0)=0\end{array}\right\}$ discount at $x=0$
for $x=1$
$\left.\begin{array}{l}\text { L.H.L }=\left[1^{-}\right]^2-\left[\left(1^{-}\right)^2\right]=0^2-0=0 \\ \text { R.H.L }=\left[1^{+}\right]^2-\left[\left(1^{+}\right)^2\right]=1^2-1=0 \\ \text { F.V. }=[1]^2-\left[1^2\right]=1-1=0\end{array}\right\}$ continuous at $x=1$
the function $f(x)$ is continuous at $x=1$ and discontinuous at all other integral point

</details>

---

### Q61. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f: R \rightarrow R$ be a function defined as
$f(x)=\left\{\begin{array}{ccc}
5 & , & \text { if } x \leq 1 \\
a+b x & , & \text { if } 1 < x < 3 \\
b+5 x & , & \text { if } 3 \leq x < 5 \\
30 & , & \text { if } x \geq 5
\end{array} \mid \text { then } f\right. \text { is }$

**Options:**

- **(A)** continuous if $a=5$ and $b=5$.
- **(B)** continuous if $a=-5$ and $b=10$.
- **(C)** not continuous for any values of $a$ and $b$.
- **(D)** continuous is $a=0$ and $b=5$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) not continuous for any values of $a$ and $b$.**

**Detailed Solution:**

for continuity at $x=1, a+b=5$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/n6cTyDj-U92zzcUTU5SQGss1xx-siXy1WFhtpW-6Rc0.original.fullsize.png">

for continuity at $x=3, a+3 b=b+15$
$\Rightarrow a+2 b=15$<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/vyR4PNWwqaeqf55PBKS1sALZIUOhI2eDVO86intndPk.original.fullsize.png">

$\because$ system of equation (i), (ii) and (iii) is inconsistent Hence, $f(x)$ is not continuous for any values of $a$ and $b$ on $R$

</details>

---

### Q62. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$f(x)=\left\{\begin{array}{cc}
\frac{x-4}{|x-4|}+a, & \text { for } x < 4 \\
a+b, & \text { for } x=4 \\
\frac{x-4}{|x-4|}+b, & \text { for } x>4
\end{array}\right.$
Is continuous at $x=4$, then

**Options:**

- **(A)** a=0,b=0
- **(B)** a=1,b=1
- **(C)** a=-1,b=1
- **(D)** a=1,b=-1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) a=1,b=-1**

**Detailed Solution:**

For continuity at $x=4$
$\begin{aligned}
& \lim _{x \rightarrow 4^{-}} f(x)=f(4)=\lim _{x \rightarrow 4^{+}} f(x) \\
& \Rightarrow \lim _{x \rightarrow 4^{-}} \frac{x-4}{|x-4|}+a=a+b=\lim _{x \rightarrow 4^{+}} \frac{x-4}{|x-4|}+b \\
& \Rightarrow-1+a=a+b=1+b \\
& \Rightarrow a=1 \text { and } b=-1
\end{aligned}$

</details>

---

### Q63. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\frac{e^{x^2}-\cos x}{x^2}$ if $x \neq 0$ is continuous at $x=0$, then $f(0)=$.

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{3}{2}$
- **(C)** $\frac{2}{3}$
- **(D)** $\frac{-3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{2}$**

**Detailed Solution:**

For continuity at $x=0, \lim _{x \rightarrow 0} f(x)=f(0)$
$$
\begin{aligned}
& \Rightarrow f(0)=\lim _{x \rightarrow 0} \frac{e^{x^2}-\cos x}{x^2}=\lim _{x \rightarrow 0} \\
& \frac{\left(1+x^2+\frac{x^4}{2 !}+\ldots \ldots\right)-\left(1-\frac{x^2}{2 !}+\ldots . . .\right)}{x^2} \\
& =\lim _{x \rightarrow 0} \frac{\frac{3}{2} x^2+\ldots . .}{x^2}=\frac{3}{2}
\end{aligned}
$$

</details>

---

### Q64. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Give that $f(x) \begin{cases}=\frac{1-\cos 4 x}{x^2} & \text { if } x<0 \\ =a & \text { if } x=0 \quad \text {, is continuous } \\ =\frac{\sqrt{x}}{\sqrt{16+\sqrt{x}}-4} & \text { if } x>0\end{cases}$ at $x=0$, then $a=$

**Options:**

- **(A)** 2
- **(B)** 8
- **(C)** 4
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 8**

**Detailed Solution:**

for continuity at $x=0$
$\begin{aligned} & \lim _{x \rightarrow 0} \frac{1-\cos 4 x}{x^2}=a=\lim _{x \rightarrow 0} \frac{\sqrt{x}}{\sqrt{16+\sqrt{x}}-4} \\ & \Rightarrow \lim _{x \rightarrow 0} \frac{2 \sin ^2 2 x}{(2 x)^2} \times 4=a=\lim _{x \rightarrow 0} \frac{\sqrt{x}}{16+\sqrt{x}-16} \times(\sqrt{16+\sqrt{x}}+4) \\ & \Rightarrow a=8\end{aligned}$

</details>

---

### Q65. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)= \begin{cases}a x^2+b x+1 & \text { if }|2 x-3| \geq 2 \\ 3 x+2 & \text {; if } \frac{1}{2}<x<\frac{5}{2}\end{cases}$ is continuous on its domain, then $a+b$ has the value

**Options:**

- **(A)** $\frac{23}{5}$
- **(B)** $\frac{1}{5}$
- **(C)** $\frac{13}{5}$
- **(D)** $\frac{31}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{23}{5}$**

**Detailed Solution:**

$\begin{aligned} & f(x)=\left\{\begin{array}{ccc}a x^2+b x+1 & ; & |2 x-3| \geq 2 \\ 3 x+2 & ; & \frac{1}{2}<x<\frac{5}{2}\end{array}\right. \\ & =\left\{\begin{array}{ccc}a x^2+b x+1 & ; & x £ \frac{1}{2} \\ 3 x+2 & ; & \frac{1}{2}<x<\frac{5}{2} \\ a x^2+b x+1 & ; & x^3 \frac{5}{2}\end{array}\right.\end{aligned}$
for continuity at $x=\frac{1}{2}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/B7jw2n1orE52k3R183BlwbMF_y5zSlpUa3NEqXT8-SY.original.fullsize.png">
for continuity at $x=\frac{5}{2}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/hUBSqhM293JDBdKv-vpL8SqOFYqHanhJjHLwOXvBBFI.original.fullsize.png">
from (1) and (2)
$a=-\frac{4}{5}$ and $b=\frac{27}{5}$
$a+b=\frac{-4+27}{5}=\frac{23}{5}$

</details>

---

### Q66. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The function defined by
$$
f(x)=\left\{\begin{array}{cc}
\frac{x-4}{|x-4|}+a & \text { if } x<4 \\
a+b & \text { if } x=4 \\
\frac{x-4}{|x-4|}+b & \text { if } x>4
\end{array}\right.
$$
is continuous at $x=4$, are

**Options:**

- **(A)** $a=0, b=1$
- **(B)** $\mathrm{a}=1, \mathrm{~b}=0$
- **(C)** $\mathrm{a}=1, \mathrm{~b}=-1$
- **(D)** $\mathrm{a}=-1, \mathrm{~b}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{a}=1, \mathrm{~b}=-1$**

**Detailed Solution:**

L.H.L at $x=4$
$\lim _{h \rightarrow 0} \frac{4-h-4}{|4-h-4|}+a=\lim _{h \rightarrow 0} \frac{-h}{|-h|}+a=\lim _{h \rightarrow 0} \frac{-h}{h}+a=-1+a$
R.H.L at $x=4$
$\lim _{h \rightarrow 0} \frac{4+h-4}{|4+h-4|}+b=\lim _{h \rightarrow 0} \frac{h}{|h|}+b=\lim _{h \rightarrow 0} \frac{h}{h}+b=1+b$
For continuity at $\mathrm{x}=4$
$-1+\mathrm{a}=\mathrm{a}+\mathrm{b}=1+\mathrm{b} \Rightarrow \mathrm{a}=1$ and $\mathrm{b}=-1$

</details>

---

### Q67. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(\mathrm{x})$
$=K+1 \quad$, for $x=0$
is continuous at $x=0$, then value of $K$ is

**Options:**

- **(A)** $1$
- **(B)** $\mathrm{e}^{-1}$
- **(C)** $0$
- **(D)** e

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0$**

**Detailed Solution:**

For continuity at $\mathrm{x}=0$
$\begin{aligned} & \lim _{x \rightarrow 0} f(x)=f(0) \Rightarrow \lim _{x \rightarrow 0} \log \left(\sec ^2 x\right) \cot ^2 x=K+1 \\ & \Rightarrow \lim _{x \rightarrow 0} \log \left(1+\tan ^2 x\right)^{\frac{1}{\tan ^2 x}}=K+1 \\ & \Rightarrow \log _e=K+1 \\ & \Rightarrow 1=K+1 \\ & \Rightarrow K=0\end{aligned}$

</details>

---

### Q68. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(\mathrm{x})=\frac{\mathrm{x}}{2}-1$, then on the interval $[0, \pi]$ where [.] represents greatest integer function

**Options:**

- **(A)** $\tan [\mathrm{f}(\mathrm{x})]$ is continuous but $\frac{1}{\mathrm{f}(\mathrm{x})}$ is not continuous.
- **(B)** $\tan [\mathrm{f}(\mathrm{x})]$ and $\frac{1}{\mathrm{f}(\mathrm{x})}$ are both continuous.
- **(C)** $\tan [\mathrm{f}(\mathrm{x})]$ and $\frac{1}{\mathrm{f}(\mathrm{x})}$ are both discontinuous.
- **(D)** $\tan [\mathrm{f}(\mathrm{x})]$ is discontinuous and $\frac{1}{\mathrm{f}(\mathrm{x})}$ is continuous.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\tan [\mathrm{f}(\mathrm{x})]$ and $\frac{1}{\mathrm{f}(\mathrm{x})}$ are both discontinuous.**

**Detailed Solution:**

$\tan [\mathrm{f}(\mathrm{x})]=\tan \left[\frac{\mathrm{x}}{2}-1\right]=\left\{\begin{array}{lll}\tan (-1), & \text { if } & 0 \leq \mathrm{x}<2 \\ \tan (0)=0, & \text { if } & 2 \leq \mathrm{x} \leq \pi\end{array}\right.$
which is discontinuous at $\mathrm{x}=2$
$\frac{1}{f(x)}=\frac{1}{\frac{x}{2}-1}$ which is discontinuous at $x=2$

</details>

---

### Q69. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(\mathrm{x})=\left\{\begin{array}{ll}\mathrm{x}, & \text { for } \mathrm{x} \leq 0 \\ 0, & \text { for } \mathrm{x}>0\end{array}\right.$, then the function $\mathrm{f}(\mathrm{x})$ at $\mathrm{x}=0$ is

**Options:**

- **(A)** not continuous and not differentiable
- **(B)** not continuous but differentiable
- **(C)** continuous but not differentiable
- **(D)** continuous and differentiable

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) continuous but not differentiable**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{f}(\mathrm{x})=\mathrm{x}, \quad \text { if } \mathrm{x} \leq 0 \\
& =0, \quad \text { if } x>0 \\
& \therefore \quad \lim _{x \rightarrow 0^{-}} f(x)=\lim _{n \rightarrow 0} x=0 \text { and } \lim _{x \rightarrow 0^{+}} f(x)=0 \\
& \mathrm{f}(0)=0 \\
& \mathrm{f}^{\prime}(\mathrm{x})=1, \quad \text { if } \mathrm{x} \leq 0 \\
& =0, \quad \text { if } x>0 \\
&
\end{aligned}$
Thus $f(x)$ is continuous at $x=0$
$\begin{aligned}
\mathrm{f}^{\prime}(\mathrm{x}) & =1, & & \text { if } \mathrm{x} \leq 0 \\
& =0, & & \text { if } \mathrm{x}>0
\end{aligned}$
Thus $\mathrm{f}(\mathrm{x})$ is not differentiable at $\mathrm{x}=0$.

</details>

---

### Q70. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the function given by
$$
f(x)= \begin{cases}-2 \sin x & -\pi \leq x < -(\pi / 2) \\ a \sin x+b & -(\pi / 2) < x < (\pi / 2) \\ \cos x & (\pi / 2) \leq x \leq \pi\end{cases}
$$
is continuous in $[-\pi, \pi]$, then the value of $(3 a+2 b)^3$ is

**Options:**

- **(A)** 1
- **(B)** 8
- **(C)** -1
- **(D)** -8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -1**

**Detailed Solution:**

$$
\begin{aligned}
& \lim _{x \rightarrow \frac{\pi^{-}}{2}} f(x)=\lim _{x \rightarrow \frac{\pi^{-}}{2}}-2 \sin x=-2 \sin \left(-\frac{\pi}{2}\right)=2 \\
& \lim _{x \rightarrow \frac{-\pi^{+}}{2}} f(x)=\lim _{x \rightarrow \frac{-\pi^{+}}{2}} a \sin x+b=a \sin \left(\frac{-\pi}{2}\right)+b=-a
\end{aligned}
$$
Since $f(x)$ is continuous at $x=\frac{-\pi}{2}$, we write
$$
\begin{aligned}
& 2=-a+b \\
& \lim _{x \rightarrow \frac{\pi^{-}}{2}} f(x) \lim _{x \rightarrow \frac{\pi^{-}}{2}} a \sin x+b=a \sin \left(\frac{\pi}{2}\right)+b=a+b \\
& \lim _{x \rightarrow \frac{\pi^{+}}{2}} f(x)=\lim _{x \rightarrow \frac{\pi^{+}}{2}} \cos x=\cos \left(\frac{\pi}{2}\right)=0
\end{aligned}
$$
Since $f(x)$ is continuous at $x=\frac{\pi}{2}$, we write
$$
\mathrm{a}+\mathrm{b}=0
$$
From (1) and (2), we get $\mathrm{a}=-1, \mathrm{~b}=1$
$$
\therefore(3 a+2 b)^3=(-3+2)^3=-1
$$

</details>

---

### Q71. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\frac{1-\sin x+\cos x}{1+\sin x+\cos x}$, for $x \neq \pi$ is continuous at $x=\pi$, then the value of $f(\pi)$ is

**Options:**

- **(A)** $\frac{-1}{2}$
- **(B)** $-1$
- **(C)** $1$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-1$**

**Detailed Solution:**

$f(x)=\frac{(1+\cos x)-(\sin x)}{(1+\cos x)+(\sin x)}$, is continuous at $x=\pi$
$$
\begin{aligned}
& \lim _{x \rightarrow \pi} f(x)=\lim _{x \rightarrow \pi} \frac{\left(2 \cos ^2 \frac{x}{2}\right)-\left(2 \sin \frac{x}{2} \cos \frac{x}{2}\right)}{\left(2 \cos ^2 \frac{x}{2}\right)+\left(2 \sin \frac{x}{2} \cos \frac{x}{2}\right)} \\
& =\lim _{x \rightarrow \pi} \frac{2 \cos \frac{x}{2}\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)}{2 \cos \frac{x}{2}\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)} \\
& =\lim _{x \rightarrow \pi} \frac{1-\tan \frac{x}{2}}{1+\tan \frac{x}{2}}=\lim _{x \rightarrow \pi} \tan \left(\frac{\pi}{4}-\frac{x}{2}\right)=\tan \left(\frac{\pi}{4}-\frac{\pi}{2}\right)=-1
\end{aligned}
$$

</details>

---

### Q72. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x)= \begin{cases}3 a x+b, & \text { for } x < 1 \\ 11, & \text { for } x=1 \text { is continuous at } \\ 5 a x-2 b, & \text { for } x>1\end{cases}$ $x=1$. Then, the values of $a$ and $b$ are

**Options:**

- **(A)** $a=2, b=3$
- **(B)** $a=3, b=3$
- **(C)** $a=2, b=2$
- **(D)** $a=3, b=2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a=3, b=2$**

**Detailed Solution:**

$$
\begin{aligned}
& \lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}} 3 a x+b=3 a+b \\
& \lim _{x \rightarrow 1^{+}} f(x) \lim _{x \rightarrow 1^{+}} 5 a x-2 b=5 a-2 b
\end{aligned}
$$
$f(1)=11$ and function is continuous at $x=1$, so we write
$$
3 \mathrm{a}+\mathrm{b}=11=5 \mathrm{a}-2 \mathrm{~b} \Rightarrow 2 \mathrm{a}=3 \mathrm{~b}
$$
This condition is satisfied when $\mathrm{a}=3, \mathrm{~b}=2$

</details>

---

### Q73. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{f}(\mathrm{x}) \begin{cases}=\mathrm{x}+\mathrm{a} \sqrt{2} \sin \mathrm{x}, & 0 \leq \mathrm{x} < \frac{\pi}{4} \\ =2 \mathrm{x} \cot \mathrm{x}+\mathrm{b}, & \frac{\pi}{4} \leq \mathrm{x} < \frac{\pi}{2} \\ =\mathrm{a} \cos 2 \mathrm{x}-\mathrm{b} \sin \mathrm{x}, & \frac{\pi}{2} \leq \mathrm{x} \leq \pi\end{cases}$ If $\mathrm{f}(\mathrm{x})$ is continuous for $0 \leq \mathrm{x} \leq \pi$, then

**Options:**

- **(A)** $a=\frac{\pi}{6}, b=\frac{-\pi}{12}$
- **(B)** $\mathrm{a}=\frac{-\pi}{6}, \mathrm{~b}=\frac{-\pi}{12}$
- **(C)** $a=\frac{-\pi}{6}, b=\frac{\pi}{12}$
- **(D)** $\mathrm{a}=\frac{\pi}{6}, \mathrm{~b}=\frac{\pi}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $a=\frac{\pi}{6}, b=\frac{-\pi}{12}$**

**Detailed Solution:**

$\lim _{x \rightarrow \frac{\pi^{-}}{4}} f(x)=\lim _{x \rightarrow \frac{\pi^{-}}{4}} x+a \sqrt{2} \sin x$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/hcQiAVI3GSQtjWOQuL5buyoxZmFW6vTmVEe9FC9A7M4.original.fullsize.png">

$\lim _{x \rightarrow \frac{\pi^{+}}{4}} f(x)=\lim _{x \rightarrow \frac{\pi^{+}}{4}} 2 x \cot x+b$<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/bmczS6mJrF7J4k_SVxEtk9ccOQgzL5p2G0iO42mX48I.original.fullsize.png">

$\lim _{x \rightarrow \frac{\pi^{-}}{2}} f(x)=\lim _{x \rightarrow \frac{\pi^{-}}{2}} 2 x \cot x+b$<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/m1PAub7i96-ccdhgjX2z0RYlGcfCjE8Wv5bDXNvC4ss.original.fullsize.png">

$\begin{aligned} & \lim _{x \rightarrow \frac{\pi^{+}}{2}} f(x)=\lim _{x \rightarrow \frac{\pi^{+}}{2}} a \cos 2 x-b \sin x \\ & =a \cos 2\left(\frac{\pi}{2}\right)-b \sin \left(\frac{\pi}{2}\right)\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/7sb6LNad4gzet3bSTtaShE-_Ik_ilXz-PYlZglRqz9A.original.fullsize.png">

Since $f(x)$ is continuous at $\frac{\pi}{4}$ and $\frac{\pi}{2}$, we write
$\frac{\pi}{4}+\mathrm{a}=\frac{\pi}{2}+\mathrm{b} \quad \ldots[$ From (1) and (2) $]$<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/c36sYOTgfNQKRG4dy3uAH4Rya9iFYgOC4X9WvpY4cw0.original.fullsize.png">

$\mathrm{b}=-\mathrm{a}-\mathrm{b} \quad \ldots[$ From (3) and (4) $]$<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/WsccvTMRp9wkIz8saRUQUFT5H-7Qgrayn33QPygwrao.original.fullsize.png">

</details>

---

### Q74. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x) \begin{cases}=|x|+3, & \text { if } x \leq-3 \\ =-2 x, & \text { if }-3 < x < 3, \text { then } \\ =6 x+2, & \text { if } x \geq 3\end{cases}$

**Options:**

- **(A)** $f(x)$ is discontinuous at both $x=-3$ as well as $x=3$
- **(B)** $f(x)$ is continuous at $x=-3$ but discontinuous at $x=3$
- **(C)** $f(x)$ is continuous at $x=-3$ as well as $x=3$
- **(D)** $f(x)$ of discontinuous at $x-3$ but $f(x)$ is continuous at $x=3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $f(x)$ is continuous at $x=-3$ but discontinuous at $x=3$**

**Detailed Solution:**

We have $f(x)=-x+3$, if $x \leq-3$
$$
\begin{aligned}
& =-2 x \text {, if }-3 < x < 3 \\
& =6 \mathrm{x}+2 \text {, if } \mathrm{x} \geq 3 \\
& \underset{x \rightarrow 3^{-}}{f(x)}=-(-3)+3=6 \text { and } \underset{x \rightarrow 3^{+}}{f(x)}=-2(-3)=6 \text { and } f(-3) \\
& =-(-3)+3=6 \\
&
\end{aligned}
$$
Thus $\mathrm{f}(\mathrm{x})$ is continuous at $\mathrm{x}=-3$
$$
\underset{x \rightarrow 3^{-}}{f(x)}=-2(3)=-6 \quad \text { and } \underset{x \rightarrow 3^{+}}{f(x)}=6(3)+2=20
$$
Thus $\mathrm{f}(\mathrm{x})$ is not continuous at $\mathrm{x}=3$.

</details>

---

### Q75. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$$
f(x) \begin{cases}=\frac{\sqrt{1+p x}-\sqrt{1-p x}}{x} & \text {, if } 1 \leq x < 0 \\ =\frac{2 x+1}{x-2} & \text {, if } 0 \leq x \leq 1\end{cases}
$$
is continuous in the interval $[-1,1]$, then $\mathrm{p}=$

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** $\frac{-1}{2}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-1}{2}$**

**Detailed Solution:**

$$
\begin{aligned}
& \lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}} \frac{\sqrt{1+p x}-\sqrt{1-p x}}{x} \\
& =\lim _{x \rightarrow 0^{-1}} \frac{[(\sqrt{1+p x})-(\sqrt{1-p x})][(\sqrt{1+p x})+(\sqrt{1-p x})]}{x[(\sqrt{1+p x})+(\sqrt{1-p x})]} \\
& =\lim _{x \rightarrow 0^{-}} \frac{[(1+p x)-(1-p x)]}{x[\sqrt{1+p x}+\sqrt{1-p x}]}=\lim _{x \rightarrow 0^{-}} \frac{2 p}{\sqrt{1+p x}+\sqrt{1-p x}} \\
& =\frac{2 p}{2}=p \\
& \lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}} \frac{2 x+1}{x-2}=\frac{1}{-2}
\end{aligned}
$$
Since $\mathrm{f}(\mathrm{x})$ is continuous at $\mathrm{x}=0$, we get $\mathrm{p}=\frac{-1}{2}$

</details>

---

### Q76. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$$
=1+\sin \frac{\pi}{2}, \quad-\infty < x \leq 1
$$
If the function $\mathrm{f}(\mathrm{x})=\mathrm{ax}+\mathrm{b}, \quad 1 < \mathrm{x} < 3$ is continuous in
$$
=6 \tan \frac{x \pi}{12}, \quad 3 \leq x < 6
$$
$(-\infty, 6)$, then the values of $a$ and $b$ are respectively.

**Options:**

- **(A)** 1,1
- **(B)** 2,1
- **(C)** 0,2
- **(D)** 2,0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2,0**

**Detailed Solution:**

$$
\begin{aligned}
& \lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}} 1+\sin \frac{\pi}{2}=1+1=2 \\
& \lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}} a+b=a+b
\end{aligned}
$$
Since $f(x)$ is continuous at $x=1$, we get $a+b=2$
[From (1), (2)]
$$
\begin{aligned}
& \lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3^{-}} a x+b=3 a+b \\
& \lim _{x \rightarrow 3^{+}} f(x)=\lim _{x \rightarrow 3^{+}} 6 \tan \frac{x \pi}{12}=6 \tan \frac{3 \pi}{12}=6
\end{aligned}
$$


Since $f(x)$ is continuous at $x=3$, we get $3 a+b=6$
[From (4), (5)]
Solving (3) and (6), we get a $=2, b=0$

</details>

---

### Q77. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $f(x)=\frac{4^{x-\pi}+4^{\pi-x}-2}{(x-\pi)^2}$ for $\neq \pi$, is continuous at $x=\pi$, then $=\mathrm{k} \quad$ for $=\pi$
$\mathrm{k}=$

**Options:**

- **(A)** $2 \log 2$
- **(B)** $(\log 2)^2$
- **(C)** $-4(\log 2)^2$
- **(D)** $8(\log 2)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-4(\log 2)^2$**

**Detailed Solution:**

$$
f(\pi)=\lim _{x \rightarrow \pi} f(x)=\lim _{x \rightarrow \pi} \frac{4^{x-\pi}+4^{\pi-4}-2}{(x-\pi)^2}
$$
Put $\mathrm{x}=\pi+\mathrm{h}$. As $\mathrm{x} \rightarrow \pi, \mathrm{h} \rightarrow 0$
$$
\begin{aligned}
& \therefore \mathrm{f}(\pi)=\lim _{\mathrm{h} \rightarrow 0} \frac{4^{\mathrm{h}}+4^{-\mathrm{h}}-1-1}{\mathrm{~h}^2}=\lim _{\mathrm{h} \rightarrow 0} \frac{\left(4^{\mathrm{h}}-1\right)}{\mathrm{h}} \times \lim _{\mathrm{h} \rightarrow 0} \frac{4^{-\mathrm{h}}-1}{-\mathrm{h}} \times(-1) \\
& =(\log 4)(-\log 4)=(2 \log 2)(-2 \log 2)=-4(\log 2)^2
\end{aligned}
$$

</details>

---

### Q78. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\begin{aligned} f(x) &=\frac{\left(e^{3 x}-1\right) \sin x^{\circ}}{x^{2}} \text { if } x \neq 0 \\ &=\frac{\pi}{60} \quad \text { if } x=0, \text { then } \end{aligned}$

**Options:**

- **(A)** $f$ is continuous at $x=0$
- **(B)** $\lim _{x \rightarrow 0} f(x)=3$
- **(C)** $f$ has irremovable discontinuity at $x=0$
- **(D)** $f$ has removable discontinuity at $x=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $f$ is continuous at $x=0$**

**Detailed Solution:**

$$
\lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0} \frac{\left(e^{3 x}-1\right) \sin x^{0}}{x^{2}}
$$
Dividing numerator and denominator by $x^{2}$, we get
$$
\begin{array}{l}
=\lim _{x \rightarrow 0}\left(\frac{e^{3 x}-1}{3 x} \times 3\right) \frac{\sin \left(\frac{\pi x}{180}\right)^{0}}{\left(\frac{\pi x}{180}\right)^{c}} \times\left(\frac{\pi}{180}\right) \\
=\frac{\left(\frac{x^{2}}{x^{2}}\right)}{=(3)(1)\left(\frac{\pi}{180}\right)}=\frac{\pi}{60}
\end{array}
$$
Hence $f(x)$ is continuous at $x=0$.

</details>

---

### Q79. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\frac{1-\sin x+\cos x}{1+\sin x+\cos x}$, for $x \neq \pi$ is continuous at $x=\pi$, then $f(\pi)=$

**Options:**

- **(A)** $-1$
- **(B)** 2
- **(C)** 0
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-1$**

**Detailed Solution:**

(A)
$f$ is continuous at $x=\pi$
$\begin{aligned} f(\pi) &=\lim _{x \rightarrow \pi} f(x)=\lim _{x \rightarrow \pi} \frac{1-\sin x+\cos x}{1+\sin x+\cos x} \\ &=\lim _{x \rightarrow \pi} \frac{-\cos x-\sin x}{\cos x-\sin x} \\ &=\frac{-\cos \pi-\sin \pi}{\cos \pi-\sin \pi}=\frac{-(-1)-0}{-1-0}=\frac{1}{-1}=-1 \end{aligned}$

</details>

---

### Q80. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\begin{aligned} f(x) &=\frac{4 \sin \pi x}{5 x} \text { for } x \neq 0 \\ &=2 \mathrm{k} \quad \text { for } x=0 \end{aligned}$
is continuous at $x=0$, then the value of $k$ is

**Options:**

- **(A)** $\frac{2 \pi}{5}$
- **(B)** $\frac{\pi}{5}$
- **(C)** $\frac{\pi}{10}$
- **(D)** $\frac{4 \pi}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2 \pi}{5}$**

**Detailed Solution:**

(C)
Since $f(x)$ is continuous at $x=0$,
$\begin{array}{l}
\lim _{x \rightarrow 0} f(x)=f(0) \Rightarrow \lim _{x \rightarrow 0} \frac{4 \sin \pi x}{5 x}=2 k \\
\therefore \lim _{x \rightarrow 0}\left(\frac{4 \sin \pi x}{\pi x}\right) \cdot \frac{\pi}{5}=2 k \Rightarrow(1) \cdot \frac{4 \pi}{5}=2 k \Rightarrow k=\frac{2 \pi}{5}
\end{array}$

</details>

---

### Q81. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The points of discontinuity of the function $f(x)=\frac{1}{x-1}$ if $0 \leq x \leq 2$ $=\frac{x+5}{x+3} \quad$ if $\quad 2 < x \leq 4$ in its domain are

**Options:**

- **(A)** x=2 only
- **(B)** x=1, x=2
- **(C)** x=4 only
- **(D)** x=0, x=2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) x=1, x=2**

**Detailed Solution:**

(B)
$\begin{aligned}
f(x) &=\frac{1}{x-1}, \text { if } 0 \leq x \leq 2 \Rightarrow f(x) \text { is not defined at } x=1 \\
&=\frac{x+5}{x+3}, \text { if } 2 < x \leq 4
\end{aligned}$
$\lim _{x \rightarrow 2^{-}} f(x)=\frac{1}{2-1}=1 \text { and } \lim _{x \rightarrow 2^{+}} f(x)=\frac{7}{5}$
Thus $f(x)$ is not continuous at $x=2$

</details>

---

### Q82. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function given by $f(x)=\left(\frac{4 x+1}{1-4 x}\right)^{\frac{1}{x}}$ for $x \neq o$ is continuous at $x=0$, then
the value of $\mathrm{f}(\mathrm{o})$ is

**Options:**

- **(A)** $\mathrm{e}^{8}$
- **(B)** $\mathrm{e}^{10}$
- **(C)** $\mathrm{e}^{-8}$
- **(D)** $\mathrm{e}^{-10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{e}^{8}$**

**Detailed Solution:**

$\begin{aligned} \lim _{x \rightarrow 0}\left(\frac{1+4 x}{1-4 x}\right)^{\frac{1}{x}} &=\frac{\lim _{x \rightarrow 0}(1+4 x)^{\frac{1}{x}}}{\lim _{x \rightarrow 0}(1-4 x)^{\frac{1}{x}}}=\frac{\left[\lim _{x \rightarrow 0}(1+4 x)^{\frac{1}{4 x}}\right]^{4}}{\left[\lim _{x \rightarrow 0}(1-4 x)^{\frac{-1}{4 x}}\right]^{-4}}=\frac{e^{4}}{e^{-4}} \\ &=e^{8} \end{aligned}$

</details>

---

### Q83. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$$
\text { If } \begin{aligned}
f(x) &=\frac{|x-2|}{x-2}, \quad \text { for } x \neq 2 \\
&=1 \quad, \quad \text { for } x=2,
\end{aligned}
$$
then which of the following statements is true?

**Options:**

- **(A)** $f(x)$ is continuous at $x=2$
- **(B)** $\lim _{x \rightarrow 2^{-}} f(x)=f(2)$
- **(C)** $\lim _{x \rightarrow 2^{+}} f(x)=\lim _{x \rightarrow 2^{-}} f(x)$
- **(D)** $f(x)$ is discontinuous at $x=2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $f(x)$ is discontinuous at $x=2$**

**Detailed Solution:**

Here $\begin{aligned}|x-2| &=x-2, \quad \text { if } x>2 \Rightarrow \lim _{x \rightarrow 2^{-}} f(x)=\lim _{x \rightarrow 2^{+}} f(x)=0 \\ &=-(x-2), \text { if } x < 2 \end{aligned}$
But $f(2)=1 \neq 0$
So $f(x)$ is discontinuous at $x=2$

</details>

---

### Q84. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the function $f(x)=\frac{\log 10+\log (0.1+2 x)}{2 x}$ if $x \neq 0$
$=k \quad$ if $x=0$
is continuous at $x=0$, then $k+2=$

**Options:**

- **(A)** 2
- **(B)** 10
- **(C)** 12
- **(D)** 11

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 12**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{\log 10+\log (0.1+2 x)}{2 x}=k$
$\therefore \lim _{x \rightarrow 0} \frac{\log (1+20 x)}{2 x}=k \Rightarrow \lim _{x \rightarrow 0} \log (1+20 x)^{\frac{1}{2 x}}=k$
$\therefore \log \lim _{x \rightarrow 0}\left[(1+20 x)^{\frac{1}{20 x}}\right]^{10}=k \Rightarrow \log e^{10}=k \Rightarrow k=10 \Rightarrow k+2=10+2=12$

</details>

---

### Q85. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\frac{(81)^{x}-(9)^{x}}{(k)^{x}-1}$ if $x \neq 0$
$=2 \quad$ if $\quad x=0$
is continuous at $x=0$, then the value of $k$ is

**Options:**

- **(A)** 3
- **(B)** 9
- **(C)** 2
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{81^{x}-9^{x}}{k^{x}-1}=2$
$\therefore \lim _{x \rightarrow 0} \frac{9^{x}\left(9^{x}-1\right)}{k^{x}-1}=2 \Rightarrow \frac{\left(\lim _{x \rightarrow 0} 9^{x}\right)\left(\lim _{x \rightarrow 0} \frac{9^{x}-1}{x}\right)}{\lim _{x \rightarrow 0} \frac{k^{x}-1}{x}}=2$
$\frac{\log 9}{\log k}=2 \Rightarrow \log 9=2 \log k \Rightarrow \log k^{2}=\log 9 \Rightarrow k^{2}=9 \Rightarrow k=3$

</details>

---

### Q86. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\left[\tan \left(\frac{\pi}{4}+x\right)\right]^{\frac{1}{x}} \quad$ if $x \neq 0$
$=k \quad$ if $x=0$,
is continuous at $x=0$ then $k=$

**Options:**

- **(A)** $e$
- **(B)** $\sqrt{e}$
- **(C)** $e^{2}$
- **(D)** $e^{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $e^{2}$**

**Detailed Solution:**

Given $f(x)$ is continuous at $x=0$
$\therefore \lim _{x \rightarrow 0}\left[\tan \left(\frac{\pi}{4}+x\right)\right]^{\frac{1}{x}}=K$
$\therefore \lim _{x \rightarrow 0}\left(\frac{1+\tan x}{1-\tan x}\right)^{\frac{1}{x}}=K$
$\therefore \frac{\left[\lim _{x \rightarrow 0}(1+\tan x)^{\frac{1}{\tan x}}\right]^{\frac{\tan x}{x}}}{\left[\lim _{x \rightarrow 0}(1-\tan x) \frac{-1}{\tan x}\right]^{\frac{\tan x}{x}}}=\mathrm{K}$
$\frac{\left[\lim _{x \rightarrow 0}(1+\tan x) \frac{1}{\tan x}\right]^{\lim _{x \rightarrow 0} \frac{\tan x}{x}}}{\left[\lim _{x \rightarrow 0}(1-\tan x)\right]^{-\lim _{x \rightarrow 0} \frac{\tan x}{x}}}=K$
$\frac{e^{1}}{e^{-1}}=K \quad \Rightarrow K=e^{2}$

</details>

---

### Q87. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the function $f(x)=\frac{1-\sin 2 x+\cos 2 x}{1+\sin 2 x+\cos 2 x}$ if $\quad x \neq \frac{\pi}{2}$
$=\mathrm{k} \quad$ if $\quad x=\frac{\pi}{2}$
is continuous at $x=\frac{\pi}{2}$, then $\mathrm{k}=$

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** 0
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -1**

**Detailed Solution:**

$\begin{aligned}
\lim _{x \rightarrow \frac{\pi}{2}} f(x)=& \lim _{x \rightarrow \frac{\pi}{2}} \frac{1-\sin 2 x+\cos 2 x}{1+\sin 2 x+\cos 2 x} \\
=& \lim _{x \rightarrow \frac{\pi}{2}} \frac{(1+\cos 2 x)-\sin 2 x}{(1+\cos 2 x)+\sin 2 x}=\lim _{x \rightarrow \frac{\pi}{2}} \frac{2 \cos ^{2} x-2 \sin x \cos x}{x+2 \sin x \cos x} \\
=& \lim _{x \rightarrow \frac{\pi}{2}} \frac{2 \cos x(\cos x-\sin x)}{2 \cos x(\cos x+\sin x)}=\lim _{x \rightarrow \frac{\pi}{2}} \frac{\cos x-\sin x}{\cos x+\sin x}=\frac{0-1}{0+1}=-1
\end{aligned}$
Since $f(x)$ is continuous at $x=\frac{\pi}{2}$, we get $k=-1$

</details>

---

### Q88. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\frac{\left(e^{2 x}-1\right) \sin x^{0}}{x^{2}}, x \neq 0$ is continuous at $x=0$, then $f(0)=$

**Options:**

- **(A)** $\frac{90}{\pi}$
- **(B)** $\frac{180}{\pi}$
- **(C)** $\frac{\pi}{90}$
- **(D)** $\frac{\pi}{180}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{90}$**

**Detailed Solution:**

$\begin{aligned} \mathrm{f}(0) &=\lim _{\mathrm{x} \rightarrow 0} \frac{\left(\mathrm{e}^{2 \mathrm{x}}-1\right) \sin \frac{x \pi}{180}}{\mathrm{x}^{2}} \quad\quad\cdots\left[\because x^{\circ}=\left(\frac{x \pi}{180}\right)^{c}\right] \\ &=\lim _{\mathrm{x} \rightarrow 0}\left(\frac{\mathrm{e}^{2 \mathrm{x}}-1}{\mathrm{x}}\right)\left(\frac{\sin \frac{\pi \mathrm{x}}{180}}{\mathrm{x}}\right) \\ &=\left(2 \lim _{\mathrm{x} \rightarrow 0} \frac{\mathrm{e}^{2 \mathrm{x}}-1}{2 \mathrm{x}}\right) \frac{\pi}{180}\left[\lim _{\mathrm{x} \rightarrow 0} \frac{\frac{\sin \mathrm{x} \pi}{180}}{\frac{\mathrm{x} \pi}{180}}\right]=2(\log \mathrm{e}) \times\left(\frac{\pi}{180}\right)=\frac{\pi}{90} \end{aligned}$

</details>

---

### Q89. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Which of the following functions is not p.d.f. of a continuous random variable X?
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/MDClfbuL6lrF4wAcaXSf1WeqVpO0ap4_l1GW2wCqgV4.original.fullsize.png">

**Options:**

- **(A)** $F_{3}$
- **(B)** $F_{4}$
- **(C)** $F_{1}$
- **(D)** $F_{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $F_{4}$**

**Detailed Solution:**

Since $P(X=1)=P(X=2)=\ldots \ldots \ldots=P(X=n)$ 
and $P(X=1)+P(X=2)+\ldots \ldots+P(X=n)=1$, 
We get $P(X=1)=P(X=2)=P(X=n)=\frac{1}{n}$
\begin{array}{|c|c|c|c|}
\hline \mathbf{x}_{\mathbf{i}} & \mathbf{p}_{\mathbf{i}} & \mathbf{x}_{\mathbf{i}} \mathbf{p}_{\mathbf{i}} & \mathbf{x}_{\mathbf{i}}^{2} \mathbf{p}_{\mathbf{i}} \\
\hline 1 & \frac{1}{\mathrm{n}} & \frac{1}{\mathrm{n}} & \frac{1}{\mathrm{n}} \\
2 & \frac{1}{\mathrm{n}} & \frac{2}{\mathrm{n}} & \frac{2^{2}}{\mathrm{n}} \\
3 & \frac{1}{\mathrm{n}} & \frac{3}{\mathrm{n}} & \frac{3^{2}}{\mathrm{n}} \\
\vdots & \vdots & \vdots & \vdots \\
\mathrm{n} & \frac{1}{\mathrm{n}} & \frac{\mathrm{n}}{\mathrm{n}} & \frac{\mathrm{n}^{2}}{\mathrm{n}} \\
\hline
\end{array}
$\sum \mathrm{x}_{\mathrm{i}} \mathrm{p}_{\mathrm{i}}=\frac{1}{\mathrm{n}}+\frac{2}{\mathrm{n}}+\frac{3}{\mathrm{n}}+\ldots \ldots+\frac{\mathrm{n}}{\mathrm{n}}=\frac{1}{\mathrm{n}}(1+2+3+\ldots \ldots \ldots \mathrm{n})=\frac{1}{\mathrm{n}} \frac{\mathrm{n}(\mathrm{n}+1)}{2}=\frac{\mathrm{n}+1}{2}$
$\begin{aligned}
\sum x_{1}{ }^{2} p_{1} &=\frac{1^{2}}{n}+\frac{2^{2}}{n}+\frac{3^{2}}{n}+\ldots \ldots+\frac{n^{2}}{n} \\
&=\frac{1}{n}\left(1^{2}+2^{2}+3^{2}+\ldots+n^{2}\right)=\frac{1}{n} \frac{n(n+1)(2 n+1)}{6}-\frac{(n+1)(2 n+1)}{6}
\end{aligned}$
Given $E(X)=V(X)$
$\begin{array}{l}
\sum x_{i} p_{i}=\sum x_{i}^{2} p_{i}-\left[\sum x_{i} p_{i}\right]^{2} \\
\frac{n+1}{2}=\frac{(n+1)(2 n+1)}{6}-\left(\frac{n+1}{2}\right)^{2} \\
\frac{n+1}{2}=(n+1)\left(\frac{2 n+1}{6}-\frac{n+1}{4}\right) \Rightarrow \frac{1}{2}=\frac{8 n+4-6 n-6}{24} \\
12=2 n-2 \Rightarrow n=7
\end{array}$

</details>

---

### Q90. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If 
$\begin{aligned} f(x) &=6 \beta-3 \propto x, \text { if }-4 \leq x < -2 \\ &=4 x+1, \text { if }-2 \leq x \leq 2 \end{aligned}$
is continuous on $[-4,2]$, then $\propto+\beta=$

**Options:**

- **(A)** $\frac{-7}{6}$
- **(B)** $\frac{4}{7}$
- **(C)** $\frac{-4}{7}$
- **(D)** $\frac{7}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-7}{6}$**

**Detailed Solution:**

$\lim _{x \rightarrow-2^{-}} f(x)=\lim _{x \rightarrow-2^{-}}(6 \beta-3 \alpha x)$
$=6 \beta+6 \alpha$ ...(1)
$\lim _{x \rightarrow-2^{+}} f(x)=\lim _{x \rightarrow-2^{+}}(4 x+1)=-7$ ...(2)
Given $f(x)$ is continuous on $[-4,2]$
$\therefore 6 \beta+6 \alpha=-7$
$\therefore \alpha+\beta=\frac{-7}{6}$

</details>

---

### Q91. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>b</mi><mi>x</mi></mrow></mfenced></mrow></mrow></mrow></mrow></mrow><mrow><mi>x</mi></mrow></mfrac><mo>,</mo><mi></mi><mi>x</mi><mo>≠</mo><mn>0</mn></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math> then, <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>a</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>b</mi></mrow></mrow></mrow></mrow></math>
- **(B)** <math><mi>a</mi><mo>+</mo><mi>b</mi></math>
- **(C)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>a</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>b</mi></mrow></mrow></mrow></mrow></math>
- **(D)** <math><mi>a</mi><mo>-</mo><mi>b</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>a</mi><mo>+</mo><mi>b</mi></math>**

**Detailed Solution:**

Given: <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>b</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi></mrow></mfrac><mi mathvariant="normal"></mi><mi>x</mi><mo>≠</mo><mn>0</mn></math>  
is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math> , then 
<math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mi mathvariant="normal"></mi><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfrac><mrow><mo> </mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi></mrow></mfenced></mrow></mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>b</mi><mi>x</mi></mrow></mfenced></mrow></mrow></mrow><mrow><mi>x</mi></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>0</mn></mrow><mrow><mn>0</mn></mrow></mfrac></math> form 
<math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mfrac><mrow><mfrac><mrow><mi>a</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>b</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>b</mi><mi>x</mi></mrow></mfrac></mrow><mrow><mn>1</mn></mrow></mfrac></math> (by L–hospital rule) 
<math><mo>=</mo><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced></math>

</details>

---

### Q92. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following function is not continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn><mo>?</mo></math>

**Options:**

- **(A)** <math><mtable><mtr><mtd><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup></mtd><mtd><mo>,</mo><mi></mi><mi>x</mi><mo>≠</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mo>,</mo><mi></mi><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></math>
- **(B)** <math><mtable><mtr><mtd><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow></mtd><mtd><mo>,</mo><mi></mi><mi>x</mi><mo>≠</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>=</mo><mo>-</mo><mn>1</mn></mtd><mtd><mo>,</mo><mi></mi><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></math>
- **(C)** <math><mtable><mtr><mtd><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mtd><mtd><mo>,</mo><mi></mi><mi>x</mi><mo>≠</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi></mi><mo>=</mo><mo>-</mo><mn>1</mn></mtd><mtd><mo>,</mo><mi></mi><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></math>
- **(D)** <math><mtable><mtr><mtd><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>5</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mn>3</mn><mi>x</mi></mrow></mrow></mrow></mfrac></mtd><mtd><mo>,</mo><mi></mi><mi>x</mi><mo>≠</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>=</mo><mn>1</mn><mi></mi></mtd><mtd><mo>,</mo><mi></mi><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mtable><mtr><mtd><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mtd><mtd><mo>,</mo><mi></mi><mi>x</mi><mo>≠</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi></mi><mo>=</mo><mo>-</mo><mn>1</mn></mtd><mtd><mo>,</mo><mi></mi><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></math>**

**Detailed Solution:**

Given <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  
<math><mfenced close="" open="{" separators="|"><mrow><mtable columnalign="left"><mtr><mtd><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>1</mn><mo>/</mo><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>1</mn><mo>/</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mtd><mtd><mi>x</mi><mo>≠</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>  
R.H.L. <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mi mathvariant="normal"></mi><mi mathvariant="normal"></mi><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mi>x</mi></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mi>x</mi></mrow></msup></mrow></mfrac><mo>=</mo><mn>1</mn><mo>≠</mo><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced></math>

</details>

---

### Q93. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If function <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mfrac><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi></mrow></mfrac><mo>,</mo><mi>x</mi><mo>&lt;</mo><mn>0</mn></math> <math><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi></mrow></mfrac><mo>,</mo><mi>x</mi><mo>&gt;</mo><mn>0</mn></math> <math><mo>=</mo><mn>1</mn><mo>,</mo><mi>x</mi><mo>=</mo><mn>0</mn></math>, then

**Options:**

- **(A)** <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> does not exist
- **(B)** <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> does not exist
- **(C)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is continuous at x = 0
- **(D)** <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>≠</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is continuous at x = 0**

**Detailed Solution:**

Given function, 
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mfrac><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi></mrow></mfrac><mo>,</mo><mi>x</mi><mo>&lt;</mo><mn>0</mn></math>  
<math><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi></mrow></mfrac><mo>,</mo><mi>x</mi><mo>&gt;</mo><mn>0</mn>,</mo><mi>x</mi><mo>=</mo><mn>0</mn></math>  
Now, at x = 0 
<math><mi>L</mi><mi>H</mi><mi>L</mi><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></math>  
<math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>  
<math><mi>R</mi><mi>H</mi><mi>L</mi><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mo>+</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mfrac><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></math>  
<math><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>  
<math><mo>∴</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>  
<math><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is continuous at x = 0

</details>

---

### Q94. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function <math> <mrow> <mi>f</mi><mfenced> <mi>x</mi> </mfenced><mo>=</mo><mfenced close="" open="{"> <mrow> <mtable equalcolumns="true" equalrows="true"> <mtr> <mtd> <mrow> <mfrac> <mrow> <mfenced> <mrow> <msup> <mi>e</mi> <mrow> <mi>k</mi><mi>x</mi></mrow> </msup> <mo>−</mo><mn>1</mn></mrow> </mfenced><mtext>tan</mtext><mi>k</mi><mi>x</mi></mrow> <mrow> <mn>4</mn><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> <mo>,</mo></mrow> </mtd> <mtd> <mrow> <mi>x</mi><mo>≠</mo><mn>0</mn></mrow> </mtd> </mtr> <mtr> <mtd> <mrow> <mn>16</mn><mo>,</mo></mrow> </mtd> <mtd> <mrow> <mi>x</mi><mo>=</mo><mn>0</mn></mrow> </mtd> </mtr> </mtable></mrow> </mfenced></mrow> </math> is continuous at x = 0, then k = ….

**Options:**

- **(A)** <math><mo>±</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(B)** <math><mo>±</mo><mn>4</mn></math>
- **(C)** <math><mo>±</mo><mn>2</mn></math>
- **(D)** <math><mo>±</mo><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mo>±</mo><mn>8</mn></math>**

**Detailed Solution:**

We have function, 
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>k</mi><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>k</mi><mi>x</mi></mrow><mrow><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>,</mo><mi>x</mi><mo>≠</mo><mn>0</mn></math>  
<math><mn>16</mn><mo>,</mo><mi>x</mi><mo>=</mo><mn>0</mn></math>  
is continuous at x = 0 
<math><mo>∴</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced></math>  
<math><mo>&#8658;</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>k</mi><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>k</mi><mi>x</mi></mrow><mrow><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>16</mn><mfenced separators="|"><mrow><mfrac><mrow><mn>0</mn></mrow><mrow><mn>0</mn></mrow></mfrac><mi>f</mi><mi>o</mi><mi>r</mi><mi>m</mi></mrow></mfenced></math>  
<math><mo>&#8658;</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>k</mi><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mi>k</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>k</mi><mi>x</mi></mrow><mrow><mi>k</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>×</mo><mfrac><mrow><msup><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mn>16</mn></math>  
<math><mo>&#8658;</mo><mfrac><mrow><msup><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mn>16</mn><mo>&#8658;</mo><msup><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>64</mn><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mo>±</mo></math>8

</details>

---

### Q95. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>3</mn></math> where <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mrow><mo>{</mo> <mrow> <mtable> <mtr> <mtd> <mrow> <mi>a</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mtext> </mtext><mtext> </mtext><mtext> </mtext><mi>f</mi><mi>o</mi><mi>r</mi><mtext> </mtext><mi>x</mi><mo>≤</mo><mn>3</mn></mrow> </mtd> </mtr> <mtr> <mtd> <mrow> <mi>b</mi><mi>x</mi><mo>+</mo><mn>3</mn><mo>,</mo><mtext> </mtext><mtext> </mtext><mtext> </mtext><mi>f</mi><mi>o</mi><mi>r</mi><mtext> </mtext><mi>x</mi><mo>&gt;</mo><mn>3</mn></mrow> </mtd> </mtr> </mtable></mrow> </mrow></mrow> </math> , then

**Options:**

- **(A)** <math><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

We have, <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>3</mn></math>
Where <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mi>a</mi><mi>x</mi><mo>+</mo><mn>1</mn><mtext>    </mtext><mi>f</mi><mi>o</mi><mi>r</mi></mtd><mtd><mi>x</mi><mo>≤</mo><mn>3</mn></mtd></mtr><mtr><mtd><mi>b</mi><mi>x</mi><mo>+</mo><mn>3</mn><mtext>   </mtext><mi>f</mi><mi>o</mi><mi>r</mi></mtd><mtd><mi>x</mi><mo>&gt;</mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math><mo>∴</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced><mtext>    </mtext><mo>…</mo><mfenced separators="|"><mrow><mi>i</mi></mrow></mfenced></math>
Now, <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mi>h</mi></mrow></mfenced></math>
<math><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mi>h</mi></mrow></mfenced><mo>+</mo><mn>1</mn></math>
<math><mo>=</mo><mn>3</mn><mi>a</mi><mo>+</mo><mn>1</mn><mtext>           </mtext><mo>…</mo><mfenced separators="|"><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>
<math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mi>h</mi></mrow></mfenced></math>
<math><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>h</mi><mo>→</mo><mn>0</mn></mrow></munder><mi>b</mi><mfenced separators="|"><mrow><mn>3</mn><mo>+</mo><mi>h</mi></mrow></mfenced><mo>+</mo><mn>3</mn></math>
<math><mo>=</mo><mn>3</mn><mi>b</mi><mo>+</mo><mn>3</mn><mtext>          </mtext><mo>…</mo></math> (iii)
and <math><mi>f</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced><mo>=</mo><mn>3</mn><mi>a</mi><mo>+</mo><mn>1</mn><mtext>      </mtext><mo>…</mo></math> (iv)
Since, <math><mi></mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>3</mn></math>
<math><mo>∴</mo><mi></mi></math> From Eqs. (i), (ii), (iii) and (iv)
we get <math><mn>3</mn><mi>a</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>3</mn><mi>b</mi><mo>+</mo><mn>3</mn></math>
<math><mo>⇒</mo><mn>3</mn><mi>a</mi><mo>-</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>2</mn></math>
<math><mo>⇒</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

</details>

---

### Q96. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></msup><mo>-</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>,</mo></math> for <math><mi>x</mi><mo>≠</mo><mn>0</mn></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math>, then the value of <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mn>1</mn></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

Since <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow></mrow> </math> is continuous at <math> <mrow> <mi>x</mi><mo>=</mo><mn>0</mn></mrow> </math>
Hence <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mn>0</mn> <mo>)</mo></mrow><mo>=</mo><munder> <mrow> <mi>lim</mi></mrow> <mrow> <mi>x</mi><mo>→</mo><mn>0</mn></mrow> </munder> <mfrac> <mrow> <msup> <mi>e</mi> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </msup> <mo>−</mo><mi>cos</mi><mi>x</mi></mrow> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <mo>=</mo> <munder> <mrow> <mi>lim</mi></mrow> <mrow> <mi>x</mi><mo>→</mo><mn>0</mn></mrow> </munder> <mfrac> <mrow> <msup> <mi>e</mi> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </msup> <mo>−</mo><mn>1</mn></mrow> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> <mo>+</mo><munder> <mrow> <mi>lim</mi></mrow> <mrow> <mi>x</mi><mo>→</mo><mn>0</mn></mrow> </munder> <mfrac> <mrow> <mn>1</mn><mo>−</mo><mi>cos</mi><mi>x</mi></mrow> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <mo>=</mo> <munder> <mtext>lim</mtext> <mrow> <mtext>x</mtext> <mo>→</mo> <mn>0</mn> </mrow> </munder> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <msup> <mtext>e</mtext> <msup> <mtext>x</mtext> <mn>2</mn> </msup> </msup> <mo>-</mo> <mn>1</mn> </mrow> <mrow> <msup> <mtext>x</mtext> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </mfenced> <mo>+</mo><munder> <mrow> <mi>lim</mi></mrow> <mrow> <mi>x</mi><mo>→</mo><mn>0</mn></mrow> </munder> <mfrac> <mrow> <mn>2</mn> <msup> <mtext>sin</mtext> <mn>2</mn> </msup> <mfrac> <mrow> <mtext>x</mtext> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> <mrow> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mtext>x</mtext> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> </mrow> </mfrac> <mo>×</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <mo>=</mo><mn>1</mn><mo>+</mo><mfrac> <mrow> <msup> <mn>1</mn> <mn>2</mn> </msup> </mrow> <mn>2</mn> </mfrac> <mo>=</mo><mfrac> <mn>3</mn> <mn>2</mn> </mfrac> </mrow> </math>

</details>

---

### Q97. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>α</mi></math> for <math><mi>x</mi><mo>≥</mo><mn>0 </mn></math><math><mo>=</mo><mn>2</mn><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mi>β</mi></math> for <math><mi>x</mi><mo>&lt;</mo><mn>0</mn></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn></math> then <math><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>β</mi></mrow><mrow><mn>2</mn></mrow></msup></math> is

**Options:**

- **(A)** <math > <mn>3</mn></math>
- **(B)** <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>25</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>25</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math> <mrow> <munder> <mrow> <mi>lim</mi></mrow> <mrow> <mi>x</mi><mo>→</mo><mrow> <msup> <mn>0</mn> <mo>+</mo> </msup></mrow> </mrow></munder> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mi>α</mi><mo>=</mo><munder> <mrow> <mi>lim</mi></mrow> <mrow> <mi>x</mi><mo>→</mo><mrow> <msup> <mn>0</mn> <mo>-</mo> </msup></mrow> </mrow></munder> <mn>2</mn><msqrt> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>1</mn></mrow> </msqrt> <mo>+</mo><mi>β</mi></mrow> </math>
<math> <mrow> <mi>α</mi><mo>=</mo><mn>2</mn><mo>+</mo><mi>β</mi><mn>.........</mn><mrow><mo>(</mo> <mn>1</mn> <mo>)</mo></mrow></mrow> </math>
<math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mi>α</mi><mo>;</mo><mtext> </mtext><mi>x</mi><mo>≥</mo><mn>0</mn></mrow> </math>
<math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mrow> <mfrac> <mn>1</mn> <mn>2</mn> </mfrac> </mrow> <mo>)</mo></mrow><mo>=</mo><mfrac> <mn>1</mn> <mn>4</mn> </mfrac> <mo>+</mo><mi>α</mi></mrow> </math>
<math> <mrow> <mn>2</mn><mo>=</mo><mfrac> <mn>1</mn> <mn>4</mn> </mfrac> <mo>+</mo><mi>α</mi></mrow> </math>
<math> <mrow> <mfrac> <mn>7</mn> <mn>4</mn> </mfrac> <mo>=</mo><mi>α</mi></mrow></math>
<math> <mrow> <mfrac> <mn>7</mn> <mn>4</mn> </mfrac> <mo>−</mo><mn>2</mn><mo>=</mo><mi>β</mi></mrow></math>
<math> <mrow> <mo>⇒</mo> <mi>β</mi> <mo>=</mo> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>
Hence <math> <mrow> <msup> <mi>α</mi> <mn>2</mn> </msup> <mo>+</mo><msup> <mi>β</mi> <mn>2</mn> </msup> <mo>=</mo><mfrac> <mrow> <mn>49</mn></mrow> <mrow> <mn>16</mn></mrow> </mfrac> <mo>+</mo><mfrac> <mn>1</mn> <mrow> <mn>16</mn></mrow> </mfrac> <mo>=</mo><mfrac> <mrow> <mn>50</mn></mrow> <mrow> <mn>16</mn></mrow> </mfrac> <mo>=</mo><mfrac> <mrow> <mn>25</mn></mrow> <mn>8</mn> </mfrac> </mrow> </math>

</details>

---

### Q98. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo> = </mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi></mtd><mtd><mo>≤</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi></mtd><mtd><mo>&gt;</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math> then <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> at <math><mi>x</mi><mo>=</mo><mn>0</mn></math> is

**Options:**

- **(A)** Continuous but not differentiable
- **(B)** Not continuous but differentiable
- **(C)** Continuous and differentiable
- **(D)** Not continuous and not differentiable

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Continuous but not differentiable**

**Detailed Solution:**

Continuity at <math><mi>x</mi><mo>=</mo><mn>0</mn></math>
<math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder></mrow><mo>⁡</mo><mrow><mi>f</mi><mi> </mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo></mrow></mrow><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow></mrow></math>
<math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder></mrow><mo>⁡</mo><mrow><mi>f</mi><mi> </mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></mrow></mrow></math>
<math><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>0</mn></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi> </mi><mi>x</mi><mo>=</mo><mn>0</mn></math>
For differentiability 
<math>  <mrow>   <mi>f</mi><mo>&#x0027;</mo><mrow><mo>(</mo>    <mrow>     <msup>      <mn>0</mn>      <mo>+</mo>     </msup>     </mrow>   <mo>)</mo></mrow><mo>=</mo><mi>0</mi></mrow>  <br 
</math><math>  <mrow>   <mi>f</mi><mo>&#x0027;</mo><mrow><mo>(</mo>    <mrow>     <msup>      <mn>0</mn>      <mo>&#x2212;</mo>     </msup>     </mrow>   <mo>)</mo></mrow><mo>=</mo><mn>1</mn></mrow></math>
<math><mo>∴</mo><mi> </mi><mi> </mi></math> Not differentiable
<b>Alternative</b>
Diagram:
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/unzjkgjqssofhgoycpiwccnbvxkczpjtiidzkytustttjkqhlq.jpeg" />
It has sharp edge at <math><mi>x</mi><mo>=</mo><mn>0</mn></math>
<math><mo>∴</mo><mi> </mi><mi> </mi></math> not differentiable but continuous

</details>

---

### Q99. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">cot</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></msup></mrow></mrow></mtd><mtd><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi></mtd><mtd><mi>x</mi><mo>≠</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>K</mi></mtd><mtd><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math> then <math> <mi>K</mi> </math> is

**Options:**

- **(A)** <math><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** <math><mi>e</mi></math>
- **(D)** <math><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>1</mn></math>**

**Detailed Solution:**

Since <math>   <mrow>   <mi>f</mi><mo stretchy='false'>(</mo><mi>x</mi><mo stretchy='false'>)</mo></mrow>  </math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math>
<math>   <mo>&#x21D2;</mo>  </math><math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><msup><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></mrow><mrow><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow></mrow></msup></mrow></mrow></math>
<math>   <mo>&#x21D2;</mo>  </math><math><mi>k</mi><mo>=</mo><mi> </mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">cot</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi><mo>⋅</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mo>⁡</mo><mo>(</mo><mn>1</mn><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>)</mo></mrow></mrow></mrow></mrow><mi> </mi></math>
<math><mo>=</mo><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mo>⁡</mo><mo>(</mo><mn>1</mn><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>)</mo></mrow><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mrow></math>
<math>   <mo>&#x21D2;</mo>  </math><math><mi>k</mi><mo>=</mo><mn>1</mn></math>

</details>

---

### Q100. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

If the function <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup></mtd><mtd><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi></mtd><mtd><mi>x</mi><mo>≠</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>K</mi></mtd><mtd><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math> <mrow> <mi>k</mi><mo>=</mo><mo>?</mo> </mrow> </math>

**Options:**

- **(A)** <math><mi>e</mi></math>
- **(B)** <math><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

Since <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> </math> is continuous at <math> <mrow> <mi>x</mi><mo>=</mo><mn>0</mn> </mrow> </math>
<math><mo>⇒</mo><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi> </mi></mrow></mrow></math>
<math><mo>=</mo><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mi>π</mi></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup></mrow></mrow></math>
<math><mo>=</mo><msup><mrow><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mn>1</mn><mo>-</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mfenced></mrow></mrow></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup></math>
<math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><mfrac><mrow><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup></mrow><mrow><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mo>-</mo><mfrac><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></msup></mrow></mfrac></mrow></mrow></math>
Taking limits
<math><mo>=</mo><mi> </mi><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mo>+</mo><mn>1</mn></mrow></msup></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfrac><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>1</mn></mrow></msup><mo>⋅</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>1</mn></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

</details>

---

### Q101. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

For what value of <math> <mrow> <mi>k</mi><mo>,</mo> </mrow> </math> the function defined by <math >
 <mi>f</mi><mrow><mo>(</mo>
  <mi>x</mi>
 <mo>)</mo></mrow><mi>&#x00A0;</mi><mo>=</mo><mi>&#x00A0;</mi><mrow><mo>{</mo> <mrow>
  <mtable>
   <mtr>
    <mtd>
     <mrow>
      <mfrac>
       <mrow>
        <mi>log</mi><mrow><mo>(</mo>
         <mrow>
          <mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi>
         </mrow>
        <mo>)</mo></mrow><mi>sin</mi><msup>
         <mi>x</mi>
         <mi>o</mi>
        </msup>
        
       </mrow>
       <mrow>
        <msup>
         <mi>x</mi>
         <mn>2</mn>
        </msup>
        
       </mrow>
      </mfrac>
      <mi>&#x00A0;</mi>
     </mrow>
    </mtd>
    <mtd>
     <mrow>
      <mtext>for</mtext>
     </mrow>
    </mtd>
    <mtd>
     <mrow>
      <mi>x</mi><mo>&#x2260;</mo><mn>0</mn>
     </mrow>
    </mtd>
   </mtr>
   <mtr>
    <mtd>
     <mi>k</mi>
    </mtd>
    <mtd>
     <mrow>
      <mtext>for</mtext>
     </mrow>
    </mtd>
    <mtd>
     <mrow>
      <mi>x</mi><mo>=</mo><mn>0</mn>
     </mrow>
    </mtd>
   </mtr>
   
  </mtable>
 </mrow> </mrow>
</math>




is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math> ?

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>90</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>90</mn></mrow><mrow><mi>π</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>90</mn></mrow></mfrac></math>**

**Detailed Solution:**

Since f(x) is continuous at x = 0, hence <math>  <mrow>   <munder>    <mrow>     <mi>lim</mi></mrow>    <mrow>     <mi>x</mi><mo>&#x2192;</mo><mn>0</mn></mrow>   </munder>   <mi>f</mi><mrow><mo>(</mo>    <mi>x</mi>   <mo>)</mo></mrow><mo>=</mo><mi>f</mi><mrow><mo>(</mo>    <mn>0</mn>   <mo>)</mo></mrow></mrow></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi> </mi><mo>.</mo><mi> </mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><msup><mrow><mi>x</mi></mrow><mrow><mi>o</mi></mrow></msup></mrow></mrow></mrow></mrow></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mi>k</mi></mrow></mrow></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>2</mn><mi> </mi><mo>.</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mrow></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mrow></mrow><mi> </mi><mo>⋅</mo><mfrac><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mi>x</mi><mo>×</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>180</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></mrow><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>×</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>180</mn></mrow></mfrac></mrow></mfenced></mrow></mfrac><mo>×</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>180</mn></mrow></mfrac><mo>=</mo><mi>k</mi></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mn>2</mn><mo>×</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>180</mn></mrow></mfrac><mo>=</mo><mi>k</mi></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mfrac><mrow><mi>π</mi></mrow><mrow><mn>90</mn></mrow></mfrac><mo>=</mo><mi>k</mi></math>

</details>

---

### Q102. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

If the function <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> defined by <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mrow><mi> </mi></mtd><mtd><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi></mtd><mtd><mi>x</mi><mo>≠</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>k</mi></mtd><mtd><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math> , then <math><mi>k</mi><mo>=</mo></math> _______

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** <math><mo>-</mo><mn>1</mn></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>0</mn></math>**

**Detailed Solution:**

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mrow><mi> </mi></mtd><mtd><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi></mtd><mtd><mi>x</mi><mo>≠</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>k</mi></mtd><mtd><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>
Since <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow></mrow> </math> is continuous at <math> <mrow> <mi>x</mi><mo>=</mo><mn>0</mn></mrow> </math>
<math> <mrow> <mo>⇒</mo><munder> <mrow> <mi>lim</mi></mrow> <mrow> <mi>x</mi><mo>→</mo><mn>0</mn></mrow> </munder> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mi>f</mi><mrow><mo>(</mo> <mn>0</mn> <mo>)</mo></mrow></mrow> </math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mn>0</mn></mrow></munder></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mrow><mo>=</mo><mi>k</mi></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mn>0</mn><mo>=</mo><mi>k</mi></math>
<math> <mrow> <mrow><mo>(</mo> <mrow> <mo>∵</mo><mi>sin</mi><mrow><mo>(</mo> <mrow> <mfrac> <mn>1</mn> <mi>x</mi> </mfrac> </mrow> <mo>)</mo></mrow><mo>∈</mo><mtext> </mtext><mtext> </mtext><mrow><mo>[</mo> <mrow> <mo>−</mo><mn>1</mn><mo>,</mo><mtext> </mtext><mn>1</mn></mrow> <mo>]</mo></mrow><mi>f</mi><mi>o</mi><mi>r</mi><mtext> </mtext><mi>a</mi><mi>l</mi><mi>l</mi><mtext> </mtext><mi>x</mi><mo>≠</mo><mn>0</mn></mrow> <mo>)</mo></mrow></mrow> </math>

</details>

---

### Q103. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\left\{\begin{array}{c}x \sin \left(\frac{1}{x}\right), x \neq 0 \text { , then at } x=0 \text { the } \\ 0, x=0\end{array}\right.$
function $f(x)$ is

**Options:**

- **(A)** continuous
- **(B)** differentiable
- **(C)** continuous but not differentiable
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) continuous but not differentiable**

**Detailed Solution:**

Given, $f(x)=\left\{\begin{array}{c}x \sin \left(\frac{1}{x}\right), x \neq 0 \\ 0, \quad x=0\end{array}\right.$
For continuity at $x=0$,
$\mathrm{LHL}=f(0-0)=\lim _{h \rightarrow 0} f(0-h)$
$\begin{aligned} &=\lim _{h \rightarrow 0}(-h) \sin \left(-\frac{1}{h}\right) \\ &=0 \times(\text { finite quantity }) \\ &=0 \\ \text { RHL } &=f(0+0)=\lim _{h \rightarrow 0} f(0+h) \\ &=\lim _{h \rightarrow 0}(h) \sin \left(\frac{1}{h}\right) \end{aligned}$
$=0 \times($ finite quantity $)$
$=0$
and $f(0)=0$
$\therefore \quad f(0)=\mathrm{LHL}=\mathrm{RHL}$
$\therefore f(x)$ is continuous at $x=0 .$
For differentiability at $x=0$, 
$R f^{\prime}(0)=\lim _{h \rightarrow 0} \frac{f(0+h)-f(0)}{h}$
$\begin{aligned} &=\lim _{h \rightarrow 0} \frac{h \sin \left(\frac{1}{h}\right)-0}{h} \\ &=\lim _{h \rightarrow 0} \sin \left(\frac{1}{h}\right) \\ &=(\text { a finite quantity persist between }-1\\ & &\text { to }+1) \\ &=\text { does not exist } \\ L f^{\prime}(0) &=\lim _{h \rightarrow 0} \frac{f(0-h)-f(0)}{-h} \\ &=\lim _{h \rightarrow 0} \frac{(-h) \sin \left(-\frac{1}{h}\right)-0}{-h} \\=& \lim _{h \rightarrow 0}\left\{-\sin \left(\frac{1}{h}\right)\right\} \\=&(\text { finite quantity persist between }\\ & &-1 \text { to }+1) \\ &=\text { does not exist } \\ \because R f^{\prime}(0) \neq L^{\prime}(0) & \end{aligned}$
$\therefore f(x)$ is not differentiable at $x=0$.

</details>

---

### Q104. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\left\{\begin{array}{cl}\frac{\log (1+2 a x)-\log (1-b x)}{x}, & x \neq 0 \\ k & , x=0\end{array}\right.$
continuous at $x=0$, then value of $k$ is

**Options:**

- **(A)** $b+a$
- **(B)** $b-2 a$
- **(C)** $2 a-b$
- **(D)** $2 a+b$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 a+b$**

**Detailed Solution:**

Given, $f(x)=\left\{\begin{array}{cl}\frac{\log (1+2 a x)-\log (1-b x)}{x}, & x \neq 0 \\ k & , x=0\end{array}\right.$
is continuous at $x=0$. $\therefore f(0)=\lim _{x \rightarrow 0} \frac{\log (1+2 a x)-\log (1-b x)}{x}$
$\left(\frac{0}{0}\right.$ form $)$
$\Rightarrow k=\lim _{x \rightarrow 0} \frac{\frac{1}{2 a x+1}(2 a)-\frac{1}{1-b x}(-b)}{+1}$
(by 'L' Hospital's rule) $\Rightarrow k=\frac{2 a}{0+1}+\frac{b}{1-0}=2 a+b$

</details>

---

### Q105. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `3`

If $f(x)=\left\{\begin{array}{cc}(1+|\sin x|)^{\frac{a}{|\sin x|}}, & -\pi / 6 < x < 0 \\ b & x=0 \\ \frac{\tan 2 x}{e^{\tan 3 x}}, & 0 < x < \pi / 6\end{array}\right.$
is continuous at $x=0$, find the values of $a$ and $b$.

**Options:**

- **(A)** $3 / 2, e^{3 / 2}$
- **(B)** $-2 / 3, e^{-3 / 2}$
- **(C)** $2 / 3, e^{2 / 3}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 / 3, e^{2 / 3}$**

**Detailed Solution:**

We have, $\lim _{x \rightarrow 0^{-}} f(x)$
$$
\begin{aligned}
=& \lim _{x \rightarrow 0}\{1+|\sin x|\}^{\frac{a}{|\sin x|}} \\
=& \lim _{x \rightarrow 0}|\sin x| \cdot \frac{a}{|\sin x|}=e^{a} \\
\text { and } \quad \lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0} e^{\frac{\tan 2 x}{\tan 3 x}} \\
=& \lim _{x \rightarrow 0} \frac{\tan 2 x}{2 x} \cdot \frac{3 x}{\tan 3 x} \times \frac{2}{3} \\
=& e^{2 / 3}
\end{aligned}
$$
For $f(x)$ to be continuous at $x=0$, we must have
$$
\begin{aligned}
& \lim _{x \rightarrow 0^{-}} f(x) &=\lim _{x \rightarrow 0^{+}} f(x) \\
& &=f(0) \\
\Rightarrow & e^{a} &=e^{2 / 3}=b \\
\Rightarrow & a &=2 / 3 \\
\text { and } & b &=e^{2 / 3}
\end{aligned}
$$

</details>

---

### Q106. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

The value of $a$ and $b$ such that the function $f(x)=\left\{\begin{array}{ll}-2 \sin x, & -\pi \leq x \leq-\frac{\pi}{2} \\ a \sin x+b, & -\frac{\pi}{2} < x < \frac{\pi}{2} \text { is continuous } \\ \cos x, & \frac{\pi}{2} \leq x \leq \pi\end{array}\right.$
in $[-\pi, \pi]$, are

**Options:**

- **(A)** $-1,0$
- **(B)** 1,0
- **(C)** 1,1
- **(D)** $-1,1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-1,1$**

**Detailed Solution:**

For continuity in $[-\pi, \pi]$, we must have
$$
\begin{array}{l}
\text { At } x=-\frac{\pi}{2}, f\left(-\frac{\pi}{2}\right)=\lim _{x \rightarrow\left(-\frac{\pi}{2}\right)^{-}}(-2 \sin x) \\
=\lim _{x \rightarrow\left(-\frac{\pi}{2}\right)^{+}}(a \sin x+b) \\
\Rightarrow \quad 2=-a+b
\end{array}
$$
At $x=\frac{\pi}{2}$,
$$
f\left(\frac{\pi}{2}\right)=\lim _{x \rightarrow\left(\frac{\pi}{2}\right)^{-}}(a \sin x+b)=\lim _{x \rightarrow\left(\frac{\pi}{2}\right)^{+}} \cos x
$$
$$
\Rightarrow \quad 0=a+b
$$
$\cdots$
On solving Eqs. (i) and (ii) we get, $a=-1, b=1$

</details>

---

### Q107. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\left\{\begin{array}{cl}x \sin \frac{1}{x} & , x \neq 0 \\ k & , x=0\end{array}\right.$ is continuous at
$x=0$, then the value of $k$ is

**Options:**

- **(A)** 1
- **(B)** $-1$
- **(C)** 0
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

If function $f(x)$ is continuous at $x=0$, then
$$
f(0)=\lim _{x \rightarrow 0} f(x)
$$
Given, $\quad f(0)=k$
$$
\begin{array}{ll}
\therefore \quad f(0)=k=\lim _{x \rightarrow 0} x \sin \frac{1}{x} \\
\Rightarrow \quad k=0 \quad\left(\because-1 \leq \sin \frac{1}{x} \leq 1\right)
\end{array}
$$

</details>

---

### Q108. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `3`

The function $f(x)=e^{-|x|}$ is

**Options:**

- **(A)** continuous everywhere but not differentiable at $x=0$
- **(B)** continuous and differentiable everywhere
- **(C)** not continuous at $x=0$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) continuous everywhere but not differentiable at $x=0$**

**Detailed Solution:**

Given, $f(x)=\left\{\begin{array}{r}e^{-x}, x \geq 0 \\ e^{x}, x < 0\end{array}\right.$
$$
\begin{array}{l}
\text { LHL }=\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0} e^{x}=1 \\
\text { RHL }=\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0} e^{-x}=1 \\
\text { Also, } \quad f(0)=e^{0}=1
\end{array}
$$
$\because$
$$
\mathrm{LHL}=\mathrm{RHL}=f(0)
$$
$\therefore$ It is continuous for every value of $x$.
Now, LHD at $x=0$
$$
\left(\frac{d}{d x} e^{x}\right)_{x=0}=\left[e^{x}\right]_{x=0}=e^{0}=1
$$
RHD at $x=0$
$$
\left(\frac{d}{d x} e^{-x}\right)_{x=0}=\left[-e^{-x}\right]_{x=0}=-1
$$
So, $f(x)$ is not differentiable at $x=0$. Hence, $f(x)=e^{-\dashv x \mid}$ is continuous everywhere but not differentiable at $x=0$.
Alternative<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/9KxGmFYEhtj4CbVcJ2j8inBsM3nfzoWK1jJMaprXGRM.original.fullsize.png">

Hence, it is clear from the figure that $f(x)$ is continuous everywhere and not differentiable at $x=0 .$
$$

</details>

---

