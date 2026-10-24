# JEE Main Mathematics - Trigonometric Ratios & Identities

## Topic 3: Sum and Difference & Multiple angle Formula

**Total Questions:** 27

---

### Q1. JEE Main 2026 (04 April Shift 1)

*Type:* `numerical` | *Level:* `3`

If $A = \dfrac{\sin 3^\circ}{\cos 9^\circ} + \dfrac{\sin 9^\circ}{\cos 27^\circ} + \dfrac{\sin 27^\circ}{\cos 81^\circ}$ and $B = \tan 81^\circ - \tan 3^\circ$, then $\dfrac{B}{A}$ is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

Consider the general term $\dfrac{\sin x}{\cos 3x}$.

We can rewrite this by multiplying and dividing by $2\cos x$:

$\dfrac{2\sin x \cos x}{2\cos 3x \cos x} = \dfrac{\sin 2x}{2\cos 3x \cos x}$

Using $\sin 2x = \sin(3x - x) = \sin 3x \cos x - \cos 3x \sin x$, we get:

$\dfrac{\sin 3x \cos x - \cos 3x \sin x}{2\cos 3x \cos x} = \dfrac{1}{2} \left( \dfrac{\sin 3x}{\cos 3x} - \dfrac{\sin x}{\cos x} \right) = \dfrac{1}{2} (\tan 3x - \tan x)$

Applying this identity to each term of $A$:

$\dfrac{\sin 3^\circ}{\cos 9^\circ} = \dfrac{1}{2} (\tan 9^\circ - \tan 3^\circ)$

$\dfrac{\sin 9^\circ}{\cos 27^\circ} = \dfrac{1}{2} (\tan 27^\circ - \tan 9^\circ)$

$\dfrac{\sin 27^\circ}{\cos 81^\circ} = \dfrac{1}{2} (\tan 81^\circ - \tan 27^\circ)$

Adding these terms, the series telescopes:

$A = \dfrac{1}{2} (\tan 9^\circ - \tan 3^\circ + \tan 27^\circ - \tan 9^\circ + \tan 81^\circ - \tan 27^\circ)$

$A = \dfrac{1}{2} (\tan 81^\circ - \tan 3^\circ)$

We are given $B = \tan 81^\circ - \tan 3^\circ$.

Substituting $B$ into the equation for $A$:

$A = \dfrac{1}{2} B$

$\Rightarrow \dfrac{B}{A} = 2$

Answer: $2$

</details>

---

### Q2. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $P = \{\theta \in [0, 4\pi] : \tan^2\theta \neq 1\}$ and $S = \{a \in \mathbb{Z} : 2(\cos^8\theta - \sin^8\theta)\sec 2\theta = a^2, \theta \in P\}$. Then $n(S)$ is:

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0$**

**Detailed Solution:**

Given the expression $2(\cos^8\theta - \sin^8\theta)\sec 2\theta = a^2$.

We can simplify the term $\cos^8\theta - \sin^8\theta$ as follows:
$\cos^8\theta - \sin^8\theta = (\cos^4\theta - \sin^4\theta)(\cos^4\theta + \sin^4\theta)$
$\Rightarrow (\cos^2\theta - \sin^2\theta)(\cos^2\theta + \sin^2\theta)((\cos^2\theta + \sin^2\theta)^2 - 2\sin^2\theta\cos^2\theta)$
$\Rightarrow \cos 2\theta \times 1 \times \left(1 - \dfrac{1}{2}\sin^2 2\theta\right)$

Substitute this back into the given equation:
$2 \left[ \cos 2\theta \left(1 - \dfrac{1}{2}\sin^2 2\theta\right) \right] \dfrac{1}{\cos 2\theta} = a^2$

Since $\theta \in P$, we have $\tan^2\theta \neq 1$, which implies $\cos 2\theta \neq 0$. Thus, we can safely cancel $\cos 2\theta$:
$2 \left(1 - \dfrac{1}{2}\sin^2 2\theta\right) = a^2$
$\Rightarrow 2 - \sin^2 2\theta = a^2$

We know that for any real $\theta$, $0 \le \sin^2 2\theta \le 1$.
However, since $\tan^2\theta \neq 1$, $\sin^2 2\theta \neq 1$.
Therefore, $0 \le \sin^2 2\theta < 1$.

Multiplying by $-1$ and adding $2$, we get the range of $a^2$:
$1 < 2 - \sin^2 2\theta \le 2$
$\Rightarrow 1 < a^2 \le 2$

Since $a \in \mathbb{Z}$, $a^2$ must be a perfect square integer. The only integer in the interval $(1, 2]$ is $2$, so $a^2 = 2$.

But there is no integer $a$ such that $a^2 = 2$.

Thus, the set $S$ contains no elements, meaning $S = \emptyset$.

Therefore, $n(S) = 0$.

Answer: $0$

</details>

---

### Q3. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin\left(\dfrac{\pi}{18}\right) \sin\left(\dfrac{5\pi}{18}\right) \sin\left(\dfrac{7\pi}{18}\right) = K$, then the value of $\sin\left(\dfrac{10K\pi}{3}\right)$ is :

**Options:**

- **(A)** $\dfrac{\sqrt{3} + 1}{2\sqrt{2}}$
- **(B)** $\dfrac{\sqrt{3} - 1}{\sqrt{2}}$
- **(C)** $\dfrac{\sqrt{3}}{2}$
- **(D)** $\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\sqrt{3} + 1}{2\sqrt{2}}$**

**Detailed Solution:**

Given $K = \sin\left(\dfrac{\pi}{18}\right) \sin\left(\dfrac{5\pi}{18}\right) \sin\left(\dfrac{7\pi}{18}\right)$

