# JEE Main Mathematics - Continuity and Differentiability

## Topic 1: Continuity

**Total Questions:** 73

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x) = \begin{cases} \dfrac{1}{3}, & x \leq \pi/2 \\ \dfrac{b(1-\sin x)}{(\pi-2x)^2}, & x > \pi/2 \end{cases}$. If $f$ is continuous at $x=\pi/2$, then the value of $\displaystyle\int_{0}^{3b-6} |x^2+2x-3|\,dx$ is:

**Options:**

- **(A)** $5$
- **(B)** $2$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4$**

**Detailed Solution:**

Since $f(x)$ is continuous at $x = \pi/2$, the right-hand limit must equal the value of the function at $x = \pi/2$.

$\lim_{x \to \pi/2^+} f(x) = f(\pi/2)$

$\lim_{x \to \pi/2^+} \dfrac{b(1-\sin x)}{(\pi-2x)^2} = \dfrac{1}{3}$

Let $x = \pi/2 + h$. As $x \to \pi/2^+$, $h \to 0^+$.

$\lim_{h \to 0^+} \dfrac{b(1-\sin(\pi/2+h))}{(\pi-2(\pi/2+h))^2} = \dfrac{1}{3}$

$\lim_{h \to 0^+} \dfrac{b(1-\cos h)}{(-2h)^2} = \dfrac{1}{3}$

$\lim_{h \to 0^+} \dfrac{b(1-\cos h)}{4h^2} = \dfrac{1}{3}$

Using the standard limit $\lim_{h \to 0} \dfrac{1-\cos h}{h^2} = \dfrac{1}{2}$, we get:

$\dfrac{b}{4} \times \dfrac{1}{2} = \dfrac{1}{3} \Rightarrow \dfrac{b}{8} = \dfrac{1}{3} \Rightarrow b = \dfrac{8}{3}$

The upper limit of the integral is $3b - 6 = 3\left(\dfrac{8}{3}\right) - 6 = 2$.

The integral to evaluate is $I = \displaystyle\int_{0}^{2} |x^2+2x-3|\,dx$.

Factoring the quadratic expression gives $x^2+2x-3 = (x+3)(x-1)$.

For $x \in [0, 1]$, $(x+3)(x-1) \leq 0$, so $|x^2+2x-3| = 3 - 2x - x^2$.

For $x \in [1, 2]$, $(x+3)(x-1) \geq 0$, so $|x^2+2x-3| = x^2+2x-3$.

Splitting the integral at $x = 1$:

$I = \displaystyle\int_{0}^{1} (3 - 2x - x^2)\,dx + \displaystyle\int_{1}^{2} (x^2+2x-3)\,dx$

Evaluating the first integral:

$\displaystyle\int_{0}^{1} (3 - 2x - x^2)\,dx = \left[ 3x - x^2 - \dfrac{x^3}{3} \right]_0^1 = 3 - 1 - \dfrac{1}{3} = \dfrac{5}{3}$

Evaluating the second integral:

$\displaystyle\int_{1}^{2} (x^2+2x-3)\,dx = \left[ \dfrac{x^3}{3} + x^2 - 3x \right]_1^2$

$= \left( \dfrac{8}{3} + 4 - 6 \right) - \left( \dfrac{1}{3} + 1 - 3 \right) = \left( \dfrac{8}{3} - 2 \right) - \left( \dfrac{1}{3} - 2 \right) = \dfrac{7}{3}$

Adding the two parts:

$I = \dfrac{5}{3} + \dfrac{7}{3} = \dfrac{12}{3} = 4$

Answer: $4$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $f(x) = \begin{cases} x^3 + 8 ; & x < 0 \\ x^2 - 4 ; & x \geq 0 \end{cases}$ and $g(x) = \begin{cases} (x-8)^{1/3} ; & x < 0 \\ (x+4)^{1/2} ; & x \geq 0 \end{cases}$.
Then the number of points, where the function $g \circ f$ is discontinuous, is __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

The possible points of discontinuity for the composite function $g(f(x))$ are the points where $f(x)$ is discontinuous and the points where $f(x)$ is equal to a point of discontinuity of $g(x)$.

First, we find the points of discontinuity of $f(x)$ and $g(x)$.

For $f(x)$, the only possible point of discontinuity is at $x = 0$.
$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (x^3 + 8) = 8$
$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} (x^2 - 4) = -4$
Since $\lim_{x \to 0^-} f(x) \neq \lim_{x \to 0^+} f(x)$, $f(x)$ is discontinuous at $x = 0$.

For $g(x)$, the only possible point of discontinuity is at $x = 0$.
$\lim_{x \to 0^-} g(x) = \lim_{x \to 0^-} (x - 8)^{1/3} = -2$
$\lim_{x \to 0^+} g(x) = \lim_{x \to 0^+} (x + 4)^{1/2} = 2$
Since $\lim_{x \to 0^-} g(x) \neq \lim_{x \to 0^+} g(x)$, $g(x)$ is discontinuous at $x = 0$.

Next, we find the points where $f(x)$ equals the point of discontinuity of $g(x)$, which is $f(x) = 0$.
For $x < 0$, $x^3 + 8 = 0 \Rightarrow x = -2$.
For $x \geq 0$, $x^2 - 4 = 0 \Rightarrow x = 2$.

Thus, the possible points of discontinuity for $g(f(x))$ are $x = -2$, $x = 0$, and $x = 2$. We check the continuity at each of these points.

At $x = -2$:
As $x \to -2^-$, $f(x) \to 0^-$, so $\lim_{x \to -2^-} g(f(x)) = \lim_{y \to 0^-} g(y) = -2$
As $x \to -2^+$, $f(x) \to 0^+$, so $\lim_{x \to -2^+} g(f(x)) = \lim_{y \to 0^+} g(y) = 2$
Since the left-hand limit and right-hand limit are not equal, $g(f(x))$ is discontinuous at $x = -2$.

At $x = 0$:
$\lim_{x \to 0^-} g(f(x)) = g(8) = (8 + 4)^{1/2} = 2\sqrt{3}$
$\lim_{x \to 0^+} g(f(x)) = g(-4) = (-4 - 8)^{1/3} = (-12)^{1/3}$
Since the limits are not equal, $g(f(x))$ is discontinuous at $x = 0$.

At $x = 2$:
As $x \to 2^-$, $f(x) \to 0^-$, so $\lim_{x \to 2^-} g(f(x)) = \lim_{y \to 0^-} g(y) = -2$
As $x \to 2^+$, $f(x) \to 0^+$, so $\lim_{x \to 2^+} g(f(x)) = \lim_{y \to 0^+} g(y) = 2$
Since the limits are not equal, $g(f(x))$ is discontinuous at $x = 2$.

Therefore, there are $3$ points of discontinuity.

Answer: $3$

</details>

---

### Q3. JEE Main 2026 (04 April Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $f(x)=\begin{cases} e^{x-1}, & x<0 \\ x^2-5x+6, & x \geq 0 \end{cases}$ and $g(x)=f(|x|)+|f(x)|$. If the number of points where $g$ is not continuous and is not differentiable are $\alpha$ and $\beta$ respectively, then $\alpha+\beta$ is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

We are given the function:

$f(x) = \begin{cases} e^{x-1}, & x < 0 \\ x^2 - 5x + 6, & x \geq 0 \end{cases}$

We need to analyze the continuity and differentiability of $g(x) = f(|x|) + |f(x)|$.

For $x < 0$, $|x| = -x > 0$. Thus, $f(|x|) = (-x)^2 - 5(-x) + 6 = x^2 + 5x + 6$.
Also, for $x < 0$, $f(x) = e^{x-1} > 0$, so $|f(x)| = e^{x-1}$.
Therefore, for $x < 0$, $g(x) = x^2 + 5x + 6 + e^{x-1}$.

For $x \geq 0$, $|x| = x$. Thus, $f(|x|) = f(x) = x^2 - 5x + 6$.
Therefore, for $x \geq 0$, $g(x) = x^2 - 5x + 6 + |x^2 - 5x + 6|$.

Let us check the continuity of $g(x)$ at $x = 0$:
$\lim_{x \to 0^-} g(x) = \lim_{x \to 0^-} (x^2 + 5x + 6 + e^{x-1}) = 6 + \dfrac{1}{e}$
$\lim_{x \to 0^+} g(x) = \lim_{x \to 0^+} (x^2 - 5x + 6 + |x^2 - 5x + 6|) = 6 + 6 = 12$
$g(0) = 12$

Since $\lim_{x \to 0^-} g(x) \neq \lim_{x \to 0^+} g(x)$, $g(x)$ is discontinuous at $x = 0$. For all other $x$, $g(x)$ is a sum of continuous functions and is therefore continuous. 
Thus, the number of points of discontinuity is $\alpha = 1$.

Now, let us check the differentiability of $g(x)$.
Since $g(x)$ is discontinuous at $x = 0$, it is not differentiable at $x = 0$.

For $x < 0$, $g(x) = x^2 + 5x + 6 + e^{x-1}$, which is differentiable everywhere in its domain.

For $x > 0$, we can rewrite $g(x)$ by analyzing the sign of $x^2 - 5x + 6 = (x-2)(x-3)$:
$g(x) = \begin{cases} 2(x^2 - 5x + 6), & x \in (0, 2] \cup [3, \infty) \\ 0, & x \in (2, 3) \end{cases}$

Differentiating $g(x)$ for $x > 0, x \neq 2, 3$:
$g'(x) = \begin{cases} 4x - 10, & x \in (0, 2) \cup (3, \infty) \\ 0, & x \in (2, 3) \end{cases}$

Checking differentiability at $x = 2$:
$g'(2^-) = 4(2) - 10 = -2$
$g'(2^+) = 0$
Since $g'(2^-) \neq g'(2^+)$, $g(x)$ is not differentiable at $x = 2$.

Checking differentiability at $x = 3$:
$g'(3^-) = 0$
$g'(3^+) = 4(3) - 10 = 2$
Since $g'(3^-) \neq g'(3^+)$, $g(x)$ is not differentiable at $x = 3$.

Thus, $g(x)$ is not differentiable at exactly three points: $x = 0, 2, 3$.
So, the number of points of non-differentiability is $\beta = 3$.

Finally, $\alpha + \beta = 1 + 3 = 4$.

Answer: $4$

</details>

---

### Q4. JEE Main 2026 (02 April Shift 2)

*Type:* `numerical` | *Level:* `2`

The number of points in the interval $[2, 4]$, at which the function $f(x) = \left[x^2 - x - \dfrac{1}{2}\right]$, where $[\cdot]$ denotes the greatest integer function, is discontinuous, is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

Let $g(x) = x^2 - x - \dfrac{1}{2}$.

Differentiating with respect to $x$, we get $g'(x) = 2x - 1$.

For $x \in [2, 4]$, $g'(x) > 0$, which implies that $g(x)$ is strictly increasing in the interval $[2, 4]$.

The values of $g(x)$ at the endpoints are:

$g(2) = 2^2 - 2 - \dfrac{1}{2} = 1.5$

$g(4) = 4^2 - 4 - \dfrac{1}{2} = 11.5$

The function $f(x) = [g(x)]$ is discontinuous at all points where $g(x)$ is an integer, as $g(x)$ is strictly monotonic and crosses these integer values.

The integers between $1.5$ and $11.5$ are $2, 3, 4, 5, 6, 7, 8, 9, 10, 11$.

Since $g(x)$ is strictly increasing, it attains each of these $10$ integer values exactly once in the interval $(2, 4)$.

At the endpoints $x = 2$ and $x = 4$, $g(x)$ is not an integer, so $f(x)$ is continuous from the right at $x = 2$ and continuous from the left at $x = 4$.

Thus, the number of points of discontinuity in the interval $[2, 4]$ is $10$.

Answer: $10$

</details>

---

### Q5. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)=\lim _{\theta \rightarrow 0}\left(\frac{\cos \pi x-x^{\left(\frac{2}{\theta}\right)} \sin (x-1)}{1+x^{\left(\frac{2}{\theta}\right)}(x-1)}\right), x \in \mathbf{R}$. Consider the following two statements : 
 (I) $f(x)$ is discontinous at $x=1$. 
 (II) $f(x)$ is continous at $x=-1$. 
 Then,

**Options:**

- **(A)** Only (II) is True
- **(B)** Neither (I) nor (II) is True
- **(C)** Both (I) and (II) are True
- **(D)** Only (I) is True

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Neither (I) nor (II) is True**

**Detailed Solution:**

Taking the limit as $ \theta \to 0 $, we note $ x^{(2/\theta)} \to 0 $ for $ |x| < 1 $ and $ \to \infty $ for $ |x| > 1 $. This gives:

$ f(x) = \begin{cases} \cos \pi x & x \to 1^- \\ \dfrac{-\sin(x-1)}{(x-1)} & x \to 1^+ \end{cases} $

<b>Continuity at $ x = 1 $:</b>
$ \text{RHL} = \lim_{x \to 1^+} \frac{-\sin(x-1)}{(x-1)} = -1 $
$ \text{LHL} = \lim_{x \to 1^-} \cos \pi x = -1 $, $ f(1) = -1 $
$ \Rightarrow f(x) $ is continuous at $ x = 1 $. So Statement (I) is false.

<b>Continuity at $ x = -1 $:</b>
$ f(x) = \begin{cases} \dfrac{-\sin(x-1)}{-(x-1)} & x \to -1^- \\ \cos \pi x & x \to -1^+ \end{cases} $

$ \text{RHL} = \lim_{x \to -1^+} \cos \pi x = -1 $
$ \text{LHL} = \lim_{x \to -1^-} \frac{-\sin(x-1)}{-(x-1)} = \frac{\sin 2}{-2} $

Since LHL $ \neq $ RHL, $ f(x) $ is discontinuous at $ x = -1 $. So Statement (II) is also false.

Hence, neither (I) nor (II) is true.

</details>

---

### Q6. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $[t]$ denote the greatest integer less than or equal to $t$. If the function $f(x)=\left\{\begin{array}{cl}b^{2} \sin \left(\frac{\pi}{2}\left[\frac{\pi}{2}(\cos x+\sin x) \cos x\right]\right), & x<0 \\ \frac{\sin x-\frac{1}{2} \sin 2 x}{x^{3}} &, x>0 \\ a &, x=0\end{array}\right.$ is continuous at $x=0$, then $a^{2}+b^{2}$ is equal to

**Options:**

- **(A)** $\frac{5}{8}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{9}{16}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3}{4}$**

**Detailed Solution:**

For $x > 0$: $\sin x - \frac{1}{2}\sin 2x = \sin x(1 - \cos x)$.
$\lim_{x \to 0^+} \frac{\sin x(1-\cos x)}{x^3} = \lim_{x \to 0^+} \frac{\sin x}{x} \cdot \frac{1-\cos x}{x^2} = 1 \cdot \frac{1}{2} = \frac{1}{2}$.
So $a = \frac{1}{2}$.
For $x < 0$ near $0$: $\frac{\pi}{2}(\cos x + \sin x)\cos x \to \frac{\pi}{2}$ from below, so $\left[\frac{\pi}{2}(\cos x + \sin x)\cos x\right] = 1$.
$f(x) = b^2 \sin\left(\frac{\pi}{2} \cdot 1\right) = b^2$.
For continuity: $b^2 = a = \frac{1}{2}$.
$a^2 + b^2 = \frac{1}{4} + \frac{1}{2} = \frac{3}{4}$.

</details>

---

### Q7. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the function $f(x)=\frac{e^{x}\left(e^{\tan x-x}-1\right)+\log _{e}(\sec x+\tan x)-x}{\tan x-x}$ is continuous at $x=0$, then the value of $f(0)$ is equal to

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** 2
- **(C)** $\frac{3}{2}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{2}$**

