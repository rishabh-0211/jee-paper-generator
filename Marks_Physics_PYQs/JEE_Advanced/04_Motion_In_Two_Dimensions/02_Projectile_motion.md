# JEE Advanced Physics - Motion In Two Dimensions

## Topic 2: Projectile motion

**Total Questions:** 12

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

A particle is thrown with a speed $v$ from a point $O$ at an angle $\theta$ with the horizontal plane such that it passes through the point $P$ at a height of $1$ m and horizontal distance of $5$ m from $O$, as shown in the figure. If acceleration due to gravity is $g$ ms$^{-2}$, then the correct statement(s) is/are:
<img style="width: 550px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p1_english__q22_d1.png" />

**Options:**

- **(A)** If $\theta = 45^\circ$, then $v = \dfrac{5\sqrt{g}}{2}$ ms$^{-1}$.
- **(B)** If $\theta = 45^\circ$, the particle reaches its maximum height before it reaches $P$.
- **(C)** If $\theta = 30^\circ$, the particle reaches its maximum height after reaching $P$.
- **(D)** If $\theta = \tan^{-1}\left(\dfrac{1}{5}\right)$, then $v = 125\sqrt{g}$ ms$^{-1}$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) If $\theta = 45^\circ$, the particle reaches its maximum height before it reaches $P$.**

**Detailed Solution:**

The equation of trajectory of a projectile is given by:

$y = x \tan \theta - \dfrac{g x^2}{2 v^2 \cos^2 \theta}$

The particle passes through point $P(5, 1)$. Substituting $x = 5$ and $y = 1$:

$1 = 5 \tan \theta - \dfrac{25 g}{2 v^2 \cos^2 \theta}$

For option (A), substituting $\theta = 45^\circ$:

$1 = 5 \tan 45^\circ - \dfrac{25 g}{2 v^2 \cos^2 45^\circ}$

$1 = 5(1) - \dfrac{25 g}{2 v^2 (1/2)}$

$1 = 5 - \dfrac{25 g}{v^2}$

$\dfrac{25 g}{v^2} = 4 \Rightarrow v^2 = \dfrac{25 g}{4} \Rightarrow v = \dfrac{5\sqrt{g}}{2}$ ms$^{-1}$

Thus, option (A) is correct.

For option (B), the horizontal distance to the maximum height is $x_m = \dfrac{R}{2} = \dfrac{v^2 \sin(2\theta)}{2g}$.

For $\theta = 45^\circ$ and $v^2 = \dfrac{25g}{4}$:

$x_m = \dfrac{\left(\dfrac{25g}{4}\right) \sin 90^\circ}{2g} = \dfrac{25}{8} = 3.125$ m

Since $x_m = 3.125$ m $< 5$ m, the particle reaches its maximum height before it reaches $P$. Thus, option (B) is correct.

For option (C), substituting $\theta = 30^\circ$ into the trajectory equation:

$1 = 5 \tan 30^\circ - \dfrac{25 g}{2 v^2 \cos^2 30^\circ}$

$1 = \dfrac{5}{\sqrt{3}} - \dfrac{25 g}{2 v^2 (3/4)} \Rightarrow \dfrac{50 g}{3 v^2} = \dfrac{5}{\sqrt{3}} - 1$

$v^2 = \dfrac{50\sqrt{3}g}{3(5 - \sqrt{3})}$

The horizontal distance to the maximum height is:

$x_m = \dfrac{v^2 \sin 60^\circ}{2g} = \dfrac{v^2 \sqrt{3}}{4g} = \dfrac{50\sqrt{3}g}{3(5 - \sqrt{3})} \times \dfrac{\sqrt{3}}{4g} = \dfrac{25}{2(5 - \sqrt{3})} \approx 3.82$ m

Since $x_m < 5$ m, the particle reaches its maximum height before reaching $P$. Thus, option (C) is incorrect.

For option (D), substituting $\theta = \tan^{-1}\left(\dfrac{1}{5}\right)$, so $\tan \theta = \dfrac{1}{5}$:

$1 = 5\left(\dfrac{1}{5}\right) - \dfrac{25 g}{2 v^2 \cos^2 \theta} \Rightarrow 1 = 1 - \dfrac{25 g}{2 v^2 \cos^2 \theta}$

$\dfrac{25 g}{2 v^2 \cos^2 \theta} = 0$

This is only possible if $v \to \infty$. Thus, option (D) is incorrect.

Answer: If $\theta = 45^\circ$, then $v = \dfrac{5\sqrt{g}}{2}$ ms$^{-1}$.; If $\theta = 45^\circ$, the particle reaches its maximum height before it reaches $P$.

