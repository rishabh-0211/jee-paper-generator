# MHT CET Mathematics - Functions

## Topic 8: Functional Equation

**Total Questions:** 18

---

### Q1. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) + 2f(1 - x) = x^2 + 5$ for all real $x$, then $f(x)$ is equal to...

**Options:**

- **(A)** $\dfrac{(x-2)^2 + 3}{3}$
- **(B)** $\dfrac{(x-2)^2 - 3}{3}$
- **(C)** $\dfrac{(x-3)^2 - 2}{2}$
- **(D)** $\dfrac{(x-3)^2 + 2}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{(x-2)^2 + 3}{3}$**

**Detailed Solution:**

Given equation is $f(x) + 2f(1 - x) = x^2 + 5$.

Replacing $x$ with $1 - x$, we get:

$f(1 - x) + 2f(1 - (1 - x)) = (1 - x)^2 + 5$

$2f(x) + f(1 - x) = x^2 - 2x + 6$

Multiplying this equation by $2$ and subtracting the given equation from it:

$2(2f(x) + f(1 - x)) - (f(x) + 2f(1 - x)) = 2(x^2 - 2x + 6) - (x^2 + 5)$

$4f(x) - f(x) = 2x^2 - 4x + 12 - x^2 - 5$

$3f(x) = x^2 - 4x + 7$

$f(x) = \dfrac{x^2 - 4x + 7}{3}$

$f(x) = \dfrac{(x - 2)^2 + 3}{3}$

Answer: $\dfrac{(x-2)^2 + 3}{3}$

</details>

---

### Q2. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f\left(\dfrac{x-1}{x+1}\right) = x + 1$, then $\int f(x)\,dx = \cdots$

**Options:**

- **(A)** $2\log|1 - x| + c$
- **(B)** $-2\log|1 - x| + c$
- **(C)** $2\log|1 + x| + c$
- **(D)** $-2\log|1 + x| + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-2\log|1 - x| + c$**

**Detailed Solution:**

Let $t = \dfrac{x-1}{x+1}$

$t(x+1) = x-1$

$tx + t = x - 1$

$x(1-t) = t+1$

$x = \dfrac{t+1}{1-t}$

Substituting $x$ in the given equation:

$f(t) = \dfrac{t+1}{1-t} + 1$

$f(t) = \dfrac{t+1+1-t}{1-t} = \dfrac{2}{1-t}$

Replacing $t$ with $x$:

$f(x) = \dfrac{2}{1-x}$

Integrating with respect to $x$:

$\int f(x)\,dx = \int \dfrac{2}{1-x}\,dx$

$\int f(x)\,dx = -2\log|1-x| + c$

Answer: $-2\log|1 - x| + c$

</details>

---

### Q3. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x-y) + f(x+y) = 2f(x)f(y)$ for all $x, y \in \mathbb{R}$, then $f(x)$ is .....

**Options:**

- **(A)** an odd function
- **(B)** an even function
- **(C)** neither even nor odd function
- **(D)** a periodic function

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) an even function**

**Detailed Solution:**

Given the functional equation:

$f(x-y) + f(x+y) = 2f(x)f(y)$

Substituting $y = 0$, we get:

$f(x) + f(x) = 2f(x)f(0)$

$2f(x) = 2f(x)f(0)$

$f(x)(1 - f(0)) = 0$

This implies that either $f(x) = 0$ for all $x \in \mathbb{R}$, or $f(0) = 1$.

Case 1: If $f(x) = 0$ for all $x$, then $f(-x) = 0 = f(x)$. Thus, $f(x)$ is an even function.

Case 2: If $f(0) = 1$, substitute $x = 0$ in the given functional equation:

$f(0-y) + f(0+y) = 2f(0)f(y)$

$f(-y) + f(y) = 2(1)f(y)$

$f(-y) = f(y)$

This shows that $f(x)$ is an even function.

In all possible cases, $f(x)$ is an even function.

</details>

---

