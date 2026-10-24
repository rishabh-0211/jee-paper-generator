# MHT CET Mathematics - Application of Derivatives

## Topic 2: Rate Measure Error and Approximation

**Total Questions:** 119

---

### Q1. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A student learned 100 Math formulae for an examination. The number of formulae the student can remember in '$t$' days after learning is given by $f(t) = 100(1 - 0.1t)^2$. Then, the magnitude of the rate at which the student forgets the formula 3 days after learning is:

**Options:**

- **(A)** $-14$
- **(B)** $16$
- **(C)** $14$
- **(D)** $10$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $14$**

**Detailed Solution:**

Given $f(t) = 100(1 - 0.1t)^2$

Differentiating with respect to $t$:

$f'(t) = \dfrac{d}{dt} [100(1 - 0.1t)^2]$

$f'(t) = 100 \times 2(1 - 0.1t) \times (-0.1)$

$f'(t) = -20(1 - 0.1t)$

At $t = 3$ days:

$f'(3) = -20(1 - 0.1 \times 3)$

$f'(3) = -20(1 - 0.3) = -20(0.7) = -14$

The rate of change of remembered formulae is $-14$.

The magnitude of the rate at which the student forgets the formulae is $|-14| = 14$.

Answer: $14$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A right circular cone is melting such that its volume is decreasing at the rate of $12\pi$ $\text{cm}^3/\text{sec}$. The radius of the base is always equal to half of its height. Then the rate of change of the radius when the radius is $2$ cm is:

**Options:**

- **(A)** radius is increasing at the rate of $1$ cm/sec
- **(B)** radius is decreasing at the rate of $1$ cm/sec
- **(C)** radius is increasing at the rate of $1.5$ cm/sec
- **(D)** radius is decreasing at the rate of $1.5$ cm/sec

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) radius is decreasing at the rate of $1.5$ cm/sec**

**Detailed Solution:**

Let $V$ be the volume, $r$ be the radius, and $h$ be the height of the cone.

Given $\dfrac{dV}{dt} = -12\pi$ cm$^3$/sec and $r = \dfrac{h}{2} \Rightarrow h = 2r$.

The volume of the cone is $V = \dfrac{1}{3}\pi r^2 h$.

Substituting $h = 2r$, we get:

$V = \dfrac{1}{3}\pi r^2 (2r) = \dfrac{2}{3}\pi r^3$

Differentiating with respect to time $t$:

$\dfrac{dV}{dt} = \dfrac{2}{3}\pi (3r^2) \dfrac{dr}{dt} = 2\pi r^2 \dfrac{dr}{dt}$

Substitute $\dfrac{dV}{dt} = -12\pi$ and $r = 2$:

$-12\pi = 2\pi (2)^2 \dfrac{dr}{dt}$

$-12\pi = 8\pi \dfrac{dr}{dt}$

$\dfrac{dr}{dt} = -1.5$ cm/sec

Thus, the radius is decreasing at the rate of $1.5$ cm/sec.

Answer: radius is decreasing at the rate of $1.5$ cm/sec

</details>

---

### Q3. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A man of height $1.2$ m is moving away from the lamp post at the rate $0.6$ m/sec. If the height of the lamp post is $4.8$ m, then the rate at which the shadow of the man is lengthening is:

**Options:**

- **(A)** $0.02\ \text{m/s}$
- **(B)** $1.8\ \text{m/s}$
- **(C)** $0.2\ \text{m/s}$
- **(D)** $2.0\ \text{m/s}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.2\ \text{m/s}$**

**Detailed Solution:**

Let $x$ be the distance of the man from the lamp post and $y$ be the length of his shadow.

Using similar triangles formed by the lamp post, the man, and the shadow:

$\dfrac{y}{1.2} = \dfrac{x+y}{4.8}$

$4.8y = 1.2(x+y)$

$4y = x+y$

$3y = x$

Differentiating with respect to time $t$:

$3\dfrac{dy}{dt} = \dfrac{dx}{dt}$

Given that the man is moving away from the lamp post at $0.6$ m/s, we have $\dfrac{dx}{dt} = 0.6$ m/s.

$3\dfrac{dy}{dt} = 0.6$

$\dfrac{dy}{dt} = 0.2$ m/s

The rate at which the shadow is lengthening is $0.2$ m/s.

Answer: $0.2\ \text{m/s}$

</details>

---

### Q4. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The approximate surface area of a sphere of radius $2.01$ cm is

**Options:**

- **(A)** $16.16\pi\ \text{cm}^2$
- **(B)** $16.15\pi\ \text{cm}^2$
- **(C)** $16.14\pi\ \text{cm}^2$
- **(D)** $16.17\pi\ \text{cm}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $16.16\pi\ \text{cm}^2$**

**Detailed Solution:**

The surface area of a sphere of radius $r$ is given by $S = 4\pi r^2$.

Let $r = 2$ and $\Delta r = 0.01$.

Differentiating $S$ with respect to $r$, we get:

$\dfrac{dS}{dr} = 8\pi r$

The approximate change in surface area is given by $dS = \left(\dfrac{dS}{dr}\right) \Delta r$.

At $r = 2$ and $\Delta r = 0.01$:

$dS = 8\pi (2) (0.01) = 0.16\pi$

The approximate surface area is $S(r + \Delta r) \approx S(r) + dS$.

$S(2) = 4\pi (2)^2 = 16\pi$

$S(2.01) \approx 16\pi + 0.16\pi = 16.16\pi\ \text{cm}^2$

Answer: $16.16\pi\ \text{cm}^2$

</details>

---

### Q5. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A stone is dropped into a quiet lake and waves move in circles at the speed of $7$ cm s$^{-1}$. At the instant when the radius of circular wave is $5$ cm, the enclosed area is increasing at the rate -------- cm$^2$ s$^{-1}$

**Options:**

- **(A)** $50\pi$
- **(B)** $60\pi$
- **(C)** $25\pi$
- **(D)** $70\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $70\pi$**

**Detailed Solution:**

Let $r$ be the radius of the circular wave and $A$ be the enclosed area.

Given that the waves move in circles at the speed of $7$ cm s$^{-1}$, we have $\dfrac{dr}{dt} = 7$ cm s$^{-1}$.

The area of the circle is given by $A = \pi r^2$.

Differentiating with respect to time $t$, we get:

$\dfrac{dA}{dt} = 2\pi r \dfrac{dr}{dt}$

Substituting $r = 5$ cm and $\dfrac{dr}{dt} = 7$ cm s$^{-1}$:

$\dfrac{dA}{dt} = 2\pi (5)(7) = 70\pi$ cm$^2$ s$^{-1}$

Answer: $70\pi$

</details>

---

### Q6. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A water tank in the house of an inverted cone is being emptied at the rate of $2$ cubic feet per second. The height of the cone is $8$ feet and the radius is $4$ feet, then the rate of change of the water level when the depth is $6$ feet.

**Options:**

- **(A)** $\dfrac{2}{9\pi} ft/sec$
- **(B)** $\dfrac{4}{9\pi} ft/sec$
- **(C)** $\dfrac{8}{9\pi} ft/sec$
- **(D)** $\dfrac{10}{9\pi} ft/sec$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2}{9\pi} ft/sec$**

**Detailed Solution:**

Let $r$ be the radius and $h$ be the height of the water level at any time $t$.

From similar triangles, $\dfrac{r}{h} = \dfrac{4}{8} \Rightarrow r = \dfrac{h}{2}$

The volume of water in the cone is $V = \dfrac{1}{3}\pi r^2 h$

Substituting $r = \dfrac{h}{2}$, we get $V = \dfrac{1}{3}\pi \left(\dfrac{h}{2}\right)^2 h = \dfrac{\pi h^3}{12}$

Differentiating with respect to $t$, we get $\dfrac{dV}{dt} = \dfrac{\pi}{12} (3h^2) \dfrac{dh}{dt} = \dfrac{\pi h^2}{4} \dfrac{dh}{dt}$

Given that the tank is being emptied at the rate of $2$ cubic feet per second, the magnitude of the rate of change of volume is $\dfrac{dV}{dt} = 2$

Substituting $h = 6$ and $\dfrac{dV}{dt} = 2$, we get $2 = \dfrac{\pi (6)^2}{4} \dfrac{dh}{dt}$

$2 = 9\pi \dfrac{dh}{dt}$

$\dfrac{dh}{dt} = \dfrac{2}{9\pi}$ ft/sec

Answer: $\dfrac{2}{9\pi} ft/sec$

</details>

---

### Q7. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The approximate value of $\sin^{-1}(0.51)$ is .......
[Given $\pi = 3.1416$, $\dfrac{2}{\sqrt{3}} = 1.1547$]

**Options:**

- **(A)** $0.535247$
- **(B)** $0.535547$
- **(C)** $0.535347$
- **(D)** $0.535147$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.535147$**

**Detailed Solution:**

Let $f(x) = \sin^{-1}(x)$.

Using the first-order approximation, $f(x + \Delta x) \approx f(x) + f'(x) \Delta x$.

Let $x = 0.5$ and $\Delta x = 0.01$.

$f(0.5) = \sin^{-1}(0.5) = \dfrac{\pi}{6}$

$f'(x) = \dfrac{1}{\sqrt{1 - x^2}}$

$f'(0.5) = \dfrac{1}{\sqrt{1 - (0.5)^2}} = \dfrac{1}{\sqrt{1 - 0.25}} = \dfrac{2}{\sqrt{3}}$

Substituting these values into the approximation formula:

$f(0.51) \approx \dfrac{\pi}{6} + \dfrac{2}{\sqrt{3}} \times 0.01$

Given $\pi = 3.1416$ and $\dfrac{2}{\sqrt{3}} = 1.1547$:

$\dfrac{\pi}{6} = \dfrac{3.1416}{6} = 0.5236$

$\dfrac{2}{\sqrt{3}} \times 0.01 = 1.1547 \times 0.01 = 0.011547$

$f(0.51) \approx 0.5236 + 0.011547 = 0.535147$

Answer: $0.535147$

</details>

---

### Q8. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The radius of a spherical balloon increases at the rate of $4$ cm/sec. The rate at which its surface area increases, when the radius is $5$ metres is

**Options:**

- **(A)** $160\pi$ $\text{cm}^2/\text{sec}$
- **(B)** $1600\pi$ $\text{cm}^2/\text{sec}$
- **(C)** $16000\pi$ $\text{cm}^2/\text{sec}$
- **(D)** $16000$ $\text{cm}^2/\text{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $16000\pi$ $\text{cm}^2/\text{sec}$**

**Detailed Solution:**

Let $r$ be the radius and $S$ be the surface area of the spherical balloon.

Given $\dfrac{dr}{dt} = 4$ cm/sec and $r = 5$ m $= 500$ cm.

The surface area of a sphere is given by $S = 4\pi r^2$.

Differentiating with respect to time $t$, we get:

$\dfrac{dS}{dt} = 8\pi r \dfrac{dr}{dt}$

Substituting the values of $r$ and $\dfrac{dr}{dt}$:

$\dfrac{dS}{dt} = 8\pi (500) (4) = 16000\pi$ $\text{cm}^2/\text{sec}$

Answer: $16000\pi$ $\text{cm}^2/\text{sec}$

</details>

---

### Q9. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The radius of a spherical soap bubble is increasing at a constant rate of $0.5$ cm/sec. At the instant when the radius is $5$ cm, the rate at which its volume is increasing is...

**Options:**

- **(A)** $25\pi$ cm$^3$/sec
- **(B)** $50\pi$ cm$^3$/sec
- **(C)** $100\pi$ cm$^3$/sec
- **(D)** $10\pi$ cm$^3$/sec

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $50\pi$ cm$^3$/sec**

**Detailed Solution:**

Let $r$ be the radius and $V$ be the volume of the spherical soap bubble.

Given $\dfrac{dr}{dt} = 0.5$ cm/sec.

The volume of a sphere is $V = \dfrac{4}{3}\pi r^3$.

Differentiating with respect to time $t$, we get:

$\dfrac{dV}{dt} = 4\pi r^2 \dfrac{dr}{dt}$

Substituting $r = 5$ cm and $\dfrac{dr}{dt} = 0.5$ cm/sec:

$\dfrac{dV}{dt} = 4\pi (5)^2 (0.5) = 4\pi (25) \left(\dfrac{1}{2}\right) = 50\pi$ cm$^3$/sec.

Answer: $50\pi$ cm$^3$/sec

</details>

---

### Q10. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A man of height $2$ meters walks at a uniform speed of $6$ km/hr away from a lamp post of height $6$ meters, then the rate at which the length of the shadow is increasing is ...

**Options:**

- **(A)** $7$ km/hr
- **(B)** $10$ km/hr
- **(C)** $3$ km/hr
- **(D)** $23$ km/hr

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$ km/hr**

**Detailed Solution:**

Let $x$ be the distance of the man from the lamp post and $y$ be the length of his shadow.

From the property of similar triangles formed by the lamp post, the man, and the shadow:

$\dfrac{6}{x + y} = \dfrac{2}{y}$

$6y = 2x + 2y$

$4y = 2x$

$y = \dfrac{x}{2}$

Differentiating with respect to time $t$:

$\dfrac{dy}{dt} = \dfrac{1}{2} \dfrac{dx}{dt}$

Given that the speed of the man is $\dfrac{dx}{dt} = 6$ km/hr:

$\dfrac{dy}{dt} = \dfrac{1}{2} \times 6 = 3$ km/hr

The rate at which the length of the shadow is increasing is $3$ km/hr.

Answer: $3$ km/hr

</details>

---

### Q11. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An aeroplane at an altitude of 1 km is flying horizontally at 600 km / hr, passes directly over an observer. Then the rate at which it is approaching the observer when it is 1250 meters away from him is........

**Options:**

- **(A)** $360\ km/hr$
- **(B)** $430\ km/hr$
- **(C)** $600\ km/hr$
- **(D)** $250\ km/hr$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $360\ km/hr$**

**Detailed Solution:**

Let the horizontal distance of the aeroplane from the observer be $x$ km and the actual distance be $s$ km.

The altitude of the aeroplane is $h = 1$ km.

From the right-angled triangle formed by the observer, the aeroplane, and the point on the ground directly below the aeroplane, we have:

$s^2 = x^2 + 1^2$

Differentiating with respect to time $t$, we get:

$2s \dfrac{ds}{dt} = 2x \dfrac{dx}{dt}$

$\dfrac{ds}{dt} = \dfrac{x}{s} \dfrac{dx}{dt}$

We are given the horizontal velocity $\dfrac{dx}{dt} = 600$ km/hr.

When the distance $s = 1250$ m $= 1.25$ km, the horizontal distance $x$ is:

$x = \sqrt{s^2 - 1^2} = \sqrt{1.25^2 - 1} = \sqrt{1.5625 - 1} = \sqrt{0.5625} = 0.75$ km

Substituting the values into the derivative equation:

$\dfrac{ds}{dt} = \dfrac{0.75}{1.25} \times 600$

$\dfrac{ds}{dt} = \dfrac{3}{5} \times 600 = 360$ km/hr

Answer: $360\ km/hr$

</details>

---

### Q12. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A spherical iron ball $10$ cm in radius is coated with a layer of ice of uniform thickness that melts at a rate of $50\ \text{cm}^3/\text{min}$. When the thickness of ice is $5$ cm, the rate at which the thickness of ice decreases is...

**Options:**

- **(A)** $\dfrac{1}{18\pi}\ \text{cm}/\text{min}$
- **(B)** $\dfrac{1}{36\pi}\ \text{cm}/\text{min}$
- **(C)** $\dfrac{5}{6\pi}\ \text{cm}/\text{min}$
- **(D)** $\dfrac{1}{54\pi}\ \text{cm}/\text{min}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{18\pi}\ \text{cm}/\text{min}$**

**Detailed Solution:**

Let $r$ be the radius of the iron ball and $x$ be the thickness of the ice.

Given $r = 10$ cm.

The volume of the ice is $V = \dfrac{4}{3}\pi (r+x)^3 - \dfrac{4}{3}\pi r^3$.

Differentiating with respect to time $t$:

$\dfrac{dV}{dt} = 4\pi (r+x)^2 \dfrac{dx}{dt}$

Given that the ice melts at a rate of $50\ \text{cm}^3/\text{min}$, we have $\dfrac{dV}{dt} = -50$.

When $x = 5$ cm, $r+x = 10 + 5 = 15$ cm.

Substituting the values:

$-50 = 4\pi (15)^2 \dfrac{dx}{dt}$

$-50 = 900\pi \dfrac{dx}{dt}$

$\dfrac{dx}{dt} = -\dfrac{50}{900\pi} = -\dfrac{1}{18\pi}\ \text{cm}/\text{min}$

The rate at which the thickness of ice decreases is $\dfrac{1}{18\pi}\ \text{cm}/\text{min}$.

</details>

---

### Q13. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the rate of increase of surface area of a spherical balloon is $5\,\text{cm}^2/\text{sec}$ and rate of increase of volume of a spherical balloon is $10\,\text{cm}^3/\text{sec}$, then the radius of the balloon at that time is...

**Options:**

- **(A)** $3$ cm
- **(B)** $5$ cm
- **(C)** $6$ cm
- **(D)** $4$ cm

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4$ cm**

**Detailed Solution:**

Let $r$ be the radius, $S$ be the surface area, and $V$ be the volume of the spherical balloon.

$S = 4\pi r^2$

Differentiating with respect to time $t$:

$\dfrac{dS}{dt} = 8\pi r \dfrac{dr}{dt} = 5$

$V = \dfrac{4}{3}\pi r^3$

Differentiating with respect to time $t$:

$\dfrac{dV}{dt} = 4\pi r^2 \dfrac{dr}{dt} = 10$

Dividing $\dfrac{dV}{dt}$ by $\dfrac{dS}{dt}$:

$\dfrac{4\pi r^2 \dfrac{dr}{dt}}{8\pi r \dfrac{dr}{dt}} = \dfrac{10}{5}$

$\dfrac{r}{2} = 2$

$r = 4$ cm

Answer: $4$ cm

</details>

---

### Q14. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A particle is fired straight up from the ground. Its height in feet after $t$ second is given by $s(t) = 128t - 16t^2$. The velocity of the particle when it hits the ground is...

**Options:**

- **(A)** $-128$ ft/sec
- **(B)** $128$ ft/sec
- **(C)** $0$ ft/sec
- **(D)** $256$ ft/sec

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-128$ ft/sec**

**Detailed Solution:**

The height of the particle is given by $s(t) = 128t - 16t^2$.

The particle hits the ground when $s(t) = 0$.

$128t - 16t^2 = 0$

$16t(8 - t) = 0$

This gives $t = 0$ or $t = 8$. The particle hits the ground at $t = 8$ seconds.

The velocity of the particle is given by the derivative of the position function:

$v(t) = \dfrac{ds}{dt} = 128 - 32t$

Substituting $t = 8$ into the velocity equation:

$v(8) = 128 - 32(8) = 128 - 256 = -128$ ft/sec.

Answer: $-128$ ft/sec

</details>

---

### Q15. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a particle moves such that the displacement (s) is proportional to the square of the velocity (v), then its acceleration (a) is

**Options:**

- **(A)** proportional to $s^2$
- **(B)** proportional to $1/s$
- **(C)** proportional to $1/s^2$
- **(D)** a constant

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) a constant**

**Detailed Solution:**

Given $s \propto v^2$

$s = k v^2$ where $k$ is a constant.

Differentiating both sides with respect to time $t$:

$\dfrac{ds}{dt} = 2kv \dfrac{dv}{dt}$

Since $\dfrac{ds}{dt} = v$ and $\dfrac{dv}{dt} = a$:

$v = 2kv a$

$a = \dfrac{1}{2k}$

Since $k$ is a constant, acceleration $a$ is a constant.

Answer: a constant

</details>

---

### Q16. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the side of an equilateral triangle increases at the rate of $\sqrt{3}\ \text{cm/sec}$, then the rate of change of increase of its area when the side is $12\ \text{cm}$ is ____

**Options:**

- **(A)** $18\ \text{cm}^2/\text{sec}$
- **(B)** $10\ \text{cm}^2/\text{sec}$
- **(C)** $12\ \text{cm}^2/\text{sec}$
- **(D)** $3\sqrt{3}\ \text{cm}^2/\text{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $18\ \text{cm}^2/\text{sec}$**

**Detailed Solution:**

Let the side of the equilateral triangle be $a$ and its area be $A$.

Given $\dfrac{da}{dt} = \sqrt{3}\ \text{cm/sec}$ and $a = 12\ \text{cm}$.

The area of an equilateral triangle is given by $A = \dfrac{\sqrt{3}}{4}a^2$.

Differentiating with respect to time $t$:

$\dfrac{dA}{dt} = \dfrac{\sqrt{3}}{4} \times 2a \times \dfrac{da}{dt}$

$\dfrac{dA}{dt} = \dfrac{\sqrt{3}}{2}a \dfrac{da}{dt}$

Substituting the given values:

$\dfrac{dA}{dt} = \dfrac{\sqrt{3}}{2} \times 12 \times \sqrt{3}$

$\dfrac{dA}{dt} = 6 \times 3 = 18\ \text{cm}^2/\text{sec}$

Answer: $18\ \text{cm}^2/\text{sec}$

</details>

---

### Q17. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A spherical snow ball is melting so that its volume is decreasing at the rate of 8 c.c./sec then the rate of change of radius when the radius is 2 cm, is :

**Options:**

- **(A)** The radius is increasing at the rate of $\dfrac{1}{2\pi}\ \text{cm/s}$
- **(B)** The radius is decreasing at the rate of $\dfrac{1}{2\pi}\ \text{cm/s}$
- **(C)** The radius is increasing at the rate of $\dfrac{1}{\pi}\ \text{cm/s}$
- **(D)** The radius is decreasing at the rate of $\dfrac{1}{\pi}\ \text{cm/s}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) The radius is decreasing at the rate of $\dfrac{1}{2\pi}\ \text{cm/s}$**