</details>

---

### Q2. JEE Advanced 2025 (Paper 2)

*Type:* `numerical` | *Level:* `2`

A projectile of mass 200 g is launched in a viscous medium at an angle $60^{\circ}$ with the horizontal, with an initial velocity of $270 \mathrm{~m} / \mathrm{s}$. It experiences a viscous drag force $\vec{F}=-c \vec{v}$ where the drag coefficient $c=0.1 \mathrm{~kg} / \mathrm{s}$ and $\vec{v}$ is the instantaneous velocity of the projectile. The projectile hits a vertical wall after 2 s . Taking $e=2.7$, the horizontal distance of the wall from the point of projection (in m ) is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **170**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/mT-03WjplujBtna1y1Inz8Vxz_uLYLRMxIFjEMUE278.original.fullsize.png">
$\overrightarrow{\mathrm{F}}_{\mathrm{net}}=\mathrm{m} \frac{\mathrm{~d} \overrightarrow{\mathrm{v}}}{\mathrm{dt}}$
$\mathrm{mg}+\overrightarrow{\mathrm{F}}=\frac{\mathrm{md} \overrightarrow{\mathrm{v}}}{\mathrm{dt}}$
$\mathrm{mg}-\mathrm{C} \overrightarrow{\mathrm{v}}=\frac{\mathrm{md} \overrightarrow{\mathrm{v}}}{\mathrm{dt}}$
Horizontal direction
$-\mathrm{Cv}_{\mathrm{x}}=\frac{\mathrm{mdv}_{\mathrm{x}}}{\mathrm{dt}}$
$\begin{aligned} & -\frac{C}{m} \int_0^t d t=\int_{v_{0 x}}^{v_x} \frac{d v_x}{v_x} \\ & -\frac{t}{2}=\ell n \frac{v_x}{v_{0 x}} \\ & \frac{d x}{d t}=v_x=v_{0 x} e^{-t / 2} \\ & \int_0^{S_x} d x=v_{0 x} \int_0^t e^{-t / 2} d t \\ & S_x=2 v_{0 x}\left(1-e^{-t / 2}\right) \\ & \text { at } t=2 \sec \end{aligned}$
$\begin{aligned} & \mathrm{S}_{\mathrm{x}}=2 \times 270 \times \cos 60^{\circ}\left[1-\frac{1}{\mathrm{e}}\right] \\ & \mathrm{S}_{\mathrm{x}}=270\left(1-\frac{1}{2.7}\right) \\ & =\frac{270}{2.7} \times(1.7) \\ & =170 \mathrm{~m} \\ & \mathrm{~S}_{\mathrm{x}}=170 \mathrm{~m}\end{aligned}$

</details>

---

### Q3. JEE Advanced 2023 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

