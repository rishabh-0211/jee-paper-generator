# JEE Main Physics - Motion In One Dimension

## Topic 4: Non-uniform Motion

**Total Questions:** 22

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `numerical` | *Level:* `2`

Two masses of $3.4$ kg and $2.5$ kg are accelerated from an initial speed of $5$ m/s and $12$ m/s, respectively. The distances traversed by the masses in the $5^\text{th}$ second are $104$ m and $129$ m, respectively. The ratio of their momenta after $10$ s is $\dfrac{x}{8}$. The value of $x$ is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

The distance traversed in the $n^{\text{th}}$ second is given by $S_n = u + \dfrac{a}{2}(2n - 1)$.

For the first mass ($m_1 = 3.4$ kg, $u_1 = 5$ m/s):
$104 = 5 + \dfrac{a_1}{2}(2 \times 5 - 1)$
$99 = \dfrac{9a_1}{2} \Rightarrow a_1 = 22$ m/s$^2$

For the second mass ($m_2 = 2.5$ kg, $u_2 = 12$ m/s):
$129 = 12 + \dfrac{a_2}{2}(2 \times 5 - 1)$
$117 = \dfrac{9a_2}{2} \Rightarrow a_2 = 26$ m/s$^2$

Velocities of the masses after $10$ s:
$v_1 = u_1 + a_1 t = 5 + 22 \times 10 = 225$ m/s
$v_2 = u_2 + a_2 t = 12 + 26 \times 10 = 272$ m/s

Momenta of the masses after $10$ s:
$p_1 = m_1 v_1 = 3.4 \times 225 = 765$ kg m/s
$p_2 = m_2 v_2 = 2.5 \times 272 = 680$ kg m/s

Ratio of their momenta:
$\dfrac{p_1}{p_2} = \dfrac{765}{680} = \dfrac{9}{8}$

Comparing with $\dfrac{x}{8}$, we get $x = 9$.

Answer: $9$

</details>

---

### Q2. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The velocity of a particle is given as $\vec{v} = -x\hat{i} + 2y\hat{j} - z\hat{k}$ m/s. The magnitude of acceleration at point $(1, 2, 4)$ is _______ m/s$^2$.

**Options:**

- **(A)** $\sqrt{6}$
- **(B)** $9$
- **(C)** $\sqrt{33}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $9$**

**Detailed Solution:**

The velocity vector is given by $\vec{v} = v_x \hat{i} + v_y \hat{j} + v_z \hat{k} = -x \hat{i} + 2y \hat{j} - z \hat{k}$.

The components of acceleration are:

$a_x = v_x \dfrac{\partial v_x}{\partial x} + v_y \dfrac{\partial v_x}{\partial y} + v_z \dfrac{\partial v_x}{\partial z} = (-x)(-1) + 0 + 0 = x$

$a_y = v_x \dfrac{\partial v_y}{\partial x} + v_y \dfrac{\partial v_y}{\partial y} + v_z \dfrac{\partial v_y}{\partial z} = 0 + (2y)(2) + 0 = 4y$

$a_z = v_x \dfrac{\partial v_z}{\partial x} + v_y \dfrac{\partial v_z}{\partial y} + v_z \dfrac{\partial v_z}{\partial z} = 0 + 0 + (-z)(-1) = z$

The acceleration vector is $\vec{a} = x \hat{i} + 4y \hat{j} + z \hat{k}$.

At the point $(1, 2, 4)$, substituting $x = 1$, $y = 2$, and $z = 4$:

$\vec{a} = 1 \hat{i} + 4(2) \hat{j} + 4 \hat{k} = \hat{i} + 8 \hat{j} + 4 \hat{k}$

The magnitude of acceleration is:

$|\vec{a}| = \sqrt{1^2 + 8^2 + 4^2} = \sqrt{1 + 64 + 16} = \sqrt{81} = 9$ m/s$^2$

Answer: $9$

</details>

---

### Q3. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A particle starts moving from time $t=0$ and its coordinate is given as $x(t)=4 t^{3}-3 t$ 
 A. The particle returns to its original position (origin) 0.866 units later 
 B. The particle is 1 unit away from origin at its turning point 
 C. Acceleration of the particle is non-negative 
 D. The particle is 0.5 units away from origin at its turning point 
 E. Particle never turns back as acceleration is non-negative 
 Choose the correct answer from the options given below :

