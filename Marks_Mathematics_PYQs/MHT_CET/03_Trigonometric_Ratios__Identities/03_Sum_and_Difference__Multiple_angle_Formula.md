# MHT CET Mathematics - Trigonometric Ratios & Identities

## Topic 3: Sum and Difference & Multiple angle Formula

**Total Questions:** 50

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle ABC$, with usual notations, if $\sin 2A + \sin 2B = \sin 2C$, then the type of the triangle is

**Options:**

- **(A)** Isosceles triangle
- **(B)** Equilateral triangle
- **(C)** Right angled triangle
- **(D)** Scalene triangle

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Right angled triangle**

**Detailed Solution:**

Given $\sin 2A + \sin 2B = \sin 2C$

Using the sum-to-product formula on the left side:

$2 \sin(A+B) \cos(A-B) = 2 \sin C \cos C$

Since $A+B+C = \pi$, we have $\sin(A+B) = \sin(\pi - C) = \sin C$. Substituting this into the equation:

$2 \sin C \cos(A-B) = 2 \sin C \cos C$

Since $C$ is an angle of a triangle, $0 < C < \pi$, which implies $\sin C \neq 0$. Dividing both sides by $2 \sin C$:

$\cos(A-B) = \cos C$

Using $C = \pi - (A+B)$, we get $\cos C = \cos(\pi - (A+B)) = -\cos(A+B)$.

$\cos(A-B) = -\cos(A+B)$

$\cos(A-B) + \cos(A+B) = 0$

Expanding the terms or using the sum-to-product formula:

$2 \cos A \cos B = 0$

This implies that either $\cos A = 0$ or $\cos B = 0$.

Since $A$ and $B$ are angles of a triangle, either $A = \dfrac{\pi}{2}$ or $B = \dfrac{\pi}{2}$.

Therefore, the triangle is a right-angled triangle.

Answer: Right angled triangle

</details>

---

### Q2. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the expression $\cos\left(\dfrac{\pi}{24}\right)\cos\left(\dfrac{\pi}{12}\right)\cos\left(\dfrac{\pi}{6}\right)\cos\left(\dfrac{\pi}{3}\right)$ is:

**Options:**

- **(A)** $\dfrac{1}{16}\sin\left(\dfrac{\pi}{24}\right)$
- **(B)** $\dfrac{\sqrt{3}}{32}\csc\left(\dfrac{\pi}{24}\right)$
- **(C)** $\dfrac{\sqrt{3}}{16}$
- **(D)** $\dfrac{1}{32}\sec\left(\dfrac{\pi}{12}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\sqrt{3}}{32}\csc\left(\dfrac{\pi}{24}\right)$**

**Detailed Solution:**

Let $E = \cos\left(\dfrac{\pi}{24}\right)\cos\left(\dfrac{\pi}{12}\right)\cos\left(\dfrac{\pi}{6}\right)\cos\left(\dfrac{\pi}{3}\right)$

This can be rewritten as:

$E = \cos\left(\dfrac{\pi}{24}\right)\cos\left(2 \times \dfrac{\pi}{24}\right)\cos\left(2^2 \times \dfrac{\pi}{24}\right)\cos\left(2^3 \times \dfrac{\pi}{24}\right)$

Using the standard trigonometric identity $\cos A \cos 2A \cos 2^2A \dots \cos 2^{n-1}A = \dfrac{\sin(2^n A)}{2^n \sin A}$

Here $A = \dfrac{\pi}{24}$ and $n = 4$. Substituting these values, we get:

$E = \dfrac{\sin\left(2^4 \times \dfrac{\pi}{24}\right)}{2^4 \sin\left(\dfrac{\pi}{24}\right)}$

$E = \dfrac{\sin\left(\dfrac{16\pi}{24}\right)}{16 \sin\left(\dfrac{\pi}{24}\right)}$

$E = \dfrac{\sin\left(\dfrac{2\pi}{3}\right)}{16 \sin\left(\dfrac{\pi}{24}\right)}$

Since $\sin\left(\dfrac{2\pi}{3}\right) = \dfrac{\sqrt{3}}{2}$:

$E = \dfrac{\dfrac{\sqrt{3}}{2}}{16 \sin\left(\dfrac{\pi}{24}\right)}$

$E = \dfrac{\sqrt{3}}{32} \csc\left(\dfrac{\pi}{24}\right)$

Answer: $\dfrac{\sqrt{3}}{32}\csc\left(\dfrac{\pi}{24}\right)$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In $\Delta ABC$, $\angle C = \dfrac{2\pi}{3}$, then the value of $\cos^2 A + \cos^2 B - \cos A \cos B$ is

**Options:**

- **(A)** $\dfrac{1}{4}$
- **(B)** $\dfrac{3}{4}$
- **(C)** $\dfrac{5}{4}$
- **(D)** $\dfrac{7}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3}{4}$**

**Detailed Solution:**

Given $A + B + C = \pi$ and $C = \dfrac{2\pi}{3}$, we have $A + B = \dfrac{\pi}{3}$.

The given expression is $\cos^2 A + \cos^2 B - \cos A \cos B$.

Using the identities $\cos^2 A = \dfrac{1 + \cos 2A}{2}$ and $\cos^2 B = \dfrac{1 + \cos 2B}{2}$, we get:

$\cos^2 A + \cos^2 B = 1 + \dfrac{\cos 2A + \cos 2B}{2} = 1 + \cos(A+B)\cos(A-B)$

Also, using the product-to-sum formula:

$\cos A \cos B = \dfrac{1}{2}[\cos(A+B) + \cos(A-B)]$

Substituting $\cos(A+B) = \cos\left(\dfrac{\pi}{3}\right) = \dfrac{1}{2}$ into both expressions:

$\cos^2 A + \cos^2 B = 1 + \dfrac{1}{2}\cos(A-B)$

$\cos A \cos B = \dfrac{1}{2}\left[\dfrac{1}{2} + \cos(A-B)\right] = \dfrac{1}{4} + \dfrac{1}{2}\cos(A-B)$

Subtracting the second expression from the first:

$\cos^2 A + \cos^2 B - \cos A \cos B = 1 + \dfrac{1}{2}\cos(A-B) - \left[\dfrac{1}{4} + \dfrac{1}{2}\cos(A-B)\right]$

$\cos^2 A + \cos^2 B - \cos A \cos B = 1 - \dfrac{1}{4} = \dfrac{3}{4}$

Answer: $\dfrac{3}{4}$

</details>

---

### Q4. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\cos(4A) =$

**Options:**

- **(A)** $1 + 8\cos^2 A + 8\cos^4 A$
- **(B)** $1 + 8\cos^2 A - 8\cos^4 A$
- **(C)** $1 - 8\cos^2 A + 8\cos^4 A$
- **(D)** $1 - 8\cos^2 A - 8\cos^4 A$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1 - 8\cos^2 A + 8\cos^4 A$**

**Detailed Solution:**

Using the double angle formula $\cos(2\theta) = 2\cos^2 \theta - 1$:

$\cos(4A) = \cos(2(2A))$

$\cos(4A) = 2\cos^2(2A) - 1$

Substituting $\cos(2A) = 2\cos^2 A - 1$:

$\cos(4A) = 2(2\cos^2 A - 1)^2 - 1$

Expanding the square:

$\cos(4A) = 2(4\cos^4 A - 4\cos^2 A + 1) - 1$

$\cos(4A) = 8\cos^4 A - 8\cos^2 A + 2 - 1$

$\cos(4A) = 1 - 8\cos^2 A + 8\cos^4 A$

Answer: $1 - 8\cos^2 A + 8\cos^4 A$

</details>

---

### Q5. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\dfrac{\cos A + \sin A}{\cos A - \sin A} = \cot(2A)$, where $A \in \left(0, \dfrac{\pi}{2}\right) - \left\{\dfrac{\pi}{4}\right\}$, then the value of $A$ (in degrees) is...

**Options:**

- **(A)** $15$
- **(B)** $22.5$
- **(C)** $30$
- **(D)** $60$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $15$**

**Detailed Solution:**

Dividing the numerator and denominator of the left hand side by $\cos A$:

$\dfrac{1 + \tan A}{1 - \tan A} = \cot(2A)$

$\tan\left(\dfrac{\pi}{4} + A\right) = \tan\left(\dfrac{\pi}{2} - 2A\right)$

Equating the angles for the general solution:

$\dfrac{\pi}{4} + A = n\pi + \dfrac{\pi}{2} - 2A$

$3A = n\pi + \dfrac{\pi}{4}$

$A = \dfrac{n\pi}{3} + \dfrac{\pi}{12}$

For $n = 0$, $A = \dfrac{\pi}{12} = 15^{\circ}$.

This value lies in the given interval $\left(0, \dfrac{\pi}{2}\right) - \left\{\dfrac{\pi}{4}\right\}$.

Answer: $15$

</details>

---

### Q6. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \sin x + \cos x$, then which of the following is true?

**Options:**

- **(A)** $f(130^\circ) < 0$
- **(B)** $f(220^\circ) > f(320^\circ)$
- **(C)** $f(140^\circ) = f(310^\circ)$
- **(D)** $f(310^\circ) > 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $f(140^\circ) = f(310^\circ)$**

**Detailed Solution:**

Given $f(x) = \sin x + \cos x$

Multiplying and dividing by $\sqrt{2}$:

$f(x) = \sqrt{2} \left( \dfrac{1}{\sqrt{2}} \sin x + \dfrac{1}{\sqrt{2}} \cos x \right) = \sqrt{2} \sin(x + 45^\circ)$

Evaluating the given options:

$f(130^\circ) = \sqrt{2} \sin(130^\circ + 45^\circ) = \sqrt{2} \sin 175^\circ > 0$

$f(220^\circ) = \sqrt{2} \sin(220^\circ + 45^\circ) = \sqrt{2} \sin 265^\circ < 0$

