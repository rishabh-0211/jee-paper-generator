# JEE Advanced Mathematics - Probability

## Topic 1: Classical Definition of Probability

**Total Questions:** 12

---

### Q1. JEE Advanced 2023 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider an experiment of tossing a coin repeatedly until the outcomes of two consecutive tosses are same. If the probability of a random toss resulting in head is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>, then the probability that the experiment stops with head is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>21</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>21</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>7</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>21</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>H</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>T</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>Now probability of the event is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>E</mi><mo>)</mo><mo>=</mo><mi>P</mi><mo>(</mo><mi>H</mi><mi>H</mi><mo>)</mo><mo>+</mo><mi>P</mi><mo>(</mo><mi>T</mi><mi>H</mi><mi>H</mi><mo>)</mo><mo>+</mo><mi>P</mi><mo>(</mo><mi>H</mi><mi>T</mi><mi>H</mi><mi>H</mi><mo>)</mo><mo>+</mo><mi>P</mi><mo>(</mo><mi>T</mi><mi>H</mi><mi>T</mi><mi>H</mi><mi>H</mi><mo>)</mo><mo>+</mo><mi>P</mi><mo>(</mo><mi>H</mi><mi>T</mi><mi>H</mi><mi>T</mi><mi>H</mi><mi>H</mi><mo>)</mo><mo>+</mo><mi>P</mi><mo>(</mo><mi>T</mi><mi>H</mi><mi>T</mi><mi>H</mi><mi>T</mi><mi>H</mi><mi>H</mi><mo>)</mo><mo>+</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>(</mo><mi>E</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><msup><mn>3</mn><mn>5</mn></msup></mfrac><mo>+</mo><mfrac><mn>4</mn><msup><mn>3</mn><mn>6</mn></msup></mfrac><mo>+</mo><mfrac><mn>8</mn><msup><mn>3</mn><mn>7</mn></msup></mfrac><mo>+</mo><mfrac><mn>8</mn><msup><mn>3</mn><mn>8</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>(</mo><mi>E</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mn>3</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mn>3</mn><mn>4</mn></msup></mfrac><mo>+</mo><mfrac><mn>4</mn><msup><mn>3</mn><mn>5</mn></msup></mfrac><mo>+</mo><mfrac><mn>4</mn><msup><mn>3</mn><mn>6</mn></msup></mfrac><mo>+</mo><mfrac><mn>8</mn><msup><mn>3</mn><mn>7</mn></msup></mfrac><mo>+</mo><mfrac><mn>8</mn><msup><mn>3</mn><mn>8</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>(</mo><mi>E</mi><mo>)</mo><mo>=</mo><mfenced separators="|"><mrow><mfrac><mn>1</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mn>3</mn><mn>4</mn></msup></mfrac><mo>+</mo><mfrac><mn>4</mn><msup><mn>3</mn><mn>6</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mfrac><mn>2</mn><msup><mn>3</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>4</mn><msup><mn>3</mn><mn>5</mn></msup></mfrac><mo>+</mo><mfrac><mn>8</mn><msup><mn>3</mn><mn>7</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>(</mo><mi>E</mi><mo>)</mo><mo>=</mo><mfenced separators="|"><mfrac><mfrac><mn>1</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac></mrow></mfenced></mfrac></mfenced><mo>+</mo><mfenced separators="|"><mfrac><mfrac><mn>2</mn><msup><mn>3</mn><mn>3</mn></msup></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac></mrow></mfenced></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>(</mo><mi>E</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>21</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>21</mn></mfrac></math></p></blockquote>

</details>

---

