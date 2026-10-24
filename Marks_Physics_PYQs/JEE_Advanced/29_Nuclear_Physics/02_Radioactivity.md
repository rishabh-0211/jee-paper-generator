# JEE Advanced Physics - Nuclear Physics

## Topic 2: Radioactivity

**Total Questions:** 17

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

A nuclear reactor starts producing a radioactive nuclide $X$ from $t = 0$, at a constant rate of $\alpha$ per second. Each decay of $X$ produces energy $E_0$, which is utilized to heat a liquid of mass $m$ and specific heat $s$. Assuming no heat loss from the liquid and taking $\lambda$ as the decay constant of $X$, the rate of increase in the temperature of the liquid is:

**Options:**

- **(A)** $\dfrac{\alpha E_0}{m s}(1 - e^{-\lambda t})$
- **(B)** $\dfrac{\alpha E_0}{m s}(e^{\lambda t} - 1)$
- **(C)** $\dfrac{\lambda E_0}{m s}(1 - e^{-\lambda t})$
- **(D)** $\dfrac{E_0}{m s}(\alpha - \lambda e^{-\lambda t})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\alpha E_0}{m s}(1 - e^{-\lambda t})$**

**Detailed Solution:**

Let $N$ be the number of active nuclei at time $t$. The rate of change of the number of nuclei is given by

$\dfrac{dN}{dt} = \alpha - \lambda N$

Integrating with the initial condition $N = 0$ at $t = 0$:

$\int_{0}^{N} \dfrac{dN}{\alpha - \lambda N} = \int_{0}^{t} dt$

$-\dfrac{1}{\lambda} \ln\left(\dfrac{\alpha - \lambda N}{\alpha}\right) = t$

$N = \dfrac{\alpha}{\lambda} (1 - e^{-\lambda t})$

The rate of decay of the nuclide at time $t$ is

$A = \lambda N = \alpha (1 - e^{-\lambda t})$

Since each decay produces energy $E_0$, the rate of energy production is

$\dfrac{dE}{dt} = A E_0 = \alpha E_0 (1 - e^{-\lambda t})$

This energy is used to heat the liquid. The rate of heat absorption is

$\dfrac{dQ}{dt} = m s \dfrac{dT}{dt}$

Equating the rate of energy production to the rate of heat absorption:

$m s \dfrac{dT}{dt} = \alpha E_0 (1 - e^{-\lambda t})$

$\dfrac{dT}{dt} = \dfrac{\alpha E_0}{m s} (1 - e^{-\lambda t})$

Answer: $\dfrac{\alpha E_0}{m s}(1 - e^{-\lambda t})$

</details>

---

### Q2. JEE Advanced 2023 (Paper 2)

*Type:* `numerical` | *Level:* `2`

In a radioactive decay process, the activity is defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi>d</mi><mi>N</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>(</mo><mi>t</mi><mo>)</mo></math> is the number of radioactive nuclei at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>t</mi></mfenced></math>. Two radioactive sources, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> have same activity at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math>. At a later time, the activities of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub></math>, respectively. When <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> have just completed their <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mi>rd</mi></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mi>th</mi></msup></math> half-lives, respectively, the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>A</mi><mn>1</mn></msub><msub><mi>A</mi><mn>2</mn></msub></mfrac></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<blockquote><p>Activity for both the cases can be written as, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><msub><mi>A</mi><mn>0</mn></msub><msup><mi>e</mi><mrow><mo>-</mo><msub><mi>&#955;</mi><mn>1</mn></msub><msub><mi>t</mi><mn>1</mn></msub></mrow></msup></math></p><p>also <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><msub><mi>A</mi><mn>0</mn></msub><msup><mi>e</mi><mrow><mo>-</mo><msub><mi>&#955;</mi><mn>2</mn></msub><msub><mi>t</mi><mn>2</mn></msub></mrow></msup></math>.</p><p>Half-life for the reaction can be written as, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><msub><mi>t</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msub></mfenced><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>ln</mi><mn>2</mn></mrow><msub><mi>&#955;</mi><mn>1</mn></msub></mfrac></math> and hence</p><p>at <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>3</mn><mi>ln</mi><mn>2</mn></mrow><msub><mi>&#955;</mi><mn>1</mn></msub></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><msub><mi>A</mi><mn>0</mn></msub><msup><mi>e</mi><mrow><mo>-</mo><msub><mi>&#955;</mi><mn>1</mn></msub><mfenced><mfrac><mrow><mn>3</mn><mi>ln</mi><mn>2</mn></mrow><msub><mi>&#955;</mi><mn>1</mn></msub></mfrac></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><msub><mi>A</mi><mn>0</mn></msub><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn><mi>ln</mi><mn>2</mn></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Similarly, for the second case, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mn>2</mn></msub><mo>=</mo><mn>7</mn><mfenced><mfrac><mrow><mi>ln</mi><mn>2</mn></mrow><msub><mi>&#955;</mi><mn>2</mn></msub></mfrac></mfenced></math> and therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><msub><mi>A</mi><mn>0</mn></msub><msup><mi>e</mi><mrow><mo>-</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mfenced><mfrac><mrow><mn>7</mn><mi>ln</mi><mn>2</mn></mrow><msub><mi>&#955;</mi><mn>2</mn></msub></mfrac></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><msub><mi>A</mi><mn>0</mn></msub><msup><mi>e</mi><mrow><mo>-</mo><mn>7</mn><mi>ln</mi><mn>2</mn></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>A</mi><mn>1</mn></msub><msub><mi>A</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><msub><mi>A</mi><mn>0</mn></msub><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn><mi>ln</mi><mn>2</mn></mrow></msup></mrow><mrow><msub><mi>A</mi><mn>0</mn></msub><msup><mi>e</mi><mrow><mo>-</mo><mn>7</mn><mi>ln</mi><mn>2</mn></mrow></msup></mrow></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mrow><msub><mi>A</mi><mn>0</mn></msub><msup><mi>e</mi><mrow><mi>ln</mi><msup><mn>2</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></msup></mrow><mrow><msub><mi>A</mi><mn>0</mn></msub><msup><mi>e</mi><mrow><mi>ln</mi><msup><mn>2</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><msup><mn>2</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mn>2</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup></mfrac><mo>=</mo><mn>16</mn></math></p><p>Therefore, required ration would be<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfrac><msub><mi>A</mi><mn>1</mn></msub><msub><mi>A</mi><mn>2</mn></msub></mfrac><mo>=</mo><mn>16</mn></math></p></blockquote>

