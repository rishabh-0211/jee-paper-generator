# JEE Main Mathematics - Inverse Trigonometric Functions

## Topic 1: Principal Value and Basics

**Total Questions:** 18

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha = 3\sin^{-1}\left(\dfrac{6}{11}\right)$ and $\beta = 3\cos^{-1}\left(\dfrac{4}{9}\right)$, where inverse trigonometric functions take only the principal values.
Given below are two statements:
Statement I: $\cos(\alpha+\beta) > 0$.
Statement II: $\cos(\alpha) < 0$.
In the light of the above statements, choose the correct answer from the options given below:

**Options:**

- **(A)** Both Statement I and Statement II are true
- **(B)** Both Statement I and Statement II are false
- **(C)** Statement I is true but Statement II is false
- **(D)** Statement I is false but Statement II is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Both Statement I and Statement II are true**

**Detailed Solution:**

We are given $\alpha = 3\sin^{-1}\left(\dfrac{6}{11}\right)$ and $\beta = 3\cos^{-1}\left(\dfrac{4}{9}\right)$.

First, we find the range of $\alpha$.
Since $\dfrac{1}{2} < \dfrac{6}{11} < \dfrac{1}{\sqrt{2}}$, we have $\sin^{-1}\left(\dfrac{1}{2}\right) < \sin^{-1}\left(\dfrac{6}{11}\right) < \sin^{-1}\left(\dfrac{1}{\sqrt{2}}\right)$.
$\Rightarrow \dfrac{\pi}{6} < \sin^{-1}\left(\dfrac{6}{11}\right) < \dfrac{\pi}{4}$
Multiplying by $3$, we get $\dfrac{\pi}{2} < \alpha < \dfrac{3\pi}{4}$.
Since $\alpha$ lies in the second quadrant, $\cos(\alpha) < 0$. Thus, Statement II is true.

Next, we find the range of $\beta$.
Since $0 < \dfrac{4}{9} < \dfrac{1}{2}$ and $\cos^{-1}(x)$ is a decreasing function, we have $\cos^{-1}\left(\dfrac{1}{2}\right) < \cos^{-1}\left(\dfrac{4}{9}\right) < \cos^{-1}(0)$.
$\Rightarrow \dfrac{\pi}{3} < \cos^{-1}\left(\dfrac{4}{9}\right) < \dfrac{\pi}{2}$
Multiplying by $3$, we get $\pi < \beta < \dfrac{3\pi}{2}$.
Thus, $\beta$ lies in the third quadrant.

Now, we determine the sign of $\cos(\alpha+\beta)$.
Adding the inequalities for $\alpha$ and $\beta$:
$\dfrac{\pi}{2} + \pi < \alpha + \beta < \dfrac{3\pi}{4} + \dfrac{3\pi}{2}$
$\Rightarrow \dfrac{3\pi}{2} < \alpha + \beta < \dfrac{9\pi}{4}$
The angle $(\alpha + \beta)$ lies in the interval $\left(\dfrac{3\pi}{2}, \dfrac{9\pi}{4}\right)$, which covers the fourth quadrant and a part of the first quadrant. In both of these regions, the cosine function is strictly positive.
Therefore, $\cos(\alpha+\beta) > 0$. Thus, Statement I is true.

Both Statement I and Statement II are true.

Answer: Both Statement I and Statement II are true

</details>

---

### Q2. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $[\cdot]$ denote the greatest integer function. If the domain of the function $f(x) = \sin^{-1}\left(\dfrac{x+[x]}{3}\right)$ is $[\alpha, \beta)$, then $\alpha^2 + \beta^2$ is equal to:

**Options:**

- **(A)** $2$
- **(B)** $5$
- **(C)** $10$
- **(D)** $13$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $5$**

**Detailed Solution:**

For the function $f(x) = \sin^{-1}\left(\dfrac{x+[x]}{3}\right)$ to be defined, the argument of the inverse sine function must lie in the interval $[-1, 1]$.

$-1 \le \dfrac{x+[x]}{3} \le 1$

$-3 \le x + [x] \le 3$

