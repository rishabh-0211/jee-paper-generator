# JEE Advanced Chemistry - Electrochemistry

## Topic 2: Conductance and Conductivity

**Total Questions:** 11

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

At $300$ K, the molar conductivities of the aqueous solutions of three salts at two different concentrations are given below:
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><th style="border: 1px solid black; padding: 10px;">Salt</th><th style="border: 1px solid black; padding: 10px;">Concentration (M)</th><th style="border: 1px solid black; padding: 10px;">Molar conductivity (S cm$^2$ mol$^{-1}$)</th></tr><tr><td style="border: 1px solid black; padding: 10px;" rowspan="2">$\text{NaNO}_3$</td><td style="border: 1px solid black; padding: 10px;">$0.01$</td><td style="border: 1px solid black; padding: 10px;">$111$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$0.04$</td><td style="border: 1px solid black; padding: 10px;">$101$</td></tr><tr><td style="border: 1px solid black; padding: 10px;" rowspan="2">$\text{NaCl}$</td><td style="border: 1px solid black; padding: 10px;">$0.01$</td><td style="border: 1px solid black; padding: 10px;">$117$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$0.04$</td><td style="border: 1px solid black; padding: 10px;">$107$</td></tr><tr><td style="border: 1px solid black; padding: 10px;" rowspan="2">$\text{AgNO}_3$</td><td style="border: 1px solid black; padding: 10px;">$0.01$</td><td style="border: 1px solid black; padding: 10px;">$125$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$0.04$</td><td style="border: 1px solid black; padding: 10px;">$116$</td></tr></table>
The conductivity of a saturated aqueous solution of AgCl is $1.40 \times 10^{-6}$ S cm$^{-1}$ at $300$ K. If the solubility of AgCl in water at $300$ K is $X$ mol L$^{-1}$, then $\log_{10}(X^{-1})$ is
(Assume that AgCl dissolved in water ionizes completely and that the molar conductivity of saturated AgCl solution is equal to its limiting molar conductivity.)

**Options:**

- **(A)** $3$
- **(B)** $4$
- **(C)** $5$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5$**

**Detailed Solution:**

Using the Debye-Hückel-Onsager equation, $\Lambda_m = \Lambda^\circ_m - b\sqrt{C}$, we can find the limiting molar conductivity ($\Lambda^\circ_m$) for each salt.

For $\text{NaNO}_3$:
$\Lambda^\circ_m - b\sqrt{0.01} = 111 \Rightarrow \Lambda^\circ_m - 0.1b = 111$
$\Lambda^\circ_m - b\sqrt{0.04} = 101 \Rightarrow \Lambda^\circ_m - 0.2b = 101$
Subtracting the two equations gives $0.1b = 10 \Rightarrow b = 100$.
$\Lambda^\circ_m(\text{NaNO}_3) = 111 + 100(0.1) = 121 \text{ S cm}^2\text{ mol}^{-1}$.

For $\text{NaCl}$:
$\Lambda^\circ_m - 0.1b = 117$
$\Lambda^\circ_m - 0.2b = 107$
Subtracting gives $0.1b = 10 \Rightarrow b = 100$.
$\Lambda^\circ_m(\text{NaCl}) = 117 + 100(0.1) = 127 \text{ S cm}^2\text{ mol}^{-1}$.

For $\text{AgNO}_3$:
$\Lambda^\circ_m - 0.1b = 125$
$\Lambda^\circ_m - 0.2b = 116$
Subtracting gives $0.1b = 9 \Rightarrow b = 90$.
$\Lambda^\circ_m(\text{AgNO}_3) = 125 + 90(0.1) = 134 \text{ S cm}^2\text{ mol}^{-1}$.

According to Kohlrausch's law of independent migration of ions:
$\Lambda^\circ_m(\text{AgCl}) = \Lambda^\circ_m(\text{AgNO}_3) + \Lambda^\circ_m(\text{NaCl}) - \Lambda^\circ_m(\text{NaNO}_3)$
$\Lambda^\circ_m(\text{AgCl}) = 134 + 127 - 121 = 140 \text{ S cm}^2\text{ mol}^{-1}$.

The molar conductivity of the saturated $\text{AgCl}$ solution is equal to its limiting molar conductivity, so $\Lambda_m(\text{AgCl}) = 140 \text{ S cm}^2\text{ mol}^{-1}$.

The relationship between molar conductivity, conductivity ($\kappa$), and solubility ($X$ in $\text{mol L}^{-1}$) is:
$\Lambda_m = \dfrac{\kappa \times 1000}{X}$

Substituting the given values:
$140 = \dfrac{1.40 \times 10^{-6} \times 1000}{X}$
$140 = \dfrac{1.40 \times 10^{-3}}{X}$
$X = \dfrac{1.40 \times 10^{-3}}{140} = 10^{-5} \text{ mol L}^{-1}$.

We need to find $\log_{10}(X^{-1})$:
$X^{-1} = \dfrac{1}{10^{-5}} = 10^5$
$\log_{10}(X^{-1}) = \log_{10}(10^5) = 5$.

Answer: $5$

</details>

---

### Q2. JEE Advanced 2024 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

In a conductometric titration, small volume of titrant of higher concentration is added stepwise to a larger volume of titrate of much lower concentration, and the conductance is measured after each addition.
The limiting ionic conductivity $\left(\Lambda_0\right)$ values (in $\mathrm{mS} \mathrm{m}^2 \mathrm{~mol}^{-1}$) for different ions in aqueous solutions are given below:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/n4XfWZ_FiAyS_V2QzdumgTB-Y43XRVhjbCdgNqWarsU.original.fullsize.png">
For different combinations of titrates and titrants given in List-I, the graphs of 'conductance' versus 'volume of titrant' are given in List-II.
Match each entry in List-I with the appropriate entry in List-II and choose the correct option.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/jClIogwmkY-EJ5eYUVU-mkR3ErR6ZlJ452YCnlRrvfc.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{P}-4, \mathrm{Q}-3, \mathrm{R}-2, \mathrm{~S}-5$
- **(B)** $\mathrm{P}-2, \mathrm{Q}-4, \mathrm{R}-3, \mathrm{~S}-1$
- **(C)** $\mathrm{P}-3, \mathrm{Q}-4, \mathrm{R}-2, \mathrm{~S}-5$
- **(D)** $\mathrm{P}-4, \mathrm{Q}-3, \mathrm{R}-2, \mathrm{~S}-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{P}-3, \mathrm{Q}-4, \mathrm{R}-2, \mathrm{~S}-5$**