### Q2. JEE Advanced 2023 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi mathvariant="normal">&#8484;</mi><mo>&#215;</mo><mi mathvariant="normal">&#8484;</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>8</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>20</mn></mfrac><mo>&#60;</mo><mn>1</mn><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#60;</mo><mn>5</mn><mi mathvariant="normal">x</mi></mrow></mfenced></math>. Three distinct point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>,</mo><mo>&#160;</mo><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> are randomly chosen from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>. Then the probability that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>,</mo><mo>&#160;</mo><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> form a triangle whose area is a positive integer, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>71</mn><mn>220</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>73</mn><mn>220</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>79</mn><mn>220</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>83</mn><mn>220</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>73</mn><mn>220</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Equation of ellipse <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>8</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>20</mn></mfrac><mo>=</mo><mn>1</mn></math></p><p>And equation of parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>5</mn><mi mathvariant="normal">x</mi></math></p><p>Now intersection point of ellipse and parabola will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><msqrt><mn>10</mn></msqrt></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>-</mo><msqrt><mn>10</mn></msqrt></mrow></mfenced></math></p><p>Now plotting the region <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>8</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>20</mn></mfrac><mo>&#60;</mo><mn>1</mn><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#60;</mo><mn>5</mn><mi mathvariant="normal">x</mi></math> we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/e7ac496b-07c5-4b63-96d0-c586ebc3c5ce.png" style="width: 300px; height: 229px;" /></p><p>Now randomly chosen points will be between origin and the intersecting point,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/fe39bf9a-2da7-44d0-8ecf-2e43c948cfff.png" style="width: 300px; height: 267px;" /></p><p>So, the integer points inside region are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mspace linebreak="newline"></mspace><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></mrow></mfenced></math></p><p>Total number of ways to select three points <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>12</mn></mmultiscripts><mo>=</mo><mn>220</mn></math></p><p>Required number of triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><mo>+</mo><mn>9</mn><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>=</mo><mn>73</mn></math></p><p>{Note: Points are taken such a way that distance between two points are multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> for example if we take points on line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> we can take following points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math></p><p>so there will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> pairs from line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> and will chose another point from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> line so triangle will have a positive area. Also note that height of the triangle will always be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>}</p><p>Hence, probability will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>73</mn><mn>220</mn></mfrac></math></p></blockquote>

</details>

---

### Q3. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `1`

A number is chosen at random from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>2000</mn></mrow></mfenced></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> be the probability that the chosen number is a multiple of 3 or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn><mi>p</mi></math> is ____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **214**

**Detailed Solution:**

<p>Multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>=</mo><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn><mo>&#8230;</mo><mo>.</mo><mn>1998</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>666</mn></math></p><p>Multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>=</mo><mn>7</mn><mo>,</mo><mn>14</mn><mo>&#8230;</mo><mo>.</mo><mn>1995</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>285</mn></math></p><p>Multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn><mo>=</mo><mn>21</mn><mo>,</mo><mn>42</mn><mo>&#8230;</mo><mn>1995</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>95</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mrow><mn>666</mn><mo>+</mo><mn>285</mn><mo>-</mo><mn>95</mn></mrow><mn>2000</mn></mfrac><mo>=</mo><mfrac><mn>856</mn><mn>2000</mn></mfrac><mo>=</mo><mfrac><mn>214</mn><mn>500</mn></mfrac><mo>=</mo><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn><mi>p</mi><mo>=</mo><mn>214</mn></math></p>

</details>

---

### Q4. JEE Advanced 2021 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>,</mo><mo>&#160;</mo><mi>F</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math> be three events having probabilities <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>E</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>,</mo><mi>P</mi><mo>(</mo><mi>F</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>G</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo></math> and let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>E</mi><mo>&#8745;</mo><mi>F</mi><mo>&#8745;</mo><mi>G</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></math>
For any event <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>H</mi><mi>c</mi></msup></math> denotes its complement, then which of the following statements is (are) TRUE ?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>F</mi><mo>&#8745;</mo><msup><mi>G</mi><mi>c</mi></msup></mrow></mfenced><mo>&#8804;</mo><mfrac><mn>1</mn><mn>40</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msup><mi>E</mi><mi>c</mi></msup><mo>&#8745;</mo><mi>F</mi><mo>&#8745;</mo><mi>G</mi></mrow></mfenced><mo>&#8804;</mo><mfrac><mn>1</mn><mn>15</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>E</mi><mo>&#8746;</mo><mi>F</mi><mo>&#8746;</mo><mi>G</mi><mo>)</mo><mo>&#8804;</mo><mfrac><mn>13</mn><mn>24</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msup><mi>E</mi><mi>c</mi></msup><mo>&#8745;</mo><msup><mi>F</mi><mi>c</mi></msup><mo>&#8745;</mo><msup><mi>G</mi><mi>c</mi></msup></mrow></mfenced><mo>&#8804;</mo><mfrac><mn>5</mn><mn>12</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>E</mi><mo>&#8746;</mo><mi>F</mi><mo>&#8746;</mo><mi>G</mi><mo>)</mo><mo>&#8804;</mo><mfrac><mn>13</mn><mn>24</mn></mfrac></math>**

**Detailed Solution:**

