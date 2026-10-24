# JEE Advanced Physics - Electrostatics

## Topic 4: Electric Dipole

**Total Questions:** 6

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

Consider an electric dipole comprising two charges $+q$ and $-q$ each with mass $m$, separated by a fixed distance $d$ and initially at rest with its dipole moment pointing along $\hat{i}$. A uniform electric field $E\hat{j}$ is turned on at time $t = 0$ and it is turned off at $t = t_f$, when the dipole moment makes an angle $\theta_f$ with $\hat{i}$. Neglecting any sources of energy loss, correct option(s) is/are:

**Options:**

- **(A)** The center of mass of the dipole is deflected towards $\hat{j}$ in the presence of the field.
- **(B)** If the magnitude of the final angular velocity $\omega_f = \sqrt{\dfrac{2qE}{md}}$, then $\theta_f = \dfrac{\pi}{6}$.
- **(C)** If $\theta_f = \pi/3$, then the change in kinetic energy of the dipole is given by $2\sqrt{3}\, qEd$.
- **(D)** For $\theta_f = \pi/4$, the dipole rotates around its center of mass with a constant angular velocity after $t > t_f$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) For $\theta_f = \pi/4$, the dipole rotates around its center of mass with a constant angular velocity after $t > t_f$.**

**Detailed Solution:**

The net force on the dipole in a uniform electric field is zero, as the forces on the two charges are equal and opposite ($qE\hat{j}$ and $-qE\hat{j}$). Therefore, the center of mass remains at rest and is not deflected. Option (A) is incorrect.

The moment of inertia of the dipole about its center of mass is $I = m\left(\dfrac{d}{2}\right)^2 + m\left(\dfrac{d}{2}\right)^2 = \dfrac{md^2}{2}$.

The torque on the dipole is $\vec{\tau} = \vec{p} \times \vec{E}$. The angle between the dipole moment $\vec{p}$ and the electric field $\vec{E}$ is $90^{\circ} - \theta$. The magnitude of the torque is $\tau = pE \sin(90^{\circ} - \theta) = qdE \cos\theta$.

The work done by the electric field as the dipole rotates from $\theta = 0$ to $\theta = \theta_f$ is equal to the change in kinetic energy:

$\Delta K = \int_{0}^{\theta_f} \tau d\theta = \int_{0}^{\theta_f} qdE \cos\theta d\theta = qdE \sin\theta_f$

Equating this to the final kinetic energy $\dfrac{1}{2}I\omega_f^2$:

$\dfrac{1}{2} \left(\dfrac{md^2}{2}\right) \omega_f^2 = qdE \sin\theta_f$

$\dfrac{md^2}{4} \omega_f^2 = qdE \sin\theta_f$

For option (B), substituting $\omega_f = \sqrt{\dfrac{2qE}{md}}$:

$\dfrac{md^2}{4} \left(\dfrac{2qE}{md}\right) = qdE \sin\theta_f$

$\dfrac{qdE}{2} = qdE \sin\theta_f \Rightarrow \sin\theta_f = \dfrac{1}{2} \Rightarrow \theta_f = \dfrac{\pi}{6}$

Thus, option (B) is correct.

For option (C), if $\theta_f = \dfrac{\pi}{3}$, the change in kinetic energy is $\Delta K = qdE \sin\left(\dfrac{\pi}{3}\right) = \dfrac{\sqrt{3}}{2} qEd$. Thus, option (C) is incorrect.

For option (D), after $t > t_f$, the electric field is turned off. The net torque on the dipole becomes zero. By Newton's first law of rotational motion, the dipole will continue to rotate about its center of mass with a constant angular velocity. Thus, option (D) is correct.

Answer: If the magnitude of the final angular velocity $\omega_f = \sqrt{\dfrac{2qE}{md}}$, then $\theta_f = \dfrac{\pi}{6}$.; For $\theta_f = \pi/4$, the dipole rotates around its center of mass with a constant angular velocity after $t > t_f$.

</details>

---

### Q2. JEE Advanced 2025 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

