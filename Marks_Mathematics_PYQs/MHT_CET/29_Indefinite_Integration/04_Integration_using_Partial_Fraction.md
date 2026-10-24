# MHT CET Mathematics - Indefinite Integration

## Topic 4: Integration using Partial Fraction

**Total Questions:** 33

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{dx}{(x + 2)(x^2 + 1)}$ is equal to

**Options:**

- **(A)** $\dfrac{1}{5}\log|x + 2| - \dfrac{1}{10}\log(x^2 + 1) + \dfrac{2}{5}\tan^{-1} x + C$
- **(B)** $\log|x + 2| + \dfrac{1}{10}\log(x^2 + 1) + \dfrac{1}{5}\tan^{-1} x + C$
- **(C)** $5\log|x + 2| + 10\log(x^2 + 1) + \tan^{-1} x + C$
- **(D)** $\log|x + 2| + \dfrac{1}{10}\log(x^2 + 1) - \dfrac{1}{5}\tan^{-1} x + C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{5}\log|x + 2| - \dfrac{1}{10}\log(x^2 + 1) + \dfrac{2}{5}\tan^{-1} x + C$**

**Detailed Solution:**

Let the given integral be $I = \int \dfrac{dx}{(x + 2)(x^2 + 1)}$.

Using partial fractions, we can write:
$\dfrac{1}{(x + 2)(x^2 + 1)} = \dfrac{A}{x + 2} + \dfrac{Bx + C}{x^2 + 1}$

Multiplying both sides by $(x + 2)(x^2 + 1)$, we get:
$1 = A(x^2 + 1) + (Bx + C)(x + 2)$

Substituting $x = -2$, we get:
$1 = A((-2)^2 + 1) \Rightarrow 1 = 5A \Rightarrow A = \dfrac{1}{5}$

Comparing the coefficients of $x^2$ on both sides:
$0 = A + B \Rightarrow B = -A = -\dfrac{1}{5}$

Comparing the constant terms on both sides:
$1 = A + 2C \Rightarrow 1 = \dfrac{1}{5} + 2C \Rightarrow 2C = \dfrac{4}{5} \Rightarrow C = \dfrac{2}{5}$

Substituting the values of $A$, $B$, and $C$ back into the partial fraction decomposition:
$\dfrac{1}{(x + 2)(x^2 + 1)} = \dfrac{1/5}{x + 2} + \dfrac{-1/5 x + 2/5}{x^2 + 1}$

Now, integrating both sides with respect to $x$:
$I = \dfrac{1}{5} \int \dfrac{dx}{x + 2} - \dfrac{1}{5} \int \dfrac{x}{x^2 + 1} dx + \dfrac{2}{5} \int \dfrac{dx}{x^2 + 1}$

For the second integral, multiply and divide by $2$:
$I = \dfrac{1}{5} \int \dfrac{dx}{x + 2} - \dfrac{1}{10} \int \dfrac{2x}{x^2 + 1} dx + \dfrac{2}{5} \int \dfrac{dx}{x^2 + 1}$

Using standard integration formulas:
$I = \dfrac{1}{5}\log|x + 2| - \dfrac{1}{10}\log(x^2 + 1) + \dfrac{2}{5}\tan^{-1} x + C$

Answer: $\dfrac{1}{5}\log|x + 2| - \dfrac{1}{10}\log(x^2 + 1) + \dfrac{2}{5}\tan^{-1} x + C$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{2x}{4 - 3x - x^2}\ dx = \ldots$

**Options:**

- **(A)** $-\dfrac{8}{5}\log|4 - x| - \dfrac{2}{5}\log|1 + x| + c$
- **(B)** $-\dfrac{2}{5}\log|4 + x| - \dfrac{8}{5}\log|1 - x| + c$
- **(C)** $-\dfrac{2}{5}\log|4 - x| - \dfrac{8}{5}\log|1 + x| + c$
- **(D)** $-\dfrac{8}{5}\log|4 + x| - \dfrac{2}{5}\log|1 - x| + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\dfrac{8}{5}\log|4 + x| - \dfrac{2}{5}\log|1 - x| + c$**

**Detailed Solution:**

Let $I = \int \dfrac{2x}{4 - 3x - x^2}\ dx$

Factorizing the denominator, we get:
$4 - 3x - x^2 = (4+x)(1-x)$

Using partial fractions:
$\dfrac{2x}{(4+x)(1-x)} = \dfrac{A}{4+x} + \dfrac{B}{1-x}$

$2x = A(1-x) + B(4+x)$

Substituting $x = 1$, we get:
$2 = 5B \Rightarrow B = \dfrac{2}{5}$

Substituting $x = -4$, we get:
$-8 = 5A \Rightarrow A = -\dfrac{8}{5}$

Therefore, the integral becomes:
$I = \int \left( \dfrac{-8/5}{4+x} + \dfrac{2/5}{1-x} \right)\ dx$

Integrating each term:
$I = -\dfrac{8}{5}\log|4+x| + \dfrac{2}{5}\left(\dfrac{\log|1-x|}{-1}\right) + c$

$I = -\dfrac{8}{5}\log|4+x| - \dfrac{2}{5}\log|1-x| + c$

Answer: $-\dfrac{8}{5}\log|4 + x| - \dfrac{2}{5}\log|1 - x| + c$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\displaystyle\int \dfrac{dx}{x^4 + x^3}$ is

**Options:**

- **(A)** $-\dfrac{1}{2x^2} + \dfrac{1}{x} + \log\left|\dfrac{x}{x+1}\right| + c$
- **(B)** $\dfrac{1}{2x^2} + \dfrac{1}{x} + \log\left|\dfrac{x}{x+1}\right| + c$
- **(C)** $-\dfrac{1}{2x^2} - \dfrac{1}{x} + \log\left|\dfrac{x}{x+1}\right| + c$
- **(D)** $-\dfrac{1}{2x^2} - \dfrac{1}{x} - \log\left|\dfrac{x}{x+1}\right| + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\dfrac{1}{2x^2} + \dfrac{1}{x} + \log\left|\dfrac{x}{x+1}\right| + c$**

**Detailed Solution:**

$I = \displaystyle\int \dfrac{dx}{x^4 + x^3} = \displaystyle\int \dfrac{dx}{x^3(x + 1)}$

We can rewrite the integrand as:

$\dfrac{1}{x^3(x+1)} = \dfrac{(x+1)-x}{x^3(x+1)} = \dfrac{1}{x^3} - \dfrac{1}{x^2(x+1)}$

$= \dfrac{1}{x^3} - \dfrac{(x+1)-x}{x^2(x+1)} = \dfrac{1}{x^3} - \dfrac{1}{x^2} + \dfrac{1}{x(x+1)}$

$= \dfrac{1}{x^3} - \dfrac{1}{x^2} + \dfrac{(x+1)-x}{x(x+1)} = \dfrac{1}{x^3} - \dfrac{1}{x^2} + \dfrac{1}{x} - \dfrac{1}{x+1}$

Integrating each term with respect to $x$:

$I = \displaystyle\int \left( \dfrac{1}{x^3} - \dfrac{1}{x^2} + \dfrac{1}{x} - \dfrac{1}{x+1} \right) dx$

$I = -\dfrac{1}{2x^2} - \left(-\dfrac{1}{x}\right) + \log|x| - \log|x+1| + c$

$I = -\dfrac{1}{2x^2} + \dfrac{1}{x} + \log\left|\dfrac{x}{x+1}\right| + c$

Answer: $-\dfrac{1}{2x^2} + \dfrac{1}{x} + \log\left|\dfrac{x}{x+1}\right| + c$

</details>

---

### Q4. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int\dfrac{3x + 7}{x^2 - 3x + 2}\, dx = m\log\left(\dfrac{x - 2}{x - 1}\right) + n\log(x - 2) + c$, where $m, n \in R$ and $c$ is an integration constant, then $m + n =$

**Options:**

- **(A)** $6$
- **(B)** $7$
- **(C)** $3$
- **(D)** $13$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $13$**

**Detailed Solution:**

Let $I = \int\dfrac{3x + 7}{x^2 - 3x + 2}\, dx = \int\dfrac{3x + 7}{(x - 1)(x - 2)}\, dx$

