# JEE Advanced Mathematics - Probability

## Topic 6: Bernoulli Trial and Binomial Distribution

**Total Questions:** 3

---

### Q1. JEE Advanced 2020 (Paper 2)

*Type:* `numerical` | *Level:* `3`

The probability that a missile hits a target successfully is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>75</mn><mo>.</mo></math> In order to destroy the target completely, at least three successful hits are required. Then the minimum number of missiles that have to be fired so that the probability of completely destroying the target is not less than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>95</mn><mo>,</mo></math> is ___________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p>Let the number of missiles be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi></math> (of destroying the target) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8805;</mo><mn>0</mn><mo>.</mo><mn>95</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>&#183;</mo><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>3</mn></msup><mo>&#183;</mo><msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>4</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mi>n</mi></msup><mo>&#8805;</mo><mn>0</mn><mo>.</mo><mn>95</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfenced close="}" open="{"><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>0</mn></msup><mo>&#183;</mo><msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mi>n</mi></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>1</mn></msup><mo>&#183;</mo><msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>2</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mo>&#8805;</mo><mn>0</mn><mo>.</mo><mn>95</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><mn>95</mn><mn>100</mn></mfrac><mo>&#8805;</mo><mfrac><mn>1</mn><msup><mn>4</mn><mi>n</mi></msup></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><msup><mn>4</mn><mi>n</mi></msup></mfrac><mo>+</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>9</mn><msup><mn>4</mn><mi>n</mi></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>4</mn><mi>n</mi></msup><mn>20</mn></mfrac><mo>&#8805;</mo><mfrac><mrow><mn>2</mn><mo>+</mo><mn>6</mn><mi>n</mi><mo>+</mo><mn>9</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mi>n</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>2</mn><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mn>5</mn></mfrac><mo>&#8805;</mo><mn>9</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8805;</mo><mn>5</mn><mfenced><mrow><mn>9</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>3</mn><mo>&#8658;</mo><mn>32</mn><mo>&#8805;</mo><mn>5</mn><mo>&#215;</mo><mn>74</mn></math>   (not true)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mn>128</mn><mo>&#8805;</mo><mn>5</mn><mo>&#215;</mo><mn>134</mn></math>   (not true)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>5</mn><mo>&#8658;</mo><mn>512</mn><mo>&#8805;</mo><mn>5</mn><mo>&#215;</mo><mn>212</mn></math>    (not true)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>6</mn><mo>&#8658;</mo><mn>2048</mn><mo>&#8805;</mo><mn>5</mn><mo>&#215;</mo><mn>308</mn></math>    (true)</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>6</mn></math>.</p>

</details>

---

### Q2. JEE Advanced 2015 (Paper 1)

*Type:* `numerical` | *Level:* `1`

The minimum number of times a fair coin needs to be tossed so that the probability of getting at least two heads is at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>96</mn></math>, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mn>2</mn></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mn>3</mn></mfenced><mo>&#8230;</mo><mo>&#8805;</mo><mn>0</mn><mo>.96</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mi>P</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>&#8805;</mo><mn>0</mn><mo>.96</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mn>0</mn><mo>.96</mo><msup><mo>&#8805;</mo><mi>n</mi></msup><msub><mi>C</mi><mn>0</mn></msub><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>n</mi></msup><msup><mo>+</mo><mi>n</mi></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>n</mi></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>.04</mo></mrow></mfenced><msup><mn>2</mn><mi>n</mi></msup><mo>&#8805;</mo><mn>1</mn><mo>+</mo><mi>n</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mo>.2</mo><mi>n</mi></msup><mo>&#8805;</mo><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>100</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup><mo>&#8805;</mo><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>100</mn></math>
As, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>10</mn></msup><mo>&#8805;</mo><mn>900</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>8</mn></math>

</details>

---

### Q3. JEE Advanced 2012 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Four fair dice $D_{1}, D_{2}, D_{3}$ and $D_{4}$; each having six faces numbered $1,2,3,4,5$ and 6 are rolled simultaneously. The probability that $D_{4}$ shows a number appearing on one of $D_{1}, D_{2}$ and $\mathrm{D}_{3}$ is

**Options:**

- **(A)** $\frac{91}{216}$
- **(B)** $\frac{108}{216}$
- **(C)** $\frac{125}{216}$
- **(D)** $\frac{127}{216}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{91}{216}$**

**Detailed Solution:**

$D_{4}$ can show a number appearing on one of $D_{1}, D_{2}$ and $D_{3}$ in the following cases.

Case $\mathbf{I}: D_{4}$ shows a number which is shown by exactly one of $D_{1}, D_{2}$ and $D_{3}$.

$D_{4}$ shows a number in ${ }^{6} C_{1}$ ways.

One out of $D_{1}, D_{2}$ and $D_{3}$ can be selected in ${ }^{3} C_{1}$ ways.

[The selected die shows the same number as on $D_{4}$ in one way and rest two dice show the different number in 5 ways each, ]

$\therefore$ Number of ways

$={ }^{6} C_{1} \times{ }^{3} C_{1} \times 1 \times 5 \times 5=450$

Case II : $D_{4}$ shows a number which is shown by exactly two of $D_{1}, D_{2}$ and $D_{3}$.

Number of ways

$={ }^{6} C_{1} \times{ }^{3} C_{2} \times 1 \times 1 \times 5=90$

Case III : $D_{4}$ shows a number which is shown by all three dice $D_{1}, D_{2}$ and $D_{3}$.

Number of ways

$={ }^{6} C_{1} \times{ }^{3} C_{3} \times 1 \times 1 \times 1=6$

$\therefore$ Total number of favourable ways $=450+90+6=546$ Total ways $=6 \times 6 \times 6 \times 6$

$\therefore$ Required Probability $=\frac{546}{6 \times 6 \times 6 \times 6}=\frac{91}{216}$

</details>

---

