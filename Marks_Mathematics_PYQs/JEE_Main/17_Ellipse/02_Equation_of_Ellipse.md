# JEE Main Mathematics - Ellipse

## Topic 2: Equation of Ellipse

**Total Questions:** 69

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\dfrac{x^2}{f(a^2+7a+3)} + \dfrac{y^2}{f(3a+15)} = 1$ represent an ellipse with major axis along $y$-axis, where $f$ is a strictly decreasing positive function on $\mathbb{R}$. If the set of all possible values of $a$ is $\mathbb{R} - [\alpha, \beta]$, then $\alpha^2+\beta^2$ is equal to:

**Options:**

- **(A)** $28$
- **(B)** $40$
- **(C)** $61$
- **(D)** $24$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $40$**

**Detailed Solution:**

For the given equation to represent an ellipse with its major axis along the $y$-axis, the denominator of $y^2$ must be strictly greater than the denominator of $x^2$.

$f(3a+15) > f(a^2+7a+3)$

Since $f$ is given as a strictly decreasing positive function on $\mathbb{R}$, the inequality sign reverses for the arguments:

$3a+15 < a^2+7a+3$

$a^2 + 4a - 12 > 0$

$(a+6)(a-2) > 0$

The solution to this inequality is $a \in (-\infty, -6) \cup (2, \infty)$.

This can be rewritten in terms of the set difference as $a \in \mathbb{R} - [-6, 2]$.

Comparing this with the given set $\mathbb{R} - [\alpha, \beta]$, we get $\alpha = -6$ and $\beta = 2$.

$\alpha^2 + \beta^2 = (-6)^2 + (2)^2 = 36 + 4 = 40$

Answer: $40$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $x = 9$ be a directrix of an ellipse $E$, whose centre is at the origin and eccentricity is $\dfrac{1}{3}$. Let $P(\alpha, 0)$, $\alpha > 0$, be a focus of $E$ and $AB$ be a chord passing through $P$. Then the locus of the mid point of $AB$ is :

**Options:**

