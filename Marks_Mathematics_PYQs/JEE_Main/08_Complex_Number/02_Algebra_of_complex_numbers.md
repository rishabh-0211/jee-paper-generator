# JEE Main Mathematics - Complex Number

## Topic 2: Algebra of complex numbers

**Total Questions:** 44

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the set of all values of $k \in \mathbb{R}$ such that the equation $z(\bar{z} + 2 + i) + k(2 + 3i) = 0$, $z \in \mathbb{C}$, has at least one solution, be the interval $[\alpha, \beta]$. Then $9(\alpha + \beta)$ is equal to:

**Options:**

- **(A)** $-10$
- **(B)** $-8$
- **(C)** $10\sqrt{13}$
- **(D)** $8\sqrt{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-10$**

**Detailed Solution:**

Let $z = x + iy$, then $\bar{z} = x - iy$.

Substituting $z$ into the given equation:

$(x + iy)(x - iy + 2 + i) + k(2 + 3i) = 0$

$x^2 + y^2 + 2x + ix + 2iy - y + 2k + 3ki = 0$

Separating the real and imaginary parts, we get:

Real part: $x^2 + y^2 + 2x - y + 2k = 0$

Imaginary part: $x + 2y + 3k = 0 \Rightarrow x = -2y - 3k$

Substituting $x$ into the real part equation:

$(-2y - 3k)^2 + y^2 + 2(-2y - 3k) - y + 2k = 0$

$4y^2 + 12ky + 9k^2 + y^2 - 4y - 6k - y + 2k = 0$

$5y^2 + (12k - 5)y + 9k^2 - 4k = 0$

For the equation to have at least one solution $z \in \mathbb{C}$, there must be at least one real value of $y$. Thus, the discriminant of this quadratic equation in $y$ must be non-negative ($\Delta \ge 0$):

$\Delta = (12k - 5)^2 - 4(5)(9k^2 - 4k) \ge 0$

$144k^2 - 120k + 25 - 180k^2 + 80k \ge 0$

$-36k^2 - 40k + 25 \ge 0$

$36k^2 + 40k - 25 \le 0$

The values of $k$ lie in the interval $[\alpha, \beta]$, where $\alpha$ and $\beta$ are the roots of the equation $36k^2 + 40k - 25 = 0$.

The sum of the roots is given by:

$\alpha + \beta = -\dfrac{40}{36} = -\dfrac{10}{9}$

Therefore, $9(\alpha + \beta) = 9 \left( -\dfrac{10}{9} \right) = -10$.

Answer: $-10$

</details>

---

### Q2. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $x$ and $y$ be real numbers such that $50\left(\dfrac{2x}{1+3i} - \dfrac{y}{1-2i}\right) = 31 + 17i$, $i = \sqrt{-1}$. Then the value of $10(x - 3y)$ is :

**Options:**

- **(A)** $20$
- **(B)** $31$
- **(C)** $35$
- **(D)** $75$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $75$**

**Detailed Solution:**

Given the equation:

$50\left(\dfrac{2x}{1+3i} - \dfrac{y}{1-2i}\right) = 31 + 17i$

Rationalizing the denominators inside the parentheses:

$\dfrac{2x}{1+3i} = \dfrac{2x(1-3i)}{(1+3i)(1-3i)} = \dfrac{2x(1-3i)}{1^2 + 3^2} = \dfrac{2x(1-3i)}{10} = \dfrac{x(1-3i)}{5}$

$\dfrac{y}{1-2i} = \dfrac{y(1+2i)}{(1-2i)(1+2i)} = \dfrac{y(1+2i)}{1^2 + 2^2} = \dfrac{y(1+2i)}{5}$

Substituting these back into the given equation:

$50\left(\dfrac{x(1-3i)}{5} - \dfrac{y(1+2i)}{5}\right) = 31 + 17i$

$10(x(1-3i) - y(1+2i)) = 31 + 17i$

$10(x - y) - 10i(3x + 2y) = 31 + 17i$

Equating the real and imaginary parts on both sides:

$10(x - y) = 31 \Rightarrow 10x - 10y = 31$

$-10(3x + 2y) = 17 \Rightarrow -30x - 20y = 17$

Multiplying the first equation by $3$ gives:

$30x - 30y = 93$

Adding this to the second equation:

$(-30x - 20y) + (30x - 30y) = 17 + 93$

$-50y = 110 \Rightarrow y = -\dfrac{11}{5}$

Substituting $y = -\dfrac{11}{5}$ into $10x - 10y = 31$:

$10x - 10\left(-\dfrac{11}{5}\right) = 31$

$10x + 22 = 31 \Rightarrow 10x = 9 \Rightarrow x = \dfrac{9}{10}$

Now, finding the value of $10(x - 3y)$:

$10(x - 3y) = 10x - 30y = 10\left(\dfrac{9}{10}\right) - 30\left(-\dfrac{11}{5}\right)$

$10(x - 3y) = 9 + 66 = 75$

Answer: $75$

</details>

---

### Q3. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the product of $\omega_1=(8+i) \sin \theta+(7+4 i) \cos \theta$ and $\omega_2=(1+8 i) \sin \theta+(4+7 i) \cos \theta$ be $\alpha+i \beta$, $\mathrm{i}=\sqrt{-1}$. Let p and q be the maximum and the minimum values of $\alpha+\beta$ respectively.

**Options:**

- **(A)** $140$
- **(B)** $130$
- **(C)** $160$
- **(D)** $150$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $130$**

**Detailed Solution:**

$\begin{aligned}
& \omega_1=(8 \sin \theta+7 \cos \theta)+i(\sin \theta+4 \cos \theta) \\
& \omega_2=(\sin \theta+4 \cos \theta)+i(8 \sin \theta+7 \cos \theta) \\
& \omega_1 \omega_2=8 \sin ^2 \theta+7 \sin \theta \cos \theta+32 \sin \theta \cos \theta+ \\
& 28 \cos ^2 \theta-8 \sin ^2 \theta-32 \sin \theta \cos \theta-7 \sin \theta \cos \theta \\
& -28 \cos ^2 \theta+i\left(\sin ^2 \theta+4 \sin \theta \cos \theta+4 \sin \theta \cos \theta\right. \\
& +16 \cos ^2 \theta+64 \sin ^2 \theta+56 \sin \theta \cos \theta+56 \sin \theta \\
& \left.\cos \theta+49 \cos ^2 \theta\right) \\
& \omega_1 \omega_2=0+i\left(65 \sin ^2 \theta+120 \sin \theta \cos \theta+65 \cos ^2 \theta\right) \\
& \alpha+\beta=65+60 \sin 2 q \\
& \alpha+\left.\beta\right|_{\max }=125 \\
& \alpha+\left.\beta\right|_{\min }=5
\end{aligned}$
$\text { Ans. }=125+5=130$
option (2)

</details>

---

### Q4. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $z \in C$ be such that $\frac{z^2+3 i}{z-2+i}=2+3 i$. Then the sum of all possible values of $z^2$ is

**Options:**

- **(A)** $19-2 \mathrm{i}$
- **(B)** $-19-2 \mathrm{i}$
- **(C)** $19+2 i$
- **(D)** $-19+2 i$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-19-2 \mathrm{i}$**

**Detailed Solution:**

$z^2+3 i=z(2+3 i)-7-4 i$
$\mathrm{z}^2-\mathrm{z}(2+3 \mathrm{i})+7+7 \mathrm{i}=0$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/-rweKsieqmS1LBcSoo_sAW2SM7SCVllbRatlEGe1Za0.original.fullsize.png"/>
$\begin{aligned}
& z_1^2+z_2^2=\left(z_1+z_2\right)^2-2 z_1 z_2 \\
& =4-9+12 i-14-14 i \\
& =-19-2 i
\end{aligned}$

</details>

---

### Q5. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\alpha+i \beta$ and $\gamma+i \delta$ are the roots of $x^2-(3-2 i) x-(2 i-2)=0, i=\sqrt{-1}$, then $\alpha \gamma+\beta \delta$ is equal to :

**Options:**

- **(A)** $-2$
- **(B)** $6$
- **(C)** $-6$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2$**

**Detailed Solution:**

$\begin{aligned} & x^2-(3-2 \mathrm{i}) \mathrm{x}-(2 \mathrm{i}-2)=0 \\ & \mathrm{x}=\frac{(3-2 \mathrm{i}) \pm \sqrt{(3-2 \mathrm{i})^2-4(1)(-(2 \mathrm{i}-2))}}{2(1)} \\ & ==\frac{(3-2 \mathrm{i}) \pm \sqrt{9-4-12 \mathrm{i}+8 \mathrm{i}-8}}{2} \\ & ==\frac{3-2 \mathrm{i} \pm \sqrt{-3-4 \mathrm{i}}}{2} \\ & =\frac{3-2 \mathrm{i} \pm \sqrt{(1)^2+(2 \mathrm{i})^2-2(1)(2 \mathrm{i})}}{2} \\ & =\frac{3-2 \mathrm{i} \pm(1-2 \mathrm{i})}{2} \\ & \Rightarrow \frac{3-2 \mathrm{i}+1-2 \mathrm{i}}{2} \text { or } \frac{3-2 \mathrm{i}-1+2 \mathrm{i}}{2} \\ & \Rightarrow 2-2 \mathrm{i} \text { or } 1+0 \mathrm{i} \\ & \text { So } \alpha \gamma+\beta \delta=2(1)+(-2)(0)=2\end{aligned}$

</details>

---

### Q6. JEE Main 2025 (23 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $\alpha, \beta$ be the roots of the equation $x^2-a x-b=0$ with $\operatorname{Im}(\alpha) \lt \operatorname{Im}(\beta)$. Let $P_n=\alpha^n-\beta^n$. If $\mathrm{P}_3=-5 \sqrt{7} i, \mathrm{P}_4=-3 \sqrt{7} i, \mathrm{P}_5=11 \sqrt{7} i$ and $\mathrm{P}_6=45 \sqrt{7} i$, then $\left|\alpha^4+\beta^4\right|$ is equal to $\qquad$ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **31**

**Detailed Solution:**

$\begin{aligned}
& \alpha+\beta=\mathrm{a} \quad \alpha \beta=-\mathrm{b} \\
& \mathrm{P}_6=\mathrm{aP}_5+\mathrm{bP}_4 \\
& 45 \sqrt{7} \mathrm{i}=\mathrm{a} \times 11 \sqrt{7} \mathrm{i}+\mathrm{b}(-3 \sqrt{7}) \mathrm{i} \\
& 45=11 \mathrm{a}-3 \mathrm{~b}
\end{aligned}$
and
$\begin{aligned}
& P_5=\mathrm{aP}_4+b P_3 \\
& 11 \sqrt{7} \mathrm{i}=\mathrm{a}(-3 \sqrt{7} \mathrm{i})+\mathrm{b}(-5 \sqrt{7} \mathrm{i}) \\
& 11=-3 \mathrm{a}-5 \mathrm{~b} \\
& \mathrm{a}=3, \mathrm{~b}=-4 \\
& \left|\alpha^4+\beta^4\right|=\sqrt{\left(\alpha^4-\beta^4\right)^2+4 \alpha^4 \beta^4} \\
& =\sqrt{-63+4.4^4} \\
& =\sqrt{-63+1024}=\sqrt{961}=31
\end{aligned}$

</details>

---

### Q7. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of complex numbers $z$, satisfying $|z|=1$ and $\left|\frac{z}{\bar{z}}+\frac{\bar{z}}{z}\right|=1$, is :

**Options:**

- **(A)** 4
- **(B)** 8
- **(C)** 10
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 8**

**Detailed Solution:**

$\begin{aligned}
& |z|=1 \\
& \left|\frac{z}{\bar{z}}+\frac{\bar{z}}{z}\right|=1 \\
& \Rightarrow\left|z^2+(\bar{z})^2\right|=1
\end{aligned}$
Let $z=x+i y$
$\begin{aligned}
& \Rightarrow\left|(x+i y)^2+(x-i y)^2\right|=1 \\
& \Rightarrow\left|2 x^2-2 y^2\right|=1 \\
& \Rightarrow\left|x^2-y^2\right|=\frac{1}{2} \\
& \Rightarrow x^2-y^2=\frac{ \pm 1}{2} \\
& \text { and } x^2+y^2=1
\end{aligned}$
Case I: $x^2-y^2=\frac{1}{2}$
Case II: $x^2-y^2=-\frac{1}{2}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/og8TEMnqg76KtVOosOT0nmTKMc31yR69ZGORSa039Kg.original.fullsize.png">

</details>

---

### Q8. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $z$ be a complex number such that $|z+2|=1$ and $\operatorname{Im}\left(\frac{z+1}{z+2}\right)=\frac{1}{5}$. Then the value of $|\operatorname{Re}(\overline{z+2})|$ is

**Options:**

- **(A)** $\frac{2 \sqrt{6}}{5}$
- **(B)** $\frac{24}{5}$
- **(C)** $\frac{1+\sqrt{6}}{5}$
- **(D)** $\frac{\sqrt{6}}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2 \sqrt{6}}{5}$**