**Detailed Solution:**

Option (P) :
On adding $\mathrm{AgNO}_3$ solution to $\mathrm{KCl}$ solution precipitation of $\mathrm{AgCl}$ will occur due to which $\mathrm{Cl}^{-}$already present will be replaced by $\mathrm{NO}_3^{-}$ions. So conductance of solution will decrease till equivalence point. After complete precipitation of $\mathrm{AgCl}$, further added $\mathrm{AgNO}_3$ will increase the number of ions in resulting solution so conductance will increase.
Option $(\mathbf{Q})$ :
On adding $\mathrm{KCl}$ solution to $\mathrm{AgNO}_3$ solution precipitation of $\mathrm{AgCl}$ will occur due to which already present $\mathrm{Ag}^{+}$ions will be replaced by $\mathrm{K}^{+}$ions in solution. So conductance of solution will increase. After complete precipitation of $\mathrm{AgCl}$ further added $\mathrm{KCl}$ will increase the number of ions in resulting solution so conductance will increase further.
Option (R) :
On adding $\mathrm{HCl}$ solution to $\mathrm{NaOH}$ solution, $\mathrm{OH}^{-}$will be replaced by $\mathrm{Cl}^{-}$ions so conductance of solution decreases. After complete neutralisation further added $\mathrm{HCl}$ will increase number of ions in the solution. So conductance will increase further.
Option (S) :
On adding $\mathrm{CH}_3 \mathrm{COOH}$ solution to $\mathrm{NaOH}$ solution $\mathrm{OH}^{-}$will be replaced by $\mathrm{CH}_3 \mathrm{COO}^{-}$ions, so conductance of solution decreases. After complete neutralisation further added $\mathrm{CH}_3 \mathrm{COOH}$ will remain undissociated because it is a weak acid and there is also common ion effect on acetate ions. So number of ions in solution will remain almost constant therefore conductance of solution will remain constant.

</details>

---

### Q3. JEE Advanced 2023 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Plotting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>/</mo><msub><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi></msub></math> against <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>c&#923;</mi><mi mathvariant="normal">m</mi></msub></math> for aqueous solutions of a monobasic weak acid <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>HX</mi><mo>)</mo></math> resulted in a straight line with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>-</mo></math>axis intercept of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi></math> and slope of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi></math>. The ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>/</mo><mi mathvariant="normal">S</mi></math> is
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="" open="[" separators="|"><mrow><msub><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi></msub><mo>=</mo></mrow></mfenced><mtext>&#160;molar conductivity&#160;</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup><mo>=</mo><mo>&#160;</mo><mi>limiting</mi><mo>&#160;</mo><mi>molar</mi><mo>conductivity</mo><mspace linebreak="newline"/><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi mathvariant="normal">c</mi><mo>=</mo><mo>&#160;</mo><mi>molar</mi><mo>concentration</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="" separators="|"><mrow><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><mo>=</mo><mtext>&#160;dissociation constant of&#160;</mtext><mi>HX</mi></mrow></mfenced></math></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup><mo>/</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>/</mo><mfenced><mrow><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup></math>**

**Detailed Solution:**

<blockquote><p>The degree of dissociation is the ratio of molar conductivity to the limiting molar conductivity.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#945;</mi><mo>=</mo><mfrac><msub><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi></msub><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup></mfrac></math></p><p>The equilibrium reaction is given below,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>HX</mi><mover><mo>&#8652;</mo><mrow></mrow></mover><msup><mi mathvariant="normal">H</mi><mo>+</mo></msup><mo>+</mo><msup><mi mathvariant="normal">X</mi><mo>-</mo></msup><mspace linebreak="newline"></mspace><mi>initial</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi mathvariant="normal">c</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mspace linebreak="newline"></mspace><mi>At</mi><mo>&#160;</mo><mi>equilibrium</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi mathvariant="normal">c</mi><mo>-</mo><mi>c&#945;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>c&#945;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>c&#945;</mi></math></p><p>The acid dissociation constant, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><mo>=</mo><mfrac><msup><mi>c&#945;</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>&#8722;</mo><mi mathvariant="normal">&#945;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">c</mi><msup><mfenced separators="|"><mrow><msub><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi></msub><mo>/</mo><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>&#8722;</mo><mfenced separators="|"><mrow><msub><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi></msub><mo>/</mo><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><mo>=</mo><mfrac><msubsup><mi>c&#923;</mi><mi mathvariant="normal">m</mi><mn>2</mn></msubsup><mrow><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup><mfenced separators="|"><mrow><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup><mo>&#8722;</mo><msub><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi></msub></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msup><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup><mn>2</mn></msup><mo>&#8722;</mo><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup><msub><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi></msub><mo>=</mo><msubsup><mi>c&#923;</mi><mi mathvariant="normal">m</mi><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msup><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup><mn>2</mn></msup></mrow><msub><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi></msub></mfrac><mo>&#8722;</mo><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup><mo>=</mo><msub><mi>C&#923;</mi><mi mathvariant="normal">m</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msup><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup><mn>2</mn></msup></mrow><msub><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi></msub></mfrac><mo>=</mo><msub><mi>c&#923;</mi><mi mathvariant="normal">m</mi></msub><mo>+</mo><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msub><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi></msub></mfrac><mo>=</mo><mfenced separators="|"><mfrac><msub><mi>c&#923;</mi><mi mathvariant="normal">m</mi></msub><mrow><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msup><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup><mn>2</mn></msup></mrow></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup></mfrac></math></p><p>From the above line equation, slope and y-intercept can be written as follows,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>=</mo><mfrac><mn>1</mn><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>=</mo><mfrac><mn>1</mn><mrow><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msup><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">P</mi><mi mathvariant="normal">S</mi></mfrac><mo>=</mo><mfenced separators="|"><mfrac><mfrac><mn>1</mn><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup></mfrac><mfrac><mn>1</mn><mrow><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msup><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup><mn>2</mn></msup></mrow></mfrac></mfrac></mfenced><mo>=</mo><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><msubsup><mi mathvariant="normal">&#923;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">o</mi></msubsup></math></p></blockquote>