**Detailed Solution:**

Let $V$ be the volume and $r$ be the radius of the spherical snowball.

$V = \dfrac{4}{3}\pi r^3$

Differentiating with respect to time $t$:

$\dfrac{dV}{dt} = 4\pi r^2 \dfrac{dr}{dt}$

Given that the volume is decreasing at the rate of $8$ c.c./sec, $\dfrac{dV}{dt} = -8$ cm$^3$/sec.

Substituting $r = 2$ cm and $\dfrac{dV}{dt} = -8$:

$-8 = 4\pi (2)^2 \dfrac{dr}{dt}$

$-8 = 16\pi \dfrac{dr}{dt}$

$\dfrac{dr}{dt} = -\dfrac{1}{2\pi}$ cm/sec

The negative sign indicates that the radius is decreasing at the rate of $\dfrac{1}{2\pi}$ cm/s.

Answer: The radius is decreasing at the rate of $\dfrac{1}{2\pi}\ \text{cm/s}$

</details>

---

### Q18. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A triangle has two fixed vertices A $(a, 0)$ and B$(0, b)$ . Let its third vertex C is moving along the line $x = y$. If $s$ is the area of triangle ABC, then $\dfrac{ds}{dx} =$

**Options:**

- **(A)** $a + b$
- **(B)** $-\left(\dfrac{a + b}{2}\right)$
- **(C)** $\dfrac{a - b}{2}$
- **(D)** $\dfrac{a}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\left(\dfrac{a + b}{2}\right)$**

**Detailed Solution:**

Let the coordinates of the vertices of the triangle be $A(a, 0)$, $B(0, b)$, and $C(x, x)$ since $C$ lies on the line $y = x$.

The area of the triangle $s$ is given by the determinant formula:

$s = \dfrac{1}{2} \begin{vmatrix} a & 0 & 1 \\ 0 & b & 1 \\ x & x & 1 \end{vmatrix}$

Expanding the determinant along the first row:

$s = \dfrac{1}{2} [a(b - x) - 0 + 1(0 - bx)]$

$s = \dfrac{1}{2} (ab - ax - bx)$

$s = \dfrac{1}{2} [ab - (a + b)x]$

Differentiating $s$ with respect to $x$:

$\dfrac{ds}{dx} = \dfrac{d}{dx} \left[ \dfrac{1}{2} (ab - (a + b)x) \right]$

$\dfrac{ds}{dx} = -\left(\dfrac{a + b}{2}\right)$

Answer: $-\left(\dfrac{a + b}{2}\right)$

</details>

---

### Q19. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The surface area of a spherical ball is increasing at the rate of $4\pi\ \text{cm}^2$/second. The rate at which the radius is increasing when the surface area is $16\pi\ \text{cm}^2$ is

**Options:**

- **(A)** $0.5$ cm/second
- **(B)** $0.25$ cm/second
- **(C)** $0.125$ cm/second
- **(D)** $1$ cm/second

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.25$ cm/second**

**Detailed Solution:**

Let $S$ be the surface area and $r$ be the radius of the spherical ball.

$S = 4\pi r^2$

Differentiating with respect to time $t$:

$\dfrac{dS}{dt} = 8\pi r \dfrac{dr}{dt}$

Given $\dfrac{dS}{dt} = 4\pi$ cm$^2$/s.

When $S = 16\pi$ cm$^2$:

$4\pi r^2 = 16\pi \Rightarrow r^2 = 4 \Rightarrow r = 2$ cm.

Substituting the values into the derivative equation:

$4\pi = 8\pi (2) \dfrac{dr}{dt}$

$4\pi = 16\pi \dfrac{dr}{dt}$

$\dfrac{dr}{dt} = \dfrac{4\pi}{16\pi} = 0.25$ cm/s.

</details>

---

### Q20. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A spherical mothball has initial radius 3 cm. Due to evaporation, the radius of the ball reduces to 1 cm in 4 months. In how many months would the mothball evaporate completely if the volume is lost at a rate proportional to the surface area ?

**Options:**

- **(A)** $6$ months
- **(B)** $8$ months
- **(C)** $10$ months
- **(D)** $12$ months

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6$ months**

**Detailed Solution:**

Let $V$ be the volume and $S$ be the surface area of the spherical mothball of radius $r$.

$V = \dfrac{4}{3} \pi r^3$

$S = 4 \pi r^2$

Given that the rate of loss of volume is proportional to the surface area:

$\dfrac{dV}{dt} = -k S$

Differentiating $V$ with respect to $t$:

$\dfrac{dV}{dt} = \dfrac{d}{dt} \left( \dfrac{4}{3} \pi r^3 \right) = 4 \pi r^2 \dfrac{dr}{dt} = S \dfrac{dr}{dt}$

Equating the two expressions for $\dfrac{dV}{dt}$:

$S \dfrac{dr}{dt} = -k S \Rightarrow \dfrac{dr}{dt} = -k$

Integrating both sides with respect to $t$:

$r(t) = -kt + C$

At $t = 0$, $r = 3$ cm, which gives $C = 3$.

$r(t) = 3 - kt$

At $t = 4$ months, $r = 1$ cm:

$1 = 3 - 4k \Rightarrow 4k = 2 \Rightarrow k = \dfrac{1}{2}$

The mothball evaporates completely when $r(t) = 0$:

$0 = 3 - \dfrac{1}{2} t \Rightarrow t = 6$ months.

Answer: $6$ months

</details>

---

### Q21. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If a spherical balloon has a variable diameter $3x + \dfrac{9}{2}$ units, then the rate of change of its volume with respect to $x$ is

**Options:**

- **(A)** $\dfrac{27\pi}{4}(2x + 3)^2$
- **(B)** $\dfrac{2\pi}{3}(2x + 3)^2$
- **(C)** $\dfrac{27\pi}{8}(2x + 3)^2$
- **(D)** $\dfrac{27\pi}{2}(2x + 3)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{27\pi}{8}(2x + 3)^2$**

**Detailed Solution:**

Given the diameter of the spherical balloon is $D = 3x + \dfrac{9}{2} = \dfrac{3(2x + 3)}{2}$

The radius of the balloon is $r = \dfrac{D}{2} = \dfrac{3(2x + 3)}{4}$

The volume of the spherical balloon is $V = \dfrac{4}{3}\pi r^3$

Substituting the value of $r$:

$V = \dfrac{4}{3}\pi \left( \dfrac{3(2x + 3)}{4} \right)^3$

$V = \dfrac{4}{3}\pi \left( \dfrac{27(2x + 3)^3}{64} \right)$

$V = \dfrac{9\pi}{16}(2x + 3)^3$

Differentiating the volume with respect to $x$:

$\dfrac{dV}{dx} = \dfrac{9\pi}{16} \cdot 3(2x + 3)^2 \cdot \dfrac{d}{dx}(2x + 3)$

$\dfrac{dV}{dx} = \dfrac{27\pi}{16}(2x + 3)^2 \cdot 2$

$\dfrac{dV}{dx} = \dfrac{27\pi}{8}(2x + 3)^2$

</details>

---

### Q22. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The approximate value of $\sqrt[3]{63}$ is

**Options:**

- **(A)** $3.9791$
- **(B)** $3.8791$
- **(C)** $3.9581$
- **(D)** $4.0205$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3.9791$**

**Detailed Solution:**

Let $f(x) = x^{1/3}$.

Let $x = 64$ and $\Delta x = -1$.

We know that $f(x + \Delta x) \approx f(x) + f'(x) \Delta x$.

Differentiating $f(x)$ with respect to $x$, we get:

$f'(x) = \dfrac{1}{3} x^{-2/3}$

At $x = 64$, $f'(64) = \dfrac{1}{3} (64)^{-2/3} = \dfrac{1}{3} \times \dfrac{1}{16} = \dfrac{1}{48}$

Now, $\Delta y \approx f'(64) \Delta x = \dfrac{1}{48} \times (-1) \approx -0.02083$

Therefore, the approximate value is:

$f(63) \approx 4 - 0.02083 = 3.97917$

A more precise calculation using the binomial expansion yields $3.979057$, which rounds to $3.9791$. The closest given option is $3.9791$.

Answer: $3.9791$

</details>

---

### Q23. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A spherical balloon is filled with $4500 \pi$ cubic meters of helium gas. If a leak in the balloon causes the gas to escape at the rate of $72 \pi$ cubic meters per minute, then the rate (in meters per minute) at which the radius of the balloon decreases 49 minutes after the leakage has begun, is

**Options:**

- **(A)** $\frac{9}{7}$
- **(B)** $-\frac{2}{9}$
- **(C)** $\frac{9}{2}$
- **(D)** $\frac{2}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2}{9}$**

**Detailed Solution:**

Volume of the spherical balloon is $V = \dfrac{4}{3} \pi r^3$.

Given initial volume $V_0 = 4500 \pi$ and the rate of change of volume $\dfrac{dV}{dt} = -72 \pi$.

Volume after $49$ minutes is $V = 4500 \pi - 72 \pi \times 49 = 4500 \pi - 3528 \pi = 972 \pi$.

Equating to the volume formula:

$\dfrac{4}{3} \pi r^3 = 972 \pi$

$r^3 = \dfrac{972 \times 3}{4} = 243 \times 3 = 729$

$r = 9$

Differentiating $V = \dfrac{4}{3} \pi r^3$ with respect to $t$:

$\dfrac{dV}{dt} = 4 \pi r^2 \dfrac{dr}{dt}$

Substituting the values $r = 9$ and $\dfrac{dV}{dt} = -72 \pi$:

$-72 \pi = 4 \pi (9)^2 \dfrac{dr}{dt}$

$-72 \pi = 324 \pi \dfrac{dr}{dt}$

$\dfrac{dr}{dt} = -\dfrac{72}{324} = -\dfrac{2}{9}$

The rate at which the radius decreases is the negative of the rate of change, which is $\dfrac{2}{9}$.

Answer: $\frac{2}{9}$

</details>

---

### Q24. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The approximate value of $\frac{1}{(2.002)^2}$ is

**Options:**

- **(A)** 0.2495
- **(B)** 0.2595
- **(C)** 0.2095
- **(D)** 0.2392

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0.2495**

**Detailed Solution:**

Let $f(x) = \dfrac{1}{x^2} = x^{-2}$

Let $a = 2$ and $h = 0.002$

$f(a) = f(2) = \dfrac{1}{2^2} = 0.25$

$f'(x) = -2x^{-3} = -\dfrac{2}{x^3}$

$f'(a) = f'(2) = -\dfrac{2}{2^3} = -0.25$

Using the approximation formula $f(a+h) \approx f(a) + h f'(a)$

$f(2.002) \approx 0.25 + (0.002)(-0.25)$

$f(2.002) \approx 0.25 - 0.0005 = 0.2495$

Answer: 0.2495

</details>

---

### Q25. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The surface area of a spherical ball is increasing at the rate of $4 \pi \mathrm{~cm}^2 /$ second . The rate at which the radius is increasing when the surface area is $16 \pi \mathrm{~cm}^2$ is

**Options:**

- **(A)** $0.25 \mathrm{~cm} /$ second
- **(B)** $0.5 \mathrm{~cm} /$ second
- **(C)** $0.125 \mathrm{~cm} /$ second
- **(D)** $1 \mathrm{~cm} /$ second

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.25 \mathrm{~cm} /$ second**

**Detailed Solution:**

Let $S$ be the surface area and $r$ be the radius of the spherical ball.

The surface area of a sphere is given by:
$S = 4 \pi r^2$

Differentiating with respect to time $t$, we get:
$\dfrac{dS}{dt} = 8 \pi r \dfrac{dr}{dt}$

We are given that $\dfrac{dS}{dt} = 4 \pi \text{ cm}^2/\text{second}$.

When the surface area $S = 16 \pi \text{ cm}^2$, we can find the radius $r$:
$4 \pi r^2 = 16 \pi$
$r^2 = 4 \Rightarrow r = 2 \text{ cm}$

Substituting the values of $\dfrac{dS}{dt}$ and $r$ into the derivative equation:
$4 \pi = 8 \pi (2) \dfrac{dr}{dt}$
$4 \pi = 16 \pi \dfrac{dr}{dt}$

$\dfrac{dr}{dt} = \dfrac{4 \pi}{16 \pi} = \dfrac{1}{4} = 0.25 \text{ cm}/\text{second}$

Answer: $0.25 \mathrm{~cm} /$ second

</details>

---

### Q26. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x$ and y are sides of two squares such that $\mathrm{y}=x-x^2$, then the rate of change of area of the second square with respect to that of the first square is

**Options:**

- **(A)** $2 x^2+3 x+1$
- **(B)** $3 x^2+2 x-1$
- **(C)** $2 x^2-3 x+1$
- **(D)** $3 x^2+2 x+1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 x^2-3 x+1$**

**Detailed Solution:**

Let $A_1$ and $A_2$ be the areas of the first and second squares respectively.

$A_1 = x^2$

$A_2 = y^2 = (x - x^2)^2$

Differentiating $A_1$ and $A_2$ with respect to $x$:

$\dfrac{dA_1}{dx} = 2x$

$\dfrac{dA_2}{dx} = 2(x - x^2)(1 - 2x) = 2x(1 - x)(1 - 2x)$

The rate of change of the area of the second square with respect to the first square is given by:

$\dfrac{dA_2}{dA_1} = \dfrac{\dfrac{dA_2}{dx}}{\dfrac{dA_1}{dx}}$

$\dfrac{dA_2}{dA_1} = \dfrac{2x(1 - x)(1 - 2x)}{2x}$

$\dfrac{dA_2}{dA_1} = (1 - x)(1 - 2x) = 2x^2 - 3x + 1$

Answer: $2 x^2-3 x+1$

</details>

---

### Q27. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The rate of change of the volume of a sphere with respect to its surface area, when the radius is 5 m is

**Options:**