**Detailed Solution:**

$f(0) = \lim_{x \to 0} \dfrac{e^{\tan x} - e^x + \ln(\sec x + \tan x) - x}{\tan x - x}$
Applying L'hospital rule
$\Rightarrow f(0) = \lim_{x \to 0} \dfrac{e^{\tan x} \cdot \sec^2 x - e^x + \sec x - 1}{\sec^2 x - 1}$
$\Rightarrow f(0) = \lim_{x \to 0} \dfrac{e^{\tan x}(\sec^2 x - 1) + (e^{\tan x} - e^x) + \sec x - 1}{\tan^2 x}$
$\Rightarrow f(0) = \lim_{x \to 0} \left( e^{\tan x} + \dfrac{e^x \left( e^{\tan x - x} - 1 \right)}{\tan^2 x} + \dfrac{1}{\sec x + 1} \right)$
$\Rightarrow f(0) = 1 + 0 + \dfrac{1}{2} = \dfrac{3}{2}$

</details>

---

### Q8. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\left\{\begin{array}{cc}\frac{a|x|+x^{2}-2(\sin |x|)(\cos |x|)}{x} &, x \neq 0 \\ b &, x=0\end{array}\right.$ 
 is continuous at $x=0$, then $a+b$ is equal to

**Options:**

- **(A)** 4
- **(B)** 1
- **(C)** 2
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

Note $2\sin|x|\cos|x| = \sin(2|x|)$.
For $x > 0$: $f(x) = a + x - \frac{\sin 2x}{x} \xrightarrow{x \to 0^+} a - 2$.
For $x < 0$: $f(x) = -a + x + \frac{\sin 2x}{x} \xrightarrow{x \to 0^-} -a + 2$.
For continuity: $a - 2 = 2 - a \Rightarrow a = 2$, and $b = a - 2 = 0$.
$a + b = 2$.

</details>

---

### Q9. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)= \begin{cases}\frac{\mathrm{a} x^{2}+2 \mathrm{a} x+3}{4 x^{2}+4 x-3} &, x \neq-\frac{3}{2}, \frac{1}{2} \\ \mathrm{~b} &, x=-\frac{3}{2}, \frac{1}{2}\end{cases}$ 
 be continuous at $x=-\frac{3}{2}$. If $f \circ f(x)=\frac{7}{5}$, then $x$ is equal to:

**Options:**

- **(A)** 4
- **(B)** 0
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

$4x^2+4x-3 = (2x+3)(2x-1)$. For continuity at $x = -3/2$, numerator must vanish there:
$a(9/4) - 3a + 3 = 0 \Rightarrow a = 4$.
$f(x) = \frac{(2x+1)(2x+3)}{(2x+3)(2x-1)} = \frac{2x+1}{2x-1}$ for $x \neq -3/2$.
$f \circ f(x) = f\!\left(\frac{2x+1}{2x-1}\right) = \frac{6x+1}{2x+3}$.
$\frac{6x+1}{2x+3} = \frac{7}{5} \Rightarrow 30x+5 = 14x+21 \Rightarrow x = 1$.

</details>

---

### Q10. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $[\cdot]$ denote the greatest integer function, and let $f(x)=\min \left\{\sqrt{2} x, x^{2}\right\}$. Let $\mathrm{S}=\left\{x \in(-2,2)\right.$ : the function $\mathrm{g}(x)=|x|\left[x^{2}\right]$ is discontinuous at $\left.x\right\}$. Then $\sum_{x \in S} f(x)$ equals

**Options:**

- **(A)** $\sqrt{6}-2 \sqrt{2}$
- **(B)** $1-\sqrt{2}$
- **(C)** $2-\sqrt{2}$
- **(D)** $2 \sqrt{6}-3 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1-\sqrt{2}$**

**Detailed Solution:**

$\mathrm{g}(\mathrm{x})=|\mathrm{x}|\left[\mathrm{x}^2\right]$
Points of discontinuity of $\mathrm{g}(\mathrm{x})$ in $(-2,2)$ are
$( \pm 1, \pm \sqrt{2}, \pm \sqrt{3})$
$\therefore S=\{-1,1,-\sqrt{2}, \sqrt{2},-\sqrt{3}, \sqrt{3}\}$
$\because f(x)=\min \left\{\sqrt{2} x, x^2\right\}$
$\therefore \sum_{x \in S} f(x)=-\sqrt{2}+1-2+2-\sqrt{6}+\sqrt{6}$
$=1-\sqrt{2}$

</details>

---

### Q11. JEE Main 2025 (7 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

The number of points of discontinuity of the function $f(\mathrm{x})=\left[\frac{\mathrm{x}^2}{2}\right]-[\sqrt{\mathrm{x}}], \mathrm{x} \in[0,4]$, where $[\cdot]$ denotes the greatest integer function is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

Check for $\left[\frac{x^2}{2}\right]$ and $[\sqrt{x}]$ becomes integers.
$\{0,1, \sqrt{2}, 2, \sqrt{6}, \sqrt{8}, \sqrt{10}, \sqrt{12}, \sqrt{14}, 4\}$
Continuous at $0^{+}$, continuous at $4^{-}$ $\left[\frac{x^2}{2}\right]=[\sqrt{x}]$, occurs at $x=\sqrt{2}$
$\Rightarrow$ Not continuous

</details>

---

### Q12. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(\mathrm{x})= \begin{cases}(1+\mathrm{ax})^{1 / \mathrm{x}} & , \quad \mathrm{x} \lt 0 \\ 1+\mathrm{b} & , \quad \mathrm{x}=0 \\ \frac{(\mathrm{x}+4)^{1 / 2}-2}{(\mathrm{x}+\mathrm{c})^{1 / 3}-2} & ,\end{cases}$
be continuous at $x=0$. Then $e^a b c$ is equal to

**Options:**

- **(A)** $64$
- **(B)** $72$
- **(C)** $48$
- **(D)** $36$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $48$**

**Detailed Solution:**

$\begin{aligned}
& f\left(0^{-}\right)=\mathrm{e}^{\lim _{x \rightarrow 0} \frac{\mathrm{ax}}{\mathrm{x}}}=\mathrm{e}^{\mathrm{a}} \\
& \mathrm{f}(0)=1+\mathrm{b} \\
& \mathrm{f}\left(0^{+}\right)=\frac{\frac{1}{2 \sqrt{\mathrm{x}+4}}}{\frac{1}{3}(\mathrm{x}+\mathrm{c})^{-\frac{2}{3}}}=\frac{\frac{1}{2(2)}}{\frac{1}{3} \cdot \mathrm{c}^{-\frac{2}{3}}} \\
& =\frac{3}{4} \mathrm{c}^{2 / 3}
\end{aligned}$
Also at $\mathrm{x}=0$;
$c^{1 / 3}=2 \Rightarrow c=8$
So $\mathrm{f}\left(0^{+}\right)=\frac{3}{4}(8)^{2 / 3}=3$
Now, $\mathrm{e}^{\mathrm{a}}=\mathrm{b}+1=3$
$\mathrm{e}^{\mathrm{a}} . \mathrm{b} \cdot \mathrm{c}=3 \cdot 2 \cdot 8=48$

</details>

---

### Q13. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function
$f(x)=\left\{\begin{array}{l}\frac{2}{x}\left\{\sin \left(k_1+1\right) x+\sin \left(k_2-1\right) x\right\}, \quad x \lt 0 \\ 4, \quad x=0 \\ \frac{2}{x} \log _e\left(\frac{2+k_1 x}{2+k_2 x}\right), \quad x\gt0\end{array}\right.$
is continuous at $\mathrm{x}=0$, then $\mathrm{k}_1^2+\mathrm{k}_2^2$ is equal to

**Options:**

- **(A)** $20$
- **(B)** $5$
- **(C)** $8$
- **(D)** $10$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $10$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0^{-}} \frac{2}{\mathrm{x}}\left\{\sin \left(\mathrm{k}_1+1\right) \mathrm{x}+\sin \left(\mathrm{k}_2-1\right) \mathrm{x}\right\}=4 \\ & \Rightarrow 2\left(\mathrm{k}_1+1\right)+2\left(\mathrm{k}_2-1\right)=4 \\ & \Rightarrow \mathrm{k}_1+\mathrm{k}_2=2 \\ & \Rightarrow \lim _{\mathrm{x} \rightarrow 0^{+}} \frac{2}{\mathrm{x}} \ln \left(\frac{2+\mathrm{k}_1 \mathrm{x}}{2+\mathrm{k}_2 \mathrm{x}}\right)=4 \\ & \Rightarrow \lim _{\mathrm{x} \rightarrow 0^{+}} \frac{1}{\mathrm{x}} \ln \left(1+\frac{\left(\mathrm{k}_1-\mathrm{k}_2\right) \mathrm{x}}{2+\mathrm{k}_2 \mathrm{x}}\right)=2 \\ & \Rightarrow \frac{\mathrm{k}_1-\mathrm{k}_2}{2}=2 \\ & \Rightarrow \mathrm{k}_1-\mathrm{k}_2=4 \\ & \therefore \mathrm{k}_1=3, \mathrm{k}_2=-1 \\ & \mathrm{k}_1^2+\mathrm{k}_2^2=9+1=10\end{aligned}$

</details>

---

### Q14. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $f:(0, \pi) \rightarrow \mathbf{R}$ be a function given by $f(x)=$
\(\left\{\begin{array}{cc}\left(\frac{8}{7}\right)^{\frac{\tan 8 x}{\tan 7 x}}, & 0 < x < \frac{\pi}{2} \\ \mathrm{a}-8, & x=\frac{\pi}{2} \\ (1+|\cot x|)^{\frac{\mathrm{b}}{}|\tan x|}, & \frac{\pi}{2} < x < \pi\end{array}\right.\)
where $\mathrm{a}, \mathrm{b} \in \mathbf{Z}$. If $f$ is continuous at $x=\frac{\pi}{2}$, then $\mathrm{a}^2+\mathrm{b}^2$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **81**

**Detailed Solution:**

LHL at $\mathrm{x}=\frac{\pi}{2}$
$\lim _{x \rightarrow \frac{\pi}{2}}\left(\frac{8}{7}\right)^{\frac{\tan 8 x}{\tan 7 x}}=\left(\frac{8}{7}\right)^0=1$
RHL at $\mathrm{x}=\frac{\pi}{2}$
$\begin{aligned}
& \lim _{x \rightarrow \frac{\pi}{2}}(1+|\cot x|)^{\frac{b}{\operatorname{lan}} \tan x} \\
& =e^{\lim _{x-\frac{\pi}{2}}|\cot x| \frac{b}{a}|\tan x|}=e^{\frac{b}{a}}
\end{aligned}$
$\begin{aligned} & \Rightarrow 1=a-8=e^{\frac{b}{a}} \\ & \Rightarrow a=9, b=0 \\ & \Rightarrow a^2+b^2=81\end{aligned}$

</details>

---

### Q15. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

For $\mathrm{a}, \mathrm{b}>0$, let $f(x)=\left\{\begin{array}{cc}\frac{\tan ((\mathrm{a}+1) x)+\mathrm{b} \tan x}{x}, & x < 0 \\ 3, & x=0 \\ \frac{\sqrt{\mathrm{a} x+\mathrm{b}^2 x^2}-\sqrt{\mathrm{a} x}}{\mathrm{~b} \sqrt{\mathrm{a}} x \sqrt{x}}, & x>0\end{array}\right.$
be a continous function at $x=0$. Then $\frac{\mathrm{b}}{\mathrm{a}}$ is equal to :

**Options:**

- **(A)** 6
- **(B)** 4
- **(C)** 5
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 6**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0} f(x)=f(0)=3 \\ & \lim _{x \rightarrow 0^{+}} \frac{\sqrt{a x+b^2 x^2}-\sqrt{a x}}{b \sqrt{a} x \sqrt{x}}=3 \\ & \lim _{x \rightarrow 0^{+}} \frac{a x+b^2 x^2-a x}{b \sqrt{a} x^{3 / 2}\left(\sqrt{a x+b^2 x^2}+\sqrt{a x}\right)} \\ & \lim _{x \rightarrow 0^{+}} \frac{b^2}{b \sqrt{a}\left(\sqrt{a+b^2 x}+\sqrt{a}\right)} \\ & \frac{b}{\sqrt{a} \cdot 2 \sqrt{a}} \Rightarrow \frac{b}{2 a}=3 \Rightarrow \frac{b}{a}=6\end{aligned}$

</details>

---

### Q16. JEE Main 2024 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $[\mathrm{t}]$ denote the greatest integer less than or equal to $\mathrm{t}$. Let $f:[0, \infty) \rightarrow \mathbf{R}$ be a function defined by $f(x)=\left[\frac{x}{2}+3\right]-[\sqrt{x}]$. Let $S$ be the set of all points in the interval $[0,8]$ at which $f$ is not continuous. Then $\sum_{\mathrm{a} \in \mathrm{S}} \mathrm{a}$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17**

**Detailed Solution:**

$\left[\frac{x}{2}+3\right]$ is discontinuous at $x=2,4,6,8$
$\sqrt{\mathrm{x}}$ is discontinuous at $\mathrm{x}=1,4$ $\mathrm{F}(\mathrm{x})$ is discontinuous at $\mathrm{x}=1,2,6,8$
$\sum \mathrm{a}=1+2+6+8=17$

</details>

---

### Q17. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f:[-1,2] \rightarrow \mathbf{R}$ be given by $f(x)=2 x^2+x+\left[x^2\right]-[x]$, where $[t]$ denotes the greatest integer less than or equal to $t$. The number of points, where $f$ is not continuous, is :

**Options:**

- **(A)** 5
- **(B)** 6
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

Doubtful points : $-1,0,1, \sqrt{2}, \sqrt{3}, 2$ at $x=\sqrt{2}, \sqrt{3}$
\(\begin{array}{cc} f(x)=\left(2 x^2+x-[x]\right)+\left[x^2\right]= \text{Discount} \\ \downarrow \qquad\qquad\quad \downarrow \\ \text{Cont.} \qquad\qquad \text{Cont.} \end{array}\)
at $x=-1$ :
$\left.\begin{array}{rl}\text { RHL } \Rightarrow & f(x)=(2-1-(-1))+0=2 \\ & f(-1)=2-1-(-1)+1=3\end{array}\right\}$ Dis.
at $x=2$ :
$\left.\begin{array}{rl}
\text {LHL } \Rightarrow f(x) & =8+2-1+3=12 \\
f(2) & =8+2-2+4=12
\end{array}\right\} \text { Cont. }$
at $\mathrm{x}=0$ :
$\left.\begin{array}{rl}
\text {LHL } \Rightarrow & 0+0-(-1)+0=1 \\
& \mathrm{f}(0)=0
\end{array}\right\} \text { Dis. }$
at $\mathrm{x}=1$
$\left.\begin{array}{rl}
\text {LHL } \Rightarrow & 2+1-0+0=3 \\
& f(1)=3-1+1=3 \\
\text {RHL } \Rightarrow & 2+1-1+1=3
\end{array}\right\} \text { Cont. }$

</details>

---

### Q18. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x)=\frac{\sin 3 x+\alpha \sin x-\beta \cos 3 x}{x^3}, x \in \mathbf{R}$, is continuous at $x=0$, then $f(0)$ is equal to :

**Options:**

- **(A)** 2
- **(B)** -2
- **(C)** 4
- **(D)** -4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -4**

**Detailed Solution:**