### Q4. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The values of b and c for which the identity $\mathrm{f}(x+1)-\mathrm{f}(x)=8 x+3$ is satisfied, where $\mathrm{f}(x)=\mathrm{b} x^2+\mathrm{c} x+\mathrm{d}$, are

**Options:**

- **(A)** $b=2, c=1$
- **(B)** $b=4, c=-1$
- **(C)** $b=1, c=2$
- **(D)** $b=3, c=-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $b=4, c=-1$**

**Detailed Solution:**

Given $\mathrm{f}(x) = \mathrm{b} x^2 + \mathrm{c} x + \mathrm{d}$.

$\mathrm{f}(x+1) = \mathrm{b}(x+1)^2 + \mathrm{c}(x+1) + \mathrm{d}$

$\mathrm{f}(x+1) = \mathrm{b}(x^2 + 2x + 1) + \mathrm{c}x + \mathrm{c} + \mathrm{d}$

$\mathrm{f}(x+1) = \mathrm{b}x^2 + 2\mathrm{b}x + \mathrm{b} + \mathrm{c}x + \mathrm{c} + \mathrm{d}$

Subtracting $\mathrm{f}(x)$:

$\mathrm{f}(x+1) - \mathrm{f}(x) = (\mathrm{b}x^2 + 2\mathrm{b}x + \mathrm{b} + \mathrm{c}x + \mathrm{c} + \mathrm{d}) - (\mathrm{b}x^2 + \mathrm{c}x + \mathrm{d})$

$\mathrm{f}(x+1) - \mathrm{f}(x) = 2\mathrm{b}x + \mathrm{b} + \mathrm{c}$

Given identity:

$\mathrm{f}(x+1) - \mathrm{f}(x) = 8x + 3$

Equating the two expressions:

$2\mathrm{b}x + (\mathrm{b} + \mathrm{c}) = 8x + 3$

Comparing the coefficients of $x$ and the constant terms:

$2\mathrm{b} = 8 \Rightarrow \mathrm{b} = 4$

$\mathrm{b} + \mathrm{c} = 3$

Substituting $\mathrm{b} = 4$ in the second equation:

$4 + \mathrm{c} = 3 \Rightarrow \mathrm{c} = -1$

Thus, $\mathrm{b} = 4$ and $\mathrm{c} = -1$.

Answer: $b=4, c=-1$

</details>

---

### Q5. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{f}(x)=(x+1)^2-1, x \geqslant-1$, then the set $\left\{x / \mathrm{f}(x)=\mathrm{f}^{-1}(x)\right\}$ is

**Options:**

- **(A)** $\{0,1,-1\}$
- **(B)** $\{0,-1\}$
- **(C)** $\left\{0,-1, \frac{-3+\mathrm{i} \sqrt{3}}{2}, \frac{-3-\mathrm{i} \sqrt{3}}{2}\right.$, where $\left.\mathrm{i}=\sqrt{-1}\right\}$
- **(D)** $\phi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\{0,-1\}$**

**Detailed Solution:**

Given $\mathrm{f}(x) = (x+1)^2 - 1$ for $x \geqslant -1$.

Let $y = (x+1)^2 - 1$

$\Rightarrow y + 1 = (x+1)^2$

Since $x \geqslant -1$, $x+1 \geqslant 0$. Taking the square root on both sides:

$x+1 = \sqrt{y+1}$

$\Rightarrow x = \sqrt{y+1} - 1$

Therefore, $\mathrm{f}^{-1}(x) = \sqrt{x+1} - 1$

We need to find $x$ such that $\mathrm{f}(x) = \mathrm{f}^{-1}(x)$.

$(x+1)^2 - 1 = \sqrt{x+1} - 1$

$\Rightarrow (x+1)^2 = \sqrt{x+1}$

Let $x+1 = t$. Since $x \geqslant -1$, $t \geqslant 0$.

$t^2 = \sqrt{t}$

Squaring both sides:

$t^4 = t$