Using the fractional part function $\{x\}$, we can write $x = [x] + \{x\}$, where $0 \le \{x\} < 1$. Substituting this into the inequality gives:

$-3 \le 2[x] + \{x\} \le 3$

We analyze the possible integer values for $[x]$:

If $[x] \le -2$, then $2[x] + \{x\} \le -4 + \{x\} < -3$, which does not satisfy the inequality.

If $[x] = -1$, then $2[x] + \{x\} = -2 + \{x\}$. Since $0 \le \{x\} < 1$, we have $-2 \le -2 + \{x\} < -1$, which satisfies the inequality. This gives $x \in [-1, 0)$.

If $[x] = 0$, then $2[x] + \{x\} = \{x\}$. Since $0 \le \{x\} < 1$, this satisfies the inequality. This gives $x \in [0, 1)$.

If $[x] = 1$, then $2[x] + \{x\} = 2 + \{x\}$. Since $0 \le \{x\} < 1$, we have $2 \le 2 + \{x\} < 3$, which satisfies the inequality. This gives $x \in [1, 2)$.

If $[x] \ge 2$, then $2[x] + \{x\} \ge 4 + \{x\} \ge 4 > 3$, which does not satisfy the inequality.

Taking the union of the valid intervals, the domain of $f(x)$ is $[-1, 0) \cup [0, 1) \cup [1, 2) = [-1, 2)$.

Comparing this with the given domain $[\alpha, \beta)$, we get $\alpha = -1$ and $\beta = 2$.

Therefore, $\alpha^2 + \beta^2 = (-1)^2 + (2)^2 = 1 + 4 = 5$.

Answer: $5$

</details>

---

### Q3. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the domain of the function $f(x)=\sin ^{-1}\left(\frac{1}{x^{2}-2 x-2}\right)$, is $(-\infty, \alpha] \cup[\beta, \gamma] \cup[\delta, \infty)$, then $\alpha+\beta+\gamma+\delta$ is equal to

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** 4
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

For $\sin^{-1}\left(\frac{1}{x^2-2x-2}\right)$ to be defined, we need $\left|\frac{1}{x^2-2x-2}\right| \leq 1$, i.e., $|x^2-2x-2| \geq 1$.
Case 1:
$x^2-2x-2 \geq 1 \Rightarrow x^2-2x-3 \geq 0$
$\Rightarrow (x-3)(x+1) \geq 0$
$\Rightarrow x \leq -1$ or $x \geq 3$.
Case 2:
$x^2-2x-2 \leq -1 \Rightarrow x^2-2x-1 \leq 0$
$\Rightarrow (x-1)^2 \leq 2$
$\Rightarrow 1-\sqrt{2} \leq x \leq 1+\sqrt{2}$.
Domain $= (-\infty, -1] \cup [1-\sqrt{2}, 1+\sqrt{2}] \cup [3, \infty)$.
So $\alpha = -1,\ \beta = 1-\sqrt{2},\ \gamma = 1+\sqrt{2},\ \delta = 3$.
$\alpha + \beta + \gamma + \delta = -1 + 1 - \sqrt{2} + 1 + \sqrt{2} + 3 = 4$.

</details>

---

### Q4. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the domain of the function $f(x)=\cos ^{-1}\left(\frac{2 x-5}{11-3 x}\right)+\sin ^{-1}\left(2 x^{2}-3 x+1\right)$ is the interval $[\alpha, \beta]$, then $\alpha+2 \beta$ is equal to :

**Options:**

- **(A)** 3
- **(B)** 5
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

For $\cos^{-1}\left(\frac{2x-5}{11-3x}\right)$: $-1 \leq \frac{2x-5}{11-3x} \leq 1$ gives $x \leq \frac{16}{5}$ or $x > 6$.
For $\sin^{-1}(2x^2 - 3x + 1)$: $-1 \leq 2x^2 - 3x + 1 \leq 1$.
Lower bound always satisfied (discriminant $< 0$).
Upper bound gives $x(2x-3) \leq 0$, so $0 \leq x \leq \frac{3}{2}$.
Intersection of both conditions: $[0, \frac{3}{2}]$.
Thus $\alpha = 0$, $\beta = \frac{3}{2}$.
$\alpha + 2\beta = 0 + 3 = 3$.

