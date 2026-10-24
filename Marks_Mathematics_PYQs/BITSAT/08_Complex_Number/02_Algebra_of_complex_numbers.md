# BITSAT Mathematics - Complex Number

## Topic 2: Algebra of complex numbers

**Total Questions:** 8

---

### Q1. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `2`

The smallest positive integral value of $n$ such that 
$\left[\frac{1+\sin \frac{\pi}{8}+i \cos \frac{\pi}{8}}{1+\sin \frac{\pi}{8}-i \cos \frac{\pi}{8}}\right]^n$ is purely imaginary, is equal to

**Options:**

- **(A)** $4$
- **(B)** $3$
- **(C)** $2$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4$**

**Detailed Solution:**

$\left[\frac{1+\sin \frac{\pi}{8}+i \cos \frac{\pi}{8}}{1+\sin \frac{\pi}{8}-i \cos \frac{\pi}{8}}\right]^n=\left[\frac{1+\cos \alpha+i \sin \alpha}{1+\cos \alpha-i \sin \alpha}\right]^n$
$\left[\because \alpha=\frac{\pi}{2}-\frac{\pi}{8}\right]$
$=\left[\frac{2 \cos ^2 \frac{\alpha}{2}+2 i \sin \frac{\alpha}{2} \cos \frac{\alpha}{2}}{2 \cos ^2 \frac{\alpha}{2}-2 i \sin \frac{\alpha}{2} \cos \frac{\alpha}{2}}\right]^n$
$=\left[\frac{\cos \frac{\alpha}{2}+i \sin \frac{\alpha}{2}}{\cos \frac{\alpha}{2}-i \sin \frac{\alpha}{2}}\right]_{-}^n=\left(e^{2 i \frac{\alpha}{2}}\right]^n=e^{i n \alpha}$
$=e^{i n\left(\frac{3 \pi}{8}\right)}=\cos \frac{3 n \pi}{8}+i \sin \frac{3 n \pi}{8}$
For $n=4$ we get imaginary part.

</details>

---

### Q2. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `3`

If $|w|=2$, then the set of points $z=w-\frac{1}{w}$ is contained in or equal to the set of points $z$ satisfying

**Options:**

- **(A)** $\operatorname{Im}(z)=0$
- **(B)** $|\operatorname{Im}(z)| \leq 1$
- **(C)** $|\operatorname{Re}(z)| \leq 2$
- **(D)** $|z| \leq 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $|z| \leq 3$**

**Detailed Solution:**

We have, $|w|=2 \Rightarrow w=2(\cos \theta+i \sin \theta)$
$\therefore \quad z=w-\frac{1}{w}$
$=2(\cos \theta+i \sin \theta)-\frac{1}{2}(\cos \theta-i \sin \theta)$
$\Rightarrow \quad z=\frac{3}{2} \cos \theta+\frac{5}{2} i \sin \theta$
$\Rightarrow \quad|z|=\sqrt{\frac{9}{4}+\frac{25}{4}}=\frac{\sqrt{17}}{2} < 3$
Hence, option (d) is correct.

</details>

---

### Q3. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `3`

If $z$ is a complex number such that $z^{2}=(\bar{z})^{2}$, then

**Options:**

- **(A)** $z$ is purely real
- **(B)** $z$ is purely imaginary
- **(C)** either $z$ is purely real or purely imaginary
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) either $z$ is purely real or purely imaginary**

**Detailed Solution:**

Let $z=x+i y$, then its conjugate $\bar{z}=x-i y$

Given that $z^{2}=(\bar{z})^{2}$

$\begin{array}{l}

\Rightarrow x^{2}-y^{2}+2 i x y=x^{2}-y^{2}-2 i x y \\

\Rightarrow 4 i x y=0

\end{array}$

</details>

---

### Q4. BITSAT 2019

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>z</mi><mo>&#175;</mo></mover><mn>1</mn></msub></math> represents adjacent vertices of a regular polygon of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> sides and if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>I</mi><mi>m</mi><mfenced><msub><mi>z</mi><mn>1</mn></msub></mfenced></mrow><mrow><mi>R</mi><mi>e</mi><mfenced><msub><mi>z</mi><mn>1</mn></msub></mfenced></mrow></mfrac><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><mi>r</mi><msup><mi>e</mi><mrow><mi>i</mi><mi>&#952;</mi></mrow></msup></math></p><p>then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>z</mi><mo>&#175;</mo></mover><mn>1</mn></msub><mo>=</mo><mi>r</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>i</mi><mi>&#952;</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>z</mi><mn>1</mn></msub><msub><mover><mi>z</mi><mo>&#175;</mo></mover><mn>1</mn></msub></mfrac><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>i</mi><mi>&#952;</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>&#960;</mi><mi>i</mi><mo>/</mo><mi>n</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mi>n</mi></mfrac></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>I</mi><mi>m</mi></msub><mfenced><msub><mi>z</mi><mn>1</mn></msub></mfenced></mrow><mrow><msub><mi>R</mi><mi>e</mi></msub><mfenced><msub><mi>z</mi><mn>1</mn></msub></mfenced></mrow></mfrac><mo>=</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mi>tan</mi><mfrac><mi>&#960;</mi><mi>n</mi></mfrac><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>tan</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q5. BITSAT 2016