Using the standard trigonometric identity $\sin(\theta) \sin\left(\dfrac{\pi}{3} - \theta\right) \sin\left(\dfrac{\pi}{3} + \theta\right) = \dfrac{1}{4} \sin(3\theta)$ with $\theta = \dfrac{\pi}{18}$:

$\dfrac{\pi}{3} - \theta = \dfrac{6\pi}{18} - \dfrac{\pi}{18} = \dfrac{5\pi}{18}$

$\dfrac{\pi}{3} + \theta = \dfrac{6\pi}{18} + \dfrac{\pi}{18} = \dfrac{7\pi}{18}$

Applying the identity, we get:

$K = \dfrac{1}{4} \sin\left(3 \times \dfrac{\pi}{18}\right) = \dfrac{1}{4} \sin\left(\dfrac{\pi}{6}\right)$

$K = \dfrac{1}{4} \times \dfrac{1}{2} = \dfrac{1}{8}$

We need to find the value of $\sin\left(\dfrac{10K\pi}{3}\right)$. Substituting $K = \dfrac{1}{8}$:

$\sin\left(\dfrac{10 \times \dfrac{1}{8} \times \pi}{3}\right) = \sin\left(\dfrac{10\pi}{24}\right) = \sin\left(\dfrac{5\pi}{12}\right)$

Expanding $\dfrac{5\pi}{12}$ as $\dfrac{\pi}{4} + \dfrac{\pi}{6}$:

$\sin\left(\dfrac{5\pi}{12}\right) = \sin\left(\dfrac{\pi}{4} + \dfrac{\pi}{6}\right)$

$\sin\left(\dfrac{5\pi}{12}\right) = \sin\left(\dfrac{\pi}{4}\right)\cos\left(\dfrac{\pi}{6}\right) + \cos\left(\dfrac{\pi}{4}\right)\sin\left(\dfrac{\pi}{6}\right)$

$\sin\left(\dfrac{5\pi}{12}\right) = \left(\dfrac{1}{\sqrt{2}}\right)\left(\dfrac{\sqrt{3}}{2}\right) + \left(\dfrac{1}{\sqrt{2}}\right)\left(\dfrac{1}{2}\right) = \dfrac{\sqrt{3} + 1}{2\sqrt{2}}$

Answer: $\dfrac{\sqrt{3} + 1}{2\sqrt{2}}$

</details>

---

### Q4. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\frac{\tan (\mathrm{A}-\mathrm{B})}{\tan \mathrm{A}}+\frac{\sin ^{2} \mathrm{C}}{\sin ^{2} \mathrm{~A}}=1, \mathrm{~A}, \mathrm{~B}, \mathrm{C} \in\left(0, \frac{\pi}{2}\right)$, then

**Options:**

- **(A)** $\tan \mathrm{A}, \tan \mathrm{C}, \tan \mathrm{B}$ are in A.P.
- **(B)** $\tan A, \tan B, \tan C$ are in G.P.
- **(C)** $\tan A, \tan C, \tan B$ are in G.P.
- **(D)** $\tan \mathrm{A}, \tan \mathrm{B}, \tan \mathrm{C}$ are in A.P.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\tan A, \tan C, \tan B$ are in G.P.**

**Detailed Solution:**

Starting with $\frac{\tan(A-B)}{\tan A} + \frac{\sin^2 C}{\sin^2 A} = 1$, rearrange to $\frac{\tan(A-B)}{\tan A} = 1 - \frac{\sin^2 C}{\sin^2 A}$.
$\Rightarrow \tan(A-B) \tan A = \sin^2 A - \sin^2 C$.
Applying the identity $\sin^2 \theta = \frac{\tan^2 \theta}{1+\tan^2 \theta}$ and simplifying leads to a relationship between the tangent values.
The constraint reduces to $(\tan C)^2 = \tan A \cdot \tan B$, which means $\tan A$, $\tan C$, and $\tan B$ form a geometric progression with common ratio $r = \frac{\tan C}{\tan A}$.

</details>

---

### Q5. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\frac{\sqrt{3} \operatorname{cosec} 20^{\circ}-\sec 20^{\circ}}{\cos 20^{\circ} \cos 40^{\circ} \cos 60^{\circ} \cos 80^{\circ}}$ is equal to

**Options:**

- **(A)** 16
- **(B)** 32
- **(C)** 64
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 64**

**Detailed Solution:**

Numerator:
$\sqrt{3}\operatorname{cosec} 20° - \sec 20° = \frac{\sqrt{3}\cos 20° - \sin 20°}{\sin 20° \cos 20°}$
$\sqrt{3}\cos 20° - \sin 20° = 2\left(\frac{\sqrt{3}}{2}\cos 20° - \frac{1}{2}\sin 20°\right)$ 
$= 2\cos(20° + 30°) = 2\cos 50°$
So numerator = $\frac{2\cos 50°}{\sin 20° \cos 20°} = \frac{4\cos 50°}{\sin 40°} = 4$
Denominator:
$\cos 20° \cos 40° \cos 60° \cos 80°$ where $\cos 60° = \frac{1}{2}$
Using product formula:
$\sin 20° \cos 20° \cos 40° \cos 80° = \frac{1}{8}\sin 20°$
Therefore $\cos 20° \cos 40° \cos 80° \cdot \frac{1}{2} = \frac{1}{16}$
So, $\frac{4 \cdot \sin 20° \cos 20°}{\frac{1}{16}} = 64$

</details>

---

