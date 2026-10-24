# MHT CET Mathematics - Differential Equations

## Topic 2: Formation of Differential Equation

**Total Questions:** 67

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The differential equation which represents the family of curves $(a + bx)e^{y/x} = x$, (where $a$ and $b$ are arbitrary constants); is

**Options:**

- **(A)** $x\dfrac{d^2y}{dx^2} = x\dfrac{dy}{dx} - y$
- **(B)** $x^3\dfrac{d^2y}{dx^2} = \left(x\dfrac{dy}{dx} - y\right)^2$
- **(C)** $x^2\dfrac{d^2y}{dx^2} = x\dfrac{dy}{dx} - y$
- **(D)** $x^3\dfrac{d^2y}{dx^2} = \left(x\dfrac{dy}{dx} - y\right)^3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^3\dfrac{d^2y}{dx^2} = \left(x\dfrac{dy}{dx} - y\right)^2$**

**Detailed Solution:**

Given the family of curves:
$(a + bx)e^{y/x} = x$

Taking the natural logarithm on both sides:
$\ln(a + bx) + \dfrac{y}{x} = \ln x$

$\Rightarrow \dfrac{y}{x} = \ln x - \ln(a + bx)$

Differentiating with respect to $x$:
$\dfrac{x\dfrac{dy}{dx} - y}{x^2} = \dfrac{1}{x} - \dfrac{b}{a + bx}$

$\Rightarrow \dfrac{x\dfrac{dy}{dx} - y}{x} = 1 - \dfrac{bx}{a + bx} = \dfrac{a}{a + bx}$

Taking the reciprocal and multiplying by $x$:
$\dfrac{x}{x\dfrac{dy}{dx} - y} = \dfrac{a + bx}{a} = 1 + \dfrac{b}{a}x$

Differentiating again with respect to $x$:
$\dfrac{1 \cdot \left(x\dfrac{dy}{dx} - y\right) - x \cdot \left(\dfrac{dy}{dx} + x\dfrac{d^2y}{dx^2} - \dfrac{dy}{dx}\right)}{\left(x\dfrac{dy}{dx} - y\right)^2} = \dfrac{b}{a}$

$\Rightarrow \dfrac{x\dfrac{dy}{dx} - y - x^2\dfrac{d^2y}{dx^2}}{\left(x\dfrac{dy}{dx} - y\right)^2} = \dfrac{b}{a}$

From the first derivative equation, we can also express $\dfrac{b}{a}$ as:
$\dfrac{b}{a} = \dfrac{1}{x} \left( \dfrac{x}{x\dfrac{dy}{dx} - y} - 1 \right) = \dfrac{x - \left(x\dfrac{dy}{dx} - y\right)}{x\left(x\dfrac{dy}{dx} - y\right)}$

Equating the two expressions for $\dfrac{b}{a}$:
$\dfrac{x\dfrac{dy}{dx} - y - x^2\dfrac{d^2y}{dx^2}}{\left(x\dfrac{dy}{dx} - y\right)^2} = \dfrac{x - \left(x\dfrac{dy}{dx} - y\right)}{x\left(x\dfrac{dy}{dx} - y\right)}$

Cross-multiplying by $x\left(x\dfrac{dy}{dx} - y\right)^2$:
$x\left(x\dfrac{dy}{dx} - y - x^2\dfrac{d^2y}{dx^2}\right) = \left(x - \left(x\dfrac{dy}{dx} - y\right)\right)\left(x\dfrac{dy}{dx} - y\right)$

$x^2\dfrac{dy}{dx} - xy - x^3\dfrac{d^2y}{dx^2} = x\left(x\dfrac{dy}{dx} - y\right) - \left(x\dfrac{dy}{dx} - y\right)^2$

$x^2\dfrac{dy}{dx} - xy - x^3\dfrac{d^2y}{dx^2} = x^2\dfrac{dy}{dx} - xy - \left(x\dfrac{dy}{dx} - y\right)^2$

Canceling $x^2\dfrac{dy}{dx} - xy$ from both sides:
$-x^3\dfrac{d^2y}{dx^2} = -\left(x\dfrac{dy}{dx} - y\right)^2$

$\Rightarrow x^3\dfrac{d^2y}{dx^2} = \left(x\dfrac{dy}{dx} - y\right)^2$

Answer: $x^3\dfrac{d^2y}{dx^2} = \left(x\dfrac{dy}{dx} - y\right)^2$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y = c_1 \sin^2 x + c_2$, then its differential equation is:

**Options:**

- **(A)** $\dfrac{d^2 y}{dx^2} + 2\cot 2x \dfrac{dy}{dx} = 0$
- **(B)** $\dfrac{d^2 y}{dx^2} - \cot 2x \dfrac{dy}{dx} = 0$
- **(C)** $\dfrac{d^2 y}{dx^2} - 2\cot x \dfrac{dy}{dx} = 0$
- **(D)** $\dfrac{d^2 y}{dx^2} - 2\cot 2x \dfrac{dy}{dx} = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{d^2 y}{dx^2} - 2\cot 2x \dfrac{dy}{dx} = 0$**

**Detailed Solution:**

Given equation is $y = c_1 \sin^2 x + c_2$

Differentiating with respect to $x$, we get:

$\dfrac{dy}{dx} = c_1 (2 \sin x \cos x) = c_1 \sin 2x$

Differentiating again with respect to $x$, we get:

$\dfrac{d^2 y}{dx^2} = 2 c_1 \cos 2x$

From the first derivative, we have $c_1 = \dfrac{1}{\sin 2x} \dfrac{dy}{dx}$

Substituting this value of $c_1$ in the second derivative:

$\dfrac{d^2 y}{dx^2} = 2 \left( \dfrac{1}{\sin 2x} \dfrac{dy}{dx} \right) \cos 2x$

$\dfrac{d^2 y}{dx^2} = 2 \cot 2x \dfrac{dy}{dx}$

$\dfrac{d^2 y}{dx^2} - 2 \cot 2x \dfrac{dy}{dx} = 0$

Answer: $\dfrac{d^2 y}{dx^2} - 2\cot 2x \dfrac{dy}{dx} = 0$

</details>

---

### Q3. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For a certain substance, the rate of change of vapor pressure $P$ with respect to temperature $T$ is directly proportional to the vapor pressure $P$, and inversely proportional to the square of the temperature $T$. The representation of this statement in the form of a differential equation is:
(where $k$ is a constant of proportionality)

**Options:**

- **(A)** $\dfrac{dP}{dT} = \dfrac{kP}{T^2}$
- **(B)** $\dfrac{dP}{dT} = \dfrac{P}{T^2}$
- **(C)** $\dfrac{dP}{dT} = \dfrac{kT}{P^2}$
- **(D)** $\dfrac{dP}{dT} = \dfrac{T^2}{P}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{dP}{dT} = \dfrac{kP}{T^2}$**

**Detailed Solution:**

The rate of change of vapor pressure $P$ with respect to temperature $T$ is given by $\dfrac{dP}{dT}$.

According to the given statement, this rate is directly proportional to $P$ and inversely proportional to $T^2$.

$\dfrac{dP}{dT} \propto \dfrac{P}{T^2}$

Introducing the constant of proportionality $k$, we get:

$\dfrac{dP}{dT} = \dfrac{kP}{T^2}$

Answer: $\dfrac{dP}{dT} = \dfrac{kP}{T^2}$

</details>

---

### Q4. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of the equation $x^2 + (y - b)^2 = 1$ is

**Options:**

- **(A)** $x^2\left[\left(\dfrac{dy}{dx}\right)^2 + 1\right] = \left(\dfrac{dy}{dx}\right)^2$
- **(B)** $x^2\left[\left(\dfrac{dy}{dx}\right)^2 + 1\right] = -\left(\dfrac{dy}{dx}\right)^2$
- **(C)** $x^2\left[\left(\dfrac{dy}{dx}\right)^2 - 1\right] = -\left(\dfrac{dy}{dx}\right)^2$
- **(D)** $x^2\left[\left(\dfrac{dy}{dx}\right)^2 - 1\right] = \left(\dfrac{dy}{dx}\right)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x^2\left[\left(\dfrac{dy}{dx}\right)^2 + 1\right] = \left(\dfrac{dy}{dx}\right)^2$**

**Detailed Solution:**

Given equation is $x^2 + (y - b)^2 = 1$.

Differentiating with respect to $x$:

$2x + 2(y - b)\dfrac{dy}{dx} = 0$

$y - b = -\dfrac{x}{\dfrac{dy}{dx}}$

Substituting the value of $(y - b)$ in the given equation:

$x^2 + \left(-\dfrac{x}{\dfrac{dy}{dx}}\right)^2 = 1$

$x^2 + \dfrac{x^2}{\left(\dfrac{dy}{dx}\right)^2} = 1$

$x^2\left[\left(\dfrac{dy}{dx}\right)^2 + 1\right] = \left(\dfrac{dy}{dx}\right)^2$

Answer: $x^2\left[\left(\dfrac{dy}{dx}\right)^2 + 1\right] = \left(\dfrac{dy}{dx}\right)^2$

</details>

---

### Q5. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of system of concentric circles with center $(1, 2)$ is ____

**Options:**

