# MHT CET Mathematics - Properties of Triangles

## Topic 3: Napiers Analogy, Area of Triangle & Half angle Formulae

**Total Questions:** 45

---

### Q1. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle ABC$, if $b = \sqrt{3} + 1$, $c = \sqrt{3} - 1$ and $A = \dfrac{\pi}{3}$, then $B - C = \ldots$

**Options:**

- **(A)** $\dfrac{\pi}{18}$
- **(B)** $\dfrac{\pi}{12}$
- **(C)** $\dfrac{\pi}{4}$
- **(D)** $\dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\pi}{2}$**

**Detailed Solution:**

Using Napier's Analogy:

$\tan\left(\dfrac{B - C}{2}\right) = \dfrac{b - c}{b + c} \cot\left(\dfrac{A}{2}\right)$

Substituting the given values $b = \sqrt{3} + 1$, $c = \sqrt{3} - 1$, and $A = \dfrac{\pi}{3}$:

$b - c = (\sqrt{3} + 1) - (\sqrt{3} - 1) = 2$

$b + c = (\sqrt{3} + 1) + (\sqrt{3} - 1) = 2\sqrt{3}$

$\cot\left(\dfrac{A}{2}\right) = \cot\left(\dfrac{\pi}{6}\right) = \sqrt{3}$

$\tan\left(\dfrac{B - C}{2}\right) = \dfrac{2}{2\sqrt{3}} \times \sqrt{3} = 1$

$\dfrac{B - C}{2} = \dfrac{\pi}{4}$

$B - C = \dfrac{\pi}{2}$

Answer: $\dfrac{\pi}{2}$

</details>

---

### Q2. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle ABC$, with usual notations, the value of $\text{cosec}\left(\dfrac{A}{2}\right) \text{cosec}\left(\dfrac{B}{2}\right) \text{cosec}\left(\dfrac{C}{2}\right)$ is:

**Options:**

- **(A)** $\dfrac{[A\triangle ABC]^2}{abcs}$
- **(B)** $\dfrac{abcs}{[A\triangle ABC]^2}$
- **(C)** $\dfrac{[A\triangle ABC]}{abcs}$
- **(D)** $\dfrac{abcs}{[A\triangle ABC]}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{abcs}{[A\triangle ABC]^2}$**

**Detailed Solution:**

Using the half-angle formulas for a triangle:

$\sin\left(\dfrac{A}{2}\right) = \sqrt{\dfrac{(s-b)(s-c)}{bc}}$

$\sin\left(\dfrac{B}{2}\right) = \sqrt{\dfrac{(s-a)(s-c)}{ac}}$

$\sin\left(\dfrac{C}{2}\right) = \sqrt{\dfrac{(s-a)(s-b)}{ab}}$

Multiplying these expressions gives:

$\sin\left(\dfrac{A}{2}\right) \sin\left(\dfrac{B}{2}\right) \sin\left(\dfrac{C}{2}\right) = \dfrac{(s-a)(s-b)(s-c)}{abc}$

Using Heron's formula for the area of the triangle $\Delta$:

$\Delta = \sqrt{s(s-a)(s-b)(s-c)}$

Squaring both sides yields $\Delta^2 = s(s-a)(s-b)(s-c)$, which implies $(s-a)(s-b)(s-c) = \dfrac{\Delta^2}{s}$.

Substituting this into the product of sines:

$\sin\left(\dfrac{A}{2}\right) \sin\left(\dfrac{B}{2}\right) \sin\left(\dfrac{C}{2}\right) = \dfrac{\Delta^2}{abcs}$

The given expression is the reciprocal of the product of sines:

$\text{cosec}\left(\dfrac{A}{2}\right) \text{cosec}\left(\dfrac{B}{2}\right) \text{cosec}\left(\dfrac{C}{2}\right) = \dfrac{abcs}{\Delta^2}$

Replacing $\Delta$ with $[A\triangle ABC]$ gives $\dfrac{abcs}{[A\triangle ABC]^2}$.

Answer: $\dfrac{abcs}{[A\triangle ABC]^2}$

</details>

---

### Q3. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle ABC$, if $l(AB) = 8, l(BC) = 5, l(AC) = 7$, then $\cot \dfrac{A}{2} + \cot \dfrac{B}{2} + \cot \dfrac{C}{2}$ is equal to......

**Options:**

- **(A)** $\dfrac{10}{\sqrt{3}}$
- **(B)** $\dfrac{10}{3}$
- **(C)** $\dfrac{5}{\sqrt{3}}$
- **(D)** $\dfrac{\sqrt{3}}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{10}{\sqrt{3}}$**

**Detailed Solution:**

Given $a = 5$, $b = 7$, $c = 8$.

Semi-perimeter $s = \dfrac{a + b + c}{2} = \dfrac{5 + 7 + 8}{2} = 10$.

Area of the triangle $\Delta = \sqrt{s(s-a)(s-b)(s-c)} = \sqrt{10(10-5)(10-7)(10-8)} = \sqrt{10 \times 5 \times 3 \times 2} = 10\sqrt{3}$.

Using the half-angle formula $\cot \dfrac{A}{2} = \dfrac{s(s-a)}{\Delta}$, we have:

$\cot \dfrac{A}{2} + \cot \dfrac{B}{2} + \cot \dfrac{C}{2} = \dfrac{s(s-a)}{\Delta} + \dfrac{s(s-b)}{\Delta} + \dfrac{s(s-c)}{\Delta}$

$= \dfrac{s(3s - (a+b+c))}{\Delta}$

$= \dfrac{s(3s - 2s)}{\Delta} = \dfrac{s^2}{\Delta}$

Substituting the values of $s$ and $\Delta$:

$\dfrac{s^2}{\Delta} = \dfrac{10^2}{10\sqrt{3}} = \dfrac{10}{\sqrt{3}}$

Answer: $\dfrac{10}{\sqrt{3}}$

</details>

---

### Q4. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In $\Delta ABC$, with usual notations, if $1-\tan\dfrac{A}{2}\cdot\tan\dfrac{C}{2}=\dfrac{b}{k}$, then $k=$ ...

**Options:**

- **(A)** $s$
- **(B)** $2s$
- **(C)** $(s-a)$
- **(D)** $(s-a)(s-b)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $s$**

**Detailed Solution:**

Using the half-angle formulas for a triangle:

$\tan\dfrac{A}{2} = \sqrt{\dfrac{(s-b)(s-c)}{s(s-a)}}$

$\tan\dfrac{C}{2} = \sqrt{\dfrac{(s-a)(s-b)}{s(s-c)}}$

Multiplying these two expressions:

$\tan\dfrac{A}{2}\cdot\tan\dfrac{C}{2} = \sqrt{\dfrac{(s-b)(s-c)}{s(s-a)} \cdot \dfrac{(s-a)(s-b)}{s(s-c)}} = \dfrac{s-b}{s}$

Substituting this into the given equation:

$1 - \tan\dfrac{A}{2}\cdot\tan\dfrac{C}{2} = 1 - \dfrac{s-b}{s}$

$= \dfrac{s - (s-b)}{s} = \dfrac{b}{s}$

Given that $1 - \tan\dfrac{A}{2}\cdot\tan\dfrac{C}{2} = \dfrac{b}{k}$, we have:

$\dfrac{b}{s} = \dfrac{b}{k}$

$k = s$

Answer: $s$

</details>

---

### Q5. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle ABC$, with usual notations, $(a + b + c)(b + c - a)(c + a - b)(a + b - c) = 3b^2c^2$, then $\angle A = $

**Options:**

- **(A)** $60^\circ$ or $120^\circ$
- **(B)** $30^\circ$ or $150^\circ$
- **(C)** $45^\circ$ or $135^\circ$
- **(D)** $30^\circ$ or $90^\circ$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $60^\circ$ or $120^\circ$**

**Detailed Solution:**

Given $(a + b + c)(b + c - a)(c + a - b)(a + b - c) = 3b^2c^2$

Grouping the terms:

$((b + c) + a)((b + c) - a)(a - (b - c))(a + (b - c)) = 3b^2c^2$

$((b + c)^2 - a^2)(a^2 - (b - c)^2) = 3b^2c^2$

$(b^2 + c^2 + 2bc - a^2)(a^2 - (b^2 + c^2 - 2bc)) = 3b^2c^2$

$(2bc + (b^2 + c^2 - a^2))(2bc - (b^2 + c^2 - a^2)) = 3b^2c^2$

Using the algebraic identity $(x+y)(x-y) = x^2 - y^2$:

$4b^2c^2 - (b^2 + c^2 - a^2)^2 = 3b^2c^2$

$(b^2 + c^2 - a^2)^2 = b^2c^2$

$b^2 + c^2 - a^2 = \pm bc$

Dividing by $2bc$:

$\dfrac{b^2 + c^2 - a^2}{2bc} = \pm \dfrac{1}{2}$

Using the cosine rule, $\cos A = \dfrac{b^2 + c^2 - a^2}{2bc}$:

$\cos A = \pm \dfrac{1}{2}$

Since $0^\circ < A < 180^\circ$, we get $A = 60^\circ$ or $120^\circ$.

Answer: $60^\circ$ or $120^\circ$

</details>

---

### Q6. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If ABC is a triangle of area $\Delta$ with $a = 2, b = \dfrac{7}{2}, c = \dfrac{5}{2}$, where $a, b, c$ are the lengths of the sides of the triangle opposite to angles A, B and C respectively, then $\dfrac{2\sin A - \sin 2A}{2\sin A + \sin 2A}$ is equal to...

**Options:**

- **(A)** $\dfrac{3}{4\Delta}$
- **(B)** $\left(\dfrac{3}{4\Delta}\right)^2$
- **(C)** $\dfrac{45}{4\Delta}$
- **(D)** $\left(\dfrac{45}{4\Delta}\right)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\dfrac{3}{4\Delta}\right)^2$**

**Detailed Solution:**

Simplifying the given expression:

