# JEE Advanced Physics - Rotational Motion

## Topic 6: Rolling without Slipping

**Total Questions:** 9

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

A solid cylinder of radius $R$ rolls without slipping with a center of mass speed $v_0 = \sqrt{\dfrac{gR}{3}}$ on a horizontal surface with a vertical edge, as shown in the figure. Here, $g$ is the acceleration due to the gravity. At the moment when the cylinder loses contact with the surface due to rotation around the corner, the speed of its center of mass is:

<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p1_english__q19_d1.png" />

**Options:**

- **(A)** $0$
- **(B)** $\sqrt{\dfrac{5gR}{7}}$
- **(C)** $\sqrt{\dfrac{gR}{15}}$
- **(D)** $\sqrt{\dfrac{3gR}{7}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{\dfrac{5gR}{7}}$**

**Detailed Solution:**

Let the mass of the cylinder be $m$ and its radius be $R$.

When the cylinder is rolling on the horizontal surface, its kinetic energy is:
$K_i = \dfrac{1}{2}mv_0^2 + \dfrac{1}{2}I_{cm}\omega_0^2$

Since it rolls without slipping, $\omega_0 = \dfrac{v_0}{R}$ and $I_{cm} = \dfrac{1}{2}mR^2$.
$K_i = \dfrac{1}{2}mv_0^2 + \dfrac{1}{2}\left(\dfrac{1}{2}mR^2\right)\left(\dfrac{v_0}{R}\right)^2 = \dfrac{3}{4}mv_0^2$

Given $v_0 = \sqrt{\dfrac{gR}{3}}$, we have $v_0^2 = \dfrac{gR}{3}$.
$K_i = \dfrac{3}{4}m\left(\dfrac{gR}{3}\right) = \dfrac{1}{4}mgR$

Let the corner be the reference level for potential energy. The initial total mechanical energy of the cylinder just as it reaches the corner is:
$E_i = K_i + U_i = \dfrac{1}{4}mgR + mgR = \dfrac{5}{4}mgR$

As the cylinder rotates around the corner, let $\theta$ be the angle the line connecting the corner to the center of mass makes with the vertical. Let $v$ be the speed of the center of mass at this angle.
The total mechanical energy at angle $\theta$ is:
$E_f = \dfrac{3}{4}mv^2 + mgR\cos\theta$

By conservation of mechanical energy, $E_i = E_f$:
$\dfrac{5}{4}mgR = \dfrac{3}{4}mv^2 + mgR\cos\theta$

The forces acting on the cylinder along the radial direction (towards the corner) are the component of gravity $mg\cos\theta$ and the normal force $N$. The equation of motion is:
$mg\cos\theta - N = \dfrac{mv^2}{R}$

The cylinder loses contact with the corner when the normal force becomes zero ($N = 0$):
$mg\cos\theta = \dfrac{mv^2}{R} \Rightarrow mgR\cos\theta = mv^2$

Substituting this into the energy conservation equation:
$\dfrac{5}{4}mgR = \dfrac{3}{4}mv^2 + mv^2$

$\dfrac{5}{4}mgR = \dfrac{7}{4}mv^2$

Solving for $v$:
$v^2 = \dfrac{5}{7}gR$

$v = \sqrt{\dfrac{5gR}{7}}$

Answer: $\sqrt{\dfrac{5gR}{7}}$

</details>

---

### Q2. JEE Advanced 2026 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider a large disk of radius $R$ and two smaller disks, each of radius $r = R/50$, lying on its circumference, as shown in the figure. The smaller disks are initially in contact with each other, with an angular separation $\Delta\theta$ between their centers. They are made to roll without slipping in opposite directions, with constant angular velocities $\omega$ and $2\omega$ while the large disk is held stationary. The time $\tau$ at which the smaller disks are again in contact is:
[Use $\sin(\Delta\theta) = \Delta\theta$ and ignore gravity.]

<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p1_english__q17_d1.png" />

**Options:**

- **(A)** $\tau = 51 \times \left(2\pi - \dfrac{4}{51}\right) / \omega$
- **(B)** $\tau = 51 \times \left(2\pi - \dfrac{2}{51}\right) / 3\omega$
- **(C)** $\tau = 51 \times \left(2\pi - \dfrac{4}{51}\right) / 3\omega$
- **(D)** $\tau = 51 \times \left(2\pi - \dfrac{2}{51}\right) / \omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\tau = 51 \times \left(2\pi - \dfrac{4}{51}\right) / 3\omega$**

**Detailed Solution:**

Let the radius of the large disk be $R$ and the radius of the small disks be $r$. We are given $r = R/50$, which implies $R = 50r$.

The centers of the small disks move along a circular path of radius $R + r = 50r + r = 51r$.

When the two small disks are in contact, the distance between their centers is $2r$. The angular separation $\Delta\theta$ between their centers is given by the arc length (which is approximately the chord length for small angles):
$(R + r)\Delta\theta = 2r$
$(51r)\Delta\theta = 2r \implies \Delta\theta = \dfrac{2}{51} \text{ rad}$

The small disks roll without slipping on the stationary large disk. For a disk of radius $r$ rolling with angular velocity $\omega$, the velocity of its center is $v = \omega r$.
The angular velocity of the center of the first small disk about the center of the large disk is:
$\Omega_1 = \dfrac{v_1}{R+r} = \dfrac{\omega r}{51r} = \dfrac{\omega}{51}$

Similarly, for the second small disk rolling with angular velocity $2\omega$, the angular velocity of its center is:
$\Omega_2 = \dfrac{v_2}{R+r} = \dfrac{2\omega r}{51r} = \dfrac{2\omega}{51}$

Since they move in opposite directions, their relative angular velocity is:
$\Omega_{\text{rel}} = \Omega_1 + \Omega_2 = \dfrac{\omega}{51} + \dfrac{2\omega}{51} = \dfrac{3\omega}{51}$

The disks are initially in contact, meaning their centers are separated by an angle $\Delta\theta$. They will be in contact again when their centers are once again separated by $\Delta\theta$ after crossing each other on the opposite side of the large disk. 
The total angular distance that the two centers must cover together is:
$\theta_{\text{total}} = 2\pi - 2\Delta\theta$

Substituting $\Delta\theta = \dfrac{2}{51}$:
$\theta_{\text{total}} = 2\pi - 2\left(\dfrac{2}{51}\right) = 2\pi - \dfrac{4}{51}$

The time $\tau$ taken for them to meet again is:
$\tau = \dfrac{\theta_{\text{total}}}{\Omega_{\text{rel}}} = \dfrac{2\pi - \dfrac{4}{51}}{\dfrac{3\omega}{51}}$

$\tau = \dfrac{51}{3\omega} \left(2\pi - \dfrac{4}{51}\right)$

Answer: $\tau = 51 \times \left(2\pi - \dfrac{4}{51}\right) / 3\omega$

</details>

---

### Q3. JEE Advanced 2022 (Paper 1)

*Type:* `numerical` | *Level:* `3`

<p>At time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math>, a disk of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> starts to roll without slipping on a horizontal plane with an angular acceleration of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>. A small stone is stuck to the disk. At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math>, it is at the contact point of the disk and the plane. Later, at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msqrt><mi>&#960;</mi></msqrt><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>, the stone detaches itself and flies off tangentially from the disk. The maximum height (in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi></math>) reached by the stone measured from the plane is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>x</mi><mn>10</mn></mfrac></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is [Take <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>.]</p><p>If the numerical value has more than two decimal places, truncate/round-off the value to TWO decimal places.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.52**

**Detailed Solution:**

<blockquote><p>Using second equation of motion,</p><p>The angle rotated by disc in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msqrt><mi>&#960;</mi></msqrt><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><msub><mi>&#969;</mi><mn>0</mn></msub><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>&#945;</mi><msup><mi>t</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mfenced><msqrt><mi>&#960;</mi></msqrt></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>&#160;</mo><mi>rad</mi></math></p><p>Now using first equation of motion, the angular velocity of disc is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><msub><mi>&#969;</mi><mn>0</mn></msub><mo>+</mo><mi>&#945;</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#969;</mi><mo>=</mo><mn>0</mn><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mi>&#960;</mi></msqrt></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mi>&#960;</mi></msqrt></mrow><mn>3</mn></mfrac><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>And, velocity of disk about centre of mass is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mi>cm</mi></msub><mo>=</mo><mi>&#969;</mi><mi>R</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mi>&#960;</mi></msqrt></mrow><mn>3</mn></mfrac><mo>&#215;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mi>&#960;</mi></msqrt></mrow><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p></blockquote><blockquote><p>At the moment the stone detaches, the situation is shown in figure below.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/4a070e6a-cb1a-4dee-b328-1e4a1a961b21-image.png" style="width: 340px; height: 135px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><msqrt><msup><mfenced><mrow><mi>&#969;</mi><mi>R</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msubsup><mi>v</mi><mi>cm</mi><mn>2</mn></msubsup><mo>+</mo><mn>2</mn><mfenced><mrow><mi>&#969;</mi><mi>R</mi></mrow></mfenced><msub><mi>v</mi><mi>cm</mi></msub><mi>cos</mi><mn>120</mn><mo>&#176;</mo></msqrt></math></p><p>Putting the values, we get </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mi>&#960;</mi></msqrt></mrow><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mi>&#969;</mi><mi>R</mi><mi>sin</mi><mn>120</mn><mo>&#176;</mo></mrow><mrow><msub><mi>v</mi><mi>cm</mi></msub><mo>+</mo><mi>&#969;</mi><mi>R</mi><mi>cos</mi><mn>120</mn><mo>&#176;</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mi>rad</mi></math></p><p>So, the maximum height reached by the stone is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mi>max</mi></msub><mo>=</mo><mfrac><mrow><msup><mi>v</mi><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced><mfrac><mrow><mn>2</mn><msqrt><mi>&#960;</mi></msqrt></mrow><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><mo>&#215;</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>60</mn><mo>&#176;</mo></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>10</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi><mo>&#215;</mo><mn>3</mn></mrow><mrow><mn>9</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>60</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p>So, height from ground will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>60</mn><mo>&#176;</mo></mrow></mfenced><mo>+</mo><mfrac><mi>&#960;</mi><mn>60</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>x</mi><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>52</mn></math></p></blockquote>

</details>

---

### Q4. JEE Advanced 2021 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

<p>A horizontal force <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math> is applied at the centre of mass of a cylindrical object of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>, perpendicular to its axis as shown in the figure. The coefficient of friction between the object and the ground is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi></math>. The centre of mass of the object has an acceleration <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>. The acceleration due to gravity is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math>. Given that the object rolls without slipping, which of the following statement(s) is (are) correct?</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/c40aaf47-970f-42c6-a45c-5b3be0c39e9a-image.png" style="width: 200px; height: 177px;" /></p>

**Options:**

- **(A)** For the same <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math>, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> does not depend on whether the cylinder is solid or hollow.
- **(B)** For a solid cylinder, the maximum possible value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#956;</mi><mi>g</mi></math>.
- **(C)** The magnitude of the frictional force on the object due to the ground is always <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mi>m</mi><mi>g</mi></math>.
- **(D)** For a thin-walled hollow cylinder, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mi>F</mi><mrow><mn>2</mn><mi>m</mi></mrow></mfrac></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) For a thin-walled hollow cylinder, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mi>F</mi><mrow><mn>2</mn><mi>m</mi></mrow></mfrac></math>.**