$f(x)=\frac{\sin 3 x+\alpha \sin x-\beta \cos 3 x}{x^3}$
is continuous at $\mathrm{x}=0$
$\lim _{x \rightarrow 0}=\frac{3 x-\frac{(3 x)^3}{\underline{|3}}+\ldots+\alpha\left(x-\frac{x^3}{\underline{|3}} \ldots\right)-\beta\left(1-\frac{(3 x)^2}{\lfloor 2} \ldots\right)}{x^3}=f(0)$
$\begin{aligned}
& \lim _{x \rightarrow 0}= \frac{-\beta+x(3+\alpha)+\frac{9 \beta x^2}{\underline{|2}}+\left(\frac{-27}{\underline{|3}}-\frac{\alpha}{\underline{|3}}\right) x^3 \ldots}{x^3}=f(0) \\
& \text { for exist } \\
& \beta=0,3+\alpha=0,-\frac{27}{\underline{|3}}-\frac{\alpha}{\underline{|3}}=f(0)
\end{aligned}$
$\begin{aligned} & \alpha=-3,-\frac{27}{6}-\frac{(-3)}{6}=f(0) \\ & f(0)=\frac{-27+3}{6}=-4\end{aligned}$

</details>

---

### Q19. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If the function
$f(x)= \begin{cases}\frac{72^x-9^x-8^x+1}{\sqrt{2}-\sqrt{1+\cos x}}, & x \neq 0 \\ a \log _e 2 \log _e 3 & , x=0\end{cases}$
is continuous at $x=0$, then the value of $a^2$ is equal to

**Options:**

- **(A)** 968
- **(B)** 1152
- **(C)** 746
- **(D)** 1250

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1152**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0} f(x)=a \ln 2 \ln 3 \\ & \lim _{n \rightarrow 0} \frac{72^x-9^x-8^x+1}{\sqrt{2}-\sqrt{1+\cos x}}=\lim _{x \rightarrow 0} \frac{\left(8^x-1\right)\left(9^x-1\right)}{\sqrt{2}-\sqrt{1+\cos x}} \\ & \lim _{n \rightarrow 0}\left(\frac{8^x-1}{x}\right)\left(\frac{9^x-1}{x}\right)\left(\frac{x^2}{1-\cos x}\right)(\sqrt{2}+\sqrt{1+\cos x}) \\ & \therefore \ln 8 \times \ln 9 \times 2 \times 2 \sqrt{2}=24 \sqrt{2} \ln 2 \ln 3 \\ & \therefore a=24 \sqrt{2}, a^2=576 \times 2=1152\end{aligned}$

</details>

---

