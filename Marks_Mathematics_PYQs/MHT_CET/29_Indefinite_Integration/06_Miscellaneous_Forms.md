# MHT CET Mathematics - Indefinite Integration

## Topic 6: Miscellaneous Forms

**Total Questions:** 30

---

### Q1. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \cos ^{\frac{-3}{7}} x \cdot \sin ^{\frac{-11}{7}} x d x=$

**Options:**

- **(A)** $\frac{-4}{7} \tan ^{\frac{-4}{7}} x+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\frac{4}{7} \tan ^{\frac{4}{7}} x+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\frac{-7}{4} \tan ^{\frac{-4}{7}} x+\mathrm{c}$, where c is a constant of integration.
- **(D)** $\frac{7}{4} \tan ^{\frac{4}{7}} x+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-7}{4} \tan ^{\frac{-4}{7}} x+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int \cos^{\dfrac{-3}{7}} x \cdot \sin^{\dfrac{-11}{7}} x \, dx$

$I = \int \dfrac{1}{\cos^{\dfrac{3}{7}} x \cdot \sin^{\dfrac{11}{7}} x} \, dx$

Dividing the numerator and the denominator by $\cos^2 x$, we get:

$I = \int \dfrac{\sec^2 x}{\dfrac{\cos^{\dfrac{3}{7}} x \cdot \sin^{\dfrac{11}{7}} x}{\cos^2 x}} \, dx$

$I = \int \dfrac{\sec^2 x}{\dfrac{\sin^{\dfrac{11}{7}} x}{\cos^{\dfrac{11}{7}} x}} \, dx$

$I = \int \dfrac{\sec^2 x}{\tan^{\dfrac{11}{7}} x} \, dx$

Let $\tan x = t$, then $\sec^2 x \, dx = dt$.

$I = \int t^{\dfrac{-11}{7}} \, dt$

$I = \dfrac{t^{\dfrac{-11}{7} + 1}}{\dfrac{-11}{7} + 1} + c$

$I = \dfrac{t^{\dfrac{-4}{7}}}{\dfrac{-4}{7}} + c$

$I = \dfrac{-7}{4} \tan^{\dfrac{-4}{7}} x + c$

Answer: $\frac{-7}{4} \tan ^{\frac{-4}{7}} x+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q2. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The integral $\int \frac{2 x^3-1}{x^4+x} \mathrm{~d} x$ is equal to

**Options:**

