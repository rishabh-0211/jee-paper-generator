# JEE Main Physics - Electrostatics

## Topic 1: Electric Charge and Coulomb's law

**Total Questions:** 47

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two point charges $q_1=3\,\mu C$ and $q_2=-4\,\mu C$ are placed at points $(2\hat{i}+3\hat{j}+3\hat{k})$ and $(\hat{i}+\hat{j}+\hat{k})$ respectively. Force on charge $q_2$ is ________ N. $\left(\text{Take } \dfrac{1}{4\pi\epsilon_0} = 9\times 10^9 \text{ SI Units}\right)$

**Options:**

- **(A)** $(12\hat{i}+24\hat{j}+24\hat{k})\times 10^{-3}$
- **(B)** $(4\hat{i}+8\hat{j}+8\hat{k})\times 10^{-3}$
- **(C)** $(3\hat{i}+6\hat{j}+6\hat{k})\times 10^{-3}$
- **(D)** $(-4\hat{i}-8\hat{j}-8\hat{k})\times 10^{-3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(4\hat{i}+8\hat{j}+8\hat{k})\times 10^{-3}$**

**Detailed Solution:**

Position vector of $q_1$, $\vec{r}_1 = 2\hat{i} + 3\hat{j} + 3\hat{k}$

Position vector of $q_2$, $\vec{r}_2 = \hat{i} + \hat{j} + \hat{k}$

Vector from $q_1$ to $q_2$ is $\vec{r}_{21} = \vec{r}_2 - \vec{r}_1 = (\hat{i} + \hat{j} + \hat{k}) - (2\hat{i} + 3\hat{j} + 3\hat{k}) = -\hat{i} - 2\hat{j} - 2\hat{k}$

Magnitude $|\vec{r}_{21}| = \sqrt{(-1)^2 + (-2)^2 + (-2)^2} = \sqrt{9} = 3$

Force on $q_2$ due to $q_1$ is given by Coulomb's law in vector form:

$\vec{F}_{21} = \dfrac{1}{4\pi\epsilon_0} \dfrac{q_1 q_2}{|\vec{r}_{21}|^3} \vec{r}_{21}$

Substituting the given values:

$\vec{F}_{21} = \dfrac{9 \times 10^9 \times (3 \times 10^{-6}) \times (-4 \times 10^{-6})}{3^3} (-\hat{i} - 2\hat{j} - 2\hat{k})$

$\vec{F}_{21} = \dfrac{-108 \times 10^{-3}}{27} (-\hat{i} - 2\hat{j} - 2\hat{k})$

$\vec{F}_{21} = -4 \times 10^{-3} (-\hat{i} - 2\hat{j} - 2\hat{k})$

$\vec{F}_{21} = (4\hat{i} + 8\hat{j} + 8\hat{k}) \times 10^{-3} \text{ N}$

Answer: $(4\hat{i}+8\hat{j}+8\hat{k})\times 10^{-3}$

</details>

---

### Q2. JEE Main 2026 (24 January Shift 2)

*Type:* `numerical` | *Level:* `2`

A point charge $q=1 \mu \mathrm{C}$ is located at a distance 2 cm from one end of a thin insulating wire of length 10 cm having a charge $Q=24 \mu \mathrm{C}$, distributed uniformly along its length, as shown in figure. Force between $q$ and wire is $\_\_\_\_$ N. (Use : $\frac{1}{4 \pi \epsilon_{\mathrm{o}}}=9 \times 10^{9} \mathrm{~N}. \mathrm{m}^{2} / \mathrm{C}^{2}$) 
 <img style="width:400px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/24S2_q_48_1.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **90**

**Detailed Solution:**

Consider a small element of length $dx$ on the wire at a distance $x$ from the point charge $q$.
The linear charge density of the wire is $\lambda = \frac{Q}{L} = \frac{24 \times 10^{-6}}{0.1} = 240 \times 10^{-6}$ C/m.
The charge on the small element is $dQ = \lambda dx$.
The electrostatic force between the point charge $q$ and the element $dQ$ is $dF = \frac{k q dQ}{x^2} = \frac{k q \lambda dx}{x^2}$.
The total force $F$ is obtained by integrating $dF$ from $x = a$ to $x = a + L$, where $a = 2$ cm and $L = 10$ cm.
$F = \int_{0.02}^{0.12} \frac{k q \lambda}{x^2} dx = k q \lambda \left[ -\frac{1}{x} \right]_{0.02}^{0.12}$
$F = k q \lambda \left( \frac{1}{0.02} - \frac{1}{0.12} \right) = k q \frac{Q}{L} \left( \frac{0.12 - 0.02}{0.02 \times 0.12} \right)$
$F = \frac{k q Q}{L} \frac{L}{a(a+L)} = \frac{k q Q}{a(a+L)}$
Substituting the given values: $k = 9 \times 10^9$ N.m$^2$/C$^2$, $q = 1 \times 10^{-6}$ C, $Q = 24 \times 10^{-6}$ C, $a = 0.02$ m, and $a+L = 0.12$ m.
$F = \frac{9 \times 10^9 \times 1 \times 10^{-6} \times 24 \times 10^{-6}}{0.02 \times 0.12}$
$F = \frac{9 \times 24 \times 10^{-3}}{0.0024} = \frac{216 \times 10^{-3}}{2.4 \times 10^{-3}}$
$F = \frac{216}{2.4} = 90$ N.

</details>

---

### Q3. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two metal spheres of radius $R$ and $3 R$ have same surface charge density $\sigma$. If they are brought in contact and then separated, the surface charge density on smaller and bigger sphere becomes $\sigma_1$ and $\sigma_2$, respectively. The ratio $\frac{\sigma_1}{\sigma_2}$ is.

**Options:**

- **(A)** $\frac{1}{9}$
- **(B)** 9
- **(C)** $\frac{1}{3}$
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

For conducting sphere, $\mathrm{V}=\frac{\sigma \mathrm{r}}{\varepsilon_0}$
After contact, $\mathrm{V}_1=\mathrm{V}_2$
$\begin{aligned}
& \sigma_1 r_1=\sigma_2 r_2 \\
& \frac{\sigma_1}{\sigma_2}=\frac{r_2}{\mathrm{r}_1} \\
& \frac{\sigma_1}{\sigma_2}=3
\end{aligned}$

</details>

---

### Q4. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A small bob of mass 100 mg and charge $+10 \mu \mathrm{C}$ is connected to an insulating string of length 1 m. It is brought near to an infinitely long nonconducting sheet of charge density ' $\sigma$ ' as shown in figure. If string subtends an angle of $45^{\circ}$ with the sheet at equilibrium the charge density of sheet will be :
(Given, $\varepsilon_0=8.85 \times 10^{-12} \frac{\mathrm{~F}}{\mathrm{~m}}$ and acceleration due to gravity, $g=10 \mathrm{~m} / \mathrm{s}^2$)
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1EpPEURCP5Ix_xGUrB4RhVE_-vuwF7UvIdiqFExwM4Y.original.fullsize.png"/>

**Options:**

- **(A)** $0.885 \mathrm{nC} / \mathrm{m}^2$
- **(B)** $17.7 \mathrm{nC} / \mathrm{m}^2$
- **(C)** $885 \mathrm{nC} / \mathrm{m}^2$
- **(D)** $1.77 \mathrm{nC} / \mathrm{m}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1.77 \mathrm{nC} / \mathrm{m}^2$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/MWpxmQR0NR_3rYnuG7lF-wa00y43X_LbqxroNyqKwZM.original.fullsize.png"/>
$\begin{aligned} & \mathrm{qE}=\mathrm{mg} \\ & \mathrm{q}\left[\frac{\sigma}{2 \varepsilon_0}\right]=\mathrm{mg} \\ & \sigma=\frac{2 \varepsilon_0 \mathrm{mg}}{\mathrm{q}} \\ & \sigma=\frac{2 \times 8.85 \times 10^{-12} \times 100 \times 10^{-6} \times 10}{10 \times 10^{-6}} \\ & \sigma=17.7 \times 10^{-10} \mathrm{C} / \mathrm{m}^2 \\ & \sigma=1.77 \mathrm{nC} / \mathrm{m}^2\end{aligned}$

</details>

---

### Q5. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A small uncharged conducting sphere is placed in contact with an identical sphere but having $4 \times 10^{-8} \mathrm{C}$ charge and then removed to a distance such that the force of repulsion between them is $9 \times 10^{-3} \mathrm{~N}$. The distance between them is (Take $\frac{1}{4 \pi \epsilon_{\mathrm{o}}}$ as $9 \times 10^9 \mathrm{in} \mathrm{SI}$ units)

**Options:**

- **(A)** 3 cm
- **(B)** 2 cm
- **(C)** 4 cm
- **(D)** 1 cm

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2 cm**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/atIquIupRDXLswVF6bi5nhSyC8CPvMiZBycLEGcIpAU.original.fullsize.png">




$\begin{aligned} & \mathrm{F}=\frac{\mathrm{k}\left(\frac{\theta}{2}\right)\left(\frac{\theta}{2}\right)}{\mathrm{r}^2} \\ & 9 \times 10^{-3}=\frac{9 \times 10^9 \times\left(4 \times 10^{-8}\right) \times 4 \times 10^{-8}}{4 \times \mathrm{r}^2} \\ & \mathrm{r}^2=\frac{9 \times 10^9 \times 16 \times 10^{-16}}{4 \times 9 \times 10^{-3}}=4 \times 10^{-4} \\ & \mathrm{r}=2 \times 10^{-2} \mathrm{~m} \Rightarrow 2 \mathrm{~cm}\end{aligned}$

</details>

---

### Q6. JEE Main 2025 (23 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

A positive ion $A$ and a negative ion $B$ has charges $6.67 \times 10^{-19} \mathrm{C}$ and $9.6 \times 10^{-10} \mathrm{C}$, and masses $19.2 \times 10^{-27} \mathrm{~kg}$ and $9 \times 10^{-27} \mathrm{~kg}$ respectively. At an instant, the ions are separated by a certain distance r. At that instant the ratio of the magnitudes of electrostatic force to gravitational force is $P \times 10^{45}$, where the value of 10$P$ is $\qquad$
(Take $\frac{1}{4 \pi \varepsilon_0}=9 \times 10^9 \mathrm{Nm}^2 \mathrm{C}^{-1}$ and universal gravitational constant as $6.67 \times 10^{-11} \mathrm{Nm}^2 \mathrm{~kg}^{-2}$ )
Assume that charge may not be an integral multiple of electrons.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$\begin{aligned}
F_e & =\frac{k q_1 q_2}{r^2} \\
F_g & =\frac{G m_1 m_2}{r^2} \\
\frac{F_e}{F_g} & =\frac{k q_1 q_2}{G m_1 m_2} \\
& =\frac{9 \times 10^9 \times 6.67 \times 10^{-19} \times 9.6 \times 10^{-10}}{6.67 \times 10^{-11} \times 19.2 \times 10^{-27} \times 9 \times 10^{-27}} \\
& =\frac{10^{-20}}{2 \times 10^{-65}}
\end{aligned}$

</details>

---

### Q7. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Two identical conducting spheres $P$ and $S$ with charge $Q$ on each, repel each other with a force $16 \mathrm{~N}$. A third identical uncharged conducting sphere $R$ is successively brought in contact with the two spheres. The new force of repulsion between $\mathrm{P}$ and $\mathrm{S}$ is :

**Options:**

- **(A)** $1 \mathrm{~N}$
- **(B)** $6 \mathrm{~N}$
- **(C)** $12 \mathrm{~N}$
- **(D)** $4 \mathrm{~N}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6 \mathrm{~N}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/BKDoEzkhtsftiaf7JdbQNNJd4EbmiiNtMZGOscSXc0A.original.fullsize.png">
$\begin{aligned}
& F_{P S} \propto Q^2 \\
& F_{P S}=16 \mathrm{~N}
\end{aligned}$
Now If $\mathrm{P} ~\&~ \mathrm{R}$ are brought in contact then
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/NTrtGxSR2AwUl33HCr9v-wS2DzdpLNck7AoucIw-k6M.original.fullsize.png">
Now If $S \& R$ are brought in contact then
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/GRQyVjbW1ZFBwv9o1lRPD9ci5RAJNiUjGxdMSQnWZh4.original.fullsize.png">
New force between $P ~\&~ S$ is :
$\begin{aligned}
& \mathrm{F}_{\mathrm{PS}} \propto \frac{\mathrm{Q}}{2} \times \frac{3 \mathrm{Q}}{4} \\
& \mathrm{~F}_{\mathrm{PS}} \propto \frac{3 \mathrm{Q}^2}{8}=\frac{3}{8} \times 16=6 \mathrm{~N}
\end{aligned}$

</details>

---

### Q8. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The vehicles carrying inflammable fluids usually have metallic chains touching the ground :

**Options:**

- **(A)** To protect tyres from catching dirt from ground
- **(B)** To alert other vehicles
- **(C)** It is a custom
- **(D)** To conduct excess charge due to air friction to ground and prevent sparking

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) To conduct excess charge due to air friction to ground and prevent sparking**