- **(A)** $\frac{5}{2} \mathrm{~m}$
- **(B)** $\frac{2}{5} \mathrm{~m}$
- **(C)** $\frac{1}{2} \mathrm{~m}$
- **(D)** $\frac{1}{3} \mathrm{~m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{5}{2} \mathrm{~m}$**

**Detailed Solution:**

Let $V$ be the volume and $S$ be the surface area of the sphere with radius $r$.

$V = \dfrac{4}{3} \pi r^3$

$S = 4 \pi r^2$

Differentiating both with respect to $r$:

$\dfrac{dV}{dr} = 4 \pi r^2$

$\dfrac{dS}{dr} = 8 \pi r$

The rate of change of volume with respect to surface area is given by:

$\dfrac{dV}{dS} = \dfrac{\dfrac{dV}{dr}}{\dfrac{dS}{dr}}$

$\dfrac{dV}{dS} = \dfrac{4 \pi r^2}{8 \pi r} = \dfrac{r}{2}$

Substituting $r = 5$ m:

$\dfrac{dV}{dS} = \dfrac{5}{2}$ m

Answer: $\frac{5}{2} \mathrm{~m}$

</details>

---

### Q28. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The length and breadth of a rectangle are $x \mathrm{~cm}$ and y cm respectively. If the length decreases at the rate of $5 \mathrm{~cm} /$ minute and the breadth increases at the rate of $3 \mathrm{~cm} /$ minute, then the rates of change of the perimeter and area respectively when the length is 5 cm and breadth is 2 cm , are

**Options:**

- **(A)** -4 and 5
- **(B)** -5 and 3
- **(C)** 3 and 5
- **(D)** 3 and -5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -4 and 5**

**Detailed Solution:**

Let $x$ be the length and $y$ be the breadth of the rectangle.

Given that the length decreases at $5$ cm/min and the breadth increases at $3$ cm/min, we have:
$\dfrac{dx}{dt} = -5$
$\dfrac{dy}{dt} = 3$

The perimeter of the rectangle is given by $P = 2(x + y)$.
Differentiating with respect to $t$ gives the rate of change of the perimeter:
$\dfrac{dP}{dt} = 2\left(\dfrac{dx}{dt} + \dfrac{dy}{dt}\right)$
$\dfrac{dP}{dt} = 2(-5 + 3) = 2(-2) = -4$ cm/min

The area of the rectangle is given by $A = xy$.
Differentiating with respect to $t$ gives the rate of change of the area:
$\dfrac{dA}{dt} = x\dfrac{dy}{dt} + y\dfrac{dx}{dt}$

Substituting $x = 5$, $y = 2$, $\dfrac{dx}{dt} = -5$, and $\dfrac{dy}{dt} = 3$:
$\dfrac{dA}{dt} = (5)(3) + (2)(-5)$
$\dfrac{dA}{dt} = 15 - 10 = 5$ cm$^2$/min

The rates of change of the perimeter and area are $-4$ and $5$ respectively.

Answer: -4 and 5

</details>

---

### Q29. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The rate of change of volume of spherical balloon at any instant is directly proportional to its surface area. If initially its radius is 3 cm , after 2 minutes its radius becomes 9 cm , then radius of balloon after 4 minutes is

**Options:**

- **(A)** 12 cm
- **(B)** 14 cm
- **(C)** 15 cm
- **(D)** 18 cm

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 15 cm**

**Detailed Solution:**

Let $V$ be the volume and $S$ be the surface area of the spherical balloon of radius $r$.

$V = \dfrac{4}{3} \pi r^3$ and $S = 4 \pi r^2$

Given that the rate of change of volume is directly proportional to its surface area:

$\dfrac{dV}{dt} \propto S$

$\dfrac{dV}{dt} = kS$

Differentiating $V$ with respect to $t$:

$\dfrac{d}{dt} \left( \dfrac{4}{3} \pi r^3 \right) = k(4 \pi r^2)$

$4 \pi r^2 \dfrac{dr}{dt} = 4 \pi k r^2$

$\dfrac{dr}{dt} = k$

Integrating both sides with respect to $t$:

$r = kt + c$

Initially, at $t = 0$, $r = 3$ cm:

$3 = k(0) + c \Rightarrow c = 3$

After $t = 2$ minutes, $r = 9$ cm:

$9 = k(2) + 3 \Rightarrow 2k = 6 \Rightarrow k = 3$

The equation for the radius becomes:

$r = 3t + 3$

To find the radius after $t = 4$ minutes:

$r = 3(4) + 3 = 12 + 3 = 15$ cm.

Answer: 15 cm

</details>

---

### Q30. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The equation of motion of the particle is $s=a t^2+b t+c$. If the displacement after 1 second is 20 m , velocity after 2 seconds is 30 $\mathrm{m} /$ seconds and the acceleration is $10 \mathrm{~m} /$ seconds $^2$, then

**Options:**

- **(A)** $a+c=2 b$
- **(B)** $a+c=b$
- **(C)** $a-c=b$
- **(D)** $a+c=3 b$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $a+c=b$**

**Detailed Solution:**

Given $s = at^2 + bt + c$

Velocity $v = \dfrac{ds}{dt} = 2at + b$

Acceleration $A = \dfrac{dv}{dt} = 2a$

Given acceleration is $10 \text{ m/s}^2$, so $2a = 10 \Rightarrow a = 5$

Velocity after 2 seconds is $30 \text{ m/s}$, so $v(2) = 4a + b = 30$

Substituting $a = 5$, we get $4(5) + b = 30 \Rightarrow b = 10$

Displacement after 1 second is $20 \text{ m}$, so $s(1) = a + b + c = 20$

Substituting $a = 5$ and $b = 10$, we get $5 + 10 + c = 20 \Rightarrow c = 5$

Now, checking the options, we find $a + c = 5 + 5 = 10$ and $b = 10$

Therefore, $a + c = b$.

Answer: $a+c=b$

</details>

---

### Q31. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The approximate value of $\sqrt[3]{64.04}$ is

**Options:**

- **(A)** $4.00043$
- **(B)** $4.00076$
- **(C)** $4.00083$
- **(D)** $4.00064$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4.00083$**

**Detailed Solution:**

Let $f(x) = x^{1/3}$.

Differentiating with respect to $x$, we get $f'(x) = \dfrac{1}{3} x^{-2/3} = \dfrac{1}{3x^{2/3}}$.

Let $x = 64$ and $\Delta x = 0.04$.

$f(x) = f(64) = (64)^{1/3} = 4$

$f'(x) = f'(64) = \dfrac{1}{3(64)^{2/3}} = \dfrac{1}{3(16)} = \dfrac{1}{48}$

The approximate value is given by $f(x + \Delta x) \approx f(x) + f'(x) \Delta x$.

$f(64.04) \approx 4 + \left(\dfrac{1}{48}\right)(0.04)$

$f(64.04) \approx 4 + \dfrac{0.04}{48} = 4 + \dfrac{1}{1200}$

$f(64.04) \approx 4 + 0.000833... \approx 4.00083$

Answer: $4.00083$

</details>

---

### Q32. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $x$ be the length of each of the equal sides of an isosceles triangle and $\theta$ be the angle between these sides. If $x$ is increasing at the rate $\frac{1}{12} \mathrm{~m} /$ hour and $\theta$ is increasing at the rate $\frac{\pi}{180} \mathrm{rad} /$ hour, then the rate at which area of the triangle is increasing when $x=12 \mathrm{~m}$ and $\theta=\frac{\pi}{4}$ is

**Options:**

- **(A)** $\left(\frac{\pi}{5}+\frac{1}{2}\right) \mathrm{m}^2 /$ hour
- **(B)** $\sqrt{2}\left(\frac{\pi}{5}+\frac{1}{2}\right) \mathrm{m}^2 /$ hour
- **(C)** $2\left(\frac{\pi}{5}+\frac{1}{2}\right) \mathrm{m}^2 /$ hour
- **(D)** $\sqrt{3}\left(\frac{\pi}{5}+\frac{1}{2}\right) \mathrm{m}^2 /$ hour

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{2}\left(\frac{\pi}{5}+\frac{1}{2}\right) \mathrm{m}^2 /$ hour**

**Detailed Solution:**

Let $A$ be the area of the isosceles triangle. The area is given by $A = \dfrac{1}{2} x^2 \sin \theta$.

Differentiating with respect to time $t$:

$\dfrac{dA}{dt} = \dfrac{1}{2} \left( 2x \dfrac{dx}{dt} \sin \theta + x^2 \cos \theta \dfrac{d\theta}{dt} \right)$

$\dfrac{dA}{dt} = x \dfrac{dx}{dt} \sin \theta + \dfrac{1}{2} x^2 \cos \theta \dfrac{d\theta}{dt}$

Given $x = 12$, $\theta = \dfrac{\pi}{4}$, $\dfrac{dx}{dt} = \dfrac{1}{12}$, and $\dfrac{d\theta}{dt} = \dfrac{\pi}{180}$.

Substituting these values:

$\dfrac{dA}{dt} = 12 \left( \dfrac{1}{12} \right) \sin \dfrac{\pi}{4} + \dfrac{1}{2} (12)^2 \cos \dfrac{\pi}{4} \left( \dfrac{\pi}{180} \right)$

$\dfrac{dA}{dt} = 1 \cdot \dfrac{1}{\sqrt{2}} + 72 \cdot \dfrac{1}{\sqrt{2}} \cdot \dfrac{\pi}{180}$

$\dfrac{dA}{dt} = \dfrac{1}{\sqrt{2}} + \dfrac{2\pi}{5\sqrt{2}}$

$\dfrac{dA}{dt} = \dfrac{1}{\sqrt{2}} \left( 1 + \dfrac{2\pi}{5} \right)$

$\dfrac{dA}{dt} = \dfrac{2}{\sqrt{2}} \left( \dfrac{1}{2} + \dfrac{\pi}{5} \right) = \sqrt{2} \left( \dfrac{\pi}{5} + \dfrac{1}{2} \right)$

Answer: $\sqrt{2}\left(\frac{\pi}{5}+\frac{1}{2}\right) \mathrm{m}^2 /$ hour

</details>

---

### Q33. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The radius of the base of a cone is increasing at the rate $3 \mathrm{~cm} /$ minute and the altitude is decreasing at the rate $4 \mathrm{~cm} /$ minute. The rate at which the lateral surface area is changing, when the radius is 7 cm and altitude is 24 cm . is

**Options:**

- **(A)** $75 \pi \mathrm{~cm}^2 /$ minute
- **(B)** $25 \pi \mathrm{~cm}^2 /$ minute
- **(C)** $3 \pi \mathrm{~cm}^2 /$ minute
- **(D)** $54 \pi \mathrm{~cm}^2 /$ minute

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $54 \pi \mathrm{~cm}^2 /$ minute**

**Detailed Solution:**

Let $r$ be the radius, $h$ be the altitude, $l$ be the slant height, and $S$ be the lateral surface area of the cone.

Given: $\dfrac{dr}{dt} = 3$ and $\dfrac{dh}{dt} = -4$.

At the given instant, $r = 7$ and $h = 24$.

The slant height is $l = \sqrt{r^2 + h^2} = \sqrt{7^2 + 24^2} = 25$.

Differentiating $l^2 = r^2 + h^2$ with respect to $t$:

$2l \dfrac{dl}{dt} = 2r \dfrac{dr}{dt} + 2h \dfrac{dh}{dt}$

$l \dfrac{dl}{dt} = r \dfrac{dr}{dt} + h \dfrac{dh}{dt}$

$25 \dfrac{dl}{dt} = 7(3) + 24(-4) = 21 - 96 = -75$

$\dfrac{dl}{dt} = -3$

The lateral surface area is $S = \pi r l$. Differentiating with respect to $t$:

$\dfrac{dS}{dt} = \pi \left( r \dfrac{dl}{dt} + l \dfrac{dr}{dt} \right)$

$\dfrac{dS}{dt} = \pi \left( 7(-3) + 25(3) \right) = \pi (-21 + 75) = 54\pi$

The rate at which the lateral surface area is changing is $54\pi \text{ cm}^2/\text{minute}$.

Answer: $54 \pi \mathrm{~cm}^2 /$ minute

</details>

---

### Q34. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The approximate value of $\cos \left(59^{\circ} 30^{\prime}\right)$ is (given $1^{\circ}=0.0175^{\mathrm{c}}, \sin 60^{\circ}=0.8660$ )

**Options:**

- **(A)** $0.5076$
- **(B)** $0.5176$
- **(C)** $0.5256$
- **(D)** $0.5150$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.5076$**

**Detailed Solution:**

Let $f(x) = \cos x$, then $f'(x) = -\sin x$.

We need to find the value of $f(59^{\circ} 30')$.

Let $x = 60^{\circ}$ and $h = -30' = -0.5^{\circ}$.

Converting $h$ into radians:

$h = -0.5 \times 0.0175^{\mathrm{c}} = -0.00875^{\mathrm{c}}$

Using the approximation formula $f(x+h) \approx f(x) + h f'(x)$:

$\cos(59^{\circ} 30') \approx \cos(60^{\circ}) + h(-\sin 60^{\circ})$

$\cos(59^{\circ} 30') \approx 0.5 + (-0.00875)(-0.8660)$

$\cos(59^{\circ} 30') \approx 0.5 + 0.0075775$

$\cos(59^{\circ} 30') \approx 0.5075775 \approx 0.5076$

Answer: $0.5076$

</details>

---

### Q35. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The position of a point in time t is given by $x=\mathrm{a}+\mathrm{bt}-\mathrm{ct}^2, \mathrm{y}=\mathrm{at}+\mathrm{bt}^2$.
It's resultant acceleration at time $t$ in seconds is given by

**Options:**

- **(A)** $\mathrm{b}-\mathrm{c} \quad$ unit/seconds ${ }^2$
- **(B)** $\mathrm{b}+\mathrm{c} \quad$ unit/seconds ${ }^2$
- **(C)** $2 \mathrm{~b}-2 \mathrm{c} \quad$ unit $/$ seconds $^2$
- **(D)** $2 \sqrt{b^2+c^2}$ unit/seconds ${ }^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 \sqrt{b^2+c^2}$ unit/seconds ${ }^2$**

**Detailed Solution:**

Given $x = a + bt - ct^2$ and $y = at + bt^2$.

Differentiating with respect to time $t$, we get the velocity components:
$v_x = \dfrac{dx}{dt} = b - 2ct$
$v_y = \dfrac{dy}{dt} = a + 2bt$

Differentiating again with respect to time $t$, we get the acceleration components:
$a_x = \dfrac{dv_x}{dt} = -2c$
$a_y = \dfrac{dv_y}{dt} = 2b$

The resultant acceleration is given by:
$a = \sqrt{a_x^2 + a_y^2}$
$a = \sqrt{(-2c)^2 + (2b)^2}$
$a = \sqrt{4c^2 + 4b^2} = 2\sqrt{b^2 + c^2}$

Answer: $2 \sqrt{b^2+c^2}$ unit/seconds ${ }^2$

</details>

---

### Q36. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

By dropping a stone in a quiet lake, a wave in the form of circle is generated. The radius of the circular wave increases at the rate of $2.1 \mathrm{~cm} / \mathrm{sec}$. Then the rate of increase of the enclosed circular region, when the radius of the circular wave is 10 cm, is (Given $\pi = \frac{22}{7}$)

**Options:**

- **(A)** $66 \mathrm{~cm}^2 /$ second
- **(B)** $122 \mathrm{~cm}^2 /$ second
- **(C)** $132 \mathrm{~cm}^2 /$ second
- **(D)** $110 \mathrm{~cm}^2 /$ second

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $132 \mathrm{~cm}^2 /$ second**

**Detailed Solution:**

Let $r$ be the radius and $A$ be the area of the circular wave at time $t$.

Given $\dfrac{dr}{dt} = 2.1 \text{ cm/sec}$ and $r = 10 \text{ cm}$.

The area of the circular region is $A = \pi r^2$.

Differentiating with respect to $t$, we get:

$\dfrac{dA}{dt} = 2\pi r \dfrac{dr}{dt}$

Substituting the given values:

$\dfrac{dA}{dt} = 2 \times \dfrac{22}{7} \times 10 \times 2.1$

$\dfrac{dA}{dt} = 2 \times 22 \times 10 \times 0.3$

$\dfrac{dA}{dt} = 44 \times 3 = 132 \text{ cm}^2/\text{sec}$

Answer: $132 \mathrm{~cm}^2 /$ second

</details>

---

### Q37. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Water is being poured at the rate of $36 \mathrm{~m}^3 / \mathrm{min}$ into a cylindrical vessel, whose circular base is of radius 3 meters. Then the water level in the cylinder is rising at the rate of

**Options:**

- **(A)** $4 \pi \mathrm{~m} / \mathrm{min}$
- **(B)** $\frac{4}{\pi} \mathrm{~m} / \mathrm{min}$
- **(C)** $\frac{1}{4 \pi} \mathrm{~m} / \mathrm{min}$
- **(D)** $\frac{\pi}{4} \mathrm{~m} / \mathrm{min}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{4}{\pi} \mathrm{~m} / \mathrm{min}$**

**Detailed Solution:**

Let $V$ be the volume and $h$ be the height of the water in the cylindrical vessel at time $t$.

The volume of the cylinder is given by $V = \pi r^2 h$.

Since the radius $r = 3 \mathrm{~m}$ is constant, substituting $r = 3$ gives:

$V = 9 \pi h$

Differentiating with respect to $t$, we get:

$\dfrac{dV}{dt} = 9 \pi \dfrac{dh}{dt}$

Given that the rate of change of volume is $\dfrac{dV}{dt} = 36 \mathrm{~m}^3/\mathrm{min}$, we have:

$36 = 9 \pi \dfrac{dh}{dt}$

$\dfrac{dh}{dt} = \dfrac{36}{9 \pi} = \dfrac{4}{\pi} \mathrm{~m}/\mathrm{min}$

Answer: $\frac{4}{\pi} \mathrm{~m} / \mathrm{min}$

</details>

---

### Q38. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The rate of change of the volume of a sphere with respect to its surface area, when its radius is 2 cm, is _______ $\mathrm{cm}^3 / \mathrm{cm}^2$.

**Options:**

- **(A)** 0.1
- **(B)** 0.5
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

Let $V$ be the volume and $S$ be the surface area of the sphere of radius $r$.

$V = \dfrac{4}{3}\pi r^3$ and $S = 4\pi r^2$

Differentiating with respect to $r$:

$\dfrac{dV}{dr} = 4\pi r^2$

$\dfrac{dS}{dr} = 8\pi r$

The rate of change of volume with respect to surface area is:

$\dfrac{dV}{dS} = \dfrac{\dfrac{dV}{dr}}{\dfrac{dS}{dr}} = \dfrac{4\pi r^2}{8\pi r} = \dfrac{r}{2}$

Substituting $r = 2$ cm:

$\dfrac{dV}{dS} = \dfrac{2}{2} = 1$ cm$^3$/cm$^2$

Answer: 1

</details>

---

### Q39. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The approximate value of $3^{2.001}$, if $\log 3=1.0986$ is

**Options:**

- **(A)** 9.00898
- **(B)** 9.0989
- **(C)** 9.0898
- **(D)** 9.00989

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 9.00989**

**Detailed Solution:**

Let $f(x) = 3^x$. We need to find the approximate value of $f(2.001)$.

Let $x = 2$ and $\Delta x = 0.001$.

The derivative of the function is:

$f'(x) = 3^x \log 3$

Using the approximation formula $f(x + \Delta x) \approx f(x) + f'(x) \Delta x$, we have:

$f(2.001) \approx f(2) + f'(2) \times 0.001$

Calculate $f(2)$ and $f'(2)$:

$f(2) = 3^2 = 9$

$f'(2) = 3^2 \log 3 = 9 \times 1.0986 = 9.8874$

Substitute these values into the approximation formula:

$f(2.001) \approx 9 + 9.8874 \times 0.001$

$f(2.001) \approx 9 + 0.0098874$

$f(2.001) \approx 9.0098874$

Rounding to five decimal places, we get $9.00989$.

Answer: 9.00989

</details>

---

### Q40. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A ladder 5 m in length is leaning against a wall. The bottom of the ladder is pulled along the ground away from the wall, at the rate of $2 \mathrm{~m} / \mathrm{sec}$. How fast is the height on the wall decreasing when the foot of the ladder is 4 m away from the wall?

**Options:**

- **(A)** $\frac{4}{3} \mathrm{~m} / \mathrm{sec}$
- **(B)** $\frac{2}{3} \mathrm{~m} / \mathrm{sec}$
- **(C)** $\frac{5}{3} \mathrm{~m} / \mathrm{sec}$
- **(D)** $\frac{8}{3} \mathrm{~m} / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{8}{3} \mathrm{~m} / \mathrm{sec}$**

**Detailed Solution:**

Let $x$ be the distance of the foot of the ladder from the wall and $y$ be the height of the ladder on the wall.

By Pythagoras theorem, $x^2 + y^2 = 25$.

Given $\dfrac{dx}{dt} = 2$ m/sec.

When $x = 4$ m, $4^2 + y^2 = 25 \Rightarrow y = 3$ m.

Differentiating $x^2 + y^2 = 25$ with respect to $t$, we get:

$2x \dfrac{dx}{dt} + 2y \dfrac{dy}{dt} = 0$

$x \dfrac{dx}{dt} + y \dfrac{dy}{dt} = 0$

Substituting the values, we get:

$4(2) + 3 \dfrac{dy}{dt} = 0$

$\dfrac{dy}{dt} = -\dfrac{8}{3}$ m/sec.

The height on the wall is decreasing at the rate of $\dfrac{8}{3}$ m/sec.

Answer: $\frac{8}{3} \mathrm{~m} / \mathrm{sec}$

</details>

---

### Q41. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Twenty meters of wire is available for fencing off a flower-bed in the form of a circular sector. Then the maximum area (in sq.m) of the flowerbed is

**Options:**

- **(A)** 30
- **(B)** 12.5
- **(C)** 25
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 25**

**Detailed Solution:**

Let $r$ be the radius and $s$ be the arc length of the circular sector.

The perimeter of the sector is given by $P = 2r + s$.

Since $20$ meters of wire is available, we have:

$2r + s = 20 \Rightarrow s = 20 - 2r$

The area of the circular sector is $A = \dfrac{1}{2}rs$.

Substituting the value of $s$ into the area formula, we get:

$A = \dfrac{1}{2}r(20 - 2r) = 10r - r^2$

To find the maximum area, we differentiate $A$ with respect to $r$ and equate it to zero:

$\dfrac{dA}{dr} = 10 - 2r = 0$

$\Rightarrow r = 5$

To confirm it is a maximum, we check the second derivative:

$\dfrac{d^2A}{dr^2} = -2 < 0$

Thus, the area is maximum when $r = 5$ m.

The maximum area is:

$A_{max} = 10(5) - (5)^2 = 50 - 25 = 25$ sq.m.

Answer: 25

</details>

---

### Q42. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The distance ' $s$ ' in meters covered by a body in $t$ seconds is given by $s=3 t^2-8 t+5$. The body will stop after

**Options:**

- **(A)** 1 sec
- **(B)** $\frac{3}{4} \mathrm{sec}$
- **(C)** $\frac{4}{3} \mathrm{sec}$
- **(D)** 4 sec

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4}{3} \mathrm{sec}$**

**Detailed Solution:**

Given $s = 3t^2 - 8t + 5$.

Velocity $v = \dfrac{ds}{dt}$.

$v = \dfrac{d}{dt}(3t^2 - 8t + 5) = 6t - 8$.

The body stops when its velocity becomes zero, so $v = 0$.

$6t - 8 = 0$

$t = \dfrac{8}{6} = \dfrac{4}{3}$ sec.

Answer: $\frac{4}{3} \mathrm{sec}$

</details>

---

### Q43. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The rate of change of the volume of a sphere with respect to its surface area, when its radius is 2 cm , is

**Options:**

- **(A)** $0.1 \mathrm{~cm}^3 / \mathrm{cm}^2$
- **(B)** $\frac{1}{2} \mathrm{~cm}^3 / \mathrm{cm}^2$
- **(C)** $1 \mathrm{~cm}^3 / \mathrm{cm}^2$
- **(D)** $2 \mathrm{~cm}^3 / \mathrm{cm}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1 \mathrm{~cm}^3 / \mathrm{cm}^2$**

**Detailed Solution:**

Let $V$ be the volume and $S$ be the surface area of the sphere of radius $r$.

$V = \dfrac{4}{3}\pi r^3$

Differentiating with respect to $r$,

$\dfrac{dV}{dr} = 4\pi r^2$

$S = 4\pi r^2$

Differentiating with respect to $r$,

$\dfrac{dS}{dr} = 8\pi r$

The rate of change of volume with respect to surface area is given by

$\dfrac{dV}{dS} = \dfrac{\dfrac{dV}{dr}}{\dfrac{dS}{dr}} = \dfrac{4\pi r^2}{8\pi r} = \dfrac{r}{2}$

Substituting $r = 2$ cm,

$\dfrac{dV}{dS} = \dfrac{2}{2} = 1 \text{ cm}^3/\text{cm}^2$

Answer: $1 \mathrm{~cm}^3 / \mathrm{cm}^2$

</details>

---

### Q44. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The approximate value of $(3.978)^{\frac{3}{2}}$ is

**Options:**

- **(A)** 7.934
- **(B)** 8.934
- **(C)** 7.022
- **(D)** $8.866^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 7.934**

**Detailed Solution:**

Let $f(x) = x^{\dfrac{3}{2}}$

Let $x = 4$ and $\Delta x = -0.022$

$f(x) = 4^{\dfrac{3}{2}} = 8$

$f'(x) = \dfrac{3}{2} x^{\dfrac{1}{2}}$

$f'(4) = \dfrac{3}{2} (4)^{\dfrac{1}{2}} = 3$

Using the approximation formula $f(x + \Delta x) \approx f(x) + f'(x) \Delta x$

$f(3.978) \approx 8 + 3(-0.022)$

$f(3.978) \approx 8 - 0.066 = 7.934$

Answer: 7.934

</details>

---

### Q45. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The volume of a ball is increasing at the rate of $4 \pi \mathrm{cc} / \mathrm{sec}$. The rate of increase of the radius, when the volume is $288 \pi \mathrm{cc}$, is

**Options:**

- **(A)** $\dfrac{1}{6} \mathrm{~cm} / \mathrm{sec}$
- **(B)** $\dfrac{1}{36} \mathrm{~cm} / \mathrm{sec}$
- **(C)** $6 \mathrm{~cm} / \mathrm{sec}$
- **(D)** $36 \mathrm{~cm} / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{36} \mathrm{~cm} / \mathrm{sec}$**

**Detailed Solution:**

Let $V$ be the volume and $r$ be the radius of the ball.

$V = \dfrac{4}{3} \pi r^3$

Given $\dfrac{dV}{dt} = 4 \pi \text{ cc/sec}$ and $V = 288 \pi \text{ cc}$.

$\dfrac{4}{3} \pi r^3 = 288 \pi$

$r^3 = 216 \Rightarrow r = 6 \text{ cm}$

Differentiating $V$ with respect to $t$:

$\dfrac{dV}{dt} = 4 \pi r^2 \dfrac{dr}{dt}$

$4 \pi = 4 \pi (6)^2 \dfrac{dr}{dt}$

$\dfrac{dr}{dt} = \dfrac{1}{36} \text{ cm/sec}$

Answer: $\dfrac{1}{36} \mathrm{~cm} / \mathrm{sec}$

</details>

---

### Q46. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The approximate value of $x^3-2 x^2+3 x+2$ at $x=2.01$ is

**Options:**

- **(A)** 8.07
- **(B)** 8.27
- **(C)** 8.007
- **(D)** 8.17

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 8.07**

**Detailed Solution:**

Let $f(x) = x^3 - 2x^2 + 3x + 2$.

We need to find the approximate value of $f(x)$ at $x = 2.01$.

Let $x = 2$ and $\Delta x = 0.01$.

Using the approximation formula $f(x + \Delta x) \approx f(x) + f'(x) \Delta x$:

$f(2) = 2^3 - 2(2)^2 + 3(2) + 2 = 8 - 8 + 6 + 2 = 8$

Differentiating $f(x)$ with respect to $x$, we get:

$f'(x) = 3x^2 - 4x + 3$

$f'(2) = 3(2)^2 - 4(2) + 3 = 12 - 8 + 3 = 7$

Substituting the values in the approximation formula:

$f(2.01) \approx f(2) + f'(2) \Delta x$

$f(2.01) \approx 8 + 7(0.01) = 8 + 0.07 = 8.07$

Answer: 8.07

</details>

---

### Q47. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A point moves along the arc of parabola $y=2 x^2$. Its abscissa increases uniformly at the rate of 2 units $/ \mathrm{sec}$. At the instant, the point is passing through $(1,2)$, its distance from origin is increasing at the rate of

**Options:**

- **(A)** $\dfrac{36}{\sqrt{5}}$ units/sec.
- **(B)** $\dfrac{18}{\sqrt{5}}$ units $/ \mathrm{sec}$.
- **(C)** $\dfrac{36}{5}$ units/sec.
- **(D)** $\dfrac{18}{5}$ units / sec.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{18}{\sqrt{5}}$ units $/ \mathrm{sec}$.**

**Detailed Solution:**

Given $y = 2x^2$ and $\dfrac{dx}{dt} = 2$.

Differentiating with respect to $t$, we get $\dfrac{dy}{dt} = 4x \dfrac{dx}{dt}$.

At $x = 1$, $\dfrac{dy}{dt} = 4(1)(2) = 8$.

The distance of the point from the origin is $D = \sqrt{x^2 + y^2}$.

Differentiating with respect to $t$, we get $2D \dfrac{dD}{dt} = 2x \dfrac{dx}{dt} + 2y \dfrac{dy}{dt}$, which simplifies to $D \dfrac{dD}{dt} = x \dfrac{dx}{dt} + y \dfrac{dy}{dt}$.

At the point $(1, 2)$, $D = \sqrt{1^2 + 2^2} = \sqrt{5}$.

Substituting the values, we get $\sqrt{5} \dfrac{dD}{dt} = (1)(2) + (2)(8)$.

$\sqrt{5} \dfrac{dD}{dt} = 2 + 16 = 18$.

$\dfrac{dD}{dt} = \dfrac{18}{\sqrt{5}}$ units/sec.

Answer: $\dfrac{18}{\sqrt{5}}$ units $/ \mathrm{sec}$.

</details>

---

### Q48. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Water is running in a hemispherical bowl of radius 180 cm at the rate of 108 cubic decimeters per minute. How fast the water level is rising when depth of the water level in the bowl is 120 cm ? ( 1 decimeter $=10 \mathrm{~cm}$ )

**Options:**

- **(A)** $16 \pi \mathrm{~cm} / \mathrm{s}$
- **(B)** $\dfrac{16}{\pi} \mathrm{~cm} / \mathrm{s}$
- **(C)** $\dfrac{1}{16 \pi} \mathrm{~cm} / \mathrm{s}$
- **(D)** $\dfrac{\pi}{16} \mathrm{~cm} / \mathrm{s}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{16 \pi} \mathrm{~cm} / \mathrm{s}$**

**Detailed Solution:**

The volume $V$ of water in a hemispherical bowl of radius $R$ at a depth $h$ is given by the formula for the volume of a spherical cap:

$V = \dfrac{\pi h^2}{3}(3R - h)$

Differentiating both sides with respect to time $t$:

$\dfrac{dV}{dt} = \dfrac{\pi}{3} \left[ 2h(3R - h) \dfrac{dh}{dt} + h^2 \left( -\dfrac{dh}{dt} \right) \right]$

$\dfrac{dV}{dt} = \pi h(2R - h) \dfrac{dh}{dt}$

Given that the radius $R = 180$ cm, the depth $h = 120$ cm, and the rate of water flow $\dfrac{dV}{dt} = 108$ dm$^3$/min.

Since $1$ dm $= 10$ cm, $1$ dm$^3 = 1000$ cm$^3$.

$\dfrac{dV}{dt} = 108 \times 1000 = 108000$ cm$^3$/min.

Substituting the given values into the differentiated equation:

$108000 = \pi (120)(2(180) - 120) \dfrac{dh}{dt}$

$108000 = \pi (120)(360 - 120) \dfrac{dh}{dt}$

$108000 = \pi (120)(240) \dfrac{dh}{dt}$

$108000 = 28800 \pi \dfrac{dh}{dt}$

$\dfrac{dh}{dt} = \dfrac{108000}{28800 \pi} = \dfrac{1080}{288 \pi} = \dfrac{15}{4 \pi}$ cm/min.

To find the rate in cm/s, we divide by $60$:

$\dfrac{dh}{dt} = \dfrac{15}{4 \pi \times 60} = \dfrac{15}{240 \pi} = \dfrac{1}{16 \pi}$ cm/s.

Answer: $\dfrac{1}{16 \pi} \mathrm{~cm} / \mathrm{s}$

</details>

---

### Q49. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The approximate value of $(3.978)^{3 / 2}$ is

**Options:**

- **(A)** 7.096
- **(B)** 8.096
- **(C)** 7.934
- **(D)** 8.934

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7.934**

**Detailed Solution:**

Let $f(x) = x^{3/2}$.

We need to find the approximate value of $f(3.978)$.

Let $x = 4$ and $\Delta x = -0.022$.

Using the approximation formula $f(x + \Delta x) \approx f(x) + f'(x) \Delta x$:

$f(4) = 4^{3/2} = 8$

$f'(x) = \dfrac{3}{2} x^{1/2}$

$f'(4) = \dfrac{3}{2} (4)^{1/2} = 3$

$f(3.978) \approx 8 + 3(-0.022)$

$f(3.978) \approx 8 - 0.066 = 7.934$

Answer: 7.934

</details>

---

### Q50. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A square plate is contracting at the uniform rate $3 \mathrm{~cm}^2 / \mathrm{sec}$, then the rate at which the perimeter is decreasing, when the side of the square is 15 cm , is

**Options:**

- **(A)** $\dfrac{1}{5} \mathrm{~cm} / \mathrm{sec}$
- **(B)** $\dfrac{2}{5} \mathrm{~cm} / \mathrm{sec}$
- **(C)** $\dfrac{1}{10} \mathrm{~cm} / \mathrm{sec}$
- **(D)** $\dfrac{3}{10} \mathrm{~cm} / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{2}{5} \mathrm{~cm} / \mathrm{sec}$**

**Detailed Solution:**

Let the side of the square be $x$.

Area of the square, $A = x^2$

Differentiating with respect to time $t$, we get $\dfrac{dA}{dt} = 2x \dfrac{dx}{dt}$

Given that the area is contracting at the rate of $3 \mathrm{~cm}^2/\mathrm{sec}$, $\dfrac{dA}{dt} = -3$

$-3 = 2x \dfrac{dx}{dt} \Rightarrow \dfrac{dx}{dt} = \dfrac{-3}{2x}$

Perimeter of the square, $P = 4x$

Differentiating with respect to time $t$, we get $\dfrac{dP}{dt} = 4 \dfrac{dx}{dt}$

Substituting the value of $\dfrac{dx}{dt}$, we get $\dfrac{dP}{dt} = 4 \left( \dfrac{-3}{2x} \right) = \dfrac{-6}{x}$

When $x = 15 \mathrm{~cm}$, $\dfrac{dP}{dt} = \dfrac{-6}{15} = -\dfrac{2}{5} \mathrm{~cm}/\mathrm{sec}$

The negative sign indicates that the perimeter is decreasing. Therefore, the rate of decrease of the perimeter is $\dfrac{2}{5} \mathrm{~cm}/\mathrm{sec}$.

Answer: $\dfrac{2}{5} \mathrm{~cm} / \mathrm{sec}$

</details>

---

### Q51. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The population of a town increases at a rate proportional to the population at that time. If the population increases from 40 thousand to 80 thousand in 40 years, then the population in another 40 years will be

**Options:**

- **(A)** 180000
- **(B)** 128000
- **(C)** 160000
- **(D)** 256000

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 160000**

**Detailed Solution:**

Let $P$ be the population at time $t$.

$\dfrac{dP}{dt} = kP$

$\int \dfrac{dP}{P} = \int k dt$

$\ln P = kt + C$

$P = P_0 e^{kt}$

Given $P_0 = 40000$ at $t = 0$.

At $t = 40$, $P = 80000$.

$80000 = 40000 e^{40k}$

$e^{40k} = 2$

We need to find the population in another $40$ years, i.e., at $t = 80$.

$P = 40000 e^{80k} = 40000 (e^{40k})^2$

$P = 40000 (2)^2 = 160000$

Answer: 160000

</details>

---

### Q52. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A ladder 5 m long rests against a vertical wall. If its top slides downwards at the rate of $10 \mathrm{~cm} / \mathrm{sec}$., then the foot of the ladder is sliding at the rate of _______ $\mathrm{m} / \mathrm{sec}$, when it is 4 m away from the wall.

**Options:**

- **(A)** 0.75
- **(B)** 7.5
- **(C)** 0.0075
- **(D)** 0.075

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0.075**

**Detailed Solution:**

Let $x$ be the distance of the foot of the ladder from the wall and $y$ be the height of the top of the ladder from the ground.

From the given information, $x^2 + y^2 = 5^2 = 25$.

Differentiating with respect to $t$, we get:

$2x \dfrac{dx}{dt} + 2y \dfrac{dy}{dt} = 0$

$x \dfrac{dx}{dt} + y \dfrac{dy}{dt} = 0$

We are given $\dfrac{dy}{dt} = -10 \text{ cm/sec} = -0.1 \text{ m/sec}$.

When $x = 4 \text{ m}$, $y = \sqrt{25 - 4^2} = 3 \text{ m}$.

Substituting these values into the differentiated equation:

$4 \dfrac{dx}{dt} + 3(-0.1) = 0$

$4 \dfrac{dx}{dt} = 0.3$

$\dfrac{dx}{dt} = \dfrac{0.3}{4} = 0.075 \text{ m/sec}$

The foot of the ladder is sliding at the rate of $0.075 \text{ m/sec}$.

Answer: 0.075

</details>

---

### Q53. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The approximate value of $\tan ^{-1}(0.999)$ is (use $\pi=3.1415$ )

**Options:**

- **(A)** 0.7843
- **(B)** 0.7849
- **(C)** 0.7847
- **(D)** 0.7851

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0.7849**

**Detailed Solution:**

Let $f(x) = \tan^{-1}(x)$

Using the first-order approximation $f(x + \Delta x) \approx f(x) + f'(x) \Delta x$

Let $x = 1$ and $\Delta x = -0.001$

$f(1) = \tan^{-1}(1) = \dfrac{\pi}{4}$

$f'(x) = \dfrac{1}{1 + x^2} \Rightarrow f'(1) = \dfrac{1}{2} = 0.5$

$f(0.999) \approx \dfrac{\pi}{4} + 0.5(-0.001) = \dfrac{\pi}{4} - 0.0005$

Given $\pi = 3.1415$, $\dfrac{\pi}{4} = 0.785375$

$f(0.999) \approx 0.785375 - 0.0005 = 0.784875$

Rounding to four decimal places, the approximate value is $0.7849$

Answer: 0.7849

</details>

---

### Q54. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A wet substance in the open air loses its moisture at a rate proportional to the moisture content. If a sheet hung in the open air loses half its moisture during the first hour, then the time t , in which $99 \%$ of the moisture will be lost, is

**Options:**

- **(A)** $\dfrac{2 \log 10}{\log 2}$
- **(B)** $\dfrac{\log 10}{\log 2}$
- **(C)** $\dfrac{3 \log 10}{\log 2}$
- **(D)** $\dfrac{1}{2} \dfrac{\log 10}{\log 2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2 \log 10}{\log 2}$**

**Detailed Solution:**

Let $M$ be the moisture content at time $t$.

$\dfrac{dM}{dt} = -kM$

$\int \dfrac{dM}{M} = -k \int dt$

$M = M_0 e^{-kt}$

At $t = 1$, $M = \dfrac{M_0}{2}$:

$\dfrac{M_0}{2} = M_0 e^{-k}$

$e^{-k} = \dfrac{1}{2} \Rightarrow k = \log_e 2$

When $99\%$ of the moisture is lost, the remaining moisture is $1\%$, so $M = \dfrac{M_0}{100}$.

$\dfrac{M_0}{100} = M_0 e^{-kt}$

$e^{-kt} = \dfrac{1}{100}$

$-kt = \log_e \left(\dfrac{1}{100}\right) = -2 \log_e 10$

$t \log_e 2 = 2 \log_e 10$

$t = \dfrac{2 \log 10}{\log 2}$

Answer: $\dfrac{2 \log 10}{\log 2}$

</details>

---

### Q55. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If a body cools from $80^{\circ} \mathrm{C}$ to $60^{\circ} \mathrm{C}$ in the room temperature of $30^{\circ} \mathrm{C}$ in 30 min , then the temperature of a body after one hour is

**Options:**

- **(A)** $42^{\circ} \mathrm{C}$
- **(B)** $24^{\circ} \mathrm{C}$
- **(C)** $48^{\circ} \mathrm{C}$
- **(D)** $56^{\circ} \mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $48^{\circ} \mathrm{C}$**

**Detailed Solution:**

Using Newton's law of cooling, the temperature $T$ at time $t$ is given by:

$T = T_0 + (T_1 - T_0)e^{-kt}$

where $T_0$ is the room temperature and $T_1$ is the initial temperature.

Given $T_1 = 80^{\circ}\mathrm{C}$, $T_0 = 30^{\circ}\mathrm{C}$, and $T = 60^{\circ}\mathrm{C}$ at $t = 30$ min:

$60 = 30 + (80 - 30)e^{-30k}$

$30 = 50e^{-30k}$

$e^{-30k} = \dfrac{3}{5}$

We need to find the temperature $T'$ after one hour, which is $t = 60$ min from the start:

$T' = 30 + (80 - 30)e^{-60k}$

$T' = 30 + 50(e^{-30k})^2$

Substituting the value of $e^{-30k}$:

$T' = 30 + 50\left(\dfrac{3}{5}\right)^2$

$T' = 30 + 50\left(\dfrac{9}{25}\right)$

$T' = 30 + 18 = 48^{\circ}\mathrm{C}$

Answer: $48^{\circ} \mathrm{C}$

</details>

---

### Q56. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The approximate value of $\cos(30^\circ 30')$ is, given that $1^\circ = 0.0175^c$ and $\cos 30^\circ = 0.8660$

**Options:**

- **(A)** 0.8778
- **(B)** 0.7666
- **(C)** 0.7916
- **(D)** 0.8616

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0.8616**

**Detailed Solution:**

Let $f(x) = \cos x$

We need to find the value of $f(x + \Delta x)$ where $x = 30^\circ$ and $\Delta x = 30' = 0.5^\circ$

Converting $\Delta x$ into radians:

$\Delta x = 0.5 \times 0.0175 = 0.00875$ radians

Using the approximation formula:

$f(x + \Delta x) \approx f(x) + f'(x) \Delta x$

Here, $f'(x) = -\sin x$

Substituting the values:

$\cos(30^\circ 30') \approx \cos 30^\circ - \sin 30^\circ \times \Delta x$

$\cos(30^\circ 30') \approx 0.8660 - 0.5 \times 0.00875$

$\cos(30^\circ 30') \approx 0.8660 - 0.004375$

$\cos(30^\circ 30') \approx 0.861625$

Rounding to four decimal places, we get $0.8616$

Answer: 0.8616

</details>

---

### Q57. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A bullet is shot horizontally and its distance S cm at time t second is given by $\mathrm{S}=1200 \mathrm{t}-15 \cdot \mathrm{t}^2$, then the distance covered by the bullet when it comes to the rest, is

**Options:**

- **(A)** 12000 cm
- **(B)** 24000 cm
- **(C)** 1200 cm
- **(D)** 2400 cm

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 24000 cm**

**Detailed Solution:**

Given $S = 1200t - 15t^2$

Velocity $v = \dfrac{dS}{dt} = 1200 - 30t$

The bullet comes to rest when $v = 0$

$1200 - 30t = 0 \Rightarrow t = 40$ s

Distance covered in $40$ s is:

$S = 1200(40) - 15(40)^2$

$S = 48000 - 15(1600)$

$S = 48000 - 24000 = 24000$ cm

Answer: 24000 cm

</details>

---

### Q58. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A stone is dropped into a quiet lake and waves move in circles at speed of $8 \mathrm{~cm} / \mathrm{sec}$. At the instant when the radius of the circular wave is 12 cm . how fast is the enclosed area increasing?

**Options:**

- **(A)** $180 \pi \mathrm{~cm}^2 / \mathrm{sec}$
- **(B)** $196 \pi \mathrm{~cm}^2 / \mathrm{sec}$
- **(C)** $192 \pi \mathrm{~cm}^2 / \mathrm{sec}$
- **(D)** $200 \pi \mathrm{~cm}^2 / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $192 \pi \mathrm{~cm}^2 / \mathrm{sec}$**

**Detailed Solution:**

Let $r$ be the radius of the circular wave and $A$ be the enclosed area.

Given that the waves move in circles at a speed of $8 \text{ cm/sec}$, the rate of change of the radius is $\dfrac{dr}{dt} = 8 \text{ cm/sec}$.

The area of the circle is given by $A = \pi r^2$.

Differentiating with respect to time $t$, we get:

$\dfrac{dA}{dt} = 2\pi r \dfrac{dr}{dt}$

At the instant when $r = 12 \text{ cm}$, substituting the values gives:

$\dfrac{dA}{dt} = 2\pi (12)(8) = 192\pi \text{ cm}^2/\text{sec}$

Answer: $192 \pi \mathrm{~cm}^2 / \mathrm{sec}$

</details>

---

### Q59. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The approximate value of $\sqrt[3]{0 \cdot 026}$ is

**Options:**

- **(A)** 0.2762
- **(B)** 0.2963
- **(C)** 0.2632
- **(D)** 0.2692

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0.2963**

**Detailed Solution:**

Let $y = x^{1/3}$. We need to find the value of $y$ when $x = 0.026$.

Let $x = 0.027$ and $\Delta x = -0.001$.

For $x = 0.027$, $y = (0.027)^{1/3} = 0.3$.

Differentiating $y$ with respect to $x$, we get:

$\dfrac{dy}{dx} = \dfrac{1}{3} x^{-2/3} = \dfrac{1}{3(0.027)^{2/3}} = \dfrac{1}{3(0.09)} = \dfrac{1}{0.27} = \dfrac{100}{27}$

Using the approximation $\Delta y \approx \dfrac{dy}{dx} \Delta x$:

$\Delta y \approx \dfrac{100}{27} \times (-0.001) = -\dfrac{0.1}{27} = -\dfrac{1}{270} \approx -0.0037$

The approximate value of $\sqrt[3]{0.026}$ is:

$y + \Delta y \approx 0.3 - 0.0037 = 0.2963$

Answer: 0.2963

</details>

---

### Q60. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A spherical metal ball at $80^{\circ} \mathrm{C}$ cools in 5 minutes to $60^{\circ} \mathrm{C}$, in surrounding temperature of $20^{\circ} \mathrm{C}$, then the temperature of the ball after 20 minutes is approximately

**Options:**

- **(A)** $(8.15)^{\circ} \mathrm{C}$
- **(B)** $(11.85)^{\circ} \mathrm{C}$
- **(C)** $(28.15)^{\circ} \mathrm{C}$
- **(D)** $(31.85)^{\circ} \mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(31.85)^{\circ} \mathrm{C}$**

**Detailed Solution:**

According to Newton's law of cooling, the temperature $T$ of a body at time $t$ is given by:

$T(t) = T_s + (T_0 - T_s) e^{-kt}$

where $T_s$ is the surrounding temperature and $T_0$ is the initial temperature.

Given $T_0 = 80^{\circ} \mathrm{C}$, $T_s = 20^{\circ} \mathrm{C}$, and $T(5) = 60^{\circ} \mathrm{C}$ at $t = 5$ minutes:

$60 = 20 + (80 - 20) e^{-5k}$

$40 = 60 e^{-5k}$

$e^{-5k} = \dfrac{2}{3}$

We need to find the temperature after 20 minutes, which corresponds to $t = 20$:

$T(20) = 20 + (80 - 20) e^{-20k}$

$T(20) = 20 + 60 (e^{-5k})^4$

Substituting the value of $e^{-5k}$:

$T(20) = 20 + 60 \left(\dfrac{2}{3}\right)^4$

$T(20) = 20 + 60 \times \dfrac{16}{81}$

$T(20) = 20 + \dfrac{320}{27}$

$T(20) \approx 20 + 11.85$

$T(20) \approx 31.85^{\circ} \mathrm{C}$

Answer: $(31.85)^{\circ} \mathrm{C}$

</details>

---

### Q61. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{P}(x)$ be a polynomial of degree 2 , with $\mathrm{P}(2)=-1, \mathrm{P}^{\prime}(2)=0, \mathrm{P}^{\prime \prime}(2)=2$, then $\mathrm{P}(1.001)$ is

**Options:**

- **(A)** 0.002
- **(B)** -0.002
- **(C)** 0.004
- **(D)** -0.004

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -0.002**

**Detailed Solution:**

$\begin{aligned}
& \text { Let } \mathrm{P}(x)=\mathrm{a} x^2+\mathrm{b} x+\mathrm{c} \\
& \Rightarrow \mathrm{P}^{\prime}(x)=2 \mathrm{a} x+\mathrm{b} \\
& \Rightarrow \mathrm{P}^{\prime \prime}(x)=2 \mathrm{a} \\
& \mathrm{P}^{\prime \prime}(2)=2 \mathrm{a} \\
& \Rightarrow 2=2 \mathrm{a} \\
& \Rightarrow \mathrm{a}=1 \\
& \mathrm{P}^{\prime}(2)=2 \mathrm{a}(2)+\mathrm{b} \\
& \Rightarrow 0=4 \mathrm{a}+\mathrm{b} \\
& \Rightarrow 0=4(1)+\mathrm{b} \\
& \Rightarrow \mathrm{b}=-4 \\
& \mathrm{P}(2)=\mathrm{a}(2)^2+\mathrm{b}(2)+\mathrm{c} \\
& \Rightarrow-1=4 \mathrm{a}+2 \mathrm{~b}+\mathrm{c} \\
& \Rightarrow-1=4(1)+2(-4)+\mathrm{c} \\
& \Rightarrow \mathrm{c}=3 \\
& \mathrm{P}(x)=x^2-4 x+3 \\
& \Rightarrow \mathrm{P}^{\prime}(x)=2 x-4 \\
& x=1.001=1+0.001=\mathrm{a}+\mathrm{h}
\end{aligned}$
Here, $\mathrm{a}=1, \mathrm{~h}=0.001$
$\begin{gathered}
\mathrm{P}(\mathrm{a})=\mathrm{P}(1)=1-4+3=0 \\
\mathrm{P}^{\prime}(\mathrm{a})=\mathrm{P}^{\prime}(1)=2-4=-2
\end{gathered}$
$\therefore \quad \mathrm{P}(1.001)=0+(0.001)(-2)=-0.002$

</details>

---

### Q62. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The diagonal of a square is changing at the rate of $0.5 \mathrm{~cm} / \mathrm{sec}$. Then the rate of change of area when the area is $400 \mathrm{~cm}^2$ is equal to

**Options:**

- **(A)** $20 \sqrt{2} \mathrm{~cm}^2 / \mathrm{sec}$
- **(B)** $10 \sqrt{2} \mathrm{~cm}^2 / \mathrm{sec}$
- **(C)** $\frac{1}{10 \sqrt{2}} \mathrm{~cm}^2 / \mathrm{sec}$
- **(D)** $\frac{10}{\sqrt{2}} \mathrm{~cm}^2 / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $10 \sqrt{2} \mathrm{~cm}^2 / \mathrm{sec}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/l5VcQSw4PtmM_coCfl2CWKfM8L5rO84gFiLK0bZ9n9c.original.fullsize.png">

$\begin{array}{ll} 
& \frac{\mathrm{d} x}{\mathrm{dt}}=0.5 \mathrm{~cm} / \mathrm{sec} \\
\therefore \quad & \text { Area }=\frac{x^2}{2} \\
\therefore \quad & \frac{\mathrm{dA}}{\mathrm{dt}}=\frac{2 x}{2} \cdot \frac{\mathrm{d} x}{\mathrm{dt}}=x \frac{\mathrm{d} x}{\mathrm{dt}}=\frac{1}{2} x
\end{array}$
$\begin{aligned} \therefore \quad\left[\frac{\mathrm{dA}}{\mathrm{dt}}\right]_{\mathrm{A}=400} & =\frac{1}{2} \sqrt{800} \quad \ldots\left[\begin{array}{l}\because \mathrm{A}=400 \mathrm{~cm}^2 \\ x=\sqrt{800} \mathrm{~cm}\end{array}\right] \\ & =10 \sqrt{2} \mathrm{~cm}^2 / \mathrm{sec}\end{aligned}$

</details>

---

### Q63. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $B \equiv(0,3)$ and $C \equiv(4,0)$. The point $A$ is moving on the line $y=2 x$ at the rate of 2 units/second. The area of $\triangle \mathrm{ABC}$ is increasing at the rate of

**Options:**

- **(A)** $\frac{11}{\sqrt{5}}$ (units $)^2 / \mathrm{sec}$
- **(B)** $\frac{11}{5}$ (units) $)^2 / \mathrm{sec}$
- **(C)** $\frac{43}{\sqrt{5}}$ (units $)^2 / \mathrm{sec}$
- **(D)** $\frac{13}{5}$ (units) $)^2 / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{11}{\sqrt{5}}$ (units $)^2 / \mathrm{sec}$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{A}=(\mathrm{h}, 2 \mathrm{~h}) \\ & \quad \mathrm{OA}=\sqrt{\mathrm{h}^2+4 \mathrm{~h}^2}=\sqrt{5} \mathrm{~h} \\ & \therefore \quad \frac{\mathrm{d}(\mathrm{OA})}{\mathrm{dt}}=\sqrt{5} \frac{\mathrm{dh}}{\mathrm{dt}} \\ & \Rightarrow 2=\sqrt{5} \frac{\mathrm{dh}}{\mathrm{dt}} \\ & \Rightarrow \frac{\mathrm{dh}}{\mathrm{dt}}=\frac{2}{\sqrt{5}}\end{aligned}$
$\begin{aligned} \alpha & =\mathrm{A}(\triangle \mathrm{ABC})=\frac{1}{2}\left|\begin{array}{ccc}\mathrm{h} & 2 \mathrm{~h} & 1 \\ 0 & 3 & 1 \\ 4 & 0 & 1\end{array}\right| \\ & =\frac{1}{2}(3 \mathrm{~h}+8 \mathrm{~h}-12) \\ & =\frac{11 \mathrm{~h}-12}{2} \\ \therefore \quad \frac{\mathrm{d} \alpha}{\mathrm{dt}} & =\frac{11}{2} \cdot \frac{\mathrm{dh}}{\mathrm{dt}} \\ & =\frac{11}{2} \cdot \frac{2}{\sqrt{5}} \\ & =\frac{11}{\sqrt{5}}(\text { units })^2 / \mathrm{sec}\end{aligned}$

</details>

---

### Q64. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Water is running in a hemispherical bowl of radius $180 \mathrm{~cm}$ at the rate of 108 cubic decimetres per minute. How fast the water level is rising when depth of the water level in the bowl is $120 \mathrm{~cm}$ ?
$(1$ decimeter $=10 \mathrm{~cm})$

**Options:**

- **(A)** $16 \pi \mathrm{cm} / \mathrm{sec}$
- **(B)** $\frac{16}{\pi} \mathrm{cm} / \mathrm{sec}$
- **(C)** $\frac{1}{16 \pi} \mathrm{cm} / \mathrm{sec}$
- **(D)** $\frac{\pi}{16} \mathrm{~cm} / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{16 \pi} \mathrm{cm} / \mathrm{sec}$**

**Detailed Solution:**

Radius of hemispherical bowl $(\mathrm{r})=180 \mathrm{~cm}$ Rate of flow $\left(\frac{\mathrm{dV}}{\mathrm{dt}}\right)=108 \mathrm{dm}^3 / \mathrm{min}$
$\begin{aligned} & =108000 \mathrm{~cm}^3 / \mathrm{min} \\ & =\frac{108000}{60} \mathrm{~cm}^3 / \mathrm{sec} \\ & =1800 \mathrm{~cm}^3 / \mathrm{sec}\end{aligned}$
Let depth of water in bowl be $x$.
$\therefore \quad$ Volume of water in hemispherical.
$\begin{aligned} & \text { bowl }(\mathrm{V})=\frac{\pi}{3} x^2(3 \mathrm{r}-x) \\ & \mathrm{V}=\frac{\pi}{3} x^2(3 \times 180-x)\end{aligned}$
$\therefore \quad \mathrm{V}=180 \pi x^2-\frac{\pi}{3} x^3$
Differentiating w.r.t. $x$, we get
$\frac{\mathrm{dV}}{\mathrm{dt}}=360 \pi x \frac{\mathrm{d} x}{\mathrm{dt}}-\pi x^2 \frac{\mathrm{d} x}{\mathrm{dt}}$
$\left.\frac{\mathrm{dV}}{\mathrm{dt}}\right|_{x=120}=\frac{\mathrm{d} x}{\mathrm{dt}}\left(360 \pi \times 120-120^2 \pi\right)$
$\therefore \quad 1800=\frac{\mathrm{d} x}{\mathrm{dt}}\left(360 \pi \times 120-120^2 \pi\right)$
$\therefore \quad 15=\frac{\mathrm{d} x}{\mathrm{dt}}(360 \pi-120 \pi)$
$\frac{\mathrm{d} x}{\mathrm{dt}}=\frac{15}{240 \pi}$
$=\frac{1}{16 \pi} \mathrm{cm} / \mathrm{sec}$

</details>

---

### Q65. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A right circular cone has height $9 \mathrm{~cm}$ and radius of base $5 \mathrm{~cm}$. It is inverted and water is poured into it. If at any instant, the water level rises at the rate $\frac{\pi}{\mathrm{A}} \mathrm{cm} / \mathrm{sec}$. where $\mathrm{A}$ is area of the water surface at that instant, then cone is completely filled in

**Options:**

- **(A)** $70 \mathrm{sec}$.
- **(B)** $75 \mathrm{sec}$.
- **(C)** $72 \mathrm{sec}$.
- **(D)** $77 \mathrm{sec}$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $75 \mathrm{sec}$.**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/EacbuPluS0FHXvy3teJp6mFUFacYeP0-uiHv4ijKE1I.original.fullsize.png">


For the conical vessel, $\mathrm{h}=9 \mathrm{~cm}, \mathrm{r}=5 \mathrm{~cm}$
$\therefore \quad$ Full volume of the vessel,
$$
\begin{aligned}
\mathrm{V} & =\frac{1}{3} \pi \mathrm{r}^2 \mathrm{~h} \\
& =\frac{1}{3} \pi \times 25 \times 9 \\
& =75 \pi \mathrm{cm}^3
\end{aligned}
$$
Now, $\frac{\mathrm{h}}{\mathrm{r}}=\frac{9}{5}$
$$
\begin{aligned}
& \therefore \quad \mathrm{r}=\frac{5 \mathrm{~h}}{9} \\
& \therefore \quad \mathrm{A}=\pi \mathrm{r}^2=\pi \frac{25 \mathrm{~h}^2}{81}
\end{aligned}
$$
According to the given condition, $\frac{\mathrm{dh}}{\mathrm{dt}}=\frac{\pi}{\mathrm{A}}=\pi \frac{81}{\pi 25 \mathrm{~h}^2}=\frac{81}{25 \mathrm{~h}^2}$
$\therefore \quad h^2 \mathrm{dh}=\frac{81}{25} \mathrm{dt}$
Integrating on both sides, we get
$$
\begin{aligned}
& \frac{\mathrm{h}^3}{3}=\frac{81}{25} \mathrm{t}+\mathrm{c}_1 \\
\therefore \quad & \mathrm{h}^3=\frac{243}{25} \mathrm{t}+\mathrm{c}, \text { where } \mathrm{c}=3 \mathrm{c}_1
\end{aligned}
$$
Naturally, $\mathrm{h}=0$, when $\mathrm{t}=0$ and hence, $\mathrm{c}=0$
$$
\begin{aligned}
\therefore \quad \mathrm{h}^3 & =\frac{243}{25} \mathrm{t} \\
\therefore \quad \mathrm{V} & =\frac{1}{3} \pi \mathrm{r}^2 \mathrm{~h} \\
& =\frac{1}{3} \pi \frac{25 \mathrm{~h}^2}{81} \mathrm{~h} \\
& =\frac{25}{243} \pi \mathrm{h}^3 \\
& =\frac{25}{243} \pi \frac{243}{25} \mathrm{t} \\
\therefore \quad \mathrm{V} & =\pi \mathrm{t}
\end{aligned}
$$
But volume of vessel, $\mathrm{V}=75 \pi$
$$
\begin{array}{ll}
\therefore & \pi \mathrm{t}=75 \pi \\
\therefore & \mathrm{t}=75 \text { seconds. }
\end{array}
$$

</details>

---

### Q66. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Water flows from the base of rectangular tank, of depth 16 meters. The rate of flow of the water is proportional to the square root of depth at any time $\mathrm{t}$. If depth is $4 \mathrm{~m}$ when $\mathrm{t}=2$ hours, then after 3.5 hours the depth (in meters) is

**Options:**

- **(A)** $0$
- **(B)** $0.25$
- **(C)** $0.5$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.25$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/7aHEShuqekarzkr2k6KiUkeB4U77lMRAHF2UcE6x0po.original.fullsize.png">

Given that $\frac{\mathrm{d} x}{\mathrm{dt}} \propto \sqrt{x}$
$\therefore \quad \frac{\mathrm{d} x}{\mathrm{dt}}=\mathrm{a} \sqrt{x}$, for real number a
$\therefore \quad \int \frac{\mathrm{d} x}{\sqrt{x}}=\int \mathrm{adt}$
$\therefore \quad 2 \sqrt{x}=\mathrm{at}+\mathrm{c}$
When $\mathrm{t}=0, x=16$
$\therefore \quad$ (i) $\Rightarrow \mathrm{c}=8$
$\therefore \quad$ (i) becomes $2 \sqrt{x}=$ at +8
When $\mathrm{t}=2, x=4$
$\therefore \quad$ (ii) $\Rightarrow \mathrm{a}=-2$
$\therefore \quad$ (ii) becomes $2 \sqrt{x}=-2 t+8$
$\therefore \quad$ when $\mathrm{t}=3.5$
(iii) $\Rightarrow x=0.25 \mathrm{~m}$

</details>

---

### Q67. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A tank with a rectangular base and rectangular sides, open at the top is to be constructed so that its depth is 4 meter and volume is 36 cubic meters. If building of the tank costs $₹ 100$ per square meter for the base and $₹ 50$ per square meter for the sides, then the cost of least expensive tank is

**Options:**

- **(A)** $₹ 3000$
- **(B)** $₹ 3300$
- **(C)** $₹ 2400$
- **(D)** $₹ 3500$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $₹ 3300$**

**Detailed Solution:**

Let length and breadth of the tank be ' $x$ ' $\mathrm{m}$ and ' $y$ ' $m$ respectively.

Height of the tank is $4 \mathrm{~m}$.
Volume $=36 \mathrm{~m}^3$
$$
\begin{array}{ll}
\therefore & 4 x y=36 \\
\therefore & x y=9 \\
\therefore & y=\frac{9}{x}
\end{array}
$$
$\therefore \quad$ Total area of the tank including sides and base $=x y+2(4 x)+2(4 y)$
....[From (i) and (ii)]
$\therefore \quad \mathrm{f}(x)=9+8 x+8\left(\frac{9}{x}\right)$
$$
=9+8 x+\frac{72}{x}
$$
$$
\therefore \quad \mathrm{f}^{\prime}(x)=8-\frac{72}{x^2}
$$
$\therefore \quad \mathrm{f}^{\prime}(x)=0 \Rightarrow x=3$
$$
\Rightarrow y=3
$$
$\therefore \quad$ Required cost $=100 \times(3 \times 3)+50$
$$
\begin{aligned}
& \times(2 \times 4 \times 3+2 \times 4 \times 3) \\
= & 900+2400 \\
= & ₹ 3300
\end{aligned}
$$

</details>

---

### Q68. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A poster is to be printed on a rectangular sheet of paper of area $18 \mathrm{~m}^2$. The margins at the top and bottom of $75 \mathrm{~cm}$ each and at the sides $50 \mathrm{~cm}$ each are to be left. Then the dimensions i.e. height and breadth of the sheet, so that the space available for printing is maximum, are respectively.

**Options:**

- **(A)** $2 \sqrt{3} \mathrm{~m}, 3 \sqrt{3} \mathrm{~m}$
- **(B)** $3 \sqrt{3} \mathrm{~m}, 2 \sqrt{3} \mathrm{~m}$
- **(C)** $3 \mathrm{~m}, 6 \mathrm{~m}$
- **(D)** $6 \mathrm{~m}, 3 \mathrm{~m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 \sqrt{3} \mathrm{~m}, 2 \sqrt{3} \mathrm{~m}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/3U80ui6ARx2YWMHPRMOprnDUK7Z0LYe3gZ6jdTYpPxo.original.fullsize.png">

Let height and breadth of the sheet be ' $y$ ' $\mathrm{m}$ and ' $x$ ' $\mathrm{m}$ respectively.
$$
\begin{aligned}
& \therefore \quad x y=180000 \mathrm{~cm}^2 \\
& \therefore \quad y=\frac{180000}{x}
\end{aligned}
$$
$\therefore \quad$ The area available for printing is
$$
\begin{aligned}
\mathrm{A} & =(y-150)(x-100) \\
& =\left(\frac{180000}{x}-150\right)(x-100) \\
& =180000-\frac{18000000}{x}-150 x-15000 \\
& =165000-150 x-\frac{18000000}{x} \\
\therefore \quad \frac{\mathrm{dA}}{\mathrm{d} x} & =0-150+\frac{18000000}{x^2} \\
\therefore \quad \frac{\mathrm{dA}}{\mathrm{d} x} & =0 \Rightarrow x^2=\frac{18000000}{150}=120000 \\
\Rightarrow x=200 \sqrt{3} \mathrm{~cm} & \Rightarrow y=\frac{180000}{200 \sqrt{3}}=300 \sqrt{3} \mathrm{~cm}
\end{aligned}
$$

Now, $\frac{\mathrm{d}^2 \mathrm{~A}}{\mathrm{~d} x^2}=\frac{-36000000}{x^3}$
$\therefore \quad$ At $x=200 \sqrt{3} \mathrm{~cm}, \frac{\mathrm{d}^2 \mathrm{~A}}{\mathrm{~d} x^2} < 0$
$\therefore \quad$ Area is maximum at $x=200 \sqrt{3} \mathrm{~cm}$ and $\begin{aligned} y & =300 \sqrt{3} \mathrm{~cm} \\ \therefore \quad y & =3 \sqrt{3} \mathrm{~m} \text { and } x=2 \sqrt{3} \mathrm{~m}\end{aligned}$

</details>

---

### Q69. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the surface area of a spherical balloon of radius $6 \mathrm{~cm}$ is increasing at the rate $2 \mathrm{~cm}^2 / \mathrm{sec}$, then the rate of increase in its volume in $\mathrm{cm}^3 / \mathrm{sec}$ is

**Options:**

- **(A)** $16$
- **(B)** $6$
- **(C)** $12$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6$**

**Detailed Solution:**

Surface area, $S=4 \pi r^2$
$\begin{aligned}
& \therefore \quad \frac{\mathrm{dS}}{\mathrm{dt}}=8 \pi \mathrm{r} \frac{\mathrm{dr}}{\mathrm{dt}} \\
& \Rightarrow 2=8 \pi \mathrm{r} \frac{\mathrm{dr}}{\mathrm{dt}} \\
& \Rightarrow \frac{\mathrm{dr}}{\mathrm{dt}}=\frac{1}{4 \pi \mathrm{r}}...(i) \\
& \text { Volume, } V=\frac{4}{3} \pi r^3 \\
& \therefore \quad \frac{\mathrm{dV}}{\mathrm{dt}}=\frac{4}{3} \times 3 \pi \mathrm{r}^2 \times \frac{\mathrm{dr}}{\mathrm{dt}} \\
& =4 \pi r^2 \times \frac{1}{4 \pi r}... [From (i)] \\
& =\mathrm{r} \\
& =6 \mathrm{~cm}^3 / \mathrm{sec} \\
&
\end{aligned}$

</details>

---

### Q70. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A kite is $120 \mathrm{~m}$ high and $130 \mathrm{~m}$ of string is out. If the kite is moving away horizontally at the rate of $39 \mathrm{~m} / \mathrm{sec}$, then the rate at which the string is being out, is

**Options:**

- **(A)** $12 \mathrm{~m} / \mathrm{sec}$.
- **(B)** $15 \mathrm{~m} / \mathrm{sec}$.
- **(C)** $18 \mathrm{~m} / \mathrm{sec}$.
- **(D)** $20 \mathrm{~m} / \mathrm{sec}$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $15 \mathrm{~m} / \mathrm{sec}$.**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/XMh-3oePJ9QjPlheliKPjTVrzT9okNSPDN5s_7jjbp4.original.fullsize.png">

Let 'P' be the position of the kite and PR be the string.
Let $\mathrm{QR}=x$ and $\mathrm{PR}=y$
By Pythagoras theorem,
$\begin{aligned}
& -\mathrm{PR}^2=\mathrm{PQ}^2+\mathrm{QR}^2 \\
& \Rightarrow y^2=(120)^2+x^2... (i)
\end{aligned}$
Differentiating w.r.t.t, we get
$\begin{aligned}
& 2 y \frac{\mathrm{d} y}{\mathrm{dt}}=2 x \frac{\mathrm{d} x}{\mathrm{dt}} \\
& \Rightarrow y \frac{\mathrm{d} y}{\mathrm{dt}}=x \frac{\mathrm{d} x}{\mathrm{dt}}... (ii)
\end{aligned}$
Now, kite is moving away horizontally at the rate of $39 \mathrm{~m} / \mathrm{sec}$.
$\begin{aligned}
\therefore \quad & \frac{\mathrm{d} x}{\mathrm{dt}}=39 \mathrm{~m} / \mathrm{sec} \\
& \text { From (i), } \\
& (130)^2=(120)^2+x^2 \\
\Rightarrow & x^2=16900-14400 \\
\Rightarrow & x^2=2500 \\
\Rightarrow & x=50 \\
& \text { From (ii), } \\
& 130 \frac{\mathrm{d} y}{\mathrm{dt}}=50 \times 39 \\
\therefore \quad & \frac{\mathrm{d} y}{\mathrm{dt}}=\frac{50 \times 39}{130}=15 \mathrm{~m} / \mathrm{sec}
\end{aligned}$

</details>

---

### Q71. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A ladder of length $17 \mathrm{~m}$ rests with one end against a vertical wall and the other on the level ground. If the lower end slips away at the rate of $1 \mathrm{~m} / \mathrm{sec}$., then when it is $8 \mathrm{~m}$ away from the wall, its upper end is coming down at the rate of

**Options:**

- **(A)** $\frac{5}{8} \mathrm{~m} / \mathrm{sec}$.
- **(B)** $\frac{8}{15} \mathrm{~m} / \mathrm{sec}$.
- **(C)** $\frac{-8}{15} \mathrm{~m} / \mathrm{sec}$.
- **(D)** $\frac{15}{8} \mathrm{~m} / \mathrm{sec}$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{8}{15} \mathrm{~m} / \mathrm{sec}$.**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/giaJ43zBv8W7yF1jhjU8O1f_HQ42SSQvqTrrrIrTHQo.original.fullsize.png">

In $\triangle \mathrm{ABC}, \mathrm{AC}$ represents ladder
$\mathrm{AB} \rightarrow$ vertical wall
Let $\mathrm{AB}=x, \mathrm{BC}=y$
$\therefore \quad \angle \mathrm{ABC}=90^{\circ}$
By Pythagoras theorem,
$\begin{aligned}
& \mathrm{AB}^2+\mathrm{BC}^2=\mathrm{AC}^2 \\
& \Rightarrow x^2+y^2=17^2 \\
& \Rightarrow x^2=289-y^2 ... (i)\\
& \Rightarrow x^2=289-64 \\
& \Rightarrow x^2=225 \\
& \Rightarrow x=15 \mathrm{~m}
\end{aligned}$
Consider equation (i),
$x^2=289-y^2$
Differentiating w.r.t. t, we get
$\begin{aligned}
& 2 x \frac{\mathrm{d} x}{\mathrm{dt}}=-2 y \frac{\mathrm{d} y}{\mathrm{dt}} \\
& \Rightarrow 15 \frac{\mathrm{d} x}{\mathrm{dt}}=-8(1) \\
& \Rightarrow \frac{\mathrm{d} x}{\mathrm{dt}}=\frac{-8}{15} \mathrm{~m} / \mathrm{s}
\end{aligned}$
Negative sign shows that the ladder is moving down. i.e., vertical length is decreasing
$\therefore \quad$ Upper end is coming down at the rate of $\frac{8}{15} \mathrm{~m} / \mathrm{s}$.

</details>

---

### Q72. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A square plate is contracting at the uniform rate $4 \mathrm{~cm}^2 / \mathrm{sec}$, then the rate at which the perimeter is decreasing, when side of the square is $20 \mathrm{~cm}$, is

**Options:**

- **(A)** $\frac{1}{5} \mathrm{~cm} / \mathrm{sec}$.
- **(B)** $4 \mathrm{~cm} / \mathrm{sec}$.
- **(C)** $2 \mathrm{~cm} / \mathrm{sec}$.
- **(D)** $\frac{2}{5} \mathrm{~cm} / \mathrm{sec}$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2}{5} \mathrm{~cm} / \mathrm{sec}$.**

**Detailed Solution:**

Let $\mathrm{A}, \mathrm{P}$ and $\mathrm{X}$ be the area, perimeter and length of side of square respectively at time ' $\mathrm{t}$ ' seconds. Then,
$\begin{aligned}
\mathrm{A} & =\mathrm{X}^2, \mathrm{P}=4 \mathrm{X} \\
\therefore \quad \mathrm{P} & =4 \sqrt{\mathrm{A}}
\end{aligned}$
Differentiating w.r.t. t, we get
$\begin{aligned}
\frac{\mathrm{dP}}{\mathrm{dt}} & =4 \frac{1}{2 \sqrt{\mathrm{A}}} \cdot \frac{\mathrm{dA}}{\mathrm{dt}} \\
& =\frac{2}{\mathrm{X}} \cdot \frac{\mathrm{dA}}{\mathrm{dt}} \\
& =\frac{2}{20} \times 4...\left[\begin{array}{l}
\text { side }=20 \mathrm{~cm} \\
\frac{\mathrm{dA}}{\mathrm{dt}}=4 \mathrm{~cm}^2 / \mathrm{sec}
\end{array}\right] \\
& =\frac{2}{5} \mathrm{~cm} / \mathrm{sec}
\end{aligned}$

</details>

---

### Q73. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An object is moving in the clockwise direction around the unit circle $x^2+y^2=1$. As it passes through the point $\left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$, its $y$-co-ordinate is decreasing at the rate of 3 units per sec. The rate at which the $x$-co-ordinate changes at this point is

**Options:**

- **(A)** $2$ units $/ \mathrm{sec}$
- **(B)** $3 \sqrt{3}$ units $/ \mathrm{sec}$
- **(C)** $\sqrt 3$ units $/ \mathrm{sec}$
- **(D)** $2\sqrt 3$ units $/ \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 \sqrt{3}$ units $/ \mathrm{sec}$**

**Detailed Solution:**

Given equation is $x^2+y^2=1$ Differentiating w.r.t. t, we get
$\begin{aligned}
& 2 x \frac{\mathrm{d} x}{\mathrm{dt}}+2 y \frac{\mathrm{d} y}{\mathrm{dt}}=0 \\
& 2 x \frac{\mathrm{d} x}{\mathrm{dt}}+2 y(-3)=0 \\
& \frac{\mathrm{d} x}{\mathrm{dt}}=\frac{6 y}{2 x} \\
& \frac{\mathrm{d} x}{\mathrm{dt}}=\frac{3 y}{x} \\
& \left.\frac{\mathrm{d} x}{\mathrm{dt}}\right|_{\left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right)}=\frac{3 \times \frac{\sqrt{3}}{2}}{\frac{1}{2}} \\
& =3 \sqrt{3} \text { units/sec }
\end{aligned}$

</details>

---

### Q74. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The approximate value of $\log _{10} 998$ is (given that $\log _{10} \mathrm{e}=0.4343$ )

**Options:**

- **(A)** 3.0008686
- **(B)** 1.9991314
- **(C)** 2.0008686
- **(D)** 2.9991314

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2.9991314**

**Detailed Solution:**

Let
$\begin{aligned}
\mathrm{f}(x)=\log _{10} x=\frac{\log _{\mathrm{e}} x}{\log _{\mathrm{e}} 10} & =\left(\log _{10} \mathrm{e}\right)\left(\log _{\mathrm{e}} x\right) \\
& =0.4343\left(\log _{\mathrm{e}} x\right)
\end{aligned}$
On differentiating w.r.t. $x$, we get
$\begin{aligned}
\mathrm{f}^{\prime}(x) & =\frac{0.4343}{x} \\
\text { Let } x & =998 \\
& =1000-2=\mathrm{a}+\mathrm{h} \\
\therefore \quad \mathrm{a}= & 1000, \mathrm{~h}=-2 \\
\mathrm{f}(\mathrm{a}) & =\mathrm{f}(1000) \\
& =\log _{10}(1000) \\
& =3 \log _{10} 10 \\
\therefore \quad \mathrm{f}(\mathrm{a}) & =3
\end{aligned}$
$\begin{aligned}
& \text { Also, } \mathrm{f}^{\prime}(\mathrm{a})=\mathrm{f}^{\prime}(1000)=\frac{0.4343}{1000}=0.0004343 \\
& \mathrm{f}(\mathrm{a}+\mathrm{h}) \approx \mathrm{f}(\mathrm{a})+\mathrm{hf}^{\prime}(\mathrm{a}) \\
& \therefore \quad \log _{10}(998) \approx 3-2(0.0004343) \\
&
\end{aligned}$

</details>

---

### Q75. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The radius of right circular cylinder increase at the rate $0.1 \mathrm{~cm} / \mathrm{min}$ and height decreases at the rate of $0 \cdot 2 \mathrm{~cm} / \mathrm{min}$ The rate of change of volume of the cylinder in $\mathrm{cm}^3 / \mathrm{min}$, when the radius is $2 \mathrm{~cm}$ and height is $3 \mathrm{~cm}$, is

**Options:**

- **(A)** $-2 \mathrm{pm}^3 / \mathrm{min}$
- **(B)** $\frac{-3 \pi}{5} \mathrm{~cm}^3 / \mathrm{min}$
- **(C)** $\frac{-8 \pi}{5} \mathrm{~cm}^3 / \mathrm{min}$
- **(D)** $\frac{2 \pi}{5} \mathrm{~cm}^3 / \mathrm{min}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2 \pi}{5} \mathrm{~cm}^3 / \mathrm{min}$**

**Detailed Solution:**

$\begin{aligned} & V=p r^2 h \\ & \Rightarrow \frac{\mathrm{d} v}{\mathrm{~d} t}=\pi\left\{2 r \cdot \frac{\mathrm{d} r}{\mathrm{~d} t} \cdot h+r^2 \cdot \frac{\mathrm{d} h}{\mathrm{~d} t}\right\} \\ & =\pi\left\{2 \times 2 \times 0 \cdot 1 \times 3+2^2 \times(-0 \cdot 2)\right\} \\ & =\pi\{1 \cdot 2-0 \cdot 8\}=0 \cdot 4 \pi=\frac{2 \pi}{5} \mathrm{~cm}^3 / \mathrm{min}\end{aligned}$

</details>

---

### Q76. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The rate of change volume of a sphere with respect to its surface area when the radius is 5 meters is

**Options:**

- **(A)** $\frac{2}{5}$
- **(B)** 5
- **(C)** $\frac{5}{2}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{5}{2}$**

**Detailed Solution:**

$\begin{aligned} & V=\frac{4}{3} \pi r^3 \\ & \Rightarrow \frac{\mathrm{d} v}{\mathrm{~d} t}=4 \pi r^2 \frac{\mathrm{d} r}{\mathrm{~d} t} \\ & S=4 \pi r^2 \\ & \Rightarrow \frac{\mathrm{d} s}{\mathrm{~d} t}=8 \pi r \frac{\mathrm{d} r}{\mathrm{~d} t} \\ & \text { Now } \frac{\mathrm{d} v}{\mathrm{~d} s}=\frac{\frac{\mathrm{d} v}{\mathrm{~d} t}}{\frac{\mathrm{ds}}{\mathrm{d} t}}=\frac{r}{2}=\frac{5}{2}\end{aligned}$

</details>

---

### Q77. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The radius of a cylinder is increasing at the rate $2 \mathrm{~cm} / \mathrm{sec}$ and its height is decreasing at the rate of $3 \mathrm{~cm} / \mathrm{sec}$, then the rate of change of volume, when radius is $3 \mathrm{~cm}$ and the height is $5 \mathrm{~cm}$, is

**Options:**

- **(A)** $44 \pi \mathrm{cm}^3 / \mathrm{sec}$
- **(B)** $11 \pi \mathrm{cm}^3 / \mathrm{sec}$
- **(C)** $23 \pi \mathrm{cm}^3 / \mathrm{sec}$
- **(D)** $33 \pi \mathrm{cm}^3 / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $33 \pi \mathrm{cm}^3 / \mathrm{sec}$**

**Detailed Solution:**

$V=\pi r^2 h$
$\begin{aligned} & \Rightarrow \frac{\mathrm{d} v}{\mathrm{~d} t}=\pi\left(2 r \frac{\mathrm{d} r}{\mathrm{~d} t} h+r^2 \frac{\mathrm{d} h}{\mathrm{~d} t}\right) \\ & \Rightarrow \frac{\mathrm{d} v}{\mathrm{~d} t}=\pi\left(2 \times 3 \times 2 \times 5+3^2 \times(-3)\right) \\ & \Rightarrow \frac{\mathrm{d} v}{\mathrm{~d} t}=33 \pi \mathrm{cm}^3 / \mathrm{sec}\end{aligned}$

</details>

---

### Q78. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A spherical iron ball $10 \mathrm{~cm}$ in radius is coated with a layer of ice of uniform thickness that melts at a rate of $50 \mathrm{~cm}^3 / \mathrm{min}$. When the thickness of ice is $5 \mathrm{~cm}$, then the rate at which the thickness of ice decreases, is

**Options:**

- **(A)** $\frac{1}{36 \pi} \mathrm{cm} / \mathrm{min}$
- **(B)** $\frac{5}{6 \pi} \mathrm{cm} / \mathrm{min}$
- **(C)** $\frac{1}{54 \pi} \mathrm{cm} / \mathrm{min}$
- **(D)** $\frac{1}{18 \pi} \mathrm{cm} / \mathrm{min}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{18 \pi} \mathrm{cm} / \mathrm{min}$**

**Detailed Solution:**

$\begin{aligned} & V=\frac{4}{3} \pi r^3 \\ & \Rightarrow \frac{\mathrm{d} v}{\mathrm{~d} t}=4 \pi r^2 \frac{\mathrm{d} r}{\mathrm{~d} t} \\ & \Rightarrow 50=4 \pi \times 15^2 \times \frac{\mathrm{d} r}{\mathrm{~d} t} \\ & \Rightarrow \frac{\mathrm{d} r}{\mathrm{~d} t}=\frac{50}{4 \pi \times 15^2}=\frac{1}{18 \pi} \mathrm{cm} / \mathrm{min}\end{aligned}$

</details>

---

### Q79. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sides of an equilateral triangle are increasing at the rate of $2 \mathrm{~cm} / \mathrm{sec}$. The rate at which the area increases, when side is $10 \mathrm{~cm}$, is

**Options:**

- **(A)** $\frac{\sqrt{3}}{10} \mathrm{~cm}^2 / \mathrm{sec}$
- **(B)** $\frac{10}{\sqrt{3}} \mathrm{~cm}^2 / \mathrm{sec}$
- **(C)** $\sqrt{3} \mathrm{~cm}^2 / \mathrm{sec}$
- **(D)** $10 \sqrt{3} \mathrm{~cm}^2 / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $10 \sqrt{3} \mathrm{~cm}^2 / \mathrm{sec}$**

**Detailed Solution:**

$\begin{aligned} & A=\frac{\sqrt{3}}{4} S^2 \\ & \Rightarrow \frac{\mathrm{d} A}{\mathrm{~d} t}=\frac{\sqrt{3}}{4} \cdot 2 S \frac{\mathrm{d} s}{\mathrm{~d} t}=\frac{\sqrt{3}}{4} \times 2 \times 10 \times 2 \mathrm{~cm}^2 / \mathrm{sec} \\ & \Rightarrow \frac{\mathrm{d} A}{\mathrm{~d} t}=10 \sqrt{3} \mathrm{~cm}^2 / \mathrm{sec}\end{aligned}$

</details>

---

### Q80. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the water is being poured at the rate $36 \mathrm{~m}^3 / \mathrm{sec}$ in cylindrical vessel of base radius $3 \mathrm{~m}$, then the rate at which water level is rising, is

**Options:**

- **(A)** $\frac{4}{\pi} \mathrm{m} / \mathrm{sec}$
- **(B)** $4 \pi \mathrm{m} / \mathrm{sec}$
- **(C)** $\frac{\pi}{4} \mathrm{~m} / \mathrm{sec}$
- **(D)** $\frac{3}{\pi} \mathrm{m} / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{4}{\pi} \mathrm{m} / \mathrm{sec}$**

**Detailed Solution:**

$\frac{\mathrm{d} v}{\mathrm{~d} t}=36 \mathrm{~m}^3 / \mathrm{sec}$
and $v=\pi r^2 \mathrm{~h}=\pi \times 3^2 \mathrm{~h}=9 \pi \mathrm{h}$
$\Rightarrow \frac{\mathrm{d} v}{\mathrm{~d} t}=9 \pi \frac{\mathrm{d} h}{\mathrm{~d} t}$
$\Rightarrow 36=9 \pi \frac{\mathrm{d} h}{\mathrm{~d} t}$
$\Rightarrow \frac{\mathrm{d} h}{\mathrm{~d} t}=\frac{4}{\pi} \mathrm{m} / \mathrm{sec}$

</details>

---

### Q81. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The rate of disintegration of a radio active element at time $t$ is proportional to its mass at that time. Then the time during which the original mass of $6 \mathrm{gm}$ will disintegrate into its mass of $3 \mathrm{gm}$ is proportional to

**Options:**

- **(A)** $\log 4$
- **(B)** $\log 3$
- **(C)** $\log 5$
- **(D)** $\log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log 2$**

**Detailed Solution:**

$\begin{aligned} & \frac{d(m)}{d t} \propto m \\ & \Rightarrow \frac{d m}{d t}=-k m \\ & \int \frac{d m}{m}=-\int k d t \\ & \Rightarrow \log _e m=-k t+c \\ & \Rightarrow m=e^{-k t+c}=e^c \cdot e^{-k t} \\ & \text { at } t=0, m=6 \Rightarrow e^c=6 \\ & \text { i.e., } m=6 \cdot e^{-k t}\end{aligned}$
at $t=t, m=3$
Hence $3=6 \cdot e^{-k t}$
$\begin{aligned} & \Rightarrow \frac{1}{2}=e^{-k t} \\ & \Rightarrow \log \left(\frac{1}{2}\right)=-k t \\ & \Rightarrow-\log 2=-k t \\ & \left.\Rightarrow t=\frac{\log 2}{k} \text { [Propotional to } \log 2\right]\end{aligned}$

</details>

---

### Q82. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If surrounding air is kept at $20^{\circ} \mathrm{C}$ and body cools from $80^{\circ} \mathrm{C}$ to $70^{\circ} \mathrm{C}$ in 5 minutes, then the temperature of the body after 15 minute will be

**Options:**

- **(A)** $52.7^{\circ} \mathrm{C}$
- **(B)** $51.7^{\circ} \mathrm{C}$
- **(C)** $54.7^{\circ} \mathrm{C}$
- **(D)** $50.7^{\circ} \mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $54.7^{\circ} \mathrm{C}$**

**Detailed Solution:**

$\frac{d T}{d t}=-k(T-20) \Rightarrow T-20=e^{-k t+c} \Rightarrow T=20+e^c e^{-k t}$
for $t=0, T=80 \Rightarrow e^c=60$
i.e. $T=20+60 \cdot e^{-k t}$
For $t=5, T=70 \Rightarrow 70=20+60 e \Rightarrow-5 k=\log \frac{5}{6}$
i.e. $T=20+60 e^{\frac{1}{5} \log \frac{5}{6} \times t}$
Now, for $t=15$
$T=20+60 e^{15 \times \frac{1}{5} \log \frac{5}{6}}=20+60 \times\left(\frac{5}{6}\right)^3=54.7$

</details>

---

### Q83. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

20 meters of wire is available to fence of a flowerbed in the form of a circular sector. If the flowerbed is to have maximum surface area, then the radius of the circle is

**Options:**

- **(A)** $8 \mathrm{~m}$
- **(B)** $4 \mathrm{~m}$
- **(C)** $2 \mathrm{~m}$
- **(D)** $5 \mathrm{~m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5 \mathrm{~m}$**

**Detailed Solution:**

$\theta^c=\frac{\ell}{r}=\frac{20-2 r}{r}=\frac{20-2 r}{r} \times \frac{180^{\circ}}{\pi}$
Now area of sector $=\frac{\pi r^2 \theta}{360^{\circ}}$
$A(r)=\frac{\pi r^2 \times \frac{20-2 r}{r} \times \frac{180^{\circ}}{\pi}}{360^{\circ}}=10 r-r^2$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/bGe8KyjIwmYvTIG2RGK0E6lwiDWc0muD8c7JYZgaYTs.original.fullsize.png">
For maximum area $A^{\prime}(r)=0$
$\begin{aligned} & \Rightarrow 10-2 r=0 \\ & \Rightarrow r=5 \mathrm{~m}\end{aligned}$

</details>

---

### Q84. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A spherical iron ball of $10 \mathrm{~cm}$ radius is coated with a layer of ice of uniform thickness that melts at the rate of $50 \mathrm{~cm}^3 / \mathrm{min}$. If the thickness of ice is $5 \mathrm{~cm}$, then the rate at which the thickness of ice decrease is

**Options:**

- **(A)** $\frac{1}{18 \pi} \mathrm{cm} / \mathrm{min}$
- **(B)** $\frac{2}{9 \pi} \mathrm{cm} / \mathrm{min}$
- **(C)** $\frac{-1}{18 \pi} \mathrm{cm} / \mathrm{min}$
- **(D)** $\frac{1}{3 \pi} \mathrm{cm} / \mathrm{min}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{18 \pi} \mathrm{cm} / \mathrm{min}$**

**Detailed Solution:**

$\begin{aligned} & v=\frac{4}{3} \pi r^3 \\ & \frac{d v}{d t}=50 \quad r=(10+5)=15 \mathrm{~cm} \\ & \Rightarrow \frac{d v}{d t}=4 \pi r^2 \frac{d r}{d t} \\ & \Rightarrow 50=4 \pi \times 15 \times 15 \times \frac{d r}{d t} \\ & \Rightarrow \frac{d r}{d t}=\frac{50}{4 \pi \times 15 \times 15}=\frac{1}{18 \pi} \mathrm{cm} / \mathrm{min}\end{aligned}$

</details>

---

### Q85. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A firm is manufacturing 2000 items. It is estimated that the rate of change of production $P$ with respect to additional number of workers $x$ is given by $\frac{d p}{d x}=100-12 \sqrt{x}$. If the firm employs 25 more workers, then the new level of production of items is

**Options:**

- **(A)** $2500$
- **(B)** $3000$
- **(C)** $3500$
- **(D)** $4500$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3500$**

**Detailed Solution:**

$\begin{aligned} & \frac{d p}{d x}=100-12 \sqrt{x} \Rightarrow \int d p=\int(100-12 \sqrt{x}) d x \\ & \Rightarrow p=100 x-12 \times \frac{2}{3} x^{3 / 2}+C \\ & \Rightarrow p=100 x-8 x^{3 / 2}+200[\because \text { at } x=0, p=2000] \\ & \Rightarrow p=100 \times 25-8 \times(25)^{3 / 2}+2000[\text { putting } x=25] \\ & \Rightarrow p=2500-1000+2000=3500\end{aligned}$

</details>

---

### Q86. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The rate at which the population of a city increases varies as the population present. Within the period of 30 years, the population grew from 20 lakhs to 40 lakhs. Then, the population after a further period of 15 years will be
$($ Take $\sqrt{2}=1.41)$

**Options:**

- **(A)** 56 lakhs
- **(B)** 60 lakhs
- **(C)** 57.4 lakhs
- **(D)** 56.4 lakhs

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 56.4 lakhs**

**Detailed Solution:**

$\begin{aligned} & \frac{d p}{d t} \propto p \Rightarrow \frac{d p}{d t}=k p \Rightarrow \int \frac{d p}{p}=\int k d t \\ & \Rightarrow \log _e P=k t+C\end{aligned}$
Putting $\mathrm{t}=0$ year and $\mathrm{p}=20$ lakhs
We get $\mathrm{c}=\log _{\mathrm{e}} 20$
$\Rightarrow \log _e P=K t+\log _e 20$
Again putting $\mathrm{t}=30$ years and $\mathrm{P}=40$ lakhs
$\begin{aligned} & \Rightarrow \log _e 40=K \times 30+\log _e 20 \\ & \Rightarrow K=\frac{\log _e 2}{30} \\ & \Rightarrow \log _e P=\frac{\log _e 2}{30} t \log _e 20\end{aligned}$
Putting $\mathrm{t}=45$ years
We get $\log _e p=\frac{\log _e 2}{30} \times 45+\log _e 20$
$\begin{aligned} & \Rightarrow \log _e P=\frac{3}{2} \log _e 2+\log _e 20 \\ & \Rightarrow \log _e P=\log _e 2 \frac{3}{2} \times 20 \\ & \Rightarrow P=2 \sqrt{2} \times 20 \text { lakhs }\end{aligned}$
$\Rightarrow \mathrm{P}=2 \times 1.41 \times 20$ lakhs
$\Rightarrow \mathrm{P}=56.4$ lakhs

</details>

---

### Q87. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A circular sector of perimeter 60 meter with maximum area is to be constructed. The radius of the circular are in meter must be

**Options:**

- **(A)** $5 \mathrm{~m}$
- **(B)** $15 \mathrm{~m}$
- **(C)** $10 \mathrm{~m}$
- **(D)** $20 \mathrm{~m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $15 \mathrm{~m}$**

**Detailed Solution:**

Perimeter $=2 r+r \theta=60$
$\Rightarrow \theta=\frac{60-2 r}{r}$
Area $=\mathrm{A}(\mathrm{r})=\frac{\pi \mathrm{r}^2 \theta}{360}=\frac{\pi \mathrm{r}^2\left(\frac{60-2 \mathrm{r}}{\mathrm{r}}\right)}{360}=\frac{\pi}{360}\left(60 r-2 \mathrm{r}^2\right)$
$A^{\prime}(r)=\frac{\pi}{360}(60-4 r)$
For area to be maximum $A^{\prime}(r)=0 \Rightarrow r=15$

</details>

---

### Q88. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The side of a square sheet of metal is increasing at the rate of $3 \mathrm{~cm} / \mathrm{min}$. At what rate is the area increasing when the length of the side is $6 \mathrm{~cm}$ long?

**Options:**

- **(A)** $36 \mathrm{~cm}^2 / \mathrm{min}$
- **(B)** $12 \mathrm{~cm}^2 / \mathrm{min}$
- **(C)** $18 \mathrm{~cm}^2 / \mathrm{min}$
- **(D)** $9 \mathrm{~cm}^2 / \mathrm{min}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $36 \mathrm{~cm}^2 / \mathrm{min}$**

**Detailed Solution:**

$\mathrm{A}=\mathrm{a}^2$ and $\frac{\mathrm{da}}{\mathrm{dt}}=3 \mathrm{~cm} / \mathrm{min}$
Now $\frac{\mathrm{dA}}{\mathrm{dt}}=2 \mathrm{a} \frac{\mathrm{dA}}{\mathrm{dt}}$
$\Rightarrow \frac{\mathrm{dA}}{\mathrm{dt}}=2 \times 6 \times 3 \mathrm{~cm}^2 / \min =36 \mathrm{~cm}^2 / \min$

</details>

---

### Q89. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A stone is dropped in a quiet lake and it is observed that waves move in circles, If the radius of a circular wave increases at the rate $2 \mathrm{~cm} / \mathrm{sec}$, then the rate of increase in its area at the instant when its radius is $10 \mathrm{~cm}$, is $\mathrm{cm}^2 / \mathrm{sec}$.

**Options:**

- **(A)** $40 \pi$
- **(B)** $80 \pi$
- **(C)** $10 \pi$
- **(D)** $20 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $40 \pi$**

**Detailed Solution:**

Given $\frac{d r}{d t}=2 \mathrm{~cm} / \mathrm{sec} r=10 \mathrm{~cm}$
We have $A=\pi r^2$
Diff. w.r.t. $\mathrm{t}$
$\begin{aligned} & \frac{d A}{d t}=2 \pi r \frac{d r}{d t} \\ & =2 \pi \times 10 \times 2 \\ & =40 \pi\end{aligned}$

</details>

---

### Q90. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The distance ' $\mathrm{s}$ ' in meters covered by a particle in $\mathrm{t}$ seconds is given by $s=2+27 t-t^3$. The particle will stop after <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/luPzKaQFjP2u82EjfruKwOgee1f6Xm73tgylXbYqW2A.original.fullsize.png">
distance.

**Options:**

- **(A)** 65 meters
- **(B)** 80 meters
- **(C)** 56 meters
- **(D)** 60 meters

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 56 meters**

**Detailed Solution:**

$\mathrm{s}=2+27 \mathrm{t}-\mathrm{t}^3$ and particle stops when its velocity is zero.
$\therefore \frac{\mathrm{ds}}{\mathrm{dt}}=27-3 \mathrm{t}^2=0 \Rightarrow \mathrm{t}^2=9 \Rightarrow \mathrm{t}=3 \mathrm{sec} .$
$\therefore$ Distance covered in $3 \mathrm{sec}$, is
$\mathrm{S}_{(\mathrm{t}=3)}=2+27(3)-(3)^3=56 \mathrm{~m}$

</details>

---

### Q91. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The radius of a circular plate is increasing at the rate of 0.01 $\mathrm{cm} / \mathrm{sec}$, when the radius is $12 \mathrm{~cm}$. Then the rate at which the area increases is

**Options:**

- **(A)** $60 \pi$ sq. cm $/ \mathrm{sec}$
- **(B)** $0.24 \pi$ sq. cm $/ \mathrm{sec}$
- **(C)** $1.2 \pi$ sq. cm $/ \mathrm{sec}$
- **(D)** $24 \pi$ sq. cm $/ \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.24 \pi$ sq. cm $/ \mathrm{sec}$**

**Detailed Solution:**

We have $\frac{\mathrm{dr}}{\mathrm{dt}}=0.01$
$$
\begin{aligned}
& \mathrm{A}=\pi \mathrm{r}^2 \\
& \therefore \quad \frac{\mathrm{dA}}{\mathrm{dt}}=\pi(2 \mathrm{r}) \frac{\mathrm{dr}}{\mathrm{dt}}=(2 \pi)(12)(0.01)=0.24 \pi \mathrm{sq} \cdot \mathrm{cm} / \mathrm{sec}
\end{aligned}
$$

</details>

---

### Q92. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A spherical raindrop evaporates at a rate proportional to its surface area. If its radius originally is $3 \mathrm{~mm}$. and 1 hour later has been reduced to $2 \mathrm{~mm}$, then the expression of radius $\mathrm{r}$ of the raindrop at any time $t$ is (where $0 \leq t < 3$ )

**Options:**

- **(A)** $\mathrm{r}=\mathrm{t}+5$
- **(B)** $r=t-5$
- **(C)** $\mathrm{r}=3-\mathrm{t}$
- **(D)** $r=t+3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{r}=3-\mathrm{t}$**

**Detailed Solution:**

We have $\frac{\mathrm{dv}}{\mathrm{dt}} \propto-\left(4 \pi \mathrm{r}^2\right)$
We know that $\mathrm{v}=\frac{4}{3} \pi \mathrm{r}^2 \Rightarrow \frac{\mathrm{dv}}{\mathrm{dt}}=4 \pi \mathrm{r}^2 \frac{\mathrm{dr}}{\mathrm{dt}}$
$$
\begin{aligned}
& \therefore 4 \pi \mathrm{r}^2 \frac{\mathrm{dr}}{\mathrm{dt}} \propto-\left(4 \pi \mathrm{r}^2\right) \\
& \therefore 4 \pi \mathrm{r}^2 \frac{\mathrm{dr}}{\mathrm{dt}}=\left(-4 \mathrm{k} \pi \mathrm{r}^2\right) \Rightarrow \frac{\mathrm{dr}}{\mathrm{dt}}=-\mathrm{k}
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/bHHdA1jBR0twhqo-gHi2m3I46GQK8xLQReTMrKGQNZ0.original.fullsize.png">

</details>

---

### Q93. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A spherical snow ball is forming so that its volume is increasing at the rate of $8 \mathrm{~cm}^3 / \mathrm{sec}$. Find the rate of increase of radius when radius is $2 \mathrm{~cm}$

**Options:**

- **(A)** $\pi \mathrm{cm} / \mathrm{sec}$
- **(B)** $\frac{1}{8 \pi} \mathrm{cm} / \mathrm{sec}$
- **(C)** $2 \pi \mathrm{cm} / \mathrm{sec}$
- **(D)** $\frac{1}{2 \pi} \mathrm{cm} / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2 \pi} \mathrm{cm} / \mathrm{sec}$**

**Detailed Solution:**

$\mathrm{V}=\frac{4}{3} \pi \mathrm{r}^3$
$\therefore \frac{\mathrm{dV}}{\mathrm{dt}}=\frac{4}{3} \pi\left(3 \mathrm{r}^2\right) \frac{\mathrm{dr}}{\mathrm{dt}}=4 \pi \mathrm{r}^2 \frac{\mathrm{dr}}{\mathrm{dt}}$
$\therefore 8=4 \pi(2)^2 \frac{\mathrm{dr}}{\mathrm{dt}} \Rightarrow \frac{\mathrm{dr}}{\mathrm{dt}}=\frac{1}{2 \pi}$

</details>

---

### Q94. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A stone is dropped in a quiet lake and it is observed that waves move in circles, If the radius of a circular wave increases at the rate $2 \mathrm{~cm} / \mathrm{sec}$, then the rate of increase in its area at the instant when its radius is $10 \mathrm{~cm}$, is $\mathrm{cm}^2 / \mathrm{sec}$.

**Options:**

- **(A)** $40 \pi$
- **(B)** $80 \pi$
- **(C)** $10 \pi$
- **(D)** $20 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $40 \pi$**

**Detailed Solution:**

Given $\frac{d r}{d t}=2 \mathrm{~cm} / \mathrm{sec} r=10 \mathrm{~cm}$
We have $A=\pi r^2$
Diff. w.r.t. t
$$
\begin{aligned}
& \frac{d A}{d t}=2 \pi r \frac{d r}{d t} \\
& =2 \pi \times 10 \times 2 \\
& =40 \pi
\end{aligned}
$$

</details>

---

### Q95. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The surface area of a spherical balloon is increasing at the rate $2 \mathrm{~cm}^2 / \mathrm{sec}$. Then rate of increase in the volume of the balloon is , when the radius of the balloon is $6 \mathrm{~cm}$.

**Options:**

- **(A)** $4 \mathrm{~cm}^3 / \mathrm{sec}$
- **(B)** $16 \mathrm{~cm}^3 / \mathrm{sec}$
- **(C)** $36 \mathrm{~cm}^3 / \mathrm{sec}$
- **(D)** $6 \mathrm{~cm}^3 / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $6 \mathrm{~cm}^3 / \mathrm{sec}$**

**Detailed Solution:**

We have $\frac{\mathrm{dA}}{\mathrm{dt}}=2$ and $\mathrm{A}=4 \pi \mathrm{r}^2$
$$
\begin{aligned}
& \therefore \frac{\mathrm{dA}}{\mathrm{dt}}=8 \pi \mathrm{r} \frac{\mathrm{dt}}{\mathrm{dt}} \Rightarrow 2=8 \pi(6) \frac{\mathrm{dr}}{\mathrm{dt}} \\
& \therefore \frac{\mathrm{dr}}{\mathrm{dt}}=\frac{1}{24 \pi}
\end{aligned}
$$
Here $\mathrm{V}=\frac{4}{3} \pi \mathrm{r}^3$
$$
\begin{aligned}
& \therefore \frac{\mathrm{dV}}{\mathrm{dt}}=4 \pi \mathrm{r}^2 \frac{\mathrm{dr}}{\mathrm{dt}} \\
& =4 \pi(6)^2\left(\frac{1}{24 \pi}\right)=6 \mathrm{~cm}^3 / \mathrm{sec}
\end{aligned}
$$

</details>

---

### Q96. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Water is being poured at the rate of $36 \mathrm{~m}^3 / \mathrm{min}$. into a cylindrical vessel, whose circular base is of radius $3 \mathrm{~m}$. then the water level in the cylinder is rising at the rate of

**Options:**

- **(A)** $\frac{4}{\pi} \mathrm{m} / \mathrm{min}$
- **(B)** $4 \pi \mathrm{m} / \mathrm{min}$
- **(C)** $\frac{1}{4 \pi} \mathrm{m} / \mathrm{min}$
- **(D)** $\frac{2}{\pi} \mathrm{m} / \mathrm{min}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{4}{\pi} \mathrm{m} / \mathrm{min}$**

**Detailed Solution:**

Volume of cylinder $=\pi \mathrm{r}^2 \mathrm{~h}$
$$
\begin{aligned}
& \therefore \frac{\mathrm{dv}}{\mathrm{dt}}=\pi \mathrm{r}^2 \frac{\mathrm{dh}}{\mathrm{dt}} \\
& \therefore 36=\pi(3)^2 \frac{\mathrm{dh}}{\mathrm{dt}} \Rightarrow \frac{\mathrm{dh}}{\mathrm{dt}}=\frac{4}{\pi} \mathrm{m} / \mathrm{min}
\end{aligned}
$$

</details>

---

### Q97. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A particle is moving on a straight line. The distance $\mathrm{S}$ travelled in time $t$ is given by $S=a t^2+b t+6$. If the particle comes to rest after 4 seconds at a distance of $16 \mathrm{~m}$. from the starting point, then the acceleration of the particle is.

**Options:**

- **(A)** $\frac{-3}{4} \mathrm{~m} / \mathrm{sec}^2$
- **(B)** $\frac{-1}{2} \mathrm{~m} / \mathrm{sec}^2$
- **(C)** $-1 \mathrm{~m} / \mathrm{sec}^2$
- **(D)** $\frac{-5}{4} \mathrm{~m} / \mathrm{sec}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{-5}{4} \mathrm{~m} / \mathrm{sec}^2$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{S}=\mathrm{at} \mathrm{t}^2+\mathrm{bt}+6 \\
& \therefore \mathrm{V}=\frac{\mathrm{dS}}{\mathrm{dt}}=2 \mathrm{at}+\mathrm{b} \text { and } \mathrm{A}=\frac{\mathrm{d}^2 \mathrm{~S}}{\mathrm{dt}^2}=2 \mathrm{a}
\end{aligned}
$$
When particle comes to rest,
$$
\begin{aligned}
& S=16, \mathrm{t}=4, \mathrm{~V}=0 \\
& \therefore 16=\mathrm{a}(4)^2+\mathrm{b}(4)+6 \\
& \Rightarrow 16 \mathrm{a}+4 \mathrm{~b}=10 \ldots(1)
\end{aligned}
$$
Also $0=2 \mathrm{a}(1)(2)+4$
$$
\Rightarrow \mathrm{b}=-8 \mathrm{a}
$$
From (1) and (2), we get
$$
16 a+4(8 a)=10 \Rightarrow-16=10 \Rightarrow a=\frac{-5}{9}
$$
We have acceleration $\mathrm{A}=2 \mathrm{a}=2\left(\frac{-5}{8}\right)=\frac{-5}{4} \mathrm{~m} / \mathrm{sec}^2$

</details>

---

### Q98. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The approximate value of $(66)^{\frac{1}{3}}$ is

**Options:**

- **(A)** $4.0416$
- **(B)** $4.0447$
- **(C)** $4.0433$
- **(D)** $4.0481$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4.0416$**

**Detailed Solution:**

Let $\mathrm{a}=64, \mathrm{~h}=2$ and let $\mathrm{f}(\mathrm{x})=\mathrm{x}^{\frac{1}{3}} \Rightarrow \mathrm{f}^{\prime}(\mathrm{x})=\frac{1}{3} \mathrm{x}^{-\frac{2}{3}}=\frac{1}{3 \mathrm{x}^{\frac{2}{3}}}$
$\therefore \mathrm{f}(\mathrm{a})=64^{\frac{1}{3}}=4 \quad$ and $\quad \mathrm{f}^{\prime}(\mathrm{a})=\frac{1}{3(64)^{\frac{2}{3}}}=\frac{1}{3(16)}=\frac{1}{48}$
We have $\mathrm{f}(\mathrm{a}+\mathrm{h}) \neq \mathrm{f}(\mathrm{a})+\mathrm{h} \cdot \mathrm{f}^{\prime}(\mathrm{a})$
$\therefore(66)^{\frac{1}{3}} \div 4+(2)\left(\frac{1}{48}\right) \div 4+\frac{1}{24} \div 4.0416$

</details>

---

### Q99. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The approximate value of $f(x)=3 x^{2}+5 x+3$ at $x=3 \cdot 02$ is

**Options:**

- **(A)** $45.46$
- **(B)** $v=45 \cdot 46$
- **(C)** $44 \cdot 76$
- **(D)** $44 \cdot 46$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $v=45 \cdot 46$**

**Detailed Solution:**

Given $f(x)=3 x^{2}+5 x+3 \Rightarrow f^{\prime}(x)=6 x+5$
Let $\mathrm{a}=3, \mathrm{~h}=0.02$
$\therefore \mathrm{f}(\mathrm{a}) \quad=\mathrm{f}(3)=27+15+3=45$
$f^{\prime}(a)=f^{\prime}(3) \quad=18+5=23$
We know that
$$
\begin{aligned}
\mathrm{f}(\mathrm{a}+\mathrm{h}) & \div \mathrm{f}(\mathrm{a})+\mathrm{hf}^{\prime}(\mathrm{a}) \\
&=45+(0.02)(23)=45+0.46=45.46
\end{aligned}
$$

</details>

---

### Q100. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The area of the square increases at the rate of $0.5 \mathrm{~cm}^{2} / \mathrm{sec}$. The rate at which its
perimeter is increasing when the side of the square is $10 \mathrm{~cm}$ long, is

**Options:**

- **(A)** $0 \cdot 3 \mathrm{~cm} / \mathrm{sec}$
- **(B)** $0 \cdot 1 \mathrm{~cm} / \mathrm{sec}$
- **(C)** $0 \cdot 2 \mathrm{~cm} / \mathrm{sec}$
- **(D)** $0 \cdot 4 \mathrm{~cm} / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0 \cdot 1 \mathrm{~cm} / \mathrm{sec}$**

**Detailed Solution:**

(D)
Let $x$ be the side of the square. Then area $A=x^{2}$
$\therefore \frac{\mathrm{d} \mathrm{A}}{\mathrm{dt}}=2 \mathrm{x} \frac{\mathrm{dx}}{\mathrm{dt}} \Rightarrow 0.5=2(10) \frac{\mathrm{d} \mathrm{x}}{\mathrm{dt}}$
$\therefore \frac{\mathrm{dx}}{\mathrm{dt}}=0.025$
Now perimeter $=4 \mathrm{x}=\mathrm{p}$
$\therefore \frac{\mathrm{dp}}{\mathrm{dt}}=4 \frac{\mathrm{dx}}{\mathrm{dt}}=4(0.025)=0.1 \mathrm{~cm} / \mathrm{sec} .$

</details>

---

### Q101. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The approximate value of the function $f(x)=x^{3}-3 x+5$ at $x=1.99$ is

**Options:**

- **(A)** 6.91
- **(B)** 6.94
- **(C)** 7.94
- **(D)** 7.91

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 6.91**

**Detailed Solution:**

(D)
$f(x)=x^{3}-3 x+5 \Rightarrow f^{\prime}(x)=3 x^{2}-3$
Let $a=2, h=-0.01$
$\therefore f(a)=f(2)=2^{3}-3(2)+5=7$
$f^{\prime}(a)=f^{\prime}(2)=3(2)^{2}-3=9$
We know that $f(a+h) \neq f(a)+h f^{\prime}(a)$
$f(1.99) \div 7-(0.01)(9) \div 7-0.09 \neq 6.91$

</details>

---

### Q102. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The approximate value of the function $\mathrm{f}(x)=x^{3}+5 x^{2}-7 x+10$ at $x=1 \cdot 1$ is

**Options:**

- **(A)** $7 \cdot 6$
- **(B)** $8 \cdot 6$
- **(C)** $6 \cdot 6$
- **(D)** $9 \cdot 6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $9 \cdot 6$**

**Detailed Solution:**

Given $f(x)=x^{3}+5 x^{2}-7 x+10 \Rightarrow f^{\prime}(x)=3 x^{2}+10 x-7$
Let $a=1, h=0.1$
$\therefore \mathrm{f}(1)=1+5-7+10=9$ and $\mathrm{f}^{\prime}(1)=3+10-7=6$
We know that $\mathrm{f}(\mathrm{a}+\mathrm{h}) \div \mathrm{f}(\mathrm{a})+\mathrm{hf}^{\prime}(\mathrm{a})$
$f(1.1)=9+(0.1)(6)=9+0.6=9.6$

</details>

---

### Q103. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The approximate value of $\log _{10} 99$ is $\quad\left(\right.$ Given $\log _{10} \mathrm{e}=0.4343$ )

**Options:**

- **(A)** $1.9657$
- **(B)** $1.9857$
- **(C)** $1.1 .9957$
- **(D)** $1.9757$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1.1 .9957$**

**Detailed Solution:**

Let $f(x)=\log _{10} x=\frac{\log _{e} x}{\log _{e} 10}$
$f^{\prime}(x)=\frac{1}{x \log 10}$
Let $\mathrm{a}=100, \mathrm{~h}=-1$
$\therefore f(a)=\log _{10} 100 \quad=\log _{10} 10^{2}=2$
$f^{\prime}(a)=\frac{1}{100 \times \log _{e} 10}=\frac{1}{100} \log _{10} e=\frac{1}{100} \times 0.4343$
We know that
$$
\begin{aligned}
f(a-h) & \doteqdot f(a)+h f^{\prime}(a) \\
& \doteqdot 2+(-1) \times \frac{1}{100}(0.4343)=2-0.004343=1.995657 \\
& \doteqdot 1.9957
\end{aligned}
$$

</details>

---

### Q104. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the displacement of a particle at a point is given by $s=3 t^{2}-12 t+14$, then the
displacement of the particle when its velocity becomes zero is

**Options:**

- **(A)** 14 units
- **(B)** 4 units
- **(C)** 0 units
- **(D)** 2 units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2 units**

**Detailed Solution:**

Given $\quad s \quad=3 t^{2}-12 t+14$
$$
v=\frac{d s}{d t}=6 t-12
$$
When $v=0$, we get $t=2$
$\therefore \mathrm{s}=(3 \times 4)-(12 \times 2)+14=12-24+14=2$ units

</details>

---

### Q105. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A particle moves according to the law $s=t^{3}-6 t^{2}+9 t+25 .$ The displacement of

**Options:**

- **(A)** 0 units
- **(B)** -27 units
- **(C)** 27 units
- **(D)** 9 units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 27 units**

**Detailed Solution:**

Given $s=t^{3}-6 t^{2}+9 t+25$ ....(1)
$$
\begin{array}{l}v=\frac{d s}{d t}=3 t^{2}-12 t+9 \\ \frac{d v}{d t}=6 t-12\end{array}
$$
Given $6 t-12=0 \Rightarrow t=2$
$\therefore$ from $(1), s=(2)^{3}-6 \times 4+18+25=27$

</details>

---

### Q106. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The approximate value of $\cot ^{-1}(1 \cdot 001)$ is

**Options:**

- **(A)** $\frac{\pi}{4}-0 \cdot 0005$
- **(B)** $\frac{\pi}{4}+0 \cdot 005$
- **(C)** $\frac{\pi}{4}+0 \cdot 0005$
- **(D)** $\frac{\pi}{4}-0 \cdot 005$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}-0 \cdot 0005$**

**Detailed Solution:**

Let $f(x)=\cos ^{-1} x \Rightarrow f^{\prime}(x)=\frac{-1}{1+x^{2}}$
Let, $\mathrm{a}=1, \mathrm{~h}=0.001$
Now $\mathrm{f}(\mathrm{a})=\cot ^{-1} 1=\frac{\pi}{4}$ and $\mathrm{f}^{\prime}(\mathrm{a})=\frac{-1}{1+1}=-\frac{1}{2}$
We know that, $f(a+h) \doteqdot f(a)+h f^{\prime}(a)$
$=\frac{\pi}{4}+(0.001)\left(-\frac{1}{2}\right)=\frac{\pi}{4}-0.0005$

</details>

---

### Q107. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The radius of a circle is increasing at the rate $2 \mathrm{~cm} / \mathrm{sec}$. The rate at which its area is
increasing when the radius of the circle is 5 decimeters is

**Options:**

- **(A)** $100 \pi \mathrm{cm}^{2} / \mathrm{sec}$
- **(B)** $200 \pi \mathrm{cm}^{2} / \mathrm{sec}$
- **(C)** $2000 \pi \mathrm{cm}^{2} / \mathrm{sec}$
- **(D)** $20 \pi \mathrm{cm}^{2} / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $200 \pi \mathrm{cm}^{2} / \mathrm{sec}$**

**Detailed Solution:**

Here $\frac{\mathrm{dr}}{\mathrm{dt}}=2$ and $\mathrm{r}=5$ decimeter $=50 \mathrm{~cm}$ 
Now Area of circle $=\mathrm{A}=\pi \mathrm{r}^{2}$.
$\begin{aligned}
\therefore \frac{\mathrm{d} \mathrm{A}}{\mathrm{dt}} &=2 \pi \mathrm{r} \frac{\mathrm{dr}}{\mathrm{dt}} \\
&=2 \times \pi \times 50 \times 2=200 \pi \mathrm{cm}^{2} / \mathrm{sec}
\end{aligned}$

</details>

---

### Q108. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The displacement of a particle at time 't' is $s=t^{3}-4 t^{2}-5 t$, then the velocity of
the particle at $t=2 \mathrm{sec}$. is

**Options:**

- **(A)** $\left(\frac{1}{9}\right)$ units $/ \mathrm{sec}.$
- **(B)** $-9$ units $/ \mathrm{sec}$
- **(C)** 9 units $/ \mathrm{sec}$.
- **(D)** $\left(\frac{-1}{9}\right)$ units $/$ sec.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-9$ units $/ \mathrm{sec}$**

**Detailed Solution:**

Given $s=t^{3}-4 t^{2}-5 t$
$\therefore \frac{d s}{d t}=3 t^{2}-8 t-5$
At $t=2, \quad v=\frac{d s}{d t}=3(4)-8(2)-5=12-16-5=-9$

</details>

---

### Q109. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A stone is dropped into a pond. Waves in the form of circles are generated and radius of outermostripple increases at the rate of <math><mrow><mrow><mn>5</mn><mi></mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi></mrow><mo>/</mo><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mo>.</mo></mrow></mrow></math> Then area increased after <math><mn>2</mn></math> seconds is ________

**Options:**

- **(A)** <math><mn>100</mn><mrow><mrow><mi>π</mi><mi></mi><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>/</mo><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow></mrow></math>
- **(B)** <math><mn>40</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>/</mo><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow></mrow></math>
- **(C)** <math><mn>50</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>/</mo><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow></mrow></math>
- **(D)** <math><mn>25</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>/</mo><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>100</mn><mrow><mrow><mi>π</mi><mi></mi><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>/</mo><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow></mrow></math>**

**Detailed Solution:**

Given: <math><mfrac><mrow><mi>d</mi><mi>r</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>5</mn><mi mathvariant="normal"></mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi><mo>/</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mo>&#8658;</mo><mi>d</mi><mi>r</mi><mo>=</mo><mn>5</mn><mi>d</mi><mi>t</mi></math>  
<math><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">n</mi><mo> </mo><mi>r</mi><mo>=</mo><mn>5</mn><mi>t</mi><mo>+</mo><mi>c</mi><mo>,</mo></math> at <math><mi>t</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi></mi><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>  
<math><mo> </mo><mi>r</mi><mo>=</mo><mn>5</mn><mi>t</mi></math>  
New <math><mi>A</mi><mo>=</mo><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>π</mi><mi>r</mi><mfrac><mrow><mi>d</mi><mi>r</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></math>  
<math><mo>=</mo><mn>2</mn><mi>π</mi><mo>.</mo><mn>10.5</mn></math>  at <math><mi>t</mi><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>10</mn></math>  
<math><mo>=</mo><mn>100</mn><mi mathvariant="normal"></mi><mi>π</mi><mo> </mo><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>/</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mo>.</mo></math>

</details>

---

### Q110. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Using differentiation, approximate value of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></math> at x = 2.99 is ….

**Options:**

- **(A)** 3.96
- **(B)** 9.96
- **(C)** 4.98
- **(D)** 5.98

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3.96**

**Detailed Solution:**

Given function, <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></math>  
<math><mo>&#8658;</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></math>  
Let x = 3 and <math><mi>Δ</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>0.01</mn></math>  
So that <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>Δ</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2.99</mn></mrow></mfenced></math>  
We know that, <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>Δ</mi><mi>x</mi></mrow></mfenced><mo>≈</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mi>Δ</mi><mi>x</mi><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  
<math><mo>≈</mo><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mn>0.01</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>  
Putting x = 3 and <math><mi>Δ</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>0.01</mn></math> , we get 
<math><mi>f</mi><mfenced separators="|"><mrow><mn>2.99</mn></mrow></mfenced><mo>≈</mo><mfenced separators="|"><mrow><msup><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mo>×</mo><mn>3</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mn>0.01</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mo>×</mo><mn>3</mn><mo>-</mo><mn>2</mn></mrow></mfenced></math>  
<math><mo>≈</mo><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mn>0.01</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced></math>  
<math><mo>≈</mo><mn>4</mn><mo>-</mo><mn>0.04</mn><mo>≈</mo><mn>3.96</mn></math>

</details>

---

### Q111. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The edge of a cube is decreasing at the rate of 0.04 cm/sec. If the edge of the cube is 10 cms, then rate of decrease of surface area of the cube is …

**Options:**

- **(A)** <math><mfrac><mrow><mn>4.8</mn><mi></mi><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>4.08</mn><mi></mi><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>48</mn><mi></mi><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>4.008</mn><mi></mi><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>4.8</mn><mi></mi><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow></mfrac></math>**

**Detailed Solution:**

Let edge of a cube be <math><mi>x</mi></math> cm, then surface area of the cube, <math><mi>A</mi><mo>=</mo><mn>6</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
It is given that, <math><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>0.04</mn></math> cm/sec
Now, <math><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>12</mn><mi>x</mi><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></math>
<math><mo>=</mo><mn>12</mn><mi>x</mi><mfenced separators="|"><mrow><mo>-</mo><mn>0.04</mn></mrow></mfenced></math>
<math><mo>=</mo><mo>-</mo><mn>0.48</mn><mi>x</mi></math>
when, <math><mi>x</mi><mo>=</mo><mn>10</mn><mo>,</mo><mi></mi></math> then <math><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>0.48</mn><mo>×</mo><mn>10</mn><mo>=</mo><mo>-</mo><mn>4.8</mn><mfrac><mrow><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow></mfrac></math>

</details>

---

### Q112. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

If the volume of spherical ball is increasing at the rate of <math> <mrow> <mn>4</mn><mi>π</mi> </mrow> </math> <math> <mrow> <mrow><mrow> <mi>c</mi><msup> <mi>m</mi> <mn>3</mn> </msup> </mrow><mo>/</mo><mrow> <mi>sec</mi> </mrow></mrow> </mrow> </math> then the rate of change of its surface area when the volume is <math> <mrow> <mn>288</mn><mi>π</mi><mtext> </mtext><mi>c</mi><msup> <mi>m</mi> <mn>3</mn> </msup> </mrow> </math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>π</mi><mrow><mi> </mi><mrow><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>/</mo><mrow><mi>s</mi><mi>e</mi><mi>c</mi></mrow></mrow></math>
- **(B)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>π</mi><mrow><mi> </mi><mrow><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>/</mo><mrow><mi>s</mi><mi>e</mi><mi>c</mi></mrow></mrow></math>
- **(C)** <math><mn>4</mn><mi> </mi><mi>π</mi><mrow><mi> </mi><mrow><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>/</mo><mrow><mi>s</mi><mi>e</mi><mi>c</mi></mrow></mrow></math>
- **(D)** <math><mn>2</mn><mi>π</mi><mrow><mi> </mi><mrow><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>/</mo><mrow><mi>s</mi><mi>e</mi><mi>c</mi></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>π</mi><mrow><mi> </mi><mrow><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>/</mo><mrow><mi>s</mi><mi>e</mi><mi>c</mi></mrow></mrow></math>**

**Detailed Solution:**

<math> <mrow> <mi>V</mi><mo>=</mo><mfrac> <mn>4</mn> <mn>3</mn> </mfrac> <mi>π</mi><msup> <mi>r</mi> <mn>3</mn> </msup> <mo>⇒</mo><mfrac> <mrow> <mi>d</mi><mi>V</mi></mrow> <mrow> <mi>d</mi><mi>t</mi></mrow> </mfrac> <mo>=</mo><mn>4</mn><mi>π</mi><msup> <mi>r</mi> <mn>2</mn> </msup> <mfrac> <mrow> <mi>d</mi><mi>r</mi></mrow> <mrow> <mi>d</mi><mi>t</mi></mrow> </mfrac> </mrow> </math>
When <math><mi>V</mi><mo>-</mo><mn>288</mn><mi>π</mi></math>
<math><mn>288</mn><mi> </mi><mi>π</mi><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>⇒</mo><mi>r</mi><mo>=</mo><mn>6</mn></math>
Now <math><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>4</mn><mi>π</mi></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mn>4</mn><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mfrac><mrow><mi>d</mi><mi>r</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>4</mn><mi>π</mi><mo>=</mo><mfrac><mrow><mi>d</mi><mi>r</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
A = surface area <math><mo>=</mo><mn>4</mn><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mo>∴</mo><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>8</mn><mi>π</mi><mi>r</mi><mfrac><mrow><mi>d</mi><mi>r</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>8</mn><mi>π</mi><mi>r</mi><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>8</mn><mi>π</mi></mrow><mrow><mi>r</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>8</mn><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>

</details>

---

### Q113. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

The point on the curve <math><mn>6</mn><mi>y</mi><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>2</mn></math> at which <math> <mrow> <mi>y</mi><mo>−</mo> </mrow> </math> co-ordinate is changing <math> <mn>8</mn> </math> times as fast as <math> <mrow> <mi>x</mi><mo>−</mo> </mrow> </math> co-ordinate is ________

**Options:**

- **(A)** <math><mo>(</mo><mn>4</mn><mo>,</mo><mn>11</mn><mo>)</mo></math>
- **(B)** <math><mo>(</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>11</mn><mo>)</mo></math>
- **(C)** <math > <mrow>  <mrow><mo>(</mo>   <mrow>    <mo>&#x2212;</mo><mn>4</mn><mo>,</mo><mn>11</mn>   </mrow>  <mo>)</mo></mrow> </mrow></math>
- **(D)** <math><mo>(</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>11</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>(</mo><mn>4</mn><mo>,</mo><mn>11</mn><mo>)</mo></math>**

**Detailed Solution:**

<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>8</mn></math>
<math><mo>⇒</mo><mi>x</mi><mo>=</mo><mi> </mi><mo>±</mo><mn>4</mn></math>
Substituting value of x in the curve, we get <math><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mi> </mi><mn>11</mn></mrow></mfenced><mo>,</mo><mi> </mi><mo>(</mo><mo>-</mo><mn>4</mn><mo>,</mo><mi> </mi><mo>-</mo><mfrac><mrow><mn>31</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>)</mo></math>

</details>

---

### Q114. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

The approximate value of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mi> </mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>5</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>9</mn><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi> </mi><mi>x</mi><mo>=</mo><mn>1.1</mn></math> is

**Options:**

- **(A)** <math><mn>8.6</mn></math>
- **(B)** <math><mn>8.5</mn></math>
- **(C)** <math><mn>8.4</mn></math>
- **(D)** <math><mn>8.3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>8.6</mn></math>**

**Detailed Solution:**

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mi>h</mi><mi> </mi><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>
Here, <math><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi>h</mi><mo>=</mo><mn>0.1</mn><mo>,</mo><mi> </mi><msup><mrow><mi>f</mi></mrow><mrow><mi>'</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>10</mn><mi>x</mi><mo>-</mo><mn>7</mn></math>
<math><mo>∴</mo><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>0.1</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>+</mo><mn>0.1</mn><mi> </mi><mo>×</mo><mi>f</mi><mi>'</mi><mo>(</mo><mn>1</mn><mo>)</mo></math>
<math><mo>=</mo><mn>8</mn><mo>+</mo><mn>0.1</mn><mi> </mi><mo>×</mo><mn>6</mn></math>
<math><mo>=</mo><mn>8.6</mn></math>

</details>

---

### Q115. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

The height of right circular cylinder of maximum volume inscribed in a sphere of diameter $2 a$ is

**Options:**

- **(A)** $2 \sqrt{3} a$
- **(B)** $\sqrt{3} a$
- **(C)** $\frac{2 a}{\sqrt{3}}$
- **(D)** $\frac{a}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2 a}{\sqrt{3}}$**

**Detailed Solution:**

Let the radius and height of the cylinder are and $h$, respectively.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/F2DXSEKSRvmuhVwpM35Nu44kM7b7fDXt13sq3cEgXHY.original.fullsize.png">

In $\triangle A O M$
$\therefore$
$$
\begin{array}{l}
r^{2}+\left(\frac{h^{2}}{4}\right)=a^{2} \\
h^{2}=4\left(a^{2}-r^{2}\right)
\end{array}
$$
Now, $V=\pi r^{2} h=\pi\left(a^{2} h-\frac{1}{4} h^{3}\right)$
For max or min,
$$
\begin{aligned}
& \frac{d V}{d h} &=\pi\left(a^{2}-\frac{3}{4} h^{2}\right)=0 \\
\Rightarrow & h &=\left(\frac{2}{\sqrt{3}}\right) a
\end{aligned}
$$
Now, $\quad \frac{d^{2} V}{d h^{2}}=-\frac{6 h}{4} < 0$
So, $V$ is maximum at $h=\frac{2 a}{\sqrt{3}}$.

</details>

---

### Q116. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

Divide 10 into two parts such that the sum of double of the first and the square of the second is minimum

**Options:**

- **(A)** $(6,4)$
- **(B)** $(7,3)$
- **(C)** $(8,2)$
- **(D)** $(9,1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(9,1)$**

**Detailed Solution:**

Let $x$ and $y$ be the two parts of the number 10 .
$\therefore$
$x+y=10\ldots$ (i)
According to the question, Let $\quad \begin{aligned} A &=2 x+y^{2} \\ &=2 x+(10-x)^{2} \\ &=2 x+100+x^{2}-20 x \\ &=x^{2}-18 x+100 \end{aligned}$
On differentiating w.r.t. $x$, we get $\frac{d A}{d x}=2 x-18$
For max or min of $A$, Put $\quad \frac{d A}{d x}=0=2 x-18$
$\Rightarrow$
$x=9$
Now, $\quad \frac{d^{2} A}{d x^{2}}=2>0 \quad(\min )$
On putting $x=9$ in Eq. (i), we get $y=1$
$\therefore \quad(x, y)=(9,1)$

</details>

---

### Q117. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

The approximate value of $\sqrt[3]{28}$ is

**Options:**

- **(A)** $3.0037$
- **(B)** $3.037$
- **(C)** $3.0086$
- **(D)** $3.37$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3.037$**

**Detailed Solution:**

Let $y=\sqrt[3]{28}$
Taking log on both sides, we get
$=3.037$ (approximately)

</details>

---

### Q118. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `2`

The maximum area of the rectangle that can be inscribed in a circle of radius $r$, is

**Options:**

- **(A)** $\pi r^{2}$
- **(B)** $r^{2}$
- **(C)** $\pi r^{2} / 4$
- **(D)** $2 r^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 r^{2}$**

**Detailed Solution:**

Area of rectangle,
$$
\begin{aligned}
A &=2 x \cdot 2 \sqrt{r^{2}-x^{2}} \\
&=4 x \sqrt{r^{2}-x^{2}} \\
\frac{d A}{d x} &=\frac{4\left(r^{2}-2 x^{2}\right)}{\sqrt{r^{2}-x^{2}}}
\end{aligned}
$$
For maximum or minimum put $\frac{d A}{d x}=0$
$$
\Rightarrow \quad x=r / \sqrt{2}
$$
It can be easily checked that $\frac{d^{2} A}{d x^{2}} < 0$ for this value of $x$. $\therefore A$ is maximum for $x=\frac{r}{\sqrt{2}}$ and the maximum value of $A$ is given by
$$
A=4 \frac{r}{\sqrt{2}} \sqrt{r^{2}-\frac{r^{2}}{2}}=2 r^{2}
$$

</details>

---

### Q119. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

The positive root of $x^{2}-78.8=0$ after first approximation by Newton Raphson method assuming initial approximation to the root is 14, is

**Options:**

- **(A)** $9.821$
- **(B)** $9.814$
- **(C)** $9.715$
- **(D)** $9.915$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $9.814$**

**Detailed Solution:**

Here, $\quad x_{0}=14, f(x)=x^{2}-78.8$
and $f^{\prime}(x)=2 x$
$$
\begin{aligned}
\therefore \quad x_{1}=x_{0}-& \frac{f\left(x_{0}\right)}{f^{\prime}\left(x_{0}\right)} \\
&=14-\frac{(14)^{2}-(78.8)}{2 \times 14}=9.814
\end{aligned}
$$

</details>

---