</details>

---

### Q5. JEE Main 2025 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

If for some $\alpha, \beta ; \alpha \leq \beta, \alpha+\beta-8$ and $\sec ^2\left(\tan ^{-1} \alpha\right)+\operatorname{cosec}^2\left(\cot ^{-1} \beta\right)-36$, then $\alpha^2+\beta$ is_______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

$\begin{aligned}
& \text { Let } \tan ^{-1} \alpha=A \Rightarrow \tan A=\alpha \\
& \cot ^{-1} \beta=B \Rightarrow \cot B=\beta \\
& \sec ^2 A+\operatorname{cosec}^2 B=36 \\
& \Rightarrow 1+\tan ^2 A+1+\cot ^2 B=36 \\
& \Rightarrow \alpha^2+\beta^2=34
\end{aligned}$

Also $\alpha+\beta=8$ (Given)
$\begin{aligned}
& \therefore(\alpha+\beta)^2=34+2 \alpha \beta=64 \\
& \Rightarrow \alpha \beta=15
\end{aligned}$
$\Rightarrow \alpha, \beta$ are roots of equation
$\begin{aligned}
& x^2-8 x+15=0 \\
& \Rightarrow(x-3)(x-5)=0 \\
& \Rightarrow \quad x=3,5 \\
& \therefore \quad \alpha=3, \beta=5 \quad(\alpha < \beta) \\
& \therefore \quad \alpha^2+\beta=9+5=14
\end{aligned}$

</details>

---

### Q6. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given that the inverse trigonometric function assumes principal values only. Let $x$, $y$ be any two real numbers in $[-1,1]$ such that $\cos ^{-1} x-\sin ^{-1} y=\alpha, \frac{-\pi}{2} \leq \alpha \leq \pi$.
Then, the minimum value of $x^2+y^2+2 x y \sin \alpha$ is

**Options:**

- **(A)** 0
- **(B)** -1
- **(C)** $\frac{1}{2}$
- **(D)** $-\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

$\begin{aligned}
& \cos ^{-1} x-\left(\frac{\pi}{2}-\cos ^{-1} y\right)=\alpha \\
& \cos ^{-1} x+\cos ^{-1} y=\frac{\pi}{2}+\alpha \\
& \alpha \in\left[-\frac{\pi}{2}, \pi\right], \frac{\pi}{2}+\alpha \in\left[0, \frac{3 \pi}{2}\right] \\
& \cos ^{-1}\left(x y-\sqrt{1-x^2} \sqrt{1-y^2}\right)=\frac{\pi}{2}+\alpha \\
& x y-\sqrt{1-x^2} \sqrt{1-y^2}=-\sin \alpha \\
& (x y+\sin \alpha)=\left(1-x^2\right)\left(1-y^2\right) \\
& x^2 y^2+2 x y \sin a+\sin ^2 a=1-x^2-y^2+x^2 y^2 \\
& x^2+y^2+2 x y \sin \alpha=1-\sin ^2 \alpha \\
& x^2+y^2+2 x y \sin \alpha=\cos ^2 \alpha
\end{aligned}$
Min. value of $\cos ^2 \alpha=0$
At $\alpha=\frac{\pi}{2}$

</details>

---