Using partial fractions, let $\dfrac{3x + 7}{(x - 1)(x - 2)} = \dfrac{A}{x - 1} + \dfrac{B}{x - 2}$

$3x + 7 = A(x - 2) + B(x - 1)$

Substituting $x = 1$, we get $10 = -A \Rightarrow A = -10$

Substituting $x = 2$, we get $13 = B$

$I = \int\left(\dfrac{-10}{x - 1} + \dfrac{13}{x - 2}\right)\, dx = -10\log(x - 1) + 13\log(x - 2) + c$

The given expression is $I = m\log\left(\dfrac{x - 2}{x - 1}\right) + n\log(x - 2) + c$

Expanding the logarithmic term:

$I = m\log(x - 2) - m\log(x - 1) + n\log(x - 2) + c$

$I = (m + n)\log(x - 2) - m\log(x - 1) + c$

Comparing the coefficients with our integrated result, we get:

$m = 10$

$m + n = 13$

Therefore, the value of $m + n$ is $13$.

</details>

---

### Q5. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{x^2\, \text{d}x}{(x^2 + 2)(x^2 + 5)} =$

**Options:**

- **(A)** $-\left(\dfrac{\sqrt{2}}{3}\tan^{-1}\dfrac{x}{\sqrt{2}} + \dfrac{\sqrt{5}}{3}\tan^{-1}\dfrac{x}{\sqrt{5}}\right) + c$, where c is the constant of integration
- **(B)** $\left(\dfrac{\sqrt{2}}{3}\tan^{-1}\dfrac{x}{\sqrt{2}} + \dfrac{\sqrt{5}}{3}\tan^{-1}\dfrac{x}{\sqrt{5}}\right) + c$, where c is the constant of integration
- **(C)** $\dfrac{\sqrt{2}}{3}\tan^{-1}\left(\dfrac{x}{\sqrt{2}}\right) - \dfrac{\sqrt{5}}{3}\tan^{-1}\left(\dfrac{x}{\sqrt{5}}\right) + c$, where c is the constant of integration
- **(D)** $-\dfrac{\sqrt{2}}{3}\tan^{-1}\left(\dfrac{x}{\sqrt{2}}\right) + \dfrac{\sqrt{5}}{3}\tan^{-1}\left(\dfrac{x}{\sqrt{5}}\right) + c$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\dfrac{\sqrt{2}}{3}\tan^{-1}\left(\dfrac{x}{\sqrt{2}}\right) + \dfrac{\sqrt{5}}{3}\tan^{-1}\left(\dfrac{x}{\sqrt{5}}\right) + c$, where c is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{x^2}{(x^2 + 2)(x^2 + 5)} \, \text{d}x$

To resolve into partial fractions, substitute $x^2 = t$:

$\dfrac{t}{(t + 2)(t + 5)} = \dfrac{A}{t + 2} + \dfrac{B}{t + 5}$

$t = A(t + 5) + B(t + 2)$

Putting $t = -2$, we get $-2 = 3A \Rightarrow A = -\dfrac{2}{3}$

Putting $t = -5$, we get $-5 = -3B \Rightarrow B = \dfrac{5}{3}$

Therefore, $\dfrac{x^2}{(x^2 + 2)(x^2 + 5)} = -\dfrac{2}{3(x^2 + 2)} + \dfrac{5}{3(x^2 + 5)}$

Integrating with respect to $x$:

$I = -\dfrac{2}{3} \int \dfrac{1}{x^2 + (\sqrt{2})^2} \, \text{d}x + \dfrac{5}{3} \int \dfrac{1}{x^2 + (\sqrt{5})^2} \, \text{d}x$

$I = -\dfrac{2}{3} \left( \dfrac{1}{\sqrt{2}} \tan^{-1} \dfrac{x}{\sqrt{2}} \right) + \dfrac{5}{3} \left( \dfrac{1}{\sqrt{5}} \tan^{-1} \dfrac{x}{\sqrt{5}} \right) + c$

$I = -\dfrac{\sqrt{2}}{3} \tan^{-1} \left( \dfrac{x}{\sqrt{2}} \right) + \dfrac{\sqrt{5}}{3} \tan^{-1} \left( \dfrac{x}{\sqrt{5}} \right) + c$

Answer: $-\dfrac{\sqrt{2}}{3}\tan^{-1}\left(\dfrac{x}{\sqrt{2}}\right) + \dfrac{\sqrt{5}}{3}\tan^{-1}\left(\dfrac{x}{\sqrt{5}}\right) + c$, where c is the constant of integration

</details>

---

### Q6. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{2x}{4 - 3x - x^2} dx = \cdots$

**Options:**

- **(A)** $\dfrac{8}{5}\log|4 + x| - \dfrac{2}{5}\log|1 - x| + c$
- **(B)** $2\log|4 + x| + \dfrac{2}{5}\log|1 - x| + c$
- **(C)** $-\log|4 + x| + \dfrac{2}{5}\log|1 - x| + c$
- **(D)** $-\dfrac{8}{5}\log|4 + x| - \dfrac{2}{5}\log|1 - x| + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\dfrac{8}{5}\log|4 + x| - \dfrac{2}{5}\log|1 - x| + c$**

**Detailed Solution:**

Let $I = \int \dfrac{2x}{4 - 3x - x^2} dx$

Factorizing the denominator:

$4 - 3x - x^2 = (1 - x)(4 + x)$

Using partial fractions:

$\dfrac{2x}{(1 - x)(4 + x)} = \dfrac{A}{1 - x} + \dfrac{B}{4 + x}$

$2x = A(4 + x) + B(1 - x)$

Substituting $x = 1$, we get $2 = 5A \Rightarrow A = \dfrac{2}{5}$

Substituting $x = -4$, we get $-8 = 5B \Rightarrow B = -\dfrac{8}{5}$

Therefore,

$I = \int \left( \dfrac{2/5}{1 - x} - \dfrac{8/5}{4 + x} \right) dx$

$I = \dfrac{2}{5} \left( \dfrac{\log|1 - x|}{-1} \right) - \dfrac{8}{5} \log|4 + x| + c$

$I = -\dfrac{8}{5} \log|4 + x| - \dfrac{2}{5} \log|1 - x| + c$

Answer: $-\dfrac{8}{5}\log|4 + x| - \dfrac{2}{5}\log|1 - x| + c$

</details>

---

### Q7. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \dfrac{x + 2}{x^2 - 7x + 12} dx$ is equal to

**Options:**

- **(A)** $-5\log|x - 3| + 6\log|x - 4| + c$
- **(B)** $-5\log|x - 3| - 6\log|x - 4| + c$
- **(C)** $5\log|x - 3| - 6\log|x - 4| + c$
- **(D)** $5\log|x - 3| + 6\log|x - 4| + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-5\log|x - 3| + 6\log|x - 4| + c$**

**Detailed Solution:**

Let $I = \int \dfrac{x + 2}{x^2 - 7x + 12} dx$

Factorizing the denominator, we get $x^2 - 7x + 12 = (x - 3)(x - 4)$

Using partial fractions:

$\dfrac{x + 2}{(x - 3)(x - 4)} = \dfrac{A}{x - 3} + \dfrac{B}{x - 4}$

$x + 2 = A(x - 4) + B(x - 3)$

Substituting $x = 3$, we get $5 = -A \Rightarrow A = -5$

Substituting $x = 4$, we get $6 = B \Rightarrow B = 6$

Therefore, the integral becomes:

$I = \int \left( \dfrac{-5}{x - 3} + \dfrac{6}{x - 4} \right) dx$

$I = -5\log|x - 3| + 6\log|x - 4| + c$

Answer: $-5\log|x - 3| + 6\log|x - 4| + c$

</details>

---

### Q8. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{\mathrm{d} x}{x^4+5 x^2+4}=\mathrm{A} \tan^{-1} x+\mathrm{B} \tan ^{-1} \frac{x}{2}+\mathrm{c}$ where $c$ is a constant of integration, then

**Options:**

- **(A)** $\mathrm{A}=\frac{1}{2}, \mathrm{~B}=\frac{1}{4}$
- **(B)** $A=\frac{1}{3}, B=-\frac{1}{6}$
- **(C)** $A=\frac{1}{3}, B=\frac{1}{6}$
- **(D)** $A=\frac{1}{2}, B=-\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $A=\frac{1}{3}, B=-\frac{1}{6}$**