### Q20. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $f: \mathbf{R} \rightarrow \mathbf{R}$ be a function given by
$f(x)=\left\{\begin{array}{ll}
\frac{1-\cos 2 x}{x^2}, & x < 0 \\
\alpha, & x=0, \\
\frac{\beta \sqrt{1-\cos x}}{x}, & x>0
\end{array}\right.$
where $\alpha, \beta \in \mathbf{R}$. If $f$ is continuous at $x=0$, then $\alpha^2+\beta^2$ is equal to :

**Options:**

- **(A)** 3
- **(B)** 12
- **(C)** 48
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 12**

**Detailed Solution:**

$\begin{aligned} & f\left(0^{-}\right)=\lim _{x \rightarrow 0^{-}} \frac{2 \sin ^2 x}{x^2}=2=\alpha \\ & f\left(0^{+}\right)=\lim _{x \rightarrow 0^{+}} \beta \times \sqrt{2} \frac{\sin \frac{x}{2}}{2 \frac{x}{2}}=\frac{\beta}{\sqrt{2}}=2 \\ & \Rightarrow \beta=2 \sqrt{2} \\ & \alpha^2+\beta^2=4+8=12\end{aligned}$

</details>

---

### Q21. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<span style="font-size:11.0pt"><span style='font-family:"Georgia",serif'>Consider the function </span></span><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mrow><mi mathvariant="normal">a</mi><mfenced><mrow><mn>7</mn><mi mathvariant="normal">x</mi><mo>-</mo><mn>12</mn><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mi mathvariant="normal">b</mi><mfenced close="|" open="|"><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>12</mn></mrow></mfenced></mrow></mfrac></mtd><mtd><mo>,</mo><mi mathvariant="normal">x</mi><mo>&lt;</mo><mn>3</mn></mtd></mtr><mtr><mtd><msup><mn>2</mn><mfrac><mrow><mi>sin</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mo>[</mo><mi mathvariant="normal">x</mi><mo>]</mo></mrow></mfrac></msup></mtd><mtd><mo>,</mo><mi mathvariant="normal">x</mi><mo>&gt;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mi mathvariant="normal">b</mi></mtd><mtd><mo>,</mo><mi mathvariant="normal">x</mi><mo>=</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math>,where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">x</mi><mo>]</mo></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi></math> denotes the set of all ordered pairs <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>,</mo><mo> </mo><mi mathvariant="normal">b</mi><mo>)</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo> </mo></math>is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mn>3</mn></math>, then the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** Infinitely many
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mrow><mi mathvariant="normal">a</mi><mfenced><mrow><mn>7</mn><mi mathvariant="normal">x</mi><mo>-</mo><mn>12</mn><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mi mathvariant="normal">b</mi><mfenced close="|" open="|"><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>12</mn></mrow></mfenced></mrow></mfrac></mtd><mtd><mo>,</mo><mi mathvariant="normal">x</mi><mo>&lt;</mo><mn>3</mn></mtd></mtr><mtr><mtd><msup><mn>2</mn><mfrac><mrow><mi>sin</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mo>[</mo><mi mathvariant="normal">x</mi><mo>]</mo></mrow></mfrac></msup></mtd><mtd><mo>,</mo><mi mathvariant="normal">x</mi><mo>&gt;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mi mathvariant="normal">b</mi></mtd><mtd><mo>,</mo><mi mathvariant="normal">x</mi><mo>=</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">f</mi><mfenced><msup><mn>3</mn><mo>-</mo></msup></mfenced><mo>=</mo><mpadded><mfrac><mrow><mi mathvariant="normal">a</mi><mfenced><mrow><mn>7</mn><mi mathvariant="normal">x</mi><mo>-</mo><mn>12</mn><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mi mathvariant="normal">b</mi><mo>|</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>12</mn><mo>|</mo></mrow></mfrac></mpadded></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">f</mi><mfenced><msup><mn>3</mn><mo>-</mo></msup></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mi mathvariant="normal">a</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>(</mo><mi mathvariant="normal">x</mi><mo>-</mo><mn>4</mn><mo>)</mo></mrow><mrow><mi mathvariant="normal">b</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>(</mo><mi mathvariant="normal">x</mi><mo>-</mo><mn>4</mn><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">f</mi><mfenced><msup><mn>3</mn><mo>-</mo></msup></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mi mathvariant="normal">a</mi></mrow><mi mathvariant="normal">b</mi></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><msup><mn>3</mn><mo>+</mo></msup></mfenced><mo>=</mo><msup><mn>2</mn><mrow><munder><mi>lim</mi><mrow><mi mathvariant="normal">x</mi><mo>→</mo><msup><mn>3</mn><mo>+</mo></msup></mrow></munder><mfenced><mfrac><mrow><mi>sin</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mn>3</mn></mrow></mfrac></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">f</mi><mfenced><msup><mn>3</mn><mo>+</mo></msup></mfenced><mo>=</mo><mn>2</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo> </mo><mo>=</mo><mo> </mo><mi mathvariant="normal">b</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>iii</mi></mfenced></math></p><p>It is given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mn>3</mn></math>.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mi mathvariant="normal">f</mi><mo>(</mo><msup><mn>3</mn><mo>+</mo></msup><mo>)</mo><mo>=</mo><mi mathvariant="normal">f</mi><mo>(</mo><msup><mn>3</mn><mo>-</mo></msup><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">b</mi><mo>=</mo><mn>2</mn><mo>=</mo><mfrac><mrow><mo>-</mo><mi mathvariant="normal">a</mi></mrow><mi mathvariant="normal">b</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">b</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">a</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p>Hence, there is only <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi></math>, which is ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>4</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>.</p>

</details>

---

### Q22. JEE Main 2023 (12 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> be the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi></math>. Then the number of points in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>&#8211;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo></math> where the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mfenced close="]" open="["><mi>x</mi></mfenced></mfenced><mo>+</mo><msqrt><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></msqrt></math> is discontinuous, is _____.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mfenced close="]" open="["><mi>x</mi></mfenced></mfenced><mo>+</mo><msqrt><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>&#8805;</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>Now using the property of greatest integer function and simplifying the function we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mn>2</mn><mo>+</mo><msqrt><mi>x</mi><mo>+</mo><mn>2</mn></msqrt><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>+</mo><msqrt><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msqrt><mi>x</mi></msqrt><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn><mo>&#160;</mo></mtd></mtr></mtable></mfenced></math></p><p>Now plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b6c78f72-2e3a-4af6-9cb4-16130816aa9e.png" style="width: 300px; height: 223px;" /></p><p>Now from the diagram we can say that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is discontinuous at two points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mo>&#8211;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math>.</p>

</details>

---

### Q23. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced open="|" close="|"><mrow><mo>-</mo><mi>x</mi><mo>+</mo><mfenced open="[" close="]"><mi>x</mi></mfenced></mrow></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>t</mi></mfenced></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is

**Options:**

- **(A)** continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, but not continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>
- **(B)** continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>, but not continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>
- **(C)** continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>
- **(D)** not continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>, but not continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mi>x</mi><mo>+</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mo>&#160;</mo><mtext>as</mtext><mo>&#160;</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mi>A</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mfenced close="}" open="{"><mi>x</mi></mfenced></mfenced><mo>,</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mfenced close="}" open="{"><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></mrow></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced close="}" open="{"><mi>x</mi></mfenced><mo>&#160;&#160;</mo><mo>(</mo><mo>&#8757;</mo><mfenced close="}" open="{"><mi>x</mi></mfenced><mo>&#8805;</mo><mn>0</mn><mo>)</mo></math></p><p>Now at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn><mo>&#160;</mo><mtext>for</mtext><mo>&#160;</mo><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></mfenced></math></p><p>So, function is discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p>Now at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>1</mn><mo>+</mo></msup></mfenced><mo>=</mo><mn>0</mn><mo>+</mo><mn>0</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>1</mn><mo>-</mo></msup></mfenced><mo>=</mo><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Hence, the function is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>.</p></blockquote>

</details>

---

### Q24. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mfenced><mrow><mn>1</mn><mo>+</mo><mo>|</mo><mi>cos</mi><mo>&#160;</mo><mi>x</mi><mo>|</mo></mrow></mfenced><mfrac><mi>&#955;</mi><mrow><mo>|</mo><mi>cos</mi><mo>&#160;</mo><mi>x</mi><mo>|</mo></mrow></mfrac><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mi>&#956;</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><msup><mi>e</mi><mfrac><mrow><mi>cot</mi><mo>&#160;</mo><mn>6</mn><mi>x</mi></mrow><mrow><mi>cot</mi><mo>&#160;</mo><mn>4</mn><mi>x</mi></mrow></mfrac></msup><mo>,</mo></mtd><mtd><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mi>&#960;</mi></mtd></mtr></mtable></mfenced></math>is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#955;</mi><mo>+</mo><mn>6</mn><mo>&#160;</mo><msub><mi>log</mi><mi>c</mi></msub><mi>&#956;</mi><mo>+</mo><msup><mi>&#956;</mi><mn>6</mn></msup><mo>-</mo><msup><mi>e</mi><mrow><mn>6</mn><mi>&#955;</mi></mrow></msup></math> is equal to</p><p> </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>e</mi><mn>4</mn></msup><mo>+</mo><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p><p>Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">L</mi><mo>.</mo></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><msup><mi>&#960;</mi><mo>+</mo></msup><mn>2</mn></mfrac></mrow></munder><msup><mi>e</mi><mfrac><mrow><mi>cot</mi><mo>&#160;</mo><mn>6</mn><mi>x</mi></mrow><mrow><mi>cot</mi><mo>&#160;</mo><mn>4</mn><mi>x</mi></mrow></mfrac></msup><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><msup><mi>&#960;</mi><mo>+</mo></msup><mn>2</mn></mfrac></mrow></munder><msup><mi>e</mi><mfrac><mrow><mi>sin</mi><mo>&#160;</mo><mn>4</mn><mi>x</mi><mo>&#183;</mo><mi>cos</mi><mo>&#160;</mo><mn>6</mn><mi>x</mi></mrow><mrow><mi>sin</mi><mo>&#160;</mo><mn>6</mn><mi>x</mi><mo>&#183;</mo><mi>cos</mi><mo>&#160;</mo><mn>4</mn><mi>x</mi></mrow></mfrac></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mo>/</mo><mn>3</mn></mrow></msup></math></p><p>Similarly, on simplification for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">L</mi><mo>.</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo></msup></mrow></munder><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mo>|</mo><mi>cos</mi><mi>x</mi><mo>|</mo></mrow></mfenced><mfrac><mi>&#955;</mi><mrow><mo>|</mo><mi>cos</mi><mi>x</mi><mo>|</mo></mrow></mfrac></msup><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo></msup></mrow></munder><mi>&#955;</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mi>&#955;</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mi>&#956;</mi></math></p><p>For continuous function, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">e</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mo>=</mo><msup><mi mathvariant="normal">e</mi><mi>&#955;</mi></msup><mo>=</mo><mi>&#956;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#956;</mi><mo>=</mo><msup><mi mathvariant="normal">e</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#955;</mi><mo>+</mo><mn>6</mn><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mi>&#956;</mi><mo>+</mo><msup><mi>&#956;</mi><mn>6</mn></msup><mo>-</mo><msup><mi mathvariant="normal">e</mi><mrow><mn>6</mn><mi>&#955;</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>(</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>)</mo><mo>+</mo><mn>6</mn><mo>(</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>)</mo><mo>+</mo><msup><mfenced><msup><mi>e</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></mfenced><mn>6</mn></msup><mo>-</mo><msup><mi>e</mi><mrow><mn>6</mn><mo>(</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>)</mo></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>+</mo><mn>4</mn><mo>+</mo><msup><mi>e</mi><mn>4</mn></msup><mo>-</mo><msup><mi>e</mi><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn></math></p>

</details>

---

### Q25. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mn>5</mn><mi>x</mi></mrow></mfenced><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>&#945;</mi><mi>x</mi></mrow></mfenced></mrow><mi>x</mi></mfrac></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>10</mn></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> be continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mn>5</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>&#945;</mi><mi>x</mi></mrow></mfenced></mrow><mi>x</mi></mfrac></mtd><mtd><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>10</mn></mtd><mtd><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> to be continuous</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mn>5</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>&#945;</mi><mi>x</mi></mrow></mfenced></mrow><mi>x</mi></mfrac><mo>=</mo><mn>10</mn></math></p><p>Using expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>5</mn><mi>x</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mrow><mn>25</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mstyle><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>&#945;</mi><mi>x</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mstyle><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo></mrow></mfenced></mrow><mi>x</mi></mfrac><mo>=</mo><mn>10</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>-</mo><mi>&#945;</mi><mo>=</mo><mn>10</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q26. JEE Main 2022 (28 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><mi>cos</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mo>-</mo><msup><mi>x</mi><mrow><mn>2</mn><mi>n</mi></mrow></msup><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>-</mo><msup><mi>x</mi><mrow><mn>2</mn><mi>n</mi></mrow></msup></mrow></mfrac></math> is continuous for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mn>1</mn></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi><mo>-</mo><msup><mi>x</mi><mrow><mn>2</mn><mi>n</mi></mrow></msup><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>-</mo><msup><mi>x</mi><mrow><mn>2</mn><mi>n</mi></mrow></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi><mo>-</mo><msup><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mi>n</mi></msup><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi><msup><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mi>n</mi></msup><mo>-</mo><msup><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mi>n</mi></msup></mrow></mfrac></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn><mo>,</mo></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mn>1</mn><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mi>x</mi><mrow><mn>2</mn><mi>n</mi></mrow></msup><mo>&#8594;</mo><mn>0</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></math></p><p>Now again rewriting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfrac><mrow><msup><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mrow><mo>-</mo><mi>n</mi></mrow></msup><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mrow><mo>-</mo><mi>n</mi></mrow></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>1</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>1</mn><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn><mi>n</mi></mrow></msup><mo>&#8594;</mo><mn>0</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>1</mn></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn></mrow></mfenced><mrow><mo>&#8722;</mo><mn>1</mn></mrow></mfrac></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mo>&#8722;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><msup><mn>1</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mrow><mi>sin</mi><mn>2</mn></mrow><mn>2</mn></mfrac></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p></blockquote>

</details>

---

### Q27. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>&#8800;</mo><mi>q</mi><mo>&#8800;</mo><mn>0</mn></math>, then function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mroot><mrow><mi>p</mi><mfenced><mrow><mn>729</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mn>7</mn></mroot><mo>-</mo><mn>3</mn></mrow><mrow><mroot><mrow><mn>729</mn><mo>+</mo><mi>q</mi><mi>x</mi></mrow><mn>3</mn></mroot><mo>-</mo><mn>9</mn></mrow></mfrac></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mi>p</mi><mi>q</mi><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn><mi>q</mi><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><msup><mi>p</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn><mi>q</mi><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><msup><mi>p</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mi>p</mi><mi>q</mi><mo>&#160;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><mn>9</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn><mi>q</mi><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><msup><mi>p</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>For a function to be continuous <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, we know </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mroot><mrow><mi>p</mi><mfenced><mrow><mn>729</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mn>7</mn></mroot><mo>-</mo><mn>3</mn></mrow><mrow><mroot><mrow><mn>729</mn><mo>+</mo><mi>q</mi><mi>x</mi></mrow><mn>3</mn></mroot><mo>-</mo><mn>9</mn></mrow></mfrac></math> </p><p>limit should be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>0</mn><mn>0</mn></mfrac></math> from</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mrow><mroot><mrow><mi>p</mi><mfenced><mrow><mn>729</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mn>7</mn></mroot><mo>-</mo><mn>3</mn></mrow></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mroot><mrow><mi>p</mi><mo>.</mo><mn>729</mn></mrow><mn>7</mn></mroot><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>&#183;</mo><mn>729</mn><mo>=</mo><msup><mn>3</mn><mn>7</mn></msup><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mi>p</mi><mo>=</mo><mn>3</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mroot><mrow><mn>3</mn><mfenced><mrow><msup><mn>3</mn><mn>6</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mn>7</mn></mroot><mo>-</mo><mn>3</mn></mrow><mrow><mroot><mrow><msup><mn>3</mn><mn>6</mn></msup><mo>+</mo><mi>q</mi><mi>x</mi></mrow><mn>3</mn></mroot><mo>-</mo><mn>9</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>3</mn><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><msup><mn>3</mn><mn>6</mn></msup></mfrac></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>7</mn></mfrac></mstyle></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>9</mn><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>q</mi><mi>x</mi></mrow><msup><mn>3</mn><mn>6</mn></msup></mfrac></mrow></mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>9</mn></mfrac><mo>&#215;</mo><mfrac><mfrac><mn>1</mn><mrow><mn>7</mn><mo>&#183;</mo><msup><mn>3</mn><mn>6</mn></msup></mrow></mfrac><mfrac><mi mathvariant="normal">q</mi><mrow><mn>3</mn><mo>&#183;</mo><msup><mn>3</mn><mn>6</mn></msup></mrow></mfrac></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mrow><mn>7</mn><mi>q</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>7</mn><mi>q</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mi>q</mi><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mo>&#183;</mo><msup><mi>p</mi><mn>2</mn></msup><mo>&#183;</mo><mi>q</mi><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><msup><mi>p</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math>  (multiplying the equation by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mn>2</mn></msup></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>63</mn><mi>q</mi><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><msup><mi>p</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p></blockquote>

</details>

---

### Q28. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnspacing="1.4ex" columnalign="left"><mtr><mtd><mi>x</mi><mo>+</mo><mi>a</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnspacing="1.4ex" columnalign="left"><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mi>b</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> are continuous on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>g</mi><mi>o</mi><mi>f</mi></mrow></mfenced><mfenced><mn>2</mn></mfenced><mo>+</mo><mfenced><mrow><mi>f</mi><mi>o</mi><mi>g</mi></mrow></mfenced><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>8</mn></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><mi>x</mi><mo>+</mo><mi>a</mi><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mi>b</mi><mo>;</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></math> are continuous on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></p><p>So, for continuity</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>0</mn><mo>-</mo></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mn>0</mn><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>4</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><msup><mn>0</mn><mo>-</mo></msup></mfenced><mo>=</mo><mi>g</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>g</mi><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>=</mo><msup><mfenced><mrow><mn>0</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>1</mn><mo>-</mo><mn>16</mn><mo>=</mo><mo>-</mo><mn>15</mn></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mn>2</mn></mfenced></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>g</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>2</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>15</mn><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>-</mo><mn>15</mn><mo>+</mo><mn>3</mn><mo>=</mo><mo>-</mo><mn>8</mn></math></p></blockquote>

</details>

---

### Q29. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnspacing="1.4ex" columnalign="left"><mtr><mtd><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mi>s</mi><mi>e</mi><mi>c</mi><mo>&#160;</mo><mi>x</mi><mo>-</mo><mi>cos</mi><mo>&#160;</mo><mi>x</mi></mrow></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></mtd></mtr><mtr><mtd><mi>k</mi></mtd><mtd><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mi>s</mi><mi>e</mi><mi>c</mi><mo>&#160;</mo><mi>x</mi><mo>-</mo><mi>cos</mi><mo>&#160;</mo><mi>x</mi></mrow></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mn>0</mn></mfenced></mtd></mtr><mtr><mtd><mi>k</mi></mtd><mtd><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced></mrow></mfenced><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>=</mo><mi>k</mi></math></p><p>Taking L.H.S<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced></mrow></mfenced><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mfrac><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfrac></mfenced><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>cos</mi><mi>x</mi></mrow><mrow><mfenced><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mfrac><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfrac></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>cos</mi><mi>x</mi></mrow><mfenced><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mn>1</mn></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mn>0</mn></mrow></mfenced><mn>1</mn></mrow><mfenced><mn>1</mn></mfenced></mfrac><mo>=</mo><mn>1</mn></math></p><p>Now equating with R.H.S we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>1</mn></math></p></blockquote>

</details>

---

### Q30. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>,</mo><mi>g</mi><mo>:</mo><mi mathvariant="bold-italic">R</mi><mo>&#8594;</mo><mi mathvariant="bold-italic">R</mi></math> be functions defined by
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfenced close="]" open="["><mi>x</mi></mfenced></mtd><mtd><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced close="|" open="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mtd><mtd><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> and
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>
where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denote the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. Then, the function fog is discontinuous at exactly

**Options:**

- **(A)** one point
- **(B)** two points
- **(C)** three points
- **(D)** four points

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) two points**

**Detailed Solution:**

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>,</mo><mi>g</mi><mo>:</mo><mi mathvariant="bold-italic">R</mi><mo>&#8594;</mo><mi mathvariant="bold-italic">R</mi></math> be functions defined by
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfenced close="]" open="["><mi>x</mi></mfenced></mtd><mtd><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced close="|" open="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mtd><mtd><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> and
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mfenced open="[" close="]"><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced open="|" close="|"><mrow><mn>1</mn><mo>-</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>After taking intersection we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mfenced open="|" close="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced open="[" close="]"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfenced><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mfenced open="|" close="|"><mrow><mn>2</mn><mo>-</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math> </p><p>Now, checking continuity at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> and at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p>Hence, discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><msup><mn>2</mn><mo>+</mo></msup></mfenced><mo>=</mo><mn>1</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><msup><mn>2</mn><mo>-</mo></msup></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Hence, discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q31. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="[" close=""><mtable columnalign="left"><mtr><mtd><mfenced open="[" close="]"><msup><mi>e</mi><mi>x</mi></msup></mfenced><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>a</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mfenced open="[" close="]"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>b</mi><mo>+</mo><mfenced open="[" close="]"><mrow><mi>sin</mi><mfenced><mrow><mi>&#960;</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>,</mo></mtd><mtd><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mfenced open="[" close="]"><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mfenced><mo>-</mo><mi>c</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math>
where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>&#8712;</mo><mi>&#8477;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> denotes greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>. Then, which of the following statements is true?

**Options:**

- **(A)** There exists <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8477;</mi></math>.
- **(B)** If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is discontinuous at exactly one point, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>1</mn></math>
- **(C)** If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is discontinuous at exactly one point, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>&#8800;</mo><mn>1</mn></math>.
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is discontinuous at atleast two points, for any values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is discontinuous at exactly one point, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>&#8800;</mo><mn>1</mn></math>.**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="["><mtable columnalign="left"><mtr><mtd><mfenced close="]" open="["><msup><mi>e</mi><mi>x</mi></msup></mfenced><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>a</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>b</mi><mo>+</mo><mfenced close="]" open="["><mrow><mi>sin</mi><mfenced><mrow><mi>&#960;</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>,</mo></mtd><mtd><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mfenced close="]" open="["><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mfenced><mo>-</mo><mi>c</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>a</mi><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>b</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>b</mi><mo>-</mo><mn>1</mn><mo>,</mo></mtd><mtd><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>c</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>Here, we know <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>&#8800;</mo><mi>b</mi><mo>-</mo><mn>1</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> to be continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mn>1</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> to be continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>;</mo><mo>&#160;</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q32. JEE Main 2022 (25 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> is the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>t</mi></math>. Then, in the open interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>, the number of points where fog is discontinuous is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **62**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mn>2</mn><msup><mi>g</mi><mn>2</mn></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfenced close="]" open="["><mrow><mn>2</mn><msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mn>1</mn><mo>;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfenced close="]" open="["><mrow><mn>2</mn><msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mn>1</mn><mo>;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mn>0</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>5</mn><mo>&#60;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>&#60;</mo><mo>-</mo><mn>3</mn><mo>&#8658;</mo><mo>&#8658;</mo><mn>9</mn><mo>&#60;</mo><msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>&#60;</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>18</mn><mo>&#60;</mo><mn>2</mn><msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>&#60;</mo><mn>50</mn></math>, So there will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math> values where <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup></math> is integer, Similarly for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup></math> there will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math>, so total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>62</mn></math> points of discontinuity</p><p> </p>

</details>

---

### Q33. JEE Main 2022 (24 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

The number of points where the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#10877;</mo><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mfenced close="]" open="["><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#10878;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#10877;</mo><mi>t</mi></math>, is discontinuous is ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<p>Here both the modulus function is continuous in its domain.</p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></munder><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><msup><mn>1</mn><mo>+</mo></msup></mrow></munder><mfenced close="]" open="["><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></munder><mfenced close="]" open="["><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>+</mo></msup></mrow></munder><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is discontinuous when <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>/</mo><mo>&#160;</mo><mn>1</mn><mo>/</mo><mo>&#160;</mo><mn>2</mn></math></p><p>i.e when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mo>&#177;</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>,</mo><mo>&#177;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#177;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/de9e46e8-f87d-44d9-b10e-cc06196ceee8-image.png" style="width: 450px; height: 221px;" /></p><p> </p>

</details>

---

### Q34. JEE Main 2021 (01 Sep Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">t</mi><mo>]</mo></math> denote the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi mathvariant="normal">t</mi><mo>.</mo></math> The number of points where the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mo>[</mo><mi>x</mi><mo>]</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>sin</mi><mfenced><mfrac><mi>&#960;</mi><mrow><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced><mo>-</mo><mo>[</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>]</mo><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>)</mo></math> is not continuous is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>.</mo><mo>]</mo></math> is discontinuous at integers so we will check at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></math> only </p><p>at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><msup><mn>1</mn><mo>-</mo></msup><mo>]</mo><mo>=</mo><mo>-</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><msup><mn>1</mn><mo>+</mo></msup><mo>]</mo><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>we have </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHL</mi><mo>=</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>&#183;</mo><mo>(</mo><mn>0</mn><mo>)</mo><mo>+</mo><mi>sin</mi><mfenced><mi mathvariant="normal">&#960;</mi></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>RHL</mi><mo>=</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>&#183;</mo><mo>(</mo><mn>0</mn><mo>)</mo><mo>+</mo><mi>sin</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>0</mn><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn><mo>&#8658;</mo></math> Continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Again at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><msup><mn>0</mn><mo>-</mo></msup><mo>]</mo><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>[</mo><msup><mn>0</mn><mo>+</mo></msup><mo>]</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHL</mi><mo>=</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>&#183;</mo><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>sin</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>0</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>RHL</mi><mo>=</mo><mn>0</mn><mo>+</mo><mi>sin</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>-</mo><mn>1</mn><mo>&#8800;</mo><mi>LHL</mi></math></p><p>Hence, discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn></math></p><p>Again at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><msup><mn>1</mn><mo>-</mo></msup><mo>]</mo><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>[</mo><msup><mn>1</mn><mo>+</mo></msup><mo>]</mo><mo>=</mo><mn>1</mn></math></p><p>We have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHL</mi><mo>=</mo><mn>0</mn><mo>+</mo><mi>sin</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>RHL</mi><mo>=</mo><mn>0</mn><mo>+</mo><mi>sin</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>-</mo><mn>2</mn><mo>&#8800;</mo><mi>LHL</mi></math> </p><p>Hence, discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>Hence, discontinuous at exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> points</p>

</details>

---

### Q35. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mfrac><mn>1</mn><mi>x</mi></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mi>a</mi></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mi>x</mi><mrow><mo>&#160;</mo><mi>b</mi></mrow></mfrac></mrow></mfrac></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>k</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mrow><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mo>&#160;</mo><mi>b</mi></mrow></mfrac><mo>+</mo><mfrac><mn>4</mn><mi>k</mi></mfrac></math> is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math>**

**Detailed Solution:**

<p>Given that </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfrac><mn>1</mn><mi>x</mi></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mi>a</mi></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mi>x</mi><mrow><mo>&#160;</mo><mi>b</mi></mrow></mfrac></mrow></mfrac></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>k</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mrow><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">L</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">L</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><mi>log</mi><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mi>a</mi></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mi>x</mi><mi>b</mi></mfrac></mrow></mfrac></mfenced></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mi>a</mi></mfrac></mrow></mfenced><mo>-</mo><mi>log</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>x</mi><mi>b</mi></mfrac></mrow></mfenced></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mi>a</mi></mfrac></mrow></mfenced></mrow><mfrac><mi>x</mi><mi>a</mi></mfrac></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>-</mo><mfrac><mrow><mi>log</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>x</mi><mi>b</mi></mfrac></mrow></mfenced></mrow><mrow><mo>-</mo><mfrac><mi>x</mi><mi>b</mi></mfrac></mrow></mfrac><mo>&#215;</mo><mo>-</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>a</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>RHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mfenced><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;&#160;</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>=</mo><mi>k</mi><mo>=</mo><mo>-</mo><mn>4</mn><mo>&#160;</mo><mo>.</mo></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>-</mo><mn>4</mn><mo>&#160;</mo><mo>&#8658;</mo><mfrac><mn>4</mn><mi>k</mi></mfrac><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>-</mo><mn>4</mn><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mfrac><mn>4</mn><mi>k</mi></mfrac><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>-</mo><mn>5</mn><mo>.</mo></math></p>

</details>

---

### Q36. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>t</mi><mo>]</mo></math> denote the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>.</mo></math>
Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>x</mi><mo>-</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>,</mo><mo>&#160;</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>min</mi><mo>{</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>,</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>}</mo><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>]</mo><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math> is :

**Options:**

- **(A)** continuous in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>]</mo></math> but not differentiable at more than four points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>
- **(B)** Continous in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>]</mo></math> but not differentiable at exactly three poionts in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>
- **(C)** not continuous at exactly four points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>]</mo></math>
- **(D)** not continuous at exactly three points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>]</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) continuous in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>]</mo></math> but not differentiable at more than four points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>x</mi><mo>-</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>=</mo><mo>{</mo><mi>x</mi><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>=</mo><mn>1</mn><mo>-</mo><mo>{</mo><mi>x</mi><mo>}</mo></math></p><p>Now, Graph of min <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>,</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>}</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/097a4854-839b-4efd-bb7a-a0bcbb3b4455-image.png" style="width: 326px; height: 250px;" /></p><p>Clearly graph is continuous in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>]</mo></math> but non differentiable at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> points (i.e. greater than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>) in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>)</mo></math></p>