### Q6. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\cot x=\frac{5}{12}$ for some $x \in\left(\pi, \frac{3 \pi}{2}\right)$, then $\sin 7 x\left(\cos \frac{13 x}{2}+\sin \frac{13 x}{2}\right)+\cos 7 x\left(\cos \frac{13 x}{2}-\sin \frac{13 x}{2}\right)$ is equal to

**Options:**

- **(A)** $\frac{4}{\sqrt{26}}$
- **(B)** $\frac{6}{\sqrt{26}}$
- **(C)** $\frac{5}{\sqrt{13}}$
- **(D)** $\frac{1}{\sqrt{13}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{\sqrt{13}}$**

**Detailed Solution:**

$\cot x = \dfrac{5}{12} \Rightarrow \cos x = \dfrac{-5}{13} = 2\cos^2 \dfrac{x}{2} - 1$
$\cos\left(\dfrac{x}{2}\right) = -\dfrac{2}{\sqrt{13}}$ or $\dfrac{2}{\sqrt{13}}$ (rejected)
$\left\{ \because \dfrac{x}{2} \in \left(\dfrac{\pi}{2}, \dfrac{3\pi}{4}\right) \right\}$
$\left(\sin 7x \dfrac{\sin 13x}{2} + \cos 7x \dfrac{\cos 13x}{2}\right) + \left(\sin 7x \dfrac{\cos 13x}{2} - \cos 7x \dfrac{\sin 13x}{2}\right)$
$\cos\left(7x - \dfrac{13x}{2}\right) + \sin\left(7x - \dfrac{13x}{2}\right)$
$\cos \dfrac{x}{2} + \sin\left(\dfrac{x}{2}\right)$
$\dfrac{3}{\sqrt{13}} - \dfrac{2}{\sqrt{13}} = \dfrac{1}{\sqrt{13}}$

</details>

---

### Q7. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\frac{\pi}{2}<\theta<\pi$ and $\cot \theta=-\frac{1}{2 \sqrt{2}}$. Then the value of 
 $\sin \left(\frac{15 \theta}{2}\right)(\cos 8 \theta+\sin 8 \theta)+\cos \left(\frac{15 \theta}{2}\right)(\cos 8 \theta-\sin 8 \theta)$ 
 is equal to

**Options:**

- **(A)** $-\frac{\sqrt{2}}{\sqrt{3}}$
- **(B)** $\frac{\sqrt{2}-1}{\sqrt{3}}$
- **(C)** $\frac{\sqrt{2}}{\sqrt{3}}$
- **(D)** $\frac{1-\sqrt{2}}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1-\sqrt{2}}{\sqrt{3}}$**

**Detailed Solution:**

Expanding and regrouping:
$\sin\frac{15\theta}{2}(\cos 8\theta + \sin 8\theta) + \cos\frac{15\theta}{2}(\cos 8\theta - \sin 8\theta)$
$= \left(\cos\frac{15\theta}{2}\cos 8\theta + \sin\frac{15\theta}{2}\sin 8\theta\right) + \left(\sin\frac{15\theta}{2}\cos 8\theta - \cos\frac{15\theta}{2}\sin 8\theta\right)$
$= \cos\left(8\theta - \frac{15\theta}{2}\right) + \sin\left(\frac{15\theta}{2} - 8\theta\right) = \cos\frac{\theta}{2} - \sin\frac{\theta}{2}$.
From $\cot\theta = -\frac{1}{2\sqrt{2}}$: $\sin\theta = \frac{2\sqrt{2}}{3}$, $\cos\theta = -\frac{1}{3}$.
$\left(\cos\frac{\theta}{2} - \sin\frac{\theta}{2}\right)^2 = 1 - \sin\theta = 1 - \frac{2\sqrt{2}}{3} = \frac{(\sqrt{2}-1)^2}{3}$.
Since $\frac{\pi}{4} < \frac{\theta}{2} < \frac{\pi}{2}$, $\sin\frac{\theta}{2} > \cos\frac{\theta}{2}$, so the value is $\frac{1-\sqrt{2}}{\sqrt{3}}$.

</details>

---

### Q8. JEE Main 2026 (22 January Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $\cos (\alpha+\beta)=-\frac{1}{10}$ and $\sin (\alpha-\beta)=\frac{3}{8}$, where $0<\alpha<\frac{\pi}{3}$ and $0<\beta<\frac{\pi}{4}$. If $\tan 2 \alpha=\frac{3(1-r \sqrt{5})}{\sqrt{11}(s+\sqrt{5})}, r, s \in N$, then $r+s$ is equal to $\_\_\_\_$ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

$\tan 2 \alpha=\tan [(\alpha+\beta)+(\alpha-\beta)]$
$\tan 2 \alpha=\frac{\tan (\alpha+\beta)+\tan (\alpha-\beta)}{1-\tan (\alpha+\beta) \cdot \tan (\alpha-\beta)}$
$\tan 2 \alpha=\frac{\left(-\sqrt{99}+\frac{3}{\sqrt{55}}\right)}{1-(\sqrt{99})\left(\frac{3}{\sqrt{55}}\right)}$
$\tan 2 \alpha=\frac{-3 \sqrt{11}+\frac{3}{\sqrt{5} \times \sqrt{11}}}{1+\frac{9 \sqrt{11}}{\sqrt{5} \times \sqrt{11}}}$
$\tan 2 \alpha=\frac{3(1-11 \sqrt{5})}{\sqrt{11}(9+\sqrt{5})}$
$\mathrm{r}=11, \mathrm{~s}=9$
$\mathrm{r}+\mathrm{s}=20$

</details>

---

### Q9. JEE Main 2026 (22 January Shift 1)

*Type:* `numerical` | *Level:* `2`

