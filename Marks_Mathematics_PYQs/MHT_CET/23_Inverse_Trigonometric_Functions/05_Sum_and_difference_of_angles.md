# MHT CET Mathematics - Inverse Trigonometric Functions

## Topic 5: Sum and difference of angles

**Total Questions:** 61

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\sin^{-1} x + \sin^{-1} y + \sin^{-1} z = \pi$, then $x^4 + y^4 + z^4 + 4x^2 y^2 z^2 = $

**Options:**

- **(A)** $x^2 y^2 + x^2 z^2 + y^2 z^2$
- **(B)** $2(x^2 y^2 + x^2 z^2 + y^2 z^2)$
- **(C)** $3(x^2 y^2 + x^2 z^2 + y^2 z^2)$
- **(D)** $4(x^2 y^2 + x^2 z^2 + y^2 z^2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2(x^2 y^2 + x^2 z^2 + y^2 z^2)$**

**Detailed Solution:**

Let $A = \sin^{-1} x$, $B = \sin^{-1} y$, and $C = \sin^{-1} z$.

Then $A + B + C = \pi$, which gives $A + B = \pi - C$.

Taking $\cos$ on both sides:

$\cos(A + B) = \cos(\pi - C)$

$\cos A \cos B - \sin A \sin B = -\cos C$

$\cos A \cos B + \cos C = \sin A \sin B$

Squaring both sides:

$\cos^2 A \cos^2 B + \cos^2 C + 2 \cos A \cos B \cos C = \sin^2 A \sin^2 B$

$(1 - \sin^2 A)(1 - \sin^2 B) + 1 - \sin^2 C + 2 \cos A \cos B \cos C = \sin^2 A \sin^2 B$

$1 - \sin^2 A - \sin^2 B + \sin^2 A \sin^2 B + 1 - \sin^2 C + 2 \cos A \cos B \cos C = \sin^2 A \sin^2 B$

$2 - (\sin^2 A + \sin^2 B + \sin^2 C) + 2 \cos A \cos B \cos C = 0$

Substituting $x = \sin A$, $y = \sin B$, and $z = \sin C$:

$2 \cos A \cos B \cos C = x^2 + y^2 + z^2 - 2$

Squaring both sides again:

$4 \cos^2 A \cos^2 B \cos^2 C = (x^2 + y^2 + z^2 - 2)^2$

$4 (1 - x^2)(1 - y^2)(1 - z^2) = (x^2 + y^2 + z^2 - 2)^2$

$4 (1 - x^2 - y^2 - z^2 + x^2 y^2 + y^2 z^2 + z^2 x^2 - x^2 y^2 z^2) = (x^2 + y^2 + z^2)^2 - 4(x^2 + y^2 + z^2) + 4$

$4 - 4(x^2 + y^2 + z^2) + 4(x^2 y^2 + y^2 z^2 + z^2 x^2) - 4x^2 y^2 z^2 = x^4 + y^4 + z^4 + 2(x^2 y^2 + y^2 z^2 + z^2 x^2) - 4(x^2 + y^2 + z^2) + 4$

Canceling common terms from both sides:

$4(x^2 y^2 + y^2 z^2 + z^2 x^2) - 4x^2 y^2 z^2 = x^4 + y^4 + z^4 + 2(x^2 y^2 + y^2 z^2 + z^2 x^2)$

$x^4 + y^4 + z^4 + 4x^2 y^2 z^2 = 2(x^2 y^2 + y^2 z^2 + z^2 x^2)$

Answer: $2(x^2 y^2 + x^2 z^2 + y^2 z^2)$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan^{-1}\left(\dfrac{1}{3}\right) + \tan^{-1}\left(\dfrac{1}{5}\right) + \tan^{-1}\left(\dfrac{1}{7}\right) = \dfrac{\pi}{4} - \tan^{-1}\left(\dfrac{1}{k}\right)$ then the value of $k$ is

**Options:**

- **(A)** $6$
- **(B)** $9$
- **(C)** $4$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $8$**

**Detailed Solution:**

Using the formula $\tan^{-1}x + \tan^{-1}y = \tan^{-1}\left(\dfrac{x+y}{1-xy}\right)$ for $xy < 1$:

$\tan^{-1}\left(\dfrac{1}{3}\right) + \tan^{-1}\left(\dfrac{1}{5}\right) = \tan^{-1}\left(\dfrac{\dfrac{1}{3} + \dfrac{1}{5}}{1 - \dfrac{1}{3} \cdot \dfrac{1}{5}}\right) = \tan^{-1}\left(\dfrac{\dfrac{8}{15}}{\dfrac{14}{15}}\right) = \tan^{-1}\left(\dfrac{4}{7}\right)$

Adding the third term:

$\tan^{-1}\left(\dfrac{4}{7}\right) + \tan^{-1}\left(\dfrac{1}{7}\right) = \tan^{-1}\left(\dfrac{\dfrac{4}{7} + \dfrac{1}{7}}{1 - \dfrac{4}{7} \cdot \dfrac{1}{7}}\right) = \tan^{-1}\left(\dfrac{\dfrac{5}{7}}{\dfrac{45}{49}}\right) = \tan^{-1}\left(\dfrac{5}{7} \cdot \dfrac{49}{45}\right) = \tan^{-1}\left(\dfrac{7}{9}\right)$

The given equation becomes:

$\tan^{-1}\left(\dfrac{7}{9}\right) = \dfrac{\pi}{4} - \tan^{-1}\left(\dfrac{1}{k}\right)$

Since $\dfrac{\pi}{4} = \tan^{-1}(1)$, the right hand side can be written as:

$\tan^{-1}(1) - \tan^{-1}\left(\dfrac{1}{k}\right) = \tan^{-1}\left(\dfrac{1 - \dfrac{1}{k}}{1 + 1 \cdot \dfrac{1}{k}}\right) = \tan^{-1}\left(\dfrac{k-1}{k+1}\right)$

Equating both sides:

$\tan^{-1}\left(\dfrac{7}{9}\right) = \tan^{-1}\left(\dfrac{k-1}{k+1}\right)$

$\dfrac{7}{9} = \dfrac{k-1}{k+1}$

$7(k+1) = 9(k-1)$

$7k + 7 = 9k - 9$

$2k = 16$

$k = 8$

Answer: $8$

</details>

---

### Q3. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan^{-1}\left[\dfrac{\sqrt{5 + 2\sqrt{6}}}{1 - \sqrt{6}}\right] = a + \tan^{-1}(\sqrt{2})$, then $\csc(a) = \ldots$

**Options:**

- **(A)** $2$
- **(B)** $-2$
- **(C)** $\dfrac{2}{\sqrt{3}}$
- **(D)** $\dfrac{-2}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{-2}{\sqrt{3}}$**

**Detailed Solution:**

First, simplify the expression inside the square root:

$\sqrt{5 + 2\sqrt{6}} = \sqrt{3 + 2 + 2\sqrt{3}\sqrt{2}} = \sqrt{(\sqrt{3} + \sqrt{2})^2} = \sqrt{3} + \sqrt{2}$

Now, substitute this back into the given inverse trigonometric expression:

$\tan^{-1}\left[\dfrac{\sqrt{5 + 2\sqrt{6}}}{1 - \sqrt{6}}\right] = \tan^{-1}\left(\dfrac{\sqrt{3} + \sqrt{2}}{1 - \sqrt{3}\sqrt{2}}\right)$

Using the identity $\tan^{-1}\left(\dfrac{x + y}{1 - xy}\right) = \tan^{-1}(x) + \tan^{-1}(y) - \pi$ for $x > 0$, $y > 0$, and $xy > 1$, we have $x = \sqrt{3}$ and $y = \sqrt{2}$. Since $\sqrt{3} \times \sqrt{2} = \sqrt{6} > 1$, we get:

$\tan^{-1}\left(\dfrac{\sqrt{3} + \sqrt{2}}{1 - \sqrt{3}\sqrt{2}}\right) = \tan^{-1}(\sqrt{3}) + \tan^{-1}(\sqrt{2}) - \pi$

We know that $\tan^{-1}(\sqrt{3}) = \dfrac{\pi}{3}$, so the expression becomes:

$\dfrac{\pi}{3} + \tan^{-1}(\sqrt{2}) - \pi = -\dfrac{2\pi}{3} + \tan^{-1}(\sqrt{2})$

Given that this is equal to $a + \tan^{-1}(\sqrt{2})$, we can equate the two:

$a = -\dfrac{2\pi}{3}$

Finally, we need to find $\csc(a)$:

$\csc\left(-\dfrac{2\pi}{3}\right) = -\csc\left(\dfrac{2\pi}{3}\right) = -\dfrac{1}{\sin\left(\dfrac{2\pi}{3}\right)} = -\dfrac{1}{\dfrac{\sqrt{3}}{2}} = \dfrac{-2}{\sqrt{3}}$

Answer: $\dfrac{-2}{\sqrt{3}}$

</details>

---

### Q4. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin^{-1} x + \cos^{-1}\left(\dfrac{1}{\sqrt{5}}\right) = \dfrac{\pi}{4}$, then $x = \ldots$

**Options:**

- **(A)** $\dfrac{-1}{\sqrt{10}}$
- **(B)** $\dfrac{1}{\sqrt{10}}$
- **(C)** $\dfrac{3}{\sqrt{10}}$
- **(D)** $\dfrac{-3}{\sqrt{10}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{-1}{\sqrt{10}}$**

**Detailed Solution:**

Given $\sin^{-1} x + \cos^{-1}\left(\dfrac{1}{\sqrt{5}}\right) = \dfrac{\pi}{4}$

$\sin^{-1} x = \dfrac{\pi}{4} - \cos^{-1}\left(\dfrac{1}{\sqrt{5}}\right)$

Taking sine on both sides:

$x = \sin\left(\dfrac{\pi}{4} - \cos^{-1}\left(\dfrac{1}{\sqrt{5}}\right)\right)$

Using the formula $\sin(A - B) = \sin A \cos B - \cos A \sin B$:

$x = \sin\left(\dfrac{\pi}{4}\right) \cos\left(\cos^{-1}\left(\dfrac{1}{\sqrt{5}}\right)\right) - \cos\left(\dfrac{\pi}{4}\right) \sin\left(\cos^{-1}\left(\dfrac{1}{\sqrt{5}}\right)\right)$

We know that $\cos\left(\cos^{-1}\left(\dfrac{1}{\sqrt{5}}\right)\right) = \dfrac{1}{\sqrt{5}}$ and $\sin\left(\cos^{-1}\left(\dfrac{1}{\sqrt{5}}\right)\right) = \sqrt{1 - \left(\dfrac{1}{\sqrt{5}}\right)^2} = \dfrac{2}{\sqrt{5}}$

Substituting these values:

$x = \dfrac{1}{\sqrt{2}} \cdot \dfrac{1}{\sqrt{5}} - \dfrac{1}{\sqrt{2}} \cdot \dfrac{2}{\sqrt{5}}$

$x = \dfrac{1}{\sqrt{10}} - \dfrac{2}{\sqrt{10}} = \dfrac{-1}{\sqrt{10}}$

Answer: $\dfrac{-1}{\sqrt{10}}$

</details>

---

### Q5. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\cot^{-1}\left(\dfrac{ab+1}{a-b}\right) + \tan^{-1}\left(\dfrac{b-c}{bc+1}\right) + \cot^{-1}\left(\dfrac{ac+1}{c-a}\right)$ is

**Options:**

- **(A)** $abc$
- **(B)** $ab + bc + ca$
- **(C)** $0$
- **(D)** $1 - ab - bc - ac$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0$**

**Detailed Solution:**

Using the inverse trigonometric identity $\cot^{-1} y - \cot^{-1} x = \cot^{-1}\left(\dfrac{xy+1}{x-y}\right)$, we can evaluate each term of the given expression.

The first term is:
$\cot^{-1}\left(\dfrac{ab+1}{a-b}\right) = \cot^{-1} b - \cot^{-1} a$

For the second term, using $\tan^{-1} x = \cot^{-1}\left(\dfrac{1}{x}\right)$, we get:
$\tan^{-1}\left(\dfrac{b-c}{bc+1}\right) = \cot^{-1}\left(\dfrac{bc+1}{b-c}\right) = \cot^{-1} c - \cot^{-1} b$

The third term is:
$\cot^{-1}\left(\dfrac{ac+1}{c-a}\right) = \cot^{-1} a - \cot^{-1} c$

Adding all three terms together:
$(\cot^{-1} b - \cot^{-1} a) + (\cot^{-1} c - \cot^{-1} b) + (\cot^{-1} a - \cot^{-1} c)$

All terms cancel out, yielding:
$0$

Answer: $0$

</details>

---

### Q6. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\cot^{-1} 2$ and $\cot^{-1} 3$ are the angles of a triangle, then the third angle is ...

**Options:**

- **(A)** $\dfrac{\pi}{4}$
- **(B)** $\dfrac{3\pi}{4}$
- **(C)** $\dfrac{\pi}{6}$
- **(D)** $\dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3\pi}{4}$**

**Detailed Solution:**

Let the angles of the triangle be $A$, $B$, and $C$.

Given $A = \cot^{-1} 2$ and $B = \cot^{-1} 3$.

This implies $\tan A = \dfrac{1}{2}$ and $\tan B = \dfrac{1}{3}$.

Using the tangent addition formula:

$\tan(A + B) = \dfrac{\tan A + \tan B}{1 - \tan A \tan B}$

Substituting the values:

$\tan(A + B) = \dfrac{\dfrac{1}{2} + \dfrac{1}{3}}{1 - \dfrac{1}{2} \cdot \dfrac{1}{3}} = \dfrac{\dfrac{5}{6}}{\dfrac{5}{6}} = 1$

Since $A$ and $B$ are acute angles, $A + B = \dfrac{\pi}{4}$.

In a triangle, the sum of angles is $\pi$. Therefore, the third angle $C$ is:

$C = \pi - (A + B) = \pi - \dfrac{\pi}{4} = \dfrac{3\pi}{4}$

Answer: $\dfrac{3\pi}{4}$

</details>

---

### Q7. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For $x > 0$ and $(x \log x) < 1$, if $y = \cot^{-1}\left(\dfrac{x - \log x^{x^2}}{\log e^{x^2} + \log x^x}\right)$, then $\dfrac{dy}{dx} = \ldots$

**Options:**

- **(A)** $\dfrac{1}{1+x^2} + \dfrac{2}{x[1+(\log x)^2]}$
- **(B)** $\dfrac{1}{1+x^2} + \dfrac{1}{x[1+(\log x)^2]}$
- **(C)** $\dfrac{-1}{1+x^2} + \dfrac{1}{x[1+(\log x)^2]}$
- **(D)** $\dfrac{1}{1+x^2} + \dfrac{1}{[1+(\log x)^2]}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{1+x^2} + \dfrac{1}{x[1+(\log x)^2]}$**

**Detailed Solution:**

Given function is:

$y = \cot^{-1}\left(\dfrac{x - \log x^{x^2}}{\log e^{x^2} + \log x^x}\right)$

Simplify the numerator and the denominator of the argument:
Numerator $= x - x^2 \log x = x(1 - x \log x)$
Denominator $= x^2 \log e + x \log x = x^2 + x \log x = x(x + \log x)$

Substitute these back into the function:

$y = \cot^{-1}\left(\dfrac{x(1 - x \log x)}{x(x + \log x)}\right) = \cot^{-1}\left(\dfrac{1 - x \log x}{x + \log x}\right)$

We know the inverse trigonometric identity $\cot^{-1}\left(\dfrac{1 - ab}{a + b}\right) = \tan^{-1}\left(\dfrac{a + b}{1 - ab}\right)$ (up to a constant multiple of $\pi$ depending on the sign of $a+b$, which becomes zero upon differentiation).

Using $a = x$ and $b = \log x$, and given $x \log x < 1$ (so $1 - ab > 0$):

$y = C + \tan^{-1}\left(\dfrac{x + \log x}{1 - x \log x}\right)$

$y = C + \tan^{-1} x + \tan^{-1}(\log x)$

Differentiating both sides with respect to $x$:

$\dfrac{dy}{dx} = \dfrac{d}{dx}(\tan^{-1} x) + \dfrac{d}{dx}(\tan^{-1}(\log x))$

$\dfrac{dy}{dx} = \dfrac{1}{1+x^2} + \dfrac{1}{1+(\log x)^2} \cdot \dfrac{d}{dx}(\log x)$

$\dfrac{dy}{dx} = \dfrac{1}{1+x^2} + \dfrac{1}{x[1+(\log x)^2]}$

Answer: $\dfrac{1}{1+x^2} + \dfrac{1}{x[1+(\log x)^2]}$

</details>

---

### Q8. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\tan^{-1}ax + \tan^{-1}3x = \dfrac{\pi}{4}$, where $3ax^2 < 1$, then value of $a$ for $x = \dfrac{1}{6}$ is $\ldots$

**Options:**

- **(A)** $2$
- **(B)** $3$
- **(C)** $4$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2$**

**Detailed Solution:**

Given $\tan^{-1}ax + \tan^{-1}3x = \dfrac{\pi}{4}$

Using the formula $\tan^{-1}A + \tan^{-1}B = \tan^{-1}\left(\dfrac{A+B}{1-AB}\right)$ for $AB < 1$, we get:

$\tan^{-1}\left(\dfrac{ax + 3x}{1 - 3ax^2}\right) = \dfrac{\pi}{4}$

$\dfrac{ax + 3x}{1 - 3ax^2} = \tan\left(\dfrac{\pi}{4}\right) = 1$

$ax + 3x = 1 - 3ax^2$

Substituting $x = \dfrac{1}{6}$:

$a\left(\dfrac{1}{6}\right) + 3\left(\dfrac{1}{6}\right) = 1 - 3a\left(\dfrac{1}{6}\right)^2$

$\dfrac{a}{6} + \dfrac{1}{2} = 1 - \dfrac{3a}{36}$

$\dfrac{a}{6} + \dfrac{a}{12} = 1 - \dfrac{1}{2}$

$\dfrac{3a}{12} = \dfrac{1}{2}$

$\dfrac{a}{4} = \dfrac{1}{2}$

$a = 2$

Answer: $2$

</details>

---

### Q9. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \tan^{-1}\left(\dfrac{\log\left(\dfrac{e}{x^3}\right)}{\log ex^3}\right) + \tan^{-1}\left(\dfrac{\log(e^4x^3)}{\log\left(\dfrac{e}{x^{12}}\right)}\right)$, $x \in \left(e^{-\frac{1}{3}}, e^{\frac{1}{12}}\right)$ then $\dfrac{dy}{dx}$ is equal to...

**Options:**

- **(A)** $1$
- **(B)** $0$
- **(C)** $-1$
- **(D)** $\dfrac{1}{e}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0$**

**Detailed Solution:**

Given function is:

$y = \tan^{-1}\left(\dfrac{\log\left(\dfrac{e}{x^3}\right)}{\log(ex^3)}\right) + \tan^{-1}\left(\dfrac{\log(e^4x^3)}{\log\left(\dfrac{e}{x^{12}}\right)}\right)$

Using the properties of logarithms, we can simplify the arguments:

$\dfrac{\log\left(\dfrac{e}{x^3}\right)}{\log(ex^3)} = \dfrac{\log e - \log x^3}{\log e + \log x^3} = \dfrac{1 - 3\log x}{1 + 3\log x}$

$\dfrac{\log(e^4x^3)}{\log\left(\dfrac{e}{x^{12}}\right)} = \dfrac{\log e^4 + \log x^3}{\log e - \log x^{12}} = \dfrac{4 + 3\log x}{1 - 12\log x}$

Substituting these back into the expression for $y$:

$y = \tan^{-1}\left(\dfrac{1 - 3\log x}{1 + 1 \cdot 3\log x}\right) + \tan^{-1}\left(\dfrac{4 + 3\log x}{1 - 4 \cdot 3\log x}\right)$

We use the inverse trigonometric identities:
$\tan^{-1}\left(\dfrac{a - b}{1 + ab}\right) = \tan^{-1}a - \tan^{-1}b$ (valid for $ab > -1$)
$\tan^{-1}\left(\dfrac{a + b}{1 - ab}\right) = \tan^{-1}a + \tan^{-1}b$ (valid for $ab < 1$)

For the first term, $a = 1$ and $b = 3\log x$. Since $x > e^{-1/3}$, we have $3\log x > -1$, so $ab > -1$.
$\tan^{-1}\left(\dfrac{1 - 3\log x}{1 + 3\log x}\right) = \tan^{-1}(1) - \tan^{-1}(3\log x) = \dfrac{\pi}{4} - \tan^{-1}(3\log x)$

For the second term, $a = 4$ and $b = 3\log x$. Since $x < e^{1/12}$, we have $12\log x < 1$, so $ab < 1$.
$\tan^{-1}\left(\dfrac{4 + 3\log x}{1 - 12\log x}\right) = \tan^{-1}(4) + \tan^{-1}(3\log x)$

Adding the two terms together:

$y = \left(\dfrac{\pi}{4} - \tan^{-1}(3\log x)\right) + \left(\tan^{-1}(4) + \tan^{-1}(3\log x)\right)$

$y = \dfrac{\pi}{4} + \tan^{-1}(4)$

Since $y$ is a constant and independent of $x$, its derivative with respect to $x$ is zero:

$\dfrac{dy}{dx} = 0$

Answer: $0$

</details>

---

### Q10. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sum\limits_{n=1}^{2026}\tan^{-1}\left(\dfrac{1}{n^2+n+1}\right) = \tan^{-1}\left(1 - \dfrac{1}{x}\right)$, where $x \neq 0$, then $x = $

**Options:**

- **(A)** $2028$
- **(B)** $2026$
- **(C)** $1014$
- **(D)** $1013$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1014$**

**Detailed Solution:**

The general term of the series is given by:

$T_n = \tan^{-1}\left(\dfrac{1}{n^2+n+1}\right)$

This can be rewritten as:

$T_n = \tan^{-1}\left(\dfrac{1}{1 + n(n+1)}\right) = \tan^{-1}\left(\dfrac{(n+1) - n}{1 + (n+1)n}\right)$

Using the formula $\tan^{-1}\left(\dfrac{x-y}{1+xy}\right) = \tan^{-1}(x) - \tan^{-1}(y)$, we get:

$T_n = \tan^{-1}(n+1) - \tan^{-1}(n)$

Summing from $n=1$ to $n=2026$, we obtain a telescoping series:

$\sum\limits_{n=1}^{2026} T_n = (\tan^{-1}(2) - \tan^{-1}(1)) + (\tan^{-1}(3) - \tan^{-1}(2)) + \dots + (\tan^{-1}(2027) - \tan^{-1}(2026))$

$\sum\limits_{n=1}^{2026} T_n = \tan^{-1}(2027) - \tan^{-1}(1)$

Applying the inverse tangent difference formula again:

$\tan^{-1}(2027) - \tan^{-1}(1) = \tan^{-1}\left(\dfrac{2027 - 1}{1 + 2027 \times 1}\right)$

$= \tan^{-1}\left(\dfrac{2026}{2028}\right) = \tan^{-1}\left(\dfrac{1013}{1014}\right)$

We are given that this sum is equal to $\tan^{-1}\left(1 - \dfrac{1}{x}\right)$. Therefore:

$\tan^{-1}\left(\dfrac{1013}{1014}\right) = \tan^{-1}\left(1 - \dfrac{1}{x}\right)$

Equating the arguments:

$\dfrac{1013}{1014} = 1 - \dfrac{1}{x}$

$\dfrac{1}{x} = 1 - \dfrac{1013}{1014} = \dfrac{1}{1014}$

$x = 1014$

Answer: $1014$

</details>

---

### Q11. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\sin^{-1}\left(\dfrac{12}{13}\right) + \cos^{-1}\left(\dfrac{4}{5}\right) + \tan^{-1}\left(\dfrac{63}{16}\right) =$

**Options:**

- **(A)** $\dfrac{\pi}{2}$
- **(B)** $\dfrac{3\pi}{2}$
- **(C)** $\pi$
- **(D)** $2\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\pi$**

**Detailed Solution:**

Let $A = \sin^{-1}\left(\dfrac{12}{13}\right) \Rightarrow \tan A = \dfrac{12}{5}$

Let $B = \cos^{-1}\left(\dfrac{4}{5}\right) \Rightarrow \tan B = \dfrac{3}{4}$

Let $C = \tan^{-1}\left(\dfrac{63}{16}\right)$

$\tan(A + B) = \dfrac{\tan A + \tan B}{1 - \tan A \tan B}$

$\tan(A + B) = \dfrac{\dfrac{12}{5} + \dfrac{3}{4}}{1 - \dfrac{12}{5} \times \dfrac{3}{4}} = \dfrac{\dfrac{63}{20}}{1 - \dfrac{36}{20}} = -\dfrac{63}{16}$

Since $A, B \in \left(0, \dfrac{\pi}{2}\right)$ and $\tan A \tan B = \dfrac{36}{20} > 1$, we have:

$A + B = \pi + \tan^{-1}\left(-\dfrac{63}{16}\right) = \pi - \tan^{-1}\left(\dfrac{63}{16}\right)$

$A + B = \pi - C$

$A + B + C = \pi$

Answer: $\pi$

</details>

---

### Q12. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \tan^{-1}\left(\dfrac{1}{x^2+x+1}\right) + \tan^{-1}\left(\dfrac{1}{x^2+3x+3}\right) + \tan^{-1}\left(\dfrac{1}{x^2+5x+7}\right) + \ldots$ upto $n$ terms, then $y'(0) =$

**Options:**

- **(A)** $\dfrac{n^2}{n^2+1}$
- **(B)** $-\dfrac{n^2}{n^2+1}$
- **(C)** $0$
- **(D)** $\dfrac{1}{n^2+1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\dfrac{n^2}{n^2+1}$**

**Detailed Solution:**

The given series can be written as the sum of $n$ terms where the $r$-th term is given by:

$T_r = \tan^{-1}\left(\dfrac{1}{1 + (x+r-1)(x+r)}\right)$

Using the identity $\tan^{-1}\left(\dfrac{A-B}{1+AB}\right) = \tan^{-1}(A) - \tan^{-1}(B)$, we can rewrite $T_r$ as:

$T_r = \tan^{-1}\left(\dfrac{(x+r) - (x+r-1)}{1 + (x+r)(x+r-1)}\right) = \tan^{-1}(x+r) - \tan^{-1}(x+r-1)$

Writing the first few terms:

$T_1 = \tan^{-1}(x+1) - \tan^{-1}(x)$

$T_2 = \tan^{-1}(x+2) - \tan^{-1}(x+1)$

$T_3 = \tan^{-1}(x+3) - \tan^{-1}(x+2)$

$\vdots$

$T_n = \tan^{-1}(x+n) - \tan^{-1}(x+n-1)$

Summing these $n$ terms, all intermediate terms cancel out, leaving:

$y = \sum_{r=1}^{n} T_r = \tan^{-1}(x+n) - \tan^{-1}(x)$

Differentiating with respect to $x$:

$y'(x) = \dfrac{1}{1+(x+n)^2} - \dfrac{1}{1+x^2}$

Substituting $x = 0$:

$y'(0) = \dfrac{1}{1+n^2} - \dfrac{1}{1+0} = \dfrac{1}{1+n^2} - 1$

$y'(0) = \dfrac{1 - (1+n^2)}{1+n^2} = -\dfrac{n^2}{n^2+1}$

Answer: $-\dfrac{n^2}{n^2+1}$

</details>

---

### Q13. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan^{-1}(1) + \tan^{-1}(3) + \tan^{-1}(5) + \tan^{-1}\left(\dfrac{1}{4}\right) = \pi + \tan^{-1}\left(\dfrac{\alpha}{2}\right)$, then the value of $\alpha$ is...

**Options:**

- **(A)** $\dfrac{46}{41}$
- **(B)** $\dfrac{23}{41}$
- **(C)** $\dfrac{42}{41}$
- **(D)** $\dfrac{44}{41}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{46}{41}$**

**Detailed Solution:**

Grouping the terms of the left hand side:

$\tan^{-1}(1) + \tan^{-1}\left(\dfrac{1}{4}\right) = \tan^{-1}\left(\dfrac{1 + \dfrac{1}{4}}{1 - \dfrac{1}{4}}\right) = \tan^{-1}\left(\dfrac{5}{3}\right)$

Adding $\tan^{-1}(3)$ to this result:

$\tan^{-1}\left(\dfrac{5}{3}\right) + \tan^{-1}(3) = \pi + \tan^{-1}\left(\dfrac{\dfrac{5}{3} + 3}{1 - \dfrac{5}{3} \times 3}\right)$

$= \pi + \tan^{-1}\left(\dfrac{14}{-12}\right) = \pi - \tan^{-1}\left(\dfrac{7}{6}\right)$

Adding $\tan^{-1}(5)$ to this result:

$\pi - \tan^{-1}\left(\dfrac{7}{6}\right) + \tan^{-1}(5) = \pi + \tan^{-1}\left(\dfrac{5 - \dfrac{7}{6}}{1 + 5 \times \dfrac{7}{6}}\right)$

$= \pi + \tan^{-1}\left(\dfrac{\dfrac{23}{6}}{\dfrac{41}{6}}\right) = \pi + \tan^{-1}\left(\dfrac{23}{41}\right)$

Equating this to the right hand side:

$\pi + \tan^{-1}\left(\dfrac{23}{41}\right) = \pi + \tan^{-1}\left(\dfrac{\alpha}{2}\right)$

$\dfrac{\alpha}{2} = \dfrac{23}{41} \Rightarrow \alpha = \dfrac{46}{41}$

Answer: $\dfrac{46}{41}$

</details>

---

### Q14. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\tan ^{-1}\left(\frac{1}{1+x+x^2}\right)+\tan ^{-1}\left(\frac{1}{x^2+3 x+3}\right)+\tan ^{-1}\left(\frac{1}{x^2+5 x+7}\right)$ then the value of $\mathrm{y}^{\prime}(0)$ is

**Options:**

- **(A)** $\frac{9}{10}$
- **(B)** $\frac{1}{10}$
- **(C)** $-\frac{9}{10}$
- **(D)** $-\frac{1}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{9}{10}$**

**Detailed Solution:**

The given function can be rewritten by splitting the denominators:

$y = \tan^{-1}\left(\dfrac{1}{1+x(x+1)}\right) + \tan^{-1}\left(\dfrac{1}{1+(x^2+3x+2)}\right) + \tan^{-1}\left(\dfrac{1}{1+(x^2+5x+6)}\right)$

$y = \tan^{-1}\left(\dfrac{1}{1+x(x+1)}\right) + \tan^{-1}\left(\dfrac{1}{1+(x+1)(x+2)}\right) + \tan^{-1}\left(\dfrac{1}{1+(x+2)(x+3)}\right)$

Using the formula $\tan^{-1}\left(\dfrac{a-b}{1+ab}\right) = \tan^{-1}a - \tan^{-1}b$, we can express each term as a difference:

$y = \tan^{-1}\left(\dfrac{(x+1)-x}{1+x(x+1)}\right) + \tan^{-1}\left(\dfrac{(x+2)-(x+1)}{1+(x+1)(x+2)}\right) + \tan^{-1}\left(\dfrac{(x+3)-(x+2)}{1+(x+2)(x+3)}\right)$

$y = [\tan^{-1}(x+1) - \tan^{-1}x] + [\tan^{-1}(x+2) - \tan^{-1}(x+1)] + [\tan^{-1}(x+3) - \tan^{-1}(x+2)]$

Most terms cancel out, leaving:

$y = \tan^{-1}(x+3) - \tan^{-1}x$

Differentiating with respect to $x$:

$y' = \dfrac{1}{1+(x+3)^2} - \dfrac{1}{1+x^2}$

Substituting $x = 0$:

$y'(0) = \dfrac{1}{1+(0+3)^2} - \dfrac{1}{1+0^2}$

$y'(0) = \dfrac{1}{10} - 1 = -\dfrac{9}{10}$

Answer: $-\frac{9}{10}$

</details>

---

### Q15. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan ^{-1}(x+1)+\tan ^{-1} x+\tan ^{-1}(x-1)=\tan ^{-1} 3$, then for $x < 0$ the value of $500 x^4+270 x^2+997=$

**Options:**

- **(A)** 6716
- **(B)** 1767
- **(C)** 1768
- **(D)** 6717

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1767**

**Detailed Solution:**

Given the equation:

$\tan^{-1}(x+1) + \tan^{-1} x + \tan^{-1}(x-1) = \tan^{-1} 3$

We can group the terms as follows:

$\left[ \tan^{-1}(x+1) + \tan^{-1}(x-1) \right] + \tan^{-1} x = \tan^{-1} 3$

Using the formula $\tan^{-1} A + \tan^{-1} B = \tan^{-1} \left( \dfrac{A+B}{1-AB} \right)$:

$\tan^{-1} \left( \dfrac{(x+1) + (x-1)}{1 - (x+1)(x-1)} \right) + \tan^{-1} x = \tan^{-1} 3$

$\tan^{-1} \left( \dfrac{2x}{1 - (x^2 - 1)} \right) + \tan^{-1} x = \tan^{-1} 3$

$\tan^{-1} \left( \dfrac{2x}{2 - x^2} \right) + \tan^{-1} x = \tan^{-1} 3$

Applying the addition formula again:

$\tan^{-1} \left( \dfrac{\dfrac{2x}{2-x^2} + x}{1 - \left(\dfrac{2x}{2-x^2}\right)x} \right) = \tan^{-1} 3$

$\dfrac{2x + 2x - x^3}{2 - x^2 - 2x^2} = 3$

$\dfrac{4x - x^3}{2 - 3x^2} = 3$

Cross-multiplying yields:

$4x - x^3 = 6 - 9x^2$

$x^3 - 9x^2 - 4x + 6 = 0$

By inspection, substituting $x = -1$:

$(-1)^3 - 9(-1)^2 - 4(-1) + 6 = -1 - 9 + 4 + 6 = 0$

Thus, $x = -1$ is a root. Factoring out $(x+1)$ gives:

$(x+1)(x^2 - 10x + 6) = 0$

The roots of the quadratic equation $x^2 - 10x + 6 = 0$ are:

$x = \dfrac{10 \pm \sqrt{100 - 24}}{2} = 5 \pm \sqrt{19}$

Since $\sqrt{19} \approx 4.36$, both of these roots are positive. We are given that $x < 0$, so the only valid root is $x = -1$.

Now, substituting $x = -1$ into the given expression:

$500 x^4 + 270 x^2 + 997 = 500(-1)^4 + 270(-1)^2 + 997$

$= 500(1) + 270(1) + 997$

$= 500 + 270 + 997 = 1767$

Answer: 1767

</details>

---

### Q16. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of solutions of
$\tan ^{-1}\left(x+\frac{2}{x}\right)-\tan ^{-1}\left(\frac{4}{x}\right)-\tan ^{-1}\left(x-\frac{2}{x}\right)=0$ are

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

The given equation can be rewritten as:

$\tan^{-1}\left(x+\dfrac{2}{x}\right) - \tan^{-1}\left(x-\dfrac{2}{x}\right) = \tan^{-1}\left(\dfrac{4}{x}\right)$

Using the formula $\tan^{-1}A - \tan^{-1}B = \tan^{-1}\left(\dfrac{A-B}{1+AB}\right)$, we get:

$\tan^{-1}\left(\dfrac{\left(x+\dfrac{2}{x}\right) - \left(x-\dfrac{2}{x}\right)}{1 + \left(x+\dfrac{2}{x}\right)\left(x-\dfrac{2}{x}\right)}\right) = \tan^{-1}\left(\dfrac{4}{x}\right)$

$\tan^{-1}\left(\dfrac{\dfrac{4}{x}}{1 + x^2 - \dfrac{4}{x^2}}\right) = \tan^{-1}\left(\dfrac{4}{x}\right)$

Equating the arguments of the inverse tangent functions:

$\dfrac{\dfrac{4}{x}}{1 + x^2 - \dfrac{4}{x^2}} = \dfrac{4}{x}$

Since $x \neq 0$, we can divide both sides by $\dfrac{4}{x}$:

$\dfrac{1}{1 + x^2 - \dfrac{4}{x^2}} = 1$

$1 + x^2 - \dfrac{4}{x^2} = 1$

$x^2 - \dfrac{4}{x^2} = 0$

$x^4 - 4 = 0$

$x^4 = 4$

Since $x$ is a real number, $x^2$ must be positive, so:

$x^2 = 2 \Rightarrow x = \pm \sqrt{2}$

Substituting $x = \pm \sqrt{2}$ back into the original equation verifies that both are valid solutions. Thus, there are $2$ solutions.

Answer: $2$

</details>

---

### Q17. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin ^{-1} \frac{1}{3}+\sin ^{-1} \frac{3}{5}+\sin ^{-1} x=\frac{\pi}{2} \quad$ then $x=$

**Options:**

- **(A)** $\frac{8 \sqrt{2}+3}{5}$
- **(B)** $\frac{8 \sqrt{2}-3}{5}$
- **(C)** $\frac{8 \sqrt{2}+3}{15}$
- **(D)** $\frac{8 \sqrt{2}-3}{15}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{8 \sqrt{2}-3}{15}$**

**Detailed Solution:**

Given $\sin^{-1} \dfrac{1}{3} + \sin^{-1} \dfrac{3}{5} + \sin^{-1} x = \dfrac{\pi}{2}$

$\sin^{-1} x = \dfrac{\pi}{2} - \left(\sin^{-1} \dfrac{1}{3} + \sin^{-1} \dfrac{3}{5}\right)$

Taking sine on both sides:

$x = \sin\left[\dfrac{\pi}{2} - \left(\sin^{-1} \dfrac{1}{3} + \sin^{-1} \dfrac{3}{5}\right)\right]$

$x = \cos\left(\sin^{-1} \dfrac{1}{3} + \sin^{-1} \dfrac{3}{5}\right)$

Let $A = \sin^{-1} \dfrac{1}{3}$ and $B = \sin^{-1} \dfrac{3}{5}$

$\sin A = \dfrac{1}{3} \Rightarrow \cos A = \sqrt{1 - \left(\dfrac{1}{3}\right)^2} = \dfrac{2\sqrt{2}}{3}$

$\sin B = \dfrac{3}{5} \Rightarrow \cos B = \sqrt{1 - \left(\dfrac{3}{5}\right)^2} = \dfrac{4}{5}$

$x = \cos(A + B) = \cos A \cos B - \sin A \sin B$

$x = \left(\dfrac{2\sqrt{2}}{3}\right)\left(\dfrac{4}{5}\right) - \left(\dfrac{1}{3}\right)\left(\dfrac{3}{5}\right)$

$x = \dfrac{8\sqrt{2} - 3}{15}$

Answer: $\frac{8 \sqrt{2}-3}{15}$

</details>

---

### Q18. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan ^{-1}\left(\frac{x}{2}\right)+\tan ^{-1}\left(\frac{y}{2}\right)+\tan ^{-1}\left(\frac{z}{2}\right)=\frac{\pi}{2}$ then $x y+y z+z x=$

**Options:**

- **(A)** $0$
- **(B)** $2$
- **(C)** $-1$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4$**

**Detailed Solution:**

Given $\tan^{-1}\left(\dfrac{x}{2}\right) + \tan^{-1}\left(\dfrac{y}{2}\right) + \tan^{-1}\left(\dfrac{z}{2}\right) = \dfrac{\pi}{2}$

Let $\tan^{-1}\left(\dfrac{x}{2}\right) = A$, $\tan^{-1}\left(\dfrac{y}{2}\right) = B$, and $\tan^{-1}\left(\dfrac{z}{2}\right) = C$.

Then $A + B + C = \dfrac{\pi}{2}$

$A + B = \dfrac{\pi}{2} - C$

Taking $\tan$ on both sides:

$\tan(A + B) = \tan\left(\dfrac{\pi}{2} - C\right)$

$\dfrac{\tan A + \tan B}{1 - \tan A \tan B} = \cot C$

$\dfrac{\tan A + \tan B}{1 - \tan A \tan B} = \dfrac{1}{\tan C}$

$\tan A \tan C + \tan B \tan C = 1 - \tan A \tan B$

$\tan A \tan B + \tan B \tan C + \tan C \tan A = 1$

Substituting $\tan A = \dfrac{x}{2}$, $\tan B = \dfrac{y}{2}$, and $\tan C = \dfrac{z}{2}$:

$\left(\dfrac{x}{2}\right)\left(\dfrac{y}{2}\right) + \left(\dfrac{y}{2}\right)\left(\dfrac{z}{2}\right) + \left(\dfrac{z}{2}\right)\left(\dfrac{x}{2}\right) = 1$

$\dfrac{xy}{4} + \dfrac{yz}{4} + \dfrac{zx}{4} = 1$

$xy + yz + zx = 4$

Answer: $4$

</details>

---

### Q19. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\sin \left(\sin ^{-1} \frac{1}{5}+\cos ^{-1} x\right)=1$, then the value of $x$ is

**Options:**

- **(A)** $\frac{1}{5}$
- **(B)** $1$
- **(C)** $0$
- **(D)** $-\frac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{5}$**

**Detailed Solution:**

Given $\sin \left(\sin ^{-1} \dfrac{1}{5}+\cos ^{-1} x\right)=1$

$\Rightarrow \sin ^{-1} \dfrac{1}{5}+\cos ^{-1} x = \sin^{-1}(1)$

$\Rightarrow \sin ^{-1} \dfrac{1}{5}+\cos ^{-1} x = \dfrac{\pi}{2}$

Using the standard inverse trigonometric identity $\sin ^{-1} y + \cos ^{-1} y = \dfrac{\pi}{2}$, we get:

$x = \dfrac{1}{5}$

Answer: $\frac{1}{5}$

</details>

---

### Q20. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $a, b, c, r > 0$ and $a^2+b^2+c^2=r^2$, then the value of $\tan ^{-1}\left(\frac{a b}{c r}\right)+\tan ^{-1}\left(\frac{b c}{a r}\right)+\tan ^{-1}\left(\frac{c a}{b r}\right)=$

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{2}$**

**Detailed Solution:**

Let $x = \dfrac{ab}{cr}$, $y = \dfrac{bc}{ar}$, and $z = \dfrac{ca}{br}$.

The given expression is $\tan^{-1} x + \tan^{-1} y + \tan^{-1} z$.

Consider the sum of the products of these terms taken two at a time:

$xy + yz + zx = \left(\dfrac{ab}{cr} \times \dfrac{bc}{ar}\right) + \left(\dfrac{bc}{ar} \times \dfrac{ca}{br}\right) + \left(\dfrac{ca}{br} \times \dfrac{ab}{cr}\right)$

$xy + yz + zx = \dfrac{b^2}{r^2} + \dfrac{c^2}{r^2} + \dfrac{a^2}{r^2} = \dfrac{a^2 + b^2 + c^2}{r^2}$

Given that $a^2 + b^2 + c^2 = r^2$, we get:

$xy + yz + zx = \dfrac{r^2}{r^2} = 1$

For $x, y, z > 0$, if $xy + yz + zx = 1$, the sum of their inverse tangents is given by a standard identity:

$\tan^{-1} x + \tan^{-1} y + \tan^{-1} z = \dfrac{\pi}{2}$

Answer: $\frac{\pi}{2}$

</details>

---

### Q21. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan \mathrm{A}=\frac{1}{\sqrt{x\left(x^2+x+1\right)}}, \tan \mathrm{B}=\frac{\sqrt{x}}{\sqrt{x^2+x+1}}$ and $\tan \mathrm{C}=\sqrt{x^{-1}+x^{-2}+x^{-3}}$ then

**Options:**

- **(A)** $A+B=C$
- **(B)** $A+B=2 C$
- **(C)** $A+B=3 C$
- **(D)** $A+B=4 C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $A+B=C$**

**Detailed Solution:**

Given $\tan A = \dfrac{1}{\sqrt{x(x^2+x+1)}}$ and $\tan B = \dfrac{\sqrt{x}}{\sqrt{x^2+x+1}}$

$\tan(A+B) = \dfrac{\tan A + \tan B}{1 - \tan A \tan B}$

$\tan A + \tan B = \dfrac{1}{\sqrt{x(x^2+x+1)}} + \dfrac{\sqrt{x}}{\sqrt{x^2+x+1}} = \dfrac{1+x}{\sqrt{x(x^2+x+1)}}$

$\tan A \tan B = \dfrac{1}{\sqrt{x(x^2+x+1)}} \times \dfrac{\sqrt{x}}{\sqrt{x^2+x+1}} = \dfrac{1}{x^2+x+1}$

$1 - \tan A \tan B = 1 - \dfrac{1}{x^2+x+1} = \dfrac{x^2+x}{x^2+x+1} = \dfrac{x(x+1)}{x^2+x+1}$

$\tan(A+B) = \dfrac{\dfrac{1+x}{\sqrt{x(x^2+x+1)}}}{\dfrac{x(x+1)}{x^2+x+1}} = \dfrac{1+x}{\sqrt{x}\sqrt{x^2+x+1}} \times \dfrac{x^2+x+1}{x(x+1)} = \dfrac{\sqrt{x^2+x+1}}{x\sqrt{x}}$

Also given, $\tan C = \sqrt{x^{-1}+x^{-2}+x^{-3}} = \sqrt{\dfrac{1}{x} + \dfrac{1}{x^2} + \dfrac{1}{x^3}}$

$\tan C = \sqrt{\dfrac{x^2+x+1}{x^3}} = \dfrac{\sqrt{x^2+x+1}}{x\sqrt{x}}$

Therefore, $\tan(A+B) = \tan C$

$\Rightarrow A+B = C$

Answer: $A+B=C$

</details>

---

### Q22. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\tan ^{-1}(-\sqrt{3})-\sin ^{-1}\left(\frac{1}{\sqrt{2}}\right)+\cos ^{-1}\left(\frac{-1}{2}\right)$ is

**Options:**

- **(A)** $\frac{-\pi}{4}$
- **(B)** $\frac{4 \pi}{3}$
- **(C)** $\frac{\pi}{12}$
- **(D)** $\frac{7 \pi}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{12}$**

**Detailed Solution:**

The principal value branch of $\tan^{-1}x$ is $\left(\dfrac{-\pi}{2}, \dfrac{\pi}{2}\right)$.
$\tan^{-1}(-\sqrt{3}) = \dfrac{-\pi}{3}$

The principal value branch of $\sin^{-1}x$ is $\left[\dfrac{-\pi}{2}, \dfrac{\pi}{2}\right]$.
$\sin^{-1}\left(\dfrac{1}{\sqrt{2}}\right) = \dfrac{\pi}{4}$

The principal value branch of $\cos^{-1}x$ is $[0, \pi]$.
$\cos^{-1}\left(\dfrac{-1}{2}\right) = \pi - \cos^{-1}\left(\dfrac{1}{2}\right) = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$

Substituting these values into the given expression:
$\tan^{-1}(-\sqrt{3}) - \sin^{-1}\left(\dfrac{1}{\sqrt{2}}\right) + \cos^{-1}\left(\dfrac{-1}{2}\right)$

$= \dfrac{-\pi}{3} - \dfrac{\pi}{4} + \dfrac{2\pi}{3}$

$= \left(\dfrac{2\pi}{3} - \dfrac{\pi}{3}\right) - \dfrac{\pi}{4}$

$= \dfrac{\pi}{3} - \dfrac{\pi}{4}$

$= \dfrac{4\pi - 3\pi}{12}$

$= \dfrac{\pi}{12}$

Answer: $\frac{\pi}{12}$

</details>

---

### Q23. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\tan ^{-1}\left(\frac{x+1}{x-1}\right)+\tan ^{-1}\left(\frac{x-1}{x}\right)=\pi+\tan ^{-1}(-7)$, then $x$ is equal to

**Options:**

- **(A)** -1
- **(B)** 1
- **(C)** 2
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

Taking tangent on both sides of the given equation:

$\tan\left(\tan^{-1}\left(\dfrac{x+1}{x-1}\right) + \tan^{-1}\left(\dfrac{x-1}{x}\right)\right) = \tan(\pi + \tan^{-1}(-7))$

Using the formula $\tan(A+B) = \dfrac{\tan A + \tan B}{1 - \tan A \tan B}$ and $\tan(\pi + \theta) = \tan \theta$:

$\dfrac{\dfrac{x+1}{x-1} + \dfrac{x-1}{x}}{1 - \left(\dfrac{x+1}{x-1}\right)\left(\dfrac{x-1}{x}\right)} = -7$

Simplifying the numerator and the denominator:

$\dfrac{\dfrac{x(x+1) + (x-1)^2}{x(x-1)}}{\dfrac{x(x-1) - (x^2-1)}{x(x-1)}} = -7$

$\dfrac{x^2 + x + x^2 - 2x + 1}{x^2 - x - x^2 + 1} = -7$

$\dfrac{2x^2 - x + 1}{1 - x} = -7$

$2x^2 - x + 1 = -7(1 - x)$

$2x^2 - x + 1 = -7 + 7x$

$2x^2 - 8x + 8 = 0$

$x^2 - 4x + 4 = 0$

$(x - 2)^2 = 0 \Rightarrow x = 2$

For $x = 2$, $\dfrac{x+1}{x-1} = 3 > 0$ and $\dfrac{x-1}{x} = \dfrac{1}{2} > 0$. Since their product is $\dfrac{3}{2} > 1$, the sum $\tan^{-1}(3) + \tan^{-1}\left(\dfrac{1}{2}\right)$ correctly evaluates to $\pi + \tan^{-1}(-7)$, satisfying the original equation.

Answer: 2

</details>

---

### Q24. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\cos ^{-1}\left(\frac{12}{13}\right)+\sin ^{-1}\left(\frac{3}{5}\right)=\sin ^{-1} P$, then the value of $P$ is

**Options:**

- **(A)** $\frac{63}{65}$
- **(B)** $\frac{56}{65}$
- **(C)** $\frac{48}{65}$
- **(D)** $\frac{36}{65}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{56}{65}$**

**Detailed Solution:**

Let $\alpha = \cos^{-1}\left(\dfrac{12}{13}\right)$ and $\beta = \sin^{-1}\left(\dfrac{3}{5}\right)$

$\cos \alpha = \dfrac{12}{13} \Rightarrow \sin \alpha = \sqrt{1 - \left(\dfrac{12}{13}\right)^2} = \dfrac{5}{13}$

$\sin \beta = \dfrac{3}{5} \Rightarrow \cos \beta = \sqrt{1 - \left(\dfrac{3}{5}\right)^2} = \dfrac{4}{5}$

Given $\alpha + \beta = \sin^{-1} P$

$P = \sin(\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta$

$P = \left(\dfrac{5}{13}\right)\left(\dfrac{4}{5}\right) + \left(\dfrac{12}{13}\right)\left(\dfrac{3}{5}\right)$

$P = \dfrac{20}{65} + \dfrac{36}{65} = \dfrac{56}{65}$

Answer: $\frac{56}{65}$

</details>

---

### Q25. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\tan ^{-1}\left(\frac{1}{4}\right)+\tan ^{-1}\left(\frac{2}{9}\right)=\frac{1}{2} \cos ^{-1} x$, then $x$ is

**Options:**

- **(A)** $\frac{1}{5}$
- **(B)** $\frac{2}{5}$
- **(C)** $\frac{3}{5}$
- **(D)** $\frac{4}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{5}$**

**Detailed Solution:**

Using the formula $\tan^{-1} A + \tan^{-1} B = \tan^{-1}\left(\dfrac{A+B}{1-AB}\right)$ for $AB < 1$:

$\tan^{-1}\left(\dfrac{1}{4}\right) + \tan^{-1}\left(\dfrac{2}{9}\right) = \tan^{-1}\left(\dfrac{\dfrac{1}{4} + \dfrac{2}{9}}{1 - \dfrac{1}{4} \times \dfrac{2}{9}}\right)$

$= \tan^{-1}\left(\dfrac{\dfrac{17}{36}}{\dfrac{34}{36}}\right) = \tan^{-1}\left(\dfrac{1}{2}\right)$

Given that $\tan^{-1}\left(\dfrac{1}{2}\right) = \dfrac{1}{2} \cos^{-1} x$

$\Rightarrow \cos^{-1} x = 2 \tan^{-1}\left(\dfrac{1}{2}\right)$

Using the formula $2 \tan^{-1} y = \cos^{-1}\left(\dfrac{1-y^2}{1+y^2}\right)$ for $y \ge 0$:

$\cos^{-1} x = \cos^{-1}\left(\dfrac{1 - \left(\dfrac{1}{2}\right)^2}{1 + \left(\dfrac{1}{2}\right)^2}\right)$

$\cos^{-1} x = \cos^{-1}\left(\dfrac{1 - \dfrac{1}{4}}{1 + \dfrac{1}{4}}\right) = \cos^{-1}\left(\dfrac{\dfrac{3}{4}}{\dfrac{5}{4}}\right) = \cos^{-1}\left(\dfrac{3}{5}\right)$

$\Rightarrow x = \dfrac{3}{5}$

Answer: $\frac{3}{5}$

</details>

---

### Q26. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\sin \left(\cos ^{-1}\left(-\frac{1}{3}\right)-\sin ^{-1}\left(\frac{1}{3}\right)\right)$ is

**Options:**

- **(A)** 1
- **(B)** 3
- **(C)** 2
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Using the property of inverse trigonometric functions, $\cos^{-1}(-x) = \pi - \cos^{-1}(x)$.

The given expression becomes $\sin \left(\pi - \cos^{-1}\left(\dfrac{1}{3}\right) - \sin^{-1}\left(\dfrac{1}{3}\right)\right)$.

This can be written as $\sin \left(\pi - \left(\cos^{-1}\left(\dfrac{1}{3}\right) + \sin^{-1}\left(\dfrac{1}{3}\right)\right)\right)$.

Using the identity $\sin^{-1}(x) + \cos^{-1}(x) = \dfrac{\pi}{2}$, we get $\cos^{-1}\left(\dfrac{1}{3}\right) + \sin^{-1}\left(\dfrac{1}{3}\right) = \dfrac{\pi}{2}$.

Substituting this value, the expression becomes $\sin \left(\pi - \dfrac{\pi}{2}\right) = \sin \left(\dfrac{\pi}{2}\right)$.

The value of $\sin \left(\dfrac{\pi}{2}\right)$ is $1$.

Answer: 1

</details>

---

### Q27. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\cos \left[\sin ^{-1}\left(\frac{3}{5}\right)+\cos ^{-1}\left(\frac{12}{13}\right)\right]=$

**Options:**

- **(A)** $\frac{36}{65}$
- **(B)** $\frac{12}{65}$
- **(C)** $\frac{33}{65}$
- **(D)** $\frac{3}{65}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{33}{65}$**

**Detailed Solution:**

Let $A = \sin^{-1}\left(\dfrac{3}{5}\right)$ and $B = \cos^{-1}\left(\dfrac{12}{13}\right)$.

Then $\sin A = \dfrac{3}{5}$ and $\cos B = \dfrac{12}{13}$.

Since $A$ and $B$ lie in the first quadrant, we have:

$\cos A = \sqrt{1 - \sin^2 A} = \sqrt{1 - \left(\dfrac{3}{5}\right)^2} = \dfrac{4}{5}$

$\sin B = \sqrt{1 - \cos^2 B} = \sqrt{1 - \left(\dfrac{12}{13}\right)^2} = \dfrac{5}{13}$

We need to find $\cos(A + B)$. Using the trigonometric identity:

$\cos(A + B) = \cos A \cos B - \sin A \sin B$

Substituting the values:

$\cos(A + B) = \left(\dfrac{4}{5}\right)\left(\dfrac{12}{13}\right) - \left(\dfrac{3}{5}\right)\left(\dfrac{5}{13}\right)$

$\cos(A + B) = \dfrac{48}{65} - \dfrac{15}{65} = \dfrac{33}{65}$

Answer: $\frac{33}{65}$

</details>

---

### Q28. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\tan ^{-1}\left\{\frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}\right\}+\frac{1}{2} \cos ^{-1} x$ is

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{\pi}{4}$
- **(C)** 0
- **(D)** $\frac{\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{4}$**

**Detailed Solution:**

Let $x = \cos 2\theta$, where $\theta \in \left[0, \dfrac{\pi}{2}\right]$.

Then $\sqrt{1+x} = \sqrt{1+\cos 2\theta} = \sqrt{2\cos^2\theta} = \sqrt{2}\cos\theta$

And $\sqrt{1-x} = \sqrt{1-\cos 2\theta} = \sqrt{2\sin^2\theta} = \sqrt{2}\sin\theta$

Substituting these into the given expression:

$\tan^{-1}\left\{\dfrac{\sqrt{2}\cos\theta - \sqrt{2}\sin\theta}{\sqrt{2}\cos\theta + \sqrt{2}\sin\theta}\right\} + \dfrac{1}{2} \cos^{-1}(\cos 2\theta)$

$= \tan^{-1}\left\{\dfrac{\cos\theta - \sin\theta}{\cos\theta + \sin\theta}\right\} + \theta$

Dividing the numerator and denominator by $\cos\theta$:

$= \tan^{-1}\left\{\dfrac{1 - \tan\theta}{1 + \tan\theta}\right\} + \theta$

$= \tan^{-1}\left\{\tan\left(\dfrac{\pi}{4} - \theta\right)\right\} + \theta$

$= \dfrac{\pi}{4} - \theta + \theta$

$= \dfrac{\pi}{4}$

Answer: $\frac{\pi}{4}$

</details>

---

### Q29. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan ^{-1}(x+2)+\tan ^{-1}(x-2)-\tan ^{-1}\left(\dfrac{1}{2}\right)=0$, then one value of $x$ is

**Options:**

- **(A)** -1
- **(B)** $\dfrac{1}{2}$
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

The given equation can be written as:

$\tan^{-1}(x+2) + \tan^{-1}(x-2) = \tan^{-1}\left(\dfrac{1}{2}\right)$

Taking $\tan$ on both sides, we get:

$\dfrac{(x+2) + (x-2)}{1 - (x+2)(x-2)} = \dfrac{1}{2}$

$\dfrac{2x}{1 - (x^2 - 4)} = \dfrac{1}{2}$

$\dfrac{2x}{5 - x^2} = \dfrac{1}{2}$

$4x = 5 - x^2$

$x^2 + 4x - 5 = 0$

$(x+5)(x-1) = 0$

$x = 1$ or $x = -5$

For $x = -5$, the LHS of the original equation becomes $\tan^{-1}(-3) + \tan^{-1}(-7)$, which is negative, whereas the RHS is positive. Thus, $x = -5$ is rejected.

For $x = 1$, $\tan^{-1}(3) + \tan^{-1}(-1) = \tan^{-1}(3) - \dfrac{\pi}{4} > 0$, which satisfies the equation.

Therefore, $x = 1$.

Answer: 1

</details>

---

### Q30. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\cos \left(2 \cos ^{-1} x+\sin ^{-1} x\right)$ at $x=\dfrac{1}{5}$ is

**Options:**

- **(A)** $-\dfrac{\sqrt{6}}{5}$
- **(B)** $\dfrac{2 \sqrt{6}}{5}$
- **(C)** $-\dfrac{2 \sqrt{6}}{5}$
- **(D)** $\dfrac{2 \sqrt{5}}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\dfrac{2 \sqrt{6}}{5}$**

**Detailed Solution:**

Given expression is $\cos \left(2 \cos ^{-1} x+\sin ^{-1} x\right)$

This can be written as $\cos \left(\cos ^{-1} x + \cos ^{-1} x + \sin ^{-1} x\right)$

Using the inverse trigonometric identity $\cos ^{-1} x + \sin ^{-1} x = \dfrac{\pi}{2}$, we get:

$\cos \left(\cos ^{-1} x + \dfrac{\pi}{2}\right)$

Using the trigonometric identity $\cos \left(\dfrac{\pi}{2} + \theta\right) = -\sin \theta$, the expression becomes:

$-\sin \left(\cos ^{-1} x\right)$

Since $\sin \left(\cos ^{-1} x\right) = \sqrt{1 - x^2}$, we have:

$-\sqrt{1 - x^2}$

Substituting $x = \dfrac{1}{5}$:

$-\sqrt{1 - \left(\dfrac{1}{5}\right)^2}$

$-\sqrt{1 - \dfrac{1}{25}}$

$-\sqrt{\dfrac{24}{25}}$

$-\dfrac{2 \sqrt{6}}{5}$

Answer: $-\dfrac{2 \sqrt{6}}{5}$

</details>

---

### Q31. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\tan \left(\cos ^{-1} \dfrac{1}{\sqrt{2}}+\tan ^{-1} \dfrac{1}{2}\right)=$

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

The given expression is $\tan \left(\cos ^{-1} \dfrac{1}{\sqrt{2}}+\tan ^{-1} \dfrac{1}{2}\right)$

We know that $\cos ^{-1} \dfrac{1}{\sqrt{2}} = \dfrac{\pi}{4}$

Substituting this in the expression, we get $\tan \left(\dfrac{\pi}{4} + \tan ^{-1} \dfrac{1}{2}\right)$

Let $\tan ^{-1} \dfrac{1}{2} = \theta \Rightarrow \tan \theta = \dfrac{1}{2}$

The expression becomes $\tan \left(\dfrac{\pi}{4} + \theta\right)$

Using the identity $\tan(A + B) = \dfrac{\tan A + \tan B}{1 - \tan A \tan B}$

$\tan \left(\dfrac{\pi}{4} + \theta\right) = \dfrac{\tan \dfrac{\pi}{4} + \tan \theta}{1 - \tan \dfrac{\pi}{4} \tan \theta}$

Substituting $\tan \dfrac{\pi}{4} = 1$ and $\tan \theta = \dfrac{1}{2}$

$= \dfrac{1 + \dfrac{1}{2}}{1 - (1) \left(\dfrac{1}{2}\right)} = \dfrac{\dfrac{3}{2}}{\dfrac{1}{2}} = 3$

Answer: 3

</details>

---

### Q32. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\cos ^{-1} x+\cos ^{-1} y+\cos ^{-1} z=\pi$ and $x^2+y^2+z^2+k x y z=1$, then k is

**Options:**

- **(A)** -1
- **(B)** 1
- **(C)** -2
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

Let $\cos^{-1} x = A$, $\cos^{-1} y = B$, $\cos^{-1} z = C$.

Then $A + B + C = \pi$ and $x = \cos A$, $y = \cos B$, $z = \cos C$.

Consider the expression $x^2 + y^2 + z^2$:

$x^2 + y^2 + z^2 = \cos^2 A + \cos^2 B + \cos^2 C$

$= \cos^2 A + \dfrac{1 + \cos 2B}{2} + \dfrac{1 + \cos 2C}{2}$

$= 1 + \cos^2 A + \dfrac{\cos 2B + \cos 2C}{2}$

$= 1 + \cos^2 A + \cos(B+C) \cos(B-C)$

Since $A + B + C = \pi$, we have $\cos(B+C) = \cos(\pi - A) = -\cos A$.

Substituting this, we get:

$= 1 + \cos^2 A - \cos A \cos(B-C)$

$= 1 + \cos A (\cos A - \cos(B-C))$

Again using $\cos A = -\cos(B+C)$:

$= 1 - \cos A (\cos(B+C) + \cos(B-C))$

$= 1 - \cos A (2 \cos B \cos C)$

$= 1 - 2 \cos A \cos B \cos C$

$= 1 - 2xyz$

Therefore, $x^2 + y^2 + z^2 + 2xyz = 1$.

Comparing this with the given equation $x^2 + y^2 + z^2 + kxyz = 1$, we get $k = 2$.

Answer: 2

</details>

---

### Q33. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\tan ^{-1}\left(\tan \dfrac{7 \pi}{6}\right)$ is

**Options:**

- **(A)** $\dfrac{-\pi}{6}$
- **(B)** $\dfrac{\pi}{6}$
- **(C)** $\dfrac{-\pi}{3}$
- **(D)** $\dfrac{\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\pi}{6}$**

**Detailed Solution:**

The principal value branch of $\tan^{-1} x$ is $\left(\dfrac{-\pi}{2}, \dfrac{\pi}{2}\right)$.

We can write $\dfrac{7\pi}{6}$ as $\pi + \dfrac{\pi}{6}$.

$\tan^{-1}\left(\tan \dfrac{7\pi}{6}\right) = \tan^{-1}\left(\tan \left(\pi + \dfrac{\pi}{6}\right)\right)$

Since $\tan(\pi + \theta) = \tan \theta$, we get:

$\tan^{-1}\left(\tan \dfrac{\pi}{6}\right)$

Since $\dfrac{\pi}{6} \in \left(\dfrac{-\pi}{2}, \dfrac{\pi}{2}\right)$, the value is $\dfrac{\pi}{6}$.

Answer: $\dfrac{\pi}{6}$

</details>

---

### Q34. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$2 \pi-\left(\sin ^{-1} \dfrac{4}{5}+\sin ^{-1} \dfrac{5}{13}+\sin ^{-1} \dfrac{16}{65}\right)$ is equal to

**Options:**

- **(A)** $\dfrac{\pi}{2}$
- **(B)** $\dfrac{5 \pi}{4}$
- **(C)** $\dfrac{7 \pi}{4}$
- **(D)** $\dfrac{3 \pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{3 \pi}{2}$**

**Detailed Solution:**

Let $x = \sin^{-1} \dfrac{4}{5}$ and $y = \sin^{-1} \dfrac{5}{13}$.

Then $\sin x = \dfrac{4}{5} \Rightarrow \cos x = \dfrac{3}{5}$ and $\sin y = \dfrac{5}{13} \Rightarrow \cos y = \dfrac{12}{13}$.

Now, $\cos(x + y) = \cos x \cos y - \sin x \sin y$

$\cos(x + y) = \dfrac{3}{5} \times \dfrac{12}{13} - \dfrac{4}{5} \times \dfrac{5}{13} = \dfrac{36 - 20}{65} = \dfrac{16}{65}$.

Since $\cos(x + y) > 0$ and $x, y \in \left(0, \dfrac{\pi}{2}\right)$, we have $x + y \in \left(0, \dfrac{\pi}{2}\right)$.

Thus, $x + y = \cos^{-1} \dfrac{16}{65}$.

The given expression becomes $2 \pi - \left(x + y + \sin^{-1} \dfrac{16}{65}\right)$.

Substituting $x + y = \cos^{-1} \dfrac{16}{65}$, we get:

$2 \pi - \left(\cos^{-1} \dfrac{16}{65} + \sin^{-1} \dfrac{16}{65}\right)$

Using the identity $\sin^{-1} \theta + \cos^{-1} \theta = \dfrac{\pi}{2}$, the expression simplifies to:

$2 \pi - \dfrac{\pi}{2} = \dfrac{3 \pi}{2}$.

Answer: $\dfrac{3 \pi}{2}$

</details>

---

### Q35. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\cos ^{-1}\left\{\dfrac{1}{\sqrt{2}}\left(\cos \dfrac{9 \pi}{10}-\sin \dfrac{9 \pi}{10}\right)\right\}$ is

**Options:**

- **(A)** $\dfrac{7 \pi}{20}$
- **(B)** $\dfrac{13 \pi}{20}$
- **(C)** $\dfrac{17 \pi}{20}$
- **(D)** $\dfrac{21 \pi}{20}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{17 \pi}{20}$**

**Detailed Solution:**

The given expression is $\cos^{-1}\left\{\dfrac{1}{\sqrt{2}}\left(\cos \dfrac{9 \pi}{10}-\sin \dfrac{9 \pi}{10}\right)\right\}$

This can be rewritten using the trigonometric identity $\cos A \cos B - \sin A \sin B = \cos(A+B)$:

$\cos^{-1}\left\{\cos \dfrac{\pi}{4} \cos \dfrac{9 \pi}{10} - \sin \dfrac{\pi}{4} \sin \dfrac{9 \pi}{10}\right\}$

$= \cos^{-1}\left\{\cos \left(\dfrac{\pi}{4} + \dfrac{9 \pi}{10}\right)\right\}$

$= \cos^{-1}\left\{\cos \left(\dfrac{5 \pi + 18 \pi}{20}\right)\right\}$

$= \cos^{-1}\left\{\cos \left(\dfrac{23 \pi}{20}\right)\right\}$

The principal value branch of $\cos^{-1} x$ is $[0, \pi]$. Since $\dfrac{23 \pi}{20}$ does not lie in this interval, we use the property $\cos(2\pi - \theta) = \cos \theta$:

$\cos \left(\dfrac{23 \pi}{20}\right) = \cos \left(2\pi - \dfrac{23 \pi}{20}\right) = \cos \left(\dfrac{17 \pi}{20}\right)$

Substituting this back into the expression:

$= \cos^{-1}\left\{\cos \left(\dfrac{17 \pi}{20}\right)\right\}$

Since $\dfrac{17 \pi}{20} \in [0, \pi]$, we get:

$= \dfrac{17 \pi}{20}$

Answer: $\dfrac{17 \pi}{20}$

</details>

---

### Q36. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\cos ^{-1} x+\cos ^{-1} y+\cos ^{-1} z=3 \pi$, then the value of $x^2+y^2+z^2-2 x y z$ is

**Options:**

- **(A)** 3
- **(B)** 2
- **(C)** 1
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 5**

**Detailed Solution:**

The principal value branch of $\cos^{-1} \theta$ has the range $[0, \pi]$.

Given $\cos^{-1} x + \cos^{-1} y + \cos^{-1} z = 3\pi$.

Since the maximum value of the inverse cosine function is $\pi$, the sum can be $3\pi$ if and only if each term is equal to its maximum value.

$\cos^{-1} x = \pi \Rightarrow x = -1$

$\cos^{-1} y = \pi \Rightarrow y = -1$

$\cos^{-1} z = \pi \Rightarrow z = -1$

Substituting the values of $x$, $y$, and $z$ into the given expression:

$x^2 + y^2 + z^2 - 2xyz = (-1)^2 + (-1)^2 + (-1)^2 - 2(-1)(-1)(-1)$

$= 1 + 1 + 1 - 2(-1)$

$= 3 + 2 = 5$

Answer: 5

</details>

---

### Q37. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\cot ^{-1}(7)+\cot ^{-1}(8)+\cot ^{-1}(18)=\cot ^{-1} x$, then the value of $x$ is

**Options:**

- **(A)** $\dfrac{1}{3}$
- **(B)** 2
- **(C)** 3
- **(D)** $\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

Using the formula $\cot^{-1} a + \cot^{-1} b = \cot^{-1} \left( \dfrac{ab - 1}{a + b} \right)$ for $a, b > 0$:

$\cot^{-1}(7) + \cot^{-1}(8) = \cot^{-1} \left( \dfrac{7 \times 8 - 1}{7 + 8} \right)$

$= \cot^{-1} \left( \dfrac{55}{15} \right) = \cot^{-1} \left( \dfrac{11}{3} \right)$

Now, adding the third term:

$\cot^{-1} \left( \dfrac{11}{3} \right) + \cot^{-1}(18) = \cot^{-1} \left( \dfrac{\dfrac{11}{3} \times 18 - 1}{\dfrac{11}{3} + 18} \right)$

$= \cot^{-1} \left( \dfrac{66 - 1}{\dfrac{11 + 54}{3}} \right)$

$= \cot^{-1} \left( \dfrac{65}{\dfrac{65}{3}} \right) = \cot^{-1}(3)$

Given that this equals $\cot^{-1} x$, we have $x = 3$.

Answer: 3

</details>

---

### Q38. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\dfrac{\tan ^{-1}(\sqrt{3})-\sec ^{-1}(-2)}{\operatorname{cosec}^{-1}(-\sqrt{2})+\cos ^{-1}\left(\dfrac{-1}{2}\right)}$ is

**Options:**

- **(A)** $\dfrac{4}{5}$
- **(B)** $\dfrac{-4}{5}$
- **(C)** $\dfrac{3}{5}$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{-4}{5}$**

**Detailed Solution:**

The principal value of $\tan^{-1}(\sqrt{3})$ is $\dfrac{\pi}{3}$.

The principal value of $\sec^{-1}(-2)$ is $\pi - \sec^{-1}(2) = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$.

The principal value of $\operatorname{cosec}^{-1}(-\sqrt{2})$ is $-\dfrac{\pi}{4}$.

The principal value of $\cos^{-1}\left(\dfrac{-1}{2}\right)$ is $\pi - \cos^{-1}\left(\dfrac{1}{2}\right) = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$.

Substituting these values into the given expression:

Numerator $= \dfrac{\pi}{3} - \dfrac{2\pi}{3} = -\dfrac{\pi}{3}$

Denominator $= -\dfrac{\pi}{4} + \dfrac{2\pi}{3} = \dfrac{-3\pi + 8\pi}{12} = \dfrac{5\pi}{12}$

Expression value $= \dfrac{-\dfrac{\pi}{3}}{\dfrac{5\pi}{12}} = -\dfrac{\pi}{3} \times \dfrac{12}{5\pi} = -\dfrac{4}{5}$

Answer: $\dfrac{-4}{5}$

</details>

---

### Q39. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of real solutions of $\tan ^{-1} \sqrt{x(x+1)}+\sin ^{-1} \sqrt{x^2+x+1}=\dfrac{\pi}{2}$ is

**Options:**

- **(A)** one
- **(B)** zero
- **(C)** two
- **(D)** infinite

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) two**

**Detailed Solution:**

Let $y = x^2+x$.

The given equation can be written as $\tan^{-1} \sqrt{y} + \sin^{-1} \sqrt{y+1} = \dfrac{\pi}{2}$.

For the term $\tan^{-1} \sqrt{y}$ to be defined, we must have $y \ge 0$.

For the term $\sin^{-1} \sqrt{y+1}$ to be defined, the argument must lie in the domain of the inverse sine function, which gives $0 \le \sqrt{y+1} \le 1$.

Squaring all parts yields $0 \le y+1 \le 1$, which simplifies to $-1 \le y \le 0$.

The only value of $y$ satisfying both $y \ge 0$ and $y \le 0$ is $y = 0$.

Substituting $y = 0$ into the original equation gives $\tan^{-1} 0 + \sin^{-1} 1 = 0 + \dfrac{\pi}{2} = \dfrac{\pi}{2}$, which satisfies the equation.

Therefore, $x^2+x = 0$.

$x(x+1) = 0 \Rightarrow x = 0$ or $x = -1$.

Thus, there are two real solutions.

Answer: two

</details>

---

### Q40. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\tan \left(\dfrac{\pi}{4}+\dfrac{1}{2} \cos ^{-1}\left(\dfrac{\mathrm{a}}{\mathrm{b}}\right)\right)+\tan \left(\dfrac{\pi}{4}-\dfrac{1}{2} \cos ^{-1}\left(\dfrac{\mathrm{a}}{\mathrm{b}}\right)\right)$ is

**Options:**

- **(A)** $\dfrac{2 \mathrm{a}}{\mathrm{b}}$
- **(B)** $\dfrac{2 \mathrm{~b}}{\mathrm{a}}$
- **(C)** $\dfrac{\mathrm{a}}{\mathrm{b}}$
- **(D)** $\dfrac{\mathrm{b}}{\mathrm{a}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{2 \mathrm{~b}}{\mathrm{a}}$**

**Detailed Solution:**

Let $\theta = \dfrac{1}{2} \cos^{-1}\left(\dfrac{\mathrm{a}}{\mathrm{b}}\right)$

$\Rightarrow \cos 2\theta = \dfrac{\mathrm{a}}{\mathrm{b}}$

The given expression becomes:

$\tan \left(\dfrac{\pi}{4}+\theta\right) + \tan \left(\dfrac{\pi}{4}-\theta\right)$

$= \dfrac{1+\tan\theta}{1-\tan\theta} + \dfrac{1-\tan\theta}{1+\tan\theta}$

$= \dfrac{(1+\tan\theta)^2 + (1-\tan\theta)^2}{(1-\tan\theta)(1+\tan\theta)}$

$= \dfrac{2(1+\tan^2\theta)}{1-\tan^2\theta}$

$= \dfrac{2}{\left(\dfrac{1-\tan^2\theta}{1+\tan^2\theta}\right)}$

$= \dfrac{2}{\cos 2\theta}$

Substituting $\cos 2\theta = \dfrac{\mathrm{a}}{\mathrm{b}}$:

$= \dfrac{2}{\left(\dfrac{\mathrm{a}}{\mathrm{b}}\right)} = \dfrac{2\mathrm{b}}{\mathrm{a}}$

Answer: $\dfrac{2 \mathrm{~b}}{\mathrm{a}}$

</details>

---

### Q41. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of real solutions of $\tan ^{-1} \sqrt{x(x+1)}+\sin ^{-1} \sqrt{x^2+x+1}=\dfrac{\pi}{2}$ is

**Options:**

- **(A)** zero.
- **(B)** one.
- **(C)** two.
- **(D)** infinite.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) two.**

**Detailed Solution:**

Let $y = x^2+x$.

The given equation becomes $\tan^{-1} \sqrt{y} + \sin^{-1} \sqrt{y+1} = \dfrac{\pi}{2}$.

For the terms to be defined, we must have $y \ge 0$ and $0 \le y+1 \le 1$.

The second condition simplifies to $-1 \le y \le 0$.

Combining $y \ge 0$ and $y \le 0$, the only possible value is $y = 0$.

Substituting $y = 0$ into the equation gives $\tan^{-1}(0) + \sin^{-1}(1) = 0 + \dfrac{\pi}{2} = \dfrac{\pi}{2}$, which satisfies the equation.

Thus, $x^2+x = 0 \Rightarrow x(x+1) = 0$.

This gives $x = 0$ or $x = -1$.

Therefore, there are two real solutions.

Answer: two.

</details>

---

### Q42. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\tan ^{-1}\left(\frac{1}{8}\right)+\tan ^{-1}\left(\frac{1}{2}\right)+\tan ^{-1}\left(\frac{1}{5}\right)$ is

**Options:**

- **(A)** $\frac{\pi}{6}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1}\left(\frac{1}{8}\right)+\tan ^{-1}\left(\frac{1}{2}\right)+\tan ^{-1}\left(\frac{1}{5}\right) \\ & =\tan ^{-1}\left(\frac{1}{8}\right)+\tan ^{-1}\left(\frac{\frac{1}{2}+\frac{1}{5}}{1-\frac{1}{2} \cdot \frac{1}{5}}\right) \\ & =\tan ^{-1}\left(\frac{1}{8}\right)+\tan ^{-1}\left(\frac{7}{9}\right) \\ & =\tan ^{-1}\left(\frac{\frac{1}{8}+\frac{7}{9}}{1-\frac{1}{8} \cdot \frac{7}{9}}\right) \\ & =\tan ^{-1}\left(\frac{\frac{72}{65}}{\frac{72}{9}}\right) \\ & =\tan ^{-1}(1) \\ & =\frac{\pi}{4}\end{aligned}$

</details>

---

### Q43. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\pi+\left(\sin ^{-1} \frac{4}{5}+\sin ^{-1} \frac{5}{13}+\sin ^{-1} \frac{16}{65}\right)$ is equal to

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{5 \pi}{4}$
- **(C)** $\frac{3 \pi}{2}$
- **(D)** $\frac{7 \pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3 \pi}{2}$**

**Detailed Solution:**

$\begin{aligned} & \pi+\left[\left(\sin ^{-1} \frac{4}{5}+\sin ^{-1} \frac{5}{13}\right)+\sin ^{-1} \frac{16}{65}\right] \\ & =\pi+\left[\left(\tan ^{-1} \frac{4}{3}+\tan ^{-1} \frac{5}{12}\right)+\sin ^{-1} \frac{16}{65}\right] \\ & =\pi+\left[\tan ^{-1}\left(\frac{\frac{4}{3}+\frac{5}{12}}{1-\frac{4}{3} \times \frac{5}{12}}\right)+\sin ^{-1} \frac{16}{65}\right] \\ & =\pi+\left[\tan ^{-1}\left(\frac{63}{16}\right)+\sin ^{-1}\left(\frac{16}{65}\right)\right] \\ & =\pi+\left[\cos ^{-1}\left(\frac{16}{65}\right)+\sin ^{-1}\left(\frac{16}{65}\right)\right] \\ & =\pi+\frac{\pi}{2} \\ & =\frac{3 \pi}{2}\end{aligned}$

</details>

---

### Q44. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\cos ^{-1} \sqrt{\mathrm{p}}+\cos ^{-1} \sqrt{1-\mathrm{p}}+\cos ^{-1} \sqrt{1-\mathrm{q}}=\frac{3 \pi}{4}$, then $\mathrm{q}$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{\sqrt{2}}$
- **(C)** $1$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

$\begin{aligned} & \cos ^{-1} \sqrt{\mathrm{p}}-\cos ^{-1} \sqrt{1-\mathrm{p}}+\cos ^{-1} \sqrt{1-\mathrm{q}}=\frac{3 \pi}{4} \\ & \text { Let } \mathrm{t}=\cos ^{-1} \sqrt{\mathrm{p}} \\ & \Rightarrow \mathrm{p}=\cos ^2 \mathrm{t} \\ & \Rightarrow \mathrm{p}=1-\sin ^2 \mathrm{t} \\ & \Rightarrow \sin \mathrm{t}=\sqrt{1-\mathrm{p}} \\ & \Rightarrow \mathrm{t}=\sin ^{-1} \sqrt{1-\mathrm{p}}\end{aligned}$
$\Rightarrow \cos ^{-1} \sqrt{\mathrm{p}}=\sin ^{-1} \sqrt{1-\mathrm{p}}$
$\therefore \quad$ Given equation becomes
$\sin ^{-1} \sqrt{1-p}-\cos ^{-1} \sqrt{1-p}+\cos ^{-1} \sqrt{1-q}=\frac{3 \pi}{4}$
$\therefore \quad \frac{\pi}{2}+\cos ^{-1} \sqrt{1-q}=\frac{3 \pi}{4} \quad \ldots\left[\because \cos ^{-1} a+\sin ^{-1} a=\frac{\pi}{2}\right]$
$\begin{array}{ll}\therefore & \cos ^{-1} \sqrt{1-q}=\frac{-\pi}{4} \\ \therefore & \sqrt{1-q}=\cos \left(-\frac{\pi}{4}\right) \\ \therefore & q=1-\frac{1}{2} \\ \therefore & q=\frac{1}{2}\end{array}$

</details>

---

### Q45. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $2 \tan ^{-1} \frac{1}{2}+\tan ^{-1} \frac{1}{7}$

**Options:**

- **(A)** $\tan ^{-1}\left(\frac{17}{31}\right)$
- **(B)** $\tan ^{-1}\left(\frac{19}{31}\right)$
- **(C)** $\tan ^{-1}\left(\frac{31}{17}\right)$
- **(D)** $\tan ^{-1}\left(\frac{31}{19}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\tan ^{-1}\left(\frac{31}{17}\right)$**

**Detailed Solution:**

$\begin{aligned} & 2 \tan ^{-1} \frac{1}{2}+\tan ^{-1} \frac{1}{7} \\ & =\tan ^{-1}\left(\frac{2\left(\frac{1}{2}\right)}{1-\left(\frac{1}{2}\right)^2}\right)+\tan ^{-1}\left(\frac{1}{7}\right) \\ & =\tan ^{-1}\left(\frac{4}{3}\right)+\tan ^{-1}\left(\frac{1}{7}\right) \\ & =\tan ^{-1}\left(\frac{\frac{4}{3}+\frac{1}{7}}{1-\left(\frac{4}{3}\right)\left(\frac{1}{7}\right)}\right) \\ & =\tan ^{-1}\left(\frac{31}{17}\right)\end{aligned}$

</details>

---

### Q46. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\tan ^{-1}(1)+\cos ^{-1}\left(-\frac{1}{2}\right)+\sin ^{-1}\left(-\frac{1}{2}\right)$ is

**Options:**

- **(A)** $\frac{5 \pi}{6}$
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{2 \pi}{3}$
- **(D)** $\frac{3 \pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3 \pi}{4}$**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1}(1)+\cos ^{-1}\left(\frac{-1}{2}\right)+\sin ^{-1}\left(\frac{-1}{2}\right) \\ & =\frac{\pi}{4}+\frac{2 \pi}{3}-\frac{\pi}{6} \\ & =\frac{3 \pi}{4}\end{aligned}$

</details>

---

### Q47. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Considering only the principal values of an inverse function, the set
$\mathrm{A}=\left\{x \geq 0 / \tan ^{-1} x+\tan ^{-1} 6 x=\frac{\pi}{4}\right\}$

**Options:**

- **(A)** is an empty set.
- **(B)** is a singleton set.
- **(C)** contains more than two elements.
- **(D)** contains two elements.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) is a singleton set.**

**Detailed Solution:**

Consider, $\tan ^{-1} x+\tan ^{-1} 6 x=\frac{\pi}{4}$
$\begin{aligned}
& \Rightarrow \tan ^{-1}\left(\frac{7 x}{1-6 x^2}\right)=\frac{\pi}{4} \\
& \quad \quad \ldots\left[\tan ^{-1}(x)+\tan ^{-1}(y)=\tan ^{-1}\left(\frac{x+y}{1-x y}\right)\right] \\
& \Rightarrow \frac{7 x}{1-6 x^2}=1 \\
& \Rightarrow 7 x=1-6 x^2 \\
& \Rightarrow 6 x^2+7 x-1=0 \\
& \Rightarrow x=\frac{-7 \pm \sqrt{73}}{12} \\
& \quad \text { Since } x \geq 0 \\
& \therefore \quad x=\frac{-7+\sqrt{73}}{12}
\end{aligned}$
$\therefore \quad$ A is a singleton set.

</details>

---

### Q48. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\tan \left(\cos ^{-1}\left(\frac{4}{5}\right)+\tan ^{-1}\left(\frac{2}{3}\right)\right)$ is

**Options:**

- **(A)** $\frac{6}{17}$
- **(B)** $\frac{7}{16}$
- **(C)** $\frac{16}{7}$
- **(D)** $\frac{17}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{17}{6}$**

**Detailed Solution:**

$\tan \left(\cos ^{-1} \frac{4}{5}+\tan ^{-1} \frac{2}{3}\right)=\tan \left(\tan ^{-1} \frac{3}{4}+\tan ^{-1} \frac{2}{3}\right)$
$=\tan \tan ^{-1}\left(\frac{\frac{3}{4}+\frac{2}{3}}{1-\frac{3}{4} \times \frac{2}{3}}\right)=\tan \tan ^{-1}\left(\frac{17}{6}\right)=\frac{17}{6}$

</details>

---

### Q49. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\tan \left[2 \tan ^{-1}\left(\frac{1}{5}\right)-\frac{\pi}{4}\right]$ is

**Options:**

- **(A)** $\frac{7}{17}$
- **(B)** $-\frac{7}{17}$
- **(C)** $-\frac{17}{7}$
- **(D)** $\frac{17}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{7}{17}$**

**Detailed Solution:**

$\begin{aligned} & 2 \tan ^{-1}\left(\frac{1}{5}\right)-\frac{\pi}{4}=\tan ^{-1} \frac{2 \times \frac{1}{5}}{1-\left(\frac{1}{5}\right)^2}-\tan ^{-1}(1)=\tan ^{-1} \frac{5}{12}-\tan ^{-1}(1) \\ & =\tan ^{-1}\left(\frac{\frac{5}{12}-1}{1+\frac{5}{12} \times 1}\right)=\tan ^{-1}\left(\frac{-7}{17}\right) \\ & \Rightarrow \tan \left\{2 \tan ^{-1} \frac{1}{5}-\frac{\pi}{4}\right\}=\frac{-7}{17}\end{aligned}$

</details>

---

### Q50. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\tan ^{-1} 2+\tan ^{-1} 3=$

**Options:**

- **(A)** $\frac{5 \pi}{4}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $-\frac{\pi}{4}$
- **(D)** $\frac{3 \pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3 \pi}{4}$**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1} 2+\tan ^{-1} 3=\pi+\tan ^{-1}\left(\frac{2+3}{1-2 \times 3}\right)=\pi+\tan ^{-1}\left(\frac{5}{-5}\right) \\ & =\pi+\tan ^{-1}(-1)=\pi-\frac{\pi}{4}=\frac{3 \pi}{4}\end{aligned}$

</details>

---

### Q51. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\tan ^{-1}\left(\frac{1}{3}\right)+\tan ^{-1}\left(\frac{1}{5}\right)+\tan ^{-1}\left(\frac{1}{7}\right)+\tan ^{-1}\left(\frac{1}{8}\right)$ is

**Options:**

- **(A)** $\frac{4 \pi}{3}$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{2 \pi}{4}$
- **(D)** $\frac{3 \pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1}\left(\frac{1}{3}\right)+\tan ^{-1}\left(\frac{1}{5}\right)+\tan ^{-1}\left(\frac{1}{7}\right)+\tan ^{-1}\left(\frac{1}{8}\right) \\ & =\tan ^{-1}\left(\frac{\frac{1}{3}+\frac{1}{5}}{1-\frac{1}{3} \times \frac{1}{5}}\right)+\tan ^{-1}\left(\frac{\frac{1}{7}+\frac{1}{8}}{1-\frac{1}{7} \times \frac{1}{8}}\right) \\ & =\tan ^{-1}\left(\frac{4}{7}\right)+\tan ^{-1}\left(\frac{3}{11}\right) \\ & =\tan ^{-1} \frac{\frac{4}{7}+\frac{3}{11}}{\left(1-\frac{4}{7} \times \frac{3}{11}\right)}=\tan ^{-1}\left(\frac{65}{65}\right)=\tan ^{-1}(1)=\frac{\pi}{4}\end{aligned}$

</details>

---

### Q52. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$2 \tan ^{-1}\left(\frac{1}{3}\right)+\cos ^{-1}\left(\frac{3}{5}\right)=$

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $0$
- **(C)** $\tan ^{-1}\left(\frac{5}{4}\right)$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{2}$**

**Detailed Solution:**

$\begin{aligned} & 2 \tan ^{-1}\left(\frac{1}{3}\right)+\cos ^{-1}\left(\frac{3}{5}\right)=\tan ^{-1} \frac{2 \times \frac{1}{3}}{1-\left(\frac{1}{3}\right)^2}+\cos ^{-1}\left(\frac{3}{5}\right) \\ & =\tan ^{-1}\left(\frac{\frac{2}{3}}{\frac{8}{9}}\right)+\cos ^{-1}\left(\frac{3}{5}\right) \\ & =\tan ^{-1}\left(\frac{3}{4}\right)+\cot ^{-1}\left(\frac{3}{4}\right) \\ & =\frac{\pi}{2}\end{aligned}$

</details>

---

### Q53. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\tan ^{-1} \frac{1}{3}+\tan ^{-1} \frac{1}{5}+\tan ^{-1} \frac{1}{7}+\tan ^{-1} \frac{1}{8}$ has the value

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $\frac{\pi}{2}$
- **(D)** $\frac{\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1} \frac{1}{3}+\tan ^{-1} \frac{1}{5}+\tan ^{-1} \frac{1}{7}+\tan ^{-1} \frac{1}{8} \\ & =\tan ^{-1}\left(\frac{\frac{1}{3}+\frac{1}{5}}{1-\frac{1}{3} \times \frac{1}{5}}\right)+\tan ^{-1}\left(\frac{\frac{1}{7}+\frac{1}{8}}{1-\frac{1}{7} \times \frac{1}{8}}\right) \\ & =\tan ^{-1}\left(\frac{4}{7}\right)+\tan ^{-1}\left(\frac{3}{11}\right) \\ & =\tan ^{-1}\left(\frac{\frac{4}{7}+\frac{3}{11}}{1-\frac{4}{7} \times \frac{3}{11}}\right)\end{aligned}$
$=\tan ^{-1}\left(\frac{65}{65}\right)=\tan ^{-1}(1)=\frac{\pi}{4}$

</details>

---

### Q54. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\tan ^{-1} 2+\tan ^{-1} 3$ is

**Options:**

- **(A)** $\left(\frac{3 \pi}{4}\right)^c$
- **(B)** $\left(\frac{\pi}{2}\right)^c$
- **(C)** $\left(\frac{\pi}{4}\right)^c$
- **(D)** $\left(\frac{\pi}{6}\right)^c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(\frac{3 \pi}{4}\right)^c$**

**Detailed Solution:**

$\begin{aligned} & \tan ^{-1} 2+\tan ^{-1} 3 \\ & =\tan ^{-1}\left[\frac{2+3}{1-(2)(3)}\right]=\tan ^{-1}\left(\frac{5}{1-6}\right)=\tan ^{-1}(-1)=\left(\frac{3 \pi}{4}\right)^c\end{aligned}$

</details>

---

### Q55. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\tan ^{-1}(2 x)+\tan ^{-1}(3 x)=\frac{\pi}{4}$, where $x>0$, then $x=$

**Options:**

- **(A)** 1
- **(B)** $\frac{1}{6}$
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{6}$**

**Detailed Solution:**

$$
\begin{aligned}
& \tan ^{-1}(2 x)+\tan ^{-1}(3 x)=\frac{\pi}{4} \\
& \therefore \tan ^{-1}\left[\frac{2 x+3 x}{1-(2 x)(3 x)}\right]=\frac{\pi}{4} \Rightarrow \tan \frac{\pi}{4}=\frac{5 x}{1-6 x^2}=1 \\
& \therefore 6 x^2+5 x-1=0 \Rightarrow(6 x-1)(x+1)=0 \Rightarrow x=-1, \frac{1}{6}
\end{aligned}
$$
Since $x>0$, we get $x=\frac{1}{6}$

</details>

---

### Q56. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\tan \left(\cos ^{-1}\left(\frac{4}{5}\right)+\tan ^{-1}\left(\frac{2}{3}\right)\right)=$

**Options:**

- **(A)** $\frac{17}{6}$
- **(B)** $\frac{17}{3}$
- **(C)** $\frac{18}{5}$
- **(D)** $\frac{7}{15}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{17}{6}$**

**Detailed Solution:**

$\begin{aligned} & \tan \left[\cos ^{-1}\left(\frac{4}{5}\right)+\tan ^{-1}\left(\frac{2}{3}\right)\right] \\ & =\tan \left[\tan ^{-1}\left(\frac{3}{4}\right)+\tan ^{-1}\left(\frac{2}{3}\right)\right]=\tan \left[\tan ^{-1}\left(\frac{\left(\frac{3}{4}\right)+\left(\frac{2}{3}\right)}{1-\left(\frac{3}{4}\right)+\left(\frac{2}{3}\right)}\right)\right] \\ & =\tan \left[\tan ^{-1}\left(\frac{17}{6}\right)\right]=\frac{17}{6}\end{aligned}$

</details>

---

### Q57. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\tan \left[\cos ^{-1}\left(\frac{4}{5}\right)+\tan ^{-1}\left(\frac{2}{3}\right)\right]$ is

**Options:**

- **(A)** $\frac{17}{6}$
- **(B)** $\frac{16}{7}$
- **(C)** $\frac{6}{17}$
- **(D)** $\frac{7}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{17}{6}$**

**Detailed Solution:**

The value of $\tan \left[\cos ^{-1}\left(\frac{4}{5}\right)+\tan ^{-1}\left(\frac{2}{3}\right)\right]$ is to be found out. Let $\quad \cos ^{-1}\left(\frac{4}{5}\right)=\theta \Rightarrow \cos \theta=\frac{4}{5} \Rightarrow \sin \theta=\frac{3}{5}$
$\therefore \tan \theta=\frac{3}{4} \Rightarrow \theta=\tan ^{-1}\left(\frac{3}{4}\right)$
Hence given expression.
$$
\begin{array}{l}
=\tan \left[\tan ^{-1}\left(\frac{3}{4}\right)+\tan ^{-1}\left(\frac{2}{3}\right)\right]=\tan \left[\tan ^{-1}\left(\frac{\frac{3}{4}+\frac{2}{3}}{1-\left(\frac{3}{4}\right)\left(\frac{2}{3}\right)}\right)\right] \\
=\tan \left[\tan ^{-1}\left(\frac{17}{6}\right)\right]=\frac{17}{6}
\end{array}
$$

</details>

---

### Q58. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin ^{-1} x+\sin ^{-1} \mathrm{y}+\sin ^{-1} \mathrm{z}=\frac{3 \pi}{2}, \quad$ then $x^{100}+\mathrm{y}^{100}+\mathrm{z}^{100}=$

**Options:**

- **(A)** $3$
- **(B)** $4$
- **(C)** $2$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3$**

**Detailed Solution:**

Given
$$
\begin{array}{l}
\sin ^{-1} x+\sin ^{-1} y+\sin ^{-1} z=\frac{3 \pi}{2} \Rightarrow \sin ^{-1} x=\sin ^{-1} y=\sin ^{-1} z=\frac{\pi}{2} \\
\therefore x=y=z=1 \\
\therefore x^{100}+y^{100}+z^{100}=1+1+1=3
\end{array}
$$

</details>

---

### Q59. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\tan ^{-1}\left(\frac{1}{3}\right)+\tan ^{-1}\left(\frac{1}{5}\right)+\tan ^{-1}\left(\frac{1}{7}\right)+\tan ^{-1}\left(\frac{1}{8}\right)$ is

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{\pi}{12}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{4}$**

**Detailed Solution:**

(D)
Point of intersection of $x=4$ and $3 x+2 y=18$ is $Q \equiv(4,3)$
Point of intersection of $y=6$ and $3 x+2 y=18$ is $P \equiv(2,6)$
Point $D \equiv(4,0)$ and $C \equiv(0,6)$ are as shown.
The feasible region of th given L.P.P. is shaded portion CPQ D O.
We have to maximize $\mathrm{Z}=3 \mathrm{x}+5 \mathrm{y}$.
Now,
$\begin{array}{ll}\mathrm{Z} \text { at } \mathrm{C}(0,6) & =3(0)+5(6)=30 \\ \mathrm{Z} \text { at } \mathrm{P}(2,6) & =3(2)+5(6)=36 \\ \mathrm{Z} \text { at } \mathrm{Q}(4,3) & =3(4)+5(3)=27 \\ \mathrm{Z} \text { at } \mathrm{D}(4,0) & =3(4)+5(0)=12 \\ \mathrm{Z} \text { at } \mathrm{O}(0,0) & =3(0)+5(0)=0\end{array}$
Clearly the maximum value of $Z$ is 36 at $P(2,6)$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/3tr57-rtaQK8CmgJrt3LRA0-IxuyXJ7PXw-_c0aOQsw.original.fullsize.png">

</details>

---

### Q60. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$2 \tan ^{-1}\left(\frac{1}{3}\right)-\tan ^{-1}\left(\frac{3}{4}\right)=$

**Options:**

- **(A)** $0$
- **(B)** $2$
- **(C)** $1$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0$**

**Detailed Solution:**

$\begin{aligned} 2 \tan ^{-1} \frac{1}{3} &=\tan ^{-1} \frac{1}{3}+\tan ^{-1} \frac{1}{3}=\tan ^{-1}\left(\frac{\frac{1}{3}+\frac{1}{3}}{1-\frac{1}{3} \times \frac{1}{3}}\right) \\ &=\tan ^{-1}\left(\frac{2}{3} \times \frac{9}{8}\right)=\tan ^{-1} \frac{3}{4} \\ \text { Now } 2 \tan ^{-1}\left(\frac{1}{3}\right)-\tan ^{-1}\left(\frac{3}{4}\right) &=\tan ^{-1}\left(\frac{3}{4}\right)-\tan ^{-1}\left(\frac{3}{4}\right)=0 \end{aligned}$

</details>

---

### Q61. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan ^{-1}\left(\frac{1-x}{1+x}\right)-\frac{1}{2} \tan ^{-1} x=0$, for $x>0$, then $x=$

**Options:**

- **(A)** $\sqrt{3}$
- **(B)** $\frac{1}{\sqrt{2}}$
- **(C)** $\frac{1}{\sqrt{3}}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{\sqrt{3}}$**

**Detailed Solution:**

Here $\tan ^{-1}\left(\frac{1-x}{1+x}\right)=\frac{1}{2} \tan ^{-1} x \Rightarrow \tan ^{-1}\left[\frac{1-x}{1+(1)(x)}\right]=\frac{1}{2} \tan ^{-1} x$
$\therefore \tan ^{-1}(1)-\tan ^{-1} x=\frac{1}{2} \tan ^{-1} x$
$\frac{\pi}{4}=\frac{3}{2} \tan ^{-1} x \Rightarrow \tan ^{-1} x=\frac{\pi}{4} \times \frac{2}{3} \Rightarrow \tan ^{-1} x=\frac{\pi}{6}$
$\therefore x=\tan \frac{\pi}{6}=\frac{1}{\sqrt{3}}$

</details>

---