</details>

---

### Q3. JEE Advanced 2023 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> shows different radioactive decay processes and List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> provides possible emitted particles. Match each entry in List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> with an appropriate entry from List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math>, and choose the correct option.</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td style="text-align: center;">List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math></td>			<td style="text-align: center;"> </td>			<td style="text-align: center;">List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><msup><mrow></mrow><mn>238</mn></msup><mn>92</mn></msub><mi>U</mi><msub><msup><mo>&#8594;</mo><mn>234</mn></msup><mn>91</mn></msub><mi>P</mi><mi>a</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td>one <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> particle and one <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mo>+</mo></msup></math> particle</td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Q</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><msup><mrow></mrow><mn>214</mn></msup><mn>82</mn></msub><mi>P</mi><mi>b</mi><msub><msup><mo>&#8594;</mo><mn>210</mn></msup><mn>82</mn></msub><mi>P</mi><mi>b</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td>three <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mo>-</mo></msup></math> particles and one <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> particle</td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><msup><mrow></mrow><mn>210</mn></msup><mn>81</mn></msub><mi>T</mi><mi>l</mi><msub><msup><mo>&#8594;</mo><mn>206</mn></msup><mn>82</mn></msub><mi>P</mi><mi>b</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td>two <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mo>-</mo></msup></math> particles and one <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> particle</td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><msup><mrow/><mn>228</mn></msup><mn>91</mn></msub><mi>P</mi><mi>a</mi><msub><msup><mo>&#8594;</mo><mn>224</mn></msup><mn>88</mn></msub><mi>R</mi><mi>a</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td>one <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> particle and one <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mo>-</mo></msup></math> particle</td>		</tr>		<tr>			<td> </td>			<td> </td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>			<td>one <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> particle and two <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mo>+</mo></msup></math> particles</td>		</tr>	</tbody></table>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>&#8594;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">Q</mi><mo>&#8594;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#8594;</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>&#8594;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">Q</mi><mo>&#8594;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#8594;</mo><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>&#8594;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">Q</mi><mo>&#8594;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#8594;</mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>&#8594;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">Q</mi><mo>&#8594;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#8594;</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>&#8594;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">Q</mi><mo>&#8594;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#8594;</mo><mn>1</mn></math>**

**Detailed Solution:**

<blockquote><p>In <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> decay mass number decreases by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> unit and atomic number decreases by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> unit.</p><p>In <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mo>-</mo></msup></math> decay mass number does not change but atomic number increases by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> unit.</p><p>In <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mo>+</mo></msup></math> decay mass number does not change but atomic number decreases by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> unit.</p><p>So for</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>P</mi></mfenced><msub><msup><mo>&#160;</mo><mn>238</mn></msup><mn>92</mn></msub><mi>U</mi><msub><msup><mo>&#8594;</mo><mn>234</mn></msup><mn>91</mn></msub><mi>P</mi><mi>a</mi></math>.</p><p>Number of alpha particle <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>238</mn><mo>-</mo><mn>234</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mn>1</mn></math>. Due to alpha particle, atomic number should decrease by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> but it has decreased by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> only, therefore an additional <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mo>-</mo></msup></math> decay is required, then net change in atomic number will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>1</mn></math>. Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>&#8594;</mo><mn>4</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>Q</mi></mfenced><msub><msup><mo>&#160;</mo><mn>214</mn></msup><mn>82</mn></msub><mi>P</mi><mi>b</mi><msub><msup><mo>&#8594;</mo><mn>210</mn></msup><mn>82</mn></msub><mi>P</mi><mi>b</mi></math>.</p><p>Number of alpha particle <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>214</mn><mo>-</mo><mn>210</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mn>1</mn></math>. Due to alpha particle, atomic number should decrease by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, but there is no change in atomic number, which means two additional <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mo>-</mo></msup></math> decay is required, then net change in atomic number will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>. Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Q</mi><mo>&#8594;</mo><mn>3</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>R</mi></mfenced><msub><msup><mo>&#160;</mo><mn>210</mn></msup><mn>81</mn></msub><mi>T</mi><mi>l</mi><msub><msup><mo>&#8594;</mo><mn>206</mn></msup><mn>82</mn></msub><mi>P</mi><mi>b</mi></math>.</p><p>Number of alpha particle <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>210</mn><mo>-</mo><mn>206</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mn>1</mn></math>. Due to alpha particle, atomic number should decrease by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, but atomic number has increased by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>, which means three additional <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mo>-</mo></msup></math> decay is required, then net change in atomic number will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>1</mn></math>. Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mn>2</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>S</mi></mfenced><msub><msup><mo>&#160;</mo><mn>228</mn></msup><mn>91</mn></msub><mi>P</mi><mi>a</mi><msub><msup><mo>&#8594;</mo><mn>224</mn></msup><mn>88</mn></msub><mi>R</mi><mi>a</mi></math>.</p><p>Number of alpha particle <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>228</mn><mo>-</mo><mn>224</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mn>1</mn></math>. Due to alpha particle, atomic number should decrease by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, but atomic number has decreased by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>, which means one additional <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mo>+</mo></msup></math> is required, then net change in atomic number will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>-</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>3</mn></math>. Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>&#8594;</mo><mn>1</mn></math>.</p></blockquote>