If $\frac{\cos ^{2} 48^{\circ}-\sin ^{2} 12^{\circ}}{\sin ^{2} 24^{\circ}-\sin ^{2} 6^{\circ}}=\frac{\alpha+\beta \sqrt{5}}{2}$, where $\alpha, \beta \in \mathbb{N}$, then $\alpha+\beta$ is equal to $\_\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

Using $\cos^2A - \sin^2B = \cos(A+B)\cos(A-B)$:
$\cos^2 48° - \sin^2 12° = \cos 60° \cos 36° = \frac{1}{2}\cos 36°$.
Using $\sin^2A - \sin^2B = \sin(A+B)\sin(A-B)$:
$\sin^2 24° - \sin^2 6° = \sin 30° \sin 18° = \frac{1}{2}\sin 18°$.
Ratio $= \frac{\cos 36°}{\sin 18°} = \frac{(1+\sqrt{5})/4}{(\sqrt{5}-1)/4} = \frac{(1+\sqrt{5})^2}{4} = \frac{6+2\sqrt{5}}{4} = \frac{3+\sqrt{5}}{2}$.
$\alpha = 3,\ \beta = 1$. $\alpha + \beta = 4$.

</details>

---

### Q10. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\operatorname{cosec} 10^{\circ}-\sqrt{3} \sec 10^{\circ}$ is equal to :

**Options:**

- **(A)** 8
- **(B)** 6
- **(C)** 2
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

$\operatorname{cosec} 10° - \sqrt{3} \sec 10° = \frac{\cos 10° - \sqrt{3} \sin 10°}{\sin 10° \cos 10°}$.
Numerator: $\cos 10° - \sqrt{3} \sin 10° = 2\left(\frac{1}{2}\cos 10° - \frac{\sqrt{3}}{2} \sin 10°\right) = 2\cos 70° = 2\sin 20°$.
Denominator: $\sin 10° \cos 10° = \frac{1}{2}\sin 20°$.
Result $= \frac{2\sin 20°}{\frac{1}{2}\sin 20°} = 4$.

</details>

---

### Q11. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\sum_{r=1}^{13}\left\{\frac{1}{\sin \left(\frac{\pi}{4}+(r-1) \frac{\pi}{6}\right) \sin \left(\frac{\pi}{4}+\frac{r \pi}{6}\right)}\right\}=a \sqrt{3}+b, a, b \in \mathbf{Z}$, then $a^2+b^2$ is equal to :

**Options:**

- **(A)** $10$
- **(B)** $4$
- **(C)** $2$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $8$**

**Detailed Solution:**

$\frac{1}{\sin \frac{\pi}{6}} \sum_{r=1}^{13} \frac{\sin \left[\left(\frac{\pi}{4}+\frac{r \pi}{6}\right)-\left(\frac{\pi}{4}\right)-(r-1) \frac{\pi}{6}\right]}{\sin \left(\frac{\pi}{4}+(r-1) \frac{\pi}{6}\right) \sin \left(\frac{\pi}{4}+\frac{r \pi}{6}\right)}$


$\begin{aligned}
& \frac{1}{\sin \frac{\pi}{6}} \sum_{\mathrm{r}=1}^{13}\left(\cot \left(\frac{\pi}{4}+(\mathrm{r}-1) \frac{\pi}{6}\right)-\cot \left(\frac{\pi}{4}+\frac{\mathrm{r} \pi}{6}\right)\right) \\
& =2 \sqrt{3}-2=\alpha \sqrt{3}+\mathrm{b}
\end{aligned}$

So $a^2+b^2=8$

</details>

---

### Q12. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt></mfrac><mo>,</mo><mi>tan</mi><mi>B</mi><mo>=</mo><mfrac><msqrt><mi>x</mi></msqrt><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>C</mi><mo>=</mo><msup><mfenced><mrow><msup><mi>x</mi><mrow><mo>−</mo><mn>3</mn></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>−</mo><mn>2</mn></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>,</mo><mn>0</mn><mo>&lt;</mo><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi><mo>&lt;</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>π</mi><mo>−</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>π</mi><mo>−</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>−</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>**

**Detailed Solution:**

Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt></mfrac><mo>,</mo><mi>tan</mi><mi>B</mi><mo>=</mo><mfrac><msqrt><mi>x</mi></msqrt><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>C</mi><mo>=</mo><msup><mfenced><mrow><msup><mi>x</mi><mrow><mo>−</mo><mn>3</mn></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>−</mo><mn>2</mn></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>=</mo><mfrac><msqrt><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mrow><mi>x</mi><msqrt><mi>x</mi></msqrt></mrow></mfrac></math><p>We know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>tan</mi><mi>A</mi><mo>+</mo><mi>tan</mi><mi>B</mi></mrow><mrow><mn>1</mn><mo>−</mo><mi>tan</mi><mi>A</mi><mi>tan</mi><mi>B</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mfrac><mn>1</mn><msqrt><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msqrt></mfrac><mo>+</mo><mfrac><msqrt><mi>x</mi></msqrt><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mfrac></mrow><mrow><mn>1</mn><mo>−</mo><mfrac><mn>1</mn><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mfenced></mrow><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><msqrt><mi>x</mi></msqrt></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mfenced></mrow><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><msqrt><mi>x</mi></msqrt></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mrow><mi>x</mi><msqrt><mi>x</mi></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>tan</mi><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>+</mo><mi>B</mi><mo>=</mo><mi>C</mi></math></p>

</details>

---

### Q13. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mi>β</mi><mo>∈</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow></mfenced></math> let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>sin</mi><mo>(</mo><mi>α</mi><mo>+</mo><mi>β</mi><mo>)</mo><mo>=</mo><mn>2</mn><mi>sin</mi><mo>(</mo><mi>α</mi><mo>-</mo><mi>β</mi><mo>)</mo></math> and a real number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>α</mi><mo>=</mo><mo> </mo><mi>tan</mi><mi>β</mi></math>. Then the value of<math xmlns="http://www.w3.org/1998/Math/MathML"><mo> </mo><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math>**

