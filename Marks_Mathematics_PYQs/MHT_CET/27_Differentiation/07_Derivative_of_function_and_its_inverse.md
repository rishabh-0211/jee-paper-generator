# MHT CET Mathematics - Differentiation

## Topic 7: Derivative of function and its inverse

**Total Questions:** 13

---

### Q1. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)$ and $g(x)$ are inverse functions of each other and $f(x) = x + e^x$, then $g'(x) = $...

**Options:**

- **(A)** $\dfrac{1}{1 + e^{g(x)}}$
- **(B)** $\dfrac{e^{g(x)}}{1 + e^{g(x)}}$
- **(C)** $\dfrac{1}{1 + g(x)}$
- **(D)** $e^{g(x)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{1 + e^{g(x)}}$**

**Detailed Solution:**

Since $f(x)$ and $g(x)$ are inverse functions of each other, we have $f(g(x)) = x$.

Differentiating both sides with respect to $x$, we get:

$f'(g(x)) \cdot g'(x) = 1$

$g'(x) = \dfrac{1}{f'(g(x))}$

Given $f(x) = x + e^x$, differentiating with respect to $x$ gives:

$f'(x) = 1 + e^x$

Substituting $x$ with $g(x)$, we get:

$f'(g(x)) = 1 + e^{g(x)}$

Therefore, $g'(x) = \dfrac{1}{1 + e^{g(x)}}$.

Answer: $\dfrac{1}{1 + e^{g(x)}}$

</details>

---

### Q2. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x) = 3x^3 + 4e^{\frac{x}{2}}$ and $g(x) = f^{-1}(x)$. Then the value of $g'(4)$ is equal to...

**Options:**

- **(A)** $4$
- **(B)** $2$
- **(C)** $1$
- **(D)** $\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{2}$**

**Detailed Solution:**

Given $f(x) = 3x^3 + 4e^{\dfrac{x}{2}}$ and $g(x) = f^{-1}(x)$.

Using the derivative of an inverse function, $g'(x) = \dfrac{1}{f'(g(x))}$.

For $x = 4$, $g'(4) = \dfrac{1}{f'(g(4))}$.

To find $g(4)$, we set $f(x) = 4$:

$3x^3 + 4e^{\dfrac{x}{2}} = 4$

By inspection, $x = 0$ satisfies the equation, so $g(4) = 0$.

Differentiating $f(x)$ with respect to $x$:

$f'(x) = 9x^2 + 4 \cdot \dfrac{1}{2}e^{\dfrac{x}{2}} = 9x^2 + 2e^{\dfrac{x}{2}}$

Evaluating $f'(x)$ at $x = 0$:

$f'(0) = 9(0)^2 + 2e^{0} = 2$

Therefore, $g'(4) = \dfrac{1}{f'(0)} = \dfrac{1}{2}$.

Answer: $\dfrac{1}{2}$

</details>

---

### Q3. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = x + e^x$, then $\dfrac{d^2 x}{dy^2}$ is equal to

**Options:**