</details>

---

### Q4. JEE Advanced 2022 (Paper 2)

*Type:* `numerical` | *Level:* `2`

<p>Consider the strong electrolytes <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Z</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">X</mi><mi mathvariant="normal">n</mi></msub><mo>,</mo><mo>&#160;</mo><msub><mi mathvariant="normal">U</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">Y</mi><mi mathvariant="normal">p</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">X</mi><mi mathvariant="normal">n</mi></msub></math>. Limiting molar conductivity of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">U</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">Y</mi><mi mathvariant="normal">p</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">X</mi><mi mathvariant="normal">n</mi></msub></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>250</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>440</mn><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#160;</mo><msup><mi>cm</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi>mol</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, respectively. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">m</mi><mo>+</mo><mi mathvariant="normal">n</mi><mo>+</mo><mi mathvariant="normal">p</mi></mrow></mfenced></math> is</p><p>Given:</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td>Ion</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">Z</mi><mrow><mi mathvariant="normal">n</mi><mo>+</mo></mrow></msup></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">U</mi><mrow><mi mathvariant="normal">p</mi><mo>+</mo></mrow></msup></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">V</mi><mrow><mi mathvariant="normal">n</mi><mo>+</mo></mrow></msup></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">X</mi><mrow><mi mathvariant="normal">m</mi><mo>-</mo></mrow></msup></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">Y</mi><mrow><mi mathvariant="normal">m</mi><mo>-</mo></mrow></msup></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mn>0</mn></msup><mfenced><mrow><mi mathvariant="normal">S</mi><mo>&#160;</mo><mi>cm</mi><mmultiscripts><mo>&#160;</mo><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><msup><mi>mol</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>.</mo><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mo>.</mo><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>.</mo><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn><mo>.</mo><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>.</mo><mn>0</mn></math></td>		</tr>	</tbody></table><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mn>0</mn></msup></math> is the limiting molar conductivity of ions</p><p>The plot of molar conductivity <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>&#923;</mi></mfenced></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Z</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">X</mi><mi mathvariant="normal">n</mi></msub></math> vs <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">c</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math> is given below.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/8f22ac03-49c6-47b4-86b9-9e69736b0508-image.png" style="width: 303px; height: 270px;" /></p><p>If the numerical value has more than two decimal places, truncate/round-off the value to TWO decimal places.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#955;</mi><mi mathvariant="normal">m</mi></msub><mo>=</mo><msubsup><mi mathvariant="normal">&#955;</mi><mi mathvariant="normal">m</mi><mo>&#176;</mo></msubsup><mo>-</mo><mi mathvariant="normal">A</mi><msqrt><mi mathvariant="normal">C</mi></msqrt></math></p><p>For electrolyte <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Z</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">X</mi><mi mathvariant="normal">n</mi></msub></math> and from given curve</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#955;</mi><mi mathvariant="normal">m</mi></msub><mfenced><mrow><msub><mi mathvariant="normal">Z</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">X</mi><mi mathvariant="normal">n</mi></msub></mrow></mfenced><mo>=</mo><msubsup><mi mathvariant="normal">&#955;</mi><mi mathvariant="normal">m</mi><mn>0</mn></msubsup><mfenced><mrow><msub><mi mathvariant="normal">Z</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">X</mi><mi mathvariant="normal">n</mi></msub></mrow></mfenced><mo>-</mo><mi mathvariant="normal">A</mi><msqrt><mi mathvariant="normal">C</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi mathvariant="normal">A</mi><mo>=</mo><mfrac><mrow><mn>336</mn><mo>-</mo><mn>339</mn></mrow><mrow><mn>0</mn><mo>.</mo><mn>04</mn><mo>-</mo><mn>0</mn><mo>.</mo><mn>01</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mrow><mn>0</mn><mo>.</mo><mn>03</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">A</mi><mo>=</mo><mn>100</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mi mathvariant="normal">m</mi></msub><mo>=</mo><mn>336</mn><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#160;</mo><msup><mi>cm</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi>mol</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>336</mn><mo>=</mo><msubsup><mi mathvariant="normal">&#955;</mi><mi mathvariant="normal">m</mi><mn>0</mn></msubsup><mfenced><mrow><msub><mi mathvariant="normal">Z</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">X</mi><mi mathvariant="normal">n</mi></msub></mrow></mfenced><mo>-</mo><mn>100</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>04</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>&#955;</mi><mi mathvariant="normal">m</mi><mn>0</mn></msubsup><mo>=</mo><mn>336</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>340</mn><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#160;</mo><msup><mi>cm</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi>mol</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">Z</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">X</mi><mi mathvariant="normal">n</mi></msub><mo>&#10230;</mo><msup><mi>mZ</mi><mrow><mi mathvariant="normal">n</mi><mo>+</mo></mrow></msup><mo>+</mo><msup><mi>nX</mi><mrow><mi mathvariant="normal">m</mi><mo>-</mo></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mn>50</mn><mi mathvariant="normal">m</mi><mo>+</mo><mn>80</mn><mi mathvariant="normal">n</mi><mo>=</mo><mn>340</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi mathvariant="normal">m</mi><mo>+</mo><mn>8</mn><mi mathvariant="normal">n</mi><mo>=</mo><mn>34</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">U</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">Y</mi><mi mathvariant="normal">p</mi></msub><mo>&#10230;</mo><msup><mi>mU</mi><mrow><mi mathvariant="normal">p</mi><mo>+</mo></mrow></msup><mo>+</mo><msup><mi>pY</mi><mrow><mi mathvariant="normal">m</mi><mo>-</mo></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>25</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>+</mo><mn>100</mn><mi mathvariant="normal">p</mi><mo>=</mo><msubsup><mi>&#955;</mi><mi mathvariant="normal">m</mi><mn>0</mn></msubsup><mfenced><mrow><msub><mi mathvariant="normal">U</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">Y</mi><mi mathvariant="normal">p</mi></msub></mrow></mfenced><mo>=</mo><mn>250</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">m</mi><mo>+</mo><mn>4</mn><mi mathvariant="normal">p</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">m</mi></msub><msub><mi mathvariant="normal">X</mi><mi mathvariant="normal">n</mi></msub><mo>&#10230;</mo><msup><mi>mV</mi><mrow><mi mathvariant="normal">n</mi><mo>+</mo></mrow></msup><mo>+</mo><msup><mi>nX</mi><mrow><mi mathvariant="normal">m</mi><mo>-</mo></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>100</mn><mi mathvariant="normal">m</mi><mo>+</mo><mn>80</mn><mi mathvariant="normal">n</mi><mo>=</mo><mn>440</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi mathvariant="normal">m</mi><mo>+</mo><mn>4</mn><mi mathvariant="normal">n</mi><mo>=</mo><mn>22</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>iii</mi></mfenced></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>iii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo>=</mo><mn>2</mn></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">p</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mi mathvariant="normal">m</mi><mo>+</mo><mi mathvariant="normal">n</mi><mo>+</mo><mi mathvariant="normal">p</mi><mo>=</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>7</mn></math></p></blockquote>