**Options:**

- **(A)** A, B, C Only
- **(B)** C, E Only
- **(C)** A, C Only
- **(D)** A, C, D Only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A, B, C Only**

**Detailed Solution:**

Given $x(t) = 4t^3 - 3t$, we find $v(t) = 12t^2 - 3$ and $a(t) = 24t$. 
Statement A: Setting $x(t) = 0$ gives $4t^3 - 3t = 0 \Rightarrow t(4t^2-3) = 0$, so $t = 0$ or $t = \sqrt{3/4} = 0.866$. The particle returns to origin at $t = 0.866$ units. TRUE. 
Statement B: Turning points occur at $v(t) = 0 \Rightarrow 12t^2 - 3 = 0 \Rightarrow t = \pm 0.5$. At $t = 0.5$: $x = 4(0.125) - 1.5 = -1$; distance = 1 unit. At $t = -0.5$: $x = 1$; distance = 1 unit. TRUE. 
Statement C: For $t \geq 0$ (particle starts at $t=0$), $a(t) = 24t \geq 0$. TRUE. 
Statement D: At turning points, distance is 1 unit, not 0.5. FALSE. 
Statement E: False because acceleration is non-negative only for $t \geq 0$, and particle does turn back at $t = 0.5$. FALSE. 
Correct statements: A, B, C Only.

</details>

---

### Q4. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A body of mass 2 kg moving with velocity of $\overrightarrow{\mathrm{v}}_{\mathrm{in}}=3 \hat{\mathrm{i}}+4 \hat{\mathrm{j}} \mathrm{ms}^{-1}$ enters into a constant force field of 6 N directed along positive z -axis. If the body remains in the field for a period of $\frac{5}{3}$ seconds, then velocity of the body when it emerges from force field is

**Options:**