**Detailed Solution:**

<p>Let moment of inertia <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>I</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/f4eb0c6e-932c-407c-b3e4-d033856c2fa9-758f5244-8b39-44c0-b24d-ebcc14e0b238-image.png" style="width: 250px; height: 256px;" /></p><p>For pure rolling, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>&#945;</mi><mi>R</mi></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>&#8722;</mo><mi>f</mi><mo>=</mo><mi>m</mi><mi>a</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>R</mi><mo>=</mo><mi>I</mi><mi>&#945;</mi></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>R</mi><mo>=</mo><mfrac><mrow><mi>I</mi><mi>a</mi></mrow><mi>R</mi></mfrac></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>=</mo><mfrac><mrow><mi>I</mi><mi>a</mi></mrow><msup><mi>R</mi><mn>2</mn></msup></mfrac></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>&#8722;</mo><mfrac><mrow><mi>I</mi><mi>a</mi></mrow><msup><mi>R</mi><mn>2</mn></msup></mfrac><mo>=</mo><mi>m</mi><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>F</mi><mo>=</mo><mfenced><mrow><mi>m</mi><mo>+</mo><mfrac><mi>I</mi><msup><mi>R</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> For the same value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math>, value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> depends on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> For a solid cylinder<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>I</mi><mo>=</mo><mfrac><mrow><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mrow></mfenced></math> (to calculate maximum <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>=</mo><mi>&#956;</mi><mi>m</mi><mi>g</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#956;</mi><mi>m</mi><mi>g</mi><mo>=</mo><mfenced><mfrac><mrow><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mfenced><mo>&#215;</mo><mfrac><mi>a</mi><msup><mi>R</mi><mn>2</mn></msup></mfrac></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mi>&#956;</mi><mi>g</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi></math> is dependent on applied force.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> For thin-walled hollow cylinder<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>I</mi><mo>=</mo><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup></mrow></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mfenced><mrow><mi>m</mi><mo>+</mo><mfrac><mrow><mi>m</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><msup><mi>R</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>a</mi><mo>=</mo><mn>2</mn><mi>m</mi><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mfrac><mi>F</mi><mrow><mn>2</mn><mi>m</mi></mrow></mfrac></math> </p>