$\Rightarrow t(t^3 - 1) = 0$

$\Rightarrow t(t-1)(t^2+t+1) = 0$

Since $t$ is a real number and $t \geqslant 0$, the only possible values are $t = 0$ and $t = 1$.

For $t = 0$, $x+1 = 0 \Rightarrow x = -1$

For $t = 1$, $x+1 = 1 \Rightarrow x = 0$

Thus, the required set is $\{0, -1\}$.

Answer: $\{0,-1\}$

</details>

---

### Q6. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{f}:[-1,3] \rightarrow \mathbb{R}$ be defined as
$\begin{cases}|x|+[x], & -1 \leqslant x \lt 1 \\ x+|x|, & 1 \leqslant x \lt 2 \\ x+[x], & 2 \leqslant x \leqslant 3\end{cases}$
where $[t]$ denotes the greatest integer function.
Then f is discontinuous at

**Options:**

- **(A)** only two points
- **(B)** only three points
- **(C)** four or more points
- **(D)** only one point

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) only three points**

**Detailed Solution:**

The given function is:

$f(x) = \begin{cases} |x| + [x], & -1 \leqslant x < 1 \\ x + |x|, & 1 \leqslant x < 2 \\ x + [x], & 2 \leqslant x \leqslant 3 \end{cases}$

We check the continuity at the critical points $x = -1, 0, 1, 2, 3$.

At $x = -1$:
$\lim_{x \to -1^+} f(x) = \lim_{x \to -1^+} (|x| + [x]) = |-1| + (-1) = 1 - 1 = 0$
$f(-1) = |-1| + [-1] = 1 - 1 = 0$
Since $\lim_{x \to -1^+} f(x) = f(-1)$, $f(x)$ is continuous at $x = -1$.

At $x = 0$:
$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (|x| + [x]) = 0 + (-1) = -1$
$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} (|x| + [x]) = 0 + 0 = 0$
Since $\lim_{x \to 0^-} f(x) \neq \lim_{x \to 0^+} f(x)$, $f(x)$ is discontinuous at $x = 0$.

At $x = 1$:
$\lim_{x \to 1^-} f(x) = \lim_{x \to 1^-} (|x| + [x]) = 1 + 0 = 1$
$\lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} (x + |x|) = 1 + 1 = 2$
Since $\lim_{x \to 1^-} f(x) \neq \lim_{x \to 1^+} f(x)$, $f(x)$ is discontinuous at $x = 1$.

At $x = 2$:
$\lim_{x \to 2^-} f(x) = \lim_{x \to 2^-} (x + |x|) = 2 + 2 = 4$
$\lim_{x \to 2^+} f(x) = \lim_{x \to 2^+} (x + [x]) = 2 + 2 = 4$
$f(2) = 2 + [2] = 2 + 2 = 4$
Since $\lim_{x \to 2^-} f(x) = \lim_{x \to 2^+} f(x) = f(2)$, $f(x)$ is continuous at $x = 2$.

At $x = 3$:
$\lim_{x \to 3^-} f(x) = \lim_{x \to 3^-} (x + [x]) = 3 + 2 = 5$
$f(3) = 3 + [3] = 3 + 3 = 6$
Since $\lim_{x \to 3^-} f(x) \neq f(3)$, $f(x)$ is discontinuous at $x = 3$.

Thus, $f(x)$ is discontinuous at exactly three points: $x = 0, 1, 3$.

Answer: only three points

</details>

---

### Q7. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

For a suitable chosen real constant a, let a function $\mathrm{f}: \mathbb{R}-\{-\mathrm{a}\} \rightarrow \mathbb{R}$ be defined by $\mathrm{f}(x)=\dfrac{\mathrm{a}-x}{\mathrm{a}+x}$. Further suppose that for any real number $x \neq-\mathrm{a}$ and $\mathrm{f}(x) \neq-\mathrm{a}$, (fof) $(x)=x$. Then $\mathrm{f}\left(-\dfrac{1}{5}\right)$ is equal to