- **(A)** $\dfrac{dy}{dx} = \dfrac{x - 1}{x - 2}$
- **(B)** $\dfrac{dy}{dx} = \dfrac{x - 1}{2 - x}$
- **(C)** $\dfrac{dy}{dx} = \dfrac{1 - x}{2 - y}$
- **(D)** $\dfrac{dy}{dx} = \dfrac{1 - x}{y - 2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{dy}{dx} = \dfrac{1 - x}{y - 2}$**

**Detailed Solution:**

The equation of the family of concentric circles with center $(1, 2)$ is

$(x - 1)^2 + (y - 2)^2 = r^2$

where $r$ is an arbitrary constant.

Differentiating both sides with respect to $x$, we get

$2(x - 1) + 2(y - 2) \dfrac{dy}{dx} = 0$

$(y - 2) \dfrac{dy}{dx} = -(x - 1)$

$(y - 2) \dfrac{dy}{dx} = 1 - x$

$\dfrac{dy}{dx} = \dfrac{1 - x}{y - 2}$

Answer: $\dfrac{dy}{dx} = \dfrac{1 - x}{y - 2}$

</details>

---

### Q6. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of all parabolas which have $4a$ as latus rectum and whose axis is parallel to the X-axis is $2a \dfrac{d^2 y}{dx^2} + \left(\dfrac{dy}{dx}\right)^k = 0$, then the value of $k$ is...

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$**

**Detailed Solution:**

The equation of a family of parabolas with latus rectum $4a$ and axis parallel to the X-axis is given by:

$(y - \beta)^2 = 4a(x - \alpha)$

Differentiating with respect to $x$, we get:

$2(y - \beta) \dfrac{dy}{dx} = 4a$

$(y - \beta) \dfrac{dy}{dx} = 2a$

Differentiating again with respect to $x$, we get:

$\left(\dfrac{dy}{dx}\right)^2 + (y - \beta) \dfrac{d^2y}{dx^2} = 0$

From the first derivative, substitute $y - \beta = \dfrac{2a}{\dfrac{dy}{dx}}$ into the above equation:

$\left(\dfrac{dy}{dx}\right)^2 + \left(\dfrac{2a}{\dfrac{dy}{dx}}\right) \dfrac{d^2y}{dx^2} = 0$

Multiplying the entire equation by $\dfrac{dy}{dx}$, we obtain:

$\left(\dfrac{dy}{dx}\right)^3 + 2a \dfrac{d^2y}{dx^2} = 0$

Rearranging the terms:

$2a \dfrac{d^2y}{dx^2} + \left(\dfrac{dy}{dx}\right)^3 = 0$

Comparing this with the given differential equation $2a \dfrac{d^2y}{dx^2} + \left(\dfrac{dy}{dx}\right)^k = 0$, we get $k = 3$.

Answer: $3$

</details>

---

### Q7. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of the equation $y = a\cos(x + b)$ is

**Options:**

- **(A)** $\dfrac{d^2 y}{dx^2} + y = 0$
- **(B)** $\dfrac{d^2 y}{dx^2} - y = 0$
- **(C)** $\dfrac{dy}{dx} + y = 0$
- **(D)** $\dfrac{dy}{dx} - y = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{d^2 y}{dx^2} + y = 0$**

**Detailed Solution:**

Given equation is $y = a\cos(x + b)$

Differentiating with respect to $x$, we get

$\dfrac{dy}{dx} = -a\sin(x + b)$

Differentiating again with respect to $x$, we get

$\dfrac{d^2 y}{dx^2} = -a\cos(x + b)$

Substituting $y = a\cos(x + b)$, we get

$\dfrac{d^2 y}{dx^2} = -y$

$\dfrac{d^2 y}{dx^2} + y = 0$

Answer: $\dfrac{d^2 y}{dx^2} + y = 0$

</details>

---

### Q8. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The order of the differential equation representing the family of all parabolas having a fixed latus rectum of length $4a$ and an axis parallel to the x-axis is...

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

The equation of the family of parabolas with a fixed latus rectum of length $4a$ and an axis parallel to the x-axis is given by:

$(y - k)^2 = 4a(x - h)$

where $(h, k)$ are the coordinates of the vertex.

Since $4a$ is a fixed constant, there are exactly two independent arbitrary constants, $h$ and $k$, in the equation of this family of curves.

The order of the differential equation representing a family of curves is equal to the number of independent arbitrary constants present in its general equation.

Therefore, the order of the differential equation is $2$.

Answer: $2$

</details>

---

### Q9. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of the family of lines perpendicular to the line passing through the point $(3, -5)$ with inclination $\dfrac{\pi}{3}$ is...

**Options:**

- **(A)** $\dfrac{dy}{dx} + \sqrt{3} = 0$
- **(B)** $\dfrac{dy}{dx} + 1 = 0$
- **(C)** $dx + \sqrt{3}\,dy = 0$
- **(D)** $\dfrac{dy}{dx} = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $dx + \sqrt{3}\,dy = 0$**

**Detailed Solution:**

The inclination of the given line is $\theta = \dfrac{\pi}{3}$.

Slope of the given line is $m = \tan\left(\dfrac{\pi}{3}\right) = \sqrt{3}$.

The slope of any line perpendicular to this line is $m' = -\dfrac{1}{m} = -\dfrac{1}{\sqrt{3}}$.

The equation of the family of lines perpendicular to the given line is $y = -\dfrac{1}{\sqrt{3}}x + c$, where $c$ is an arbitrary constant.

Differentiating both sides with respect to $x$, we get:

$\dfrac{dy}{dx} = -\dfrac{1}{\sqrt{3}}$

$\sqrt{3}\,dy = -dx$

$dx + \sqrt{3}\,dy = 0$

Answer: $dx + \sqrt{3}\,dy = 0$

</details>

---

### Q10. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of the family of all straight lines touching the circle $x^2+y^2=1$ is ...

**Options:**

- **(A)** $\left(x-y\dfrac{dy}{dx}\right)^2=1+\left(\dfrac{dy}{dx}\right)^2$
- **(B)** $\left(y-x\dfrac{dy}{dx}\right)^2=1+\left(\dfrac{dy}{dx}\right)^2$
- **(C)** $\left(x+y\dfrac{dy}{dx}\right)^2=1+\left(\dfrac{dy}{dx}\right)^2$
- **(D)** $\left(y+x\dfrac{dy}{dx}\right)^2=1+\left(\dfrac{dy}{dx}\right)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(y-x\dfrac{dy}{dx}\right)^2=1+\left(\dfrac{dy}{dx}\right)^2$**

**Detailed Solution:**

The equation of any tangent to the circle $x^2+y^2=1$ is given by $y = mx \pm \sqrt{1+m^2}$, where $m$ is the slope of the tangent.

Differentiating both sides with respect to $x$, we get:

$\dfrac{dy}{dx} = m$

Substituting $m = \dfrac{dy}{dx}$ back into the equation of the tangent, we obtain:

$y = x\dfrac{dy}{dx} \pm \sqrt{1+\left(\dfrac{dy}{dx}\right)^2}$

Rearranging the terms gives:

$y - x\dfrac{dy}{dx} = \pm \sqrt{1+\left(\dfrac{dy}{dx}\right)^2}$

Squaring both sides, we get the required differential equation:

$\left(y - x\dfrac{dy}{dx}\right)^2 = 1+\left(\dfrac{dy}{dx}\right)^2$

Answer: $\left(y-x\dfrac{dy}{dx}\right)^2=1+\left(\dfrac{dy}{dx}\right)^2$

</details>

---

### Q11. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of all lines where the length of the normal from the origin is p and the inclination of the normal is $\alpha$ is... (where p and $\alpha$ are arbitrary constants)

**Options:**

- **(A)** $\dfrac{d^2y}{dx^2} = 0$
- **(B)** $\dfrac{dy}{dx} = 0$
- **(C)** $\dfrac{dy}{dx} = -\cot\alpha$
- **(D)** $\dfrac{d^2y}{dx^2} = \csc^2\alpha$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{d^2y}{dx^2} = 0$**

**Detailed Solution:**

The equation of a straight line in normal form is given by:

$x \cos \alpha + y \sin \alpha = p$

Since $p$ and $\alpha$ are arbitrary constants, we need to eliminate them by differentiating the equation.

Differentiating once with respect to $x$, we get:

$\cos \alpha + \dfrac{dy}{dx} \sin \alpha = 0$

Differentiating again with respect to $x$, we get:

$\dfrac{d^2y}{dx^2} \sin \alpha = 0$

Since $\alpha$ is an arbitrary constant, $\sin \alpha$ is not identically zero. Therefore, we must have:

$\dfrac{d^2y}{dx^2} = 0$

Answer: $\dfrac{d^2y}{dx^2} = 0$

</details>

---

### Q12. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of the family of all parabolas whose axis is the $y$-axis is $\ldots$

**Options:**

- **(A)** $\dfrac{d^2y}{dx^2} + x\dfrac{dy}{dx} = 0$
- **(B)** $x\dfrac{d^2y}{dx^2} - \dfrac{dy}{dx} = 0$
- **(C)** $\dfrac{d^2y}{dx^2} - x\dfrac{dy}{dx} = 0$
- **(D)** $x\dfrac{d^2y}{dx^2} + \dfrac{dy}{dx} = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x\dfrac{d^2y}{dx^2} - \dfrac{dy}{dx} = 0$**

**Detailed Solution:**

The equation of the family of all parabolas whose axis is the $y$-axis is given by:

$y = ax^2 + c$

where $a$ and $c$ are arbitrary constants.

Differentiating both sides with respect to $x$, we get:

$\dfrac{dy}{dx} = 2ax$

$\Rightarrow 2a = \dfrac{1}{x} \dfrac{dy}{dx}$

Differentiating again with respect to $x$, we get:

$\dfrac{d^2y}{dx^2} = 2a$

Substituting the value of $2a$ from the first derivative into the second derivative, we get:

$\dfrac{d^2y}{dx^2} = \dfrac{1}{x} \dfrac{dy}{dx}$

$\Rightarrow x\dfrac{d^2y}{dx^2} - \dfrac{dy}{dx} = 0$

Answer: $x\dfrac{d^2y}{dx^2} - \dfrac{dy}{dx} = 0$

</details>

---

### Q13. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The degree of the differential equation obtained from the equation $(y - a)^2 = 4(x - b)$ [where $a$ and b are arbitrary constants] is

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** not defined

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

Given equation: $(y - a)^2 = 4(x - b)$

Since there are two arbitrary constants $a$ and $b$, we differentiate the equation twice with respect to $x$.

Differentiating with respect to $x$:

$2(y - a) \dfrac{dy}{dx} = 4$

$(y - a) \dfrac{dy}{dx} = 2$

Differentiating again with respect to $x$:

$\left(\dfrac{dy}{dx}\right)^2 + (y - a) \dfrac{d^2y}{dx^2} = 0$

From the first derivative, we have $y - a = \dfrac{2}{\dfrac{dy}{dx}}$. Substituting this into the second derivative equation:

$\left(\dfrac{dy}{dx}\right)^2 + \dfrac{2}{\dfrac{dy}{dx}} \dfrac{d^2y}{dx^2} = 0$

Multiplying the entire equation by $\dfrac{dy}{dx}$ to make it a polynomial in derivatives:

$\left(\dfrac{dy}{dx}\right)^3 + 2 \dfrac{d^2y}{dx^2} = 0$

The highest order derivative in this differential equation is $\dfrac{d^2y}{dx^2}$, and its highest power is $1$.

Therefore, the degree of the differential equation is $1$.

Answer: $1$

</details>

---

### Q14. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of $3y = \sqrt[3]{x+c}$ is

**Options:**

- **(A)** $\dfrac{dy}{dx} = \dfrac{1}{9y^2}$
- **(B)** $\dfrac{dy}{dx} = \dfrac{1}{27y^2}$
- **(C)** $\dfrac{dy}{dx} = \dfrac{1}{81y^2}$
- **(D)** $\dfrac{dy}{dx} = \dfrac{1}{36y^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{dy}{dx} = \dfrac{1}{81y^2}$**

**Detailed Solution:**

Given equation is $3y = \sqrt[3]{x+c}$

Cubing both sides, we get:

$27y^3 = x + c$

Differentiating both sides with respect to $x$:

$27 \times 3y^2 \dfrac{dy}{dx} = 1$

$81y^2 \dfrac{dy}{dx} = 1$

$\dfrac{dy}{dx} = \dfrac{1}{81y^2}$

Answer: $\dfrac{dy}{dx} = \dfrac{1}{81y^2}$

</details>

---

### Q15. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation representing the family of curves $x \sin x + y^3 = 4ax$ is

**Options:**

- **(A)** $\dfrac{dy}{dx} = \dfrac{y^3 + x^2 \cos x}{3xy^2}$
- **(B)** $\dfrac{dy}{dx} = \dfrac{y^3 - x^2 \cos x}{3xy^2}$
- **(C)** $\dfrac{dy}{dx} = \dfrac{y^3 - x^2 \cos x}{3xy}$
- **(D)** $\dfrac{dy}{dx} = \dfrac{y^3 - x^2 \cos x}{3x^2 y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{dy}{dx} = \dfrac{y^3 - x^2 \cos x}{3xy^2}$**

**Detailed Solution:**

The given equation of the family of curves is $x \sin x + y^3 = 4ax$.

Dividing the entire equation by $x$, we get:

$\sin x + \dfrac{y^3}{x} = 4a$

Differentiating both sides with respect to $x$, we obtain:

$\cos x + \dfrac{3y^2 \dfrac{dy}{dx} \cdot x - y^3 \cdot 1}{x^2} = 0$

Multiplying the equation by $x^2$ gives:

$x^2 \cos x + 3xy^2 \dfrac{dy}{dx} - y^3 = 0$

Rearranging the terms to solve for $\dfrac{dy}{dx}$:

$3xy^2 \dfrac{dy}{dx} = y^3 - x^2 \cos x$

$\dfrac{dy}{dx} = \dfrac{y^3 - x^2 \cos x}{3xy^2}$

Answer: $\dfrac{dy}{dx} = \dfrac{y^3 - x^2 \cos x}{3xy^2}$

</details>

---

### Q16. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation representing the family of parabolas having vertex at the origin and axis along the positive Y-axis is

**Options:**

- **(A)** $x \frac{\mathrm{dy}}{\mathrm{~d} x}-2 \mathrm{y}=0$
- **(B)** $\frac{\mathrm{dy}}{\mathrm{~d} x}+x \mathrm{y}=0$
- **(C)** $x \frac{\mathrm{dy}}{\mathrm{~d} x}+\mathrm{y}=0$
- **(D)** $x^2 \frac{\mathrm{dy}}{\mathrm{~d} x}+\mathrm{y}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x \frac{\mathrm{dy}}{\mathrm{~d} x}-2 \mathrm{y}=0$**

**Detailed Solution:**

The equation of the family of parabolas having vertex at the origin and axis along the positive Y-axis is given by

$x^2 = 4ay$

where $a$ is an arbitrary constant.

Differentiating both sides with respect to $x$, we get

$2x = 4a \dfrac{\mathrm{dy}}{\mathrm{d}x}$

From the equation of the parabola, we have $4a = \dfrac{x^2}{y}$. Substituting this value in the above equation, we get

$2x = \left(\dfrac{x^2}{y}\right) \dfrac{\mathrm{dy}}{\mathrm{d}x}$

$2xy = x^2 \dfrac{\mathrm{dy}}{\mathrm{d}x}$

Dividing by $x$ (for $x \neq 0$), we get

$x \dfrac{\mathrm{dy}}{\mathrm{d}x} - 2y = 0$

Answer: $x \frac{\mathrm{dy}}{\mathrm{~d} x}-2 \mathrm{y}=0$

</details>

---

### Q17. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of the curve passing through the point $(0,2)$ given that the sum of the ordinate and abscissa of any point exceeds the slope of the tangent to the curve at that point by 5 is

**Options:**

- **(A)** $\mathrm{y}=x-4-2 \mathrm{e}^x$
- **(B)** $y=4-x-2 e^x$
- **(C)** $\mathrm{y}=4+x-2 \mathrm{e}^x$
- **(D)** $y=4-x+2 e^x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $y=4-x-2 e^x$**

**Detailed Solution:**

Let the point on the curve be $(x, y)$.

According to the given condition, the sum of the ordinate and abscissa exceeds the slope of the tangent by $5$.

$x + y = \dfrac{dy}{dx} + 5$

$\dfrac{dy}{dx} - y = x - 5$

This is a linear differential equation of the form $\dfrac{dy}{dx} + Py = Q$, where $P = -1$ and $Q = x - 5$.

Integrating Factor (I.F.) $= e^{\int P dx} = e^{\int -1 dx} = e^{-x}$

The general solution is given by:

$y \times (\text{I.F.}) = \int Q \times (\text{I.F.}) dx + C$

$y e^{-x} = \int (x - 5) e^{-x} dx + C$

Using integration by parts:

$y e^{-x} = (x - 5)(-e^{-x}) - \int (1)(-e^{-x}) dx + C$

$y e^{-x} = -x e^{-x} + 5 e^{-x} - e^{-x} + C$

$y e^{-x} = (4 - x) e^{-x} + C$

Multiplying by $e^x$ on both sides:

$y = 4 - x + C e^x$

Since the curve passes through the point $(0, 2)$, substitute $x = 0$ and $y = 2$:

$2 = 4 - 0 + C e^0$

$2 = 4 + C$

$C = -2$

Substituting $C = -2$ in the general solution, we get the equation of the curve:

$y = 4 - x - 2 e^x$

Answer: $y=4-x-2 e^x$

</details>

---

### Q18. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation which represents the family of curves $\mathrm{y}=\mathrm{C}_1 \mathrm{e}^{\mathrm{c}_2 x}$, where $\mathrm{C}_1, \mathrm{C}_2$ are arbitrary constants is

**Options:**

- **(A)** $y^{\prime \prime}=y^{\prime} y$
- **(B)** $y y^{\prime \prime}=y^{\prime}$
- **(C)** $y y^{\prime \prime}=\left(y^{\prime}\right)^2$
- **(D)** $\mathrm{y}^{\prime}=\mathrm{y}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y y^{\prime \prime}=\left(y^{\prime}\right)^2$**

**Detailed Solution:**

Given equation of the family of curves is $y = C_1 e^{C_2 x}$.

Taking natural logarithm on both sides:

$\ln y = \ln C_1 + C_2 x$

Differentiating with respect to $x$:

$\dfrac{1}{y} y' = C_2$

Differentiating again with respect to $x$:

$\dfrac{y y'' - (y')^2}{y^2} = 0$

$y y'' - (y')^2 = 0$

$y y'' = (y')^2$

Answer: $y y^{\prime \prime}=\left(y^{\prime}\right)^2$

</details>

---

### Q19. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\mathrm{y}=\mathrm{e}^x(\mathrm{~A} \cos x+\mathrm{B} \sin x)$ is the solution of the differential equation

**Options:**

- **(A)** $x^2 \frac{\mathrm{~d}^2 \mathrm{y}}{\mathrm{d} x^2}+\left(1+\mathrm{y}^2\right)=0$
- **(B)** $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}-\frac{\mathrm{dy}}{\mathrm{d} x}+\mathrm{y}=0$
- **(C)** $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}-2 \frac{\mathrm{dy}}{\mathrm{d} x}+2 \mathrm{y}=0$
- **(D)** $x \frac{\mathrm{~d}^2 \mathrm{y}}{\mathrm{d} x^2}-2 \frac{\mathrm{dy}}{\mathrm{d} x}+2 \mathrm{y}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}-2 \frac{\mathrm{dy}}{\mathrm{d} x}+2 \mathrm{y}=0$**

**Detailed Solution:**

Given $y = e^x (A \cos x + B \sin x)$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = e^x (A \cos x + B \sin x) + e^x (-A \sin x + B \cos x)$

$\dfrac{dy}{dx} = y + e^x (-A \sin x + B \cos x)$

$\dfrac{dy}{dx} - y = e^x (-A \sin x + B \cos x)$

Differentiating again with respect to $x$:

$\dfrac{d^2y}{dx^2} - \dfrac{dy}{dx} = e^x (-A \sin x + B \cos x) + e^x (-A \cos x - B \sin x)$

Substituting $\dfrac{dy}{dx} - y$ for the first term and $-y$ for the second term:

$\dfrac{d^2y}{dx^2} - \dfrac{dy}{dx} = \left(\dfrac{dy}{dx} - y\right) - y$

$\dfrac{d^2y}{dx^2} - 2\dfrac{dy}{dx} + 2y = 0$

Answer: $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}-2 \frac{\mathrm{dy}}{\mathrm{d} x}+2 \mathrm{y}=0$

</details>

---

### Q20. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of all circles touching the Y-axis at the origin and centre on the X -axis is

**Options:**

- **(A)** $x^2+\mathrm{y}^2+2 x y \frac{\mathrm{dy}}{\mathrm{d} x}=0$
- **(B)** $x^2-y^2+2 x y \frac{d y}{d x}=0$
- **(C)** $2 x^2+\mathrm{y}^2+x \mathrm{y} \frac{\mathrm{dy}}{\mathrm{d} x}=0$
- **(D)** $x^2-2 \mathrm{y}^2+2 x \mathrm{y} \frac{\mathrm{dy}}{\mathrm{d} x}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2-y^2+2 x y \frac{d y}{d x}=0$**

**Detailed Solution:**

The equation of a circle touching the Y-axis at the origin and having its centre on the X-axis is given by $(x - a)^2 + y^2 = a^2$, where $(a, 0)$ is the centre and $a$ is the radius.

Expanding this, we get:
$x^2 - 2ax + a^2 + y^2 = a^2$
$x^2 + y^2 = 2ax$

Differentiating both sides with respect to $x$, we get:
$2x + 2y \dfrac{dy}{dx} = 2a$

Substituting the value of $2a$ back into the equation of the circle, we get:
$x^2 + y^2 = \left(2x + 2y \dfrac{dy}{dx}\right)x$

$x^2 + y^2 = 2x^2 + 2xy \dfrac{dy}{dx}$

$x^2 - y^2 + 2xy \dfrac{dy}{dx} = 0$

Answer: $x^2-y^2+2 x y \frac{d y}{d x}=0$

</details>

---

### Q21. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation satisfied by $y=X \sin (6 t+5)+Y \cos (6 t+5)$ is (where $X$ and $Y$ are constants)

**Options:**

- **(A)** $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{dt}^2}+6 \mathrm{y}=0$
- **(B)** $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{dt}^2}=0$
- **(C)** $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{dt}^2}+36 \mathrm{y}=0$
- **(D)** $\frac{d^2 y}{d t^2}+25 y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{dt}^2}+36 \mathrm{y}=0$**

