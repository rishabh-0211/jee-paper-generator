# MHT CET Mathematics - Functions

## Topic 5: Composite Function

**Total Questions:** 39

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \log_e\left(\dfrac{1-x}{1+x}\right)$, $|x| < 1$, then $f\left(\dfrac{4x}{4+x^2}\right)$ is equal to

**Options:**

- **(A)** $2f(x)$
- **(B)** $-2f(x)$
- **(C)** $2f\left(\dfrac{x}{2}\right)$
- **(D)** $-2f\left(\dfrac{x}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2f\left(\dfrac{x}{2}\right)$**

**Detailed Solution:**

Given $f(x) = \log_e\left(\dfrac{1-x}{1+x}\right)$

Substituting $\dfrac{4x}{4+x^2}$ in place of $x$:

$f\left(\dfrac{4x}{4+x^2}\right) = \log_e\left(\dfrac{1 - \dfrac{4x}{4+x^2}}{1 + \dfrac{4x}{4+x^2}}\right)$

$f\left(\dfrac{4x}{4+x^2}\right) = \log_e\left(\dfrac{4+x^2-4x}{4+x^2+4x}\right)$

$f\left(\dfrac{4x}{4+x^2}\right) = \log_e\left(\dfrac{(2-x)^2}{(2+x)^2}\right)$

$f\left(\dfrac{4x}{4+x^2}\right) = 2 \log_e\left(\dfrac{2-x}{2+x}\right)$

Dividing the numerator and denominator by $2$:

$f\left(\dfrac{4x}{4+x^2}\right) = 2 \log_e\left(\dfrac{1 - \dfrac{x}{2}}{1 + \dfrac{x}{2}}\right)$

$f\left(\dfrac{4x}{4+x^2}\right) = 2 f\left(\dfrac{x}{2}\right)$

Answer: $2f\left(\dfrac{x}{2}\right)$

</details>

---

### Q2. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \dfrac{1}{\sqrt{x}}, g(x) = 3 - 2x - x^2$ then $\int \left[(f \circ g)(e^x)\right] \cdot e^x dx = \cdots\cdots\cdots$

**Options:**

- **(A)** $\dfrac{1}{2}\sin^{-1}\left(\dfrac{e^x + 1}{2}\right) + c$
- **(B)** $\sin^{-1}\left(\dfrac{e^x - 1}{4}\right) + c$
- **(C)** $\sin^{-1}\left(\dfrac{e^x + 2}{2}\right) + c$
- **(D)** $\sin^{-1}\left(\dfrac{e^x + 1}{2}\right) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sin^{-1}\left(\dfrac{e^x + 1}{2}\right) + c$**

**Detailed Solution:**

Given $f(x) = \dfrac{1}{\sqrt{x}}$ and $g(x) = 3 - 2x - x^2$.

First, we find the composition $(f \circ g)(x)$:

$(f \circ g)(x) = f(g(x)) = \dfrac{1}{\sqrt{3 - 2x - x^2}}$

Substituting $x = e^x$, we get:

$(f \circ g)(e^x) = \dfrac{1}{\sqrt{3 - 2e^x - e^{2x}}}$

The given integral is:

$I = \int \left[(f \circ g)(e^x)\right] \cdot e^x dx = \int \dfrac{e^x}{\sqrt{3 - 2e^x - e^{2x}}} dx$

Let $e^x = t$, which gives $e^x dx = dt$. The integral becomes:

$I = \int \dfrac{1}{\sqrt{3 - 2t - t^2}} dt$

Completing the square for the expression inside the square root:

$3 - 2t - t^2 = 3 - (t^2 + 2t) = 3 - (t^2 + 2t + 1 - 1) = 4 - (t + 1)^2$

Substituting this back into the integral:

$I = \int \dfrac{1}{\sqrt{2^2 - (t + 1)^2}} dt$

Using the standard formula $\int \dfrac{1}{\sqrt{a^2 - x^2}} dx = \sin^{-1}\left(\dfrac{x}{a}\right) + c$, we get:

$I = \sin^{-1}\left(\dfrac{t + 1}{2}\right) + c$

Substituting $t = e^x$ back into the expression:

$I = \sin^{-1}\left(\dfrac{e^x + 1}{2}\right) + c$

Answer: $\sin^{-1}\left(\dfrac{e^x + 1}{2}\right) + c$

</details>

---

### Q3. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x) = \dfrac{2}{x + 5}$ and $g(x) = x^2 - 1$, then the positive value of $x$ satisfying $(f \circ g)(x) = \dfrac{1}{10}$ is

**Options:**

- **(A)** $4$
- **(B)** $2$
- **(C)** $6$
- **(D)** $16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4$**

**Detailed Solution:**

Given $f(x) = \dfrac{2}{x + 5}$ and $g(x) = x^2 - 1$.

The composite function $(f \circ g)(x)$ is given by:

$(f \circ g)(x) = f(g(x)) = f(x^2 - 1)$

Substituting $x^2 - 1$ into $f(x)$:

$(f \circ g)(x) = \dfrac{2}{(x^2 - 1) + 5} = \dfrac{2}{x^2 + 4}$

We are given that $(f \circ g)(x) = \dfrac{1}{10}$.

$\dfrac{2}{x^2 + 4} = \dfrac{1}{10}$

$x^2 + 4 = 20$

$x^2 = 16$

$x = \pm 4$

Since the positive value of $x$ is required, we get $x = 4$.

Answer: $4$

</details>

---

### Q4. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x) = 1 - \dfrac{1}{x}, g_2(x) = f(f(x)), g_3(x) = f(f(f(x)))$ and so on. If $\int x \cdot g_{2026}(x)\,dx = \int g_{2025}(x)\,dx + h(x) + c$, then $h(x) = $...

**Options:**

- **(A)** $x$
- **(B)** $-x$
- **(C)** $\log x$
- **(D)** $-\log x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-x$**

**Detailed Solution:**

Given $f(x) = 1 - \dfrac{1}{x} = \dfrac{x-1}{x}$

$g_2(x) = f(f(x)) = 1 - \dfrac{1}{\dfrac{x-1}{x}} = 1 - \dfrac{x}{x-1} = \dfrac{-1}{x-1} = \dfrac{1}{1-x}$

$g_3(x) = f(g_2(x)) = 1 - \dfrac{1}{\dfrac{1}{1-x}} = 1 - (1-x) = x$

$g_4(x) = f(g_3(x)) = f(x)$

The sequence of functions is periodic with a period of $3$.

Since $2025$ is a multiple of $3$, $g_{2025}(x) = g_3(x) = x$.

Consequently, $g_{2026}(x) = g_1(x) = 1 - \dfrac{1}{x}$.

Substituting these into the given integral equation:

$\int x \cdot g_{2026}(x)\,dx = \int g_{2025}(x)\,dx + h(x) + c$

$\int x \left(1 - \dfrac{1}{x}\right) dx = \int x \,dx + h(x) + c$

$\int (x - 1) \,dx = \dfrac{x^2}{2} + h(x) + c$

$\dfrac{x^2}{2} - x = \dfrac{x^2}{2} + h(x) + c'$

Comparing both sides, we get $h(x) = -x$.

Answer: $-x$

</details>

---

### Q5. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $g(x) = 1 - \sqrt{x}$ and $f(g(x)) = 5 + 4\sqrt{x} + x$, then the value of $f(6)$ is...

**Options:**

- **(A)** $5$
- **(B)** $10$
- **(C)** $15$
- **(D)** $20$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $10$**

**Detailed Solution:**

Given $g(x) = 1 - \sqrt{x}$ and $f(g(x)) = 5 + 4\sqrt{x} + x$.

Let $y = g(x) = 1 - \sqrt{x}$.

Then $\sqrt{x} = 1 - y$ and $x = (1 - y)^2$.

Substituting these into the equation for $f(g(x))$:

$f(y) = 5 + 4(1 - y) + (1 - y)^2$

To find $f(6)$, substitute $y = 6$ into the equation:

$f(6) = 5 + 4(1 - 6) + (1 - 6)^2$

$f(6) = 5 + 4(-5) + (-5)^2$

$f(6) = 5 - 20 + 25 = 10$

Answer: $10$

</details>

---

### Q6. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x) = x^2$ and $g(x) = [x^2]$ where $[\cdot]$ represents the greatest integer function then, $(f \circ g)\left(\dfrac{3}{2}\right) + (g \circ f)\left(\dfrac{3}{2}\right)$ is equal to ...

**Options:**

- **(A)** $2$
- **(B)** $5$
- **(C)** $9$
- **(D)** $10$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $9$**

**Detailed Solution:**

Given $f(x) = x^2$ and $g(x) = [x^2]$.

First, evaluating $(f \circ g)\left(\dfrac{3}{2}\right)$:

$g\left(\dfrac{3}{2}\right) = \left[\left(\dfrac{3}{2}\right)^2\right] = \left[\dfrac{9}{4}\right] = [2.25] = 2$

$f\left(g\left(\dfrac{3}{2}\right)\right) = f(2) = 2^2 = 4$

Next, evaluating $(g \circ f)\left(\dfrac{3}{2}\right)$:

$f\left(\dfrac{3}{2}\right) = \left(\dfrac{3}{2}\right)^2 = \dfrac{9}{4}$

$g\left(f\left(\dfrac{3}{2}\right)\right) = g\left(\dfrac{9}{4}\right) = \left[\left(\dfrac{9}{4}\right)^2\right] = \left[\dfrac{81}{16}\right] = [5.0625] = 5$

Adding both values:

$(f \circ g)\left(\dfrac{3}{2}\right) + (g \circ f)\left(\dfrac{3}{2}\right) = 4 + 5 = 9$

Answer: $9$

</details>

---

### Q7. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x) = ax + b$ and $g(x) = cx + d$. The condition $f(g(x)) = g(f(x))$ holds for all $x$ if and only if ...

**Options:**

- **(A)** $f(a) = f(c)$
- **(B)** $f(b) = g(b)$
- **(C)** $f(d) = g(b)$
- **(D)** $f(c) = g(a)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $f(d) = g(b)$**

**Detailed Solution:**

Given $f(x) = ax + b$ and $g(x) = cx + d$.

Substituting $g(x)$ into $f(x)$:

$f(g(x)) = a(cx + d) + b = acx + ad + b$

Substituting $f(x)$ into $g(x)$:

$g(f(x)) = c(ax + b) + d = acx + cb + d$

For $f(g(x)) = g(f(x))$ to hold for all $x$, the corresponding coefficients and constant terms must be equal:

$acx + ad + b = acx + cb + d$

$ad + b = cb + d$

Now, evaluating $f(d)$ and $g(b)$:

$f(d) = ad + b$

$g(b) = cb + d$

Therefore, the required condition is $f(d) = g(b)$.

Answer: $f(d) = g(b)$

</details>

---

### Q8. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x) = \dfrac{1 - x}{1 + x}$, then $f(f(\cos x)) =$

**Options:**

- **(A)** $\cos x$
- **(B)** $x$
- **(C)** $\tan\dfrac{x}{2}$
- **(D)** $\cos\dfrac{x}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\cos x$**

**Detailed Solution:**

Given $f(x) = \dfrac{1 - x}{1 + x}$

Evaluating $f(f(x))$:

$f(f(x)) = \dfrac{1 - f(x)}{1 + f(x)}$

$f(f(x)) = \dfrac{1 - \dfrac{1 - x}{1 + x}}{1 + \dfrac{1 - x}{1 + x}}$

$f(f(x)) = \dfrac{(1 + x) - (1 - x)}{(1 + x) + (1 - x)}$

$f(f(x)) = \dfrac{2x}{2} = x$

Substituting $x = \cos x$ into the above result:

$f(f(\cos x)) = \cos x$

Answer: $\cos x$

</details>

---

### Q9. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f : R \to R$ and $g : R \to R$ are defined as $f(x) = 2x - |x|$ and $g(x) = 2x + |x|$, then

**Options:**

- **(A)** $(fog)(2) + (gof)(2) = 0$
- **(B)** $(fog)(2) - (gof)(-2) = 0$
- **(C)** $(fog)(2) - (fog)(-2) = 0$
- **(D)** $(gof)(2) + (gof)(-2) = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(gof)(2) + (gof)(-2) = 0$**

**Detailed Solution:**

Given $f(x) = 2x - |x|$ and $g(x) = 2x + |x|$.

Evaluating the inner functions for the required values:

$f(2) = 2(2) - |2| = 2$

$f(-2) = 2(-2) - |-2| = -4 - 2 = -6$

$g(2) = 2(2) + |2| = 4 + 2 = 6$

$g(-2) = 2(-2) + |-2| = -4 + 2 = -2$

Evaluating the composite functions:

$(f \circ g)(2) = f(g(2)) = f(6) = 2(6) - |6| = 6$

$(f \circ g)(-2) = f(g(-2)) = f(-2) = -6$

$(g \circ f)(2) = g(f(2)) = g(2) = 6$

$(g \circ f)(-2) = g(f(-2)) = g(-6) = 2(-6) + |-6| = -12 + 6 = -6$

Checking the options, for the expression in option (4):

$(g \circ f)(2) + (g \circ f)(-2) = 6 + (-6) = 0$

</details>

---

### Q10. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x) = \dfrac{4x + 3}{6x - 4}$, $x \neq \dfrac{2}{3}$ and $(\text{fof})(x) = g(x)$ where $g: \mathbb{R} - \left\{\dfrac{2}{3}\right\} \rightarrow \mathbb{R} - \left\{\dfrac{2}{3}\right\}$, then $(g\,o\,g\,o\,g\,o\,g\,o\,g)\,(3) =$

**Options:**

- **(A)** $3$
- **(B)** $\dfrac{1}{3}$
- **(C)** $3^5$
- **(D)** $\dfrac{1}{3^5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3$**

**Detailed Solution:**

Given $f(x) = \dfrac{4x + 3}{6x - 4}$

We find $g(x) = (f \circ f)(x) = f(f(x))$

$g(x) = \dfrac{4f(x) + 3}{6f(x) - 4}$

Substituting $f(x)$ into the expression:

$g(x) = \dfrac{4\left(\dfrac{4x + 3}{6x - 4}\right) + 3}{6\left(\dfrac{4x + 3}{6x - 4}\right) - 4}$

$g(x) = \dfrac{16x + 12 + 18x - 12}{24x + 18 - 24x + 16}$

$g(x) = \dfrac{34x}{34} = x$

Since $g(x) = x$, $g$ is the identity function. Any number of compositions of an identity function with itself yields the identity function.

$(g \circ g \circ g \circ g \circ g)(x) = x$

Substituting $x = 3$:

$(g \circ g \circ g \circ g \circ g)(3) = 3$

Answer: $3$

</details>

---

### Q11. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $g(x) = x^2 + x - 2$ and $\dfrac{1}{2}(g \circ f)(x) = 2x^2 - 5x + 2$ then $f(x)$ is equal to

**Options:**

- **(A)** $2x + 3$
- **(B)** $2x - 3$
- **(C)** $2x^2 + 3x + 2$
- **(D)** $2x^2 - 3x - 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2x - 3$**

**Detailed Solution:**

Given $\dfrac{1}{2}(g \circ f)(x) = 2x^2 - 5x + 2$

$(g \circ f)(x) = 4x^2 - 10x + 4$

Since $g(x) = x^2 + x - 2$, substituting $f(x)$ in place of $x$ gives:

$(f(x))^2 + f(x) - 2 = 4x^2 - 10x + 4$

$(f(x))^2 + f(x) - (4x^2 - 10x + 6) = 0$

Solving for $f(x)$ using the quadratic formula:

$f(x) = \dfrac{-1 \pm \sqrt{1 - 4(1)(-(4x^2 - 10x + 6))}}{2}$

$f(x) = \dfrac{-1 \pm \sqrt{16x^2 - 40x + 25}}{2}$

$f(x) = \dfrac{-1 \pm \sqrt{(4x - 5)^2}}{2}$

$f(x) = \dfrac{-1 \pm (4x - 5)}{2}$

Taking the positive sign:

$f(x) = \dfrac{-1 + 4x - 5}{2} = 2x - 3$

Taking the negative sign:

$f(x) = \dfrac{-1 - (4x - 5)}{2} = -2x + 2$

From the given options, $f(x) = 2x - 3$ is the correct choice.

Answer: $2x - 3$

</details>

---

### Q12. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\log \left(\frac{1+x}{1-x}\right)$ and $\mathrm{g}(x)=\frac{3 x+x^3}{1+3 x^2}$, then $($ fog $)(x)=$

**Options:**

- **(A)** $2 \mathrm{f}(x)$
- **(B)** $3 \mathrm{f}(x)$
- **(C)** $4 \mathrm{f}(x)$
- **(D)** $-\mathrm{f}(x)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 \mathrm{f}(x)$**

**Detailed Solution:**

$f(g(x)) = \log\left(\dfrac{1+g(x)}{1-g(x)}\right)$

Substituting $g(x) = \dfrac{3x+x^3}{1+3x^2}$:

$1+g(x) = 1 + \dfrac{3x+x^3}{1+3x^2} = \dfrac{1+3x^2+3x+x^3}{1+3x^2} = \dfrac{(1+x)^3}{1+3x^2}$

$1-g(x) = 1 - \dfrac{3x+x^3}{1+3x^2} = \dfrac{1+3x^2-3x-x^3}{1+3x^2} = \dfrac{(1-x)^3}{1+3x^2}$

$\dfrac{1+g(x)}{1-g(x)} = \dfrac{\dfrac{(1+x)^3}{1+3x^2}}{\dfrac{(1-x)^3}{1+3x^2}} = \left(\dfrac{1+x}{1-x}\right)^3$

$(f \circ g)(x) = \log\left(\left(\dfrac{1+x}{1-x}\right)^3\right)$

$(f \circ g)(x) = 3\log\left(\dfrac{1+x}{1-x}\right) = 3f(x)$

Answer: $3 \mathrm{f}(x)$

</details>

---

### Q13. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$f(x)=\left\{\begin{array}{cc}
3-x, & 2 < x \leqslant 3 \\
1+\frac{5 x}{3}, & -3 \leqslant x \leqslant 2
\end{array}\right.$
and $g(x)=\left\{\begin{array}{rr}-x, & -2 \leqslant x \leqslant 3 \\ x, & -3 \leqslant x < -2\end{array}\right.$ then range of $(f o g)(x)$ is

**Options:**

- **(A)** $\left[1, \frac{8}{3}\right]$
- **(B)** $\left[-4, \frac{8}{3}\right]$
- **(C)** $\left[-4, \frac{13}{3}\right]$
- **(D)** $\left[\frac{8}{3}, \frac{10}{3}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left[-4, \frac{13}{3}\right]$**

**Detailed Solution:**

First, we find the range of the inner function $g(x)$ for its given domain $x \in [-3, 3]$.

For $x \in [-3, -2)$, $g(x) = x$, which gives values in the interval $[-3, -2)$.

For $x \in [-2, 3]$, $g(x) = -x$, which gives values in the interval $[-3, 2]$.

The overall range of $g(x)$ is the union of these two intervals:
$[-3, -2) \cup [-3, 2] = [-3, 2]$.

Now, we need to find the range of $(f \circ g)(x) = f(g(x))$. Let $y = g(x)$, so $y \in [-3, 2]$.

From the definition of $f(x)$, for the interval $[-3, 2]$, the function is given by:
$f(y) = 1 + \dfrac{5y}{3}$

Since $f(y) = 1 + \dfrac{5y}{3}$ is a strictly increasing linear function, its minimum and maximum values on the interval $[-3, 2]$ will occur at the endpoints.

Minimum value at $y = -3$:
$f(-3) = 1 + \dfrac{5(-3)}{3} = 1 - 5 = -4$

Maximum value at $y = 2$:
$f(2) = 1 + \dfrac{5(2)}{3} = 1 + \dfrac{10}{3} = \dfrac{13}{3}$

Therefore, the range of $(f \circ g)(x)$ is $\left[-4, \dfrac{13}{3}\right]$.

Answer: $\left[-4, \frac{13}{3}\right]$

</details>

---

### Q14. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=3 \mathrm{x}+10, \mathrm{~g}(x)=x^2-1, x \geq 0$, then $(\mathrm{fog})^{-1}(x)=$

**Options:**

- **(A)** $\left(\frac{x-7}{3}\right)$
- **(B)** $\left(\frac{x-7}{3}\right)^{\frac{1}{2}}$
- **(C)** $\left(\frac{x-7}{3}\right)^{\frac{1}{3}}$
- **(D)** $\left(\frac{3}{x-7}\right)^{\frac{3}{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\frac{x-7}{3}\right)^{\frac{1}{2}}$**

**Detailed Solution:**

Given $f(x) = 3x + 10$ and $g(x) = x^2 - 1$ for $x \geq 0$.

First, we find the composite function $(f \circ g)(x)$:

$(f \circ g)(x) = f(g(x)) = f(x^2 - 1)$

$(f \circ g)(x) = 3(x^2 - 1) + 10$

$(f \circ g)(x) = 3x^2 - 3 + 10 = 3x^2 + 7$

To find the inverse, let $y = (f \circ g)(x)$:

$y = 3x^2 + 7$

$3x^2 = y - 7$

$x^2 = \dfrac{y - 7}{3}$

Since $x \geq 0$, taking the positive square root gives:

$x = \left(\dfrac{y - 7}{3}\right)^{\dfrac{1}{2}}$

Replacing $y$ with $x$, we get the inverse function:

$(f \circ g)^{-1}(x) = \left(\dfrac{x - 7}{3}\right)^{\dfrac{1}{2}}$

Answer: $\left(\frac{x-7}{3}\right)^{\frac{1}{2}}$

</details>

---

### Q15. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\cos (\log x)$ then
$\mathrm{f}\left(x^2\right) \cdot \mathrm{f}\left(\mathrm{y}^2\right)-\frac{1}{2}\left[\mathrm{f}\left(\frac{x^2}{\mathrm{y}^2}\right)+\mathrm{f}\left(x^2 \mathrm{y}^2\right)\right]$ has the value

**Options:**

- **(A)** $-2$
- **(B)** $-1$
- **(C)** $\frac{1}{2}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0$**

**Detailed Solution:**

Given $f(x) = \cos(\log x)$

We have:
$f(x^2) = \cos(\log x^2) = \cos(2\log x)$
$f(y^2) = \cos(\log y^2) = \cos(2\log y)$
$f\left(\dfrac{x^2}{y^2}\right) = \cos\left(\log \dfrac{x^2}{y^2}\right) = \cos(2\log x - 2\log y)$
$f(x^2 y^2) = \cos(\log(x^2 y^2)) = \cos(2\log x + 2\log y)$

Substituting these into the given expression:
$f(x^2) \cdot f(y^2) - \dfrac{1}{2}\left[f\left(\dfrac{x^2}{y^2}\right) + f(x^2 y^2)\right]$

$= \cos(2\log x) \cos(2\log y) - \dfrac{1}{2} [ \cos(2\log x - 2\log y) + \cos(2\log x + 2\log y) ]$

Using the trigonometric identity $\cos(A - B) + \cos(A + B) = 2\cos A \cos B$, we get:
$= \cos(2\log x) \cos(2\log y) - \dfrac{1}{2} [ 2\cos(2\log x) \cos(2\log y) ]$

$= \cos(2\log x) \cos(2\log y) - \cos(2\log x) \cos(2\log y)$

$= 0$

Answer: $0$

</details>

---

### Q16. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{f}(x)=\dfrac{\mathrm{ax}}{x+1}, x \neq-1$, then for $a=$ $\qquad$ , $\mathrm{f}(\mathrm{f}(\mathrm{x}) \mathrm{)}=x$.

**Options:**

- **(A)** $\sqrt{2}$
- **(B)** $-\sqrt{2}$
- **(C)** 1
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -1**

**Detailed Solution:**

Given $f(x) = \dfrac{ax}{x+1}$

We need to find $f(f(x))$:

$f(f(x)) = \dfrac{a f(x)}{f(x)+1}$

Substituting $f(x)$ into the expression:

$f(f(x)) = \dfrac{a \left(\dfrac{ax}{x+1}\right)}{\dfrac{ax}{x+1} + 1}$

$f(f(x)) = \dfrac{a^2 x}{ax + x + 1} = \dfrac{a^2 x}{(a+1)x + 1}$

It is given that $f(f(x)) = x$. Therefore:

$\dfrac{a^2 x}{(a+1)x + 1} = x$

$a^2 x = (a+1)x^2 + x$

$(a+1)x^2 + (1-a^2)x = 0$

For this equation to hold true for all valid $x$, the coefficients of $x^2$ and $x$ must be zero:

$a+1 = 0 \Rightarrow a = -1$

$1-a^2 = 0 \Rightarrow a = \pm 1$

The common value satisfying both conditions is $a = -1$.

Answer: -1

</details>

---

### Q17. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}(x)=\dfrac{x}{2-x}, \mathrm{~g}(x)=\dfrac{x+1}{x+2}$, then (gogof) $(x)=$

**Options:**

- **(A)** $\dfrac{6+x}{10-2 x}$
- **(B)** $\dfrac{6-x}{10+2 x}$
- **(C)** $\dfrac{6+x}{10+2 x}$
- **(D)** $\dfrac{6-x}{10-2 x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{6-x}{10-2 x}$**

**Detailed Solution:**

Given $\mathrm{f}(x)=\dfrac{x}{2-x}$ and $\mathrm{g}(x)=\dfrac{x+1}{x+2}$

First, find $\mathrm{g}(\mathrm{f}(x))$:

$\mathrm{g}(\mathrm{f}(x)) = \dfrac(\mathrm{f}(x)+1)(\mathrm{f}(x)+2)$

Substituting $\mathrm{f}(x)$:

$\mathrm{g}(\mathrm{f}(x)) = \dfrac{\dfrac{x}{2-x} + 1}{\dfrac{x}{2-x} + 2}$

$\mathrm{g}(\mathrm{f}(x)) = \dfrac{\dfrac{x + 2 - x}{2-x}}{\dfrac{x + 4 - 2x}{2-x}} = \dfrac{2}{4-x}$

Now, find $\mathrm{g}(\mathrm{g}(\mathrm{f}(x)))$:

$\mathrm{g}(\mathrm{g}(\mathrm{f}(x))) = \mathrm{g}\left(\dfrac{2}{4-x}\right)$

$\mathrm{g}(\mathrm{g}(\mathrm{f}(x))) = \dfrac{\dfrac{2}{4-x} + 1}{\dfrac{2}{4-x} + 2}$

$\mathrm{g}(\mathrm{g}(\mathrm{f}(x))) = \dfrac{\dfrac{2 + 4 - x}{4-x}}{\dfrac{2 + 8 - 2x}{4-x}} = \dfrac{6-x}{10-2x}$

Answer: $\dfrac{6-x}{10-2 x}$

</details>

---

### Q18. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the function $\mathrm{f}(x)=x^3+\mathrm{e}^{\dfrac{x}{2}}$ and $\mathrm{g}(x)=\mathrm{f}^{-1}(x)$, then the value of $g^{\prime}(1)$ is

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** 2
- **(D)** $\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

Given $\mathrm{f}(x) = x^3 + \mathrm{e}^{\dfrac{x}{2}}$ and $\mathrm{g}(x) = \mathrm{f}^{-1}(x)$.

We know that $\mathrm{g}^{\prime}(x) = \dfrac{1}{\mathrm{f}^{\prime}(\mathrm{g}(x))}$.

To find $\mathrm{g}(1)$, we set $\mathrm{f}(x) = 1$:

$x^3 + \mathrm{e}^{\dfrac{x}{2}} = 1$

By observation, $x = 0$ satisfies this equation, so $\mathrm{g}(1) = 0$.

Now, differentiating $\mathrm{f}(x)$ with respect to $x$:

$\mathrm{f}^{\prime}(x) = 3x^2 + \dfrac{1}{2}\mathrm{e}^{\dfrac{x}{2}}$

Substituting $x = 0$:

$\mathrm{f}^{\prime}(0) = 3(0)^2 + \dfrac{1}{2}\mathrm{e}^{0} = \dfrac{1}{2}$

Therefore, $\mathrm{g}^{\prime}(1) = \dfrac{1}{\mathrm{f}^{\prime}(\mathrm{g}(1))} = \dfrac{1}{\mathrm{f}^{\prime}(0)} = \dfrac{1}{\dfrac{1}{2}} = 2$.

Answer: 2

</details>

---

### Q19. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{g}(x)=x^2+x-1$ and (gof) $(x)=4 x^2-10 x+5$, then $\mathrm{f}(2)$ is equal to

**Options:**

- **(A)** 0
- **(B)** -1
- **(C)** 2
- **(D)** -2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -2**

**Detailed Solution:**

Given $g(x) = x^2 + x - 1$ and $g(f(x)) = 4x^2 - 10x + 5$.

Substituting $x = 2$ in the equation for $g(f(x))$:

$g(f(2)) = 4(2)^2 - 10(2) + 5 = 1$

Let $f(2) = y$. Then $g(y) = 1$.

$y^2 + y - 1 = 1$

$y^2 + y - 2 = 0$

$(y + 2)(y - 1) = 0$

$y = -2$ or $y = 1$

Since $1$ is not among the options, $f(2) = -2$.

Answer: -2

</details>

---

### Q20. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}(x)=x^2+1$ and $\mathrm{g}(x)=\frac{1}{x}$, then the value of $\mathrm{f}(\mathrm{g}(\mathrm{g}(\mathrm{f}(x))))$ at $x=1$ is

**Options:**

- **(A)** $4$
- **(B)** $1$
- **(C)** $5$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5$**

**Detailed Solution:**

$$
\begin{aligned}
\mathrm{f}(x)=x^2+1, & \mathrm{~g}(x)=\frac{1}{x} \\
\therefore \quad \mathrm{f}(\mathrm{g}(\mathrm{g}(\mathrm{f}(x)))) & =\mathrm{f}\left(\mathrm{g}\left(\mathrm{g}\left(x^2+1\right)\right)\right) \\
& =\mathrm{f}\left(\mathrm{g}\left(\frac{1}{x^2+1}\right)\right) \\
& =\mathrm{f}\left(x^2+1\right) \\
& =\left(x^2+1\right)^2+1
\end{aligned}
$$
$\therefore \quad$ At $x=1$, we get the value of above function
$$
\begin{aligned}
& =\left[(1)^2+1\right]^2+1 \\
& =5
\end{aligned}
$$

</details>

---

### Q21. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{g}(x)=1+\sqrt{x}$ and $\mathrm{f}(\mathrm{g}(x))=3+2 \sqrt{x}+x$, then $\mathrm{f}(\mathrm{f}(x))$ is

**Options:**

- **(A)** $x^2+4 x+6$
- **(B)** $x^4+x^2+6$
- **(C)** $x^2+x+6$
- **(D)** $x^4+4 x^2+6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x^4+4 x^2+6$**

**Detailed Solution:**

$\begin{aligned} & g(x)=1+\sqrt{x} \text { and } \mathrm{f}(\mathrm{g}(x))=3+2 \sqrt{x}+x \\ & \therefore \quad \mathrm{f}(\mathrm{g}(x))=\left[(\sqrt{x})^2+2 \sqrt{x}+1\right]+2 \\ & =(\sqrt{x}+1)^2+2 \\ & =[\mathrm{g}(x)]^2+2 \\ & \Rightarrow \mathrm{f}(x)=x^2+2 \\ & \Rightarrow \mathrm{f}(\mathrm{f}(x))=\left(x^2+2\right)^2+2=x^4+4 x^2+6 \\ & \end{aligned}$

</details>

---

### Q22. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(x)=\frac{3 x+4}{5 x-7}$ and $\mathrm{g}(x)=\frac{7 x+4}{5 x-3}$, then $\mathrm{f}(\mathrm{g}(x))=$

**Options:**

- **(A)** $\frac{x^3+1}{x^2+2}$
- **(B)** $41 x$
- **(C)** $g(f(x))$
- **(D)** $\frac{5 x-7}{41}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $g(f(x))$**

**Detailed Solution:**

$\begin{aligned} f(g(x)) & =f\left(\frac{7 x+4}{5 x-3}\right) \\ & =\frac{3\left(\frac{7 x+4}{5 x-3}\right)+4}{5\left(\frac{7 x+4}{5 x-3}\right)-7} \\ & =\frac{21 x+12+20 x-12}{35 x+20-35 x+21} \\ & =\frac{41 x}{41} \\ & =x\end{aligned}$
$\begin{aligned} & \text { Now, } \mathrm{g}(\mathrm{f}(x))=\mathrm{g}\left(\frac{3 x+4}{5 x-7}\right) \\ &=\frac{7\left(\frac{3 x+4}{5 x-7}\right)+4}{5\left(\frac{3 x+4}{5 x-7}\right)-3} \\ &=\frac{21 x+28+20 x-28}{15 x+20-15 x+21} \\ &=\frac{41 x}{41} \\ &=x \\ & \mathrm{f}(\mathrm{g}(x))=\mathrm{g}(\mathrm{f}(x))\end{aligned}$

</details>

---

### Q23. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{f}(x)=\log (\sin x), 0 < x < \pi$ and $\mathrm{g}(x)=\sin ^{-1}\left(\mathrm{e}^{-x}\right), x \geq 0$.

If $\alpha$ is a positive real number such that $a=(f \circ g)^{\prime}(\alpha)$ and $b=(f \circ g)(\alpha)$, then

**Options:**

- **(A)** $a \alpha^2-b \alpha-a=0$
- **(B)** $a \alpha^2-b \alpha-a=1$
- **(C)** $\mathrm{a} \alpha^2+\mathrm{b} \alpha-\mathrm{a}=-2 \alpha^2$
- **(D)** $a \alpha^2+b \alpha+a=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $a \alpha^2-b \alpha-a=1$**

**Detailed Solution:**

$\begin{array}{ll} & \mathrm{f}(x)=\log (\sin x), 0 < x < \pi \text { and } \\ & \mathrm{g}(x)=\sin ^{-1}\left(\mathrm{e}^{-x}\right), x \geq 0 \\ \therefore \quad & \left(\text { fog) }(x)=\log \left[\sin \left(\sin ^{-1} \mathrm{e}^{-x}\right)\right]=\log \left(\mathrm{e}^{-x}\right)=-x\right. \\ \therefore \quad & (\text { fog })^{\prime}(x)=-1 \\ \therefore \quad & \mathrm{a}=(\text { fog })^{\prime}(\alpha)=-1 \text { and } \mathrm{b}=(\mathrm{fog})(\alpha)=-\alpha \\ & \text { These values satisfy only option (B). } \\ \therefore \quad & \text { Option (B) is correct. }\end{array}$

</details>

---

### Q24. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{f}$ be a differentiable function such that $\mathrm{f}(1)=2$ and $\mathrm{f}^{\prime}(x)=\mathrm{f}(x)$, for all $x \in \mathrm{R}$. If $\mathrm{h}(x)=\mathrm{f}(\mathrm{f}(x))$, then $\mathrm{h}^{\prime}(1)$ is equal to

**Options:**

- **(A)** $4 \mathrm{e}^2$
- **(B)** $4 e$
- **(C)** $2 \mathrm{e}$
- **(D)** $2 \mathrm{e}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4 e$**

**Detailed Solution:**

Given: $\mathrm{f}^{\prime}(x)=\mathrm{f}(x)$ for all $x \in \mathrm{R}^{\prime}$
$\Rightarrow \frac{\mathrm{f}^{\prime}(x)}{\mathrm{f}(x)}=1$
Integrating on both sides, wwe get $\log |\mathrm{f}(x)|=x+\mathrm{c}$
$\Rightarrow \mathrm{f}(x)=\mathrm{e}^{x+c}$
$\Rightarrow \mathrm{f}(x)=\mathrm{e}^x \cdot \mathrm{e}^{\mathrm{c}}$
$\Rightarrow \mathrm{f}(x)=\mathrm{e}^x \cdot \mathrm{c}_1$... (i)$\left[\mathrm{e}^{\mathrm{c}}=\mathrm{c}_1\right]$
As $f(1)=2$
$\begin{aligned}
& \therefore \quad \mathrm{c}_1 \cdot \mathrm{e}=2 \\
& \Rightarrow \mathrm{c}_1=\frac{2}{\mathrm{e}}
\end{aligned}$
Equation (i) becomes
$\mathrm{f}(x)=\mathrm{e}^x \cdot \frac{2}{\mathrm{e}}$
Now, $\mathrm{h}(x)=\mathrm{f}(\mathrm{f}(x))$
$\begin{array}{ll}
\therefore \quad \mathrm{h}^{\prime}(x)=\mathrm{f}^{\prime}(\mathrm{f}(x)) \times \mathrm{f}^{\prime}(x) \\
\therefore \quad \mathrm{h}^{\prime}(1)=\mathrm{f}^{\prime}(\mathrm{f}(1)) \times \mathrm{f}^{\prime}(1) \\
\Rightarrow \mathrm{h}^{\prime}(1)=\mathrm{f}^{\prime}(2) \times \mathrm{f}^{\prime}(1) \\
\Rightarrow \mathrm{h}^{\prime}(1)=\mathrm{e}^2 \times \frac{2}{\mathrm{e}} \times 2 \\
\Rightarrow \mathrm{h}^{\prime}(1)=4 \mathrm{e}
\end{array}$

</details>

---

### Q25. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{f}(x)=\mathrm{e}^x-x$ and $\mathrm{g}(x)=x^2-x, \forall x \in \mathrm{R}$, then the set of all $x \in \mathrm{R}$, where the function $\mathrm{h}(x)=(\mathrm{fog})(x)$ is increasing is

**Options:**

- **(A)** $\left[0, \frac{1}{2}\right] \cup[1, \infty)$
- **(B)** $\left[-1,-\frac{1}{2}\right] \cup\left[\frac{1}{2}, \infty\right)$
- **(C)** $[0, \infty)$
- **(D)** $\left[-\frac{1}{2}, 0\right] \cup[1, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[0, \frac{1}{2}\right] \cup[1, \infty)$**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{h}(x)=(\mathrm{fog})(x) \\
& \Rightarrow \mathrm{h}(x)=\mathrm{f}\left(x^2-x\right) \\
& \Rightarrow \mathrm{h}(x)=\mathrm{e}^{x^2-x}-x^2+x \\
& \therefore \quad \mathrm{h}^{\prime}(x)=\mathrm{e}^{x^2-x}(2 x-1)-2 x+1 \\
& \Rightarrow \mathrm{h}^{\prime}(x)=\left(\mathrm{e}^{x^2-x}-1\right)(2 x-1)
\end{aligned}$
For function $\mathrm{h}(x)$ to be increasing,
$\begin{aligned}
& \mathrm{h}^{\prime}(x) \geq 0 \\
& \Rightarrow\left(\mathrm{e}^{x^2-x}-1\right)(2 x-1) \geq 0 \\
& \Rightarrow x \in\left[0, \frac{1}{2}\right] \cup[1, \infty)
\end{aligned}$
\begin{array}{c|c|c|c}
\mathrm{h}^{\prime}- & + & - & + \\
\hline & & & \\
0 & \frac{1}{2} & 1
\end{array}

</details>

---

### Q26. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$f: R \rightarrow R ; g: R \rightarrow R$ are two functions such that $\mathrm{f}(x)=2 x-3, \mathrm{~g}(x)=x^3+5$, then $(f \circ g)^{-1}(-9)$ is

**Options:**

- **(A)** $-2$
- **(B)** $2$
- **(C)** $-\sqrt{2}$
- **(D)** $\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-2$**

**Detailed Solution:**

We have, $\mathrm{f}(x)=2 x-3, \mathrm{~g}(x)=x^3+5$
$\begin{aligned}
\operatorname{fog}(x) & =\mathrm{f}(\mathrm{g}(x)) \\
& =2 \mathrm{~g}(x)-3 \\
& =2\left(x^3+5\right)-3=2 x^3+7
\end{aligned}$
Let $(f \circ g)(x)=y=2 x^3+7$
$\begin{aligned}
& y=2 x^3+7 \\
& \Rightarrow y-7=2 x^3 \\
& \Rightarrow x^3=\frac{y-7}{2} \\
& \Rightarrow x=\left(\frac{y-7}{2}\right)^{\frac{1}{3}} \\
\therefore \quad & (\text { fog })^{-1}(y)=\left(\frac{y-7}{2}\right)^{\frac{1}{3}} \\
\therefore \quad & (\text { fog })^{-1}(-9)=\left(\frac{-9-7}{2}\right)^{\frac{1}{3}}=(-8)^{\frac{1}{3}}=-2
\end{aligned}$

</details>

---

### Q27. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\mathrm{e}^x, \mathrm{~g}(x)=\sin ^{-1} x$ and $\mathrm{h}(x)=\mathrm{f}(\mathrm{g}(x))$, then $\frac{\mathrm{h}^{\prime}(x)}{\mathrm{h}(x)}$ is

**Options:**

- **(A)** $\mathrm{e}^{\sin ^{-1} x}$
- **(B)** $\frac{1}{\sqrt{1-x^2}}$
- **(C)** $\sin ^{-1} x$
- **(D)** $\frac{\mathrm{e}^{\sin ^{-1} x}}{\sqrt{1-x^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{\sqrt{1-x^2}}$**

**Detailed Solution:**

$\begin{aligned}
\mathrm{h}(x) & =\mathrm{f}(\mathrm{g}(x)) \\
& =\mathrm{f}\left(\sin ^{-1} x\right) \\
\therefore \quad \mathrm{h}(x) & =\mathrm{e}^{\sin ^{-1} x}
\end{aligned}$
Differentiating w.r.t. $x$, we get
$\begin{aligned}
& \begin{aligned}
\mathrm{h}^{\prime}(x) & =\mathrm{e}^{\sin ^{-1} x} \cdot \frac{\mathrm{d}}{\mathrm{d} x}\left(\sin ^{-1} x\right) \\
& =\mathrm{e}^{\sin ^{-1} x} \cdot \frac{1}{\sqrt{1-x^2}}
\end{aligned} \\
& \text { Now, } \frac{\mathrm{h}^{\prime}(x)}{\mathrm{h}(x)}=\frac{\mathrm{e}^{\sin ^{-1} x} \cdot \frac{1}{\sqrt{1-x^2}}}{\mathrm{e}^{\sin ^{-1} x}}=\frac{1}{\sqrt{1-x^2}}
\end{aligned}$

</details>

---

### Q28. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\mathrm{f}: \mathbb{R}-\left(-\frac{3}{5}\right) \rightarrow \mathbb{R}$ is defined by $f(x)=\frac{3 x-2}{5 x+3}$, then $f \circ f(1)$ is

**Options:**

- **(A)** $1$
- **(B)** $\frac {-13}{29}$
- **(C)** $\frac {13}{29}$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac {-13}{29}$**

**Detailed Solution:**

$\begin{aligned} & f(x)=\frac{3 x-2}{5 x+3} \\ & \begin{aligned} f(f(x)) & =\frac{3\left(\frac{3 x-2}{5 x+3}\right)-2}{5\left(\frac{3 x-2}{5 x+3}\right)+3} \\ & =\frac{3(3 x-2)-2(5 x+3)}{5(3 x-2)+3(5 x+3)} \\ & =\frac{9 x-6-10 x-6}{15 x-10+15 x+9} \\ & =\frac{-x-12}{30 x-1}\end{aligned} \\ & \text { fof }(1)=\frac{-1-12}{30-1}=\frac{-13}{29}\end{aligned}$

</details>

---

### Q29. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

For a suitable chosen real constant a, let the function $f: R-\{-a\} \rightarrow R$ be defined by $f(x)=\frac{a-x}{a+x}$. Further, suppose that for any real number $x \neq-a$ and $f(x) \neq-a,(f o f)(x)=x$. Then, $f\left(-\frac{1}{2}\right)$ is equal to

**Options:**

- **(A)** -3
- **(B)** $\frac{1}{3}$
- **(C)** $-\frac{1}{3}$
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

$\begin{aligned} & \text { fof }(x)=f(f(x))=f\left(\frac{a-x}{a+x}\right)=x \\ & \Rightarrow \frac{a-\frac{a-x}{a+x}}{a+\frac{a-x}{a+x}}=x \\ & \Rightarrow \frac{a^2+a x-a+x}{a^2+a x+a-x}=x \\ & \Rightarrow a^2+a x-a+x=a^2 x+a x^2+a x-x^2 \\ & \Rightarrow(a-1) x^2+\left(a^2-1\right) x-a(a-1)=0 \\ & \Rightarrow(a-1)(x+a)(x-1)=0 \\ & \Rightarrow a=1[\operatorname{as} x \neq-a] \\ & \Rightarrow f(x)=\frac{1-x}{1+x} \\ & \Rightarrow f\left(-\frac{1}{2}\right)=\frac{1+\frac{1}{2}}{1-\frac{1}{2}}=3\end{aligned}$

</details>

---

### Q30. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=e^{|x|}, g(x)=\log x$, then $(g$ of $)(x)=$

**Options:**

- **(A)** $|x|$
- **(B)** $1$
- **(C)** $2 x$
- **(D)** $-x^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $|x|$**

**Detailed Solution:**

$\begin{aligned} & f(x)=e^{|x|}, g(x)=\log x \\ & g \text { of }(x)=g(f(x))=\log e^{|x|}=|x|\end{aligned}$

</details>

---

### Q31. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For a suitable chosen real constant $a$, let a function $f: R-[-a] \rightarrow R$ be defined by $f(x)=\frac{a-x}{a+x}$. Further, suppose that for any real number $x \neq-a$ and $f(x) \neq-a,(f o f)(x)=x$. Then $f\left(\frac{-1}{2}\right)$ is equal to

**Options:**

- **(A)** $\frac{-1}{3}$
- **(B)** 3
- **(C)** $\frac{1}{3}$
- **(D)** $-3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3**

**Detailed Solution:**

$\begin{aligned} & (f \circ f)(x)=\frac{a-\frac{a-x}{a+x}}{a+\frac{a-x}{a+x}}=x \\ & \Rightarrow \frac{a^2+a x-a+x}{a^2+a x+a-x}=x \\ & \Rightarrow(a+1) x+\left(a^2-a\right)=\left(a^2+a\right) x+(a-1) x^2 \\ & \Rightarrow a+1=a^2+a, a^2-a=0, a-1=0 \\ & \Rightarrow a=1 \\ & \Rightarrow f(x)=\frac{1-x}{1+x} \\ & \Rightarrow f\left(-\frac{1}{2}\right)=\frac{1+\frac{1}{2}}{1-\frac{1}{2}}=3\end{aligned}$

</details>

---

### Q32. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\frac{x}{2 x+1}$ and $g(x)=\frac{x}{x+1}$, then $(f \circ g)(x)=$

**Options:**

- **(A)** $\frac{2 x-1}{x+1}$
- **(B)** $\frac{x}{3 x+1}$
- **(C)** $\frac{x+1}{x+2}$
- **(D)** $\frac{x-1}{2 x+1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{x}{3 x+1}$**

**Detailed Solution:**

$$
\begin{aligned}
& (f \circ g)(x)=f\left[\frac{x}{x+1}\right] \\
& =\frac{\left(\frac{x}{x+1}\right)}{2\left(\frac{x}{x+1}\right)+1}=\frac{x}{x+1} \times \frac{x+1}{2 x+x+1}=\frac{x}{3 x+1}
\end{aligned}
$$
$\begin{aligned} & (f \circ g)(x)=f\left[\frac{x}{x+1}\right] \\ & =\frac{\left(\frac{x}{x+1}\right)}{2\left(\frac{x}{x+1}\right)+1}=\frac{x}{x+1} \times \frac{x+1}{2 x+x+1}=\frac{x}{3 x+1}\end{aligned}$

</details>

---

### Q33. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=2 x^{2}+b x+c, f(0)=3$ and $f(2)=1$, then $(f o f)(1)=$

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** 1
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

$\begin{aligned} \text { Here } \mathrm{f}(\mathrm{x}) &=2 \mathrm{x}^{2}+\mathrm{bx}+\mathrm{c} \\ \mathrm{f}(0) &=0+0+\mathrm{c} \quad \Rightarrow 3=\mathrm{c} \\ \mathrm{f}(2) &=8+2 \mathrm{~b}+3 \end{aligned}$
$\begin{array}{ll}\therefore \quad \mathrm{f}=8 & +2 \mathrm{~b}+3 \Rightarrow 2 \mathrm{~b}=-10 \Rightarrow \mathrm{b}=-5 \\ \therefore \quad \mathrm{f}(\mathrm{x})= & 2 \mathrm{x}^{2}-5 \mathrm{x}+3 \\ & \mathrm{f}(1)=2-5+3=0 \\ & (\mathrm{f} 0 \mathrm{f})(\mathrm{x})=\mathrm{f}[\mathrm{f}(\mathrm{x})] \\ & (\mathrm{f} 0 \mathrm{f})(1)=\mathrm{f}[\mathrm{f}(1)] \\ & =\mathrm{f}(0)=0-0+3=3\end{array}$

</details>

---

### Q34. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\frac{3 x+4}{5 x-7}, x \neq \frac{7}{5}$
$g(x)=\frac{7 x+4}{5 x-3}, x \neq \frac{3}{5}$ then
$(g \circ f)(3)=$

**Options:**

- **(A)** $-3$
- **(B)** $-\frac{1}{3}$
- **(C)** 3
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

$\begin{aligned} \therefore(g \circ f)(x) &=g[f(x)] \\ &=g\left[\frac{3 x+4}{5 x-7}\right] \\ &=\frac{7\left(\frac{3 x+4}{5 x-7}\right)+4}{5\left(\frac{3 x+4}{5 x-7}\right)-3}=\frac{7(3 x+4)+4(5 x-7)}{5(3 x+4)-3(5 x-7)}=\frac{41 x}{41}=x \\ \therefore(g \circ f)(3) &=3 \end{aligned}$

</details>

---

### Q35. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}: \mathrm{R} \rightarrow \mathrm{R}, g: \mathrm{R} \rightarrow \mathrm{R}$ defined by $f(x)=x^{2}-3 x+4$ and $g(x)=2 x+1$, then the
value of $x$ for which $f(x)=f \circ g)(x)$ is

**Options:**

- **(A)** $1, \frac{-2}{3}$
- **(B)** $-1, \frac{2}{3}$
- **(C)** $1, \frac{2}{3}$
- **(D)** $-1, \frac{-2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-1, \frac{2}{3}$**

**Detailed Solution:**

$($ fog $)(x)=f[g(x)]=f(2 x+1)=(2 x+1)^{2}-3(2 x+1)+4$
$\quad=4 x^{2}+4 x+1-6 x-3+4=4 x^{2}-2 x+2$
Given $f(x)=(f \circ g)(x)$
$\therefore x^{2}-3 x+4=4 x^{2}-2 x+2$
$3 x^{2}+x-2=0 \Rightarrow 3 x^{2}+3 x-2 x-2=0$
$3 x(x+1)-2(x+1)=0 \Rightarrow(x+1)(3 x-2)=0$
$\therefore x=-1, \frac{2}{3}$

</details>

---

### Q36. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\frac{4 x+7}{7 x-4}$, then the value of $f\{f[f(2)]\}=$

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** $\frac{2}{3}$
- **(C)** $\frac{35}{39}$
- **(D)** $\frac{39}{35}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{2}$**

**Detailed Solution:**

$f(x)=\frac{4 x+7}{7 x-4}$
$f(2)=\frac{8+7}{14-4}=\frac{15}{10}=\frac{3}{2}$
$f[f(2)]=f\left(\frac{3}{2}\right)=\frac{\left(4 \times \frac{3}{2}\right)+7}{\left(7 \times \frac{3}{2}\right)-4}=\frac{6+7}{\left(\frac{21-8}{2}\right)}=\frac{13 \times 2}{13}=2$
$f\{f[f(2)]\}=f(2)=\frac{3}{2}$
This problem can also be solved as follows :
$\begin{aligned}
\mathrm{f}(\mathrm{x}) \quad=\frac{4 \mathrm{x}+7}{7 \mathrm{x}-4} & \Rightarrow \mathrm{f}[\mathrm{f}(\mathrm{x})]=\mathrm{f}\left[\frac{4 \mathrm{x}+7}{7 \mathrm{x}-4}\right] \\
\therefore \mathrm{f}\left[\frac{4 \mathrm{x}+7}{7 \mathrm{x}-4}\right] \quad &=\frac{4\left(\frac{4 \mathrm{x}+7}{7 \mathrm{x}-4}\right)+7}{7\left(\frac{4 \mathrm{x}+7}{7 \mathrm{x}-4}\right)-4} \\
&=\frac{16 \mathrm{x}+28+49 \mathrm{x}-28}{28 \mathrm{x}+49-28 \mathrm{x}+16}=\frac{65 \mathrm{x}}{65}=\mathrm{x} \\
\therefore \quad \mathrm{f}\{\mathrm{f}[\mathrm{f}(\mathrm{x})]\} &=\mathrm{f}\{\mathrm{x}\}=\frac{4 \mathrm{x}+7}{7 \mathrm{x}-4} \\
\therefore \quad \mathrm{f}\{\mathrm{f}[\mathrm{f}(2)]\} &=\frac{4(2)+7}{7(2)-4}=\frac{15}{10}=\frac{3}{2}
\end{aligned}$

</details>

---

### Q37. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn></math> and <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>,</mo></math> then <math><mi>f</mi><mi>o</mi><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn></math>
- **(B)** <math><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn></math>
- **(C)** <math><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn></math>
- **(D)** <math><mn>2</mn><mo>-</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

Given: <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
<math><mi mathvariant="normal">N</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">w</mi><mo>,</mo><mo> </mo><mi>f</mi><mi>o</mi><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>  
<math><mo>=</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn></math>

</details>

---

### Q38. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>6</mn><mo>,</mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>4</mn><mi>x</mi><mo>+</mo><mi>k</mi></math> and <math><mi>f</mi><mi>o</mi><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>g</mi><mi>o</mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> then k =

**Options:**

- **(A)** -9
- **(B)** 18
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac></math>
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 9**

**Detailed Solution:**

We have, 
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>6</mn><mo>,</mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>4</mn><mi>x</mi><mo>+</mo><mi>k</mi></math>  
Since, <math><mi>f</mi><mi>o</mi><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>g</mi><mi>o</mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>g</mi></mrow></mfenced><mi>x</mi><mo>=</mo><mi>g</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mi>g</mi><mfenced separators="|"><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mn>3</mn><mfenced separators="|"><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mo>+</mo><mn>6</mn><mo>=</mo><mn>4</mn><mfenced separators="|"><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mi>K</mi></math>  
<math><mo>&#8658;</mo><mn>3</mn><mi>k</mi><mo>-</mo><mi>k</mi><mo>=</mo><mn>24</mn><mo>-</mo><mn>6</mn></math>  
<math><mo>&#8658;</mo><mn>2</mn><mi>k</mi><mo>=</mo><mn>18</mn></math>  
<math><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>9</mn></math>

</details>

---

### Q39. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x)=\frac{a x+b}{c x+d}$. Then, $f o f(x)=x$ provided
that

**Options:**

- **(A)** $d=-a$
- **(B)** $d=a$
- **(C)** $a=b=c=d=1$
- **(D)** $a=b=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $d=-a$**

**Detailed Solution:**

Given,
and $\quad f o f(x)=x$
$$
\Rightarrow \quad f\left(\frac{a x+b}{c x+d}\right)=x
$$
$$
\begin{array}{l}
\Rightarrow \quad \frac{a\left(\frac{a x+b}{c x+d}\right)+b}{c\left(\frac{a x+b}{c x+d}\right)+d}=x \\
\Rightarrow \quad \frac{x\left(a^{2}+b c\right)+a b+b d}{x(a c+c d)+b c+d^{2}}=x \\
\Rightarrow \quad d=-a
\end{array}
$$

</details>

---