**Detailed Solution:**

<blockquote><p>Given:</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>sin</mi><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi>sin</mi><mfenced><mrow><mi>α</mi><mo>-</mo><mi>β</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>α</mi><mo>-</mo><mi>β</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi></mrow></mfenced><mo>+</mo><mi>sin</mi><mfenced><mrow><mi>α</mi><mo>-</mo><mi>β</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>α</mi><mo>+</mo><mi>β</mi></mrow></mfenced><mo>-</mo><mi>sin</mi><mfenced><mrow><mi>α</mi><mo>-</mo><mi>β</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>+</mo><mn>3</mn></mrow><mrow><mn>2</mn><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>α</mi><mi>cos</mi><mi>β</mi></mrow><mrow><mn>2</mn><mi>cos</mi><mi>α</mi><mi>sin</mi><mi>β</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>tan</mi><mi>α</mi></mrow><mrow><mi>tan</mi><mi>β</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mi>α</mi><mo>=</mo><mo>-</mo><mn>5</mn><mi>tan</mi><mi>β</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>k</mi><mo>=</mo><mo>-</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q14. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>:</mo><munderover><mo>&#8721;</mo><mrow><mi>m</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><mi>sec</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfenced><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mi>sec</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mrow><mi>m</mi><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>8</mn><msqrt><mn>3</mn></msqrt></mfrac></mrow></mfenced></math>. Then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>=</mo><mfenced open="{" close="}"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>+</mo><mfenced><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>=</mo><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>+</mo><mi>m</mi><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>=</mo><mi>y</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>m</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><mi>sec</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfenced><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mi>sec</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mrow><mi>m</mi><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>m</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><mi>sec</mi><mi>x</mi><mi>sec</mi><mi>y</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>m</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><mfrac><mn>1</mn><mrow><mi>cos</mi><mi>x</mi><mi>cos</mi><mi>y</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><munderover><mo>&#8721;</mo><mrow><mi>m</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi>y</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mi>cos</mi><mi>x</mi><mi>cos</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mn>2</mn><munderover><mo>&#8721;</mo><mrow><mi>m</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><mfenced><mrow><mi>tan</mi><mi>y</mi><mo>-</mo><mi>tan</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><munderover><mo>&#8721;</mo><mrow><mi>m</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><mfenced><mrow><mi>tan</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mi>m</mi><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mo>-</mo><mi>tan</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mo>(</mo><mi>m</mi><mo>-</mo><mn>1</mn><mo>)</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mi>tan</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mo>-</mo><mi>tan</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mrow><mn>0</mn><mo>&#183;</mo><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mi>tan</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mn>2</mn><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mo>-</mo><mi>tan</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mn>2</mn><mfenced><mrow><mi>tan</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mn>3</mn><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mo>-</mo><mi>tan</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mn>2</mn><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow></mfenced><mo>+</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mo>+</mo><mn>2</mn><mfenced><mrow><mi>tan</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mn>9</mn><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mo>-</mo><mi>tan</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mn>8</mn><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mi>tan</mi><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mrow><mn>9</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced><mo>-</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mi>cot</mi><mi>&#952;</mi><mo>-</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mo>-</mo><mi>cot</mi><mi>&#952;</mi><mo>-</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>8</mn><msqrt><mn>3</mn></msqrt></mfrac></math> (Given)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mi>tan</mi><mi>&#952;</mi><mo>+</mo><mi>cot</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>4</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt></math> (as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>)</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p></blockquote>

</details>

---

### Q15. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cot</mi><mi>&#945;</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sec</mi><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>&#60;</mo><mi>&#945;</mi><mo>&#60;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>&#60;</mo><mi>&#946;</mi><mo>&#60;</mo><mi>&#960;</mi></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced></math> and the quadrant in which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> lies, respectively are

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>IV</mi><mi>th</mi></msup></math> quadrant
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">I</mi><mi>st</mi></msup></math> quadrant
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>IV</mi><mi>th</mi></msup></math> quadrant
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>7</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">I</mi><mi>st</mi></msup></math> quadrant

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>IV</mi><mi>th</mi></msup></math> quadrant**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cot</mi><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>sec</mi><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mn>3</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>5</mn></mfrac><mo>,</mo><mi>tan</mi><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#945;</mi><mo>=</mo><mn>1</mn></math></p><p>Now using formula <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>tan</mi><mi>&#945;</mi><mo>+</mo><mi>tan</mi><mi>&#946;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mi>&#945;</mi><mi>tan</mi><mi>&#946;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow><mrow><mn>1</mn><mo>+</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>7</mn></mfrac></math> </p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi></math> is negative in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mi>n</mi><mi>d</mi></mrow></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mn>4</mn><mrow><mi>t</mi><mi>h</mi></mrow></msup></math>  quadrant but as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>&#60;</mo><mi>&#945;</mi><mo>&#60;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> will lie in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mtext>IV</mtext><mtext>th</mtext></msup></math> quadrant.</p>

</details>

---

