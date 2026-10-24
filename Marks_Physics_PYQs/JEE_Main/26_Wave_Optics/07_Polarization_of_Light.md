# JEE Main Physics - Wave Optics

## Topic 7: Polarization of Light

**Total Questions:** 34

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `numerical` | *Level:* `2`

An unpolarized light of intensity $I_o$ passes through polarizer and then through a certain optically active solution and finally it goes to analyser. If the angle between analyser and polariser is $0°$ and intensity of light emerged from analyser is $\dfrac{3}{8}I_o$, the angle of rotation of the light by the solution with respect to analyser is _______ degrees.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

Intensity of light after passing through the first polarizer is:

$I_1 = \dfrac{I_o}{2}$

Let the optically active solution rotate the plane of polarization by an angle $\theta$. Since the angle between the polarizer and the analyser is $0^\circ$, the angle between the plane of polarization of the light emerging from the solution and the transmission axis of the analyser is also $\theta$.

According to Malus's law, the intensity of light emerging from the analyser is:

$I_2 = I_1 \cos^2 \theta = \dfrac{I_o}{2} \cos^2 \theta$

Given that the final intensity is $\dfrac{3}{8}I_o$, we have:

$\dfrac{I_o}{2} \cos^2 \theta = \dfrac{3}{8}I_o$

$\cos^2 \theta = \dfrac{3}{4}$

$\cos \theta = \dfrac{\sqrt{3}}{2}$

$\theta = 30^\circ$

Answer: $30$

</details>

---

### Q2. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An unpolarized light of certain intensity passes through a combination of two polarizers whose transmission axes are at $30°$ and $90°$, respectively, with respect to the horizontal axis. A third polarizer with its transmission axis at $60°$ with the horizontal axis is placed between the two existing polarizers. The ratio of the output intensities with and without the third polarizer is ______.

**Options:**

- **(A)** $3/4$
- **(B)** $4/3$
- **(C)** $9/4$
- **(D)** $4/9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $9/4$**

**Detailed Solution:**

Let the intensity of the incident unpolarized light be $I_0$.

After passing through the first polarizer, the intensity becomes $I_1 = \dfrac{I_0}{2}$.

Without the third polarizer, the light passes directly from the first polarizer (at $30^{\circ}$) to the second polarizer (at $90^{\circ}$). The angle between their transmission axes is $90^{\circ} - 30^{\circ} = 60^{\circ}$.

Using Malus's law, the output intensity without the third polarizer is:
$I_{without} = I_1 \cos^2(60^{\circ}) = \dfrac{I_0}{2} \times \left(\dfrac{1}{2}\right)^2 = \dfrac{I_0}{8}$

When the third polarizer (at $60^{\circ}$) is placed between them, the light first passes from the first polarizer to the third polarizer. The angle between their axes is $60^{\circ} - 30^{\circ} = 30^{\circ}$.

The intensity after the third polarizer is:
$I_3 = I_1 \cos^2(30^{\circ}) = \dfrac{I_0}{2} \times \left(\dfrac{\sqrt{3}}{2}\right)^2 = \dfrac{3I_0}{8}$

The light then passes from the third polarizer to the second polarizer. The angle between their axes is $90^{\circ} - 60^{\circ} = 30^{\circ}$.

The final output intensity with the third polarizer is:
$I_{with} = I_3 \cos^2(30^{\circ}) = \dfrac{3I_0}{8} \times \left(\dfrac{\sqrt{3}}{2}\right)^2 = \dfrac{9I_0}{32}$

The ratio of the output intensities with and without the third polarizer is:
$\text{Ratio} = \dfrac{I_{with}}{I_{without}} = \dfrac{\dfrac{9I_0}{32}}{\dfrac{I_0}{8}} = \dfrac{9}{4}$

Answer: $9/4$

</details>

---

### Q3. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An unpolarized light is incident on the plane interface of air-dielectric medium shown in figure. If the incident angle is equal to Brewster angle, identify the expression representing reflected wave.
<img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/04APRS1__q45_d1.png" />

**Options:**

- **(A)** $(E_x\hat{i} + E_y\hat{j})\sin(kx - kz - \omega t)$
- **(B)** $(E_x\hat{i} + E_z\hat{k})\sin(kx + ky - \omega t)$
- **(C)** $(E_x\hat{j} + E_y\hat{k})\sin(ky + kz - \omega t)$
- **(D)** $(E_x\hat{i} + E_y\hat{j} + E_z\hat{k})\sin(kx + ky - kz - \omega t)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(E_x\hat{i} + E_y\hat{j})\sin(kx - kz - \omega t)$**

**Detailed Solution:**

From the given figure, the incident light rays lie in the $xz$-plane. Therefore, the plane of incidence is the $xz$-plane.

The incident wave travels from the air ($z < 0$) towards the medium ($z > 0$), so it propagates in the $+x$ and $+z$ directions. The reflected wave will travel back into the air, meaning it propagates in the $+x$ and $-z$ directions. 

The wave vector for the reflected wave can be written as $\vec{k}_r = k_x \hat{i} - k_z \hat{k}$.
The phase of the reflected wave is given by $\vec{k}_r \cdot \vec{r} - \omega t = k_x x - k_z z - \omega t$. This phase matches the expression in option (1).

According to Brewster's law, when unpolarized light is incident at the Brewster angle, the reflected light is completely polarized perpendicular to the plane of incidence. Since the plane of incidence is the $xz$-plane, the reflected electric field must be entirely along the $y$-axis ($\hat{j}$ direction).

Let us verify this with option (1), which gives the electric field as $\vec{E} = E_x \hat{i} + E_y \hat{j}$.
For an electromagnetic wave, the electric field must be perpendicular to the direction of propagation, so $\vec{k}_r \cdot \vec{E} = 0$.
$(k_x \hat{i} - k_z \hat{k}) \cdot (E_x \hat{i} + E_y \hat{j}) = 0$
$k_x E_x = 0$

Since $k_x \neq 0$, we must have $E_x = 0$. This leaves $\vec{E} = E_y \hat{j}$, which means the wave is purely polarized along the $y$-axis. This perfectly satisfies the condition for reflection at the Brewster angle.

