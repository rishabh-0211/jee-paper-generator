# JEE Main Mathematics - Definite Integration

## Topic 9: Definite as Limit of Sum

**Total Questions:** 18

---

### Q1. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>→</mo><mo>∞</mo></mrow></munder><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><msup><mi>n</mi><mn>3</mn></msup><mrow><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>k</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>(</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn><mo>)</mo><mi>π</mi></mrow><mn>24</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>13</mn><mi>π</mi></mrow><mrow><mn>8</mn><mo>(</mo><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn><mo>)</mo></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>13</mn><mo>(</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>3</mn><mo>)</mo><mi>π</mi></mrow><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mrow><mn>8</mn><mo>(</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn><mo>)</mo></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>13</mn><mi>π</mi></mrow><mrow><mn>8</mn><mo>(</mo><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn><mo>)</mo></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>→</mo><mo>∞</mo></mrow></munder><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><msup><mi>n</mi><mn>3</mn></msup><mrow><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>k</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>→</mo><mo>∞</mo></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><msup><mi>k</mi><mn>2</mn></msup><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mo>·</mo><mfrac><msup><mi>k</mi><mn>2</mn></msup><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced></mrow></mfrac></math></p><p>Now, using limit as a sum integral we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msubsup><mo>∫</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>3</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msubsup><mo>∫</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>1</mn><mfenced><mrow><msup><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mstyle></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><msqrt><mn>3</mn></msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msqrt><mn>3</mn></msqrt><mi>x</mi></mrow></mfenced><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msqrt><mn>3</mn></msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mn>3</mn></msqrt></mfenced><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><msqrt><mn>3</mn></msqrt><mo>·</mo><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac><mo>-</mo><mfrac><mi mathvariant="normal">π</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mi mathvariant="normal">π</mi><msqrt><mn>3</mn></msqrt></mfrac><mo>-</mo><mfrac><mi mathvariant="normal">π</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>13</mn><mi>π</mi></mrow><mrow><mn>8</mn><mo>·</mo><mo>(</mo><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>3</mn><mo>)</mo></mrow></mfrac></math></p>

</details>

---

### Q2. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Among</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced><mo>:</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><msup><mi>n</mi><mn>2</mn></msup></mfrac><mo>(</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>6</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>2</mn><mi>n</mi><mo>)</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced><mo>:</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><msup><mi>n</mi><mn>16</mn></msup></mfrac><mfenced><mrow><msup><mn>1</mn><mn>15</mn></msup><mo>+</mo><msup><mn>2</mn><mn>15</mn></msup><mo>+</mo><msup><mn>3</mn><mn>15</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>n</mi><mn>15</mn></msup></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>16</mn></mfrac></math></p>

**Options:**

- **(A)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are true
- **(B)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> is true
- **(C)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are false
- **(D)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are true**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>:</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><msup><mi>n</mi><mn>2</mn></msup></mfrac><mo>[</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>6</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>2</mn><mi>n</mi><mo>]</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mn>2</mn><mfrac><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>:</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><msup><mi>n</mi><mn>16</mn></msup></mfrac><mfenced><mrow><msup><mn>1</mn><mn>15</mn></msup><mo>+</mo><msup><mn>2</mn><mn>15</mn></msup><mo>+</mo><msup><mn>3</mn><mn>15</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>n</mi><mn>15</mn></msup></mrow></mfenced></math></p><p>This is limit of sum.</p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>f</mi><mfenced><mfrac><mi>r</mi><mi>n</mi></mfrac></mfenced><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>d</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msup><mi>r</mi><mi>k</mi></msup></mrow><msup><mi>n</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msup><mfenced><mstyle displaystyle="true"><mfrac><mi>r</mi><mi>n</mi></mfrac></mstyle></mfenced><mi>k</mi></msup></mrow><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>x</mi><mi>k</mi></msup><mo>d</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msup><mi>r</mi><mn>15</mn></msup></mrow><msup><mi>n</mi><mn>16</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mn>2</mn></math> are correct</p><p>Hence this is the required option.</p></blockquote>

</details>

---

