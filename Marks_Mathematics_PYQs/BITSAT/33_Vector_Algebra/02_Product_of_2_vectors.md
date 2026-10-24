# BITSAT Mathematics - Vector Algebra

## Topic 2: Product of 2 vectors

**Total Questions:** 9

---

### Q1. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

A vector perpendicular to the plane containing the vectors $\hat{i}-2 \hat{j}-\hat{k}$ and $3 \hat{i}-2 \hat{j}-\hat{k}$ is inclined to the vector $\hat{i}+\hat{j}+\hat{k}$ at an angle

**Options:**

- **(A)** $\tan ^{-1} \sqrt{14}$
- **(B)** $\sec ^{-1} \sqrt{14}$
- **(C)** $\tan ^{-1} \sqrt{15}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan ^{-1} \sqrt{14}$**

**Detailed Solution:**

A vector perpendicular to the plane is
$\begin{aligned}
& (\hat{i}-2 \hat{j}-\hat{k}) \times(3 \hat{i}-2 \hat{j}-\hat{k}) \\
& =\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
1 & -2 & -1 \\
3 & -2 & -1
\end{array}\right|=-2 \hat{j}+4 \hat{k} \\
& \Rightarrow \text { unit vector } \hat{a}=\frac{-2 \hat{j}+4 \hat{k}}{\sqrt{4+16}}=\frac{-2 \hat{j}+4 \hat{k}}{2 \sqrt{5}}
\end{aligned}$
Angle between the unit vector and $\vec{r}=\hat{i}+\hat{j}+\hat{k}$
$=\cos ^{-1} \frac{\vec{r} \cdot \hat{a}}{|\vec{r}| \cdot|\hat{a}|}=\cos ^{-1} \frac{1}{\sqrt{15}}=\tan ^{-1} \sqrt{14}$

</details>

---

### Q2. BITSAT 2023 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\vec{a}=\hat{i}+\hat{j}+\hat{k}, \vec{a} \cdot \vec{b}=1$ and $\vec{a} \times \vec{b}=\vec{j}-\vec{k}$, then $\vec{b}$ is

**Options:**

- **(A)** $\hat{i}-\hat{j}+\hat{k}$
- **(B)** $2 \hat{j}-\hat{k}$
- **(C)** $2 \hat{i}$
- **(D)** $\hat{i}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\hat{i}$**

**Detailed Solution:**

Given $\vec{a}=\hat{i}+\hat{j}+\hat{k}, \vec{a} \cdot \vec{b}=1$ and $\vec{a} \times \vec{b}=\vec{j}-\vec{k}$,
Let $\bar{b}=b_1 \hat{i}+b_2 \hat{j}+b_3 \widehat{k}$
Now, $\hat{j}-\widehat{k}=\bar{a} \times \bar{b}=\left|\begin{array}{ccc}\hat{i} & \hat{j} & \widehat{k} \\ 1 & 1 & 1 \\ b_2 & b_2 & b_3\end{array}\right|$
$\Rightarrow b_3-b_2=0, b_1-b_3=1, b_2-b_1=-1$
$\Rightarrow b_3=b_2, b_1=b_2+1$
Also, $\bar{a} \cdot \bar{b}=1$
$\Rightarrow b_1+b_2+b_3=1$
$\Rightarrow 3 b_2+1=1$
$\Rightarrow b_2=0$
$\Rightarrow b_1=1, b_3=0$
Thus, $\bar{b}=\hat{i}$

</details>

---

### Q3. BITSAT 2019

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>3</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>p</mi><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover></math> is normal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>p</mi><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math> is normal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfenced><mrow><mover><mi mathvariant="normal">a</mi><mo>&#8594;</mo></mover><mo>+</mo><mi>p</mi><mover><mi mathvariant="normal">b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#183;</mo><mover><mi mathvariant="normal">c</mi><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>p</mi></mrow></mfenced><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mn>2</mn><mi>p</mi></mrow></mfenced><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mi>p</mi></mrow></mfenced><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mn>3</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>+</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo><mn>3</mn><mi>p</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>p</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q4. BITSAT 2015

