# MHT CET Mathematics - Limits

## Topic 2: Algebraic and Rational Limits

**Total Questions:** 54

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(9) = 36$, $u(9) = 9$, $f'(9) = 12$, $u'(9) = 4$, then $\displaystyle\lim_{x\to 9} \dfrac{\sqrt{f(x)} - 2\sqrt{u(x)}}{\sqrt{x} - 3} = \ldots$

**Options:**

- **(A)** $2$
- **(B)** $-2$
- **(C)** $3$
- **(D)** Does not exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-2$**

**Detailed Solution:**

The given limit is $\displaystyle\lim_{x\to 9} \dfrac{\sqrt{f(x)} - 2\sqrt{u(x)}}{\sqrt{x} - 3}$

Substituting $x = 9$, the expression takes the form $\dfrac{\sqrt{f(9)} - 2\sqrt{u(9)}}{\sqrt{9} - 3} = \dfrac{\sqrt{36} - 2\sqrt{9}}{3 - 3} = \dfrac{6 - 6}{0} = \dfrac{0}{0}$

Applying L'Hospital's rule, differentiating the numerator and the denominator with respect to $x$:

$\displaystyle\lim_{x\to 9} \dfrac{\dfrac{f'(x)}{2\sqrt{f(x)}} - \dfrac{2u'(x)}{2\sqrt{u(x)}}}{\dfrac{1}{2\sqrt{x}}}$

Substituting $x = 9$ into the expression:

$\dfrac{\dfrac{f'(9)}{2\sqrt{f(9)}} - \dfrac{u'(9)}{\sqrt{u(9)}}}{\dfrac{1}{2\sqrt{9}}}$

Substituting the given values $f(9) = 36$, $u(9) = 9$, $f'(9) = 12$, and $u'(9) = 4$:

$\dfrac{\dfrac{12}{2\sqrt{36}} - \dfrac{4}{\sqrt{9}}}{\dfrac{1}{2\sqrt{9}}}$

$\dfrac{\dfrac{12}{12} - \dfrac{4}{3}}{\dfrac{1}{6}}$

$\dfrac{1 - \dfrac{4}{3}}{\dfrac{1}{6}}$

$\dfrac{-\dfrac{1}{3}}{\dfrac{1}{6}} = -2$

Answer: $-2$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $k > 5$ and $\lim_{x \to 0} \dfrac{k^{2x} + 25^x - 2 \cdot (5k)^x}{\tan 3x \cdot \ln(1 + 3x)} = \lim_{n \to \infty} \dfrac{(n+1)! + n!}{(n+1)! - n!}$, then value of $k$ is...

**Options:**

- **(A)** $e^{15}$
- **(B)** $5e$
- **(C)** $3e^{9/2}$
- **(D)** $5e^3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5e^3$**

**Detailed Solution:**

Evaluating the right-hand side limit:

$\lim_{n \to \infty} \dfrac{(n+1)! + n!}{(n+1)! - n!} = \lim_{n \to \infty} \dfrac{n!(n+1 + 1)}{n!(n+1 - 1)} = \lim_{n \to \infty} \dfrac{n+2}{n} = \lim_{n \to \infty} \left(1 + \dfrac{2}{n}\right) = 1$

Evaluating the left-hand side limit:

$\lim_{x \to 0} \dfrac{k^{2x} + 25^x - 2 \cdot (5k)^x}{\tan 3x \cdot \ln(1 + 3x)}$

The numerator can be written as:

$k^{2x} + 5^{2x} - 2 \cdot k^x \cdot 5^x = (k^x - 5^x)^2$

Dividing the numerator and the denominator by $x^2$:

$\lim_{x \to 0} \dfrac{\left(\dfrac{k^x - 5^x}{x}\right)^2}{\left(\dfrac{\tan 3x}{x}\right) \cdot \left(\dfrac{\ln(1 + 3x)}{x}\right)}$

Using standard limits $\lim_{x \to 0} \dfrac{a^x - b^x}{x} = \ln\left(\dfrac{a}{b}\right)$, $\lim_{x \to 0} \dfrac{\tan ax}{x} = a$, and $\lim_{x \to 0} \dfrac{\ln(1 + ax)}{x} = a$:

$\dfrac{\left(\ln\left(\dfrac{k}{5}\right)\right)^2}{3 \cdot 3} = \dfrac{1}{9} \left(\ln\left(\dfrac{k}{5}\right)\right)^2$

Equating the left-hand side and the right-hand side:

$\dfrac{1}{9} \left(\ln\left(\dfrac{k}{5}\right)\right)^2 = 1$

$\left(\ln\left(\dfrac{k}{5}\right)\right)^2 = 9$

$\ln\left(\dfrac{k}{5}\right) = \pm 3$

Since $k > 5$, $\dfrac{k}{5} > 1$, which implies $\ln\left(\dfrac{k}{5}\right) > 0$.

$\ln\left(\dfrac{k}{5}\right) = 3$

$\dfrac{k}{5} = e^3$

$k = 5e^3$

Answer: $5e^3$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\displaystyle\lim_{x \to \infty}\left[\dfrac{x^3 + 1}{x^2 + 1} - (ax + b)\right] = 2$ then

**Options:**

- **(A)** $a = 1,\ b = 1$
- **(B)** $a = 1,\ b = -1$
- **(C)** $a = 1,\ b = -2$
- **(D)** $a = 1,\ b = 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $a = 1,\ b = -2$**

**Detailed Solution:**

The given limit is $\lim_{x \to \infty}\left[\dfrac{x^3 + 1}{x^2 + 1} - (ax + b)\right] = 2$

Simplifying the expression inside the limit:

$\dfrac{x^3 + 1 - (ax + b)(x^2 + 1)}{x^2 + 1}$

$= \dfrac{x^3(1 - a) - bx^2 - ax + (1 - b)}{x^2 + 1}$

For the limit to be finite as $x \to \infty$, the degree of the numerator must not exceed the degree of the denominator. Since the denominator is of degree $2$, the coefficient of $x^3$ in the numerator must be zero.

$1 - a = 0 \Rightarrow a = 1$

Substituting $a = 1$ into the limit expression:

$\lim_{x \to \infty} \dfrac{-bx^2 - x + (1 - b)}{x^2 + 1} = 2$

Dividing the numerator and the denominator by $x^2$:

$\lim_{x \to \infty} \dfrac{-b - \dfrac{1}{x} + \dfrac{1 - b}{x^2}}{1 + \dfrac{1}{x^2}} = 2$

$-b = 2 \Rightarrow b = -2$

Therefore, $a = 1$ and $b = -2$.

Answer: $a = 1,\ b = -2$

</details>

---

### Q4. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x) = \dfrac{ax - 3}{5x + 7}$ and $\lim_{x \to 0} f(x) \cdot \lim_{x \to \infty} f(x) = 3$ then $a = \ldots$

**Options:**

- **(A)** $35$
- **(B)** $-35$
- **(C)** $15$
- **(D)** $\dfrac{21}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-35$**

**Detailed Solution:**

Given $f(x) = \dfrac{ax - 3}{5x + 7}$

Evaluating the first limit:

$\lim_{x \to 0} f(x) = \lim_{x \to 0} \dfrac{ax - 3}{5x + 7} = -\dfrac{3}{7}$

Evaluating the second limit:

$\lim_{x \to \infty} f(x) = \lim_{x \to \infty} \dfrac{ax - 3}{5x + 7} = \lim_{x \to \infty} \dfrac{a - \dfrac{3}{x}}{5 + \dfrac{7}{x}} = \dfrac{a}{5}$

According to the given condition:

$\lim_{x \to 0} f(x) \cdot \lim_{x \to \infty} f(x) = 3$

$\left(-\dfrac{3}{7}\right) \cdot \left(\dfrac{a}{5}\right) = 3$

$-\dfrac{3a}{35} = 3$

$a = -35$

Answer: $-35$

</details>

---

### Q5. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\lim_{x \to \infty} \left(\sqrt[3]{x^3 + 6x^2 + 1} - x\right)$ is:

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $2$
- **(D)** $\infty$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

Let $L = \lim_{x \to \infty} \left(\sqrt[3]{x^3 + 6x^2 + 1} - x\right)$

Taking $x$ common from the cube root, we get:

$L = \lim_{x \to \infty} x \left( \left( 1 + \dfrac{6}{x} + \dfrac{1}{x^3} \right)^{1/3} - 1 \right)$

Using the binomial expansion $(1 + t)^n = 1 + nt + \dfrac{n(n-1)}{2!}t^2 + \dots$ for $|t| < 1$, where $t = \dfrac{6}{x} + \dfrac{1}{x^3}$ and $n = \dfrac{1}{3}$:

$L = \lim_{x \to \infty} x \left( 1 + \dfrac{1}{3} \left( \dfrac{6}{x} + \dfrac{1}{x^3} \right) + \dots - 1 \right)$

$L = \lim_{x \to \infty} x \left( \dfrac{2}{x} + \dfrac{1}{3x^3} + \dots \right)$

$L = \lim_{x \to \infty} \left( 2 + \dfrac{1}{3x^2} + \dots \right)$

As $x \to \infty$, the terms containing $\dfrac{1}{x}$ and higher powers approach zero.

$L = 2$

Answer: $2$

</details>

---

### Q6. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\lim\limits_{n \to \infty}\left[\dfrac{1}{1 - n^2} + \dfrac{2}{1 - n^2} + \ldots + \dfrac{n}{1 - n^2}\right]^3$ is

**Options:**

- **(A)** $8$
- **(B)** $-8$
- **(C)** $\dfrac{1}{8}$
- **(D)** $\dfrac{-1}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{-1}{8}$**

**Detailed Solution:**

Let $L = \lim\limits_{n \to \infty}\left[\dfrac{1}{1 - n^2} + \dfrac{2}{1 - n^2} + \ldots + \dfrac{n}{1 - n^2}\right]^3$

The expression inside the bracket can be simplified by taking the common denominator:

$S_n = \dfrac{1 + 2 + \ldots + n}{1 - n^2}$

Using the sum of the first $n$ natural numbers, $1 + 2 + \ldots + n = \dfrac{n(n+1)}{2}$:

$S_n = \dfrac{\dfrac{n(n+1)}{2}}{1 - n^2}$

$S_n = \dfrac{n(n+1)}{2(1 - n)(1 + n)}$

$S_n = \dfrac{n}{2(1 - n)}$

Taking the limit as $n \to \infty$:

$\lim\limits_{n \to \infty} S_n = \lim\limits_{n \to \infty} \dfrac{n}{2(1 - n)} = \lim\limits_{n \to \infty} \dfrac{1}{2\left(\dfrac{1}{n} - 1\right)} = -\dfrac{1}{2}$

Therefore, the required limit is:

$L = \left(-\dfrac{1}{2}\right)^3 = -\dfrac{1}{8}$

Answer: $\dfrac{-1}{8}$

</details>

---

### Q7. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x) = \dfrac{2\sqrt{2} - (\cos x + \sin x)^3}{1 - \sin 2x}$ is continuous at $x = \dfrac{\pi}{4}$, then the value of $f\left(\dfrac{\pi}{4}\right)$ is ...

**Options:**

- **(A)** $\dfrac{3\sqrt{2}}{2}$
- **(B)** $\dfrac{5\sqrt{2}}{2}$
- **(C)** $0$
- **(D)** $\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{3\sqrt{2}}{2}$**

**Detailed Solution:**

Since $f(x)$ is continuous at $x = \dfrac{\pi}{4}$, we have $f\left(\dfrac{\pi}{4}\right) = \lim_{x \to \pi/4} f(x)$.

Let $t = \cos x + \sin x$. As $x \to \dfrac{\pi}{4}$, $t \to \cos\left(\dfrac{\pi}{4}\right) + \sin\left(\dfrac{\pi}{4}\right) = \sqrt{2}$.

Squaring both sides, $t^2 = (\cos x + \sin x)^2 = \cos^2 x + \sin^2 x + 2\sin x \cos x = 1 + \sin 2x$.

This gives $\sin 2x = t^2 - 1$.

Substituting these into the limit:

$\lim_{x \to \pi/4} \dfrac{2\sqrt{2} - (\cos x + \sin x)^3}{1 - \sin 2x} = \lim_{t \to \sqrt{2}} \dfrac{2\sqrt{2} - t^3}{1 - (t^2 - 1)} = \lim_{t \to \sqrt{2}} \dfrac{2\sqrt{2} - t^3}{2 - t^2}$

This is a $\dfrac{0}{0}$ form. Applying L'Hopital's rule:

$\lim_{t \to \sqrt{2}} \dfrac{-3t^2}{-2t} = \lim_{t \to \sqrt{2}} \dfrac{3t}{2} = \dfrac{3\sqrt{2}}{2}$

Alternatively, by factorizing:

$\lim_{t \to \sqrt{2}} \dfrac{(\sqrt{2} - t)(2 + \sqrt{2}t + t^2)}{(\sqrt{2} - t)(\sqrt{2} + t)} = \lim_{t \to \sqrt{2}} \dfrac{2 + \sqrt{2}t + t^2}{\sqrt{2} + t} = \dfrac{2 + 2 + 2}{\sqrt{2} + \sqrt{2}} = \dfrac{6}{2\sqrt{2}} = \dfrac{3\sqrt{2}}{2}$

Thus, $f\left(\dfrac{\pi}{4}\right) = \dfrac{3\sqrt{2}}{2}$.

Answer: $\dfrac{3\sqrt{2}}{2}$

</details>

---

### Q8. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\lim\limits_{x \to k} \dfrac{x^3 - k^3}{x^2 - k^2} = \lim\limits_{x \to 0} \dfrac{1 - \cos(2x)}{x \sin x}$, then the value of $k$ is $\ldots$

**Options:**

- **(A)** $\dfrac{4}{3}$
- **(B)** $\dfrac{3}{4}$
- **(C)** $\dfrac{8}{3}$
- **(D)** $\dfrac{3}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{4}{3}$**

**Detailed Solution:**

Evaluating the left hand side limit:

$\lim\limits_{x \to k} \dfrac{x^3 - k^3}{x^2 - k^2} = \lim\limits_{x \to k} \dfrac{(x - k)(x^2 + xk + k^2)}{(x - k)(x + k)}$

$= \dfrac{k^2 + k^2 + k^2}{k + k} = \dfrac{3k^2}{2k} = \dfrac{3k}{2}$

Evaluating the right hand side limit:

$\lim\limits_{x \to 0} \dfrac{1 - \cos(2x)}{x \sin x} = \lim\limits_{x \to 0} \dfrac{2 \sin^2 x}{x \sin x}$

$= \lim\limits_{x \to 0} 2 \left(\dfrac{\sin x}{x}\right) = 2(1) = 2$

Equating both the limits:

$\dfrac{3k}{2} = 2$

$k = \dfrac{4}{3}$

Answer: $\dfrac{4}{3}$

</details>

---

### Q9. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\lim\limits_{x \to \infty}\left[\dfrac{x^2+x+1}{x+1} - ax - b\right] = 3$, then $a - b = $...

**Options:**

- **(A)** $2$
- **(B)** $3$
- **(C)** $-2$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4$**

**Detailed Solution:**

The given limit is $\lim\limits_{x \to \infty}\left[\dfrac{x^2+x+1}{x+1} - ax - b\right] = 3$

Taking the LCM, we get:

$\lim\limits_{x \to \infty}\left[\dfrac{x^2+x+1 - ax(x+1) - b(x+1)}{x+1}\right] = 3$

$\lim\limits_{x \to \infty}\left[\dfrac{(1-a)x^2 + (1-a-b)x + (1-b)}{x+1}\right] = 3$

For the limit to be finite as $x \to \infty$, the degree of the numerator must be less than or equal to the degree of the denominator. Therefore, the coefficient of $x^2$ in the numerator must be zero.

$1 - a = 0 \Rightarrow a = 1$

Substituting $a = 1$ in the limit expression:

$\lim\limits_{x \to \infty}\left[\dfrac{-bx + (1-b)}{x+1}\right] = 3$

Dividing the numerator and the denominator by $x$:

$\lim\limits_{x \to \infty}\left[\dfrac{-b + \dfrac{1-b}{x}}{1 + \dfrac{1}{x}}\right] = 3$

$-b = 3 \Rightarrow b = -3$

We need to find the value of $a - b$:

$a - b = 1 - (-3) = 4$

Answer: $4$

</details>

---

### Q10. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\lim\limits_{x \to 1} \dfrac{\sin(3x^2 - 4x + 1) - x^2 + 1}{2x^3 - 7x^2 + ax + b} = -2$, then the quadratic equation having roots $a$ and $b$ is

**Options:**

- **(A)** $x^2 + 5x - 24 = 0$
- **(B)** $x^2 - 5x + 24 = 0$
- **(C)** $x^2 - 5x - 24 = 0$
- **(D)** $x^2 + 5x + 24 = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x^2 - 5x - 24 = 0$**

**Detailed Solution:**

Given limit is $\lim\limits_{x \to 1} \dfrac{\sin(3x^2 - 4x + 1) - x^2 + 1}{2x^3 - 7x^2 + ax + b} = -2$

Let $N(x) = \sin(3x^2 - 4x + 1) - x^2 + 1$ and $D(x) = 2x^3 - 7x^2 + ax + b$.

As $x \to 1$, $N(1) = \sin(0) - 1 + 1 = 0$.

For the limit to exist and be finite, the denominator must also approach $0$ as $x \to 1$.

$D(1) = 2(1)^3 - 7(1)^2 + a(1) + b = 0 \Rightarrow a + b = 5$

Applying L'Hopital's rule, we differentiate the numerator and the denominator:

$N'(x) = (6x - 4)\cos(3x^2 - 4x + 1) - 2x$

$D'(x) = 6x^2 - 14x + a$

As $x \to 1$, $N'(1) = 2\cos(0) - 2 = 0$.

Since $N'(1) = 0$ and the limit is a non-zero finite value, $D'(1)$ must also be $0$.

$D'(1) = 6(1)^2 - 14(1) + a = 0 \Rightarrow a = 8$

Substituting $a = 8$ into $a + b = 5$, we get $b = -3$.

Applying L'Hopital's rule again to verify the limit:

$N''(x) = -(6x - 4)^2\sin(3x^2 - 4x + 1) + 6\cos(3x^2 - 4x + 1) - 2$

$D''(x) = 12x - 14$

$\lim\limits_{x \to 1} \dfrac{N''(x)}{D''(x)} = \dfrac{0 + 6 - 2}{12 - 14} = \dfrac{4}{-2} = -2$, which matches the given limit.

The roots of the required quadratic equation are $a = 8$ and $b = -3$.

The sum of the roots is $a + b = 5$.

The product of the roots is $ab = 8 \times (-3) = -24$.

The quadratic equation is $x^2 - (a + b)x + ab = 0$, which gives $x^2 - 5x - 24 = 0$.

Answer: $x^2 - 5x - 24 = 0$

</details>

---

### Q11. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\lim\limits_{x \to \infty} \dfrac{(2x-1)^{19} \cdot (3x+2)^{11}}{(6x-5)^{30}} = 2^a \cdot 3^b$, then $a + b =$

**Options:**

- **(A)** $-30$
- **(B)** $-11$
- **(C)** $-19$
- **(D)** $30$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-30$**

**Detailed Solution:**

$\lim\limits_{x \to \infty} \dfrac{(2x-1)^{19} \cdot (3x+2)^{11}}{(6x-5)^{30}}$

Dividing the numerator and the denominator by $x^{30}$:

$\lim\limits_{x \to \infty} \dfrac{\left(2 - \dfrac{1}{x}\right)^{19} \left(3 + \dfrac{2}{x}\right)^{11}}{\left(6 - \dfrac{5}{x}\right)^{30}}$

As $x \to \infty$, $\dfrac{1}{x} \to 0$. The limit evaluates to:

$\dfrac{2^{19} \cdot 3^{11}}{6^{30}}$

Substituting $6 = 2 \cdot 3$:

$\dfrac{2^{19} \cdot 3^{11}}{2^{30} \cdot 3^{30}} = 2^{19 - 30} \cdot 3^{11 - 30} = 2^{-11} \cdot 3^{-19}$

Comparing with $2^a \cdot 3^b$, we get $a = -11$ and $b = -19$.

Therefore, $a + b = -11 - 19 = -30$.

Answer: $-30$

</details>

---

### Q12. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\lim_{n\to\infty} \dfrac{(n+2)! + (n+1)!}{(n+2)! - (n+1)!}$ is ____

**Options:**

- **(A)** $-1$
- **(B)** $0$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

The given limit is $\lim_{n\to\infty} \dfrac{(n+2)! + (n+1)!}{(n+2)! - (n+1)!}$

Taking $(n+1)!$ common from both numerator and denominator:

$\lim_{n\to\infty} \dfrac{(n+1)![(n+2) + 1]}{(n+1)![(n+2) - 1]}$