</details>

---

### Q4. JEE Advanced 2022 (Paper 2)

*Type:* `numerical` | *Level:* `1`

In a radioactive decay chain reaction, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mrow/><mn>90</mn><mn>230</mn></msubsup><mi>Th</mi></math> nucleus decays into <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>Po</mi><mprescripts/><mn>84</mn><mn>214</mn></mmultiscripts></math> nucleus. The ratio of the number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> to number of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mo>-</mo></msup></math> particles emitted in this process is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<blockquote><p>Let number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> particles are <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mi>&#945;</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> particles are <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mi>&#946;</mi></msub></math>.</p><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow/><mn>90</mn></msub><msup><mi>Th</mi><mn>230</mn></msup><msub><mo stretchy="false">&#8594;</mo><mn>84</mn></msub><msup><mi>Po</mi><mn>214</mn></msup><mo>+</mo><msub><mi>n</mi><mi>&#945;</mi></msub><mi>&#945;</mi><mo>+</mo><msub><mi>n</mi><mi>&#946;</mi></msub><mi>&#946;</mi></math>.</p><p>Change in mass number is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>230</mn><mo>-</mo><mn>214</mn><mo>=</mo><mn>4</mn><msub><mi>n</mi><mi>&#945;</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>n</mi><mi>&#945;</mi></msub><mo>=</mo><mn>4</mn></math></p><p>Number of proton, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mi>&#946;</mi></msub><mo>=</mo><mn>84</mn><mo>-</mo><mfenced><mrow><mn>90</mn><mo>-</mo><mn>2</mn><msub><mi>n</mi><mi>a</mi></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>n</mi><mi>&#946;</mi></msub><mo>=</mo><mn>2</mn></math></p><p>So, the ratio, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>n</mi><mi>&#945;</mi></msub><msub><mi>n</mi><mi>&#946;</mi></msub></mfrac><mo>=</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q5. JEE Advanced 2021 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

A heavy nucleus <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> of half-life <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> minutes undergoes alpha-decay with probability of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>%</mo></math>  and beta-decay with probability of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>%</mo></math>. Initially, the number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> nuclei is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math>. The number of alpha-decays of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> in the first one hour is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>75</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>350</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>525</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>525</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msub><mo>=</mo><mn>20</mn><mo>&#160;</mo><mi>min</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>N</mi><mn>0</mn></msub><mo>=</mo><mn>1000</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>1</mn><mo>&#160;</mo><mi>hour</mi><mo>=</mo><mn>60</mn><mo>&#160;</mo><mi>min</mi><mo>=</mo><mn>3</mn><msub><mi>T</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Number of nuclei remain after <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> hour,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><mfrac><msub><mi>N</mi><mi>o</mi></msub><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>=</mo><mfrac><mn>1000</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>N</mi><mo>=</mo><mn>125</mn></math></p><p>It means <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>875</mn></math> nuclei has decayed,</p><p>Now,</p><p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> decayed Nucleus</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>875</mn><mo>&#215;</mo><mn>60</mn></mrow><mn>100</mn></mfrac><mo>=</mo><mn>525</mn></math></p>

</details>

---

### Q6. JEE Advanced 2019 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>In a radioactive sample, <math><msubsup><mrow><mi mathvariant="normal"> </mi></mrow><mrow><mn>19</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi mathvariant="normal">K</mi></math> nuclei either decay into stable <math><msubsup><mrow><mi mathvariant="normal"> </mi></mrow><mrow><mn>20</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi mathvariant="normal">C</mi><mi mathvariant="normal">a</mi></math> nuclei with decay constant <math><mn>4.5</mn><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></math> per year or into stable <math><msubsup><mrow><mi mathvariant="normal"> </mi></mrow><mrow><mn>18</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi mathvariant="normal">A</mi><mi mathvariant="normal">r</mi></math> nuclei with decay constant <math><mn>0.5</mn><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></math> per year. Given that in this sample all the stable <math><msubsup><mrow><mi mathvariant="normal"> </mi></mrow><mrow><mn>20</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi mathvariant="normal">C</mi><mi mathvariant="normal">a</mi></math> and <math><msubsup><mrow><mi mathvariant="normal"> </mi></mrow><mrow><mn>18</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi mathvariant="normal">A</mi><mi mathvariant="normal">r</mi></math> nuclei are produced by the <math><msubsup><mrow><mi mathvariant="normal"> </mi></mrow><mrow><mn>19</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi mathvariant="normal">K</mi></math> nuclei only. In time <math><mi mathvariant="normal">t</mi><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>9</mn></mrow></msup></math> years, if the ratio of the sum of stable <math><msubsup><mrow><mi mathvariant="normal"> </mi></mrow><mrow><mn>20</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi mathvariant="normal">C</mi><mi mathvariant="normal">a</mi></math> and <math><msubsup><mrow><mi mathvariant="normal"> </mi></mrow><mrow><mn>18</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi mathvariant="normal">A</mi><mi mathvariant="normal">r</mi></math> nuclei to the radioactive <math><msubsup><mrow><mi mathvariant="normal"> </mi></mrow><mrow><mn>19</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi mathvariant="normal">K</mi></math> nuclei is <math><mn>99</mn><mo>,</mo></math> the value of t will be : [Given <math><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal"> </mi><mn>10</mn><mo>=</mo><mn>2.3</mn></math> ]
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/xycwymmewvkdmpybreczihkxuiuyrmeqtmexumbwjrzltamsyi.png"/></p>