**Detailed Solution:**

Let $I = \int \dfrac{\mathrm{d} x}{x^4+5 x^2+4}$

Factorizing the denominator, we get $x^4+5 x^2+4 = (x^2+1)(x^2+4)$

Using partial fractions, let $x^2 = t$

$\dfrac{1}{(t+1)(t+4)} = \dfrac{1}{3} \left( \dfrac{1}{t+1} - \dfrac{1}{t+4} \right)$

Substituting back $t = x^2$, we get:

$I = \dfrac{1}{3} \int \left( \dfrac{1}{x^2+1} - \dfrac{1}{x^2+4} \right) \mathrm{d} x$

$I = \dfrac{1}{3} \int \dfrac{\mathrm{d} x}{x^2+1} - \dfrac{1}{3} \int \dfrac{\mathrm{d} x}{x^2+2^2}$

Using the standard integral formula $\int \dfrac{\mathrm{d} x}{x^2+a^2} = \dfrac{1}{a} \tan^{-1} \left( \dfrac{x}{a} \right) + c$, we get:

$I = \dfrac{1}{3} \tan^{-1} x - \dfrac{1}{3} \left( \dfrac{1}{2} \tan^{-1} \dfrac{x}{2} \right) + c$

$I = \dfrac{1}{3} \tan^{-1} x - \dfrac{1}{6} \tan^{-1} \dfrac{x}{2} + c$

Comparing this with the given expression $A \tan^{-1} x + B \tan^{-1} \dfrac{x}{2} + c$, we get:

$A = \dfrac{1}{3}$ and $B = -\dfrac{1}{6}$

Answer: $A=\frac{1}{3}, B=-\frac{1}{6}$

</details>

---

### Q9. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{\left(x^4+1\right)}{x\left(x^2+1\right)^2} \mathrm{dx}=\mathrm{A} \log |x|+\frac{\mathrm{B}}{1+x^2}+\mathrm{c}$, then $\mathrm{A}-\mathrm{B}$ is (where c is the constant of integration)

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 2
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Let $I = \int \dfrac{x^4+1}{x(x^2+1)^2} dx$

Adding and subtracting $2x^2$ in the numerator, we get:

$I = \int \dfrac{x^4+2x^2+1-2x^2}{x(x^2+1)^2} dx$

$I = \int \dfrac{(x^2+1)^2-2x^2}{x(x^2+1)^2} dx$

Separating the terms, we get:

$I = \int \left( \dfrac{1}{x} - \dfrac{2x}{(x^2+1)^2} \right) dx$

$I = \int \dfrac{1}{x} dx - \int \dfrac{2x}{(x^2+1)^2} dx$

For the second integral, substitute $x^2+1 = t \Rightarrow 2x dx = dt$:

$I = \log |x| - \int \dfrac{1}{t^2} dt$

$I = \log |x| - \left( -\dfrac{1}{t} \right) + c$

$I = \log |x| + \dfrac{1}{x^2+1} + c$

Comparing this with the given expression $A \log |x| + \dfrac{B}{1+x^2} + c$, we get:

$A = 1$ and $B = 1$

Therefore, $A - B = 1 - 1 = 0$

Answer: 0

</details>

---

### Q10. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{2 x^2+3}{\left(x^2-1\right)\left(x^2-4\right)} \mathrm{d} x=\log \left[\left(\frac{x-2}{x+2}\right)^a \cdot\left(\frac{x+1}{x-1}\right)^b\right]+c$,
(where c is the constant of integration) then the value of $a+\mathrm{b}$ is equal to

**Options:**

- **(A)** $\frac{1}{12}$
- **(B)** $\frac{21}{12}$
- **(C)** $\frac{-1}{12}$
- **(D)** $\frac{-21}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{21}{12}$**

**Detailed Solution:**

Let $x^2 = t$ to resolve the integrand into partial fractions.

$\dfrac{2t+3}{(t-1)(t-4)} = \dfrac{A}{t-1} + \dfrac{B}{t-4}$

$2t+3 = A(t-4) + B(t-1)$

Substituting $t=1$, we get $5 = -3A \Rightarrow A = -\dfrac{5}{3}$

Substituting $t=4$, we get $11 = 3B \Rightarrow B = \dfrac{11}{3}$

Now, substituting back $t = x^2$ and integrating:

$\int \dfrac{2x^2+3}{(x^2-1)(x^2-4)} dx = \int \left( \dfrac{-5/3}{x^2-1} + \dfrac{11/3}{x^2-4} \right) dx$

Using the standard formula $\int \dfrac{1}{x^2-a^2} dx = \dfrac{1}{2a} \log \left| \dfrac{x-a}{x+a} \right| + c$, we get:

$= -\dfrac{5}{3} \left( \dfrac{1}{2(1)} \log \left| \dfrac{x-1}{x+1} \right| \right) + \dfrac{11}{3} \left( \dfrac{1}{2(2)} \log \left| \dfrac{x-2}{x+2} \right| \right) + c$

$= -\dfrac{5}{6} \log \left| \dfrac{x-1}{x+1} \right| + \dfrac{11}{12} \log \left| \dfrac{x-2}{x+2} \right| + c$

Using the property $-m \log \left( \dfrac{p}{q} \right) = m \log \left( \dfrac{q}{p} \right)$:

$= \dfrac{5}{6} \log \left| \dfrac{x+1}{x-1} \right| + \dfrac{11}{12} \log \left| \dfrac{x-2}{x+2} \right| + c$

$= \log \left[ \left( \dfrac{x-2}{x+2} \right)^{11/12} \cdot \left( \dfrac{x+1}{x-1} \right)^{5/6} \right] + c$

Comparing this with the given expression $\log \left[ \left( \dfrac{x-2}{x+2} \right)^a \cdot \left( \dfrac{x+1}{x-1} \right)^b \right] + c$, we get:

$a = \dfrac{11}{12}$ and $b = \dfrac{5}{6}$

Therefore, $a+b = \dfrac{11}{12} + \dfrac{5}{6} = \dfrac{11}{12} + \dfrac{10}{12} = \dfrac{21}{12}$

Answer: $\frac{21}{12}$

</details>

---

### Q11. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{3 \sin x \cos x}{4 \sin x+7} \mathrm{~d} x=\mathrm{A} \sin x-\mathrm{B} \log (4 \sin x+7)+\mathrm{c}$ where $c$ is the constant of integration, then the value of $A+B$ is equal to

**Options:**

- **(A)** $\frac{9}{16}$
- **(B)** $\frac{-9}{16}$
- **(C)** $\frac{33}{16}$
- **(D)** $\frac{-33}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{33}{16}$**

**Detailed Solution:**

Let $I = \int \dfrac{3 \sin x \cos x}{4 \sin x+7} \mathrm{~d} x$

Substitute $\sin x = t$, then $\cos x \mathrm{~d}x = \mathrm{d}t$

$I = \int \dfrac{3t}{4t+7} \mathrm{~d}t$

$I = \dfrac{3}{4} \int \dfrac{4t+7-7}{4t+7} \mathrm{~d}t$

$I = \dfrac{3}{4} \int \left(1 - \dfrac{7}{4t+7}\right) \mathrm{d}t$

$I = \dfrac{3}{4} \left( t - \dfrac{7}{4} \log |4t+7| \right) + c$

$I = \dfrac{3}{4} t - \dfrac{21}{16} \log |4t+7| + c$

Substituting $t = \sin x$:

$I = \dfrac{3}{4} \sin x - \dfrac{21}{16} \log (4 \sin x + 7) + c$

Comparing with $A \sin x - B \log (4 \sin x + 7) + c$, we get:

$A = \dfrac{3}{4}$ and $B = \dfrac{21}{16}$

$A + B = \dfrac{3}{4} + \dfrac{21}{16} = \dfrac{12+21}{16} = \dfrac{33}{16}$

Answer: $\frac{33}{16}$

</details>

---

### Q12. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{2 x+3}{(x-1)\left(x^2+1\right)} \mathrm{d} x=\log _e\left\{(x-1)^{\frac{5}{2}}\left(x^2+1\right)^a\right\}-\frac{1}{2} \tan ^{-1} x+\mathrm{A}$ where $A$ is an arbitrary constant, then the value of $a$ is

**Options:**