</details>

---

### Q5. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `3`

At $298 \mathrm{~K}$, the limiting molar conductivity of a weak monobasic acid is $4 \times 10^{2} \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$. At $298 \mathrm{~K}$, for an aqueous solution of the acid the degree of dissociation is $\boldsymbol{\alpha}$ and the molar conductivity is $\mathbf{y} \times 10^{2} \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$. At $298 \mathrm{~K}$, upon 20 times dilution with water, the molar conductivity of the solution becomes $3 \mathbf{y} \times 10^{2} \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$
The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi></math> is _________ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.86**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#945;</mi><mo>=</mo><mfrac><msub><mi mathvariant="normal">&#955;</mi><mi mathvariant="normal">m</mi></msub><msubsup><mi mathvariant="normal">&#955;</mi><mi mathvariant="normal">m</mi><mo>&#8728;</mo></msubsup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>+</mo><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mi mathvariant="normal">y</mi><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">k</mi><mi mathvariant="normal">a</mi></msub><mo>=</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#945;</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>After dilution</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">y</mi><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></mrow><mrow><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">y</mi></mrow><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">k</mi><mi mathvariant="normal">a</mi></msub><mo>=</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><msubsup><mi mathvariant="normal">&#945;</mi><mn>2</mn><mn>2</mn></msubsup></mrow><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>eq. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>/</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>eq <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>/</mo><mfenced><mn>4</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>1</mn><mo>=</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#945;</mi><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfenced><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><msubsup><mi mathvariant="normal">&#945;</mi><mn>2</mn><mn>2</mn></msubsup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msubsup><mi mathvariant="normal">&#945;</mi><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><msubsup><mi mathvariant="normal">&#945;</mi><mn>2</mn><mn>2</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>=</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mo>&#160;</mo><mn>20</mn><mi mathvariant="normal">y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msubsup><mi mathvariant="normal">&#945;</mi><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><msubsup><mi mathvariant="normal">&#945;</mi><mn>2</mn><mn>2</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>20</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>20</mn><msubsup><mi mathvariant="normal">&#945;</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfenced></mfrac><mo>=</mo><mfrac><msubsup><mi mathvariant="normal">&#945;</mi><mn>2</mn><mn>2</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>20</mn><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfenced></mfrac><mo>=</mo><mfrac><mn>9</mn><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mn>3</mn><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#8722;</mo><mn>60</mn><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub><mo>=</mo><mn>9</mn><mo>&#8722;</mo><mn>9</mn><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>=</mo><mn>51</mn><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>11</mn><mn>51</mn></mfrac><mo>=</mo><mn>0.22</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mn>4</mn><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn><mo>&#215;</mo><mfrac><mn>11</mn><mn>51</mn></mfrac><mo>=</mo><mn>0</mn><mo>.86</mo></math></p>

</details>

---

### Q6. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `3`