### Q7. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><msup><mi>sin</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mfenced><mn>5</mn></mfenced></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><msup><mi>cos</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mfenced><mn>5</mn></mfenced></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>π</mi><mn>2</mn></msup><mo>+</mo><mn>25</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msup><mi>π</mi><mn>2</mn></msup><mo>−</mo><mn>40</mn><mi>π</mi><mo>+</mo><mn>50</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>π</mi><mn>2</mn></msup><mo>−</mo><mn>20</mn><mi>π</mi><mo>+</mo><mn>50</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msup><mi>π</mi><mn>2</mn></msup><mo>−</mo><mn>40</mn><mi>π</mi><mo>+</mo><mn>50</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mfenced><mn>5</mn></mfenced></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mi>b</mi><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>cos</mi><mfenced><mn>5</mn></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>5</mn><mo>-</mo><mn>2</mn><mi>π</mi><mo> </mo><mtext>and</mtext><mo> </mo><mi>b</mi><mo>=</mo><mn>2</mn><mi>π</mi><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>5</mn><mo>-</mo><mn>2</mn><mi>π</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mi>π</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>25</mn><mo>+</mo><mn>4</mn><msup><mi>π</mi><mn>2</mn></msup><mo>-</mo><mn>20</mn><mi>π</mi><mo>+</mo><mn>4</mn><msup><mi>π</mi><mn>2</mn></msup><mo>+</mo><mn>25</mn><mo>-</mo><mn>20</mn><mi>π</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><msup><mi>π</mi><mn>2</mn></msup><mo>-</mo><mn>40</mn><mi>π</mi><mo>+</mo><mn>50</mn></math></p>

</details>

---

### Q8. JEE Main 2022 (25 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced open="[" close="]"><mfrac><mrow><mi>cos</mi><mfenced><mfrac><mrow><mn>15</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mfenced><mo>-</mo><mn>1</mn></mrow><mrow><mi>sin</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced></mrow></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>cos</mi><mfenced><mfrac><mrow><mn>15</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mfenced><mo>-</mo><mn>1</mn></mrow><mrow><mi>sin</mi><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>cos</mi><mfenced><mrow><mn>4</mn><mi>&#960;</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>-</mo><mn>1</mn></mrow><mrow><mi>sin</mi><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>-</mo><mn>1</mn></mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mstyle></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>&#160;</mo><mo>=</mo><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math></p>

</details>

---

### Q9. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#215;</mo><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>&#215;</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mn>1</mn><mo>=</mo><mi>x</mi><mo>&#160;</mo><mo>&#215;</mo><mfenced><mrow><mn>1</mn><mo>&#215;</mo><mn>1</mn></mrow></mfenced></math>. Then a value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#215;</mo><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>&#215;</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mo>&#160;</mo><mn>1</mn><mo>=</mo><mi>x</mi><mo>&#215;</mo><mfenced><mrow><mn>1</mn><mo>&#215;</mo><mn>1</mn></mrow></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>3</mn></msup></mrow></mfenced><mo>&#215;</mo><mn>1</mn><mo>=</mo><mi>x</mi><mo>&#215;</mo><mfenced><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>3</mn></msup></mrow></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>3</mn></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>t</mi></math>   </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mi>t</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>t</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>t</mi><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#8800;</mo><mo>&#8722;</mo><mn>3</mn></math> so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mo>=</mo><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>4</mn><mo>+</mo><mn>2</mn><mo>-</mo><mn>2</mn></mrow><mrow><mn>4</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>&#215;</mo><mn>2</mn><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></math> </p>

</details>

---

### Q10. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of real roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></msqrt><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>For equation to be defined,</p><p>for <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#8805;</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And, from domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#8804;</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> only possibility that the equation is defined is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></math></p><p>at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>=</mo><mn>0</mn><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>&#8800;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>and at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>=</mo><mn>0</mn><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>&#8800;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>None of these values satisfy</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Number of roots<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q11. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

All $x$ satisfying the inequality $\left(\cot ^{-1} x\right)^{2}-7\left(\cot ^{-1} x\right)+10>$ 0 , lie in the interval :

**Options:**

- **(A)** $(-\infty, \cot 5) \cup(\cot 4, \cot 2)$
- **(B)** $(\cot 2, \infty)$
- **(C)** $(-\infty, \cot 5) \cup(\cot 2, \infty)$
- **(D)** $(\cot 5, \cot 4)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\cot 2, \infty)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/kf0SkMhiqUsflQKHxUWOdfJ0uIoE_bh2Xq9554w046I.original.fullsize.png">


$\left(\cot ^{-1} x\right)^{2}-7\left(\cot ^{-1} x\right)+10>0$

