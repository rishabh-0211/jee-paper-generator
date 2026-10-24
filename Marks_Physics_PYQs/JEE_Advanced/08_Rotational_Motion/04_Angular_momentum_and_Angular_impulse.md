# JEE Advanced Physics - Rotational Motion

## Topic 4: Angular momentum and Angular impulse

**Total Questions:** 15

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `3`

<strong>Passage:</strong> A uniform circular disk of radius $0.2$ m and mass $1$ kg is pivoted at its top point $C$ such that it can rotate freely around $C$ in the $XY$ plane, as shown in the figure. Initially, when the disk is at rest, a particle of mass $20$ g, travelling along negative $x$ direction in the $XY$ plane with speed $100$ ms$^{-1}$, hits the circumference of the disk at a point $P$. After collision the particle moves along negative $y$ direction at a speed of $90$ ms$^{-1}$.
[Given: the acceleration due to gravity $(g) = -10\hat{j}$ ms$^{-2}$]
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p2_english__q35_d1.png" />

<strong>Question:</strong> After the collision the disk starts to rotate around point $C$ in the $XY$ plane. The maximum change in the height (in m) of its center $O$ is:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.15**

**Detailed Solution:**

Moment of inertia of the disk about the pivot $C$ is $I_C = \dfrac{1}{2}MR^2 + MR^2 = \dfrac{3}{2}MR^2$.

Substituting $M = 1$ kg and $R = 0.2$ m, we get $I_C = \dfrac{3}{2}(1)(0.2)^2 = 0.06$ kg m$^2$.

The initial angular momentum of the particle about $C$ is $L_i = m u y_{\perp}$, where $y_{\perp}$ is the perpendicular distance from $C$ to the initial line of motion.

$L_i = m u (R + R\cos 45^\circ) = (0.02)(100)(0.2)\left(1 + \dfrac{1}{\sqrt{2}}\right) = 0.4 + 0.2\sqrt{2}$ kg m$^2$/s.

This initial angular momentum is in the clockwise direction.

The final angular momentum of the particle about $C$ is $L_f = m v x_{\perp}$, where $x_{\perp}$ is the perpendicular distance from $C$ to the final line of motion.

$L_f = m v (R\sin 45^\circ) = (0.02)(90)(0.2)\left(\dfrac{1}{\sqrt{2}}\right) = 0.18\sqrt{2}$ kg m$^2$/s.

This final angular momentum is also in the clockwise direction.

By conservation of angular momentum about $C$ during the collision, $L_i = L_f + I_C \omega$, where $\omega$ is the angular velocity of the disk just after the collision.

$0.4 + 0.2\sqrt{2} = 0.18\sqrt{2} + 0.06 \omega$

$0.06 \omega = 0.4 + 0.02\sqrt{2}$

$\omega = \dfrac{40 + 2\sqrt{2}}{6} = \dfrac{20 + \sqrt{2}}{3}$ rad/s.

Applying conservation of mechanical energy for the disk to find the maximum change in height $h$ of its center $O$:

$\dfrac{1}{2}I_C \omega^2 = M g h$

$h = \dfrac{I_C \omega^2}{2 M g} = \dfrac{0.06}{2(1)(10)} \left(\dfrac{20 + \sqrt{2}}{3}\right)^2$

$h = 0.003 \left(\dfrac{400 + 40\sqrt{2} + 2}{9}\right)$

$h = \dfrac{3}{1000} \left(\dfrac{402 + 40\sqrt{2}}{9}\right)$

$h = \dfrac{402 + 40\sqrt{2}}{3000} = \dfrac{201 + 20\sqrt{2}}{1500}$ = 0.15

</details>

---

### Q2. JEE Advanced 2024 (Paper 1)

*Type:* `numerical` | *Level:* `3`

A thin uniform rod of length $L$ and certain mass is kept on a frictionless horizontal table with a massless string of length $L$ fixed to one end (top view is shown in the figure). The other end of the string is pivoted to a point $\mathrm{O}$. If a horizontal impulse $P$ is imparted to the rod at a distance $x=L / n$ from the mid-point of the rod (see figure), then the rod and string revolve together around the point $\mathrm{O}$, with the rod remaining aligned with the string. In such a case, the value of $n$ is _______ .
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/58icvqNDammKb94DrMYGUGG9YOXHPcDwocJ5MVvbvww.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