### Q3. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>+</mo><mi>n</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>+</mo><mi>n</mi></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi></mrow></mfrac></mrow></mfenced></math>  is equal to :-</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>+</mo><mi>n</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>+</mo><mi>n</mi></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>n</mi></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfrac><mo>+</mo><mfrac><mn>3</mn><mrow><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mi>n</mi></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mo>&#160;</mo><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mi>r</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo><mo>&#160;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mn>1</mn><mi>n</mi></mfrac><mfenced><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mfrac><mi>r</mi><mi>n</mi></mfrac></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced open="[" close="]"><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>2</mn></mfenced></math></p>

</details>

---

### Q4. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>3</mn><mi>n</mi></mfrac><mfenced open="{" close="}"><mrow><mn>4</mn><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mn>2</mn><mi>n</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>3</mn><mi>n</mi></mfrac><mfenced close="]" open="["><mrow><mn>4</mn><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>2</mn></mstyle><mstyle displaystyle="true"><mi>n</mi></mstyle></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mi>n</mi></mstyle></mfrac></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>3</mn><mi>n</mi></mfrac><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mn>0</mn><mi>n</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>2</mn></mstyle><mstyle displaystyle="true"><mi>n</mi></mstyle></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mi>n</mi></mstyle></mfrac></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mn>3</mn><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><mfenced close="]" open="["><mrow><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mstyle displaystyle="true"><mi>r</mi></mstyle><mstyle displaystyle="true"><mi>n</mi></mstyle></mfrac></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mn>3</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><msubsup><mfenced close="]" open="["><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mn>27</mn><mo>-</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo>=</mo><mn>19</mn></math></p>

</details>

---

### Q5. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mrow><mn>2</mn><mi>n</mi></mrow><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></msqrt><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>, then:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt><mi>f</mi><mfenced><mfrac><mi>a</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mi>a</mi><mn>2</mn></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mi>a</mi><mn>2</mn></mfrac></mfenced><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mi>a</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mi>f</mi><mfenced><mfrac><mi>a</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mi>a</mi><mn>2</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mi>a</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mi>a</mi><mn>2</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mi>f</mi><mfenced><mfrac><mi>a</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mi>a</mi><mn>2</mn></mfrac></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mrow><mn>2</mn><mi>n</mi></mrow><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><msup><mfenced><mfrac><mi>k</mi><mi>n</mi></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>tan</mi><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mi>a</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mi>f</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>sec</mi><mn>2</mn></msup><mfenced><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mfenced><mo>=</mo><mfrac><msqrt><mn>2</mn></msqrt><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>f</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced></math></p></blockquote>

</details>

---