- **(A)** $\frac{5}{4}$
- **(B)** $-\frac{5}{4}$
- **(C)** $-\frac{5}{3}$
- **(D)** $-\frac{5}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{5}{4}$**

**Detailed Solution:**

Let $\dfrac{2x+3}{(x-1)(x^2+1)} = \dfrac{P}{x-1} + \dfrac{Qx+R}{x^2+1}$

Multiplying by $(x-1)(x^2+1)$, we get:

$2x+3 = P(x^2+1) + (Qx+R)(x-1)$

Substituting $x=1$:

$5 = 2P \Rightarrow P = \dfrac{5}{2}$

Comparing the coefficients of $x^2$ on both sides:

$P + Q = 0 \Rightarrow Q = -\dfrac{5}{2}$

Comparing the constant terms on both sides:

$P - R = 3 \Rightarrow R = \dfrac{5}{2} - 3 = -\dfrac{1}{2}$

Now, the integral becomes:

$\int \dfrac{2x+3}{(x-1)(x^2+1)} dx = \int \left( \dfrac{5/2}{x-1} - \dfrac{\dfrac{5}{2}x + \dfrac{1}{2}}{x^2+1} \right) dx$

$= \dfrac{5}{2} \int \dfrac{1}{x-1} dx - \dfrac{5}{4} \int \dfrac{2x}{x^2+1} dx - \dfrac{1}{2} \int \dfrac{1}{x^2+1} dx$

$= \dfrac{5}{2} \log_e(x-1) - \dfrac{5}{4} \log_e(x^2+1) - \dfrac{1}{2} \tan^{-1}x + A$

Using the property $m \log n = \log n^m$ and $\log m + \log n = \log(mn)$:

$= \log_e \left\{ (x-1)^{\dfrac{5}{2}} (x^2+1)^{-\dfrac{5}{4}} \right\} - \dfrac{1}{2} \tan^{-1}x + A$

Comparing this with the given expression $\log_e\left\{ (x-1)^{\dfrac{5}{2}}(x^2+1)^a \right\} - \dfrac{1}{2} \tan^{-1}x + A$, we get:

$a = -\dfrac{5}{4}$

Answer: $-\frac{5}{4}$

</details>

---

### Q13. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{x d x}{(x-1)(x-2)}=$

**Options:**

- **(A)** $\log \left(\frac{x-1}{x-2}\right)+c$, where $c$ is the constant of integration
- **(B)** $\log \left(\frac{x-2}{(x-1)^2}\right)+c$, where $c$ is the constant of integration
- **(C)** $\log \left(\frac{x-2}{x-1}\right)+c$, where $c$ is the constant of integration
- **(D)** $\log \left(\frac{(x-2)^2}{x-1}\right)+c$, where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log \left(\frac{(x-2)^2}{x-1}\right)+c$, where $c$ is the constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{x}{(x-1)(x-2)} dx$

Using partial fractions, let $\dfrac{x}{(x-1)(x-2)} = \dfrac{A}{x-1} + \dfrac{B}{x-2}$

$x = A(x-2) + B(x-1)$

Substituting $x = 1$, we get $1 = A(-1) \Rightarrow A = -1$

Substituting $x = 2$, we get $2 = B(1) \Rightarrow B = 2$

Therefore, $\dfrac{x}{(x-1)(x-2)} = \dfrac{-1}{x-1} + \dfrac{2}{x-2}$

Integrating both sides with respect to $x$:

$I = \int \left( \dfrac{-1}{x-1} + \dfrac{2}{x-2} \right) dx$

$I = -\log(x-1) + 2\log(x-2) + c$

$I = \log(x-2)^2 - \log(x-1) + c$

$I = \log \left( \dfrac{(x-2)^2}{x-1} \right) + c$

Answer: $\log \left(\frac{(x-2)^2}{x-1}\right)+c$, where $c$ is the constant of integration

</details>

---

### Q14. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \frac{\log \left(t+\sqrt{1+\mathrm{t}^2}\right)}{\sqrt{1+\mathrm{t}^2}} \mathrm{dt}=\frac{1}{2}(\mathrm{~g}(\mathrm{t}))^2+\mathrm{c}$
where c is a constant of integration, then $g(2)$ is equal to

**Options:**

- **(A)** $2 \log (2+\sqrt{5})$
- **(B)** $\log (2+\sqrt{5})$
- **(C)** $\frac{1}{\sqrt{5}} \log (2+\sqrt{5})$
- **(D)** $\frac{1}{2} \log (2+\sqrt{5})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log (2+\sqrt{5})$**

**Detailed Solution:**

Let $I = \int \dfrac{\log \left(t+\sqrt{1+t^2}\right)}{\sqrt{1+t^2}} dt$

Substitute $u = \log \left(t+\sqrt{1+t^2}\right)$

Differentiating with respect to $t$, we get:

$du = \dfrac{1}{t+\sqrt{1+t^2}} \left(1 + \dfrac{2t}{2\sqrt{1+t^2}}\right) dt$

$du = \dfrac{1}{t+\sqrt{1+t^2}} \left(\dfrac{\sqrt{1+t^2}+t}{\sqrt{1+t^2}}\right) dt$

$du = \dfrac{1}{\sqrt{1+t^2}} dt$

The integral becomes:

$I = \int u \, du = \dfrac{1}{2} u^2 + c$

Substituting back $u = \log \left(t+\sqrt{1+t^2}\right)$:

$I = \dfrac{1}{2} \left( \log \left(t+\sqrt{1+t^2}\right) \right)^2 + c$

Comparing this with the given expression $\dfrac{1}{2}(g(t))^2+c$, we get:

$g(t) = \log \left(t+\sqrt{1+t^2}\right)$

Substituting $t = 2$:

$g(2) = \log \left(2+\sqrt{1+2^2}\right) = \log (2+\sqrt{5})$

Answer: $\log (2+\sqrt{5})$

</details>

---

### Q15. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \mathrm{e}^{x^2}. x^3 \mathrm{~d} x=\mathrm{e}^{x^2} \mathrm{f}(x)+\mathrm{c}$ and $\mathrm{f}(\mathrm{I})=0$ (where c is a constant of integration), then the value of $\mathrm{f}(x)$ is

**Options:**