<p>A slide with a frictionless curved surface, which becomes horizontal at its lower end, is fixed on the terrace of a building of height <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>h</mi></math> from the ground, as shown in the figure. A spherical ball of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is released on the slide from rest at a height <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math> from the top of the terrace. The ball leaves the slide with a velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>u</mi><mo>&#8594;</mo></mover><mn>0</mn></msub><mo>=</mo><msub><mi>u</mi><mn>0</mn></msub><mover><mi>x</mi><mo>&#8743;</mo></mover></math> and falls on the ground at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> from the building making an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> with the horizontal. It bounces off with a velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover></math> and reaches a maximum height <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>h</mi><mn>1</mn></msub></math>. The acceleration due to gravity is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> and the coefficient of restitution of the ground is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math>. Which of the following statement(s) is(are) correct?</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/f7208a69-a5ba-4db4-a179-b415761f2923.png" style="width: 500px; height: 282px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>u</mi><mo>&#8594;</mo></mover><mn>0</mn></msub><mo>=</mo><msqrt><mn>2</mn><mi>g</mi><mi>h</mi></msqrt><mover><mi>x</mi><mo>&#8743;</mo></mover></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><msqrt><mn>2</mn><mi>g</mi><mi>h</mi></msqrt><mfenced><mrow><mover><mi>x</mi><mo>&#8743;</mo></mover><mo>-</mo><mover><mi>z</mi><mo>&#8743;</mo></mover></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><msup><mn>60</mn><mi mathvariant="normal">o</mi></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><msub><mi>h</mi><mn>1</mn></msub></mfrac><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><msub><mi>h</mi><mn>1</mn></msub></mfrac><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/8121f631-c7a5-4bbd-a9c5-602950b55627.png" style="width: 500px; height: 312px;" /></p><p>Using energy conservation,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>g</mi><mi>h</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>m</mi><msup><mfenced><msub><mi>u</mi><mn>0</mn></msub></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>u</mi><mn>0</mn></msub><mo>=</mo><msqrt><mn>2</mn><mi>g</mi><mi>h</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>u</mi><mn>0</mn></msub></math> is the horizontal component of the velocity throughout the flight. For vertical component of the velocity(just before collision with the ground), we can use equation of motion</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><msub><mi>v</mi><mi>z</mi></msub></mfenced><mn>2</mn></msup><mo>=</mo><msup><mn>0</mn><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mi>g</mi></mrow></mfenced><mfenced><mrow><mo>-</mo><mn>3</mn><mi>h</mi></mrow></mfenced><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>v</mi><mi>z</mi></msub><mo>=</mo><msqrt><mn>6</mn><mi>g</mi><mi>h</mi></msqrt></math></p><p>Angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> can be written as,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><msub><mi>v</mi><mi>z</mi></msub><mi>u</mi></mfrac><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><msup><mn>60</mn><mi mathvariant="normal">o</mi></msup></math></p><p>Horizontal distance covered just before the collision will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><msub><mi>u</mi><mn>0</mn></msub><mi>T</mi><mspace linebreak="newline"></mspace><mo>=</mo><msub><mi>u</mi><mn>0</mn></msub><msqrt><mn>2</mn><mfenced><mfrac><mrow><mn>3</mn><mi>h</mi></mrow><mi>g</mi></mfrac></mfenced></msqrt><mspace linebreak="newline"></mspace><mo>=</mo><msqrt><mn>2</mn><mi>g</mi><mi>h</mi></msqrt><msqrt><mfenced><mn>2</mn></mfenced><mfenced><mfrac><mrow><mn>3</mn><mi>h</mi></mrow><mi>g</mi></mfrac></mfenced></msqrt><mspace linebreak="newline"></mspace><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mi>h</mi></math></p><p>After collision, only velocity along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math>-direction changes. Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mn>1</mn></msub><mo>=</mo><mi>e</mi><msub><mi>v</mi><mi>z</mi></msub><mo>=</mo><msqrt><mn>2</mn><mi>g</mi><mi>h</mi></msqrt></math> and hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>v</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>u</mi><mn>0</mn></msub><mover><mi>i</mi><mo>&#8743;</mo></mover><mo>+</mo><msub><mi>v</mi><mn>1</mn></msub><mover><mi>k</mi><mo>&#8743;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>2</mn><mi>g</mi><mi>h</mi></msqrt><mfenced close="]" open="["><mrow><mover><mi>i</mi><mo>&#8743;</mo></mover><mo>+</mo><mover><mi>k</mi><mo>&#8743;</mo></mover></mrow></mfenced><mspace linebreak="newline"></mspace><mo>=</mo><msqrt><mn>2</mn><mi>g</mi><mi>h</mi></msqrt><mfenced close="]" open="["><mrow><mover><mi>x</mi><mo>&#8743;</mo></mover><mo>+</mo><mover><mi>z</mi><mo>&#8743;</mo></mover></mrow></mfenced></math></p><p>Now, maximum height achieved after collision will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>h</mi><mn>1</mn></msub><mo>=</mo><mfrac><msup><msub><mi>v</mi><mn>1</mn></msub><mn>2</mn></msup><mrow><mn>2</mn><mi>g</mi></mrow></mfrac><mo>=</mo><mi>h</mi></math>.</p><p>Finally, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>u</mi><mn>0</mn></msub><mo>=</mo><msqrt><mn>2</mn><mi>g</mi><mi>h</mi></msqrt><mo>,</mo><mo>&#160;</mo><mi>&#952;</mi><mo>=</mo><msup><mn>60</mn><mi mathvariant="normal">o</mi></msup><mo>,</mo><mo>&#160;</mo><mfrac><mi>d</mi><msub><mi>h</mi><mn>1</mn></msub></mfrac><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>.</p>

</details>

---

### Q4. JEE Advanced 2022 (Paper 1)

*Type:* `numerical` | *Level:* `1`

A projectile is fired from horizontal ground with speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi></math> and projection angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math>. When the acceleration due to gravity is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math>, the range of the projectile is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>. If at the highest point in its trajectory, the projectile enters a different region where the effective acceleration due to gravity is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>'</mo></msup><mo>=</mo><mfrac><mi>g</mi><mrow><mn>0</mn><mo>.</mo><mn>81</mn></mrow></mfrac></math>, then the new range is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>d</mi><mo>'</mo></msup><mo>=</mo><mi>n</mi><mi>d</mi><mo>.</mo></math> The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.95**