Linear impulse $\int F d t=\Delta$ momentum
$\begin{aligned} & =\mathrm{m}\left(\mathrm{V}_{\mathrm{cm}}-0\right) \\ & \mathrm{P}=\mathrm{m}\left(\omega \mathrm{r}_{\mathrm{cm}}\right) \\ & =\mathrm{m} \omega\left(\mathrm{L}+\frac{\mathrm{L}}{2}\right)\end{aligned}$
$\mathrm{P}=\mathrm{m} \omega\left(\frac{3 \mathrm{~L}}{2}\right)$   ...(i)
Angular impulse $\int \tau \mathrm{dt}=\Delta$ angular momentum
$\begin{aligned} & \int \mathrm{r} \times \mathrm{Fdt}=\Delta \mathrm{L} \\ & \begin{aligned} & \mathrm{r} \times \int \mathrm{Fdt}=\mathrm{I}(\omega-0), \text { and } \mathrm{I} \text { is moment of inertia about axis of rotation. } \\ & \begin{aligned} &\left(\mathrm{L}+\frac{\mathrm{L}}{2}+\mathrm{x}\right) \times \mathrm{P}=\left(\mathrm{I}_{\mathrm{cm}}+\mathrm{md}^2\right) \omega \\ &=\left(\frac{\mathrm{mL}^2}{12}+\mathrm{m}\left(\mathrm{L}+\frac{\mathrm{L}}{2}\right)^2\right) \omega\end{aligned} \\ &\left(\frac{3 \mathrm{~L}}{2}+\mathrm{x}\right) \mathrm{P}=\mathrm{mL}^2\left(\frac{1}{12}+\left(\frac{3}{2}\right)^2\right) \omega\end{aligned}\end{aligned}$
$\left(\frac{3 L}{2}+x\right) P=\mathrm{mL}^2\left(\frac{7}{3}\right) \omega$ ...(ii)
Divide eq.-(i) & (ii)
$\begin{aligned} & \left(\frac{3 L}{2}+x\right)=\frac{L\left(\frac{7}{3}\right)}{\left(\frac{3}{2}\right)} \\ & \frac{3 L}{2}+x=L\left(\frac{14}{9}\right) \\ & x=\frac{L}{18}\end{aligned}$

</details>

---

### Q3. JEE Advanced 2024 (Paper 1)

*Type:* `numerical` | *Level:* `2`

A disc of mass $M$ and radius $R$ is free to rotate about its vertical axis as shown in the figure. A battery operated motor of negligible mass is fixed to this disc at a point on its circumference. Another disc of the same mass $M$ and radius $R / 2$ is fixed to the motor's thin shaft. Initially, both the discs are at rest. The motor is switched on so that the smaller disc rotates at a uniform angular speed $\omega$. If the angular speed at which the large disc rotates is $\omega / n$, then the value of $n$ is ______ .
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/xtMcE37d2OKyPklTuyGADXrq8-L5iHP3oI9KpsTdCaY.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/_E90K8D7__9NOppKNuNvEd1Nl78b67Kp2o-79IsbTJ4.original.fullsize.png">
On applying conservation of angular momentum about axis of larger disc.
$\begin{aligned} & \frac{1}{2} \cdot \mathrm{M}\left(\frac{\mathrm{R}}{2}\right)^2 \cdot \omega-\mathrm{M}\left(\omega^{\prime} \mathrm{R}\right) \cdot \mathrm{R}-\frac{\mathrm{MR}^2}{2} \cdot \omega^{\prime}=0 \\ & \Rightarrow \frac{\omega}{8}=\frac{3 \omega^{\prime}}{2} \\ & \Rightarrow \omega^{\prime}=\frac{\omega}{12} \quad \text { Hence, } \mathrm{n}=12\end{aligned}$

</details>

---

### Q4. JEE Advanced 2023 (Paper 2)

*Type:* `numerical` | *Level:* `3`