List-I shows four configurations, each consisting of a pair of ideal electric dipoles. Each dipole has a dipole moment of magnitude $p$, oriented as marked by arrows in the figures. In all the configurations the dipoles are fixed such that they are at a distance $2 r$ apart along the $x$ direction. The midpoint of the line joining the two dipoles is $X$. The possible resultant electric fields $\vec{E}$ at $X$ are given in List-II. Choose the option that describes the correct match between the entries in List-I to those in List-II.
 <table> <thead> <tr> <th> </th> <th>List-I </th> <th> </th> <th>List-II </th> </tr> </thead> <tbody> <tr> <td>$(P)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/_2cIggLI2-IuOeux5D4klfIqr_eo9OBw20sgpi5AZH4.original.fullsize.png">
 </td> <td>$(1)$ </td> <td>$\vec{E}=0$ </td> </tr> <tr> <td>$(Q)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ES3Bt0P-QD7ujpHXRFs1NJpliZN0IqgrajtKYYkJbfc.original.fullsize.png">
 </td> <td>$(2)$ </td> <td>$\vec{E}=-\frac{p}{2 \pi \epsilon_0 \mathrm{r}^3} \hat{\mathrm{j}}$ </td> </tr> <tr> <td>$(R)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/blH3NHLZI1I1aaMPF3b2lQXvgZG4NQqtLTat_UVFlKU.original.fullsize.png">
 </td> <td>$(3)$ </td> <td>$\vec{E}=-\frac{p}{4 \pi \epsilon_0 \mathrm{r}^3}(\hat{\mathrm{i}}-\hat{\mathrm{j}})$ </td> </tr> <tr> <td> </td> <td> </td> <td> </td> <td> </td> </tr> <tr> <td>$(S)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/TbENVbQd8EnD3iL9JJAP7dC66Zo9EqezZWek71rJMZg.original.fullsize.png">
 </td> <td>$(4)$ </td> <td>$\vec{E}=\frac{p}{4 \pi \epsilon_0 \mathrm{r}^3}(2 \hat{\mathrm{i}}-\hat{\mathrm{j}})$ </td> </tr> <tr> <td> </td> <td> </td> <td>$(5)$ </td> <td>$\vec{E}=\frac{p}{\pi \epsilon_0 \mathrm{r}^3} \hat{\mathrm{i}}$ </td> </tr> </tbody> </table>

**Options:**

- **(A)** $\mathrm{P} \rightarrow 3, \mathrm{Q} \rightarrow 1, \mathrm{R} \rightarrow 2, \mathrm{~S} \rightarrow 4$
- **(B)** $\mathrm{P} \rightarrow 4, \mathrm{Q} \rightarrow 5, \mathrm{R} \rightarrow 3, \mathrm{~S} \rightarrow 1$
- **(C)** $\mathrm{P} \rightarrow 2, \mathrm{Q} \rightarrow 1, \mathrm{R} \rightarrow 4, \mathrm{~S} \rightarrow 5$
- **(D)** $\mathrm{P} \rightarrow 2, \mathrm{Q} \rightarrow 1, \mathrm{R} \rightarrow 3, \mathrm{~S} \rightarrow 5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{P} \rightarrow 2, \mathrm{Q} \rightarrow 1, \mathrm{R} \rightarrow 4, \mathrm{~S} \rightarrow 5$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/YvKfujV6Iu_JmlDZPnbKQEnopaiAFGIYjOBh4hbCWkk.original.fullsize.png">
 $E_{\text {net }}=\frac{-2 k P}{r^3} \hat{j}$
$E_{n e t}=\frac{-P \hat{j}}{2 \pi \epsilon_0 r^3}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/AxLlo7UZc1nUX42p2CiZq-mK8k9jPhRklw2yU1WKBq8.original.fullsize.png">
 $\mathrm{E}_{\mathrm{net}}=0$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/NKo3gWwQcxYfwdhigujjm6glBc6HwvqGjukDB3MyBWs.original.fullsize.png">
 $\frac{2 \mathrm{P} \hat{\mathrm{i}}}{4 \pi \epsilon_0 \mathrm{r}^3}-\frac{\mathrm{P} \hat{\mathrm{j}}}{4 \pi \epsilon_0 \mathrm{r}^3}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/lfeHbfnFoG3v3YYlhBEVCIcbsoGFmzKNn-7hrPKMMK0.original.fullsize.png">
 $\mathrm{E}_{\mathrm{net}}=\frac{4 \mathrm{kP} \hat{\mathrm{i}}}{\mathrm{r}^3}$