Thus, the correct expression representing the reflected wave is $(E_x\hat{i} + E_y\hat{j})\sin(kx - kz - \omega t)$.

Answer: $(E_x\hat{i} + E_y\hat{j})\sin(kx - kz - \omega t)$

</details>

---

### Q4. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An unpolarised light is incident at an interface of two dielectric media having refractive indices of 2 (incident medium) and $2 \sqrt{3}$ (medium) respectively. To satisfy the condition that reflected and refracted rays are perpendicular to each other, the angle of incidence is $\_\_\_\_$.

**Options:**

- **(A)** $45^{\circ}$
- **(B)** $60^{\circ}$
- **(C)** $10^{\circ}$
- **(D)** $30^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $60^{\circ}$**

**Detailed Solution:**

For reflected and refracted rays to be perpendicular, if $i$ is the angle of incidence and $r$ is the angle of refraction, then $i + r = 90°$, giving $r = 90° - i$.
Applying Snell's law: $n_1 \sin i = n_2 \sin r$
$2 \sin i = 2\sqrt{3} \sin(90° - i)$
$2 \sin i = 2\sqrt{3} \cos i$
$\tan i = \sqrt{3}$
$i = 60°$

</details>

---

### Q5. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

When an unpolarized light falls at a particular angle on a glass plate (placed in air), it is observed that the reflected beam is linearly polarized. The angle of refracted beam with respect to the normal is $\_\_\_\_$. 
 $\left(\tan ^{-1}(1.52)=57.7^{\circ}\right.$, refractive indices of air and glass are 1.00 and 1.52, respectively.)

**Options:**

- **(A)** $39.6^{\circ}$
- **(B)** $32.3^{\circ}$
- **(C)** $36.3^{\circ}$
- **(D)** $42.6^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $32.3^{\circ}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/23S2_s_41_1.png">
$\tan i = \dfrac{\mu_2}{\mu_1} = \dfrac{\mu_g}{\mu_a}$
$\tan i = 1.52$
$i = 57.7°$
$r = 90° - i$
$r = 32.3°$

</details>

---