$\dfrac{2\sin A - \sin 2A}{2\sin A + \sin 2A} = \dfrac{2\sin A(1 - \cos A)}{2\sin A(1 + \cos A)}$

$\Rightarrow \dfrac{1 - \cos A}{1 + \cos A} = \tan^2 \dfrac{A}{2}$

Using the half-angle formula in terms of the area $\Delta$:

$\tan \dfrac{A}{2} = \dfrac{(s-b)(s-c)}{\Delta}$

Calculating the semi-perimeter $s$:

$s = \dfrac{a + b + c}{2} = \dfrac{2 + \dfrac{7}{2} + \dfrac{5}{2}}{2} = 4$

Evaluating $s-b$ and $s-c$:

$s - b = 4 - \dfrac{7}{2} = \dfrac{1}{2}$

$s - c = 4 - \dfrac{5}{2} = \dfrac{3}{2}$

Substituting these values:

$\tan \dfrac{A}{2} = \dfrac{\dfrac{1}{2} \times \dfrac{3}{2}}{\Delta} = \dfrac{3}{4\Delta}$

Squaring both sides gives:

$\tan^2 \dfrac{A}{2} = \left(\dfrac{3}{4\Delta}\right)^2$

Answer: $\left(\dfrac{3}{4\Delta}\right)^2$

</details>

---

### Q7. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle ABC$, with usual notations, if the sides $a$, $b$ and $c$ are in the ratio $18 : 17 : 7$, then $\cot\dfrac{A}{2} : \cot\dfrac{B}{2} : \cot\dfrac{C}{2} =$

**Options:**

- **(A)** $4 : 3 : 14$
- **(B)** $14 : 4 : 3$
- **(C)** $3 : 4 : 14$
- **(D)** $4 : 14 : 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3 : 4 : 14$**

**Detailed Solution:**

Let the sides of the triangle be $a = 18k$, $b = 17k$, and $c = 7k$.

The semi-perimeter $s$ is given by:

$s = \dfrac{a+b+c}{2} = \dfrac{18k + 17k + 7k}{2} = 21k$

Using the half-angle formula for cotangent:

$\cot\dfrac{A}{2} = \sqrt{\dfrac{s(s-a)}{(s-b)(s-c)}} = \dfrac{s(s-a)}{\Delta}$

Similarly, $\cot\dfrac{B}{2} = \dfrac{s(s-b)}{\Delta}$ and $\cot\dfrac{C}{2} = \dfrac{s(s-c)}{\Delta}$.

Thus, the required ratio is:

$\cot\dfrac{A}{2} : \cot\dfrac{B}{2} : \cot\dfrac{C}{2} = (s-a) : (s-b) : (s-c)$

Substituting the values of $s$, $a$, $b$, and $c$:

$s-a = 21k - 18k = 3k$

$s-b = 21k - 17k = 4k$

$s-c = 21k - 7k = 14k$

Therefore, the ratio is:

$3k : 4k : 14k = 3 : 4 : 14$

Answer: $3 : 4 : 14$

</details>

---

### Q8. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In $\triangle ABC$, with usual notations, if $\Delta$ denotes the area of triangle $ABC$ then the value of $2s(b+c-a)\tan\left(\dfrac{A}{2}\right)$ is equal to $\ldots$

**Options:**

- **(A)** $\Delta$
- **(B)** $2\Delta$
- **(C)** $3\Delta$
- **(D)** $4\Delta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4\Delta$**

**Detailed Solution:**

We know that the semi-perimeter of a triangle is given by $s = \dfrac{a+b+c}{2}$, which implies $2s = a+b+c$.

The term $b+c-a$ can be rewritten as:

$b+c-a = (a+b+c) - 2a = 2s - 2a = 2(s-a)$

Substituting this into the given expression, we get:

$2s(b+c-a)\tan\left(\dfrac{A}{2}\right) = 2s(2(s-a))\tan\left(\dfrac{A}{2}\right) = 4s(s-a)\tan\left(\dfrac{A}{2}\right)$

Using the half-angle formula for tangents in a triangle:

$\tan\left(\dfrac{A}{2}\right) = \sqrt{\dfrac{(s-b)(s-c)}{s(s-a)}}$

Multiplying the numerator and the denominator inside the square root by $s(s-a)$ gives:

$\tan\left(\dfrac{A}{2}\right) = \dfrac{\sqrt{s(s-a)(s-b)(s-c)}}{s(s-a)}$

By Heron's formula, the area of the triangle is $\Delta = \sqrt{s(s-a)(s-b)(s-c)}$. Therefore:

$\tan\left(\dfrac{A}{2}\right) = \dfrac{\Delta}{s(s-a)}$

Substituting this back into the modified expression:

$4s(s-a)\tan\left(\dfrac{A}{2}\right) = 4s(s-a) \times \dfrac{\Delta}{s(s-a)} = 4\Delta$

Answer: $4\Delta$

</details>

---

### Q9. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle ABC$, with usual notation, if $a = 13, b = 14, c = 15$, then the sum of the values of $\sin\left(\dfrac{A}{2}\right)$ and $\sin A$ is....

**Options:**

- **(A)** $\dfrac{14}{5\sqrt{5}}$
- **(B)** $\dfrac{\sqrt{5}+4}{5}$
- **(C)** $\dfrac{5+\sqrt{5}}{5}$
- **(D)** $\dfrac{2}{\sqrt{5}}+\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\sqrt{5}+4}{5}$**

**Detailed Solution:**

The semi-perimeter of the triangle is given by:

$s = \dfrac{a+b+c}{2} = \dfrac{13+14+15}{2} = 21$

Using Heron's formula, the area of the triangle is:

$\Delta = \sqrt{s(s-a)(s-b)(s-c)} = \sqrt{21 \times 8 \times 7 \times 6} = 84$

Using the area formula $\Delta = \dfrac{1}{2}bc \sin A$, we get:

$\sin A = \dfrac{2\Delta}{bc} = \dfrac{2 \times 84}{14 \times 15} = \dfrac{4}{5}$

Using the half-angle formula for sine:

$\sin\left(\dfrac{A}{2}\right) = \sqrt{\dfrac{(s-b)(s-c)}{bc}} = \sqrt{\dfrac{7 \times 6}{14 \times 15}} = \sqrt{\dfrac{1}{5}} = \dfrac{1}{\sqrt{5}}$

The required sum is:

$\sin\left(\dfrac{A}{2}\right) + \sin A = \dfrac{1}{\sqrt{5}} + \dfrac{4}{5} = \dfrac{\sqrt{5}}{5} + \dfrac{4}{5} = \dfrac{\sqrt{5}+4}{5}$

Answer: $\dfrac{\sqrt{5}+4}{5}$

</details>

---

### Q10. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle ABC, with usual notations $a = \sqrt{3} + 1$, $b = \sqrt{3} - 1$ and $\angle C = 60^\circ$ then the values of $\angle A$ and $\angle B$ respectively are

**Options:**

- **(A)** $105^\circ, 15^\circ$
- **(B)** $100^\circ, 20^\circ$
- **(C)** $90^\circ, 30^\circ$
- **(D)** $110^\circ, 10^\circ$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $105^\circ, 15^\circ$**

**Detailed Solution:**

Using Napier's Analogy:

$\tan\left(\dfrac{A - B}{2}\right) = \dfrac{a - b}{a + b} \cot\left(\dfrac{C}{2}\right)$

Substituting the given values $a = \sqrt{3} + 1$, $b = \sqrt{3} - 1$, and $C = 60^\circ$:

$a - b = 2$

$a + b = 2\sqrt{3}$

$\cot\left(\dfrac{C}{2}\right) = \cot 30^\circ = \sqrt{3}$

$\tan\left(\dfrac{A - B}{2}\right) = \dfrac{2}{2\sqrt{3}} \times \sqrt{3} = 1$

$\dfrac{A - B}{2} = 45^\circ \Rightarrow A - B = 90^\circ$

In $\triangle ABC$, the sum of angles is $180^\circ$:

$A + B + C = 180^\circ \Rightarrow A + B = 120^\circ$

Solving $A - B = 90^\circ$ and $A + B = 120^\circ$:

$2A = 210^\circ \Rightarrow A = 105^\circ$

$2B = 30^\circ \Rightarrow B = 15^\circ$

Answer: $105^\circ, 15^\circ$

</details>

---

### Q11. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In $\triangle ABC$ with usual notations, if $1 + \tan\left(\dfrac{A}{2}\right)\tan\left(\dfrac{B}{2}\right) = \dfrac{k}{s}$ (where $s$ is the semi-perimeter), then the value of $k$ is...

**Options:**

- **(A)** $2$
- **(B)** $a + b - c$
- **(C)** $a + b$
- **(D)** $s - c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $a + b$**

**Detailed Solution:**

Using the half-angle formulas for a triangle:

$\tan\left(\dfrac{A}{2}\right) = \sqrt{\dfrac{(s-b)(s-c)}{s(s-a)}}$

$\tan\left(\dfrac{B}{2}\right) = \sqrt{\dfrac{(s-a)(s-c)}{s(s-b)}}$

Multiplying these two expressions:

$\tan\left(\dfrac{A}{2}\right)\tan\left(\dfrac{B}{2}\right) = \sqrt{\dfrac{(s-b)(s-c)}{s(s-a)} \dfrac{(s-a)(s-c)}{s(s-b)}} = \dfrac{s-c}{s}$

Substituting this into the given equation:

$1 + \tan\left(\dfrac{A}{2}\right)\tan\left(\dfrac{B}{2}\right) = 1 + \dfrac{s-c}{s} = \dfrac{2s - c}{s}$

Since $2s = a + b + c$, we have $2s - c = a + b$.

Therefore, $1 + \tan\left(\dfrac{A}{2}\right)\tan\left(\dfrac{B}{2}\right) = \dfrac{a + b}{s}$

Comparing this with $\dfrac{k}{s}$, we get $k = a + b$.

Answer: $a + b$

</details>

---