</details>

---

### Q5. JEE Advanced 2018 (Paper 1)

*Type:* `numerical` | *Level:* `1`

A ring and a disc are initially at rest, side by side, at the top of an inclined plane which makes an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>&#176;</mo></math> with the horizontal. They start to roll without slipping at the same instant of time along the shortest path. If the time difference between their reaching the ground is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>/</mo><msqrt><mn>10</mn></msqrt><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>, then the height of the top of the inclined plane (in meters) is __________. Take <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>=</mo><mn>10</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.75**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/9_solu_2.jpg"/>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>c</mi></msub><mo>=</mo><mfrac><mrow><mi>g</mi><mi>sin</mi><mtext>θ</mtext></mrow><mrow><mn>1</mn><mo>+</mo><mfrac><msub><mi>I</mi><mi>c</mi></msub><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">g</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>g</mi><mi>sin</mi><mtext>θ</mtext></mrow><mn>2</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">g</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mi>g</mi><mi>sin</mi><mtext>θ</mtext></mrow><mn>3</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>h</mi><mrow><mi>sin</mi><mtext>θ</mtext></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced separators="|"><mfrac><mrow><mi>g</mi><mi>sin</mi><mtext>θ</mtext></mrow><mn>2</mn></mfrac></mfenced><msubsup><mi>t</mi><mn>1</mn><mn>2</mn></msubsup><mo>⇒</mo><msub><mi>t</mi><mn>1</mn></msub><mo>=</mo><msqrt><mfrac><mrow><mn>4</mn><mi>h</mi></mrow><mrow><mi>g</mi><mi> </mi><msup><mi>sin</mi><mn>2</mn></msup><mtext>θ</mtext></mrow></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mrow><mn>16</mn><mi>h</mi></mrow><mrow><mn>3</mn><mi>g</mi></mrow></mfrac></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>h</mi><mrow><mi>sin</mi><mtext>θ</mtext></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced separators="|"><mfrac><mrow><mn>2</mn><mi>g</mi><mi>sin</mi><mtext>θ</mtext></mrow><mn>3</mn></mfrac></mfenced><msubsup><mi>t</mi><mn>2</mn><mn>2</mn></msubsup><mo>⇒</mo><msub><mi>t</mi><mn>2</mn></msub><mo>=</mo><msqrt><mfrac><mrow><mn>3</mn><mi>h</mi></mrow><mrow><mi>g</mi><mi> </mi><msup><mi>sin</mi><mn>2</mn></msup><mtext>θ</mtext></mrow></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mrow><mn>4</mn><mi>h</mi></mrow><mi>g</mi></mfrac></msqrt></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><msqrt><mfrac><mrow><mn>16</mn><mi>h</mi></mrow><mrow><mn>3</mn><mi>g</mi></mrow></mfrac></msqrt><mo>-</mo><msqrt><mfrac><mrow><mn>4</mn><mi>h</mi></mrow><mrow><mi>g</mi></mrow></mfrac></msqrt><mo>=</mo><mfrac><mrow><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mrow><msqrt><mn>10</mn></msqrt></mrow></mfrac></math>
<math><msqrt><mi>h</mi></msqrt><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>h</mi></msqrt><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><msqrt><mn>3</mn></msqrt></mrow><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced></mfrac><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>⇒</mo><mi>h</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mn>0.75</mn><mi> </mi><mi mathvariant="normal">m</mi></math>