(i)<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>F</mi><mo>&#8745;</mo><msup><mi>G</mi><mi>c</mi></msup></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>F</mi></mrow></mfenced><mo>-</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>F</mi><mo>&#8745;</mo><mi>G</mi></mrow></mfenced><mo>&#8804;</mo><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>40</mn></mfrac></math>

(ii)<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msup><mi>E</mi><mi>c</mi></msup><mo>&#8745;</mo><mi>F</mi><mo>&#8745;</mo><mi>G</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mo>(</mo><mi>F</mi><mo>&#8745;</mo><mi>G</mi><mo>)</mo><mo>-</mo><mi>P</mi><mo>(</mo><mi>E</mi><mo>&#8745;</mo><mi>F</mi><mo>&#8745;</mo><mi>G</mi><mo>)</mo><mo>&#8804;</mo><mi>P</mi><mo>(</mo><mi>F</mi><mo>)</mo><mo>-</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>15</mn></mfrac></math>

(iii)

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8746;</mo><mi>F</mi><mo>&#8746;</mo><mi>G</mi></mrow></mfenced><mo>&#8804;</mo><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>F</mi></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>G</mi></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>6</mn></mrow><mn>24</mn></mfrac><mo>=</mo><mfrac><mn>13</mn><mn>24</mn></mfrac></math>

(iv)<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><msub><mfenced><mrow><msup><mi>E</mi><mi>c</mi></msup><mo>&#8745;</mo><msup><mi>F</mi><mi>c</mi></msup><mo>&#8745;</mo><msup><mi>G</mi><mi>c</mi></msup></mrow></mfenced><mi>max</mi></msub><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mo>(</mo><mi>E</mi><mo>&#8745;</mo><mi>F</mi><mo>&#8745;</mo><mi>G</mi><msub><mo>)</mo><mi>min</mi></msub></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>P</mi><mo>(</mo><mi>E</mi><mo>&#8745;</mo><mi>F</mi><mo>&#8745;</mo><mi>G</mi><msub><mo>)</mo><mi>min</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>

Thus<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msup><mi>E</mi><mi>c</mi></msup><mo>&#8745;</mo><msup><mi>F</mi><mi>c</mi></msup><mo>&#8745;</mo><msup><mi>G</mi><mi>c</mi></msup></mrow></mfenced><mo>&#8804;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math>

</details>

---

### Q5. JEE Advanced 2018 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

<strong> Paragraph: </strong> There are five students <math><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>S</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>S</mi></mrow><mrow><mn>4</mn></mrow></msub></math> and <math><msub><mrow><mi>S</mi></mrow><mrow><mn>5</mn></mrow></msub></math> in a music class and for them there are five seats <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></msub></math> and <math><msub><mrow><mi>R</mi></mrow><mrow><mn>5</mn></mrow></msub></math> arranged in a row, where initially the seat <math><msub><mrow><mi>R</mi></mrow><mrow><mi>i</mi></mrow></msub></math> is allotted to the student <math><msub><mrow><mi>S</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>,</mo><mi>&#160;</mi><mi>i</mi><mi>&#160;</mi><mo>=</mo><mi>&#160;</mi><mn>1,2</mn><mo>,</mo><mn>3,4</mn><mo>,</mo><mn>5</mn><mo>.</mo></math> But, on the examination day, the five students are randomly allotted the five seats
 <strong> Question : </strong>For <math> <mrow> <mi>i</mi><mi>&#160;</mi><mo>=</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn> </mrow> </math> Let <math> <mrow> <msub> <mi>T</mi> <mi>i</mi> </msub> </mrow> </math> denote the event that the students <math> <mrow> <msub> <mi>S</mi> <mi>i</mi> </msub> </mrow> </math> and <math> <mrow> <msub> <mi>S</mi> <mrow> <mi>i</mi><mo>+</mo><mn>1</mn> </mrow> </msub> </mrow> </math> do NOT sit adjacent to each other on the day of the examination. Then, the probability of the event <math><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>&#8745;</mo><mi>&#160;</mi><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&#8745;</mo><mi>&#160;</mi><msub><mrow><mi>T</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#8745;</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>4</mn></mrow></msub></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>60</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>60</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>n</mi><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>&#8745;</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&#8745;</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#8745;</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>4</mn></mrow></msub><mi>&#160;</mi></mrow></mfenced><mo>=</mo><mi>T</mi><mi>o</mi><mi>t</mi><mi>a</mi><mi>l</mi><mo>-</mo><mi>n</mi><mfenced separators="|"><mrow><mover accent="false"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mo>&#175;</mo></mover><mo>&#8746;</mo><mover accent="false"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mo>&#175;</mo></mover><mo>&#8746;</mo><mover accent="false"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow><mo>&#175;</mo></mover><mo>&#8746;</mo><mover accent="false"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>4</mn></mrow></msub></mrow><mo>&#175;</mo></mover></mrow></mfenced></math>