**Detailed Solution:**

Given equation is $y = X \sin(6t + 5) + Y \cos(6t + 5)$

Differentiating with respect to $t$, we get

$\dfrac{dy}{dt} = 6X \cos(6t + 5) - 6Y \sin(6t + 5)$

Differentiating again with respect to $t$, we get

$\dfrac{d^2y}{dt^2} = -36X \sin(6t + 5) - 36Y \cos(6t + 5)$

$\dfrac{d^2y}{dt^2} = -36[X \sin(6t + 5) + Y \cos(6t + 5)]$

Substituting the value of $y$, we get

$\dfrac{d^2y}{dt^2} = -36y$

$\dfrac{d^2y}{dt^2} + 36y = 0$

Answer: $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{dt}^2}+36 \mathrm{y}=0$

</details>

---

### Q22. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of all circles having their centres on the line $\mathrm{y}=5$ and touching X -axis is ......

**Options:**

- **(A)** $(5-\mathrm{y}) \frac{\mathrm{d} y}{\mathrm{~d} x}+\mathrm{y}^2-10 \mathrm{y}=0$
- **(B)** $(5-\mathrm{y})^2 \frac{\mathrm{~d}^2 y}{\mathrm{~d} x^2}+\mathrm{y}^2-10 \mathrm{y}=0$
- **(C)** $(5-\mathrm{y}) \frac{\mathrm{dy}}{\mathrm{d} x}+\mathrm{y}-10=0$
- **(D)** $(5-\mathrm{y})^2\left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)^2+\mathrm{y}^2-10 \mathrm{y}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(5-\mathrm{y})^2\left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)^2+\mathrm{y}^2-10 \mathrm{y}=0$**

**Detailed Solution:**

Let the centre of the circle be $(h, 5)$.

Since the circle touches the X-axis, its radius is $r = 5$.

The equation of the circle is:

$(x - h)^2 + (y - 5)^2 = 5^2$

$(x - h)^2 + (y - 5)^2 = 25$

Differentiating with respect to $x$:

$2(x - h) + 2(y - 5) \dfrac{dy}{dx} = 0$

$x - h = -(y - 5) \dfrac{dy}{dx} = (5 - y) \dfrac{dy}{dx}$

Substituting the value of $(x - h)$ in the equation of the circle:

$\left( (5 - y) \dfrac{dy}{dx} \right)^2 + (y - 5)^2 = 25$

$(5 - y)^2 \left( \dfrac{dy}{dx} \right)^2 + y^2 - 10y + 25 = 25$

$(5 - y)^2 \left( \dfrac{dy}{dx} \right)^2 + y^2 - 10y = 0$

Answer: $(5-\mathrm{y})^2\left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)^2+\mathrm{y}^2-10 \mathrm{y}=0$

</details>

---

### Q23. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation whose solution represents the family $x^2 y=4 e^x+c$, where $c$ is an arbitrary constant, is

**Options:**

- **(A)** $x \frac{\mathrm{dy}}{\mathrm{d} x}+x \mathrm{y}=0$
- **(B)** $x^2 \frac{\mathrm{dy}}{\mathrm{d} x}+(2 xy-4e^x)=0$
- **(C)** $x \frac{\mathrm{dy}}{\mathrm{d} x}+(x-2) \mathrm{y}=0$
- **(D)** $x \frac{\mathrm{dy}}{\mathrm{d} x}+(2-x) \mathrm{y}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2 \frac{\mathrm{dy}}{\mathrm{d} x}+(2 xy-4e^x)=0$**

**Detailed Solution:**

The given equation of the family of curves is $x^2 y = 4 e^x + c$.

Differentiating both sides with respect to $x$, we get:

$\dfrac{d}{dx}(x^2 y) = \dfrac{d}{dx}(4 e^x + c)$

$x^2 \dfrac{dy}{dx} + y \dfrac{d}{dx}(x^2) = 4 e^x$

$x^2 \dfrac{dy}{dx} + 2xy = 4 e^x$

$x^2 \dfrac{dy}{dx} + (2xy - 4 e^x) = 0$

Answer: $x^2 \frac{\mathrm{dy}}{\mathrm{d} x}+(2 xy-4e^x)=0$

</details>

---

### Q24. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of all straight lines passing through the point $(1,-1)$ is

**Options:**

