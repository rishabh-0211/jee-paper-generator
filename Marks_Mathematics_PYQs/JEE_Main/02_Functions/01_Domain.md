# JEE Main Mathematics - Functions

## Topic 1: Domain

**Total Questions:** 44

---

### Q1. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $[\cdot]$ denote the greatest integer function. If the domain of the function $f(x) = \cos^{-1}\left(\dfrac{4x+2[x]}{3}\right)$ is $[\alpha, \beta]$, then $12(\alpha + \beta)$ is equal to:

**Options:**

- **(A)** $6$
- **(B)** $8$
- **(C)** $9$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6$**

**Detailed Solution:**

For the domain of $f(x) = \cos^{-1}\left(\dfrac{4x+2[x]}{3}\right)$, the argument must satisfy:

$-1 \le \dfrac{4x+2[x]}{3} \le 1$

$-3 \le 4x + 2[x] \le 3$

Let $x = I + f$, where $I = [x] \in \mathbb{Z}$ and $f = \{x\} \in [0, 1)$. Substituting $x = I + f$ into the inequality:

$-3 \le 4(I + f) + 2I \le 3$

$-3 \le 6I + 4f \le 3$

Since $0 \le f < 1$, we have $0 \le 4f < 4$. We can check the possible integer values of $I$:
If $I \ge 1$, $6I + 4f \ge 6(1) + 0 = 6 > 3$, which gives no solution.
If $I \le -2$, $6I + 4f < 6(-2) + 4 = -8 < -3$, which gives no solution.

Thus, the only possible values for $I$ are $0$ and $-1$.

Case 1: $I = 0$
$-3 \le 6(0) + 4f \le 3 \Rightarrow -3 \le 4f \le 3 \Rightarrow -\dfrac{3}{4} \le f \le \dfrac{3}{4}$
Since $f \in [0, 1)$, we get $0 \le f \le \dfrac{3}{4}$.
Therefore, $x = I + f \in \left[0, \dfrac{3}{4}\right]$.

Case 2: $I = -1$
$-3 \le 6(-1) + 4f \le 3 \Rightarrow 3 \le 4f \le 9 \Rightarrow \dfrac{3}{4} \le f \le \dfrac{9}{4}$
Since $f \in [0, 1)$, we get $\dfrac{3}{4} \le f < 1$.
Therefore, $x = I + f \in \left[-1 + \dfrac{3}{4}, -1 + 1\right) = \left[-\dfrac{1}{4}, 0\right)$.

Taking the union of the intervals from both cases, the domain is $x \in \left[-\dfrac{1}{4}, \dfrac{3}{4}\right]$.

Comparing this with $[\alpha, \beta]$, we get $\alpha = -\dfrac{1}{4}$ and $\beta = \dfrac{3}{4}$.

Finally, evaluating the required expression:

$12(\alpha + \beta) = 12\left(-\dfrac{1}{4} + \dfrac{3}{4}\right) = 12\left(\dfrac{2}{4}\right) = 12\left(\dfrac{1}{2}\right) = 6$

Answer: $6$

</details>

---

### Q2. JEE Main 2026 (02 April Shift 1)

*Type:* `numerical` | *Level:* `3`

If the domain of the function $f(x) = \sqrt{\log_{(0.6)}\left(\left|\dfrac{2x-5}{x^2-4}\right|\right)}$ is $(-\infty, a] \cup \{b\} \cup [c, d) \cup (e, \infty)$, then the value of $a + b + c + d + e$ is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

For the function $f(x) = \sqrt{\log_{0.6}\left(\left|\dfrac{2x-5}{x^2-4}\right|\right)}$ to be defined, two conditions must be satisfied:

1. The argument of the logarithm must be strictly positive:
$\left|\dfrac{2x-5}{x^2-4}\right| > 0 \implies 2x - 5 \neq 0 \implies x \neq \dfrac{5}{2}$
Also, the denominator cannot be zero:
$x^2 - 4 \neq 0 \implies x \neq \pm 2$

2. The expression inside the square root must be non-negative:
$\log_{0.6}\left(\left|\dfrac{2x-5}{x^2-4}\right|\right) \ge 0$

Since the base of the logarithm is $0.6 < 1$, the inequality sign reverses when removing the logarithm:
$\left|\dfrac{2x-5}{x^2-4}\right| \le (0.6)^0$
$\left|\dfrac{2x-5}{x^2-4}\right| \le 1$

Since both sides are non-negative, we can square both sides:
$(2x-5)^2 \le (x^2-4)^2$
$(x^2-4)^2 - (2x-5)^2 \ge 0$

Using the identity $A^2 - B^2 = (A-B)(A+B)$:
$(x^2 - 4 - 2x + 5)(x^2 - 4 + 2x - 5) \ge 0$
$(x^2 - 2x + 1)(x^2 + 2x - 9) \ge 0$
$(x - 1)^2 (x^2 + 2x - 9) \ge 0$

Since $(x - 1)^2 \ge 0$ for all real $x$, the inequality holds if:
$x - 1 = 0 \implies x = 1$
or
$x^2 + 2x - 9 \ge 0$

Finding the roots of $x^2 + 2x - 9 = 0$ using the quadratic formula:
$x = \dfrac{-2 \pm \sqrt{4 - 4(1)(-9)}}{2} = \dfrac{-2 \pm \sqrt{40}}{2} = -1 \pm \sqrt{10}$

Thus, $x^2 + 2x - 9 \ge 0$ gives:
$x \in (-\infty, -1 - \sqrt{10}] \cup [-1 + \sqrt{10}, \infty)$

Combining this with $x = 1$, the solution to the inequality is:
$x \in (-\infty, -1 - \sqrt{10}] \cup \{1\} \cup [-1 + \sqrt{10}, \infty)$

Now, we must exclude the restricted values $x = \pm 2$ and $x = \dfrac{5}{2}$.
Note that $-1 - \sqrt{10} \approx -4.16$ and $-1 + \sqrt{10} \approx 2.16$.
The values $-2$ and $2$ do not fall in the above intervals, so they are already excluded.
However, $\dfrac{5}{2} = 2.5$, which lies in the interval $[-1 + \sqrt{10}, \infty)$. We must exclude it by splitting the interval:
$[-1 + \sqrt{10}, \dfrac{5}{2}) \cup (\dfrac{5}{2}, \infty)$

The final domain of the function is:
$(-\infty, -1 - \sqrt{10}] \cup \{1\} \cup [-1 + \sqrt{10}, \dfrac{5}{2}) \cup (\dfrac{5}{2}, \infty)$

Comparing this with the given domain $(-\infty, a] \cup \{b\} \cup [c, d) \cup (e, \infty)$, we get:
$a = -1 - \sqrt{10}$
$b = 1$
$c = -1 + \sqrt{10}$
$d = \dfrac{5}{2}$
$e = \dfrac{5}{2}$

We need to find the value of $a + b + c + d + e$:
$a + b + c + d + e = (-1 - \sqrt{10}) + 1 + (-1 + \sqrt{10}) + \dfrac{5}{2} + \dfrac{5}{2}$
$= -1 - \sqrt{10} + 1 - 1 + \sqrt{10} + 5$
$= 4$

