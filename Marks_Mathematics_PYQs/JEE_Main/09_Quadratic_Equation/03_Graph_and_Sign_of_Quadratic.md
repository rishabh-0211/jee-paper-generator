# JEE Main Mathematics - Quadratic Equation

## Topic 3: Graph and Sign of Quadratic

**Total Questions:** 6

---

### Q1. JEE Main 2026 (02 April Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $a, b, c \in \{1, 2, 3, 4\}$. If the probability, that $ax^2 + 2\sqrt{2}\,bx + c > 0$ for all $x \in \mathbb{R}$, is $\dfrac{m}{n}$, $\gcd(m, n) = 1$, then $m + n$ is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **81**

**Detailed Solution:**

For the quadratic expression $ax^2 + 2\sqrt{2}bx + c > 0$ for all $x \in \mathbb{R}$, the leading coefficient must be positive and the discriminant must be negative.

Since $a \in \{1, 2, 3, 4\}$, the condition $a > 0$ is always satisfied.

The discriminant condition is:
$D < 0$
$\Rightarrow (2\sqrt{2}b)^2 - 4ac < 0$
$\Rightarrow 8b^2 - 4ac < 0$
$\Rightarrow 2b^2 < ac$

The total number of possible triplets $(a, b, c)$ is $4 \times 4 \times 4 = 64$.

Now, we find the number of favorable outcomes by checking the possible values of $b \in \{1, 2, 3, 4\}$:

Case 1: $b = 1$
We need $2(1)^2 < ac \Rightarrow ac > 2$.
The total number of pairs $(a, c)$ is $4 \times 4 = 16$.
The pairs for which $ac \le 2$ are $(1, 1), (1, 2), (2, 1)$, which are $3$ in number.
So, the number of pairs with $ac > 2$ is $16 - 3 = 13$.

Case 2: $b = 2$
We need $2(2)^2 < ac \Rightarrow ac > 8$.
The possible pairs $(a, c)$ from the given set are $(3, 3), (3, 4), (4, 3), (4, 4)$.
So, there are $4$ pairs.

Case 3: $b = 3$
We need $2(3)^2 < ac \Rightarrow ac > 18$.
Since the maximum possible value of $ac$ is $4 \times 4 = 16$, there are $0$ pairs.

Case 4: $b = 4$
We need $2(4)^2 < ac \Rightarrow ac > 32$.
Again, there are $0$ pairs.

Total number of favorable outcomes = $13 + 4 = 17$.

The required probability is $\dfrac{m}{n} = \dfrac{17}{64}$.

Since $\gcd(17, 64) = 1$, we have $m = 17$ and $n = 64$.

Therefore, $m + n = 17 + 64 = 81$.

Answer: $81$

</details>

---

### Q2. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of positive integral values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mn>9</mn><mi>a</mi><mo>+</mo><mn>4</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>32</mn></mrow></mfrac><mo>&lt;</mo><mn>0</mn><mo>,</mo><mo> </mo><mo>∀</mo><mi>x</mi><mo>∈</mo><mi mathvariant="normal">ℝ</mi></math>. Then, the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∞</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Given:</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>(</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo>)</mo><mi>x</mi><mo>+</mo><mn>9</mn><mi>a</mi><mo>+</mo><mn>4</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>32</mn></mrow></mfrac><mo>&lt;</mo><mn>0</mn><mo> </mo><mo> </mo><mo>∀</mo><mi>x</mi><mo>∈</mo><mi>R</mi></math></p><p>For quadratic <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>32</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mo> </mo><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>8</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mfenced><mn>32</mn></mfenced><mo>=</mo><mo>-</mo><mn>64</mn></math></p><p>Since the discriminant is less than zero and the leading coefficient is positive, this quadratic will always be positive.</p><p>Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>(</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo>)</mo><mi>x</mi><mo>+</mo><mn>9</mn><mi>a</mi><mo>+</mo><mn>4</mn><mo>&lt;</mo><mn>0</mn></math></p><p>We know that, for a quadratic to be always negative, the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>&lt;</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>D</mi><mo>&lt;</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>&lt;</mo><mn>0</mn></math> </p><p>But we want positive values.</p><p>So, no positive integral value exist.</p>

</details>

---