**Options:**

- **(A)** 1.5
- **(B)** $2 \cdot 0$
- **(C)** $1 \cdot 0$
- **(D)** $3 \cdot 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1.5**

**Detailed Solution:**

Given $f(x) = \dfrac{a-x}{a+x}$

Evaluating $f(f(x))$:

$f(f(x)) = \dfrac{a - f(x)}{a + f(x)} = \dfrac{a - \dfrac{a-x}{a+x}}{a + \dfrac{a-x}{a+x}}$

$f(f(x)) = \dfrac{a(a+x) - (a-x)}{a(a+x) + (a-x)} = \dfrac{a^2 + ax - a + x}{a^2 + ax + a - x}$

$f(f(x)) = \dfrac{a^2 - a + x(a+1)}{a^2 + a + x(a-1)}$

Since $f(f(x)) = x$ for all valid $x$, we get:

$\dfrac{a^2 - a + x(a+1)}{a^2 + a + x(a-1)} = x$

$a^2 - a + x(a+1) = x(a^2 + a) + x^2(a-1)$

For this equation to hold for all $x$, the coefficients of corresponding powers of $x$ must be equal on both sides.

Comparing the coefficient of $x^2$:

$a - 1 = 0 \Rightarrow a = 1$

Comparing the constant term:

$a^2 - a = 0 \Rightarrow 1^2 - 1 = 0$, which is consistent.

Substituting $a = 1$ into the function gives:

$f(x) = \dfrac{1-x}{1+x}$

Evaluating $f\left(-\dfrac{1}{5}\right)$:

$f\left(-\dfrac{1}{5}\right) = \dfrac{1 - \left(-\dfrac{1}{5}\right)}{1 + \left(-\dfrac{1}{5}\right)} = \dfrac{1 + \dfrac{1}{5}}{1 - \dfrac{1}{5}} = \dfrac{\dfrac{6}{5}}{\dfrac{4}{5}} = \dfrac{6}{4} = 1.5$

Answer: 1.5

</details>

---

### Q8. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $3 \mathrm{f}(x)-\mathrm{f}\left(\frac{1}{x}\right)=8 \log _2 x^3, x>0$, then $\mathrm{f}(2), \mathrm{f}(4)$ $\mathrm{f}(8)$ are in

**Options:**

- **(A)** A.P.
- **(B)** G.P.
- **(C)** H.P.
- **(D)** Arithmetico Geometric Progression.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A.P.**

**Detailed Solution:**

