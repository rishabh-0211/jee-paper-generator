# JEE Advanced Physics - Gravitation

## Topic 5: Motion of satellite

**Total Questions:** 7

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

A particle of mass $m$, and angular momentum $\ell$ is moving in a circular orbit of radius $r_0$ under the influence of an attractive force $\vec{F}(r) = -\dfrac{k}{r^2}\hat{r}$. Keeping its angular momentum unchanged, the particle is displaced radially by a small distance $\delta r \ll r_0$, due to which its radial distance varies periodically. The corresponding time period is:

**Options:**

- **(A)** $\dfrac{2\pi\ell^3}{m k^2}$
- **(B)** $2\pi\sqrt{\dfrac{m}{k}}$
- **(C)** $\dfrac{2\pi\ell^3}{3 m k^2}$
- **(D)** $\dfrac{2\pi\ell^3}{5 m k^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{2\pi\ell^3}{m k^2}$**

**Detailed Solution:**

The equation of motion for the radial distance $r$ is given by:

$m \dfrac{d^2r}{dt^2} = F(r) + \dfrac{\ell^2}{mr^3} = -\dfrac{k}{r^2} + \dfrac{\ell^2}{mr^3}$

For a circular orbit of radius $r_0$, the radial acceleration is zero:

$-\dfrac{k}{r_0^2} + \dfrac{\ell^2}{mr_0^3} = 0 \Rightarrow r_0 = \dfrac{\ell^2}{mk}$

Let the particle be displaced by a small distance $x$ such that $r = r_0 + x$. The restoring force is:

$m \dfrac{d^2x}{dt^2} = -\dfrac{k}{(r_0+x)^2} + \dfrac{\ell^2}{m(r_0+x)^3}$

Using the binomial expansion for $x \ll r_0$:

$m \dfrac{d^2x}{dt^2} \approx -\dfrac{k}{r_0^2}\left(1 - \dfrac{2x}{r_0}\right) + \dfrac{\ell^2}{mr_0^3}\left(1 - \dfrac{3x}{r_0}\right)$

Since $\dfrac{k}{r_0^2} = \dfrac{\ell^2}{mr_0^3}$, the constant terms cancel out:

$m \dfrac{d^2x}{dt^2} \approx \left( \dfrac{2k}{r_0^3} - \dfrac{3\ell^2}{mr_0^4} \right) x$

Substituting $\dfrac{\ell^2}{mr_0^4} = \dfrac{k}{r_0^3}$ into the equation:

$m \dfrac{d^2x}{dt^2} = \left( \dfrac{2k}{r_0^3} - \dfrac{3k}{r_0^3} \right) x = -\dfrac{k}{r_0^3} x$

This represents simple harmonic motion with angular frequency $\omega = \sqrt{\dfrac{k}{mr_0^3}}$.

The time period is $T = \dfrac{2\pi}{\omega} = 2\pi \sqrt{\dfrac{mr_0^3}{k}}$.

Substituting $r_0 = \dfrac{\ell^2}{mk}$:

$T = 2\pi \sqrt{\dfrac{m}{k} \left( \dfrac{\ell^2}{mk} \right)^3} = 2\pi \sqrt{\dfrac{m \ell^6}{k m^3 k^3}} = \dfrac{2\pi \ell^3}{m k^2}$

Answer: $\dfrac{2\pi\ell^3}{m k^2}$

</details>

---

### Q2. JEE Advanced 2025 (Paper 2)

*Type:* `numerical` | *Level:* `3`

A geostationary satellite above the equator is orbiting around the earth at a fixed distance $r_1$ from the center of the earth. A second satellite is orbiting in the equatorial plane in the opposite direction to the earth's rotation, at a distance $r_2$ from the center of the earth, such that $r_1=1.21 r_2$. The time period of the second satellite as measured from the geostationary satellite is $\frac{24}{p}$ hours. The value of $p$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2.33**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/jKpQ6HTfHtrSqMo-D_gFNvnqR3tEyJWKvMUd-dwYpQo.original.fullsize.png">
$\mathrm{T} \propto \mathrm{r}^{3 / 2}$
$\frac{\mathrm{T}_2}{\mathrm{~T}_1}=\left(\frac{\mathrm{r}_2}{\mathrm{r}_1}\right)^{3 / 2}$
$\frac{\omega_2}{\omega_1}=\left(\frac{r_1}{r_2}\right)^{3 / 2}=(1.21)^{3 / 2}$
$\begin{aligned}
& \omega_2=\omega_1(1.331) \qquad ...(i)\\
& \left(\omega_2+\omega_1\right) t_0=2 \pi \qquad ...(ii)
\end{aligned}$
$t_0=\frac{2 \pi}{\omega_2+\omega_1}=\frac{2 \pi}{\left(\frac{4}{3}+1\right) \omega_1}=\frac{6 \pi}{7 \omega_1}$
$\mathrm{t}_0=\frac{6 \pi}{2 \pi} \frac{\left(\mathrm{~T}_{\mathrm{GSS}}\right)}{(7)}$
$\mathrm{t}_0=\frac{3 \times 24 \text { hours }}{7}=\frac{24}{\mathrm{p}} \text { hours }$
$\mathrm{p}=\frac{7}{3}=2.33$

</details>

---

### Q3. JEE Advanced 2024 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

A particle of mass $m$ is under the influence of the gravitational field of a body of mass $M(\gg m)$. The particle is moving in a circular orbit of radius $r_0$ with time period $T_0$ around the mass $M$. Then, the particle is subjected to an additional central force, corresponding to the potential energy $V_{\mathrm{c}}(r)=m \alpha / r^3$, where $\alpha$ is a positive constant of suitable dimensions and $r$ is the distance from the center of the orbit. If the particle moves in the same circular orbit of radius $r_0$ in the combined gravitational potential due to $M$ and $V_{\mathrm{c}}(r)$, but with a new time period $T_1$, then $\left(T_1^2-T_0^2\right) / T_1^2$ is given by
[ $G$ is the gravitational constant.]

**Options:**

- **(A)** $\frac{3 \alpha}{G M r_0^2}$
- **(B)** $\frac{\alpha}{2 G M r_0^2}$
- **(C)** $\frac{\alpha}{G M r_0^2}$
- **(D)** $\frac{2 \alpha}{G M r_0^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3 \alpha}{G M r_0^2}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{F}_1=\frac{\mathrm{GMm}}{\mathrm{r}_0^2} \\ & \mathrm{~F}_2=\frac{\mathrm{GMm}}{\mathrm{r}_0^2}-\frac{3 \mathrm{~m} \alpha}{\mathrm{r}_0^4} \\ & \frac{\omega_1^2}{\omega_0^2}=\frac{\mathrm{F}_2}{\mathrm{~F}_1}=\frac{\frac{\mathrm{GM}}{\mathrm{r}_0^2}-\frac{3 \alpha}{\mathrm{r}_0^4}}{\frac{\mathrm{GM}}{\mathrm{r}_0^2}} \\ & \frac{\mathrm{T}_0^2}{\mathrm{~T}_1^2}=1-\frac{3 \alpha}{\mathrm{GMr}_0^2} \\ & \frac{\mathrm{T}_1^2-\mathrm{T}_0^2}{\mathrm{~T}_1^2}=\frac{3 \alpha}{\mathrm{GMr}_0^2}\end{aligned}$

</details>

---

### Q4. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `2`

<p>The distance between two stars of masses <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msub><mi mathvariant="normal">M</mi><mi>S</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msub><mi mathvariant="normal">M</mi><mi>S</mi></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi mathvariant="normal">R</mi></math>. Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is the mean distance between the centres of the Earth and the Sun, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>M</mi><mi>S</mi></msub></math> is the mass of the Sun. Two stars orbit around their common centre of mass in circular orbits with period <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>T</mi></math>, where<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is the period of Earth&#39;s revolution around the Sun.</p><p>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is _____.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>R</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><msqrt><mi>G</mi><msub><mi>M</mi><mi>S</mi></msub></msqrt></mfrac></math></p><p>For binary stars,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>&#39;</mo><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>r</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><msqrt><mi>G</mi><mfenced><mrow><msub><mi>M</mi><mn>1</mn></msub><mo>+</mo><msub><mi>M</mi><mn>2</mn></msub></mrow></mfenced></msqrt></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>M</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><msub><mi>M</mi><mi>S</mi></msub></math>,<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>M</mi><mn>2</mn></msub><mo>=</mo><mn>6</mn><msub><mi>M</mi><mi>S</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>9</mn><mi mathvariant="normal">R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>'</mo><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi><mo>&#215;</mo><msup><mn>9</mn><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>&#215;</mo><msup><mi>R</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><msqrt><mi>G</mi><mfenced><mrow><mn>3</mn><msub><mi>M</mi><mi>S</mi></msub><mo>+</mo><mn>6</mn><msub><mi>M</mi><mi>S</mi></msub></mrow></mfenced></msqrt></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi><mo>&#215;</mo><msup><mn>9</mn><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>&#215;</mo><msup><mi>R</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><mrow><msup><mn>9</mn><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msqrt><mi>G</mi><msub><mi>M</mi><mi>S</mi></msub></msqrt></mrow></mfrac><mo>=</mo><mn>9</mn><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>R</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><msqrt><mi>G</mi><msub><mi>M</mi><mi>S</mi></msub></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mi>T</mi><mo>&#39;</mo><mo>=</mo><mn>9</mn><mi>T</mi></math></p><p>Value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>9</mn></math>.</p>

</details>

---

### Q5. JEE Advanced 2018 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

A planet of mass M, has two natural satellites with masses <math><msub><mrow><mi>m</mi></mrow><mrow><mn>1</mn></mrow></msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><msub><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msub></math> . The radii of their circular orbits are <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi>&#160;</mi><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math> respectively. Ignore the gravitational force between the satellites. Define <math><msub><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>L</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>K</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi>&#160;</mi><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub></math> to be, respectively, the orbital speed, angular momentum, kinetic energy and time period of revolution of satellite <math><mn>1</mn><mo>;</mo><mi>&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi>&#160;</mi><msub><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><msub><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><msub><mrow><mi>K</mi></mrow><mrow><mn>2</mn></mrow></msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi>&#160;</mi><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub></math> and to be the corresponding quantities of satellite 2. Given <math><mrow><mrow><msub><mrow><mi>m</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mo>/</mo><mrow><msub><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mrow><mo>=</mo><mn>2</mn><mi>&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi>&#160;</mi><mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mo>/</mo><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mrow><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math> , match the ratios in List-I to the numbers in List-II.<table border="1">	<tbody>		<tr>			<td> </td>			<td>LIST -I</td>			<td> </td>			<td>LIST-II</td>		</tr>		<tr>			<td>A)</td>			<td><math><mfrac><mrow><msub><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></math></td>			<td>P)</td>			<td><math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math></td>		</tr>		<tr>			<td>B)</td>			<td><math><mfrac><mrow><msub><mrow><mi>L</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></math></td>			<td>Q)</td>			<td>1</td>		</tr>		<tr>			<td>C)</td>			<td><math><mfrac><mrow><msub><mrow><mi>K</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>K</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></math></td>			<td>R)</td>			<td>2</td>		</tr>		<tr>			<td>D)</td>			<td><math><mfrac><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></math></td>			<td>S)</td>			<td>8</td>		</tr>	</tbody></table>

**Options:**

- **(A)** a-p;b-q;c-s;d-r;
- **(B)** a-s;b-p;c-r;d-q;
- **(C)** a-s;b-q;c-r;d-p;
- **(D)** a-r;b-q;c-s;d-p;

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) a-r;b-q;c-s;d-p;**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/luifxbqbcwonrutsrttkrvnnaemralajxbaoexvmgviezymthl.jpeg"/>
<math><mfenced close="}" open="" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><msub><mrow><mi>m</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mn>2</mn></mtd></mtr><mtr><mtd><mfrac><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mtd></mtr></mtable></mrow></mfenced></math> given
<math><mfrac><mrow><mi>G</mi><mi>M</mi><msub><mrow><mi>m</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msubsup><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mrow><mi>m</mi></mrow><mrow><mn>1</mn></mrow></msub><msubsup><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>1</mn></mrow></msubsup></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac></math>
<math><msubsup><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mi>G</mi><mi>M</mi></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>,</mo><msubsup><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mi>G</mi><mi>M</mi></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></math>
<math><mfrac><mrow><msubsup><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow><mrow><msubsup><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>=</mo><mn>4</mn></math>
<math><mfenced separators="|"><mrow><mi>i</mi></mrow></mfenced></math> <math><mfrac><mrow><msub><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mn>2</mn></math>
<math><mfenced separators="|"><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> <math><mi>L</mi><mo>=</mo><mi>m</mi><mi>v</mi><mi>R</mi></math>
<math><mfrac><mrow><msub><mrow><mi>L</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mrow><mi>m</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msub><msub><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msub><mi> </mi><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mn>2</mn><mo>×</mo><mn>2</mn><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mn>1</mn></math>
<math><mfenced separators="|"><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math> <math><mi>K</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>m</mi><msup><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mfrac><mrow><msub><mrow><mi>K</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>K</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mrow><mi>m</mi></mrow><mrow><mn>1</mn></mrow></msub><msubsup><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow><mrow><msub><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msub><msubsup><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>=</mo><mn>2</mn><mo>×</mo><msup><mrow><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>8</mn></math>
<math><mo>(</mo><mi>i</mi><mi>v</mi><mo>)</mo></math> <math><mi>T</mi><mo>=</mo><mrow><mrow><mn>2</mn><mi>π</mi><mi>R</mi></mrow><mo>/</mo><mrow><mi>V</mi></mrow></mrow></math>
<math><mfrac><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>×</mo><mfrac><mrow><msub><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>×</mo><mfrac><mrow><msub><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msub><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>