</details>

---

### Q6. JEE Advanced 2012 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Two solid cylinders $P$ and $Q$ of same mass and same radius start rolling down a fixed inclined plane from the same height at the same time. Cylinder $P$ has most of its mass concentrated near its surface, while $Q$ has most of its mass concentrated near the axis. Which statement(s) is(are) correct?

**Options:**

- **(A)** Both cylinders $P$ and $Q$ reach the ground at the same time.
- **(B)** Cylinders $P$ has larger linear acceleration than cylinder $Q$.
- **(C)** Both cylinders reach the ground with same translational kinetic energy.
- **(D)** Cylinder $Q$ reaches the ground with larger angular speed.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Cylinder $Q$ reaches the ground with larger angular speed.**

**Detailed Solution:**

As we know, acceleration of the center of mass of cylinder rolling down an inclined plane

$a_{c}=\frac{g \sin \theta}{1+\frac{I}{M R^{2}}}$

In case of $P$ the mass is concentrated away from the axis, So $I_{P}>I_{Q}$

$\therefore \quad a_{P} < a_{Q} \Rightarrow v_{\mathrm{P}} < v_{\mathrm{Q}} \Rightarrow \omega_{\mathrm{P}} < \omega_{\mathrm{Q}}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ANENaTvUCAd2VYC6vCTFI7UrvJHtVD1BadiNHQTQ598.original.fullsize.png">