**Detailed Solution:**

$|z+2|=1, \operatorname{Im}\left(\frac{z+1}{z+2}\right)=\frac{1}{5}$
Let $z+2=\cos \theta+i \sin \theta$
$\begin{aligned}
& \frac{1}{z+2}=\cos \theta-i \sin \theta \\
& \Rightarrow \frac{z+1}{z+2}=1-\frac{1}{z+2}=1-(\cos \theta-i \sin \theta) \\
& =(1-\cos \theta)+\operatorname{isin} \theta \\
& \operatorname{Im}\left(\frac{z+1}{z+2}\right)=\sin \theta, \sin \theta=\frac{1}{5} \\
& \cos \theta= \pm \sqrt{1-\frac{1}{25}}= \pm \frac{2 \sqrt{6}}{5} \\
& |\operatorname{Re}(\overline{z+2})|=\frac{2 \sqrt{6}}{5}
\end{aligned}$

</details>

---

### Q9. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Consider the following two statements :
Statement I : For any two non-zero complex numbers $z_1, z_2$,
$\left(\left|z_1\right|+\left|z_2\right|\right)\left|\frac{z_1}{\left|z_1\right|}+\frac{z_2}{\left|z_2\right|}\right| \leq 2\left(\left|z_1\right|+\left|z_2\right|\right) \text {, and }$
Statement II : If $x, y, z$ are three distinct complex numbers and $\mathrm{a}, \mathrm{b}, \mathrm{c}$ are three positive real numbers such that $\frac{\mathrm{a}}{|y-z|}=\frac{\mathrm{b}}{|z-x|}=\frac{\mathrm{c}}{|x-y|}$, then
$\frac{\mathrm{a}^2}{y-z}+\frac{\mathrm{b}^2}{z-x}+\frac{\mathrm{c}^2}{x-y}=1 .$
Between the above two statements,

**Options:**

- **(A)** Statement I is correct but Statement II is incorrect.
- **(B)** both Statement I and Statement II are correct.
- **(C)** both Statement I and Statement II are incorrect.
- **(D)** Statement I is incorrect but Statement II is correct.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement I is correct but Statement II is incorrect.**

**Detailed Solution:**

Statement I :
$\left(\left|z_1\right|+\left|z_2\right|\right)\left|\frac{z_1}{\left|z_1\right|}+\frac{z_2}{\left|z_2\right|}\right|$
Since $\left|\frac{z_1}{\left|z_1\right|}+\frac{z_2}{\left|z_2\right|}\right| \leq\left|\frac{z_1}{\left|z_1\right|}\right|+\left|\frac{z_2}{\left|z_2\right|}\right|$
$\begin{aligned}
& \left|\frac{z_1}{\left|z_1\right|}+\frac{z_2}{\left|z_2\right|}\right| \leq \frac{\left|z_1\right|}{\left|z_1\right|}+\frac{\left|z_2\right|}{\left|z_2\right|} \\
& \left|\frac{z_1}{\left|z_1\right|}+\frac{z_2}{\left|z_2\right|}\right| \leq 2
\end{aligned}$
$\left(\left|z_1\right|+\left|z_2\right|\right)\left(\left|\frac{z_1}{\left|z_1\right|}+\frac{z_2}{\left|z_2\right|}\right|\right) \leq 2\left(\left|z_1\right|+\left|z_2\right|\right)$
$\therefore$ statement $\mathrm{I}$ is correct
For Statement II :
$\begin{aligned}
& \frac{a}{|y-z|}=\frac{b}{|z-x|}=\frac{c}{|x-y|} \\
& \frac{a^2}{|y-z|^2}=\frac{b^2}{|z-x|^2}=\frac{c^2}{|x-y|^2}=\lambda \\
& a^2=\lambda\left(|y-z|^2\right)=\lambda(y-z)(\bar{y}-\bar{z}) \\
& b^2=\lambda(z-x)(\bar{z}-\bar{x}) \text { and } c^2=\lambda(x-y)(\bar{x}-\bar{y}) \\
& \frac{a^2}{y-z}+\frac{b^2}{z-x}+\frac{c^2}{x-y}=\lambda(\bar{y}-\bar{z}+\bar{z}-\bar{x}+\bar{x}-\bar{y})=0
\end{aligned}$
Statement II is false

</details>

---

### Q10. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo mathvariant="italic">Re</mo><mfenced><mfrac><mrow><mi>z</mi><mo>-</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>+</mo><mi>z</mi><mover><mi>z</mi><mo>&#175;</mo></mover></mrow><mrow><mn>2</mn><mo>-</mo><mn>3</mn><mi>z</mi><mo>+</mo><mn>5</mn><mover><mi>z</mi><mo>&#175;</mo></mover></mrow></mfrac></mfenced><mo>:</mo><mi>z</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8450;</mi><mo>,</mo><mo>&#160;</mo><mo mathvariant="italic">Re</mo><mi>z</mi><mo>=</mo><mn>3</mn></mrow></mfenced></math> is equal to the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>]</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>42</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that the set<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>Re</mo><mfenced><mfrac><mrow><mi>z</mi><mo>-</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>+</mo><mi>z</mi><mover><mi>z</mi><mo>&#175;</mo></mover></mrow><mrow><mn>2</mn><mo>-</mo><mn>3</mn><mi>z</mi><mo>+</mo><mn>5</mn><mover><mi>z</mi><mo>&#175;</mo></mover></mrow></mfrac></mfenced><mo>:</mo><mi>z</mi><mo>&#8712;</mo><mi>&#8450;</mi><mo>,</mo><mo>&#160;</mo><mo>Re</mo><mi>z</mi><mo>=</mo><mn>3</mn></mrow></mfenced></math> is equal to the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>]</mo></math>.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">=</mo><mo mathvariant="italic">Re</mo><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi><mo>-</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mo>-</mo><mn>3</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mo>+</mo><mn>5</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mi>i</mi><mi>y</mi></mrow></mfenced></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">=</mo><mo mathvariant="italic">Re</mo><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>i</mi><mfenced><mrow><mn>2</mn><mi>y</mi></mrow></mfenced></mrow><mrow><mn>2</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>8</mn><mi>i</mi><mi>y</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">=</mo><mo mathvariant="italic">Re</mo><mfenced><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>y</mi><mi>i</mi></mrow></mfenced><mfenced><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mn>8</mn><mi>i</mi><mi>y</mi></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>8</mn><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mn>16</mn><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mn>4</mn><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>8</mn><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p>Now using, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mi>e</mi><mfenced><mi>z</mi></mfenced><mo>=</mo><mn>3</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>3</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>8</mn><mfenced><mrow><mn>9</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mn>16</mn><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mn>64</mn><mo>+</mo><mn>64</mn><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mfrac><mfenced><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mfrac><mfenced><mrow><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mi>t</mi><mo>+</mo><mn>8</mn><mi>t</mi><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mfenced><mrow><mn>8</mn><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>8</mn><mi>t</mi><mo>-</mo><mn>9</mn><mo>=</mo><mn>0</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>0</mn><mn>2</mn></msup><mo>-</mo><mn>4</mn><mfenced><mrow><mn>8</mn><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>8</mn><mi>t</mi><mo>-</mo><mn>9</mn></mrow></mfenced><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>t</mi><mo>-</mo><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>8</mn></mfrac></mfenced></mrow></mfenced><mfenced><mrow><mi>t</mi><mo>-</mo><mfrac><mn>9</mn><mn>8</mn></mfrac></mrow></mfenced><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>&#8712;</mo><mo>(</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>8</mn></mfrac><mo>,</mo><mfrac><mn>9</mn><mn>8</mn></mfrac><mo>]</mo></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#8800;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>8</mn></mfrac></math></p><p>Range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>=</mo><mo>(</mo><mo>-</mo><mn>0</mn><mo>.</mo><mn>125</mn><mo>,</mo><mn>1</mn><mo>.</mo><mn>125</mn><mo>]</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mo>&#160;</mo><mn>0</mn><mo>.</mo><mn>125</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>125</mn><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>24</mn><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mn>30</mn></math></p><p>Hence this is the required solution.</p></blockquote>