$\mathrm{P} \rightarrow 2, \mathrm{Q} \rightarrow 1, \mathrm{R} \rightarrow 4, \mathrm{~S} \rightarrow 5$
Ans. (C)

</details>

---

### Q3. JEE Advanced 2024 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

A small electric dipole $\vec{p}_0$, having a moment of inertia $I$ about its center, is kept at a distance $r$ from the center of a spherical shell of radius $R$. The surface charge density $\sigma$ is uniformly distributed on the spherical shell. The dipole is initially oriented at a small angle $\theta$ as shown in the figure. While staying at a distance $r$, the dipole is free to rotate about its center.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/jT2AlT4J8eWJWe2ONqy4elc8YpmyqX8H_uzdsxnX9i4.original.fullsize.png">
If released from rest, then which of the following statement(s) is(are) correct?
[ $\varepsilon_0$ is the permittivity of free space.]

**Options:**

- **(A)** The dipole will undergo small oscillations at any finite value of $r$.
- **(B)** The dipole will undergo small oscillations at any finite value of $r>R$.
- **(C)** The dipole will undergo small oscillations with an angular frequency of $\sqrt{\frac{2 \sigma p_0}{\epsilon_0 I}}$ at $r=2 R$.
- **(D)** The dipole will undergo small oscillations with an angular frequency of $\sqrt{\frac{\sigma p_0}{100 \epsilon_0 I}}$ at $r=10 R$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The dipole will undergo small oscillations with an angular frequency of $\sqrt{\frac{\sigma p_0}{100 \epsilon_0 I}}$ at $r=10 R$.**

**Detailed Solution:**

<img src="images/dfe7ry346r3rsjhd_34dc.png">
\(\begin{aligned}
& \tau=|\vec{p} \times \vec{E}| \\
& I \alpha=p_0 E \sin \theta \\
& \alpha=\frac{p \cdot \theta}{I}\left(\frac{1}{4 \pi \varepsilon_0} \frac{\sigma 4 \pi R^2}{r^2}\right) \\
& \alpha=\left(\frac{p 0 \sigma R^2}{I \varepsilon_0 r^2}\right) \cdot \theta \\
& \therefore \omega=\sqrt{\frac{p 0 \sigma R^2}{I \varepsilon_0 r^2}}
\end{aligned}\)
For \(r=2 R\)
\(\omega=\sqrt{\frac{p_0 \sigma}{4 / \varepsilon_0}} \quad(\mathrm{C}\) is incorrect \()\)
Also, for \(r=10 R\)
\(\omega=\sqrt{\frac{p_0 \sigma}{4 l(100)}}\) (D is correct)
It will oscillate for any finite value of \(r>R\). (B is correct)

</details>

---