*Type:* `singleCorrect` | *Level:* `2`

If $z_{1}=\sqrt{3}+i \sqrt{3}$ and $z_{2}=\sqrt{3}+i$, then the

complex number $\left(\frac{\mathrm{z}_{1}}{\mathrm{z}_{2}}\right)^{50}$ lies in the :

**Options:**

- **(A)** first quadrant
- **(B)** second quadrant
- **(C)** third quadrant
- **(D)** fourth quadrant

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) first quadrant**

**Detailed Solution:**

$\left(\frac{z_{1}}{z_{2}}\right)^{50}=\left(\frac{\sqrt{3}+i \sqrt{3}}{\sqrt{3}+i}\right)^{50}$

$=\left[\left(\frac{\sqrt{3}(1+i)}{\sqrt{3}+i}\right)^{2}\right]^{25}=\left[\frac{3(2 i)}{3-1+2 \sqrt{3} i}\right]^{25}$

$=\left(\frac{3 i}{1+\sqrt{3} i}\right)^{25}=\frac{3^{25} i^{25}}{\left(-2 \omega^{2}\right)^{25}}$

$$

\begin{array}{l}

=-i . \omega\left(\frac{3}{2}\right)^{25}=-\mathrm{i}\left(\frac{-1+\sqrt{3} \mathrm{i}}{2}\right)\left(\frac{3}{2}\right)^{25} \\

=\left(\frac{3}{2}\right)^{25}\left(\frac{\sqrt{3}}{2}+\frac{1}{2} \mathrm{i}\right)

\end{array}

$$

Hence, $\left(\frac{z_{1}}{z_{2}}\right)^{50}$ lies in the first quadrant as both real and imaginary parts of this number are positive.

</details>

---

### Q6. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `2`

If $z=x+i y, z^{1 / 3}=a-i b,$ then $\frac{x}{a}-\frac{y}{b}=k\left(a^{2}-b^{2}\right)$

where $k$ is equal to

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

$z^{1 / 3}=a-i b \Rightarrow z=(a-i b)^{3}$

$\therefore x+i y=a^{3}+i b^{3}-3 i a^{2} b-3 a b^{2}$

$\Rightarrow x=a^{3}-3 a b^{2} \Rightarrow \frac{x}{a}=a^{2}-3 b^{2}$

and $y=b^{3}-3 a^{2} b \Rightarrow \frac{y}{b}=b^{2}-3 a^{2}$

So, $\frac{x}{a}-\frac{y}{b}=4\left(a^{2}-b^{2}\right)$

</details>

---

### Q7. BITSAT 2011

*Type:* `singleCorrect` | *Level:* `1`

If \(a > 0, a \in R, z=a+2 i\) and \(z|z|-a z+1=0\) then

**Options:**

- **(A)** \(z\) is always a positive real number
- **(B)** \(z\) is always a negative real number
- **(C)** \(z\) is purely imaginary number
- **(D)** such a complex z does not exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) such a complex z does not exist**

**Detailed Solution:**

Putting \(z=a+2 i\) in the given equation and comparing imaginary parts, we get \(\mathrm{a}^2+4=\mathrm{a}^2\), which is not possible.

</details>

---

### Q8. BITSAT 2010

*Type:* `singleCorrect` | *Level:* `1`

The roots of the equation \(x^2-2 \sqrt{2} x+1=0\) are

**Options:**

- **(A)** Real and different
- **(B)** Imaginary and different
- **(C)** Real and equal
- **(D)** Rational and different

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Real and different**

**Detailed Solution:**

The discriminant of the equation \((-2 \sqrt{2})^2-4(1)(1)=8-4=4 > 0\) and \(a\) perfect square, so roots are real and different but we can't say that roots are rational because coefficients are not rational therefore.
\(\frac{\sqrt{2 \sqrt{2} \pm \sqrt{(2 \sqrt{2})^2-4}}}{2}=\frac{2 \sqrt{2} \pm 2}{2}=\sqrt{2} \pm 1\)
this is irrational \(\therefore\) the roots are real and different.

</details>

---