$f(320^\circ) = \sqrt{2} \sin(320^\circ + 45^\circ) = \sqrt{2} \sin 365^\circ = \sqrt{2} \sin 5^\circ > 0$

Thus, $f(220^\circ) < f(320^\circ)$

$f(140^\circ) = \sqrt{2} \sin(140^\circ + 45^\circ) = \sqrt{2} \sin 185^\circ = -\sqrt{2} \sin 5^\circ$

$f(310^\circ) = \sqrt{2} \sin(310^\circ + 45^\circ) = \sqrt{2} \sin 355^\circ = -\sqrt{2} \sin 5^\circ$

Thus, $f(140^\circ) = f(310^\circ)$

$f(310^\circ) = -\sqrt{2} \sin 5^\circ < 0$

Therefore, only $f(140^\circ) = f(310^\circ)$ is true.

Answer: $f(140^\circ) = f(310^\circ)$

</details>

---

### Q7. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $x + y = \dfrac{\pi}{4}$, then $(1 + \tan x)(1 + \tan y) =$

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

Given $x + y = \dfrac{\pi}{4}$

Taking $\tan$ on both sides:

$\tan(x + y) = \tan\left(\dfrac{\pi}{4}\right)$

$\dfrac{\tan x + \tan y}{1 - \tan x \tan y} = 1$

$\tan x + \tan y = 1 - \tan x \tan y$

$\tan x + \tan y + \tan x \tan y = 1$

Adding $1$ to both sides:

$1 + \tan x + \tan y + \tan x \tan y = 2$

$(1 + \tan x)(1 + \tan y) = 2$

Answer: $2$

</details>

---

### Q8. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sec^{-1}\left(\dfrac{x^2 + y^2}{x^2 - y^2}\right) = 2a$ such that $y\dfrac{dy}{dx} = x \cdot f(a)$ then the value of $f\left(\dfrac{2\pi}{3}\right)$ is

**Options:**

- **(A)** $-3$
- **(B)** $\sqrt{3}$
- **(C)** $3$
- **(D)** $\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$**

**Detailed Solution:**

Given $\sec^{-1}\left(\dfrac{x^2 + y^2}{x^2 - y^2}\right) = 2a$

$\Rightarrow \dfrac{x^2 + y^2}{x^2 - y^2} = \sec(2a)$

Applying componendo and dividendo:

$\dfrac{(x^2 + y^2) - (x^2 - y^2)}{(x^2 + y^2) + (x^2 - y^2)} = \dfrac{\sec(2a) - 1}{\sec(2a) + 1}$

$\Rightarrow \dfrac{2y^2}{2x^2} = \dfrac{\dfrac{1}{\cos(2a)} - 1}{\dfrac{1}{\cos(2a)} + 1}$

$\Rightarrow \dfrac{y^2}{x^2} = \dfrac{1 - \cos(2a)}{1 + \cos(2a)}$

$\Rightarrow \dfrac{y^2}{x^2} = \dfrac{2\sin^2(a)}{2\cos^2(a)} = \tan^2(a)$

$\Rightarrow y^2 = x^2 \tan^2(a)$

Differentiating both sides with respect to $x$:

$2y \dfrac{dy}{dx} = 2x \tan^2(a)$

$\Rightarrow y \dfrac{dy}{dx} = x \tan^2(a)$

Comparing with $y \dfrac{dy}{dx} = x \cdot f(a)$, we get:

$f(a) = \tan^2(a)$

Substituting $a = \dfrac{2\pi}{3}$:

$f\left(\dfrac{2\pi}{3}\right) = \tan^2\left(\dfrac{2\pi}{3}\right) = (-\sqrt{3})^2 = 3$

Answer: $3$

</details>

---

### Q9. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\cos 15^\circ - \sin 15^\circ$ is ......

**Options:**

- **(A)** $\sqrt{2}$
- **(B)** $-\sqrt{2}$
- **(C)** $\dfrac{1}{\sqrt{2}}$
- **(D)** $-\dfrac{1}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{\sqrt{2}}$**

**Detailed Solution:**

The given expression is $\cos 15^\circ - \sin 15^\circ$.

Multiplying and dividing by $\sqrt{2}$, we get:

$\sqrt{2} \left( \dfrac{1}{\sqrt{2}} \cos 15^\circ - \dfrac{1}{\sqrt{2}} \sin 15^\circ \right)$

Substituting $\dfrac{1}{\sqrt{2}} = \cos 45^\circ = \sin 45^\circ$:

$\sqrt{2} (\cos 45^\circ \cos 15^\circ - \sin 45^\circ \sin 15^\circ)$

Using the identity $\cos A \cos B - \sin A \sin B = \cos(A + B)$:

$\sqrt{2} \cos(45^\circ + 15^\circ)$

$\sqrt{2} \cos 60^\circ$

$\sqrt{2} \times \dfrac{1}{2} = \dfrac{1}{\sqrt{2}}$

Answer: $\dfrac{1}{\sqrt{2}}$

</details>

---

### Q10. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle ABC$, if $\angle C = \dfrac{\pi}{3}$, then the value of $\cos^2 A + \cos^2 B + \cos A\cos B$ is...

**Options:**

- **(A)** $\dfrac{3}{4}$
- **(B)** $\dfrac{5}{4}$
- **(C)** $\dfrac{-3}{4}$
- **(D)** $\dfrac{-5}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{3}{4}$**

**Detailed Solution:**

Given $A + B + C = \pi$ and $C = \dfrac{\pi}{3}$, we have $A + B = \dfrac{2\pi}{3}$.

The given expression is $\cos^2 A + \cos^2 B + \cos A\cos B$.

Using the identity $\cos^2 A + \cos^2 B = 1 + \dfrac{\cos 2A + \cos 2B}{2}$, we get:

$\cos^2 A + \cos^2 B = 1 + \cos(A+B)\cos(A-B)$

Also, using the product-to-sum formula:

$\cos A\cos B = \dfrac{\cos(A+B) + \cos(A-B)}{2}$

Substituting these into the expression, we get:

$1 + \cos(A+B)\cos(A-B) + \dfrac{\cos(A+B) + \cos(A-B)}{2}$

Since $A + B = \dfrac{2\pi}{3}$, we have $\cos(A+B) = \cos\left(\dfrac{2\pi}{3}\right) = -\dfrac{1}{2}$.

Substituting $\cos(A+B) = -\dfrac{1}{2}$ into the expression:

$1 - \dfrac{1}{2}\cos(A-B) + \dfrac{-\dfrac{1}{2} + \cos(A-B)}{2}$

$= 1 - \dfrac{1}{2}\cos(A-B) - \dfrac{1}{4} + \dfrac{1}{2}\cos(A-B)$

$= 1 - \dfrac{1}{4} = \dfrac{3}{4}$

Answer: $\dfrac{3}{4}$

</details>

---

### Q11. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\cos 43^\circ + \sin 43^\circ = k^3$, then $\cos 2^\circ = \ldots$

**Options:**

- **(A)** $-\dfrac{k^3}{\sqrt{2}}$
- **(B)** $\dfrac{k^3}{\sqrt{2}}$
- **(C)** $-\dfrac{k^3}{\sqrt{3}}$
- **(D)** $\dfrac{k^3}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{k^3}{\sqrt{2}}$**

**Detailed Solution:**

Given $\cos 43^\circ + \sin 43^\circ = k^3$

Multiplying and dividing the LHS by $\sqrt{2}$:

$\sqrt{2} \left( \dfrac{1}{\sqrt{2}} \cos 43^\circ + \dfrac{1}{\sqrt{2}} \sin 43^\circ \right) = k^3$

$\sqrt{2} (\sin 45^\circ \cos 43^\circ + \cos 45^\circ \sin 43^\circ) = k^3$

Using the identity $\sin A \cos B + \cos A \sin B = \sin(A + B)$:

$\sqrt{2} \sin(45^\circ + 43^\circ) = k^3$

$\sqrt{2} \sin 88^\circ = k^3$

Since $\sin \theta = \cos(90^\circ - \theta)$:

$\sqrt{2} \cos(90^\circ - 88^\circ) = k^3$

$\sqrt{2} \cos 2^\circ = k^3$

$\cos 2^\circ = \dfrac{k^3}{\sqrt{2}}$

Answer: $\dfrac{k^3}{\sqrt{2}}$

</details>

---

### Q12. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\cos(60^\circ - A)\cdot\cos A\cdot\cos(60^\circ + A)$ is

**Options:**

- **(A)** $\dfrac{1}{4}\cos 3A$
- **(B)** $\sin 3A$
- **(C)** $\cos 3A$
- **(D)** $\dfrac{1}{4}\sin 3A$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{4}\cos 3A$**

**Detailed Solution:**

Using the identity $\cos(x - y)\cos(x + y) = \cos^2 x - \sin^2 y$

$\cos(60^\circ - A)\cos(60^\circ + A) = \cos^2 60^\circ - \sin^2 A$

$= \dfrac{1}{4} - \sin^2 A$

Multiplying by $\cos A$

$\cos A \left( \dfrac{1}{4} - \sin^2 A \right) = \dfrac{1}{4} \cos A - \cos A (1 - \cos^2 A)$

$= \cos^3 A - \dfrac{3}{4} \cos A$

$= \dfrac{4\cos^3 A - 3\cos A}{4}$

$= \dfrac{1}{4} \cos 3A$

Answer: $\dfrac{1}{4}\cos 3A$

</details>

---

### Q13. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\dfrac{\sin^2 3A}{\sin^2 A} - \dfrac{\cos^2 3A}{\cos^2 A}$ is

**Options:**

- **(A)** $\cos 2A$
- **(B)** $8\cos 2A$
- **(C)** $\dfrac{1}{8}\cos 2A$
- **(D)** $\dfrac{1}{2}\sin 2A$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $8\cos 2A$**