- **(A)** $4 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}+5 \hat{\mathrm{k}}$
- **(B)** $3 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+5 \hat{\mathrm{k}}$
- **(C)** $3 \hat{i}+4 \hat{j}-5 \hat{k}$
- **(D)** $3 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+\sqrt{5} \hat{\mathrm{k}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+5 \hat{\mathrm{k}}$**

**Detailed Solution:**

$\begin{aligned} & \overrightarrow{\mathrm{a}}=\frac{\mathrm{B}}{2} \hat{\mathrm{k}}=3 \hat{\mathrm{k}}, \mathrm{t}=\frac{5}{3} \mathrm{~s} \\ & \overrightarrow{\mathrm{u}}=3 \hat{\mathrm{i}}+4 \hat{\mathrm{j}} \\ & \overrightarrow{\mathrm{v}}=\overrightarrow{\mathrm{u}}+\overrightarrow{\mathrm{a}} \mathrm{t}=3 \hat{\mathrm{i}}+4 \hat{\mathrm{j}}+5 \hat{\mathrm{k}}\end{aligned}$

</details>

---

### Q5. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A particle moves along the $x$-axis and has its displacement $x$ varying with time $t$ according to the equation $\mathrm{x}=\mathrm{c}_0\left(\mathrm{t}^2-2\right)+\mathrm{c}(\mathrm{t}-2)^2$ where $c_0$ and $c$ are constants of appropriate dimensions. Then, which of the following statements is correct?

**Options:**

- **(A)** the acceleration of the particle is $2 \mathrm{c}_0$
- **(B)** the acceleration of the particle is $2\mathrm{~c}$
- **(C)** the initial velocity of the particle is $4\mathrm{~c}$
- **(D)** the acceleration of the particle is $2\left(c+c_0\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) the acceleration of the particle is $2\left(c+c_0\right)$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{v}=\frac{\mathrm{dx}}{\mathrm{dt}}=2 \mathrm{tC}_0+2 \mathrm{C}(\mathrm{t}-2) \\ & \mathrm{a}=\frac{\mathrm{dv}}{\mathrm{dt}}=2 \mathrm{C}_0+2 \mathrm{C}\end{aligned}$

</details>

---

### Q6. JEE Main 2024 (05 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

A body moves on a frictionless plane starting from rest. If $S_n$ is distance moved between $t=n-1$ and $\mathrm{t}=\mathrm{n}$ and $\mathrm{S}_{\mathrm{n}-1}$ is distance moved between $\mathrm{t}=\mathrm{n}-2$ and $\mathrm{t}=\mathrm{n}-1$, then the ratio $\frac{\mathrm{S}_{\mathrm{n}-1}}{\mathrm{~S}_{\mathrm{n}}}$ is $\left(1-\frac{2}{x}\right)$ for $\mathrm{n}=10$. The value of $x$ is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **19**

**Detailed Solution:**

$\begin{aligned} & S_n=\frac{1}{2} a(2 n-1)=\frac{19 a}{2} \\ & S_{n-1}=\frac{1}{2} a(2 n-3)=\frac{17 a}{2} \\ & \frac{S_{n-1}}{S_n}=\frac{17}{19}=1-\frac{2}{x} \Rightarrow x=19\end{aligned}$

</details>

---

### Q7. JEE Main 2024 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `1`

A particle initially at rest starts moving from reference point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis, with velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi></math> that varies as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mn>4</mn><msqrt><mi>x</mi></msqrt><mo> </mo><mi mathvariant="normal">m</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The acceleration of the particle is _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mn>4</mn><msqrt><mi>x</mi></msqrt></math></p><p>Instantaneous acceleration of the particle can be written as, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>v</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>4</mn><msqrt><mi>x</mi></msqrt></mrow></mfenced><mo>×</mo><mfenced><mrow><mn>4</mn><mo>×</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfenced><mo>=</mo><mn>8</mn><mo> </mo><mi mathvariant="normal">m</mi><mo> </mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p>

</details>

---

### Q8. JEE Main 2023 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>A particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">g</mi><mo>&#160;</mo></math>moves in a straight line with retardation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is the displacement in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>SI</mi></math> units. Its loss of kinetic energy for above displacement is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mn>10</mn><mi>x</mi></mfrac></mfenced><mrow><mo>-</mo><mi>n</mi></mrow></msup><mi mathvariant="normal">J</mi><mo>.</mo></math> The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo>.</mo></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<blockquote><p>Acceleration can be written as, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>v</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>.</p><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi></math>(-ve sign is due to retardation)</p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>v</mi><mi>d</mi><mi>v</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Integrating both sides, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msubsup><mi>v</mi><mi>f</mi><mn>2</mn></msubsup><mo>-</mo><msubsup><mi>v</mi><mi>i</mi><mn>2</mn></msubsup></mrow></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>m</mi><mfenced><mrow><msubsup><mi>v</mi><mi>f</mi><mn>2</mn></msubsup><mo>-</mo><msubsup><mi>v</mi><mi>i</mi><mn>2</mn></msubsup></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>m</mi><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>&#916;</mi><mi>K</mi><mi>E</mi><mo>|</mo><mo>=</mo><mn>0</mn><mo>.</mo><mn>01</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mfrac><mn>10</mn><mi>x</mi></mfrac></mfenced><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>2</mn></math>.</p></blockquote>

</details>

---

### Q9. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The distance travelled by a particle is related to time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup></math>. The velocity of the particle at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<p>Given here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup></math></p><p>We know that velocity is the rate at which displacement changes with time. So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi>x</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>d</mo><mfenced><mrow><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac><mo>=</mo><mn>8</mn><mi>t</mi></math></p><p>Now, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></math></p><p>Velocity of particle is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mn>8</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>40</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>.</p>

</details>

---

### Q10. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msqrt><mi>x</mi></msqrt><mo>+</mo><mn>4</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mfrac><mrow><mi mathvariant="normal">d</mi><mi>x</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>t</mi></mrow></mfrac></mfenced><mrow><mi>t</mi><mo>=</mo><mn>4</mn></mrow></msub></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** Zero
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Zero**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msqrt><mi>x</mi></msqrt><mo>+</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msup><mfenced><mrow><mi>t</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>t</mi><mo>+</mo><mn>16</mn></math></p><p>Differentiating the above equation with respect to time,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi>x</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>t</mi><mo>-</mo><mn>8</mn></math></p><p>Putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>&#8722;</mo><mn>8</mn><mo>=</mo><mn>0</mn></math></p></blockquote>

</details>

---

### Q11. JEE Main 2022 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

A particle is moving in a straight line such that its velocity is increasing at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> per meter. The acceleration of the particle is _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> at a point where its velocity is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **100**

**Detailed Solution:**

<blockquote><p>According to the question, velocity is increasing at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">d</mi><mi>v</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>s</mi></mrow></mfrac><mo>=</mo><mn>5</mn><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. </p><p>Now acceleration <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mrow><mo>d</mo><mi>v</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mfrac><mrow><mo>d</mo><mi>v</mi></mrow><mrow><mo>d</mo><mi>s</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mi>v</mi><mfrac><mrow><mi mathvariant="normal">d</mi><mi>v</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>s</mi></mrow></mfrac><mo>=</mo><mn>20</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p></blockquote>

</details>

---

### Q12. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An object is thrown vertically upwards. At its maximum height, which of the following quantity becomes zero ?

**Options:**

- **(A)** Momentum
- **(B)** Potential energy
- **(C)** Acceleration
- **(D)** Force

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Momentum**

**Detailed Solution:**

<p>When a ball is thrown vertically upwards, at the maximum height the velocity is zero.</p><p>As momentum is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mi>m</mi><mi>v</mi></math>, so momentum is also zero at maximum height.</p>

</details>

---

### Q13. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A small ball of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is thrown upward with velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi></math> from the ground. The ball experiences a resistive force <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>k</mi><msup><mi>v</mi><mn>2</mn></msup></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi></math> is it speed. The maximum height attained by the ball is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mi>k</mi></mrow></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mi>k</mi><msup><mi>u</mi><mn>2</mn></msup></mrow><mi>g</mi></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>k</mi></mfrac><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>k</mi><msup><mi>u</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>k</mi></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mi>k</mi><msup><mi>u</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>g</mi></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mi>k</mi></mrow></mfrac><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>k</mi><msup><mi>u</mi><mn>2</mn></msup></mrow><mi>g</mi></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mi>k</mi></mrow></mfrac><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>k</mi><msup><mi>u</mi><mn>2</mn></msup></mrow><mi>g</mi></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">F</mi><mtext>ne&#160;</mtext></msub><mo>=</mo><mi>ma</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>mg</mi><mo>-</mo><msup><mi>mkv</mi><mn>2</mn></msup><mo>=</mo><mi>mv</mi><mfrac><mi>dv</mi><mi>ds</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">v</mi><mfrac><mi>dv</mi><mi>ds</mi></mfrac><mo>=</mo><mo>-</mo><mi mathvariant="normal">g</mi><mo>-</mo><msup><mi>kv</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msubsup><mo>&#8747;</mo><msub><mi mathvariant="normal">v</mi><mn>0</mn></msub><mn>0</mn></msubsup><mfrac><mi>vdv</mi><mrow><mi mathvariant="normal">g</mi><mo>+</mo><msup><mi>kv</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi mathvariant="normal">h</mi></msubsup><mi>ds</mi><mo>=</mo><msub><mi mathvariant="normal">h</mi><mi>max</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">h</mi><mi>max</mi></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi mathvariant="normal">K</mi></mrow></mfrac><mo>in</mo><mfenced><mfrac><mrow><mi mathvariant="normal">g</mi><mo>+</mo><msubsup><mi>kv</mi><mn>0</mn><mn>2</mn></msubsup></mrow><mi mathvariant="normal">g</mi></mfrac></mfenced></math></p><p> </p>

</details>

---

### Q14. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A particle of charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> and mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is subjected to an electric field <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><msub><mi>E</mi><mn>0</mn></msub><mfenced><mrow><mn>1</mn><mo>&#8211;</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></math> in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>direction, where a and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>0</mn></msub></math> are constants. Initially the particle was at rest at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>. Other than the initial position the kinetic energy of the particle becomes zero when the distance of the particle from the origin is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">a</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>2</mn><mi mathvariant="normal">a</mi></mfrac></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>3</mn><mi mathvariant="normal">a</mi></mfrac></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>1</mn><mi mathvariant="normal">a</mi></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>3</mn><mi mathvariant="normal">a</mi></mfrac></msqrt></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">W</mi><mi>ex</mi></msub><mo>=</mo><mi>&#916;K</mi><mo>&#160;&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi mathvariant="normal">K</mi><mn>1</mn></msub><mo>-</mo><msub><mi mathvariant="normal">K</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi mathvariant="normal">x</mi></msubsup><mi>qEdx</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;q&#160;</mtext><msubsup><mo>&#8747;</mo><mn>0</mn><mi mathvariant="normal">x</mi></msubsup><msub><mi mathvariant="normal">E</mi><mn>0</mn></msub><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>Qx</mi><mn>2</mn></msup></mrow></mfenced><mi>dx</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>qE</mi><mn>0</mn></msub><msubsup><mo>&#8747;</mo><mn>0</mn><mi mathvariant="normal">x</mi></msubsup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>ax</mi><mn>2</mn></msup></mrow></mfenced><mi>dx</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>-</mo><mfrac><msup><mi>ax</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><msup><mi>ax</mi><mn>2</mn></msup><mn>3</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>ax</mi><mn>2</mn></msup><mn>3</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>3</mn><mi mathvariant="normal">a</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><msqrt><mfrac><mn>3</mn><mi mathvariant="normal">a</mi></mfrac></msqrt></math> </p>

</details>

---

### Q15. JEE Main 2020 (09 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

The distance <math><mi>x</mi></math> covered by a paritcle in one dimensional motion varies with time <math><mi>t</mi></math> as <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>a</mi><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>b</mi><mi>t</mi><mo>+</mo><mi>c</mi></math> . If the acceleration of the particle depends on <math><mi>x</mi></math> as <math><msup><mrow><mi>x</mi></mrow><mrow><mo>-</mo><mi>n</mi></mrow></msup></math> , where <math><mi>n</mi></math> is an integer, the value of <math><mi>n</mi></math> is _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>a</mi><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>b</mi><mi>t</mi><mo>+</mo><mi>c</mi></math>
<math><mn>2</mn><mi>x</mi><mi>v</mi><mo>=</mo><mn>2</mn><mi>a</mi><mi>t</mi><mo>+</mo><mn>2</mn><mi>b</mi></math>
<math><mi>x</mi><mi>v</mi><mo>=</mo><mi>a</mi><mi>t</mi><mo>+</mo><mi>b</mi></math>
<math><msup><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>a</mi><mi>x</mi><mo>=</mo><mi>a</mi></math>
<math><mi>a</mi><mi>x</mi><mo>=</mo><mi>a</mi><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>a</mi><mi>t</mi><mo>+</mo><mi>b</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mi>a</mi><mo>=</mo><mfrac><mrow><mi>a</mi><mfenced separators="|"><mrow><mi>a</mi><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>b</mi><mi>t</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mi>a</mi><mi>t</mi><mo>+</mo><mi>b</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mrow><mi>a</mi><msup><mi>c</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mi>&#945;</mi><mo>&#160;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>

</details>

---

### Q16. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A particle is moving with speed <math><mi>v</mi><mo>=</mo><mi>b</mi><msqrt><mi>x</mi></msqrt></math> along positive <math><mi>x</mi><mo>-</mo></math> axis. Calculate the speed of the particle at time <math><mi>t</mi><mo>=</mo><mi>&#964;</mi></math> (assume that the particle is at origin at <math><mi>t</mi><mo>=</mo><mn>0</mn></math> )

**Options:**

- **(A)** <math><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>τ</mi></math>
- **(B)** <math><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>τ</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>τ</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>τ</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>τ</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>v</mi><mo>=</mo><mi mathvariant="normal">b</mi><msqrt><mi mathvariant="normal">x</mi></msqrt></math> &hellip; (1)
<math><mo>&#8658;</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">t</mi></mrow></mfrac><mo>=</mo><mi mathvariant="normal">b</mi><msqrt><mi mathvariant="normal">x</mi></msqrt></math>
<math><mfrac><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow><mrow><msqrt><mi mathvariant="normal">x</mi></msqrt></mrow></mfrac><mo>=</mo><mi mathvariant="normal">b</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">t</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8747;</mo><mn>0</mn><mi mathvariant="normal">x</mi></munderover><mfrac><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">x</mi></mrow><msqrt><mi mathvariant="normal">x</mi></msqrt></mfrac><mo>=</mo><munderover><mo stretchy="true">&#8747;</mo><mn>0</mn><mi>t</mi></munderover><mi mathvariant="normal">b</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">t</mi></math>
<math><mn>2</mn><msqrt><mi mathvariant="normal">x</mi></msqrt><mo>=</mo><mi mathvariant="normal">b</mi><mi mathvariant="normal">t</mi></math> &hellip; (2)
From equation (1) and (2)
<math><mi>v</mi><mo>=</mo><mi mathvariant="normal">b</mi><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">b</mi><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo></math>
<math><mo>&#8756;</mo><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">t</mi><mo>=</mo><mi mathvariant="normal">&#964;</mi></math> 
<math><mi>v</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">b</mi></mrow><mrow><mn>2</mn></mrow></msup><mi mathvariant="normal">&#964;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>

</details>

---

### Q17. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The position of a particle as a function of time <math><mi>t</mi><mo>,</mo></math> is given by <math><mi>x</mi><mfenced separators="|"><mrow><mi>t</mi></mrow></mfenced><mo>=</mo><mi>a</mi><mi>t</mi><mo>+</mo><mi>b</mi><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>c</mi><msup><mrow><mi>t</mi></mrow><mrow><mn>3</mn></mrow></msup></math> where <math><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi></math> and <math><mi>c</mi></math> are constants. When the particles zero acceleration, then its velocity will be:

**Options:**

- **(A)** <math><mi>a</mi><mo>+</mo><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn><mi>c</mi></mrow></mfrac></math>
- **(B)** <math><mi>a</mi><mo>+</mo><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><mi>c</mi></mrow></mfrac></math>
- **(C)** <math><mi>a</mi><mo>+</mo><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>c</mi></mrow></mfrac></math>
- **(D)** <math><mi>a</mi><mo>+</mo><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mi>c</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi>a</mi><mo>+</mo><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn><mi>c</mi></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>x</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>a</mi><mi>t</mi><mo>+</mo><mi>b</mi><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>c</mi><msup><mrow><mi>t</mi></mrow><mrow><mn>3</mn></mrow></msup></math>
velocity <math><mi>v</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mi>d</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mi>d</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mfenced separators="|"><mrow><mi>a</mi><mi>t</mi><mo>+</mo><mi>b</mi><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>c</mi><msup><mrow><mi>t</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mi>t</mi><mo>-</mo><mn>3</mn><mi>c</mi><msup><mi>t</mi><mn>2</mn></msup></math>
Acceleration <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mi>v</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mn>2</mn><mi>b</mi><mo>-</mo><mn>6</mn><mi>t</mi><mi>c</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>acceleration</mtext><mo>=</mo><mn>0</mn><mspace linebreak="newline"/><mo>&#8658;</mo><mn>2</mn><mi>b</mi><mo>-</mo><mn>6</mn><mi>t</mi><mi>c</mi><mo>=</mo><mn>0</mn></math>
<math><mi>t</mi><mo>=</mo><mfrac><mrow><mi>b</mi></mrow><mrow><mn>3</mn><mi>c</mi></mrow></mfrac></math>
<math><mo>&#8756;</mo></math> velocity when <math><mi>t</mi><mo>=</mo><mfrac><mrow><mi>b</mi></mrow><mrow><mn>3</mn><mi>c</mi></mrow></mfrac><mo>,</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mfenced separators="|"><mrow><mi>t</mi><mo>=</mo><mfrac><mi>b</mi><mrow><mn>3</mn><mi>c</mi></mrow></mfrac></mrow></mfenced></msub><mo>=</mo><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mfenced separators="|"><mfrac><mi>b</mi><mrow><mn>3</mn><mi>c</mi></mrow></mfrac></mfenced><mo>-</mo><mn>3</mn><msup><mfenced separators="|"><mfrac><mi>b</mi><mrow><mn>3</mn><mi>c</mi></mrow></mfrac></mfenced><mn>2</mn></msup></math>
<math><mo>=</mo><mi>a</mi><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn><mi>c</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn><mi>c</mi></mrow></mfrac></math>
<math><mo>=</mo><mi>a</mi><mo>+</mo><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn><mi>c</mi></mrow></mfrac></math>

</details>

---

### Q18. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `1`

An object, moving with a speed of $6.25 \mathrm{~m} / \mathrm{s}$, is decelerated at a rate given by :
$$
\frac{\mathrm{dv}}{\mathrm{dt}}=-2.5 \sqrt{\mathrm{v}}
$$
where $v$ is the instantaneous speed. The time taken by the object, to come to rest, would be:

**Options:**

- **(A)** $2 \mathrm{~s}$
- **(B)** $4 \mathrm{~s}$
- **(C)** $8 \mathrm{~s}$
- **(D)** $1 \mathrm{~s}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \mathrm{~s}$**

**Detailed Solution:**

$$
\frac{d v}{d t}=-2.5 \sqrt{v}
$$
Integrating the above equation.
$$
\Rightarrow 2 \sqrt{v}=-2.5 \mathrm{t}+\mathrm{C}
$$
at $\mathrm{t}=0, \mathrm{v}=6.25 \Rightarrow \mathrm{C}=5$
at $v=0 \Rightarrow t=\frac{5}{2.5}=2 \mathrm{~s}$

</details>

---

### Q19. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

The velocity of a particle is $\mathrm{v}=\mathrm{v}_0+\mathrm{gt}+\mathrm{ft}^2$. If its position is $\mathrm{x}=0$ at $\mathrm{t}=0$, then its displacement after unit time $(t=1)$ is

**Options:**

- **(A)** $\mathrm{v_0+2 g+3 f}$
- **(B)** $\mathrm{v_0+g / 2+f / 3}$
- **(C)** $\mathrm{v_0+g+f}$
- **(D)** $\mathrm{v_0+g / 2+f}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{v_0+g / 2+f / 3}$**

**Detailed Solution:**

$\mathrm{\int_0^x d x=\int_0^1\left(V_0+g t+\mathrm{ft}^2\right) d t}$
$\mathrm{x=v_0+g\left(\frac{1}{2}\right)+f\left(\frac{1}{3}\right)}$

</details>

---

### Q20. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

A particle located at $x=0$ at time $t=0$, starts moving along the positive $x$-direction with a velocity ' $v$ ' that varies as $v=\alpha \sqrt{x}$. The displacement of the particle varies with time as

**Options:**

- **(A)** $t^3$
- **(B)** $t^2$
- **(C)** $t$
- **(D)** $t^{1 / 2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $t^2$**

**Detailed Solution:**

$\frac{\mathrm{d} x}{\mathrm{dt}}=\alpha \int \frac{\mathrm{dx}}{\sqrt{\mathrm{x}}}=\int \alpha \mathrm{dt} \Rightarrow \mathrm{x} \alpha \mathrm{t}^2$

</details>

---

### Q21. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

The relation between time $t$ and distance $\mathrm{x}$ is $\mathrm{t}=a \mathrm{x}^2+\mathrm{bx}$ where $\mathrm{a}$ and $\mathrm{b}$ are constants. The acceleration is

**Options:**

- **(A)** $-2 a b v^2$
- **(B)** $2 b v^3$
- **(C)** $-2 a v^3$
- **(D)** $2 a v^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-2 a v^3$**

**Detailed Solution:**

$$
t=a x^2+b x
$$
by differentiating acceleration $=-2 a v^3$

</details>

---

### Q22. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

The co-ordinates of a moving particle at any time ' $t$ ' are given by $x=\alpha t^3$ and $y=\beta t^3$. The speed of the particle at time ' $t$ ' is given by

**Options:**

- **(A)** $3 t \sqrt{\alpha^2+\beta^2}$
- **(B)** $3 t^2 \sqrt{\alpha^2+\beta^2}$
- **(C)** $\mathrm{t}^2 \sqrt{\alpha^2+\beta^2}$
- **(D)** $\sqrt{\alpha^2+\beta^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 t^2 \sqrt{\alpha^2+\beta^2}$**

**Detailed Solution:**

$V_x=\frac{d x}{d t}=3 \alpha t^2, V_y=\frac{d y}{d t}=3 \beta t^2$
$\overrightarrow{\mathrm{v}}=\sqrt{\mathrm{V}_{\mathrm{x}^2}+\mathrm{V}_{\mathrm{y}^2}}=3 \mathrm{t}^2 \sqrt{\alpha^2+\beta^2}$

</details>

---