**Detailed Solution:**

Static charge is developed due to air friction. This can result in combustion. So, metallic chains is used to discharge excess charge.

</details>

---

### Q9. JEE Main 2024 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>Two identical charged spheres are suspended by strings of equal lengths. The strings make an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>θ</mi></math> with each other. When suspended in water the angle remains the same. If density of the material of the sphere is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo> </mo><mi mathvariant="normal">g</mi><mo>/</mo><mi>cc</mi><mo>,</mo></math> the dielectric constant of water will be ______.</p><p>(Take density of water <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo> </mo><mi mathvariant="normal">g</mi><mo>/</mo><mi>cc</mi></math>)</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/861fab98-5938-470d-8be7-bf274f340afe.png" style="width: 300px; height: 223px;"/></p><p>In air:</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfrac><mi>θ</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>F</mi><mrow><mi>m</mi><mi>g</mi></mrow></mfrac><mo>=</mo><mfrac><msup><mi>q</mi><mn>2</mn></msup><mrow><mn>4</mn><mi>π</mi><msub><mi>ε</mi><mn>0</mn></msub><msup><mi>r</mi><mn>2</mn></msup><mi>m</mi><mi>g</mi></mrow></mfrac></math></p><p>In water:</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfrac><mi>θ</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><msup><mi>F</mi><mo>'</mo></msup><mrow><mi>m</mi><msup><mi>g</mi><mo>'</mo></msup></mrow></mfrac><mo>=</mo><mfrac><msup><mi mathvariant="normal">q</mi><mn>2</mn></msup><mrow><mn>4</mn><mi>π</mi><msub><mi>ε</mi><mn>0</mn></msub><msub><mi>ε</mi><mi mathvariant="normal">r</mi></msub><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup><msub><mi>mg</mi><mi>eff</mi></msub></mrow></mfrac></math></p><p>Equate both equations, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>ε</mi><mn>0</mn></msub><mo> </mo><mi mathvariant="normal">g</mi><mo>=</mo><msub><mi>ε</mi><mn>0</mn></msub><msub><mi>ε</mi><mi mathvariant="normal">r</mi></msub><mi mathvariant="normal">g</mi><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>.</mo><mn>5</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>ε</mi><mi mathvariant="normal">r</mi></msub><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q10. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Force between two point charges <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>2</mn></msub></math> placed in vacuum at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cm</mi></math> apart is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math>. Force between them when placed in a medium having dielectric <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><mn>5</mn></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mn>5</mn></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cm</mi></math> apart will be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>F</mi><mn>25</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>F</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>F</mi><mn>5</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mi>F</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>F</mi></math>**

**Detailed Solution:**

<p>Using Coulomb's law, we can write:</p><p>In air <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>π</mi><msub><mi>ε</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><msub><mi>q</mi><mn>1</mn></msub><msub><mi>q</mi><mn>2</mn></msub></mrow><msup><mi>r</mi><mn>2</mn></msup></mfrac></math></p><p>In medium <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>'</mo><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>π</mi><mfenced><mrow><mi>K</mi><msub><mi>ε</mi><mn>0</mn></msub></mrow></mfenced></mrow></mfrac><mfrac><mrow><msub><mi>q</mi><mn>1</mn></msub><msub><mi>q</mi><mn>2</mn></msub></mrow><msup><mfenced><mrow><mi>r</mi><mo>'</mo></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>π</mi><mfenced><mrow><mn>5</mn><msub><mi>ε</mi><mn>0</mn></msub></mrow></mfenced></mrow></mfrac><mfrac><mrow><mn>25</mn><msub><mi>q</mi><mn>1</mn></msub><msub><mi>q</mi><mn>2</mn></msub></mrow><msup><mfenced><mi>r</mi></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>5</mn><mi>F</mi></math></p>

</details>

---

### Q11. JEE Main 2024 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Two identical charged spheres are suspended by strings of equal lengths. The string make an angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>37</mn><mo>°</mo></math> with each other. When suspended in a liquid of density <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>7</mn><mo> </mo><mi mathvariant="normal">g</mi><mo> </mo><msup><mi>cm</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>, the angle remains same. If density of material of the sphere is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>4</mn><mo> </mo><mi mathvariant="normal">g</mi><mo> </mo><msup><mi>cm</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>, the dielectric constant of the liquid is _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>tan</mi><mn>37</mn><mo>°</mo><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7b33333b-f203-4cf1-b181-c629a462bfdc.png" style="width: 250px; height: 128px;"/></p><p>For first case:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mi>c</mi><mi>o</mi><mi>s</mi><mi>θ</mi><mo>=</mo><mi>m</mi><mi>g</mi></math> and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mi>s</mi><mi>i</mi><mi>n</mi><mi>θ</mi><mo>=</mo><msub><mi>F</mi><mi>e</mi></msub></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mi>a</mi><mi>n</mi><mi>θ</mi><mo>=</mo><mfrac><msub><mi>F</mi><mi>e</mi></msub><mrow><mi>m</mi><mi>g</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mi>a</mi><mi>n</mi><mi>θ</mi><mo>=</mo><mfrac><msub><mi>F</mi><mi>e</mi></msub><mrow><msub><mi>ρ</mi><mi>B</mi></msub><mi>V</mi><mi>g</mi></mrow></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math></p><p>For second case:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mi>a</mi><mi>n</mi><mi>θ</mi><mo>=</mo><mfrac><mfrac><msub><mi>F</mi><mi>e</mi></msub><mi>k</mi></mfrac><mrow><msub><mi>ρ</mi><mi>B</mi></msub><mi>V</mi><mi>g</mi><mo>-</mo><msub><mi>ρ</mi><mi>L</mi></msub><mi>V</mi><mi>g</mi></mrow></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>ii</mi><mo>)</mo></math> </p><p>From Eq. (i) &amp; (ii), we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>ρ</mi><mi>B</mi></msub><mi>V</mi><mi>g</mi><mo>=</mo><mfenced><mrow><msub><mi>ρ</mi><mi>B</mi></msub><mo>-</mo><msub><mi>ρ</mi><mi>L</mi></msub></mrow></mfenced><mi>k</mi><mi>V</mi><mi>g</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>.</mo><mn>4</mn><mo> </mo><mo>=</mo><mo> </mo><mn>0</mn><mo>.</mo><mn>7</mn><mo> </mo><mi>k</mi><mo> </mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>k</mi><mo> </mo><mo>=</mo><mo> </mo><mn>2</mn><mo> </mo></math></p></blockquote>

</details>

---

### Q12. JEE Main 2023 (13 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>Three point charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>,</mo><mo>-</mo><mn>2</mn><mi>q</mi></math>  and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>q</mi></math> are placed on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> axis at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>R</mi></math> respectively from origin as shown. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>cm</mi></math>, the magnitude of net force experienced by the charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>q</mi></math> is _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math>.</p><p style="text-align: center;"><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1d8663ee-7730-41dd-bb85-719dc3433887.png" style="width: 350px; height: 95px;" /></p><p> </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5440**

**Detailed Solution:**

<blockquote><p>The net force on the given charge will be the resultant of the forces due to the other two charges.</p><p>Hence, the net force <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>F</mi><mi>n</mi></msub></mfenced></math> can be calculated as follows:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>F</mi><mi>n</mi></msub></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><mn>4</mn><msup><mi>q</mi><mn>2</mn></msup></mrow><msup><mfenced><mfrac><mi>R</mi><mn>4</mn></mfrac></mfenced><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><mn>2</mn><msup><mi>q</mi><mn>2</mn></msup></mrow><msup><mfenced><mfrac><mrow><mn>3</mn><mi>R</mi></mrow><mn>4</mn></mfrac></mfenced><mn>2</mn></msup></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><mfrac><mrow><mn>16</mn><msup><mi>q</mi><mn>2</mn></msup></mrow><msup><mi>R</mi><mn>2</mn></msup></mfrac><mfenced close="]" open="["><mrow><mn>4</mn><mo>-</mo><mfrac><mn>2</mn><mn>9</mn></mfrac></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><mfrac><mrow><mn>16</mn><mo>&#215;</mo><msup><mfenced><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">C</mi></mrow></mfenced><mn>2</mn></msup></mrow><msup><mfenced><mrow><mn>0</mn><mo>.</mo><mn>02</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>&#215;</mo><mfrac><mn>34</mn><mn>9</mn></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mn>5440</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi></mtd></mtr></mtable></math></p></blockquote>

</details>

---