</details>

---

### Q37. JEE Main 2021 (26 Aug Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mi>b</mi><mo>&#8800;</mo><mn>0</mn></math>. Defined a function, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mtable columnalign="left left" columnspacing="1em" rowspacing=".2em"><mtr><mtd><mrow><mi>a</mi><mi>sin</mi><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>(</mo><mi>x</mi><mo>&#8722;</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>&#8197;&#8197;&#8197;&#8197;</mo></mrow><mo>&#160;</mo><mi>for</mi><mo>&#160;</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mrow><mi>tan</mi><mn>2</mn><mi>x</mi><mo>&#8722;</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac><mo>,</mo><mo>&#8197;&#8197;&#8197;&#8197;</mo><mo>&#160;</mo><mi>for</mi><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous at<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>-</mo><mi>a</mi><mi>b</mi></math> is equal to</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mtable columnalign="left left" columnspacing="1em" rowspacing=".2em"><mtr><mtd><mrow><mi>a</mi><mi>sin</mi><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#8197;&#8197;&#8197;&#8197;</mo></mrow><mi>for</mi><mo>&#160;</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mrow><mi>tan</mi><mn>2</mn><mi>x</mi><mo>&#8722;</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac><mo>,</mo><mo>&#8197;&#8197;&#8197;&#8197;</mo><mi>for</mi><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>If function is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHL</mi><mo>=</mo><mi>RHL</mi><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfenced close="]" open="["><mrow><mi>a</mi><mi>sin</mi><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>LHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mi>a</mi><mi>sin</mi><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mfenced><mrow><mn>0</mn><mo>-</mo><mi>h</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>LHL</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mi>a</mi><mi>sin</mi><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mfenced><mrow><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>LHL</mi><mo>=</mo><mo>-</mo><mi>a</mi></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>RHL</mi><mo>=</mo><munder accentunder="false"><mo>lim</mo><mrow><mi>x</mi><mo stretchy="false">&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>&#8202;</mo><mfenced><mfrac><mrow><mi>tan</mi><mn>2</mn><mi>x</mi><mo>&#8722;</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mi>x</mi><mo>&#8722;</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>5</mn></msup><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>tan</mi><mi>x</mi><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>5</mn></msup></mrow><mn>15</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>RHL</mi><mo>=</mo><munder accentunder="false"><mo>lim</mo><mrow><mi>x</mi><mo stretchy="false">&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>&#8202;</mo><mfenced close="]" open="["><mfrac><mrow><mfrac><mrow><mo>(</mo><mn>2</mn><mi>x</mi><msup><mo>)</mo><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mo>(</mo><mn>2</mn><mi>x</mi><msup><mo>)</mo><mn>3</mn></msup></mrow><mn>6</mn></mfrac></mrow><mrow><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>8</mn><mn>3</mn></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>8</mn><mn>6</mn></mfrac></mstyle></mrow><mi>b</mi></mfrac><mo>=</mo><mfrac><mn>4</mn><mi>b</mi></mfrac></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mi>a</mi><mi>sin</mi><mfenced close="]" open="[" separators="|"><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>(</mo><mn>0</mn><mo>&#8722;</mo><mn>1</mn><mo>)</mo></mrow></mfenced><mo>=</mo><mi>a</mi><mi>sin</mi><mfenced separators="|"><mrow><mo>&#8722;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mo>&#8722;</mo><mi>a</mi></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>RHL</mi><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mfrac><mn>4</mn><mi>b</mi></mfrac><mo>=</mo><mo>&#8722;</mo><mi>a</mi><mo stretchy="false">&#8658;</mo><mo>&#8722;</mo><mi>a</mi><mi>b</mi><mo>=</mo><mn>4</mn><mo stretchy="false">&#8658;</mo><mn>10</mn><mo>&#8722;</mo><mi>a</mi><mi>b</mi><mo>=</mo><mn>14</mn></math></p>

</details>

---

### Q38. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be defined as, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced></mfrac></msup></mtd><mtd><mo>,</mo><mo>&#160;&#160;</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>e</mi><mrow><mi>cot</mi><mn>4</mn><mi>x</mi><mo>/</mo><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></msup></mtd><mtd><mo>,</mo><mo>&#160;&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mtd></mtr></mtable></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>a</mi><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mi>e</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>e</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>e</mi></math>**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>a</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>From the question, we can say that <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>b</mi></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><msup><mi>e</mi><mfrac><mrow><mi>cot</mi><mn>4</mn><mi>x</mi></mrow><mrow><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfrac></msup><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><msup><mi>e</mi><mfrac><mrow><mi>tan</mi><mn>2</mn><mi>x</mi></mrow><mrow><mi>tan</mi><mn>4</mn><mi>x</mi></mrow></mfrac></msup><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><msup><mi>e</mi><mfrac><mstyle displaystyle="true"><mfrac><mrow><mi>tan</mi><mn>2</mn><mi>x</mi></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>2</mn><mi>x</mi></mrow></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mrow><mi>tan</mi><mn>4</mn><mi>x</mi></mrow><mrow><mn>4</mn><mi>x</mi></mrow></mfrac></mstyle></mfrac></msup><mo>=</mo><msup><mi>e</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>=</mo><mi>b</mi></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced></mfrac></msup><mo>=</mo><msup><mi>e</mi><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfenced close="]" open="["><mrow><mfenced><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced></mfenced><mfenced><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced></mfrac></mfenced></mrow></mfenced></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>a</mi></mrow></msup></math></p><p>From the above we can say that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>3</mn><mi>a</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#8658;</mo><mn>6</mn><mi>a</mi><mo>=</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>6</mn><mi>a</mi><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>e</mi></mrow></mfenced></math></p>

</details>

---

### Q39. JEE Main 2021 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Consider the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>2</mn></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>2</mn></math>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>x</mi></mfenced></math> is a polynomial such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced></math> is always a constant and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>9</mn><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mn>5</mn></mfenced></math> is equal to __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **39**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfrac><mrow><mi>P</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>,</mo></mtd></mtr><mtr><mtd><mn>7</mn><mo>,</mo></mtd></mtr></mtable></mfenced><mtable><mtr><mtd><mi>x</mi><mo>&#8800;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>=</mo><mn>2</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo></math> Constant</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mi>x</mi></mfenced></math> is a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> degree polynomial</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>2</mn><mo>+</mo></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mn>2</mn><mo>-</mo></msup></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><mi>P</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>b</mi><mo>=</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mn>5</mn></mfenced><mo>=</mo><mfenced><mrow><mn>5</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>.</mo><mn>5</mn><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>.</mo><mn>13</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>39</mn><mo>.</mo></math></p>

</details>

---

### Q40. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnspacing="1.4ex" columnalign="left"><mtr><mtd><mfrac><mrow><mi>&#955;</mi><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced></mrow><mrow><mi>&#956;</mi><mfenced><mrow><mn>5</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn></mrow></mfenced></mrow></mfrac></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><msup><mi>e</mi><mfrac><mrow><mi>tan</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo></mrow><mrow><mi>x</mi><mo>-</mo><mo>[</mo><mi>x</mi><mo>]</mo></mrow></mfrac></msup></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>&#956;</mi></mtd><mtd><mi>x</mi><mo>=</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> is the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi></math> is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>(</mo><mo>-</mo><mi>e</mi><mo>+</mo><mn>1</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>(</mo><mi>e</mi><mo>-</mo><mn>2</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>e</mi><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>(</mo><mo>-</mo><mi>e</mi><mo>+</mo><mn>1</mn><mo>)</mo></math>**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>Here,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>+</mo></msup></mrow></munder><msup><mi>e</mi><mfrac><mrow><mi>tan</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo></mrow><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></msup><mo>=</mo><msup><mi>e</mi><mn>1</mn></msup><mo>=</mo><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><mi>&#955;</mi><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced></mrow><mrow><mi>&#956;</mi><mfenced><mrow><mn>5</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>2</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><mo>-</mo><mi>&#955;</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow><mrow><mi>&#956;</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mi>&#955;</mi><mi>&#956;</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mtext>if&#160;x&#160;&#60;&#160;2&#160;or&#160;x&#160;&#62;&#160;3</mtext></mtd></mtr><mtr><mtd><mo>-</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mtext>if&#160;2&#160;&#60;&#160;x&#160;&#60;&#160;3&#160;</mtext></mtd></mtr></mtable></mfenced></mrow></mfenced></math></p><p>For continuity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mi>e</mi><mo>=</mo><mo>-</mo><mfrac><mi>&#955;</mi><mi>&#956;</mi></mfrac><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mi>e</mi><mo>,</mo><mo>&#160;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><msup><mi>e</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>+</mo><mi>&#956;</mi><mo>=</mo><mi>e</mi><mo>(</mo><mo>-</mo><mi>e</mi><mo>+</mo><mn>1</mn><mo>)</mo></math></p>

</details>

---

### Q41. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="center left"><mtr><mtd><mfrac><msup><mi>x</mi><mn>3</mn></msup><mrow><mo>(</mo><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mn>2</mn></msup></mfrac></mfenced></mtd><mtd><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>A function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>a</mi><mo>,</mo></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>a</mi></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>.</mo></math></p><p>Thus, for continuity of the given function, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mrow><mo>(</mo><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mn>2</mn></msup></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>&#945;</mi></math></p><p>Using, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>,</mo><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mi>m</mi><mi>n</mi></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mi>m</mi><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mi>n</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#38;</mo><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><msup><mi>m</mi><mi>n</mi></msup><mo>=</mo><mi>n</mi><msub><mi>log</mi><mi>e</mi></msub><mi>m</mi><mo>,</mo></math></p><p>we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><msup><mfenced><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mrow><mn>4</mn><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mo>-</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>4</mn></msup><mrow><mn>4</mn><mi>x</mi><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi></mrow></mfrac><mfenced><mrow><mfrac><mrow><mn>2</mn><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>&#183;</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></mrow><mrow><mo>-</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>&#945;</mi></math></p><p>Now, using the standard limits <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mfenced><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mi>x</mi></mfrac></mfenced><mo>=</mo><mn>1</mn><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mrow><mn>4</mn><mi>x</mi></mrow></mfrac><mfenced><mrow><mn>2</mn><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>&#945;</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="[" close="]"><mrow><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>4</mn><mi>x</mi></mrow></mfrac><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mn>2</mn></mfenced><mo>=</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>.</mo></math></p>

</details>

---

### Q42. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mtable columnalign="left left" columnspacing="1em" rowspacing=".2em"><mtr><mtd><mi>sin</mi><mi>x</mi><mo>&#8722;</mo><msup><mi>e</mi><mi>x</mi></msup></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>a</mi><mo>+</mo><mfenced close="]" open="["><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>&#8722;</mo><mi>b</mi></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> is the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close="" separators="|"><mtable columnspacing="1em" rowspacing=".2em" columnalign="left left"><mtr><mtd><mi>sin</mi><mi>x</mi><mo>&#8722;</mo><msup><mi>e</mi><mi>x</mi></msup></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>a</mi><mo>+</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>&#8722;</mo><mi>b</mi></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>a</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>a</mi><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>a</mi><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced></math>.</p><p>Continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mn>0</mn><mo>-</mo></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>-</mo><msup><mi>e</mi><mn>0</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mn>0</mn></math></p><p>Continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>1</mn><mo>+</mo></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mn>1</mn><mo>-</mo></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn><mfenced><mn>1</mn></mfenced><mo>-</mo><mi>b</mi><mo>=</mo><mi>a</mi><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>2</mn><mo>-</mo><mi>a</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q43. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a function defined as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="center left"><mtr><mtd><mfrac><mrow><mi>sin</mi><mo>(</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo>)</mo><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mtd><mtd><mo>,</mo><mpadded lspace="-1px"><mi>if</mi></mpadded><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mo>,</mo><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mrow><msqrt><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup></msqrt><mo>-</mo><msqrt><mi>x</mi></msqrt></mrow><mrow><mi>b</mi><msup><mi>x</mi><mrow><mn>5</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfrac></mtd><mtd><mo>,</mo><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi></math> is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mi>b</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfenced><mrow><mfrac><mrow><mi>sin</mi><mo>(</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo>)</mo><mi>x</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><msqrt><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup></msqrt><mo>-</mo><msqrt><mi>x</mi></msqrt></mrow><mrow><mi>b</mi><msup><mi>x</mi><mrow><mn>5</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mfenced><mrow><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><mi>b</mi><msup><mi>x</mi><mrow><mn>5</mn><mo>/</mo><mn>2</mn></mrow></msup><mfenced><mrow><msqrt><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup></msqrt><mo>+</mo><msqrt><mi>x</mi></msqrt></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><msqrt><mi>x</mi></msqrt><mrow><msqrt><mi>x</mi></msqrt><mfenced><mrow><msqrt><mn>1</mn><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>Use <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>3</mn><mo>)</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>(</mo><mn>4</mn><mo>)</mo></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p>

</details>

---