$\left(\cot ^{-1} x-5\right)\left(\cot ^{-1}-2\right)>0$

$\cot ^{-1} x \in(-\infty, 2) \cup(5, \infty)$

But $\cot ^{-1} x$ lies in $(0, \pi)$

Now, from equation (1)

$\cot ^{-1} x \in(0,2)$

Now, it is clear from the graph

$x \in(\cot 2, \infty)$

</details>

---

### Q12. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

A value of <math><mi>x</mi></math> satisfying the equation <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">cot</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow></mrow><mo>=</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow><mo>,</mo></math> is:

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mn>0</mn></math>
- **(C)** <math><mo>-</mo><mn>1</mn></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mfenced close="]" open="["><mrow><msup><mi>cot</mi></msup></mrow></mfenced><mfenced close="]" open="["><mrow><msup><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow></mfenced><mo>=</mo><mi>cos</mi><mfenced><mrow><msup><mi>tan</mi></msup></mrow></mfenced><mfenced><mrow><msup><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dedb8b25-5c0d-45ef-a510-92a3fc395a69-image.png" style="width: 300px; height: 142px;" /></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cot</mi><mi>&lambda;</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&beta;</mi><mo>=</mo><mi mathvariant="normal">x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&rArr;</mo><mo>  </mo><mi>sin</mi><mi>&lambda;</mi><mo>=</mo><mi>cos</mi><mi>&beta;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&rArr;</mo><mo>  </mo><mfrac><mn>1</mn><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&rArr;</mo><mo>  </mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&rArr;</mo><mo>  </mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></math></p>

</details>

---

### Q13. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#62;</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>5</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mn>65</mn><mn>156</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mn>5</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi></math>**

**Detailed Solution:**

<p>Substitute <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><mi>&#952;</mi><mo>,</mo><mi>&#160;</mi><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>&#952;</mi><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>&#952;</mi><mo>+</mo><mi>&#960;</mi><mo>-</mo><mn>2</mn><mi>&#952;</mi></math>, as  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>&#952;</mi><mo>&#62;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math><mo>=</mo><mi>&#960;</mi></math></p>

</details>

---

### Q14. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The principal value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>c</mi><mi>o</mi><mi>t</mi><mfrac><mrow><mn>43</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math>
- **(D)** <math> <mrow> <mo>-</mo> <mfrac> <mrow> <mn>3</mn> <mi>&pi;</mi> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>&#60;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2991f94e-894d-4840-a82c-28bca07012b5-3bb03b17-88b9-4926-b246-4d8576ff28b7-image.png" style="width: 400px; height: 306px;" />

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mi>o</mi><mi>t</mi><mfenced><mfrac><mrow><mn>4</mn><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mfenced><mo>=</mo><mi>c</mi><mi>o</mi><mi>t</mi><mfenced><mrow><mn>1</mn><mn>0</mn><mi>&#960;</mi><mo>+</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>c</mi><mi>o</mi><mi>t</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>c</mi><mi>o</mi><mi>t</mi><mfenced><mfrac><mrow><mn>4</mn><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p>

</details>

---

### Q15. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `1`

A value of $\tan ^{-1}\left(\sin \left(\cos ^{-1}\left(\sqrt{\frac{2}{3}}\right)\right)\right)$ is

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{6}$**

**Detailed Solution:**

Consider $\tan ^{-1}\left[\sin \left(\cos ^{-1} \sqrt{\frac{2}{3}}\right)\right]$
$$
\begin{aligned}
& \text { Let } \cos ^{-1} \sqrt{\frac{2}{3}}=\theta \Rightarrow \cos \theta=\sqrt{\frac{2}{3}} \\
& \Rightarrow \quad \sin \theta=\sqrt{1-\cos ^2 \theta}=\sqrt{1-\frac{2}{3}}=\sqrt{\frac{1}{3}} \\
& \therefore \quad \tan ^{-1}\left[\sin \left(\cos ^{-1} \sqrt{\frac{2}{3}}\right)\right]=\tan ^{-1}[\sin \theta] \\
& =\tan ^{-1}\left[\sqrt{\frac{1}{3}}\right]=\tan ^{-1}\left(\frac{1}{\sqrt{3}}\right) \\
& =\frac{\pi}{6}
\end{aligned}
$$