- **(A)** $\mathrm{y}=(x-1) \frac{\mathrm{dy}}{\mathrm{d} x}-1$
- **(B)** $x=(x-1) \frac{\mathrm{dy}}{\mathrm{d} x}+1$
- **(C)** $\mathrm{y}=(x-1) \frac{\mathrm{dy}}{\mathrm{d} x}$
- **(D)** $\mathrm{y}=2(x-1) \frac{\mathrm{dy}}{\mathrm{d} x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{y}=(x-1) \frac{\mathrm{dy}}{\mathrm{d} x}-1$**

**Detailed Solution:**

The equation of the family of straight lines passing through the point $(1, -1)$ is

$y - (-1) = m(x - 1)$

$y + 1 = m(x - 1)$

Differentiating with respect to $x$, we get

$\dfrac{dy}{dx} = m$

Substituting the value of $m$ in the equation of the line, we get

$y + 1 = \dfrac{dy}{dx}(x - 1)$

$y = (x - 1)\dfrac{dy}{dx} - 1$

Answer: $\mathrm{y}=(x-1) \frac{\mathrm{dy}}{\mathrm{d} x}-1$

</details>

---

### Q25. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation obtained by eliminating arbitrary constant from the equation $y^2=(x+c)^3$ is

**Options:**

- **(A)** $\left(\dfrac{\mathrm{d} y}{\mathrm{~d} x}\right)^3=27 y$
- **(B)** $\left(\dfrac{\mathrm{d} y}{\mathrm{~d} x}\right)^3=-27 y$
- **(C)** $8\left(\dfrac{\mathrm{~d} y}{\mathrm{~d} x}\right)^3=27 y$
- **(D)** $8\left(\dfrac{\mathrm{~d} y}{\mathrm{~d} x}\right)^3+27 y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8\left(\dfrac{\mathrm{~d} y}{\mathrm{~d} x}\right)^3=27 y$**

**Detailed Solution:**

Given equation is $y^2 = (x+c)^3$.

Differentiating both sides with respect to $x$, we get:

$2y \dfrac{\mathrm{d}y}{\mathrm{d}x} = 3(x+c)^2$

Cubing both sides to eliminate the fractional power of $(x+c)$:

$8y^3 \left(\dfrac{\mathrm{d}y}{\mathrm{d}x}\right)^3 = 27(x+c)^6$

Squaring the original given equation, we get:

$y^4 = (x+c)^6$

Substituting $(x+c)^6 = y^4$ into the cubed differential equation:

$8y^3 \left(\dfrac{\mathrm{d}y}{\mathrm{d}x}\right)^3 = 27y^4$

Dividing both sides by $y^3$ (assuming $y \neq 0$), we obtain:

$8\left(\dfrac{\mathrm{d}y}{\mathrm{d}x}\right)^3 = 27y$

Answer: $8\left(\dfrac{\mathrm{~d} y}{\mathrm{~d} x}\right)^3=27 y$

</details>

---

### Q26. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of $y=\mathrm{e}^x(\mathrm{a} \cos x+\mathrm{b} \sin x)$ is

**Options:**

- **(A)** $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}-2 \frac{\mathrm{d} y}{\mathrm{~d} x}-y=0$
- **(B)** $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}+2 \frac{\mathrm{d} y}{\mathrm{~d} x}+2 y=0$
- **(C)** $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}-2 \frac{\mathrm{d} y}{\mathrm{~d} x}+y=0$
- **(D)** $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}-2 \frac{\mathrm{d} y}{\mathrm{~d} x}+2 y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}-2 \frac{\mathrm{d} y}{\mathrm{~d} x}+2 y=0$**

**Detailed Solution:**

$\begin{aligned} & y=\mathrm{e}^x(\mathrm{a} \cos x+\mathrm{b} \sin x) \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\mathrm{e}^x(\mathrm{a} \cos x+\mathrm{b} \sin x) \\ & +\mathrm{e}^x(\mathrm{~b} \cos x-\mathrm{a} \sin x) \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=y+\mathrm{e}^x(\mathrm{~b} \cos x-\mathrm{a} \sin x) \\ & \Rightarrow \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}=\frac{\mathrm{d} y}{\mathrm{~d} x}+\mathrm{e}^x(\mathrm{~b} \cos x-\mathrm{a} \sin x) \\ & +\mathrm{e}^x(-\mathrm{b} \sin x-\mathrm{a} \cos x) \\ & \Rightarrow \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}=\frac{\mathrm{d} y}{\mathrm{~d} x}+\left(\frac{\mathrm{d} y}{\mathrm{~d} x}-y\right)-y \\ & \Rightarrow \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}-2 \frac{\mathrm{d} y}{\mathrm{~d} x}+2 y=0 \\ & \end{aligned}$

</details>

---

### Q27. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The parametric equations of the curve $x^2+y^2+a x+b y=0$ are

**Options:**

- **(A)** $x=\frac{\mathrm{a}}{2}+\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}} \cos \theta, y=\frac{\mathrm{b}}{2}+\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}} \sin \theta$
- **(B)** $x=\frac{\mathrm{a}}{2}-\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}} \cos \theta, y=\frac{\mathrm{b}}{2}-\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}} \sin \theta$
- **(C)** $x=-\frac{\mathrm{a}}{2}+\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}} \cos \theta, y=-\frac{\mathrm{b}}{2}+\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}} \sin \theta$
- **(D)** $x=-\frac{\mathrm{a}}{2}-\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}} \cos \theta, y=-\frac{\mathrm{b}}{2}-\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}} \sin \theta$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x=-\frac{\mathrm{a}}{2}+\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}} \cos \theta, y=-\frac{\mathrm{b}}{2}+\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}} \sin \theta$**

**Detailed Solution:**

$$
\begin{aligned}
& x^2+y^2+\mathrm{a} x+\mathrm{b} y=0 \\
& \Rightarrow\left(x+\frac{\mathrm{a}}{2}\right)^2+\left(y+\frac{\mathrm{b}}{2}\right)^2=\frac{\mathrm{a}^2+\mathrm{b}^2}{4}
\end{aligned}
$$
Comparing with $(x-\mathrm{h})^2+(y-\mathrm{k})^2=\mathrm{r}^2$, we get
$$
\mathrm{h}=-\frac{\mathrm{a}}{2}, \mathrm{k}=-\frac{\mathrm{b}}{2}, \mathrm{r}=\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}}
$$
$\therefore \quad$ The parametric equations are
$$
x=-\frac{\mathrm{a}}{2}+\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}} \cos \theta, y=-\frac{\mathrm{b}}{2}+\sqrt{\frac{\mathrm{a}^2+\mathrm{b}^2}{4}} \sin \theta
$$

</details>

---

### Q28. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x^k+y^k=a^k(a, k>0)$ and $\frac{d y}{d x}+\left(\frac{y}{x}\right)^{\frac{1}{b}}-0$, then $\mathrm{k}$ has the value

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{2}{3}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{2}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{3}$**

**Detailed Solution:**

$x^{\mathrm{k}}+y^{\mathrm{k}}=\mathrm{a}^{\mathrm{k}}$
Differentiating w.r.t. $x$, we get
$\begin{aligned}
& \mathrm{k} x^{k-1}+\mathrm{k} y^{\mathrm{k}-1} \frac{\mathrm{d} y}{\mathrm{~d} x}=0 \\
\therefore \quad & \frac{\mathrm{d} y}{\mathrm{~d} x}=-\frac{\mathrm{k} x^{\mathrm{k}-1}}{\mathrm{k} y^{\mathrm{k}-1}} \\
\therefore \quad & \frac{\mathrm{d} y}{\mathrm{~d} x}=-\left(\frac{x}{y}\right)^{\mathrm{k}-1} \\
& \frac{\mathrm{d} y}{\mathrm{~d} x}+\left(\frac{y}{x}\right)^{1-\mathrm{k}}=0 \\
& \text { But } \frac{\mathrm{d} y}{\mathrm{~d} x}+\left(\frac{y}{x}\right)^{\frac{1}{3}}=0 ...[Given]
\end{aligned}$ 
Comparing above equations, we get
$\begin{aligned}
1-k & =\frac{1}{3} \\
& 1-\frac{1}{3}=k \\
\therefore \quad k & =\frac{2}{3}
\end{aligned}$

</details>

---

### Q29. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of all circles which pass through the origin and whose centres lie on $\mathrm{Y}$-axis is

**Options:**

- **(A)** $\left(x^2-y^2\right) \frac{d y}{d x}-2 x y=0$
- **(B)** $\left(x^2-y^2\right) \frac{d y}{d x}+2 x y=0$
- **(C)** $\left(x^2-y^2\right) \frac{d y}{d x}+x y=0$
- **(D)** $\left(x^2-y^2\right) \frac{d y}{d x}-x y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(x^2-y^2\right) \frac{d y}{d x}-2 x y=0$**

**Detailed Solution:**

Circle passes through origin and centre lie on $\mathrm{Y}$-axis.
Let $(0, k)$ be centre and ' $k$ ' be radius
$\therefore \quad$ Equation of circle is
$\begin{aligned}
& (x-0)^2+(y-\mathrm{k})^2=\mathrm{k}^2 \\
& x^2+y^2-2 y \mathrm{k}+\mathrm{k}^2=\mathrm{k}^2 \\
& x^2+y^2-2 \mathrm{k} y=0 \\
& x^2+y^2=2 \mathrm{k} y ...(i)\\
& \frac{x^2+y^2}{2 y}=\mathrm{k} ...(ii)
\end{aligned}$
Differentiating equation (i) with respect to $x$, we get
$\begin{aligned}
& 2 x+2 y \frac{\mathrm{d} y}{\mathrm{~d} x}=2 \mathrm{k} \frac{\mathrm{d} y}{\mathrm{~d} x} \\
& 2 x+2 y \frac{\mathrm{d} y}{\mathrm{~d} x}-2 \mathrm{k} \frac{\mathrm{d} y}{\mathrm{~d} x}=0 \\
& 2 x+2(y-\mathrm{k}) \frac{\mathrm{d} y}{\mathrm{~d} x}=0 \\
& 2 x+2\left[y-\left(\frac{x^2+y^2}{2 y}\right)\right] \frac{\mathrm{d} y}{\mathrm{~d} x}=0 ...[From(ii)]\\
& 2 x+2\left[\frac{2 y^2-x^2-y^2}{2 y}\right] \frac{\mathrm{d} y}{\mathrm{~d} x}=0 \\
& 2 x+\left(\frac{y^2-x^2}{y}\right) \frac{\mathrm{d} y}{\mathrm{~d} x}=0 \\
& 2 x y+\left(y^2-x^2\right) \frac{\mathrm{d} y}{\mathrm{~d} x}=0 \\
& \text { i.e. }\left(x^2-y^2\right) \frac{\mathrm{d} y}{\mathrm{~d} x}-2 x y=0
\end{aligned}$

</details>

---

### Q30. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of all parabolas, whose axes are parallel to $\mathrm{Y}$-axis, is

**Options:**

- **(A)** $y_3=1$
- **(B)** $y_3=-1$
- **(C)** $y_3=0$
- **(D)** $yy_3+y_1=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y_3=0$**

**Detailed Solution:**

Parabola whose axes are parallel to $\mathrm{Y}$-axis. Vertex is not $(0,0)$
Equation becomes
$(x-\mathrm{h})^2=4 \mathrm{~b}(y-\mathrm{k})$
Differentiating w.r.t. $x$, we get
$2(x-h)=4 b\left(\frac{d y}{d x}\right)$
Again differentiating w.r.t. $x$, we get
$2=4 \mathrm{~b}\left(\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}\right)$
Again differentiating w.r.t. $x$, we get
$\begin{aligned}
& 0=4 b\left(\frac{\mathrm{d}^3 y}{\mathrm{~d} x^3}\right) \\
\therefore \quad & \frac{\mathrm{d}^3 y}{\mathrm{~d} x^3}=0 \\
& \text { i.e., } y_3=0
\end{aligned}$

</details>

---

### Q31. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of family of lines, having $x$-intercept as a and $y$-intercept as $b$, is

**Options:**

- **(A)** $\frac{d^2 y}{d x^2}=0$
- **(B)** $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}-\frac{\mathrm{d} y}{\mathrm{~d} x}+y=0$
- **(C)** $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}+\frac{\mathrm{d} y}{\mathrm{~d} x}=y$
- **(D)** $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}+\frac{\mathrm{d} y}{\mathrm{~d} x}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{d^2 y}{d x^2}=0$**

**Detailed Solution:**

Diff $\frac{x}{a}+\frac{y}{b}=1$ [two arbitrary constants]
$\frac{1}{a}+\frac{1}{b} \cdot \frac{\mathrm{d} y}{\mathrm{~d} x}=0$
Again in diff $0+\frac{1}{b} \cdot \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}=0$
$\Rightarrow \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}=0$

</details>

---

### Q32. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

An ice ball melts at the rate which is proportional to the amount of ice at that instant. Half the quantity of ice melts in 20 minutes. $x_0$ is the initial quantity of ice. If after 40 minutes the amount of ice left is $k x_0 x$, then $k$ is

**Options:**

- **(A)** $\frac{1}{8}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{4}$**

**Detailed Solution:**

$\begin{aligned} & \frac{\mathrm{d} x}{\mathrm{~d} t}=-k x \\ & \Rightarrow \frac{\mathrm{d} x}{x}=-k d t \\ & \Rightarrow \log _e x=-k t+c \\ & \Rightarrow x=e^{-k t+c}=e^c \cdot e^{-k t} \\ & \text { at } t=0, x^{-k}=x_0 \\ & \Rightarrow e^c=x_0 \\ & \Rightarrow x=x_0 e^{-k t}\end{aligned}$

</details>

---

### Q33. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of the curve passing through the point $(0,-2)$ given that at any point $(x, y)$ on the curve, the product of the slope of its tangent and $y$-co-ordinate of the point is equal to the $x$-co-ordinate of the point, is

**Options:**