### Q12. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle ABC, with usual notations if $\dfrac{s-a}{11} = \dfrac{s-b}{12} = \dfrac{s-c}{13}$ and $\lambda \tan^2 \dfrac{A}{2} = 455$, then $\lambda =$

**Options:**

- **(A)** $1155$
- **(B)** $1255$
- **(C)** $1355$
- **(D)** $1055$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1155$**

**Detailed Solution:**

Let $\dfrac{s-a}{11} = \dfrac{s-b}{12} = \dfrac{s-c}{13} = k$

$s-a = 11k$, $s-b = 12k$, $s-c = 13k$

Adding these three equations, we get:

$3s - (a+b+c) = 11k + 12k + 13k$

Since $a+b+c = 2s$, this becomes:

$3s - 2s = 36k \Rightarrow s = 36k$

Using the half-angle formula for tangents:

$\tan^2 \dfrac{A}{2} = \dfrac{(s-b)(s-c)}{s(s-a)}$

Substituting the values in terms of $k$:

$\tan^2 \dfrac{A}{2} = \dfrac{12k \times 13k}{36k \times 11k} = \dfrac{12 \times 13}{36 \times 11} = \dfrac{13}{33}$

Given that $\lambda \tan^2 \dfrac{A}{2} = 455$:

$\lambda \times \dfrac{13}{33} = 455$

$\lambda = \dfrac{455 \times 33}{13} = 35 \times 33 = 1155$

Answer: $1155$

</details>

---

### Q13. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle $P Q R$ with usual notations, $\angle R=\frac{\pi}{2}$. If $\tan \frac{P}{2}$ and $\tan \frac{Q}{2}$ are the roots of the equation $a x^2+b x+c=0 \quad(a \neq 0)$, then

**Options:**

- **(A)** $a+b=c$
- **(B)** $\mathrm{b}+\mathrm{c}=a$
- **(C)** $a+c=b$
- **(D)** $\mathrm{b}=\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $a+b=c$**

**Detailed Solution:**

Given $\angle R = \dfrac{\pi}{2}$, we have $P + Q = \dfrac{\pi}{2}$.

Dividing by 2, we get $\dfrac{P}{2} + \dfrac{Q}{2} = \dfrac{\pi}{4}$.

Taking $\tan$ on both sides:

$\tan\left(\dfrac{P}{2} + \dfrac{Q}{2}\right) = \tan \dfrac{\pi}{4} = 1$

$\dfrac{\tan \dfrac{P}{2} + \tan \dfrac{Q}{2}}{1 - \tan \dfrac{P}{2} \tan \dfrac{Q}{2}} = 1$

Since $\tan \dfrac{P}{2}$ and $\tan \dfrac{Q}{2}$ are the roots of the equation $a x^2+b x+c=0$, we have:

Sum of roots: $\tan \dfrac{P}{2} + \tan \dfrac{Q}{2} = -\dfrac{b}{a}$

Product of roots: $\tan \dfrac{P}{2} \tan \dfrac{Q}{2} = \dfrac{c}{a}$

Substituting these values into the equation:

$\dfrac{-\dfrac{b}{a}}{1 - \dfrac{c}{a}} = 1$

$\dfrac{-b}{a - c} = 1$

$-b = a - c$

$a + b = c$

Answer: $a+b=c$

</details>

---

### Q14. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle ABC , with usual notations, $\cot \left(\frac{A+B}{2}\right) \cdot \tan \left(\frac{A-B}{2}\right)=$

**Options:**

- **(A)** $\frac{a+b}{a-b}$
- **(B)** $\frac{a-b}{a+b}$
- **(C)** $\frac{a}{a+b}$
- **(D)** $\frac{\mathrm{b}}{a-\mathrm{b}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{a-b}{a+b}$**

**Detailed Solution:**

Using the definitions of cotangent and tangent:

$\cot \left(\dfrac{A+B}{2}\right) \cdot \tan \left(\dfrac{A-B}{2}\right) = \dfrac{\cos \left(\dfrac{A+B}{2}\right)}{\sin \left(\dfrac{A+B}{2}\right)} \cdot \dfrac{\sin \left(\dfrac{A-B}{2}\right)}{\cos \left(\dfrac{A-B}{2}\right)}$

Multiplying the numerator and the denominator by $2$:

$= \dfrac{2 \cos \left(\dfrac{A+B}{2}\right) \sin \left(\dfrac{A-B}{2}\right)}{2 \sin \left(\dfrac{A+B}{2}\right) \cos \left(\dfrac{A-B}{2}\right)}$

Using the trigonometric identities $2 \cos X \sin Y = \sin(X+Y) - \sin(X-Y)$ and $2 \sin X \cos Y = \sin(X+Y) + \sin(X-Y)$:

$= \dfrac{\sin A - \sin B}{\sin A + \sin B}$

By the Sine Rule, $\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = 2R$, which implies $\sin A = \dfrac{a}{2R}$ and $\sin B = \dfrac{b}{2R}$. Substituting these values:

$= \dfrac{\dfrac{a}{2R} - \dfrac{b}{2R}}{\dfrac{a}{2R} + \dfrac{b}{2R}} = \dfrac{a-b}{a+b}$

Answer: $\frac{a-b}{a+b}$

</details>

---

### Q15. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If in triangle $A B C$, with usual notations $\sin \frac{A}{2} \cdot \sin \frac{C}{2}=\sin \frac{B}{2}$ and $2 s$ is the perimeter of the triangle, then the value of $s$ is

**Options:**

- **(A)** 2b
- **(B)** b
- **(C)** 4b
- **(D)** $\frac{b}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2b**

**Detailed Solution:**

Using the half-angle formulas for a triangle:

$\sin \dfrac{A}{2} = \sqrt{\dfrac{(s-b)(s-c)}{bc}}$

$\sin \dfrac{C}{2} = \sqrt{\dfrac{(s-a)(s-b)}{ab}}$

$\sin \dfrac{B}{2} = \sqrt{\dfrac{(s-a)(s-c)}{ac}}$

Given the relation:

$\sin \dfrac{A}{2} \cdot \sin \dfrac{C}{2} = \sin \dfrac{B}{2}$

Substituting the formulas into the given equation:

$\sqrt{\dfrac{(s-b)(s-c)}{bc}} \cdot \sqrt{\dfrac{(s-a)(s-b)}{ab}} = \sqrt{\dfrac{(s-a)(s-c)}{ac}}$

Combining the terms under the square root on the left side:

$\sqrt{\dfrac{(s-b)^2 (s-a)(s-c)}{a b^2 c}} = \sqrt{\dfrac{(s-a)(s-c)}{ac}}$

Taking $(s-b)$ and $b$ out of the square root:

$\dfrac{s-b}{b} \sqrt{\dfrac{(s-a)(s-c)}{ac}} = \sqrt{\dfrac{(s-a)(s-c)}{ac}}$

Since $s > a$ and $s > c$ in any valid triangle, $\sqrt{\dfrac{(s-a)(s-c)}{ac}} \neq 0$. Dividing both sides by this term gives:

$\dfrac{s-b}{b} = 1$

$s - b = b$

$s = 2b$

Answer: 2b

</details>

---

### Q16. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle ABC with usual notations if $b \sin C(b \cos C+c \cos B)=42$, then area of triangle $A B C=$

**Options:**

- **(A)** 42 sq.units
- **(B)** 21 sq.units
- **(C)** 24 sq.units
- **(D)** 12 sq.units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 21 sq.units**

**Detailed Solution:**

Using the projection rule in triangle ABC:

$a = b \cos C + c \cos B$

Substituting this into the given equation:

$b \sin C (a) = 42$

$ab \sin C = 42$

The area of triangle ABC is given by:

$\Delta = \dfrac{1}{2} ab \sin C$

$\Delta = \dfrac{1}{2} \times 42 = 21$ sq. units.

Answer: 21 sq.units

</details>

---

### Q17. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle ABC with usual notations.
$\cot \frac{\mathrm{A}}{2}+\cot \frac{\mathrm{B}}{2}+\cot \frac{\mathrm{C}}{2}=$

**Options:**

- **(A)** $\frac{s^2}{\Delta}$, where $\Delta$ is the area of the triangle $A B C$.
- **(B)** $\frac{s}{\Delta}$, where $\Delta$ is the area of the triangle $A B C$.
- **(C)** $\frac{\triangle}{s}$, where $\triangle$ is the area of the triangle $A B C$.
- **(D)** $\Delta$, where $\Delta$ is the area of the triangle $A B C$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{s^2}{\Delta}$, where $\Delta$ is the area of the triangle $A B C$.**

**Detailed Solution:**

Using the half-angle formula for cotangent in a triangle:

$\cot \dfrac{A}{2} = \dfrac{s(s-a)}{\Delta}$

$\cot \dfrac{B}{2} = \dfrac{s(s-b)}{\Delta}$

$\cot \dfrac{C}{2} = \dfrac{s(s-c)}{\Delta}$

Adding these three expressions:

$\cot \dfrac{A}{2} + \cot \dfrac{B}{2} + \cot \dfrac{C}{2} = \dfrac{s(s-a)}{\Delta} + \dfrac{s(s-b)}{\Delta} + \dfrac{s(s-c)}{\Delta}$

$= \dfrac{s}{\Delta} [(s-a) + (s-b) + (s-c)]$

$= \dfrac{s}{\Delta} [3s - (a+b+c)]$

Since the perimeter of the triangle is $a+b+c = 2s$:

$= \dfrac{s}{\Delta} [3s - 2s]$

$= \dfrac{s}{\Delta} [s]$

$= \dfrac{s^2}{\Delta}$

Answer: $\frac{s^2}{\Delta}$, where $\Delta$ is the area of the triangle $A B C$.

</details>

---

### Q18. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle ABC with usual notations, if $3 a=\mathrm{b}+\mathrm{c}$, then $\cot \frac{B}{2} \cdot \cot \frac{C}{2}=$

**Options:**

- **(A)** $1$
- **(B)** $\sqrt{2}$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

Using the half-angle formulas for a triangle, we have:

$\cot \dfrac{B}{2} = \sqrt{\dfrac{s(s-b)}{(s-a)(s-c)}}$

$\cot \dfrac{C}{2} = \sqrt{\dfrac{s(s-c)}{(s-a)(s-b)}}$

Multiplying these two expressions gives:

$\cot \dfrac{B}{2} \cdot \cot \dfrac{C}{2} = \sqrt{\dfrac{s(s-b)}{(s-a)(s-c)} \cdot \dfrac{s(s-c)}{(s-a)(s-b)}} = \sqrt{\dfrac{s^2}{(s-a)^2}} = \dfrac{s}{s-a}$

The semi-perimeter of the triangle is given by $2s = a + b + c$.

Given that $3a = b + c$, we substitute this into the perimeter equation:

$2s = a + 3a = 4a$

$s = 2a$

Substituting $s = 2a$ into the simplified product:

$\cot \dfrac{B}{2} \cdot \cot \dfrac{C}{2} = \dfrac{2a}{2a - a} = \dfrac{2a}{a} = 2$

Answer: $2$

</details>

---

### Q19. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle ABC with usual notations if, $\cot \frac{A}{2}=\frac{b+c}{a}$, then the triangle $A B C$ is

**Options:**

- **(A)** an isosceles triangle.
- **(B)** an equilateral triangle.
- **(C)** a right angled triangle.
- **(D)** an obtuse angled triangle.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) a right angled triangle.**