<math><mo>=</mo><mn>5</mn><mo>!</mo><mo>-</mo><mfenced separators="|"><mrow><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>4</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mn>4</mn><mo>!</mo><mn>2</mn><mo>!</mo><mo>-</mo><mfenced separators="|"><mrow><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>3</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>.</mo><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo><mo>+</mo><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>3</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>2</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mn>2</mn><mo>!</mo><mn>2</mn><mo>!</mo><mo>+</mo><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>4</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>.</mo><mn>2.2</mn><mo>!</mo></mrow></mfenced><mo>-</mo><mn>2</mn></mrow></mfenced></math>
<math><mo>=</mo><mi>&#160;</mi><mi>&#160;</mi><mn>14</mn></math>
Probability <math><mo>=</mo><mfrac><mrow><mn>14</mn></mrow><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>60</mn></mrow></mfrac></math>

</details>

---

### Q6. JEE Advanced 2018 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<strong> Paragraph: </strong> There are five students <math><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>S</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>S</mi></mrow><mrow><mn>4</mn></mrow></msub></math> and <math><msub><mrow><mi>S</mi></mrow><mrow><mn>5</mn></mrow></msub></math> in a music class and for them there are five seats <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></msub></math> and <math><msub><mrow><mi>R</mi></mrow><mrow><mn>5</mn></mrow></msub></math> arranged in a row, where initially the seat <math><msub><mrow><mi>R</mi></mrow><mrow><mi>i</mi></mrow></msub></math> is allotted to the student <math><msub><mrow><mi>S</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>,</mo><mi>&#160;</mi><mi>i</mi><mi>&#160;</mi><mo>=</mo><mi>&#160;</mi><mn>1,2</mn><mo>,</mo><mn>3,4</mn><mo>,</mo><mn>5</mn><mo>.</mo></math> But, on the examination day, the five students are randomly allotted the five seats
 <strong> Question : </strong>The probability that, on the examination day, the student <math><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub></math> gets the previously allotted seat <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo></math> and NONE of the remaining students gets the seat previously allotted to him/her is

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>40</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>40</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>40</mn></mrow></mfrac></math>**

**Detailed Solution:**

Required probability <math><mo>=</mo><mfrac><mrow><mn>4</mn><mo>!</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mo>!</mo></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>120</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>40</mn></mrow></mfrac></math>

</details>

---

### Q7. JEE Advanced 2017 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Three randomly chosen non negative integers <math><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mi>z</mi></math> are found to satisfy the equation  <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>10</mn></math> . Then the probability that <math><mi>z</mi></math> is even, is

**Options:**

- **(A)** <math><mfrac><mrow><mn>36</mn></mrow><mrow><mn>55</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>6</mn></mrow><mrow><mn>11</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>11</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>6</mn></mrow><mrow><mn>11</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let <math><mi>z</mi><mo>=</mo><mn>2</mn><mi>k</mi><mo>,</mo><mi>&#160;</mi></math> where  <math><mi>k</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn></math></p><p><math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>10</mn><mo>-</mo><mn>2</mn><mi>k</mi></math></p><p>Number of non negative integral solutions</p><p><math><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mrow><mn>5</mn></mrow></munderover><mrow><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>11</mn><mo>-</mo><mn>2</mn><mi>k</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mrow><mo>=</mo><mi>&#160;</mi><mrow><mo stretchy="false">&#8721;</mo><mrow><mn>11</mn><mo>-</mo><mn>2</mn><mi>k</mi></mrow></mrow><mo>=</mo><mn>3</mn><mn>6</mn></math></p><p>Total cases <math><mo>=</mo><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>10</mn><mo>+</mo><mn>3</mn><mo>-</mo><mn>1</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>66</mn></math></p><p>Required probability <math><mo>=</mo><mfrac><mrow><mn>36</mn></mrow><mrow><mn>66</mn></mrow></mfrac><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mn>6</mn></mrow><mrow><mn>11</mn></mrow></mfrac></math></p>

</details>

---

### Q8. JEE Advanced 2014 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

<strong> Paragraph: </strong>