### Q44. JEE Main 2021 (17 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>cos</mi><mo>(</mo><mi>sin</mi><mi>x</mi><mo>)</mo><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></math> is continuous at each point in its domain and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>k</mi></mfrac><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>cos</mi><mo>(</mo><mi>sin</mi><mi>x</mi><mo>)</mo><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>2</mn><mi>sin</mi><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mi>sin</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>k</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>2</mn><mi>sin</mi><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mi>sin</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow><mrow><mfenced><mstyle displaystyle="true"><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mn>2</mn></mfrac></mstyle></mfenced><mfenced><mstyle displaystyle="true"><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mstyle></mfenced><msup><mi>x</mi><mn>4</mn></msup></mrow></mfrac><mo>&#215;</mo><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>k</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mn>2</mn><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mfenced><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>k</mi></mfrac><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mfenced></mrow></mfenced><mfenced><mrow><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>k</mi></mfrac></math></p><p>Apply L&#39;Hospital rule for an indeterminate form of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>0</mn><mn>0</mn></mfrac></math>, we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#215;</mo><mfrac><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mo>&#160;</mo><mi>k</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q45. JEE Main 2021 (16 Mar Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="center left"><mtr><mtd><mi>x</mi><mo>+</mo><mi>a</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mi>b</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></math> are non-negative real numbers. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>o</mi><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is continuous for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi></math> is equal to ______ .<gwmw style="display:none;"></gwmw>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced close="]" open="["><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced close="" open="["><mtable><mtr><mtd><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mn>1</mn></mtd><mtd><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>(</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mi>b</mi></mtd><mtd><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced open="[" close="]"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced open="[" close=""><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mi>a</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>x</mi><mo>+</mo><mi>a</mi><mo>&#60;</mo><mn>0</mn><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>+</mo><mn>1</mn></mtd><mtd><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>&#60;</mo><mn>0</mn><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>(</mo><mi>x</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mi>b</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>a</mi><mo>&#8805;</mo><mn>0</mn><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>(</mo><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mi>b</mi></mtd><mtd><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>&#8805;</mo><mn>0</mn><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced open="[" close="]"><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced open="[" close=""><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mi>a</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mi>a</mi><mo>)</mo><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>0</mn><mo>)</mo></mtd></mtr><mtr><mtd><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>+</mo><mn>1</mn></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mi>&#981;</mi></mtd></mtr><mtr><mtd><mo>(</mo><mi>x</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mi>b</mi></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mi>a</mi><mo>,</mo><mo>&#8734;</mo><mo>)</mo><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>0</mn><mo>)</mo></mtd></mtr><mtr><mtd><mo>(</mo><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mi>b</mi></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced close="]" open="["><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced close="" open="["><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mi>a</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mi>a</mi><mo>)</mo></mtd></mtr><mtr><mtd><mo>(</mo><mi>x</mi><mo>+</mo><mi>a</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mi>b</mi></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mi>a</mi><mo>,</mo><mn>0</mn><mo>)</mo></mtd></mtr><mtr><mtd><mo>(</mo><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mi>b</mi></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>)</mo></math> is continuous</p><p>at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mi>a</mi><mo>&#160;&#160;</mo><mo>&#38;</mo></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>=</mo><mi>b</mi><mo>+</mo><mn>1</mn><mo>&#160;&#160;</mo><mo>&#38;</mo><mo>&#160;&#160;</mo><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mi>b</mi><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>0</mn><mo>&#160;&#160;</mo><mo>&#38;</mo><mo>&#160;&#160;</mo><mi>a</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q46. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi></math> be such that the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mfenced close="}" open="{"><mi>x</mi></mfenced><mn>2</mn></msup></mrow></mfenced><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfenced close="}" open="{"><mi>x</mi></mfenced></mrow></mfenced></mrow><mrow><mfenced close="}" open="{"><mi>x</mi></mfenced><mo>-</mo><msup><mfenced close="}" open="{"><mi>x</mi></mfenced><mn>3</mn></msup></mrow></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>,</mo><mfenced close="]" open="["><mi>x</mi></mfenced></math> is the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. Then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mi>&#960;</mi><msqrt><mn>2</mn></msqrt></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>0</mn></math>
- **(C)** no such <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> exists
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) no such <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> exists**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><msub><mo>Lim</mo><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></msub><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>&#183;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mi>x</mi><mo>&#183;</mo><mn>1</mn><mo>&#183;</mo><mn>1</mn></mrow></mfrac><mo>&#183;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mi>&#952;</mi><msqrt><mn>1</mn><mo>-</mo><mi>cos</mi><mi>&#952;</mi></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><munder><mi>lim</mi><mrow><mi>&#952;</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfrac><mi>&#952;</mi><mrow><msqrt><mn>2</mn></msqrt><mi>sin</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><msqrt><mn>2</mn></msqrt></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfrac><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mfenced><mrow><mo>-</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfrac><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mrow><mn>1</mn><mo>&#183;</mo><mn>2</mn></mrow></mfrac><mo>&#183;</mo><mfrac><mrow><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mi>x</mi></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>RHL</mi><mo>&#8800;</mo><mi>LHL</mi></math></p><p>Function can&#39;t be continuous</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> No value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> exist</p>

</details>

---

### Q47. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mi>&#8594;</mi><mi>R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left"><mtr><mtd><mn>2</mn><mi>sin</mi><mfenced><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mfenced close="|" open="|"><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>sin</mi><mfenced><mrow><mi>&#960;</mi><mi>x</mi></mrow></mfenced><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math><gwmw style="display:none;"></gwmw></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi></math> equals :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><msup><mn>1</mn><mo>-</mo></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mn>1</mn><mo>+</mo></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>a</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi>b</mi></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>+</mo></msup></mrow></munder><mi>sin</mi><mfenced><mi>&#960;x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> Also</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mo>-</mo><msup><mn>1</mn><mo>+</mo></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><mn>1</mn></mrow></munder><mn>2</mn><mi>sin</mi><mfenced><mfrac><mrow><mo>-</mo><mi>&#960;</mi><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>a</mi><mo>-</mo><mn>1</mn><mo>+</mo><mi>b</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mo>-</mo><mn>1</mn><mo>+</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p>Either <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>1</mn><mo>+</mo><mi>b</mi><mo>=</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>1</mn><mo>+</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>3</mn><mo>=</mo><mo>-</mo><mn>1</mn></math> (reject) </p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q48. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> is a function defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mi>&#960;</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mo>&#183;</mo></mfenced></math> denotes the greatest integer function, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is:

**Options:**

- **(A)** discontinuous only at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>
- **(B)** discontinuous at all integral values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> except at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>
- **(C)** continuous only at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>
- **(D)** continuous for every real <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) continuous for every real <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>**

**Detailed Solution:**

<p>Doubtful points are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>n</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>.</mo><mi>H</mi><mo>.</mo><mi>L</mi><mo>&#160;</mo><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>n</mi><mo>-</mo></msup></mrow></munder><mfenced open="[" close="]"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mi>&#960;</mi><mo>=</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>cos</mi><mfenced><mfrac><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mi>&#960;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>.</mo><mi>H</mi><mo>.</mo><mi>L</mi><mo>&#160;</mo><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>n</mi><mo>+</mo></msup></mrow></munder><mfenced close="]" open="["><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mi>&#960;</mi><mo>=</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mfenced><mfrac><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mi>&#960;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p>Hence continuous.</p>

</details>

---

### Q49. JEE Main 2020 (05 Sep Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>x</mi><mo>&#183;</mo><mfenced close="]" open="["><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>,</mo></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>10</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>10</mn><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> denotes the greatest integer function. Then the number of points of discontinuity of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>We know that the greatest integer function is discontinuous at integral points.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn><mo>&#60;</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>&#60;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfenced open="[" close="]"><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>5</mn><mo>,</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></math>, are the integer values.</p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mn>0</mn><mo>-</mo></msup></mfenced><mo>=</mo><mn>0</mn></math>, which means that function is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>x</mi><mo>&#8800;</mo><mo>-</mo><mn>10</mn><mo>&#8658;</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>&#8800;</mo><mo>-</mo><mn>5</mn></math></p><p>Hence, the function is discontinuous at points <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></math></p><p>The number of values is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> .</p>

</details>

---

### Q50. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>If a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mi>a</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>b</mi><msup><mi>e</mi><mrow><mo>&#8722;</mo><mi>x</mi></mrow></msup><mo>,</mo></mtd><mtd><mo>&#8722;</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>c</mi><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo></mtd><mtd><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>c</mi><mi>x</mi><mo>,</mo></mtd><mtd><mn>3</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math>be continuous for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>&#8712;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>2</mn></mfenced><mo>=</mo><mi>e</mi></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>e</mi><mo>+</mo><mn>13</mn></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>e</mi><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>e</mi><mo>-</mo><mn>13</mn></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>e</mi><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>e</mi><mo>+</mo><mn>13</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>e</mi><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>e</mi><mo>+</mo><mn>13</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>e</mi><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>e</mi><mo>+</mo><mn>13</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p> Continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>1</mn><mo>-</mo></msup></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#160;&#160;</mo><mo>&#8658;</mo><mi>a</mi><mi>e</mi><mo>+</mo><mi>b</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>c</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><msup><mn>3</mn><mo>+</mo></msup></mfenced><mo>&#160;</mo><mo>&#8658;</mo><mn>9</mn><mi>c</mi><mo>=</mo><mn>9</mn><mi>a</mi><mo>+</mo><mn>6</mn><mi>c</mi><mo>&#160;</mo><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>3</mn><mi>a</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>b</mi><mo>=</mo><mi>a</mi><mi>e</mi><mo>(</mo><mn>3</mn><mo>-</mo><mi>e</mi><mo>)</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mi>a</mi><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mi>b</mi><msup><mi>e</mi><mrow><mo>&#8722;</mo><mi>x</mi></mrow></msup><mo>,</mo></mtd><mtd><mo>&#8722;</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>c</mi><mi>x</mi><mo>,</mo></mtd><mtd><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>a</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>c</mi><mo>,</mo></mtd><mtd><mn>3</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>4</mn><mi>c</mi></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>0</mn><mo>)</mo><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>b</mi><mo>+</mo><mn>4</mn><mi>c</mi><mo>=</mo><mi>e</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>By using eq. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mn>3</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>4</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mi>e</mi><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>e</mi><mo>+</mo><mn>13</mn></mrow></mfrac></math></p>

</details>

---

### Q51. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mfenced close="]" open="[" separators="|"><mrow><mi>t</mi></mrow></mfenced></math> denote the greatest integer <math><mo>&#8804;</mo><mi>t</mi></math> and <math><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mi>x</mi><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>A</mi><mo>.</mo></mrow></mrow></math> Then the function, <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi>&#960;</mi><mi>x</mi></mrow></mfenced></mrow></mrow></math> is discontinuous, when <math><mi>x</mi></math> is equal to:

**Options:**

- **(A)** <math><msqrt><mi>A</mi><mo>+</mo><mn>1</mn></msqrt></math>
- **(B)** <math><msqrt><mi>A</mi><mo>+</mo><mn>5</mn></msqrt></math>
- **(C)** <math><msqrt><mi>A</mi><mo>+</mo><mn>21</mn></msqrt></math>
- **(D)** <math><msqrt><mi>A</mi></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><msqrt><mi>A</mi><mo>+</mo><mn>1</mn></msqrt></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></msub><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mn>4</mn><mi>x</mi></mfrac><mo>-</mo><mfenced close="}" open="{" separators="|"><mfrac><mn>4</mn><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>A</mi><mo>&#8658;</mo><msub><mi>log</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>O</mi></mrow></msub><mo>&#8289;</mo><mn>4</mn><mo>-</mo><mi>x</mi><mfenced close="}" open="{" separators="|"><mfrac><mn>4</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mi>A</mi></mrow></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mo>-</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>4</mn></math></p><p>Hence, for <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>5</mn></msqrt></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is discontinuous as it is an non-integral value.</p>

</details>

---

### Q52. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close="" separators="|"><mtable><mtr><mtd><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mtd><mtd><mo>;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mo>;</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mrow><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mfrac></mtd><mtd><mo>;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math> , then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi></math> is equal to:

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mo>-</mo><mn>1</mn></math>
- **(C)** <math><mn>0</mn></math>
- **(D)** <math><mo>-</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>0</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>0</mn><mo>-</mo></msup></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfenced><mrow><mfrac><mrow><mi>sin</mi><mi>a</mi><mi>x</mi><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><mi>x</mi></mfrac><mo>+</mo><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi><mi>cos</mi><mi>a</mi><mi>x</mi></mrow><mi>x</mi></mfrac><mo>+</mo><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>-</mo></msup></mrow></munder><mfenced><mrow><mi>a</mi><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>a</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>a</mi><mo>+</mo><mn>3</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>b</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><msup><mi>x</mi><mstyle displaystyle="true"><mfrac bevelled="true"><mn>1</mn><mn>3</mn></mfrac></mstyle></msup><msup><mi>x</mi><mstyle displaystyle="true"><mfrac bevelled="true"><mn>1</mn><mn>3</mn></mfrac></mstyle></msup></mfrac><mfenced separators="|"><mfrac><mrow><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>-</mo><mn>1</mn></mrow><mi>x</mi></mfrac></mfenced><mo>&#160;</mo></math>, this is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mn>0</mn><mn>0</mn></mfrac></mfenced></math>form</p><p>Apply <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LH</mi></math> Rule </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><msup><mn>0</mn><mo>+</mo></msup></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math><mi>b</mi><mo>=</mo><mn>1</mn></math></p><p><math><mo>&#8756;</mo><mi></mi><mi></mi><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q53. JEE Main 2020 (07 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

If the function <math><mi>f</mi></math> defined on <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mn>1</mn><mo>/</mo><mn>3</mn></mrow></mfenced></math> by <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>,</mo></mtd><mtd><mtext>when&#160;</mtext><mi>x</mi><mo>&#8800;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>k</mi></mtd><mtd><mo>,</mo><mtext>when&#160;</mtext><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>, is continuous, then <math><mi>k</mi></math> is equal to.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>x</mi></mrow></mfenced></mrow><mi>x</mi></mfrac><mo>-</mo><mfrac><mrow><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><mi>x</mi></mfrac></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>x</mi></mrow></mfenced></mrow><mrow><mn>3</mn><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>ln</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><munder><mi>lim</mi><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>ln</mi><mfenced close="}" open="{"><mrow><mn>1</mn><mo>+</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></mrow><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfrac><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p><math><mo>&#8756;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>, will be continuous if <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mrow><mrow><munder><mrow><mi mathvariant="normal">lim</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder></mrow><mo>&#8289;</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q54. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mo>(</mo><mi>p</mi><mo>+</mo><mn>1</mn><mo>)</mo><mi>x</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>q</mi></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mrow><msqrt><mi>x</mi><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>-</mo><msqrt><mi>x</mi></msqrt></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfrac></mtd><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math> , then the ordered pair <math><mo>(</mo><mi>p</mi><mo>,</mo><mi>&#160;</mi><mi>q</mi><mo>)</mo></math> is equal to:

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><mi>sin</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mi>&#160;</mi><mo>+</mo><mi>s</mi><mi>i</mi><mi>n</mi><mi>x</mi></mrow><mtable><mtr><mtd><mi>x</mi></mtd></mtr></mtable></mfrac></mtd></mtr><mtr><mtd><mi>q</mi></mtd></mtr><mtr><mtd><mfrac><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></msqrt><mo>-</mo><msqrt><mi>x</mi></msqrt></mrow><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></mtd></mtr></mtable><mi>&#160;</mi><mi mathvariant="normal">&#160;</mi><mtable><mtr><mtd><mo>:</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>:</mo><mi>x</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>:</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced><mi>&#160;</mi></math></p><p><math><mo>&#8757;</mo><mi>f</mi></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>.</mo><mi>H</mi><mo>.</mo><mi>L</mi><mo>=</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>&#160;</mi><mfrac><mrow><mi>sin</mi><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mo>-</mo><mi>h</mi></mrow></mfenced><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mo>(</mo><mo>-</mo><mi>h</mi><mo>)</mo></mrow><mrow><mo>-</mo><mi>h</mi></mrow></mfrac><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>h</mi><mo>+</mo><mi>sin</mi><mi>h</mi></mrow><mi>h</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>h</mi></mrow><mrow><mi>h</mi><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mfenced separators="|"><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>sin</mi><mi>h</mi></mrow><mi>h</mi></mfrac><mo>=</mo><mi>p</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn></math></p><p><math><mo>=</mo><mi>p</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>.</mo><mi>H</mi><mo>.</mo><mi>L</mi><mo>=</mo><mi>&#160;</mi><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>&#160;</mi><mfrac><mrow><msqrt><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><mi>h</mi><mo>-</mo></msqrt><mi>&#160;</mi><msqrt><mi>h</mi></msqrt></mrow><msup><mi>h</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mfrac><mo>&#215;</mo><mi>&#160;</mi><mfrac><mrow><msqrt><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><mi>h</mi></msqrt><mo>+</mo><msqrt><mi>h</mi></msqrt></mrow><mrow><msqrt><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><mi>h</mi></msqrt><mo>+</mo><msqrt><mi>h</mi></msqrt></mrow></mfrac><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>h</mi><mn>2</mn></msup><mo>+</mo><mi>h</mi><mo>-</mo><mi>h</mi></mrow><mrow><msup><mi>h</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>&#160;</mi><msup><mi>h</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mfenced separators="|"><mrow><msqrt><mi>h</mi><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p><math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><mi>h</mi></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>L</mi><mo mathvariant="italic">.</mo><mi>H</mi><mo mathvariant="italic">.</mo><mi>L</mi><mo mathvariant="italic">.</mo><mo>=</mo><mi>R</mi><mo>.</mo><mi>H</mi><mo>.</mo><mi>L</mi><mo>.</mo><mo>=</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>&#8658;</mo><mi>p</mi><mo>+</mo><mn>2</mn><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mi>q</mi></math>
<math><mo>=</mo><mtable><mtr><mtd><mi>p</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>q</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr></mtable><mi>&#160;</mi></math></p>