Answer: $4$

</details>

---

### Q3. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the domain of the function $f(x)=\log _{\left(10 x^{2}-17 x+7\right)}\left(18 x^{2}-11 x+1\right)$ is $(-\infty, a) \cup(b, c) \cup(d, \infty)-\{e\}$, then $90(a+b+c+d+e)$ equals:

**Options:**

- **(A)** 170
- **(B)** 307
- **(C)** 316
- **(D)** 177

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 316**

**Detailed Solution:**

For $f(x) = \log_{(10x^2-17x+7)}(18x^2-11x+1)$, we need:
Base $> 0$: $10x^2-17x+7 > 0 \Rightarrow 10(x-1)(x-7/10) > 0 \Rightarrow x < 7/10$ or $x > 1$
Base $\neq 1$: $10x^2-17x+6 = 0 \Rightarrow x = 1/2$ or $x = 6/5$
Argument $> 0$: $18x^2-11x+1 > 0 \Rightarrow 18(x-1/2)(x-1/9) > 0 \Rightarrow x < 1/9$ or $x > 1/2$
Intersecting conditions 1 and 3: $(-\infty, 1/9) \cup (1/2, 7/10) \cup (1, \infty)$
Removing base $= 1$ points: $x = 1/2$ is already excluded; $x = 6/5 \in (1,\infty)$ must be removed.
Domain: $(-\infty, 1/9) \cup (1/2, 7/10) \cup (1, \infty) - \{6/5\}$
So $a = 1/9,\; b = 1/2,\; c = 7/10,\; d = 1,\; e = 6/5$.
$90(a+b+c+d+e) = 90\left(\frac{1}{9}+\frac{1}{2}+\frac{7}{10}+1+\frac{6}{5}\right) = 10+45+63+90+108 = 316$

</details>

---

### Q4. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let the domain of the function $f(x)=\log _{3} \log _{5}\left(7-\log _{2}\left(x^{2}-10 x+85\right)\right)+\sin ^{-1}\left(\left|\frac{3 x-7}{17-x}\right|\right)$ be $(\alpha, \beta]$. Then $\alpha+\beta$ is equal to :

**Options:**

- **(A)** 9
- **(B)** 10
- **(C)** 12
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 9**

**Detailed Solution:**

For $\log_3\log_5(\cdot)$ we need $\log_5(\cdot)>0$
So $7-\log_2(x^2-10x+85)>1$, giving $x^2-10x+85<64$
$(x-3)(x-7) < 0$
$\Rightarrow 3 < x < 7$.
For $\sin^{-1}\left(\left|\frac{3x-7}{17-x}\right|\right)$ we need $|3x-7|\leq|17-x|$
i.e, $(x-6)(x+5)\leq 0 \Rightarrow -5\leq x\leq 6$.
Intersection: $(3,6]$, so $\alpha=3,\beta=6$.
$\alpha+\beta=9$

</details>

---

### Q5. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the domain of the function $f(x)=\sin ^{-1}\left(\frac{5-x}{3+2 x}\right)+\frac{1}{\log _{e}(10-x)}$ is $(-\infty, \alpha] \cup[\beta, \gamma)-\{\delta\}$, then $6(\alpha+\beta+\gamma+\delta)$ is equal to

**Options:**

- **(A)** 67
- **(B)** 66
- **(C)** 70
- **(D)** 68

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 70**

**Detailed Solution:**

$-1 \leq \dfrac{5-x}{2x+3} \leq$ & $10 - x > 0$, $10 - x \neq 1$
$\left| \dfrac{5-x}{2x+3} \right| \geq 1$ & $x < 10$ & $x \neq 9$
$(5-x)^2 - (2x+3)^2 \leq 0$ & $x < 10$ & $4x \neq 9$
$(x+8)(3x-2) \geq 0$ & $x < 10$ & $x \neq 9$
$\Rightarrow (-\infty, -8] \cup \left[\dfrac{2}{3}, 10\right) - \{9\}$
$\Rightarrow (\alpha + \beta + \gamma + \delta) = 6\left(-8 + \dfrac{2}{3} + 10 + 9\right)$
$= 70$

</details>

---

### Q6. JEE Main 2025 (8 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the domain of the function
$f(x)=\cos ^{-1}\left(\frac{4 x+5}{3 x-7}\right)$ be $[\alpha, \beta]$ and the domain of $\mathrm{g}(\mathrm{x})=\log _2\left(2-6 \log _{27}(2 \mathrm{x}+5)\right)$ be $(\gamma, \delta)$.
Then $|7(\alpha+\beta)+4(\gamma+\delta)|$ is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **96**

**Detailed Solution:**