**Detailed Solution:**

Using the Sine Rule, $a = 2R \sin A$, $b = 2R \sin B$, $c = 2R \sin C$.

Substituting these into the given equation:

$\cot \dfrac{A}{2} = \dfrac{2R \sin B + 2R \sin C}{2R \sin A} = \dfrac{\sin B + \sin C}{\sin A}$

Using sum-to-product formulas and half-angle formulas:

$\dfrac{\cos \dfrac{A}{2}}{\sin \dfrac{A}{2}} = \dfrac{2 \sin \left(\dfrac{B+C}{2}\right) \cos \left(\dfrac{B-C}{2}\right)}{2 \sin \dfrac{A}{2} \cos \dfrac{A}{2}}$

Since $A + B + C = \pi$, we have $\sin \left(\dfrac{B+C}{2}\right) = \cos \dfrac{A}{2}$.

$\dfrac{\cos \dfrac{A}{2}}{\sin \dfrac{A}{2}} = \dfrac{\cos \dfrac{A}{2} \cos \left(\dfrac{B-C}{2}\right)}{\sin \dfrac{A}{2} \cos \dfrac{A}{2}}$

$\dfrac{\cos \dfrac{A}{2}}{\sin \dfrac{A}{2}} = \dfrac{\cos \left(\dfrac{B-C}{2}\right)}{\sin \dfrac{A}{2}}$

$\cos \dfrac{A}{2} = \cos \left(\dfrac{B-C}{2}\right)$

This implies $\dfrac{A}{2} = \pm \dfrac{B-C}{2}$.

If $\dfrac{A}{2} = \dfrac{B-C}{2}$, then $A = B - C \Rightarrow B = A + C$.

Since $A + B + C = \pi$, we get $2B = \pi \Rightarrow B = \dfrac{\pi}{2}$.

If $\dfrac{A}{2} = -\dfrac{B-C}{2}$, then $A = C - B \Rightarrow C = A + B$.

Since $A + B + C = \pi$, we get $2C = \pi \Rightarrow C = \dfrac{\pi}{2}$.

In both cases, one angle is $\dfrac{\pi}{2}$, so the triangle is a right angled triangle.

Answer: a right angled triangle.

</details>

---

### Q20. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle ABC with usual notations if, $\tan \left(\frac{\mathrm{B}-\mathrm{C}}{2}\right)=x \cot \frac{\mathrm{~A}}{2}$, then $x=$

**Options:**

- **(A)** $\frac{c-a}{c+a}$
- **(B)** $\frac{a-b}{a+b}$
- **(C)** $\frac{b-c}{b+c}$
- **(D)** $\frac{a+b}{a-b}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{b-c}{b+c}$**

**Detailed Solution:**

Using the Sine Rule, $\dfrac{b}{\sin B} = \dfrac{c}{\sin C} = k$

Consider the expression $\dfrac{b-c}{b+c}$:

$\dfrac{b-c}{b+c} = \dfrac{k\sin B - k\sin C}{k\sin B + k\sin C} = \dfrac{\sin B - \sin C}{\sin B + \sin C}$

Using the sum-to-product formulas:

$\dfrac{b-c}{b+c} = \dfrac{2\cos\left(\dfrac{B+C}{2}\right)\sin\left(\dfrac{B-C}{2}\right)}{2\sin\left(\dfrac{B+C}{2}\right)\cos\left(\dfrac{B-C}{2}\right)}$

$\dfrac{b-c}{b+c} = \cot\left(\dfrac{B+C}{2}\right)\tan\left(\dfrac{B-C}{2}\right)$

Since $A+B+C = \pi$, we have $\dfrac{B+C}{2} = \dfrac{\pi}{2} - \dfrac{A}{2}$

$\cot\left(\dfrac{B+C}{2}\right) = \cot\left(\dfrac{\pi}{2} - \dfrac{A}{2}\right) = \tan\dfrac{A}{2}$

Substituting this back, we get:

$\dfrac{b-c}{b+c} = \tan\dfrac{A}{2}\tan\left(\dfrac{B-C}{2}\right)$

$\tan\left(\dfrac{B-C}{2}\right) = \dfrac{b-c}{b+c}\cot\dfrac{A}{2}$

Comparing this with the given equation $\tan \left(\dfrac{B-C}{2}\right) = x \cot \dfrac{A}{2}$, we get:

$x = \dfrac{b-c}{b+c}$

Answer: $\frac{b-c}{b+c}$

</details>

---

### Q21. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle ABC , with usual notations , $\tan \left(\frac{\mathrm{A}}{2}\right)=\frac{5}{6}, \tan \left(\frac{\mathrm{C}}{2}\right)=\frac{2}{5}$, then

**Options:**

- **(A)** $\mathrm{a}, \mathrm{c}, \mathrm{b}$ are in A.P.
- **(B)** $\mathrm{b}, \mathrm{a}, \mathrm{c}$ are in A.P.
- **(C)** $\mathrm{a}, \mathrm{b}, \mathrm{c}$ are in A.P.
- **(D)** $\mathrm{a}, \mathrm{b}, \mathrm{c}$ are in G.P.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{a}, \mathrm{b}, \mathrm{c}$ are in A.P.**

**Detailed Solution:**

Using the half-angle formulas for a triangle:

$\tan\left(\dfrac{A}{2}\right) = \sqrt{\dfrac{(s-b)(s-c)}{s(s-a)}}$

$\tan\left(\dfrac{C}{2}\right) = \sqrt{\dfrac{(s-a)(s-b)}{s(s-c)}}$

Multiplying these two expressions:

$\tan\left(\dfrac{A}{2}\right) \tan\left(\dfrac{C}{2}\right) = \sqrt{\dfrac{(s-b)(s-c)}{s(s-a)} \times \dfrac{(s-a)(s-b)}{s(s-c)}} = \dfrac{s-b}{s}$

Substituting the given values:

$\dfrac{5}{6} \times \dfrac{2}{5} = \dfrac{s-b}{s}$

$\dfrac{1}{3} = \dfrac{s-b}{s}$

$s = 3s - 3b$

$2s = 3b$

Since $2s = a + b + c$:

$a + b + c = 3b$

$a + c = 2b$

This is the condition for $a, b, c$ to be in an Arithmetic Progression (A.P.).

Answer: $\mathrm{a}, \mathrm{b}, \mathrm{c}$ are in A.P.

</details>

---

### Q22. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle ABC , with usual notations, $3 \mathrm{~b}=\mathrm{a}+\mathrm{c}$, then $\cot \frac{\mathrm{A}}{2} \cdot \cot \frac{\mathrm{c}}{2}=$

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $\frac{1}{2}$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

Using the half-angle formulas for a triangle:

$\cot \dfrac{A}{2} = \sqrt{\dfrac{s(s-a)}{(s-b)(s-c)}}$

$\cot \dfrac{C}{2} = \sqrt{\dfrac{s(s-c)}{(s-a)(s-b)}}$

Multiplying these two expressions:

$\cot \dfrac{A}{2} \cdot \cot \dfrac{C}{2} = \sqrt{\dfrac{s(s-a)}{(s-b)(s-c)} \cdot \dfrac{s(s-c)}{(s-a)(s-b)}}$

$\cot \dfrac{A}{2} \cdot \cot \dfrac{C}{2} = \sqrt{\dfrac{s^2}{(s-b)^2}} = \dfrac{s}{s-b}$

We are given that $3b = a + c$.

Adding $b$ to both sides:

$4b = a + b + c$

Since the perimeter $2s = a + b + c$, we have:

$2s = 4b \Rightarrow s = 2b$

Substituting $s = 2b$ into the simplified product:

$\cot \dfrac{A}{2} \cdot \cot \dfrac{C}{2} = \dfrac{2b}{2b - b} = \dfrac{2b}{b} = 2$

Answer: $2$

</details>

---

### Q23. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle ABC with usual notations, if $\mathrm{a}, \mathrm{b}, \mathrm{c}$ are in arithmetic progression, then, $\tan \frac{A}{2} \cdot \tan \frac{C}{2}=$

**Options:**

- **(A)** $3$
- **(B)** $\frac{1}{13}$
- **(C)** $-3$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{3}$**

**Detailed Solution:**

Given $a, b, c$ are in arithmetic progression, we have $2b = a + c$.

The semi-perimeter of the triangle is $s = \dfrac{a+b+c}{2}$.

Substituting $a+c = 2b$, we get $s = \dfrac{2b+b}{2} = \dfrac{3b}{2}$.

Using the half-angle formulas for a triangle:

$\tan \dfrac{A}{2} = \sqrt{\dfrac{(s-b)(s-c)}{s(s-a)}}$