### Q3. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability of selecting integers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mn>5</mn><mo>,</mo><mn>30</mn></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>5</mn><mi>a</mi><mo>+</mo><mn>64</mn><mo>&#62;</mo><mn>0</mn></math>, for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>, is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>36</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>9</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>9</mn></mfrac></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>5</mn><mi>a</mi><mo>+</mo><mn>64</mn><mo>&#62;</mo><mn>0</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msup><mi>B</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>A</mi><mi>C</mi><mo>&#60;</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>B</mi><mi>x</mi><mo>+</mo><mi>C</mi><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>.</p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>4</mn><msup><mfenced><mrow><mi mathvariant="normal">a</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mfenced><mrow><mo>-</mo><mn>5</mn><mi>a</mi><mo>+</mo><mn>64</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><mo>+</mo><mn>8</mn><mi>a</mi><mo>+</mo><mn>5</mn><mi>a</mi><mo>-</mo><mn>64</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>13</mn><mi>a</mi><mo>-</mo><mn>48</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>16</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>a</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>16</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Possible values for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo>-</mo><mn>15</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>14</mn><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>,</mo><mn>2</mn></mrow></mfenced></math> containing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math> integers.</p><p>But given range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mn>5</mn><mo>,</mo><mn>30</mn></mrow></mfenced></math>, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> would take values <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo>-</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>, containing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> integers.</p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>30</mn></mrow></mfenced></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math> numbers.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Required probability</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>8</mn><mn>36</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac></math></p>

</details>

---

### Q4. JEE Main 2021 (25 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>,</mo></math> for which the inequality <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mrow><mn>3</mn><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mn>8</mn><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mo>&#62;</mo><mn>0</mn></math> is valid for every <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mrow><mn>3</mn><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mn>8</mn><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mo>&#62;</mo><mn>0</mn></math><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>4</mn><msup><mfenced><mrow><mn>3</mn><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mfenced><mrow><mn>8</mn><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>9</mn><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>k</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>8</mn><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>k</mi><mo>+</mo><mn>8</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfenced><mrow><mi>k</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>k</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>k</mi><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q5. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of integral values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> for which the quadratic expression <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>m</mi></mrow></mfenced><mi>&#160;</mi><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>m</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mn>4</mn><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>m</mi></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> is always positive, is

**Options:**

- **(A)** <math><mn>7</mn></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><mn>6</mn></math>
- **(D)** <math><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>7</mn></math>**

**Detailed Solution:**

<p><math><mo>&#8757;</mo></math> Quadratic expression is positive, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mi>m</mi><mo>&#62;</mo><mn>0</mn></math> and <math><mi>D</mi><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>&#62;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math> and</p><p><math><mn>4</mn><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>m</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>16</mn><mi>&#160;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>m</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>m</mi></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mn>9</mn><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn><mo>+</mo><mn>6</mn><mi>m</mi><mo>-</mo><mn>4</mn><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>3</mn><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>6</mn><mi>m</mi><mo>-</mo><mn>3</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>m</mi><mo>-</mo><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced><mfenced separators="|"><mrow><mi>m</mi><mo>-</mo><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>&#8712;</mo><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>,</mo><mi>&#160;</mi><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced></math></p><p><math><mo>&#8756;</mo><mi>m</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn><mo>,</mo><mi>&#160;</mi><mn>6</mn></math></p><p><math><mo>&#8756;</mo></math> Number of integral values <math><mo>=</mo><mn>7</mn></math></p>

</details>

---

### Q6. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The sum of all the real values of <math><mi>x</mi></math> Satisfying the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>50</mn></mrow></mfenced></mrow></msup><mo>=</mo><mn>1</mn></math> is:

**Options:**

- **(A)** <math><mn>16</mn></math>
- **(B)** <math><mo>-</mo><mn>5</mn></math>
- **(C)** <math><mo>-</mo><mn>4</mn></math>
- **(D)** <math><mn>14</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>-</mo><mn>4</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>50</mn></mrow></mfenced></mrow></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>50</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><msup><mn>2</mn><mn>0</mn></msup><mo>=</mo><mn>1</mn></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>10</mn></math>

Sum of the real value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>5</mn><mo>-</mo><mn>10</mn><mo>=</mo><mo>-</mo><mn>4</mn></math></p>

</details>

---