### Q6. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><mfrac><mn>3</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac></msqrt></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><msup><mn>2</mn><mi>n</mi></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>2</mn><mi>n</mi></msup></mfrac></msqrt></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><mfrac><mn>3</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac></msqrt></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><msup><mn>2</mn><mi>n</mi></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>2</mn><mi>n</mi></msup></mfrac></msqrt></mfrac></mrow></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>n</mi></msup><mo>=</mo><mi>t</mi></math> and if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#8594;</mo><mo>&#8734;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><mi>t</mi></mfrac><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></munderover><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><mfrac><mi>r</mi><mi>t</mi></mfrac></msqrt></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt></mfrac></math> (Using definite integral as limit of sum)</p><p>Applying <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mi>a</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msqrt><mi>x</mi></msqrt></mfrac><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mn>2</mn><msqrt><mi>x</mi></msqrt></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>=</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q7. JEE Main 2022 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi>l</mi><mi>i</mi><mi>m</mi></mrow><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>n</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mfenced open="[" close="]"><mrow><mo>(</mo><mi>n</mi><mi>k</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>+</mo><mo>(</mo><mi>n</mi><mi>k</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><mi>n</mi><mi>k</mi><mo>+</mo><mi>n</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>33</mn></math> . <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><msup><mi>n</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mo>&#183;</mo><mfenced close="]" open="["><mrow><msup><mn>1</mn><mi>k</mi></msup><mo>+</mo><msup><mn>2</mn><mi>k</mi></msup><mo>+</mo><msup><mn>3</mn><mi>k</mi></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>n</mi><mi>k</mi></msup></mrow></mfenced></math>, then the integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi>l</mi><mi>i</mi><mi>m</mi></mrow><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>n</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mfenced close="]" open="["><mrow><mo>(</mo><mi>n</mi><mi>k</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>+</mo><mo>(</mo><mi>n</mi><mi>k</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><mi>n</mi><mi>k</mi><mo>+</mo><mi>n</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>33</mn></math></p><p>Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHS</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>n</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mfenced close="]" open="["><mrow><mi>n</mi><mi>k</mi><mo>&#183;</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>n</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mrow></mrow><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msup></msup><msup><mi>n</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mo>&#183;</mo><mfenced close="]" open="["><mrow><msup><mi>n</mi><mn>2</mn></msup><mi>k</mi><mo>+</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>&#183;</mo><msup><mi>n</mi><mn>2</mn></msup><mfenced><mrow><mi>k</mi><mo>+</mo><mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mn>2</mn></mfrac></mrow></mfenced></mrow><msup><mi>n</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mfenced><mrow><mi>k</mi><mo>+</mo><mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mi>k</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>RHS</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>33</mn><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><msup><mi>n</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mfenced><mrow><msup><mn>1</mn><mi>k</mi></msup><mo>+</mo><msup><mn>2</mn><mi>k</mi></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>n</mi><mi>k</mi></msup></mrow></mfenced><mo>=</mo><mn>33</mn><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mn>1</mn><mi>n</mi></mfrac><msup><mfenced><mfrac><mi>k</mi><mi>n</mi></mfrac></mfenced><mi>k</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>33</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>x</mi><mi>k</mi></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>33</mn><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>Now given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHS</mi><mo>=</mo><mi>RHS</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mn>33</mn><mo>&#183;</mo><mfrac><mn>1</mn><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>66</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>k</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>k</mi><mo>+</mo><mn>13</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=5</mo></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>13</mn><mn>2</mn></mfrac></math></p><p>So, integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q8. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mfrac><msup><mi>n</mi><mn>2</mn></msup><mrow><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><msup><mi>n</mi><mn>2</mn></msup><mrow><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><msup><mi>n</mi><mn>2</mn></msup><mrow><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><msup><mi>n</mi><mn>2</mn></msup><mrow><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mi>n</mi></mrow></mfenced></mrow></mfrac></mrow></mfenced></math>
is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>ln</mi><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mi>ln</mi><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mi>ln</mi><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>+</mo><mi>ln</mi><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>ln</mi><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mfrac><mn>1</mn><mi>n</mi></mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><msup><mi>r</mi><mn>2</mn></msup><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi>r</mi><mi>n</mi></mfrac></mrow></mfenced></mrow></mfrac><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>tan</mi><mi>&#952;</mi><mo>,</mo><mi>d</mi><mi>x</mi><mo>=</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mfrac><mrow><mi>d</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mfrac><mrow><mn>2</mn><mi>cos</mi><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi></mrow><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mfrac><mrow><mfenced><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mi>d</mi><mi>&#952;</mi></mrow><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo stretchy="true">&#8747;</mo><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></munderover><mfrac><mrow><mfenced><mrow><mi>cos</mi><mi>&#952;</mi><mo>&#8722;</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mi>d</mi><mi>&#952;</mi></mrow><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfenced></mrow></mfenced><mn>0</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></msubsup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>ln</mi><mn>2</mn></math></p>

</details>

---