### Q6. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two polarisers $P_1$ and $P_2$ are placed in such a way that the intensity of the transmitted light will be zero. A third polariser $P_3$ is inserted in between $P_1$ and $\mathrm{P}_2$, at the particular angle between $\mathrm{P}_2$ and $\mathrm{P}_3$. The transmitted intensity of the light passing the through all three polarisers is maximum. The angle between the polarisers $\mathrm{P}_2$ and $\mathrm{P}_3$ is :

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $\frac{\pi}{8}$
- **(D)** $\frac{\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{4}$**

**Detailed Solution:**

Through $P_2 I_1=I_0 \sin ^2\left(\frac{\pi}{2}-\theta\right)$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/KV9JC3sCu1ub_zLz-B9MxyBeixXLOOZgKqvdBY4vjKU.original.fullsize.png"/>
$I_1=I_0 \cos ^2 \theta$
Through $P_3 I_{\text {net }}=\left(I_0 \cos ^2 \theta\right) \sin ^2 \theta$
$I_{n c t}=\frac{I_0}{4}[\sin (2 \theta)]^2 \text { for max } I_{\text {net }} \theta=45^{\circ}$
So angle between $P_2$ and $P_3=\frac{\pi}{4}$
Correct Ans. (1)

</details>

---

### Q7. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

In a Young's double slit experiment, three polarizers are kept as shown in the figure. The transmission axes of $P_1$ and $P_2$ are orthogonal to each other. The polarizer $P_3$ covers both the slits with its transmission axis at $45^{\circ}$ to those of $P_1$ and $P_2$. An unpolarized light of wavelength $\lambda$ and intensity $I_0$ is incident on $P_1$ and $P_2$. The intensity at a point after $P_3$ where the path difference between the light waves from $s_1$ and $s_2$ is $\frac{\lambda}{3}$, is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9S6x01tQt9218voaYBlmkPcncEfSCAcGNF4nk13x-CM.original.fullsize.png"/>

**Options:**

- **(A)** $\frac{I_0}{2}$
- **(B)** $\frac{I_0}{4}$
- **(C)** $\frac{\mathrm{I}_0}{3}$
- **(D)** $I_0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{I_0}{4}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ozb7ot16Ei5j4lCjKNSQGLTo1uQsgaWXWDabKZk-QO8.original.fullsize.png">




after passing through third poleriser, Intensity of both the waves must be $\frac{\mathrm{I}_0}{4}$
now, at a point where path diff is $\frac{\lambda}{3}$, phase difference
$\begin{aligned}
& \Delta \phi=2 \mathrm{~K}\left(\frac{\Delta \mathrm{x}}{\lambda}\right)=\frac{2 \pi}{3} \\
& \therefore \mathrm{I}_{\mathrm{res}}=\sqrt{\left(\frac{\mathrm{I}_0}{4}\right)^2+\left(\frac{\mathrm{I}_0}{4}\right)^2+2\left(\frac{\mathrm{I}_0}{4}\right)^2} \cos \frac{2 \pi}{3} \\
& =\frac{\mathrm{I}_0}{4}
\end{aligned}$

</details>

---

### Q8. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>When unpolarized light is incident at an angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>°</mo></math> on a transparent medium from air. The reflected ray is completely polarized. The angle of refraction in the medium is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>°</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>°</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>°</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>°</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>°</mo></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9b3638b8-f15d-4293-968d-d093eb592d2c.png" style="width: 300px; height: 194px;"/></p><p>By Brewster’s law at complete polarization, refracted ray and reflected ray are perpendicular to each other.</p><p>As angle of reflection will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>60</mn><mo>°</mo></math>. Therefore, angle of refraction will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>180</mn><mo>°</mo><mo>-</mo><mn>60</mn><mo>°</mo><mo>-</mo><mn>90</mn><mo>°</mo><mo>=</mo><mn>30</mn><mo>°</mo></math>.</p>

</details>

---

### Q9. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A beam of unpolarised light of intensity <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub></math> is passed through a polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and then through another polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> which is oriented so that its principal plane makes an angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>°</mo></math> relative to that of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. The intensity of emergent light is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Intensity of polarised light from polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac></math>. Therefore,</p><p>Intensity of emergent light
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mn>45</mn><mo>°</mo><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>4</mn></mfrac></math></p></blockquote>

</details>

---

### Q10. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

When a polaroid sheet is rotated between two crossed polaroids then the transmitted light intensity will be maximum for a rotation of :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>°</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>°</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>°</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>°</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>°</mo></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub></math> be intensity of unpolarised light incident on first polaroid.
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo></math> Intensity of light transmitted from <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mtext>st </mtext></msup></math> polaroid
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac></math>
If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>θ</mi></math> be the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mtext>st </mtext></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mtext>nd </mtext></msup></math> polaroid and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ϕ</mi></math> be the angle between <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mtext>nd </mtext></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mtext>rd </mtext></msup></math> polaroid, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>θ</mi><mo>+</mo><mi>ϕ</mi><mo>=</mo><mn>90</mn><mo>°</mo><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo></math> Intensity from <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mtext>nd </mtext></msup></math> polaroid,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>I</mi><mn>2</mn></msub></mtd><mtd><mo>=</mo></mtd><mtd><msub><mi>I</mi><mn>1</mn></msub><mi>c</mi><mi>o</mi><msup><mi>s</mi><mn>2</mn></msup><mi>θ</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac><mi>c</mi><mi>o</mi><msup><mi>s</mi><mn>2</mn></msup><mi>θ</mi></mtd></mtr></mtable></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>3</mn></msub><mo>=</mo></math> Intensity from <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mtext>rd </mtext></msup></math> polaroid</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>I</mi><mn>3</mn></msub></mtd><mtd><mo>=</mo></mtd><mtd><msub><mi>I</mi><mn>2</mn></msub><mi>c</mi><mi>o</mi><msup><mi>s</mi><mn>2</mn></msup><mi>ϕ</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><msub><mi>I</mi><mn>1</mn></msub><msup><mi>cos</mi><mn>2</mn></msup><mi>θ</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>ϕ</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac><mi>c</mi><mi>o</mi><msup><mi>s</mi><mn>2</mn></msup><mi>θ</mi><mi>c</mi><mi>o</mi><msup><mi>s</mi><mn>2</mn></msup><mfenced><mrow><mn>90</mn><mo>°</mo><mo>-</mo><mi>θ</mi></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac><mi>c</mi><mi>o</mi><msup><mi>s</mi><mn>2</mn></msup><mi>θ</mi><mi>s</mi><mi>i</mi><msup><mi>n</mi><mn>2</mn></msup><mi>θ</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac><msup><mfenced close="]" open="["><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>θ</mi><mi>cos</mi><mi>θ</mi></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>8</mn></mfrac><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>θ</mi></mtd></mtr></mtable></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>3</mn></msub></math> will be maximum when</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>2</mn><mi>θ</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>θ</mi><mo>=</mo><mn>90</mn><mo>°</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>θ</mi><mo>=</mo><mn>45</mn><mo>°</mo></math></p>

</details>

---

### Q11. JEE Main 2023 (10 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Unpolarised light of intensity <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>&#8722;</mo><mn>2</mn></mrow></msup></math> passes through the combination of three polaroids such that the pass axis of the last polaroids is perpendicular to that of the pass axis of first polaroids. If intensity of emerging light is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>&#8722;</mo><mn>2</mn></mrow></msup></math>, then the angle between pass axis of first two polaroids is _________<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#176;</mo></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/92e65e15-0c67-49dd-ac6f-bf2b15d53633.png" style="width: 200px; height: 181px;" /></p><p>The given data is</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub><mo>=</mo><mn>32</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>f</mi></msub><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p>Thus, by substituting the value, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>f</mi></msub><mo>=</mo><mfenced><mrow><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>&#215;</mo><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mrow><mn>90</mn><mo>&#176;</mo><mo>-</mo><mi>&#952;</mi></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>=</mo><mn>16</mn><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#183;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mo>&#183;</mo><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mn>30</mn><mo>&#176;</mo></math></p></blockquote>

</details>

---

### Q12. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

&lsquo;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>&rsquo; polarizing sheets are arranged such that each makes an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>&#176;</mo></math> with the proceeding sheet. An unpolarized light of intensity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> is incident into this arrangement. The output intensity is found to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>I</mi><mn>64</mn></mfrac></math> . The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> will be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

<p>When an unpolarized light passes through a polariser, the intensity of the emergent light from the polariser depends on the square of the cosine of the angle between the plane of the polariser and the direction of the incident light.</p><p>The formula to calculate the intensity <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>I</mi><mn>1</mn></msub></mfenced></math> of the emergent light from a polariser which makes an angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> with the direction of the incident light is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mo>&#160;</mo><mi>I</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> is the intensity of the incident light.</p><p>Substitute <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>&#176;</mo></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> into equation (1) to obtain the intensity of the first emergent light.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>I</mi><mn>1</mn></msub></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mi>I</mi><msup><mi>cos</mi><mn>2</mn></msup><mn>45</mn><mo>&#176;</mo></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mfrac><mi>I</mi><mn>2</mn></mfrac></mtd></mtr></mtable></math></p><p>In a similar manner, the intensity <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>I</mi><mn>2</mn></msub></mfenced></math> of the second emergent light can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>I</mi><mn>2</mn></msub></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><msub><mi>I</mi><mn>1</mn></msub><msup><mi>cos</mi><mn>2</mn></msup><mn>45</mn><mo>&#176;</mo></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mfrac><msub><mi>I</mi><mn>1</mn></msub><mn>2</mn></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mfrac><mi>I</mi><mn>4</mn></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mi>I</mi><msup><mn>2</mn><mn>2</mn></msup></mfrac></mtd></mtr></mtable></math></p><p>Thus, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> number of such polarisers, the net intensity <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>I</mi><mi>n</mi></msub></mfenced></math> of the emergent light can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>n</mi></msub><mo>=</mo><mo>&#160;</mo><mfrac><mi>I</mi><msup><mn>2</mn><mi>n</mi></msup></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Comparing equation (1) with the given expression for the intensity, it can be concluded that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mo>&#160;</mo><mn>6</mn></math></p>

</details>

---

### Q13. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two polaroids <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>B</mi></math> are placed in such a way that the pass-axis of polaroids are perpendicular to each other. Now, another polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is placed between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>B</mi></math> bisecting angle between them. If intensity of unpolarised light is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub></math> then intensity of transmitted light after passing through polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> will be :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>8</mn></mfrac></math>
- **(D)** Zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>8</mn></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/22691055-1072-4c41-ae32-2622b53d7ab2-9895925.png" style="width: 400px; height: 282px;" /></p><p>As given here, the pass axis of polaroids <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are inclined at angle of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>&#186;</mo></math> with each other. Another polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>is placed at angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>&#176;</mo></math>with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>. </p><p>Therefore, intensity of light after falling on polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><msub><mi>I</mi><mi>A</mi></msub><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac></math></p><p>Intensity of light after falling on polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>,</mo><mo>&#160;</mo><msub><mi>I</mi><mi>C</mi></msub><mo>=</mo><msub><mi>I</mi><mi>A</mi></msub><msup><mi>cos</mi><mn>2</mn></msup><mn>45</mn><mo>&#176;</mo><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mn>45</mn><mo>&#176;</mo><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>4</mn></mfrac></math></p><p>Intensity of light after falling on polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>,</mo><mo>&#160;</mo><msub><mi>I</mi><mi>B</mi></msub><mo>=</mo><msub><mi>I</mi><mi>C</mi></msub><msup><mi>cos</mi><mn>2</mn></msup><mn>45</mn><mo>&#176;</mo><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>4</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mn>45</mn><mo>&#176;</mo><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>8</mn></mfrac></math></p>

</details>

---

### Q14. JEE Main 2023 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>Unpolarised light is incident on the boundary between two dielectric media, whose dielectric constants are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>8</mn></math> (medium &ndash;<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>) and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mn>8</mn></math> (medium &ndash; <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>), respectively. To satisfy the condition, so that the reflected and refracted rays are perpendicular to each other, the angle of incidence should be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>10</mn><mi>&#952;</mi></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math>, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> is ______.</p><p>(Given for dielectric media, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#956;</mi><mi>r</mi></msub><mo>=</mo><mn>1</mn></math>)</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<p>As given in the question, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#956;</mi><mn>1</mn></msub><mo>=</mo><msqrt><msub><mi>&#949;</mi><mi>r</mi></msub><msub><mi>&#956;</mi><mi>r</mi></msub></msqrt><mo>=</mo><msqrt><mn>2</mn><mo>.</mo><mn>8</mn><mo>&#215;</mo><mn>1</mn></msqrt><mo>=</mo><msqrt><mn>2</mn><mo>.</mo><mn>8</mn></msqrt></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#956;</mi><mn>2</mn></msub><mo>=</mo><msqrt><msub><mi>&#949;</mi><mi>r</mi></msub><msub><mi>&#956;</mi><mi>r</mi></msub></msqrt><mo>=</mo><msqrt><mn>6</mn><mo>.</mo><mn>8</mn><mo>&#215;</mo><mn>1</mn></msqrt><mo>=</mo><msqrt><mn>6</mn><mo>.</mo><mn>8</mn></msqrt></math></p><p>Now applying Snell&#39;s law and considering <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>90</mn><mo>&#176;</mo><mo>-</mo><mi>i</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#956;</mi><mn>1</mn></msub><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>i</mi><mo>=</mo><msub><mi>&#956;</mi><mn>2</mn></msub><mo>&#160;</mo><mi>cos</mi><mo>&#160;</mo><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mo>&#160;</mo><mi>i</mi><mo>=</mo><mfrac><msub><mi>&#956;</mi><mn>2</mn></msub><msub><mi>&#956;</mi><mn>1</mn></msub></mfrac><mo>=</mo><msqrt><mfrac><mrow><mn>6</mn><mo>.</mo><mn>8</mn></mrow><mrow><mn>2</mn><mo>.</mo><mn>8</mn></mrow></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mo>&#160;</mo><mi>i</mi><mo>=</mo><msup><mfenced><mfrac><mrow><mn>2</mn><mo>.</mo><mn>8</mn><mo>+</mo><mn>4</mn></mrow><mrow><mn>2</mn><mo>.</mo><mn>8</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>i</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>10</mn><mn>7</mn></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mn>7</mn></math>.</p>

</details>

---

### Q15. JEE Main 2023 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>As shown in figures, three identical polaroids <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>3</mn></msub></math> are placed one after another. The pass axis of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>3</mn></msub></math> are inclined at angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>&#186;</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>&#186;</mo></math> with respect to axis of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math>. The source <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> has an intensity of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>256</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>. The intensity of light at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> is _____<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">W</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1e130c68-883c-4904-9180-d55c8c515e11-9894954.png" style="width: 700px; height: 196px;" /> </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **24**

**Detailed Solution:**

<p>As given here, the pass axis of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>3</mn></msub></math> are inclined at angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>&#186;</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>&#186;</mo></math> with respect to axis of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math>. </p><p>Therefore, intensity of light after falling on first polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac></math></p><p>Intensity of light after falling on second polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub><msup><mi>cos</mi><mn>2</mn></msup><mn>60</mn><mo>&#176;</mo><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>8</mn></mfrac></math></p><p>Intensity of light after falling on third polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>3</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>I</mi><mn>3</mn></msub><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><msup><mi>cos</mi><mn>2</mn></msup><mn>30</mn><mo>&#176;</mo><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>8</mn></mfrac><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><msub><mi>I</mi><mn>0</mn></msub></mrow><mn>32</mn></mfrac></math></p><p>The intensity of light at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msub><mi>I</mi><mn>0</mn></msub></mrow><mn>32</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#215;</mo><mn>256</mn></mrow><mn>32</mn></mfrac><mo>=</mo><mn>24</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p>

</details>

---

### Q16. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An unpolarised light beam of intensity <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>I</mi><mn>0</mn></msub></math> is passed through a polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and then through another polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> which is oriented in such a way that its passing axis makes an angle of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#176;</mo></math> relative to that of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>. The intensity of the emergent light is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msub><mi>I</mi><mn>0</mn></msub></mrow><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msub><mi>I</mi><mn>0</mn></msub></mrow><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msub><mi>I</mi><mn>0</mn></msub></mrow><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>When unpolarized light passes from Polaroid, then it becomes polarised light and intensity becomes half of the original, therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>2</mn><msub><mi>I</mi><mn>0</mn></msub></mrow><mn>2</mn></mfrac><mo>=</mo><msub><mi>I</mi><mn>0</mn></msub></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/912cf425-df11-4e8f-b3d6-290a6a77f598-image.png" style="width: 200px; height: 79px;" /></p><p>Given here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mn>30</mn><mo>&#176;</mo></math>.</p><p>Using law of Malus for the second polariser, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msub><mi>I</mi><mn>0</mn></msub><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></math></p><p>We have, intensity of emergent light, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub><msup><mi>cos</mi><mn>2</mn></msup><mn>30</mn><mo>&#176;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>I</mi><mn>0</mn></msub><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><msub><mi>I</mi><mn>0</mn></msub></mrow><mn>4</mn></mfrac></math></p></blockquote>

</details>

---

### Q17. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A wave of frequency <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>GHz</mi></math>, strikes a particle of size <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mn>1</mn><mn>100</mn></mfrac></mfenced><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math>, then this phenomenon is called as

**Options:**

- **(A)** Diffraction
- **(B)** Scattering
- **(C)** Reflection
- **(D)** Refraction

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Scattering**

**Detailed Solution:**

<p>Rayleigh scattering applies to particles that are small with respect to wavelengths of light.</p>

</details>

---

### Q18. JEE Main 2022 (25 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A light whose electric field vectors are completely removed by using a good polaroid, allowed to incident on the surface of the prism at Brewster&#39;s angle. Choose the most suitable option for the phenomenon related to the prism.

**Options:**

- **(A)** Reflected and refracted rays will be perpendicular to each other.
- **(B)** Wave will propagate along the surface of prism.
- **(C)** No refraction, and there will be total reflection of light.
- **(D)** No reflection. and there will be total transmission of light.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) No reflection. and there will be total transmission of light.**