**Detailed Solution:**

Using the multiple angle formulas $\sin 3A = 3\sin A - 4\sin^3 A$ and $\cos 3A = 4\cos^3 A - 3\cos A$.

$\dfrac{\sin 3A}{\sin A} = 3 - 4\sin^2 A$

$\dfrac{\cos 3A}{\cos A} = 4\cos^2 A - 3$

Substituting these into the given expression:

$\left(\dfrac{\sin 3A}{\sin A}\right)^2 - \left(\dfrac{\cos 3A}{\cos A}\right)^2 = (3 - 4\sin^2 A)^2 - (4\cos^2 A - 3)^2$

Expanding the squares:

$= (9 - 24\sin^2 A + 16\sin^4 A) - (16\cos^4 A - 24\cos^2 A + 9)$

$= 16(\sin^4 A - \cos^4 A) - 24(\sin^2 A - \cos^2 A)$

Using $a^2 - b^2 = (a-b)(a+b)$ and $\sin^2 A + \cos^2 A = 1$:

$= 16(\sin^2 A - \cos^2 A)(\sin^2 A + \cos^2 A) - 24(\sin^2 A - \cos^2 A)$

$= 16(\sin^2 A - \cos^2 A)(1) - 24(\sin^2 A - \cos^2 A)$

$= -8(\sin^2 A - \cos^2 A)$

$= 8(\cos^2 A - \sin^2 A)$

Since $\cos^2 A - \sin^2 A = \cos 2A$, the expression simplifies to:

$= 8\cos 2A$

Answer: $8\cos 2A$

</details>

---

### Q14. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In $\triangle ABC$, with the usual notations, $\angle C = 90^\circ$, then $\sin(A - B)$ is equal to....

**Options:**

- **(A)** $\dfrac{a^2 + b^2}{a^2 - b^2}$
- **(B)** $\dfrac{a^2 + c^2}{a^2 - c^2}$
- **(C)** $\dfrac{b^2 + c^2}{b^2 - c^2}$
- **(D)** $\dfrac{a^2 - b^2}{a^2 + b^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{a^2 - b^2}{a^2 + b^2}$**

**Detailed Solution:**

In $\triangle ABC$, $\angle C = 90^\circ$.

Using trigonometric ratios in a right-angled triangle:

$\sin A = \dfrac{a}{c}$

$\cos A = \dfrac{b}{c}$

$\sin B = \dfrac{b}{c}$

$\cos B = \dfrac{a}{c}$

Using the expansion formula for $\sin(A - B)$:

$\sin(A - B) = \sin A \cos B - \cos A \sin B$

Substituting the values:

$\sin(A - B) = \left(\dfrac{a}{c}\right)\left(\dfrac{a}{c}\right) - \left(\dfrac{b}{c}\right)\left(\dfrac{b}{c}\right)$

$\sin(A - B) = \dfrac{a^2 - b^2}{c^2}$

By Pythagoras theorem in $\triangle ABC$, $c^2 = a^2 + b^2$.

Substituting $c^2 = a^2 + b^2$:

$\sin(A - B) = \dfrac{a^2 - b^2}{a^2 + b^2}$

Answer: $\dfrac{a^2 - b^2}{a^2 + b^2}$

</details>

---

### Q15. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $P = \tan 20^\circ$, then the value of $\dfrac{\tan 160^\circ - \tan 110^\circ}{1 + \tan 160^\circ \tan 110^\circ}$ in terms of $P$, is...

**Options:**

- **(A)** $\dfrac{1+P^2}{2P^2}$
- **(B)** $\dfrac{1+P^2}{2P}$
- **(C)** $\dfrac{1-P^2}{2P^2}$
- **(D)** $\dfrac{1-P^2}{2P}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1-P^2}{2P}$**

**Detailed Solution:**

We have $P = \tan 20^{\circ}$.

Expressing the terms in the given expression using $20^{\circ}$:

$\tan 160^{\circ} = \tan(180^{\circ} - 20^{\circ}) = -\tan 20^{\circ} = -P$

$\tan 110^{\circ} = \tan(90^{\circ} + 20^{\circ}) = -\cot 20^{\circ} = -\dfrac{1}{\tan 20^{\circ}} = -\dfrac{1}{P}$

Substituting these values into the given expression:

$\dfrac{\tan 160^{\circ} - \tan 110^{\circ}}{1 + \tan 160^{\circ} \tan 110^{\circ}} = \dfrac{-P - \left(-\dfrac{1}{P}\right)}{1 + (-P)\left(-\dfrac{1}{P}\right)}$

$= \dfrac{\dfrac{1}{P} - P}{1 + 1}$

$= \dfrac{\dfrac{1 - P^2}{P}}{2}$

$= \dfrac{1 - P^2}{2P}$

Answer: $\dfrac{1-P^2}{2P}$

</details>

---

### Q16. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin 3\alpha = 4\sin\alpha \cdot \sin(x+\alpha) \cdot \sin(x-\alpha)$ where $\alpha \neq n\pi, n \in Z$, then all possible values of $x$ are given as

**Options:**

- **(A)** $x = n\pi \pm \dfrac{\pi}{3}, n \in Z$
- **(B)** $x = n\pi \pm \dfrac{\pi}{4}, n \in Z$
- **(C)** $x = n\pi \pm \dfrac{\pi}{6}, n \in Z$
- **(D)** $x = n\pi \pm \dfrac{\pi}{2}, n \in Z$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x = n\pi \pm \dfrac{\pi}{3}, n \in Z$**

**Detailed Solution:**

Given equation is $\sin 3\alpha = 4\sin\alpha \cdot \sin(x+\alpha) \cdot \sin(x-\alpha)$

Using the identities $\sin 3\alpha = 3\sin\alpha - 4\sin^3\alpha$ and $\sin(A+B)\sin(A-B) = \sin^2 A - \sin^2 B$, we get:

$3\sin\alpha - 4\sin^3\alpha = 4\sin\alpha(\sin^2 x - \sin^2\alpha)$

$3\sin\alpha - 4\sin^3\alpha = 4\sin\alpha \sin^2 x - 4\sin^3\alpha$

$3\sin\alpha = 4\sin\alpha \sin^2 x$

Since $\alpha \neq n\pi$, $\sin\alpha \neq 0$. Dividing both sides by $\sin\alpha$, we get:

$3 = 4\sin^2 x$

$\sin^2 x = \dfrac{3}{4}$

$\sin^2 x = \left(\dfrac{\sqrt{3}}{2}\right)^2$

$\sin^2 x = \sin^2\left(\dfrac{\pi}{3}\right)$

The general solution is $x = n\pi \pm \dfrac{\pi}{3}, n \in Z$.

Answer: $x = n\pi \pm \dfrac{\pi}{3}, n \in Z$

</details>

---

### Q17. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\cos(\theta-\alpha)=a$ and $\sin(\theta-\beta)=b$, then the value of $\cos^2(\alpha-\beta)+2ab\sin(\alpha-\beta)+\cos^2(\theta-\alpha)$ is...

**Options:**

- **(A)** $a^2 - 2b^2$
- **(B)** $a^2 + 2b^2$
- **(C)** $2a^2 - b^2$
- **(D)** $2a^2 + b^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2a^2 + b^2$**

**Detailed Solution:**

Let $x = \theta - \alpha$ and $y = \theta - \beta$.

Given $\cos x = a$ and $\sin y = b$.

We can write $\alpha - \beta = (\theta - \beta) - (\theta - \alpha) = y - x$.

Using the trigonometric expansion formulas:

$\cos(\alpha - \beta) = \cos(y - x) = \cos y \cos x + \sin y \sin x = a \cos y + b \sin x$

$\sin(\alpha - \beta) = \sin(y - x) = \sin y \cos x - \cos y \sin x = ab - \cos y \sin x$

Substituting these into the given expression $\cos^2(\alpha-\beta)+2ab\sin(\alpha-\beta)+\cos^2(\theta-\alpha)$:

$(a \cos y + b \sin x)^2 + 2ab(ab - \cos y \sin x) + a^2$

Expanding the terms, we get:

$a^2 \cos^2 y + b^2 \sin^2 x + 2ab \cos y \sin x + 2a^2b^2 - 2ab \cos y \sin x + a^2$

Canceling $2ab \cos y \sin x$ and expressing $\cos^2 y$ and $\sin^2 x$ in terms of $a$ and $b$:

$a^2(1 - \sin^2 y) + b^2(1 - \cos^2 x) + 2a^2b^2 + a^2$

Since $\sin y = b$ and $\cos x = a$, this becomes:

$a^2(1 - b^2) + b^2(1 - a^2) + 2a^2b^2 + a^2$

$a^2 - a^2b^2 + b^2 - a^2b^2 + 2a^2b^2 + a^2$

Simplifying the expression, the terms with $a^2b^2$ cancel out:

$a^2 + b^2 + a^2 = 2a^2 + b^2$

Answer: $2a^2 + b^2$

</details>

---

### Q18. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\tan 105^\circ = $ ......

**Options:**

- **(A)** $\dfrac{\sqrt{3} - 1}{2\sqrt{2}}$
- **(B)** $\dfrac{\sqrt{3} + 1}{2\sqrt{2}}$
- **(C)** $\dfrac{1 + \sqrt{3}}{1 - \sqrt{3}}$
- **(D)** $\dfrac{2\sqrt{2}}{\sqrt{3} + 1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1 + \sqrt{3}}{1 - \sqrt{3}}$**

**Detailed Solution:**

$\tan 105^\circ = \tan(60^\circ + 45^\circ)$

Using the identity $\tan(A + B) = \dfrac{\tan A + \tan B}{1 - \tan A \tan B}$

Substituting $A = 60^\circ$ and $B = 45^\circ$:

$\tan 105^\circ = \dfrac{\tan 60^\circ + \tan 45^\circ}{1 - \tan 60^\circ \tan 45^\circ}$

Since $\tan 60^\circ = \sqrt{3}$ and $\tan 45^\circ = 1$:

$\tan 105^\circ = \dfrac{\sqrt{3} + 1}{1 - \sqrt{3}(1)} = \dfrac{1 + \sqrt{3}}{1 - \sqrt{3}}$

Answer: $\dfrac{1 + \sqrt{3}}{1 - \sqrt{3}}$

</details>

---

### Q19. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In $\Delta ABC$, if $\angle A = 90^\circ$, then $\sin(B - C) = $

**Options:**

- **(A)** $\dfrac{a^2 - c^2}{a^2 + c^2}$
- **(B)** $\dfrac{c^2 - a^2}{c^2 + a^2}$
- **(C)** $\dfrac{b^2 - c^2}{b^2 + c^2}$
- **(D)** $\dfrac{c^2 - b^2}{c^2 + b^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{b^2 - c^2}{b^2 + c^2}$**

**Detailed Solution:**

Given $\angle A = 90^\circ$, $\Delta ABC$ is a right-angled triangle with hypotenuse $a$.

From the properties of a right-angled triangle, $\sin B = \dfrac{b}{a}$, $\cos B = \dfrac{c}{a}$, $\sin C = \dfrac{c}{a}$, and $\cos C = \dfrac{b}{a}$.

Using the expansion formula for sine:

$\sin(B - C) = \sin B \cos C - \cos B \sin C$

Substituting the trigonometric ratios:

$\sin(B - C) = \left(\dfrac{b}{a}\right)\left(\dfrac{b}{a}\right) - \left(\dfrac{c}{a}\right)\left(\dfrac{c}{a}\right)$

$\sin(B - C) = \dfrac{b^2 - c^2}{a^2}$

Using Pythagoras theorem, $a^2 = b^2 + c^2$.

Therefore, $\sin(B - C) = \dfrac{b^2 - c^2}{b^2 + c^2}$.

</details>

---

### Q20. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\cos^2 10^\circ - \cos 10^\circ \cos 50^\circ + \cos^2 50^\circ$ is equal to....

**Options:**

- **(A)** $\dfrac{1}{4}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{3}{4}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{3}{4}$**

**Detailed Solution:**

Given expression: $\cos^2 10^\circ - \cos 10^\circ \cos 50^\circ + \cos^2 50^\circ$

Multiplying and dividing by $2$:

$= \dfrac{1}{2} [ 2\cos^2 10^\circ - 2\cos 10^\circ \cos 50^\circ + 2\cos^2 50^\circ ]$

Using the identities $2\cos^2 \theta = 1 + \cos 2\theta$ and $2\cos A \cos B = \cos(A+B) + \cos(A-B)$:

$= \dfrac{1}{2} [ (1 + \cos 20^\circ) - (\cos 60^\circ + \cos 40^\circ) + (1 + \cos 100^\circ) ]$

Substituting $\cos 60^\circ = \dfrac{1}{2}$:

$= \dfrac{1}{2} \left[ 1 + \cos 20^\circ - \dfrac{1}{2} - \cos 40^\circ + 1 + \cos 100^\circ \right]$

$= \dfrac{1}{2} \left[ \dfrac{3}{2} + (\cos 100^\circ + \cos 20^\circ) - \cos 40^\circ \right]$

Applying the sum-to-product formula $\cos C + \cos D = 2\cos\left(\dfrac{C+D}{2}\right)\cos\left(\dfrac{C-D}{2}\right)$:

$\cos 100^\circ + \cos 20^\circ = 2\cos 60^\circ \cos 40^\circ = 2 \left(\dfrac{1}{2}\right) \cos 40^\circ = \cos 40^\circ$

Substituting this back into the expression:

$= \dfrac{1}{2} \left[ \dfrac{3}{2} + \cos 40^\circ - \cos 40^\circ \right]$

$= \dfrac{1}{2} \left( \dfrac{3}{2} \right) = \dfrac{3}{4}$

Answer: $\dfrac{3}{4}$

</details>

---

### Q21. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\begin{aligned} & \text { If } \sin (\alpha+\beta)=1, \sin (\alpha-\beta)=\frac{1}{2}, \alpha, \beta \in\left[0, \frac{\pi}{2}\right] \\ & \text { then } \tan (\alpha+2 \beta) \cdot \tan (2 \alpha+\beta)=\end{aligned}$

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** 0
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Given $\sin(\alpha+\beta) = 1$ and $\alpha, \beta \in \left[0, \dfrac{\pi}{2}\right]$, we have $\alpha+\beta = \dfrac{\pi}{2}$.

Given $\sin(\alpha-\beta) = \dfrac{1}{2}$, we have $\alpha-\beta = \dfrac{\pi}{6}$.

Adding the two equations gives $2\alpha = \dfrac{2\pi}{3} \Rightarrow \alpha = \dfrac{\pi}{3}$.

Subtracting the two equations gives $2\beta = \dfrac{\pi}{3} \Rightarrow \beta = \dfrac{\pi}{6}$.

We need to find $\tan(\alpha+2\beta) \cdot \tan(2\alpha+\beta)$.

Substituting the values of $\alpha$ and $\beta$:

$\alpha+2\beta = \dfrac{\pi}{3} + 2\left(\dfrac{\pi}{6}\right) = \dfrac{2\pi}{3}$

$2\alpha+\beta = 2\left(\dfrac{\pi}{3}\right) + \dfrac{\pi}{6} = \dfrac{5\pi}{6}$

$\tan(\alpha+2\beta) \cdot \tan(2\alpha+\beta) = \tan\left(\dfrac{2\pi}{3}\right) \cdot \tan\left(\dfrac{5\pi}{6}\right)$

$= (-\sqrt{3}) \cdot \left(-\dfrac{1}{\sqrt{3}}\right) = 1$

Answer: 1

</details>

---

### Q22. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\tan \frac{\pi}{3}+2 \tan \frac{2 \pi}{3}+4 \tan \frac{4 \pi}{3}+8 \tan \frac{8 \pi}{3}$ is equal to

**Options:**

- **(A)** $-5 \sqrt{3}$
- **(B)** $5 \sqrt{3}$
- **(C)** $-10 \sqrt{3}$
- **(D)** $15 \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-5 \sqrt{3}$**

**Detailed Solution:**

The values of the trigonometric terms are evaluated as follows:

$\tan \dfrac{\pi}{3} = \sqrt{3}$

$\tan \dfrac{2 \pi}{3} = \tan \left(\pi - \dfrac{\pi}{3}\right) = -\tan \dfrac{\pi}{3} = -\sqrt{3}$

$\tan \dfrac{4 \pi}{3} = \tan \left(\pi + \dfrac{\pi}{3}\right) = \tan \dfrac{\pi}{3} = \sqrt{3}$

$\tan \dfrac{8 \pi}{3} = \tan \left(2\pi + \dfrac{2\pi}{3}\right) = \tan \dfrac{2\pi}{3} = -\sqrt{3}$

Substituting these values into the given expression:

$\tan \dfrac{\pi}{3} + 2 \tan \dfrac{2 \pi}{3} + 4 \tan \dfrac{4 \pi}{3} + 8 \tan \dfrac{8 \pi}{3}$

$= \sqrt{3} + 2(-\sqrt{3}) + 4(\sqrt{3}) + 8(-\sqrt{3})$

$= \sqrt{3} - 2\sqrt{3} + 4\sqrt{3} - 8\sqrt{3}$

$= (1 - 2 + 4 - 8)\sqrt{3}$

$= -5\sqrt{3}$

Answer: $-5 \sqrt{3}$

</details>

---

### Q23. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\cos ^4 \frac{\pi}{8}+\cos ^4 \frac{3 \pi}{8}+\cos ^4 \frac{5 \pi}{8}+\cos ^4 \frac{7 \pi}{8}=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{3}{2}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{2}$**

**Detailed Solution:**

The given expression is $\cos^4 \dfrac{\pi}{8} + \cos^4 \dfrac{3\pi}{8} + \cos^4 \dfrac{5\pi}{8} + \cos^4 \dfrac{7\pi}{8}$.

Using the property $\cos(\pi - \theta) = -\cos \theta$, we have:
$\cos \dfrac{7\pi}{8} = \cos\left(\pi - \dfrac{\pi}{8}\right) = -\cos \dfrac{\pi}{8} \Rightarrow \cos^4 \dfrac{7\pi}{8} = \cos^4 \dfrac{\pi}{8}$
$\cos \dfrac{5\pi}{8} = \cos\left(\pi - \dfrac{3\pi}{8}\right) = -\cos \dfrac{3\pi}{8} \Rightarrow \cos^4 \dfrac{5\pi}{8} = \cos^4 \dfrac{3\pi}{8}$

Substituting these into the expression, we get:
$2 \left( \cos^4 \dfrac{\pi}{8} + \cos^4 \dfrac{3\pi}{8} \right)$

Using the property $\cos\left(\dfrac{\pi}{2} - \theta\right) = \sin \theta$, we have:
$\cos \dfrac{3\pi}{8} = \cos\left(\dfrac{\pi}{2} - \dfrac{\pi}{8}\right) = \sin \dfrac{\pi}{8}$

The expression becomes:
$2 \left( \cos^4 \dfrac{\pi}{8} + \sin^4 \dfrac{\pi}{8} \right)$

Using the algebraic identity $a^4 + b^4 = (a^2 + b^2)^2 - 2a^2b^2$:
$2 \left( (\cos^2 \dfrac{\pi}{8} + \sin^2 \dfrac{\pi}{8})^2 - 2 \sin^2 \dfrac{\pi}{8} \cos^2 \dfrac{\pi}{8} \right)$

Since $\cos^2 \theta + \sin^2 \theta = 1$ and $2 \sin \theta \cos \theta = \sin 2\theta$:
$2 \left( 1 - \dfrac{1}{2} (2 \sin \dfrac{\pi}{8} \cos \dfrac{\pi}{8})^2 \right)$

$= 2 \left( 1 - \dfrac{1}{2} \sin^2 \dfrac{\pi}{4} \right)$

$= 2 \left( 1 - \dfrac{1}{2} \left(\dfrac{1}{\sqrt{2}}\right)^2 \right)$

$= 2 \left( 1 - \dfrac{1}{4} \right)$

$= 2 \times \dfrac{3}{4} = \dfrac{3}{2}$

Answer: $\frac{3}{2}$

</details>

---

### Q24. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin \theta=\frac{1}{2}\left(x+\frac{1}{x}\right)$, then $\sin 3 \theta+\frac{1}{2}\left(x^3+\frac{1}{x^3}\right)=$

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $\frac{1}{4}$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Given $\sin \theta = \dfrac{1}{2}\left(x + \dfrac{1}{x}\right)$

We know the trigonometric identity:

$\sin 3\theta = 3\sin \theta - 4\sin^3 \theta$

Substituting the value of $\sin \theta$ into the identity:

$\sin 3\theta = 3\left[\dfrac{1}{2}\left(x + \dfrac{1}{x}\right)\right] - 4\left[\dfrac{1}{2}\left(x + \dfrac{1}{x}\right)\right]^3$

$\sin 3\theta = \dfrac{3}{2}\left(x + \dfrac{1}{x}\right) - \dfrac{4}{8}\left(x + \dfrac{1}{x}\right)^3$

$\sin 3\theta = \dfrac{3}{2}\left(x + \dfrac{1}{x}\right) - \dfrac{1}{2}\left(x^3 + \dfrac{1}{x^3} + 3x\left(\dfrac{1}{x}\right)\left(x + \dfrac{1}{x}\right)\right)$

$\sin 3\theta = \dfrac{3}{2}\left(x + \dfrac{1}{x}\right) - \dfrac{1}{2}\left(x^3 + \dfrac{1}{x^3} + 3\left(x + \dfrac{1}{x}\right)\right)$

$\sin 3\theta = \dfrac{3}{2}\left(x + \dfrac{1}{x}\right) - \dfrac{1}{2}\left(x^3 + \dfrac{1}{x^3}\right) - \dfrac{3}{2}\left(x + \dfrac{1}{x}\right)$

$\sin 3\theta = -\dfrac{1}{2}\left(x^3 + \dfrac{1}{x^3}\right)$

$\sin 3\theta + \dfrac{1}{2}\left(x^3 + \dfrac{1}{x^3}\right) = 0$

Answer: 0

</details>

---

### Q25. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin \mathrm{A}+\sin \mathrm{B}=x$ and $\cos \mathrm{A}+\cos \mathrm{B}=\mathrm{y}$, then $\sin (\mathrm{A}+\mathrm{B})=$

**Options:**

- **(A)** $\frac{2 x y}{x^2+y^2}$
- **(B)** $\frac{x y}{x^2+y^2}$
- **(C)** $\frac{2 x y}{y^2-x^2}$
- **(D)** $\frac{x y}{y^2-x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2 x y}{x^2+y^2}$**

**Detailed Solution:**

Given $\sin A + \sin B = x$ and $\cos A + \cos B = y$.

Using the sum-to-product trigonometric identities:

$2 \sin\left(\dfrac{A+B}{2}\right) \cos\left(\dfrac{A-B}{2}\right) = x$

$2 \cos\left(\dfrac{A+B}{2}\right) \cos\left(\dfrac{A-B}{2}\right) = y$

Dividing the first equation by the second equation:

$\dfrac{2 \sin\left(\dfrac{A+B}{2}\right) \cos\left(\dfrac{A-B}{2}\right)}{2 \cos\left(\dfrac{A+B}{2}\right) \cos\left(\dfrac{A-B}{2}\right)} = \dfrac{x}{y}$

$\tan\left(\dfrac{A+B}{2}\right) = \dfrac{x}{y}$

Using the half-angle formula for sine:

$\sin(A+B) = \dfrac{2 \tan\left(\dfrac{A+B}{2}\right)}{1 + \tan^2\left(\dfrac{A+B}{2}\right)}$

Substituting the value of $\tan\left(\dfrac{A+B}{2}\right)$:

$\sin(A+B) = \dfrac{2 \left(\dfrac{x}{y}\right)}{1 + \left(\dfrac{x}{y}\right)^2}$

$\sin(A+B) = \dfrac{\dfrac{2x}{y}}{\dfrac{x^2+y^2}{y^2}}$

$\sin(A+B) = \dfrac{2xy}{x^2+y^2}$

Answer: $\frac{2 x y}{x^2+y^2}$

</details>

---

### Q26. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin A=n \sin (A+2 B)$, then $\tan (A+B)=$

**Options:**

- **(A)** $\frac{1+n}{2-n} \cdot \tan B$
- **(B)** $\frac{1-n}{1+n} \cdot \tan B$
- **(C)** $\frac{1-n}{2+n} \cdot \tan B$
- **(D)** $\frac{1+n}{1-n} \cdot \tan B$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1+n}{1-n} \cdot \tan B$**