### Q13. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi><mo>&#160;</mo></math> charge is divided into two parts and placed at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>cm</mi></math> distance so that the repulsive force between them is maximum. The charges of the two parts are:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi><mo>,</mo><mn>3</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi><mo>,</mo><mn>2</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi><mo>,</mo><mn>5</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi><mo>,</mo><mn>1</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi><mo>,</mo><mn>5</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>**

**Detailed Solution:**

<blockquote><p>Let the charges be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mi>&#956;C</mi><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>q</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mi>&#956;C</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi>&#956;C</mi></math></p><p>The force between them is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mfrac><mrow><mi>K</mi><mi>x</mi><mo>(</mo><mi>q</mi><mo>-</mo><mi>x</mi><mo>)</mo></mrow><msup><mi>r</mi><mn>2</mn></msup></mfrac></math>.</p><p>For the force to be maximum,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>F</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><mi>d</mi><mi>F</mi></mstyle><mstyle displaystyle="true"><mi>d</mi><mi>x</mi></mstyle></mfrac><mo>=</mo><mfrac><mrow><mi>K</mi><mo>(</mo><mi>q</mi><mo>-</mo><mn>2</mn><mi>x</mi><mo>)</mo></mrow><msup><mi>r</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mi>q</mi><mn>2</mn></mfrac><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi>&#956;C</mi></math></p></blockquote>

</details>

---

### Q14. JEE Main 2023 (11 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>As shown in the figure, a configuration of two equal point charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>q</mi><mn>0</mn></msub><mo>=</mo><mo>+</mo><mn>2</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></mrow></mfenced></math> is placed on an inclined plane. Mass of each point charge is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">g</mi></math>. Assume that there is no friction between charge and plane. For the system of two point charges to be in equilibrium (at rest) the height <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><mi>x</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>. The value of<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>x</mi></math> is
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mtext>&#160;Take&#160;</mtext><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>,</mo><mo>&#160;</mo><mi>g</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1c41f125-c078-4d15-a66c-46c2ba6a0c57-image.png" style="width: 200px; height: 167px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **300**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e1c06aab-2931-40b8-8aa5-4f670a70f55f-image.png" style="width: 200px; height: 167px;" /></p><p>For the condition of equilibrium, the Coulomb force is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>g</mi><mi>sin</mi><mi>&#952;</mi></math>. Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>k</mi><msup><msub><mi>q</mi><mn>0</mn></msub><mn>2</mn></msup></mrow><mrow><mn>4</mn><msup><mi>h</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mo>(</mo><mi>m</mi><mi>g</mi><mi>sin</mi><mi>&#952;</mi><mo>)</mo><mspace linebreak="newline"/><mo>&#8658;</mo><mfrac><mrow><mi>k</mi><msup><msub><mi>q</mi><mn>0</mn></msub><mn>2</mn></msup></mrow><mrow><mn>4</mn><msup><mi>h</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfenced><mrow><mn>20</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8722;</mo><mn>12</mn></mrow></msup></mrow><mrow><mn>4</mn><msup><mi>h</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>20</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>h</mi><mo>=</mo><mfenced><msqrt><mfrac><mn>9</mn><mn>100</mn></mfrac></msqrt></mfenced><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>=</mo><mn>300</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mn>2</mn></msup><mo>=</mo><mfenced separators="|"><mfrac><mn>9</mn><mn>100</mn></mfrac></mfenced><mo stretchy="false">&#8658;</mo><mi>h</mi><mo>=</mo><mfenced separators="|"><mfrac><mn>3</mn><mn>10</mn></mfrac></mfenced><mi mathvariant="normal">m</mi><mo>=</mo><mn>0</mn><mo>.3</mo><mi mathvariant="normal">m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>300</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8722;</mo><mn>3</mn></mrow></msup><mi mathvariant="normal">m</mi></math></p>

</details>

---

### Q15. JEE Main 2023 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>Experimentally it is found that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>.</mo><mn>8</mn><mo>&#160;</mo><mi>eV</mi></math> energy is required to separate a hydrogen atom into a proton and an electron. So the orbital radius of the electron in a hydrogen atom is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mi>x</mi></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>10</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>.</p><p>The value of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is: _____.</p><p>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>eV</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#160;</mo><mfrac><msup><mi>Nm</mi><mn>2</mn></msup><msup><mi mathvariant="normal">C</mi><mn>2</mn></msup></mfrac></math> and electronic charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">C</mi></math>)</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<blockquote><p>The given data is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn><mo>&#160;</mo></mrow></msup><mi mathvariant="normal">C</mi><mspace linebreak="newline"/><mfrac><mn>1</mn><mrow><mn>4</mn><msub><mi>&#960;&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p>The formula for the value of energy in a hydrogen atom is given by </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><msup><mi>q</mi><mn>2</mn></msup><mrow><mn>8</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>r</mi></mrow></mfrac><mspace linebreak="newline"/><mo>&#8658;</mo><mi>E</mi><mo>=</mo><mfrac><msup><mi>q</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>(</mo><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mo>)</mo><mi>r</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup></mrow><mrow><mn>12</mn><mo>.</mo><mn>8</mn><mo>&#215;</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mn>9</mn><mn>16</mn></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>10</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p>It is given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mfrac><mn>9</mn><mi>x</mi></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>10</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mspace linebreak="newline"/><mo>&#8658;</mo><mfrac><mn>9</mn><mn>16</mn></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>10</mn></mrow></msup><mo>=</mo><mfrac><mn>9</mn><mi mathvariant="normal">x</mi></mfrac><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>10</mn></mrow></msup><mo>&#160;</mo><mspace linebreak="newline"/><mo>&#8658;</mo><mi mathvariant="normal">x</mi><mo>=</mo><mn>16</mn></math></p></blockquote>

</details>

---

### Q16. JEE Main 2023 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

A point charge <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn><msub><mi>q</mi><mn>0</mn></msub></math> is placed at origin. Another point charge <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><msub><mi>q</mi><mn>0</mn></msub></math> is placed at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>12</mn><mo>&#160;</mo><mi>cm</mi></math>. Charge of proton is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>0</mn></msub></math>. The proton is placed on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis so that the electrostatic force on the proton in zero. In this situation, the position of the proton from the origin is ______ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cm</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **24**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/94873610-5ccc-476a-8f4c-c039e13d758b-86a0596d-729d-4d7a-b91d-6053b9d4336e-9894938.png" style="width: 400px; height: 102px;" /></p><p>Let at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> net electric field is zero.</p><p>As direction of electric field due to both charges at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is opposite, equating magnitude we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><mn>4</mn><msub><mi>q</mi><mn>0</mn></msub></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><msub><mi>q</mi><mn>0</mn></msub><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mspace linebreak="newline"/><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mo>=</mo><mi>x</mi><mspace linebreak="newline"/><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>24</mn><mo>&#160;</mo><mi>cm</mi></math></p><p>Distance of proton from origin <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>24</mn><mo>&#160;</mo><mi>cm</mi></math>.</p>

</details>

---

### Q17. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If two charges <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>1</mn></msub></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>2</mn></msub></math> are separated with distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> and placed in a medium of dielectric constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>. What will be the equivalent distance between charges in air for the same electrostatic force?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><msqrt><mi>k</mi></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><msqrt><mi>d</mi></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mi>d</mi><msqrt><mi>k</mi></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>d</mi><msqrt><mi>k</mi></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><msqrt><mi>k</mi></msqrt></math>**

**Detailed Solution:**

<p><span style="font-size:11.0pt"><span style="line-height:107%"><span style="font-family:&quot;Calibri&quot;,sans-serif">The force between the two charges when they are placed in dielectric is</span></span></span></p><p><span style="font-size:11.0pt"><span style="line-height:107%"><span style="font-family:&quot;Calibri&quot;,sans-serif"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mi>o</mi></msub><mi>k</mi></mrow></mfrac><mfrac><mrow><msub><mi>q</mi><mn>1</mn></msub><msub><mi>q</mi><mn>2</mn></msub><mo>&#160;</mo></mrow><msup><mi>d</mi><mn>2</mn></msup></mfrac></math></span></span></span></p><p><span style="font-size:11.0pt"><span style="line-height:107%"><span style="font-family:&quot;Calibri&quot;,sans-serif">The force between the two charges when they are placed at separation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>&#39;</mo></math> is</span></span></span></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mi>o</mi></msub></mrow></mfrac><mfrac><mrow><msub><mi>q</mi><mn>1</mn></msub><msub><mi>q</mi><mn>2</mn></msub><mo>&#160;</mo></mrow><mrow><mi>d</mi><msup><mo>&#39;</mo><mn>2</mn></msup></mrow></mfrac><mo>&#160;</mo></math></p><p>Since, the force between the two charges is same in both case</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>1</mn></msub><mo>=</mo><msub><mi>F</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mi>o</mi></msub><mi>k</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><msub><mi>q</mi><mn>1</mn></msub><msub><mi>q</mi><mn>2</mn></msub><mo>&#160;</mo></mrow><msup><mi>d</mi><mn>2</mn></msup></mfrac><mo>=</mo><mo>&#160;</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mi>o</mi></msub></mrow></mfrac><mo>&#160;</mo><mfrac><mrow><msub><mi>q</mi><mn>1</mn></msub><msub><mi>q</mi><mn>2</mn></msub><mo>&#160;</mo></mrow><mrow><mi>d</mi><msup><mo>&#39;</mo><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>&#39;</mo><mo>=</mo><mi>d</mi><msqrt><mi>k</mi></msqrt></math></p>

</details>

---

### Q18. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two identical metallic spheres <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> when placed at certain distance in air repel each other with a force of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math>. Another identical uncharged sphere <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is first placed in contact with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and then in contact with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and finally placed at midpoint between spheres <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>. The force experienced by sphere <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> will be :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>F</mi></mrow><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>F</mi></mrow><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>F</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>F</mi></mrow><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Let charge on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mi>A</mi></msub><mo>=</mo><msub><mi>q</mi><mi>B</mi></msub><mo>=</mo><mi>q</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c29c0735-6425-4323-a661-1ca8a6df3b90-image.png" style="width: 350px; height: 75px;" /></p><p>Then force acting between them is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mfrac><mrow><mi>K</mi><msup><mi>q</mi><mn>2</mn></msup></mrow><msup><mi>r</mi><mn>2</mn></msup></mfrac></math>.</p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is placed in contact with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>, charge on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>q</mi><mn>2</mn></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is placed in contact with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>, charge on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>  and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>q</mi><mo>+</mo><mfrac><mi>q</mi><mn>2</mn></mfrac></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi>q</mi></mrow><mn>4</mn></mfrac></math></p><p>Now, force experienced by sphere <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c1414dc5-80e0-4523-a570-c0775bc74962-image.png" style="width: 260px; height: 107px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>F</mi><mo>&#39;</mo></msup><mo>=</mo><msub><mi>F</mi><mn>2</mn></msub><mo>-</mo><msub><mi>F</mi><mn>1</mn></msub><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mrow><mi>K</mi><mn>9</mn><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mn>16</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><msup><mi>r</mi><mn>2</mn></msup><mn>4</mn></mfrac></mstyle></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>K</mi><mn>3</mn><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mn>8</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><msup><mi>r</mi><mn>2</mn></msup><mn>4</mn></mfrac></mstyle></mrow></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mfenced><mrow><mi>K</mi><mstyle displaystyle="true"><mfrac><mrow><mn>3</mn><mi>q</mi></mrow><mn>4</mn></mfrac></mstyle><mo>-</mo><mi>K</mi><mstyle displaystyle="true"><mfrac><mi>q</mi><mn>2</mn></mfrac></mstyle></mrow></mfenced><mstyle displaystyle="true"><mfrac><msup><mi>r</mi><mn>2</mn></msup><mn>4</mn></mfrac></mstyle></mfrac><mo>&#215;</mo><mfrac><mrow><mn>3</mn><mi>q</mi></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>3</mn><mi>K</mi><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mn>4</mn><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#160;</mo><mi>F</mi></mrow><mn>4</mn></mfrac></math></p></blockquote>