**Detailed Solution:**

A light whose electric field vectors are completely removed by using a good Polaroid, allowed to incident on the surface of the prism at Brewster&#39;s angle. Then, no reflection of light but there will be total transmission of light.

</details>

---

### Q19. JEE Main 2021 (26 Aug Shift 2)

*Type:* `numerical` | *Level:* `2`

A source of light is placed in front of a screen. The intensity of light on the screen is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math>. Two Polaroids <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> are so placed in between the source of light and screen that the intensity of light on the screen is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>I</mi><mn>2</mn></mfrac></math>. Then the <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math>, should be rotated by an angle of (degrees) so that the intensity of light on the screen becomes <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>I</mi></mrow><mn>8</mn></mfrac></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2358a799-fae9-4cdd-9bf1-88b15dd71b35-image.png" style="width: 226px; height: 137px;" /></p><p>Recall the law of Malus <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>I</mi><mo>&#39;</mo></msup><mo>=</mo><mfrac><mi>I</mi><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> is the angle between two polaroids, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>3</mn><mi>I</mi></mrow><mn>8</mn></mfrac><mo>=</mo><mfrac><mi>I</mi><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mn>30</mn><mo>&#176;</mo></math>.</p>

</details>

---

### Q20. JEE Main 2021 (24 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

An unpolarized light beam is incident on the polarizer of a polarization experiment and the intensity of light beam emerging from the analyzer is measured as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math> Lumens. Now, if the analyzer is rotated around the horizontal axis (direction of light) by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#176;</mo></math> in clockwise direction, the intensity of emerging light will be _______Lumens.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **75**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a754a870-3239-4fd4-a888-4eaf8f6cfd3a-image.png" style="width: 550px; height: 147px;" /></p><p>Assuming initially axis of Polarizer and Analyzer are parallel</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/facc8b44-0302-4abe-97ea-87936241d261-image.png" style="width: 550px; height: 158px;" /></p><p>Now emerging intensity <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mn>30</mn><mo>&#176;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>100</mn><msup><mfenced><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>100</mn><mo>&#215;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mn>75</mn></math></p>