- **(A)** $\dfrac{e^x}{(1 + e^x)^2}$
- **(B)** $\dfrac{-e^x}{(1 + e^x)^2}$
- **(C)** $\dfrac{e^x}{(1 + e^x)^3}$
- **(D)** $\dfrac{-e^x}{(1 + e^x)^3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{-e^x}{(1 + e^x)^3}$**

**Detailed Solution:**

Given $y = x + e^x$

Differentiating with respect to $x$:

$\dfrac{dy}{dx} = 1 + e^x$

Taking the reciprocal:

$\dfrac{dx}{dy} = \dfrac{1}{1 + e^x}$

Differentiating with respect to $y$:

$\dfrac{d^2 x}{dy^2} = \dfrac{d}{dy} \left( \dfrac{dx}{dy} \right) = \dfrac{d}{dx} \left( \dfrac{dx}{dy} \right) \cdot \dfrac{dx}{dy}$

Substituting the values:

$\dfrac{d^2 x}{dy^2} = \dfrac{d}{dx} \left( \dfrac{1}{1 + e^x} \right) \cdot \left( \dfrac{1}{1 + e^x} \right)$

$\dfrac{d^2 x}{dy^2} = \left( \dfrac{-e^x}{(1 + e^x)^2} \right) \cdot \left( \dfrac{1}{1 + e^x} \right)$

$\dfrac{d^2 x}{dy^2} = \dfrac{-e^x}{(1 + e^x)^3}$

Answer: $\dfrac{-e^x}{(1 + e^x)^3}$

</details>

---

### Q4. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\frac{\mathrm{d} y}{\mathrm{~d} x}=y+3, y+3\gt0$ and $y(0)=2$, then $y(\log 2)$ is equal to

**Options:**

- **(A)** 13
- **(B)** $\quad-2$
- **(C)** 7
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7**

**Detailed Solution:**

Given differential equation is $\dfrac{\mathrm{d}y}{\mathrm{d}x} = y + 3$

Separating the variables, we get

$\dfrac{\mathrm{d}y}{y + 3} = \mathrm{d}x$

Integrating both sides, we get

$\int \dfrac{\mathrm{d}y}{y + 3} = \int \mathrm{d}x$

$\log(y + 3) = x + C$

Given $y(0) = 2$, substituting $x = 0$ and $y = 2$:

$\log(2 + 3) = 0 + C$

$C = \log 5$

Substituting $C$ back into the equation:

$\log(y + 3) = x + \log 5$

To find $y(\log 2)$, substitute $x = \log 2$:

$\log(y + 3) = \log 2 + \log 5$

$\log(y + 3) = \log(2 \times 5)$

$\log(y + 3) = \log 10$

$y + 3 = 10$

$y = 7$

Answer: 7

</details>

---

### Q5. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=\dfrac{x^2-x}{x^2+2 x}$ then $\dfrac{\mathrm{d}}{\mathrm{dx}}\left(\mathrm{f}^{-1}(x)\right)$ at $x=2$ is

**Options:**

- **(A)** -3
- **(B)** 3
- **(C)** -1
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3**

**Detailed Solution:**

$f(x) = \dfrac{x^2-x}{x^2+2x} = \dfrac{x(x-1)}{x(x+2)} = \dfrac{x-1}{x+2}$ for $x \neq 0, -2$

Let $y = f^{-1}(x)$, then $x = f(y)$

Differentiating with respect to $x$, we get $1 = f'(y) \dfrac{dy}{dx} \Rightarrow \dfrac{dy}{dx} = \dfrac{1}{f'(y)}$

To find $y$ when $x = 2$, we solve $f(y) = 2$:

$\dfrac{y-1}{y+2} = 2 \Rightarrow y - 1 = 2y + 4 \Rightarrow y = -5$

Now, differentiating $f(y)$ with respect to $y$:

$f'(y) = \dfrac{d}{dy}\left(\dfrac{y-1}{y+2}\right) = \dfrac{1(y+2) - (y-1)(1)}{(y+2)^2} = \dfrac{3}{(y+2)^2}$

At $y = -5$, $f'(-5) = \dfrac{3}{(-5+2)^2} = \dfrac{3}{9} = \dfrac{1}{3}$

Therefore, $\dfrac{d}{dx}\left(f^{-1}(x)\right)$ at $x=2$ is $\dfrac{1}{1/3} = 3$

Answer: 3

</details>

---

### Q6. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The displacement ' $\mathrm{S}$ ' of a moving particle at a time $t$ is given by $S=5+\frac{48}{t}+t^3$. Then its acceleration when the velocity is zero, is

**Options:**

- **(A)** $12$
- **(B)** $20$
- **(C)** $16$
- **(D)** $24$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $24$**

**Detailed Solution:**

Given, $S=5+\frac{48}{t}+t^3$
Velocity $(V)=\frac{d S}{d t}=0-\frac{48}{t^2}+3 t^2$
$\begin{aligned}
\therefore \quad & V=\frac{-48}{t^2}+3 t^2 ...(i)\\
& \text { But } V=0 ...[Given]\\
& \Rightarrow \frac{-48}{t^2}+3 t^2=0 \\
& \Rightarrow t=2
\end{aligned}$
Now, $\mathrm{A}=\frac{\mathrm{dV}}{\mathrm{dt}}$
$\begin{aligned}
& =\frac{d}{d t}\left(\frac{-48}{t^2}+3 t^2\right) \\
& =\frac{96}{t^3}+6 t
\end{aligned}$
Acceleration at $\mathrm{t}=2$ is $\frac{96}{8}+12=24$

</details>

---

### Q7. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $g$ is the inverse of $f$ and $f^{\prime}(x)=\frac{1}{1+x^3}$, then $g^{\prime}(x)$ is

**Options:**