<p>A thin circular coin of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>gm</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi>cm</mi></math> is initially in a horizontal <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi></math>-plane. The coin is tossed vertically up (<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>z</mi></math> direction) by applying an impulse of <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msqrt><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>-</mo><mi mathvariant="normal">s</mi></math> at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi>cm</mi></math> from its center. The coin spins about its diameter and moves along the <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>z</mi></math> direction. By the time the coin reaches back to its initial position, it completes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> rotations. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is _____.</p><p>[Given: The acceleration due to gravity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>&#8722;</mo><mn>2</mn></mrow></msup></math>]</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/6e04c60e-1993-4062-867a-1dc229e567c0.png" style="width: 400px; height: 199px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

<blockquote><p>By impulse <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo></math> momentum theorem:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>J</mi><mo>=</mo><mi>M</mi><msub><mi>V</mi><mrow><mi>C</mi><mi>M</mi></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>V</mi><mrow><mi>C</mi><mi>M</mi></mrow></msub><mo>=</mo><mfrac><mi>J</mi><mi>M</mi></mfrac><mo>=</mo><mfrac><msqrt><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mstyle></msqrt><mrow><mn>100</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>1000</mn></mfrac></mstyle></mrow></mfrac><mo>=</mo><msqrt><mn>2</mn><mi>&#960;</mi></msqrt><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> Total time of journey <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><msub><mi>V</mi><mrow><mi>C</mi><mi>M</mi></mrow></msub></mrow><mi>g</mi></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mn>2</mn><mi>g</mi></mfrac><mo>&#215;</mo><msqrt><mn>2</mn><mi>&#960;</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#8710;</mo><mi>t</mi><mo>=</mo><mfrac><msqrt><mn>2</mn><mi>&#960;</mi></msqrt><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">s</mi></math></p><p>Also, by angular impulse<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo></math> momentum theorem:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>J</mi><mo>&#215;</mo><mfrac><mi>R</mi><mn>2</mn></mfrac><mo>=</mo><mi>I</mi><mi>&#969;</mi><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>J</mi><mo>&#215;</mo><mfrac><mi>R</mi><mn>2</mn></mfrac><mo>=</mo><mfenced close="]" open="["><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></mfenced><mi>&#969;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#969;</mi><mo>=</mo><mfrac><mrow><mi>J</mi><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mi>R</mi><mn>2</mn></mfrac></mstyle></mrow><mstyle displaystyle="true"><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mi>J</mi><mrow><mi>M</mi><mi>R</mi></mrow></mfrac><mo>&#215;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><mfenced><mfrac><msqrt><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mstyle></msqrt><mn>100</mn></mfrac></mfenced></mstyle><mo>&#215;</mo><mn>2</mn></mrow><mrow><mfenced><mfrac><mn>5</mn><mn>1000</mn></mfrac></mfenced><mo>&#215;</mo><mfenced><mrow><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>100</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>150</mn><msqrt><mn>2</mn><mi>&#960;</mi></msqrt><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> Number of rotations <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>&#969;</mi><mo>&#8710;</mo><mi>t</mi></mrow><mrow><mn>2</mn><mi>&#960;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>150</mn><msqrt><mn>2</mn><mi>&#960;</mi></msqrt></mrow></mfenced><mo>&#215;</mo><mstyle displaystyle="true"><mfenced><mfrac><msqrt><mn>2</mn><mi>&#960;</mi></msqrt><mn>5</mn></mfrac></mfenced></mstyle></mrow><mrow><mn>2</mn><mi>&#960;</mi></mrow></mfrac><mo>=</mo><mn>30</mn></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>30</mn></math>.</p></blockquote>

</details>

---

### Q5. JEE Advanced 2023 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

<p>An annular disk of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math>, inner radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and outer radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> is placed on a horizontal surface with coefficient of friction <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi></math>, as shown in the figure. At some time, an impulse <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>J</mi><mn>0</mn></msub><mover><mi>x</mi><mo>&#8743;</mo></mover></math> is applied at a height <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math> above the center of the disk. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><msub><mi>h</mi><mi>m</mi></msub></math> then the disk rolls without slipping along the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis. Which of the following statement(s) is(are) correct?</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/a0315bc6-1fb8-4ce8-a034-ddcaf52e88b8.png" style="width: 400px; height: 170px;" /></p>

**Options:**

- **(A)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>&#8800;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8594;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msub><mi>h</mi><mi>m</mi></msub><mo>=</mo><mfrac><mi>b</mi><mn>2</mn></mfrac></math>
- **(B)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>&#8800;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8594;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><msub><mi>h</mi><mi>m</mi></msub><mo>=</mo><mi>b</mi></math>
- **(C)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><msub><mi>h</mi><mi>m</mi></msub></math>, the initial angular velocity does not depend on the inner radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>
- **(D)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><mn>0</mn></math>, the wheel always slides without rolling

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><mn>0</mn></math>, the wheel always slides without rolling**

**Detailed Solution:**

<p>As we know, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>J</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>&#8710;</mo><mover><mi>P</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>J</mi><mn>0</mn></msub><mo>=</mo><mi>M</mi><mi>V</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/653eae2f-7d86-4ac1-be2a-344654fad9e8.png" style="width: 349px; height: 231px;" /></p><p>About center of the disk, we can also write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>J</mi><mn>0</mn></msub><mo>&#215;</mo><mi>h</mi><mo>=</mo><msub><mi>I</mi><mrow><mi>C</mi><mi>M</mi></mrow></msub><mi>&#969;</mi><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>J</mi><mn>0</mn></msub><mo>&#215;</mo><mi>h</mi><mo>=</mo><mfenced close="]" open="["><mrow><mfrac><mi>M</mi><mn>2</mn></mfrac><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced><mi>&#969;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><msub><mi>h</mi><mi>m</mi></msub><mo>&#8658;</mo><mi>&#969;</mi><mo>=</mo><mfrac><mi>V</mi><mi>b</mi></mfrac><mfenced><mtext>pure&#160;rolling</mtext></mfenced></math></p><p>From equation(ii), we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>J</mi><mn>0</mn></msub><mo>&#215;</mo><msub><mi>h</mi><mi>m</mi></msub><mo>=</mo><mfenced><mfrac><mi>M</mi><mn>2</mn></mfrac></mfenced><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced><mfrac><mi>V</mi><mi>b</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi>iii</mi></mfenced></math></p><p>By dividing equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math> with the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>iii</mi><mo>)</mo></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>h</mi><mi>m</mi></msub><mo>=</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>b</mi></mrow></mfrac></math></p><p>Now, considering all cases:</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8594;</mo><mn>0</mn><mo>&#8658;</mo><msub><mi>h</mi><mi>m</mi></msub><mo>=</mo><mfrac><mi>b</mi><mn>2</mn></mfrac></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8594;</mo><mi>b</mi><mo>&#8658;</mo><msub><mi>h</mi><mi>m</mi></msub><mo>=</mo><mi>b</mi></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><msub><mi>h</mi><mi>m</mi></msub><mo>&#8658;</mo><mi>&#969;</mi></math> is independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>(As we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mfrac><mi>V</mi><mi>b</mi></mfrac></math>)</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>h</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo></math>Wheel will slide without rolling.</p>

</details>

---

### Q6. JEE Advanced 2022 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>A flat surface of a thin uniform disk <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is glued to a horizontal table. Another thin uniform disk <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and with the same radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> rolls without slipping on the circumference of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>, as shown in the figure. A flat surface of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> also lies on the plane of the table. The center of mass of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> has fixed angular speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&omega;</mi></math> about the vertical axis passing through the center of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. The angular momentum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>M</mi><mi>&omega;</mi><msup><mi>R</mi><mn>2</mn></msup></math> with respect to the center of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. Which of the following is the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>?</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/35a7eb5c-0819-40c8-b88c-662a016b0a3f-image.png" style="width: 153px; height: 200px;" />​​​​​​​</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<blockquote><p>The centre of mass of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> has angular velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi></math> about the centre of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. Therefore, the velocity of the centre of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>B</mi></msub><mo>=</mo><mi>&#969;</mi><mn>2</mn><mi>R</mi></math>.</p><p>The point of contact of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is at rest therefore, the angular velocity of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#969;</mi><mi>B</mi></msub><mo>=</mo><mfrac><msub><mi>v</mi><mi>B</mi></msub><mi>R</mi></mfrac><mo>=</mo><mn>2</mn><mi>&#969;</mi></math></p><p>Now the angular momentum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> with respect to centre of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mi>M</mi><msub><mi>v</mi><mi>B</mi></msub><mi>r</mi><mo>+</mo><msub><mi>I</mi><mrow><mi>C</mi><mi>M</mi></mrow></msub><msub><mi>&#969;</mi><mi>B</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mi>M</mi><mi>&#969;</mi><mn>2</mn><mi>R</mi><mn>2</mn><mi>R</mi><mo>+</mo><mfrac><mrow><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mn>2</mn><mi>&#969;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mn>5</mn><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mi>&#969;</mi></math></p><p>Comparing the magnitude with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>M</mi><mi>&#969;</mi><msup><mi>R</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q7. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `2`

A pendulum consists of a bob of mass $m=0.1 \mathrm{~kg}$ and a massless inextensible string of length $L=1.0 \mathrm{~m}$. It is suspended from a fixed point at height $H=0.9 \mathrm{~m}$ above a frictionless horizontal floor. Initially, the bob of the pendulum is lying on the floor at rest vertically below the point of suspension. A horizontal impulse $P=0.2 \mathrm{~kg}-\mathrm{m} / \mathrm{s}$ is imparted to the bob at some instant. After the bob slides for some distance, the string becomes taut and the bob lifts off the floor. The magnitude of the angular momentum of the pendulum about the point of suspension just before the bob lifts off is $J \mathrm{~kg}-\mathrm{m}^{2} / \mathrm{s}$. The kinetic energy of the pendulum just after the liftoff is $K$ Joules.
The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>J</mi></math> is ____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.18**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/5cac6d5a-fb08-4b05-a94b-7f8841f31689-image.png" style="width: 250px; height: 131px;" /></p><p>The magnitude of the angular momentum of the pendulum about the point of suspension just before the bob lifts off is,</p><p>Angular momentum about top point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mi>m</mi><mi>V</mi><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>18</mn><mo>&#160;</mo><mi>kg</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">s</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>J</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>18</mn></math>.</p>

</details>

---

### Q8. JEE Advanced 2021 (Paper 1)

*Type:* `numerical` | *Level:* `2`

<p>A thin rod of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is free to rotate in horizontal plane about a fixed vertical axis passing through point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math>. A thin circular disc of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mn>4</mn></mfrac></math> is pivoted on this rod with its centre at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mn>4</mn></mfrac></math> from the free end so that it can rotate freely about its vertical axis, as shown in the figure. Assume that both the rod and the disc have uniform density and they remain horizontal during the motion. An outside stationary conserver finds the rod rotating with an angular velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#937;</mi></math> and the disc rotating about its vertical axis with angular velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#937;</mi></math>. The total angular momentum of the system about the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfenced><mfrac><mrow><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup><mi>&#937;</mi></mrow><mn>48</mn></mfrac></mfenced><mi>n</mi></mrow></mfenced></math>.</p><p>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is _________ .</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/57172981-f4e8-48a0-bb89-2209330604f4-image.png" style="width: 400px; height: 158px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **49**

**Detailed Solution:**

<p>Angular momentum of the system about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mover accent="true"><mi>L</mi><mo>&#8594;</mo></mover><mi>Rod</mi></msub><mo>+</mo><msub><mover accent="true"><mi>L</mi><mo>&#8594;</mo></mover><mi>Disc</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover accent="true"><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mover accent="true"><mi>L</mi><mo>&#8594;</mo></mover><mi>Rod</mi></msub><mo>+</mo><mfenced open="[" close="]"><mrow><msub><mfenced><msub><mover accent="true"><mi>L</mi><mo>&#8594;</mo></mover><mrow><mi>C</mi><mi>M</mi></mrow></msub></mfenced><mi>Disc</mi></msub><mo>+</mo><msub><mover accent="true"><mi>r</mi><mo>&#8594;</mo></mover><mrow><mi>C</mi><mi>M</mi></mrow></msub><mo>&#215;</mo><mfenced><mrow><msub><mi>M</mi><mrow><mi>D</mi><mi>i</mi><mi>s</mi><mi>c</mi></mrow></msub><msub><mover accent="true"><mi>V</mi><mo>&#8594;</mo></mover><mrow><mi>C</mi><mi>M</mi></mrow></msub></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup><mi>&#937;</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>8</mn></mfrac><mi>&#937;</mi><mo>+</mo><mi>M</mi><mfenced><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mn>4</mn></mfrac></mfenced><mi>&#937;</mi><mfenced><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mn>4</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac><mi>&#937;</mi><mo>+</mo><mfrac><mrow><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>8</mn></mfrac><mi>&#937;</mi><mo>+</mo><mfrac><mrow><mn>9</mn><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>16</mn></mfrac><mi>&#937;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mfrac><mrow><mn>16</mn><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup><mi>&#937;</mi><mo>+</mo><mn>6</mn><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup><mi>&#937;</mi><mo>+</mo><mn>27</mn><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup><mi>&#937;</mi></mrow><mn>48</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mfrac><mn>49</mn><mn>48</mn></mfrac><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup><mi>&#937;</mi></math></p><p>Compare it with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mi>M</mi><msup><mi>a</mi><mn>2</mn></msup></mrow><mn>48</mn></mfrac><mi>&#937;</mi></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>49</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>49</mn></math></p>

</details>

---

### Q9. JEE Advanced 2021 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

A particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi>kg</mi></math> is initially at rest in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi></math>-plane at a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>=</mo><mo>&#8722;</mo><mi>l</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>&#8722;</mo><mi>h</mi></mrow></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>. The particle is accelerated at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math> with a constant acceleration <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> along the positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-direction. Its angular momentum and torque with respect to the origin, in SI units, are represented by <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>L</mi><mo>&#8594;</mo></mover></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#964;</mi><mo>&#8594;</mo></mover></math>, respectively. <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> are unit vectors along the positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math>-directions, respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>=</mo><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>&#215;</mo><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></math> then which of the following statement(s) is (are) correct?

**Options:**

- **(A)** The particle arrives at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>=</mo><mi>l</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mi>h</mi></mrow></mfenced></math> at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math>.
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>&#964;</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> when the particle passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>=</mo><mi>l</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mi>h</mi></mrow></mfenced></math>.
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> when the particle passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>=</mo><mi>l</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mi>h</mi></mrow></mfenced></math>.
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>&#964;</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> when the particle passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mi>h</mi></mrow></mfenced></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>4</mn><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></math> when the particle passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>=</mo><mi>l</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mi>h</mi></mrow></mfenced></math>.**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/1efe06a1-b2d9-4375-ba2a-f1df63cc765e-image.png" style="width: 230px; height: 196px;" /></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>t</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow></mfenced><mo>:</mo></math></p><p>displacement along <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>X</mi></math> axis</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfenced><mn>10</mn></mfenced><mo>&#215;</mo><msup><mi>t</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p>Hence, particle arrives at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>10</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>=</mo><mi>l</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>&#8722;</mo><mi>h</mi></mrow></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>&#964;</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>F</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>10</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>&#8722;</mo><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>.2</mo><mo>&#215;</mo><mn>10</mn></mrow></mfenced><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>2</mn><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>p</mi><mo>&#8594;</mo></mover></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>10</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>&#8722;</mo><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>.2</mo><mo>&#215;</mo><mi>v</mi><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mfenced><mrow><mi>at</mi><mo>&#160;</mo><mi>t</mi><mo>=</mo><mn>2</mn><mi>s</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mo>+</mo><mn>10</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mover accent="true"><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>10</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>&#8722;</mo><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mn>4</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>=</mo><mfenced><mrow><mn>4</mn><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>y</mi><mo>=</mo><mo>&#8722;</mo><mi>h</mi></mrow></mfenced><mo>:</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>&#8722;</mo><mover accent="true"><mi mathvariant="normal">j</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover accent="true"><mi>F</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>2</mn><mover accent="true"><mi mathvariant="normal">i</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mover accent="true"><mi>&#964;</mi><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover accent="true"><mi>F</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>2</mn><mover accent="true"><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p>

</details>

---

### Q10. JEE Advanced 2020 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

<p>A rod of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>,</mo></math> pivoted at one of its ends, is hanging vertically. A bullet of the same mass moving at speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi></math> strikes the rod horizontally at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> from its pivoted end and gets embedded in it. The combined system now rotates with an angular speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ω</mi></math> about the pivot. The maximum angular speed <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>ω</mi><mi mathvariant="normal">M</mi></msub></math> is achieved for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msub><mi>x</mi><mi mathvariant="normal">M</mi></msub></math>. Then</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/99ef344b-db43-4bbb-8159-6d88ebd91855-D494.png"/></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>v</mi><mi>x</mi></mrow><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mfrac><mrow><mn>12</mn><mi>v</mi><mi>x</mi></mrow><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mi>M</mi></msub><mo>=</mo><mfrac><mi>L</mi><msqrt><mn>3</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#969;</mi><mi>M</mi></msub><mo>=</mo><mfrac><mi>v</mi><mrow><mn>2</mn><mi>L</mi></mrow></mfrac><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#969;</mi><mi>M</mi></msub><mo>=</mo><mfrac><mi>v</mi><mrow><mn>2</mn><mi>L</mi></mrow></mfrac><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p>The net torque on the system (rod+bullet) will be zero about hinge point. Therefore, we can apply the principle of angular momentum conservation about hinge point.</p><p>From angular momentum conservation,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>v</mi><mi>x</mi><mo>=</mo><mfenced><mrow><mfrac><mrow><mi>m</mi><msup><mi>L</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac><mo>+</mo><mi>m</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>&#969;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#969;</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>v</mi><mi>x</mi></mrow><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi>v</mi></mrow><mfenced><mrow><mstyle displaystyle="true"><mfrac><msup><mi>L</mi><mn>2</mn></msup><mi>x</mi></mfrac></mstyle><mo>+</mo><mn>3</mn><mi>x</mi></mrow></mfenced></mfrac></math></p><p>For maximum angular velocity,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">d</mi><mi>&#969;</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi mathvariant="normal">d</mi><mrow><mi mathvariant="normal">d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><mfrac><msup><mi>L</mi><mn>2</mn></msup><mi>x</mi></mfrac><mo>+</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><msup><mi>L</mi><mn>2</mn></msup></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mi>L</mi><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#969;</mi><mi>max</mi></msub><mo>=</mo><mfrac><mrow><mn>3</mn><mi>v</mi></mrow><mfenced><mstyle displaystyle="true"><mfrac><mrow><msqrt><mn>3</mn></msqrt><msup><mi>L</mi><mn>2</mn></msup></mrow><mi>L</mi></mfrac><mo>+</mo><msqrt><mn>3</mn></msqrt><mi>L</mi></mstyle></mfenced></mfrac><mo>=</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi mathvariant="normal">v</mi></mrow><mrow><mn>2</mn><mi>L</mi></mrow></mfrac></math></p>

</details>

---

### Q11. JEE Advanced 2016 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

<p>Two thin circular discs of mass m and 4m, having radii of a and 2a, respectively, are rigidly fixed by a massless, right rod of length <math><mi mathvariant="script">l</mi><mo>=</mo><msqrt><mn>24</mn></msqrt><mi>a</mi></math> through their center. This assembly is laid on a firm and flat surface, and set rolling without slipping on the surface so that the angular speed about the axis of the rod is <math><mi>ω</mi></math> . The angular momentum of the entire assembly about the point 'O' is <math><mover accent="true"><mrow><mi>L</mi></mrow><mo>→</mo></mover></math> (see the figure). Which of the following statement(s) is(are) true?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/Phy_Papr2_11.jpg"/></p>

**Options:**

- **(A)** The magnitude of angular momentum of the assembly about its center of mass is  <math><mn>17</mn><mi> </mi><mi>m</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mfrac><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** The magnitude of the z - component of  <math><mover accent="true"><mrow><mi>L</mi></mrow><mo>→</mo></mover><mi> </mi><mi>i</mi><mi>s</mi><mi> </mi><mn>55</mn><mi> </mi><mi>m</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>ω</mi></math>
- **(C)** The magnitude of angular momentum of center of mass of the assembly about the point O is 81  <math><mi>m</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mfrac><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** The center of mass of the assembly rotates about the z-axis with an angular speed of  <math><mfrac><mrow><mi>ω</mi></mrow><mrow><mn>5</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The center of mass of the assembly rotates about the z-axis with an angular speed of  <math><mfrac><mrow><mi>ω</mi></mrow><mrow><mn>5</mn></mrow></mfrac></math>**

**Detailed Solution:**

Magnitude of angular momentum of the assembly about its centre of mass =
 <math><mfrac><mrow><mi>m</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mi>ω</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi>m</mi><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>a</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mi>ω</mi><mo>=</mo><mfrac><mrow><mn>17</mn><mi>m</mi><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mi>ω</mi></math>

</details>

---

### Q12. JEE Advanced 2015 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `1`

<p>A ring of mass <math><mi mathvariant="normal">M</mi></math> and radius <math><mi mathvariant="normal">R</mi></math> is rotating with angular speed <math><mi mathvariant="normal">ω</mi></math> about a fixed vertical axis passing through its centre O with two point masses each of mass <math><mfrac><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mn>8</mn></mrow></mfrac></math> at rest at O. These masses can move radially outwards along two massless rods fixed on the ring as shown in the figure. At some instant the angular speed of the system is <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mi mathvariant="normal">ω</mi></math> and one of the masses is at a distance of <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi mathvariant="normal">R</mi></math> from O. At this instant the distance of the other mass from O is

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image11-050b419d-f020-4c1d-a6cd-50ce9d83eaee.png"/></p>

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi mathvariant="normal">R</mi></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi mathvariant="normal">R</mi></math>
- **(C)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi mathvariant="normal">R</mi></math>
- **(D)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi mathvariant="normal">R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi mathvariant="normal">R</mi></math>**

**Detailed Solution:**

Using conservation of angular momentum about axis of ring
 <math><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">ω</mi><mo>=</mo><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup><mfrac><mrow><mn>8</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mi mathvariant="normal">ω</mi><mo>+</mo><mfrac><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mn>8</mn></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mn>9</mn></mrow><mrow><mn>25</mn></mrow></mfrac><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mfenced separators="|"><mrow><mfrac><mrow><mn>8</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mi mathvariant="normal">ω</mi></mrow></mfenced><mo>+</mo><mfrac><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>8</mn></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mn>8</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mi mathvariant="normal">ω</mi></mrow></mfenced><mi mathvariant="normal"> </mi></math> 
 <math><mi mathvariant="normal">r</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">R</mi></mrow><mrow><mn>5</mn></mrow></mfrac></math>

</details>

---

### Q13. JEE Advanced 2014 (Paper 1)

*Type:* `numerical` | *Level:* `2`

<p>A horizontal circular platform of radius 0.5 m and mass 0.45 kg is free to rotate about its axis. Two massless spring toy-guns, each carrying a steel ball of mass 0.05 kg are attached to the platform at a distance 0.25 m from the centre on its either sides along its diameter (see figure). Each gun simultaneously fires the balls horizontally and perpendicular to the diameter in opposite directions. After leaving the platform, the balls have horizontal speed of 9 <math><mi mathvariant="normal">m</mi><msup><mrow><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> with respect to the ground. The rotational speed of the platform in rad <math><msup><mrow><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> after the balls leave the platform is

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image16-f46e5d55-7858-4d26-9211-d905259bec55.png"/></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

Since net torque about centre of rotation is zero, so we can apply conservation of angular momentum of the system about center of disc
 <math><msub><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mi mathvariant="normal">i</mi></mrow></msub><mo>=</mo><msub><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mi mathvariant="normal">f</mi></mrow></msub></math> 
 <math><mn>0</mn><mo>=</mo><mi mathvariant="normal">I</mi><mi mathvariant="normal">ω</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">m</mi><mi mathvariant="normal">v</mi><mi mathvariant="normal"> </mi><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">r</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> ; comparing magnitude
 <math><mo>∴</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>0.45</mn><mo>×</mo><mn>0.5</mn><mo>×</mo><mn>0.5</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mi mathvariant="normal">ω</mi><mo>=</mo><mn>0.05</mn><mo>×</mo><mn>9</mn><mo>×</mo><mfrac><mrow><mn>0.5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>×</mo><mn>2</mn></math> 
 <math><mo>∴</mo><mi mathvariant="normal">ω</mi><mo>=</mo><mn>4</mn></math>

</details>

---

### Q14. JEE Advanced 2013 (Paper 1)

*Type:* `numerical` | *Level:* `2`

A uniform circular disc of mass <math> <mrow> <mtext>50 kg</mtext> </mrow> </math> and radius <math> <mrow> <mtext>0.4 m</mtext> </mrow> </math> is rotating with an angular velocity of <math> <mrow> <msup> <mtext>10 rad s</mtext> <mn>-1</mn> </msup> </mrow> </math> about its own axis, which is vertical. Two uniform circular rings, each of mass <math> <mrow> <mtext>6.25 kg</mtext> </mrow> </math> and radius <math> <mrow> <mtext>0.2 m</mtext> </mrow> </math>, are gently placed symmetrically on the disc in such a manner that they are touching each other along the axis of the disc and are horizontal. Assume that the friction is large enough such that the rings are at rest relative to the disc and the system rotates about the original axis. The new angular velocity <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mo>in rad s</mo> <mn>-1</mn> </msup> </mrow> </mfenced> </mrow> </math> of the system is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM0012553_AnsExp_1.jpg"/>
​
Apply law of conservation of angular momentum
I<sub>i</sub>ω<sub>i</sub> = I<sub>f</sub> · ω<sub>f</sub>
<math> <mrow> <mo>∴</mo> <mspace width="0.5em"></mspace> <msub> <mtext>ω</mtext> <mtext>f</mtext> </msub> <mo>=</mo> <mfrac> <mrow> <msub> <mtext>I</mtext> <mn>2</mn> </msub> <mo>·</mo> <msub> <mtext>ω</mtext> <mn>2</mn> </msub> </mrow> <mrow> <msub> <mtext>I</mtext> <mtext>f</mtext> </msub> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mo>=</mo> <mo>{</mo> <mfrac> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>×</mo> <mtext>50</mtext> <mo>×</mo> <msup> <mtext>(0.4)</mtext> <mn>2</mn> </msup> </mrow> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>×</mo> <mtext>50</mtext> <msup> <mtext>(0.4)</mtext> <mn>2</mn> </msup> <mo>+</mo> <mn>4</mn> <mtext>(6.25)</mtext> <msup> <mtext>(0.2)</mtext> <mn>2</mn> </msup> </mrow> </mfrac> <mo>}</mo> <mo>×</mo> <mtext>10</mtext> </mrow> </math>
= 8 rad/sec

</details>

---

### Q15. JEE Advanced 2012 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

A small mass $m$ is attached to a massless string whose other end is fixed at $P$ as shown in the figure. The mass is undergoing circular motion in the $x-y$ plane with centre at $O$ and constant angular speed $\omega$. If the angular momentum of the system, calculated about $O$ and $P$ are denoted by $\vec{L}_{O}$ and $\vec{L}_{P}$ respectively, then

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/8I6vSvu0X5rikcmCVJdUb7jfJ20GlgxqNY9J1KxpsgU.original.fullsize.png">

**Options:**

- **(A)** $\vec{L}_{O}$ and $\vec{L}_{P}$ do not vary with time
- **(B)** $\vec{L}_{O}$ varies with time while $\vec{L}_{P}$ remains constant
- **(C)** $\vec{L}_{O}$ remains constant while $\vec{L}_{P}$ varies with time
- **(D)** $\vec{L}_{O}$ and $\vec{L}_{P}$ both vary with time

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\vec{L}_{O}$ remains constant while $\vec{L}_{P}$ varies with time**

**Detailed Solution:**

For all locations of $\mathrm{m}$ the angular momentum of the mass $m$ about $O$ i.e., $L_{o}$ is $m r^{2} \omega$ and is directed toward $+z$ direction. The angular momentum of mass $m$ about $P$ i.e., $L_{p}$ is $m v l$ and is directed for the given location of $m$ as shown in the figure. For different location of $m$, the direction of $\vec{L}_{P}$ remains changing.

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/bwsNwamWN-cQ7HKxrMmC3itcaB_EkdPHkLoI6EWocck.original.fullsize.png">

</details>

---