</details>

---

### Q21. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A beam of plane polarized light of large cross-sectional area and uniform intensity of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.3</mo><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>&#8211;</mo><mn>2</mn></mrow></msup></math> falls normally on a polarizer (cross-sectional area <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8211;</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math>), which rotates about its axis with an angular speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn><mo>.4</mo><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The energy of light passing through the polarizer per revolution, is close to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.0</mo><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8722;</mo><mn>5</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8722;</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8722;</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8722;</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8722;</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b077eab1-34eb-4561-b543-6f5da033c31b-image.png" style="width: 250px; height: 175px;" /></p><p>Given,</p><p>Intensity of plane polarized light of large cross-sectional area is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub><mo>=</mo><mn>3</mn><mo>.</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p>Area of cross-section of polarizer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn><mo>&#160;</mo></mrow></msup><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math></p><p>Angular speed of rotation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mn>31</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>The intensity of light is the given by the definition,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mi mathvariant="normal">E</mi><mrow><mi>A</mi><mi>T</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Intensity of light passing through the polarizer as polarizer rotates is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>a</mi><mi>v</mi><mi>g</mi></mrow></msub><mo>=</mo><msub><mi>I</mi><mn>0</mn></msub><mfrac><mn>1</mn><mi>T</mi></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>T</mi></msubsup><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mrow><mi>&#969;</mi><mi>t</mi></mrow></mfenced><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mrow><mi>a</mi><mi>v</mi><mi>g</mi></mrow></msub><mo>=</mo><msub><mi>I</mi><mn>0</mn></msub><mfrac><mn>1</mn><mi>T</mi></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mi>T</mi></msubsup><mfenced close="]" open="["><mfrac><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mfenced><mrow><mn>2</mn><mi>&#969;</mi><mi>t</mi></mrow></mfenced></mrow><mn>2</mn></mfrac></mfenced><mo>d</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mrow><mi>a</mi><mi>v</mi><mi>g</mi></mrow></msub><mo>=</mo><msub><mi>I</mi><mn>0</mn></msub><mfrac><mn>1</mn><mrow><mn>2</mn><mi>T</mi></mrow></mfrac><mfenced close="]" open="["><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mi>T</mi></msubsup><mo>d</mo><mi>t</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>T</mi></msubsup><mi>cos</mi><mfenced><mrow><mn>2</mn><mi>&#969;</mi><mi>t</mi></mrow></mfenced><mo>d</mo><mi>t</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mrow><mi>a</mi><mi>v</mi><mi>g</mi></mrow></msub><mo>=</mo><msub><mi>I</mi><mn>0</mn></msub><mfrac><mn>1</mn><mrow><mn>2</mn><mi>T</mi></mrow></mfrac><mfenced open="[" close="]"><mrow><mi>T</mi><mo>+</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mrow><mi>a</mi><mi>v</mi><mi>g</mi></mrow></msub><mo>=</mo><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>Using equation (1) and (2) we get energy per revolution is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><msub><mi>I</mi><mn>0</mn></msub><mi>A</mi></mrow><mn>2</mn></mfrac><mi>T</mi><mo>=</mo><mfrac><mrow><msub><mi>I</mi><mn>0</mn></msub><mi>A</mi></mrow><mn>2</mn></mfrac><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mi>&#969;</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>.3</mo><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8722;</mo><mn>4</mn></mrow></msup></mrow><mn>2</mn></mfrac><mfrac><mrow><mn>3</mn><mo>.</mo><mn>14</mn></mrow><mrow><mn>31</mn><mo>.</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>&#8771;</mo><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi></math></p>