### Q16. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mi>sin</mi><mfenced><mrow><mn>20</mn><mo>&#176;</mo></mrow></mfenced><mi>sin</mi><mfenced><mrow><mn>40</mn><mo>&#176;</mo></mrow></mfenced><mi>sin</mi><mfenced><mrow><mn>80</mn><mo>&#176;</mo></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#952;</mi><mi>sin</mi><mfenced><mrow><mn>60</mn><mo>-</mo><mi>&#952;</mi></mrow></mfenced><mi>sin</mi><mfenced><mrow><mn>60</mn><mo>+</mo><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>sin</mi><mn>3</mn><mi>&#952;</mi></math></p><p>Now given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mi>sin</mi><mn>20</mn><mo>&#176;</mo><mi>sin</mi><mn>40</mn><mo>&#176;</mo><mi>sin</mi><mn>80</mn><mo>&#176;</mo></math></p><p>Comparing with above formula <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mn>20</mn><mo>&#176;</mo></math></p><p>we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mi>sin</mi><mn>20</mn><mo>&#176;</mo><mi>sin</mi><mn>40</mn><mo>&#176;</mo><mi>sin</mi><mn>80</mn><mo>&#176;</mo><mo>=</mo><mn>16</mn><mo>&#215;</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac><mo>&#215;</mo><mi>sin</mi><mfenced><mrow><mn>3</mn><mo>&#215;</mo><mn>20</mn><mo>&#176;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>16</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#215;</mo><mi>sin</mi><mn>60</mn><mo>&#176;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#215;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math></p>

</details>

---

### Q17. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>cosec</mo><mn>18</mn><mo>&#176;</mo></math> is a root of the equation:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>We know that </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>18</mn><mo>&#176;</mo><mo>=</mo><mfrac><mrow><msqrt><mn>5</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>cosec</mo><mn>18</mn><mo>&#176;</mo><mo>=</mo><mfrac><mn>1</mn><mrow><mi>sin</mi><mn>18</mn><mo>&#176;</mo></mrow></mfrac><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><mn>4</mn><mrow><msqrt><mn>5</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p>Rationalizing denominator</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>4</mn><mrow><msqrt><mn>5</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><msqrt><mn>5</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>5</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mfenced><mrow><msqrt><mn>5</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>5</mn></msqrt><mo>+</mo><mn>1</mn></math></p><p>Hence equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msqrt><mn>5</mn></msqrt><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>5</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q18. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> inches long pencil <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> with mid point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> and a small eraser <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> are placed on the horizontal top of a table such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>C</mi><mo>=</mo><msqrt><mn>5</mn></msqrt></math> inches and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8736;</mo><mi>P</mi><mi>C</mi><mi>B</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mn>2</mn><mo>)</mo></math>. The acute angle through which the pencil must be rotated about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> so that the perpendicular distance between eraser and pencil becomes exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> inch is :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/979a2e2e-574a-4682-a5dc-e35b4084ec96-image.png" style="width: 350px; height: 185px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>1</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fee5d83e-50a5-4685-8630-83d9731d92b8-image.png" style="width: 279px; height: 250px;" />From figure,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac><mspace linebreak="newline"></mspace><mi>tan</mi><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo><mo>=</mo><mn>2</mn><mspace linebreak="newline"></mspace><mi>tan</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>tan</mi><mi>&#945;</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mi>&#945;</mi><mo>&#160;</mo><mo>.</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfrac><mo>=</mo><mn>2</mn><mspace linebreak="newline"></mspace></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></math></p>

</details>

---

### Q19. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mfenced><mrow><mi>sin</mi><mfenced><mrow><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mi>cos</mi><mfenced><mrow><mn>4</mn><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mi>sin</mi><mfenced><mrow><mn>6</mn><mi>&#952;</mi></mrow></mfenced></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>23</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>27</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>23</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>23</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8658;</mo><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p>Now:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>4</mn><mi>&#952;</mi><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><msup><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>9</mn><mn>16</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>6</mn><mi>&#952;</mi><mo>=</mo><mn>3</mn><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>4</mn><msup><mi>sin</mi><mn>3</mn></msup><mn>2</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>3</mn><mo>-</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mo>&#183;</mo><mi>sin</mi><mn>2</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><mn>3</mn><mo>-</mo><mn>4</mn><mfenced><mfrac><mn>9</mn><mn>16</mn></mfrac></mfenced></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="[" close="]"><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>9</mn><mn>16</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mfenced close="]" open="["><mrow><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mn>4</mn><mi>&#952;</mi><mo>+</mo><mi>sin</mi><mn>6</mn><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>16</mn><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>-</mo><mfrac><mn>9</mn><mn>16</mn></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mn>23</mn></math></p>

</details>

---

### Q20. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cot</mi><mfrac><mi>&#960;</mi><mn>24</mn></mfrac></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>2</mn><mo>-</mo><msqrt><mn>6</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>2</mn><mo>+</mo><msqrt><mn>6</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>2</mn><mo>+</mo><msqrt><mn>6</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>6</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>2</mn><mo>+</mo><msqrt><mn>6</mn></msqrt></math>**

**Detailed Solution:**

<p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cot</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow><mrow><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow></mfrac></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>24</mn></mfrac></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cot</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></mrow><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cot</mi><mfenced><mfrac><mi>&#960;</mi><mn>24</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></mrow><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac><mo>&#215;</mo><mfrac><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>6</mn></msqrt><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>3</mn><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>6</mn></msqrt><mo>+</mo><msqrt><mn>2</mn></msqrt><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>2</mn><mo>.</mo></math></p>

</details>

---