$\tan \dfrac{C}{2} = \sqrt{\dfrac{(s-a)(s-b)}{s(s-c)}}$

Multiplying the two expressions:

$\tan \dfrac{A}{2} \cdot \tan \dfrac{C}{2} = \sqrt{\dfrac{(s-b)(s-c)}{s(s-a)} \cdot \dfrac{(s-a)(s-b)}{s(s-c)}}$

$\tan \dfrac{A}{2} \cdot \tan \dfrac{C}{2} = \sqrt{\dfrac{(s-b)^2}{s^2}} = \dfrac{s-b}{s}$

Substituting $s = \dfrac{3b}{2}$:

$\tan \dfrac{A}{2} \cdot \tan \dfrac{C}{2} = \dfrac{\dfrac{3b}{2} - b}{\dfrac{3b}{2}} = \dfrac{\dfrac{b}{2}}{\dfrac{3b}{2}} = \dfrac{1}{3}$

Answer: $\frac{1}{3}$

</details>

---

### Q24. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The ratios of sides in a triangle $A B C$ are $5: 12: 13$ and its area is 270 .
Then sides of the triangle are

**Options:**

- **(A)** $5,12,13$
- **(B)** $10,24,26$
- **(C)** $15,36,39$
- **(D)** $20,48,52$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $15,36,39$**

**Detailed Solution:**

Let the sides of the triangle be $a = 5x$, $b = 12x$, and $c = 13x$.

Since $(5x)^2 + (12x)^2 = 25x^2 + 144x^2 = 169x^2 = (13x)^2$, the triangle is a right-angled triangle with hypotenuse $13x$.

The area of the right-angled triangle is $\dfrac{1}{2} \times \text{base} \times \text{height}$.

Area $= \dfrac{1}{2} \times 5x \times 12x = 30x^2$

Given that the area is $270$, we have $30x^2 = 270$.

$x^2 = 9 \Rightarrow x = 3$

The sides of the triangle are $5(3), 12(3), 13(3)$, which are $15, 36, 39$.

Answer: $15,36,39$

</details>

---

### Q25. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

With usual notations, if the lengths of the sides of a triangle are $7 \mathrm{~cm}, 4 \sqrt{3} \mathrm{~cm}$ and $\sqrt{13} \mathrm{~cm}$, then the measures of the smallest angle is

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{6}$**

**Detailed Solution:**

Let $a = 7$, $b = 4\sqrt{3}$, and $c = \sqrt{13}$.

Since $c$ is the smallest side, the smallest angle is $C$.

Using the cosine rule:

$\cos C = \dfrac{a^2 + b^2 - c^2}{2ab}$

Substituting the given values:

$\cos C = \dfrac{7^2 + (4\sqrt{3})^2 - (\sqrt{13})^2}{2(7)(4\sqrt{3})}$

$\cos C = \dfrac{49 + 48 - 13}{56\sqrt{3}}$

$\cos C = \dfrac{84}{56\sqrt{3}}$

$\cos C = \dfrac{3}{2\sqrt{3}} = \dfrac{\sqrt{3}}{2}$

Therefore, $C = \dfrac{\pi}{6}$.

Answer: $\frac{\pi}{6}$

</details>

---

### Q26. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $(\mathrm{a}+\mathrm{b}) \cos \mathrm{C}+(\mathrm{b}+\mathrm{c}) \cos \mathrm{A}+(\mathrm{c}+\mathrm{a}) \cos \mathrm{B}=72$ and if $\mathrm{a}=18, \mathrm{~b}=24$, then area of the triangle ABC is

**Options:**

- **(A)** 144 sq.units
- **(B)** 216 sq.units
- **(C)** 256 sq.units
- **(D)** 296 sq.units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 216 sq.units**

**Detailed Solution:**

The given equation is:

$(a+b) \cos C + (b+c) \cos A + (c+a) \cos B = 72$

Expanding the terms, we get:

$a \cos C + b \cos C + b \cos A + c \cos A + c \cos B + a \cos B = 72$

Rearranging and grouping the terms:

$(a \cos C + c \cos A) + (b \cos C + c \cos B) + (a \cos B + b \cos A) = 72$

Using the projection formula in a triangle ($a = b \cos C + c \cos B$, $b = a \cos C + c \cos A$, $c = a \cos B + b \cos A$), the equation simplifies to:

$b + a + c = 72$

Substituting the given values $a = 18$ and $b = 24$:

$18 + 24 + c = 72$

$42 + c = 72 \Rightarrow c = 30$

The sides of the triangle are $a = 18$, $b = 24$, and $c = 30$.

Checking the sum of the squares of the two smaller sides:

$a^2 + b^2 = 18^2 + 24^2 = 324 + 576 = 900$

Since $c^2 = 30^2 = 900$, we have $a^2 + b^2 = c^2$. This means the triangle is right-angled at $C$.

The area of the right-angled triangle is:

$\Delta = \dfrac{1}{2}ab = \dfrac{1}{2} \times 18 \times 24 = 216 \text{ sq. units}$

Answer: 216 sq.units

</details>

---

### Q27. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the angles $\mathrm{A}, \mathrm{B}$ and $\mathrm{C}$ of a triangle are in an Arithmetic Progression and if $\mathrm{a}, \mathrm{b}$ and $\mathrm{c}$ denote the lengths of the sides opposite to A, B and C respectively, then the value of the expression $\frac{\mathrm{a}}{\mathrm{c}} \sin 2 \mathrm{C}+\frac{\mathrm{c}}{\mathrm{a}} \sin 2 \mathrm{~A}$ is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{\sqrt{3}}{2}$
- **(C)** $1$
- **(D)** $\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{3}$**

**Detailed Solution:**

A, B, C are in A.P.
$$
\begin{array}{ll}
\therefore \quad & A+C=2 B \\
& \text { Also, } A+B+C=180^{\circ} \\
& \angle B=60^{\circ} \\
& B y \operatorname{sine} \text { rule, } \\
& \frac{\sin A}{a}=\frac{\sin B}{b}=\frac{\sin C}{c}=k \\
\therefore \quad & \sin A=a k, \sin B=b k, \sin C=c k \\
\therefore \quad & \frac{a}{c} \sin 2 C+\frac{c}{a} \sin 2 A \\
& =\frac{a}{c}(2 \sin C \cos C)+\frac{c}{a}(2 \sin A \cos A) \\
& =\frac{a}{c}(2 \operatorname{ck} \cos C)+\frac{c}{a}(2 a k \cos A) \\
& =2 k a \cos C+2 k c \cos A \\
& =2 k(a \cos C+c \cos A)
\end{array}
$$
$\begin{array}{ll}=2 \mathrm{~kb} & \ldots[\because b=\mathrm{a} \cos \mathrm{C}+\mathrm{c} \cos \mathrm{A}] \\ =2 \sin \mathrm{B} & \\ =2 \times \frac{\sqrt{3}}{2} & \ldots \ldots\left[\because \angle \mathrm{B}=60^{\circ}\right] \\ =\sqrt{3} & \end{array}$

</details>

---

### Q28. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle \mathrm{ABC}$, with usual notations, $2 \mathrm{ac} \sin \left(\frac{1}{2}(\mathrm{~A}-\mathrm{B}+\mathrm{C})\right)$ is equal to

**Options:**

- **(A)** $a^2+b^2-c^2$
- **(B)** $c^2+a^2-b^2$
- **(C)** $b^2-c^2-a^2$
- **(D)** $c^2-a^2-b^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $c^2+a^2-b^2$**

**Detailed Solution:**

$\begin{aligned} 2 \mathrm{ac} \sin \frac{\mathrm{A}-\mathrm{B}+\mathrm{C}}{2} & =2 \mathrm{ac} \sin \frac{\pi-2 \mathrm{~B}}{2} \\ & =2 \mathrm{ac} \cos \mathrm{B}\end{aligned}$
$$
=2 \mathrm{ac} \frac{\mathrm{c}^2+\mathrm{a}^2-\mathrm{b}^2}{2 \mathrm{ca}}
$$....[By cosine rule $]$
$=c^2+a^2-b^2$

</details>

---

### Q29. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle \mathrm{ABC}$, with usual notations, if $\frac{b+c}{11}=\frac{c+a}{12}=\frac{a+b}{13}$, then the value of $\cos \mathrm{A}+\cos \mathrm{B}+\cos \mathrm{C}$ is

**Options:**

- **(A)** $\frac{17}{35}$
- **(B)** $\frac{51}{35}$
- **(C)** $\frac{5}{7}$
- **(D)** $\frac{19}{35}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{51}{35}$**

**Detailed Solution:**

Let $\frac{\mathrm{b}+\mathrm{c}}{11}=\frac{\mathrm{c}+\mathrm{a}}{12}=\frac{\mathrm{a}+\mathrm{b}}{13}=\mathrm{k}$
$\therefore \quad b+c=11 k$    ...(i)
$c+a=12 k$                              ...(ii)
and $a+b=13 k$                      ...(iii)
From (i) $+($ ii) + (iii), $2(a+b+c)=36 k$
$\therefore \quad a+b+c=18 k$                   ...(iv)
Now, (iv) - (i) gives, $a=7 k$
(iv) - (ii) gives, $b=6 \mathrm{k}$
(iv) - (iii) gives, $c=5 \mathrm{k}$
Now,
$\begin{aligned} \cos A & =\frac{b^2+c^2-a^2}{2 b c} \\ & =\frac{(6 k)^2+(5 k)^2-(7 k)^2}{2 \times(6 k) \times(5 k)} \\ & =\frac{36 k^2+25 k^2-49 k^2}{60 k^2} \\ & =\frac{12 k^2}{60 k^2} \\ & =\frac{1}{5}\end{aligned}$
$\begin{aligned} \cos \mathrm{B} & =\frac{\mathrm{c}^2+\mathrm{a}^2-\mathrm{b}^2}{2 \mathrm{ca}} \\ & =\frac{(5 \mathrm{k})^2+(7 \mathrm{k})^2-(6 \mathrm{k})^2}{2 \times(5 \mathrm{k}) \times(7 \mathrm{k})} \\ & =\frac{25 \mathrm{k}^2+49 \mathrm{k}^2-36 \mathrm{k}^2}{70 \mathrm{k}^2} \\ & =\frac{38 \mathrm{k}^2}{70 \mathrm{k}^2} \\ & =\frac{19}{35}\end{aligned}$
$\begin{aligned} \cos C & =\frac{\mathrm{a}^2+\mathrm{b}^2-\mathrm{c}^2}{2 \mathrm{ab}}=\frac{(7 \mathrm{k})^2+(6 \mathrm{k})^2-(5 \mathrm{k})^2}{2 \times(7 \mathrm{k}) \times(6 \mathrm{k})} \\ & =\frac{49 \mathrm{k}^2+36 \mathrm{k}^2-25 \mathrm{k}^2}{84 \mathrm{k}^2}=\frac{60 \mathrm{k}^2}{84 \mathrm{k}^2}=\frac{5}{7}\end{aligned}$
$\therefore \quad \cos \mathrm{A}+\cos \mathrm{B}+\cos \mathrm{C}=\frac{1}{5}+\frac{19}{35}+\frac{5}{7}$
$\begin{aligned} & =\frac{7+19+25}{35} \\ & =\frac{51}{35}\end{aligned}$