At $298 \mathrm{~K}$, the limiting molar conductivity of a weak monobasic acid is $4 \times 10^{2} \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$. At $298 \mathrm{~K}$, for an aqueous solution of the acid the degree of dissociation is $\boldsymbol{\alpha}$ and the molar conductivity is $\mathbf{y} \times 10^{2} \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$. At $298 \mathrm{~K}$, upon 20 times dilution with water, the molar conductivity of the solution becomes $3 \mathbf{y} \times 10^{2} \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$
The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#945;</mi></math> is _______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.22**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#945;</mi><mo>=</mo><mfrac><msub><mi mathvariant="normal">&#955;</mi><mi mathvariant="normal">m</mi></msub><msubsup><mi mathvariant="normal">&#955;</mi><mi mathvariant="normal">m</mi><mo>&#8728;</mo></msubsup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>+</mo><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mi mathvariant="normal">y</mi><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">k</mi><mi mathvariant="normal">a</mi></msub><mo>=</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#945;</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>After dilution</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">y</mi><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></mrow><mrow><mn>4</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">y</mi></mrow><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">k</mi><mi mathvariant="normal">a</mi></msub><mo>=</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><msubsup><mi mathvariant="normal">&#945;</mi><mn>2</mn><mn>2</mn></msubsup></mrow><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>eq. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>/</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>eq <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>/</mo><mfenced><mn>4</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>1</mn><mo>=</mo><mfrac><mrow><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><msubsup><mi mathvariant="normal">&#945;</mi><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfenced><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><msubsup><mi mathvariant="normal">&#945;</mi><mn>2</mn><mn>2</mn></msubsup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msubsup><mi mathvariant="normal">&#945;</mi><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><msubsup><mi mathvariant="normal">&#945;</mi><mn>2</mn><mn>2</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>=</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mo>&#160;</mo><mn>20</mn><mi mathvariant="normal">y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msubsup><mi mathvariant="normal">&#945;</mi><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><msubsup><mi mathvariant="normal">&#945;</mi><mn>2</mn><mn>2</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>20</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>20</mn><msubsup><mi mathvariant="normal">&#945;</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfenced></mfrac><mo>=</mo><mfrac><msubsup><mi mathvariant="normal">&#945;</mi><mn>2</mn><mn>2</mn></msubsup><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>20</mn><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></mrow></mfenced></mfrac><mo>=</mo><mfrac><mn>9</mn><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><msub><mi mathvariant="normal">&#945;</mi><mn>2</mn></msub></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#8722;</mo><mn>60</mn><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub><mo>=</mo><mn>9</mn><mo>&#8722;</mo><mn>9</mn><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>=</mo><mn>51</mn><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#945;</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>11</mn><mn>51</mn></mfrac><mo>=</mo><mn>0</mn><mo>.22</mo></math></p><p> </p>

</details>

---

### Q7. JEE Advanced 2017 (Paper 1)

*Type:* `numerical` | *Level:* `3`

The conductance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.0015</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">M</mi></math> aqueous solution of a weak monobasic acid was determined by using a conductivity cell consisting of platinized <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Pt</mi><mo>&#160;</mo></math>electrodes. The distance between the electrodes is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn><mi mathvariant="normal">&#160;</mi><mi>cm</mi></math> with an area of cross-section of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><msup><mi>cm</mi><mn>2</mn></msup></math>. The conductance of this solution was found to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mi mathvariant="normal">S</mi></math> . The <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>pH</mi><mo>&#160;</mo></math>of the solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>. The value of limiting molar conductivity of this weak monobasic acid in aqueous solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">Z</mi><mi mathvariant="normal">&#160;</mi><mo>&#215;</mo><mi mathvariant="normal">&#160;</mi><msup><mn>10</mn><mn>2</mn></msup><mi mathvariant="normal">S</mi><mi mathvariant="normal">&#160;</mi><msup><mi>cm</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>mol</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>.</mo></math> The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Z</mi><mo>&#160;</mo></math>is.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p>For weak acid, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="[" separators="|"><msup><mi mathvariant="normal">H</mi><mo>+</mo></msup></mfenced><mo>=</mo><mi>c&#945;</mi><mo>=</mo><mi mathvariant="normal">c</mi><mo>&#215;</mo><mfrac><msubsup><mo>&#8743;</mo><mi mathvariant="normal">m</mi><mi mathvariant="normal">c</mi></msubsup><msubsup><mo>&#8743;</mo><mi mathvariant="normal">m</mi><mi mathvariant="normal">&#8734;</mi></msubsup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">c</mi><mo>&#215;</mo><mfrac><mrow><mi mathvariant="normal">k</mi><mo>&#215;</mo><mfrac><mn>1000</mn><mi mathvariant="normal">c</mi></mfrac></mrow><msubsup><mo>&#8743;</mo><mi mathvariant="normal">m</mi><mi mathvariant="normal">&#8734;</mi></msubsup></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">k</mi><mo>&#215;</mo><mn>1000</mn></mrow><msubsup><mo>&#8743;</mo><mi mathvariant="normal">m</mi><mi mathvariant="normal">&#8734;</mi></msubsup></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">G</mi><mo>&#215;</mo><mfenced separators="|"><mfrac><mi mathvariant="normal">l</mi><mi mathvariant="normal">a</mi></mfrac></mfenced><mo>&#215;</mo><mn>1000</mn></mrow><msubsup><mo>&#8743;</mo><mi mathvariant="normal">m</mi><mi mathvariant="normal">&#8734;</mi></msubsup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mfenced separators="|"><mfrac><mn>120</mn><mn>1</mn></mfrac></mfenced><mo>&#215;</mo><mn>1000</mn></mrow><mrow><mi mathvariant="normal">Z</mi><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup></mrow></mfrac><mi mathvariant="normal">&#160;</mi><mo>&#8658;</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">Z</mi><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q8. JEE Advanced 2015 (Paper 2)

*Type:* `numerical` | *Level:* `3`