</details>

---

### Q19. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A charge of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> is to be divided into two. The distance between the two divided charges is constant. The magnitude of the divided charges so that the force between them is maximum, will be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>5</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/70f8853f-3bd4-4361-be42-7e7ed394782e-image.png" style="width: 300px; height: 51px;" /></p><p>If after division, one of the charge is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> the other charge will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>-</mo><mi>q</mi></mrow></mfenced></math>. The force between them can be written as,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mfrac><mrow><mi>K</mi><mi>q</mi><mfenced><mrow><mn>4</mn><mo>-</mo><mi>q</mi></mrow></mfenced></mrow><msup><mi>d</mi><mn>2</mn></msup></mfrac></math></p><p>For the force between them to be maximum,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">d</mi><mi>F</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>q</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfrac><mi>K</mi><msup><mi>d</mi><mn>2</mn></msup></mfrac><mfenced close="]" open="["><mrow><mn>4</mn><mo>-</mo><mn>2</mn><mi>q</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>q</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>&#956;C</mi></math></p></blockquote>

</details>

---

### Q20. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two identical positive charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> each are fixed at a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi></math> apart from each other. Another point charge <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>0</mn></msub></math> with mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is placed at midpoint between two fixed charges. For a small displacement along the line joining the fixed charges, the charge <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>0</mn></msub></math> executes SHM. The time period of oscillation of charge <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>0</mn></msub></math> will be

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mrow><mn>4</mn><msup><mi>&#960;</mi><mn>3</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>a</mi><mn>3</mn></msup></mrow><mrow><msub><mi>q</mi><mn>0</mn></msub><mi>Q</mi></mrow></mfrac></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mrow><msub><mi>q</mi><mn>0</mn></msub><mi>Q</mi></mrow><mrow><mn>4</mn><msup><mi>&#960;</mi><mn>3</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>a</mi><mn>3</mn></msup></mrow></mfrac></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mrow><mn>2</mn><msup><mi>&#960;</mi><mn>2</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>a</mi><mn>3</mn></msup></mrow><mrow><msub><mi>q</mi><mn>0</mn></msub><mi>Q</mi></mrow></mfrac></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mrow><mn>8</mn><msup><mi>&#960;</mi><mn>3</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>a</mi><mn>3</mn></msup></mrow><mrow><msub><mi>q</mi><mn>0</mn></msub><mi>Q</mi></mrow></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mrow><mn>4</mn><msup><mi>&#960;</mi><mn>3</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>a</mi><mn>3</mn></msup></mrow><mrow><msub><mi>q</mi><mn>0</mn></msub><mi>Q</mi></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c4cc5ffd-4e6c-4bd7-967f-6091be0cf637-1b833bce-44a7-4fda-bf61-d9df17d1fa51-image.png" style="width: 250px; height: 125px;" /></p><p>Let the charged particle be displaced slightly towards right by distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><mi>x</mi><mo>&#8810;</mo><mi>d</mi></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>Q</mi><mo>&#160;</mo><mi>a</mi><mi>t</mi><mo>&#160;</mo><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>q</mi></mrow></mfenced><mo>:</mo><msub><mi>F</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><mi>Q</mi><mi>q</mi></mrow><msup><mfenced><mrow><mi>d</mi><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac></math>, towards right</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>Q</mi><mo>&#160;</mo><mtext>at</mtext><mo>&#160;</mo><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>q</mi></mrow></mfenced><mo>:</mo><mo>&#160;</mo><msub><mi>F</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><mi>Q</mi><mi>q</mi></mrow><msup><mfenced><mrow><mi>d</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac></math>, towards left</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><msub><mover><mi>F</mi><mo>&#8594;</mo></mover><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>=</mo><msub><mover><mi>F</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>+</mo><msub><mover><mi>F</mi><mo>&#8594;</mo></mover><mn>2</mn></msub></math>, will bring it towards <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math>.<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>F</mi><mo>&#8594;</mo></mover><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><msup><mstyle displaystyle="true"><mfenced><mrow><mi>d</mi><mo>+</mo><mi>x</mi></mrow></mfenced></mstyle><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><msup><mfenced><mrow><mi>d</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mi>Q</mi><mi>q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mfenced close="]" open="["><mfrac><mrow><mn>4</mn><mi>x</mi><mi>d</mi></mrow><msup><mfenced><mrow><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac></mfenced><mover><mi>i</mi><mo>^</mo></mover></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8810;</mo><mi>d</mi><mo>,</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup></math> is negligible.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>F</mi><mo>&#8594;</mo></mover><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>=</mo><mo>-</mo><mfenced><mfrac><mrow><mi>Q</mi><mi>q</mi></mrow><mrow><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><msup><mi>d</mi><mn>3</mn></msup></mrow></mfrac></mfenced><mo>&#215;</mo><mi>x</mi><mover><mi>i</mi><mo>^</mo></mover></math></p><p>Clearly, the direction of the force is opposite to the displacement &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>&#8733;</mo><mi>x</mi></math>, hence it is an SHM.</p><p>Acceleration of charged particle is given as,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mi>F</mi><mi>m</mi></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mi>Q</mi><mi>q</mi></mrow><mrow><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>d</mi><mn>3</mn></msup></mrow></mfrac><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And we know that for SHM,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Comparing <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><msqrt><mfrac><mrow><mi>Q</mi><mi>q</mi></mrow><mrow><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>d</mi><mn>3</mn></msup></mrow></mfrac></msqrt></math></p><p>Hence, the time period, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mi>&#969;</mi></mfrac><mo>=</mo><mn>2</mn><mi>&#960;</mi><msqrt><mfrac><mrow><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>d</mi><mn>3</mn></msup></mrow><mrow><mi>Q</mi><mi>q</mi></mrow></mfrac></msqrt></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><msqrt><mfrac><mrow><mn>4</mn><msup><mi>&#960;</mi><mn>3</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>a</mi><mn>3</mn></msup></mrow><mrow><msub><mi>q</mi><mn>0</mn></msub><mi>Q</mi></mrow></mfrac></msqrt></math></p></blockquote>

</details>

---

### Q21. JEE Main 2022 (26 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Three point charges of magnitude <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>.</mo><mn>16</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>3</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> are located at the vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi></math> of a right angled triangle whose sides are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>cm</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>&#160;</mo><mi>cm</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>A</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>cm</mi></math> and point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is the right angle corner. Charge at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> experiences _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> of electrostatic force due to the other two charges.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/704fc0c2-9e82-45df-b603-d73ee1f9042a-image.png" style="width: 200px; height: 156px;" /></p><p>Using Coulomb&#39;s law the electrostatic force on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> due to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mrow><mi>A</mi><mi>C</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>K</mi><msub><mi>q</mi><mi>A</mi></msub><msub><mi>q</mi><mi>C</mi></msub></mrow><msup><mfenced><msub><mi>r</mi><mrow><mi>A</mi><mi>C</mi></mrow></msub></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>12</mn></mrow></msup></mrow><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup></mrow></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>12</mn></mrow></msup></mrow><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi></math></p><p>Similarly, the force on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> due to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mrow><mi>A</mi><mi>B</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>K</mi><msub><mi>q</mi><mi>A</mi></msub><msub><mi>q</mi><mi>B</mi></msub></mrow><msup><mfenced><msub><mi>r</mi><mrow><mi>A</mi><mi>B</mi></mrow></msub></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>16</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>12</mn></mrow></msup></mrow><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi></math></p><p>We can see that the forces are perpendicular to each other. Therefore, the net force experienced by charge at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><msqrt><msup><msub><mi>F</mi><mrow><mi>A</mi><mi>C</mi></mrow></msub><mn>2</mn></msup><mo>+</mo><msup><msub><mi>F</mi><mrow><mi>A</mi><mi>B</mi></mrow></msub><mn>2</mn></msup></msqrt></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><msup><mn>15</mn><mn>2</mn></msup><mo>+</mo><msup><mn>8</mn><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>289</mn></msqrt><mo>=</mo><mn>17</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi></math></p></blockquote>

</details>

---

### Q22. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two point charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> each are placed at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> apart. A third point charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> is placed at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> from mid-point on the perpendicular bisector. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> at which charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> will experience the maximum Coulomb&#39;s force is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/25284b10-22d6-400c-9e5e-424dbd9ad6ad-image.png" style="width: 230px; height: 240px;" /></p><p>The distance between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mi>d</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><msup><mi>d</mi><mn>2</mn></msup><mn>4</mn></mfrac></msqrt></math>.</p><p>The force between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi><mi>Q</mi></mrow><msup><mi>r</mi><mn>2</mn></msup></mfrac></math>.</p><p>From the given figure we can see that only vertical components of the forces will add, and the horizontal components will get cancelled out. Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi><mi>q</mi><mi>Q</mi></mrow><msup><mi>r</mi><mn>2</mn></msup></mfrac><mi>cos</mi><mi>&#952;</mi><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi><mi>q</mi><mi>Q</mi></mrow><msup><mi>r</mi><mn>2</mn></msup></mfrac><mo>&#215;</mo><mfrac><mi>x</mi><mi>r</mi></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi><mi>Q</mi><mi>x</mi></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mstyle displaystyle="true"><mfrac><msup><mi>d</mi><mn>2</mn></msup><mn>4</mn></mfrac></mstyle></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup></mfrac></math></p><p>For force to be maximum, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>d</mo><msub><mi>F</mi><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub></mrow><mrow><mo>d</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mi>q</mi><mi>Q</mi><mfenced close="]" open="["><mfrac><mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><msup><mi>d</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>-</mo><mi>x</mi><mo>&#215;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><msup><mi>d</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>&#215;</mo><mn>2</mn><mi>x</mi></mrow><msup><mfenced><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><msup><mi>d</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mfenced><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><msup><mi>d</mi><mn>2</mn></msup><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>&#8658;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mfrac><msup><mi>d</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mi>d</mi><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p>