### Q9. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>U</mi><mi>n</mi></msub><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><msup><mn>2</mn><mn>2</mn></msup><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>2</mn></msup><mo>&#8230;</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><msup><mi>n</mi><mn>2</mn></msup><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>n</mi></msup><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mfenced><msub><mi>U</mi><mi>n</mi></msub></mfenced><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><msup><mi>e</mi><mn>2</mn></msup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mi>e</mi></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><msup><mi>e</mi><mn>2</mn></msup></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>16</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>16</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>U</mi><mi>n</mi></msub><mo>=</mo><munderover><mo>&#8719;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><msup><mi>r</mi><mn>2</mn></msup><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mfenced><msub><mi>U</mi><mi>n</mi></msub></mfenced><mfrac bevelled="true"><mrow><mo>-</mo><mn>4</mn></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mo>&#160;</mo><mi>log</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><msup><mi>r</mi><mn>2</mn></msup><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mo>&#160;</mo><mi>L</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mo>&#160;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mn>4</mn><mi>r</mi></mrow><mi>n</mi></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>&#160;</mo><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><msup><mi>r</mi><mn>2</mn></msup><msup><mi>n</mi><mn>2</mn></msup></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mo>&#160;</mo><mi>L</mi><mo>=</mo><mo>-</mo><mn>4</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>x</mi><mo>&#160;</mo><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>d</mo><mi>x</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>log</mi><mo>&#160;</mo><mfenced><mi>t</mi></mfenced><mo>d</mo><mi>t</mi><mo>=</mo><mo>-</mo><mn>2</mn><msubsup><mfenced open="[" close="]"><mrow><mi>t</mi><mo>&#160;</mo><mi>log</mi><mo>&#160;</mo><mi>t</mi><mo>-</mo><mi>t</mi></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>log</mi><mo>&#160;</mo><mi>L</mi><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>log</mi><mo>&#160;</mo><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>L</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>log</mi><mo>&#160;</mo><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mfenced><mrow><mi>log</mi><mo>&#160;</mo><mfrac><mn>4</mn><mi>e</mi></mfrac></mrow></mfenced></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>log</mi><msup><mfenced><mfrac><mn>4</mn><mi>e</mi></mfrac></mfenced><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mo>&#160;</mo><msup><mfenced><mfrac><mi>e</mi><mn>4</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>16</mn></mfrac></math></p>

</details>

---

### Q10. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mfrac><msup><mi>n</mi><mn>2</mn></msup><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></math> is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>2</mn></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>4</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>4</mn></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mn>4</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>4</mn></mfenced></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mfenced><mfrac><msup><mi>n</mi><mn>2</mn></msup><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mfenced><mfrac><msup><mi>n</mi><mn>2</mn></msup><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mfenced><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mfenced><mstyle displaystyle="true"><mfrac><mi>r</mi><mi>n</mi></mfrac></mstyle></mfenced><mn>2</mn></msup></mrow></mfrac></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mi>n</mi></mfrac><mo>=</mo><mi>x</mi></math>, lower limit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>0</mn></math> and upper limit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfrac><mn>1</mn><mrow><msup><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#215;</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>2</mn><mi>x</mi></mrow></mfenced><mn>0</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mn>4</mn><mo>)</mo></math></p>

</details>

---

### Q11. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>j</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>8</mn><mi>n</mi></mrow><mrow><mfenced><mrow><mn>2</mn><mi>j</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>4</mn><mi>n</mi></mrow></mfrac></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mfenced><mrow><mfrac><mrow><mn>2</mn><mi>j</mi></mrow><mi>n</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>+</mo><mn>8</mn></mrow></mfenced><mfenced><mrow><mfrac><mrow><mn>2</mn><mi>j</mi></mrow><mi>n</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>+</mo><mn>4</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>8</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mn>4</mn><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>4</mn><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi mathvariant="script">l</mi><mi>n</mi><mfenced open="|" close="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mrow></mfenced><msubsup><mo>|</mo><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>&#8467;</mi><mi>n</mi><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></math></p>

</details>

---