Box $1$ contains three cards bearing numbers $1,2,3$; box $2$ contains five cards bearing numbers $1,2,3,4,5$; and box $3$ contains seven cards bearing numbers $1,2,3,4,5,6,7$. A card is drawn from each of the boxes. Let $x_{i}$ be the number on the card drawn from the $i^{t h}$ box, $i=1,2,3$.


 <strong> Question: </strong>

The probability that $x_{1}+x_{2}+x_{3}$ is odd, is

**Options:**

- **(A)** <math><mfrac><mrow><mn>29</mn></mrow><mrow><mn>105</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>53</mn></mrow><mrow><mn>105</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>57</mn></mrow><mrow><mn>105</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>53</mn></mrow><mrow><mn>105</mn></mrow></mfrac></math>**

**Detailed Solution:**

Case I: One odd, 2 even
Total number of ways <math><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>1</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>1</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>29</mn></math>
Case II: All 3 odd
Number of ways <math><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>24</mn></math>
Favourable ways = 53
Required probability <math><mo>=</mo><mfrac><mrow><mn>53</mn></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>7</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>53</mn></mrow><mrow><mn>105</mn></mrow></mfrac></math>

</details>

---

### Q9. JEE Advanced 2010 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\omega$ be a complex cube root of unity with $\omega \neq 1$. A fair die is thrown three times. If $r_1, r_2$ and $r_3$ are the numbers obtained on the die, then the probability that $\omega^{r_1}+\omega^{r_2}+\omega^{r_3}=0$ is

**Options:**

- **(A)** $\frac{1}{18}$
- **(B)** $\frac{1}{9}$
- **(C)** $\frac{2}{9}$
- **(D)** $\frac{1}{36}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{9}$**

**Detailed Solution:**

Sample space A dice is thrown thrice, $n(s)=6 \times 6 \times 6$.
Favorable events $\omega^{r_1}+\omega^{r_2}+\omega^{r_3}=0$ ie, $\left(r_1, r_2, r_3\right)$ are ordered 3-triples which can take values, $\left.\begin{array}{llll}(1,2,3), & (1,5,3), & (4,2,3), & (4,5,3) \\ (1,2,6), & (1,5,6), & (4,2,6), & (4,5,6)\end{array}\right\}$ ie, 8 ordered pairs and each can be arranged in 3 ! ways $=6$
$$
\begin{array}{ll}
\therefore & n(E)=8 \times 6 \\
\Rightarrow & P(E)=\frac{8 \times 6}{6 \times 6 \times 6}=\frac{2}{9}
\end{array}
$$

</details>

---

### Q10. JEE Advanced 2009 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

<strong>Paragraph:</strong>
A fair die is tossed repeatedly until a six is obtained. Let $X$ denotes the number of tosses required.<strong>Question:</strong>
The probability that $X \geq 3$ equals

**Options:**

- **(A)** $\frac{125}{216}$
- **(B)** $\frac{25}{36}$
- **(C)** $\frac{5}{36}$
- **(D)** $\frac{25}{216}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{25}{36}$**

**Detailed Solution:**

$P(X \geq 3)=\frac{5}{6} \cdot \frac{5}{6} \cdot 1=\frac{25}{36}$

</details>

---

### Q11. JEE Advanced 2009 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

<strong>Paragraph:</strong>
A fair die is tossed repeatedly until a six is obtained. Let $X$ denotes the number of tosses required.<strong>Question:</strong>
The probability that $X=3$ equals

**Options:**

- **(A)** $\frac{25}{216}$
- **(B)** $\frac{25}{36}$
- **(C)** $\frac{5}{36}$
- **(D)** $\frac{125}{216}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{25}{216}$**

**Detailed Solution:**

$P(X=3)=\frac{5}{6} \cdot \frac{5}{6} \cdot \frac{1}{6}=\frac{25}{216}$

</details>

---

### Q12. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `3`

<strong>Paragraph:</strong>
There are $n$ urns each containing $(n+1)$ balls such that the ith urn contains $i$ white balls and $(n+1-i)$ red balls. Let $u_i$ be the event of selecting ith urn, $i=1,2,3, \ldots, n$ and $W$ denotes the event of getting a white balls.<strong>Question:</strong>
If $P\left(u_i\right) \propto i$, where $i=1,2,3, \ldots, n$, then $\lim _{n \rightarrow \infty} P(W)$ is equal to

**Options:**

- **(A)** 1
- **(B)** $\frac{2}{3}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{3}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/P2FXcCfLyF2E7Scmlez396yBvjhkeK-dJUDHezmuJrc.original.fullsize.png">

</details>

---