**Options:**

- **(A)** <math><mn>1.15</mn></math>
- **(B)** <math><mn>2.3</mn></math>
- **(C)** <math><mn>4.6</mn></math>
- **(D)** <math><mn>9.2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>9.2</mn></math>**

**Detailed Solution:**

Given that,  <math><msubsup><mrow><mi> </mi></mrow><mrow><mn>19</mn></mrow><mrow><mn>49</mn></mrow></msubsup><mi>K</mi></math>  decays in two stable  <math><msubsup><mrow><mi> </mi></mrow><mrow><mn>20</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi>C</mi><mi>a</mi><mi> </mi><mi>o</mi><mi>f</mi><mi> </mi><msubsup><mrow><mi> </mi></mrow><mrow><mn>18</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi>A</mi><mi>r</mi><mi> </mi></math> Nuclei. Let there be  <math><msub><mrow><mi>N</mi></mrow><mrow><mn>0</mn></mrow></msub></math>  active nuclei of  <math><msubsup><mrow><mi> </mi></mrow><mrow><mn>19</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi>K</mi></math>  present at  <math><mi>t</mi><mo>=</mo><mn>0</mn></math>  and none of  <math><msubsup><mrow><mi> </mi></mrow><mrow><mn>20</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi>C</mi><mi>a</mi></math>  and  <math><msubsup><mrow><mi> </mi></mrow><mrow><mn>18</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi>A</mi><mi>r</mi></math>  present of  <math><mi>t</mi><mo>=</mo><mn>0</mn></math> .
Where  <math><msub><mrow><mi>λ</mi></mrow><mrow><mn>1</mn></mrow></msub></math>  (decay constant for  <math><mi>K</mi><mo>→</mo><mi>C</mi><mi>a</mi></math> )  <math><mo>=</mo><mn>4.5</mn><mo>×</mo><mfrac><mrow><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">y</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi></mrow></mfrac></math>  and
 <math><msub><mrow><mi>λ</mi></mrow><mrow><mn>2</mn></mrow></msub></math>  (decay constant for  <math><mi>K</mi><mo>→</mo><mi>A</mi><mi>r</mi></math> )  <math><mo>=</mo><mn>0.5</mn><mo>×</mo><mfrac><mrow><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">y</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi></mrow></mfrac></math> 
These form two parallel nuclear reactions.
 <math><mo>∴</mo></math>  Equivalent decay consent,  <math><mi>λ</mi><mo>=</mo><msub><mrow><mi>λ</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>λ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>5</mn><mo>×</mo><mfrac><mrow><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">y</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi></mrow></mfrac></math> 
Now, number of active nuclei of  <math><msubsup><mrow><mi> </mi></mrow><mrow><mn>19</mn></mrow><mrow><mn>40</mn></mrow></msubsup><mi>K</mi></math>  left at  <math><mfenced separators="|"><mrow><mi>t</mi><mo>=</mo><mi>t</mi></mrow></mfenced><mo>=</mo><mi>N</mi></math> 
And according to Law of Radioactivity,
 <math><mi>N</mi><mo>=</mo><msub><mrow><mi>N</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>λ</mi><mi>t</mi></mrow></msup></math>  ........(i)
Now, according to question,
 <math><mfrac><mrow><msub><mrow><mi>N</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>-</mo><mi>N</mi></mrow><mrow><mi>N</mi></mrow></mfrac><mo>=</mo><mn>99</mn><mo>⇒</mo><msub><mrow><mi>N</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>100</mn><mi>N</mi><mo>⇒</mo><mi>N</mi><mo>=</mo><mfrac><mrow><msub><mrow><mi>N</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>100</mn></mrow></mfrac></math> 
Then using equation (i)
 <math><mfrac><mrow><msub><mrow><mi>N</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>100</mn></mrow></mfrac><mo>=</mo><msub><mrow><mi>N</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>λ</mi><mi>t</mi></mrow></msup></math> 
 <math><mo>⇒</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mtext> </mtext><mn>100</mn><mo>=</mo><mi>λ</mi><mi>t</mi><mo>⇒</mo><mi>t</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mn>10</mn></mrow><mrow><mi>λ</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>×</mo><mn>2.3</mn></mrow><mrow><mn>5</mn><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>10</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>9.2</mn><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>10</mn></mrow></msup><mi mathvariant="normal"> </mi><mi mathvariant="normal">y</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">s</mi></math>

</details>

---

### Q7. JEE Advanced 2018 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<strong> Paragraph: </strong> If the measurement errors in all the independent quantities are known, then it is possible to determine the error in any dependent quantity. This is done by the use of series expansion and truncating the expansion at the first power of the error. For example, consider the relation <math><mi>z</mi><mi>&#160;</mi><mo>=</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></math>. If the errors in <math><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi><mi>&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi>&#160;</mi><mi>z</mi><mi>&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi>&#160;</mi><mo>&#8710;</mo><mi>x</mi><mo>,</mo><mi>&#160;</mi><mo>&#8710;</mo><mi>y</mi><mi>&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi>&#160;</mi><mo>&#8710;</mo><mi>z</mi></math> , respectively, then