### Q12. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><mfenced open="[" close="]"><mrow><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>5</mn><mi>n</mi></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>10</mn><mi>n</mi></mfrac></mfenced><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>f</mi><mfenced><mfrac><mrow><mn>5</mn><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mi>n</mi></mfrac></mfenced></mrow></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><mfenced close="]" open="["><mrow><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>5</mn><mi>n</mi></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>10</mn><mi>n</mi></mfrac></mfenced><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>f</mi><mfenced><mfrac><mrow><mn>5</mn><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mi>n</mi></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mi>f</mi><mfenced><mfrac><mrow><mn>5</mn><mi>r</mi></mrow><mi>n</mi></mfrac></mfenced><mfrac><mn>1</mn><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mfenced><mrow><mn>5</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>=</mo><mfrac><mn>7</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q13. JEE Main 2021 (16 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi mathvariant="normal">x</mi></mrow><mn>4</mn></mfrac></mfenced></mrow></mfenced></math>.</p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>2</mn><mi>n</mi></mfrac><mfenced><mrow><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>n</mi></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2</mn><mi>n</mi></mfrac></mfenced><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced></math> is equal to ________.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi mathvariant="normal">x</mi></mrow><mn>4</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mi mathvariant="normal">x</mi></mrow><mn>4</mn></mfrac></mfenced></mrow></mfenced></mrow><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mn>2</mn><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mn>1</mn><mi>n</mi></mfrac><mi>f</mi><mfenced><mfrac><mi>r</mi><mi>n</mi></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mn>2</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>4</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math></p><p>Replacing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mn>1</mn><mo>-</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mn>2</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mn>2</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mn>2</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>x</mi></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mn>2</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>4</mn></mfrac></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mn>2</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math>    <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>ii</mi><mo>)</mo></math></p><p>Adding an equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>(</mo><mi>ii</mi><mo>)</mo></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q14. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>+</mo><mfrac><mi>n</mi><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mi>n</mi><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mi>n</mi><msup><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>+</mo><mfrac><mi>n</mi><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mi>n</mi><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mi>n</mi><msup><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mfrac><mi>n</mi><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mi>r</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>n</mi><mi>r</mi><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mfrac><mn>1</mn><mrow><msup><mfenced><mrow><mi>r</mi><mo>/</mo><mi>n</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mi>r</mi><mo>/</mo><mi>n</mi></mrow></mfenced><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><msubsup><mfenced close="]" open="["><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q15. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>n</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow><mrow><msup><mrow><mi>n</mi></mrow><mrow><mn>4</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mo>(</mo><mi>n</mi><mo>+</mo><mn>2</mn><mo>)</mo></mrow><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow><mrow><msup><mrow><mi>n</mi></mrow><mrow><mn>4</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mrow><msup><mrow><mo>(</mo><mn>2</mn><mi>n</mi><mo>)</mo></mrow><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow><mrow><msup><mrow><mi>n</mi></mrow><mrow><mn>4</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><msup><mrow><mo>(</mo><mn>2</mn><mo>)</mo></mrow><mrow><mn>4</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msup><mrow><mo>(</mo><mn>2</mn><mo>)</mo></mrow><mrow><mn>3</mn><mo>/</mo><mn>4</mn></mrow></msup></math>
- **(C)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msup><mrow><mo>(</mo><mn>2</mn><mo>)</mo></mrow><mrow><mn>4</mn><mo>/</mo><mn>3</mn></mrow></msup></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><msup><mrow><mo>(</mo><mn>2</mn><mo>)</mo></mrow><mrow><mn>4</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><msup><mrow><mo>(</mo><mn>2</mn><mo>)</mo></mrow><mrow><mn>4</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