**Detailed Solution:**

<blockquote><p>Horizontal range of the projectile is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mfrac><mrow><msup><mi>v</mi><mn>2</mn></msup><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow><mi>g</mi></mfrac></math></p><p>Maximum height attained by the projectile is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi><mo>=</mo><mfrac><mrow><msup><mi>v</mi><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac></math></p><p>So, after entering the new region, time taken by projectile to reach ground</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn><mi>H</mi></mrow><msup><mi>g</mi><mo>&#39;</mo></msup></mfrac></msqrt></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn><mfenced><mstyle displaystyle="true"><mfrac><mrow><msup><mi>v</mi><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac></mstyle></mfenced></mrow><mstyle displaystyle="true"><mfrac><mi>g</mi><mrow><mn>0</mn><mo>.</mo><mn>81</mn></mrow></mfrac></mstyle></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>94</mn><mi>v</mi><mi>sin</mi><mi>&#952;</mi></mrow><mi>g</mi></mfrac></math></p><p>So, horizontal displacement done by the projectile in new region is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>9</mn><mi>v</mi><mi>sin</mi><mi>&#952;</mi></mrow><mi>g</mi></mfrac><mo>&#215;</mo><mi>v</mi><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>9</mn><mfrac><mrow><msup><mi>v</mi><mn>2</mn></msup><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac></math></p><p>So, new range is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>d</mi><mo>&#39;</mo></msup><mo>=</mo><mfrac><mi>d</mi><mn>2</mn></mfrac><mo>+</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mi>v</mi><mn>2</mn></msup><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac><mo>+</mo><mn>0</mn><mo>.</mo><mn>9</mn><mfrac><mrow><msup><mi>v</mi><mn>2</mn></msup><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>95</mn><mo>&#160;</mo><mi>d</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>95</mn><mo>&#160;</mo><mi mathvariant="normal">d</mi></math></p></blockquote>

</details>

---

### Q5. JEE Advanced 2021 (Paper 1)

*Type:* `numerical` | *Level:* `1`

A projectile is thrown from a point $\mathrm{O}$ on the ground at an angle $45^{\circ}$ from the vertical and with a speed $5 \sqrt{2} \mathrm{~m} / \mathrm{s}$. The projectile at the highest point of its trajectory splits into two equal parts. One part falls vertically down to the ground, $0.5 \mathrm{~s}$ after the splitting. The other part, $t$ seconds after the splitting, falls to the ground at a distance $x$ meters from the point O. The acceleration due to gravity $g=10 \mathrm{~m} / \mathrm{s}^{2}$.
The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7.5**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/4731f6d0-00df-4d09-8598-ce80c9599f21-image.png" style="width: 400px; height: 172px;" /></p><p>So,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>R</mi><mn>2</mn></mfrac><mo>+</mo><mi>r</mi></math> </p><p>Where,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is the range of oblique projectile and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is the range of horizontal projectile.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>R</mi><mn>2</mn></mfrac><mo>+</mo><mn>10</mn><mo>&#215;</mo><msqrt><mfrac><mrow><mn>2</mn><mi>h</mi></mrow><mi>g</mi></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><msup><mi>u</mi><mn>2</mn></msup><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow><mrow><mi>g</mi><mo>&#215;</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mn>10</mn><mo>&#215;</mo><mn>0.5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>50</mn><mn>20</mn></mfrac><mo>+</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2.5</mn><mo>+</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>7.5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p>

</details>

---

### Q6. JEE Advanced 2021 (Paper 1)

*Type:* `numerical` | *Level:* `1`

A projectile is thrown from a point $\mathrm{O}$ on the ground at an angle $45^{\circ}$ from the vertical and with a speed $5 \sqrt{2} \mathrm{~m} / \mathrm{s}$. The projectile at the highest point of its trajectory splits into two equal parts. One part falls vertically down to the ground, $0.5 \mathrm{~s}$ after the splitting. The other part, $t$ seconds after the splitting, falls to the ground at a distance $x$ meters from the point O. The acceleration due to gravity $g=10 \mathrm{~m} / \mathrm{s}^{2}$.
The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> is _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.5**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ec94909c-b9ed-4731-8d59-52f05eecd4e4-image.png" style="width: 500px; height: 145px;" /></p><p>After splitting of projectile in two equal parts one part falls vertically down to the ground. </p><p>So, velocity of another part will be according to conservation of linear momentum,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>&#215;</mo><mn>5</mn><mo>=</mo><mfrac><mi>m</mi><mn>2</mn></mfrac><mo>&#215;</mo><mn>0</mn><mo>+</mo><mfrac><mi>m</mi><mn>2</mn></mfrac><mo>&#215;</mo><mi>v</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>v</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup></math></p><p>Now time taken by <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mn>1</mn></msub></math>, to reach ground, </p><p>since after splitting of projectile <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mn>1</mn></msub></math> will perform horizontal projectile so,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn><mi>h</mi></mrow><mi>g</mi></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn><msup><mi>u</mi><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mn>2</mn><msup><mi>g</mi><mn>2</mn></msup></mrow></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>50</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></msqrt><mo>=</mo><msqrt><mn>0.25</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>0.5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> </p>