- **(A)** $y^2+x^2=4$
- **(B)** $y^2-x^2=4$
- **(C)** $2 y^2+x^2=8$
- **(D)** $4 y^2+3 x^2=16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $y^2-x^2=4$**

**Detailed Solution:**

$\begin{aligned}
& A / Q \frac{d y}{d x} \cdot y=x \\
& \Rightarrow \int y d y=\int x d x \\
& \Rightarrow \frac{y^2}{2}=\frac{x^2}{2}+c
\end{aligned}$
putting $x=0$ and $y=-2$ we get $c=2$
$\begin{aligned}
& \Rightarrow \frac{y^2}{2}=\frac{x^2}{2}+2 \\
& \Rightarrow y^2-x^2=4
\end{aligned}$

</details>

---

### Q34. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Water at $100^{\circ} \mathrm{C}$ cools in 10 minutes to $80^{\circ} \mathrm{C}$ in a room temperature of $25^{\circ} \mathrm{C}$, then the temperature of water after 20 minutes will be

**Options:**

- **(A)** $65.33^{\circ} \mathrm{C}$
- **(B)** $69.33^{\circ} \mathrm{C}$
- **(C)** $60.33^{\circ} \mathrm{C}$
- **(D)** $63.33^{\circ} \mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $65.33^{\circ} \mathrm{C}$**

**Detailed Solution:**

$\begin{aligned} & \frac{\mathrm{d} T}{\mathrm{~d} t}=-k(T-25) \\ & \Rightarrow T-25=e^{-k t+c} \\ & \Rightarrow T=25+e^c \cdot e^{-k t} \\ & \text { for } t=0, T=100 \\ & \Rightarrow e^c=75 \\ & \Rightarrow T=25+75 e^{-k t} \\ & \text { for } t=10, T=80 \\ & \Rightarrow 80=25+75 e^{-k \times 10} \\ & \Rightarrow-10 k=\log \left(\frac{11}{55}\right) \\ & \text { i.e., } T=25+75 e^{\left(\frac{1}{10} \log \frac{11}{15}\right) t} \\ & \text { Now for } t=20, T=25+75 e^{20 \times \frac{1}{10} \log \frac{11}{15}}=25+75 \times\left(\frac{11}{15}\right)^2 \\ & \Rightarrow T=25+40.33=65.33 \\ & \end{aligned}$

</details>

---

### Q35. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation whose solution is $y=c^2+\frac{c}{x}$, where $c$ is constant, is

**Options:**

- **(A)** $x^4\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^2-x \frac{\mathrm{d} y}{\mathrm{~d} x}-y=0$
- **(B)** $x^2\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^2+\frac{\mathrm{d} y}{\mathrm{~d} x}-y=0$
- **(C)** $x\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^2-x^2 \frac{\mathrm{d} y}{\mathrm{~d} x}+y=0$
- **(D)** $x^4\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^2-\frac{\mathrm{d} y}{\mathrm{~d} x}+y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x^4\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^2-x \frac{\mathrm{d} y}{\mathrm{~d} x}-y=0$**

**Detailed Solution:**

$\begin{aligned} & y=c^2+\frac{c}{x} \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{-c}{x^2} \\ & \Rightarrow c=-x^2 \frac{\mathrm{d} y}{\mathrm{~d} x}\end{aligned}$
$\begin{aligned} & \text { Hence, } y=\left(-x^2 \frac{\mathrm{d} y}{\mathrm{~d} x}\right)^2+\left(-x^2 \frac{\mathrm{d} y}{\mathrm{~d} x}\right) \times \frac{1}{x} \\ & \Rightarrow y=x^4 \cdot\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^2-x \cdot \frac{\mathrm{d} y}{\mathrm{~d} x} \\ & \Rightarrow x^4\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^2-x \cdot \frac{\mathrm{d} y}{\mathrm{~d} x}-y=0\end{aligned}$

</details>

---

### Q36. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The general solution of differential equation $x d y-y d x=0$ represents

**Options:**

- **(A)** the circle whose centre is at the origin
- **(B)** a straight line passing through the origin
- **(C)** a rectangular hyperbola
- **(D)** the parabola whose vertex is at the origin.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a straight line passing through the origin**

**Detailed Solution:**

$\begin{aligned} & x d y-y d x=0 \Rightarrow \int \frac{d y}{y}=\int \frac{d x}{x} \\ & \Rightarrow \log y=\log x+\log c \\ & \Rightarrow \log y=\log c x \\ & \Rightarrow y=c x\end{aligned}$
which is a straight line passing through the origin

</details>

---

### Q37. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation $\frac{d y}{d x}=\frac{\sqrt{1-y^2}}{y}$ determines a family of circles with

**Options:**

- **(A)** variable radii and a fixed centre at $(0,-1)$
- **(B)** fixed radius of 1 unit and variable centres along the $\mathrm{X}$-axis
- **(C)** fixed radius of 1 unit and variable centres along the Y-axis
- **(D)** variable radii and a fixed centre at $(0,1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) fixed radius of 1 unit and variable centres along the $\mathrm{X}$-axis**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}=\frac{\sqrt{1-y^2}}{y} \\ & \Rightarrow \int \frac{y d y}{\sqrt{1-y^2}}=\int d x \\ & \Rightarrow-\sqrt{1-y^2}=x+c \\ & \Rightarrow 1-y^2=(x+c)^2 \\ & \Rightarrow(x+c)^2+y^2=1\end{aligned}$
The above equation represents a circle having centre at $(-c, 0)$ which is variable and radius is equal to ' 1 ' which is fixed.

</details>

---

### Q38. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The differential equation of all parabolas whose axis is y-axis, is

**Options:**

- **(A)** $\frac{d^2 y}{d x^2}-\frac{d y}{d x}=0$
- **(B)** $\frac{d^2 y}{d x^2}+\frac{d y}{d x}=0$
- **(C)** $x \frac{d^2 y}{d x^2}-\frac{d y}{d x}=0$
- **(D)** $\frac{d^2 y}{d x^2}-y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x \frac{d^2 y}{d x^2}-\frac{d y}{d x}=0$**

**Detailed Solution:**

Differential Equation of parabolas whose axis is $\mathrm{Y}$ axis, is Let the vertex be $(0, \mathrm{k})$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Pcu8T3ZiK-wDF3euPTtMkL5ILeiqY35S3kthIecuRks.original.fullsize.png">

$\begin{aligned}
& \therefore x^2=4 b y-4 b k \\
& \therefore 2 x=4 b \frac{d y}{d x}-0 \Rightarrow b=\left(\frac{x}{2}\right) \times \frac{1}{\left(\frac{d y}{d x}\right)} \\
& 2 x=4 b \frac{d y}{d x}-0 \Rightarrow b=\left(\frac{x}{2}\right) \times \frac{1}{\left(\frac{d y}{d x}\right)}
\end{aligned}$
Substituting value of $b$ in eq. (1), we get
$\begin{aligned}
& \therefore \quad x^2=4\left(\frac{x}{2}\right) \times \frac{1}{\left(\frac{d y}{d x}\right)}(y-k) \\
& \therefore \quad \mathrm{x}^2\left(\frac{\mathrm{dy}}{\mathrm{dx}}\right)=2 \mathrm{x}(\mathrm{y}-\mathrm{k}) \\
& \therefore \quad x^2\left(\frac{d^2 y}{d x^2}\right)+\left(\frac{d y}{d x}\right)(2 x)=2 x \frac{d y}{d x}+2(y-k) \\
& \therefore \quad \mathrm{y}-\mathrm{k}=\frac{\mathrm{x}^2\left(\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{dx}}\right)}{2} \\
&
\end{aligned}$
Substituting value of $(\mathrm{y}-\mathrm{k})$ in eq. (1), we get
$\begin{aligned}
& \left.x^2=4\left(\frac{x}{2}\right)\left[\frac{1}{\left(\frac{d y}{d x}\right)}\right]^{\left.\frac{x^2\left(\frac{d^2 y}{d^2}\right)}{2}\right]}\right] \\
& \therefore \quad x^2\left(\frac{d y}{d x}\right)=x^3\left(\frac{d^2 y}{d x^2}\right) \Rightarrow x\left(\frac{d^2 y}{d x^2}\right)-\left(\frac{d y}{d x}\right)=0
\end{aligned}$

</details>

---

### Q39. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation obtained by eliminating $\mathrm{A}$ and $\mathrm{B}$ from $y=A \cos \omega t+B \sin \omega t$

**Options:**

- **(A)** $\frac{d^2 y}{d t^2}+\omega^2 y=0$
- **(B)** $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{dt}^2}+\omega \mathrm{y}^2=0$
- **(C)** $\frac{d^2 y}{d t^2}-\omega^2 y=0$
- **(D)** $\frac{d^2 y}{d t^2}-\omega y^2=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{d^2 y}{d t^2}+\omega^2 y=0$**

**Detailed Solution:**

$\begin{aligned} & y=A \cos \omega t+B \sin \omega t \\ & \therefore \quad \frac{d y}{d t}=-A \omega \sin \omega t+B \omega \cos \omega t \\ & \frac{d^2 y}{d t^2}=-A \omega^2 \cos \omega t-B \omega^2 \sin \omega t \\ & =-\omega^2(A \cos \omega t+B \sin \omega t)=-\omega^2 y \\ & \therefore \quad \frac{d^2 y}{d t^2}+\omega^2 y=0\end{aligned}$

</details>

---

### Q40. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of the family of parabolas with focus at the origin and the $\mathrm{X}$ - axis as axis, is

**Options:**