</details>

---

### Q16. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

If $\sin ^{-1}\left(\frac{x}{5}\right)+\operatorname{cosec}^{-1}\left(\frac{5}{4}\right)=\frac{\pi}{2}$ then a value of $x$ is

**Options:**

- **(A)** $1$
- **(B)** $3$
- **(C)** $4$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3$**

**Detailed Solution:**

$\sin ^{-1} \frac{x}{5}+\sin ^{-1} \frac{4}{5}=\frac{\pi}{2}$
$\Rightarrow \sin ^{-1} \frac{x}{5}=\cos ^{-1} \frac{4}{5} \Rightarrow \sin ^{-1} \frac{x}{5}=\sin ^{-1} \frac{3}{5}$
$\therefore x=3$.

</details>

---

### Q17. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

If $\cos ^{-1} x-\cos ^{-1} \frac{y}{2}=\alpha$, then $4 x^2-4 x y \cos \alpha+y^2$ is equal to

**Options:**

- **(A)** $2 \sin 2 \alpha$
- **(B)** 4
- **(C)** $4 \sin ^2 \alpha$
- **(D)** $-4 \sin ^2 \alpha$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 \sin ^2 \alpha$**

**Detailed Solution:**

$$
\begin{aligned}
& \cos ^{-1} x-\cos ^{-1} \frac{y}{2}=\alpha \\
& \cos ^{-1}\left(\frac{x y}{2}+\sqrt{\left(-x^2\right)\left(1-\frac{y^2}{4}\right)}\right)=\alpha \\
& \cos ^{-1}\left(\frac{x y+\sqrt{4-y^2-4 x^2+x^2 y^2}}{2}\right)=\alpha \\
& \Rightarrow 4-y^2-4 x^2+x^2 y^2=4 \cos ^2 \alpha+x^2 y^2-4 x y \cos \alpha \\
& \Rightarrow 4 x^2+y^2-4 x y \cos \alpha=4 \sin ^2 \alpha
\end{aligned}
$$

</details>

---

### Q18. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

$\cot ^{-1}(\sqrt{\cos \alpha})=\tan ^{-1}(\sqrt{\cos \alpha})=x$, then $\sin x=$

**Options:**

- **(A)** $\tan ^2\left(\frac{\alpha}{2}\right)$
- **(B)** $\cot ^2\left(\frac{\alpha}{2}\right)$
- **(C)** $\tan \alpha$
- **(D)** $\cot \left(\frac{\alpha}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan ^2\left(\frac{\alpha}{2}\right)$**

**Detailed Solution:**

$\cot ^{-1}(\sqrt{\cos \alpha})-\tan ^{-1}(\sqrt{\cos \alpha})=x$
$\tan ^{-1}\left(\frac{1}{\sqrt{\cos \alpha}}\right)-\tan ^{-1}(\sqrt{\cos \alpha})=x \Rightarrow \tan ^{-1} \frac{\frac{1}{\sqrt{\cos \alpha}}-\sqrt{\cos \alpha}}{1+\frac{1}{\sqrt{\cos \alpha}} \cdot \sqrt{\cos \alpha}}=x$
$\Rightarrow \tan ^{-1} \frac{1-\cos \alpha}{2 \sqrt{\cos \alpha}}=x \Rightarrow \tan x=\frac{1-\cos \alpha}{2 \sqrt{\cos \alpha}}$
OR $\cot x=\frac{2 \sqrt{\cos \alpha}}{1-\cos \alpha}$ or $\operatorname{cosec} x=\frac{1+\cos \alpha}{1-\cos \alpha}$
$\sin x=\frac{1-\cos \alpha}{1+\cos \alpha}=\frac{1-\left(1-2 \sin ^2 \alpha / 2\right)}{1+2 \cos ^2 \alpha / 2-1}$ or $\sin x=\tan ^2 \frac{\alpha}{2}$

</details>

---