- **(A)** $\frac{x-1}{2}$
- **(B)** $\frac{x^2+1}{2}$
- **(C)** $\frac{x+1}{2}$
- **(D)** $\frac{x^2-1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{x^2-1}{2}$**

**Detailed Solution:**

Let $I = \int \mathrm{e}^{x^2} x^3 \mathrm{d}x$

Substitute $x^2 = t$, which gives $2x \mathrm{d}x = \mathrm{d}t$ or $x \mathrm{d}x = \dfrac{\mathrm{d}t}{2}$.

The integral becomes:

$I = \int \mathrm{e}^t \cdot t \dfrac{\mathrm{d}t}{2} = \dfrac{1}{2} \int t \mathrm{e}^t \mathrm{d}t$

Using integration by parts:

$I = \dfrac{1}{2} \left( t \mathrm{e}^t - \int 1 \cdot \mathrm{e}^t \mathrm{d}t \right)$

$I = \dfrac{1}{2} (t \mathrm{e}^t - \mathrm{e}^t) + \mathrm{c}$

$I = \mathrm{e}^t \left( \dfrac{t - 1}{2} \right) + \mathrm{c}$

Substituting back $t = x^2$:

$I = \mathrm{e}^{x^2} \left( \dfrac{x^2 - 1}{2} \right) + \mathrm{c}$

Comparing this with the given expression $\mathrm{e}^{x^2} \mathrm{f}(x) + \mathrm{c}$, we get:

$\mathrm{f}(x) = \dfrac{x^2 - 1}{2}$

Checking the given condition $\mathrm{f}(1) = 0$:

$\mathrm{f}(1) = \dfrac{1^2 - 1}{2} = 0$, which is satisfied.

Answer: $\frac{x^2-1}{2}$

</details>

---

### Q16. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int \frac{d x}{5+4 \sin x}$ is equal to

**Options:**

- **(A)** $\frac{2}{5} \tan ^{-1}\left(\frac{5 \tan \frac{x}{2}+4}{3}\right)+\mathrm{c}$, (where c is a constant of integration) .
- **(B)** $\frac{2}{3} \tan ^{-1}\left(\frac{5 \tan \frac{x}{2}+4}{3}\right)+\mathrm{c}$, (where c is a constant of integration)
- **(C)** $\frac{2}{5} \log \left(\frac{5 \tan \frac{x}{2}+7}{5 \tan \frac{x}{2}+1}\right)+\mathrm{c}$, (where c is a constant of integration)
- **(D)** $\frac{2}{3} \log \left(\frac{5 \tan \frac{x}{2}+7}{5 \tan \frac{x}{2}+1}\right)+\mathrm{c}$, (where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{3} \tan ^{-1}\left(\frac{5 \tan \frac{x}{2}+4}{3}\right)+\mathrm{c}$, (where c is a constant of integration)**

**Detailed Solution:**

Let $I = \int \dfrac{dx}{5+4 \sin x}$

Substitute $t = \tan \dfrac{x}{2}$, which gives $\sin x = \dfrac{2t}{1+t^2}$ and $dx = \dfrac{2 dt}{1+t^2}$.

$I = \int \dfrac{\dfrac{2 dt}{1+t^2}}{5 + 4 \left( \dfrac{2t}{1+t^2} \right)}$

$I = \int \dfrac{2 dt}{5(1+t^2) + 8t}$

$I = \int \dfrac{2 dt}{5t^2 + 8t + 5}$

$I = \dfrac{2}{5} \int \dfrac{dt}{t^2 + \dfrac{8}{5}t + 1}$

$I = \dfrac{2}{5} \int \dfrac{dt}{\left( t + \dfrac{4}{5} \right)^2 + \dfrac{9}{25}}$

$I = \dfrac{2}{5} \int \dfrac{dt}{\left( t + \dfrac{4}{5} \right)^2 + \left( \dfrac{3}{5} \right)^2}$

Using the standard integral $\int \dfrac{dx}{x^2 + a^2} = \dfrac{1}{a} \tan^{-1} \left( \dfrac{x}{a} \right) + c$:

$I = \dfrac{2}{5} \times \dfrac{1}{\dfrac{3}{5}} \tan^{-1} \left( \dfrac{t + \dfrac{4}{5}}{\dfrac{3}{5}} \right) + c$

$I = \dfrac{2}{3} \tan^{-1} \left( \dfrac{5t + 4}{3} \right) + c$

Substituting back $t = \tan \dfrac{x}{2}$:

$I = \dfrac{2}{3} \tan^{-1} \left( \dfrac{5 \tan \dfrac{x}{2} + 4}{3} \right) + c$

Answer: $\frac{2}{3} \tan ^{-1}\left(\frac{5 \tan \frac{x}{2}+4}{3}\right)+\mathrm{c}$, (where c is a constant of integration)

</details>

---

### Q17. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x \mathrm{~d} x}{(x-1)^2(x+2)}=$

**Options:**

- **(A)** $\frac{2}{9} \log (x-1)+\frac{1}{3} \times \frac{1}{x-1}+\frac{2}{9} \log (x+2)+\mathrm{c}$, where c is a constant of integration
- **(B)** $\frac{2}{9} \log (x-1)-\frac{1}{3} \times \frac{1}{(x-1)}+\frac{2}{9} \log (x+2)+\mathrm{c}$, where c is a constant of integration
- **(C)** $\frac{2}{9} \log (x-1)+\frac{1}{3} \times \frac{1}{x-1}-\frac{2}{9} \log (x+2)+\mathrm{c}$, where c is a constant of integration
- **(D)** $\frac{2}{9} \log (x-1)-\frac{1}{3} \times \frac{1}{x-1}-\frac{2}{9} \log (x+2)+\mathrm{c}$, where c is a constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2}{9} \log (x-1)-\frac{1}{3} \times \frac{1}{x-1}-\frac{2}{9} \log (x+2)+\mathrm{c}$, where c is a constant of integration**

**Detailed Solution:**

Let $I = \int \dfrac{x}{(x-1)^2(x+2)} \mathrm{d} x$

Using partial fractions, let:

$\dfrac{x}{(x-1)^2(x+2)} = \dfrac{A}{x-1} + \dfrac{B}{(x-1)^2} + \dfrac{C}{x+2}$

Multiplying by $(x-1)^2(x+2)$, we get:

$x = A(x-1)(x+2) + B(x+2) + C(x-1)^2$

Substituting $x = 1$:

$1 = B(1+2) \Rightarrow 3B = 1 \Rightarrow B = \dfrac{1}{3}$

Substituting $x = -2$:

$-2 = C(-2-1)^2 \Rightarrow 9C = -2 \Rightarrow C = -\dfrac{2}{9}$

Substituting $x = 0$:

$0 = A(-1)(2) + B(2) + C(-1)^2$

$0 = -2A + 2B + C$

$2A = 2\left(\dfrac{1}{3}\right) - \dfrac{2}{9} = \dfrac{2}{3} - \dfrac{2}{9} = \dfrac{4}{9} \Rightarrow A = \dfrac{2}{9}$

Now, substitute $A$, $B$, and $C$ back into the integral:

$I = \int \left( \dfrac{2/9}{x-1} + \dfrac{1/3}{(x-1)^2} - \dfrac{2/9}{x+2} \right) \mathrm{d} x$

Integrating each term, we get:

$I = \dfrac{2}{9} \log (x-1) + \dfrac{1}{3} \left( -\dfrac{1}{x-1} \right) - \dfrac{2}{9} \log (x+2) + \mathrm{c}$

$I = \dfrac{2}{9} \log (x-1) - \dfrac{1}{3} \times \dfrac{1}{x-1} - \dfrac{2}{9} \log (x+2) + \mathrm{c}$

Answer: $\frac{2}{9} \log (x-1)-\frac{1}{3} \times \frac{1}{x-1}-\frac{2}{9} \log (x+2)+\mathrm{c}$, where c is a constant of integration

</details>

---

### Q18. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{2 x^2-1}{\left(x^2+4\right)\left(x^2-3\right)} d x=$

**Options:**

- **(A)** $\dfrac{9}{14} \tan ^{-1}\left(\dfrac{x}{2}\right)+\dfrac{5}{14 \sqrt{3}} \log \left(\dfrac{x-\sqrt{3}}{x+\sqrt{3}}\right)+\mathrm{c}$,
(where c is constant of integration)
- **(B)** $\dfrac{9}{7} \tan ^{-1}\left(\dfrac{x}{2}\right)+\dfrac{5}{7 \sqrt{3}} \log \left(\dfrac{x-\sqrt{3}}{x+\sqrt{3}}\right)+\mathrm{c}$,
(where c is constant of integration)
- **(C)** $\dfrac{9}{7} \tan ^{-1}\left(\dfrac{x}{2}\right)-\dfrac{5}{7 \sqrt{3}} \log \left(\dfrac{x-\sqrt{3}}{x+\sqrt{3}}\right)+\mathrm{c}$,
(where c is constant of integration)
- **(D)** $\dfrac{9}{14} \tan ^{-1}\left(\dfrac{x}{2}\right)+\dfrac{5}{7} \log \left(\dfrac{x-\sqrt{3}}{x+\sqrt{3}}\right)+\mathrm{c}$,
(where c is constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{9}{14} \tan ^{-1}\left(\dfrac{x}{2}\right)+\dfrac{5}{14 \sqrt{3}} \log \left(\dfrac{x-\sqrt{3}}{x+\sqrt{3}}\right)+\mathrm{c}$,
(where c is constant of integration)**

**Detailed Solution:**

Let $x^2 = t$ to resolve the integrand into partial fractions.

$\dfrac{2t - 1}{(t + 4)(t - 3)} = \dfrac{A}{t + 4} + \dfrac{B}{t - 3}$

$2t - 1 = A(t - 3) + B(t + 4)$

Substituting $t = 3$, we get $5 = 7B \Rightarrow B = \dfrac{5}{7}$.

Substituting $t = -4$, we get $-9 = -7A \Rightarrow A = \dfrac{9}{7}$.

Therefore, the integral becomes:

$\int \left( \dfrac{9/7}{x^2 + 4} + \dfrac{5/7}{x^2 - 3} \right) dx$

$= \dfrac{9}{7} \int \dfrac{1}{x^2 + 2^2} dx + \dfrac{5}{7} \int \dfrac{1}{x^2 - (\sqrt{3})^2} dx$

Using the standard formulas $\int \dfrac{1}{x^2 + a^2} dx = \dfrac{1}{a} \tan^{-1}\left(\dfrac{x}{a}\right)$ and $\int \dfrac{1}{x^2 - a^2} dx = \dfrac{1}{2a} \log \left| \dfrac{x - a}{x + a} \right|$:

$= \dfrac{9}{7} \left( \dfrac{1}{2} \tan^{-1}\left(\dfrac{x}{2}\right) \right) + \dfrac{5}{7} \left( \dfrac{1}{2\sqrt{3}} \log \left| \dfrac{x - \sqrt{3}}{x + \sqrt{3}} \right| \right) + \mathrm{c}$

$= \dfrac{9}{14} \tan^{-1}\left(\dfrac{x}{2}\right) + \dfrac{5}{14\sqrt{3}} \log \left( \dfrac{x - \sqrt{3}}{x + \sqrt{3}} \right) + \mathrm{c}$

Answer: $\dfrac{9}{14} \tan ^{-1}\left(\dfrac{x}{2}\right)+\dfrac{5}{14 \sqrt{3}} \log \left(\dfrac{x-\sqrt{3}}{x+\sqrt{3}}\right)+\mathrm{c}$,
(where c is constant of integration)

</details>

---

### Q19. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{\mathrm{d} x}{\cot ^2 x-1}=\frac{1}{\mathrm{~A}} \log |\sec 2 x+\tan 2 x|-\frac{x}{\mathrm{~B}}+\mathrm{c}$, (where $\mathrm{c}$ is constant of integration), then $\mathrm{A}+\mathrm{B}=$

**Options:**

- **(A)** $-6$
- **(B)** $6$
- **(C)** $-5$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6$**

**Detailed Solution:**

$\begin{aligned} \int \frac{\mathrm{d} x}{\cot ^2 x-1} & =\int \frac{\mathrm{d} x}{\frac{\cos ^2 x-\sin ^2 x}{\sin ^2 x}} \\ & =\int \frac{\sin ^2 x}{\cos 2 x} \mathrm{~d} x \\ & =\int \frac{\frac{1-\cos 2 x}{2}}{\cos 2 x} \mathrm{~d} x \\ & =\frac{1}{2} \int(\sec 2 x-1) \mathrm{d} x \\ & =\frac{1}{2}\left(\frac{\log |\sec 2 x+\tan 2 x|}{2}-x\right)+\mathrm{c} \\ & =\frac{1}{4} \log |\sec 2 x+\tan 2 x|-\frac{x}{2}+\mathrm{c} \\ \therefore \quad \mathrm{A}=4, \mathrm{~B} & =2 \\ \Rightarrow \mathrm{A}+\mathrm{B} & =6\end{aligned}$

</details>

---

### Q20. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{I}=\int \frac{2 x-7}{\sqrt{3 x-2}} \mathrm{~d} x$, then $\mathrm{I}$ is given by

**Options:**

- **(A)** $\frac{106}{27}(3 x-2)^{\frac{3}{2}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\frac{98}{27}(3 x-2)^{\frac{3}{2}}+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\frac{4}{27}(3 x-2)^{\frac{3}{2}}-\frac{34}{9}(3 x-2)^{\frac{1}{2}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\frac{4}{27}(3 x-2)^{\frac{3}{2}}+\frac{34}{9}(3 x-2)^{\frac{1}{2}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4}{27}(3 x-2)^{\frac{3}{2}}-\frac{34}{9}(3 x-2)^{\frac{1}{2}}+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$\begin{aligned} \mathrm{I} & =\int \frac{2 x-7}{\sqrt{3 x-2}} \mathrm{~d} x \\ & =\int \frac{\frac{2}{3}(3 x-2)-\frac{17}{3}}{\sqrt{3 x-2}} \mathrm{~d} x \\ & =\frac{2}{3} \int(3 x-2)^{\frac{1}{2}} \mathrm{~d} x-\frac{17}{3} \int(3 x-2)^{\frac{-1}{2}} \mathrm{~d} x \\ & =\frac{2}{3} \times \frac{(3 x-2)^{\frac{3}{2}}}{\frac{3}{2}} \times \frac{1}{3}-\frac{17}{3} \times \frac{(3 x-2)^{\frac{1}{2}}}{\frac{1}{2}} \times \frac{1}{3}+\mathrm{c} \\ & =\frac{4}{27}(3 x-2)^{\frac{3}{2}}-\frac{34}{9}(3 x-2)^{\frac{1}{2}}+\mathrm{c}\end{aligned}$

</details>

---

### Q21. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{1}{(x+2)(1+x)^2} \mathrm{~d} x$ has the value

**Options:**

- **(A)** $2 \log \left(\frac{x+2}{x^2+1}\right)+4 \tan ^{-1} x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\log \frac{x+2}{x^2+1}-4 \tan ^{-1} x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\log \frac{(x+2)^2}{\left(x^2+1\right)}+4 \tan ^{-1} x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\log \frac{(x+2)}{\left(x^2+1\right)^2}-4 \tan ^{-1} x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log \frac{(x+2)^2}{\left(x^2+1\right)}+4 \tan ^{-1} x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

Std.12 $\mid$ Part-2 $\mid$ Ch-3 $\mid$ Exercise-3.4
[Note: The question cannot be solved due to insufficient data.]

</details>

---

### Q22. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$$
\int \frac{x^2+1}{x\left(x^2-1\right)} \mathrm{d} x=
$$

**Options:**

- **(A)** $\log x\left(x^2-1\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\log \left(\frac{x^2-1}{x}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\log \left(x^2-1\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\log \left(\frac{x^2+1}{x}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log \left(\frac{x^2-1}{x}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{I}=\int \frac{x^2+1}{x\left(x^2-1\right)} \mathrm{d} x \\ & =\int \frac{\frac{x^2+1}{x^2-1}}{x} \mathrm{~d} x \\ & \text { Let } \mathrm{t}=\frac{x^2-1}{x} \Rightarrow \mathrm{dt}=\frac{x^2+1}{x^2} \mathrm{~d} x \\ & \therefore \quad \mathrm{I}=\int \frac{1}{\mathrm{t}} \mathrm{dt}=\log (\mathrm{t})+\mathrm{c}=\log \left(\frac{x^2-1}{x}\right)+\mathrm{c}\end{aligned}$

</details>

---

### Q23. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{1}{7-6 x-x^2} d x=$

**Options:**

- **(A)** $\frac{1}{4} \log \left(\frac{7+x}{1-x}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\frac{1}{8} \log \left(\frac{7+x}{1-x}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\frac{1}{16} \log \left(\frac{7+x}{1-x}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\frac{1}{32} \log \left(\frac{7+x}{1-x}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{8} \log \left(\frac{7+x}{1-x}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

Let
$\begin{aligned}
\mathbf{I} & =\int \frac{1}{7-6 x-x^2} \mathrm{~d} x \\
& =\int \frac{1}{7-6 x-x^2-9+9} \mathrm{~d} x \\
& =\int \frac{1}{16-\left(x^2+6 x+9\right)} \mathrm{d} x \\
& =\int \frac{1}{(4)^2-(x+3)^2} \mathrm{~d} x \\
& =\frac{1}{8} \log \left|\frac{4+x+3}{4-(x+3)}\right|+\mathrm{c} \\
& =\frac{1}{8} \log \left|\frac{7+x}{1-x}\right|+\mathrm{c}
\end{aligned}$

</details>

---

### Q24. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{3 x-2}{(x+1)(x-2)^2} d x=$
(where $C$ is a constant of integration.)

**Options:**

- **(A)** $\frac{-5}{9} \log (x+1)+\frac{5}{9} \log (x-2)-\frac{4}{3} \times \frac{1}{(x-2)}+C$
- **(B)** $\frac{1}{9} \log (x+1)+\frac{5}{9} \log (x-2)-\frac{4}{3} \times \frac{1}{(x-2)}+C$
- **(C)** $\frac{-5}{9} \log (x+1)+\frac{5}{9} \log (x-2)-\frac{4}{3} \times \frac{1}{x-2}+C$
- **(D)** $\frac{-5}{9} \log (x+1)+\frac{1}{9} \log (x-2)+\frac{1}{x-2}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-5}{9} \log (x+1)+\frac{5}{9} \log (x-2)-\frac{4}{3} \times \frac{1}{(x-2)}+C$**

**Detailed Solution:**

$\int \frac{3 x-2}{(x+1)(x-2)^2} d x=\int\left\{\frac{-5}{9(x+1)}+\frac{5}{9(x-2)}+\frac{4}{3(x-2)^2}\right\} d x$
[Using partial fraction]
$=-\frac{5}{9} \log |x+1|+\frac{5}{9} \log |x-2|-\frac{4}{3(x-2)}+C$

</details>

---

### Q25. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$$
\int \frac{2 x^2-1}{x^4-x^2-20} d x=
$$

**Options:**

- **(A)** $\frac{1}{\sqrt{5}} \log \left|\frac{\mathrm{x}+\sqrt{5}}{\mathrm{x}-\sqrt{5}}\right|+\tan ^{-1}\left(\frac{\mathrm{x}}{2}\right)+\mathrm{c}$
- **(B)** $\frac{1}{2 \sqrt{5}} \log \left|\frac{\mathrm{x}+\sqrt{5}}{\mathrm{x}-\sqrt{5}}\right|+\tan ^{-1}\left(\frac{\mathrm{x}}{2}\right)+\mathrm{c}$
- **(C)** $\frac{1}{2 \sqrt{5}} \log \left|\frac{\mathrm{x}-\sqrt{5}}{\mathrm{x}+\sqrt{5}}\right|+\frac{1}{2} \tan ^{-1}\left(\frac{\mathrm{x}}{2}\right)+\mathrm{c}$
- **(D)** $\frac{1}{2} \log \left|\frac{\mathrm{x}-\sqrt{5}}{\mathrm{x}+\sqrt{5}}\right|+\frac{1}{2} \tan ^{-1}\left(\frac{\mathrm{x}}{2}\right)+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2 \sqrt{5}} \log \left|\frac{\mathrm{x}-\sqrt{5}}{\mathrm{x}+\sqrt{5}}\right|+\frac{1}{2} \tan ^{-1}\left(\frac{\mathrm{x}}{2}\right)+\mathrm{c}$**

**Detailed Solution:**

Let $I=\int \frac{2 x^2-1}{x^4-x^2-20} d x$
If $x^2=t$, then $\frac{2 x^2-1}{x^4-x^2-20}=\frac{2 t-1}{t^2-t-20}$
Let $\frac{2 t-1}{(t-5)(t+4)}=\frac{A}{(t-5)}+\frac{B}{(t+4)}$
$$
\begin{aligned}
& \therefore 2 \mathrm{t}-1=(\mathrm{t}+4) \mathrm{a}+(\mathrm{t}-5) \mathrm{B} \\
& \therefore 2=\mathrm{A}+\mathrm{B} \text { and }-1=4 \mathrm{~A}-5 \mathrm{~B}
\end{aligned}
$$
Solving, we get $\mathrm{B}=1, \mathrm{~A}=1$
$$
\therefore I=\int\left[\frac{1}{x^2-5}+\frac{1}{x^2+4}\right] d x=\frac{1}{2 \sqrt{5}} \log \left|\frac{x-\sqrt{5}}{x+\sqrt{5}}\right|+\frac{1}{2} \tan ^{-1}\left(\frac{x}{2}\right)+c
$$

</details>

---

### Q26. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \sec ^4 x \cdot \tan ^4 x d x=\frac{\tan ^m x}{m}+\frac{\tan ^n x}{n}+c$ (where $c$ is constant of integration), then $\mathrm{m}+\mathrm{n}=$

**Options:**

- **(A)** 8
- **(B)** 12
- **(C)** 10
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 12**

**Detailed Solution:**

Let $I=\int \sec ^4 \tan ^4 x d x$
Put $\tan \mathrm{x}=\mathrm{t} \Rightarrow \sec ^2 \mathrm{x} d \mathrm{x}=\mathrm{dt}$
$$
\begin{aligned}
& \therefore \mathrm{I}=\int \sec ^2 \mathrm{x}\left(\sec ^2 \mathrm{x}\right)\left(\tan ^4 \mathrm{x}\right) \mathrm{dx} \\
& =\int\left(1+\mathrm{t}^2\right)(\mathrm{t})^4 \mathrm{dt}=\int\left(\mathrm{t}^4+\mathrm{t}^6\right) \mathrm{dt}=\frac{\mathrm{t}^5}{5}+\frac{\mathrm{t}^7}{7}+\mathrm{c}=\frac{\tan ^5 \mathrm{x}}{5}+\frac{\tan ^7 \mathrm{x}}{7}+\mathrm{c}
\end{aligned}
$$

</details>

---

### Q27. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{2 x^{2}+3}{\left(x^{2}-1\right)\left(x^{2}+4\right)} d x=a \log \left|\frac{x-1}{x+1}\right|+b \tan ^{-1}\left(\frac{x}{2}\right)+C$, then

**Options:**

- **(A)** $\mathrm{a}=\frac{1}{2}, \quad \mathrm{~b}=\frac{1}{2}$
- **(B)** $\mathrm{a}=-1, \mathrm{~b}=1$
- **(C)** $\mathrm{a}=\frac{1}{2}, \quad \mathrm{~b}=\frac{-1}{2}$
- **(D)** $\mathrm{a}=1, \quad \mathrm{~b}=-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{a}=\frac{1}{2}, \quad \mathrm{~b}=\frac{1}{2}$**

**Detailed Solution:**

$$
\text { Let } \begin{aligned}
I &=\int \frac{2 x^{2}+3}{\left(x^{2}-1\right)\left(x^{2}+4\right)} d x=\int\left[\frac{1}{x^{2}-1}+\frac{1}{x^{2}+4}\right] d x \\
I &=\frac{1}{2(1)} \log \left|\frac{x-1}{x+1}\right|+\frac{1}{2} \tan ^{-1} \frac{x}{2}+C
\end{aligned}
$$
Comparing with given data, we get $a=\frac{1}{2}, b=\frac{1}{2}$

</details>

---

### Q28. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{x+1}{x^{2}+5 x+6} d x=$

**Options:**

- **(A)** $-\log |x+2|-2 \log |x+3|+C$
- **(B)** $-\log |x+2|+2 \log |x+3|+C$
- **(C)** $2 \log |x+2|-2 \log |x+3|+C$
- **(D)** $\log |x+2|+2 \log |x+3|+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\log |x+2|+2 \log |x+3|+C$**

**Detailed Solution:**

$I=\int \frac{x+1}{x^{2}+5 x+6} d x$
Let $\quad \frac{x+1}{(x+3)(x+2)}=\int\left[\frac{x+1}{(x+3)(x+2)}\right] d x$
$\therefore x+1=A(x+2)+B(x+3)$
When $x=-2$, we get $B=-1$
When $x=-3$, we get $A=2$
$\therefore I=\int\left[\frac{2}{x+3}-\frac{B}{x+2}\right] d x$
$\therefore 2 \log |(x+3)|-\log |x+2|+c$

</details>

---

### Q29. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x^{2}+1}{(x-3)(x-2)} d x=P x+Q \log |x-3|+R \log |x-2|+c$, where $c$ is constant of
integration, then the values of $\mathrm{P}, \mathrm{Q}, \mathrm{R}$ are, respectively

**Options:**

- **(A)** $0,10,5$
- **(B)** $0,10,-5$
- **(C)** $1,10,5$
- **(D)** $1,10,-5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1,10,-5$**

**Detailed Solution:**

(C)
$I=\int \frac{x^{2}+1}{(x-3)(x-2)} d x$
$=\int \frac{\left(x^{2}-5 x+6\right)+(5 x-5)}{(x-3)(x-2)} d x$
$\quad=\int \frac{x^{2}-5 x+6}{x^{2}-5 x+6} d x+5 \int \frac{x-1}{(x-3)(x-2)} d x$
Let $\frac{(x-1)}{(x-3)(x-2)}=\frac{A}{(x-3)}+\frac{B}{(x-2)}$
$\therefore(x-1)=A(x-2)+B(x-3)$
$\therefore A+B=1$ and $2 A+3 B=1 \Rightarrow A=2, B=-1$
$\therefore I=\int d x+5 \int\left[\frac{2}{(x-3)}-\frac{1}{(x-2)}\right] d x$
Thus $P=1, Q=10, R=-5$

</details>

---

### Q30. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x^{2}}{(x+1)(x+2)^{2}} d x=$

**Options:**

- **(A)** $\log |x+1|+\frac{4}{x+2}+c$
- **(B)** $\log |x+1|-\frac{4}{x+2}+\frac{3}{(x+2)^{2}}+c$
- **(C)** $\log |x+1|+\frac{1}{x+2}+c$
- **(D)** $\log |x+1|-\frac{4}{x+2}-\frac{3}{(x+2)^{2}}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log |x+1|+\frac{4}{x+2}+c$**

**Detailed Solution:**

$$
I=\int \frac{x^{2}}{(x+1)(x+2)^{2}} d x
$$
$$
\begin{array}{l}
\text { Let } \frac{\mathrm{x}^{2}}{(\mathrm{x}+1)(\mathrm{x}+2)^{2}}=\frac{\mathrm{A}}{\mathrm{x}+1}+\frac{\mathrm{B}}{\mathrm{x}+2}+\frac{\mathrm{C}}{(\mathrm{x}+2)^{2}} \\
\therefore \mathrm{x}^{2}=\mathrm{A}(\mathrm{x}+2)^{2}+\mathrm{B}(\mathrm{x}+1)(\mathrm{x}+2)+\mathrm{C}(\mathrm{x}+1) \\
\text { When } \mathrm{x}=-2 \text {, we get } 4=-\mathrm{C} \Rightarrow \mathrm{C}=-4 \\
\text { When } \mathrm{x}=-1 \text {, we get } 1=\mathrm{A} \Rightarrow \mathrm{A}=1
\end{array}
$$
When $x=0, A=1, C=-4$, we get $0=4+2 B-4 \Rightarrow B=0$
$$
\begin{aligned}
\therefore I &=\int\left[\frac{1}{x+1}-\frac{4}{(x+2)^{2}}\right] d x \\
&=\int \frac{d x}{x+1}-4 \int(x+2)^{-2} d x \\
&=\log |x+1|-4 \frac{(x+2)^{-1}}{(-1)}+c \\
&=\log |x+1|+\frac{4}{x+2}+c
\end{aligned}
$$

</details>

---

### Q31. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{2}^{3} \frac{d x}{x^{2}+x}=$

**Options:**

- **(A)** $\log \left(\frac{3}{4}\right)$
- **(B)** $\log \left(\frac{3}{2}\right)$
- **(C)** $\log \left(\frac{9}{8}\right)$
- **(D)** $\log \left(\frac{8}{9}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log \left(\frac{9}{8}\right)$**

**Detailed Solution:**

$\begin{aligned} \mathrm{I} &=\int_{2}^{3} \frac{\mathrm{dx}}{\mathrm{x}^{2}+\mathrm{x}}=\int_{2}^{3} \frac{\mathrm{dx}}{\mathrm{x}(\mathrm{x}+1)} \\ \therefore \mathrm{I} &=\int_{2}^{3}\left[\frac{1}{\mathrm{x}}-\frac{1}{\mathrm{x}+1}\right] \mathrm{dx} \\ &=[\log \mathrm{x}-\log (\mathrm{x}+1)]_{2}^{3}=\left[\log \left(\frac{\mathrm{x}}{\mathrm{x}+1}\right)\right]_{2}^{3} \\ &=\log \left(\frac{3}{4}\right)-\log \left(\frac{2}{3}\right)=\log \left(\frac{3}{4} \times \frac{3}{2}\right)=\log \left(\frac{9}{8}\right) \end{aligned}$

</details>

---

### Q32. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{\infty} \frac{d x}{\left(x^{2}+4\right)\left(x^{2}+9\right)}=$

**Options:**

- **(A)** $\frac{\pi}{120}$
- **(B)** $\frac{\pi}{60}$
- **(C)** $\frac{\pi}{80}$
- **(D)** $\frac{-\pi}{60}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{60}$**

**Detailed Solution:**

Let $x^{2}=t$
$\begin{aligned}
\therefore & \frac{1}{\left(x^{2}+4\right)\left(x^{2}+9\right)}=\frac{1}{(t+4)(t+9)} \text { and let } \frac{1}{(t+4)(t+9)}=\frac{1}{5}\left[\frac{1}{t+4}-\frac{1}{t+9}\right] \\
\therefore I &=\frac{1}{5} \int_{0}^{\infty}\left[\frac{1}{x^{2}+4}-\frac{1}{x^{2}+9}\right] \mathrm{dx} \\
&=\frac{1}{5}\left\{\left[\frac{1}{2} \tan ^{-1}\left(\frac{x}{2}\right)\right]_{0}^{\infty}-\left[\frac{1}{3} \tan ^{-1}\left(\frac{x}{3}\right)\right]_{0}^{\infty}\right\} \\
&=\frac{1}{5}\left\{\frac{1}{2} \times \frac{\pi}{2}-\frac{1}{3} \times \frac{\pi}{2}\right\}=\frac{\pi}{10}\left\{\frac{1}{2}-\frac{1}{3}\right\}=\frac{\pi}{60}
\end{aligned}$

</details>

---

### Q33. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{0}^{\infty} \frac{x}{(1+x)\left(x^{2}+1\right)} d x$ is

**Options:**

- **(A)** $2 \pi$
- **(B)** $\frac{\pi}{4}$
- **(C)** $\frac{\pi}{16}$
- **(D)** $\frac{\pi}{32}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{4}$**

**Detailed Solution:**

Let $I=\int_{0}^{\infty} \frac{x d x}{(1+x)\left(x^{2}+1\right)}$
By partial fraction, $\frac{x}{(1+x)\left(x^{2}+1\right)}=\frac{A}{(1+x)}+\frac{B x+C}{\left(x^{2}+1\right)}$
$\Rightarrow x=A\left(x^{2}+1\right)+(1+x)(B x+C)$
$\Rightarrow x=A\left(x^{2}+1\right)+\left(B x+B x^{2}+C+C x\right)$
$\Rightarrow x=(A+B) x^{2}+(B+C) x+(A+C)$
On comparing both sides, we get $A+B=0, \quad B+C=1, \quad A+C=0 \quad \ldots(\mathrm{i})$
On adding all these equations, we get $\begin{aligned} A+B+C &=\frac{1}{2}...(ii) \\ \therefore \quad A=\frac{1}{2}-1 &=-\frac{1}{2}, \quad C=\frac{1}{2} \\ \text { and } \quad B=\frac{1}{2} \\ \therefore \quad I=\int_{0}^{\infty}\left\{\frac{-1}{2(1+x)}+\frac{1}{2} \frac{(x+1)}{\left(x^{2}+1\right)}\right\} d x \\=-\frac{1}{2} \int_{0}^{\infty} \frac{d x}{1+x}+\frac{1}{2} \int_{0}^{\infty} \frac{x}{x^{2}+1} d x \\+\frac{1}{2} \int_{0}^{\infty} \frac{d x}{1+x^{2}} \end{aligned}$
$=-\frac{1}{2}[\log (1+x)]_{0}^{\infty}+\frac{1}{4}\left[\log \left(x^{2}+1\right)\right]_{0}^{\infty}$
$+\frac{1}{2} \times \frac{\pi}{2}$
$=-\frac{1}{2} \lim _{x \rightarrow \infty} \log (1+x)+\frac{1}{4}$
$\lim _{x \rightarrow \infty} \log \left(1+x^{2}\right)+\frac{\pi}{4}$
$=\lim _{x \rightarrow \infty} \log \left[\frac{\left(1+x^{2}\right)^{1 / 4}}{(1+x)^{1 / 2}}\right]+\frac{\pi}{4}$
$=\lim _{x \rightarrow \infty} \log \left[\frac{\sqrt{x}\left(\frac{1}{x^{2}}+1\right)^{1 / 4}}{\sqrt{x}\left(\frac{1}{x}+1\right)^{1 / 2}}\right]+\frac{\pi}{4}$
$=\log \frac{(0+1)^{1 / 4}}{(0+1)^{1 / 2}}+\frac{\pi}{4}$
$=\log (1)+\frac{\pi}{4}=0+\frac{\pi}{4}=\frac{\pi}{4}$

</details>

---