**Detailed Solution:**

Given $\sin A = n \sin (A+2B)$

$\Rightarrow \dfrac{\sin (A+2B)}{\sin A} = \dfrac{1}{n}$

Applying componendo and dividendo, we get:

$\dfrac{\sin (A+2B) + \sin A}{\sin (A+2B) - \sin A} = \dfrac{1+n}{1-n}$

Using the sum-to-product formulas $\sin C + \sin D = 2 \sin \left(\dfrac{C+D}{2}\right) \cos \left(\dfrac{C-D}{2}\right)$ and $\sin C - \sin D = 2 \cos \left(\dfrac{C+D}{2}\right) \sin \left(\dfrac{C-D}{2}\right)$:

$\dfrac{2 \sin \left(\dfrac{A+2B+A}{2}\right) \cos \left(\dfrac{A+2B-A}{2}\right)}{2 \cos \left(\dfrac{A+2B+A}{2}\right) \sin \left(\dfrac{A+2B-A}{2}\right)} = \dfrac{1+n}{1-n}$

$\dfrac{2 \sin (A+B) \cos B}{2 \cos (A+B) \sin B} = \dfrac{1+n}{1-n}$

$\tan (A+B) \cot B = \dfrac{1+n}{1-n}$

$\tan (A+B) = \dfrac{1+n}{1-n} \tan B$

Answer: $\frac{1+n}{1-n} \cdot \tan B$

</details>

---

### Q27. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\tan 20^{\circ} \tan 80^{\circ} \cot 50^{\circ}=$

**Options:**

- **(A)** $\sqrt{3}$
- **(B)** $\frac{1}{\sqrt{3}}$
- **(C)** $\frac{1}{2 \sqrt{3}}$
- **(D)** $2 \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{3}$**

**Detailed Solution:**

The given expression is $\tan 20^{\circ} \tan 80^{\circ} \cot 50^{\circ}$.

Using the complementary angle relation $\cot \theta = \tan(90^{\circ} - \theta)$, we have $\cot 50^{\circ} = \tan 40^{\circ}$.

Substituting this into the expression, we get:

$\tan 20^{\circ} \tan 40^{\circ} \tan 80^{\circ}$

We know the standard trigonometric identity:

$\tan \theta \tan(60^{\circ} - \theta) \tan(60^{\circ} + \theta) = \tan 3\theta$

Putting $\theta = 20^{\circ}$, we get:

$\tan 20^{\circ} \tan(60^{\circ} - 20^{\circ}) \tan(60^{\circ} + 20^{\circ}) = \tan(3 \times 20^{\circ})$

$\Rightarrow \tan 20^{\circ} \tan 40^{\circ} \tan 80^{\circ} = \tan 60^{\circ}$

Since $\tan 60^{\circ} = \sqrt{3}$, the value of the given expression is $\sqrt{3}$.

Answer: $\sqrt{3}$

</details>

---

### Q28. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$3 \tan ^6 10^{\circ}-27 \tan ^4 10^{\circ}+33 \tan ^2 10^{\circ}=$

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

Let $\theta = 10^{\circ}$. Then $3\theta = 30^{\circ}$.

Using the multiple angle formula $\tan 3\theta = \dfrac{3 \tan \theta - \tan^3 \theta}{1 - 3 \tan^2 \theta}$, we get:

$\tan 30^{\circ} = \dfrac{3 \tan 10^{\circ} - \tan^3 10^{\circ}}{1 - 3 \tan^2 10^{\circ}}$

$\dfrac{1}{\sqrt{3}} = \dfrac{\tan 10^{\circ} (3 - \tan^2 10^{\circ})}{1 - 3 \tan^2 10^{\circ}}$

Squaring both sides, we obtain:

$\dfrac{1}{3} = \dfrac{\tan^2 10^{\circ} (3 - \tan^2 10^{\circ})^2}{(1 - 3 \tan^2 10^{\circ})^2}$

Let $x = \tan^2 10^{\circ}$. Substituting $x$ into the equation:

$\dfrac{1}{3} = \dfrac{x(9 - 6x + x^2)}{1 - 6x + 9x^2}$

$1 - 6x + 9x^2 = 3x(9 - 6x + x^2)$

$1 - 6x + 9x^2 = 27x - 18x^2 + 3x^3$

Rearranging the terms, we get:

$3x^3 - 27x^2 + 33x = 1$

Substituting $x = \tan^2 10^{\circ}$ back into the equation:

$3 \tan^6 10^{\circ} - 27 \tan^4 10^{\circ} + 33 \tan^2 10^{\circ} = 1$