<math><mi>z</mi><mo>&#177;</mo><mo>&#8710;</mo><mi>z</mi><mo>=</mo><mfrac><mrow><mi>x</mi><mo>&#177;</mo><mo>&#8710;</mo><mi>x</mi></mrow><mrow><mi>y</mi><mo>&#177;</mo><mo>&#8710;</mo><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>&#177;</mo><mfrac><mrow><mo>&#8710;</mo><mi>x</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>&#177;</mo><mfrac><mrow><mo>&#8710;</mo><mi>y</mi></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

The series expansion for <math><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>&#177;</mo><mfrac><mrow><mo>&#8710;</mo><mi>y</mi></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, to first power in <math><mrow><mrow><mo>&#8710;</mo><mi>y</mi></mrow><mo>/</mo><mrow><mi>y</mi></mrow></mrow><mo>,</mo><mi>&#160;</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mi>&#160;</mi><mn>1</mn><mo>&#8723;</mo><mfenced separators="|"><mrow><mrow><mrow><mo>&#8710;</mo><mi>y</mi></mrow><mo>/</mo><mrow><mi>y</mi></mrow></mrow></mrow></mfenced></math>. The relative errors in independent variables are always added. So the error in <math> <mi>z</mi> </math> will be

<math> <mrow> <mtext>&#916;</mtext><mi>z</mi><mo>=</mo><mi>z</mi><mrow><mo>(</mo> <mrow> <mfrac> <mrow> <mtext>&#916;</mtext><mi>x</mi></mrow> <mi>x</mi> </mfrac> <mo>+</mo><mfrac> <mrow> <mtext>&#916;</mtext><mi>y</mi></mrow> <mi>y</mi> </mfrac> </mrow> <mo>)</mo></mrow><mo>.</mo></mrow> </math>

 <strong> Question : </strong>The above derivation makes the assumption that <math> <mrow> <mfrac> <mrow> <mtext>&#916;</mtext><mi>r</mi></mrow> <mi>x</mi> </mfrac> <mo>&#8810;</mo><mn>1</mn><mo>,</mo><mfrac> <mrow> <mtext>&#916;</mtext><mi>y</mi></mrow> <mi>y</mi> </mfrac> <mo>&#8810;</mo><mn>1</mn></mrow> </math>. Therefore, the higher powers of these quantities are neglected.

**Options:**

- **(A)** <math> <mrow> <mn>0.04</mn></mrow> </math>
- **(B)** <math><mn>0.03</mn></math>
- **(C)** <math><mn>0.02</mn></math>
- **(D)** <math><mn>0.01</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>0.02</mn></math>**

**Detailed Solution:**

<math><mi>N</mi><mo>=</mo><msub><mrow><mi>N</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>&#955;</mi><mi>t</mi></mrow></msup></math>
<math><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>&#8289;</mo><mrow><mi>N</mi></mrow></mrow><mo>=</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>&#8289;</mo><mrow><msub><mrow><mi>N</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mrow><mo>-</mo><mi>&#955;</mi><mi>t</mi></math>
<math><mfrac><mrow><mn>d</mn><mi>N</mi></mrow><mrow><mi>N</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>d</mn><mi>&#955;</mi><mi>t</mi></math>
Converting to error,
<math><mfrac><mrow><mo>&#8710;</mo><mi>N</mi></mrow><mrow><mi>N</mi></mrow></mfrac><mo>=</mo><mo>&#8710;</mo><mi>&#955;</mi><mi>t</mi></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mo>&#8710;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mrow><mn>40</mn></mrow><mrow><mn>2000</mn><mo>&#215;</mo><mi>L</mi></mrow></mfrac><mo>=</mo><mn>0.02</mn></math> (<math> <mi>N</mi> </math> is number of nuclei left undecayed)

</details>

---

### Q8. JEE Advanced 2017 (Paper 1)

*Type:* `numerical` | *Level:* `1`