*Type:* `singleCorrect` | *Level:* `2`

Let $a, b$ and $c$ be three vectors satisfying $a \times b=$ $(a \times c),|a|=|c|=1,|b|=4$ and $|b \times c|=\sqrt{15}$. If $b-$

$2 \mathrm{c}=\lambda \mathrm{a},$ then $\lambda$ equals

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** 2
- **(D)** -4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -4**

**Detailed Solution:**

Let $\theta$ be the angle between $\mathbf{b}$ and $\mathbf{c}$. Given, $|\mathrm{b} \times \mathrm{c}|=\sqrt{15}$

$$

\begin{array}{l}

\Rightarrow|\mathrm{b} \| \mathrm{c}| \sin \theta=\sqrt{15} \\

\Rightarrow \sin \theta=\frac{\sqrt{15}}{|\mathrm{~b}| \mathrm{c} \mid} \\

\Rightarrow \sin \theta=\sqrt{\frac{15}{4 \times 1}}=\frac{\sqrt{15}}{4} \\

\quad \therefore \cos \theta=\sqrt{1-\frac{15}{16}}=\frac{1}{\sqrt{16}}=\frac{1}{4}

\end{array}

$$

Now given, $\mathrm{b}-2 \mathrm{c}=\lambda \mathrm{a} \Rightarrow\left|\mathrm{b}-2 \mathrm{c}^{2}\right|=\mid \lambda \mathrm{a}^{2}$

$$

\Rightarrow|\mathrm{b}|^{2}+4|\mathrm{c}|-4(\mathrm{~b} \cdot \mathrm{c})=\lambda^{2}|\mathrm{a}|^{2}

$$

$$

\begin{array}{l}

\Rightarrow 16+4-4|\mathrm{~b} \| \mathrm{c}| \cos \theta=\lambda^{2} \\

\Rightarrow 20-16 \cos \theta=\lambda^{2} \\

\Rightarrow 20-4=\lambda^{2} \Rightarrow \lambda^{2}=16\left(\therefore \cos \theta=\frac{1}{4}\right) \\

\Rightarrow \lambda=\pm 4

\end{array}

$$

</details>

---

### Q5. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `1`

The angle between any two diagonal of a cube is

**Options:**

- **(A)** $45^{\circ}$
- **(B)** $60^{\circ}$
- **(C)** $30^{\circ}$
- **(D)** $\tan ^{-1}(2 \sqrt{2})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan ^{-1}(2 \sqrt{2})$**

**Detailed Solution:**

for a unit cube unit vector along the diagonal

$$

\mathrm{OP}=\frac{1}{\sqrt{3}}(\hat{\mathrm{i}}+\hat{\mathrm{j}}+\hat{\mathrm{k}})

$$

<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/7NTWetRK4yxOBniSvpXeh_Q4dVkdpauFDXCZLGDxbqY.original.fullsize.png">


unit vector along the diagonal

$\mathrm{CD}=\frac{1}{\sqrt{3}}(\hat{\mathrm{i}}+\hat{\mathrm{j}}-\hat{\mathrm{k}})$

$\therefore \cos \theta=\frac{1}{3}(1+1-1)=\frac{1}{3} \quad \therefore \tan \theta=2 \sqrt{2}$

</details>

---

### Q6. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `2`

If $a$.b $=a$.c and $a \times b=a \times c$, then correct statement is

**Options:**

- **(A)** $\mathrm{a} \|(\mathrm{b}-\mathrm{c})$
- **(B)** $a \perp(b-c)$
- **(C)** $a=0$ or $b=c$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $a=0$ or $b=c$**

**Detailed Solution:**