Answer: $1$

</details>

---

### Q29. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $3 \sin 2 \theta=2 \sin 3 \theta$ and $0 < \theta < \pi$, then the value of $\sin \theta$ is equal to

**Options:**

- **(A)** $\frac{\sqrt{17}}{4}$
- **(B)** $\frac{5 \sqrt{2}}{4}$
- **(C)** $\frac{3 \sqrt{2}}{4}$
- **(D)** $\frac{\sqrt{15}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\sqrt{15}}{4}$**

**Detailed Solution:**

Given $3 \sin 2 \theta = 2 \sin 3 \theta$

Using the formulas $\sin 2 \theta = 2 \sin \theta \cos \theta$ and $\sin 3 \theta = 3 \sin \theta - 4 \sin^3 \theta$:

$3(2 \sin \theta \cos \theta) = 2(3 \sin \theta - 4 \sin^3 \theta)$

$6 \sin \theta \cos \theta = 6 \sin \theta - 8 \sin^3 \theta$

Since $0 < \theta < \pi$, $\sin \theta \neq 0$. Dividing both sides by $2 \sin \theta$:

$3 \cos \theta = 3 - 4 \sin^2 \theta$

Substituting $\sin^2 \theta = 1 - \cos^2 \theta$:

$3 \cos \theta = 3 - 4(1 - \cos^2 \theta)$

$3 \cos \theta = -1 + 4 \cos^2 \theta$

$4 \cos^2 \theta - 3 \cos \theta - 1 = 0$

$(4 \cos \theta + 1)(\cos \theta - 1) = 0$

$\cos \theta = -\dfrac{1}{4}$ or $\cos \theta = 1$

Since $0 < \theta < \pi$, $\cos \theta \neq 1$. Therefore, $\cos \theta = -\dfrac{1}{4}$.

$\sin \theta = \sqrt{1 - \cos^2 \theta} = \sqrt{1 - \left(-\dfrac{1}{4}\right)^2} = \sqrt{1 - \dfrac{1}{16}} = \dfrac{\sqrt{15}}{4}$

Answer: $\frac{\sqrt{15}}{4}$

</details>

---

### Q30. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

With usual notations, in a triangle ABC , if $\theta$ is any real number, then $a \cos (B-\theta)+b \cos (A+\theta)$ is

**Options:**

- **(A)** $a \cos \theta$
- **(B)** $\mathrm{b} \cos \theta$
- **(C)** $\cos \theta$
- **(D)** $c \cos \theta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $c \cos \theta$**

**Detailed Solution:**

The given expression is $a \cos (B-\theta) + b \cos (A+\theta)$.

Expanding the cosine terms using the formula $\cos(x \pm y) = \cos x \cos y \mp \sin x \sin y$, we get:

$a (\cos B \cos \theta + \sin B \sin \theta) + b (\cos A \cos \theta - \sin A \sin \theta)$

Grouping the terms with $\cos \theta$ and $\sin \theta$ together:

$(a \cos B + b \cos A) \cos \theta + (a \sin B - b \sin A) \sin \theta$

By the projection rule in a triangle, $a \cos B + b \cos A = c$.

By the sine rule, $\dfrac{a}{\sin A} = \dfrac{b}{\sin B}$, which gives $a \sin B = b \sin A$, so $a \sin B - b \sin A = 0$.

Substituting these values into the expression, we get:

$c \cos \theta + 0 \cdot \sin \theta = c \cos \theta$

Answer: $c \cos \theta$

</details>

---

### Q31. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}+\mathrm{B}=\frac{\pi}{2}$ then the maximum value of $\cos \mathrm{A} \cdot \cos \mathrm{B}$ is

**Options:**

- **(A)** $\frac{1}{\sqrt{2}}$
- **(B)** $\frac{1}{2}$
- **(C)** $-\frac{1}{2}$
- **(D)** $-\frac{1}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2}$**

**Detailed Solution:**

Given $A + B = \dfrac{\pi}{2}$

$B = \dfrac{\pi}{2} - A$

Let $y = \cos A \cdot \cos B$

Substituting the value of $B$:

$y = \cos A \cdot \cos\left(\dfrac{\pi}{2} - A\right)$

$y = \cos A \cdot \sin A$

Multiplying and dividing by $2$:

$y = \dfrac{1}{2} (2 \sin A \cos A)$

$y = \dfrac{1}{2} \sin 2A$

The maximum value of $\sin 2A$ is $1$.

Therefore, the maximum value of $y$ is $\dfrac{1}{2} \times 1 = \dfrac{1}{2}$.

Answer: $\frac{1}{2}$

</details>

---

### Q32. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\sqrt{3} \cot 20^{\circ}-4 \cos 20^{\circ}$ is equal to

**Options:**

- **(A)** $1$
- **(B)** $-1$
- **(C)** $0$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

$\sqrt{3} \cot 20^{\circ} - 4 \cos 20^{\circ}$

$= \dfrac{\sqrt{3} \cos 20^{\circ}}{\sin 20^{\circ}} - 4 \cos 20^{\circ}$

$= \dfrac{\sqrt{3} \cos 20^{\circ} - 4 \sin 20^{\circ} \cos 20^{\circ}}{\sin 20^{\circ}}$

$= \dfrac{\sqrt{3} \cos 20^{\circ} - 2 \sin 40^{\circ}}{\sin 20^{\circ}}$

Substituting $\sqrt{3} = 2 \sin 60^{\circ}$:

$= \dfrac{2 \sin 60^{\circ} \cos 20^{\circ} - 2 \sin 40^{\circ}}{\sin 20^{\circ}}$

Using $2 \sin A \cos B = \sin(A + B) + \sin(A - B)$:

$= \dfrac{\sin(60^{\circ} + 20^{\circ}) + \sin(60^{\circ} - 20^{\circ}) - 2 \sin 40^{\circ}}{\sin 20^{\circ}}$

$= \dfrac{\sin 80^{\circ} + \sin 40^{\circ} - 2 \sin 40^{\circ}}{\sin 20^{\circ}}$

$= \dfrac{\sin 80^{\circ} - \sin 40^{\circ}}{\sin 20^{\circ}}$

Using $\sin C - \sin D = 2 \cos \left(\dfrac{C + D}{2}\right) \sin \left(\dfrac{C - D}{2}\right)$:

$= \dfrac{2 \cos 60^{\circ} \sin 20^{\circ}}{\sin 20^{\circ}}$

$= 2 \cos 60^{\circ}$

$= 2 \times \dfrac{1}{2} = 1$

Answer: $1$

</details>

---

### Q33. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum to infinite terms of the series
$\tan ^{-1}\left(\frac{1}{3}\right)+\tan ^{-1}\left(\frac{2}{9}\right)+\ldots \ldots \ldots \ldots+\tan ^{-1}\left(\frac{2^{\mathrm{n}-1}}{1+2^{2 \mathrm{n}-1}}\right)+\ldots \ldots \ldots \text { is }$

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{\pi}{6}$
- **(D)** $\frac{\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}$**

**Detailed Solution:**

The $n^{\text{th}}$ term of the given series is:

$T_n = \tan^{-1}\left(\dfrac{2^{n-1}}{1+2^{2n-1}}\right)$

This can be rewritten by expressing the numerator as the difference of two terms whose product is the second term in the denominator:

$T_n = \tan^{-1}\left(\dfrac{2^n - 2^{n-1}}{1 + 2^n \cdot 2^{n-1}}\right)$

Using the inverse trigonometric identity $\tan^{-1}\left(\dfrac{x-y}{1+xy}\right) = \tan^{-1}(x) - \tan^{-1}(y)$, we get:

$T_n = \tan^{-1}(2^n) - \tan^{-1}(2^{n-1})$

The sum of the first $n$ terms is:

$S_n = \sum_{k=1}^n T_k$

$S_n = (\tan^{-1}(2) - \tan^{-1}(1)) + (\tan^{-1}(2^2) - \tan^{-1}(2)) + \dots + (\tan^{-1}(2^n) - \tan^{-1}(2^{n-1}))$

This is a telescoping series where all intermediate terms cancel out, leaving:

$S_n = \tan^{-1}(2^n) - \tan^{-1}(1)$

To find the sum to infinite terms, we take the limit as $n \to \infty$:

$S_\infty = \lim_{n \to \infty} (\tan^{-1}(2^n) - \tan^{-1}(1))$

Since $\lim_{n \to \infty} 2^n = \infty$, we have $\lim_{n \to \infty} \tan^{-1}(2^n) = \dfrac{\pi}{2}$. Also, $\tan^{-1}(1) = \dfrac{\pi}{4}$.

$S_\infty = \dfrac{\pi}{2} - \dfrac{\pi}{4} = \dfrac{\pi}{4}$

Answer: $\frac{\pi}{4}$

</details>

---

### Q34. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $3 \sin \alpha=5 \sin \beta$, then $\tan \left(\frac{\alpha+\beta}{2}\right) \div \tan \left(\frac{\alpha-\beta}{2}\right)=$

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4$**

**Detailed Solution:**

Given $3 \sin \alpha = 5 \sin \beta$

$\dfrac{\sin \alpha}{\sin \beta} = \dfrac{5}{3}$

By componendo and dividendo:

$\dfrac{\sin \alpha + \sin \beta}{\sin \alpha - \sin \beta} = \dfrac{5 + 3}{5 - 3}$

Using the formulas $\sin C + \sin D = 2 \sin\left(\dfrac{C+D}{2}\right) \cos\left(\dfrac{C-D}{2}\right)$ and $\sin C - \sin D = 2 \cos\left(\dfrac{C+D}{2}\right) \sin\left(\dfrac{C-D}{2}\right)$:

$\dfrac{2 \sin \left(\dfrac{\alpha+\beta}{2}\right) \cos \left(\dfrac{\alpha-\beta}{2}\right)}{2 \cos \left(\dfrac{\alpha+\beta}{2}\right) \sin \left(\dfrac{\alpha-\beta}{2}\right)} = \dfrac{8}{2}$

$\tan \left(\dfrac{\alpha+\beta}{2}\right) \cot \left(\dfrac{\alpha-\beta}{2}\right) = 4$

$\dfrac{\tan \left(\dfrac{\alpha+\beta}{2}\right)}{\tan \left(\dfrac{\alpha-\beta}{2}\right)} = 4$

Answer: $4$

</details>

---

### Q35. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\sin (y+z-x), \sin (z+x-y)$ and $\sin (x+y-z)$ are in $A P$, then

**Options:**

- **(A)** $\tan y=\tan x+\tan z$
- **(B)** $\tan y=\tan x-\tan z$
- **(C)** $2 \tan y=\tan x+\tan z$
- **(D)** $2 \tan y=\tan x-\tan z$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 \tan y=\tan x+\tan z$**

**Detailed Solution:**

We have $2 \sin (z+x-y)=\sin (y+z-x)+\sin (x+y-z)$
$$
\begin{aligned}
& \therefore \sin (\mathrm{y}+\mathrm{z}-\mathrm{x})-\sin (\mathrm{z}+\mathrm{x}-\mathrm{y})=\sin (\mathrm{z}+\mathrm{x}-\mathrm{y})-\sin (\mathrm{x}+\mathrm{y}-\mathrm{z}) \\
& \therefore 2 \cos \mathrm{z} \sin (\mathrm{y}-\mathrm{x})=2 \cos \mathrm{x} \sin (\mathrm{z}-\mathrm{y}) \\
& \therefore \cos \mathrm{z}(\sin \mathrm{y} \cos \mathrm{x}-\cos \mathrm{y} \sin \mathrm{x})=\cos \mathrm{x}(\sin \mathrm{z} \cos \mathrm{y}-\cos \mathrm{z} \sin \mathrm{y}) \\
& \therefore \cos \mathrm{x} \sin \mathrm{y} \cos \mathrm{z}-\sin \mathrm{x} \cos \mathrm{y} \cos \mathrm{z}=\cos \mathrm{x} \cos \mathrm{y} \sin \mathrm{z} \\
& -\cos \mathrm{x} \sin \mathrm{y} \cos \mathrm{z} \\
& \text { Dividing both } \operatorname{sides} \text { by } \cos \mathrm{x} \cos \mathrm{y} \cos \mathrm{z} \text {, we get } \\
& \tan \mathrm{y}-\tan \mathrm{x}=\tan \mathrm{z}-\tan \mathrm{y} \\
& \therefore 2 \tan \mathrm{y}=\tan \mathrm{x}+\tan \mathrm{z}
\end{aligned}
$$

</details>

---

### Q36. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If in $A \triangle A B C$, with usual notations, $a^2, b^2, c^2$ are in A.P. then $\frac{\sin 3 B}{\sin B}=$

**Options:**

- **(A)** $\frac{a^2-c^2}{2 a c}$
- **(B)** $\left(\frac{a^2-c^2}{2 a c}\right)^2$
- **(C)** $\frac{\mathrm{a}^2-\mathrm{c}^2}{\mathrm{ac}}$
- **(D)** $\left(\frac{a^2-c^2}{a c}\right)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\frac{a^2-c^2}{2 a c}\right)^2$**

**Detailed Solution:**

We have $2 b^2=a^2+c^2$
$$
\begin{aligned}
& \frac{\sin 3 \mathrm{~B}}{\sin \mathrm{B}}=\frac{3 \sin \mathrm{B}-4 \sin ^2 \mathrm{~B}}{\sin \mathrm{B}} \\
& =3-4 \sin ^2 \mathrm{~B}=3-4\left(1-\cos ^2 \mathrm{~B}\right)=4 \cos ^2 \mathrm{~B}-1 \\
& =4\left[\frac{\mathrm{c}^2+\mathrm{a}^2-\mathrm{b}^2}{2 \mathrm{ac}}\right]^2-1=4\left[\frac{\mathrm{b}^2}{2 \mathrm{ac}}\right]-1 \\
& =\left(\frac{2 \mathrm{~b}^2}{2 \mathrm{ac}}\right)-1=\left(\frac{\mathrm{a}^2+\mathrm{c}^2}{2 \mathrm{ac}}\right)-1=\left(\frac{\mathrm{a}^2+\mathrm{c}^2}{2 \mathrm{ac}}+1\right)\left(\frac{\mathrm{a}^2+\mathrm{c}^2}{2 \mathrm{ac}}-1\right) \\
& =\frac{(\mathrm{a}+\mathrm{c})^2(\mathrm{a}-\mathrm{c})^2}{(2 \mathrm{ac})^2} \\
& =\left[\frac{(\mathrm{a}+\mathrm{c})(\mathrm{a}-\mathrm{c})}{2 \mathrm{ac}}\right]=\left(\frac{\mathrm{a}^2-\mathrm{c}^2}{2 \mathrm{ac}}\right)^2
\end{aligned}
$$

</details>

---

### Q37. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{d x}{32-2 x^2}=A \log (4-x)+B \log (4+x)+c$, then the value of $\mathrm{A}$ and $\mathrm{B}$ are respectively (where $\mathrm{c}$ is a constant of integration)

**Options:**

- **(A)** $\frac{-1}{8}, \frac{1}{8}$
- **(B)** $\frac{1}{8}, \frac{-1}{8}$
- **(C)** $\frac{-1}{16}, \frac{1}{16}$
- **(D)** $\frac{1}{8}, \frac{1}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-1}{16}, \frac{1}{16}$**

**Detailed Solution:**

Let $I=\int \frac{d x}{32-2 x^2}$
$$
=\frac{1}{2}\left[\frac{1}{2(4)} \log \left|\frac{4+\mathrm{x}}{4-\mathrm{x}}\right|\right]+\mathrm{c}=\frac{1}{16}[\log |4+\mathrm{x}|-\log |4-\mathrm{x}|]+\mathrm{c}
$$
Comparing with given data we get $\mathrm{A}=\frac{-1}{16}, \mathrm{~B}=\frac{1}{16}$

</details>

---

### Q38. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\theta+\phi=\alpha$ and $\tan \theta=\mathrm{k} \tan \phi$ (where $\mathrm{K}>1)$, then the value of $\sin (\theta-\phi)$ is

**Options:**

- **(A)** $\mathrm{k} \tan \phi$
- **(B)** $\sin \alpha$
- **(C)** $\left(\frac{\mathrm{k}-1}{\mathrm{k}+1}\right) \sin \alpha$
- **(D)** $\mathrm{k} \cos \phi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\frac{\mathrm{k}-1}{\mathrm{k}+1}\right) \sin \alpha$**

**Detailed Solution:**

We have $\tan \theta=\mathrm{k} \tan \phi$ and $\theta+\phi=\alpha$
$$
\therefore \frac{\tan \theta}{\tan \phi}=\frac{k}{1}
$$
By Componendo Dividendo, we get
$$
\begin{aligned}
& \frac{\tan \theta+\tan \phi}{\tan \theta-\tan \phi}=\frac{\mathrm{k}+1}{\mathrm{k}-1} \\
& \therefore \frac{\frac{\sin \theta}{\cos \theta}+\frac{\sin \phi}{\cos \phi}}{\frac{\sin \theta}{\cos \theta}-\frac{\sin \phi}{\cos \phi}}=\frac{k+1}{k-1} \\
& \therefore \frac{\sin \cos \phi+\cos \theta \sin \phi}{\sin \theta \cos \phi-\cos \theta \sin \phi}=\frac{k+1}{k-1} \\
& \therefore \frac{\sin (\theta+\phi)}{\sin (\theta-\phi)}=\frac{\mathrm{k}+1}{\mathrm{k}-1} \Rightarrow \frac{\sin \alpha}{\sin (\theta-\phi)}=\frac{\mathrm{k}+1}{\mathrm{k}-1} \\
& \therefore \sin (\theta-\phi)=\frac{\mathrm{k}-1}{\mathrm{k}+1}(\sin \alpha) \\
&
\end{aligned}
$$

</details>

---

### Q39. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\sin ^{2}\left(\frac{\pi}{8}\right)=$

**Options:**

- **(A)** $\frac{\sqrt{2}+1}{2 \sqrt{2}}$
- **(B)** $\frac{\sqrt{5}+1}{2 \sqrt{2}}$
- **(C)** $\frac{\sqrt{5}-1}{2 \sqrt{2}}$
- **(D)** $\frac{\sqrt{2}-1}{2 \sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\sqrt{2}-1}{2 \sqrt{2}}$**

**Detailed Solution:**

$$
\begin{aligned}
\sin ^{2}\left(\frac{\pi}{8}\right) &=\frac{1-\cos 2\left(\frac{\pi}{8}\right)}{2} \\
&=\frac{1-\cos \frac{\pi}{4}}{2}=\frac{1-\frac{1}{\sqrt{2}}}{2}=\frac{\sqrt{2}-1}{2 \sqrt{2}}
\end{aligned}
$$

</details>

---

### Q40. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\operatorname{cosec} 2 \theta-\cot 2 \theta=$

**Options:**

- **(A)** $\tan \theta$
- **(B)** $\sin 2 \theta$
- **(C)** $\cos \theta$
- **(D)** $\tan 2 \theta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan \theta$**

**Detailed Solution:**

(D)
$\begin{aligned}
\operatorname{cosec} 2 \theta-\cot 2 \theta &=\frac{1}{\sin 2 \theta}-\frac{\cos 2 \theta}{\sin 2 \theta} \\
&=\frac{1-\cos 2 \theta}{\sin 2 \theta}=\frac{2 \sin ^{2} \theta}{2 \sin \theta \cos \theta}=\tan \theta
\end{aligned}$