<math><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>131</mn></mrow></msup><mi>I</mi><mi>&#160;</mi><mi>i</mi><mi>s</mi></math> an isotope of Iodine that <math><mi>&#946;</mi><mi>&#160;</mi></math> decays to an isotope of Xenon with a half-life of <math><mn>8</mn><mi>&#160;</mi><mi>d</mi><mi>a</mi><mi>y</mi><mi>s</mi></math> . A small amount of a serum labelled with <math><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>131</mn></mrow></msup><mi>I</mi></math> is injected into the blood of a person. The activity of the amount of <math><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>131</mn></mrow></msup><mi>I</mi></math> injected was <math><mn>2.4</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>5</mn></mrow></msup></math> Becquerel (Bq). It is known that the injected serum will get distributed uniformly in the blood stream in less than half an hour. After 11.5 hours, 2.5 ml of blood is drawn from the person&#39;s body, and gives an activity of <math><mn>115</mn><mi>&#160;</mi><mi>B</mi><mi>q</mi></math> . The total volume of blood in the person&#39;s body, in litres is approximately (you may use $\mathrm{e}^{\mathrm{x}} \approx 1+\mathrm{x}$ for $|\mathrm{x}|<<1$ and $\ln 2 \approx 0.7$).

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><math><msub><mrow><mi>t</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msub><mo>=</mo><mn>8</mn><mi> </mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">y</mi><mi mathvariant="normal">s</mi></math></p><p><math><mi>A</mi><mo>=</mo><msub><mrow><mi>A</mi></mrow><mrow><mn>0</mn></mrow></msub><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>&lambda;</mi><mi>t</mi></mrow></msup></math></p><p><math><msup><mrow><mi>e</mi></mrow><mrow><mi>&lambda;</mi><mi>t</mi></mrow></msup><mi> </mi><mfenced separators="|"><mrow><mn>115</mn></mrow></mfenced><mo>=</mo><msub><mrow><mi>A</mi></mrow><mrow><mn>0</mn></mrow></msub></math></p><p><math><msub><mrow><mi>A</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>115</mn><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>&lambda;</mi><mi>t</mi></mrow></mfenced><mo>=</mo><mn>115</mn><mi> </mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi mathvariant="script">l</mi><mi>n</mi><mn>2</mn></mrow><mrow><msub><mrow><mi>t</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msub></mrow></mfrac><mo>&times;</mo><mn>11.5</mn></mrow></mfenced></math></p><p><math><msub><mrow><mi>A</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>115</mn><mo>&times;</mo><mn>1.042</mn><mo>=</mo><mn>119.82</mn></math></p><p><math><msub><mrow><mi>A</mi></mrow><mrow><mn>0</mn></mrow></msub><mi> </mi><mo>&cong;</mo><mn>120</mn><mi> </mi><mi>B</mi><mi>q</mi></math></p><p>120 Bq is the activity of 2.5 ml</p><p><math><mo>&there4;</mo><mi> </mi><mi> </mi><mi> </mi><mn>2.4</mn><mo>&times;</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>5</mn></mrow></msup><mi> </mi><mi>B</mi><mi>q</mi></math>  is the activity of <math><mfrac><mrow><mn>2.5</mn><mo>&times;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow><mrow><mn>120</mn></mrow></mfrac><mo>&times;</mo><mn>2.4</mn><mo>&times;</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>5</mn></mrow></msup></math></p><p><math><mo>&there4;</mo></math>    Total volume of blood = 5 litres</p>

</details>

---

### Q9. JEE Advanced 2016 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

An accident in a nuclear laboratory resulted in deposition of a certain amount of radioactive material of half-life 18 days inside the laboratory. Tests revealed that the radiation was 64 times more than the permissible level required for safe operation of the laboratory. What is the minimum number of days after which the laboratory can be considered safe for use?

**Options:**

- **(A)** 64
- **(B)** 90
- **(C)** 108
- **(D)** 120

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 108**

**Detailed Solution:**

<p>Given half-life of radioactive material <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mfrac bevelled="true"><mn>1</mn><mn>2</mn></mfrac></msub><mo>=</mo><mn>18</mn><mo>&#160;</mo></math>days.</p><p>Let the permissible level have activity of <math><msub><mrow><mi>A</mi></mrow><mrow><mi>P</mi><mi>e</mi><mi>r</mi><mi>m</mi><mi>i</mi><mi>s</mi><mi>s</mi><mi>i</mi><mi>b</mi><mi>l</mi><mi>e</mi></mrow></msub></math>
Thus, initially
<math><msub><mrow><mi>A</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>64</mn><mi>&#160;</mi><msub><mrow><mi>A</mi></mrow><mrow><mi>p</mi><mi>e</mi><mi>r</mi><mi>m</mi><mi>i</mi><mi>s</mi><mi>s</mi><mi>i</mi><mi>b</mi><mi>l</mi><mi>e</mi></mrow></msub></math> [Given]
Let number of days required be t.
<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mfrac><mrow><msub><mrow><mi>A</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mfrac><mrow><mi>t</mi></mrow><mrow><mn>18</mn></mrow></mfrac></mrow></msup></mrow></mfrac><mo>=</mo><msub><mrow><mi>A</mi></mrow><mrow><mi>p</mi><mi>e</mi><mi>r</mi><mi>m</mi><mi>i</mi><mi>s</mi><mi>s</mi><mi>i</mi><mi>b</mi><mi>l</mi><mi>e</mi></mrow></msub></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>t</mi><mo>=</mo><mn>108</mn><mi>&#160;</mi><mi>d</mi><mi>a</mi><mi>y</mi><mi>s</mi></math></p>

</details>

---

### Q10. JEE Advanced 2015 (Paper 2)

*Type:* `numerical` | *Level:* `2`