</details>

---

### Q30. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle \mathrm{ABC}$ with usual notation, $\frac{\cos \mathrm{A}}{\mathrm{a}}=\frac{\cos \mathrm{B}}{\mathrm{b}}=\frac{\cos \mathrm{C}}{\mathrm{c}}$ and $\mathrm{a}=\frac{1}{\sqrt{6}}$, then the area of triangle is

**Options:**

- **(A)** $\frac{1}{8}$ sq. units.
- **(B)** $\frac{1}{24 \sqrt{3}}$
- **(C)** $\frac{1}{24}$
- **(D)** $\frac{1}{8 \sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{8 \sqrt{3}}$**

**Detailed Solution:**

If $\frac{\cos A}{a}=\frac{\cos B}{b}=\frac{\cos C}{c}$, then the triangle is equilateral.
$$
\begin{aligned}
\therefore \quad \mathrm{A}(\triangle \mathrm{ABC}) & =\frac{\sqrt{3}}{4} \mathrm{a}^2 \\
& =\frac{\sqrt{3}}{4}\left(\frac{1}{\sqrt{6}}\right)^2 \\
& =\frac{\sqrt{3}}{24}=\frac{1}{8 \sqrt{3}} \text { sq. units }
\end{aligned}
$$

</details>

---

### Q31. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In $\triangle \mathrm{ABC}, \mathrm{m} \angle \mathrm{B}=\frac{\pi}{3}$ and $\mathrm{m} \angle \mathrm{C}=\frac{\pi}{4}$. Let point $\mathrm{D}$ divide $\mathrm{BC}$ internally in the ratio $1: 3$, then $\frac{\sin (\angle B A D)}{\sin (\angle C A D)}$ has the value

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{1}{\sqrt{3}}$
- **(C)** $\frac{1}{\sqrt{6}}$
- **(D)** $\sqrt{\frac{2}{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{\sqrt{6}}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/aCCRNgcfRpo--m7l7-6uAfCpdiNXY3ce-4umBtGM77U.original.fullsize.png">

In $\triangle \mathrm{ABD}$,
$$
\begin{aligned}
& \frac{\sin (\angle \mathrm{BAD})}{\mathrm{BD}}=\frac{\sin (\angle \mathrm{ABD})}{\mathrm{AD}} \\
& \Rightarrow \frac{\sin (\angle \mathrm{BAD})}{x}=\frac{\frac{\sqrt{3}}{2}}{\mathrm{AD}} \\
& \Rightarrow \mathrm{AD}=\frac{\sqrt{3} x}{2 \sin (\angle \mathrm{BAD})}
\end{aligned}
$$

In $\triangle \mathrm{ADC}$,
$$
\begin{aligned}
& \frac{\sin (\angle \mathrm{CAD})}{\mathrm{DC}}=\frac{\sin (\angle \mathrm{ACD})}{\mathrm{AD}} \\
\Rightarrow & \frac{\sin (\angle \mathrm{CAD})}{3 x}=\frac{\frac{1}{\sqrt{2}}}{\mathrm{AD}} \\
\therefore \quad & \mathrm{AD}=\frac{3 x}{\sqrt{2} \sin (\angle \mathrm{CAD})}
\end{aligned}
$$

From (i) and (ii), we get
$$
\begin{aligned}
& \frac{\sqrt{3} x}{2 \sin (\angle \mathrm{BAD})}=\frac{3 x}{\sqrt{2} \sin (\angle \mathrm{CAD})} \\
\therefore \quad & \frac{\sin (\angle \mathrm{BAD})}{\sin (\angle \mathrm{CAD})}=\frac{\sqrt{6}}{6}=\frac{1}{\sqrt{6}}
\end{aligned}
$$

</details>

---

### Q32. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If two angles of $\triangle \mathrm{ABC}$ are $\frac{\pi}{4}$ and $\frac{\pi}{3}$, then the ratio of the smallest and greatest sides are

**Options:**

- **(A)** $(\sqrt{3}-1): 1$
- **(B)** $\sqrt{3}: \sqrt{5}$
- **(C)** $\sqrt{2}: \sqrt{3}$
- **(D)** $(\sqrt{3}-1): 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(\sqrt{3}-1): 1$**

**Detailed Solution:**

Let three angles of the triangle be given as $\mathrm{A}=\frac{\pi}{4}, \mathrm{~B}=\frac{\pi}{3}$ and $\mathrm{C}=\frac{\pi}{4}+\frac{\pi}{6}$

Let a, b, c be the opposite to angles A, B, C respectively.

As $\frac{\sin A}{a}=\frac{\sin C}{c}$, we get
$$
\text { Required Ratio }=\frac{\mathrm{a}}{\mathrm{c}}=\frac{\sin \mathrm{A}}{\sin \mathrm{C}}
$$
$$
=\frac{\sin \left(\frac{\pi}{4}\right)}{\sin \left(\frac{\pi}{4}+\frac{\pi}{6}\right)}
$$
$\begin{aligned} & =\frac{\sin \frac{\pi}{4}}{\sin \frac{\pi}{4} \cos \frac{\pi}{6}+\cos \frac{\pi}{4} \sin \frac{\pi}{6}} \\ & =\frac{2}{\sqrt{3}+1} \\ & =\frac{2(\sqrt{3}-1)}{2} \\ & =(\sqrt{3}-1): 1\end{aligned}$

</details>

---

### Q33. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $D, E$ and $F$ are the mid-points of the sides $B C$, $\mathrm{CA}$ and $\mathrm{AB}$ of triangle $\mathrm{ABC}$ respectively, then $\overline{\mathrm{AD}}+\frac{2}{3} \overline{\mathrm{BE}}+\frac{1}{3} \overline{\mathrm{CF}}=$

**Options:**

- **(A)** $\frac{1}{2} \overline{\mathrm{AB}}$
- **(B)** $\frac{1}{2} \overline{\mathrm{AC}}$
- **(C)** $\frac{1}{2} \overline{\mathrm{BC}}$
- **(D)** $\frac{2}{3} \overline{\mathrm{AC}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2} \overline{\mathrm{AC}}$**

**Detailed Solution:**

Let the position vector of A, B, C, D, E, F be $\overline{\mathrm{a}}, \overline{\mathrm{b}}, \overline{\mathrm{c}}, \overline{\mathrm{d}}, \overline{\mathrm{e}}, \overline{\mathrm{f}}$ respectively.
$\begin{aligned}
\therefore \quad \overline{\mathrm{d}} & =\frac{\overline{\mathrm{b}}+\overline{\mathrm{c}}}{2}, \overline{\mathrm{e}}=\frac{\overline{\mathrm{c}}+\overline{\mathrm{a}}}{2}, \overline{\mathrm{f}}=\frac{\overline{\mathrm{a}}+\overline{\mathrm{b}}}{2} \\
& \text { Now, } \overline{\mathrm{AD}}+\frac{2}{3} \overline{\mathrm{BE}}+\frac{1}{3} \overline{\mathrm{CF}} \\
& =\overline{\mathrm{d}}-\overline{\mathrm{a}}+\frac{2}{3}(\overline{\mathrm{e}}-\overline{\mathrm{b}})+\frac{1}{3}(\overline{\mathrm{f}}-\overline{\mathrm{c}}) \\
& =\frac{\overline{\mathrm{b}}+\overline{\mathrm{c}}}{2}-\overline{\mathrm{a}}+\frac{2}{3}\left(\frac{\overline{\mathrm{c}}+\overline{\mathrm{a}}}{2}-\overline{\mathrm{b}}\right)+\frac{1}{3}\left(\frac{\overline{\mathrm{a}}+\overline{\mathrm{b}}}{2}-\overline{\mathrm{c}}\right) \\
& =\frac{\overline{\mathrm{b}}+\overline{\mathrm{c}}-2 \overline{\mathrm{a}}}{2}+\frac{\overline{\mathrm{c}}+\overline{\mathrm{a}}-2 \overline{\mathrm{b}}}{3}+\frac{\overline{\mathrm{a}}+\overline{\mathrm{b}}-2 \overline{\mathrm{c}}}{6} \\
& =\frac{3 \overline{\mathrm{c}}-3 \overline{\mathrm{a}}}{6} \\
& =\frac{3}{6}(\overline{\mathrm{c}}-\overline{\mathrm{a}}) \\
& =\frac{1}{2} \overline{\mathrm{AC}}
\end{aligned}$

</details>

---

### Q34. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $a, b, c$ be the lengths of sides of triangle $\mathrm{ABC}$ such that $\frac{\mathrm{a}+\mathrm{b}}{7}=\frac{\mathrm{b}+\mathrm{c}}{8}=\frac{\mathrm{c}+\mathrm{a}}{9}=\mathrm{k}$. Then $\frac{(\mathrm{A}(\triangle \mathrm{ABC}))^2}{\mathrm{k}^4}=$

**Options:**

- **(A)** 36
- **(B)** 32
- **(C)** 38
- **(D)** 40

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 36**

**Detailed Solution:**

$\begin{aligned}
& \Rightarrow \text { In } \triangle \mathrm{ABC} \text {, } \\
& \frac{\mathrm{a}+\mathrm{b}}{7}=\frac{\mathrm{b}+\mathrm{c}}{8}=\frac{\mathrm{c}+\mathrm{a}}{9} \Rightarrow \mathrm{k} \\
& \therefore \quad \mathrm{a}+\mathrm{b}=7 \mathrm{k} ...(i)\\
& \mathrm{b}+\mathrm{c}=8 \mathrm{k} ... (ii) \\
& \mathrm{c}+\mathrm{a}=9 \mathrm{k} ... (iii)\\
&
\end{aligned}$
Adding above equations,
$\begin{aligned}
& 2 a+2 b+2 c=24 k \\
& a+b+c=12 k ... (iv)
\end{aligned}$
Solving equations (i), (ii), (iii), (iv)
We get,
$\begin{array}{ll} 
& \mathrm{c}=5 \mathrm{k}, \mathrm{a}=4 \mathrm{k}, \mathrm{b}=3 \mathrm{k} \\
\therefore \quad & \mathrm{c}^2=\mathrm{a}^2+\mathrm{b}^2
\end{array}$
$\therefore \quad \triangle \mathrm{ABC}$ is right angled triangle
$\therefore \quad \angle \mathrm{C}=90^{\circ}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/TQW6zR96FLrOo3-DMRsMJqg9gEaxmVEvPaOSyrgxuIw.original.fullsize.png">

$\begin{aligned} & \text { Area of } \begin{aligned} \triangle \mathrm{ABC} & =\frac{1}{2} \mathrm{ab} \sin \mathrm{C} \\ & =\frac{1}{2} \mathrm{ab} \sin 90 \\ & =\frac{1}{2} \times 4 \mathrm{k} \times 3 \mathrm{k} \\ & =6 \mathrm{k}^2\end{aligned} \\ & \therefore \quad \text { Now, } \frac{[\mathrm{A}(\Delta \mathrm{ABC})]^2}{\mathrm{k}^4}=\frac{\left(6 \mathrm{k}^2\right)^2}{\mathrm{k}^4}=\frac{36 \mathrm{k}^4}{\mathrm{k}^4}=36\end{aligned}$

</details>

---

### Q35. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle $A B C$, with usual notations, if $\frac{b+c}{11}=\frac{c+a}{12}=\frac{a+b}{13}$, then $\cos A: \cos B: \cos C=$

**Options:**

- **(A)** 11:12:13
- **(B)** 25:19:7
- **(C)** 7:19:25
- **(D)** $19: 7: 25$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7:19:25**

**Detailed Solution:**

$\begin{aligned} & \frac{b+c}{11}=\frac{c+a}{12}=\frac{a+b}{13}=k(\text { say }) \\ & \Rightarrow a+b+c=18 k \\ & \Rightarrow a=7 k, b=6 k, c=5 k\end{aligned}$
Using cosine rule
$\begin{aligned} & \cos A=\frac{1}{5}, \cos B=\frac{19}{35}, \cos C=\frac{5}{7} \\ & \Rightarrow \cos A: \cos B: \cos C=\frac{1}{5}: \frac{19}{35}: \frac{5}{7}=7: 19: 25\end{aligned}$

</details>

---

### Q36. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle $A B C$, with usual notations, if $b=\sqrt{3}, c=1, \angle A=30^{\circ}$, then angle $B$ is

**Options:**

- **(A)** $60^{\circ}$
- **(B)** $90^{\circ}$
- **(C)** $30^{\circ}$
- **(D)** $120^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $120^{\circ}$**

**Detailed Solution:**

$\begin{aligned} & \cos A=\frac{b^2+c^2-a^2}{2 b c} \\ & \Rightarrow \cos 30^{\circ}=\frac{3+1-a^2}{2 \times \sqrt{3} \times 1} \\ & \Rightarrow \frac{\sqrt{3}}{2}=\frac{4-a^2}{2 \sqrt{3}} \\ & \Rightarrow a=1\end{aligned}$
Now $\cos B=\frac{c^2+a^2-b^2}{2 c a}=\frac{1^2+1^2-(\sqrt{3})^2}{2 \times 1 \times 1}=-\frac{1}{2}$
$\Rightarrow B=120^{\circ}$

</details>

---

### Q37. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a triangle $\mathrm{ABC}$, with usual notations $\angle A=60^{\circ}$, then $\left(1+\frac{a}{c}+\frac{b}{c}\right)\left(1+\frac{c}{b}-\frac{a}{b}\right)=$

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** $\frac{1}{2}$
- **(C)** 1
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

$\begin{aligned} & \left(1+\frac{a}{c}+\frac{b}{c}\right)\left(1+\frac{c}{b}-\frac{a}{b}\right)=\frac{a+b+c}{c} \times \frac{b+c-a}{b}=\frac{(b+c)^2-a^2}{b c} \\ & =\frac{b^2+c^2-a^2+2 b c}{b c}=2\left(\frac{b^2+c^2-a^2}{2 b c}\right)+2 \\ & =2 \cos A+2=2 \cos 60^{\circ}+2=2 \times \frac{1}{2}+2=3\end{aligned}$

</details>

---

### Q38. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

With usual notations, In $\triangle \mathrm{ABC}, \angle \mathrm{C}=90^{\circ}$, then the value of $\sin (\mathrm{A}-\mathrm{B})$ is

**Options:**

- **(A)** $\frac{a^2+b^2}{a^2-b^2}$
- **(B)** $\frac{a^2-b^2}{a^2+b^2}$
- **(C)** $\frac{\mathrm{a}^2+\mathrm{b}^2}{\mathrm{a}^2}$
- **(D)** $\frac{a^2-b^2}{b^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{a^2-b^2}{a^2+b^2}$**

**Detailed Solution:**

$\begin{aligned} & \because \angle C=90^{\circ} \\ & \Rightarrow \angle A+\angle B=90^{\circ} \\ & \Rightarrow \sin c=1 \text { and } \sin (A+B)=1\end{aligned}$
Also $\mathrm{c}^2=\mathrm{a}^2+\mathrm{b}^2$
$\begin{aligned} & \text { Now } \sin (A-B)=\frac{\sin (A-B) \cdot \sin (A+B)}{\sin ^2 C}=\frac{\sin ^2 A-\sin ^2 B}{\sin ^2 C} \\ & =\frac{k^2 a^2-k^2 b^2}{k^2 c^2}=\frac{a^2-b^2}{c^2}=\frac{a^2-b^2}{a^2+b^2}\end{aligned}$

</details>

---

### Q39. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The area of the triangle $\mathrm{ABC}$ is $10 \sqrt{3} \mathrm{~cm}^2$, angle $\mathrm{B}$ is $60^{\circ}$ and its perimeter is $20 \mathrm{~cm}$, then $\ell(\mathrm{AC})=$

**Options:**

- **(A)** 10 cm
- **(B)** 8 cm
- **(C)** 5 cm
- **(D)** 7 cm

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 7 cm**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Area }=\frac{\operatorname{acsin} B}{2}=\Rightarrow 10 \sqrt{3}=\frac{\operatorname{acsin} 60^{\circ}}{2} \\
& 10 \sqrt{3}=\frac{a c \sqrt{3}}{4} \Rightarrow a c=40
\end{aligned}
$$
Now
$$
\begin{aligned}
& \cos B=\frac{a^2+c^2-b^2}{2 a c} \\
& \cos 60^{\circ} \times 2 a c=a^2+c^2-b^2 \\
& \therefore \frac{1}{2} \times 2 \times 40=\left(a^2+c^2\right)-2 a c-b^2 \\
& \therefore 40=(20-b)^2-(2 \times 40)-b^2 \quad \ldots[a+b+c=20, \text { given }] \\
& =400+b^2-40 b-80-b^2 \\
& \therefore 40 b=280 \Rightarrow b=7
\end{aligned}
$$

</details>

---

### Q40. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the triangle $\mathrm{ABC}$ is $10 \sqrt{3} \mathrm{~cm}^{2}$, angle $\mathrm{B}$ is $60^{\circ}$ and its perimeter is $20 \mathrm{~cm}$,
then $\ell(\mathrm{AC})=$

**Options:**

- **(A)** $7 \mathrm{~cm}$
- **(B)** $8 \mathrm{~cm}$
- **(C)** $10 \mathrm{~cm}$
- **(D)** $5 \mathrm{~cm}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $7 \mathrm{~cm}$**

**Detailed Solution:**

(D)
$\begin{array}{l}
\text { Area }=\frac{\operatorname{acsin} B}{2}=10 \sqrt{3}=\frac{\operatorname{acsin} 60}{2} \\
10 \sqrt{3}=\frac{\operatorname{ac} \sqrt{3}}{4} a c=40
\end{array}$
Now
$\begin{aligned} & \cos \mathrm{B}=\frac{\mathrm{a}^{2}+\mathrm{c}^{2}-\mathrm{b}^{2}}{2 \mathrm{ac}} \\ & \cos 60 \times 2 \mathrm{ac}=\mathrm{a}^{2}+\mathrm{c}^{2}-\mathrm{b}^{2} \\ \therefore & \frac{1}{2} \times 2 \times 40=(\mathrm{a}+\mathrm{c})^{2}-2 \mathrm{ac}-\mathrm{b}^{2} \end{aligned}$
$\therefore 40=(20-b)^{2}-(2 \times 40)-b^{2} \quad \ldots[a+b+c=20$, given $]$
$\begin{aligned} &=400+b^{2}-40 b-80-b^{2} \\ \therefore \quad 40 b &=280 \Rightarrow b=7 \end{aligned}$

</details>

---

### Q41. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

With usual notations, if in $\triangle \mathrm{ABC}, 8$ is semi perimeter and $(\mathrm{s}-a)(\mathrm{s}-\mathrm{b})=\mathrm{s}(\mathrm{s}-\mathrm{c})$,
then $\triangle A B C$ is

**Options:**

- **(A)** an equilateral triangle
- **(B)** an obtuse angle triangle
- **(C)** a right angled triangle
- **(D)** an acute angle triangle

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) a right angled triangle**

**Detailed Solution:**

We have
$\begin{array}{l}
\sin \frac{C}{2}=\sqrt{\frac{(s-a)(s-b)}{a b}} \Rightarrow \sin ^{2} \frac{C}{2}=\frac{(s-a)(s-b)}{a b} \text { and } \\
\cos \frac{C}{2}=\sqrt{\frac{s(s-c)}{a b}} \Rightarrow \cos ^{2} \frac{C}{2}=\frac{s(s-c)}{a b} \\
\text { Given }(s-a)(s-b)=s(s-c) \\
\therefore \quad a b \sin ^{2} \frac{C}{2}=a b \cos ^{2} \frac{C}{2}
\end{array}$
$\therefore \tan ^{2} \frac{C}{2}=1 \Rightarrow \tan \frac{C}{2}=1 \Rightarrow \frac{C}{2}=45^{\circ} \Rightarrow C=90^{\circ}$
$\therefore \triangle \mathrm{ABC}$ is a right angled triangle

</details>

---

### Q42. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

With usual notations, in $\Delta \mathrm{ABC}$, if $\mathrm{b} \cos ^{2} \frac{\mathrm{C}}{2}+\mathrm{c} \cos ^{2} \frac{\mathrm{B}}{2}=\frac{3 \mathrm{a}}{2}$, then

**Options:**

- **(A)** $\mathrm{b}, \mathrm{a}, \mathrm{c}$ are in A.P.
- **(B)** $\mathrm{b}, \mathrm{a}, \mathrm{c}$ are in G.P.
- **(C)** $\mathrm{a}, \mathrm{b}, \mathrm{c}$ are in G.P.
- **(D)** $\mathrm{a}, \mathrm{b}, \mathrm{c}$ are in A.P.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{b}, \mathrm{a}, \mathrm{c}$ are in A.P.**

**Detailed Solution:**

Given $\mathrm{b} \cos ^{2} \frac{\mathrm{C}}{2}+\mathrm{c} \cos ^{2} \frac{\mathrm{B}}{2}=\frac{3 \mathrm{a}}{2}$
$\therefore \quad \mathrm{b}\left(\frac{1+\cos \mathrm{C}}{2}\right)+\mathrm{c}\left(\frac{1+\cos \mathrm{B}}{2}\right)=\frac{3 \mathrm{a}}{2}$
$\therefore \mathrm{b}+\mathrm{b} \cos \mathrm{C}+\mathrm{c}+\mathrm{C} \cos \mathrm{B}=3 \mathrm{a} \Rightarrow(\mathrm{b} \cos \mathrm{C}+\mathrm{c} \cos \mathrm{B})+\mathrm{b}+\mathrm{c}=3 \mathrm{a}$
$\quad \mathrm{a}+\mathrm{b}+\mathrm{c}=3 \mathrm{a} \Rightarrow \mathrm{b}+\mathrm{c}=2 \mathrm{a} \Rightarrow \mathrm{a}=\frac{\mathrm{b}+\mathrm{c}}{2}$
$\therefore \quad \mathrm{b}, \mathrm{a}, \mathrm{c}$ are in A.P.

</details>

---

### Q43. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In <math><mi>Δ</mi><mi>A</mi><mi>B</mi><mi>C</mi><mi></mi></math> with the usual notations, if <math><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mi>B</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math> then <math><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo></math> …

**Options:**

- **(A)** 4c
- **(B)** 2c
- **(C)** 7c
- **(D)** 3c

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7c**

**Detailed Solution:**

We have, In <math><mi>Δ</mi><mi>A</mi><mi>B</mi><mi>C</mi></math>  
<math><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mi>B</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>  
<math><mo>&#8658;</mo><msqrt><mfrac><mrow><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>c</mi></mrow></mfenced></mrow><mrow><mi>s</mi><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>a</mi></mrow></mfenced></mrow></mfrac></msqrt><msqrt><mfrac><mrow><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>c</mi></mrow></mfenced></mrow><mrow><mi>s</mi><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>b</mi></mrow></mfenced></mrow></mfrac></msqrt><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>  
<math><mo>&#8658;</mo><msqrt><mfrac><mrow><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>c</mi></mrow></mfenced></mrow><mrow><mi>s</mi><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mo>.</mo><mi>s</mi><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>b</mi></mrow></mfenced></mrow></mfrac></msqrt><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>  
<math><mo>&#8658;</mo><mfrac><mrow><mfenced separators="|"><mrow><mi>s</mi><mo>-</mo><mi>c</mi></mrow></mfenced></mrow><mrow><mi>s</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>&#8658;</mo><mfrac><mrow><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi>c</mi></mrow><mrow><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>  
<math><mo>&#8658;</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>c</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>  
<math><mo>&#8658;</mo><mn>4</mn><mi>a</mi><mo>+</mo><mn>4</mn><mi>b</mi><mo>-</mo><mn>4</mn><mi>c</mi><mo>=</mo><mn>3</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>+</mo><mn>3</mn><mi>c</mi></math>  
<math><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>7</mn><mi>c</mi></math>

</details>

---

### Q44. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `3`

In <math><mi mathvariant="normal">Δ</mi><mi>A</mi><mi>B</mi><mi>C</mi></math> if <math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>A</mi></mrow></mrow><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>B</mi></mrow></mrow><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>C</mi></mrow></mrow></math> and <math><mi>l</mi><mfenced separators="|"><mrow><mi>A</mi><mi>B</mi></mrow></mfenced><mo>=</mo><mn>10</mn><mo>,</mo></math> then the maximum value of the area of <math><mi mathvariant="normal">Δ</mi><mi>A</mi><mi>B</mi><mi>C</mi></math> is

**Options:**

- **(A)** <math><mn>50</mn></math>
- **(B)** <math><mn>10</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math><mn>25</mn></math>
- **(D)** <math><mn>25</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>25</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/vcjwpetzcyipzyduknsohwiojxuliqdpiszpdbsjwegehldkrf.jpeg" />
<math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>A</mi></mrow></mrow><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>B</mi></mrow></mrow><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>C</mi></mrow></mrow></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></math> (Sine Rule) <math><mo>⇒</mo></math> Right Angled<math><mo>∆</mo></math>
 <math >  <mrow>   <mo>&#x21D2;</mo><mi>C</mi><mo>=</mo><msup>    <mrow>     <mn>90</mn></mrow>    <mi>o</mi>   </msup>   <mo>,</mo><mtext>&#x2009;</mtext><mtext>&#x2009;</mtext><mi>B</mi><mo>=</mo><msup>    <mrow>     <mn>90</mn></mrow>    <mi>o</mi>   </msup>   <mo>&#x2212;</mo><mi>A</mi></mrow></math> 
Also Area <math><mi>A</mi><mi> </mi><mfenced separators="|"><mrow><mi mathvariant="normal">Δ</mi><mi>A</mi><mi>B</mi><mi>C</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>a</mi><mi>b</mi></math> ..........(i)
<math>  <mrow>   <mo>=</mo><mfrac>    <mn>1</mn>    <mn>2</mn>   </mfrac>   <mrow><mo>(</mo>    <mrow>     <mi>c</mi><mi>sin</mi><mi>A</mi></mrow>   <mo>)</mo></mrow><mrow><mo>(</mo>    <mrow>     <mi>c</mi><mi>cos</mi><mi>A</mi></mrow>   <mo>)</mo></mrow></mrow></math> 
<math >  <mrow>   <mo>=</mo><mn>50</mn><mi>sin</mi><mi>A</mi><mi>cos</mi><mi>A</mi><mo>=</mo><mn>25</mn><mi>sin</mi><mi>A</mi><mo>&#x2264;</mo><mn>25</mn></mrow></math>
So maximum value of <math>  <mrow>   <mi>&#x0394;</mi><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><mn>25</mn></mrow></math>

</details>

---

### Q45. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

In <math> <mi>A</mi><mi>B</mi><mi>C</mi><mi> </mi><msup> <mrow><mo>(</mo> <mrow> <mi>a</mi><mo>−</mo><mi>b</mi> </mrow> <mo>)</mo></mrow> <mn>2</mn> </msup> <msup> <mi>cos</mi> <mn>2</mn> </msup> <mfrac> <mi>C</mi> <mn>2</mn> </mfrac> <mo>+</mo><msup> <mrow><mo>(</mo> <mrow> <mi>a</mi><mo>+</mo><mi>b</mi> </mrow> <mo>)</mo></mrow> <mn>2</mn> </msup> <msup> <mi>sin</mi> <mn>2</mn> </msup> <mfrac> <mi>C</mi> <mn>2</mn> </mfrac> <mo>=</mo><mi> </mi> </math>

**Options:**

- **(A)** <math><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(B)** <math><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

Let <math><mi>X</mi><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></mrow></mrow></math>
<math><mo>=</mo><mo>(</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>)</mo><mo>(</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>)</mo><mo>-</mo><mn>2</mn><mi>a</mi><mi>b</mi><mi> </mi><mo>(</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>)</mo></mrow></mrow></mrow></mrow></mrow></mrow></mrow></mrow></math>
<math><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>a</mi><mi>b</mi><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>C</mi></mrow></mrow></math>
<math><mo>=</mo><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup><mi> </mi><mi> </mi><mi> </mi><mo>&because;</mo><mo>(</mo><mi>c</mi><mi>o</mi><mi>s</mi><mi>i</mi><mi>n</mi><mi>e</mi><mi> rule</mi><mo>)</mo></math>

</details>

---