</details>

---

### Q11. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8450;</mi></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mi>z</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8450;</mi><mo>:</mo><mo>Re</mo><mo>(</mo><mi>a</mi><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>)</mo><mo>&#62;</mo><mo>Im</mo><mo>(</mo><mover><mi>a</mi><mo>&#175;</mo></mover><mo>+</mo><mi>z</mi><mo>)</mo><mo>}</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mo>{</mo><mi>z</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8450;</mi><mo>:</mo><mo>Re</mo><mo>(</mo><mi>a</mi><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>)</mo><mo>&#60;</mo><mo>Im</mo><mo>(</mo><mover><mi>a</mi><mo>&#175;</mo></mover><mo>+</mo><mi>z</mi><mo>)</mo><mo>}</mo></math>. Then among the two statements:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>S</mi><mn>1</mn><mo>)</mo></math> : If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Re</mo><mo>(</mo><mi>a</mi><mo>)</mo><mo>,</mo><mo>Im</mo><mo>(</mo><mi>a</mi><mo>)</mo><mo>&#62;</mo><mn>0</mn></math>, then the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> contains all the real numbers
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>S</mi><mn>2</mn><mo>)</mo></math> : If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Re</mo><mo>(</mo><mi>a</mi><mo>)</mo><mo>,</mo><mo>Im</mo><mo>(</mo><mi>a</mi><mo>)</mo><mo>&#60;</mo><mn>0</mn></math>, then the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> contains all the real numbers,

**Options:**

- **(A)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is true
- **(B)** only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> is true
- **(C)** Both are true
- **(D)** Both are false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Both are false**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mi>i</mi><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><mover><mi>a</mi><mo>&#175;</mo></mover><mo>=</mo><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mi>i</mi><msub><mi>y</mi><mn>1</mn></msub></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mi>i</mi><msub><mi>y</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mi>i</mi><msub><mi>y</mi><mn>2</mn></msub></math>      </p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mo>+</mo><mi>i</mi><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#175;</mo></mover><mo>+</mo><mi>z</mi><mo>=</mo><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mo>+</mo><mi>i</mi><mfenced><mrow><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced></math></p><p>Now according to the question,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Re</mo><mo>(</mo><mi>a</mi><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>)</mo><mo>=</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Im</mo><mo>(</mo><mover><mi>a</mi><mo>&#175;</mo></mover><mo>+</mo><mi>z</mi><mo>)</mo><mo>=</mo><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>z</mi><mo>:</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#62;</mo><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mo>=</mo><mfenced close="}" open="{"><mrow><mi>z</mi><mo>:</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#62;</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced></math>
  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>z</mi><mo>:</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#60;</mo><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mo>=</mo><mfenced close="}" open="{"><mrow><mi>z</mi><mo>:</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#60;</mo><msub><mi>y</mi><mn>2</mn></msub></mrow></mfenced></math></p><p>If  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>y</mi><mn>1</mn></msub><mo>&#62;</mo><mn>0</mn></math> then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mi>z</mi><mo>:</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#62;</mo><mo>-</mo><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mo>}</mo></math></p><p>A covers a part of negative real axis and therefore, does not contain whole real axis</p><p>Similarly if <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>y</mi><mn>1</mn></msub><mo>&#60;</mo><mn>0</mn></math>, then 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mo>{</mo><mi>z</mi><mo>:</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#60;</mo><mo>-</mo><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced><mo>}</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> covers part of positive real axis and therefore does not cover whole real axis.</p><p>Hence, both are false.</p>

</details>

---