Cancelling $(n+1)!$ from numerator and denominator:

$\lim_{n\to\infty} \dfrac{n+3}{n+1}$

Dividing numerator and denominator by $n$:

$\lim_{n\to\infty} \dfrac{1 + \dfrac{3}{n}}{1 + \dfrac{1}{n}}$

As $n \to \infty$, $\dfrac{1}{n} \to 0$. Substituting the limit:

$\dfrac{1 + 0}{1 + 0} = 1$

Answer: $1$

</details>

---

### Q13. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\lim_{x \to 0}\left[\dfrac{\log|2 + x| - \log|2 - x|}{\tan x}\right] = $ .......

**Options:**

- **(A)** $2$
- **(B)** $0$
- **(C)** $-1$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1$**

**Detailed Solution:**

As $x \to 0$, $2+x > 0$ and $2-x > 0$, so the absolute value signs can be removed:

$\lim_{x \to 0} \dfrac{\log(2 + x) - \log(2 - x)}{\tan x}$

This limit is of the form $\dfrac{0}{0}$. Applying L'Hospital's rule by differentiating the numerator and the denominator with respect to $x$:

$\lim_{x \to 0} \dfrac{\dfrac{1}{2 + x} - \dfrac{1}{2 - x}(-1)}{\sec^2 x}$

$= \lim_{x \to 0} \dfrac{\dfrac{1}{2 + x} + \dfrac{1}{2 - x}}{\sec^2 x}$

Substituting $x = 0$:

$= \dfrac{\dfrac{1}{2} + \dfrac{1}{2}}{1} = 1$

Answer: $1$

</details>

---

### Q14. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\lim_{x \to 1} \left[\dfrac{x-2}{x^2-x} - \dfrac{1}{x^3 - 3x^2 + 2x}\right] = $

**Options:**

- **(A)** $3$
- **(B)** $4$
- **(C)** $2$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

The given limit is $\lim_{x \to 1} \left[\dfrac{x-2}{x^2-x} - \dfrac{1}{x^3 - 3x^2 + 2x}\right]$

Factorizing the denominators, we get:

$= \lim_{x \to 1} \left[\dfrac{x-2}{x(x-1)} - \dfrac{1}{x(x-1)(x-2)}\right]$

Taking the common denominator $x(x-1)(x-2)$:

$= \lim_{x \to 1} \left[\dfrac{(x-2)^2 - 1}{x(x-1)(x-2)}\right]$

Expanding the numerator:

$= \lim_{x \to 1} \left[\dfrac{x^2 - 4x + 4 - 1}{x(x-1)(x-2)}\right]$

$= \lim_{x \to 1} \left[\dfrac{x^2 - 4x + 3}{x(x-1)(x-2)}\right]$

Factorizing the numerator:

$= \lim_{x \to 1} \left[\dfrac{(x-1)(x-3)}{x(x-1)(x-2)}\right]$

Canceling the common factor $(x-1)$ since $x \to 1$ implies $x \neq 1$:

$= \lim_{x \to 1} \dfrac{x-3}{x(x-2)}$

Substituting $x = 1$ into the simplified expression:

$= \dfrac{1-3}{1(1-2)} = \dfrac{-2}{-1} = 2$

Answer: $2$

</details>

---

### Q15. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\left\{\begin{array}{cc}\frac{9^x-2 \cdot 3^x+1}{\log (1+3 x) \cdot \tan 2 x} & , \text { if } x \neq 0 \\ \mathrm{a}(\log \mathrm{b})^{\mathrm{c}} & , \text { if } x=0\end{array}\right.$ is continuous at $x=0$, then $\mathrm{a}+\mathrm{b}+\mathrm{c}=$

**Options:**

- **(A)** $\frac{31}{6}$
- **(B)** $\frac{1}{6}$
- **(C)** $\frac{5}{6}$
- **(D)** $\frac{3}{20}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{31}{6}$**

**Detailed Solution:**

Since the function $f(x)$ is continuous at $x=0$, we have:

$\lim_{x \to 0} f(x) = f(0)$

$\lim_{x \to 0} \dfrac{9^x - 2 \cdot 3^x + 1}{\log(1+3x) \cdot \tan 2x} = a(\log b)^c$

The numerator can be written as a perfect square:

$9^x - 2 \cdot 3^x + 1 = (3^x)^2 - 2 \cdot 3^x + 1 = (3^x - 1)^2$

Now, divide the numerator and the denominator by $x^2$:

$\lim_{x \to 0} \dfrac{\left(\dfrac{3^x - 1}{x}\right)^2}{\left(\dfrac{\log(1+3x)}{x}\right) \cdot \left(\dfrac{\tan 2x}{x}\right)} = a(\log b)^c$

Using the standard limits $\lim_{x \to 0} \dfrac{k^x - 1}{x} = \log k$, $\lim_{x \to 0} \dfrac{\log(1+kx)}{x} = k$, and $\lim_{x \to 0} \dfrac{\tan kx}{x} = k$, we get:

$\dfrac{(\log 3)^2}{3 \cdot 2} = a(\log b)^c$

$\dfrac{1}{6}(\log 3)^2 = a(\log b)^c$

Comparing both sides, we get:

$a = \dfrac{1}{6}$, $b = 3$, $c = 2$

Therefore, the value of $a + b + c$ is:

$a + b + c = \dfrac{1}{6} + 3 + 2 = \dfrac{1}{6} + 5 = \dfrac{31}{6}$

Answer: $\frac{31}{6}$

</details>

---

### Q16. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 0} \frac{\mathrm{e}^{x^2}-\cos 3 x}{\sin x \log (1+2 x)}=$

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** $\frac{-3}{2}$
- **(C)** $\frac{11}{4}$
- **(D)** $\frac{-11}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{11}{4}$**

**Detailed Solution:**

Divide the numerator and the denominator by $x^2$:

$\lim_{x \rightarrow 0} \dfrac{\dfrac{e^{x^2} - \cos 3x}{x^2}}{\dfrac{\sin x}{x} \cdot \dfrac{\log(1+2x)}{x}}$

Rewrite the numerator by adding and subtracting $1$:

$\lim_{x \rightarrow 0} \dfrac{\dfrac{e^{x^2} - 1}{x^2} + \dfrac{1 - \cos 3x}{x^2}}{\dfrac{\sin x}{x} \cdot \dfrac{\log(1+2x)}{2x} \cdot 2}$

Using standard limits $\lim_{x \rightarrow 0} \dfrac{e^x - 1}{x} = 1$, $\lim_{x \rightarrow 0} \dfrac{1 - \cos ax}{x^2} = \dfrac{a^2}{2}$, $\lim_{x \rightarrow 0} \dfrac{\sin x}{x} = 1$, and $\lim_{x \rightarrow 0} \dfrac{\log(1+x)}{x} = 1$:

Numerator limit: $\lim_{x \rightarrow 0} \dfrac{e^{x^2} - 1}{x^2} + \lim_{x \rightarrow 0} \dfrac{1 - \cos 3x}{x^2} = 1 + \dfrac{3^2}{2} = 1 + \dfrac{9}{2} = \dfrac{11}{2}$

Denominator limit: $\lim_{x \rightarrow 0} \dfrac{\sin x}{x} \cdot \lim_{x \rightarrow 0} \dfrac{\log(1+2x)}{2x} \cdot 2 = 1 \cdot 1 \cdot 2 = 2$

Dividing the limits, we get:

$\dfrac{\dfrac{11}{2}}{2} = \dfrac{11}{4}$

Answer: $\frac{11}{4}$

</details>

---

### Q17. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow \infty} \frac{(2 x+1)^{50}+(2 x+2)^{50}+(2 x+3)^{50}+\cdots \cdots+(2 x+100)^{50}}{(2 x)^{50}+(10)^{50}}=\cdots$

**Options:**

- **(A)** 50
- **(B)** 100
- **(C)** 25
- **(D)** 200

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 100**

**Detailed Solution:**

Divide the numerator and the denominator by $(2x)^{50}$ to get:

$\lim _{x \rightarrow \infty} \dfrac{\left(1+\dfrac{1}{2 x}\right)^{50}+\left(1+\dfrac{2}{2 x}\right)^{50}+\cdots+\left(1+\dfrac{100}{2 x}\right)^{50}}{1+\left(\dfrac{10}{2 x}\right)^{50}}$

As $x \rightarrow \infty$, the terms $\dfrac{1}{2x}, \dfrac{2}{2x}, \dots, \dfrac{100}{2x}$ and $\dfrac{10}{2x}$ all approach $0$.

Substituting these limits into the expression, each of the $100$ terms in the numerator approaches $1^{50} = 1$.

The denominator approaches $1 + 0 = 1$.

Therefore, the limit evaluates to:

$\dfrac{1 + 1 + \cdots + 1 \text{ (100 times)}}{1} = \dfrac{100}{1} = 100$

Answer: 100

</details>

---

### Q18. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 0} \frac{63^x-9^x-7^x+1}{\sqrt{2}-\sqrt{1+\cos x}}=\ldots$.

**Options:**