- **(A)** $\log \frac{\left|x^3+1\right|}{x^2}+\mathrm{c}$, (where c is a constant of integration)
- **(B)** $\frac{1}{2} \log \frac{\left(x^3+1\right)^2}{\left|x^3\right|}+\mathrm{c}$; (where c is a constant of integration)
- **(C)** $\log \left|\frac{x^3+1}{x}\right|+\mathrm{c}$, (where c is a constant of integration)
- **(D)** $\frac{1}{2} \log \frac{\left|x^3+1\right|}{x^2}+\mathrm{c}$, (where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log \left|\frac{x^3+1}{x}\right|+\mathrm{c}$, (where c is a constant of integration)**

**Detailed Solution:**

Let $I = \int \dfrac{2x^3 - 1}{x^4 + x} \, dx$

We can rewrite the numerator as $3x^3 - x^3 - 1$ and factor the denominator as $x(x^3 + 1)$.

$I = \int \dfrac{3x^3 - (x^3 + 1)}{x(x^3 + 1)} \, dx$

Separating the terms, we get:

$I = \int \left( \dfrac{3x^3}{x(x^3 + 1)} - \dfrac{x^3 + 1}{x(x^3 + 1)} \right) \, dx$

$I = \int \left( \dfrac{3x^2}{x^3 + 1} - \dfrac{1}{x} \right) \, dx$

Integrating each term with respect to $x$:

$I = \log|x^3 + 1| - \log|x| + c$

Using the property of logarithms $\log a - \log b = \log \left(\dfrac{a}{b}\right)$:

$I = \log \left| \dfrac{x^3 + 1}{x} \right| + c$

Answer: $\log \left|\frac{x^3+1}{x}\right|+\mathrm{c}$, (where c is a constant of integration)

</details>

---

### Q3. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \frac{\mathrm{d} x}{\cos ^3 x \sqrt{2 \sin 2 x}}=(\tan x)^A+C(\tan x)^B+\mathrm{k}$ where $k$ is a constant of integration, then $\mathrm{A}+\mathrm{B}+\mathrm{C}$ equals

**Options:**

- **(A)** $\frac{27}{10}$
- **(B)** $\frac{16}{5}$
- **(C)** $\frac{27}{5}$
- **(D)** $\frac{21}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{16}{5}$**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{\cos ^3 x \sqrt{2 \sin 2 x}}$.

Using the identity $\sin 2x = 2 \sin x \cos x$, we get:

$\sqrt{2 \sin 2 x} = \sqrt{4 \sin x \cos x} = 2 \sqrt{\sin x \cos x}$

Substituting this into the integral:

$I = \int \dfrac{\mathrm{d} x}{\cos ^3 x \cdot 2 \sqrt{\sin x \cos x}}$

Multiplying and dividing the term inside the square root by $\cos x$:

$\sqrt{\sin x \cos x} = \sqrt{\dfrac{\sin x}{\cos x} \cdot \cos^2 x} = \cos x \sqrt{\tan x}$

Therefore, the integral becomes:

$I = \dfrac{1}{2} \int \dfrac{\mathrm{d} x}{\cos^4 x \sqrt{\tan x}} = \dfrac{1}{2} \int \dfrac{\sec^4 x}{\sqrt{\tan x}} \mathrm{d} x$

We can write $\sec^4 x = \sec^2 x \cdot \sec^2 x = (1 + \tan^2 x) \sec^2 x$.

$I = \dfrac{1}{2} \int \dfrac{1 + \tan^2 x}{\sqrt{\tan x}} \sec^2 x \mathrm{d} x$

Let $\tan x = t$, then $\sec^2 x \mathrm{d} x = \mathrm{d} t$.

$I = \dfrac{1}{2} \int \dfrac{1 + t^2}{\sqrt{t}} \mathrm{d} t$

$I = \dfrac{1}{2} \int \left( t^{-1/2} + t^{3/2} \right) \mathrm{d} t$

Integrating term by term:

$I = \dfrac{1}{2} \left( \dfrac{t^{1/2}}{1/2} + \dfrac{t^{5/2}}{5/2} \right) + \mathrm{k}$

$I = t^{1/2} + \dfrac{1}{5} t^{5/2} + \mathrm{k}$

Substituting back $t = \tan x$:

$I = (\tan x)^{1/2} + \dfrac{1}{5} (\tan x)^{5/2} + \mathrm{k}$

Comparing this with the given expression $(\tan x)^A + C(\tan x)^B + \mathrm{k}$, we get:

$A = \dfrac{1}{2}$, $B = \dfrac{5}{2}$, $C = \dfrac{1}{5}$

Now, finding the sum $A + B + C$:

$A + B + C = \dfrac{1}{2} + \dfrac{5}{2} + \dfrac{1}{5} = \dfrac{6}{2} + \dfrac{1}{5} = 3 + \dfrac{1}{5} = \dfrac{16}{5}$

Answer: $\frac{16}{5}$

</details>

---

### Q4. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\frac{x}{x+1}, x \neq-1$ and (fof) $(x)=\mathrm{F}(x)$, then $\int \mathrm{F}(x) \mathrm{d} x$ is

**Options:**

- **(A)** $\frac{x}{2}+\frac{1}{2} \log (2 x+1)+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\frac{x}{2}-\frac{1}{4} \log (2 x+1)+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\frac{x}{2}-\frac{1}{2} \log (2 x+1)+\mathrm{c}$, where c is a constant of integration.
- **(D)** $\frac{x}{2}+\frac{1}{4} \log (2 x+1)+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{x}{2}-\frac{1}{4} \log (2 x+1)+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Given $\mathrm{f}(x) = \dfrac{x}{x+1}$

$\mathrm{F}(x) = (\mathrm{fof})(x) = \mathrm{f}(\mathrm{f}(x))$

$\mathrm{F}(x) = \dfrac{\dfrac{x}{x+1}}{\dfrac{x}{x+1} + 1}$

$\mathrm{F}(x) = \dfrac{x}{x + (x+1)} = \dfrac{x}{2x+1}$

Now, integrating $\mathrm{F}(x)$ with respect to $x$:

$\int \mathrm{F}(x) \mathrm{d} x = \int \dfrac{x}{2x+1} \mathrm{d} x$

Multiply and divide by $2$:

$\int \mathrm{F}(x) \mathrm{d} x = \dfrac{1}{2} \int \dfrac{2x}{2x+1} \mathrm{d} x$

$\int \mathrm{F}(x) \mathrm{d} x = \dfrac{1}{2} \int \dfrac{2x+1-1}{2x+1} \mathrm{d} x$

$\int \mathrm{F}(x) \mathrm{d} x = \dfrac{1}{2} \int \left(1 - \dfrac{1}{2x+1}\right) \mathrm{d} x$

$\int \mathrm{F}(x) \mathrm{d} x = \dfrac{1}{2} \left(x - \dfrac{1}{2} \log (2x+1)\right) + \mathrm{c}$

$\int \mathrm{F}(x) \mathrm{d} x = \dfrac{x}{2} - \dfrac{1}{4} \log (2x+1) + \mathrm{c}$

Answer: $\frac{x}{2}-\frac{1}{4} \log (2 x+1)+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q5. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\quad \int \operatorname{cosec}(x-a) \cdot \operatorname{cosec} x d x=$

**Options:**

- **(A)** $\frac{-1}{\sin \mathrm{a}} \log (\sin (x-\mathrm{a}) \sin x)+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\frac{1}{\sin \mathrm{a}} \log (\sin (x-\mathrm{a}) \sin x)+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\frac{1}{\sin \mathrm{a}} \log (\sin (x-\mathrm{a}) \cdot \operatorname{cosec} x)+\mathrm{c}$, where c is a constant of integration.
- **(D)** $\frac{-1}{\sin \mathrm{a}} \log (\sin (x-\mathrm{a}) \cdot \operatorname{cosec} x)+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{\sin \mathrm{a}} \log (\sin (x-\mathrm{a}) \cdot \operatorname{cosec} x)+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int \operatorname{cosec}(x-a) \operatorname{cosec} x \, dx$

$I = \int \dfrac{1}{\sin(x-a) \sin x} \, dx$

Multiplying and dividing by $\sin a$:

$I = \dfrac{1}{\sin a} \int \dfrac{\sin a}{\sin(x-a) \sin x} \, dx$

Writing $a = x - (x-a)$ in the numerator:

$I = \dfrac{1}{\sin a} \int \dfrac{\sin(x - (x-a))}{\sin(x-a) \sin x} \, dx$

Using the formula $\sin(A-B) = \sin A \cos B - \cos A \sin B$:

$I = \dfrac{1}{\sin a} \int \dfrac{\sin x \cos(x-a) - \cos x \sin(x-a)}{\sin(x-a) \sin x} \, dx$

$I = \dfrac{1}{\sin a} \int \left( \dfrac{\sin x \cos(x-a)}{\sin(x-a) \sin x} - \dfrac{\cos x \sin(x-a)}{\sin(x-a) \sin x} \right) \, dx$

$I = \dfrac{1}{\sin a} \int (\cot(x-a) - \cot x) \, dx$

Integrating with respect to $x$:

$I = \dfrac{1}{\sin a} (\log(\sin(x-a)) - \log(\sin x)) + c$

$I = \dfrac{1}{\sin a} \log \left( \dfrac{\sin(x-a)}{\sin x} \right) + c$

$I = \dfrac{1}{\sin a} \log (\sin(x-a) \cdot \operatorname{cosec} x) + c$

Answer: $\frac{1}{\sin \mathrm{a}} \log (\sin (x-\mathrm{a}) \cdot \operatorname{cosec} x)+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q6. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int \frac{\sec x \cdot \tan x}{9-16 \tan ^2 x} \mathrm{~d} x$ is equal to

**Options:**

- **(A)** $\frac{1}{24} \log \left(\frac{5+4 \sec x}{5-4 \sec x}\right)+\mathrm{c}$, (where c is a constant of integration)
- **(B)** $\frac{1}{40} \log \left(\frac{5+4 \sec x}{5-4 \sec x}\right)+\mathrm{c}$, (where c is a constant of integration)
- **(C)** $\frac{1}{24} \log \left(\frac{5-4 \sec x}{5+4 \sec x}\right)+\mathrm{c}$, (where c is a constant of integration)
- **(D)** $\frac{1}{40} \log \left(\frac{5-4 \sec x}{5+4 \sec x}\right)+\mathrm{c}$, (where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{40} \log \left(\frac{5+4 \sec x}{5-4 \sec x}\right)+\mathrm{c}$, (where c is a constant of integration)**

**Detailed Solution:**

Let $I = \int \dfrac{\sec x \cdot \tan x}{9 - 16 \tan^2 x} \mathrm{~d} x$

Using the identity $\tan^2 x = \sec^2 x - 1$, the denominator becomes:

$9 - 16(\sec^2 x - 1) = 25 - 16 \sec^2 x$

$I = \int \dfrac{\sec x \cdot \tan x}{25 - 16 \sec^2 x} \mathrm{~d} x$

Substitute $\sec x = t$, which gives $\sec x \tan x \mathrm{~d} x = \mathrm{d} t$

$I = \int \dfrac{1}{25 - 16 t^2} \mathrm{~d} t$

$I = \dfrac{1}{16} \int \dfrac{1}{\left(\dfrac{5}{4}\right)^2 - t^2} \mathrm{~d} t$

Using the standard integral formula $\int \dfrac{1}{a^2 - x^2} \mathrm{~d} x = \dfrac{1}{2a} \log \left| \dfrac{a+x}{a-x} \right| + c$:

$I = \dfrac{1}{16} \cdot \dfrac{1}{2 \left(\dfrac{5}{4}\right)} \log \left| \dfrac{\dfrac{5}{4} + t}{\dfrac{5}{4} - t} \right| + c$

$I = \dfrac{1}{16} \cdot \dfrac{2}{5} \log \left| \dfrac{5 + 4t}{5 - 4t} \right| + c$

$I = \dfrac{1}{40} \log \left| \dfrac{5 + 4 \sec x}{5 - 4 \sec x} \right| + c$

Answer: $\frac{1}{40} \log \left(\frac{5+4 \sec x}{5-4 \sec x}\right)+\mathrm{c}$, (where c is a constant of integration)

</details>

---

### Q7. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int \frac{\mathrm{d} x}{7+6 x-x^2}$ is equal to

**Options:**

- **(A)** $\frac{1}{4} \log \left(\frac{1+x}{7-x}\right)+\mathrm{c}$, (where c is a constant of integration)
- **(B)** $\frac{1}{8} \log \left(\frac{7-x}{1+x}\right)+\mathrm{c},($ where c is a constant of integration)
- **(C)** $\frac{1}{4} \log \left(\frac{7-x}{1+x}\right)+\mathrm{c}$, (where c is a constant of integration)
- **(D)** $\frac{1}{8} \log \left(\frac{1+x}{7-x}\right)+\mathrm{c}$, (where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{8} \log \left(\frac{1+x}{7-x}\right)+\mathrm{c}$, (where c is a constant of integration)**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{7+6 x-x^2}$

The quadratic expression in the denominator can be rewritten by completing the square:

$7+6x-x^2 = 16 - 9 + 6x - x^2 = 16 - (x^2 - 6x + 9) = 4^2 - (x-3)^2$

Substituting this back into the integral, we get:

$I = \int \dfrac{\mathrm{d} x}{4^2 - (x-3)^2}$

Using the standard integration formula $\int \dfrac{\mathrm{d} x}{a^2 - x^2} = \dfrac{1}{2a} \log \left( \dfrac{a+x}{a-x} \right) + c$

Here, $a = 4$ and the variable part is $(x-3)$:

$I = \dfrac{1}{2(4)} \log \left( \dfrac{4 + (x-3)}{4 - (x-3)} \right) + c$

$I = \dfrac{1}{8} \log \left( \dfrac{1+x}{7-x} \right) + c$

Answer: $\frac{1}{8} \log \left(\frac{1+x}{7-x}\right)+\mathrm{c}$, (where c is a constant of integration)

</details>

---

### Q8. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int\left(1+x-\dfrac{1}{x}\right) \mathrm{e}^{x+\dfrac{1}{x}} \mathrm{~d} x$ equal to

**Options:**

- **(A)** $(x+1) \mathrm{e}^{x+\dfrac{1}{x}}+\mathrm{c}$, (where c is a constant of integration)
- **(B)** $-x \mathrm{e}^{x+\dfrac{1}{x}}+\mathrm{c}$, (where c is a constant of integration)
- **(C)** $\quad(x-1) \mathrm{e}^{x+\dfrac{1}{x}}+\mathrm{c}$, (where c is a constant of integration)
- **(D)** $x \mathrm{e}^{x+\dfrac{1}{x}}+\mathrm{c}$, (where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x \mathrm{e}^{x+\dfrac{1}{x}}+\mathrm{c}$, (where c is a constant of integration)**

**Detailed Solution:**

Let $I = \int \left(1 + x - \dfrac{1}{x}\right) \mathrm{e}^{x + \dfrac{1}{x}} \mathrm{d}x$

Splitting the integral, we get:

$I = \int \mathrm{e}^{x + \dfrac{1}{x}} \mathrm{d}x + \int \left(x - \dfrac{1}{x}\right) \mathrm{e}^{x + \dfrac{1}{x}} \mathrm{d}x$

$I = \int \mathrm{e}^{x + \dfrac{1}{x}} \mathrm{d}x + \int x \left(1 - \dfrac{1}{x^2}\right) \mathrm{e}^{x + \dfrac{1}{x}} \mathrm{d}x$

Applying integration by parts on the second integral, taking $x$ as the first function and $\left(1 - \dfrac{1}{x^2}\right) \mathrm{e}^{x + \dfrac{1}{x}}$ as the second function:

$\int x \left(1 - \dfrac{1}{x^2}\right) \mathrm{e}^{x + \dfrac{1}{x}} \mathrm{d}x = x \mathrm{e}^{x + \dfrac{1}{x}} - \int 1 \cdot \mathrm{e}^{x + \dfrac{1}{x}} \mathrm{d}x$

Substituting this back into the expression for $I$:

$I = \int \mathrm{e}^{x + \dfrac{1}{x}} \mathrm{d}x + x \mathrm{e}^{x + \dfrac{1}{x}} - \int \mathrm{e}^{x + \dfrac{1}{x}} \mathrm{d}x$

$I = x \mathrm{e}^{x + \dfrac{1}{x}} + \mathrm{c}$

Answer: $x \mathrm{e}^{x+\dfrac{1}{x}}+\mathrm{c}$, (where c is a constant of integration)

</details>

---

### Q9. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}\left(\dfrac{x-4}{x-2}\right)=2 x+1, x \in \mathbb{R}-\{1,-2\}$, then $\int \mathrm{f}(x) \mathrm{d} x$ is equal to

**Options:**

- **(A)** $5 x-4 \log (x-1)+\mathrm{c}$, where c is constant of integration.
- **(B)** $x-4 \log (x-1)+c$, where c is constant of integration.
- **(C)** $5 x+4 \log (x-1)+\mathrm{c}$, where c is constant of integration.
- **(D)** $5 x+\log (x-1)+\mathrm{c}$, where c is constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5 x-4 \log (x-1)+\mathrm{c}$, where c is constant of integration.**

**Detailed Solution:**

Let $t = \dfrac{x-4}{x-2}$

$tx - 2t = x - 4$

$x(t-1) = 2t - 4$

$x = \dfrac{2t-4}{t-1}$

Substituting $x$ in the given equation:

$f(t) = 2\left(\dfrac{2t-4}{t-1}\right) + 1$

$f(t) = \dfrac{4t-8+t-1}{t-1} = \dfrac{5t-9}{t-1}$

Replacing $t$ with $x$:

$f(x) = \dfrac{5x-9}{x-1} = \dfrac{5(x-1)-4}{x-1} = 5 - \dfrac{4}{x-1}$

Integrating with respect to $x$:

$\int f(x) \mathrm{d} x = \int \left(5 - \dfrac{4}{x-1}\right) \mathrm{d} x$

$\int f(x) \mathrm{d} x = 5x - 4 \log(x-1) + c$

Answer: $5 x-4 \log (x-1)+\mathrm{c}$, where c is constant of integration.

</details>

---

### Q10. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \cos ^{\frac{3}{5}} x \cdot \sin ^3 x \mathrm{~d} x=\frac{-1}{\mathrm{~m}} \cos ^{\mathrm{m}} x+\frac{1}{\mathrm{n}} \cos ^{\mathrm{n}} x+\mathrm{c}$, (where $c$ is the constant of integration), then $(\mathrm{m}, \mathrm{n})=$

**Options:**

- **(A)** $\left(\frac{18}{5}, \frac{8}{5}\right)$
- **(B)** $\left(\frac{-8}{5}, \frac{18}{5}\right)$
- **(C)** $\left(\frac{8}{5}, \frac{18}{5}\right)$
- **(D)** $\left(\frac{-18}{5}, \frac{-8}{5}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\frac{8}{5}, \frac{18}{5}\right)$**

**Detailed Solution:**

Let
$$
\begin{aligned}
\mathbf{I} & =\int \cos ^{\frac{3}{5}} x \sin ^3 x \mathrm{~d} x \\
& =\int \cos ^{\frac{3}{5}} x\left(1-\cos ^2 x\right) \sin x \mathrm{~d} x \\
& =\int \cos ^{\frac{3}{5}} x \sin x \mathrm{~d} x-\int \cos ^{\frac{13}{5}} x \sin x \mathrm{~d} x
\end{aligned}
$$
Let $\cos x=\mathrm{t} \Rightarrow-\sin x \mathrm{~d} x=\mathrm{dt}$
$$
\begin{aligned}
\therefore \quad I & =-\int t^{\frac{3}{5}} d t+\int t^{\frac{13}{5}} d t \\
& =\frac{-1}{\left(\frac{8}{5}\right)} t^{\frac{8}{5}}+\frac{1}{\left(\frac{18}{5}\right)} t^{\frac{13}{5}}+c \\
& =\frac{-1}{\left(\frac{8}{5}\right)} \cos ^{\frac{8}{5}} x+\frac{1}{\left(\frac{18}{5}\right)} \cos ^{\frac{13}{5}} x+\mathrm{c}
\end{aligned}
$$
Comparing with $\frac{-1}{\mathrm{~m}} \cos ^{\mathrm{m}} x+\frac{1}{\mathrm{n}} \cos ^{\mathrm{n}} x+\mathrm{c}$, we get $\mathrm{m}=\frac{8}{5}, \mathrm{n}=\frac{18}{5}$

</details>

---

### Q11. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \mathrm{e}^x\left(1-\cot x+\cot ^2 x\right) \mathrm{d} x=$

**Options:**

- **(A)** $\mathrm{e}^x \cdot \cot x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\mathrm{e}^x \cdot \operatorname{cosec} x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $-\mathrm{e}^x \cdot \cot x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $-\mathrm{e}^x \cdot \operatorname{cosec} x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\mathrm{e}^x \cdot \cot x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$\begin{aligned} & \int \mathrm{e}^x\left(1-\cot x+\cot ^2 x\right) \mathrm{d} x \\ & =\int \mathrm{e}^x\left(1+\cot ^2 x-\cot x\right) \mathrm{d} x \\ & =\int \mathrm{e}^x\left(-\cot x+\operatorname{cosec}^2 x\right) \mathrm{d} x \\ & =\mathrm{e}^x(-\cot x)+\mathrm{c} \\ & \quad \cdots\left[\because \int \mathrm{e}^x\left[\mathrm{f}(x)+\mathrm{f}^{\prime}(x)\right] \mathrm{d} x=\mathrm{e}^x \mathrm{f}(x)+\mathrm{c}\right] \\ & =-\mathrm{e}^x \cdot \cot x+\mathrm{c}\end{aligned}$

</details>

---

### Q12. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \sqrt{\frac{x-7}{x-9}} \mathrm{~d} x=A \sqrt{x^2-16 x+63}$
$+\log \left|(x-8)+\sqrt{x^2-16 x+63}\right|+c,$
(where $\mathrm{c}$ is a constant of integration) then $\mathrm{A}$ is

**Options:**

- **(A)** $-1$
- **(B)** $\frac{1}{2}$
- **(C)** 1
- **(D)** $\frac{-1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

Let $\mathrm{I}=\int \sqrt{\frac{x-7}{x-9}} \mathrm{~d} x$
$\begin{aligned}
& =\int \sqrt{\frac{(x-7)(x-7)}{(x-9)(x-7)}} \mathrm{d} x \\
& =\int \frac{x-7}{\sqrt{x^2-16 x+63}} \mathrm{~d} x
\end{aligned}$
Let $(x-7)=\mathrm{A}\left[\frac{\mathrm{d}}{\mathrm{d} x}\left(x^2-16 x+63\right)\right]+\mathrm{B}$
$\begin{aligned}
& \therefore \quad x-7=\mathrm{A}(2 x-16)+\mathrm{B} \\
& \therefore \quad x-7=2 \mathrm{~A} x-16 \mathrm{~A}+\mathrm{B} \\
& \therefore \quad \mathrm{A}=\frac{1}{2}, \mathrm{~B}=1 \\
& \therefore \quad \mathrm{I}=\int \frac{\frac{1}{2}(2 x-16)+1}{\sqrt{x^2-16 x+63}} \mathrm{~d} x \\
& =\frac{1}{2} \int \frac{2 x-16}{\sqrt{x^2-16 x+63}} \mathrm{~d} x+\int \frac{1}{\sqrt{x^2-16 x+63}} \mathrm{~d} x \\
& =\frac{1}{2} \times 2 \sqrt{x^2-16 x+63}+\int \frac{1}{\sqrt{(x-8)^2-(1)^2}} \mathrm{~d} x \\
& \ldots\left[\int \frac{\mathrm{f}^{\prime}(x)}{\sqrt{\mathrm{f}(x)}} \mathrm{d} x=2 \sqrt{\mathrm{f}(x)}+\mathrm{c}\right] \\
& \therefore \quad \mathrm{I}=\sqrt{x^2-16 x+63}+\log \left|x-8+\sqrt{x^2-16 x+63}\right|+\mathrm{c} \\
&\end{aligned}$
But, $\int \sqrt{\frac{x-7}{x-9}} \mathrm{~d} x=A \sqrt{x^2-16 x+63}$
$+\log \left|(x-8)+\sqrt{x^2-16 x+63}\right|+\mathrm{c}$
Comparing, we get
$A=1$

</details>

---

### Q13. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$$
\int \frac{\sin 2 x}{4 \sin ^2 x+9 \cos ^2 x} \mathrm{~d} x=
$$
(Where $C$ is a constant of integration).

**Options:**

- **(A)** $-\log \left(4 \sin ^2 x+9 \cos ^2 x\right)+C$
- **(B)** $\frac{1}{5} \log \left(4 \sin ^2 x+9 \cos ^2 x\right)+C$
- **(C)** $-\frac{1}{5} \log \left(4 \sin ^2 x+9 \cos ^2 x\right)+C$
- **(D)** $\log \left(4 \sin ^2 x+9 \cos ^2 x\right)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{1}{5} \log \left(4 \sin ^2 x+9 \cos ^2 x\right)+C$**

**Detailed Solution:**

Let $4 \sin ^2 x+9 \cos ^2 x=t$
$\begin{aligned} & \Rightarrow(4 \times 2 \sin x \cdot \cos x-9 \times 2 \cos x \sin x) \mathrm{d} x=\mathrm{d} t \\ & \Rightarrow-5 \sin 2 x \mathrm{~d} x=\mathrm{d} t \\ & \Rightarrow-\frac{1}{5} \int \frac{\mathrm{d} t}{t}=-\log |t|+c \\ & =-\frac{1}{5} \log \left|4 \sin ^2 x+9 \cos ^2 x\right|+c\end{aligned}$

</details>

---

### Q14. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \sin \sqrt{x} \mathrm{~d} x=\ldots+C$
(where $C$ is a constant of integration.)

**Options:**

- **(A)** $2(-\sqrt{x} \cos \sqrt{x}+\sin \sqrt{x})$
- **(B)** $2(-\cos \sqrt{x}+\sin \sqrt{x})$
- **(C)** $2(\cos \sqrt{x}+\sqrt{x} \sin \sqrt{x})$
- **(D)** $2(\sqrt{x} \cos \sqrt{x}+\sin \sqrt{x})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2(-\sqrt{x} \cos \sqrt{x}+\sin \sqrt{x})$**

**Detailed Solution:**

$\begin{aligned} & \int \sin \sqrt{x} \mathrm{~d} x \text { let } \sqrt{x}=t \\ & \Rightarrow \mathrm{d} x=2 t \mathrm{~d} t \\ & =2 \int t \sin t \mathrm{~d} t \\ & =2\left\{t \int \sin t \mathrm{~d} t-\int\left(\frac{\mathrm{d} t}{\mathrm{~d} t} \int \sin t \mathrm{~d} t\right) \mathrm{d} t\right\} \text { [integrating by parts] } \\ & =2\left\{t(-\cos t)+\int \cos t \mathrm{~d} t\right\} \\ & =2\{-t \cos t+\sin t\}+C \\ & =2\{-\sqrt{x} \cos \sqrt{x}+\sin \sqrt{x}\}+C\end{aligned}$

</details>

---

### Q15. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}(\mathrm{x})=\frac{1}{\log \mathrm{x}}, \mathrm{g}(\mathrm{x})=\frac{1}{(\log \mathrm{x})^2}$
(Where C is a constant of integration.)

**Options:**

- **(A)** $(\log x)^2+C$
- **(B)** $x \log x+C$
- **(C)** $\frac{x}{\log x}+C$
- **(D)** $\frac{1}{\log x}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{x}{\log x}+C$**

**Detailed Solution:**

$\begin{aligned} & \int\{f(x)-g(x)\} d x=\int f(x) d x-\int g(x) d x \\ & =\int \frac{1}{\log x} d x-\int \frac{1}{(\log x)^2} d x \\ & =\int \frac{1}{\log x} \times 1 d x-\int \frac{1}{(\log x)^2} d x \\ & =\frac{1}{\log x} \cdot x-\int \frac{-1}{(\log x)^2} \times \frac{1}{x} \times x d x-\int \frac{1}{(\log x)^2} d x \\ & =\frac{x}{\log x}+\int \frac{1}{(\log x)^2} d x-\int \frac{d x}{(\log x)^2} \\ & =\frac{x}{\log x}\end{aligned}$

</details>

---

### Q16. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

For $-\frac{\pi}{2}<x<\frac{\pi}{2}, \int \tan ^{-1}\left(\sqrt{\frac{1-\sin x}{1+\sin x}}\right) d x=$
(Where $\mathrm{C}$ is a constant of integration)

**Options:**

- **(A)** $\frac{\pi}{4} x+\frac{x^2}{2}+C$
- **(B)** $\frac{\pi}{4}-\frac{x^2}{2}+C$
- **(C)** $\frac{\pi}{4}+\frac{x^2}{2}+C$
- **(D)** $\frac{\pi}{4} x-\frac{x^2}{4}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{4} x-\frac{x^2}{4}+C$**

**Detailed Solution:**

$\begin{aligned} & \int \tan ^{-1}\left(\sqrt{\frac{1-\sin x}{1+\sin x}}\right) d x=\int \tan ^{-1} \sqrt{\frac{\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)^2}{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)^2}} d x \\ & =\int \tan ^{-1}\left(\frac{\cos \frac{x}{2}-\sin \frac{x}{2}}{\cos \frac{x}{2}+\sin \frac{x}{2}}\right) d x=\int \tan ^{-1}\left(\frac{1-\tan \frac{x}{2}}{1+\tan \frac{x}{2}}\right) d x \\ & =\int \tan ^{-1} \tan \left(\frac{\pi}{4}-\frac{x}{2}\right) d x=\int\left(\frac{\pi}{4}-\frac{x}{2}\right) d x \\ & =\frac{\pi}{2} x-\frac{x^2}{4}+C\end{aligned}$

</details>

---

### Q17. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int e^x\left(\frac{1+\sin x}{1+\cos x}\right) d x=$

**Options:**

- **(A)** $\mathrm{e}^{\mathrm{x}} \tan \frac{\mathrm{x}}{2}+\mathrm{c}$
- **(B)** $e^x \cot \frac{x}{2}+c$
- **(C)** $\mathrm{e}^{\mathrm{x}} \cos \frac{\mathrm{x}}{2}+\mathrm{c}$
- **(D)** $e^x \sin \frac{x}{2}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{e}^{\mathrm{x}} \tan \frac{\mathrm{x}}{2}+\mathrm{c}$**

**Detailed Solution:**

$\begin{aligned} & I=\int e^x\left(\frac{1+\sin x}{1+\cos x}\right) d x=\int e^x\left(\frac{1}{1+\cos x}+\frac{\sin x}{1+\cos x}\right) d x \\ & =\int e^x\left(\frac{1}{2 \cos ^2 \frac{x}{2}}+\frac{2 \sin \frac{x}{2} \cos \frac{x}{2}}{2 \cos ^2 \frac{x}{2}}\right) d x=\int e^x\left(\frac{1}{2}\right)\left(\sec ^2 \frac{x}{2}+2 \tan \frac{x}{2}\right) d x \\ & =\frac{1}{2} \int e^x\left[2 \tan \frac{x}{2}+\sec ^2 \frac{x}{2}\right] d x=\frac{1}{2} \cdot e^x(2)+\tan \left(\frac{x}{2}\right)+c=e^x \tan \frac{x}{2}+c\end{aligned}$

</details>

---

### Q18. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \frac{5 \tan x}{\tan x-2} d x=x+a \log |\sin x-2 \cos x|+c$, then $a$ (Where $\mathrm{c}$ is constant of integration)

**Options:**

- **(A)** 1
- **(B)** -2
- **(C)** -1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

Let $I=\int \frac{5 \tan x}{\tan x-2} d x$
$$
I=\int \frac{5 \sin x}{\sin x-2 \cos x} d x
$$
Here $\frac{d}{d x}(\sin x-2 \cos x)=\cos x+2 \sin x$
$$
\begin{aligned}
\therefore \mathrm{I} & =\int \frac{(2 \sin x+2 \sin x+\sin x)+(2 \cos x-2 \cos x)}{\sin x-2 \cos x} d x \\
& =\int \frac{(2 \sin x+\cos x)+(2 \sin x+\cos x)+(\sin x-2 \cos x)}{\sin x-2 \cos x} d x \\
& =\int \frac{2(2 \sin x+\cos x)+(\sin x-2 \cos x)}{\sin x-2 \cos x} d x \\
& =\int d x+2 \int \frac{2 \sin x+\cos x}{\sin x-2 \cos x} d x \\
& =x+2 \log |\sin x-2 \cos x|+c
\end{aligned}
$$
From given data, $a=2$

</details>

---

### Q19. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \frac{\sin \theta}{\sin 3 \theta} d \theta=\frac{1}{2 k} \log \left|\frac{k+\tan \theta}{k-\tan \theta}\right|+c$, then $k=$

**Options:**

- **(A)** $\sqrt{3}$
- **(B)** $\sqrt{2}$
- **(C)** $\sqrt{7}$
- **(D)** $\sqrt{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{3}$**

**Detailed Solution:**

(A)
$\begin{aligned}
\int \frac{\sin \theta}{\sin 3 \theta} d \theta &=\int \frac{\sin \theta}{3 \sin \theta-4 \sin ^{2} \theta} d \theta=\int \frac{\sin \theta}{\sin \theta\left(3-4 \sin ^{2} \theta\right)} d \theta \\
&=\int \frac{1}{3-4 \sin ^{2} \theta} d \theta
\end{aligned}$
Dividing both numerator and denominator by $\cos ^{2} \theta$, we get
$\begin{aligned}
I &=\int \frac{\sec ^{2} \theta}{3 \sec ^{2} \theta-4 \tan ^{2} \theta} d \theta=\int \frac{\sec ^{2} \theta}{3\left(1+\tan ^{2} \theta\right)-4 \tan ^{2} \theta} d \theta \\
I &=\int \frac{\sec ^{2} \theta}{3-\tan ^{2} \theta} d \theta
\end{aligned}$
Put $\tan \theta=t \Rightarrow \sec ^{2} \theta d \theta=d t$
$I=\int \frac{1}{(\sqrt{3})^{2}-t^{2}} d t=\frac{1}{2 \sqrt{3}} \log \left|\frac{\sqrt{3}+t}{\sqrt{3}-t}\right|=\frac{1}{2 \sqrt{3}} \log \left|\frac{\sqrt{3}+\tan \theta}{\sqrt{3}-\tan \theta}\right|$
Comparing with given data, we get $\mathrm{k}=\sqrt{3}$

</details>

---

### Q20. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \mathrm{e}^{x}\left(\frac{1-x}{1+x^{2}}\right)^{2} \mathrm{~d} x=$

**Options:**

- **(A)** $\mathrm{e}^{x}\left(\frac{1}{1+x^{2}}\right)+\mathrm{C}$
- **(B)** $\mathrm{e}^{x}\left(\frac{-1}{1+x^{2}}\right)+\mathrm{C}$
- **(C)** $\mathrm{e}^{x}\left(\frac{2}{1+x^{2}}\right)+\mathrm{C}$
- **(D)** $\mathrm{e}^{x}\left(\frac{-2}{1+x^{2}}\right)+\mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{e}^{x}\left(\frac{1}{1+x^{2}}\right)+\mathrm{C}$**

**Detailed Solution:**

$\begin{aligned} I &=\int e^{x}\left(\frac{1-x}{1+x^{2}}\right)^{2} d x \\ &=\int e^{x} \frac{\left(1+x^{2}-2 x\right)}{\left(1+x^{2}\right)^{2}} d x=\int e^{x}\left[\frac{1+x^{2}}{\left(1+x^{2}\right)^{2}}-\frac{2 x}{\left(1+x^{2}\right)^{2}}\right] d x \\ &=\int e^{x}\left[\frac{1}{1+x^{2}}-\frac{2 x}{\left(1+x^{2}\right)^{2}}\right] d x=\frac{e^{x}}{1+x^{2}}+C \end{aligned}$

</details>

---

### Q21. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$$
\int\left[\frac{1-\log x}{1+(\log x)^{2}}\right]^{2} d x=
$$

**Options:**

- **(A)** $\frac{1}{1+(\log x)^{2}}+c$
- **(B)** $\frac{x}{1+(\log x)^{2}}+c$
- **(C)** $\frac{1}{1+\log x}+c$
- **(D)** $\frac{x}{1+\log x}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{x}{1+(\log x)^{2}}+c$**

**Detailed Solution:**

$\begin{aligned}{\text{Let}} I &=\int\left[\frac{1-\log x}{1+(\log x)^{2}}\right]^{2} d x \\ \text { Put } \log x &=t \Rightarrow \frac{1}{x} d x=d t \Rightarrow d x=x \text { dt i.e. } d x=e^{t} d t \\ \therefore I &=\int e^{t}\left[\frac{1-t}{1+t^{2}}\right]^{2} d t=\int e^{t} \frac{(1-t)^{2}}{\left(1+t^{2}\right)^{2}} d t=\int e^{t}\left[\frac{1+t^{2}-2 t}{\left(1+t^{2}\right)^{2}}\right] d t \\ I &=\int e^{t}\left[\frac{1}{1+t^{2}}-\frac{2 t}{\left(1+t^{2}\right)^{2}}\right] d t=\frac{e^{t}}{1+t^{2}}+c \\ I &=\frac{x}{1+(\log x)^{2}}+c \end{aligned}$

</details>

---

### Q22. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\sin x}{\sin \left(x-\frac{\pi}{4}\right)} d x=$

**Options:**

- **(A)** $\frac{1}{\sqrt{2}}\left[x+\log \left|\sin \left(x-\frac{\pi}{4}\right)\right|\right]+c$
- **(B)** $x+\log \left|\sin \left(x-\frac{\pi}{4}\right)\right|+c$
- **(C)** $x-\log \left|\sin \left(x-\frac{\pi}{4}\right)\right|+c$
- **(D)** $\frac{1}{\sqrt{2}}\left[x-\log \left|\sin \left(x-\frac{\pi}{4}\right)\right|\right]+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\sqrt{2}}\left[x+\log \left|\sin \left(x-\frac{\pi}{4}\right)\right|\right]+c$**

**Detailed Solution:**

$\begin{aligned} I &=\int \frac{\sin x}{\sin \left(x-\frac{\pi}{4}\right)} d x \\ &=\int \frac{\sin \left(x-\frac{\pi}{4}+\frac{\pi}{4}\right)}{\sin \left(x-\frac{\pi}{4}\right)} d x=\int \frac{\sin \left(x-\frac{\pi}{4}\right) \cos \frac{\pi}{4}+\cos \left(x-\frac{\pi}{4}\right) \sin \frac{\pi}{4}}{\sin \left(x-\frac{\pi}{4}\right)} \\ &=\int\left(\frac{1}{\sqrt{2}}+\cot \left(x-\frac{\pi}{4}\right) \cdot \frac{1}{\sqrt{2}}\right) d x=\int \frac{1}{\sqrt{2}}\left[1+\cot \left(x-\frac{\pi}{4}\right)\right] d x \\ &=\frac{1}{\sqrt{2}}\left[\int 1 d x+\int \cot \left(x-\frac{\pi}{4}\right)\right] d x=\frac{1}{\sqrt{2}}\left[x+\log \left(\sin \left(x-\frac{\pi}{4}\right)\right]+c\right.\end{aligned}$

</details>

---

### Q23. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int\left[\log (1+\cos x)-x \tan \left(\frac{x}{2}\right)\right] d x=$

**Options:**

- **(A)** $x \log |x|+c$
- **(B)** $x \log |1+\sin x|+c$
- **(C)** $x \log \left|\tan \frac{x}{2}\right|+c$
- **(D)** $x \log |1+\cos x|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x \log |1+\cos x|+c$**

**Detailed Solution:**

$$
\begin{aligned}
I &=\int\left[\log (1+\cos x)-x \tan \left(\frac{x}{2}\right)\right] d x \\
I &=\int \log (1+\cos x) \cdot 1 d x-\int x \tan \frac{x}{2} d x \\
&=x \log (1+\cos x)-\int \frac{(-\sin x)(x)}{1+\cos x} d x-\int x \tan \frac{x}{2}
\end{aligned}
$$
$=x \log (1+\cos x)+\int \frac{x\left(2 \sin \frac{x}{2} \cos \frac{x}{2}\right)}{2 \cos ^{2} \frac{x}{2}} d x-\int x \tan \frac{x}{2} d x$
$=x \log (1+\cos x)+\int x \tan \frac{x}{2} d x-\int x \tan \frac{x}{2} d x$
$=x \log (1+\cos x)+c$

</details>

---

### Q24. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{x^{2}+1}{x^{4}+x^{2}+1} d x=$

**Options:**

- **(A)** $\frac{1}{\sqrt{3}} \tan ^{-1}\left(\frac{x-\frac{1}{x}}{\sqrt{3}}\right)+c$
- **(B)** $\frac{1}{3} \tan ^{-1}\left(\frac{x-\frac{1}{x}}{3}\right)+c$
- **(C)** $\frac{1}{\sqrt{3}} \tan ^{-1}\left(\frac{x+\frac{1}{x}}{\sqrt{3}}\right)+c$
- **(D)** $\frac{1}{3} \tan ^{-1}\left(\frac{x+\frac{1}{x}}{3}\right)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\sqrt{3}} \tan ^{-1}\left(\frac{x-\frac{1}{x}}{\sqrt{3}}\right)+c$**

**Detailed Solution:**

Let 
$\begin{aligned} I &=\int \frac{x^{2}+1}{x^{4}+x^{2}+1} d x \\ &=\int \frac{x^{2}\left(1+\frac{1}{x^{2}}\right)}{x^{2}\left(x^{2}+1+\frac{1}{x^{2}}\right)} d x=\int \frac{1+\frac{1}{x^{2}}}{\left(x^{2}+\frac{1}{x^{2}}-2\right)+3} \\ I &=\int \frac{1+\frac{1}{x^{2}}}{\left(x-\frac{1}{x}\right)^{2}+(\sqrt{3})^{2}} d x \end{aligned}$
Put $x-\frac{1}{x}=t \Rightarrow\left(1+\frac{1}{x^{2}}\right) d x=d t$
$\therefore I=\int \frac{d t}{t^{2}+(\sqrt{3})^{2}}$
$=\frac{1}{\sqrt{3}} \tan ^{-1}\left(\frac{t}{\sqrt{3}}\right)+c=\frac{1}{\sqrt{3}} \tan ^{-1}\left(\frac{x-\frac{1}{x}}{\sqrt{3}}\right)+c$

</details>

---

### Q25. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{\sin 2 x}{\sin ^{2} x \cos ^{2} x} d x=$

**Options:**

- **(A)** $\log \left|\tan ^{2} x\right|+c$
- **(B)** $\log \left|\sec ^{2} x\right|+c$
- **(C)** $\log |\tan x|+c$
- **(D)** $\log |\sec x|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log \left|\tan ^{2} x\right|+c$**

**Detailed Solution:**

$\begin{aligned} I &=\int \frac{\sin 2 x}{\sin ^{2} x \cos ^{2} x}=\int \frac{2 \sin x \cos x d x}{\sin ^{2} x \cos ^{2} x}=2 \int \frac{1}{\sin x \cos x} d x=2 \int \frac{2}{2 \sin x \cos x} d x \\ &=2 \times 2 \int \frac{1}{\sin 2 x} d x=4 \int \operatorname{cosec} 2 x d x \\ &=2 \log |\tan x|+c=\log \left|\tan ^{2} x\right|+c \end{aligned}$

</details>

---

### Q26. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<math><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></msubsup><mrow><mfrac><mrow><mn>2</mn><msqrt><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></msqrt></mrow><mrow><msqrt><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></msqrt><mo>+</mo><msqrt><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></msqrt></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mo>…</mo></math>

**Options:**

- **(A)** <math><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>36</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>5</mn><mi>π</mi></mrow><mrow><mn>36</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>5</mn><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></math>**

**Detailed Solution:**

Let <math><mo>=</mo><mi>l</mi><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></msubsup><mrow><mfrac><mrow><mn>2</mn><msqrt><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></msqrt></mrow><mrow><msqrt><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></msqrt><mo>+</mo><msqrt><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></math>  
<math><mo>=</mo><mn>2</mn><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></msubsup><mrow><mfrac><mrow><msqrt><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></msqrt></mrow><mrow><msqrt><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></msqrt><mo>+</mo><msqrt><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></math> …(i) 
<math><mo>=</mo><mn>2</mn><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></msubsup><mrow><mfrac><mrow><msqrt><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mrow></msqrt></mrow><mrow><msqrt><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>8</mn></mrow></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mrow></msqrt><mo>+</mo><msqrt><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>8</mn></mrow></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mrow></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></math>  
<math><mfenced separators="|"><mrow><mo>∵</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></msubsup><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo></mrow></mrow><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></msubsup><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mi>l</mi><mo>=</mo><mn>2</mn><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></msubsup><mrow><mfrac><mrow><msqrt><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></msqrt></mrow><mrow><msqrt><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></msqrt><mo>+</mo><msqrt><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></math> …(ii) 
On adding Eqs. (i) and (ii), we get 
<math><mn>2</mn><mi>l</mi><mo>=</mo><mn>2</mn><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></msubsup><mrow><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></msubsup></mrow></mrow></math>  
<math><mo>=</mo><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mi>l</mi><mo>=</mo><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></math>

</details>

---

### Q27. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `3`

$\int_{0}^{\pi} \frac{x d x}{1+\cos \alpha \sin x},(0 < \alpha < \pi)$ is equal to

**Options:**

- **(A)** $\frac{\pi \alpha}{\sin \alpha}$
- **(B)** $\frac{\pi \alpha}{\cos \alpha}$
- **(C)** $\frac{\pi \alpha}{1+\sin \alpha}$
- **(D)** $\frac{\pi \alpha}{1+\cos \alpha}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi \alpha}{\sin \alpha}$**

**Detailed Solution:**

$$
\begin{array}{l}
\text { Let } I=\int_{0}^{\pi} \frac{x d x}{1+\cos \alpha \cdot \sin x} \quad \text { .. } \\
\Rightarrow \quad I=\int_{0}^{\pi} \frac{(\pi-x)}{1+\cos \alpha \cdot \sin (\pi-x)} d x \quad \ldots
\end{array}
$$
On adding Eqs. (i) and (ii), we get
$$
\begin{aligned}
2 I=\pi \int_{0}^{\pi} \frac{d x}{1+\cos \alpha \cdot \sin x} \\
=\pi \int_{0}^{\pi} \frac{d x}{1+\cos \alpha\left(\frac{2 \tan x / 2}{1+\tan ^{2} x / 2}\right)} \\
=\pi \int_{0}^{\pi} \frac{\sec ^{2} x / 2 d x}{\left(1+\tan ^{2} x / 2\right)+\cos \alpha(2 \tan x / 2)}
\end{aligned}
$$
Put $\quad \tan x / 2=t$
$$
\Rightarrow \quad(1 / 2) \sec ^{2} x / 2 d x=d t
$$
$\therefore$
$$
\begin{array}{l}
2 I=\pi \int_{0}^{\infty} \frac{2 d t}{1+t^{2}+2 t \cos \alpha} \\
I=\pi \int_{0}^{\infty} \frac{d t}{1+t^{2}+2 t \cos \alpha} \\
=\pi \int_{0}^{\infty} \frac{d t}{(t+\cos \alpha)^{2}+\sin ^{2} \alpha} \\
\quad=\frac{\pi}{\sin \alpha}\left[\tan ^{-1}\left(\frac{t+\cos \alpha}{\sin \alpha}\right)\right]_{0}^{\infty} \\
I=\frac{\pi \alpha}{\sin \alpha}
\end{array}
$$

</details>

---

### Q28. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

$\int_{5}^{10} \frac{1}{(x-1)(x-2)} d x$ is equal to

**Options:**

- **(A)** $\log \frac{27}{32}$
- **(B)** $\log \frac{32}{27}$
- **(C)** $\log \frac{8}{9}$
- **(D)** $\log \frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log \frac{32}{27}$**

**Detailed Solution:**

Let $I=\int_{5}^{10} \frac{1}{(x-1)(x-2)} d x$
$\quad=\int_{5}^{10}\left[\frac{-1}{x-1}+\frac{1}{x-2}\right] d x$
$=[-\log (x-1)+\log (x-2)]_{5}^{10}$
$=-\log 9+\log 8+\log 4-\log 3$
$=-2 \log 3+3 \log 2+2 \log 2-\log 3$
$=-3 \log 3+5 \log 2$
$=-\log 27+\log 32$
$=\log \frac{32}{27}$

</details>

---

### Q29. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `3`

$\int[\sin (\log x)+\cos (\log x)] d x$ is equal to

**Options:**

- **(A)** $x \cos (\log x)+c$
- **(B)** $\cos (\log x)+c$
- **(C)** $x \sin (\log x)+c$
- **(D)** $\sin (\log x)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x \sin (\log x)+c$**

**Detailed Solution:**

$\begin{aligned} \int[\sin (\log x)&+\cos (\log x)] d x \\ &=\int \frac{d}{d x}\{x \sin (\log x)\} d x \\ &=x \sin (\log x)+c \end{aligned}$

</details>

---

### Q30. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{x+\sin x}{1+\cos x} d x$ is equal to

**Options:**

- **(A)** $x \tan \frac{x}{2}+c$
- **(B)** $\log (1+\cos x)+c$
- **(C)** $\cot \frac{x}{2}+c$
- **(D)** $\log (x+\sin x)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x \tan \frac{x}{2}+c$**

**Detailed Solution:**

Let $I=\int \frac{x+\sin x}{1+\cos x} d x$
$$
\begin{array}{l}
=\int\left(\frac{x}{2} \sec ^{2} \frac{x}{2}+\tan \frac{x}{2}\right) d x \\
=x \tan \frac{x}{2}-\int \tan \frac{x}{2} d x+\int \tan \frac{x}{2} d x+c
\end{array}
$$
$=x \tan \frac{x}{2}+c$

</details>

---