</details>

---

### Q7. JEE Advanced 2012 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

The figure shows a system consisting of (i) a ring of outer radius $3 R$ rolling clockwise without slipping on a horizontal surface with angular speed $\omega$ and (ii) an inner disc of radius $2 R$ rotating anti-clockwise with angular speed $\omega / 2$. The ring and disc are separated by frictionless ball bearings. The point $P$ on the inner disc is at a distance $R$ from the origin, where $O P$ makes an angle of $30^{\circ}$ with the horizontal. Then with respect to the horizontal surface,

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ge9QixmoxOpuMhx_qKFq8uhBUqr8BxjSA_VoLSc8lA0.original.fullsize.png">

**Options:**

- **(A)** the point $O$ has linear velocity $3 R \omega \hat{i}$
- **(B)** the point $P$ has linear velocity $\frac{11}{4} R \omega \hat{i}+\frac{\sqrt{3}}{4} R \omega \hat{k}$.
- **(C)** the point $P$ has linear velocity $\frac{13}{4} R \omega \hat{i}-\frac{\sqrt{3}}{4} R \omega \hat{k}$
- **(D)** the point $P$ has linear velocity

$\left(3-\frac{\sqrt{3}}{4}\right) R \omega \hat{i}+\frac{1}{4} R \omega \hat{k}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) the point $P$ has linear velocity $\frac{11}{4} R \omega \hat{i}+\frac{\sqrt{3}}{4} R \omega \hat{k}$.**