</details>

---

### Q55. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close="" separators="|"><mtable><mtr><mtd><mi>a</mi><mfenced open="|" close="|" separators="|"><mrow><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mo>,</mo><mtext>&#8201;</mtext><mtext>&#8201;</mtext><mi>x</mi><mo>&#8804;</mo><mn>5</mn></mtd></mtr><mtr><mtd><mi>b</mi><mfenced open="|" close="|" separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mo>,</mo><mtext>&#8201;</mtext><mtext>&#8201;</mtext><mi>x</mi><mo>&#62;</mo><mn>5</mn></mtd></mtr></mtable></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>5</mn><mo>,</mo></math> then the value of <math><mi>a</mi><mo>-</mo><mi>b</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mrow><mn>5</mn><mo>-</mo><mi>&#960;</mi></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mi>π</mi><mo>+</mo><mn>5</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mi>π</mi><mo>+</mo><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mi>π</mi><mo>-</mo><mn>5</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mrow><mn>5</mn><mo>-</mo><mi>&#960;</mi></mrow></mfrac></math>**

**Detailed Solution:**

<p>For continuity at <math><mi>x</mi><mo>=</mo><mn>5</mn></math></p><p><math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>5</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>5</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>5</mn><mo>+</mo></msup></mrow></munder><mfenced><mrow><mi>b</mi><mfenced open="|" close="|" separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>5</mn><mo>-</mo></msup></mrow></munder><mi>a</mi><mfenced><mrow><mfenced open="|" close="|" separators="|"><mrow><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left left"><mtr><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>-</mo><mn>1</mn><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>-</mo><mi>b</mi><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mi>&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>5</mn><mo>-</mo><mi>&#960;</mi></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mfrac><mn>2</mn><mrow><mn>5</mn><mo>-</mo><mi>&#960;</mi></mrow></mfrac><mo>.</mo></math></p>

</details>

---

### Q56. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the function <math><mi>f</mi></math> defined on <math><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>6</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close="" separators="|"><mtable><mtr><mtd><mfrac><mrow><msqrt><mn>2</mn></msqrt><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">t</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mtd></mtr><mtr><mtd><mi>k</mi><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mtd></mtr></mtable></mfenced></math> is continuous, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** <math><mn>2</mn></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mi>&#160;</mi></math> is continuous at <math><mi>x</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>f</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mi>k</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfenced><mfrac><mrow><msqrt><mn>2</mn></msqrt><mi>cos</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>cot</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>&#8594;</mo><mfenced><mfrac><mn>0</mn><mn>0</mn></mfrac></mfenced></math> form </p><p>Applying L&#39; Hospital Rule</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></munder><mfenced><mfrac><mrow><msqrt><mn>2</mn></msqrt><mfenced><mrow><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mo>-</mo><msup><mi>cosec</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mi>sin</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow><mrow><msup><mi>cosec</mi><mn>2</mn></msup><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>&#215;</mo><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced></mrow><msup><mfenced separators="|"><msqrt><mn>2</mn></msqrt></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q57. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>f</mi><mo>:</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mn>1,3</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">R</mi><mi mathvariant="normal">&#160;</mi></math> be defined as
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close="" separators="|"><mrow><mtable><mtr><mtd><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>+</mo><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>,</mo></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>,</mo></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>,</mo></mtd></mtr></mtable><mtable><mtr><mtd><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>3</mn><mo>,</mo></mtd></mtr></mtable></mrow></mfenced></math>
Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi mathvariant="normal">t</mi></mfenced></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>. Then, <math><mi>f</mi></math> is discontinuous at:

**Options:**

- **(A)** Only one point
- **(B)** Only two points
- **(C)** Four or more points
- **(D)** Only three points

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Only three points**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mtable><mtr><mtd><mfenced close="|" open="|" separators="|"><mi>x</mi></mfenced><mo>+</mo><mfenced close="]" open="[" separators="|"><mi>x</mi></mfenced><mo>;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mfenced close="|" open="|" separators="|"><mi>x</mi></mfenced><mo>;</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mfenced close="|" open="|" separators="|"><mi>x</mi></mfenced><mo>+</mo><mfenced close="]" open="[" separators="|"><mi>x</mi></mfenced><mo>;</mo><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="" open="{" separators="|"><mtable><mtr><mtd><mo>-</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mn>0</mn><mo>;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>;</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn><mo>;</mo><mn>2</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>6</mn><mo>;</mo><mi>x</mi><mo>=</mo><mn>3</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi></mtd></mtr></mtable></mfenced></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn></math> <math><mi>f</mi></math> changes its definition.</p><p><math><mo>&#8756;</mo></math> At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mi>LHL</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>RHL</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi mathvariant="normal">f</mi></math>  is discontinuous at</p><p><math><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi>LHL</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>RHL</mi><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi>f</mi></math> is discontinuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>LHL</mi><mo>=</mo><mi>RHL</mi><mo>=</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mi>f</mi></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>LHL</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>6</mn><mo>&#8658;</mo><mi>f</mi></math> is discontinuous at <math><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math><mo>&#8756;</mo></math> Points of discontinuity are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn><mo>.</mo></math></p>

</details>

---

### Q58. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a function defined as

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mrow><maligngroup></maligngroup><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mn>5</mn><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>i</mi><mi>f</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>&#8804;</mo><mn>1</mn></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mi>a</mi><mo>+</mo><mi>b</mi><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mi>i</mi><mi>f</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>3</mn></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mi>b</mi><mo>+</mo><mn>5</mn><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>i</mi><mi>f</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mn>3</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>5</mn></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mn>30</mn><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>i</mi><mi>f</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>&#8805;</mo><mn>5</mn></mrow></mtd></mtr></mtable></mrow></mfenced><mi>&#160;</mi></math>

Then <math><mi>f</mi></math> is:

**Options:**

- **(A)** continuous if  <math><mi>a</mi><mo>=</mo><mo>-</mo><mn>5</mn></math>  and  <math><mi>b</mi><mo>=</mo><mn>10</mn></math>
- **(B)** continuous if  <math><mi>a</mi><mo>=</mo><mn>0</mn></math>  and  <math><mi>b</mi><mo>=</mo><mn>5</mn></math>
- **(C)** not continuous for any values of  <math><mi>a</mi></math>  and  <math><mi>b</mi></math>
- **(D)** continuous if  <math><mi>a</mi><mo>=</mo><mn>5</mn></math>  and  <math><mi>b</mi><mo>=</mo><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) not continuous for any values of  <math><mi>a</mi></math>  and  <math><mi>b</mi></math>**

**Detailed Solution:**

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mrow><maligngroup/><mn>5</mn><mo>:</mo><mi>x</mi><mo>≤</mo><mn>1</mn></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup/><mi>a</mi><mo>+</mo><mi>b</mi><mi>x</mi><mo>:</mo><mn>1</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>3</mn></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup/><mi>b</mi><mo>+</mo><mn>5</mn><mi>x</mi><mo>:</mo><mn>3</mn><mo>≤</mo><mi>x</mi><mo>&lt;</mo><mn>5</mn></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup/><mn>30</mn><mo>:</mo><mi>x</mi><mo>≥</mo><mn>5</mn></mrow></mtd></mtr></mtable></mrow></mfenced><mi> </mi></math>  

        For  <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>  to be continuous at  <math><mi>x</mi><mo>=</mo><mn>5</mn></math> 

         <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>5</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>5</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>5</mn></mrow></mfenced></math> 

         <math><mo>⇒</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>5</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder><mfenced separators="|"><mrow><mi>b</mi><mo>+</mo><mn>5</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mn>30</mn></math> 

         <math><mo>⇒</mo><mi>b</mi><mo>+</mo><mn>25</mn><mo>=</mo><mn>30</mn><mo>⇒</mo><mi>b</mi><mo>=</mo><mn>5</mn></math> 

        For  <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>  to be continuous at  <math><mi>x</mi><mo>=</mo><mn>1</mn></math> 

         <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>1</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>1</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></math> 

         <math><mo>⇒</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>1</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mn>5</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mn>5</mn></math> 

 <math><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>0</mn></math> 

        Now at  <math><mi>x</mi><mo>=</mo><mn>3</mn><mo>,</mo></math> 

         <math><mi>L</mi><mi>H</mi><mi>L</mi><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>-</mo></mrow></msup></mrow></munder><mfenced separators="|"><mrow><mn>0</mn><mo>+</mo><mn>5</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mn>15</mn></math> 

         <math><mi>R</mi><mi>H</mi><mi>L</mi><mo>=</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>→</mo><msup><mrow><mn>3</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mfenced separators="|"><mrow><mn>5</mn><mo>+</mo><mn>5</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mn>20</mn></math> 

        Hence function  <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>  is discontinuous at  <math><mi>x</mi><mo>=</mo><mn>3</mn></math>  for all  <math><mi>a</mi><mo>,</mo><mtext> </mtext><mi>b</mi><mo>∈</mo><mi>R</mi></math> .

</details>

---

### Q59. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If the function <math><mi>f</mi></math> defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>-</mo><mfrac><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math>, then ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>k</mi><mo>,</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>-</mo><mfrac><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></math></p><p>and <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>-</mo><mfrac><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><msup><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>x</mi><mfenced separators="|"><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></mrow></mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mfenced separators="|"><mfrac><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><msup><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mi>x</mi><mfenced separators="|"><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></mrow></mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>Clearly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math>Equating coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo></math></p>

</details>

---

### Q60. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x)=\left\{\begin{array}{cc}(x-1)^{\frac{1}{2-x}}, & x>1, x \neq 2 \\ k, & x=2\end{array}\right.$
The value of $k$ for which $f$ is continuous at $x=2$ is

**Options:**

- **(A)** $e^{-2}$
- **(B)** $e$
- **(C)** $e^{-1}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $e^{-1}$**

**Detailed Solution:**

Since $f(x)$ is continuous at $x=2$.
$$
\begin{aligned}
&\therefore \lim _{x \rightarrow 2} f(x)=f(2) \\
&\Rightarrow \lim _{x \rightarrow 2}(x-1)^{\frac{1}{2-x}}=k \quad\left(1^{\infty} \text { form }\right) \\
&\therefore e^{l=k}
\end{aligned}
$$
where
$$
\begin{aligned}
&l=\lim _{x \rightarrow 2}(x-1-1) \times \frac{1}{2-x}=\lim _{x \rightarrow 2} \frac{x-2}{2-x} \\
&=\lim _{x \rightarrow 2}\left(\frac{x-2}{x-2}\right) \\
&\Rightarrow k=e^{-1}
\end{aligned}
$$

</details>

---

### Q61. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> which the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>&#160;</mi><mfenced close="" open="{" separators="|"><mtable><mtr><mtd><msup><mfenced separators="|"><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mfrac><mrow><mi>tan</mi><mo>&#8289;</mo><mn>4</mn><mi>x</mi></mrow><mrow><mi>tan</mi><mo>&#8289;</mo><mn>5</mn><mi>x</mi></mrow></mfrac></msup><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mi>k</mi><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(B)** <math><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>17</mn></mrow><mrow><mn>20</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given function is continuous at <math> <mrow> <mi>x</mi><mo>=</mo><mfrac> <mi>&#960;</mi> <mn>2</mn> </mfrac> </mrow> </math>

<math><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>&#960;</mi></mrow><mrow><mo>+</mo></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>&#960;</mi></mrow><mrow><mo>-</mo></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>=</mo><msup><mfenced separators="|"><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mfrac><mrow><mi>tan</mi><mo>&#8289;</mo><mn>4</mn><mi>x</mi></mrow><mrow><mi>tan</mi><mo>&#8289;</mo><mn>5</mn><mi>x</mi></mrow></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>=</mo><msup><mfenced><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mrow><mi>tan</mi><mfenced><mrow><mn>2</mn><mi>&#960;</mi></mrow></mfenced><mi>cot</mi><mfenced><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>=</mo><msup><mfenced separators="|"><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mn>0</mn></msup><mi>&#160;</mi><mi>&#160;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>=</mo><mn>1</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mn>3</mn><mn>5</mn></mfrac></math></p>

</details>

---

### Q62. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mfenced separators="|"><mrow><mi>a</mi><mo>&#8800;</mo><mn>0</mn></mrow></mfenced><mo>.</mo></math> If the function <math><mi>f</mi></math>, defined as

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mi>a</mi></mfrac><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>a</mi><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><msqrt><mn>2</mn></msqrt></mtd></mtr><mtr><mtd><mfrac><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>b</mi></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>,</mo><mo>&#160;</mo><msqrt><mn>2</mn></msqrt><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>8</mn></mtd></mtr></mtable></mfenced></math>,is continuous in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced></math>, then an ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> can be

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>,</mo><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>,</mo><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mi> </mi><mn>1</mn><mo>+</mo><mi> </mi><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>,</mo><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/516377a5-d390-4a5d-9900-91ca1e7916d0-image.png" style="width: 382px; height: 98px;" />
Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is continuous at <math><mi>x</mi><mo>=</mo><mn>1&#160;</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math>
<math><mo>&#8658;</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>a</mi></mrow></mfrac><mo>=</mo><mi>a</mi><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mi>&#160;</mi><mo>&#177;</mo><mi>&#160;</mi><mi>&#160;</mi><msqrt><mn>2</mn></msqrt></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is continuous at <math><mi>x</mi><mo>=</mo><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><msqrt><mn>2</mn></msqrt><mo>-</mo></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><msqrt><mn>2</mn></msqrt><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>b</mi></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p><p>Put <math><mi>a</mi><mo>=</mo><mi>&#160;</mi><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>=</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>b</mi><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>b</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mo>2&#177;</mo><mi>&#160;</mi><msqrt><mn>4</mn><mo>+</mo><mn>4.2</mn></msqrt></mrow><mn>2</mn></mfrac><mo>=</mo><mn>1</mn><mo>&#177;</mo><mi>&#160;</mi><msqrt><mn>3</mn></msqrt></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8801;</mo><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>,</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math></p>

</details>

---

### Q63. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> be a non - zero real number. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left"><mtr><mtd><mfrac><msup><mrow><mo>(</mo><msup><mi>e</mi><mi>x</mi></msup><mo>&#8722;</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></msup><mrow><mi>sin</mi><mi>&#8201;</mi><mfenced><mfrac><mi>x</mi><mi>k</mi></mfrac></mfenced><mi>log</mi><mi>&#8201;</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac><mtable><mtr><mtd><mo>,</mo></mtd><mtd><mi>x</mi><mi>&#8201;</mi><mo>&#8800;</mo><mi>&#8201;</mi><mn>0</mn></mtd></mtr></mtable></mtd></mtr><mtr><mtd><mtable><mtr><mtd><mn>12</mn><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mi>&#8201;</mi><mo>,</mo></mtd><mtd><mi>x</mi><mi>&#8201;</mi><mo>=</mo><mi>&#8201;</mi><mn>0</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced><mi>&#8201;</mi></math> is a continuous function at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