</details>

---

### Q22. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A polarizer - analyser set is adjusted such that the intensity of light coming out of the analyser is just <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn><mi>%</mi></math> of the original intensity. Assuming that the polarizer - analyser set does not absorb any light, the angle by which the analyser needs to be rotated further, to reduce the output intensity to zero, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>5</mn></mfrac></mfenced><mo>=</mo><mn>37</mn><mo>&#176;</mo></mrow></mfenced></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>53</mn><mi mathvariant="normal">o</mi></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>37</mn><mi mathvariant="normal">o</mi></msup></math>
- **(C)** <math><msup><mrow><mn>90</mn></mrow><mrow><mi mathvariant="normal">o</mi></mrow></msup></math>
- **(D)** <math><msup><mrow><mn>45</mn></mrow><mrow><mi mathvariant="normal">o</mi></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>37</mn><mi mathvariant="normal">o</mi></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msub><mi>I</mi><mn>0</mn></msub><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><msup><mi mathvariant="normal">s</mi><mn>2</mn></msup><mi mathvariant="normal">&#952;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>36</mn><msub><mi>I</mi><mn>0</mn></msub><mo>=</mo><msub><mi>I</mi><mn>0</mn></msub><msup><mi>cos</mi><mn>2</mn></msup><mi mathvariant="normal">&#952;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mi mathvariant="normal">&#952;</mi></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mn>53</mn><mo>&#176;</mo></math>
 
angle rotated should be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>90</mn><mi mathvariant="normal">o</mi></msup><mo>-</mo><msup><mn>53</mn><mi mathvariant="normal">o</mi></msup><mo>=</mo><msup><mn>37</mn><mi mathvariant="normal">o</mi></msup></math></p>

</details>

---

### Q23. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A system of three polarizers <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>3</mn></mrow></msub></math> is set up such that the pass axis of <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>3</mn></mrow></msub></math> is crossed with respect to that of <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub></math> . The pass axis of <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is inclined at <math><msup><mrow><mn>60</mn></mrow><mrow><mi mathvariant="normal">o</mi></mrow></msup></math> to the pass axis of <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>.</mo></math> When a beam of unpolarized light of intensity <math><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mi mathvariant="normal">o</mi></mrow></msub></math> is incident on <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo></math> the intensity of light transmitted by the three polarizers is <math><mi mathvariant="normal">I</mi></math> . The ratio <math><mfenced separators="|"><mrow><mrow><mrow><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mi mathvariant="normal">o</mi></mrow></msub></mrow><mo>/</mo><mrow><mi mathvariant="normal">I</mi></mrow></mrow></mrow></mfenced></math> equals (nearly):

**Options:**

- **(A)** <math><mn>5.33</mn></math>
- **(B)** <math><mn>16.00</mn></math>
- **(C)** <math><mn>1.80</mn></math>
- **(D)** <math><mn>10.67</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>10.67</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/359618b3-b40d-4628-b061-67c8a799dc18-image.png" style="width: 604px; height: 147px;" />
The intensity of light coming out of 1st Polaroid will be <math><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn></mrow></mfrac></math>
From Malus law <math><mi mathvariant="normal">I</mi><mo>=</mo><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></math>
From Polaroid 2: <math><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>30</mn><mo>&#176;</mo></mrow></mrow><mo>=</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>3</mn><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>8</mn></mrow></mfrac></math>
From Polaroid 3: <math><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mrow><mn>3</mn><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>8</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>60</mn><mo>&#176;</mo></mrow></mrow><mo>=</mo><mfrac><mrow><mn>3</mn><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>8</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>3</mn><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>32</mn></mrow></mfrac></math>
Now, <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">I</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>32</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mn>10.67</mn></math>

</details>

---

### Q24. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider a tank made of glass (refractive index <math><mn>1.5</mn></math> ) with a thick bottom. It is filled with a liquid of refractive index <math><mi>&#956;</mi><mo>.</mo></math> A student finds that, irrespective of what the incident angle <math><mi>i</mi></math> (see figure) is for a beam of light entering the liquid, the light reflected from the liquid glass interface is never completely polarized. For this to happen, the minimum value of <math><mi>&#956;</mi></math> is:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/eifuxtqcpovatxmolgmigpjhuijueoiwbcibepjlijkpahegko.png" />

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><msqrt><mn>5</mn></msqrt></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(D)** <math><msqrt><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>3</mn></mrow><mrow><msqrt><mn>5</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/wrdszehlkazjhgodgeswfkowszafgbaazattifyxzuxcoonyck.png" />

For reflected light not be completely polarized,