### Q4. JEE Advanced 2023 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>An electric dipole is formed by two charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>q</mi></math> located in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi></math>-plane at <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>)</mo><mo>&#160;</mo><mi>mm</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#8722;</mo><mn>2</mn><mo>)</mo><mo>&#160;</mo><mi>mm</mi></math>, respectively, as shown in the figure. The electric potential at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mn>100</mn><mo>,</mo><mo>&#160;</mo><mn>100</mn><mo>)</mo><mo>&#160;</mo><mi>mm</mi></math> due to the dipole is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>0</mn></msub></math>. The charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8211;</mo><mi>q</mi></math> are then moved to the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>&#8722;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>)</mo><mo>&#160;</mo><mi>mm</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#8722;</mo><mn>2</mn><mo>)</mo><mo>&#160;</mo><mi>mm</mi></math>, respectively. What is the value of electric potential at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> due to the new dipole?</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/89918752-cf37-4a23-9c23-ac6df765182c.png" style="width: 400px; height: 273px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>V</mi><mn>0</mn></msub><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>V</mi><mn>0</mn></msub><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>V</mi><mn>0</mn></msub><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msub><mi>V</mi><mn>0</mn></msub></mrow><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>V</mi><mn>0</mn></msub><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Electric potential at any general point for vertical dipole is written as, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>1</mn></msub><mo>&#8733;</mo><mfrac><mrow><msub><mi>p</mi><mn>1</mn></msub><mi>cos</mi><msub><mi>&#952;</mi><mn>1</mn></msub></mrow><msup><mfenced><msub><mi>r</mi><mn>1</mn></msub></mfenced><mn>2</mn></msup></mfrac></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/85ff45a7-efa9-4056-a857-b2998fb2085c.png" style="width: 300px; height: 215px;" /></p><p>Electric potential at any general point for <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>2</mn></msub><mo>&#8733;</mo><mfrac><mrow><msub><mi>p</mi><mn>2</mn></msub><mi>cos</mi><msub><mi>&#952;</mi><mn>2</mn></msub></mrow><msup><mfenced><msub><mi>r</mi><mn>2</mn></msub></mfenced><mn>2</mn></msup></mfrac></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/1845199e-0210-4c83-a0dd-d7eaabaa82ec.png" style="width: 300px; height: 219px;" /></p><p>For first case: </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><msub><mi>&#952;</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>100</mn><mn>100</mn></mfrac><mo>=</mo><mn>1</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>&#952;</mi><mn>1</mn></msub><mo>=</mo><mn>45</mn><mo>&#176;</mo></math></p><p>For second case:</p><p>slope in this is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>2</mn></mrow><mrow><mn>1</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>which is equal to </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mrow><mn>45</mn><mo>&#176;</mo><mo>+</mo><msub><mi>&#952;</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><msub><mi>&#952;</mi><mn>2</mn></msub></mrow><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><msub><mi>&#952;</mi><mn>2</mn></msub></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mn>1</mn><mo>+</mo><mi>tan</mi><msub><mi>&#952;</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>tan</mi><msub><mi>&#952;</mi><mn>2</mn></msub><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>tan</mi><msub><mi>&#952;</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn><mspace linebreak="newline"></mspace><mi>cos</mi><msub><mi>&#952;</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><msqrt><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac></math></p><p>also <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><msub><mi>r</mi><mn>2</mn></msub></math>.</p><p>Therefore, required ratio</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>V</mi><mn>2</mn></msub><msub><mi>V</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><msub><mi>p</mi><mn>2</mn></msub><mi>cos</mi><msub><mi>&#952;</mi><mn>2</mn></msub></mrow><mrow><msub><mi>p</mi><mn>1</mn></msub><mi>cos</mi><msub><mi>&#952;</mi><mn>1</mn></msub></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>V</mi><mn>2</mn></msub><msub><mi>V</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mi>q</mi><msub><mi>l</mi><mn>2</mn></msub><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac></mstyle></mrow><mrow><mi>q</mi><msub><mi>l</mi><mn>1</mn></msub><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mstyle></mrow></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><msqrt><msup><mfenced><mrow><mn>2</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mrow><mn>4</mn><mo>&#215;</mo><msqrt><mn>5</mn></msqrt></mrow></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>5</mn></msqrt></mrow><mrow><mn>4</mn><mo>&#215;</mo><msqrt><mn>5</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>V</mi><mn>2</mn></msub><mo>=</mo><mfrac><msub><mi>V</mi><mn>0</mn></msub><mn>2</mn></mfrac></math></p></blockquote>

</details>

---

### Q5. JEE Advanced 2020 (Paper 1)

*Type:* `numerical` | *Level:* `3`

One end of a spring of negligible unstretched length and spring constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is fixed at the origin <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo> </mo><mn>0</mn><mo>)</mo></math>. A point particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> carrying a positive charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> is attached at its other end. The entire system is kept on a smooth horizontal surface. When a point dipole <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>p</mi><mo>→</mo></mover></math> pointing towards the charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> is fixed at the origin, the spring gets stretched to a length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> and attains a new equilibrium position (see figure below). If the point mass is now displaced slightly by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Δ</mi><mi>l</mi><mo>≪</mo><mi>l</mi></math> from its equilibrium position and released, it is found to oscillate at frequency <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>δ</mi></mfrac><msqrt><mfrac><mi>k</mi><mi>m</mi></mfrac></msqrt><mo>,</mo></math> The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>δ</mi></math> is _______.

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/93216289-136e-4a1a-9124-1e84bb6cd65a-image.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3.14**

**Detailed Solution:**