$\begin{aligned} & f(x)=\cos ^{-1}\left(\frac{4 x+5}{3 x-7}\right) \\ & \Rightarrow-1 \leq\left(\frac{4 x+5}{3 x-7}\right) \leq 1 \\ & \left(\frac{4 x+5}{3 x-7}\right) \geq-1 \\ & \frac{4 x+5+3 x-7}{3 x-7} \geq 0 \\ & \Rightarrow \frac{7 x-2}{3 x-7} \geq 0\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e7cmqbQ5RPiS1biaoozuX6-b0z2-k44R2eRjdXZNF8k.original.fullsize.png"/>
$\begin{aligned} & x \in\left(-\infty, \frac{2}{7}\right] \cup\left(\frac{7}{3}, \infty\right) \\ & \& \frac{4 x+5}{3 x-7} \leq 1 \Rightarrow \frac{x+12}{3 x-7} \leq 0\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6pVI74YkOIbZm_zwxuHjmrGYN0kZbNBbuQ7Q68v2FiM.original.fullsize.png"/>
$\therefore$ Domain of $f(x)$ is
$\begin{aligned}
& {\left[-12, \frac{2}{7}\right] \alpha=-12, \beta=\frac{2}{7}} \\
& \mathrm{~g}(\mathrm{x})=\log _2\left(2-6 \log _{27}(2 \mathrm{x}+5)\right)
\end{aligned}$
Domain
$2-6 \log _{27}(2 x+5) \gt 0$
$\begin{array}{ll}\Rightarrow & 6 \log _{27}(2 \mathrm{x}+5) \lt 2 \\ \Rightarrow & \log _{27}(2 \mathrm{x}+5) \lt \frac{1}{3} \\ \Rightarrow & 2 \mathrm{x}+5 \lt 3 \\ \Rightarrow & \mathrm{x} \lt -1\end{array}$
$\& 2 x+5 \gt 0 \Rightarrow x \gt -\frac{5}{2}$
Domain is $\mathrm{x} \in\left(-\frac{5}{2},-1\right)$
$\begin{aligned}
& \gamma=-\frac{5}{2}, \delta=-1 \\
& |7(\alpha+\beta)+4(\gamma+\delta)|=\left\lvert\, 7\left(\left.-12+\frac{2}{7}+4\left(-\frac{5}{2}-1\right) \right\rvert\,\right.\right. \\
& |-82-14|=96
\end{aligned}$

</details>

---

### Q7. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the domains of the functions
$\mathrm{f}(\mathrm{x})=\log _4 \log _3 \log _7\left(8-\log _2\left(\mathrm{x}^2+4 \mathrm{x}+5\right)\right)$ and $g(x)=\sin ^{-1}\left(\frac{7 x+10}{x-2}\right)$ be $(\alpha, \beta)$ and $[\gamma, \delta]$, respectively. Then $\alpha^2+\beta^2+\gamma^2+\delta^2$ is equal to :-

**Options:**

- **(A)** $15$
- **(B)** $13$
- **(C)** $16$
- **(D)** $14$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $15$**

**Detailed Solution:**

$\begin{aligned} & \log _3\left(\log _7\left(8-\log _2\left(\mathrm{x}^2+4 \mathrm{x}+5\right)\right)\right) \gt 0 \\ & \log _2\left(\mathrm{x}^2+4 \mathrm{x}+5\right) \lt 1 \\ & \mathrm{x}^2+4 \mathrm{x}+3 \lt 0 \\ & \Rightarrow \mathrm{x} \in(-3,-1) \\ & -1 \leq \frac{7 \mathrm{x}+10}{\mathrm{x}-2} \leq 1 \\ & \Rightarrow \mathrm{x} \in[-2,-1] \\ & \alpha=-3, \beta=-1, \gamma=-2, \delta=-1 \\ & \alpha^2+\beta^2+\gamma^2+\delta^2=15 \\ & \text { option }(1)\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the domain of the function $f(x)=\log _7\left(1-\log _4\left(x^2-9 x+18\right)\right)$ is $(\alpha, \beta) \cup(\gamma, \delta)$, then $\alpha+\beta+\gamma+\delta$ is equal to

**Options:**

- **(A)** $18$
- **(B)** $16$
- **(C)** $15$
- **(D)** $17$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $18$**

**Detailed Solution:**

$\begin{aligned} & \text { Domain } 1-\log _4\left(x^2-9 x+18\right) \gt 0 \\ & \text { Also } x^2-9 x+18 \gt 0 \\ & (x-3)(x-6) \gt 0\end{aligned}$
$x \in(-\infty, 3) \cup(6, \infty)$    ...(1)
$\begin{aligned} & \text { also } x^2-9 x+18 \lt 4 \\ & x^2-9 x+14 \lt 0\end{aligned}$
$x \in(2,7)$   ...(2)
$\begin{aligned} & (1) \cap(2) \quad(2,3) \cup(6,7)=(\alpha, \beta) \cup(\gamma, \delta) \\ & \Rightarrow \alpha+\beta+\gamma+\delta=18\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the domain of the function
$f(x)=\log _e\left(\frac{2 x-3}{5+4 x}\right)+\sin ^{-1}\left(\frac{4+3 x}{2-x}\right) \quad \text { is } \quad[\alpha, \beta)$
then $\alpha^2+4 \beta$ is equal to

**Options:**

- **(A)** $5$
- **(B)** $4$
- **(C)** $3$
- **(D)** $7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4$**

**Detailed Solution:**

Given function is
$f(x)=\log _e\left(\frac{2 x-3}{5+4 x}\right)+\sin ^{-1}\left(\frac{4+3 x}{2-x}\right)$
For domain, the conditions are
$\frac{2 x-3}{5+4 x} \gt 0 \text { and }\left|\frac{4+3 x}{2-x}\right| \leq 1$
Now, $\frac{2 \mathrm{x}-3}{5+4 \mathrm{x}} \gt 0 \Rightarrow \mathrm{x} \in\left(-\infty,-\frac{5}{4}\right) \cup\left[\frac{3}{2}, \infty\right)$
and $\quad-1 \leq \frac{4+3 x}{2-x} \leq 1$
$\Rightarrow\left(-1 \leq \frac{4+3 x}{2-x}\right) \cap\left(\frac{4+3 x}{2-x} \leq 1\right)$
$\Rightarrow\left(\frac{6+2 \mathrm{x}}{2-\mathrm{x}} \geq 0\right) \cap\left(\frac{2+4 \mathrm{x}}{2-\mathrm{x}} \leq 0\right)$
$\begin{aligned} & \Rightarrow \frac{6+2 x}{2-x} \cdot \frac{2+4 x}{2-x} \leq 0 \\ & \Rightarrow x \in\left[-3,-\frac{1}{2}\right]\end{aligned}$
Hence, we get the domain of f as $\mathrm{x} \in\left[-3,-\frac{5}{4}\right)$ This means that $\alpha=-3, \beta=-\frac{5}{4}$ Thus, $\alpha^2+4 \beta=9-5=4$

</details>

---

### Q10. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the domain of the function
$f(x)=\frac{1}{\sqrt{10+3 x-x^2}}+\frac{1}{\sqrt{x+|x|}}$ is $(a, b)$, then $(1+a)^2+b^2$ is equal to :

**Options:**

- **(A)** $26$
- **(B)** $29$
- **(C)** $25$
- **(D)** $30$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $26$**

**Detailed Solution:**

$\mathrm{x}+|\mathrm{x}| \gt 0 \quad \Rightarrow \mathrm{x} \in(0, \infty)$   ...(1)
$\begin{aligned} & \& 10+3 x-x^2 \gt 0 \\ & \Rightarrow x^2-3 x-10 \lt 0\end{aligned}$
$\Rightarrow x \in(-2,5)$   ...(2)
$\begin{aligned} & \text { from }(1) \&(2) \quad \mathrm{x} \in(0,5) \\ & \therefore \mathrm{a}=0 \& \mathrm{~b}=5 \\ & \therefore\left(1+\mathrm{a}^2\right)+\mathrm{b}^2=1+25=26\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the domain of the function $\log _5\left(18 x-x^2-77\right)$ is $(\alpha, \beta)$ and the domain of the function $\log _{(x-1)}\left(\frac{2 x^2+3 x-2}{x^2-3 x-4}\right)$ is $(\gamma, \delta)$, then $\alpha^2+\beta^2+\gamma^2$ is equal to :

**Options:**

- **(A)** 195
- **(B)** 179
- **(C)** 186
- **(D)** 174

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 186**

**Detailed Solution:**

$\begin{aligned} & f_1(x)=\log _5\left(18 x-x^2-77\right) \\ & \therefore \quad 18 x-x^2-77>0 \\ & \quad x^2-18 x+77 < 0 \\ & x \in(7,11) \\ & \alpha=7, \beta=11 \\ & f_2(x)=\log _{(x-1)}\left(\frac{2 x^2+3 x-2}{x^2-3 x-4}\right) \\ & x>1, x-1 \neq 1, \frac{2 x^2+3 x-2}{x^2-3 x-4}>0 \\ & x>1, x \neq 2, \frac{(2 x-1)(x+2)}{(x-4)(x+1)}>0\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0s8b0HsjeC8CA2qvAmp2YmYP512keberVk6VgTprOVE.original.fullsize.png">

$\begin{aligned}
& \therefore \quad x \in(4, \infty) \\
& \therefore \quad \gamma=4 \\
& \therefore \quad \alpha^2+\beta^2+\gamma^2=49+121+16 \\
& =186
\end{aligned}$

</details>

---

### Q12. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $[x]$ denote the greatest integer less than or equal to $x$. Then the domain of $f(x)=\sec ^{-1}(2[x]+1)$ is :

**Options:**

- **(A)** $(-\infty,-1] \cup[0, \infty)$
- **(B)** $(-\infty,-1] \cup[1, \infty)$
- **(C)** $(-\infty, \infty)$
- **(D)** $(-\infty, \infty)-\{0\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(-\infty, \infty)$**

**Detailed Solution:**

$\begin{array}{ll}
f(x)=\sec ^{-1}(2[x]+1) \\
\Rightarrow 2[x]+1 \geq 1 & \text { or } 2[x]+1 \leq-1 \\
\Rightarrow 2[x] \geq 0 & \text { or } 2[x] \leq-2 \\
\Rightarrow[x] \geq 0 & \text { or }[x] \leq-1 \\
\Rightarrow x \geq 0 & \text { or } x \leq 0
\end{array}$
Domain of $f(x)$ is $(-\infty, \infty)$

</details>

---

### Q13. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the domain of the function $f(x)=\sin ^{-1}\left(\frac{x-1}{2 x+3}\right)$ is $\mathbf{R}-(\alpha, \beta)$, then $12 \alpha \beta$ is equal to :

**Options:**

- **(A)** 32
- **(B)** 40
- **(C)** 24
- **(D)** 36

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 32**

**Detailed Solution:**

Domain of $f(x)=\sin ^{-1}\left(\frac{x-1}{2 x+3}\right)$ is
$\begin{aligned}
& 2 x+3 \neq 0 \& x \neq \frac{-3}{2} \text { and }\left|\frac{(x-1)}{2 x+3}\right| \leq 1 \\
& |x-1| \leq|2 x+3|
\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/OkE4iMeQTtMyxIVV_CzlE2otwc_q_uu2dNbLNcCRc8E.original.fullsize.png">
$\begin{aligned} & \text { For }|2 x+3| \geq|x-1| \\ & x \in(-\infty,-4] \cup\left(-\frac{2}{3}, \infty\right) \\ & \alpha=-4 \& \beta=-\frac{2}{3}: 12 \alpha \beta=32\end{aligned}$

</details>

---

### Q14. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the domain of the function $\sin ^{-1}\left(\frac{3 x-22}{2 x-19}\right)+\log _{\mathrm{e}}\left(\frac{3 x^2-8 x+5}{x^2-3 x-10}\right)$ is $(\alpha, \beta]$, then $3 \alpha+10 \beta$ is equal to:

**Options:**

- **(A)** 100
- **(B)** 95
- **(C)** 97
- **(D)** 98

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 97**

**Detailed Solution:**

$\begin{array}{ll}
-1 \leq \frac{3 x-22}{2 x-19} \leq 1 & \frac{3 x^2-8 x+5}{x^2-3 x-10}>0 \\
x \in\left(5, \frac{41}{5}\right] & \\
3 \alpha+10 \beta=97 &
\end{array}$

</details>

---

### Q15. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>25</mn></msqrt><mfenced><mrow><mn>4</mn><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mo>+</mo><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>−</mo><mn>15</mn></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>−</mo><mi>∞</mi><mo>,</mo><mi>α</mi></mrow></mfenced><mo>∪</mo><mfenced open="["><mrow><mi>β</mi><mo>,</mo><mi>∞</mi></mrow></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>3</mn></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>140</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>175</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>125</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>25</mn></msqrt><mrow><mn>4</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>log</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>15</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>25</mn><mo>≥</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>≥</mo><mn>0</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6fa9cb25-54c6-4b13-b6eb-43b6b7bc0681.png" style="width: 405px; height: 118px;"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>∈</mo><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mo>-</mo><mn>5</mn><mo>]</mo><mo>∪</mo><mo>[</mo><mn>5</mn><mo>,</mo><mo>∞</mo><mo>)</mo><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>≠</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>≠</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>15</mn><mo>&gt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&gt;</mo><mn>0</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d54eaf17-6382-454b-93a7-5fb9b519a1b3.png" style="width: 404px; height: 115px;"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>∈</mo><mfenced><mrow><mo>-</mo><mo>∞</mo><mo>,</mo><mo>-</mo><mn>5</mn></mrow></mfenced><mo>∪</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>∞</mo></mrow></mfenced><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f964e1ce-17fa-4961-a92b-ed2f16aa59e9.png" style="width: 409px; height: 133px;"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>∈</mo><mfenced><mrow><mo>-</mo><mo>∞</mo><mo>,</mo><mo>-</mo><mn>5</mn></mrow></mfenced><mo>∪</mo><mo>[</mo><mn>5</mn><mo>,</mo><mo>∞</mo><mo>)</mo></math></p><p>So, on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mfenced><mrow><mo>-</mo><mo>∞</mo><mo>,</mo><mi>α</mi></mrow></mfenced><mo>∪</mo><mo>[</mo><mi>β</mi><mo>,</mo><mo>∞</mo><mo>)</mo></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>3</mn></msup><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>5</mn></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>3</mn></msup><mo>=</mo><mn>150</mn></math></p>

</details>

---

### Q16. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>α</mi><mo>,</mo><mi>β</mi><mo>]</mo></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>β</mi><mo>-</mo><mn>4</mn><mi>α</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced></math></p><p>Now, using the definition of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi></math> function and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> function we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfrac><mo>&gt;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>≤</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>≤</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mo>(</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac><mo>&gt;</mo><mn>0</mn><mo>,</mo><mo> </mo><mfrac><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>≥</mo><mn>0</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>≤</mo><mn>0</mn></math></p><p> </p><p>Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mo>(</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac><mo>&gt;</mo><mn>0</mn></math> we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/776375c9-fbd1-4cd2-83d9-8d67d158cbe6.png" style="width: 150px; height: 50px;"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>∈</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>∪</mo><mfenced><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mo>∞</mo></mrow></mfenced><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Similarly for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>≥</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>∪</mo><mfenced open="["><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>,</mo><mo>∞</mo></mrow></mfenced><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>And for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>≤</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>]</mo><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now, taking intersection of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>∩</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>∩</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mn>3</mn><mo>]</mo></math></p><p>So, on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>α</mi><mo>,</mo><mi>β</mi><mo>]</mo></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo> </mo><mo>&amp;</mo><mo> </mo><mi>β</mi><mo>=</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>β</mi><mo>-</mo><mn>4</mn><mi>α</mi><mo>=</mo><mn>15</mn><mo>-</mo><mn>3</mn><mo>=</mo><mn>12</mn></math></p></blockquote>

</details>

---

### Q17. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mo>-</mo><mo>|</mo><mi>x</mi><mo>|</mo></mrow><mn>4</mn></mfrac></mfenced><mo>+</mo><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mn>3</mn><mo>-</mo><mi>x</mi><mo>)</mo></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mi>α</mi><mo>,</mo><mi>β</mi><mo>)</mo><mo>-</mo><mo>{</mo><mi>γ</mi><mo>}</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="|" open="|"><mfrac><mrow><mn>2</mn><mo>-</mo><mfenced close="|" open="|"><mi>x</mi></mfenced></mrow><mn>4</mn></mfrac></mfenced><mo>+</mo><mi>log</mi><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>1</mn><mo>≤</mo><mfenced close="|" open="|"><mfrac><mrow><mn>2</mn><mo>-</mo><mfenced close="|" open="|"><mi>x</mi></mfenced></mrow><mn>4</mn></mfrac></mfenced><mo>≤</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>4</mn><mo>≤</mo><mn>2</mn><mo>-</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>≤</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>6</mn><mo>≤</mo><mo>-</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>≤</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>2</mn><mo>≤</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>≤</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>≤</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>6</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>6</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo><mi>x</mi><mo>&gt;</mo><mn>0</mn><mo> </mo><mtext>and</mtext><mo> </mo><mn>3</mn><mo>-</mo><mi>x</mi><mo>≠</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>≠</mo><mn>2</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&lt;</mo><mn>3</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>∈</mo><mo>[</mo><mo>-</mo><mn>6</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>-</mo><mfenced close="}" open="{"><mn>2</mn></mfenced></math></p><p>So, on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mo>[</mo><mo>-</mo><mi>α</mi><mo>,</mo><mi>β</mi><mo>)</mo><mo>-</mo><mfenced close="}" open="{"><mi>γ</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mi>β</mi><mo>+</mo><mi>γ</mi><mo>=</mo><mn>6</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>11</mn></math></p>

</details>

---

### Q18. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>:</mo><mi mathvariant="normal">R</mi><mo>-</mo><mfenced close="}" open="{"><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mo>→</mo><mi mathvariant="normal">R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mo>:</mo><mi mathvariant="normal">R</mi><mo>-</mo><mfenced close="}" open="{"><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mn>2</mn></mfrac></mfenced><mo>→</mo><mi mathvariant="normal">R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfrac><mrow><mo>|</mo><mi mathvariant="normal">x</mi><mo>|</mo><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>5</mn></mrow></mfrac></math>. Then the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>fog</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mfrac><mn>7</mn><mn>4</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>7</mn><mn>4</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced close="|" open="|"><mi mathvariant="normal">x</mi></mfenced><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>5</mn></mrow></mfrac></math>.</p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>≠</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mfenced close="|" open="|"><mi mathvariant="normal">x</mi></mfenced><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>5</mn></mrow></mfrac><mo>≠</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p>Case-I: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>≥</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mfrac><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mo>-</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi mathvariant="normal">x</mi><mo>=</mo><mo>-</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>7</mn></mrow><mn>4</mn></mfrac><mo>→</mo><mtext>Rejected as</mtext><mo> </mo><mi mathvariant="normal">x</mi><mo>≥</mo><mn>0</mn></math></p><p>Case-I: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&lt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mo>-</mo><mi mathvariant="normal">x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mo>-</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mo>=</mo><mo>-</mo><mn>5</mn><mo>→</mo><mtext>Not possible</mtext></math></p><p>So, domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mrow><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced><mo>=</mo></math>domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mtext>Domain of</mtext><mo> </mo><mi>fog</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>=</mo><mi mathvariant="normal">R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q19. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>10</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow><mn>3</mn></mfrac></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>]</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn><mfenced open="|" close="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>54</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>log</mi><mfenced><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>10</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow><mn>3</mn></mfrac></mfenced></math></p><p>We know that the domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>B</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>C</mi><mfenced><mi>x</mi></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mfenced><mi>A</mi></mfenced><mo>&#8745;</mo><mi>D</mi><mfenced><mi>B</mi></mfenced><mo>&#8745;</mo><mi>D</mi><mfenced><mi>C</mi></mfenced></math>.</p><p>Let us find the domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced></math>.</p><p>We know that domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>6</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>6</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p>Domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>9</mn></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>.</p><p>Let us find the domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Let us find the domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>10</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow><mn>3</mn></mfrac></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mrow><mn>10</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow><mn>3</mn></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>3</mn><mo>&#8804;</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>6</mn><mo>&#8804;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>9</mn></mrow><mn>10</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>10</mn></mfrac></math>.</p><p>Now the common domain is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p>But given that the domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>36</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>36</mn><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>4</mn></mfrac><mo>+</mo><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>36</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>36</mn><mo>&#215;</mo><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>36</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>45</mn></math></p><p>Therefore, the required answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn></math>.</p></blockquote>

</details>

---

### Q20. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><msup><mfenced open="[" close="]"><mi>x</mi></mfenced><mn>2</mn></msup><mo>-</mo><mn>3</mn><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>-</mo><mn>10</mn></msqrt></mfrac></math> is (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn><mo>]</mo><mo>&#8746;</mo><mo>(</mo><mn>5</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>&#8746;</mo><mo>[</mo><mn>6</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>5</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn><mo>]</mo><mo>&#8746;</mo><mo>[</mo><mn>6</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>&#8746;</mo><mo>[</mo><mn>6</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><msup><mfenced close="]" open="["><mi>x</mi></mfenced><mn>2</mn></msup><mo>-</mo><mn>3</mn><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mn>10</mn></msqrt></mfrac></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> to be defined,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="]" open="["><mi>x</mi></mfenced><mn>2</mn></msup><mo>-</mo><mn>3</mn><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mn>10</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><mo>-</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>&#60;</mo><mo>-</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>&#62;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>6</mn></math></p><p>So, domain is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#8746;</mo><mo>[</mo><mn>6</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>.</p>

</details>

---

### Q21. JEE Main 2023 (10 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

If the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mi>&#947;</mi><mo>,</mo><mi>&#948;</mi><mo>]</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>10</mn><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mo>+</mo><mn>21</mn><mi>&#948;</mi></mrow></mfenced></math> is equal to __________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **24**

**Detailed Solution:**

<blockquote><p>We know that,</p><p>Domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn><mo>]</mo><mo>&#8746;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8804;</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8805;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>+</mo><mn>1</mn><mo>&#8804;</mo><mn>0</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>-</mo><mn>1</mn><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>7</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>7</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mo>-</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mo>]</mo></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#948;</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>7</mn></mfrac></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>10</mn><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mo>+</mo><mn>21</mn><mi>&#948;</mi></mrow></mfenced><mspace linebreak="newline"/><mo>=</mo><mfenced open="|" close="|"><mrow><mo>-</mo><mn>3</mn><mo>-</mo><mn>6</mn><mo>-</mo><mn>6</mn><mo>-</mo><mn>9</mn></mrow></mfenced><mspace linebreak="newline"/><mo>=</mo><mn>24</mn></math></p><p>Hence this is the required answer.</p></blockquote>

</details>

---

### Q22. JEE Main 2023 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

If domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mi>&#947;</mi><mo>,</mo><mi>&#948;</mi></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#947;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#948;</mi><mn>2</mn></msup></mrow></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

<blockquote><p>We need to find the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math>
Now From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>(</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow></mfrac><mo>&#62;</mo><mn>0</mn></math></p><p>Now we get the common region here as
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> we get that
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac><mo>&#8805;</mo><mo>-</mo><mn>1</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> we get
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac><mo>+</mo><mn>1</mn><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac><mo>,</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">b</mi></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math> we get
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>9</mn></mrow><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mfenced><mn>2</mn></mfenced><mfenced><mn>9</mn></mfenced><mo>&#60;</mo><mn>0</mn><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mn>2</mn><mo>&#62;</mo><mn>0</mn></math>, we observe that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>9</mn><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn><mo>&#160;&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>9</mn><mo>&#62;</mo><mn>0</mn><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">c</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> Intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">b</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo></math> gives us
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced></math>.</p><p>On comparing this with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mi>&#947;</mi><mo>,</mo><mi>&#948;</mi></mrow></mfenced></math>,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#947;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#948;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>10</mn><mn>9</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>18</mn><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#947;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#948;</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>20</mn></math>.</p><p>Hence this is the required answer.</p></blockquote>

</details>

---

### Q23. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msub><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><msup><mi>e</mi><mrow><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></msup><mo>-</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8477;</mi><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>3</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>3</mn></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8477;</mi><mo>-</mo><mfenced open="{" close="}"><mn>3</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>3</mn></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p>Function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msub><mi>log</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></msub><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><msup><mi>e</mi><mrow><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></msup><mo>-</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>To find domain we will take following cases:</p><p>Case-1:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>&#62;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p>Case-2:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>&#62;</mo><mo>-</mo><mn>1</mn></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#8800;</mo><mn>1</mn><mo>&#8658;</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p>Case-3:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p>Case-4:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mi>x</mi></mfenced></mrow></msup><mo>-</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>case&#160;</mtext><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>&#8745;</mo><mo>&#160;</mo><mtext>case&#160;</mtext><mo>(</mo><mn>2</mn><mo>)</mo><mo>&#160;</mo><mo>&#8745;</mo><mo>&#160;</mo><mtext>case&#160;</mtext><mo>(</mo><mn>3</mn><mo>)</mo><mo>&#160;</mo><mo>&#8745;</mo><mo>&#160;</mo><mtext>case&#160;</mtext><mo>(</mo><mn>4</mn><mo>)</mo></math> we get,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mn>3</mn></mfenced></math></p>

</details>

---

### Q24. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn></mrow></mfrac></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>]</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mn>2</mn><mo>]</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn></mrow></mfrac></mfenced></math></p><p>We know that domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn></mrow></mfrac><mo>&#8805;</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn></mrow></mfrac><mo>&#8805;</mo><mo>-</mo><mn>1</mn></math></p><p>Since denominator <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn></math> is always positive,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#8805;</mo><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>9</mn><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>x</mi><mo>&#8805;</mo><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8805;</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>So from equation  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> we get domain <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math></p></blockquote>

</details>

---

### Q25. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Considering only the principal values of the inverse trigonometric functions, the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced></math></p><p>We know that domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mtext>is&#160;</mtext><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>&#8804;</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mn>0</mn></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math> as its discriminant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#60;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>&#8805;</mo><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math></p></blockquote>

</details>

---

### Q26. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced open="[" close="]"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msub><mi>log</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msub><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced></mrow></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>t</mi></mfenced></math> is the greatest integer function, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><msqrt><mfrac><mn>5</mn><mn>2</mn></mfrac></msqrt><mo>,</mo><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mn>1</mn><mo>,</mo><mfrac><mrow><mn>5</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msub><mi>log</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msub><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced></mrow></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> to be defined</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfenced close="]" open="["><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mo>&#60;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#60;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>&#60;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><msqrt><mfrac><mn>5</mn><mn>2</mn></mfrac></msqrt><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><msqrt><mfrac><mn>5</mn><mn>2</mn></mfrac></msqrt></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mfenced><mfrac><mrow><mn>5</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mrow><mn>5</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msub><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>&#60;</mo><mn>0</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p></blockquote>

</details>

---

### Q27. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced></mrow><mi>&#960;</mi></mfrac></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>&#8746;</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>&#8746;</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>&#8746;</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced></mrow><mi>&#960;</mi></mfrac></mfenced></math></p><p>Case I: <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mn>1</mn><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>&#8805;</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8805;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mo>&#177;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>&#8746;</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math></p><p>Case II: <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mrow><mn>2</mn><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced></mrow><mi>&#960;</mi></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>&#8804;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>&#8804;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math> which is always true.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>&#8746;</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math></p>

</details>

---

### Q28. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn></mrow></mfrac></mfenced></mrow><mrow><mi>log</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mn>3</mn></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>3</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mn>2</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>3</mn></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mn>2</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>3</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mn>3</mn></mfenced></math>**

**Detailed Solution:**

<p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> is defined when <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#10877;</mo><mi>x</mi><mo>&#10877;</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn></mrow></mfrac></mfenced></math> is defined when</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#10877;</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn></mrow></mfrac><mo>&#10877;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mo>&#8800;</mo><mn>0</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mo>&#177;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mo>&#177;</mo><mn>3</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn><mo>-</mo><mn>5</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mo>&#177;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mn>1</mn><mo>-</mo><mfrac><mn>5</mn><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mo>&#177;</mo><mn>3</mn></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mo>-</mo><mfrac><mn>5</mn><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#10877;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mo>&#177;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#8804;</mo><mfrac><mn>5</mn><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#10877;</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mo>&#177;</mo><mn>3</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>&#8805;</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mo>&#177;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mo>&#177;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mn>3</mn></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now, we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced><mi>x</mi></mfenced></math> is defined for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math> is defined for <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#62;</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#62;</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mn>1</mn><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p>from equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0a4305a5-eeea-47d7-a0ce-722514312221-image.png" style="width: 250px; height: 120px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mn>3</mn></mfenced></math></p>

</details>

---

### Q29. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The domain of the function, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math>**

**Detailed Solution:**

<p>The domain of the function</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math> </p><p>For, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#8804;</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>For, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>&#8804;</mo><mn>1</mn><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>&#8804;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#8804;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>1</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>&#8804;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfenced><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>]</mo><mo>&#8746;</mo><mfenced open="["><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo></mrow></mfenced><mo>&#160;</mo><mo>-</mo><mfenced open="{" close="}"><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#8804;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>1</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></mfenced></math> from the equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math></p><p>Now the domain of the given function will be the intersection of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math></p><p>Hence, domain is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mo>{</mo><mn>0</mn><mo>}</mo></math></p>

</details>

---

### Q30. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>cosec</mo><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mi>x</mi></mfrac></mfenced></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mo>{</mo><mn>0</mn><mo>}</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mo>{</mo><mn>0</mn><mo>}</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mo>{</mo><mn>0</mn><mo>}</mo></math>**

**Detailed Solution:**

Domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>e</mi><msup><mi>c</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8804;</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mi>o</mi><mi>r</mi><mo>&#160;</mo><mi>x</mi><mo>&#8805;</mo><mn>1</mn></math> <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mi>x</mi></mfrac><mo>&#8804;</mo><mo>-</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mi>x</mi></mfrac><mo>&#8805;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>x</mi></mrow><mi>x</mi></mfrac><mo>&#8804;</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>-</mo><mi>x</mi></mrow><mi>x</mi></mfrac><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mi>x</mi></mfrac><mo>&#8804;</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>&#8805;</mo><mn>0</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/56074de8-543d-46fe-b53d-e1b48ae27058-image.png" style="width: 464px; height: 74px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mn>0</mn></mrow></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>-</mo><mo>{</mo><mn>0</mn><mo>}</mo></math></p>

</details>

---

### Q31. JEE Main 2021 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>log</mi><mn>4</mn></msub><mfenced><mrow><msub><mi>log</mi><mn>5</mn></msub><mfenced><mrow><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><mn>18</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>77</mn></mrow></mfenced></mrow></mfenced></mrow></mfenced></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math>. Then the value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mfrac><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi></mrow><mfenced><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mn>3</mn></msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced></mfrac></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>For domain <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>5</mn></msub><mfenced><mrow><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><mn>18</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>77</mn></mrow></mfenced></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><mn>18</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>77</mn></mrow></mfenced><mo>&#62;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>18</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>77</mn><mo>&#62;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>18</mn><mi>x</mi><mo>+</mo><mn>80</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>8</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mfrac><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mn>3</mn></msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Apply <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mi>f</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mi>a</mi><mi>b</mi></msubsup><mfrac><mrow><msup><mi>sin</mi><mn>3</mn></msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mn>3</mn></msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>I</mi><mo>=</mo><mfenced><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow><mn>2</mn></mfrac><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mn>8</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mrow><mn>10</mn><mo>-</mo><mn>8</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q32. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mrow><msqrt><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mstyle></mfenced></msqrt></mfrac></math> is the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>]</mo><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given function is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt></mrow><msqrt><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mstyle></mfenced></msqrt></mfrac></math></p><p>For, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>cos</mi><mn>1</mn></msup><mi>x</mi></math> to be defined <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn></math> and for <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>f</mi><mfenced><mi>x</mi></mfenced></msqrt></math> to be defined <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8805;</mo><mn>0</mn></math> and the denominator of any expression can never be zero.</p><p>Thus, to define the domain of the given function, we have </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></msqrt><mo>&#8804;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#8805;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>Taking the common values and using the range of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> i.e. for positive values <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>&#8804;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#8804;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>]</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#60;</mo><mn>2</mn><mi>x</mi><mo>&#8804;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p>Now, taking intersection, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p>Given, domain of the function is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfenced close="]"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q33. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denote the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>. If the domain of the real valued function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><mfrac><mrow><mfenced close="|" open="|"><mfenced close="]" open="["><mi>x</mi></mfenced></mfenced><mo>-</mo><mn>2</mn></mrow><mrow><mfenced close="|" open="|"><mfenced close="]" open="["><mi>x</mi></mfenced></mfenced><mo>-</mo><mn>3</mn></mrow></mfrac></msqrt></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mi>a</mi></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mn>4</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>,</mo><mi>a</mi><mo>&#60;</mo><mi>b</mi><mo>&#60;</mo><mi>c</mi></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

We have,<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msqrt><mfrac><mrow><mfenced open="|" close="|"><mfenced open="[" close="]"><mi>x</mi></mfenced></mfenced><mo>-</mo><mn>2</mn></mrow><mrow><mfenced open="|" close="|"><mfenced open="[" close="]"><mi>x</mi></mfenced></mfenced><mo>-</mo><mn>3</mn></mrow></mfrac></msqrt></math></p><p>For domain,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><mfenced open="|" close="|"><mfenced open="[" close="]"><mi>x</mi></mfenced></mfenced><mo>-</mo><mn>2</mn></mrow><mrow><mfenced open="|" close="|"><mfenced open="[" close="]"><mi>x</mi></mfenced></mfenced><mo>-</mo><mn>3</mn></mrow></mfrac></mfenced><mo>&#8805;</mo><mn>0</mn></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>:</mo></math> When <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>|</mo><mo>-</mo><mn>2</mn><mo>&#8805;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mfenced open="[" close="]"><mi>x</mi></mfenced></mfenced><mo>-</mo><mn>3</mn><mo>&#62;</mo><mn>0</mn></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi mathvariant="normal">x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mn>4</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi><mo>:</mo></math> When <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mfenced open="[" close="]"><mi>x</mi></mfenced></mfenced><mo>-</mo><mn>2</mn><mo>&#8804;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mfenced open="[" close="]"><mi>x</mi></mfenced></mfenced><mo>-</mo><mn>3</mn><mo>&#60;</mo><mn>0</mn></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="["><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>So, from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get</p><p>Domain of function is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mn>4</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>3</mn><mo>+</mo><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mi>a</mi><mo>&#60;</mo><mi>b</mi><mo>&#60;</mo><mi>c</mi></mrow></mfenced></math></p>

</details>

---

### Q34. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the functions are defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msqrt><mi>x</mi></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>,</mo></math> then what is the common domain of the following functions: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>+</mo><mi>g</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi><mo>-</mo><mi>g</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi><mo>/</mo><mi>g</mi><mo>,</mo><mo>&#160;</mo><mi>g</mi><mo>/</mo><mi>f</mi><mo>,</mo><mo>&#160;</mo><mi>g</mi><mo>-</mo><mi>f</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>f</mi><mo>&#177;</mo><mi>g</mi></mrow></mfenced><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#177;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>,</mo><mfenced><mrow><mi>f</mi><mo>/</mo><mi>g</mi></mrow></mfenced><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mrow><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfrac></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msqrt><mi>x</mi></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>,</mo></math> domain <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msqrt><mi>x</mi></msqrt><mo>-</mo><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>,</mo></math> domain <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><mo>-</mo><msqrt><mi>x</mi></msqrt><mo>,</mo></math> domain <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mrow><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><msqrt><mi>x</mi></msqrt><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt></mfrac><mo>,</mo></math> domain <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt><msqrt><mi>x</mi></msqrt></mfrac><mo>,</mo></math> domain <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>]</mo></math></p><p>So, common domain is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q35. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The real valued function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mo>cosec</mo><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><msqrt><mi>x</mi><mo>-</mo><mo>[</mo><mi>x</mi><mo>]</mo></msqrt></mfrac><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>x</mi></mfenced></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo></math> is defined for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> belonging to:</p>

**Options:**

- **(A)** all reals except integers
- **(B)** all non-integers except the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** all integers except <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></math>
- **(D)** all reals except the Interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) all non-integers except the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mo>cosec</mo><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><msqrt><mo>{</mo><mi>x</mi><mo>}</mo></msqrt></mfrac></math></p><p>Domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cosec</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn><mo>]</mo><mo>&#8746;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math></p><p>We know, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi>x</mi><mo>}</mo><mo>&#8800;</mo><mn>0</mn><mo>,</mo></math> so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo></math>integers. </p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> belongs to all non-integers except the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>.</mo><mo>&#160;</mo></math></p>