</details>

---

### Q6. JEE Advanced 2010 (Paper 1)

*Type:* `numerical` | *Level:* `2`

A binary star consists of two stars $A$ (mass $2.2 M_S$ ) and $B$ (mass $11 M_s$ ), where $M_S$ is the mass of the sun. They are separated by distance $d$ and are rotating about their centre of mass, which is stationary. The ratio of the total angular momentum of the binary star to the angular momentum of $\operatorname{star} B$ about the centre of mass is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

$\frac{L_{\text {Total }}}{L_B}=\frac{\left(I_A+I_B\right) \omega}{I_B \cdot \omega}$ (as $\omega$ will be same in both cases)
$$
\begin{aligned}
& =\frac{I_A}{I_B}+1=\frac{m_A r_A^2}{m_B r_B^2}+1 \\
& \left.=\frac{r_A}{r_B}+1 \quad \quad \text { (as } m_A r_A=m_B r_B\right) \\
& =\frac{11}{2.2}+1 \quad \quad\left(\text { as } r \propto \frac{1}{m}\right) \\
& =6
\end{aligned}
$$
$\therefore$ The correct answer is 6 .

</details>

---

### Q7. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `2`

A double star system consists of two stars $A$ and $B$ which have time period $T_A$ and $T_B$. Radius $R_A$ and $R_B$ and mass $M_A$ and $M_B$. Choose the correct option.

**Options:**

- **(A)** If $T_A>T_B$, then $R_A>R_B$
- **(B)** If $T_A>T_B$, then $M_A>M_B$
- **(C)** $\left(\frac{T_A}{T_B}\right)^2=\left(\frac{R_A}{R_B}\right)^3$
- **(D)** $T_A=T_B$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $T_A=T_B$**

**Detailed Solution:**

In case of binary star system angular velocity and hence the time period of both the stars are equal.

</details>

---