<p>Original frequency <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>π</mi></mrow></mfrac><msqrt><mfrac><mi>k</mi><mi>m</mi></mfrac></msqrt></math></p><p>If dipole appears,</p><p>At equilibrium</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>K</mi><mi>p</mi></mrow><msup><mfenced><mrow><mi>ℓ</mi><mo>+</mo><msub><mi mathvariant="normal">x</mi><mn>0</mn></msub></mrow></mfenced><mn>3</mn></msup></mfrac><mo>·</mo><mi mathvariant="normal">q</mi><mo>=</mo><mi>k</mi><msub><mi>x</mi><mn>0</mn></msub><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/9b4240e6-b0f6-4647-b163-a89b55608978-image.png"/></p><p>Now disturbed</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>K</mi><mi>p</mi></mrow><msup><mfenced><mrow><mi>ℓ</mi><mo>+</mo><msub><mi>x</mi><mn>0</mn></msub><mo>+</mo><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mfrac><mo>·</mo><mi>q</mi><mo>-</mo><mi>k</mi><mfenced><mrow><msub><mi>x</mi><mn>0</mn></msub><mo>+</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>m</mi><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>m</mi><mi>a</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>K</mi><mi>pq</mi></mrow><msup><mfenced><mrow><mi>ℓ</mi><mo>+</mo><msub><mi mathvariant="normal">x</mi><mn>0</mn></msub></mrow></mfenced><mn>3</mn></msup></mfrac><msup><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mrow><mi>ℓ</mi><mo>+</mo><msub><mi mathvariant="normal">x</mi><mn>0</mn></msub></mrow></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>-</mo><mi>k</mi><mfenced><mrow><msub><mi>x</mi><mn>0</mn></msub><mo>+</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>m</mi><mi>a</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>K</mi><mi>p</mi><mi>q</mi></mrow><msup><mfenced><mrow><mi>ℓ</mi><mo>+</mo><msub><mi>x</mi><mn>0</mn></msub></mrow></mfenced><mn>3</mn></msup></mfrac><msup><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mrow><mi>ℓ</mi><mo>+</mo><msub><mi>x</mi><mn>0</mn></msub></mrow></mfrac></mrow></mfenced><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>-</mo><mi>k</mi><mfenced><mrow><msub><mi>x</mi><mn>0</mn></msub><mo>+</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mrow><mn>6</mn><mi>K</mi><mi>p</mi><mi>q</mi><mi>x</mi></mrow><msup><mfenced><mrow><mi>ℓ</mi><mo>+</mo><msub><mi>x</mi><mn>0</mn></msub></mrow></mfenced><mn>4</mn></msup></mfrac><mo>-</mo><mi>k</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mrow><mi>ℓ</mi><mo>+</mo><msub><mi>x</mi><mn>0</mn></msub></mrow></mfrac><mi>k</mi><msub><mi>x</mi><mn>0</mn></msub><mo>-</mo><mi>k</mi><mi>x</mi><mo>=</mo><mo>-</mo><mi>k</mi><mi>x</mi><mfenced close="]" open="["><mrow><mfrac><mrow><mn>3</mn><msub><mi>x</mi><mn>0</mn></msub></mrow><mrow><mi>ℓ</mi><mo>+</mo><msub><mi>x</mi><mn>0</mn></msub></mrow></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>As<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ℓ</mi></math> is negative,   </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>a</mi><mo>=</mo><mo>-</mo><mn>4</mn><mi>k</mi><mi>x</mi></math>;   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mi>k</mi></mrow><mi>m</mi></mfrac><mi>x</mi></math></p><p>New frequency :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>π</mi></mrow></mfrac><msqrt><mfrac><mrow><mn>4</mn><mi mathvariant="normal">k</mi></mrow><mi mathvariant="normal">m</mi></mfrac></msqrt><mo>=</mo><mn>2</mn><mi mathvariant="normal">f</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mi>δ</mi></mfrac><msqrt><mfrac><mi mathvariant="normal">k</mi><mi mathvariant="normal">m</mi></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mo>  </mo><mi>δ</mi><mo>=</mo><mi>π</mi><mo>=</mo><mn>3</mn><mo>.</mo><mn>14</mn></math></p>

</details>

---

### Q6. JEE Advanced 2019 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

<p>An electric dipole with dipole moment <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">p</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac><mfenced separators="|"><mrow><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover></mrow></mfenced></math> is held fixed at the origin <math><mi mathvariant="normal">O</mi></math> in the presence of an uniform electric field of magnitude <math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>.</mo></math> If the potential is constant on a circle of radius <math><mi mathvariant="normal">R</mi></math> centered at the origin as shown in figure, then the correct statement(s) is/are:
( <math><msub><mrow><mi mathvariant="normal">ε</mi></mrow><mrow><mn>0</mn></mrow></msub></math> is permittivity of free space, <math><mi mathvariant="normal">R</mi><mo>></mo><mo>></mo></math> dipole size)
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/e13da0a4-4139-41ae-8cad-448f8af18f55-image8.png"/></p>

**Options:**

- **(A)** <math><mi mathvariant="normal">R</mi><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi mathvariant="normal">p</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>4</mn><mi mathvariant="normal">π</mi><msub><mrow><mi mathvariant="normal">ε</mi></mrow><mrow><mn>0</mn></mrow></msub><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>
- **(B)** The magnitude of total electric field on any two points of the circle will be same
- **(C)** Total electric field at point <math><mi mathvariant="normal">A</mi></math> is <math><msub><mrow><mover accent="true"><mrow><mi mathvariant="normal">E</mi></mrow><mo>→</mo></mover></mrow><mrow><mi mathvariant="normal">A</mi></mrow></msub><mo>=</mo><msqrt><mn>2</mn></msqrt><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover></mrow></mfenced></math>
- **(D)** Total electric field at point <math><mi mathvariant="normal">B</mi></math> is <math><msub><mrow><mover accent="true"><mrow><mi mathvariant="normal">E</mi></mrow><mo>→</mo></mover></mrow><mrow><mi mathvariant="normal">B</mi></mrow></msub><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Total electric field at point <math><mi mathvariant="normal">B</mi></math> is <math><msub><mrow><mover accent="true"><mrow><mi mathvariant="normal">E</mi></mrow><mo>→</mo></mover></mrow><mrow><mi mathvariant="normal">B</mi></mrow></msub><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/bbb08a86-78d9-4af3-99ac-62878725314e-image9.png"/> 
Radius of circle, <math><mi>R</mi><mo>≫</mo></math> dipole size 
As, circle is equipotential 
So, <math><msub><mrow><mi>E</mi></mrow><mrow><mi mathvariant="normal">n</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">t</mi></mrow></msub></math> should be <math><mo>⊥</mo></math> to surface, so <math><mfrac><mrow><mi>k</mi><msub><mrow><mi>p</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>=</mo><msub><mrow><mi>E</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>⇒</mo><mi>r</mi><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>k</mi><msub><mrow><mi>p</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msub><mrow><mi>E</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>3</mn></mrow></mrow></mrow></msup><mo>⇒</mo><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced></math> is correct 
At point <math><mi>B</mi></math> net electric field will be zero. 
<math><msub><mrow><mi>E</mi></mrow><mrow><mi>B</mi></mrow></msub><mo>=</mo><mn>0</mn></math> 
<math><msub><mrow><mfenced separators="|"><mrow><msub><mrow><mi>E</mi></mrow><mrow><mi>A</mi></mrow></msub></mrow></mfenced></mrow><mrow><mi mathvariant="normal">N</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">t</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi><msub><mrow><mi>p</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>+</mo><msub><mrow><mi>E</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>3</mn><msub><mrow><mi>E</mi></mrow><mrow><mn>0</mn></mrow></msub></math> 
Electric field at point <math><mi>A</mi><mo>,</mo><mi> </mi><msub><mrow><mover accent="true"><mrow><mi>E</mi></mrow><mo>→</mo></mover></mrow><mrow><mi>A</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac><msub><mrow><mi>E</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced close="]" open="[" separators="|"><mrow><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>⇒</mo><mfenced separators="|"><mrow><mi>C</mi></mrow></mfenced></math> is incorrect 
<math><msub><mrow><mfenced separators="|"><mrow><msub><mrow><mi>E</mi></mrow><mrow><mi>B</mi></mrow></msub></mrow></mfenced></mrow><mrow><mi mathvariant="normal">N</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">t</mi></mrow></msub><mo>=</mo><mn>0</mn><mo>⇒</mo><mfenced separators="|"><mrow><mi>D</mi></mrow></mfenced></math> is correct

</details>

---