</details>

---

### Q23. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Three identical charged balls each of charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>C</mi></math> are suspended from a common point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> by silk threads of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> each (as shown in figure). They form an equilateral triangle of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>.</p><p>The ratio of net force on a charged ball to the force between any two charged balls will be</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/69ba51c5-2f6a-4539-a554-cfb5cc748e71-image.png" style="width: 300px; height: 212px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mo>:</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mo>:</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mo>:</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c8be4247-8bbb-4c40-a00b-ece9bb5d5cad-image.png" style="width: 170px; height: 154px;" /></p><p>We have force between any two charge<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><msub><mi>F</mi><mn>1</mn></msub><mo>=</mo><msub><mi>F</mi><mn>2</mn></msub><mo>=</mo><mfrac><msup><mi>q</mi><mn>2</mn></msup><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>l</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mi>F</mi></math></p><p>Resultant electrostatics force <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mi>R</mi></msub><mo>=</mo><msqrt><msubsup><mi>F</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>F</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><mn>2</mn><msub><mi>F</mi><mn>1</mn></msub><msub><mi>F</mi><mn>2</mn></msub><mi>cos</mi><mn>60</mn><mo>&#176;</mo></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><msup><mi>F</mi><mn>2</mn></msup><mo>+</mo><msup><mi>F</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>2</mn><msup><mi>F</mi><mn>2</mn></msup><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></msqrt><mo>=</mo><msqrt><mn>3</mn><msup><mi>F</mi><mn>2</mn></msup></msqrt></math></p><p>So, the ratio of net force on a charged ball to the force between any charged balls is </p><p>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>F</mi><mi>R</mi></msub><mi>F</mi></mfrac><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p>

</details>

---

### Q24. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Sixty four conducting drops each of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>02</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> and each carrying a charge of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> are combined to form a bigger drop. The ratio of surface density of bigger drop to the smaller drop will be

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>:</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>:</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>:</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Total volume will be constant. Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><msup><mi>r</mi><mn>3</mn></msup></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><msup><mi>R</mi><mn>3</mn></msup><mo>&#8658;</mo><msup><mn>64</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mi>r</mi><mo>=</mo><mi>R</mi><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mn>4</mn><mi>r</mi></math></p><p>Final surface charge density <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mo>&#39;</mo></msup><mo>=</mo><mfrac><mrow><mi>n</mi><msub><mi>&#963;</mi><mn>0</mn></msub><mn>4</mn><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup></mrow><mrow><mn>4</mn><mi>&#960;</mi><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>64</mn><mo>&#215;</mo><msub><mi>&#963;</mi><mn>0</mn></msub><msup><mi>r</mi><mn>2</mn></msup></mrow><mrow><mn>16</mn><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac><mo>&#8658;</mo><mfrac><msup><mi>&#963;</mi><mo>&#39;</mo></msup><msub><mi>&#963;</mi><mn>0</mn></msub></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>1</mn></mfrac></math></p>

</details>

---

### Q25. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Two identical charged particles each having a mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">g</mi></math> and charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mi mathvariant="normal">C</mi></math> are placed on a horizontal table with a separation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> between them such that they stay in limited equilibrium. If the coefficient of friction between each particle and the table is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>25</mn></math>, find the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math>. [Use <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mo>=</mo><mn>10</mn><msup><mrow><mo>&#160;</mo><mi>ms</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> ]

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi>cm</mi></math>**

**Detailed Solution:**

<p>Normal reaction applied by table on object will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><mi>m</mi><mi>g</mi></math>.</p><p>Both charges are same, hence a repulsive force will act between them.</p><p>Value of force acting will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>k</mi><msup><mi>Q</mi><mn>2</mn></msup></mrow><msup><mi>L</mi><mn>2</mn></msup></mfrac></math>.</p><p>Now the maximum value of friction force which table can provide is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#956;</mi><mi>N</mi><mo>=</mo><mi>&#956;</mi><mi>m</mi><mi>g</mi></math></p><p>For equilibrium, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>k</mi><msup><mi>Q</mi><mn>2</mn></msup></mrow><msup><mi>L</mi><mn>2</mn></msup></mfrac><mo>=</mo><mi>&#956;</mi><mi>m</mi><mi>g</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><msqrt><mfrac><mrow><mi>k</mi><msup><mi>Q</mi><mn>2</mn></msup></mrow><mrow><mi>&#956;</mi><mi>m</mi><mi>g</mi></mrow></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mi>k</mi><mrow><mn>0</mn><mo>.</mo><mn>25</mn><mi>m</mi><mi>g</mi></mrow></mfrac></msqrt><mi>Q</mi><mo>=</mo><mn>2</mn><msqrt><mfrac><mi>k</mi><mrow><mi>m</mi><mi>g</mi></mrow></mfrac></msqrt><mi>Q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msqrt><mfrac><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup></mrow><mrow><mn>10</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#215;</mo><mn>10</mn></mrow></mfrac></msqrt><mfenced><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup></mrow></mfenced><mo>=</mo><mn>0</mn><mo>.</mo><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>=</mo><mn>12</mn><mo>&#160;</mo><mi>cm</mi></math></p>

</details>

---

### Q26. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The relative permittivity of distilled water is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>81</mn><mo>.</mo></math> The velocity of light in it will be: <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo></math>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open=""><mrow><msub><mi>&#956;</mi><mi mathvariant="normal">r</mi></msub><mo>=</mo><mn>1</mn></mrow></mfenced></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo><mn>33</mn><mo>&#215;</mo><msup><mn>10</mn><mn>7</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>33</mn><mo>&#215;</mo><msup><mn>10</mn><mn>7</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>33</mn><mo>&#215;</mo><msup><mn>10</mn><mn>7</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>.</mo><mn>33</mn><mo>&#215;</mo><msup><mn>10</mn><mn>7</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>33</mn><mo>&#215;</mo><msup><mn>10</mn><mn>7</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mi>c</mi><msqrt><msub><mi mathvariant="normal">&#956;</mi><mi>r</mi></msub><msub><mi mathvariant="normal">&#949;</mi><mi>r</mi></msub></msqrt></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>.</mo><mn>33</mn><mo>&#215;</mo><msup><mn>10</mn><mn>7</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

</details>

---

### Q27. JEE Main 2021 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>A particle of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>mg</mi></math> and charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> is lying at the mid-point of two stationary particles kept at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> when each is carrying same charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math>. If the free charged particle is displaced from its equilibrium position through distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>&#60;</mo><mo>&#60;</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></mrow></mfenced></math>. The particle executes SHM. Its angular frequency of oscillation will be _______ <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> (if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>q</mi><mn>2</mn></msup><mo>=</mo><mn>10</mn><msup><mi>C</mi><mn>2</mn></msup></math>)</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6000**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/81c76b28-9126-414d-b87a-12111b970e44-image.png" style="width: 238px; height: 97px;" /></p><p>Net force on free charged particle, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mfrac><mrow><mi>k</mi><msup><mi>q</mi><mn>2</mn></msup></mrow><msup><mfenced><mrow><mi>d</mi><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mrow><mi>k</mi><msup><mi>q</mi><mn>2</mn></msup></mrow><msup><mfenced><mrow><mi>d</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mo>-</mo><mi>k</mi><msup><mi>q</mi><mn>2</mn></msup><mfenced close="]" open="["><mfrac><mrow><mn>4</mn><mi>d</mi><mi>x</mi></mrow><msup><mfenced><mrow><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>4</mn><mi>k</mi><msup><mi>q</mi><mn>2</mn></msup><mi>d</mi></mrow><mi>m</mi></mfrac><mfenced><mfrac><mi>x</mi><msup><mi>d</mi><mn>4</mn></msup></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mfenced><mfrac><mrow><mn>4</mn><mi>k</mi><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mi>m</mi><msup><mi>d</mi><mn>3</mn></msup></mrow></mfrac></mfenced><mi>x</mi></math></p><p>So, angular frequency </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><msqrt><mfrac><mrow><mn>4</mn><mo>&#160;</mo><mi>k</mi><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mi>m</mi><msup><mi>d</mi><mn>3</mn></msup></mrow></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><msqrt><mfrac><mrow><mn>4</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><mn>10</mn></mrow><mrow><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo>&#215;</mo><msup><mn>1</mn><mn>3</mn></msup></mrow></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mn>8</mn></msup><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p>

</details>

---

### Q28. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A certain charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is divided into two parts <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>Q</mi><mo>-</mo><mi>q</mi><mo>)</mo><mo>.</mo></math> How should the charges <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> be divided so that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>Q</mi><mo>-</mo><mi>q</mi><mo>)</mo></math> placed at a certain distance apart experience maximum electrostatic repulsion?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfrac><mi>q</mi><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mn>2</mn><mi>q</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mn>4</mn><mi>q</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mn>3</mn><mi>q</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mn>2</mn><mi>q</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7ec565f6-baf1-4df0-bae4-4bcb4ebfc1db-image.png" style="width: 356px; height: 101px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mi mathvariant="normal">q</mi></msub><mo>=</mo><mfrac><mrow><mi>k</mi><mi>q</mi><mo>(</mo><mi>Q</mi><mo>-</mo><mi>q</mi><mo>)</mo></mrow><msup><mi>L</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mi>k</mi><msup><mi>L</mi><mn>2</mn></msup></mfrac><mfenced><mrow><mi>q</mi><mi>Q</mi><mo>-</mo><msup><mi>q</mi><mn>2</mn></msup></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mtext>d</mtext><mi>F</mi></mrow><mrow><mtext>d</mtext><mi>q</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math> when force is maximum
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mtext>d</mtext><mi>F</mi></mrow><mrow><mtext>d</mtext><mi>q</mi></mrow></mfrac><mo>=</mo><mfrac><mi>k</mi><msup><mi>L</mi><mn>2</mn></msup></mfrac><mo>[</mo><mi>Q</mi><mo>-</mo><mn>2</mn><mi>q</mi><mo>]</mo><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Q</mi><mo>-</mo><mn>2</mn><mi>q</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>Q</mi><mo>=</mo><mn>2</mn><mi>q</mi></math></p>

</details>

---

### Q29. JEE Main 2021 (18 Mar Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>An infinite number of point charges, each carrying <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi></math> charge, are placed along the y-axis at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>,</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>,</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>,</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mo>.</mo></math></p><p>The total force on a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">C</mi></math> point charge, placed at the origin, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, to the nearest integer, is ___ .</p><p>[Take <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>]</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8d2ec4b9-60c2-46bb-b6cf-8bbc96eba00a-image.png" style="width: 356px; height: 105px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>k</mi><mfenced><mrow><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">C</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>&#160;</mo><mi>&#956;</mi><mi mathvariant="normal">C</mi></mrow></mfenced><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>4</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>8</mn><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mfenced close="]" open="["><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfrac></mfenced><mo>=</mo><mn>12</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi></math></p>