<math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>r</mi><mo>≠</mo><mfrac><mrow><msub><mrow><mi>μ</mi></mrow><mrow><mi>g</mi></mrow></msub></mrow><mrow><msub><mrow><mi>μ</mi></mrow><mrow><mi>w</mi></mrow></msub></mrow></mfrac></mrow></mrow><mo>=</mo><mfrac><mrow><mn>1.5</mn></mrow><mrow><mi>μ</mi></mrow></mfrac></math>

For minimum <math><mi>μ</mi><mi> </mi><mi>r</mi></math> is maximum. <math><mi>r</mi></math> is maximum when <math><mi>i</mi></math> is maximum i.e. <math><mi>i</mi><mo>=</mo><msup><mrow><mn>90</mn></mrow><mrow><mi>o</mi></mrow></msup></math>

<math><mo>⇒</mo><mi> </mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>r</mi></mrow></mrow><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>μ</mi></mrow></mfrac></math>

<math><mo>⇒</mo><mi> </mi><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>r</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><msup><mrow><mi>μ</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac></mrow></mrow></math>

<math><mo>∴</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><msup><mrow><mi>μ</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1.5</mn></mrow><mrow><mi>μ</mi></mrow></mfrac></math>

<math><mo>⇒</mo><mi> </mi><msup><mrow><mi>μ</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>2.25</mn><mi> </mi><mfenced separators="|"><mrow><msup><mrow><mi>μ</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<math><mo>⇒</mo><mi> </mi><mn>1.25</mn><mi> </mi><msup><mrow><mi>μ</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>2.25</mn></math>

<math><mo>⇒</mo><mi> </mi><mi> </mi><mi>μ</mi><mo>=</mo><msqrt><mfrac><mrow><mn>2.25</mn></mrow><mrow><mn>1.25</mn></mrow></mfrac></msqrt></math>

<math><mo>=</mo><msqrt><mfrac><mrow><mn>9</mn></mrow><mrow><mn>5</mn></mrow></mfrac></msqrt><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><msqrt><mn>5</mn></msqrt></mrow></mfrac></math>

</details>

---

### Q25. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Unpolarized light of intensity <math><mi>I</mi></math> is incident on a system of two polarizers, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> followed by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>. The intensity of emergent light is <math><mfrac><mrow><mi>I</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math> . If a third the polarizer <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is placed between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> the intensity of emergent light is reduced to <math><mfrac><mrow><mi>I</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math> . The angle between the polarizers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is <math><mi>&#952;</mi></math> , then

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></math>
- **(B)** <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></math>
- **(C)** <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></math>
- **(D)** <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1e8b5476-fd1e-4f3d-823b-b0e615403d75-image.png" style="width: 350px; height: 162px;" />

A and B have the same alignment of the transmission axis. Let&#39;s assume <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is introduced at <math><mi>&#952;</mi></math> angle, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn mathvariant="italic">I</mn><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#215;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mfrac><mn mathvariant="italic">I</mn><mn>3</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>&#952;</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><msup><mfenced separators="|"><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></math>.

</details>

---

### Q26. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `2`

A plane polarized light is incident on a polariser with its pass axis making angle $\theta$ with $\mathrm{x}$-axis, as shown in the figure. At four different values of $\theta, \theta=8^{\circ}, 38^{\circ}, 188^{\circ}$ and $218^{\circ}$, the observed intensities are same. What is the angle between the direction of polarization and $\mathrm{x}$-axis
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5JXaihObAF_Ku3LMDxD-HCcgbc5sO6BCSUkLJ_3Mpvo.original.fullsize.png">

**Options:**

- **(A)** $203^{\circ}$
- **(B)** $45^{\circ}$
- **(C)** $98^{\circ}$
- **(D)** $128^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $203^{\circ}$**

**Detailed Solution:**

No Solution Available

</details>

---

### Q27. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Unpolarized light of intensity <math xmlns="http://www.w3.org/1998/Math/MathML"><mn mathvariant="italic">I</mn></math> passes through an ideal polariser <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. Another identical polariser <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is placed behind <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. The intensity of light beyond B is found to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn mathvariant="italic">I</mn><mn>2</mn></mfrac></math>. Now another identical polariser <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is placed between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>. The intensity beyond B is now found to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn mathvariant="italic">I</mn><mn>8</mn></mfrac></math> . The angle between polariser <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>&#176;</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#176;</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#176;</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>&#176;</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>&#176;</mo></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b7c55f32-42a2-4b6f-b7e6-a1f738bd94cf-image.png" style="width: 250px; height: 184px;" />

Transformation axis <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are parallel. If the transformation axis of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is making angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#952;</mi></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>, it will make angle <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>90</mn><mo>&#8722;</mo><mi mathvariant="normal">&#952;</mi></mrow></mfenced></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>. Therefore,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>I</mi><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><msup><mi>&#952;cos</mi><mn>2</mn></msup><mrow><mo>(</mo><mn>90</mn><mo>&#8722;</mo><mi mathvariant="normal">&#952;</mi><mo>)</mo></mrow><mo>=</mo><mfrac><mi>I</mi><mn>8</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi mathvariant="normal">&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi mathvariant="normal">&#952;</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">&#952;</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math>

</details>

---

### Q28. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Unpolarized light of intensity <math><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></math> is incident on surface of a block of glass at Brewster's angle. In that case, which one of the following statements is true?

**Options:**

- **(A)** transmitted light is partially polarized with intensity <math><mfrac><mrow><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** transmitted light is completely polarized with intensity less than <math><mfrac><mrow><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** reflected light is partially polarized with intensity <math><mfrac><mrow><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** reflected light is completely polarized with intensity less than <math><mfrac><mrow><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) reflected light is completely polarized with intensity less than <math><mfrac><mrow><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

By polarizations due to reflection at a polarising angle reflected light is completely polarise and the intensity is less than average intensity <math><mfrac><mrow><msub><mrow><mi>I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn></mrow></mfrac></math>.

</details>

---

### Q29. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `1`

Two beams, A and B of plane polarized light with mutually perpendicular planes of polarization are seen through a polaroid. From the position when the beam A has maximum intensity (and beam B has zero intensity), a rotation of polaroid through 30<sup>o</sup> makes the two beams appear equally bright. If the initial intensities of the two beams are I<sub>A</sub> and I<sub>B</sub> respectively, then <math> <mrow> <mfrac> <mrow> <msub> <mtext>I</mtext> <mtext>A</mtext> </msub> </mrow> <mrow> <msub> <mtext>I</mtext> <mtext>B</mtext> </msub> </mrow> </mfrac> </mrow> </math> equals :