- **(A)** $\frac{1}{1+(\operatorname{g}(x))^3}$
- **(B)** $1+(g(x))^3$
- **(C)** $\frac{g(x)}{1+(g(x))^3}$
- **(D)** $\frac{(g(x))^3}{1+(g(x))^3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1+(g(x))^3$**

**Detailed Solution:**

$\begin{array}{ll} & \mathrm{g}(x) \text { is inverse of function } \mathrm{f}(x) \\ & \text { i.e., } \mathrm{g}(x)=\mathrm{f}^{-1}(x) \\ & \mathrm{f}(\mathrm{g}(x))=x \\ & \text { differentiating w.r.t. } x \text {, we get } \\ & \mathrm{f}^{\prime}(\mathrm{g}(x)) \times \mathrm{g}^{\prime}(x)=1 \\ \therefore \quad & \mathrm{g}^{\prime}(x)=\frac{1}{\mathrm{f}^{\prime}(\mathrm{g}(x))}... (i)\end{array}$
Now, $\mathrm{f}^{\prime}(x)=\frac{1}{1+x^3}$... [Given]
$\therefore \quad \mathrm{f}^{\prime}(\mathrm{g}(x))=\frac{1}{1+(\mathrm{g}(x))^3}$ ... (ii)
$\therefore \quad$ From (i) and (ii), we get
$\begin{aligned}
& \therefore \quad \mathrm{g}^{\prime}(x)=1+(\mathrm{g}(x))^3 \\
&
\end{aligned}$

</details>

---

### Q8. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $\tan ^{-1}\left(\frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}\right)$ is

**Options:**

- **(A)** x
- **(B)** $\frac{1}{2 \sqrt{1-x^2}}$
- **(C)** $\frac{1}{\sqrt{1-x^2}}$
- **(D)** $\sqrt{1-x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2 \sqrt{1-x^2}}$**

**Detailed Solution:**

$\begin{aligned} & y=\tan ^{-1}\left(\frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}\right) \text { let } x=\cos 2 \theta \\ & \Rightarrow \theta=\frac{1}{2} \cos ^{-1} x \\ & \Rightarrow y=\tan ^{-1}\left(\frac{\sqrt{1+\cos 2 \theta}-\sqrt{1-\cos 2 \theta}}{\sqrt{1+\cos 2 \theta}+\sqrt{1-\cos 2 \theta}}\right) \\ & \Rightarrow y=\tan ^{-1}\left(\frac{\sqrt{2} \cos \theta-\sqrt{2} \sin \theta}{\sqrt{2} \cos \theta+\sqrt{2} \sin \theta}\right)=\tan ^{-1}\left(\frac{1-\tan \theta}{1+\tan \theta}\right) \\ & \Rightarrow y=\tan ^{-1} \tan \left(\frac{\pi}{4}-\theta\right)=\frac{\pi}{4}-\theta=\frac{\pi}{4}-\frac{1}{2} \cos ^{-1} x \\ & \Rightarrow \frac{d y}{d x}=0-\frac{1}{2} \times \frac{-1}{\sqrt{1-x^2}}=\frac{1}{2 \sqrt{1-x^2}}\end{aligned}$

</details>

---

### Q9. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\cos \left(\sin x^2\right)$, then $\frac{d y}{d x} a t x=\sqrt{\frac{\pi}{2}}$ is

**Options:**

- **(A)** $-2$
- **(B)** $0$
- **(C)** $2$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0$**

**Detailed Solution:**

$\begin{aligned} & y=\cos \left(\sin x^2\right) \\ & \Rightarrow \frac{d y}{d x}=-\sin \left(\sin x^2\right) \cdot \cos x^2 \cdot 2 x \\ & \frac{d y}{d x}\left(a t x \sqrt{\frac{\pi}{2}}\right)=-\sin \left(\sin \frac{\pi}{2}\right) \cdot \cos \cdot 2 \times \sqrt{\frac{\pi}{2}} \\ & =-\sin (1) \times 0 \times 2 \times \sqrt{\frac{\pi}{2}}=0\end{aligned}$

</details>

---

### Q10. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\frac{d}{d x}\left(\sqrt{\frac{1-\tan x}{1+\tan x}}\right)=$

**Options:**