$$
\begin{aligned}
& 3 f(x)-f\left(\frac{1}{x}\right)=8 \log _2 x^3 \\
& \Rightarrow 3 \mathrm{f}\left(\frac{1}{x}\right)-\mathrm{f}(x)=8 \log _2\left(\frac{1}{x}\right)^3 .
\end{aligned}
$$
From (i) and (ii), we get
$$
\begin{aligned}
& 8 \mathrm{f}(x)=24 \log _2 x^3+8 \log _2\left(\frac{1}{x}\right)^3 \\
& \Rightarrow 8 \mathrm{f}(x)=72 \log _2 x-24 \log _2 x \\
& \Rightarrow 8 \mathrm{f}(x)=48 \log _2 x \\
& \Rightarrow \mathrm{f}(x)=6 \log _2 x
\end{aligned}
$$
$\begin{array}{ll}\therefore \quad & f^{\prime}(2)=6 \log _2 2=6 \\ & f^{\prime}(4)=6 \log _2 4=12 \\ & f^{(}(8)=6 \log _2 8=18 \\ \therefore \quad & f(2), f(4), f(8) \text { are in A.P. }\end{array}$

</details>

---

### Q9. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $f: R \rightarrow R$ be a differentiable function with $f(0)=1$ and satisfying the equation $f(x+y)=f(x) \cdot f^{\prime}(y)+f^{\prime}(x) \cdot f(y), \forall x, y \in R$, then the value of $\log (f(4))$ is

**Options:**

- **(A)** 1
- **(B)** 4
- **(C)** 2
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

$f(x+y)=f(x) \cdot f^{\prime}(y)+f^{\prime}(x) \cdot f(y) \forall x, y \in R$
putting $x=y=0$ we get
$\begin{aligned} & f(0)=2 f(0) \cdot f^{\prime}(0) \\ & \Rightarrow f^{\prime}(0)=\frac{1}{2}[\because \text { given } f(0)=1]\end{aligned}$
Now putting $x=x$ and $y=0$
$\begin{aligned} & f(x)=f(x) \cdot f^{\prime}(0)+f^{\prime}(x) \cdot f(0) \\ & \Rightarrow f(x)=\frac{1}{2} f(x)+f^{\prime}(x)\left[\because f(0)=1 \text { and } f^{\prime}(0)=\frac{1}{2}\right] \\ & \Rightarrow \frac{1}{2} f(x)=f^{\prime}(x) \\ & \Rightarrow \int \frac{f^{\prime}(x)}{f(x)} \mathrm{d} x=\int \frac{1}{2} \mathrm{~d} x \\ & \Rightarrow \log (f(x))=\frac{1}{2} x+c \\ & \because f(0)=1 \\ & \Rightarrow c=0\end{aligned}$
i.e., $\log (f(x))=\frac{1}{2} x$ putting $x=4$
$\log (f(4))=\frac{1}{2} \times 4=2$

</details>

---

### Q10. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\cos (\log x)$, then $f(x) \cdot f(y)-\frac{1}{2}\left(f\left(\frac{x}{y}\right)+f(x y)\right)$ has the value

**Options:**

- **(A)** $-2$
- **(B)** $-1$
- **(C)** $0$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0$**

**Detailed Solution:**

$\begin{aligned} & f(x)=\cos (\log x) \\ & \text { Now, } f(x) \cdot f(y)-\frac{1}{2}\left(f\left(\frac{x}{y}\right)+f(x y)\right) \\ & =\cos (\log x) \cdot \cos (\log y)-\frac{1}{2}\left(\cos \log \left(\frac{x}{y}\right)+\cos \log (x y)\right) \\ & =\cos (\log x) \cdot \cos (\log y)-\frac{1}{2}\{\cos (\log x-\log y)+\cos (\log x+\log y)\} \\ & =\cos (\log x) \cdot \cos (\log y)-\frac{1}{2} \times 2 \cos (\log x) \cdot \cos (\log y) \\ & =0\end{aligned}$

</details>

---

### Q11. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(\mathrm{x})=2\{\mathrm{x}\}+5 \mathrm{x}$, where $\{\mathrm{x}\}$ is fractional part function, then $f(-1.4)$ is

**Options:**

- **(A)** 8.2
- **(B)** -8.2
- **(C)** -5.8
- **(D)** -5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -5.8**

**Detailed Solution:**

We know that $\mathrm{x}=[\mathrm{x}]+\{\mathrm{x}\}$
When $\mathrm{x}=-1.4$, we get $[\mathrm{x}]=-2$ and $\{\mathrm{x}\}=0.6$
We have $f(x)=2\{x\}+5 x$
$\therefore \mathrm{f}(-1.4)=2(0.6)+5(-1.4)=-7+1.2=-5.8$

</details>

---

### Q12. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=[8 x]-3$, where $[x]$ is greatest integer function of $x$, then $\mathrm{f}(\pi)=$

**Options:**

- **(A)** 21
- **(B)** 25
- **(C)** 23
- **(D)** 22

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 22**

**Detailed Solution:**

$f(x)=[8 x]-3$
$\therefore \mathrm{f}(\pi)=[8(3.14)]-3=[25.12]-3=25-3=22$

</details>

---

### Q13. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=3[x]+\{x+1\}$, where $[x]$ is greatest integer function of $x$ and $\{x\}$ is fractional part function of $x$, then $f(-1.32)=$

**Options:**

- **(A)** -4.6
- **(B)** -2.6
- **(C)** -7.4
- **(D)** -3.4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -2.6**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{f}(\mathrm{x})=3[\mathrm{x}]+5\{\mathrm{x}+1\} \\
& \mathrm{x}=-1.32 \Rightarrow[\mathrm{x}]=[-1.32]=-2 \\
& \text { Also } \mathrm{x}+1=-1.32+1=-0.32 \\
& \therefore[\mathrm{x}+1]=[-0.32]=-1 \text { and }\{\mathrm{x}+1\}=0.68 \\
& \therefore \mathrm{f}(\mathrm{x})=3(-2)+5(0.68) \\
& =-6+3.4=-2.6
\end{aligned}
$$

</details>

---

### Q14. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $2 f(x)-3 f\left(\frac{1}{x}\right)=x$, then $\int_1^e f(x) d x=$

**Options:**

- **(A)** $-\left(\frac{2+\mathrm{e}^2}{5}\right)$
- **(B)** $\frac{2+\mathrm{e}}{5}$
- **(C)** $\frac{2+\mathrm{e}^2}{5}$
- **(D)** $\frac{2-\mathrm{e}^2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\left(\frac{2+\mathrm{e}^2}{5}\right)$**

**Detailed Solution:**

$2 f(x)-3 f\left(\frac{1}{x}\right)=x$
...(1) and replacing $x$ by $\frac{1}{x}$, we get
$$
2 f\left(\frac{1}{x}\right)-3 f(x)=\frac{1}{x}
$$
[ $2 \times$ equation (1) $]+[3 \times$ equation (2) $]$ gives,
$$
\begin{aligned}
& 4 f(x)-9 f(x)=2 x+\frac{3}{x} \quad \Rightarrow-5 f(x)=2 x+\frac{3}{x} \\
& \therefore f(x)=\frac{-2}{5} x-\frac{3}{5 x}
\end{aligned}
$$


$$
\begin{aligned}
& \therefore \int_1^{\mathrm{e}} \mathrm{f}(\mathrm{x}) \mathrm{dx}=\int_1^{\mathrm{e}}\left(\frac{-2}{5} \mathrm{x}-\frac{3}{5 \mathrm{x}}\right) \mathrm{d} x=\frac{-2}{5} \int_1^{\mathrm{e}} \mathrm{x} d \mathrm{x}-\frac{3}{5} \int_1^{\mathrm{e}} \frac{1}{\mathrm{x}} \mathrm{dx} \\
& =\frac{-2}{5}\left[\frac{\mathrm{x}^2}{2}\right]_1^{\mathrm{e}}-\frac{3}{5}[\log \mathrm{x}]_1^{\mathrm{e}}=\frac{-1}{5}\left(\mathrm{e}^2-1\right)-\frac{3}{5}(\log \mathrm{e}-\log 1)=\frac{-1}{5} \mathrm{e}^2+\frac{1}{5}-\frac{3}{5} \\
& =-\left(\frac{2+\mathrm{e}^2}{5}\right)
\end{aligned}
$$

</details>

---

### Q15. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=[x]^{2}-5[x]+6=0$, where $[x]$ denotes greatest integer function
then $x \in$

**Options:**

- **(A)** $(2,4]$
- **(B)** $[2,4]$
- **(C)** $[2,4)$
- **(D)** $(2,4)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $[2,4)$**

**Detailed Solution:**

We have, $[x]^{2}-5[x]+6=0$
$\therefore([x]-3)([x]-2)=0 \Rightarrow[x]=2,3$
For $[x]=2, x \in[2,3)$ and for $[x]=3, x \in[3,4)$
$\therefore \quad x \in[2,4)$

</details>

---

### Q16. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\frac{2^{x}+2^{-x}}{2}$, then $f(x+y) \cdot f(x-y)$ is

**Options:**

- **(A)** $\frac{1}{4}[f(2 x)-f(2 y)]$
- **(B)** $\frac{1}{2}[f(2 x)-f(2 y)]$
- **(C)** $\frac{1}{4}[f(2 x)+f(2 y)]$
- **(D)** $\frac{1}{2}[f(2 x)+f(2 y)]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2}[f(2 x)+f(2 y)]$**

**Detailed Solution:**

Given $f(x)=\frac{2^{x}+2^{-x}}{2}$
Now, $f(x+y)=\frac{2^{x+y}+2^{-x-y}}{2}$
and $f(x-y)=\frac{2^{x-y}+2^{-x+y}}{2}$
$\therefore f(x+y) \cdot f(x-y)$
$=\frac{\left(2^{x+y}+2^{-x-y}\right)}{2} \cdot \frac{\left(2^{x-y}+2^{-x+y}\right)}{2}$
$=\frac{2^{2 x}+2^{-2 y}+2^{2 y}+2^{-2 x}}{4}$
$=\frac{1}{2}\left\{\left(\frac{2^{2 x}+2^{-2 x}}{2}\right)+\left(\frac{2^{2 y}+2^{-2 y}}{2}\right)\right\}$
$=\frac{1}{2}\{f(2 x)+f(2 y)\}$

</details>

---

### Q17. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x+y)=f(x) \cdot f(y), \forall x, y \in R$, suppose that $f(3)=3$ and $f^{\prime}(0)=11$, then $f^{\prime}(3)$ is given by

**Options:**

- **(A)** 22
- **(B)** 44
- **(C)** 28
- **(D)** 33

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 33**

**Detailed Solution:**

$f^{\prime}(3)=\lim _{h \rightarrow 0} \frac{f(3+h)-f(3)}{h}$
$$
\begin{aligned}
&=\lim _{h \rightarrow 0} \frac{f(3) \cdot f(h)-f(3)}{h} \\
\Rightarrow \quad f^{\prime}(3) &=3 \lim _{h \rightarrow 0} \frac{f(h)-1}{h}
\end{aligned}
$$
$[\because f(3)=3]$
Use L'Hospital rule,
$$
\begin{aligned}
\Rightarrow \quad f^{\prime}(3) &=3 \lim _{h \rightarrow 0} \frac{f^{\prime}(h)}{1} \\
&=3 f^{\prime}(0)
\end{aligned}
$$
$\left[\because f^{\prime}(0)=11\right]$
$$
=3 \times 11=33
$$

</details>

---

### Q18. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

Missing term in the following table is
$\begin{array}{lllllll}x & : & 0 & 1 & 2 & 3 & 4 \\ y=f(x) & : & 1 & 3 & 9 & ? & 81\end{array}$

**Options:**

- **(A)** 27
- **(B)** 30
- **(C)** 31
- **(D)** 34

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 31**

**Detailed Solution:**

Here, 4 values are given, therefore
$$
\begin{aligned}
\Delta^{4} f(x)=0 \forall x & \\
\Rightarrow &(E-1)^{4} f(x)=0 \\
\Rightarrow &\left(E^{4}-4 E^{3}+6 E^{2}-4 E+1\right) f(x)=0 \\
\Rightarrow & E^{4} f(x)-4 E^{3} f(x)+6 E^{2} f(x) \\
-4 E f(x)+f(x)=0 \\
\Rightarrow & f(x+4)-4 f(x+3)+6 f(x+2) \\
-4 f(x+1)+f(x)=0
\end{aligned}
$$
On putting $x=0$, we get
$$
f(4)-4 f(3)+6 f(2)-4 f(1)+f(0)=0 \quad \ldots(\mathrm{i})
$$
On substituting the values of $f(0), f(1), f(2), f(4)$ in Eq. (i), we get
$$
\begin{array}{ll} 
& 81-4 f(3)+6 \times 9-4 \times 3+1=0 \\
\Rightarrow & 4 f(3)=124
\end{array}
$$
$\Rightarrow \quad f(3)=31$

</details>

---