- **(A)** $-y\left(\frac{d y}{d x}\right)^2=2 x \frac{d y}{d x}-y$
- **(B)** $y\left(\frac{d y}{d x}\right)^2+2 x y \frac{d y}{d x}+y=0$
- **(C)** $y\left(\frac{d y}{d x}\right)^2+4 x \frac{d y}{d x}=4 x y$
- **(D)** $y\left(\frac{d y}{d x}\right)^2+y=2 x y \frac{d y}{d x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-y\left(\frac{d y}{d x}\right)^2=2 x \frac{d y}{d x}-y$**

**Detailed Solution:**

Equation of parabola is $y^2=4 a(x+a)$
$$
2 y \frac{d y}{d x}=4 a \Rightarrow a=\frac{y \frac{d y}{d x}}{2}
$$
Substituting value of ' $a$ ', we get
$$
\begin{aligned}
& y^2=4\left(\frac{y \frac{d y}{d x}}{2}\right)\left[x+\left(\frac{y \frac{d y}{d x}}{2}\right)\right]=\left(2 y \frac{d y}{d x}\right)\left(\frac{2 x+y \frac{d y}{d x}}{2}\right) \\
& 2 y^2=\left(2 y \frac{d y}{d x}\right)\left(2 x+y \frac{d y}{d x}\right)=4 x y \frac{d y}{d x}+2 y^2\left(\frac{d y}{d x}\right)^2 \\
& \therefore \quad y=2 x \frac{d y}{d x}+y\left(\frac{d y}{d x}\right)^2
\end{aligned}
$$

</details>

---

### Q41. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\log _{10} x+\log _x 10+\log _x x+\log _{10} 10$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{1}{x \log _e}+\frac{1}{x \log _{10} e}$
- **(B)** $\frac{1}{x \log _e 10}+\frac{\log _e 10}{x\left(\log _{10} e\right)^2}$
- **(C)** $\frac{1}{x \log _e10}+\frac{1}{x \log _{10} e}$
- **(D)** $\frac{1}{x \log _e 10}+\frac{\log _0 10}{x\left(\log _e x\right)^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{x \log _e 10}+\frac{\log _0 10}{x\left(\log _e x\right)^2}$**

**Detailed Solution:**

$\begin{aligned} & y=\frac{\log _e x}{\log _e 10}+\frac{\log _e 10}{\log _e x}+1+1 \\ & \therefore \frac{d y}{d x}=\left(\frac{1}{\log _e 10}\right)\left(\frac{1}{x}\right)+\left(\log _e 10\right)\left[\frac{-\frac{1}{x}}{\left(\log _e x\right)^2}\right] \\ & =\frac{1}{x \log _e 10}-\frac{\log _e 10}{x\left(\log _e x\right)^2}\end{aligned}$

</details>

---

### Q42. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of all parabolas having vertex at the origin and axis along positive $\mathrm{Y}$-axis is

**Options:**

- **(A)** $x^2 \frac{d y}{d x}-y=0$
- **(B)** $x \frac{d y}{d x}+2 y=0$
- **(C)** $x \frac{d y}{d x}+y=0$
- **(D)** $2 x \frac{d y}{d x}-y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 x \frac{d y}{d x}-y=0$**

**Detailed Solution:**

We have $y^2=4 a x$
$$
\begin{aligned}
& \therefore 2 y \frac{d y}{d x}=4 a \quad \Rightarrow a=\left(\frac{y}{2}\right) \frac{d y}{d x} \\
& \therefore y^2=4\left(\frac{y}{2}\right)\left(\frac{d y}{d x}\right) x \Rightarrow y^2=2 x y \frac{d y}{d x} \\
& \therefore 2 x \frac{d y}{d x}-y=0
\end{aligned}
$$

</details>

---

### Q43. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of all family of lines $y=m x+\frac{4}{m}$ obtained by eliminating the arbitrary constant $\mathrm{m}$ is

**Options:**

- **(A)** $y\left(\frac{d y}{d x}\right)=4$
- **(B)** $y\left(\frac{d y}{d x}\right)^2+y\left(\frac{d y}{d x}\right)+4=0$
- **(C)** $x\left(\frac{d y}{d x}\right)+4=0$
- **(D)** $x\left(\frac{d y}{d x}\right)^2-y\left(\frac{d y}{d x}\right)+4=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x\left(\frac{d y}{d x}\right)^2-y\left(\frac{d y}{d x}\right)+4=0$**

**Detailed Solution:**

$$
\begin{aligned}
& y=m x+\frac{4}{m} \\
& \therefore \frac{d y}{d x}=m
\end{aligned}
$$
Substituting value of $\mathrm{m}$ in equation (1), we get
$$
\begin{aligned}
& y=\left(\frac{d y}{d x}\right) x+\frac{4}{\left(\frac{d y}{d x}\right)} \\
& \therefore y\left(\frac{d y}{d x}\right)=\left(\frac{d y}{d x}\right)^2 x+4
\end{aligned}
$$

</details>

---

### Q44. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of the family of circles touching $y$-axis at the origin is

**Options:**

- **(A)** $x^2-y^2-2 x y \frac{d y}{d x}=0$
- **(B)** $x^2-y^2+2 x y \frac{d y}{d x}=0$
- **(C)** $x^2+y^2-2 x y \frac{d y}{d x}=0$
- **(D)** $x^2+y^2+2 x y \frac{d y}{d x}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2-y^2+2 x y \frac{d y}{d x}=0$**

**Detailed Solution:**

Since circles touch $\mathrm{Y}$ axis at origin, the centres of the circles lie on $\mathrm{X}$ axis.
Let centre be $(\mathrm{h}, 0)$ and radius $=\mathrm{h}$
$$
\therefore(\mathrm{x}-\mathrm{h})^2+(\mathrm{y}-0)^2=\mathrm{h}^2 \Rightarrow \mathrm{x}^2-2 \mathrm{hx}+\mathrm{y}^2=0
$$
Differentiating w.r.t. $\mathrm{x}$, we get
$$
2 x-2 h+2 y \frac{d y}{d x}=0 \quad \Rightarrow x+y \frac{d y}{d x}=h
$$
Substituting value of $h$ in eq. (1), we get
$$
\begin{aligned}
& x^2-2\left(x+y \frac{d y}{d x}\right) x+y^2=0 \\
& \therefore x^2-2 x^2-2 x y \frac{d y}{d x}+y^2=0 \quad \Rightarrow x^2-y^2+2 x y \frac{d y}{d x}=0
\end{aligned}
$$

</details>

---

### Q45. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of family of circles whose centre lie on $\mathrm{X}$-axis is

**Options:**

- **(A)** $\frac{d^2 y}{d x^2}+\left(\frac{d y}{d x}\right)^2+1=0$
- **(B)** $y\left(\frac{d^2 y}{d x^2}\right)+\left(\frac{d y}{d x}\right)^2+1=0$
- **(C)** $y\left(\frac{d^2 y}{d x^2}\right)-\left(\frac{d y}{d x}\right)^2-1=0$
- **(D)** $y\left(\frac{d^2 y}{d x^2}\right)+\left(\frac{d y}{d x}\right)^2-1=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $y\left(\frac{d^2 y}{d x^2}\right)+\left(\frac{d y}{d x}\right)^2+1=0$**

**Detailed Solution:**

Let $(h, 0)$ be the centre of the circle and ' $r$ ' be the radius.
$$
\therefore(\mathrm{x}-\mathrm{h})^2+(\mathrm{y}-0)^2=\mathrm{r}^2 \Rightarrow(\mathrm{x}-\mathrm{h})^2+\mathrm{y}^2=\mathrm{r}^2
$$
Differentiating w.r.t. $\mathrm{x}$, we get
$$
\therefore 2(\mathrm{x}-\mathrm{h})(1)+2 \mathrm{y} \frac{\mathrm{dy}}{\mathrm{dx}}=0 \quad \Rightarrow \mathrm{h}=\mathrm{x}+\mathrm{y} \frac{\mathrm{dy}}{\mathrm{dx}}
$$
Substituting value of ' $h$ ' in eq. (1), we get
$$
y^2\left(\frac{d y}{d x}\right)^2+y^2=r^2 \Rightarrow y^2\left[1+\left(\frac{d y}{d x}\right)^2\right]=r^2
$$


Differentiating w.r.t. $\mathrm{x}$, we get
$$
\begin{aligned}
& y^2\left(2 \frac{d y}{d x} \cdot \frac{d^2 y}{d x^2}\right)+\left[1+\left(\frac{d y}{d x}\right)^2\right] 2 y \frac{d y}{d x}=0 \\
& \therefore y \frac{d^2 y}{d x^2}+\left(\frac{d y}{d x}\right)^2+1=0
\end{aligned}
$$

</details>

---

### Q46. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of an ellipse whose major axis is twice its minor axis, is

**Options:**

- **(A)** $x+4 y \frac{d y}{d x}=0$
- **(B)** $x-4 y \frac{d y}{d x}=0$
- **(C)** $x+2 y \frac{d y}{d x}=0$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x+4 y \frac{d y}{d x}=0$**

**Detailed Solution:**

For the given ellipse, we have $\mathrm{a}=2 \mathrm{~b}$
$$
\therefore \therefore \frac{\mathrm{x}^2}{4 \mathrm{~b}^2}+\frac{\mathrm{y}^2}{\mathrm{~b}^2}=1 \Rightarrow \mathrm{x}^2+4 \mathrm{y}^2=4 \mathrm{~b}^2
$$
Differentiating both sides w.r.t., we get
$$
2 x+8 y \frac{d y}{d x}=0 \Rightarrow x+4 y \frac{d y}{d x}=0
$$

</details>

---

### Q47. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of all circles which pass through the origin and whose centre lie on $\mathrm{Y}$-axis is

**Options:**

- **(A)** $\left(x^2-y^2\right) \frac{d y}{d x}-2 x y=0$
- **(B)** $\left(x^2+y^2\right) \frac{d y}{d x}-2 x y=0$
- **(C)** $\left(x^2+y^2\right) \frac{d y}{d x}+2 x y=0$
- **(D)** $\left(x^2+y^2\right) \frac{d y}{d x}+2 x y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(x^2-y^2\right) \frac{d y}{d x}-2 x y=0$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/wjDA2Pib7aQ2TKX-19xpvxxZnCB2wL9uX55i20bP_t0.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/pOMplIwcuvYZh1r4NPV_FlTA5tt4OdSt_6LSi6ZPOUs.original.fullsize.png">

</details>

---

### Q48. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x=a \sin t-b$ cost
$y=a \operatorname{cost}+b \sin t$
then $y^{3} \frac{d^{2} y}{d x^{2}}+x^{2}+y^{2}=$

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** 1
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

(D)
We have, $x=a \sin t-b \cos t$ and $y=a \cos t+b \sin t$
$\begin{array}{l}
x^{2}+y^{2}=\left\{[a \sin t-b \cos t]^{2}+[a \cos t+b \sin t]^{2}\right\} \\
x^{2}+y^{2}=\left\{a^{2} \cdot \sin ^{2} t-2 a b \sin t \cdot \cos t+b^{2} \cos ^{2} t+a^{2} \cos ^{2} t+2 a b \sin t \cdot \cos t+b^{2} \sin ^{2} t\right\} \\
x^{2}+y^{2}=\left\{a^{2}\left(\sin ^{2} t+\cos ^{2} t\right)+b^{2}\left(\cos ^{2} t+\sin ^{2} t\right)\right\} \\
x^{2}+y^{2}=a^{2}+b^{2}
\end{array}$
Differentiate w.r.t. $x$, we get
$2 x+2 y \frac{d y}{d x}=0 \Rightarrow \frac{d y}{d x}=-\frac{x}{y}$...(1)
$\therefore \quad \mathrm{y} \frac{\mathrm{dy}}{\mathrm{dx}}=-\mathrm{x}$
Again differentiating w.r.t. x, we get
$y \frac{d^{2} y}{d x^{2}}+\left(\frac{d y}{d x}\right)^{2}=-1$
Substituting value of $\frac{d y}{d x}$ from (1), we get
$\begin{aligned}
& y \frac{d^{2} y}{d x^{2}}+\left(\frac{-x}{y}\right)^{2}=-1 \Rightarrow y \frac{d^{2} y}{d x^{2}}+\frac{x^{2}}{y^{2}}=-1 \\
\therefore & y^{3} \frac{d^{2} y}{d x^{2}}+x^{2}+y^{2}=0
\end{aligned}$

</details>

---

### Q49. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of the circles having their centres on the line $\mathrm{y}=8$ and touching the $\mathrm{X}$ -axis is

**Options:**

- **(A)** $(y-8)^{2}\left[1-\left(\frac{d y}{d x}\right)^{2}\right]=64$
- **(B)** $(y-8)^{2}\left[1+\left(\frac{d y}{d x}\right)^{2}\right]=64$
- **(C)** $(y-8)\left[1+\left(\frac{d y}{d x}\right)^{2}\right]=64$
- **(D)** $y^{2}\left(1+\frac{d y}{d x}\right)=64$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(y-8)^{2}\left[1+\left(\frac{d y}{d x}\right)^{2}\right]=64$**

**Detailed Solution:**

(B)
Let $(\mathrm{h}, 8)$ be the centre of the circle.
Since circle touches $X$ axis, radius $=8$
$\therefore(x-h)^{2}+(y-8)^{2}=(8)^{2}$...(1)
Differentiating w.r.t. x, we get
$\begin{aligned}
& 2(x-h)+2(y-8) \frac{d y}{d x}=0 \\
\therefore \quad &(x-h)=-(y-8) \frac{d y}{d x}
\end{aligned}$
Substituting value of $(x-h)$ in eq. (1), we get
$\begin{aligned}
&\left[-(y-8) \frac{d y}{d x}\right]^{2}+(y-8)^{2}=64 \\
\therefore &(y-8)^{2}\left[\left(\frac{d y}{d x}\right)^{2}+1\right]=64
\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Io1Q5Si0vaUKh0q2Vp61JHSAO0Nuazg1hFtK9jBQkjw.original.fullsize.png">

</details>

---

### Q50. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation obtained from the function $y=a(x-a)^{2}$ is

**Options:**

- **(A)** $8 y^{2}=\left(\frac{d y}{d x}\right)^{2}\left[x-\frac{1}{4 y}\left(\frac{d y}{d x}\right)^{2}\right]^{2}$
- **(B)** $8 y^{2}=\left(\frac{d y}{d x}\right)^{2}\left[x+\frac{1}{4 y}\left(\frac{d y}{d x}\right)^{2}\right]^{2}$
- **(C)** $2 y^{2}=\left(\frac{d y}{d x}\right)^{2}\left[x-\frac{1}{4 y}\left(\frac{d y}{d x}\right)^{2}\right]^{2}$
- **(D)** $4 y^{2}=\left(\frac{d y}{d x}\right)^{2}\left[x-\frac{1}{4 y}\left(\frac{d y}{d x}\right)^{2}\right]^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4 y^{2}=\left(\frac{d y}{d x}\right)^{2}\left[x-\frac{1}{4 y}\left(\frac{d y}{d x}\right)^{2}\right]^{2}$**

**Detailed Solution:**

(B)
$\begin{aligned}
y &=a(x-a)^{2}...(1) \\
\therefore \frac{d y}{d x} &=2 a(x-a)...(2)
\end{aligned}$
Eq. $(2)+\mathrm{cq} \cdot(1)$ gives
$\frac{\left(\frac{d y}{d x}\right)}{y}=\frac{2 a(x-a)}{a(x-a)^{2}} \quad \Rightarrow(x-a)=\frac{2 y}{\left(\frac{d y}{d x}\right)} \text { and } a=x-\frac{2 y}{\left(\frac{d y}{d x}\right)}$
Substituting these values of $a$ and $(x-a)$ in eq. (1), we get
$\begin{aligned}
y &=\left[x-\frac{2 y}{\left(\frac{d y}{d x}\right)}\right]\left[\frac{2 y}{\left(\frac{d y}{d x}\right)}\right]^{2} \\
&=\left[\frac{x\left(\frac{d y}{d x}\right)-2 y}{\left(\frac{d y}{d x}\right)}\right]\left[\frac{4 y^{2}}{\left(\frac{d y}{d x}\right)^{2}}\right] \\
\therefore & \frac{(y)\left(\frac{d y}{d x}\right)^{3}}{x\left(\frac{d y}{d x}-2 y\right)}=4 y^{2}
\end{aligned}$

</details>

---

### Q51. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of the family of curves $\mathrm{y}=e^{x}(\mathrm{~A} \cos x+\mathrm{B} \sin x)$, where
$\mathrm{A}$ and $\mathrm{B}$ are arbitrary constants is

**Options:**

- **(A)** $\frac{\mathrm{d}^{2} \mathrm{y}}{\mathrm{d} x^{2}}+2\left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)+2 \mathrm{y}=0$
- **(B)** $\frac{\mathrm{d}^{2} \mathrm{y}}{\mathrm{d} x^{2}}-2\left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)-2 \mathrm{y}=0$
- **(C)** $\frac{\mathrm{d}^{2} \mathrm{y}}{\mathrm{d} x^{2}}+2\left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)-2 \mathrm{y}=0$
- **(D)** $\frac{\mathrm{d}^{2} \mathrm{y}}{\mathrm{d} x^{2}}-2\left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)+2 \mathrm{y}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mathrm{d}^{2} \mathrm{y}}{\mathrm{d} x^{2}}-2\left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)+2 \mathrm{y}=0$**