</details>

---

### Q30. JEE Main 2021 (25 Feb Shift 2)

*Type:* `numerical` | *Level:* `1`

Two identical conducting spheres with negligible volume have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>1</mn><mo>&#160;</mo><mi>nC</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#160;</mo><mi>nC</mi></math> charges, respectively. They are brought into contact and then separated by a distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>. The electrostatic force acting between the spheres is ___<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi></math>.
[Given : <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup></mrow></mfrac></math> SI unit]

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mfenced><mrow><mn>2</mn><mo>.</mo><mn>1</mn><mo>-</mo><mn>0</mn><mo>.</mo><mn>1</mn></mrow></mfenced><mn>2</mn></mfrac><mo>&#160;</mo><mi>nC</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi>nC</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>=</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>9</mn></msup><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>18</mn></mrow></msup></mrow><msup><mfenced><mrow><mn>0</mn><mo>.</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>36</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup></math></p>

</details>

---

### Q31. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Two electrons each are fixed at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>d</mi><mo>.</mo></math> A third charge proton placed at the midpoint is displaced slightly by a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><mi>x</mi><mo>&#8810;</mo><mi>d</mi></mrow></mfenced></math> perpendicular to the line joining the two fixed charges. Proton will execute simple harmonic motion having angular frequency:
(<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo></math> mass of charged particle)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>d</mi><mn>3</mn></msup></mrow><mrow><mn>2</mn><msup><mi>q</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>d</mi><mn>3</mn></msup></mrow><msup><mi>q</mi><mn>2</mn></msup></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><msup><mi>q</mi><mn>2</mn></msup><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>d</mi><mn>3</mn></msup></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><mn>2</mn><msup><mi>q</mi><mn>2</mn></msup></mrow><mrow><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>d</mi><mn>3</mn></msup></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><msup><mi>q</mi><mn>2</mn></msup><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>d</mi><mn>3</mn></msup></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math>**

**Detailed Solution:**

<p>From the given condition, we have</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/712b0155-af92-4106-9552-23fa5edaaca6-image.png" style="width: 254px; height: 100px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mrow><mi>net</mi><mo>&#160;</mo><mi mathvariant="normal">q</mi></mrow></msub><mo>=</mo><mo>-</mo><mfenced close="]" open="["><mrow><mn>2</mn><msub><mi>F</mi><mrow><mi>q</mi><mo>/</mo><mi>q</mi></mrow></msub><mi>cos</mi><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mrow><mi>net</mi><mo>&#160;</mo><mi mathvariant="normal">q</mi></mrow></msub><mo>=</mo><mo>-</mo><mn>2</mn><mo>&#183;</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>&#183;</mo><mfrac><msup><mi>q</mi><mn>2</mn></msup><msup><mfenced><msqrt><msup><mi>d</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfenced><mn>2</mn></msup></mfrac><mo>&#183;</mo><mfrac><mi>x</mi><msqrt><msup><mi>d</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><msup><mi>q</mi><mn>2</mn></msup><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mi>x</mi><msup><mfenced><mrow><msup><mi>d</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mo>&#60;</mo><mi>d</mi><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mrow><mi>net</mi><mo>&#160;</mo><mi>q</mi></mrow></msub><mo>=</mo><mo>-</mo><mfrac><msup><mi>q</mi><mn>2</mn></msup><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mo>&#160;</mo><msup><mi>d</mi><mn>3</mn></msup></mrow></mfrac><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi>q</mi><mn>2</mn></msup><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mo>&#183;</mo><mi>m</mi><msup><mi>d</mi><mn>3</mn></msup></mrow></mfrac><mi>x</mi></math></p><p>Comparing with equation of SHM <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>=</mo><mo>-</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#969;</mi><mo>=</mo><msqrt><mfrac><msup><mi>q</mi><mn>2</mn></msup><mrow><mn>2</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>m</mi><msup><mi>d</mi><mn>3</mn></msup></mrow></mfrac></msqrt></math></p>

</details>

---

### Q32. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider the force <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">F</mi></math> on a charge &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">q</mi></math>&#39; due to a uniformly charged spherical shell of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math> carrying charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Q</mi></math> distributed uniformly over it. Which one of the following statements is true for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">F</mi></math>, if  &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">q</mi></math>&#39; is placed at distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">r</mi></math> from the centre of the shell?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">F</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub></mrow></mfrac><mfrac><mi>Qq</mi><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup></mfrac></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">r</mi><mo>&#60;</mo><mi mathvariant="normal">R</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub></mrow></mfrac><mfrac><mi>qQ</mi><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup></mfrac><mo>&#62;</mo><mi mathvariant="normal">F</mi><mo>&#62;</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">r</mi><mo>&#60;</mo><mi mathvariant="normal">R</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">F</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub></mrow></mfrac><mfrac><mi>Qq</mi><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mfrac></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">r</mi><mo>&#62;</mo><mi mathvariant="normal">R</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">F</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub></mrow></mfrac><mfrac><mi>Qq</mi><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mfrac></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">r</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">F</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub></mrow></mfrac><mfrac><mi>Qq</mi><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mfrac></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">r</mi><mo>&#62;</mo><mi mathvariant="normal">R</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/99143aa1-6111-40a1-bad6-0e6a593b092c-image.png" style="width: 315px; height: 194px;" />  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">E</mi><mo>=</mo><mi mathvariant="normal">O</mi><mo>,</mo><mtext>&#8201;</mtext><mi mathvariant="normal">r</mi><mo>&#60;</mo><mi mathvariant="normal">R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>qQ</mi><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mfrac><mo>,</mo><mtext>&#8201;</mtext><mi mathvariant="normal">r</mi><mo>&#8805;</mo><mi mathvariant="normal">R</mi></math></p><p>Inside <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">F</mi><mo>=</mo><mn>0</mn></math> and outside sphare</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">F</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>Qq</mi></mrow><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow></mfrac></math></p><p> </p>

</details>

---

### Q33. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>A solid sphere of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> carries a charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>+</mo><mi>q</mi></math> distributed uniformly over its volume. A very small point like piece of it of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> gets detached from the bottom of the sphere and falls down vertically under gravity. This piece carries charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math>. If it acquires a speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#957;</mi></math> when it has fallen through a vertical height <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> (see figure), then (assume the remaining portion to be spherical)</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/edf411e1-ddef-47bd-a95c-53c89161b690-image.png" style="width: 147px; height: 248px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>v</mi><mn>2</mn></msup><mo>=</mo><mi>y</mi><mfenced open="[" close="]"><mrow><mfrac><mrow><mi>q</mi><mi>Q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><msup><mi>R</mi><mn>2</mn></msup><mi>y</mi><mi>m</mi></mrow></mfrac><mo>+</mo><mi>g</mi></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>v</mi><mn>2</mn></msup><mo>=</mo><mi>y</mi><mfenced open="[" close="]"><mrow><mfrac><mrow><mi>q</mi><mi>Q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><mi>R</mi><mo>(</mo><mi>R</mi><mo>+</mo><mi>y</mi><mo>)</mo><mi>m</mi></mrow></mfrac><mo>+</mo><mi>g</mi></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>v</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>y</mi><mfenced open="[" close="]"><mrow><mfrac><mrow><mi>Q</mi><mi>q</mi><mi>R</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub><mo>(</mo><mi>R</mi><mo>+</mo><mi>y</mi><msup><mo>)</mo><mn>3</mn></msup><mi>m</mi></mrow></mfrac><mo>+</mo><mi>g</mi></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>v</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>y</mi><mfenced open="[" close="]"><mrow><mfrac><mrow><mi>q</mi><mi>Q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>R</mi><mo>(</mo><mi>R</mi><mo>+</mo><mi>y</mi><mo>)</mo><mi>m</mi></mrow></mfrac><mo>+</mo><mi>g</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>v</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>y</mi><mfenced open="[" close="]"><mrow><mfrac><mrow><mi>q</mi><mi>Q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>R</mi><mo>(</mo><mi>R</mi><mo>+</mo><mi>y</mi><mo>)</mo><mi>m</mi></mrow></mfrac><mo>+</mo><mi>g</mi></mrow></mfenced></math>**

**Detailed Solution:**