If the function is continuous then

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><msup><mrow><mo>(</mo><msup><mi>e</mi><mi>x</mi></msup><mo>&#8722;</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></msup><mrow><mi>sin</mi><mfrac><mi>x</mi><mi>k</mi></mfrac><mo>.</mo><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>12</mn></math>

<math> <mo>&#8658;</mo> </math><math>&#160;</math><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><msup><mfenced separators="|"><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow><mi>x</mi></mfrac></mfenced><mn>2</mn></msup><mrow><mfrac><mrow><mi>sin</mi><mfrac><mi>x</mi><mi>k</mi></mfrac></mrow><mrow><mi>k</mi><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mi>&#160;</mi><mfrac><mi>x</mi><mi>k</mi></mfrac></mrow></mfrac><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mi>&#160;</mi><mfrac><mrow><mi>log</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mn>4</mn></mfrac></mrow></mfenced></mrow><mrow><mn>4</mn><mo>.</mo><mi>&#160;</mi><mi>&#160;</mi><mfrac><mi>x</mi><mn>4&#160;&#160;</mn></mfrac></mrow></mfrac></mrow></mfrac></math> = 12

<math> <mo>&#8658;</mo></math><math>&#160;</math><math><mfrac><mrow><mn>1</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>k</mi></mrow></mfrac><mi>&#160;</mi><mo>.</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mn>12</mn></math>

<math> <mo>&#8658;</mo></math><math>&#160;</math><math><mn>4</mn><mi>k</mi><mo>=</mo><mn>12</mn></math>

<math> <mo>&#8658;</mo> </math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>3</mn></math>

</details>

---

### Q64. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mrow><msqrt><mn>2</mn><mo>+</mo><mo>cos</mo><mi>x</mi></msqrt><mo>-</mo><mn>1</mn></mrow><msup><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8800;</mo><mi>&#960;</mi></mtd></mtr><mtr><mtd><mi>k</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mi>&#960;</mi></mtd></mtr></mtable></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#960;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> equals

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfrac><mrow><msqrt><mn>2</mn><mo>+</mo><mo>cos</mo><mi>x</mi></msqrt><mo>-</mo><mn>1</mn></mrow><msup><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8800;</mo><mi>&#960;</mi></mtd></mtr><mtr><mtd><mi>k</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>=</mo><mi>&#960;</mi></mtd></mtr></mtable></mfenced></math> is continuous at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#960;</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi mathvariant="normal">&#960;</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mi>&#960;</mi></mrow></munder><mfrac><mrow><msqrt><mn>2</mn><mo>+</mo><mi>cos</mi><mi>x</mi></msqrt><mo>-</mo><mn>1</mn></mrow><msup><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p>Consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>.</mo><mi>H</mi><mo>.</mo><mi>L</mi><mo>.</mo><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mi>&#960;</mi><mo>-</mo></msup></mrow></munder><mfrac><mrow><msqrt><mn>2</mn><mo>+</mo><mi>cos</mi><mo mathvariant="italic">x</mo></msqrt><mo>-</mo><mn>1</mn></mrow><msup><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msqrt><mn>2</mn><mo>+</mo><mi>cos</mi><mrow><mo>(</mo><mi>&#960;</mi><mo>-</mo><mi>h</mi><mo>)</mo></mrow></msqrt><mo>-</mo><mn>1</mn></mrow><msup><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>h</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></mfrac></math>

Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mi>h</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>cos</mi><mo>&#160;</mo><mi>h</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msqrt><mn>2</mn><mo>-</mo><mi>cos</mi><mi>h</mi></msqrt><mo>-</mo><mn>1</mn></mrow><msup><mi>h</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><msqrt><mn>2</mn><mo>-</mo><mi>cos</mi><mi>h</mi></msqrt><mo>-</mo><mn>1</mn></mrow><msup><mi>h</mi><mn>2</mn></msup></mfrac></mfenced><mo>&#215;</mo><mfenced><mfrac><mrow><msqrt><mn>2</mn><mo>-</mo><mi>cos</mi><mi>h</mi></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>2</mn><mo>-</mo><mi>cos</mi><mi>h</mi></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi mathvariant="normal">k</mi><mi mathvariant="normal">=</mi><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mfenced><mrow><mn>2</mn><mo>-</mo><mi>cos</mi><mi>h</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>h</mi><mn>2</mn></msup><mfenced close="}" open="{"><mrow><msqrt><mn>2</mn><mo>-</mo><mi>cos</mi><mi>h</mi></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi mathvariant="normal">k</mi><mi mathvariant="normal">=</mi><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mi>h</mi></mrow><msup><mi>h</mi><mn>2</mn></msup></mfrac></mfenced><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mn>1</mn><mfenced close="}" open="{"><mrow><msqrt><mn>2</mn><mo>-</mo><mi>cos</mi><mi>h</mi></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>2</mn><msup><mo>sin</mo><mn>2</mn></msup><mfenced><mfrac><mi>h</mi><mn>2</mn></mfrac></mfenced></mrow><mrow><mn>4</mn><msup><mfenced><mfrac><mi>h</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mfenced><mrow><msqrt><mn>2</mn><mo>-</mo><mn>1</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q65. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Consider the function :
$f(x)=[x]+|1-x|,-1 \leq x \leq 3$ where $[x]$ is the greatest integer function.
Statement 1: $f$ is not continuous at $x=0,1,2$ and 3 
Statement 2:f(x)= $=\begin{array}{cc}-x, & -1 \leq x < 0 \\ 1-x, & 0 \leq x < 1 \\ 1+x, & 1 \leq x < 2 \\ 2+x, & 2 \leq x \leq 3\end{array}$

**Options:**

- **(A)** Statement 1 is true; Statement 2 is false,
- **(B)** Statement 1 is true; Statement 2 is true; Statement 2 is not correct explanation for Statement 1.
- **(C)** Statement 1 is true; Statement 2 is true; Statement It is a correct explanation for Statement 1.
- **(D)** Statement 1 is false; Statement 2 is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement 1 is true; Statement 2 is false,**

**Detailed Solution:**

Let $f(x)=[x]+|1-x|,-1 \leq x \leq 3$ where $[x]=$ greatest integer function. $f$ is not continuous at $x=0,1,2,3$ But in statement-2 $f(x)$ is continuous at $x=3$.

Hence, statement-1 is true and 2 is false.

</details>

---

### Q66. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $f$ be a composite function of $x$ defined by $f(u)=\frac{1}{u^2+u-2}, u(x)=\frac{1}{x-1}$.
Then the number of points $x$ where $f$ is discontinuous is :

**Options:**

- **(A)** 4
- **(B)** 3
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3**

**Detailed Solution:**

$\mu(x)=\frac{1}{x-1}$, which is discontinous at $x=1$
$$
f(u)=\frac{1}{u^2+u-2}=\frac{1}{(u+2)(u-1)},
$$
which is discontinous at $u=-2,1$
when $u=-2$, then $\frac{1}{x-1}=-2 \Rightarrow x=\frac{1}{2}$
when $u=1$, then $\frac{1}{x-1}=1 \Rightarrow x=2$
Hence given composite function is discontinous at three points, $x=1, \frac{1}{2}$ and 2 .

</details>

---

### Q67. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=-1+|x-2|$, and $g(x)=1-|x|$; then the set of all points where $f_{o g}$ is discontinuous is :

**Options:**

- **(A)** $\{0,2\}$
- **(B)** $\{0,1,2\}$
- **(C)** $\{0\}$
- **(D)** an empty set

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) an empty set**

**Detailed Solution:**

$$
\text { } \begin{aligned}
& f \circ g=f(g(x))=f(1-|x|) \\
& =-1+|1-| x|-2| \\
& =-1+|-| x|-1|=-1+|| x|+1|
\end{aligned}
$$
Let $f \circ g=y$
$$
\begin{aligned}
& \therefore y=-1+|| x|+1| \\
& \Rightarrow y= \begin{cases}-1+x+1, & x \geq 0 \\
-1-x+1, & x < 0\end{cases} \\
& \Rightarrow y=\left\{\begin{array}{cc}
x, & x \geq 0 \\
-x, & x < 0
\end{array}\right.
\end{aligned}
$$
LHL at $(x=0)=\lim _{x \rightarrow 0}(-x)=0$
RHL at $(x=0)=\lim _{x \rightarrow 0}(x)=0$
When $x=0$, then $y=0$
Hence, LHL at $(x=0)=$ RHL at $(x=0)=$ value of $y$ at $(x=0)$
Hence $y$ is continuous at $x=0$.
Clearly at all other point $y$ continuous. Therefore, the set of all points where fog is discontinuous is an empty set.

</details>

---

### Q68. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `3`

Let $f:[1,3] \rightarrow R$ be a function satisfying $\frac{x}{[x]} \leq f(x) \leq \sqrt{6-x}$, for all $x \neq 2$ and $f(2)=1$, where $R$ is the set of all real numbers and $[x]$ denotes the largest integer less than or equal to $x$.
Statement 1: $\lim _{x \rightarrow 2^{-}} f(x)$ exists.
Statement 2: $f$ is continuous at $x=2$.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation for Statement 1.
- **(B)** Statement 1 is false, Statement 2 is true.
- **(C)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation for Statement 1.
- **(D)** Statement 1 is true, Statement 2 is false.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement 1 is true, Statement 2 is false.**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Consider } \frac{x}{[x]} \leq f(x) \leq \sqrt{6-x} \\
& \Rightarrow \lim _{x \rightarrow 2^{-}} \frac{x}{[x]}=\frac{2}{1}=2
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow \lim _{x \rightarrow 2^{-}} \sqrt{6-x}=2 \\
& \therefore \lim _{x \rightarrow 2^{-}} f(x)=2
\end{aligned}
$$
[By Sandwich theorem]
Now $\lim _{x \rightarrow 2^{+}} \frac{x}{[x]}=1, \lim _{x \rightarrow 2^{+}} \sqrt{6-x}=2$
Hence by Sandwich theorem $\lim _{x \rightarrow 2^{+}} f(x)$ does not exists.
Therefore $f$ is not continuous at $x=2$. Thus statement-1 is true but statement- 2 is not true

</details>

---

### Q69. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Statement 1: A function $f: R \rightarrow R$ is continuous at $x_0$ if and only if $\lim _{x \rightarrow x_0} f(x)$ exists and $\lim _{x \rightarrow x_0} f(x)=f\left(x_0 \cdot\right)$
Statement 2: A function $f: R \rightarrow R$ is discontinuous at $x_0$ if and only if, $\lim _{x \rightarrow x_0} f(x)$ exists and $\lim _{x \rightarrow x_0} f(x) \neq f\left(x_0.\right)$

**Options:**

- **(A)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation of Statement 1.
- **(B)** Statement 1 is false, Statement 2 is true.
- **(C)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation of Statement 1.
- **(D)** Statement 1 is true, Statement 2 is false.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement 1 is true, Statement 2 is false.**

**Detailed Solution:**

Statement-1 is true.
It is the definition of continuity.
Statement $-2$ is false.

</details>

---

### Q70. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}: \mathrm{R} \rightarrow \mathrm{R}$ is a function defined by $f(x)=[\mathrm{x}] \cos \left(\frac{2 x-1}{2}\right) \pi$, where $[\mathrm{x}]$ denotes the greatest integer function, then $f$ is

**Options:**

- **(A)** continuous for every real $x$
- **(B)** discontinuous only at $x=0$
- **(C)** discontinuous only at non-zero integral values of $x$
- **(D)** continuous only at $x=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) continuous for every real $x$**

**Detailed Solution:**

$f(x)=[x] \cos \left(\frac{2 x-1}{2}\right) \pi=[x] \cos \left(x-\frac{1}{2}\right) \pi$
$=[x] \sin \pi x$ is continuous for every real $x$.

</details>

---

### Q71. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `1`

The value of $p$ and $q$ for which the function $f(x)=\left\{\begin{array}{cl}\frac{\sin (p+1) x+\sin x}{x} & x < 0 \\ q & , x=0 \\ \frac{\sqrt{x+x^2}-\sqrt{x}}{x^{3 / 2}} & , x>0\end{array}\right.$ is continuous for all $\mathrm{x}$ in $\mathrm{R}$, is

**Options:**

- **(A)** $p=\frac{5}{2}, q=\frac{1}{2}$
- **(B)** $p=-\frac{3}{2}, q=\frac{1}{2}$
- **(C)** $p=\frac{1}{2}, q=\frac{3}{2}$
- **(D)** $p=\frac{1}{2}, q=-\frac{3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $p=-\frac{3}{2}, q=\frac{1}{2}$**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{\sin (p+1)+\sin x}{x}=q=\lim _{x \rightarrow 0} \frac{\sqrt{x+x^2}-\sqrt{x}}{x^{3 / 2}}$
$\lim _{x \rightarrow 0}(p+1) \cos (p+1) x+\cos x=q=\frac{1}{2}$
$\Rightarrow p+1+1=\frac{1}{2} \Rightarrow p=-\frac{3}{2} ; q=\frac{1}{2}$

</details>

---

### Q72. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `2`

Let $f: R \rightarrow R$ be a continuous function defined by $f(x)=\frac{1}{e^x+2 e^{-x}}$.
Statement-1: $f(c)=\frac{1}{3}$, for some $c \in R$.
Statement-2: $0 < f(x) \leq \frac{1}{2 \sqrt{2}}$, for all $x \in R$

**Options:**

- **(A)** Statement-1 is true, Statement-2 is true; Statement-2 is not the correct explanation for Statement-1
- **(B)** Statement-1 is true, Statement-2 is false
- **(C)** Statement-1 is false, Statement-2 is true
- **(D)** Statement-1 is true, Statement-2 is true; Statement-2 is the correct explanation for Statement-1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement-1 is true, Statement-2 is true; Statement-2 is the correct explanation for Statement-1**

**Detailed Solution:**

$f(x)=\frac{1}{e^x+2 e^{-x}}=\frac{e^x}{e^{2 x}+2}$
$f^{\prime}(x)=\frac{\left(e^{2 x}+2\right) e^x-2 e^{2 x} \cdot e^x}{\left(e^{2 x+2}\right)^2}$
$f^{\prime}(x)=0 \quad \Rightarrow e^{2 x}+2=2 e^{2 x}$
$\mathrm{e}^{2 \mathrm{x}}=2 \quad \Rightarrow \mathrm{e}^{\mathrm{x}}=\sqrt{2}$
maximum $f(x)=\frac{\sqrt{2}}{4}=\frac{1}{2 \sqrt{2}}$
$0 < f(x) \leq \frac{1}{2 \sqrt{2}} \quad \forall x \in R$
Since $0 < \frac{1}{3} < \frac{1}{2 \sqrt{2}} \quad \Rightarrow$ for some $c \in R$
$f(c)=\frac{1}{3}$

</details>

---

### Q73. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `1`

f is defined in [-5, 5] as f(x) = x if x is rational and = -x is irrational. Then

**Options:**

- **(A)** f(x) is continuous at every x, except x = 0
- **(B)** f(x) is discontinuous at every x, except x = 0
- **(C)** f(x) is continuous everywhere
- **(D)** f(x) is discontinuous everywhere

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) f(x) is discontinuous at every x, except x = 0**

**Detailed Solution:**

No Solution Available

</details>

---