- **(A)** $9y^2 = 8x(1-x)$
- **(B)** $3y^2 = 4x(1-x)$
- **(C)** $9y^2 = 8x(x-1)$
- **(D)** $3y^2 = 4x(x-1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $9y^2 = 8x(1-x)$**

**Detailed Solution:**

Given the directrix of the ellipse is $x = \dfrac{a}{e} = 9$ and eccentricity $e = \dfrac{1}{3}$.

$\dfrac{a}{1/3} = 9 \Rightarrow a = 3$

The value of $b^2$ is given by $b^2 = a^2(1 - e^2) = 9\left(1 - \dfrac{1}{9}\right) = 8$.

The equation of the ellipse is $\dfrac{x^2}{9} + \dfrac{y^2}{8} = 1$.

The focus $P(\alpha, 0)$ for $\alpha > 0$ is at $(ae, 0) = \left(3 \times \dfrac{1}{3}, 0\right) = (1, 0)$.

Let the midpoint of the chord $AB$ be $(h, k)$. The equation of the chord in terms of its midpoint is given by $T = S_1$ :

$\dfrac{hx}{9} + \dfrac{ky}{8} = \dfrac{h^2}{9} + \dfrac{k^2}{8}$

Since the chord passes through the focus $P(1, 0)$, substituting $x = 1$ and $y = 0$ gives:

$\dfrac{h}{9} = \dfrac{h^2}{9} + \dfrac{k^2}{8}$

$\dfrac{k^2}{8} = \dfrac{h}{9} - \dfrac{h^2}{9}$

$9k^2 = 8h(1 - h)$

Replacing $(h, k)$ with $(x, y)$, the locus of the midpoint is:

$9y^2 = 8x(1 - x)$

Answer: $9y^2 = 8x(1-x)$

</details>

---

### Q3. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The eccentricity of an ellipse $E$ with centre at the origin $O$ is $\dfrac{\sqrt{3}}{2}$ and its directrices are $x = \pm \dfrac{4\sqrt{6}}{3}$. Let $H: \dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ be a hyperbola whose eccentricity is equal to the length of semi-major axis of $E$, and whose length of latus rectum is equal to the length of minor axis of $E$. Then the distance between the foci of $H$ is :

**Options:**

- **(A)** $\dfrac{4\sqrt{2}}{\sqrt{7}}$
- **(B)** $\dfrac{4\sqrt{2}}{7}$
- **(C)** $\dfrac{4}{\sqrt{7}}$
- **(D)** $\dfrac{8}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{8}{7}$**

**Detailed Solution:**

For the ellipse $E$, the eccentricity is $e_E = \dfrac{\sqrt{3}}{2}$ and the directrices are $x = \pm \dfrac{a_E}{e_E} = \pm \dfrac{4\sqrt{6}}{3}$.

The semi-major axis $a_E$ is given by:

$a_E = e_E \times \dfrac{4\sqrt{6}}{3} = \dfrac{\sqrt{3}}{2} \times \dfrac{4\sqrt{6}}{3} = \dfrac{12\sqrt{2}}{6} = 2\sqrt{2}$

The semi-minor axis $b_E$ is given by:

$b_E^2 = a_E^2(1 - e_E^2) = (2\sqrt{2})^2 \left(1 - \dfrac{3}{4}\right) = 8 \times \dfrac{1}{4} = 2 \Rightarrow b_E = \sqrt{2}$

For the hyperbola $H: \dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$, its eccentricity $e_H$ is equal to the semi-major axis of $E$:

$e_H = a_E = 2\sqrt{2}$

The length of the latus rectum of $H$ is equal to the length of the minor axis of $E$ ($2b_E$):

$\dfrac{2b^2}{a} = 2b_E = 2\sqrt{2} \Rightarrow b^2 = \sqrt{2}a$

Using the standard relation for a hyperbola $b^2 = a^2(e_H^2 - 1)$, we substitute $b^2$ and $e_H$:

$\sqrt{2}a = a^2((2\sqrt{2})^2 - 1)$

$\sqrt{2}a = a^2(8 - 1) = 7a^2$

Since $a > 0$, dividing by $a$ gives:

$a = \dfrac{\sqrt{2}}{7}$

The distance between the foci of the hyperbola $H$ is $2ae_H$:

$2ae_H = 2 \times \dfrac{\sqrt{2}}{7} \times 2\sqrt{2} = \dfrac{8}{7}$

Answer: $\dfrac{8}{7}$

</details>

---

### Q4. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let a focus of the ellipse $E: \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ be $S(4, 0)$ and its eccentricity be $\dfrac{4}{5}$. If the point $P(3, \alpha)$ lies on $E$ and $O$ is the origin, then the area of $\triangle POS$ is equal to:

**Options:**

- **(A)** $12/5$
- **(B)** $14/5$
- **(C)** $24/5$
- **(D)** $48/5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $24/5$**

**Detailed Solution:**

Given the focus of the ellipse $S(4, 0)$, we have $ae = 4$.

Since the eccentricity $e = \dfrac{4}{5}$, we get $a \left(\dfrac{4}{5}\right) = 4 \Rightarrow a = 5$.

Using the relation $b^2 = a^2(1 - e^2)$, we find:

$b^2 = 25 \left(1 - \dfrac{16}{25}\right) = 9$

The equation of the ellipse is $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$.

Since the point $P(3, \alpha)$ lies on the ellipse, substituting $x = 3$ gives:

$\dfrac{9}{25} + \dfrac{\alpha^2}{9} = 1$

$\dfrac{\alpha^2}{9} = 1 - \dfrac{9}{25} = \dfrac{16}{25}$

$\alpha^2 = \dfrac{144}{25} \Rightarrow |\alpha| = \dfrac{12}{5}$

The coordinates of the vertices of $\triangle POS$ are $O(0, 0)$, $S(4, 0)$, and $P\left(3, \pm \dfrac{12}{5}\right)$.

The area of $\triangle POS$ is $\dfrac{1}{2} \times \text{base} \times \text{height}$.

Taking $OS$ as the base, the length is $4$, and the height is the absolute value of the y-coordinate of $P$, which is $\dfrac{12}{5}$.

Area $= \dfrac{1}{2} \times 4 \times \dfrac{12}{5} = \dfrac{24}{5}$

Answer: $24/5$

</details>

---

### Q5. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let an ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$, $a < b$, pass through the point $(4, 3)$ and have eccentricity $\dfrac{\sqrt{5}}{3}$. Then the length of its latus rectum is :

**Options:**

- **(A)** $\dfrac{4\sqrt{5}}{3}$
- **(B)** $2\sqrt{5}$
- **(C)** $\dfrac{7\sqrt{5}}{3}$
- **(D)** $\dfrac{8\sqrt{5}}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{8\sqrt{5}}{3}$**

**Detailed Solution:**

Given the equation of the ellipse is $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ with $a < b$.

The eccentricity is given by $e = \dfrac{\sqrt{5}}{3}$.

Since $a < b$, the relation between $a$, $b$, and $e$ is $a^2 = b^2(1 - e^2)$.

Substituting the value of $e$:

$a^2 = b^2\left(1 - \dfrac{5}{9}\right) = \dfrac{4}{9}b^2$

The ellipse passes through the point $(4, 3)$, so substituting $x = 4$ and $y = 3$ into the equation of the ellipse gives:

$\dfrac{16}{a^2} + \dfrac{9}{b^2} = 1$

Substituting $a^2 = \dfrac{4}{9}b^2$ into the above equation:

$\dfrac{16}{\dfrac{4}{9}b^2} + \dfrac{9}{b^2} = 1$

$\dfrac{36}{b^2} + \dfrac{9}{b^2} = 1$

$\dfrac{45}{b^2} = 1 \implies b^2 = 45$

Now, finding $a^2$:

$a^2 = \dfrac{4}{9} \times 45 = 20$

For an ellipse with $a < b$, the length of the latus rectum is given by $\dfrac{2a^2}{b}$.

Substituting the values of $a^2$ and $b = \sqrt{45} = 3\sqrt{5}$:

Length of latus rectum $= \dfrac{2 \times 20}{3\sqrt{5}} = \dfrac{40}{3\sqrt{5}} = \dfrac{8\sqrt{5}}{3}$

Answer: $\dfrac{8\sqrt{5}}{3}$

</details>

---

### Q6. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the ellipse $\mathrm{E}: \frac{x^{2}}{144}+\frac{y^{2}}{169}=1$ and the hyperbola $\mathrm{H}: \frac{x^{2}}{16}-\frac{y^{2}}{\lambda^{2}}=-1$ have the same foci. If e and L respectively denote the eccentricity and the length of the latus rectum of H, then the value of $24(\mathrm{e}+\mathrm{L})$ is :

**Options:**

- **(A)** 148
- **(B)** 126
- **(C)** 67
- **(D)** 296

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 296**

**Detailed Solution:**

Ellipse E: $\frac{x^2}{144} + \frac{y^2}{169} = 1$ has $a^2 = 169, b^2 = 144$, so $c_E = \sqrt{25} = 5$ with foci at $(0, \pm 5)$.
Hyperbola H: $\frac{y^2}{x^2} - \frac{x^2}{16} = 1$ has the same foci, so $c_H^2 = x^2 + 16 = 25$, giving $x^2 = 9$.
Thus H is $\frac{y^2}{9} - \frac{x^2}{16} = 1$ with $a = 3, b = 4, c = 5$.
Eccentricity: $e = \frac{5}{3}$.
Latus rectum: $L = \frac{2b^2}{a} = \frac{32}{3}$.
Therefore $24(e + L) = 24\left(\frac{5}{3} + \frac{32}{3}\right) = 24 \cdot \frac{37}{3} = 296$

</details>

---

### Q7. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An ellipse has its center at $(1,-2)$, one focus at $(3,-2)$ and one vertex at $(5,-2)$. Then the length of its latus rectum is :

**Options:**

- **(A)** 6
- **(B)** $4 \sqrt{3}$
- **(C)** $\frac{16}{\sqrt{3}}$
- **(D)** $6 \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 6**

**Detailed Solution:**

Center at $(1, -2)$, focus at $(3, -2)$, vertex at $(5, -2)$ lie on horizontal line. 
Distance from center to focus: $c = 2$.
Distance from center to vertex: $a = 4$.
Since $b^2 = a^2 - c^2 = 16 - 4 = 12$.
Length of latus rectum: $L = \dfrac{2b^2}{a} = \dfrac{2(12)}{4} = 6$

</details>

---

### Q8. JEE Main 2026 (24 January Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $(h, k)$ lie on the circle $\mathrm{C}: x^{2}+y^{2}=4$ and the point $(2 h+1,3 k+2)$ lie on an ellipse with eccentricity $e$. Then the value of $\frac{5}{e^{2}}$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

Since $(h, k)$ lies on circle $x^2 + y^2 = 4$, we have $h = 2\cos\theta$ and $k = 2\sin\theta$.
The transformed point is $(2h+1, 3k+2) = (4\cos\theta + 1, 6\sin\theta + 2)$.
Rearranging: $\frac{(x-1)^2}{16} + \frac{(y-2)^2}{36} = 1$
This is an ellipse with $a^2 = 36$, $b^2 = 16$, so $e^2 = 1 - \frac{b^2}{a^2} = 1 - \frac{16}{36} = \frac{5}{9}$
Therefore $\frac{5}{e^2} = \frac{5}{5/9} = 9$

</details>

---

### Q9. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the length of the latus rectum of an ellipse $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1,(a>b)$, be 30. If its eccentricity is the maximum value of the function $f(t)=-\frac{3}{4}+2 t-t^{2}$, then ($a^{2}+b^{2}$) is equal to

**Options:**

- **(A)** 276
- **(B)** 256
- **(C)** 516
- **(D)** 496

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 496**

**Detailed Solution:**

$f(t) = -t^2 + 2t - \frac{3}{4} = -(t-1)^2 + \frac{1}{4}$.
Maximum value $= \frac{1}{4}$, so $e = \frac{1}{4}$.
$b^2 = a^2(1 - e^2) = a^2\left(1 - \frac{1}{16}\right) = \frac{15a^2}{16}$.
Latus rectum $= \frac{2b^2}{a} = \frac{2 \cdot 15a^2/16}{a} = \frac{15a}{8} = 30 \Rightarrow a = 16$.
$b^2 = \frac{15 \times 256}{16} = 240$.
$a^2 + b^2 = 256 + 240 = 496$.

</details>

---

### Q10. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let each of the two ellipses $\mathrm{E}_{1}: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1,(a>b)$ and $\mathrm{E}_{2}: \frac{x^{2}}{\mathrm{~A}^{2}}+\frac{y^{2}}{\mathrm{~B}^{2}}=1,(\mathrm{~A}<\mathrm{B})$ have eccentricity $\frac{4}{5}$. Let the lengths of the latus recta of $E_{1}$ and $E_{2}$ be $l_{1}$ and $l_{2}$, respectively, such that $2 l_{1}^{2}=9 l_{2}$. If the distance between the foci of $E_{1}$ is 8, then the distance between the foci of $E_{2}$ is

**Options:**

- **(A)** $\frac{32}{5}$
- **(B)** $\frac{8}{5}$
- **(C)** $\frac{16}{5}$
- **(D)** $\frac{96}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{32}{5}$**

**Detailed Solution:**

Both ellipses have $e = 4/5$.
For $E_1$ ($a > b$):
$b^2 = a^2(1-e^2) = 9a^2/25$. 
Latus rectum $l_1 = 2b^2/a = 18a/25$.
Distance between foci of $E_1$:
$2ae = 8a/5 = 8 \Rightarrow a = 5$, so $l_1 = 18/5$.
For $E_2$ ($A < B$, major axis along $y$):
$A^2 = B^2(1-e^2) = 9B^2/25$. 
Latus rectum $l_2 = 2A^2/B = 18B/25$.
Given $2l_1^2 = 9l_2$:
$2 \cdot \frac{324}{25} = 9 \cdot \frac{18B}{25} \Rightarrow 648 = 162B \Rightarrow B = 4$.
Distance between foci of $E_2 = 2Be = 2 \cdot 4 \cdot \frac{4}{5} = \frac{32}{5}$

</details>

---

### Q11. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the line $y-x=1$ intersect the ellipse $\frac{x^{2}}{2}+\frac{y^{2}}{1}=1$ at the points A and B. Then the angle made by the line segment AB at the center of the ellipse is :

**Options:**

- **(A)** $\frac{\pi}{2}+\tan ^{-1}\left(\frac{1}{4}\right)$
- **(B)** $\frac{\pi}{2}+2 \tan ^{-1}\left(\frac{1}{4}\right)$
- **(C)** $\frac{\pi}{2}-\tan ^{-1}\left(\frac{1}{4}\right)$
- **(D)** $\pi-\tan ^{-1}\left(\frac{1}{4}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{2}+\tan ^{-1}\left(\frac{1}{4}\right)$**

**Detailed Solution:**

<img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/23S1_s_15_1.png">
By solving line & equation of ellipse we get $x = 0$
& $x = -\dfrac{4}{3}$
$\therefore B\left(-\dfrac{4}{3}, -\dfrac{1}{3}\right)$
$m_{OB} = \tan\theta = \dfrac{1}{4}$
$\therefore \angle AOB = \dfrac{\pi}{2} + \theta = \dfrac{\pi}{2} + \tan^{-1}\dfrac{1}{4}$

</details>

---

### Q12. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let S and $\mathrm{S}^{\prime}$ be the foci of the ellipse $\frac{x^{2}}{25}+\frac{y^{2}}{9}=1$ and $\mathrm{P}(\alpha, \beta)$ be a point on the ellipse in the first quadrant. If $(\mathrm{SP})^{2}+\left(\mathrm{S}^{\prime} \mathrm{P}\right)^{2}-\mathrm{SP} \cdot \mathrm{S}^{\prime} \mathrm{P}=37$, then $\alpha^{2}+\beta^{2}$ is equal to :

**Options:**

- **(A)** 15
- **(B)** 11
- **(C)** 17
- **(D)** 13

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 13**

**Detailed Solution:**

For the ellipse $\frac{x^2}{25} + \frac{y^2}{9} = 1$, we have $a = 5$, $b = 3$, $c = 4$.
So foci are at $S(\pm 4, 0)$.
For point $P$ on the ellipse: $SP + S'P = 10$.
Given $(SP)^2 + (S'P)^2 - SP \cdot S'P = 37$
Let $r_1 = SP$ and $r_2 = S'P$.
From $(r_1 + r_2)^2 = 100$, we get $r_1^2 + r_2^2 = 100 - 2r_1r_2$.
Substituting into the given equation: $100 - 3r_1r_2 = 37$, so $r_1r_2 = 21$.
Thus $r_1 = 3, r_2 = 7$.
From $(\alpha + 4)^2 + \beta^2 = 9$ and $(\alpha - 4)^2 + \beta^2 = 49$, subtracting gives $16\alpha = -40$, so $\alpha = -\frac{5}{2}$.
From the ellipse equation: $\beta^2 = \frac{27}{4}$.
Therefore $\alpha^2 + \beta^2 = \frac{25}{4} + \frac{27}{4} = 13$.

</details>

---

### Q13. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the line $\alpha x+4 y=\sqrt{7}$, where $\alpha \in \mathbf{R}$, touches the ellipse $3 x^{2}+4 y^{2}=1$ at the point P in the first quadrant, then one of the focal distances of $P$ is :

**Options:**

- **(A)** $\frac{1}{\sqrt{3}}+\frac{1}{2 \sqrt{7}}$
- **(B)** $\frac{1}{\sqrt{3}}-\frac{1}{2 \sqrt{5}}$
- **(C)** $\frac{1}{\sqrt{3}}+\frac{1}{2 \sqrt{5}}$
- **(D)** $\frac{1}{\sqrt{3}}-\frac{1}{2 \sqrt{11}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\sqrt{3}}+\frac{1}{2 \sqrt{7}}$**

**Detailed Solution:**

Ellipse $3x^2 + 4y^2 = 1$: $a^2 = \frac{1}{3}$, $b^2 = \frac{1}{4}$, $e = \frac{1}{2}$.
Tangent at $(x_0, y_0)$: $3x_0x + 4y_0y = 1$.
Comparing with $\alpha x + 4y = \sqrt{7}$:
$4y_0 = \frac{4}{\sqrt{7}} \Rightarrow y_0 = \frac{1}{\sqrt{7}}$ and $3x_0 = \frac{\alpha}{\sqrt{7}}$.
Substituting in ellipse equation: $\frac{\alpha^2}{21} + \frac{4}{7} = 1 \Rightarrow \alpha^2 = 9 \Rightarrow \alpha = 3$.
$P = \left(\frac{1}{\sqrt{7}}, \frac{1}{\sqrt{7}}\right)$.
Focal distances $= a \pm ex_0 = \frac{1}{\sqrt{3}} \pm \frac{1}{2\sqrt{7}}$.
One focal distance is $\frac{1}{\sqrt{3}} + \frac{1}{2\sqrt{7}}$.

</details>

---

### Q14. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the ellipse $3 x^2+\mathrm{py}^2=4$ pass through the centre $C$ of the circle $x^2+y^2-2 x-4 y-11=0$ of radius $r$. Let $f_1, f_2$ be the focal distances of the point C on the ellipse. Then $6 f_1 f_2-r$ is equal to

**Options:**

- **(A)** 74
- **(B)** 68
- **(C)** 70
- **(D)** 78

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 70**

**Detailed Solution:**

$\mathrm{E}: \frac{\mathrm{x}^2}{4 / 3}+\frac{\mathrm{y}^2}{4 / \mathrm{P}}=1$
Centre of circle ( 1,2 ), radius
$\begin{aligned}
& \mathrm{r}=\sqrt{1+4+11} \\
& \mathrm{r}=4
\end{aligned}$
$\because$ E pass from centre $(1,2)$
$\therefore \frac{3}{4}+\mathrm{P}=1$
$\mathrm{P}=\frac{1}{4} \quad \therefore$ vertical ellipse
$\begin{aligned} & \mathrm{e}=\sqrt{1-\frac{4 / 3}{16}}=\sqrt{1-\frac{1}{12}}=\sqrt{\frac{11}{12}} \\ & \therefore \text { Focal distance of } \mathrm{C}(\mathrm{h}, \mathrm{k}) \\ & =\mathrm{b} \pm \mathrm{ek} \\ & \mathrm{F}_1=4+\sqrt{\frac{11}{12}} \times 2 \\ & \mathrm{~F}_2=4-\sqrt{\frac{11}{12}} \times 2 \\ & \therefore \mathrm{~F}_1 \mathrm{~F}_2=16-\frac{11}{3}=\frac{37}{3} \\ & \therefore 6 \mathrm{~F}_1 \mathrm{~F}_2-\mathrm{r}=74-4=70\end{aligned}$

</details>

---

### Q15. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the length of a latus rectum of an ellipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ be 10 . If its eccentricity is the minimum value of the function $f(\mathrm{t})=\mathrm{t}^2+\mathrm{t}+\frac{11}{12}$, $\mathrm{t} \in \mathbf{R}$, then $\mathrm{a}^2+\mathrm{b}^2$ is equal to :

**Options:**

- **(A)** 125
- **(B)** 126
- **(C)** 120
- **(D)** 115

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 126**

**Detailed Solution:**

Length of LR $=\frac{2 b^2}{a}=10 \Rightarrow 5 \mathrm{a}=\mathrm{b}^2$...(1)
$\begin{aligned} & \mathrm{f}(\mathrm{t})=\mathrm{t}^2+\mathrm{t}+\frac{11}{12} \\ & \frac{\mathrm{df}(\mathrm{t})}{\mathrm{dt}}=2 \mathrm{t}+1=0 \Rightarrow \mathrm{t}=\frac{-1}{2} \\ & \text { Min value of } \mathrm{f}(\mathrm{t})=\left(\frac{-1}{2}\right)^2+\left(\frac{-1}{2}\right)+\frac{11}{12} \\ & =\frac{1}{4} \frac{-1}{2}+\frac{11}{12}=\frac{3-6+11}{12}=\frac{8}{12}=\frac{2}{3}=\mathrm{e} \\ & \mathrm{e}^2=\frac{1-\mathrm{b}^2}{\mathrm{a}^2} \Rightarrow \frac{4}{9}=\frac{1-\mathrm{b}^2}{\mathrm{a}^2}\end{aligned}$
$\Rightarrow \frac{\mathrm{b}^2}{\mathrm{a}^2}=\frac{1-4}{\mathrm{a}}=\frac{5}{\mathrm{a}} \Rightarrow \mathrm{b}^2=\frac{5 \mathrm{a}^2}{\mathrm{a}}$...(2)
$\begin{aligned} & \text { From (1) \& (2) } \\ & 5 \mathrm{a}=\frac{5 \mathrm{a}^2}{\mathrm{a}} \Rightarrow \mathrm{a}=9, \quad \mathrm{~b}=\sqrt{45}=3 \sqrt{5} \\ & \therefore \mathrm{a} 2+\mathrm{b} 2=81+45=126\end{aligned}$

</details>

---

### Q16. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let
$A=\{(\alpha, \beta) \in \mathbf{R} \times \mathbf{R}:|\alpha-1| \leq 4 \text { and }|\beta-5| \leq 6\}$
and
$B=\left\{(\alpha, \beta) \in \mathbf{R} \times \mathbf{R}: 16(\alpha-2)^2+9(\beta-6)^2 \leq 144\right\}$

**Options:**

- **(A)** $\mathrm{B} \subset \mathrm{A}$
- **(B)** $\mathrm{A} \cup \mathrm{B}=\{(\mathrm{x}, \mathrm{y}):-4 \leq \mathrm{x} \leq 4,-1 \leq \mathrm{y} \leq 11\}$
- **(C)** neither $\mathrm{A} \subset \mathrm{B}$ nor $\mathrm{B} \subset \mathrm{A}$
- **(D)** $A \subset B$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{B} \subset \mathrm{A}$**

**Detailed Solution:**

$\begin{aligned} & \text { A : }|x-1| \leq 4 \text { and }|y-5| \leq 6 \\ & \Rightarrow-4 \leq x-1 \leq 4 \Rightarrow-6 \leq y-5 \leq 6 \\ & \Rightarrow-3 \leq x \leq 5 \quad \Rightarrow-1 \leq y \leq 11 \\ & \text { B : } 16(x-2)^2+9(y-6)^2 \leq 144 \\ & \text { B : } \frac{(x-2)^2}{9}+\frac{(y-6)^2}{16} \leq 1\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/gtdjsS85poiLSJpjf8mW6lPz7SF-nQFG2XIAdCutYoQ.original.fullsize.png"/>
From Diagram $\mathrm{B} \subset \mathrm{A}$

</details>

---

### Q17. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The centre of a circle C is at the centre of the ellipse $E: \frac{x^2}{a^2}+\frac{y^2}{b^2}=1, a \gt b$. Let $C$ pass through the foci $F_1$ and $F_2$ of $E$ such that the circle $C$ and the ellipse $E$ intersect at four points. Let P be one of these four points. If the area of the triangle $\mathrm{PF}_1 \mathrm{~F}_2$ is 30 and the length of the major axis of E is 17 , then the distance between the foci of E is :

**Options:**

- **(A)** $26$
- **(B)** $13$
- **(C)** $12$
- **(D)** $\frac{13}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $13$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/P5v5VzYrzx3MQIWHP7NUKu3oBqkodytEKexXHZJTtjM.original.fullsize.png"/>
$\begin{aligned} & \frac{1}{2} \mathrm{PF}_1 \cdot \mathrm{PF}_2=30 \\ & \mathrm{PF}_1+\mathrm{PF}_2=17 \\ & \mathrm{PF}_1=12 \mathrm{PF}_2=5 \\ & \mathrm{~F}_1 \mathrm{~F}_2=13 \\ & \text { option }(2)\end{aligned}$

</details>

---

### Q18. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The length of the latus-rectum of the ellipse, whose foci are $(2,5)$ and $(2,-3)$ and eccentricity is $\frac{4}{5}$, is

**Options:**

- **(A)** $\frac{6}{5}$
- **(B)** $\frac{50}{3}$
- **(C)** $\frac{10}{3}$
- **(D)** $\frac{18}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{18}{5}$**

**Detailed Solution:**

$\begin{aligned} & 2 \mathrm{be}=8 \\ & \mathrm{be}=4\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/LrF2nsCJkE8PkRigK8F_PISXXvp1yR8_yPcqxKgSUHY.original.fullsize.png"/>
$\begin{aligned} & \mathrm{b}\left(\frac{4}{5}\right)=4 \Rightarrow \mathrm{~b}=5 \\ & \because \mathrm{c}^2=\mathrm{b}^2-\mathrm{a}^2 \\ & 16=25-\mathrm{a}^2 \Rightarrow \mathrm{a}=3 \\ & \text { L.R. }=\frac{2 \mathrm{a}^2}{\mathrm{~b}}=\frac{18}{5}\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $C$ be the circle of minimum area enclosing the ellipse $E: \frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ with eccentricity $\frac{1}{2}$ and foci $( \pm 2,0)$. Let PQR be a variable triangle, whose vertex $P$ is on the circle $C$ and the side $Q R$ of length 29 is parallel to the major axis of $E$ and contains the point of intersection of $E$ with the negative $y$-axis. Then the maximum area of the triangle PQR is :

**Options:**

- **(A)** $6(3+\sqrt{2})$
- **(B)** $8(3+\sqrt{2})$
- **(C)** $62+\sqrt{3}$
- **(D)** $82+\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $82+\sqrt{3}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/C2M4XJc2gYyjSXpuSQyRKiV4KlqTZuIXTJdiu8urVTQ.original.fullsize.png"/>
Area of $\triangle P Q R$
$\begin{aligned}
& =\frac{1}{2}(2 a)(a \sin \theta+b) \\
& \therefore \text { maximum area }=a(a+b) \\
& \quad=4(4+2 \sqrt{3})=8(2+\sqrt{3})
\end{aligned}$

</details>

---

### Q20. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A line passing through the point $\mathrm{P}(\sqrt{5}, \sqrt{5})$ intersects the ellipse $\frac{\mathrm{x}^2}{36}+\frac{\mathrm{y}^2}{25}=1$ at $A$ and $B$ such that $(P A) .(P B)$ is maximum. Then $5\left(P A^2+P B^2\right)$ is equal to :

**Options:**

- **(A)** $218$
- **(B)** $377$
- **(C)** $290$
- **(D)** $338$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $338$**

**Detailed Solution:**

Given ellipse is $\frac{x^2}{36}+\frac{y^2}{25}=1$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/gU9kvE9xeSebbeiqnjRbQDNKYCjaIpfkQeKd0TM5FeE.original.fullsize.png"/>
Any point on line $A B$ can be assumed as
$\mathrm{Q}(\sqrt{5}+\mathrm{r} \cos \theta, \sqrt{5}+\mathrm{r} \sin \theta)$
Putting this in equation of ellipse, we get
$25(\sqrt{5}+r \cos \theta)^2+36(\sqrt{5}+r \sin \theta)^2=900$
Simplifying, we get
$\begin{aligned}
& \mathrm{r}^2\left(25 \cos ^2 \theta+36 \sin ^2 \theta\right)+2 \sqrt{5} \mathrm{r}(25 \cos \theta+36 \sin \theta)-595=0 \\
& \quad|\mathrm{r}|=\mathrm{PA}, \mathrm{~PB}
\end{aligned}$
$\text { Thus, } \begin{aligned}
\text { PA } \cdot \mathrm{PB} & =\frac{595}{25 \cos ^2 \theta+36 \sin ^2 \theta}=\frac{595}{25+11 \sin ^2 \theta} \\
& =\text { maximum, if } \sin ^2 \theta=0
\end{aligned}$
This means line $A B$ must be parallel to $x$-axis
$\Rightarrow y_A=y_B=\sqrt{5}$
Putting $\mathrm{y}=\sqrt{5}$ in equation of ellipse, we get
$\frac{x^2}{36}+\frac{1}{5}=1 \Rightarrow x^2=36 \cdot \frac{4}{5}$
Hence,
$\mathrm{PA}^2+\mathrm{PB}^2=\left(\sqrt{5}-\frac{12}{\sqrt{5}}\right)^2+\left(\sqrt{5}+\frac{12}{\sqrt{5}}\right)^2$
$\begin{aligned} & =2\left(5+\frac{144}{5}\right)=\frac{338}{5} \\ & 5\left(\mathrm{PA}^2+\mathrm{PB}^2\right)=338\end{aligned}$

</details>

---

### Q21. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the length of the minor axis of an ellipse is equal to one fourth of the distance between the foci, then the eccentricity of the ellipse is :

**Options:**

- **(A)** $\frac{4}{\sqrt{17}}$
- **(B)** $\frac{\sqrt{3}}{16}$
- **(C)** $\frac{3}{\sqrt{19}}$
- **(D)** $\frac{\sqrt{5}}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{4}{\sqrt{17}}$**

**Detailed Solution:**

$\begin{aligned} & 2 \mathrm{~b}=\frac{1}{4}(2 \mathrm{ae}) \\ & \frac{\mathrm{b}}{\mathrm{a}}=\frac{\mathrm{e}}{4} \\ & \mathrm{e}=\sqrt{1-\frac{\mathrm{b}^2}{\mathrm{a}^2}} \\ & \mathrm{e}=\sqrt{1-\frac{\mathrm{e}^2}{16}} \\ & \mathrm{e}^2\left(1+\frac{1}{16}\right)=1 \\ & \mathrm{e}=\frac{4}{\sqrt{17}}\end{aligned}$

</details>

---

### Q22. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $S$ and $S^{\prime}$ are the foci of the ellipse $\frac{x^2}{18}+\frac{y^2}{9}=1$ and P be a point on the ellipse, then $\min \left(S P . S^{\prime} \mathrm{P}\right)+$ $\max \left(\mathrm{SP} . \mathrm{S}^{\prime} \mathrm{P}\right)$ is equal to :

**Options:**

- **(A)** $3(1+\sqrt{2})$
- **(B)** $3(6+\sqrt{2})$
- **(C)** 9
- **(D)** 27

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 27**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/arVV8CsGE00VCoQFpWgpvUDx4VmVC52rO18h1aCVr3E.original.fullsize.png"/>
$\mathrm{PS}+\mathrm{PS}^{\prime}=2 \times 3 \sqrt{2}$
$\mathrm{b}^2=\mathrm{a}^2\left(1-\mathrm{e}^2\right) \Rightarrow 9=18\left(1-\mathrm{e}^2\right)$
$\Rightarrow \mathrm{e}=\frac{1}{\sqrt{2}}$
Directrix $\mathrm{x}=\frac{\mathrm{a}}{\mathrm{e}}=\frac{3 \sqrt{2}}{\frac{1}{\sqrt{2}}}=6$
$P S \cdot P S '=\left|\frac{1}{\sqrt{2}}(3 \sqrt{2} \cos \theta-6) \frac{1}{\sqrt{2}}(3 \sqrt{2} \cos \theta+6)\right|$
$=\frac{1}{2}\left|18 \cos ^2 \theta-36\right|$
$\left(\mathrm{PS} \cdot \mathrm{PS}^{\prime}\right)_{\max }=18 ;(\mathrm{PS} \cdot \mathrm{PS})_{\min }=9$
sum $=27$

</details>

---

### Q23. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let the ellipse \(\mathrm{E}_1: \frac{x^2}{\mathrm{a}^2}+\frac{y^2}{\mathrm{~b}^2}=1, \mathrm{a}\gt\mathrm{b}\) and \(\mathrm{E}_2: \frac{x^2}{\mathrm{~A}^2}+\frac{y^2}{\mathrm{~B}^2}=1, \mathrm{~A} \lt \mathrm{B}\) have same eccentricity \(\frac{1}{\sqrt{3}}\). Let the product of their lengths of latus rectums be \(\frac{32}{\sqrt{3}}\), and the distance between the foci of \(E_1\) be 4. If \(E_1\) and \(E_2\) meet at \(A, B, C\) and \(D\), then the area of the quadrilateral \(A B C D\) equals :

**Options:**

- **(A)** \(\frac{12 \sqrt{6}}{5}\)
- **(B)** \(6 \sqrt{6}\)
- **(C)** \(\frac{18 \sqrt{6}}{5}\)
- **(D)** \(\frac{24 \sqrt{6}}{5}\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) \(\frac{24 \sqrt{6}}{5}\)**

**Detailed Solution:**

$\begin{aligned} & 2 a e=4 \\ & \Rightarrow \quad a=2 \sqrt{3} \\ & \Rightarrow \quad 1-\frac{b^2}{12}=\frac{1}{3} \Rightarrow b^2=8 \\ & \\ & \frac{2 b^2}{a} \times \frac{2 A^2}{B}=\frac{32}{\sqrt{3}} \\ & \Rightarrow \\ & \frac{2 \times 8}{2 \sqrt{3}} \times \frac{2 A^2}{B}=\frac{32}{\sqrt{3}} \\ & \Rightarrow \\ & \frac{A^2}{B}=2 \Rightarrow A^2=2 B \\ & \\ & \quad 1-\frac{A^2}{B}=\frac{1}{3} \\ & \Rightarrow \\ & B=3 \Rightarrow A^2=6\end{aligned}$
$E_1: \frac{x^2}{12}+\frac{y^2}{8}=1$ ....(i)
$E_1: \frac{x^2}{6}+\frac{y^2}{9}=1$...(ii)
On solving (i) \& (ii)
$\begin{aligned} &(x, y)=\left(\frac{\sqrt{6}}{\sqrt{5}}, \frac{6}{\sqrt{5}}\right),\left(\frac{-\sqrt{6}}{\sqrt{5}}, \frac{6}{\sqrt{5}}\right),\left(\frac{\sqrt{6}}{\sqrt{5}}, \frac{-6}{\sqrt{5}}\right), \\ &\left(\frac{-\sqrt{6}}{\sqrt{5}}, \frac{-6}{\sqrt{5}}\right)\end{aligned}$
Four points are vertices of rectangle area $=\frac{24 \sqrt{6}}{5}$

</details>

---

### Q24. JEE Main 2025 (28 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $\mathrm{E}_1: \frac{x^2}{9}+\frac{y^2}{4}=1$ be an ellipse. Ellipses $\mathrm{E}_1$ 's are constructed such that their centres and eccentricities are same as that of $E_1$, and the length of minor axis of $E_i$ is the length of major axis of $E_{i+1}(i \geq 1)$. If $A_i$ is the area of the ellipse $E_i$, then $\frac{5}{\pi}\left(\sum_{i=1}^{\infty} A_i\right)$, is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **54**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/U9639J4di3gKkWuVLy0MoUeIC03GiP25tcLF4_szhi4.original.fullsize.png">




$\begin{aligned} & \mathrm{E}_1=\frac{\mathrm{x}^2}{9}+\frac{\mathrm{y}^2}{4} \Rightarrow \mathrm{e}=\sqrt{1-\frac{4}{9}}=\frac{\sqrt{5}}{3} \\ & \mathrm{E}_2: \frac{\mathrm{x}^2}{\mathrm{a}^2}+\frac{\mathrm{y}^2}{4}=1 \\ & \mathrm{e}=\frac{\sqrt{5}}{3}=\sqrt{1-\frac{\mathrm{a}^2}{4}} \Rightarrow \frac{5}{9}=1-\frac{\mathrm{a}^2}{4} \\ & \mathrm{a}^2=\frac{16}{9}\end{aligned}$


$\begin{aligned} & \mathrm{E}_2: \frac{\mathrm{x}^2}{\frac{16}{9}}+\frac{\mathrm{y}^2}{4}=1 \\ & \mathrm{E}_3: \frac{\mathrm{x}^2}{\frac{16}{9}}+\frac{\mathrm{y}^2}{\mathrm{~b}^2}=1 \\ & \mathrm{e}=\frac{\sqrt{5}}{3}=\sqrt{1-\frac{\mathrm{b}^2}{\frac{16}{9}}} \Rightarrow b^2=\frac{64}{81}\end{aligned}$


$\begin{aligned} & \mathrm{E}_3=\frac{\mathrm{x}^2}{\frac{16}{9}}+\frac{\mathrm{y}^2}{\frac{64}{81}}=1 \\ & \mathrm{~A}_1=\pi \times 3 \times 2 \Rightarrow 6 \pi \\ & \mathrm{~A}_2=\pi \times \frac{4}{3} \times 2=\frac{8 \pi}{3} \\ & \mathrm{~A}_3=\pi \times \frac{4}{3} \times \frac{8}{9}=\frac{32 \pi}{81} \\ & \sum_{\mathrm{i}=1}^{\infty} \mathrm{A}_{\mathrm{i}}=6 \pi+\frac{8 \pi}{3}+\frac{32 \pi}{81}+\ldots . \infty \Rightarrow \frac{6 \pi}{1-\frac{4}{9}} \Rightarrow \frac{54 \pi}{5} \\ & \therefore \frac{5}{\pi} \sum_{\mathrm{i}=1}^{\infty} \mathrm{A}_{\mathrm{i}} \Rightarrow \frac{5}{\pi} \times \frac{54 \pi}{5}=54\end{aligned}$

</details>

---

### Q25. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let the product of the focal distances of the point $\left(\sqrt{3}, \frac{1}{2}\right)$ on the ellipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1,(\mathrm{a}\gt\mathrm{b})$, be $\frac{7}{4}$. Then the absolute difference of the eccentricities of two such ellipses is

**Options:**

- **(A)** $\frac{1-\sqrt{3}}{\sqrt{2}}$
- **(B)** $\frac{3-2 \sqrt{2}}{2 \sqrt{3}}$
- **(C)** $\frac{3-2 \sqrt{2}}{3 \sqrt{2}}$
- **(D)** $\frac{1-2 \sqrt{2}}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3-2 \sqrt{2}}{2 \sqrt{3}}$**

**Detailed Solution:**

$\begin{aligned} & \text { Product of focal distances }=\left(a+e x_1\right)\left(a-e x_1\right) \\ & =a^2-e^2 x_1^2=a^2-e^2(3) \\ & =a^2-3 e^2=\frac{7}{4} \Rightarrow a^2=\frac{7}{4}+3 e^2 \\ & \Rightarrow 4 a^2=7+12 e^2 \\ & \&\left(\sqrt{3}, \frac{1}{2}\right) \text { lines on } \frac{x^2}{a^2}+\frac{y^2}{b^2}=1 \\ & \therefore \frac{3}{a^2}+\frac{1}{4 b^2}=1\end{aligned}$
$\begin{aligned} & \frac{3}{\mathrm{a}^2}+\frac{1}{4\left(\mathrm{a}^2\right)\left(1-\mathrm{e}^2\right)}=1 \\ & 12\left(1-\mathrm{e}^2\right)+1=4 \mathrm{a}^2\left(1-\mathrm{e}^2\right) \\ & 13-12 \mathrm{e}^2=\left(7+12 \mathrm{e}^2\right)\left(1-\mathrm{e}^2\right) \\ & \Rightarrow 13-12 \mathrm{e}^2=7-7 \mathrm{e}^2+12 \mathrm{e}^2-12 \mathrm{e}^4 \\ & \Rightarrow 12 \mathrm{e}^4-17 \mathrm{e}^2+6=0 \\ & \therefore \mathrm{e}^2=\frac{17 \pm \sqrt{289-288}}{24}=\frac{17 \pm 1}{24}=\frac{3}{4} \& \frac{2}{3} \\ & \therefore \mathrm{e}=\frac{\sqrt{3}}{2} \& \sqrt{\frac{2}{3}} \\ & \therefore \text { difference }==\frac{\sqrt{3}}{2}-\sqrt{\frac{2}{3}}=\frac{3-2 \sqrt{2}}{2 \sqrt{3}}\end{aligned}$

</details>

---

### Q26. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=x^2+9, g(x)=\frac{x}{x-9}$ and $\mathrm{a}=f \circ g(10), \mathrm{b}=g \circ f(3)$. If $\mathrm{e}$ and $l$ denote the eccentricity and the length of the latus rectum of the ellipse $\frac{x^2}{a}+\frac{y^2}{b}=1$, then $8 \mathrm{e}^2+l^2$ is equal to.

**Options:**

- **(A)** 8
- **(B)** 16
- **(C)** 6
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 8**

**Detailed Solution:**

$\begin{aligned} & f(x)=x^2+9 \quad g(x)=\frac{x}{x-9} \\ & a=f(g(10))=f\left(\frac{10}{10-9}\right) \\ & =f(10)=109 \\ & b=g(f(3))=g(9+9) \\ & =g(18)=\frac{18}{9}=2 \\ & E: \frac{x^2}{109}+\frac{y^2}{2}=1\end{aligned}$
$\begin{aligned} & \mathrm{e}^2=1-\frac{2}{109}=\frac{107}{109} \\ & \ell=\frac{2(2)}{\sqrt{109}}=\frac{4}{\sqrt{109}} \\ & 8 \mathrm{e}^2+\ell^2=\frac{8(107)}{109}+\frac{16}{109} \\ & =8\end{aligned}$

</details>

---

### Q27. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let the line $2 x+3 y-\mathrm{k}=0, \mathrm{k}>0$, intersect the $x$-axis and $y$-axis at the points $\mathrm{A}$ and $\mathrm{B}$, respectively. If the equation of the circle having the line segment $\mathrm{AB}$ as a diameter is $x^2+y^2-3 x-2 y=0$ and the length of the latus rectum of the ellipse $x^2+9 y^2=k^2$ is $\frac{m}{n}$, where $m$ and $n$ are coprime, then $2 \mathrm{~m}+\mathrm{n}$ is equal to

**Options:**

- **(A)** 11
- **(B)** 10
- **(C)** 12
- **(D)** 13

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 11**

**Detailed Solution:**

Centre of the circle $=\left(\frac{3}{2}, 1\right)$
Equation of diameter $=2 \mathrm{x}+3 \mathrm{y}-\mathrm{k}=0$
$\begin{aligned}
& 2\left(\frac{3}{2}\right)+3(1)-\mathrm{k}=0 \\
& \Rightarrow \mathrm{k}=6
\end{aligned}$
Now, Equation of ellipse becomes
$\begin{aligned}
& x^2+9 y^2=36 \\
& \frac{x^2}{6^2}+\frac{y^2}{2^2}=1
\end{aligned}$
$\begin{aligned} & \text { length of } L R=\frac{2 b^2}{a}=\frac{2.2^2}{6}=\frac{8}{6}=\frac{4}{3}=\frac{m}{n} \\ & \therefore 2 m+n=2(4)+3=11\end{aligned}$

</details>

---

### Q28. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be a point on the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>9</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>=</mo><mn>1</mn></math>. Let the line passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo></math>axis meet the circle <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn></math> at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo> </mo><mtext>and</mtext><mo> </mo><mi>Q</mi></math> are on the same side of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis. Then, the eccentricity of the locus of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>R</mi><mo>:</mo><mi>R</mi><mi>Q</mi><mo>=</mo><mn>4</mn><mo>:</mo><mn>3</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> moves on the ellipse, is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>19</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><mn>21</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>139</mn></msqrt><mn>23</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>13</mn></msqrt><mn>7</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>13</mn></msqrt><mn>7</mn></mfrac></math>**

**Detailed Solution:**

<p>Given equation of ellipse and circle are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>9</mn></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><msup><mi>y</mi><mn>2</mn></msup></mstyle><mn>4</mn></mfrac><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>≡</mo><mfenced><mrow><mn>3</mn><mi>cos</mi><mi>θ</mi><mo>,</mo><mo> </mo><mn>2</mn><mi>sin</mi><mi>θ</mi></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mi>Q</mi><mo>≡</mo><mfenced><mrow><mn>3</mn><mi>cos</mi><mi>θ</mi><mo>,</mo><mo> </mo><mn>3</mn><mi>sin</mi><mi>θ</mi></mrow></mfenced></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>≡</mo><mfenced><mrow><mi>h</mi><mo>,</mo><mi>k</mi></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7a88b321-8d4a-4e77-bce7-43bb0cc67b2d.png" style="width: 400px; height: 182px;"/></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d4cc2947-1847-422e-894e-e3afb10b0377.png" style="width: 300px; height: 86px;"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>h</mi><mo>=</mo><mn>3</mn><mi>cos</mi><mi>θ</mi><mo>,</mo><mo> </mo><mi>k</mi><mo>=</mo><mfrac><mn>18</mn><mn>7</mn></mfrac><mi>sin</mi><mi>θ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>h</mi><mn>3</mn></mfrac><mo>=</mo><mi>cos</mi><mi>θ</mi><mo>,</mo><mo> </mo><mfrac><mrow><mn>7</mn><mi>k</mi></mrow><mn>18</mn></mfrac><mo>=</mo><mi>sin</mi><mi>θ</mi></math></p><p>So, locus of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>9</mn></mfrac><mo>+</mo><mfrac><mrow><mn>49</mn><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>324</mn></mfrac><mo>=</mo><mn>1</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>e</mi><mo>=</mo><msqrt><mn>1</mn><mo>−</mo><mfrac><mn>324</mn><mrow><mn>49</mn><mo>×</mo><mn>9</mn></mrow></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>e</mi><mo>=</mo><mfrac><msqrt><mn>117</mn></msqrt><mn>21</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>e</mi><mo>=</mo><mfrac><msqrt><mn>13</mn></msqrt><mn>7</mn></mfrac></math></p>

</details>

---

### Q29. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be a parabola with vertex  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo> </mo><mn>3</mn></mrow></mfenced></math> and directrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>6</mn></math>. Let an ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>:</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>a</mi><mo>&gt;</mo><mi>b</mi></math> of eccentricity <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math> pass through the focus of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>. Then the square of the length of the latus rectum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>385</mn><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>347</mn><mn>8</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>512</mn><mn>25</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>656</mn><mn>25</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>656</mn><mn>25</mn></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/78d1b8d4-f21e-4ac8-a4e6-54eb07267a04.png" style="width: 300px; height: 184px;"/></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi></math> be the foot of perpendicular from vertex to directrix of parabola,</p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mfenced><mrow><mn>4</mn><mo>+</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mn>6</mn></mrow><mrow><mn>4</mn><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac><mo>,</mo><mo> </mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mfrac><mn>12</mn><mn>5</mn></mfrac><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mfrac><mn>16</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Z</mi><mo>≡</mo><mfenced><mrow><mfrac><mn>12</mn><mn>5</mn></mfrac><mo>,</mo><mfrac><mn>16</mn><mn>5</mn></mfrac></mrow></mfenced></math></p><p>Eccentricity of ellipse is given as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math>.</p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup></math> using eccentricity formula we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mfrac><msup><mi>a</mi><mn>2</mn></msup><mn>2</mn></mfrac></math></p><p>So, equation of ellipse will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>144</mn><mrow><mn>25</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>256</mn><mrow><mn>25</mn><mo>×</mo><mstyle displaystyle="true"><mfrac><msup><mi>a</mi><mn>2</mn></msup><mn>2</mn></mfrac></mstyle></mrow></mfrac><mo>=</mo><mn>1</mn></math> {as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>≡</mo><mfenced><mrow><mfrac><mn>12</mn><mn>5</mn></mfrac><mo>,</mo><mfrac><mn>16</mn><mn>5</mn></mfrac></mrow></mfenced></math> }</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>144</mn><mrow><mn>25</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>512</mn><mrow><mn>25</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>656</mn><mrow><mn>25</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>656</mn><mn>25</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>328</mn><mn>25</mn></mfrac></math></p><p>Length of latus rectum is given by,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>L</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mo>×</mo><mstyle displaystyle="true"><mfrac><mn>328</mn><mn>25</mn></mfrac></mstyle></mrow><mstyle displaystyle="true"><mfrac><msqrt><mn>656</mn></msqrt><mn>5</mn></mfrac></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>L</mi><mo>=</mo><mfrac><msqrt><mn>656</mn></msqrt><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>L</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>656</mn><mn>25</mn></mfrac></math></p>

</details>

---

### Q30. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mi>α</mi><mo>,</mo><mn>0</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>(</mo><mn>0</mn><mo>,</mo><mi>β</mi><mo>)</mo></math> be the points on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>x</mi><mo>+</mo><mn>7</mn><mi>y</mi><mo>=</mo><mn>50</mn></math>. Let the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> divide the line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> internally in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>:</mo><mo> </mo><mn>3</mn></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mn>25</mn><mo>=</mo><mn>0</mn></math> be a directrix of the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>:</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math> and the corresponding focus be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>. If from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>, the perpendicular on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>, then the length of the latus rectum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>32</mn><mn>9</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>9</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>32</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>32</mn><mn>5</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mi>α</mi><mo>,</mo><mn>0</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>(</mo><mn>0</mn><mo>,</mo><mi>β</mi><mo>)</mo></math> lies on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>x</mi><mo>+</mo><mn>7</mn><mi>y</mi><mo>=</mo><mn>50</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>5</mn><mfenced><mi>α</mi></mfenced><mo>+</mo><mn>7</mn><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>50</mn><mo>,</mo><mo> </mo><mn>5</mn><mfenced><mn>0</mn></mfenced><mo>+</mo><mn>7</mn><mfenced><mi>β</mi></mfenced><mo>=</mo><mn>50</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>10</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mfrac><mn>50</mn><mn>7</mn></mfrac></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> divide the line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> internally in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>:</mo><mo> </mo><mn>3</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>≡</mo><mfenced><mrow><mfrac><mrow><mn>7</mn><mo>×</mo><mn>0</mn><mo>+</mo><mn>3</mn><mo>×</mo><mn>10</mn></mrow><mrow><mn>7</mn><mo>+</mo><mn>3</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mo>×</mo><mstyle displaystyle="true"><mfrac><mn>50</mn><mn>7</mn></mfrac></mstyle><mo>+</mo><mn>3</mn><mo>×</mo><mn>0</mn></mrow><mrow><mn>7</mn><mo>+</mo><mn>3</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>≡</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mi>e</mi><mo>=</mo><mn>3</mn></math> as perpendicular from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mn>25</mn><mo>=</mo><mn>0</mn></math> is a directrix of the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>:</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mfrac><mn>25</mn><mn>3</mn></mfrac></math></p><p>We know that, directrix of an ellipse is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>±</mo><mfrac><mi>a</mi><mi>e</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>a</mi><mi>e</mi></mfrac><mo>=</mo><mfrac><mn>25</mn><mn>3</mn></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5a249eda-1de0-4ae4-8ba4-967388bdee9b.png" style="width: 200px; height: 147px;"/></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>e</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo> </mo><mi>b</mi><mo>=</mo><mn>4</mn></math></p><p>Length of LR <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac><mo>=</mo><mfrac><mn>32</mn><mn>5</mn></mfrac></math></p></blockquote>

</details>

---

### Q31. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the length of the minor axis of ellipse is equal to half of the distance between the foci, then the eccentricity of the ellipse is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>5</mn></msqrt><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>5</mn></msqrt></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>5</mn></msqrt></mfrac></math>**

**Detailed Solution:**

<p>The length of minor axis is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>b</mi></mrow></mfenced></math> and the distance between foci is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>a</mi><mi>e</mi></mrow></mfenced></math></p><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>b</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>×</mo><mn>2</mn><mi>a</mi><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>b</mi><mo>=</mo><mi>a</mi><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><msup><mi>e</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>4</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>=</mo><msup><mi>e</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mo>-</mo><mn>4</mn><msup><mi>e</mi><mn>2</mn></msup><mo>=</mo><msup><mi>e</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>e</mi><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>5</mn></msqrt></mfrac></math></p>

</details>

---

### Q32. JEE Main 2024 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

If the points of intersection of two distinct conics <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>16</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math> lie on the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>3</mn></msqrt></math> times the area of the rectangle formed by the intersection points is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **432**

**Detailed Solution:**

<p>Given conics are <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>b</mi><mo> </mo><mtext>and</mtext><mo> </mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>16</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math>.</p><p>The intersection point of these conics lie on <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></math>.</p><p>So, putting <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></math> in both the conics.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>b</mi><mo>,</mo><mo> </mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>16</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>b</mi><mo>,</mo><mo> </mo><mfrac><mi>b</mi><mn>16</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>b</mi></mrow><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>b</mi><mn>16</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mi>b</mi></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>48</mn><mo>=</mo><mn>16</mn><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>16</mn><mi>b</mi><mo>+</mo><mn>48</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>b</mi><mo>-</mo><mn>4</mn><mi>b</mi><mo>+</mo><mn>48</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>b</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>-</mo><mn>12</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>b</mi><mo>=</mo><mo> </mo><mn>4</mn><mo>,</mo><mo> </mo><mn>12</mn></math> ( <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>4</mn></math>is rejected because curves coincide)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">b</mi><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mo>±</mo><msqrt><mn>12</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>12</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>48</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mo>±</mo><mn>6</mn></math></p><p>Hence points of intersection are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>±</mo><msqrt><mn>12</mn></msqrt><mo>,</mo><mo>±</mo><mn>6</mn><mo>)</mo></math>.</p><p>So, length and breadth of rectangle are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>12</mn></msqrt><mo> </mo><mtext>and</mtext><mo> </mo><mn>12</mn></math>. </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/12b8723e-aa3a-4ba1-96cb-94ab741d9dfa.png" style="width: 400px; height: 235px;"/></p><p>So, the area of rectangle is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>2</mn><msqrt><mn>12</mn></msqrt><mo>×</mo><mn>12</mn><mo>=</mo><mn>48</mn><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>A</mi><mo>=</mo><mn>48</mn><msqrt><mn>3</mn></msqrt><mo>×</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mi>A</mi><mo>=</mo><mn>432</mn></math></p>

</details>

---

### Q33. JEE Main 2023 (15 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let an ellipse with centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math> and latus rectum of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math> have its major axis along x-axis. If its minor axis subtends an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>60</mn><mo>&#8728;</mo></msup></math> at the foci, then the square of the sum of the lengths of its minor and major axes is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<blockquote><p>Given,</p><p>An ellipse with centre <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math> and latus rectum of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math> have its major axis along x-axis </p><p>And its minor axis subtends an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>60</mn><mo>&#8728;</mo></msup></math> at the foci, </p><p>So, on plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/12178a13-1713-4adc-91fc-6e84b5897480.png" style="width: 340px; height: 256px;" /></p><p>Now from diagram we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mfrac><mi>a</mi><mn>4</mn></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>tan</mi><msup><mn>30</mn><mo>&#8728;</mo></msup><mo>=</mo><mfrac><mi>b</mi><mrow><mi>a</mi><mi>e</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mfrac><mi>b</mi><mrow><mi>a</mi><mi>e</mi></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><msup><mi>b</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mfrac><msup><mi>a</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn></math></p></blockquote>

</details>

---

### Q34. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><msqrt><mn>7</mn></msqrt></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>6</mn><msqrt><mn>7</mn></msqrt></mfrac></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>Q</mi><mo>,</mo><mo>&#160;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be four points on the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>36</mn></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mi>S</mi></math> be mutually perpendicular and pass through the origin. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mfenced><mrow><mi>P</mi><mi>Q</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><mstyle displaystyle="true"><msup><mfenced><mrow><mi>R</mi><mi>S</mi></mrow></mfenced><mn>2</mn></msup></mstyle></mfrac><mo>=</mo><mfrac><mi>p</mi><mi>q</mi></mfrac><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> are coprime, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>+</mo><mi>q</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>147</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>143</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>137</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>157</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>157</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><msqrt><mn>7</mn></msqrt></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>6</mn><msqrt><mn>7</mn></msqrt></mfrac></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>Q</mi><mo>,</mo><mo>&#160;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be four points on the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>9</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>P</mi><mo>=</mo><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><msqrt><msup><mfenced><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><msqrt><mn>7</mn></msqrt></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mn>6</mn><msqrt><mn>7</mn></msqrt></mfrac></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mfrac><mn>48</mn><mn>7</mn></mfrac></msqrt></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> is origin,</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>r</mi><mn>1</mn></msub><mi>cos</mi><mi>&#952;</mi><mo>,</mo><mo>&#160;</mo><msub><mi>r</mi><mn>1</mn></msub><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> lies on ellipse, so we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><msub><mi>r</mi><mn>1</mn></msub><mn>2</mn></msup><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><msup><msub><mi>r</mi><mn>1</mn></msub><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mstyle><mstyle displaystyle="true"><mn>9</mn></mstyle></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mn>9</mn></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>48</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><msub><mi>r</mi><mn>2</mn></msub><mi>sin</mi><mi>&#952;</mi><mo>,</mo><mo>&#160;</mo><msub><mi>r</mi><mn>2</mn></msub><mi>cos</mi><mi>&#952;</mi></mrow></mfenced></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>&#8201;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>R</mi><mi>S</mi></math> are perpendicular and pass through origin,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><msub><mi>r</mi><mn>2</mn></msub><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><msup><msub><mi>r</mi><mn>2</mn></msub><mn>2</mn></msup><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mn>9</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mn>9</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><msup><msub><mi>r</mi><mn>2</mn></msub><mn>2</mn></msup></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Now adding equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><msub><mi>r</mi><mn>2</mn></msub><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>-</mo><mfrac><mn>7</mn><mn>48</mn></mfrac><mo>=</mo><mfrac><mn>31</mn><mn>144</mn></mfrac></math></p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>P</mi><msup><mi>Q</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>R</mi><msup><mi>S</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><mrow><mi>O</mi><msup><mi>P</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>O</mi><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mi>P</mi><msup><mi>Q</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>R</mi><msup><mi>S</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><msup><msub><mi>r</mi><mn>1</mn></msub><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><msub><mi>r</mi><mn>2</mn></msub><mn>2</mn></msup></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mi>P</mi><msup><mi>Q</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>R</mi><msup><mi>S</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mfrac><mn>7</mn><mn>48</mn></mfrac><mo>+</mo><mfrac><mn>31</mn><mn>144</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>13</mn><mn>144</mn></mfrac><mo>=</mo><mfrac><mi>p</mi><mi>m</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>p</mi><mo>+</mo><mi>m</mi><mo>=</mo><mn>157</mn></math></p>

</details>

---

### Q35. JEE Main 2022 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

If the length of the latus rectum of the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>8</mn><mi>y</mi><mo>-</mo><mi>&#955;</mi><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is the length of its major axis, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>+</mo><mi>l</mi></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **75**

**Detailed Solution:**

<blockquote><p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>8</mn><mi>y</mi><mo>-</mo><mi>&#955;</mi><mo>=</mo><mn>0</mn></math> is a ellipse</p><p>Now on rearranging the terms we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mrow><mi>&#955;</mi><mo>+</mo><mn>5</mn></mrow></mfrac><mo>+</mo><mfrac><msup><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mfrac><mrow><mi>&#955;</mi><mo>+</mo><mn>5</mn></mrow><mn>4</mn></mfrac></mfrac><mo>=</mo><mn>1</mn></math></p><p>We know that length of latus rectum is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac><mo>=</mo><mn>4</mn></math> </p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>5</mn></mrow></mfenced></mrow><mrow><mn>4</mn><mfenced><mstyle displaystyle="true"><msqrt><mi>&#955;</mi><mo>+</mo><mn>5</mn></msqrt></mstyle></mfenced></mrow></mfrac><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>5</mn></mrow></mfenced></mrow><mn>4</mn></mfrac><mo>=</mo><mn>4</mn><mfenced><msqrt><mi>&#955;</mi><mo>+</mo><mn>5</mn></msqrt></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>8</mn><mfenced><msqrt><mi>&#955;</mi><mo>+</mo><mn>5</mn></msqrt></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>64</mn><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>25</mn><mo>+</mo><mn>10</mn><mi>&#955;</mi><mo>=</mo><mn>64</mn><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>54</mn><mi>&#955;</mi><mo>-</mo><mn>295</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>=</mo><mn>59</mn><mo>&#160;</mo><mtext>or&#160;</mtext><mo>-</mo><mn>5</mn></math></p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8800;</mo><mo>-</mo><mn>5</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>2</mn><mi>a</mi><mo>=</mo><mn>2</mn><msqrt><mi>&#955;</mi><mo>+</mo><mn>5</mn></msqrt><mo>=</mo><mn>2</mn><msqrt><mn>64</mn></msqrt><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>+</mo><mi>l</mi><mo>=</mo><mn>59</mn><mo>+</mo><mn>16</mn><mo>=</mo><mn>75</mn></math></p></blockquote>

</details>

---

### Q36. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math> meets the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>7</mn></mfrac><mo>+</mo><mfrac><mi>y</mi><mrow><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow></mfrac><mo>=</mo><mn>1</mn></math> on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis and the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>7</mn></mfrac><mo>-</mo><mfrac><mi>y</mi><mrow><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow></mfrac><mo>=</mo><mn>1</mn></math> on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis, then the eccentricity of the ellipse is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>7</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow><mn>7</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>7</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msqrt><mn>5</mn></msqrt></mrow><mn>7</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>7</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math> meets the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>7</mn></mfrac><mo>+</mo><mfrac><mi>y</mi><mrow><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow></mfrac><mo>=</mo><mn>1</mn></math> on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis, so at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn></math> putting in both equation and comparing we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>7</mn></math> </p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math> meets the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>7</mn></mfrac><mo>-</mo><mfrac><mi>y</mi><mrow><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow></mfrac><mo>=</mo><mn>1</mn></math> on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> so putting in both equation and comparing we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>24</mn><mn>49</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>e</mi><mo>=</mo><msqrt><mfrac><mn>25</mn><mn>49</mn></mfrac></msqrt><mo>=</mo><mfrac><mn>5</mn><mn>7</mn></mfrac></math></p></blockquote>

</details>

---

### Q37. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> be a focal chord of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>x</mi></math> such that it subtends an angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math> at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>. Let the line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> be also a focal chord of the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>:</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><msup><mi>a</mi><mn>2</mn></msup><mo>&#62;</mo><msup><mi>b</mi><mn>2</mn></msup></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math> is the eccentricity of the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>e</mi><mn>2</mn></msup></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>+</mo><mn>5</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> is focal chord of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi>x</mi></math></p><p>so let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mn>2</mn><mi>t</mi></mrow></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>2</mn><mi>t</mi></mfrac></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/776eae04-0033-4836-aebe-d3f047ae9fa8-image.png" style="width: 295px; height: 270px;" /></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mrow><mi>P</mi><mi>R</mi></mrow></msub><mo>&#183;</mo><msub><mi>m</mi><mrow><mi>P</mi><mi>Q</mi></mrow></msub><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>t</mi></mrow><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>2</mn><mi>t</mi></mfrac></mstyle></mrow><mrow><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>1</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> must be the latus rectum</p><p>We get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Q</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p>For ellipse</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>a</mi><mi>e</mi><mo>=</mo><mn>1</mn></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></math></p><p>and<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><msup><mi>e</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>e</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q38. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the eccentricity of an ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><mi>a</mi><mo>&#62;</mo><mi>b</mi></math>, be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>. If this ellipse passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>4</mn><msqrt><mfrac><mn>2</mn><mn>5</mn></mfrac></msqrt><mo>,</mo><mn>3</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>29</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>&#160;&#160;</mo><mi mathvariant="normal">a</mi><mo>&#62;</mo><mi mathvariant="normal">b</mi></math></p><p>Now using eccentricity formula, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>=</mo><mfrac><mn>15</mn><mn>16</mn></mfrac><mo>&#8658;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>15</mn><mn>16</mn></mfrac><msup><mi>a</mi><mn>2</mn></msup></math></p><p>Now again <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math> is passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>4</mn><msqrt><mfrac><mn>2</mn><mn>5</mn></mfrac></msqrt><mo>,</mo><mn>3</mn></mrow></mfenced></math> on satisfying the point we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>16</mn><mo>&#215;</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></mrow><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>9</mn><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>32</mn><mrow><mn>5</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>9</mn><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p>Now putting the value <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>15</mn><mn>16</mn></mfrac><msup><mi>a</mi><mn>2</mn></msup></math> in above equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>32</mn><mrow><mn>5</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>9</mn><mrow><mfrac><mn>15</mn><mn>16</mn></mfrac><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>80</mn><mrow><mn>5</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>15</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>15</mn><mo>+</mo><mn>16</mn><mo>=</mo><mn>31</mn></math></p>

</details>

---

### Q39. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let the maximum area of the triangle that can be inscribed in the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><mi>a</mi><mo>&#62;</mo><mn>2</mn></math>, having one of its vertices at one end of the major axis of the ellipse and one of its sides parallel to the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis, be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msqrt><mn>3</mn></msqrt></math>. Then the eccentricity of the ellipse is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Plotting the diagram as per given information we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c5451a3c-6ae9-4abf-92ce-aaa54d867be9-image.png" style="width: 250px; height: 187px;" /></p><p>Now finding area of the triangle we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>a</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mfenced><mrow><mn>4</mn><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">a</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos&#952;</mi></mrow></mfenced><mi>sin</mi><mi>&#952;</mi></math></p><p>Differentiating to get maxima and minima we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>dA</mi><mrow><mi mathvariant="normal">d</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi mathvariant="normal">a</mi><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">d</mi><mi>A</mi></mrow><mrow><mo>&#160;</mo><mi mathvariant="normal">d</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>1</mn><mo>+</mo><mi>cos</mi><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mn>1</mn><mfenced><mi>Reject</mi></mfenced></math></p><p>OR</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mo>&#160;</mo><mi mathvariant="normal">d</mi><msup><mi>&#952;</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>2</mn><mi mathvariant="normal">a</mi><mfenced><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mo>&#160;</mo><mi mathvariant="normal">d</mi><msup><mi>&#952;</mi><mn>2</mn></msup></mrow></mfrac><mo>&#60;</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">A</mi><mi>max</mi></msub><mo>=</mo><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mi mathvariant="normal">a</mi><mo>=</mo><mn>6</mn><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>4</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><msqrt><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><msup><mi>a</mi><mn>2</mn></msup></mfrac></msqrt><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p>

</details>

---

### Q40. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A ray of light through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> is reflected at a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo></math> axis and then passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>.</mo></math> If this reflected ray is the directrix of an ellipse with eccentricity <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math> and the distance of the nearer focus from this directrix is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><msqrt><mn>53</mn></msqrt></mfrac><mo>,</mo></math> then the equation of the other directrix can be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mi>x</mi><mo>+</mo><mn>7</mn><mi>y</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mi>x</mi><mo>+</mo><mn>7</mn><mi>y</mi><mo>-</mo><mn>15</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mi>x</mi><mo>-</mo><mn>7</mn><mi>y</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mi>x</mi><mo>+</mo><mn>7</mn><mi>y</mi><mo>+</mo><mn>15</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mi>y</mi><mo>+</mo><mn>29</mn><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mi>y</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mi>y</mi><mo>-</mo><mn>39</mn><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mi>y</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mi>y</mi><mo>+</mo><mn>29</mn><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mi>y</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>The reflected point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0187573e-6468-4151-bb74-e8f5ec5fdf83-image.png" style="width: 306px; height: 250px;" /></p><p>Equation of reflected ray</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow><mrow><mn>5</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mn>2</mn><mn>7</mn></mfrac><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mi>y</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mi>y</mi><mo>+</mo><mn>11</mn><mo>=</mo><mn>0</mn></math></p><p>Let the equation of other directrix is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mi>y</mi><mo>+</mo><mi>&#955;</mi><mo>=</mo><mn>0</mn></math></p><p>Distance of directrix from focus</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mi>e</mi></mfrac><mo>-</mo><mi>a</mi><mi>e</mi><mo>=</mo><mfrac><mn>8</mn><msqrt><mn>53</mn></msqrt></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math> is the eccentricity</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>a</mi><mo>-</mo><mfrac><mi>a</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>8</mn><msqrt><mn>53</mn></msqrt></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>3</mn><msqrt><mn>53</mn></msqrt></mfrac></math></p><p>Distance from other focus <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mi>e</mi></mfrac><mo>+</mo><mi>a</mi><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mi>a</mi><mo>+</mo><mfrac><mi>a</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>10</mn><mi>a</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><msqrt><mn>53</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>10</mn><msqrt><mn>53</mn></msqrt></mfrac></math></p><p>Distance between two directrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mi>a</mi></mrow><mi>e</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mfrac><mn>3</mn><msqrt><mn>53</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>18</mn><msqrt><mn>53</mn></msqrt></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mrow><mi>&#955;</mi><mo>-</mo><mn>11</mn></mrow><msqrt><mn>53</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mn>18</mn><msqrt><mn>53</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>-</mo><mn>11</mn><mo>=</mo><mn>18</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mi>y</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>7</mn><mi>y</mi><mo>+</mo><mn>29</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q41. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let an ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>:</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><msup><mi>a</mi><mn>2</mn></msup><mo>&#62;</mo><msup><mi>b</mi><mn>2</mn></msup></math>, passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msqrt><mfrac><mn>3</mn><mn>2</mn></mfrac></msqrt><mo>,</mo><mn>1</mn></mrow></mfenced></math> and has eccentricity <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math>. If a circle, centered at focus <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>(</mo><mi>&#945;</mi><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn></math>, of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></math>, intersects <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> at two points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><msup><mi>Q</mi><mn>2</mn></msup></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>The ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math> passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msqrt><mfrac><mn>3</mn><mn>2</mn></mfrac></msqrt><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>On solving equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>3</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>We know that, focii of the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#177;</mo><mi>a</mi><mi>e</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>e</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Its focus is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math></p><p>Now, equation of circle is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>&#177;</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>,</mo><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><msup><mi>Q</mi><mn>2</mn></msup><mo>=</mo><msqrt><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></mrow></mfenced><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mfrac><mn>4</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>16</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q42. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>:</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>&#62;</mo><mi>b</mi><mo>.</mo></math> Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> be another ellipse such that it touches the end points of major axis of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math> and the foci of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> are the end points of minor axis of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> have same eccentricities, then its value is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>8</mn></msqrt></mrow><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>6</mn></msqrt></mrow><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given ellipse is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>:</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>&#62;</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> is another ellipse which touches the end points of the major axis of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math> and foci of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> are at the minor axis of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>,</mo></math> thus the two ellipses are given by the following diagram.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f6b7d58e-5f54-4192-aa88-3c9e87da4e44-image.png" style="width: 327px; height: 298px;" /></p><p>Since, the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> touches the major axis of the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math>, hence, the minor axis of the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mi>a</mi><mo>.</mo></math></p><p>Now, let the major axis of the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mi>c</mi></math> and it is obvious from the diagram and the given conditions that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>&#62;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>.</mo></math></p><p>We know that the eccentricity of an ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>A</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>B</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>A</mi><mo>&#62;</mo><mi>B</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>-</mo><mfrac><msup><mi>B</mi><mn>2</mn></msup><msup><mi>A</mi><mn>2</mn></msup></mfrac></msqrt><mo>.</mo></math></p><p>Thus, for the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>,</mo></math> we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac></msqrt></math> and for the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub><mo>,</mo></math> we have <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>e</mi><mn>1</mn></msub><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><msup><mi>a</mi><mn>2</mn></msup><msup><mi>c</mi><mn>2</mn></msup></mfrac></msqrt><mo>.</mo></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><msub><mi>e</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>-</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac></msqrt><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><msup><mi>a</mi><mn>2</mn></msup><msup><mi>c</mi><mn>2</mn></msup></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>1</mn><mo>-</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><msup><mi>a</mi><mn>2</mn></msup><msup><mi>c</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><msup><mi>a</mi><mn>2</mn></msup><msup><mi>c</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><mfrac><msup><mi>a</mi><mn>4</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mfrac><msup><mi>a</mi><mn>2</mn></msup><mi>b</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Also, given that the foci of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> are the end points of the minor axis of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>,</mo></math> thus <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mi>c</mi><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mfrac><mi>b</mi><mi>e</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>From the above two equations, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>b</mi><mi>e</mi></mfrac><mo>=</mo><mfrac><msup><mi>a</mi><mn>2</mn></msup><mrow><mo>&#160;</mo><mi>b</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>e</mi><mo>=</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac></math></p><p>Now, using the definition of eccentricity, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><mi>e</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Now, applying the Sridharacharya&#39;s formula for the roots of a quadratic equation, i.e. if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>b</mi><mo>&#177;</mo><msqrt><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>a</mi><mi>c</mi></msqrt></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><msqrt><msup><mn>1</mn><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></msqrt></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>e</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>1</mn><mo>+</mo><mn>4</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>e</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p>But, eccentricity can never be negative, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q43. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>If the points of intersection of the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>16</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math> and the circle <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#62;</mo><mn>4</mn></math> lie on the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>b</mi></math></p><p>Solving both the equations we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>b</mi></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>16</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>16</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>b</mi><mn>16</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mi>b</mi></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>16</mn><mi>b</mi><mo>+</mo><mn>48</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>b</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>12</mn><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mo>&#8757;</mo><mi>b</mi><mo>&#62;</mo><mn>4</mn></mrow></mfenced></math></p>

</details>

---

### Q44. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math> intersects the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn></math> at two points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>, then the angle subtended by the line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> at the origin is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/eb7af0c0-3f76-4d97-be67-44869709a436-image.png" style="width: 364px; height: 250px;" /></p><p>Homogenising</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p>Lines are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mfrac><mi>x</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Angle between lines <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p>option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math></p>

</details>

---

### Q45. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the co-ordinates of two points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msqrt><mn>7</mn></msqrt><mo>,</mo><mn>0</mn><mo>)</mo></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><msqrt><mn>7</mn></msqrt><mo>,</mo><mn>0</mn><mo>)</mo></math> respectively and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is any point on the conic, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>144</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>A</mi><mo>+</mo><mi>P</mi><mi>B</mi></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<p>For ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>16</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>9</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p>Comparing with, standard equation of ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math>, we get  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>4</mn><mo>,</mo><mi>b</mi><mo>=</mo><mn>3</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>e</mi><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><mn>9</mn><mn>16</mn></mfrac></msqrt><mo>=</mo><mfrac><msqrt><mn>7</mn></msqrt><mn>4</mn></mfrac></math>
Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are foci</p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>A</mi><mo>+</mo><mi>P</mi><mi>B</mi><mo>=</mo><mn>2</mn><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>8</mn></math>.</p>

</details>

---

### Q46. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mfenced><mrow><mi>a</mi><mo>&#62;</mo><mi>b</mi></mrow></mfenced></math> be a given ellipse, length of whose latus rectum is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>. If its eccentricity is the maximum value of the function, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>+</mo><mi>t</mi><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>145</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>116</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>126</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>135</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>126</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mi>R</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac><mo>=</mo><mn>10</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;&#8201;</mtext><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>5</mn><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>&#8722;</mo><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8722;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8722;</mo><msup><mfenced><mrow><mi>t</mi><mo>&#8722;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#8722;</mo><msup><mfenced><mrow><mi>t</mi><mo>&#8722;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup></math></p><p>max <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msup><mi>e</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>a</mi><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mfrac><mn>4</mn><mn>9</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;</mtext><mn>5</mn><mo>=</mo><mfrac><mn>5</mn><mn>9</mn></mfrac><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#8201;&#8201;&#8201;</mtext><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mn>81</mn><mo>,</mo><mtext>&#8201;&#8201;</mtext><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>45</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>126</mn></math>.</p>

</details>

---

### Q47. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the distance between the foci of an ellipse is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> and the distance between its directrix is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>,</mo></math> then the length of its latus rectum is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2cdf790a-7c91-4a7f-8280-3bbd38bd505d-image.png" style="width: 300px; height: 221px;" />Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mi>e</mi><mo>=</mo><mn>6</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>a</mi></mrow><mi>e</mi></mfrac><mo>=</mo><mn>12</mn></math>, directrices are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>&#177;</mo><mfrac><mi>a</mi><mi>e</mi></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mi>e</mi></mfrac><mo>=</mo><mn>6</mn></math>

Now, using the formula for eccentricity of an ellipse</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>a</mi><mn>2</mn></msup><msup><mi>e</mi><mn>2</mn></msup><mo>=</mo><mn>18</mn><mo>-</mo><mn>9</mn><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>.</mo><mi>R</mi><mo>.</mo><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>9</mn></mrow><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q48. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An ellipse, with foci at <math><mfenced separators="|"><mrow><mn>0,2</mn></mrow></mfenced></math> and <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mi>&#160;</mi></math> and minor axis of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> , passes through which of the following points?

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi> </mi><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>,</mo><mi> </mi><mn>2</mn></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mi> </mi><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>,</mo><mi> </mi><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

Given that be <math><mo>=</mo><mn>2</mn></math> and <math><mi>a</mi><mo>=</mo><mn>2</mn></math>  
(here <math><mi>a</mi><mo>&lt;</mo><mi>b</mi></math> ) 
<math><mo>∵</mo><mtext> </mtext><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>  
<math><mo>∴</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>8</mn></math>  
<math><mo>∴</mo></math> Equation of ellipse <math><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>8</mn></mrow></mfrac><mo>=</mo><mn>1</mn></math>  
Clearly <math><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>,</mo><mi> </mi><mn>2</mn></mrow></mfenced></math> lies on the ellipse.

</details>

---

### Q49. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In an ellipse, with centre at the origin, if the difference of the lengths of major axis and minor axis is 10 and one of the foci is at <math><mfenced separators="|"><mrow><mn>0,5</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>,</mo></math> then the length of its latus rectum is:

**Options:**

- **(A)** <math><mn>6</mn></math>
- **(B)** <math><mn>10</mn></math>
- **(C)** <math><mn>8</mn></math>
- **(D)** <math><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>5</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7132e35b-1a2f-4178-9402-e85c68e9d11f-image3.jpeg" />
Given, difference of the lengths of major and minor axis is <math><mn>10</mn></math>.
<math><mo>&#8658;</mo><mn>2</mn><mi>b</mi><mo>-</mo><mn>2</mn><mi>a</mi><mo>=</mo><mn>10</mn></math> &hellip; (1)
One of the focii is <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>
<math><mo>&#8658;</mo><mi>b</mi><mi>e</mi><mo>=</mo><mn>5</mn><msqrt><mn>3</mn></msqrt></math> &hellip; (2)
Also <math><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math> .......(3)
<math><mo>&#8658;</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>75</mn></math>
<math><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>75</mn></math>
<math><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>15</mn></math> &hellip; (4)
From (1) and (4)
<math><mi>a</mi><mo>=</mo><mn>5</mn></math> and <math><mi>b</mi><mo>=</mo><mn>10</mn></math>
Hence length of the latus rectum <math><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>b</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mo>&#8901;</mo><mfrac><mrow><mn>25</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>=</mo><mn>5</mn></math>

</details>

---

### Q50. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>S</mi><mo>'</mo></msup></math> be the foci of an ellipse and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be any one of the extremities of its minor axis. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><msup><mi>S</mi><mo>'</mo></msup><mi>B</mi><mi>S</mi></math> is a right angled triangle with right angle at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and area <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>&#916;</mi><msup><mi>S</mi><mo>'</mo></msup><mi>B</mi><mi>S</mi></mrow></mfenced><mo>=</mo><mn>8</mn><mo>&#160;</mo><mi>sq</mi><mo>.</mo><mi>units</mi></math>, then the length of a latus rectum of the ellipse is :

**Options:**

- **(A)** <math><mn>2</mn><mi> </mi><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math><mn>2</mn></math>
- **(C)** <math><mn>4</mn></math>
- **(D)** <math><mn>4</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>4</mn></math>**

**Detailed Solution:**

<p>Given that, </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9cf6e5d8-a3e8-4241-9967-4415b2e0bb4a-image.png" style="width: 250px; height: 240px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#8736;</mi><mi>S</mi><mi>B</mi><msup><mi>S</mi><mo>'</mo></msup><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p><math><mo>&#8658;</mo><mi>&#8736;</mi><mi>O</mi><mi>B</mi><mi>S</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mi>a</mi><mi>e</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math> </p><p>Also, area <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8710;</mo><mi>S</mi><mi>B</mi><msup><mi>S</mi><mo>'</mo></msup></mrow></mfenced><mo>=</mo><mn>8</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo><mn>2</mn><mi>a</mi><mi>e</mi><mo>.</mo><mi>b</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mi>e</mi><mi>b</mi><mo>=</mo><mn>8</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> </p><p>From equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><msup><mi>e</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mo>+</mo><mn>8</mn><mo>=</mo><mn>16</mn></math></p><p><math><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math> and <math><mi>a</mi><mo>=</mo><mn>4</mn></math></p><p>Thus, the length of the latus rectum is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac><mo>=</mo><mfrac><mn>16</mn><mn>4</mn></mfrac><mo>=</mo><mn>4</mn></math> </p>

</details>

---

### Q51. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the length of the latus rectum of an ellipse with its major axis along $x$ -axis and centre at the origin, be 8 . If the distance between the foci of this ellipse is equal to the length of its minor axis, then which one of the following points lies on it?

**Options:**

- **(A)** $(4 \sqrt{2}, 2 \sqrt{2})$
- **(B)** $(4 \sqrt{3}, 2 \sqrt{2})$
- **(C)** $(4 \sqrt{3}, 2 \sqrt{3})$
- **(D)** $(4 \sqrt{2}, 2 \sqrt{3})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(4 \sqrt{3}, 2 \sqrt{2})$**

**Detailed Solution:**

Let the ellipse be $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$

Then, $\frac{2 b^{2}}{a}=8,2 a e-b^{2}$ and $b^{2}=a^{3}\left(1-e^{2}\right)$

$\Rightarrow a=8, b^{2}=32$

Then, the equation of the ellipse

$\frac{x^{2}}{64}+\frac{y^{2}}{32}=1$

Hence, the point $(4 \sqrt{3}, 2 \sqrt{2})$ lies on the ellipse.

</details>

---

### Q52. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><msup><mi>R</mi><mn>2</mn></msup><mo>:</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>+</mo><mi>r</mi></mrow></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>-</mo><mi>r</mi></mrow></mfrac><mo>=</mo><mn>1</mn></mrow></mfenced><mo>,</mo></math> where <math><mi>r</mi><mo>&#8800;</mo><mo>&#177;</mo><mn>1</mn><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> represents:

**Options:**

- **(A)** An ellipse whose eccentricity is <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mi>r</mi><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac><mo>,</mo></math> when <math><mi>r</mi><mo>&#62;</mo><mn>1</mn><mo>.</mo></math>
- **(B)** A hyperbola whose eccentricity is <math><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mi>r</mi><mo>+</mo><mn>1</mn></msqrt></mrow></mfrac><mo>,</mo></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>r</mi><mo>&#60;</mo><mn>1</mn><mo>.</mo></math>
- **(C)** An ellipse whose eccentricity is  <math><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt><mo>,</mo></math>  when  <math><mi>r</mi><mo>&gt;</mo><mn>1</mn></math>
- **(D)** A hyperbola whose eccentricity is  <math><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><mi>r</mi></msqrt></mrow></mfrac><mo>,</mo></math>  when  <math><mn>0</mn><mo>&lt;</mo><mi>r</mi><mo>&lt;</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) An ellipse whose eccentricity is  <math><msqrt><mfrac><mrow><mn>2</mn></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt><mo>,</mo></math>  when  <math><mi>r</mi><mo>&gt;</mo><mn>1</mn></math>**

**Detailed Solution:**

Given <math><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><mi>r</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>r</mi></mrow></mfrac><mo>=</mo><mn>1</mn></math>

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> then this curve is a hyperbola whose eccentricity is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>r</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>r</mi></mrow></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mn>2</mn><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt></math>. 

If <math><mi>r</mi><mo>&#62;</mo><mn>1</mn></math> , then this curve is an ellipse whose
eccentricity is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mn>2</mn><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt></math>.

</details>

---

### Q53. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If the length of the latus rectum of an ellipse is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> units and the distance between a focus and its nearest vertex on the major axis is <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> units, then its eccentricity is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given length of latus-rectum of an ellipse is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac><mo>=</mo><mn>4</mn><mo>&#8658;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>a</mi></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>a</mi><mi>e</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mi>a</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>.</p><p>Now we know, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mi>a</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow></mfenced><mi>a</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>e</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mi>a</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>e</mi></mrow></mfenced></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>a</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>e</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>.</p>

</details>

---

### Q54. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>&#946;</mi></math> is one of the angles between the normals to the ellipse <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>3</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>9</mn></math> at the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>3</mn><mi>cos</mi><mi>&#952;</mi><mo>,</mo><msqrt><mn>3</mn></msqrt><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn><mi>sin</mi><mi>&#952;</mi><mo>,</mo><msqrt><mn>3</mn></msqrt><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mo>;</mo><mo>&#160;</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>; then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>cot</mi><mi>&#946;</mi></mrow><mrow><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow></mfrac></math> is equal to :

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(D)** <math><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given equation of ellipse is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>9</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>3</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p>Normal at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>3</mn><mi>cos</mi><mi>&#952;</mi><mo>,</mo><msqrt><mn>3</mn></msqrt><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>sec</mi><mi>&#952;</mi><mo>.</mo><mi>x</mi><mo>-</mo><msqrt><mn>3</mn></msqrt><mi>cosec</mi><mi>&#952;</mi><mi>y</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>Slope <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>3</mn><mi>sec</mi><mi>&#952;</mi></mrow><mrow><msqrt><mn>3</mn></msqrt><mi>cosec</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><msqrt><mn>3</mn></msqrt><mi>tan</mi><mi>&#952;</mi></math></p><p>Normal at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8722;</mo><mn>3</mn><mi>sin&#952;</mi><mo>,</mo><msqrt><mn>3</mn></msqrt><mi>cos</mi><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn><mi>cosec</mi><mi>&#952;</mi><mo>.</mo><mi>x</mi><mo>-</mo><msqrt><mn>3</mn></msqrt><mi>sec</mi><mi>&#952;</mi><mo>.</mo><mi>y</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>Slope <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mi>cosec</mi><mi>&#952;</mi></mrow><mrow><msqrt><mn>3</mn></msqrt><mi>sec</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mo>-</mo><msqrt><mn>3</mn></msqrt><mi>cot</mi><mi>&#952;</mi></math></p><p>Angle between normal is <math><mi>&#946;</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>&#946;</mi><mo>=</mo><mfenced open="|" close="|"><mfrac><mrow><msub><mi>m</mi><mn>1</mn></msub><mo>-</mo><msub><mi>m</mi><mn>2</mn></msub></mrow><mrow><mn>1</mn><mo>+</mo><msub><mi>m</mi><mn>1</mn></msub><msub><mi>m</mi><mn>2</mn></msub></mrow></mfrac></mfenced><mo>=</mo><mfenced open="|" close="|" separators="|"><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>tan</mi><mi>&#952;</mi><mo>+</mo><msqrt><mn>3</mn></msqrt><mi>cot</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>3</mn></mrow></mfrac></mfenced><mo>=</mo><mfenced open="|" close="|" separators="|"><mfrac><msqrt><mn>3</mn></msqrt><mrow><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>&#946;</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mrow><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow></mfrac><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>cot</mi><mi>&#946;</mi></mrow><mrow><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p>

</details>

---

### Q55. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Two sets <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are as under: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><mo>&#215;</mo><mi>R</mi><mi>&#160;</mi><mo>:</mo><mfenced close="|" open="|" separators="|"><mrow><mi>a</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>&#60;</mo><mn>1</mn><mi>&#160;</mi><mtext>and</mtext><mi>&#160;</mi><mfenced close="|" open="|" separators="|"><mrow><mi>b</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>&#60;</mo><mn>1</mn></mrow></mfenced><mo>;</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><mo>&#215;</mo><mi>R</mi><mo>:</mo><mn>4</mn><msup><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>9</mn><msup><mfenced separators="|"><mrow><mi>b</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup><mo>&#8804;</mo><mn>36</mn></mrow></mfenced><mo>.</mo></math> Then :

**Options:**

- **(A)** neither <math><mi>A</mi><mo>&#8834;</mo><mi>B</mi></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8834;</mo><mi>A</mi></math>
- **(B)** <math><mi>B</mi><mo>⊂</mo><mi>A</mi></math>
- **(C)** <math><mi>A</mi><mo>⊂</mo><mi>B</mi></math>
- **(D)** <math><mi>A</mi><mo>∩</mo><mi>B</mi><mo>=</mo><mi>ϕ</mi></math>  (an empty set)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>A</mi><mo>⊂</mo><mi>B</mi></math>**

**Detailed Solution:**

<p>Given sets, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><mo>&#215;</mo><mi>R</mi><mi>&#160;</mi><mo>:</mo><mfenced close="|" open="|" separators="|"><mrow><mi>a</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>&#60;</mo><mn>1</mn><mi>&#160;</mi><mtext>and</mtext><mi>&#160;</mi><mfenced close="|" open="|" separators="|"><mrow><mi>b</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>&#60;</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><mo>&#215;</mo><mi>R</mi><mi>&#160;</mi><mo>:</mo><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>a</mi><mo>-</mo><mn>5</mn><mo>&#60;</mo><mn>1</mn><mi>&#160;</mi><mtext>and</mtext><mi>&#160;</mi><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>b</mi><mo>-</mo><mn>5</mn><mo>&#60;</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><mo>&#215;</mo><mi>R</mi><mi>&#160;</mi><mo>:</mo><mn>4</mn><mo>&#60;</mo><mi>a</mi><mo>&#60;</mo><mn>6</mn><mi>&#160;</mi><mtext>and</mtext><mi>&#160;</mi><mn>4</mn><mo>&#60;</mo><mi>b</mi><mo>&#60;</mo><mn>6</mn></mrow></mfenced><mo>&#160;</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfrac><mrow><msup><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mn>2</mn></msup><mi>&#160;</mi></mrow><mn>9</mn></mfrac><mo>+</mo><mfrac><msup><mfenced separators="|"><mrow><mi>b</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup><mn>4</mn></mfrac><mo>&#8804;</mo><mn>1</mn></math> </p><p>For set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/86f95aeb-2723-44f2-8d36-9d2f19001c93-image.png" style="width: 265px; height: 237px;" /></p><p>For corner coordinates of the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#160;</mo></math>is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>.</mo><mo>&#160;</mo></math></p><p>For set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>,</mo><mo>&#160;</mo></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4509ca30-3013-418e-bee8-90e2b47732bf-e0dbeab1-9c71-4364-97d7-4bdd2a7cf983-image.png" style="width: 343px; height: 265px;" /></p><p>Now, Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>&#160;</mo></math>in the equation of the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>,</mo><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>9</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8804;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>&#160;</mo></math>lies in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>.</mo><mo>&#160;</mo></math>

Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo></math>also lies in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>.</mo><mo>&#160;</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8834;</mo><mi>B</mi><mo>&#160;</mo></math>.</p>

</details>

---

### Q56. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The eccentricity of an ellipse having centre at the origin, axes along the co-ordinate axes and passing through the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mn>5</mn></msqrt></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Equation of ellipse whose centre at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p>It passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>4</mn><mo>,</mo><mo>&#8722;</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>16</mn><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>16</mn><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Again it passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>&#8722;</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>4</mn><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>4</mn><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>From the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>, we get, </p><p><math><mn>16</mn><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><msup><mi>b</mi><mn>2</mn></msup></math></p><p>  Now, we have, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>e</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math>.</p>

</details>

---

### Q57. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Consider an ellipse, whose center is at the origin and its major axis is along the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis. If its eccentricity is <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math> and the distance between its foci is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>, then the area (in sq. units) of the quadrilateral inscribed in the ellipse, with the vertices as the vertices of the ellipse, is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/776d010f-c45e-431f-8860-7c2e7ccfa90b-image.png" style="width: 250px; height: 151px;" />

Given eccentricity of the ellipse <math> <mrow> </mrow></math><math><mrow><mi>e</mi><mtext> </mtext><mo>=</mo><mtext> </mtext><mfrac> </mfrac><mfrac><mn>3</mn> <mn>5</mn> </mfrac> <mo>.</mo></mrow> </math>

Distance between foci  is  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mi>e</mi><mo>=</mo><mn>6</mn></math>
<math> <mrow> <mo>&rArr;</mo><mtext> </mtext><mi>a</mi><mtext> </mtext><mo>=</mo><mtext> </mtext><mn>5.</mn></mrow> </math>

Also, <math> <mrow> <msup> </msup></mrow></math><math><mrow><msup><mi>b</mi> <mn>2</mn></msup><msup> </msup> <mo>=</mo><msup> <mi>a</mi> <mn>2</mn></msup><msup> </msup> <mtext> </mtext><mo stretchy="false">(</mo><mn>1</mn><mo>&minus;</mo><msup> <mi>e</mi> <mn>2</mn> </msup> <mo stretchy="false">)</mo></mrow> </math>

<math> <mo>&rArr;</mo></math><math> </math> <math><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>25</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>25</mn></mrow></mfrac></mrow></mfenced></math>

<math> <mo>&rArr;</mo> </math> <math><mi>b</mi><mo>=</mo><mn>4</mn></math>

Area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>a</mi><mi>b</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>40</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math>

</details>

---

### Q58. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `1`

The eccentricity of an ellipse whose centre is at the origin is <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> . If one of its directrices is <math><mi>x</mi><mo>=</mo><mo>-</mo><mn>4</mn></math> , then the equation of the normal to it at <math><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> is:

**Options:**

- **(A)** <math><mn>2</mn><mi>y</mi><mo>-</mo><mi>x</mi><mo>=</mo><mn>2</mn></math>
- **(B)** <math><mn>4</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>1</mn></math>
- **(C)** <math><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>7</mn></math>
- **(D)** <math><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>4</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Given, <math><mi>e</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> and <math><mfrac><mrow><mi>a</mi></mrow><mrow><mi>e</mi></mrow></mfrac><mo>=</mo><mn>4</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi></math>

<math><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>2</mn><mo>,&#160;</mo></math></p><p>Also, <math><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>

<math><mo>&#8658;</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>3</mn></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/210efedd-9922-4eb2-883c-4b98159607fd-image.png" style="width: 330px; height: 202px;" /></p><p> Equation of ellipse is  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>3</mn></mfrac><mo>=</mo><mn>1</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi></math>
We know that, equation of normal to the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mi>x</mi></mrow><msub><mi>x</mi><mn>1</mn></msub></mfrac><mo>-</mo><mfrac><mrow><msup><mi>b</mi><mn>2</mn></msup><mi>y</mi></mrow><msub><mi>y</mi><mn>1</mn></msub></mfrac><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup></math>
So, equation of normal at <math><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> is  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>1</mn></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn><mi>y</mi></mrow><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mn>4</mn><mo>-</mo><mn>3</mn></math> 
<math><mo>&#8658;</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q59. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If the distance between the foci of an ellipse is half the length of its latus rectum, then the eccentricity of the ellipse is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></math>
- **(C)** <math><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<math><mn>2</mn><mi>a</mi><mi>e</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>2</mn><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>a</mi></mrow></mfrac></math>

<math><mn>2</mn><mi>e</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

We know that

<math><mi>e</mi><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></msqrt></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mn>2</mn><mi>e</mi></msqrt></math>

<math><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>e</mi></math>

<math><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>e</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

<math><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#177;</mo><msqrt><mn>4</mn><mo>+</mo><mn>4</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#177;</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt><mi>&#160;</mi><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><mo>-</mo><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></math>

<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>e</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></math>

</details>

---

### Q60. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

An ellipse passes through the foci of the hyperbola, <math><mn>9</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>36</mn></math> and its major and minor axes lie along the transverse and conjugate axes of the hyperbola respectively. If the product of eccentricities of the two conics is <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo></math> then which of the following points does not lie on the ellipse?

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mfrac><mrow><msqrt><mn>39</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi> </mi><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mfrac><msqrt><mn>13</mn></msqrt><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><msqrt><mfrac><mrow><mn>13</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt><mo>,</mo><mi> </mi><msqrt><mn>6</mn></msqrt></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><msqrt><mn>13</mn></msqrt><mo>,</mo><mi> </mi><mn>0</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mfrac><msqrt><mn>13</mn></msqrt><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>Equation of the hyperbola
<math><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac><mo>=</mo><mn>1</mn></math>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/127ae8da-47e1-4ef0-818c-cc3c01564de4-image.png" style="width: 300px; height: 192px;" />

Focus of hyperbola <math><mfenced separators="|"><mrow><msub><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi mathvariant="normal"> </mi><mn>0</mn></mrow></mfenced></math> and <math><mo>(</mo><mo>-</mo><msub><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi mathvariant="normal"> </mi><mn>0</mn><mo>)</mo></math>  

<math><msub><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><mo>,</mo><mi mathvariant="normal"> </mi><msub><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mi mathvariant="normal"> </mi><msqrt><mn>1</mn><mo>+</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>4</mn></mrow></mfrac></msqrt><mo>=</mo><mfrac><mrow><msqrt><mn>13</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mo>&there4;</mo></math> Foci would be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>+</mo><msqrt><mn>13</mn></msqrt><mo>,</mo><mi> </mi><mn>0</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><msqrt><mn>13</mn></msqrt><mo>,</mo><mi> </mi><mn>0</mn></mrow></mfenced></math> 

Product of eccentricity would be 

<math><mfrac><mrow><msqrt><mn>13</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi><mo>&sdot;</mo><msub><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mo>&there4;</mo><mi> </mi><mi> </mi><msub><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>13</mn></msqrt></mrow></mfrac></math> .

As the major &amp; minor axis of the ellipse coincide with axis of hyperbola then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub></math> for ellipse would be <math><msqrt><mn>13</mn></msqrt></math> ,

<math><msub><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><msubsup><mrow><mi mathvariant="normal">b</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow><mrow><msubsup><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac></msqrt></math>

<math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>13</mn></msqrt></mrow></mfrac><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><msubsup><mrow><mi mathvariant="normal">b</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow><mrow><mn>13</mn></mrow></mfrac></msqrt></math>

<math><msubsup><mrow><mi mathvariant="normal">b</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mn>12</mn></math>

<math><mo>&there4;</mo></math> Equation of the ellipse would be 

<math><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>13</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>12</mn></mrow></mfrac><mo>=</mo><mn>1</mn><mo>.</mo></math>

Option (1)  <math><mfrac><mrow><mn>39</mn></mrow><mrow><mn>4</mn><mi> </mi><mo>&sdot;</mo><mo>(</mo><mn>13</mn><mo>)</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>12</mn></mrow></mfrac><mo>=</mo><mn>1</mn></math>

Satisfies the equation, hence it lies on the ellipse. 

Option (2) <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>4</mn><mi> </mi><mo>(</mo><mn>13</mn><mo>)</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4.12</mn></mrow></mfrac><mo>=</mo><mn>1</mn></math>

does not lie on the ellipse.

Option (3)  <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>2</mn><mo>(</mo><mn>13</mn><mo>)</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mn>12</mn></mrow></mfrac><mo>=</mo><mn>1</mn></math> satisfy.

Option (4) <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>13</mn></mrow></mfrac><mo>+</mo><mn>0</mn><mo>=</mo><mn>1</mn></math> satisfy.

So, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mfrac><msqrt><mn>13</mn></msqrt><mn>2</mn></mfrac><mo>,</mo><mi> </mi><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math> is the answer.</p>

</details>

---

### Q61. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of the quadrilateral formed by the tangents at the end points of the latus ractum to the ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>9</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>5</mn></mfrac><mo>=</mo><mn>1</mn><mo>,</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mn>2</mn> <mn>7</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>
- **(C)** <math > <mrow>  <mn>18</mn> </mrow></math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>2</mn> <mn>7</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/36f51ce3-d4b2-4097-a9ab-b40794829c3f-image.png" style="width: 250px; height: 276px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>9</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>5</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><mn>5</mn><mn>9</mn></mfrac></msqrt><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn><mi>,</mi><mo>&#160;</mo><msup><mo mathvariant="italic">b</mo><mn>2</mn></msup><mo>=</mo><mn>5</mn></math></p><p>Foci <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mo>&#177;</mo><mo mathvariant="italic">ae</mo><mo mathvariant="italic">,</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mo>&#177;</mo><mn>2</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Ends of latus rectum<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mo>&#177;</mo><mo mathvariant="italic">ae</mo><mi>,</mi><mo>&#177;</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><mi>a</mi></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mo>&#177;</mo><mn>2</mn><mo>,</mo><mo>&#177;</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p>Tangent at &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math>&#39; is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">T</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mi>x</mi></mrow><mn>9</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mi>y</mi><mn>5</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p>It cuts coordinate axes at <math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">P</mo><mfenced><mrow><mfrac><mn>9</mn><mn>2</mn></mfrac><mo mathvariant="italic">,</mo><mn>0</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo mathvariant="italic">Q</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>Area of quadrilateral <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mi>R</mi><mi>S</mi><mo>=</mo><mn>4</mn></math> (Area of triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>P</mi><mi>Q</mi></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4&#160;</mn><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mn>7</mn></math> sq. units</p>

</details>

---

### Q62. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>B</mi></math> is the semi-minor axis of an ellipse, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>2</mn></msub></math> are its focii and the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>1</mn></msub><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>2</mn></msub><mi>B</mi></math> is a right angle, then the square of the eccentricity of the ellipse is

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <msqrt> <mn>2</mn> </msqrt> </mrow> </mfrac> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> <msqrt> <mn>2</mn> </msqrt> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<p>In standard ellipse  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msup><mi>a</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p>Semi-major axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>A</mi><mo>=</mo><mi>a</mi></math></p><p>Semi-minor axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>B</mi><mo>=</mo><mi>b</mi></math></p><p>Focus <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>1</mn></msub><mo>&#8801;</mo><mfenced><mrow><mo>-</mo><mi>a</mi><mi>e</mi><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>2</mn></msub><mo>&#8801;</mo><mfenced><mrow><mi>a</mi><mi>e</mi><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/97267906-9fe5-4c22-8e5c-e302e59d48ac-image.png" style="width: 350px; height: 191px;" />

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8736;</mo><msub><mi>F</mi><mn>1</mn></msub><mi>B</mi><msub><mi>F</mi><mn>2</mn></msub><mo>=</mo><mn>9</mn><mn>0</mn><mo>&#176;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><msub><mi>F</mi><mn>1</mn></msub><mo>=</mo><mi>O</mi><msub><mi>F</mi><mn>2</mn></msub><mo>&#8658;</mo><mo>&#8736;</mo><msub><mi>F</mi><mn>1</mn></msub><mi>B</mi><mi>O</mi><mo>=</mo><mo>&#8736;</mo><msub><mi>F</mi><mn>2</mn></msub><mi>B</mi><mi>O</mi><mo>=</mo><mn>4</mn><mn>5</mn><mo>&#176;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>a</mi><mi>e</mi></mrow><mi>b</mi></mfrac><mo>=</mo><mo>tan</mo><mn>4</mn><mn>5</mn><mo>&#176;</mo><mo>=</mo><mn>1</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mi>a</mi><mi>e</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><msup><mi>e</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>e</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q63. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `1`

If the foci of the ellipse $\frac{x^2}{16}+\frac{y^2}{b^2}=1$ coincide with the foci of the hyperbola $\frac{x^2}{144}-\frac{y^2}{81}=\frac{1}{25}$, then $b^2$ is equal to

**Options:**

- **(A)** 8
- **(B)** 10
- **(C)** 7
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7**

**Detailed Solution:**

Given equation of ellipse is
$$
\frac{x^2}{16}+\frac{y^2}{b^2}=1
$$

$$
\begin{aligned}
& \text { eccentricity }=e=\sqrt{1-\frac{b^2}{16}} \\
& \text { foci: } \pm a e=\pm 4 \sqrt{1-\frac{b^2}{16}}
\end{aligned}
$$
Equation of hyperbola is $\frac{x^2}{144}-\frac{y^2}{81}=\frac{1}{25}$
$$
\begin{aligned}
& \Rightarrow \frac{x^2}{\frac{144}{25}}-\frac{y^2}{\frac{81}{25}}=1 \\
& \text { eccentricity }=e=\sqrt{1+\frac{81}{25} \times \frac{25}{144}}=\sqrt{1+\frac{81}{144}} \\
& =\sqrt{\frac{225}{144}}=\frac{15}{12} \\
& \text { foci: } \pm a e=\pm \frac{12}{5} \times \frac{15}{12}=\pm 3 \\
&
\end{aligned}
$$
Since, foci of ellipse and hyperbola coincide
& \therefore \pm 4 \sqrt{1-\frac{b^2}{16}}=\pm 3 \Rightarrow b^2=7 \\
$$

</details>

---

### Q64. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `3`

An ellipse is drawn by taking a diameter of the circle $(x-1)^2+y^2=1$ as its semiminor axis and a diameter of the circle $x^2+(y-2)^2=4$ as its semi-major axis. If the centre of the ellipse is the origin and its axes are the coordinate axes, then the equation of the ellipse is

**Options:**

- **(A)** $4 x^2+y^2=4$
- **(B)** $x^2+4 y^2=8$
- **(C)** $4 x^2+y^2=8$
- **(D)** $x^2+4 y^2=16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x^2+4 y^2=16$**

**Detailed Solution:**

Semi minor axis $b=2$
Semi major axis $a=4$
Equation of ellipse $=\frac{x^2}{a^2}+\frac{y^2}{b^2}=1 \quad \Rightarrow \frac{x^2}{16}+\frac{y^2}{4}=1$
$\Rightarrow x^2+4 y^2=16$.

</details>

---

### Q65. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

A focus of an ellipse is at the origin. The directrix is the line $x=4$ and the eccentricity is $1 / 2$. Then the length of the semi-major axis is

**Options:**

- **(A)** $\frac{8}{3}$
- **(B)** $\frac{2}{3}$
- **(C)** $\frac{4}{3}$
- **(D)** $\frac{5}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{8}{3}$**

**Detailed Solution:**

Major axis is along $x$-axis.
$$
\begin{aligned}
& \frac{a}{e}-a e=4 \\
& a\left(2-\frac{1}{2}\right)=4 \\
& a=\frac{8}{3} .
\end{aligned}
$$

</details>

---

### Q66. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

In an ellipse, the distance between its foci is 6 and minor axis is 8. Then its eccentricity is

**Options:**

- **(A)** $\frac{3}{5}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{4}{5}$
- **(D)** $\frac{1}{\sqrt{5}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{5}$**

**Detailed Solution:**

$2 a e=6 \Rightarrow a e=3$
$2 b=8 \Rightarrow b=4$
$b^2=a^2\left(1-e^2\right)$
$16=a^2-a^2 e^2$
$a^2=16+9=25$
$a=5$
$\therefore e=\frac{3}{a}=\frac{3}{5}$

</details>

---

### Q67. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

An ellipse has $\mathrm{OB}$ as semi minor axis, $\mathrm{F}$ and $\mathrm{F}^{\prime}$ its focii and the angle FBF' is a right angle. Then the eccentricity of the ellipse is

**Options:**

- **(A)** $\frac{1}{\sqrt{2}}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{1}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\sqrt{2}}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/YgtQRD-UT57iIAcuTZ85Orf7bdxN-5qWdQjTdxERSog.original.fullsize.png">

$$
\begin{aligned}
& \because \angle \text { FBF }^{\prime}=90^{\circ} \\
& \therefore\left(\sqrt{a^2 e^2+b^2}\right)^2+\left(\sqrt{a^2 e^2+b^2}\right)^2=(2 a \mathrm{e})^2 \\
& \Rightarrow 2\left(a^2 e^2+b^2\right)=4 a^2 e^2 \\
& \Rightarrow \mathrm{e}^2=\mathrm{b}^2 / \mathrm{a}^2 \\
& \text { Also } \mathrm{e}^2=1-\mathrm{b}^2 / \mathrm{a}^2=1-\mathrm{e}^2 \\
& \Rightarrow 2 \mathrm{e}^2=1, \mathrm{e}=\frac{1}{\sqrt{2}} .
\end{aligned}
$$

</details>

---

### Q68. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

The eccentricity of an ellipse, with its centre at the origin, is $\frac{1}{2}$. If one of the directrices is $x=$ 4 , then the equation of the ellipse is

**Options:**

- **(A)** $3 x^2+4 y^2=1$
- **(B)** $3 x^2+4 y^2=12$
- **(C)** $4 x^2+3 y^2=12$
- **(D)** $4 x^2+3 y^2=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 x^2+4 y^2=12$**

**Detailed Solution:**

Equation of directrix is $x=a / e=4 \Rightarrow a=2$
$$
b^2=a^2\left(1-e^2\right) \Rightarrow b^2=3
$$
Hence equation of ellipse is $3 x^2+4 y^2=12$

</details>

---

### Q69. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

The foci of the ellipse $\frac{x^2}{16}+\frac{y^2}{b^2}=1$ and the hyperbola $\frac{x^2}{144}-\frac{y^2}{81}=\frac{1}{25}$ coincide. Then the value of $b^2$ is

**Options:**

- **(A)** 9
- **(B)** 1
- **(C)** 5
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 7**

**Detailed Solution:**

$\frac{x^2}{144}-\frac{y^2}{81}=\frac{1}{25}$
$\mathrm{a}=\sqrt{\frac{144}{25}}, \mathrm{~b}=\sqrt{\frac{81}{25}}, \mathrm{e}=\sqrt{1+\frac{81}{144}}=\frac{15}{12}=\frac{5}{4}$
Foci $=(3,0)$, focus of ellipse $=(3,0) \Rightarrow \mathrm{e}=\frac{3}{4}$
$b^2=16\left(1-\frac{9}{16}\right)=7$

</details>

---