**Detailed Solution:**

Given $y=e^{x}(A \cos x+B \sin x)$...(1)
$$
\begin{aligned} \frac{d y}{d x} &=e^{x}(-A \sin x+B \cos x)+e^{x}(A \cos x+B \sin x) \\ \frac{d^{2} y}{d x^{2}} &=e^{x}(-A \cos x-B \sin x)+e^{x}(-A \sin x+B \cos x)+e^{x}(-A \sin x+B \cos x) \\ &-e^{x}(A \cos x+B \sin x) \\ &=2 e^{x}(-A \sin x+B \cos x) \end{aligned}
$$
Thus we get
$$
\begin{aligned} y &=e^{x}(A \cos x+B \sin x) \\ \frac{d y}{d x} &=e^{x}(-A \sin x+A \cos x+B \cos x+B \sin x) \end{aligned}
$$
$\begin{aligned} & \frac{d^{2} y}{d x^{2}}=e^{x}(-2 A \sin x+2 B \cos x) \\ \therefore & \frac{d^{2} y}{d x^{2}}-\frac{2 d y}{d x}+2 y \\ &=e^{x}[-2 A \sin x+2 B \cos x+2 A \sin x-2 A \cos x-2 B \cos x-2 B \sin x+2 A \cos x+2 B \sin x] \\ &=0 \end{aligned}$

</details>

---

### Q52. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The particular solution of the differential equation $\cos \left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)=a$, under the conditions $\mathrm{a} \epsilon \mathrm{R}$ and $y(0)=2$ is

**Options:**

- **(A)** $\cos \left(\frac{x-2}{y-2}\right)=a$
- **(B)** $\cos ^{-1}\left(\frac{y-2}{x}\right)=a$
- **(C)** $\cos \left(\frac{y-2}{x}\right)=a$
- **(D)** $\cos \left(\frac{x-2}{y+2}\right)=a$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\cos \left(\frac{y-2}{x}\right)=a$**

**Detailed Solution:**

$\begin{aligned} & \cos \left(\frac{d y}{d x}\right)=a \Rightarrow \frac{d y}{d x}=\cos ^{-1} a \\ & \int d y=\int \cos ^{-1} a d x \\ \therefore & y=x \cos ^{-1} a+c ....(1)\\ & \text { We have } x=0, y=2 \\ \therefore \quad & 2=0+c \Rightarrow c=2 \\ \therefore \quad & y=x \cos ^{-1} a+2 \\ \therefore & y-2=x \cos ^{-1} a \Rightarrow \frac{y-2}{x}=\cos ^{-1} a \Rightarrow \cos \left(\frac{y-2}{x}\right)=a \end{aligned}$

</details>

---

### Q53. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$$If \frac{x}{x-y}=\log \left(\frac{a}{x-y}\right), \text { then } \frac{d y}{d x}=$$

**Options:**

- **(A)** $2+\frac{1}{y}$
- **(B)** $\frac{2 y-x}{y}$
- **(C)** $\frac{2 x-y}{x}$
- **(D)** $\frac{x-2 y}{y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2 y-x}{y}$**

**Detailed Solution:**

$\frac{x}{x-y}=\log a-\log (x-y)$
$\therefore \log (x-y)+\frac{x}{x-y}=\log a$
$\therefore \frac{1}{(x-y)}\left(1-\frac{d y}{d x}\right)+\left[\frac{(x-y)(1)-(x)\left(1-\frac{d y}{d x}\right)}{x-y}\right]=0$
$\therefore\left[\frac{1}{x-y}-\frac{1}{x-y} \frac{d y}{d x}\right]+\left[\frac{x-y-x+x \frac{d y}{d x}}{x-y}\right]=0$
$\therefore \frac{1}{x-y}-\frac{1}{x-y} \frac{d y}{d x}-\frac{y}{(x-y)^{2}}+\frac{x}{(x-y)^{2}}=0$
$\therefore \quad(x-y)-(x-y) \frac{d y}{d x}-y+x \frac{d y}{d x}=0$
$\therefore \frac{d y}{d x}=\frac{x-2 y}{-y}=\frac{2 y-x}{y}$

</details>

---

### Q54. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$y=m x+\frac{2}{m}$ is the general solution of

**Options:**

- **(A)** $y\left(\frac{d y}{d x}\right)^{2}=x\left(\frac{d y}{d x}\right)+2$
- **(B)** $y=x \frac{d y}{d x}+2$
- **(C)** $y\left(\frac{d y}{d x}\right)=x\left(\frac{d y}{d x}\right)^{2}+2$
- **(D)** $y\left(\frac{d y}{d x}\right)=x+2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y\left(\frac{d y}{d x}\right)=x\left(\frac{d y}{d x}\right)^{2}+2$**

**Detailed Solution:**

$$
\begin{array}{l}
\text { Given } \mathrm{y}=\mathrm{m} \mathrm{x}+\frac{2}{\mathrm{~m}}....(1) \\
\therefore \frac{\mathrm{d} \mathrm{y}}{\mathrm{dx}}=(\mathrm{m} \times 1)+0 \Rightarrow \mathrm{m}=\frac{\mathrm{dy}}{\mathrm{dx}}
\end{array}
$$
Putting value of $m$ in equation (1), we get
$$
y=x \frac{d y}{d x}+\frac{2}{\left(\frac{d y}{d x}\right)} \Rightarrow y \frac{d y}{d x}=x\left(\frac{d y}{d x}\right)^{2}+2
$$

</details>

---

### Q55. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\tan ^{-1} x+\tan ^{-1} y=c$ is the general solution of the differential equation

**Options:**