</details>

---

### Q7. JEE Advanced 2020 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `1`

<p>A uniform electric field, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>E</mi><mo>→</mo></mover><mo>=</mo><mo>-</mo><mn>400</mn><msqrt><mn>3</mn></msqrt><mo> </mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo> </mo><mi mathvariant="normal">N</mi><mo> </mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> is applied in a region. A charged particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> carrying positive charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> is projected in this region with an initial speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>10</mn></msqrt><mo>×</mo><msup><mn>10</mn><mn>6</mn></msup><mo> </mo><mi mathvariant="normal">m</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. This particle is aimed to hit a target <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math>, which is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo> </mo><mi mathvariant="normal">m</mi></math> away from its entry point into the field as shown schematically in the figure. Take <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>q</mi><mi>m</mi></mfrac><mo>=</mo><msup><mn>10</mn><mn>10</mn></msup><mo> </mo><mi mathvariant="normal">C</mi><mo> </mo><msup><mi>kg</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. Then</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/7a2b89eb-38aa-4693-b2b8-03e4c1edc461-image.png"/></p>

**Options:**

- **(A)** the particle will hit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">T</mi></math> if projected at an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>&#176;</mo></math> from the horizontal
- **(B)** the particle will hit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">T</mi></math> if projected either at an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#176;</mo></math> or  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>&#176;</mo></math> from the horizontal
- **(C)** time taken by the particle to hit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">T</mi></math> could be <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>5</mn><mn>6</mn></mfrac></msqrt><mi>&#956;</mi><mi mathvariant="normal">s</mi></math> as well as <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>5</mn><mn>2</mn></mfrac></msqrt><mi>&#956;</mi><mi mathvariant="normal">s</mi></math>
- **(D)** time taken by the particle to hit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">T</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>5</mn><mn>3</mn></mfrac></msqrt><mi>&#956;</mi><mi>s</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) time taken by the particle to hit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">T</mi></math> could be <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>5</mn><mn>6</mn></mfrac></msqrt><mi>&#956;</mi><mi mathvariant="normal">s</mi></math> as well as <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>5</mn><mn>2</mn></mfrac></msqrt><mi>&#956;</mi><mi mathvariant="normal">s</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>y</mi></msub><mo>=</mo><mfrac><mi>E</mi><mi>M</mi></mfrac><mo>=</mo><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>×</mo><msup><mn>10</mn><mn>12</mn></msup><mo> </mo><mi mathvariant="normal">m</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mn>2</mn></msup></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/d26e9e69-5cd5-443d-a87f-508327036d0b-image.png"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>=</mo><mfrac><mrow><msup><mi mathvariant="normal">u</mi><mn>2</mn></msup><mi>sin</mi><mn>2</mn><mi>θ</mi></mrow><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">y</mi></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>2</mn><mi>θ</mi><mo>=</mo><mfrac><mrow><mi>R</mi><msub><mi>a</mi><mi>y</mi></msub></mrow><msup><mi>u</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>θ</mi><mo>=</mo><mn>30</mn><mo>°</mo></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>°</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>u</mi><mi>sin</mi><mo> </mo><mn>30</mn><mo>°</mo></mrow><msub><mi>a</mi><mi>y</mi></msub></mfrac></math> or  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>u</mi><mi>sin</mi><mo> </mo><mn>60</mn><mo>°</mo></mrow><msub><mi>a</mi><mi>y</mi></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mn>5</mn><mn>6</mn></mfrac></msqrt><mi>μ</mi><mi mathvariant="normal">s</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>5</mn><mn>2</mn></mfrac></msqrt><mi>μ</mi><mi mathvariant="normal">s</mi></math></p>

</details>

---

### Q8. JEE Advanced 2019 (Paper 2)

*Type:* `numerical` | *Level:* `1`