$a . b .=a \cdot c \Rightarrow a \cdot(b-c)=0$
$\Rightarrow \mathrm{a}=0 \mathrm{or} \mathrm{b}-\mathrm{c}=0$ or $\mathrm{a} \perp(\mathrm{b}-\mathrm{c})$
$\Rightarrow \mathrm{a}=0$ or $\mathrm{b}=\mathrm{c}$ or $\mathrm{a} \perp(\mathrm{b}-\mathrm{c})$
Also a $x b=a x c \Rightarrow a \times(b-c)=0$
$\Rightarrow \mathrm{a}=0$ or $\mathrm{b}-\mathrm{c}=0$ or a $\|(\mathrm{b}-\mathrm{c})$
$\Rightarrow a=0$ or $b=c$ or $a \|(b-c)$
Observing to ( 1 ) and ( 2 ) we find that $\mathrm{a}=0$ or $\mathrm{b}=\mathrm{c}$

</details>

---

### Q7. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `1`

The unit vector perpendicular to the vectors $6 \hat{i}+2 \hat{j}+3 \hat{k}$ and $3 \hat{i}-6 \hat{j}-2 \hat{k}$ is $-$

**Options:**

- **(A)** $\frac{2 \hat{i}-3 \hat{j}+6 \hat{k}}{7}$
- **(B)** $\frac{2 \hat{\mathrm{i}}-3 \hat{\mathrm{j}}-6 \hat{\mathrm{k}}}{7}$
- **(C)** $\frac{2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}-6 \hat{\mathrm{k}}}{7}$
- **(D)** $\frac{2 \hat{i}+3 \hat{j}+6 \hat{k}}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2 \hat{\mathrm{i}}+3 \hat{\mathrm{j}}-6 \hat{\mathrm{k}}}{7}$**

**Detailed Solution:**

Unit vector perpendicular to both the given vectors is, $\frac{(6 \hat{i}+2 \hat{j}+3 \hat{k}) \times(3 \hat{i}-6 \hat{j}-2 \hat{k})}{|(6 \hat{i}+2 \hat{j}+3 \hat{k}) \times(3 \hat{i}-6 \hat{j}-2 \hat{k})|}=\frac{2 \hat{i}+3 \hat{j}-6 \hat{k}}{7}$

</details>

---

### Q8. BITSAT 2010

*Type:* `singleCorrect` | *Level:* `1`

If \((\vec{a} \times \vec{b})^2+(\vec{a} \cdot \vec{b})^2=676\) and \(|\vec{b}|=2\) then \(|\vec{a}|\) is equal to

**Options:**

- **(A)** 13
- **(B)** 26
- **(C)** 39
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 13**

**Detailed Solution:**

\(\begin{aligned} &(\vec{a} \times \vec{b})^2+(\vec{a} \cdot \vec{b})^2=676 \\ &(|\vec{a}| \cdot|\vec{b}| \sin \theta \hat{n})^2+(|\vec{a}| \cdot|\vec{b}| \cos \theta)^2=676 \\ & \Rightarrow a^2 b^2 \sin ^2 \theta+a^2 b^2 \cos ^2 \theta=676\left[(\hat{n})^2=1\right] \\ & a^2 b^2\left(\sin ^2 \theta+\cos ^2 \theta\right)=676 \Rightarrow a^2=\frac{676}{b^2}=\frac{676}{4} \\ &|\vec{a}|=\sqrt{\frac{676}{4}} \Rightarrow|\vec{a}|=\frac{26}{2} \Rightarrow|\vec{a}|=13\end{aligned}\)

</details>

---

### Q9. BITSAT 2010

*Type:* `singleCorrect` | *Level:* `1`

The solution of differential equation \(2 x \frac{d y}{d x}-y=3\) represents a family of

**Options:**

- **(A)** circles
- **(B)** straight lines
- **(C)** ellipses
- **(D)** parabola

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) parabola**

**Detailed Solution:**

We have, \(2 x \frac{d y}{d x}=y+3 \Rightarrow \frac{2}{y+3} d y=\frac{d x}{x}\) integrating, \(2 \ln (y+3)=\ln x+\ln c=\ln c x\)
\(\Rightarrow \ln (y+3)^2=\ln \mathrm{cx} \Rightarrow(y+3)^2=\mathrm{cx}\)
which is a family of parabolas.

</details>

---