- **(A)** $\frac{4 \sqrt{2}}{\log 7 \cdot \log 9}$
- **(B)** $4 \sqrt{2} \log 7 \cdot \log 9$
- **(C)** $4 \sqrt{2} \log 63$
- **(D)** $\frac{\log 7 \cdot \log 9}{4 \sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4 \sqrt{2} \log 7 \cdot \log 9$**

**Detailed Solution:**

The given limit is $\lim_{x \rightarrow 0} \dfrac{63^x-9^x-7^x+1}{\sqrt{2}-\sqrt{1+\cos x}}$.

Factorizing the numerator:
$63^x - 9^x - 7^x + 1 = 9^x \cdot 7^x - 9^x - 7^x + 1 = (9^x - 1)(7^x - 1)$

Rationalizing the denominator by multiplying the numerator and the denominator by $\sqrt{2} + \sqrt{1 + \cos x}$:
$\lim_{x \rightarrow 0} \dfrac{(9^x - 1)(7^x - 1)(\sqrt{2} + \sqrt{1 + \cos x})}{2 - (1 + \cos x)}$

$= \lim_{x \rightarrow 0} \dfrac{(9^x - 1)(7^x - 1)(\sqrt{2} + \sqrt{1 + \cos x})}{1 - \cos x}$

Dividing the numerator and the denominator by $x^2$:
$= \lim_{x \rightarrow 0} \dfrac{\dfrac{9^x - 1}{x} \cdot \dfrac{7^x - 1}{x} \cdot (\sqrt{2} + \sqrt{1 + \cos x})}{\dfrac{1 - \cos x}{x^2}}$

Using the standard limits $\lim_{x \rightarrow 0} \dfrac{a^x - 1}{x} = \log a$ and $\lim_{x \rightarrow 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2}$:
$= \dfrac{\log 9 \cdot \log 7 \cdot (\sqrt{2} + \sqrt{1 + 1})}{\dfrac{1}{2}}$

$= \dfrac{\log 9 \cdot \log 7 \cdot 2\sqrt{2}}{\dfrac{1}{2}}$

$= 4\sqrt{2} \log 7 \cdot \log 9$

Answer: $4 \sqrt{2} \log 7 \cdot \log 9$

</details>

---

### Q19. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 5^-} \frac{\sqrt{2-2 \cos \left(x^2-12 x+35\right)}}{(x-5)}=\ldots \ldots$

**Options:**

- **(A)** $\frac{2}{-5}$
- **(B)** $-2$
- **(C)** $\frac{-1}{2}$
- **(D)** $-5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-2$**

**Detailed Solution:**

Given limit is $\lim_{x \to 5^-} \dfrac{\sqrt{2-2 \cos(x^2-12x+35)}}{x-5}$

Using the half-angle formula $1 - \cos \theta = 2 \sin^2\left(\dfrac{\theta}{2}\right)$, we get:

$\lim_{x \to 5^-} \dfrac{\sqrt{4 \sin^2\left(\dfrac{x^2-12x+35}{2}\right)}}{x-5}$

$\lim_{x \to 5^-} \dfrac{2 \left| \sin\left(\dfrac{(x-5)(x-7)}{2}\right) \right|}{x-5}$

As $x \to 5^-$, $x < 5$. Therefore, $x-5 < 0$ and $x-7 < 0$.

This implies $(x-5)(x-7) > 0$, so for values of $x$ close to $5$, $\dfrac{(x-5)(x-7)}{2}$ is a small positive angle, and its sine is positive.

Thus, $\left| \sin\left(\dfrac{(x-5)(x-7)}{2}\right) \right| = \sin\left(\dfrac{(x-5)(x-7)}{2}\right)$.

The limit becomes:

$\lim_{x \to 5^-} \dfrac{2 \sin\left(\dfrac{(x-5)(x-7)}{2}\right)}{x-5}$

Multiply and divide by $\dfrac{x-7}{2}$:

$\lim_{x \to 5^-} 2 \left[ \dfrac{\sin\left(\dfrac{(x-5)(x-7)}{2}\right)}{\dfrac{(x-5)(x-7)}{2}} \right] \times \left( \dfrac{x-7}{2} \right)$

Using the standard limit $\lim_{\theta \to 0} \dfrac{\sin \theta}{\theta} = 1$, we get:

$2 \times 1 \times \left( \dfrac{5-7}{2} \right) = 2 \times \left( \dfrac{-2}{2} \right) = -2$

Answer: $-2$

</details>

---

### Q20. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\frac{\sin \left(\pi \cos ^2 x\right)}{3 x^2}, x \neq 0$ is continuous at $x=0$ then $\mathrm{f}(0)=$

**Options:**

- **(A)** 0
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{-\pi}{3}$
- **(D)** $\frac{3}{\pi}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{3}$**

**Detailed Solution:**

Since $\mathrm{f}(x)$ is continuous at $x=0$, we have $\mathrm{f}(0) = \lim_{x \to 0} \mathrm{f}(x)$.

$\mathrm{f}(0) = \lim_{x \to 0} \dfrac{\sin(\pi \cos^2 x)}{3x^2}$

Using the identity $\cos^2 x = 1 - \sin^2 x$, we get:

$\mathrm{f}(0) = \lim_{x \to 0} \dfrac{\sin(\pi(1 - \sin^2 x))}{3x^2}$

$\mathrm{f}(0) = \lim_{x \to 0} \dfrac{\sin(\pi - \pi \sin^2 x)}{3x^2}$

Since $\sin(\pi - \theta) = \sin \theta$, this becomes:

$\mathrm{f}(0) = \lim_{x \to 0} \dfrac{\sin(\pi \sin^2 x)}{3x^2}$

Multiplying and dividing by $\pi \sin^2 x$:

$\mathrm{f}(0) = \lim_{x \to 0} \left[ \dfrac{\sin(\pi \sin^2 x)}{\pi \sin^2 x} \times \dfrac{\pi \sin^2 x}{3x^2} \right]$

As $x \to 0$, $\pi \sin^2 x \to 0$. Using the standard limit $\lim_{\theta \to 0} \dfrac{\sin \theta}{\theta} = 1$:

$\mathrm{f}(0) = 1 \times \dfrac{\pi}{3} \lim_{x \to 0} \left( \dfrac{\sin x}{x} \right)^2$

$\mathrm{f}(0) = \dfrac{\pi}{3} \times (1)^2 = \dfrac{\pi}{3}$

Answer: $\frac{\pi}{3}$

</details>

---

### Q21. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\frac{10^x+7^x-14^x-5^x}{1-\cos x}, x \neq 0$ is continuous at $x=0$, then the value of $f(0)$ is

**Options:**

- **(A)** $\log 2\left[\log \left(\frac{5}{7}\right)\right]$
- **(B)** $\log 4\left[\log \left(\frac{5}{7}\right)\right]$
- **(C)** $\log 2\left[\log \left(\frac{7}{5}\right)\right]$
- **(D)** $\log 4\left[\log \left(\frac{7}{5}\right)\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log 4\left[\log \left(\frac{5}{7}\right)\right]$**

**Detailed Solution:**

Since the function is continuous at $x=0$, we have $f(0) = \lim_{x \to 0} f(x)$.

$\lim_{x \to 0} \dfrac{10^x + 7^x - 14^x - 5^x}{1 - \cos x}$

Factorizing the numerator:

$10^x + 7^x - 14^x - 5^x = 2^x 5^x - 5^x - 2^x 7^x + 7^x$

$= 5^x(2^x - 1) - 7^x(2^x - 1)$

$= (5^x - 7^x)(2^x - 1)$

Substituting this back into the limit and dividing the numerator and the denominator by $x^2$:

$\lim_{x \to 0} \dfrac{\dfrac{5^x - 7^x}{x} \cdot \dfrac{2^x - 1}{x}}{\dfrac{1 - \cos x}{x^2}}$

Using the standard limits $\lim_{x \to 0} \dfrac{a^x - 1}{x} = \log a$ and $\lim_{x \to 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2}$:

$\lim_{x \to 0} \dfrac{5^x - 7^x}{x} = \lim_{x \to 0} \dfrac{(5^x - 1) - (7^x - 1)}{x} = \log 5 - \log 7 = \log\left(\dfrac{5}{7}\right)$

$\lim_{x \to 0} \dfrac{2^x - 1}{x} = \log 2$

Therefore, the limit evaluates to:

$f(0) = \dfrac{\log\left(\dfrac{5}{7}\right) \cdot \log 2}{\dfrac{1}{2}}$

$f(0) = 2 \log 2 \left[ \log\left(\dfrac{5}{7}\right) \right]$

$f(0) = \log(2^2) \left[ \log\left(\dfrac{5}{7}\right) \right] = \log 4 \left[ \log\left(\dfrac{5}{7}\right) \right]$

Answer: $\log 4\left[\log \left(\frac{5}{7}\right)\right]$

</details>

---

### Q22. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 2} \frac{x+3 x^2+5 x^3+7 x^4-166}{x-2}=$

**Options:**

- **(A)** 167
- **(B)** 267
- **(C)** 287
- **(D)** 297

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 297**

**Detailed Solution:**

Let $L = \lim_{x \rightarrow 2} \dfrac{x+3 x^2+5 x^3+7 x^4-166}{x-2}$

Substituting $x = 2$ gives $\dfrac{0}{0}$ form.

Applying L'Hospital's rule, we differentiate the numerator and the denominator with respect to $x$:

$L = \lim_{x \rightarrow 2} \dfrac{\dfrac{d}{dx}(x+3 x^2+5 x^3+7 x^4-166)}{\dfrac{d}{dx}(x-2)}$

$L = \lim_{x \rightarrow 2} \dfrac{1 + 6x + 15x^2 + 28x^3}{1}$

Substituting $x = 2$:

$L = 1 + 6(2) + 15(2)^2 + 28(2)^3$

$L = 1 + 12 + 15(4) + 28(8)$

$L = 1 + 12 + 60 + 224$

$L = 297$

Answer: 297

</details>

---

### Q23. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)= \begin{cases}\frac{8^x-4^x-2^x+1^x}{x^2} & , \text { if } x>0 \\ \mathrm{e}^x \sin x+i x+\lambda \log 4 & , \text { if } x \leqslant 0, i \in \mathbb{R}\end{cases}$
is continuous at $x=0$, then the value of $500 e^\lambda$ is

**Options:**

- **(A)** $1000$
- **(B)** $2000$
- **(C)** $4000$
- **(D)** $3000$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1000$**

**Detailed Solution:**

For $x > 0$, the function is $f(x) = \dfrac{8^x - 4^x - 2^x + 1^x}{x^2} = \dfrac{8^x - 4^x - 2^x + 1}{x^2}$.

The right-hand limit at $x = 0$ is:

$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \dfrac{4^x(2^x - 1) - 1(2^x - 1)}{x^2}$

$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \dfrac{(4^x - 1)(2^x - 1)}{x^2}$

$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \left( \dfrac{4^x - 1}{x} \right) \left( \dfrac{2^x - 1}{x} \right) = (\log 4)(\log 2)$

For $x \leqslant 0$, the function is $f(x) = e^x \sin x + ix + \lambda \log 4$.

The left-hand limit at $x = 0$ is:

$\lim_{x \to 0^-} f(x) = e^0 \sin 0 + i(0) + \lambda \log 4 = \lambda \log 4$

Since $f(x)$ is continuous at $x = 0$, the left-hand limit and right-hand limit must be equal:

$\lambda \log 4 = (\log 4)(\log 2)$

$\lambda = \log 2$

The value of $500 e^\lambda$ is:

$500 e^{\log 2} = 500 \times 2 = 1000$

Answer: $1000$

</details>

---

### Q24. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow \infty} \frac{\mathrm{e}^{x^4}-1}{\mathrm{e}^{x^4}+1}=$

**Options:**

- **(A)** $1$
- **(B)** e
- **(C)** $\frac{1}{\mathrm{e}}$
- **(D)** not defined

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

Let $L = \lim_{x \rightarrow \infty} \dfrac{\mathrm{e}^{x^4}-1}{\mathrm{e}^{x^4}+1}$

Dividing the numerator and the denominator by $\mathrm{e}^{x^4}$:

$L = \lim_{x \rightarrow \infty} \dfrac{1 - \dfrac{1}{\mathrm{e}^{x^4}}}{1 + \dfrac{1}{\mathrm{e}^{x^4}}}$

As $x \rightarrow \infty$, $x^4 \rightarrow \infty$, which implies $\mathrm{e}^{x^4} \rightarrow \infty$ and $\dfrac{1}{\mathrm{e}^{x^4}} \rightarrow 0$.

Substituting this in the limit expression:

$L = \dfrac{1 - 0}{1 + 0} = 1$

Answer: $1$

</details>

---

### Q25. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\lim _{x \rightarrow 0} \frac{\left(7^x-1\right)^4}{\tan \left(\frac{x}{\mathrm{k}}\right) \cdot \log \left(1+\frac{x^2}{3}\right) \cdot \sin 4 x}=3(\log 7)^3$, then $\mathrm{k}=$

**Options:**

- **(A)** $4(\log 7)^{-1}$
- **(B)** $\frac{1}{4}(\log 7)^{-1}$
- **(C)** $4 \log \left(\frac{1}{7}\right)$
- **(D)** $\frac{1}{4} \log 7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4(\log 7)^{-1}$**

**Detailed Solution:**

The given limit is:

$\lim _{x \rightarrow 0} \dfrac{\left(7^x-1\right)^4}{\tan \left(\dfrac{x}{\mathrm{k}}\right) \cdot \log \left(1+\dfrac{x^2}{3}\right) \cdot \sin 4 x} = 3(\log 7)^3$

Dividing the numerator and the denominator by $x^4$, we get:

$\lim _{x \rightarrow 0} \dfrac{\left(\dfrac{7^x-1}{x}\right)^4}{\left(\dfrac{\tan (x/\mathrm{k})}{x}\right) \cdot \left(\dfrac{\log (1+x^2/3)}{x^2}\right) \cdot \left(\dfrac{\sin 4 x}{x}\right)}$

Using standard limits $\lim _{x \rightarrow 0} \dfrac{a^x-1}{x} = \log a$, $\lim _{x \rightarrow 0} \dfrac{\tan \theta}{\theta} = 1$, $\lim _{x \rightarrow 0} \dfrac{\log(1+x)}{x} = 1$, and $\lim _{x \rightarrow 0} \dfrac{\sin \theta}{\theta} = 1$:

Numerator limit: $\lim _{x \rightarrow 0} \left(\dfrac{7^x-1}{x}\right)^4 = (\log 7)^4$

Denominator limit:

$\lim _{x \rightarrow 0} \dfrac{\tan (x/\mathrm{k})}{x/\mathrm{k}} \cdot \dfrac{1}{\mathrm{k}} = \dfrac{1}{\mathrm{k}}$

$\lim _{x \rightarrow 0} \dfrac{\log (1+x^2/3)}{x^2/3} \cdot \dfrac{1}{3} = \dfrac{1}{3}$

$\lim _{x \rightarrow 0} \dfrac{\sin 4 x}{4 x} \cdot 4 = 4$

The limit of the denominator is $\dfrac{1}{\mathrm{k}} \cdot \dfrac{1}{3} \cdot 4 = \dfrac{4}{3\mathrm{k}}$

Substituting these back into the expression:

$\dfrac{(\log 7)^4}{\dfrac{4}{3\mathrm{k}}} = \dfrac{3\mathrm{k}(\log 7)^4}{4}$

Equating this to the given value:

$\dfrac{3\mathrm{k}(\log 7)^4}{4} = 3(\log 7)^3$

$\dfrac{\mathrm{k} \log 7}{4} = 1$

$\mathrm{k} = \dfrac{4}{\log 7} = 4(\log 7)^{-1}$

Answer: $4(\log 7)^{-1}$

</details>

---

### Q26. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 0} \frac{\mathrm{e}^{\tan x}-\mathrm{e}^x}{\tan x-x}=$

**Options:**

- **(A)** $1$
- **(B)** $0$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

Given limit is $\lim_{x \rightarrow 0} \dfrac{e^{\tan x} - e^x}{\tan x - x}$

Taking $e^x$ common in the numerator:

$= \lim_{x \rightarrow 0} \dfrac{e^x (e^{\tan x - x} - 1)}{\tan x - x}$

$= \lim_{x \rightarrow 0} e^x \times \lim_{x \rightarrow 0} \dfrac{e^{\tan x - x} - 1}{\tan x - x}$

Since $\tan x - x \rightarrow 0$ as $x \rightarrow 0$, we use the standard limit $\lim_{t \rightarrow 0} \dfrac{e^t - 1}{t} = 1$.

$= e^0 \times 1$

$= 1$

Answer: $1$

</details>

---

### Q27. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\frac{(27-2 x)^{\frac{1}{3}}-3}{9-3(243+5 x)^{\frac{1}{5}}}, x \neq 0$ is continuous at $x=0$, then the value of $f(0)$ is

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $6$
- **(C)** $2$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

Since $f(x)$ is continuous at $x=0$, $f(0) = \lim_{x \to 0} f(x)$.

$f(0) = \lim_{x \to 0} \dfrac{(27-2x)^{1/3} - 3}{9 - 3(243+5x)^{1/5}}$

This is a $\dfrac{0}{0}$ form. Applying L'Hospital's rule, we differentiate the numerator and the denominator with respect to $x$:

$f(0) = \lim_{x \to 0} \dfrac{\dfrac{1}{3}(27-2x)^{-2/3}(-2)}{-3 \times \dfrac{1}{5}(243+5x)^{-4/5}(5)}$

$f(0) = \lim_{x \to 0} \dfrac{-\dfrac{2}{3}(27-2x)^{-2/3}}{-3(243+5x)^{-4/5}}$

Substituting $x=0$:

$f(0) = \dfrac{-\dfrac{2}{3}(27)^{-2/3}}{-3(243)^{-4/5}}$

Using $27 = 3^3$ and $243 = 3^5$:

$f(0) = \dfrac{-\dfrac{2}{3} \times (3^3)^{-2/3}}{-3 \times (3^5)^{-4/5}}$

$f(0) = \dfrac{-\dfrac{2}{3} \times 3^{-2}}{-3 \times 3^{-4}}$

$f(0) = \dfrac{-\dfrac{2}{3} \times \dfrac{1}{9}}{-3 \times \dfrac{1}{81}}$

$f(0) = \dfrac{-\dfrac{2}{27}}{-\dfrac{1}{27}} = 2$

Answer: $2$

</details>

---

### Q28. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 3} \frac{(84-x)^{\frac{1}{4}}-3}{x-3}$ is

**Options:**

- **(A)** $\frac{-1}{108}$
- **(B)** $\frac{-1}{84}$
- **(C)** $\frac{-1}{27}$
- **(D)** $\frac{-1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-1}{108}$**

**Detailed Solution:**

Let $L = \lim_{x \rightarrow 3} \dfrac{(84-x)^{\dfrac{1}{4}}-3}{x-3}$

Let $y = 84 - x$. As $x \rightarrow 3$, $y \rightarrow 81$.

Also, $x - 3 = 81 - y = -(y - 81)$.

Substituting these in the limit, we get:

$L = \lim_{y \rightarrow 81} \dfrac{y^{\dfrac{1}{4}} - 81^{\dfrac{1}{4}}}{-(y - 81)}$

$L = - \lim_{y \rightarrow 81} \dfrac{y^{\dfrac{1}{4}} - 81^{\dfrac{1}{4}}}{y - 81}$

Using the standard limit $\lim_{x \rightarrow a} \dfrac{x^n - a^n}{x - a} = n a^{n-1}$:

$L = - \dfrac{1}{4} (81)^{\dfrac{1}{4} - 1}$

$L = - \dfrac{1}{4} (81)^{-\dfrac{3}{4}}$

$L = - \dfrac{1}{4} (3^4)^{-\dfrac{3}{4}}$

$L = - \dfrac{1}{4} \times 3^{-3} = - \dfrac{1}{4} \times \dfrac{1}{27} = \dfrac{-1}{108}$

Answer: $\frac{-1}{108}$

</details>

---

### Q29. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{y \rightarrow 0} \frac{\sqrt{1+\sqrt{1+y^4}}-\sqrt{2}}{y^4}=$

**Options:**

- **(A)** 0
- **(B)** $\frac{1}{2 \sqrt{2}}$
- **(C)** $\frac{1}{4 \sqrt{2}}$
- **(D)** $\frac{1}{2 \sqrt{2}(\sqrt{2}+1)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{4 \sqrt{2}}$**

**Detailed Solution:**

Rationalizing the numerator by multiplying and dividing by $\sqrt{1+\sqrt{1+y^4}}+\sqrt{2}$:

$\lim_{y \rightarrow 0} \dfrac{\sqrt{1+\sqrt{1+y^4}}-\sqrt{2}}{y^4}$

$= \lim_{y \rightarrow 0} \dfrac{(\sqrt{1+\sqrt{1+y^4}}-\sqrt{2})(\sqrt{1+\sqrt{1+y^4}}+\sqrt{2})}{y^4(\sqrt{1+\sqrt{1+y^4}}+\sqrt{2})}$

$= \lim_{y \rightarrow 0} \dfrac{1+\sqrt{1+y^4}-2}{y^4(\sqrt{1+\sqrt{1+y^4}}+\sqrt{2})}$

$= \lim_{y \rightarrow 0} \dfrac{\sqrt{1+y^4}-1}{y^4(\sqrt{1+\sqrt{1+y^4}}+\sqrt{2})}$

Rationalizing the numerator again by multiplying and dividing by $\sqrt{1+y^4}+1$:

$= \lim_{y \rightarrow 0} \dfrac{(\sqrt{1+y^4}-1)(\sqrt{1+y^4}+1)}{y^4(\sqrt{1+\sqrt{1+y^4}}+\sqrt{2})(\sqrt{1+y^4}+1)}$

$= \lim_{y \rightarrow 0} \dfrac{1+y^4-1}{y^4(\sqrt{1+\sqrt{1+y^4}}+\sqrt{2})(\sqrt{1+y^4}+1)}$

$= \lim_{y \rightarrow 0} \dfrac{y^4}{y^4(\sqrt{1+\sqrt{1+y^4}}+\sqrt{2})(\sqrt{1+y^4}+1)}$

$= \lim_{y \rightarrow 0} \dfrac{1}{(\sqrt{1+\sqrt{1+y^4}}+\sqrt{2})(\sqrt{1+y^4}+1)}$

Substituting $y = 0$:

$= \dfrac{1}{(\sqrt{1+\sqrt{1+0}}+\sqrt{2})(\sqrt{1+0}+1)}$

$= \dfrac{1}{(\sqrt{2}+\sqrt{2})(1+1)}$

$= \dfrac{1}{(2\sqrt{2})(2)}$

$= \dfrac{1}{4\sqrt{2}}$

Answer: $\frac{1}{4 \sqrt{2}}$

</details>

---

### Q30. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\lim _{x \rightarrow 0}\left((\sin x)^{\frac{1}{x}}+\left(\frac{1}{x}\right)^{\sin x}\right)$, where $x\gt0$ is

**Options:**

- **(A)** 0
- **(B)** -1
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

Let the given limit be $L = L_1 + L_2$, where $L_1 = \lim_{x \rightarrow 0^+} (\sin x)^{\dfrac{1}{x}}$ and $L_2 = \lim_{x \rightarrow 0^+} \left(\dfrac{1}{x}\right)^{\sin x}$.

For $L_1$, as $x \rightarrow 0^+$, $\sin x \rightarrow 0^+$ and $\dfrac{1}{x} \rightarrow \infty$.

Thus, $L_1$ is of the form $0^{\infty}$, which evaluates to $0$. So, $L_1 = 0$.

For $L_2$, let $y = \left(\dfrac{1}{x}\right)^{\sin x}$. Taking the natural logarithm on both sides:

$\ln y = \sin x \ln\left(\dfrac{1}{x}\right) = -\sin x \ln x$

Taking the limit as $x \rightarrow 0^+$:

$\lim_{x \rightarrow 0^+} \ln y = \lim_{x \rightarrow 0^+} \left( -\dfrac{\sin x}{x} \cdot x \ln x \right)$

We know that $\lim_{x \rightarrow 0^+} \dfrac{\sin x}{x} = 1$ and $\lim_{x \rightarrow 0^+} x \ln x = 0$.

$\lim_{x \rightarrow 0^+} \ln y = -1 \times 0 = 0$

Therefore, $L_2 = \lim_{x \rightarrow 0^+} y = e^0 = 1$.

The required limit is $L = L_1 + L_2 = 0 + 1 = 1$.

Answer: 1

</details>

---

### Q31. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 2} \frac{3^x+3^{3-x}-12}{3^{3-x}-3^{\frac{x}{2}}}=$

**Options:**

- **(A)** $-\frac{4}{3}$
- **(B)** $\frac{4}{3}$
- **(C)** $\frac{2}{3}$
- **(D)** $-\frac{4}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\frac{4}{3}$**

**Detailed Solution:**

Let $3^{\dfrac{x}{2}} = t$. As $x \rightarrow 2$, $t \rightarrow 3$.

The given limit can be rewritten in terms of $t$ as:

$\lim_{t \rightarrow 3} \dfrac{t^2 + \dfrac{27}{t^2} - 12}{\dfrac{27}{t^2} - t}$

Multiplying the numerator and the denominator by $t^2$, we get:

$\lim_{t \rightarrow 3} \dfrac{t^4 - 12t^2 + 27}{27 - t^3}$

Factorizing the numerator and the denominator:

$\lim_{t \rightarrow 3} \dfrac{(t^2 - 9)(t^2 - 3)}{(3 - t)(9 + 3t + t^2)}$

$\lim_{t \rightarrow 3} \dfrac{(t - 3)(t + 3)(t^2 - 3)}{-(t - 3)(t^2 + 3t + 9)}$

Canceling the common factor $(t - 3)$ since $t \neq 3$:

$\lim_{t \rightarrow 3} \dfrac{(t + 3)(t^2 - 3)}{-(t^2 + 3t + 9)}$

Substituting $t = 3$ into the simplified expression:

$\dfrac{(3 + 3)(3^2 - 3)}{-(3^2 + 3(3) + 9)}$

$\dfrac{6 \times 6}{-27} = -\dfrac{36}{27} = -\dfrac{4}{3}$

Answer: $-\frac{4}{3}$

</details>

---

### Q32. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\lim _{x \rightarrow 2}\left(\frac{5^x+5^{3-x}-30}{5^{3-x}-5^{\frac{x}{2}}}\right)=$

**Options:**

- **(A)** $\frac{-16}{3}$
- **(B)** $\frac{8}{3}$
- **(C)** $\frac{-8}{3}$
- **(D)** $\frac{16}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-8}{3}$**

**Detailed Solution:**

Let $5^{\dfrac{x}{2}} = t$. As $x \rightarrow 2$, $t \rightarrow 5$.

The given limit can be rewritten in terms of $t$ as:

$\lim_{t \rightarrow 5} \dfrac{t^2 + \dfrac{125}{t^2} - 30}{\dfrac{125}{t^2} - t}$

Multiplying the numerator and the denominator by $t^2$, we get:

$\lim_{t \rightarrow 5} \dfrac{t^4 - 30t^2 + 125}{125 - t^3}$

Factorizing the numerator and the denominator:

$\lim_{t \rightarrow 5} \dfrac{(t^2 - 25)(t^2 - 5)}{-(t^3 - 125)}$

$\lim_{t \rightarrow 5} \dfrac{(t - 5)(t + 5)(t^2 - 5)}{-(t - 5)(t^2 + 5t + 25)}$

Cancelling the common factor $(t - 5)$ since $t \neq 5$:

$\lim_{t \rightarrow 5} \dfrac{(t + 5)(t^2 - 5)}{-(t^2 + 5t + 25)}$

Substituting $t = 5$ into the simplified expression:

$\dfrac{(5 + 5)(5^2 - 5)}{-(5^2 + 5(5) + 25)}$

$\dfrac{10 \times 20}{-(25 + 25 + 25)}$

$\dfrac{200}{-75} = \dfrac{-8}{3}$

Answer: $\frac{-8}{3}$

</details>

---

### Q33. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \dfrac{9^x-4^x}{x\left(9^x+4^x\right)}=$

**Options:**

- **(A)** $\quad \log \left(\dfrac{3}{2}\right)$
- **(B)** $\dfrac{1}{2} \log \left(\dfrac{3}{2}\right)$
- **(C)** $\quad 2 \log \left(\dfrac{3}{2}\right)$
- **(D)** $2 \log \left(\dfrac{9}{4}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\quad \log \left(\dfrac{3}{2}\right)$**

**Detailed Solution:**

$\lim_{x \rightarrow 0} \dfrac{9^x-4^x}{x\left(9^x+4^x\right)}$

$= \lim_{x \rightarrow 0} \dfrac{1}{9^x+4^x} \times \left( \dfrac{9^x-1}{x} - \dfrac{4^x-1}{x} \right)$

Using the standard limit $\lim_{x \rightarrow 0} \dfrac{a^x-1}{x} = \log a$,

$= \dfrac{1}{9^0+4^0} \times (\log 9 - \log 4)$

$= \dfrac{1}{1+1} \times \log \left(\dfrac{9}{4}\right)$

$= \dfrac{1}{2} \log \left(\left(\dfrac{3}{2}\right)^2\right)$

$= \dfrac{1}{2} \times 2 \log \left(\dfrac{3}{2}\right)$

$= \log \left(\dfrac{3}{2}\right)$

Answer: $\quad \log \left(\dfrac{3}{2}\right)$

</details>

---

### Q34. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\lim _{x \rightarrow \infty}\left(\dfrac{x^2+x+1}{x+1}-a x-b\right)=4$ then

**Options:**

- **(A)** $\mathrm{a}=1, \mathrm{~b}=4$
- **(B)** $\mathrm{a}=1, \mathrm{~b}=-4$
- **(C)** $\quad \mathrm{a}=2, \mathrm{~b}=-3$
- **(D)** $\mathrm{a}=2, \mathrm{~b}=3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{a}=1, \mathrm{~b}=-4$**

**Detailed Solution:**

$\lim _{x \rightarrow \infty}\left(\dfrac{x^2+x+1}{x+1}-a x-b\right)=4$

$\lim _{x \rightarrow \infty}\left(\dfrac{x^2+x+1 - (ax+b)(x+1)}{x+1}\right)=4$

$\lim _{x \rightarrow \infty}\left(\dfrac{x^2(1-a) + x(1-a-b) + (1-b)}{x+1}\right)=4$

For the limit to be finite, the degree of the numerator must be less than or equal to the degree of the denominator. Therefore, the coefficient of $x^2$ must be zero.

$1 - a = 0 \Rightarrow a = 1$

Substituting $a = 1$ into the limit expression:

$\lim _{x \rightarrow \infty}\left(\dfrac{-bx + 1-b}{x+1}\right)=4$

Dividing the numerator and denominator by $x$:

$\lim _{x \rightarrow \infty}\left(\dfrac{-b + \dfrac{1-b}{x}}{1 + \dfrac{1}{x}}\right) = -b$

Given that the limit is $4$, we have:

$-b = 4 \Rightarrow b = -4$

Thus, $a = 1$ and $b = -4$.

Answer: $\mathrm{a}=1, \mathrm{~b}=-4$

</details>

---

### Q35. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\lim _{x \rightarrow 1} \dfrac{x^2-\mathrm{a} x+\mathrm{b}}{x-1}=7$, then $\mathrm{a}+\mathrm{b}$ is equal to

**Options:**

- **(A)** -1
- **(B)** 1
- **(C)** -11
- **(D)** 11

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -11**

**Detailed Solution:**

For the limit to exist and be finite, the numerator must be zero when $x = 1$.

$1^2 - a(1) + b = 0 \Rightarrow b = a - 1$

Substituting $b = a - 1$ into the limit:

$\lim_{x \rightarrow 1} \dfrac{x^2 - ax + a - 1}{x - 1} = 7$

$\lim_{x \rightarrow 1} \dfrac{(x^2 - 1) - a(x - 1)}{x - 1} = 7$

$\lim_{x \rightarrow 1} \dfrac{(x - 1)(x + 1 - a)}{x - 1} = 7$

$\lim_{x \rightarrow 1} (x + 1 - a) = 7$

$1 + 1 - a = 7 \Rightarrow a = -5$

Substituting $a = -5$ into $b = a - 1$:

$b = -5 - 1 = -6$

Therefore, $a + b = -5 - 6 = -11$

Answer: -11

</details>

---

### Q36. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(x)=\dfrac{1+\cos \pi x}{\pi(1-x)^2}$, for $x \neq 1$ is continuous at $x=1$, then $\mathrm{f}(1)$ is equal to

**Options:**

- **(A)** $\dfrac{\pi}{2}$
- **(B)** $\dfrac{2}{\pi}$
- **(C)** $\dfrac{\pi^2}{4}$
- **(D)** $\dfrac{4}{\pi^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\pi}{2}$**

**Detailed Solution:**

Since $\mathrm{f}(x)$ is continuous at $x=1$, $\mathrm{f}(1) = \lim_{x \to 1} \mathrm{f}(x)$

$\mathrm{f}(1) = \lim_{x \to 1} \dfrac{1+\cos \pi x}{\pi(1-x)^2}$

Let $x = 1 - h$. As $x \to 1$, $h \to 0$.

$\mathrm{f}(1) = \lim_{h \to 0} \dfrac{1+\cos(\pi(1-h))}{\pi h^2}$

$\mathrm{f}(1) = \lim_{h \to 0} \dfrac{1-\cos(\pi h)}{\pi h^2}$

$\mathrm{f}(1) = \lim_{h \to 0} \dfrac{2\sin^2\left(\dfrac{\pi h}{2}\right)}{\pi h^2}$

$\mathrm{f}(1) = \lim_{h \to 0} \dfrac{2}{\pi} \left( \dfrac{\sin\left(\dfrac{\pi h}{2}\right)}{\dfrac{\pi h}{2}} \right)^2 \left( \dfrac{\pi^2}{4} \right)$

$\mathrm{f}(1) = \dfrac{2}{\pi} (1) \left( \dfrac{\pi^2}{4} \right) = \dfrac{\pi}{2}$

Answer: $\dfrac{\pi}{2}$

</details>

---

### Q37. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\lim _{x \rightarrow 0} \dfrac{x}{|x|+x^2}$ is .

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** 0
- **(D)** does not exist.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) does not exist.**

**Detailed Solution:**

Evaluating the right-hand limit as $x \rightarrow 0^+$:

For $x > 0$, $|x| = x$.

$\lim _{x \rightarrow 0^+} \dfrac{x}{x+x^2} = \lim _{x \rightarrow 0^+} \dfrac{x}{x(1+x)} = \lim _{x \rightarrow 0^+} \dfrac{1}{1+x} = 1$

Evaluating the left-hand limit as $x \rightarrow 0^-$:

For $x < 0$, $|x| = -x$.

$\lim _{x \rightarrow 0^-} \dfrac{x}{-x+x^2} = \lim _{x \rightarrow 0^-} \dfrac{x}{x(-1+x)} = \lim _{x \rightarrow 0^-} \dfrac{1}{-1+x} = -1$

Since the left-hand limit is not equal to the right-hand limit, the limit does not exist.

Answer: does not exist.

</details>

---

### Q38. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 2}\left[\frac{1}{x-2}-\frac{2}{x^3-3 x^2+2 x}\right]$ is equal to

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{-2}{3}$
- **(C)** $\frac{3}{2}$
- **(D)** $\frac{-3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{2}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 2}\left[\frac{1}{x-2}-\frac{2}{x\left(x^2-3 x+2\right)}\right] \\ & =\lim _{x \rightarrow 2}\left[\frac{1}{(x-2)}-\frac{2}{x(x-2)(x-1)}\right] \\ & =\lim _{x \rightarrow 2}\left[\frac{x^2-x-2}{x(x-1)(x-2)}\right] \\ & =\lim _{x \rightarrow 2} \frac{(x-2)(x+1)}{x(x-1)(x-2)} \\ & =\lim _{x \rightarrow 2} \frac{x+1}{x(x-1)} \\ & =\frac{3}{2}\end{aligned}$

</details>

---

### Q39. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow a} \frac{\sqrt{a+2 x}-\sqrt{3 x}}{\sqrt{3 a+x}-2 \sqrt{x}}=$

**Options:**

- **(A)** $\frac{1}{3 \sqrt{3}}$
- **(B)** $\frac{2}{\sqrt{3}}$
- **(C)** $\frac{2}{3 \sqrt{3}}$
- **(D)** $\frac{-2}{3 \sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{3 \sqrt{3}}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow a} \frac{\sqrt{a+2 x}-\sqrt{3 x}}{\sqrt{3 a+x}-2 \sqrt{x}} \\ & =\lim _{x \rightarrow a} \frac{(\sqrt{a+2 x}-\sqrt{3 x})(\sqrt{a+2 x}+\sqrt{3 x})(\sqrt{3 a+x}+2 \sqrt{x})}{(\sqrt{3 a+x}-2 \sqrt{x})(\sqrt{3 a+x}+2 \sqrt{x})(\sqrt{a+2 x}+\sqrt{3 x})} \\ & =\lim _{x \rightarrow a} \frac{(a+2 x-3 x)(\sqrt{3 a+x}+2 \sqrt{x})}{(3 a+x-4 x)(\sqrt{a+2 x}+\sqrt{3 x})} \\ & =\frac{(\sqrt{3 a+a}+2 \sqrt{a})}{3(\sqrt{a+2 a}+\sqrt{3 a})} \\ & =\frac{1}{3} \cdot \frac{(2 \sqrt{a}+2 \sqrt{a})}{(\sqrt{3 a}+\sqrt{3 a})} \\ & =\frac{4 \sqrt{a}}{6 \sqrt{3 a}} \\ & =\frac{2}{3 \sqrt{3}}\end{aligned}$

</details>

---

### Q40. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\lim _{x \rightarrow a} \frac{\sqrt{a+2 x}-\sqrt{3 x}}{\sqrt{3 a+x}-2 \sqrt{x}}$ is

**Options:**

- **(A)** $\frac{1}{3 \sqrt{3}}$
- **(B)** $\frac{2}{\sqrt{3}}$
- **(C)** $\frac{2}{3 \sqrt{3}}$
- **(D)** $\frac{4}{3 \sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{3 \sqrt{3}}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow a} \frac{\sqrt{a+2 x}-\sqrt{3 x}}{\sqrt{3 a+x}-2 \sqrt{x}} \\ & =\lim _{x \rightarrow a} \frac{(\sqrt{a+2 x}-\sqrt{3 x})(\sqrt{a+2 x}+\sqrt{3 x})(\sqrt{3 a+x}+2 \sqrt{x})}{(\sqrt{3 a+x}-2 \sqrt{x})(\sqrt{3 a+x}+2 \sqrt{x})(\sqrt{a+2 x}+\sqrt{3 x})} \\ & =\lim _{x \rightarrow a} \frac{(a+2 x-3 x)(\sqrt{3 a+x}+2 \sqrt{x})}{(3 a+x-4 x)(\sqrt{a+2 x}+\sqrt{3 x})} \\ & =\lim _{x \rightarrow a} \frac{(a-x)(\sqrt{3 a+x}+2 \sqrt{x})}{3(a-x)(\sqrt{a+2 x}+\sqrt{3 x})}\end{aligned}$
$\begin{aligned}
& =\frac{1}{3} \cdot \frac{(\sqrt{3 a+a}+2 \sqrt{a})}{(\sqrt{a+2 a}+\sqrt{3 a})} \\
& =\frac{4 \sqrt{a}}{3 \times 2 \times \sqrt{3} \cdot \sqrt{a}} \\
& =\frac{2}{3 \sqrt{3}}
\end{aligned}$

</details>

---

### Q41. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow \infty}\left[\frac{8 x^2+5 x+3}{2 x^2-7 x-5}\right]^{\frac{4 x+3}{8 x-1}}=$

**Options:**

- **(A)** 4
- **(B)** $\frac{1}{2}$
- **(C)** 2
- **(D)** $\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow \infty}\left(\frac{8 x^2+5 x+3}{2 x^2-7 x-5}\right)^{\frac{4 x+3}{8 x-1}}=\lim _{x \rightarrow \infty}\left(\frac{8+\frac{5}{x}+\frac{3}{x^2}}{2-\frac{7}{x}-\frac{5}{x}}\right)^{\frac{4+\frac{3}{x}}{8-\frac{1}{x}}}=\left(\frac{8+0+0}{2-0-0}\right)^{\frac{4+0}{8-0}} \\ & =4^{\frac{1}{2}}=2\end{aligned}$

</details>

---

### Q42. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The quadratic equation whose roots are $m$ and $n$, where $m=\lim _{x \rightarrow 0} \frac{x \log (1+2 x)}{x \tan x}$ and $n=\lim _{x \rightarrow 0} \frac{\log x+\log \left(\frac{(1+x)}{x}\right)}{x}$, is

**Options:**

- **(A)** $x^2-x+2=0$
- **(B)** $x^2-3 x+2=0$
- **(C)** $x^2+x+2=0$
- **(D)** $x^2+3 x+2=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2-3 x+2=0$**

**Detailed Solution:**

$\begin{aligned} & m=\lim _{x \rightarrow 0} \frac{x \log (1+2 x)}{x \cdot \tan x}=\lim _{x \rightarrow 0} \frac{\frac{\log (1+2 x)}{2 x} \cdot 2 x}{\frac{\tan x}{x} \cdot x}=2 \\ & n=\lim _{x \rightarrow 0} \frac{\log x+\log \left(\frac{1+x}{x}\right)}{x}=\lim _{x \rightarrow 0} \frac{\log \left(x \times \frac{1+x}{x}\right)}{x} \\ & =\lim _{x \rightarrow 0} \frac{\log (1+x)}{x}=1\end{aligned}$
now, required quadratic equation is
$x^2-(m+n) x+m n=0$
$\Rightarrow x^2-3 x+2=0$

</details>

---

### Q43. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{n \rightarrow \infty} n\left(\sqrt{n^2+9}-n\right)=$

**Options:**

- **(A)** $\frac{9}{4}$
- **(B)** $9$
- **(C)** $\frac{9}{\sqrt{2}}$
- **(D)** $\frac{9}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{9}{2}$**

**Detailed Solution:**

$\lim _{n \rightarrow \infty} n\left(\sqrt{n^2+9}-n\right)$
$\lim _{n \rightarrow \infty} \frac{n\left(n^2+9-n^2\right)}{\sqrt{n^2+9}+n}$
$\lim _{n \rightarrow \infty} \frac{9}{\sqrt{1+\frac{9}{n^2}}+1}=\frac{9}{2}$

</details>

---

### Q44. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{f}(\mathrm{x})=5-|\mathrm{x}-2|$ and $\mathrm{g}(\mathrm{x})=|\mathrm{x}+1|, \mathrm{x} \in \mathrm{R}$. If $\mathrm{f}(\mathrm{x})$ attains maximum value at $\alpha$ and $g(x)$ attains minimum value at $\beta$, then $\lim _{x \rightarrow-\alpha \beta} \frac{(x-1)\left(x^2-5 x+6\right)}{\left(x^2-6 x+8\right)}$ is equal to

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{3}{2}$
- **(C)** $-\frac{3}{2}$
- **(D)** $-\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

$\mathrm{f}(\mathrm{x})=5-|\mathrm{x}-2|$ is maximum at $\mathrm{x}=2 \Rightarrow \alpha=2$
$\mathrm{g}(\mathrm{x})=|\mathrm{x}+1|$ is minimum at $\mathrm{x}=-1 \Rightarrow \beta=-1$
Now $\lim _{x \rightarrow-\alpha \beta} \frac{(x-1)\left(x^2-5 x+6\right)}{\left(x^2-6 x+8\right)}=\lim _{x \rightarrow-(2)(-1)} \frac{(x-1)(x-2)(x-3)}{(x-2)(x-4)}$
$\begin{aligned} & =\lim _{x \rightarrow 2} \frac{(x-1)(x-3)}{x-4} \\ & =\frac{(2-1)(2-3)}{2-4} \\ & =\frac{1}{2}\end{aligned}$

</details>

---

### Q45. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow x}\left[\frac{\sqrt{x}-1}{\log x}\right]=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $2$
- **(C)** $-2$
- **(D)** $-\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

$$
\begin{aligned}
& \lim _{x \rightarrow x}\left[\frac{\sqrt{x}-1}{\log x}\right] \\
& =\lim _{x \rightarrow 1} \frac{\frac{1}{2 \sqrt{x}}}{\left(\frac{1}{x}\right)} \\
& =\frac{1}{2}
\end{aligned}
$$
... [L' Hospital rule]

</details>

---

### Q46. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 1} \frac{a b^x-a^x b}{x^2-1}=$

**Options:**

- **(A)** $\frac{-\mathrm{ab}}{2} \log \left(\frac{\mathrm{b}}{\mathrm{a}}\right)$
- **(B)** $\frac{\mathrm{ab}}{2} \log \left(\frac{\mathrm{b}}{\mathrm{a}}\right)$
- **(C)** $a b \log \left(\frac{b}{a}\right)$
- **(D)** $-a b \log \left(\frac{b}{a}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\mathrm{ab}}{2} \log \left(\frac{\mathrm{b}}{\mathrm{a}}\right)$**

**Detailed Solution:**

Let $\lim _{x \rightarrow 1} \frac{a b^x-a^x b}{x^2-1}=L$
$$
\begin{aligned}
& \Rightarrow L=\lim _{x \rightarrow 1} \frac{\left(a b^x \log b\right)-\left(a^x \log a \cdot b\right)}{2 x} \\
& =\frac{a b \log b-a b \log a}{2}=\frac{a b}{2} \log \left(\frac{b}{a}\right)
\end{aligned}
$$
... [L' Hospital rule]

</details>

---

### Q47. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 2}(x-1)^{\frac{1}{3 x-6}}=$

**Options:**

- **(A)** $\mathrm{e}^2$
- **(B)** $\mathrm{e}^3$
- **(C)** $\mathrm{e}^{\frac{1}{3}}$
- **(D)** $\mathrm{e}^{\frac{1}{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{e}^{\frac{1}{3}}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 2}(x-1)^{\frac{1}{3 x-6}} \\ & =\lim _{x \rightarrow 2}(x-2+1)^{\frac{1}{3(x-2)}}=\lim _{x \rightarrow 2}\left\{[1+(x-2)]^{\frac{1}{(x-2)}}\right\}^{\frac{1}{3}}=e^{\frac{1}{3}}\end{aligned}$

</details>

---

### Q48. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\lim _{\mathrm{x} \rightarrow 5} \frac{\mathrm{x}^{\mathrm{k}}-5^{\mathrm{k}}}{\mathrm{x}-5}=500$, then the value of $\mathrm{k}$, where $\mathrm{k} \in \mathrm{N}$ is

**Options:**

- **(A)** 5
- **(B)** 3
- **(C)** 4
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 5} \frac{x^k-5^k}{x-5}=500 \\ & \therefore(k)(5)^{k-1}=500 \\ & =4(125)=4(5)^3=4(5)^{4-1} \\ & \therefore k=4\end{aligned}$

</details>

---

### Q49. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$$
\lim _{x \rightarrow 1} \frac{(2 x-3)(\sqrt{x}-1)}{2 x^2+x-3}=
$$

**Options:**

- **(A)** $\frac{1}{5}$
- **(B)** $\frac{1}{10}$
- **(C)** $\frac{-1}{10}$
- **(D)** $\frac{-1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-1}{10}$**

**Detailed Solution:**

$$
\begin{aligned}
& \lim _{x \rightarrow 1} \frac{(2 x-3)(\sqrt{x}-1)}{2 x^2+x-3} \\
& \lim _{x \rightarrow 1} \frac{(2 x-3)(\sqrt{x}-1)}{(x-1)(2 x+3)}=\lim _{x \rightarrow 1} \frac{(2 x-3)(\sqrt{x}-1)}{(\sqrt{x}-1)(\sqrt{x}+1)(2 x+3)} \\
& \lim _{x \rightarrow 1} \frac{(2 x-3)}{(\sqrt{x}+1)(2 x+3)}=\frac{-1}{2(5)}=\frac{-1}{10}
\end{aligned}
$$

</details>

---

### Q50. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow \infty}\left(\sqrt{x^2+5 x-7}-x\right)=$

**Options:**

- **(A)** $\frac{7}{2}$
- **(B)** $5$
- **(C)** $\frac{5}{2}$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{5}{2}$**

**Detailed Solution:**

$$
\begin{aligned}
& \lim _{x \rightarrow \infty} \sqrt{x^2+5-7}-x \\
& =\lim _{x \rightarrow \infty} \frac{\left(\sqrt{x^2+5 x-7}\right)\left(\sqrt{x^2+5 x-7+x}\right)}{\left(\sqrt{x^2+5 x-7+x}\right)} \\
& =\lim _{x \rightarrow \infty} \frac{x^2+5 x-7-x^2}{\left(\sqrt{x^2+5 x-7+x}\right)}
\end{aligned}
$$
Dividing numerator and denominator by $\mathrm{x}$, we get
$$
=\lim _{x \rightarrow \infty} \frac{5-\frac{7}{x}}{\left(\sqrt{1+\frac{5}{x}-\frac{7}{x^2}+1}\right)}=\frac{5}{\sqrt{1}+1}=\frac{5}{2}
$$

</details>

---

### Q51. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

If $G(x)=-\sqrt{25-x^{2}}$, then $\lim _{x \rightarrow 1} \frac{G(x)-G(t)}{x-1}$ is

**Options:**

- **(A)** $\frac{1}{24}$
- **(B)** $\frac{1}{5}$
- **(C)** $-\sqrt{24}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) None of these**

**Detailed Solution:**

$\lim _{x \rightarrow 1} \frac{G(x)-G(1)}{x-1}=\lim _{x \rightarrow 1} G^{\prime}(x)$
$$
\begin{array}{l}
=\lim _{x \rightarrow 1}-\frac{1}{2 \sqrt{25-x^{2}}}(-2 x) \\
=\frac{1}{\sqrt{24}}
\end{array}
$$

</details>

---

### Q52. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

The value of $\lim _{x \rightarrow \infty} \frac{1+2+3 \ldots+n}{n^{2}}$ is

**Options:**

- **(A)** 1
- **(B)** $\frac{1}{2}$
- **(C)** 0
- **(D)** $\frac{3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2}$**

**Detailed Solution:**

$\lim _{n \rightarrow \infty} \frac{1+2+3+\ldots+n}{n^{2}}=\lim _{n \rightarrow \infty} \frac{n(n+1)}{2 n^{2}}$
$=\lim _{n \rightarrow \infty} \frac{\left(1+\frac{1}{n}\right)}{2}=\frac{1}{2}$

</details>

---

### Q53. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

If $\lim _{x \rightarrow 0} \frac{\left(e^{k x}-1\right) \sin k x}{x^{2}}=4$, then $k$ is equal to

**Options:**

- **(A)** 2
- **(B)** $-2$
- **(C)** $\pm 2$
- **(D)** $\pm 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\pm 2$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0} \frac{\left(e^{k x}-1\right) \sin k x}{x^{2}}=4 \\ & \Rightarrow \quad \lim _{x \rightarrow 0}\left[\frac{e^{k x} \sin k x}{x^{2}}-\frac{\sin k x}{x^{2}}\right]=4 \\ & \Rightarrow \lim _{x \rightarrow 0}\left[\frac{e^{k x} \cos k x \cdot k+k e^{k x} \sin k x}{2 x}-\frac{k \cos k x}{2 x}\right]=4 \\ & \Rightarrow \lim _{x \rightarrow 0}\left[\frac{k^{2} e^{k x} \cos k x-k^{2} e^{k x} \sin k x+k^{2} e^{k x} \sin k x}{+k^{2} e^{k x} \cos k x}{2}\right.\\ & \Rightarrow \frac{k^{2}-0+0+k^{2}}{2}+0=4 \\ & \Rightarrow \quad k^{2}=4 \\ & \Rightarrow \quad k=\pm 2 \end{aligned}$

</details>

---

### Q54. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

Given $f(x)=\frac{a x+b}{x+1}, \lim _{x \rightarrow \infty} f(x)=1 \quad$ and
$\lim _{x \rightarrow 0} f(x)=2$, then $f(-2)$ is

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $\overline{2}$
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Given, $\lim _{x \rightarrow \infty} f(x)=1$
$\Rightarrow \quad \lim _{x \rightarrow \infty} \frac{a x+b}{x+1}=1$
$\Rightarrow \quad \lim _{x \rightarrow \infty} \frac{a+\frac{b}{x}}{1+\frac{1}{x}}=1$
$\Rightarrow \quad a=1$
$\Rightarrow \quad \lim _{x \rightarrow 0} f(x)=2$
$\Rightarrow \quad \lim _{x \rightarrow 0} \frac{a x+b}{x+1}=2$
$\Rightarrow \quad b=2$
$\Rightarrow \quad \begin{aligned} \Rightarrow[\sin (\log x)&+\cos (\log x)] d x \\=& \int \frac{d}{d x}\{x \sin (\log x)\} d x \\ &=x \sin (\log x)+c \end{aligned}$

</details>

---