### Q21. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mfrac><mi>&#960;</mi><mn>16</mn></mfrac></mfenced><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mfrac><mi>&#960;</mi><mn>16</mn></mfrac></mfenced><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mfenced></math></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>cos</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>cos</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>cos</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>cos</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>cos</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mi>sin</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>16</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>16</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>sin</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>16</mn></mfrac><mo>&#183;</mo><mi>sin</mi><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>16</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>cos</mi><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>16</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>16</mn></mfrac></mrow></mfenced><mo>-</mo><mi>cos</mi><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>16</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>16</mn></mfrac></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>-</mo><mi>cos</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mi>cos</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>16</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mrow></mfenced><mi>cos</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>16</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>cos</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>16</mn></mfrac><mo>&#183;</mo><mi>cos</mi><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>16</mn></mfrac></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>cos</mi><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>16</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>16</mn></mfrac></mrow></mfenced><mo>+</mo><mi>cos</mi><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>16</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>16</mn></mfrac></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mi>cos</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q22. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mn>3</mn></msup><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mfenced><mo>.</mo><mi>cos</mi><mfenced separators="|"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac></mfenced><mo>+</mo><msup><mi>sin</mi><mn>3</mn></msup><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mfenced><mo>.</mo><mi>sin</mi><mfenced separators="|"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac></mfenced></math> is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>3</mn></msup><mfenced><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mfenced><mi>cos</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mrow></mfenced><mo>+</mo><msup><mi>sin</mi><mn>3</mn></msup><mfenced><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mfenced><mi>sin</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>3</mn></msup><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mi>sin</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>+</mo><msup><mi>sin</mi><mn>3</mn></msup><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mi>cos</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mi>cos</mi><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p>

</details>

---

### Q23. JEE Main 2020 (08 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>2</mn></msqrt><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#945;</mi></mrow><msqrt><mn>1</mn><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>&#945;</mi></msqrt></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>&#946;</mi></mrow><mn>2</mn></mfrac></msqrt><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>,</mo><mtext>&#8201;</mtext><mi>&#946;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>, then <math><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#946;</mi></mrow></mfenced></math>, is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>&#945;</mi></mrow><msqrt><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>&#945;</mi></msqrt></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>&#946;</mi></mrow><mn>2</mn></mfrac></msqrt><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>,</mo><mtext>&#8201;</mtext><mi>&#946;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Now using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></math>, we can write</p><p><math><mfrac><mrow><msqrt><mn>2</mn><mi></mi></msqrt><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#945;</mi></mrow></mrow></mrow><mrow><msqrt><mn>2</mn></msqrt><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#945;</mi></mrow></mrow></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>7</mn></mrow></mfrac></math> and <math><mfrac><mrow><msqrt><mn>2</mn><mi></mi></msqrt><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#946;</mi></mrow></mrow></mrow><mrow><msqrt><mn>2</mn><mi></mi></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>10</mn></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"/>
<math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>7</mn></mrow></mfrac></mrow></mrow></math> and <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>10</mn></msqrt></mrow></mfrac></mrow></mrow></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>&#8289;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mi>a</mi><mi>n</mi><mn>2</mn><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>tan</mi><mo>&#8289;</mo><mi>&#946;</mi></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#946;</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mo>.</mo><mfrac><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></mfenced><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>9</mn></mfrac></mstyle></mfenced></mrow></mfenced></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>t</mi><mi>a</mi><mi>n</mi><mi>&#945;</mi><mo>+</mo><mi>t</mi><mi>a</mi><mi>n</mi><mn>2</mn><mi>&#946;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>t</mi><mi>a</mi><mi>n</mi><mi>&#945;</mi><mi>tan</mi><mo>&#8289;</mo><mn>2</mn><mi>&#946;</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mfrac><mn>1</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><mo>&#183;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mfrac><mrow><mn>4</mn><mo>+</mo><mn>21</mn></mrow><mn>28</mn></mfrac><mfrac><mn>25</mn><mn>28</mn></mfrac></mfrac><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q24. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>10</mn><mo>&#176;</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>30</mn><mo>&#176;</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>50</mn><mo>&#176;</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>70</mn><mo>&#176;</mo></math> is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>36</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>18</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>32</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>10</mn><mo>&#176;</mo><mi>sin</mi><mn>30</mn><mo>&#176;</mo><mi>sin</mi><mn>50</mn><mo>&#176;</mo><mi>sin</mi><mn>70</mn><mo>&#176;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>sin</mi><mn>10</mn><mo>&#176;</mo><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>2</mn><mi>sin</mi><mn>50</mn><mo>&#176;</mo><mi>sin</mi><mn>70</mn><mo>&#176;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>sin</mi><mn>10</mn><mo>&#176;</mo><mfenced separators="|"><mrow><mn>2</mn><mi>sin</mi><mn>50</mn><mo>&#176;</mo><mi>sin</mi><mn>70</mn><mo>&#176;</mo></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>sin</mi><mi>A</mi><mi>sin</mi><mi>B</mi><mo>=</mo><mi>cos</mi><mfenced><mrow><mi>A</mi><mo>-</mo><mi>B</mi></mrow></mfenced><mo>-</mo><mi>cos</mi><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>sin</mi><mn>10</mn><mo>&#176;</mo><mfenced><mrow><mi>cos</mi><mn>20</mn><mo>&#176;</mo><mo>-</mo><mi>cos</mi><mn>120</mn><mo>&#176;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>sin</mi><mn>10</mn><mo>&#176;</mo><mfenced><mrow><mi>cos</mi><mn>20</mn><mo>&#176;</mo><mo>-</mo><mi>cos</mi><mfenced><mrow><mn>90</mn><mo>&#176;</mo><mo>+</mo><mn>30</mn><mo>&#176;</mo></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>sin</mi><mn>10</mn><mo>&#176;</mo><mfenced><mrow><mi>cos</mi><mn>20</mn><mo>&#176;</mo><mo>+</mo><mi>sin</mi><mn>30</mn><mo>&#176;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>sin</mi><mn>10</mn><mo>&#176;</mo><mfenced><mrow><mi>cos</mi><mn>20</mn><mo>&#176;</mo><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mfenced separators="|"><mrow><mn>2</mn><mi>sin</mi><mn>10</mn><mo>&#176;</mo><mi>cos</mi><mn>20</mn><mo>&#176;</mo><mo>+</mo><mi>sin</mi><mn>10</mn><mo>&#176;</mo></mrow></mfenced></math></p><p>Again, using <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>sin</mi><mi>A</mi><mi>cos</mi><mi>B</mi><mo>=</mo><mi>sin</mi><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>-</mo><mi>sin</mi><mfenced><mrow><mi>A</mi><mo>-</mo><mi>B</mi></mrow></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mfenced separators="|"><mrow><mi>sin</mi><mn>30</mn><mo>&#176;</mo><mo>-</mo><mi>sin</mi><mn>10</mn><mo>&#176;</mo><mo>+</mo><mi>sin</mi><mn>10</mn><mo>&#176;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q25. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi mathvariant="normal">&#160;</mi><mo>,</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo></mrow></mrow><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>13</mn></mrow></mfrac></math> and <math><mn>0</mn><mo>&#60;</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#60;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>,</mo></math> then <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>&#945;</mi></mrow></mfenced></mrow></mrow></math> is equal to:

**Options:**

- **(A)** <math><mfrac><mrow><mn>21</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>63</mn></mrow><mrow><mn>52</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>33</mn></mrow><mrow><mn>52</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>63</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>63</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>&#8658;</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math></p><p><math><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>13</mn></mrow></mfrac><mo>&#8658;</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math></p><p>Now,</p><p><math><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>&#945;</mi><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mfenced separators="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced></mrow></mfenced></math></p><p>            <math><mo>=</mo><mfrac><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo></mrow><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mo>(</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>)</mo></mrow></mfrac></math></p><p>            <math><mo>=</mo><mfrac><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>12</mn></mrow></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>12</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>63</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math></p>

</details>

---

### Q26. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>m</mi></math> and <math><mi>M</mi></math> are the minimum and the maximum values of <math><mn>4</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow><mo>-</mo><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>,</mo><mi>&#160;</mi><mi>x</mi><mi>&#160;</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> then <math><mi>M</mi><mo>-</mo><mi>m</mi></math> is equal to:

**Options:**

- **(A)** <math> <mrow>  <mfrac>   <mrow>    <mn>15</mn>   </mrow>   <mn>4</mn>  </mfrac>   </mrow></math>
- **(B)** <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given expression is <math><mn>4</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow><mo>-</mo><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></math>

<math><mo>=&#160;</mo> </math><math><mn>4</mn><mo>+</mo><mn>2</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></math></p><p>Creating perfect squares, we get

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>4</mn><mi>&#160;</mi><mfenced open="{" close="}" separators="|"><mrow><msup><mfenced separators="|"><mrow><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mfrac><mn>17</mn><mn>16</mn></mfrac></mrow></mfenced><mi>&#160;</mi></math>

Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mi>&#160;</mi><mo>&#8804;</mo><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>x</mi><mi>&#160;</mi><mo>&#8804;</mo><mn>1</mn></math>

<math><mo>&#8658;</mo></math> <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mi>&#160;</mi><mo>&#8804;</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mi>&#160;</mi><mo>&#8804;</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo></math> <math><mn>0</mn><mi>&#160;</mi><mo>&#8804;</mo><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mo>&#8804;</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo></math> <math><mo>-</mo><mfrac><mrow><mn>17</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mi>&#160;</mi><mo>&#8804;</mo><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>17</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mi>&#160;</mi><mo>&#8804;</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>17</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>4</mn></mfrac><mi>&#160;</mi><mo>&#8805;</mo><mo>-</mo><mn>4</mn><mi>&#160;</mi><mfenced open="{" close="}" separators="|"><mrow><msup><mfenced separators="|"><mrow><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mfrac><mn>17</mn><mn>16</mn></mfrac></mrow></mfenced><mi>&#160;</mi><mo>&#8805;</mo><mn>2</mn></math>

<math><mo>&#8658;</mo></math> <math><mi>M</mi><mo>=</mo><mfrac><mrow><mn>17</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math> and <math><mi>m</mi><mo>=</mo><mrow><mn>2</mn></mrow></math>
<math><mo>&#8658;</mo></math> <math><mi>M</mi><mo>-</mo><mi>m</mi><mo>=</mo><mfrac><mrow><mn>17</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mrow><mn>2</mn></mrow><mo>=</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math></p>

</details>

---

### Q27. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>k</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>k</mi></mfrac><mfenced><mrow><msup><mi>sin</mi><mrow><mi>k</mi><mo>&#160;</mo></mrow></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mrow><mi>k</mi><mo>&#160;</mo></mrow></msup><mi>x</mi></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8805;1</mo></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>4</mn></msub><mfenced><mi>x</mi></mfenced><mo>-</mo><msub><mi>f</mi><mn>6</mn></msub><mfenced><mi>x</mi></mfenced></math> equals

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>1</mn> <mn>2</mn></mrow> </mfrac> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>1</mn> <mn>2</mn></mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>4</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><msup><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>&#160;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>&#160;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>6</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced open="[" close="]"><mrow><msup><mi>sin</mi><mn>6</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>6</mn></msup><mi>x</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced open="[" close="]"><mrow><msup><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>&#160;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced open="[" close="]"><mrow><mn>1</mn><mo>-</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>&#160;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>4</mn></msub><mfenced><mi>x</mi></mfenced><mo>-</mo><msub><mi>f</mi><mn>6</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mn>2</mn></mrow></mfrac></math>

</details>

---