<p>By using total energy conservation
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>KE</mi><mo>+</mo><mo>(</mo><mi>&#916;</mi><mi>PE</mi><msub><mo>)</mo><mtext>electo</mtext></msub><mtext>&#160;</mtext><mo>+</mo><mo>(</mo><mi>&#916;</mi><mi>PE</mi><msub><mo>)</mo><mtext>gravitation</mtext></msub><mtext>&#160;</mtext><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>m</mi><msup><mi>V</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mi>k</mi><mfrac><mrow><mi>Q</mi><mi>q</mi></mrow><mrow><mi>R</mi><mo>+</mo><mi>y</mi></mrow></mfrac><mo>-</mo><mi>k</mi><mfrac><mrow><mi>Q</mi><mi>q</mi></mrow><mi>R</mi></mfrac></mrow></mfenced><mo>+</mo><mo>(</mo><mo>-</mo><mi>m</mi><mi>g</mi><mi>y</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>m</mi><msup><mi>V</mi><mn>2</mn></msup><mo>=</mo><mi>m</mi><mi>g</mi><mi>y</mi><mo>+</mo><mi>k</mi><mi>Q</mi><mi>q</mi><mfenced><mrow><mfrac><mn>1</mn><mi>R</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>R</mi><mo>+</mo><mi>y</mi></mrow></mfrac></mrow></mfenced><mo>;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>V</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>g</mi><mi>y</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi>k</mi><mi>Q</mi><mi>q</mi></mrow><mi>m</mi></mfrac><mfrac><mi>y</mi><mrow><mi>R</mi><mo>(</mo><mi>R</mi><mo>+</mo><mi>y</mi><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>V</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>y</mi><mfenced close="]" open="["><mrow><mfrac><mrow><mi>q</mi><mi>Q</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub><mi>R</mi><mo>(</mo><mi>R</mi><mo>+</mo><mi>y</mi><mo>)</mo><mi>m</mi></mrow></mfrac><mo>+</mo><mi>g</mi></mrow></mfenced></math></p>

</details>

---

### Q34. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two isolated conducting spheres <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>R</mi></math> have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi></math> charges, respectively, and are at a large distance from each other, They are now connected by a conducting wire. A long time after this is done the charges on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> are respectively:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;</mo><mi>both</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mn>4</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mo>-</mo><mn>4</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo mathvariant="italic">&#160;</mo><mi>&#956;</mi><mi>C</mi><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mn>6</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi></math>**

**Detailed Solution:**

<blockquote><p>Total charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>12</mn><mo>-</mo><mn>3</mn><mo>=</mo><mn>9</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi></math></p><p>If final charges are <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi mathvariant="normal">q</mi><mn>1</mn></msub><msub><mi mathvariant="normal">q</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><msub><mi mathvariant="normal">R</mi><mn>1</mn></msub><msub><mi mathvariant="normal">R</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mn>1</mn></msub><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>&#956;</mi><mi>C</mi></math></p></blockquote>

</details>

---

### Q35. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>A charge Q is distributed over two concentric conducting thin spherical shells radii <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">r</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>&#160;</mo><mfenced><mrow><mi mathvariant="normal">R</mi><mo>&#62;</mo><mi mathvariant="normal">r</mi></mrow></mfenced></math>. If the surface charge densities on the two shells are equal, the electric potential at the common centre is : </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6f6a31b5-33af-4e16-aed3-4688f0f05d64-image.png" style="width: 140px; height: 137px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><msub><mi>&#960;&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mfenced><mrow><mi mathvariant="normal">R</mi><mo>+</mo><mi mathvariant="normal">r</mi></mrow></mfenced><mrow><mn>2</mn><mfenced><mrow><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac><mi mathvariant="normal">Q</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><msub><mi>&#960;&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mfenced><mrow><mn>2</mn><mi mathvariant="normal">R</mi><mo>+</mo><mi mathvariant="normal">r</mi></mrow></mfenced><mfenced><mrow><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mi mathvariant="normal">Q</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><msub><mi>&#960;&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><mfenced><mrow><mi mathvariant="normal">R</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">r</mi></mrow></mfenced><mi mathvariant="normal">Q</mi></mrow><mrow><mn>2</mn><mfenced><mrow><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><msub><mi>&#960;&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><mo>(</mo><mi mathvariant="normal">R</mi><mo>+</mo><mi mathvariant="normal">r</mi><mo>)</mo></mrow><mfenced><mrow><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mi mathvariant="normal">Q</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><msub><mi>&#960;&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><mrow><mo>(</mo><mi mathvariant="normal">R</mi><mo>+</mo><mi mathvariant="normal">r</mi><mo>)</mo></mrow><mfenced><mrow><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mi mathvariant="normal">Q</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c49c1fb6-4884-41b2-8fcd-a76faa00fee0-image.png" style="width: 125px; height: 141px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Q</mi><mn>1</mn></msub><mo>=</mo><mi mathvariant="normal">&#963;</mi><mn>4</mn><msup><mi>&#960;r</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Q</mi><mn>2</mn></msub><mo>=</mo><mi mathvariant="normal">&#963;</mi><mn>4</mn><msup><mi>&#960;r</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mo mathvariant="italic">&#8756;</mo></mtd><mtd><mi mathvariant="italic">Q</mi><mo mathvariant="italic">=</mo><mi mathvariant="italic">&#963;</mi><mn mathvariant="italic">4</mn><mi mathvariant="italic">&#960;</mi><mfenced><mrow><msup><mi mathvariant="italic">r</mi><mn mathvariant="italic">2</mn></msup><mo mathvariant="italic">+</mo><msup><mi mathvariant="italic">R</mi><mn mathvariant="italic">2</mn></msup></mrow></mfenced></mtd></mtr><mtr><mtd><mo mathvariant="italic">&#8756;</mo><mo mathvariant="italic">&#160;&#160;</mo></mtd><mtd><mi mathvariant="italic">&#963;</mi><mo mathvariant="italic">=</mo><mfrac><mi mathvariant="italic">Q</mi><mrow><mn mathvariant="italic">4</mn><mi mathvariant="italic">&#960;</mi><mfenced><mrow><msup><mi mathvariant="italic">r</mi><mn mathvariant="italic">2</mn></msup><mo mathvariant="italic">+</mo><msup><mi mathvariant="italic">R</mi><mn mathvariant="italic">2</mn></msup></mrow></mfenced></mrow></mfrac></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">C</mi></msub><mo>=</mo><mfrac><msub><mi>KQ</mi><mn>1</mn></msub><mi mathvariant="normal">r</mi></mfrac><mo>+</mo><mfrac><msub><mi>KQ</mi><mn>2</mn></msub><mi mathvariant="normal">R</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msub><mi mathvariant="normal">K</mi><mn>0</mn></msub><mn>4</mn><msup><mi>&#960;r</mi><mn>2</mn></msup></mrow><mi mathvariant="normal">r</mi></mfrac><mo>+</mo><mfrac><mrow><msub><mi mathvariant="normal">K</mi><mn>0</mn></msub><mn>4</mn><msup><mi>&#960;R</mi><mn>2</mn></msup></mrow><mi mathvariant="normal">R</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>KQ</mi><mn>4</mn><mi mathvariant="normal">&#960;</mi><mo>(</mo><mi mathvariant="normal">r</mi><mo>+</mo><mi mathvariant="normal">R</mi><mo>)</mo></mrow><mrow><mn>4</mn><mi mathvariant="normal">&#960;</mi><mfenced><mrow><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>KQ</mi><mo>(</mo><mi mathvariant="normal">r</mi><mo>+</mo><mi mathvariant="normal">R</mi><mo>)</mo></mrow><mfenced><mrow><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">R</mi><mn>2</mn></msup></mrow></mfenced></mfrac></math></p><p> </p>

</details>

---

### Q36. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Charge is distributed within a sphere of radius <math><mi>R</mi></math> with a volume charge density <math><mi>&#961;</mi><mfenced separators="|"><mrow><mi>r</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>A</mi></mrow><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>2</mn><mi>r</mi></mrow><mrow><mi>a</mi></mrow></mfrac></mrow></msup><mo>,</mo></math> where <math><mi>A</mi></math> and <math><mi>a</mi></math> are constants. If <math><mi>Q</mi></math> is the total charge of this charge distribution, the radius <math><mi>R</mi></math> is:

**Options:**

- **(A)** <math><mfrac><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi>Q</mi></mrow><mrow><mn>2</mn><mi>π</mi><mi>a</mi><mi>A</mi></mrow></mfrac></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(B)** <math><mi>a</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi>Q</mi></mrow><mrow><mn>2</mn><mi>π</mi><mi>a</mi><mi>A</mi></mrow></mfrac></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(C)** <math><mi>a</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi>Q</mi></mrow><mrow><mn>2</mn><mi>π</mi><mi>a</mi><mi>A</mi></mrow></mfrac></mrow></mfenced></mrow></mrow></math>
- **(D)** <math><mfrac><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi>Q</mi></mrow><mrow><mn>2</mn><mi>π</mi><mi>a</mi><mi>A</mi></mrow></mfrac></mrow></mfenced></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi>Q</mi></mrow><mrow><mn>2</mn><mi>π</mi><mi>a</mi><mi>A</mi></mrow></mfrac></mrow></mfrac></mrow></mfenced></mrow></mrow></math>**

**Detailed Solution:**

<blockquote><p><math><mi>&#961;</mi><mfenced separators="|"><mrow><mi>r</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>A</mi></mrow><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>2</mn><mi>r</mi></mrow><mrow><mi>a</mi></mrow></mfrac></mrow></msup></math>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/anpqxfqkgzkrqfdodumeyfpiixgxlviuruhgirraxkirinveru.png" />

Charge enclosed between <math><mi>r</mi></math> and <math><mi>r</mi><mo>+</mo><mi>d</mi><mi>r</mi></math> is

<math><mi>d</mi><mi>q</mi><mo>=</mo><mi>&#961;</mi><mfenced separators="|"><mrow><mi>r</mi></mrow></mfenced><mi>&#160;</mi><mn>4</mn><mi>&#960;</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>d</mi><mi>r</mi></math>

To get total charge <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>Q</mi><mrow></mrow></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mi>R</mi></munderover><mi>d</mi><mi>q</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mi>R</mi></munderover><mfrac><mi>A</mi><msup><mi>r</mi><mn>2</mn></msup></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>r</mi><mo>/</mo><mi>a</mi></mrow></msup><mi>&#160;</mi><mn>4</mn><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mi>d</mi><mi>r</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>4</mn><mi>&#960;A</mi><mfrac><mi mathvariant="normal">a</mi><mn>2</mn></mfrac><msubsup><mrow><mo>[</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mn>2</mn><mi mathvariant="normal">r</mi><mo>/</mo><mi mathvariant="normal">a</mi></mrow></msup><mo>]</mo></mrow><mn>0</mn><mi mathvariant="normal">R</mi></msubsup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mo>-</mo><mn>4</mn><mi mathvariant="normal">&#960;</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">A</mi><mfrac><mi mathvariant="normal">a</mi><mn>2</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mn>2</mn><mi mathvariant="normal">R</mi><mo>/</mo><mi mathvariant="normal">a</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mo>-</mo><mi>ln</mi><mo>&#8289;</mo><mfenced open="[" close="]" separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi mathvariant="normal">Q</mi><mn>2</mn></mrow><mrow><mn>4</mn><mi>&#960;Aa</mi></mrow></mfrac></mrow></mfenced><mfrac><mi mathvariant="normal">a</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi mathvariant="normal">a</mi><mn>2</mn></mfrac><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mfrac><mn>Q</mn><mrow><mn>2</mn><mi>&#960;aA</mi></mrow></mfrac></mrow></mfrac></mfenced></math></p></blockquote>

</details>

---

### Q37. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Three charges <math><mo>+</mo><mi>Q</mi><mo>,</mo><mi>&#160;</mi><mi>q</mi><mo>,</mo><mo>+</mo><mi>Q</mi></math> are placed respectively, at distance, <math><mn>0</mn><mo>,</mo><mrow><mrow><mi>d</mi></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></math> and <math><mi>d</mi></math> from the origin, on the <math><mi>x</mi></math> -axis. If the net force experienced by <math><mo>+</mo><mi>Q</mi><mo>,</mo></math> placed at <math><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> is zero, then value of <math><mi>q</mi></math> is:

**Options:**

- **(A)** <math><mrow><mrow><mo>+</mo><mi>Q</mi></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></math>
- **(B)** <math><mrow><mrow><mo>+</mo><mi>Q</mi></mrow><mo>/</mo><mrow><mn>4</mn></mrow></mrow></math>
- **(C)** <math><mrow><mrow><mo>-</mo><mi>Q</mi></mrow><mo>/</mo><mrow><mn>4</mn></mrow></mrow></math>
- **(D)** <math><mrow><mrow><mo>-</mo><mi>Q</mi></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mrow><mrow><mo>-</mo><mi>Q</mi></mrow><mo>/</mo><mrow><mn>4</mn></mrow></mrow></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/zkkekkezckeyyjuifibywdtyngxsukdlcysqhcjnnxhppbtxpy.png" />

For net force on charge placed at origin is given as 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mfrac><mrow><mi>K</mi><msup><mrow><mi>Q</mi><mo>.</mo><mi>q</mi></mrow><mi>&#160;</mi></msup></mrow><msup><mfenced separators="|"><mfrac><mi>d</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mrow><mi>K</mi><msup><mi>Q</mi><mn>2</mn></msup></mrow><msup><mi>d</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is a constant.</p><p>Solving the above equation, we get, <math><mi>q</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>Q</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math></p><p>Hence, the charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mo>-</mo><mfrac><mi>Q</mi><mn>4</mn></mfrac></math> such that net force on the charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>Q</mi></math> placed at origin is zero.</p></blockquote>

</details>

---

### Q38. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Two identical conducting spheres <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> carry an equal charges. They are separated by a distance much larger than their diameters, and the force between them is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math>. A third identical conducting sphere, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>, is uncharged. Sphere <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is first touched to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>, then to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>, and then removed. As a result, the force between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> would be equal to:

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn><mi>F</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>F</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>3</mn><mi>F</mi></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(D)** <math><mi> </mi><mi>F</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>3</mn><mi>F</mi></mrow><mrow><mn>8</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ac209d94-4f0a-4f88-a56b-1799a14a5b90-image.png" style="width: 231px; height: 100px;" />

<math><mi>F</mi><mo>=</mo><mfrac><mrow><mi>k</mi><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> are touched charge on both will be <math><mfrac><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>. Then when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> are touched, <math><msub><mrow><mi>q</mi></mrow><mrow><mi>B</mi></mrow></msub><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mfrac><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi>q</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi>q</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
<math><msup><mrow><mi>F</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mo>=</mo><mfrac><mrow><mi>k</mi><msub><mrow><mi>q</mi></mrow><mrow><mi>A</mi></mrow></msub><msub><mrow><mi>q</mi></mrow><mrow><mi>B</mi></mrow></msub></mrow><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mi>k</mi><mi>&#160;</mi><mo>&#215;</mo><mfrac><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mi>&#160;</mi><mo>&#215;</mo><mfrac><mrow><mn>3</mn><mi>q</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac><mfrac><mrow><mi>k</mi><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac><mi>F</mi></math>.</p>

</details>

---

### Q39. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `1`

A copper rod of cross-sectional area A carries a uniform current I through it. At temperature T, if the volume charge density of the rod is $\rho$, how long will the charges take to travel a distance $\mathrm{d}$ ?

**Options:**

- **(A)** $\frac{2 \rho \mathrm{dA}}{\mathrm{IT}}$
- **(B)** $\frac{2 \rho \mathrm{dA}}{\mathrm{I}}$
- **(C)** $\frac{\rho \mathrm{dA}}{\mathrm{I}}$
- **(D)** $\frac{\rho \mathrm{dA}}{\mathrm{IT}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\rho \mathrm{dA}}{\mathrm{I}}$**

**Detailed Solution:**

Charge density
$$
\begin{aligned}
&\rho=\frac{\text { charge }}{\text { volume }}=\frac{q}{A d} \Rightarrow q=\rho A d \\
&\text { Also, } q=I T \Rightarrow T=\frac{q}{I}=\frac{\rho A d}{I}
\end{aligned}
$$

</details>

---

### Q40. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

A liquid drop having 6 excess electrons is kept stationary under a uniform electric field of $25.5$ $\mathrm{kVm}^{-1}$. The density of liquid is $1.26 \times 10^3 \mathrm{~kg} \mathrm{~m}^{-3}$. The radius of the drop is (neglect buoyancy).

**Options:**

- **(A)** $4.3 \times 10^{-7} \mathrm{~m}$
- **(B)** $7.8 \times 10^{-7} \mathrm{~m}$
- **(C)** $0.078 \times 10^{-7} \mathrm{~m}$
- **(D)** $3.4 \times 10^{-7} \mathrm{~m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $7.8 \times 10^{-7} \mathrm{~m}$**

**Detailed Solution:**

$\mathrm{F}=\mathrm{qE}=m g\left(\mathrm{q}=6 \mathrm{e}=6 \times 1.6 \times 10^{-19}\right)$
$\operatorname{Density}(\mathrm{d})=\frac{\text { mass }}{\text { volume }}=\frac{\mathrm{m}}{\frac{4}{3} \pi \mathrm{r}^3}$
or $r^3=\frac{m}{\frac{4}{3} \pi d}$
Putting the value of $d$ and $m\left(=\frac{q E}{g}\right)$ and
solving we get $\mathrm{r}=7.8 \times 10^{-7} \mathrm{~m}$

</details>

---

### Q41. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Consider a finite insulated, uncharged conductor placed near a finite positively charged conductor. The uncharged body must have a potential :

**Options:**

- **(A)** less than the charged conductor and more than at infinity.
- **(B)** more than the charged conductor and less than at infinity.
- **(C)** more than the charged conductor and more than at infinity.
- **(D)** less than the charged conductor and less than at infinity.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) less than the charged conductor and more than at infinity.**

**Detailed Solution:**

The potential of uncharged body is less than that of the charged conductor and more than at infinity.

</details>

---

### Q42. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `3`

Two identical charged spheres suspended from a common point by two massless strings of length I are initially a distance $d(d< < 1)$ apart because of their mutual repulsion. The charge begins to leak from both the spheres at a constant rate. As a result the charges approach each other with a velocity $v$. Then as a function of distance $x$ between them,

**Options:**

- **(A)** $v \propto x^{-1}$
- **(B)** $v \propto x^{1 / 2}$
- **(C)** $v \propto x$
- **(D)** $v \propto x^{-1 / 2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $v \propto x^{-1 / 2}$**

**Detailed Solution:**

At any instant of separation between charges is $x$.
$$
\begin{aligned}
& \text { equilibrium condition }=\mathrm{K} \frac{\mathrm{Q}^2}{\mathrm{x}^2}=\omega \frac{\mathrm{x}}{2 \ell} \\
& \Rightarrow \mathrm{Q}^2=\mathrm{Cx}^3 \\
& \Rightarrow 2 \mathrm{Q} \frac{\mathrm{dQ}}{\mathrm{dt}}=\mathrm{C} 3 \mathrm{x}^2 \frac{\mathrm{dx}}{\mathrm{dt}} \\
& \Rightarrow \frac{\mathrm{dx}}{\mathrm{dt}} \propto \frac{\mathrm{x}^{3 / 2}}{\mathrm{x}^2} \propto \mathrm{x}^{-1 / 2}
\end{aligned}
$$

</details>

---

### Q43. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `3`

Two identical charged spheres are suspended by strings of equal lengths. The strings make an angle of $30^{\circ}$ with each other. When suspended in a liquid of density $0.8 \mathrm{~g} \mathrm{~cm}^{-3}$, the angle remains the same. If density of the material of the sphere is $16 \mathrm{~g} \mathrm{~cm}^{-3}$, the dielectric constant of the liquid is

**Options:**

- **(A)** 4
- **(B)** 3
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

From F.B.D of sphere, using Lami's theorem
$$
\frac{\mathrm{F}}{\mathrm{mg}}=\tan \theta
$$
when suspended in liquid, as $\theta$ remains same,
$\therefore \quad \frac{\mathrm{F}^{\prime}}{\mathrm{mg}\left(1-\frac{\rho}{\mathrm{d}}\right)}=\tan \theta$
using (i) and (ii)
$$
\frac{F}{m g}=\frac{F^{\prime}}{m g\left(1-\frac{\rho}{d}\right)} \text { where, } F^{\prime}=\frac{F}{K}
$$
$\therefore \quad \frac{\mathrm{F}}{\mathrm{mg}}=\frac{\mathrm{F}^{\prime}}{\mathrm{mg} \mathrm{K}\left(1-\frac{\rho}{\mathrm{d}}\right)}$
or $\quad \mathrm{K}=\frac{1}{1-\frac{\rho}{d}}=2$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f8TXgba_g3wEP1jTnqx8XPypbUads0UYGbOPgCoJbmI.original.fullsize.png">

</details>

---

### Q44. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{g}_{\mathrm{E}}$ and $\mathrm{g}_{\mathrm{m}}$ are the accelerations due to gravity on the surfaces of the earth and the moon respectively and if Millikan's oil drop experiment could be performed on the two surfaces, one will find the ratio $\frac{\text { electronic charge on the moon }}{\text { electronic charge on the earth }}$ to be

**Options:**

- **(A)** $1$
- **(B)** $0$
- **(C)** $\mathrm{g}_{\mathrm{E}} / \mathrm{g}_{\mathrm{m}}$
- **(D)** $\mathrm{g_m}$ / $\mathrm{g_E}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

No Solution Available

</details>

---

### Q45. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

Charges are placed on the vertices of a square as shown. Let $\mathrm{E}$ be the electric field and $\mathrm{V}$ the potential at the centre. If the charges on $\mathrm{A}$ and $\mathrm{B}$ are interchanged with those on $\mathrm{D}$ and $\mathrm{C}$ respectively, then
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/KCUoT9rFLOJn_XA78YWBJ2MHdHjL0cjtJ46J86sH970.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{\vec{E}}$ remains unchanged, $\mathrm{V}$ changes
- **(B)** Both $\mathrm{\vec{E}}$ and $\mathrm{V}$ change
- **(C)** $\mathrm{\vec{E}}$ and $\mathrm{V}$ remains unchanged
- **(D)** $\mathrm{\vec{E}}$ changes, $\mathrm{V}$ remains unchanged

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{\vec{E}}$ changes, $\mathrm{V}$ remains unchanged**

**Detailed Solution:**

As $\overrightarrow{\mathrm{E}}$ is a vector quantity

</details>

---

### Q46. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

Two point charges $+8 q$ and $-2 q$ are located at $x=0$ and $x=L$ respectively. The location of a point on the $x$ axis at which the net electric field due to these two point charges is zero is

**Options:**

- **(A)** $2 \mathrm{~L}$
- **(B)** $L / 4$
- **(C)** $8 \mathrm{~L}$
- **(D)** $4 \mathrm{~L}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \mathrm{~L}$**

**Detailed Solution:**

$-\frac{\mathrm{k} 2 q}{(\mathrm{x}-\mathrm{L})^2}+\frac{\mathrm{k} 8 \mathrm{q}}{\mathrm{x}^2}=0$
$\Rightarrow \mathrm{x}=2 \mathrm{~L}$

</details>

---

### Q47. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `3`

Two spherical conductor $B$ and $C$ having equal radii and carrying equal charges in them repel each other with a force $F$ when kept apart at some distance. A third spherical conductor having same radius as that of $B$ but uncharged brought in contact with $B$, then brought in contact with $\mathrm{C}$ and finally removed away from both. The new force of repulsion, between $B$ and $C$ is

**Options:**

- **(A)** $\mathrm{F} / 4$
- **(B)** $3 F / 4$
- **(C)** $\mathrm{F} / 8$
- **(D)** $3 \mathrm{~F} / 8$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3 \mathrm{~F} / 8$.**

**Detailed Solution:**

$F^{\prime}=\frac{1}{4 \pi \varepsilon_0} \frac{(q / 2)(3 q / 4)}{d^2}=\frac{3 F}{8}$

</details>

---