**Options:**

- **(A)** 3
- **(B)** <math> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(C)** 1
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<math> <mrow> <msub> <mtext>I</mtext> <mtext>A</mtext> </msub> <msup> <mtext>cos</mtext> <mn>2</mn> </msup> <mi>&#952;</mi> <mo>=</mo> <msub> <mtext>I</mtext> <mtext>B</mtext> </msub> <msup> <mtext>cos</mtext> <mn>2</mn> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mn>9</mn> <mn>0</mn> <mo>-</mo> <mi>&#952;</mi> </mrow> </mfenced> </mrow> </math>   <math display="block"> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mtext>I</mtext> <mo>=</mo> <msub> <mtext>I</mtext> <mn>0</mn> </msub> <msup> <mtext>cos</mtext> <mn>2</mn> </msup> <mi>&#952;</mi> </mrow> </mfenced> </mrow> </math> by malus equation

<math> <mrow> <mo>&#8756;&#160;&#160;&#160;</mo> <mfrac> <mrow> <msub> <mtext>I</mtext> <mtext>A</mtext> </msub> </mrow> <mrow> <msub> <mtext>I</mtext> <mtext>B</mtext> </msub> </mrow> </mfrac> <mo>=</mo> <msup> <mtext>tan</mtext> <mn>2</mn> </msup> <mi>&#952;</mi> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </math>

where <math> <mrow> <mi>&#952;</mi> <mo>=</mo> <mn>3</mn> <msup> <mn>0</mn> <mtext>o</mtext> </msup> </mrow> </math>

</details>

---

### Q30. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

A person lives in a high-rise building on the bank of a river $50 \mathrm{~m}$ wide. Across the river is a well lit tower of height $40 \mathrm{~m}$. When the person, who is at a height of $10 \mathrm{~m}$, looks through a polarizer at an appropriate angle at light of the tower reflecting from the river surface, he notes that intensity of light coming from distance $\mathrm{X}$ from his building is the least and this corresponds to the light coming from light bulbs at height ' $\mathrm{Y}$ ' on the tower. The values of $\mathrm{X}$ and $\mathrm{Y}$ are respectively close to (refractive index of water $\simeq \frac{4}{3}$ )
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/w_KVq_jn1q4obXVY-2dEduDQaUddFg3sAsKTqxmLnsM.original.fullsize.png">

**Options:**

- **(A)** $25 \mathrm{~m}, 10 \mathrm{~m}$
- **(B)** $13 \mathrm{~m}, 27 \mathrm{~m}$
- **(C)** $22 \mathrm{~m}, 13 \mathrm{~m}$
- **(D)** $17 \mathrm{~m}, 20 \mathrm{~m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $13 \mathrm{~m}, 27 \mathrm{~m}$**

**Detailed Solution:**

No Solution is Given.

</details>

---

### Q31. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `1`

A beam of unpolarised light of intensity <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub></math> is passed through a polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and then through another polaroid <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> which is oriented so that its principle plane makes an angle of <math> <mrow> <msup> <mtext>45</mtext> <mtext>o</mtext> </msup> </mrow> </math> relative to that of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. The intensity of the emergent light is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>8</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>I</mi><mn>0</mn></msub><mn>4</mn></mfrac></math>**

**Detailed Solution:**

Relation between intensities is

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM0010357_AnsExp1_1.jpg" />

<math> <mrow> <msub> <mtext>I</mtext> <mtext>R</mtext> </msub> <mo>=</mo> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <msub> <mtext>I</mtext> <mn>0</mn> </msub> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </mfenced> <msup> <mtext> cos</mtext> <mn>2</mn> </msup> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mtext>45</mtext> <mtext>o</mtext> </msup> </mrow> </mfenced> <mo>=</mo> <mfrac> <mrow> <msub> <mtext>I</mtext> <mn>0</mn> </msub> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>&times;</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <msub> <mtext>I</mtext> <mn>0</mn> </msub> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>

</details>

---

### Q32. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `1`

Two polaroids have their polarizing directions parallel so that the intensity of a transmitted light is maximum. The angle through which either polaroid must be turned if the intensity is to drop by one-half is

**Options:**

- **(A)** $135^{\circ}$
- **(B)** $90^{\circ}$
- **(C)** $120^{\circ}$
- **(D)** $180^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $135^{\circ}$**

**Detailed Solution:**

For $I=\frac{I_0}{2}$ and $I=I_0 \cos ^2 \theta=\frac{I_0}{2}$ $\therefore \theta=45^{\circ}$
Therefore the angle through which either polaroids turned is $135^{\circ}\left(=180^{\circ}-45^{\circ}\right)$

</details>

---

### Q33. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

When an unpolarized light of intensity $I_0$ is incident on a polarizing sheet, the intensity of the light which does not get transmitted is

**Options:**

- **(A)** $\frac{1}{2} \mathrm{I}_0$
- **(B)** $\frac{1}{4} \mathrm{I}_0$
- **(C)** zero
- **(D)** $\mathrm{I}_0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2} \mathrm{I}_0$**

**Detailed Solution:**

When unpolarised light of intensity $\mathrm{I}_0$ is incident on a polarizing sheet, only $\mathrm{I}_0 / 2$ is transmitted.

</details>

---

### Q34. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

The angle of incidence at which reflected light totally polarized for reflection from air to glass (refractive index $n$ ), is

**Options:**

- **(A)** $\sin ^{-1}(n)$
- **(B)** $\sin ^{-1}(1 / n)$
- **(C)** $\tan ^{-1}(1 / n)$
- **(D)** $\tan ^{-1}(n)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan ^{-1}(n)$**

**Detailed Solution:**

Brewster's law: According to this law the ordinary light is completely polarised in the plane of incidence when it gets reflected from transparent medium at a particular angle known as the angle of polarisation.
$$
\mathrm{n}=\tan \mathrm{i}_{\mathrm{p}}
$$

</details>

---