### Q12. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>For two non-zero complex number <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>2</mn></msub></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Re</mo><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Re</mo><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>0</mn></math>, then which of the following are possible?</p><p>(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Im</mo><mfenced><msub><mi mathvariant="normal">z</mi><mn>1</mn></msub></mfenced><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Im</mo><mfenced><msub><mi mathvariant="normal">z</mi><mn>2</mn></msub></mfenced><mo>&#62;</mo><mn>0</mn></math>
(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Im</mo><mfenced><msub><mi mathvariant="normal">z</mi><mn>1</mn></msub></mfenced><mo>&#60;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Im</mo><mfenced><msub><mi mathvariant="normal">z</mi><mn>2</mn></msub></mfenced><mo>&#62;</mo><mn>0</mn></math>
(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Im</mo><mfenced><msub><mi mathvariant="normal">z</mi><mn>1</mn></msub></mfenced><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Im</mo><mfenced><msub><mi mathvariant="normal">z</mi><mn>2</mn></msub></mfenced><mo>&#60;</mo><mn>0</mn></math>
(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Im</mo><mfenced><msub><mi mathvariant="normal">z</mi><mn>1</mn></msub></mfenced><mo>&#60;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Im</mo><mfenced><msub><mi mathvariant="normal">z</mi><mn>2</mn></msub></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p>Choose the correct answer from the options given below:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">D</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi></math>**

**Detailed Solution:**

<p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>1</mn></msub><mo>=</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mi>i</mi><msub><mi>y</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>z</mi><mn>2</mn></msub><mo>=</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mi>i</mi><msub><mi>y</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>Re</mo><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>Re</mo><mfenced><mrow><msub><mi>z</mi><mn>1</mn></msub><mo>+</mo><msub><mi>z</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>From equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><msub><mi>x</mi><mn>1</mn></msub><mn>2</mn></msup><mo>+</mo><msub><mi>y</mi><mn>1</mn></msub><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>y</mi><mn>1</mn></msub><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><msup><msub><mi>x</mi><mn>1</mn></msub><mn>2</mn></msup></math></p><p>Therefore <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>m</mi><mo>(</mo><msub><mi>z</mi><mn>1</mn></msub><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>m</mi><mo>(</mo><msub><mi>z</mi><mn>2</mn></msub><mo>)</mo></math> are of opposite sign</p>

</details>

---

### Q13. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let for some real numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>,</mo><mi>a</mi><mo>=</mo><mi>&#945;</mi><mo>-</mo><mi>i</mi><mi>&#946;</mi></math>. If the system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>i</mi><mi>x</mi><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow></mfenced><mi>y</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mfenced><mrow><mi>cos</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mi>i</mi><mi>sin</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>x</mi><mo>+</mo><mover><mi>a</mi><mo>&#175;</mo></mover><mi>y</mi><mo>=</mo><mn>0</mn></math> has more than one solution then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p>The given system of equations has more than one solution, then it must have infinitely many solutions.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mi>i</mi></mrow><mrow><mn>8</mn><mfenced><mrow><mi>cos</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mi>i</mi><mi>sin</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow><mrow><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>&#946;</mi></mrow></mfrac></math>    <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><mtable columnalign="right left"><mtr><mtd><mi>a</mi></mtd><mtd><mo>=</mo><mi>&#945;</mi><mo>-</mo><mi>i</mi><mi>&#946;</mi></mtd></mtr><mtr><mtd><mo>&#8658;</mo><menclose notation="top"><mi>a</mi></menclose></mtd><mtd><mo>=</mo><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>&#946;</mi></mtd></mtr></mtable></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>4</mn><mi>i</mi></mrow><mrow><mn>8</mn><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mi>i</mi><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>i</mi></mrow><mrow><mi>&#945;</mi><mo>+</mo><mi>i</mi><mi>&#946;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mi>i</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>-</mo><mi>i</mi><mo>+</mo><msqrt><mn>3</mn></msqrt><mi>i</mi><mo>-</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mi>&#946;</mi><mo>+</mo><mi>&#945;</mi><mi>i</mi><mo>=</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mo>=</mo><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math>  </p>

</details>

---

### Q14. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let a complex number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>,</mo><mo>&#160;</mo><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>&#8800;</mo><mn>1</mn></math>, satisfy <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></msub><mfenced><mfrac><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>11</mn></mrow><msup><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></mfenced><mo>&#8804;</mo><mn>2</mn></math>. Then, the largest value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>z</mi></mfenced></math> is equal to _________.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></msub><mfenced><mfrac><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>+</mo><mn>11</mn></mrow><msup><mfenced><mrow><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></mfenced><mo>&#8804;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>+</mo><mn>11</mn></mrow><msup><mfenced><mrow><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>&#8805;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo>&#8757;</mo><msub><mi>log</mi><mi>a</mi></msub><mfenced><mi>b</mi></mfenced><mo>&#8804;</mo><mi>c</mi><mo>&#8658;</mo><mi>b</mi><mo>&#8805;</mo><msup><mi>a</mi><mi>c</mi></msup><mo>&#160;</mo><mi>i</mi><mi>f</mi><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>a</mi><mo>&#60;</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>+</mo><mn>22</mn><mo>&#8805;</mo><msup><mfenced><mrow><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo>&#8757;</mo><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>&#8800;</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mfenced><mrow><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>+</mo><mn>22</mn><mo>&#8805;</mo><msup><mfenced open="|" close="|"><mi>z</mi></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><mfenced open="|" close="|"><mi>z</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="|" close="|"><mi>z</mi></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>-</mo><mn>21</mn><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>-</mo><mn>7</mn></mrow></mfenced><mfenced><mrow><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>&#8804;</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Largest value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>z</mi></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p>

</details>

---

### Q15. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>z</mi><mo>+</mo><mi>i</mi></mrow><mrow><mi>z</mi><mo>-</mo><mi>k</mi><mi>i</mi></mrow></mfrac><mo>,</mo><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#62;</mo><mn>0</mn></math>. If the curve represented by<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Re</mo><mo>(</mo><mi>u</mi><mo>)</mo><mo>+</mo><mo>Im</mo><mo>(</mo><mi>u</mi><mo>)</mo><mo>=</mo><mn>1</mn></math> intersects the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis at points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Q</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>PQ</mi><mo>=</mo><mn>5</mn></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">k</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mo>+</mo><mi>i</mi></mrow><mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mo>&#8722;</mo><mi>k</mi><mtext>&#8201;</mtext><mi>i</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mfenced><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>i</mi></mrow><mrow><mi>x</mi><mo>+</mo><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><mi>k</mi></mrow></mfenced><mi>i</mi></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mi>x</mi><mo>&#8722;</mo><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><mi>k</mi></mrow></mfenced><mi>i</mi></mrow><mrow><mi>x</mi><mo>&#8722;</mo><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><mi>k</mi></mrow></mfenced><mi>i</mi></mrow></mfrac></math></p><p>Real part of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo mathvariant="italic">=</mo><mi>R</mi><mi>e</mi><mfenced><mi>u</mi></mfenced><mo mathvariant="italic">=</mo><mfrac><mrow><mn mathvariant="italic">2</mn><msup><mi>x</mi><mn mathvariant="italic">2</mn></msup><mo>+</mo><mfenced><mrow><mn mathvariant="italic">2</mn><mi>y</mi><mo mathvariant="italic">+</mo><mn mathvariant="italic">1</mn></mrow></mfenced><mfenced><mrow><mi>y</mi><mo mathvariant="italic">&#8722;</mo><mi>k</mi></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn mathvariant="italic">2</mn></msup><mo mathvariant="italic">+</mo><msup><mfenced><mrow><mi>y</mi><mo mathvariant="italic">&#8722;</mo><mi>k</mi></mrow></mfenced><mn mathvariant="italic">2</mn></msup></mrow></mfrac></math></p><p>Imaginary part of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>=</mo><mi>Im</mi><mfenced><mi>u</mi></mfenced><mfrac><mrow><mi>x</mi><mfenced><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8722;</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><mi>k</mi></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><mi>k</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Re</mi><mfenced><mi>u</mi></mfenced><mo>+</mo><mi>Im</mi><mfenced><mi>u</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><mi>k</mi></mrow></mfenced><mo>+</mo><mi>x</mi><mfenced><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8722;</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><mi>k</mi></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><mi>k</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p>for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><mi>k</mi></mrow></mfenced></mrow><msup><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><mi>k</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>y</mi><mo>&#8722;</mo><mi>k</mi></mrow></mfenced><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>k</mi><mo>,</mo><mtext>&#8201;</mtext><mo>&#8722;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>k</mi></mrow></mfenced></math></p><p>Now point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mtext>&#8201;</mtext><mi>k</mi></mrow></mfenced><mo>,</mo><mtext>&#8201;</mtext><mi>Q</mi><mfenced><mrow><mn>0</mn><mo>,</mo><mtext>&#8201;</mtext><mo>&#8722;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>k</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi>K</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>k</mi><mo>+</mo><mn>1</mn><mo>=</mo><mo>&#177;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>k</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#8722;</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#8722;</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mi>k</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math>.</p>

</details>

---

### Q16. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The imaginary part of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mo>-</mo><mn>54</mn></msqrt></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mo>-</mo><mn>54</mn></msqrt></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math>,can be

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>6</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>6</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mo>-</mo><mn>54</mn></msqrt><mo>|</mo><mo>=</mo><msqrt><mn>9</mn><mo>+</mo><mn>216</mn></msqrt><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mo>-</mo><mn>54</mn></msqrt></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mo>&#177;</mo><mfenced><mrow><msqrt><mfrac><mrow><mn>15</mn><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac></msqrt><mo>+</mo><mi>i</mi><msqrt><mfrac><mrow><mn>15</mn><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#177;</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mi>i</mi><msqrt><mn>6</mn></msqrt></mrow></mfenced></math> </p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mo>-</mo><mn>54</mn></msqrt></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mo>&#177;</mo><mfenced><mrow><mn>3</mn><mo>-</mo><mi>i</mi><msqrt><mn>6</mn></msqrt></mrow></mfenced></math> </p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><msup><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mo>-</mo><mn>54</mn></msqrt></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>-</mo><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mo>-</mo><mn>54</mn></msqrt></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#177;</mo><mn>2</mn><msqrt><mn>6</mn></msqrt><mi>i</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#177;</mo><mn>6</mn></math> </p><p>Hence, imaginary part <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#177;</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></math></p>

</details>

---

### Q17. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mi mathvariant="normal">R</mi><mi mathvariant="normal">e</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>z</mi><mo>+</mo><mi>i</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mi></mi></math> where <math><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi><mo>,</mo><mi></mi></math> then the point <math><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi></mi><mi>y</mi></mrow></mfenced></math> lies on a

**Options:**

- **(A)** circle whose centre is at <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi></mi><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
- **(B)** straight line whose slope is <math><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** straight line whose slope is <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** circle whose diameter is <math><mfrac><mrow><msqrt><mn>5</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) circle whose diameter is <math><mfrac><mrow><msqrt><mn>5</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let <math><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>z</mi><mo>+</mo><mi>i</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>i</mi><mi>y</mi></mrow><mrow><mn>2</mn><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mo>+</mo><mi>i</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>i</mi><mi>y</mi></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>i</mi></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mfenced separators="|"><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>i</mi></mrow><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mfenced separators="|"><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>i</mi></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mi>e</mi><mfenced separators="|"><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>z</mi><mo>+</mo><mi>i</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>y</mi><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>y</mi><mo>+</mo><mn>1</mn></math>
<math><mo>&#8658;</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>y</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p>Circle with center <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><msqrt><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>9</mn><mn>16</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mrow><mn>4</mn><mo>+</mo><mn>9</mn><mo>-</mo><mn>8</mn></mrow><mn>16</mn></mfrac></msqrt><mo>=</mo><mfrac><msqrt><mn>5</mn></msqrt><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mfrac><msqrt><mn>5</mn></msqrt><mn>2</mn></mfrac></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo></math>diameter of the given circle.</p>

</details>

---

### Q18. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\left(-2-\frac{1}{3} i\right)^{3}=\frac{x+i y}{27}(i=\sqrt{-1}),$ where $x$ and $y$ are real numbers then $\mathrm{y}-\mathrm{x}$ equals

**Options:**

- **(A)** 91
- **(B)** -85
- **(C)** 85
- **(D)** -91

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 91**

**Detailed Solution:**

$-(6+i)^{3}=x+i y$

$\Rightarrow \quad-\left[216+i^{3}+18 i(6+i)\right]=x+i y$

$\Rightarrow \quad-[216-i+108 i-18]=x+i y$

$\Rightarrow \quad-216+i-108 i+18=x+i y$

$\Rightarrow-198-107 i=x+i y$

$\Rightarrow \quad x=-198, y=-107$

$\Rightarrow \quad y-x=-107+198=91$

</details>

---

### Q19. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The least positive integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> for which <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>1</mn><mo>-</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup><mo>=</mo><mn>1</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

Given <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>1</mn><mo>-</mo><mi>i</mi><msqrt><mn>3</mn></msqrt></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup><mo>=</mo><mn>1</mn></math>

<mo>&rArr;</mo><math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mn>2</mn><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mo>-</mo><mn>2</mn><mi>&#969;</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup><mo>=</mo><mn>1</mn></math>

 <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math><math><msup><mrow><mi>&#969;</mi></mrow><mrow><mi>n</mi></mrow></msup><mo>=</mo><mn>1</mn></math>

Hence, the least positive integer value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>.

</details>

---

### Q20. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `1`

If $|z-3+2 i| \leq 4$ then the difference between the greatest value and the least value of $|z|$ is

**Options:**

- **(A)** $\sqrt{13}$
- **(B)** $2 \sqrt{13}$
- **(C)** 8
- **(D)** $4+\sqrt{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \sqrt{13}$**

**Detailed Solution:**

$|z-(3-2 i)| \leq 4$ represents a circle whose centre is $(3,-2)$ and radius $=4$.
$|z|=|z-0|$ represents the distance of point ' $z$ ' from origin $(0,0)$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4R4LF9hu88ha12Q0bSfH9LBCZHHtwgeIXGPPo_phgw8.original.fullsize.png">

Suppose $R S$ is the normal of the circle passing through origin ' $O$ ' and $G$ is its center $(3,-2)$
Here, $O R$ is the least distance and $O S$ is the greatest distance $O R=R G-O G$ and $O S=O G+G S \ldots(1)$ As, $R G=G S=4$ $O G=\sqrt{3^2+(-2)^2}=\sqrt{9+4}=\sqrt{13}$ From (1), $O R=4-\sqrt{13}$ and $O S=4+\sqrt{13}$ So, required difference
$$
\begin{aligned}
&=(4+\sqrt{13})-(4-\sqrt{13}) \\
&=\sqrt{13}+\sqrt{13}=2 \sqrt{13}
\end{aligned}
$$

</details>

---

### Q21. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `3`

The set of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi></math>, for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>8</mn><mi>&#945;</mi></mrow></mfenced><mi>z</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>z</mi></mrow></mfrac></math> is a purely imaginary number, for all <math><mi>z</mi><mo>&#8712;</mo><mi>C</mi></math> satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mi mathvariant="normal">e</mi><mfenced separators="|"><mi mathvariant="normal">z</mi></mfenced><mo>&#8800;</mo><mn>1</mn></math>, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mn>0</mn></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{" separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced></math>
- **(C)** equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>
- **(D)** an empty set

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mn>0</mn></mfenced></math>**

**Detailed Solution:**

<p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi></math> to be purely imaginary, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>8</mn><mi>&#945;</mi></mrow></mfenced><mi>z</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>z</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>8</mn><mi>&#945;</mi></mrow></mfenced><mover><mi>z</mi><mo>&#175;</mo></mover></mrow><mrow><mn>1</mn><mo>-</mo><mover><mi>z</mi><mo>&#175;</mo></mover></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>8</mn><mi>&#945;</mi></mrow></mfenced><mi>z</mi><mo>-</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>8</mn><mi>&#945;</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mo>-</mo><mi>z</mi><mo>+</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>8</mn><mi>&#945;</mi></mrow></mfenced><mover><mi>z</mi><mo>&#175;</mo></mover><mo>-</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>8</mn><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>-</mo><mfenced separators="|"><mrow><mi>z</mi><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>8</mn><mi>&#945;</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>z</mi><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover></mrow></mfenced><mo>-</mo><mn>2</mn><mo>+</mo><mn>16</mn><mi>&#945;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mi>&#945;</mi><mfenced separators="|"><mrow><mi>z</mi><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover></mrow></mfenced><mo>=</mo><mn>16</mn><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>+</mo><mover><mi>z</mi><mo>&#175;</mo></mover><mo>=</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>0</mn></math></p><p>For all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>&#8712;</mo><mi>C</mi></math>, we have <math><mi>&#945;</mi><mo>=</mo><mn>0</mn></math>.</p>

</details>

---

### Q22. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `3`

The set of all $\alpha \in R$, for which $w=\frac{1+(1-8 \alpha) z}{1-z}$ is a purely imaginary number, for all $z \in C$ satisfying $|z|=1$ and $\operatorname{Re} z \neq 1$, is

**Options:**

- **(A)** $\{0\}$
- **(B)** an empty set
- **(C)** $\left\{0, \frac{1}{4},-\frac{1}{4}\right\}$
- **(D)** equal to $R$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\{0\}$**

**Detailed Solution:**

$$
\begin{aligned}
&\because|z|=1 \text { \& } \operatorname{Re} z \neq 1 \\
&\text { Suppose } z=x+i y \Rightarrow x^2+y^2=1 \ldots \ldots(\mathrm{i}) \\
&\text { Now, } w=\frac{1+(1-8 \alpha) z}{1-z} \\
&\Rightarrow w=\frac{1+(1-8 \alpha)(x+i y)}{1-(x+i y)} \\
&\Rightarrow w=\frac{1+(1-8 \alpha)(x+i y))((1-\mathrm{x})+\mathrm{iy})}{1-(x+i y))((1-\mathrm{x})+\mathrm{iy})} \\
&\Rightarrow \quad w=\frac{\left[\left(1+x(1-8 \alpha)(1-x)-(1-8) y^2\right]\right.}{(1-x)^2+y^2} \\
&+i \frac{[(1+x(1-8 \alpha)) y-(1-8 \alpha) y(1-x)]}{(1-x)^2+y^2}
\end{aligned}
$$
If, $w$ is purely imaginary. So,
$$
\begin{aligned}
&\operatorname{Re} w=\frac{\left[(1+x(1-8 \alpha))(1-\alpha)-(1-8 \alpha) y^2\right]}{(1-x)^2+y^2} \\
&=0 \\
&\Rightarrow(1-x)+x(1-8 \alpha)(1-x)=(1-8) y^2 \\
&\Rightarrow(1-x)+x(1-8 \alpha)-x^2(1-8 \alpha)=(1-8 x) y^2 \\
&\Rightarrow(1-x)+x(1-8 \alpha)=1-8 \alpha \\
&{\left[\text { From }(i), x^2+y^2=1\right]}
\end{aligned}
$$
$\Rightarrow 1-8 \alpha=1$
$\Rightarrow \alpha=0$
$\therefore \alpha \in\{0\}$

</details>

---

### Q23. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The equation <math><mi>I</mi><mi>m</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>i</mi><mi>z</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>z</mi><mo>-</mo><mi>i</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>z</mi><mo>&#8712;</mo><mi>C</mi><mo>,</mo><mi>&#160;</mi><mi>z</mi><mo>&#8800;</mo><mi>i</mi></math> represents a part of a circle having radius equal to :

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mn>2</mn></math>
- **(C)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let <math> <mrow> <mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi><mo>,</mo></mrow> </math> then

<math><mi>I</mi><mi>m</mi><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>i</mi><mi>x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>i</mi></mrow></mfrac></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>-</mo><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>i</mi></mrow><mrow><mi>x</mi><mo>-</mo><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>i</mi></mrow></mfrac></mrow></mfenced></mrow></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>0</mn></math>

Center <math><mo>(</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>)</mo></math></p><p>Radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><msup><mi>g</mi><mn>2</mn></msup><mo>+</mo><msup><mi>f</mi><mn>2</mn></msup><mo>-</mo><mi>c</mi></msqrt></math>

Radius<math><mo>=</mo><mi>&#160;</mi><msqrt><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt><mo>=</mo><mi>&#160;</mi><msqrt><mfrac><mrow><mn>9</mn></mrow><mrow><mn>16</mn></mrow></mfrac></msqrt><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math></p>

</details>

---

### Q24. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mi>z</mi><mo>&#8712;</mo><mi>C</mi><mo>,</mo></math> the set of complex numbers. Then the equation, <math><mn>2</mn><mfenced close="|" open="|" separators="|"><mrow><mi>z</mi><mo>+</mo><mn>3</mn><mi>i</mi></mrow></mfenced><mo>-</mo><mfenced close="|" open="|" separators="|"><mrow><mi>z</mi><mo>-</mo><mi>i</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> represents:

**Options:**

- **(A)** A circle with radius <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** An ellipse with length of minor axis  <math><mfrac><mrow><mn>16</mn></mrow><mrow><mn>9</mn></mrow></mfrac></math>
- **(C)** An ellipse with length of major axis  <math><mfrac><mrow><mn>16</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** A circle with diameter  <math><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A circle with radius <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

Let <math> <mrow> <mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow> </math> so that

<math><mn>2</mn><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math>

<math><mo>&#8658;</mo><mn>2</mn><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mi>&#160;=&#160;</mi><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>

<math><mo>&#8658;</mo><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn><msup><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+26</mo><mi>y</mi><mo>+</mo><mn>35</mn><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>26</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>y</mi><mo>+</mo><mfrac><mrow><mn>35</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mi>&#160;</mi><msqrt><mn>0</mn><mo>+</mo><mfrac><mrow><mn>169</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>35</mn></mrow><mrow><mn>3</mn></mrow></mfrac></msqrt></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><msqrt><mfrac><mn>64</mn><mn>9</mn></mfrac></msqrt><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></math>

</details>

---

### Q25. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>&#969;</mi></math> be a complex number such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#969;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mi>z</mi></math> where <math><mi>z</mi><mo>=</mo><msqrt><mo>-</mo><mn>3</mn></msqrt></math> . If

<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mtd><mtd><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>7</mn></mrow></msup></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>3</mn><mi>k</mi><mo>,</mo></math>

Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> can be equal to:

**Options:**

- **(A)** <math><mo>–</mo><mi>z</mi></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>z</mi></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mn>1</mn></math>
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>–</mo><mi>z</mi></math>**

**Detailed Solution:**

<p><math><mi>&#969;</mi><mo>=</mo><mi>&#160;</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mi>&#160;</mi><mi>i</mi></math> (cube root of unity)

So, <math><mn>1</mn><mo>+</mo><mi>&#969;</mi><mo>+</mo><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math>  and  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>&#969;</mo><mn>3</mn></msup><mo>=1</mo></math>

Now <math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#969;</mi></mtd><mtd><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mi>&#969;</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>3</mn><mfenced separators="|"><mrow><msup><mrow><mi>&#969;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>&#969;</mi></mrow></mfenced></math>

So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><msup><mi>&#969;</mi><mn>2</mn></msup><mo>-</mo><mi>&#969;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>i</mi></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>i</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mo>-</mo><msqrt><mn>3</mn></msqrt><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mo>-</mo><mi>z</mi></math></p>

</details>

---

### Q26. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>z</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi>a</mi><mi>i</mi></math>, be a complex number, <math><mi>a</mi><mo>&#62;</mo><mn>0</mn></math>, such that <math><msup><mrow><mi>z</mi></mrow><mrow><mn>3</mn></mrow></msup></math> is a real number. Then, the sum <math><mn>1</mn><mo>+</mo><mi>z</mi><mo>+</mo><msup><mrow><mi>z</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mrow><mi>z</mi></mrow><mrow><mn>11</mn></mrow></msup></math> is equal to :

**Options:**

- **(A)** <math><mn>1365</mn><mi> </mi><msqrt><mn>3</mn></msqrt><mi>i</mi></math>
- **(B)** <math><mo>-</mo><mn>1365</mn><mi> </mi><msqrt><mn>3</mn></msqrt><mi>i</mi></math>
- **(C)** <math><mo>-</mo><mn>1250</mn><mi> </mi><msqrt><mn>3</mn></msqrt><mi>i</mi></math>
- **(D)** <math><mn>1250</mn><mi> </mi><msqrt><mn>3</mn></msqrt><mi>i</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mo>-</mo><mn>1365</mn><mi> </mi><msqrt><mn>3</mn></msqrt><mi>i</mi></math>**

**Detailed Solution:**

<math><mi>z</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi>a</mi><mi>i</mi></math>
Cubing both sides,
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>3</mn></msup><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mn>2</mn><mi>a</mi><mi>i</mi><mo>+</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mi>a</mi><mi>i</mi><mo>-</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>3</mn></msup><mo>=</mo><mn>1</mn><mo>-</mo><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mo>(</mo><mn>3</mn><mi>a</mi><mo>-</mo><msup><mi>a</mi><mn>3</mn></msup><mo>)</mo><mi>i</mi></math>
<math><mo>&#8757;</mo></math> <math><msup><mrow><mi>z</mi></mrow><mrow><mn>3</mn></mrow></msup></math> is a real number.
<math><mi>a</mi><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>=</mo><mn>0</mn><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>a</mi><mo>=</mo><mi>&#160;</mi><msqrt><mn>3</mn></msqrt></math> <math><mfenced separators="|"><mrow><mi>a</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math>

<math><mn>1</mn><mo>+</mo><mi>z</mi><mo>+</mo><msup><mrow><mi>z</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>&#8230;</mo><mo>.</mo><mo>.</mo><msup><mrow><mi>z</mi></mrow><mrow><mn>11</mn></mrow></msup><mo>=</mo><mfrac><mrow><msup><mrow><mi>z</mi></mrow><mrow><mn>12</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>&#160;</mi><msqrt><mn>3</mn></msqrt><mi>i</mi></mrow></mfenced></mrow><mrow><mn>12</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><mi>&#160;</mi><msqrt><mn>3</mn></msqrt><mi>i</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>&#160;</mi><msqrt><mn>3</mn></msqrt><mi>i</mi></mrow></mfenced></mrow><mrow><mn>12</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt><mi>i</mi></mrow></mfrac></math>

<math><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>&#160;</mi><msqrt><mn>3</mn></msqrt><mi>i</mi></mrow></mfenced></mrow><mrow><mn>12</mn></mrow></msup><mo>=</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>12</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mi>i</mi></mrow></mfenced></mrow><mrow><mn>12</mn></mrow></msup><mo>=</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>12</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mrow><mo>+</mo><mi>i</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mrow></mrow></mfenced></mrow><mrow><mn>12</mn></mrow></msup><mo>=</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>12</mn></mrow></msup><mi>&#160;</mi><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>4</mn><mi>&#960;</mi></mrow></mrow><mo>+</mo><mi>i</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>4</mn><mi>&#960;</mi></mrow></mrow></mrow></mfenced><mo>=</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>12</mn></mrow></msup></math>

 <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mn>12</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt><mi>i</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>1365</mn><msqrt><mn>3</mn></msqrt><mi>i</mi></math>

</details>

---

### Q27. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `2`

A value of <math><mi>&#952;</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mo>+</mo><mn>3</mn><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mrow></mfrac></math> is purely imaginary, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced></math>
- **(C)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mrow><mn>2&#160;</mn><mo>+&#160;</mo><mn>3</mn><mi>i</mi><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi></mrow><mrow><mn>1&#160;</mn><mo>-&#160;</mo><mn>2</mn><mi>i</mi><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi></mrow></mfrac></math></p><p>Multiplying the denominator by its conjugate, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mn>3</mn><mo>&#160;</mo><mi>i</mi><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi>i</mi><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mn>4</mn><mo>&#160;</mo><msup><mi>sin</mi><mn>2</mn></msup><mo>&#160;</mo><mi>&#952;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mn>6&#160;</mn><msup><mi>sin</mi><mn>2</mn></msup><mo>&#160;</mo><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mi>i</mi><mfenced separators="|"><mrow><mn>7</mn><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mn>4&#160;</mn><msup><mi>sin</mi><mn>2</mn></msup><mo>&#160;</mo><mi>&#952;</mi></mrow></mfrac></math></p><p>To make it purely imaginary. Its real part should be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>.</p><p>Hence, <math><mn>2</mn><mo>=</mo><mn>6&#160;</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mo>&#8289;</mo><mi>&#952;</mi><mo>=</mo><mo>&#177;</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p>

</details>

---

### Q28. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>z</mi></math> is a non-real complex number, then the minimum value of <math><mfrac><mrow><mi>I</mi><mi>m</mi><mo>&#160;</mo><msup><mi>z</mi><mn>5</mn></msup></mrow><msup><mfenced separators="|"><mrow><mi>I</mi><mi>m</mi><mo>&#160;</mo><mi>z</mi></mrow></mfenced><mn>5</mn></msup></mfrac></math> is (Where <math><mi>I</mi><mi>m</mi><mo>&#160;</mo><mi>z</mi><mo>&#160;</mo><mo>=</mo></math> Imaginary part of <math><mi>z</mi></math>)

**Options:**

- **(A)** <math><mo>-</mo><mn>2</mn></math>
- **(B)** <math><mo>-</mo><mn>4</mn></math>
- **(C)** <math><mo>-</mo><mn>5</mn></math>
- **(D)** <math><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mo>-</mo><mn>4</mn></math>**

**Detailed Solution:**

<p>Let, <math><mrow><mi>z</mi><mo>=</mo><mi>r</mi><mo stretchy="false">(</mo><mtext>cos</mtext><mi>&#952;</mi><mo>+</mo><mi>i</mi><mtext>sin</mtext><mi>&#952;</mi><mo stretchy="false">)</mo></mrow> </math>

<math> <mrow> <msup> <mi>z</mi> <mn>5</mn> </msup> <mo>=</mo><msup> <mi>r</mi> <mn>5</mn> </msup> <mo stretchy="false">(</mo><mtext>cos</mtext><mn>5</mn><mi>&#952;</mi><mo>+</mo><mi>i</mi><mtext>sin</mtext><mn>5</mn><mi>&#952;</mi><mo stretchy="false">)</mo></mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>m</mi><mfenced><msup><mi>z</mi><mn>5</mn></msup></mfenced><mo>=</mo><msup><mi>r</mi><mn>5</mn></msup><mi>sin</mi><mn>5</mn><mi>&#952;</mi></math>

and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mi>I</mi><mi>m</mi><mi>&#160;</mi><mi>z</mi></mrow></mfenced><mn>5</mn></msup><mo>=</mo><msup><mi>r</mi><mn>5</mn></msup><msup><mi>sin</mi><mn>5</mn></msup><mi>&#952;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>I</mi><mi>m</mi><mi>&#160;</mi><mo>(</mo><msup><mi>z</mi><mn>5</mn></msup><mo>)</mo></mrow><msup><mfenced separators="|"><mrow><mi>I</mi><mi>m</mi><mi>&#160;</mi><mi>z</mi></mrow></mfenced><mn>5</mn></msup></mfrac><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mi>sin</mi><mn>5</mn><mi>&#952;</mi></mrow><mrow><msup><mi>sin</mi><mn>5</mn></msup><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mi>A&#160;</mi></math>(Let)

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><msup><mi>sin</mi><mn>5</mn></msup><mi>&#952;</mi><mi>cos</mi><mn>5</mn><mi>&#952;</mi><mo>-</mo><mn>5</mn><mi>sin</mi><mn>5</mn><mi>&#952;</mi><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mi>cos</mi><mi>&#952;</mi></mrow><msup><mfenced separators="|"><mrow><msup><mi>sin</mi><mn>5</mn></msup><mi>&#952;</mi></mrow></mfenced><mn>2</mn></msup></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mfenced separators="|"><mrow><mi>sin</mi><mi>&#952;</mi><mi>cos</mi><mn>5</mn><mi>&#952;</mi><mo>-</mo><mi>sin</mi><mn>5</mn><mi>&#952;</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfenced></mrow><mrow><msup><mi>sin</mi><mn>10</mn></msup><mi>&#952;</mi></mrow></mfrac></math>

<math> <mrow> <mo>&#8658;</mo><mfrac> <mrow> <mi>d</mi><mi>A</mi></mrow> <mrow> <mi>d</mi><mi>&#952;</mi></mrow> </mfrac> <mo>=</mo><mfrac> <mn>5</mn> <mrow> <msup> <mrow> <mi>sin</mi></mrow> <mn>6</mn> </msup> <mi>&#952;</mi></mrow> </mfrac> <mfenced close="]" open="["> <mrow> <mi>sin</mi><mfenced> <mrow> <mo>&#8722;</mo><mn>4</mn><mi>&#952;</mi></mrow> </mfenced></mrow> </mfenced><mo>=</mo><mn>0</mn></mrow> </math>

<math><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>

The minimum value of <math><mi>A</mi></math> will be at  <math><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>.</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mrow><mi>sin</mi><mn>5</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow><msup><mfenced separators="|"><mrow><mi>sin</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mn>5</mn></msup></mfrac></math>
<math><mo>=</mo><mfrac><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><msup><mfenced separators="|"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mn>5</mn></msup></mfrac></math>

<math><mo>=</mo><mo>-</mo><msup><mfenced separators="|"><msqrt><mn>2</mn></msqrt></mfenced><mn>4</mn></msup><mo>=</mo><mo>-</mo><mn>4</mn></math></p>

</details>

---

### Q29. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mn>2</mn><mo>+</mo><mn>3</mn><mi>i</mi></math> is one of the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>k</mi><mi>x</mi><mo>-</mo><mn>13</mn><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>k</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> then the real root of this equation (where <math><msup><mrow><mi>i</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mo>-</mo><mn>1</mn></math>) :

**Options:**

- **(A)** Exists and is equal to <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** Does not exist
- **(C)** Exists and is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** Exists and is equal to  <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Exists and is equal to <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>If <math><mn>2</mn><mo>+</mo><mn>3</mn><mi>i</mi></math> in one of the roots, then <math><mn>2</mn><mo>-</mo><mn>3</mn><mi>i</mi></math> would be other.
Since coefficients of the equation are real.</p><p>Let <math><mi>&#947;</mi></math> be the third root, then product of roots <math><mo>&#8594;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#945;</mi><mi>&#160;</mi><mi>&#946;</mi><mi>&#160;</mi><mi>&#947;</mi><mi>&#160;</mi><mo>=</mo><mfrac><mrow><mn>13</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mn>3</mn><mi>i</mi></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mn>3</mn><mi>i</mi></mrow></mfenced><mi>&#160;</mi><mo>&#8901;</mo><mi>&#947;</mi><mo>=</mo><mfrac><mrow><mn>13</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mi>&#160;</mi><mfenced separators="|"><mrow><mn>4</mn><mo>+</mo><mn>9</mn></mrow></mfenced><mo>&#8901;</mo><mi>&#947;</mi><mo>=</mo><mfrac><mrow><mn>13</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#947;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

The value of k will come if we put <math><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> in the equation
<math><mn>2</mn><mo>&#8901;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mi>k</mi><mo>&#8901;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>13</mn><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>k</mi><mn>2</mn></mfrac><mo>=</mo><mn>15</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>30</mn></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi></math> Equation will become <math><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>9</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>30</mn><mi>x</mi><mo>-</mo><mn>13</mn><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>+</mo><mi>&#946;</mi><mi>&#947;</mi><mo>+</mo><mi>&#947;</mi><mi>&#945;</mi><mo>=</mo><mfrac><mn>30</mn><mn>2</mn></mfrac><mo>=</mo><mn>15</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mn>3</mn><mi>i</mi></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mn>3</mn><mi>i</mi></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mn>3</mn><mi>i</mi></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mn>3</mn><mi>i</mi></mrow></mfenced><mo>=</mo><mn>15</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><mfrac><mi>i</mi><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>-</mo><mfrac><mi>i</mi><mn>2</mn></mfrac><mo>+</mo><mn>13</mn><mo>=</mo><mn>15</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>15</mn><mo>=</mo><mn>15</mn><mi>&#160;</mi></math>
Hence roots exists and is equal to <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> &#39;</p>

</details>

---

### Q30. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

For all complex numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>i</mi><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi><mo>,</mo></math> then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi mathvariant="italic">i&#945;</mi><mo>,</mo><mo>&#160;</mo><msup><mi>z</mi><mn>2</mn></msup><mo>=</mo><mi>x</mi><mo>+</mo><mi mathvariant="italic">iy</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi mathvariant="italic">i&#945;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mi>x</mi><mo>+</mo><mi mathvariant="italic">iy</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mi>i</mi><mn>2</mn></msup><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>i</mi><mi>&#945;</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>i</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>i</mi><mi>&#945;</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi mathvariant="italic">iy</mi></math></p><p>Equating the real and imaginary parts, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup></math> and <math><mi>y</mi><mo>=</mo><mn>2</mn><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>-</mo><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><msup><mi>&#945;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>-</mo><mn>4</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>.</mo></math></p>

</details>

---

### Q31. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $z \neq-i$ be any complex number such that $\frac{\mathrm{z}-\mathrm{i}}{\mathrm{z}+\mathrm{i}}$ is a purely imaginary number.
Then $\mathrm{z}+\frac{1}{\mathrm{z}}$ is:

**Options:**

- **(A)** 0
- **(B)** any non-zero real number other than 1 .
- **(C)** any non-zero real number.
- **(D)** a purely imaginary number.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) any non-zero real number.**

**Detailed Solution:**

Let $z=x+i y$
$\frac{z-i}{z+i}$ is purely imaginary means its real part is zero.
$$
\begin{aligned}
&\frac{x+i y-i}{x+i y+i}=\frac{x+i(y-1)}{x+i(y+1)} \times \frac{x-i(y+1)}{x-i(y+1)} \\
&=\frac{x^2-2 i x(y+1)+x i(y-1)+y^2-1}{x^2+(y+1)^2} \\
&=\frac{x^2+y^2-1}{x^2+(y+1)^2}-\frac{2 x i}{x^2+(y+1)^2}
\end{aligned}
$$
for pure imaginary, we have
$$
\begin{aligned}
& \frac{x^2+y^2-1}{x^2+(y+1)^2}=0 \\
\Rightarrow & x^2+y^2=1 \\
\Rightarrow &(x+i y)(x-i y)=1 \\
\Rightarrow & x+i y=\frac{1}{x-i y}=z
\end{aligned}
$$
and $\frac{1}{z}=x-i y$
$$
z+\frac{1}{z}=(x+i y)+(x-i y)=2 x
$$
$\left(z+\frac{1}{z}\right)$ is any non-zero real number

</details>

---

### Q32. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi><mfenced><mrow><mi>I</mi><mi>m</mi><mo>&#160;</mo><mi>w</mi><mo>&#8800;0</mo></mrow></mfenced></math> be a complex number. Then, the set of all complex numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> satisfying the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi><mo>-</mo><mover><mi>w</mi><mo>&#175;</mo></mover><mi>z</mi><mo>=</mo><mi>k</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>z</mi></mrow></mfenced></math>, for some real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">k</mo></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>z</mi><mo>:</mo><mo>&#160;</mo><mi>z</mi><mo>&#8800;</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>z</mi><mo>:</mo><mo>&#160;</mo><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>&#8800;</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>z</mi><mo>:</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mover><mi>z</mi><mo>&#175;</mo></mover></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>z</mi><mo>:</mo><mo>&#160;</mo><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>=</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>z</mi><mo>:</mo><mo>&#160;</mo><mfenced open="|" close="|"><mi>z</mi></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>&#8800;</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi><mo>&#8712;</mo><mi>C</mi></math>,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>I</mi><mi>m</mi><mo>&#160;</mo><mi>w</mi><mo>&#8800;</mo><mn>0</mn></mrow></mfenced><mo>&#160;&#8658;</mo><mi>w</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>i</mi><mi>b</mi><mo>:</mo><mi>b</mi><mo>&#8800;0</mo></math> (suppose)

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi><mo>-</mo><mover><mi>w</mi><mo>&#175;</mo></mover><mo>&#160;</mo><mi>z</mi><mo>=</mo><mi>k</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>z</mi></mrow></mfenced></math>

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>i</mi><mi>b</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mi>i</mi><mi>b</mi></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mo>=</mo><mi>k</mi><mo>{</mo><mn>1</mn><mo>-</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>i</mi><mi>y</mi></mrow></mfenced><mo>}</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>i</mi><mi>b</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mi>i</mi><mi>a</mi><mi>y</mi><mo>-</mo><mi>i</mi><mi>b</mi><mi>x</mi><mo>+</mo><mi>b</mi><mi>y</mi></mrow></mfenced><mo>=</mo><mi>k</mi><mo>-</mo><mi>k</mi><mi>x</mi><mo>-</mo><mi>i</mi><mi>k</mi><mi>y</mi></math>

Equating real and imaginary parts

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>a</mi><mi>x</mi><mo>-</mo><mi>b</mi><mi>y</mi><mo>=</mo><mi>k</mi><mo>-</mo><mi>k</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>(</mo><mn>1</mn><mo>)</mo></math>

and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>-</mo><mi>a</mi><mi>y</mi><mo>+</mo><mi>b</mi><mi>x</mi><mo>=</mo><mo>-</mo><mi>k</mi><mi>y</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced separators="|"><mn>2</mn></mfenced></math>

From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mn>1</mn></mfenced><mo>&#160;</mo><mfenced separators="|"><mrow><mi>k</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>b</mi><mi>y</mi></math>

 <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mn>2</mn></mfenced><mo>&#160;</mo><mfenced separators="|"><mrow><mi>k</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mi>y</mi><mo>=</mo><mi>b</mi><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></math>
Dividing the two equations, we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mi>y</mi></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>=</mo><msup><mi>y</mi><mn>2</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8658;</mi><mfenced close="|" open="|"><mi>z</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>&#8800;</mo><mn>1</mn><mo>+</mo><mi>i</mi><mn>0</mn></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>z</mi><mo>=</mo><mn>1</mn></math> then from original equation   <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi><mo>=</mo><menclose notation="top"><mi>w</mi></menclose><mo>&#160;</mo><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>i</mi><mi>b</mi><mo>=</mo><mi>a</mi><mo>-</mo><mi>i</mi><mi>b</mi><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>0</mn></math>)</p>

</details>

---

### Q33. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let $a=\operatorname{Im}\left(\frac{1+z^2}{2 i z}\right)$, where $z$ is any non-zero complex number. The set $\mathrm{A}=\{a:|z|=1$ and $z \neq \pm 1\}$ is equal to:

**Options:**

- **(A)** $(-1,1)$
- **(B)** $[-1,1]$
- **(C)** $[0,1)$
- **(D)** $(-1,0]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-1,1)$**

**Detailed Solution:**

Let $z=x+i y \Rightarrow z^2=x^2-y^2+2 i x y$ Now,
$$
\begin{aligned}
& \frac{1+z^2}{2 i z}=\frac{1+x^2-y^2+2 i x y}{2 i(x+i y)}=\frac{\left(x^2-y^2+1\right)+2 i x y}{2 i x-2 y} \\
& =\frac{\left(x^2-y^2+1\right)+2 i x y}{-2 y+2 i x} \times \frac{-2 y-2 i x}{-2 y-2 i x} \\
& =\frac{y\left(x^2+y^2-1\right)+x\left(x^2+y^2+1\right) i}{2\left(x^2+y^2\right)} \\
&
\end{aligned}
$$

$$
a=\frac{x\left(x^2+y^2+1\right)}{2\left(x^2+y^2\right)}
$$
Since, $|z|=1 \Rightarrow \sqrt{x^2+y^2}=1$
$$
\begin{aligned}
& \Rightarrow x^2+y^2=1 \\
& \therefore a=\frac{x(1+1)}{2 \times 1}=x \\
& \text { Also } z \neq 1 \Rightarrow x+i y \neq 1 \\
& \therefore \mathrm{A}=(-1,1)
\end{aligned}
$$

</details>

---

### Q34. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If a complex number $z$ statisfies the equation $x+\sqrt{2}|z+1|+i=0$, then $|z|$ is equal to :

**Options:**

- **(A)** 2
- **(B)** $\sqrt{3}$
- **(C)** $\sqrt{5}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{5}$**

**Detailed Solution:**

Given equation is
$$
\begin{aligned}
& z+\sqrt{2}|z+1|+i=0 \\
& \text { put } z=x+i y \text { in the given equation. } \\
& (x+i y)+\sqrt{2}|x+i y+1|+i=0 \\
& \Rightarrow x+i y+\sqrt{2}\left[\sqrt{(x+1)^2+y^2}\right]+i=0
\end{aligned}
$$
Now, equating real and imaginary part, we get
$$
\begin{aligned}
& x+\sqrt{2} \sqrt{(x+1)^2+y^2}=0 \text { and } \\
& y+1=0 \Rightarrow y=-1 \\
& \Rightarrow x+\sqrt{2} \sqrt{(x+1)^2+(-1)^2}=0 \\
& \Rightarrow \sqrt{2} \sqrt{(x+1)^2+1}=-x \\
& \Rightarrow 2\left[(x+1)^2+1\right]=x^2 \\
& \Rightarrow x^2+4 x+4=0 \\
& \Rightarrow x=-2
\end{aligned}
$$
Thus, $z=-2+i(-1) \Rightarrow|z|=\sqrt{5}$

</details>

---

### Q35. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $Z_1 \neq 0$ and $Z_2$ be two complex numbers such that $\frac{Z_2}{Z_1}$ is a purely imaginary number, then $\left|\frac{2 Z_1+3 Z_2}{2 Z_1-3 Z_2}\right|$ is equal to:

**Options:**

- **(A)** 2
- **(B)** 5
- **(C)** 3
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

Let $z_1=1+i$ and $z_2=1-i$
$\frac{z_2}{z_1}=\frac{1-i}{1+i}=\frac{(1-i)(1-i)}{(1+i)(1-i)}=-i$
$\frac{2 z_1+3 z_2}{2 z_1-3 z_2}=\frac{2+3\left(\frac{z_2}{z_1}\right)}{2-3\left(\frac{z_2}{z_1}\right)}=\frac{2-3 i}{2+3 i}$
$\left|\frac{2 z_1+3 z_2}{2 z_1-3 z_2}\right|=\left|\frac{2-3 i}{2+3 i}\right|=\left|\frac{2-3 i}{2+3 i}\right|$
$\left[\because\left|\frac{z_1}{z_2}\right|=\frac{\left|z_1\right|}{\left|z_2\right|}\right]$
$=\frac{\sqrt{4+9}}{\sqrt{4+9}}=1$

</details>

---

### Q36. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

$\left|z_1+z_2\right|^2+\left|z_1-z_2\right|^2$ is equal to

**Options:**

- **(A)** $2\left(\left|z_1\right|+\left|z_2\right|\right.$
- **(B)** $2\left(\left|z_1\right|^2+\left|z_2\right|^2\right)$
- **(C)** $\left|z_1\right|\left|z_2\right|$
- **(D)** $\left|z_1\right|^2+\left|z_2\right|^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2\left(\left|z_1\right|^2+\left|z_2\right|^2\right)$**

**Detailed Solution:**

$\left|z_1+z_2\right|^2+\left|z_1-z_2\right|^2$
$$
=\left|z_1\right|^2+\left|z_2\right|^2+2\left|z_1\right|\left|z_2\right|+\left|z_1\right|^2+\left|z_2\right|^2-2\left|z_1\right|\left|z_2\right|
$$
$$
=2\left|z_1\right|^2+2\left|z_2\right|^2=2\left[\left|z_1\right|^2+\left|z_2\right|^2\right]
$$

</details>

---

### Q37. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `3`

Let $Z_1$ and $Z_2$ be any two complex number.
Statement 1: $\left|Z_1-Z_2\right| \geq\left|Z_1\right|-\left|Z_2\right|$
Statement 2: $\left|Z_1+Z_2\right| \leq\left|Z_1\right|+\left|Z_2\right|$

**Options:**

- **(A)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation of Statement 1.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation of Statement 1.
- **(C)** Statement 1 is true, Statement 2 is false.
- **(D)** Statement 1 is false, Statement 2 is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation of Statement 1.**

**Detailed Solution:**

Statement $-1$ and 2 both are true.
It is fundamental property.
But Statement - 2 is not correct explanation for Statement $-1$.

</details>

---

### Q38. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha, \beta$ be real and $z$ be a complex number. If $z^2+\alpha z+\beta=0$ has two distinct roots on the line $\operatorname{Re} z=1$, then it is necessary that

**Options:**

- **(A)** $\beta \in(-1,0)$
- **(B)** $|\beta|=1$
- **(C)** $\beta \in(1, \infty)$
- **(D)** $\beta \in(0,1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\beta \in(1, \infty)$**

**Detailed Solution:**

Suppose roots are $1+\mathrm{pi}, 1+\mathrm{qi}$
Sum of roots $1+p i+1+q i=-\alpha$ which is real $\Rightarrow$ roots of $1+\mathrm{pi}, 1-\mathrm{pi}$
Product of roots $=\beta=1+p^2 \in(1, \infty)$
$\mathrm{p} \neq 0$ since roots are distinct.

</details>

---

### Q39. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `2`

The number of complex numbers $z$ such that $|z-1|=|z+1|=|z-i|$ equals

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** $\infty$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Let $z=x+i y$
$$
\begin{array}{lll}
|z-1|=|z+1| & \Rightarrow \operatorname{Re} z=0 & \Rightarrow x=0 \\
|z-1|=|z-i| & \Rightarrow x=y & \\
|z+1|=|z-i| & \Rightarrow y=-x &
\end{array}
$$
Only $(0,0)$ will satisfy all conditions.
$\Rightarrow$ Number of complex number $z=1$

</details>

---

### Q40. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

If $\left|z-\frac{4}{z}\right|=2$, then the maximum value of $|z|$ is equal to

**Options:**

- **(A)** $\sqrt{3}+1$
- **(B)** $\sqrt{5}+1$
- **(C)** 2
- **(D)** $2+\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{5}+1$**

**Detailed Solution:**

$$
\begin{aligned}
& |z|=\left|\left(z-\frac{4}{z}\right)+\frac{4}{z}\right| \Rightarrow|z|=\left|z-\frac{4}{z}+\frac{4}{z}\right| \\
& \Rightarrow|z| \leq\left|z-\frac{4}{z}\right|+\frac{4}{|z|} \Rightarrow|z| \leq 2+\frac{4}{|z|}
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow|z|^2-2|z|-4 \leq 0 \\
& (|z|-(\sqrt{5}+1))(|z|-(1-\sqrt{5})) \leq 0 \Rightarrow 1-\sqrt{5} \leq|z| \leq \sqrt{5}+1
\end{aligned}
$$

</details>

---

### Q41. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

If $\omega=\frac{z}{z-\frac{1}{3} i}$ and $|\omega|=1$, then $z$ lies on

**Options:**

- **(A)** an ellipse
- **(B)** a circle
- **(C)** a straight line
- **(D)** a parabola.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) a straight line**

**Detailed Solution:**

As given $w=\frac{z}{z-\frac{1}{3} i} \Rightarrow|w|=\frac{|z|}{\left|z-\frac{1}{3} i\right|}=1 \Rightarrow$ distance of $z$ from origin and point
$\left(0, \frac{1}{3}\right)$ is same hence $z$ lies on bisector of the line joining points $(0,0)$ and $(0,1 / 3)$.
Hence $z$ lies on a straight line.

</details>

---

### Q42. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

If $z=x-i y$ and $z^{\frac{1}{3}}=p+i q$, then $\frac{\left(\frac{x}{p}+\frac{y}{q}\right)}{\left(p^2+q^2\right)}$ is equal to

**Options:**

- **(A)** 1
- **(B)** $-2$
- **(C)** 2
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-2$**

**Detailed Solution:**

$z=(p+i q)^3=p\left(p^2-3 q^2\right)-i q\left(q^2-3 p^2\right)$
$\Rightarrow \frac{x}{p}=p^2-3 q^2 \& \frac{y}{q}=q^2-3 p^2 \Rightarrow \frac{\frac{x}{p}+\frac{y}{q}}{\left(p^2+q^2\right)}=-2$

</details>

---

### Q43. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

If $\left(\frac{1+i}{1-i}\right)^x=1$ then

**Options:**

- **(A)** $x=2 n+1$, where $n$ is any positive integer
- **(B)** $x=4 n$, where $n$ is any positive integer
- **(C)** $x=2 n$, where $n$ is any positive integer
- **(D)** $x=4 n+1$, where $n$ is any positive integer

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x=4 n$, where $n$ is any positive integer**

**Detailed Solution:**

$\left(\frac{1+\mathrm{i}}{1-\mathrm{i}}\right)^{\mathrm{x}}=1 \Rightarrow\left[\frac{(1+\mathrm{i})}{1-\mathrm{i}^2}\right]^{\mathrm{x}}=1$
$\left(\frac{1+\mathrm{i}^2+2 \mathrm{i}}{1+1}\right)^{\mathrm{x}}=1 \Rightarrow(\mathrm{i})^{\mathrm{x}}=1 ; \quad \therefore \mathrm{x}=4 \mathrm{n} ; \mathrm{n} \in 1^{+}$

</details>

---

### Q44. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

If $|z-4| < |z-2|$, its solution is given by

**Options:**

- **(A)** Re(z) > 0
- **(B)** Re(z)  < 0
- **(C)** Re (z) > 3
- **(D)** Re(z) > 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Re (z) > 3**

**Detailed Solution:**

Given $|z-4| < |z-2|$ Let $z=x+$ iy
$$
\begin{aligned}
& \Rightarrow \mid(x-4)+i y)| < |(x-2)+i y \mid \Rightarrow(x-4)^2+y^2 < (x-2)^2+y^2 \\
& \Rightarrow x^2-8 x+16 < x^2-4 x+4 \Rightarrow 12 < 4 x \Rightarrow x>3 \Rightarrow \operatorname{Re}(z)>3
\end{aligned}
$$

</details>

---