The molar conductivity of a solution of a weak acid HX (0.01 M) is 10 times smaller than the molar conductivity of a solution of a weak acid HY (0.10 M). If <math><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mo>-</mo></mrow></msup></mrow><mrow><mn>0</mn></mrow></msubsup><mo>&#8776;</mo><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mo>-</mo></mrow></msup></mrow><mrow><mn>0</mn></mrow></msubsup></math> , the difference in their <math><mi mathvariant="normal">p</mi><msub><mrow><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">a</mi></mrow></msub></math> values, <math><mi mathvariant="normal">p</mi><msub><mrow><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">a</mi></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">X</mi></mrow></mfenced><mo>-</mo><mi mathvariant="normal">p</mi><msub><mrow><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">a</mi></mrow></msub><mo>(</mo><mi mathvariant="normal">H</mi><mi mathvariant="normal">Y</mi><mo>)</mo></math> , is (Consider degree of ionization of both acids to &lt;&lt; 1)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<math><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mo>-</mo></mrow></msup></mrow><mrow><mn>0</mn></mrow></msubsup><mo>&#8776;</mo><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mo>-</mo></mrow></msup></mrow><mrow><mn>0</mn></mrow></msubsup></math>
<math><mo>&#8658;</mo><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">H</mi></mrow><mrow><mo>+</mo></mrow></msup></mrow><mrow><mn>0</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mo>-</mo></mrow></msup></mrow><mrow><mn>0</mn></mrow></msubsup><mi mathvariant="normal">&#160;</mi><mo>&#8776;</mo><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">H</mi></mrow><mrow><mo>+</mo></mrow></msup></mrow><mrow><mn>0</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mo>-</mo></mrow></msup></mrow><mrow><mn>0</mn></mrow></msubsup></math>
<math><mo>&#8658;</mo><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">X</mi></mrow><mrow><mn>0</mn></mrow></msubsup><mo>&#8776;</mo><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">Y</mi></mrow><mrow><mn>0</mn></mrow></msubsup></math> ...... (i)
Also, <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow></msub></mrow><mrow><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mn>0</mn></mrow></msubsup></mrow></mfrac><mo>=</mo><mi mathvariant="normal">&#945;</mi></math> ,
So <math><msub><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">X</mi></mrow></mfenced><mo>=</mo><mi mathvariant="normal">&#160;</mi><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mn>0</mn></mrow></msubsup><msub><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">Y</mi></mrow></mfenced><mo>=</mo><mi mathvariant="normal">&#160;</mi><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mn>0</mn></mrow></msubsup><msub><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mn>2</mn></mrow></msub></math>
(Where <math><msub><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mn>2</mn></mrow></msub></math> are degree of dissociation of HX and HY respectively)
Now, given that
<math><msub><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">Y</mi></mrow></mfenced><mo>=</mo><mn>10</mn><msub><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">X</mi></mrow></mfenced></math>
<math><mo>&#8658;</mo><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mn>0</mn></mrow></msubsup><msub><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>10</mn><mo>&#215;</mo><msubsup><mrow><mi mathvariant="normal">&#955;</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mn>0</mn></mrow></msubsup><msub><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mn>1</mn></mrow></msub></math>
<math><msub><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>10</mn><msub><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mn>1</mn></mrow></msub></math> ...... (ii)
<math><msub><mrow><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">a</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">C</mi><msup><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">&#945;</mi></mrow></mfrac></math> , But <math><mi mathvariant="normal">&#945;</mi><mo>&#8810;</mo><mn>1</mn></math> , therefore <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">K</mi><mi mathvariant="normal">a</mi></msub><mo>=</mo><mi mathvariant="normal">C</mi><msup><mi mathvariant="normal">&#945;</mi><mn>2</mn></msup></math>
<math><mo>&#8658;</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">a</mi></mrow></msub><mo>(</mo><mi mathvariant="normal">H</mi><mi mathvariant="normal">X</mi><mo>)</mo></mrow><mrow><msub><mrow><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">a</mi></mrow></msub><mo>(</mo><mi mathvariant="normal">H</mi><mi mathvariant="normal">Y</mi><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>0.01</mn><msubsup><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow><mrow><mn>0.1</mn><msubsup><mrow><mi mathvariant="normal">&#945;</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>0.01</mn></mrow><mrow><mn>0.1</mn></mrow></mfrac><mo>&#215;</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>10</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1000</mn></mrow></mfrac></math>
<math><mo>&#8658;</mo><mrow><mrow><mo>[</mo><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mo>(</mo><msub><mrow><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">a</mi></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">X</mi></mrow></mfenced><mo>-</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mfenced close="]" separators="|"><mrow><msub><mrow><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">a</mi></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">Y</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mo>-</mo><mn>3</mn></mrow></mrow></mrow></mrow></math>
<math><mo>&#8658;</mo><mi mathvariant="normal">p</mi><msub><mrow><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">a</mi></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">X</mi></mrow></mfenced><mo>-</mo><mi mathvariant="normal">p</mi><msub><mrow><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">a</mi></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">Y</mi></mrow></mfenced><mo>=</mo><mn>3</mn></math>

</details>

---

### Q9. JEE Advanced 2013 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

An aqueous solution of X is added slowly to an aqueous solution of Y as shown in List I. The variation in conductivity of these reactions is given in List II. Match List I with List II and select the correct using answer the code given below the lists :
 <table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td><strong>List I</strong></td>			<td> </td>			<td><strong>List II</strong></td>		</tr>		<tr>			<td>a. </td>			<td><math> <mrow> <mtable> <mtr> <mtd> <msub> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <msub> <mtext>C</mtext> <mn>2</mn> </msub> <msub> <mtext>H</mtext> <mn>5</mn> </msub> </mrow> </mfenced> </mrow> <mn>3</mn> </msub> <mtext>N</mtext> <mo>+</mo> <msub> <mtext>CH</mtext> <mn>3</mn> </msub> <mtext>COOH</mtext> </mtd> </mtr> <mtr> <mtd> <mtext>X</mtext> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mtable> <mtr> <mtd> <mtext>Y</mtext> </mtd> </mtr> </mtable> </mtd> </mtr> </mtable> </mrow> </math></td>			<td>p. </td>			<td>Conductivity decreases and then 
			increases </td>		</tr>		<tr>			<td>b. </td>			<td><math> <mrow> <mtable> <mtr> <mtd> <mtext>KI</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mn>0</mn> <mtext>.</mtext> <mn>1</mn> <mtext>M</mtext> </mrow> </mfenced> <mo>+</mo> <msub> <mtext>AgNO</mtext> <mn>3</mn> </msub> <mfenced close=")" open="(" separators=","> <mrow> <mn>0</mn> <mtext>.</mtext> <mn>0</mn> <mn>1</mn> <mtext>M</mtext> </mrow> </mfenced> </mtd> </mtr> <mtr> <mtd> <mtext>X</mtext> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mtable> <mtr> <mtd> <mtext>Y</mtext> </mtd> </mtr> </mtable> </mtd> </mtr> </mtable> </mrow> </math></td>			<td>q. </td>			<td>Conductivity decreases and then
			does not change much </td>		</tr>		<tr>			<td>c. </td>			<td><math> <mrow> <mtable> <mtr> <mtd> <msub> <mtext>CH</mtext> <mn>3</mn> </msub> <mtext>COOH</mtext> <mo>+</mo> <mtext>KOH</mtext> </mtd> </mtr> <mtr> <mtd> <mtext>X</mtext> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mtable> <mtr> <mtd> <mtext>Y</mtext> </mtd> </mtr> </mtable> </mtd> </mtr> </mtable> </mrow> </math></td>			<td>r. </td>			<td>Conductivity increases and then
			does not change much</td>		</tr>		<tr>			<td>d. </td>			<td><math> <mrow> <mtable> <mtr> <mtd> <mtext>NaOH</mtext> <mo>+</mo> <mtext>HI</mtext> </mtd> </mtr> <mtr> <mtd> <mtext>X</mtext> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mtable> <mtr> <mtd> <mtext>Y</mtext> </mtd> </mtr> </mtable> </mtd> </mtr> </mtable> </mrow> </math></td>			<td>s. </td>			<td>Conductivity does not change much and 
			then increases</td>		</tr>	</tbody></table>