<p>A ball is thrown from ground at an angle <math><mi mathvariant="normal">θ</mi></math> with horizontal and with an initial speed <math><msub><mrow><mi mathvariant="normal">u</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>.</mo></math> For the resulting projectile motion, the magnitude of average velocity of the ball up to the point when it hits the ground for the first time is <math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>.</mo></math> After hitting the ground, ball rebounds at the same angle <math><mi mathvariant="normal">θ</mi></math> but with a reduced speed of <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">u</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">α</mi></mrow></mfrac><mo>.</mo></math> Its motion continues for a long time as shown in figure. If the magnitude of average velocity of the ball for entire duration of motion is <math><mn>0.8</mn><mtext> </mtext><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo></math> the value of <math><mi mathvariant="normal">α</mi></math> is______
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/9e4cc92b-70db-4e0f-90dc-127f599005f2-image25.png"/></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

For first projectile
Average velocity, <math><mfenced close=〉 open=〈 separators=|><mrow><mi>V</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>R</mi></mrow><mrow><mi>T</mi></mrow></mfrac><mo>=</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>x</mi></mrow></msub><mo>=</mo><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub><mi> </mi><mfenced close=] open=[ separators=|><mrow><mtable><mtr><mtd><mrow><maligngroup></maligngroup><mfenced separators=|><mrow><mi mathvariant=normal>w</mi><mi mathvariant=normal>h</mi><mi mathvariant=normal>e</mi><mi mathvariant=normal>r</mi><mi mathvariant=normal>e</mi><mi mathvariant=normal> </mi><mi>R</mi><mo>=</mo><mi mathvariant=normal>R</mi><mi mathvariant=normal>a</mi><mi mathvariant=normal>n</mi><mi mathvariant=normal>g</mi><mi mathvariant=normal>e</mi><mi mathvariant=normal> </mi><mi mathvariant=normal>a</mi><mi mathvariant=normal>n</mi><mi mathvariant=normal>d</mi><mi mathvariant=normal> </mi><mi>T</mi><mo>=</mo><mi mathvariant=normal>T</mi><mi mathvariant=normal>i</mi><mi mathvariant=normal>m</mi><mi mathvariant=normal>e</mi><mi mathvariant=normal> </mi><mi mathvariant=normal>o</mi><mi mathvariant=normal>f</mi><mi mathvariant=normal> </mi><mi mathvariant=normal>f</mi><mi mathvariant=normal>l</mi><mi mathvariant=normal>i</mi><mi mathvariant=normal>g</mi><mi mathvariant=normal>h</mi><mi mathvariant=normal>t</mi></mrow></mfenced></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mtable><mtr><mtd><mi>R</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msub><mrow><mi>U</mi></mrow><mrow><mi>x</mi></mrow></msub><mo>.</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>y</mi></mrow></msub></mrow><mrow><mi>g</mi></mrow></mfrac></mtd><mtd><mi>T</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mo>.</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>y</mi></mrow></msub></mrow><mrow><mi>g</mi></mrow></mfrac></mtd></mtr></mtable></mrow></mtd></mtr></mtable></mrow></mfenced></math>
For journey
<math><msub><mrow><mfenced close=〉 open=〈 separators=|><mrow><mi>V</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>→</mo><mi>n</mi></mrow></msub><mo>=</mo><mfrac><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mo>…</mo><mo>+</mo><msub><mrow><mi>R</mi></mrow><mrow><mi>n</mi></mrow></msub></mrow><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mo>…</mo><mo>+</mo><msub><mrow><mi>T</mi></mrow><mrow><mi>n</mi></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mfrac><mrow><mn>2</mn><msub><mrow><mi>u</mi></mrow><mrow><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></msub><msub><mrow><mi>u</mi></mrow><mrow><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></msub></mrow><mrow><mi>g</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><msub><mrow><mi>u</mi></mrow><mrow><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></msub><msub><mrow><mi>u</mi></mrow><mrow><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></msub></mrow><mrow><mi>g</mi></mrow></mfrac><mo>+</mo><mo>…</mo><mo>+</mo><mfrac><mrow><mn>2</mn><msub><mrow><mi>u</mi></mrow><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msub></mrow></msub><msub><mrow><mi>u</mi></mrow><mrow><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi></mrow></msub></mrow></msub></mrow><mrow><mi>g</mi></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>2</mn><msub><mrow><mi>u</mi></mrow><mrow><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></msub></mrow><mrow><mi>g</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><msub><mrow><mi>u</mi></mrow><mrow><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></msub></mrow><mrow><mi>g</mi></mrow></mfrac><mo>+</mo><mo>…</mo><mfrac><mrow><mn>2</mn><msub><mrow><mi>u</mi></mrow><mrow><msub><mrow><mi>y</mi></mrow><mrow><mi>n</mi></mrow></msub></mrow></msub></mrow><mrow><mi>g</mi></mrow></mfrac></mrow></mfrac></math>
<math><mo>⇒</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>x</mi></mrow></msub><mfenced close=] open=[ separators=|><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>α</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac><mo>+</mo><mo>…</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn><mi>n</mi></mrow></msup></mrow></mfrac></mrow><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>α</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mo>…</mo><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>α</mi></mrow><mrow><mi>n</mi></mrow></msup></mrow></mfrac></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>0.8</mn><mi> </mi><msub><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi> </mi><mfenced close=] open=[ separators=|><mrow><mtable><mtr><mtd><mrow><maligngroup></maligngroup><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>α</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac><mo>+</mo><mo>…</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn><mi>n</mi></mrow></msup></mrow></mfrac><mo>⇒</mo><mi>G</mi><mi>e</mi><mi>o</mi><mi>m</mi><mi>e</mi><mi>t</mi><mi>r</mi><mi>i</mi><mi>c</mi><mi> </mi><mi>p</mi><mi>r</mi><mi>o</mi><mi>g</mi><mi>r</mi><mi>e</mi><mi>s</mi><mi>s</mi><mi>i</mi><mi>o</mi><mi>n</mi></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mi>S</mi><mi>u</mi><mi>m</mi><mi> </mi><mi>o</mi><mi>f</mi><mi> </mi><mi>G</mi><mo>.</mo><mi>P</mi><mo>.</mo><mi> </mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mtd></mtr></mtable></mrow></mfenced></math>
<math><mo>⇒</mo><mfrac><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub><mfenced close=] open=[ separators=|><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfrac></mrow></mfenced></mrow><mrow><mfenced close=] open=[ separators=|><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>α</mi></mrow></mfrac></mrow></mfrac></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>0.8</mn><msub><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>⇒</mo><mfrac><mrow><mi>α</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>α</mi></mrow></mfrac><mo>=</mo><mn>0.8</mn><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>4</mn></math>

</details>

---

### Q9. JEE Advanced 2018 (Paper 2)

*Type:* `numerical` | *Level:* `2`

A ball is projected from the ground at an angle of <math><msup><mrow><mn>45</mn></mrow><mrow><mi>o</mi></mrow></msup></math> with the horizontal surface. It reaches a maximum height of <math><mn>120</mn><mi> m</mi></math> and returns to the ground. Upon hitting the ground for the first time, it loses half of its kinetic energy. Immediately after the bounce, the velocity of the ball makes an angle of <math><msup><mrow><mn>30</mn></mrow><mrow><mi>o</mi></mrow></msup></math> with the horizontal surface. The maximum height it reaches after the bounce (in meters) is _____________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/2f366f69-38b3-4c3c-9eed-b47d1f7fdd5c-image.png"/>
<math><msub><mrow><mi>H</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><msup><mrow><mi>u</mi></mrow><mrow><mn>2</mn></mrow></msup><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mrow> <msup> <mrow> <mn>45</mn></mrow> <mi>o</mi> </msup> </mrow></mrow></mrow></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac><mo>=</mo><mn>120</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mfrac><msup><mi>u</mi><mn>2</mn></msup><mrow><mn>4</mn><mi>g</mi></mrow></mfrac><mo>=</mo><mn>120</mn><mi> </mi><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math>
when half of kinetic energy is lost <math><mi>v</mi><mo>=</mo><mfrac><mrow><mi>u</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><msup><mfenced separators="|"><mfrac><mi>u</mi><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mo> </mo><mn>30</mn><mo>°</mo></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac><mo>=</mo><mfrac><msup><mi>u</mi><mn>2</mn></msup><mrow><mn>16</mn><mi>g</mi></mrow></mfrac><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math>
From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math>,
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mn>2</mn></msub><mo>=</mo><mfrac><msub><mi>H</mi><mn>1</mn></msub><mn>4</mn></mfrac><mo>=</mo><mn>30</mn><mi> </mi><mn>m</mn></math>

</details>

---

### Q10. JEE Advanced 2013 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

A particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is projected from the ground with an initial speed <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>u</mi><mo>&#8728;</mo></msub></math> at an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> with the horizontal. At the highest point of its trajectory, it makes a completely inelastic collision with another identical particle, which was thrown vertically upward from the ground with the same initial speed <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>u</mi><mo>&#8728;</mo></msub></math>. The angle that the composite system makes with the horizontal immediately after the collision is

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mi>&pi;</mi> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math><mrow>  <mfrac>    <mrow>      <mi>&pi;</mi>    </mrow>    <mrow>      <mn>2</mn>    </mrow>  </mfrac>  <mo>+</mo>  <mi>&alpha;</mi></mrow></math>
- **(C)** <math><mrow>  <mfrac>    <mrow>      <mi>&pi;</mi>    </mrow>    <mrow>      <mn>2</mn>    </mrow>  </mfrac>  <mo>-</mo>  <mi>&alpha;</mi></mrow></math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mi>&pi;</mi> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mfrac> <mrow> <mi>&pi;</mi> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

At the highest point

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ndehrydyswka.png">

\(v_{1}=\frac{u_{0} \cos \alpha}{2} \quad\) (by applying momentum conservation in horizontal direction)

\(\mathrm{v}_{2}=\frac{\mathrm{u}_{0} \cos \alpha}{2} \quad\) (by applying momentum conservation in vertical direction)

\(\theta=45^{\circ}\left(\mathrm{H}=\frac{\mathrm{u}_{0}^{2} \sin ^{2} \alpha}{2 \mathrm{~g}}\right)\)

</details>

---

### Q11. JEE Advanced 2012 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

A small block is connected to one end of a massless spring of un-stretched length $4.9 \mathrm{~m}$. The other end of the spring (see the figure) is fixed. The system lies on a horizontal frictionless surface. The block is stretched by $0.2 \mathrm{~m}$ and released from rest at $t=0$. It then executes simple harmonic motion with angular frequency $\omega=\pi / 3 \mathrm{rad} / \mathrm{s}$. Simultaneously at $t=0$, a small pebble is projected with speed $v$ form point $P$ at an angle of $45^{\circ}$ as shown in the figure. Point $P$ is at a horizontal distance of $10 \mathrm{~m}$ from $O$. If the pebble hits the block at $t=1 \mathrm{~s}$, the value of $v$ is (take $g$ $=10 \mathrm{~m} / \mathrm{s}^{2}$ )

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/8JfHbEDRw9CzUF3KhntqqOIXAPC3H9itqgYrnpnqqJI.original.fullsize.png">

**Options:**

- **(A)** $\sqrt{50} \mathrm{~m} / \mathrm{s}$
- **(B)** $\sqrt{51} \mathrm{~m} / \mathrm{s}$
- **(C)** $\sqrt{52} \mathrm{~m} / \mathrm{s}$
- **(D)** $\sqrt{53} \mathrm{~m} / \mathrm{s}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{50} \mathrm{~m} / \mathrm{s}$**

**Detailed Solution:**

Time of flight of projectile,

$T=\frac{2 V \sin \theta}{g}$

$\therefore \quad 1=\frac{2 V \sin 45^{\circ}}{g} \quad \therefore \quad V=\sqrt{50} \mathrm{~ms}^{-1}$

Hence pebble is projected with a speed $V=\sqrt{50} \mathrm{~ms}^{-1}$

</details>

---

### Q12. JEE Advanced 2011 (Paper 2)

*Type:* `numerical` | *Level:* `2`

A train is moving along a straight line with a constant acceleration a. A boy standing in the train throws a ball forward with a speed of $10 \mathrm{~m} / \mathrm{s}$, at an angle of $60^{\circ}$ to the horizontal. The boy has to move forward by $1.15 \mathrm{~m}$ inside the train to catch the ball back at the initial height. The acceleration of the train in $\mathrm{m} / \mathrm{s}^2$, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$\begin{aligned} t & =T=\frac{2 u \sin \theta}{g} \\ & =\frac{2 \times 10 \times \sin 60^{\circ}}{10}=\sqrt{3} \mathrm{~s}\end{aligned}$
Displacement of train in time $t=\frac{1}{2} a t^2$
Displacement of boy with respect to train
$$
=1.15 \mathrm{~m}
$$
$\therefore$ Displacement of boy with respect to ground $=\left(1.15+\frac{1}{2} a t^2\right)$
Displacement of ball with respect to ground $=\left(u \cos 60^{\circ}\right) t$
To catch the ball back at initial height,
$$
\begin{aligned}
1.15+\frac{1}{2} a t^2 & =\left(u \cos 60^{\circ}\right) t \\
\therefore 1.15+\frac{1}{2} a(\sqrt{3})^2 & =10 \times \frac{1}{2} \times \sqrt{3}
\end{aligned}
$$
Solving this equation, we get
$$
a=5 \mathrm{~ms}^{-2}
$$
$\therefore$ Answer is 5 .
Analysis of Question
(i) Question is moderately tough.
(ii) Velocity of ball given in the question is with respect to ground.

</details>

---