For a radioactive material, its activity <math><mi mathvariant="normal">A</mi></math> and rate of change of its activity <math><mi mathvariant="normal">R</mi></math> are defined as <math><mi mathvariant="normal">A</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">N</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">t</mi></mrow></mfrac></math> and <math><mi mathvariant="normal">R</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">A</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">t</mi></mrow></mfrac></math> , where <math><mi mathvariant="normal">N</mi><mo>(</mo><mi mathvariant="normal">t</mi><mo>)</mo></math> is the number of nuclei at time <math><mi mathvariant="normal">t</mi></math> . Two radioactive sources <math><mi mathvariant="normal">P</mi></math> (mean life <math><mi mathvariant="normal">&#964;</mi></math> ) and <math><mi mathvariant="normal">Q</mi></math> (mean life <math><mn>2</mn><mi mathvariant="normal">&#964;</mi></math> ) have the same activity at <math><mi mathvariant="normal">t</mi><mo>=</mo><mn>0</mn></math> . Their rates of change of activities at <math><mi mathvariant="normal">t</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#964;</mi></math> are <math><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub></math> , respectively. If <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mi mathvariant="normal">e</mi></mrow></mfrac></math> , then the value of <math><mi mathvariant="normal">n</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<math><mi mathvariant="normal">N</mi><mo>=</mo><msub><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mo>-</mo><mi mathvariant="normal">λ</mi><mi mathvariant="normal">t</mi></mrow></msup></math> 
 <math><mi mathvariant="normal">A</mi><mo>=</mo><mi mathvariant="normal">λ</mi><msub><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mo>-</mo><mi mathvariant="normal">λ</mi><mi mathvariant="normal">t</mi></mrow></msup></math> 
 <math><mi mathvariant="normal">R</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mn>2</mn></mrow></msup><msub><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mo>-</mo><mi mathvariant="normal">λ</mi><mi mathvariant="normal">t</mi></mrow></msup></math> 
 <math><msub><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub><mo>=</mo><msub><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub></math>  at  <math><mi mathvariant="normal">t</mi><mo>=</mo><mn>0</mn></math> 
 <math><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub><msub><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mo>-</mo><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub><mi mathvariant="normal">t</mi></mrow></msup><mo>=</mo><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub><msub><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mo>-</mo><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub><mi mathvariant="normal">t</mi></mrow></msup></math>  at  <math><mi mathvariant="normal">t</mi><mo>=</mo><mn>0</mn></math> 
 <math><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub><msub><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub><mo>=</mo><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub><msub><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub></math>                     ...(i) 
 <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub></mrow></mfrac><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub></mrow></mfrac></mrow></mfenced><mfrac><mrow><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mo>-</mo><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub><mn>2</mn><mi mathvariant="normal">τ</mi></mrow></msup></mrow><mrow><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mo>-</mo><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub><mn>2</mn><mi mathvariant="normal">τ</mi></mrow></msup></mrow></mfrac><mi mathvariant="normal"> </mi></math> 
 <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub></mrow></mfrac><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">N</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub></mrow></mfrac></mrow></mfenced><mfrac><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">e</mi></mrow></mfrac><mi mathvariant="normal"> </mi></math>             ...(ii)
 <math><mfenced close="]" open="[" separators="|"><mrow><msub><mrow><mi mathvariant="normal">λ</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">f</mi><mi mathvariant="normal">e</mi></mrow></mfrac></mrow></mfenced></math>     
From equation (i) and equation (ii)
 <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">P</mi></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">Q</mi></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi mathvariant="normal">e</mi></mrow></mfrac><mi> </mi><mo>⇒</mo><mi>n</mi><mo>=</mo><mn>2</mn></math>

</details>

---

### Q11. JEE Advanced 2015 (Paper 1)

*Type:* `numerical` | *Level:* `1`

A nuclear power plant supplying electrical power to a village uses a radioactive material of half life <math><mi mathvariant="normal">T</mi></math> years as the fuel. The amount of fuel at the beginning is such that the total power requirement of the village is 12.5% of the electrical power available from the plant at that time. If the plant is able to meet the total power needs of the village for a maximum period of <math><mi mathvariant="normal">n</mi><mi mathvariant="normal">T</mi></math> years, then the value of <math><mi mathvariant="normal">n</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<math><mn>12.5</mn><mi mathvariant="normal">%</mi><mo>→</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math>  of initial power
 <math><mo>∵</mo></math>  After each T, P will be half
 <math><mi mathvariant="normal">P</mi><mover accent="false"><mo>→</mo><mrow><mi mathvariant="normal">T</mi></mrow></mover><mfrac><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mi mathvariant="normal"> </mi><mover accent="false"><mo>→</mo><mrow><mi mathvariant="normal">T</mi></mrow></mover><mfrac><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mi mathvariant="normal"> </mi><mover accent="false"><mo>→</mo><mrow><mi mathvariant="normal">T</mi></mrow></mover><mfrac><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>8</mn></mrow></mfrac></math> 
 <math><mo>∴</mo></math>  Total time  <math><mo>=</mo><mn>3</mn><mi mathvariant="normal">T</mi></math> 
 <math><mi mathvariant="normal">n</mi><mo>=</mo><mn>3</mn></math>

</details>

---

### Q12. JEE Advanced 2013 (Paper 1)

*Type:* `numerical` | *Level:* `2`

A freshly prepared sample of a radioisotope of half-life 1386 s has activity ${10}^{3}$ disintegrations per second. Given that In 2 = 0.693, the fraction of the initial number of nuclei (expressed in nearest integer percentage) that will decay in the first 80 s after preparation of the sample is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<math><mrow>  <mtext>f</mtext>  <mo>=</mo>  <mfenced open="(" close=")" separators=",">    <mrow>      <mn>1</mn>      <mo>-</mo>      <msup>              <mtext>e</mtext>          <mrow>            <mo>-</mo>            <mi>&lambda;</mi>            <mtext>t</mtext>          </mrow>      </msup>    </mrow>  </mfenced>  <mo>=</mo>  <mn>1</mn>  <mo>-</mo>  <msup>          <mtext>e</mtext>      <mrow>        <mo>-</mo>        <mi>&lambda;</mi>        <mtext>t</mtext>      </mrow>  </msup>  <mo>&asymp;</mo>  <mn>1</mn>  <mo>-</mo>  <mfenced open="(" close=")" separators=",">    <mrow>      <mn>1</mn>      <mo>-</mo>      <mi>&lambda;</mi>      <mtext>t</mtext>    </mrow>  </mfenced>  <mo>=</mo>  <mi>&lambda;</mi>  <mtext>t</mtext></mrow></math>
f = 0.04
Hence <math><mrow>  <mtext>%</mtext>  <mo>decay </mo>  <mo>&asymp; </mo>  <mn>4</mn>  <mo>%</mo></mrow></math>

</details>

---

### Q13. JEE Advanced 2011 (Paper 1)

*Type:* `numerical` | *Level:* `2`

The activity of a freshly prepared radioactive sample is $10^{10}$ disintegrations per second, whose mean life is $10^{-9} \mathrm{~s}$. The mass of an atom of this radioisotope is $10^{-25} \mathrm{~kg}$. The mass (in $\mathrm{mg}$ ) of the radioactive sample is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

Activity $\left(-\frac{d N}{d t}\right)=\lambda N=\left(\frac{1}{t_{\text {mean }}}\right) \times N$
$$
\begin{aligned}
& \therefore \quad N=\left(-\frac{d N}{d t}\right) \times t_{\text {mean }} \\
& \quad=\text { Total number of atoms } \\
& \text { Mass of one atom is } 10^{-25} \mathrm{~kg}=m \text { (say) } \\
& \therefore \quad \text { Total mass of radioactive substance } \\
& =(\text { number of atoms) } \\
& \quad \times(\text { mass of one atom) } \\
& =\left(-\frac{d N}{d t}\right)\left(t_{\text {mean }}\right)(m)
\end{aligned}
$$
Substituting the values, we get
Total mass of radioactive substance
$$
=1 \mathrm{mg}
$$
$\therefore$ Answer is 1 .
Analysis of Question
Question is very simple. Again in my opinion one can solve it.

</details>

---

### Q14. JEE Advanced 2010 (Paper 2)

*Type:* `numerical` | *Level:* `3`

To determine the half-life of a radioactive element, a student plots a graph of $\ln \left|\frac{d N(t)}{d t}\right|$ versust. Here $\frac{d N(t)}{d t}$ is the rate of radioactive decay at time $t$. If the number of radioactive nuclei of this element decreases by a factor of $p$ after $4.16 \mathrm{yr}$, the value of $p$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/cVWnejtFcY6cljXBHxMmON746JdsX22aYXuq-g9-vyg.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

$\left|\frac{d N}{d t}\right|=\mid$ Activity of radioactive substance|
$$
=\lambda N=\lambda N_0 e^{-\lambda t}
$$
Taking log both sides
$$
\ln \left|\frac{d N}{d t}\right|=\ln \left(\lambda N_0\right)-\lambda t
$$
Hence, $\ln \left|\frac{d N}{d t}\right|$ versus $t$ graph is a straight line with slope $-\lambda$
From the graph we can see that,
$$
\lambda=\frac{1}{2}=0.5 \mathrm{yr}^{-1}
$$
Now applying the equation,
$$
\begin{aligned}
N & =N_0 e^{-\lambda t} \\
& =N_0 e^{-0.5 \times 4.16} \\
& =N_0 e^{-2.08}=0.125 N_0 \\
& =\frac{N_0}{8}
\end{aligned}
$$
ie, nuclei decreases by a factor of 8 . Hence the answer is 8 .

</details>

---

### Q15. JEE Advanced 2008 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

A radioactive sample $S_1$ having an activity of $5 \mu \mathrm{Ci}$ has twice the number of nuclei as another sample $S_2$ which has an activity of $10 \mu \mathrm{Ci}$. The half lives of $S_1$ and $S_2$ can be

**Options:**

- **(A)** 20 yr and 5 yr, respectively
- **(B)** 20 yr and 10 yr, respectively
- **(C)** 10 yr each
- **(D)** 5 yr each

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 20 yr and 5 yr, respectively**

**Detailed Solution:**

Activity of $S_1=\frac{1}{2}$ (activity of $S_2$ )
or
$$
\lambda_2 N_1=\frac{1}{2}\left(\lambda_2 N_2\right) \text { or } \frac{\lambda_1}{\lambda_2}=\frac{N_2}{2 N_1}
$$
or
$$
\begin{aligned}
& \frac{T_1}{T_2}=\frac{2 N_1}{N_2}\left(T=\text { half-life }=\frac{\ln 2}{\lambda}\right) \\
& N_1=2 N_2 \\
& \frac{T_1}{T_2}=4
\end{aligned}
$$
Given
$\therefore$ correct option is (a).

</details>

---

### Q16. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `2`

Match the following columns
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/UWvjzowOsy9s6gkOqAlYesntU2oLVtSYhsrLUqDtv3A.original.fullsize.png">

**Options:**

- **(A)** (a) p,q, (b) p, (c) p, (d) p,q
- **(B)** (a) p,q,r, (b) p, s, (c) p,r, (d) p,q,r
- **(C)** (a) p,q, (b) p, r, (c) p,s, (d) p,q,r
- **(D)** (a) p,s, (b) p, s, (c) p, (d) p,q

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) (a) p,q, (b) p, r, (c) p,s, (d) p,q,r**

**Detailed Solution:**

(a) $\rightarrow$ p, q
(b) $\rightarrow \mathrm{p}, \mathrm{r}$
(c) $\rightarrow$ p, $s$
(d) $\rightarrow$ p, q, r

</details>

---

### Q17. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `1`

Half-life of a radio active substance ' $A$ ' is 4 days. The probability that a nucleus will decay in two half-lives is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{3}{4}$
- **(C)** $\frac{1}{2}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{4}$**

**Detailed Solution:**

After two half lives $\frac{1}{4}$ th fraction of nuclei will remain undecayed. Or, $\frac{3}{4}$ th fraction will decay. Hence, the probability that a nucleus decays in two half lives is $\frac{3}{4}$.

</details>

---