</details>

---

### Q36. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>6</mn></mrow></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn></mrow></munder><mi>g</mi><mfenced><mi>x</mi></mfenced></math>, then the domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn><mo>]</mo><mo>&#8746;</mo><mo>[</mo><mn>2</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>]</mo><mo>&#8746;</mo><mfenced open="["><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>]</mo><mo>&#8746;</mo><mfenced open="["><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>]</mo><mo>&#8746;</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>]</mo><mo>&#8746;</mo><mfenced open="["><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>**

**Detailed Solution:**

<p>Domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow></mfenced><mo>&#8804;</mo><mn>1</mn><mo>,</mo><mi>g</mi><mfenced><mn mathvariant="italic">2</mn></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>6</mn></mrow></mfrac></mfenced><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></mfenced><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8805;</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8804;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8805;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>2</mn><mo>]</mo><mo>&#8746;</mo><mfenced open="["><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p>

</details>

---

### Q37. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The domain of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mstyle mathvariant="italic"><mo>(</mo><mi>x</mi><mo>)</mo></mstyle><mo>=</mo><msup><mi>sin</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>+</mo><mn>5</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mo>&#8722;</mo><mo>&#8734;</mo><mo>,</mo><mo>&#160;</mo><mo>&#8722;</mo><mi>a</mi></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>17</mn></msqrt><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>&#8722;</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>17</mn></msqrt></mrow><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>17</mn></msqrt><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>17</mn></msqrt></mrow><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>+</mo><mn>5</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtable columnalign="left"><mtr><mtd><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mrow><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>+</mo><mn>5</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#8804;</mo><mn>1</mn></mtd></mtr></mtable><mo>,</mo><mo>&#160;</mo><mo>&#8757;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mi>for</mi><mo>&#160;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> to exist.</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mn>5</mn><mo>&#8805;</mo><mn>0</mn></math>, true for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>.</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mn>5</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>-</mo><mn>4</mn><mo>&#8805;</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mi>t</mi><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>-</mo><mn>4</mn><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mrow></mfenced><mfenced><mrow><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>-</mo><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>a</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>17</mn></msqrt></mrow><mn>2</mn></mfrac></math></p>