The given limit can be written as
<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>n</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><mfenced close="]" open="[" separators="|"><mrow><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mi>n</mi></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mi>n</mi><mi>n</mi></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>n</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mi>r</mi><mi>n</mi></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></math>
<math><mo>=</mo><mrow><munderover><mo stretchy="true">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></munderover><mrow><msup><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mi>d</mi><mi>x</mi></mrow></mrow></math>
<math><msubsup><mrow><mfenced close="|" open="" separators="|"><mrow><mo>=</mo><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></mrow><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mn>1</mn></mrow></msubsup></math>
<math><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>(</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>4</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>&#8211;</mo><mn>1</mn><mo>)</mo></math>
<math><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><msup><mrow><mo>.</mo><mn>2</mn></mrow><mrow><mn>4</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

</details>

---

### Q16. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced separators="|"><mrow><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mi>&#160;</mi><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><mrow><mn>5</mn><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced><mn>2</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mrow><mo>(</mo><mn>3</mn><mo>)</mo></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced><mn>2</mn></mfenced></math>**

**Detailed Solution:**

<p>To find,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>n</mi></mrow></msubsup><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><msubsup><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>n</mi></mrow></msubsup><msubsup><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mfenced separators="|"><mfrac><mi>r</mi><mi>n</mi></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac><mi>&#160;</mi><mi>&#160;</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mfenced close="]" open="[" separators="|"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mi>x</mi></mrow></mfenced><mn>0</mn><mn>2</mn></msubsup></math></p><p><math><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>2</mn></mrow></mrow></math>.</p>

</details>

---

### Q17. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><mo>&#8289;</mo><mfenced><mfrac><mrow><msup><mn>1</mn><mi>a</mi></msup><mo>+</mo><msup><mn>2</mn><mi>a</mi></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>n</mi><mi>a</mi></msup></mrow><mrow><msup><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mi>n</mi><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>n</mi><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfenced separators="|"><mrow><mi>n</mi><mi>a</mi><mo>+</mo><mi>n</mi></mrow></mfenced></mrow></mfenced></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac><mi>&#160;</mi></math> for some positive real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>17</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mn>7</mn></math>
- **(D)** <math><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>7</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><mfrac><mrow><msup><mi>n</mi><mi>a</mi></msup><mrow><mo>(</mo><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mrow><mo>(</mo><mfrac><mi>r</mi><mi>n</mi></mfrac><mo>)</mo></mrow><mi>a</mi></msup></mstyle><mo>)</mo></mrow></mrow><mrow><msup><mrow><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mi>a</mi><mo>&#8722;</mo><mn>1</mn></mrow></msup><mo>.</mo><msup><mi>n</mi><mn>2</mn></msup><mrow><mo>(</mo><mi>a</mi><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow><mn>2</mn></mfrac><mo>)</mo></mrow></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><msup><mi>n</mi><mi>a</mi></msup><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow></mrow></munderover></mstyle><msup><mfenced><mstyle displaystyle="true"><mfrac><mi>r</mi><mi>n</mi></mfrac></mstyle></mfenced><mi>a</mi></msup></mrow><mrow><msup><mfenced><mi>n</mi></mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></mrow></mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>a</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></mrow><mn>2</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mi>&#8734;</mi></mrow></munder><mfrac><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mrow><mo>(</mo><mfrac><mi>r</mi><mi>n</mi></mfrac><mo>)</mo></mrow><mi>a</mi></msup></mstyle><mrow><msup><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>)</mo></mrow><mrow><mi>a</mi><mo>-1</mo></mrow></msup><mstyle displaystyle="true"><mfenced><mrow><mi>a</mi><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></mrow><mn>2</mn></mfrac></mrow></mfenced></mstyle></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><munderover><mo>&#8747;</mo><mn>0</mn><mn>1</mn></munderover><msup><mi>x</mi><mi>a</mi></msup><mi>d</mi><mi>x</mi></mstyle><mrow><mo>(</mo><mi>a</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow><mrow><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>60</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>120</mn></math>

<math><mo>&#8658;</mo><mn>2</mn><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>3</mn><mi>a</mi><mo>-</mo><mn>119</mn><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mn>2</mn><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>17</mn><mi>a</mi><mo>-</mo><mn>14</mn><mi>a</mi><mo>-</mo><mn>119</mn><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mi>a</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>17</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mi>a</mi><mo>=</mo><mn>7</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mfrac><mrow><mn>17</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>.</p>

</details>

---

### Q18. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $x=\int_0^y \frac{d t}{\sqrt{1+t^2}}$, then $\frac{d^2 y}{d x^2}$ is equal to :

**Options:**

- **(A)** $y$
- **(B)** $\sqrt{1+y^2}$
- **(C)** $\frac{x}{\sqrt{1+y^2}}$
- **(D)** $y^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $y$**

**Detailed Solution:**

$x=\int_0^y \frac{d t}{\sqrt{1+t^2}}$
$\Rightarrow 1=\frac{1}{\sqrt{1+y^2}} \cdot \frac{d y}{d x}$
$\left[\because\right.$ If $\mathrm{I}(x)=\int_{\phi(x)}^{\psi(x)} f(t) d t$, then $\frac{d \mathrm{I}(x)}{d x}=f\{\psi(x)\}$
$\frac{\mathrm{dy}}{\mathrm{dx}}=\sqrt{1-\mathrm{y}^2}$
$\frac{d^2 y}{d x^2}=\frac{1}{2 \sqrt{1+y^2}} \cdot 2 y \cdot \frac{d y}{d x}=\frac{y}{\sqrt{1+y^2}} \cdot \sqrt{1+y^2}=y$

</details>

---