**Detailed Solution:**

Velocity at centre 'O' $\quad \therefore \quad \vec{v}_{o}=3 R \omega \hat{i}$

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/BTLX1MyJcyw68QSy9fxOwAPZRL8YvKBprcNEUT_hdtg.original.fullsize.png">


$\vec{V}_{P}=3 R \omega \hat{i}-\frac{R \omega}{2} \sin 30^{\circ} \hat{i}+\frac{R \omega}{2} \cos 30^{\circ} \hat{k}$

$\therefore \quad \vec{V}_{P}=\left[3 R_{\omega} \hat{i}-\frac{R_{\omega}}{4} \hat{i}\right]+\frac{\sqrt{3} R_{\omega}}{4} \hat{k}$

or, $\quad \vec{V}_{P}=\frac{11}{4} R_{\omega} \hat{i}+\frac{\sqrt{3}}{4} R_{\omega} \hat{k}$

</details>

---

### Q8. JEE Advanced 2008 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Statement 1 Two cylinders, one hollow (metal) and the other solid (wood) with the same mass and identical dimensions are simultaneously allowed to roll without slipping down an inclined plane from the same height. The hollow cylinder will reach the bottom of the inclined plane first.
and Statement 2 By the principle of conservation of energy, the total kinetic energies of both the cylinders are identical when they reach the bottom of the incline.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation for Statement 1.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation for Statement 1.
- **(C)** Statement 1 is true, Statement 2 is false.
- **(D)** Statement 1 is false, Statement 2 is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement 1 is false, Statement 2 is true**

**Detailed Solution:**

In case of pure rolling on inclined plane,
$$
\begin{aligned}
& a=\frac{g \sin \theta}{1+I / m R^2} \\
& I_{\text {solid }} < I_{\text {hollow }} \\
\therefore \quad & a_{\text {solid }}>a_{\text {hollow }}
\end{aligned}
$$
$\therefore$ solid cylinder will reach the bottom first.
Further, in case of pure rolling on stationary ground, work done by friction is zero. Therefore, mechanical energy of both the cylinders will remain constant.
$$
\begin{aligned}
& \therefore(\mathrm{KE})_{\text {Hollow }}=(\mathrm{KE})_{\text {solid }}=\text { decrease in } \mathrm{PE}=m g h \\
& \therefore \text { correct option is }(\mathrm{d})
\end{aligned}
$$

</details>

---

### Q9. JEE Advanced 2006

*Type:* `multipleCorrect` | *Level:* `2`

A solid sphere is in pure rolling motion on an inclined surface having inclination $\theta$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/SqpFTGNOh5r0Id1yrfTHMgHqm61n25jCGlaCyaWC2gQ.original.fullsize.png">

**Options:**

- **(A)** frictional force acting on sphere is $f=\mu m g \cos \theta$
- **(B)** $f$ is disspative force
- **(C)** friction will increase its angular velocity and decreases its linear velocity
- **(D)** If $\theta$ decreases, friction will decrease

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) If $\theta$ decreases, friction will decrease**

**Detailed Solution:**

In case of pure rolling,
$$
\begin{aligned}
& f=\frac{m g \sin \theta}{1+\frac{m R^2}{I}} \\
\therefore & f \propto \sin \theta
\end{aligned}
$$
(upwards)
Therefore, as $\theta$ decreases force of friction will also decrease.

</details>

---