</details>

---

### Q38. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The domain of the definition of the function <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mn>10</mn></mrow></msub><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mi>x</mi></mrow></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>1,</mn><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>&#8734;</mi></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>)</mo><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>&#8734;</mi></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>&#8734;</mi></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>&#8734;</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>1,</mn><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>&#8734;</mi></mrow></mfenced></math>**

**Detailed Solution:**

<p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>10</mn></msub><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is defined when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math> and for a fraction to be defined its denominator must be non-zero.</p><p>Thus, the given function is defined only when</p><p><math><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math> and <math><mn>4</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>&#8800;</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mi>x</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math> and <math><mi>x</mi><mo>&#8800;</mo><mn>2</mn><mo>,</mo><mtext>&#8201;</mtext><mo>-</mo><mn>2</mn></math></p><p>The wavy curve for the inequality is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/112b9cbf-fe11-4dbe-8cb4-6509ffcfb09b-image9.png" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn><mo>.</mo></math></p><p>Hence, domain is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q39. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Statement 1: If $A$ and $B$ be two sets having $p$ and $q$ elements respectively, where $q>p$. Then the total number of functions from set $A$ to set $B$ is $q^p$
Statement 2: The total number of selections of $p$ different objects out of $q$ objects is ${ }^q \mathrm{C}_p$.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is false.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation of Statement 1.
- **(C)** Statement 1 is false, Statement 2 is true
- **(D)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation of Statement 1.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation of Statement 1.**