**Options:**

- **(A)** a-r;b-s;c-q;d-p;
- **(B)** a-q;b-s;c-r;d-p;
- **(C)** a-p;b-r;c-s;d-q;
- **(D)** a-p;b-s;c-q;d-r;

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) a-r;b-s;c-q;d-p;**

**Detailed Solution:**

p)  (C<sub>2</sub>H<sub>5</sub>)<sub>3</sub> N added to CH<sub>3</sub>COOH
(C<sub>2</sub>H<sub>5</sub>)<sub>3</sub> NH<sup>+</sup> and CH<sub>3</sub>COO<sup>-</sup> ions generated in solution, conductivity increases &amp; then remains constant as (C<sub>2</sub>H<sub>5</sub>)<sub>3</sub> N is not dissociated when in excess.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/0bd481aa-0e29-40bf-965d-cfe2b1836f5e-image.png" style="width: 300px; height: 176px;" />
q)  KI<sub>eq</sub> added to AgNO<sub>3</sub>
<math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <msubsup> <mtext>Ag</mtext> <mtext>(aq)</mtext> <mo>+</mo> </msubsup> <mo>+</mo> <msubsup> <mtext>NO</mtext> <mrow> <mn>3</mn> <mtext>(aq)</mtext> </mrow> <mo>-</mo> </msubsup> </mrow> </mfenced> <mo>+</mo> <mtext>KI</mtext> <mo>&#10230;</mo> <mfenced close="]" open="[" separators=","> <mrow> <msubsup> <mtext>K</mtext> <mtext>(aq)</mtext> <mo>+</mo> </msubsup> <mo>+</mo> <msubsup> <mtext>NO</mtext> <mrow> <mn>3</mn> <mtext>(aq)</mtext> </mrow> <mo>-</mo> </msubsup> </mrow> </mfenced> <mo>+</mo> <mtext>AgI</mtext> </mrow> </math>
<math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mtext>Ag</mtext> <mo>+</mo> </msup> <mo>&#38;</mo> <msubsup> <mtext>NO</mtext> <mn>3</mn> <mo>-</mo> </msubsup> </mrow> </mfenced> </mrow> </math>  ions replaced by <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <msubsup> <mtext>K</mtext> <mtext>(aq)</mtext> <mo>+</mo> </msubsup> <mo>&#38;</mo> <msubsup> <mtext>NO</mtext> <mrow> <mn>3</mn> <mtext>(aq)</mtext> </mrow> <mo>-</mo> </msubsup> </mrow> </mfenced> </mrow> </math>
conductivity does not change till complete precipitation but later on with additional KI<sub>(aq)</sub> added conductivity will increase.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/35b64711-ffb4-4e10-b51e-ebebe5f75645-image.png" style="width: 300px; height: 164px;" />
r)  On addition of acetic acid to KOH. KOH fully dissociated replaced by
<math> <mrow> <msub> <mtext>CH</mtext> <mn>3</mn> </msub> <mtext>COOH</mtext> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mtext>K</mtext> <mo>+</mo> </msup> <mo>+</mo> <msup> <mtext>OH</mtext> <mo>-</mo> </msup> </mrow> </mfenced> <mo>&#10230;</mo> <mfenced close="]" open="[" separators=","> <mrow> <msub> <mtext>CH</mtext> <mn>3</mn> </msub> <msup> <mtext>COO</mtext> <mo>-</mo> </msup> <mo>+</mo> <msup> <mtext>K</mtext> <mo>+</mo> </msup> </mrow> </mfenced> <mo>+</mo> <msub> <mtext>H</mtext> <mn>2</mn> </msub> <mtext>O</mtext> </mrow> </math>
The net result is replacement of OH<sup>-</sup> by CH<sub>3</sub>COO<sup>-</sup> ions whose ionic mobility is less so conductivity will decrease first and then will not change much due to addition of CH<sub>3</sub>COOH(in excess) which will not be dissociated
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/85de8e9d-c815-4419-9072-1e4079233d4c-image.png" style="width: 300px; height: 173px;" /> 
s)  On addition of NaOH to HI <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <msubsup> <mtext>H</mtext> <mtext>(aq)</mtext> <mo>+</mo> </msubsup> <mo>+</mo> <msubsup> <mtext>I</mtext> <mtext>(aq)</mtext> <mo>-</mo> </msubsup> </mrow> </mfenced> <mo>+</mo> <mtext>NaOH</mtext> <mo>&#10230;</mo> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mtext>Na</mtext> <mo>+</mo> </msup> <mo>+</mo> <msup> <mtext>I</mtext> <mo>-</mo> </msup> </mrow> </mfenced> <mo>+</mo> <msub> <mtext>H</mtext> <mn>2</mn> </msub> <mtext>O</mtext> </mrow> </math>
there will be replacement of H<sup>+</sup> by Na<sup>+</sup> whose mobility is less than H<sup>+</sup> which means conductivity will decrease first &amp; then due to adding NaOH which is a strong electrolyte which fully dissociates, so conductivity will increase.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/df925f64-e431-44d8-9161-3d1be01c950c-image.png" style="width: 300px; height: 166px;" />