- **(A)** $\frac{\sec ^2 x}{(1+\tan x)^{3 / 2}(1-\tan x)^{1 / 2}}$
- **(B)** $\frac{-\sec ^2 x}{\left(1-\tan ^2 x\right)^{1 / 2}}$
- **(C)** $\frac{\sec ^2 x}{\left(1-\tan ^2 x\right)^{1 / 2}}$
- **(D)** $\frac{-\sec ^2 x}{(1+\tan x)^{3 / 2}(1-\tan x)^{1 / 2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{-\sec ^2 x}{(1+\tan x)^{3 / 2}(1-\tan x)^{1 / 2}}$**

**Detailed Solution:**

$\begin{aligned} & \frac{d}{d x}\left(\sqrt{\frac{1-\tan x}{1+\tan x}}\right)=\frac{1}{\sqrt[2]{\frac{1-\tan x}{1+\tan x}}} \times \frac{(1+\tan x)\left(0-\sec ^2 x\right)-(1-\tan x)\left(0-\sec ^2 x\right)}{(1+\tan x)^2} \\ & =\frac{2 \sec ^2 x}{2 \sqrt{1-\tan x}(1+\tan x)^{3 / 2}} \\ & =\frac{\sec ^2 x}{(1-\tan x)^{1 / 2} \cdot(1+\tan x)^{3 / 2}}\end{aligned}$

</details>

---

### Q11. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is the inverse function of <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> and <math> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mfrac> <mn>1</mn> <mrow> <mn>1</mn><mo>+</mo><msup> <mi>x</mi> <mn>4</mn> </msup> </mrow> </mfrac> <mo>,</mo> </mrow> </math> then <math> <mrow> <msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> </math> is

**Options:**

- **(A)** <math><mn>1</mn><mo>+</mo><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></math>
- **(B)** <math><mn>1</mn><mo>-</mo><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></math>
- **(C)** <math><mn>1</mn><mo>+</mo><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>1</mn><mo>+</mo><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></math>**

**Detailed Solution:**

<math><mi>g</mi><mo>=</mo><msup><mrow><mi>f</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
<math><mi>f</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi></math>
Differentiate w.r.t x
<math> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mrow> <mi>g</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> <mo>)</mo></mrow><mo>.</mo><msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mn>1</mn> </mrow> </math>
<math> <mrow> <mo>∴</mo><mi> </mi><mfrac> <mn>1</mn> <mrow> <mn>1</mn><mo>+</mo><msup> <mrow> <mrow><mo>(</mo> <mrow> <mi>g</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow> </mrow> <mo>)</mo></mrow> </mrow> <mn>4</mn> </msup> </mrow> </mfrac> <mo>.</mo><msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mn>1</mn> </mrow> </math>
<math > <mrow>  <msup>   <mi>g</mi>   <mo>&#x2032;</mo>  </msup>  <mrow><mo>(</mo>   <mi>x</mi>  <mo>)</mo></mrow><mo>=</mo><mn>1</mn><mo>+</mo><msup>   <mrow>    <mrow><mo>[</mo> <mrow>     <mi>g</mi><mrow><mo>(</mo>      <mi>x</mi>     <mo>)</mo></mrow>    </mrow> <mo>]</mo></mrow>   </mrow>   <mn>4</mn>  </msup>   </mrow></math>

</details>

---

### Q12. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=|x-3|$, then $f^{\prime}(3)$ is

**Options:**

- **(A)** $-1$
- **(B)** 1
- **(C)** 0
- **(D)** does not exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) does not exist**

**Detailed Solution:**

Given, $f(x)=|x-3|$ Redefine this function:
$$
f(x)=\left\{\begin{array}{cc}
3-x, & x < 3 \\
0, & x=3 \\
x-3, & x>3
\end{array}\right.
$$
$f^{\prime}(x)=\left\{\begin{aligned}-1, & x < 3 \\ 0, & x=3 \\ 1, & x>3 \end{aligned}\right.$
It is clear that, $L f^{\prime}(3) \neq R f^{\prime}(3)$. $\therefore f^{\prime}(3)$ does not exist.

</details>

---

### Q13. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

If $y^{2}=a x^{2}+b x+c, \quad$ where $\quad a, b, c$ are constants, then $y^{3} \frac{d^{2} y}{d x^{2}}$ is equal to

**Options:**

- **(A)** a constant
- **(B)** a function of $x$
- **(C)** a function of $y$
- **(D)** a function of $x$ and $y$ both

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) a constant**

**Detailed Solution:**

Given, $y^{2}=a x^{2}+b x+c$
On differentiating w.r.t. $x$, we get $2 y \frac{d y}{d x}=2 a x+b$
Again differentiating w.r.t. $x$, we get
$$
\begin{aligned}
& 2\left(\frac{d y}{d x}\right)^{2}+2 y \frac{d^{2} y}{d x^{2}}=2 a \\
\Rightarrow & y \frac{d^{2} y}{d x^{2}}=a-\left(\frac{d y}{d x}\right)^{2}
\end{aligned}
$$
$\Rightarrow \quad y \frac{d^{2} y}{d x^{2}}=a-\left(\frac{2 a x+b}{2 y}\right)^{2}$
$\Rightarrow \quad y \frac{d^{2} y}{d x^{2}}=\frac{4 a y^{2}-(2 a x+b)^{2}}{4 y^{2}}$
$\Rightarrow \quad 4 y^{3} \frac{d^{2} y}{d x^{2}}=4 a\left(a x^{2}+b x+c\right)$
$-\left(4 a^{2} x^{2}+4 a b x+b^{2}\right)$
$\Rightarrow \quad 4 y^{3} \frac{d^{2} y}{d x^{2}}=4 a c-b^{2}$
$\Rightarrow \quad y^{3} \frac{d^{2} y}{d x^{2}}=\frac{4 a c-b^{2}}{4}=$ constant

</details>

---