**Detailed Solution:**

Statement-1: $n(A)=p, n(B)=q, q>p$
Total number of functions from $A \rightarrow B=q^p$ It is a true statement.
Statement - 2 : The total number of selections of $p$ different objects out of $q$ objects is ${ }^q \mathrm{C}_p$.
It is also a true statement and it is a correct explanation for statement $-1$ also.

</details>

---

### Q40. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `2`

The domain of the function $f(x)=\frac{1}{\sqrt{|x|-x}}$ is

**Options:**

- **(A)** $(0, \infty)$
- **(B)** $(-\infty, 0)$
- **(C)** $(-\infty, \infty)-\{0\}$
- **(D)** $(-\infty, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(-\infty, 0)$**

**Detailed Solution:**

$\frac{1}{\sqrt{|x|-x}} \Rightarrow|x|-x>0 \Rightarrow|x|>x \Rightarrow x$ is negative
$x \in(-\infty, 0)$

</details>

---

### Q41. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `3`

The largest interval lying in $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ for which the function $\left[f(x)=4^{-x^2}+\cos ^{-1}\left(\frac{x}{2}-1\right)+\log (\cos x)\right]$ is defined, is

**Options:**

- **(A)** $[0, \pi]$
- **(B)** $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$
- **(C)** $\left[-\frac{\pi}{4}, \frac{\pi}{2}\right)$
- **(D)** $\left[0, \frac{\pi}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[0, \frac{\pi}{2}\right)$**

**Detailed Solution:**

$f(x)$ is defined if $-1 \leq \frac{x}{2}-1 \leq 1$ and $\cos x>0$ 
or $0 \leq x \leq 4$ and $-\frac{\pi}{2} < x < \frac{\pi}{2}$
$\therefore \mathrm{x} \in\left[0, \frac{\pi}{2}\right) \text {. }$

</details>

---

### Q42. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

The domain of the function $f(x)=\frac{\sin ^{-1}(x-3)}{\sqrt{9-x^2}}$ is

**Options:**

- **(A)** $[2,3]$
- **(B)** $[2,3)$
- **(C)** $[1,2]$
- **(D)** $[1,2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $[2,3)$**

**Detailed Solution:**

$9-x^2>0$ and $-1 \leq x-3 \leq 1 \Rightarrow x \in[2,3)$

</details>

---

### Q43. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

Domain of definition of the function $f(x)=\frac{3}{4-x^2}+\log _{10}\left(x^3-x\right)$, is

**Options:**

- **(A)** $(-1,0) \cup(1,2) \cup(2, \infty)$
- **(B)** $(0,2)$
- **(C)** $(-1,0) \cup(0,2)$
- **(D)** $(1,2) \cup(2, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-1,0) \cup(1,2) \cup(2, \infty)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/RIPqVuQnbfjh_QLZJf3hkRIsSPiMVmWq3Qfg35MlbQY.original.fullsize.png">

$f(x)=\frac{3}{4-x^2}+\log _{10}\left(x^3-x\right)$
$4-x^2 \neq 0 ; x^3-x>0 ; x \neq \pm \sqrt{4}$
$\therefore \mathrm{D}=(-1,0) \bigcup(1, \infty)-\{\sqrt{4}\}$
$\mathrm{D}=(-1,0) \bigcup(1,2) \bigcup(2, \infty)$

</details>

---

### Q44. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

The domain of $\sin ^{-1}\left[\log _3(x / 3)\right]$ is

**Options:**

- **(A)** [1, 9]
- **(B)** [-1,9]
- **(C)** [-9, 1]
- **(D)** [-9, -1]

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) [1, 9]**

**Detailed Solution:**

$f(x)=\sin ^{-1}\left(\log _3\left(\frac{x}{3}\right)\right)$ exists if
$-1 \leq \log _3\left(\frac{x}{3}\right) \leq 1 \Leftrightarrow 3^{-1} \leq \frac{x}{3} \leq 3^1 \Leftrightarrow 1 \leq x \leq 9$ or $x \in[1,9]$

</details>

---