</details>

---

### Q10. JEE Advanced 2011 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

$\mathrm{AgNO}_3(a q)$ was added to an aqueous $\mathrm{KCl}$ solution gradually and the conductivity of the solution was measured. The plot of conductance $(\Lambda)$ versus the volume of $\mathrm{AgNO}_3$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/x4Pn93AWrdiTkVBRs6YPrh21nwy2nt14bs0_b-LZpos.original.fullsize.png">

**Options:**

- **(A)** $P$
- **(B)** $Q$
- **(C)** $R$
- **(D)** $S$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $S$**

**Detailed Solution:**

As $\mathrm{AgNO}_3$ is added to solution, $\mathrm{KCl}$ will be displaced accrding to following reaction
$$
\mathrm{AgNO}_3(a q)+\mathrm{KCl}(a q) \longrightarrow \operatorname{AgCl}(s)+\mathrm{KNO}_3(a q)
$$
For every mole of $\mathrm{KCl}$ displaced from solution, one mole of $\mathrm{KNO}_3$ comes in solution resulting in almost constant conductivity. As the end point is reached, added $\mathrm{AgNO}_3$ remain in solution increasing ionic concentration, hence conductivity increases.

</details>

---

### Q11. JEE Advanced 2006

*Type:* `numerical` | *Level:* `3`

We have taken a saturated solution of $\mathrm{AgBr}, K_{\mathrm{sp}}$ is $12 \times 10^{-14}$. If $10^{-7}$ mole of $\mathrm{AgNO}_3$ are added to 1 litre of this solution, find conductivity (specific conductance) of this solution in terms of $10^{-7} \mathrm{Sm}^{-1}$ units.
$$
\text { Given, } \begin{aligned}
\lambda_{\left(\mathrm{Ag}^{+}\right)}^{\circ} & =6 \times 10^{-3} \mathrm{Sm}^2 \mathrm{~mol}^{-1}, \lambda_{\left(\mathrm{Br}^{-}\right)}^{\circ}=8 \times 10^{-3} \mathrm{Sm}^2 \mathrm{~mol}^{-1}, \\
\lambda_{\left(\mathrm{NO}_3^{-}\right)} & =7 \times 10^{-3} \mathrm{Sm}^2 \mathrm{~mol}^{-1},
\end{aligned}
$$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **55**

**Detailed Solution:**

Suppose the solubility of $\mathrm{AgBr}$ in $10^{-7} \mathrm{MAgNO}_3$ is $\mathrm{mol} / \mathrm{L}$
$$
\begin{aligned}
& \underset{s \mathrm{~mol} / \mathrm{L}}{\mathrm{AgBr}} \rightleftharpoons \mathrm{Ag}^{+}+\mathrm{Br}^{-} \\
& \mathrm{AgNO}_3 \rightleftharpoons \mathrm{Ag}^{+}+\mathrm{NO}_3^{-} \\
& 10^{-7} \mathrm{M} \quad 10^{-7} \mathrm{M} \times 10^{-7} \mathrm{M} \\
& \text { Total }\left[\mathrm{Ag}^{+}\right]=\left(s+10^{-7}\right) \mathrm{M} \\
& K_{\mathrm{sp}} \text { of } \mathrm{AgBr}=\left[\mathrm{Ag}^{+}\right]\left[\mathrm{Br}^{-}\right] \\
& 12 \times 10^{-14}=\left(s+10^{-7}\right)(s)=s^2+10^{-7} s \\
& s^2+10^{-7} s-12 \times 10^{-14}=0 \\
&
\end{aligned}
$$
On solving $s=3 \times 10^{-7} \mathrm{M}$
Hence, $\left[\mathrm{Br}^{-}\right]=3 \times 10^{-7} \mathrm{M}=3 \times 10^{-7} \times 10^3 \mathrm{~m}^3=3 \times 10^{-4} \mathrm{~m}^3$
$$
\left[\mathrm{Ag}^{+}\right]=\left(3 \times 10^{-7}+10^{-7}\right) \mathrm{M}=4 \times 10^{-7} \times 10^3 \mathrm{~m}^3=4 \times 10^{-4} \mathrm{~m}^3
$$
$$
\left[\mathrm{NO}_3^{-}\right]=10^{-7} \mathrm{M}=10^{-7} \times 10^{+3}=1 \times 10^{-4} \mathrm{~m}^3
$$
$$
\because \quad \lambda=\frac{k}{C} \text { or } k=\lambda \times C
$$

$$
\begin{aligned}
\therefore \quad k_{\mathrm{Br}^{-}} & =3 \times 10^{-4} \times 8 \times 10^{-3} \mathrm{Sm}^{-1}=24 \times 10^{-7} \mathrm{Sm}^{-1} \\
k_{\mathrm{Ag}^{+}} & =4 \times 10^{-4} \times 6 \times 10^{-3} \mathrm{Sm}^{-1}=24 \times 10^{-7} \mathrm{Sm}^{-1} \\
k_{\mathrm{NO}_3^{-}} & =1 \times 10^{-4} \times 7 \times 10^{-3}=7 \times 10^{-7} \mathrm{Sm}^{-1} \\
k_{\text {Total }} & =k_{\mathrm{Br}^{-}}+k_{\mathrm{Ag}^{+}}+k_{\mathrm{NO}_3^{-}} \\
& =\left(24 \times 10^{-7}+24 \times 10^{-7}+7 \times 10^{-7} \mathrm{Sm}^{-1}\right. \text { ) } \\
& =55 \times 10^{-7} \mathrm{Sm}^{-1} \\
& \left.=\mathbf{5 5} \mathbf{S m}^{-1} \text { (in term of } 10^{-7} \mathrm{Sm}^{-1}\right)
\end{aligned}
$$

</details>

---

