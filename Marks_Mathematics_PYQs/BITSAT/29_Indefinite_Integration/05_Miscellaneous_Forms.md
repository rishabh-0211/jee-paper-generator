# BITSAT Mathematics - Indefinite Integration

## Topic 5: Miscellaneous Forms

**Total Questions:** 4

---

### Q1. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=\int \frac{x^2 d x}{\left(1+x^2\right)\left(1+\sqrt{\left.1+x^2\right)}\right.}$ and $f(0)=0$, 
then the value of $f(1)$ be

**Options:**

- **(A)** $\log (1+\sqrt{2})$
- **(B)** $\log (1+\sqrt{2})-\frac{\pi}{4}$
- **(C)** $\log (1+\sqrt{2})+\frac{\pi}{2}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log (1+\sqrt{2})-\frac{\pi}{4}$**

**Detailed Solution:**

$f(x)=\int \frac{x^2 d x}{\left(1+x^2\right)\left(1+\sqrt{1+x^2}\right)}$
Let $x=\tan \theta$
$\Rightarrow \quad d x=\sec ^2 \theta d \theta=\left(1+x^2\right) d \theta$
$f(x)=\int \frac{x^2 d x}{\left(1+x^2\right)\left(1+\sqrt{1+x^2}\right)}$
$=\int \frac{\tan ^2 \theta \sec ^2 \theta d \theta}{\sec ^2 \theta(1+\sec \theta)}=\int \frac{\tan ^2 \theta d \theta}{1+\sec \theta}$
$=\int \frac{\sin ^2 \theta d \theta}{\cos \theta(1+\cos \theta)}$
$=\int \frac{1-\cos ^2 \theta d \theta}{\cos \theta(1+\cos \theta)}$
$=\int \frac{(1-\cos \theta) d \theta}{\cos \theta}$
$=\int \sec \theta d \theta-\int d \theta$
$=\log \left(x+\sqrt{1+x^2}\right)-\tan ^{-1} x+C$
$\therefore \quad f(0)=\log (0+\sqrt{1+0})-\tan ^{-1}(0)+C$
$0=\log 1-0+C$
$\Rightarrow \quad C=0$
$\therefore \quad f(1)=\log \left(1+\sqrt{1+1^2}\right)-\tan ^{-1}(1)$
$=\log (1+\sqrt{2})-\frac{\pi}{4}$

</details>

---

### Q2. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \frac{1}{\left[(x-1)^3(x+2)^5\right]^{\frac{1}{4}}} d x$, is

**Options:**

- **(A)** $\frac{4}{3}\left(\frac{x+1}{x-2}\right)^{\frac{1}{4}}+C$
- **(B)** $\frac{3}{4}\left(\frac{x-1}{x+2}\right)^{\frac{1}{4}}+C$
- **(C)** $\frac{4}{3}\left(\frac{x-1}{x+2}\right)^{\frac{1}{4}}+C$
- **(D)** $\frac{1}{3}\left(\frac{2 x-1}{4 x-3}\right)^{\frac{1}{4}}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4}{3}\left(\frac{x-1}{x+2}\right)^{\frac{1}{4}}+C$**

**Detailed Solution:**

$I=\int \frac{1}{\left(\frac{x-1}{x+2}\right)^{3 / 4}(x+2)^2} d x$
Let $\frac{x-1}{x+2}=t \Rightarrow \frac{3 d x}{(x+2)^2}=d t$
$$
\begin{aligned}
\Rightarrow \quad I & =\frac{1}{3} \int \frac{1}{t^{3 / 4}} d t=\frac{1}{3}\left(\frac{t^{1 / 4}}{1 / 4}\right)+C \\
& =\frac{4}{3} t^{1 / 4}+C=\frac{4}{3}\left(\frac{x-1}{x+2}\right)^{1 / 4}+C
\end{aligned}
$$

</details>

---

### Q3. BITSAT 2018

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>8</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>4</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn><mi>x</mi></mrow></msup></mrow></mfrac><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>8</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>4</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>P</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>2</mn><mi>Q</mi><mfenced><mi>x</mi></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>A</mi><mfenced><mfrac><mrow><mi>B</mi><mo>+</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mi>C</mi></mfrac></mfenced><mo>+</mo><mi>K</mi><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>,</mo><mn>2</mn><mo>,</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>,</mo><msup><mi>e</mi><mi>x</mi></msup><mo>,</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><msup><mi>e</mi><mi>x</mi></msup></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>,</mo><mfrac><mn>1</mn><msup><mi>e</mi><mi>x</mi></msup></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>,</mo><msup><mi>e</mi><mi>x</mi></msup><mo>,</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>8</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>4</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn><mi>x</mi></mrow></msup></mrow></mfrac><mo>-</mo><mn>2</mn><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>8</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>4</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>R</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>8</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>4</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>8</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>t</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>t</mi></mrow><mrow><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mn>2</mn><msup><mi>t</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>t</mi><mo>+</mo><mn>2</mn><msup><mi>t</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mi>K</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>R</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mi>K</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>,</mo><msup><mi>e</mi><mi>x</mi></msup><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Option (b) is correct.</p>

</details>

---

### Q4. BITSAT 2017

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mo>(</mo><msqrt><mi>x</mi></msqrt><msup><mo>)</mo><mn>5</mn></msup><mi>d</mi><mi>x</mi></mrow><mrow><mo>(</mo><msqrt><mi>x</mi></msqrt><msup><mo>)</mo><mn>7</mn></msup><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfrac><mo>=</mo><mi>&#955;</mi><mi>log</mi><mfenced><mfrac><msup><mi>x</mi><mn>9</mn></msup><mrow><msup><mi>x</mi><mn>9</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>&#955;</mi></math> equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#62;</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#60;</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#62;</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#62;</mo><mn>2</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mfenced><msqrt><mi>x</mi></msqrt></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><msqrt><mi>x</mi></msqrt></mfenced><mn>7</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mfenced><msqrt><mi>x</mi></msqrt></mfenced><mn>7</mn></msup><mfenced><mrow><mfrac><mn>1</mn><mrow><mo>(</mo><msqrt><mi>x</mi></msqrt><msup><mo>)</mo><mn>5</mn></msup></mrow></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mfenced><msqrt><mi>x</mi></msqrt></mfenced><mn>5</mn></msup></mfrac><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mrow><mo>(</mo><msqrt><mi>x</mi></msqrt><msup><mo>)</mo><mn>7</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mi>t</mi></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>5</mn></mfrac><mi>log</mi><mi>t</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>5</mn></mfrac><mi>log</mi><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mfenced><msqrt><mi>x</mi></msqrt></mfenced><mn>5</mn></msup></mfrac></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>log</mi><mfenced><mfrac><mrow><msup><mi>x</mi><mrow><mn>5</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow><msup><mi>x</mi><mrow><mn>5</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>5</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>a</mi><mo>+</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn><mo>.</mo><mn>1</mn><mo>&#62;</mo><mn>2</mn></math></p>

</details>

---