- **(A)** $\frac{d y}{d x}=-\left(\frac{1+y^{2}}{1+x^{2}}\right)$
- **(B)** $\frac{d y}{d x}=\left(\frac{1+y^{2}}{1+x^{2}}\right)$
- **(C)** $\frac{d y}{d x}=-\left(\frac{1+x^{2}}{1+y^{2}}\right)$
- **(D)** $\frac{d y}{d x}=\left(\frac{1+x^{2}}{1+y^{2}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{d y}{d x}=-\left(\frac{1+y^{2}}{1+x^{2}}\right)$**

**Detailed Solution:**

Given $\tan ^{-1} x+\tan ^{-1} y=c$
$\therefore \frac{1}{1+x^{2}}+\frac{1}{1+y^{2}} \frac{d y}{d x}=0$
$\frac{1}{1+y^{2}} \frac{d y}{d x}=-\frac{1}{1+x^{2}} \quad \Rightarrow \frac{d y}{d x}=-\left(\frac{1+y^{2}}{1+x^{2}}\right)$

</details>

---

### Q56. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The differential equation of the family of lines having $x$ - intercept ' $\mathrm{a}$ ' and
$y$ - intercept ' $\mathrm{b}$ ' is

**Options:**

- **(A)** $\frac{d^{2} y}{d x^{2}}=-1$
- **(B)** $\frac{d^{2} y}{d x^{2}}=10$
- **(C)** $\frac{d^{2} y}{d x^{2}}=1$
- **(D)** $\frac{d^{2} y}{d x^{2}}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{d^{2} y}{d x^{2}}=0$**

**Detailed Solution:**

Equation of line having $x-$ intercept $a$ and $y$ intercept $b$ is $\frac{x}{a}+\frac{y}{b}=1$ i.e. $b x+a y=a b$ Differentiating w.r.t. x, we get
$\mathrm{b}+\mathrm{a} \frac{\mathrm{dy}}{\mathrm{dx}}=0 \Rightarrow \mathrm{a} \frac{\mathrm{dy}}{\mathrm{dx}}=-\mathrm{b} \Rightarrow \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{-\mathrm{b}}{\mathrm{a}}$
Again differentiating w.r.t. $\mathrm{x}$, we get 
$\frac{d^{2} y}{d x^{2}}=0$

</details>

---

### Q57. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation obtained by eliminating the arbitrary constants from the
equation $y^{2}=(2 x+c)^{5}$ is

**Options:**

- **(A)** $\left(\frac{d y}{d x}\right)^{4}-625 y^{4}=0$
- **(B)** $\left(\frac{d y}{d x}\right)^{5}-3125 y^{3}=0$
- **(C)** $\left(\frac{d y}{d x}\right)^{3}-125 y^{3}=0$
- **(D)** $x y \frac{d y}{d x}=5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\frac{d y}{d x}\right)^{5}-3125 y^{3}=0$**

**Detailed Solution:**

We have $y^{2}=(2 x+c)^{5}$ ...(i)
$\therefore 2 \mathrm{y} \frac{\mathrm{dy}}{\mathrm{dx}}=5(2 \mathrm{x}+\mathrm{c})^{4}(2) \Rightarrow \mathrm{y} \frac{\mathrm{dy}}{\mathrm{dx}}=5(2 \mathrm{x}+\mathrm{c})^{4}$
$\therefore(2 x+c)=\left[\frac{y}{5}\left(\frac{d y}{d x}\right)\right]^{\frac{1}{4}}$ and substituting value of $(2 x+c)$ in eq. (i), we write
$y^{2}=\left[\frac{y}{5}\left(\frac{d y}{d x}\right)\right]^{\frac{5}{4}}$
Raising both sides to power of 4 , we get
$\begin{aligned}
& y^{8}=\left[\frac{y}{5}\left(\frac{d y}{d x}\right)\right]^{5}=\frac{y^{5}}{3125}\left(\frac{d y}{d x}\right)^{5} \\
\therefore & 3125 y^{3}=\left(\frac{d y}{d x}\right)^{5}
\end{aligned}$

</details>

---

### Q58. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation whose solution is $y=e^{a x}$ is

**Options:**

- **(A)** $y \frac{d y}{d x}=x \log y$
- **(B)** $\frac{d y}{d x}=x \log x$
- **(C)** $\frac{d y}{d x}=y \log x$
- **(D)** $x \frac{d y}{d x}=y \log y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x \frac{d y}{d x}=y \log y$**

**Detailed Solution:**

Given $y=e^{a x}$
Taking log on both sides, we get
$\therefore \frac{\log y}{y}=\log e^{a x} \Rightarrow \log y=\operatorname{axlog} e \Rightarrow \log y=a x$ ...(1)
$\therefore \frac{1}{y} \frac{d y}{d x}=a$
Substituting value of ' $a$ ' in equation (1), we get
$\log y=\left[\left(\frac{1}{y}\right) \frac{d y}{d x}\right] x \Rightarrow x \frac{d y}{d x}=y \log y$

</details>

---

### Q59. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation of all circles having centre at <math><mi>A</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mi></mi><mn>2</mn></mrow></mfenced></math> is ________

**Options:**

- **(A)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>
- **(B)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>
- **(C)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

Equation of circle is <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mi>y</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>  
Whose centre is <math><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mi></mi><mn>2</mn></mrow></mfenced></math>

</details>

---

### Q60. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>y</mi><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math> then <math><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mn>2</mn><mi>x</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi> </mi></math>

**Options:**

- **(A)** <math > <mn>4</mn></math>
- **(B)** <math > <mn>2</mn></math>
- **(C)** <math > <mn>1</mn></math>
- **(D)** <math > <mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math > <mn>2</mn></math>**

**Detailed Solution:**

<math> <mrow> <mi>y</mi><mo>=</mo><msup> <mrow> <mrow><mo>(</mo> <mrow> <msup> <mrow> <mi>tan</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mi>x</mi></mrow> <mo>)</mo></mrow></mrow> <mn>2</mn> </msup> </mrow> </math>
<math> <mrow> <mfrac> <mrow> <mi>d</mi><mi>y</mi></mrow> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> <mo>=</mo><mfrac> <mrow> <mn>2</mn><msup> <mrow> <mi>tan</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow></mrow> <mrow> <mrow><mo>(</mo> <mrow> <mn>1</mn><mo>+</mo><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> <mo>)</mo></mrow></mrow> </mfrac> </mrow> </math>
<math> <mrow> <mrow><mo>(</mo> <mrow> <mn>1</mn><mo>+</mo><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> <mo>)</mo></mrow><mfrac> <mrow> <mi>d</mi><mi>y</mi></mrow> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> <mo>=</mo><mn>2</mn><msup> <mrow> <mi>tan</mi></mrow> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow></mrow> </math>
<math> <mrow> <mrow><mo>(</mo> <mrow> <mn>1</mn><mo>+</mo><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> <mo>)</mo></mrow><mfrac> <mrow> <msup> <mi>d</mi> <mn>2</mn> </msup> <mi>y</mi></mrow> <mrow> <mi>d</mi><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> <mo>+</mo><mfrac> <mrow> <mi>d</mi><mi>y</mi></mrow> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> <mrow><mo>(</mo> <mrow> <mn>2</mn><mi>x</mi></mrow> <mo>)</mo></mrow><mo>=</mo><mfrac> <mn>2</mn> <mrow> <mn>1</mn><mo>+</mo><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <msup> <mrow> <mrow><mo>(</mo> <mrow> <mn>1</mn><mo>+</mo><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> <mo>)</mo></mrow></mrow> <mn>2</mn> </msup> <mfrac> <mrow> <msup> <mi>d</mi> <mn>2</mn> </msup> <mi>y</mi></mrow> <mrow> <mi>d</mi><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> <mo>+</mo><mn>2</mn><mi>x</mi><mrow><mo>(</mo> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>+</mo><mn>1</mn></mrow> <mo>)</mo></mrow><mfrac> <mrow> <mi>d</mi><mi>y</mi></mrow> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> <mo>=</mo><mn>2</mn></mrow> </math>

</details>

---

### Q61. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of all parabolas whose axis is <math><mi>y</mi><mo>-</mo><mi mathvariant="normal">a</mi><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi></math> is

**Options:**

- **(A)** <math><mi>x</mi><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>
- **(B)** <math><mi>x</mi><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mi> </mi><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math><mi> </mi><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi>x</mi><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

Axis = <math><mi>y</mi></math> axis
Vertex is (0, k)
Equation of parabola is
<math><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>0</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><mi>a</mi><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mi>k</mi></mrow></mfenced></math>
<math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi>y</mi><mo>-</mo><mn>4</mn><mi>a</mi><mi>k</mi></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/qmlyyyxtlmfyakacsljnkirdmrjfsoxygzhtxmhisvaogfxcch.jpeg" />
Differentiate w.r.t x,
<math><mn>2</mn><mi>x</mi><mo>=</mo><mn>4</mn><mi>a</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>
<math>   <mo>&#x21D2;</mo>  </math><math><mi>x</mi><mo>=</mo><mn>2</mn><mi>a</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>
Differentiate w.r.t x,
<math><mfrac><mrow><mi>d</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>⋅</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>d</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac></mrow></mfenced></math>
<math>   <mo>&#x21D2;</mo>  </math><math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>⋅</mo><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math>   <mo>&#x21D2;</mo>  </math><math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi>x</mi><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>

</details>

---

### Q62. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of the family of circles touching y-axis at the origin is

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>0</mn><mi> </mi></math>
- **(B)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>0</mn></math>
- **(D)** <math><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

As required circle touches y - axis at the origin.
 <math><mo>∴</mo><mi> </mi><mi> </mi></math> Let Center of the circle is  <math><mi>d</mi><mo>(</mo><mi>a</mi><mo>,</mo><mn>0</mn><mo>)</mo></math>  and radius is a
 <math><mo>∴</mo><mi> </mi></math>  Equation of circle will be,
 <math><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>a</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>0</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></math> 
 <math><mo>⇒</mo><mi> </mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>a</mi><mi>x</mi><mo>+</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></math> 
 <math><mo>⇒</mo><mi> </mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>a</mi><mi>x</mi><mo>=</mo><mn>0</mn></math>              .... (i)
By differentiating above equation w.r.t x, we get
 <math><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><mi>a</mi><mo>=</mo><mn>0</mn></math> 
 <math><mo>∴</mo><mi> </mi><mn>2</mn><mi>a</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>              .... (ii)
From (i) and (ii),
 <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mo>+</mo><mi> </mi><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mi>x</mi><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><mi> </mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>

</details>

---

### Q63. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `2`

The differential equation whose solution is $(x-h)^{2}+(y-k)^{2}=a^{2}(a$ is a constant $)$, is

**Options:**

- **(A)** $\left[1+\left(\frac{d y}{d x}\right)^{2}\right]^{3}=a^{2} \frac{d^{2} y}{d x^{2}}$
- **(B)** $\left[1+\left(\frac{d y}{d x}\right)^{2}\right]^{3}=a^{2}\left(\frac{d^{2} y}{d x^{2}}\right)^{2}$
- **(C)** $\left[1+\left(\frac{d y}{d x}\right)\right]^{3}=a^{2}\left(\frac{d^{2} y}{d x^{2}}\right)^{2}$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[1+\left(\frac{d y}{d x}\right)^{2}\right]^{3}=a^{2}\left(\frac{d^{2} y}{d x^{2}}\right)^{2}$**

**Detailed Solution:**

Given, $(x-h)^{2}+(y-k)^{2}=a^{2} \quad$...(i)
$$
\begin{array}{lr}
\Rightarrow & 2(x-h)+2(y-k) \frac{d y}{d x}=0 \\
\Rightarrow & \quad(x-h)+(y-k) \frac{d y}{d x}=0
\end{array}
$$
Again differentiating
$$
(y-k)=-\frac{1+\left(\frac{d y}{d x}\right)^{2}}{d^{2} y / d x^{2}}
$$
Putting in Eq. (ii), we get
$$
\begin{array}{l}
x-h=-(y-k) \frac{d y}{d x} \\
=\frac{\left[1+\left(\frac{d y}{d x}\right)^{2}\right] \frac{d y}{d x}}{\frac{d^{2} y}{d x^{2}}}
\end{array}
$$
Putting in Eq. (i), we get
$$
\begin{array}{l}
\frac{\left[1+\left(\frac{d y}{d x}\right)^{2}\right]^{2}\left(\frac{d y}{d x}\right)^{2}}{\left(\frac{d^{2} y}{d x^{2}}\right)^{2}} \\
\Rightarrow \quad\left[1+\left(\frac{d y}{d x}\right)^{2}\right]^{2}\left[\left(\frac{d y}{d x}\right)^{2}+1\right]=a^{2}\left(\frac{d^{2} y}{d x^{2}}\right)^{2} \\
+\frac{\left[1+\left(\frac{d y}{d x}\right)^{2}\right]^{2}}{\left(\frac{d^{2} y}{d x^{2}}\right)^{2}}=a^{2} \\
\Rightarrow\left[1+\left(\frac{d y}{d x}\right)^{2}\right]^{3}=a^{2}\left(\frac{d^{2} y}{d x^{2}}\right)^{2}
\end{array}
$$

</details>

---

### Q64. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of all circles which pass through the origin and whose centres lie on $y$ -axis is

**Options:**

- **(A)** $\left(x^{2}-y^{2}\right) \frac{d y}{d x}-2 x y=0$
- **(B)** $\left(x^{2}-y^{2}\right) \frac{d y}{d x}+2 x y=0$
- **(C)** $\left(x^{2}-y^{2}\right) \frac{d y}{d x}-x y=0$
- **(D)** $\left(x^{2}-y^{2}\right) \frac{d y}{d x}+x y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(x^{2}-y^{2}\right) \frac{d y}{d x}-2 x y=0$**

**Detailed Solution:**

Equation of a circle is
$$
\begin{array}{r}
x^{2}+(y-a)^{2}=a^{2} \\
2 x+2 y \frac{d y}{d x}-2 a \frac{d y}{d x}=0
\end{array}
$$
Form Eqs. (i) and (ii)
$$
\begin{aligned}
\frac{d y}{d x} &=\frac{2 x y}{x^{2}-y^{2}} \\
\Rightarrow \quad\left(x^{2}-y^{2}\right) \frac{d y}{d x}-2 x y &=0
\end{aligned}
$$

</details>

---

### Q65. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of family of circles whose centre lies on $x$ -axis, is

**Options:**

- **(A)** $\frac{d^{2} y}{d x^{2}}+\left(\frac{d y}{d x}\right)^{2}+1=0$
- **(B)** $y \frac{d^{2} y}{d x^{2}}+\left(\frac{d y}{d x}\right)^{2}-1=0$
- **(C)** $y \frac{d^{2} y}{d x^{2}}-\left(\frac{d y}{d x}\right)^{2}-1=0$
- **(D)** $y \frac{d^{2} y}{d x^{2}}+\left(\frac{d y}{d x}\right)^{2}+1=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y \frac{d^{2} y}{d x^{2}}+\left(\frac{d y}{d x}\right)^{2}+1=0$**

**Detailed Solution:**

The equation of family of circle having centre at $x$ -axis is $x^{2}+y^{2}-2 a x=0$.
On differentiating, we get
$$
2 x+2 y \frac{d y}{d x}-2 a=0
$$
Again, differentiating, we get
$$
\begin{aligned}
& 2+2\left[y \frac{d^{2} y}{d x^{2}}+\left(\frac{d y}{d x}\right)^{2}\right]=0 \\
\Rightarrow \quad & y \frac{d^{2} y}{d x^{2}}+\left(\frac{d y}{d x}\right)^{2}+1=0
\end{aligned}
$$

</details>

---

### Q66. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `2`

Form the differential equation of all family of lines $y=m x+\frac{4}{m}$ by eliminating the arbitrary constant ' $m^{\prime}$ ' is

**Options:**

- **(A)** $\frac{d^{2} y}{d x^{2}}=0$
- **(B)** $x\left(\frac{d y}{d x}\right)^{2}-y \frac{d y}{d x}+4=0$
- **(C)** $x\left(\frac{d y}{d x}\right)^{2}+y \frac{d y}{d x}+4=0$
- **(D)** $\frac{d y}{d x}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x\left(\frac{d y}{d x}\right)^{2}-y \frac{d y}{d x}+4=0$**

**Detailed Solution:**

$y=m x+\frac{4}{m}$
$\therefore \quad \frac{d y}{d x}=m$
From Eq. (i), we get
$$
\begin{aligned}
y &=x\left(\frac{d y}{d x}\right)+\frac{4}{(d y / d x)} \\
\Rightarrow & y\left(\frac{d y}{d x}\right)=x\left(\frac{d y}{d x}\right)^{2}+4 \\
\Rightarrow & x\left(\frac{d y}{d x}\right)^{2}-y \frac{d y}{d x}+4=0
\end{aligned}
$$
Which is the required differential equation.

</details>

---

### Q67. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of all parabolas with axis parallel to the axis of $y$ is

**Options:**

- **(A)** $y_{2}=2 y_{1}+x$
- **(B)** $y_{3}=2 y_{1}$
- **(C)** $y_{2}^{3}=y_{1}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) None of these**

**Detailed Solution:**

The equation of the family of parabolas with axis parallel to axis of $y$ is
$$
(x-a)^{2}=A(y-b)
$$
On differentiating w.r.t. $x$, we get $2(x-a)=A y_{1}$
Again differentiating w.r.t. $x$, we get
$$
2=A y_{2}
$$
On again differentiating w.r.t. $x$, we get
$$
\begin{array}{l}
\qquad \begin{array}{c}
y_{3}=0 \\

</details>

---