</details>

---

### Q41. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle $\mathrm{ABC}$ if $\frac{\sin \mathrm{A}-\sin \mathrm{C}}{\cos \mathrm{C}-\cos \mathrm{A}}=\cot \mathrm{B}$, then $\mathrm{A}, \mathrm{B}, \mathrm{C}$ are in

**Options:**

- **(A)** Arithmetico - Geometric progression
- **(B)** Harmonic Progression
- **(C)** Geometric progression
- **(D)** Arithmetic progression

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Arithmetic progression**

**Detailed Solution:**

(D)
$\frac{\sin A-\sin C}{\cos C-\cos A}=\cot B$
$2 \cos \left(\frac{A+C}{2}\right) \cdot \sin \left(\frac{A-C}{2}\right)$
$2 \cdot \sin \left(\frac{A+C}{2}\right) \cdot \sin \left(\frac{A-C}{2}\right)$
$\cot \left(\frac{A+C}{2}\right)=\cot B \Rightarrow \frac{A+C}{2}=B \Rightarrow A+C=2 B$
$\therefore A, B, C$ are in A.P.

</details>

---

### Q42. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A, B, C$ are angles of a $\triangle A B C$, then $\tan 2 A+\tan 2 B+\tan 2 C=$

**Options:**

- **(A)** $\tan 2 A \tan 3 B \tan 2 C$
- **(B)** $\tan 2 A \tan 2 B \tan 2 C$
- **(C)** $\tan A \tan B \tan C$
- **(D)** $\tan 3 A \tan 2 B \tan 2 C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan 2 A \tan 2 B \tan 2 C$**

**Detailed Solution:**

$\begin{aligned} & \text { In } \Delta A B C, A+B+C=\pi \Rightarrow 2 A+2 B+2 C=2 \pi \\ \therefore & 2 A+2 B=2 \pi-2 C \Rightarrow \tan (2 A+2 B)=\tan (2 \pi-2 C)=-\tan 2 C \\ & \frac{\tan 2 A+\tan 2 B}{1-\tan 2 A \tan 2 B}=-\tan 2 C \\ \therefore & \tan 2 A+\tan 2 B=-\tan 2 C(1-\tan 2 A \tan 2 B) \\ \therefore & \tan 2 A+\tan 2 B+\tan 2 C=\tan 2 A \tan 2 B \tan 2 C \end{aligned}$

</details>

---

### Q43. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\sqrt{2+\sqrt{2+2 \cos 4 \theta}}=$

**Options:**

- **(A)** $2 \cos \theta$
- **(B)** $\frac{\cos \theta}{2}$
- **(C)** $\frac{\cos \theta}{\sqrt{2}}$
- **(D)** $\sqrt{2} \cdot \cos \theta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \cos \theta$**

**Detailed Solution:**

$\begin{aligned} \sqrt{2+\sqrt{2+2 \cos 4 \theta}} &=\sqrt{2+\sqrt{2(1+\cos 4 \theta)}} \\ &=\sqrt{2+\sqrt{2 \times 2 \cos ^{2} 2 \theta}}=\sqrt{2+2 \cos ^{2} 2 \theta} \\ &=\sqrt{2\left(1+\cos ^{2} 2 \theta\right)}=\sqrt{2 \times 2 \cos ^{2} \theta}=2 \cos \theta \end{aligned}$

</details>

---

### Q44. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\cos x+\cos y=-\cos \alpha, \sin x+\sin y=-\sin \alpha$, then $\cot \left(\frac{x+y}{2}\right)=$

**Options:**

- **(A)** $-\cot \propto$
- **(B)** $\cot \propto$
- **(C)** $-\tan \propto$
- **(D)** $\tan \propto$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\cot \propto$**

**Detailed Solution:**

Given $\cos x+\cos y=-\cos \alpha$ and $\sin x+\sin y=-\sin \alpha$
$2 \cos \left(\frac{x+y}{2}\right) \cos \left(\frac{x-y}{2}\right)=-\cos \alpha$ ...(1) and
$2 \sin \left(\frac{x+y}{2}\right) \cos \left(\frac{x-y}{2}\right)=-\sin \alpha$ ...(2)
Divided equation (1) by equation (2) 
$\cot \left(\frac{x+y}{2}\right)=\cot \alpha$

</details>

---

### Q45. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\tan ^{-1}\left(\frac{\sin 2 x}{1+\cos 2 x}\right)$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** $-1$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Given $y=\tan ^{-1}\left(\frac{\sin 2 x}{1+\cos 2 x}\right)=\tan ^{-1}\left(\frac{2 \sin x \cos x}{2 \cos ^{2} x}\right)=\tan ^{-1}(\tan x)$
$\therefore \quad y=x \Rightarrow \frac{d y}{d x}=1$

</details>

---

### Q46. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\tan \theta=\frac{1}{3}$, then $\cos 2 \theta=$

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{1}{10}$
- **(C)** $\frac{1}{5}$
- **(D)** $\frac{4}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{4}{5}$**

**Detailed Solution:**

$\cos 2 \theta=\frac{1-\tan ^{2} \theta}{1+\tan ^{2} \theta}=\frac{\left(1-\frac{1}{9}\right)}{\left(1+\frac{1}{9}\right)}=\frac{4}{5}$

</details>

---

### Q47. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\tan A=\frac{5}{6}, \tan B=\frac{1}{11}$, then $A+B=$

**Options:**

- **(A)** $\frac{-\pi}{4}$
- **(B)** $\frac{-\pi}{3}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} \tan (A+B) &=\frac{\tan A+\tan B}{1-\tan A \tan B} \\ &=\frac{\frac{5}{6}+\frac{1}{11}}{1-\frac{5}{6} \times \frac{1}{11}}=\frac{\frac{55+6}{66}}{1-\frac{5}{66}}=\frac{\left(\frac{61}{66}\right)}{\left(\frac{61}{66}\right)} \\ \tan (A+B) &=1 \Rightarrow A+B=\tan ^{-1}(1) \Rightarrow A+B=\frac{\pi}{4} \end{aligned}$

</details>

---

### Q48. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\sec 2 \theta-\tan 2 \theta=$

**Options:**

- **(A)** $\tan \left(\frac{\pi}{4}-\theta\right)$
- **(B)** $\tan 2 \theta$
- **(C)** $\cot 2 \theta$
- **(D)** $\cot \left(\frac{\pi}{4}-\theta\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan \left(\frac{\pi}{4}-\theta\right)$**

**Detailed Solution:**

$\begin{aligned} \sec 2 \theta-\tan 2 \theta &=\frac{1}{\cos 2 \theta}-\frac{\sin 2 \theta}{\cos 2 \theta}=\frac{1-\sin 2 \theta}{\cos 2 \theta} \\ &=\frac{(\cos \theta-\sin \theta)^{2}}{\cos ^{2} \theta-\sin ^{2} \theta}=\frac{(\cos \theta-\sin \theta)^{2}}{(\cos \theta-\sin \theta)(\cos \theta+\sin \theta)} \end{aligned}$
$=\frac{\cos \theta-\sin \theta}{\cos \theta+\sin \theta}=\frac{1-\tan \theta}{1+\tan \theta}=\frac{\tan \frac{\pi}{4}-\tan \theta}{1+\tan \frac{\pi}{4} \tan \theta}$
$=\tan \left(\frac{\pi}{4}-\theta\right)$

</details>

---

### Q49. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In <math><mi>Δ</mi><mi>A</mi><mi>B</mi><mi>C</mi></math> , if tan A + tan B + tan C = 6 and tan A.tan B = 2 then tan C = ……

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

Key Idea Use Identity . In <math><mi>Δ</mi><mi>A</mi><mi>B</mi><mi>C</mi></math>  
<math><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>A</mi><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>B</mi><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>C</mi><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>A</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>B</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>C</mi></math>  
We have, tan A + tan B + tan C = 6 
<math><mo>&#8658;</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>A</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>B</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>C</mi><mo>=</mo><mn>6</mn></math> ….(i) 
and tan A. tan B = 2 …..(ii) 
From Eqs. (i) and (ii) we get, tanC =3

</details>

---

### Q50. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced close="]" open="[" separators="|"><mrow><mn>3</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>0.4</mn></mrow></mfenced></mrow></mfenced></mrow></mrow><mo>=</mo></math> ….

**Options:**

- **(A)** 0.466
- **(B)** 0.256
- **(C)** 0.944
- **(D)** 0.764

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0.944**

**Detailed Solution:**

Let <math><mi>E</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced close="]" open="[" separators="|"><mrow><mn>3</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>0.4</mn></mrow></mfenced></mrow></mfenced></mrow></mrow></math>
put <math><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>0.4</mn></mrow></mfenced><mo>=</mo><mi>θ</mi><mo>⇒</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>=</mo><mn>0.4</mn></math>
<math><mo>∴</mo><mi>E</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>3</mn><mi>θ</mi></mrow></mfenced></mrow></mrow><mo>=</mo><mn>3</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi><mo>-</mo><mn>4</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>3</mn></mrow></msup><mi>θ</mi></math>
<math><mo>=</mo><mn>3</mn><mfenced separators="|"><mrow><mn>0.4</mn></mrow></mfenced><mo>-</mo><mn>4</mn><msup><mrow><mfenced separators="|"><mrow><mn>0.4</mn></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></math>
<math><mo>=</mo><mn>12</mn><mo>-</mo><mn>4</mn><mfenced separators="|"><mrow><mn>0.064</mn></mrow></mfenced></math>
<math><mo>=</mo><mn>12</mn><mo>-</mo><mn>0.25</mn><mn>6</mn></math>
<math><mo>=</mo><mn>0.94</mn><mn>4</mn></math>

</details>

---

